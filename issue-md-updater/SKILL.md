---
name: issue-md-updater
description: Update existing Markdown documentation from GitHub issues or issue URLs. Use when Codex needs to read an issue, identify affected MD documents, merge the issue's additions/deletions/changes into existing feature or policy docs, preserve unrelated work, update version/change history, commit only intended files, and optionally prepare a PR from a working branch such as plan to main.
---

# Issue MD Updater

## Overview

Use this skill when a user asks to reflect one or more GitHub issues into existing Markdown documentation, especially product planning docs under a working branch such as `plan`.

## Workflow

1. Confirm the working branch and scope.
   - If the user says `plan only`, never merge to `main` and never push `main`.
   - If the target is a future PR to `main`, explain whether the working branch should be updated from `origin/main`.
   - Preserve unrelated local changes, untracked files, and stashes unless the user explicitly names them.

2. Read the source issue completely.
   - Use `gh issue view <number> --repo <owner>/<repo>` when available.
   - Include issue title, body, checklists, comments, reviewers, and linked docs when they change requirements.
   - Treat `확인 필요`, expected problems, and open questions as unresolved unless the issue states the final decision.

3. Update the branch safely.
   - Fetch the relevant remotes first.
   - Pull the working branch with `--ff-only`.
   - If the PR base branch has advanced and the user wants a clean branch for PR, fast-forward or merge the base into the working branch only when that is within the user's requested workflow.
   - Never use destructive reset/checkout commands without explicit permission.

4. Find affected Markdown files.
   - Use `rg` with exact issue terms and likely synonyms.
   - Search both feature docs and policy docs when the issue changes behavior that affects product, permission, notification, UI, or backend-facing rules.
   - Do not edit docs that only match historical change-log rows unless current behavior text is also affected.

5. Merge the issue into existing docs.
   - Keep existing document structure and terminology.
   - Delete obsolete feature text, add new behavior, and update changed rules in the most local section first, then summary tables and requirement rows.
   - Keep feature docs aligned with the `feature-generator` structure and policy docs aligned with the `policy-generator` structure when those skills are available.
   - Use `원문 기준 추가 정의 필요` for unresolved decisions instead of inventing implementation details.
   - Update version metadata and add a change-history row using `Codex, 김혜연` when working for 김혜연.

6. Validate consistency.
   - Run `rg` for stale terms that should have been removed or changed.
   - Run `git diff --check`.
   - Inspect the diff and ensure only intended files are staged.
   - Keep unrelated untracked files out of the commit.

7. Commit, push, and PR only as requested.
   - Commit only the affected files.
   - Push only the requested branch.
   - If a PR is requested, summarize changes by issue number and request the named reviewers.
   - Do not merge the PR unless the user explicitly asks to merge.

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
- 이 스킬의 예외: 기존 문서의 용어·구조·문장은 유지하고, 새로 추가하거나 고쳐 쓰는 문장에만 적용한다.

## Issue-to-doc mapping hints

- UI button/state issues usually affect feature specs and may also affect permission or notification policies.
- Notification duplication issues usually affect both notification policy and the feature spec's requirements table.
- Permission issues usually affect project settings, permission policy, and the feature spec's role/action matrix.
- Deleted features must be removed from all current behavior sections, tables, and requirements, but past change-history rows can remain as historical record.
