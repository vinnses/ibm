#!/usr/bin/env python3
"""Validate W011 administrative-register invariants."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "administracao/historico"


def digest(path: Path) -> str:
    hash_ = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hash_.update(chunk)
    return hash_.hexdigest()


def rows(name: str) -> list[dict[str, str]]:
    with (BASE / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    errors: list[str] = []
    sources = {row["id"]: row for row in rows("fontes/manifesto.csv")}
    for identifier, row in sources.items():
        if row["status"] != "preserved":
            errors.append(f"source {identifier}: unexpected status {row['status']}")
            continue
        path = ROOT / row["local_path"]
        if not path.is_file():
            errors.append(f"source {identifier}: missing {row['local_path']}")
        elif digest(path) != row["sha256"]:
            errors.append(f"source {identifier}: SHA-256 mismatch")

    negative = {row["id"] for row in rows("buscas-negativas.csv")}
    transitions = rows("transicoes.csv")
    proposal_stages = {row["stage"]: row for row in transitions if row["object"] == "Reorganização para Inteligência Artificial Aplicada à Saúde"}
    required_stages = {"proposal", "selected", "approved", "authorized", "implemented"}
    if set(proposal_stages) != required_stages:
        errors.append("proposal stages must be exactly proposal/selected/approved/authorized/implemented")
    for row in transitions:
        source_id = row["source_id"]
        if row["status"] == "proven" and source_id not in sources:
            errors.append(f"transition {row['id']}: unknown preserved source {source_id}")
        if row["status"] == "not_located" and source_id not in negative:
            errors.append(f"transition {row['id']}: unknown negative-search record {source_id}")

    for name in ("avaliacoes.csv", "series-complementares.csv"):
        for row in rows(name):
            source_id = row["source_id"]
            if row["status"] == "proven" and source_id not in sources:
                errors.append(f"{name} {row['id']}: unknown preserved source {source_id}")
            if row["status"] == "not_located" and source_id not in negative:
                errors.append(f"{name} {row['id']}: unknown negative-search record {source_id}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked {len(sources)} source hashes, {len(transitions)} transitions, and {len(negative)} negative searches; errors={len(errors)}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
