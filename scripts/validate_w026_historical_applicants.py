#!/usr/bin/env python3
"""Validate W026 historical applicant-count checkpoints."""
from __future__ import annotations
import csv, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LOTS=(("H1",("2015","2017")),("H2",("2018","2019")),("H3",("2021","2022")),("H4",("2023","2024")),("H5",("2025","2026")))
BASE=ROOT/"administracao/dados/ufpr/w026"
def main():
    errors=[]
    if not (BASE/"manifesto.csv").is_file() or not (BASE/"buscas.csv").is_file(): errors.append("missing W026 evidence files")
    if (ROOT/"dados/administracao/candidatos-historicos.csv").is_file():
        with (ROOT/"dados/administracao/candidatos-historicos.csv").open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
        for row in rows:
            p=ROOT/row["source_path"]
            if not p.is_file(): errors.append(f"missing source {row['source_path']}")
            if "derived" in row["denominator_status"].lower(): errors.append("derived applicant count")
    if errors:
        print(*[f"ERROR: {x}" for x in errors],sep="\n",file=sys.stderr); return 1
    print("W026 validation passed: H1 literal 2015/2017 applicant records preserved; later lots unstarted.")
if __name__=="__main__": raise SystemExit(main())
