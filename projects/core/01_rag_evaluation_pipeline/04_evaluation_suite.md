[← Back: Architecture](03_architecture.md) | [Next: Cost Model →](05_cost_model.md)

# Module 4: Evaluation Suite

Build the infrastructure to measure your system's performance.

---

## The Core Principle

**Evaluation is not a one-time activity. It's infrastructure.**

A good evaluation suite:
- Runs automatically
- Catches regressions before users do
- Enables confident iteration
- Provides evidence for decisions

This module teaches you to build that infrastructure.

---

## Evaluation Suite Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     EVALUATION PIPELINE                         │
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │   Golden    │    │    RAG      │    │  Evaluator  │         │
│  │   Dataset   │───▶│   System    │───▶│   (LLM +    │         │
│  │             │    │             │    │   Metrics)  │         │
│  └─────────────┘    └─────────────┘    └──────┬──────┘         │
│                                               │                 │
│                                               ▼                 │
│                                        ┌─────────────┐         │
│                                        │   Results   │         │
│                                        │  Dashboard  │         │
│                                        │             │         │
│                                        └─────────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Components

1. **Golden Dataset** — Your source of truth
2. **RAG System** — The thing you're evaluating
3. **Evaluator** — Computes metrics on outputs
4. **Results Dashboard** — Visualizes and tracks metrics over time

---

## Component 1: Golden Dataset

### Structure

Each example in your golden dataset should include:

```yaml
- id: "query_001"
  query: "How do I export my data to CSV?"
  category: "how-to"
  difficulty: "simple"
  
  # Ground truth for retrieval
  relevant_docs:
    - doc_id: "user_guide_ch5"
      chunk_ids: ["chunk_127", "chunk_128"]
      relevance: "high"  # high, medium, low
    - doc_id: "api_reference"
      chunk_ids: ["chunk_456"]
      relevance: "medium"
  
  # Ground truth for generation
  reference_answer: |
    To export your data to CSV:
    1. Go to Settings > Data > Export
    2. Select "CSV" as the format
    3. Choose the data range
    4. Click "Export"
    
    Your file will download automatically.
  
  # Evaluation criteria
  must_include:
    - "Settings"
    - "Export"
    - "CSV"
  must_not_include:
    - pricing information
    - competitor mentions
  
  # Metadata
  created_at: "2025-01-15"
  last_verified: "2025-01-15"
  notes: "Steps verified against v2.3"
```

### Building Your Dataset

**Start with 20 examples** across these categories:

| Category | Count | Purpose |
|:---------|:------|:--------|
| Simple factual | 4 | Baseline — should always work |
| How-to | 4 | Common user need |
| Troubleshooting | 4 | High value |
| Comparison | 2 | Requires synthesis |
| Complex/Multi-step | 2 | Stress test |
| Out of scope | 2 | Should gracefully fail |
| Ambiguous | 2 | Tests edge handling |

**Quality criteria for each example:**
- [ ] Query is realistic (from real users if possible)
- [ ] Relevant documents are correctly identified
- [ ] Reference answer is accurate and complete
- [ ] Must-include/must-not-include are specified
- [ ] Category and difficulty are labeled

---

## Component 2: Retrieval Evaluation

### Metrics Implementation

```python
def evaluate_retrieval(query: str, retrieved_chunks: list, ground_truth: dict) -> dict:
    """
    Evaluate retrieval quality for a single query.
    
    Args:
        query: The user's question
        retrieved_chunks: List of chunk IDs returned by retrieval
        ground_truth: Dict with 'relevant_chunks' list
    
    Returns:
        Dict with precision, recall, mrr metrics
    """
    relevant = set(ground_truth['relevant_chunks'])
    retrieved = set(retrieved_chunks)
    
    # Precision@k: What fraction of retrieved are relevant?
    precision = len(relevant & retrieved) / len(retrieved) if retrieved else 0
    
    # Recall@k: What fraction of relevant did we retrieve?
    recall = len(relevant & retrieved) / len(relevant) if relevant else 0
    
    # MRR: Reciprocal rank of first relevant
    mrr = 0
    for i, chunk_id in enumerate(retrieved_chunks):
        if chunk_id in relevant:
            mrr = 1 / (i + 1)
            break
    
    return {
        'precision': precision,
        'recall': recall,
        'mrr': mrr,
        'retrieved_count': len(retrieved),
        'relevant_retrieved': len(relevant & retrieved)
    }
```

### Running Retrieval Evaluation

```python
def run_retrieval_eval(rag_system, golden_dataset: list) -> dict:
    """
    Run retrieval evaluation across full golden dataset.
    """
    results = []
    
    for example in golden_dataset:
        # Get retrieval results (without generation)
        retrieved = rag_system.retrieve(example['query'], top_k=5)
        retrieved_ids = [chunk.id for chunk in retrieved]
        
        # Evaluate
        metrics = evaluate_retrieval(
            query=example['query'],
            retrieved_chunks=retrieved_ids,
            ground_truth={'relevant_chunks': example['relevant_chunk_ids']}
        )
        metrics['query_id'] = example['id']
        metrics['category'] = example['category']
        results.append(metrics)
    
    # Aggregate
    return {
        'mean_precision': mean([r['precision'] for r in results]),
        'mean_recall': mean([r['recall'] for r in results]),
        'mean_mrr': mean([r['mrr'] for r in results]),
        'by_category': group_by_category(results),
        'detailed': results
    }
```

---

## Component 3: Generation Evaluation

### LLM-as-Judge Setup

Create an evaluation prompt:

```python
EVAL_PROMPT = """You are evaluating a RAG system's response.

## Query
{query}

## Retrieved Context
{context}

## System Response
{response}

## Reference Answer
{reference}

Rate the response on these criteria (1-5 scale):

1. **Relevance**: Does the response address the query?
   1 = Completely irrelevant
   5 = Directly addresses the query

2. **Accuracy**: Is the information correct (based on the context)?
   1 = Contains significant errors
   5 = Factually accurate

3. **Completeness**: Does it cover what the user needs?
   1 = Missing critical information
   5 = Comprehensive

4. **Groundedness**: Is it based on the provided context (not hallucinated)?
   1 = Mostly hallucinated
   5 = Fully grounded in context

5. **Helpfulness**: Would this help a user?
   1 = Not helpful at all
   5 = Very helpful

Respond in JSON format:
{
  "relevance": <score>,
  "accuracy": <score>,
  "completeness": <score>,
  "groundedness": <score>,
  "helpfulness": <score>,
  "reasoning": "<brief explanation>"
}
"""
```

### Implementation

```python
def evaluate_generation(
    query: str,
    context: str,
    response: str,
    reference: str,
    evaluator_model: str = "gpt-4o-mini"
) -> dict:
    """
    Use LLM-as-judge to evaluate generation quality.
    """
    prompt = EVAL_PROMPT.format(
        query=query,
        context=context,
        response=response,
        reference=reference
    )
    
    result = call_llm(evaluator_model, prompt)
    scores = parse_json(result)
    
    # Compute weighted average
    weights = {
        'relevance': 0.2,
        'accuracy': 0.3,
        'completeness': 0.2,
        'groundedness': 0.2,
        'helpfulness': 0.1
    }
    
    scores['overall'] = sum(
        scores[k] * weights[k] 
        for k in weights
    )
    
    return scores
```

### Calibrating LLM-as-Judge

**Critical step:** Validate that your LLM judge matches human judgment.

1. Rate 20 responses manually (you, as human)
2. Have LLM rate the same 20
3. Compare — correlation should be > 0.7
4. If not, adjust the prompt or criteria

```python
def calibrate_judge(human_ratings: list, llm_ratings: list) -> dict:
    """Check correlation between human and LLM ratings."""
    from scipy.stats import pearsonr
    
    correlation, p_value = pearsonr(human_ratings, llm_ratings)
    
    return {
        'correlation': correlation,
        'p_value': p_value,
        'calibrated': correlation > 0.7
    }
```

---

## Component 4: End-to-End Evaluation

### Full Pipeline

```python
def run_full_eval(rag_system, golden_dataset: list, config: dict) -> dict:
    """
    Run complete evaluation pipeline.
    """
    results = {
        'retrieval': [],
        'generation': [],
        'latency': [],
        'cost': []
    }
    
    for example in golden_dataset:
        start_time = time.time()
        
        # Run full RAG pipeline
        response = rag_system.query(example['query'])
        
        latency = time.time() - start_time
        
        # Evaluate retrieval
        retrieval_metrics = evaluate_retrieval(
            query=example['query'],
            retrieved_chunks=response.retrieved_chunk_ids,
            ground_truth={'relevant_chunks': example['relevant_chunk_ids']}
        )
        
        # Evaluate generation
        generation_metrics = evaluate_generation(
            query=example['query'],
            context=response.context,
            response=response.answer,
            reference=example['reference_answer']
        )
        
        # Track cost
        cost = calculate_cost(response.token_usage)
        
        results['retrieval'].append(retrieval_metrics)
        results['generation'].append(generation_metrics)
        results['latency'].append(latency)
        results['cost'].append(cost)
    
    return aggregate_results(results)
```

### Results Aggregation

```python
def aggregate_results(results: dict) -> dict:
    """Aggregate results into summary statistics."""
    return {
        'retrieval': {
            'precision': {
                'mean': mean([r['precision'] for r in results['retrieval']]),
                'std': std([r['precision'] for r in results['retrieval']]),
                'min': min([r['precision'] for r in results['retrieval']])
            },
            'recall': {
                'mean': mean([r['recall'] for r in results['retrieval']]),
                'std': std([r['recall'] for r in results['retrieval']]),
                'min': min([r['recall'] for r in results['retrieval']])
            },
            'mrr': {
                'mean': mean([r['mrr'] for r in results['retrieval']])
            }
        },
        'generation': {
            'overall': {
                'mean': mean([r['overall'] for r in results['generation']]),
                'std': std([r['overall'] for r in results['generation']])
            },
            'by_criterion': {
                'relevance': mean([r['relevance'] for r in results['generation']]),
                'accuracy': mean([r['accuracy'] for r in results['generation']]),
                'completeness': mean([r['completeness'] for r in results['generation']]),
                'groundedness': mean([r['groundedness'] for r in results['generation']]),
                'helpfulness': mean([r['helpfulness'] for r in results['generation']])
            }
        },
        'system': {
            'latency_p50': percentile(results['latency'], 50),
            'latency_p95': percentile(results['latency'], 95),
            'cost_total': sum(results['cost']),
            'cost_per_query': mean(results['cost'])
        }
    }
```

---

## Component 5: Continuous Monitoring

### Drift Detection

```python
def detect_drift(current_results: dict, baseline_results: dict, threshold: float = 0.1) -> dict:
    """
    Compare current results to baseline and flag significant degradation.
    """
    alerts = []
    
    metrics_to_check = [
        ('retrieval.precision.mean', 'Retrieval precision'),
        ('retrieval.recall.mean', 'Retrieval recall'),
        ('generation.overall.mean', 'Generation quality'),
        ('system.latency_p95', 'P95 latency')
    ]
    
    for metric_path, metric_name in metrics_to_check:
        current = get_nested(current_results, metric_path)
        baseline = get_nested(baseline_results, metric_path)
        
        # Check for degradation (latency increase is bad, others decrease is bad)
        if 'latency' in metric_path:
            degraded = current > baseline * (1 + threshold)
        else:
            degraded = current < baseline * (1 - threshold)
        
        if degraded:
            alerts.append({
                'metric': metric_name,
                'baseline': baseline,
                'current': current,
                'change': (current - baseline) / baseline
            })
    
    return {
        'drift_detected': len(alerts) > 0,
        'alerts': alerts
    }
```

### Scheduled Evaluation

Set up evaluation to run:
- On every deployment (CI/CD integration)
- Daily (catch drift)
- After content updates (docs change)

---

## Your Task: Build Your Evaluation Suite

### Step 1: Create Golden Dataset

Build 20 examples following the structure above. Save as `golden_dataset.yaml`.

### Step 2: Implement Retrieval Evaluation

Write code that:
- Takes your golden dataset
- Runs queries through retrieval
- Computes precision, recall, MRR

### Step 3: Implement Generation Evaluation

Write code that:
- Takes retrieval output + generation
- Uses LLM-as-judge with your criteria
- Returns scores per criterion

### Step 4: Calibrate Your Judge

- Manually rate 10-20 responses
- Compare to LLM ratings
- Adjust until correlation > 0.7

### Step 5: Run Full Evaluation

- Execute end-to-end on golden dataset
- Record baseline metrics
- Set up alerting for drift

---

## Evaluation Configuration

Complete the template in `artifacts/eval_config.yaml`:

```yaml
evaluation:
  golden_dataset: "path/to/golden_dataset.yaml"
  
  retrieval:
    metrics: ["precision@5", "recall@5", "mrr"]
    targets:
      precision: 0.8
      recall: 0.7
      mrr: 0.6
  
  generation:
    evaluator_model: "gpt-4o-mini"
    criteria:
      - name: relevance
        weight: 0.2
      - name: accuracy
        weight: 0.3
      - name: completeness
        weight: 0.2
      - name: groundedness
        weight: 0.2
      - name: helpfulness
        weight: 0.1
    targets:
      overall: 4.0
  
  system:
    latency_p50_target: 2.0
    latency_p95_target: 5.0
    cost_per_query_target: 0.05

monitoring:
  drift_threshold: 0.1
  alert_channels: ["email", "slack"]
```

---

## Common Pitfalls

### 1. Golden Dataset Too Small

20 examples is a minimum. For production, aim for 100+.

### 2. Golden Dataset Not Representative

If your golden dataset doesn't include hard cases, you'll miss real problems.

### 3. Metrics Don't Match User Experience

Precision/recall may be high while users are unhappy. Validate with real feedback.

### 4. LLM Judge Not Calibrated

If you don't validate against human judgment, your automated scores are meaningless.

### 5. One-Time Evaluation

A system that worked yesterday may not work today. Continuous monitoring is essential.

---

## Checkpoint

### You Should Now Have

- [ ] Golden dataset with 20+ examples
- [ ] Retrieval evaluation code
- [ ] Generation evaluation code with LLM-as-judge
- [ ] Calibration results showing LLM matches human judgment
- [ ] Evaluation configuration file

### You Should Be Able To Answer

- What's your current retrieval precision?
- What's your current generation quality score?
- How long does evaluation take to run?
- What would trigger a drift alert?

---

[← Back: Architecture](03_architecture.md) | [Next: Cost Model →](05_cost_model.md)
