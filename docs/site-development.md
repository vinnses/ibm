# IBM site development environment

This guide covers only the operational bootstrap created by W031. It is separate
from the project's historical and documentary research.

## 1. Requirements and Docker installation

The host needs Docker Engine, Compose v2, Buildx, Git, and network access to
Docker Hub and GitHub Container Registry. On this CachyOS/Arch host:

```sh
sudo pacman -Syu --needed docker docker-compose docker-buildx jq
sudo systemctl enable --now docker.service
sudo usermod -aG docker "$USER"
newgrp docker
docker run --rm hello-world
```

A kernel upgrade can require a reboot before Docker can load the `bridge`,
`veth`, and `overlay` modules. W031 adds `vinnses` to the `docker`
group as explicitly requested. Log out and back in (or use `newgrp docker`)
before using `docker` without `sudo`. Docker documents that this group grants
root-equivalent daemon access.

The stack pins these runtime images by version and digest:

- `node:24.20.0-alpine` for the SvelteKit build and runtime;
- `ghcr.io/coder/code-server:4.135.0` for the development workspace;
- `tailscale/tailscale:v1.102.3` for the project node.

## 2. Create local configuration

Real credentials remain inside this project's working directory but outside
version control:

```sh
cp .env.example .env
chmod 600 .env
```

Edit `.env` in the project root and replace `CODE_SERVER_PASSWORD` with a long
random value. The file is ignored by Git. Because code-server deliberately
mounts the full checkout, its trusted development terminal can read this local
file; the isolated web container cannot.

`TS_AUTHKEY` is optional. If used, generate a reusable, non-ephemeral key in
the Tailscale admin console and store it only in the project-local `.env`.
The named Tailscale state volume normally makes that key necessary only for the
first registration. Do not place OAuth secrets or auth keys in tracked files.

## 3. Start

From the repository root:

```sh
docker compose up --build
```

Use `docker compose up --build -d` to run in the background. The web image
build runs the Svelte and TypeScript checks before producing the runtime layer.

## 4. Stop

```sh
docker compose down
```

This retains named volumes. Do not add `--volumes` when the Tailscale identity
must survive.

## 5. Local ports

| Service | Default local URL | Controls | Exposure |
|---|---|---|---|
| `web` | `http://127.0.0.1:5173` | `WEB_BIND`, `WEB_PORT` | Host loopback and explicitly configured Funnel |
| `code` | `http://127.0.0.1:8080` | `CODE_BIND`, `CODE_PORT` | Host loopback only |
| `tailscale` | none | none | Tailnet node and Funnel endpoint |

Changing a bind address to `0.0.0.0` exposes that port on host interfaces. The
defaults intentionally use loopback.

## 6. Network and container isolation

`web` joins only the dedicated `ibm_edge` bridge. `code` joins only
`ibm_dev`. `tailscale` is the sole member of both and uses `ibm_dev` for
external connectivity:

```text
Internet -> Funnel -> tailscale -> ibm_edge -> web
                         |
                         +----------> ibm_dev  -> code
```

Docker's user-defined bridges provide service-name DNS. No fixed container IP
is used. Because `web` and `code` share no network, a compromised web
process has no direct Docker route or DNS record for the workspace service.

`web` uses a read-only root filesystem, UID/GID `10001:10001`, drops every
Linux capability, and enables `no-new-privileges`. It has no mounts, Docker
socket, Tailscale state, code-server password, or repository checkout.

`code` is password-authenticated, non-root, capability-free, not privileged,
and has no Docker socket. Its repository bind mount is intentional because the
service is the development workspace. It is never a Funnel target.

`tailscale` uses userspace networking, a read-only root filesystem, no Linux
capabilities, no privileged mode, and private named state. Only its state
volume is writable; the declarative Funnel file is mounted read-only. Neither
state nor socket is shared with `web`.
The supported `TS_BOOT_TIMEOUT=24h` setting keeps the first unauthenticated
boot stable long enough for coordinated authorization rather than restarting
the container after the default one-minute timeout.

## 7. Authenticate and verify the `ibm` node

With `TS_AUTHKEY` in the project-local `.env`, recreate Tailscale:

```sh
docker compose up -d web tailscale
```

Without a key, follow the initial container output and complete the official
interactive login it presents within the configured bootstrap window:

```sh
docker compose logs --follow tailscale
```

Complete the printed authorization flow in the browser. Do not copy its
one-time URL into project documentation or Git. Then verify:

```sh
docker compose exec tailscale tailscale status
docker compose exec tailscale tailscale status --json
docker compose exec tailscale wget -qO- http://web:3000/health
```

The self node must report hostname `ibm`; the last command must return
`{"status":"ok","service":"ibm-web"}`.

## 8. Automatic Funnel activation and verification

Funnel requires MagicDNS, HTTPS certificates, and a `funnel` node attribute in
tailnet policy. An Owner, Admin, or Network admin may have to approve these
settings. W031 does not bypass that external gate.

No post-start Funnel command is required. Following the pattern used by
`arcane/livesync`, Compose sets
`TS_SERVE_CONFIG=/config/funnel.json` and mounts
`infrastructure/tailscale/funnel.json` read-only. After Tailscale
authentication, `containerboot` substitutes the real certificate domain and
applies this configuration:

```json
{
  "Web": {
    "${TS_CERT_DOMAIN}:443": {
      "Handlers": {
        "/": {
          "Proxy": "http://web:3000"
        }
      }
    }
  },
  "AllowFunnel": {
    "${TS_CERT_DOMAIN}:443": true
  }
}
```

Verify the applied backend and allocated URL:

```sh
docker compose exec tailscale tailscale funnel status
docker compose exec tailscale tailscale funnel status --json
```

The final domain is tailnet-specific: record only the URL actually reported by
Tailscale. Public DNS propagation can take time. To stop public exposure
immediately, stop the gateway with `docker compose stop tailscale`. Never add
a handler for `code:8080`.

## 9. Access code-server

Open `http://127.0.0.1:8080` and enter the external
`CODE_SERVER_PASSWORD`. The repository is mounted directly at
`/home/coder/project`; datasets are neither copied into the image nor
duplicated into a data volume. Editor state remains container-local because
W031 persists only the identity-bearing Tailscale state.

## 10. Verification and current limitations

Static checks:

```sh
docker compose config
python scripts/validate_w031_site_bootstrap.py
python scripts/validate_repository.py
python scripts/validate_governance_audit.py
```

Runtime checks and their interpretation are recorded in the W031 handoff.
Tailnet hostname, Funnel status, and public URL cannot be claimed until an
authorized login has completed.

The page remains an operational placeholder. W031 does not implement curriculum
visualization, lineage, storytelling, final protest aesthetics, curricular
analysis, dataset integration, a database, an API, application authentication,
data processing, notebooks, or a 2026 proposal.

## Preserved architecture evidence

Official Docker evidence and its SHA-256 manifest are under
[`infrastructure/docker/sources/`](../infrastructure/docker/sources/).
Official Tailscale documentation and the exact v1.102.3 forwarding
implementation inspected for this design are under
[`infrastructure/tailscale/sources/`](../infrastructure/tailscale/sources/).

The local `thesis`, `drugslm`, and `arcane` projects were also inspected as
architecture references. W031 reuses only relevant bind-mount, named-volume,
network, and health-check patterns, not their unrelated services or data.
