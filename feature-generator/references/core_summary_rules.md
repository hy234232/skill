# Core Summary Rules

Use these rules whenever generating a 기능명세서 MD.

## Required Core Tables

The `## 2. 핵심 규칙` section must always include developer-facing summary tables. These tables help product, backend, frontend, QA, and AI quickly understand the requirement logic before reading the full body.

Always include these subsections in this order:

1. `### 2.1 IA / 기능 그룹`
2. `### 2.2 권한 요약`
3. `### 2.3 알림·위험알림 요약`
4. `### 2.4 단계/상태 요약`
5. `### 2.5 백엔드 핵심 로직 요약`

Do not omit these tables. If the source lacks enough detail, keep the table and write `원문 기준 추가 정의 필요` in unknown cells.

## Source-Grounded Rule

- Core summaries must summarize requirements, not invent implementation design.
- Do not create imagined API shapes, database schemas, enum values, error codes, state machines, component names, analytics events, tracking events, or backend architecture.
- It is allowed to summarize source-provided logic such as role permissions, recipients, view/edit rights, alert routing, report creation rules, saved history/data items, statuses, and exceptions.
- If a backend-facing logic is important but missing from the source, mark it as `원문 기준 추가 정의 필요`.

## 2.1 IA / 기능 그룹

Use IA depth to show page and feature hierarchy.

| 1depth | 2depth | 3depth | 설명 |
| --- | --- | --- | --- |
| {{상위 메뉴}} | {{화면/탭}} | {{기능/액션}} | {{요약}} |

## 2.2 권한 요약

Always include a role/permission summary table. For general feature documents, use this default format:

| 권한 | 해당 사용자(예시) | 주요 역할 | 주요 뷰권한 | 주요 처리 권한 | 제한/예외 |
| --- | --- | --- | --- | --- | --- |
| {{권한명}} | {{사용자 예시}} | {{주요 역할}} | {{조회 가능 범위}} | {{수정/처리 가능 범위}} | {{제한사항}} |

For construction safety SOP documents, prefer this detailed format when the source includes or implies 위험알림, 보고서, and 비계 정합성:

| 권한 | 해당 사용자(예시) | 주요 역할 | 위험알림 목록/상세 뷰권한 | 위험알림 확인 및 조치 | 보고서 뷰권한 | 보고서 수정 | 비계 정합성 요청/상세 뷰권한 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 안전 관리자 | 현장 안전관리자, 안전보건관리자, 안전감시단, 협력사 안전담당자 | 위험알림 수신·확인·조치(조치내용 기입, 사진 첨부) | 가능 | 가능 | 가능 | 불가 | 불가 |
| 보고서 관리자 | 현장소장, 안전보건관리책임자, 공사/시공 관리자, 본사 또는 발주처 보고 담당자 | SOP 보고서 작성완료 알림 수신·수정 | 가능 | 불가 | 가능 | 가능 | 불가 |
| 시설 관리자 | 비계/가설재 담당자, 시설·장비 관리자, 공무 담당자, 비계 점검 담당자 | 비계 정합성 알림 수신·요청 | 가능 | 불가 | 가능 | 불가 | 가능 |

If the source says a menu is exposed only to a certain role, write that rule above or below the table as a short note. Example:

> 비계 정합성 요청 및 상세 뷰권한은 시설 관리자만 가능하며, 비계 정합성 GNB 카테고리 자체도 시설 관리자에게만 노출됩니다.

## 2.3 알림·위험알림 요약

Always include an alert summary table. This table should capture who receives what, who can view it, who can act on it, and what history/data is saved.

| 알림/이벤트 | 발송 대상 | 조회 권한 | 처리 권한 | 후속 처리 | 데이터/이력 |
| --- | --- | --- | --- | --- | --- |
| {{알림명}} | {{수신 권한/사용자}} | {{목록/상세 조회 가능 권한}} | {{확인/조치/수정 가능 권한}} | {{다음 흐름}} | {{저장되는 원문 기반 항목}} |

For SOP 위험알림, preserve source rules such as:

- 위험알림 Push는 안전 관리자에게 발송
- 위험알림 목록/상세는 안전 관리자, 보고서 관리자, 시설 관리자가 모두 조회 가능
- 제한시간 초과 시 안전 관리자에게 재알림 Push 발송
- 알림 오류 버튼 선택 시 SOP 프로세스 중단 및 이력 저장

## 2.4 단계/상태 요약

Always include a stage/status table when the source includes risk stages, workflow stages, statuses, report statuses, or processing states.

For SOP 위험 단계, use this table when applicable:

| 단계 | 명칭 | 보고서 작성 기준 |
| --- | --- | --- |
| 1단계 | 주의 | 미작성 |
| 2단계 | 위험 | 작업중단 선택 시 작성 |
| 3단계 | 사고발생 | 작성 |

For non-SOP documents, use the default format:

| 구분 | 명칭 | 기준 | 후속 처리 |
| --- | --- | --- | --- |
| {{단계/상태}} | {{표시명}} | {{진입/판단 기준}} | {{다음 처리}} |

## 2.5 백엔드 핵심 로직 요약

Always include a backend-facing requirement logic table. This is not an implementation design table. It must summarize only source-grounded requirement logic.

| 구분 | 핵심 로직 | 권한/대상 | 저장/이력 | 관련 요구사항 |
| --- | --- | --- | --- | --- |
| {{권한/알림/보고서/설정/상태 등}} | {{요구사항 로직 요약}} | {{적용 권한/대상}} | {{원문 기반 저장/이력 항목}} | {{요구사항 ID 또는 IA 경로}} |

Good examples:

- `위험알림` / `AI 감지 시 위험 단계별 알림 생성 및 대상자에게 발송` / `안전 관리자 수신, 전체 권한 조회` / `발송 여부, 수신자, 수신 시간 저장`
- `보고서` / `조치 완료 후 SOP 보고서 자동 작성` / `보고서 관리자 수정 가능` / `수정 이력 저장`
- `프로젝트 설정` / `구성원별 권한 중복 부여 가능` / `프로젝트 관리자 또는 원문 기준 권한` / `사용자 역할, 권한 정보 저장`

Bad examples:

- API endpoint, DB table, column name, enum name, error code, internal event name, or state machine that the source did not provide.
