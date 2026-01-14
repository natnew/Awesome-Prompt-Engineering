[← Back: Evaluation Suite](04_evaluation_suite.md) | [Next: Synthesis →](06_synthesis.md)

# Module 5: Cost Model

Understand the real costs of your RAG system.

---

## The Core Principle

**Cost is a design constraint, not an afterthought.**

Most teams think about cost only after building. Then they're surprised:
- API bills are higher than expected
- Infrastructure costs weren't budgeted
- Maintenance overhead wasn't considered
- Error handling adds hidden costs

This module teaches you to model costs upfront so you can make informed trade-offs.

---

## The Full Cost Picture

RAG system costs are more than API calls:

```
┌─────────────────────────────────────────────────────────────────┐
│                        TOTAL COST                               │
│                                                                 │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│   │   Build     │  │    Run      │  │   Maintain  │            │
│   │   Costs     │  │   Costs     │  │   Costs     │            │
│   └─────────────┘  └─────────────┘  └─────────────┘            │
│         │                │                │                     │
│         ▼                ▼                ▼                     │
│   • Development     • API calls      • Monitoring              │
│   • Indexing        • Vector DB      • Updates                 │
│   • Testing         • Compute        • Bug fixes               │
│   • Infrastructure  • Evaluation     • Reindexing              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Build Costs (One-Time)

### Development Time

| Activity | Typical Hours | Your Estimate |
|:---------|:--------------|:--------------|
| Architecture & design | 8-16 | |
| Chunking & indexing | 8-16 | |
| Retrieval implementation | 4-8 | |
| Generation implementation | 4-8 | |
| Evaluation suite | 8-16 | |
| Testing & debugging | 8-16 | |
| Documentation | 4-8 | |
| **Total** | **44-88 hours** | |

At your hourly rate, development cost = hours × rate.

### Initial Indexing

| Component | Calculation | Your Numbers |
|:----------|:------------|:-------------|
| Documents | _____ pages × _____ tokens/page = _____ tokens | |
| Embedding cost | _____ tokens × $0.00002/1K tokens = $_____ | |
| Processing time | _____ hours | |
| **Total indexing cost** | | |

**Example:**
- 500 pages × 500 tokens/page = 250,000 tokens
- 250,000 tokens × $0.00002/1K = $0.005
- Embedding cost is often trivial; development time dominates

### Infrastructure Setup

| Component | Options | Monthly Cost |
|:----------|:--------|:-------------|
| Vector database | Pinecone Starter: Free / Standard: $70+ | |
| | Qdrant Cloud: Free tier / Paid | |
| | Self-hosted: Compute cost | |
| Application hosting | Serverless: Pay per use | |
| | VM: $20-100/month | |
| Monitoring | Basic: Free / Full: $20+ | |

---

## Run Costs (Per Query)

This is where most ongoing cost comes from.

### Per-Query Cost Breakdown

```
Query Cost = Embedding Cost + Retrieval Cost + Generation Cost

Embedding Cost = query_tokens × embedding_price_per_token
Retrieval Cost = queries × vector_search_price_per_query
Generation Cost = (input_tokens + output_tokens) × generation_price_per_token
```

### Detailed Calculation

**1. Query Embedding**

| Model | Price per 1K tokens | Your query size | Cost per query |
|:------|:-------------------|:----------------|:---------------|
| OpenAI text-embedding-3-small | $0.00002 | ~50 tokens | $0.000001 |
| OpenAI text-embedding-3-large | $0.00013 | ~50 tokens | $0.0000065 |
| Cohere embed-english-v3.0 | $0.0001 | ~50 tokens | $0.000005 |

**2. Vector Search**

| Provider | Price | Notes |
|:---------|:------|:------|
| Pinecone | $0.000002/query | Varies by tier |
| Qdrant Cloud | Included in tier | Depends on plan |
| Self-hosted | Compute cost | ~$0.00001/query |

**3. Generation (the big one)**

| Model | Input ($/1K) | Output ($/1K) | Typical query cost |
|:------|:-------------|:--------------|:-------------------|
| GPT-4o | $0.0025 | $0.01 | ~$0.015 |
| GPT-4o-mini | $0.00015 | $0.0006 | ~$0.001 |
| Claude 3.5 Sonnet | $0.003 | $0.015 | ~$0.02 |
| Claude 3.5 Haiku | $0.00025 | $0.00125 | ~$0.002 |

**Typical breakdown:**
- Embedding: < 1% of cost
- Retrieval: < 1% of cost
- Generation: > 95% of cost

### Your Cost Per Query

Complete this calculation:

| Component | Calculation | Cost |
|:----------|:------------|:-----|
| Query embedding | ___ tokens × $___ /1K = | $ |
| Vector search | 1 query × $___ = | $ |
| Generation (input) | ___ tokens × $___ /1K = | $ |
| Generation (output) | ___ tokens × $___ /1K = | $ |
| **Total per query** | | $ |

---

## Run Costs (Monthly)

### Query Volume Projection

| Metric | Your Estimate |
|:-------|:--------------|
| Expected queries/day | |
| Expected queries/month | |
| Peak queries/hour | |

### Monthly Calculation

| Cost Type | Calculation | Monthly Cost |
|:----------|:------------|:-------------|
| Query costs | queries/month × cost/query = | $ |
| Vector DB | Monthly tier cost | $ |
| Hosting | Monthly hosting cost | $ |
| Evaluation | eval_runs × cost/run | $ |
| **Total monthly** | | $ |

### Scenario Planning

| Scenario | Queries/Month | Monthly Cost |
|:---------|:--------------|:-------------|
| Conservative | | $ |
| Expected | | $ |
| High growth | | $ |

---

## Maintenance Costs

Often overlooked, always significant.

### Ongoing Maintenance

| Activity | Frequency | Hours/Month | Monthly Cost |
|:---------|:----------|:------------|:-------------|
| Monitoring & alerting | Continuous | 2-4 | $ |
| Bug fixes | As needed | 4-8 | $ |
| Performance tuning | Monthly | 2-4 | $ |
| Content updates | Weekly | 4-8 | $ |
| Reindexing | Monthly | 1-2 | $ |
| **Total maintenance** | | | $ |

### Content Update Costs

When documentation changes:

| Activity | Frequency | Cost |
|:----------|:----------|:-----|
| Detect changed docs | Weekly | Time |
| Re-chunk affected docs | Weekly | Time |
| Re-embed changed chunks | Weekly | ~$0.01/update |
| Update vector store | Weekly | Minimal |
| Validate quality | Weekly | Eval cost |

---

## Cost Optimization Strategies

### Reduce Generation Costs (Biggest Impact)

| Strategy | Savings | Trade-off |
|:---------|:--------|:----------|
| Use smaller model | 10-20x | Potential quality loss |
| Cache common queries | 20-50% | Stale answers possible |
| Reduce context size | 20-40% | May miss relevant info |
| Shorter max output | 10-30% | Less complete answers |

### Reduce Retrieval Costs

| Strategy | Savings | Trade-off |
|:---------|:--------|:----------|
| Fewer chunks retrieved | Minimal | Lower recall |
| Simpler reranking | Some | Lower precision |
| Tiered retrieval | Some | Complexity |

### Operational Efficiency

| Strategy | Savings | Trade-off |
|:---------|:--------|:----------|
| Batch similar queries | 10-20% | Latency increase |
| Off-peak processing | 10-30% | Timing constraints |
| Aggressive caching | 30-50% | Cache invalidation complexity |

---

## Cost vs. Quality Trade-offs

### Model Selection Example

| Option | Quality Score | Cost/Query | Monthly (10K queries) |
|:-------|:--------------|:-----------|:---------------------|
| GPT-4o | 4.5/5 | $0.015 | $150 |
| GPT-4o-mini | 4.0/5 | $0.001 | $10 |
| Claude Haiku | 3.8/5 | $0.002 | $20 |

**Question:** Is 0.5 quality points worth $140/month?

This is a business decision, not a technical one. Document your choice.

### Context Size Example

| Chunks Retrieved | Quality | Input Tokens | Cost/Query |
|:-----------------|:--------|:-------------|:-----------|
| 3 | 3.5/5 | 1,500 | $0.005 |
| 5 | 4.0/5 | 2,500 | $0.008 |
| 10 | 4.2/5 | 5,000 | $0.015 |

**Question:** Is 0.2 quality points worth 2x cost?

---

## Your Task: Build Your Cost Model

Complete the cost model template in `artifacts/cost_model_template.md`.

### Required Sections

1. **Build costs**
   - Development hours and rate
   - Initial indexing cost
   - Infrastructure setup

2. **Per-query costs**
   - Embedding
   - Retrieval
   - Generation
   - Total

3. **Monthly projections**
   - Conservative scenario
   - Expected scenario
   - High growth scenario

4. **Maintenance costs**
   - Monitoring
   - Updates
   - Support

5. **Total cost of ownership**
   - Year 1 total
   - Steady-state monthly

### Cost Model Summary

| Metric | Your Calculation |
|:-------|:-----------------|
| Cost per query | $ |
| Monthly cost (expected) | $ |
| Annual cost (Year 1) | $ |
| Break-even queries | |

---

## ROI Calculation

### Value Side

What's the value of a successful query?

| Scenario | Calculation |
|:---------|:------------|
| Support ticket avoided | Cost of ticket × deflection rate |
| User time saved | User's time × average resolution time |
| Support team time saved | Agent's time × tickets automated |

**Example:**
- Cost per support ticket: $25
- Deflection rate: 40%
- Value per query: $25 × 0.4 = $10

### ROI Calculation

```
ROI = (Value Generated - Total Cost) / Total Cost

Value Generated = queries × value_per_query × success_rate
Total Cost = build_cost + (monthly_cost × 12)
```

**Example:**
- 10,000 queries/month
- Value per query: $10
- Success rate: 60%
- Monthly value: 10,000 × $10 × 0.6 = $60,000

- Build cost: $10,000
- Monthly cost: $500
- Year 1 cost: $10,000 + ($500 × 12) = $16,000

- Year 1 ROI: ($720,000 - $16,000) / $16,000 = 44x

---

## Communicating Costs to Stakeholders

### What Leadership Wants to Know

| Question | Your Answer |
|:---------|:------------|
| How much will this cost to build? | $ |
| How much will it cost to run monthly? | $ |
| What's the expected ROI? | X% or Xx |
| When will we break even? | X months |
| What are the risks? | List top 3 |

### Cost Summary Slide

```
RAG System Cost Summary
───────────────────────

Build Cost:     $XX,XXX  (one-time)
Monthly Cost:   $X,XXX   (at expected volume)
Annual Cost:    $XX,XXX  (Year 1)

Expected Value: $XXX,XXX (Year 1)
ROI:            XX%

Break-even:     XX,XXX queries
Timeline:       X months
```

---

## Checkpoint

### You Should Now Have

- [ ] Cost per query calculated
- [ ] Monthly cost projections for 3 scenarios
- [ ] Maintenance cost estimate
- [ ] Total cost of ownership for Year 1
- [ ] ROI calculation (if value is quantifiable)

### You Should Be Able To Answer

- What does each query cost?
- What's the biggest cost driver?
- What would 10x volume do to costs?
- What's the ROI (or how would you measure it)?

---

[← Back: Evaluation Suite](04_evaluation_suite.md) | [Next: Synthesis →](06_synthesis.md)
