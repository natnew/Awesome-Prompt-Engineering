# Circuit Breaker

*Automatic failure containment. Stop cascading problems before they spread.*

**Competencies:** [Safety & Reliability](../COMPETENCIES.md#3-safety--reliability), [Systems Design](../COMPETENCIES.md#5-systems-design--integration)  
**Source:** [Agent with Guardrails](../projects/core/02_agent_with_guardrails/README.md)

---

## The Problem

AI systems can fail in ways that compound: an agent stuck in a loop burns through API budget. A slow dependency backs up requests until the whole system crashes. An error in one request triggers retries that amplify the problem. Without automatic intervention, small issues become catastrophic.

The deeper problem: by the time a human notices, the damage is done. You need automatic responses that act faster than humans can react.

---

## The Solution

**Implement automatic tripwires that halt or limit operation when thresholds are exceeded.**

Like an electrical circuit breaker that cuts power when current exceeds safe levels, software circuit breakers cut off problematic operations before they cause wider damage. They're the immune system of your AI application.

---

## How It Works

### Circuit Breaker States

```
     ┌──────────────────────────────────────────────────┐
     │                                                   │
     ▼                                                   │
┌─────────┐    failures > threshold    ┌─────────┐      │
│ CLOSED  │ ─────────────────────────▶ │  OPEN   │      │
│ (normal)│                            │ (broken)│      │
└─────────┘                            └─────────┘      │
     ▲                                       │          │
     │          timeout expires              ▼          │
     │                               ┌────────────┐     │
     │         success               │ HALF-OPEN  │     │
     └───────────────────────────────│  (testing) │─────┘
                                     └────────────┘
                                           │
                                     failure │
                                           ▼
                                     back to OPEN
```

**CLOSED:** Normal operation. Requests flow through. Failures are counted.

**OPEN:** Circuit tripped. All requests fail immediately (or use fallback). No load on failing system.

**HALF-OPEN:** Testing recovery. Limited requests allowed through. Success closes circuit; failure reopens.

### Types of Circuit Breakers

#### 1. Iteration Breaker

Limits how many steps an agent can take.

```python
class IterationBreaker:
    def __init__(self, max_iterations: int = 10):
        self.max = max_iterations
        self.count = 0
    
    def check(self):
        self.count += 1
        if self.count > self.max:
            raise CircuitBroken("Max iterations exceeded")
```

**Use when:** Agents, loops, recursive processes.

#### 2. Time Breaker

Limits how long an operation can run.

```python
class TimeBreaker:
    def __init__(self, timeout_seconds: float = 60):
        self.timeout = timeout_seconds
        self.start = time.time()
    
    def check(self):
        elapsed = time.time() - self.start
        if elapsed > self.timeout:
            raise CircuitBroken(f"Timeout after {elapsed:.1f}s")
```

**Use when:** Any operation with variable duration.

#### 3. Cost Breaker

Limits spending on API calls.

```python
class CostBreaker:
    def __init__(self, budget_usd: float = 1.0):
        self.budget = budget_usd
        self.spent = 0.0
    
    def record(self, cost: float):
        self.spent += cost
        if self.spent > self.budget:
            raise CircuitBroken(f"Budget exceeded: ${self.spent:.2f}")
```

**Use when:** LLM API calls, external service usage.

#### 4. Error Rate Breaker

Trips when errors exceed threshold.

```python
class ErrorRateBreaker:
    def __init__(self, threshold: float = 0.5, window: int = 10):
        self.threshold = threshold
        self.window = window
        self.results = deque(maxlen=window)
    
    def record(self, success: bool):
        self.results.append(success)
        if len(self.results) >= self.window:
            error_rate = 1 - (sum(self.results) / len(self.results))
            if error_rate > self.threshold:
                raise CircuitBroken(f"Error rate {error_rate:.0%}")
```

**Use when:** External dependencies, model calls.

#### 5. Consecutive Failure Breaker

Trips after N failures in a row.

```python
class ConsecutiveFailureBreaker:
    def __init__(self, max_consecutive: int = 3):
        self.max = max_consecutive
        self.consecutive = 0
    
    def record(self, success: bool):
        if success:
            self.consecutive = 0
        else:
            self.consecutive += 1
            if self.consecutive >= self.max:
                raise CircuitBroken(f"{self.consecutive} consecutive failures")
```

**Use when:** Dependencies that fail intermittently vs. completely.

---

## When to Use

**Always use for:**
- Agent loops (prevent infinite execution)
- API calls (prevent cost explosion)
- External dependencies (prevent cascade failures)
- User-facing systems (prevent poor experience)

**Especially important when:**
- Operations can run unbounded
- Costs scale with usage
- Failures can cascade
- Human reaction time is too slow

---

## When NOT to Use

- Operations with natural bounds
- When you want to exhaust all options before failing
- When false positives are very costly

Even then, consider very high thresholds rather than no breaker.

---

## Examples

### Example 1: Agent with Multiple Breakers

```python
class GuardedAgent:
    def __init__(self):
        self.iteration_breaker = IterationBreaker(max=10)
        self.time_breaker = TimeBreaker(timeout=60)
        self.cost_breaker = CostBreaker(budget=1.0)
        self.error_breaker = ErrorRateBreaker(threshold=0.5)
    
    def run(self, task):
        while not task.complete:
            # Check all breakers
            self.iteration_breaker.check()
            self.time_breaker.check()
            
            try:
                result = self.execute_step(task)
                cost = self.estimate_cost(result)
                self.cost_breaker.record(cost)
                self.error_breaker.record(success=True)
            except Exception as e:
                self.error_breaker.record(success=False)
                # Continue or break based on error type
```

### Example 2: API Client with Circuit Breaker

```python
class ModelClient:
    def __init__(self):
        self.breaker = ErrorRateBreaker(threshold=0.3, window=20)
        self.state = "CLOSED"
        self.open_until = None
    
    def call(self, prompt):
        if self.state == "OPEN":
            if time.time() < self.open_until:
                return self.fallback(prompt)
            self.state = "HALF-OPEN"
        
        try:
            result = self._make_request(prompt)
            self.breaker.record(success=True)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
            return result
        except Exception as e:
            self.breaker.record(success=False)
            if self.breaker.is_tripped():
                self.state = "OPEN"
                self.open_until = time.time() + 30  # 30s timeout
            raise
```

### Example 3: Cost-Aware Pipeline

```python
class CostAwarePipeline:
    def __init__(self, hourly_budget=100):
        self.hourly_budget = hourly_budget
        self.hour_start = time.time()
        self.hour_cost = 0
    
    def process(self, request):
        # Reset hourly counter
        if time.time() - self.hour_start > 3600:
            self.hour_start = time.time()
            self.hour_cost = 0
        
        # Check budget
        if self.hour_cost >= self.hourly_budget:
            raise CircuitBroken("Hourly budget exhausted")
        
        result = self._process(request)
        self.hour_cost += result.cost
        
        # Warn at 80%
        if self.hour_cost > self.hourly_budget * 0.8:
            self.alert("Approaching hourly budget limit")
        
        return result
```

---

## Anti-Patterns

### Too Sensitive

**What happens:** Circuit trips on normal variation. Constant false positives.

**Fix:** Tune thresholds based on real data. Use percentiles, not absolutes.

### Too Insensitive

**What happens:** Circuit never trips. Problems cascade before intervention.

**Fix:** Start conservative, loosen based on evidence.

### No Recovery Path

**What happens:** Circuit opens but nothing recovers it. System stays broken.

**Fix:** Implement half-open state. Automatic recovery testing.

### Silent Tripping

**What happens:** Circuit trips but no one knows. Users see errors with no context.

**Fix:** Alert on trip. Log extensively. Provide user-facing message.

### Single Global Breaker

**What happens:** One bad endpoint trips the breaker for everything.

**Fix:** Granular breakers per dependency, per operation type.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Automatic containment | May interrupt legitimate work |
| Fast response | Tuning required |
| Cost protection | False positives possible |
| Prevents cascade | Added complexity |

---

## Implementation Checklist

- [ ] Identified operations needing breakers
- [ ] Chose appropriate breaker types for each
- [ ] Set thresholds based on data (not guesses)
- [ ] Implemented recovery paths (half-open state)
- [ ] Added alerting when breakers trip
- [ ] Defined fallback behaviors
- [ ] Tested breaker behavior (including recovery)

---

## Related Patterns

- **[Defense in Depth](defense_in_depth.md)** — Breakers as one defensive layer
- **[Graceful Degradation](graceful_degradation.md)** — What happens when breakers trip
- **[Human-in-the-Loop](human_in_the_loop.md)** — Escalate when breakers trip repeatedly

---

## Key Insight

> "The best time to stop a runaway process is before it runs away. The second best time is automatically, the moment it starts."

Circuit breakers are about accepting that failures happen, and responding faster than humans can.
