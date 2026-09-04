#!/usr/bin/env python3
"""Validate W010 2023 curriculum-inventory invariants and local manifests."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculos/2023"
INVENTORY = BASE / "inventario"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path, errors: list[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        raw_rows = list(csv.reader(stream))
    if not raw_rows or len({len(row) for row in raw_rows}) != 1:
        errors.append(f"invalid CSV width: {path.relative_to(ROOT)}")
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def check_hash_records(
    rows: list[dict[str, str]], path_field: str, hash_field: str, status_field: str,
    accepted: set[str], errors: list[str], label: str,
) -> int:
    checked = 0
    for row in rows:
        if row[status_field] not in accepted:
            continue
        path = ROOT / row[path_field]
        expected = row[hash_field].lower()
        if not path.is_file():
            errors.append(f"{label}: missing {row[path_field]}")
        elif len(expected) != 64 or sha256(path) != expected:
            errors.append(f"{label}: hash mismatch {row[path_field]}")
        else:
            checked += 1
    return checked


def main() -> int:
    errors: list[str] = []
    components = read_csv(INVENTORY / "componentes.csv", errors)
    ementas = read_csv(INVENTORY / "ementas.csv", errors)
    dependencies = read_csv(INVENTORY / "dependencias.csv", errors)
    regulations = read_csv(INVENTORY / "regulamentos.csv", errors)
    searches = read_csv(INVENTORY / "buscas-negativas.csv", errors)
    sources = read_csv(BASE / "fontes/manifesto.csv", errors)
    dinf = read_csv(BASE / "fichas/manifesto-dinf.csv", errors)
    external = read_csv(BASE / "fichas/manifesto-outros-departamentos.csv", errors)

    codes = {row["code"] for row in components}
    if len(components) != 43 or len(codes) != 43:
        errors.append("components must contain exactly 43 unique targets")
    if sum(row["nature"] == "TCC alternativa" for row in components) != 4:
        errors.append("components must contain exactly four TCC alternatives")
    if sum(row["nature"] != "TCC alternativa" for row in components) != 39:
        errors.append("components must contain exactly 39 non-TCC targets")
    for row in components:
        if not row["evidence_status"] or not row["applicability_2023"]:
            errors.append(f"component lacks status/applicability: {row['code']}")

    ci1055 = next((row for row in components if row["code"] == "CI1055"), None)
    if not ci1055 or ci1055["title"] != "Algoritmos e Estruturas de Dados 1":
        errors.append("CI1055 title does not match the preserved Ficha 1 transcription")
    bq083 = next((row for row in components if row["code"] == "BQ083"), None)
    if not bq083 or bq083["applicability_2023"] != "indeterminado":
        errors.append("BQ083 applicability must remain indeterminate without an applicability act")
    bq083_ficha = next((row for row in ementas if row["code"] == "BQ083" and row["document_kind"] == "Ficha 1"), None)
    if not bq083_ficha or "2022" not in bq083_ficha["document_version_or_term"] or bq083_ficha["applicability_2023"] != "indeterminado":
        errors.append("BQ083 Ficha 1 date/applicability is not source-supported")
    for row in ementas:
        if not row["applicability_2023"]:
            errors.append(f"Ficha record lacks applicability: {row['code']} {row['document_kind']}")

    graph: dict[str, set[str]] = {code: set() for code in codes}
    for row in dependencies:
        if row["dependent_code"] not in codes or row["prerequisite_code"] not in codes:
            errors.append(f"dependency endpoint absent from inventory: {row}")
        else:
            graph[row["dependent_code"]].add(row["prerequisite_code"])
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"dependency cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for next_node in graph[node]:
            visit(next_node)
        visiting.remove(node)
        visited.add(node)
    for code in graph:
        visit(code)

    required_regulations = {"Atividades Formativas", "Estágio obrigatório e não obrigatório", "Trabalho de Conclusão de Curso", "Atividades Curriculares de Extensão"}
    if not required_regulations <= {row["subject"] for row in regulations}:
        errors.append("required regulation coverage is incomplete")
    if not searches or any(not row["accessed_at"] or not row["official_domains"] or not row["limits"] for row in searches):
        errors.append("negative-search records lack required scope fields")

    source_count = check_hash_records(sources, "local_path", "sha256", "status", {"preservado"}, errors, "source manifest")
    ficha_count = check_hash_records(dinf, "local_path", "sha256", "status", {"downloaded"}, errors, "DInf Ficha manifest")
    ficha_count += check_hash_records(external, "local_path", "sha256", "status", {"downloaded"}, errors, "external Ficha manifest")
    portal = next((row for row in sources if row["id"] == "2023-EMENTARIO"), None)
    if not portal or portal["local_path"] != "curriculos/2023/fontes/pagina-ementario-curriculo-96a-2026-09-04.html":
        errors.append("Ementário manifest does not identify the preserved curriculum response")
    elif "3000" not in (ROOT / portal["local_path"]).read_text(encoding="utf-8"):
        errors.append("Ementário curriculum capture does not contain the recorded 3000-hour value")

    readme = (BASE / "fontes/README.md").read_text(encoding="utf-8")
    for row in sources:
        source_path = Path(row["local_path"])
        if source_path.parent != Path("curriculos/2023/fontes") or source_path.suffix.lower() != ".pdf":
            continue
        pattern = re.compile(
            rf"^\| `{re.escape(source_path.name)}` \|.*\| `([0-9a-f]{{64}})` \|$",
            re.MULTILINE,
        )
        match = pattern.search(readme)
        if not match:
            errors.append(f"source README lacks hash row for {source_path.name}")
        elif match.group(1) != row["sha256"]:
            errors.append(f"source README hash differs from manifest for {source_path.name}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked {len(components)} targets, {len(dependencies)} dependencies, {source_count} source hashes, {ficha_count} Ficha hashes, and {len(searches)} negative searches; errors={len(errors)}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
