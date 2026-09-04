#!/usr/bin/env python3
"""Validate preserved INEP packages and the exact extracted XLSX members."""

from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INEP_SOURCES = ROOT / "administracao/dados/inep/fontes"
PACKAGE_DIR = INEP_SOURCES / "pacotes"
SPREADSHEET_DIR = INEP_SOURCES / "planilhas"
MD5_DIR = INEP_SOURCES / "md5"
MD5_ENTRY = re.compile(r"([0-9a-fA-F]{32}) \*([^\r\n]+\.xlsx)")


def digest(path: Path, algorithm: str) -> str:
    checksum = hashlib.new(algorithm)
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def main() -> int:
    errors: list[str] = []
    packages = sorted(PACKAGE_DIR.glob("*.zip"))
    spreadsheets = sorted(SPREADSHEET_DIR.glob("*.xlsx"))
    official_md5: dict[str, str] = {}

    for manifest in sorted(MD5_DIR.glob("*.txt")):
        match = MD5_ENTRY.search(manifest.read_text(encoding="utf-8-sig"))
        if not match:
            errors.append(f"XLSX MD5 entry not found: {manifest.relative_to(ROOT)}")
            continue
        official_md5[match.group(2)] = match.group(1).lower()

    if len(packages) != 11:
        errors.append(f"expected 11 ZIP packages; found {len(packages)}")
    if len(spreadsheets) != 11:
        errors.append(f"expected 11 XLSX spreadsheets; found {len(spreadsheets)}")
    if len(official_md5) != 11:
        errors.append(f"expected 11 official XLSX MD5 entries; found {len(official_md5)}")

    archived_names: set[str] = set()
    for package in packages:
        with zipfile.ZipFile(package) as archive:
            damaged = archive.testzip()
            if damaged:
                errors.append(f"damaged ZIP member in {package.name}: {damaged}")
            xlsx_members = [name for name in archive.namelist() if name.lower().endswith(".xlsx")]
            if len(xlsx_members) != 1:
                errors.append(f"expected one XLSX member in {package.name}; found {len(xlsx_members)}")
                continue
            member = xlsx_members[0]
            name = Path(member).name
            archived_names.add(name)
            extracted = SPREADSHEET_DIR / name
            if not extracted.is_file():
                errors.append(f"missing extracted XLSX member: {name}")
                continue
            archived_md5 = hashlib.md5(archive.read(member)).hexdigest()
            extracted_md5 = digest(extracted, "md5")
            expected_md5 = official_md5.get(name)
            if archived_md5 != extracted_md5:
                errors.append(f"ZIP member differs from extracted XLSX: {name}")
            if expected_md5 is None:
                errors.append(f"official MD5 not found for: {name}")
            elif extracted_md5 != expected_md5:
                errors.append(
                    f"official MD5 mismatch: {name} expected={expected_md5} actual={extracted_md5}"
                )

    unpaired = {path.name for path in spreadsheets} - archived_names
    if unpaired:
        errors.append(f"XLSX files without a matching ZIP member: {sorted(unpaired)}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"Checked {len(packages)} INEP packages, {len(spreadsheets)} extracted spreadsheets, "
        f"and {len(official_md5)} official MD5 entries; errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
