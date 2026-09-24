# Public site architecture

Status: W045 architecture contract, 2026-09-24. This describes the intended
boundary between documentary browsing and future analysis. It does **not**
claim that a Dash service or the analysis routes are implemented.

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
| `/analises/...` | Dash (future) | Question-led filters, plots, tables, download of the exact public data slice, and source/method links. No empty route is published until a complete first analysis exists. |

The current Tailscale Funnel routes `/` to SvelteKit only. A later deployment
can introduce a small HTTP reverse proxy in the existing Docker `edge` network:

```text
public HTTPS / Tailscale Funnel
    -> internal HTTP router
       -> /analises/* : Dash Python service
       -> all other paths : SvelteKit service
```

The router should preserve the `/analises/` prefix; configure Dash with a
matching route/request prefix and test its callback and asset URLs through the
public origin before enabling the route. Dash's official server-backend guide
documents a mounted application prefix (preserved copy:
`architecture/sources/dash-server-backends.html`). The existing Tailscale
Funnel configuration and source capture are under `../infrastructure/tailscale/`.
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

The first Dash work should choose **one** reproducible question and test the
full source-to-chart path. Dashboard framework setup alone is not a useful
public deliverable. Future analyses can then reuse the validated contract.

## Delivery order and safeguards

1. Keep the existing public SvelteKit service and document routes healthy.
2. Define and validate one public analytical data release from preserved tables.
3. Implement one Dash question locally under `/analises/`, including method,
   table, source links, accessibility and empty/error states.
4. Add the internal router and Dash container. Test root, documents, PDFs,
   Dash assets/callbacks, health checks and mobile layout before changing Funnel.
5. Switch Funnel from the web container to the router only after rollback is
   prepared; verify that the public origin still exposes only intended routes.

W045 covers only the first item and this contract. No public service is changed
by this work. A later deployment is a separate bounded, reviewed work unit.
