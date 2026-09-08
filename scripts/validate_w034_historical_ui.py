#!/usr/bin/env python3
"""Validate W034 review UI invariants and optional production routes."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "site/src/lib/data/generated/content-model.json"
MAP_PATH = ROOT / "site/src/routes/mapa-curricular/+page.svelte"
LAYOUT_PATH = ROOT / "site/src/routes/+layout.svelte"
PACKAGE_PATH = ROOT / "site/package.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def get_status(url: str) -> tuple[int, bytes]:
    request = urllib.request.Request(url, headers={"User-Agent": "W034-validator/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.read()


def validate_static(model: dict) -> dict[str, str]:
    factual = model["factual"]
    analytical = model["analytical"]
    provenance = model["provenance"]
    components = {item["id"]: item for item in factual["component_instances"]}
    topics = {item["id"]: item for item in analytical["content_topics"]}
    occurrences = {item["id"]: item for item in analytical["topic_occurrences"]}
    evidence = {item["id"]: item for item in provenance["evidence"]}
    documents = {item["id"]: item for item in factual["documents"]}
    relations = analytical["evolution_relations"]

    if {item["review_state"] for item in relations} != {"proposed"}:
        fail("W034 must preserve the W033 proposed relation state")
    if {item["evidence_strength"] for item in relations} != {"indeterminate"}:
        fail("W034 must expose the W033 indeterminate relation strength")
    required_types = {"maintained", "fragmented", "merged", "new", "indeterminate"}
    present_types = {item["change_type"] for item in relations}
    if not required_types <= present_types:
        fail(f"required audit relation classes missing: {sorted(required_types - present_types)}")

    for relation in relations:
        for occurrence_id in relation["source_occurrence_ids"] + relation["target_occurrence_ids"]:
            if occurrence_id not in occurrences:
                fail(f"orphan relation occurrence: {relation['id']} -> {occurrence_id}")
        for evidence_id in relation["evidence_ids"]:
            if evidence_id not in evidence:
                fail(f"orphan relation evidence: {relation['id']} -> {evidence_id}")

    component_evidence: dict[str, set[str]] = {identifier: set(item["evidence_ids"]) for identifier, item in components.items()}
    for occurrence in occurrences.values():
        if occurrence["component_instance_id"] not in components:
            fail(f"orphan component occurrence: {occurrence['id']}")
        if occurrence["topic_id"] not in topics:
            fail(f"orphan topic occurrence: {occurrence['id']}")
        component_evidence[occurrence["component_instance_id"]].update(occurrence["evidence_ids"])

    ficha_components: set[str] = set()
    indeterminate_ficha_components: set[str] = set()
    for component_id, evidence_ids in component_evidence.items():
        linked_documents = [documents[evidence[item]["document_id"]] for item in evidence_ids if item in evidence and evidence[item]["document_id"] in documents]
        fichas = [item for item in linked_documents if item["document_type"] in {"Ficha 1", "Ficha 2"}]
        if fichas:
            ficha_components.add(component_id)
        if any(item["applicability_status"] == "indeterminate" for item in fichas):
            indeterminate_ficha_components.add(component_id)

    missing_components = {
        item["id"] for item in components.values()
        if item["id"] not in ficha_components and any(marker in item["notes"].casefold() for marker in ("não localizada", "não localizado", "não consta", "slot"))
    }
    if not missing_components:
        fail("no explicit missing-document component was derivable")
    if not indeterminate_ficha_components:
        fail("no applicability-indeterminate Ficha component was derivable")

    map_source = MAP_PATH.read_text(encoding="utf-8")
    layout_source = LAYOUT_PATH.read_text(encoding="utf-8")
    for token in (
        "Currículo", "Período", "Domínio", "Disciplina", "Estado de revisão", "Força da evidência",
        "Disponibilidade documental", "Tópicos nos dois currículos", "Somente relações/tópicos propostos",
        "Somente casos indeterminados", "@media (max-width: 700px)", "mobile-switch",
        "aria-pressed", "aria-live", "Ver evidências"
    ):
        if token not in map_source:
            fail(f"map control/accessibility token missing: {token}")
    for token in ("Pular para o conteúdo", "--focus", "prefers-reduced-motion", "Mapa 2011→2023"):
        if token not in layout_source:
            fail(f"shared accessibility/navigation token missing: {token}")

    package = json.loads(PACKAGE_PATH.read_text(encoding="utf-8"))
    dependencies = set(package.get("dependencies", {})) | set(package.get("devDependencies", {}))
    forbidden_graphics = {"d3", "cytoscape", "echarts", "highcharts"}
    if dependencies & forbidden_graphics:
        fail(f"unexpected visualization dependency: {sorted(dependencies & forbidden_graphics)}")

    samples = {
        "maintained": next(item["id"] for item in relations if item["change_type"] == "maintained"),
        "fragmented": next(item["id"] for item in relations if item["change_type"] == "fragmented"),
        "merged": next(item["id"] for item in relations if item["change_type"] == "merged"),
        "new": next(item["id"] for item in relations if item["change_type"] == "new"),
        "indeterminate": next(item["id"] for item in relations if item["change_type"] == "indeterminate"),
        "missing_component": sorted(missing_components)[0],
        "applicability_component": sorted(indeterminate_ficha_components)[0],
        "applicability_document": next(item["id"] for item in documents.values() if item["applicability_status"] == "indeterminate")
    }
    return samples


def validate_runtime(model: dict, base_url: str) -> None:
    base_url = base_url.rstrip("/")
    component = model["factual"]["component_instances"][0]["id"]
    topic = model["analytical"]["content_topics"][0]["id"]
    evidence = model["provenance"]["evidence"][0]["id"]
    document = model["factual"]["documents"][0]
    routes = (
        "/", "/mapa-curricular", f"/mapa-curricular?disciplina={component}",
        f"/mapa-curricular?conteudo={topic}", "/curriculos", "/curriculos/curriculum-2011",
        f"/disciplinas/{component}", "/conteudos", f"/conteudos/{topic}",
        f"/evidencias/{evidence}", f"/documentos/{document['id']}", "/metodologia", "/health"
    )
    for route in routes:
        status, body = get_status(base_url + route)
        if status != 200 or not body:
            fail(f"runtime route failed: {route} -> {status}, {len(body)} bytes")

    status, downloaded = get_status(base_url + document["public_path"])
    if status != 200:
        fail(f"preserved document route failed: {status}")
    if hashlib.sha256(downloaded).hexdigest() != document["sha256"]:
        fail("preserved document runtime SHA-256 mismatch")

    for route in (
        "/disciplinas/not-a-component", "/conteudos/not-a-topic", "/evidencias/not-evidence",
        "/documentos/not-a-document", "/documentos/..%2F..%2Fetc%2Fpasswd/arquivo",
        "/documentos/%2e%2e%2f%2e%2e%2fetc%2fpasswd/arquivo"
    ):
        status, _ = get_status(base_url + route)
        if status != 404:
            fail(f"negative/traversal route did not return 404: {route} -> {status}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", help="Optional running production URL")
    args = parser.parse_args()
    model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    samples = validate_static(model)
    if args.base_url:
        validate_runtime(model, args.base_url)
    print(f"W034 historical UI valid; samples={samples}; runtime={'checked' if args.base_url else 'skipped'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as error:
        print(f"W034 validation error: {error}", file=sys.stderr)
        raise SystemExit(1)
