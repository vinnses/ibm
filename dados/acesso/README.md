# W015 existing data access package

This directory is a local, reproducible access index for the already-recorded repository snapshot. It is an access aid, not a replacement for the preserved sources and does not claim that every underlying document is available or applicable to a curriculum.

- [`datasets.csv`](datasets.csv) indexes existing repository CSV datasets with path, header, row count, SHA-256, and scope.
- [`source-records.csv`](source-records.csv) retains each recorded source-manifest row, its origin manifest and row, complete original metadata as JSON, local path, URL and hash. Mechanical same-path metadata differences are marked without interpreting them as substantive contradictions. Rows are not deduplicated; a code or title alone does not establish Ficha applicability. Selected display columns are conveniences; original JSON and the origin row retain fields without an equivalent display column.
- [`gaps.csv`](gaps.csv) copies already-recorded human-review and bounded negative-search records, distinguishing institutional access from public documentary gaps.
- [Builder and checker](../../scripts/build_w015_data_access.py) rebuilds or checks the package.

Use `python scripts/build_w015_data_access.py` to rebuild all outputs and `python scripts/build_w015_data_access.py --check` to verify paths, counts, hashes, origins, and nonempty gap coverage.

Integrated snapshot after W024: 115 datasets, 191 curated source-manifest records and 33 curated human-question/search records. Counts are records, not unique documents or unresolved gaps. W022-W024 work-local datasets expose code-specific public Ficha searches for all 37 coded 2011 components, including preserved findings and bounded negative outcomes; they are not folded into the older curated unions. Curriculum-96A applicability remains an institutional-evidence question.
