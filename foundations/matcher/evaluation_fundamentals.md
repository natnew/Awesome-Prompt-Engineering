# Evaluation Fundamentals

*How to measure AI system quality.*

**Time:** 20 minutes  
**Competencies:** [Evaluation & Measurement](../COMPETENCIES.md#2-evaluation--measurement)

---

## Why Evaluation Matters

Without evaluation, you're guessing:
- Is this prompt better than that one?
- Is the system good enough to ship?
- Did that change help or hurt?
- Are we improving over time?

Evaluation transforms subjective impressions into measurable data.

---

## The Quality Dimensions

AI output quality is multidimensional. You can't capture it with a single number.

### Core Dimensions

| Dimension | Question |
|:----------|:---------|
| **Correctness** | Is the output factually accurate? |
| **Relevance** | Does it address what was asked? |
| **Completeness** | Is anything important missing? |
| **Safety** | Does it avoid harmful content? |
| **Coherence** | Is it well-structured and logical? |

### Operational Dimensions

| Dimension | Question |
|:----------|:---------|
| **Latency** | Is it fast enough? |
| **Cost** | Is it affordable at scale? |
| **Consistency** | Are outputs stable across runs? |

### Which Dimensions Matter?

Depends on your use case:

| Use Case | Primary Dimensions |
|:---------|:-------------------|
| Factual Q&A | Correctness, Relevance |
| Creative writing | Coherence, Relevance |
| Code generation | Correctness, Safety, Completeness |
| Customer support | Relevance, Safety, Tone |
| Summarization | Correctness, Completeness, Conciseness |

---

## Evaluation Methods

### Method 1: Automatic Metrics

Computed without human judgment.

**Examples:**
- Exact match (output == expected)
- String containment (expected substring present)
- BLEU, ROUGE (text similarity scores)
- Code: passes tests / compiles
- Latency, token count, cost

**Pros:** Fast, cheap, reproducible  
**Cons:** Often miss nuance, can be gamed

### Method 2: Human Evaluation

Humans judge output quality.

**Examples:**
- Rating scales (1-5 quality)
- Pairwise comparison (A vs B)
- Categorical (correct/incorrect)
- Open-ended feedback

**Pros:** Captures nuance, aligns with real needs  
**Cons:** Slow, expensive, potentially inconsistent

### Method 3: LLM-as-Judge

Use another LLM to evaluate outputs.

**Examples:**
```
Evaluate this response for accuracy:
[response]

Rate on a scale of 1-5 where:
1 = Completely incorrect
5 = Fully accurate
```

**Pros:** Faster than humans, captures more nuance than simple metrics  
**Cons:** Has its own biases and errors, needs calibration

### Choosing Methods

| Situation | Recommended Method |
|:----------|:-------------------|
| Development iteration | Automatic + spot-check human |
| Pre-deployment validation | Human evaluation sample |
| Production monitoring | Automatic metrics + sampled human |
| A/B testing | Statistical comparison of automatic metrics |
| Edge case coverage | Manual test suite |

---

## Building Test Sets

Your evaluation is only as good as your test set.

### Test Set Requirements

| Property | Why It Matters |
|:---------|:---------------|
| **Representative** | Matches real usage distribution |
| **Diverse** | Covers different scenarios |
| **Challenging** | Includes hard cases |
| **Stable** | Doesn't change arbitrarily |
| **Labeled** | Has ground truth for comparison |

### Test Set Sources

1. **Historical data** — Real past queries with known good responses
2. **Synthetic generation** — Programmatically create test cases
3. **Expert creation** — Subject matter experts write cases
4. **Adversarial** — Intentionally difficult cases
5. **Production sampling** — Random sample of live traffic

### How Many Test Cases?

| Purpose | Typical Size |
|:--------|:-------------|
| Quick iteration | 20-50 |
| Serious evaluation | 100-500 |
| Production validation | 500+ |
| Benchmark publication | 1000+ |

**Trade-off:** More cases = more confidence, but also more cost and time.

---

## The Evaluation Loop

### Build → Measure → Learn

```
┌─────────────────────────────────────────────┐
│                                              │
│  ┌─────────┐    ┌──────────┐    ┌────────┐  │
│  │  Build  │ → │  Measure  │ → │  Learn │  │
│  │ (change │    │  (run     │    │(analyze│  │
│  │ prompt) │    │  eval)    │    │results)│  │
│  └─────────┘    └──────────┘    └────────┘  │
│       ↑                              │       │
│       └──────────────────────────────┘       │
│                                              │
└─────────────────────────────────────────────┘
```

### Before Building

1. Define success criteria
2. Choose dimensions to measure
3. Build initial test set
4. Establish baseline

### During Development

1. Run evals after each change
2. Track multiple dimensions (not just primary)
3. Watch for regressions
4. Investigate failures

### Before Deployment

1. Full evaluation on complete test set
2. Human review of sample
3. Compare to baseline
4. Make go/no-go decision

### In Production

1. Monitor automatic metrics
2. Sample for human review
3. Track drift over time
4. Alert on degradation

---

## Common Pitfalls

### Overfitting to Test Set

**Problem:** System is optimized for test cases but fails on real usage.

**Solution:** 
- Keep a held-out test set you don't use during development
- Refresh test set periodically
- Sample production traffic for evaluation

### Goodhart's Law

"When a measure becomes a target, it ceases to be a good measure."

**Problem:** Optimizing for metric instead of actual quality.

**Example:** Optimizing for BLEU score produces text that scores well but reads poorly.

**Solution:** Use multiple metrics. Include human evaluation.

### Sample Size Issues

**Problem:** Drawing conclusions from too few examples.

**Example:** "100% accuracy!" (on 3 test cases)

**Solution:** Report confidence intervals. Use statistical tests.

### Label Quality

**Problem:** Ground truth labels are wrong or inconsistent.

**Solution:** Multiple annotators. Inter-annotator agreement checks. Review disagreements.

---

## Evaluation Metrics in Practice

### Binary Classification

For right/wrong tasks:

| Metric | Formula | When to Use |
|:-------|:--------|:------------|
| Accuracy | Correct / Total | Balanced classes |
| Precision | True Positives / Predicted Positives | When false positives are costly |
| Recall | True Positives / Actual Positives | When false negatives are costly |
| F1 | 2 × (P × R) / (P + R) | Balance precision and recall |

### Text Quality

For generated text:

| Metric | What It Measures | Limitations |
|:-------|:-----------------|:------------|
| BLEU | N-gram overlap with reference | Doesn't capture meaning |
| ROUGE | Recall-oriented overlap | Same |
| BERTScore | Semantic similarity via embeddings | Better, but imperfect |
| Human rating | Actual quality | Expensive, slow |

### Retrieval (RAG)

For information retrieval:

| Metric | What It Measures |
|:-------|:-----------------|
| Precision@K | Relevant results in top K |
| Recall@K | Fraction of relevant results retrieved |
| MRR | Position of first relevant result |
| NDCG | Graded relevance with position discount |

### Cost/Performance

| Metric | What It Measures |
|:-------|:-----------------|
| Latency (p50, p95, p99) | Response time distribution |
| Tokens per request | Resource consumption |
| Cost per request | Economic efficiency |
| Throughput | Requests per second |

---

## Setting Thresholds

### How Good Is Good Enough?

Thresholds depend on:
- Use case criticality
- User expectations
- Competitive alternatives
- Cost of errors

### Example Thresholds

| Dimension | High-Stakes | Medium-Stakes | Low-Stakes |
|:----------|:------------|:--------------|:-----------|
| Correctness | >95% | >85% | >70% |
| Safety | >99% | >95% | >90% |
| Latency p95 | <1s | <3s | <10s |

### Threshold-Setting Process

1. Understand user requirements
2. Benchmark current solutions
3. Define acceptable and target levels
4. Adjust based on reality

---

## Practical Exercise

### Design an Evaluation

For a customer support chatbot:

1. **What dimensions matter most?**
   - Correctness (is information accurate?)
   - Helpfulness (did it solve the problem?)
   - Safety (no inappropriate content?)
   - Tone (professional but friendly?)

2. **What test cases do you need?**
   - Common questions (50%)
   - Edge cases (20%)
   - Adversarial inputs (15%)
   - Multi-turn conversations (15%)

3. **What methods will you use?**
   - Automatic: Contains required keywords, response time
   - LLM-as-judge: Helpfulness, tone
   - Human: Sample review, safety validation

4. **What are your thresholds?**
   - Correctness: >90%
   - Helpfulness: >80%
   - Safety: >99%
   - Latency p95: <3s

---

## Summary

| Concept | Key Point |
|:--------|:----------|
| Dimensions | Quality is multidimensional |
| Methods | Automatic, human, LLM-as-judge each have trade-offs |
| Test sets | Must be representative, diverse, challenging |
| Loop | Build → Measure → Learn, continuously |
| Pitfalls | Overfitting, Goodhart's Law, sample size |
| Thresholds | Depend on use case and stakes |

---

## Further Reading

- [The Measurement Problem](measurement_problem.md) — Why evaluation is hard
- [Evaluation-First Pattern](../patterns/evaluation_first.md) — Applying evaluation in practice
- [Evaluation Scorecard Template](../templates/evaluation/evaluation_scorecard.md) — Tracking metrics
