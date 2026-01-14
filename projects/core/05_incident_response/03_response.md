[← Back: Detection](02_detection.md) | [Next: Communication →](04_communication.md)

# Module 3: Response

What to do when something is wrong.

---

## The Response Sequence

```
DETECT ─▶ ASSESS ─▶ DECLARE ─▶ MITIGATE ─▶ INVESTIGATE ─▶ RESOLVE
            │
            ▼
        Severity?
        Impact?
        Urgency?
```

### Step 1: Acknowledge

Within 5 minutes of alert:
- Acknowledge the alert
- Check if it's real (not false positive)
- Begin assessment

### Step 2: Assess

Within 15 minutes:
- What's the impact?
- How many users affected?
- Is it getting worse?
- What's the severity?

### Step 3: Declare

If significant:
- Declare an incident
- Assign severity level
- Notify stakeholders
- Start incident channel/call

### Step 4: Mitigate

**STOP THE BLEEDING FIRST**

| Mitigation | When to Use |
|:-----------|:------------|
| Disable feature | AI giving harmful/wrong answers |
| Roll back | Recent change caused issue |
| Rate limit | Cost explosion |
| Failover | Infrastructure failure |
| Scale up | Capacity issues |

**Decision framework:**
```
Is the system actively causing harm?
├── YES: Disable immediately, then investigate
└── NO: Is it getting worse?
    ├── YES: Mitigate, then investigate
    └── NO: Investigate while monitoring
```

### Step 5: Investigate

Only after mitigation:
- Review logs and metrics
- Identify timeline
- Find root cause
- Develop fix

### Step 6: Resolve

- Deploy fix
- Verify fix works
- Restore service
- Confirm recovery
- Stand down incident

---

## AI-Specific Mitigation Options

| Problem | Mitigation Options |
|:--------|:-------------------|
| **Hallucinations** | Disable AI, fall back to static content/search, add disclaimers |
| **Cost explosion** | Rate limit, block expensive queries, switch to cheaper model |
| **Data leak** | Disable immediately, preserve logs, notify security |
| **Quality degradation** | Increase guardrails, add human review, roll back |
| **API failure** | Switch provider, graceful degradation, queue requests |

---

## Response Decisions

### Decision 1: Disable or Continue?

```
Disable if:
├── Active harm to users
├── Data security issue
├── Regulatory/legal concern
├── Getting worse rapidly
└── Can't monitor effectively

Continue if:
├── Impact is limited
├── Have good visibility
├── Degradation not harmful
└── Fix is being deployed
```

### Decision 2: Roll Back or Fix Forward?

```
Roll back if:
├── Recent change caused it
├── Previous version was stable
└── Can roll back quickly

Fix forward if:
├── Cause isn't recent change
├── Roll back won't help
└── Fix is faster than rollback
```

### Decision 3: Who Needs to Know?

See Module 4: Communication.

---

## Response Checklist

### On Detection

- [ ] Acknowledge alert
- [ ] Verify it's real
- [ ] Assess impact
- [ ] Check recent changes

### If Declaring Incident

- [ ] Assign severity
- [ ] Open incident channel
- [ ] Page incident commander
- [ ] Start timeline documentation

### During Response

- [ ] Mitigate immediate harm
- [ ] Communicate status (every 15-30 min)
- [ ] Investigate root cause
- [ ] Document actions taken

### On Resolution

- [ ] Verify fix works
- [ ] Restore full service
- [ ] Confirm metrics normal
- [ ] Send resolution notice
- [ ] Schedule post-mortem

---

## Your Task

Create response procedures for your AI system:

1. **Decision trees** for common incident types
2. **Mitigation options** for each failure mode
3. **Response checklist** customized to your system
4. **Escalation criteria** — when to wake people up

---

[← Back: Detection](02_detection.md) | [Next: Communication →](04_communication.md)
