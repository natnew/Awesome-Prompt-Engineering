[← Back: Monitoring](05_monitoring.md) | [Next: Synthesis →](07_synthesis.md)

# Module 6: Human Escalation

Know when automation should stop and humans should decide.

---

## The Escalation Principle

**Automation should know its limits.**

An agent that never escalates is either:
1. Handling everything perfectly (unlikely), or
2. Making decisions it shouldn't make (dangerous)

Well-designed escalation is a feature, not a failure. It protects users, the business, and the agent's credibility.

---

## When to Escalate

### Clear Escalation Triggers

| Trigger | Why Escalate | Example |
|:--------|:-------------|:--------|
| **Policy limit reached** | Agent can't authorize | Refund > $50 |
| **Ambiguity** | Agent can't be confident | Unclear what user wants |
| **High stakes** | Consequences of error too high | Legal threat mentioned |
| **Explicit request** | User asks for human | "Let me talk to a person" |
| **Repeated failure** | Agent isn't helping | 3 failed attempts |
| **Safety concern** | Potential harm detected | User mentions self-harm |
| **Unusual pattern** | Something seems off | Suspicious activity |

### Escalation Decision Framework

```python
def should_escalate(context: ConversationContext) -> EscalationDecision:
    """Decide if this conversation should escalate to a human."""
    
    # Hard triggers - always escalate
    if context.user_requested_human:
        return EscalationDecision(
            escalate=True,
            reason="user_requested",
            urgency="normal"
        )
    
    if context.safety_concern_detected:
        return EscalationDecision(
            escalate=True,
            reason="safety_concern",
            urgency="high"
        )
    
    if context.policy_limit_reached:
        return EscalationDecision(
            escalate=True,
            reason="policy_limit",
            urgency="normal",
            details=context.limit_details
        )
    
    # Soft triggers - escalate based on thresholds
    if context.failed_attempts >= 3:
        return EscalationDecision(
            escalate=True,
            reason="repeated_failure",
            urgency="normal"
        )
    
    if context.confidence_score < 0.5:
        return EscalationDecision(
            escalate=True,
            reason="low_confidence",
            urgency="low"
        )
    
    return EscalationDecision(escalate=False)
```

---

## Escalation Paths

Not all escalations are equal. Define different paths:

### Path 1: Immediate Transfer

For urgent situations requiring immediate human attention.

```python
class ImmediateTransfer:
    """Transfer to human immediately."""
    
    triggers = ["safety_concern", "legal_threat", "fraud_suspected"]
    
    def execute(self, context: ConversationContext):
        # 1. Stop agent immediately
        context.agent.stop()
        
        # 2. Alert human operator
        self.notify_operator(
            urgency="high",
            context=context.summary(),
            reason=context.escalation_reason
        )
        
        # 3. Transfer conversation
        return TransferResponse(
            message="I'm connecting you with a support specialist right now.",
            hold_music=True,
            estimated_wait="< 2 minutes"
        )
```

### Path 2: Queue for Human Review

For non-urgent situations where human can follow up.

```python
class QueueForReview:
    """Queue for human follow-up."""
    
    triggers = ["policy_limit", "complex_request", "low_confidence"]
    
    def execute(self, context: ConversationContext):
        # 1. Create ticket
        ticket = create_support_ticket(
            priority="normal",
            summary=context.summary(),
            conversation_history=context.history,
            recommended_action=context.agent_recommendation
        )
        
        # 2. Notify user
        return QueueResponse(
            message=f"I've created a support ticket (#{ticket.id}). "
                    f"A team member will follow up within {ticket.sla}.",
            ticket_id=ticket.id
        )
```

### Path 3: Supervisor Approval

For actions that need human authorization before proceeding.

```python
class SupervisorApproval:
    """Request supervisor approval for action."""
    
    triggers = ["high_value_action", "policy_exception"]
    
    def execute(self, context: ConversationContext, proposed_action: AgentAction):
        # 1. Request approval
        approval_request = ApprovalRequest(
            conversation_id=context.id,
            proposed_action=proposed_action,
            reason=context.escalation_reason,
            agent_confidence=context.confidence_score
        )
        
        # 2. Wait for response (or timeout)
        approval = await self.wait_for_approval(
            approval_request,
            timeout=300  # 5 minutes
        )
        
        if approval.granted:
            return ApprovalResponse(
                proceed=True,
                message="A supervisor has approved this action."
            )
        else:
            return ApprovalResponse(
                proceed=False,
                message=f"I wasn't able to complete that action. {approval.alternative}"
            )
```

---

## Information Handoff

When escalating, provide humans with what they need:

### Handoff Content

```python
@dataclass
class EscalationHandoff:
    """Information passed to human during escalation."""
    
    # Identification
    conversation_id: str
    user_id: str
    timestamp: datetime
    
    # Context
    user_request_summary: str
    conversation_history: list[Message]
    
    # Agent's work
    actions_taken: list[AgentAction]
    actions_attempted: list[AgentAction]  # Including failures
    information_gathered: dict
    
    # Escalation reason
    escalation_trigger: str
    escalation_reason: str
    
    # Recommendations
    agent_recommendation: str
    confidence_score: float
    
    # Risk factors
    guardrails_triggered: list[str]
    unusual_patterns: list[str]
    
    def to_display(self) -> str:
        """Format for human agent display."""
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESCALATION: {self.escalation_trigger}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User Request: {self.user_request_summary}

Escalation Reason: {self.escalation_reason}

Actions Completed:
{self._format_actions(self.actions_taken)}

Information Gathered:
{self._format_info(self.information_gathered)}

Agent Recommendation: {self.agent_recommendation}
Confidence: {self.confidence_score:.0%}

⚠️  Guardrails Triggered: {', '.join(self.guardrails_triggered) or 'None'}

Conversation History: [Click to expand]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
```

### Good vs. Bad Handoffs

**Bad handoff:**
> "User wants a refund. Couldn't process. Escalating."

**Good handoff:**
> "User requested $75 refund for order #ORD-12345678 (delivered 2 days ago). 
> Reason: Item not as described.
> Agent verified order exists and is eligible for refund.
> Escalating because: Amount exceeds $50 auto-approval limit.
> Recommendation: Approve refund — order history shows first-time issue with loyal customer.
> Confidence: 85%"

---

## User Communication

How you communicate escalation matters:

### Do Say

```python
escalation_messages = {
    "policy_limit": 
        "This request needs supervisor approval. Let me connect you with someone who can help.",
    
    "user_requested":
        "Of course! I'm transferring you to a support specialist now.",
    
    "repeated_failure":
        "I want to make sure you get the right help. Let me bring in a specialist.",
    
    "complex_request":
        "This is a great question that needs some additional expertise. "
        "I'm connecting you with someone who can give you a complete answer.",
}
```

### Don't Say

- "I'm not smart enough to handle this" (undermines trust)
- "This is too hard for me" (sounds incompetent)
- "Error: escalation required" (robotic)
- "I give up" (abandons user)

---

## Escalation Metrics

Track escalation patterns to improve the agent:

| Metric | What It Tells You |
|:-------|:------------------|
| `escalation_rate` | % of conversations that escalate |
| `escalation_by_reason` | Why escalations happen |
| `time_to_escalation` | How long before escalating |
| `post_escalation_resolution` | What humans do after escalation |
| `escalation_satisfaction` | User satisfaction after escalation |

### Using Metrics to Improve

```python
def analyze_escalations(escalations: list[Escalation]) -> ImprovementPlan:
    """Analyze escalation patterns to improve agent."""
    
    by_reason = group_by(escalations, 'reason')
    
    improvements = []
    
    # High volume reasons are improvement opportunities
    for reason, cases in by_reason.items():
        if len(cases) / len(escalations) > 0.1:  # >10% of escalations
            if reason == "policy_limit":
                improvements.append(
                    "Consider raising auto-approval limits or adding supervisor approval flow"
                )
            elif reason == "low_confidence":
                # Analyze what queries cause low confidence
                low_conf_queries = [c.query for c in cases]
                improvements.append(
                    f"Agent needs better handling of: {cluster_queries(low_conf_queries)}"
                )
            elif reason == "repeated_failure":
                improvements.append(
                    "Analyze failure patterns — may need new tools or better prompts"
                )
    
    return ImprovementPlan(improvements=improvements)
```

---

## Your Task: Design Escalation System

### Step 1: Define Escalation Triggers

| Trigger | Urgency | Path | User Message |
|:--------|:--------|:-----|:-------------|
| | High/Normal/Low | Immediate/Queue/Approval | |
| | | | |
| | | | |
| | | | |

### Step 2: Design Handoff Content

What information should humans receive?

- [ ] Conversation summary
- [ ] Actions taken
- [ ] Agent recommendation
- [ ] Confidence score
- [ ] Risk factors
- [ ] Full history (expandable)

### Step 3: Define User Communication

Write user-facing messages for each escalation type.

### Step 4: Plan Metrics

What will you measure to improve escalation over time?

---

## Checkpoint

### You Should Now Have

- [ ] Escalation triggers defined
- [ ] Escalation paths designed
- [ ] Handoff content structured
- [ ] User messages written
- [ ] Metrics planned

### You Should Be Able To Answer

- What triggers an immediate transfer vs. queued escalation?
- What information does a human need during escalation?
- How would you reduce unnecessary escalations?
- How do you tell the user the agent is escalating?

---

[← Back: Monitoring](05_monitoring.md) | [Next: Synthesis →](07_synthesis.md)
