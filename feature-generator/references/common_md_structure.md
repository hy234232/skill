# Common MD Structure

Every feature specification MD must include the following sections in this order.

| 순서 | 항목 | 필수 여부 | 작성 내용 | 필드/구성 | 예시 | 위치 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 헤더 | 필수 | 파일명 + 한 줄 설명 | 문서명, 한 줄 설명 | `# SOP 기능명세서`<br>`건설현장안전 SOP 알림, SOP 관리, SOP 보고서, 권한/수신자 요구사항을 개발자와 AI가 읽기 쉽게 정리한 기능명세서입니다.` | 최상단 |
| 2 | 메타 블록 | 필수 | 문서 식별 및 관리 정보 | `id`, `version`, `status`, `owner_team`, `effective_date` | `id: FEAT-SOP-001`<br>`version: 1.0.0`<br>`status: draft`<br>`owner_team: AI Research team`<br>`effective_date: 2026-06-02` | 상단 |
| 3 | 목적·범위 | 필수 | 이 문서가 왜 존재하는지, 어디까지 다루는지 | 목적, 포함 범위, 제외 범위 | `SOP 관리 기능의 요구사항과 권한 기준을 정의한다.`<br>`포함: 알림, 보고서, 권한`<br>`제외: 결제, 약관` | 상단 |
| 4 | 핵심 규칙 | 필수 | 주요 규칙을 표 또는 트리 형태로 정리 | IA/기능 그룹, 권한 요약, 알림·위험알림 요약, 단계/상태, 백엔드 핵심 로직 요약 | `안전관리자는 위험알림 수신·확인·조치 가능`<br>`보고서 관리자는 SOP 보고서 작성완료 알림 수신·수정 가능` | 상단 |
| 5 | 본문 | 필수 | 문서 유형별 상세 내용 | IA, 요구사항 테이블, 권한, 데이터, 예외 처리 | `기능명세서: IA, 요구사항 테이블, 권한, 데이터, 예외 처리` | 중간 |
| 6 | 연관 링크 | 선택 | 관련 문서, 정책, 기능명세서, 외부 링크 | 관련 PRD, 관련 정책, 관련 기능명세서, 외부 링크 | `관련 PRD: ../A. PRD/prd.md`<br>`관련 정책: ../B. policy/A. system/A-1. access-permission.md`<br>`외부 링크: Figma, Jira, Notion` | 변경 이력 바로 위 |
| 7 | 변경 이력 | 필수 | 최초 작성일, 수정일, 버전별 변경 내용, 작성자 | 최초작성일, 수정일, 버전, 변경 내용(최신순), 작성자 | `최초작성: 2026-06-02 AM 10:00`<br>`v1.0.0: 최초 작성` | 최하단 |

## Required Section Template

````md
# {{문서명}}

{{한 줄 설명}}

```yaml
id: {{문서_ID}}
version: 1.0.0
status: draft
owner_team: AI Research team
effective_date: {{YYYY-MM-DD}}
```

<br>
<br>
<br>

## 1. 목적·범위

- 목적:
- 포함 범위:
- 제외 범위:

<br>
<br>
<br>

## 2. 핵심 규칙

### 2.1 IA / 기능 그룹

| 1depth | 2depth | 3depth | 설명 |
| --- | --- | --- | --- |

<br>
<br>

### 2.2 권한 요약

| 권한 | 해당 사용자(예시) | 주요 역할 | 주요 뷰권한 | 주요 처리 권한 | 제한/예외 |
| --- | --- | --- | --- | --- | --- |

<br>
<br>

### 2.3 알림·위험알림 요약

| 알림/이벤트 | 발송 대상 | 조회 권한 | 처리 권한 | 후속 처리 | 데이터/이력 |
| --- | --- | --- | --- | --- | --- |

<br>
<br>

### 2.4 단계/상태 요약

| 구분 | 명칭 | 기준 | 후속 처리 |
| --- | --- | --- | --- |

<br>
<br>

### 2.5 백엔드 핵심 로직 요약

| 구분 | 핵심 로직 | 권한/대상 | 저장/이력 | 관련 요구사항 |
| --- | --- | --- | --- | --- |

<br>
<br>
<br>

## 3. 본문

### 3.1 요구사항 테이블

| 1depth | 2depth | 3depth | 요구사항 ID | 요구사항명 | 요청목적 | 기능 요구사항 | 프로세스 요구사항 | 화면 요구사항 | 보안 요구사항 | 데이터 요구사항 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

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
| 1.0.0 | {{YYYY-MM-DD}} | 최초 작성 | Codex, 김혜연 |
````

## Change History Author

- When writing a feature specification for the current user, always use `Codex, 김혜연` in the `작성자` column for the initial creation row and every revision row.

## File Naming

- Use the same concise English kebab-case topic for MD and XLSX: `<topic>.md`, `<topic>.xlsx`.
- Omit `feature`, `기능명세서`, dates, versions, status labels, and redundant directory context.
- Match document-specific assets to the same topic: `assets/<topic>/`.
- Example: a project settings specification uses `project-settings.md`, `project-settings.xlsx`, and `assets/project-settings/`.

## Status Values

| 상태 | 의미 | 사용 기준 |
| --- | --- | --- |
| `draft` | 초안 | 작성 중이거나 검토 전인 문서 |
| `active` | 활성 | 확정되어 현재 기준으로 사용하는 문서 |
| `deprecated` | 폐기 예정/비권장 | 히스토리용으로 남기지만 신규 작업 기준으로 사용하지 않는 문서 |

## No Speculative Development Design

- 기능명세서는 요구사항을 정리하는 문서이며, 개발 구조를 상상해서 미리 설계하지 않습니다.
- 원문에 없는 enum, error code, API 구조, DB schema, state machine, class name, component name, backend architecture를 임의로 작성하지 않습니다.
- 원문에 없는 개발 코드, pseudo-code, API endpoint, DB table/field, analytics event, tracking event, 내부 상태머신, 컴포넌트명도 작성하지 않습니다.
- 사용자가 명시한 개발 정보가 있는 경우에만 원문 기반 요구사항으로 정리합니다.

## Required Core Summary Tables

- `권한 요약`, `알림·위험알림 요약`, `단계/상태 요약`, `백엔드 핵심 로직 요약`은 기능명세서 MD에서 항상 작성합니다.
- 권한, 알림, 위험 단계, 보고서, 설정, 저장 이력처럼 개발자가 구조를 잡을 때 필요한 요구사항 로직은 본문에만 흩어두지 말고 핵심 규칙에 표로 요약합니다.
- 핵심 요약은 개발 구조 설계가 아니라 요구사항 요약입니다. 원문에 없는 API, DB, enum, error code, 이벤트명, 내부 상태값은 작성하지 않습니다.
- 원문이 부족해 필수 표를 채울 수 없으면 표를 삭제하지 말고 `원문 기준 추가 정의 필요`로 표시합니다.
