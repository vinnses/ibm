# Error log — W017 preserved 2011 ementa extraction

This file is append-only and is distinct from `governance/errors/W017.md`, which belongs to the previously integrated W017 planning Work.

## E-W017-101 — Requested Work identifier collides with an integrated Work

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator.
- **Operation:** create the requested bounded Work identity and governance paths.
- **Expected result:** one unused Work identifier with unambiguous governance records.
- **Actual result:** `W017` already identifies the integrated remaining-data planning Work, while the user explicitly assigned the same identifier to this execution.
- **Affected paths/state:** governance filenames and event identifiers; the requested branch name is unique and was not affected.
- **Impact:** using the old generic W017 paths would overwrite or conflate distinct work histories.
- **Attempts:** inspected `governance/WORK_INDEX.md` and existing W017 specification, review, handoff, and error-log paths; retained the user-requested label while assigning the unique slug `w017-ementas-preservadas-2011` to every new path and reserving event numbers 101 onward.
- **Resolution/status:** resolved; the identifier collision remains a naming fact for later integration review.
- **Prevention/follow-up:** integration should either retain the qualified label or assign the next unused global ID without rewriting this branch's historical record.
- **Evidence:** commit base governance tree and this Work specification.

## E-W017-102 — Initial clone exceeded the command yield window

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / pre-branch repository setup.
- **Actor:** execution environment and primary orchestrator.
- **Operation:** clone `https://github.com/vinnses/ibm.git` with its checked-out source files and Git LFS objects.
- **Expected result:** a completed clean checkout within the first 30-second command window.
- **Actual result:** the command yielded after displaying `Cloning into 'ibm'...` while the clone process and `.git/index.lock` remained active; a concurrent status check temporarily displayed staged deletions and untracked replacements because checkout was incomplete.
- **Affected paths/state:** transient clone worktree only; no remote or repository commit changed.
- **Impact:** branch creation and inspection were paused until checkout completion; no evidence impact.
- **Attempts:** verified the live clone process and index lock; waited in a bounded read-only poll; rechecked a clean `main`, fetched `origin/main`, and confirmed commit `3530173f374d0c361e9f8829d3347c638b21a7db` before creating the branch.
- **Resolution/status:** resolved
- **Prevention/follow-up:** wait for `.git/index.lock` removal and a clean status before inspecting a large LFS-backed clone.
- **Evidence:** local process/status checks and recorded commit base.

## E-W017-103 — Optional BeautifulSoup parser dependency unavailable

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator and Python environment.
- **Operation:** mechanically summarize the 37 preserved Ementário HTML pages with `bs4`.
- **Expected result:** parse the files and print their general-information and ementa fields.
- **Actual result:** Python stopped before reading files with `ModuleNotFoundError: No module named 'bs4'`.
- **Affected paths/state:** none; the command was read-only and no output artifact was created.
- **Impact:** no evidence impact; mechanical inspection required a dependency-free parser.
- **Attempts:** initial optional parser import failed; replacement will use Python standard-library HTML parsing or repository-available tools.
- **Resolution/status:** resolved; no package installation is required.
- **Prevention/follow-up:** prefer standard-library parsing for preserved simple HTML when third-party parser availability has not been established.
- **Evidence:** execution output in the primary session.

## E-W017-104 — W009 CI262 formal label and period do not reproduce the resolution

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** prior W009 extractor/validator; detected by the W017 primary source review.
- **Operation:** reuse the established W009 target universe and formal labels while comparing preserved ementa/Ficha evidence.
- **Expected result:** W009's formal label and recommended period reproduce the cited Resolução nº 34/2010-CEPE.
- **Actual result:** `curriculos/2011/inventario/componentes.csv` labels CI262 as `Trabalho De Conclusão De Curso Em Informática` and records `recommended_term=7`; the preserved resolution, Anexo I page 6, reads `Trabalho de Conclusão de Curso em Informática Biomédica` under `8º sem`. The current Ementário page also displays period 8 but truncates the title after `Informática`.
- **Affected paths/state:** pre-existing W009 `componentes.csv` and its validator expectations; W017 coverage uses `w009_target_label` only as an upstream label and does not treat it as a literal historical transcription.
- **Impact:** reusing those two W009 fields as primary evidence would misstate CI262's formal name and period. The 41-target identity by code is unaffected, and no W017 ementa text depends on the incorrect period.
- **Attempts:** compared W009 row CI262 with the preserved resolution page 6 and Ementário record `161283.html`; kept all source versions separate; did not modify the accepted W009 dataset because this Work is scoped to preserved ementa/Ficha extraction.
- **Resolution/status:** open; bounded W009 correction, contained for W017 by explicit field labeling and source-specific extraction.
- **Prevention/follow-up:** a later correction Work should update the W009 CI262 title/period and its validator against the primary act, then rerun repository-wide checks.
- **Evidence:** `curriculos/2011/fontes/resolucao-34-2010-cepe.pdf`, Anexo I page 6; `curriculos/2011/fontes/ementario/disciplinas/161283.html`; `curriculos/2011/inventario/componentes.csv`.

## E-W017-105 — First governance-audit run rejected status formatting

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator and `scripts/validate_governance_audit.py`.
- **Operation:** run all required validators after creating the W017 datasets and documentation.
- **Expected result:** governance audit accepts the four complete error records.
- **Actual result:** the audit reported four invalid status values because the log wrote status names in Markdown code formatting and, for two events, added prose before the first semicolon.
- **Affected paths/state:** `governance/errors/W017-ementas-preservadas-2011.md`; research evidence and datasets were unaffected.
- **Impact:** the governance acceptance check failed while all source/data and repository checks passed.
- **Attempts:** inspected `event_status()` in the audit script; changed each earlier status line to an unformatted allowed value before the first semicolon; appended this event and reran the audit.
- **Resolution/status:** resolved
- **Prevention/follow-up:** use exactly `open`, `resolved`, `accepted exception`, or `blocked` as the first unformatted status token in new event records.
- **Evidence:** first governance-audit output (`invalid or missing status value` for E-W017-101 through E-W017-104) and subsequent passing rerun.

## E-W017-106 — Three additional W009 labels reproduce portal variants instead of the cited act

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** prior W009 extractor; detected by W017 primary visual source review using the PDF procedure.
- **Operation:** visually verify Resolução nº 34/2010-CEPE Anexo I pages 5–6 against source-specific W017 records and upstream W009 labels.
- **Expected result:** W009 labels cited to the resolution reproduce its component names, allowing them to serve as accurate upstream target labels.
- **Actual result:** the resolution reads CI171 `Aprendizado de Máquina`, CI218 `Sistemas de Banco de Dados`, and CI172 `Processamento de Imagens Biomédicas`; W009 records `Aprendizado De Máquinas`, `Sistemas De Bancos De Dados`, and `Processamento De Imagnes Biomédicas`, matching the current portal variants apart from case. This is additional to the CI262 defect in E-W017-104.
- **Affected paths/state:** pre-existing W009 `componentes.csv`; W017 `cobertura.csv` explicitly labels the carried field `w009_target_label`, while `evidencias.csv` preserves each portal source string and `divergencias.md` preserves both source versions.
- **Impact:** the three W009 labels cannot be cited as literal transcriptions of the resolution. Component identity by code and all W017 ementa/Ficha fields remain unaffected.
- **Attempts:** rendered and visually inspected resolution pages 5–6; compared them with Ementário pages `161269.html`, `161275.html`, and `161281.html`; added version-separated difference records D-W017-012 through D-W017-014 without changing W009.
- **Resolution/status:** open; bounded W009 correction, contained for W017 by source-specific fields and explicit divergence records.
- **Prevention/follow-up:** the later W009 correction batch should audit every `title` against the primary act, correct these three rows together with CI262, and add literal-source regression expectations.
- **Evidence:** `curriculos/2011/fontes/resolucao-34-2010-cepe.pdf`, Anexo I page 5; preserved Ementário component pages; `curriculos/2011/inventario/componentes.csv`.

## E-W017-107 — Local HTTPS push had no GitHub credentials

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator, local Git client, and authenticated GitHub connector.
- **Operation:** publish the completed local branch to `origin` without merging `main`.
- **Expected result:** `git push --set-upstream origin work/w017-ementas-preservadas-2011` publishes the five local semantic commits.
- **Actual result:** the Git client failed with `fatal: could not read Username for 'https://github.com': No such device or address`; no CLI credential helper or authenticated `gh` session was available.
- **Affected paths/state:** local branch remained clean at `a99fa67`; the remote branch did not yet contain the Work; `main` was unchanged.
- **Impact:** the exact local commit objects could not be transferred through the configured HTTPS remote.
- **Attempts:** (1) direct non-force push failed before writing; (2) checked for an available CLI credential/helper, which was unavailable; (3) used the authenticated GitHub connector to create the requested remote branch from base `3530173`, upload all 12 new-file blobs, create tree `2db0554cd3fa3b49b04ceba4262ce8c73c6f3164`, and publish commit `4ed8a129e34ed00248fad07446033e4892bd8790`; (4) the containing follow-up sync record is published separately and tree equality is verified after it.
- **Resolution/status:** resolved; the remote branch is published without modifying `main`, with the local semantic commit sequence retained in this handoff and a byte-identical remote tree.
- **Prevention/follow-up:** in this Work runtime, test authenticated Git push availability before the final checkpoint; if absent, publish through the GitHub connector and explicitly record the local/remote history mapping.
- **Evidence:** failed Git output; connector branch/blob/tree/commit/ref results; final local-versus-remote tree comparison.

## E-W017-108 — Combined synchronization-record patch used an incorrect heading context

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator and patch tool.
- **Operation:** append E-W017-107 and the remote synchronization section to the existing error log and handoff in one patch.
- **Expected result:** both documentation updates apply cleanly.
- **Actual result:** the patch was rejected before changing either file because it searched for `- Recommended next bounded work`, while the handoff uses the Markdown heading `## Recommended next bounded work`.
- **Affected paths/state:** none; the patch application was atomic and made no partial changes.
- **Impact:** no evidence or Git impact; documentation recovery required a corrected patch.
- **Attempts:** inspected the handoff heading; split the update and reapplied it with the exact heading/file-end context.
- **Resolution/status:** resolved
- **Prevention/follow-up:** inspect exact surrounding text before a multi-file patch near a heading; prefer smaller patches for append-only audit records.
- **Evidence:** patch verification failure and the successfully applied replacement patches.

## E-W017-109 — Independent unauthenticated fetch encountered a transient GitHub 502

- **Date/time:** 2026-09-06 UTC.
- **Work / branch:** requested W017 / `work/w017-ementas-preservadas-2011`.
- **Actor:** primary orchestrator, local Git client, and authenticated GitHub connector.
- **Operation:** independently fetch the published remote branch through the local HTTPS remote and compare its tree with local checkpoint `446fcc67`.
- **Expected result:** update the local remote-tracking ref and confirm remote commit/tree identity.
- **Actual result:** GitHub returned HTTP 502 while `git fetch` requested the branch; the local remote-tracking ref was not updated.
- **Affected paths/state:** none; the operation was read-only, the local branch stayed clean, and the previously published remote ref was unchanged.
- **Impact:** only the redundant verification path was interrupted; publication and research artifacts were unaffected.
- **Attempts:** after the failed fetch, queried the authenticated branch endpoint directly. It returned remote head `c414e007404e02569db249d5344e84484ae449e0` and tree `671975d1c26e211904493a6c6f025c81bc7296b8`, exactly equal to `git rev-parse HEAD^{tree}` at local checkpoint `446fcc67`.
- **Resolution/status:** resolved
- **Prevention/follow-up:** use the authenticated connector as the authoritative verification path when the unauthenticated HTTPS transport is unavailable or transiently failing.
- **Evidence:** failed `git fetch` output; authenticated GitHub branch response; local `git rev-parse HEAD^{tree}` output.
