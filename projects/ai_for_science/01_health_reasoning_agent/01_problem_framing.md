[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Project Overview](README.md) | [Next: Safety Architecture →](02_safety_architecture.md)

# Problem Framing

Before building anything, understand the problem space deeply.

---

## The Scenario

You're building a health reasoning assistant for a nonprofit focused on health literacy in underserved communities. The goal: help everyday people understand health information and make better decisions about when and how to seek care.

### Context

- **Users:** General public, often with limited health literacy
- **Access:** Mobile-first, conversational interface
- **Languages:** English initially, with internationalisation planned
- **Cost:** Must be sustainable (inference costs matter)
- **Regulation:** Not a medical device, but must operate responsibly

### What Users Need

Users come to this system with questions like:
- "I've had this headache for three days — should I be worried?"
- "My doctor prescribed X — what should I know about it?"
- "What does this lab result mean?"
- "My child has a rash — what could it be?"
- "I read online that Y causes Z — is that true?"

They need:
- **Clarity** — Plain language explanations, not medical jargon
- **Context** — Help understanding what's normal vs. concerning
- **Guidance** — When to self-manage vs. seek professional care
- **Trust** — Honest acknowledgment of uncertainty

### What Users Don't Need (But Might Ask For)

- Diagnoses ("You have condition X")
- Treatment plans ("Take medication Y")
- Reassurance without basis ("Don't worry, it's nothing")
- Medical advice that substitutes for professional care

---

## Stakeholder Map

Understanding who has stakes in this system helps you make design decisions.

### Primary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Users** | Clear, helpful health information | Being misled, false reassurance |
| **Healthcare providers** | Patients who are informed, not misinformed | System undermining professional advice |
| **Nonprofit (operator)** | Effective tool that serves mission | Liability, reputational risk, sustainability |

### Secondary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Regulators** | Compliance with health information guidelines | Unapproved medical device claims |
| **Public health** | Better health outcomes | Misinformation spreading |
| **Caregivers** | Support in helping loved ones | Being given advice beyond their capacity |

### Adversarial Stakeholders

| Stakeholder | Behaviour | Risk |
|:------------|:----------|:-----|
| **Health anxiety** | Users seeking reassurance repeatedly | System enables avoidance of care |
| **Self-harmers** | Users seeking information for harm | System provides dangerous information |
| **Misinformation** | Users seeking validation of false beliefs | System legitimises misinformation |

---

## Constraints

### Hard Constraints (Non-Negotiable)

These are absolute boundaries. The system must never:

| Constraint | Rationale |
|:-----------|:----------|
| Provide specific diagnoses | Diagnosis requires examination, history, tests |
| Prescribe or recommend specific treatments | Treatment decisions require professional judgment |
| Discourage seeking professional care | Must never delay necessary treatment |
| Provide information for self-harm | Ethical and legal requirement |
| Claim to be a medical professional | Deception causes harm |

### Soft Constraints (Strong Defaults)

These should be followed unless there's explicit justification:

| Constraint | Rationale |
|:-----------|:----------|
| Recommend professional consultation when uncertain | Err on side of caution |
| Cite sources for medical claims | Transparency and verifiability |
| Acknowledge limitations explicitly | Honest about what system can't do |
| Use plain language | Accessibility for all users |

### Resource Constraints

| Constraint | Impact |
|:-----------|:-------|
| Inference cost ceiling | Limits model size, call frequency |
| Response latency targets | Users expect conversational speed |
| Storage limitations | Affects conversation history, caching |

---

## Success Criteria

How do you know if this system is working?

### Safety Metrics (Must Pass)

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| Dangerous advice rate | 0% | Red team evaluation |
| Escalation accuracy | >95% | Does it recommend care when needed? |
| Boundary violations | 0% | Does it stay within scope? |

### Helpfulness Metrics (Optimise)

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| User understanding | >80% | Post-interaction survey |
| Appropriate care-seeking | Increase | Longitudinal tracking |
| Information accuracy | >95% | Expert evaluation |

### Calibration Metrics (Monitor)

| Metric | Target | Measurement |
|:-------|:-------|:------------|
| Confidence calibration | Close to diagonal | Calibration curves |
| Uncertainty acknowledgment | When appropriate | Qualitative review |

---

## Failure Modes

Understanding how this system could fail helps you prevent failures.

### High-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **False reassurance** | "That's probably nothing" for serious symptoms | Delayed treatment, harm |
| **False alarm** | "Go to ER immediately" for minor issues | Anxiety, unnecessary costs, system distrust |
| **Harmful information** | Dosage info that could cause overdose | Direct physical harm |
| **Scope creep** | Acting as therapist, diagnostician | Harm from unqualified advice |

### Medium-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Confidently wrong** | Stating incorrect information with certainty | Misinformation spread |
| **Unhelpful hedging** | "I can't help with any health questions" | System useless |
| **Inaccessible language** | Medical jargon without explanation | Fails accessibility goal |

### Low-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Inconsistency** | Different answers to same question | Confusion, reduced trust |
| **Verbosity** | Long responses when brief would suffice | Poor user experience |

---

## Scoping Decisions

Given constraints and failure modes, what should this system do?

### In Scope

| Capability | Example |
|:-----------|:--------|
| Symptom information | "Headaches can have many causes, including..." |
| General health education | "Here's how blood pressure is measured..." |
| Care navigation | "This sounds like something to discuss with your doctor" |
| Source synthesis | "According to NHS guidelines..." |
| Uncertainty expression | "I'm not certain, but..." |

### Out of Scope

| Capability | Why |
|:-----------|:----|
| Diagnosis | Requires professional examination |
| Treatment recommendations | Requires professional judgment |
| Mental health crisis intervention | Requires specialised training |
| Medication interactions | Requires complete medication history |
| Paediatric emergencies | Stakes too high, defer to professionals |

### Grey Areas (Requires Judgment)

| Capability | Considerations |
|:-----------|:---------------|
| Medication information | General info OK, specific advice not |
| Lab result interpretation | Context without diagnosis |
| Symptom urgency assessment | "Consider seeking care" vs. "Go to ER" |

---

## Your Task

Before proceeding to the next section, document your analysis:

### Exercise 1: Stakeholder Analysis

For each stakeholder group, write:
1. What they most need from this system
2. What harm could come to them from system failure
3. How you'll design for their needs

### Exercise 2: Failure Mode Prioritisation

Rank the failure modes by:
1. Probability (how likely is this to happen?)
2. Severity (how bad is it if it happens?)
3. Detectability (how would you know it happened?)

Use this to prioritise your safety work.

### Exercise 3: Scope Boundaries

For each "Grey Area" capability:
1. Where would you draw the line?
2. What would trigger escalation to professional care?
3. How would you communicate the boundary to users?

Document your reasoning. These decisions will guide your architecture.

---

## Reflection Questions

Before moving on:

- What surprised you in this analysis?
- Where do you feel most uncertain?
- What would you want to know that isn't here?
- How does this compare to other AI systems you've built?

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Project Overview](README.md) | [All Sections](#project-structure) | [Safety Architecture →](02_safety_architecture.md) |
