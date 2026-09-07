# IBM site development environment

This directory documents only the operational bootstrap created by W031. It is separate from the project's historical and documentary research.

## 1. Requirements

- Docker Engine with the Docker Compose v2 plugin (`docker compose`).
- Permission to pull images from Docker Hub and GitHub Container Registry.
- For tailnet access: a Tailscale account allowed to register a non-ephemeral node.
- For public access: an authorized tailnet administrator must permit Funnel and HTTPS certificates.

The stack uses these pinned runtime images:

- `node:24.20.0-alpine` (`sha256:e67514e5…`) for the SvelteKit build and runtime;
- `ghcr.io/coder/code-server:4.135.0` (`sha256:ccd32618…`) for the development workspace;
- `tailscale/tailscale:v1.102.3` (`sha256:8c42c457…`) for the project node.

The complete digests are fixed in `site/Dockerfile` and `compose.yml`.

## 2. Create local configuration

Copy the safe example and edit the local file:

```sh
cp .env.example .env
```

At minimum, replace `CODE_SERVER_PASSWORD`. The `.env` file is ignored by Git.

For unattended Tailscale registration, put a reusable, non-ephemeral auth key in `TS_AUTHKEY`. Generate it in the Tailscale admin console and never commit it. Because node state is persistent, the key is normally used only for the first registration (`TS_AUTH_ONCE=true`). An OAuth secret is not required for this bootstrap.

## 3. Start

From the repository root:

```sh
docker compose up --build
```

Use `docker compose up --build -d` to run in the background. The SvelteKit build runs its type and diagnostic check inside the image build.

## 4. Stop

```sh
docker compose down
```

This retains the named volumes. Do not add `--volumes` when the Tailscale node identity should survive.

## 5. Local ports

| Service | Default local URL | Environment controls | Exposure |
|---|---|---|---|
| `web` | `http://127.0.0.1:5173` | `WEB_BIND`, `WEB_PORT` | Host loopback and, after explicit activation, Funnel |
| `code` | `http://127.0.0.1:8080` | `CODE_BIND`, `CODE_PORT` | Host loopback only |
| `tailscale` | none | none | Tailnet node and Funnel endpoint |

Changing a bind address to `0.0.0.0` exposes that local port on all host interfaces. The defaults intentionally use loopback.

## 6. Authenticate and configure Tailscale

The recommended reproducible path is a reusable, non-ephemeral auth key in the ignored `.env` file:

```dotenv
TS_AUTHKEY=your-real-key-only-in-this-ignored-file
```

Then start or recreate the service:

```sh
docker compose up -d web tailscale
```

The container is configured with:

- `TS_HOSTNAME=ibm` for the tailnet hostname;
- `TS_STATE_DIR=/var/lib/tailscale` backed by `ibm_tailscale_state`;
- `TS_AUTH_ONCE=true` to reuse an authenticated state;
- userspace networking, so no host `/dev/net/tun` or elevated network capabilities are required;
- Docker DNS retained (`TS_ACCEPT_DNS=false`).

If the tailnet requires tags or other already-approved `tailscale up` flags, add them to `TS_EXTRA_ARGS` in `.env`.

## 7. Verify the `ibm` node

Check the container and authenticated Tailscale state:

```sh
docker compose ps
docker compose exec tailscale tailscale status
docker compose exec tailscale tailscale status --json
```

Confirm that the self node reports the hostname `ibm`. The container health check uses `tailscale status`, so an unauthenticated node is distinguishable from a merely started container.

The two containers share the `web` network namespace because current Funnel HTTP proxy targets must be loopback addresses. Docker service-name reachability can still be checked independently:

```sh
docker compose exec tailscale wget -qO- http://web:3000/health
```

The expected response is `{"status":"ok","service":"ibm-web"}`.

## 8. Activate and verify Funnel

Funnel requires MagicDNS, tailnet HTTPS certificates, and a `funnel` node attribute in the tailnet policy. The first activation may provide a web approval flow. An Owner, Admin, or Network admin must authorize policy changes; do not bypass this gate.

After `web` is healthy and the node is authenticated, publish only the SvelteKit service:

```sh
docker compose exec tailscale tailscale funnel --bg --yes http://127.0.0.1:3000
```

Loopback is intentional: the current official CLI documentation states that HTTP reverse-proxy targets support `http://127.0.0.1`, and the Tailscale sidecar shares the web container's network namespace. The `--bg` configuration persists and resumes after Tailscale restarts.

Inspect the actual state and URL allocated by the tailnet:

```sh
docker compose exec tailscale tailscale funnel status
docker compose exec tailscale tailscale funnel status --json
```

Do not infer the public domain. Use only the URL printed by these commands. Public DNS propagation can take up to ten minutes according to Tailscale's documentation.

To disable this bootstrap's Funnel:

```sh
docker compose exec tailscale tailscale funnel --https=443 off
```

## 9. Access code-server

Open `http://127.0.0.1:8080` and enter `CODE_SERVER_PASSWORD` from the local `.env`. The repository is bind-mounted directly at `/home/coder/project`; existing datasets are not copied into the image or duplicated into a separate data volume. Editor state is retained in `ibm_code_server_data`.

## 10. Current limitations

- The page is an operational placeholder, not the final visual design.
- No dataset is selected, transformed, or integrated with the frontend.
- There is no curriculum visualization, lineage graph, storytelling, database, API, application authentication, analytics processing, or notebook stack.
- code-server is locally password-protected but is not exposed through Funnel.
- The final Funnel URL and approval state are tailnet-specific and cannot be recorded until an authorized, authenticated runtime test occurs.
- Named volumes retain runtime state outside Git. `docker compose down --volumes` deliberately deletes that state and can require the Tailscale node to register again.

## Architecture evidence

The implementation follows the current official guidance preserved under [`infrastructure/tailscale/sources/`](../infrastructure/tailscale/sources/). The source manifest records URLs, access date, document validation dates, local paths, SHA-256 values, and evidentiary purposes. The principal upstream references are the official [Docker configuration parameters](https://tailscale.com/docs/features/containers/docker/docker-params), [Tailscale Funnel guide](https://tailscale.com/docs/features/tailscale-funnel), and [`tailscale funnel` CLI reference](https://tailscale.com/docs/reference/tailscale-cli/funnel).

The local `thesis`, `drugslm`, and `arcane` projects were inspected as architecture references. W031 adopts their useful repository bind-mount, named-volume, explicit-network, and health-check patterns without importing their unrelated services, data layouts, or custom Tailscale startup commands.
