#!/usr/bin/env python3
"""Validate W022 checkpoint B's bounded CI055, CI056, and CI057 records."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
def read_csv(base: Path, name: str) -> list[dict[str, str]]:
    with (base / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    checkpoints = {
        "CI055": {
            "base": ROOT / "curriculos/2011/fichas/w022-ci055",
            "records": {"W022-CI055-ARCHIVE-PAGE", "W022-CI055-F1-2011", "W022-CI055-OLDER-COMPONENT", "W022-CI055-F2-2011-1"},
            "f1": "W022-CI055-F1-2011",
            "f2": "W022-CI055-F2-2011-1",
            "f2_context": "Ciência da Computação",
        },
        "CI056": {
            "base": ROOT / "curriculos/2011/fichas/w022-ci056",
            "records": {"W022-CI056-F1-2011", "W022-CI056-F2-IBM-2010-1"},
            "f1": "W022-CI056-F1-2011",
            "f2": "W022-CI056-F2-IBM-2010-1",
            "f2_context": "Informática Biomédica",
        },
        "CI057": {
            "base": ROOT / "curriculos/2011/fichas/w022-ci057",
            "records": {"W022-CI057-F1-2011", "W022-CI057-F2-2011-1"},
            "f1": "W022-CI057-F1-2011",
            "f2": "W022-CI057-F2-2011-1",
            "f2_context": "Ciência da Computação",
        },
    }
    total_sources = 0
    for code, checkpoint in checkpoints.items():
        manifest = read_csv(checkpoint["base"], "manifesto.csv")
        total_sources += len(manifest)
        if {row.get("record_id") for row in manifest} != checkpoint["records"]:
            errors.append(f"{code}: manifest record identifiers differ from checkpoint scope")
        for row in manifest:
            path = ROOT / row.get("local_path", "")
            if not path.is_file(): errors.append(f"{code}: missing manifested source: {row.get('local_path')}")
            elif sha256(path) != row.get("sha256"): errors.append(f"{code}: SHA-256 mismatch: {row.get('local_path')}")
            if row.get("institution") != "Universidade Federal do Paraná": errors.append(f"{code}: non-UFPR institution: {row.get('record_id')}")
            if not row.get("source_url", "").startswith("https://www.inf.ufpr.br/"): errors.append(f"{code}: non-official source URL: {row.get('record_id')}")
            if not row.get("accessed_at") or not row.get("document_type") or not row.get("purpose"): errors.append(f"{code}: incomplete provenance: {row.get('record_id')}")
        by_id = {row.get("record_id"): row for row in manifest}
        if by_id.get(checkpoint["f1"], {}).get("document_type") != "Ficha 1": errors.append(f"{code}: permanent document must remain Ficha 1")
        if by_id.get(checkpoint["f1"], {}).get("status") != "preserved_indeterminate": errors.append(f"{code}: Ficha 1 curriculum applicability must remain indeterminate")
        if by_id.get(checkpoint["f2"], {}).get("document_type") != "Ficha 2": errors.append(f"{code}: separate plan must remain Ficha 2")
        if checkpoint["f2_context"] not in by_id.get(checkpoint["f2"], {}).get("notes", ""): errors.append(f"{code}: Ficha 2 must retain source-stated course context")
        searches = read_csv(checkpoint["base"], "buscas-negativas.csv")
        expected_searches = {f"W022-{code}-01", f"W022-{code}-02", f"W022-{code}-03"}
        if {row.get("search_id") for row in searches} != expected_searches or len(searches) != 3: errors.append(f"{code}: checkpoint must record exactly three targeted attempts")
        for row in searches:
            if row.get("targets") != code: errors.append(f"{code}: out-of-scope search target: {row.get('search_id')}")
            for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
                if not row.get(field): errors.append(f"{code}: missing {field}: {row.get('search_id')}")
    if errors:
        for error in errors: print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"W022 checkpoint B validation passed: CI055, CI056, and CI057 have three targeted attempts each and {total_sources} separately preserved, hashed official sources; Ficha 1/Ficha 2 applicability limits remain explicit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
