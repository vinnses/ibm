#!/usr/bin/env python3
"""Build a reviewable Markdown inventory from collected UFPR Ficha PDFs."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import subprocess


def extract_text(pdf: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True
    )
    return result.stdout.decode("utf-8", errors="replace")


def normalized_ementa(text: str) -> str:
    match = re.search(
        r"\bEMENTA(?:\s*\([^)]*\))?\s*(.*?)(?=\n\s*(?:\*?OBS|Documento assinado|Art\.\s*9|Chefe de Departamento|BIBLIOGRAFIA)\b)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return "[Ementa não extraída automaticamente; requer leitura manual do PDF.]"
    value = match.group(1).replace("\f", " ")
    return re.sub(r"\s+", " ", value).strip()


def signature_date(text: str) -> str:
    dates = re.findall(r"\bem\s+(\d{2}/\d{2}/\d{4})", text)
    return dates[0] if dates else "não identificada automaticamente"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.manifest.open(encoding="utf-8")))
    rows = [row for row in rows if row["kind_in_index"] == "ficha-1" and row["status"] == "downloaded"]
    rows.sort(key=lambda row: row["code"])

    parts = [
        "# Ementas localizadas no índice do Departamento de Informática",
        "",
        "Extração automática para conferência humana. As ementas abaixo tiveram apenas espaços e quebras de linha normalizados. O texto original permanece nos PDFs referenciados e prevalece em caso de erro de extração.",
        "",
        "As Fichas foram publicadas no índice atual do Departamento de Informática, mas várias foram assinadas antes da reforma de 2023. Portanto, elas comprovam versões oficiais das ementas, mas sua vigência específica no currículo de 2023 ainda precisa ser confirmada individualmente.",
        "",
    ]
    for row in rows:
        pdf = Path(row["local_path"])
        text = extract_text(pdf)
        relative = pdf.relative_to(args.root).as_posix()
        parts.extend(
            [
                f"## {row['code']}",
                "",
                f"- Documento local: [`{relative}`]({relative})",
                f"- URL original: {row['source_url']}",
                f"- SHA-256: `{row['sha256']}`",
                f"- Primeira data de assinatura extraída: {signature_date(text)}",
                "- Estado de vigência: requer confirmação contra o currículo de 2023",
                "",
                "**Ementa — transcrição normalizada automaticamente:**",
                "",
                normalized_ementa(text),
                "",
            ]
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
