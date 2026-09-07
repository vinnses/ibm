# W031 — Site bootstrap review

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary session / implementation-independent acceptance pass / GPT-5 family, exact backend unknown / effort unknown / no subagent was requested or used; the primary compared deliverables directly against the Work acceptance criteria and did not treat implementation narrative as runtime evidence.

## Verdict

**SITE BOOTSTRAP BLOCKED — the current environment has no Docker CLI or daemon, so the required image build, three-container stability, Docker DNS, persistent Tailscale identity, observed hostname, and end-to-end Funnel checks remain unexecuted.**

The source and static architecture are ready for that bounded runtime verification. This verdict does not assert that the stack fails; it keeps unobserved container behavior separate from validated application and configuration facts.

## Acceptance review

| Criterion | Evidence | Result |
|---|---|---|
| Dedicated Work branch from updated `origin/main` | branch `work/w031-site-bootstrap`; base `be77b7185f0c9eb3bf46f5e12aa3a3fd32a67f2e` | pass |
| Minimal TypeScript SvelteKit application | clean lockfile install; `svelte-check` 0 errors/0 warnings; adapter-node build; native production artifact served `/` and `/health` | pass |
| Web container and application health check | multi-stage, digest-pinned Dockerfile and HTTP health command parse in Compose | static pass; container not run |
| code-server repository workspace | pinned image, root checkout bind mount, password environment variable, loopback port, named editor-state volume, health check | static pass; container not run |
| Dedicated persistent Tailscale node | pinned official image; `TS_HOSTNAME=ibm`; `TS_STATE_DIR`; `TS_AUTH_ONCE=true`; named state volume | static pass; identity/hostname not observed |
| Docker service networking | explicit `ibm` network; Tailscale sidecar uses `network_mode: service:web`; documented service-name health request | configuration pass; DNS request not run |
| Funnel targets only web | documented current CLI command targets loopback web port; no code-server Funnel rule | static pass; external authorization/runtime untested |
| Safe configuration and secrets | ignored `.env`; safe `.env.example`; tracked-file checks found no auth key; local ports default to loopback | pass |
| Source preservation | nine official Tailscale captures with provenance and verified SHA-256 | pass |
| Repository governance | W031 validator, repository validator, governance audit, and `git diff --check` pass after recorded recoveries | pass |
| Required Docker runtime checks | Docker command is absent | blocked |

## Architecture assessment

### Established facts

- `compose.yml` resolves statically with exactly `web`, `code`, and `tailscale` services, named network `ibm`, and named volumes `ibm_code_server_data` and `ibm_tailscale_state`.
- Node 24.20.0 executes the generated SvelteKit production server after development dependencies are pruned; both required endpoints respond.
- Registry HEAD requests returned the pinned multi-architecture digests for Node 24.20.0 Alpine, code-server 4.135.0, and Tailscale 1.102.3.
- The official current Tailscale CLI documentation limits HTTP reverse-proxy backends to loopback and says `--bg` resumes Funnel after restart.

### Architecture interpretation

- Sharing the `web` network namespace is the smallest current configuration that satisfies the documented Funnel loopback constraint while keeping Tailscale in its own container and retaining Docker service-name reachability as a separate check.
- `TS_ACCEPT_DNS=false` avoids replacing Docker's resolver and supports the intended `web` service-name diagnostic.
- Named Tailscale state plus `TS_AUTH_ONCE=true` should prevent unnecessary node recreation after ordinary `docker compose down`/`up`, but this remains an unverified operational expectation until Docker execution.

### External and unobserved conditions

- Tailnet registration, the self hostname, MagicDNS, HTTPS certificates, Funnel policy, public DNS, and the allocated URL are not observed.
- code-server image startup, its `/healthz` endpoint, and repository-write ownership are not observed in a container.
- No claim is made that `docker compose build` or `docker compose up` passes in an actual engine solely because static parsing passes.

## Security and scope review

- `npm audit --audit-level=low` reports zero vulnerabilities after the documented `cookie@0.7.2` override.
- No real auth key, password, token, or `.env` is tracked.
- code-server binds to host loopback by default and has no Funnel exposure.
- Existing datasets are only visible through the repository bind mount; none was copied, transformed, reorganized, or selected for frontend use.
- No database, API, application authentication, analytics, notebooks, curriculum visualization, lineage graph, storytelling, final aesthetic, curricular analysis, or 2026 proposal work was added.

