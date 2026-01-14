[← Back: Problem Framing](01_problem_framing.md) | [Next: Architecture →](03_architecture.md)

# Module 2: Success Metrics

Define what "working" means before writing code.

---

## The Core Principle

**You cannot improve what you cannot measure.**

But in AI systems, measurement is hard:
- Outputs are non-deterministic
- "Good" is often subjective
- Ground truth may not exist
- Users care about things that are hard to quantify

This module teaches you to define success metrics that are:
- **Measurable** — You can actually compute them
- **Meaningful** — They correlate with real value
- **Actionable** — They tell you what to improve

---

## RAG System Quality: Two Dimensions

A RAG system can fail in two independent ways:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   Query → [RETRIEVAL] → Documents → [GENERATION] → Answer   │
│              ↑                           ↑                  │
│         Can fail here              Can fail here            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Retrieval quality:** Did we find the right documents?
**Generation quality:** Given documents, did we produce the right answer?

These must be measured separately. A system with perfect retrieval and bad generation will fail. A system with bad retrieval and perfect generation will also fail.

---

## Retrieval Metrics

### What We're Measuring

Given a query, did we retrieve documents that contain the answer?

### Standard Metrics

| Metric | What It Measures | Formula |
|:-------|:-----------------|:--------|
| **Precision@k** | What fraction of retrieved docs are relevant? | relevant_retrieved / k |
| **Recall@k** | What fraction of relevant docs did we retrieve? | relevant_retrieved / total_relevant |
| **MRR** (Mean Reciprocal Rank) | How high is the first relevant doc? | 1 / rank_of_first_relevant |
| **NDCG** | Quality weighted by position | Complex; accounts for graded relevance |

### For This Project

Start with **Precision@5** and **Recall@5**:
- Practical to compute
- Interpretable to stakeholders
- Sufficient for detecting problems

### The Hard Part

These metrics require **ground truth** — you need to know which documents are actually relevant for each query.

This means building a golden dataset (covered below).

---

## Generation Metrics

### What We're Measuring

Given retrieved documents, did we produce a helpful, accurate answer?

### Standard Approaches

| Approach | What It Measures | Pros | Cons |
|:---------|:-----------------|:-----|:-----|
| **Human evaluation** | Human judges rate answers | Gold standard | Expensive, slow |
| **Automated metrics** (BLEU, ROUGE) | Text overlap with reference | Fast, cheap | Poor correlation with quality |
| **LLM-as-judge** | Another LLM rates the answer | Scalable, nuanced | Can be biased, costs money |
| **Task completion** | Did user solve their problem? | Measures real value | Hard to attribute |

### For This Project

Use **LLM-as-judge** with **human calibration**:
1. Define rating criteria
2. Have LLM rate answers on those criteria
3. Validate LLM ratings against human judgments
4. Adjust prompts until LLM matches human ratings

### LLM-as-Judge Criteria

Rate each answer on:

| Criterion | Question | Scale |
|:----------|:---------|:------|
| **Relevance** | Does the answer address the query? | 1-5 |
| **Accuracy** | Is the information correct (given the docs)? | 1-5 |
| **Completeness** | Does it cover what the user needs? | 1-5 |
| **Groundedness** | Is it based on retrieved docs, not hallucinated? | 1-5 |

**Overall quality** = weighted average (you decide the weights)

---

## Building a Golden Dataset

### What It Is

A curated set of (query, expected_answer, relevant_docs) triples that you use to:
- Benchmark system performance
- Detect regressions
- Compare approaches

### How to Build It

**Step 1: Gather Real Queries**
- Support ticket history
- User feedback
- Stakeholder examples
- Edge cases you anticipate

**Step 2: Categorize by Type**

| Query Type | Example | Why Include |
|:-----------|:--------|:------------|
| **Simple factual** | "What file formats are supported?" | Baseline — should always work |
| **How-to** | "How do I export to CSV?" | Common user need |
| **Troubleshooting** | "Why am I getting error 403?" | High value if automated |
| **Comparison** | "What's the difference between X and Y?" | Requires synthesis |
| **Complex/Multi-step** | "How do I set up SSO for my team?" | Stress test |
| **Out of scope** | "What's your company's revenue?" | Should gracefully fail |
| **Ambiguous** | "How do I do the thing?" | Tests clarification |

**Step 3: Define Ground Truth**

For each query:
1. Identify which documents contain the answer
2. Write or identify the ideal answer
3. Note any edge cases or variations

**Step 4: Target Size**

| Stage | Minimum | Recommended |
|:------|:--------|:------------|
| **Initial development** | 20 examples | 50 examples |
| **Pre-production** | 50 examples | 100 examples |
| **Production monitoring** | 100 examples | 200+ examples |

More is better, but 20 well-chosen examples beats 200 random ones.

---

## End-to-End Metrics

Beyond component metrics, measure the full system:

### Latency

| Metric | Target | Why |
|:-------|:-------|:----|
| **P50 latency** | < 2s | Typical experience |
| **P95 latency** | < 5s | Worst acceptable |
| **P99 latency** | < 10s | Outliers |

### Cost

| Metric | How to Calculate |
|:-------|:-----------------|
| **Cost per query** | (API costs + compute) / queries |
| **Cost per successful query** | Total cost / queries_that_helped |

### User-Facing (if measurable)

| Metric | What It Indicates |
|:-------|:------------------|
| **Answer acceptance rate** | % of answers users found helpful |
| **Escalation rate** | % of queries that became support tickets anyway |
| **Session length** | How many turns to resolve |

---

## Your Task: Define Your Metrics

Before building, complete this table:

### Retrieval Metrics

| Metric | How You'll Compute It | Target | Minimum Acceptable |
|:-------|:---------------------|:-------|:-------------------|
| | | | |
| | | | |

### Generation Metrics

| Metric | How You'll Compute It | Target | Minimum Acceptable |
|:-------|:---------------------|:-------|:-------------------|
| | | | |
| | | | |

### System Metrics

| Metric | How You'll Compute It | Target | Minimum Acceptable |
|:-------|:---------------------|:-------|:-------------------|
| Latency (P50) | | | |
| Latency (P95) | | | |
| Cost per query | | | |

### Golden Dataset Plan

| Query Type | Count | Examples |
|:-----------|:------|:---------|
| Simple factual | | |
| How-to | | |
| Troubleshooting | | |
| Comparison | | |
| Complex | | |
| Out of scope | | |
| **Total** | | |

---

## Common Mistakes

### 1. Measuring Only Retrieval OR Generation

Both matter. A system with 95% retrieval precision and 60% generation quality is not a 95% good system.

### 2. Using Metrics That Don't Correlate

BLEU and ROUGE scores often don't correlate with human judgment for RAG. Validate before trusting.

### 3. Setting Arbitrary Targets

"95% accuracy" sounds good but means nothing without context. What accuracy is achievable? What does the business need?

### 4. Ignoring Cost

A system that's 5% better but 3x more expensive may not be worth it. Include cost in your metrics.

### 5. One-Time Evaluation

Metrics need to be computed continuously. A system that worked last month may not work today.

---

## Decision: How Will You Measure Success?

Before moving on, you should have:

1. **Retrieval metrics defined** with computation method and targets
2. **Generation metrics defined** with evaluation criteria and targets  
3. **System metrics defined** with latency and cost targets
4. **Golden dataset plan** with query types and counts

If you can't define how you'll measure success, you're not ready to build.

---

## Checkpoint

### You Should Now Have

- [ ] 2-3 retrieval metrics with targets
- [ ] 2-3 generation metrics with evaluation criteria
- [ ] Latency and cost targets
- [ ] Golden dataset plan (types and counts)

### You Should Be Able To Answer

- How will you know if retrieval quality degrades by 10%?
- How will you know if generation quality is "good enough"?
- What query types are most important to get right?

---

[← Back: Problem Framing](01_problem_framing.md) | [Next: Architecture →](03_architecture.md)
