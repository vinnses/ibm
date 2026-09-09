#!/usr/bin/env python3
"""Validate the W035 source preservation and epistemic editorial boundary."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REL = "argumentacao/fontes/pearson-aima-fourth-edition.html"
EXPECTED_SHA256 = "3e72f7725f19d338025e9c52754cf63bd28018d97687bb0ff7f7ef6976bcf242"


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    argument_path = ROOT / "argumentacao/linha-editorial-inicial.md"
    testimony_path = ROOT / "governance/research-hypotheses/2026-09-09-editorial-premises.md"
    source_path = ROOT / SOURCE_REL
    manifest_path = ROOT / "argumentacao/fontes/manifest.csv"
    proposal_path = ROOT / "dados/extracoes-w029/proposal-2026.json"

    for path in (argument_path, testimony_path, source_path, manifest_path, proposal_path):
        if not path.is_file() or path.is_symlink():
            errors.append(f"missing or invalid W035 input: {path.relative_to(ROOT)}")

    if errors:
        print("W035 editorial validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    actual_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
    if actual_hash != EXPECTED_SHA256:
        errors.append(f"unexpected Pearson source SHA-256: {actual_hash}")

    with manifest_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required_manifest_fields = {
        "title",
        "institution",
        "source_url",
        "access_date",
        "document_date_or_version",
        "document_type",
        "local_path",
        "sha256",
        "evidentiary_purpose",
    }
    if len(rows) != 1 or set(rows[0]) != required_manifest_fields:
        errors.append("unexpected W035 source manifest structure")
    else:
        row = rows[0]
        if row["local_path"] != SOURCE_REL or row["sha256"] != EXPECTED_SHA256:
            errors.append("W035 manifest does not bind the preserved source and hash")
        if row["institution"] != "Pearson" or row["access_date"] != "2026-09-09":
            errors.append("W035 manifest has unexpected provenance metadata")
        if not row["source_url"].startswith("https://www.pearson.com/"):
            errors.append("W035 manifest source is not the official Pearson page")

    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))["proposal"]
    if proposal.get("current_hours_stated") != 3200:
        errors.append("W029 proposal extraction no longer states 3,200 current hours")
    if proposal.get("proposed_hours_stated") != 2700:
        errors.append("W029 proposal extraction no longer states 2,700 proposed hours")
    if proposal.get("evidence_status") != "proposal_statement_only":
        errors.append("W029 proposal status was upgraded beyond proposal statement")
    if not any("matrix" in item.lower() and "not provided" in item.lower() for item in proposal.get("limits", [])):
        errors.append("W029 proposal extraction no longer records the missing matrix")

    argument = argument_path.read_text(encoding="utf-8")
    testimony = testimony_path.read_text(encoding="utf-8")
    required_argument_markers = [
        "Fato documentado",
        "Declaração da proposta",
        "Testemunho da parte interessada",
        "Interpretação estratégica da parte interessada",
        "Proposta normativa",
        "2.700 horas sejam um teto imposto",
        "não contém a matriz proposta",
        "não uma lista\naprovada de disciplinas",
        "não fixa horas",
        "Fundamentos e agentes",
        "Resolução de problemas, busca e otimização",
        "Conhecimento, raciocínio e planejamento",
        "Incerteza e decisão",
        "Aprendizagem",
        "Comunicação, percepção e ação",
        "1–2",
        "3–6",
        "7–11",
        "12–18",
        "19–22",
        "23–25",
        "26–27",
    ]
    for marker in required_argument_markers:
        if marker not in argument:
            errors.append(f"editorial argument is missing required marker: {marker}")

    required_testimony_markers = [
        "stakeholder testimony",
        "Not established by this record",
        "MEC-imposed 2,700-hour maximum",
        "Biological Sciences Sector",
        "Health Sciences Sector",
    ]
    for marker in required_testimony_markers:
        if marker not in testimony:
            errors.append(f"stakeholder record is missing required marker: {marker}")

    if "2.700 horas são o máximo" in argument or "MEC limita o curso a 2.700" in argument:
        errors.append("editorial argument asserts an unproven MEC maximum")
    if "Setor de Ciências Biológicas recusou" in argument or "Setor de Ciências da Saúde recusou" in argument:
        errors.append("editorial argument upgrades stakeholder testimony to institutional fact")

    if errors:
        print("W035 editorial validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("W035 editorial validation passed:")
    print("- 1 official publisher source is preserved and hash-bound")
    print("- W029 hours remain 3,200 current / 2,700 proposal-stated")
    print("- 2,700 is not represented as a proven MEC ceiling")
    print("- stakeholder testimony, interpretation, fact, and normative proposal remain distinct")
    print("- the six-block AIMA reading is provisional and contains no fixed workload")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
