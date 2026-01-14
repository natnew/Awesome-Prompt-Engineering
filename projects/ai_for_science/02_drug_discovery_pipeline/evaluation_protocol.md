# Evaluation Protocol

## Overview

This document defines how the drug discovery pipeline is evaluated for scientific rigour and accuracy.

---

## Evaluation Dimensions

### Dimension Summary

| Dimension | Weight | Key Metric | Target |
|:----------|:-------|:-----------|:-------|
| Citation Integrity | 0.25 | Validity rate | 100% |
| Factual Accuracy | 0.25 | Expert rating | >4/5 |
| Coverage | 0.20 | Reference recall | >80% |
| Calibration | 0.15 | ECE | <0.1 |
| Conflict Handling | 0.15 | Detection rate | >85% |

---

## Evaluation Methods

### Method 1: Automated Citation Validation

**Frequency:** Every query

**Process:**
1. Extract all citations from output
2. Verify each citation exists in source database
3. Assess relevance to associated claim
4. Report validity metrics

**Metrics:**
| Metric | Calculation | Target |
|:-------|:------------|:-------|
| Existence rate | Citations found / Total citations | 100% |
| Relevance rate | Relevant citations / Total citations | >95% |

**Pass criteria:** Zero invalid citations

---

### Method 2: Expert Evaluation

**Frequency:** Monthly (sampled)

**Evaluators:**
- Minimum 2 domain experts per evaluation
- Expertise in relevant scientific area
- Independent evaluation, then reconciliation

**Evaluation Rubric:**

| Dimension | 5 | 4 | 3 | 2 | 1 |
|:----------|:--|:--|:--|:--|:--|
| **Accuracy** | All facts correct, nuanced | Minor errors only | Some errors | Multiple errors | Significant errors |
| **Coverage** | Comprehensive | Minor gaps | Moderate gaps | Major gaps | Critical gaps |
| **Interpretation** | Sophisticated | Appropriate | Adequate | Simplistic | Incorrect |
| **Synthesis** | Insightful | Good integration | Adequate | Disjointed | Poor |
| **Uncertainty** | Perfectly calibrated | Appropriate | Adequate | Sometimes wrong | Miscalibrated |

**Process:**
1. Select sample of queries (N=20 minimum)
2. Distribute to evaluators (blind to each other)
3. Evaluators rate each dimension
4. Calculate inter-rater reliability
5. Reconcile significant disagreements
6. Compute aggregate scores

---

### Method 3: Reference Set Comparison

**Frequency:** Weekly

**Reference set requirements:**
- Expert-created gold standard answers
- Known key claims and citations
- Known conflicts to detect
- Minimum 50 queries

**Metrics:**
| Metric | Calculation | Target |
|:-------|:------------|:-------|
| Claim recall | Expected claims found / Total expected | >80% |
| Citation recall | Key citations found / Total key citations | >85% |
| Conflict recall | Conflicts detected / Known conflicts | >85% |
| Precision | Correct claims / All claims made | >90% |

---

### Method 4: Calibration Assessment

**Frequency:** Monthly

**Process:**
1. Collect all claims with confidence scores
2. Expert evaluation of claim correctness
3. Bin by confidence level
4. Calculate accuracy per bin
5. Compute Expected Calibration Error

**Calibration target:** ECE < 0.1

**Calibration curve requirements:**
- 10 confidence bins (0-10%, 10-20%, etc.)
- Minimum 20 claims per bin for significance
- Plot expected vs. actual accuracy

---

### Method 5: Adversarial Testing

**Frequency:** Quarterly

**Test categories:**

| Category | Examples | Expected Behaviour |
|:---------|:---------|:-------------------|
| Non-existent entities | Fake gene names, fake compounds | Report not found |
| Retracted work | Queries about retracted papers | Flag retraction |
| Outdated information | Old guidelines superseded | Include recency context |
| Conflicting requests | "Prove X and disprove X" | Handle both fairly |
| Hallucination probes | Very specific fake claims | Never confirm false |

**Pass criteria:** No hallucinations, appropriate responses to all adversarial inputs

---

## Test Suite

### Test Case Template

```yaml
test_case:
  id: [Unique ID]
  category: [known_answer | coverage | conflict | hallucination | adversarial]
  query: [Research question]
  
  expected_outputs:
    key_claims: [List of claims that should appear]
    key_citations: [Citations that should be included]
    conflicts_to_detect: [Known conflicts]
    confidence_range: [Expected confidence level]
  
  negative_checks:
    should_not_contain: [Things that shouldn't appear]
    hallucination_probes: [Specific false claims to avoid]
  
  evaluation_criteria:
    claim_coverage: [Minimum % of key claims]
    citation_coverage: [Minimum % of key citations]
    conflict_detection: [Required conflicts to find]
```

### Minimum Test Suite Size

| Category | Minimum Tests |
|:---------|:--------------|
| Known-answer | 25 |
| Coverage | 15 |
| Conflict detection | 10 |
| Calibration | 30 |
| Adversarial | 20 |
| **Total** | **100** |

---

## Evaluation Schedule

### Per-Query (Automated)

| Check | Method | Threshold |
|:------|:-------|:----------|
| Citation existence | API lookup | 100% |
| Output structure | Schema validation | Pass |

### Daily

| Evaluation | Size | Threshold |
|:-----------|:-----|:----------|
| Automated test suite | Full suite | >95% pass |
| Regression tests | Critical tests | 100% pass |

### Weekly

| Evaluation | Size | Threshold |
|:-----------|:-----|:----------|
| Reference set comparison | Full reference set | >80% recall |
| Coverage analysis | Sample (N=50) | >85% coverage |

### Monthly

| Evaluation | Size | Threshold |
|:-----------|:-----|:----------|
| Expert evaluation | Sample (N=20) | >4.0 average |
| Calibration assessment | All claims from month | ECE <0.1 |

### Quarterly

| Evaluation | Size | Threshold |
|:-----------|:-----|:----------|
| Adversarial testing | Full adversarial suite | 100% appropriate |
| Deep expert review | Sample (N=10) | Detailed feedback |

---

## Failure Response

### Critical Failures (Immediate)

| Failure | Definition | Response |
|:--------|:-----------|:---------|
| Hallucinated citation | Citation doesn't exist | Stop, investigate, fix |
| Dangerous misinformation | Factually wrong with potential harm | Stop, investigate, fix |
| Zero coverage | Missed all key information | Investigate, adjust |

### Serious Failures (Within 24h)

| Failure | Definition | Response |
|:--------|:-----------|:---------|
| Missed conflict | Known conflict not surfaced | Add to test suite, investigate |
| Systematic bias | Pattern of incorrect emphasis | Root cause analysis |
| Calibration drift | ECE significantly increased | Recalibrate |

### Minor Failures (Within Sprint)

| Failure | Definition | Response |
|:--------|:-----------|:---------|
| Low coverage query | Single query with gaps | Add to test suite |
| Suboptimal synthesis | Could be better organised | Track for improvement |

---

## Reporting

### Daily Report

```
EVALUATION REPORT: [Date]

Test Suite Results:
- Total tests: [N]
- Passed: [N] ([%])
- Failed: [N] ([%])

Critical Metrics:
- Citation validity: [%]
- Hallucination incidents: [N]

Failed Tests:
- [Test ID]: [Failure reason]
- ...

Action Required: [Yes/No]
```

### Weekly Report

```
WEEKLY EVALUATION SUMMARY: [Week]

Dimension Scores:
- Citation Integrity: [Score]
- Factual Accuracy: [Score]
- Coverage: [Score]
- Calibration: [ECE]
- Conflict Handling: [Score]

Trends:
- [Improving/Stable/Declining] vs last week

Reference Set Performance:
- Claim recall: [%]
- Citation recall: [%]
- Conflict recall: [%]

Issues Identified:
- [Issue 1]
- [Issue 2]

Actions Taken:
- [Action 1]
- [Action 2]
```

### Monthly Report

```
MONTHLY EVALUATION REPORT: [Month]

Overall Score: [X/100]

Expert Evaluation:
- Accuracy: [Score]
- Coverage: [Score]
- Interpretation: [Score]
- Synthesis: [Score]
- Uncertainty: [Score]
- Inter-rater reliability: [Score]

Calibration:
- ECE: [Value]
- Calibration curve: [Chart]

Trend Analysis:
- [3-month trend for each dimension]

Recommendations:
- [Recommendation 1]
- [Recommendation 2]
```

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Quality Lead | | |
| Domain Expert | | |
| System Owner | | |
