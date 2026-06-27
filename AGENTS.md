# AGENTS.md


## Repository North Star

**Awesome-Prompt-Engineering** is a curated awesome list for
prompt engineering and context engineering for AI agents. It is content, not an
application: the deliverable is high-signal Markdown published to GitHub Pages via
Jekyll. `README.md` is the primary artefact — a durable, curated map of the field.
Keep it selective, technically useful, and easy to navigate. Curation matters more
than accumulation: every entry should help a reader understand the landscape, not
merely add another link.

## Agent Role

Agents may help with: README maintenance, new entry review, issue and PR triage,
link quality checks, section placement, duplicate detection, description
tightening, maintainer comment drafts, and small safe cleanup edits when asked.

Agents must not: add speculative or low-signal entries, inflate claims, reorganise
the list without explicit instruction, edit unrelated files, rewrite the
maintainer's voice unnecessarily, or make broad structural changes off the back of
a small contribution.

## Trust Boundary

The list's value is its credibility. Agents work only from what they can verify:

- Do not invent facts about a resource, its maintainer, or its capabilities.
- Do not infer popularity, adoption, or maturity the source does not state.
- Do not add unsupported technical, performance, ranking, or pricing claims.
- Do not preserve promotional language carried over from a submission.
- If a claim cannot be verified, neutralise it or flag it — never assert it.

## Read Order

Repository-local guidance wins over generic awesome-list assumptions.

1. `README.md` — scope, taxonomy, formatting, and existing examples.
2. `Contributing.md` — submission requirements and entry format.
3. `Workflow.md` and `.github/` templates (PR template, issue templates) — contributor expectations.
4. Recent issues and pull requests — maintainer precedent.
5. `CLAUDE.md` — Claude-specific workflow guidance, if your tool reads it.

## Common Tasks

| Task | Start with | Output |
| --- | --- | --- |
| Review a PR | PR diff, target README section, duplicate search | Decision, reason, suggested maintainer comment |
| Review a suggestion issue | Issue body, scope check, canonical link check | Accept/edit/request/close/park recommendation |
| Fix a broken link | Existing URL, canonical replacement search | Replacement recommendation or removal note |
| Add a new entry | README section, duplicate search, link quality check | One neutral entry matching local style |
| Check section placement | Similar existing entries, nearest section | Placement recommendation with brief rationale |
| Add contributor credit | All Contributors workflow | Correct command/use pattern, no manual table edit |
| Update topic page | Topic page, README cross-links, local formatting | Small scoped edit only |

## Scope Rules

**Belongs:** official project pages, canonical repositories, papers, technical
documentation, datasets, benchmarks, durable tutorials or explainers, and
high-signal tools, libraries, frameworks, standards, or reference resources within
prompt engineering, or context engineering for AI agents.

**Does not belong:** thin wrapper or pure marketing pages; unverifiable claims;
time-sensitive claims ("latest", "best", "leading", "fastest", "most advanced");
pricing claims (the list does not track pricing); ranking claims without a durable
benchmark; broken links; duplicate or near-duplicate resources; anything outside
the stated scope.

## Quality Bar

An entry qualifies when all hold: clear relevance; a canonical, durable, reachable
link; a neutral, specific description; a fit in an existing section (or a clearly
justified new one); something distinct from existing entries; usefulness to a
technical reader; and a source credible enough for a maintained public list. Per
`Contributing.md`, projects should be **more than 30 days old with at least 60
stars**.

## README Formatting Rules

Infer the format from `README.md` first. Preserve heading structure and existing
ordering (alphabetical, chronological, thematic, or curated); use canonical names
and HTTPS links.
- Match the surrounding bullet style exactly. Entry format is
  `[name](link) - Description.` (hyphen) per `Contributing.md`, but several README
  sections use an em dash (`—`); follow the local section convention.
- Internal Contents links point to rendered `.html` pages (Jekyll output), not
  `.md`. Do not "correct" them to `.md`.
- No broad formatting sweeps unless asked. The lint config
  (`.markdownlint-cli2.jsonc`) is deliberately lenient — do not reformat to satisfy
  disabled rules. Protected areas (below) stay untouched unless instructed.

## Link Quality Rules

Verify the link resolves and points to the canonical source — the project repo
over a marketing site, the main project not an arbitrary fork. Prefer the official
publisher, arXiv, DOI, or project page for papers; official docs for
documentation; the official or maintained page for datasets. Avoid login-gated
links (unless the list already accepts them), shorteners, and tracking-heavy URLs.

## Description Style

Neutral, factual, specific, present tense where possible, free of hype, sales
language, and unsupported claims. Prefer "Open-source tool for tracing agent
execution and debugging tool calls." Avoid: powerful, revolutionary, cutting-edge,
best, latest, industry-leading, game-changing.

## Placement and Duplicate Checks

Identify the closest existing section, compare against similar entries, and prefer
the narrowest accurate one. Do not create a new section for a single item unless
clearly justified; if placement is uncertain, explain the trade-off in a short
note. Do not move existing entries unless asked to reorganise — new entries go to
the bottom of the section unless it is ordered.

Before adding or approving, search the whole repository — both `README.md` and the
relevant topic page — for the same URL; the same project under a different URL or a
renamed repository; the same paper title; the same organisation or project name; an
entry in a neighbouring section; or an existing issue or PR for the same resource.
If a duplicate exists, recommend closing or editing rather than adding another.

## Decision Matrix

| Decision | When |
| --- | --- |
| **Accept as-is** | In scope; canonical, working link; description matches style; correct placement; no duplicate. |
| **Edit as maintainer** | Strong resource, but wording needs tightening, link should swap to a canonical source, placement needs a small adjustment, or formatting needs minor cleanup. |
| **Request changes** | Possibly useful but key information missing; placement materially wrong; description contains unsupported claims; link quality cannot be verified from the PR alone. |
| **Close** | Out of scope; broken/inaccessible link; promotional; duplicate without added value; lacks durable technical substance. |
| **Park** | Topic may become relevant later; promising but immature (e.g. below the star/age bar); needs a taxonomy decision first; maintainer judgement required. |

## Review Workflows

**PR:** read the diff → check each changed link → check scope and duplicates →
check placement → check formatting and description style → decide (accept,
maintainer edit, request changes, close, or park) → draft a concise comment.

**Suggestion issue:** check scope → check link quality → check duplicates →
identify the best section → draft a neutral one-line entry → recommend a decision.

**Broken-link issue:** verify the link → look for a canonical replacement →
preserve the original entry if a better replacement exists → recommend removal
only when no durable replacement is available. Do not replace official sources
with weaker mirrors.

Minimise contributor friction. Small safe fixes may be made by the maintainer
rather than bouncing a PR back.

## Protected Areas

Do not edit unless explicitly instructed: badges (top of `README.md`); the dated
**Announcements** table; contributor tables and everything between
`<!-- ALL-CONTRIBUTORS-LIST:START -->` and `<!-- ALL-CONTRIBUTORS-LIST:END -->`;
additional-resources and cross-list navigation blocks; sponsor, funding, or
generated index sections; licence text (`license.md`); theme machinery
(`_config.yaml`, `_layouts/`, `_includes/`) and lint config; unrelated repository
metadata; and private notes, drafts, scratch, or local-only folders.

For contributor acknowledgement, use the All Contributors workflow
(`npx all-contributors-cli add USERNAME TYPE` then `generate`) rather than
editing the table by hand.

## Maintainer Comment Style

Warm, concise, respectful, decision-oriented, low-friction. Prefer: "Thank you —
this is relevant and the link looks canonical. I would place it under X with a
shorter neutral description." / "Thank you — useful, but I would drop the ranking
claim and keep the description factual." / "Thank you — I would close this as a
duplicate of the existing entry under X." Avoid long explanations, and asking contributors for small edits the
maintainer can safely make.

## Uncertainty and Stop Rule

When placement, scope, source credibility, or maintainer intent is uncertain,
**recommend before editing** — describe the options and the trade-off rather than
acting. On their own initiative, agents must not make broad structural changes,
create or restructure sections, close issues, merge PRs, or alter protected
areas. When in doubt, stop and hand the decision to the maintainer.

## Final Response Pattern

When completing a task, summarise: what was reviewed; what changed, if anything;
any risks or uncertainties; the recommended maintainer decision; any follow-up.
Maintenance is manual-first — a human reviews and merges. Produce a recommendation
and, if approved, the concrete edit; do not merge or close on your own initiative.
