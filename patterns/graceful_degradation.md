# Graceful Degradation

*Fail partially, not completely. Maintain core function when components fail.*

**Competencies:** [Safety & Reliability](../COMPETENCIES.md#3-safety--reliability), [Systems Design](../COMPETENCIES.md#5-systems-design--integration)  
**Source:** [Agent with Guardrails](../projects/core/02_agent_with_guardrails/README.md)

---

## The Problem

AI systems have dependencies: model APIs, databases, external services, network connectivity. Any of these can fail. If your system handles failure with "500 Internal Server Error," users get nothing when they could have gotten something.

The deeper problem: partial failure is more common than complete failure. A slow API isn't down—it's degraded. A model returning low-confidence outputs isn't broken—it's uncertain. Binary thinking (works/broken) misses the spectrum.

---

## The Solution

**Design fallback behaviors for every failure mode. When the best option fails, provide the next best option, not nothing.**

Graceful degradation means users always get value—even if reduced. A search system with a slow embedding model can fall back to keyword search. An agent with tool failures can acknowledge the limitation and offer alternatives.

---

## How It Works

### Step 1: Identify Dependencies

List everything your system depends on:

```
- Model API (OpenAI, Anthropic, etc.)
- Vector database
- Traditional database
- Cache layer
- External APIs
- Network connectivity
- Compute resources
```

### Step 2: Define Failure Modes

For each dependency, enumerate how it might fail:

| Dependency | Failure Modes |
|:-----------|:--------------|
| Model API | Timeout, rate limit, errors, degraded quality, complete outage |
| Database | Slow queries, connection failure, stale data |
| External API | Timeout, rate limit, bad data, outage |
| Cache | Miss, connection failure, stale data |

### Step 3: Design Fallback Hierarchy

For each failure mode, define what happens instead:

```
Primary: Full AI-powered response
    ↓ (if model API fails)
Fallback 1: Cached similar response
    ↓ (if cache miss)
Fallback 2: Template-based response
    ↓ (if no template matches)
Fallback 3: Acknowledge limitation, offer alternatives
    ↓ (if user needs immediate help)
Fallback 4: Route to human
```

### Step 4: Communicate Degradation

Users should know when they're getting degraded service:

```
Full service: "Here's your answer..."
Degraded: "I'm experiencing some limitations right now. 
          Here's what I can tell you: [partial answer]. 
          For complete information, you might also try: [alternative]"
Minimal: "I can't fully process your request right now. 
         Let me connect you with someone who can help."
```

---

## Fallback Strategies

### Strategy 1: Simpler Model

When primary model fails, use a simpler/faster one.

```
Primary: GPT-4 with complex reasoning
Fallback: GPT-3.5 with simpler prompt
Fallback: Rule-based response
```

**Trade-off:** Lower quality, but available.

### Strategy 2: Cached Responses

Pre-compute responses for common queries.

```
Primary: Live model inference
Fallback: Semantically similar cached response
Fallback: Exact match from cache
```

**Trade-off:** May be stale, but fast.

### Strategy 3: Reduced Scope

Do less, but do it reliably.

```
Primary: Full analysis with recommendations
Fallback: Summary without recommendations
Fallback: Acknowledge receipt, promise follow-up
```

**Trade-off:** Less helpful, but honest.

### Strategy 4: Human Handoff

When AI can't help, humans can.

```
Primary: AI resolves request
Fallback: AI drafts, human reviews
Fallback: Direct to human queue
```

**Trade-off:** Slower, but reliable.

### Strategy 5: Informative Failure

If nothing else works, fail informatively.

```
Bad: "Error 500"
Good: "I'm unable to process this request right now. 
      This usually resolves within a few minutes. 
      You can also try [alternative] or contact [support]."
```

---

## When to Use

**Always use for:**
- Production user-facing systems
- Systems with external dependencies
- Systems where availability matters
- Any system that could fail partially

**Especially important when:**
- Dependencies have variable reliability
- Users have urgent needs
- Partial answers have value
- Complete failure has high cost

---

## When NOT to Use

- When partial results are dangerous (better to fail completely)
- When fallbacks would mislead users
- Internal tools where failure is acceptable

**Key question:** Is a degraded response better than no response?

---

## Examples

### Example 1: Search System

```
Query: "How do I reset my password?"

Primary (working):
  → Embedding search → Rerank → Generate answer
  Result: "To reset your password, go to Settings > Security..."

Embedding API timeout:
  → Keyword search → Direct document match
  Result: "I found this help article: [Password Reset Guide]"

All search fails:
  → FAQ fallback
  Result: "Here's our most common password question: 
          [link to password reset docs]"

Complete failure:
  → Graceful error
  Result: "I'm having trouble searching right now. 
          You can browse our help center at [link] or 
          contact support at [email]."
```

### Example 2: Code Assistant

```
Request: "Help me write a function to parse JSON"

Primary (working):
  → Full code generation with explanation
  Result: [Complete function + explanation + edge cases]

Model degraded (high latency):
  → Simpler generation, no explanation
  Result: [Function only, minimal comments]

Model unavailable:
  → Template/snippet library
  Result: "Here's a common JSON parsing pattern: [snippet]. 
          I can't customize it right now, but this should help."

Complete failure:
  Result: "I can't generate code right now. 
          Try the Python docs: [json module link]"
```

### Example 3: Agent with Tools

```
User: "What's the weather in Tokyo?"

Primary (working):
  → Call weather API → Format response
  Result: "It's currently 72°F and sunny in Tokyo..."

Weather API timeout:
  → Return cached recent data
  Result: "As of 2 hours ago, Tokyo was 71°F and partly cloudy. 
          I couldn't get live data right now."

Weather API down:
  → Acknowledge limitation
  Result: "I can't check the weather right now. 
          You can try weather.com or your phone's weather app."
```

---

## Anti-Patterns

### Silent Degradation

**What happens:** System uses fallback but doesn't tell users. They think they're getting full service.

**Fix:** Always communicate degradation. Users can make informed decisions.

### Degradation Loops

**What happens:** Fallback triggers another fallback triggers another... System thrashes.

**Fix:** Limit fallback depth. Have a terminal state.

### Dangerous Fallbacks

**What happens:** Fallback provides inaccurate or harmful responses to maintain availability.

**Fix:** Sometimes failing is better than being wrong. Know when to stop.

### Untested Fallbacks

**What happens:** Fallback code path never runs in production, breaks when needed.

**Fix:** Regularly test fallbacks. Chaos engineering. Synthetic failures.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Higher availability | Implementation complexity |
| Better user experience | More code paths to maintain |
| Partial value beats nothing | May mask underlying problems |
| Resilience to failures | Need to test all fallback paths |

---

## Implementation Checklist

- [ ] Enumerated all dependencies
- [ ] Identified failure modes for each
- [ ] Designed fallback for each failure mode
- [ ] Fallbacks provide decreasing value (not increasing risk)
- [ ] Users informed of degradation
- [ ] Fallback paths tested regularly
- [ ] Monitoring distinguishes primary vs. fallback usage

---

## Related Patterns

- **[Circuit Breaker](circuit_breaker.md)** — Trigger fallbacks automatically
- **[Defense in Depth](defense_in_depth.md)** — Fallbacks as a defensive layer
- **[Human-in-the-Loop](human_in_the_loop.md)** — Humans as ultimate fallback

---

## Key Insight

> "The question isn't 'will this fail?' It's 'what happens when it does?'"

Graceful degradation is optimism about failure: users always get something, even when the ideal path breaks.
