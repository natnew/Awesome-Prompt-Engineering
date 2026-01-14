# Incident Communication Template

## Overview

**Purpose:** Provide consistent, clear status updates during incidents for different audiences.

**When to use:** Active incidents requiring stakeholder communication.

**Competencies:** [Governance & Defensibility](../../COMPETENCIES.md#4-governance--defensibility)

---

# Incident Communication Templates

## Quick Reference: Update Frequency

| Severity | Update Frequency |
|:---------|:-----------------|
| SEV1 | Every 15 minutes |
| SEV2 | Every 30 minutes |
| SEV3 | Every 60 minutes |
| SEV4 | As needed |

---

## Template 1: Internal Team (Slack/Teams)

Use for: Engineering team, on-call channel

```
🔴/🟠/🟡 [SEV-X] [Brief Title]

Status: Investigating / Identified / Mitigating / Monitoring / Resolved
Duration: [X minutes/hours]
IC: @[name]

Impact: [Who/what is affected]

Current Action: [What we're doing right now]

ETA: [If known, otherwise "Investigating"]

Next update: [Time]

Thread for discussion 👇
```

### Example

```
🔴 [SEV1] API Error Rate Spike

Status: Mitigating
Duration: 45 minutes
IC: @alice

Impact: ~30% of API requests failing. Customer-facing features degraded.

Current Action: Rolling back deployment v2.3.1 which introduced regression.

ETA: Rollback completing in ~10 minutes. Monitoring for 15 min after.

Next update: 14:45 UTC

Thread for discussion 👇
```

---

## Template 2: Engineering Update

Use for: Broader engineering org, technical stakeholders

```markdown
# Incident Update: [INC-XXXX]

**Severity:** SEV-X
**Status:** [Status]
**Duration:** [X hours Y minutes]
**Commander:** [Name]

## Summary
[2-3 sentences on what's happening]

## Impact
- Services affected: [List]
- Users affected: [Number/percentage]
- Error rate: [Current vs normal]

## Technical Details
[What we know about the cause]

## Actions Taken
1. [Action 1]
2. [Action 2]

## Current Focus
[What we're doing now]

## Next Steps
[What comes next]

---
Next update: [Time]
Incident channel: #[channel]
```

---

## Template 3: Leadership Update

Use for: Executives, non-technical leadership

```
Subject: [SEV-X] Incident Update: [Title]

SITUATION
[One paragraph: What's happening, business impact]

IMPACT
• Customers affected: [Number/scope]
• Duration so far: [Time]
• Business impact: [Revenue/reputation/compliance if applicable]

ACTIONS
• [What we're doing]
• Team engaged: [Who's working on it]

TIMELINE
• Detected: [Time]
• Expected resolution: [Estimate or "Under investigation"]

NEXT UPDATE
[Time]

Questions? Contact: [IC name and contact]
```

### Example

```
Subject: [SEV1] Incident Update: Payment Processing Degraded

SITUATION
We are experiencing elevated failures in payment processing, affecting approximately 15% of checkout attempts. Engineering is actively working on resolution. A rollback of recent changes is in progress.

IMPACT
• Customers affected: ~2,000 transactions impacted
• Duration so far: 45 minutes
• Business impact: Estimated $50K in delayed transactions (recoverable once resolved)

ACTIONS
• Root cause identified as database connection issue from recent deployment
• Rollback in progress, expected complete in 10 minutes
• Customer support briefed and handling inquiries

TIMELINE
• Detected: 13:30 UTC
• Expected resolution: Within 30 minutes

NEXT UPDATE
14:15 UTC

Questions? Contact: Alice Smith (Incident Commander) - @alice / 555-0123
```

---

## Template 4: Customer Communication

Use for: Status page, customer emails, support scripts

### Initial Notice

```
[Service] - Investigating Issues

We are aware of an issue affecting [service/feature]. Some users may experience [symptom - e.g., "errors when accessing their dashboard"].

Our team is investigating and we will provide an update shortly.

We apologize for any inconvenience.

Posted: [Time] UTC
```

### Update - Identified

```
[Service] - Issue Identified

We have identified the cause of the [service/feature] issues and are implementing a fix.

During this time, you may continue to experience [symptom].

We expect to have an update within [time frame].

We apologize for the disruption.

Updated: [Time] UTC
```

### Update - Monitoring

```
[Service] - Fix Implemented

We have implemented a fix for the [service/feature] issues. We are monitoring the results.

Most users should now be able to [normal behavior]. If you continue to experience issues, please try [action - e.g., "refreshing your browser"].

We will provide a final update once we confirm the issue is fully resolved.

Updated: [Time] UTC
```

### Resolution

```
[Service] - Resolved

The issue affecting [service/feature] has been resolved. All systems are operating normally.

Between [start time] and [end time] UTC, some users experienced [symptom]. This was caused by [brief, non-technical explanation].

We apologize for any inconvenience this caused. If you have any questions, please contact support.

Resolved: [Time] UTC
```

---

## Template 5: Support Team Brief

Use for: Customer support team during active incidents

```markdown
# Support Brief: [INC-XXXX]

**DO NOT SHARE THIS DOCUMENT WITH CUSTOMERS**

## Quick Facts
- Issue: [What's broken]
- Status: [Current status]
- ETA: [Best estimate]
- Severity: SEV-X

## Customer Impact
[What customers are experiencing]

## Approved Customer Message
[Copy of status page message they can share]

## FAQs

**Q: When will this be fixed?**
A: [Approved answer - be careful with promises]

**Q: Why is this happening?**
A: [Simple, non-technical explanation]

**Q: Is my data safe?**
A: [Answer - typically "Yes, this does not affect data security"]

**Q: Will I be compensated?**
A: [Answer - typically "Please contact your account manager for SLA discussions after resolution"]

## Do NOT Say
- Specific timelines not in this brief
- Technical details about root cause
- Speculation about cause
- Anything about other customers

## Escalation
- For urgent customer issues: [Contact]
- For questions about this brief: [Contact]

## Updates
This brief will be updated every [frequency].
Last update: [Time]
```

---

## Template 6: Post-Incident Customer Notice

Use for: Customer communication after resolution

```
Subject: Resolved: [Service] Issue on [Date]

Dear [Customer],

We wanted to follow up regarding the service disruption that occurred on [date].

WHAT HAPPENED
Between [start time] and [end time] UTC, [description of impact]. This affected [scope of impact].

ROOT CAUSE
[Brief, non-technical explanation]

WHAT WE'RE DOING
To prevent this from happening again, we are:
• [Action 1]
• [Action 2]

We sincerely apologize for any inconvenience this caused. We take reliability seriously and are committed to providing you with dependable service.

If you have any questions or concerns, please don't hesitate to reach out to [contact].

Thank you for your patience and understanding.

[Signature]
```

---

## Communication Checklist

### Before Sending

- [ ] Accurate information?
- [ ] Appropriate audience?
- [ ] No blame/finger-pointing?
- [ ] No technical jargon (for non-technical audiences)?
- [ ] Clear next update time?
- [ ] Contact information included?
- [ ] Proofread?

### Channels to Update

| Audience | Channel | Who Updates |
|:---------|:--------|:------------|
| Engineering | Slack #incidents | IC |
| Leadership | Email | IC |
| Customers | Status page | Comms lead |
| Support | Internal brief | Support lead |

---

*Template version: 1.0*  
*Last updated: [Date]*
