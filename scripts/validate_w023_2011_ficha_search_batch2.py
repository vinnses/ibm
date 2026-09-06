#!/usr/bin/env python3
"""Validate W023 checkpoints B-D's CI241, CI243, and CI244 records."""

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
    ci241 = ROOT / "curriculos/2011/fichas/w023-ci241"
    manifest = read_csv(ci241, "manifesto.csv")
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
    searches = read_csv(ci241, "buscas-negativas.csv")
    expected = {"W023-CI241-01", "W023-CI241-02", "W023-CI241-03"}
    if len(searches) != 3 or {row.get("search_id") for row in searches} != expected:
        errors.append("CI241 must record exactly three new targeted attempts")
    for row in searches:
        if row.get("targets") != "CI241": errors.append(f"out-of-scope target: {row.get('search_id')}")
        for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
            if not row.get(field): errors.append(f"missing {field}: {row.get('search_id')}")
    ci243 = ROOT / "curriculos/2011/fichas/w023-ci243"
    ci243_manifest = read_csv(ci243, "manifesto.csv")
    if ci243_manifest:
        errors.append("CI243 manifest must remain empty unless a Ficha source is preserved")
    ci243_searches = read_csv(ci243, "buscas-negativas.csv")
    ci243_expected = {"W023-CI243-01", "W023-CI243-02", "W023-CI243-03"}
    if len(ci243_searches) != 3 or {row.get("search_id") for row in ci243_searches} != ci243_expected:
        errors.append("CI243 must record exactly three new targeted attempts")
    for row in ci243_searches:
        if row.get("targets") != "CI243": errors.append(f"CI243 out-of-scope target: {row.get('search_id')}")
        for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
            if not row.get(field): errors.append(f"CI243 missing {field}: {row.get('search_id')}")
    ci244 = ROOT / "curriculos/2011/fichas/w023-ci244"
    ci244_manifest = read_csv(ci244, "manifesto.csv")
    ci244_ids = {"W023-CI244-F1-2011", "W023-CI244-F2-2011-1"}
    if len(ci244_manifest) != 2 or {row.get("record_id") for row in ci244_manifest} != ci244_ids:
        errors.append("CI244 manifest must contain the separately preserved Ficha 1 and Ficha 2")
    ci244_by_id = {row.get("record_id"): row for row in ci244_manifest}
    for row in ci244_manifest:
        path = ROOT / row.get("local_path", "")
        if not path.is_file(): errors.append(f"CI244 missing manifested source: {row.get('local_path')}")
        elif sha256(path) != row.get("sha256"): errors.append(f"CI244 SHA-256 mismatch: {row.get('local_path')}")
        if row.get("institution") != "Universidade Federal do Paraná": errors.append(f"CI244 non-UFPR institution: {row.get('record_id')}")
        if not row.get("source_url", "").startswith("https://www.inf.ufpr.br/"): errors.append(f"CI244 non-official source URL: {row.get('record_id')}")
    if ci244_by_id.get("W023-CI244-F1-2011", {}).get("document_type") != "Ficha 1": errors.append("CI244 permanent document must remain Ficha 1")
    if ci244_by_id.get("W023-CI244-F1-2011", {}).get("status") != "preserved_indeterminate": errors.append("CI244 Ficha 1 must retain indeterminate 96A applicability")
    if ci244_by_id.get("W023-CI244-F2-2011-1", {}).get("document_type") != "Ficha 2": errors.append("CI244 separate plan must remain Ficha 2")
    if "Ciência da Computação" not in ci244_by_id.get("W023-CI244-F2-2011-1", {}).get("notes", ""): errors.append("CI244 Ficha 2 must retain its source-stated course context")
    ci244_searches = read_csv(ci244, "buscas-negativas.csv")
    ci244_expected = {"W023-CI244-01", "W023-CI244-02", "W023-CI244-03"}
    if len(ci244_searches) != 3 or {row.get("search_id") for row in ci244_searches} != ci244_expected:
        errors.append("CI244 must record exactly three new targeted attempts")
    for row in ci244_searches:
        if row.get("targets") != "CI244": errors.append(f"CI244 out-of-scope target: {row.get('search_id')}")
        for field in ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence"):
            if not row.get(field): errors.append(f"CI244 missing {field}: {row.get('search_id')}")
    if errors:
        for error in errors: print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("W023 checkpoint D validation passed: CI241 retains one 2025 Ficha 1, CI243 has an explicit no-source result, and CI244 preserves separate Ficha 1/Ficha 2 sources; each code has three new targeted attempts without 2011/96A inference.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
