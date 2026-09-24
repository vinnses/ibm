# W043 — Integrate and publish curriculum site

- **Objective:** Integrate reviewed W042 site changes into `main` and update the existing public IBM web service to the integrated build.
- **Branch:** `work/w043-site-release`, followed by user-authorized integration into `main`.
- **Commit base:** `fdada2dd65aed5e6a24dd496c122ad2af7101af6` (updated `main`, 2026-09-23).
- **Primary-session assignment:** Runtime does not expose exact active model/effort; `unknown / unknown`, not inferred. Primary agent is integrator, release operator, and final auditor, because the user requested integration and publication. No subagents.
- **Agent assignments:** Primary agent; primary; integration, deployment, final audit; model `unknown`; effort `unknown`; planned/actual. Sol subagents prohibited; any Sol-requiring task remains with the primary session.
- **Escalation rule:** No delegation; preserve primary-session authority.
- **Inputs:** W042 branch at `1111334`, existing Compose/Tailscale deployment, governance specs and existing release URL.
- **In scope:** Review W042 diff and handoff, run repository/site checks, merge to `main`, rebuild only the `web` service from integrated source, verify health and public URL, record integration and release status.
- **Out of scope:** New site features, source research, curriculum evaluation, unrelated W041 branch, deletion of existing volumes, migration to a different hosting platform.
- **Deliverables:** Merge commit on `main`; integration review/handoff; validated running web deployment at the existing URL if infrastructure remains healthy.
- **Method:** Use clean worktrees; preserve the active code-server and Tailscale services; no secret output; build immutable container from integrated source; replace only the web service; verify HTTP and deployment state.
- **Acceptance criteria:** Required checks pass, `main` contains W042, web service is healthy, public URL serves both grades and six new PDFs, existing user files/branches remain untouched, errors are logged.
- **Risks and uncertainty:** Public Funnel availability can change; the Docker Compose project uses an ignored `.env` in the original checkout; main worktree will use that file without printing its contents. Browser visual QA is outside this release gate.
- **Validation:** `python scripts/validate_repository.py`, W042 hash check, `npm run check`/`npm run build` via Docker, Compose health and HTTP response checks.
- **Error log:** `governance/errors/W043-site-release.md`.
- **Human review:** None anticipated; existing public Funnel is the intended publication target under the user's instruction.
