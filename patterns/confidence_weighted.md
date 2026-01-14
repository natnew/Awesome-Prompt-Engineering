# Confidence-Weighted Decisions

*Explicit uncertainty in estimates. Know how much you know.*

**Competencies:** [Governance & Defensibility](../COMPETENCIES.md#4-governance--defensibility), [Evaluation & Measurement](../COMPETENCIES.md#2-evaluation--measurement)  
**Source:** [Cost-Benefit Analysis](../projects/core/04_cost_benefit_analysis/README.md)

---

## The Problem

We make decisions based on estimates: "This will save $100K/year." "This will take 3 weeks." "This will improve conversion by 5%." These estimates are presented with false precision, as if we know them exactly. But some estimates are based on solid data while others are guesses. Treating all estimates equally leads to poor decisions.

The deeper problem: single-point estimates hide the range of possible outcomes. "Expected value: $100K" could mean "almost certainly $95K-$105K" or "50% chance of $0, 50% chance of $200K." These are very different bets.

---

## The Solution

**Attach explicit confidence levels to every estimate. Distinguish what you know from what you're guessing. Make decisions using the confidence-adjusted range, not just the point estimate.**

This isn't about being uncertain—it's about being honest about uncertainty that already exists.

---

## How It Works

### Step 1: Assign Confidence Levels

For every estimate, ask: "How confident am I in this number?"

| Level | Meaning | Basis | Typical Range |
|:------|:--------|:------|:--------------|
| **High** | We have strong evidence | Historical data, benchmarks | ±10-20% |
| **Medium** | We have some evidence | Similar projects, expert opinion | ±30-50% |
| **Low** | We're mostly guessing | Extrapolation, intuition | ±50-100% |
| **Very Low** | We really don't know | Pure speculation | ±100%+ |

### Step 2: Express as Ranges

Convert point estimates to ranges based on confidence:

```
Estimate: $100K savings
Confidence: Medium

Range: $50K to $150K (most likely $100K)
```

Better yet, use three-point estimates:

| Scenario | Value | Probability |
|:---------|:------|:------------|
| Pessimistic | $50K | 25% |
| Expected | $100K | 50% |
| Optimistic | $150K | 25% |

### Step 3: Calculate Confidence-Adjusted Values

Use expected value with ranges:

```
Expected Value = P(pessimistic) × V(pessimistic) 
              + P(expected) × V(expected) 
              + P(optimistic) × V(optimistic)

EV = 0.25 × $50K + 0.50 × $100K + 0.25 × $150K
   = $12.5K + $50K + $37.5K
   = $100K

But: 25% chance of only $50K
```

### Step 4: Make Decisions on Worst Plausible Case

Ask: "Is this still a good decision if the pessimistic case happens?"

| Question | How to Decide |
|:---------|:--------------|
| Is pessimistic case acceptable? | Proceed with awareness |
| Is pessimistic case survivable? | Consider mitigation |
| Is pessimistic case catastrophic? | Reconsider or derisk first |

---

## Confidence in Practice

### For Benefits

| Benefit Type | Typical Confidence | Why |
|:-------------|:-------------------|:----|
| Direct cost savings | Medium-High | Measurable, predictable |
| Productivity gains | Low-Medium | Hard to measure, varies |
| Revenue increase | Low | Many confounding factors |
| Competitive advantage | Very Low | Nearly impossible to attribute |
| Strategic value | Very Low | Unmeasurable |

**Rule of thumb:** The further from direct measurement, the lower confidence.

### For Costs

| Cost Type | Typical Confidence | Why |
|:----------|:-------------------|:----|
| Direct development | Medium | Known rate, unknown scope |
| Infrastructure | Medium-High | Predictable pricing |
| Ongoing maintenance | Medium | Historical patterns exist |
| Opportunity cost | Low | Counterfactual is guessed |
| Hidden costs | Low | Unknown unknowns |

### For Timelines

| Estimate Type | Typical Confidence | Why |
|:--------------|:-------------------|:----|
| Simple, done before | High | Historical data |
| Complex, done before | Medium | Variation exists |
| Novel work | Low | Unknown unknowns |
| Dependent on others | Very Low | Out of your control |

---

## When to Use

**Always use for:**
- Cost-benefit analyses
- Project estimates
- Business cases for AI features
- Any decision based on estimates

**Especially important when:**
- Stakes are high
- Reversibility is low
- Stakeholders have different risk tolerance
- Estimates come from uncertain sources

---

## When NOT to Use

- Quick informal estimates
- Situations where precision doesn't matter
- When it would be theatrical (you know the answer)

Even then, mental confidence-weighting helps.

---

## Examples

### Example 1: AI Feature Business Case

**Without Confidence Weighting:**
```
Benefits: $500K/year
Costs: $200K development + $50K/year ops
ROI: 150%
Recommendation: BUILD
```

**With Confidence Weighting:**
```
Benefits:
- Support ticket reduction: $200K (High confidence, ±20%)
- User productivity: $200K (Low confidence, ±75%)
- Competitive advantage: $100K (Very Low confidence, ±100%)

Confidence-Adjusted:
- Pessimistic: $160K + $50K + $0K = $210K
- Expected: $200K + $200K + $100K = $500K
- Optimistic: $240K + $350K + $200K = $790K

Costs:
- Development: $200K (Medium confidence)
  - Pessimistic: $280K, Expected: $200K, Optimistic: $150K
- Ongoing: $50K/year (Medium-High confidence)

Year 1 Analysis:
- Pessimistic: $210K benefit - $330K cost = -$120K
- Expected: $500K benefit - $250K cost = +$250K
- Optimistic: $790K benefit - $200K cost = +$590K

Recommendation: PILOT
Rationale: Expected case is strong, but pessimistic case is negative.
           Pilot reduces exposure while validating benefit assumptions.
```

### Example 2: Project Estimate

**Without Confidence:**
```
"This will take 6 weeks."
```

**With Confidence:**
```
Timeline estimate: 6 weeks (Medium confidence)

Breakdown:
- Core development: 3 weeks (High confidence, ±1 week)
- Integration: 2 weeks (Medium confidence, ±1 week)
- Testing & polish: 1 week (Medium confidence, ±1 week)

Range: 4-9 weeks (most likely 6 weeks)

Commit to: 8 weeks (buffer for pessimistic case)
```

### Example 3: Model Selection

**Without Confidence:**
```
Model A accuracy: 92%
Model B accuracy: 89%
Choose Model A.
```

**With Confidence:**
```
Model A: 92% accuracy (Medium confidence, ±3%)
         Range: 89-95%
         
Model B: 89% accuracy (High confidence, ±1%)
         Range: 88-90%

If accuracy consistency matters more than peak accuracy:
  Choose Model B (more predictable)

If maximum accuracy matters:
  Choose Model A (higher ceiling, higher floor risk)
```

---

## Anti-Patterns

### Confidence Theater

**What happens:** You assign confidence levels, but they don't change decisions. "Low confidence" still treated like fact.

**Fix:** Actually use ranges in calculations. Make decisions on pessimistic case.

### Uniform Confidence

**What happens:** Everything is "Medium confidence." No differentiation.

**Fix:** Force ranking. What do you know best? What do you know least?

### False Precision

**What happens:** "I'm 73.5% confident." Precision implies knowledge you don't have.

**Fix:** Use broad categories. Acknowledge ranges are estimates too.

### Ignoring Correlations

**What happens:** Multiple estimates are all pessimistic or optimistic together, but you treat them as independent.

**Fix:** Consider scenarios where multiple things go wrong together.

### Optimism Bias

**What happens:** "Expected" is actually optimistic. "Pessimistic" is actually expected.

**Fix:** Have someone else set the pessimistic case. Use historical data.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Honest about uncertainty | More complex communication |
| Better risk management | Requires more thought |
| Aligned expectations | Can feel like hedging |
| Defensible decisions | May slow down decision-making |

---

## Implementation Checklist

- [ ] All estimates include confidence level
- [ ] Ranges provided, not just point estimates
- [ ] Pessimistic, expected, and optimistic scenarios
- [ ] Decisions consider worst plausible case
- [ ] Confidence assumptions stated explicitly
- [ ] Historical accuracy tracked to calibrate

---

## Related Patterns

- **[Evaluation-First](evaluation_first.md)** — Measure to increase confidence
- **[Blameless Post-Mortem](blameless_postmortem.md)** — Learn from estimate misses
- **[Structured Skepticism](structured_skepticism.md)** — Challenge confidence assumptions

---

## Key Insight

> "The goal isn't to be right. It's to know how wrong you might be, and make decisions accordingly."

High confidence in your uncertainty is more valuable than false confidence in your estimates.
