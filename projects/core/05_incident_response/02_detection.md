[← Back: Incident Framework](01_incident_framework.md) | [Next: Response →](03_response.md)

# Module 2: Detection

Know something is wrong before users tell you.

---

## The Detection Challenge

AI system failures are often subtle:

| Traditional System | AI System |
|:-------------------|:----------|
| Returns error code | Returns plausible-looking wrong answer |
| Crashes on bad input | Hallucinates on bad input |
| Fails visibly | Fails silently |
| Binary: works or doesn't | Spectrum: better or worse |

This makes detection harder but more important.

---

## Detection Sources

### Source 1: Automated Monitoring

**What to monitor:**

| Metric | What It Catches | Alert Threshold |
|:-------|:----------------|:----------------|
| Error rate | System failures | > 5% |
| Latency (P95) | Performance degradation | > 5s |
| Token usage | Cost anomalies | > 2x normal |
| Guardrail triggers | Safety issues | > 2x normal |
| API response codes | Upstream issues | Any 5xx |
| Queue depth | Processing backlog | Growing |

**Example alerts:**

```yaml
# High error rate
alert: ai_high_error_rate
condition: error_rate > 0.05 for 5m
severity: SEV2
runbook: /runbooks/high-error-rate.md

# Cost spike
alert: ai_cost_anomaly
condition: hourly_cost > 3 * avg_hourly_cost_7d
severity: SEV3
runbook: /runbooks/cost-spike.md

# Quality degradation (if measurable)
alert: ai_quality_drop
condition: quality_score < 0.8 * baseline
severity: SEV3
runbook: /runbooks/quality-degradation.md
```

### Source 2: User Reports

Users often detect issues before monitoring:

**User signals:**
- "This answer doesn't seem right"
- "It's being weird today"
- "It gave me wrong information"
- "Something is slow"

**How to capture:**
- In-product feedback mechanisms (thumbs down, report button)
- Support ticket keywords
- Social media monitoring
- Sales/customer success escalations

### Source 3: Proactive Testing

Don't wait for problems to find you:

**Continuous testing:**
- Run evaluation suite on schedule
- Test canary queries hourly
- Compare responses to baseline
- Alert on drift

**Example canary test:**

```python
CANARY_QUERIES = [
    ("What is 2+2?", "4"),
    ("Who was the first US president?", "George Washington"),
    ("Is the sky blue?", "yes"),
]

def run_canary():
    failures = []
    for query, expected_substring in CANARY_QUERIES:
        response = ai_system.query(query)
        if expected_substring.lower() not in response.lower():
            failures.append((query, response))
    
    if failures:
        alert("Canary test failed", failures)
```

### Source 4: Anomaly Detection

Look for patterns that don't match expectations:

**Behavioral anomalies:**
- Sudden change in response length
- Unusual vocabulary patterns
- Repeated responses
- Very fast or very slow responses

**Usage anomalies:**
- Spike in requests from single user
- Unusual query patterns
- Requests at unusual times

---

## Detection Speed

Time to detect determines incident impact.

```
                    DETECTION TIMELINE
                    
   Automated      User       Manual       Never
   alert          report     discovery    detected
   │              │          │            │
   ▼              ▼          ▼            ▼
───●──────────────●──────────●────────────●────────▶
   5 min          30 min     Hours-Days   ∞
   
   │              │          │            │
   ▼              ▼          ▼            ▼
   Best           Good       Risky        Bad
```

**Goal:** Detect issues automatically within minutes, not hours.

---

## AI-Specific Detection Challenges

### Challenge 1: No Ground Truth

How do you know if an answer is wrong?

**Approaches:**
- Compare to golden answers (for known queries)
- LLM-as-judge (for general queries)
- User feedback (lagging indicator)
- Human review (expensive, sampled)

### Challenge 2: Gradual Degradation

Quality might decline slowly, not suddenly.

**Approaches:**
- Track quality metrics over time
- Compare to baseline, not just threshold
- Use trend alerts, not just point alerts

### Challenge 3: Non-Determinism

Same query might give different answers.

**Approaches:**
- Test with fixed seeds if possible
- Use aggregate metrics over samples
- Compare distributions, not individual responses

---

## Building Your Detection System

### Step 1: Define What "Wrong" Means

For your system, what are the failure modes?

| Failure Mode | How It Manifests | How to Detect |
|:-------------|:-----------------|:--------------|
| Wrong answers | Incorrect information | Human review, LLM judge |
| Refusal to answer | "I can't help with that" | Response classification |
| Irrelevant answers | Doesn't address query | Relevance scoring |
| Harmful answers | Inappropriate content | Content filtering |
| Slow responses | High latency | Latency monitoring |
| No response | Timeout/error | Error monitoring |

### Step 2: Choose Detection Methods

| Failure Mode | Primary Detection | Secondary Detection |
|:-------------|:------------------|:-------------------|
| | | |
| | | |
| | | |

### Step 3: Set Thresholds

| Alert | Warning Threshold | Critical Threshold | Notes |
|:------|:------------------|:-------------------|:------|
| | | | |
| | | | |
| | | | |

### Step 4: Reduce Noise

Too many alerts = ignored alerts.

**Strategies:**
- Tune thresholds based on history
- Group related alerts
- Use alert suppression during maintenance
- Route low-priority alerts to queue, not page

---

## Detection Runbook Template

For each alert, document:

```markdown
## Alert: [Name]

### What It Means
[Description of what this alert indicates]

### Severity
SEV1/2/3/4

### Likely Causes
1. [Cause 1]
2. [Cause 2]
3. [Cause 3]

### Immediate Actions
1. [ ] [Action 1]
2. [ ] [Action 2]

### Investigation Steps
1. Check [X] for [Y]
2. Look at [logs/metrics] for [Z]

### Escalation
If [condition], escalate to [who]

### Resolution Criteria
Alert can be closed when:
- [Criterion 1]
- [Criterion 2]
```

---

## Your Task

Design detection for your AI system:

1. **List failure modes** specific to your system
2. **Map detection methods** for each failure mode
3. **Define alerts** with thresholds and runbooks
4. **Plan user feedback** capture mechanisms
5. **Design canary tests** for critical functionality

---

## Key Insight

**The best time to detect an incident is before users do.**

Invest in automated detection. Every minute of faster detection is a minute of reduced impact.

---

[← Back: Incident Framework](01_incident_framework.md) | [Next: Response →](03_response.md)
