#!/usr/bin/env python3
"""Validate per-work error events and human-review question records."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERROR_DIR = ROOT / "governance/errors"
HUMAN_DIR = ROOT / "governance/human-reviews"
EVENT_HEADING = re.compile(r"^## (E-W\d{3}-\d{3}) — ", re.MULTILINE)
QUESTION_HEADING = re.compile(r"^## (HR-W\d{3}-\d{3}) — ", re.MULTILINE)
EVENT_FIELDS = (
    "Date/time",
    "Work / branch",
    "Actor",
    "Operation",
    "Expected result",
    "Actual result",
    "Affected paths/state",
    "Impact",
    "Attempts",
    "Resolution/status",
    "Prevention/follow-up",
    "Evidence",
)
QUESTION_FIELDS = (
    "Related gap",
    "Why agent work is insufficient",
    "Human action/question",
    "Required response provenance",
    "Gate consequence",
    "Status",
)


def sections(text: str, pattern: re.Pattern[str]) -> list[tuple[str, str]]:
    matches = list(pattern.finditer(text))
    return [
        (match.group(1), text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)])
        for index, match in enumerate(matches)
    ]


def validate_records(
    paths: list[Path], pattern: re.Pattern[str], required_fields: tuple[str, ...], errors: list[str]
) -> tuple[int, set[str]]:
    count = 0
    identifiers: set[str] = set()
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for identifier, section in sections(text, pattern):
            count += 1
            if identifier in identifiers:
                errors.append(f"duplicate identifier: {identifier}")
            identifiers.add(identifier)
            for field in required_fields:
                if f"**{field}:**" not in section:
                    errors.append(f"missing {field} in {identifier} ({path.relative_to(ROOT)})")
    return count, identifiers


def main() -> int:
    errors: list[str] = []
    error_paths = sorted(path for path in ERROR_DIR.glob("W*.md") if path.is_file())
    human_paths = sorted(path for path in HUMAN_DIR.glob("W*.md") if path.is_file())
    event_count, event_ids = validate_records(error_paths, EVENT_HEADING, EVENT_FIELDS, errors)
    question_count, question_ids = validate_records(
        human_paths, QUESTION_HEADING, QUESTION_FIELDS, errors
    )

    expected_logs = {f"W{number:03d}.md" for number in range(8, 13)}
    missing_logs = expected_logs - {path.name for path in error_paths}
    if missing_logs:
        errors.append(f"missing expected retrospective logs: {sorted(missing_logs)}")
    if not event_ids:
        errors.append("no error events found")
    if not question_ids:
        errors.append("no human-review questions found")

    allowed_statuses = ("open", "resolved", "accepted exception", "blocked")
    for path in error_paths:
        for identifier, section in sections(path.read_text(encoding="utf-8"), EVENT_HEADING):
            status_line = next(
                (line for line in section.splitlines() if line.startswith("- **Resolution/status:**")),
                "",
            ).lower()
            if not any(status in status_line for status in allowed_statuses):
                errors.append(f"invalid or missing status value: {identifier}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"Checked {len(error_paths)} error logs with {event_count} events and "
        f"{len(human_paths)} human-review files with {question_count} questions; "
        f"errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
