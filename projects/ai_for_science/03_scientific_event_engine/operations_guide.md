# Operations Guide

## Overview

This document describes how to operate the scientific event processing system in a production environment.

---

## System Overview

### Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES                                    │
│  Telescope A │ Telescope B │ Satellite │ Archive                   │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  INGESTION LAYER                                                    │
│  Message Queue (Kafka) │ Stream Processor                          │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  PROCESSING LAYER                                                   │
│  Filter → Classify → Route → Agents                                │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│  OUTPUT LAYER                                                       │
│  Alerts │ Review Queue │ Archive                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Endpoints

| Service | Endpoint | Purpose |
|:--------|:---------|:--------|
| API Gateway | `api.events.facility.org` | External API |
| Dashboard | `dashboard.events.facility.org` | Monitoring |
| Alert Portal | `alerts.events.facility.org` | Alert management |
| Admin | `admin.events.facility.org` | System administration |

---

## Normal Operations

### Daily Checklist

| Time | Task | Owner |
|:-----|:-----|:------|
| 06:00 | Review overnight alerts | On-call |
| 06:00 | Check system health dashboard | On-call |
| 09:00 | Review processing metrics | Ops team |
| 18:00 | Pre-night health check | On-call |
| 22:00 | Confirm night processing started | On-call |

### Monitoring Dashboard

**Key panels to watch:**

| Panel | Normal Range | Action if Abnormal |
|:------|:-------------|:-------------------|
| Event rate | ±20% of expected | Check data sources |
| Processing latency | <1min (p50) | Check for backlog |
| Queue depth | <10,000 | Scale up if needed |
| Error rate | <0.1% | Investigate errors |
| Alert volume | <50/night | Review thresholds |

### Alert Response

| Alert Level | Response Time | Responder |
|:------------|:--------------|:----------|
| CRITICAL | <15 min | On-call + Science |
| HIGH | <1 hour | On-call |
| MEDIUM | <4 hours | Ops team |
| LOW | Next business day | Ops team |

---

## Incident Response

### Severity Levels

| Level | Definition | Example |
|:------|:-----------|:--------|
| **SEV-1** | System down, no events processing | Pipeline crash |
| **SEV-2** | Major degradation, missing events | Critical recall <99% |
| **SEV-3** | Minor degradation | Increased latency |
| **SEV-4** | Cosmetic/minor issue | Dashboard glitch |

### Response Procedures

#### SEV-1: System Down

```
1. Acknowledge alert
2. Assess scope (which components affected?)
3. Check recent changes (deployments, config)
4. Engage additional responders if needed
5. Implement fix or rollback
6. Verify recovery
7. Document incident
```

**Escalation:**
- 15 min: Page backup on-call
- 30 min: Page engineering lead
- 1 hour: Page director

#### SEV-2: Major Degradation

```
1. Acknowledge alert
2. Identify affected functionality
3. Check metrics for root cause
4. Implement mitigation
5. Schedule permanent fix
6. Document incident
```

#### Common Issues

| Symptom | Likely Cause | Quick Fix |
|:--------|:-------------|:----------|
| High latency | Queue backup | Scale up workers |
| Missed events | Threshold too high | Lower threshold |
| Too many alerts | Threshold too low | Raise threshold |
| Processing errors | Bad data | Check data source |
| Agent timeout | Resource exhaustion | Restart agent |

---

## Maintenance

### Scheduled Maintenance

| Task | Frequency | Duration | Impact |
|:-----|:----------|:---------|:-------|
| Database backup | Daily | 30 min | None |
| Index rebuild | Weekly | 2 hours | Slow queries |
| Model update | Monthly | 4 hours | Brief downtime |
| Full system test | Quarterly | 8 hours | Planned downtime |

### Maintenance Windows

| Type | Schedule | Notification |
|:-----|:---------|:-------------|
| Rolling restart | Any time | None needed |
| Brief downtime | Tuesday 10:00-14:00 UTC | 24h advance |
| Extended downtime | Saturday 06:00-18:00 UTC | 1 week advance |

### Deployment Procedure

```
1. Pre-deployment
   - Review changes
   - Verify tests pass
   - Announce deployment

2. Deployment
   - Deploy to staging
   - Run smoke tests
   - Deploy to production (canary)
   - Monitor metrics
   - Full rollout

3. Post-deployment
   - Verify metrics normal
   - Run injection test
   - Update documentation
```

---

## Scaling

### Auto-Scaling Rules

| Metric | Scale Up | Scale Down |
|:-------|:---------|:-----------|
| Queue depth | >10,000 | <1,000 |
| CPU usage | >80% | <30% |
| Processing latency | >2min | <30s |

### Manual Scaling

**When to scale manually:**
- Known high-volume events (e.g., survey start)
- Maintenance on other components
- Unusual data patterns

**How to scale:**
```bash
# Scale processing workers
kubectl scale deployment event-processor --replicas=10

# Scale agent workers
kubectl scale deployment agent-pool --replicas=20

# Verify scaling
kubectl get pods -l app=event-processor
```

---

## Data Management

### Retention Policies

| Data Type | Hot Storage | Warm Storage | Archive |
|:----------|:------------|:-------------|:--------|
| Critical events | Permanent | - | - |
| Significant events | 1 year | Permanent | - |
| Interesting events | 90 days | 5 years | Archive |
| Routine events | 7 days | 1 year | Archive |
| Rejected events | 24 hours | 30 days | - |

### Backup Procedures

| Data | Backup Frequency | Retention | Location |
|:-----|:-----------------|:----------|:---------|
| Event database | Continuous | 30 days | Region B |
| Configuration | On change | 90 days | Git |
| Models | On update | All versions | S3 |

### Data Recovery

```
1. Identify data loss scope
2. Stop incoming data (if needed)
3. Restore from backup
4. Replay missed events from sources
5. Verify data integrity
6. Resume normal operations
```

---

## Access Control

### Roles

| Role | Permissions |
|:-----|:------------|
| **Observer** | View dashboard, alerts |
| **Operator** | Above + acknowledge alerts, adjust thresholds |
| **Admin** | Above + system configuration |
| **Super Admin** | Above + user management, audit |

### Access Procedures

**Requesting access:**
1. Submit ticket with justification
2. Manager approval
3. Security review (for Admin+)
4. Access granted

**Revoking access:**
- Automatic on role change
- Immediate on termination
- Quarterly access review

---

## On-Call

### On-Call Rotation

| Role | Coverage | Escalation |
|:-----|:---------|:-----------|
| Primary | 24/7 | 15 min response |
| Secondary | 24/7 | 30 min response |
| Engineering Lead | Business hours | SEV-1/2 escalation |

### On-Call Responsibilities

**During shift:**
- Monitor alert channels
- Respond to pages within SLA
- Escalate appropriately
- Document incidents

**Handoff:**
- Review active incidents
- Brief incoming on-call
- Update status page

### On-Call Tools

| Tool | Purpose | Access |
|:-----|:--------|:-------|
| PagerDuty | Alert routing | All on-call |
| Slack #ops | Team communication | All on-call |
| Dashboard | System monitoring | All on-call |
| Runbook | Incident procedures | All on-call |

---

## Runbooks

### Runbook: High Queue Depth

**Symptoms:** Queue depth >10,000

**Steps:**
1. Check processing worker status
2. Check for error spike
3. Scale up workers if healthy
4. If errors, identify source
5. If data source issue, contact source
6. Monitor until queue drains

### Runbook: Critical Alert Not Sent

**Symptoms:** Critical event detected but no alert

**Steps:**
1. Check alert service status
2. Check alert thresholds
3. Check notification channels
4. Manually send alert if critical
5. Fix underlying issue
6. Post-incident review

### Runbook: Agent Timeout

**Symptoms:** Agent exceeding latency budget

**Steps:**
1. Identify which agent
2. Check agent resource usage
3. Restart agent if stuck
4. Scale agent if resource-bound
5. Check for data causing slow processing
6. Consider skipping agent for critical events

---

## Contact Information

### Internal

| Team | Contact | Escalation |
|:-----|:--------|:-----------|
| Operations | #ops-events | ops-lead@facility.org |
| Engineering | #eng-events | eng-lead@facility.org |
| Science | #sci-events | sci-lead@facility.org |

### External

| Service | Contact | Support Hours |
|:--------|:--------|:--------------|
| Cloud Provider | support@cloud.com | 24/7 |
| Data Sources | dataops@source.org | Business hours |

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Operations Lead | | |
| Engineering Lead | | |
