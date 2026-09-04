# Work Unit Specification

Every execution branch requires a work specification containing the following fields before substantive work begins.

## Required fields

| Field | Requirement |
|---|---|
| Identifier and title | Stable short ID and descriptive title |
| Objective | One measurable outcome |
| Branch | Dedicated branch name |
| Commit base | Exact starting SHA from updated `main` |
| Inputs | Existing repository paths and authorized external sources |
| In scope | Closed list of tasks |
| Out of scope | Explicit exclusions, including tempting adjacent research |
| Deliverables | Exact expected paths and formats |
| Method | Capture, extraction, normalization, and validation rules |
| Acceptance criteria | Observable conditions for completion |
| Risks and uncertainty | Expected gaps, conflicting sources, or access limits |
| Validation | Commands and manual checks required before handoff |

## Execution lifecycle

1. Inspect `main`, active branches, worktrees, and relevant governance.
2. Create the work branch from the recorded base.
3. Capture and manifest sources before relying on them.
4. Extract or transcribe without interpretation drift.
5. Validate against sources and work-specific invariants.
6. Commit in semantically bounded increments.
7. Produce the handoff in the format defined by `HANDOFF.md`.
8. Stop. Integration is a separate authorization.

## Definition of done

The work unit is done only when every acceptance criterion is met or explicitly classified as an unresolved gap that the specification permits. Discovery of a new research direction does not expand the work unit.
