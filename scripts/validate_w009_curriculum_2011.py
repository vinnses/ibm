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
    edges: dict[str, set[str]] = {code: set() for code in component_codes}
    for row in rows("curriculos/2011/inventario/dependencias.csv"):
        for endpoint in (row["from_target"], row["to_target"]):
            if endpoint != "BLOCK-A" and endpoint not in component_codes:
                errors.append(f"dependency endpoint not in coded inventory: {endpoint}")
        if row["relation"] == "prerequisite":
            edges[row["from_target"]].add(row["to_target"])
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
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked {len(components)} targets, {len(component_codes)} codes, and local W009 manifests; errors={len(errors)}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
