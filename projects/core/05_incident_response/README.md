[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Projects Overview](../00_overview.md) | [Competencies](../../Competencies.md)

# Project 5: Incident Response Simulation

## The Challenge

Your AI system is in production. Something goes wrong. **What do you do?**

The time to figure out your incident response process is not during an incident. It's now — when you can think clearly, plan carefully, and practice without pressure.

This project teaches you to prepare for, detect, respond to, and learn from AI system failures.

---

## What You'll Do

You'll work through realistic AI incident scenarios and produce:

1. **Incident runbooks** — Documented response procedures
2. **Detection strategies** — How to know something is wrong
3. **Communication templates** — What to say to whom
4. **Post-mortem practice** — How to learn from incidents

This is a simulation. The failures are fictional. The learning is real.

---

## Competencies Developed

| Competency | Emphasis | What You'll Practice |
|:-----------|:--------:|:---------------------|
| **Safety & Reliability** | ●●● | Incident detection, response, recovery |
| **Governance & Defensibility** | ●● | Documentation, communication, accountability |
| **Evaluation & Measurement** | ● | Metrics, monitoring, alerting |

---

## Prerequisites

- Understanding of AI system architecture (complete [Agent with Guardrails](../02_agent_with_guardrails/) first recommended)
- Familiarity with monitoring and alerting concepts
- Basic understanding of on-call and incident response (helpful but not required)

---

## Time Estimate

| Depth | Time | What You'll Produce |
|:------|:-----|:--------------------|
| **Minimum** | 4-6 hours | Walk through 2 scenarios, basic runbook |
| **Recommended** | 8-10 hours | All scenarios, complete runbook set, post-mortem |
| **Deep Dive** | 12-16 hours | Full simulation, team exercise, comprehensive documentation |

---

## Project Structure

```
05_incident_response/
├── README.md                    # You are here
├── 01_incident_framework.md     # How incidents work
├── 02_detection.md              # Knowing something is wrong
├── 03_response.md               # What to do when it happens
├── 04_communication.md          # Who to tell and what to say
├── 05_recovery.md               # Getting back to normal
├── 06_learning.md               # Post-mortems and improvement
├── 07_synthesis.md              # Bringing it together
├── scenarios/
│   ├── scenario_1_hallucination_crisis.md
│   ├── scenario_2_cost_explosion.md
│   └── scenario_3_data_leak.md
└── artifacts/
    ├── runbook_template.md
    ├── postmortem_template.md
    └── communication_templates.md
```

---

## The Scenarios

You'll work through three incident scenarios:

### Scenario 1: Hallucination Crisis

Your customer service AI starts giving confidently wrong answers. Customers are complaining. Some have acted on bad information.

**Practice:** Detection, immediate response, customer communication, root cause analysis.

### Scenario 2: Cost Explosion

Your AI usage costs spike 10x overnight. You're burning through your monthly budget in days.

**Practice:** Alerting, cost controls, triage, business communication.

### Scenario 3: Data Leak Suspicion

A user reports seeing another user's information in an AI response. Is this real? How bad is it?

**Practice:** Investigation, escalation, legal/compliance coordination, incident communication.

---

## What "Done" Looks Like

You've completed this project when you have:

### Required Artifacts

1. **Incident runbook** — Detection, response, recovery procedures for AI-specific incidents
2. **Post-mortem** — Completed post-mortem for at least one scenario
3. **Communication templates** — Templates for stakeholder, user, and internal communication

### Quality Criteria

Your artifacts should:
- [ ] Be usable by someone who wasn't involved in creating them
- [ ] Include specific, actionable steps (not vague guidance)
- [ ] Address AI-specific failure modes
- [ ] Include escalation criteria and paths
- [ ] Have communication templates ready to use

### Self-Assessment Questions

After completing the project, you should be able to answer:
- How would you know if your AI system started giving wrong answers?
- What's the first thing you do when you detect an incident?
- Who needs to know about an incident, and when?
- How do you decide to shut down a system vs. keep it running?
- How do you prevent the same incident from happening again?

---

## Navigation

| Section | Focus | Time |
|:--------|:------|:-----|
| [01 Incident Framework](01_incident_framework.md) | How incidents work | 30 min |
| [02 Detection](02_detection.md) | Knowing something is wrong | 1 hour |
| [03 Response](03_response.md) | What to do | 1-2 hours |
| [04 Communication](04_communication.md) | Who to tell | 1 hour |
| [05 Recovery](05_recovery.md) | Getting back to normal | 1 hour |
| [06 Learning](06_learning.md) | Post-mortems | 1-2 hours |
| [07 Synthesis](07_synthesis.md) | Bringing it together | 1 hour |

---

## Ready?

Start with [Incident Framework →](01_incident_framework.md)

Or jump directly to a scenario:
- [Scenario 1: Hallucination Crisis](scenarios/scenario_1_hallucination_crisis.md)
- [Scenario 2: Cost Explosion](scenarios/scenario_2_cost_explosion.md)
- [Scenario 3: Data Leak Suspicion](scenarios/scenario_3_data_leak.md)

---

*This project is part of the [Core Projects](../00_overview.md) tier. It builds on safety and governance skills from earlier projects.*
