[← Back: Cost Analysis](01_cost_analysis.md) | [Next: Risk Assessment →](03_risk_assessment.md)

# Module 2: Benefit Estimation

Quantify benefits honestly, including uncertainty.

---

## The Benefit Problem

Benefits are harder to estimate than costs because:

1. **They're in the future**: You're guessing what will happen
2. **They depend on behavior**: Users have to actually use the feature
3. **They're often indirect**: Hard to attribute to the feature
4. **They're subject to optimism**: We want the feature to succeed

This module teaches you to estimate benefits honestly, with appropriate uncertainty.

---

## Benefit Categories

### Category 1: Cost Savings

Things you spend less money on.

**Examples for AI features:**
- Reduced support tickets
- Lower labor costs
- Less infrastructure (if replacing something)

**How to estimate:**

```
Savings = Volume × Addressable % × Success Rate × Cost per Unit

Example (support tickets):
Savings = 2,000 tickets/month × 40% addressable × 50% deflected × $25/ticket
        = $10,000/month
```

**Key variables:**

| Variable | How to Estimate | Confidence |
|:---------|:----------------|:-----------|
| Volume | Historical data | High |
| Addressable % | Analysis of types | Medium |
| Success rate | Pilot or benchmark | Low-Medium |
| Unit cost | Accounting data | High |

---

### Category 2: Productivity Gains

Things people do faster or better.

**Examples:**
- Users find information faster
- Employees complete tasks more quickly
- Fewer errors requiring rework

**How to estimate:**

```
Productivity value = Users × Frequency × Time Saved × Value of Time

Example:
Value = 10,000 users × 5 searches/month × 2 min saved × ($50/hr ÷ 60)
      = 10,000 × 5 × 2 × $0.83
      = $83,000/month
```

**Reality check:** 
- Is this time actually valuable? (Or just slack time?)
- Will users actually use the feature?
- How much faster is it really?

---

### Category 3: Revenue Impact

New or protected revenue.

**Types:**
- **New revenue**: Features that drive new sales
- **Retained revenue**: Features that prevent churn
- **Premium revenue**: Features that justify higher pricing

**How to estimate:**

```
New revenue = Influenced deals × Deal size × Conversion lift × Attribution %

Example:
Revenue = 100 deals/quarter × $10,000 × 5% lift × 20% attribution
        = 100 × $10,000 × 0.05 × 0.20
        = $10,000/quarter additional revenue
```

**Warning:** Revenue attribution is the weakest estimate. Be very conservative.

---

### Category 4: Strategic Value

Harder to quantify but sometimes real.

**Examples:**
- Competitive positioning
- Brand perception
- Platform for future features
- Talent attraction

**How to handle:**
- Don't put a dollar value on it
- List it as a "qualitative benefit"
- Don't let it override negative quantitative analysis

---

## Estimating with Uncertainty

### The Confidence Scale

| Level | What It Means | Example |
|:------|:--------------|:--------|
| **High** | Based on data, likely accurate within 20% | Historical ticket volume |
| **Medium** | Informed estimate, could be 50% off | Deflection rate from pilot |
| **Low** | Educated guess, could be 2-3x off | User behavior change |
| **Very Low** | Speculation, could be 10x off | Revenue attribution |

### Three-Point Estimation

For each benefit, estimate:
- **Optimistic**: 80th percentile (20% chance of being better)
- **Expected**: 50th percentile (most likely)
- **Pessimistic**: 20th percentile (20% chance of being worse)

**Example:**

| Benefit | Pessimistic | Expected | Optimistic | Confidence |
|:--------|:------------|:---------|:-----------|:-----------|
| Support savings | $5K/mo | $10K/mo | $15K/mo | Medium |
| Productivity | $20K/mo | $50K/mo | $80K/mo | Low |
| Revenue impact | $0 | $5K/mo | $20K/mo | Very Low |

### Expected Value Calculation

```
Weighted value = (Pessimistic × 0.2) + (Expected × 0.6) + (Optimistic × 0.2)

Support: (5 × 0.2) + (10 × 0.6) + (15 × 0.2) = $10K/mo
Productivity: (20 × 0.2) + (50 × 0.6) + (80 × 0.2) = $50K/mo
Revenue: (0 × 0.2) + (5 × 0.6) + (20 × 0.2) = $7K/mo
```

---

## Benefit Estimation Worksheet

### Cost Savings

| Savings Type | Volume | Addressable | Success Rate | Unit Value | Monthly Value | Confidence |
|:-------------|:-------|:------------|:-------------|:-----------|:--------------|:-----------|
| Support tickets | /month | % | % | $ | $ | |
| Other | | | | | | |

### Productivity Gains

| Gain Type | Users | Frequency | Time Saved | Time Value | Monthly Value | Confidence |
|:----------|:------|:----------|:-----------|:-----------|:--------------|:-----------|
| | | /month | min | $/hr | $ | |
| | | | | | | |

### Revenue Impact

| Impact Type | Volume | Lift | Attribution | Unit Value | Monthly Value | Confidence |
|:------------|:-------|:-----|:------------|:-----------|:--------------|:-----------|
| | | % | % | $ | $ | |
| | | | | | | |

### Total Benefits

| Category | Pessimistic | Expected | Optimistic | Confidence |
|:---------|:------------|:---------|:-----------|:-----------|
| Cost savings | $/mo | $/mo | $/mo | |
| Productivity | $/mo | $/mo | $/mo | |
| Revenue | $/mo | $/mo | $/mo | |
| **Total** | $/mo | $/mo | $/mo | |

---

## Validation Techniques

### Technique 1: Pilot Testing

Before committing, run a small pilot:
- Subset of users
- Limited scope
- Real measurement

**What you learn:**
- Actual usage rate
- Actual success rate
- User feedback
- Real costs

### Technique 2: Comparable Features

Look at similar features:
- Internal: How did Feature X perform?
- External: What do benchmarks say?
- Competitive: What do competitors report?

### Technique 3: User Research

Ask users directly:
- Would you use this?
- How often?
- What's it worth to you?

**Warning:** Users overstate willingness to use new features. Discount by 50-75%.

### Technique 4: Expert Judgment

Ask people who would know:
- Support team: What tickets could this address?
- Sales team: Would this help close deals?
- Engineering: Is this technically feasible at claimed performance?

---

## Common Benefit Estimation Mistakes

### Mistake 1: Double Counting

**Wrong:**
- "Reduced support tickets" AND
- "Support team can focus on other things"

These are the same benefit counted twice.

### Mistake 2: Theoretical vs. Actual

**Wrong:** "If all 100K users use this 5 times a day..."
**Right:** "Based on similar features, ~20% of users will use this weekly..."

### Mistake 3: Ignoring Adoption

Features don't help if nobody uses them.

**Expected adoption by feature type:**

| Feature Type | Typical Adoption | Notes |
|:-------------|:-----------------|:------|
| Core workflow | 60-80% | Part of normal work |
| Enhancement | 30-50% | Nice to have |
| New capability | 10-30% | Requires behavior change |
| AI feature | 15-40% | Novelty wears off |

### Mistake 4: Optimism Bias

We tend to overestimate benefits of things we want to build.

**Correction:** Use pessimistic estimate as base case, require evidence for higher.

### Mistake 5: Conflating Value and Capture

Value created ≠ value captured.

- Feature makes users 10% more productive
- Does that mean they pay 10% more? (Probably not)
- Does that mean they churn 10% less? (Maybe)

---

## Communicating Uncertainty

### To Stakeholders

**Don't say:** "This will save $100K/year."

**Do say:** "We estimate savings of $50-150K/year, most likely around $100K. The main uncertainty is adoption rate — if only 20% of users engage, it's closer to $50K; if 60% engage, it's $150K."

### In Documents

Use ranges and confidence levels:

> **Expected benefit: $80-120K/year (Medium confidence)**
> 
> Based on:
> - Support ticket analysis (High confidence)
> - Estimated deflection rate of 40-60% (Medium confidence)  
> - Assumed 50% user adoption (Low confidence)
>
> If adoption is lower than expected, benefits could be as low as $50K/year.

---

## Your Task

Complete the Benefit Estimation Worksheet with:
- All benefit categories relevant to your scenario
- Three-point estimates (pessimistic, expected, optimistic)
- Confidence levels for each
- Documentation of key assumptions

Be honest about uncertainty. A credible analysis with wide ranges is better than a precise analysis that's wrong.

---

## Key Insight

**Benefits are uncertain. Communicate that uncertainty.**

A stakeholder who understands "we expect $100K with 40% uncertainty" can make a better decision than one who thinks "$100K is guaranteed."

---

[← Back: Cost Analysis](01_cost_analysis.md) | [Next: Risk Assessment →](03_risk_assessment.md)
