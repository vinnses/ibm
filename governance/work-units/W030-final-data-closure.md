# W030 — Final documentary data closure and CPA extraction

- Objective: reproducibly extract the preserved CPA workbook and determine whether any justified, currently executable factual collection/extraction task remains.
- Branch: `work/w030-final-data-closure`.
- Exact updated remote-main base: `c87d5a996210135807821b8c8d5ad757b25485de` (origin/main fetched 2026-09-07).
- Primary-session assignment: runtime exposes GPT-6 family; exact backend model and selected effort are not exposed and are recorded as unknown, not inferred from the user's suggested routing.

- Agent assignments: recorded in the table below and the prospective execution log.

| Actor | Primary/subagent | Functional role | Model | Effort | Planned/actual | Routing rationale |
|---|---|---|---|---|---|---|
| primary | primary | orchestration, final audit, integration within W030 branch | GPT-6 family; exact backend unknown | unknown | actual | primary-session authority |
| cpa-extractor | subagent | workbook inspection, Python extraction, normalization and validation | gpt-5.6-luna | medium | planned | mechanical processing |
| gap-reviewer | subagent | repository evidence and remaining-gap classification | gpt-5.6-terra | medium | planned | documentary investigation |

- Escalation rule: ambiguous structure returns to primary for routing; Terra/high only if necessary and recorded before use. No Sol subagent. Sol-requiring work returns to the primary.
- Inputs: `administracao/historico/fontes/documentos/cpa-avaliacao-curso-informatica-biomedica-2022.xlsx`, its preserved CPA page and existing manifests; W029 handoff; remaining-data, roadmap, work index, release/catalogs and human-review records.
- In scope: source identity and structure inspection; faithful cell intermediate; source-derived normalized data; deterministic Python extraction/validation; exhaustive review of already recorded gaps; authorized global index and documentary release rebuild; final factual closure and handoff.
- Out of scope: curricular comparison, lineage, similarity, evaluation, argument, recommendations, visualization/site, institutional contact, protected-access bypass, broad/repeated searches without a concrete new lead, source workbook modification, merge to main, subsequent milestones.
- Deliverables: `scripts/extract_cpa_workbook.py`, `scripts/validate_cpa_extraction.py`, `administracao/dados/cpa/` inventory/intermediate/datasets/methodology; `governance/reviews/W030-final-data-closure.md`; updated documentary-access outputs; `dados/entrega-documental/FECHAMENTO_DA_COLETA.md`; `governance/handoffs/W030-final-data-closure.md`.
- Method: inspect with openpyxl before schema design; preserve source bytes and hash; retain formulas separately from stored caches without recalculation; preserve literal headers, categories and universes; do not impute denominators, zeros or counts. All observations carry source coordinates. The explicit user instruction authorizes Python and takes precedence over spreadsheet-skill defaults. Delegated subtasks use disjoint owned paths on the sole user-required branch; only primary commits and updates global indexes.
- Acceptance: original SHA unchanged, all relevant cells represented, deterministic outputs, source-linked observations, source-supported consistency checks, repository and related validators passing, rebuilt catalogs/release, every remaining gap classified, explicit agent-actionability verdict, no unjustified new collection.
- Risks/uncertainty: workbook may omit population/period/denominators; absent information stays absent. Public-search exhaustion and institutional custody do not prove nonexistence.
- Validation: `python scripts/extract_cpa_workbook.py`; `python scripts/validate_cpa_extraction.py`; deterministic regeneration; documentary builders and related validators; `python scripts/validate_repository.py`; governance audit and `git diff --check`.
- Error log: `governance/errors/W030.md` (append-only).
- Human review: existing `governance/human-reviews/` questions retain their evidence gates; consolidated W030 register will reference them; no institutional answer is required to close autonomous extraction.
- Commit policy: primary creates scoped incremental commits; exact resulting list in final handoff/response. No merge or automatic next Work.

## Assignment execution log

- `cpa_extractor`: initial spawn interrupted before accepting outputs because `fork_turns=all` cannot establish the requested override; actual backend/effort unknown (E-W030-001).
- `cpa_python`: replacement assignment, `gpt-5.6-luna` / medium, mechanical extractor, planned before spawn using bounded fork.
- `gap_reviewer`: `gpt-5.6-terra` / medium, actual, bounded-fork documentary review with disjoint output paths.
- `historical_ficha_extractor`: `gpt-5.6-luna` / medium, planned before spawn; mechanical extraction of twelve already-preserved W022-W024 PDFs into `dados/curriculos/2011/fichas-preservadas/` with `scripts/extract_w030_historical_fichas.py` and `scripts/validate_w030_historical_fichas.py`. Required by Part I: reviewer identified a concrete local extraction omission in W029, not a new research front. Preserve version/applicability uncertainty; no new searches. Primary performs catalog integration; no historical inventory status is silently replaced.
