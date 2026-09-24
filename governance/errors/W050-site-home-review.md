# W050 process and review events

Append-only log. No events at work start.

## E-W050-001

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: primary implementer / patch tool.
- Operation: replace homepage and curriculum index in one patch.
- Expected result: replace both route files and delete obsolete loaders.
- Actual result: patch rejected because it contained delete and add operations for the same path; no source file changed.
- Affected paths/state: `site/src/routes/+page.svelte`, `site/src/routes/curriculos/+page.svelte`, route loaders; unchanged.
- Impact: brief implementation delay; no evidence or published-state impact.
- Attempts: (1) rejected multi-operation patch; (2) retry with update operations and separate loader deletion.
- Resolution/status: resolved; update patch applied and route loaders removed.
- Prevention/follow-up: use update hunks when replacing an existing file.
- Evidence: patch-tool response in W050 execution.

## E-W050-002

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: environment / primary validator.
- Operation: `npm run check` in `site/`.
- Expected result: Svelte type and compile check.
- Actual result: `/usr/bin/bash: npm: command not found` (exit 127).
- Affected paths/state: no files changed; validation unavailable on host.
- Impact: run the established Docker-based Node checks instead.
- Attempts: (1) direct host npm failed; (2) Docker-based check planned.
- Resolution/status: resolved; Docker build ran Svelte check and build successfully.
- Prevention/follow-up: document containerized check as the default in this environment.
- Evidence: command output in W050 execution.

## E-W050-003

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: primary validator.
- Operation: inspect deployment configuration and search proposal name.
- Expected result: read existing compose file and find the name in repository evidence.
- Actual result: two exploratory commands used nonexistent path guesses (`compose.yaml`, `docker-compose.yml`, and `proposta*`), producing file-not-found diagnostics.
- Affected paths/state: none; read-only diagnostics.
- Impact: no artifact or publication impact.
- Attempts: (1) guessed paths failed; (2) `rg --files` identified `compose.yml`; (3) targeted `rg` found proposal evidence in `administracao/mec/2026/`.
- Resolution/status: resolved.
- Prevention/follow-up: list paths before opening or searching uncertain locations.
- Evidence: W050 command outputs.

## E-W050-004

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: primary reviewer/implementer.
- Operation: review homepage factual wording against preserved proposal.
- Expected result: use the documented name of the proposed new course.
- Actual result: initial homepage draft used the stakeholder's phrase “Computação e Inteligência Artificial na Saúde”; the preserved proposal and claim matrix name it “Inteligência Artificial Aplicada à Saúde.”
- Affected paths/state: `site/src/routes/+page.svelte` in worktree draft only.
- Impact: would have misstated the proposal's formal title if published.
- Attempts: (1) repository search located `administracao/mec/2026/matriz-validacao-alegacoes.md`; (2) homepage corrected to the documented proposal name before publication.
- Resolution/status: resolved.
- Prevention/follow-up: check institutional names against preserved primary evidence before release.
- Evidence: preserved proposal `administracao/mec/2026/apendice-b-proposta-informatica-biomedica.pdf` and claim matrix.

## E-W050-005

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: primary validator.
- Operation: first Docker Svelte check/build.
- Expected result: zero errors and warnings.
- Actual result: zero errors, three unused CSS warnings after removal of positive Ficha and footer elements.
- Affected paths/state: `CurriculumView.svelte`, `+layout.svelte`.
- Impact: cosmetic code-quality defect only.
- Attempts: (1) remove obsolete selectors; (2) rerun Docker build successfully.
- Resolution/status: resolved.
- Prevention/follow-up: remove associated styles when removing UI elements.
- Evidence: first and second Docker build outputs in W050 execution.

## E-W050-006

- Date/time: 2026-09-24, America/Sao_Paulo.
- Work / branch: W050 / `work/w050-site-home-review`.
- Actor: primary reviewer.
- Operation: inspect rendered grade-page sharing metadata.
- Expected result: each grade page identifies its own curriculum year.
- Actual result: the shared component produced the same “Grades curriculares 2011 e 2023” title and description for both grade URLs.
- Affected paths/state: `site/src/lib/components/CurriculumView.svelte`.
- Impact: ambiguous shared-page preview; no documentary data impact.
- Attempts: (1) rendered local routes and inspected metadata; (2) changed title and descriptions to use `data.year`; (3) final Docker build and HTTP checks confirmed distinct titles for 2011 and 2023.
- Resolution/status: resolved.
- Prevention/follow-up: validate metadata on both variants of a shared page component.
- Evidence: local HTTP response inspection in W050 execution.
