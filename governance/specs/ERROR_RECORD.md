# Agent and Process Error Record

Every agent, tool, validation, review, source-access, Git, environment, or orchestration error must be recorded in the affected work's file under `governance/errors/`. Record failed attempts even when a later attempt succeeds. Do not erase or rewrite the failed path; append the resolution.

Using an unrecorded model/effort, creating a Sol subagent, delegating primary-session-only work, or continuing after an unrecorded model escalation is an orchestration error and must be recorded.

## Required fields

- `Event ID`: stable `E-W###-NNN` identifier.
- `Date/time`: ISO date and time zone when available.
- `Work / branch`: affected work and branch.
- `Actor`: orchestrator, collector, reviewer, integrator, tool, or environment.
- `Operation`: command or bounded action being attempted.
- `Expected result`: intended observable outcome.
- `Actual result`: exact failure or incorrect result, with a short sanitized excerpt when useful.
- `Affected paths/state`: files, branch, worktree, remote state, or evidence claims affected.
- `Impact`: effect on evidence, reproducibility, scope, timing, or gate status.
- `Attempts`: ordered recovery attempts and their outcomes.
- `Resolution/status`: `open`, `resolved`, `accepted exception`, or `blocked`.
- `Prevention/follow-up`: check or rule that should prevent recurrence.
- `Evidence`: commit, review, handoff, preserved source, or command-output reference.

## Rules

- Never include passwords, tokens, private keys, session cookies, or other secrets.
- Preserve original source bytes even when they contain formatting defects; log the consequence instead of normalizing the source.
- A review finding is an error event when it identifies an incorrect claim, transcription, provenance link, dataset rule, missing required deliverable, or false negative search.
- A source that is genuinely inaccessible is a source-access event, not proof of nonexistence.
- Corrections must point back to the original event ID. If a correction is itself wrong, append a new event.
- Each Work owns its own log so parallel branches do not edit a shared event file. Global summaries may be generated only during integration.
- The handoff must list open event IDs and confirm that resolved events remain in the log.

## Human-review separation

Agent-correctable defects remain in the error log and are returned to the implementing agent. Questions requiring protected access, institutional knowledge, identity/authority, value judgment, or materially ambiguous interpretation also receive a separate record under `governance/human-reviews/`.
