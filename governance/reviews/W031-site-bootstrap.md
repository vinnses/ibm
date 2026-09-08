# W031 — Site bootstrap review

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary session / implementation and acceptance audit / GPT-5 family, exact backend unknown / effort unknown / no subagent was requested or used; the primary compared live container evidence directly with the Work criteria.

## Verdict

**SITE BOOTSTRAP READY — infrastructure validated for the next site-development milestone.**

The local architecture and every attack-surface control passed. After the user
provided an ignored local credential, Tailscale registered the persistent
userspace node as `ibm`, automatically applied the declarative Funnel config,
obtained a TLS certificate, and served the SvelteKit page through both observed
public ingress IPv4 addresses. HR-W031-001 is resolved.

## Acceptance review

| Criterion | Observed evidence | Result |
|---|---|---|
| Work branch from updated `origin/main` | `work/w031-site-bootstrap`; base `be77b7185f0c9eb3bf46f5e12aa3a3fd32a67f2e` | pass |
| Docker host runtime | kernel `7.2.3-1-cachyos`; Docker client/server 29.7.2; Compose 5.5.1; Buildx 0.36.1; disposable container ran | pass |
| Minimal TypeScript SvelteKit | image build ran clean install, `svelte-check` with zero findings, adapter-node build, and zero-advisory audit | pass |
| Web health and local access | healthy; `127.0.0.1:5173/health` returned exact `ibm-web` JSON | pass |
| code-server workspace | healthy; root request redirects to `./login`; logs confirm password environment auth; only checkout bind mount | pass |
| Network segmentation | web=`ibm_edge`; code=`ibm_dev`; tailscale=both; no fixed IPs | pass |
| Positive edge path | Tailscale fetched `http://web:3000/`; web reaches the healthy Tailscale endpoint; public ingress returned the SvelteKit page | pass |
| Negative web-to-code path | Docker DNS lookup from web returned `ENOTFOUND` | pass |
| Web least privilege | UID/GID 10001; read-only root; no-new-privileges; all capabilities dropped; not privileged; zero mounts | pass |
| Web secret/socket/workspace isolation | no Docker socket, Tailscale state, code workspace, repository governance tree, or secret-shaped environment names | pass |
| code-server hardening | UID/GID 1000; all capabilities dropped; no-new-privileges; not privileged; loopback-only host binding; no Docker socket | pass |
| Tailscale hardening | userspace mode; read-only root; all capabilities dropped; no-new-privileges; not privileged; one writable state volume plus read-only Funnel config; no host port | pass |
| Persistent Tailscale state | identical pre-auth state hash across `down`/`up`; after authentication, a container restart preserved the exact node ID and restored healthy live Funnel state | pass |
| Hostname | authenticated status reports `HostName: ibm`, `DNSName: ibm.tail6629d6.ts.net.`, `Online: true`, and backend `Running` | pass |
| Funnel excludes code | live Funnel status has the sole backend `http://web:3000` on HTTPS 443; code is absent from edge and config; both public IPv4 ingress addresses returned HTTP 200 | pass |
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
gateway and active Funnel endpoint. The live declarative configuration contains
one public handler for `http://web:3000` and no code-server reference. The exact v1.102.3
implementation preserved under `infrastructure/tailscale/sources/`
establishes the configuration schema and Docker-DNS proxy behavior.

## Authenticated Funnel evidence

- The credential exists only in ignored `.env`; no value was displayed or committed.
- The node is healthy, online, tagged `tag:funnel`, and reports no health warnings.
- The observed public URL is `https://ibm.tail6629d6.ts.net/`.
- Public DNS-over-HTTPS returned `209.177.145.97`, `209.177.145.192`,
  `2607:f740:f::67`, and `2607:f740:f::b31`.
- Forced HTTPS requests through both observed IPv4 ingress addresses returned
  HTTP 200 and the title `Informática Biomédica — UFPR`.

## Scope review

No dataset was copied, transformed, reorganized, selected, or integrated.
No curriculum visualization, lineage graph, storytelling, final visual
aesthetic, curricular evaluation, database, ORM, API, application
authentication, processing pipeline, notebook stack, or 2026 proposal was
implemented. No merge or next milestone was started.
