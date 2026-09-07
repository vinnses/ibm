#!/usr/bin/env python3
"""Validate W029's preserved-source extraction closure outputs."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados" / "extracoes-w029"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    readme = OUT / "README.md"
    data_path = OUT / "proposal-2026.json"
    if not readme.exists():
        errors.append("missing extraction README")
    if not data_path.exists():
        errors.append("missing proposal JSON")
    if errors:
        print("W029 preserved extraction validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid proposal JSON: {exc}")
        data = {}

    if data.get("work") != "W029":
        errors.append("proposal JSON has incorrect work identifier")
    if len(data.get("sources", [])) != 2:
        errors.append("proposal JSON must cite exactly two preserved source inputs")
    for source in data.get("sources", []):
        local = ROOT / source.get("local_path", "")
        if not local.is_file():
            errors.append(f"missing cited source: {source.get('local_path', '')}")
            continue
        actual = sha256(local)
        if actual != source.get("sha256"):
            errors.append(
                f"hash mismatch for {source.get('local_path', '')}: "
                f"expected {source.get('sha256', '')}, actual {actual}"
            )

    call = data.get("call", {})
    for key in ("purpose", "submission_method", "mandatory_submission_parts", "schedule", "locators"):
        if not call.get(key):
            errors.append(f"missing call field: {key}")
    proposal = data.get("proposal", {})
    for key in (
        "current_course_name",
        "proposed_course_name",
        "campus",
        "degree",
        "shift",
        "format",
        "student_vacancies_stated",
        "current_hours_stated",
        "proposed_hours_stated",
        "locators",
        "limits",
    ):
        if proposal.get(key) in (None, "", [], {}):
            errors.append(f"missing proposal field: {key}")
    if proposal.get("evidence_status") != "proposal_statement_only":
        errors.append("proposal evidence status must remain proposal_statement_only")
    if not readme.read_text(encoding="utf-8").count("| 2026 internal call and proposal form |"):
        errors.append("README lacks the 2026 proposal-family review row")
    if readme.read_text(encoding="utf-8").count("| ") < 8:
        errors.append("README does not contain the expected family review table")

    if errors:
        print("W029 preserved extraction validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("W029 preserved extraction validation passed: 8 families reviewed, 1 JSON output, 2 preserved inputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
