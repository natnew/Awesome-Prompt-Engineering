# Agent Specification

## Overview

This document defines the specifications for all agents in the scientific event processing system.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     EVENT STREAM                                    │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  TRIAGE AGENT                                                       │
│  Purpose: Rapid initial assessment and routing                     │
│  Latency: <100ms                                                   │
└─────────────────────────────────────────────────────────────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  PATTERN AGENT  │   │  ANOMALY AGENT  │   │  CONTEXT AGENT  │
│  <1s            │   │  <1s            │   │  <30s           │
└─────────────────┘   └─────────────────┘   └─────────────────┘
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYNTHESIS AGENT                                                    │
│  Purpose: Combine analyses into coherent assessment                │
│  Latency: <5s                                                      │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  COORDINATION AGENT (significant events only)                       │
│  Purpose: Plan follow-up observations                              │
│  Latency: <5min                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent 1: Triage Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Triage Agent |
| **ID** | `triage_agent` |
| **Version** | 1.0.0 |
| **Role** | Rapid initial assessment and routing |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <50ms | 100ms |
| Latency (p99) | <100ms | 200ms |
| Throughput | >1000/s | N/A |
| Error rate | <0.01% | 0.1% |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Classified event to triage |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| priority | Priority | Assigned priority (1-5) |
| agents_to_invoke | list[str] | Which agents should analyse |
| fast_track | bool | Skip normal flow for critical |
| quick_assessment | dict | Brief initial assessment |

### Decision Logic

```python
def triage(event: ProcessedEvent) -> TriageResult:
    """Fast triage decision."""
    
    # Critical indicators - fast track
    if event.category == EventCategory.CRITICAL:
        return TriageResult(
            priority=1,
            agents=["pattern", "anomaly", "context", "coordination"],
            fast_track=True
        )
    
    # Significant events
    if event.significance_score > 0.7:
        return TriageResult(
            priority=2,
            agents=["pattern", "anomaly", "context"]
        )
    
    # Interesting events
    if event.significance_score > 0.3:
        return TriageResult(
            priority=3,
            agents=["pattern", "anomaly"]
        )
    
    # Unknown classification
    if event.category == EventCategory.UNKNOWN:
        return TriageResult(
            priority=3,
            agents=["pattern", "anomaly"]
        )
    
    # Routine
    return TriageResult(
        priority=5,
        agents=[]
    )
```

### Constraints

| Constraint | Type | Description |
|:-----------|:-----|:------------|
| No external calls | Hard | Must use only cached data |
| Deterministic | Hard | Same input → same output |
| Stateless | Hard | No state between calls |

---

## Agent 2: Pattern Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Pattern Agent |
| **ID** | `pattern_agent` |
| **Version** | 1.0.0 |
| **Role** | Deep pattern matching and classification |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <500ms | 1s |
| Latency (p99) | <1s | 2s |
| Throughput | >100/s | N/A |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Event to analyse |
| triage_result | TriageResult | No | Triage context |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| matched_patterns | list[PatternMatch] | Matched known patterns |
| refined_classification | Classification | More precise category |
| similar_events | list[HistoricalEvent] | Similar past events |
| confidence | float | Confidence in analysis |

### Pattern Libraries

| Library | Description | Size |
|:--------|:------------|:-----|
| supernovae | Supernova light curves | ~1000 templates |
| variable_stars | Variable star patterns | ~10000 templates |
| asteroids | Moving object patterns | ~100 templates |
| artifacts | Known artifact patterns | ~500 templates |
| unknown | Unclassified but seen | ~1000 examples |

### Matching Algorithm

```python
async def match_patterns(
    event: ProcessedEvent
) -> list[PatternMatch]:
    """Match event against pattern libraries."""
    
    matches = []
    
    for library in self.libraries:
        # Extract relevant features
        features = library.extract_features(event)
        
        # Find matches above threshold
        library_matches = library.match(
            features,
            threshold=0.5,
            max_results=10
        )
        
        matches.extend(library_matches)
    
    # Sort by confidence
    matches.sort(key=lambda m: m.confidence, reverse=True)
    
    return matches[:20]  # Top 20
```

---

## Agent 3: Anomaly Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Anomaly Agent |
| **ID** | `anomaly_agent` |
| **Version** | 1.0.0 |
| **Role** | Novelty and outlier detection |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <500ms | 1s |
| Latency (p99) | <1s | 2s |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Event to analyse |
| pattern_result | PatternAnalysis | No | Pattern agent result |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| anomaly_score | float | 0-1 novelty score |
| unusual_features | list[FeatureAnomaly] | What's unusual |
| discovery_potential | float | Likelihood of new phenomenon |
| comparison_baseline | dict | What's "normal" |

### Detection Methods

| Method | Purpose | Weight |
|:-------|:--------|:-------|
| Isolation Forest | Global outlier detection | 0.3 |
| Autoencoder | Reconstruction anomaly | 0.3 |
| Feature distribution | Per-feature outliers | 0.4 |

### Scoring

```python
def compute_anomaly_score(
    event: ProcessedEvent,
    pattern_result: PatternAnalysis
) -> float:
    """Compute composite anomaly score."""
    
    # Individual method scores
    isolation = self.isolation_forest.score(event.features)
    reconstruction = self.autoencoder.error(event.features)
    feature_score = self.feature_anomalies(event.features)
    
    # Weighted combination
    score = (
        0.3 * isolation +
        0.3 * reconstruction +
        0.4 * feature_score
    )
    
    # Boost if pattern matching failed
    if pattern_result and pattern_result.confidence < 0.5:
        score = min(1.0, score * 1.2)
    
    return score
```

---

## Agent 4: Context Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Context Agent |
| **ID** | `context_agent` |
| **Version** | 1.0.0 |
| **Role** | Historical and environmental context |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <10s | 30s |
| Latency (p99) | <30s | 60s |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Event to contextualise |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| historical_context | HistoricalContext | Past observations at location |
| environmental_context | EnvironmentalContext | Observing conditions |
| related_observations | list[Observation] | Related data |
| literature_references | list[Reference] | Relevant publications |

### Data Sources

| Source | Data | Query Latency |
|:-------|:-----|:--------------|
| Observation archive | Past observations | <5s |
| Object catalog | Known objects | <1s |
| Literature database | Publications | <10s |
| Environmental logs | Conditions | <1s |

---

## Agent 5: Synthesis Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Synthesis Agent |
| **ID** | `synthesis_agent` |
| **Version** | 1.0.0 |
| **Role** | Combine analyses into assessment |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <2s | 5s |
| Latency (p99) | <5s | 10s |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Original event |
| agent_results | dict | Yes | All agent outputs |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| assessment | Assessment | Overall assessment |
| confidence | float | Combined confidence |
| recommendation | Recommendation | What to do |
| summary | str | Human-readable summary |

### Synthesis Logic

```python
async def synthesize(
    event: ProcessedEvent,
    agent_results: dict
) -> SynthesisResult:
    """Combine agent outputs."""
    
    pattern = agent_results.get("pattern")
    anomaly = agent_results.get("anomaly")
    context = agent_results.get("context")
    
    # Resolve conflicts
    conflicts = self.detect_conflicts(agent_results)
    resolution = self.resolve_conflicts(conflicts)
    
    # Generate assessment
    assessment = self.generate_assessment(
        event=event,
        pattern=pattern,
        anomaly=anomaly,
        context=context,
        resolution=resolution
    )
    
    # Generate recommendation
    recommendation = self.generate_recommendation(assessment)
    
    return SynthesisResult(
        assessment=assessment,
        confidence=self.compute_confidence(agent_results),
        recommendation=recommendation,
        summary=self.generate_summary(assessment)
    )
```

---

## Agent 6: Coordination Agent

### Identity

| Attribute | Value |
|:----------|:------|
| **Name** | Coordination Agent |
| **ID** | `coordination_agent` |
| **Version** | 1.0.0 |
| **Role** | Multi-facility follow-up coordination |

### Performance Requirements

| Metric | Target | Hard Limit |
|:-------|:-------|:-----------|
| Latency (p50) | <1min | 5min |
| Latency (p99) | <5min | 15min |

### Inputs

| Input | Type | Required | Description |
|:------|:-----|:---------|:------------|
| event | ProcessedEvent | Yes | Event to coordinate |
| synthesis | SynthesisResult | Yes | Synthesis assessment |

### Outputs

| Output | Type | Description |
|:-------|:-----|:------------|
| observation_requests | list[Request] | Follow-up requests |
| facility_assignments | list[Assignment] | Facility assignments |
| public_alert | Alert | Community alert |

### Coordination Logic

```python
async def coordinate(
    event: ProcessedEvent,
    synthesis: SynthesisResult
) -> CoordinationPlan:
    """Plan follow-up observations."""
    
    # What observations would help?
    needed = self.determine_needed_observations(event, synthesis)
    
    # Which facilities can help?
    for obs in needed:
        capable = await self.find_capable_facilities(
            observation_type=obs.type,
            coordinates=event.coordinates,
            time_constraints=obs.time_window
        )
        obs.capable_facilities = capable
    
    # Assign and prioritise
    assignments = self.assign_facilities(needed)
    
    # Generate alert if warranted
    alert = None
    if synthesis.significance > 0.9:
        alert = self.generate_alert(event, synthesis)
    
    return CoordinationPlan(
        requests=needed,
        assignments=assignments,
        alert=alert
    )
```

---

## Communication Protocol

### Message Format

```python
@dataclass
class AgentMessage:
    message_id: str
    source_agent: str
    target_agent: str
    message_type: str
    event_id: str
    content: dict
    timestamp: datetime
    latency_budget_ms: float
    priority: int
```

### Error Handling

| Error | Response |
|:------|:---------|
| Agent timeout | Use partial results, mark incomplete |
| Agent crash | Skip agent, log error |
| Invalid output | Discard, retry if time allows |

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| System Architect | | |
| Operations Lead | | |
