# CLAUDE.md

This file provides guidance to Claude Code when assisting with this content repository.

This is **Awesome-Prompt-Engineering** — a curated awesome list 
for prompt engineering, and context engineering for AI agents. It is **content, not
an application**: the deliverable is high-signal Markdown published to GitHub
Pages via Jekyll (`https://natnew.github.io/Awesome-Prompt-Engineering/`). There
is no build, test, or runtime to reason about beyond Markdown rendering. Each
`Foo.md` renders to `Foo.html`, which is why Contents links point to `.html`.

`AGENTS.md` is the tool-agnostic operating protocol. **Read it for the full
rules** (scope, link quality, decision matrix, protected areas). This file is the
Claude-specific maintainer assistant: concise, practical, optimised for repeated
use. Where the two overlap, `AGENTS.md` is canonical — do not duplicate it here.

## North Star

- Preserve `README.md` as the canonical public artefact.
- Prefer selective curation over accumulation.
- Keep entries technically useful, neutral, durable, and easy to scan.
- Help the maintainer make fast, consistent, low-friction decisions.
- Do not broaden the repository beyond its stated scope.

## Claude's Role

May assist with: README entry review, PR and issue triage, broken-link
investigation, duplicate detection, section placement, neutral description
rewrites, contributor response drafts, small safe maintainer edits when asked,
and repository instruction improvements when asked.

Must not: add an entry without checking scope, link, duplicates, and placement;
invent facts about a resource; preserve promotional claims; add ranking, pricing,
novelty, or performance claims without strong evidence; rewrite the taxonomy
without explicit instruction; edit unrelated files; or touch protected/generated
areas unless instructed.

## Claude Behaviour Rule

- When the requested action is clear, make the smallest safe edit.
- When scope, placement, credibility, or maintainer intent is uncertain, produce
  a recommendation before editing.
- Never close issues, merge PRs, restructure the README, or edit protected areas
  on your own initiative.
- Keep maintainer comments concise, warm, and decision-oriented; prefer a small
  safe fix over asking a contributor to re-push a trivial change.

## Always-Loaded Context

Keep this file a short orientation, not a manual. Load detail on demand:

- Concise rules → here.
- Full operating protocol → `AGENTS.md`.
- Detailed contribution process → `Contributing.md` and `Workflow.md`.
- Public contributor expectations → `.github/` PR and issue templates.
- Style examples → `README.md` itself.

Do not duplicate long sections from those files.

## First-Pass Workflow

For any issue, PR, or README task:

1. Read the relevant diff or issue.
2. Check repository scope in `README.md`.
3. Check contribution guidance (`Contributing.md`).
4. Check existing entries in the target section.
5. Search the whole repo for duplicates (URL **and** name).
6. Verify the link where tools allow.
7. Inspect the resource enough to understand what it is.
8. Decide the smallest useful action.
9. Produce a concise recommendation or edit.

## Entry Checklist

Before accepting or adding: in scope · technically useful · durable source ·
canonical HTTPS URL · no duplicate · correct section · matches local formatting ·
neutral one-line description · no hype · no unsupported claims · no avoidable
tracking parameters · no unnecessary new section. Projects should be **>30 days
old with ≥60 stars** (`Contributing.md`).

## Common Claude Tasks

| Task | Claude should do |
| --- | --- |
| PR review | Check scope, link, duplicate, placement, formatting, description; return decision and maintainer comment. |
| Suggestion issue | Assess fit, verify canonical source where possible, draft a neutral entry if useful. |
| Broken link | Find a canonical replacement first; recommend removal only if no durable source exists. |
| Entry rewrite | Remove hype, unsupported claims, pricing/ranking language; make the description factual. |
| Section placement | Compare against similar entries and recommend the narrowest accurate section. |
| Maintainer edit | Make only small safe changes when asked; otherwise recommend. |
| Contributor acknowledgement | Use the All Contributors workflow; do not manually edit generated tables. |

Entry format: `- [Name](URL) - Factual description of what it is and who it
helps.` Use the hyphen, or an em dash where the surrounding section already does;
start with a capital, end with a full stop, not title-case, not "A"/"An". See
`AGENTS.md` for full scope, source, and description rules.

## PR Triage

| Decision | When |
| --- | --- |
| **Accept as-is** | Scope, link, placement, format, and description all sound. |
| **Edit as maintainer** | Strong resource, only small fixes (neutralise wording, swap to canonical link, correct placement) — without changing intent. |
| **Request changes** | Contributor must clarify relevance; resource unverifiable; needs substantive repositioning; PR mixes useful and unsuitable changes. |
| **Close** | Out of scope; promotional; duplicate; broken with no replacement; low technical value; mostly marketing/self-promotion. |
| **Park** | Useful but immature; needs a taxonomy decision; needs maintainer judgement; could fit a future section but not yet. |

## Issue Triage

**Suggestions:** strong + in-scope + canonical → draft entry, recommend accept ·
strong but wording/placement unclear → recommend maintainer edit · missing
evidence → ask for minimal clarification · duplicate → close with pointer ·
out of scope → close politely · interesting but premature → park.

**Broken links:** find a canonical replacement first · prefer official over
mirrors · remove only when no durable replacement exists · leave a concise note.

## Protected Areas

Do not edit unless explicitly instructed: badges; generated table of contents;
the Announcements block; cross-list navigation; contributor tables and everything
between `<!-- ALL-CONTRIBUTORS-LIST:START -->` and `<!-- ...:END -->`; licence
text; generated indexes; funding/sponsor files; theme machinery (`_config.yaml`,
`_layouts/`, `_includes/`); lint config; private notes, scratch, or local-only
files. For contributor acknowledgement use the All Contributors workflow
(`npx all-contributors-cli add USERNAME TYPE`, then `generate`); only update
`.all-contributorsrc` and the generated block unless asked for more.

## Maintainer Comment Templates

- **Accept:** "Thank you — this looks relevant, the link is canonical, and the placement works. I would accept this."
- **Maintainer edit:** "Thank you — I would accept this with a small maintainer edit to tighten the description and keep the wording neutral."
- **Request changes:** "Thank you for the suggestion. I think this could fit, but I would ask for a little more context on why this is the canonical source and where it belongs in the list."
- **Close (duplicate):** "Thank you — I would close this as a duplicate, since the resource already appears under [section]."
- **Close (scope):** "Thank you for sharing this. I would close it as it sits outside the current scope of the list."
- **Park:** "Thank you — this may be worth revisiting, but I would park it for now until the list has a clearer section for this category."

## Output Format

When reviewing a PR or issue, respond with:

- **Decision:** accept / maintainer edit / request changes / close / park
- **Reason:** 1–3 bullets
- **Suggested README entry**, if useful
- **Suggested maintainer comment**
- **Files changed**, if any
- **Remaining uncertainty**, if any

## Conventions & Editing Rule

Commits and PRs are scoped to one logical change, with concise conventional-style
messages (`docs:`, `feat:`, `chore:`). The maintainer works on feature branches
off `main`; contributors fork and branch (see `Workflow.md`).

Maintenance is **manual-first**: a human reviews and merges. Produce a
recommendation and, if approved, the concrete edit — do not merge or close on
your own initiative. Do not modify `README.md`, `Contributing.md`, `.github/`
templates, or other files unless explicitly asked. For this kind of task, only
create or refine the instruction file requested.
