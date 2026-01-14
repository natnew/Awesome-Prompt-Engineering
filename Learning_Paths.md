[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

# Learning Paths

This repository contains a lot of material. This guide helps you navigate it based on who you are and what you're trying to accomplish.

Each path is designed around the [five core competencies](Competencies.md) — but different roles emphasize different competencies. Choose the path that fits your situation, or build your own by combining elements from multiple paths.

---

## Quick Navigation

| Path | Who It's For | Time Investment | Primary Competencies |
|:-----|:-------------|:----------------|:---------------------|
| [Foundation Builder](#foundation-builder) | New to AI/LLMs, want solid fundamentals | 2-3 weeks | Systems Design, Evaluation |
| [Production Engineer](#production-engineer) | Building AI into products, need reliability | 3-4 weeks | Safety, Evaluation, Governance |
| [AI Systems Architect](#ai-systems-architect) | Designing AI infrastructure, leading teams | 4-6 weeks | All five competencies |
| [AI-Augmented Developer](#ai-augmented-developer) | Using AI tools daily, want to use them well | 1-2 weeks | Output Review, Evaluation |
| [Technical Leader](#technical-leader) | Making decisions about AI adoption | 2-3 weeks | Governance, Evaluation, Systems Design |
| [AI for Science Practitioner](#ai-for-science-practitioner) | Building AI for research/discovery | 6-8 weeks | All five, science-specific |

---

## Foundation Builder

### Who This Is For

You're relatively new to working with LLMs and AI systems. You may have experimented with ChatGPT or Copilot, but you haven't built production systems. You want to understand how these systems actually work — not just how to use them — so you can build on a solid foundation.

### What You'll Learn

- How LLMs work (enough to make good decisions, not enough to train one)
- Core prompting patterns that transfer across models
- How to think about AI as a system component
- How to evaluate whether your AI integration is working
- The vocabulary to discuss AI systems with colleagues

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●●○○○ |
| Evaluation | ●●○○○ |
| Safety | ●○○○○ |
| Output Review | ●●○○○ |
| Governance | ●○○○○ |

### The Path

**Week 1: Understanding the Landscape**

1. [Introduction](Introduction.md) — Timeline and context for how we got here
2. [Deep Learning Guide](Deep_Learning_Guide.md) — How LLMs actually work (concepts, not math)
3. [AI Glossary](AI_Glossary.md) — Reference as you go, don't memorize

**Week 2: Core Techniques**

4. [Basic Prompting](Basic_Prompting.md) — Foundational patterns
5. [Intermediate Prompting](Intermediate_Prompting.md) — Reasoning techniques
6. [Advanced Prompting](Advanced_Prompting.md) — Agentic patterns and composition

**Week 3: Putting It Together**

7. [Multi-Modal Prompting](Multi_Modal_Prompting.md) — Working with images and other modalities
8. [AI Tools](AI_Tools.md) — Survey the landscape of available tools
9. **Project:** [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/) — Your first hands-on build

### Success Criteria

You can:
- Explain how an LLM generates text (conceptually)
- Choose appropriate prompting techniques for different tasks
- Identify when a task is well-suited for LLMs vs. when it isn't
- Set up basic evaluation for an AI feature
- Have informed conversations about AI system design

### Next Steps

After completing this path, most people move to either [Production Engineer](#production-engineer) (if building products) or [AI-Augmented Developer](#ai-augmented-developer) (if using AI tools daily).

---

## Production Engineer

### Who This Is For

You're building AI features into production systems. You've moved past experimentation — now you need things to work reliably, fail gracefully, and be defensible when leadership asks questions. You care about uptime, costs, and user trust.

### What You'll Learn

- How to design AI systems that fail safely
- How to build evaluation pipelines that catch problems before users do
- How to implement guardrails that actually constrain behavior
- How to monitor AI systems in production
- How to respond when things go wrong
- How to communicate technical decisions to stakeholders

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●●●○○ |
| Evaluation | ●●●●○ |
| Safety | ●●●●○ |
| Output Review | ●●○○○ |
| Governance | ●●●○○ |

### The Path

**Week 1: Foundations (Review or Complete)**

1. [Advanced Prompting](Advanced_Prompting.md) — Ensure you understand agentic patterns
2. [Agents](Agents.md) — Agent architectures and orchestration
3. [Competencies](Competencies.md) — Understand the framework

**Week 2: Evaluation & Measurement**

4. **Project:** [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/) — Build evaluation infrastructure
5. **Pattern:** [Evaluation-First Design](patterns/evaluation_first_design.md)
6. **Template:** [Eval Suite Template](templates/eval_suite_template.md)

**Week 3: Safety & Reliability**

7. **Project:** [Agent with Guardrails](projects/core/02_agent_with_guardrails/) — Build systems that fail safely
8. **Pattern:** [Graceful Degradation](patterns/graceful_degradation.md)
9. **Pattern:** [Human-in-the-Loop](patterns/human_in_the_loop.md)

**Week 4: Operations & Governance**

10. **Project:** [Incident Response Simulation](projects/core/05_incident_response/) — Practice failure response
11. **Template:** [Incident Runbook](templates/incident_runbook.md)
12. **Template:** [Architecture Decision Record](templates/architecture_decision_record.md)

### Success Criteria

You can:
- Design an AI system with explicit failure modes and fallbacks
- Build an evaluation pipeline that runs automatically
- Implement guardrails that constrain agent behavior
- Write a runbook for operating an AI system
- Respond to an AI system incident with a structured process
- Document architectural decisions so they're defensible later

### Portfolio Artifacts

By completing this path, you'll have:
- A working evaluation suite with defined metrics
- An agent with implemented guardrails and monitoring
- An incident runbook and post-mortem document
- Architecture Decision Records for your design choices

---

## AI Systems Architect

### Who This Is For

You're responsible for AI infrastructure decisions at your organization. You're not just building features — you're designing systems, setting standards, and helping teams adopt AI responsibly. You need deep competency across all five areas, plus the ability to teach others.

### What You'll Learn

- How to design AI architectures that scale and evolve
- How to establish evaluation standards across teams
- How to build safety into organizational practice
- How to create governance frameworks that work
- How to communicate AI decisions to executives and regulators
- How to build AI for high-stakes domains (science, health, finance)

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●●●●● |
| Evaluation | ●●●●● |
| Safety | ●●●●○ |
| Output Review | ●●●○○ |
| Governance | ●●●●● |

### The Path

**Weeks 1-2: Core Projects**

Complete all five core projects in order:
1. [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/)
2. [Agent with Guardrails](projects/core/02_agent_with_guardrails/)
3. [AI Code Review Exercise](projects/core/03_ai_code_review/)
4. [Cost-Benefit Analysis](projects/core/04_cost_benefit_analysis/)
5. [Incident Response Simulation](projects/core/05_incident_response/)

**Weeks 3-4: Patterns & Templates**

Study and adapt all patterns and templates:
- [Patterns Library](patterns/) — Understand each pattern deeply
- [Templates Library](templates/) — Customize for your organization

**Weeks 5-6: AI for Science (High-Stakes Domains)**

Complete at least one AI for Science project:
- [Health Reasoning Agent](projects/ai_for_science/01_health_reasoning_agent/) — Safety-critical AI
- [Drug Discovery Pipeline](projects/ai_for_science/02_drug_discovery_pipeline/) — Multi-agent scientific reasoning
- [Scientific Event Engine](projects/ai_for_science/03_scientific_event_engine/) — Event-driven discovery

**Ongoing: Case Studies & Leadership**

- Review [Case Studies](case_studies/) — Learn from real scenarios
- Develop your own case studies from organizational experience
- Create learning paths for your teams

### Success Criteria

You can:
- Design AI architectures for complex, multi-system environments
- Establish evaluation standards and governance frameworks
- Make build/buy/partner decisions for AI capabilities
- Communicate AI strategy to executives and board members
- Navigate regulatory requirements (EU AI Act, HIPAA, etc.)
- Mentor others on responsible AI development
- Adapt practices for high-stakes domains

### Portfolio Artifacts

By completing this path, you'll have:
- All artifacts from core projects
- At least one AI for Science project artifact
- Organizational templates adapted for your context
- A governance framework document
- Case studies from your experience

---

## AI-Augmented Developer

### Who This Is For

You use AI coding assistants (Copilot, Claude, Cursor) daily. You're productive with them, but you've also noticed they sometimes generate plausible-looking code that's subtly wrong. You want to use these tools more effectively — getting their benefits while catching their failures.

### What You'll Learn

- How to review AI-generated code critically
- Common failure patterns in AI-generated code
- When to trust, verify, or reject AI suggestions
- How to maintain expertise while using AI assistance
- How to stay productive without sacrificing quality

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●○○○○ |
| Evaluation | ●●○○○ |
| Safety | ●○○○○ |
| Output Review | ●●●●● |
| Governance | ●○○○○ |

### The Path

**Week 1: Understanding the Tool**

1. [Advanced Prompting](Advanced_Prompting.md) — How to guide AI effectively
2. [Agents](Agents.md) — How AI coding tools work (conceptually)
3. [Competencies](Competencies.md) — Focus on "AI Output Review & Oversight"

**Week 2: Building Judgment**

4. **Project:** [AI Code Review Exercise](projects/core/03_ai_code_review/) — Practice critical review
5. **Template:** [AI Review Checklist](templates/ai_review_checklist.md) — Your personal checklist

### Success Criteria

You can:
- Identify common AI code generation failure patterns
- Review AI-generated code systematically
- Know when AI suggestions need verification vs. when they're safe
- Maintain deep understanding of your codebase despite AI assistance
- Explain your AI tool usage practices to others

### Portfolio Artifacts

By completing this path, you'll have:
- Annotated code reviews with reasoning
- A personal AI code review checklist
- Documentation of failure patterns you've encountered

---

## Technical Leader

### Who This Is For

You're a tech lead, engineering manager, or CTO making decisions about AI adoption. You need to understand AI systems well enough to evaluate proposals, allocate resources, and communicate with stakeholders — but you're not writing production AI code yourself.

### What You'll Learn

- How to evaluate AI feature proposals
- How to assess costs, risks, and benefits
- How to communicate AI decisions to non-technical stakeholders
- How to build governance frameworks
- How to identify when AI is the right solution vs. when it isn't

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●●●○○ |
| Evaluation | ●●●○○ |
| Safety | ●●○○○ |
| Output Review | ●○○○○ |
| Governance | ●●●●● |

### The Path

**Week 1: Understanding the Landscape**

1. [Introduction](Introduction.md) — Context and history
2. [Competencies](Competencies.md) — The framework your teams should develop
3. [AI Tools](AI_Tools.md) — Survey of available tools and frameworks

**Week 2: Evaluation & Decision-Making**

4. **Project:** [Cost-Benefit Analysis](projects/core/04_cost_benefit_analysis/) — Practice making defensible recommendations
5. **Template:** [Architecture Decision Record](templates/architecture_decision_record.md)
6. **Template:** [Cost Estimation Worksheet](templates/cost_estimation_worksheet.md)

**Week 3: Governance & Communication**

7. **Project:** [Incident Response Simulation](projects/core/05_incident_response/) — Understand failure modes
8. **Template:** [Stakeholder Brief](templates/stakeholder_brief.md)
9. [Ethical Charter](ethical_charter.md) — Values and principles

### Success Criteria

You can:
- Evaluate AI feature proposals with appropriate skepticism
- Make defensible build/buy/wait decisions
- Communicate AI decisions to executives and boards
- Establish governance frameworks for your organization
- Ask the right questions when reviewing AI systems

### Portfolio Artifacts

By completing this path, you'll have:
- A cost-benefit analysis document
- An incident response plan
- A governance framework outline
- Templates adapted for your organization

---

## AI for Science Practitioner

### Who This Is For

You're building AI systems for scientific discovery — drug discovery, medical reasoning, observatory coordination, or other research applications. The stakes are higher than typical software: wrong answers waste research effort, mislead scientists, or harm patients. You need all five competencies, plus domain-specific practices.

### What You'll Learn

- How to build AI systems where correctness matters more than speed
- How to design for uncertainty quantification and provenance
- How to implement safety in domains where failure causes real harm
- How to build multi-agent systems for complex scientific reasoning
- How to create audit trails for scientific reproducibility
- How to communicate uncertainty to researchers and clinicians

### Competency Focus

| Competency | Emphasis |
|:-----------|:---------|
| Systems Design | ●●●●● |
| Evaluation | ●●●●● |
| Safety | ●●●●● |
| Output Review | ●●●●○ |
| Governance | ●●●●● |

### The Path

**Weeks 1-3: Core Foundation**

Complete all five core projects — the fundamentals apply everywhere:
1. [RAG Evaluation Pipeline](projects/core/01_rag_evaluation_pipeline/)
2. [Agent with Guardrails](projects/core/02_agent_with_guardrails/)
3. [AI Code Review Exercise](projects/core/03_ai_code_review/)
4. [Cost-Benefit Analysis](projects/core/04_cost_benefit_analysis/)
5. [Incident Response Simulation](projects/core/05_incident_response/)

**Weeks 4-5: AI for Science Overview**

6. [AI for Science Overview](projects/ai_for_science/00_overview.md) — Why science is different
7. Study the patterns with a science lens:
   - Provenance and reproducibility
   - Uncertainty quantification
   - Multi-agent coordination
   - Human expert oversight

**Weeks 6-8: Domain Projects**

Complete the AI for Science projects relevant to your domain:

**For Health/Medical:**
- [Health Reasoning Agent](projects/ai_for_science/01_health_reasoning_agent/)

**For Drug Discovery/Chemistry:**
- [Drug Discovery Pipeline](projects/ai_for_science/02_drug_discovery_pipeline/)

**For Physical Sciences/Observatories:**
- [Scientific Event Engine](projects/ai_for_science/03_scientific_event_engine/)

### Success Criteria

You can:
- Design AI systems that quantify and communicate uncertainty
- Build provenance tracking into scientific AI pipelines
- Implement safety constraints appropriate to your domain
- Create multi-agent systems with appropriate coordination
- Audit and explain AI-assisted scientific conclusions
- Navigate domain-specific regulatory requirements

### Portfolio Artifacts

By completing this path, you'll have:
- All core project artifacts
- At least one complete AI for Science project
- Domain-specific templates and runbooks
- A governance framework for scientific AI

---

## Building Your Own Path

The predefined paths above are starting points, not constraints. You can build your own path by:

### 1. Assess Your Current State

For each competency, honestly evaluate where you are:

| Level | What It Looks Like |
|:------|:-------------------|
| **Novice** | Haven't thought about this systematically |
| **Developing** | Aware of the concepts, limited practice |
| **Competent** | Can apply in familiar situations |
| **Advanced** | Can adapt to novel situations, teach others |

### 2. Identify Your Gaps

Which competencies matter most for your role? Where are your biggest gaps between current state and where you need to be?

### 3. Select Materials

Choose materials that target your gaps:
- **Foundations** — For conceptual understanding
- **Projects** — For hands-on practice
- **Patterns** — For reusable approaches
- **Templates** — For practical tools

### 4. Set a Timeline

Be realistic. Deep competency takes time:
- A single project: 3-5 days of focused work
- A full learning path: 2-8 weeks depending on scope
- Mastery: Ongoing practice over months

### 5. Build Portfolio Artifacts

Each project produces artifacts. Collect them. They demonstrate competency better than certificates.

---

## How to Use This Guide

**If you're just starting:** Pick the path closest to your role and follow it sequentially.

**If you're experienced:** Skim the paths, identify gaps, and go directly to the materials that address them.

**If you're a manager:** Use this to identify learning paths for your team members based on their roles and growth areas.

**If you're building a training program:** Adapt these paths for your organization's context and tools.

---

## Tracking Progress

For each path, track:

| Milestone | Status | Date Completed | Notes |
|:----------|:-------|:---------------|:------|
| Foundation materials | ☐ | | |
| Project 1 | ☐ | | |
| Project 2 | ☐ | | |
| Patterns studied | ☐ | | |
| Templates adapted | ☐ | | |
| Portfolio complete | ☐ | | |

The goal isn't speed — it's genuine competency development.

---

## Next Steps

Ready to begin?

1. Choose your path from the options above
2. Review the [Competencies](Competencies.md) framework
3. Start with the first material in your path
4. Build the portfolio artifacts as you go

Questions about which path to choose? Start with [Foundation Builder](#foundation-builder) — the fundamentals transfer everywhere.

---

*This guide is a living document. As new projects and patterns are added, learning paths will be updated. Contributions welcome.*