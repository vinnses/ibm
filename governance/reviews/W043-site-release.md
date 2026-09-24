# W043 integration review

- **Date:** 2026-09-23 (America/Sao_Paulo).
- **Branch/base:** `work/w043-site-release` from `fdada2dd65aed5e6a24dd496c122ad2af7101af6`.
- **Reviewed input:** W042 at `1111334`; merge commit `3a37cdd` had no conflicts.
- **Scope:** The public surface is limited to 2011 and 2023 curricula, Ficha 1 links, and explicitly non-formal cross-grade clues. Legacy analytical pages redirect rather than exposing work metadata. W041 jobs work and the untracked user PDF in the original checkout are untouched.
- **Evidence and uncertainty:** Formal components come from the existing preserved content model. Six W036 PDFs were copied byte-for-byte and remain labeled with applicability limits. Same-code/name pairings are called navigation clues, not formal equivalences. Missing Ficha status is described as a bounded public-search result.
- **Preservation and consistency:** The six PDF copies have a local hash manifest. The source hashes match their published copies. The source W036 manifest remains unchanged.
- **Validation:** W042 repository validator: 227 CSVs, 132 preserved hashes, 282 links, 0 warnings/errors. Svelte check: 0 errors/warnings; production build passed. W043 post-merge repository validator: same passing counts. Runtime smoke checks from W042 covered both curricula, detail, source page, new PDF, and old-route redirect.
- **Git and process:** Scoped W042 commits and handoff present. W043 spec and error log present. No subagents. Runtime did not expose the primary model/effort; they are recorded unknown rather than inferred.
- **Exceptions:** Applicability of many Ficha 1 versions and formal curricular equivalences remains undetermined. Consequence: the public UI cannot make those claims. Destination: existing P2 documentary reconciliation/human-review records, not this site-release scope.
- **Verdict:** `approved with documented exceptions` for main integration and publication to the existing URL, as authorized by the user.
