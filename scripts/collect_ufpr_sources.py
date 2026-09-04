#!/usr/bin/env python3
"""Collect UFPR course documents while preserving provenance and integrity."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
import hashlib
import html
from html.parser import HTMLParser
from pathlib import Path
import re
import urllib.parse
import urllib.request


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._label: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._label = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._label.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href is not None:
            self.links.append((self._href, " ".join(self._label).strip()))
            self._href = None
            self._label = []


def safe_url(url: str) -> str:
    parts = urllib.parse.urlsplit(html.unescape(url).replace("http://", "https://", 1))
    path = urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/%:@")
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "ibm-curriculum-archive/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--codes", required=True, nargs="+")
    args = parser.parse_args()

    source = args.index.read_text(encoding="utf-8")
    link_parser = LinkParser()
    link_parser.feed(source)
    args.output.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)

    planned: list[tuple[dict[str, str], Path, str]] = []
    seen: set[tuple[str, str]] = set()
    for code in args.codes:
        matches = [
            (href, label)
            for href, label in link_parser.links
            if code.casefold() in f"{href} {label}".casefold() and href.lower().endswith(".pdf")
        ]
        for position, (raw_url, label) in enumerate(matches, start=1):
            url = safe_url(raw_url)
            lower = f"{label} {urllib.parse.unquote(url)}".casefold()
            if re.search(r"(?:^|/)2ci\d+", lower) or "ficha 2" in lower:
                kind = "ficha-2"
            elif "ficha 1" in lower or re.search(r"(?:^|/)ci\d+", lower):
                kind = "ficha-1"
            else:
                kind = "documento"
            key = (code, url)
            if key in seen:
                continue
            seen.add(key)
            suffix = f"-{position}" if sum(1 for _, item_label in matches if item_label == label) > 1 else ""
            target = args.output / code / f"{kind}{suffix}.pdf"
            target.parent.mkdir(parents=True, exist_ok=True)
            row = {
                "code": code,
                "kind_in_index": kind,
                "index_label": label,
                "source_url": url,
                "local_path": target.as_posix(),
                "status": "",
                "sha256": "",
                "bytes": "",
            }
            planned.append((row, target, url))

    def download(item: tuple[dict[str, str], Path, str]) -> dict[str, str]:
        row, target, url = item
        try:
            data = fetch(url)
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            target.write_bytes(data)
            row["status"] = "downloaded"
            row["sha256"] = hashlib.sha256(data).hexdigest()
            row["bytes"] = str(len(data))
        except Exception as exc:  # preserve failures in the manifest
            row["status"] = f"failed: {type(exc).__name__}: {exc}"
        return row

    with ThreadPoolExecutor(max_workers=8) as pool:
        rows = list(pool.map(download, planned))

    with args.manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["code", "status"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
