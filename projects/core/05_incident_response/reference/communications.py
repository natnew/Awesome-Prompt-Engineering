"""
Incident Communication Utilities

Tools for generating status updates for different audiences.
Reference implementation - adapt for your organization.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum


class Audience(Enum):
    """Target audience for communications."""
    INTERNAL_TEAM = "internal_team"
    ENGINEERING = "engineering"
    LEADERSHIP = "leadership"
    CUSTOMERS = "customers"
    SUPPORT = "support"


class Severity(Enum):
    SEV1 = "sev1"
    SEV2 = "sev2"
    SEV3 = "sev3"
    SEV4 = "sev4"


@dataclass
class IncidentContext:
    """Context needed for generating communications."""
    incident_id: str
    title: str
    severity: Severity
    status: str
    summary: str
    impact: str
    started_at: datetime
    current_action: str
    next_update_minutes: int = 30
    eta_resolution: Optional[str] = None
    incident_commander: str = ""
    affected_services: list = None
    
    def __post_init__(self):
        if self.affected_services is None:
            self.affected_services = []


class CommunicationGenerator:
    """Generate incident communications for different audiences."""
    
    def generate(self, context: IncidentContext, audience: Audience) -> str:
        """Generate communication for specified audience."""
        generators = {
            Audience.INTERNAL_TEAM: self._generate_internal,
            Audience.ENGINEERING: self._generate_engineering,
            Audience.LEADERSHIP: self._generate_leadership,
            Audience.CUSTOMERS: self._generate_customer,
            Audience.SUPPORT: self._generate_support,
        }
        
        generator = generators.get(audience, self._generate_internal)
        return generator(context)
    
    def _generate_internal(self, ctx: IncidentContext) -> str:
        """Generate internal team update (Slack/Teams)."""
        severity_emoji = {
            Severity.SEV1: "🔴",
            Severity.SEV2: "🟠",
            Severity.SEV3: "🟡",
            Severity.SEV4: "🟢",
        }
        
        emoji = severity_emoji.get(ctx.severity, "⚪")
        duration = self._format_duration(ctx.started_at)
        
        lines = [
            f"{emoji} **[{ctx.severity.value.upper()}] {ctx.title}**",
            "",
            f"**Status:** {ctx.status}",
            f"**Duration:** {duration}",
            f"**IC:** {ctx.incident_commander}",
            "",
            f"**Impact:** {ctx.impact}",
            "",
            f"**Current Action:** {ctx.current_action}",
        ]
        
        if ctx.eta_resolution:
            lines.append(f"**ETA:** {ctx.eta_resolution}")
        
        lines.extend([
            "",
            f"_Next update in {ctx.next_update_minutes} minutes_",
        ])
        
        return "\n".join(lines)
    
    def _generate_engineering(self, ctx: IncidentContext) -> str:
        """Generate detailed engineering update."""
        duration = self._format_duration(ctx.started_at)
        
        lines = [
            f"# Incident Update: {ctx.incident_id}",
            "",
            f"**Severity:** {ctx.severity.value.upper()}",
            f"**Status:** {ctx.status}",
            f"**Duration:** {duration}",
            f"**Commander:** {ctx.incident_commander}",
            "",
            "## Summary",
            ctx.summary,
            "",
            "## Impact",
            ctx.impact,
            "",
        ]
        
        if ctx.affected_services:
            lines.extend([
                "## Affected Services",
                "",
            ])
            for service in ctx.affected_services:
                lines.append(f"- {service}")
            lines.append("")
        
        lines.extend([
            "## Current Action",
            ctx.current_action,
            "",
            "## Technical Details",
            "_[Add technical context here]_",
            "",
        ])
        
        if ctx.eta_resolution:
            lines.append(f"**Estimated Resolution:** {ctx.eta_resolution}")
        
        lines.extend([
            "",
            f"---",
            f"_Next update: {ctx.next_update_minutes} minutes_",
        ])
        
        return "\n".join(lines)
    
    def _generate_leadership(self, ctx: IncidentContext) -> str:
        """Generate executive summary for leadership."""
        duration = self._format_duration(ctx.started_at)
        
        # Severity to business impact mapping
        severity_impact = {
            Severity.SEV1: "Critical business impact - all hands responding",
            Severity.SEV2: "Significant impact - dedicated team responding",
            Severity.SEV3: "Moderate impact - being addressed",
            Severity.SEV4: "Minor impact - monitored",
        }
        
        lines = [
            f"**Incident Update: {ctx.title}**",
            "",
            f"**Business Impact:** {severity_impact.get(ctx.severity, 'Unknown')}",
            f"**Duration:** {duration}",
            "",
            f"**What's happening:** {ctx.summary}",
            "",
            f"**Customer impact:** {ctx.impact}",
            "",
            f"**What we're doing:** {ctx.current_action}",
        ]
        
        if ctx.eta_resolution:
            lines.extend([
                "",
                f"**Expected resolution:** {ctx.eta_resolution}",
            ])
        
        lines.extend([
            "",
            f"_Incident Commander: {ctx.incident_commander}_",
            f"_Next update in {ctx.next_update_minutes} minutes_",
        ])
        
        return "\n".join(lines)
    
    def _generate_customer(self, ctx: IncidentContext) -> str:
        """Generate customer-facing status update."""
        # Customer updates should be clear, non-technical, and empathetic
        
        status_messages = {
            "investigating": "We are investigating this issue.",
            "identified": "We have identified the cause and are working on a fix.",
            "mitigating": "We are implementing a fix.",
            "monitoring": "A fix has been implemented. We are monitoring the results.",
            "resolved": "This issue has been resolved.",
        }
        
        status_msg = status_messages.get(ctx.status.lower(), "We are working on this issue.")
        
        lines = [
            f"**Service Disruption - {ctx.title}**",
            "",
            f"We are aware of an issue affecting {self._simplify_impact(ctx.impact)}.",
            "",
            status_msg,
        ]
        
        if ctx.eta_resolution and ctx.status.lower() not in ("resolved", "monitoring"):
            lines.extend([
                "",
                f"We expect to have an update within {ctx.next_update_minutes} minutes.",
            ])
        
        lines.extend([
            "",
            "We apologize for any inconvenience this may cause.",
            "",
            f"_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC_",
        ])
        
        return "\n".join(lines)
    
    def _generate_support(self, ctx: IncidentContext) -> str:
        """Generate support team briefing."""
        duration = self._format_duration(ctx.started_at)
        
        lines = [
            f"# Support Brief: {ctx.incident_id}",
            "",
            f"**Issue:** {ctx.title}",
            f"**Severity:** {ctx.severity.value.upper()}",
            f"**Status:** {ctx.status}",
            f"**Duration:** {duration}",
            "",
            "## Customer Impact",
            ctx.impact,
            "",
            "## What to Tell Customers",
            self._generate_customer(ctx),
            "",
            "## FAQs",
            "",
            "**Q: When will this be fixed?**",
        ]
        
        if ctx.eta_resolution:
            lines.append(f"A: We expect resolution {ctx.eta_resolution}.")
        else:
            lines.append(f"A: We're actively working on this. Updates every {ctx.next_update_minutes} minutes.")
        
        lines.extend([
            "",
            "**Q: Is my data safe?**",
            "A: Yes, this issue does not affect data integrity or security.",
            "",
            "**Q: Will I be compensated?**",
            "A: Please refer affected customers to account management for SLA discussions.",
            "",
            "## Escalation Path",
            f"- Incident Commander: {ctx.incident_commander}",
            "- For urgent customer issues: #incident-{} Slack channel".format(ctx.incident_id.lower()),
            "",
            "## Do NOT",
            "- Promise specific resolution times not in this brief",
            "- Speculate about root cause",
            "- Share technical details with customers",
        ])
        
        return "\n".join(lines)
    
    def _format_duration(self, started_at: datetime) -> str:
        """Format duration since incident start."""
        delta = datetime.utcnow() - started_at
        total_minutes = int(delta.total_seconds() / 60)
        
        if total_minutes < 60:
            return f"{total_minutes} minutes"
        
        hours = total_minutes // 60
        minutes = total_minutes % 60
        
        if hours < 24:
            return f"{hours}h {minutes}m"
        
        days = hours // 24
        hours = hours % 24
        return f"{days}d {hours}h"
    
    def _simplify_impact(self, technical_impact: str) -> str:
        """Simplify technical impact for customer consumption."""
        # Map technical terms to customer-friendly language
        simplifications = {
            "api": "our services",
            "latency": "slower response times",
            "error rate": "some requests failing",
            "database": "our services",
            "authentication": "login functionality",
            "500 errors": "service errors",
        }
        
        result = technical_impact.lower()
        for tech, simple in simplifications.items():
            result = result.replace(tech, simple)
        
        return result


# =============================================================================
# UPDATE SCHEDULER
# =============================================================================

class UpdateScheduler:
    """Determine when to send updates based on severity and status."""
    
    # Update intervals in minutes by severity
    INTERVALS = {
        Severity.SEV1: {
            "investigating": 15,
            "identified": 15,
            "mitigating": 15,
            "monitoring": 30,
        },
        Severity.SEV2: {
            "investigating": 30,
            "identified": 30,
            "mitigating": 30,
            "monitoring": 60,
        },
        Severity.SEV3: {
            "investigating": 60,
            "identified": 60,
            "mitigating": 60,
            "monitoring": 120,
        },
        Severity.SEV4: {
            "investigating": 120,
            "identified": 120,
            "mitigating": 120,
            "monitoring": 240,
        },
    }
    
    def get_interval(self, severity: Severity, status: str) -> int:
        """Get update interval in minutes."""
        severity_intervals = self.INTERVALS.get(severity, self.INTERVALS[Severity.SEV3])
        return severity_intervals.get(status.lower(), 60)
    
    def should_update(
        self,
        severity: Severity,
        status: str,
        last_update: datetime,
    ) -> bool:
        """Check if an update is due."""
        interval = self.get_interval(severity, status)
        minutes_since = (datetime.utcnow() - last_update).total_seconds() / 60
        return minutes_since >= interval


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    print("Incident Communication Demo")
    print("=" * 60)
    
    # Create incident context
    context = IncidentContext(
        incident_id="INC-1705123456",
        title="Elevated API Error Rates",
        severity=Severity.SEV2,
        status="Mitigating",
        summary="API error rates increased to 15% due to database connection pool exhaustion",
        impact="15% of API requests are failing. Users may see errors when loading data.",
        started_at=datetime.utcnow(),
        current_action="Increasing connection pool size and restarting affected services",
        next_update_minutes=30,
        eta_resolution="within 1 hour",
        incident_commander="alice@example.com",
        affected_services=["api-gateway", "user-service", "data-service"],
    )
    
    generator = CommunicationGenerator()
    
    # Generate for each audience
    for audience in Audience:
        print(f"\n{'=' * 60}")
        print(f"AUDIENCE: {audience.value.upper()}")
        print("=" * 60)
        print()
        print(generator.generate(context, audience))
    
    # Show update schedule
    print(f"\n{'=' * 60}")
    print("UPDATE SCHEDULE")
    print("=" * 60)
    
    scheduler = UpdateScheduler()
    for sev in Severity:
        interval = scheduler.get_interval(sev, "investigating")
        print(f"{sev.value.upper()}: Update every {interval} minutes during investigation")
