[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Safety Architecture](02_safety_architecture.md) | [Uncertainty Communication →](04_uncertainty_communication.md)

# Agent Design

Design a multi-agent system where specialised agents collaborate to provide safe, helpful health reasoning.

---

## Why Multi-Agent?

A single monolithic agent handling all health reasoning faces fundamental tensions:

| Tension | Problem |
|:--------|:--------|
| **Empathy vs. Accuracy** | Warm communication style may soften important warnings |
| **Breadth vs. Depth** | General knowledge vs. specialised reasoning |
| **Speed vs. Thoroughness** | Quick responses vs. careful evidence review |
| **Helpfulness vs. Safety** | Wanting to help vs. knowing limits |

Multi-agent architecture resolves these tensions by separating concerns:

```
Each agent optimises for one thing → Coordination produces balanced output
```

---

## Agent Roles

### The Five Agents

| Agent | Responsibility | Optimises For |
|:------|:---------------|:--------------|
| **Intake Agent** | Structured information gathering | Empathy, completeness |
| **Reasoning Agent** | Symptom analysis, hypothesis generation | Accuracy, uncertainty |
| **Literature Agent** | Evidence retrieval and synthesis | Source quality, relevance |
| **Synthesis Agent** | User-facing communication | Clarity, appropriate tone |
| **Safety Agent** | Continuous safety monitoring | Risk detection, escalation |

### Agent Interaction Model

```
                    ┌─────────────────────┐
                    │    User Message     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    INTAKE AGENT     │
                    │  "What's going on?" │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
    │ REASONING AGENT │ │ LITERATURE AGENT│ │  SAFETY AGENT   │
    │   "Analysis"    │ │   "Evidence"    │ │  "Risk check"   │
    └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────┐
                    │  SYNTHESIS AGENT    │
                    │ "Here's what I can  │
                    │      tell you..."   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   User Response     │
                    └─────────────────────┘
```

---

## Agent 1: Intake Agent

### Purpose
Gather structured information from the user while maintaining empathetic, conversational tone.

### Responsibilities
- Extract relevant symptoms, duration, context
- Ask clarifying questions when needed
- Detect emotional state and adjust tone
- Identify urgency signals for Safety Agent

### Design Principles

| Principle | Implementation |
|:----------|:---------------|
| **Empathy first** | Acknowledge distress before gathering information |
| **Structured extraction** | Map natural language to structured representation |
| **Minimal burden** | Ask only what's needed, don't interrogate |
| **Urgency awareness** | Detect signals that require immediate escalation |

### Example Interaction

```
User: "I've had this really bad headache for three days and I'm getting worried"

Intake Agent internal processing:
{
  "symptom": "headache",
  "severity": "bad (self-reported)",
  "duration": "3 days",
  "emotional_state": "worried",
  "urgency_signals": ["duration", "worry expressed"],
  "clarification_needed": ["location", "other symptoms", "what makes it worse"]
}

Intake Agent output to user:
"Three days is a long time to have a bad headache — I understand why you're 
worried. To help me give you useful information, can you tell me:
- Where exactly is the pain? (forehead, temples, back of head?)
- Have you noticed anything else — nausea, light sensitivity, neck stiffness?"
```

### Your Task: Intake Agent Design

1. **Structured extraction schema**
   - What fields do you extract?
   - How do you handle ambiguity?
   - What's required vs. optional?

2. **Conversation flow**
   - When do you ask follow-ups?
   - How many questions before responding?
   - How do you handle users who just want an answer?

3. **Emotional calibration**
   - How do you detect distress?
   - How does tone change based on emotional state?
   - How do you balance warmth with information gathering?

---

## Agent 2: Reasoning Agent

### Purpose
Analyse symptoms and context to generate hypotheses with appropriate uncertainty.

### Responsibilities
- Pattern matching against medical knowledge
- Hypothesis generation with confidence levels
- Uncertainty quantification
- Identification of information gaps

### Design Principles

| Principle | Implementation |
|:----------|:---------------|
| **Epistemic humility** | Always uncertain, never diagnostic |
| **Multiple hypotheses** | Consider alternatives, not just most likely |
| **Explicit uncertainty** | Confidence levels on all outputs |
| **Information gaps** | Identify what would change assessment |

### Reasoning Framework

```
Symptom Profile → Pattern Analysis → Hypothesis Generation → Uncertainty Quantification

Pattern Analysis:
  - What conditions are consistent with these symptoms?
  - What's the base rate for each?
  - What additional symptoms would differentiate?

Hypothesis Generation:
  - Generate candidate explanations
  - Rank by consistency with evidence
  - Identify distinguishing features

Uncertainty Quantification:
  - What's my confidence in each hypothesis?
  - What information would change my confidence?
  - What am I uncertain about?
```

### Example Reasoning

```
Input from Intake Agent:
{
  "symptom": "headache",
  "location": "temples, bilateral",
  "severity": "6/10",
  "duration": "3 days",
  "associated": ["light sensitivity"],
  "context": ["stress at work", "poor sleep"]
}

Reasoning Agent output:
{
  "hypotheses": [
    {
      "condition": "tension headache",
      "consistency": "high",
      "supporting": ["bilateral", "stress", "duration"],
      "concerning": ["light sensitivity unusual for tension type"],
      "confidence": 0.6
    },
    {
      "condition": "migraine",
      "consistency": "moderate",
      "supporting": ["light sensitivity", "duration"],
      "concerning": ["no nausea reported", "bilateral less typical"],
      "confidence": 0.3
    },
    {
      "condition": "other/uncertain",
      "confidence": 0.1
    }
  ],
  "urgency_assessment": "low-moderate",
  "escalation_recommendation": "suggest GP visit if persists",
  "information_gaps": ["medication use", "fever", "vision changes"]
}
```

### Your Task: Reasoning Agent Design

1. **Knowledge representation**
   - How do you represent medical knowledge?
   - How do you handle knowledge updates?
   - How do you ensure accuracy?

2. **Uncertainty quantification**
   - How do you calibrate confidence?
   - How do you communicate uncertainty to other agents?
   - How do you handle cases where you genuinely don't know?

3. **Hypothesis generation**
   - How many hypotheses do you generate?
   - How do you avoid anchoring on first hypothesis?
   - How do you handle rare conditions?

---

## Agent 3: Literature Agent

### Purpose
Retrieve and synthesise evidence from trusted medical sources.

### Responsibilities
- Query formulation from reasoning output
- Source selection and quality assessment
- Evidence synthesis
- Citation and provenance tracking

### Design Principles

| Principle | Implementation |
|:----------|:---------------|
| **Source quality** | Only trusted, authoritative sources |
| **Relevance** | Evidence directly applicable to query |
| **Recency** | Prefer current guidelines |
| **Provenance** | Every claim traceable to source |

### Source Hierarchy

| Tier | Source Type | Examples |
|:-----|:------------|:---------|
| 1 | Clinical guidelines | NICE, CDC, WHO |
| 2 | Systematic reviews | Cochrane, PubMed |
| 3 | Authoritative health sites | NHS, Mayo Clinic |
| 4 | Peer-reviewed literature | Filtered PubMed |
| ✗ | Excluded | Social media, forums, unvetted sites |

### Example Literature Retrieval

```
Input from Reasoning Agent:
{
  "query_intent": "tension headache vs migraine differentiation",
  "context": "patient with 3-day bilateral headache, light sensitivity"
}

Literature Agent output:
{
  "evidence": [
    {
      "source": "NICE Headache Guidelines 2021",
      "finding": "Tension-type headaches typically bilateral, pressing quality",
      "relevance": "high",
      "citation": "NICE CG150, Section 1.2"
    },
    {
      "source": "International Headache Society Criteria",
      "finding": "Migraine: photophobia + at least one of nausea, unilateral",
      "relevance": "high",
      "citation": "ICHD-3, Section 1.1"
    }
  ],
  "synthesis": "Light sensitivity suggests migraine features, but bilateral 
               presentation and absence of nausea more consistent with tension-type. 
               Mixed presentations common.",
  "confidence_in_sources": "high"
}
```

### Your Task: Literature Agent Design

1. **Source selection**
   - What sources do you include?
   - How do you assess quality?
   - How do you handle conflicting sources?

2. **Retrieval strategy**
   - How do you formulate queries?
   - How do you handle retrieval failures?
   - How do you ensure relevance?

3. **Synthesis approach**
   - How do you combine multiple sources?
   - How do you handle uncertainty in sources?
   - How do you maintain provenance?

---

## Agent 4: Synthesis Agent

### Purpose
Translate technical reasoning into clear, helpful, appropriately-toned user communication.

### Responsibilities
- Translate medical language to plain language
- Calibrate tone to user emotional state
- Structure information for clarity
- Ensure safety messages are prominent

### Design Principles

| Principle | Implementation |
|:----------|:---------------|
| **Clarity** | No jargon without explanation |
| **Honesty** | Uncertainty expressed clearly |
| **Actionability** | Clear next steps |
| **Warmth** | Supportive, not clinical |

### Communication Templates

**Information delivery:**
```
[Acknowledge] → [Explain] → [Context] → [Guidance] → [Invitation]

"That sounds uncomfortable. [Acknowledge]

Based on what you've described, this could be [Explain — plain language hypotheses].

[Context about the condition, what's normal, what to watch for]

[Guidance — what to do, when to seek care]

Is there anything specific you'd like me to explain further?" [Invitation]
```

**Uncertainty expression:**
```
"From what you've shared, I think [higher confidence item].
I'm less certain about [lower confidence item] — [reason for uncertainty].
[What would help clarify]"
```

**Escalation:**
```
"This sounds like something that would really benefit from a doctor's assessment.
[Reason this warrants professional evaluation]
[What the doctor can do that I can't]
[Supportive offer to help prepare for appointment]"
```

### Your Task: Synthesis Agent Design

1. **Language calibration**
   - How do you adjust reading level?
   - How do you explain necessary medical terms?
   - How do you handle users who want technical detail?

2. **Tone management**
   - How do you balance warmth with accuracy?
   - How do you handle distressed users?
   - How do you deliver concerning information?

3. **Structure decisions**
   - When do you use lists vs. prose?
   - How long should responses be?
   - What's the information hierarchy?

---

## Agent 5: Safety Agent

### Purpose
Continuously monitor all agent outputs for safety concerns and escalation triggers.

### Responsibilities
- Monitor all inter-agent communications
- Detect safety signals across the pipeline
- Trigger escalations when thresholds met
- Veto unsafe outputs

### Design Principles

| Principle | Implementation |
|:----------|:---------------|
| **Always watching** | Monitors all agent outputs, not just final |
| **Conservative** | Err on side of escalation |
| **Independent** | Cannot be overridden by other agents |
| **Transparent** | Logs all decisions |

### Safety Monitoring Points

```
User Input → [SAFETY CHECK] → Intake Agent
Intake Agent → [SAFETY CHECK] → Reasoning Agent
Reasoning Agent → [SAFETY CHECK] → Literature Agent
Literature Agent → [SAFETY CHECK] → Synthesis Agent
Synthesis Agent → [SAFETY CHECK] → User Output

Safety Agent can:
- PASS: Allow flow to continue
- FLAG: Add safety note to output
- ESCALATE: Insert escalation into output
- BLOCK: Replace output with safety response
```

### Safety Signal Categories

| Category | Signals | Action |
|:---------|:--------|:-------|
| **Emergency** | Chest pain, breathing difficulty, stroke signs | Immediate escalation |
| **Crisis** | Self-harm ideation, harm to others | Crisis resource redirect |
| **Medical urgency** | Symptoms suggesting serious condition | Strong recommendation for care |
| **Scope violation** | System attempting diagnosis/treatment | Block and redirect |
| **Miscalibration** | Overconfident or underconfident | Calibrate before output |

### Your Task: Safety Agent Design

1. **Monitoring architecture**
   - What does the safety agent see?
   - How does it integrate with other agents?
   - What's the latency impact?

2. **Decision thresholds**
   - What triggers each action level?
   - How do you calibrate sensitivity?
   - How do you handle ambiguous cases?

3. **Override mechanisms**
   - Can safety decisions be overridden?
   - Who has override authority?
   - How are overrides logged?

---

## Agent Coordination

### Orchestration Pattern

```python
class HealthReasoningOrchestrator:
    """
    Coordinates multi-agent health reasoning pipeline.
    """
    
    def __init__(self):
        self.intake = IntakeAgent()
        self.reasoning = ReasoningAgent()
        self.literature = LiteratureAgent()
        self.synthesis = SynthesisAgent()
        self.safety = SafetyAgent()
    
    async def process(self, user_input: str, context: ConversationContext) -> Response:
        # Safety check on input
        safety_check = await self.safety.check_input(user_input)
        if safety_check.action == "BLOCK":
            return safety_check.response
        
        # Intake processing
        intake_result = await self.intake.process(user_input, context)
        safety_check = await self.safety.check(intake_result)
        if safety_check.action == "ESCALATE":
            return self.synthesis.format_escalation(safety_check)
        
        # Parallel reasoning and literature retrieval
        reasoning_result, literature_result = await asyncio.gather(
            self.reasoning.analyse(intake_result),
            self.literature.retrieve(intake_result)
        )
        
        # Safety check on reasoning
        safety_check = await self.safety.check_reasoning(reasoning_result)
        
        # Synthesis with safety context
        synthesis_result = await self.synthesis.generate(
            intake_result,
            reasoning_result,
            literature_result,
            safety_check
        )
        
        # Final safety check
        final_check = await self.safety.check_output(synthesis_result)
        if final_check.action == "MODIFY":
            synthesis_result = final_check.modified_response
        
        return synthesis_result
```

### Communication Protocol

Agents communicate via structured messages:

```python
@dataclass
class AgentMessage:
    source: str  # Agent identifier
    content: dict  # Structured content
    confidence: float  # Confidence in content
    flags: list[str]  # Safety flags, warnings
    provenance: list[str]  # Sources for claims
```

### Your Task: Orchestration Design

1. **Flow control**
   - Sequential vs. parallel execution?
   - How do you handle agent failures?
   - What's the timeout strategy?

2. **State management**
   - How do you maintain conversation state?
   - How do agents share context?
   - How do you handle multi-turn conversations?

3. **Error handling**
   - What if an agent fails?
   - What if agents disagree?
   - How do you ensure graceful degradation?

---

## Deliverables

By the end of this section, you should have:

| Deliverable | Description |
|:------------|:------------|
| **Agent specifications** | Detailed spec for each agent |
| **Communication protocol** | How agents exchange information |
| **Orchestration design** | How agents coordinate |
| **Failure handling** | What happens when things go wrong |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Safety Architecture](02_safety_architecture.md) | [Project Overview](README.md) | [Uncertainty Communication →](04_uncertainty_communication.md) |
