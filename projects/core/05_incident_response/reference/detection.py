"""
Incident Detection Utilities

Tools for detecting AI system incidents through monitoring and alerting.
These are reference implementations - adapt for your infrastructure.

Requirements:
    pip install structlog
"""

import time
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Callable, Any
from enum import Enum
from collections import deque
import statistics
import structlog

logger = structlog.get_logger()


# =============================================================================
# DATA STRUCTURES
# =============================================================================

class Severity(Enum):
    """Incident severity levels."""
    SEV1 = "sev1"  # Critical - immediate response
    SEV2 = "sev2"  # High - respond within 1 hour
    SEV3 = "sev3"  # Medium - respond within 4 hours
    SEV4 = "sev4"  # Low - next business day


class IncidentType(Enum):
    """Categories of AI system incidents."""
    QUALITY_DEGRADATION = "quality_degradation"
    SAFETY_VIOLATION = "safety_violation"
    COST_ANOMALY = "cost_anomaly"
    LATENCY_SPIKE = "latency_spike"
    ERROR_RATE = "error_rate"
    DATA_LEAK = "data_leak"
    AVAILABILITY = "availability"


@dataclass
class Alert:
    """An alert triggered by a detector."""
    id: str
    incident_type: IncidentType
    severity: Severity
    title: str
    description: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    metrics: dict = field(default_factory=dict)
    suggested_actions: list = field(default_factory=list)
    runbook_link: str = ""
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "incident_type": self.incident_type.value,
            "severity": self.severity.value,
            "title": self.title,
            "description": self.description,
            "timestamp": self.timestamp.isoformat(),
            "metrics": self.metrics,
            "suggested_actions": self.suggested_actions,
            "runbook_link": self.runbook_link,
        }


@dataclass
class MetricPoint:
    """A single metric observation."""
    value: float
    timestamp: datetime = field(default_factory=datetime.utcnow)
    labels: dict = field(default_factory=dict)


# =============================================================================
# METRIC COLLECTORS
# =============================================================================

class MetricBuffer:
    """Thread-safe rolling buffer for metrics."""
    
    def __init__(self, max_age_seconds: float = 300, max_size: int = 1000):
        self.max_age = timedelta(seconds=max_age_seconds)
        self.max_size = max_size
        self.points: deque = deque(maxlen=max_size)
        self.lock = threading.Lock()
    
    def add(self, value: float, labels: dict = None):
        """Add a metric point."""
        point = MetricPoint(value=value, labels=labels or {})
        with self.lock:
            self.points.append(point)
    
    def get_recent(self, seconds: float = None) -> list:
        """Get recent points within time window."""
        cutoff = datetime.utcnow() - timedelta(seconds=seconds or self.max_age.total_seconds())
        with self.lock:
            return [p for p in self.points if p.timestamp > cutoff]
    
    def stats(self, seconds: float = None) -> dict:
        """Calculate statistics for recent points."""
        points = self.get_recent(seconds)
        if not points:
            return {"count": 0}
        
        values = [p.value for p in points]
        return {
            "count": len(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "min": min(values),
            "max": max(values),
            "stdev": statistics.stdev(values) if len(values) > 1 else 0,
            "p95": sorted(values)[int(len(values) * 0.95)] if len(values) >= 20 else max(values),
            "p99": sorted(values)[int(len(values) * 0.99)] if len(values) >= 100 else max(values),
        }


class MetricsRegistry:
    """Central registry for all metrics."""
    
    def __init__(self):
        self.buffers: dict[str, MetricBuffer] = {}
        self.lock = threading.Lock()
    
    def get_or_create(self, name: str, **kwargs) -> MetricBuffer:
        """Get existing buffer or create new one."""
        with self.lock:
            if name not in self.buffers:
                self.buffers[name] = MetricBuffer(**kwargs)
            return self.buffers[name]
    
    def record(self, name: str, value: float, labels: dict = None):
        """Record a metric value."""
        buffer = self.get_or_create(name)
        buffer.add(value, labels)
    
    def get_stats(self, name: str, seconds: float = None) -> dict:
        """Get statistics for a metric."""
        if name not in self.buffers:
            return {"count": 0}
        return self.buffers[name].stats(seconds)


# Global registry
metrics = MetricsRegistry()


# =============================================================================
# DETECTORS
# =============================================================================

class Detector(ABC):
    """Base class for incident detectors."""
    
    def __init__(self, name: str, check_interval: float = 60):
        self.name = name
        self.check_interval = check_interval
        self.last_alert: Optional[Alert] = None
        self.alert_cooldown = timedelta(minutes=5)
    
    @abstractmethod
    def check(self) -> Optional[Alert]:
        """Check for incident condition. Return Alert if triggered."""
        pass
    
    def should_alert(self) -> bool:
        """Check if we should send an alert (respects cooldown)."""
        if self.last_alert is None:
            return True
        return datetime.utcnow() - self.last_alert.timestamp > self.alert_cooldown
    
    def record_alert(self, alert: Alert):
        """Record that an alert was sent."""
        self.last_alert = alert


class ErrorRateDetector(Detector):
    """Detect elevated error rates."""
    
    def __init__(
        self,
        metric_name: str = "request_errors",
        threshold: float = 0.1,  # 10% error rate
        window_seconds: float = 300,
        min_samples: int = 10,
    ):
        super().__init__(name="error_rate")
        self.metric_name = metric_name
        self.threshold = threshold
        self.window_seconds = window_seconds
        self.min_samples = min_samples
    
    def check(self) -> Optional[Alert]:
        stats = metrics.get_stats(self.metric_name, self.window_seconds)
        
        if stats["count"] < self.min_samples:
            return None
        
        error_rate = stats["mean"]
        
        if error_rate > self.threshold and self.should_alert():
            severity = Severity.SEV1 if error_rate > 0.5 else Severity.SEV2
            
            alert = Alert(
                id=f"err-{int(time.time())}",
                incident_type=IncidentType.ERROR_RATE,
                severity=severity,
                title=f"Elevated Error Rate: {error_rate:.1%}",
                description=f"Error rate of {error_rate:.1%} exceeds threshold of {self.threshold:.1%}",
                metrics={
                    "error_rate": error_rate,
                    "threshold": self.threshold,
                    "sample_count": stats["count"],
                },
                suggested_actions=[
                    "Check recent deployments",
                    "Review error logs for patterns",
                    "Check upstream dependencies",
                    "Consider enabling circuit breaker",
                ],
                runbook_link="/runbooks/error-rate-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        return None


class LatencyDetector(Detector):
    """Detect latency spikes."""
    
    def __init__(
        self,
        metric_name: str = "request_latency_ms",
        p95_threshold_ms: float = 5000,
        p99_threshold_ms: float = 10000,
        window_seconds: float = 300,
        min_samples: int = 20,
    ):
        super().__init__(name="latency")
        self.metric_name = metric_name
        self.p95_threshold = p95_threshold_ms
        self.p99_threshold = p99_threshold_ms
        self.window_seconds = window_seconds
        self.min_samples = min_samples
    
    def check(self) -> Optional[Alert]:
        stats = metrics.get_stats(self.metric_name, self.window_seconds)
        
        if stats["count"] < self.min_samples:
            return None
        
        p95 = stats.get("p95", 0)
        p99 = stats.get("p99", 0)
        
        if p99 > self.p99_threshold and self.should_alert():
            alert = Alert(
                id=f"lat-{int(time.time())}",
                incident_type=IncidentType.LATENCY_SPIKE,
                severity=Severity.SEV2,
                title=f"Latency Spike: p99={p99:.0f}ms",
                description=f"p99 latency of {p99:.0f}ms exceeds threshold of {self.p99_threshold:.0f}ms",
                metrics={
                    "p95_ms": p95,
                    "p99_ms": p99,
                    "mean_ms": stats["mean"],
                    "threshold_p99_ms": self.p99_threshold,
                },
                suggested_actions=[
                    "Check model provider status",
                    "Review request queue depth",
                    "Check for traffic spike",
                    "Consider request shedding",
                ],
                runbook_link="/runbooks/latency-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        elif p95 > self.p95_threshold and self.should_alert():
            alert = Alert(
                id=f"lat-{int(time.time())}",
                incident_type=IncidentType.LATENCY_SPIKE,
                severity=Severity.SEV3,
                title=f"Latency Elevated: p95={p95:.0f}ms",
                description=f"p95 latency of {p95:.0f}ms exceeds threshold of {self.p95_threshold:.0f}ms",
                metrics={
                    "p95_ms": p95,
                    "p99_ms": p99,
                    "mean_ms": stats["mean"],
                    "threshold_p95_ms": self.p95_threshold,
                },
                suggested_actions=[
                    "Monitor for further degradation",
                    "Check concurrent request count",
                ],
                runbook_link="/runbooks/latency-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        return None


class CostAnomalyDetector(Detector):
    """Detect unusual cost patterns."""
    
    def __init__(
        self,
        metric_name: str = "request_cost_usd",
        hourly_budget: float = 100.0,
        spike_multiplier: float = 3.0,
        window_seconds: float = 3600,
    ):
        super().__init__(name="cost_anomaly")
        self.metric_name = metric_name
        self.hourly_budget = hourly_budget
        self.spike_multiplier = spike_multiplier
        self.window_seconds = window_seconds
        self.baseline_hourly: Optional[float] = None
    
    def set_baseline(self, hourly_cost: float):
        """Set baseline hourly cost for anomaly detection."""
        self.baseline_hourly = hourly_cost
    
    def check(self) -> Optional[Alert]:
        stats = metrics.get_stats(self.metric_name, self.window_seconds)
        
        if stats["count"] == 0:
            return None
        
        total_cost = stats["mean"] * stats["count"]
        hourly_rate = total_cost * (3600 / self.window_seconds)
        
        # Check absolute budget
        if hourly_rate > self.hourly_budget and self.should_alert():
            severity = Severity.SEV1 if hourly_rate > self.hourly_budget * 2 else Severity.SEV2
            
            alert = Alert(
                id=f"cost-{int(time.time())}",
                incident_type=IncidentType.COST_ANOMALY,
                severity=severity,
                title=f"Cost Budget Exceeded: ${hourly_rate:.2f}/hr",
                description=f"Hourly cost rate of ${hourly_rate:.2f} exceeds budget of ${self.hourly_budget:.2f}",
                metrics={
                    "hourly_rate_usd": hourly_rate,
                    "budget_usd": self.hourly_budget,
                    "total_cost_window": total_cost,
                },
                suggested_actions=[
                    "Enable cost circuit breaker",
                    "Check for runaway requests",
                    "Review recent traffic patterns",
                    "Consider rate limiting",
                ],
                runbook_link="/runbooks/cost-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        # Check relative spike
        if self.baseline_hourly and hourly_rate > self.baseline_hourly * self.spike_multiplier:
            if self.should_alert():
                alert = Alert(
                    id=f"cost-{int(time.time())}",
                    incident_type=IncidentType.COST_ANOMALY,
                    severity=Severity.SEV3,
                    title=f"Cost Spike: {hourly_rate/self.baseline_hourly:.1f}x baseline",
                    description=f"Hourly cost ${hourly_rate:.2f} is {hourly_rate/self.baseline_hourly:.1f}x the baseline of ${self.baseline_hourly:.2f}",
                    metrics={
                        "hourly_rate_usd": hourly_rate,
                        "baseline_usd": self.baseline_hourly,
                        "multiplier": hourly_rate / self.baseline_hourly,
                    },
                    suggested_actions=[
                        "Investigate traffic source",
                        "Check for loops or retries",
                    ],
                    runbook_link="/runbooks/cost-incident.md"
                )
                self.record_alert(alert)
                return alert
        
        return None


class QualityDegradationDetector(Detector):
    """Detect AI output quality degradation."""
    
    def __init__(
        self,
        metric_name: str = "quality_score",
        threshold: float = 0.7,
        baseline: float = 0.85,
        degradation_pct: float = 0.1,
        window_seconds: float = 600,
        min_samples: int = 50,
    ):
        super().__init__(name="quality")
        self.metric_name = metric_name
        self.threshold = threshold
        self.baseline = baseline
        self.degradation_pct = degradation_pct
        self.window_seconds = window_seconds
        self.min_samples = min_samples
    
    def check(self) -> Optional[Alert]:
        stats = metrics.get_stats(self.metric_name, self.window_seconds)
        
        if stats["count"] < self.min_samples:
            return None
        
        current_quality = stats["mean"]
        
        # Absolute threshold
        if current_quality < self.threshold and self.should_alert():
            alert = Alert(
                id=f"qual-{int(time.time())}",
                incident_type=IncidentType.QUALITY_DEGRADATION,
                severity=Severity.SEV2,
                title=f"Quality Below Threshold: {current_quality:.2f}",
                description=f"Quality score of {current_quality:.2f} is below threshold of {self.threshold:.2f}",
                metrics={
                    "quality_score": current_quality,
                    "threshold": self.threshold,
                    "sample_count": stats["count"],
                },
                suggested_actions=[
                    "Check model provider status",
                    "Review recent prompt changes",
                    "Examine sample of low-quality outputs",
                    "Consider fallback to previous version",
                ],
                runbook_link="/runbooks/quality-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        # Relative degradation
        degradation = (self.baseline - current_quality) / self.baseline
        if degradation > self.degradation_pct and self.should_alert():
            alert = Alert(
                id=f"qual-{int(time.time())}",
                incident_type=IncidentType.QUALITY_DEGRADATION,
                severity=Severity.SEV3,
                title=f"Quality Degraded: {degradation:.1%} below baseline",
                description=f"Quality score {current_quality:.2f} is {degradation:.1%} below baseline of {self.baseline:.2f}",
                metrics={
                    "quality_score": current_quality,
                    "baseline": self.baseline,
                    "degradation_pct": degradation,
                },
                suggested_actions=[
                    "Monitor for further degradation",
                    "Review recent changes",
                ],
                runbook_link="/runbooks/quality-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        return None


class SafetyViolationDetector(Detector):
    """Detect safety guardrail violations."""
    
    def __init__(
        self,
        metric_name: str = "safety_violations",
        threshold_per_hour: int = 5,
        critical_threshold: int = 1,  # Any critical violation
        window_seconds: float = 3600,
    ):
        super().__init__(name="safety")
        self.metric_name = metric_name
        self.threshold_per_hour = threshold_per_hour
        self.critical_threshold = critical_threshold
        self.window_seconds = window_seconds
        self.alert_cooldown = timedelta(minutes=1)  # Shorter cooldown for safety
    
    def check(self) -> Optional[Alert]:
        stats = metrics.get_stats(self.metric_name, self.window_seconds)
        
        if stats["count"] == 0:
            return None
        
        # Check for critical violations (max value indicates severity)
        if stats["max"] >= 3 and self.should_alert():  # 3 = critical
            alert = Alert(
                id=f"safety-{int(time.time())}",
                incident_type=IncidentType.SAFETY_VIOLATION,
                severity=Severity.SEV1,
                title="Critical Safety Violation Detected",
                description="A critical safety violation has been detected. Immediate investigation required.",
                metrics={
                    "violation_count": stats["count"],
                    "max_severity": stats["max"],
                },
                suggested_actions=[
                    "IMMEDIATELY review flagged outputs",
                    "Consider pausing affected feature",
                    "Notify safety team",
                    "Preserve logs for investigation",
                ],
                runbook_link="/runbooks/safety-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        # Check violation rate
        violation_rate = stats["count"] * (3600 / self.window_seconds)
        if violation_rate > self.threshold_per_hour and self.should_alert():
            alert = Alert(
                id=f"safety-{int(time.time())}",
                incident_type=IncidentType.SAFETY_VIOLATION,
                severity=Severity.SEV2,
                title=f"Elevated Safety Violations: {violation_rate:.1f}/hr",
                description=f"Safety violation rate of {violation_rate:.1f}/hr exceeds threshold of {self.threshold_per_hour}/hr",
                metrics={
                    "violations_per_hour": violation_rate,
                    "threshold": self.threshold_per_hour,
                    "total_violations": stats["count"],
                },
                suggested_actions=[
                    "Review violation patterns",
                    "Check for adversarial inputs",
                    "Verify guardrails are functioning",
                ],
                runbook_link="/runbooks/safety-incident.md"
            )
            self.record_alert(alert)
            return alert
        
        return None


# =============================================================================
# ALERT MANAGER
# =============================================================================

class AlertHandler(ABC):
    """Base class for alert handlers."""
    
    @abstractmethod
    def handle(self, alert: Alert):
        pass


class LogAlertHandler(AlertHandler):
    """Log alerts using structured logging."""
    
    def handle(self, alert: Alert):
        log_method = logger.critical if alert.severity == Severity.SEV1 else \
                     logger.error if alert.severity == Severity.SEV2 else \
                     logger.warning
        
        log_method(
            "alert_triggered",
            alert_id=alert.id,
            incident_type=alert.incident_type.value,
            severity=alert.severity.value,
            title=alert.title,
            metrics=alert.metrics,
        )


class CallbackAlertHandler(AlertHandler):
    """Call a function when alert triggers."""
    
    def __init__(self, callback: Callable[[Alert], None]):
        self.callback = callback
    
    def handle(self, alert: Alert):
        self.callback(alert)


class AlertManager:
    """Manages detectors and alert routing."""
    
    def __init__(self):
        self.detectors: list[Detector] = []
        self.handlers: list[AlertHandler] = [LogAlertHandler()]
        self.running = False
        self.thread: Optional[threading.Thread] = None
    
    def add_detector(self, detector: Detector):
        """Register a detector."""
        self.detectors.append(detector)
    
    def add_handler(self, handler: AlertHandler):
        """Register an alert handler."""
        self.handlers.append(handler)
    
    def check_all(self) -> list[Alert]:
        """Run all detectors and return any alerts."""
        alerts = []
        for detector in self.detectors:
            try:
                alert = detector.check()
                if alert:
                    alerts.append(alert)
                    for handler in self.handlers:
                        try:
                            handler.handle(alert)
                        except Exception as e:
                            logger.error("handler_error", handler=type(handler).__name__, error=str(e))
            except Exception as e:
                logger.error("detector_error", detector=detector.name, error=str(e))
        return alerts
    
    def start(self, interval: float = 60):
        """Start background monitoring."""
        self.running = True
        
        def run():
            while self.running:
                self.check_all()
                time.sleep(interval)
        
        self.thread = threading.Thread(target=run, daemon=True)
        self.thread.start()
    
    def stop(self):
        """Stop background monitoring."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def create_default_alert_manager() -> AlertManager:
    """Create alert manager with standard detectors."""
    manager = AlertManager()
    
    manager.add_detector(ErrorRateDetector())
    manager.add_detector(LatencyDetector())
    manager.add_detector(CostAnomalyDetector())
    manager.add_detector(QualityDegradationDetector())
    manager.add_detector(SafetyViolationDetector())
    
    return manager


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    import random
    
    print("Incident Detection Demo")
    print("=" * 50)
    
    # Create alert manager
    manager = create_default_alert_manager()
    
    # Add callback handler
    alerts_received = []
    manager.add_handler(CallbackAlertHandler(lambda a: alerts_received.append(a)))
    
    # Simulate normal metrics
    print("\nSimulating normal operation...")
    for _ in range(100):
        metrics.record("request_errors", random.random() * 0.05)  # ~2.5% error rate
        metrics.record("request_latency_ms", random.gauss(500, 100))
        metrics.record("request_cost_usd", random.gauss(0.01, 0.002))
        metrics.record("quality_score", random.gauss(0.85, 0.05))
    
    alerts = manager.check_all()
    print(f"Alerts during normal operation: {len(alerts)}")
    
    # Simulate incident
    print("\nSimulating error rate incident...")
    for _ in range(50):
        metrics.record("request_errors", random.random() * 0.3 + 0.2)  # ~35% error rate
    
    alerts = manager.check_all()
    print(f"Alerts after incident: {len(alerts)}")
    
    for alert in alerts:
        print(f"\n  [{alert.severity.value.upper()}] {alert.title}")
        print(f"  {alert.description}")
        print(f"  Suggested actions:")
        for action in alert.suggested_actions[:2]:
            print(f"    - {action}")
    
    print("\n" + "=" * 50)
    print("Demo complete.")
