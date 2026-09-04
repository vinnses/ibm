# Work Unit Specification

Every execution branch requires a work specification containing the following fields before substantive work begins.

## Required fields

| Field | Requirement |
|---|---|
| Identifier and title | Stable short ID and descriptive title |
| Objective | One measurable outcome |
| Branch | Dedicated branch name |
| Commit base | Exact starting SHA from updated `main` |
| Primary-session assignment | Exact model and effort selected by the user or exposed by the runtime; never inferred |
| Agent assignments | For every actor: primary/subagent, functional role, exact model, effort, planned/actual status, and routing rationale |
| Escalation rule | Permitted reassignment path; must state that Sol subagents are prohibited and Sol-requiring work returns to the primary session |
| Inputs | Existing repository paths and authorized external sources |
| In scope | Closed list of tasks |
| Out of scope | Explicit exclusions, including tempting adjacent research |
| Deliverables | Exact expected paths and formats |
| Method | Capture, extraction, normalization, and validation rules |
| Acceptance criteria | Observable conditions for completion |
| Risks and uncertainty | Expected gaps, conflicting sources, or access limits |
| Validation | Commands and manual checks required before handoff |
| Error log | Exact per-work path under `governance/errors/` |
| Human review | Exact question-record path or an explicit statement that none is anticipated |

## Execution lifecycle

1. Inspect `main`, active branches, worktrees, and relevant governance.
2. Create the work branch from the recorded base.
3. Record model, effort, role, and routing rationale before assigning substantive work; never create a Sol subagent.
4. Capture and manifest sources before relying on them.
5. Extract or transcribe without interpretation drift.
6. Validate against sources and work-specific invariants.
7. Commit in semantically bounded increments.
8. Append every failed attempt, incorrect output, review defect, and recovery to the per-work error log.
9. Record any model reassignment or escalation before work continues and preserve it in the handoff.
10. Separate agent-correctable errors from questions that genuinely require human access or judgment.
11. Produce the handoff in the format defined by `HANDOFF.md`.
12. Stop. Integration is a separate authorization performed by the primary session.

Record assignments as a table or compact list with these stable fields: `Actor`, `Primary/subagent`, `Functional role`, `Model`, `Effort`, `Planned/actual`, and `Routing rationale`. Product-generated display names may identify actors but never substitute for `Model`.

## Definition of done

The work unit is done only when every acceptance criterion is met or explicitly classified as an unresolved gap that the specification permits. Discovery of a new research direction does not expand the work unit.
