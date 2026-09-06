#!/usr/bin/env python3
"""Validate the bounded W019 D01 batch 2 Ficha 1 extraction."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv"
W010 = ROOT / "curriculos/2023/inventario/ementas.csv"
MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-dinf.csv"

TARGETS = ("CI1005", "CI1007", "CI1056", "CI1057", "CI1062")
EXPECTED_SHA256 = {
    "CI1005": "935422a55c7fe7098ea65530797d554f49b2ebe7fff09518da78fe8858a55aae",
    "CI1007": "8aa057ad98da9cee72cd52308cf00b2dabc2e05c2c2657a255c3e174e105c4c3",
    "CI1056": "20bc2234d68d3c913eb61f9a3bb09d4f90ee22beae707b94ff04d9c20f943899",
    "CI1057": "c320e876f8476b9e3886e333b0504fdfea46f2bff3c5c00044d7232a75736dd5",
    "CI1062": "b2cd36af20053f8350e540438b4c4b2a3858a0aa3d0433b12fe0743a463201da",
}
EXPECTED_TITLES = {
    "CI1005": "Qualidade de Software",
    "CI1007": "Segurança Computacional",
    "CI1056": "Algoritmos e Estrutura de Dados 2",
    "CI1057": "Algoritmos e Estruturas de Dados 3",
    "CI1062": "Paradigmas de Programação",
}
EXPECTED_EMENTAS = {
    "CI1005": "Qualidade de software. Métricas de qualidade. Gerenciamento de Conﬁguração. Veriﬁcação e Validação. Teste de software. Qualidade de processo. Ética na computação. Computação e a sociedade.",
    "CI1007": "Conceitos básicos. Introdução à criptograﬁa. Autenticação e controle de acesso. Segurança de sistemas e aplicações. Segurança em redes e na Internet. Auditoria. Gestão da segurança. Ética na computação. Computação e a sociedade. Politicas nacionais de segurança da informação.",
    "CI1056": "Recursão, Busca, Ordenação, Heaps, Contagem de recursos computacionais.",
    "CI1057": "Acesso seqüêncial, indexado. Tipo abstrato de dados dicionário. Ordenação externa. Algoritmos gulosos.",
    "CI1062": "Aprender diferentes paradigmas de programação estruturados e não estruturados.",
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
        errors.append(f"D01 batch 2 must contain exactly 5 data rows, found {len(rows)}")
    if tuple(row.get("code") for row in rows) != TARGETS:
        errors.append(f"D01 batch 2 code order/scope must be {TARGETS}")
    if len({row.get("code") for row in rows}) != len(rows):
        errors.append("D01 batch 2 codes must be unique")

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
        errors.append("D01 batch 2 header does not match the W018 field set")

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
            errors.append(f"{code}: stored PDF hash differs from CSV/expected hash")
        w010_row = w010.get((code, path))
        if not w010_row:
            errors.append(f"{code}: missing corresponding W010 Ficha 1 record")
        else:
            if row.get("source_sha256") != w010_row["sha256"]:
                errors.append(f"{code}: hash differs from W010 inventory")
            if row.get("applicability_2023") != w010_row["applicability_2023"]:
                errors.append(f"{code}: applicability differs from W010 inventory")
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
    print("W019 D01 batch 2 validation passed: 5 unique Ficha 1 rows, source values/locators, manifest hashes, and W010 cross-checks verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
