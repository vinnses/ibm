#!/usr/bin/env python3
"""Validate all 23 preserved Ficha 1 records across W018-W020."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
W018 = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv"
W019 = ROOT / "dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv"
W020 = ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv"
DINF_MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-dinf.csv"
EXTERNAL_MANIFEST = ROOT / "curriculos/2023/fichas/manifesto-outros-departamentos.csv"

ALL_CODES = (
    "CI1001", "CI1002", "CI1003", "CI1055", "CI1215", "CI1005", "CI1007",
    "CI1056", "CI1057", "CI1062", "CI1068", "CI1162", "CI1163", "CI1171",
    "CI1209", "CI1212", "CI1218", "CI1221", "CI1316", "CI1350", "BF114",
    "BQ083", "MN162",
)
W020_CODES = (
    "CI1068", "CI1162", "CI1163", "CI1171", "CI1209", "CI1212", "CI1218",
    "CI1221", "CI1316", "CI1350", "BF114", "BQ083", "MN162",
)
REQUIRED_FIELDS = {
    "document_id", "document_kind", "code", "source_title", "ementa",
    "source_total_hours", "unit_department", "document_date", "signature_date",
    "applicability_2023", "source_path", "source_sha256", "source_url",
    "title_locator", "ementa_locator", "total_hours_locator", "unit_locator",
    "date_locator", "normalization_notes",
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
    datasets = (("W018", W018), ("W019", W019), ("W020", W020))
    all_rows: list[tuple[str, dict[str, str]]] = []
    for label, path in datasets:
        if not path.is_file():
            errors.append(f"{label}: missing dataset {path}")
            continue
        rows = read_csv(path)
        expected_count = 5 if label != "W020" else 13
        if len(rows) != expected_count:
            errors.append(f"{label}: expected {expected_count} rows, found {len(rows)}")
        for row in rows:
            if set(row) != REQUIRED_FIELDS:
                errors.append(f"{label}/{row.get('code', '')}: schema differs from W018/W019 fields")
            all_rows.append((label, row))

    if len(all_rows) != 23:
        errors.append(f"combined W018/W019/W020 rows must equal 23, found {len(all_rows)}")
    codes = [row.get("code", "") for _, row in all_rows]
    if tuple(codes) != ALL_CODES:
        errors.append(f"combined code order/scope must be {ALL_CODES}")
    if len(set(codes)) != len(codes):
        errors.append("combined Ficha 1 codes must be unique")
    w020_codes = [row.get("code", "") for label, row in all_rows if label == "W020"]
    if tuple(w020_codes) != W020_CODES:
        errors.append(f"W020 code order/scope must be {W020_CODES}")

    manifest: dict[tuple[str, str], dict[str, str]] = {}
    for row in read_csv(DINF_MANIFEST):
        if row.get("kind_in_index") == "ficha-1":
            manifest[(row["code"], row["local_path"])] = {
                "sha256": row["sha256"], "source_url": row["source_url"]
            }
    for row in read_csv(EXTERNAL_MANIFEST):
        if row.get("kind") == "ficha-1":
            manifest[(row["code"], row["local_path"])] = {
                "sha256": row["sha256"], "source_url": row["source_url"]
            }

    paths: set[str] = set()
    urls: set[str] = set()
    identities: set[tuple[str, str]] = set()
    for label, row in all_rows:
        code = row.get("code", "")
        path = row.get("source_path", "")
        url = row.get("source_url", "")
        identity = (code, path)
        if identity in identities:
            errors.append(f"duplicate Ficha 1 identity: {identity}")
        identities.add(identity)
        if path in paths:
            errors.append(f"duplicate Ficha 1 source path: {path}")
        paths.add(path)
        if url in urls:
            errors.append(f"duplicate Ficha 1 source URL: {url}")
        urls.add(url)
        if row.get("document_kind") != "Ficha 1":
            errors.append(f"{label}/{code}: document_kind is not Ficha 1")
        if row.get("applicability_2023") != "indeterminado":
            errors.append(f"{label}/{code}: applicability_2023 must remain indeterminado")
        for field in ("document_date", "signature_date", "normalization_notes"):
            if not row.get(field):
                errors.append(f"{label}/{code}: {field} must be explicit and non-empty")
        for field in ("title_locator", "ementa_locator", "total_hours_locator", "unit_locator", "date_locator"):
            if "PDF p. " not in row.get(field, ""):
                errors.append(f"{label}/{code}: {field} lacks a PDF page locator")
        pdf = ROOT / path
        if not pdf.is_file():
            errors.append(f"{label}/{code}: stored PDF missing: {path}")
            continue
        actual = sha256(pdf)
        if actual != row.get("source_sha256"):
            errors.append(f"{label}/{code}: CSV hash differs from stored PDF bytes")
        manifest_row = manifest.get(identity)
        if not manifest_row:
            errors.append(f"{label}/{code}: no matching Ficha 1 manifest record")
        else:
            if row.get("source_sha256") != manifest_row["sha256"]:
                errors.append(f"{label}/{code}: CSV hash differs from manifest")
            if url != manifest_row["source_url"]:
                errors.append(f"{label}/{code}: CSV URL differs from manifest")

    if len(paths) != 23 or len(urls) != 23 or len(identities) != 23:
        errors.append(f"combined identity/path/URL uniqueness counts must all equal 23: identities={len(identities)}, paths={len(paths)}, urls={len(urls)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("W020 validation passed: 23 unique preserved Ficha 1 records across W018/W019/W020, manifest URLs/hashes, paths, and stored bytes verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
