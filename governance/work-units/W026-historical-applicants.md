# W026 — Historical applicant-count data

- Objective: locate and preserve official absolute applicant-count records for Informática Biomédica admission processes from 2015 through 2026 where not already represented, without deriving counts from ratios or unmatched vacancy acts.
- Branch/base: `work/w026-historical-applicants`; `b1669e01a8cc9d38449d044b0fbf632ff20497eb`.
- Primary-session assignment: GPT-5 exposed family; backend/effort unavailable; actual orchestrator, reviewer and integrator.
- Agent assignments: `01a076b5-7590-7dd0-bfcc-180246e9027e` / subagent / documentary investigator / `gpt-5.6-terra` / medium / planned reuse / targeted stable official-data retrieval. Recorded Luna/medium may perform mechanical capture after exact source identification. Primary / primary / reviewer-integrator / GPT-5 exposed family / effort unknown / actual.
- Escalation rule: denominator/universe ambiguity returns to primary; no Sol subagent.
- Inputs: existing UFPR/NC datasets and sources, W011 searches, official NC/UFPR and UFPR archive surfaces. Existing 2016 total and 2019/2020 partial category remain unchanged.
- In-scope checkpoints: H1 2015/2017; H2 2018/2019; H3 2021/2022; H4 2023/2024; H5 2025/2026. Up to three new targeted official attempts per year/process.
- Deliverables: preserved originals and manifest; `dados/administracao/candidatos-historicos.csv` with source-stated count, process, year, category/universe, unit, denominator status and locator; negative-search log; validator, errors/review/handoff.
- Method: preserve originals before use; retain categories separately; never sum overlapping categories; never calculate absolute applicants from candidate/vacancy ratios or vacancy acts; missing comparable total remains explicit.
- Out of scope: final seat occupancy, cutoff scores, causal interpretation, current compliance, CPA workbook extraction, institutional contact and protected systems.
- Acceptance: each target year has a preserved literal record or bounded not-located outcome; every value states universe/category; hashes/provenance/locators verified; intermediate lot committed/pushed; no open agent-correctable defect.
- Risks: reports may expose only ratios or category fragments; these are not converted into totals.
- Validation: W026, W011, governance, repository, authored whitespace and LFS per lot; full suite/D09 at integration.
- Error log: `governance/errors/W026.md`.
- Human review: `governance/human-reviews/W011-p1-admin-procedure.md`; HR-W011-003 remains for matched final occupancy/cutoffs.
- Checkpoint contract: specification first; H1-H5 intermediate commits pushed before the next; one final primary review/integration.

