---
name: write-feature-spec
description: Create a new Korean 기능명세서 or requirements/feature-spec Markdown document from a reference 기능명세서 file and raw text input. Use when the user provides an existing 기능명세서/요구사항정의서 file and asks Codex to keep the same table columns, section hierarchy, text length, tone, terminology, and Markdown table format while converting new pasted text, notes, screen descriptions, or feature ideas into a matching 기능명세서.
---

# Write Feature Spec

## Workflow

1. Identify the reference 기능명세서 file and the new source text.
2. Extract the reference structure before writing:
   - Headings and section order.
   - Table headers exactly as written.
   - Existing row grouping/IA hierarchy.
   - Cell style patterns: bullet usage, sentence length, terms, and tone.
3. Preserve the reference file's table columns exactly. Do not rename, remove, or reorder columns unless the user explicitly asks.
4. Convert the new source text into rows that match the reference:
   - Keep one requirement per row unless the reference groups multiple atomic items in one row.
   - Use the same ID pattern and page hierarchy.
   - Keep text length similar to nearby rows in the reference.
   - Use the same Korean business tone: concise, implementation-ready, no marketing copy.
5. If the user asks to edit an existing 기능명세서, change only the requested rows/cells and preserve all unrelated content.
6. Save the output next to the source/reference file unless the user specifies another location.
7. Validate that the generated document opens as plain Markdown and that all tables have consistent column counts.

## Required Output Shape

When creating a Markdown 기능명세서, include these sections unless the reference clearly uses a different structure:

1. Header: file name and one-line description.
2. Metadata block: YAML with `id`, `version`, `status`, `owner_team`.
3. Purpose and scope: why the document exists.
4. Core rules: concise tables or trees.
5. Conditional rules: if/then branches.
6. Implementation notes: enum/error-code style developer notes only when useful.
7. Change history.
8. Original or generated feature-spec table in the same table format as the reference.

## Formatting Rules

- Preserve original source content when the user says not to modify/delete it.
- Use Markdown tables for table-shaped content.
- Escape pipe characters inside cells as `\|`.
- Represent cell-internal line breaks as `<br>` inside Markdown tables.
- If a cell has multiple list items, format each item with `- `.
- Do not let Markdown table rows have inconsistent column counts.
- Do not invent legal, compliance, or policy statements not present in the source.
- Do not add unrelated sections such as README, installation notes, or explanations of the skill.

## 문체 규칙 (공통)

이 스킬이 만드는 모든 한국어 산문은 `human-writing` 스킬을 따른다 (`~/.codex/skills/human-writing/SKILL.md`, 저장소 hy0909/skills). 핵심만 요약:

- 한 문장에 생각 하나, 60자 안팎. 대조·원인은 `~지만`, `~기 때문에`로 한 문장에 잇고, 짧은 문장을 문두 `하지만/그래서`로 툭툭 끊지 않는다. 핵심 먼저.
- 개발·디자인을 모르는 사람도 읽게 일상 동사(쓰다·적어 두다·손보다·나누다)로 쓴다. 한자어 명사구는 `언제 쓰는지, 어디까지 바꿀 수 있는지`처럼 푼다. 용어는 우리말이 있으면 바꾸고(베리언트→형태별 구분), 팀이 매일 쓰는 말은 그대로 둔다. 서술 문장 한가운데 괄호 설명을 끼우지 않는다. 억지 동의어·도치·조각 문장 금지. 문단 첫 문장은 결론.
- 번역투 금지: `~를 통해`, `~에 있어서`, `~에 의해`, `~되어지다`, `위치해 있다`, `~함에도 불구하고`, `~를 가지고 있다`.
- 상투·기계적 표현 금지: `결론적으로`, `시사하는 바가 크다`, `~하는 것이 중요합니다`, `~할 필요가 있다`, `단순한 ~가 아니라`, `~뿐만 아니라 ~도`, `첫째·둘째·셋째` 나열, 형용사·명사 3개 나열, 문두 `또한/따라서/아울러` 연속, 대시(—), `혁신적인·원활한·강력한·다양한·효과적으로`, `파고들어 봅시다`, `잠재력을 발휘하다`.
- `~습니다`가 세 문장 연속이면 하나는 바꾼다. `-적/-성/-화`는 절반으로.
- `많은·다양한·최근·크게 개선`은 숫자·사례로 바꾼다. 정보가 없으면 지어내지 말고 `TBD` 또는 `[확인 필요]`.
- 비교·대조 가능한 항목은 표로 쓴다. 표로 할지 줄글로 할지 판단이 서지 않으면 사용자에게 묻는다(Claude Code에서는 AskUserQuestion 도구).
- 다 쓴 뒤 한 번 더 읽고 "여전히 AI 같아 보이는 곳"을 한 군데 찾아 고친다.
- 이 스킬의 예외: 참조 문서의 톤·문장 길이를 따르는 것이 이 스킬의 목적이므로, 참조 문서와 충돌하면 참조 문서가 우선한다. 번역투·상투 표현 금지는 그래도 적용한다.

## Reference Extraction

Use `scripts/extract_feature_spec_structure.py` when useful to inspect a reference `.md` or `.xlsx` file without loading the whole artifact into context:

```bash
python3 path/to/write-feature-spec/scripts/extract_feature_spec_structure.py <reference-file>
```

The script prints headings, Markdown table headers, and a compact preview of rows. Use it to infer column names and style, then write the final document manually or with a focused script.

For detailed writing rules, read `references/feature_spec_style.md` only when the task involves generating or heavily rewriting a feature-spec document.
