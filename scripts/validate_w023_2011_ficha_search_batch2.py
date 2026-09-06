#!/usr/bin/env python3
"""Validate W023 checkpoint B's bounded CI241 documentary-search record."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculos/2011/fichas/w023-ci241"


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
    if len(manifest) != 1 or {row.get("record_id") for row in manifest} != {"W023-CI241-EXISTING-F1-2025"}:
        errors.append("CI241 manifest must contain only the retained pre-existing 2025 Ficha 1")
    if manifest:
        row = manifest[0]
        path = ROOT / row.get("local_path", "")
        if not path.is_file(): errors.append(f"missing retained Ficha: {row.get('local_path')}")
        elif sha256(path) != row.get("sha256"): errors.append("retained CI241 Ficha SHA-256 mismatch")
        if row.get("document_type") != "Ficha 1": errors.append("retained CI241 document must remain Ficha 1")
        if row.get("status") != "preserved_indeterminate": errors.append("retained CI241 Ficha must remain indeterminate")
        if "2025" not in row.get("version_or_validity", "") or "2011 Informática Biomédica curriculum 96A" not in row.get("notes", ""):
            errors.append("retained CI241 Ficha must retain its 2025 and 2011/96A applicability limit")
        if not row.get("source_url", "").startswith("https://bio.ufpr.br/"):
            errors.append("retained CI241 Ficha must retain its official UFPR source URL")
    searches = read_csv("buscas-negativas.csv")
    expected = {"W023-CI241-01", "W023-CI241-02", "W023-CI241-03"}
    if len(searches) != 3 or {row.get("search_id") for row in searches} != expected:
        errors.append("CI241 must record exactly three new targeted attempts")
    for row in searches:
        if row.get("targets") != "CI241": errors.append(f"out-of-scope target: {row.get('search_id')}")
        for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
            if not row.get(field): errors.append(f"missing {field}: {row.get('search_id')}")
    if errors:
        for error in errors: print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("W023 checkpoint B validation passed: CI241 has three new targeted attempts and retains one separately hashed 2025 Ficha 1 without 2011/96A assignment.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
