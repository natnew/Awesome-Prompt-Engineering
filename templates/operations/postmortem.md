# Post-Mortem Template

## Overview

**Purpose:** Learn from incidents through blameless analysis of what happened and why.

**When to use:** After any SEV1/SEV2 incident, or any incident with learning value.

**Competencies:** [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability), [Governance & Defensibility](../../COMPETENCIES.md#4-governance--defensibility)

---

# Post-Mortem: [Incident Title]

**Incident ID:** INC-XXXX  
**Date of Incident:** YYYY-MM-DD  
**Post-Mortem Date:** YYYY-MM-DD  
**Author:** [Name]  
**Status:** Draft | Under Review | Final

---

## Incident Summary

**Duration:** _[Start time]_ to _[End time]_ (_[X hours Y minutes]_)

**Severity:** SEV1 / SEV2 / SEV3

**Impact:**
- Users affected: _[Number or percentage]_
- Requests failed: _[Number or percentage]_
- Revenue impact: _[$X or N/A]_
- Other impact: _[Description]_

**One-line summary:**  
_[What happened in one sentence]_

---

## Timeline

All times in UTC.

| Time | Event |
|:-----|:------|
| HH:MM | _[First sign of problem]_ |
| HH:MM | _[Alert fired / User report]_ |
| HH:MM | _[Investigation started]_ |
| HH:MM | _[Root cause identified]_ |
| HH:MM | _[Mitigation started]_ |
| HH:MM | _[Mitigation complete]_ |
| HH:MM | _[Incident resolved]_ |

### Key Timestamps

| Metric | Time | Duration |
|:-------|:-----|:---------|
| Time to Detection | HH:MM | _[X min from start]_ |
| Time to Acknowledge | HH:MM | _[X min from detection]_ |
| Time to Mitigate | HH:MM | _[X min from detection]_ |
| Time to Resolve | HH:MM | _[X min from detection]_ |

---

## Root Cause

_[Clear explanation of what caused the incident. Be specific.]_

**The immediate cause was:**  
_[Direct trigger]_

**This was possible because:**  
_[Underlying condition that allowed the trigger to cause impact]_

**Contributing factors:**
1. _[Factor 1]_
2. _[Factor 2]_
3. _[Factor 3]_

---

## Detection

**How was this detected?**  
_[Alert / User report / Monitoring / Other]_

**Why wasn't it detected sooner?**  
_[Gap in monitoring / Alert threshold / Other]_

**What would have detected this earlier?**  
_[Improved detection mechanism]_

---

## Response

### What Went Well

- _[Effective action 1]_
- _[Effective action 2]_
- _[Effective action 3]_

### What Went Poorly

- _[Problem 1]_
- _[Problem 2]_
- _[Problem 3]_

### Where We Got Lucky

- _[Lucky circumstance 1]_
- _[Lucky circumstance 2]_

---

## Impact Analysis

### User Impact

_[Detailed description of how users were affected]_

### Business Impact

_[Revenue, reputation, contractual implications]_

### Data Impact

_[Any data loss, corruption, or exposure]_

---

## Lessons Learned

### Key Insights

1. _[Insight 1]_
2. _[Insight 2]_
3. _[Insight 3]_

### Surprises

_[Anything that surprised us about how the system behaved]_

### Questions Raised

_[Open questions we should investigate further]_

---

## Action Items

### Prevent Recurrence

| Action | Owner | Priority | Due Date | Status |
|:-------|:------|:---------|:---------|:-------|
| _[Fix root cause]_ | | P0 | | |
| _[Address contributing factor 1]_ | | P1 | | |
| _[Address contributing factor 2]_ | | P1 | | |

### Improve Detection

| Action | Owner | Priority | Due Date | Status |
|:-------|:------|:---------|:---------|:-------|
| _[Add monitoring]_ | | P1 | | |
| _[Improve alerting]_ | | P1 | | |

### Improve Response

| Action | Owner | Priority | Due Date | Status |
|:-------|:------|:---------|:---------|:-------|
| _[Update runbook]_ | | P2 | | |
| _[Improve tooling]_ | | P2 | | |

### Process Improvements

| Action | Owner | Priority | Due Date | Status |
|:-------|:------|:---------|:---------|:-------|
| _[Process change]_ | | P2 | | |

---

## Follow-Up

### Review Schedule

| Date | Type | Attendees |
|:-----|:-----|:----------|
| _[Date]_ | Action item review | _[Team]_ |
| _[Date]_ | 30-day retrospective | _[Team]_ |

### Related Incidents

| Incident | Relationship |
|:---------|:-------------|
| _[INC-XXX]_ | _[How related]_ |

---

## Appendix

### Technical Details

_[Detailed technical information for future reference]_

### Communication Log

| Time | Channel | Message Summary |
|:-----|:--------|:----------------|
| | | |

### Supporting Data

_[Links to dashboards, logs, charts from the incident]_

---

## Post-Mortem Review

### Attendees

| Name | Role |
|:-----|:-----|
| | Incident Commander |
| | Responder |
| | Responder |
| | Observer |

### Approval

| Role | Name | Date |
|:-----|:-----|:-----|
| Author | | |
| Incident Commander | | |
| Engineering Lead | | |

---

*Reminder: Post-mortems are blameless. We focus on systems and processes, not individuals.*

---

*Template version: 1.0*  
*Last updated: [Date]*
