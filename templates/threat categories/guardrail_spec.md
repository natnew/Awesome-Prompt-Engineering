# Guardrail Specification Template

## Overview

**Purpose:** Document safety constraints, their implementation, and verification criteria.

**When to use:** When implementing any safety constraint on an AI system.

**Competencies:** [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability)

---

# Guardrail Specification: [Guardrail Name]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Version:** 1.0  
**Status:** Draft | Implemented | Verified

---

## Summary

| Attribute | Value |
|:----------|:------|
| **Name** | _[Descriptive name]_ |
| **Type** | Input / Action / Output / Runtime |
| **Stage** | Pre-processing / Processing / Post-processing |
| **Threat Addressed** | _[Reference to threat model]_ |
| **Severity if Bypassed** | Critical / High / Medium / Low |

**One-sentence description:**  
_[What this guardrail does]_

---

## Constraint Definition

### What It Prevents

_[Specific behavior or outcome this guardrail blocks]_

### What It Allows

_[Expected legitimate behavior that should pass]_

### Boundary Cases

| Scenario | Expected Behavior | Rationale |
|:---------|:------------------|:----------|
| _[Edge case 1]_ | Allow / Block | _[Why]_ |
| _[Edge case 2]_ | Allow / Block | _[Why]_ |
| _[Edge case 3]_ | Allow / Block | _[Why]_ |

---

## Implementation

### Detection Logic

```
[Pseudocode or description of detection mechanism]

IF [condition] THEN
    TRIGGER guardrail
    ACTION: [block / modify / escalate / log]
END IF
```

### Parameters

| Parameter | Value | Rationale |
|:----------|:------|:----------|
| _[Param 1]_ | _[Value]_ | _[Why this value]_ |
| _[Param 2]_ | _[Value]_ | _[Why this value]_ |

### Action on Trigger

| Action | Description |
|:-------|:------------|
| **Primary** | _[What happens when triggered]_ |
| **User message** | _[What the user sees, if applicable]_ |
| **Logging** | _[What gets logged]_ |
| **Alerting** | _[Who gets notified]_ |

### Code Reference

```
File: [path/to/implementation]
Function: [function_name]
Lines: [start-end]
```

---

## Dependencies

| Dependency | Type | Failure Mode |
|:-----------|:-----|:-------------|
| _[Dependency 1]_ | Required / Optional | _[What happens if unavailable]_ |
| _[Dependency 2]_ | Required / Optional | _[What happens if unavailable]_ |

---

## Test Cases

### Must Block (True Positives)

| ID | Input | Expected | Rationale |
|:---|:------|:---------|:----------|
| TB-01 | _[Test input]_ | BLOCK | _[Why this should be blocked]_ |
| TB-02 | _[Test input]_ | BLOCK | |
| TB-03 | _[Test input]_ | BLOCK | |

### Must Allow (True Negatives)

| ID | Input | Expected | Rationale |
|:---|:------|:---------|:----------|
| TA-01 | _[Test input]_ | ALLOW | _[Why this should pass]_ |
| TA-02 | _[Test input]_ | ALLOW | |
| TA-03 | _[Test input]_ | ALLOW | |

### Edge Cases

| ID | Input | Expected | Rationale |
|:---|:------|:---------|:----------|
| EC-01 | _[Test input]_ | _[Decision]_ | _[Why]_ |
| EC-02 | _[Test input]_ | _[Decision]_ | _[Why]_ |

### Adversarial Tests

| ID | Attack Type | Input | Expected |
|:---|:------------|:------|:---------|
| AT-01 | _[Bypass attempt type]_ | _[Crafted input]_ | BLOCK |
| AT-02 | _[Bypass attempt type]_ | _[Crafted input]_ | BLOCK |

---

## Performance

| Metric | Target | Current | Notes |
|:-------|:-------|:--------|:------|
| Latency added | < _[X]_ ms | _[Y]_ ms | |
| False positive rate | < _[X]_% | _[Y]_% | |
| False negative rate | < _[X]_% | _[Y]_% | |
| Resource usage | _[Constraint]_ | _[Actual]_ | |

---

## Failure Modes

| Failure | Likelihood | Impact | Mitigation |
|:--------|:-----------|:-------|:-----------|
| Guardrail unavailable | _[L/M/H]_ | _[L/M/H/C]_ | _[What happens]_ |
| False positive spike | _[L/M/H]_ | _[L/M/H/C]_ | _[What happens]_ |
| Bypass discovered | _[L/M/H]_ | _[L/M/H/C]_ | _[What happens]_ |

**Fail-safe behavior:**  
_[What happens if this guardrail fails? Open or closed?]_

---

## Monitoring

### Metrics to Track

| Metric | Alert Threshold | Dashboard |
|:-------|:----------------|:----------|
| Trigger rate | _[Threshold]_ | _[Link]_ |
| Block rate | _[Threshold]_ | _[Link]_ |
| Latency p99 | _[Threshold]_ | _[Link]_ |

### Alerts

| Alert | Condition | Severity | Runbook |
|:------|:----------|:---------|:--------|
| _[Alert name]_ | _[When it fires]_ | _[Sev]_ | _[Link]_ |

---

## Maintenance

### Update Triggers

This guardrail should be reviewed when:
- [ ] New bypass technique discovered
- [ ] False positive complaints increase
- [ ] Upstream model changes
- [ ] Threat model updates
- [ ] Quarterly (minimum)

### Tuning History

| Date | Change | Reason | Result |
|:-----|:-------|:-------|:-------|
| | | | |

---

## Approval

| Role | Name | Approved | Date |
|:-----|:-----|:---------|:-----|
| Author | | ✅ | |
| Security Review | | | |
| System Owner | | | |

---

## Related Documents

- Threat Model: _[Link]_
- Runbook: _[Link]_
- Other Guardrails: _[Links]_

---

*Template version: 1.0*  
*Last updated: [Date]*
