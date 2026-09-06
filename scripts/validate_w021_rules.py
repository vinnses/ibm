#!/usr/bin/env python3
"""Validate W021 literal provisions, topic coverage, and source provenance."""

from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados/curriculos/regras-estaveis/regras.csv"
MANIFESTS = (ROOT / "curriculos/2011/fontes/manifesto.csv", ROOT / "curriculos/2023/fontes/manifesto.csv")
REQUIRED = {"provision_id", "topic", "curriculum_version", "source_kind", "rule_type", "rule_text", "workload", "eligibility", "process", "approval_evaluation", "evidence_status", "uncertainty", "source_path", "source_sha256", "source_url", "locator", "normalization_notes"}
FORBIDDEN = re.compile(r"see[- ](?:the )?pdf|see locator|source[- ]stated summary|listed in pdf|topic count|titles on pdf|entries span|\bpoints\b", re.IGNORECASE)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_manifests() -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    for path in MANIFESTS:
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                records[row["local_path"]] = row
    return records


def main() -> int:
    errors: list[str] = []
    if not DATA.is_file():
        print(f"ERROR: missing {DATA}")
        return 1
    with DATA.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 75:
        errors.append(f"expected 75 distinct provisions (19 TCC + 35 Internship + 10 Formative + 11 Extension), found {len(rows)}")
    if any(set(row) != REQUIRED for row in rows):
        errors.append("schema differs from the documented W021 rule schema")
    if len({row.get("provision_id", "") for row in rows}) != len(rows):
        errors.append("provision_id values must be unique")
    if {row.get("curriculum_version") for row in rows} != {"2011", "2023"}:
        errors.append("both curriculum versions must be represented")
    for topic, expected in (("TCC", 19), ("Internship", 35), ("Formative", 10), ("Extension", 11)):
        if sum(row.get("topic") == topic for row in rows) != expected:
            errors.append(f"{topic} must have exactly {expected} provisions")
        if {row.get("curriculum_version") for row in rows if row.get("topic") == topic} != {"2011", "2023"}:
            errors.append(f"{topic} must cover both curriculum versions")
    for row in rows:
        ident = row.get("provision_id", "")
        for field in REQUIRED:
            if not row.get(field):
                errors.append(f"{ident}: empty required field {field}")
        if row.get("topic") not in {"TCC", "Internship", "Formative", "Extension"}:
            errors.append(f"{ident}: unsupported topic")
        if row.get("evidence_status") not in {"proven", "probable", "contradictory", "not located"}:
            errors.append(f"{ident}: invalid evidence_status")
        if len(row.get("rule_text", "")) < 80:
            errors.append(f"{ident}: rule_text is too short for a literal provision")
        if FORBIDDEN.search(row.get("rule_text", "")):
            errors.append(f"{ident}: rule_text contains a summary/pointer placeholder")
        if "PDF p. " not in row.get("locator", "") and "PDF pp. " not in row.get("locator", ""):
            errors.append(f"{ident}: locator lacks an exact PDF page")
        if not any(token in row.get("locator", "") for token in ("Art.", "Anexo", "seção", "semestre", "matrix", "SISTEMA DE AVALIAÇÃO", "project-only evaluation", "TRABALHO DE CONCLUSÃO")):
            errors.append(f"{ident}: locator lacks article/section/annex/table context")
        if "Whitespace and line-break normalization only" not in row.get("normalization_notes", ""):
            errors.append(f"{ident}: normalization note does not document whitespace-only normalization")
    manifests = load_manifests()
    seen_paths: set[str] = set()
    for row in rows:
        ident, path = row.get("provision_id", ""), row.get("source_path", "")
        if path not in manifests:
            errors.append(f"{ident}: source path absent from a preserved manifest")
            continue
        if path in seen_paths:
            continue
        seen_paths.add(path)
        record = manifests[path]
        pdf = ROOT / path
        if not pdf.is_file():
            errors.append(f"{ident}: stored source missing: {path}")
            continue
        if digest(pdf) != row.get("source_sha256"):
            errors.append(f"{ident}: CSV hash differs from stored bytes")
        if row.get("source_sha256") != record.get("sha256"):
            errors.append(f"{ident}: CSV hash differs from manifest")
        if row.get("source_url") != record.get("source_url"):
            errors.append(f"{ident}: CSV URL differs from manifest")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("W021 validation passed: 19 TCC + 35 Internship + 10 Formative + 11 Extension provisions across 2011/2023; manifest URLs, hashes, stored bytes, locators, and non-placeholder rule text verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
