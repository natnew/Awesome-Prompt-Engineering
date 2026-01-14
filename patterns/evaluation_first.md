# Evaluation-First

*Define success before building.*

**Competencies:** [Evaluation & Measurement](../COMPETENCIES.md#2-evaluation--measurement)  
**Source:** [RAG Evaluation Pipeline](../projects/core/01_rag_evaluation_pipeline/README.md)

---

## The Problem

Teams build AI features, ship them, then ask "is this any good?" By then, they have no baseline, no systematic way to measure quality, and no clear definition of success. Improvements become guesswork. Regressions go unnoticed.

The deeper problem: without upfront evaluation criteria, you can't distinguish "this doesn't work" from "we don't know what working looks like."

---

## The Solution

**Define how you'll measure success before writing implementation code.**

Create your evaluation framework first—metrics, test cases, quality dimensions—then build toward those targets. The eval isn't a checkbox after development; it's the foundation that guides development.

---

## How It Works

### Step 1: Define Quality Dimensions

What does "good" mean for this system? Quality is multidimensional.

| Dimension | Question It Answers |
|:----------|:--------------------|
| Correctness | Is the output factually accurate? |
| Relevance | Does it address what the user needed? |
| Safety | Does it avoid harmful outputs? |
| Latency | Is it fast enough for the use case? |
| Cost | Is it economically sustainable? |

Choose dimensions relevant to your use case. Not everything needs all five.

### Step 2: Create Evaluation Cases

Build test cases BEFORE the system exists.

```
Test Case: [ID]
Input: [Representative input]
Expected: [What good looks like]
Evaluation: [How you'll judge it]
```

Sources for test cases:
- Historical user queries
- Edge cases you anticipate
- Adversarial inputs
- Stakeholder scenarios

### Step 3: Establish Baseline

Run your eval on the simplest possible implementation—or the current system if one exists. This is your baseline. All improvements are measured against it.

### Step 4: Build Toward Targets

Now implement. But at each decision point, ask: "How will this affect the metrics?" Run evals frequently. Watch dimensions trade off against each other.

### Step 5: Continuous Evaluation

Evals aren't a one-time gate. Integrate them into:
- Development (run before committing)
- CI/CD (run before deploying)
- Production (run on sample traffic)

---

## When to Use

- Starting any new AI feature
- Improving an existing AI system
- Comparing models or approaches
- Preparing for production deployment
- After incidents (to prevent regression)

**Especially important when:**
- Quality requirements are unclear
- Stakeholders disagree on "good"
- You'll iterate over time
- Multiple people will work on the system

---

## When NOT to Use

- Quick prototypes where you're exploring feasibility
- One-off scripts with no ongoing use
- When requirements are genuinely unknowable upfront

Even then, consider lightweight evaluation. "I'll know it when I see it" is not a strategy for systems that persist.

---

## Examples

### Example 1: RAG System

**Before building:**
```
Dimensions:
- Answer correctness (does it match ground truth?)
- Retrieval relevance (are the right docs found?)
- Faithfulness (does answer match retrieved content?)
- Latency (< 2 seconds for 95th percentile)

Test set: 200 historical questions with verified answers
Baseline: BM25 retrieval + direct quote
```

**Development guided by:**
- Trying different chunk sizes → measuring retrieval relevance
- Testing embedding models → measuring correctness
- Adding reranking → measuring faithfulness vs. latency

### Example 2: Code Assistant

**Before building:**
```
Dimensions:
- Functional correctness (passes test suite)
- Code quality (linting, style)
- Security (no vulnerabilities introduced)
- Explanation quality (human rating)

Test set: 50 coding tasks with test suites
Baseline: Direct model output, no enhancement
```

---

## Anti-Patterns

### "We'll evaluate later"

**What happens:** You ship, then realize you have no way to measure if it's working. You create evals retroactively, but they're biased toward what you built.

**Fix:** Spend 20% of initial project time on evaluation design.

### Vanity Metrics

**What happens:** You measure what's easy, not what matters. "99% uptime" while users complain about quality.

**Fix:** Tie dimensions to actual user outcomes.

### Evaluation Theater

**What happens:** You have evals, but they don't match production reality. You pass all tests but users are unhappy.

**Fix:** Continuously validate that eval cases represent real usage.

### Single-Dimension Optimization

**What happens:** You optimize accuracy at the expense of latency, or cost at the expense of safety.

**Fix:** Track multiple dimensions simultaneously. Make trade-offs explicit.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Clear success criteria | Upfront time investment |
| Measurable progress | May constrain creative exploration |
| Catch regressions | Maintenance burden for test sets |
| Aligned stakeholders | Initial disagreement on metrics |

---

## Implementation Checklist

- [ ] Identified quality dimensions relevant to use case
- [ ] Created initial test set (minimum 50 cases)
- [ ] Defined evaluation method for each dimension
- [ ] Established baseline measurement
- [ ] Integrated evaluation into development workflow
- [ ] Planned for ongoing evaluation maintenance

---

## Related Patterns

- **[Confidence-Weighted Decisions](confidence_weighted.md)** — Apply uncertainty to eval results
- **[Structured Skepticism](structured_skepticism.md)** — Review eval design itself critically
- **[Circuit Breaker](circuit_breaker.md)** — Use eval metrics as triggers

---

## Key Insight

> "You can't improve what you can't measure, and you can't measure what you haven't defined."

The eval isn't a test of the system—it's the specification of what the system should be.
