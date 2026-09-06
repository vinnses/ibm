# W018 — D01 first preserved Ficha 1 batch

- Objective: publish one factual, source-located CSV for five already preserved Ficha 1 documents: CI1001, CI1002, CI1003, CI1055 and CI1215.
- Branch: `work/w018-d01-ficha1-batch`; commit base: `e861153344cf772d29c524fb8106221fdc255388` (clean main matched fetched origin/main).
- Primary-session assignment: GPT-5 exposed family; exact backend and active effort are not exposed. The primary acts as orchestrator, reviewer and integrator.
- Agent assignments: extractor `01a07485-ece4-7091-8840-b30978c79bf3` / subagent / mechanical PDF field extraction / `gpt-5.6-luna` / medium / actual, activated after specification commit `4c428d8` / five preserved documents with existing normalized ementas are a bounded extraction task. Primary / orchestrator, source reviewer and integrator / GPT-5 / effort unknown / actual / final source checks and integration remain in the user-supervised session.
- Escalation rule: no Sol subagents. A specific documentary ambiguity may be returned to the primary; no tier change or continuation after reassignment without a prospective record.
- Inputs: the five unchanged PDFs under `curriculos/2023/fichas/dinf/`; `manifesto-dinf.csv`; `fichas/inventario-dinf.md`; W010 `componentes.csv` and `ementas.csv`.
- In scope: create `dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv` and README; record document ID/type, code, source title, literal/normalized ementa, source-stated total hours, department/unit, dates, applicability, path/hash/page/field locator and normalization notes; add a compact W018 validator; Work error log, review and handoff. Reuse verified existing transcription, then check every row against PDF text/layout.
- Out of scope: new internet search; Ficha 2; other codes; changing source bytes/manifests/W010 inventories; deciding 2023 applicability; present offering/compliance; comparison or analysis; D09 refresh until D01 integration.
- Method: PDF skill read-only workflow; inspect complete relevant pages and render when layout is needed. Missing fields remain explicit. Applicability stays `indeterminado`; matching code/title does not prove continuity. One five-document data commit before documentation/review. Any source/data defect blocks; minor prose issues are deferred in the Work log.
- Deliverables: D01 CSV/README, `scripts/validate_w018_d01.py`, `governance/errors/W018.md`, W018 review/handoff.
- Acceptance criteria: exactly five unique codes and five Ficha 1 records; each path/hash agrees with manifest/stored bytes; ementa and stated metadata have PDF locator and source-supported value; no silent field invention or applicability upgrade; validator/repository/governance/whitespace checks pass.
- Risks/uncertainty: PDF extraction may obscure checkboxes, accents or signature dates; resolve by visual inspection or record `not stated/not identified`. Existing transcription is normalized and does not replace source bytes.
- Validation: W018 validator; W010 validator for regression; repository/governance validators; `git diff --check`; manual PDF samples for all five.
- Error log: `governance/errors/W018.md`.
- Human review: HR-W010-001 remains applicable; this batch does not establish which preserved Ficha version governs the 2023 curriculum.
- Checkpoints: A this specification; B five-row dataset/README/validator committed; C source review/handoff committed; D primary integration, D09 refresh and publication. Stop after D01+D09; no next D01 batch automatically.
