#!/usr/bin/env python3
"""Reconcile W033 agent proposals into stable taxonomy and occurrence records."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "site/data/source/w033"
OUTPUT = SOURCE_DIR / "taxonomy.json"
GENERATED_DIR = ROOT / "site/data/generated/w033"

DOMAIN_MAP = {
    "Fundamentos de Computação": "Fundamentos da Computação",
    "Fundamentos da Computação": "Fundamentos da Computação",
    "Teoria da Computação": "Fundamentos da Computação",
    "Programação e Algoritmos": "Programação",
    "Programação e Desenvolvimento de Software": "Programação",
    "Estruturas de Dados": "Algoritmos e Estruturas de Dados",
    "Algoritmos e Estruturas de Dados": "Algoritmos e Estruturas de Dados",
    "Análise de Algoritmos": "Algoritmos e Estruturas de Dados",
    "Qualidade e Engenharia de Software": "Engenharia de Software",
    "Arquitetura e Hardware": "Arquitetura e Hardware",
    "Inteligência Artificial e Aprendizado de Máquina": "Inteligência Artificial e Aprendizado de Máquina",
    "Banco de Dados": "Banco de Dados",
    "Segurança Computacional": "Segurança Computacional",
    "Computação, Sociedade e Ética": "Computação, Sociedade e Ética",
    "Bioinformática": "Bioinformática",
    "Biociências e Saúde": "Biociências",
    "Biologia Molecular": "Biociências",
    "Bioquímica": "Biociências",
    "Estatística": "Estatística",
    "Sistemas Distribuídos e Paralelos": "Redes, Sistemas Distribuídos e Paralelismo",
    "Redes e Sistemas Distribuídos": "Redes, Sistemas Distribuídos e Paralelismo",
    "Sistemas Operacionais": "Sistemas Operacionais",
    "Interação Humano-Computador": "Interação Humano-Computador",
    "Saúde Coletiva e Sistema de Saúde": "Saúde Coletiva e Sistema de Saúde",
    "Metodologia Científica e Bioética": "Metodologia Científica e Bioética",
    "Informática Biomédica": "Informática Biomédica",
}

CANONICAL_LABELS = {
    "arquitetura de Von Neumann": "modelo de Von Neumann",
    "recursividade": "recursão",
    "estruturas heap": "heaps",
    "estrutura de ácidos nucléicos": "estrutura de ácidos nucleicos",
    "refinamentos sucessivos": "refinamento sucessivo",
}

RELATIONS = [
    {"key": "maintained-access", "source": ["acesso sequencial e indexado"], "target": ["acesso sequencial e indexado"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only: matching source-grounded topic labels occur in both corpora; applicability of every source remains indeterminate."},
    {"key": "maintained-search", "source": ["algoritmos de busca"], "target": ["algoritmos de busca"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only: content wording overlaps, but this is not documentary proof of curricular continuity."},
    {"key": "maintained-sequence-alignment", "source": ["alinhamento de sequências e busca de genes"], "target": ["alinhamento de sequências e busca de genes"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; both occurrences rely on sources of indeterminate curriculum applicability."},
    {"key": "maintained-phylogeny", "source": ["análise filogenética"], "target": ["análise filogenética"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; exact analytical label overlap does not establish a formal continuity act."},
    {"key": "maintained-omics", "source": ["análises genômica, transcriptômica e proteômica"], "target": ["análises genômica, transcriptômica e proteômica"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; retained for human review with source applicability limits."},
    {"key": "maintained-biological-databases", "source": ["bancos de dados biológicos"], "target": ["bancos de dados biológicos"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; not merged with general database-system content."},
    {"key": "maintained-external-sorting", "source": ["ordenação externa"], "target": ["ordenação externa"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; source versions remain independently evidenced."},
    {"key": "maintained-structured-programming", "source": ["programação estruturada"], "target": ["programação estruturada"], "change_type": "maintained", "method": "exact normalized topic-label overlap", "notes": "Candidate only; code/name were not used as evidence."},
    {"key": "fragmented-order-search", "source": ["pesquisa e ordenação em memória principal"], "target": ["algoritmos de busca", "algoritmos de ordenação"], "change_type": "fragmented", "method": "qualitative reconciliation of source-grounded topic units", "notes": "Split candidate: one combined 2011 analytical unit maps to separately represented search and sorting units in 2023; not a formal equivalence."},
    {"key": "merged-linear-structures", "source": ["tipos abstratos de dados lineares", "listas, filas e pilhas"], "target": ["estruturas de dados básicas"], "change_type": "merged", "method": "qualitative reconciliation of source-grounded topic units", "notes": "Merge candidate: two explicit 2011 units may be covered by a broader 2023 basic-data-structures description. The target's breadth makes this a hypothesis only."},
    {"key": "new-security-access-control", "source": [], "target": ["autenticação e controle de acesso"], "change_type": "new", "method": "absence check limited to the declared usable 2011 corpus", "notes": "New-content candidate only relative to the sparse usable corpus. It is not a claim that the curriculum lacked this content; 2011 coverage is insufficient and evidence strength is indeterminate."},
    {"key": "indeterminate-networks", "source": ["modelos de referência OSI e TCP/IP"], "target": [], "change_type": "indeterminate", "method": "coverage-gap check", "notes": "No matching topic was located in the usable 2023 Ficha corpus, but incomplete coverage prohibits a removed classification."},
]


def load(name: str) -> dict[str, Any]:
    return json.loads((SOURCE_DIR / name).read_text(encoding="utf-8"))


def slug(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return "-".join(part for part in re.sub(r"[^a-z0-9]+", "-", ascii_value).split("-") if part)


def proposal_records() -> list[dict[str, Any]]:
    corpus = load("content-corpus.json")
    corpus_by_path = {item["document"]["repository_path"]: item for item in corpus["sources"]}
    records: list[dict[str, Any]] = []
    source_2011 = load("agent-2011-proposals.json")
    for source in source_2011["source_documents"]:
        corpus_item = corpus_by_path[source["source_path"]]
        for topic in source["proposed_topics"]:
            records.append({"corpus": corpus_item, "label": topic["label"], "domain": topic["domain_label"], "excerpt": topic["supporting_excerpt"], "locator": source["locator"], "aliases": topic["aliases"], "notes": topic["notes"]})
    source_2023 = load("agent-2023-proposals.json")
    for source in source_2023["sources"]:
        corpus_item = corpus_by_path[source["source_path"]]
        for topic in source["topic_proposals"]:
            records.append({"corpus": corpus_item, "label": topic["proposed_label_pt"], "domain": topic["suggested_domain_label_pt"], "excerpt": topic["supporting_excerpt"], "locator": source["locator"], "aliases": topic["aliases"], "notes": topic["notes"]})
    return records


def build() -> dict[str, Any]:
    records = proposal_records()
    topic_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if not record["corpus"]["occurrence_eligible"]:
            continue
        canonical = CANONICAL_LABELS.get(record["label"], record["label"])
        record["canonical_label"] = canonical
        record["canonical_domain"] = DOMAIN_MAP[record["domain"]]
        topic_records[canonical].append(record)

    domain_labels = sorted({record["canonical_domain"] for group in topic_records.values() for record in group})
    domains = [{"id": f"domain-{slug(label)}", "label": label, "description": f"Domínio analítico inicial que organiza tópicos de {label.lower()} no corpus documental utilizável.", "review_state": "proposed", "provenance_note": "W033 reconciliation of broad domain suggestions emerging from source-grounded topic proposals.", "is_fixture": False} for label in domain_labels]

    topics: list[dict[str, Any]] = []
    occurrences: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    links: list[dict[str, str]] = []
    aliases_by_topic: dict[str, set[str]] = defaultdict(set)
    occurrence_ids_by_label_year: dict[tuple[str, str], list[str]] = defaultdict(list)

    for canonical in sorted(topic_records):
        group = topic_records[canonical]
        domain_counts = Counter(record["canonical_domain"] for record in group)
        domain_label = sorted(domain_counts, key=lambda label: (-domain_counts[label], label))[0]
        topic_id = f"topic-{slug(canonical)}"
        for record in group:
            if record["label"] != canonical:
                aliases_by_topic[topic_id].add(record["label"])
            if "SGBD" in record["aliases"]:
                aliases_by_topic[topic_id].add("SGBD")
        for record in group:
            corpus = record["corpus"]
            occurrence_id = f"occurrence-{slug(corpus['id'])}-{slug(canonical)}"
            evidence_id = f"evidence-{slug(corpus['id'])}-{slug(canonical)}"
            occurrence_ids_by_label_year[(canonical, corpus["curriculum_id"])].append(occurrence_id)
            evidence.append({"id": evidence_id, "document_id": corpus["document"]["id"], "page": None, "section": record["locator"], "cell_range": None, "normalized_excerpt": record["excerpt"], "applicability_note": corpus["applicability_note"], "documentary_state": "indeterminate", "notes": "Evidence locator and excerpt originate in the W033 consolidated normalized corpus; preserved source bytes prevail."})
            occurrences.append({"id": occurrence_id, "topic_id": topic_id, "component_instance_id": corpus["component_instance_id"], "evidence_text": record["excerpt"], "evidence_ids": [evidence_id], "locator": record["locator"], "evidence_strength": "indeterminate", "notes": f"{record['notes']} Source applicability: {corpus['applicability_note']}", "review_state": "proposed", "is_fixture": False})
            links.extend([
                {"id": f"link-{evidence_id}-{occurrence_id}", "evidence_id": evidence_id, "target_type": "topic_occurrence", "target_id": occurrence_id, "purpose": "Quoted support for proposed topic occurrence"},
                {"id": f"link-{evidence_id}-{topic_id}", "evidence_id": evidence_id, "target_type": "content_topic", "target_id": topic_id, "purpose": "Source-grounded identification of proposed topic"},
            ])
        topic_evidence = sorted({item["evidence_ids"][0] for item in occurrences if item["topic_id"] == topic_id})
        ambiguity = ""
        if len(domain_counts) > 1:
            ambiguity = " Ambiguous domain suggestions retained in provenance: " + ", ".join(f"{label} ({count})" for label, count in sorted(domain_counts.items())) + "."
        topics.append({"id": topic_id, "label": canonical, "domain_id": f"domain-{slug(domain_label)}", "description": f"Unidade analítica intermediária proposta para representar {canonical} entre descrições curriculares.", "aliases": sorted(alias for alias in aliases_by_topic[topic_id] if alias != canonical), "review_state": "proposed", "identification_provenance": f"W033 model-assisted reconciliation of {len(group)} source-grounded proposal(s); no code/title-only inference.{ambiguity}", "evidence_ids": topic_evidence, "is_fixture": False})

    occurrence_by_id = {item["id"]: item for item in occurrences}
    relations: list[dict[str, Any]] = []
    for relation in RELATIONS:
        source_ids = sorted({identifier for label in relation["source"] for identifier in occurrence_ids_by_label_year[(label, "curriculum-2011")]})
        target_ids = sorted({identifier for label in relation["target"] for identifier in occurrence_ids_by_label_year[(label, "curriculum-2023")]})
        if relation["source"] and not source_ids:
            raise ValueError(f"lineage source topic missing: {relation['key']}")
        if relation["target"] and not target_ids:
            raise ValueError(f"lineage target topic missing: {relation['key']}")
        evidence_ids = sorted({eid for identifier in source_ids + target_ids for eid in occurrence_by_id[identifier]["evidence_ids"]})
        relation_id = f"relation-{relation['key']}"
        relations.append({"id": relation_id, "source_occurrence_ids": source_ids, "target_occurrence_ids": target_ids, "change_type": relation["change_type"], "evidence_strength": "indeterminate", "evidence_ids": evidence_ids, "notes": relation["notes"], "review_state": "proposed", "is_fixture": False, "candidate_method": relation["method"], "similarity_score": None, "analysis_provenance": "W033 primary-session qualitative reconciliation; no embeddings or numerical threshold used."})
        for evidence_id in evidence_ids:
            links.append({"id": f"link-{evidence_id}-{relation_id}", "evidence_id": evidence_id, "target_type": "evolution_relation", "target_id": relation_id, "purpose": "Evidence underlying proposed lineage candidate"})

    return {
        "schema_version": "1.0.0",
        "generated_by": "scripts/build_w033_taxonomy.py",
        "data_as_of": "2026-09-08",
        "method_note": "Model-assisted source proposals reconciled deterministically; all outputs remain proposed and all source applicability remains explicit.",
        "content_domains": domains,
        "content_topics": sorted(topics, key=lambda item: item["id"]),
        "topic_occurrences": sorted(occurrences, key=lambda item: item["id"]),
        "evolution_relations": sorted(relations, key=lambda item: item["id"]),
        "evidence": sorted(evidence, key=lambda item: item["id"]),
        "evidence_links": sorted(links, key=lambda item: item["id"]),
    }


def content() -> bytes:
    return (json.dumps(build(), ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def split_outputs(result: dict[str, Any]) -> dict[str, bytes]:
    aliases = []
    for topic in result["content_topics"]:
        for alias in topic["aliases"]:
            aliases.append({
                "id": f"alias-{slug(topic['id'])}-{slug(alias)}",
                "topic_id": topic["id"],
                "alias": alias,
                "justification": "Explicit source abbreviation." if alias == "SGBD" else "W033 normalization of a source-proposed lexical variant; review remains pending.",
                "review_state": "proposed",
            })
    payloads = {
        "domains.json": result["content_domains"],
        "topics.json": result["content_topics"],
        "topic-occurrences.json": result["topic_occurrences"],
        "aliases.json": sorted(aliases, key=lambda item: item["id"]),
        "candidate-lineage-relations.json": result["evolution_relations"],
        "evidence-mappings.json": {"evidence": result["evidence"], "evidence_links": result["evidence_links"]},
    }
    rendered = {}
    for filename, records in payloads.items():
        envelope = {"schema_version": "1.0.0", "generated_by": "scripts/build_w033_taxonomy.py", "data_as_of": "2026-09-08", "records": records}
        rendered[filename] = (json.dumps(envelope, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    rendered = (json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    split = split_outputs(result)
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("W033 taxonomy output is stale")
        for filename, expected in split.items():
            path = GENERATED_DIR / filename
            if not path.is_file() or path.read_bytes() != expected:
                raise SystemExit(f"W033 generated dataset is stale: {filename}")
        print("W033 taxonomy is deterministic and current")
        return 0
    OUTPUT.write_bytes(rendered)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for filename, expected in split.items():
        (GENERATED_DIR / filename).write_bytes(expected)
    print(f"built W033 taxonomy: domains={len(result['content_domains'])}, topics={len(result['content_topics'])}, occurrences={len(result['topic_occurrences'])}, relations={len(result['evolution_relations'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
