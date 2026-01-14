"""
RAG Evaluation Pipeline - Reference Implementation

This is ONE valid approach, not THE approach. 
The learning is in deciding, not in copying.

Use this to understand the concepts, then build your own.

Requirements:
    pip install openai chromadb pyyaml numpy
"""

import os
import json
import yaml
import time
from dataclasses import dataclass
from typing import Optional
import numpy as np

# Optional: uncomment if you have these installed
# import openai
# import chromadb


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class RetrievalResult:
    """Result from retrieval step."""
    chunk_ids: list[str]
    chunks: list[str]
    scores: list[float]
    latency_ms: float


@dataclass
class GenerationResult:
    """Result from generation step."""
    answer: str
    input_tokens: int
    output_tokens: int
    latency_ms: float


@dataclass 
class RAGResult:
    """Combined RAG result."""
    query: str
    retrieval: RetrievalResult
    generation: GenerationResult
    total_latency_ms: float


@dataclass
class RetrievalMetrics:
    """Metrics for retrieval evaluation."""
    precision: float
    recall: float
    mrr: float
    retrieved_count: int
    relevant_retrieved: int


@dataclass
class GenerationMetrics:
    """Metrics for generation evaluation."""
    relevance: float
    accuracy: float
    completeness: float
    groundedness: float
    helpfulness: float
    overall: float
    reasoning: str


# =============================================================================
# RETRIEVAL EVALUATION
# =============================================================================

def evaluate_retrieval(
    retrieved_ids: list[str],
    relevant_ids: list[str]
) -> RetrievalMetrics:
    """
    Evaluate retrieval quality.
    
    Args:
        retrieved_ids: List of chunk IDs returned by retrieval
        relevant_ids: List of chunk IDs that are actually relevant (ground truth)
    
    Returns:
        RetrievalMetrics with precision, recall, mrr
    """
    if not retrieved_ids:
        return RetrievalMetrics(
            precision=0.0,
            recall=0.0,
            mrr=0.0,
            retrieved_count=0,
            relevant_retrieved=0
        )
    
    retrieved_set = set(retrieved_ids)
    relevant_set = set(relevant_ids)
    
    # Precision: what fraction of retrieved are relevant?
    relevant_retrieved = len(retrieved_set & relevant_set)
    precision = relevant_retrieved / len(retrieved_ids)
    
    # Recall: what fraction of relevant did we retrieve?
    recall = relevant_retrieved / len(relevant_ids) if relevant_ids else 0.0
    
    # MRR: reciprocal rank of first relevant result
    mrr = 0.0
    for i, chunk_id in enumerate(retrieved_ids):
        if chunk_id in relevant_set:
            mrr = 1.0 / (i + 1)
            break
    
    return RetrievalMetrics(
        precision=precision,
        recall=recall,
        mrr=mrr,
        retrieved_count=len(retrieved_ids),
        relevant_retrieved=relevant_retrieved
    )


# =============================================================================
# GENERATION EVALUATION (LLM-as-Judge)
# =============================================================================

EVAL_PROMPT = """You are evaluating a RAG system's response quality.

## User Query
{query}

## Retrieved Context (what the system had access to)
{context}

## System Response
{response}

## Reference Answer (ideal response)
{reference}

Rate the response on these criteria using a 1-5 scale:

1. **Relevance** (1-5): Does the response address the user's query?
   - 1 = Completely irrelevant or off-topic
   - 3 = Partially addresses the query
   - 5 = Directly and fully addresses the query

2. **Accuracy** (1-5): Is the information correct based on the retrieved context?
   - 1 = Contains significant factual errors
   - 3 = Mostly accurate with minor errors
   - 5 = Completely accurate

3. **Completeness** (1-5): Does the response cover what the user needs?
   - 1 = Missing critical information
   - 3 = Covers main points but missing details
   - 5 = Comprehensive and complete

4. **Groundedness** (1-5): Is the response based on the retrieved context?
   - 1 = Mostly hallucinated (not in context)
   - 3 = Mix of grounded and ungrounded claims
   - 5 = Fully grounded in the provided context

5. **Helpfulness** (1-5): Would this response help the user?
   - 1 = Not helpful at all
   - 3 = Somewhat helpful
   - 5 = Very helpful

Respond ONLY with valid JSON in this exact format:
{{
    "relevance": <1-5>,
    "accuracy": <1-5>,
    "completeness": <1-5>,
    "groundedness": <1-5>,
    "helpfulness": <1-5>,
    "reasoning": "<brief explanation of your ratings>"
}}
"""


def evaluate_generation_mock(
    query: str,
    context: str,
    response: str,
    reference: str
) -> GenerationMetrics:
    """
    Mock generation evaluation (replace with real LLM call).
    
    In real implementation, this would call an LLM.
    """
    # This is a placeholder - replace with actual LLM evaluation
    return GenerationMetrics(
        relevance=4.0,
        accuracy=4.0,
        completeness=3.5,
        groundedness=4.5,
        helpfulness=4.0,
        overall=4.0,
        reasoning="Mock evaluation - replace with LLM-as-judge"
    )


def evaluate_generation(
    query: str,
    context: str,
    response: str,
    reference: str,
    evaluator_model: str = "gpt-4o-mini",
    weights: Optional[dict] = None
) -> GenerationMetrics:
    """
    Evaluate generation quality using LLM-as-judge.
    
    Args:
        query: The user's question
        context: Retrieved context provided to the system
        response: The system's generated response
        reference: The reference (ideal) answer
        evaluator_model: Model to use for evaluation
        weights: Weights for computing overall score
    
    Returns:
        GenerationMetrics with scores and reasoning
    """
    if weights is None:
        weights = {
            'relevance': 0.2,
            'accuracy': 0.3,
            'completeness': 0.2,
            'groundedness': 0.2,
            'helpfulness': 0.1
        }
    
    prompt = EVAL_PROMPT.format(
        query=query,
        context=context[:2000],  # Truncate for eval
        response=response,
        reference=reference
    )
    
    # TODO: Replace with actual LLM call
    # response = openai.chat.completions.create(
    #     model=evaluator_model,
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=0.0
    # )
    # result = json.loads(response.choices[0].message.content)
    
    # Using mock for now
    return evaluate_generation_mock(query, context, response, reference)


# =============================================================================
# GOLDEN DATASET HANDLING
# =============================================================================

def load_golden_dataset(path: str) -> list[dict]:
    """Load golden dataset from YAML file."""
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('examples', data)


def validate_golden_dataset(examples: list[dict]) -> dict:
    """
    Validate golden dataset structure and completeness.
    
    Returns dict with validation results and any issues found.
    """
    issues = []
    categories = {}
    
    required_fields = ['id', 'query', 'category']
    
    for i, example in enumerate(examples):
        # Check required fields
        for field in required_fields:
            if field not in example:
                issues.append(f"Example {i}: missing required field '{field}'")
        
        # Track categories
        cat = example.get('category', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1
    
    # Check category distribution
    required_categories = [
        'simple_factual', 'how_to', 'troubleshooting',
        'comparison', 'complex', 'out_of_scope', 'ambiguous'
    ]
    
    for cat in required_categories:
        if cat not in categories:
            issues.append(f"Missing category: {cat}")
        elif categories[cat] < 2:
            issues.append(f"Insufficient examples in category '{cat}': {categories[cat]}")
    
    return {
        'valid': len(issues) == 0,
        'example_count': len(examples),
        'categories': categories,
        'issues': issues
    }


# =============================================================================
# FULL EVALUATION PIPELINE
# =============================================================================

@dataclass
class EvalConfig:
    """Configuration for evaluation pipeline."""
    golden_dataset_path: str
    retrieval_top_k: int = 5
    retrieval_precision_target: float = 0.8
    retrieval_recall_target: float = 0.7
    generation_overall_target: float = 4.0
    latency_p95_target: float = 5.0
    evaluator_model: str = "gpt-4o-mini"


@dataclass
class EvalResults:
    """Results from evaluation run."""
    timestamp: str
    config: dict
    retrieval: dict
    generation: dict
    system: dict
    by_category: dict
    detailed: list[dict]


def run_evaluation(
    rag_system,  # Your RAG system with .retrieve() and .generate() methods
    config: EvalConfig
) -> EvalResults:
    """
    Run full evaluation pipeline.
    
    Args:
        rag_system: RAG system to evaluate
        config: Evaluation configuration
    
    Returns:
        EvalResults with all metrics
    """
    # Load golden dataset
    examples = load_golden_dataset(config.golden_dataset_path)
    
    # Validate dataset
    validation = validate_golden_dataset(examples)
    if not validation['valid']:
        print(f"Warning: Golden dataset has issues: {validation['issues']}")
    
    # Run evaluation
    results = []
    latencies = []
    
    for example in examples:
        start_time = time.time()
        
        # Run RAG pipeline
        rag_result = rag_system.query(example['query'], top_k=config.retrieval_top_k)
        
        total_latency = (time.time() - start_time) * 1000  # ms
        latencies.append(total_latency)
        
        # Evaluate retrieval
        relevant_ids = []
        for doc in example.get('relevant_documents', []):
            relevant_ids.extend(doc.get('chunk_ids', []))
        
        retrieval_metrics = evaluate_retrieval(
            retrieved_ids=rag_result.retrieval.chunk_ids,
            relevant_ids=relevant_ids
        )
        
        # Evaluate generation
        generation_metrics = evaluate_generation(
            query=example['query'],
            context="\n".join(rag_result.retrieval.chunks),
            response=rag_result.generation.answer,
            reference=example.get('reference_answer', ''),
            evaluator_model=config.evaluator_model
        )
        
        results.append({
            'id': example['id'],
            'category': example['category'],
            'retrieval': {
                'precision': retrieval_metrics.precision,
                'recall': retrieval_metrics.recall,
                'mrr': retrieval_metrics.mrr
            },
            'generation': {
                'relevance': generation_metrics.relevance,
                'accuracy': generation_metrics.accuracy,
                'completeness': generation_metrics.completeness,
                'groundedness': generation_metrics.groundedness,
                'helpfulness': generation_metrics.helpfulness,
                'overall': generation_metrics.overall
            },
            'latency_ms': total_latency
        })
    
    # Aggregate results
    return aggregate_results(results, latencies, config)


def aggregate_results(
    results: list[dict],
    latencies: list[float],
    config: EvalConfig
) -> EvalResults:
    """Aggregate individual results into summary statistics."""
    
    # Retrieval aggregation
    retrieval_agg = {
        'precision': {
            'mean': np.mean([r['retrieval']['precision'] for r in results]),
            'std': np.std([r['retrieval']['precision'] for r in results]),
            'min': np.min([r['retrieval']['precision'] for r in results]),
            'target': config.retrieval_precision_target,
            'meets_target': np.mean([r['retrieval']['precision'] for r in results]) >= config.retrieval_precision_target
        },
        'recall': {
            'mean': np.mean([r['retrieval']['recall'] for r in results]),
            'std': np.std([r['retrieval']['recall'] for r in results]),
            'target': config.retrieval_recall_target,
            'meets_target': np.mean([r['retrieval']['recall'] for r in results]) >= config.retrieval_recall_target
        },
        'mrr': {
            'mean': np.mean([r['retrieval']['mrr'] for r in results])
        }
    }
    
    # Generation aggregation
    generation_agg = {
        'overall': {
            'mean': np.mean([r['generation']['overall'] for r in results]),
            'std': np.std([r['generation']['overall'] for r in results]),
            'target': config.generation_overall_target,
            'meets_target': np.mean([r['generation']['overall'] for r in results]) >= config.generation_overall_target
        },
        'by_criterion': {
            'relevance': np.mean([r['generation']['relevance'] for r in results]),
            'accuracy': np.mean([r['generation']['accuracy'] for r in results]),
            'completeness': np.mean([r['generation']['completeness'] for r in results]),
            'groundedness': np.mean([r['generation']['groundedness'] for r in results]),
            'helpfulness': np.mean([r['generation']['helpfulness'] for r in results])
        }
    }
    
    # System metrics
    system_agg = {
        'latency': {
            'p50': np.percentile(latencies, 50),
            'p95': np.percentile(latencies, 95),
            'p99': np.percentile(latencies, 99),
            'target_p95': config.latency_p95_target * 1000,  # convert to ms
            'meets_target': np.percentile(latencies, 95) <= config.latency_p95_target * 1000
        }
    }
    
    # By category
    categories = {}
    for r in results:
        cat = r['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)
    
    by_category = {}
    for cat, cat_results in categories.items():
        by_category[cat] = {
            'count': len(cat_results),
            'retrieval_precision': np.mean([r['retrieval']['precision'] for r in cat_results]),
            'generation_overall': np.mean([r['generation']['overall'] for r in cat_results])
        }
    
    return EvalResults(
        timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
        config={
            'golden_dataset': config.golden_dataset_path,
            'retrieval_top_k': config.retrieval_top_k,
            'evaluator_model': config.evaluator_model
        },
        retrieval=retrieval_agg,
        generation=generation_agg,
        system=system_agg,
        by_category=by_category,
        detailed=results
    )


# =============================================================================
# DRIFT DETECTION
# =============================================================================

def detect_drift(
    current: EvalResults,
    baseline: EvalResults,
    threshold: float = 0.1
) -> dict:
    """
    Compare current results to baseline and detect significant drift.
    
    Args:
        current: Current evaluation results
        baseline: Baseline evaluation results
        threshold: Percentage change that triggers alert (e.g., 0.1 = 10%)
    
    Returns:
        Dict with drift detection results
    """
    alerts = []
    
    # Check retrieval metrics
    metrics_to_check = [
        ('retrieval', 'precision', 'mean'),
        ('retrieval', 'recall', 'mean'),
        ('generation', 'overall', 'mean')
    ]
    
    for category, metric, stat in metrics_to_check:
        current_val = current.__dict__[category][metric][stat]
        baseline_val = baseline.__dict__[category][metric][stat]
        
        if baseline_val > 0:
            change = (current_val - baseline_val) / baseline_val
            
            if change < -threshold:  # Degradation
                alerts.append({
                    'metric': f'{category}.{metric}',
                    'baseline': baseline_val,
                    'current': current_val,
                    'change': change,
                    'severity': 'critical' if change < -2*threshold else 'warning'
                })
    
    # Check latency (increase is bad)
    current_latency = current.system['latency']['p95']
    baseline_latency = baseline.system['latency']['p95']
    
    if baseline_latency > 0:
        latency_change = (current_latency - baseline_latency) / baseline_latency
        
        if latency_change > threshold:  # Increase is bad for latency
            alerts.append({
                'metric': 'system.latency.p95',
                'baseline': baseline_latency,
                'current': current_latency,
                'change': latency_change,
                'severity': 'critical' if latency_change > 2*threshold else 'warning'
            })
    
    return {
        'drift_detected': len(alerts) > 0,
        'alert_count': len(alerts),
        'alerts': alerts
    }


# =============================================================================
# REPORTING
# =============================================================================

def generate_report(results: EvalResults, format: str = 'markdown') -> str:
    """Generate evaluation report."""
    
    if format == 'markdown':
        return _generate_markdown_report(results)
    elif format == 'json':
        return json.dumps(results.__dict__, indent=2, default=str)
    else:
        raise ValueError(f"Unknown format: {format}")


def _generate_markdown_report(results: EvalResults) -> str:
    """Generate markdown evaluation report."""
    
    report = f"""# RAG Evaluation Report

**Timestamp:** {results.timestamp}

## Summary

### Retrieval Metrics

| Metric | Value | Target | Status |
|:-------|:------|:-------|:-------|
| Precision | {results.retrieval['precision']['mean']:.3f} | {results.retrieval['precision']['target']:.2f} | {'✅' if results.retrieval['precision']['meets_target'] else '❌'} |
| Recall | {results.retrieval['recall']['mean']:.3f} | {results.retrieval['recall']['target']:.2f} | {'✅' if results.retrieval['recall']['meets_target'] else '❌'} |
| MRR | {results.retrieval['mrr']['mean']:.3f} | - | - |

### Generation Metrics

| Metric | Value | Target | Status |
|:-------|:------|:-------|:-------|
| Overall | {results.generation['overall']['mean']:.2f} | {results.generation['overall']['target']:.1f} | {'✅' if results.generation['overall']['meets_target'] else '❌'} |
| Relevance | {results.generation['by_criterion']['relevance']:.2f} | - | - |
| Accuracy | {results.generation['by_criterion']['accuracy']:.2f} | - | - |
| Completeness | {results.generation['by_criterion']['completeness']:.2f} | - | - |
| Groundedness | {results.generation['by_criterion']['groundedness']:.2f} | - | - |
| Helpfulness | {results.generation['by_criterion']['helpfulness']:.2f} | - | - |

### System Metrics

| Metric | Value | Target | Status |
|:-------|:------|:-------|:-------|
| Latency P50 | {results.system['latency']['p50']:.0f}ms | - | - |
| Latency P95 | {results.system['latency']['p95']:.0f}ms | {results.system['latency']['target_p95']:.0f}ms | {'✅' if results.system['latency']['meets_target'] else '❌'} |
| Latency P99 | {results.system['latency']['p99']:.0f}ms | - | - |

## Results by Category

| Category | Count | Retrieval Precision | Generation Overall |
|:---------|:------|:-------------------|:-------------------|
"""
    
    for cat, stats in results.by_category.items():
        report += f"| {cat} | {stats['count']} | {stats['retrieval_precision']:.3f} | {stats['generation_overall']:.2f} |\n"
    
    report += f"""

## Configuration

```json
{json.dumps(results.config, indent=2)}
```

---
*Report generated automatically by RAG Evaluation Pipeline*
"""
    
    return report


# =============================================================================
# MAIN (Example Usage)
# =============================================================================

if __name__ == "__main__":
    print("RAG Evaluation Pipeline - Reference Implementation")
    print("=" * 50)
    print()
    print("This is a reference implementation to understand the concepts.")
    print("To use it:")
    print()
    print("1. Implement your RAG system with .query() method")
    print("2. Create a golden dataset following the template")
    print("3. Configure evaluation settings")
    print("4. Run evaluation")
    print()
    print("Example:")
    print()
    print("    config = EvalConfig(")
    print("        golden_dataset_path='golden_dataset.yaml',")
    print("        retrieval_top_k=5,")
    print("        retrieval_precision_target=0.8")
    print("    )")
    print()
    print("    results = run_evaluation(my_rag_system, config)")
    print("    report = generate_report(results, format='markdown')")
    print("    print(report)")
