# W015 — Existing data access package

- Objective: deliver a reproducible access index for existing repository data and source records, and a factual queue of already recorded gaps.
- Branch: `work/w015-data-access`; commit base: `ac096760373114e93585c9c021c1fbb7fdb52f75`.
- Primary-session assignment: GPT-6 exposed family; backend/active effort not exposed; medium last requested by user. Primary handles review/integration.
- Agent assignments: collector / subagent / mechanical indexer and extractor / `gpt-5.6-luna` / medium / actual assignment before activation / existing CSV discovery and faithful record indexing are mechanical. Primary / reviewer, integrator / GPT-6 / medium last requested, runtime unknown / actual / final audit remains primary.
- Escalation rule: no Sol subagent; documentary ambiguity is retained as a gap and returned to primary; record reassignment before any continued work.
- Inputs: existing curriculum/admin CSVs, local manifests, original-source paths, human-review and negative-search records on recorded baseline.
- In scope: `dados/acesso/README.md`, `datasets.csv`, `source-records.csv`, `gaps.csv`; one small reproducible builder/checker under `scripts/`; W015 handoff/error log. Source-record index must retain origin manifest and record identity/row, path, URL, original metadata/status and hash without silently deduplicating conflicting versions. Dataset index includes path, header, row count, SHA-256 and scope. Gap queue copies existing records with source path/ID and distinguishes institutional access from public documentary gaps. Do not invent component facts or priority based on content names.
- Out of scope: changing existing sources/CSV schemas/global indexes, new internet research, comparison, inference, current compliance/offering checks, editorial cleanup.
- Method: discover CSV inputs explicitly; exclude own generated output; preserve original metadata and noncomparable records. Use apply_patch for scripts/docs; generated data may use the committed builder. Do not use spreadsheet artifact tooling for repository CSV indexing. Keep terminal output compact.
- Acceptance criteria: every indexed path exists, counts and hashes match; original manifest records are traceable; preserved/not-located statuses remain distinct; output is deterministic on the recorded snapshot; README links to useful datasets without claiming all underlying documents are available.
- Validation: builder/check mode or reproducibility comparison; `python scripts/validate_repository.py`; `python scripts/validate_governance_audit.py`; `git diff --check`.
- Error log: `governance/errors/W015.md`; log every unplanned failure, minor items may be deferred explicitly.
- Human review: reference existing W009/W010/W011 human-review records; no new question required.
- Checkpoints: A specification commit (primary); B dataset index and README commit; C manifest index/gap queue and validated handoff commit. If interrupted stop after the last complete commit; record active substep. No integration or push by subagent; primary publishes checkpoints and integrates separately under user's data-first execution request.
