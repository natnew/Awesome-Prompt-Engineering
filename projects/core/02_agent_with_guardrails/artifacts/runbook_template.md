# Production Runbook: [Agent Name]

## Document Information

| Field | Value |
|:------|:------|
| **Agent Name** | |
| **Version** | |
| **Last Updated** | |
| **Owner** | |
| **On-Call Contact** | |

---

## 1. System Overview

### 1.1 Purpose

[What does this agent do? Who uses it? What business function does it serve?]

### 1.2 Architecture

```
[Insert architecture diagram]

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│             │    │             │    │             │
│   Input     │───▶│   Agent     │───▶│   Output    │
│             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 1.3 Dependencies

| Dependency | Purpose | Failure Impact |
|:-----------|:--------|:---------------|
| | | |
| | | |
| | | |

### 1.4 Key Configuration

| Parameter | Value | Description |
|:----------|:------|:------------|
| `max_turns` | | Maximum conversation turns |
| `max_single_refund` | | Maximum refund without approval |
| `timeout_seconds` | | Request timeout |
| | | |

---

## 2. Normal Operation

### 2.1 Expected Behavior

[Describe what normal, healthy operation looks like]

- Conversations typically resolve in X turns
- Error rate should be below X%
- P95 latency should be under X seconds
- Escalation rate should be around X%

### 2.2 Normal Metric Ranges

| Metric | Normal Range | Warning Threshold | Critical Threshold |
|:-------|:-------------|:------------------|:-------------------|
| Error rate | 0-2% | >5% | >10% |
| P95 latency | 1-3s | >5s | >10s |
| Escalation rate | 10-20% | >30% | >50% |
| Guardrail triggers/hour | 0-10 | >20 | >50 |
| | | | |

### 2.3 Daily Checks

- [ ] Review error rate trends
- [ ] Check escalation reasons
- [ ] Review guardrail triggers
- [ ] Verify monitoring is operational

### 2.4 Weekly Checks

- [ ] Review conversation samples
- [ ] Analyze escalation patterns
- [ ] Check cost trends
- [ ] Review and update this runbook if needed

---

## 3. Alerts and Responses

### 3.1 Alert: High Error Rate

**Trigger:** Error rate > 10% for 5 minutes

**Severity:** Critical

**Immediate Actions:**
1. Check if specific tool is failing
2. Check if LLM API is degraded
3. Check recent deployments
4. Consider enabling degraded mode

**Escalation:** If not resolved in 15 minutes, escalate to [team/person]

**Resolution Verification:** Error rate returns to <5%

---

### 3.2 Alert: Circuit Breaker Trips

**Trigger:** >5 circuit breaker trips in 1 hour

**Severity:** Warning

**Immediate Actions:**
1. Identify which breaker is tripping
2. Check for attack patterns (prompt injection)
3. Review recent traffic patterns
4. Check for upstream issues

**Escalation:** If pattern continues for 1 hour, escalate to [team/person]

**Resolution Verification:** No trips for 30 minutes

---

### 3.3 Alert: Guardrail Spike

**Trigger:** Guardrail triggers 3x above normal rate

**Severity:** Warning

**Immediate Actions:**
1. Identify which guardrail is triggering
2. Review sample blocked requests
3. Check for attack patterns
4. Verify guardrail is not mis-configured

**Escalation:** If sustained for 30 minutes, escalate to [team/person]

**Resolution Verification:** Trigger rate returns to normal

---

### 3.4 Alert: High Latency

**Trigger:** P95 latency > 10 seconds

**Severity:** Warning

**Immediate Actions:**
1. Check LLM API latency
2. Check tool response times
3. Check for complex queries
4. Consider rate limiting

**Escalation:** If impacting users, escalate to [team/person]

**Resolution Verification:** P95 returns to <5s

---

### 3.5 Alert: Cost Anomaly

**Trigger:** Hourly cost > 2x normal

**Severity:** Warning

**Immediate Actions:**
1. Identify high-cost conversations
2. Check for loop patterns
3. Verify circuit breakers are working
4. Consider temporary rate limiting

**Escalation:** If cost continues, escalate to [team/person]

**Resolution Verification:** Cost returns to normal range

---

## 4. Incident Response

### 4.1 Severity Classification

| Severity | Definition | Response Time | Example |
|:---------|:-----------|:--------------|:--------|
| **SEV1** | Complete outage or data breach | 15 min | Agent completely down |
| **SEV2** | Significant degradation | 30 min | 50%+ error rate |
| **SEV3** | Partial degradation | 2 hours | Single tool failing |
| **SEV4** | Minor issue | 24 hours | Cosmetic issue |

### 4.2 SEV1 Response Procedure

1. **Acknowledge** (within 5 min)
   - Acknowledge alert
   - Join incident channel
   - Begin investigation

2. **Assess** (within 10 min)
   - Determine scope of impact
   - Identify affected users
   - Decide: disable agent or continue with degraded mode

3. **Mitigate** (within 15 min)
   - Implement immediate fix OR
   - Disable agent with user-friendly message OR
   - Route all traffic to human agents

4. **Communicate** (within 20 min)
   - Update status page
   - Notify stakeholders
   - Post to incident channel

5. **Resolve**
   - Implement permanent fix
   - Verify resolution
   - Update status page

6. **Follow Up** (within 48 hours)
   - Write incident report
   - Schedule post-mortem
   - Identify action items

### 4.3 Communication Templates

**Internal Alert:**
```
🚨 [SEV1/2/3] Agent Incident

Status: [Investigating/Identified/Monitoring/Resolved]
Impact: [Description of user impact]
Started: [Time]
Current actions: [What's being done]

Updates in: #incident-channel
```

**External Status Update:**
```
We are currently experiencing issues with [service].
Impact: [User-facing description]
Status: Our team is actively investigating.
Next update: [Time]
```

---

## 5. Troubleshooting

### 5.1 Common Issues

#### Issue: Agent stuck in loop

**Symptoms:** 
- High iteration count
- Circuit breaker trips
- High token usage

**Diagnosis:**
```bash
# Check recent conversations with high turn count
[query for high-turn conversations]

# Review specific conversation
[query for conversation details]
```

**Resolution:**
- Check if tool is returning ambiguous results
- Review prompt for clarity
- Verify circuit breakers are configured correctly

---

#### Issue: High guardrail trigger rate

**Symptoms:**
- Elevated guardrail_triggers metric
- User complaints about blocked requests

**Diagnosis:**
```bash
# Check which guardrails are triggering
[query for guardrail triggers by type]

# Review sample blocked requests
[query for recent blocks]
```

**Resolution:**
- If legitimate requests blocked: adjust guardrail thresholds
- If attack: tighten guardrails, investigate source
- If misconfiguration: fix and deploy

---

#### Issue: Tool timeouts

**Symptoms:**
- High latency
- Timeout errors in logs
- Incomplete responses

**Diagnosis:**
```bash
# Check tool response times
[query for tool latency]

# Check upstream service status
[health check commands]
```

**Resolution:**
- If upstream issue: wait for resolution or enable fallback
- If our issue: check for inefficient queries
- Adjust timeout settings if needed

---

### 5.2 Diagnostic Commands

```bash
# View recent errors
[command]

# Check agent metrics
[command]

# Review conversation history
[command]

# Check guardrail status
[command]

# View circuit breaker state
[command]
```

### 5.3 Log Locations

| Log Type | Location | Retention |
|:---------|:---------|:----------|
| Application logs | | |
| Conversation logs | | |
| Audit logs | | |
| Metrics | | |

---

## 6. Maintenance

### 6.1 Deployment Procedure

1. [ ] Review changes in staging
2. [ ] Run evaluation suite
3. [ ] Verify safety tests pass
4. [ ] Deploy to canary (X%)
5. [ ] Monitor for 30 minutes
6. [ ] Roll out to production
7. [ ] Monitor for 2 hours
8. [ ] Mark deployment complete

### 6.2 Rollback Procedure

1. Identify need for rollback
2. Execute rollback: `[rollback command]`
3. Verify previous version is running
4. Monitor for stabilization
5. Investigate issue before re-deploying

### 6.3 Configuration Changes

**Low Risk Changes:**
- Logging levels
- Non-critical thresholds
- Message wording

**Medium Risk Changes:**
- Guardrail thresholds
- Tool configurations
- Rate limits

**High Risk Changes (require review):**
- Adding new tools
- Modifying guardrail logic
- Changing escalation rules

### 6.4 Scaling

| Load Level | Configuration | Notes |
|:-----------|:--------------|:------|
| Normal | | |
| High | | |
| Emergency | | |

---

## 7. Contacts

| Role | Name | Contact | Availability |
|:-----|:-----|:--------|:-------------|
| Primary On-Call | | | |
| Secondary On-Call | | | |
| Engineering Lead | | | |
| Product Owner | | | |

---

## 8. Change Log

| Date | Author | Change |
|:-----|:-------|:-------|
| | | Initial version |
| | | |

---

*This runbook should be reviewed and updated monthly or after any significant incident.*
