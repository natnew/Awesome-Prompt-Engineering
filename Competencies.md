[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

# AI Systems Competencies

This document defines the core competencies this repository builds. Everything else — guides, projects, patterns, templates — exists to develop these capabilities.

---

## The Gap This Addresses

The challenge in 2026 is not accessing AI. It's integrating, trusting, measuring, and governing AI under pressure.

Most teams will embed AI the way they once embedded JavaScript snippets: opportunistically and without architecture. They will claim success based on anecdotes. They will discover failure modes in production. They will struggle to answer the question executives are quietly asking:

> "How do we know this AI-driven thing is actually working, safe enough, and worth the cost?"

This repository trains you to answer that question — with evidence, not intuition.

---

## The Five Competencies

| Competency | The Question It Answers |
|:-----------|:------------------------|
| [Systems Design for AI](#1-systems-design-for-ai) | How should this AI capability fit into my system? |
| [Evaluation & Measurement](#2-evaluation--measurement) | How do I know if this is working? |
| [Safety & Reliability Engineering](#3-safety--reliability-engineering) | What happens when this fails? |
| [AI Output Review & Oversight](#4-ai-output-review--oversight) | Should I trust this output? |
| [Governance & Defensibility](#5-governance--defensibility) | Can I defend this decision? |

Every flagship project in this repository reinforces at least two of these competencies. The competencies are tool-agnostic — they apply whether you're using Claude, GPT, Gemini, Llama, or whatever comes next.

---

## 1. Systems Design for AI

### What It Means

Understanding AI as a **probabilistic component** in a larger system — not a magic black box that solves problems, but an infrastructure dependency with specific characteristics:

- **Non-deterministic**: Same input can produce different outputs
- **Failure-prone**: Hallucinations, drift, context limits, API failures
- **Cost-variable**: Performance varies with spend, latency, and compute
- **Opaque**: Internal reasoning is not directly inspectable
- **Evolving**: Model updates change behavior without warning

Systems design for AI means treating these characteristics as engineering constraints, not surprises.

### Why It Matters

Teams that treat AI as a feature will:
- Build brittle systems that fail unpredictably
- Discover cost overruns after deployment
- Create technical debt that compounds
- Struggle to maintain or improve systems over time

Teams that treat AI as infrastructure will:
- Design for graceful degradation from the start
- Make cost-performance trade-offs explicit
- Build observability into the architecture
- Create systems that can evolve as models change

### What You'll Be Able To Do

- Identify where AI components create risk in a system architecture
- Design fallback paths for AI component failures
- Model the cost structure of AI-dependent systems
- Make architectural decisions that remain valid as models change
- Evaluate when AI is the right solution vs. when it's not

### Key Concepts

| Concept | What It Means |
|:--------|:--------------|
| **AI as dependency** | Treating AI like a database or API — something that can fail, slow down, or change |
| **Probabilistic contracts** | Defining expected behavior in terms of distributions, not guarantees |
| **Graceful degradation** | What the system does when AI is unavailable or unreliable |
| **Cost modeling** | Understanding the real cost of AI components (API, compute, latency, errors, maintenance) |
| **Architecture decision records** | Documenting trade-offs explicitly so decisions are defensible |

### Related Projects

- [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/) — Designing retrieval systems with explicit trade-offs
- [Agent with Guardrails](projects/core/02_agent_with_guardrails/) — Architecting autonomous systems that fail safely
- [Scientific Event Engine](projects/ai_for_science/03_scientific_event_engine/) — Event-driven AI for discovery

---

## 2. Evaluation & Measurement

### What It Means

Defining what "working" means **before** building, and measuring it **continuously** after deployment.

This is where most teams fail. They ship AI features based on:
- Demos that impressed stakeholders
- Anecdotes from early users
- Gut feelings about quality
- Metrics that measure activity, not value

Evaluation competency means:
- Defining success metrics before writing code
- Measuring non-deterministic systems appropriately
- Separating perceived value from measured value
- Making trade-offs explicit and quantified

### Why It Matters

Without rigorous evaluation:
- You can't tell if changes improve or degrade quality
- You can't justify costs to leadership
- You can't compare approaches systematically
- You can't catch drift before users do
- You ship based on hope, not evidence

With rigorous evaluation:
- You can ship with confidence
- You can make data-driven improvements
- You can communicate value to stakeholders
- You can catch problems before they become incidents
- You build credibility over time

### What You'll Be Able To Do

- Define evaluation metrics appropriate to the task
- Build golden datasets for regression testing
- Design evaluation pipelines that run automatically
- Measure retrieval quality separately from generation quality
- Detect drift and degradation over time
- Translate technical metrics to business value
- Use LLM-as-judge appropriately (and know its limits)

### Key Concepts

| Concept | What It Means |
|:--------|:--------------|
| **Evaluation-first design** | Defining what "good" looks like before building |
| **Golden datasets** | Curated examples with known-good answers for regression testing |
| **Offline vs. online evaluation** | Testing before deployment vs. measuring in production |
| **Proxy metrics** | Measurable signals that correlate with actual value |
| **LLM-as-judge** | Using language models to evaluate other model outputs |
| **Drift detection** | Identifying when system behavior changes over time |
| **Evals as documentation** | Test cases that define expected behavior |

### Related Projects

- [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/) — Building comprehensive evaluation infrastructure
- [Cost-Benefit Analysis](projects/core/04_cost_benefit_analysis/) — Measuring value, not just activity
- [Drug Discovery Pipeline](projects/ai_for_science/02_drug_discovery_pipeline/) — Evaluation where ground truth emerges slowly

---

## 3. Safety & Reliability Engineering

### What It Means

Designing systems where failures are **expected, contained, and recoverable** — not surprising, catastrophic, and mysterious.

Safety isn't a checklist or a policy document. It's a property that emerges from design decisions:
- Guardrails that constrain behavior
- Circuit breakers that stop runaway processes
- Monitoring that surfaces anomalies
- Fallbacks that maintain function
- Escalation paths that involve humans

### Why It Matters

AI systems fail in novel ways:
- Hallucinations that sound confident
- Prompt injections that bypass instructions
- Context limits that silently truncate information
- Model updates that change behavior
- Adversarial inputs that exploit weaknesses
- Cascading failures in multi-agent systems

Teams that treat safety as an afterthought will:
- Discover failure modes in production
- Lose user trust after incidents
- Face regulatory or legal consequences
- Spend more time firefighting than building

Teams that design for safety will:
- Catch failures before users do
- Maintain trust through transparency
- Meet compliance requirements by design
- Build systems that improve after incidents

### What You'll Be Able To Do

- Identify failure modes before deployment
- Implement guardrails that constrain model behavior
- Design circuit breakers for autonomous systems
- Build monitoring that surfaces anomalies
- Create escalation paths to human oversight
- Write incident runbooks before incidents happen
- Conduct post-mortems that prevent recurrence

### Key Concepts

| Concept | What It Means |
|:--------|:--------------|
| **Guardrails** | Constraints on inputs, outputs, or behavior that prevent harm |
| **Circuit breakers** | Mechanisms that stop processes when anomalies are detected |
| **Human-in-the-loop** | Designs that escalate to humans for high-stakes decisions |
| **Defense in depth** | Multiple layers of protection, not single points of failure |
| **Graceful degradation** | Maintaining partial function when components fail |
| **Blast radius** | How much damage a failure can cause before containment |
| **Runbooks** | Pre-written procedures for responding to known failure modes |

### Related Projects

- [Agent with Guardrails](projects/core/02_agent_with_guardrails/) — Building autonomous systems that fail safely
- [Incident Response Simulation](projects/core/05_incident_response/) — Practicing failure response
- [Health Reasoning Agent](projects/ai_for_science/01_health_reasoning_agent/) — Safety in high-stakes domains

---

## 4. AI Output Review & Oversight

### What It Means

Developing the **judgment** to know when to trust, verify, or reject AI outputs.

As AI assistants become ubiquitous — in IDEs, in documents, in workflows — the bottleneck shifts from generating outputs to evaluating them. Code generation is cheap. Knowing whether the code is correct is expensive.

This competency is about:
- Reviewing AI-generated content critically
- Identifying silent failure paths (things that look right but aren't)
- Knowing when automation should stop and humans should decide
- Maintaining quality while maintaining velocity

### Why It Matters

The failure mode isn't "AI is useless." It's "AI is useful enough to be dangerous."

Teams that over-trust AI will:
- Ship bugs that look like working code
- Propagate hallucinations as facts
- Lose the ability to verify what they're building
- Create technical debt faster than they realize

Teams that develop oversight competency will:
- Use AI to accelerate without sacrificing quality
- Catch errors before they reach production
- Maintain deep understanding of their systems
- Know when to slow down and verify

### What You'll Be Able To Do

- Review AI-generated code for correctness, security, and maintainability
- Identify common AI failure patterns (plausible but wrong)
- Create checklists for AI output review
- Design workflows that include verification steps
- Know when human judgment is required
- Maintain expertise while using AI assistance

### Key Concepts

| Concept | What It Means |
|:--------|:--------------|
| **Silent failures** | Outputs that look correct but aren't (the most dangerous kind) |
| **Plausibility vs. correctness** | AI optimizes for plausible; you need correct |
| **Verification workflows** | Processes that check AI outputs before they matter |
| **Expertise maintenance** | Staying sharp enough to catch AI errors |
| **Appropriate delegation** | Knowing what to delegate to AI and what to keep |
| **Critical review stance** | Assuming AI outputs need verification, not assuming they're right |

### Related Projects

- [AI Code Review Exercise](projects/core/03_ai_code_review/) — Practicing critical review of AI outputs
- [Health Reasoning Agent](projects/ai_for_science/01_health_reasoning_agent/) — Output review where mistakes cause harm
- [Drug Discovery Pipeline](projects/ai_for_science/02_drug_discovery_pipeline/) — Verifying AI reasoning in scientific contexts

---

## 5. Governance & Defensibility

### What It Means

Making decisions that are **explicit, documented, and defensible** to stakeholders who weren't in the room.

Governance isn't bureaucracy. It's the practice of:
- Making trade-offs explicit
- Documenting decisions and their rationale
- Creating audit trails for important actions
- Communicating with non-technical stakeholders
- Operating within regulatory and ethical constraints

### Why It Matters

You will be asked to explain:
- Why you chose this approach over alternatives
- What the risks are and how you're managing them
- What it costs and whether it's worth it
- What happens when it fails
- Whether it's compliant with regulations
- Whether it's ethical

Teams that can't answer these questions will:
- Lose stakeholder trust
- Face regulatory challenges
- Make decisions that don't survive scrutiny
- Struggle to get resources for AI initiatives

Teams that practice governance will:
- Build credibility with leadership
- Navigate regulatory requirements smoothly
- Make decisions that hold up over time
- Create organizational knowledge that compounds

### What You'll Be Able To Do

- Write architecture decision records that capture trade-offs
- Communicate technical decisions to non-technical audiences
- Create audit trails for AI-driven decisions
- Assess and document risks appropriately
- Operate within regulatory frameworks (GDPR, HIPAA, EU AI Act, etc.)
- Make ethical considerations operational, not theoretical

### Key Concepts

| Concept | What It Means |
|:--------|:--------------|
| **Architecture decision records** | Documents that capture what was decided, why, and what was considered |
| **Audit trails** | Records that allow decisions to be reviewed later |
| **Stakeholder communication** | Translating technical trade-offs into business terms |
| **Risk documentation** | Explicit recording of risks, mitigations, and residual risk |
| **Compliance by design** | Building regulatory requirements into architecture, not bolting them on |
| **Ethical operationalization** | Turning ethical principles into concrete design constraints |

### Related Projects

- [Cost-Benefit Analysis](projects/core/04_cost_benefit_analysis/) — Making defensible recommendations
- [Incident Response Simulation](projects/core/05_incident_response/) — Communicating during failures
- [Scientific Event Engine](projects/ai_for_science/03_scientific_event_engine/) — Provenance and trust in scientific discovery

---

## How Competencies Map to Projects

| Project | Systems Design | Evaluation | Safety | Output Review | Governance |
|:--------|:--------------:|:----------:|:------:|:-------------:|:----------:|
| **RAG Evaluation Pipeline** | ● | ●● | ○ | ● | ● |
| **Agent with Guardrails** | ●● | ● | ●● | ○ | ● |
| **AI Code Review** | ○ | ● | ○ | ●● | ○ |
| **Cost-Benefit Analysis** | ● | ●● | ○ | ○ | ●● |
| **Incident Response** | ● | ○ | ●● | ○ | ●● |
| **Health Reasoning Agent** | ● | ●● | ●● | ●● | ● |
| **Drug Discovery Pipeline** | ●● | ●● | ● | ●● | ● |
| **Scientific Event Engine** | ●● | ● | ● | ○ | ●● |

`●●` = Primary focus | `●` = Secondary focus | `○` = Touched on

---

## How to Use This Framework

### If You're Learning

1. Start with the [Core Projects](projects/core/) — they build foundational competencies
2. Use the competency framework to identify your gaps
3. Track which competencies each project develops
4. Build portfolio artifacts that demonstrate competency

### If You're Hiring

Use the competencies to:
- Define what "AI-ready" means for your team
- Evaluate candidates beyond "uses ChatGPT"
- Identify training needs for existing team members
- Structure interviews around concrete capabilities

### If You're Leading

Use the competencies to:
- Assess organizational readiness for AI adoption
- Identify where your teams need development
- Set expectations for AI initiatives
- Evaluate whether AI projects are being done responsibly

---

## The Outcome

Someone who completes the flagship projects should be able to say:

> "I can design, evaluate, and govern AI systems — from production software to scientific discovery — with appropriate safety constraints, measurable outcomes, and defensible decisions. I can do this regardless of which model or framework I'm using, because I understand the underlying principles."

That is enduring value. That is what this repository builds.

---

## Next Steps

- [Projects Overview](projects/00_overview.md) — How flagship projects work
- [Learning Paths](LEARNING_PATHS.md) — Routes through the material by role
- [Core Projects](projects/core/) — Start building competencies
- [AI for Science Projects](projects/ai_for_science/) — Advanced applications

---

*Last updated: January 2026*