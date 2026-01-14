# Threat Model: [Agent Name]

## Document Information

| Field | Value |
|:------|:------|
| **Agent Name** | |
| **Version** | |
| **Date** | |
| **Author** | |
| **Reviewers** | |

---

## 1. System Description

### 1.1 Purpose

[What does this agent do?]

### 1.2 Capabilities

[What actions can the agent take?]

| Capability | Description | Side Effects |
|:-----------|:------------|:-------------|
| | | |
| | | |
| | | |

### 1.3 Data Access

[What data can the agent access?]

| Data Type | Access Level | Sensitivity |
|:----------|:-------------|:------------|
| | Read / Write | Low / Medium / High |
| | | |
| | | |

### 1.4 Trust Boundaries

```
[Diagram showing trust boundaries]

┌─────────────────────────────────────────────────────────┐
│                    UNTRUSTED                            │
│  ┌───────────┐                                          │
│  │   User    │                                          │
│  │   Input   │                                          │
│  └─────┬─────┘                                          │
├────────┼────────────────────────────────────────────────┤
│        │           SEMI-TRUSTED                         │
│        ▼                                                │
│  ┌───────────┐    ┌───────────┐                        │
│  │   Agent   │───▶│   Tools   │                        │
│  └───────────┘    └─────┬─────┘                        │
├─────────────────────────┼───────────────────────────────┤
│                         │     TRUSTED                   │
│                         ▼                               │
│                   ┌───────────┐                        │
│                   │ Database  │                        │
│                   │ / APIs    │                        │
│                   └───────────┘                        │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Threat Identification

### 2.1 Threat Categories

| Category | Description | Relevant? |
|:---------|:------------|:----------|
| **Overreach** | Agent does more than intended | Yes / No |
| **Runaway** | Agent enters infinite loop or spirals | Yes / No |
| **Misuse** | Bad actor exploits the agent | Yes / No |
| **Hallucination** | Agent takes action based on false belief | Yes / No |
| **Cascade** | One failure triggers others | Yes / No |
| **Opacity** | Can't tell what agent did or why | Yes / No |
| **Data Exfiltration** | Sensitive data exposed | Yes / No |
| **Denial of Service** | Agent makes system unavailable | Yes / No |

### 2.2 Detailed Threat Analysis

---

#### T-001: [Threat Name]

**Category:** [Overreach / Runaway / Misuse / etc.]

**Description:**
[Detailed description of the threat]

**Attack Vector:**
[How could this happen?]

**Impact:**
- Business impact: [Description]
- User impact: [Description]
- Reputation impact: [Description]

**Likelihood:** Low / Medium / High

**Impact Severity:** Low / Medium / High

**Risk Score:** Likelihood × Severity = [Low/Medium/High]

**Existing Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

**Proposed Mitigations:**
- [Mitigation 1]
- [Mitigation 2]

**Residual Risk:** [After mitigations]

---

#### T-002: [Threat Name]

**Category:** 

**Description:**

**Attack Vector:**

**Impact:**
- Business impact:
- User impact:
- Reputation impact:

**Likelihood:**

**Impact Severity:**

**Risk Score:**

**Existing Mitigations:**

**Proposed Mitigations:**

**Residual Risk:**

---

#### T-003: [Threat Name]

[Repeat for each threat]

---

## 3. Risk Assessment Matrix

### 3.1 Risk Heatmap

|              | Low Impact | Medium Impact | High Impact |
|:-------------|:-----------|:--------------|:------------|
| **High Likelihood** | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Minimal | Low | Medium |

### 3.2 Threats by Risk Level

| Risk Level | Threat IDs |
|:-----------|:-----------|
| **Critical** | |
| **High** | |
| **Medium** | |
| **Low** | |
| **Minimal** | |

---

## 4. Mitigation Strategy

### 4.1 Prioritized Mitigations

| Priority | Threat | Mitigation | Implementation |
|:---------|:-------|:-----------|:---------------|
| 1 | T-XXX | | Guardrail / Circuit Breaker / Monitoring |
| 2 | T-XXX | | |
| 3 | T-XXX | | |
| 4 | T-XXX | | |
| 5 | T-XXX | | |

### 4.2 Defense in Depth Mapping

| Layer | Threats Addressed | Implementation |
|:------|:------------------|:---------------|
| Input Validation | | |
| Tool Constraints | | |
| Output Validation | | |
| Circuit Breakers | | |
| Monitoring | | |

---

## 5. Acceptance Criteria

### 5.1 Accepted Residual Risks

| Threat | Residual Risk | Acceptance Rationale |
|:-------|:--------------|:---------------------|
| | | |
| | | |

### 5.2 Unacceptable Risks

| Threat | Required Mitigation | Status |
|:-------|:--------------------|:-------|
| | | Implemented / In Progress / Planned |
| | | |

---

## 6. Monitoring and Detection

### 6.1 Threat Indicators

| Threat | Detection Method | Alert Threshold |
|:-------|:-----------------|:----------------|
| | | |
| | | |

### 6.2 Incident Triggers

| Threat | Incident Criteria | Response |
|:-------|:------------------|:---------|
| | | |
| | | |

---

## 7. Review Schedule

| Review Type | Frequency | Next Review |
|:------------|:----------|:------------|
| Full threat model review | Quarterly | |
| Mitigation effectiveness | Monthly | |
| New threat assessment | After incidents / changes | |

---

## 8. Sign-Off

| Role | Name | Date | Signature |
|:-----|:-----|:-----|:----------|
| Author | | | |
| Security Review | | | |
| Engineering Lead | | | |
| Product Owner | | | |

---

## Appendix A: Threat Scenarios

### Scenario 1: [Name]

**Setup:**
[Describe the scenario]

**Attack Steps:**
1. 
2. 
3. 

**Expected Outcome (without mitigations):**

**Expected Outcome (with mitigations):**

---

### Scenario 2: [Name]

[Repeat for additional scenarios]

---

## Appendix B: References

- [Security guidelines]
- [Industry standards]
- [Previous threat models]

---

*This threat model should be reviewed and updated when the system changes or new threats are identified.*
