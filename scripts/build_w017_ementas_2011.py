#!/usr/bin/env python3
"""Build the W017 preserved 2011 ementa evidence datasets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "dados/curriculos/2011/ementas-preservadas"
COMPONENTS = ROOT / "curriculos/2011/inventario/componentes.csv"
SOURCE_MANIFEST = ROOT / "curriculos/2011/fontes/manifesto.csv"
FICHA_MANIFEST = ROOT / "curriculos/2011/fichas/manifesto.csv"
FICHA_PATH = ROOT / (
    "curriculos/2011/fichas/ficha-1-indeterminada/"
    "CI241-ficha-1-2025-3-periodo.pdf"
)

EVIDENCE_FIELDS = [
    "evidence_id",
    "target_id",
    "code",
    "document_title",
    "name_literal",
    "ementa_literal",
    "ementa_normalized",
    "ementa_presence",
    "total_hours",
    "weekly_hours",
    "credits",
    "nature_literal",
    "unit_literal",
    "unit_normalized",
    "prerequisites_literal",
    "corequisites_literal",
    "document_type",
    "document_date",
    "document_version",
    "source_url",
    "accessed_at",
    "source_path",
    "source_sha256",
    "source_locator",
    "applicability_2011",
    "applicability_justification",
    "observations",
]

COVERAGE_FIELDS = [
    "target_id",
    "target_type",
    "code",
    "w009_target_label",
    "coverage_status",
    "evidence_count",
    "ementa_content_records",
    "ficha1_records",
    "primary_evidence_ids",
    "formal_context_path",
    "applicability_summary",
    "gap_or_note",
]

APPLICABILITY_FIELDS = [
    "record_id",
    "target_scope",
    "document_title",
    "document_type",
    "document_date_or_version",
    "source_path",
    "source_sha256",
    "applicability_2011",
    "supported_use",
    "justification",
    "version_relationship",
]


class TextCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if text:
            self.parts.append(text)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def capture(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not extract pattern: {pattern}")
    return match.group(1).strip()


def parse_ementario(path: Path) -> dict[str, str]:
    parser = TextCollector()
    parser.feed(path.read_text(encoding="utf-8"))
    text = " | ".join(parser.parts)
    return {
        "name": capture(
            text,
            r"Informações Gerais \| Disciplina \| (.*?)\s*\(\s*[A-Z]{2,5}\d{3}\s*\)",
        ),
        "code": capture(
            text,
            r"Informações Gerais \| Disciplina \| .*?\(\s*([A-Z]{2,5}\d{3})\s*\)",
        ).upper(),
        "unit": capture(text, r"\) \| Unidade \| (.*?) \| Tipo"),
        "nature": capture(text, r"\| Tipo \| (.*?) \| Período Ideal"),
        "term": capture(text, r"Período Ideal no Curso \| (.*?) \| Nota Mínima"),
        "total_hours": capture(text, r"Carga Horária \| (.*?) \| Nº de Créditos"),
        "credits": capture(text, r"Nº de Créditos \| (.*?) \| Docentes"),
        "ementa": capture(text, r"Ementa \| (.*?) \| Programa"),
        "objectives": capture(text, r"Objetivos \| (.*?) \| Ementa"),
    }


def extract_ci241_ementa() -> tuple[str, str]:
    result = subprocess.run(
        [
            "pdftotext",
            "-f",
            "24",
            "-l",
            "25",
            "-layout",
            str(FICHA_PATH),
            "-",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"EMENTA\s+(.*?)\n\s*Professores:", result.stdout, re.DOTALL)
    if not match:
        raise ValueError("Could not locate the CI241 ementa on PDF pages 24-25")
    literal = "\n".join(line.strip() for line in match.group(1).splitlines() if line.strip())
    normalized = " ".join(literal.split())
    return literal, normalized


def build_rows() -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    components = read_csv(COMPONENTS)
    targets = {row["code"]: row for row in components if row["code"]}
    source_rows = {row["local_path"]: row for row in read_csv(SOURCE_MANIFEST)}
    ficha_row = read_csv(FICHA_MANIFEST)[0]

    evidence: list[dict[str, str]] = []
    html_dir = ROOT / "curriculos/2011/fontes/ementario/disciplinas"
    for path in sorted(html_dir.glob("*.html")):
        parsed = parse_ementario(path)
        code = parsed["code"]
        if code not in targets:
            raise ValueError(f"Unexpected Ementário code {code}: {path}")
        relative = path.relative_to(ROOT).as_posix()
        manifest = source_rows[relative]
        evidence.append(
            {
                "evidence_id": f"EMENTARIO-{code}-2026-09-04",
                "target_id": targets[code]["target_id"],
                "code": code,
                "document_title": manifest["title"],
                "name_literal": parsed["name"],
                "ementa_literal": parsed["ementa"],
                "ementa_normalized": "",
                "ementa_presence": "ausente_na_fonte",
                "total_hours": parsed["total_hours"],
                "weekly_hours": "",
                "credits": parsed["credits"],
                "nature_literal": parsed["nature"],
                "unit_literal": parsed["unit"],
                "unit_normalized": parsed["unit"],
                "prerequisites_literal": "",
                "corequisites_literal": "",
                "document_type": manifest["document_type"],
                "document_date": manifest["document_date"],
                "document_version": (
                    "Current 96A portal representation captured 2026-09-04; "
                    "date and validity not stated"
                ),
                "source_url": manifest["source_url"],
                "accessed_at": manifest["accessed_at"],
                "source_path": relative,
                "source_sha256": manifest["sha256"],
                "source_locator": "Informações Gerais table; Ementa section",
                "applicability_2011": "indeterminada",
                "applicability_justification": (
                    "The preserved page is a current 96A portal representation with no stated "
                    "historical date or validity; matching code and curriculum display do not "
                    "establish that these fields governed in 2011."
                ),
                "observations": (
                    "The Ementa and Objetivos fields display 'Não consta'. The page does not "
                    "display prerequisites or corequisites."
                ),
            }
        )

    literal, normalized = extract_ci241_ementa()
    ficha_relative = FICHA_PATH.relative_to(ROOT).as_posix()
    evidence.append(
        {
            "evidence_id": "FICHA1-CI241-2025-05-14",
            "target_id": "CI241",
            "code": "CI241",
            "document_title": "Ficha 1 (permanente) — Introdução a Sistemas Computacionais",
            "name_literal": "Introdução a Sistemas Computacionais",
            "ementa_literal": literal,
            "ementa_normalized": normalized,
            "ementa_presence": "presente",
            "total_hours": "60",
            "weekly_hours": "04",
            "credits": "",
            "nature_literal": "Obrigatória; Semestral; Totalmente Presencial",
            "unit_literal": "Coordenação do Curso de ou Departamento de Informática",
            "unit_normalized": "Departamento de Informática",
            "prerequisites_literal": "Não",
            "corequisites_literal": "Não",
            "document_type": ficha_row["document_type"],
            "document_date": ficha_row["document_date"],
            "document_version": "Multi-course PDF; CI241 section signed 2025-05-14",
            "source_url": ficha_row["source_url"],
            "accessed_at": "2026-09-04",
            "source_path": ficha_relative,
            "source_sha256": ficha_row["sha256"],
            "source_locator": (
                "PDF pages 24-25: Disciplina, Natureza, Pré-requisito, Co-requisito and CH "
                "on page 24; EMENTA and electronic signature on page 25"
            ),
            "applicability_2011": "indeterminada",
            "applicability_justification": (
                "The Ficha is signed in 2025. Code and title continuity do not establish its "
                "validity for the 2011 curriculum."
            ),
            "observations": (
                "CI241 is one section of a 27-page multi-course PDF. Credits are not stated in "
                "the Ficha. The source is preserved without alteration."
            ),
        }
    )

    by_target: dict[str, list[dict[str, str]]] = {}
    for row in evidence:
        by_target.setdefault(row["target_id"], []).append(row)

    coverage: list[dict[str, str]] = []
    for component in components:
        target_id = component["target_id"]
        rows = by_target.get(target_id, [])
        if target_id == "CI241":
            status = "documento_aplicabilidade_indeterminada"
            summary = (
                "A 2025 Ficha 1 contains an ementa, but no preserved evidence links that "
                "version to 2011; the current portal record displays 'Não consta'."
            )
            gap = "Applicable 2011 Ficha 1/version evidence is not preserved."
        elif component["target_type"] == "coded_component":
            status = "evidencia_parcial"
            summary = (
                "The 2010 act proves the formal target; the current portal page preserves "
                "metadata but displays 'Não consta' for Ementa and has indeterminate 2011 validity."
            )
            gap = "No ementa-bearing Ficha 1 proven applicable to 2011 is preserved."
        else:
            status = "nenhuma_evidencia_preservada_suficiente"
            summary = (
                "The 2010 act proves an elective space, not a selected coded component or a "
                "component-level ementa/Ficha 1."
            )
            gap = "No selected elective component or corresponding ementa/Ficha 1 is identified."
        coverage.append(
            {
                "target_id": target_id,
                "target_type": component["target_type"],
                "code": component["code"],
                "w009_target_label": component["title"],
                "coverage_status": status,
                "evidence_count": str(len(rows)),
                "ementa_content_records": str(
                    sum(row["ementa_presence"] == "presente" for row in rows)
                ),
                "ficha1_records": str(
                    sum(row["document_type"].lower().startswith("ficha 1") for row in rows)
                ),
                "primary_evidence_ids": "|".join(row["evidence_id"] for row in rows),
                "formal_context_path": component["formal_evidence_path"],
                "applicability_summary": summary,
                "gap_or_note": gap,
            }
        )

    resolution = source_rows["curriculos/2011/fontes/resolucao-34-2010-cepe.pdf"]
    ppc = source_rows["curriculos/2011/fontes/ppc-2011.pdf"]
    applicability = [
        {
            "record_id": "APP-RES34-2010",
            "target_scope": "all 41 W009 targets",
            "document_title": resolution["title"],
            "document_type": resolution["document_type"],
            "document_date_or_version": resolution["document_date"],
            "source_path": resolution["local_path"],
            "source_sha256": resolution["sha256"],
            "applicability_2011": "comprovada",
            "supported_use": (
                "Formal 2011 curriculum identity, 37 coded components, four elective spaces, "
                "workloads, periodization, credits and stated prerequisites; no ementas or Fichas."
            ),
            "justification": "Article 5 states that the resolution enters into force in academic year 2011.",
            "version_relationship": "Primary 2011 curriculum act; controls formal structure.",
        },
        {
            "record_id": "APP-PPC-2010",
            "target_scope": "2011 curriculum context",
            "document_title": ppc["title"],
            "document_type": ppc["document_type"],
            "document_date_or_version": ppc["document_date"],
            "source_path": ppc["local_path"],
            "source_sha256": ppc["sha256"],
            "applicability_2011": "comprovada",
            "supported_use": (
                "Implementation-curriculum context and statement that Fichas 1 were annexed; "
                "the preserved 32-page PDF does not contain those annexes."
            ),
            "justification": (
                "The repository-established 2010 PPC is the project for the curriculum implemented "
                "in 2011; its internal date is 2010-07-30."
            ),
            "version_relationship": (
                "Corroborating PPC; placeholder codes do not replace the final resolution."
            ),
        },
    ]
    for row in evidence:
        applicability.append(
            {
                "record_id": f"APP-{row['evidence_id']}",
                "target_scope": row["target_id"],
                "document_title": row["document_title"],
                "document_type": row["document_type"],
                "document_date_or_version": row["document_version"],
                "source_path": row["source_path"],
                "source_sha256": row["source_sha256"],
                "applicability_2011": row["applicability_2011"],
                "supported_use": (
                    "Presence and contents of the preserved 2025 CI241 Ficha only."
                    if row["evidence_id"].startswith("FICHA1-")
                    else "Current 96A portal record identity and displayed fields only."
                ),
                "justification": row["applicability_justification"],
                "version_relationship": (
                    "Later separate Ficha version; not merged with the 2010 act or portal page."
                    if row["evidence_id"].startswith("FICHA1-")
                    else "Current undated portal representation; not a proven historical 2011 version."
                ),
            }
        )
    return evidence, coverage, applicability


def serialize(rows: list[dict[str, str]], fields: list[str]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify committed outputs")
    args = parser.parse_args()
    evidence, coverage, applicability = build_rows()
    outputs = {
        OUTPUT_DIR / "evidencias.csv": serialize(evidence, EVIDENCE_FIELDS),
        OUTPUT_DIR / "cobertura.csv": serialize(coverage, COVERAGE_FIELDS),
        OUTPUT_DIR / "aplicabilidade.csv": serialize(applicability, APPLICABILITY_FIELDS),
    }
    errors = 0
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                print(f"ERROR: generated output differs: {path.relative_to(ROOT)}")
                errors += 1
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="")
    if args.check and not errors:
        print("W017 generated outputs match preserved sources")
    elif not args.check:
        print("W017 generated outputs written")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
