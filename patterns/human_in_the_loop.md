# Human-in-the-Loop

*Strategic human oversight at high-stakes decision points.*

**Competencies:** [Safety & Reliability](../COMPETENCIES.md#3-safety--reliability), [Governance & Defensibility](../COMPETENCIES.md#4-governance--defensibility)  
**Source:** [Agent with Guardrails](../projects/core/02_agent_with_guardrails/README.md)

---

## The Problem

AI systems make mistakes. Some mistakes are acceptable—a chatbot gives a slightly suboptimal answer. Others are catastrophic—an agent transfers $50,000 to the wrong account. Treating all decisions equally means either excessive human review (slow, expensive) or insufficient oversight (dangerous).

The deeper problem: as AI systems become more capable, they handle increasingly consequential decisions. Full automation trades safety for efficiency. Full human review doesn't scale.

---

## The Solution

**Insert human oversight at strategic points where the cost of errors exceeds the cost of human review.**

Not every decision needs human approval. Identify high-stakes decision points, route those to humans, and automate the rest. The goal isn't human involvement everywhere—it's human involvement where it matters.

---

## How It Works

### Step 1: Map Decision Points

Identify every point where your system makes a decision or takes an action.

```
User request
    → Interpret intent (decision)
    → Select approach (decision)
    → Retrieve information (action)
    → Generate response (decision)
    → Execute action (action)
    → Return response (action)
```

### Step 2: Assess Stakes

For each decision point, evaluate:

| Factor | Question |
|:-------|:---------|
| **Reversibility** | Can this be undone? |
| **Blast radius** | How many people are affected? |
| **Financial impact** | What's the cost of getting it wrong? |
| **Reputation risk** | Could this damage trust? |
| **Legal exposure** | Are there compliance implications? |

### Step 3: Define Thresholds

Determine when human review is required.

| Threshold Type | Example |
|:---------------|:--------|
| Value-based | Actions over $100 require approval |
| Confidence-based | Outputs with <80% confidence need review |
| Category-based | All refunds need approval |
| Anomaly-based | First-time actions for this user |

### Step 4: Design Escalation Paths

Three common patterns:

**1. Approval Required (Synchronous)**
```
Agent: "I'd like to process a refund of $150."
[Paused - awaiting approval]
Human: [Approve / Deny / Modify]
[Continue or abort]
```
Best for: High-stakes, time-tolerant decisions.

**2. Review Queue (Asynchronous)**
```
Agent: [Completes action]
[Action logged to review queue]
Human: [Reviews later, may reverse]
```
Best for: Medium-stakes, time-sensitive decisions.

**3. Parallel Notification**
```
Agent: [Completes action]
Human: [Notified, can intervene]
```
Best for: Lower-stakes, needs visibility.

### Step 5: Provide Context

Humans can't review effectively without context. Include:

- What decision is needed
- Why this was escalated
- Relevant history
- Agent's recommendation (if any)
- Time constraints
- Consequences of each choice

---

## When to Use

**Always use for:**
- Irreversible actions
- Financial transactions above threshold
- Actions affecting many users
- First-time or unusual operations
- Legally sensitive decisions

**Consider using for:**
- Low-confidence outputs
- Anomalous requests
- Edge cases not in training
- Sensitive topics

---

## When NOT to Use

- Routine, low-stakes decisions
- When human review adds no value
- When latency requirements preclude it
- When humans can't meaningfully evaluate

**Key question:** Would a human actually catch errors here, or is this theater?

---

## Examples

### Example 1: Customer Service Agent

```
Automatic (no human):
- Answer product questions
- Check order status
- Update contact info
- Refunds ≤ $50

Human approval required:
- Refunds > $50
- Account deletion
- Exceptions to policy
- Escalation to legal/compliance

Human notification:
- All refunds (review queue)
- Flagged interactions
- Negative sentiment detected
```

### Example 2: Content Moderation

```
Automatic:
- Clear policy violations (spam, illegal content)
- Obvious safe content

Human review:
- Borderline cases
- Appeals
- Novel violation types
- High-profile accounts
```

### Example 3: Code Generation

```
Automatic:
- Syntax suggestions
- Simple refactoring
- Documentation generation

Human approval required:
- Security-sensitive code
- Database schema changes
- Production deployments
- External API integrations
```

---

## Anti-Patterns

### Rubber-Stamp Reviews

**What happens:** Humans approve everything because volume is too high or context is insufficient. Review becomes theater.

**Fix:** Reduce volume by raising thresholds. Improve context. Track approval rates—if >95%, something's wrong.

### Alert Fatigue

**What happens:** Too many escalations desensitize reviewers. Important items get missed in noise.

**Fix:** Be selective. Escalate less. Make high-priority items visually distinct.

### Missing Context

**What happens:** Humans get "Approve this refund?" without knowing why it was flagged or what's unusual.

**Fix:** Design the review interface. Include history, reasoning, and stakes.

### Bottleneck Creation

**What happens:** Human review becomes the rate limiter. Users wait, business suffers.

**Fix:** Staff appropriately. Use async patterns where possible. Reconsider thresholds.

### Diffusion of Responsibility

**What happens:** "A human approved it" becomes excuse for poor system design.

**Fix:** Humans augment systems, not replace accountability. Track and improve system decisions.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Catches AI errors | Added latency |
| Accountability | Operational expense |
| Handles edge cases | Doesn't scale infinitely |
| Builds trust | Can become bottleneck |

---

## Metrics to Track

| Metric | What It Tells You |
|:-------|:------------------|
| Escalation rate | Are thresholds calibrated? |
| Approval rate | Is escalation valuable? |
| Time to review | Is staffing adequate? |
| Override rate | Are humans adding value? |
| Error rate post-approval | Are humans catching errors? |

---

## Implementation Checklist

- [ ] Mapped all decision points
- [ ] Assessed stakes for each point
- [ ] Defined clear escalation criteria
- [ ] Designed review interfaces with context
- [ ] Established escalation paths (sync/async/notify)
- [ ] Staffed appropriately
- [ ] Tracking metrics

---

## Related Patterns

- **[Defense in Depth](defense_in_depth.md)** — Human review as one defensive layer
- **[Circuit Breaker](circuit_breaker.md)** — Automatic escalation when metrics degrade
- **[Graceful Degradation](graceful_degradation.md)** — Fall back to human when AI fails

---

## Key Insight

> "Human-in-the-loop isn't about distrust of AI. It's about appropriate allocation of oversight to risk."

The goal is right-sized oversight: enough human involvement to catch consequential errors, not so much that you've built an expensive approval factory.
