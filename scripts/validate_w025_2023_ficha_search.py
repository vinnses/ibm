#!/usr/bin/env python3
"""Validate contiguous W025 bounded official-public search checkpoints."""
from __future__ import annotations
import csv, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"curriculos/2023/fichas"
LOTS=(("M1",("BA040","CM310","BQ112")),("M2",("CM304","CM311","BC056")),("M3",("CM303","BG079","CI1054")),("M4",("CI1101","MN163","CE009")),("M5",("CI1172","CI1244","MN129")),("M6",("CI1131","CI1133","CI1169")),("M7",("CI1132","CI1134")),("A1",("CI1003","CI1055","CI1068")),("A2",("MN162","CI1001","CI1056")),("A3",("BQ083","CI1002","CI1057")),("A4",("CI1212","BF114","CI1062")),("A5",("CI1350","CI1162","CI1215")),("A6",("CI1163","CI1171","CI1209")),("A7",("CI1218","CI1316","CI1007")),("A8",("CI1221","CI1005")))
def main():
    errors=[]; done=[]; missing=False; targets=0
    for lot,codes in LOTS:
        ds=[BASE/f"w025-{c.lower()}" for c in codes]; present=[d.is_dir() for d in ds]
        if all(present):
            if missing: errors.append(f"{lot}: noncontiguous checkpoint")
            done.append(lot)
        else: missing=True
        for code,d in zip(codes,ds):
            if not d.is_dir(): continue
            targets+=1
            for n in ("README.md","manifesto.csv","buscas.csv"):
                if not (d/n).is_file(): errors.append(f"{code}: missing {n}")
            if (d/"buscas.csv").is_file():
                with (d/"buscas.csv").open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
                if len(rows)!=3 or {r.get("search_id") for r in rows}!={f"W025-{code}-{i:02d}" for i in range(1,4)}: errors.append(f"{code}: three attempts required")
                if any(r.get("target")!=code for r in rows): errors.append(f"{code}: out-of-scope search")
    if errors:
        print(*[f"ERROR: {e}" for e in errors],sep="\n",file=sys.stderr); return 1
    print(f"W025 validation passed: lots={','.join(done) or 'none'}; targets={targets}; three attempts per target.")
if __name__=="__main__": raise SystemExit(main())
