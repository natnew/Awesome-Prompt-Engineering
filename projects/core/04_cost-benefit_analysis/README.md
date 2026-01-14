[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Projects Overview](../00_overview.md) | [Competencies](../../Competencies.md)

# Project 4: Cost-Benefit Analysis

## The Challenge

Someone proposes an AI feature. Should you build it?

The answer is not "yes, AI is amazing" or "no, AI is risky." The answer is a **defensible recommendation** based on:
- Real costs (not just API calls)
- Realistic benefits (with uncertainty)
- Identified risks (and mitigations)
- Explicit trade-offs

This project teaches you to make AI feature decisions that you can defend to stakeholders who weren't in the room.

---

## What You'll Do

You'll work through a realistic AI feature proposal and produce:

1. **Cost analysis** — Full costs including hidden ones
2. **Benefit estimation** — With appropriate uncertainty
3. **Risk assessment** — What could go wrong
4. **Recommendation** — With explicit trade-offs
5. **Decision memo** — A one-page summary for stakeholders

---

## Competencies Developed

| Competency | Emphasis | What You'll Practice |
|:-----------|:--------:|:---------------------|
| **Governance & Defensibility** | ●●● | Making decisions explicit and defensible |
| **Evaluation & Measurement** | ●●● | Quantifying costs and benefits |
| **Systems Design** | ● | Understanding system economics |

---

## The Scenario

**Company:** Mid-sized SaaS company (~500 employees, ~$50M ARR)

**Proposal:** Add an AI-powered "smart search" feature to the product

**Claimed Benefits:**
- Users find what they need faster
- Reduced support tickets
- Competitive differentiation
- "Everyone else is doing it"

**Your Role:** You're the technical lead asked to evaluate whether to build this.

---

## Part 1: Cost Analysis

### Direct Costs

#### Development Costs

| Item | Estimate | Assumptions |
|:-----|:---------|:------------|
| Engineering time | ____ hours × $__/hr = $____ | Seniority mix, loaded cost |
| Design time | ____ hours × $__/hr = $____ | |
| PM time | ____ hours × $__/hr = $____ | |
| QA time | ____ hours × $__/hr = $____ | |
| **Total Development** | **$____** | |

**Guidance:** A feature like this typically takes 2-4 engineers 4-8 weeks. Think about:
- Embedding pipeline
- Search infrastructure
- UI/UX
- Integration with existing product
- Testing and iteration

#### Infrastructure Costs (Monthly)

| Item | Estimate | Calculation |
|:-----|:---------|:------------|
| Embedding model API | $____ | ___ queries/month × ___ tokens × $___/1K tokens |
| Vector database | $____ | ___ vectors × $___/million |
| LLM API (generation) | $____ | ___ queries × ___ tokens × $___/1K tokens |
| Additional compute | $____ | |
| **Total Monthly Infrastructure** | **$____** | |

**Key question:** What's your expected query volume? This drives most costs.

| Volume Scenario | Queries/Month | Monthly Cost |
|:----------------|:--------------|:-------------|
| Conservative | | $____ |
| Expected | | $____ |
| High Growth | | $____ |

#### Ongoing Costs (Monthly)

| Item | Estimate | Notes |
|:-----|:---------|:------|
| Maintenance engineering | ____ hours × $__/hr | Bug fixes, updates |
| Content updates | ____ hours × $__/hr | Reindexing, new content |
| Monitoring | ____ hours × $__/hr | |
| **Total Monthly Ongoing** | **$____** | |

### Hidden Costs

Don't forget:

| Cost | Estimate | Notes |
|:-----|:---------|:------|
| Opportunity cost | $____ | What else could the team build? |
| Training | $____ | Team learning curve |
| Support | $____ | Handling new types of questions |
| Risk mitigation | $____ | Safety work, legal review |

### Total Cost Summary

| Timeframe | Cost |
|:----------|:-----|
| Development (one-time) | $____ |
| Year 1 Total | $____ |
| Year 2 Total | $____ |
| 3-Year Total | $____ |

---

## Part 2: Benefit Estimation

### Benefit Categories

#### Category 1: Support Ticket Reduction

**Logic:** If users can self-serve, they open fewer tickets.

| Variable | Estimate | Confidence | Source |
|:---------|:---------|:-----------|:-------|
| Current tickets/month | | High | Historical data |
| % addressable by search | | Medium | Analysis of ticket types |
| Deflection rate | | Low | Guess until measured |
| Cost per ticket | | High | Support team data |

**Calculation:**
```
Monthly savings = tickets × addressable_% × deflection_rate × cost_per_ticket
               = ___ × ___% × ___% × $___
               = $___/month
```

**Confidence interval:** $____ to $____ (be honest about uncertainty)

#### Category 2: User Productivity

**Logic:** Users find answers faster, do their jobs better.

| Variable | Estimate | Confidence | Notes |
|:---------|:---------|:-----------|:------|
| Users who search | | Medium | |
| Searches per user/month | | Low | |
| Time saved per search | | Low | Very hard to measure |
| Value of user time | | Medium | |

**Calculation:**
```
Monthly value = users × searches × time_saved × hourly_value / 60
             = ___ × ___ × ___ min × $___/hr / 60
             = $___/month
```

**Reality check:** Is this real value or theoretical value? Will users actually do more, or just have more slack time?

#### Category 3: Competitive Differentiation

**Logic:** Users choose us because we have this feature.

| Variable | Estimate | Confidence | Notes |
|:---------|:---------|:-----------|:------|
| Deals influenced | | Very Low | Hard to attribute |
| Additional revenue | | Very Low | |

**Honest assessment:** This is usually the weakest justification. "Everyone else has it" is not a quantified benefit.

#### Category 4: Reduced Churn

**Logic:** Users stay because they can find help.

| Variable | Estimate | Confidence | Notes |
|:---------|:---------|:-----------|:------|
| Current churn rate | | High | |
| Churn due to findability | | Low | Hard to isolate |
| Expected churn reduction | | Very Low | |

### Total Benefit Summary

| Benefit | Annual Value | Confidence |
|:--------|:-------------|:-----------|
| Support reduction | $____ | Medium |
| User productivity | $____ | Low |
| Revenue impact | $____ | Very Low |
| Churn reduction | $____ | Very Low |
| **Total Annual** | **$____** | |

**Honest total:** Weight by confidence. A "Low confidence" $100K is not the same as a "High confidence" $50K.

---

## Part 3: Risk Assessment

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Search quality is poor | Medium | High | Build evaluation suite first |
| Latency is unacceptable | Low | High | Set targets, measure early |
| Scale issues at launch | Medium | Medium | Load testing |
| Model API changes | Medium | Medium | Abstract provider |

### Business Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Users don't use it | Medium | High | Validate need before building |
| ROI doesn't materialize | Medium | High | Measure and have exit criteria |
| Diverts team from roadmap | High | Medium | Clear prioritization |

### Safety Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Hallucinated answers | Medium | High | Guardrails, citations |
| Exposed sensitive data | Low | Critical | Access controls, filtering |
| Wrong answers cause harm | Low | Medium | Depends on domain |

---

## Part 4: Decision Framework

### Calculate ROI

```
Year 1 ROI = (Benefits - Costs) / Costs
          = ($____ - $____) / $____
          = ____%
```

### Payback Period

```
Payback = Development Cost / Monthly Net Benefit
        = $____ / $____
        = ____ months
```

### Confidence-Adjusted Analysis

| Scenario | Benefits | Costs | ROI |
|:---------|:---------|:------|:----|
| Optimistic (80th percentile) | $____ | $____ | ___% |
| Expected (50th percentile) | $____ | $____ | ___% |
| Pessimistic (20th percentile) | $____ | $____ | ___% |

**Key question:** Is the pessimistic case acceptable? If the pessimistic case is "lose money," are you okay with that risk?

### Decision Criteria

| Criterion | Your Assessment |
|:----------|:----------------|
| Is expected ROI > cost of capital? | Yes / No |
| Is payback < 18 months? | Yes / No |
| Is pessimistic case tolerable? | Yes / No |
| Do benefits justify opportunity cost? | Yes / No |
| Are risks manageable? | Yes / No |

---

## Part 5: Your Recommendation

### The Decision

[ ] **BUILD**: Benefits clearly outweigh costs and risks
[ ] **PILOT**: Test with subset before full commitment  
[ ] **DEFER**: Wait for better timing or more information
[ ] **REJECT**: Costs and risks outweigh benefits

### Rationale

[Write 2-3 paragraphs explaining your recommendation]

### Conditions

If BUILD or PILOT:
- Success criteria: ____
- Kill criteria: ____
- Review timeline: ____

If DEFER:
- What would change the decision: ____
- When to revisit: ____

---

## Part 6: Decision Memo

Write a one-page memo summarizing your analysis for leadership.

### Template

```markdown
# Decision Memo: AI-Powered Smart Search

**Date:** ____
**Author:** ____
**Recommendation:** [BUILD / PILOT / DEFER / REJECT]

## Summary

[2-3 sentences summarizing the decision]

## Cost Summary

| Item | Amount |
|:-----|:-------|
| Development | $____ |
| Year 1 Operating | $____ |
| Year 1 Total | $____ |

## Expected Benefits

| Benefit | Annual Value | Confidence |
|:--------|:-------------|:-----------|
| Support savings | $____ | Medium |
| Other | $____ | Low |
| **Total** | $____ | |

## ROI Analysis

- Expected ROI: ____%
- Payback period: ____ months
- Break-even point: ____ queries

## Key Risks

1. ____
2. ____
3. ____

## Recommendation

[Your recommendation with reasoning]

## Success Criteria

If built, we will consider this successful if:
- ____
- ____

## Next Steps

1. ____
2. ____
```

---

## Artifacts

### Required
- [ ] Cost analysis complete
- [ ] Benefit estimation with confidence levels
- [ ] Risk assessment
- [ ] Decision memo (one page)

### Quality Criteria
- [ ] All assumptions documented
- [ ] Uncertainty acknowledged
- [ ] Trade-offs explicit
- [ ] Defensible to skeptic

---

## Common Mistakes

1. **Counting benefits twice**: "Reduced support tickets" and "support team can do other things" are the same benefit
2. **Ignoring opportunity cost**: The team could build something else
3. **Optimism bias**: Using best-case for benefits, worst-case for costs
4. **Confidence theater**: Made-up precision ("23.7% improvement")
5. **Missing hidden costs**: Training, migration, support changes

---

## Reflection Questions

1. **What was the hardest thing to estimate?**

2. **How confident are you in your recommendation?**

3. **What additional information would most change your analysis?**

4. **How would you explain your uncertainty to a non-technical stakeholder?**

5. **What would make you revisit this decision?**

---

## What You've Learned

After completing this project, you should be able to:

- [ ] Calculate comprehensive AI feature costs
- [ ] Estimate benefits with appropriate uncertainty
- [ ] Assess and communicate risks
- [ ] Make defensible recommendations
- [ ] Write clear decision memos

---

**What's Next?**

- [Incident Response Simulation](../05_incident_response/) — What happens when things go wrong
- [RAG Evaluation Pipeline](../01_rag_evaluation_pipeline/) — Deep dive on evaluation
- Return to [Projects Overview](../00_overview.md)

---

*Project completed: [DATE]*

*Decision: [BUILD / PILOT / DEFER / REJECT]*

*Key insight: [ONE SENTENCE]*
