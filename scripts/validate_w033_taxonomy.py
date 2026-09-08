#!/usr/bin/env python3
"""Validate W033 corpus, taxonomy, provenance, uncertainty, and lineage candidates."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
from validate_w032_content_model import validate_model, validate_schema  # noqa: E402


def load(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_check(script: str, errors: list[str]) -> None:
    result = subprocess.run([sys.executable, str(ROOT / script), "--check"], cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        errors.append(result.stderr.strip() or result.stdout.strip() or f"{script} check failed")


def main() -> int:
    errors: list[str] = []
    corpus = load("site/data/source/w033/content-corpus.json")
    corpus_schema = load("site/data/schema/content-corpus.schema.json")
    taxonomy = load("site/data/source/w033/taxonomy.json")
    model = load("site/src/lib/data/generated/content-model.json")
    proposal_2011 = load("site/data/source/w033/agent-2011-proposals.json")
    proposal_2023 = load("site/data/source/w033/agent-2023-proposals.json")

    errors.extend(validate_schema(corpus, corpus_schema, corpus_schema, "corpus"))
    errors.extend(validate_model(model))
    run_check("scripts/build_w033_content_corpus.py", errors)
    run_check("scripts/build_w033_taxonomy.py", errors)
    run_check("scripts/build_w032_site_data.py", errors)

    sources = corpus["sources"]
    if len(sources) != 52 or Counter(item["curriculum_id"] for item in sources) != {"curriculum-2011": 12, "curriculum-2023": 40}:
        errors.append("unexpected W033 corpus coverage")
    if Counter(item["occurrence_eligible"] for item in sources) != {True: 49, False: 3}:
        errors.append("unexpected corpus eligibility distribution")
    corpus_by_path = {item["document"]["repository_path"]: item for item in sources}
    for item in sources:
        path = ROOT / item["document"]["repository_path"]
        if not path.is_file() or path.is_symlink() or digest(path) != item["document"]["sha256"]:
            errors.append(f"invalid corpus source file: {item['id']}")
        if item["component_instance_id"] not in {component["id"] for component in model["factual"]["component_instances"]}:
            errors.append(f"corpus source has missing component: {item['id']}")

    proposal_count = 0
    eligible_proposal_count = 0
    for source in proposal_2011["source_documents"]:
        item = corpus_by_path.get(source["source_path"])
        if not item:
            errors.append(f"2011 proposal source is outside corpus: {source['document_id']}")
            continue
        available = "\n".join(section["text"] for section in item["sections"])
        for topic in source["proposed_topics"]:
            proposal_count += 1
            eligible_proposal_count += int(item["occurrence_eligible"])
            if topic["supporting_excerpt"] not in available:
                errors.append(f"2011 excerpt not found: {source['document_id']} / {topic['label']}")
    for source in proposal_2023["sources"]:
        item = corpus_by_path.get(source["source_path"])
        if not item:
            errors.append(f"2023 proposal source is outside corpus: {source['source_document_id']}")
            continue
        available = "\n".join(section["text"] for section in item["sections"])
        for topic in source["topic_proposals"]:
            proposal_count += 1
            eligible_proposal_count += int(item["occurrence_eligible"])
            if topic["supporting_excerpt"] not in available:
                errors.append(f"2023 excerpt not found: {source['source_document_id']} / {topic['proposed_label_pt']}")
    if proposal_count != 260 or eligible_proposal_count != 242:
        errors.append(f"proposal coverage mismatch: total={proposal_count}, eligible={eligible_proposal_count}")

    domains = {item["id"] for item in taxonomy["content_domains"]}
    topics = {item["id"]: item for item in taxonomy["content_topics"]}
    occurrences = {item["id"]: item for item in taxonomy["topic_occurrences"]}
    evidence = {item["id"]: item for item in taxonomy["evidence"]}
    document_ids = {item["id"] for item in model["factual"]["documents"]}
    if len(domains) != 18 or len(topics) != 156 or len(occurrences) != eligible_proposal_count:
        errors.append("unexpected reconciled taxonomy counts")
    canonical_labels = {topic["label"] for topic in topics.values()}
    alias_values: list[str] = []
    for topic in topics.values():
        if topic["domain_id"] not in domains:
            errors.append(f"topic without domain: {topic['id']}")
        for alias in topic["aliases"]:
            alias_values.append(alias)
            if alias == topic["label"] or alias in canonical_labels:
                errors.append(f"alias cycle/canonical collision: {topic['id']} / {alias}")
    if len(alias_values) != 3 or len(alias_values) != len(set(alias_values)):
        errors.append("unexpected or duplicate alias set")

    for occurrence in occurrences.values():
        if not occurrence["evidence_ids"]:
            errors.append(f"occurrence without evidence: {occurrence['id']}")
        if occurrence["review_state"] != "proposed" or occurrence["evidence_strength"] != "indeterminate":
            errors.append(f"occurrence does not preserve generated/uncertain state: {occurrence['id']}")
        if "Source applicability:" not in occurrence["notes"]:
            errors.append(f"occurrence lacks applicability note: {occurrence['id']}")
        for evidence_id in occurrence["evidence_ids"]:
            item = evidence.get(evidence_id)
            if not item or item["document_id"] not in document_ids:
                errors.append(f"occurrence evidence does not resolve: {occurrence['id']} / {evidence_id}")
            elif item["normalized_excerpt"] != occurrence["evidence_text"] or item["documentary_state"] != "indeterminate":
                errors.append(f"occurrence/evidence content or uncertainty mismatch: {occurrence['id']}")
    excluded_documents = {item["document"]["id"] for item in sources if not item["occurrence_eligible"]}
    if excluded_documents & {item["document_id"] for item in evidence.values()}:
        errors.append("ineligible source generated a topic occurrence")

    relations = taxonomy["evolution_relations"]
    if len(relations) != 12:
        errors.append("unexpected lineage candidate count")
    for relation in relations:
        endpoints = relation["source_occurrence_ids"] + relation["target_occurrence_ids"]
        if not endpoints or any(identifier not in occurrences for identifier in endpoints):
            errors.append(f"invalid lineage endpoints: {relation['id']}")
        expected_evidence = {eid for identifier in endpoints for eid in occurrences[identifier]["evidence_ids"]}
        if set(relation["evidence_ids"]) != expected_evidence:
            errors.append(f"lineage evidence mismatch: {relation['id']}")
        if relation["review_state"] != "proposed" or relation["evidence_strength"] != "indeterminate":
            errors.append(f"lineage candidate has overstated state: {relation['id']}")
        if not relation["candidate_method"] or not relation["analysis_provenance"] or relation["similarity_score"] is not None:
            errors.append(f"lineage method metadata invalid: {relation['id']}")
        if relation["change_type"] == "removed" and (not relation["source_occurrence_ids"] or relation["target_occurrence_ids"] or "coverage" not in relation["notes"].lower()):
            errors.append(f"removed candidate lacks coverage justification: {relation['id']}")
        if relation["change_type"] == "new" and "sparse usable corpus" not in relation["notes"]:
            errors.append(f"new candidate lacks bounded-corpus warning: {relation['id']}")
    relation_types = Counter(item["change_type"] for item in relations)
    if relation_types["fragmented"] != 1 or relation_types["merged"] != 1 or relation_types["indeterminate"] != 1 or relation_types["new"] != 1:
        errors.append("qualitative relation cases are incomplete")
    if relation_types["reduced"]:
        errors.append("W033 should not retain the independently rejected reduction candidate")
    if relation_types["removed"]:
        errors.append("W033 should not assert removed content with current coverage")

    split_files = {
        "domains.json": 18,
        "topics.json": 156,
        "topic-occurrences.json": 242,
        "aliases.json": 3,
        "candidate-lineage-relations.json": 12,
    }
    for filename, count in split_files.items():
        payload = load(f"site/data/generated/w033/{filename}")
        if len(payload["records"]) != count:
            errors.append(f"generated dataset count mismatch: {filename}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("W033 taxonomy valid: corpus=52, proposals=260, domains=18, topics=156, occurrences=242, aliases=3, relations=12; provenance and uncertainty checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
