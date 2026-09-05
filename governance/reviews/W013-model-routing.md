# Independent review — W013 model routing and primary-session authority

- Date: 2026-09-04.
- Reviewer role: independent governance reviewer.
- Reviewer assignment (primary/subagent, model, effort, routing rationale): subagent / independent governance reviewer / gpt-5.6-terra (Terra) / high / actual; cross-validation of binding, cross-cutting model-routing rules.
- Branch and commits: `governance/w013-model-routing`; reviewed `eedbaae`, `8204236`, `3e37081`, and `4ad0d41`.
- Verdict: `approved for integration`.

## Findings

### Blocking

None.

### Non-blocking

None.

### Preservation and provenance

This is a governance-only work. It adds no project-subject source and makes no documentary or historical-curriculum claim. The user-supplied routing policy is correctly treated as operational authority rather than course evidence.

### Reproducibility

The routing audit identifies W013-and-later Work, handoff, and review records by stable filename and verifies the required routing-record fields. Independent external temporary fixtures confirmed that a complete prospective Work record is accepted and that an incomplete record is rejected with exactly the two expected missing-field diagnostics. The external-path diagnostic fallback introduced in `3e37081` operates correctly.

### Scope and historical validity

The changes stay within W013's defined governance scope. They do not rewrite W008-W012, undertake P1-P4 research, or infer historical model identity. Historical assignments without recorded provenance remain explicitly `unknown`.

### Process errors and human-review boundary

`E-W013-001` retains the initial negative-test failure and a dated resolved correction. `E-W013-002` records the review cleanup-command rejection and explicit safe cleanup; it is resolved and did not affect tracked content. The W013 handoff correctly reports no open W013 events. No human-only question is introduced: the user's model/effort selection remains an authority boundary, not a research gap.

### Model routing and primary-session authority

The binding rules agree across `AGENTS.md`, `governance/AGENT_OPERATIONS.md`, `governance/DECISIONS.md`, the Work/review/handoff/error specifications, and their templates:

- Sol is reserved to the user-supervised primary agent and prohibited for every subagent effort level; Sol-requiring delegated work returns to the active primary session.
- Integration, final audit, and global synthesis remain direct duties of that session at its current user-selected model and effort. Only the user may change that selection.
- Luna/medium is assigned to mechanical work; Terra/medium to documentary investigation and structured search; Terra/high to reconciliation, cross-validation, divergence audit, and demanding independent review.
- Prospective Work and handoff records require model, effort, role, assignment status, routing rationale, and pre-continuation reassignment/escalation provenance. The reviewer template requires the equivalent reviewer assignment record.

The W013 specification and handoff meet the new requirements. No Sol subagent was recorded or created for implementation, and this independent review's actual non-Sol Terra/high assignment is now recorded. The validator appropriately limits retrospective checking to W013-and-later records, avoiding invention of unrecorded historical models.

## Validation executed

- `python scripts/validate_governance_audit.py` — passed before this review record: six error logs, 23 events, three human-review files, eight questions, and one W013 Work/one handoff routing record; zero errors.
- Independent `validate_routing_fields` fixtures outside the repository root — passed: complete W999 routing record accepted; incomplete W999 record rejected with exactly two missing-field errors.
- `python scripts/validate_repository.py` — passed: 24 CSV files, 126 preserved hashes, and 95 local Markdown links; zero warnings and zero errors.
- `git diff --check` — passed on the clean pre-review worktree.

## Exceptions and roadmap destination

None. This review approves W013 for user-supervised primary-session integration; it does not integrate, push, change the active primary-session model/effort, or authorize subsequent roadmap work.
