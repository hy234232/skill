# Common MD Structure

Feature MD output must be concise and table-first.

````md
# {{문서명}}

{{한 줄 설명}}

```yaml
id: {{문서_ID}}
version: 1.0.0
status: draft
owner_team: AI Platform Team
effective_date: {{YYYY-MM-DD}}
```

<br>
<br>
<br>

## 1. 목적·범위

- 목적: {{짧은 명사형 문구}}
- 범위: {{포함 화면·데이터·규칙}}

<br>
<br>
<br>

## 2. 핵심 기획 규칙

| 구분 | 핵심 기획 규칙 | 적용 범위 | 요구사항 연결 |
| --- | --- | --- | --- |

<br>
<br>
<br>

## 3. 기능명세서

| 요구사항 ID | 1depth | 2depth | 3depth | 요구사항명 | 요청목적 | 기능 요구사항 | 프로세스 요구사항 | 화면 요구사항 | 보안 요구사항 | 데이터 요구사항 |
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

Rules:

- Write only `목적` and `범위` bullets.
- Do not add IA summary, role summary, alert summary, status summary, or backend summary sections unless the user asks.
- Use easy words and short noun-style endings.
- When editing an existing document, preserve all previous change-history rows.
- Add the current work as the newest row and include every material change made in the task.
- Combine same-day changes into one row by default; split them only when the user requests separate entries.
- Do not rewrite or remove earlier rows without an explicit request.
