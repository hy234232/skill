---
name: feature-generator
description: Create concise Korean 기능명세서 Markdown or XLSX files from raw text, existing XLSX, or MD tables. Use when the user wants a feature spec with 목적·범위, a short 핵심 기획 규칙 table, a 기능명세서 table whose first column is 요구사항 ID, no duplicated FE/BE summaries, and standard XLSX export.
---

# Feature Generator

Create concise Korean 기능명세서 files.

## Output Principle

- Keep the MD short.
- Use easy, clear Korean. Prefer short noun-style endings such as `데이터 출처 정의`, not long `~한다` prose.
- Write only planning information needed for implementation.
- Do not repeat the same rule in both the top section and the table unless it prevents misunderstanding.
- FE/BE-owned details belong in FE/BE documents. Feature MD keeps only planning meaning.

## 문체 규칙 (공통)

이 스킬이 만드는 모든 한국어 산문은 `human-writing` 스킬을 따른다 (`~/.codex/skills/human-writing/SKILL.md`, 저장소 hy0909/skills). 핵심만 요약:

- 한 문장 60자 이내, 생각 하나. 핵심 먼저, 배경은 뒤.
- 개발·디자인을 모르는 사람이 읽는다고 가정한다. 전문용어는 첫 등장에 한 줄로 풀어 쓴다.
- 번역투 금지: `~를 통해`, `~에 있어서`, `~에 의해`, `~되어지다`, `위치해 있다`, `~함에도 불구하고`, `~를 가지고 있다`.
- 상투·기계적 표현 금지: `결론적으로`, `시사하는 바가 크다`, `~하는 것이 중요합니다`, `~할 필요가 있다`, `단순한 ~가 아니라`, `~뿐만 아니라 ~도`, `첫째·둘째·셋째` 나열, 형용사·명사 3개 나열, 문두 `또한/따라서/아울러` 연속, 대시(—), `혁신적인·원활한·강력한·다양한·효과적으로`, `파고들어 봅시다`, `잠재력을 발휘하다`.
- `~습니다`가 세 문장 연속이면 하나는 바꾼다. `-적/-성/-화`는 절반으로.
- `많은·다양한·최근·크게 개선`은 숫자·사례로 바꾼다. 정보가 없으면 지어내지 말고 `TBD` 또는 `[확인 필요]`.
- 비교·대조 가능한 항목은 표로 쓴다. 표로 할지 줄글로 할지 판단이 서지 않으면 사용자에게 묻는다(Claude Code에서는 AskUserQuestion 도구).
- 다 쓴 뒤 한 번 더 읽고 "여전히 AI 같아 보이는 곳"을 한 군데 찾아 고친다.
- 이 스킬의 예외: 표 셀·`목적`·`범위`·요구사항 행은 기존 명사형 종결 규칙(`데이터 출처 정의`)을 유지한다. 어미 변주·도치·문장 길이 변주는 설명 문단에만 적용. 반론·`[내 경험]` 같은 관점 규칙은 명세 문서에 넣지 않는다. 미정 표기는 기존 `TBD` / `원문 기준 추가 정의 필요`를 쓴다.

## MD Structure

Use this order:

1. Header
2. Metadata block
3. Top source links, only when needed
4. `## 1. 목적·범위`
5. `## 2. 핵심 기획 규칙`
6. `## 3. 기능명세서`
7. `## 4. 연관 링크`
8. `## 5. 변경 이력`

Use three `<br>` lines before each `##` heading.

## Top Source Links

- Show Figma source links only when they materially help the reader or the user asks for them.
- When a Figma source exists, place it immediately below the metadata block as a clickable Markdown link.
- Do not put Figma URLs or Figma labels inside the metadata code block because links do not render there.
- Use the original Figma link provided by the user as the source link.
- Prefer the broad source link that gathers the relevant functions and screens in one place.
- Do not create or expose additional Figma links for individual frames, pages, subframes, or MCP-discovered nodes.
- If the Figma frame or page is later deleted, the MD should still rely on the stable user-provided source link, not generated per-frame links.
- Use this format: `> Figma: [서비스명 — 출처명](https://...)`
- If the top Figma source link already appears, do not repeat the same Figma link in `## 4. 연관 링크`.

## 목적·범위

Write only two bullets:

- `목적:` one short noun-style phrase
- `범위:` included screens, data, or rules

Write only `목적` and `범위` bullets.

## 핵심 기획 규칙

Read `references/core_summary_rules.md`.

Default table:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

Rules:

- Max 5 rows unless the user explicitly asks for more.
- One row = one cross-cutting planning rule.
- Include only rules that affect multiple 기능명세서 rows or prevent implementation misunderstanding.
- If there is no meaningful cross-cutting rule, write one `공통` row saying the 기능명세서 table is the source of truth.

## 기능명세서

Read `references/feature_content_rules.md`.

Always use columns in this exact order:

`요구사항 ID`, `1depth`, `2depth`, `3depth`, `요구사항명`, `요청목적`, `기능 요구사항`, `프로세스 요구사항`, `화면 요구사항`, `보안 요구사항`, `데이터 요구사항`

Keep rows concise. Put detailed behavior in the relevant row, not in a repeated narrative section.

## XLSX

- For XLSX output, use `assets/feature_xlsx_template.xlsx`.
- For MD/Table to XLSX, use `scripts/md_table_to_feature_xlsx.py`.
- For XLSX to MD, use `scripts/xlsx_to_feature_md.py`.
- Preserve the standard XLSX design. Read `references/xlsx_design_rules.md` only when creating XLSX.

## Images

- Keep screenshots near the relevant requirement.
- Add a 1px `#D9DEE7` outer border without resizing/cropping/redrawing the original.
- Store assets in `assets/<topic>/`.

## Figma Scroll Frames

- When a Figma frame name contains `scroll` (case-insensitive), always define scrolling in the relevant feature requirement.
- Determine the scroll container from the frame hierarchy and screen layout. Specify the scrolling area, direction, overflow condition, and elements that remain fixed.
- Place the scroll area on the actual content region represented by the named frame; do not automatically apply full-page scrolling.
- Do not omit scrolling only because the mockup does not show a scrollbar.
- If the named frame's location makes scrolling structurally unusual, or the intended scroll container is ambiguous, ask the user whether scrolling there is correct before finalizing the document.

## Naming

- Use concise lowercase kebab-case: `<topic>.md`, `<topic>.xlsx`.
- Do not include `feature`, `기능명세서`, dates, versions, `draft`, or `final`.

## Metadata

- Always write `owner_team: AI Platform Team` in the metadata block.
- Never copy another team name (for example `AI Research team`) from neighboring or older documents. When editing an existing document whose metadata has a different `owner_team`, change it to `AI Platform Team`.

## Guardrails

- Preserve source meaning; do not invent scope.
- Do not invent API, DB, enum, event, state machine, component architecture, or permission models.
- Use `TBD` or `원문 기준 추가 정의 필요` only when needed.
- For Figma references, do not expose raw Figma URLs. Put the real URL behind Markdown link text only when the source link is needed.
- Do not add per-frame, per-page, or per-node Figma links from MCP output. Use only the user-provided broad source link unless the user explicitly asks for a specific link.
- When editing an existing document, preserve every existing change-history row.
- Add the current work as the newest row at the top. Combine changes made on the same date into one complete row unless the user requests separate rows.
- Never delete, shorten, reorder, or rewrite previous history without an explicit user request.
- Write `Codex, hy0909` in change history.
