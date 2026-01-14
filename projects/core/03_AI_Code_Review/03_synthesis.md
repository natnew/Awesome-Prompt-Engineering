[← Back: Review Methodology](02_review_methodology.md) | [Back to Project →](README.md)

# Module 3: Synthesis

Complete your personal checklist and reflect on what you've learned.

---

## What You've Done

Over this project, you've:

1. **Understood why AI code fails** — The gap between plausibility and correctness
2. **Learned a systematic review methodology** — Quick scan → Deep analysis → Verification → Decision
3. **Practiced on real examples** — Found issues across multiple categories
4. **Identified your blind spots** — Where you missed issues

Now synthesize this into a personal checklist you'll actually use.

---

## Portfolio Artifacts Checklist

### Required Artifacts

| Artifact | Location | Status |
|:---------|:---------|:-------|
| Completed code reviews | [your notes] | [ ] |
| Personal checklist | `artifacts/your_checklist.md` | [ ] |
| Blind spot analysis | [below] | [ ] |

---

## Creating Your Personal Checklist

The template in `artifacts/checklist_template.md` is comprehensive. Too comprehensive to use for every review.

Your personal checklist should be:
- **Prioritized** — Critical items first
- **Relevant** — Focused on your domain/language
- **Based on experience** — Emphasize what you miss

### Step 1: Analyze Your Review Performance

From the exercises you completed, fill in:

| Issue Type | Found | Missed | Accuracy |
|:-----------|:------|:-------|:---------|
| Input validation | | | % |
| Error handling | | | % |
| Security | | | % |
| Logic errors | | | % |
| Performance | | | % |
| Edge cases | | | % |
| Concurrency | | | % |

**Your weakest areas:** 
1. 
2. 
3. 

### Step 2: Customize Your Checklist

Based on your analysis, create a personalized checklist:

```markdown
# My AI Code Review Checklist

## Always Check (My Weak Spots)
- [ ] [Item from your weakest area]
- [ ] [Item from your weakest area]
- [ ] [Item from your weakest area]

## Quick Scan (30 seconds)
- [ ] Does it do what was asked?
- [ ] Are inputs validated?
- [ ] Is there error handling?

## Security (Non-negotiable)
- [ ] User input in SQL → parameterized?
- [ ] User input in file paths → validated?
- [ ] User input in HTML → escaped?
- [ ] Secrets hardcoded → NO

## For My Domain/Stack
- [ ] [Domain-specific check 1]
- [ ] [Domain-specific check 2]
- [ ] [Domain-specific check 3]

## Before Shipping
- [ ] Tested with empty input?
- [ ] Tested with boundary values?
- [ ] Would I debug this at 2 AM?
```

### Step 3: Test Your Checklist

Apply your checklist to a new piece of AI-generated code (not from the exercises):

1. Generate code using your preferred AI tool
2. Review using only your checklist
3. Note what you caught and missed
4. Update your checklist

---

## Blind Spot Analysis

Complete this reflection:

### Technical Blind Spots

**1. What type of issue do you miss most often?**

[Your answer]

**2. Why do you think you miss it?**
- [ ] Don't know what to look for
- [ ] Know but forget to check
- [ ] Assume AI handles it correctly
- [ ] Other: ____

**3. What will you do about it?**

[Your action plan]

### Process Blind Spots

**4. At what phase of review do issues slip through?**
- [ ] Quick scan — miss obvious issues
- [ ] Deep analysis — don't go deep enough
- [ ] Verification — don't actually test
- [ ] Decision — too lenient/strict

**5. What's your review confidence vs. reality?**

| Confidence Level | Issues Found Later? | What It Means |
|:-----------------|:--------------------|:--------------|
| "Looks good" | Often | Overconfident |
| "Some concerns" | Sometimes | Calibrated |
| "Not sure" | Rarely | Overcautious |

### Contextual Blind Spots

**6. What context do you miss that AI doesn't know?**
- [ ] Production environment constraints
- [ ] Codebase conventions
- [ ] Security requirements
- [ ] Performance requirements
- [ ] Other: ____

**7. How will you ensure this context is applied?**

[Your answer]

---

## Reflection Questions

Answer honestly:

### 1. What was the hardest issue to catch in the exercises?

[Your answer]

### 2. What made you trust code that was wrong?

[Your answer]

### 3. How has your trust in AI code changed?

Before this project: [More trusting / About right / More skeptical]
After this project: [More trusting / About right / More skeptical]

### 4. What's your new rule for AI code?

Complete this sentence:
"I will trust AI code when ____, but verify ____, and reject when ____."

### 5. How will you apply this to real work?

[Your specific action plan]

---

## What You've Learned

If you've completed this project thoroughly, you can now:

### Technical Skills
- [ ] Identify common AI code failure patterns
- [ ] Review code systematically (Quick scan → Deep analysis → Verification)
- [ ] Test edge cases that AI misses
- [ ] Spot security vulnerabilities in generated code

### Professional Skills
- [ ] Document review findings
- [ ] Make ship/fix/reject decisions
- [ ] Communicate review results to others
- [ ] Build and maintain personal checklists

### Mental Models
- [ ] "AI code is optimized for plausibility, not correctness"
- [ ] "Trust but verify — always verify"
- [ ] "I'm responsible for code I approve"
- [ ] "My checklist is a living document"

---

## Going Deeper

### If You Want More Practice

1. **Review more code** — Generate AI code for your actual work tasks, review it
2. **Peer review** — Compare your findings with colleagues
3. **Track metrics** — Keep a log of issues found/missed over time
4. **Study vulnerabilities** — OWASP Top 10, CWE Top 25
5. **Learn your tools** — IDE plugins, linters, static analysis

### Additional Resources

**Security:**
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [CWE Top 25](https://cwe.mitre.org/top25/)

**Code Quality:**
- [Google Engineering Practices](https://google.github.io/eng-practices/review/)
- [Microsoft Code Review Guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/review-pull-requests)

**AI-Specific:**
- GitHub Copilot security research
- AI code generation evaluation papers

---

## Final Checklist

Before marking this project complete:

### Artifacts
- [ ] Reviewed all code samples (README + extended exercises)
- [ ] Created personalized checklist
- [ ] Completed blind spot analysis
- [ ] Answered reflection questions

### Practice
- [ ] Applied checklist to at least one new piece of AI code
- [ ] Updated checklist based on experience

### Understanding
- [ ] Can explain why AI code fails
- [ ] Can describe systematic review process
- [ ] Know your personal blind spots
- [ ] Have a plan to address them

---

## Completion

Congratulations on completing the AI Code Review Exercise.

You've developed the most important skill for working with AI-generated code: **skeptical judgment**.

The AI tools will get better. The code they generate will look more correct. But the fundamental gap between plausibility and correctness will remain. Your job is to bridge that gap.

Remember:
- AI doesn't understand code; it recognizes patterns
- Plausible is not the same as correct
- You're responsible for code you approve
- Your checklist is a living document

Use what you've learned. Update your checklist as you gain experience. Share what you learn with your team.

---

**What's Next?**

- [Cost-Benefit Analysis](../04_cost_benefit_analysis/) — Decide whether to build AI features
- [Agent with Guardrails](../02_agent_with_guardrails/) — Apply review thinking to agent outputs
- Return to [Projects Overview](../00_overview.md)

---

*Project completed: [DATE]*

*Time invested: [HOURS]*

*Personal checklist items added: [NUMBER]*

*Key insight: [ONE SENTENCE]*
