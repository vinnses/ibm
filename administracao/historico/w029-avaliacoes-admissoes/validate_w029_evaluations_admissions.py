#!/usr/bin/env python3
"""Validate W029's bounded evaluation and admissions recovery lane."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGETS = {
    "EMEC_DETAIL",
    "ENADE_RESULT",
    "APPLICANTS_2018",
    "APPLICANTS_2025",
    "APPLICANTS_2026",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    searches = read_csv("buscas.csv")
    records = read_csv("registros.csv")
    manifest = read_csv("manifesto.csv")
    errors: list[str] = []
    by_target = {target: [] for target in TARGETS}
    for row in searches:
        target = row.get("target_id", "")
        if target not in TARGETS:
            errors.append(f"unexpected search target: {target!r}")
            continue
        by_target[target].append(row)
        for field in ("search_id", "accessed_at", "official_domains", "terms_or_endpoint", "result", "limits"):
            if not row.get(field):
                errors.append(f"incomplete search record {row.get('search_id', '')}: {field}")
    if len(searches) != 15:
        errors.append(f"expected 15 searches, found {len(searches)}")
    for target, rows in by_target.items():
        if len(rows) != 3:
            errors.append(f"expected three new searches for {target}, found {len(rows)}")
    if {row.get("target_id", "") for row in records} != TARGETS:
        errors.append("records do not exactly cover the five targets")
    for row in records:
        if row.get("status") != "not_located":
            errors.append(f"unexpected status for {row.get('target_id', '')}")
        if row.get("search_count") != "3":
            errors.append(f"incorrect search count for {row.get('target_id', '')}")
        if "nonexistence" not in row.get("limits", ""):
            errors.append(f"missing nonexistence limit for {row.get('target_id', '')}")
    if manifest:
        errors.append("manifest must be header-only when no qualifying source was preserved")
    if errors:
        print("W029 evaluations/admissions validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("W029 evaluations/admissions validation passed: 5 targets, 15 bounded searches, 0 new sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
