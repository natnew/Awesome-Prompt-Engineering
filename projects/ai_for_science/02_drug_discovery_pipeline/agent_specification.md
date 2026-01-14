# Agent Specification

## Document Control

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 0.1 | [Date] | [Name] | Initial draft |

---

## System Overview

**System name:** [Your pipeline name]

**Purpose:** [One sentence description]

**Agents in system:**
1. [Agent 1]
2. [Agent 2]
3. [Agent 3]
4. [Agent 4]
5. [Agent 5]

---

## Agent 1: Literature Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Literature Agent |
| **Role** | Scientific literature retrieval and synthesis |
| **Domain** | Published research, clinical trials, patents |

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| [Responsibility 1] | |
| [Responsibility 2] | |
| [Responsibility 3] | |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| research_query | string | Yes | Natural language research question |
| date_range | tuple | No | Start and end dates for search |
| source_filters | list | No | Specific sources to include/exclude |
| max_results | int | No | Maximum papers to retrieve |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| papers | list[Paper] | Retrieved papers with metadata |
| extractions | list[Extraction] | Key findings from papers |
| synthesis | LiteratureSummary | Integrated summary |
| gaps | list[str] | Identified knowledge gaps |

### Tools

| Tool | Purpose | API/Method |
|:-----|:--------|:-----------|
| [Tool 1] | | |
| [Tool 2] | | |

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| max_papers_per_query | Soft | [Value and rationale] |
| extraction_must_cite_source | Hard | Every extraction must reference source |
| no_hallucinated_citations | Critical | Never invent citations |

### Example Interaction

```
Input:
{
  "task": "[task_type]",
  "query": "[example_query]",
  "parameters": {}
}

Output:
{
  "results": [],
  "provenance": {}
}
```

---

## Agent 2: Target Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Target Agent |
| **Role** | Biological target analysis and assessment |
| **Domain** | Proteins, pathways, disease associations |

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| [Responsibility 1] | |
| [Responsibility 2] | |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| target_id | string | Yes | Gene symbol, UniProt ID, etc. |
| disease_context | string | No | Disease to evaluate against |
| assessment_type | enum | No | Type of analysis requested |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| target_profile | TargetProfile | Complete target information |
| disease_associations | list | Disease links with evidence |
| druggability_assessment | DruggabilityScore | Druggability evaluation |
| competitive_landscape | LandscapeReport | Competitive analysis |

### Tools

| Tool | Purpose | API/Method |
|:-----|:--------|:-----------|
| [Tool 1] | | |
| [Tool 2] | | |

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| [Constraint 1] | | |

---

## Agent 3: Chemistry Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Chemistry Agent |
| **Role** | Compound analysis and SAR reasoning |
| **Domain** | Small molecules, properties, activities |

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| [Responsibility 1] | |
| [Responsibility 2] | |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| compound_id | string | No | Compound identifier |
| target_id | string | No | Target for activity analysis |
| query_type | enum | Yes | Type of analysis requested |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| compound_profile | CompoundProfile | Compound information |
| activity_data | list | Activity measurements |
| sar_summary | SARSummary | Structure-activity analysis |
| admet_profile | ADMETProfile | ADMET properties |

### Tools

| Tool | Purpose | API/Method |
|:-----|:--------|:-----------|
| [Tool 1] | | |
| [Tool 2] | | |

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| experimental_data_preferred | Soft | Prefer experimental over predicted |
| predictions_must_be_labelled | Hard | Always mark predictions |

---

## Agent 4: Provenance Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Provenance Agent |
| **Role** | Source tracking and validation |
| **Domain** | Citations, confidence, conflicts |

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Validate citations | Verify all citations exist and are relevant |
| Detect conflicts | Identify when sources disagree |
| Propagate confidence | Update confidence based on provenance |
| Maintain audit trail | Record all provenance decisions |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| claims | list[Claim] | Yes | Claims to validate |
| validation_level | enum | No | Thoroughness of validation |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| validated_claims | list | Claims with validation status |
| conflicts | list[Conflict] | Detected conflicts |
| confidence_updates | list | Updated confidence scores |
| provenance_graph | ProvenanceGraph | Full provenance structure |

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| all_claims_validated | Hard | Every claim must be checked |
| conflicts_surfaced | Hard | Never hide conflicts |

---

## Agent 5: Synthesis Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Synthesis Agent |
| **Role** | Integration and communication |
| **Domain** | Cross-domain synthesis, reporting |

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Integrate findings | Combine outputs from all agents |
| Construct narrative | Build coherent research report |
| Communicate uncertainty | Express confidence clearly |
| Generate outputs | Produce final deliverables |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| agent_outputs | dict | Yes | Outputs from all agents |
| original_query | str | Yes | User's research question |
| output_format | enum | No | Desired output format |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| synthesis | SynthesisDocument | Integrated report |
| key_findings | list | Highlighted findings |
| open_questions | list | Unanswered questions |
| confidence_summary | dict | Overall confidence assessment |

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| preserve_provenance | Critical | Never lose source attribution |
| surface_conflicts | Hard | Show all disagreements |
| communicate_uncertainty | Hard | Make confidence visible |

---

## Communication Protocol

### Message Format

```python
@dataclass
class AgentMessage:
    source_agent: str      # Sending agent ID
    target_agent: str      # Receiving agent ID (or "orchestrator")
    message_type: str      # request, response, error
    content: dict          # Payload
    claims: list[Claim]    # Claims made in this message
    confidence: float      # Overall confidence
    timestamp: datetime    # When sent
```

### Claim Format

```python
@dataclass
class Claim:
    claim_id: str
    statement: str
    claim_type: str        # fact, inference, speculation
    confidence: float
    sources: list[Citation]
    reasoning_chain: list[str]  # For inferences
```

---

## Orchestration

### Query Routing

| Query Type | Primary Agent | Supporting Agents |
|:-----------|:--------------|:------------------|
| Target assessment | Target Agent | Literature, Chemistry |
| Compound analysis | Chemistry Agent | Literature, Target |
| Literature review | Literature Agent | Target, Chemistry |
| Full research question | All | All |

### Coordination Flow

```
1. Query Analysis
   - Parse user query
   - Determine required agents
   - Plan execution

2. Parallel Retrieval
   - Dispatch to relevant agents
   - Collect responses
   - Monitor for failures

3. Provenance Validation
   - Validate all claims
   - Detect conflicts
   - Update confidences

4. Synthesis
   - Integrate findings
   - Generate report
   - Final quality check
```

---

## Error Handling

### Agent Failure

| Failure Type | Detection | Response |
|:-------------|:----------|:---------|
| Agent timeout | Deadline exceeded | Use partial results, note limitation |
| Agent error | Exception raised | Log error, degrade gracefully |
| No results | Empty response | Acknowledge gap, try alternatives |

### Data Quality Issues

| Issue | Detection | Response |
|:------|:----------|:---------|
| Invalid citation | Validation fails | Remove claim, log issue |
| Low confidence | Below threshold | Add uncertainty markers |
| Conflict detected | Provenance agent | Surface to user |

---

## Sign-Off

| Role | Name | Date | Signature |
|:-----|:-----|:-----|:----------|
| System Architect | | | |
| Domain Expert | | | |
| Quality Lead | | | |
