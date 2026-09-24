# W045 — Site architecture alignment for documents and future Dash analysis

- **Objective:** Establish a coherent public-site architecture for documentary navigation and a future Dash analysis service, and make the existing SvelteKit shell support a document catalogue without publishing empty analysis views.
- **Branch:** `work/w045-site-architecture`.
- **Commit base:** `743ecb285b3a33fb806687b934afa616ab6cf434` (verified equal to `origin/main` on 2026-09-24).
- **Primary-session assignment:** Exact active model and effort are not exposed by the runtime; `unknown / unknown`, not inferred. Primary agent is architect, implementer and reviewer.
- **Agent assignments:** Primary agent; primary; architecture, site implementation and validation; exact model/effort `unknown / unknown`; planned and actual. Routing rationale: a single bounded change must keep route design, evidence provenance and deployment boundaries coherent. No subagents requested.
- **Escalation rule:** No delegation in this work. Sol subagents are prohibited; Sol-requiring work stays with the user-supervised primary session.
- **Inputs:** Current `site/` SvelteKit application, Docker Compose and Tailscale Funnel configuration, preserved document model and governance methodology; current official Dash routing documentation if needed.
- **In scope:** Document SvelteKit/Dash/reverse-proxy responsibilities and data contracts; add a public catalogue and document detail pages for already-published sources; refine the shared shell/nav/theme for an academic data-first presentation; validate local build and existing Funnel state without changing public deployment.
- **Out of scope:** Implementing Dash, ingesting new research documents or conversations, analysis/question design, private-content publication, changing Funnel routing, deploying a new container, `main` integration or remote push.
- **Deliverables:** `site/ARCHITECTURE.md`, `site/src/routes/documentos/` catalogue/detail views, shared layout update, source capture/manifest for new external technical documentation if relied upon, W045 error log and handoff.
- **Method:** Use the existing SvelteKit model and document IDs; preserve `/documentos/{id}/arquivo` file links. Show only documents already approved for the public model. Keep data and analytical interpretations separate. Specify stable `/analises/` routing as a future contract, not a live route. Match existing restrained theme while improving hierarchy and navigation.
- **Acceptance criteria:** Architecture specifies document ingest/publication gates, route ownership, shared data/version contract, deployment and privacy boundaries; document catalogue and detail pages work for all public model documents; original file URLs still work; nav has no empty target; Svelte check/build and repository validation pass. No public service is changed.
- **Risks and uncertainty:** Existing document detail route redirects straight to PDF and may have deep-link expectations; preserve file routes. Dash version/prefix specifics require implementation testing in a later work. Stakeholder conversations require human publication decisions.
- **Validation:** `npm run check`, `npm run build`, local route smoke tests, `python scripts/validate_repository.py`, W045 focused checks, diff review.
- **Error log:** `governance/errors/W045-site-architecture.md`.
- **Human review:** Publishing private conversations, identities or nonpublic records requires a later human approval gate; W045 publishes none of them.
