#!/usr/bin/env python3
"""Convert a feature XLSX into a required-section Korean feature MD."""

from __future__ import annotations

import argparse
import re
import zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def col_to_index(cell_ref: str) -> int:
    letters = re.match(r"[A-Z]+", cell_ref or "")
    if not letters:
        return 0
    value = 0
    for char in letters.group(0):
        value = value * 26 + (ord(char) - 64)
    return value - 1


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    return ["".join(node.text or "" for node in item.findall(".//main:t", NS)) for item in root.findall("main:si", NS)]


def workbook_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    with zipfile.ZipFile(path) as zf:
        shared = read_shared_strings(zf)
        root = ET.fromstring(zf.read("xl/worksheets/sheet1.xml"))
        for row in root.findall(".//main:sheetData/main:row", NS):
            values: list[str] = []
            for cell in row.findall("main:c", NS):
                index = col_to_index(cell.attrib.get("r", ""))
                while len(values) <= index:
                    values.append("")
                cell_type = cell.attrib.get("t")
                if cell_type == "s":
                    raw = cell.findtext("main:v", default="", namespaces=NS)
                    values[index] = shared[int(raw)] if raw.isdigit() and int(raw) < len(shared) else ""
                elif cell_type == "inlineStr":
                    values[index] = "".join(t.text or "" for t in cell.findall(".//main:t", NS))
                else:
                    values[index] = cell.findtext("main:v", default="", namespaces=NS)
            if any(value.strip() for value in values):
                rows.append(values)
    width = max((len(row) for row in rows), default=0)
    return [row + [""] * (width - len(row)) for row in rows]


def strip_depth_number(value: str) -> str:
    value = value.strip()
    parts = value.split(" ", 1)
    if len(parts) == 2 and re.match(r"^\d+(?:\.\d+)*\.?$", parts[0]):
        return parts[1].strip()
    return value


def split_ia_group(group: str, requirement_name: str) -> tuple[str, str, str]:
    parts = [strip_depth_number(part) for part in group.replace("&gt;", ">").split(">")]
    depth1 = parts[0] if len(parts) > 0 else ""
    depth2 = parts[1] if len(parts) > 1 else ""
    if "_" in requirement_name:
        depth3 = requirement_name.split("_", 1)[1].strip()
    elif len(parts) > 2:
        depth3 = parts[2]
    else:
        depth3 = requirement_name.strip()
    return depth1, depth2, depth3


def remove_trailing_empty_columns(rows: list[list[str]]) -> list[list[str]]:
    if not rows:
        return rows
    while rows and rows[0] and all(row and not row[-1].strip() for row in rows):
        rows = [row[:-1] for row in rows]
    return rows


def normalize_ia_rows(rows: list[list[str]]) -> list[list[str]]:
    rows = remove_trailing_empty_columns(rows)
    if not rows:
        return rows
    header_index = next(
        (
            i
            for i, row in enumerate(rows)
            if any(cell.strip() in {"업무그룹", "그룹", "기능 그룹", "1depth"} for cell in row)
            and any(cell.strip() == "요구사항 ID" for cell in row)
        ),
        0,
    )
    rows = rows[header_index:]
    headers = [cell.strip() for cell in rows[0]]
    if headers[:3] == ["1depth", "2depth", "3depth"]:
        return rows
    hierarchy_index = next((i for i, header in enumerate(headers) if header in {"업무그룹", "그룹", "기능 그룹"}), None)
    if hierarchy_index is None:
        return rows
    req_name_index = next((i for i, header in enumerate(headers) if header == "요구사항명"), None)
    new_headers = headers[:hierarchy_index] + ["1depth", "2depth", "3depth"] + headers[hierarchy_index + 1 :]
    normalized = [new_headers]
    for row in rows[1:]:
        padded = row + [""] * (len(headers) - len(row))
        req_name = padded[req_name_index] if req_name_index is not None and req_name_index < len(padded) else ""
        depth1, depth2, depth3 = split_ia_group(padded[hierarchy_index], req_name)
        normalized.append(padded[:hierarchy_index] + [depth1, depth2, depth3] + padded[hierarchy_index + 1 :])
    return remove_trailing_empty_columns(normalized)


def md_cell(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "<br>")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .strip()
    )


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return "_원본 테이블 데이터가 없습니다._"
    header = [cell or f"컬럼{i + 1}" for i, cell in enumerate(rows[0])]
    lines = [
        "| " + " | ".join(md_cell(cell) for cell in header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(md_cell(cell) for cell in row) + " |")
    return "\n".join(lines)


def column_index(headers: list[str], name: str) -> int | None:
    return next((i for i, header in enumerate(headers) if header == name), None)


def ia_summary(rows: list[list[str]]) -> str:
    if not rows or rows[0][:3] != ["1depth", "2depth", "3depth"]:
        return "_IA 기준 분류 정보가 없습니다._"
    seen: set[tuple[str, str, str]] = set()
    lines = ["| 1depth | 2depth | 3depth | 설명 |", "| --- | --- | --- | --- |"]
    for row in rows[1:]:
        depth = tuple((row + ["", "", ""])[:3])
        if depth in seen:
            continue
        seen.add(depth)
        lines.append(f"| {md_cell(depth[0])} | {md_cell(depth[1])} | {md_cell(depth[2])} | 요구사항 참조 |")
    return "\n".join(lines)


def core_rules(rows: list[list[str]]) -> str:
    if not rows:
        return "_핵심 규칙은 원본 기준으로 확인 필요_"
    headers = rows[0]
    req_index = column_index(headers, "기능 요구사항")
    security_index = column_index(headers, "보안 요구사항")
    data_index = column_index(headers, "데이터 요구사항")
    lines = ["| 구분 | 핵심 규칙 |", "| --- | --- |"]
    if req_index is not None:
        sample = next((row[req_index] for row in rows[1:] if req_index < len(row) and row[req_index].strip()), "")
        if sample:
            lines.append(f"| 기능 | {md_cell(sample[:160])} |")
    if security_index is not None:
        sample = next((row[security_index] for row in rows[1:] if security_index < len(row) and row[security_index].strip()), "")
        if sample:
            lines.append(f"| 권한/보안 | {md_cell(sample[:160])} |")
    if data_index is not None:
        sample = next((row[data_index] for row in rows[1:] if data_index < len(row) and row[data_index].strip()), "")
        if sample:
            lines.append(f"| 데이터 | {md_cell(sample[:160])} |")
    return "\n".join(lines) if len(lines) > 2 else "_핵심 규칙은 원본 기준으로 확인 필요_"


def safe_id(title: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "-", title).strip("-")
    return f"FEAT-{cleaned.upper()}" if cleaned else "FEAT-TBD"


def default_output_path(source: Path) -> Path:
    """Use the source topic as-is; callers must provide a concise topic output for verbose sources."""
    return source.with_suffix(".md")


def build_markdown(source: Path, rows: list[list[str]]) -> str:
    title = source.stem
    today = date.today().isoformat()
    rows = normalize_ia_rows(rows)

    return f"""# {title}

{source.name} 기반 기능명세서입니다.

```yaml
id: {safe_id(title)}
version: 1.0.0
status: draft
owner_team: AI Research team
effective_date: {today}
```

<br>
<br>
<br>

## 1. 목적·범위

- 목적: 원본 기능명세서 Excel 내용을 개발자와 AI가 참조하기 쉬운 Markdown 구조로 정리합니다.
- 포함 범위: IA, 요구사항, 프로세스, 화면, 권한/보안, 데이터 요구사항.
- 제외 범위: 원본에 명시되지 않은 정책, 결제, 법무 항목.

<br>
<br>
<br>

## 2. 핵심 규칙

{core_rules(rows)}

<br>
<br>
<br>

## 3. 본문

### 3.1 IA / 기능 그룹

{ia_summary(rows)}

<br>
<br>

### 3.2 요구사항 테이블

{md_table(rows)}

<br>
<br>
<br>

## 4. 연관 링크

| 구분 | 링크 |
| --- | --- |
| 관련 PRD | TBD |
| 관련 정책 | TBD |
| 관련 기능명세서 | TBD |
| 외부 링크 | TBD |

<br>
<br>
<br>

## 5. 변경 이력

| 버전 | 일자 | 변경 내용 | 작성자 |
| --- | --- | --- | --- |
| 1.0.0 | {today} | 기능명세서 MD 변환 | Codex, 김혜연 |
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_xlsx", type=Path)
    parser.add_argument("output_md", type=Path, nargs="?")
    args = parser.parse_args()
    output = args.output_md or default_output_path(args.input_xlsx)
    rows = workbook_rows(args.input_xlsx)
    output.write_text(build_markdown(args.input_xlsx, rows), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
