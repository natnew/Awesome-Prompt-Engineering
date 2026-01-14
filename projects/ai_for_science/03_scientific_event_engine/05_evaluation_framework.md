[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Provenance System](04_provenance_system.md) | [Synthesis →](synthesis.md)

# Evaluation Framework

Design evaluation that measures what matters: discoveries found, attention well-spent, science accelerated.

---

## The Evaluation Challenge

Event detection evaluation differs from typical ML evaluation:

| Typical ML | Event Detection |
|:-----------|:----------------|
| Accuracy on test set | Did we find the supernova? |
| Balanced metrics | Asymmetric costs |
| Static evaluation | Continuous monitoring |
| Single model | Complex pipeline |

Your evaluation must capture what scientists care about: **Did we catch the important events? Did we waste their time?**

---

## Evaluation Dimensions

### Dimension 1: Detection Sensitivity

**Core question:** Do we catch the events that matter?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Critical recall | Critical events detected / All critical events | >99.9% |
| Significant recall | Significant events detected / All significant events | >99% |
| Interesting recall | Interesting events detected / All interesting events | >95% |

**Why asymmetric targets:** Missing a critical event (e.g., nearby supernova) is catastrophic and irreversible. Missing an interesting event is unfortunate but recoverable.

### Dimension 2: Specificity / Precision

**Core question:** Do we respect scientists' attention?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Alert precision | True critical / All critical alerts | >50% |
| Queue precision | True interesting / All queued | >10% |
| False positive rate | False alerts / All events | <0.1% |

**Why these targets:** Scientists can handle reviewing 10 events to find 1 real one. They can't handle 1000:1.

### Dimension 3: Latency

**Core question:** Are alerts timely enough to act on?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Critical latency | Time from observation to alert | <5 min (p99) |
| Significant latency | Time from observation to queue | <30 min (p99) |
| Processing latency | Time through pipeline | <1 min (p50) |

### Dimension 4: Classification Accuracy

**Core question:** Are our categories correct?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Category accuracy | Correct category / All classified | >90% |
| Confidence calibration | ECE across categories | <0.1 |
| Unknown detection | True unknowns flagged as unknown | >80% |

### Dimension 5: Provenance Completeness

**Core question:** Can detections support publications?

| Metric | Definition | Target |
|:-------|:-----------|:-------|
| Raw data linkage | Events with raw data link | 100% |
| Processing trace | Events with complete trace | 100% |
| Reproducibility | Events that can be reproduced | >99% |

---

## Evaluation Methods

### Method 1: Injection Testing

Inject known events into the stream to test detection:

```python
class InjectionTester:
    """Test detection with injected events."""
    
    def __init__(self, injection_library: dict):
        """
        injection_library: {
            "critical": [list of critical event templates],
            "significant": [list of significant templates],
            ...
        }
        """
        self.library = injection_library
        self.injected = {}
    
    async def inject_event(
        self, 
        category: str,
        stream: EventStream
    ) -> str:
        """Inject a synthetic event."""
        template = random.choice(self.library[category])
        event = self.synthesize_event(template)
        
        # Record injection
        injection_id = generate_id()
        self.injected[injection_id] = {
            "event": event,
            "category": category,
            "injected_at": datetime.now()
        }
        
        # Inject into stream
        await stream.inject(event, metadata={"injection_id": injection_id})
        
        return injection_id
    
    async def check_detection(
        self, 
        injection_id: str,
        timeout: float = 300  # 5 minutes
    ) -> DetectionResult:
        """Check if injected event was detected."""
        injection = self.injected[injection_id]
        deadline = injection["injected_at"] + timedelta(seconds=timeout)
        
        while datetime.now() < deadline:
            detection = await self.find_detection(injection["event"])
            if detection:
                return DetectionResult(
                    detected=True,
                    latency=(detection.detected_at - injection["injected_at"]).total_seconds(),
                    category_correct=(detection.category == injection["category"]),
                    detection=detection
                )
            await asyncio.sleep(1)
        
        return DetectionResult(detected=False)
    
    async def run_injection_suite(
        self,
        n_per_category: int = 100
    ) -> InjectionReport:
        """Run full injection test suite."""
        results = defaultdict(list)
        
        for category in self.library.keys():
            for _ in range(n_per_category):
                injection_id = await self.inject_event(category)
                result = await self.check_detection(injection_id)
                results[category].append(result)
        
        return self.compile_report(results)
```

### Method 2: Historical Replay

Replay historical data with known events:

```python
class HistoricalReplay:
    """Replay historical data for evaluation."""
    
    def __init__(self, known_events: list[KnownEvent]):
        """
        known_events: List of historically confirmed events
        with their observation data.
        """
        self.known_events = {e.event_id: e for e in known_events}
    
    async def replay_period(
        self,
        start: datetime,
        end: datetime
    ) -> ReplayReport:
        """Replay a historical period."""
        
        # Get all observations from period
        observations = await self.archive.get_observations(start, end)
        
        # Get known events from period
        period_events = [
            e for e in self.known_events.values()
            if start <= e.discovery_time <= end
        ]
        
        # Run through pipeline
        detections = []
        for obs in observations:
            result = await self.pipeline.process(obs)
            if result.detected:
                detections.append(result)
        
        # Compare to known events
        return self.evaluate_replay(detections, period_events)
    
    def evaluate_replay(
        self,
        detections: list,
        known_events: list
    ) -> ReplayReport:
        """Evaluate replay results."""
        
        # Match detections to known events
        matches = self.match_detections(detections, known_events)
        
        # Calculate metrics
        recall = len(matches) / len(known_events) if known_events else 1.0
        
        # Check for false positives
        false_positives = [
            d for d in detections
            if d not in [m.detection for m in matches]
        ]
        
        return ReplayReport(
            period_start=start,
            period_end=end,
            known_events=len(known_events),
            detections=len(detections),
            matches=len(matches),
            recall=recall,
            false_positives=len(false_positives)
        )
```

### Method 3: Real-Time Monitoring

Continuous monitoring of production system:

```python
class RealTimeMonitor:
    """Monitor production system metrics."""
    
    def __init__(self):
        self.metrics = MetricsCollector()
    
    async def record_detection(self, detection: Detection):
        """Record a detection for metrics."""
        
        # Latency
        latency = (detection.detected_at - detection.observation_time).total_seconds()
        self.metrics.record("latency", latency, tags={"category": detection.category})
        
        # Volume
        self.metrics.increment("detections", tags={"category": detection.category})
        
        # Confidence
        self.metrics.record("confidence", detection.confidence, tags={"category": detection.category})
    
    async def record_human_review(
        self,
        detection: Detection,
        review: HumanReview
    ):
        """Record human review result."""
        
        correct = review.confirmed_category == detection.category
        
        self.metrics.increment(
            "reviews",
            tags={
                "category": detection.category,
                "correct": str(correct)
            }
        )
        
        # Update precision estimates
        self.update_precision_estimate(detection.category, correct)
    
    def get_current_metrics(self) -> dict:
        """Get current metric values."""
        return {
            "latency_p50": self.metrics.percentile("latency", 50),
            "latency_p99": self.metrics.percentile("latency", 99),
            "detection_rate": self.metrics.rate("detections", window="1h"),
            "precision_by_category": self.get_precision_estimates(),
        }
```

### Method 4: Scientist Feedback

Structured feedback from scientists:

```python
@dataclass
class ScientistFeedback:
    """Feedback from scientist on detection."""
    
    detection_id: str
    reviewer: str
    timestamp: datetime
    
    # Core assessment
    true_positive: bool              # Was this a real event?
    category_correct: bool           # Right category?
    correct_category: str            # If wrong, what should it be?
    
    # Quality assessment
    alert_value: int                 # 1-5: Was alert worthwhile?
    information_quality: int         # 1-5: Was provided info useful?
    provenance_adequate: bool        # Could you verify the detection?
    
    # Free text
    comments: str
```

---

## Test Case Design

### Test Categories

#### Category 1: Known Event Types

Events with known correct classification:

```yaml
- id: KE_001
  type: "Type Ia Supernova"
  template: "sn_ia_template_v2"
  expected_category: "critical"
  expected_latency: "<5min"
  
- id: KE_002
  type: "Known variable star"
  template: "variable_rr_lyrae"
  expected_category: "routine"
```

#### Category 2: Edge Cases

Difficult or ambiguous events:

```yaml
- id: EC_001
  description: "Faint transient near detection threshold"
  challenge: "Low SNR"
  expected_behavior: "Flag for review with appropriate uncertainty"

- id: EC_002
  description: "Event resembling both asteroid and transient"
  challenge: "Ambiguous classification"
  expected_behavior: "Flag ambiguity, suggest both possibilities"
```

#### Category 3: Adversarial Cases

Designed to stress-test the system:

```yaml
- id: ADV_001
  description: "Artifact mimicking transient"
  challenge: "False positive resistance"
  expected_behavior: "Correctly reject"

- id: ADV_002
  description: "Unusual but real transient"
  challenge: "Novelty detection"
  expected_behavior: "Flag as unknown/interesting"
```

#### Category 4: Latency Tests

Time-critical scenarios:

```yaml
- id: LAT_001
  description: "Critical event during high load"
  challenge: "Maintain latency under pressure"
  expected_behavior: "Alert within 5 minutes despite load"
```

---

## Metrics Dashboard

### Summary View

```
┌─────────────────────────────────────────────────────────────────────┐
│  EVENT DETECTION SYSTEM - METRICS DASHBOARD                        │
│  Last updated: 2024-01-15 10:30:00 UTC                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  DETECTION PERFORMANCE                                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐  │
│  │ Critical    │ │ Significant │ │ Interesting │ │ Queue       │  │
│  │ Recall      │ │ Recall      │ │ Recall      │ │ Precision   │  │
│  │   99.8%     │ │   98.5%     │ │   94.2%     │ │   12.3%     │  │
│  │   ✓         │ │   ✓         │ │   ⚠         │ │   ✓         │  │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘  │
│                                                                     │
│  LATENCY (last 24h)                                                │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Critical:  p50=42s  p99=3.2min  ✓                           │  │
│  │ Significant: p50=8min  p99=22min  ✓                         │  │
│  │ Processing: p50=0.8s  p99=4.2s  ✓                           │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  VOLUME (last 24h)                                                 │
│  Total processed: 10,234,567                                       │
│  Critical alerts: 2                                                │
│  Significant: 45                                                   │
│  Interesting: 892                                                  │
│  Routine: 9,845,234                                               │
│  Rejected: 388,394                                                │
│                                                                     │
│  RECENT ALERTS                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ 10:24 CRITICAL EVT-001234 Supernova candidate RA 12.3 Dec -45│  │
│  │ 09:15 SIGNIFICANT EVT-001198 Unusual transient              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Alert Thresholds

| Metric | Warning | Critical |
|:-------|:--------|:---------|
| Critical recall | <99.5% | <99% |
| Latency p99 (critical) | >4min | >5min |
| Queue depth | >10,000 | >50,000 |
| Processing errors | >0.1% | >1% |
| Injection test failures | Any | Multiple |

---

## Evaluation Cadence

| Evaluation | Frequency | Scope |
|:-----------|:----------|:------|
| Real-time monitoring | Continuous | All metrics |
| Injection testing | Hourly | Sample injections |
| Full injection suite | Daily | All categories |
| Historical replay | Weekly | Selected periods |
| Expert review | Monthly | Sampled detections |
| Adversarial testing | Quarterly | Full adversarial suite |

---

## Your Task

### Exercise 1: Metric Selection

Design your metric set:
1. What are your primary metrics?
2. What are acceptable targets?
3. How do you handle metric conflicts?
4. What triggers alerts?

### Exercise 2: Test Suite

Design your test suite:
1. What event types must you test?
2. How do you generate test events?
3. How many tests per category?
4. How do you handle evolving event types?

### Exercise 3: Monitoring Design

Design real-time monitoring:
1. What do you monitor continuously?
2. What are your alert thresholds?
3. How do you visualize metrics?
4. How do you detect degradation?

### Exercise 4: Feedback Loop

Design scientist feedback:
1. How do you collect feedback?
2. How do you incorporate it?
3. How do you close the loop?
4. How do you measure improvement?

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Metrics specification** | `artifacts/detection_thresholds.md` |
| **Test suite** | Event categories, templates |
| **Monitoring design** | Dashboard, alerts |
| **Feedback system** | Collection and integration |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Provenance System](04_provenance_system.md) | [Project Overview](README.md) | [Synthesis →](synthesis.md) |
