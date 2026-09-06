# Documentary audit and freeze

Checkpoint N5 of W028. This is an independent documentary audit of the existing release inputs and N2--N4 package outputs. It freezes an auditable repository state; it neither adds evidence nor resolves the historical meaning of a divergence.

## Audited baseline

- **Commit:** `e0c7a21d503efbff18264ead057c1b0250c2c80a` (`Complete N4 gap crosswalk and error audit`)
- **Branch:** `work/w028-documentary-release`
- **Audit date:** 2026-09-06 (America/Sao_Paulo)
- **Excluded untracked files:** `scripts/build_w028_release_manifest.py` and `scripts/validate_w028_documentary_release.py` were read as future N6 tooling, but were not edited and are not part of this N5 baseline.

## Scope and method

The audit independently checked the three W015 access catalogs, their originating manifests/search and human-review inputs, the W027 generated coverage view, and all N2--N4 Markdown outputs. It recalculated every indexed dataset and preserved-source SHA-256, checked indexed dataset row counts, verified origin reconstruction through the W015 checker, parsed CSV schemas and required fields, and resolved every local link authored by N2--N4.

It also checked duplicate identity markers, Ficha document-type separation, the administrative axis's explicit universe boundaries, and the N4 crosswalk against every access-catalog gap ID. The audit did not modify originals, manifests, CSV datasets, indexes, or the untracked W028 scripts.

## Findings

| Check | Result |
| --- | --- |
| Indexed datasets | 204 paths, SHA-256 values and declared row counts verified |
| Preserved source records | 191 paths and SHA-256 values verified; source-record rows reconstruct from their recorded origin manifests |
| Source provenance fields | 191 local paths and hashes recorded; 178 records include a source URL |
| Schemas | Access catalogs and indexed CSVs have consistent parsed structure and required catalog fields |
| Duplicate/conflict handling | 32 duplicate identity groups containing 66 rows; all carry a consistent `duplicate-origin` or `metadata-differences-not-adjudicated` marker |
| Ficha boundaries | 24 Ficha 1 records and 17 Ficha 2 records; no shared local path between the two document types |
| Statistical-universe boundaries | N2 administrative navigation explicitly retains annual/cumulative, course-total/category-specific, vacancy/entrant, and occupancy boundaries; no derived final-occupancy claim is introduced |
| N2--N4 navigation | 142 local Markdown links in the six package documents resolve in this checkout |
| N4 gap routing | All 33 `dados/acesso/gaps.csv` IDs occur in the explicit N4 crosswalk and have a documented route |
| Deterministic/package checks | W015 access package, W027 coverage build/check, W027 validator, W011 validator, repository validator, authored whitespace check, and Git LFS integrity check passed |

The repeated source identities remain separate records. Their metadata differences are visible in `dados/acesso/source-records.csv`; this audit records that they are marked and preserved, not that their documentary content is equivalent.

## Accepted documentary exceptions

- Thirteen preserved-source records have no recorded source URL. Their local path and SHA-256 are present, but the absent URL remains a provenance limitation rather than being synthesized here.
- The 33 gap/search records remain unresolved documentary states where the underlying evidence requires protected/human access or a bounded public search did not locate it. Each is explicitly routed in `SOLICITACOES_E_LACUNAS.md`; `not located` is not nonexistence.
- Applicable historical Fichas, term/class-specific Ficha 2 records, historical offering-unit confirmation, original acts, matched final-occupancy/cutoff definitions, CPA workbook extraction in the mandated runtime, and post-proposal 2026 acts remain subject to their recorded boundaries and routes.
- Duplicate source identities and any metadata differences remain unadjudicated unless a source-specific work supplies documentary grounds to reconcile them.

These exceptions are documented and machine- or human-readable in the existing catalogs and request register. No open agent-correctable material defect was found in the N5 audit scope.

## No-analysis boundary

This freeze establishes only file identity, preservation, navigation, catalog correspondence, schema consistency, version/document-type separation, stated statistical-universe boundaries, and explicit routing of gaps. It does not compare curricula, decide applicability, infer continuity, adjudicate documentary conflicts, evaluate the 2026 proposal, assess current practice, or make recommendations.

## Verdict

**approved with documented exceptions**

The baseline above is suitable to proceed to N6 documentary-release packaging. The accepted exceptions constrain claims exactly as recorded; they do not authorize their silent completion or analytical use.
