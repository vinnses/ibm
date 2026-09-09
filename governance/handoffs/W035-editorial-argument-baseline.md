# W035 — Initial editorial argument and AI curricular spine handoff

- Branch: `work/w035-editorial-argument-baseline`.
- Commit base: `3cd8680d394ac22cfbf473050bc3f08991156356`, synchronized local and remote `main` after W034 publication.
- Commits produced before the closure commit:
  - `b45fa08` — define the W035 work unit;
  - `089e44d` — preserve W035 editorial premises and AI reference;
  - `e4c60a4` — draft the evidence-disciplined AI curriculum argument.
- Primary-session model and effort: GPT-5 family as exposed by the active runtime; exact backend model and reasoning effort were not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary session only; details follow.

| Actor | Primary/subagent | Functional role | Model | Effort | Routing rationale |
|---|---|---|---|---|---|
| primary | primary | orchestration, public-source preservation, documentary reconciliation, testimony classification, editorial synthesis, curricular framing, validation, acceptance review, and handoff | GPT-5 family; exact backend unknown | unknown | The Work combines stakeholder premises, evidence boundaries, and normative synthesis under primary-session authority. |

- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none. No subagent and no Sol subagent were created.
- Objective and completion verdict: establish a first evidence-disciplined editorial line and AIMA-informed AI curricular spine without a complete matrix, workload balancing, or final 2026 judgment. **W035 complete.**

## Deliverables and coverage

- `argumentacao/linha-editorial-inicial.md`: Portuguese editorial baseline, epistemic-status table, six-block AI reading, candidate foundation/AI architecture, sector scenario rules, matrix tests, messaging lines, evidence gaps, and explicit deferrals.
- `governance/research-hypotheses/2026-09-09-editorial-premises.md`: stakeholder testimony preserved in substance without conversion into institutional fact.
- `argumentacao/fontes/`: unchanged Pearson source page, provenance/hash manifest, and source note.
- `scripts/validate_w035_editorial_argument.py`: source, W029 value/status, epistemic-label, six-block, missing-matrix, sector-claim, and no-fixed-workload checks.
- Acceptance audit, error log, and human-review questions under `governance/`.

The argument covers foundations and agents; search/optimization; knowledge,
reasoning, and planning; uncertainty and decision; machine learning, deep
learning, and reinforcement learning; language; vision; action/robotics; and
ethics/future. Candidate units have no assigned hours and are not an approved
matrix.

## Sources and documentary boundary

One new public source was added: Pearson's official fourth-edition product
page for *Artificial Intelligence: A Modern Approach*. Original bytes are
preserved at SHA-256
`3e72f7725f19d338025e9c52754cf63bd28018d97687bb0ff7f7ef6976bcf242`.
The page supplies fourth-edition metadata and a public 27-chapter contents
sequence. W035 derives, and labels as interpretation, six curricular blocks.

The W029 extraction remains unchanged: 3,200 current hours and 2,700 proposed
hours are statements from the proposal; the component-level proposed matrix is
not preserved; proposal existence does not establish selection, approval,
authorization, or implementation. No source establishes 2,700 as a MEC ceiling.

## Validation

- W031 baseline: 16 preserved sources, Compose/application/secret checks, zero errors.
- W032: 84 components, 54 dependencies, 56 documents, 18 domains, 156 topics, 242 occurrences, 12 relations, 246 evidence records, and 658 evidence links; negative invariants passed.
- W033: 52 corpus sources, 260 proposals, 242 occurrences, 3 aliases, and 12 relations; provenance and uncertainty passed.
- W034: required historical samples and UI source assertions passed; runtime intentionally skipped by that validator because W035 does not change the site.
- W035: source hash/provenance, W029 hours/status, epistemic separation, six-block derivation, missing matrix, sector boundaries, and workload deferral passed.
- Repository: 224 CSVs, 126 preserved hashes, and 279 local Markdown links; zero warnings/errors.
- Governance: 28 logs, 178 events, 5 human-review files with 13 questions, and routing metadata passed.
- `git diff --check`: passed.

## Gaps, divergences, and provisional information

- Gaps: exact regulatory basis for 2,700; applicable missing Fichas; complete proposed matrix/equivalences; formal sector positions; staffing; objectives, prerequisites, and transition records.
- Divergence corrected: the initial Work specification overstated the exact six-block grouping as source-backed; it now distinguishes the sourced chapters from the derived grouping (E-W035-005).
- Provisional information: sector expectations are stakeholder testimony; candidate AI units and protected-foundation rule are normative proposals; the six-block mapping is an interpretation.
- No W033 taxonomy or occurrence data, current curriculum, proposal extraction, or site route was changed.

## Audit closure and explicit exclusions

- Error log: `governance/errors/W035.md`.
- Resolved event IDs: E-W035-002 through E-W035-006.
- Accepted exception: E-W035-001, current AIMA author site outage; the accessible official Pearson page was preserved instead.
- Open error event IDs: none.
- Human-review question path: `governance/human-reviews/W035.md`.
- Open human-review questions: HR-W035-001 through HR-W035-003.
- Gate consequences: these questions do not block this provisional argument; they block claiming a MEC ceiling, treating sector expectations as institutional facts, completing documentary 2023→2026 lineage, selecting defensible reductions/equivalences, or validating a final matrix.
- Explicitly unperformed: complete 2026 matrix, component hours, workload optimization, named component removal, final recommendation, approval/rejection conclusion, systematic 2023→2026 comparison, Ficha ingestion, institutional request, formal sector negotiation, site changes, merge, push, deployment, global-index update, W036, manifesto, or campaign.
- Recommended next bounded work unit: after the complete proposed matrix and new Fichas are obtained, preserve and ingest them before a documentary 2023→2026 lineage and scenario comparison. Do not start it automatically.

## Integration update — 2026-09-09

- Merged branch: `work/w035-editorial-argument-baseline` into local `main` after explicit user authorization.
- Merge commit: `e4c23e03972a63b9b0c9f2ecb02d757c8dbc7ea2` (`Merge W035 editorial argument baseline`).
- Conflict resolution: none; the `ort` merge completed cleanly.
- Global indexes updated: none; W035 adds one locally manifested argument source but does not authorize a global documentary-index integration milestone.
- Application/site state: unchanged. W035 is a documentary and editorial baseline, not a site implementation Work, so no route, container image, or public deployment was modified or unnecessarily rebuilt.
- Final validation: W031, W032, W033, W034, W035, repository, governance, and diff checks passed on merged `main` before remote synchronization.
- Remote synchronization state: merge and integration record through `1f2332e` were pushed successfully to `origin/main`; the final synchronization-record commit follows this verified push.
