# Formal-component distribution example

This is a deliberately small Dash analysis, not a curricular evaluation. Its
question is: how many **coded components** are listed in each recommended
period of the distinct formal 2011 and 2023 curricula? A row represents one
code in one curriculum. The public selector filters the chart, period table,
and CSV download to 2011, 2023, or both.

`data/formal_components.csv` is derived deterministically from the two
repository inventories by `scripts/build_demo_data.py`. Its release metadata
records source paths, SHA-256 hashes, row counts, unit and exclusions. The
original resolutions and creation acts remain unchanged in `curriculos/`.
Regenerate and check from the repository root:

```bash
python analises/scripts/build_demo_data.py
python scripts/validate_w046_dashboard.py
```

The 2011 inventory contributes 37 coded components; its four code-free elective
spaces are excluded, so period 8 has zero *within this recorte*. The 2023
inventory contributes 43 coded components, including four alternative TCC
codes. Those alternatives are not four simultaneous completion requirements.
The broad formal elective catalogue is excluded. The chart describes formal
periodization, not teaching actually delivered in a semester, content quality,
course equivalence, or the relative curricular merit of either version.

The dashboard uses a real route prefix (`/analises/`). The reverse proxy
preserves that prefix and forwards only this path to the internal Dash service;
the rest of the public origin remains on SvelteKit. The Dash container has no
public/host port. `scripts/validate_w046_dashboard.py --base-url URL` checks
health, assets, callbacks and the filtered CSV through a running origin.
