[← Back: Response](03_response.md) | [Next: Recovery →](05_recovery.md)

# Module 4: Communication

Who needs to know, and what do you tell them?

---

## Communication Audiences

| Audience | What They Need | When to Tell |
|:---------|:---------------|:-------------|
| **Responders** | Technical details, access | Immediately |
| **Leadership** | Business impact, ETA | Early, updates |
| **Customers** | Status, workarounds | Public acknowledgment |
| **Legal/Compliance** | Facts, risks | If security/data issue |
| **Support team** | What to tell users | Before users ask |

---

## Communication Timing

```
INCIDENT TIMELINE
─────────────────────────────────────────────────────▶

Detection          Mid-incident        Resolution
    │                   │                   │
    ▼                   ▼                   ▼
┌─────────┐       ┌─────────┐       ┌─────────┐
│"We're   │       │"Still   │       │"Issue   │
│aware of │       │working  │       │resolved"│
│an issue"│       │on it"   │       │         │
└─────────┘       └─────────┘       └─────────┘
```

### Initial (< 15 min)

- Acknowledge internally
- Begin stakeholder notification
- Post to status page if user-impacting

### During (every 15-30 min for SEV1/2)

- Update status
- Share new findings
- Revise ETA if needed

### Resolution

- Confirm resolution
- Share what happened (high level)
- Communicate next steps

### Post-incident

- Detailed summary
- Root cause analysis
- Preventive measures

---

## Communication Templates

### Internal: Incident Declaration

```
🚨 [SEV2] AI Feature Incident

Status: Investigating
Impact: AI-powered search returning incorrect results
Started: [TIME]
Responders: [NAMES]

Current actions:
- Reviewing recent deployments
- Analyzing error logs

Next update: [TIME + 30 min]

Incident channel: #incident-[NUMBER]
```

### Status Page: Initial

```
Investigating issues with AI-powered features

We are investigating reports of issues with our AI-powered 
search feature. Some users may experience incorrect or 
delayed results.

We are working to resolve this as quickly as possible. 
Updates will be posted here.

Posted: [TIME]
```

### Customer Communication

```
Subject: Update on [Product] AI Feature

Dear [Customer],

We experienced an issue with our AI-powered [feature] on 
[DATE] from [TIME] to [TIME] [TIMEZONE].

What happened: [Brief, non-technical explanation]

Impact to you: [Specific impact]

What we're doing: [Actions taken and preventive measures]

We apologize for any inconvenience this may have caused.

If you have questions, please contact [support].

[Signature]
```

---

## Communication Principles

### Principle 1: Acknowledge Early

Even if you don't know what's wrong, say you're aware.

**Don't:** Wait until you have all the answers
**Do:** "We're aware of an issue and investigating"

### Principle 2: Be Honest About Uncertainty

**Don't:** "Will be fixed in 30 minutes" (if you don't know)
**Do:** "Currently investigating. Next update in 30 minutes."

### Principle 3: Technical Inside, Simple Outside

**Internal:** "Redis cluster failover caused connection pool exhaustion"
**External:** "We experienced a technical issue with our systems"

### Principle 4: Follow Up After Resolution

Don't just say "fixed." Explain what happened and what you're doing to prevent it.

---

## Your Task

Prepare communication templates for:

1. **Internal notification** — Declaring an incident
2. **Status page updates** — Initial, update, resolution
3. **Customer communication** — For significant incidents
4. **Post-incident summary** — What happened, why, prevention

---

[← Back: Response](03_response.md) | [Next: Recovery →](05_recovery.md)
