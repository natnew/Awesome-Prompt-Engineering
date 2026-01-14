# Integration Guide

## Overview

This document describes how the drug discovery pipeline integrates with scientific workflows and existing tools.

---

## Integration Philosophy

### Principles

| Principle | Implementation |
|:----------|:---------------|
| **Augment, don't replace** | System supports scientists, not substitutes for them |
| **Verify, don't trust** | All outputs designed to be verifiable |
| **Export, don't lock** | Data exportable to standard formats |
| **Integrate, don't isolate** | Works with existing scientific tools |

### User Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SCIENTIFIC WORKFLOW                              │
└─────────────────────────────────────────────────────────────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
         ▼                      ▼                      ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Literature      │   │ Data Analysis   │   │ Documentation   │
│ Review          │   │ Tools           │   │ & Reporting     │
│                 │   │                 │   │                 │
│ • PubMed        │   │ • R/Python      │   │ • Word/LaTeX    │
│ • Zotero        │   │ • GraphPad      │   │ • PowerPoint    │
│ • Mendeley      │   │ • Spotfire      │   │ • Confluence    │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 DRUG DISCOVERY PIPELINE                             │
│                 (This System)                                       │
│                                                                     │
│   Inputs:  Research queries from scientists                        │
│   Outputs: Synthesis reports with provenance                       │
│   Role:    Accelerate literature review and synthesis              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Input Integration

### Query Sources

| Source | Integration Method | Notes |
|:-------|:-------------------|:------|
| Direct query | Web interface / API | Primary method |
| Slack | Bot integration | Team access |
| Jupyter | Python SDK | Data science workflow |
| Email | Forwarding integration | Asynchronous queries |

### Query Format

**Simple query:**
```
"What's known about BRAF inhibitor resistance?"
```

**Structured query:**
```json
{
  "query": "What's known about BRAF inhibitor resistance?",
  "context": {
    "disease": "melanoma",
    "focus": ["mechanisms", "clinical observations"],
    "date_range": ["2020-01-01", null]
  },
  "output_format": "detailed_report"
}
```

---

## Output Formats

### Report Formats

| Format | Use Case | Contents |
|:-------|:---------|:---------|
| **Summary** | Quick answers | Key findings, top citations |
| **Detailed Report** | Deep dive | Full synthesis, all citations |
| **Presentation** | Team meetings | Slides with key points |
| **Data Export** | Further analysis | Structured data |

### Summary Format

```markdown
# [Query Title]

## Key Findings
- [Finding 1] [1]
- [Finding 2] [2,3]
- [Finding 3] [4]

## Confidence Assessment
[High/Medium/Low] confidence based on [N] sources.

## References
1. [Citation 1]
2. [Citation 2]
...
```

### Detailed Report Format

```markdown
# [Query Title]

## Executive Summary
[2-3 paragraph summary]

## Background
[Context and framing]

## Findings

### [Topic 1]
[Detailed synthesis with inline citations [1,2]]

### [Topic 2]
[Detailed synthesis]

## Conflicts and Uncertainties
[Known disagreements in literature]

## Gaps and Limitations
[What we don't know]

## Conclusion
[Summary and recommendations]

## References
[Full bibliography]

## Appendix: Provenance
[Detailed provenance information]
```

---

## Export Integrations

### Reference Manager Export

**Supported formats:**
- BibTeX (.bib)
- RIS (.ris)
- EndNote XML
- Zotero RDF

**Export example (BibTeX):**
```bibtex
@article{smith2021kras,
  title={KRAS G12C Inhibitors in Clinical Development},
  author={Smith, John and Doe, Jane},
  journal={Nature Reviews Drug Discovery},
  year={2021},
  volume={20},
  pages={100-115},
  doi={10.1038/s41573-021-00100-1}
}
```

### Data Export

**Structured data (JSON):**
```json
{
  "query": "...",
  "timestamp": "...",
  "claims": [
    {
      "statement": "...",
      "confidence": 0.85,
      "sources": ["PMID:12345678"],
      "claim_type": "fact"
    }
  ],
  "conflicts": [...],
  "provenance": {...}
}
```

**Tabular data (CSV):**
```csv
claim_id,statement,confidence,sources,claim_type
C001,"KRAS G12C occurs in 13% of NSCLC",0.9,"PMID:12345;PMID:23456",fact
```

### Notebook Integration

**Jupyter/Python:**
```python
from drug_discovery_pipeline import Client

client = Client(api_key="...")

# Run query
result = client.query(
    "What's known about KRAS G12C inhibitors?",
    output_format="detailed"
)

# Access structured data
for claim in result.claims:
    print(f"{claim.statement} (confidence: {claim.confidence})")
    for source in claim.sources:
        print(f"  - {source.citation}")

# Export to DataFrame
df = result.to_dataframe()

# Export citations
result.export_citations("references.bib", format="bibtex")
```

---

## Tool Integrations

### Literature Management

| Tool | Integration | Capability |
|:-----|:------------|:-----------|
| Zotero | Export | BibTeX/RIS export |
| Mendeley | Export | RIS export |
| EndNote | Export | XML export |
| Papers | Export | RIS export |

### Documentation

| Tool | Integration | Capability |
|:-----|:------------|:-----------|
| Microsoft Word | Export | DOCX with citations |
| Google Docs | Export | HTML import |
| LaTeX | Export | BibTeX + formatted text |
| Confluence | API | Direct publish |

### Data Analysis

| Tool | Integration | Capability |
|:-----|:------------|:-----------|
| Python/Pandas | SDK | DataFrame export |
| R | Export | CSV/JSON |
| Spotfire | Export | CSV |
| Tableau | Export | CSV/JSON |

### Communication

| Tool | Integration | Capability |
|:-----|:------------|:-----------|
| Slack | Bot | Query and receive summaries |
| Email | Forwarding | Async queries |
| Teams | Bot | Query integration |

---

## API Reference

### Authentication

```python
# API key authentication
client = Client(api_key="your-api-key")

# OAuth (for enterprise)
client = Client(oauth_token="your-token")
```

### Endpoints

| Endpoint | Method | Purpose |
|:---------|:-------|:--------|
| `/query` | POST | Submit research query |
| `/status/{id}` | GET | Check query status |
| `/result/{id}` | GET | Get query results |
| `/export/{id}` | GET | Export in specified format |

### Query Request

```json
POST /api/v1/query

{
  "query": "string",
  "context": {
    "disease": "string (optional)",
    "target": "string (optional)",
    "date_range": ["start", "end"] (optional)
  },
  "options": {
    "output_format": "summary|detailed|data",
    "max_sources": 100,
    "include_patents": true
  }
}
```

### Query Response

```json
{
  "query_id": "uuid",
  "status": "completed",
  "result": {
    "summary": "string",
    "claims": [...],
    "citations": [...],
    "conflicts": [...],
    "confidence_summary": {...}
  },
  "provenance": {
    "sources_consulted": [...],
    "processing_time": 12.5,
    "agents_used": [...]
  }
}
```

---

## Verification Workflow

### How Scientists Verify Results

```
1. Review summary
   - Does it address my question?
   - Are key points reasonable?

2. Check key citations
   - Click through to 2-3 important sources
   - Verify claims match source content

3. Review conflicts
   - Are disagreements surfaced?
   - Is the conflict description accurate?

4. Assess confidence
   - Do confidence levels seem reasonable?
   - Are limitations acknowledged?

5. Use or iterate
   - Use results in work, or
   - Refine query for more specific results
```

### Verification Support Features

| Feature | Purpose |
|:--------|:--------|
| Click-through citations | Direct links to sources |
| Source quotes | Exact text supporting claims |
| Confidence explanation | Why confidence is X |
| Conflict details | Full conflict context |
| Audit trail | Complete provenance record |

---

## Security and Compliance

### Data Handling

| Data Type | Handling |
|:----------|:---------|
| Queries | Logged for quality improvement |
| Results | Stored for user access |
| Citations | Cached from public sources |
| User data | Protected per privacy policy |

### Access Control

| Role | Capabilities |
|:-----|:-------------|
| User | Query, view results, export |
| Team Lead | Above + team usage analytics |
| Admin | Above + configuration |

### Audit Requirements

| Requirement | Implementation |
|:------------|:---------------|
| Query logging | All queries logged with timestamp |
| Result retention | Results retained per policy |
| Export tracking | Exports logged |
| Access logging | API access logged |

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|:------|:------|:---------|
| No results | Too specific query | Broaden query terms |
| Low confidence | Limited literature | Note limitation, search manually |
| Missing citations | Retrieval failure | Report issue, try again |
| Slow response | Complex query | Wait or simplify |

### Support

| Channel | Response Time | Use For |
|:--------|:--------------|:--------|
| In-app feedback | 24-48h | Feature requests, minor issues |
| Email support | 24h | Technical issues |
| Slack channel | Same day | Quick questions |

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Integration Lead | | |
| User Representative | | |
