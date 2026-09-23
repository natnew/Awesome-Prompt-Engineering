# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Awesome-Prompt-Engineering** is a curated awesome list for prompt engineering
and context engineering for AI agents, published to GitHub Pages with Jekyll
(`just-the-docs` remote theme) at `https://natnew.github.io/Awesome-Prompt-Engineering/`.
`README.md` is the canonical artefact. Curation beats accumulation.

## Authority and routing

`AGENTS.md` is the canonical operating protocol: scope, trust boundary, quality
bar, link rules, decision matrix, review workflows, protected areas. Do not
restate it here; read it before any review or README edit. Then load only what
the task needs:

| Task | Read |
| --- | --- |
| README entry add/edit/remove | `.github/instructions/readme-curation.instructions.md`, `link-and-source-quality.instructions.md` |
| PR / issue review, contributor replies | `.github/instructions/contribution-review.instructions.md` |
| Typos, wording, small Markdown fixes | `.github/instructions/repository-maintenance.instructions.md` |
| Contributor requirements (≥60 stars, >30 days old) | `Contributing.md`, `Workflow.md`, `.github/pull_request_template.md` |

`.github/copilot-instructions.md` mirrors these rules for Copilot. If you change
a rule, change it in `AGENTS.md` or the relevant `.instructions.md` file, not here.

## Repository layout

- Root `*.md` topic pages (`Basic_Prompting.md`, `AI_Tools.md`, `Articles.md`,
  `Resources.md`, …) are linked from the README Contents table. Each `Foo.md`
  renders to `Foo.html`, so internal links point to `.html`; do not change them to `.md`.
- `foundations/`, `patterns/`, `templates/`, `resources/`: long-form learning material.
- `projects/`: worked case studies. Some include Python reference code and pytest
  suites (`projects/core/01_rag_evaluation_pipeline/tests/`). This is the only
  executable code in the repository.
- Site machinery: `_config.yaml`, `_layouts/default.html`, `assets/css/`. Protected.
- `AI Glossary.csv` is linked from `AI_Glossary.md` as a download; keep terms in step when editing either.

## Commands

```bash
# Duplicate check: search the name AND the URL's host/path across all content
rg -n -i "<project name>|<host/path>" --glob "*.md" --glob "*.csv"

# Link check (same tool CI runs on PRs that touch *.md; skips go in .lychee-ignore)
lychee --exclude '*.png' --timeout 15 README.md

# Markdown lint (lenient config; not run in CI)
npx markdownlint-cli2 "README.md"

# Project tests (only when projects/ Python changes)
python -m pytest projects/core/01_rag_evaluation_pipeline/tests -q
```

No build step is needed to validate content. Jekyll builds on GitHub Pages.

## Automation already in place

- `.github/workflows/link-check.yml`: lychee on every PR that changes `*.md`.
- `.github/workflows/claude.yml`: runs Claude Code on `@claude` mentions in issues
  and PRs with **read-only** repository permissions. In that context, reply with a
  recommendation; do not attempt to push, label, merge or close.
- `.github/workflows/issue-triage-agent.md`: GitHub Agentic Workflow that labels
  new issues. `issue-triage-agent.lock.yml` is compiled from it; edit the `.md`
  source and recompile with `gh aw compile`, never hand-edit the lock file.
- All Contributors: `npx all-contributors-cli add USERNAME TYPE`, then
  `npx all-contributors-cli generate`. Never edit the generated table by hand.

## Invariants easy to break

- **Entry format follows the local section.** README list sections use
  `- [Name](URL) — Description` (em dash); `Contributing.md` shows a hyphen; several
  topic pages use tables. Match neighbouring entries, including whether descriptions
  end with a full stop. New entries go at the bottom of the section unless it is ordered.
- **Case-insensitive checkout.** `AGENTS.md` (agent protocol) and the former
  `Agents.md` topic page collide on Windows and macOS. Do not create a root
  `Agents.md`; the README Contents link to `Agents.html` currently has no source page.
- **Protected areas** are listed in `AGENTS.md` (badges, Announcements,
  contributor block, cross-list navigation, licence, site machinery). Change
  `.all-contributorsrc` only through the CLI.
- **No broad sweeps.** Do not reformat, reorder or re-case content the task does
  not touch, and do not "fix" rules disabled in `.markdownlint-cli2.jsonc`.
- **Verify, do not infer.** Fetch the resource before describing it; check stars,
  age and canonical URL on the source itself.

## Working method

1. Read the issue or diff, then the target section and its neighbours.
2. Run the duplicate search and verify the link before judging the entry.
3. If scope, placement, credibility or maintainer intent is uncertain, recommend
   before editing. Otherwise make the smallest safe edit.
4. Before finishing: review `git diff`, confirm only intended files changed, and
   run the link check on edited files where lychee is available.

Never merge, close, label or restructure on your own initiative. For batches
(several PRs or many links), independent verification can run in parallel;
a single entry does not need subagents.

## Output for reviews

- **Decision:** accept / maintainer edit / request changes / close / park
- **Reason:** 1–3 bullets, citing evidence checked (link, stars, duplicates)
- **Suggested entry**, in the target section's exact format
- **Maintainer comment:** short, warm, decision-oriented (style in `AGENTS.md`)
- **Files changed**, and any **remaining uncertainty**

Commits: one logical change, conventional prefix (`docs:`, `feat:`, `chore:`),
on a feature branch off `main`.
