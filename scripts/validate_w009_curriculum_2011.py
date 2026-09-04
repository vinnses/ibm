#!/usr/bin/env python3
"""Validate W009's local 2011 curriculum inventory invariants."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def rows(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    errors: list[str] = []
    components = rows("curriculos/2011/inventario/componentes.csv")
    if len(components) != 41:
        errors.append(f"expected 41 inventory targets, found {len(components)}")
    identifiers = [row["target_id"] for row in components]
    if len(set(identifiers)) != len(identifiers):
        errors.append("duplicate inventory target identifier")
    coded = [row for row in components if row["target_type"] == "coded_component"]
    elective_spaces = [row for row in components if row["target_type"] == "elective_space"]
    if len(coded) != 37 or len(elective_spaces) != 4:
        errors.append("inventory does not contain exactly 37 coded components and four elective spaces")
    for row in components:
        if not row["status"] or not row["formal_evidence_path"] or not row["applicability"]:
            errors.append(f"incomplete evidence/status fields: {row['target_id']}")
        if row["target_type"] == "coded_component" and not row["ficha1_status"]:
            errors.append(f"missing Ficha 1 state: {row['target_id']}")
    component_codes = {row["code"] for row in coded}
    target_ids = set(identifiers)
    required_attribute_columns = {"total_hours", "weekly_total_hours", "credits"}
    if not required_attribute_columns.issubset(components[0] if components else {}):
        errors.append("component inventory does not separate total hours, weekly total hours, and credits")
    for row in components:
        for column in required_attribute_columns:
            if not row.get(column, "").isdigit() or int(row[column]) <= 0:
                errors.append(f"invalid {column}: {row['target_id']}")
    expected_credits = {
        "CI241": 3, "CI055": 3, "CM201": 4, "CM045": 4, "BA040": 3,
        "CI243": 3, "CI056": 3, "CI067": 3, "CM005": 4, "BQ005": 4,
        "CI244": 3, "CI057": 3, "CI166": 3, "BQ054": 4, "BC056": 3,
        "CI215": 3, "CI062": 3, "CE003": 4, "CI164": 3, "BF075": 4,
        "BG054": 3, "CI162": 3, "CI065": 3, "CI171": 3, "CI316": 3,
        "MN127": 4, "CI167": 3, "CI209": 3, "CI218": 3, "CI394": 3,
        "MN128": 4, "CI220": 3, "CI221": 3, "CI169": 3, "CI172": 3,
        "MN129": 4, "CI262": 6,
    }
    for row in coded:
        if int(row["credits"]) != expected_credits.get(row["code"], -1):
            errors.append(f"credits do not reproduce Anexo I Créd. value: {row['code']}")
    for row in elective_spaces:
        if (row["total_hours"], row["weekly_total_hours"], row["credits"]) != ("60", "4", "4"):
            errors.append(f"elective slot attributes do not reproduce Anexo I: {row['target_id']}")
    block_a = {
        "CI241", "CI055", "CM201", "CM045", "BA040", "CM005", "BQ005", "BQ054",
        "BC056", "CI166", "CI056", "CI057", "CI067", "CI243", "CI244",
    }
    if len(block_a) != 15:
        errors.append("internal validator error: Bloco A membership set must contain 15 components")
    edges: dict[str, set[str]] = {code: set() for code in component_codes}
    hidden_targets: set[str] = set()
    for row in rows("curriculos/2011/inventario/dependencias.csv"):
        for endpoint in (row["from_target"], row["to_target"]):
            if endpoint != "BLOCK-A" and endpoint not in target_ids:
                errors.append(f"dependency endpoint not in inventory: {endpoint}")
        if row["relation"] == "prerequisite":
            edges[row["from_target"]].add(row["to_target"])
        if row["relation"] == "hidden_requirement":
            if row["from_target"] != "BLOCK-A":
                errors.append(f"hidden requirement does not originate at BLOCK-A: {row['dependency_id']}")
            hidden_targets.add(row["to_target"])
            if row["to_target"] in block_a:
                errors.append(f"Bloco A rule incorrectly targets its own member: {row['to_target']}")
            if row["to_target"] in {entry["target_id"] for entry in elective_spaces} and "selected" not in row["notes"]:
                errors.append(f"elective-space Bloco A row lacks conditional mapping note: {row['to_target']}")
    expected_hidden_targets = target_ids - block_a
    if hidden_targets != expected_hidden_targets:
        missing = sorted(expected_hidden_targets - hidden_targets)
        extra = sorted(hidden_targets - expected_hidden_targets)
        errors.append(f"Bloco A targets differ from all non-members; missing={missing}, extra={extra}")
    if len(hidden_targets) != 26:
        errors.append(f"expected 26 Bloco A targets (22 coded components and four elective spaces), found {len(hidden_targets)}")
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"prerequisite cycle includes: {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for successor in edges[node]:
            visit(successor)
        visiting.remove(node)
        visited.add(node)
    for code in component_codes:
        visit(code)
    for manifest in ("curriculos/2011/fontes/manifesto.csv", "curriculos/2011/fichas/manifesto.csv"):
        for row in rows(manifest):
            path = ROOT / row["local_path"]
            if not path.is_file():
                errors.append(f"missing manifested file: {row['local_path']}")
            elif digest(path) != row["sha256"]:
                errors.append(f"manifest SHA-256 mismatch: {row['local_path']}")
    divergences = rows("curriculos/2011/inventario/divergencias.csv")
    if len(divergences) != 1:
        errors.append(f"expected one workload divergence record, found {len(divergences)}")
    elif divergences[0].get("classification") != "contradictory":
        errors.append("workload divergence is not classified contradictory")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"Checked {len(components)} targets, {len(component_codes)} codes, "
        f"{len(hidden_targets)} Bloco A targets, one workload divergence, and local W009 manifests; errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
