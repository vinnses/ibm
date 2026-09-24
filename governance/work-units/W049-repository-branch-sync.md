# W049 — Synchronize repository and local branch heads

- **Objective:** Synchronize local committed branch heads with GitHub after the user made SSH authentication available.
- **Branch:** `work/w049-repository-branch-sync`.
- **Commit base:** `3f2ef35a2cc76d1ad07950a2c952101b85389cf8`.
- **Primary-session assignment:** Exact model/effort not exposed by runtime; `unknown / unknown`, not inferred.
- **Agent assignments:** Primary session only; release integrator and Git operator; model/effort unknown / unknown; actual. No subagents. This affects the shared canonical repository and external refs, so synchronization stays with the primary.
- **Escalation rule:** No delegation. Sol subagents are prohibited; Sol-requiring work stays with primary.
- **Inputs:** Local and remote Git refs; all current worktree states; user authorization in the current request to align repositories and branches.
- **In scope:** Fetch current remote refs; compare local and remote branch heads; fast-forward-push all committed local branches and set upstream tracking; verify remote refs; record remaining remote-only branches and local uncommitted items.
- **Out of scope:** Rebasing, force-pushing, deleting remote-only branches, adding uncommitted files, or cleaning any worktree.
- **Deliverables:** This work spec, append-only error log, handoff and integration index entry; synchronized Git refs.
- **Method:** Fetch/prune tracking refs, compare exact branch head pairs, push local branches non-forcibly with upstream setup, and verify refs. Retain any push-rejected divergence as an explicit gap. Never include untracked or modified working-tree content in pushes.
- **Acceptance criteria:** GitHub `main` equals local `main`; every local branch is pushed to a same-named remote ref at the exact commit and tracks it, or a concrete protected/divergent exception is recorded; remote-only branches are preserved; pre-existing worktree changes remain untouched.
- **Risks and uncertainty:** `main` is substantially ahead; a branch push may be rejected if the remote changed after fetch. Some local topic branches are old snapshots, and a separate active worktree has untracked files.
- **Validation:** Fetch, exact local/remote head comparison, final branch tracking status, repository validator and clean main worktree; inspect dirty-worktree findings without altering them.
- **Error log:** `governance/errors/W049-repository-branch-sync.md`.
- **Human review:** None anticipated; if remote protection blocks a push, report the concrete gate and leave history unchanged.
