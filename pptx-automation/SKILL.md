---
name: pptx-automation
description: Create, improve, and verify presentation deliverables from raw text or existing PowerPoint files. Use when Codex needs to turn Korean or English source material into a polished PPTX, PDF, and HTML preview; improve an existing .pptx for readability, hierarchy, and design consistency; create company introductions, project proposals, government R&D proposals, B2B sales proposals, IR decks, or presentation materials; or preserve editable slide structure while exporting fixed-layout review files.
---

# PPTX Automation

## Core Workflow

1. Identify the input path:
   - **Raw text**: restructure the material into a slide outline before building the deck.
   - **Existing PPTX**: inspect the current slide flow, extract content, then rebuild or improve the slides while preserving meaning.
2. Identify the output intent:
   - Company introduction: self/third-party profile, solution technology, history, organization, revenue.
   - Project proposal: government task, B2B customer proposal, solution proposal, selected-page customization.
   - Presentation cleanup: readability, visual hierarchy, consistency, summarization.
3. Load brand defaults from `assets/brand-profile.json` when present, then ask only for missing essentials that materially affect the result: document type, one-time brand override, company/project name, logo/template if required, and whether uncertain facts should remain blank or be marked as TODO.
4. Build a slide outline first. Each slide must have one main message, a title, optional subtitle, and a body type such as bullets, cards, table, timeline, comparison, process, or closing CTA.
5. Create editable PPTX, export PDF, and create an HTML preview or review file when requested or useful.
6. Render and visually inspect the output before finishing. Iterate until text fits, hierarchy is clear, slides open, and PDF layout matches the PPTX.

## Required Quality Rules

- Do not invent market size, revenue, customer names, dates, credentials, or technical claims not provided by the user. Mark missing facts as `TODO:` or ask for the data.
- Keep one core message per slide.
- Prefer conclusion-style titles over topic labels.
- Convert long paragraphs into cards, tables, steps, comparisons, timelines, or summary boxes.
- Preserve semantic meaning when improving an existing PPTX; simplify phrasing and layout without changing facts.
- Keep PPTX objects editable: use text boxes, shapes, tables, and image placeholders instead of flattening whole slides into screenshots.
- Apply a consistent grid, font scale, color palette, spacing, and section structure.
- Use the saved brand profile first, then apply any request-specific brand overrides. If no brand colors are available, choose a restrained professional palette and state the assumption.
- Avoid complex animation, video, motion graphics, and unlicensed external imagery unless the user explicitly asks and provides assets.

## Document Blueprints

Read `references/deck-blueprints.md` when choosing slide order, section structure, or content emphasis for:

- company introduction / IR / B2B sales decks
- government task proposals
- customer proposals
- presentation readability cleanup

Use the blueprint as a starting point, then adapt to the actual source material.

## Brand Profile

Use `assets/brand-profile.json` as the reusable default brand source. It may include:

- `name`
- `primary`
- `secondary`
- `accent`
- `font_family`
- `website`
- `email`
- `phone`
- `footer_text`
- `logo_path`
- `tone`

Brand precedence:

1. One-time user request overrides, such as "use blue instead today" or a project-specific brand file.
2. The outline JSON `brand` object.
3. `assets/brand-profile.json`.
4. Script fallback colors.

For permanent brand changes, update `assets/brand-profile.json`. For one-time changes, keep the saved profile intact and add a `brand` object to the outline or pass `--brand-profile path/to/project-brand.json` to the script.

## Text to Deck

1. Parse the source into claims, evidence, metrics, audiences, constraints, and missing facts.
2. Choose a document blueprint and generate a slide outline with:
   - cover
   - table of contents when the deck has more than 6 content slides
   - section dividers for longer decks
   - body slides
   - final message/contact slide
3. Rewrite titles and subtitles so the reader can understand the point within 3 seconds.
4. Choose visual formats:
   - bullet list for simple summary
   - cards for grouped concepts, features, benefits, roles, or business models
   - table for comparison, requirements, budgets, or role split
   - timeline for history, roadmap, schedule, or milestones
   - process diagram for workflows or implementation steps
5. Generate PPTX and HTML from the outline. Use `scripts/outline_to_pptx.py` for a fast editable baseline, then refine manually when the deck needs stronger visual craft.
6. Export PDF and visually verify both files.

## Existing PPTX Improvement

1. Extract or inspect each slide's title, body text, tables, images, and layout intent.
2. Create a slide-by-slide diagnosis:
   - text overload
   - unclear title/message
   - weak hierarchy
   - inconsistent colors/fonts/spacing
   - dense or unreadable tables
   - broken flow between slides
3. Rebuild slides when the original layout is too unstable; otherwise modify in place.
4. Keep the original claims and ordering unless a better flow is clearly needed.
5. Split overloaded slides, simplify tables, and convert long text into structured visuals.
6. Preserve or improve brand elements from the original deck when they are usable.
7. Export improved PPTX, PDF, and HTML preview/review artifact.

## Scripted Baseline

Use `scripts/outline_to_pptx.py` when you have a structured JSON outline and need a quick editable deck:

```bash
python3 scripts/outline_to_pptx.py outline.json --out dist/deck.pptx --html dist/deck.html --pdf
```

The script expects JSON like:

```json
{
  "title": "Company Introduction",
  "subtitle": "AI solution proposal",
  "brand": {"primary": "#1F4E79", "secondary": "#22A699"},
  "slides": [
    {"type": "cover", "title": "Company Introduction", "subtitle": "AI solution proposal"},
    {"type": "content", "title": "Customers reduce review time with automated document intelligence", "bullets": ["Problem", "Solution", "Expected impact"]},
    {"type": "cards", "title": "Solution scope", "cards": [{"title": "Analyze", "body": "Extract key facts"}, {"title": "Generate", "body": "Create editable reports"}]},
    {"type": "closing", "title": "Next step", "subtitle": "Confirm scope and pilot schedule"}
  ]
}
```

To use a different brand for only one deck:

```bash
python3 scripts/outline_to_pptx.py outline.json --brand-profile project-brand.json --out dist/deck.pptx
```

To override a single brand value from the command line. When `name` is overridden without `footer_text`, the footer follows the new name:

```bash
python3 scripts/outline_to_pptx.py outline.json --brand primary=#003A70 --brand name="Client Proposal" --out dist/deck.pptx
```

The script can export PDF only when LibreOffice or `soffice` is available. If PDF conversion fails, report that PPTX and HTML were generated and explain the missing converter.

## Verification Checklist

Before final delivery:

- Open or inspect the PPTX package to confirm it is valid.
- Render slides to images or PDF and visually check the first, middle, and last slides at minimum.
- Confirm no text spills outside slide bounds.
- Confirm Korean text renders correctly in PPTX and PDF.
- Confirm the PDF has the same visual layout as the PPTX.
- Confirm HTML preview opens and includes all slide text when HTML output is requested.
- Check that final filenames distinguish source, improved, PDF, and HTML artifacts.

## Output Summary

When finished, report:

- created or modified files
- document type and assumptions used
- any missing facts marked as TODO
- verification performed and any limitations, especially PDF conversion availability
