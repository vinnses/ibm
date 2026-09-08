# W032 — Content model infrastructure review

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary session / implementation and acceptance audit / GPT-5 family, exact backend unknown / effort unknown / no subagent was requested or used; the primary checked generated artifacts, mutated negative cases, the container build, and the running routes directly against the Work criteria.

## Verdict

**Approved for bounded W032 completion.** The content/evidence infrastructure,
public-document path, and review surface are functional. No substantive
taxonomy, occurrence classification, or curricular lineage was produced.

## Acceptance review

| Criterion | Observed evidence | Result |
|---|---|---|
| Historical unit is content, not abstract discipline | curriculum-specific component IDs; analytical topic/occurrence schema; no cross-curriculum discipline entity | pass |
| Factual/analytical separation | distinct top-level JSON layers and TypeScript interfaces; analytical records reference but cannot replace facts | pass |
| Required entities | 2 curricula, 84 component instances, domain/topic/occurrence/relation schemas, 54 component dependencies | pass |
| Occurrence semantics | independent textual evidence, evidence IDs, locator, evidence strength, notes, and review state | pass |
| Evolution semantics | change type and evidence strength are separate enums; no automatic derivation exists | pass |
| Review states | proposed/reviewed/contested/indeterminate accepted; proposed badge visible | pass |
| Evidence as structural entity | 4 evidence records, generic typed links, 4 canonical document records, and future typed claim support | pass |
| Existing metadata reuse | allowlist resolves exact rows from existing 2011/2023 manifests; canonical metadata lives on document records | pass |
| Deterministic data | byte comparison against temporary rebuild passed | pass |
| Explicit schema | JSON Schema plus dependency-free evaluator and referential validator passed | pass |
| Invalid data detection | mutated orphan, duplicate, invalid state, missing origin, and traversal cases were rejected | pass |
| Public document safety | exact four-file allowlist; repository-prefix, regular-file, symlink, SHA-256, and exact-tree checks passed | pass |
| Requested routes | all seven requested route families returned HTTP 200 for known IDs and 404 for unknown IDs | pass |
| Preserved copy | document endpoint returned bytes matching the source resolution SHA-256 | pass |
| W031 security guarantees | W031 validator passed with zero errors; web Compose mounts/networks/privileges remain unchanged | pass |
| Application build | pinned Docker build ran Svelte check with 0 errors/warnings, adapter-node build, and production prune | pass |
| Dependency audit | full development dependency image reported 0 vulnerabilities | pass |
| Repository governance | repository validator 0 warnings/errors; governance validator 0 errors; diff check clean | pass |

## Public-set audit

The only files copied into the web public tree are the 2011 Resolution 34/2010
and PPC, and the 2023 Resolution 75/22 and PPC. All four are public curricular
sources already preserved and manifested by the repository. The validator
found exactly four tracked files and no `.git`, `.env`, Tailscale, socket, or
secret-shaped path. Runtime routing uses a known document ID and a generated
asset path; user input never becomes a filesystem path.

## Documentary and analytical limits

- The 84 factual records reproduce the existing bounded component inventories;
  W032 did not adjudicate their already recorded gaps or applicability limits.
- One synthetic domain and topic test the proposed-state interface. Both are
  prefixed `fixture-`, marked `is_fixture`, visibly warned, and have no
  occurrence in a historical discipline.
- Topic occurrences, evolution relations, and claims are empty. W033 may
  populate taxonomy under its own evidence and review method.
- The public set is deliberately minimal, not an assertion that other
  repository sources are private or unsuitable. Adding one requires a new
  audited allowlist entry.
- Host npm was unavailable; the pinned W031 Docker toolchain supplied the
  successful Svelte and audit environment.
- The initial remote fetch failed for SSH authentication. The branch base is
  the identical locally tracked `main`/`origin/main` W031 merge SHA; remote
  freshness beyond that ref remains E-W032-001's accepted exception.

## Scope review

No full taxonomy, mass classification, 2011→2023 comparison, semantic
similarity, 2026 proposal evaluation, narrative, protest, final design,
database, merge, or W033 work was performed.
