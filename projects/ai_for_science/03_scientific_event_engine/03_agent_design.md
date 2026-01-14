[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Event Architecture](02_event_architecture.md) | [Provenance System →](04_provenance_system.md)

# Agent Design

Design specialised agents that collaborate on scientific event analysis.

---

## Multi-Agent Analysis System

### Why Multi-Agent?

Event analysis requires different expertise applied in sequence:

| Task | Expertise Needed | Time Constraint |
|:-----|:-----------------|:----------------|
| Initial triage | Broad pattern recognition | Milliseconds |
| Pattern matching | Domain-specific knowledge | Seconds |
| Anomaly assessment | Statistical expertise | Seconds |
| Context gathering | Historical knowledge | Minutes |
| Follow-up coordination | Operational awareness | Minutes |

No single agent handles all of these well. Specialisation enables:
- **Speed** — Fast agents for time-critical decisions
- **Depth** — Thorough agents for complex analysis
- **Modularity** — Upgrade agents independently
- **Reliability** — Graceful degradation if one agent fails

---

## Agent Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CLASSIFIED EVENT                                │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  TRIAGE AGENT                                                       │
│  - Initial assessment                                              │
│  - Priority assignment                                             │
│  - Agent routing                                                   │
│  Latency target: <100ms                                            │
└─────────────────────────────────────────────────────────────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  PATTERN AGENT  │   │  ANOMALY AGENT  │   │  CONTEXT AGENT  │
│                 │   │                 │   │                 │
│  Known patterns │   │  Novel signals  │   │  Historical     │
│  Classification │   │  Outlier score  │   │  context        │
│                 │   │                 │   │                 │
│  <1 second      │   │  <1 second      │   │  <30 seconds    │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SYNTHESIS AGENT                                                    │
│  - Combine agent outputs                                           │
│  - Generate assessment                                             │
│  - Recommend actions                                               │
└─────────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  COORDINATION AGENT (for significant events)                        │
│  - Multi-facility follow-up                                        │
│  - Observation requests                                            │
│  - Community alerts                                                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Agent 1: Triage Agent

### Purpose
Rapid initial assessment and routing.

### Design Philosophy

The Triage Agent is optimised for **speed over depth**. It makes fast decisions about where to route events for more detailed analysis.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Priority assignment | How urgent is this event? |
| Agent routing | Which agents should analyse this? |
| Quick screening | Obvious false positives/negatives |
| Load balancing | Don't overwhelm downstream agents |

### Specification

```yaml
triage_agent:
  role: "Rapid initial assessment"
  
  inputs:
    - event: ClassifiedEvent
    
  outputs:
    - priority: PriorityLevel
    - agents_to_invoke: list[str]
    - quick_assessment: TriageAssessment
    
  latency_target: 100ms
  
  decision_rules:
    critical_indicators:
      - known_critical_pattern_match
      - multi_facility_detection
      - extreme_anomaly_score
    
    priority_factors:
      - classification_confidence
      - event_rarity
      - scientific_significance
      - time_sensitivity
```

### Example Logic

```python
class TriageAgent:
    """Fast initial assessment."""
    
    async def assess(
        self, 
        event: ClassifiedEvent
    ) -> TriageResult:
        """Assess event and determine routing."""
        
        # Fast checks for critical indicators
        if self.has_critical_indicators(event):
            return TriageResult(
                priority=Priority.CRITICAL,
                agents=["pattern", "anomaly", "context", "coordination"],
                fast_track=True
            )
        
        # Determine priority based on scores
        priority = self.calculate_priority(event)
        
        # Determine which agents to invoke
        agents = self.select_agents(event, priority)
        
        return TriageResult(
            priority=priority,
            agents=agents,
            assessment=self.quick_assessment(event)
        )
    
    def select_agents(
        self, 
        event: ClassifiedEvent, 
        priority: Priority
    ) -> list[str]:
        """Select agents based on event characteristics."""
        
        agents = []
        
        # Pattern agent for classifiable events
        if event.classification_confidence > 0.3:
            agents.append("pattern")
        
        # Anomaly agent for unusual events
        if event.anomaly_score > 0.5:
            agents.append("anomaly")
        
        # Context agent for significant events
        if priority >= Priority.SIGNIFICANT:
            agents.append("context")
        
        return agents
```

---

## Agent 2: Pattern Agent

### Purpose
Match events against known patterns and provide detailed classification.

### Design Philosophy

The Pattern Agent has **deep domain knowledge** encoded in pattern libraries. It's slower but more accurate than initial classification.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Pattern matching | Compare against known event types |
| Classification refinement | More precise than initial classification |
| Similar event retrieval | Find historical analogues |
| Confidence calibration | Well-calibrated confidence scores |

### Specification

```yaml
pattern_agent:
  role: "Deep pattern matching"
  
  inputs:
    - event: ClassifiedEvent
    - context: TriageResult
    
  outputs:
    - matched_patterns: list[PatternMatch]
    - refined_classification: Classification
    - similar_events: list[HistoricalEvent]
    
  latency_target: 1s
  
  pattern_libraries:
    - supernovae_patterns
    - variable_star_patterns
    - asteroid_patterns
    - artifact_patterns
    - unknown_patterns  # "things we've seen but don't understand"
```

### Pattern Matching

```python
class PatternAgent:
    """Deep pattern matching."""
    
    def __init__(self, pattern_libraries: list[PatternLibrary]):
        self.libraries = pattern_libraries
    
    async def analyse(
        self, 
        event: ClassifiedEvent
    ) -> PatternAnalysis:
        """Match event against known patterns."""
        
        matches = []
        
        for library in self.libraries:
            library_matches = await library.match(event)
            matches.extend(library_matches)
        
        # Rank matches by confidence
        matches.sort(key=lambda m: m.confidence, reverse=True)
        
        # Find similar historical events
        similar = await self.find_similar(event, matches)
        
        # Refine classification
        classification = self.refine_classification(event, matches)
        
        return PatternAnalysis(
            matched_patterns=matches[:10],  # Top 10
            refined_classification=classification,
            similar_events=similar,
            confidence=matches[0].confidence if matches else 0.0
        )
    
    async def find_similar(
        self,
        event: ClassifiedEvent,
        matches: list[PatternMatch]
    ) -> list[HistoricalEvent]:
        """Find similar historical events."""
        
        similar = []
        
        # Search by position
        positional = await self.search_by_position(event.coordinates)
        similar.extend(positional)
        
        # Search by pattern similarity
        for match in matches[:3]:
            pattern_similar = await self.search_by_pattern(match.pattern_id)
            similar.extend(pattern_similar)
        
        # Deduplicate and rank
        similar = self.rank_similarity(event, similar)
        
        return similar[:5]
```

---

## Agent 3: Anomaly Agent

### Purpose
Assess how novel or unusual an event is.

### Design Philosophy

The Anomaly Agent is **skeptical of classifications** and specifically looks for events that don't fit known patterns — the potential discoveries.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Novelty detection | How different from known patterns? |
| Outlier identification | What features are unusual? |
| Confidence assessment | How sure are we it's anomalous? |
| Discovery potential | Could this be something new? |

### Specification

```yaml
anomaly_agent:
  role: "Novelty and outlier detection"
  
  inputs:
    - event: ClassifiedEvent
    - pattern_analysis: PatternAnalysis
    
  outputs:
    - anomaly_score: float
    - unusual_features: list[FeatureAnomaly]
    - discovery_potential: float
    - comparison_to_normal: ComparisonReport
    
  latency_target: 1s
  
  methods:
    - isolation_forest
    - autoencoder_reconstruction
    - feature_distribution_analysis
```

### Anomaly Detection

```python
class AnomalyAgent:
    """Detect novel or unusual events."""
    
    def __init__(self, models: dict):
        self.isolation_forest = models["isolation_forest"]
        self.autoencoder = models["autoencoder"]
        self.feature_distributions = models["distributions"]
    
    async def analyse(
        self, 
        event: ClassifiedEvent,
        pattern_analysis: PatternAnalysis
    ) -> AnomalyAnalysis:
        """Assess event novelty."""
        
        features = self.extract_features(event)
        
        # Multiple anomaly detection methods
        isolation_score = self.isolation_forest.score(features)
        reconstruction_error = self.autoencoder.reconstruction_error(features)
        feature_anomalies = self.check_feature_distributions(features)
        
        # Combine scores
        anomaly_score = self.combine_scores(
            isolation=isolation_score,
            reconstruction=reconstruction_error,
            feature_count=len(feature_anomalies)
        )
        
        # Assess discovery potential
        # High anomaly + low pattern match = potential discovery
        pattern_confidence = pattern_analysis.confidence if pattern_analysis else 0.0
        discovery_potential = anomaly_score * (1 - pattern_confidence)
        
        return AnomalyAnalysis(
            anomaly_score=anomaly_score,
            unusual_features=feature_anomalies,
            discovery_potential=discovery_potential,
            method_scores={
                "isolation": isolation_score,
                "reconstruction": reconstruction_error,
                "feature_distribution": len(feature_anomalies)
            }
        )
```

---

## Agent 4: Context Agent

### Purpose
Gather historical and environmental context for significant events.

### Design Philosophy

The Context Agent **enriches events with background** that helps scientists interpret them. Slower, used only for significant events.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Historical context | What's at this location? |
| Environmental context | Observing conditions |
| Cross-reference | Related observations |
| Literature search | Known science at this position |

### Specification

```yaml
context_agent:
  role: "Context enrichment"
  
  inputs:
    - event: ClassifiedEvent
    - analysis_so_far: dict
    
  outputs:
    - historical_context: HistoricalContext
    - environmental_context: EnvironmentalContext
    - related_observations: list[Observation]
    - literature_references: list[Reference]
    
  latency_target: 30s
  
  data_sources:
    - archive_database
    - catalog_services
    - literature_search
    - environmental_logs
```

### Context Gathering

```python
class ContextAgent:
    """Gather context for events."""
    
    async def enrich(
        self, 
        event: ClassifiedEvent
    ) -> EventContext:
        """Gather context from multiple sources."""
        
        # Parallel context gathering
        tasks = [
            self.get_historical_context(event),
            self.get_environmental_context(event),
            self.get_related_observations(event),
            self.search_literature(event),
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return EventContext(
            historical=results[0] if not isinstance(results[0], Exception) else None,
            environmental=results[1] if not isinstance(results[1], Exception) else None,
            related=results[2] if not isinstance(results[2], Exception) else [],
            literature=results[3] if not isinstance(results[3], Exception) else [],
        )
    
    async def get_historical_context(
        self, 
        event: ClassifiedEvent
    ) -> HistoricalContext:
        """What's at this sky position?"""
        
        # Search catalog for known objects
        catalog_matches = await self.catalog.cone_search(
            ra=event.coordinates.ra,
            dec=event.coordinates.dec,
            radius=10.0  # arcseconds
        )
        
        # Search archive for previous observations
        archive_history = await self.archive.search(
            coordinates=event.coordinates,
            time_range=("2000-01-01", None)
        )
        
        return HistoricalContext(
            known_objects=catalog_matches,
            previous_observations=archive_history,
            previous_transients=self.filter_transients(archive_history)
        )
```

---

## Agent 5: Coordination Agent

### Purpose
Coordinate follow-up observations across facilities.

### Design Philosophy

The Coordination Agent **thinks operationally** — what observations are needed, which facilities can do them, how to prioritise requests.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Follow-up planning | What observations are needed? |
| Facility selection | Which facilities can observe? |
| Request generation | Format observation requests |
| Response tracking | Track follow-up status |

### Specification

```yaml
coordination_agent:
  role: "Multi-facility coordination"
  
  inputs:
    - event: ClassifiedEvent
    - synthesis: SynthesisResult
    
  outputs:
    - observation_requests: list[ObservationRequest]
    - facility_assignments: list[FacilityAssignment]
    - public_alert: optional[PublicAlert]
    
  latency_target: 5 minutes
  
  facilities:
    - optical_telescopes
    - radio_telescopes
    - space_telescopes
    - spectroscopic_facilities
```

### Coordination Logic

```python
class CoordinationAgent:
    """Coordinate follow-up observations."""
    
    async def coordinate(
        self, 
        event: ClassifiedEvent,
        synthesis: SynthesisResult
    ) -> CoordinationPlan:
        """Plan follow-up observations."""
        
        # Determine what observations would help
        needed = self.determine_needed_observations(event, synthesis)
        
        # Find capable facilities
        for observation in needed:
            capable = await self.find_capable_facilities(
                observation=observation,
                coordinates=event.coordinates,
                time_constraints=observation.time_window
            )
            observation.capable_facilities = capable
        
        # Prioritise and assign
        assignments = self.assign_facilities(needed)
        
        # Generate requests
        requests = [
            self.generate_request(obs, facility)
            for obs, facility in assignments
        ]
        
        # Generate public alert if warranted
        public_alert = None
        if synthesis.significance > 0.9:
            public_alert = self.generate_public_alert(event, synthesis)
        
        return CoordinationPlan(
            observation_requests=requests,
            facility_assignments=assignments,
            public_alert=public_alert
        )
```

---

## Agent 6: Synthesis Agent

### Purpose
Combine outputs from all agents into a coherent assessment.

### Responsibilities

| Responsibility | Description |
|:---------------|:------------|
| Integration | Combine all agent outputs |
| Conflict resolution | Handle disagreements |
| Summary generation | Human-readable assessment |
| Recommendation | What action to take |

### Synthesis Logic

```python
class SynthesisAgent:
    """Combine agent outputs."""
    
    async def synthesize(
        self, 
        event: ClassifiedEvent,
        agent_outputs: dict
    ) -> SynthesisResult:
        """Synthesize all agent outputs."""
        
        # Extract key findings
        pattern_result = agent_outputs.get("pattern")
        anomaly_result = agent_outputs.get("anomaly")
        context_result = agent_outputs.get("context")
        
        # Resolve any conflicts
        conflicts = self.detect_conflicts(agent_outputs)
        resolution = self.resolve_conflicts(conflicts)
        
        # Generate overall assessment
        assessment = self.generate_assessment(
            event=event,
            pattern=pattern_result,
            anomaly=anomaly_result,
            context=context_result,
            conflict_resolution=resolution
        )
        
        # Generate recommendation
        recommendation = self.generate_recommendation(assessment)
        
        return SynthesisResult(
            assessment=assessment,
            recommendation=recommendation,
            confidence=self.calculate_confidence(agent_outputs),
            supporting_evidence=self.collect_evidence(agent_outputs)
        )
```

---

## Agent Communication

### Message Protocol

```python
@dataclass
class AgentMessage:
    """Message between agents."""
    
    message_id: str
    source_agent: str
    target_agent: str
    message_type: str  # request, response, update
    
    # Content
    event_id: str
    content: dict
    
    # Metadata
    timestamp: datetime
    latency_budget_remaining: float  # seconds
    priority: int
```

### Orchestration

```python
class AgentOrchestrator:
    """Coordinate agent execution."""
    
    async def process_event(
        self, 
        event: ClassifiedEvent
    ) -> ProcessingResult:
        """Process event through agent pipeline."""
        
        # Triage
        triage_result = await self.triage_agent.assess(event)
        
        # Parallel analysis by selected agents
        analysis_tasks = {}
        for agent_name in triage_result.agents:
            agent = self.agents[agent_name]
            analysis_tasks[agent_name] = agent.analyse(event)
        
        analysis_results = await asyncio.gather(
            *analysis_tasks.values(),
            return_exceptions=True
        )
        
        agent_outputs = dict(zip(analysis_tasks.keys(), analysis_results))
        
        # Synthesis
        synthesis = await self.synthesis_agent.synthesize(event, agent_outputs)
        
        # Coordination if needed
        coordination = None
        if synthesis.significance > 0.7:
            coordination = await self.coordination_agent.coordinate(
                event, synthesis
            )
        
        return ProcessingResult(
            event=event,
            triage=triage_result,
            analysis=agent_outputs,
            synthesis=synthesis,
            coordination=coordination
        )
```

---

## Deliverables

| Deliverable | Location |
|:------------|:---------|
| **Agent specifications** | `artifacts/agent_specification.md` |
| **Communication protocol** | Message formats, routing |
| **Orchestration design** | Execution flow |
| **Error handling** | Graceful degradation |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Event Architecture](02_event_architecture.md) | [Project Overview](README.md) | [Provenance System →](04_provenance_system.md) |
