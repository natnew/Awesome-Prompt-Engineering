[← Back: Problem Framing](01_problem_framing.md) | [Next: Guardrails →](03_guardrails.md)

# Module 2: Agent Architecture

Design the agent system with safety as a first-class concern.

---

## Agent Architecture Patterns

Before diving into implementation, understand the common patterns:

### Pattern 1: ReAct (Reasoning + Acting)

```
┌─────────────────────────────────────────────────────────────────┐
│                        ReAct LOOP                               │
│                                                                 │
│   User Query                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐                    │
│   │  Think  │───▶│   Act   │───▶│ Observe │──┐                 │
│   └─────────┘    └─────────┘    └─────────┘  │                 │
│       ▲                                       │                 │
│       └───────────────────────────────────────┘                 │
│                                                                 │
│   Until: Answer ready or max iterations                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**How it works:**
1. **Think**: Reason about what to do next
2. **Act**: Execute a tool/action
3. **Observe**: See the result
4. **Repeat** until done

**Safety implications:**
- Loop can run forever → need circuit breaker
- Each action has side effects → need action validation
- Reasoning can be manipulated → need input validation

### Pattern 2: Plan-then-Execute

```
┌─────────────────────────────────────────────────────────────────┐
│                   PLAN-THEN-EXECUTE                             │
│                                                                 │
│   User Query                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────┐                                                   │
│   │  Plan   │──▶ [Step 1, Step 2, Step 3, ...]                 │
│   └─────────┘                                                   │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐                    │
│   │Execute 1│───▶│Execute 2│───▶│Execute 3│───▶ ...            │
│   └─────────┘    └─────────┘    └─────────┘                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**How it works:**
1. **Plan**: Generate full plan upfront
2. **Execute**: Run each step sequentially

**Safety implications:**
- Plan can be reviewed before execution → easier to validate
- But: plan may be wrong, and you've committed to it
- Need ability to abort mid-execution

### Pattern 3: Hierarchical / Multi-Agent

```
┌─────────────────────────────────────────────────────────────────┐
│                      HIERARCHICAL                               │
│                                                                 │
│                   ┌─────────────┐                               │
│                   │ Supervisor  │                               │
│                   │   Agent     │                               │
│                   └──────┬──────┘                               │
│                          │                                      │
│            ┌─────────────┼─────────────┐                        │
│            │             │             │                        │
│            ▼             ▼             ▼                        │
│      ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│      │ Research │  │  Action  │  │  Review  │                  │
│      │  Agent   │  │  Agent   │  │  Agent   │                  │
│      └──────────┘  └──────────┘  └──────────┘                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**How it works:**
- Supervisor coordinates specialized agents
- Each agent has limited capabilities
- Separation of concerns

**Safety implications:**
- Can isolate dangerous capabilities to specific agents
- Supervisor can enforce policies
- But: more complex, more failure modes

---

## Architecture for This Project

For the customer service agent, we'll use a **guarded ReAct pattern**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    GUARDED ReAct                                │
│                                                                 │
│   User Input                                                    │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                           │
│   │ INPUT GUARDRAIL │◀── Prompt injection detection            │
│   └────────┬────────┘    Scope validation                      │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │   AGENT CORE    │◀── ReAct reasoning loop                  │
│   │  (Think→Act→Obs)│                                          │
│   └────────┬────────┘                                          │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │ ACTION GUARDRAIL│◀── Parameter validation                  │
│   └────────┬────────┘    Policy enforcement                    │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │  TOOL EXECUTOR  │◀── Actual tool calls                     │
│   └────────┬────────┘    with timeouts                         │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │OUTPUT GUARDRAIL │◀── PII filtering                         │
│   └────────┬────────┘    Response validation                   │
│            │                                                    │
│            ▼                                                    │
│       Response                                                  │
│                                                                 │
│   ═══════════════════════════════════════════════════════════  │
│   │         CIRCUIT BREAKERS (watching everything)          │  │
│   │         LOGGING (recording everything)                  │  │
│   │         MONITORING (alerting on anomalies)             │  │
│   ═══════════════════════════════════════════════════════════  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Design

### 1. Tool Definitions

Tools are the agent's capabilities. Define them carefully:

```python
# Good: Specific, constrained, documented
tools = [
    {
        "name": "lookup_order",
        "description": "Look up order details by order ID",
        "parameters": {
            "order_id": {
                "type": "string",
                "pattern": "^ORD-[0-9]{8}$",  # Constrained format
                "description": "Order ID in format ORD-XXXXXXXX"
            }
        },
        "returns": "Order details including status, items, and total",
        "side_effects": "None (read-only)",
        "rate_limit": "10 per minute"
    },
    {
        "name": "process_refund",
        "description": "Process a refund for an order",
        "parameters": {
            "order_id": {"type": "string", "pattern": "^ORD-[0-9]{8}$"},
            "amount": {"type": "number", "minimum": 0.01, "maximum": 50.00},
            "reason": {"type": "string", "maxLength": 200}
        },
        "returns": "Refund confirmation or error",
        "side_effects": "Credits customer account, updates order status",
        "rate_limit": "5 per minute",
        "requires_confirmation": True  # Human must confirm
    }
]
```

**Key principles:**
- **Constrain parameters**: Use patterns, min/max, enums
- **Document side effects**: Is this read-only or does it change state?
- **Specify rate limits**: Prevent runaway tool use
- **Mark sensitive tools**: Some tools need extra validation

### 2. State Management

Track what the agent has done:

```python
@dataclass
class AgentState:
    # Conversation
    conversation_id: str
    turn_count: int
    
    # Actions taken
    actions_taken: list[dict]
    refunds_processed: float  # Running total
    
    # Resource usage
    llm_calls: int
    tool_calls: int
    start_time: float
    
    # Safety
    guardrail_triggers: list[dict]
    escalation_requested: bool
```

**Why this matters:**
- Can enforce per-conversation limits
- Can detect patterns across turns
- Can audit what happened

### 3. Agent Configuration

Make limits explicit and configurable:

```python
@dataclass
class AgentConfig:
    # Behavior
    max_turns: int = 10
    max_tool_calls_per_turn: int = 3
    max_total_tool_calls: int = 20
    
    # Financial limits
    max_single_refund: float = 50.00
    max_total_refunds_per_conversation: float = 100.00
    
    # Time limits
    max_conversation_duration_seconds: float = 300.0
    tool_timeout_seconds: float = 10.0
    
    # Safety
    require_confirmation_for: list[str] = field(
        default_factory=lambda: ["process_refund"]
    )
    blocked_tools: list[str] = field(default_factory=list)
```

---

## Tool Design Principles

### Principle 1: Least Privilege

Give the agent only the tools it needs, nothing more.

```python
# Bad: Overly powerful tool
def execute_sql(query: str) -> str:
    """Execute arbitrary SQL query."""
    return database.execute(query)

# Good: Specific, constrained tool
def lookup_order(order_id: str) -> dict:
    """Look up a specific order by ID."""
    if not re.match(r'^ORD-[0-9]{8}$', order_id):
        raise ValueError("Invalid order ID format")
    return database.get_order(order_id)
```

### Principle 2: Explicit Side Effects

Clearly separate read and write operations.

```python
# Read operations - safe to retry, cache, etc.
read_tools = [
    "lookup_order",
    "check_inventory",
    "get_customer_info"
]

# Write operations - need extra care
write_tools = [
    "process_refund",      # Changes financial state
    "update_order_status", # Changes order state
    "send_notification"    # External side effect
]
```

### Principle 3: Idempotency Where Possible

Design tools so repeated calls don't cause problems.

```python
# Bad: Each call processes a new refund
def process_refund(order_id: str, amount: float):
    return payment_service.refund(order_id, amount)

# Good: Idempotent - same refund_id = same result
def process_refund(order_id: str, amount: float, refund_id: str):
    existing = get_refund(refund_id)
    if existing:
        return existing  # Already processed
    return payment_service.refund(order_id, amount, refund_id)
```

### Principle 4: Reversibility

Prefer reversible actions; make irreversible actions obvious.

| Action | Reversible? | Handling |
|:-------|:------------|:---------|
| Lookup order | N/A (read-only) | No special handling |
| Process refund | Partially (can be charged back) | Require confirmation |
| Send email | No | Extra confirmation + rate limit |
| Delete data | No | Should not be available to agent |

---

## Your Task: Design Your Architecture

### Step 1: Define Your Tools

List the tools your agent needs:

| Tool Name | Purpose | Read/Write | Parameters | Constraints |
|:----------|:--------|:-----------|:-----------|:------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

### Step 2: Define State Tracking

What state do you need to track?

| State | Why Track It? | Limits |
|:------|:--------------|:-------|
| | | |
| | | |
| | | |

### Step 3: Define Configuration

What should be configurable?

| Parameter | Default | Rationale |
|:----------|:--------|:----------|
| | | |
| | | |
| | | |

---

## Architecture Decision: ReAct vs Plan-Execute

For this project, choose your approach:

| Factor | ReAct | Plan-then-Execute |
|:-------|:------|:------------------|
| **Flexibility** | High — can adapt | Lower — committed to plan |
| **Predictability** | Lower | Higher — plan is visible |
| **Safety validation** | Per-action | Can validate whole plan |
| **Failure recovery** | Natural — just reason again | Need explicit replanning |
| **Complexity** | Moderate | Higher |

**Recommendation:** Start with ReAct. It's simpler and the guardrails pattern works naturally with it. Plan-then-execute is better for complex, multi-step workflows where you want to validate the whole plan upfront.

---

## Checkpoint

### You Should Now Have

- [ ] Chosen an agent architecture pattern
- [ ] Defined your tool set with constraints
- [ ] Designed state tracking structure
- [ ] Created configuration with explicit limits

### You Should Be Able To Answer

- Why did you choose this architecture pattern?
- What's the most dangerous tool in your set?
- How will you enforce the refund limit?
- What state do you need to track across turns?

---

[← Back: Problem Framing](01_problem_framing.md) | [Next: Guardrails →](03_guardrails.md)
