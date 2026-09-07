#!/usr/bin/env python3
"""Validate W030's deterministic CPA workbook extraction."""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REL = Path("administracao/historico/fontes/documentos/cpa-avaliacao-curso-informatica-biomedica-2022.xlsx")
SOURCE = ROOT / SOURCE_REL
OUT = ROOT / "administracao/dados/cpa"
SHA = "4c968ff6e4c32b9d023cfd4f783c0a38b3474bbcde231c383587a9198771cf40"
COURSE = "40001016064G0"
EXPECTED = [
    "workbook-inventory.json", "observed-cells.jsonl.gz", "provenance.json",
    "cpa_observations.csv", "cpa_response_frequencies.csv", "cpa_questions.csv",
    "cpa_response_criteria.csv", "cpa_course_response_counts.csv",
    "cpa_course_registry.csv", "README.md",
]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def report(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


def main() -> int:
    errors: list[str] = []
    if not SOURCE.is_file():
        errors.append("source missing")
    elif digest(SOURCE) != SHA:
        errors.append("source SHA mismatch")
    for name in EXPECTED:
        if not (OUT / name).is_file():
            errors.append(f"missing output: {name}")
    if errors:
        return report(errors)

    inventory = json.loads((OUT / "workbook-inventory.json").read_text(encoding="utf-8"))
    if inventory["source"]["path"] != SOURCE_REL.as_posix() or inventory["source"]["sha256"] != SHA:
        errors.append("inventory source provenance mismatch")
    expected_sheets = [
        'dados', 'HAB_LETRAS', 'Quantidade de respostas', 'Frequencia de respostas',
        'Questoes', 'criterio_analise', 'Setor', 'Cursos', 'Modelo', 'SEGURANÇA',
        'AMBIENTES', 'SERVIÇOS TERCEIRIZADOS', 'SALAS DE AULA', 'NTE',
        'LABORATÓRIOS', 'BIBLIOTECAS', 'SISTEMA DE REDES',
        'AVALIAÇÃO DE SERVIÇOS ', 'INST_PESQUISA '
    ]
    if inventory["worksheet_count"] != 19 or [sheet["worksheet"] for sheet in inventory["worksheets"]] != expected_sheets:
        errors.append("worksheet inventory mismatch")
    removed = inventory.get("dangling_relationships_removed_for_openpyxl", [])
    if len(removed) != 25 or any(not item["type"].endswith(("/drawing", "/vmlDrawing")) for item in removed):
        errors.append("unexpected sanitized relationship set")

    with gzip.open(OUT / "observed-cells.jsonl.gz", "rt", encoding="utf-8") as handle:
        cells = [json.loads(line) for line in handle if line.strip()]
    if len(cells) != inventory["populated_cell_count"]:
        errors.append("faithful cell count differs from inventory")
    keys = [(cell.get("worksheet"), cell.get("cell")) for cell in cells]
    if any(not all(key) for key in keys) or len(keys) != len(set(keys)):
        errors.append("cell provenance is missing or non-unique")
    formula_cells = [cell for cell in cells if cell.get("formula") is not None]
    if len(formula_cells) != inventory["formula_cell_count"] or not formula_cells:
        errors.append("formula count mismatch")
    if any(cell.get("formula_cache_status") not in {"stored", "missing"} for cell in formula_cells):
        errors.append("formula cache status missing")
    cache_counts = Counter(cell["formula_cache_status"] for cell in formula_cells)
    if inventory.get("formula_cached_value_count") != cache_counts["stored"] or inventory.get("formula_missing_cache_count") != cache_counts["missing"]:
        errors.append("formula cache summary mismatch")
    if not inventory.get("openpyxl_direct_load_error", "").startswith("KeyError:"):
        errors.append("direct-load structural defect not recorded")
    cell_map = {(cell["worksheet"], cell["cell"]): cell for cell in cells}

    observations = rows(OUT / "cpa_observations.csv")
    if len(observations) != 132 or len({row["source_row"] for row in observations}) != 132:
        errors.append("expected 132 unique literal observations")
    id_counts = sorted(Counter(row["id_pesquisa"] for row in observations).values())
    if id_counts != [44, 44, 44]:
        errors.append("source ID_PESQUISA rows are not three groups of 44")
    question_counts = Counter(row["question_id"] for row in observations)
    if len(question_counts) != 44 or set(question_counts.values()) != {3}:
        errors.append("expected 44 questions with three response rows each")
    for row in observations:
        if row["source_workbook"] != SOURCE_REL.as_posix() or row["workbook_sha256"] != SHA:
            errors.append("observation workbook provenance mismatch")
            break
        source_row = row["source_row"]
        expected_values = {
            "value": ("dados", f"F{source_row}"), "course_literal": ("dados", f"G{source_row}"),
            "course_code": ("dados", f"H{source_row}"), "question": ("dados", f"E{source_row}"),
            "question_id": ("dados", f"D{source_row}"),
        }
        for field, key in expected_values.items():
            if key not in cell_map or str(cell_map[key]["value"]) != row[field]:
                errors.append(f"observation field lacks matching source cell: row {source_row} {field}")
        if row["course_code"] != COURSE or row["course_literal"] != "INFORMÁTICA BIOMÉDICA":
            errors.append(f"non-target course observation: row {source_row}")
        if not row["value"] or row["denominator"] != "3":
            errors.append(f"blank value or unsupported denominator: row {source_row}")

    frequencies = rows(OUT / "cpa_response_frequencies.csv")
    frequency_keys = [(row["questionnaire_id"], row["question_id"], row["category"]) for row in frequencies]
    if len(frequency_keys) != len(set(frequency_keys)):
        errors.append("frequency keys are not unique")
    sums: dict[tuple[str, str], list[float]] = defaultdict(lambda: [0, 0.0])
    observation_by_cell = {f"F{row['source_row']}": row for row in observations}
    for row in frequencies:
        try:
            value, denominator, percentage = int(row["value"]), int(row["denominator"]), float(row["percentage"])
        except ValueError:
            errors.append("frequency numeric type failure")
            continue
        if denominator != 3 or not 0 <= percentage <= 1 or abs(percentage - value / denominator) > 1e-12:
            errors.append(f"frequency denominator/percentage mismatch: {row['question_id']} {row['category']}")
        cited = row["source_cells"].split(";")
        if len(cited) != value or any(cell not in observation_by_cell for cell in cited):
            errors.append(f"frequency source-cell count mismatch: {row['question_id']} {row['category']}")
        elif any(observation_by_cell[cell]["value"] != row["category"] or observation_by_cell[cell]["question_id"] != row["question_id"] for cell in cited):
            errors.append(f"frequency category invented or mismatched: {row['question_id']} {row['category']}")
        aggregate = sums[(row["questionnaire_id"], row["question_id"])]
        aggregate[0] += value
        aggregate[1] += percentage
    if any(count != 3 or abs(percent - 1.0) > 1e-12 for count, percent in sums.values()) or len(sums) != 44:
        errors.append("question frequency totals do not reconcile to three source rows")

    questions = rows(OUT / "cpa_questions.csv")
    criteria = rows(OUT / "cpa_response_criteria.csv")
    counts = rows(OUT / "cpa_course_response_counts.csv")
    registry = rows(OUT / "cpa_course_registry.csv")
    if len(questions) != 47 or any(not row["source_cell"] for row in questions):
        errors.append("question registry count/provenance mismatch")
    if len(criteria) != 5 or {row["tipo_quest"] for row in criteria} != {"A", "B", "C", "D", "E"}:
        errors.append("response criteria were not preserved literally")
    if len(counts) != 3 or any(row["COD_CURSO"] != COURSE or row["CURSO"] != "INFORMÁTICA BIOMÉDICA" or row["QTD_RESPONDENTES_CURSO"] != "3" or row["QTD_RESPOSTAS_CURSO"] != "132" for row in counts):
        errors.append("course quantity rows do not reconcile")
    if len(registry) != 1 or registry[0].get("COD_CURSO") != COURSE or registry[0].get("CURSO") != "INFORMÁTICA BIOMÉDICA":
        errors.append("course registry does not prove literal code/name mapping")
    for dataset in (questions, criteria, counts, registry):
        if any(row.get("source_workbook") != SOURCE_REL.as_posix() or row.get("workbook_sha256") != SHA for row in dataset):
            errors.append("normalized dataset row lacks workbook provenance")

    with tempfile.TemporaryDirectory() as directory:
        process = subprocess.run(
            [sys.executable, str(ROOT / "scripts/extract_cpa_workbook.py"), "--output", directory],
            cwd=ROOT, capture_output=True, text=True,
        )
        if process.returncode:
            errors.append("regeneration failed: " + process.stderr + process.stdout)
        else:
            for name in EXPECTED:
                if (OUT / name).read_bytes() != (Path(directory) / name).read_bytes():
                    errors.append(f"non-deterministic output: {name}")

    if not errors:
        print(
            "CPA validation: PASS; "
            f"worksheets=19 populated_cells={len(cells)} formulas={len(formula_cells)} "
            f"observations={len(observations)} questions=44 frequency_rows={len(frequencies)} "
            f"respondents=3 source_sha={SHA}"
        )
    return report(errors)


if __name__ == "__main__":
    raise SystemExit(main())
