# Runbook Template

## Overview

**Purpose:** Document operational procedures for running AI systems in production.

**When to use:** Before production deployment. Update when procedures change.

**Competencies:** [Safety & Reliability](../../COMPETENCIES.md#3-safety--reliability)

---

# Runbook: [System Name]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Version:** 1.0  
**On-Call Team:** _[Team name/rotation]_

---

## Quick Reference

### Emergency Contacts

| Role | Name | Contact | Escalate After |
|:-----|:-----|:--------|:---------------|
| Primary On-Call | _[Rotation]_ | _[Phone/Slack]_ | — |
| Secondary On-Call | _[Rotation]_ | _[Phone/Slack]_ | 15 min |
| Engineering Lead | _[Name]_ | _[Contact]_ | 30 min |
| Incident Commander | _[Rotation]_ | _[Contact]_ | SEV1/SEV2 |

### Critical Links

| Resource | Link |
|:---------|:-----|
| Dashboard | _[URL]_ |
| Logs | _[URL]_ |
| Alerts | _[URL]_ |
| Status Page | _[URL]_ |
| Incident Channel | _[Slack channel]_ |

### Kill Switches

| Switch | What It Does | How to Activate |
|:-------|:-------------|:----------------|
| Feature flag | Disable AI feature | `[command or UI path]` |
| Rate limit | Block all traffic | `[command or UI path]` |
| Rollback | Revert to previous version | `[command or UI path]` |

---

## System Overview

### Architecture

```
[Simple diagram]

Users → Load Balancer → API Service → AI Service → Model Provider
                            ↓              ↓
                         Database      Cache
```

### Dependencies

| Dependency | Purpose | Impact if Down | Fallback |
|:-----------|:--------|:---------------|:---------|
| _[Model API]_ | AI generation | No AI responses | _[Fallback]_ |
| _[Database]_ | State storage | Limited functionality | _[Fallback]_ |
| _[Cache]_ | Performance | Degraded latency | None (graceful) |

### Health Endpoints

| Endpoint | Expected | Meaning |
|:---------|:---------|:--------|
| `/health` | 200 OK | Service is running |
| `/health/ready` | 200 OK | Service can handle traffic |
| `/health/live` | 200 OK | Service is not deadlocked |

---

## Normal Operations

### Daily Checks

- [ ] Review overnight alerts
- [ ] Check error rate dashboard
- [ ] Verify backup completion
- [ ] Review cost dashboard

### Weekly Tasks

- [ ] Review metrics trends
- [ ] Check capacity utilization
- [ ] Update documentation if needed
- [ ] Review recent changes

### Deployments

**Pre-deployment:**
1. Verify tests pass
2. Review changes
3. Notify team in _[channel]_
4. Ensure rollback plan ready

**Deployment:**
```bash
# [Deployment commands]
```

**Post-deployment:**
1. Monitor error rates for 30 minutes
2. Verify key functionality
3. Update deployment log

**Rollback:**
```bash
# [Rollback commands]
```

---

## Incident Response

### Severity Definitions

| Level | Definition | Response Time | Examples |
|:------|:-----------|:--------------|:---------|
| SEV1 | Service down or safety incident | Immediate | Complete outage, data breach |
| SEV2 | Major functionality impaired | 15 min | 50%+ errors, security issue |
| SEV3 | Degraded performance | 1 hour | Elevated latency, partial failures |
| SEV4 | Minor issue | 4 hours | Cosmetic issues, edge cases |

### Initial Response (All Incidents)

1. **Assess** — What's happening? What's the impact?
2. **Communicate** — Post in _[incident channel]_
3. **Mitigate** — Stop the bleeding first
4. **Investigate** — Find root cause after stable
5. **Resolve** — Fix properly
6. **Document** — Update timeline, create post-mortem

---

## Common Issues

### Issue: High Error Rate

**Symptoms:** Error rate > 5% on dashboard

**Diagnosis:**
```bash
# Check recent errors
[log query command]

# Check model provider status
[status check command]
```

**Resolution:**
1. Check if deployment-related → Rollback if yes
2. Check model provider status → Wait or switch if down
3. Check for traffic spike → Enable rate limiting
4. Escalate if unclear

### Issue: High Latency

**Symptoms:** p99 latency > [threshold] ms

**Diagnosis:**
```bash
# Check latency by component
[query command]

# Check queue depth
[query command]
```

**Resolution:**
1. Check model provider latency → Wait or cache more
2. Check database performance → Scale or optimize
3. Check traffic volume → Rate limit if needed

### Issue: Cost Spike

**Symptoms:** Hourly cost > $[threshold]

**Diagnosis:**
```bash
# Check request volume
[query command]

# Check tokens per request
[query command]
```

**Resolution:**
1. Check for loops/retries → Fix and redeploy
2. Check for abuse → Block source
3. Enable cost circuit breaker if severe

### Issue: Safety Alert

**Symptoms:** Safety guardrail trigger rate elevated

**Diagnosis:**
```bash
# Review triggered content
[query command]

# Check for attack patterns
[query command]
```

**Resolution:**
1. If attack → Block source, review for gaps
2. If false positives → Tune guardrail (carefully)
3. If real violations → Investigate, consider pause
4. **Always escalate SEV1/SEV2 safety issues**

### Issue: Model Provider Outage

**Symptoms:** Model API returning errors or timeouts

**Diagnosis:**
1. Check provider status page
2. Check if affecting all requests or some

**Resolution:**
1. If total outage → Enable fallback (if available)
2. If partial → Increase retries/timeouts
3. Communicate expected impact to stakeholders
4. Monitor for recovery

---

## Maintenance Procedures

### Scaling

**Scale up:**
```bash
# [Scale up commands]
```

**Scale down:**
```bash
# [Scale down commands]
```

### Database Maintenance

**Backup verification:**
```bash
# [Backup check commands]
```

**Cleanup procedures:**
```bash
# [Cleanup commands]
```

### Log Rotation

Logs are automatically rotated every _[period]_.
Retention: _[duration]_

Manual cleanup if needed:
```bash
# [Cleanup commands]
```

---

## Monitoring Reference

### Key Metrics

| Metric | Normal Range | Warning | Critical |
|:-------|:-------------|:--------|:---------|
| Error rate | < 1% | > 5% | > 10% |
| Latency p99 | < 2s | > 5s | > 10s |
| Request rate | _[baseline]_ | > 2x | > 5x |
| Cost/hour | $[baseline] | > 2x | > 5x |

### Alert Responses

| Alert | Likely Cause | First Action |
|:------|:-------------|:-------------|
| `high_error_rate` | Deployment, provider issue | Check recent changes |
| `high_latency` | Load, provider issue | Check traffic and provider |
| `cost_spike` | Loop, abuse | Check request patterns |
| `safety_trigger` | Attack, bug | Review triggered content |

---

## Configuration Reference

### Environment Variables

| Variable | Purpose | Default |
|:---------|:--------|:--------|
| `MODEL_API_KEY` | Model provider auth | _[secret manager]_ |
| `MAX_TOKENS` | Token limit per request | 1000 |
| `TIMEOUT_SECONDS` | Request timeout | 30 |

### Feature Flags

| Flag | Purpose | Default |
|:-----|:--------|:--------|
| `ai_enabled` | Master AI toggle | true |
| `guardrails_strict` | Strict mode for safety | true |
| `fallback_enabled` | Use fallback on errors | false |

---

## Recovery Procedures

### Full Service Restart

```bash
# [Restart commands]
```

Expected downtime: _[duration]_

### Data Recovery

If data corruption detected:
1. Stop writes immediately
2. Identify corruption scope
3. Restore from backup: `[commands]`
4. Verify integrity
5. Resume service

### Disaster Recovery

RTO: _[Recovery Time Objective]_
RPO: _[Recovery Point Objective]_

Procedure:
1. Activate DR environment: `[commands]`
2. Verify data sync status
3. Update DNS/routing
4. Verify functionality
5. Communicate status

---

## Appendix: Useful Commands

```bash
# Check service status
[command]

# View recent logs
[command]

# Check current config
[command]

# Force cache clear
[command]

# Manual health check
[command]
```

---

## Change Log

| Date | Author | Change |
|:-----|:-------|:-------|
| | | Initial version |

---

*Template version: 1.0*  
*Last updated: [Date]*
