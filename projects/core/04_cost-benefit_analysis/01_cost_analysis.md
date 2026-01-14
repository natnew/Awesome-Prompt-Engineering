[← Back to Project](README.md) | [Next: Benefit Estimation →](02_benefit_estimation.md)

# Module 1: Cost Analysis

Calculate the real costs, not just the obvious ones.

---

## The Cost Iceberg

Most AI feature cost estimates are wrong because they only count the visible costs:

```
                    VISIBLE COSTS
                   ╱             ╲
                  ╱   API calls   ╲
                 ╱   Infrastructure╲
                ╱                   ╲
═══════════════════════════════════════════════════ WATERLINE
               ╲                     ╱
                ╲   Development     ╱
                 ╲  Maintenance    ╱
                  ╲ Opportunity   ╱
                   ╲ Training    ╱
                    ╲ Support   ╱
                     ╲ Risk    ╱
                      ╲      ╱
                       HIDDEN COSTS
```

This module teaches you to see the whole iceberg.

---

## Cost Categories

### Category 1: Development Costs (One-Time)

**What to count:**
- Engineering hours
- Design hours
- Product management
- QA/Testing
- Security review
- Documentation

**How to estimate:**

| Role | Hours | Loaded Rate | Total |
|:-----|:------|:------------|:------|
| Senior Engineer | | $150-250/hr | |
| Mid-level Engineer | | $100-150/hr | |
| Designer | | $100-150/hr | |
| PM | | $100-150/hr | |
| QA | | $75-125/hr | |
| **Total** | | | |

**Loaded rate includes:** Salary + benefits + overhead (typically 1.3-1.5x salary)

**Typical scope for AI features:**

| Feature Type | Engineering Weeks | Notes |
|:-------------|:------------------|:------|
| Simple integration | 2-4 weeks | API wrapper, basic UI |
| RAG/Search | 4-8 weeks | Indexing, retrieval, UI |
| Agent-based | 8-16 weeks | Tool integration, safety |
| Custom model | 16-32 weeks | Training, evaluation, deployment |

**Don't forget:**
- Ramp-up time (learning new tools/APIs)
- Integration with existing systems
- Edge case handling (always longer than expected)
- Testing and iteration

---

### Category 2: Infrastructure Costs (Ongoing)

**Components to consider:**

#### LLM API Costs

| Model | Input Cost | Output Cost | Typical Query | Cost/Query |
|:------|:-----------|:------------|:--------------|:-----------|
| GPT-4o | $2.50/1M | $10/1M | 2K in, 500 out | ~$0.01 |
| GPT-4o-mini | $0.15/1M | $0.60/1M | 2K in, 500 out | ~$0.0006 |
| Claude Sonnet | $3/1M | $15/1M | 2K in, 500 out | ~$0.014 |
| Claude Haiku | $0.25/1M | $1.25/1M | 2K in, 500 out | ~$0.0011 |

**Calculate your costs:**
```
Monthly LLM cost = queries/month × tokens/query × $/token
                 = _____ × _____ × $_____ = $_____
```

#### Embedding Costs

| Model | Cost | Notes |
|:------|:-----|:------|
| OpenAI text-embedding-3-small | $0.02/1M tokens | Recommended for most |
| OpenAI text-embedding-3-large | $0.13/1M tokens | Higher quality |

**Calculate:**
```
Initial indexing = documents × tokens/doc × $/token
                 = _____ × _____ × $_____ = $_____

Query embedding = queries/month × tokens/query × $/token
               = _____ × _____ × $_____ = $_____/month
```

#### Vector Database Costs

| Provider | Pricing | Notes |
|:---------|:--------|:------|
| Pinecone | Free tier, then ~$70+/month | Managed |
| Weaviate Cloud | Free tier, then usage-based | Managed |
| Qdrant Cloud | Free tier, then usage-based | Managed |
| Self-hosted | Compute costs | ~$50-200/month for small |

#### Compute/Hosting

| Component | Typical Cost |
|:----------|:-------------|
| Application server | $50-200/month |
| Caching (Redis) | $15-50/month |
| Monitoring | $0-50/month |

---

### Category 3: Maintenance Costs (Ongoing)

**The part everyone forgets.**

| Activity | Hours/Month | Rate | Monthly Cost |
|:---------|:------------|:-----|:-------------|
| Bug fixes | 2-8 hrs | $ | $ |
| Performance tuning | 2-4 hrs | $ | $ |
| Model/API updates | 2-4 hrs | $ | $ |
| Content updates | 4-8 hrs | $ | $ |
| Monitoring/alerts | 1-2 hrs | $ | $ |
| **Total** | | | $ |

**Expect maintenance to be 15-25% of initial development cost per year.**

---

### Category 4: Hidden Costs

#### Opportunity Cost

What else could the team build with this time?

```
Opportunity cost = development_hours × value_of_alternative
```

Questions to ask:
- What's on the roadmap that will be delayed?
- What's the value of those delayed features?
- Is this the highest-impact use of engineering time?

#### Training Costs

| Who | Time | Purpose |
|:----|:-----|:--------|
| Engineering team | | Learning new tools |
| Support team | | Understanding new feature |
| Sales team | | Selling the feature |
| Customers | | Using the feature |

#### Support Costs

New feature = new support tickets:
- "How does this work?"
- "Why did it give me X?"
- "It gave me a wrong answer"

```
Additional support cost = new_tickets/month × cost_per_ticket
```

#### Risk Costs

Not a direct cost, but should be provisioned:
- What if the model API price increases 50%?
- What if we need to switch providers?
- What if it doesn't work as expected?

---

## Cost Estimation Worksheet

### Development (One-Time)

| Item | Low | Expected | High |
|:-----|:----|:---------|:-----|
| Engineering | $____ | $____ | $____ |
| Design | $____ | $____ | $____ |
| PM | $____ | $____ | $____ |
| QA | $____ | $____ | $____ |
| Security | $____ | $____ | $____ |
| **Total Development** | $____ | $____ | $____ |

### Infrastructure (Monthly)

| Item | Low | Expected | High |
|:-----|:----|:---------|:-----|
| LLM API | $____ | $____ | $____ |
| Embeddings | $____ | $____ | $____ |
| Vector DB | $____ | $____ | $____ |
| Compute | $____ | $____ | $____ |
| **Total Monthly** | $____ | $____ | $____ |

### Maintenance (Monthly)

| Item | Low | Expected | High |
|:-----|:----|:---------|:-----|
| Engineering | $____ | $____ | $____ |
| Content updates | $____ | $____ | $____ |
| Monitoring | $____ | $____ | $____ |
| **Total Monthly** | $____ | $____ | $____ |

### Hidden Costs

| Item | Estimate | Notes |
|:-----|:---------|:------|
| Opportunity cost | $____ | |
| Training | $____ | |
| Support increase | $____/month | |
| Risk provision | $____ | |

### Total Cost of Ownership

| Timeframe | Low | Expected | High |
|:----------|:----|:---------|:-----|
| Year 1 | $____ | $____ | $____ |
| Year 2 | $____ | $____ | $____ |
| Year 3 | $____ | $____ | $____ |
| **3-Year Total** | $____ | $____ | $____ |

---

## Cost Estimation Principles

### Principle 1: Use Ranges, Not Point Estimates

Nobody knows exactly what something will cost. Use:
- **Low**: Best case, everything goes smoothly
- **Expected**: Realistic, accounting for normal delays
- **High**: Pessimistic, accounting for problems

### Principle 2: Estimate Bottom-Up

Don't say "this will cost $100K." Instead:
- List every component
- Estimate each component
- Sum them up
- Add contingency (20-30%)

### Principle 3: Validate Against Benchmarks

- How much did similar features cost?
- What do industry benchmarks say?
- What do vendors quote?

### Principle 4: Include Variance Costs

Some costs are predictable; others vary:
- **Fixed**: Development, monthly hosting
- **Variable**: API calls, storage
- **Unexpected**: Support, bugs, changes

Plan for variable costs at expected + some buffer.

---

## Common Mistakes

### Mistake 1: Forgetting Maintenance

"We'll build it and it'll just work."

Reality: AI features need ongoing maintenance. Plan for it.

### Mistake 2: Underestimating API Costs at Scale

Works fine in testing, expensive at scale.

Always calculate:
```
Monthly cost at 10x current volume = ?
Monthly cost at 100x = ?
```

### Mistake 3: Ignoring Hidden Costs

Opportunity cost is real cost. Training is real cost. Support is real cost.

### Mistake 4: Using List Prices

Vendors often discount. But also:
- Rate limits may require higher tiers
- Enterprise features may be required
- Support may cost extra

Get real quotes before finalizing.

---

## Your Task

Complete the Cost Estimation Worksheet above with:
- Three-point estimates (low, expected, high)
- All categories (development, infrastructure, maintenance, hidden)
- 3-year total cost of ownership

You'll use this in the synthesis module to make your recommendation.

---

## Key Insight

**The cost of an AI feature is not what you pay the LLM provider.**

It's development + infrastructure + maintenance + opportunity cost + risk provision.

Most cost estimates are 2-3x lower than reality because they forget the hidden costs.

---

[← Back to Project](README.md) | [Next: Benefit Estimation →](02_benefit_estimation.md)
