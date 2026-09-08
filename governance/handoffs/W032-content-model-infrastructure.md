# W032 — Content model infrastructure handoff

- Branch: `work/w032-content-model-infrastructure`.
- Commit base: `33c4fbda51b56de8110a19478908afb0ffa25fdd` (locally identical `main` and tracked `origin/main`, W031 merge).
- Commits produced before this closure commit:
  - `f388bf7` — define W032 and record the remote-refresh exception;
  - `8b92790` — add deterministic factual/analytical/evidence model and public-document set;
  - `c7e96d9` — add the requested SvelteKit review routes;
  - `c7b1d9e` — document architecture and harden schema validation.
- Primary-session model and effort: GPT-5 family as exposed by the runtime; exact backend and effort are not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary / primary / orchestration, architecture, implementation, validation, review, and handoff / GPT-5 family, exact backend unknown / effort unknown / actual / the bounded Work and final audit remained in the user-supervised primary session; no subagent was requested or used.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none.
- Objective and completion verdict: the static content/evidence model, SvelteKit review routes, deterministic generation, validation, and allowlisted preserved-document access are implemented. **W032 complete.**

## Model, schemas, and generated data

- `site/data/schema/content-model.schema.json`: JSON Schema 2020-12 for curricula, curriculum-specific component instances, group-capable dependencies, documents, content domains/topics, occurrences, evolution relations, claims, evidence, and typed evidence links.
- `site/src/lib/model.ts`: matching SvelteKit TypeScript contracts.
- `site/data/source/public-documents.json`: auditable four-document publication allowlist.
- `site/data/source/analytical-fixtures.json`: one conspicuously synthetic domain/topic pair; no historical occurrence.
- `scripts/build_w032_site_data.py`: manifest adapter, curriculum inventory builder, deterministic sorter, hash-verifying document copier, and stale-output check.
- `site/src/lib/data/generated/content-model.json`: 2 curricula, 84 component instances (41 from 2011, 43 from 2023), 54 dependency rules, 4 documents, 4 evidence records, 142 evidence links, 1 fixture domain, 1 fixture topic, and zero occurrences, evolution relations, or claims.
- `scripts/validate_w032_content_model.py`: dependency-free schema evaluation plus semantic/reference/file checks and negative mutation tests.

The factual layer retains each curriculum as a historical unit and each
component as a curriculum-specific instance. The analytical layer is separate.
`TopicOccurrence` is the future content-to-component association and carries
evidence text, exact locator, epistemic strength, notes, and review state.
`EvolutionRelation.change_type` is independent of `evidence_strength`.

## Routes and review interface

- `/curriculos`
- `/curriculos/[id]`
- `/disciplinas/[id]`
- `/conteudos`
- `/conteudos/[id]`
- `/evidencias/[id]`
- `/documentos/[id]`, with `/documentos/[id]/arquivo` for the preserved copy

The plain interface lists curricula and disciplines, displays evidence and
review/documentary states, leaves proposed analysis visible, and carries a
prominent fixture warning. Known routes passed runtime checks; unknown IDs and
an encoded traversal attempt returned 404.

## Documents served and security

Generated public files are limited to:

- 2011 Resolução nº 34/2010-CEPE;
- 2011 PPC;
- 2023 Resolução nº 75/22-CEPE;
- 2023 PPC.

Every copy is resolved from an existing manifest, restricted to a declared
repository prefix, required to be a regular non-symlink file, and verified
against the recorded SHA-256 before copying. The runtime document endpoint
looks up only a known ID and redirects to its generated static asset. The exact
public tree is validated; the repository, `.git`, `.env`, secrets, Tailscale
state, and Docker socket are absent. W031 Compose security controls remain
unchanged: no repository/web mount, no Docker socket, no added Tailscale data,
read-only non-root web runtime, dropped capabilities, and segmented networks.

## Validation executed

- deterministic builder write and `--check`: pass;
- explicit schema evaluation, ID/reference/state/origin/hash/public-tree checks: pass;
- negative orphan, invalid state, duplicate ID, missing origin, and traversal tests: pass;
- Docker Svelte check: 0 errors and 0 warnings;
- Docker adapter-node production build: pass;
- full development dependency audit: 0 vulnerabilities;
- `docker compose config --quiet`: pass;
- `docker compose build`: pass;
- disposable runtime checks for all requested routes, fixture label, exact served-document SHA-256, unknown IDs, and traversal: pass;
- `python scripts/validate_w031_site_bootstrap.py`: 16 sources, 0 errors;
- `python scripts/validate_repository.py`: 223 CSVs, 126 hashes, 276 Markdown links, 0 warnings/errors;
- `python scripts/validate_governance_audit.py`: 25 logs, 149 events, routing records valid, 0 errors at pre-handoff run;
- tracked public-path audit and `git diff --check`: pass.

## Limits, fixtures, and exclusions

- Fixture: `fixture-domain-review` and `fixture-topic-review`, synthetic and not connected to historical facts.
- Limitation: the public allowlist is a deliberately audited minimum, not the complete repository source collection.
- Limitation: existing inventory uncertainty is preserved; W032 does not upgrade Ficha applicability or resolve documentary conflicts.
- Limitation: host npm is absent; the pinned Docker build/audit path passed.
- Accepted exception: E-W032-001; SSH prevented a new remote fetch, while local `main` and tracked `origin/main` were identical at the W031 merge base.
- Error log: `governance/errors/W032.md`; resolved events E-W032-002 through E-W032-009 remain preserved; open event IDs: none; accepted-exception event: E-W032-001.
- Human review: no W032 human-review question file was required and no acceptance gate depends on protected access or value judgment.
- Explicitly unperformed: substantive taxonomy, mass classification, content lineage, 2011→2023 comparison, semantic similarity, 2026 proposal evaluation, storytelling, protest, final design, database, merge, remote publication, and W033.
- Recommended next bounded Work: W033 may populate the initial content taxonomy and provenance under separate authorization. It was not started.

CONTENT MODEL READY — infrastructure prepared for taxonomy and lineage population.
