"""
Incident Management Utilities

Tools for tracking, managing, and documenting incidents.
Reference implementation - adapt for your infrastructure.

Requirements:
    pip install structlog
"""

import json
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from typing import Optional, List
from enum import Enum
from pathlib import Path
import structlog

logger = structlog.get_logger()


# =============================================================================
# DATA STRUCTURES
# =============================================================================

class Severity(Enum):
    SEV1 = "sev1"
    SEV2 = "sev2"
    SEV3 = "sev3"
    SEV4 = "sev4"


class IncidentStatus(Enum):
    DETECTED = "detected"
    INVESTIGATING = "investigating"
    IDENTIFIED = "identified"
    MITIGATING = "mitigating"
    MONITORING = "monitoring"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IncidentType(Enum):
    QUALITY_DEGRADATION = "quality_degradation"
    SAFETY_VIOLATION = "safety_violation"
    COST_ANOMALY = "cost_anomaly"
    LATENCY_SPIKE = "latency_spike"
    ERROR_RATE = "error_rate"
    DATA_LEAK = "data_leak"
    AVAILABILITY = "availability"
    OTHER = "other"


@dataclass
class TimelineEntry:
    """A single entry in the incident timeline."""
    timestamp: datetime
    author: str
    action: str
    details: str = ""
    
    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp.isoformat(),
            "author": author,
            "action": self.action,
            "details": self.details,
        }


@dataclass
class Incident:
    """Complete incident record."""
    id: str
    title: str
    severity: Severity
    incident_type: IncidentType
    status: IncidentStatus = IncidentStatus.DETECTED
    
    # Timing
    detected_at: datetime = field(default_factory=datetime.utcnow)
    acknowledged_at: Optional[datetime] = None
    mitigated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    
    # Description
    summary: str = ""
    impact: str = ""
    root_cause: str = ""
    
    # People
    incident_commander: str = ""
    responders: List[str] = field(default_factory=list)
    
    # Tracking
    timeline: List[TimelineEntry] = field(default_factory=list)
    action_items: List[dict] = field(default_factory=list)
    related_alerts: List[str] = field(default_factory=list)
    
    # Metrics
    users_affected: int = 0
    requests_affected: int = 0
    estimated_cost: float = 0.0
    
    # Links
    slack_channel: str = ""
    postmortem_link: str = ""
    runbook_used: str = ""
    
    def add_timeline_entry(self, author: str, action: str, details: str = ""):
        """Add entry to timeline."""
        entry = TimelineEntry(
            timestamp=datetime.utcnow(),
            author=author,
            action=action,
            details=details,
        )
        self.timeline.append(entry)
    
    def update_status(self, new_status: IncidentStatus, author: str, details: str = ""):
        """Update incident status with timeline entry."""
        old_status = self.status
        self.status = new_status
        
        self.add_timeline_entry(
            author=author,
            action=f"Status changed: {old_status.value} → {new_status.value}",
            details=details,
        )
        
        # Update timestamps
        if new_status == IncidentStatus.INVESTIGATING and self.acknowledged_at is None:
            self.acknowledged_at = datetime.utcnow()
        elif new_status == IncidentStatus.MONITORING and self.mitigated_at is None:
            self.mitigated_at = datetime.utcnow()
        elif new_status == IncidentStatus.RESOLVED and self.resolved_at is None:
            self.resolved_at = datetime.utcnow()
    
    def time_to_acknowledge(self) -> Optional[timedelta]:
        """Time from detection to acknowledgment."""
        if self.acknowledged_at:
            return self.acknowledged_at - self.detected_at
        return None
    
    def time_to_mitigate(self) -> Optional[timedelta]:
        """Time from detection to mitigation."""
        if self.mitigated_at:
            return self.mitigated_at - self.detected_at
        return None
    
    def time_to_resolve(self) -> Optional[timedelta]:
        """Time from detection to resolution."""
        if self.resolved_at:
            return self.resolved_at - self.detected_at
        return None
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "severity": self.severity.value,
            "incident_type": self.incident_type.value,
            "status": self.status.value,
            "detected_at": self.detected_at.isoformat(),
            "acknowledged_at": self.acknowledged_at.isoformat() if self.acknowledged_at else None,
            "mitigated_at": self.mitigated_at.isoformat() if self.mitigated_at else None,
            "resolved_at": self.resolved_at.isoformat() if self.resolved_at else None,
            "summary": self.summary,
            "impact": self.impact,
            "root_cause": self.root_cause,
            "incident_commander": self.incident_commander,
            "responders": self.responders,
            "timeline": [
                {
                    "timestamp": e.timestamp.isoformat(),
                    "author": e.author,
                    "action": e.action,
                    "details": e.details,
                }
                for e in self.timeline
            ],
            "action_items": self.action_items,
            "related_alerts": self.related_alerts,
            "users_affected": self.users_affected,
            "requests_affected": self.requests_affected,
            "estimated_cost": self.estimated_cost,
            "slack_channel": self.slack_channel,
            "postmortem_link": self.postmortem_link,
            "runbook_used": self.runbook_used,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Incident":
        """Create from dictionary."""
        incident = cls(
            id=data["id"],
            title=data["title"],
            severity=Severity(data["severity"]),
            incident_type=IncidentType(data["incident_type"]),
            status=IncidentStatus(data["status"]),
        )
        
        incident.detected_at = datetime.fromisoformat(data["detected_at"])
        if data.get("acknowledged_at"):
            incident.acknowledged_at = datetime.fromisoformat(data["acknowledged_at"])
        if data.get("mitigated_at"):
            incident.mitigated_at = datetime.fromisoformat(data["mitigated_at"])
        if data.get("resolved_at"):
            incident.resolved_at = datetime.fromisoformat(data["resolved_at"])
        
        incident.summary = data.get("summary", "")
        incident.impact = data.get("impact", "")
        incident.root_cause = data.get("root_cause", "")
        incident.incident_commander = data.get("incident_commander", "")
        incident.responders = data.get("responders", [])
        
        incident.timeline = [
            TimelineEntry(
                timestamp=datetime.fromisoformat(e["timestamp"]),
                author=e["author"],
                action=e["action"],
                details=e.get("details", ""),
            )
            for e in data.get("timeline", [])
        ]
        
        incident.action_items = data.get("action_items", [])
        incident.related_alerts = data.get("related_alerts", [])
        incident.users_affected = data.get("users_affected", 0)
        incident.requests_affected = data.get("requests_affected", 0)
        incident.estimated_cost = data.get("estimated_cost", 0.0)
        incident.slack_channel = data.get("slack_channel", "")
        incident.postmortem_link = data.get("postmortem_link", "")
        incident.runbook_used = data.get("runbook_used", "")
        
        return incident


# =============================================================================
# INCIDENT MANAGER
# =============================================================================

class IncidentManager:
    """Manages incident lifecycle and persistence."""
    
    def __init__(self, storage_path: str = "./incidents"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.incidents: dict[str, Incident] = {}
        self._load_incidents()
    
    def _load_incidents(self):
        """Load incidents from storage."""
        for file_path in self.storage_path.glob("*.json"):
            try:
                with open(file_path) as f:
                    data = json.load(f)
                    incident = Incident.from_dict(data)
                    self.incidents[incident.id] = incident
            except Exception as e:
                logger.error("failed_to_load_incident", file=str(file_path), error=str(e))
    
    def _save_incident(self, incident: Incident):
        """Save incident to storage."""
        file_path = self.storage_path / f"{incident.id}.json"
        with open(file_path, "w") as f:
            json.dump(incident.to_dict(), f, indent=2)
    
    def create_incident(
        self,
        title: str,
        severity: Severity,
        incident_type: IncidentType,
        summary: str = "",
        commander: str = "",
    ) -> Incident:
        """Create a new incident."""
        incident_id = f"INC-{int(time.time())}"
        
        incident = Incident(
            id=incident_id,
            title=title,
            severity=severity,
            incident_type=incident_type,
            summary=summary,
            incident_commander=commander,
        )
        
        incident.add_timeline_entry(
            author=commander or "system",
            action="Incident created",
            details=summary,
        )
        
        self.incidents[incident_id] = incident
        self._save_incident(incident)
        
        logger.info(
            "incident_created",
            incident_id=incident_id,
            severity=severity.value,
            incident_type=incident_type.value,
        )
        
        return incident
    
    def get_incident(self, incident_id: str) -> Optional[Incident]:
        """Get incident by ID."""
        return self.incidents.get(incident_id)
    
    def update_incident(self, incident: Incident):
        """Update and save incident."""
        self.incidents[incident.id] = incident
        self._save_incident(incident)
    
    def get_active_incidents(self) -> List[Incident]:
        """Get all non-closed incidents."""
        return [
            inc for inc in self.incidents.values()
            if inc.status not in (IncidentStatus.RESOLVED, IncidentStatus.CLOSED)
        ]
    
    def get_incidents_by_severity(self, severity: Severity) -> List[Incident]:
        """Get incidents by severity."""
        return [inc for inc in self.incidents.values() if inc.severity == severity]
    
    def get_incidents_in_range(
        self,
        start: datetime,
        end: datetime,
    ) -> List[Incident]:
        """Get incidents within date range."""
        return [
            inc for inc in self.incidents.values()
            if start <= inc.detected_at <= end
        ]


# =============================================================================
# STATUS PAGE GENERATOR
# =============================================================================

class StatusPageGenerator:
    """Generate status page content from incidents."""
    
    STATUS_MESSAGES = {
        0: ("Operational", "All systems operational"),
        1: ("Degraded Performance", "Some systems experiencing issues"),
        2: ("Partial Outage", "Major functionality impacted"),
        3: ("Major Outage", "Service significantly impaired"),
    }
    
    def __init__(self, incident_manager: IncidentManager):
        self.manager = incident_manager
    
    def get_current_status(self) -> dict:
        """Get current system status based on active incidents."""
        active = self.manager.get_active_incidents()
        
        if not active:
            status_level = 0
        else:
            # Worst severity determines status
            severities = [inc.severity for inc in active]
            if Severity.SEV1 in severities:
                status_level = 3
            elif Severity.SEV2 in severities:
                status_level = 2
            elif Severity.SEV3 in severities:
                status_level = 1
            else:
                status_level = 0
        
        status_name, status_message = self.STATUS_MESSAGES[status_level]
        
        return {
            "status": status_name,
            "message": status_message,
            "level": status_level,
            "active_incidents": len(active),
            "updated_at": datetime.utcnow().isoformat(),
        }
    
    def generate_status_page(self) -> str:
        """Generate markdown status page."""
        status = self.get_current_status()
        active = self.manager.get_active_incidents()
        
        lines = [
            "# System Status",
            "",
            f"**Status:** {status['status']}",
            f"**Message:** {status['message']}",
            f"**Last Updated:** {status['updated_at']}",
            "",
        ]
        
        if active:
            lines.extend([
                "## Active Incidents",
                "",
            ])
            
            for inc in sorted(active, key=lambda x: x.severity.value):
                lines.extend([
                    f"### [{inc.severity.value.upper()}] {inc.title}",
                    f"**Status:** {inc.status.value}",
                    f"**Started:** {inc.detected_at.isoformat()}",
                    "",
                    inc.summary,
                    "",
                ])
        else:
            lines.extend([
                "## No Active Incidents",
                "",
                "All systems are operating normally.",
                "",
            ])
        
        # Recent resolved
        recent = [
            inc for inc in self.manager.incidents.values()
            if inc.status == IncidentStatus.RESOLVED
            and inc.resolved_at
            and (datetime.utcnow() - inc.resolved_at) < timedelta(days=7)
        ]
        
        if recent:
            lines.extend([
                "## Recently Resolved",
                "",
            ])
            
            for inc in sorted(recent, key=lambda x: x.resolved_at, reverse=True)[:5]:
                lines.append(f"- **{inc.title}** - Resolved {inc.resolved_at.strftime('%Y-%m-%d %H:%M')}")
            
            lines.append("")
        
        return "\n".join(lines)


# =============================================================================
# POSTMORTEM GENERATOR
# =============================================================================

class PostmortemGenerator:
    """Generate postmortem documents from incidents."""
    
    def generate(self, incident: Incident) -> str:
        """Generate postmortem markdown document."""
        lines = [
            f"# Postmortem: {incident.title}",
            "",
            f"**Incident ID:** {incident.id}",
            f"**Date:** {incident.detected_at.strftime('%Y-%m-%d')}",
            f"**Severity:** {incident.severity.value.upper()}",
            f"**Status:** {incident.status.value}",
            f"**Incident Commander:** {incident.incident_commander}",
            "",
            "---",
            "",
            "## Summary",
            "",
            incident.summary or "_[TODO: Add summary]_",
            "",
            "## Impact",
            "",
            incident.impact or "_[TODO: Describe impact]_",
            "",
        ]
        
        # Metrics
        if incident.users_affected or incident.requests_affected or incident.estimated_cost:
            lines.extend([
                "### Impact Metrics",
                "",
                f"- Users affected: {incident.users_affected:,}",
                f"- Requests affected: {incident.requests_affected:,}",
                f"- Estimated cost: ${incident.estimated_cost:,.2f}",
                "",
            ])
        
        # Timeline
        lines.extend([
            "## Timeline",
            "",
            "| Time (UTC) | Action |",
            "|:-----------|:-------|",
        ])
        
        for entry in incident.timeline:
            time_str = entry.timestamp.strftime("%H:%M")
            action = entry.action
            if entry.details:
                action += f" - {entry.details}"
            lines.append(f"| {time_str} | {action} |")
        
        lines.extend([
            "",
            "### Key Timestamps",
            "",
        ])
        
        lines.append(f"- **Detected:** {incident.detected_at.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        
        if incident.acknowledged_at:
            tta = incident.time_to_acknowledge()
            lines.append(f"- **Acknowledged:** {incident.acknowledged_at.strftime('%H:%M:%S')} UTC (TTA: {tta})")
        
        if incident.mitigated_at:
            ttm = incident.time_to_mitigate()
            lines.append(f"- **Mitigated:** {incident.mitigated_at.strftime('%H:%M:%S')} UTC (TTM: {ttm})")
        
        if incident.resolved_at:
            ttr = incident.time_to_resolve()
            lines.append(f"- **Resolved:** {incident.resolved_at.strftime('%H:%M:%S')} UTC (TTR: {ttr})")
        
        # Root cause
        lines.extend([
            "",
            "## Root Cause",
            "",
            incident.root_cause or "_[TODO: Identify root cause]_",
            "",
        ])
        
        # Contributing factors
        lines.extend([
            "## Contributing Factors",
            "",
            "_[TODO: List contributing factors]_",
            "",
            "1. ",
            "2. ",
            "3. ",
            "",
        ])
        
        # What went well / poorly
        lines.extend([
            "## What Went Well",
            "",
            "_[TODO: List what worked]_",
            "",
            "- ",
            "",
            "## What Went Poorly",
            "",
            "_[TODO: List what didn't work]_",
            "",
            "- ",
            "",
        ])
        
        # Action items
        lines.extend([
            "## Action Items",
            "",
            "| Action | Owner | Priority | Due Date | Status |",
            "|:-------|:------|:---------|:---------|:-------|",
        ])
        
        if incident.action_items:
            for item in incident.action_items:
                lines.append(
                    f"| {item.get('action', '')} | {item.get('owner', '')} | "
                    f"{item.get('priority', '')} | {item.get('due', '')} | {item.get('status', '')} |"
                )
        else:
            lines.append("| _[TODO]_ | | | | |")
        
        # Lessons learned
        lines.extend([
            "",
            "## Lessons Learned",
            "",
            "_[TODO: Key takeaways]_",
            "",
            "1. ",
            "2. ",
            "3. ",
            "",
            "---",
            "",
            f"*Generated: {datetime.utcnow().isoformat()}*",
        ])
        
        return "\n".join(lines)


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("Incident Management Demo")
    print("=" * 50)
    
    # Create manager (uses temp directory)
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = IncidentManager(storage_path=tmpdir)
        
        # Create an incident
        incident = manager.create_incident(
            title="Elevated Error Rate in Production",
            severity=Severity.SEV2,
            incident_type=IncidentType.ERROR_RATE,
            summary="Error rate spiked to 15% starting at 14:30 UTC",
            commander="alice@example.com",
        )
        
        print(f"\nCreated incident: {incident.id}")
        
        # Simulate incident response
        print("\nSimulating incident response...")
        
        time.sleep(0.1)
        incident.update_status(
            IncidentStatus.INVESTIGATING,
            author="alice@example.com",
            details="Starting investigation",
        )
        incident.responders.append("bob@example.com")
        
        time.sleep(0.1)
        incident.add_timeline_entry(
            author="bob@example.com",
            action="Identified cause",
            details="Recent deployment introduced regression",
        )
        
        time.sleep(0.1)
        incident.update_status(
            IncidentStatus.MITIGATING,
            author="alice@example.com",
            details="Rolling back deployment",
        )
        
        time.sleep(0.1)
        incident.update_status(
            IncidentStatus.MONITORING,
            author="alice@example.com",
            details="Rollback complete, monitoring metrics",
        )
        
        incident.root_cause = "Regression in v2.3.1 caused null pointer exception"
        incident.impact = "15% of API requests failed for 45 minutes"
        incident.users_affected = 1200
        incident.requests_affected = 45000
        
        time.sleep(0.1)
        incident.update_status(
            IncidentStatus.RESOLVED,
            author="alice@example.com",
            details="Error rate returned to normal levels",
        )
        
        incident.action_items = [
            {
                "action": "Add null check to UserService",
                "owner": "bob@example.com",
                "priority": "P1",
                "due": "2025-01-20",
                "status": "TODO",
            },
            {
                "action": "Add integration test for edge case",
                "owner": "carol@example.com",
                "priority": "P2",
                "due": "2025-01-22",
                "status": "TODO",
            },
        ]
        
        manager.update_incident(incident)
        
        # Generate status page
        print("\n" + "-" * 50)
        print("STATUS PAGE:")
        print("-" * 50)
        
        status_gen = StatusPageGenerator(manager)
        print(status_gen.generate_status_page())
        
        # Generate postmortem
        print("\n" + "-" * 50)
        print("POSTMORTEM:")
        print("-" * 50)
        
        pm_gen = PostmortemGenerator()
        print(pm_gen.generate(incident))
        
        # Show metrics
        print("\n" + "-" * 50)
        print("INCIDENT METRICS:")
        print("-" * 50)
        print(f"Time to Acknowledge: {incident.time_to_acknowledge()}")
        print(f"Time to Mitigate: {incident.time_to_mitigate()}")
        print(f"Time to Resolve: {incident.time_to_resolve()}")
    
    print("\n" + "=" * 50)
    print("Demo complete.")
