#!/usr/bin/env python3
"""Validate the bounded W018 D01 Ficha 1 extraction."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv"
W010 = ROOT / "curriculos/2023/inventario/ementas.csv"
MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-dinf.csv"

TARGETS = ("CI1001", "CI1002", "CI1003", "CI1055", "CI1215")
EXPECTED_SHA256 = {
    "CI1001": "de98f9b0340f8243d9f8f1f8eb9f0ef76a63ced54fd2088f915709281fa4dbb8",
    "CI1002": "166c5dcb4b46c9a999308d4907559c3bd4697f79315800de887b660abe80412a",
    "CI1003": "50a65e1bfe4986f1e5ba39d9a36e1bec0ce8caf6c860df37ff5cfa99e748e91d",
    "CI1055": "2b08392604d4cfb41fbebef1d32ceb41372a8b7491fded4e593356735fcb5cca",
    "CI1215": "1de3538f19829396f8c7a99cd8af298d33afbc0b7ce2148dfafda13298f91e93",
}
EXPECTED_TITLES = {
    "CI1001": "Programação 1",
    "CI1002": "Programação 2",
    "CI1003": "Introdução à Ciência da Computação",
    "CI1055": "Algoritmos e Estruturas de Dados 1",
    "CI1215": "Sistemas Operacionais",
}
EXPECTED_EMENTAS = {
    "CI1001": "Uso dirigido de ferramentas para programação. Estudo de estruturas de dados básicas. Práticas de programação.",
    "CI1002": "Uso de técnicas avançadas para desenvolvimento de software. Práticas de projetos de desenvolvimento de programas de média e alta complexidade.",
    "CI1003": "Introdução à Ciência da Computação; História da Computação; Impactos da Computação na Ciência, Tecnologia e Sociedade; Áreas da Ciência da Computação; O Curso de Ciência da Computação no DInf; Pensamento Computacional; Pensamento Sistêmico e Socialmente Consciente; Computação, Ética e Sociedade; Possibilidades e Demandas do Mercado de Trabalho; Características esperadas de um proﬁssional de Ciência da Computação. Ética na computação. Computação e a sociedade. Politicas nacionais de computação.",
    "CI1055": "Programação de computadores em linguagem de alto nível: do modelo Von Neumann à programação estruturada com estruturas de dados elementares. Tipos abstratos de dados simples. Noções básicas de custo e de teste de programas.",
    "CI1215": "Estrutura básica de um sistema operacional e sua interface com as aplicações e hardware. Mecanismos de comunicação e sincronização entre processos. Principais estruturas de dados e algoritmos de um sistema operacional para gerenciamento de processos, memória, sistemas de arquivos e entrada e saída.",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    rows = read_csv(OUTPUT)
    if len(rows) != 5:
        errors.append(f"D01 must contain exactly 5 data rows, found {len(rows)}")
    if tuple(row.get("code") for row in rows) != TARGETS:
        errors.append(f"D01 code order/scope must be {TARGETS}")
    if len({row.get("code") for row in rows}) != len(rows):
        errors.append("D01 codes must be unique")

    w010 = {(row["code"], row["document_path"]): row for row in read_csv(W010)}
    manifest = {}
    for row in read_csv(MANIFEST):
        if row.get("kind_in_index") == "ficha-1":
            manifest[(row["code"], row["local_path"])] = row

    required = {
        "document_id", "document_kind", "code", "source_title", "ementa",
        "source_total_hours", "unit_department", "document_date", "signature_date",
        "applicability_2023", "source_path", "source_sha256", "source_url",
        "title_locator", "ementa_locator", "total_hours_locator", "unit_locator",
        "date_locator", "normalization_notes",
    }
    if rows and set(rows[0]) != required:
        errors.append("D01 header does not match the required field set")

    for row in rows:
        code = row.get("code", "")
        path = row.get("source_path", "")
        pdf = ROOT / path
        if row.get("document_kind") != "Ficha 1":
            errors.append(f"{code}: document_kind is not Ficha 1")
        if row.get("source_title") != EXPECTED_TITLES.get(code):
            errors.append(f"{code}: source_title differs from checked PDF/inventory")
        if row.get("ementa") != EXPECTED_EMENTAS.get(code):
            errors.append(f"{code}: ementa differs from reused normalized transcription")
        if row.get("source_total_hours") != "60":
            errors.append(f"{code}: source_total_hours must be the source-stated 60")
        if row.get("applicability_2023") != "indeterminado":
            errors.append(f"{code}: applicability_2023 must remain indeterminado")
        for field in ("document_date", "signature_date"):
            if not row.get(field):
                errors.append(f"{code}: {field} must state a value or explicit absence")
        for field in ("title_locator", "ementa_locator", "total_hours_locator", "unit_locator", "date_locator"):
            if "PDF p. 1" not in row.get(field, ""):
                errors.append(f"{code}: {field} lacks exact PDF page locator")
        if not pdf.is_file():
            errors.append(f"{code}: source PDF missing: {path}")
            continue
        actual = sha256(pdf)
        if actual != row.get("source_sha256") or actual != EXPECTED_SHA256.get(code):
            errors.append(f"{code}: stored PDF hash differs from D01/expected hash")
        w010_row = w010.get((code, path))
        if not w010_row:
            errors.append(f"{code}: missing corresponding W010 Ficha 1 record")
        else:
            for field in ("sha256", "applicability_2023"):
                if row.get("source_sha256" if field == "sha256" else field) != w010_row[field]:
                    errors.append(f"{code}: {field} differs from W010 inventory")
        manifest_row = manifest.get((code, path))
        if not manifest_row:
            errors.append(f"{code}: missing corresponding DInf manifest record")
        else:
            if row.get("source_sha256") != manifest_row["sha256"]:
                errors.append(f"{code}: hash differs from DInf manifest")
            if row.get("source_url") != manifest_row["source_url"]:
                errors.append(f"{code}: source URL differs from DInf manifest")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("W018 D01 validation passed: 5 unique Ficha 1 rows, source values/locators, manifest hashes, and W010 cross-checks verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
