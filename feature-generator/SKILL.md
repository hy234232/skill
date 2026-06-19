---
name: feature-generator
description: Create Korean 기능명세서 Markdown or XLSX files from raw text, an existing feature XLSX, or a feature MD/table. Use when the user asks to generate a 기능명세서, convert text to feature MD, convert 기능명세서 XLSX to MD, create 기능명세서 XLSX, preserve the standard feature XLSX design, or enforce IA depth columns and common MD sections for feature specifications.
---

# Feature Generator

Use this skill to create a 기능명세서 `.md` or `.xlsx` file. It supports three input modes:

- Text to MD: raw text, pasted notes, screen descriptions, or requirements become a complete 기능명세서 MD.
- XLSX to MD: an existing 기능명세서/요구사항정의서 `.xlsx` becomes a complete 기능명세서 MD.
- MD/Table to XLSX: a 기능명세서 MD or requirements table becomes a styled 기능명세서 XLSX.

## Front Step

Before generating the MD, ask which source mode to use unless the user has already clearly provided one.

Use this Korean prompt:

> 어떤 방식으로 기능명세서.md를 만들까요?

Options:

- `Text to MD`: 텍스트만으로 기능명세서 MD 작성
- `XLSX to MD`: 기능명세서 XLSX를 기능명세서 MD로 변환
- `MD/Table to XLSX`: 기능명세서 MD 또는 테이블을 표준 디자인 XLSX로 변환

If a modal or choice tool is available, present those options. If not, ask the prompt directly. When the user's request is explicit, proceed without asking.

## Required MD Structure

Every output MD must include these sections in this order:

1. Header
2. Metadata block
3. Purpose and scope
4. Core rules
5. Body
6. Related links
7. Change history

Always place `Related links` immediately above `Change history`.

Read `references/common_md_structure.md` when drafting or reviewing the output.
Read `references/feature_content_rules.md` before drafting requirement rows.
Read `references/core_summary_rules.md` before drafting the Core rules section.

## Section Spacing Rule

Use the same heading spacing as the policy-generator skill so feature MD files remain readable in GitHub and Notion.

Before every major level-2 section heading, insert three standalone HTML line breaks:

```md
<br>
<br>
<br>

## 1. 목적·범위
```

Apply this spacing before every `##` heading, including:

- `## 1. 목적·범위`
- `## 2. 핵심 규칙`
- `## 3. 본문`
- `## 4. 연관 링크`
- `## 5. 변경 이력`

Between sibling lower-level headings, insert two standalone HTML line breaks before the next heading. Apply this consistently to repeated `###` and `####` headings:

```md
<br>
<br>

### 2.2 권한 요약
```

Do not insert these spacing tags inside Markdown table cells. When restructuring an existing feature MD, normalize its headings to this rule without adding a change-history row solely for formatting.

## Text To MD Workflow

Use this when the user provides only text or screenshots described in text.

1. Extract pages, functions, roles, permissions, data, states, exceptions, and flows from the text.
2. Fill every required MD section even if the source text is short.
   - Infer concise values from context when possible.
   - Use `TBD` only for information that cannot be inferred safely.
3. Build the body as a feature specification.
   - Include IA / feature group summary.
   - Always include developer-facing core summary tables for permissions, notifications/risk alerts, risk stages/statuses, and backend-relevant requirement logic.
   - Include permissions/roles as a core table. If the source is incomplete, mark missing values as `원문 기준 추가 정의 필요` instead of omitting the table.
   - Include conditional rules for if/then behavior.
   - Include only requirement-level states, data fields, permissions, and exceptions that are stated or directly implied by the source.
   - Include a requirements table.
4. Requirement tables must use the fixed columns and exact header names from `references/feature_content_rules.md`.
5. Requirement tables must use IA depth columns:
   - `1depth`: top-level product area or feature group.
   - `2depth`: page, tab, sub-page, or feature domain.
   - `3depth`: concrete screen, action, or requirement topic.
6. Keep Korean text concise, implementation-oriented, and consistent with the user's source tone. You may improve clarity and grouping, but must not add unprovided scope.

## XLSX To MD Workflow

Use this when the user provides a 기능명세서 or 요구사항정의서 `.xlsx`.

1. Extract table headers and rows from the relevant sheet.
2. Convert the spreadsheet into the required MD structure.
3. Preserve source row order and non-hierarchy cell text.
4. Organize requirements by IA depth.
   - If the source already has `1depth`, `2depth`, and `3depth`, preserve those columns.
   - If the source has one hierarchy column such as `업무그룹`, split it into `1depth`, `2depth`, and `3depth`.
5. Remove trailing empty columns that came only from spreadsheet formatting.
6. Convert internal spreadsheet line breaks to `<br>` inside Markdown table cells.
7. Add the required core summary tables from `references/core_summary_rules.md`.
   - Preserve and summarize any source rows about `권한`, `알림`, `위험알림`, `위험 단계`, `보고서`, and `비계 정합성`.
   - Never drop permission or notification tables because they are backend-facing contract summaries.
   - If a source workbook lacks enough detail for a required core table, include the table and write `원문 기준 추가 정의 필요` in unknown cells.

Use `scripts/xlsx_to_feature_md.py` for deterministic XLSX conversion when suitable.

## MD/Table To XLSX Workflow

Use this when the user asks for `기능명세서`, `엑셀`, `xlsx`, `엑셀파일`, or wants a Markdown 기능명세서 table exported to Excel.

1. Use the standard workbook design saved at `assets/feature_xlsx_template.xlsx`.
2. Use `scripts/md_table_to_feature_xlsx.py` when converting a Markdown 기능명세서 or Markdown table to `.xlsx`.
3. Preserve the standard design exactly:
   - table header color, text color, font, border, alignment, wrap, and row height
   - body font, border, alignment, wrap, odd/even row background colors
   - column widths A-K
   - title row, merged cells, freeze pane, and hidden gridline setting
4. Requirement tables must use columns:
   - `1depth`, `2depth`, `3depth`, `요구사항 ID`, `요구사항명`, `요청목적`, `기능 요구사항`, `프로세스 요구사항`, `화면 요구사항`, `보안 요구사항`, `데이터 요구사항`
5. Never write formulas into the generated XLSX.
6. Store every editable cell as literal text:
   - number format `@`
   - `quotePrefix=True`
   - no data validation restrictions
7. Row height rule:
   - keep the template body row height for normal rows
   - if text is long, increase row height until all wrapped text can be read
   - never clip requirement text because the row is too short

Read `references/xlsx_design_rules.md` before producing a feature XLSX.

## IA Depth Rules

- Use IA depth for both summaries and requirements tables.
- Group page/screen items by actual navigation hierarchy.
- Group page-less items into MECE functional groups such as `알림`, `권한`, `보고서`, `설정`, `데이터`, or another group implied by the source.
- Keep related requirements adjacent within the same `1depth > 2depth > 3depth` path.

## MD Image Rules

- When a 기능명세서 MD includes screenshots or images, keep each image near the requirement or screen section it supports and use a relative path from the MD file.
- Preserve the user's original image content exactly.
- Always add exactly 1px solid light gray `#D9DEE7` as an outer border on all four sides of every image asset before linking it in the MD.
- Add the border outside the original pixels so the canvas becomes exactly 2px wider and 2px taller.
- Never resize, crop, redraw, recolor, sharpen, rewrite text, or recreate the original image.
- This border step is mandatory for every feature MD image unless the user explicitly requests no border.
- Store document-specific images in `assets/<document-topic>/` and verify dimensions and visual output before delivery.

## File Naming Rules

- Name every feature specification Markdown and Excel file using the same concise topic:
  - Markdown: `<topic>.md`
  - Excel: `<topic>.xlsx`
- Use a concise, developer-friendly English topic in lowercase kebab-case.
- Keep only the core feature or page name.
- Do not include document-type words such as `feature`, `feature-spec`, `feature-specification`, `기능명세서`, or `요구사항정의서`.
- Do not include dates, versions, sequence numbers, status words, or format labels such as `v2`, `20260619`, `final`, `draft`, `md`, or `xlsx`.
- Do not add product or category prefixes that repeat the parent-directory context.
- Use the same topic for document-specific assets: `assets/<topic>/`.
- Preserve an existing filename only when it already follows this rule. Otherwise rename the MD/XLSX files and update relative links and asset paths.
- Examples:
  - Project settings feature specification: `project-settings.md`, `project-settings.xlsx`, `assets/project-settings/`
  - SOP risk alert feature specification: `sop-risk-alert.md`, `sop-risk-alert.xlsx`, `assets/sop-risk-alert/`
  - Member invitation feature specification: `member-invitation.md`, `member-invitation.xlsx`, `assets/member-invitation/`

## Output Rules

- Final output is a `.md` file unless the user asks for another format.
- When the feature specification is being written for the current user, always write `Codex, 김혜연` in every change-history `작성자` cell, including the initial creation row and later revisions.
- Apply the `<topic>.md` / `<topic>.xlsx` naming rule to every generated or restructured feature specification.
- If the user asks for a 기능명세서 Excel file or `.xlsx`, use the standard XLSX design from this skill.
- Do not require an XLSX template to create a complete MD from text.
- Do not leave required sections blank.
- Preserve original source meaning; do not delete requirements.
- Do not invent development structures that are not in the source.
- Do not omit core summary tables. MD outputs must always include `권한 요약`, `알림·위험알림 요약`, `위험 단계/상태 요약`, and `백엔드 핵심 로직 요약` when generating a 기능명세서.
- Backend-facing summaries must stay at requirement level. Summarize roles, recipients, view/edit permissions, alert routing, report creation rules, saved history/data items, statuses, and exception behavior only when they appear in or are directly implied by the source.
- Do not create imagined enums, error codes, API shapes, database schemas, state machines, class names, component names, or backend architecture.
- Do not add development code, pseudo-code, error codes, enums, API contracts, DB fields, tracking events, analytics events, or permission models unless the user/source explicitly provides them.
- Do not inflate requirements with speculative behavior. If a field is not provided and cannot be safely inferred from the product context, write `TBD`, leave it blank, or state only `원문 기준 추가 정의 필요`.
- If implementation-level information is explicitly provided by the user, include it as source-provided requirements, not as speculative design.
- Use Markdown tables that paste cleanly into Notion and GitHub.
- If writing to disk, save beside the source file or in the user's requested output directory.
