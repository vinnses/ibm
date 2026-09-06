#!/usr/bin/env python3
"""Validate the complete preserved W018/W019/W020 Ficha 1 + Ficha 2 set."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W018 = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv"
W019 = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv"
W020_F1 = ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv"
W020_F2 = ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-2.csv"
DINF_MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-dinf.csv"
EXTERNAL_MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-outros-departamentos.csv"

ALL_F1_CODES = ("CI1001", "CI1002", "CI1003", "CI1055", "CI1215", "CI1005", "CI1007", "CI1056", "CI1057", "CI1062", "CI1068", "CI1162", "CI1163", "CI1171", "CI1209", "CI1212", "CI1218", "CI1221", "CI1316", "CI1350", "BF114", "BQ083", "MN162")
W020_F1_CODES = ("CI1068", "CI1162", "CI1163", "CI1171", "CI1209", "CI1212", "CI1218", "CI1221", "CI1316", "CI1350", "BF114", "BQ083", "MN162")
F2_CODES = ("CI1001", "CI1002", "CI1005", "CI1007", "CI1055", "CI1056", "CI1057", "CI1062", "CI1068", "CI1163", "CI1171", "CI1209", "CI1212", "CI1218", "CI1221", "CI1316", "MN129")
F1_FIELDS = {"document_id", "document_kind", "code", "source_title", "ementa", "source_total_hours", "unit_department", "document_date", "signature_date", "applicability_2023", "source_path", "source_sha256", "source_url", "title_locator", "ementa_locator", "total_hours_locator", "unit_locator", "date_locator", "normalization_notes"}
F2_FIELDS = {"document_id", "document_kind", "code", "source_title", "term_or_period", "class_identifier", "plan_version", "document_date", "applicability_2023", "unit_department", "permanent_fields", "ementa", "program", "objectives", "method", "evaluation", "bibliography", "teacher_fields", "source_path", "source_sha256", "source_url", "source_locators", "normalization_notes"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifests() -> dict[tuple[str, str, str], dict[str, str]]:
    result: dict[tuple[str, str, str], dict[str, str]] = {}
    for path, kind_field in ((DINF_MANIFEST, "kind_in_index"), (EXTERNAL_MANIFEST, "kind")):
        for row in read_csv(path):
            kind = row.get(kind_field, "")
            if kind in {"ficha-1", "ficha-2"}:
                result[(kind, row["code"], row["local_path"])] = {"sha256": row["sha256"], "source_url": row["source_url"]}
    return result


def main() -> int:
    errors: list[str] = []
    datasets = (("W018", W018, 5, F1_FIELDS), ("W019", W019, 5, F1_FIELDS), ("W020-F1", W020_F1, 13, F1_FIELDS), ("W020-F2", W020_F2, 17, F2_FIELDS))
    all_rows: list[tuple[str, dict[str, str]]] = []
    for label, path, expected, fields in datasets:
        if not path.is_file():
            errors.append(f"{label}: missing dataset {path}")
            continue
        rows = read_csv(path)
        if len(rows) != expected:
            errors.append(f"{label}: expected {expected} rows, found {len(rows)}")
        for row in rows:
            if set(row) != fields:
                errors.append(f"{label}/{row.get('code', '')}: schema differs from expected fields")
            all_rows.append((label, row))

    f1_rows = [(label, row) for label, row in all_rows if row.get("document_kind") == "Ficha 1"]
    f2_rows = [(label, row) for label, row in all_rows if row.get("document_kind") == "Ficha 2"]
    if len(f1_rows) != 23: errors.append(f"combined Ficha 1 rows must equal 23, found {len(f1_rows)}")
    if len(f2_rows) != 17: errors.append(f"combined Ficha 2 rows must equal 17, found {len(f2_rows)}")
    if len(all_rows) != 40: errors.append(f"combined W018/W019/W020 rows must equal 40, found {len(all_rows)}")
    if tuple(row.get("code", "") for _, row in f1_rows) != ALL_F1_CODES: errors.append(f"combined Ficha 1 code order/scope must be {ALL_F1_CODES}")
    if tuple(row.get("code", "") for _, row in f2_rows) != F2_CODES: errors.append(f"Ficha 2 code order/scope must be {F2_CODES}")
    if tuple(row.get("code", "") for label, row in f1_rows if label == "W020-F1") != W020_F1_CODES: errors.append(f"W020 Ficha 1 code order/scope must be {W020_F1_CODES}")
    if len({row.get("code", "") for _, row in f1_rows}) != 23: errors.append("combined Ficha 1 codes must be unique")
    if len({row.get("code", "") for _, row in f2_rows}) != 17: errors.append("Ficha 2 codes must be unique")

    manifest = manifests()
    expected_manifest_keys = set(manifest)
    if len(expected_manifest_keys) != 40: errors.append(f"manifest coverage must equal 40, found {len(expected_manifest_keys)}")
    paths: set[str] = set(); urls: set[str] = set(); identities: set[tuple[str, str, str]] = set()
    for label, row in all_rows:
        kind_label = row.get("document_kind", "")
        kind = "ficha-1" if kind_label == "Ficha 1" else "ficha-2"
        code, path, url = row.get("code", ""), row.get("source_path", ""), row.get("source_url", "")
        identity = (kind, code, path)
        if identity in identities: errors.append(f"duplicate preserved identity: {identity}")
        identities.add(identity)
        if path in paths: errors.append(f"duplicate preserved source path: {path}")
        paths.add(path)
        if url in urls: errors.append(f"duplicate preserved source URL: {url}")
        urls.add(url)
        if kind_label not in {"Ficha 1", "Ficha 2"}: errors.append(f"{label}/{code}: unsupported document_kind")
        if row.get("applicability_2023") != "indeterminado": errors.append(f"{label}/{code}: applicability_2023 must remain indeterminado")
        locator_fields = ("title_locator", "ementa_locator", "total_hours_locator", "unit_locator", "date_locator") if kind_label == "Ficha 1" else ("source_locators",)
        if kind_label == "Ficha 2":
            for field in ("term_or_period", "class_identifier", "plan_version", "document_date", "permanent_fields", "program", "objectives", "method", "evaluation", "bibliography", "teacher_fields", "normalization_notes"):
                if not row.get(field): errors.append(f"{label}/{code}: {field} must be explicit and non-empty")
        for field in locator_fields:
            locator = row.get(field, "")
            if "PDF p. " not in locator and "PDF pp. " not in locator: errors.append(f"{label}/{code}: {field} lacks a PDF page locator")
        pdf = ROOT / path
        if not pdf.is_file(): errors.append(f"{label}/{code}: stored PDF missing: {path}"); continue
        if sha256(pdf) != row.get("source_sha256"): errors.append(f"{label}/{code}: CSV hash differs from stored PDF bytes")
        manifest_row = manifest.get(identity)
        if not manifest_row: errors.append(f"{label}/{code}: no matching manifest record for {kind}")
        else:
            if row.get("source_sha256") != manifest_row["sha256"]: errors.append(f"{label}/{code}: CSV hash differs from manifest")
            if url != manifest_row["source_url"]: errors.append(f"{label}/{code}: CSV URL differs from manifest")
    if identities != expected_manifest_keys: errors.append(f"row/manifest identity coverage differs: missing={sorted(expected_manifest_keys - identities)}, extra={sorted(identities - expected_manifest_keys)}")
    if len(paths) != 40 or len(urls) != 40 or len(identities) != 40: errors.append(f"uniqueness counts must all equal 40: identities={len(identities)}, paths={len(paths)}, urls={len(urls)}")
    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print("W020 validation passed: 23 Ficha 1 + 17 Ficha 2 = 40 unique preserved PDFs; manifests, URLs, hashes, paths, and stored bytes verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
