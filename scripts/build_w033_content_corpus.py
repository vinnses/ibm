#!/usr/bin/env python3
"""Build the deterministic W033 content-source corpus from preserved extractions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site/data/source/w033/content-corpus.json"
F1_2023 = (
    ROOT / "dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv",
    ROOT / "dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv",
    ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv",
)


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_id(value: str) -> str:
    return "-".join(part for part in re.sub(r"[^a-z0-9]+", "-", value.lower()).split("-") if part)


def section(kind: str, text: str, locator: str) -> dict[str, str] | None:
    if not text.strip() or text.strip().lower() == "not stated":
        return None
    return {"kind": kind, "text": text.strip(), "locator": locator.strip() or "locator not stated in extraction"}


def source_record(*, curriculum: str, code: str, document_id: str, document_kind: str,
                  title: str, path: str, source_hash: str, url: str, date: str,
                  applicability: str, applicability_note: str,
                  extracted_sections: list[dict[str, str] | None], eligible: bool = True) -> dict[str, Any]:
    source = ROOT / path
    if not source.is_file() or source.is_symlink():
        raise ValueError(f"missing or unsafe corpus source: {path}")
    if file_hash(source) != source_hash:
        raise ValueError(f"hash mismatch in corpus source: {path}")
    sections = [item for item in extracted_sections if item]
    if not sections:
        raise ValueError(f"corpus source has no usable content: {document_id}")
    return {
        "id": f"corpus-{safe_id(document_id)}",
        "curriculum_id": curriculum,
        "component_instance_id": f"{curriculum}-{safe_id(code)}",
        "component_code": code,
        "document": {
            "id": f"document-{safe_id(document_id)}",
            "title": title,
            "institution": "Universidade Federal do Paraná",
            "document_type": document_kind,
            "document_date": date or "not stated",
            "original_url": url,
            "repository_path": path,
            "sha256": source_hash,
        },
        "sections": sections,
        "applicability": applicability,
        "applicability_note": applicability_note,
        "documentary_state": "indeterminate" if applicability == "indeterminate" else "documented",
        "occurrence_eligible": eligible,
    }


def build() -> dict[str, Any]:
    corpus: list[dict[str, Any]] = []
    document_rows = {row["document_id"]: row for row in rows(ROOT / "dados/curriculos/2011/fichas-preservadas/documents.csv")}
    for row in rows(ROOT / "dados/curriculos/2011/fichas-preservadas/normalized-fields.csv"):
        metadata = document_rows[row["document_id"]]
        match = re.search(r"(?:CI|BQ|CE)\d{3,4}", row["document_id"])
        if not match:
            raise ValueError(f"cannot resolve 2011 component code: {row['document_id']}")
        code = match.group(0)
        explicitly_other_course = "explicitly applies to Ciência da Computação" in metadata["notes"]
        corpus.append(source_record(
            curriculum="curriculum-2011", code=code, document_id=row["document_id"],
            document_kind=metadata["document_kind"], title=metadata["source_title"],
            path=metadata["source_path"], source_hash=metadata["source_sha256"],
            url=metadata["source_url"], date=metadata["document_date"],
            applicability="not_applicable" if explicitly_other_course else "indeterminate",
            applicability_note=metadata["notes"], eligible=not explicitly_other_course,
            extracted_sections=[
                section("ementa", row["ementa_literal"], row["ementa_locator"]),
                section("program", row["program_literal"], row["program_locator"]),
                section("objectives", row["objectives_literal"], row["objectives_locator"]),
            ],
        ))

    for path in F1_2023:
        for row in rows(path):
            corpus.append(source_record(
                curriculum="curriculum-2023", code=row["code"], document_id=row["document_id"],
                document_kind=row["document_kind"], title=row["source_title"],
                path=row["source_path"], source_hash=row["source_sha256"], url=row["source_url"],
                date=row["document_date"], applicability="indeterminate",
                applicability_note=f"Applicability to curriculum 2023: {row['applicability_2023']}. {row['normalization_notes']}",
                extracted_sections=[section("ementa", row["ementa"], row["ementa_locator"])],
            ))

    for row in rows(ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-2.csv"):
        corpus.append(source_record(
            curriculum="curriculum-2023", code=row["code"], document_id=row["document_id"],
            document_kind=row["document_kind"], title=row["source_title"],
            path=row["source_path"], source_hash=row["source_sha256"], url=row["source_url"],
            date=row["document_date"], applicability="indeterminate",
            applicability_note=f"Applicability to curriculum 2023: {row['applicability_2023']}; Ficha 2 is offering-specific. {row['normalization_notes']}",
            extracted_sections=[
                section("ementa", row["ementa"], row["source_locators"]),
                section("program", row["program"], row["source_locators"]),
                section("objectives", row["objectives"], row["source_locators"]),
            ],
        ))

    corpus.sort(key=lambda item: item["id"])
    ids = [item["id"] for item in corpus]
    document_ids = [item["document"]["id"] for item in corpus]
    if len(ids) != len(set(ids)) or len(document_ids) != len(set(document_ids)):
        raise ValueError("duplicate corpus or document ID")
    return {
        "schema_version": "1.0.0",
        "generated_by": "scripts/build_w033_content_corpus.py",
        "data_as_of": "2026-09-08",
        "method_note": "Content is copied from existing normalized documentary extractions; original preserved files prevail.",
        "sources": corpus,
    }


def serialize() -> bytes:
    return (json.dumps(build(), ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = serialize()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_bytes() != content:
            raise SystemExit("W033 content corpus is stale")
        print("W033 content corpus is deterministic and current")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(content)
    print(f"built {OUTPUT.relative_to(ROOT)} with {len(build()['sources'])} content sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
