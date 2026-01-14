# Evaluation Scorecard Template

## Overview

**Purpose:** Track AI system quality across multiple dimensions over time.

**When to use:** Ongoing quality monitoring, comparing versions, identifying degradation.

**Competencies:** [Evaluation & Measurement](../../COMPETENCIES.md#2-evaluation--measurement)

---

# Evaluation Scorecard: [System Name]

**Date:** YYYY-MM-DD  
**Evaluator:** [Name]  
**Version Evaluated:** _[Version/commit]_  
**Evaluation Type:** Baseline | Periodic | Pre-Release | Incident

---

## Summary

| Dimension | Score | Target | Status | Trend |
|:----------|:------|:-------|:-------|:------|
| Correctness | _/100_ | ≥ 85 | 🟢 / 🟡 / 🔴 | ↑ / → / ↓ |
| Relevance | _/100_ | ≥ 80 | 🟢 / 🟡 / 🔴 | ↑ / → / ↓ |
| Safety | _/100_ | ≥ 95 | 🟢 / 🟡 / 🔴 | ↑ / → / ↓ |
| Latency | _ms_ | ≤ 2000 | 🟢 / 🟡 / 🔴 | ↑ / → / ↓ |
| Cost | $_/1K_ | ≤ $X | 🟢 / 🟡 / 🔴 | ↑ / → / ↓ |
| **Overall** | _/100_ | ≥ 80 | 🟢 / 🟡 / 🔴 | |

**Key Finding:**  
_[One sentence summary of evaluation results]_

---

## Dimension Details

### 1. Correctness

_Does the system produce accurate, factually correct outputs?_

| Metric | Value | Target | Notes |
|:-------|:------|:-------|:------|
| Factual accuracy | _% | ≥ 90% | |
| Hallucination rate | _% | ≤ 5% | |
| Citation accuracy | _% | ≥ 85% | |
| Logic errors | _% | ≤ 3% | |

**Test set:** _[Description or link to test cases]_  
**Sample size:** _[N cases]_

**Failure patterns:**
- _[Pattern 1]: [frequency]_
- _[Pattern 2]: [frequency]_

### 2. Relevance

_Does the system address what the user actually needs?_

| Metric | Value | Target | Notes |
|:-------|:------|:-------|:------|
| Task completion | _% | ≥ 85% | |
| Answer relevance | _/5_ | ≥ 4.0 | |
| Following instructions | _% | ≥ 90% | |
| Appropriate scope | _% | ≥ 85% | |

**Test set:** _[Description or link]_  
**Sample size:** _[N cases]_

**Failure patterns:**
- _[Pattern 1]: [frequency]_
- _[Pattern 2]: [frequency]_

### 3. Safety

_Does the system avoid harmful outputs and behaviors?_

| Metric | Value | Target | Notes |
|:-------|:------|:-------|:------|
| Harmful content rate | _% | ≤ 0.1% | |
| PII leakage rate | _% | 0% | |
| Guardrail bypass rate | _% | ≤ 0.5% | |
| Appropriate refusal rate | _% | ≥ 95% | |

**Test set:** _[Adversarial test suite]_  
**Sample size:** _[N cases]_

**Incidents since last eval:**
- _[Incident 1]_
- _[Incident 2]_

### 4. Latency

_Is the system responsive enough for the use case?_

| Metric | Value | Target | Notes |
|:-------|:------|:-------|:------|
| p50 latency | _ms | ≤ 1000ms | |
| p95 latency | _ms | ≤ 2000ms | |
| p99 latency | _ms | ≤ 5000ms | |
| Timeout rate | _% | ≤ 1% | |

**Measurement period:** _[Date range]_  
**Request volume:** _[N requests]_

### 5. Cost

_Is the system economically viable?_

| Metric | Value | Target | Notes |
|:-------|:------|:-------|:------|
| Cost per 1K requests | $_ | ≤ $X | |
| Tokens per request (avg) | _ | ≤ Y | |
| Cache hit rate | _% | ≥ Z% | |
| Cost trend (30d) | _% | ≤ +10% | |

**Measurement period:** _[Date range]_

---

## Segment Analysis

Performance may vary across different segments. Track key breakdowns.

### By Use Case

| Use Case | Correctness | Relevance | Safety | Volume % |
|:---------|:------------|:----------|:-------|:---------|
| _[Use case 1]_ | _% | _% | _% | _% |
| _[Use case 2]_ | _% | _% | _% | _% |
| _[Use case 3]_ | _% | _% | _% | _% |

### By User Segment

| Segment | Correctness | Relevance | Satisfaction | Volume % |
|:--------|:------------|:----------|:-------------|:---------|
| _[Segment 1]_ | _% | _% | _/5 | _% |
| _[Segment 2]_ | _% | _% | _/5 | _% |

### By Input Characteristics

| Characteristic | Correctness | Notes |
|:---------------|:------------|:------|
| Short inputs (< 50 tokens) | _% | |
| Long inputs (> 500 tokens) | _% | |
| Complex queries | _% | |
| Simple queries | _% | |

---

## Comparison

### vs. Previous Version

| Dimension | Current | Previous | Change |
|:----------|:--------|:---------|:-------|
| Correctness | _% | _% | _[+/-X%]_ |
| Relevance | _% | _% | _[+/-X%]_ |
| Safety | _% | _% | _[+/-X%]_ |
| Latency (p95) | _ms | _ms | _[+/-Xms]_ |
| Cost/1K | $_ | $_ | _[+/-$X]_ |

### vs. Baseline

| Dimension | Current | Baseline | Change |
|:----------|:--------|:---------|:-------|
| Correctness | _% | _% | _[+/-X%]_ |
| Relevance | _% | _% | _[+/-X%]_ |
| Safety | _% | _% | _[+/-X%]_ |

---

## Issues Identified

### Critical (Must Fix)

| Issue | Impact | Frequency | Recommended Action |
|:------|:-------|:----------|:-------------------|
| | | | |

### High Priority

| Issue | Impact | Frequency | Recommended Action |
|:------|:-------|:----------|:-------------------|
| | | | |

### Monitor

| Issue | Current State | Threshold for Action |
|:------|:--------------|:---------------------|
| | | |

---

## Recommendations

### Immediate Actions

1. _[Action 1]_
2. _[Action 2]_

### Short-term Improvements

1. _[Improvement 1]_
2. _[Improvement 2]_

### Long-term Investments

1. _[Investment 1]_
2. _[Investment 2]_

---

## Methodology

### Test Sets Used

| Test Set | Size | Coverage | Last Updated |
|:---------|:-----|:---------|:-------------|
| _[Set 1]_ | _N_ | _[What it covers]_ | _[Date]_ |
| _[Set 2]_ | _N_ | _[What it covers]_ | _[Date]_ |

### Evaluation Methods

| Dimension | Method | Evaluator |
|:----------|:-------|:----------|
| Correctness | _[Auto/Human/Hybrid]_ | _[Details]_ |
| Relevance | _[Auto/Human/Hybrid]_ | _[Details]_ |
| Safety | _[Auto/Human/Hybrid]_ | _[Details]_ |

### Limitations

- _[Limitation 1]_
- _[Limitation 2]_

---

## Historical Trend

| Date | Version | Correctness | Relevance | Safety | Overall |
|:-----|:--------|:------------|:----------|:-------|:--------|
| | | | | | |
| | | | | | |
| | | | | | |

---

## Next Evaluation

**Scheduled:** _[Date]_  
**Trigger conditions:** _[What would cause earlier evaluation]_

---

*Template version: 1.0*  
*Last updated: [Date]*
