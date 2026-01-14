[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Projects Overview](../00_overview.md) | [Competencies](../../Competencies.md)

# Project 2: Agent with Guardrails

## The Challenge

Agents are powerful. Agents without guardrails are dangerous.

The promise of autonomous AI agents — systems that can reason, plan, and take actions — is enormous. The risk is equally large: agents that run away, spend unlimited resources, take harmful actions, or fail in ways that are hard to detect or reverse.

This project teaches you to build agents that are **designed to fail safely**. Not agents that won't fail — that's impossible. Agents where failure is expected, contained, and recoverable.

---

## What You'll Build

By the end of this project, you'll have:

1. **A tool-using agent** — An agent that can reason, plan, and execute actions using external tools.

2. **Guardrails system** — Constraints that prevent harmful or unintended behavior.

3. **Circuit breakers** — Mechanisms that stop runaway processes before they cause damage.

4. **Monitoring infrastructure** — Observability into what the agent is doing and why.

5. **Human escalation paths** — Clear triggers for when automation should stop and humans should decide.

6. **Production runbook** — Documentation for operating the agent safely.

---

## Competencies Developed

| Competency | Emphasis | What You'll Practice |
|:-----------|:--------:|:---------------------|
| **Safety & Reliability** | ●●● | Guardrails, circuit breakers, failure modes, graceful degradation |
| **Systems Design for AI** | ●●● | Agent architecture, tool design, state management |
| **Governance & Defensibility** | ●● | Audit trails, decision documentation, stakeholder communication |
| **Evaluation & Measurement** | ● | Agent behavior testing, safety validation |
| **AI Output Review** | ● | Reviewing agent decisions and actions |

---

## Prerequisites

Before starting this project, you should have:

- [ ] Completed [RAG Evaluation Pipeline](../01_rag_evaluation_pipeline/) or equivalent
- [ ] Basic understanding of agent architectures (read [Agents Guide](../../Agents.md))
- [ ] Familiarity with tool/function calling in LLMs
- [ ] Python proficiency

---

## Time Estimate

| Depth | Time | What You'll Produce |
|:------|:-----|:--------------------|
| **Minimum** | 6-8 hours | Working agent + basic guardrails + runbook draft |
| **Recommended** | 12-16 hours | Full guardrail system + monitoring + polished runbook |
| **Deep Dive** | 20-24 hours | Red teaming + comprehensive testing + incident simulation |

---

## Project Structure

```
02_agent_with_guardrails/
├── README.md                    # You are here
├── 01_problem_framing.md        # The scenario and threat model
├── 02_agent_architecture.md     # Designing the agent system
├── 03_guardrails.md             # Implementing safety constraints
├── 04_circuit_breakers.md       # Stopping runaway processes
├── 05_monitoring.md             # Observability and alerting
├── 06_human_escalation.md       # When to involve humans
├── 07_synthesis.md              # Bringing it together
├── artifacts/
│   ├── runbook_template.md      # Production runbook template
│   ├── guardrail_spec.md        # Guardrail specification template
│   └── threat_model.md          # Threat modeling template
└── reference/
    └── guarded_agent.py         # Reference implementation
```

---

## The Core Insight

**Safety is architecture, not policy.**

You can't make an agent safe by writing a policy document or adding a disclaimer. Safety emerges from design decisions:

- What actions can the agent take?
- What actions are forbidden?
- What happens when the agent tries something forbidden?
- What happens when the agent fails?
- When does a human get involved?

These decisions must be made upfront and enforced structurally — not hoped for.

---

## What "Done" Looks Like

You've completed this project when you have:

### Required Artifacts

1. **Working guarded agent** — An agent with tools, guardrails, and circuit breakers
2. **Guardrail specification** — Documented constraints and their enforcement mechanisms
3. **Threat model** — Analysis of how the agent could fail or be misused
4. **Production runbook** — Operational documentation for running the agent safely
5. **Monitoring dashboard spec** — What metrics to track and alert on

### Quality Criteria

Your artifacts should:
- [ ] Identify at least 5 specific failure modes
- [ ] Implement guardrails for each identified failure mode
- [ ] Include circuit breakers with defined thresholds
- [ ] Specify human escalation triggers
- [ ] Document what happens when each guardrail fires

### Self-Assessment Questions

After completing the project, you should be able to answer:
- What's the worst thing this agent could do?
- How would you know if the agent was misbehaving?
- What happens if the agent enters an infinite loop?
- When should a human be notified vs. when should the agent be stopped?
- How would you explain the agent's safety constraints to a non-technical stakeholder?

---

## Navigation

| Section | Focus | Time |
|:--------|:------|:-----|
| [01 Problem Framing](01_problem_framing.md) | Scenario and threat model | 45 min |
| [02 Agent Architecture](02_agent_architecture.md) | Designing the agent system | 1-2 hours |
| [03 Guardrails](03_guardrails.md) | Implementing safety constraints | 2-3 hours |
| [04 Circuit Breakers](04_circuit_breakers.md) | Stopping runaway processes | 1-2 hours |
| [05 Monitoring](05_monitoring.md) | Observability and alerting | 1-2 hours |
| [06 Human Escalation](06_human_escalation.md) | When to involve humans | 1 hour |
| [07 Synthesis](07_synthesis.md) | Bringing it together | 1-2 hours |

---

## Ready?

Start with [Problem Framing →](01_problem_framing.md)

---

*This project is part of the [Core Projects](../00_overview.md) tier. It builds directly on evaluation thinking and introduces safety as a design constraint.*
