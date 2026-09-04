# Review Specification

## Review dimensions

1. **Scope:** deliverables match the approved work unit and do not silently expand it.
2. **Evidence:** every material claim traces to an appropriate preserved source.
3. **Historical validity:** versions and curriculum applicability are not inferred from names or codes alone.
4. **Quantitative validity:** denominators, units, cohorts, annual periods, and transformations are explicit.
5. **Preservation:** manifests contain stable paths, URLs, dates, SHA-256, and status.
6. **Reproducibility:** scripts and documented commands recreate derived outputs where feasible.
7. **Consistency:** internal links, hashes, cross-references, and summary counts agree.
8. **Uncertainty:** gaps, negative searches, conflicts, and provisional conclusions are visible.
9. **Git hygiene:** the branch has a known base, scoped commits, and no unrelated changes.

## Required verdict

Use one verdict:

- `approved for integration`
- `approved with documented exceptions`
- `changes required`
- `blocked`

Every exception must name its consequence and roadmap destination. A review does not authorize integration unless the user or current work specification explicitly includes integration.
