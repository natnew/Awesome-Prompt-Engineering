[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Agent Design](03_agent_design.md) | [Evaluation Framework →](05_evaluation_framework.md)

# Provenance System

Design provenance tracking for scientific event detection that supports publishable discoveries.

---

## Why Provenance in Event Detection?

A detection without provenance is scientifically useless.

| Without Provenance | With Provenance |
|:-------------------|:----------------|
| "We detected a transient" | "Observation X at time T showed flux Y, classified by method Z" |
| Trust us | Verify yourself |
| Unreproducible | Reproducible |
| Unpublishable | Publication-ready |

**The standard:** Any detection your system produces should be traceable back to raw data, with every processing step documented.

---

## Provenance Requirements

### Scientific Standards

| Requirement | Description | Priority |
|:------------|:------------|:---------|
| **Raw data link** | Every detection links to source observation | Critical |
| **Processing trace** | Every transformation documented | Critical |
| **Decision audit** | Classification decisions recorded | Critical |
| **Timestamp accuracy** | Precise timing throughout | High |
| **Reproducibility** | Same input → same output | High |

### Operational Standards

| Requirement | Description | Priority |
|:------------|:------------|:---------|
| **Query efficiency** | Fast provenance lookup | High |
| **Storage efficiency** | Reasonable storage overhead | Medium |
| **Retention** | Permanent for significant events | High |

---

## Provenance Data Model

### Core Entities

```python
@dataclass
class Observation:
    """Raw observation from instrument."""
    observation_id: str
    source_facility: str
    instrument: str
    observation_time: datetime
    coordinates: SkyCoordinates
    raw_data_uri: str           # Link to raw data
    calibration_applied: str    # Calibration version
    quality_flags: list[str]

@dataclass
class DetectionEvent:
    """A detected event with full provenance."""
    event_id: str
    
    # Source
    observations: list[Observation]
    
    # Processing
    processing_steps: list[ProcessingStep]
    
    # Classification
    classification: Classification
    classification_provenance: ClassificationProvenance
    
    # Agent analysis
    agent_analyses: dict[str, AgentAnalysis]
    
    # Synthesis
    synthesis: SynthesisResult
    
    # Metadata
    created_at: datetime
    updated_at: datetime
    version: int

@dataclass
class ProcessingStep:
    """A single processing step."""
    step_id: str
    step_type: str              # filter, classify, enrich
    algorithm: str              # Algorithm name
    algorithm_version: str      # Version
    parameters: dict            # Configuration
    input_ids: list[str]        # What went in
    output_ids: list[str]       # What came out
    timestamp: datetime
    duration_ms: float
    
@dataclass
class ClassificationProvenance:
    """How classification decision was made."""
    classifier_id: str
    classifier_version: str
    input_features: dict
    decision_scores: dict       # Score per category
    decision_threshold: float
    confidence_calibration: str # Calibration method
    
@dataclass
class AgentAnalysis:
    """Analysis from a single agent."""
    agent_id: str
    agent_version: str
    input_data: dict
    output_data: dict
    confidence: float
    reasoning: list[str]        # Chain of reasoning
    timestamp: datetime
    duration_ms: float
```

### Provenance Graph

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DETECTION EVENT                                 │
│                     (Final Output)                                  │
└─────────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│  Synthesis    │       │  Agent        │       │  Agent        │
│  Result       │       │  Analysis 1   │       │  Analysis 2   │
└───────┬───────┘       └───────┬───────┘       └───────┬───────┘
        │                       │                       │
        └───────────────────────┼───────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CLASSIFICATION                                  │
│                     (Category Assignment)                           │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PROCESSING STEPS                                │
│  ┌─────────┐ → ┌─────────┐ → ┌─────────┐ → ┌─────────┐            │
│  │ Ingest  │   │ Filter  │   │ Extract │   │ Classify│            │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘            │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     RAW OBSERVATIONS                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │ Obs 1       │  │ Obs 2       │  │ Obs 3       │                 │
│  │ (raw data)  │  │ (raw data)  │  │ (raw data)  │                 │
│  └─────────────┘  └─────────────┘  └─────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Provenance Capture

### Capture Points

| Stage | What to Capture | How |
|:------|:----------------|:----|
| Ingestion | Raw observation metadata | Automatic on receipt |
| Filtering | Filter decisions, reasons | Each filter logs |
| Classification | Scores, thresholds, decision | Classifier output |
| Agent analysis | Input, output, reasoning | Agent protocol |
| Synthesis | Combined assessment | Synthesis agent |
| Routing | Where sent, when | Router logs |

### Capture Implementation

```python
class ProvenanceCapture:
    """Capture provenance during event processing."""
    
    def __init__(self, event_id: str):
        self.event_id = event_id
        self.steps = []
        self.start_time = datetime.now()
    
    @contextmanager
    def step(self, step_type: str, algorithm: str, **params):
        """Context manager for capturing a processing step."""
        step = ProcessingStep(
            step_id=generate_id(),
            step_type=step_type,
            algorithm=algorithm,
            algorithm_version=get_version(algorithm),
            parameters=params,
            input_ids=[],
            output_ids=[],
            timestamp=datetime.now(),
            duration_ms=0
        )
        
        start = time.time()
        try:
            yield step
        finally:
            step.duration_ms = (time.time() - start) * 1000
            self.steps.append(step)
    
    def record_classification(
        self, 
        classifier: str,
        features: dict,
        scores: dict,
        decision: str,
        confidence: float
    ):
        """Record classification decision."""
        self.classification_provenance = ClassificationProvenance(
            classifier_id=classifier,
            classifier_version=get_version(classifier),
            input_features=features,
            decision_scores=scores,
            decision_threshold=get_threshold(classifier),
            confidence_calibration="isotonic"
        )
    
    def record_agent_analysis(
        self,
        agent_id: str,
        input_data: dict,
        output_data: dict,
        confidence: float,
        reasoning: list[str]
    ):
        """Record agent analysis."""
        self.agent_analyses[agent_id] = AgentAnalysis(
            agent_id=agent_id,
            agent_version=get_version(agent_id),
            input_data=input_data,
            output_data=output_data,
            confidence=confidence,
            reasoning=reasoning,
            timestamp=datetime.now(),
            duration_ms=0  # Set by caller
        )
    
    def finalize(self) -> DetectionEvent:
        """Finalize provenance record."""
        return DetectionEvent(
            event_id=self.event_id,
            observations=self.observations,
            processing_steps=self.steps,
            classification=self.classification,
            classification_provenance=self.classification_provenance,
            agent_analyses=self.agent_analyses,
            synthesis=self.synthesis,
            created_at=self.start_time,
            updated_at=datetime.now(),
            version=1
        )
```

### Usage in Pipeline

```python
async def process_observation(obs: RawObservation) -> DetectionEvent:
    """Process observation with full provenance capture."""
    
    provenance = ProvenanceCapture(event_id=generate_id())
    provenance.add_observation(obs)
    
    # Filtering with provenance
    with provenance.step("filter", "quality_filter") as step:
        step.input_ids.append(obs.observation_id)
        filtered = quality_filter(obs)
        step.output_ids.append(filtered.id)
    
    # Classification with provenance
    with provenance.step("classify", "ml_classifier_v2") as step:
        features = extract_features(filtered)
        scores = classifier.predict_proba(features)
        decision = classifier.predict(features)
        
        provenance.record_classification(
            classifier="ml_classifier_v2",
            features=features,
            scores=scores,
            decision=decision,
            confidence=max(scores.values())
        )
    
    # Agent analysis with provenance
    for agent in selected_agents:
        result = await agent.analyse(filtered)
        provenance.record_agent_analysis(
            agent_id=agent.id,
            input_data=filtered.to_dict(),
            output_data=result.to_dict(),
            confidence=result.confidence,
            reasoning=result.reasoning
        )
    
    return provenance.finalize()
```

---

## Provenance Storage

### Storage Schema

```sql
-- Core events table
CREATE TABLE detection_events (
    event_id VARCHAR PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    version INTEGER NOT NULL,
    classification VARCHAR NOT NULL,
    confidence FLOAT NOT NULL,
    significance FLOAT NOT NULL
);

-- Observations linked to events
CREATE TABLE event_observations (
    event_id VARCHAR REFERENCES detection_events(event_id),
    observation_id VARCHAR NOT NULL,
    source_facility VARCHAR NOT NULL,
    observation_time TIMESTAMP NOT NULL,
    raw_data_uri VARCHAR NOT NULL,
    PRIMARY KEY (event_id, observation_id)
);

-- Processing steps
CREATE TABLE processing_steps (
    step_id VARCHAR PRIMARY KEY,
    event_id VARCHAR REFERENCES detection_events(event_id),
    step_type VARCHAR NOT NULL,
    algorithm VARCHAR NOT NULL,
    algorithm_version VARCHAR NOT NULL,
    parameters JSONB,
    timestamp TIMESTAMP NOT NULL,
    duration_ms FLOAT
);

-- Classification provenance
CREATE TABLE classification_provenance (
    event_id VARCHAR PRIMARY KEY REFERENCES detection_events(event_id),
    classifier_id VARCHAR NOT NULL,
    classifier_version VARCHAR NOT NULL,
    input_features JSONB NOT NULL,
    decision_scores JSONB NOT NULL,
    decision_threshold FLOAT NOT NULL
);

-- Agent analyses
CREATE TABLE agent_analyses (
    event_id VARCHAR REFERENCES detection_events(event_id),
    agent_id VARCHAR NOT NULL,
    agent_version VARCHAR NOT NULL,
    input_data JSONB,
    output_data JSONB,
    confidence FLOAT,
    reasoning JSONB,
    timestamp TIMESTAMP,
    PRIMARY KEY (event_id, agent_id)
);

-- Indexes for common queries
CREATE INDEX idx_events_classification ON detection_events(classification);
CREATE INDEX idx_events_significance ON detection_events(significance);
CREATE INDEX idx_events_created ON detection_events(created_at);
CREATE INDEX idx_observations_time ON event_observations(observation_time);
```

### Retention Policy

| Event Category | Retention | Storage Tier |
|:---------------|:----------|:-------------|
| Critical | Permanent | Hot |
| Significant | Permanent | Warm |
| Interesting | 5 years | Warm |
| Routine | 1 year | Cold |
| Rejected | 30 days | Cold |

---

## Provenance Queries

### Common Query Patterns

```python
class ProvenanceQuery:
    """Query provenance data."""
    
    async def get_full_provenance(
        self, 
        event_id: str
    ) -> DetectionEvent:
        """Get complete provenance for an event."""
        # Fetch all related records
        event = await self.db.fetch_event(event_id)
        observations = await self.db.fetch_observations(event_id)
        steps = await self.db.fetch_processing_steps(event_id)
        classification = await self.db.fetch_classification(event_id)
        analyses = await self.db.fetch_agent_analyses(event_id)
        
        return DetectionEvent(
            event_id=event_id,
            observations=observations,
            processing_steps=steps,
            classification_provenance=classification,
            agent_analyses=analyses,
            **event
        )
    
    async def trace_to_raw_data(
        self, 
        event_id: str
    ) -> list[str]:
        """Get raw data URIs for an event."""
        observations = await self.db.fetch_observations(event_id)
        return [obs.raw_data_uri for obs in observations]
    
    async def get_processing_history(
        self, 
        event_id: str
    ) -> list[ProcessingStep]:
        """Get ordered processing steps."""
        steps = await self.db.fetch_processing_steps(event_id)
        return sorted(steps, key=lambda s: s.timestamp)
    
    async def find_events_by_algorithm(
        self, 
        algorithm: str,
        version: str = None
    ) -> list[str]:
        """Find events processed by specific algorithm."""
        return await self.db.query(
            "SELECT DISTINCT event_id FROM processing_steps "
            "WHERE algorithm = $1 AND ($2 IS NULL OR algorithm_version = $2)",
            algorithm, version
        )
```

### Reproducibility Verification

```python
async def verify_reproducibility(
    event_id: str,
    provenance: DetectionEvent
) -> ReproducibilityReport:
    """Verify that processing can be reproduced."""
    
    issues = []
    
    # Check algorithm versions still available
    for step in provenance.processing_steps:
        if not await algorithm_available(step.algorithm, step.algorithm_version):
            issues.append(f"Algorithm {step.algorithm}:{step.algorithm_version} not available")
    
    # Check raw data accessible
    for obs in provenance.observations:
        if not await raw_data_accessible(obs.raw_data_uri):
            issues.append(f"Raw data not accessible: {obs.raw_data_uri}")
    
    # Attempt reproduction if possible
    if not issues:
        reproduced = await reproduce_processing(provenance)
        if reproduced.event_id != event_id:
            issues.append("Reproduction produced different result")
    
    return ReproducibilityReport(
        event_id=event_id,
        reproducible=len(issues) == 0,
        issues=issues
    )
```

---

## Provenance Presentation

### Human-Readable Format

```markdown
# Detection Event: EVT-2024-001234

## Summary
- **Classification:** Supernova candidate (confidence: 0.94)
- **Significance:** High (score: 0.87)
- **Detected:** 2024-01-15 03:24:17 UTC

## Source Observations
| ID | Facility | Time | Coordinates |
|:---|:---------|:-----|:------------|
| OBS-001 | Telescope-A | 03:24:15 | RA 12.345, Dec -45.678 |
| OBS-002 | Telescope-A | 03:24:16 | RA 12.345, Dec -45.678 |

## Processing Pipeline
1. **Ingestion** (03:24:17.001)
   - Algorithm: standard_ingest v2.3.1
   - Duration: 12ms

2. **Quality Filter** (03:24:17.015)
   - Algorithm: quality_filter v1.8.0
   - Result: PASS
   - Duration: 45ms

3. **Classification** (03:24:17.062)
   - Algorithm: ml_classifier v2.1.0
   - Scores: {supernova: 0.94, asteroid: 0.03, artifact: 0.03}
   - Threshold: 0.5
   - Duration: 120ms

## Agent Analyses
### Pattern Agent (v1.2.0)
- **Confidence:** 0.91
- **Matched patterns:** Type Ia supernova template
- **Reasoning:** Light curve shape matches Type Ia; no prior object at location

### Anomaly Agent (v1.1.0)
- **Anomaly score:** 0.23 (low - consistent with known patterns)
- **Unusual features:** None detected

## Raw Data Access
- OBS-001: s3://archive/2024/01/15/telescope-a/obs-001.fits
- OBS-002: s3://archive/2024/01/15/telescope-a/obs-002.fits
```

### Machine-Readable Export

```json
{
  "event_id": "EVT-2024-001234",
  "classification": "supernova_candidate",
  "confidence": 0.94,
  "observations": [
    {
      "observation_id": "OBS-001",
      "source_facility": "Telescope-A",
      "raw_data_uri": "s3://archive/2024/01/15/telescope-a/obs-001.fits"
    }
  ],
  "processing_steps": [
    {
      "step_type": "ingest",
      "algorithm": "standard_ingest",
      "algorithm_version": "2.3.1",
      "timestamp": "2024-01-15T03:24:17.001Z"
    }
  ],
  "classification_provenance": {
    "classifier_id": "ml_classifier",
    "classifier_version": "2.1.0",
    "decision_scores": {
      "supernova": 0.94,
      "asteroid": 0.03,
      "artifact": 0.03
    }
  }
}
```

---

## Your Task

### Exercise 1: Schema Design

Design your complete provenance schema:
1. What entities do you need?
2. What relationships between entities?
3. What must be captured vs. optional?
4. How do you handle schema evolution?

### Exercise 2: Capture Strategy

Design provenance capture:
1. What are your capture points?
2. How do you minimize overhead?
3. How do you handle capture failures?
4. How do you ensure completeness?

### Exercise 3: Query Patterns

Design provenance queries:
1. What queries do scientists need?
2. What queries do operators need?
3. How do you optimize common queries?
4. How do you support reproducibility checks?

### Exercise 4: Presentation

Design provenance presentation:
1. What do humans need to see?
2. What export formats are required?
3. How do you balance detail vs. clarity?
4. How do you support publication?

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Provenance schema** | Data model specification |
| **Capture design** | Capture points and implementation |
| **Query patterns** | Common queries and optimizations |
| **Export formats** | Human and machine-readable |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Agent Design](03_agent_design.md) | [Project Overview](README.md) | [Evaluation Framework →](05_evaluation_framework.md) |
