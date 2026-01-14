[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Project Overview](README.md) | [Next: Knowledge Architecture →](02_knowledge_architecture.md)

# Problem Framing

Understand the drug discovery context, stakeholders, and the unique requirements of AI for scientific research.

---

## The Scenario

You're building an AI research assistant for a biotech company's early-stage drug discovery team. The team works on identifying new therapeutic targets and evaluating potential lead compounds.

### Context

- **Users:** Computational biologists, medicinal chemists, project leads
- **Scale:** Small team (5-15 researchers) working on 2-3 programs simultaneously
- **Data:** PubMed access, internal screening data, commercial databases
- **Output:** Research reports, target assessments, lead prioritisation

### What Researchers Need

Researchers come to this system with queries like:
- "What's known about [protein X] as a therapeutic target for [disease Y]?"
- "What compounds have shown activity against [target class Z]?"
- "What are the main challenges with [target] from prior work?"
- "Summarise the SAR for [compound series] against [target]"
- "What safety concerns have been reported for [mechanism]?"

They need:
- **Comprehensive coverage** — Don't miss important prior work
- **Accurate synthesis** — Correctly represent what papers say
- **Source traceability** — Every claim citable to original source
- **Honest uncertainty** — Clear about confidence levels
- **Scientific language** — Appropriate domain terminology

### What Researchers Don't Need

- Invented citations or plausible-sounding nonsense
- Overconfident conclusions not supported by evidence
- Generic information they could get from Wikipedia
- Recommendations that substitute for scientific judgment

---

## Stakeholder Map

### Primary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Researchers** | Accelerated literature review, hypothesis support | Missing critical information, incorrect synthesis |
| **Project leads** | Decision-quality summaries | Trusting AI reasoning without verification |
| **Company** | Faster time-to-candidate | Wasted resources on AI-generated wild goose chases |

### Secondary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Regulators** | Eventually: audit trail for drug rationale | Unverified AI claims in regulatory submissions |
| **Patients** | Eventually: better, safer drugs faster | Errors that propagate to clinical development |
| **Scientific community** | Reproducible, verifiable research | AI-generated misinformation in literature |

---

## Constraints

### Hard Constraints (Non-Negotiable)

| Constraint | Rationale |
|:-----------|:----------|
| Every claim must cite sources | Scientific claims require evidence |
| Never fabricate citations | Integrity is non-negotiable |
| Distinguish fact from inference | Readers must know what's certain vs. reasoned |
| Acknowledge uncertainty explicitly | Overconfidence causes harm |

### Soft Constraints (Strong Defaults)

| Constraint | Rationale |
|:-----------|:----------|
| Prefer primary sources | Original papers over reviews when possible |
| Recency weighting | Recent findings may supersede older work |
| Multiple source corroboration | Important claims should have multiple sources |
| Conflict surfacing | Highlight when sources disagree |

### Resource Constraints

| Constraint | Impact |
|:-----------|:-------|
| API rate limits | Limits retrieval volume per query |
| Context window limits | Limits synthesis scope |
| Cost per query | Limits model sophistication |
| Response time targets | Researchers won't wait minutes |

---

## Success Criteria

### Accuracy Metrics

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| Citation accuracy | 100% | Every citation exists and is relevant |
| Factual accuracy | >95% | Claims match source content |
| Coverage | >80% | Major relevant works included |
| Conflict detection | >90% | Disagreements in literature surfaced |

### Utility Metrics

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| Time savings | >50% | vs. manual literature review |
| Decision quality | Maintained | Expert comparison |
| User satisfaction | >4/5 | Researcher ratings |

### Provenance Metrics

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| Traceability | 100% | Every claim has source chain |
| Confidence calibration | ECE <0.1 | Stated vs. actual accuracy |
| Reasoning transparency | High | Human can follow logic |

---

## Failure Modes

### High-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Hallucinated citation** | Citing paper that doesn't exist | Trust destruction, wasted time |
| **Citation misattribution** | Claim cites wrong source | Scientific integrity violation |
| **Inverted finding** | Saying paper found X when it found opposite | Research misdirection |
| **Missed critical safety signal** | Not surfacing known toxicity | Downstream patient safety |

### Medium-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Overconfident synthesis** | Stating as fact what is debated | Premature narrowing |
| **Incomplete coverage** | Missing important relevant work | Repeated failed approaches |
| **Recency bias** | Overweighting new work | Missing foundational knowledge |

### Low-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Overly verbose** | 10 pages when 2 would suffice | User time |
| **Inconsistent terminology** | Using different terms for same concept | Confusion |

---

## Scientific AI Requirements

Drug discovery AI has requirements beyond general AI systems:

### Provenance

```
Every claim must be traceable:

Claim: "KRAS G12C has been validated as an oncology target"
 ↓
Evidence: [Paper A, Clinical Trial B, FDA Approval C]
 ↓
Direct quotes: "Our findings demonstrate..." (Paper A, p. 5)
 ↓
Confidence: High (multiple independent sources)
```

### Uncertainty Propagation

```
Inference chains must track uncertainty:

Literature says: "Compound X inhibits Target Y in vitro" (High confidence)
                 ↓
We infer: "Compound X may inhibit Target Y in vivo" (Medium confidence)
                 ↓
We speculate: "Compound X might be effective for Disease Z" (Low confidence)
```

### Conflict Resolution

```
When sources disagree, surface the conflict:

Paper A (2019): "Target X is essential for disease pathway"
Paper B (2021): "Target X knockout has no effect on disease"

Don't hide this. Show it. Let scientists decide.
```

### Reproducibility

```
Any synthesis should be reproducible:

Query: "What's known about BRAF inhibitor resistance?"
Date: 2024-01-15
Sources queried: PubMed (N=347), Clinical Trials (N=23)
Inclusion criteria: [specified]
Result: [documented]

Another researcher should get similar results.
```

---

## Domain Knowledge Requirements

### What the System Must "Know"

| Domain | Knowledge Type | How Acquired |
|:-------|:---------------|:-------------|
| Biology | Target-disease relationships | Literature retrieval |
| Chemistry | Structure-activity basics | Embedding + retrieval |
| Pharmacology | ADMET concepts | Retrieved knowledge |
| Clinical | Trial designs, endpoints | Literature + databases |

### What the System Must NOT Pretend to Know

| Domain | Why Not |
|:-------|:--------|
| Novel experimental findings | Can't do experiments |
| Proprietary data implications | Doesn't have access |
| Strategic business decisions | Not its role |
| Regulatory outcomes | Can't predict |

---

## Scoping Decisions

### In Scope

| Capability | Description |
|:-----------|:------------|
| Literature synthesis | Comprehensive summaries of published work |
| Target analysis | What's known about potential drug targets |
| Compound landscape | Prior art for compound classes |
| Safety signals | Known toxicity and safety findings |
| Competitive intelligence | Published work from competitors |

### Out of Scope

| Capability | Why |
|:-----------|:----|
| Novel molecule design | Requires different architecture |
| Experimental protocol design | Requires domain expert |
| Regulatory strategy | Requires specialised expertise |
| Clinical trial predictions | Too speculative |

---

## Your Task

### Exercise 1: Stakeholder Deep Dive

For each stakeholder group:
1. What question do they most want answered?
2. What would a great answer look like?
3. What would a harmful answer look like?
4. How do you design for their needs?

### Exercise 2: Failure Mode Analysis

For each high-severity failure mode:
1. What would cause this failure?
2. How would you detect it?
3. How would you prevent it?
4. What's the recovery if it happens?

### Exercise 3: Scientific Standards

Define your standards for:
1. Citation quality (what makes a citation "good"?)
2. Inference transparency (how to show reasoning?)
3. Uncertainty communication (how to express confidence?)
4. Conflict handling (what to do when sources disagree?)

Document your decisions — they'll guide your architecture.

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Project Overview](README.md) | [All Sections](#project-structure) | [Knowledge Architecture →](02_knowledge_architecture.md) |
