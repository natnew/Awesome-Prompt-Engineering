# On-Call Handoff Template

## Overview

**Purpose:** Ensure smooth transfer of responsibility between on-call responders.

**When to use:** Shift changes, escalations, or any transfer of incident responsibility.

**Competencies:** [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability)

---

# On-Call Handoff

**Date:** YYYY-MM-DD  
**Handoff Time:** HH:MM UTC

**From:** [Outgoing on-call name]  
**To:** [Incoming on-call name]

---

## Current System Status

| System | Status | Notes |
|:-------|:-------|:------|
| [System 1] | 🟢 Healthy / 🟡 Degraded / 🔴 Down | |
| [System 2] | 🟢 / 🟡 / 🔴 | |
| [System 3] | 🟢 / 🟡 / 🔴 | |

**Overall:** All clear / Issues in progress / Active incident

---

## Active Incidents

### [INC-XXXX]: [Title]

| Attribute | Value |
|:----------|:------|
| Severity | SEV-X |
| Status | [Current status] |
| Started | [Time] |
| IC | [Name] |
| Impact | [Brief description] |

**Current situation:**  
_[What's happening right now]_

**Actions in progress:**  
_[What's being done]_

**What incoming on-call needs to do:**  
_[Specific actions needed]_

**Key contacts:**
- [Name] - [Role] - [Contact]
- [Name] - [Role] - [Contact]

**Links:**
- Incident channel: [Link]
- Dashboard: [Link]
- Runbook: [Link]

---

## Recent Events

### Past 24 Hours

| Time | Event | Resolution/Status |
|:-----|:------|:------------------|
| HH:MM | [Event description] | [Outcome] |
| HH:MM | [Event description] | [Outcome] |
| HH:MM | [Event description] | [Outcome] |

### Alerts Fired

| Time | Alert | Action Taken |
|:-----|:------|:-------------|
| HH:MM | [Alert name] | [What was done] |
| HH:MM | [Alert name] | [What was done] |

---

## Ongoing Concerns

### Watch Items

Items that aren't incidents but warrant attention:

| Item | Concern | Action |
|:-----|:--------|:-------|
| [System/metric] | [What's concerning] | [Monitor / Investigate if X] |
| [System/metric] | [What's concerning] | [Monitor / Investigate if X] |

### Known Issues

| Issue | Impact | Workaround | Fix ETA |
|:------|:-------|:-----------|:--------|
| [Issue] | [Impact] | [Workaround] | [ETA] |

### Scheduled Changes

| Time | Change | Risk | Rollback |
|:-----|:-------|:-----|:---------|
| HH:MM | [Description] | Low/Med/High | [How to rollback] |

---

## Context for Incoming On-Call

### What's Different Today

_[Anything unusual about the current state]_

- _[Item 1]_
- _[Item 2]_

### Heads Up

_[Anything incoming on-call should know]_

- _[Item 1]_
- _[Item 2]_

### Pending Items

| Item | Status | Needs Action By |
|:-----|:-------|:----------------|
| [Item] | [Status] | [Deadline if any] |

---

## Key Resources

### Quick Links

| Resource | Link |
|:---------|:-----|
| Primary Dashboard | [URL] |
| Alerts | [URL] |
| Logs | [URL] |
| Runbooks | [URL] |
| Escalation Contacts | [URL] |

### Escalation Path

| Level | Contact | When |
|:------|:--------|:-----|
| Peer help | [Name/channel] | Any question |
| Secondary | [Name] | Can't resolve in 15 min |
| Manager | [Name] | SEV1/SEV2 |
| Executive | [Name] | SEV1 with major impact |

### Current On-Call Rotation

| Role | Name | Contact |
|:-----|:-----|:--------|
| Primary | [Incoming] | [Contact] |
| Secondary | [Name] | [Contact] |
| Manager | [Name] | [Contact] |

---

## Handoff Checklist

### Outgoing On-Call

- [ ] Updated this document
- [ ] Briefed incoming on active issues
- [ ] Shared any tribal knowledge needed
- [ ] Confirmed incoming has access to necessary systems
- [ ] Transferred any open threads/conversations

### Incoming On-Call

- [ ] Reviewed this document
- [ ] Understand active incidents (if any)
- [ ] Know who to escalate to
- [ ] Have access to all necessary systems
- [ ] Know location of runbooks
- [ ] Acknowledged handoff in [channel]

---

## Handoff Confirmation

**Outgoing confirms:** _[Name]_ at _[Time]_

**Incoming confirms:** _[Name]_ at _[Time]_

---

## Notes

_[Any additional context, observations, or recommendations]_

---

*Template version: 1.0*  
*Last updated: [Date]*
