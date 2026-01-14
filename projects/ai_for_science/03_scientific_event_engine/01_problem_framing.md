[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Project Overview](README.md) | [Next: Event Architecture →](02_event_architecture.md)

# Problem Framing

Understand the scientific event processing context, constraints, and what makes this domain unique.

---

## The Scenario

You're building an event processing system for a network of astronomical observatories. The network generates millions of observations nightly. Your system must identify the handful that represent genuinely interesting transient phenomena worthy of follow-up.

### Context

- **Data sources:** Multiple telescope facilities, different wavelengths
- **Event volume:** ~10 million candidates per night
- **True events:** ~1,000 worth detailed review, ~10 scientifically significant
- **Latency target:** Critical events within minutes, others within hours
- **Operations:** 24/7 continuous processing

### What Scientists Need

Scientists need the system to:
- **Catch the rare, important events** — Don't miss the supernova
- **Filter the routine** — Most observations are boring; don't show them
- **Prioritise attention** — What should I look at first?
- **Provide context** — What do we already know about this location?
- **Enable follow-up** — Coordinate observations across facilities
- **Maintain provenance** — How did we arrive at this classification?

### What Scientists Don't Need

- Thousands of false positives to review manually
- Unexplained classifications ("it's interesting, trust me")
- Alerts that arrive too late for follow-up
- Systems that can't explain their reasoning

---

## Stakeholder Map

### Primary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Observers** | Timely alerts, accurate classifications | Alert fatigue, missed events |
| **Facility operators** | Reliable, low-maintenance system | System failures, resource usage |
| **Science teams** | Discoveries with proper provenance | Unreproducible results |

### Secondary Stakeholders

| Stakeholder | Needs | Concerns |
|:------------|:------|:---------|
| **Funding agencies** | Scientific productivity | ROI on infrastructure |
| **Journal editors** | Verifiable claims | Unreliable AI-generated results |
| **Public** | Scientific discovery | Wasted resources |

---

## Constraints

### Latency Constraints

| Event Type | Latency Target | Rationale |
|:-----------|:---------------|:----------|
| Critical/rare | <5 minutes | Enable rapid follow-up |
| Significant | <30 minutes | Same-night follow-up |
| Interesting | <4 hours | Next-night planning |
| Routine | <24 hours | Archival completeness |

### Volume Constraints

| Metric | Value | Implication |
|:-------|:------|:------------|
| Raw candidates/night | ~10,000,000 | Need aggressive filtering |
| Human review capacity | ~1,000/night | 99.99% must be auto-handled |
| Storage/event | ~1KB metadata | ~10GB/night metadata |

### Reliability Constraints

| Requirement | Target | Rationale |
|:------------|:-------|:----------|
| Uptime | 99.9% | Can't miss rare events |
| Data loss | 0% | Every observation matters |
| False negative rate | <1% significant events | Discovery is the mission |

---

## The Detection Challenge

### Signal vs. Noise

Most "events" aren't scientifically interesting:

| Category | Percentage | Examples |
|:---------|:-----------|:---------|
| **Artifacts** | ~60% | Cosmic rays, satellite trails, chip defects |
| **Known objects** | ~30% | Variable stars, known asteroids |
| **Routine transients** | ~9% | Common variable types |
| **Interesting** | ~0.9% | Worth professional review |
| **Significant** | ~0.1% | Potential discoveries |
| **Critical** | ~0.001% | Immediate action required |

### The Needle in the Haystack

```
10,000,000 candidates
     ↓ Artifact rejection (60%)
4,000,000 remaining
     ↓ Known object matching (75%)
1,000,000 remaining
     ↓ Routine classification (90%)
100,000 remaining
     ↓ Quality and confidence filtering (90%)
10,000 remaining
     ↓ Scientific interest filtering (90%)
1,000 for human review
     ↓ Human review
~10 scientifically significant
```

### Error Types and Costs

| Error Type | Definition | Cost |
|:-----------|:-----------|:-----|
| **False positive** | Flagging routine as interesting | Wastes human attention |
| **False negative** | Missing truly interesting event | Lost science, unrepeatable |
| **Misclassification** | Wrong category assignment | Wrong follow-up, confusion |
| **Latency miss** | Alert too late for follow-up | Lost observation opportunity |

**The asymmetry:** A false negative for a once-in-a-decade event is catastrophic. A false positive wastes 5 minutes of human time.

---

## Success Criteria

### Detection Metrics

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Sensitivity (recall) | True events detected / All true events | >99% for significant |
| Specificity | True negatives / All negatives | >99.9% |
| Precision | True events / All flagged | >10% for human review |
| Latency | Time from observation to alert | Per category targets |

### Operational Metrics

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Throughput | Events processed / second | >1,000 sustained |
| Queue depth | Pending events | <1 hour backlog |
| System uptime | Available time / Total time | >99.9% |

### Scientific Metrics

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Provenance completeness | Events with full trace | 100% |
| Classification accuracy | Correct categories | >95% |
| Discovery contribution | Significant events found | Measurable improvement |

---

## Failure Modes

### High-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Missed critical event** | Supernova not flagged | Lost discovery, possibly unrepeatable |
| **System downtime** | Pipeline crashes | Entire night's data unprocessed |
| **Provenance loss** | Can't trace detection | Results unpublishable |

### Medium-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **High false positive rate** | 10x normal alerts | Alert fatigue, lost trust |
| **Latency spike** | Hours instead of minutes | Missed follow-up windows |
| **Misclassification** | Supernova labeled as asteroid | Wrong follow-up |

### Low-Severity Failures

| Failure | Example | Impact |
|:--------|:--------|:-------|
| **Minor latency increase** | +10% processing time | Slightly delayed alerts |
| **Classification uncertainty** | Ambiguous categories | Human must disambiguate |

---

## Multi-Facility Coordination

### The Coordination Challenge

Real discoveries often require multiple observations:

```
Facility A: Detects candidate
     ↓
System: Classifies as potentially significant
     ↓
Facility B: Requests follow-up observation
     ↓
Facility B: Confirms or refutes
     ↓
System: Updates classification
     ↓
Community: Coordinates response
```

### Coordination Requirements

| Requirement | Description |
|:------------|:------------|
| **Event identity** | Same object across facilities |
| **Priority communication** | Which facility should respond |
| **Observation requests** | What observations are needed |
| **Result integration** | Combine multi-facility data |
| **Attribution** | Who detected what when |

---

## Your Task

### Exercise 1: Stakeholder Analysis

For each stakeholder:
1. What is their primary concern?
2. What would delight them?
3. What would frustrate them?
4. How does your design serve them?

### Exercise 2: Error Cost Analysis

For each error type:
1. What is the scientific cost?
2. What is the operational cost?
3. What is the trust cost?
4. How do you minimize this error?

### Exercise 3: Threshold Design

Consider the filtering stages:
1. What thresholds would you set?
2. How would you tune sensitivity vs. specificity?
3. How would you handle edge cases?
4. How would thresholds differ by event type?

### Exercise 4: Failure Prevention

For each high-severity failure:
1. How would you detect it?
2. How would you prevent it?
3. How would you recover?
4. How would you learn from it?

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Project Overview](README.md) | [All Sections](#project-structure) | [Event Architecture →](02_event_architecture.md) |
