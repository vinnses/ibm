# Release validation record

## W030 refresh

- Current indexed coverage: 217 CSV datasets, 212 source-manifest records and 33 retained historical gap/search records.
- CPA: 19 worksheets, 276,765 populated cells, 5,126 formulas, 132 literal course observations, 44 answered questions, 85 frequency rows and three source-labelled respondents; deterministic regeneration passed with pinned openpyxl 3.1.5.
- Historical local repair: twelve W022-W024 PDFs and nineteen pages validated against seven manifests, with section-boundary regression checks.
- Final gap audit: 17 grouped classifications cover all 33 access-catalog IDs; no remaining row is agent-actionable.
- W028 counts and exceptions below are preserved as their dated historical baseline. The former CPA tooling exception is resolved by W030.

- Release Work: W028.
- Baseline audited independently: `e0c7a21d503efbff18264ead057c1b0250c2c80a`.
- N5 verdict: `approved with documented exceptions`.
- Indexed coverage: 204 datasets, 191 source-manifest records, 33 gap/search records.
- N2-N4 audit: 142 local links, 32 marked duplicate-identity groups, Ficha 1/Ficha 2 separation and statistical-universe boundaries checked.
- Accepted exceptions: 13 source records without a URL, unresolved access/search gaps, CPA extraction dependent on mandated tooling, and unadjudicated metadata differences.

## Required checks

The W028 branch closure runs the W015/W027 deterministic checks, the release manifest builder/checker, all repository validators, Git whitespace validation and Git LFS integrity. The integration milestone repeats release, governance, repository, whitespace and LFS checks.

Clean-checkout verification passed from GitHub commit `5336b3791d6221381a9f9203b502ee27231787da`: Git LFS materialized successfully; W015/W027/W028 deterministic checks, governance audit, repository validation, whitespace and LFS integrity passed; the clone remained clean and equal to `origin/main`. The containing final metadata commit is tagged `documentary-release-2026-09-06`. This file makes no claim that protected or not-located evidence was recovered.
