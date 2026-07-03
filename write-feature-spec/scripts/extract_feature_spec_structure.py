#!/usr/bin/env python3
"""Print a compact structure summary for a Markdown or XLSX feature spec."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def clean(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def markdown_summary(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    print("# Headings")
    for line in text.splitlines():
        if line.startswith("#"):
            print(line)
    print("\n# Markdown table headers")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|\s*:?-{3,}", lines[i + 1]):
            print(line)


def shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    strings: list[str] = []
    for si in root.findall("main:si", NS):
        parts = [t.text or "" for t in si.findall(".//main:t", NS)]
        strings.append("".join(parts))
    return strings


def cell_value(cell: ET.Element, strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    value = cell.find("main:v", NS)
    if value is None:
        inline = cell.find("main:is", NS)
        if inline is not None:
            return clean("".join(t.text or "" for t in inline.findall(".//main:t", NS)))
        return ""
    raw = value.text or ""
    if cell_type == "s":
        try:
            return clean(strings[int(raw)])
        except (ValueError, IndexError):
            return raw
    return clean(raw)


def xlsx_summary(path: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        strings = shared_strings(zf)
        sheet_names = sorted(name for name in zf.namelist() if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"))
        for sheet_name in sheet_names[:3]:
            print(f"# {sheet_name}")
            root = ET.fromstring(zf.read(sheet_name))
            non_empty: list[list[str]] = []
            for row in root.findall(".//main:row", NS):
                values = [cell_value(cell, strings) for cell in row.findall("main:c", NS)]
                if any(values):
                    non_empty.append(values)
                if len(non_empty) >= 12:
                    break
            for row in non_empty:
                print(" | ".join(row[:12]))
            print()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: extract_feature_spec_structure.py <reference.md|reference.xlsx>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1
    if path.suffix.lower() in {".md", ".markdown"}:
        markdown_summary(path)
    elif path.suffix.lower() == ".xlsx":
        xlsx_summary(path)
    else:
        print(f"Unsupported file type: {path.suffix}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
