# W011 handoff — administrative and procedural history

- **Branch:** `work/w011-p1-admin-procedure`
- **Commit base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Commits produced:** `8565b6d` (`research: register W011 administrative evidence`); `b65d57f` (`test: validate W011 administrative register`); `41cd390` (`docs: hand off W011 administrative procedure`); `ae67c19` (`fix: preserve 2022 CEPE reform minute`); final corrective documentation commit pending this handoff update.
- **Objective and completion verdict:** **corrected for the bounded public-source scope; awaiting independent repeat review.** Every W011 transition/evidence front is tied to a preserved evidence record or a dated bounded search record. This is not a finding that unresolved acts or records do not exist.

## Deliverables and coverage

- `administracao/historico/transicoes.csv` records the authorization and recognition as reported by the official UFPR registry; the 2022 reform approval by the preserved primary CEPE resolution and the separately preserved 2 December 2022 first-Chamber minute; and all five 2026 stages separately. Only `proposal` is proven for the 2026 reorganization.
- `administracao/historico/avaliacoes.csv` separates the undated registry-displayed MEC concept, the CPA 2022 response workbook, the existing INEP cohort trajectory front, and the not-located Enade/e-MEC detailed-record fronts.
- `administracao/historico/series-complementares.csv` registers only source-stated universes: the 2009–2018 cohort dropout measure, a 2016 applicant-count observation, and PS/UFPR-2026 vacancies. Final occupancy and comparable cutoff scores remain not located. No values were estimated or combined across unmatched universes.
- `administracao/historico/buscas-negativas.csv` records 11 dated official-domain/system searches. HN003 is retained as an auditable search record but its false-negative result is explicitly superseded by preserved source H009; it no longer claims the 2022 minute/opinion was absent.
- `administracao/historico/fontes/manifesto.csv` is the local provenance and SHA-256 manifest. New preserved originals are the official Ementário course page, CPA 2022 index page, and CPA course workbook. Existing repository-preserved primary sources are referenced by their stable paths and hashes.
- `scripts/validate_w011_admin_procedure.py` validates source hashes, transition stages, and source/negative-search references.

## Sources added

- UFPR Ementário course entry 96A (HTML): identifies Resolução 19/10-COUN as authorization, Portaria 44 (22 Jan. 2015) as recognition, and displays a MEC concept of 4 without its evaluation date/instrument.
- UFPR CPA 2022 results page (HTML) and its linked original `informatica-biomedica.xlsx`. The workbook is kept unchanged and not aggregated because its published form does not state a response denominator, field period, or aggregation rule.
- UFPR/SOC, [Ata da Sessão Ordinária da 1ª Câmara do CEPE, 2 Dec. 2022](../../administracao/historico/fontes/documentos/ata-1a-camara-cepe-2022-12-02.pdf), SHA-256 `461fd8121be84c13d53c6d77a0dcc0d11500ee84a295b08a3e8c86df914b8faf`: records the favorable opinion and unanimous approval for the 2022 Informática Biomédica reform, process `061269/2022-16`.

## Validations executed

- `python scripts/validate_w011_admin_procedure.py` — passed after correction: 10 source hashes, 9 transitions, 11 search records; 0 errors.
- `python scripts/validate_repository.py` — passed: 16 CSV files, 126 preserved hashes, 88 Markdown links; 0 warnings, 0 errors.
- `git diff --check` — passed.
- CSV width audit — passed for all five W011 CSV files.

## Gaps, divergences, and provisional information

- The original texts of Resolução 19/10-COUN and Portaria 44 were not located. The official registry attribution is preserved, but it is not a substitute copy of either underlying act.
- The 2 December 2022 first-Chamber minute and favorable opinion are now preserved as H009/TR003A. The original false negative is retained and resolved as `E-W011-001`; no claim extends this 2022 deliberation to the separate 2026 proposal.
- No public Apêndice A, forwarding memorandum, SEI identifier, NDE/Colegiado/Setor decision, PROGRAP/PROPLAD individual result, UFPR submission, MEC decision, 2,700-hour matrix, component list, equivalence table, PPC/minutes, or staffing-guarantee act was located. Some may be protected or unindexed; no protected system was accessed.
- No official course-specific Enade result with a dated instrument/value and no preservable detailed public e-MEC record was located. The Ementário’s displayed `Conceito MEC 4` is deliberately not labeled Enade, CPC, or a dated metric.
- No matched-universe final-occupancy outcome or comparable cutoff-score series was located. The 2016 applicant count, 2026 PS-only vacancies, annual observations, and cohort indicators remain distinct.
- The Apêndice B origin is recorded as user-provided, consistent with the existing global catalog. It proves a proposal document only, not its submission or approval.

## Explicitly unperformed work

- No curricular quality evaluation, matrix reconstruction, applicant/occupancy estimation, or proposal-status inference was performed.
- No global catalog/index, `ROADMAP.md`, or integration/review file was changed.
- No protected SEI/e-MEC system was accessed and no self-approval or merge was performed.

## Error log and human-review questions

- **Error log:** `governance/errors/W011.md`; resolved event: `E-W011-001` (false negative for the 2 December 2022 CEPE minute). No W011 error event remains open in this corrective handoff.
- **Human-review questions:** `governance/human-reviews/W011-p1-admin-procedure.md`; pending `HR-W011-001` (protected 2026 process), `HR-W011-002` (original creation/recognition acts), and `HR-W011-003` (matched occupancy/cutoff data). Their gate consequences remain as recorded: they do not authorize claims beyond preserved evidence.

## Recommended next bounded work unit

Independent repeat cross-review should first verify the H009/TR003A correction and closure of `E-W011-001`. Separately, an authorized access-and-records request may target the protected/unindexed 2026 UFPR procedural file (especially memorando, SEI identifier, and NDE/Colegiado/Setor records) and original authorization/recognition acts. It must preserve newly obtained records before reassessing any transition status.
