# W030 — final documentary gap audit

- Reviewer assignment (primary/subagent, model, effort, routing rationale): subagent, gpt-5.6-terra, medium, documentary evidence review.

Date: 2026-09-07. Scope: repository evidence review after W029 and during the
authorized CPA extraction. This audit did not contact an institution, download a
source, or conduct a public search. It does not adjudicate curricula, interpret
the proposal, or recommend an action.

## Method and status vocabulary

The review read `governance/REMAINING_DATA.md`, `ROADMAP.md`, `WORK_INDEX.md`,
the W028 release registers, source and dataset access catalogs, all eight human
review questions in the three human-review files, the W029 handoff and review,
the W029 extraction-family closure, and the underlying bounded search registers.
The row-level crosswalk is
[`W030-gap-classification.csv`](W030-gap-classification.csv).

`closed` means that the factual scope is sufficiently represented for this data
phase. `deferred_access` requires a custodian, protected system, or authorized
institutional record. `not_located_public_search_exhausted` records an exhausted
bounded public lane and does not claim nonexistence. `new_lead_required` means
that another public search is justified only by a specific new locator or
documentary clue. `out_of_scope_for_data_phase` identifies future analytical
work rather than a collection gap.

## Available factual coverage

### Curriculum 2011

The formal 2011 structure is available from the preserved resolution and PPC:
41 targets (37 coded components and four elective spaces), a 64-entry elective
catalog, 37 component/ementa records, seven dependency rows, and explicitly
recorded divergences. The W022-W024 public lane supplied per-code attempts for
all 37 coded components and preserved any located source separately. It did not
establish a Ficha version applicable to curriculum 96A, a complete historical
Ficha 2 set, or historically dated offering units. Those three facts remain
access-dependent (W030-G01 and W030-G02).

This audit found a correctable local-representation omission in W029's
eight-family closure: its statement that CI241 was the only preserved 2011
Ficha 1 is false for the current checkout. W022-W024 preserve 12 additional
PDFs: seven Ficha 1 records, four separate Ficha 2 records, and one
undesignated component document. They include 2011-dated Ficha 1s for CI055,
CI056, CI057, and CI244; a 2010/1 Ficha 2 naming Informática Biomédica for
CI056; Ficha 2s explicitly for Ciência da Computação; and later/indeterminate
records for BQ005, BQ054, and CE003. Their local manifests already preserve
the source URLs, hashes, document types, and limits. They were not included in
the shared 2011 inventory/ementa representation or the access-builder source
manifest list. This was an agent-actionable extraction and integration repair
(W030-G14 and W030-G15), not a new search. W030 completed it with twelve
document records, nineteen page-level raw-text representations, source-bound
normalized fields, regression checks for section boundaries, and deterministic
source-catalog integration. No applicability to curriculum 96A was inferred.

### Curriculum 2023

The formal 2023 structure is available from the preserved resolution, PPC,
component inventory (43 unique targets), 92 formal electives, 21 dependencies,
and stable regulations. Forty preserved Ficha records are separately structured
(23 Ficha 1 and 17 Ficha 2), without using matching codes as applicability
evidence. W025 completed 129 official-public attempts covering the 20
missing-Ficha and 23 applicability targets. Applicable Ficha 1 versions,
term/class-specific 2023-2026 Ficha 2 records, and an authoritative explanation
of the Ementario status remain access-dependent (W030-G03 through W030-G05).

### Administrative data

Structured public data include UFPR entrant, vacancy, candidate/vacancy, and
source-stated applicant observations; W026's historical applicant rows and
bounded search register; the INEP 2011-2020 trajectory row, cohort summary, and
annual series; transitions, evaluations, and complementary administrative
registers; and the W016 institutional reproduction/annex data. Annual, cohort,
course-total, category-specific, vacancy, entrant, and occupancy universes
remain separate.

The detailed original acts need a new lead (W030-G07). Detailed e-MEC/Enade
records and three aggregate applicant-count targets were not located after the
registered bounded public searches (W030-G08 and W030-G10). Matched final
occupancy/cutoff evidence requires institutional data (W030-G09). The CPA
workbook was the only formerly deferred local source. W030 extracted 132
literal course response rows from three source-labelled respondents across 44
answered questions, 85 uncombined response-frequency rows, the 47-row question
registry, five response-type/criterion rows, the course registry and the three
quantity rows. Its faithful intermediate represents 276,765 populated cells and
5,126 formulas, with formula text and stored-cache status separate (W030-G12).

`HN003` is closed rather than a remaining gap: it preserves W011's original
false-negative attempt, while the official SOC minute was subsequently
preserved as H009. The row remains in the access catalog as audit history
(W030-G17).

### Proposal 2026

The preserved Edital 01/2026, Apêndice B, and contextual page establish the
call, the existence of the proposal, and W029's literal machine-readable
proposal/call fields with page locators. The proposed 2,700-hour matrix,
component list, equivalences, PPC, staffing acts, process records, and all
post-proposal states are not established. They remain `deferred_access` because
the possible records are internal, protected, or unindexed (W030-G06). The
repository does not establish selection, approval, authorization, or
implementation.

## Final classification and actionability

The classification file consolidates the 33 access-catalog gap/search records
without treating repeated searches as separate missing documents. It additionally
captures W029's 21 precise searches, W026's year-specific applicant outcomes,
and the two residual partially structured families. It preserves original IDs,
provenance, rationale, actionability, and a concrete re-entry condition.

Two agent-actionable local tasks were found after W029: CPA extraction
(W030-G12) and normalization/indexing of the W022-W024 preserved 2011 sources
(W030-G14/G15). Both used only repository files; neither authorized a search.
Both are now validated and integrated in the deterministic catalogs. No other
uninvestigated factual task satisfies all five closure conditions:
relevance to the defined documentary base, resolution from current
files/tools/access, insufficient prior investigation, no
institutional/protected dependency, and no need for a new external lead. No
factual collection or extraction task remains agent-actionable.

The audit also checked the 13 blank `source_url` display cells and the 32
duplicate-metadata identity groups in `dados/acesso/source-records.csv`. The
blank cells are eleven INEP MD5 support sidecars, linked to preserved packages
with official URLs, and two user-provided proposal files whose provenance is
explicit in other manifests. The duplicate flags preserve raw manifest
differences and do not hide a missing fact. These are not a reason to begin a
new collection lane (W030-G16).

The following are explicitly outside this data phase: curricular comparison,
discipline-continuity inference, ementa similarity, lineage graphs, proposal
evaluation, argumentation, recommendations, visualization, and website work
(W030-G13). They must not be advanced under a gap-recovery label.

## Evidence consulted

- `governance/REMAINING_DATA.md`, `governance/ROADMAP.md`, and
  `governance/WORK_INDEX.md`.
- `dados/entrega-documental/STATUS_EXTRACAO.md`,
  `SOLICITACOES_E_LACUNAS.md`, `README.md`, and release/audit axis pages.
- `dados/acesso/datasets.csv`, `source-records.csv`, `gaps.csv`, and
  `COBERTURA_DOCUMENTAL.md`.
- `governance/human-reviews/W009-p1-curriculum-2011.md`,
  `W010-p1-curriculum-2023.md`, and `W011-p1-admin-procedure.md`.
- `governance/handoffs/W029-final-data-recovery.md`,
  `governance/reviews/W029-final-data-recovery.md`, and
  `dados/extracoes-w029/README.md`.
- The registered search logs cited in each CSV row.
