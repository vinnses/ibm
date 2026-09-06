# W019 — D01 second preserved Ficha 1 batch

- Objective: publish five source-located Ficha 1 records for CI1005, CI1007, CI1056, CI1057 and CI1062.
- Branch/base: `work/w019-d01-ficha1-batch2`, `3530173f374d0c361e9f8829d3347c638b21a7db` (clean fetched main/origin).
- Primary-session assignment: GPT-5 exposed family; backend/effort unknown; orchestrator/reviewer/integrator.
- Agent assignments: extractor `01a07485-ece4-7091-8840-b30978c79bf3` / subagent / `gpt-5.6-luna` / medium / planned reuse after this spec / same bounded extraction successfully completed W018. Primary / GPT-5 / effort unknown / actual / source review/integration.
- Escalation rule: no Sol subagent; ambiguity returns to primary; record runtime-limit interruption and preserve last commit.
- Inputs: five unchanged DInf PDFs, manifest, existing normalized ementas, W010 index; W018 format/validator as reusable template.
- In scope/deliverables: `dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv`, README, `scripts/validate_w019_d01.py`, W019 error/review/handoff. Same fields and source checks as W018.
- Out of scope: web/new sources, Ficha 2, other codes, source/W010 edits, applicability decisions, present practice, analysis, third batch.
- Method/acceptance: reuse existing transcription and verify PDF page 1/layout; exactly five unique rows; path/hash/URL match manifest; source title/ementa/hours/unit/date locators explicit; missing values explicit; applicability `indeterminado`; originals unchanged.
- Validation: W019, W018 and W010 validators; governance/repository; `git diff --check`.
- Risks: layout/signature ambiguity; use visual inspection or explicit `not stated`.
- Error log: `governance/errors/W019.md`.
- Human review: HR-W010-001 remains; extraction does not establish 2023 applicability.
- Checkpoints: A spec; B five-row data commit; C primary review/integration and D09 refresh; stop and push.
