---
name: policy-generator
description: Create Korean policy Markdown documents from raw text, notes, existing MD files, or screenshots. Use when the user asks to write, restructure, or convert a policy document into the standard 7-section policy format for system, billing, legal, or operational rules.
---

# Policy Generator

Use this skill to create or restructure Korean policy `.md` files. A policy document defines reusable rules, conditions, exceptions, and display/operation standards that product, design, frontend, backend, QA, and AI can all reference.

## When To Use

Use this skill when the user asks for:

- 정책 문서 작성
- policy MD 작성
- 기존 MD를 정책 문서 구조로 재작성
- 시스템/알림/권한/데이터/API/요금/법무/운영 정책 정리
- 정책 문서에 표준 7단 구조 적용

## Required 7-Section Structure

Every policy MD must include these sections in this order:

| 순서 | 항목 | 필수 여부 | 작성 내용 | 위치 |
| --- | --- | --- | --- | --- |
| 1 | 헤더 | 필수 | 문서명 + 한 줄 설명 | 최상단 |
| 2 | 메타 블록 | 필수 | `id`, `version`, `status`, `owner_team`, `effective_date`, `category` | 상단 |
| 3 | 목적·범위 | 필수 | 목적, 포함 범위, 제외 범위 | 상단 |
| 4 | 핵심 규칙 | 필수 | 정책 요약, 적용 대상, 조건별 규칙, 예외/주의사항 | 상단 |
| 5 | 본문 | 필수 | 정책 상세 기준, 화면/운영 예시, 표기 방식, 데이터 기준 | 중간 |
| 6 | 연관 링크 | 선택 | 관련 PRD, 관련 정책, 관련 기능명세서, 외부 링크 | 변경 이력 바로 위 |
| 7 | 변경 이력 | 필수 | 버전, 일자, 변경 내용, 작성자 | 최하단 |

## Section Spacing Rule

For readability in GitHub and Notion, insert three HTML line breaks before every major level-2 section heading.

Use this spacing before each `##` heading:

```md
<br>
<br>
<br>

## 1. 목적·범위
```

Apply the same spacing before:

- `## 1. 목적·범위`
- `## 2. 핵심 규칙`
- `## 3. 본문`
- `## 4. 연관 링크`
- `## 5. 변경 이력`

For sibling lower-level headings, insert two HTML line breaks before the next heading so same-depth sections are visually separated. Apply this to similar hierarchy levels throughout the document, including `### 3.1` → `### 3.2` and repeated `####` subsections.

Use this spacing before sibling `###` and `####` headings:

```md
<br>
<br>

### 3.2 테이블 컴포넌트 공통 시간 표기 방식
```

Use this section template:

```md
# {{정책 문서명}}

{{한 줄 설명}}

```yaml
id: {{POL-...}}
version: 1.0.0
status: draft
owner_team: AI Research team
effective_date: {{YYYY-MM-DD}}
category: {{system | billing | legal | operation}}
```

<br>
<br>
<br>

## 1. 목적·범위

| 구분 | 내용 |
| --- | --- |
| 목적 |  |
| 포함 범위 |  |
| 제외 범위 |  |

<br>
<br>
<br>

## 2. 핵심 규칙

### 2.1 정책 요약

### 2.2 적용 대상

### 2.3 조건별 정책

### 2.4 예외·주의사항

<br>
<br>
<br>

## 3. 본문

<br>
<br>
<br>

## 4. 연관 링크

<br>
<br>
<br>

## 5. 변경 이력
```

## Metadata Rules

- `id`: Use `POL-{{CATEGORY}}-{{TOPIC}}-001` when no ID is provided.
  - system: `POL-SYS-...`
  - billing: `POL-BIL-...`
  - legal: `POL-LEG-...`
  - operation: `POL-OPS-...`
- `version`: Default to `1.0.0`.
- `status`: Use `draft`, `active`, or `deprecated`.
- `owner_team`: Default to `AI Research team` unless provided.
- `effective_date`: Use the current date or the user-provided date.
- `category`: Use one of `system`, `billing`, `legal`, `operation`.

## Change History Author Rules

- For every policy document created or modified at 김혜연's request, always write `Codex, 김혜연` in the `작성자` column.
- Apply this author value to all change-history rows created or normalized during the task.
- Do not use `AI Research team`, `개발팀`, or `Codex` alone as the change-history author for 김혜연's policy documents.

## File Naming Rules

- Name every policy Markdown file using `<topic>.md`.
- Use a concise, developer-friendly English topic in lowercase kebab-case.
- Do not include `policy` in the filename because the parent directory already identifies the document type.
- Do not add category, sequence, or document-type prefixes or suffixes that repeat directory or file context, such as `policy-a.`, `system-`, `policy.system.`, `-policy`, or similar forms.
- Preserve an existing filename only when it already follows `<topic>.md` without the word `policy`; otherwise rename it and update all internal links and asset paths that reference the old name.
- Examples:
  - Permission policy: `permission.md`
  - Notification time policy: `notification-time.md`
  - Notification settings policy: `notification-settings.md`
- For document-specific assets, use `assets/<topic>/` so the asset folder matches the Markdown filename without `.md`.

## Core Rules Requirements

The `## 2. 핵심 규칙` section must summarize policy logic before the detailed body.

Always include:

- `### 2.1 정책 요약`: 3-5 bullet points or a compact table of the most important rules.
- `### 2.2 적용 대상`: which screens, components, users, roles, or systems the policy applies to.
- `### 2.3 조건별 정책`: if/then style rules for conditions, thresholds, states, time windows, permissions, or display formats.
- `### 2.4 예외·주의사항`: exceptions, fallback behavior, exclusions, and non-goals.

For system policies, prefer tables with these columns when relevant:

| 정책 영역 | 기준 | 적용 대상 | 결과/표기 | 예외 |
| --- | --- | --- | --- | --- |

For condition policies, prefer:

| 조건 | 정책 | 예시 | 비고 |
| --- | --- | --- | --- |

## Body Rules

- Preserve the source meaning and source examples.
- Keep policy rules concise and testable.
- Use tables for thresholds, display formats, permissions, routing rules, and conditional behavior.
- For compact explanatory rule groups such as principles, exceptions, and rationale, use a normal Markdown blockquote so the group is visually tied together with a left vertical line. Do not use GitHub/Notion special callout labels.
- Keep the explanatory text itself; only remove callout labels when converting existing callouts.
- Use screenshots/images only as references; the text policy must still be understandable without images.
- Keep images near the section they support.
- Use relative image paths from the MD file location.
- Whenever adding or replacing any screenshot or image in a policy MD, always preserve the user's original image content and apply the standard outer border directly to the image asset: exactly 1px solid light gray `#D9DEE7` on all four sides.
- The border must be added outside the original pixels, increasing the canvas by exactly 2px in width and 2px in height. Never resize, crop, redraw, recolor, sharpen, rewrite text, or recreate the original image.
- This image-border step is mandatory for every policy MD image, including user-provided originals. Skip it only when the user explicitly requests no border.
- Verify the bordered asset dimensions and visually inspect it before linking it in the MD.
- Do not rely on inline CSS because GitHub may strip style attributes. Do not use a Markdown or HTML table solely for image borders because table cells add visible padding.

## Policy Writing Rules

- Write in Korean unless the user asks otherwise.
- Use consistent terms across the document.
- Prefer noun phrases for purpose/scope values.
- Avoid speculative implementation details.
- Do not invent API endpoints, DB schemas, enum names, error codes, tracking events, internal state machines, or backend architecture.
- If source information is missing, write `TBD` or `원문 기준 추가 정의 필요`.
- Do not fabricate related links. In `## 4. 연관 링크`, include only links explicitly provided by the user/source; otherwise write `TBD`.

## Image Path Rules

When a policy uses images, place them in a document-specific assets folder:

```text
policy/
└── system/
    ├── notification-time.md
    └── assets/
        └── notification-time/
            ├── image_1.png
            └── image_2.png
```

Reference images from the policy MD with relative paths:

```md
![](./assets/notification-time/image_1.png)
```

For image borders, edit the image asset so it contains a 1px light gray outer border, then render it with normal Markdown:

```md
![이미지 설명](./assets/notification-time/image_1.png)
```

Recommended border color: `#D9DEE7`. Apply the border as the final asset step after copying the user-provided source image into the document assets folder. Do not edit the screenshot content itself.

## Output Rules

- Final output is a `.md` file unless the user asks for another format.
- Apply the `<topic>.md` naming rule to every generated or restructured policy document and omit `policy` from the filename.
- Do not overwrite the source unless the user explicitly asks.
- If writing to disk, save beside the source file or in the user's requested output directory.
