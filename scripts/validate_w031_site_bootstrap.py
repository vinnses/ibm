#!/usr/bin/env python3
"""Validate W031 source, Compose invariants, preservation, and secret hygiene."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def file_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def validate_sources(errors: list[str]) -> int:
    manifest = ROOT / "infrastructure/tailscale/sources/manifest.csv"
    expected_fields = {
        "title",
        "institution",
        "source_url",
        "access_date",
        "document_date_or_version",
        "document_type",
        "local_path",
        "sha256",
        "evidentiary_purpose",
    }
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        require(set(reader.fieldnames or ()) == expected_fields, "invalid Tailscale manifest fields", errors)
        rows = list(reader)

    require(len(rows) == 9, "expected nine preserved Tailscale source records", errors)
    for row in rows:
        relative = Path(row["local_path"])
        require(not relative.is_absolute(), f"absolute source path: {relative}", errors)
        source = ROOT / relative
        if not source.is_file():
            errors.append(f"missing preserved Tailscale source: {relative}")
            continue
        actual = hashlib.sha256(source.read_bytes()).hexdigest()
        require(actual == row["sha256"], f"SHA-256 mismatch: {relative}", errors)
        require(row["institution"] == "Tailscale", f"unexpected source institution: {relative}", errors)
        require(row["source_url"].startswith("https://tailscale.com/"), f"nonofficial source URL: {relative}", errors)
    return len(rows)


def validate_compose(errors: list[str]) -> None:
    compose = file_text("compose.yml")
    service_block = compose.partition("services:\n")[2].partition("\nnetworks:\n")[0]
    services = set(re.findall(r"^  ([a-z][a-z0-9_-]*):$", service_block, re.MULTILINE))
    require(services == {"web", "code", "tailscale"}, f"unexpected Compose services: {sorted(services)}", errors)

    required_fragments = (
        "${WEB_BIND:-127.0.0.1}:${WEB_PORT:-5173}:3000",
        "${CODE_BIND:-127.0.0.1}:${CODE_PORT:-8080}:8080",
        "./:/home/coder/project",
        "code_server_data:/home/coder/.local/share/code-server",
        "network_mode: service:web",
        "TS_HOSTNAME: ibm",
        "TS_STATE_DIR: /var/lib/tailscale",
        "tailscale_state:/var/lib/tailscale",
        "tailscale/tailscale:v1.102.3@sha256:",
        "ghcr.io/coder/code-server:4.135.0@sha256:",
    )
    for fragment in required_fragments:
        require(fragment in compose, f"missing Compose invariant: {fragment}", errors)

    require("code:\n" in compose and "funnel" not in service_block.partition("  code:\n")[2].partition("  tailscale:\n")[0].lower(), "code service must not configure Funnel", errors)

    docker = shutil.which("docker")
    if docker:
        result = subprocess.run(
            [docker, "compose", "--env-file", ".env.example", "-f", "compose.yml", "config", "--quiet"],
            cwd=ROOT,
            check=False,
        )
        require(result.returncode == 0, "docker compose config failed", errors)


def validate_application(errors: list[str]) -> None:
    package = json.loads(file_text("site/package.json"))
    require(package["scripts"].get("check") is not None, "missing Svelte check script", errors)
    require(package["scripts"].get("build") == "vite build", "unexpected Svelte build script", errors)
    for dependency in ("@sveltejs/kit", "@sveltejs/adapter-node", "svelte", "typescript", "vite"):
        require(dependency in package["devDependencies"], f"missing application dependency: {dependency}", errors)

    page = file_text("site/src/routes/+page.svelte")
    health = file_text("site/src/routes/health/+server.ts")
    dockerfile = file_text("site/Dockerfile")
    require("Informática Biomédica — UFPR" in page, "missing required landing-page identity", errors)
    require("status: 'ok'" in health and "ibm-web" in health, "invalid web health response", errors)
    require("node:24.20.0-alpine@sha256:" in dockerfile, "Node image is not version-and-digest pinned", errors)
    require("RUN npm ci" in dockerfile and "RUN npm run check && npm run build" in dockerfile, "Docker build does not validate SvelteKit", errors)


def validate_secret_hygiene(errors: list[str]) -> None:
    ignore = file_text(".gitignore").splitlines()
    require(".env" in ignore and "!.env.example" in ignore, "root .env ignore rule missing", errors)
    example = file_text(".env.example")
    require(re.search(r"^TS_AUTHKEY=$", example, re.MULTILINE) is not None, "TS_AUTHKEY example must be empty", errors)
    require("change-me-before-starting" in example, "code-server password placeholder missing", errors)

    tracked = subprocess.run(
        ["git", "ls-files", ".env", ".env.*"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    require(tracked in ([], [".env.example"]), f"unexpected tracked environment file: {tracked}", errors)


def main() -> int:
    errors: list[str] = []
    source_count = validate_sources(errors)
    validate_compose(errors)
    validate_application(errors)
    validate_secret_hygiene(errors)

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    docker_state = "available" if shutil.which("docker") else "unavailable (static checks only)"
    print(
        f"W031 checks: sources={source_count}, compose=checked, app=checked, "
        f"secret_hygiene=checked, docker={docker_state}, errors={len(errors)}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

