[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Agent Design](03_agent_design.md) | [Evaluation Framework →](05_evaluation_framework.md)

# Provenance System

Design a system that tracks every claim to its source, enabling scientific accountability.

---

## Why Provenance Matters

In scientific AI, provenance isn't a nice-to-have — it's foundational.

| Without Provenance | With Provenance |
|:-------------------|:----------------|
| "KRAS is a validated target" | "KRAS is a validated target [FDA approval, PMID:123]" |
| Trust me | Verify yourself |
| Black box | Transparent reasoning |
| Unreproducible | Reproducible |

**The standard:** Any claim your system makes should be verifiable by a scientist following the citation trail.

---

## Provenance Requirements

### Core Requirements

| Requirement | Description | Priority |
|:------------|:------------|:---------|
| **Traceability** | Every claim links to source(s) | Critical |
| **Verifiability** | Citations are real and accessible | Critical |
| **Accuracy** | Claim correctly represents source | Critical |
| **Completeness** | All supporting sources included | High |
| **Recency** | Source dates are tracked | High |

### Scientific Standards

| Standard | Implementation |
|:---------|:---------------|
| **No hallucinated citations** | Validate every citation exists |
| **No misattribution** | Verify claim matches source content |
| **Distinguish fact from inference** | Mark reasoning steps explicitly |
| **Surface conflicts** | Show when sources disagree |

---

## Provenance Data Model

### Core Schema

```python
@dataclass
class Citation:
    """A reference to a source document."""
    citation_type: str  # pmid, doi, url, database
    citation_id: str    # e.g., "32955176" for PMID
    title: str
    authors: list[str]
    year: int
    source_tier: int    # 1-7 quality tier
    access_url: str
    retrieved_date: date
    
@dataclass
class Claim:
    """A statement that requires evidence."""
    claim_id: str
    statement: str
    claim_type: str     # fact, inference, speculation
    confidence: float
    sources: list[Citation]
    source_quotes: list[SourceQuote]  # Direct quotes supporting claim
    reasoning_chain: list[str]        # If inferred, what's the logic
    conflicts: list[Conflict]         # Known contradicting sources
    
@dataclass
class SourceQuote:
    """Direct quote from source supporting a claim."""
    citation: Citation
    quote_text: str
    location: str       # e.g., "Results, paragraph 3"
    
@dataclass
class Conflict:
    """When sources disagree."""
    conflicting_claims: list[str]
    sources: list[Citation]
    conflict_type: str  # numeric, directional, methodological
    resolution_notes: str
    
@dataclass  
class ProvenanceRecord:
    """Complete provenance for a research output."""
    query: str
    timestamp: datetime
    claims: list[Claim]
    sources_consulted: list[Citation]
    agents_involved: list[str]
    confidence_summary: dict
```

### Provenance Graph

Claims often build on other claims. Track this as a graph:

```
                    ┌─────────────────────────────┐
                    │  Final Synthesis Claim      │
                    │  "KRAS G12C is a validated  │
                    │   target with approved      │
                    │   inhibitors"               │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │  Claim: KRAS    │  │  Claim: G12C    │  │  Claim: Two     │
    │  G12C drives    │  │  inhibitors     │  │  drugs approved │
    │  NSCLC          │  │  show clinical  │  │  (sotorasib,    │
    │                 │  │  efficacy       │  │  adagrasib)     │
    │  [Literature]   │  │  [Clinical]     │  │  [Regulatory]   │
    └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
             │                    │                    │
             ▼                    ▼                    ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │  PMID:12345678  │  │  NCT03600883    │  │  FDA Approval   │
    │  PMID:23456789  │  │  NCT04303780    │  │  05/2021        │
    │  COSMIC DB      │  │  PMID:34567890  │  │  12/2022        │
    └─────────────────┘  └─────────────────┘  └─────────────────┘
```

---

## Provenance Pipeline

### Stage 1: Capture

Every agent must emit structured provenance:

```python
class ProvenanceCapture:
    """Capture provenance during agent execution."""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.claims = []
        self.sources_accessed = []
    
    def add_claim(
        self, 
        statement: str,
        sources: list[Citation],
        claim_type: str = "fact",
        confidence: float = None,
        quotes: list[SourceQuote] = None
    ):
        """Record a claim with its provenance."""
        claim = Claim(
            claim_id=generate_id(),
            statement=statement,
            claim_type=claim_type,
            confidence=confidence or self.estimate_confidence(sources),
            sources=sources,
            source_quotes=quotes or [],
            reasoning_chain=[],
            conflicts=[]
        )
        self.claims.append(claim)
        return claim
    
    def add_inference(
        self,
        statement: str,
        based_on: list[Claim],
        reasoning: str,
        confidence_modifier: float = 0.8
    ):
        """Record an inference built on other claims."""
        # Inferences inherit sources from parent claims
        inherited_sources = self.collect_sources(based_on)
        
        # Confidence degrades through inference
        base_confidence = min(c.confidence for c in based_on)
        inference_confidence = base_confidence * confidence_modifier
        
        claim = Claim(
            claim_id=generate_id(),
            statement=statement,
            claim_type="inference",
            confidence=inference_confidence,
            sources=inherited_sources,
            source_quotes=[],
            reasoning_chain=[c.claim_id for c in based_on] + [reasoning],
            conflicts=[]
        )
        self.claims.append(claim)
        return claim
```

### Stage 2: Validation

Before claims reach the user, validate provenance:

```python
class ProvenanceValidator:
    """Validate all provenance claims."""
    
    async def validate(self, claims: list[Claim]) -> ValidationReport:
        results = []
        
        for claim in claims:
            result = await self.validate_claim(claim)
            results.append(result)
        
        return ValidationReport(
            total_claims=len(claims),
            validated=sum(1 for r in results if r.valid),
            failed=sum(1 for r in results if not r.valid),
            details=results
        )
    
    async def validate_claim(self, claim: Claim) -> ClaimValidation:
        """Validate a single claim."""
        issues = []
        
        # Check 1: Do sources exist?
        for source in claim.sources:
            exists = await self.check_source_exists(source)
            if not exists:
                issues.append(f"Source not found: {source.citation_id}")
        
        # Check 2: Are quotes accurate?
        for quote in claim.source_quotes:
            matches = await self.verify_quote(quote)
            if not matches:
                issues.append(f"Quote not found in source: {quote.citation.citation_id}")
        
        # Check 3: Does claim follow from sources?
        if claim.claim_type == "inference":
            valid_inference = await self.validate_inference(claim)
            if not valid_inference:
                issues.append("Inference not supported by cited claims")
        
        return ClaimValidation(
            claim_id=claim.claim_id,
            valid=len(issues) == 0,
            issues=issues
        )
    
    async def check_source_exists(self, source: Citation) -> bool:
        """Verify citation exists in source database."""
        if source.citation_type == "pmid":
            return await self.pubmed_lookup(source.citation_id)
        elif source.citation_type == "doi":
            return await self.doi_lookup(source.citation_id)
        # ... other source types
```

### Stage 3: Conflict Detection

Identify when sources disagree:

```python
class ConflictDetector:
    """Detect conflicts between claims from different sources."""
    
    def detect_conflicts(self, claims: list[Claim]) -> list[Conflict]:
        conflicts = []
        
        # Group claims by topic
        topic_groups = self.group_by_topic(claims)
        
        for topic, topic_claims in topic_groups.items():
            # Check for numeric conflicts
            numeric = self.detect_numeric_conflicts(topic_claims)
            conflicts.extend(numeric)
            
            # Check for directional conflicts
            directional = self.detect_directional_conflicts(topic_claims)
            conflicts.extend(directional)
        
        return conflicts
    
    def detect_numeric_conflicts(
        self, 
        claims: list[Claim]
    ) -> list[Conflict]:
        """Detect when claims report different numbers for same thing."""
        # Extract numeric values and compare
        # Flag significant discrepancies
        pass
    
    def detect_directional_conflicts(
        self, 
        claims: list[Claim]
    ) -> list[Conflict]:
        """Detect when claims point in opposite directions."""
        # e.g., "X increases Y" vs "X decreases Y"
        pass
```

### Stage 4: Confidence Propagation

Track how confidence flows through reasoning:

```python
class ConfidencePropagator:
    """Propagate confidence through claim graph."""
    
    def propagate(self, claim_graph: dict) -> dict:
        """Update confidences based on provenance quality."""
        
        for claim_id, claim in claim_graph.items():
            # Source quality affects confidence
            source_quality = self.assess_source_quality(claim.sources)
            
            # Corroboration increases confidence
            corroboration = self.assess_corroboration(claim.sources)
            
            # Inference depth decreases confidence
            inference_penalty = self.inference_penalty(claim.reasoning_chain)
            
            # Conflicts decrease confidence
            conflict_penalty = self.conflict_penalty(claim.conflicts)
            
            # Update confidence
            claim.confidence = self.combine_factors(
                base_confidence=claim.confidence,
                source_quality=source_quality,
                corroboration=corroboration,
                inference_penalty=inference_penalty,
                conflict_penalty=conflict_penalty
            )
        
        return claim_graph
```

---

## Provenance Presentation

### Inline Citations

Every claim in output should have inline citation:

```markdown
KRAS G12C mutations occur in approximately 13% of non-small cell lung 
cancers [1,2] and have been successfully targeted with covalent inhibitors [3].

**References:**
1. Author et al. (2021). Title. Journal. PMID:12345678
2. Author et al. (2020). Title. Journal. PMID:23456789  
3. FDA Label. Sotorasib (LUMAKRAS). Approval date: 05/2021
```

### Confidence Indicators

Make confidence visible:

```markdown
**High confidence (multiple corroborating sources):**
KRAS G12C is a validated oncology target with two approved drugs.

**Moderate confidence (limited sources):**
Resistance mechanisms may include acquired KRAS mutations and pathway 
reactivation, though clinical data is still emerging.

**Low confidence (inference from limited data):**
Combination strategies targeting resistance pathways might improve 
outcomes, but this remains speculative pending clinical validation.
```

### Conflict Surfacing

When sources disagree, show it:

```markdown
**Note: Conflicting data on prevalence**

KRAS G12C mutation frequency in NSCLC varies by population:
- Western populations: 11-14% [1,2]
- Asian populations: 3-4% [3,4]

This discrepancy likely reflects genuine population differences rather 
than methodological issues.
```

---

## Provenance Audit

### Audit Trail Requirements

| Requirement | Purpose | Implementation |
|:------------|:--------|:---------------|
| Query logging | Reproducibility | Store original query |
| Source logging | Verification | Record all sources accessed |
| Reasoning logging | Transparency | Document inference steps |
| Timestamp logging | Currency | Track when data retrieved |

### Audit Report Format

```yaml
audit_report:
  query: "What's known about KRAS G12C as a target?"
  timestamp: "2024-01-15T10:30:00Z"
  
  sources_consulted:
    pubmed:
      query: "KRAS G12C inhibitor"
      results_returned: 347
      results_used: 23
    clinical_trials:
      query: "KRAS G12C"
      results_returned: 45
      results_used: 8
    chembl:
      query: "KRAS"
      compounds_returned: 234
      
  claims_generated: 47
  claims_validated: 47
  conflicts_detected: 2
  conflicts_resolved: 2
  
  confidence_distribution:
    high: 28
    moderate: 15
    low: 4
    
  agents_involved:
    - literature_agent
    - target_agent
    - chemistry_agent
    - provenance_agent
    - synthesis_agent
```

---

## Your Task

### Exercise 1: Schema Design

Design your complete provenance schema:
1. What entities do you need?
2. What relationships between entities?
3. How do you represent inference chains?
4. How do you represent conflicts?

### Exercise 2: Validation Rules

Define your validation rules:
1. What makes a citation valid?
2. What makes a quote verifiable?
3. What makes an inference sound?
4. How do you handle validation failures?

### Exercise 3: Confidence Model

Design your confidence propagation:
1. What factors affect confidence?
2. How do you combine factors?
3. How does inference affect confidence?
4. How do conflicts affect confidence?

### Exercise 4: Presentation Design

Design how provenance appears to users:
1. How do you show citations inline?
2. How do you indicate confidence?
3. How do you surface conflicts?
4. How do you enable verification?

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Provenance schema** | `artifacts/provenance_schema.md` |
| **Validation rules** | Documented validation logic |
| **Confidence model** | Propagation algorithm |
| **Presentation templates** | Output format examples |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Agent Design](03_agent_design.md) | [Project Overview](README.md) | [Evaluation Framework →](05_evaluation_framework.md) |
