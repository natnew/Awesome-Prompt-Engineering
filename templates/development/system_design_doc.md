# System Design Document Template

## Overview

**Purpose:** Document architecture decisions for AI systems, capturing rationale and trade-offs.

**When to use:** New AI system design, major architectural changes, system reviews.

**Competencies:** [Systems Design & Integration](../../COMPETENCIES.md#5-systems-design--integration)

---

# System Design: [System Name]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Status:** Draft | Under Review | Approved | Implemented  
**Reviewers:** [Names]

---

## Executive Summary

_[2-3 paragraphs describing the system, its purpose, and key design decisions]_

---

## Goals & Non-Goals

### Goals

What this system will do:

1. _[Goal 1]_
2. _[Goal 2]_
3. _[Goal 3]_

### Non-Goals

What this system explicitly will NOT do (in this version):

1. _[Non-goal 1]_
2. _[Non-goal 2]_

---

## Background

### Problem Statement

_[What problem does this system solve?]_

### Current State

_[How is this handled today? What are the pain points?]_

### Why Now?

_[What's driving this initiative?]_

---

## Requirements

### Functional Requirements

| ID | Requirement | Priority |
|:---|:------------|:---------|
| FR-1 | _[Requirement]_ | Must have |
| FR-2 | _[Requirement]_ | Must have |
| FR-3 | _[Requirement]_ | Should have |
| FR-4 | _[Requirement]_ | Nice to have |

### Non-Functional Requirements

| Category | Requirement | Target |
|:---------|:------------|:-------|
| Latency | p95 response time | < 2s |
| Throughput | Requests per second | > 100 |
| Availability | Uptime | 99.9% |
| Cost | Per 1K requests | < $X |
| Quality | Accuracy | > 90% |

### Constraints

| Constraint | Description |
|:-----------|:------------|
| _[Constraint 1]_ | _[Description]_ |
| _[Constraint 2]_ | _[Description]_ |

---

## High-Level Design

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        [Architecture]                        │
│                                                              │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐ │
│   │ Client  │───▶│   API   │───▶│ Service │───▶│  Model  │ │
│   └─────────┘    └─────────┘    └─────────┘    └─────────┘ │
│                       │              │                       │
│                       ▼              ▼                       │
│                  ┌─────────┐   ┌─────────┐                  │
│                  │  Cache  │   │   DB    │                  │
│                  └─────────┘   └─────────┘                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Component Overview

| Component | Purpose | Technology |
|:----------|:--------|:-----------|
| _[Component 1]_ | _[Purpose]_ | _[Tech]_ |
| _[Component 2]_ | _[Purpose]_ | _[Tech]_ |
| _[Component 3]_ | _[Purpose]_ | _[Tech]_ |

### Data Flow

1. _[Step 1: What happens]_
2. _[Step 2: What happens]_
3. _[Step 3: What happens]_

---

## Detailed Design

### Component 1: [Name]

**Purpose:** _[What this component does]_

**Interface:**
```
[API or interface definition]
```

**Implementation Notes:**
- _[Note 1]_
- _[Note 2]_

**Dependencies:**
- _[Dependency 1]_
- _[Dependency 2]_

### Component 2: [Name]

**Purpose:** _[What this component does]_

**Interface:**
```
[API or interface definition]
```

**Implementation Notes:**
- _[Note 1]_
- _[Note 2]_

### AI/ML Components

**Model Selection:**

| Option | Pros | Cons | Decision |
|:-------|:-----|:-----|:---------|
| _[Model A]_ | _[Pros]_ | _[Cons]_ | ✓ Selected / Rejected |
| _[Model B]_ | _[Pros]_ | _[Cons]_ | Selected / ✓ Rejected |

**Prompt Design:**
- _[Key prompt design decisions]_
- _[Link to prompt specification]_

**Context Management:**
- _[How context is assembled]_
- _[Token budget allocation]_

---

## Data Design

### Data Model

```
[Schema or data structure]
```

### Data Flow

| Data | Source | Destination | Format | Retention |
|:-----|:-------|:------------|:-------|:----------|
| _[Data 1]_ | _[Source]_ | _[Dest]_ | _[Format]_ | _[Retention]_ |

### Data Privacy

| Data Type | Classification | Handling |
|:----------|:---------------|:---------|
| _[Type]_ | PII / Sensitive / Public | _[How handled]_ |

---

## API Design

### Endpoints

**POST /api/v1/[endpoint]**

Request:
```json
{
  "field": "value"
}
```

Response:
```json
{
  "field": "value"
}
```

### Error Handling

| Code | Meaning | When |
|:-----|:--------|:-----|
| 400 | Bad Request | _[When]_ |
| 401 | Unauthorized | _[When]_ |
| 429 | Rate Limited | _[When]_ |
| 500 | Server Error | _[When]_ |

---

## Safety & Security

### Threat Model Summary

| Threat | Risk | Mitigation |
|:-------|:-----|:-----------|
| _[Threat 1]_ | High/Med/Low | _[Mitigation]_ |
| _[Threat 2]_ | High/Med/Low | _[Mitigation]_ |

_[Link to full threat model]_

### Guardrails

| Guardrail | Type | Purpose |
|:----------|:-----|:--------|
| _[Guardrail 1]_ | Input/Output/Action | _[Purpose]_ |
| _[Guardrail 2]_ | Input/Output/Action | _[Purpose]_ |

### Human Oversight

| Scenario | Oversight Type |
|:---------|:---------------|
| _[Scenario]_ | _[Human-in-loop / Review / None]_ |

---

## Scalability & Performance

### Scaling Strategy

| Component | Scaling Type | Trigger |
|:----------|:-------------|:--------|
| _[Component]_ | Horizontal / Vertical | _[When to scale]_ |

### Performance Optimization

| Optimization | Benefit | Trade-off |
|:-------------|:--------|:----------|
| _[Optimization 1]_ | _[Benefit]_ | _[Trade-off]_ |
| _[Optimization 2]_ | _[Benefit]_ | _[Trade-off]_ |

### Capacity Planning

| Metric | Current | 6 Month | 1 Year |
|:-------|:--------|:--------|:-------|
| Requests/day | _[N]_ | _[N]_ | _[N]_ |
| Storage | _[GB]_ | _[GB]_ | _[GB]_ |
| Cost/month | $X | $Y | $Z |

---

## Reliability

### Failure Modes

| Failure | Impact | Detection | Recovery |
|:--------|:-------|:----------|:---------|
| _[Failure 1]_ | _[Impact]_ | _[How detected]_ | _[Recovery]_ |
| _[Failure 2]_ | _[Impact]_ | _[How detected]_ | _[Recovery]_ |

### Dependencies

| Dependency | SLA | If Unavailable |
|:-----------|:----|:---------------|
| _[Dependency]_ | _[SLA]_ | _[Fallback behavior]_ |

### Monitoring

| Metric | Alert Threshold | Response |
|:-------|:----------------|:---------|
| Error rate | > 5% | _[Response]_ |
| Latency p95 | > 5s | _[Response]_ |

---

## Testing Strategy

| Test Type | Scope | Tools |
|:----------|:------|:------|
| Unit | Component logic | _[Tools]_ |
| Integration | Component interaction | _[Tools]_ |
| E2E | Full system | _[Tools]_ |
| Load | Performance | _[Tools]_ |
| Evaluation | AI quality | _[Tools]_ |

---

## Deployment

### Deployment Strategy

_[Blue-green / Canary / Rolling / etc.]_

### Rollback Plan

1. _[Step 1]_
2. _[Step 2]_

### Feature Flags

| Flag | Purpose | Default |
|:-----|:--------|:--------|
| _[Flag]_ | _[Purpose]_ | _[Default]_ |

---

## Cost Analysis

### Infrastructure Costs

| Component | Monthly Cost | Notes |
|:----------|:-------------|:------|
| _[Component]_ | $X | |
| **Total** | **$Y** | |

### AI/API Costs

| Provider | Cost Model | Estimated Monthly |
|:---------|:-----------|:------------------|
| _[Provider]_ | _[$/1K tokens]_ | $X |

---

## Timeline

| Milestone | Date | Description |
|:----------|:-----|:------------|
| Design approval | _[Date]_ | |
| MVP complete | _[Date]_ | |
| Beta launch | _[Date]_ | |
| GA | _[Date]_ | |

---

## Alternatives Considered

### Alternative 1: [Name]

**Approach:** _[Description]_

**Pros:**
- _[Pro 1]_

**Cons:**
- _[Con 1]_

**Why rejected:** _[Reason]_

### Alternative 2: [Name]

**Approach:** _[Description]_

**Pros:**
- _[Pro 1]_

**Cons:**
- _[Con 1]_

**Why rejected:** _[Reason]_

---

## Open Questions

- [ ] _[Question 1]_
- [ ] _[Question 2]_

---

## References

- _[Reference 1]_
- _[Reference 2]_

---

## Appendix

### Glossary

| Term | Definition |
|:-----|:-----------|
| _[Term]_ | _[Definition]_ |

### Detailed Calculations

_[Any detailed calculations referenced above]_

---

## Approval

| Role | Name | Approved | Date |
|:-----|:-----|:---------|:-----|
| Author | | ✅ | |
| Tech Lead | | | |
| Security | | | |
| Product | | | |

---

*Template version: 1.0*  
*Last updated: [Date]*
