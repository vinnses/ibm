#!/usr/bin/env python3
"""Validate per-work error events and human-review question records."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERROR_DIR = ROOT / "governance/errors"
HUMAN_DIR = ROOT / "governance/human-reviews"
WORK_DIR = ROOT / "governance/work-units"
HANDOFF_DIR = ROOT / "governance/handoffs"
REVIEW_DIR = ROOT / "governance/reviews"
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
ALLOWED_EVENT_STATUSES = {"open", "resolved", "accepted exception", "blocked"}
WORK_ROUTING_FIELDS = (
    "Primary-session assignment",
    "Agent assignments",
    "Escalation rule",
)
HANDOFF_ROUTING_FIELDS = (
    "Primary-session model and effort",
    "Agent assignments actually used",
    "Reassignments, escalations, equivalent-tier mappings, and routing deviations",
)
REVIEW_ROUTING_FIELDS = (
    "Reviewer assignment (primary/subagent, model, effort, routing rationale)",
)
WORK_ID = re.compile(r"W(\d{3})")


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


def event_status(section: str) -> str:
    status_line = next(
        (line for line in section.splitlines() if line.startswith("- **Resolution/status:**")),
        "",
    )
    value = status_line.partition("**Resolution/status:**")[2]
    return value.split(";", 1)[0].strip().lower()


def work_number(path: Path) -> int | None:
    match = WORK_ID.search(path.name)
    return int(match.group(1)) if match else None


def validate_routing_fields(
    directory: Path, required_fields: tuple[str, ...], errors: list[str]
) -> int:
    checked = 0
    for path in sorted(directory.glob("W*.md")):
        number = work_number(path)
        if number is None or number < 13:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8")
        for field in required_fields:
            line = next(
                (candidate for candidate in text.splitlines() if candidate.startswith(f"- {field}:")),
                "",
            )
            if not line or not line.partition(":")[2].strip():
                try:
                    display_path = path.relative_to(ROOT)
                except ValueError:
                    display_path = path
                errors.append(
                    f"missing or empty model-routing field {field} in {display_path}"
                )
    return checked


def main() -> int:
    errors: list[str] = []
    error_paths = sorted(path for path in ERROR_DIR.glob("W*.md") if path.is_file())
    human_paths = sorted(path for path in HUMAN_DIR.glob("W*.md") if path.is_file())
    event_count, event_ids = validate_records(error_paths, EVENT_HEADING, EVENT_FIELDS, errors)
    question_count, question_ids = validate_records(
        human_paths, QUESTION_HEADING, QUESTION_FIELDS, errors
    )

    expected_logs = {f"W{number:03d}.md" for number in range(8, 14)}
    missing_logs = expected_logs - {path.name for path in error_paths}
    if missing_logs:
        errors.append(f"missing expected retrospective logs: {sorted(missing_logs)}")
    if not event_ids:
        errors.append("no error events found")
    if not question_ids:
        errors.append("no human-review questions found")

    for path in error_paths:
        for identifier, section in sections(path.read_text(encoding="utf-8"), EVENT_HEADING):
            if event_status(section) not in ALLOWED_EVENT_STATUSES:
                errors.append(f"invalid or missing status value: {identifier}")

    routed_works = validate_routing_fields(WORK_DIR, WORK_ROUTING_FIELDS, errors)
    routed_handoffs = validate_routing_fields(HANDOFF_DIR, HANDOFF_ROUTING_FIELDS, errors)
    routed_reviews = validate_routing_fields(REVIEW_DIR, REVIEW_ROUTING_FIELDS, errors)

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(
        f"Checked {len(error_paths)} error logs with {event_count} events and "
        f"{len(human_paths)} human-review files with {question_count} questions; "
        f"routing records={routed_works} works/{routed_handoffs} handoffs/"
        f"{routed_reviews} reviews; errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
