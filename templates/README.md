[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../COMPETENCIES.md) | [Projects](../projects/00_overview.md) | [Patterns](../patterns/README.md)

# Templates

Ready-to-use documents for AI system development, governance, and operations.

---

## How to Use Templates

1. **Copy** — Don't edit originals; copy to your project
2. **Adapt** — Modify sections for your context
3. **Delete** — Remove sections that don't apply (with intention)
4. **Version** — Track changes as your understanding evolves

Templates are starting points, not requirements. A half-completed template that captures real thinking beats a fully-completed template filled with placeholders.

---

## Template Index

### Governance

Documents for decision-making and stakeholder communication.

| Template | Purpose | When to Use |
|:---------|:--------|:------------|
| [Decision Memo](governance/decision_memo.md) | Summarize analysis for decision-makers | Before major AI feature decisions |
| [Stakeholder Brief](governance/stakeholder_brief.md) | Communicate AI capabilities to non-technical audiences | Demos, reviews, leadership updates |
| [Ethics Review](governance/ethics_review.md) | Systematic ethics assessment | Before deploying user-facing AI |

### Safety

Documents for risk identification and mitigation.

| Template | Purpose | When to Use |
|:---------|:--------|:------------|
| [Threat Model](safety/threat_model.md) | Identify and prioritize failure modes | Early in agent/system design |
| [Guardrail Specification](safety/guardrail_spec.md) | Document safety constraints | When implementing guardrails |
| [Runbook](safety/runbook.md) | Operational procedures for production systems | Before production deployment |

### Evaluation

Documents for measuring and validating AI systems.

| Template | Purpose | When to Use |
|:---------|:--------|:------------|
| [Evaluation Scorecard](evaluation/evaluation_scorecard.md) | Track metrics across dimensions | Ongoing quality monitoring |
| [Test Case Specification](evaluation/test_case_spec.md) | Document test scenarios | Building evaluation suites |
| [Benchmark Report](evaluation/benchmark_report.md) | Report comparative results | Model selection, A/B tests |

### Operations

Documents for running AI systems in production.

| Template | Purpose | When to Use |
|:---------|:--------|:------------|
| [Post-Mortem](operations/postmortem.md) | Learn from incidents | After any significant incident |
| [Incident Communication](operations/incident_communication.md) | Status updates during incidents | Active incidents |
| [On-Call Handoff](operations/on_call_handoff.md) | Transfer responsibility between responders | Shift changes, escalations |

### Development

Documents for building AI systems.

| Template | Purpose | When to Use |
|:---------|:--------|:------------|
| [Prompt Specification](development/prompt_spec.md) | Document prompt design decisions | Complex prompt development |
| [Code Review Checklist](development/code_review_checklist.md) | Systematic AI code review | Reviewing AI-generated code |
| [System Design Document](development/system_design_doc.md) | Architecture decisions for AI systems | New AI system design |

---

## Template Principles

### 1. Explicit Over Implicit

Templates force you to write down what you might otherwise assume. The act of filling in sections surfaces gaps in your thinking.

### 2. Living Documents

Templates aren't one-time artifacts. Good templates get updated as you learn. Date your versions.

### 3. Right-Sized

Not every project needs every template. A quick prototype needs a lighter touch than a production system. Scale your documentation to your risk.

| Project Stage | Typical Templates |
|:--------------|:------------------|
| Prototype | Prompt spec (light) |
| Pilot | + Evaluation scorecard, Stakeholder brief |
| Production | + Threat model, Runbook, Ethics review |
| Mature | + All operations templates |

### 4. Audience-Aware

Different templates serve different audiences:

- **Technical**: Prompt spec, Test cases, System design
- **Business**: Decision memo, Stakeholder brief
- **Operations**: Runbook, Post-mortem, Handoff
- **Compliance**: Ethics review, Threat model

Write for your reader.

---

## Contributing Templates

Good templates come from real use. If you've created a template that helped you:

1. Generalize it (remove project-specific details)
2. Add guidance (when to use, how to fill in)
3. Include an example (filled-in version)
4. Submit a PR

---

## Quick Start

**First AI project?** Start with:
1. [Prompt Specification](development/prompt_spec.md) — Document what you're building
2. [Evaluation Scorecard](evaluation/evaluation_scorecard.md) — Define success

**Going to production?** Add:
3. [Threat Model](safety/threat_model.md) — Know your risks
4. [Runbook](safety/runbook.md) — Be ready to operate

**Something went wrong?** Use:
5. [Post-Mortem](operations/postmortem.md) — Learn from it

---

*Templates support the [five competencies](../COMPETENCIES.md). Each template maps to one or more competency areas.*
