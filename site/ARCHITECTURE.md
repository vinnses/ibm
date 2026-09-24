# Public site architecture

Status: W045 contract updated for W046's bounded Dash example, 2026-09-24.
The first `/analises/` question is implemented; additional analyses remain
future work and require their own validated public data slices.

## Product boundary

The public site is an independent, academic-style evidence interface. Its
primary tasks are to inspect the 2011 and 2023 curricula, open original public
documents, and eventually answer explicit analytical questions with inspectable
data. It must not publish research-workflow metadata, turn absent documents into
claims of nonexistence, or treat analytical visualizations as institutional
facts. Factual observations, inference, interpretation, and normative proposals
remain separate layers.

| Public surface | Owner | Current / future responsibility |
| --- | --- | --- |
| `/`, `/curriculos/...`, `/disciplinas/...` | SvelteKit | Curriculum and component browsing, with restrained source and Ficha status. |
| `/documentos`, `/documentos/{id}` | SvelteKit | Catalogue and human-readable record for approved public documents. |
| `/documentos/{id}/arquivo` | SvelteKit | Stable original-file link; no public repository path is exposed. |
| `/metodologia` | SvelteKit | Reader-facing source and uncertainty conventions. |
| `/analises/...` | Dash | Question-led filters, plots, tables, download of the exact public data slice, and source/method links. The first example counts formal coded components by recommended period. |

W046 adds a small NGINX HTTP router in the existing Docker `edge` network;
Tailscale Funnel still has one root handler, now aimed at that router:

```text
public HTTPS / Tailscale Funnel
    -> internal HTTP router
       -> /analises/* : Dash Python service
       -> all other paths : SvelteKit service
```

The router preserves `/analises/` when proxying to Dash. This matters because
Dash assets and callback URLs use the same prefix. The official server-backend
guide documents a mounted application prefix (preserved copy:
`architecture/sources/dash-server-backends.html`). The Tailscale configuration
and sources are under `../infrastructure/tailscale/`; router config and official
NGINX references are under `../infrastructure/router/`.
Do not expose Dash or the code-server development service as separate public
ports. Preserve the existing code-server authentication/network boundary.

## Evidence-to-publication pipeline

```text
unchanged source originals + source manifest/hash
    -> versioned transcription / normalized tables
    -> validated, explicitly approved public data release
       -> SvelteKit documentary read model
       -> Dash pandas/Arrow read model
```

The repository is the source of truth. Neither frontend edits original
evidence. A release identifier and source-table hashes must travel with both
published read models so a chart and a document page can be reconciled to the
same snapshot. Generate both from one validated release; do not maintain
duplicate hand-edited values in TypeScript and Python. CSV is sufficient for
small, inspectable tables; Parquet/Arrow may be used for larger typed tables.
The technical data pipeline belongs outside either UI service.

Every public document needs a stable ID, title, issuer, document type, date or
explicitly unknown date, version/applicability, original-source URL when
available, preserved original path and SHA-256 in the internal manifest, a
publication decision, and explicit relationships to the curricula/observations
it supports. The public page shows only reader-useful metadata and the original
file. Ficha 1, Ficha 2, resolutions, PPCs, calls, rules, minutes, and other
document classes remain distinguishable. A new document class extends the
catalogue without requiring a new top-level page.

Private correspondence and conversations are **not** imported into the public
catalogue by default. Publication needs an explicit human review of authority,
consent, personal data, redaction, and evidentiary role; a conversation can be
testimony or a lead without becoming an institutional fact. Proposed or
unapproved material is never silently relabeled as an implemented rule.

## Analysis contract for the first Dash slice

An analysis is built around a stated question, not a persuasive essay. Its
record must identify the data-release version, observation unit, population,
period, denominator, inclusion/exclusion rules, transformation code, source
links, uncertainty, and known comparability limits. The page should present
filters, a chart, a corresponding table, and a downloadable filtered slice.
Annual snapshots must not be merged with cumulative cohort indicators.
Formal curriculum versions must not be joined by title similarity alone.

W046's first slice asks about formal coded components by recommended period.
Its source-to-chart path is documented in `../analises/README.md`; this is a
descriptive example, not a normative comparison. Future analyses must reuse
the contract with their own validated data releases.

## Delivery order and safeguards

1. Keep the existing public SvelteKit service and document routes healthy.
2. Define and validate one public analytical data release from preserved tables.
3. Implement one Dash question locally under `/analises/`, including method,
   table, source links, accessibility and empty/error states.
4. Add the internal router and Dash container. Test root, documents, PDFs,
   Dash assets/callbacks, health checks and mobile layout before changing Funnel.
5. Switch Funnel from the web container to the router only after rollback is
   prepared; verify that the public origin still exposes only intended routes.

W045 covered only the first item and the contract. W046 implements and tests
the first analysis and deploys the router/Dash service as a separate bounded
work unit; additional analyses are not authorized by this example alone.
