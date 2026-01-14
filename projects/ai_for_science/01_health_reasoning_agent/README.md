[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../../../COMPETENCIES.md) | [AI for Science](../README.md) | [Core Projects](../../core/README.md)

# Project: Health Reasoning Agent

Build a multi-agent health reasoning system that augments health literacy while maintaining hard safety boundaries.

---

## What You'll Build

A conversational health reasoning system that helps everyday people understand health information — with appropriate guardrails, uncertainty communication, and escalation paths.

This is **not** a diagnostic tool. It's a health literacy assistant that:
- Helps users understand symptoms and when to seek care
- Synthesises information from trusted medical sources
- Communicates uncertainty honestly
- Knows its limits and escalates appropriately

---

## Project Overview

| Attribute | Value |
|:----------|:------|
| **Time Estimate** | 10-14 hours |
| **Difficulty** | Advanced |
| **Prerequisites** | Complete 3+ Core Projects, especially Agent with Guardrails |

### Primary Competencies

| Competency | Depth | Why |
|:-----------|:------|:----|
| Safety & Reliability | ●●●●● | Medical domain requires hard safety boundaries |
| Output Review & Oversight | ●●●● | Every recommendation must be auditable |
| Governance & Defensibility | ●●●● | Regulatory awareness, ethical constraints |
| Systems Design | ●●● | Multi-agent coordination |
| Evaluation & Measurement | ●●● | Must measure safety AND helpfulness |

---

## Why This Project Matters

Health AI sits at the intersection of enormous potential benefit and serious risk of harm.

**The opportunity:** Billions of people lack access to basic health literacy. AI can help bridge this gap — explaining symptoms, contextualising information, guiding people toward appropriate care.

**The risk:** AI that overreaches causes direct harm. False reassurance delays treatment. False alarm causes unnecessary anxiety. Confident-sounding nonsense erodes trust in legitimate healthcare.

**What you'll learn:** How to build AI systems that help without harming — the design patterns, evaluation approaches, and safety mechanisms that make responsible health AI possible.

---

## The Mental Model

Think of this system as a **knowledgeable friend who studied medicine** — not a doctor.

A good friend with medical knowledge:
- Listens carefully and asks clarifying questions
- Shares relevant information from trusted sources
- Is honest about uncertainty ("I'm not sure, but...")
- Knows when to say "you should really see a doctor about this"
- Never pretends to have expertise they don't have
- Understands that their role is to support, not replace, professional care

Your system should embody these same qualities.

---

## What You'll Deliver

### 1. Multi-Agent Architecture
Design and implement a system with specialised agents:
- **Intake Agent** — Structured symptom collection with empathy
- **Reasoning Agent** — Symptom analysis with uncertainty quantification
- **Literature Agent** — Evidence retrieval from trusted sources
- **Synthesis Agent** — Clear, honest communication to users
- **Safety Agent** — Continuous monitoring for escalation triggers

### 2. Safety Framework
A comprehensive safety system including:
- Hard boundaries (topics the system will not engage with)
- Soft escalations (triggers for "see a doctor" recommendations)
- Uncertainty thresholds (when to say "I don't know")
- Audit trail for every interaction

### 3. Evaluation Suite
Metrics and test cases covering:
- Safety (does it escalate when it should?)
- Accuracy (is the information correct?)
- Helpfulness (does it actually help users?)
- Calibration (does uncertainty match reality?)

### 4. Governance Documentation
- Scope definition (what this system is and isn't)
- Ethical constraints and their rationale
- Incident response procedures
- User communication guidelines

---

## What "Done" Looks Like

You've completed this project when you have:

| Deliverable | Evidence |
|:------------|:---------|
| Working multi-agent system | Handles diverse health queries appropriately |
| Safety framework | Documented boundaries, escalations, audit trail |
| Evaluation suite | Passes safety tests, measures helpfulness |
| Governance docs | Clear scope, ethical constraints, incident procedures |
| Reflection | Synthesis document with honest assessment |

---

## Project Structure

```
01_health_reasoning_agent/
├── README.md                      # This file
├── 01_problem_framing.md          # Scenario, constraints, stakeholders
├── 02_safety_architecture.md      # Hard boundaries, escalation triggers
├── 03_agent_design.md             # Multi-agent coordination patterns
├── 04_uncertainty_communication.md # How to be honest with users
├── 05_evaluation_framework.md     # Measuring safety and helpfulness
├── synthesis.md                   # Reflection and portfolio artifact
├── artifacts/
│   ├── scope_definition.md        # What the system is and isn't
│   ├── safety_specification.md    # Formal safety constraints
│   ├── escalation_protocol.md     # When and how to escalate
│   ├── evaluation_scorecard.md    # Test cases and metrics
│   └── incident_response.md       # What to do when things go wrong
└── reference/
    └── (optional implementation)
```

---

## Before You Begin

### Mindset

This project requires holding two truths simultaneously:
1. AI can genuinely help people understand health information
2. AI that overreaches in health causes real harm

Your job is to build something that maximises (1) while preventing (2). This tension is the core design challenge.

### Ethical Grounding

Before you write any code or prompts, spend time with these questions:
- What are the potential harms this system could cause?
- Who is most vulnerable to those harms?
- What would I want if I were a user in distress?
- What responsibility do I have as a builder?

Document your answers. They'll guide your design decisions.

---

## Ready?

[Start with Problem Framing →](01_problem_framing.md)

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [AI for Science Overview](../README.md) | [All Projects](../../README.md) | [Problem Framing](01_problem_framing.md) |
