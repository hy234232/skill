# Feature XLSX Design Rules

Use these rules whenever generating a 기능명세서 `.xlsx`.

## Template

- Use `assets/feature_xlsx_template.xlsx` as the workbook design source.
- Sheet name: `기능명세서`.
- Title cell: `A2:C2` merged, value `기능명세서 (Feature Specification)`.
- Freeze pane: `A5`.
- Gridlines: hidden.

## Table Position

- Header row: `5`.
- Data starts at row: `6`.
- Table columns: `A:K`.

## Required Columns

Do not rename, remove, reorder, or add table columns unless the user explicitly requests a schema change.

| Column | Header | Width |
| --- | --- | --- |
| A | `1depth` | `20.0` |
| B | `2depth` | `24.0` |
| C | `3depth` | `30.0` |
| D | `요구사항 ID` | `21.6640625` |
| E | `요구사항명` | `42.83203125` |
| F | `요청목적` | `39.1640625` |
| G | `기능 요구사항` | `74.1640625` |
| H | `프로세스 요구사항` | `71.5` |
| I | `화면 요구사항` | `63.83203125` |
| J | `보안 요구사항` | `48.1640625` |
| K | `데이터 요구사항` | `55.5` |

For the content written under these columns, follow `references/feature_content_rules.md`.

## Header Style

- Font: `Arial`, size `13`, bold.
- Font color: white `#FFFFFF`.
- Fill color: dark charcoal `#111111`.
- Border: thin black.
- Alignment: center, middle, wrap text.
- Row height: `32`.

## Body Style

- Font: `Arial`, size `13`, regular.
- Font color: black `#000000`.
- Border: thin black.
- Alignment: left, top, wrap text.
- Odd data rows: white `#FFFFFF`.
- Even data rows: light gray `#F2F2F2`.
- Minimum body row height: `93.75`.

## Dynamic Row Height

- Never let long text be hidden.
- Estimate wrapped line count per row using column width and internal line breaks.
- Use the larger of:
  - template minimum body height `93.75`
  - estimated wrapped lines multiplied by line-height, plus padding
- Cap only if the user explicitly asks; otherwise expand rows enough for readability.

## Formula And Edit Safety

- Do not write formulas.
- Store all table cells as literal strings.
- Set number format to `@`.
- Set `quotePrefix=True` so `-` bullet edits do not become formulas or cell references.
- Remove data validation restrictions.
- Verify no `#NAME?`, `#VALUE!`, `#REF!`, `#DIV/0!`, or `#N/A` errors remain.
