# Defense in Depth

*Multiple independent safety layers, each assuming others will fail.*

**Competencies:** [Safety & Reliability](../COMPETENCIES.md#3-safety--reliability)  
**Source:** [Agent with Guardrails](../projects/core/02_agent_with_guardrails/README.md)

---

## The Problem

No single safety measure is perfect. Input validation can be bypassed. Content filters have blind spots. Model guidelines can be jailbroken. If your entire safety strategy depends on one component, a single failure means complete compromise.

The deeper problem: AI systems face adversarial users, unexpected inputs, and model behaviors that surprise even their creators. You can't anticipate every failure mode.

---

## The Solution

**Layer multiple independent safety mechanisms. Design each layer assuming the others have already failed.**

If an attacker bypasses Layer 1, Layer 2 is waiting. If Layers 1 and 2 fail, Layer 3 catches it. No single point of failure. Each layer provides defense for a different failure mode.

---

## How It Works

### The Layers

```
┌─────────────────────────────────────────────────┐
│                  INPUT LAYER                     │
│  Validate, sanitize, and filter before processing│
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│                PROCESSING LAYER                  │
│  Constrain what the system can do during execution│
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│                 OUTPUT LAYER                     │
│  Filter, validate, and redact before returning   │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│               MONITORING LAYER                   │
│  Detect and respond to anomalies in real-time    │
└─────────────────────────────────────────────────┘
```

### Layer 1: Input Defenses

Stop bad inputs before they enter the system.

| Defense | What It Catches |
|:--------|:----------------|
| Input validation | Malformed requests, type errors |
| Prompt injection detection | Attempts to override instructions |
| Rate limiting | Abuse, DoS attempts |
| Authentication | Unauthorized access |
| Scope validation | Out-of-bounds requests |

**Key principle:** Assume malicious intent. Validate everything.

### Layer 2: Processing Defenses

Constrain what can happen during execution.

| Defense | What It Catches |
|:--------|:----------------|
| Tool allowlisting | Unauthorized capabilities |
| Parameter validation | Dangerous arguments |
| Action limits | Exceeded thresholds (refunds, deletions) |
| Timeout/iteration limits | Infinite loops |
| Sandboxing | Scope creep |

**Key principle:** Minimize privilege. Allow only what's necessary.

### Layer 3: Output Defenses

Catch problems before they reach users.

| Defense | What It Catches |
|:--------|:----------------|
| Content filtering | Harmful/inappropriate content |
| PII detection | Data leakage |
| Factuality checking | Hallucinations (where possible) |
| Format validation | Malformed responses |
| Confidence thresholds | Low-quality outputs |

**Key principle:** Don't trust internal outputs. Verify before releasing.

### Layer 4: Monitoring Defenses

Detect and respond to problems in real-time.

| Defense | What It Catches |
|:--------|:----------------|
| Anomaly detection | Unusual patterns |
| Alert thresholds | Metric degradation |
| Audit logging | Policy violations |
| Circuit breakers | Cascading failures |

**Key principle:** Assume failures will happen. Detect them fast.

---

## Independence Principle

**Each layer must be independently effective.** If Layer 1 and Layer 2 use the same underlying check, they're not independent—they're one layer with two names.

Good independence:
- Input: Regex pattern matching
- Processing: LLM-based content classification
- Output: Keyword blocklist

Bad independence:
- Input: GPT-4 classifier
- Processing: GPT-4 classifier (same model)
- Output: GPT-4 classifier (single point of failure)

---

## When to Use

**Always use for:**
- User-facing AI systems
- Systems that take actions (agents)
- Systems handling sensitive data
- Systems in regulated domains

**Especially important when:**
- Adversarial users are expected
- Failure consequences are severe
- System behavior is unpredictable
- You can't enumerate all failure modes

---

## When NOT to Use

- Internal tools with trusted users only
- Offline batch processing with human review
- Prototypes not exposed to real users

Even then, consider lightweight layering. Habits built in development carry to production.

---

## Examples

### Example: Customer Service Agent

```
Layer 1 (Input):
├── Authentication (valid session)
├── Rate limiting (10 requests/minute)
├── Injection detection (pattern matching)
└── Scope check (is this a support question?)

Layer 2 (Processing):
├── Tool allowlist (lookup, refund ≤$50)
├── Action limits (max 3 actions/request)
├── Refund cap ($100/day cumulative)
└── Iteration limit (10 turns max)

Layer 3 (Output):
├── PII filter (redact SSN, CC numbers)
├── Content filter (no profanity)
├── Policy compliance (required disclosures)
└── Confidence check (escalate if uncertain)

Layer 4 (Monitoring):
├── Error rate alerting (>5% triggers)
├── Cost tracking ($1/hour limit)
├── Safety violation logging
└── Human escalation queue
```

### What Happens When Layer 1 Fails

User submits prompt injection that bypasses input detection:
- Layer 2: Tool allowlist prevents unauthorized actions
- Layer 2: Refund cap limits financial damage
- Layer 3: PII filter prevents data leakage
- Layer 4: Unusual pattern triggers alert

**Result:** Contained incident, not catastrophic breach.

---

## Anti-Patterns

### Security Theater

**What happens:** Layers look independent but share failure modes. Multiple checks that all fail together.

**Fix:** Audit each layer's actual independence. Use diverse techniques.

### All-or-Nothing

**What happens:** One layer is extremely strict, others are lax. When the strict layer fails, nothing catches it.

**Fix:** Distribute protection across layers. Each should catch something.

### Performance Excuse

**What happens:** "We can't afford the latency" becomes justification for removing layers.

**Fix:** Optimize layers, don't remove them. Cache where possible. Async where acceptable.

### Checkbox Compliance

**What happens:** Layers exist but aren't maintained. Blocklists are outdated. Patterns don't match current attacks.

**Fix:** Treat layers as living systems. Regular review and updates.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| No single point of failure | Added latency |
| Catches diverse failures | Implementation complexity |
| Limits blast radius | More code to maintain |
| Provides defense against unknowns | False positive potential |

---

## Implementation Checklist

- [ ] Identified at least 3 independent layers
- [ ] Each layer uses different techniques
- [ ] No shared dependencies between layers
- [ ] Each layer effective if others fail
- [ ] Monitoring covers all layers
- [ ] Regular review schedule for each layer

---

## Related Patterns

- **[Circuit Breaker](circuit_breaker.md)** — Automatic containment when layers fail
- **[Human-in-the-Loop](human_in_the_loop.md)** — Human layer for high-stakes decisions
- **[Graceful Degradation](graceful_degradation.md)** — What to do when layers trigger

---

## Key Insight

> "Assume each layer will fail. Design the next layer as if it already has."

Security isn't about building an impenetrable wall. It's about slowing attackers enough that you detect and respond before real damage occurs.
