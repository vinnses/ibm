# W051 — IBM/UFPR header mark

- Objective: replace the small `IB` header mark with a coherent `IBM` / rule / `UFPR` mark on both the Svelte site and Dash analysis page.
- Branch: `work/w051-ibm-ufpr-mark`.
- Commit base: `63794d85aae88c949cacf314433bb00744977eb6` from updated `main`.
- Primary-session assignment: active primary Codex runtime; exact model variant and effort are not exposed by this runtime and are not inferred.
- Agent assignments: primary agent, implementer/reviewer/integrator, active primary runtime, effort not exposed, actual; small cross-stack visual consistency change. No subagents.
- Escalation: Sol subagents are prohibited; Sol-requiring work returns to the primary. No delegation planned.
- Inputs: existing `site/src/routes/+layout.svelte`, `analises/app.py`, and `analises/assets/style.css`; user's visual direction.
- In scope: logo markup and styling in the shared Svelte and Dash headers, validation, publication, and non-forced `main` push.
- Out of scope: typography or layout redesign elsewhere, new brand assets, source research, and historical branch synchronization.
- Deliverables: the three changed interface files, this spec, an append-only W051 error record, and W051 handoff.
- Method: use native text and CSS so the mark stays crisp and accessible; preserve navigation and existing color palette.
- Acceptance: both headers render `IBM` above a horizontal rule and smaller `UFPR`; home links remain functional; builds and repository validator pass; public Svelte and Dash routes respond after deployment.
- Risks: two separate frontend stacks could drift visually; keep dimensions and styles aligned. Existing historical branch push protection is unrelated to this bounded mark update.
- Validation: Docker Svelte/Dash builds, Dash layout inspection, HTTP response checks, `python scripts/validate_repository.py`, and `git diff --check`.
- Error log: `governance/errors/W051-ibm-ufpr-mark.md`.
- Human review: none anticipated.
