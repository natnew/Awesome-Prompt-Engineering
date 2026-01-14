# Ethics Review Template

## Overview

**Purpose:** Systematic assessment of ethical considerations for AI systems before deployment.

**When to use:** Before deploying user-facing AI systems, when handling sensitive data, or when AI decisions have significant consequences.

**Competencies:** [Governance & Defensibility](../../COMPETENCIES.md#4-governance--defensibility), [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability)

---

# Ethics Review: [System Name]

**Date:** YYYY-MM-DD  
**Reviewer(s):** [Names]  
**System Owner:** [Name]  
**Review Type:** Initial | Update | Incident-Triggered  
**Status:** Draft | Under Review | Approved | Requires Changes

---

## System Overview

**What does this system do?**  
_[Brief description]_

**Who uses it?**  
_[End users, operators, affected parties]_

**What decisions does it influence?**  
_[What happens based on system output]_

**What data does it use?**  
_[Input data sources]_

---

## Impact Assessment

### Who Is Affected?

| Stakeholder Group | How They're Affected | Potential Harm | Potential Benefit |
|:------------------|:---------------------|:---------------|:------------------|
| Direct users | | | |
| Subjects of decisions | | | |
| Third parties | | | |
| Society broadly | | | |

### Power Dynamics

- Who has power in this system? _[Who controls, who benefits]_
- Who lacks power? _[Who has no choice, who bears risk]_
- Are there vulnerable populations affected? _[Children, elderly, disabled, economically disadvantaged]_

---

## Ethical Dimensions

### 1. Fairness & Bias

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| Does the system perform equally across demographic groups? | ✅ Yes / ⚠️ Partial / ❌ No / ❓ Unknown | |
| Could historical bias in training data affect outcomes? | | |
| Are there proxy variables that could enable discrimination? | | |
| Have we tested for disparate impact? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 2. Transparency & Explainability

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| Do users know they're interacting with AI? | ✅ Yes / ❌ No | |
| Can we explain individual decisions if asked? | | |
| Is the system's scope and limitations documented? | | |
| Do affected parties have access to information about the system? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 3. Privacy & Data Protection

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| What personal data is collected? | _[List]_ | |
| Is data collection minimized to what's necessary? | ✅ Yes / ❌ No | |
| How long is data retained? | _[Duration]_ | |
| Can individuals access, correct, or delete their data? | | |
| Is consent obtained appropriately? | | |
| Is data shared with third parties? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 4. Safety & Harm Prevention

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| What harms could the system cause? | _[List]_ | |
| Are there safeguards against misuse? | | |
| What happens when the system fails? | | |
| Is there human oversight for high-stakes decisions? | | |
| Can the system be shut down quickly if needed? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 5. Autonomy & Human Agency

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| Does the system respect user autonomy? | ✅ Yes / ⚠️ Partial / ❌ No | |
| Can users opt out? | | |
| Are users manipulated or deceived? | | |
| Does the system create unhealthy dependencies? | | |
| Is there meaningful human control over outcomes? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 6. Accountability

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| Who is responsible when things go wrong? | _[Name/role]_ | |
| Is there a clear escalation path? | | |
| Are decisions logged for audit? | | |
| Is there a mechanism for redress? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 7. Environmental Impact

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| What is the computational cost of this system? | _[Estimate]_ | |
| Is the environmental impact proportionate to the benefit? | ✅ Yes / ❌ No | |
| Are there lower-impact alternatives? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

### 8. Societal Impact

| Question | Assessment | Evidence |
|:---------|:-----------|:---------|
| Could this system be misused at scale? | ✅ Yes / ❌ No | |
| Does it concentrate power inappropriately? | | |
| Could it undermine democratic processes? | | |
| Does it displace workers? How is that addressed? | | |

**Mitigation steps:**
- [ ] _[Step 1]_
- [ ] _[Step 2]_

---

## Risk Summary

| Dimension | Risk Level | Key Concerns | Status |
|:----------|:-----------|:-------------|:-------|
| Fairness & Bias | 🟢 Low / 🟡 Medium / 🔴 High | | Mitigated / In Progress / Unaddressed |
| Transparency | 🟢 / 🟡 / 🔴 | | |
| Privacy | 🟢 / 🟡 / 🔴 | | |
| Safety | 🟢 / 🟡 / 🔴 | | |
| Autonomy | 🟢 / 🟡 / 🔴 | | |
| Accountability | 🟢 / 🟡 / 🔴 | | |
| Environmental | 🟢 / 🟡 / 🔴 | | |
| Societal | 🟢 / 🟡 / 🔴 | | |

---

## Required Actions

### Before Launch

| Action | Owner | Due Date | Status |
|:-------|:------|:---------|:-------|
| | | | |
| | | | |

### Ongoing Monitoring

| What to Monitor | Frequency | Owner |
|:----------------|:----------|:------|
| | | |
| | | |

### Review Triggers

This review should be updated when:
- [ ] Significant changes to system capabilities
- [ ] New use cases or user populations
- [ ] Incidents or near-misses
- [ ] Changes in regulatory environment
- [ ] Annually (minimum)

---

## Recommendation

**[ ] APPROVE** — Ethical risks are acceptable and appropriately mitigated

**[ ] APPROVE WITH CONDITIONS** — May proceed if:
- _[Condition 1]_
- _[Condition 2]_

**[ ] DEFER** — Cannot approve until:
- _[Blocker 1]_
- _[Blocker 2]_

**[ ] REJECT** — Ethical risks are unacceptable because:
- _[Reason]_

---

## Approval

| Role | Name | Decision | Date | Notes |
|:-----|:-----|:---------|:-----|:------|
| Ethics Reviewer | | | | |
| System Owner | | | | |
| Legal (if applicable) | | | | |
| Executive Sponsor | | | | |

---

## Appendix: Stakeholder Consultation

| Stakeholder | Consultation Method | Key Feedback | How Addressed |
|:------------|:--------------------|:-------------|:--------------|
| | | | |

---

## Appendix: References

- [ ] Relevant regulations: _[List]_
- [ ] Industry standards: _[List]_
- [ ] Internal policies: _[List]_
- [ ] Prior ethics reviews: _[List]_

---

*Template version: 1.0*  
*Last updated: [Date]*
