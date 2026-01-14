# Benchmark Report Template

## Overview

**Purpose:** Report comparative evaluation results for model selection, A/B tests, or version comparisons.

**When to use:** Comparing models, prompts, or system versions.

**Competencies:** [Evaluation & Measurement](../../COMPETENCIES.md#2-evaluation--measurement)

---

# Benchmark Report: [Comparison Name]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Version:** 1.0

---

## Executive Summary

**Comparison:** _[What's being compared]_

**Winner:** _[Option A / Option B / No clear winner]_

**Key finding:**  
_[One sentence summary]_

**Recommendation:**  
_[Clear recommendation with rationale]_

---

## What We Compared

### Option A: [Name]

| Attribute | Value |
|:----------|:------|
| Model/Version | _[Details]_ |
| Configuration | _[Key parameters]_ |
| Cost per request | $X |

### Option B: [Name]

| Attribute | Value |
|:----------|:------|
| Model/Version | _[Details]_ |
| Configuration | _[Key parameters]_ |
| Cost per request | $X |

### Key Differences

| Attribute | Option A | Option B |
|:----------|:---------|:---------|
| _[Difference 1]_ | _[Value]_ | _[Value]_ |
| _[Difference 2]_ | _[Value]_ | _[Value]_ |

---

## Results Summary

| Metric | Option A | Option B | Winner | Significance |
|:-------|:---------|:---------|:-------|:-------------|
| Correctness | _% | _% | A/B/Tie | p < 0.05? |
| Relevance | _% | _% | A/B/Tie | p < 0.05? |
| Safety | _% | _% | A/B/Tie | p < 0.05? |
| Latency (p95) | _ms | _ms | A/B/Tie | — |
| Cost/1K requests | $X | $Y | A/B/Tie | — |
| **Overall** | _/100 | _/100 | **A/B** | |

---

## Detailed Results

### Correctness

_Does the system produce accurate outputs?_

| Sub-metric | Option A | Option B | Δ |
|:-----------|:---------|:---------|:--|
| Factual accuracy | _% | _% | _% |
| Hallucination rate | _% | _% | _% |
| Logic errors | _% | _% | _% |

**Analysis:**  
_[What drove the difference]_

**Notable examples:**

| Test Case | Option A | Option B | Notes |
|:----------|:---------|:---------|:------|
| _[Case 1]_ | ✅/❌ | ✅/❌ | _[Why different]_ |
| _[Case 2]_ | ✅/❌ | ✅/❌ | _[Why different]_ |

### Relevance

_Does the system address user needs?_

| Sub-metric | Option A | Option B | Δ |
|:-----------|:---------|:---------|:--|
| Task completion | _% | _% | _% |
| Instruction following | _% | _% | _% |
| Appropriate scope | _% | _% | _% |

**Analysis:**  
_[What drove the difference]_

### Safety

_Does the system avoid harmful outputs?_

| Sub-metric | Option A | Option B | Δ |
|:-----------|:---------|:---------|:--|
| Harmful content | _% | _% | _% |
| Guardrail bypass | _% | _% | _% |
| PII leakage | _% | _% | _% |

**Analysis:**  
_[What drove the difference]_

### Latency

| Percentile | Option A | Option B | Δ |
|:-----------|:---------|:---------|:--|
| p50 | _ms | _ms | _ms |
| p95 | _ms | _ms | _ms |
| p99 | _ms | _ms | _ms |

**Distribution:**

```
Option A: [histogram or description]
Option B: [histogram or description]
```

### Cost

| Metric | Option A | Option B | Δ |
|:-------|:---------|:---------|:--|
| Avg tokens/request | _ | _ | _ |
| Cost per 1K requests | $X | $Y | $Z |
| Monthly cost at current volume | $X | $Y | $Z |

**Break-even analysis:**  
_[At what quality difference does cost justify choice?]_

---

## Segment Analysis

### By Query Type

| Query Type | Option A | Option B | Winner |
|:-----------|:---------|:---------|:-------|
| Simple queries | _% | _% | |
| Complex queries | _% | _% | |
| Multi-step tasks | _% | _% | |

### By Domain

| Domain | Option A | Option B | Winner |
|:-------|:---------|:---------|:-------|
| _[Domain 1]_ | _% | _% | |
| _[Domain 2]_ | _% | _% | |

### By Input Length

| Length | Option A | Option B | Winner |
|:-------|:---------|:---------|:-------|
| Short (< 100 tokens) | _% | _% | |
| Medium (100-500) | _% | _% | |
| Long (> 500) | _% | _% | |

---

## Statistical Analysis

### Sample Size

| Metric | N | Required for 95% CI |
|:-------|:--|:--------------------|
| Correctness | _N_ | _N_ |
| Relevance | _N_ | _N_ |
| Safety | _N_ | _N_ |

### Significance Tests

| Comparison | Test | p-value | Significant? |
|:-----------|:-----|:--------|:-------------|
| Correctness A vs B | _[test type]_ | _p_ | Yes/No |
| Relevance A vs B | _[test type]_ | _p_ | Yes/No |
| Safety A vs B | _[test type]_ | _p_ | Yes/No |

### Confidence Intervals

| Metric | Option A (95% CI) | Option B (95% CI) |
|:-------|:------------------|:------------------|
| Correctness | _% ± _% | _% ± _% |
| Relevance | _% ± _% | _% ± _% |

---

## Trade-off Analysis

### Quality vs. Cost

```
[Chart or table showing quality at different price points]
```

_[Analysis of whether quality gain justifies cost]_

### Quality vs. Latency

```
[Chart or table showing quality vs. speed trade-off]
```

_[Analysis of acceptable latency for quality]_

---

## Failure Analysis

### Where Option A Failed

| Failure Type | Count | % | Example |
|:-------------|:------|:--|:--------|
| _[Type 1]_ | _N_ | _% | _[Example]_ |
| _[Type 2]_ | _N_ | _% | _[Example]_ |

### Where Option B Failed

| Failure Type | Count | % | Example |
|:-------------|:------|:--|:--------|
| _[Type 1]_ | _N_ | _% | _[Example]_ |
| _[Type 2]_ | _N_ | _% | _[Example]_ |

### Common Failures (Both)

| Failure Type | Option A | Option B | Notes |
|:-------------|:---------|:---------|:------|
| _[Type]_ | _N_ | _N_ | _[Insight]_ |

---

## Recommendation

### Primary Recommendation

**Choose: Option [A/B]**

**Rationale:**
1. _[Reason 1]_
2. _[Reason 2]_
3. _[Reason 3]_

### Conditions

This recommendation holds if:
- _[Condition 1]_
- _[Condition 2]_

Reconsider if:
- _[Condition that would change recommendation]_

### Implementation Notes

- _[Note 1]_
- _[Note 2]_

---

## Methodology

### Benchmark Suite

| Suite | Cases | Coverage |
|:------|:------|:---------|
| _[Suite 1]_ | _N_ | _[What it tests]_ |
| _[Suite 2]_ | _N_ | _[What it tests]_ |

### Evaluation Methods

| Metric | Method | Details |
|:-------|:-------|:--------|
| Correctness | _[Auto/Human/LLM]_ | _[Specifics]_ |
| Relevance | _[Auto/Human/LLM]_ | _[Specifics]_ |
| Safety | _[Auto/Human/LLM]_ | _[Specifics]_ |

### Known Limitations

- _[Limitation 1]_
- _[Limitation 2]_

### Reproducibility

```bash
# Commands to reproduce this benchmark
[commands]
```

Data available at: _[location]_

---

## Appendix: Raw Data

_[Link to detailed results or include summary tables]_

---

## Appendix: Example Outputs

### Example 1: [Description]

**Input:**
```
[Query]
```

**Option A:**
```
[Response]
```

**Option B:**
```
[Response]
```

**Evaluation:** _[Which is better and why]_

---

*Template version: 1.0*  
*Last updated: [Date]*
