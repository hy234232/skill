# Feature Content Rules

The `기능명세서` table is the implementation source of truth.

Columns, exact order:

| 순서 | 항목명 | 작성 기준 |
| --- | --- | --- |
| 1 | `요구사항 ID` | `REQ-...` |
| 2 | `1depth` | 상위 기능 그룹 또는 메뉴 |
| 3 | `2depth` | 화면, 탭, 하위 메뉴 |
| 4 | `3depth` | 화면 주제, 액션, 요구사항 주제 |
| 5 | `요구사항명` | 핵심 주제 |
| 6 | `요청목적` | 필요 이유. 없으면 비워도 됨 |
| 7 | `기능 요구사항` | 기능 동작 |
| 8 | `프로세스 요구사항` | 사용자/시스템 흐름. `→` 사용 |
| 9 | `화면 요구사항` | UI 요소, 상태, 버튼, 입력 필드 |
| 10 | `보안 요구사항` | 권한, 접근 제한, 수정 가능 범위 |
| 11 | `데이터 요구사항` | 저장/조회 데이터 |

Writing rules:

- Keep each row focused on one screen/action/rule.
- Use short bullets inside cells.
- Use familiar, direct words that a planner, designer, frontend developer, and backend developer can understand on first read.
- Replace abstract expressions with the actual page, category, and function name.
- In `1depth`, `2depth`, and `3depth`, use the visible page/category/function name whenever the source provides one.
- Avoid ambiguous references such as `해당 화면`, `상위 페이지`, `관련 기능`, `해당 항목`, and `이 버튼`. Repeat the exact name when needed.
- For every changed item, put the before/after pair before the detailed behavior in the relevant cell.
- Use this format: `[페이지명 > 카테고리명 > 기능명] (변경 전) 기존 내용 → (변경 후) 새 내용`.
- When the location is already unambiguous from `1depth`~`3depth`, the bracketed location may be omitted, but the `(변경 전) → (변경 후)` order is mandatory.
- Split multiple changes into separate bullets; do not combine unrelated before/after pairs.
- Prefer noun-style endings where natural.
- Preserve source terminology.
- Remove duplication and merge scattered requirements.
- Do not invent API, DB, enum, FE component, event, analytics, or state machine.
- Keep BE/FE-owned details out unless the user explicitly asks this MD to own them.

## Figma Scroll Mapping

When a Figma frame name contains `scroll` (case-insensitive):

- Treat it as an explicit interaction requirement, not a visual label.
- Use the frame's parent, clipping bounds, siblings, and fixed headers/footers to identify the intended scroll container.
- Write the scroll behavior in the same requirement row as the affected screen.
- `기능 요구사항`: scrolling availability and overflow condition.
- `프로세스 요구사항`: user scroll → content movement → boundary behavior when relevant.
- `화면 요구사항`: exact scroll region, vertical/horizontal direction, and fixed elements.
- Ask the user before writing the final rule when the frame is placed in an implausible area or more than one scroll container is possible.
