# W031 — Site bootstrap handoff

- Branch: `work/w031-site-bootstrap`.
- Commit base: `be77b7185f0c9eb3bf46f5e12aa3a3fd32a67f2e` from updated `origin/main`.
- Commits produced before this handoff commit:
  - `dd41f65` — define site bootstrap Work unit;
  - `0428dc9` — bootstrap SvelteKit application;
  - `6b15c79` — add Docker Compose development stack;
  - `14e6686` — document Tailscale Funnel bootstrap;
  - `357b4af` — add bootstrap validation and audit trail;
  - `3ac1a4d` — resolve Svelte dependency audit finding;
  - `fa5493e` — initial environment-blocked review and handoff;
  - `8f2c043` — record isolation and Docker runtime addendum;
  - `e028f4c` — segment and harden development stack;
  - `357d382` — document and validate isolated Funnel design;
  - `5ec183d` — record kernel reboot validation gate;
  - `20b6a87` — validate runtime isolation and persistence;
  - `72b0447` — finalize the initial hardened bootstrap handoff;
  - `b02eaaf` — automate Funnel through declarative configuration and record Docker group access;
  - `c6e6e6e` — update the handoff for automatic Funnel;
  - `1ecc99c` — record the post-reboot Git publication credential gate;
  - `e6b743d` — keep runtime configuration project-local.
- Primary-session model and effort: GPT-5 family as exposed by the runtime; exact backend and effort are not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary / primary / orchestration, architecture research, implementation, validation, review, and handoff / GPT-5 family, exact backend unknown / effort unknown / actual / the bounded Work remained in the user-supervised primary session; no subagent was requested or used.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none.
- Completion verdict: **SITE BOOTSTRAP READY — infrastructure validated for the next site-development milestone.**

The sole remaining gate is external Tailscale authorization. The local stack,
including an unauthenticated but stable userspace daemon, is operational and
meets the Work's documented fallback for unavailable tailnet permissions.

## Primary files and structure

- `compose.yml`: one-command stack, network segmentation, hardening, health checks, ports, and persistence.
- `.env.example` and `.gitignore`: safe names/examples and local secret exclusion.
- `site/`: minimal TypeScript SvelteKit page, health endpoint, exact lockfile, and hardened multi-stage image.
- `docs/site-development.md`: installation, configuration, operation, Tailscale/Funnel procedure, isolation, and limitations.
- `infrastructure/docker/sources/`: three preserved official Docker references plus provenance/hash manifest.
- `infrastructure/tailscale/sources/`: official documentation and exact v1.102.3 implementation captures plus provenance/hash manifest.
- `scripts/validate_w031_site_bootstrap.py`: source, Compose, application, hardening, and secret-hygiene validation.
- `governance/work-units/W031-site-bootstrap.md`, `governance/reviews/W031-site-bootstrap.md`, `governance/errors/W031.md`, `governance/human-reviews/W031.md`, and this handoff.

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
  docker/sources/
  tailscale/sources/
scripts/
  validate_w031_site_bootstrap.py
governance/
  work-units/W031-site-bootstrap.md
  reviews/W031-site-bootstrap.md
  handoffs/W031-site-bootstrap.md
  errors/W031.md
  human-reviews/W031.md
```

## Host installation and versions

Installed on CachyOS with:

```sh
sudo pacman -Syu --needed docker docker-compose docker-buildx jq
sudo systemctl enable --now docker.service
```

Observed after the coordinated reboot:

| Component | Version/state |
|---|---|
| Kernel | `7.2.3-1-cachyos` |
| Docker client/server | `29.7.2` / `29.7.2` |
| Docker Compose | `5.5.1` |
| Docker Buildx | `0.36.1` |
| jq | `1.8.2` |
| Docker service | enabled and active |

At the user's explicit request, `vinnses` was added to the root-equivalent
`docker` group. A fresh login or `newgrp docker` is required before an
already-running shell can access the daemon without `sudo`.

## Images and application versions

| Use | Image/tag | Pinned digest |
|---|---|---|
| SvelteKit build/runtime | `node:24.20.0-alpine` | `sha256:e67514e5d0f6c46656005e1b693b2ec9d52e80b641307de684d4a015ba7a4eaf` |
| code-server | `ghcr.io/coder/code-server:4.135.0` | `sha256:ccd326184d71efc5ebb94155eda7bb30153902342a35dbc8525450d81aa55012` |
| Tailscale | `tailscale/tailscale:v1.102.3` | `sha256:8c42c4574ab066384fcb72f69e086a2ff1dd3652eb6f56856cee34bcf0d2f680` |

The application lock includes SvelteKit 2.70.3, Svelte 5.57.0,
adapter-node 5.5.7, Vite 8.2.2, TypeScript 6.0.3, and the patched transitive
`cookie@0.7.2` override. Builds and audits report zero findings.

## Compose services, networks, ports, and volumes

| Service | Role | Networks | Local publication | Runtime storage |
|---|---|---|---|---|
| `web` | SvelteKit adapter-node server | `ibm_edge` only | `127.0.0.1:5173` → `3000` | none |
| `code` | authenticated development workspace | `ibm_dev` only | `127.0.0.1:8080` → `8080` | `./` → `/home/coder/project` |
| `tailscale` | project node and future Funnel gateway | `ibm_edge` + `ibm_dev` | none | `ibm_tailscale_state` → `/var/lib/tailscale` |

No fixed IP is configured. User-defined bridge DNS resolves service names only
within shared networks. Ordinary `docker compose down` retains
`ibm_tailscale_state`; `down --volumes` is intentionally destructive and
was not used.

## Secret configuration

- A strong generated code-server password is stored in the project-local
  `/home/vinnses/ibm/.env`, owned by `vinnses:vinnses` with mode 0600. Its
  value is intentionally not recorded.
- `.env` is a regular ignored file, not a symlink, and is not tracked.
- Because `code` intentionally mounts the full project checkout, its trusted
  terminal can read `.env`; the isolated `web` service has no mount or
  credential access.
- `TS_AUTHKEY` is currently empty; no Tailscale credential was supplied.
- Git tracks only `.env.example`; targeted credential/private-key scans found
  no secret.

## Tailscale configuration and observed state

- `TS_HOSTNAME=ibm`;
- `TS_STATE_DIR=/var/lib/tailscale`;
- `TS_AUTH_ONCE=true`;
- `TS_USERSPACE=true`;
- `TS_ACCEPT_DNS=false`;
- `TS_ENABLE_HEALTH_CHECK=true`;
- `TS_LOCAL_ADDR_PORT=0.0.0.0:9002`, reachable only through Docker networks;
- `TS_BOOT_TIMEOUT=24h`, the official v1.102.3 control used to keep coordinated first authentication stable;
- `TS_SERVE_CONFIG=/config/funnel.json`, backed by the tracked read-only
  declarative configuration;
- no capabilities, host TUN device, privileged mode, host port, or shared socket.

Observed local preference hostname: **`ibm`**.

Observed authenticated tailnet hostname: **not available**. The backend state is
`NeedsLogin`; the unauthenticated self field is not treated as node-name
evidence.

State persistence was tested by hashing `tailscaled.state`, running
`docker compose down` and `docker compose up -d`, and comparing the result.
Both hashes were
`1c146db3abd5660ce508be4d704e6ab828dd147c040a11aaecedd5b43dfc2190`.

## Funnel state

- Observed pre-auth Funnel configuration: empty JSON object; no backend is yet
  published.
- code-server public exposure: none.
- Activation method: automatic declarative application by the official
  `containerboot` process after authentication; no manual Funnel command.
- Configuration file:
  `infrastructure/tailscale/funnel.json`, mounted read-only at
  `/config/funnel.json`.
- Intended only backend: `http://web:3000` over `ibm_edge`, selected by the
  `Web` handler; `AllowFunnel` contains only
  `${TS_CERT_DOMAIN}:443`.
- URL observed: **none**; no domain was invented.
- External dependency: an authorized tailnet login plus MagicDNS, HTTPS
  certificates, the `funnel` policy attribute, any required Owner/Admin/Network
  admin approval, and public DNS propagation.
- Human gate: HR-W031-001 remains open only for authenticated node and public
  Funnel verification.

## Attack-surface verification

1. **web reaches tailscale:** pass; it received HTTP 503 from
   `tailscale:9002/healthz`, proving network reachability while correctly
   reflecting `NeedsLogin`.
2. **web cannot reach code:** pass; Docker DNS lookup returned `ENOTFOUND`.
3. **code is not public through Funnel:** pass for current state and
   configuration; pre-auth Funnel status is empty, the declarative file has one
   `http://web:3000` handler, and it contains no code-server reference. Public
   end-to-end verification awaits HR-W031-001.
4. **web has no Docker socket:** pass; zero mounts and the socket path is absent.
5. **web has no Tailscale credentials:** pass; no secret-shaped environment
   variables and no Tailscale state path.
6. **web is non-root:** pass; `uid=10001(ibm) gid=10001(ibm)`.
7. **no secret is versioned:** pass; only the safe example is tracked and the
   targeted scan is clean.
8. **web compromise does not expose the workspace:** pass; no mounts,
   `code` is unresolvable, and repository paths are absent.

Additional observed web controls: read-only root filesystem (write test
rejected), `no-new-privileges`, `cap_drop: ALL`, not privileged, and zero
restarts. code-server runs UID/GID 1000 with required password auth,
`no-new-privileges`, `cap_drop: ALL`, no Docker socket, no privileged mode,
and only the checkout bind. Tailscale has a read-only root filesystem, the same
privilege controls, and only its private state volume.

## Commands and validation evidence

Primary start/stop:

```sh
docker compose up --build
docker compose down
```

Executed successfully:

- package installation and service enablement;
- running/installed kernel and module checks;
- `docker run --rm hello-world`;
- `docker compose config --quiet`;
- `docker compose build --pull`;
- `docker compose up -d`;
- exact `docker compose up --build -d`;
- Compose status and filtered logs;
- local web and code-server HTTP checks;
- application login redirect and auth-log checks;
- service-name positive and negative connectivity probes;
- container user, mounts, environment, privileges, capabilities, read-only
  filesystems, ports, restart counts, network membership, and declarative Funnel
  configuration inspections;
- Docker 29.7.2 client/server access without `sudo` under a refreshed
  `docker` group context;
- Tailscale preferences, state, health, Funnel status, and down/up persistence;
- `npm ci`, Svelte checks, adapter-node build, production prune/server tests,
  and audit (during image/application validation);
- `python scripts/validate_w031_site_bootstrap.py`: pass, 16 preserved
  W031 infrastructure sources and zero errors;
- `python scripts/validate_repository.py`: pass, zero warnings/errors;
- `python scripts/validate_governance_audit.py`: pass, zero errors;
- `git diff --check`: pass;
- tracked-path and targeted secret scans: pass.

`web` and `code` are healthy. Tailscale remains running with zero restarts
beyond the prior one-minute timeout; its health is correctly non-ready
(`unhealthy` / HTTP 503) solely because authentication is pending.

## Problems and recovery

The append-only log `governance/errors/W031.md` preserves E-W031-001 through
E-W031-034. All agent-correctable defects are resolved. Notable runtime
recoveries were:

- coordinated reboot after kernel/module replacement;
- explicit Tailscale health listen IP;
- removal of a nonessential root-owned code-server state volume;
- removal of the optional internal-network flag that suppressed the local web
  port while preserving two-network segmentation;
- supported 24-hour Tailscale bootstrap timeout to prevent unauthenticated
  one-minute restart loops.
- replacement of the external `.env` symlink with the ignored, mode-0600
  project-local `.env`, preserving its existing values without disclosure.

HR-W031-002 is resolved by the reboot. HR-W031-001 remains the sole external
Tailscale authorization gate. Git publication also requires the user's GitHub
SSH identity to be loaded into the live agent after reboot (E-W031-031).

## Explicitly not performed

- No merge to `main`, integration, tag, or next milestone.
- No final interface or protest aesthetic.
- No curriculum visualization, lineage graph, storytelling, curricular
  evaluation, or 2026 proposal.
- No dataset copy, transformation, reorganization, selection, or frontend
  integration.
- No database, ORM, project API, application authentication, processing
  pipeline, analytical notebook stack, or data-science environment expansion.
- No code-server Funnel publication.
- No tailnet administrative bypass, authenticated node assertion, public URL
  invention, or credential commit.
