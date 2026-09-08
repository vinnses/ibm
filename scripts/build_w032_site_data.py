#!/usr/bin/env python3
"""Build deterministic site data from the preserved curriculum inventories."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import mimetypes
import shutil
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site/src/lib/data/generated/content-model.json"
PUBLIC_ROOT = ROOT / "site/static/documents"
ALLOWLIST = ROOT / "site/data/source/public-documents.json"
FIXTURES = ROOT / "site/data/source/analytical-fixtures.json"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def integer(value: str) -> int | None:
    value = value.strip()
    return int(value) if value.isdigit() else None


def safe_id(value: str) -> str:
    return "-".join(part for part in "".join(c.lower() if c.isalnum() else "-" for c in value).split("-") if part)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_record(path: Path, record_id: str) -> dict[str, str]:
    matches = [row for row in read_csv(path) if row.get("id") == record_id]
    if len(matches) != 1:
        raise ValueError(f"expected one manifest row {record_id!r} in {path}, found {len(matches)}")
    return matches[0]


def build_documents(destination: Path) -> list[dict[str, Any]]:
    config = read_json(ALLOWLIST)
    prefixes = tuple(config["allowed_repository_prefixes"])
    documents: list[dict[str, Any]] = []
    destination.mkdir(parents=True, exist_ok=True)

    for entry in sorted(config["documents"], key=lambda item: item["id"]):
        manifest_path = ROOT / entry["manifest_path"]
        row = manifest_record(manifest_path, entry["manifest_id"])
        relative = row["local_path"]
        if Path(relative).is_absolute() or ".." in Path(relative).parts or not relative.startswith(prefixes):
            raise ValueError(f"unsafe or disallowed public document path: {relative}")
        source = ROOT / relative
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"public document is missing, not regular, or a symlink: {relative}")
        actual_hash = sha256(source)
        if actual_hash != row["sha256"]:
            raise ValueError(f"public document hash mismatch: {relative}")

        target_dir = destination / entry["id"]
        target_dir.mkdir()
        target = target_dir / entry["public_filename"]
        shutil.copyfile(source, target)
        media_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        documents.append(
            {
                "id": entry["id"],
                "title": row["title"],
                "institution": row["institution"],
                "document_type": row["document_type"],
                "document_date": row["document_date"],
                "original_url": row["source_url"],
                "repository_path": relative,
                "sha256": actual_hash,
                "documentary_state": "documented",
                "applicability_status": entry["applicability_status"],
                "applicability_note": entry["applicability_note"],
                "public_path": f"/documentos/{entry['id']}/arquivo",
                "asset_path": f"/documents/{entry['id']}/{entry['public_filename']}",
                "media_type": media_type,
            }
        )
    corpus_path = ROOT / "site/data/source/w033/content-corpus.json"
    if corpus_path.is_file():
        corpus = read_json(corpus_path)
        for item in sorted(corpus["sources"], key=lambda value: value["document"]["id"]):
            source_document = item["document"]
            relative = source_document["repository_path"]
            if Path(relative).is_absolute() or ".." in Path(relative).parts or not relative.startswith(prefixes):
                raise ValueError(f"unsafe or disallowed W033 public document path: {relative}")
            source = ROOT / relative
            if not source.is_file() or source.is_symlink():
                raise ValueError(f"W033 public document is missing, not regular, or a symlink: {relative}")
            actual_hash = sha256(source)
            if actual_hash != source_document["sha256"]:
                raise ValueError(f"W033 public document hash mismatch: {relative}")
            document_id = source_document["id"]
            target_dir = destination / document_id
            target_dir.mkdir()
            filename = f"source{source.suffix.lower()}"
            target = target_dir / filename
            shutil.copyfile(source, target)
            documents.append({
                "id": document_id,
                "title": source_document["title"],
                "institution": source_document["institution"],
                "document_type": source_document["document_type"],
                "document_date": source_document["document_date"],
                "original_url": source_document["original_url"],
                "repository_path": relative,
                "sha256": actual_hash,
                "documentary_state": item["documentary_state"],
                "applicability_status": "indeterminate",
                "applicability_note": item["applicability_note"],
                "public_path": f"/documentos/{document_id}/arquivo",
                "asset_path": f"/documents/{document_id}/{filename}",
                "media_type": mimetypes.guess_type(target.name)[0] or "application/octet-stream",
            })
    return documents


def build_model(public_destination: Path) -> dict[str, Any]:
    documents = build_documents(public_destination)
    fixtures = read_json(FIXTURES)
    taxonomy_path = ROOT / "site/data/source/w033/taxonomy.json"
    taxonomy = read_json(taxonomy_path) if taxonomy_path.is_file() else None
    document_by_id = {document["id"]: document for document in documents}

    evidence = [
        {
            "id": "evidence-2011-resolution-structure",
            "document_id": "document-2011-resolution-34-2010",
            "page": None,
            "section": "Anexo I",
            "cell_range": None,
            "normalized_excerpt": None,
            "applicability_note": document_by_id["document-2011-resolution-34-2010"]["applicability_note"],
            "documentary_state": "documented",
            "notes": "Shared structural evidence; source metadata remains canonical on the document record.",
        },
        {
            "id": "evidence-2011-ppc-context",
            "document_id": "document-2011-ppc",
            "page": None,
            "section": None,
            "cell_range": None,
            "normalized_excerpt": None,
            "applicability_note": document_by_id["document-2011-ppc"]["applicability_note"],
            "documentary_state": "documented",
            "notes": "Curriculum context only; component rows use the formal resolution as their structural basis.",
        },
        {
            "id": "evidence-2023-resolution-structure",
            "document_id": "document-2023-resolution-75-22",
            "page": None,
            "section": "Anexo I",
            "cell_range": None,
            "normalized_excerpt": None,
            "applicability_note": document_by_id["document-2023-resolution-75-22"]["applicability_note"],
            "documentary_state": "documented",
            "notes": "Shared structural evidence; source metadata remains canonical on the document record.",
        },
        {
            "id": "evidence-2023-ppc-context",
            "document_id": "document-2023-ppc",
            "page": None,
            "section": None,
            "cell_range": None,
            "normalized_excerpt": None,
            "applicability_note": document_by_id["document-2023-ppc"]["applicability_note"],
            "documentary_state": "documented",
            "notes": "Curriculum context only; component rows use the formal resolution as their structural basis.",
        },
    ]
    if taxonomy:
        evidence.extend(taxonomy["evidence"])

    curricula = [
        {
            "id": "curriculum-2011",
            "label": "Currículo 2011 (96A)",
            "year": 2011,
            "validity": "Implantado em 2011 pela Resolução nº 34/2010-CEPE.",
            "evidence_ids": ["evidence-2011-resolution-structure", "evidence-2011-ppc-context"],
            "notes": "Unidade histórica própria; não presume continuidade de Fichas posteriores.",
            "documentary_state": "documented",
        },
        {
            "id": "curriculum-2023",
            "label": "Currículo 2023",
            "year": 2023,
            "validity": "Estrutura aprovada para ingressantes de 2022/2023.",
            "evidence_ids": ["evidence-2023-resolution-structure", "evidence-2023-ppc-context"],
            "notes": "Unidade histórica própria; aplicabilidade de Fichas permanece conforme o inventário documental.",
            "documentary_state": "documented",
        },
    ]

    components: list[dict[str, Any]] = []
    dependencies: list[dict[str, Any]] = []
    evidence_links: list[dict[str, str]] = []

    component_sources = [
        ("curriculum-2011", ROOT / "curriculos/2011/inventario/componentes.csv", "evidence-2011-resolution-structure"),
        ("curriculum-2023", ROOT / "curriculos/2023/inventario/componentes.csv", "evidence-2023-resolution-structure"),
    ]
    component_ids: dict[tuple[str, str], str] = {}
    for curriculum_id, path, evidence_id in component_sources:
        for row in read_csv(path):
            code = (row.get("code") or row.get("target_id") or "").strip()
            component_id = f"{curriculum_id}-{safe_id(code)}"
            component_ids[(curriculum_id, code)] = component_id
            state_raw = (row.get("status") or row.get("evidence_status") or "").lower()
            state = "documented" if ("proven" in state_raw or "comprovad" in state_raw) else "indeterminate"
            notes = row.get("gaps_conflicts") or row.get("gaps_or_conflicts") or ""
            components.append(
                {
                    "id": component_id,
                    "curriculum_id": curriculum_id,
                    "code": code,
                    "name": (row.get("title") or "").strip(),
                    "recommended_period": integer(row.get("recommended_term") or row.get("recommended_period") or ""),
                    "workload_hours": integer(row.get("total_hours") or ""),
                    "nature": (row.get("target_type") or row.get("nature") or "").strip(),
                    "dependency_ids": [],
                    "evidence_ids": [evidence_id],
                    "evidence_state": state,
                    "notes": notes.strip(),
                }
            )
            evidence_links.append({"id": f"link-{evidence_id}-{component_id}", "evidence_id": evidence_id, "target_type": "component_instance", "target_id": component_id, "purpose": "Formal curriculum structure"})

    dependency_sources = [
        ("curriculum-2011", ROOT / "curriculos/2011/inventario/dependencias.csv", "evidence-2011-resolution-structure"),
        ("curriculum-2023", ROOT / "curriculos/2023/inventario/dependencias.csv", "evidence-2023-resolution-structure"),
    ]
    component_by_id = {component["id"]: component for component in components}
    block_a_ids = sorted(
        component["id"]
        for component in components
        if component["curriculum_id"] == "curriculum-2011"
        and component["id"].startswith("curriculum-2011-")
        and "member of Bloco A" in next(
            row["hidden_requirement"]
            for row in read_csv(ROOT / "curriculos/2011/inventario/componentes.csv")
            if (row.get("code") or row.get("target_id")) == component["code"]
        )
    )
    for curriculum_id, path, evidence_id in dependency_sources:
        for index, row in enumerate(read_csv(path), start=1):
            if curriculum_id == "curriculum-2011":
                prerequisite, dependent = row["from_target"], row["to_target"]
                relation = row["relation"]
                text = row["requirement_text"]
                notes = row["notes"]
            else:
                prerequisite, dependent = row["prerequisite_code"], row["dependent_code"]
                relation = row["relation"]
                text = f"{prerequisite} is {relation} of {dependent}"
                notes = row["notes"]
            from_ids = block_a_ids if prerequisite == "BLOCK-A" else [component_ids[(curriculum_id, prerequisite)]]
            to_id = component_ids[(curriculum_id, dependent)]
            dependency_id = f"dependency-{safe_id(curriculum_id)}-{safe_id(prerequisite)}-{safe_id(dependent)}-{index}"
            dependencies.append({"id": dependency_id, "curriculum_id": curriculum_id, "from_component_ids": from_ids, "to_component_id": to_id, "relation": relation if relation in {"prerequisite", "corequisite", "equivalence", "hidden_requirement"} else "other", "requirement_text": text, "evidence_ids": [evidence_id], "documentary_state": "documented", "notes": notes.strip()})
            component_by_id[to_id]["dependency_ids"].append(dependency_id)
            evidence_links.append({"id": f"link-{evidence_id}-{dependency_id}", "evidence_id": evidence_id, "target_type": "component_dependency", "target_id": dependency_id, "purpose": "Formal dependency structure"})

    for curriculum in curricula:
        for evidence_id in curriculum["evidence_ids"]:
            evidence_links.append({"id": f"link-{evidence_id}-{curriculum['id']}", "evidence_id": evidence_id, "target_type": "curriculum", "target_id": curriculum["id"], "purpose": "Formal curriculum evidence"})

    if taxonomy:
        evidence_links.extend(taxonomy["evidence_links"])

    return {
        "schema_version": "1.0.0",
        "generated_at": "2026-09-08T00:00:00Z",
        "generated_by": "scripts/build_w032_site_data.py",
        "fixture_notice": fixtures["fixture_notice"] if not taxonomy else "No synthetic fixture is present; W033 analytical records remain proposed pending review.",
        "factual": {
            "curricula": sorted(curricula, key=lambda item: item["id"]),
            "component_instances": sorted(components, key=lambda item: item["id"]),
            "component_dependencies": sorted(dependencies, key=lambda item: item["id"]),
            "documents": documents,
        },
        "analytical": {
            key: sorted((taxonomy[key] if taxonomy else fixtures[key]), key=lambda item: item["id"])
            for key in ("content_domains", "content_topics", "topic_occurrences", "evolution_relations")
        },
        "provenance": {
            "claims": [],
            "evidence": sorted(evidence, key=lambda item: item["id"]),
            "evidence_links": sorted(evidence_links, key=lambda item: item["id"]),
        },
    }


def write_build(output: Path, public_root: Path) -> None:
    if public_root.exists():
        shutil.rmtree(public_root)
    model = build_model(public_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(model, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if committed generated artifacts differ")
    args = parser.parse_args()
    if not args.check:
        write_build(OUTPUT, PUBLIC_ROOT)
        print(f"built {OUTPUT.relative_to(ROOT)} and public document allowlist")
        return 0

    with tempfile.TemporaryDirectory(prefix="w032-build-") as temporary:
        temporary_root = Path(temporary)
        expected_output = temporary_root / "content-model.json"
        expected_public = temporary_root / "documents"
        write_build(expected_output, expected_public)
        if not OUTPUT.is_file() or OUTPUT.read_bytes() != expected_output.read_bytes():
            raise SystemExit("generated content model is stale; run scripts/build_w032_site_data.py")
        actual_files = sorted(path.relative_to(PUBLIC_ROOT) for path in PUBLIC_ROOT.rglob("*") if path.is_file())
        expected_files = sorted(path.relative_to(expected_public) for path in expected_public.rglob("*") if path.is_file())
        if actual_files != expected_files:
            raise SystemExit("generated public document set is stale")
        for relative in actual_files:
            if (PUBLIC_ROOT / relative).read_bytes() != (expected_public / relative).read_bytes():
                raise SystemExit(f"generated public document differs: {relative}")
    print("W032 generated artifacts are deterministic and current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
