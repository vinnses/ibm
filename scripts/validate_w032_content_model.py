#!/usr/bin/env python3
"""Validate W032 schema invariants, provenance, and public document safety."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "site/src/lib/data/generated/content-model.json"
SCHEMA_PATH = ROOT / "site/data/schema/content-model.schema.json"
PUBLIC_ROOT = ROOT / "site/static/documents"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REVIEW_STATES = {"proposed", "reviewed", "contested", "indeterminate"}
EVIDENCE_STRENGTHS = {"documented", "strongly_supported", "probable", "hypothesis", "indeterminate"}
DOCUMENTARY_STATES = {"documented", "probable", "contradictory", "not_located", "indeterminate"}
CHANGE_TYPES = {"maintained", "expanded", "reduced", "moved", "fragmented", "merged", "new", "removed", "indeterminate"}


def validate_schema(instance: Any, schema: dict[str, Any], root_schema: dict[str, Any], location: str = "$") -> list[str]:
    """Evaluate the JSON Schema keywords used by W032 without a runtime dependency."""
    if "$ref" in schema:
        prefix = "#/$defs/"
        reference = schema["$ref"]
        if not reference.startswith(prefix) or reference[len(prefix):] not in root_schema.get("$defs", {}):
            return [f"{location}: unresolved schema reference {reference}"]
        return validate_schema(instance, root_schema["$defs"][reference[len(prefix):]], root_schema, location)
    errors: list[str] = []
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{location}: does not match const")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{location}: value is outside enum")
    expected = schema.get("type")
    if expected:
        names = expected if isinstance(expected, list) else [expected]
        checks = {
            "object": lambda value: isinstance(value, dict),
            "array": lambda value: isinstance(value, list),
            "string": lambda value: isinstance(value, str),
            "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
            "boolean": lambda value: isinstance(value, bool),
            "null": lambda value: value is None,
        }
        if not any(checks[name](instance) for name in names):
            return [f"{location}: expected type {expected}"]
    if isinstance(instance, str) and "pattern" in schema and not re.search(schema["pattern"], instance):
        errors.append(f"{location}: string does not match pattern")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{location}: fewer than minItems")
        if "items" in schema:
            for index, value in enumerate(instance):
                errors.extend(validate_schema(value, schema["items"], root_schema, f"{location}[{index}]"))
    if isinstance(instance, dict):
        required = schema.get("required", [])
        for field in required:
            if field not in instance:
                errors.append(f"{location}: missing required property {field}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for field in instance.keys() - properties.keys():
                errors.append(f"{location}: unexpected property {field}")
        for field, subschema in properties.items():
            if field in instance:
                errors.extend(validate_schema(instance[field], subschema, root_schema, f"{location}.{field}"))
    return errors


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_model(model: dict[str, Any], check_files: bool = True) -> list[str]:
    errors: list[str] = []
    factual = model.get("factual", {})
    analytical = model.get("analytical", {})
    provenance = model.get("provenance", {})
    collections = {
        "curriculum": factual.get("curricula", []),
        "component_instance": factual.get("component_instances", []),
        "component_dependency": factual.get("component_dependencies", []),
        "document": factual.get("documents", []),
        "content_domain": analytical.get("content_domains", []),
        "content_topic": analytical.get("content_topics", []),
        "topic_occurrence": analytical.get("topic_occurrences", []),
        "evolution_relation": analytical.get("evolution_relations", []),
        "claim": provenance.get("claims", []),
        "evidence": provenance.get("evidence", []),
        "evidence_link": provenance.get("evidence_links", []),
    }
    ids: dict[str, str] = {}
    for kind, records in collections.items():
        if not isinstance(records, list):
            errors.append(f"{kind} collection is not an array")
            continue
        for record in records:
            record_id = record.get("id", "")
            if not ID_RE.fullmatch(record_id):
                errors.append(f"invalid {kind} id: {record_id!r}")
            if record_id in ids:
                errors.append(f"duplicate global id: {record_id} ({ids[record_id]} and {kind})")
            ids[record_id] = kind

    sets = {kind: {record["id"] for record in records} for kind, records in collections.items() if isinstance(records, list)}
    evidence_ids = sets["evidence"]
    component_ids = sets["component_instance"]
    curriculum_ids = sets["curriculum"]
    topic_ids = sets["content_topic"]
    occurrence_ids = sets["topic_occurrence"]
    document_ids = sets["document"]

    def refs(record: dict[str, Any], field: str, allowed: set[str]) -> None:
        values = record.get(field, [])
        values = values if isinstance(values, list) else [values]
        for value in values:
            if value not in allowed:
                errors.append(f"{record.get('id')} has orphan {field}: {value}")

    for curriculum in collections["curriculum"]:
        refs(curriculum, "evidence_ids", evidence_ids)
        if curriculum.get("documentary_state") not in DOCUMENTARY_STATES:
            errors.append(f"{curriculum['id']} has invalid documentary_state")
    for component in collections["component_instance"]:
        refs(component, "curriculum_id", curriculum_ids)
        refs(component, "dependency_ids", sets["component_dependency"])
        refs(component, "evidence_ids", evidence_ids)
        if component.get("evidence_state") not in DOCUMENTARY_STATES:
            errors.append(f"{component['id']} has invalid evidence_state")
    for dependency in collections["component_dependency"]:
        refs(dependency, "curriculum_id", curriculum_ids)
        refs(dependency, "from_component_ids", component_ids)
        refs(dependency, "to_component_id", component_ids)
        refs(dependency, "evidence_ids", evidence_ids)
        if not dependency.get("from_component_ids"):
            errors.append(f"{dependency['id']} has no dependency source")
    for domain in collections["content_domain"]:
        if domain.get("review_state") not in REVIEW_STATES:
            errors.append(f"{domain['id']} has invalid review_state")
    for topic in collections["content_topic"]:
        refs(topic, "domain_id", sets["content_domain"])
        refs(topic, "evidence_ids", evidence_ids)
        if topic.get("review_state") not in REVIEW_STATES:
            errors.append(f"{topic['id']} has invalid review_state")
    for occurrence in collections["topic_occurrence"]:
        refs(occurrence, "topic_id", topic_ids)
        refs(occurrence, "component_instance_id", component_ids)
        refs(occurrence, "evidence_ids", evidence_ids)
        if occurrence.get("review_state") not in REVIEW_STATES or occurrence.get("evidence_strength") not in EVIDENCE_STRENGTHS:
            errors.append(f"{occurrence['id']} has invalid analytical state")
    for relation in collections["evolution_relation"]:
        refs(relation, "source_occurrence_ids", occurrence_ids)
        refs(relation, "target_occurrence_ids", occurrence_ids)
        refs(relation, "evidence_ids", evidence_ids)
        if relation.get("change_type") not in CHANGE_TYPES or relation.get("evidence_strength") not in EVIDENCE_STRENGTHS or relation.get("review_state") not in REVIEW_STATES:
            errors.append(f"{relation['id']} has invalid relation state")
    for item in collections["evidence"]:
        refs(item, "document_id", document_ids)
        if not item.get("document_id"):
            errors.append(f"{item['id']} has no origin document")
    for claim in collections["claim"]:
        refs(claim, "evidence_ids", evidence_ids)
        if claim.get("review_state") not in REVIEW_STATES or claim.get("layer") not in {"factual", "analytical"}:
            errors.append(f"{claim['id']} has invalid claim state")
    target_sets = {key: value for key, value in sets.items() if key not in {"document", "evidence", "evidence_link"}}
    target_sets["claim"] = sets["claim"]
    for link in collections["evidence_link"]:
        refs(link, "evidence_id", evidence_ids)
        target_type = link.get("target_type")
        if target_type not in target_sets or link.get("target_id") not in target_sets[target_type]:
            errors.append(f"{link['id']} has orphan target")

    expected_public: set[Path] = set()
    for document in collections["document"]:
        relative = Path(document.get("repository_path", ""))
        if relative.is_absolute() or ".." in relative.parts or str(relative).startswith((".git", ".env")):
            errors.append(f"{document['id']} has unsafe repository path")
            continue
        source = ROOT / relative
        asset_path = document.get("asset_path", "")
        expected_prefix = f"/documents/{document['id']}/"
        if not asset_path.startswith(expected_prefix) or ".." in Path(asset_path).parts:
            errors.append(f"{document['id']} has unsafe asset path")
            continue
        public_file = ROOT / "site/static" / asset_path.lstrip("/")
        expected_public.add(public_file)
        if check_files:
            if not source.is_file() or source.is_symlink() or digest(source) != document.get("sha256"):
                errors.append(f"{document['id']} source is missing, linked, or hash-invalid")
            if not public_file.is_file() or public_file.is_symlink() or digest(public_file) != document.get("sha256"):
                errors.append(f"{document['id']} public copy is missing, linked, or hash-invalid")
    if check_files and PUBLIC_ROOT.exists():
        actual_public = {path for path in PUBLIC_ROOT.rglob("*") if path.is_file()}
        if actual_public != expected_public:
            errors.append("public document tree differs from the generated manifest")
    return errors


def self_test(model: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    mutations = []
    orphan = copy.deepcopy(model)
    orphan["factual"]["component_instances"][0]["curriculum_id"] = "missing-curriculum"
    mutations.append(("orphan", orphan))
    bad_state = copy.deepcopy(model)
    bad_state["analytical"]["content_topics"][0]["review_state"] = "approved"
    mutations.append(("invalid state", bad_state))
    duplicate = copy.deepcopy(model)
    duplicate["analytical"]["content_domains"][0]["id"] = duplicate["analytical"]["content_topics"][0]["id"]
    mutations.append(("duplicate id", duplicate))
    traversal = copy.deepcopy(model)
    traversal["factual"]["documents"][0]["repository_path"] = "../.env"
    mutations.append(("path traversal", traversal))
    no_origin = copy.deepcopy(model)
    no_origin["provenance"]["evidence"][0]["document_id"] = ""
    mutations.append(("missing evidence origin", no_origin))
    for label, mutation in mutations:
        if not validate_model(mutation, check_files=False):
            failures.append(f"self-test did not reject {label}")
    return failures


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    errors = []
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema" or not schema.get("$defs"):
        errors.append("explicit JSON Schema is missing or malformed")
    errors.extend(validate_schema(model, schema, schema))
    if model.get("schema_version") != "1.0.0" or model.get("generated_by") != "scripts/build_w032_site_data.py":
        errors.append("generated metadata is invalid")
    errors.extend(validate_model(model))
    errors.extend(self_test(model))
    result = subprocess.run([sys.executable, str(ROOT / "scripts/build_w032_site_data.py"), "--check"], cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        errors.append(result.stderr.strip() or result.stdout.strip() or "builder check failed")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    counts = {key: len(value) for section in (model["factual"], model["analytical"], model["provenance"]) for key, value in section.items()}
    print(f"W032 content model valid: {counts}; negative invariant tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
