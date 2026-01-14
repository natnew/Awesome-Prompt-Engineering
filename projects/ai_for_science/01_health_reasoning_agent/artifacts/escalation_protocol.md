# Escalation Protocol

## Purpose

This document defines when and how the Health Reasoning Agent escalates users to professional healthcare resources.

---

## Escalation Philosophy

**Core principle:** When in doubt, escalate. The cost of unnecessary escalation is far lower than the cost of missed escalation.

**Escalation is not failure.** Recognising limits and connecting users with appropriate care is a core system function, not a fallback.

---

## Escalation Tiers

### Tier 1: Emergency (Immediate)

**When:** Life-threatening symptoms or situations

**Response time:** Immediate (no further questions)

**Action:** Direct to emergency services

| Trigger Category | Specific Triggers | Response |
|:-----------------|:------------------|:---------|
| Cardiac | Chest pain + arm/jaw/back radiation, crushing pressure | "Call emergency services (999/911) immediately" |
| Respiratory | Severe breathing difficulty, choking, drowning | "Call emergency services immediately" |
| Neurological | Sudden severe headache, stroke symptoms (FAST), seizure | "Call emergency services immediately" |
| Bleeding | Uncontrolled bleeding, trauma | "Call emergency services immediately" |
| Allergic | Anaphylaxis symptoms | "Call emergency services immediately" |
| Psychiatric | Active suicidal intent with plan | Crisis line + emergency services |

**Standard Emergency Response:**
```
I'm concerned about what you're describing. This sounds like it needs 
immediate medical attention.

Please call emergency services now:
- UK: 999
- US: 911
- [Regional numbers]

If you can't call, have someone nearby call for you, or go to the nearest 
emergency department.

This is not something to wait on.
```

### Tier 2: Urgent (Same Day)

**When:** Serious symptoms requiring prompt professional assessment

**Response time:** Within conversation turn

**Action:** Strong recommendation for same-day care

| Trigger Category | Specific Triggers | Response |
|:-----------------|:------------------|:---------|
| Pain | Severe pain (8-10/10) | "Please seek care today" |
| Fever | High fever (>39°C/102°F) in adults | "Please see someone today" |
| Infection signs | Spreading redness, increasing swelling, fever | "Needs assessment today" |
| [Additional] | | |

**Standard Urgent Response:**
```
What you're describing sounds like something that should be looked at today, 
not something to wait on.

Options for same-day care:
- Your GP's urgent appointment line
- Walk-in clinic or urgent care centre
- NHS 111 (UK) for guidance on nearest options

While you're waiting to be seen, [appropriate interim advice if any].

Is there anything I can help you prepare to tell the doctor?
```

### Tier 3: Soon (Within Days)

**When:** Concerning symptoms warranting professional assessment but not emergency

**Response time:** End of response

**Action:** Recommendation to schedule appointment

| Trigger Category | Specific Triggers | Response |
|:-----------------|:------------------|:---------|
| Duration | Symptoms persisting >7 days | "Worth getting checked" |
| Pattern | New or changed symptoms | "Should be assessed" |
| Risk factors | Symptoms + relevant history | "Given your history, get this looked at" |
| [Additional] | | |

**Standard Soon Response:**
```
This sounds like something worth having your doctor look at — not an 
emergency, but something that deserves professional attention.

I'd suggest booking an appointment within the next few days if possible.

In the meantime, [any appropriate self-care advice].

Would you like help thinking through what to tell your doctor?
```

### Tier 4: Consider (At Convenience)

**When:** General recommendation for professional input

**Response time:** At appropriate point in response

**Action:** Suggestion to discuss with healthcare provider

| Trigger Category | Specific Triggers | Response |
|:-----------------|:------------------|:---------|
| Checkup overdue | General health questions + no recent visit | "Good to mention at next checkup" |
| Ongoing management | Chronic condition questions | "Worth discussing with your doctor" |
| [Additional] | | |

**Standard Consider Response:**
```
This might be worth mentioning to your doctor at your next appointment — 
not urgent, but the kind of thing they'd want to know about.

In general, [relevant information that's helpful in the meantime].
```

---

## Crisis Escalation (Mental Health)

### Trigger Detection

| Signal | Detection Approach | Confidence |
|:-------|:-------------------|:-----------|
| Direct statement | "I want to end my life" | High |
| Indirect signals | Hopelessness, goodbye language | Medium |
| Self-harm mention | Any mention of self-injury | Medium |

### Response Protocol

**Never:**
- Leave the person without support resources
- Provide information that could facilitate harm
- Dismiss or minimise their feelings
- End the conversation abruptly

**Always:**
- Acknowledge their feelings
- Express genuine concern
- Provide crisis resources
- Stay supportive throughout

**Standard Crisis Response:**
```
I hear that you're going through something really difficult right now, 
and I'm concerned about you.

What you're feeling matters, and you don't have to face this alone.

Please reach out to people who specialise in supporting people through 
moments like this:

- [Country] Crisis Line: [Number]
- Crisis Text Line: Text [keyword] to [number]
- International: [Resources]

These are people trained to help, available 24/7, and the conversation 
is confidential.

I'm here to talk too, but I want to make sure you have access to the 
right support.
```

---

## Escalation Communication Guidelines

### Tone Principles

| Principle | Why | Example |
|:----------|:----|:--------|
| **Warm, not clinical** | Escalation shouldn't feel like abandonment | "I think you should..." vs "Seek medical attention" |
| **Confident, not alarming** | Concern without panic | "This needs checking" vs "This could be serious" |
| **Specific, not vague** | Actionable guidance | "Call your GP today" vs "See a doctor" |
| **Supportive throughout** | Maintain relationship | Offer to help prepare for appointment |

### What to Include

| Element | Purpose | Example |
|:--------|:--------|:--------|
| Acknowledgment | Validate their experience | "That sounds uncomfortable" |
| Rationale | Why escalation is recommended | "Symptoms lasting this long warrant..." |
| Specific action | Clear next step | "Book a GP appointment this week" |
| Interim guidance | What to do meanwhile | "Rest and stay hydrated" |
| Continued support | You're still here | "Would you like help preparing?" |

### What to Avoid

| Anti-pattern | Problem | Alternative |
|:-------------|:--------|:------------|
| "I can't help with that" | Feels like rejection | "This needs professional assessment" |
| Bare resource dump | Impersonal | Wrap resources in supportive context |
| Over-qualifying | Undermines urgency | Be direct when needed |
| Medical jargon | Accessibility | Plain language |

---

## Regional Adaptations

### UK-Specific

| Resource | When to Reference | Contact |
|:---------|:------------------|:--------|
| Emergency | Life-threatening | 999 |
| NHS 111 | Urgent, not emergency | 111 |
| GP | Routine, soon | "Your GP surgery" |
| Samaritans | Mental health crisis | 116 123 |

### US-Specific

| Resource | When to Reference | Contact |
|:---------|:------------------|:--------|
| Emergency | Life-threatening | 911 |
| Urgent care | Urgent, not emergency | "Urgent care center" |
| PCP | Routine | "Your doctor" |
| 988 | Mental health crisis | 988 |

### [Additional Regions]

[Add regional adaptations as needed]

---

## Escalation Logging

### What to Log

| Data Point | Purpose | Retention |
|:-----------|:--------|:----------|
| Trigger detected | Quality assurance | [Policy] |
| Escalation tier | Trend analysis | [Policy] |
| User response | Effectiveness assessment | [Policy] |

### Privacy Considerations

- Log escalation events, not conversation content
- Aggregate for analysis, don't identify individuals
- Comply with relevant data protection regulations

---

## Review and Update

| Trigger | Action | Responsible |
|:--------|:-------|:------------|
| Missed escalation incident | Immediate protocol review | Safety lead |
| Quarterly | Regular protocol review | Clinical advisor |
| Guideline changes | Update triggers and responses | Medical team |

---

## Sign-Off

| Role | Name | Date | Signature |
|:-----|:-----|:-----|:----------|
| System Designer | | | |
| Clinical Advisor | | | |
| Safety Lead | | | |
