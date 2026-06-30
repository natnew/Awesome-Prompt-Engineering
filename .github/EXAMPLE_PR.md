# Example: How to Contribute — A Real PR

This file shows a concrete, real-world example of a successful pull request. Use it as a template for your own contributions.

---

## ✅ What a Good PR Looks Like

### PR Title
```
Add Opik to AI_Tools.md → Testing & Evaluation
```

### PR Description
```
- Adds: `[Opik](https://github.com/comet-ml/opik) - Open-source platform for LLM observability, evaluations, and prompt optimization.`
- Section: AI_Tools.md → Testing & Evaluation (bottom)
- Validation: 
  - Link resolves to canonical source ✓
  - Project 4+ years old, 1,200+ stars ✓
  - Duplicate check: not listed elsewhere ✓
  - Description: neutral, factual, ends with period ✓
```

### What Changed in the File

Before:
```markdown
### Testing & Evaluation

- [TruLens](https://www.trulens.org/) — Feedback and evaluation for LLM applications.
- [Weave](https://wandb.ai/site/weave) — Trace-based debugging and scoring from Weights & Biases.
```

After:
```markdown
### Testing & Evaluation

- [TruLens](https://www.trulens.org/) — Feedback and evaluation for LLM applications.
- [Weave](https://wandb.ai/site/weave) — Trace-based debugging and scoring from Weights & Biases.
- [Opik](https://github.com/comet-ml/opik) - Open-source platform for LLM observability, evaluations, and prompt optimization.
```

---

## 📋 Checklist: Did You Remember?

- [ ] Searched the whole repo — URL and project name — no duplicates
- [ ] Link is canonical (GitHub repo, not npmjs.com or a marketing page)
- [ ] HTTPS, not HTTP
- [ ] For projects: >30 days old, ≥60 stars
- [ ] Description:
  - [ ] Starts with a capital letter
  - [ ] Ends with a full stop (period)
  - [ ] No title-case
  - [ ] Does not start with "A" or "An"
  - [ ] Is factual, not marketing tagline
- [ ] Added at the **bottom** of the section (unless it's alphabetised)
- [ ] Link style matches the section (hyphen `-` or em dash `—`)
- [ ] No other files changed
- [ ] No Draft PRs; ready for review when you open it

---

## ❌ Common Mistakes to Avoid

| Mistake | ❌ Wrong | ✅ Right |
| --- | --- | --- |
| **Capitalization** | `A open-source tool for evaluations` | `Open-source tool for evaluations` |
| **Starting phrase** | `This tool lets you trace LLM calls` | `Platform for tracing LLM calls` |
| **Title case** | `Opik - LLM Observability And Evaluation` | `Opik - Open-source platform for LLM observability and evaluation` |
| **No period** | `Open-source tool for LLM observability` | `Open-source tool for LLM observability.` |
| **Non-canonical link** | `https://www.npmjs.com/package/opik` | `https://github.com/comet-ml/opik` |
| **Added in middle** | Added between two existing entries | Added at the bottom of the section |
| **Multiple changes** | Updated README + fixed typo in Glossary | One logical change only |

---

## 🔗 How the Link Check Works

Every PR automatically runs **lychee**, a link checker that:
- ✅ Verifies every URL is reachable
- ✅ Detects redirects (which may indicate a wrong or stale link)
- ✅ Respects `robots.txt` and rate limits
- ✅ Generates a report if any links fail

**If your PR fails the link check:**
1. Verify the link is correct and canonical
2. Check that the host is not temporarily down
3. If the link is correct but the checker is too strict, the maintainer can add it to `.lychee-ignore`

---

## 📞 Questions?

- Read the full [Contributing.md](../Contributing.md) for detailed guidelines
- See [Workflow.md](../Workflow.md) for step-by-step git instructions
- Check the [Code of Conduct](../code-of-conduct.md)

**Thank you for contributing!** 🙏
