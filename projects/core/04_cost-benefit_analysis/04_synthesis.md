[← Back: Risk Assessment](03_risk_assessment.md) | [Back to Project →](README.md)

# Module 4: Synthesis

Make your decision and communicate it clearly.

---

## What You've Done

Over the previous modules, you've:

1. **Analyzed costs** — Development, infrastructure, maintenance, hidden
2. **Estimated benefits** — With appropriate uncertainty
3. **Assessed risks** — Likelihood, impact, mitigation

Now it's time to synthesize this into a recommendation.

---

## Making the Decision

### Step 1: Calculate ROI

```
Expected Annual Benefit = $_______
Expected Annual Cost = $_______

ROI = (Benefit - Cost) / Cost × 100 = ______%
```

### Step 2: Calculate Payback Period

```
One-time Development Cost = $_______
Monthly Net Benefit = $_______

Payback Period = Development Cost / Monthly Net Benefit = _______ months
```

### Step 3: Scenario Analysis

| Scenario | Annual Benefit | Annual Cost | ROI |
|:---------|:---------------|:------------|:----|
| Pessimistic | $_______ | $_______ | _____% |
| Expected | $_______ | $_______ | _____% |
| Optimistic | $_______ | $_______ | _____% |

**Key question:** Is the pessimistic case acceptable?

### Step 4: Risk Check

| Category | Status |
|:---------|:-------|
| Critical risks | None / _____ (must address) |
| High risks | None / _____ (with mitigation) |
| Unmitigated risks | None / _____ (accepting) |

**Key question:** Are the risks manageable?

### Step 5: Decision Criteria

| Criterion | Threshold | Your Analysis | Pass? |
|:----------|:----------|:--------------|:------|
| Expected ROI | > 50% | _____% | Yes/No |
| Payback period | < 18 months | _____ months | Yes/No |
| Pessimistic case | > Break-even | _____% | Yes/No |
| Critical risks | 0 unmitigated | _____ | Yes/No |
| Strategic fit | Aligned | Yes/No | Yes/No |

---

## The Recommendation

Based on your analysis, choose:

### BUILD

**When to recommend BUILD:**
- Expected ROI exceeds threshold
- Pessimistic case is acceptable
- Risks are manageable
- Strategic fit is clear

**What to include:**
- Clear success criteria
- Timeline and milestones
- Resource requirements
- Risk mitigation plan

### PILOT

**When to recommend PILOT:**
- Expected ROI is promising but uncertain
- Key assumptions need validation
- Risks can be reduced with data

**What to include:**
- Pilot scope and duration
- Success criteria for full build
- Kill criteria
- Resource requirements

### DEFER

**When to recommend DEFER:**
- Timing isn't right
- Dependencies aren't ready
- Better information is coming

**What to include:**
- What would need to change
- When to revisit
- What to do in the meantime

### REJECT

**When to recommend REJECT:**
- Expected ROI is negative
- Risks outweigh benefits
- Strategic misalignment

**What to include:**
- Clear reasoning
- Alternative approaches considered
- What would change the decision

---

## Portfolio Artifacts

### Required Deliverables

| Artifact | Template | Status |
|:---------|:---------|:-------|
| Cost analysis | Cost worksheet | [ ] |
| Benefit estimation | Benefit worksheet | [ ] |
| Risk assessment | Risk worksheet | [ ] |
| Decision memo | `artifacts/decision_memo_template.md` | [ ] |

### Decision Memo

The decision memo is your primary deliverable. It should:

- **Fit on one page** (two pages max)
- **Lead with the recommendation** (don't bury it)
- **Include key numbers** (cost, benefit, ROI)
- **Acknowledge uncertainty** (ranges, not false precision)
- **Be defensible** (someone who disagrees should understand your reasoning)

---

## Writing the Decision Memo

Use the template in `artifacts/decision_memo_template.md`. Key sections:

### Executive Summary (2-3 sentences)

> We recommend [BUILD/PILOT/DEFER/REJECT] for the AI Smart Search feature. 
> Expected ROI is [X]% with [Y] month payback period.
> Key risk is [Z], mitigated by [approach].

### Cost Summary (Table)

| Category | Year 1 | Ongoing/Year |
|:---------|:-------|:-------------|
| Development | $X | - |
| Infrastructure | $X | $X |
| Maintenance | $X | $X |
| **Total** | $X | $X |

### Benefit Summary (Table)

| Category | Annual Value | Confidence |
|:---------|:-------------|:-----------|
| Support savings | $X | Medium |
| Productivity | $X | Low |
| **Total** | $X | |

### ROI Analysis (Brief)

- Expected ROI: X%
- Payback: Y months
- Range: Z% (pessimistic) to W% (optimistic)

### Key Risks (Top 3)

1. [Risk 1] — [Mitigation]
2. [Risk 2] — [Mitigation]
3. [Risk 3] — [Mitigation]

### Recommendation

[Your recommendation with 2-3 sentences of reasoning]

### Success Criteria (If BUILD/PILOT)

- [Criterion 1]
- [Criterion 2]
- [Kill criterion]

---

## Self-Assessment

Before finalizing, check:

### Analysis Quality

- [ ] Costs include hidden costs (opportunity, maintenance, training)
- [ ] Benefits have confidence levels and ranges
- [ ] Risks are comprehensive and prioritized
- [ ] Assumptions are documented

### Recommendation Quality

- [ ] Decision is clear (BUILD/PILOT/DEFER/REJECT)
- [ ] Rationale is explicit
- [ ] Someone who disagrees could understand your reasoning
- [ ] Success and kill criteria are defined

### Communication Quality

- [ ] Memo fits on 1-2 pages
- [ ] Numbers are clear and honest
- [ ] Uncertainty is acknowledged
- [ ] Recommendation is defensible

---

## Reflection Questions

1. **How confident are you in your recommendation?**

   Very confident / Confident / Somewhat confident / Uncertain

2. **What's the most likely way you could be wrong?**

3. **What additional information would most change your analysis?**

4. **How would you explain your recommendation to someone who disagrees?**

5. **In 12 months, how will you know if you were right?**

---

## What You've Learned

If you've completed this project thoroughly, you can now:

### Technical Skills
- [ ] Calculate comprehensive AI feature costs
- [ ] Estimate benefits with appropriate uncertainty
- [ ] Assess and prioritize risks
- [ ] Calculate ROI and payback period

### Professional Skills
- [ ] Make defensible recommendations
- [ ] Communicate uncertainty honestly
- [ ] Write clear decision memos
- [ ] Define success and kill criteria

### Mental Models
- [ ] "Costs are more than API calls"
- [ ] "Benefits need uncertainty ranges"
- [ ] "Great ROI with unmanageable risk is still a bad idea"
- [ ] "A recommendation should be defensible, not just confident"

---

## Final Checklist

Before marking this project complete:

### Analysis
- [ ] Cost analysis complete with all categories
- [ ] Benefit estimation with three-point estimates
- [ ] Risk assessment with mitigation strategies
- [ ] ROI and payback calculated

### Deliverables
- [ ] Decision memo completed
- [ ] Recommendation is clear
- [ ] Success/kill criteria defined

### Quality
- [ ] Analysis is honest about uncertainty
- [ ] Recommendation is defensible
- [ ] Someone could disagree productively

---

## Completion

Congratulations on completing the Cost-Benefit Analysis project.

You've developed the skill of making AI feature decisions that are **defensible** — not just confident, but supported by analysis that others can evaluate and challenge.

The next time someone says "let's add AI to X," you'll know:
- What questions to ask
- How to estimate costs honestly
- How to quantify benefits with uncertainty
- How to assess and communicate risks
- How to make a recommendation you can defend

---

**What's Next?**

- [Incident Response Simulation](../05_incident_response/) — What happens when things go wrong
- [RAG Evaluation Pipeline](../01_rag_evaluation_pipeline/) — Build evaluation into your analysis
- Return to [Projects Overview](../00_overview.md)

---

*Project completed: [DATE]*

*Recommendation: [BUILD / PILOT / DEFER / REJECT]*

*Key insight: [ONE SENTENCE]*
