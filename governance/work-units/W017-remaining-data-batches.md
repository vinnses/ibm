# W017 — Divide and publish remaining data work

- Objective: publish an actionable, prioritized backlog of small data-only batches and wait for the user's choice of execution extent.
- Branch: `governance/w017-remaining-data-batches`; commit base: `11c549e7b50316e9fe570cb4061beece1a089c15` (clean main matched fetched origin/main).
- Primary-session assignment: GPT-6 exposed family; backend and active effort not exposed; medium last user-requested.
- Agent assignments: primary / planner, scope reviewer and integrator / GPT-6 / medium last requested, runtime unknown / actual / small global planning update; no subagent activated, avoiding unavailable lower-tier usage. Future batch routing is planned only.
- Escalation rule: no Sol subagents; record future assignments before work. Unavailable lower-tier runtime does not authorize unrecorded primary takeover.
- Inputs: DATA_FIRST, ROADMAP, dataset/source indexes, curriculum inventories, W016 results, eight human-review questions and W010 correction list.
- In scope: divide remaining data work into selectable bounded batches, distinguish ready local extraction from public retrieval and institutional inputs, define per-batch artifacts/stop rules; update current restart status; review, integrate and push this planning-only Work as explicitly requested.
- Out of scope: executing any listed batch, new sources, data extraction, analysis, current operational checks, contacting institutions, resolving editorial backlog.
- Deliverables: `governance/REMAINING_DATA.md`, DATA_FIRST/ROADMAP pointers, W017 review/handoff/error log and WORK_INDEX integration entry.
- Method: preserve existing evidence statuses; avoid redoing already extracted fields; define small independent save points; future IDs D01-D09 identify backlog batches, not active Works.
- Acceptance criteria: user can select a batch and extent; each has inputs, output, maximum unit, model tier, stop rule and dependency; all future batches marked not started; plan committed and published.
- Risks/uncertainty: lower-tier quota unavailable at last attempt; no duration or remaining-quota promise. Public searches may fail; institutional documents cannot be inferred.
- Validation: governance/repository validators, `git diff --check`; scope review against latest user request.
- Error log: `governance/errors/W017.md`.
- Human review: no new questions; link existing records. User choice is required before batch execution, not before publishing this plan.
