#!/usr/bin/env python3
"""Check the bounded W016 historical-act data and preserved file identities."""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "administracao/historico/atos-originais"


def rows(name):
    with (BASE / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    for row in rows("manifesto.csv") + rows("checkpoint.csv"):
        path = ROOT / row["local_path"]
        assert path.is_file(), row["local_path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], row["local_path"]
    targets = {row["target_id"]: row for row in rows("registros.csv")}
    assert len(rows("registros.csv")) == 2 and set(targets) == {"COUN19", "P44"}
    assert targets["COUN19"]["status"] == "not_located"
    assert targets["P44"]["status"] == "institutional_reproduction_preserved"
    records = rows("dados-portaria-44.csv")
    assert len(records) == 1
    row = records[0]
    assert (row["evidence_id"], row["pdf_page"], row["annex_row"], row["emec_record"]) == ("W016-P44", "3", "19", "201307170")
    assert row["act_date"] == "2015-01-22" and row["annual_seats_as_printed"] == "30 (trinta)"
    searches = rows("buscas.csv")
    assert sum(r["target_id"] == "COUN19" for r in searches) == 5
    assert sum(r["target_id"] == "P44" for r in searches) == 3
    assert all(r["accessed_at"] and r["terms_or_url"] and r["limits"] for r in searches)
    print("W016: two target statuses, one manifested reproduction, one unverified draft, one annex row and eight bounded attempts checked; errors=0.")


if __name__ == "__main__":
    main()
