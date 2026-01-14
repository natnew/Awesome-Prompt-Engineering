# Incident Response Plan

## Purpose

This document defines how the team responds when something goes wrong with the Health Reasoning Agent.

---

## Incident Classification

### Severity Levels

| Level | Definition | Examples | Response Time |
|:------|:-----------|:---------|:--------------|
| **SEV-1 Critical** | Immediate risk of harm | Dangerous medical advice given, safety system bypassed | Immediate |
| **SEV-2 High** | Significant issue, potential harm | Missed emergency escalation, repeated misinformation | <1 hour |
| **SEV-3 Medium** | Quality issue, no immediate harm | Poor uncertainty expression, unhelpful responses | <24 hours |
| **SEV-4 Low** | Minor issue | Verbose responses, minor tone issues | Next sprint |

### Classification Decision Tree

```
Is there evidence of direct harm or imminent risk?
├── Yes → SEV-1 Critical
└── No → Could this cause harm if repeated?
         ├── Yes → SEV-2 High
         └── No → Does this affect core functionality?
                  ├── Yes → SEV-3 Medium
                  └── No → SEV-4 Low
```

---

## Incident Response Workflow

### Phase 1: Detection

| Detection Source | Notification Method | Time to Acknowledge |
|:-----------------|:--------------------|:--------------------|
| Automated monitoring | PagerDuty alert | <5 minutes |
| User report | Support channel | <30 minutes |
| Internal discovery | Slack #incidents | <1 hour |
| External report | Email/social | <2 hours |

### Phase 2: Triage

**Triage checklist:**

- [ ] Classify severity (SEV-1 to SEV-4)
- [ ] Identify affected scope (users, conversations, time range)
- [ ] Assess ongoing risk (is harm continuing?)
- [ ] Assign incident commander
- [ ] Create incident channel (for SEV-1/2)

### Phase 3: Response

#### SEV-1 Critical Response

| Time | Action | Owner |
|:-----|:-------|:------|
| 0 min | Page on-call engineer | Automated |
| 5 min | Incident commander assigned | On-call |
| 15 min | Initial assessment complete | IC |
| 30 min | Mitigation deployed or escalated | Team |
| 1 hour | Stakeholders notified | IC |
| 4 hours | Root cause hypothesis | Team |
| 24 hours | Preliminary post-mortem | IC |

#### SEV-2 High Response

| Time | Action | Owner |
|:-----|:-------|:------|
| 0 min | Slack notification | Automated |
| 30 min | Owner assigned | Team lead |
| 2 hours | Investigation complete | Owner |
| 4 hours | Fix deployed or workaround | Owner |
| 48 hours | Post-mortem complete | Owner |

#### SEV-3/4 Response

| Time | Action | Owner |
|:-----|:-------|:------|
| 0 min | Ticket created | Reporter |
| 24 hours | Owner assigned | Team lead |
| Sprint | Fix planned | Owner |
| Next release | Fix deployed | Owner |

### Phase 4: Resolution

**Resolution checklist:**

- [ ] Root cause identified
- [ ] Fix deployed and verified
- [ ] Affected users notified (if applicable)
- [ ] Monitoring confirms resolution
- [ ] Incident closed

### Phase 5: Post-Mortem

**Required for:** All SEV-1 and SEV-2 incidents

**Post-mortem template:**
```
## Incident Summary
[One paragraph description]

## Timeline
[Chronological events]

## Impact
- Users affected: [N]
- Duration: [Time]
- Harm assessment: [Description]

## Root Cause
[What actually went wrong]

## Contributing Factors
[What made this possible/worse]

## What Went Well
[Effective response elements]

## What Went Poorly
[Response issues]

## Action Items
| Action | Owner | Deadline |
|--------|-------|----------|
| | | |

## Lessons Learned
[Key takeaways]
```

---

## Specific Response Procedures

### Procedure: Dangerous Medical Advice Given

**Classification:** SEV-1 Critical

**Immediate actions:**
1. Disable affected model/configuration immediately
2. Review conversation logs for scope
3. Assess if user may have acted on advice
4. Prepare user communication if needed

**Communication template:**
```
We identified an issue with a response you received from our health 
assistant. [Specific issue].

We want to make sure you have accurate information: [Correction].

If you have concerns or took action based on this information, please 
consult with a healthcare professional.

We apologize for any concern this may have caused.
```

### Procedure: Missed Emergency Escalation

**Classification:** SEV-1 Critical

**Immediate actions:**
1. Review detection system logs
2. Identify false negative patterns
3. Lower escalation thresholds pending investigation
4. Review similar recent conversations

### Procedure: Safety System Bypass

**Classification:** SEV-1 Critical

**Immediate actions:**
1. Document exact bypass method
2. Patch immediately if possible
3. If unpatchable, consider service suspension
4. Red team for similar vulnerabilities

### Procedure: Misinformation Pattern

**Classification:** SEV-2 High

**Immediate actions:**
1. Identify scope (which claims, how many users)
2. Trace to source (training, retrieval, generation)
3. Correct affected outputs
4. Update evaluation tests to catch pattern

---

## Roles and Responsibilities

### Incident Commander (IC)

**Responsibilities:**
- Overall coordination
- Decision authority
- Stakeholder communication
- Timeline management

**Authority:**
- Can page any team member
- Can authorise emergency changes
- Can escalate to leadership

### Technical Lead

**Responsibilities:**
- Technical investigation
- Fix development
- System assessment

### Communications Lead

**Responsibilities:**
- User notification drafts
- Stakeholder updates
- Public communication (if needed)

### Clinical Advisor (for health-related incidents)

**Responsibilities:**
- Assess medical accuracy issues
- Advise on user communication
- Review corrections

---

## Communication Templates

### Internal Escalation (SEV-1)

```
🚨 SEV-1 INCIDENT: [Brief description]

Incident Commander: [Name]
Channel: #incident-[date]-[number]

Impact: [Scope and severity]
Current status: [What's happening now]

Needed: [Specific help needed]

DO NOT discuss in other channels.
```

### Stakeholder Update

```
INCIDENT UPDATE: [Time]

Status: [Active/Monitoring/Resolved]
Severity: [SEV-X]
Duration: [Time since start]

Current situation: [Brief description]

Actions taken: [What we've done]

Next steps: [What's happening next]

Next update: [When]
```

### User Notification (if needed)

```
Subject: Important information about your recent conversation

[Warm opening]

[Specific issue and correction]

[What we're doing about it]

[Resources if they have concerns]

[Apology]

[Contact information]
```

---

## Escalation Contacts

| Role | Primary | Secondary | Escalation Method |
|:-----|:--------|:----------|:------------------|
| On-call engineer | [Name] | [Name] | PagerDuty |
| Engineering lead | [Name] | [Name] | Phone |
| Clinical advisor | [Name] | [Name] | Phone |
| Legal | [Name] | [Name] | Email + phone |
| Leadership | [Name] | [Name] | Phone |

---

## Prevention and Improvement

### After Each Incident

| Action | Timeline | Owner |
|:-------|:---------|:------|
| Post-mortem written | 48 hours | IC |
| Action items assigned | 48 hours | Team lead |
| Evaluation suite updated | 1 week | QA |
| Process improvements | 2 weeks | Team lead |

### Quarterly Review

- Incident trends
- Response time analysis
- Process effectiveness
- Training needs

---

## Training and Drills

### Required Training

| Training | Frequency | Audience |
|:---------|:----------|:---------|
| Incident response basics | On hire | All engineers |
| IC training | Quarterly | On-call rotation |
| Clinical incident response | On hire | Relevant roles |

### Drills

| Drill Type | Frequency | Participants |
|:-----------|:----------|:-------------|
| Tabletop exercise | Monthly | On-call rotation |
| Full simulation | Quarterly | Full team |

---

## Document Control

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 1.0 | [Date] | [Name] | Initial version |

**Review schedule:** Quarterly

**Owner:** [Name/Role]
