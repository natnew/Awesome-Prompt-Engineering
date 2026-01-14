[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Problem Framing](01_problem_framing.md) | [Agent Design →](03_agent_design.md)

# Safety Architecture

Design the safety mechanisms that ensure this system helps without harming.

---

## The Safety Mental Model

Think of safety architecture as **defense in depth** — multiple independent layers, each capable of preventing harm even if other layers fail.

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: Input Filtering                                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Layer 2: Scope Enforcement                               │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │  Layer 3: Output Validation                         │  │  │
│  │  │  ┌───────────────────────────────────────────────┐  │  │  │
│  │  │  │  Layer 4: Human Escalation                    │  │  │  │
│  │  │  │  ┌─────────────────────────────────────────┐  │  │  │  │
│  │  │  │  │  Layer 5: Audit & Monitoring            │  │  │  │  │
│  │  │  │  │                                         │  │  │  │  │
│  │  │  │  │         Core Reasoning                  │  │  │  │  │
│  │  │  │  │                                         │  │  │  │  │
│  │  │  │  └─────────────────────────────────────────┘  │  │  │  │
│  │  │  └───────────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

Each layer operates independently. A failure at one layer should be caught by another.

---

## Layer 1: Input Filtering

### Purpose
Detect and handle dangerous or out-of-scope queries before they reach the reasoning system.

### Hard Stops

These inputs should never proceed to reasoning:

| Pattern | Detection | Response |
|:--------|:----------|:---------|
| Self-harm ideation | Keyword + semantic analysis | Crisis resource redirect |
| Harm to others | Intent classification | Decline + appropriate response |
| Illegal activity | Pattern matching | Decline clearly |
| Explicit diagnosis requests | Intent classification | Redirect to scope |

### Soft Redirects

These inputs should be acknowledged and redirected:

| Pattern | Detection | Response |
|:--------|:----------|:---------|
| Emergency symptoms | Urgency classification | "This sounds urgent — please seek immediate care" |
| Mental health crisis | Distress signals | Warm handoff to crisis resources |
| Paediatric emergencies | Age + urgency | Direct to professional care immediately |

### Implementation Approach

```
Input → Classifier Pipeline → Route Decision

Classifier Pipeline:
  ├── Toxicity filter (hard stop)
  ├── Self-harm detector (crisis redirect)
  ├── Emergency detector (urgency response)
  ├── Scope classifier (in/out of scope)
  └── Intent classifier (what are they asking?)

Route Decision:
  ├── BLOCK → Safety response
  ├── REDIRECT → Appropriate resource
  ├── ESCALATE → Professional care guidance
  └── PROCEED → Continue to reasoning
```

### Your Task: Input Filter Design

Design your input filtering system:

1. **What classifiers do you need?**
   - List each classifier and its purpose
   - Define the classes/labels for each
   - Specify the action for each class

2. **How will you handle edge cases?**
   - What if classifiers disagree?
   - What's the default when uncertain?
   - How do you avoid over-blocking?

3. **What's your false positive strategy?**
   - How do you handle legitimate queries that look dangerous?
   - What's the user experience for false positives?

---

## Layer 2: Scope Enforcement

### Purpose
Ensure the system only operates within its defined capabilities, refusing gracefully when asked to exceed them.

### Scope Boundaries

| In Scope | Out of Scope | Why |
|:---------|:-------------|:----|
| General symptom information | Specific diagnosis | Diagnosis requires examination |
| Health education | Treatment recommendations | Treatment requires professional judgment |
| Care navigation | Prescription advice | Legal and safety requirement |
| Source synthesis | Mental health therapy | Requires specialised training |

### Enforcement Mechanisms

**Prompt-level enforcement:**
System prompts that clearly define scope and instruct refusal patterns.

**Runtime validation:**
Check outputs against scope definitions before delivery.

**Graceful degradation:**
When scope is exceeded, provide useful alternatives rather than hard stops.

### Example Scope Enforcement

```
User: "What antibiotic should I take for my infection?"

❌ Bad response (out of scope):
"For a bacterial infection, common antibiotics include amoxicillin..."

✓ Good response (scope-aware):
"I can't recommend specific antibiotics — that requires a doctor who can 
examine you, understand your full medical history, and consider factors 
like allergies and drug interactions.

What I can help with:
- Understanding what antibiotics are and how they work
- Questions to ask your doctor about antibiotic treatment
- General information about antibiotic resistance

Would any of these be helpful?"
```

### Your Task: Scope Definition

Create a detailed scope specification:

1. **Explicit inclusions**
   - What can this system do?
   - With what confidence level?
   - Under what conditions?

2. **Explicit exclusions**
   - What will this system never do?
   - What's the rationale for each exclusion?
   - How will exclusions be communicated?

3. **Boundary cases**
   - Where are the grey areas?
   - What decision rules apply?
   - Who decides ambiguous cases?

---

## Layer 3: Output Validation

### Purpose
Validate every output before delivery to catch safety issues that slip through earlier layers.

### Validation Checks

| Check | Purpose | Action on Failure |
|:------|:--------|:------------------|
| Diagnosis detection | Catch accidental diagnoses | Block + rephrase |
| Treatment detection | Catch treatment recommendations | Block + redirect |
| Confidence calibration | Ensure uncertainty is expressed | Add hedging |
| Source verification | Ensure claims are sourced | Add citations or hedge |
| Harm potential | Assess if output could cause harm | Block + escalate |

### Implementation Pattern

```python
def validate_output(response: str, context: dict) -> ValidationResult:
    """
    Validate output against safety criteria.
    Returns validated response or escalation.
    """
    checks = [
        DiagnosisDetector(),
        TreatmentDetector(),
        ConfidenceCalibrator(),
        SourceVerifier(),
        HarmAssessor(),
    ]
    
    for check in checks:
        result = check.validate(response, context)
        if result.action == "BLOCK":
            return generate_safe_alternative(response, result.reason)
        if result.action == "MODIFY":
            response = result.modified_response
    
    return ValidationResult(response=response, status="APPROVED")
```

### Your Task: Validation Suite

Design your output validation:

1. **What checks do you need?**
   - List each validation check
   - Define what it detects
   - Specify the action on detection

2. **How do you handle false positives?**
   - Legitimate content flagged as dangerous
   - Impact on user experience

3. **What's the performance impact?**
   - Latency budget for validation
   - Trade-offs between thoroughness and speed

---

## Layer 4: Human Escalation

### Purpose
Recognise when the system should defer to human professionals and guide users appropriately.

### Escalation Triggers

#### Immediate Escalation (Urgent)

These require immediate guidance to seek professional care:

| Trigger | Detection | Response |
|:--------|:----------|:---------|
| Emergency symptoms | Chest pain, difficulty breathing, etc. | "Please seek emergency care immediately" |
| Suicidal ideation | Direct statements, crisis signals | Crisis resource + warm handoff |
| Child in danger | Paediatric emergency indicators | Direct to emergency services |

#### Recommended Escalation (Soon)

These suggest professional consultation:

| Trigger | Detection | Response |
|:--------|:----------|:---------|
| Persistent symptoms | Duration indicators | "This has been going on long enough to warrant a doctor visit" |
| Multiple systems | Symptom complexity | "Several things going on — best to get a professional assessment" |
| User uncertainty | Expressed anxiety | "It sounds like you'd feel better getting this checked out" |

#### Optional Escalation (Consider)

These offer professional consultation as an option:

| Trigger | Detection | Response |
|:--------|:----------|:---------|
| General health questions | Broad scope | "A doctor could give you personalised advice" |
| Lifestyle factors | Ongoing concerns | "Worth discussing at your next checkup" |

### Escalation Communication

**Principle:** Escalation should feel like support, not abandonment.

```
❌ Bad escalation:
"I can't help with that. See a doctor."

✓ Good escalation:
"This sounds like something that would really benefit from a doctor's 
assessment. They can examine you, run tests if needed, and give you 
personalised advice that I'm not able to provide.

In the meantime, here's some general information that might be helpful...

Would you like help thinking through what to tell your doctor?"
```

### Your Task: Escalation Protocol

Design your escalation system:

1. **Escalation tiers**
   - Define your escalation levels
   - What triggers each level?
   - What's the response for each?

2. **Communication templates**
   - How do you communicate escalation warmly?
   - How do you avoid abandonment feeling?
   - How do you maintain helpfulness within bounds?

3. **Resource connections**
   - What resources do you direct users to?
   - How do you handle geographic variation?
   - How do you handle after-hours queries?

---

## Layer 5: Audit & Monitoring

### Purpose
Maintain complete records for accountability, learning, and incident response.

### Audit Requirements

| Data Point | Purpose | Retention |
|:-----------|:--------|:----------|
| Full conversation | Investigation, training | [Define policy] |
| Safety decisions | Understanding system behaviour | Permanent |
| Escalation events | Quality assurance | Permanent |
| User feedback | Continuous improvement | [Define policy] |

### Monitoring Dashboards

| Metric | Purpose | Alert Threshold |
|:-------|:--------|:----------------|
| Escalation rate | Detect scope issues | Deviation from baseline |
| Safety trigger rate | Detect attack patterns | Spike detection |
| User satisfaction | Detect helpfulness issues | Drop below threshold |
| Response time | Detect performance issues | Above latency target |

### Incident Response

When something goes wrong:

```
Detection → Assessment → Response → Review → Improvement

Detection:
  - User report
  - Monitoring alert
  - External report

Assessment:
  - Severity classification
  - Impact scope
  - Root cause hypothesis

Response:
  - Immediate mitigation
  - User communication
  - Stakeholder notification

Review:
  - Root cause analysis
  - Systemic factors
  - Prevention opportunities

Improvement:
  - System updates
  - Process changes
  - Documentation updates
```

### Your Task: Audit System Design

Design your audit and monitoring:

1. **What do you log?**
   - Every interaction? Samples? Safety events only?
   - What's the privacy trade-off?
   - What's the storage cost?

2. **What do you monitor?**
   - Real-time metrics
   - Alert thresholds
   - Escalation procedures

3. **Incident response plan**
   - Who's responsible?
   - What's the response timeline?
   - How do you communicate with users?

---

## Putting It Together

### Safety Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                           User Query                                │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 1: Input Filtering                                           │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │   Toxicity  │ │  Self-harm  │ │  Emergency  │ │    Scope    │   │
│  │   Filter    │ │  Detector   │ │  Detector   │ │  Classifier │   │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘   │
│         │               │               │               │           │
│         └───────────────┴───────────────┴───────────────┘           │
│                                  │                                   │
│                    ┌─────────────┴─────────────┐                    │
│                    │      Route Decision       │                    │
│                    └─────────────┬─────────────┘                    │
└──────────────────────────────────┼──────────────────────────────────┘
                     │             │             │
              ┌──────┘             │             └──────┐
              ▼                    ▼                    ▼
        ┌──────────┐        ┌──────────┐        ┌──────────┐
        │  BLOCK   │        │ REDIRECT │        │ PROCEED  │
        │ Response │        │ Response │        │          │
        └──────────┘        └──────────┘        └────┬─────┘
                                                     │
                                                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 2: Scope Enforcement                                         │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              System Prompt Scope Definition                  │   │
│  │              Runtime Scope Validation                        │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  CORE REASONING (Multi-Agent System)                                │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │   Intake    │ │  Reasoning  │ │  Literature │ │  Synthesis  │   │
│  │   Agent     │→│   Agent     │→│   Agent     │→│   Agent     │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 3: Output Validation                                         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │  Diagnosis  │ │  Treatment  │ │ Confidence  │ │    Harm     │   │
│  │  Detector   │ │  Detector   │ │ Calibrator  │ │  Assessor   │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │   Escalation Required?    │
                    └─────────────┬─────────────┘
                     │                         │
              ┌──────┘                         └──────┐
              ▼                                       ▼
┌─────────────────────────┐             ┌─────────────────────────┐
│  LAYER 4: Escalation    │             │   Deliver Response      │
│  Professional referral  │             │                         │
│  Crisis resources       │             │                         │
│  Warm handoff           │             │                         │
└─────────────────────────┘             └─────────────────────────┘
              │                                       │
              └───────────────────┬───────────────────┘
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 5: Audit & Monitoring                                        │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │  Logging    │ │  Metrics    │ │   Alerts    │ │  Incident   │   │
│  │             │ │             │ │             │ │  Response   │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Deliverables

By the end of this section, you should have:

| Deliverable | Description |
|:------------|:------------|
| **Safety specification** | Formal document defining all safety constraints |
| **Input filter design** | Classifiers, routes, responses |
| **Scope definition** | In/out/grey areas with rationale |
| **Validation suite** | Output checks and actions |
| **Escalation protocol** | Triggers, tiers, communication |
| **Audit design** | Logging, monitoring, incident response |

Use the templates in `artifacts/` to document each.

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Problem Framing](01_problem_framing.md) | [Project Overview](README.md) | [Agent Design →](03_agent_design.md) |
