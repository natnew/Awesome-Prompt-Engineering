# GitHub Copilot Instructions

## About this repository

**Awesome-Prompt-Engineering** is a curated *awesome list* and learning hub for
prompt engineering, context engineering, and AI agents. It is **content, not an
application**: the deliverable is high-quality, well-organised Markdown, published
to GitHub Pages via Jekyll.

`README.md` is the index and the main list. Topic pages (`Basic_Prompting.md`,
`Advanced_Prompting.md`, `AI_Tools.md`, `Resources.md`, `Articles.md`, and others)
hold the longer-form content. Contribution rules live in `Contributing.md`,
`Workflow.md`, and `code-of-conduct.md`.

## How to treat the repository

- Treat every change as a documentation edit. There is no build, test, or runtime
  behaviour to reason about beyond Markdown rendering.
- Make the smallest change that achieves the goal. Do not reformat, reorder, or
  rewrite existing content that the task does not touch.
- Preserve the maintainer's voice and the structure already in place.

## Contribution standard

The list is mature, so the bar is high. A good addition is **unique, broadly
useful, durable, and non-promotional**. Per `Contributing.md`, projects should be
more than 30 days old and have at least 60 stars. Prefer canonical sources
(official docs, the primary repository, the original paper or guide) over
marketing pages, mirrors, or aggregators.

## Reviewing suggested additions

When assessing a new entry, check that it:

- is genuinely relevant to prompt engineering, context engineering, or AI agents;
- is not already listed — search the whole repository for the URL and the name
  before recommending it;
- links to a canonical, HTTPS source;
- has a neutral, factual description (no marketing taglines, no title-case),
  starting with a capital and ending with a full stop, and not beginning with
  "A" or "An";
- sits in the single best-fit existing category, added at the bottom of that
  category unless the section is alphabetised or otherwise ordered;
- matches the link style of the surrounding section (some lists use a hyphen,
  others an em dash — follow the local convention).

## Preserving README structure

- Keep the existing section order and headings.
- Do not edit badges, the Announcements table, contributor tables, or anything
  between `<!-- ALL-CONTRIBUTORS-LIST:START -->` and
  `<!-- ALL-CONTRIBUTORS-LIST:END -->`.
- Keep time-sensitive wording ("new", "latest", "now supports") out of
  descriptions; the dated Announcements table is the only place for time-stamped
  entries.
- Creating or restructuring categories is a separate change from adding entries,
  and needs maintainer agreement.

## Handling weak submissions

- **Promotional or self-promotional only** — recommend declining, with a brief,
  warm reason.
- **Low quality, abandoned, or below the maturity bar** — recommend declining or
  parking until it qualifies.
- **Duplicate or near-duplicate** — point to the existing entry; only suggest
  replacing it if the new one is demonstrably better.
- **Stale or broken link** — flag it and prefer the current canonical source.
- **Poorly sourced** (thin landing page, unverifiable claims) — ask for a stronger
  source or recommend declining.

## When uncertain

If scope, quality, placement, or whether to accept is unclear, **flag it for the
human maintainer** rather than deciding. Offer a recommendation and, where useful,
a concrete edit — but leave the merge or close decision to a person.

## Do not change without maintainer direction

- Theme machinery (`_config.yaml`, `_layouts/`, `_includes/`).
- Linting configuration (`.markdownlint-cli2.jsonc`) or content formatting only to
  satisfy rules that are deliberately disabled.
- Badges, announcements, contributor tables, and other generated or
  semi-structured README areas.
- Repository structure, categories, or taxonomy.

---

## Maintenance Matrix

This matrix maps content areas to the instruction files and related rules. Use this to understand what changes where, and which rules apply to each task.

| When you change… | File(s) affected | Read these instructions | Key rule |
|---|---|---|---|
| README.md entries (add/edit/remove) | `README.md` | `.github/instructions/readme-curation.instructions.md` + `.github/instructions/link-and-source-quality.instructions.md` | Canonical HTTPS link + neutral description + bottom of section |
| Link quality, source credibility | `README.md`, `Contributing.md`, topic pages | `.github/instructions/link-and-source-quality.instructions.md` | Prefer official repo/docs over mirrors; avoid thin landing pages |
| PR or issue descriptions | `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/` | `.github/instructions/contribution-review.instructions.md` | Concise, warm, respectful tone; thank contributor first |
| General Markdown (typos, wording, small fixes) | Any `.md` file | `.github/instructions/repository-maintenance.instructions.md` | Minimal change; preserve voice and structure; keep `.html` links for Jekyll |
| Protected areas (badges, contributor tables, theme) | `README.md`, `_config.yaml`, `_layouts/`, `_includes/`, `.markdownlint-cli2.jsonc` | `.github/instructions/repository-maintenance.instructions.md` | Do not edit without explicit maintainer direction |
| New issue template | `.github/ISSUE_TEMPLATE/**/*.md` | `.github/instructions/contribution-review.instructions.md` | Guide reports; reduce friction; use YAML forms |
| New topic page or section | New `.md` file | `.github/instructions/readme-curation.instructions.md` + `.github/instructions/repository-maintenance.instructions.md` | Requires maintainer agreement; do not create speculatively |
| Contributing or Workflow guide | `Contributing.md`, `Workflow.md` | All four instruction files | Centralise contributor guidance; keep instructions DRY |

### Cross-File Dependencies

- **README.md** links to: Contributing.md (line 50+), Workflow.md, code-of-conduct.md, .github/EXAMPLE_PR.md
- **Contributing.md** links to: Workflow.md, code-of-conduct.md, .github/instructions/
- **Workflow.md** links to: Contributing.md, .github/ templates
- **AGENTS.md** (tool-agnostic) and **CLAUDE.md** (Claude-specific) describe agent role and decision matrix

When editing any of these files, verify the cross-references still resolve and make sense in context.
