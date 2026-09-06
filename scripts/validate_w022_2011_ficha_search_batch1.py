#!/usr/bin/env python3
"""Validate W022 checkpoint B's bounded CI055 documentary-search record."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculos/2011/fichas/w022-ci055"


def read_csv(name: str) -> list[dict[str, str]]:
    with (BASE / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    manifest = read_csv("manifesto.csv")
    expected_ids = {
        "W022-CI055-ARCHIVE-PAGE",
        "W022-CI055-F1-2011",
        "W022-CI055-OLDER-COMPONENT",
        "W022-CI055-F2-2011-1",
    }
    if {row.get("record_id") for row in manifest} != expected_ids:
        errors.append("manifest record identifiers differ from CI055 checkpoint scope")
    if len(manifest) != 4:
        errors.append(f"expected four preserved source records, found {len(manifest)}")
    for row in manifest:
        path = ROOT / row.get("local_path", "")
        if not path.is_file():
            errors.append(f"missing manifested source: {row.get('local_path')}")
        elif sha256(path) != row.get("sha256"):
            errors.append(f"SHA-256 mismatch: {row.get('local_path')}")
        if row.get("institution") != "Universidade Federal do Paraná":
            errors.append(f"non-UFPR institution: {row.get('record_id')}")
        if not row.get("source_url", "").startswith("https://www.inf.ufpr.br/"):
            errors.append(f"non-official source URL: {row.get('record_id')}")
        if not row.get("accessed_at") or not row.get("document_type") or not row.get("purpose"):
            errors.append(f"incomplete provenance: {row.get('record_id')}")
    by_id = {row.get("record_id"): row for row in manifest}
    if by_id.get("W022-CI055-F1-2011", {}).get("document_type") != "Ficha 1":
        errors.append("2011 CI055 source must remain classified as Ficha 1")
    if by_id.get("W022-CI055-F1-2011", {}).get("status") != "preserved_indeterminate":
        errors.append("CI055 Ficha 1 curriculum applicability must remain indeterminate")
    if by_id.get("W022-CI055-F2-2011-1", {}).get("document_type") != "Ficha 2":
        errors.append("2011/1 CI055 source must remain classified separately as Ficha 2")
    if "Ciência da Computação" not in by_id.get("W022-CI055-F2-2011-1", {}).get("notes", ""):
        errors.append("Ficha 2 must retain its explicitly different course context")
    searches = read_csv("buscas-negativas.csv")
    expected_searches = {"W022-CI055-01", "W022-CI055-02", "W022-CI055-03"}
    if {row.get("search_id") for row in searches} != expected_searches or len(searches) != 3:
        errors.append("CI055 checkpoint must record exactly three targeted attempts")
    for row in searches:
        if row.get("targets") != "CI055": errors.append(f"out-of-scope search target: {row.get('search_id')}")
        for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
            if not row.get(field): errors.append(f"missing {field}: {row.get('search_id')}")
    if errors:
        for error in errors: print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("W022 checkpoint B validation passed: CI055 has three targeted attempts and four separately preserved, hashed official sources; Ficha 1/Ficha 2 applicability limits remain explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
