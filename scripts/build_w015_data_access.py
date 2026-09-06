#!/usr/bin/env python3
"""Build the W015 local data-access package from the recorded repository snapshot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "acesso"
DATASET_OUT = OUT / "datasets.csv"
SOURCE_OUT = OUT / "source-records.csv"
GAP_OUT = OUT / "gaps.csv"

MANIFESTS = [
    Path("fontes/catalogo.csv"),
    Path("curriculos/2011/fontes/manifesto.csv"),
    Path("curriculos/2011/fichas/manifesto.csv"),
    Path("curriculos/2023/fontes/manifesto.csv"),
    Path("curriculos/2023/fichas/manifesto-dinf.csv"),
    Path("curriculos/2023/fichas/manifesto-outros-departamentos.csv"),
    Path("administracao/dados/fontes.csv"),
    Path("administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv"),
    Path("administracao/historico/fontes/manifesto.csv"),
    Path("administracao/historico/atos-originais/manifesto.csv"),
    Path("administracao/mec/2026/fontes/manifesto.csv"),
]

NEGATIVE_SEARCHES = [
    Path("curriculos/2011/inventario/buscas-negativas.csv"),
    Path("curriculos/2023/inventario/buscas-negativas.csv"),
    Path("administracao/historico/buscas-negativas.csv"),
    Path("administracao/historico/atos-originais/buscas.csv"),
]

HUMAN_REVIEWS = [
    Path("governance/human-reviews/W009-p1-curriculum-2011.md"),
    Path("governance/human-reviews/W010-p1-curriculum-2023.md"),
    Path("governance/human-reviews/W011-p1-admin-procedure.md"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fieldnames} for row in rows)


def csv_inputs() -> list[Path]:
    paths = sorted(
        path.relative_to(ROOT)
        for base in (ROOT / "curriculos", ROOT / "administracao")
        for path in base.rglob("*.csv")
        if path.is_file() and OUT not in path.parents
    )
    catalog = Path("fontes/catalogo.csv")
    if (ROOT / catalog).is_file():
        paths.insert(0, catalog)
    return list(dict.fromkeys(paths))


def build_datasets() -> list[dict[str, str]]:
    rows = []
    for rel in csv_inputs():
        path = ROOT / rel
        records = read_csv(path)
        with path.open(encoding="utf-8-sig") as handle:
            header = next(csv.reader(handle), [])
        rows.append(
            {
                "path": rel.as_posix(),
                "header": "|".join(header),
                "row_count": str(len(records)),
                "sha256": sha256(path),
                "scope": dataset_scope(rel),
            }
        )
    return rows


def dataset_scope(path: Path) -> str:
    text = path.as_posix()
    if "/inventario/" in text or "/grade-" in text:
        return "curriculum inventory or formal structure"
    if "/dados/" in text or "/historico/" in text:
        return "administrative data or historical series"
    if text == "fontes/catalogo.csv":
        return "curated global source catalog"
    return "repository dataset"


def source_value(row: dict[str, str], *names: str) -> str:
    for name in names:
        if row.get(name, ""):
            return row[name]
    return ""


def build_sources() -> list[dict[str, str]]:
    raw = []
    for manifest in MANIFESTS:
        path = ROOT / manifest
        if not path.is_file():
            continue
        for row_number, row in enumerate(read_csv(path), start=2):
            raw.append(
                {
                    "origin_manifest": manifest.as_posix(),
                    "origin_row": str(row_number),
                    "record_id": source_value(row, "id", "record_id", "code", "arquivo"),
                    "title": source_value(row, "title", "index_label"),
                    "institution": source_value(row, "institution", "instituicao"),
                    "source_url": source_value(row, "source_url", "url_oficial"),
                    "accessed_at": source_value(row, "accessed_at", "data_consulta"),
                    "document_date": source_value(row, "document_date"),
                    "document_type": source_value(row, "document_type", "tipo", "kind", "kind_in_index"),
                    "local_path": source_value(row, "local_path", "caminho_local", "path", "arquivo"),
                    "sha256": source_value(row, "sha256"),
                    "version_or_validity": source_value(row, "version_or_validity", "version_or_term", "applicability", "version_or_date"),
                    "purpose": source_value(row, "purpose"),
                    "status": source_value(row, "status"),
                    "notes": source_value(row, "notes"),
                    "original_metadata_json": json.dumps(row, ensure_ascii=False, sort_keys=True),
                }
            )

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in raw:
        identity = row["local_path"] or f"{row['origin_manifest']}:{row['origin_row']}"
        groups[identity].append(row)
    output = []
    for row in raw:
        identity = row["local_path"] or f"{row['origin_manifest']}:{row['origin_row']}"
        peers = groups[identity]
        differing = sorted(
            field
            for field in ("title", "source_url", "local_path", "sha256", "version_or_validity", "status")
            if len({peer[field] for peer in peers}) > 1
        )
        row["identity_key"] = identity
        row["conflict_group"] = identity if len(peers) > 1 else ""
        row["conflict_fields"] = "|".join(differing)
        row["conflict_status"] = "metadata-differences-not-adjudicated" if differing else ("duplicate-origin" if len(peers) > 1 else "single-origin")
        output.append(row)
    return output


def markdown_field(text: str, label: str) -> str:
    match = re.search(rf"^[-*] \*\*{re.escape(label)}:\*\* (.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def build_gaps() -> list[dict[str, str]]:
    rows = []
    for path in HUMAN_REVIEWS:
        text = (ROOT / path).read_text(encoding="utf-8")
        blocks = re.split(r"(?=^## HR-[^\n]+$)", text, flags=re.MULTILINE)
        for block in blocks:
            heading = re.search(r"^## (HR-[^\n]+)$", block, re.MULTILINE)
            if not heading:
                continue
            gap_id = heading.group(1).split(" — ", 1)[0].strip()
            rows.append(
                {
                    "gap_id": gap_id,
                    "gap_type": "institutional_access",
                    "origin_path": path.as_posix(),
                    "origin_id": gap_id,
                    "target": markdown_field(block, "Related gap"),
                    "status": markdown_field(block, "Status"),
                    "recorded_result": markdown_field(block, "Related gap"),
                    "gate_consequence": markdown_field(block, "Gate consequence"),
                    "accessed_at": "",
                    "domains_or_custodian": "",
                    "original_record": block.strip(),
                }
            )
    for path in NEGATIVE_SEARCHES:
        if not (ROOT / path).is_file():
            continue
        for row_number, row in enumerate(read_csv(ROOT / path), start=2):
            identifier = source_value(row, "search_id", "id") or f"row-{row_number}"
            rows.append(
                {
                    "gap_id": f"{path.as_posix()}:{identifier}",
                    "gap_type": "public_documentary",
                    "origin_path": path.as_posix(),
                    "origin_id": identifier,
                    "target": source_value(row, "targets", "affected_targets", "target", "target_id"),
                    "status": "recorded search; see original result and limits",
                    "recorded_result": source_value(row, "result"),
                    "gate_consequence": "",
                    "accessed_at": source_value(row, "accessed_at", "access_date"),
                    "domains_or_custodian": source_value(row, "domains", "official_domains", "official_domains_and_systems"),
                    "original_record": json.dumps(row, ensure_ascii=False, sort_keys=True),
                }
            )
    return rows


def build_all(parts: set[str]) -> None:
    if "datasets" in parts:
        write_csv(DATASET_OUT, ["path", "header", "row_count", "sha256", "scope"], build_datasets())
    if "sources" in parts:
        write_csv(SOURCE_OUT, [
            "origin_manifest", "origin_row", "record_id", "identity_key", "title", "institution",
            "source_url", "accessed_at", "document_date", "document_type", "local_path", "sha256",
            "version_or_validity", "purpose", "status", "notes", "conflict_group", "conflict_fields",
            "conflict_status", "original_metadata_json",
        ], build_sources())
    if "gaps" in parts:
        write_csv(GAP_OUT, [
            "gap_id", "gap_type", "origin_path", "origin_id", "target", "status", "recorded_result",
            "gate_consequence", "accessed_at", "domains_or_custodian", "original_record",
        ], build_gaps())


def check() -> list[str]:
    errors = []
    expected = {DATASET_OUT, SOURCE_OUT, GAP_OUT}
    for path in expected:
        if not path.is_file():
            errors.append(f"missing output: {path.relative_to(ROOT)}")
    if errors:
        return errors
    for path, builder in ((DATASET_OUT, build_datasets), (SOURCE_OUT, build_sources), (GAP_OUT, build_gaps)):
        if read_csv(path) != builder():
            errors.append(f"output differs from current recorded inputs: {path.relative_to(ROOT)}")
    datasets = read_csv(DATASET_OUT)
    for row in datasets:
        path = ROOT / row["path"]
        if not path.is_file():
            errors.append(f"dataset path missing: {row['path']}")
        elif sha256(path) != row["sha256"]:
            errors.append(f"dataset hash mismatch: {row['path']}")
        elif len(read_csv(path)) != int(row["row_count"]):
            errors.append(f"dataset count mismatch: {row['path']}")
    source_rows = read_csv(SOURCE_OUT)
    for row in source_rows:
        if row["origin_manifest"] not in {p.as_posix() for p in MANIFESTS}:
            errors.append(f"unknown source origin: {row['origin_manifest']}")
        local = row["local_path"]
        if local and not (ROOT / local).is_file() and row["status"].lower() not in {"not located", "not_localized"}:
            errors.append(f"source path missing: {local} (origin {row['origin_manifest']}:{row['origin_row']})")
        if local and (ROOT / local).is_file() and row['sha256'] and sha256(ROOT / local) != row['sha256']:
            errors.append(f"source hash mismatch: {local}")
    if not read_csv(GAP_OUT):
        errors.append("gap queue is empty")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["datasets", "sources", "gaps", "all"], default="all")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = check()
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("W015 access package check: OK")
        return 0
    build_all({"datasets", "sources", "gaps"} if args.only == "all" else {args.only})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
