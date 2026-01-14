# Event Schema

## Overview

This document defines the data model for events flowing through the scientific event processing system.

---

## Core Entities

### RawObservation

The fundamental unit of data from instruments.

```python
@dataclass
class RawObservation:
    """Raw observation from instrument."""
    
    # Identity
    observation_id: str              # Unique identifier
    source_facility: str             # Originating facility
    instrument: str                  # Specific instrument
    
    # Timing
    observation_time: datetime       # When observation occurred
    exposure_duration: float         # Seconds
    received_time: datetime          # When received by system
    
    # Position
    coordinates: SkyCoordinates      # Sky position
    position_uncertainty: float      # Arcseconds
    field_of_view: float             # Arcseconds
    
    # Measurement
    measurement_type: str            # flux, magnitude, spectrum
    measurement_value: float         # Primary measurement
    measurement_uncertainty: float   # 1-sigma uncertainty
    measurement_unit: str            # Unit of measurement
    
    # Data reference
    raw_data_uri: str                # Link to raw data file
    calibration_version: str         # Calibration applied
    
    # Quality
    quality_flags: list[str]         # Known quality issues
    snr: float                       # Signal-to-noise ratio
    
    # Metadata
    environmental_conditions: dict   # Weather, seeing, etc.
    instrument_config: dict          # Instrument settings

@dataclass
class SkyCoordinates:
    """Celestial coordinates."""
    ra: float                        # Right ascension (degrees)
    dec: float                       # Declination (degrees)
    epoch: str = "J2000"             # Coordinate epoch
    
    def separation(self, other: 'SkyCoordinates') -> float:
        """Calculate angular separation in arcseconds."""
        # Great circle distance calculation
        pass
```

---

### ProcessedEvent

An observation after processing and classification.

```python
@dataclass
class ProcessedEvent:
    """Event after processing pipeline."""
    
    # Identity
    event_id: str                    # Unique event identifier
    
    # Source observations
    observations: list[RawObservation]
    primary_observation_id: str      # Primary observation
    
    # Position (refined)
    coordinates: SkyCoordinates
    position_uncertainty: float
    
    # Classification
    category: EventCategory
    classification_confidence: float
    classification_scores: dict      # Score per category
    
    # Significance
    significance_score: float        # 0-1, scientific importance
    urgency_score: float             # 0-1, time sensitivity
    
    # Properties
    properties: EventProperties      # Measured properties
    
    # Analysis
    analysis_results: dict           # Agent analysis results
    
    # Provenance
    processing_steps: list[ProcessingStep]
    
    # Status
    status: EventStatus
    created_at: datetime
    updated_at: datetime

class EventCategory(Enum):
    """Event classification categories."""
    CRITICAL = "critical"            # Requires immediate attention
    SIGNIFICANT = "significant"      # High scientific value
    INTERESTING = "interesting"      # Worth human review
    KNOWN_TYPE = "known_type"        # Matches known class
    ROUTINE = "routine"              # Normal variation
    UNKNOWN = "unknown"              # Can't classify confidently
    ARTIFACT = "artifact"            # Instrumental artifact
    REJECTED = "rejected"            # Failed quality checks

class EventStatus(Enum):
    """Event processing status."""
    INGESTED = "ingested"
    PROCESSING = "processing"
    CLASSIFIED = "classified"
    REVIEWED = "reviewed"
    CONFIRMED = "confirmed"
    RETRACTED = "retracted"
```

---

### EventProperties

Scientific properties of detected event.

```python
@dataclass
class EventProperties:
    """Measured properties of event."""
    
    # Brightness
    peak_magnitude: Optional[float]
    current_magnitude: Optional[float]
    magnitude_uncertainty: Optional[float]
    filter_band: Optional[str]       # e.g., "g", "r", "i"
    
    # Variability
    is_variable: bool
    variability_amplitude: Optional[float]
    variability_period: Optional[float]  # If periodic
    
    # Motion
    is_moving: bool
    proper_motion: Optional[float]   # arcsec/year
    parallax: Optional[float]        # arcsec
    
    # Spectral (if available)
    spectral_class: Optional[str]
    redshift: Optional[float]
    
    # Context
    host_galaxy: Optional[str]       # If associated
    distance: Optional[float]        # If known (parsecs)
    
    # Historical
    first_detection: datetime
    last_detection: datetime
    detection_count: int
```

---

### Alert

Alert message for significant events.

```python
@dataclass
class Alert:
    """Alert for significant event."""
    
    # Identity
    alert_id: str
    event_id: str
    
    # Priority
    priority: AlertPriority
    category: EventCategory
    
    # Content
    summary: str                     # Human-readable summary
    coordinates: SkyCoordinates
    
    # Timing
    observation_time: datetime       # When event was observed
    alert_time: datetime             # When alert generated
    
    # Evidence
    classification_confidence: float
    significance_score: float
    supporting_data: dict
    
    # Actions
    recommended_actions: list[str]
    follow_up_requested: bool
    
    # Status
    acknowledged: bool
    acknowledged_by: Optional[str]
    acknowledged_at: Optional[datetime]

class AlertPriority(Enum):
    """Alert priority levels."""
    CRITICAL = 1     # Immediate human attention required
    HIGH = 2         # Same-night response needed
    MEDIUM = 3       # Next-night planning
    LOW = 4          # Routine review
```

---

### FollowUpRequest

Request for follow-up observations.

```python
@dataclass
class FollowUpRequest:
    """Request for follow-up observations."""
    
    # Identity
    request_id: str
    event_id: str
    
    # What's needed
    observation_type: str            # photometry, spectroscopy, imaging
    required_capabilities: list[str] # e.g., ["spectroscopy", "NIR"]
    
    # Where
    coordinates: SkyCoordinates
    
    # When
    priority: int                    # 1=highest
    time_window_start: datetime
    time_window_end: datetime
    
    # Constraints
    minimum_conditions: dict         # e.g., {"seeing": "<2arcsec"}
    
    # Status
    status: RequestStatus
    assigned_facility: Optional[str]
    completion_time: Optional[datetime]
    result_id: Optional[str]

class RequestStatus(Enum):
    """Follow-up request status."""
    PENDING = "pending"
    ASSIGNED = "assigned"
    SCHEDULED = "scheduled"
    OBSERVING = "observing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
```

---

## Message Formats

### Stream Message

Message format for event stream.

```python
@dataclass
class StreamMessage:
    """Message in event stream."""
    
    message_id: str
    message_type: str                # observation, event, alert
    timestamp: datetime
    
    # Payload
    payload: dict                    # Type-specific content
    
    # Routing
    source: str                      # Origin
    destination: str                 # Target queue/topic
    
    # Metadata
    schema_version: str
    correlation_id: Optional[str]    # For tracking related messages
```

### Agent Message

Message format for inter-agent communication.

```python
@dataclass
class AgentMessage:
    """Message between agents."""
    
    message_id: str
    source_agent: str
    target_agent: str
    message_type: str                # request, response, update
    
    # Content
    event_id: str
    content: dict
    
    # Timing
    timestamp: datetime
    latency_budget_ms: float         # Time remaining for processing
    
    # Priority
    priority: int
```

---

## Validation Rules

### Observation Validation

```python
def validate_observation(obs: RawObservation) -> ValidationResult:
    """Validate raw observation."""
    issues = []
    
    # Required fields
    required = ['observation_id', 'source_facility', 'observation_time', 
                'coordinates', 'measurement_value']
    for field in required:
        if getattr(obs, field) is None:
            issues.append(f"Missing required field: {field}")
    
    # Coordinate validity
    if obs.coordinates:
        if not (0 <= obs.coordinates.ra < 360):
            issues.append(f"Invalid RA: {obs.coordinates.ra}")
        if not (-90 <= obs.coordinates.dec <= 90):
            issues.append(f"Invalid Dec: {obs.coordinates.dec}")
    
    # Timing validity
    if obs.observation_time and obs.received_time:
        if obs.observation_time > obs.received_time:
            issues.append("Observation time after received time")
    
    # Uncertainty validity
    if obs.measurement_uncertainty is not None:
        if obs.measurement_uncertainty <= 0:
            issues.append("Measurement uncertainty must be positive")
    
    return ValidationResult(
        valid=len(issues) == 0,
        issues=issues
    )
```

### Event Validation

```python
def validate_event(event: ProcessedEvent) -> ValidationResult:
    """Validate processed event."""
    issues = []
    
    # Must have at least one observation
    if not event.observations:
        issues.append("Event must have at least one observation")
    
    # Classification confidence bounds
    if not (0 <= event.classification_confidence <= 1):
        issues.append(f"Invalid confidence: {event.classification_confidence}")
    
    # Scores must sum to ~1
    if event.classification_scores:
        total = sum(event.classification_scores.values())
        if not (0.99 <= total <= 1.01):
            issues.append(f"Classification scores sum to {total}, expected ~1.0")
    
    # Provenance required
    if not event.processing_steps:
        issues.append("Event must have processing provenance")
    
    return ValidationResult(
        valid=len(issues) == 0,
        issues=issues
    )
```

---

## Schema Evolution

### Versioning Strategy

| Version | Format | Example |
|:--------|:-------|:--------|
| Major | `v{N}.0` | Breaking changes |
| Minor | `v{N}.{M}` | Additive changes |
| Schema field | `schema_version` | In every message |

### Compatibility Rules

1. **New optional fields:** Always allowed
2. **New required fields:** Major version bump
3. **Removing fields:** Major version bump
4. **Changing field types:** Major version bump
5. **Adding enum values:** Minor version bump

### Migration

```python
def migrate_observation(
    obs: dict, 
    from_version: str, 
    to_version: str
) -> dict:
    """Migrate observation between schema versions."""
    
    # v1.0 -> v2.0: Added position_uncertainty
    if from_version == "v1.0" and to_version.startswith("v2"):
        if 'position_uncertainty' not in obs:
            obs['position_uncertainty'] = None
    
    # v2.0 -> v3.0: Renamed field
    if from_version.startswith("v2") and to_version.startswith("v3"):
        if 'flux' in obs:
            obs['measurement_value'] = obs.pop('flux')
    
    return obs
```

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Data Architect | | |
| Science Lead | | |
