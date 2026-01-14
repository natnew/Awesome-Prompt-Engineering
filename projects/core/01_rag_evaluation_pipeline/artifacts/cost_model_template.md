# Cost Model: [Project Name]

## Metadata

| Field | Value |
|:------|:------|
| **Project** | [Your project name] |
| **Date** | YYYY-MM-DD |
| **Author** | [Your name] |
| **Version** | 1.0 |

---

## Executive Summary

| Metric | Value |
|:-------|:------|
| **Cost per query** | $X.XX |
| **Monthly cost (expected)** | $X,XXX |
| **Annual cost (Year 1)** | $XX,XXX |
| **Expected ROI** | XX% or N/A |
| **Break-even** | X,XXX queries or N/A |

---

## 1. Build Costs (One-Time)

### 1.1 Development Time

| Activity | Hours | Rate ($/hr) | Cost |
|:---------|:------|:------------|:-----|
| Architecture & design | | $ | $ |
| Chunking & indexing implementation | | $ | $ |
| Retrieval implementation | | $ | $ |
| Generation implementation | | $ | $ |
| Evaluation suite | | $ | $ |
| Testing & debugging | | $ | $ |
| Documentation | | $ | $ |
| **Total Development** | | | **$** |

### 1.2 Initial Indexing

| Component | Calculation | Cost |
|:----------|:------------|:-----|
| Document count | _____ documents | — |
| Total tokens | _____ docs × _____ tokens/doc = _____ tokens | — |
| Embedding cost | _____ tokens × $_____ /1K = | $ |
| Processing compute | _____ hours × $_____ /hr = | $ |
| **Total Indexing** | | **$** |

### 1.3 Infrastructure Setup

| Component | Choice | Setup Cost |
|:----------|:-------|:-----------|
| Vector database | [Provider/Self-hosted] | $ |
| Application hosting | [Provider] | $ |
| Monitoring setup | [Tool] | $ |
| CI/CD pipeline | [Tool] | $ |
| **Total Infrastructure Setup** | | **$** |

### 1.4 Total Build Cost

| Category | Cost |
|:---------|:-----|
| Development | $ |
| Initial Indexing | $ |
| Infrastructure Setup | $ |
| **Total Build Cost** | **$** |

---

## 2. Per-Query Costs

### 2.1 Query Processing Breakdown

| Component | Calculation | Cost |
|:----------|:------------|:-----|
| **Query embedding** | | |
| └ Tokens per query | ~_____ tokens | — |
| └ Embedding model | [Model name] | — |
| └ Cost | _____ tokens × $_____ /1K = | $ |
| | | |
| **Vector search** | | |
| └ Provider | [Provider] | — |
| └ Cost per query | | $ |
| | | |
| **Generation** | | |
| └ Input tokens (query + context) | ~_____ tokens | — |
| └ Output tokens | ~_____ tokens | — |
| └ Model | [Model name] | — |
| └ Input cost | _____ × $_____ /1K = | $ |
| └ Output cost | _____ × $_____ /1K = | $ |
| | | |
| **Total per query** | | **$** |

### 2.2 Cost Breakdown Visualization

```
Per-Query Cost: $X.XX
────────────────────────────────────────
Embedding:   $X.XX  ( X%)  ████
Retrieval:   $X.XX  ( X%)  █
Generation:  $X.XX  (XX%)  ████████████████████
────────────────────────────────────────
```

---

## 3. Monthly Operating Costs

### 3.1 Query Volume Scenarios

| Scenario | Queries/Day | Queries/Month |
|:---------|:------------|:--------------|
| Conservative | | |
| Expected | | |
| High Growth | | |

### 3.2 Monthly Cost Calculation

#### Conservative Scenario

| Component | Calculation | Monthly Cost |
|:----------|:------------|:-------------|
| Query costs | _____ queries × $_____ = | $ |
| Vector DB | [Tier/usage] | $ |
| Hosting | [Tier/usage] | $ |
| Evaluation runs | _____ runs × $_____ = | $ |
| **Total Monthly (Conservative)** | | **$** |

#### Expected Scenario

| Component | Calculation | Monthly Cost |
|:----------|:------------|:-------------|
| Query costs | _____ queries × $_____ = | $ |
| Vector DB | [Tier/usage] | $ |
| Hosting | [Tier/usage] | $ |
| Evaluation runs | _____ runs × $_____ = | $ |
| **Total Monthly (Expected)** | | **$** |

#### High Growth Scenario

| Component | Calculation | Monthly Cost |
|:----------|:------------|:-------------|
| Query costs | _____ queries × $_____ = | $ |
| Vector DB | [Tier/usage] | $ |
| Hosting | [Tier/usage] | $ |
| Evaluation runs | _____ runs × $_____ = | $ |
| **Total Monthly (High Growth)** | | **$** |

---

## 4. Maintenance Costs

### 4.1 Ongoing Maintenance

| Activity | Frequency | Hours/Month | Rate | Monthly Cost |
|:---------|:----------|:------------|:-----|:-------------|
| Monitoring & alerting | Ongoing | | $ | $ |
| Bug fixes | As needed | | $ | $ |
| Performance tuning | Monthly | | $ | $ |
| Content updates | Weekly | | $ | $ |
| Reindexing | Monthly | | $ | $ |
| **Total Maintenance** | | | | **$** |

### 4.2 Content Update Costs

| Activity | Frequency | Cost per Update | Monthly Cost |
|:---------|:----------|:----------------|:-------------|
| Document processing | Weekly | $ | $ |
| Re-embedding | Weekly | $ | $ |
| Evaluation runs | Weekly | $ | $ |
| **Total Update Costs** | | | **$** |

---

## 5. Total Cost of Ownership

### 5.1 Year 1 Costs

| Category | Cost |
|:---------|:-----|
| Build costs (one-time) | $ |
| Monthly operating (×12) | $ |
| Monthly maintenance (×12) | $ |
| **Year 1 Total** | **$** |

### 5.2 Steady-State Monthly

| Category | Cost |
|:---------|:-----|
| Operating costs | $ |
| Maintenance costs | $ |
| **Steady-State Monthly** | **$** |

### 5.3 Cost Projection (3 Years)

| Year | Build | Operating | Maintenance | Total |
|:-----|:------|:----------|:------------|:------|
| Year 1 | $ | $ | $ | $ |
| Year 2 | $0 | $ | $ | $ |
| Year 3 | $0 | $ | $ | $ |
| **3-Year Total** | | | | **$** |

---

## 6. ROI Analysis (If Applicable)

### 6.1 Value Calculation

| Metric | Value | Notes |
|:-------|:------|:------|
| Cost per support ticket | $ | [Source] |
| Expected ticket deflection rate | % | [Estimate basis] |
| Value per successful query | $ | |
| Expected success rate | % | |
| Monthly queries | | |
| **Monthly value generated** | **$** | |

### 6.2 ROI Calculation

```
Annual Value:     $_____ (queries × value × success_rate × 12)
Annual Cost:      $_____ (Year 1 total)
Net Value:        $_____
ROI:              _____% ((value - cost) / cost × 100)
```

### 6.3 Break-Even Analysis

```
Break-even queries = Build Cost / (Value per query - Cost per query)
                   = $_____ / ($_____ - $_____) 
                   = _____ queries

At expected volume: _____ months to break even
```

---

## 7. Cost Optimization Opportunities

### 7.1 Identified Optimizations

| Optimization | Potential Savings | Trade-off | Priority |
|:-------------|:------------------|:----------|:---------|
| [Optimization 1] | $ / XX% | [Trade-off] | High/Med/Low |
| [Optimization 2] | $ / XX% | [Trade-off] | High/Med/Low |
| [Optimization 3] | $ / XX% | [Trade-off] | High/Med/Low |

### 7.2 Optimization Roadmap

| Phase | Optimization | Expected Savings | Timeline |
|:------|:-------------|:-----------------|:---------|
| Near-term | | $ | |
| Medium-term | | $ | |
| Long-term | | $ | |

---

## 8. Risks and Assumptions

### 8.1 Key Assumptions

| Assumption | Impact if Wrong |
|:-----------|:----------------|
| [Assumption 1] | [Impact] |
| [Assumption 2] | [Impact] |
| [Assumption 3] | [Impact] |

### 8.2 Cost Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| API price increase | Medium | +XX% cost | Multi-provider strategy |
| Volume spike | Medium | +XX% cost | Rate limiting, caching |
| Quality issues requiring fixes | High | +$X,XXX | Evaluation pipeline |

---

## 9. Appendix

### 9.1 Pricing References

| Service | Pricing | Source | Date Verified |
|:--------|:--------|:-------|:--------------|
| [Service 1] | $X.XX per Y | [URL] | YYYY-MM-DD |
| [Service 2] | $X.XX per Y | [URL] | YYYY-MM-DD |

### 9.2 Calculation Details

[Any detailed calculations or formulas used]

---

*Last updated: YYYY-MM-DD*
