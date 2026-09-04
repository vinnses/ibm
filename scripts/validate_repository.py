#!/usr/bin/env python3
"""Validate repository CSV structure, manifested hashes, and local Markdown links."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass(frozen=True)
class ManifestSpec:
    path: str
    local_path_column: str
    hash_column: str
    status_column: str
    preserved_statuses: frozenset[str]


MANIFESTS = (
    ManifestSpec(
        "fontes/catalogo.csv",
        "path",
        "sha256",
        "status",
        frozenset({"preserved"}),
    ),
    ManifestSpec(
        "administracao/dados/fontes.csv",
        "caminho_local",
        "sha256",
        "status",
        frozenset({"versionado", "versionado_lfs", "versionado_origem_fornecida"}),
    ),
    ManifestSpec(
        "administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv",
        "local_path",
        "sha256",
        "status",
        frozenset({"preserved_lfs"}),
    ),
    ManifestSpec(
        "curriculos/2023/fichas/manifesto-dinf.csv",
        "local_path",
        "sha256",
        "status",
        frozenset({"downloaded"}),
    ),
    ManifestSpec(
        "curriculos/2023/fichas/manifesto-outros-departamentos.csv",
        "local_path",
        "sha256",
        "status",
        frozenset({"downloaded"}),
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_csv_widths(errors: list[str]) -> int:
    checked = 0
    for path in ROOT.rglob("*.csv"):
        with path.open(encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.reader(stream))
        checked += 1
        if not rows:
            errors.append(f"empty CSV: {path.relative_to(ROOT)}")
            continue
        widths = {len(row) for row in rows}
        if len(widths) != 1:
            errors.append(
                f"inconsistent CSV width {sorted(widths)}: {path.relative_to(ROOT)}"
            )
    return checked


def validate_manifests(errors: list[str], warnings: list[str]) -> int:
    checked = 0
    for spec in MANIFESTS:
        manifest = ROOT / spec.path
        with manifest.open(encoding="utf-8-sig", newline="") as stream:
            for line_number, row in enumerate(csv.DictReader(stream), start=2):
                status = row[spec.status_column].strip()
                if status not in spec.preserved_statuses:
                    warnings.append(
                        f"unpreserved manifest record: {spec.path}:{line_number} "
                        f"status={status} path={row[spec.local_path_column]}"
                    )
                    continue
                relative = Path(row[spec.local_path_column])
                if relative.is_absolute():
                    errors.append(
                        f"absolute path for preserved record: {spec.path}:{line_number}"
                    )
                    continue
                path = ROOT / relative
                expected = row[spec.hash_column].strip().lower()
                if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
                    errors.append(f"invalid SHA-256: {spec.path}:{line_number}")
                    continue
                if not path.is_file():
                    errors.append(f"missing preserved source: {relative}")
                    continue
                checked += 1
                actual = sha256(path)
                if actual != expected:
                    errors.append(
                        f"SHA-256 mismatch: {relative} expected={expected} actual={actual}"
                    )
                expected_size = row.get("tamanho_bytes", "").strip()
                if expected_size:
                    try:
                        size = int(expected_size)
                    except ValueError:
                        errors.append(f"invalid byte size: {spec.path}:{line_number}")
                    else:
                        if path.stat().st_size != size:
                            errors.append(
                                f"byte-size mismatch: {relative} "
                                f"expected={size} actual={path.stat().st_size}"
                            )
    return checked


def validate_markdown_links(errors: list[str]) -> int:
    checked = 0
    for document in ROOT.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = unquote(target)
            checked += 1
            if not (document.parent / target).exists():
                errors.append(
                    f"broken local Markdown link: {document.relative_to(ROOT)} -> {target}"
                )
    return checked


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    csv_count = validate_csv_widths(errors)
    hash_count = validate_manifests(errors, warnings)
    link_count = validate_markdown_links(errors)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(
        f"Checked {csv_count} CSV files, {hash_count} preserved hashes, "
        f"and {link_count} local Markdown links; "
        f"warnings={len(warnings)} errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
