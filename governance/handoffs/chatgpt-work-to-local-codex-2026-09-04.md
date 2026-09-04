# Handoff — ChatGPT Work to Local Codex

Date: 2026-09-04.

## Repository and Git state

- Repository: `https://github.com/vinnses/ibm`
- Integration base: `origin/main` at `ad1ce16`
- Integrated work branch: `research/admin-data-2026` at `5b5423d`
- Administrative merge commit: `c242270`
- Source-integrity correction commit: `4421965`
- Governance branch commit: `af8437a`
- Governance merge commit: `d3ac930`
- Remote state: governance merged and `origin/main` synchronized; the later metadata-only commit containing these final remote SHAs may advance `main` again

Resolve the current remote state locally with:

```bash
git fetch --all --prune
git switch main
git pull --ff-only
git log --oneline --decorate --graph -20
python scripts/validate_repository.py
```

## Objective and verdict

Objective: consolidate completed ChatGPT Work branches into `main`, establish durable AI governance, and transfer an explicit roadmap to local Codex.

Verdict: complete, with the raw INEP preservation exception carried into roadmap P0.

## Deliverables

- Repository entry instructions: `AGENTS.md`
- Governance index and charter: `governance/README.md`, `governance/PROJECT.md`
- Work history: `governance/WORK_INDEX.md`
- Roadmap: `governance/ROADMAP.md`
- Durable decisions and agent routing: `governance/DECISIONS.md`, `governance/AGENT_OPERATIONS.md`
- Work, source, review, and handoff specifications: `governance/specs/`
- Dated consolidation audit: `governance/reviews/consolidation-2026-09-04.md`
- Reusable templates: `governance/templates/`
- Repository validator: `scripts/validate_repository.py`

## Sources added by the integrated administrative work

- UFPR Observatório pages and the institutional dropout report.
- UFPR/CEPE vacancy resolutions and NC selection-process sources.
- INEP trajectory dictionary, official MD5 manifests, source page, course extract, and reproducible scripts.
- Official UFPR contextual page for Edital nº 01/2026.

See `administracao/dados/fontes.csv` for 43 records and local manifests for Fichas.

## Coverage reached

- 2011 and 2023 formal curriculum structures are reconstructed.
- Primary resolutions and PPCs used for those structures are preserved.
- Initial 2023 Ficha coverage is inventoried and hashed.
- The 2026 call and feasibility proposal are preserved and separated from later administrative states.
- UFPR and INEP administrative series are documented with annual/cohort distinctions.
- Proposal claims have independent evidence statuses and methodological limits.

## Gaps

- Full 2011 component/Ficha/elective inventory.
- Full 2023 component/Ficha/elective/regulation inventory.
- Course creation/recognition acts, 2022 reform minutes/opinions, Enade/CPA/e-MEC evidence.
- Complete applicant counts, final occupancy, and comparable cutoff data.
- Apêndice A, memorandum, process identifier, deliberations, result, MEC decision, proposed matrix/PPC/Fichas, transition rules, and staffing guarantees.
- Repository preservation of the exact large INEP raw packages and spreadsheets used by W006.

## Divergences

- The 2026 proposal states 30 vacancies; the PS/UFPR 2026 edital lists 24 for that process only.
- UFPR/SIGA and INEP entrant totals differ in overlapping years and are preserved in parallel.
- The Observatório interface displayed 2026 values while its time selector ended in 2025.
- The Portal do Ementário still exposed the earlier 3,000-hour structure while the 2023 resolution establishes 3,200 hours.
- Several located Fichas predate the 2023 reform; their current applicability is not established automatically.

## Provisional information

- Public searches as of 2026-09-04 did not locate evidence that the 2026 proposal was selected, approved, authorized, or implemented.
- The 2026 Observatório row is retained with an interface-divergence warning.
- Some Ficha dates/terms and curriculum applicability remain indeterminate.

## Explicitly not performed

- No curricular quality judgment or recommendation.
- No 2011–2023 content comparison.
- No proposed 2,700-hour curriculum reconstruction because the matrix was not available.
- No inference that renaming or reducing workload changes demand, dropout, or completion.
- No deletion of historical work branches.

## Recommended first local work

Create a bounded P0 work unit to preserve the exact INEP raw inputs through Git LFS or another approved repository-backed mechanism. Do not begin curricular comparison until the documentary gates in `governance/ROADMAP.md` pass.
