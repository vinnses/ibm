# Release validation record

- Release Work: W028.
- Baseline audited independently: `e0c7a21d503efbff18264ead057c1b0250c2c80a`.
- N5 verdict: `approved with documented exceptions`.
- Indexed coverage: 204 datasets, 191 source-manifest records, 33 gap/search records.
- N2-N4 audit: 142 local links, 32 marked duplicate-identity groups, Ficha 1/Ficha 2 separation and statistical-universe boundaries checked.
- Accepted exceptions: 13 source records without a URL, unresolved access/search gaps, CPA extraction dependent on mandated tooling, and unadjudicated metadata differences.

## Required checks

The W028 branch closure runs the W015/W027 deterministic checks, the release manifest builder/checker, all repository validators, Git whitespace validation and Git LFS integrity. The integration milestone repeats release, governance, repository, whitespace and LFS checks.

Clean-checkout verification passed from GitHub commit `5336b3791d6221381a9f9203b502ee27231787da`: Git LFS materialized successfully; W015/W027/W028 deterministic checks, governance audit, repository validation, whitespace and LFS integrity passed; the clone remained clean and equal to `origin/main`. The containing final metadata commit is tagged `documentary-release-2026-09-06`. This file makes no claim that protected or not-located evidence was recovered.
