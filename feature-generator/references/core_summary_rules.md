# Core Planning Rules

The `핵심 기획 규칙` section is a short planning map.

Use one table:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

Write max 5 rows by default.

Include only:

- rules affecting multiple 기능명세서 rows
- required/optional distinctions
- permission rules that change visible actions
- validation/save timing rules developers can miss
- wording/source-of-truth rules

Do not include:

- repeated row summaries
- FE/BE implementation details
- API/DB/enum/status-machine definitions unless the user explicitly says this MD owns them
- separate 권한/알림/상태/백엔드 summary tables

Fallback row:

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |
| 공통 | 본 문서는 기능명세서 기준 구현 | 전체 | 3. 기능명세서 |
