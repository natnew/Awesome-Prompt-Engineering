# Scope Definition

## System Identity

**System name:** [Your system name]

**One-line description:** [What this system does in one sentence]

**What this system IS:**
- [ ] A health literacy assistant
- [ ] An information synthesis tool
- [ ] A care navigation guide
- [ ] [Other]

**What this system is NOT:**
- [ ] A diagnostic tool
- [ ] A replacement for medical professionals
- [ ] A treatment recommendation engine
- [ ] [Other]

---

## Capability Boundaries

### In Scope

| Capability | Description | Confidence Level |
|:-----------|:------------|:-----------------|
| [Capability 1] | [What the system can do] | [High/Medium/Low] |
| [Capability 2] | | |
| [Capability 3] | | |

### Out of Scope

| Capability | Rationale | How System Responds |
|:-----------|:----------|:--------------------|
| Diagnosis | Requires professional examination | Redirect to healthcare provider |
| Treatment | Requires professional judgment | Explain why, offer alternatives |
| [Other] | | |

### Grey Areas

| Capability | Conditions for Inclusion | Conditions for Exclusion |
|:-----------|:------------------------|:------------------------|
| [Grey area 1] | [When to include] | [When to exclude] |
| [Grey area 2] | | |

---

## User Scope

### Target Users

| User Group | Characteristics | Special Considerations |
|:-----------|:----------------|:----------------------|
| [Group 1] | | |
| [Group 2] | | |

### Excluded Users

| User Group | Why Excluded | Alternative |
|:-----------|:-------------|:------------|
| [Group 1] | | |

---

## Domain Scope

### Included Topics

| Health Domain | Depth | Notes |
|:--------------|:------|:------|
| General symptoms | Information only | No diagnosis |
| [Domain 2] | | |

### Excluded Topics

| Health Domain | Rationale | Response Strategy |
|:--------------|:----------|:------------------|
| Mental health crisis | Requires specialist | Crisis resources |
| [Domain 2] | | |

---

## Temporal Scope

- **Knowledge currency:** [How current is medical information?]
- **Update frequency:** [How often is knowledge updated?]
- **Staleness handling:** [What happens with outdated queries?]

---

## Geographic Scope

- **Primary region:** [Where is this designed for?]
- **Healthcare system:** [Which healthcare context?]
- **Regulatory context:** [Which regulations apply?]

---

## Scope Communication

### How Users Learn Scope

| Touchpoint | Message |
|:-----------|:--------|
| Onboarding | [What users learn first] |
| In conversation | [How scope is reinforced] |
| At boundaries | [What happens at edges] |

### Standard Scope Messages

**For diagnosis requests:**
```
[Your standard response when users ask for diagnosis]
```

**For treatment requests:**
```
[Your standard response when users ask for treatment]
```

**For out-of-scope topics:**
```
[Your standard response for excluded topics]
```

---

## Scope Maintenance

- **Review frequency:** [How often is scope reviewed?]
- **Expansion criteria:** [What would justify expanding scope?]
- **Contraction criteria:** [What would justify narrowing scope?]
- **Decision authority:** [Who decides scope changes?]

---

## Sign-Off

| Role | Name | Date | Signature |
|:-----|:-----|:-----|:----------|
| System Designer | | | |
| Clinical Reviewer | | | |
| Ethics Reviewer | | | |
