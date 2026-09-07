# W031 — Site bootstrap handoff

- Branch: `work/w031-site-bootstrap`.
- Commit base: `be77b7185f0c9eb3bf46f5e12aa3a3fd32a67f2e` from updated `origin/main`.
- Commits produced: `dd41f65` (Work specification); `0428dc9` (SvelteKit application); `6b15c79` (Compose stack); `14e6686` (Tailscale evidence and operations); `357b4af` (validation and audit trail); `3ac1a4d` (dependency advisory correction); plus the final review/handoff commit containing this file.
- Primary-session model and effort: GPT-5 family as exposed by the runtime; exact backend and reasoning effort were not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary / primary / orchestrator, infrastructure researcher, implementer, validator, reviewer, and handoff author / GPT-5 family, exact backend unknown / effort unknown / actual / bounded Work stayed in the user-supervised primary session; no subagent was requested or used.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none.
- Objective and completion verdict: deliver the minimal executable architecture for the IBM site. **SITE BOOTSTRAP BLOCKED — the implementation and static/application checks are complete, but the environment has no Docker CLI or daemon, preventing the mandatory container/runtime and Tailscale/Funnel observations.**

## Deliverables and primary files

- `compose.yml`: single entry point with `web`, `code`, and `tailscale`.
- `.env.example` and `.gitignore`: safe local configuration and secret exclusion.
- `site/`: minimal TypeScript SvelteKit application, health endpoint, exact lockfile, and multi-stage Node container.
- `docs/site-development.md`: requirements, start/stop, ports, Tailscale registration, hostname/Funnel verification, code-server access, persistence, and limitations.
- `infrastructure/tailscale/sources/`: nine preserved official source captures and `manifest.csv`.
- `scripts/validate_w031_site_bootstrap.py`: deterministic source/configuration/scope/secret checks.
- `governance/work-units/W031-site-bootstrap.md`, `governance/reviews/W031-site-bootstrap.md`, `governance/errors/W031.md`, `governance/human-reviews/W031.md`, and this handoff.

## Structure created

```text
site/
  Dockerfile
  package.json
  package-lock.json
  src/
    app.html
    routes/
      +page.svelte
      health/+server.ts
docs/
  site-development.md
infrastructure/
  tailscale/sources/
governance/
  work-units/W031-site-bootstrap.md
  reviews/W031-site-bootstrap.md
  handoffs/W031-site-bootstrap.md
  errors/W031.md
  human-reviews/W031.md
```

## Images and versions

| Use | Tag | Pinned manifest digest |
|---|---|---|
| SvelteKit build/runtime | `node:24.20.0-alpine` | `sha256:e67514e5d0f6c46656005e1b693b2ec9d52e80b641307de684d4a015ba7a4eaf` |
| code-server | `ghcr.io/coder/code-server:4.135.0` | `sha256:ccd326184d71efc5ebb94155eda7bb30153902342a35dbc8525450d81aa55012` |
| Tailscale | `tailscale/tailscale:v1.102.3` | `sha256:8c42c4574ab066384fcb72f69e086a2ff1dd3652eb6f56856cee34bcf0d2f680` |

Svelte application pins include SvelteKit 2.70.3, Svelte 5.57.0, adapter-node 5.5.7, Vite 8.2.2, and TypeScript 6.0.3. `cookie@0.7.2` is an explicit patched transitive override.

## Compose services, ports, and volumes

| Service | Role | Local port | Health signal | Storage/network |
|---|---|---|---|---|
| `web` | adapter-node SvelteKit server | `127.0.0.1:5173` → `3000` | `GET /health` through Node fetch | `ibm` network; no data volume |
| `code` | code-server over the checkout | `127.0.0.1:8080` → `8080` | `GET /healthz` through curl | `./` → `/home/coder/project`; `ibm_code_server_data` |
| `tailscale` | project tailnet node and Funnel sidecar | none | `tailscale status` | shares `web` network namespace; `ibm_tailscale_state` → `/var/lib/tailscale` |

Ordinary `docker compose down` retains both named volumes. `docker compose down --volumes` is intentionally destructive to editor and Tailscale state and was not run.

## Tailscale and Funnel state

- Configuration: `TS_HOSTNAME=ibm`, `TS_STATE_DIR=/var/lib/tailscale`, `TS_AUTH_ONCE=true`, `TS_USERSPACE=true`, `TS_ACCEPT_DNS=false`; `TS_AUTHKEY` and optional `TS_EXTRA_ARGS` come only from ignored `.env`.
- Persistence: named Compose volume `ibm_tailscale_state`.
- Funnel target: `http://127.0.0.1:3000` from the sidecar's shared web namespace, activated with `tailscale funnel --bg --yes`.
- Hostname observed: **not observed**; `ibm` is configured but Docker/Tailscale runtime was unavailable.
- Funnel state: **not activated or observed**; tailnet HTTPS/policy authorization and an authenticated Docker runtime are external dependencies.
- URL observed: **none**; no domain was invented.
- code-server Funnel exposure: none.

## Start and verification commands

```sh
cp .env.example .env
docker compose up --build
docker compose ps
curl -fsS http://127.0.0.1:5173/health
curl -fsS http://127.0.0.1:8080/healthz
docker compose exec tailscale tailscale status --json
docker compose exec tailscale wget -qO- http://web:3000/health
docker compose exec tailscale tailscale funnel --bg --yes http://127.0.0.1:3000
docker compose exec tailscale tailscale funnel status
docker compose down
docker compose up -d
```

After the final two commands, repeat `tailscale status --json` and confirm the same node identity and self hostname. Exact operational instructions are in `docs/site-development.md`.

## Sources added

Nine current official Tailscale captures were added: HTML and source Markdown for Docker, Funnel, and Serve; source Markdown for Docker parameters, Docker Compose setup, and the Funnel CLI. `infrastructure/tailscale/sources/manifest.csv` records title, institution, URL, access date, upstream validation date, type, local path, SHA-256, and purpose. All nine hashes pass the W031 validator.

## Coverage reached

- Application source, production adapter build, health endpoint, and minimal landing page complete.
- Three-service Compose architecture, loopback debugging ports, workspace mount, named persistence, health checks, and safe configuration complete.
- Current official Docker/Funnel requirements and the loopback proxy constraint are reflected and preserved.
- `thesis`, `drugslm`, and `arcane` were inspected read-only; relevant bind-mount, volume, network, and health-check patterns informed the bounded design.

## Validations executed and results

- `git fetch origin main --prune`: pass before branch creation.
- Portable official Node v24.20.0 `npm ci`: pass; 75 packages installed from lockfile.
- `npm run check`: pass; zero errors and zero warnings.
- `npm run build`: pass with adapter-node.
- `npm prune --omit=dev` followed by `node build`: pass.
- HTTP `/`: pass; rendered `Informática Biomédica — UFPR`.
- HTTP `/health`: pass; exact JSON `{"status":"ok","service":"ibm-web"}`.
- `npm audit --audit-level=low`: pass; zero vulnerabilities after correction.
- Official registry manifest checks: all three pinned tags returned HTTP 200 and the recorded digests.
- Docker Compose v5.5.1 standalone binary checksum verification and `compose.yml config --quiet`: pass with `.env.example`; this is daemon-free parsing, not `docker compose` runtime execution.
- `python scripts/validate_w031_site_bootstrap.py`: pass; nine sources, Compose invariants, app, and secret hygiene; reports Docker unavailable.
- `python scripts/validate_repository.py`: pass; zero warnings and zero errors.
- `python scripts/validate_governance_audit.py`: pass; zero errors.
- `git diff --check`: pass.
- Tracked environment/runtime-state check: pass; only `.env.example` is tracked and no build/state directory is tracked.
- Auth-key-shaped secret scan of project-authored tracked files: pass; none found.
- `docker compose config`, `docker compose build`, `docker compose up`, container stability/health, Docker service DNS, Tailscale state persistence, hostname, and Funnel: **not executed because `docker` is not installed**.

## Problems, gaps, divergences, and provisional information

- Problems encountered: E-W031-001 and E-W031-003 through E-W031-010 were resolved and remain preserved in the append-only log. E-W031-002 remains open for missing Docker runtime.
- Gaps: all runtime container evidence; actual code-server response; Docker DNS request; Tailscale registration/identity persistence; tailnet hostname; Funnel authorization, routing, public response, and URL.
- Divergence handled: the requested service-name networking and official current Funnel loopback-only proxy rule are both preserved. The sidecar shares `web` networking for Funnel and separately documents `http://web:3000/health` as the Docker DNS check. Runtime confirmation remains pending.
- Provisional information: registry tags/digests and official docs are current as observed on 2026-09-07; operational behavior is not projected beyond those sources.
- External dependencies: Docker Engine + Compose v2, image registry access, a non-ephemeral Tailscale registration credential, MagicDNS, tailnet HTTPS certificates, Funnel policy authorization by an Owner/Admin/Network admin, and public DNS propagation.

## Explicitly unperformed work

- No merge to `main`, push, integration index update, or next milestone.
- No final interface/protest aesthetic, curriculum visualization, lineage graph, storytelling, curricular evaluation, dataset selection/integration/transformation, database, ORM, API, application authentication, data processing, analytical notebooks, or 2026 proposal work.
- No code-server publication through Funnel.
- No secret, auth key, real password, tailnet domain, or invented URL was committed.

## Audit records and next bounded work

- Error-log path: `governance/errors/W031.md`.
- Resolved event IDs: E-W031-001, E-W031-003, E-W031-004, E-W031-005, E-W031-006, E-W031-007, E-W031-008, E-W031-009, E-W031-010.
- Open event IDs: E-W031-002.
- Human-review question path: `governance/human-reviews/W031.md`; HR-W031-001 blocks only authenticated node/Funnel observation and actual URL recording, while missing Docker also blocks the runtime acceptance gate.
- Recommended next bounded work unit: continue W031 only on a Docker-enabled, authorized tailnet host to execute the listed runtime checks, append evidence, resolve or precisely retain E-W031-002/HR-W031-001, and update this verdict. Do not begin interface development before that separate authorization.

