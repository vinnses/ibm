#!/usr/bin/env python3
"""Validate W017 preserved 2011 ementa evidence and coverage."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "dados/curriculos/2011/ementas-preservadas"
EXPECTED_CI241 = (
    "A disciplina visa apresentar de forma introdutória os principais conceitos da arquitetura "
    "de computadores, seus componentes de hardware e representação interna de dados, "
    "funcionamento dos sistemas operacionais e redes de computadores."
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []
    generated = subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_w017_ementas_2011.py"), "--check"],
        capture_output=True,
        text=True,
    )
    if generated.returncode:
        errors.append(generated.stdout.strip() or generated.stderr.strip())

    components = read_csv(ROOT / "curriculos/2011/inventario/componentes.csv")
    evidence = read_csv(DATA / "evidencias.csv")
    coverage = read_csv(DATA / "cobertura.csv")
    applicability = read_csv(DATA / "aplicabilidade.csv")

    target_ids = {row["target_id"] for row in components}
    coverage_ids = {row["target_id"] for row in coverage}
    if len(components) != 41 or target_ids != coverage_ids or len(coverage) != 41:
        errors.append("coverage must match the 41 unique W009 targets exactly")

    expected_statuses = Counter(
        {
            "evidencia_parcial": 36,
            "documento_aplicabilidade_indeterminada": 1,
            "nenhuma_evidencia_preservada_suficiente": 4,
        }
    )
    statuses = Counter(row["coverage_status"] for row in coverage)
    if statuses != expected_statuses:
        errors.append(f"unexpected coverage status counts: {dict(statuses)}")

    if len(evidence) != 38 or len({row["evidence_id"] for row in evidence}) != 38:
        errors.append("evidence must contain 38 unique rows")
    portal = [row for row in evidence if row["evidence_id"].startswith("EMENTARIO-")]
    fichas = [row for row in evidence if row["document_type"].lower().startswith("ficha 1")]
    if len(portal) != 37 or len(fichas) != 1:
        errors.append("evidence must contain 37 portal rows and one Ficha 1 row")
    if any(
        row["ementa_literal"] != "Não consta"
        or row["ementa_normalized"]
        or row["ementa_presence"] != "ausente_na_fonte"
        for row in portal
    ):
        errors.append("all portal rows must preserve 'Não consta' without synthetic ementa text")

    if len(fichas) == 1:
        ficha = fichas[0]
        if ficha["code"] != "CI241" or ficha["ementa_normalized"] != EXPECTED_CI241:
            errors.append("CI241 Ficha 1 identity or normalized ementa differs from the source")
        if ficha["applicability_2011"] != "indeterminada":
            errors.append("the 2025 CI241 Ficha must remain indeterminate for 2011")

    for row in evidence:
        path = ROOT / row["source_path"]
        if not path.is_file():
            errors.append(f"missing evidence path: {row['source_path']}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != row["source_sha256"]:
            errors.append(f"hash mismatch: {row['source_path']}")
        if not row["source_locator"] or not row["applicability_justification"]:
            errors.append(f"missing locator/applicability rationale: {row['evidence_id']}")

    if len(applicability) != 40:
        errors.append("applicability register must contain 40 version-separated rows")
    applicability_counts = Counter(row["applicability_2011"] for row in applicability)
    if applicability_counts != Counter({"indeterminada": 38, "comprovada": 2}):
        errors.append(f"unexpected applicability counts: {dict(applicability_counts)}")
    for row in applicability:
        path = ROOT / row["source_path"]
        if not path.is_file():
            errors.append(f"missing applicability source: {row['source_path']}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != row["source_sha256"]:
            errors.append(f"applicability hash mismatch: {row['source_path']}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "W017 validation passed: 41 targets; 38 evidence rows; "
        "coverage complete=0 partial=36 indeterminate=1 contradictory=0 insufficient=4"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
