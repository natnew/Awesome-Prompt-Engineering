[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Provenance System](04_provenance_system.md) | [Synthesis →](synthesis.md)

# Evaluation Framework

Design rigorous evaluation for scientific AI that meets the standards of scientific practice.

---

## The Evaluation Challenge

Scientific AI evaluation differs from typical AI evaluation:

| Typical AI Evaluation | Scientific AI Evaluation |
|:----------------------|:-------------------------|
| "Is the output good?" | "Is every claim verifiable?" |
| User satisfaction | Scientific accuracy |
| Task completion | Provenance integrity |
| Single metric | Multi-dimensional rigour |

Your system must be evaluated on dimensions that matter to scientists.

---

## Evaluation Dimensions

### Dimension 1: Citation Integrity

**Core question:** Are citations real, relevant, and accurate?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Citation existence | % of citations that exist | 100% |
| Citation relevance | % of citations relevant to claim | >95% |
| Citation accuracy | % of claims that match source | >95% |
| Citation completeness | % of claims with sufficient sources | >90% |

### Dimension 2: Factual Accuracy

**Core question:** Is the scientific content correct?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Factual correctness | % of facts that are true | >95% |
| No hallucinations | % of outputs with zero hallucinations | 100% |
| Correct interpretation | % of source interpretations correct | >95% |

### Dimension 3: Reasoning Quality

**Core question:** Are inferences sound?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Logical validity | % of inferences that follow | >90% |
| Appropriate confidence | Confidence matches evidence | ECE <0.1 |
| Inference transparency | Reasoning chain documented | 100% |

### Dimension 4: Coverage

**Core question:** Does the system find what matters?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Key paper recall | % of important papers found | >80% |
| Topic coverage | Major aspects addressed | >85% |
| Gap identification | Correctly identifies missing data | >80% |

### Dimension 5: Conflict Handling

**Core question:** Are disagreements surfaced?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Conflict detection | % of real conflicts found | >85% |
| Conflict transparency | % of conflicts shown to user | 100% |
| Resolution quality | Appropriate handling of conflicts | >80% |

---

## Evaluation Methods

### Method 1: Citation Validation

Automated validation of all citations:

```python
class CitationValidator:
    """Validate citation integrity automatically."""
    
    async def validate_all_citations(
        self, 
        report: ResearchReport
    ) -> CitationValidationResult:
        
        results = {
            "total_citations": 0,
            "valid_citations": 0,
            "invalid_citations": [],
            "relevance_scores": [],
        }
        
        for claim in report.claims:
            for citation in claim.sources:
                results["total_citations"] += 1
                
                # Check existence
                exists = await self.check_exists(citation)
                if not exists:
                    results["invalid_citations"].append({
                        "citation": citation,
                        "issue": "not_found"
                    })
                    continue
                
                # Check relevance
                relevance = await self.assess_relevance(claim, citation)
                results["relevance_scores"].append(relevance)
                
                if relevance > 0.5:
                    results["valid_citations"] += 1
                else:
                    results["invalid_citations"].append({
                        "citation": citation,
                        "issue": "low_relevance",
                        "score": relevance
                    })
        
        return CitationValidationResult(**results)
```

### Method 2: Expert Evaluation

Human expert assessment of scientific quality:

**Expert Evaluation Rubric:**

| Dimension | 5 (Excellent) | 3 (Acceptable) | 1 (Poor) |
|:----------|:--------------|:---------------|:---------|
| **Accuracy** | All facts correct, nuanced understanding | Minor errors, generally correct | Significant errors |
| **Coverage** | Comprehensive, no major gaps | Most important work included | Major gaps |
| **Interpretation** | Sophisticated, appropriate nuance | Correct but simplistic | Misinterpretation |
| **Synthesis** | Insightful integration | Adequate summary | Disjointed |
| **Uncertainty** | Perfectly calibrated | Generally appropriate | Over/under confident |

**Expert Evaluation Protocol:**

1. Present expert with research query
2. Show system output
3. Provide access to cited sources
4. Expert rates each dimension
5. Expert provides free-text feedback
6. Expert identifies specific errors

### Method 3: Reference Set Comparison

Compare system output to expert-created reference:

```python
class ReferenceSetEvaluator:
    """Compare system output to expert reference."""
    
    def __init__(self, reference_set: dict):
        """
        reference_set: {
            query_id: {
                "query": str,
                "expected_claims": list[str],
                "expected_citations": list[str],
                "expected_conflicts": list[str]
            }
        }
        """
        self.reference_set = reference_set
    
    def evaluate(self, query_id: str, system_output: ResearchReport) -> dict:
        reference = self.reference_set[query_id]
        
        # Claim recall: what expected claims were found?
        claim_recall = self.compute_claim_recall(
            expected=reference["expected_claims"],
            actual=[c.statement for c in system_output.claims]
        )
        
        # Citation recall: what key papers were cited?
        citation_recall = self.compute_citation_recall(
            expected=reference["expected_citations"],
            actual=self.extract_citation_ids(system_output)
        )
        
        # Conflict recall: were known conflicts identified?
        conflict_recall = self.compute_conflict_recall(
            expected=reference["expected_conflicts"],
            actual=system_output.conflicts
        )
        
        return {
            "claim_recall": claim_recall,
            "citation_recall": citation_recall,
            "conflict_recall": conflict_recall,
        }
```

### Method 4: Adversarial Testing

Test system robustness to challenging inputs:

| Test Category | Examples | Expected Behaviour |
|:--------------|:---------|:-------------------|
| Non-existent targets | "What's known about XYZABC123 target?" | Acknowledge no results |
| Contradictory requests | "Find papers proving X and papers disproving X" | Handle both fairly |
| Outdated topics | Query about retracted work | Note retractions |
| Edge of knowledge | Very recent or obscure topics | Appropriate uncertainty |

### Method 5: Calibration Assessment

Measure confidence calibration:

```python
def assess_calibration(
    predictions: list[dict]  # {confidence: float, correct: bool}
) -> CalibrationMetrics:
    """
    Assess how well stated confidence matches actual accuracy.
    """
    # Bin predictions by confidence
    bins = defaultdict(list)
    for pred in predictions:
        bin_idx = int(pred["confidence"] * 10)  # 0-10 bins
        bins[bin_idx].append(pred["correct"])
    
    # Calculate ECE
    ece = 0.0
    for bin_idx, outcomes in bins.items():
        if len(outcomes) > 0:
            bin_confidence = (bin_idx + 0.5) / 10
            bin_accuracy = sum(outcomes) / len(outcomes)
            bin_weight = len(outcomes) / len(predictions)
            ece += bin_weight * abs(bin_confidence - bin_accuracy)
    
    return CalibrationMetrics(
        ece=ece,
        bins={k: sum(v)/len(v) for k, v in bins.items()}
    )
```

---

## Test Case Design

### Test Case Categories

#### Category 1: Known-Answer Tests

Queries where correct answers are known:

```yaml
- id: KA_001
  query: "Is EGFR a validated target for NSCLC?"
  expected:
    answer: "Yes"
    key_evidence: ["FDA approvals", "Clinical trials"]
    key_citations: ["erlotinib approval", "osimertinib trials"]
  
- id: KA_002
  query: "What's the mechanism of imatinib?"
  expected:
    answer: "BCR-ABL kinase inhibition"
    key_evidence: ["Crystal structure", "Cellular assays"]
```

#### Category 2: Coverage Tests

Queries testing comprehensive retrieval:

```yaml
- id: COV_001
  query: "What are known resistance mechanisms to EGFR inhibitors?"
  expected_topics:
    - T790M mutation
    - C797S mutation
    - MET amplification
    - HER2 amplification
    - Histological transformation
  minimum_coverage: 4/5
```

#### Category 3: Conflict Tests

Queries where literature disagrees:

```yaml
- id: CONF_001
  query: "What's the role of autophagy in cancer?"
  known_conflicts:
    - "Pro-tumorigenic vs. tumor-suppressive roles"
    - "Context-dependent effects"
  expected_behaviour: "Surface both perspectives"
```

#### Category 4: Uncertainty Tests

Queries requiring appropriate uncertainty:

```yaml
- id: UNC_001
  query: "Will KRAS G12D inhibitors be successful?"
  expected:
    confidence_level: "low"
    uncertainty_expression: true
    caveats_mentioned: ["No clinical data yet", "Technical challenges"]
```

#### Category 5: Hallucination Tests

Queries designed to elicit hallucinations:

```yaml
- id: HAL_001
  query: "What clinical trials have tested XYZ-999 (fictional compound)?"
  expected:
    behaviour: "Report no results found"
    hallucination: false
  failure_modes:
    - Inventing trial numbers
    - Citing non-existent papers
```

---

## Evaluation Pipeline

### Continuous Evaluation Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        TEST SUITE                                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │Known-Answer │ │  Coverage   │ │  Conflict   │ │Hallucination│   │
│  │    Tests    │ │   Tests     │ │   Tests     │ │   Tests     │   │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘   │
└─────────┼───────────────┼───────────────┼───────────────┼───────────┘
          │               │               │               │
          └───────────────┴───────────────┴───────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     SYSTEM UNDER TEST                               │
│                  Drug Discovery Pipeline                            │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     AUTOMATED EVALUATION                            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │  Citation   │ │  Factual    │ │ Calibration │ │  Coverage   │   │
│  │ Validation  │ │  Checking   │ │ Assessment  │ │   Scoring   │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      EXPERT REVIEW                                  │
│               (Sampled for periodic deep evaluation)                │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      EVALUATION REPORT                              │
│  Citation Integrity: 98%    Factual Accuracy: 96%                  │
│  Coverage: 87%              Calibration ECE: 0.08                  │
│  Conflict Detection: 82%    Hallucination Rate: 0%                 │
└─────────────────────────────────────────────────────────────────────┘
```

### Evaluation Cadence

| Evaluation Type | Frequency | Purpose |
|:----------------|:----------|:--------|
| Citation validation | Every query | Catch hallucinations |
| Automated test suite | Daily | Regression detection |
| Reference set evaluation | Weekly | Coverage and accuracy |
| Expert evaluation | Monthly | Deep quality assessment |
| Adversarial testing | Quarterly | Robustness assessment |

---

## Evaluation Scorecard

### Summary Metrics

| Dimension | Weight | Metric | Target |
|:----------|:-------|:-------|:-------|
| Citation Integrity | 0.25 | Validity rate | 100% |
| Factual Accuracy | 0.25 | Expert rating | >4/5 |
| Coverage | 0.20 | Reference recall | >80% |
| Calibration | 0.15 | ECE | <0.1 |
| Conflict Handling | 0.15 | Detection rate | >85% |

### Failure Thresholds

| Metric | Warning | Critical |
|:-------|:--------|:---------|
| Invalid citations | Any | Any |
| Factual errors | >2% | >5% |
| Missed key papers | >30% | >50% |
| ECE | >0.15 | >0.25 |
| Hallucinations | Any | Any |

---

## Your Task

### Exercise 1: Test Suite Development

Create a test suite with:
- 10 known-answer tests
- 5 coverage tests
- 5 conflict tests
- 5 hallucination tests

For each test, define:
- Query
- Expected outputs
- Evaluation criteria
- Pass/fail thresholds

### Exercise 2: Expert Evaluation Protocol

Design your expert evaluation:
- Who are evaluators? (qualifications)
- What do they evaluate?
- How do you ensure consistency?
- How do you handle disagreements?

### Exercise 3: Calibration Analysis

Design calibration assessment:
- How do you extract confidence scores?
- How do you determine "ground truth"?
- What's your binning strategy?
- How do you visualise results?

### Exercise 4: Continuous Monitoring

Design ongoing evaluation:
- What metrics do you track?
- What triggers alerts?
- How do you catch regressions?
- How do you report to stakeholders?

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Test suite** | Test cases for all categories |
| **Evaluation protocol** | `artifacts/evaluation_protocol.md` |
| **Expert rubric** | Rating criteria and process |
| **Monitoring plan** | Continuous evaluation design |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Provenance System](04_provenance_system.md) | [Project Overview](README.md) | [Synthesis →](synthesis.md) |
