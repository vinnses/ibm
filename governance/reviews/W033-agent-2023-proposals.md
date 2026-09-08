# W033 agent review — 2023 source-level topic proposals

## Scope and result

This bounded review processed the complete declared 2023 usable Ficha corpus:
23 preserved **Ficha 1** records and 17 preserved **Ficha 2** records (40
documents total). It produced 192 source-grounded, intermediate-granularity
topic proposals in
`site/data/source/w033/agent-2023-proposals.json` (116 from Ficha 1 and 76
from Ficha 2). The companion deterministic construction script is
`scripts/build_w033_agent_2023_proposals.py`.

The dataset is an intermediate subagent deliverable, not a claim that the
proposed labels are reviewed taxonomy entries or that a document applies to
the 2023 curriculum.

## Sources and coverage

Inputs were the normalized, preserved-source datasets, in their existing
document order:

- W018 Ficha 1: `dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv`
  (5 records);
- W019 Ficha 1: `dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv`
  (5 records);
- W020 remaining Ficha 1:
  `dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv`
  (13 records);
- W020 Ficha 2:
  `dados/curriculos/2023/fichas-preservadas/fichas-2.csv` (17 records).

Every source record is separately represented with its document ID, type,
component code/name, local path, SHA-256, original URL and source locator.
Every proposal contains an exact excerpt from its own source's normalized
ementa; Ficha 2 wording variants are retained rather than silently copied
from a same-code Ficha 1. No topic was proposed from a component name alone.

The proposed broad-domain labels are organizational suggestions only. They
emerge from the available source text and are not an official curriculum
taxonomy.

## Applicability and ambiguity

All 40 source records state `applicability_2023: indeterminado`; all 192
proposals consequently use `epistemic_state: indeterminate` and
`review_state: proposed`. This includes documents whose title/code matches a
2023 component. The source records do not establish that matching as
curricular applicability.

Specific coverage limits retained in the output:

- Ficha 1 is permanent-content evidence but most preserved copies predate the
  2023 reform; their applicability is not upgraded.
- Ficha 2 is offering-specific and remains separate from Ficha 1. The MN129
  record identifies term `2022.1`, so it is especially not evidence of a 2023
  offering.
- The BF114 Ficha 1 bears 2024 electronic signatures and is still marked
  indeterminate, not retrospectively applied to 2023.
- CI1162 is represented only by its preserved Ficha 1 in this corpus; the
  absence of a Ficha 2 here does not imply absence of content or offering.
- Source breadth differs substantially: CI1062 supports only a generic
  paradigms proposal, while BQ083 and BF114 support multiple more specific
  candidates. Granularity should be reconciled during central taxonomy review.

## Candidate normalization/merge questions

No automatic merge was performed. Repeated labels across distinct documents
are retained as separate source proposals and are candidates for one shared
`ContentTopic` only after W033 integration review. The clearest candidate
groups are:

- the same-code Ficha 1/Ficha 2 pairs for CI1001, CI1002, CI1005, CI1007,
  CI1055–CI1057, CI1062, CI1068, CI1163, CI1171, CI1209, CI1212, CI1215,
  CI1218, CI1221 and CI1316; these are parallel evidence records, not proof
  that the versions are interchangeable;
- `processos de software` in CI1162 and CI1221, which may be one topic but
  has distinct local framing (requirements versus general engineering);
- testing-related material in CI1055, CI1005 and CI1002, which could be
  separated into program testing, software testing, and verification/
  validation rather than prematurely collapsed;
- performance-related material in CI1212 and CI1316, which is likely
  context-dependent (computer architecture versus parallel programs);
- database terminology in CI1218 and BQ083, which should retain the
  distinction between general database systems and biological databases.

The only alias proposed in this bounded dataset is `SGBD` for `sistemas
gerenciadores de bancos de dados`, because CI1218 itself explicitly gives the
abbreviation in parentheses. No lexical-only aliases were added.

## Mechanical verification

The builder was run and a post-generation check confirmed:

- 40 source entries: 23 Ficha 1 and 17 Ficha 2;
- 192 proposals;
- every quoted supporting excerpt occurs in its identified source's normalized
  ementa/program text;
- all entries retain `indeterminado` applicability;
- no cross-curriculum lineage candidate, 2026 claim, or continuity assertion
  was created by this subtask.

## Handoff to W033 integration

The primary should consume this file as source-level candidates, stabilize
topic/domain IDs centrally, and attach them to W032 component instances only
after retaining the source applicability limitation in evidence and occurrence
notes. The output intentionally does not create occurrence IDs, aliases beyond
the explicit SGBD form, cross-curriculum relations, or reviewed conclusions.
