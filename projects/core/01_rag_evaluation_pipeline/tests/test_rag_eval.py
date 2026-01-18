import sys
import os
import pytest
from unittest.mock import MagicMock

# Add reference directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../reference')))

try:
    import rag_eval_pipeline as eval_pipe
except ImportError:
    # If running from different context, try alternative import
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from reference import rag_eval_pipeline as eval_pipe

def test_evaluate_retrieval_perfect():
    """Test perfect retrieval scores."""
    retrieved = ["doc1", "doc2", "doc3"]
    relevant = ["doc1", "doc2", "doc3"]
    metrics = eval_pipe.evaluate_retrieval(retrieved, relevant)
    
    assert metrics.precision == 1.0
    assert metrics.recall == 1.0
    assert metrics.mrr == 1.0
    assert metrics.retrieved_count == 3
    assert metrics.relevant_retrieved == 3

def test_evaluate_retrieval_partial():
    """Test partial match retrieval."""
    retrieved = ["doc1", "wrong1", "doc2"]
    relevant = ["doc1", "doc2", "doc3"]
    metrics = eval_pipe.evaluate_retrieval(retrieved, relevant)
    
    # Precision: 2/3 (doc1, doc2)
    assert metrics.precision == pytest.approx(0.666, 0.01)
    # Recall: 2/3 (doc1, doc2 found out of 3 relevant)
    assert metrics.recall == pytest.approx(0.666, 0.01)
    # MRR: First result is relevant, so 1/1 = 1.0
    assert metrics.mrr == 1.0

def test_evaluate_retrieval_ranking():
    """Test MRR calculation."""
    retrieved = ["wrong1", "doc1", "wrong2"]
    relevant = ["doc1"]
    metrics = eval_pipe.evaluate_retrieval(retrieved, relevant)
    
    # MRR: First relevant is at index 1 (0-based) -> rank 2 -> 1/2 = 0.5
    assert metrics.mrr == 0.5

def test_evaluate_retrieval_empty():
    """Test empty retrieval."""
    retrieved = []
    relevant = ["doc1"]
    metrics = eval_pipe.evaluate_retrieval(retrieved, relevant)
    
    assert metrics.precision == 0.0
    assert metrics.recall == 0.0
    assert metrics.mrr == 0.0

def test_validate_golden_dataset_structure():
    """Test dataset validation logic."""
    # Invalid example (missing fields)
    examples = [{"id": "1"}] 
    result = eval_pipe.validate_golden_dataset(examples)
    
    assert result['valid'] is False
    assert any("missing required field" in issue for issue in result['issues'])

def test_detect_drift_no_drift():
    """Test drift detection works when metrics are stable."""
    # Create mock Baseline results
    baseline = MagicMock()
    baseline.retrieval = {'precision': {'mean': 0.8}, 'recall': {'mean': 0.8}}
    baseline.generation = {'overall': {'mean': 4.0}}
    baseline.system = {'latency': {'p95': 100.0}}
    
    # Create mock Current results (same as baseline)
    current = MagicMock()
    current.retrieval = {'precision': {'mean': 0.8}, 'recall': {'mean': 0.8}}
    current.generation = {'overall': {'mean': 4.0}}
    current.system = {'latency': {'p95': 100.0}}
    
    drift = eval_pipe.detect_drift(current, baseline, threshold=0.1)
    assert drift['drift_detected'] is False

def test_detect_drift_degradation():
    """Test detection of metric degradation."""
    baseline = MagicMock()
    baseline.retrieval = {'precision': {'mean': 0.8}, 'recall': {'mean': 0.8}}
    baseline.generation = {'overall': {'mean': 4.0}}
    baseline.system = {'latency': {'p95': 100.0}}
    
    current = MagicMock()
    current.retrieval = {'precision': {'mean': 0.6}, 'recall': {'mean': 0.8}} # 25% drop
    current.generation = {'overall': {'mean': 4.0}}
    current.system = {'latency': {'p95': 100.0}}
    
    drift = eval_pipe.detect_drift(current, baseline, threshold=0.1)
    assert drift['drift_detected'] is True
    assert len(drift['alerts']) == 1
    assert drift['alerts'][0]['metric'] == 'retrieval.precision'

def test_detect_drift_latency():
    """Test detection of latency increase."""
    baseline = MagicMock()
    baseline.retrieval = {'precision': {'mean': 0.8}, 'recall': {'mean': 0.8}}
    baseline.generation = {'overall': {'mean': 4.0}}
    baseline.system = {'latency': {'p95': 100.0}}
    
    current = MagicMock()
    current.retrieval = {'precision': {'mean': 0.8}, 'recall': {'mean': 0.8}}
    current.generation = {'overall': {'mean': 4.0}}
    current.system = {'latency': {'p95': 120.0}} # 20% increase
    
    drift = eval_pipe.detect_drift(current, baseline, threshold=0.1)
    assert drift['drift_detected'] is True
    assert any('system.latency' in alert['metric'] for alert in drift['alerts'])
