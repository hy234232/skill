# Feature Content Rules

Use these rules whenever writing 기능명세서 requirement rows.

Before writing requirement rows, write the required core summary tables from `core_summary_rules.md`. Permission, notification/risk alert, stage/status, and backend-relevant requirement logic must be summarized in `## 2. 핵심 규칙` and then detailed in the body table.

## Fixed Requirement Columns

Always use these exact column names and this exact order for 기능명세서 tables and XLSX outputs:

| 순서 | 항목명 | 작성 기준 |
| --- | --- | --- |
| 1 | `1depth` | 상위 기능 그룹 또는 GNB/메뉴 단위 |
| 2 | `2depth` | 화면, 탭, 하위 메뉴, 기능 도메인 |
| 3 | `3depth` | 구체 화면 주제, 액션, 요구사항 주제 |
| 4 | `요구사항 ID` | `REQ-...` 형식의 고유 ID |
| 5 | `요구사항명` | `화면/기능_핵심 주제` 형식으로 간결하게 작성 |
| 6 | `요청목적` | 사용자가 왜 이 기능을 필요한지 한 문장으로 작성. 원문에 없으면 비워도 됨 |
| 7 | `기능 요구사항` | 사용자가 기대하는 기능 동작을 핵심 bullet로 작성 |
| 8 | `프로세스 요구사항` | 사용자/시스템 흐름을 `→`로 작성 |
| 9 | `화면 요구사항` | 화면에 보여야 하는 UI 요소, 상태, 버튼, 입력 필드 작성 |
| 10 | `보안 요구사항` | 권한, 접근 제한, 수정 가능 범위 등 원문 기반 규칙 작성 |
| 11 | `데이터 요구사항` | 저장/조회해야 하는 원문 기반 데이터 항목 작성 |

Do not rename these columns. In particular, use `요청목적` without `(선택)`.

## Text Quality

- Write concise Korean suitable for 기획자, 개발자, QA, and AI parsing.
- Preserve the user's intent and source terminology.
- Improve grouping, wording, and consistency when helpful.
- Prefer short bullet lines for multi-item cells.
- Use `-` bullets inside cells when listing multiple items.
- Use `→` for process flow.
- Keep each row focused on one screen, action, or requirement topic.
- Group rows by IA path: `1depth > 2depth > 3depth`.
- Keep backend-important logic visible in both places:
  - summarize it in the core summary tables
  - detail it in the requirement rows
- Do not leave permission, notification, risk stage, report, or settings logic only inside scattered body rows when it affects backend structure.

## What Can Be Improved

It is allowed to improve:

- unclear wording
- duplicate or scattered requirements
- IA grouping
- row order
- concise phrasing
- consistency of role names, screen names, and status names that already appear in the source

The improvement must stay inside the source meaning.

## What Must Not Be Invented

Do not invent or add items that are not in the source:

- development code
- pseudo-code
- enum names or enum values
- error codes
- API endpoints or API schemas
- database schema or table/field names
- backend architecture
- frontend component names
- analytics events
- tracking events
- permission models beyond the source
- state machines beyond the source
- policies, restrictions, exceptions, or edge cases not described or directly implied

If content is missing:

- Use `TBD` for metadata or links.
- Leave optional cells blank when acceptable.
- Use `원문 기준 추가 정의 필요` only when the row needs an explicit placeholder.

## Source-Grounded Data Rule

For `데이터 요구사항`, write only data that is clearly required by the source requirement.

Allowed:

- "사용자 ID, 권한 목록, 수정자, 수정시간 저장" when the source says 권한 변경 and 이력 저장.
- "알림 유형, 수신자, 수신시간, 읽음상태 저장" when the source describes 알림 목록 and 수신.

Not allowed:

- adding table names, column names, API payload keys, log schemas, event names, or internal IDs unless supplied by the source.
