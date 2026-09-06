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
    manifest={}
    if (BASE/"manifesto.csv").is_file():
        with (BASE/"manifesto.csv").open(encoding="utf-8", newline="") as f:
            manifest={row["local_path"]: row for row in csv.DictReader(f)}
        for path, row in manifest.items():
            p=ROOT/path
            if not p.is_file(): errors.append(f"missing manifest source {path}")
            elif hashlib.sha256(p.read_bytes()).hexdigest() != row["sha256"]: errors.append(f"source hash mismatch {path}")
    if (ROOT/"dados/administracao/candidatos-historicos.csv").is_file():
        with (ROOT/"dados/administracao/candidatos-historicos.csv").open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
        for row in rows:
            if row["outcome_status"] not in {"preserved_literal", "not_located"}: errors.append(f"invalid outcome {row['record_id']}")
            if row["outcome_status"] == "preserved_literal" and not row["applicant_count"]: errors.append(f"missing literal count {row['record_id']}")
            if row["outcome_status"] == "not_located" and row["applicant_count"]: errors.append(f"count on no-source record {row['record_id']}")
            if row["source_path"]:
                p=ROOT/row["source_path"]
                if not p.is_file(): errors.append(f"missing source {row['source_path']}")
                elif row["source_path"] not in manifest: errors.append(f"unmanifested source {row['source_path']}")
            if "derived" in row["denominator_status"].lower(): errors.append("derived applicant count")
    if errors:
        print(*[f"ERROR: {x}" for x in errors],sep="\n",file=sys.stderr); return 1
    print(f"W026 validation passed: {len(rows)} applicant/gap records with literal-source and no-source statuses checked.")
if __name__=="__main__": raise SystemExit(main())
