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
- Use easy, direct words.
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
