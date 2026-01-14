[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Knowledge Architecture](02_knowledge_architecture.md) | [Provenance System →](04_provenance_system.md)

# Agent Design

Design a multi-agent system where specialised agents collaborate on drug discovery research tasks.

---

## Why Multi-Agent for Drug Discovery?

Drug discovery reasoning spans multiple domains that require different expertise:

| Domain | Knowledge Type | Reasoning Style |
|:-------|:---------------|:----------------|
| Biology | Targets, pathways, disease mechanisms | Mechanistic, causal |
| Chemistry | Structures, properties, SAR | Structural, quantitative |
| Pharmacology | ADMET, PK/PD | Predictive, empirical |
| Clinical | Trial results, safety signals | Statistical, evidence-based |

A single agent struggles to maintain expertise across all domains. Multi-agent architecture allows:

```
Specialisation → Each agent masters one domain
Collaboration  → Agents share findings
Integration    → Synthesis agent combines perspectives
Provenance     → Dedicated agent tracks all claims
```

---

## Agent Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Research Query                               │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  ORCHESTRATOR                                                       │
│  - Query analysis                                                  │
│  - Task decomposition                                              │
│  - Agent coordination                                              │
│  - Result integration                                              │
└─────────────────────────────────────────────────────────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ LITERATURE      │    │ TARGET          │    │ CHEMISTRY       │
│ AGENT           │    │ AGENT           │    │ AGENT           │
│                 │    │                 │    │                 │
│ - Paper search  │    │ - Target biology│    │ - Compound data │
│ - Extraction    │    │ - Druggability  │    │ - SAR analysis  │
│ - Synthesis     │    │ - Validation    │    │ - ADMET         │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PROVENANCE AGENT                                                   │
│  - Source tracking                                                 │
│  - Citation validation                                             │
│  - Confidence propagation                                          │
│  - Conflict detection                                              │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYNTHESIS AGENT                                                    │
│  - Cross-domain integration                                        │
│  - Narrative construction                                          │
│  - Uncertainty communication                                       │
│  - Report generation                                               │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Research Report                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent 1: Literature Agent

### Purpose
Retrieve and extract information from scientific literature.

### Responsibilities
- Query formulation for literature databases
- Paper retrieval and ranking
- Key finding extraction
- Citation management

### Capabilities

| Capability | Implementation | Output |
|:-----------|:---------------|:-------|
| Search | PubMed API, semantic search | Ranked paper list |
| Filter | Date, journal, citation count | Filtered results |
| Extract | LLM-based extraction | Structured findings |
| Summarise | Multi-document synthesis | Literature summary |

### Agent Specification

```yaml
literature_agent:
  role: "Scientific literature retrieval and synthesis"
  
  inputs:
    - research_query: string
    - date_range: optional[tuple]
    - source_filters: optional[list]
    
  outputs:
    - papers: list[Paper]
    - extractions: list[Extraction]
    - synthesis: LiteratureSummary
    
  tools:
    - pubmed_search
    - semantic_search
    - pdf_parser
    - extraction_llm
    
  constraints:
    - max_papers_per_query: 100
    - extraction_must_cite_source: true
    - no_hallucinated_citations: critical
```

### Example Interaction

```
Orchestrator → Literature Agent:
{
  "task": "retrieve_literature",
  "query": "KRAS G12C inhibitor resistance mechanisms",
  "date_range": ["2020-01-01", "2024-01-01"],
  "max_results": 50
}

Literature Agent → Orchestrator:
{
  "papers_retrieved": 47,
  "key_findings": [
    {
      "finding": "Acquired KRAS mutations (G12D/V) confer resistance",
      "source": {"pmid": "33106123", "title": "...", "year": 2021},
      "confidence": 0.9,
      "evidence_type": "clinical_observation"
    },
    {
      "finding": "MAPK pathway reactivation common resistance mechanism",
      "source": {"pmid": "34234567", "title": "...", "year": 2022},
      "confidence": 0.85,
      "evidence_type": "preclinical"
    }
  ],
  "synthesis": "Literature identifies several resistance mechanisms...",
  "gaps": ["Limited data on combination strategies"]
}
```

### Your Task: Literature Agent Design

1. **Search strategy**
   - How do you formulate effective queries?
   - How do you handle query ambiguity?
   - How do you balance precision and recall?

2. **Extraction protocol**
   - What do you extract from each paper?
   - How do you handle extraction errors?
   - How do you validate extractions?

3. **Quality signals**
   - How do you rank papers?
   - How do you weight source quality?
   - How do you detect when coverage is insufficient?

---

## Agent 2: Target Agent

### Purpose
Analyse biological targets for drug discovery potential.

### Responsibilities
- Target biology summarisation
- Disease association assessment
- Druggability evaluation
- Competitive landscape analysis

### Capabilities

| Capability | Data Sources | Output |
|:-----------|:-------------|:-------|
| Biology | UniProt, Gene Ontology | Function summary |
| Disease link | GWAS, OMIM, literature | Association strength |
| Druggability | Structural data, precedent | Druggability score |
| Landscape | Patents, clinical trials | Competitive map |

### Agent Specification

```yaml
target_agent:
  role: "Biological target analysis and assessment"
  
  inputs:
    - target_id: string  # Gene symbol, UniProt ID
    - disease_context: optional[string]
    - assessment_type: enum[full, druggability, landscape]
    
  outputs:
    - target_profile: TargetProfile
    - disease_associations: list[DiseaseAssociation]
    - druggability_assessment: DruggabilityScore
    - competitive_landscape: LandscapeReport
    
  tools:
    - uniprot_api
    - disease_databases
    - patent_search
    - clinical_trial_search
    
  constraints:
    - all_claims_must_cite_source: true
    - druggability_requires_evidence: true
```

### Example Interaction

```
Orchestrator → Target Agent:
{
  "task": "assess_target",
  "target_id": "KRAS",
  "disease_context": "pancreatic_cancer",
  "assessment_type": "full"
}

Target Agent → Orchestrator:
{
  "target_profile": {
    "gene": "KRAS",
    "protein": "GTPase KRas",
    "function": "Signal transduction, cell proliferation",
    "sources": ["UniProt:P01116", "PMID:12345678"]
  },
  "disease_associations": [
    {
      "disease": "Pancreatic adenocarcinoma",
      "association_type": "driver_mutation",
      "prevalence": "90%+ of cases",
      "evidence_strength": "strong",
      "sources": ["PMID:23456789", "COSMIC"]
    }
  ],
  "druggability_assessment": {
    "score": 0.7,
    "rationale": "Historically considered undruggable, but recent...",
    "precedent": ["Sotorasib (G12C)", "Adagrasib (G12C)"],
    "challenges": ["No approved non-G12C inhibitors"],
    "sources": ["FDA label", "PMID:34567890"]
  }
}
```

### Your Task: Target Agent Design

1. **Data integration**
   - Which databases do you query?
   - How do you reconcile conflicting data?
   - How do you handle missing data?

2. **Druggability assessment**
   - What factors contribute to druggability?
   - How do you weight precedent vs. novel targets?
   - How do you communicate uncertainty?

3. **Competitive intelligence**
   - How do you map the landscape?
   - How current must data be?
   - How do you handle incomplete information?

---

## Agent 3: Chemistry Agent

### Purpose
Analyse compounds and structure-activity relationships.

### Responsibilities
- Compound property retrieval
- SAR analysis
- ADMET assessment
- Chemical series characterisation

### Capabilities

| Capability | Data Sources | Output |
|:-----------|:-------------|:-------|
| Properties | ChEMBL, PubChem | Property profile |
| Activity | ChEMBL assays | Activity data |
| ADMET | Literature, predictions | ADMET profile |
| SAR | Series analysis | SAR summary |

### Agent Specification

```yaml
chemistry_agent:
  role: "Compound analysis and SAR reasoning"
  
  inputs:
    - compound_id: optional[string]  # ChEMBL ID, SMILES
    - target_id: optional[string]
    - query_type: enum[compound_profile, sar_analysis, admet]
    
  outputs:
    - compound_profile: optional[CompoundProfile]
    - activity_data: list[ActivityDatapoint]
    - admet_profile: ADMETProfile
    - sar_summary: optional[SARSummary]
    
  tools:
    - chembl_api
    - pubchem_api
    - admet_predictor
    - structure_similarity
    
  constraints:
    - experimental_data_preferred: true
    - predictions_must_be_labelled: true
    - sources_required_for_all_data: true
```

### Example Interaction

```
Orchestrator → Chemistry Agent:
{
  "task": "compound_landscape",
  "target_id": "KRAS_G12C",
  "query_type": "sar_analysis"
}

Chemistry Agent → Orchestrator:
{
  "compound_count": 234,
  "chemical_series": [
    {
      "name": "Covalent quinazoline series",
      "exemplar": "Sotorasib",
      "key_features": ["Covalent warhead", "Switch II pocket binding"],
      "activity_range": "IC50 1-100 nM",
      "sources": ["ChEMBL", "PMID:32955176"]
    }
  ],
  "sar_insights": [
    {
      "observation": "Covalent binding to Cys12 essential for activity",
      "evidence": "All active compounds contain electrophilic warhead",
      "confidence": 0.95,
      "sources": ["PMID:32955176", "PMID:33106123"]
    }
  ],
  "admet_trends": {
    "general_profile": "Moderate oral bioavailability, hepatic metabolism",
    "concerns": ["CYP3A4 interactions noted for some compounds"],
    "sources": ["FDA label", "PMID:34567890"]
  }
}
```

### Your Task: Chemistry Agent Design

1. **Data retrieval**
   - How do you query chemical databases?
   - How do you handle structure searches?
   - How do you integrate multiple data sources?

2. **SAR reasoning**
   - How do you identify meaningful patterns?
   - How do you distinguish correlation from causation?
   - How do you communicate SAR uncertainty?

3. **ADMET assessment**
   - How do you balance experimental vs. predicted data?
   - How do you flag predictions clearly?
   - How do you handle incomplete ADMET profiles?

---

## Agent 4: Provenance Agent

### Purpose
Track and validate all claims and their sources.

### Responsibilities
- Source validation
- Citation verification
- Confidence propagation
- Conflict detection

### Capabilities

| Capability | Method | Output |
|:-----------|:-------|:-------|
| Validation | Source lookup | Validation status |
| Verification | Content matching | Verification result |
| Propagation | Confidence model | Updated confidences |
| Conflict | Comparison | Conflict report |

### Agent Specification

```yaml
provenance_agent:
  role: "Provenance tracking and validation"
  
  inputs:
    - claims: list[Claim]
    - validation_level: enum[basic, thorough]
    
  outputs:
    - validated_claims: list[ValidatedClaim]
    - conflicts: list[Conflict]
    - confidence_updates: list[ConfidenceUpdate]
    - provenance_graph: ProvenanceGraph
    
  tools:
    - citation_lookup
    - content_verifier
    - conflict_detector
    
  constraints:
    - all_claims_must_be_validated: true
    - conflicts_must_be_surfaced: true
    - confidence_must_propagate: true
```

### Example Interaction

```
Orchestrator → Provenance Agent:
{
  "task": "validate_claims",
  "claims": [
    {
      "claim": "KRAS G12C mutations occur in 13% of NSCLC",
      "source": {"pmid": "12345678"},
      "claiming_agent": "target_agent"
    },
    {
      "claim": "KRAS G12C mutations occur in 11% of NSCLC", 
      "source": {"pmid": "23456789"},
      "claiming_agent": "literature_agent"
    }
  ]
}

Provenance Agent → Orchestrator:
{
  "validated_claims": [
    {
      "claim": "KRAS G12C mutations occur in 13% of NSCLC",
      "validation_status": "verified",
      "source_exists": true,
      "content_matches": true
    }
  ],
  "conflicts": [
    {
      "type": "numeric_discrepancy",
      "claims": ["13% of NSCLC", "11% of NSCLC"],
      "sources": ["PMID:12345678", "PMID:23456789"],
      "resolution": "Different patient populations (Western vs. Asian)",
      "recommendation": "Report range with context"
    }
  ],
  "confidence_updates": [
    {
      "claim": "KRAS G12C prevalence in NSCLC",
      "original_confidence": 0.9,
      "updated_confidence": 0.85,
      "reason": "Conflicting sources, population-dependent"
    }
  ]
}
```

### Your Task: Provenance Agent Design

1. **Validation approach**
   - How do you verify citations exist?
   - How do you verify content matches claims?
   - How do you handle unavailable sources?

2. **Conflict detection**
   - What types of conflicts do you detect?
   - How do you assess conflict severity?
   - How do you recommend resolution?

3. **Confidence propagation**
   - How do conflicts affect confidence?
   - How does inference depth affect confidence?
   - How do you communicate confidence changes?

---

## Agent 5: Synthesis Agent

### Purpose
Integrate findings across agents into coherent research outputs.

### Responsibilities
- Cross-domain integration
- Narrative construction
- Uncertainty communication
- Report generation

### Agent Specification

```yaml
synthesis_agent:
  role: "Integration and communication"
  
  inputs:
    - agent_outputs: dict[str, AgentOutput]
    - original_query: str
    - output_format: enum[summary, report, presentation]
    
  outputs:
    - synthesis: SynthesisDocument
    - key_findings: list[KeyFinding]
    - open_questions: list[OpenQuestion]
    - confidence_summary: ConfidenceSummary
    
  constraints:
    - must_preserve_provenance: true
    - must_surface_conflicts: true
    - must_communicate_uncertainty: true
    - no_claims_without_source: critical
```

### Synthesis Principles

| Principle | Implementation |
|:----------|:---------------|
| **Provenance preservation** | Every claim in output traces to source |
| **Conflict transparency** | Disagreements shown, not hidden |
| **Uncertainty honesty** | Confidence levels clear throughout |
| **Actionable output** | Researchers know what to do next |

---

## Agent Coordination

### Orchestration Pattern

```python
class DrugDiscoveryOrchestrator:
    """
    Coordinates multi-agent drug discovery pipeline.
    """
    
    def __init__(self):
        self.literature = LiteratureAgent()
        self.target = TargetAgent()
        self.chemistry = ChemistryAgent()
        self.provenance = ProvenanceAgent()
        self.synthesis = SynthesisAgent()
    
    async def process_query(self, query: str) -> ResearchReport:
        # Analyse query to determine required agents
        query_analysis = self.analyse_query(query)
        
        # Parallel retrieval from domain agents
        agent_tasks = []
        if query_analysis.needs_literature:
            agent_tasks.append(self.literature.search(query))
        if query_analysis.needs_target:
            agent_tasks.append(self.target.assess(query_analysis.target))
        if query_analysis.needs_chemistry:
            agent_tasks.append(self.chemistry.analyse(query_analysis.compounds))
        
        agent_results = await asyncio.gather(*agent_tasks)
        
        # Provenance validation
        all_claims = self.extract_claims(agent_results)
        validated = await self.provenance.validate(all_claims)
        
        # Synthesis
        report = await self.synthesis.integrate(
            agent_results, 
            validated,
            query
        )
        
        return report
```

### Communication Protocol

```python
@dataclass
class AgentMessage:
    source_agent: str
    content: dict
    claims: list[Claim]
    confidence: float
    metadata: dict

@dataclass
class Claim:
    statement: str
    sources: list[Citation]
    confidence: float
    evidence_type: str  # experimental, computational, inferred
    
@dataclass
class Citation:
    source_type: str  # pmid, doi, database
    source_id: str
    title: str
    relevance_score: float
```

---

## Deliverables

By the end of this section, you should have:

| Deliverable | Location |
|:------------|:---------|
| **Agent specifications** | `artifacts/agent_specification.md` |
| **Communication protocol** | Defined message formats |
| **Orchestration design** | Query routing and coordination |
| **Error handling** | Agent failure recovery |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Knowledge Architecture](02_knowledge_architecture.md) | [Project Overview](README.md) | [Provenance System →](04_provenance_system.md) |
