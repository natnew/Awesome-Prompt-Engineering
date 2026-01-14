[← Back: Benefit Estimation](02_benefit_estimation.md) | [Next: Synthesis →](04_synthesis.md)

# Module 3: Risk Assessment

Identify what could go wrong and how to handle it.

---

## Why Risk Assessment Matters

ROI analysis assumes things go according to plan. Risk assessment asks: **what if they don't?**

```
ROI Analysis:          Risk Assessment:
─────────────          ────────────────
If we build X,         What could prevent X from working?
we expect Y return.    What's the cost if X fails?
                       How do we reduce these risks?
```

A project with great expected ROI but unmanageable risks may still be a bad idea.

---

## Risk Categories

### Technical Risks

Things that might not work technically.

| Risk | Description | Impact |
|:-----|:------------|:-------|
| Quality insufficient | AI responses aren't good enough | Feature fails |
| Latency too high | Users won't wait | Poor adoption |
| Scale issues | Works in testing, fails at load | Production outage |
| Integration problems | Doesn't fit existing systems | Scope creep |
| Model changes | Provider changes API/pricing | Rework needed |

### Business Risks

Things that might not work from a business perspective.

| Risk | Description | Impact |
|:-----|:------------|:-------|
| Low adoption | Users don't engage | No ROI |
| Wrong problem | Solving something users don't care about | Wasted effort |
| Competitive response | Competitor ships better version | Differentiation lost |
| Market timing | Too early or too late | Missed window |
| Budget cut | Funding removed mid-project | Sunk cost |

### Safety Risks

Things that could cause harm.

| Risk | Description | Impact |
|:-----|:------------|:-------|
| Hallucinations | AI gives wrong information | User harm, liability |
| Data leak | Sensitive data exposed | Privacy violation |
| Bias | Unfair treatment of users | Reputation, legal |
| Misuse | Feature used for harm | Reputation, legal |

### Organizational Risks

Things that affect the team or company.

| Risk | Description | Impact |
|:-----|:------------|:-------|
| Team capacity | Team can't deliver | Delays, quality issues |
| Knowledge gaps | Don't have needed skills | Slower delivery |
| Stakeholder alignment | Disagreement on scope/goals | Rework, delays |
| Dependency on key person | Single point of failure | Risk if they leave |

---

## Risk Assessment Framework

### Step 1: Identify Risks

Brainstorm risks across all categories. Be comprehensive — you can filter later.

**Questions to ask:**
- What could prevent us from building this?
- What could prevent users from adopting it?
- What could go wrong in production?
- What could cause harm to users or the company?
- What external factors could change?

### Step 2: Assess Likelihood and Impact

For each risk, estimate:

| Likelihood | Definition |
|:-----------|:-----------|
| Low | < 20% chance |
| Medium | 20-50% chance |
| High | > 50% chance |

| Impact | Definition |
|:-------|:-----------|
| Low | Minor inconvenience, easily recovered |
| Medium | Significant setback, recoverable |
| High | Major damage, hard to recover |
| Critical | Catastrophic, potentially unrecoverable |

### Step 3: Calculate Risk Score

```
Risk Score = Likelihood × Impact

Low × Low = Minimal
Low × Medium = Low
Low × High = Medium
Medium × Medium = Medium
Medium × High = High
High × High = Critical
```

### Step 4: Prioritize

Focus on:
1. Critical and High risks — must address before proceeding
2. Medium risks — should have mitigation plan
3. Low risks — monitor but don't over-invest

---

## Risk Mitigation Strategies

### Strategy 1: Avoid

**Don't do the risky thing.**

Example: "Model hallucinations" → Don't use AI for safety-critical information.

### Strategy 2: Reduce

**Make the risk less likely or less impactful.**

Example: "Quality insufficient" → Run a pilot to validate quality before full build.

### Strategy 3: Transfer

**Make someone else bear the risk.**

Example: "Infrastructure scaling" → Use managed service instead of self-hosting.

### Strategy 4: Accept

**Acknowledge the risk and proceed anyway.**

Example: "Competitive response" → Acceptable risk given our timeline.

---

## Risk Assessment Worksheet

### Risk Identification

| # | Risk | Category | Likelihood | Impact | Score |
|:--|:-----|:---------|:-----------|:-------|:------|
| 1 | | Technical/Business/Safety/Org | L/M/H | L/M/H/C | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

### Risk Mitigation

| # | Risk | Strategy | Mitigation Action | Residual Risk |
|:--|:-----|:---------|:------------------|:--------------|
| 1 | | Avoid/Reduce/Transfer/Accept | | L/M/H |
| 2 | | | | |
| 3 | | | | |

### Risk Summary

| Risk Level | Count | Top Risks |
|:-----------|:------|:----------|
| Critical | | |
| High | | |
| Medium | | |
| Low | | |

---

## Risk-Adjusted Decision Making

### Scenario Analysis

Don't just consider the expected case. Consider:

| Scenario | Probability | Outcome | Expected Value |
|:---------|:------------|:--------|:---------------|
| Best case | 20% | +$X | |
| Expected case | 60% | +$Y | |
| Worst case | 20% | -$Z | |
| **Weighted** | 100% | | |

If the worst case is unacceptable (e.g., company-ending), the project may be too risky even with good expected value.

### Go/No-Go Criteria

Define upfront what would make you stop:

| Condition | Action |
|:----------|:-------|
| Any Critical risk without mitigation | No-Go |
| More than 2 High risks | Requires executive approval |
| Pilot shows < 50% of expected quality | No-Go |
| Costs exceed budget by > 30% | Re-evaluate |

### Kill Criteria

If you proceed, define what would make you stop mid-project:

| Signal | Action |
|:-------|:-------|
| Quality doesn't improve after 2 sprints | Kill or pivot |
| Adoption < 10% after 3 months | Kill or pivot |
| Cost per query > 3x estimate | Re-evaluate |

---

## AI-Specific Risks

AI features have unique risks to consider:

### Quality Risks

| Risk | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| Hallucinations | High | Guardrails, human review |
| Inconsistent quality | Medium | Evaluation suite, monitoring |
| Degradation over time | Medium | Continuous evaluation |

### Cost Risks

| Risk | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| Usage higher than expected | Medium | Rate limiting, cost alerts |
| API price increases | Medium | Multi-provider strategy |
| Context window abuse | Low | Input length limits |

### Dependency Risks

| Risk | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| Provider outage | Low | Fallback provider |
| Model deprecation | Medium | Abstraction layer |
| Terms of service changes | Low | Contract review |

### Reputation Risks

| Risk | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| Bad AI responses go viral | Low | Monitoring, quick response |
| Users distrust AI features | Medium | Transparency, human fallback |
| Regulatory scrutiny | Low-Medium | Compliance review |

---

## Your Task

Complete the Risk Assessment Worksheet:

1. **Identify at least 10 risks** across all categories
2. **Assess likelihood and impact** for each
3. **Calculate risk scores** and prioritize
4. **Define mitigation strategies** for High and Critical risks
5. **Document go/no-go and kill criteria**

---

## Key Insight

**A project with great expected ROI but unmanageable risks may still be a bad idea.**

Risk assessment isn't about finding reasons not to do things. It's about making decisions with eyes open — understanding what could go wrong and having a plan for it.

---

[← Back: Benefit Estimation](02_benefit_estimation.md) | [Next: Synthesis →](04_synthesis.md)
