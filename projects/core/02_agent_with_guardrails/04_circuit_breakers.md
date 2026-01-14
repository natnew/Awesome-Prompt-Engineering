[← Back: Guardrails](03_guardrails.md) | [Next: Monitoring →](05_monitoring.md)

# Module 4: Circuit Breakers

Stop runaway processes before they cause damage.

---

## What Are Circuit Breakers?

Circuit breakers are mechanisms that **automatically stop** processes when they detect anomalous behavior. The name comes from electrical circuit breakers that trip when current exceeds safe levels.

```
Normal Operation              Circuit Breaker Trips
───────────────────           ─────────────────────

Agent ──▶ Tool ──▶ Result     Agent ──▶ Tool ──▶ ERROR
Agent ──▶ Tool ──▶ Result              │
Agent ──▶ Tool ──▶ Result              ▼
Agent ──▶ Tool ──▶ Result     [CIRCUIT OPEN - STOPPED]
  ...continues...                      │
                                       ▼
                              Human notified
```

---

## Why Circuit Breakers Matter

Without circuit breakers, an agent can:

| Problem | Consequence |
|:--------|:------------|
| Infinite reasoning loop | Burns API credits indefinitely |
| Retry storm | Overwhelms downstream services |
| Resource exhaustion | Takes down the system |
| Cost explosion | $$$$ in unexpected charges |
| Cascading failures | One problem spreads everywhere |

Circuit breakers convert **unbounded failures** into **bounded failures**.

---

## Types of Circuit Breakers

### 1. Iteration Limits

Stop after too many iterations of a loop.

```python
class IterationBreaker:
    """Stop after max iterations."""
    
    def __init__(self, max_iterations: int = 10):
        self.max_iterations = max_iterations
        self.current = 0
    
    def tick(self) -> bool:
        """Call each iteration. Returns True if should continue."""
        self.current += 1
        if self.current > self.max_iterations:
            raise CircuitBreakerTripped(
                breaker="iteration",
                message=f"Exceeded {self.max_iterations} iterations",
                current=self.current
            )
        return True
    
    def reset(self):
        self.current = 0
```

**Usage:**
```python
breaker = IterationBreaker(max_iterations=10)

while not done:
    breaker.tick()  # Raises after 10 iterations
    action = agent.get_next_action()
    result = execute(action)
```

### 2. Time Limits

Stop after too much time has elapsed.

```python
class TimeBreaker:
    """Stop after max duration."""
    
    def __init__(self, max_seconds: float = 60.0):
        self.max_seconds = max_seconds
        self.start_time = None
    
    def start(self):
        self.start_time = time.time()
    
    def check(self) -> bool:
        """Returns True if within time limit."""
        if self.start_time is None:
            self.start()
        
        elapsed = time.time() - self.start_time
        if elapsed > self.max_seconds:
            raise CircuitBreakerTripped(
                breaker="time",
                message=f"Exceeded {self.max_seconds}s time limit",
                elapsed=elapsed
            )
        return True
```

### 3. Cost Limits

Stop after spending too much on API calls.

```python
class CostBreaker:
    """Stop after max cost incurred."""
    
    def __init__(self, max_cost: float = 1.0):
        self.max_cost = max_cost
        self.current_cost = 0.0
    
    def add_cost(self, cost: float):
        """Track cost of an operation."""
        self.current_cost += cost
        if self.current_cost > self.max_cost:
            raise CircuitBreakerTripped(
                breaker="cost",
                message=f"Exceeded ${self.max_cost:.2f} cost limit",
                current_cost=self.current_cost
            )
    
    def estimate_and_check(self, tokens: int, model: str):
        """Estimate cost before making a call."""
        estimated_cost = self._estimate_cost(tokens, model)
        if self.current_cost + estimated_cost > self.max_cost:
            raise CircuitBreakerTripped(
                breaker="cost",
                message="Would exceed cost limit",
                current_cost=self.current_cost,
                estimated_additional=estimated_cost
            )
```

### 4. Error Rate Limits

Stop after too many failures.

```python
class ErrorRateBreaker:
    """Stop after too many errors."""
    
    def __init__(self, max_errors: int = 3, window_seconds: float = 60.0):
        self.max_errors = max_errors
        self.window_seconds = window_seconds
        self.errors: list[float] = []  # Timestamps of errors
    
    def record_error(self, error: Exception):
        """Record an error occurrence."""
        now = time.time()
        
        # Remove old errors outside window
        self.errors = [t for t in self.errors if now - t < self.window_seconds]
        
        # Add new error
        self.errors.append(now)
        
        if len(self.errors) >= self.max_errors:
            raise CircuitBreakerTripped(
                breaker="error_rate",
                message=f"{self.max_errors} errors in {self.window_seconds}s",
                errors=len(self.errors),
                original_error=str(error)
            )
    
    def record_success(self):
        """Optionally clear errors on success."""
        pass  # Or: self.errors.clear()
```

### 5. Tool-Specific Limits

Stop after too many calls to a specific tool.

```python
class ToolCallBreaker:
    """Limit calls to specific tools."""
    
    def __init__(self, limits: dict[str, int]):
        """
        limits: {"process_refund": 5, "send_email": 3}
        """
        self.limits = limits
        self.counts: dict[str, int] = defaultdict(int)
    
    def check_tool(self, tool_name: str):
        """Check before calling a tool."""
        if tool_name in self.limits:
            self.counts[tool_name] += 1
            if self.counts[tool_name] > self.limits[tool_name]:
                raise CircuitBreakerTripped(
                    breaker="tool_calls",
                    message=f"Exceeded {self.limits[tool_name]} calls to {tool_name}",
                    tool=tool_name,
                    count=self.counts[tool_name]
                )
```

---

## The Circuit Breaker Manager

Combine multiple breakers into a single manager:

```python
class CircuitBreakerManager:
    """Manages multiple circuit breakers."""
    
    def __init__(self, config: AgentConfig):
        self.breakers = {
            'iteration': IterationBreaker(config.max_turns),
            'time': TimeBreaker(config.max_conversation_duration_seconds),
            'cost': CostBreaker(config.max_cost_per_conversation),
            'errors': ErrorRateBreaker(max_errors=3),
            'tools': ToolCallBreaker({
                'process_refund': 5,
                'send_email': 3,
            })
        }
        self.tripped = False
        self.trip_reason = None
    
    def check_all(self):
        """Run all breaker checks."""
        if self.tripped:
            raise CircuitBreakerTripped(
                breaker="already_tripped",
                message=f"Circuit already open: {self.trip_reason}"
            )
        
        for name, breaker in self.breakers.items():
            if hasattr(breaker, 'check'):
                breaker.check()
    
    def on_iteration(self):
        """Call at start of each iteration."""
        self.breakers['iteration'].tick()
        self.breakers['time'].check()
    
    def on_tool_call(self, tool_name: str, estimated_cost: float = 0):
        """Call before each tool call."""
        self.breakers['tools'].check_tool(tool_name)
        if estimated_cost > 0:
            self.breakers['cost'].estimate_and_check(estimated_cost)
    
    def on_error(self, error: Exception):
        """Call when an error occurs."""
        try:
            self.breakers['errors'].record_error(error)
        except CircuitBreakerTripped:
            self.tripped = True
            self.trip_reason = f"error_rate: {error}"
            raise
    
    def on_cost(self, cost: float):
        """Call after incurring cost."""
        self.breakers['cost'].add_cost(cost)
```

---

## Integration with Agent

```python
class GuardedAgent:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.circuit_breakers = CircuitBreakerManager(config)
        self.guardrails = GuardrailPipeline()
    
    async def process(self, user_input: str) -> AgentResponse:
        try:
            return await self._process_with_breakers(user_input)
        except CircuitBreakerTripped as e:
            return self._handle_circuit_breaker(e)
    
    async def _process_with_breakers(self, user_input: str) -> AgentResponse:
        while not self._should_stop():
            # Check breakers at start of each iteration
            self.circuit_breakers.on_iteration()
            
            # Get next action
            action = await self._get_next_action()
            
            if action.type == "respond":
                break
            
            # Check breakers before tool call
            self.circuit_breakers.on_tool_call(
                action.tool_name,
                estimated_cost=self._estimate_cost(action)
            )
            
            try:
                result = await self._execute_action(action)
                self.circuit_breakers.on_cost(result.cost)
            except Exception as e:
                self.circuit_breakers.on_error(e)
                # Handle or re-raise
        
        return await self._generate_response()
    
    def _handle_circuit_breaker(self, error: CircuitBreakerTripped) -> AgentResponse:
        """Handle a tripped circuit breaker."""
        
        # Log the event
        self._log_circuit_breaker(error)
        
        # Notify if needed
        if error.breaker in ['cost', 'error_rate']:
            self._notify_oncall(error)
        
        # Return graceful response to user
        return AgentResponse(
            content="I apologize, but I'm unable to complete this request right now. "
                    "A support representative will follow up with you shortly.",
            metadata={
                "circuit_breaker_tripped": True,
                "breaker": error.breaker,
                "escalated": True
            }
        )
```

---

## Graceful Degradation

When a circuit breaker trips, the system should degrade gracefully:

### Strategy 1: Fallback Response

```python
def handle_breaker_trip(breaker_type: str) -> str:
    fallbacks = {
        "iteration": "I wasn't able to complete that task. Let me connect you with a representative.",
        "time": "This is taking longer than expected. Would you like me to continue or escalate?",
        "cost": "I've reached my resource limit for this conversation.",
        "error_rate": "I'm experiencing technical difficulties. Please try again later.",
    }
    return fallbacks.get(breaker_type, "I'm unable to continue. Escalating to support.")
```

### Strategy 2: Partial Results

```python
def handle_breaker_with_partial(state: AgentState) -> AgentResponse:
    """Return whatever was accomplished before the breaker tripped."""
    
    if state.actions_taken:
        completed = [a for a in state.actions_taken if a.get("completed")]
        
        return AgentResponse(
            content=f"I completed {len(completed)} actions before running into an issue:\n"
                    f"{format_completed_actions(completed)}\n"
                    f"A representative will help with the remaining items.",
            partial=True
        )
    else:
        return AgentResponse(
            content="I wasn't able to complete any actions. Escalating to support.",
            partial=True
        )
```

### Strategy 3: Checkpoint and Resume

```python
def handle_breaker_with_checkpoint(state: AgentState) -> AgentResponse:
    """Save state so a human or future agent can resume."""
    
    checkpoint = {
        "conversation_id": state.conversation_id,
        "actions_completed": state.actions_taken,
        "pending_intent": state.last_user_intent,
        "breaker_reason": state.breaker_reason,
    }
    
    save_checkpoint(checkpoint)
    
    return AgentResponse(
        content="I've saved my progress. A representative will continue from where I left off.",
        checkpoint_id=checkpoint["conversation_id"]
    )
```

---

## Testing Circuit Breakers

### Unit Tests

```python
def test_iteration_breaker():
    breaker = IterationBreaker(max_iterations=3)
    
    breaker.tick()  # 1
    breaker.tick()  # 2
    breaker.tick()  # 3
    
    with pytest.raises(CircuitBreakerTripped) as exc:
        breaker.tick()  # 4 - should trip
    
    assert exc.value.breaker == "iteration"


def test_cost_breaker():
    breaker = CostBreaker(max_cost=1.0)
    
    breaker.add_cost(0.3)
    breaker.add_cost(0.3)
    breaker.add_cost(0.3)
    
    with pytest.raises(CircuitBreakerTripped):
        breaker.add_cost(0.2)  # Would exceed $1.00
```

### Integration Tests

```python
async def test_agent_respects_iteration_limit():
    config = AgentConfig(max_turns=5)
    agent = GuardedAgent(config)
    
    # Create a query that would cause infinite loop
    response = await agent.process(
        "Keep checking the order status until it ships"
    )
    
    # Agent should have stopped, not looped forever
    assert agent.state.turn_count <= 5
    assert "unable" in response.content.lower() or "escalat" in response.content.lower()
```

---

## Your Task: Implement Circuit Breakers

### Step 1: Identify What Needs Breakers

| Resource/Process | Why It Needs a Breaker | Limit |
|:-----------------|:-----------------------|:------|
| Agent iterations | Prevent infinite loops | |
| Time | Prevent hung conversations | |
| API cost | Prevent cost explosion | |
| Tool calls | Prevent abuse | |
| Errors | Prevent retry storms | |

### Step 2: Implement Each Breaker

For each breaker:
- Define the threshold
- Implement the check
- Define the response when tripped

### Step 3: Test Under Failure Conditions

Create tests that:
- Verify breakers trip at correct thresholds
- Verify graceful degradation when tripped
- Verify state is preserved for recovery

---

## Checkpoint

### You Should Now Have

- [ ] Iteration limit breaker
- [ ] Time limit breaker
- [ ] Cost limit breaker (optional)
- [ ] Error rate breaker
- [ ] Graceful degradation handling

### You Should Be Able To Answer

- What happens when an iteration limit is reached?
- How do you prevent a retry storm?
- What's the difference between a guardrail and a circuit breaker?
- How do you handle partial progress when a breaker trips?

---

[← Back: Guardrails](03_guardrails.md) | [Next: Monitoring →](05_monitoring.md)
