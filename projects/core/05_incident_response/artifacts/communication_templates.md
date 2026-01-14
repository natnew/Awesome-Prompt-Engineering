# Incident Communication Templates

## Internal Communications

### Incident Declaration

```
🚨 [SEV2] Incident Declared: [Brief Title]

Status: Investigating
Started: [TIME] [TIMEZONE]
Impact: [Who/what is affected]

Incident Commander: [Name]
Responders: [Names]

Current understanding:
[1-2 sentences about what we know]

Actions underway:
- [Action 1]
- [Action 2]

Communication:
- Incident channel: #incident-[NUMBER]
- Next update: [TIME]

Please do not contact responders directly unless urgent.
```

### Status Update (During Incident)

```
📋 [SEV2] Update: [Brief Title]

Time: [TIME]
Status: [Investigating / Mitigating / Recovering]
Duration so far: [X hours Y minutes]

What we know:
[Brief summary of current understanding]

What we've done:
- [Action 1]
- [Action 2]

What we're doing next:
- [Next step 1]
- [Next step 2]

ETA to resolution: [Time if known / "Investigating"]

Next update: [TIME]
```

### Resolution Notice

```
✅ [SEV2] Resolved: [Brief Title]

Resolved at: [TIME]
Total duration: [X hours Y minutes]

What happened:
[2-3 sentence summary]

Impact:
- [Impact description]

Resolution:
[What fixed it]

Follow-up:
- Post-mortem scheduled: [DATE/TIME]
- Post-mortem doc: [LINK]

Thank you to everyone who helped respond.
```

---

## Status Page Messages

### Initial Acknowledgment

```
Investigating issues with [Feature/Service]

We are aware of reports of [brief issue description] and are 
actively investigating.

Some users may experience [specific symptoms].

We will provide updates as we learn more.

Posted: [TIME] [TIMEZONE]
```

### Update (Problem Identified)

```
[Feature/Service] - Issue Identified

We have identified the cause of [brief issue description].

Our team is working to resolve this issue.

[Specific workaround if available]

Next update in approximately [TIME].

Updated: [TIME] [TIMEZONE]
```

### Update (Mitigation in Progress)

```
[Feature/Service] - Fix Being Implemented

We are implementing a fix for [brief issue description].

Some users may continue to experience [symptoms] while the 
fix is rolled out.

Updated: [TIME] [TIMEZONE]
```

### Resolved

```
[Feature/Service] - Resolved

The issue affecting [feature/service] has been resolved.

Duration: [TIME] to [TIME] [TIMEZONE]

What happened: [1-2 sentence summary - keep it simple]

We apologize for any inconvenience.

Resolved: [TIME] [TIMEZONE]
```

---

## Customer Communications

### Email: Significant Incident

**Subject:** Update on [Product] service disruption

```
Dear [Customer Name],

We want to inform you about a service issue that occurred 
on [DATE].

WHAT HAPPENED
[Brief, non-technical explanation of the issue]

IMPACT TO YOU
[Specific impact - be concrete]

WHAT WE DID
[Actions taken to resolve]

WHAT WE'RE DOING TO PREVENT RECURRENCE
[High-level preventive measures]

We sincerely apologize for any inconvenience this may have 
caused you.

If you have questions or concerns, please contact us at 
[support email/link].

[Signature]
```

### Email: Data-Related Incident

**Subject:** Important security notice regarding your [Product] account

```
Dear [Customer Name],

We are writing to inform you about a security issue that 
may have affected your account.

WHAT HAPPENED
[Careful, factual description - reviewed by legal]

WHAT INFORMATION WAS INVOLVED
[Specific, factual - don't speculate]

WHAT WE ARE DOING
[Actions taken and ongoing]

WHAT YOU CAN DO
[Specific recommendations]

We take the security of your information seriously and 
sincerely apologize for this incident.

For questions, please contact [specific contact].

[Signature]
```

---

## Leadership Updates

### Executive Summary (During Major Incident)

```
INCIDENT SUMMARY: [Title]
Time: [TIME]
Severity: SEV[X]

STATUS: [Investigating / Mitigating / Recovering]

IMPACT:
- Users affected: [Number/percentage]
- Revenue impact: [If known]
- Duration: [So far]

CURRENT ACTIONS:
[1-2 sentence summary of what we're doing]

EXPECTED RESOLUTION:
[Time if known, or status]

COMMUNICATIONS:
- [Who has been notified]
- [External communications status]

NEXT UPDATE: [Time]

Questions? Contact: [Incident Commander]
```

### Executive Summary (Post-Incident)

```
INCIDENT RESOLVED: [Title]

Duration: [Start] to [End] ([Total time])
Severity: SEV[X]

SUMMARY:
[2-3 sentence summary of what happened and why]

IMPACT:
- Users affected: [Number]
- Customer complaints: [Number]
- Revenue impact: [Amount if known]

ROOT CAUSE:
[1-2 sentences - non-technical]

ACTIONS TAKEN:
[Key actions]

PREVENTION:
[Key action items]

POST-MORTEM: Scheduled for [DATE]
```

---

## Tips for Incident Communication

### Do:
- Be factual, not defensive
- Acknowledge impact on users
- Provide specific, useful information
- Set expectations for updates
- Thank people for patience/help

### Don't:
- Speculate about cause
- Blame individuals or vendors
- Promise specific resolution times unless certain
- Use technical jargon in external communications
- Forget to follow up after resolution

---

*Templates last updated: [DATE]*
