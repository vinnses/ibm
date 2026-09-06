#!/usr/bin/env python3
"""Build or check the deterministic W028 documentary-release checksum manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "dados/entrega-documental"
OUTPUT = PACKAGE / "MANIFEST.sha256"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def release_paths() -> dict[str, str]:
    selected: dict[str, str] = {}
    for path in PACKAGE.rglob("*"):
        if path.is_file() and path != OUTPUT:
            selected[path.relative_to(ROOT).as_posix()] = "release-package"
    for relative in (
        "dados/acesso/datasets.csv",
        "dados/acesso/source-records.csv",
        "dados/acesso/gaps.csv",
        "dados/acesso/COBERTURA_DOCUMENTAL.md",
        "metodologia/criterios-documentais.md",
        "governance/DOCUMENTARY_DELIVERY_PLAN.md",
    ):
        selected[relative] = "release-control"
    for row in csv_rows(ROOT / "dados/acesso/datasets.csv"):
        selected[row["path"]] = "dataset"
    for row in csv_rows(ROOT / "dados/acesso/source-records.csv"):
        if row.get("local_path", "").strip():
            selected[row["local_path"]] = "preserved-source"
    return selected


def render() -> str:
    lines = ["# sha256  category  repository_path"]
    for relative, category in sorted(release_paths().items()):
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"missing release path: {relative}")
        lines.append(f"{sha256(path)}  {category}  {relative}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            raise SystemExit("release manifest is missing or stale")
    else:
        PACKAGE.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
