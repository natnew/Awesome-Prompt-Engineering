# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose & Scope

This is **Awesome-Prompt-Engineering** — a curated awesome list and learning hub for prompt engineering, context engineering, and AI agents. It is **content, not an application**. The deliverable is high-quality, well-organized Markdown.

- Content lives in top-level Markdown files (`Basic_Prompting.md`, `Advanced_Prompting.md`, `AGENTS.md`, `AI_Tools.md`, `Resources.md`, `Articles.md`, etc.). `README.md` is the index/table of contents.
- The site is published via **Jekyll + just-the-docs theme** to GitHub Pages at `https://natnew.github.io/Awesome-Prompt-Engineering/`. Each `Foo.md` renders to `Foo.html` — that is why internal links in the Contents table point to `.html`, not `.md`.
- `_config.yaml`, `_layouts/`, `_includes/` are theme machinery. Don't touch unless a task is explicitly about site rendering.
- Linting is `markdownlint-cli2` with a deliberately lenient config (`.markdownlint-cli2.jsonc`) — most rules are disabled. Don't reformat existing content to satisfy rules that are turned off.

## What Qualifies as a Good Resource

A submission should be **unique, broadly useful, and durable**. The bar is high — the list is mature. Prioritise resources that strengthen the technical signal of the list; relevance alone is not enough.

- For tools/projects: tested, documented, and generally useful (not niche). Per `Contributing.md`, projects should be **>30 days old with ≥60 stars**.
- Prefer canonical sources: official docs, the GitHub repo (not npm/marketing site), the primary paper or guide.
- Reject: boilerplates, thin wrappers, low-quality or abandoned repos, and anything that duplicates an existing entry without being demonstrably better.

## Link & Description Rules

- **HTTPS only.** Prefer the project's GitHub repo over its marketing site where one exists.
- Descriptions are **neutral and factual** — not marketing taglines, not title-case. Start with a capital, end with a period. Don't begin with "A" or "An".
- **Avoid time-sensitive claims** ("new", "latest", "now supports", "just released") in descriptions — they rot. The dated **Announcements** table in `README.md` is the only place for time-stamped entries.
- Match the link style of the **surrounding section**: `Contributing.md` specifies `[name](link) - Description.` (hyphen), but several `README.md` sections use an em dash (`—`). Follow the local convention rather than imposing one.
- Code blocks need language identifiers; images need descriptive `alt` text (accessibility, per `Contributing.md`).

### Protected / Generated README Areas

- Do not casually edit badges, announcements, additional resource callouts, cross-list links, contributor tables, or all-contributors markers.
- Never modify content between `<!-- ALL-CONTRIBUTORS-LIST:START -->` and `<!-- ALL-CONTRIBUTORS-LIST:END -->` manually unless the maintainer explicitly asks.
- Treat generated or semi-structured README sections as protected unless the task specifically targets them.

## Placement & Duplicate Checking

- **Before adding anything, search the whole repo** for the URL and the tool/resource name — duplicates are the most common problem. Check both `README.md` and the relevant topic page.
- Place each entry in the single best-fit section. New entries go to the **bottom of the relevant category** unless the section is alphabetized or otherwise ordered.
- Creating or restructuring categories should be a **separate PR** from adding entries.
- Avoid creating new sections unless the maintainer explicitly approves a taxonomy change.
- One suggestion = one logical change. If a PR bundles unrelated additions, that is a request-changes signal.

## Evaluating PRs & Issues — Decision Guide

Default to **manual review** (see workflow note below). Use this ladder:

- **Accept as-is** — link works, HTTPS, correct section, description follows the rules, no duplicate, passes the quality bar.
- **Edit as maintainer** — content is worth including but has small issues (wording, casing, trailing whitespace, wrong em dash/hyphen, slightly-off placement). Fix it on merge rather than bouncing it back; keep friction low.
- **Request changes** — good intent but needs the contributor's input: broken/duplicate link, missing context on why it beats an existing entry, bundled unrelated changes, or fails an objective rule they should fix.
- **Close** — out of scope, promotional/self-promotion only, fails the quality/maturity bar, or duplicate with no added value. Close warmly with a one-line reason.
- **Park** — borderline or promising-but-premature (e.g. a young project that may clear the 60-star bar later). Label and leave a short note rather than a hard close.

When in doubt about scope, quality, or whether to close, **flag for the human maintainer rather than auto-deciding.**

## Contributor Response Style

Be **warm, concise, respectful, and low-friction**. Thank the contributor. If requesting changes, name the specific rule and link the relevant guide (`Contributing.md`, `Workflow.md`). Prefer fixing trivial issues yourself over making someone re-push. Never gatekeep harshly — this is a community list.

## Workflow: Manual-First

- Maintenance is **manual-first today**: a human reviews and merges. When asked to help with a PR or issue, produce a recommendation and (if approved) the concrete edit — do not merge or close on your own initiative.
- Agent-assisted triage infrastructure exists under `.github/workflows/` and `agents/`, but treat it as **future/opt-in** automation. Don't invoke or rely on it unless the maintainer explicitly asks.

## Commit & PR Conventions

- Contributors fork and branch (see `Workflow.md`); the maintainer works on feature branches off `main`.
- Keep commits scoped to one logical change. Match the existing concise, conventional-style commit messages (`docs:`, `feat:`, `chore:`).

## Contributor Acknowledgement

When a contributor appears in GitHub’s sidebar or has a merged PR/accepted issue but is missing from the README Contributors table, recommend adding them through the All Contributors workflow rather than manually editing the table.

Use `npx all-contributors-cli add USERNAME TYPE` followed by `npx all-contributors-cli generate`.

Only update `.all-contributorsrc` and the generated README contributors block unless the maintainer explicitly asks for broader changes.

## Final Review Checklist

- Only the intended file was changed.
- No protected README areas touched.
- No duplicate URL or resource name introduced.
- Description is neutral, durable, and consistent with the local section style.
- Human maintainer approval required before merge/close actions.
