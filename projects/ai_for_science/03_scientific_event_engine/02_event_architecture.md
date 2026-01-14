[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Problem Framing](01_problem_framing.md) | [Agent Design →](03_agent_design.md)

# Event Architecture

Design the streaming infrastructure that processes scientific observations at scale.

---

## Stream Processing Fundamentals

### Why Streaming?

Scientific instruments produce continuous data, not discrete batches:

| Approach | Latency | Throughput | Use Case |
|:---------|:--------|:-----------|:---------|
| **Batch** | Hours | High | Archival analysis |
| **Micro-batch** | Minutes | High | Near-real-time |
| **Stream** | Seconds | Variable | Real-time alerts |

For time-critical events, streaming is essential.

### Stream Processing Model

```
                    TIME →
                    
Observation:    ●────●────●────●────●────●────●────●────●────●
                     │
                     ▼
Ingestion:      [Window 1][Window 2][Window 3][Window 4][...]
                     │
                     ▼
Processing:     Filter → Classify → Route
                     │
                     ▼
Output:         Alert ─────────────────────→ Queue ──→ Archive
```

---

## Pipeline Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │ Telescope A │ │ Telescope B │ │ Satellite   │ │ Archive     │   │
│  │  (optical)  │ │  (radio)    │ │  (X-ray)    │ │ (historical)│   │
│  └──────┬──────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘   │
└─────────┼───────────────┼───────────────┼───────────────┼───────────┘
          │               │               │               │
          └───────────────┴───────────────┴───────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  INGESTION LAYER                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Message Queue (Kafka/Pulsar)                               │   │
│  │  - Buffering                                                │   │
│  │  - Durability                                               │   │
│  │  - Replay capability                                        │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PROCESSING LAYER                                                   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │
│  │  Validator  │→│   Filter    │→│ Classifier  │→│   Router    │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  ALERT SYSTEM   │   │  ANALYSIS QUEUE │   │    ARCHIVE      │
│  (Critical)     │   │  (Interesting)  │   │  (All events)   │
└─────────────────┘   └─────────────────┘   └─────────────────┘
```

---

## Ingestion Layer

### Message Schema

```python
@dataclass
class RawObservation:
    """Raw observation from instrument."""
    
    # Identity
    observation_id: str           # Unique identifier
    source_facility: str          # Which telescope/instrument
    
    # Timing
    observation_time: datetime    # When observed
    received_time: datetime       # When received
    
    # Position
    coordinates: SkyCoordinates   # RA/Dec or equivalent
    position_uncertainty: float   # Arcseconds
    
    # Measurement
    measurement_type: str         # Brightness, spectrum, etc.
    measurement_value: float      # The measurement
    measurement_uncertainty: float
    
    # Metadata
    instrument_config: dict       # Instrument settings
    environmental_conditions: dict # Weather, seeing, etc.
    quality_flags: list[str]      # Known issues

@dataclass
class SkyCoordinates:
    """Celestial coordinates."""
    ra: float                     # Right ascension (degrees)
    dec: float                    # Declination (degrees)
    epoch: str = "J2000"          # Coordinate epoch
```

### Ingestion Guarantees

| Guarantee | Implementation | Rationale |
|:----------|:---------------|:----------|
| **At-least-once delivery** | Message acknowledgment | No data loss |
| **Ordering within partition** | Partition by source | Temporal consistency |
| **Durability** | Persistent storage | Replay capability |
| **Backpressure handling** | Queue depth monitoring | Graceful degradation |

### Quality Gates

Before processing, validate:

```python
def validate_observation(obs: RawObservation) -> ValidationResult:
    """Validate observation before processing."""
    issues = []
    
    # Required fields
    if not obs.observation_id:
        issues.append("Missing observation_id")
    
    # Coordinate validity
    if not (0 <= obs.coordinates.ra < 360):
        issues.append(f"Invalid RA: {obs.coordinates.ra}")
    if not (-90 <= obs.coordinates.dec <= 90):
        issues.append(f"Invalid Dec: {obs.coordinates.dec}")
    
    # Timing validity
    if obs.observation_time > obs.received_time:
        issues.append("Observation time in future")
    
    # Measurement validity
    if obs.measurement_uncertainty <= 0:
        issues.append("Invalid uncertainty")
    
    return ValidationResult(
        valid=len(issues) == 0,
        issues=issues
    )
```

---

## Filtering Layer

### Filter Stages

```
Raw Observations
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 1: Quality Filter                                            │
│  - Remove invalid/corrupt observations                             │
│  - Flag instrumental artifacts                                     │
│  Expected: ~20% rejected                                           │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 2: Known Object Filter                                       │
│  - Cross-match against catalog of known objects                    │
│  - Identify known variable stars, asteroids, etc.                  │
│  Expected: ~60% matched to known                                   │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│  STAGE 3: Artifact Filter                                           │
│  - Satellite trails                                                │
│  - Cosmic ray hits                                                 │
│  - Hot pixels, chip edges                                          │
│  Expected: ~10% of remainder rejected                              │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
Candidate Events (~10% of original)
```

### Filter Implementation

```python
class FilterPipeline:
    """Multi-stage filter pipeline."""
    
    def __init__(self):
        self.filters = [
            QualityFilter(),
            KnownObjectFilter(catalog=load_catalog()),
            ArtifactFilter(models=load_artifact_models()),
        ]
    
    async def process(
        self, 
        observation: RawObservation
    ) -> FilterResult:
        """Process observation through filter pipeline."""
        
        for filter in self.filters:
            result = await filter.apply(observation)
            
            if result.action == "REJECT":
                return FilterResult(
                    passed=False,
                    rejected_by=filter.name,
                    reason=result.reason
                )
            
            if result.action == "FLAG":
                observation.quality_flags.append(result.flag)
        
        return FilterResult(passed=True)

class KnownObjectFilter:
    """Cross-match against known object catalog."""
    
    def __init__(self, catalog):
        self.catalog = catalog
        self.match_radius = 2.0  # arcseconds
    
    async def apply(
        self, 
        observation: RawObservation
    ) -> FilterAction:
        """Check if observation matches known object."""
        
        matches = self.catalog.cone_search(
            ra=observation.coordinates.ra,
            dec=observation.coordinates.dec,
            radius=self.match_radius
        )
        
        if matches:
            best_match = matches[0]
            return FilterAction(
                action="FLAG",
                flag=f"known_object:{best_match.object_id}",
                metadata={"matched_object": best_match}
            )
        
        return FilterAction(action="PASS")
```

---

## Classification Layer

### Classification Categories

| Category | Definition | Downstream Action |
|:---------|:-----------|:------------------|
| `routine` | Expected variation of known object | Archive only |
| `known_type` | Matches known transient class | Log, periodic review |
| `interesting` | Unusual, warrants attention | Queue for review |
| `significant` | Likely important, high priority | Priority review |
| `critical` | Requires immediate action | Immediate alert |
| `unknown` | Can't classify confidently | Manual triage |

### Classification Pipeline

```python
class ClassificationPipeline:
    """Multi-stage classification."""
    
    def __init__(self):
        self.classifiers = [
            RuleBasedClassifier(),      # Fast, known patterns
            MLClassifier(),              # Learned patterns
            AnomalyDetector(),           # Novelty detection
            ConfidenceCalibrator(),      # Calibrate scores
        ]
    
    async def classify(
        self, 
        observation: ProcessedObservation
    ) -> Classification:
        """Classify observation."""
        
        # Collect all classifier outputs
        predictions = []
        for classifier in self.classifiers:
            pred = await classifier.predict(observation)
            predictions.append(pred)
        
        # Combine predictions
        combined = self.combine_predictions(predictions)
        
        # Assign final category based on confidence
        category = self.assign_category(combined)
        
        return Classification(
            category=category,
            confidence=combined.confidence,
            supporting_evidence=combined.evidence,
            classifier_breakdown=predictions
        )
    
    def assign_category(self, combined: CombinedPrediction) -> str:
        """Assign category based on scores."""
        
        # Critical: Very high confidence + time-critical
        if combined.urgency > 0.9 and combined.significance > 0.9:
            return "critical"
        
        # Significant: High confidence of importance
        if combined.significance > 0.8:
            return "significant"
        
        # Interesting: Worth human attention
        if combined.significance > 0.5:
            return "interesting"
        
        # Known type: Matches known class
        if combined.known_type_match > 0.8:
            return "known_type"
        
        # Unknown: Can't classify
        if combined.confidence < 0.5:
            return "unknown"
        
        # Routine: Everything else
        return "routine"
```

### Anomaly Detection

For truly novel events:

```python
class AnomalyDetector:
    """Detect observations that don't fit known patterns."""
    
    def __init__(self, model):
        self.model = model  # Trained on "normal" observations
    
    async def predict(
        self, 
        observation: ProcessedObservation
    ) -> AnomalyPrediction:
        """Assess how anomalous this observation is."""
        
        # Extract features
        features = self.extract_features(observation)
        
        # Score against model of normal
        anomaly_score = self.model.score(features)
        
        # Identify which features are unusual
        unusual_features = self.identify_unusual(features)
        
        return AnomalyPrediction(
            anomaly_score=anomaly_score,
            unusual_features=unusual_features,
            nearest_normal=self.find_nearest_normal(features)
        )
```

---

## Routing Layer

### Routing Rules

```python
class EventRouter:
    """Route classified events to appropriate destinations."""
    
    async def route(
        self, 
        event: ClassifiedEvent
    ) -> RoutingDecision:
        """Route event based on classification."""
        
        destinations = []
        
        # Critical: Immediate alert
        if event.category == "critical":
            destinations.append(AlertDestination(
                channel="immediate",
                priority=1,
                requires_ack=True
            ))
        
        # Significant: Priority queue
        if event.category in ["critical", "significant"]:
            destinations.append(QueueDestination(
                queue="priority_review",
                priority=event.significance_score
            ))
        
        # Interesting: Standard review queue
        if event.category == "interesting":
            destinations.append(QueueDestination(
                queue="standard_review",
                priority=event.significance_score
            ))
        
        # Unknown: Manual triage
        if event.category == "unknown":
            destinations.append(QueueDestination(
                queue="manual_triage",
                priority=0.5
            ))
        
        # All events: Archive
        destinations.append(ArchiveDestination(
            retention="permanent"
        ))
        
        return RoutingDecision(destinations=destinations)
```

### Alert System

```python
class AlertSystem:
    """Manage alerts for critical events."""
    
    async def send_alert(
        self, 
        event: ClassifiedEvent,
        destination: AlertDestination
    ):
        """Send alert through appropriate channels."""
        
        alert = Alert(
            event_id=event.event_id,
            category=event.category,
            summary=self.format_summary(event),
            coordinates=event.coordinates,
            urgency=destination.priority,
            timestamp=datetime.now(),
            requires_acknowledgment=destination.requires_ack
        )
        
        # Send through channels
        for channel in self.get_channels(destination):
            await channel.send(alert)
        
        # Log alert
        await self.log_alert(alert)
        
        # Start acknowledgment timer if required
        if destination.requires_ack:
            await self.start_ack_timer(alert)
```

---

## Scalability Considerations

### Horizontal Scaling

```
                    Load Balancer
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │ Worker 1  │   │ Worker 2  │   │ Worker 3  │
    │           │   │           │   │           │
    │ Filter    │   │ Filter    │   │ Filter    │
    │ Classify  │   │ Classify  │   │ Classify  │
    │ Route     │   │ Route     │   │ Route     │
    └───────────┘   └───────────┘   └───────────┘
          │               │               │
          └───────────────┼───────────────┘
                          │
                          ▼
                   Output Queues
```

### Partition Strategy

| Data | Partition Key | Rationale |
|:-----|:--------------|:----------|
| Raw observations | Source facility | Maintain source ordering |
| Classified events | Sky region | Related events together |
| Alerts | Priority | Process critical first |

### Backpressure Handling

```python
class BackpressureController:
    """Manage system load."""
    
    async def check_pressure(self) -> PressureLevel:
        """Assess current system pressure."""
        
        queue_depth = await self.get_queue_depth()
        processing_lag = await self.get_processing_lag()
        
        if queue_depth > self.critical_threshold:
            return PressureLevel.CRITICAL
        if processing_lag > self.high_threshold:
            return PressureLevel.HIGH
        if processing_lag > self.moderate_threshold:
            return PressureLevel.MODERATE
        return PressureLevel.NORMAL
    
    async def apply_backpressure(self, level: PressureLevel):
        """Apply appropriate backpressure measures."""
        
        if level == PressureLevel.CRITICAL:
            # Pause non-essential processing
            await self.pause_routine_analysis()
            # Alert operators
            await self.alert_operators()
        
        if level >= PressureLevel.HIGH:
            # Reduce classification depth
            await self.enable_fast_mode()
            # Scale up if possible
            await self.request_scaling()
```

---

## Your Task

### Exercise 1: Message Schema Design

Design your complete event schema:
1. What fields are required?
2. What metadata is essential for provenance?
3. How do you handle different instrument types?
4. How do you version the schema?

### Exercise 2: Filter Configuration

Design your filter pipeline:
1. What filters do you need?
2. In what order?
3. What are the thresholds?
4. How do you handle edge cases?

### Exercise 3: Classification Strategy

Design your classification approach:
1. What categories do you need?
2. How do you combine multiple classifiers?
3. How do you handle low confidence?
4. How do you detect true novelty?

### Exercise 4: Scaling Strategy

Design for scale:
1. What's your partition strategy?
2. How do you handle burst traffic?
3. How do you maintain latency under load?
4. What do you sacrifice when overloaded?

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Event schema** | `artifacts/event_schema.md` |
| **Filter design** | Pipeline specification |
| **Classification rules** | Category definitions, thresholds |
| **Scaling strategy** | Partitioning, backpressure |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Problem Framing](01_problem_framing.md) | [Project Overview](README.md) | [Agent Design →](03_agent_design.md) |
