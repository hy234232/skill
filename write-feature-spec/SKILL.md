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

## Reference Extraction

Use `scripts/extract_feature_spec_structure.py` when useful to inspect a reference `.md` or `.xlsx` file without loading the whole artifact into context:

```bash
python3 path/to/write-feature-spec/scripts/extract_feature_spec_structure.py <reference-file>
```

The script prints headings, Markdown table headers, and a compact preview of rows. Use it to infer column names and style, then write the final document manually or with a focused script.

For detailed writing rules, read `references/feature_spec_style.md` only when the task involves generating or heavily rewriting a feature-spec document.
