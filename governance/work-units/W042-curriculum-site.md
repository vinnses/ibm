# W042 — Two-curriculum public site

- **Objective:** Replace the research-first site surface with a usable, source-linked display of the 2011 and 2023 IBM curricula, Ficha 1 availability, and cautiously labeled cross-curriculum matches.
- **Branch:** `work/w042-curriculum-site`.
- **Commit base:** `fdada2dd65aed5e6a24dd496c122ad2af7101af6` (updated `main`, 2026-09-23).
- **Primary-session assignment:** Runtime does not expose the exact active model or effort; record as `unknown / unknown`, not inferred. Primary agent acts as implementer, reviewer, and integrator of this work branch because no delegation was requested. Routing rationale: existing-site redesign and evidence-safe data mapping require integrated judgment.
- **Agent assignments:** Primary agent; primary; site implementation, data mapping, and audit; model `unknown`; effort `unknown`; planned and actual. No subagents. Sol subagents are prohibited; Sol-requiring work returns to the primary session.
- **Inputs:** Existing site source and content model; preserved 2011/2023 curricula and Ficha manifests; W036 gap inventory; Biomedicina public grade and its public GitHub repository at commit `b2a35f603810ad6b1f44d7dac0fd606d2b01f052` as an interaction reference only, not IBM evidence.
- **In scope:** Redesign public entry, two curriculum views, component cards, restrained Ficha 1 status, comparison links, mobile layout, public-only method/source notes, accessibility and build validation.
- **Out of scope:** New documentary research, curricular evaluation, institutional accusations, publication/deployment or main integration, personal progress tracking, and treating title/code similarity as formal equivalence.
- **Deliverables:** Site source, `site/data/source/w042-static-fichas.csv`, focused checks, this specification, `governance/errors/W042-curriculum-site.md`, and handoff.
- **Method:** Reuse formal component instances and preserved source metadata; label non-applicable or uncertain Ficha versions; restrict comparative pairing to transparent heuristics with no claim of formal equivalence. Keep original source binaries unchanged.
- **Acceptance criteria:** Both curricula can be browsed by period; every coded component appears once; available Ficha 1 versions link to a real document; missing or indeterminate states are clear but unobtrusive; apparent matches are labeled as clues, not equivalences; no project-work metadata leaks into public pages; responsive layout and tests pass.
- **Risks and uncertainty:** Applicability of most Ficha versions remains indeterminate, and code/name similarity is not curricular equivalence. Reference repository has no declared license, so its source code is not copied; only observed information architecture is used.
- **Validation:** `npm run check`, `npm run build`, focused route/data checks, `python scripts/validate_repository.py`, and final diff review.
- **Error log:** `governance/errors/W042-curriculum-site.md`.
- **Human review:** None anticipated; unresolved applicability remains explicitly displayed.
