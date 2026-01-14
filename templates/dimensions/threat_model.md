# Threat Model Template

## Overview

**Purpose:** Systematically identify, analyze, and prioritize potential failure modes and security threats in AI systems.

**When to use:** Early in system design, before production deployment, when adding new capabilities.

**Competencies:** [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability), [Systems Design](../../COMPETENCIES.md#5-systems-design--integration)

---

# Threat Model: [System Name]

**Date:** YYYY-MM-DD  
**Author(s):** [Names]  
**Version:** 1.0  
**Status:** Draft | Under Review | Approved  
**Next Review:** YYYY-MM-DD

---

## System Description

### What Does It Do?

_[Brief functional description]_

### Architecture Overview

```
[Simple diagram or description of components]

User → [Input Processing] → [AI Model] → [Output Processing] → Response
              ↓                  ↓               ↓
         [Guardrails]      [Guardrails]    [Guardrails]
```

### Trust Boundaries

| Boundary | What Crosses It | Trust Level |
|:---------|:----------------|:------------|
| User input → System | User messages, files | Untrusted |
| System → Model API | Prompts, context | Internal |
| Model API → System | Responses | Semi-trusted |
| System → External APIs | Tool calls | Varies |
| System → User | Responses, data | Must be safe |

### Assets to Protect

| Asset | Sensitivity | Impact if Compromised |
|:------|:------------|:----------------------|
| User data | High | Privacy violation, legal liability |
| System prompts | Medium | Enables prompt injection |
| API keys | Critical | Financial loss, system compromise |
| Business logic | Medium | Competitive disadvantage |

---

## Threat Categories

### 1. Prompt Injection

Attacker manipulates AI behavior through crafted inputs.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| Direct injection | User input contains instructions to override system prompt | High | High | **Critical** |
| Indirect injection | Malicious content in retrieved documents | Medium | High | **High** |
| Jailbreaking | Attempts to bypass safety guidelines | High | Medium | **High** |

**Current Mitigations:**
- [ ] Input validation
- [ ] Prompt hardening
- [ ] Output filtering
- [ ] Content moderation

**Gaps:** _[What's not covered]_

### 2. Data Leakage

System exposes sensitive information inappropriately.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| PII in responses | System includes personal data in outputs | Medium | High | **High** |
| System prompt exposure | Attacker extracts system prompt | Medium | Medium | **Medium** |
| Training data leakage | Model regurgitates sensitive training data | Low | High | **Medium** |
| Cross-user leakage | Data from one user exposed to another | Low | Critical | **High** |

**Current Mitigations:**
- [ ] Output filtering for PII
- [ ] Prompt protection techniques
- [ ] User isolation
- [ ] Data minimization

**Gaps:** _[What's not covered]_

### 3. Denial of Service

Attacks on availability or resource consumption.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| Cost explosion | Attacker triggers expensive operations | Medium | High | **High** |
| Resource exhaustion | Overwhelming system with requests | Medium | Medium | **Medium** |
| Infinite loops | Agent stuck in reasoning loop | Medium | Medium | **Medium** |
| Context stuffing | Filling context window to degrade performance | Low | Low | **Low** |

**Current Mitigations:**
- [ ] Rate limiting
- [ ] Cost budgets
- [ ] Timeout limits
- [ ] Circuit breakers

**Gaps:** _[What's not covered]_

### 4. Unauthorized Actions

System takes actions beyond intended scope.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| Scope creep | Agent performs unintended actions | Medium | High | **High** |
| Privilege escalation | Agent accesses unauthorized resources | Low | Critical | **High** |
| Tool misuse | Agent uses tools in harmful ways | Medium | High | **High** |
| Unintended side effects | Actions have unexpected consequences | Medium | Medium | **Medium** |

**Current Mitigations:**
- [ ] Tool allowlisting
- [ ] Parameter validation
- [ ] Action limits
- [ ] Human approval for sensitive actions

**Gaps:** _[What's not covered]_

### 5. Output Harms

System generates harmful content.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| Misinformation | System generates false information | High | Medium | **High** |
| Harmful advice | Dangerous recommendations | Medium | High | **High** |
| Offensive content | Inappropriate or harmful language | Medium | Medium | **Medium** |
| Manipulation | Deceptive or manipulative content | Low | High | **Medium** |

**Current Mitigations:**
- [ ] Output moderation
- [ ] Factuality checking
- [ ] Human review for high-stakes outputs
- [ ] Disclaimers where appropriate

**Gaps:** _[What's not covered]_

### 6. Model-Specific Risks

Risks from the underlying AI model.

| Threat | Description | Likelihood | Impact | Risk |
|:-------|:------------|:-----------|:-------|:-----|
| Model degradation | Model quality decreases over time | Medium | Medium | **Medium** |
| Provider outage | Model API becomes unavailable | Medium | High | **High** |
| Model change | Provider updates model, changing behavior | Medium | Medium | **Medium** |
| Bias | Model exhibits unfair bias | Medium | High | **High** |

**Current Mitigations:**
- [ ] Quality monitoring
- [ ] Fallback options
- [ ] Version pinning
- [ ] Bias testing

**Gaps:** _[What's not covered]_

---

## Risk Matrix

| Risk Level | Definition | Response |
|:-----------|:-----------|:---------|
| **Critical** | Likely AND severe impact | Must address before launch |
| **High** | Likely OR severe impact | Should address before launch |
| **Medium** | Moderate likelihood and impact | Address within 30 days |
| **Low** | Unlikely AND limited impact | Accept or address opportunistically |

### Summary by Risk Level

| Level | Count | Threats |
|:------|:------|:--------|
| Critical | | _[List]_ |
| High | | _[List]_ |
| Medium | | _[List]_ |
| Low | | _[List]_ |

---

## Attack Scenarios

### Scenario 1: [Name]

**Attacker goal:** _[What they want to achieve]_

**Attack path:**
1. _[Step 1]_
2. _[Step 2]_
3. _[Step 3]_

**Current defenses:** _[What stops this]_

**Residual risk:** _[What could still happen]_

### Scenario 2: [Name]

**Attacker goal:** _[What they want to achieve]_

**Attack path:**
1. _[Step 1]_
2. _[Step 2]_
3. _[Step 3]_

**Current defenses:** _[What stops this]_

**Residual risk:** _[What could still happen]_

---

## Mitigation Plan

### Must Have (Before Launch)

| Mitigation | Threat Addressed | Owner | Status |
|:-----------|:-----------------|:------|:-------|
| | | | |
| | | | |

### Should Have (Launch + 30 Days)

| Mitigation | Threat Addressed | Owner | Status |
|:-----------|:-----------------|:------|:-------|
| | | | |
| | | | |

### Nice to Have (Future)

| Mitigation | Threat Addressed | Priority |
|:-----------|:-----------------|:---------|
| | | |
| | | |

---

## Accepted Risks

| Risk | Reason for Acceptance | Conditions | Review Date |
|:-----|:----------------------|:-----------|:------------|
| | | | |

---

## Monitoring & Detection

| Threat Category | How We Detect | Alert Threshold |
|:----------------|:--------------|:----------------|
| Prompt injection | | |
| Data leakage | | |
| DoS/Cost | | |
| Unauthorized actions | | |
| Output harms | | |

---

## Review History

| Date | Reviewer | Changes | Version |
|:-----|:---------|:--------|:--------|
| | | Initial version | 1.0 |

---

*Template version: 1.0*  
*Last updated: [Date]*
