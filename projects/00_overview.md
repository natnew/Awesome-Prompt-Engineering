[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../COMPETENCIES.md)

# Projects Overview

This document explains how flagship projects work, what you'll build, and what "done" looks like.

---

## What Flagship Projects Are

Flagship projects are **structured learning experiences** that build real competencies through building real things.

They are not:
- Tutorials you follow step-by-step
- Code you copy-paste
- Demos that impress but don't teach
- Exercises with single correct answers

They are:
- Scenarios with realistic constraints
- Decisions you have to make and defend
- Artifacts you produce that demonstrate thinking
- Skills that transfer across tools and domains

**The learning is in the decisions, not the code.**

---

## The Two Tiers

### Core Projects

Broadly applicable projects that teach AI systems literacy. Relevant to anyone working with AI in software, products, or operations.

| Project | Primary Competencies | What You Build |
|:--------|:--------------------|:---------------|
| [RAG Evaluation Pipeline](core/01_rag_evaluation_pipeline/) | Systems Design, Evaluation | Evaluation infrastructure for RAG systems |
| [Agent with Guardrails](core/02_agent_with_guardrails/) | Systems Design, Safety | Autonomous system with safety constraints |
| [AI Code Review](core/03_ai_code_review/) | Output Review, Evaluation | Critical review skills and checklists |
| [Cost-Benefit Analysis](core/04_cost_benefit_analysis/) | Evaluation, Governance | Decision framework for AI features |
| [Incident Response](core/05_incident_response/) | Safety, Governance | Response procedures and post-mortems |

**Start here.** These projects establish the foundations everything else builds on.

### AI for Science Projects

Advanced projects that apply the core competencies to high-stakes scientific and medical domains. These demonstrate what responsible AI looks like when failure is not an option.

| Project | Primary Competencies | What You Build |
|:--------|:--------------------|:---------------|
| [Health Reasoning Agent](ai_for_science/01_health_reasoning_agent/) | Safety, Output Review, Governance | Multi-agent health guidance with guardrails |
| [Drug Discovery Pipeline](ai_for_science/02_drug_discovery_pipeline/) | Systems Design, Evaluation | Self-evolving multi-agent research system |
| [Scientific Event Engine](ai_for_science/03_scientific_event_engine/) | Systems Design, Governance | Event-driven discovery infrastructure |

**Progress here after completing at least 2-3 core projects.** The AI for Science projects assume familiarity with the patterns and thinking developed in the core tier.

---

## Project Structure

Every flagship project follows the same structure:

```
project_name/
├── README.md              # Overview: what you'll build and learn
├── 01_problem_framing.md  # The scenario, constraints, and requirements
├── 02_[domain_specific].md # Project-specific learning modules
├── ...
├── synthesis.md           # Bringing it together
├── artifacts/             # Templates you complete
│   ├── [deliverable_templates]
│   └── ...
└── reference/             # Optional reference implementation
    └── [code if applicable]
```

### The Sections

**README.md**
- What competencies this project develops
- What you'll build
- What "done" looks like
- Prerequisites
- Time estimate

**Problem Framing**
- The realistic scenario you're working in
- Constraints that matter (time, cost, team, stakes)
- What success looks like
- What failure looks like

**Learning Modules**
- Concepts you need to understand
- Decisions you need to make
- Trade-offs you need to navigate
- Questions you need to answer

**Synthesis**
- Bringing the pieces together
- Final deliverables
- Self-assessment criteria

**Artifacts**
- Templates for deliverables (ADRs, runbooks, evaluation configs, etc.)
- You complete these — they become your portfolio

**Reference**
- Optional working code
- Demonstrates one valid approach (not the only approach)
- The code is not the point — the thinking is

---

## What "Done" Looks Like

A completed project produces **artifacts that demonstrate thinking**, not just working code.

### Portfolio Artifacts

Each project produces 1-3 artifacts that you can show to others:

| Artifact Type | What It Demonstrates |
|:--------------|:--------------------|
| **Architecture Decision Record (ADR)** | You can make and document trade-offs |
| **Evaluation Suite** | You can define and measure success |
| **Runbook** | You can plan for failure |
| **Cost Model** | You can quantify trade-offs |
| **Decision Memo** | You can communicate to stakeholders |
| **Post-Mortem** | You can learn from incidents |
| **Review Checklist** | You can verify AI outputs systematically |

### Quality Criteria

Your artifacts should:

1. **Show your reasoning** — Not just what you decided, but why
2. **Acknowledge trade-offs** — What you gave up, not just what you gained
3. **Be specific** — Concrete details, not generic statements
4. **Be honest** — Including uncertainty and limitations
5. **Be defensible** — Could you explain this to a skeptical stakeholder?

### Self-Assessment

Each project includes self-assessment criteria. Ask yourself:

- Did I make explicit decisions, or did I just follow instructions?
- Can I explain my trade-offs to someone who wasn't there?
- Did I consider failure modes before they happened?
- Would I trust a system built this way?
- Could I defend these choices in a review?

---

## How to Work Through a Project

### Recommended Approach

1. **Read the full project first** — Understand the whole before starting parts
2. **Make decisions before looking at references** — The learning is in deciding
3. **Document as you go** — Don't retrofit reasoning after the fact
4. **Embrace uncertainty** — There are no single correct answers
5. **Complete the artifacts** — They're the proof of learning

### What to Avoid

- **Copying reference implementations** — You learn nothing this way
- **Skipping the hard parts** — The hard parts are where learning happens
- **Treating it as a tutorial** — You're not following steps, you're making decisions
- **Rushing to code** — The thinking matters more than the implementation
- **Pretending certainty** — Acknowledge what you don't know

### Time Investment

| Project Type | Estimated Time | Depth |
|:-------------|:---------------|:------|
| Core Projects | 4-8 hours each | Thorough |
| AI for Science | 8-16 hours each | Deep |

These are estimates for meaningful engagement, not speed runs. You can go faster or slower. The goal is competency, not completion.

---

## Prerequisites

### For All Projects

- Basic Python proficiency
- Familiarity with LLM APIs (any provider)
- Understanding of basic prompting techniques
- Willingness to make decisions under uncertainty

### For Core Projects

The core projects assume you've read:
- [Basic Prompting](../Basic_Prompting.md)
- [Intermediate Prompting](../Intermediate_Prompting.md)
- [Deep Learning Guide](../Deep_Learning_Guide.md) (concepts, not implementation)

### For AI for Science Projects

The AI for Science projects assume you've completed at least 2-3 core projects and have familiarity with:
- Multi-agent architectures ([Agents Guide](../Agents.md))
- Evaluation frameworks
- Safety and guardrails patterns

---

## Tools and Dependencies

Projects are designed to be **tool-agnostic**. The concepts transfer across:
- Model providers (OpenAI, Anthropic, Google, open-source)
- Frameworks (LangChain, LlamaIndex, raw API calls)
- Evaluation tools (various options provided)

Reference implementations use common tools, but you can substitute your preferred stack. If you can justify your choice, it's valid.

### Recommended Setup

- Python 3.10+
- API access to at least one LLM provider
- A code editor
- Willingness to read documentation

---

## Getting Started

### Recommended Starting Point

**[RAG Evaluation Pipeline](core/01_rag_evaluation_pipeline/)** — This project:
- Is broadly applicable (everyone's building RAG)
- Teaches evaluation-first thinking (the scarcest skill)
- Produces clear portfolio artifacts
- Establishes patterns used in later projects

### Alternative Paths

If you're primarily interested in:
- **Safety and reliability** → Start with [Agent with Guardrails](core/02_agent_with_guardrails/)
- **Working with AI tools** → Start with [AI Code Review](core/03_ai_code_review/)
- **Stakeholder communication** → Start with [Cost-Benefit Analysis](core/04_cost_benefit_analysis/)

---

## The Outcome

When you've completed the flagship projects, you'll have:

1. **Demonstrated competencies** — Evidence you can design, evaluate, and govern AI systems
2. **Portfolio artifacts** — Concrete work products that show your thinking
3. **Transferable skills** — Capabilities that work across tools and domains
4. **Earned confidence** — You've made decisions and defended them

You'll be able to answer the question that matters:

> "How do we know this AI-driven thing is actually working, safe enough, and worth the cost?"

With evidence. Not intuition.

---

## Next Steps

- [RAG Evaluation Pipeline](core/01_rag_evaluation_pipeline/) — Recommended first project
- [Competencies Framework](../COMPETENCIES.md) — Understanding what you're building
- [Patterns Library](../patterns/) — Reusable design approaches
- [Templates](../templates/) — Ready-to-use frameworks

---

*Last updated: January 2026*