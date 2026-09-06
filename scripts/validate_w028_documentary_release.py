#!/usr/bin/env python3
"""Validate W028 N2-N6 package coverage and declared source/dataset hashes."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "dados/entrega-documental"


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    required = [
        PACKAGE / "README.md",
        PACKAGE / "STATUS_EXTRACAO.md",
        PACKAGE / "SOLICITACOES_E_LACUNAS.md",
        PACKAGE / "AUDITORIA_E_CONGELAMENTO.md",
        PACKAGE / "VALIDACAO.md",
        PACKAGE / "MANIFEST.sha256",
        PACKAGE / "eixos/curriculo-2011.md",
        PACKAGE / "eixos/curriculo-2023.md",
        PACKAGE / "eixos/administracao.md",
        PACKAGE / "eixos/proposta-2026.md",
    ]
    for path in required:
        require(path.is_file() and path.stat().st_size > 0, f"missing release deliverable: {path.relative_to(ROOT)}")

    sources = rows(ROOT / "dados/acesso/source-records.csv")
    datasets = rows(ROOT / "dados/acesso/datasets.csv")
    gaps = rows(ROOT / "dados/acesso/gaps.csv")
    for row in sources:
        path = ROOT / row["local_path"]
        require(path.is_file(), f"missing preserved source: {row['local_path']}")
        require(digest(path) == row["sha256"], f"source hash mismatch: {row['local_path']}")
    for row in datasets:
        path = ROOT / row["path"]
        require(path.is_file(), f"missing dataset: {row['path']}")
        require(digest(path) == row["sha256"], f"dataset hash mismatch: {row['path']}")

    extraction = (PACKAGE / "STATUS_EXTRACAO.md").read_text(encoding="utf-8")
    for status in ("structured", "partially_structured", "deferred_access", "deferred_tooling", "not_applicable"):
        require(status in extraction, f"missing extraction status vocabulary: {status}")
    requests = (PACKAGE / "SOLICITACOES_E_LACUNAS.md").read_text(encoding="utf-8")
    for row in gaps:
        require(row["gap_id"] in requests, f"gap not routed in request package: {row['gap_id']}")

    subprocess.run([sys.executable, str(ROOT / "scripts/build_w028_release_manifest.py"), "--check"], check=True)
    print(f"W028 release validation passed: {len(datasets)} datasets, {len(sources)} source records, {len(gaps)} gaps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
