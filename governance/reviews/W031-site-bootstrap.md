# W031 — Site bootstrap review

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary session / implementation and acceptance audit / GPT-5 family, exact backend unknown / effort unknown / no subagent was requested or used; the primary compared live container evidence directly with the Work criteria.

## Verdict

**SITE BOOTSTRAP READY — infrastructure validated for the next site-development milestone.**

The local architecture and every attack-surface control available without a
tailnet credential passed. Tailscale runs in userspace with persistent state and
the configured hostname preference `ibm`, but the node is intentionally
`NeedsLogin`. Consequently, no tailnet hostname, Funnel authorization, public
route, or URL is claimed. HR-W031-001 precisely retains that external gate.

## Acceptance review

| Criterion | Observed evidence | Result |
|---|---|---|
| Work branch from updated `origin/main` | `work/w031-site-bootstrap`; base `be77b7185f0c9eb3bf46f5e12aa3a3fd32a67f2e` | pass |
| Docker host runtime | kernel `7.2.3-1-cachyos`; Docker client/server 29.7.2; Compose 5.5.1; Buildx 0.36.1; disposable container ran | pass |
| Minimal TypeScript SvelteKit | image build ran clean install, `svelte-check` with zero findings, adapter-node build, and zero-advisory audit | pass |
| Web health and local access | healthy; `127.0.0.1:5173/health` returned exact `ibm-web` JSON | pass |
| code-server workspace | healthy; root request redirects to `./login`; logs confirm password environment auth; only checkout bind mount | pass |
| Network segmentation | web=`ibm_edge`; code=`ibm_dev`; tailscale=both; no fixed IPs | pass |
| Positive edge path | Tailscale fetched `http://web:3000/health`; web received HTTP 503 from the unauthenticated Tailscale health endpoint | pass |
| Negative web-to-code path | Docker DNS lookup from web returned `ENOTFOUND` | pass |
| Web least privilege | UID/GID 10001; read-only root; no-new-privileges; all capabilities dropped; not privileged; zero mounts | pass |
| Web secret/socket/workspace isolation | no Docker socket, Tailscale state, code workspace, repository governance tree, or secret-shaped environment names | pass |
| code-server hardening | UID/GID 1000; all capabilities dropped; no-new-privileges; not privileged; loopback-only host binding; no Docker socket | pass |
| Tailscale hardening | userspace mode; read-only root; all capabilities dropped; no-new-privileges; not privileged; one writable state volume plus read-only Funnel config; no host port | pass |
| Persistent Tailscale state | identical state hash before and after `docker compose down` / `up`; ordinary down retained the named volume | pass |
| Hostname | local Tailscale preferences report `Hostname: ibm`; authenticated tailnet self name is not yet observable | configuration observed; external observation pending |
| Funnel excludes code | pre-auth status is empty; declarative `TS_SERVE_CONFIG` has sole backend `http://web:3000`; code is absent from edge and config | pass locally; public route pending |
| Secret hygiene | project-local `.env` is ignored and mode 0600; only `.env.example` is tracked; targeted scan found no credentials | pass |
| Repository governance | Work, source hashes, repository links, governance audit, and whitespace checks | pass |

## Security interpretation

Compromise of the web process yields neither a repository mount nor Docker
service-name reachability to code-server. It also yields no Docker socket,
Tailscale credential/state, code-server password, Linux capability, writable
root filesystem, or root UID. The publicly intended component is therefore
isolated from the sensitive development workspace at both network and mount
layers.

Tailscale is the only dual-homed service. This is intentional: it is the edge
gateway and future Funnel endpoint. Its pre-auth status proves that nothing is
currently published. The declarative configuration contains one public handler
for `http://web:3000` and no code-server reference. The exact v1.102.3
implementation preserved under `infrastructure/tailscale/sources/`
establishes the configuration schema and Docker-DNS proxy behavior.

## Runtime limitations and external dependency

- No auth key or tailnet credential was supplied or committed.
- The daemon therefore reports `NeedsLogin`; its health endpoint returns 503
  readiness while the container remains running for coordinated authorization.
- MagicDNS, HTTPS certificates, the tailnet `funnel` node attribute, public
  DNS, the allocated hostname, end-to-end public response, and public URL remain
  unobserved.
- Those conditions require an authorized Tailscale human action and do not
  invalidate the validated local stack under the Work's explicit fallback.

## Scope review

No dataset was copied, transformed, reorganized, selected, or integrated.
No curriculum visualization, lineage graph, storytelling, final visual
aesthetic, curricular evaluation, database, ORM, API, application
authentication, processing pipeline, notebook stack, or 2026 proposal was
implemented. No merge or next milestone was started.
