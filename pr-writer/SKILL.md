---
name: pr-writer
description: Create or improve Korean pull request titles and Markdown bodies from issue details, code changes, diffs, commits, and test evidence. Use when Codex needs to draft, rewrite, review, or complete a PR description that explains the resolved Issue, performed tests, notification deduplication conditions, UI/API change scope, risks, review points, rollback plan, and related Issue linkage. Do not use this skill merely to create or publish a PR on GitHub.
---

# PR Writer

## Goal

Write a review-ready Korean PR title and body that lets a reviewer understand what changed, why it changed, how it was verified, where the impact stops, and how to recover safely.

## Gather Evidence

1. Inspect the user-provided Issue, requirements, diff, commits, changed files, and test output when available.
2. Separate confirmed facts from assumptions. Never invent an Issue number, test result, affected screen/API, deduplication rule, or rollback procedure.
3. If evidence is missing, still produce the most useful draft and mark the exact gap as `확인 필요: ...`. Ask a question only when the missing fact would materially change the PR.
4. Describe tests as performed only when there is evidence they ran and passed. Label unexecuted checks as `미실행` or `권장 검증`.

## Write the PR

Use concise, concrete Korean. Prefer observable behavior and named conditions over broad phrases such as “로직 개선” or “테스트 완료.”

### Title

- Use `제목: [유형] 핵심 변경` unless the repository has a different convention.
- Choose a type that matches the dominant change, such as `기능`, `수정`, `개선`, `리팩터링`, `문서`, or `운영`.
- State the user-visible or operational outcome, not the implementation mechanism alone.

### Required Sections

Keep the following section order and omit none:

```markdown
## 변경 내용

## 구현 이유

## 검증 방법

## 영향 범위와 위험 요소

## 리뷰 포인트

## 관련 Issue
Closes #
```

Fill the sections using these rules:

- `변경 내용`: State the behavior before/after and the main implementation changes. Make the screen, API, background job, database, configuration, and operations scope explicit. Say `화면 변경 없음` or `API 변경 없음` when that boundary matters.
- `구현 이유`: Connect the change to the Issue's user, business, or operational problem. Do not repeat the change list.
- `검증 방법`: List actual unit, integration, end-to-end, or manual checks and their results. Include boundary values and state transitions that could regress. For notification changes, add an explicit `중복 알림 검증: 완료/미검증` bullet with the tested condition.
- `영향 범위와 위험 요소`: Name affected components, compatibility or data risks, and monitoring needs. Add a concrete `롤백:` bullet and state what happens to data or migrations during rollback.
- `리뷰 포인트`: Direct reviewers to the riskiest conditions, boundaries, state transitions, or contracts. Do not duplicate every change bullet.
- `관련 Issue`: Use `Closes #<번호>` only when merging the PR should close the Issue. Use `Refs #<번호>` when it is related but not fully resolved. If unknown, write `확인 필요: 관련 Issue 번호 및 종료 여부` instead of a fabricated number.

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
- 이 스킬의 예외: 필수 섹션 구조와 `확인 필요:` 표기는 그대로 둔다. 각 섹션 안의 문장에 적용. 관점 규칙은 제외.

## Notification Deduplication Check

For alert or notification changes, explicitly cover all of the following even if the answer is `미검증`:

- The exact identity of the “same event” and the state or key used to prevent duplicates.
- The time threshold and its boundary values, including the exact transition point.
- Whether repeated polls, retries, concurrent workers, or process restarts can create another notification.
- When the deduplication state resets, such as recovery, acknowledgement, or expiration.
- Whether a new notification is created after recovery followed by another failure.
- Evidence from tests for duplicate suppression and reset behavior.

Place test evidence in `검증 방법`, storage and flood risks in `영향 범위와 위험 요소`, and delicate conditions in `리뷰 포인트`. For unrelated PRs, do not add artificial notification content.

## Rollback Quality

Avoid vague statements such as “기존 버전으로 되돌린다.” Describe the smallest safe reversal, for example:

- Disable the feature flag or alert rule first.
- Revert the application change while preserving backward-compatible schema changes.
- Revert an API contract and the dependent screen together.
- Stop a background worker before reverting state-handling logic.
- Explain any data cleanup or irreversible migration separately.

If no safe rollback is evident from the input, write `확인 필요: 운영 롤백 절차` and identify the missing decision.

## Final Check

Before returning the draft, verify that it answers these questions:

1. 어떤 Issue를 해결하는가?
2. 실제로 무엇을 테스트했고 결과는 어땠는가?
3. 알림 변경이라면 중복되지 않는 조건과 복구 후 재알림을 검증했는가?
4. 화면과 API를 포함해 어디까지 바뀌었고 어디는 바뀌지 않았는가?
5. 운영 중 문제가 생기면 어떤 순서로 안전하게 되돌리는가?

Return the title and completed Markdown body directly. Do not wrap the entire result in a code fence unless the user asks for copy-only Markdown.
