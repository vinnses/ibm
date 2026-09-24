# W049 error log

No synchronization failures recorded at work-unit opening. Initial inspection found the local `main` ahead of `origin/main` and local branches W032-W048 missing from the remote. The user's W041 PDF and W027 Python cache are pre-existing untracked worktree contents and are explicitly out of scope for pushes.

## E-W049-001 — GitHub push protection blocked main and descendant branches

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W049 / `main` and local topic branches.
- **Actor:** Primary agent / GitHub push protection.
- **Operation:** Run `git push --all --set-upstream origin` to synchronize local committed branch heads.
- **Expected result:** Fast-forward or create all same-named remote refs and configure tracking.
- **Actual result:** GitHub rejected `main` and the 18 local refs W032-W049 because their history contains a Mapbox access-token string embedded in the preserved public HTML capture `dados/cursos-ia-ibm/w044/fontes/curriculos/pucpr_ai_aplicada_ead.html:4257`. No token value or unblock URL is retained here. Git LFS uploaded one 457 MB object. Other refs already matching remote were accepted and tracking was configured.
- **Affected paths/state:** Remote branch refs rejected remain unchanged; local commits, preserved source bytes and worktrees remain unchanged.
- **Impact:** `origin/main` remains behind local `main`; 18 local branch names remain absent remotely. Four remote-only branches were not deleted.
- **Attempts:** (1) Confirmed the string's type using only its prefix: `pk.`. (2) Checked official Mapbox documentation that `pk` tokens are public client-side tokens and `sk` tokens are secret. (3) Checked GitHub's official push-protection workflow for false positives. (4) Attempted to reach the authenticated GitHub false-positive page in the in-app browser; runtime reports no browsers available. No bypass was executed and no history was rewritten.
- **Resolution/status:** Open pending authorized GitHub UI action. The contents appear to be a public token, but repository-owner false-positive classification is still required to let the protected push proceed.
- **Prevention/follow-up:** Owner should mark the identified public `pk` occurrence as a false positive in the repository's GitHub security UI; then rerun the non-forced branch push and verify exact ref equality. Do not publish the token itself in messages or logs.
- **Evidence:** Sanitized push result; captured source at cited path; [Mapbox token documentation](https://docs.mapbox.com/help/dive-deeper/access-tokens/) and [GitHub push-protection documentation](https://docs.github.com/en/code-security/how-tos/secure-your-secrets/work-with-leak-prevention/push-protection-on-the-command-line).

## E-W049-002 — No authenticated browser available for GitHub false-positive UI

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W049 / GitHub push-protection recovery.
- **Actor:** Primary agent / browser runtime.
- **Operation:** Open GitHub's owner-specific false-positive flow after classifying the recorded `pk` token as public.
- **Expected result:** Use an authenticated browser session to record the false-positive classification.
- **Actual result:** Browser runtime reported no browser available; `agent.browsers.list()` returned an empty list. The first module import also used an incorrect path and failed before runtime setup; corrected path setup succeeded but no browser was available.
- **Affected paths/state:** No GitHub setting or repository state changed through the browser.
- **Impact:** The push-protection false-positive action could not be submitted; the affected refs remain blocked.
- **Attempts:** (1) Corrected the browser-client module path using a read-only file listing. (2) Reused the initialized runtime and read its required troubleshooting instructions. (3) Listed browser sessions once; none were available. GitHub app connector tools do not expose this specific false-positive action.
- **Resolution/status:** Open; human owner action is required.
- **Prevention/follow-up:** Owner may use their authenticated GitHub session to mark the finding false positive, then notify the primary session to retry pushes.
- **Evidence:** Browser runtime output; available connector/tool catalog; W049-001 evidence.

## E-W049-003 — Remote-ref audit formatter referenced the wrong local variable

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W049 / post-push verification.
- **Actor:** Primary agent / tool orchestration.
- **Operation:** Format local and remote refs plus `origin/main` divergence after the partial push.
- **Expected result:** Output same-name, missing, and remote-only ref counts.
- **Actual result:** The shell/Git subcommands completed, but the JavaScript formatter referenced undefined `rs` instead of its `out` result array and raised `ReferenceError` before emitting the comparison.
- **Affected paths/state:** None; read-only operations only.
- **Impact:** Verification output was delayed; no Git state changed.
- **Attempts:** Re-ran the same three read-only commands with corrected result indexing and obtained the ref comparison successfully.
- **Resolution/status:** Resolved.
- **Prevention/follow-up:** Use named result arrays consistently when composing parallel read-only command results.
- **Evidence:** Successful post-push ref comparison output.

## E-W049-004 — Handoff patch used stale bullet text

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W049 / integration handoff.
- **Actor:** Primary agent / patch tool.
- **Operation:** Append push-protection outcome and human-review gate to the W049 handoff.
- **Expected result:** Add the HR-W049-001 record and replace the pending handoff statements.
- **Actual result:** The patch context expected an unedited `Explicitly unperformed` block, but the actual handoff already contained a separate, shorter version. Patch verification rejected the whole patch; no file was changed by that attempt.
- **Affected paths/state:** None; patch made no partial edits.
- **Impact:** No repository or external state changed; closure note needed correction.
- **Attempts:** (1) Read the exact current handoff. (2) Reapplied a narrower patch against the actual lines and added the human-review file.
- **Resolution/status:** Resolved.
- **Prevention/follow-up:** Read exact patch context before applying multi-file replacements.
- **Evidence:** Corrected handoff and `governance/human-reviews/W049.md`.
