# W052 — Cross-conversation research-front transfer

- Objective: make the unfinished courses and jobs evidence-collection fronts independently resumable from repository governance, without starting either research work.
- Branch: `work/w052-research-fronts-handoff`.
- Commit base: `5fd445bf56df6ceea94ea4315f810c7bb1ed9578` from updated `main`.
- Primary-session assignment: active primary Codex runtime; exact model variant and effort are not exposed and are not inferred.
- Agent assignments: primary agent, orchestrator/reviewer/integrator, active runtime, effort not exposed, actual; repository cross-branch reconciliation and governance integration. No subagents.
- Escalation: Sol subagents are prohibited; any Sol-requiring work returns to the user-supervised primary. No delegation planned.
- Inputs: W040, W041 and W044 branch specifications, datasets, handoffs, validators and error logs; current `main` governance and the user's direction to focus on data, documents and information.
- In scope: verify branch/deliverable locations and status; record two separate continuation tracks, concrete next gates and non-goals; link them from governance index/roadmap/work index; validate, merge and push `main`.
- Out of scope: new searches, downloads, dataset edits, analyses, curriculum judgments, W040/W041/W044 branch merge, site changes or deployment.
- Deliverables: `governance/RESEARCH_FRONTS.md`, updates to `governance/README.md`, `governance/ROADMAP.md`, `governance/WORK_INDEX.md`, W052 error record and handoff.
- Method: use repository commits and worktree files as evidence; distinguish completed bounded batches from unfinished broad fronts; preserve exact branch identifiers and documentary caveats; give each future conversation its own restart instruction.
- Acceptance: both fronts have objective, current artifact path/branch, verified counts and limits, next bounded actions, integration gate, validation path and no-analysis boundary; `main` governance links to the transfer record; repository validation passes.
- Risks: branch outputs are not in `main`; GitHub push protection has blocked bulk branch synchronization; the W041 worktree contains an unrelated untracked user PDF. Do not alter these states.
- Validation: compare notes to W040/W041/W044 handoffs and repository tree; `python scripts/validate_repository.py`; `git diff --check`; verify `main` and remote after integration.
- Error log: `governance/errors/W052-research-fronts-handoff.md`.
- Human review: no new question anticipated; existing source-access and branch-push gates remain as recorded in their original Works.
