# W033 — First 2011–2023 content taxonomy handoff

- Branch: `work/w033-first-content-taxonomy`.
- Commit base: `f8da2f441dd6a8a273a78842d6c42179d8c2711c`, the locally validated authorized W032 merge on `main`; remote `origin/main` could not be refreshed or published because SSH authentication remains unavailable.
- Commits produced before this handoff commit:
  - `bd6a56b` — define first content taxonomy work unit;
  - `2d7ca35` — build consolidated content corpus;
  - `f022fd2` — capture source-grounded topic proposals;
  - `eb95efa` — populate taxonomy occurrences and lineage candidates;
  - `fe828aa` — reconcile W033 taxonomy and lineage audit;
  - `2f188fa` — populate server-rendered taxonomy review routes;
  - `0168444` — normalize W033 audit metadata.
- Primary-session model and effort: GPT-5 family as exposed by the runtime; exact backend model and reasoning effort are not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary integration and three Terra subagents as detailed in the following table.

| Actor | Primary/subagent | Functional role | Model | Effort | Routing rationale |
|---|---|---|---|---|---|
| primary | primary | orchestration, corpus/build integration, taxonomy reconciliation, site implementation, final validation, and handoff | GPT-5 family; exact backend unknown | unknown | Primary-session authority retained complex integration and global synthesis. |
| taxonomy-2011 | subagent | documentary extraction and source-grounded 2011 topic proposals | GPT-5.6 Terra | medium | Contextual documentary investigation over a bounded 12-record corpus. |
| taxonomy-2023 | subagent | documentary extraction and source-grounded 2023 topic proposals | GPT-5.6 Terra | medium | Contextual documentary investigation over 40 preserved Fichas. |
| lineage-review | subagent | independent relation, ambiguity, split/merge, and qualitative-sample audit | GPT-5.6 Terra | high | Demanding cross-curriculum reconciliation and contradiction detection. |

- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none. No Sol subagent was created.
- Objective and completion verdict: the first source-grounded 2011–2023 taxonomy, occurrences, evidence mappings, and reviewable lineage candidates are implemented and validated. **W033 complete.**

## Deliverables and primary files

- Corpus: `site/data/source/w033/content-corpus.json` and `site/data/schema/content-corpus.schema.json`.
- Source proposals: `agent-2011-proposals.json` and `agent-2023-proposals.json` under `site/data/source/w033/`.
- Taxonomy source: `site/data/source/w033/taxonomy.json`.
- Split generated datasets under `site/data/generated/w033/`: `domains.json`, `topics.json`, `topic-occurrences.json`, `aliases.json`, `candidate-lineage-relations.json`, and `evidence-mappings.json`.
- Site model: `site/src/lib/data/generated/content-model.json`, validated by the extended W032 JSON Schema and matching TypeScript contracts.
- Builders/adapters: `scripts/build_w033_content_corpus.py`, `scripts/build_w033_agent_2023_proposals.py`, `scripts/build_w033_taxonomy.py`, and the extended `scripts/build_w032_site_data.py`.
- Validation: `scripts/validate_w033_taxonomy.py`, including schema/reference/state/hash/excerpt/uncertainty/relation/determinism checks.
- Method documentation: `docs/content-taxonomy.md` and updated `docs/content-model.md`.
- Review records: the two proposal reviews, independent lineage audit, and final acceptance review under `governance/reviews/`.

## Sources, coverage, and population

- Sources added to the W033 corpus: 52 existing preserved records, not new external downloads—12 on the 2011 investigation side and 40 on the 2023 side (23 Ficha 1 and 17 Ficha 2).
- Eligible extraction coverage: 49 records; 9 on the 2011 side covering 7 component instances, and all 40 on the 2023 side covering 24 component instances.
- Excluded but retained for audit: 3 historical Ficha 2 records whose evidence assigns them to Ciência da Computação rather than IBM/96A.
- Source-level proposals: 260 total; 68 from the 2011 investigation and 192 from 2023. Eighteen proposals from the three excluded sources produce no occurrences.
- Population: 18 domains, 156 topics, 242 topic occurrences, 3 aliases, 12 lineage candidates, 242 W033 evidence records, and no fixtures or claims.
- Review-state distribution: 18 domains, 156 topics, 242 occurrences, and 12 relations are all `proposed`.
- Evidence-strength distribution: all 242 occurrences and all 12 relations are `indeterminate` (254 analytical records).
- Relation distribution: 8 maintained, 1 fragmented, 1 merged, 1 new relative only to the bounded sparse corpus, 1 indeterminate, 0 expanded, 0 reduced, and 0 removed.
- Splits/merges detected: one proposed fragmentation candidate and one proposed merge candidate, both with multi-occurrence endpoints and explicit caveats.

Every occurrence resolves through evidence to one of 56 public-document
records: 52 W033 Ficha sources plus the 4 formal W032 curriculum documents.
The generated evidence layer totals 246 evidence records and 658 typed links.

## Site routes and document security

The W032 route families remain functional and are populated at `/curriculos`,
`/curriculos/[id]`, `/disciplinas/[id]`, `/conteudos`, `/conteudos/[id]`,
`/evidencias/[id]`, and `/documentos/[id]`, with preserved bytes at
`/documentos/[id]/arquivo`. `/conteudos` supports curriculum and domain
filters and exposes proposed candidates. The full model is imported only by
server modules, avoiding delivery of the evidence database as a client bundle.

Only manifest-resolving allowlist entries are copied. The builder enforces
approved repository prefixes, regular non-symlink files, SHA-256 equality,
unique generated paths, and an exact public tree. Request parameters are
document IDs, never filesystem paths. No repository tree, `.git`, `.env`,
secret, Tailscale runtime state, or Docker socket is exposed; W031 Compose
mount, network, non-root, read-only, and capability controls remain unchanged.

## Validation executed and results

- W033 corpus, taxonomy, and downstream W032 builders in `--check` mode: deterministic and current.
- W032 schema/semantic validator: 84 components, 54 dependencies, 56 documents, 18 domains, 156 topics, 242 occurrences, 12 relations, 246 evidence records, 658 links; negative invariant tests passed.
- W033 validator: 52 sources, 260 proposals, 242 eligible occurrences, 3 aliases, valid excerpts/references/applicability and 12 lineage candidates; pass.
- W018, W019, W020, W022, W023, W024, W025, and W030 historical/Ficha source validators: pass.
- `docker compose config --quiet`: pass.
- `docker compose build`: Svelte check 0 errors/0 warnings, adapter-node production build pass, production dependency audit 0 vulnerabilities.
- Disposable runtime: curriculum filters, domain filter, topic, discipline, evidence, and document pages returned 200; downloaded Ficha SHA-256 matched; unknown IDs and encoded traversal returned 404.
- W031 site bootstrap validator: 16 source/security checks, 0 errors.
- Repository validator: 223 CSVs, 126 preserved hashes, 277 Markdown links, 0 warnings/errors.
- Governance validator: 26 logs, 161 events, 4 human-review files, routing metadata valid, 0 errors.
- Git LFS integrity and `git diff --check`: pass.

## Gaps, divergences, and provisional information

- Documentary coverage is not curriculum-complete. A source attached to a code or year does not prove applicability to curriculum 96A or 2023; all generated occurrences retain that limitation.
- Three clearly other-course historical Ficha 2 sources remain visible in the corpus but cannot generate IBM occurrences.
- Domains and topic granularity are a first emergent reconciliation. Structured programming and linear structures deserve particular human review.
- The `new` candidate is only a bounded-corpus search result, not a historical assertion. The networks case is indeterminate rather than removed.
- An initial `reduced` recursion candidate was contradicted by CI1056 program text and removed after independent audit. This divergence is preserved in the audit and E-W033-009.
- No embeddings were used. All candidate scores are null; lexical overlap and qualitative reconciliation generate review candidates only.
- Remote divergence: local `main` contains the authorized W032 and W033 merges, while tracked `origin/main` remains stale because SSH fetch/push is unavailable. W033 is integrated locally but not published remotely.

## Audit closure and exclusions

- Error log: `governance/errors/W033.md`.
- Resolved events: E-W033-002 through E-W033-012; E-W033-008 moved from controlled `open` to resolved through its appended follow-up.
- Accepted exception: E-W033-001 (remote refresh unavailable; user-authorized local W032 integration used as base).
- Open event IDs: none.
- Human-review question path and gate consequence: no W033 human-review file was required; no completion gate depends on protected access, institutional authority, value judgment, or testimony. All analytical records remain explicitly proposed for later site-based human review.
- Explicitly unperformed: complete taxonomy, classification beyond available evidence, formal 2011→2023 continuity findings, unsupported removals, embeddings or semantic similarity at scale, 2026 proposal evaluation, advocacy or argument, political narrative, manifesto, storytelling, final visual design, remote publication, and any subsequent Work.
- Recommended next bounded work unit: human review and targeted documentary gap-filling may refine W033 before any use in a later 2026 analysis; it was not started.

## Integration update — 2026-09-08

- Merged branch: `work/w033-first-content-taxonomy` into local `main` after explicit user authorization.
- Merge commit: `d0566286207e3218ccc138aaa364365c3d0c5062` (`Merge W033 first content taxonomy`).
- Conflict resolution: none; the `ort` merge completed cleanly.
- Global indexes updated: none; W033 did not require a global documentary index update.
- Final validation: W031, W032, W033, repository, governance, Git LFS, Compose configuration/build, runtime health, route, document-hash, unknown-ID, and traversal checks passed after integration.
- Remote synchronization state: not synchronized. Local `main` is ahead of tracked `origin/main`; the previously recorded SSH authentication exception remains unresolved externally.
- Deployment state: the Compose `web` service was rebuilt from integrated `main`, recreated, and verified healthy on its configured loopback binding.

FIRST CONTENT TAXONOMY READY — 2011–2023 content model populated for site-based review.
