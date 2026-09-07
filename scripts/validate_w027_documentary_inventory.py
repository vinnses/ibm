#!/usr/bin/env python3
"""Validate the W027 generated documentary coverage inventory."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "scripts/build_w027_documentary_inventory.py"
OUTPUT = ROOT / "dados/acesso/COBERTURA_DOCUMENTAL.md"


def load_builder():
    spec = importlib.util.spec_from_file_location("w027_builder", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BUILDER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    builder = load_builder()
    expected = builder.build_markdown()
    if not OUTPUT.is_file():
        raise SystemExit(f"missing generated output: {OUTPUT}")
    actual = OUTPUT.read_text(encoding="utf-8")
    if actual != expected:
        raise SystemExit("COBERTURA_DOCUMENTAL.md is not deterministic/current")

    datasets = rows(builder.DATASETS)
    sources = rows(builder.SOURCES)
    gaps = rows(builder.GAPS)
    expected_counts = {"datasets": 209, "sources": 191, "gaps": 33}
    actual_counts = {"datasets": len(datasets), "sources": len(sources), "gaps": len(gaps)}
    if actual_counts != expected_counts:
        raise SystemExit(f"unexpected catalog counts: {actual_counts}; expected {expected_counts}")
    for row in datasets:
        try:
            int(row["row_count"])
        except (KeyError, TypeError, ValueError) as exc:
            raise SystemExit(f"invalid dataset row_count: {row}") from exc
    if not all(row.get("record_id", "").strip() for row in sources):
        raise SystemExit("source-records.csv contains a blank record_id")
    if not all(row.get("gap_id", "").strip() for row in gaps):
        raise SystemExit("gaps.csv contains a blank gap_id")
    print("W027 documentary inventory: PASS (deterministic output; 209 datasets, 191 source records, 33 gaps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
