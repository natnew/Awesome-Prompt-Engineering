# Incident Runbook: [System Name]

## System Overview

**System:** [Name]
**Purpose:** [Brief description]
**Owner:** [Team/person]
**On-call:** [Rotation/contact]

---

## Quick Reference

| Severity | Response Time | Who to Page |
|:---------|:--------------|:------------|
| SEV1 | Immediate | [Names] |
| SEV2 | 30 min | [Names] |
| SEV3 | 4 hr | [Names] |
| SEV4 | Next business day | [Names] |

---

## Common Incidents

### Incident Type 1: [Name]

**Symptoms:**
- [Symptom 1]
- [Symptom 2]

**Severity:** SEV[X]

**Immediate Actions:**
1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

**Investigation:**
1. Check [location] for [indicator]
2. Review [logs] for [pattern]
3. Verify [system] is [expected state]

**Resolution:**
1. [Step 1]
2. [Step 2]

**Escalate if:**
- [Condition]

---

### Incident Type 2: [Name]

**Symptoms:**
- [Symptom 1]
- [Symptom 2]

**Severity:** SEV[X]

**Immediate Actions:**
1. [ ] [Action 1]
2. [ ] [Action 2]

**Investigation:**
1. [Step 1]
2. [Step 2]

**Resolution:**
1. [Step 1]
2. [Step 2]

**Escalate if:**
- [Condition]

---

### Incident Type 3: AI Quality Degradation

**Symptoms:**
- User complaints about wrong answers
- Quality metrics below threshold
- Increased escalations

**Severity:** SEV2/3 depending on scope

**Immediate Actions:**
1. [ ] Assess scope (how many users, how wrong)
2. [ ] Decision: disable, add warnings, or monitor
3. [ ] Notify stakeholders

**Investigation:**
1. Check recent deployments
2. Review sample responses
3. Check upstream APIs (LLM, vector DB)
4. Run evaluation suite

**Resolution:**
1. If deployment issue: rollback
2. If upstream issue: failover or wait
3. If content issue: update knowledge base

**Escalate if:**
- Safety concerns
- Data exposure possible
- Business-critical function affected

---

## Escalation Paths

| Issue Type | First Contact | Escalation | Final Authority |
|:-----------|:--------------|:-----------|:----------------|
| Technical | On-call | Tech Lead | CTO |
| Security | On-call | Security Team | CISO |
| Legal/Compliance | Legal contact | General Counsel | CEO |
| Customer-facing | Support Lead | Customer Success | VP |

---

## Communication Templates

### Incident Declaration

```
🚨 [SEVERITY] Incident: [Brief description]

Status: Investigating
Impact: [Who/what is affected]
Responders: [Names]

Next update: [Time]
Channel: #incident-[number]
```

### Status Update

```
📋 Update: [Brief description]

Status: [Investigating/Mitigating/Resolving]
Current state: [What we know]
Actions taken: [What we did]
Next steps: [What's happening next]
ETA: [If known]

Next update: [Time]
```

### Resolution Notice

```
✅ Resolved: [Brief description]

Duration: [Start] to [End]
Impact: [What was affected]
Resolution: [What fixed it]

Post-mortem scheduled for: [Date/time]
```

---

## Key Contacts

| Role | Name | Contact | Backup |
|:-----|:-----|:--------|:-------|
| On-call | | | |
| Tech Lead | | | |
| Product | | | |
| Support | | | |
| Legal | | | |

---

## Useful Commands / Links

```bash
# Check system status
[command]

# View recent logs
[command]

# Restart service
[command]

# Roll back deployment
[command]
```

**Dashboards:**
- Monitoring: [URL]
- Logs: [URL]
- Metrics: [URL]

---

*Last updated: [DATE]*
*Next review: [DATE]*
