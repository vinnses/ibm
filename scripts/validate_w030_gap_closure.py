#!/usr/bin/env python3
"""Validate W030's exhaustive documentary-gap classification."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLASSIFICATION = ROOT / "governance/reviews/W030-gap-classification.csv"
ACCESS_GAPS = ROOT / "dados/acesso/gaps.csv"
FINAL_STATUSES = {
    "closed",
    "deferred_access",
    "not_located_public_search_exhausted",
    "new_lead_required",
    "out_of_scope_for_data_phase",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def identifiers(rows: list[dict[str, str]]) -> set[str]:
    values: set[str] = set()
    for row in rows:
        values.update(item.strip() for item in row["related_gap_ids"].split(";") if item.strip())
    return values


def main() -> int:
    errors: list[str] = []
    if not CLASSIFICATION.is_file():
        print(f"ERROR: missing classification: {CLASSIFICATION.relative_to(ROOT)}")
        return 1
    rows = read_csv(CLASSIFICATION)
    required = {
        "classification_id", "related_gap_ids", "status", "provenance", "reason",
        "current_agent_actionability", "new_lead_or_access_criterion",
    }
    header = set(rows[0]) if rows else set()
    if not rows:
        errors.append("classification is empty")
    elif missing := required - header:
        errors.append(f"classification missing columns: {', '.join(sorted(missing))}")
    ids = [row.get("classification_id", "") for row in rows]
    if len(ids) != len(set(ids)) or any(not item for item in ids):
        errors.append("classification IDs are missing or non-unique")
    for row in rows:
        for field in required - {"classification_id"}:
            if not row.get(field, "").strip():
                errors.append(f"{row.get('classification_id', '<unknown>')}: blank {field}")
        if row.get("status") not in FINAL_STATUSES:
            errors.append(
                f"{row.get('classification_id', '<unknown>')}: non-final status "
                f"{row.get('status', '')!r}"
            )
        if row.get("current_agent_actionability", "").strip().lower().startswith("yes"):
            errors.append(f"{row.get('classification_id', '<unknown>')}: remaining agent-actionable task")
    expected = {row["gap_id"] for row in read_csv(ACCESS_GAPS)}
    listed = identifiers(rows)
    missing = expected - listed
    if missing:
        errors.append("access gap IDs absent from classification: " + ", ".join(sorted(missing)))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"W030 gap-closure validation: OK ({len(rows)} classifications; {len(expected)} access gap IDs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
