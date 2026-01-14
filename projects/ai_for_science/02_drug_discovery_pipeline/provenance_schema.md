# Provenance Schema

## Overview

This document defines the data model for tracking provenance in the drug discovery pipeline.

---

## Core Entities

### Citation

A reference to a source document.

```python
@dataclass
class Citation:
    """Reference to a source document."""
    
    # Identity
    citation_id: str           # Unique identifier
    citation_type: str         # pmid, doi, url, database, patent
    external_id: str           # External identifier (e.g., PMID number)
    
    # Metadata
    title: str
    authors: list[str]
    year: int
    journal: Optional[str]
    
    # Quality
    source_tier: int           # 1-7 (1=highest quality)
    peer_reviewed: bool
    
    # Access
    access_url: str
    full_text_available: bool
    
    # Tracking
    retrieved_date: date
    retrieval_method: str      # How we found this
```

**Source Tiers:**

| Tier | Source Type | Examples |
|:-----|:------------|:---------|
| 1 | Regulatory documents | FDA labels, EMA assessments |
| 2 | Peer-reviewed clinical | Phase III results in major journals |
| 3 | Peer-reviewed preclinical | Well-controlled studies |
| 4 | Preprints | bioRxiv, medRxiv |
| 5 | Conference abstracts | AACR, ASCO abstracts |
| 6 | Patents | USPTO, EPO |
| 7 | Other | Press releases, news |

---

### Claim

A statement that requires evidence.

```python
@dataclass
class Claim:
    """A statement requiring evidence."""
    
    # Identity
    claim_id: str              # Unique identifier
    statement: str             # The claim text
    
    # Classification
    claim_type: ClaimType      # fact, inference, speculation
    domain: str                # biology, chemistry, clinical
    
    # Evidence
    sources: list[Citation]
    source_quotes: list[SourceQuote]
    
    # Confidence
    confidence: float          # 0-1
    confidence_factors: ConfidenceFactors
    
    # Reasoning (for inferences)
    reasoning_chain: list[str]
    parent_claims: list[str]   # Claims this builds on
    
    # Conflicts
    conflicts: list[Conflict]
    
    # Tracking
    created_by: str            # Agent that created
    created_at: datetime
    validated: bool
    validation_result: Optional[ValidationResult]

class ClaimType(Enum):
    FACT = "fact"              # Direct from source
    INFERENCE = "inference"    # Reasoned from facts
    SPECULATION = "speculation" # Hypothesis
```

---

### SourceQuote

Direct quote from source supporting a claim.

```python
@dataclass
class SourceQuote:
    """Direct quote from a source."""
    
    citation: Citation
    quote_text: str            # The exact quote
    location: str              # Where in document
    context: str               # Surrounding context
    extracted_by: str          # Agent/method
    verified: bool             # Human verified?
```

---

### Conflict

When sources disagree.

```python
@dataclass
class Conflict:
    """Record of conflicting information."""
    
    conflict_id: str
    conflict_type: ConflictType
    
    # The disagreement
    claim_a: str               # First claim
    claim_b: str               # Conflicting claim
    sources_a: list[Citation]
    sources_b: list[Citation]
    
    # Analysis
    severity: str              # minor, moderate, major
    resolution_notes: str      # How to interpret
    resolution_status: str     # unresolved, resolved, acknowledged
    
    # Recommendation
    user_guidance: str         # What to tell user

class ConflictType(Enum):
    NUMERIC = "numeric"        # Different numbers
    DIRECTIONAL = "directional" # Opposite conclusions
    METHODOLOGICAL = "methodological"  # Different methods
    TEMPORAL = "temporal"      # Changed over time
```

---

### ConfidenceFactors

Components of confidence score.

```python
@dataclass
class ConfidenceFactors:
    """Factors contributing to confidence."""
    
    source_quality: float      # Average source tier
    corroboration: float       # Multiple sources agree
    recency: float             # How recent
    directness: float          # Direct claim vs inference
    conflict_penalty: float    # Reduced if conflicts exist
    
    def compute_confidence(self) -> float:
        """Combine factors into overall confidence."""
        weights = {
            'source_quality': 0.25,
            'corroboration': 0.25,
            'recency': 0.15,
            'directness': 0.25,
            'conflict_penalty': 0.10,
        }
        
        score = sum(
            getattr(self, k) * v 
            for k, v in weights.items()
        )
        
        return min(max(score, 0.0), 1.0)
```

---

### ValidationResult

Result of provenance validation.

```python
@dataclass
class ValidationResult:
    """Result of validating a claim's provenance."""
    
    claim_id: str
    validated_at: datetime
    
    # Results
    valid: bool
    issues: list[ValidationIssue]
    
    # Details
    citations_checked: int
    citations_valid: int
    quotes_verified: int
    quotes_failed: int

@dataclass
class ValidationIssue:
    """A specific validation problem."""
    
    issue_type: str           # citation_not_found, quote_mismatch, etc.
    severity: str             # warning, error, critical
    description: str
    citation_id: Optional[str]
    remediation: str          # What to do about it
```

---

### ProvenanceRecord

Complete provenance for a research output.

```python
@dataclass
class ProvenanceRecord:
    """Complete provenance for a research query."""
    
    # Query
    record_id: str
    query: str
    query_timestamp: datetime
    
    # Content
    claims: list[Claim]
    conflicts: list[Conflict]
    
    # Sources
    sources_consulted: list[SourceAccess]
    total_sources: int
    sources_used: int
    
    # Processing
    agents_involved: list[str]
    processing_time: float
    
    # Quality
    validation_summary: ValidationSummary
    confidence_summary: ConfidenceSummary

@dataclass
class SourceAccess:
    """Record of accessing a source."""
    
    source_type: str          # pubmed, chembl, etc.
    query_used: str
    results_returned: int
    results_used: int
    access_time: datetime
```

---

## Relationships

### Claim Graph

```
ProvenanceRecord
    │
    ├── claims: [Claim]
    │       │
    │       ├── sources: [Citation]
    │       │       │
    │       │       └── source_quotes: [SourceQuote]
    │       │
    │       ├── parent_claims: [Claim]  (for inferences)
    │       │
    │       └── conflicts: [Conflict]
    │               │
    │               └── related_claims: [Claim]
    │
    └── sources_consulted: [SourceAccess]
```

### Inference Chain

```
Claim (fact, confidence: 0.95)
    │
    └── supports
            │
            ▼
        Claim (inference, confidence: 0.76)
            │
            └── supports
                    │
                    ▼
                Claim (speculation, confidence: 0.51)
```

---

## Confidence Propagation Rules

### Base Confidence by Source Tier

| Source Tier | Base Confidence |
|:------------|:----------------|
| Tier 1 | 0.95 |
| Tier 2 | 0.90 |
| Tier 3 | 0.85 |
| Tier 4 | 0.75 |
| Tier 5 | 0.70 |
| Tier 6 | 0.65 |
| Tier 7 | 0.50 |

### Corroboration Boost

| Number of Sources | Multiplier |
|:------------------|:-----------|
| 1 | 1.0 |
| 2 | 1.05 |
| 3+ | 1.10 |
| 5+ | 1.15 |

### Inference Penalty

| Inference Depth | Multiplier |
|:----------------|:-----------|
| Direct fact | 1.0 |
| 1-step inference | 0.85 |
| 2-step inference | 0.70 |
| 3+ step inference | 0.55 |

### Conflict Penalty

| Conflict Severity | Penalty |
|:------------------|:--------|
| Minor | -0.05 |
| Moderate | -0.15 |
| Major | -0.30 |

---

## Validation Rules

### Citation Validation

| Rule | Check | Action on Failure |
|:-----|:------|:------------------|
| Existence | Citation ID exists in source | Remove claim, log error |
| Accessibility | Source can be accessed | Flag as unverified |
| Relevance | Citation relevant to claim | Lower confidence |

### Quote Validation

| Rule | Check | Action on Failure |
|:-----|:------|:------------------|
| Presence | Quote exists in source | Remove quote, flag |
| Accuracy | Quote matches source text | Correct or remove |
| Context | Quote not taken out of context | Flag for review |

### Inference Validation

| Rule | Check | Action on Failure |
|:-----|:------|:------------------|
| Support | Parent claims support inference | Lower confidence |
| Logic | Inference logically follows | Flag for review |
| Completeness | No missing premises | Note gaps |

---

## Storage Schema

### Database Tables

```sql
-- Citations
CREATE TABLE citations (
    citation_id VARCHAR PRIMARY KEY,
    citation_type VARCHAR NOT NULL,
    external_id VARCHAR NOT NULL,
    title TEXT NOT NULL,
    authors JSONB,
    year INTEGER,
    journal VARCHAR,
    source_tier INTEGER,
    peer_reviewed BOOLEAN,
    access_url VARCHAR,
    retrieved_date DATE,
    UNIQUE(citation_type, external_id)
);

-- Claims
CREATE TABLE claims (
    claim_id VARCHAR PRIMARY KEY,
    statement TEXT NOT NULL,
    claim_type VARCHAR NOT NULL,
    domain VARCHAR,
    confidence FLOAT,
    confidence_factors JSONB,
    reasoning_chain JSONB,
    created_by VARCHAR,
    created_at TIMESTAMP,
    validated BOOLEAN DEFAULT FALSE
);

-- Claim-Citation relationships
CREATE TABLE claim_citations (
    claim_id VARCHAR REFERENCES claims(claim_id),
    citation_id VARCHAR REFERENCES citations(citation_id),
    PRIMARY KEY (claim_id, citation_id)
);

-- Conflicts
CREATE TABLE conflicts (
    conflict_id VARCHAR PRIMARY KEY,
    conflict_type VARCHAR,
    claim_a VARCHAR REFERENCES claims(claim_id),
    claim_b VARCHAR REFERENCES claims(claim_id),
    severity VARCHAR,
    resolution_notes TEXT,
    resolution_status VARCHAR
);

-- Provenance records
CREATE TABLE provenance_records (
    record_id VARCHAR PRIMARY KEY,
    query TEXT NOT NULL,
    query_timestamp TIMESTAMP,
    claims JSONB,
    sources_consulted JSONB,
    validation_summary JSONB,
    confidence_summary JSONB
);
```

---

## API Examples

### Create a Claim

```python
claim = Claim(
    claim_id=generate_id(),
    statement="KRAS G12C mutations occur in ~13% of NSCLC",
    claim_type=ClaimType.FACT,
    domain="clinical",
    sources=[citation_1, citation_2],
    source_quotes=[quote_1],
    confidence=0.9,
    confidence_factors=ConfidenceFactors(
        source_quality=0.9,
        corroboration=0.95,
        recency=0.85,
        directness=1.0,
        conflict_penalty=0.0
    ),
    reasoning_chain=[],
    parent_claims=[],
    conflicts=[],
    created_by="literature_agent",
    created_at=datetime.now(),
    validated=False
)
```

### Create an Inference

```python
inference = Claim(
    claim_id=generate_id(),
    statement="KRAS G12C inhibitors may be effective in NSCLC",
    claim_type=ClaimType.INFERENCE,
    domain="clinical",
    sources=parent_claim.sources,  # Inherit sources
    source_quotes=[],
    confidence=parent_claim.confidence * 0.85,  # Apply penalty
    confidence_factors=ConfidenceFactors(...),
    reasoning_chain=[
        parent_claim.claim_id,
        "If G12C drives disease and inhibitors block G12C, they may be effective"
    ],
    parent_claims=[parent_claim.claim_id],
    ...
)
```

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Data Architect | | |
| Domain Expert | | |
