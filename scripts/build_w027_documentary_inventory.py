#!/usr/bin/env python3
"""Build the deterministic W027 documentary coverage inventory.

The three access catalogs are inputs only.  This script never rewrites them.
Run without arguments to rebuild the Markdown output, or with ``--check`` to
verify that the committed output is byte-for-byte reproducible.
"""

from __future__ import annotations

import argparse
import csv
import os
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "dados/acesso/datasets.csv"
SOURCES = ROOT / "dados/acesso/source-records.csv"
GAPS = ROOT / "dados/acesso/gaps.csv"
OUTPUT = ROOT / "dados/acesso/COBERTURA_DOCUMENTAL.md"

AXES = ("Curricular", "Administrative", "Propositive", "Cross-cutting")
SCOPES = (
    "administrative data or historical series",
    "curriculum inventory or formal structure",
    "curated global source catalog",
    "repository dataset",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def axis_for(path: str) -> str:
    value = path.lower()
    if "curric" in value or "ficha" in value or "ement" in value:
        return "Curricular"
    if "propost" in value or "chamada" in value or "feasibility" in value:
        return "Propositive"
    if "admin" in value or "inep" in value or "ufpr" in value or "histor" in value:
        return "Administrative"
    return "Cross-cutting"


def dataset_axis(row: dict[str, str]) -> str:
    return axis_for(row["path"])


def source_axis(row: dict[str, str]) -> str:
    return axis_for(" ".join((row.get("local_path", ""), row.get("document_type", ""), row.get("purpose", ""))))


def gap_axis(row: dict[str, str]) -> str:
    return axis_for(" ".join((row.get("target", ""), row.get("origin_path", ""), row.get("gap_type", ""))))


def md_table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |" for row in rows)
    return lines


def status_table(counter: Counter[str], empty: str = "(blank)") -> list[list[object]]:
    return [[key if key else empty, value] for key, value in sorted(counter.items(), key=lambda item: (item[0] == "", item[0]))]


def build_markdown() -> str:
    datasets = read_csv(DATASETS)
    sources = read_csv(SOURCES)
    gaps = read_csv(GAPS)

    dataset_scope = Counter(row["scope"] for row in datasets)
    dataset_axis_counts = Counter(dataset_axis(row) for row in datasets)
    dataset_rows_by_scope = defaultdict(int)
    dataset_rows_by_axis = defaultdict(int)
    for row in datasets:
        count = int(row["row_count"])
        dataset_rows_by_scope[row["scope"]] += count
        dataset_rows_by_axis[dataset_axis(row)] += count

    source_status = Counter(row.get("status", "") for row in sources)
    source_type = Counter(row.get("document_type", "") for row in sources)
    source_axis_counts = Counter(source_axis(row) for row in sources)
    source_path_present = sum(bool(row.get("local_path", "").strip()) for row in sources)
    source_path_existing = sum(
        bool(row.get("local_path", "").strip()) and (ROOT / row["local_path"]).is_file()
        for row in sources
    )
    source_url_present = sum(bool(row.get("source_url", "").strip()) for row in sources)
    source_hash_present = sum(bool(row.get("sha256", "").strip()) for row in sources)

    gap_type = Counter(row.get("gap_type", "") for row in gaps)
    gap_status = Counter(row.get("status", "") for row in gaps)
    gap_axis_counts = Counter(gap_axis(row) for row in gaps)

    lines: list[str] = [
        "# Documentary coverage inventory",
        "",
        "Generated mechanically by `scripts/build_w027_documentary_inventory.py` from the three access catalogs.",
        "",
        "## Reading rules",
        "",
        "- Counts below are catalog records. They are not counts of unique documents, unique sources, or completeness.",
        "- Source-manifest rows are retained as recorded; duplicate identities, conflicting metadata, Ficha 1/Ficha 2 versions, and different statistical universes are not merged.",
        "- A local path, URL, hash, or catalog row does not by itself establish applicability, approval, implementation, or historical completeness.",
        "- `path exists` is checked against the current repository checkout; it describes accessibility, not evidentiary sufficiency.",
        "",
        "## Current catalog totals",
        "",
    ]
    lines += md_table(
        ["Catalog", "Record count", "Meaning"],
        [
            ["datasets.csv", len(datasets), "dataset index records"],
            ["source-records.csv", len(sources), "preserved/source-manifest records"],
            ["gaps.csv", len(gaps), "recorded gap or bounded-search records"],
            ["datasets.csv declared rows", sum(int(row["row_count"]) for row in datasets), "rows declared by indexed datasets"],
        ]
    )
    lines += ["", "## Dataset records by scope", ""]
    lines += md_table(
        ["Scope", "Dataset records", "Declared rows"],
        [[scope, dataset_scope[scope], dataset_rows_by_scope[scope]] for scope in SCOPES if dataset_scope[scope]],
    )
    lines += ["", "## Dataset records by top-level documentary axis", ""]
    lines += md_table(
        ["Axis", "Dataset records", "Declared rows"],
        [[axis, dataset_axis_counts[axis], dataset_rows_by_axis[axis]] for axis in AXES],
    )

    lines += ["", "### Axis interpretation", "", "The axis is a deterministic path-based display grouping, not a claim that a record belongs exclusively to one historical question.", ""]
    lines += md_table(
        ["Axis", "Included path cues"],
        [
            ["Curricular", "curriculum, Ficha, ementa"],
            ["Administrative", "administracao, INEP, UFPR, historico"],
            ["Propositive", "proposta, chamada, feasibility"],
            ["Cross-cutting", "remaining catalog paths"],
        ],
    )

    lines += ["", "## Source-record preservation and path availability", ""]
    lines += md_table(
        ["Measure", "Records"],
        [
            ["Source records", len(sources)],
            ["Local path recorded", source_path_present],
            ["Recorded local path exists", source_path_existing],
            ["Source URL recorded", source_url_present],
            ["SHA-256 recorded", source_hash_present],
        ],
    )
    lines += ["", "### Source records by documentary axis", ""]
    lines += md_table(["Axis", "Records"], [[axis, source_axis_counts[axis]] for axis in AXES])
    lines += ["", "### Recorded source status", ""]
    lines += md_table(["Status", "Records"], status_table(source_status))
    lines += ["", "### Recorded source document type", ""]
    lines += md_table(["Document type", "Records"], status_table(source_type))

    lines += ["", "## Gap records", ""]
    lines += md_table(["Measure", "Records"], [["Gap records", len(gaps)]])
    lines += ["", "### Gap records by documentary axis", ""]
    lines += md_table(["Axis", "Records"], [[axis, gap_axis_counts[axis]] for axis in AXES])
    lines += ["", "### Gap type", ""]
    lines += md_table(["Gap type", "Records"], status_table(gap_type))
    lines += ["", "### Gap status", ""]
    lines += md_table(["Status", "Records"], status_table(gap_status))

    lines += [
        "",
        "## Documentary-delivery lanes",
        "",
        "- Repository-local extraction: use already preserved files and indexed datasets; do not alter the three input catalogs in this inventory task.",
        "- Concrete public lead: pursue only a specific, bounded lead recorded in the gap/search material; preserve any newly used source before extraction.",
        "- Institutional or user access: obtain records listed as institutional-access or requiring human clarification; the absence of a public record is not proof of nonexistence.",
        "- Documentary freeze: after the data-delivery batches, validate manifests, hashes, paths, version separation, and reproducibility. This is a documentary gate, not curricular analysis.",
        "- Comparative P3 and analytical P4 work remain future work requiring direct user participation and cannot begin implicitly from this inventory.",
        "",
        "## Rebuild and check",
        "",
        "```text",
        "python scripts/build_w027_documentary_inventory.py",
        "python scripts/build_w027_documentary_inventory.py --check",
        "python scripts/validate_w027_documentary_inventory.py",
        "```",
        "",
        "The builder uses only Python's standard library, reads the three CSV inputs as UTF-8, sorts every displayed category deterministically, and writes the generated Markdown with a final newline. The validator compares a freshly rendered result byte-for-byte with the committed Markdown and checks the input record totals.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check the generated output without writing it")
    args = parser.parse_args()
    rendered = build_markdown()
    if args.check:
        if not OUTPUT.is_file():
            raise SystemExit(f"missing generated output: {OUTPUT}")
        actual = OUTPUT.read_text(encoding="utf-8")
        if actual != rendered:
            raise SystemExit("generated output is stale; run the builder")
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
