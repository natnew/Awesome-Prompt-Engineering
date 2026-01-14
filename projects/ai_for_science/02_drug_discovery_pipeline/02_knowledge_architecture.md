[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Problem Framing](01_problem_framing.md) | [Agent Design →](03_agent_design.md)

# Knowledge Architecture

Design how your system represents, retrieves, and reasons about scientific knowledge.

---

## The Knowledge Challenge

Drug discovery AI must navigate multiple knowledge types:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE LANDSCAPE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Structured Data          Semi-Structured         Unstructured      │
│  ┌─────────────┐         ┌─────────────┐        ┌─────────────┐    │
│  │ Databases   │         │ Tables in   │        │ Free text   │    │
│  │ - ChEMBL    │         │ papers      │        │ in papers   │    │
│  │ - UniProt   │         │             │        │             │    │
│  │ - PubChem   │         │ Patents     │        │ Reviews     │    │
│  │             │         │             │        │             │    │
│  │ Clinical    │         │ Clinical    │        │ Conference  │    │
│  │ trial DBs   │         │ trial docs  │        │ abstracts   │    │
│  └─────────────┘         └─────────────┘        └─────────────┘    │
│        │                       │                      │            │
│        └───────────────────────┼──────────────────────┘            │
│                                │                                    │
│                    ┌───────────▼───────────┐                       │
│                    │   Your System Must    │                       │
│                    │   Integrate All       │                       │
│                    └───────────────────────┘                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Knowledge Representation

### Entities and Relationships

Your system needs to represent key scientific entities:

| Entity Type | Examples | Key Attributes |
|:------------|:---------|:---------------|
| **Target** | EGFR, KRAS, PD-1 | Function, disease association, druggability |
| **Disease** | NSCLC, AML, Alzheimer's | Mechanism, unmet need, patient population |
| **Compound** | Imatinib, ABBV-CLS-484 | Structure, activity, selectivity, ADMET |
| **Mechanism** | Kinase inhibition, PROTAC | MoA, precedent, challenges |
| **Clinical Evidence** | Trial results, approvals | Efficacy, safety, population |

### Entity Schema Example

```yaml
Target:
  id: string  # UniProt ID, gene symbol
  name: string
  aliases: list[string]
  function: string  # Retrieved from sources
  disease_associations:
    - disease_id: string
      evidence_type: string  # genetic, clinical, preclinical
      evidence_strength: enum  # strong, moderate, weak
      sources: list[Citation]
  druggability:
    score: float
    assessment: string
    sources: list[Citation]
  known_ligands:
    - compound_id: string
      activity: string
      source: Citation
```

### Relationship Types

| Relationship | Example | Evidence Required |
|:-------------|:--------|:------------------|
| target-disease | EGFR → NSCLC | Genetic, clinical, or mechanistic |
| compound-target | Erlotinib → EGFR | Binding, functional, cellular |
| compound-effect | Erlotinib → EGFR inhibition | Preclinical or clinical |
| disease-mechanism | NSCLC → EGFR signalling | Mechanistic studies |

---

## Knowledge Sources

### Source Hierarchy

Not all sources are equal. Define your hierarchy:

| Tier | Source Type | Trust Level | Examples |
|:-----|:------------|:------------|:---------|
| 1 | Regulatory approvals | Highest | FDA labels, EMA assessments |
| 2 | Peer-reviewed clinical | High | Phase III results in journals |
| 3 | Peer-reviewed preclinical | High | Well-controlled studies |
| 4 | Preprints | Medium | bioRxiv, medRxiv |
| 5 | Conference abstracts | Medium | AACR, ASCO abstracts |
| 6 | Patents | Low-Medium | Claims may not be validated |
| 7 | Press releases | Low | Often promotional |

### Source Integration Strategy

```
Query: "What's known about Target X?"
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Source Retrieval                                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │  PubMed     │ │  ChEMBL     │ │  ClinTrials │ │  Patents  │ │
│  │  N papers   │ │  N compounds│ │  N trials   │ │  N patents│ │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └─────┬─────┘ │
└─────────┼───────────────┼───────────────┼──────────────┼────────┘
          │               │               │              │
          └───────────────┴───────────────┴──────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  Source Quality Assessment                                      │
│  - Relevance to query                                          │
│  - Source tier (1-7)                                           │
│  - Recency                                                     │
│  - Corroboration (multiple sources?)                           │
└─────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  Knowledge Integration                                          │
│  - Entity extraction                                           │
│  - Relationship mapping                                        │
│  - Conflict detection                                          │
│  - Confidence assignment                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Retrieval Architecture

### Multi-Index Retrieval

Different knowledge types need different retrieval:

| Knowledge Type | Index Type | Retrieval Method |
|:---------------|:-----------|:-----------------|
| Scientific papers | Vector + keyword | Hybrid search |
| Structured databases | Direct query | API/SQL |
| Chemical structures | Molecular fingerprints | Similarity search |
| Clinical trials | Structured query | API filters |

### Query Decomposition

Complex research questions need decomposed queries:

```
User query: "What's known about KRAS inhibitors for pancreatic cancer?"
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  Query Decomposition                                            │
│                                                                 │
│  Sub-query 1: KRAS biology + pancreatic cancer                 │
│  Sub-query 2: KRAS inhibitor compound landscape                │
│  Sub-query 3: KRAS inhibitor clinical trials                   │
│  Sub-query 4: KRAS inhibitor safety/challenges                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  Parallel Retrieval                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │ Sub-query 1 │ │ Sub-query 2 │ │ Sub-query 3 │ │Sub-query 4│ │
│  │  Results    │ │   Results   │ │   Results   │ │  Results  │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └───────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  Result Synthesis                                               │
│  - Merge and deduplicate                                       │
│  - Assess coverage                                             │
│  - Identify gaps                                               │
└─────────────────────────────────────────────────────────────────┘
```

### Retrieval Quality Signals

How do you know retrieval is working?

| Signal | What It Indicates | How to Measure |
|:-------|:------------------|:---------------|
| Precision@K | Retrieved docs are relevant | Human evaluation |
| Recall | Important docs not missed | Known document sets |
| Diversity | Different perspectives covered | Topic clustering |
| Recency distribution | Appropriate temporal coverage | Date analysis |

---

## Knowledge Synthesis

### Synthesis Challenges

| Challenge | Problem | Mitigation |
|:----------|:--------|:-----------|
| Contradictory findings | Papers disagree | Surface conflicts explicitly |
| Evolving knowledge | New work supersedes old | Recency weighting + context |
| Context dependence | Finding varies by conditions | Preserve context in synthesis |
| Partial information | No single source has full picture | Multi-source integration |

### Synthesis Architecture

```
Retrieved Documents
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Extraction Layer                                               │
│  - Key findings                                                │
│  - Methods/conditions                                          │
│  - Limitations stated                                          │
│  - Author conclusions                                          │
└─────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Alignment Layer                                                │
│  - Map to common entities                                      │
│  - Normalise terminology                                       │
│  - Identify same/different claims                              │
└─────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Integration Layer                                              │
│  - Aggregate consistent findings                               │
│  - Flag inconsistencies                                        │
│  - Assign confidence levels                                    │
│  - Track provenance                                            │
└─────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│  Output Layer                                                   │
│  - Structured synthesis                                        │
│  - Inline citations                                            │
│  - Confidence indicators                                       │
│  - Conflict notes                                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Confidence Propagation

### Confidence Model

Every piece of knowledge should have associated confidence:

```python
@dataclass
class ConfidenceScore:
    value: float  # 0-1
    source_quality: float  # Based on source tier
    corroboration: float  # Multiple sources agree
    recency: float  # How recent
    directness: float  # Direct claim vs. inference
    
    def combine(self) -> float:
        """Combine factors into overall confidence."""
        weights = {
            'source_quality': 0.3,
            'corroboration': 0.3,
            'recency': 0.2,
            'directness': 0.2,
        }
        return sum(
            getattr(self, k) * v 
            for k, v in weights.items()
        )
```

### Confidence Through Inference

When reasoning builds on retrieved knowledge:

```
Retrieved fact: "Compound X inhibits Target Y (IC50 = 10nM)"
Confidence: 0.9 (peer-reviewed, well-controlled study)
        │
        ▼
Inference: "Compound X may be effective against Disease Z"
Confidence: 0.6 (inference reduces confidence)
        │
        ▼
Further inference: "Compound X class may be worth exploring"
Confidence: 0.4 (further inference further reduces)
```

---

## Your Task

### Exercise 1: Entity Schema Design

Design complete schemas for:
1. Target (drug target)
2. Compound (small molecule)
3. Disease
4. Clinical Evidence

Include:
- Required attributes
- Optional attributes
- Relationship fields
- Provenance fields

### Exercise 2: Source Strategy

Define your source strategy:
1. Which sources will you integrate?
2. How will you assess source quality?
3. How will you handle conflicts between sources?
4. How will you weight recency vs. corroboration?

### Exercise 3: Retrieval Pipeline

Design your retrieval pipeline:
1. How will you decompose complex queries?
2. What retrieval methods for each source type?
3. How will you merge results?
4. How will you assess retrieval quality?

### Exercise 4: Confidence Model

Design your confidence propagation:
1. What factors contribute to confidence?
2. How do you combine them?
3. How does confidence degrade through inference?
4. How do you communicate confidence to users?

---

## Deliverables

| Deliverable | Description |
|:------------|:------------|
| **Entity schemas** | Complete definitions for key entities |
| **Source strategy** | Which sources, how weighted, how integrated |
| **Retrieval design** | Query decomposition, retrieval methods, merging |
| **Confidence model** | How confidence is assigned and propagated |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Problem Framing](01_problem_framing.md) | [Project Overview](README.md) | [Agent Design →](03_agent_design.md) |
