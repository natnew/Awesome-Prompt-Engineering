---
applyTo: ".github/**/*.md,*.md"
---

# Maintenance edits across Markdown files

These rules apply to general upkeep of the Markdown content (fixing typos,
clarifying wording, updating links, small consistency fixes).

This file is for **small maintenance edits only**. It is not for judging whether
a new awesome-list entry should be accepted, deciding list-entry quality,
changing README categories, or restructuring the list, and it does not replace
the more specific README curation or link/source quality instructions. When a
task involves adding, removing, reviewing, or repositioning an awesome-list
entry, follow those more specific instructions instead.

## Keep changes minimal

- Make the smallest edit that achieves the goal. Touch only what the task needs.
- Do not rewrite, reflow, or reorder content that is otherwise fine.
- Do not reformat existing content solely to satisfy lint rules that are
  deliberately disabled in `.markdownlint-cli2.jsonc`.

## Preserve voice and structure

- Match the surrounding style, heading levels, and list conventions.
- Keep the maintainer's tone. Do not impose a different register or restructure
  sections.
- Internal links between pages point to the rendered `.html` paths (Jekyll +
  just-the-docs); keep that convention.

## No large or structural changes without direction

- Do not add or remove sections, categories, or pages unless the maintainer asks.
- Do not change theme machinery (`_config.yaml`, `_layouts/`, `_includes/`) or
  configuration files unless the task is explicitly about site rendering.
- Treat badges, announcements, and contributor tables as protected.

## Readability

- Keep Markdown clean and consistent: language identifiers on code blocks,
  descriptive `alt` text on images, and descriptive link text.
