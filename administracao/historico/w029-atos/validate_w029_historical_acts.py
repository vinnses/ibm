#!/usr/bin/env python3
"""Validate W029's bounded historical-act recovery log."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_TARGETS = {"COUN19", "P44"}
EXPECTED_STATUSES = {
    "original_not_located",
    "original_dou_facsimile_not_located",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    searches = read_csv("buscas.csv")
    records = read_csv("registros.csv")
    errors: list[str] = []
    by_target: dict[str, list[dict[str, str]]] = {target: [] for target in EXPECTED_TARGETS}
    for row in searches:
        target = row.get("target_id", "")
        if target not in EXPECTED_TARGETS:
            errors.append(f"unexpected search target: {target!r}")
            continue
        by_target[target].append(row)
        if not row.get("official_domains") or not row.get("terms") or not row.get("limits"):
            errors.append(f"incomplete search record: {row.get('search_id', '')}")
    if len(searches) != 6:
        errors.append(f"expected 6 searches, found {len(searches)}")
    for target, rows in by_target.items():
        if len(rows) != 3:
            errors.append(f"expected 3 new searches for {target}, found {len(rows)}")
    if {row.get("target_id", "") for row in records} != EXPECTED_TARGETS:
        errors.append("target records do not exactly cover COUN19 and P44")
    for row in records:
        if row.get("status") not in EXPECTED_STATUSES:
            errors.append(f"unexpected status: {row.get('status', '')!r}")
        if row.get("search_count") != "3":
            errors.append(f"incorrect search count for {row.get('target_id', '')}")
        if "nonexistence" not in row.get("limits", ""):
            errors.append(f"missing nonexistence limit for {row.get('target_id', '')}")
    if errors:
        print("W029 historical-acts validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("W029 historical-acts validation passed: 2 targets, 6 bounded searches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
