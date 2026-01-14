[← Back to Project](README.md) | [Next: Detection →](02_detection.md)

# Module 1: Incident Framework

Understand how incidents work before they happen.

---

## What Is an Incident?

An incident is an unplanned event that disrupts or threatens to disrupt normal operations.

**For AI systems, incidents include:**
- System outages or unavailability
- Quality degradation (wrong answers, hallucinations)
- Cost anomalies (unexpected spending)
- Safety failures (harmful outputs)
- Security events (data exposure, unauthorized access)
- Performance issues (unacceptable latency)

---

## Incident Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    INCIDENT LIFECYCLE                           │
│                                                                 │
│   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐       │
│   │ Detect  │──▶│ Respond │──▶│ Recover │──▶│  Learn  │       │
│   └─────────┘   └─────────┘   └─────────┘   └─────────┘       │
│                                                                 │
│   Something     Mitigate      Restore       Prevent             │
│   is wrong      impact        service       recurrence          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 1: Detect

Recognize that something is wrong.

- Automated alerts fire
- Users report issues
- Monitoring shows anomalies
- Someone notices something off

### Phase 2: Respond

Stop the bleeding.

- Assess severity
- Notify stakeholders
- Mitigate immediate impact
- Begin investigation

### Phase 3: Recover

Restore normal operation.

- Fix the immediate problem
- Verify the fix works
- Gradually restore full service
- Confirm recovery

### Phase 4: Learn

Prevent recurrence.

- Document what happened
- Identify root causes
- Create action items
- Share learnings

---

## Severity Levels

Not all incidents are equal. Classify by severity to guide response.

| Level | Definition | Example | Response Time |
|:------|:-----------|:--------|:--------------|
| **SEV1** | Critical, widespread impact | System completely down | Immediate (15 min) |
| **SEV2** | Major degradation | High error rate, security concern | Urgent (30 min) |
| **SEV3** | Partial impact | Feature broken, some users affected | Same day (4 hr) |
| **SEV4** | Minor issue | Cosmetic, workaround available | Next business day |

### AI-Specific Severity Considerations

| Incident Type | Factors That Increase Severity |
|:--------------|:-------------------------------|
| Hallucinations | High confidence, actionable, safety domain |
| Cost spike | Rate of increase, budget impact |
| Data exposure | Sensitivity, number affected |
| Quality degradation | Core functionality, user visibility |

---

## Roles in Incident Response

### Incident Commander (IC)

**Responsibilities:**
- Owns the incident end-to-end
- Makes decisions on response actions
- Coordinates responders
- Manages communication flow

**Not responsible for:**
- Doing all the technical work
- Knowing all the answers

### Subject Matter Expert (SME)

**Responsibilities:**
- Technical investigation
- Proposes solutions
- Implements fixes

### Communications Lead

**Responsibilities:**
- Internal updates
- External communication
- Status page updates
- Stakeholder management

### Scribe

**Responsibilities:**
- Document timeline
- Record decisions
- Capture action items

---

## The Incident Timeline

Every incident has a timeline. Document it.

```
TIME        EVENT
────────    ─────────────────────────────────────────
14:00       Alert: Error rate spike detected
14:05       On-call engineer acknowledges alert
14:10       Incident declared (SEV2)
14:15       Initial assessment: AI responses failing
14:20       Decision: Disable AI feature
14:25       AI feature disabled
14:30       Error rate returns to normal
14:45       Root cause identified: API key expired
15:00       Fix deployed (new API key)
15:15       AI feature re-enabled
15:30       Incident resolved
15:45       Post-mortem scheduled
```

---

## Incident Response Principles

### Principle 1: Mitigate First, Investigate Later

When something is on fire, put out the fire. Don't stop to figure out how it started.

**Order of operations:**
1. Stop the immediate harm
2. Then investigate root cause
3. Then implement permanent fix

### Principle 2: Communicate Early and Often

Silence is scary. Bad news doesn't get better with time.

**Communication cadence:**
- On detection: "We're aware of an issue"
- Every 15-30 min during SEV1/2: Status update
- On resolution: "Issue resolved" with summary
- Post-incident: Detailed post-mortem

### Principle 3: Document Everything

Memory is unreliable under stress. Write it down.

**Document:**
- What happened (facts, not interpretations)
- When it happened (timestamps)
- What you did (actions taken)
- Why you did it (reasoning)
- What you're doing next (plan)

### Principle 4: Blameless Investigation

Focus on systems and processes, not individuals.

**Not:** "Bob broke production"
**Instead:** "The deployment process allowed a broken config to reach production"

---

## AI-Specific Incident Considerations

AI systems have unique incident characteristics:

### Non-Determinism

Same input may produce different outputs. This makes:
- Reproduction harder
- Detection harder
- Verification harder

### Failure Mode: Confident but Wrong

Traditional software either works or crashes. AI can fail by being confidently wrong.

```
Traditional failure:     AI failure:
───────────────────     ──────────────────
Error: Service down     Response: "Your refund
                        has been processed."
                        (It hasn't)
```

### Upstream Dependencies

AI systems often depend on external providers:
- LLM APIs
- Embedding services
- Vector databases

You may have limited visibility into their issues.

### Evaluation Challenges

How do you know if AI responses are "correct"?
- No ground truth for many queries
- Quality is subjective
- Degradation may be gradual

---

## Your Incident Response Readiness

Before an incident happens, you need:

### Prepared Documents
- [ ] Runbooks for common scenarios
- [ ] Escalation paths and contacts
- [ ] Communication templates
- [ ] Access to systems and logs

### Prepared Processes
- [ ] How to declare an incident
- [ ] How to page on-call
- [ ] How to communicate status
- [ ] How to conduct post-mortem

### Prepared People
- [ ] On-call rotation defined
- [ ] People trained on runbooks
- [ ] Authority to make decisions
- [ ] Backup contacts identified

---

## Your Task

Before diving into detection and response:

1. **List your AI system's dependencies**
   - LLM provider(s)
   - Infrastructure
   - Data sources

2. **Identify potential failure modes**
   - What could go wrong?
   - How would you know?

3. **Map your escalation path**
   - Who gets paged first?
   - Who can approve system shutdown?
   - Who handles external communication?

---

[← Back to Project](README.md) | [Next: Detection →](02_detection.md)
