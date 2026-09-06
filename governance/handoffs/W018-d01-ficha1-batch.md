# W018 handoff — D01 five Ficha 1 records

- Branch and commit base: `work/w018-d01-ficha1-batch`, `e861153344cf772d29c524fb8106221fdc255388`.
- Commits produced: `4c428d8` specification; `5dbce54` five-row data/validator checkpoint; containing closure commit adds review/handoff and assignment identity.
- Primary-session model and effort: GPT-5 exposed family; exact backend and active effort not exposed.
- Agent assignments actually used: `01a07485-ece4-7091-8840-b30978c79bf3` / subagent / extractor / `gpt-5.6-luna` / medium / bounded five-PDF extraction; primary / orchestrator, PDF source reviewer and integrator / GPT-5 / effort unknown / direct source checks and integration.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none; no Sol subagent and no model inference from nickname.
- Objective and completion verdict: five preserved Ficha 1 records extracted with locators and provenance; approved with documented exceptions.
- Deliverables: `dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv`, README and `scripts/validate_w018_d01.py`.
- Sources added: none; exact pre-existing PDFs retained unchanged. Coverage: CI1001, CI1002, CI1003, CI1055 and CI1215, one Ficha 1 row each.
- Validations: W018 source/hash/row validator, W010 regression validator, repository/governance and whitespace checks; final output recorded at integration.
- Gaps/divergences/provisional information: applicability to 2023 is indeterminate for every row; document date is not stated; signature date not identified for CI1003/CI1215. Existing normalized text is a transcription aid; PDFs remain authoritative.
- Explicitly unperformed: new retrieval, Ficha 2, other codes, current compliance/offering, analysis, source/manifest/W010 modification, another D01 batch.
- Error log: `governance/errors/W018.md`; resolved E-W018-001 and E-W018-002; no open event.
- Human review: HR-W010-001 remains and prevents treating these versions as proven applicable to the 2023 curriculum.
- Active substep / restart: D01 dataset complete; primary integration and D09 access refresh next. Stop afterward and await user direction for another batch.

## Integration record

Branch `work/w018-d01-ficha1-batch` at `edbf444` was published and merged by `d94900e` without conflicts, directly by the unchanged primary GPT-5 session. D09 was limited to extending the existing access builder to include non-generated CSVs under `dados/`, regenerating the access package and recording W018 status. Final W018/W010/access/governance/repository/whitespace checks passed. Main publication and remote equality are verified after the containing integration-metadata commit. No second extraction or analysis batch was started.
