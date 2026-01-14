[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../COMPETENCIES.md) | [Projects](../projects/00_overview.md) | [Templates](../templates/README.md)

# Patterns

Reusable approaches for building reliable AI systems.

---

## What Are Patterns?

Patterns are proven solutions to recurring problems. They're not code to copy—they're mental models to apply. Each pattern captures hard-won insight about how to build AI systems that work in the real world.

**Patterns help you:**
- Recognize situations where established solutions exist
- Communicate design decisions with shared vocabulary
- Avoid reinventing solutions to solved problems
- Learn from collective experience

---

## Pattern Index

### Design Patterns

How to structure AI systems for reliability.

| Pattern | One-Line Summary | When to Use |
|:--------|:-----------------|:------------|
| [Evaluation-First](evaluation_first.md) | Define success before building | Starting any AI feature |
| [Defense in Depth](defense_in_depth.md) | Multiple independent safety layers | Any user-facing AI system |
| [Human-in-the-Loop](human_in_the_loop.md) | Strategic human oversight points | High-stakes decisions |
| [Graceful Degradation](graceful_degradation.md) | Fail partially, not completely | Production AI systems |

### Operational Patterns

How to run AI systems reliably.

| Pattern | One-Line Summary | When to Use |
|:--------|:-----------------|:------------|
| [Circuit Breaker](circuit_breaker.md) | Automatic failure containment | Agents, pipelines, any loop |
| [Blameless Post-Mortem](blameless_postmortem.md) | Learn from failures without blame | After any incident |
| [Confidence-Weighted Decisions](confidence_weighted.md) | Explicit uncertainty in estimates | Planning, prioritization |

### Review Patterns

How to evaluate AI outputs critically.

| Pattern | One-Line Summary | When to Use |
|:--------|:-----------------|:------------|
| [Structured Skepticism](structured_skepticism.md) | Systematic doubt for AI outputs | Reviewing any AI-generated content |

---

## Pattern Format

Each pattern follows a consistent structure:

```
## [Pattern Name]

### The Problem
What recurring challenge does this address?

### The Solution
Core insight in 2-3 sentences.

### How It Works
Step-by-step application.

### When to Use
Situations where this pattern applies.

### When NOT to Use
Situations where this pattern is wrong.

### Examples
Concrete illustrations.

### Anti-Patterns
Common mistakes when applying this.

### Related Patterns
What else to consider.
```

---

## How to Use Patterns

### 1. Recognize the Situation

Patterns solve specific problems. Before applying a pattern, confirm you're facing the problem it addresses.

**Wrong:** "I'll use Defense in Depth because it's a best practice."  
**Right:** "I have untrusted inputs and high-stakes outputs—Defense in Depth addresses this."

### 2. Adapt, Don't Copy

Patterns are principles, not prescriptions. Your context matters. A startup prototype and a financial services production system will implement the same pattern differently.

### 3. Combine Thoughtfully

Patterns work together. A production AI agent might use:
- **Evaluation-First** to define success criteria
- **Defense in Depth** for safety
- **Circuit Breaker** for failure containment
- **Human-in-the-Loop** for high-stakes decisions
- **Graceful Degradation** for partial failures

### 4. Know the Costs

Every pattern has trade-offs. Defense in Depth adds latency. Human-in-the-Loop adds operational cost. Circuit Breakers can cause false positives. Understand what you're trading.

---

## Patterns vs. Templates

| Patterns | Templates |
|:---------|:----------|
| Mental models | Fill-in documents |
| "How to think about X" | "Document X this way" |
| Adapt to context | Copy and customize |
| Principles | Artifacts |

Use patterns to guide design decisions. Use templates to document those decisions.

---

## Contributing Patterns

Good patterns come from real experience. If you've discovered an approach that works:

1. **Validate it** — Has it worked in multiple contexts?
2. **Name it** — Give it a memorable, descriptive name
3. **Structure it** — Follow the pattern format
4. **Document trade-offs** — What does it cost?
5. **Include examples** — Show it in action

---

## Pattern Origins

These patterns are extracted from the [Core Projects](../projects/00_overview.md):

| Pattern | Source Project |
|:--------|:---------------|
| Evaluation-First | RAG Evaluation Pipeline |
| Defense in Depth | Agent with Guardrails |
| Human-in-the-Loop | Agent with Guardrails |
| Graceful Degradation | Agent with Guardrails |
| Circuit Breaker | Agent with Guardrails |
| Blameless Post-Mortem | Incident Response |
| Confidence-Weighted | Cost-Benefit Analysis |
| Structured Skepticism | AI Code Review |

---

*Patterns support the [five competencies](../COMPETENCIES.md). Each pattern maps to one or more competency areas.*
