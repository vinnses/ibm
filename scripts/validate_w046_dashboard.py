"""Check the W046 data release and a running prefixed Dash service."""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import json
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analises/data"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_files() -> None:
    release = json.loads((DATA / "release.json").read_text(encoding="utf-8"))
    csv_path = DATA / "formal_components.csv"
    assert sha256(csv_path) == release["csv_sha256"]
    with csv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == release["row_count"] == 80
    assert sum(row["curriculum_year"] == "2011" for row in rows) == 37
    assert sum(row["curriculum_year"] == "2023" for row in rows) == 43
    assert len({(row["curriculum_year"], row["component_code"]) for row in rows}) == 80
    assert sum(row["component_kind"] == "TCC alternativa" for row in rows) == 4
    for row in rows:
        assert row["recommended_period"] in {str(i) for i in range(1, 9)}
        assert row["source_document_id"] in {
            "document-2011-resolution-34-2010", "document-2023-resolution-75-22"
        }
    for item in release["generated_from"]:
        assert sha256(ROOT / item["inventory"]) == item["inventory_sha256"]
        assert sha256(ROOT / item["formal_source"]) == item["formal_source_sha256"]
    for item in release["additional_2023_creation_acts"]:
        assert sha256(ROOT / item["path"]) == item["sha256"]
    with (ROOT / "analises/sources/manifest.csv").open(encoding="utf-8", newline="") as handle:
        for source in csv.DictReader(handle):
            assert sha256(ROOT / source["local_path"]) == source["sha256"]
    with (ROOT / "infrastructure/router/sources/manifest.csv").open(encoding="utf-8", newline="") as handle:
        for source in csv.DictReader(handle):
            assert sha256(ROOT / source["local_path"]) == source["sha256"]


def get(base: str, path: str) -> tuple[int, bytes]:
    with urllib.request.urlopen(base + path, timeout=15) as response:
        return response.status, response.read()


def post(base: str, payload: dict) -> dict:
    request = urllib.request.Request(
        base + "/analises/_dash-update-component",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        assert response.status == 200
        return json.load(response)


def verify_http(base: str) -> None:
    for path in ("/analises/", "/analises/health", "/analises/_dash-layout",
                 "/analises/_dash-dependencies", "/analises/assets/style.css"):
        status, body = get(base, path)
        assert status == 200 and body, path
    dependencies = json.loads(get(base, "/analises/_dash-dependencies")[1])
    assert len(dependencies) == 2
    for year, expected_count in (("2011", 37), ("2023", 43)):
        view = post(base, {
            "output": dependencies[0]["output"],
            "outputs": [
                {"id": "period-chart", "property": "figure"},
                {"id": "period-table", "property": "children"},
                {"id": "row-count", "property": "children"},
            ],
            "inputs": [{"id": "grade", "property": "value", "value": year}],
            "state": [], "changedPropIds": ["grade.value"],
        })["response"]
        assert f"{expected_count} componentes" in view["row-count"]["children"]
        bars = view["period-chart"]["figure"]["data"]
        assert len(bars) == 1 and bars[0]["name"] == year
        values = bars[0]["y"]
        if isinstance(values, dict):
            assert values["dtype"] == "i1"
            values = base64.b64decode(values["bdata"])
        assert sum(values) == expected_count
        download = post(base, {
            "output": "download.data",
            "outputs": {"id": "download", "property": "data"},
            "inputs": [{"id": "download-button", "property": "n_clicks", "value": 1}],
            "state": [{"id": "grade", "property": "value", "value": year}],
            "changedPropIds": ["download-button.n_clicks"],
        })["response"]["download"]["data"]
        assert download["filename"] == f"componentes-formais-{year}.csv"
        downloaded = list(csv.DictReader(io.StringIO(download["content"])))
        assert len(downloaded) == expected_count
        assert all(row["curriculum_year"] == year for row in downloaded)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", help="Running service base origin, e.g. http://127.0.0.1:5186")
    args = parser.parse_args()
    verify_files()
    if args.base_url:
        verify_http(args.base_url.rstrip("/"))
    print("W046 dashboard validation passed" + (" (HTTP and callbacks)" if args.base_url else " (files)"))
