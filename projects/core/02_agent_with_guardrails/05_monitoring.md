[← Back: Circuit Breakers](04_circuit_breakers.md) | [Next: Human Escalation →](06_human_escalation.md)

# Module 5: Monitoring

Build observability into your agent from the start.

---

## Why Monitoring Matters

An agent without monitoring is a black box. When things go wrong — and they will — you need to answer:

- What did the agent do?
- Why did it do that?
- When did the problem start?
- How many users were affected?
- What triggered the issue?

Monitoring transforms "something is broken" into "X happened because Y at time Z."

---

## The Three Pillars of Observability

### 1. Logs

**What happened** — A record of events.

```python
# Structured logging for agents
logger.info("agent_action", extra={
    "conversation_id": state.conversation_id,
    "turn": state.turn_count,
    "action_type": "tool_call",
    "tool_name": action.tool_name,
    "parameters": sanitize(action.parameters),  # Remove PII
    "duration_ms": duration,
    "success": True
})
```

### 2. Metrics

**How much** — Quantitative measurements over time.

```python
# Counter: How many times something happened
tool_calls_total.labels(tool_name="process_refund").inc()

# Gauge: Current value of something
active_conversations.set(len(current_conversations))

# Histogram: Distribution of values
response_latency.observe(duration_seconds)
```

### 3. Traces

**The journey** — How requests flow through the system.

```python
with tracer.start_span("agent_conversation") as span:
    span.set_attribute("conversation_id", conv_id)
    
    with tracer.start_span("input_guardrails"):
        result = guardrails.check_input(user_input)
    
    with tracer.start_span("agent_reasoning"):
        action = agent.get_next_action()
    
    with tracer.start_span("tool_execution"):
        result = execute_tool(action)
```

---

## What to Monitor

### Agent Behavior Metrics

| Metric | Type | Why It Matters |
|:-------|:-----|:---------------|
| `agent_turns_total` | Counter | Detect loops, measure complexity |
| `agent_turns_per_conversation` | Histogram | Distribution of conversation lengths |
| `agent_tool_calls_total` | Counter | Tool usage patterns |
| `agent_tool_call_duration_seconds` | Histogram | Performance of tools |
| `agent_token_usage_total` | Counter | Cost tracking |
| `agent_errors_total` | Counter | Error rates |

### Safety Metrics

| Metric | Type | Why It Matters |
|:-------|:-----|:---------------|
| `guardrail_triggers_total` | Counter | How often guardrails fire |
| `circuit_breaker_trips_total` | Counter | How often breakers trip |
| `escalations_total` | Counter | How often humans are needed |
| `blocked_actions_total` | Counter | What's being prevented |

### Business Metrics

| Metric | Type | Why It Matters |
|:-------|:-----|:---------------|
| `refunds_processed_total` | Counter | Business impact |
| `refund_amount_dollars` | Histogram | Financial distribution |
| `conversations_resolved` | Counter | Success rate |
| `conversations_escalated` | Counter | What agent can't handle |

---

## Implementation

### Structured Logging

```python
import structlog

logger = structlog.get_logger()

class AgentLogger:
    """Structured logging for agent events."""
    
    def __init__(self, conversation_id: str):
        self.logger = logger.bind(conversation_id=conversation_id)
    
    def log_turn_start(self, turn: int, user_input: str):
        self.logger.info(
            "turn_start",
            turn=turn,
            input_length=len(user_input),
            input_preview=user_input[:100]  # Don't log full input
        )
    
    def log_action(self, action: AgentAction, duration_ms: float, success: bool):
        self.logger.info(
            "agent_action",
            tool_name=action.tool_name,
            parameters=self._sanitize_params(action.parameters),
            duration_ms=duration_ms,
            success=success
        )
    
    def log_guardrail_trigger(self, guardrail: str, reason: str, action_taken: str):
        self.logger.warning(
            "guardrail_triggered",
            guardrail=guardrail,
            reason=reason,
            action_taken=action_taken
        )
    
    def log_circuit_breaker(self, breaker: str, details: dict):
        self.logger.error(
            "circuit_breaker_tripped",
            breaker=breaker,
            **details
        )
    
    def _sanitize_params(self, params: dict) -> dict:
        """Remove sensitive data from parameters."""
        sanitized = {}
        sensitive_keys = {'password', 'token', 'api_key', 'ssn', 'card_number'}
        
        for key, value in params.items():
            if key.lower() in sensitive_keys:
                sanitized[key] = "[REDACTED]"
            else:
                sanitized[key] = value
        
        return sanitized
```

### Metrics Collection

```python
from prometheus_client import Counter, Histogram, Gauge

# Define metrics
TURN_COUNTER = Counter(
    'agent_turns_total',
    'Total agent turns',
    ['conversation_id', 'outcome']
)

TOOL_CALL_COUNTER = Counter(
    'agent_tool_calls_total',
    'Total tool calls',
    ['tool_name', 'success']
)

TOOL_LATENCY = Histogram(
    'agent_tool_call_duration_seconds',
    'Tool call latency',
    ['tool_name'],
    buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
)

GUARDRAIL_TRIGGERS = Counter(
    'agent_guardrail_triggers_total',
    'Guardrail trigger count',
    ['guardrail_type', 'action_taken']
)

ACTIVE_CONVERSATIONS = Gauge(
    'agent_active_conversations',
    'Currently active conversations'
)


class AgentMetrics:
    """Metrics collection for agent monitoring."""
    
    def record_turn(self, conversation_id: str, outcome: str):
        TURN_COUNTER.labels(
            conversation_id=conversation_id,
            outcome=outcome
        ).inc()
    
    def record_tool_call(self, tool_name: str, success: bool, duration: float):
        TOOL_CALL_COUNTER.labels(tool_name=tool_name, success=str(success)).inc()
        TOOL_LATENCY.labels(tool_name=tool_name).observe(duration)
    
    def record_guardrail_trigger(self, guardrail_type: str, action: str):
        GUARDRAIL_TRIGGERS.labels(
            guardrail_type=guardrail_type,
            action_taken=action
        ).inc()
```

### Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

tracer = trace.get_tracer("agent")

class AgentTracer:
    """Distributed tracing for agent operations."""
    
    def trace_conversation(self, conversation_id: str):
        """Create a span for the entire conversation."""
        return tracer.start_as_current_span(
            "agent_conversation",
            attributes={"conversation_id": conversation_id}
        )
    
    def trace_turn(self, turn: int):
        """Create a span for a single turn."""
        return tracer.start_as_current_span(
            "agent_turn",
            attributes={"turn": turn}
        )
    
    def trace_tool_call(self, tool_name: str, parameters: dict):
        """Create a span for a tool call."""
        span = tracer.start_span(
            f"tool_call_{tool_name}",
            attributes={
                "tool.name": tool_name,
                "tool.parameters": str(parameters)
            }
        )
        return span
```

---

## Alerting

Define alerts for critical conditions:

### Alert Rules

```yaml
# alerts.yaml
alerts:
  - name: agent_high_error_rate
    condition: |
      rate(agent_errors_total[5m]) > 0.1
    severity: warning
    summary: "Agent error rate above 10%"
    
  - name: agent_circuit_breaker_trips
    condition: |
      increase(circuit_breaker_trips_total[1h]) > 5
    severity: critical
    summary: "Multiple circuit breaker trips in the last hour"
    
  - name: agent_guardrail_spike
    condition: |
      rate(guardrail_triggers_total[5m]) > rate(guardrail_triggers_total[1h])* 3
    severity: warning
    summary: "Unusual spike in guardrail triggers"
    
  - name: agent_high_latency
    condition: |
      histogram_quantile(0.95, agent_tool_call_duration_seconds) > 5
    severity: warning
    summary: "P95 latency exceeds 5 seconds"
    
  - name: agent_cost_anomaly
    condition: |
      rate(agent_token_usage_total[1h]) > avg_over_time(agent_token_usage_total[7d]) * 2
    severity: warning
    summary: "Token usage significantly above normal"
```

### Alert Implementation

```python
class AlertManager:
    """Simple alerting for agent anomalies."""
    
    def __init__(self, thresholds: dict):
        self.thresholds = thresholds
        self.alert_handlers = []
    
    def check_error_rate(self, errors: int, total: int):
        if total > 0:
            rate = errors / total
            if rate > self.thresholds.get('error_rate', 0.1):
                self._fire_alert(
                    name="high_error_rate",
                    severity="warning",
                    details={"rate": rate, "errors": errors, "total": total}
                )
    
    def check_guardrail_triggers(self, triggers: list[dict]):
        recent = [t for t in triggers if time.time() - t['timestamp'] < 300]
        if len(recent) > self.thresholds.get('guardrail_spike', 10):
            self._fire_alert(
                name="guardrail_spike",
                severity="warning",
                details={"count": len(recent), "triggers": recent}
            )
    
    def _fire_alert(self, name: str, severity: str, details: dict):
        alert = {
            "name": name,
            "severity": severity,
            "timestamp": time.time(),
            "details": details
        }
        
        for handler in self.alert_handlers:
            handler(alert)
```

---

## Dashboard Design

### Key Visualizations

**1. Conversation Overview**
- Active conversations (gauge)
- Conversations per hour (time series)
- Average turns per conversation (time series)

**2. Tool Usage**
- Tool calls by type (pie chart)
- Tool latency (histogram)
- Tool success rate (time series)

**3. Safety**
- Guardrail triggers by type (stacked bar)
- Circuit breaker trips (time series)
- Escalations (time series)

**4. Business**
- Refunds processed (counter)
- Refund amounts (histogram)
- Resolution rate (percentage)

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT MONITORING DASHBOARD                   │
├─────────────────────┬─────────────────────┬─────────────────────┤
│ Active Conversations│ Conversations/Hour  │ Avg Turns/Conv      │
│        [42]         │    [line chart]     │    [line chart]     │
├─────────────────────┴─────────────────────┴─────────────────────┤
│                      TOOL USAGE                                 │
├─────────────────────┬─────────────────────┬─────────────────────┤
│ Calls by Tool       │ Tool Latency P95    │ Success Rate        │
│   [pie chart]       │   [line chart]      │   [line chart]      │
├─────────────────────┴─────────────────────┴─────────────────────┤
│                      SAFETY METRICS                             │
├─────────────────────┬─────────────────────┬─────────────────────┤
│ Guardrail Triggers  │ Circuit Breakers    │ Escalations         │
│  [stacked bar]      │   [time series]     │   [time series]     │
├─────────────────────┴─────────────────────┴─────────────────────┤
│                      RECENT ALERTS                              │
│ [table of recent alerts with severity, time, details]           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Your Task: Implement Monitoring

### Step 1: Define Your Metrics

| Category | Metric | Type | Labels |
|:---------|:-------|:-----|:-------|
| Behavior | | | |
| Behavior | | | |
| Safety | | | |
| Safety | | | |
| Business | | | |

### Step 2: Implement Logging

- [ ] Structured logging for all agent events
- [ ] Sanitization of sensitive data
- [ ] Consistent log levels (info, warning, error)

### Step 3: Define Alerts

| Alert | Condition | Severity | Response |
|:------|:----------|:---------|:---------|
| | | | |
| | | | |
| | | | |

### Step 4: Design Dashboard

Sketch your dashboard layout showing key metrics for:
- Operations (is it working?)
- Safety (is it behaving?)
- Business (is it valuable?)

---

## Checkpoint

### You Should Now Have

- [ ] Metrics defined for agent behavior
- [ ] Metrics defined for safety
- [ ] Structured logging implemented
- [ ] Alert rules defined
- [ ] Dashboard design sketched

### You Should Be Able To Answer

- How would you know if the agent started misbehaving?
- What metric would show a cost explosion?
- How quickly would you detect a guardrail spike?
- What would you look at first during an incident?

---

[← Back: Circuit Breakers](04_circuit_breakers.md) | [Next: Human Escalation →](06_human_escalation.md)
