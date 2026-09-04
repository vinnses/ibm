# Handoff — W013: Enforce model routing and primary-session authority

- Branch: `governance/w013-model-routing`.
- Commit base: `92b3f4cfb236cea252b917ad5cf6c5cd8c540929`.
- Commits produced: `eedbaae` (Work specification); `8204236` (binding routing rules and prospective validation); `3e37081` (negative-test correction and audited resolution); handoff commit at branch `HEAD`.
- Primary-session model and effort: Sol/medium, selected by the user for this active session; used directly for orchestration and the cross-cutting governance implementation.
- Agent assignments actually used: primary agent / primary / orchestrator and governance implementer / Sol / medium / user-selected active session / appropriate because this is a global governance change reserved to the primary session. No implementation subagent was used. Independent review is pending and must use a recorded non-Sol assignment.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none. No Sol subagent was created. No model identity was inferred from an agent display name.
- Objective: make model routing, primary-session authority, and actual assignment provenance binding and machine-auditable for future Works.
- Completion verdict: implementation complete; awaiting independent non-Sol review before integration.
- Deliverables: updated repository entry instructions, agent operations, decision log, Work/review/handoff/error contracts, templates, and prospective automated routing checks.
- Primary files: `AGENTS.md`; `governance/AGENT_OPERATIONS.md`; `governance/DECISIONS.md`; `governance/specs/WORK_UNIT.md`; `governance/specs/REVIEW.md`; `governance/specs/HANDOFF.md`; `governance/specs/ERROR_RECORD.md`; `scripts/validate_governance_audit.py`.
- Sources added: no external research source. The binding policy clarification was supplied directly by the user in the active session and governs agent operation rather than documentary claims about the course.
- Coverage reached: prospective W013-and-later Work specs, handoffs, and reviews; historical unrecorded model assignments remain unknown rather than reconstructed.
- Validation and result: negative fixture test rejects two omitted routing fields; governance audit passes six logs/23 events and the W013 Work routing record; repository validator passes with zero warnings/errors; `git diff --check` passes.
- Gaps: the runtime does not expose reliable historical model provenance for earlier reused agents; no retrospective assignment is asserted.
- Divergences: prior governance said `Sol/high` for integration; the binding correction makes integration, final audit, and global synthesis primary-session duties at the current user-selected model/effort, while prohibiting all Sol subagents.
- Provisional information: none.
- Explicitly not performed: no W010/P1 work; no P2-P4 research; no historical model identities invented; no integration into `main` before review.
- Error log, resolved events, and open events: `governance/errors/W013.md`; resolved `E-W013-001`; no open W013 event.
- Human-review questions and gate consequences: no additional human-only question. The user's model/effort selection remains authoritative, and only the user may change it.
- Recommended next bounded work unit: independent Terra review of W013; if approved, the primary session integrates W013, updates global indexes, validates, and synchronizes the remote.

