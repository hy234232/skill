# Feature Spec Writing Rules

## Goals

- Match the reference 기능명세서's structure and rhythm, not a generic PRD.
- Make the output usable by developers, QA, and AI agents.
- Keep the source meaning intact while converting rough text into implementation-ready rows.

## Row Writing

- `업무그룹`: express IA hierarchy with numbered groups, e.g. `2. SOP 관리 > 2.1 역할별 수신 알림`.
- `요구사항 ID`: continue the existing ID pattern if adding rows. If uncertain, use a clearly sequential provisional ID and note it.
- `요구사항명`: use `페이지/기능_동작` style.
- `요청목적`: one concise reason.
- `기능 요구사항`: what the feature must do.
- `프로세스 요구사항`: event flow, state changes, or save/apply flow.
- `화면 요구사항`: UI elements, buttons, fields, states, tables, tabs.
- `보안 요구사항`: role access, view/edit/action permissions.
- `데이터 요구사항`: stored fields, audit logs, IDs, timestamps.
- `기타 요구사항`: exceptions, constraints, non-default conditions.

## Tone

- Use short Korean business prose.
- Prefer verbs such as `표시`, `저장`, `발송`, `수정 가능`, `제공`, `차단`, `반영`.
- Avoid conversational wording.
- Avoid speculation. If details are missing, use conservative wording such as `필요 시`, `권한 범위 내`, `설정값 기준`.

## Lists In Cells

Use this style for multiple items:

```text
- 위험단계, 위험종류, 위치 표시
- 제한시간 초과 시 재알림 발송
- 처리 이력 저장
```

When placed inside a Markdown table, convert internal newlines to `<br>`:

```markdown
| - 위험단계 표시<br>- 재알림 발송<br>- 이력 저장 |
```

## Preservation Rules

- If the user says "원본 내용은 절대 수정/삭제하지 말고", put original content into a separate table section without summarizing it.
- If editing an existing file, do not normalize unrelated text.
- Keep domain terms exactly unless the user provides replacements.
