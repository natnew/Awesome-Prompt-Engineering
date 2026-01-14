[← Back: Cost Model](05_cost_model.md) | [Back to Project →](README.md)

# Module 6: Synthesis

Bring everything together and complete your portfolio artifacts.

---

## What You've Built

Over the previous modules, you've:

1. **Framed the problem** — Understood the scenario, constraints, and failure modes
2. **Defined success** — Created metrics before building
3. **Made architecture decisions** — Documented trade-offs explicitly
4. **Built evaluation infrastructure** — Created the ability to measure
5. **Modeled costs** — Understood the real economics

Now it's time to synthesize this into deliverables.

---

## Portfolio Artifacts Checklist

### Required Artifacts

Complete these to finish the project:

| Artifact | Location | Status |
|:---------|:---------|:-------|
| Architecture Decision Record | `artifacts/your_adr.md` | [ ] |
| Evaluation Configuration | `artifacts/your_eval_config.yaml` | [ ] |
| Cost Model | `artifacts/your_cost_model.md` | [ ] |
| Golden Dataset | `artifacts/your_golden_dataset.yaml` | [ ] |

### Artifact Quality Criteria

Your ADR should:
- [ ] Document at least 3 architectural decisions
- [ ] Include alternatives considered for each
- [ ] Explain rationale clearly
- [ ] Note what would change each decision
- [ ] Be understandable by someone not in the room

Your Evaluation Config should:
- [ ] Define retrieval metrics and targets
- [ ] Define generation metrics and targets
- [ ] Specify system metrics (latency, cost)
- [ ] Include drift detection thresholds
- [ ] Be runnable (or close to it)

Your Cost Model should:
- [ ] Calculate per-query cost
- [ ] Project monthly costs for 3 scenarios
- [ ] Include maintenance estimates
- [ ] Calculate or estimate ROI
- [ ] Be presentable to stakeholders

Your Golden Dataset should:
- [ ] Include 20+ examples minimum
- [ ] Cover all query categories
- [ ] Include ground truth for retrieval
- [ ] Include reference answers
- [ ] Be usable for automated evaluation

---

## Synthesis Exercise

### The Stakeholder Presentation

Imagine you're presenting this project to leadership. Complete this template:

---

**Project: Documentation Assistant RAG System**

**Problem:**
[What problem are we solving? 2-3 sentences]

**Solution:**
[What did we build? 2-3 sentences]

**Key Metrics:**

| Metric | Current Performance | Target |
|:-------|:-------------------|:-------|
| Retrieval Precision | | |
| Generation Quality | | |
| P95 Latency | | |
| Cost per Query | | |

**Architecture Highlights:**
- Chunking: [Your choice and why]
- Embedding: [Your choice and why]
- Generation: [Your choice and why]

**Costs:**

| Category | Amount |
|:---------|:-------|
| Build (one-time) | $ |
| Monthly (expected) | $ |
| Year 1 Total | $ |

**ROI:**
[Expected return or how you'd measure it]

**Key Risks:**
1. [Risk 1 and mitigation]
2. [Risk 2 and mitigation]
3. [Risk 3 and mitigation]

**Next Steps:**
1. [What happens next?]
2. [What decisions are needed?]
3. [What resources are required?]

---

### The Technical Handoff

Imagine you're handing this project to another engineer. What would they need to know?

**System Overview:**
[Architecture diagram + 2-3 sentences]

**How to Run Evaluation:**
```bash
# Commands to run evaluation
```

**How to Monitor:**
- [What to watch]
- [When to alert]
- [How to troubleshoot]

**Known Limitations:**
1. [Limitation 1]
2. [Limitation 2]
3. [Limitation 3]

**Future Improvements:**
1. [Improvement 1 and expected impact]
2. [Improvement 2 and expected impact]

---

## Self-Assessment

### Competency Check

For each competency, rate yourself honestly:

| Competency | Before Project | After Project | Evidence |
|:-----------|:--------------|:--------------|:---------|
| Systems Design | 1-5 | 1-5 | [What demonstrates this?] |
| Evaluation | 1-5 | 1-5 | [What demonstrates this?] |
| Safety | 1-5 | 1-5 | [What demonstrates this?] |
| Output Review | 1-5 | 1-5 | [What demonstrates this?] |
| Governance | 1-5 | 1-5 | [What demonstrates this?] |

### Reflection Questions

Answer honestly:

1. **What was the hardest part of this project?**

2. **What would you do differently if starting over?**

3. **What surprised you?**

4. **What do you still not understand well?**

5. **How would you explain "evaluation-first design" to a colleague?**

---

## What You've Learned

If you've completed this project thoroughly, you can now:

### Technical Skills
- [ ] Design a RAG system with explicit trade-offs
- [ ] Define and compute retrieval metrics
- [ ] Use LLM-as-judge for generation evaluation
- [ ] Build golden datasets for regression testing
- [ ] Detect drift in AI systems

### Professional Skills
- [ ] Document architectural decisions formally
- [ ] Model costs for AI systems
- [ ] Communicate technical trade-offs to stakeholders
- [ ] Make defensible recommendations

### Mental Models
- [ ] "Evaluation is not a phase, it's a design constraint"
- [ ] "Every decision is a trade-off"
- [ ] "Cost is part of the architecture"
- [ ] "You can't improve what you can't measure"

---

## Going Deeper

### If You Want More Practice

1. **Expand your golden dataset** to 50-100 examples
2. **Implement drift detection** that runs automatically
3. **A/B test** two retrieval strategies and compare
4. **Add semantic caching** and measure impact on cost/quality
5. **Build a dashboard** that visualizes metrics over time

### Related Projects

Now that you've completed this project, you're ready for:

- [Agent with Guardrails](../02_agent_with_guardrails/) — Apply evaluation thinking to agents
- [Cost-Benefit Analysis](../04_cost_benefit_analysis/) — Go deeper on decision-making
- [Health Reasoning Agent](../../ai_for_science/01_health_reasoning_agent/) — RAG for high-stakes domains

### Additional Resources

**Evaluation Frameworks:**
- [RAGAS](https://docs.ragas.io/) — RAG evaluation framework
- [TruLens](https://www.trulens.org/) — LLM application evaluation
- [Inspect AI](https://inspect.ai-safety-institute.org.uk/) — AI safety evaluations

**Cost Optimization:**
- [LangSmith](https://smith.langchain.com/) — Debugging and monitoring
- [Helicone](https://helicone.ai/) — Cost tracking and analytics

**RAG Patterns:**
- [LlamaIndex RAG Guide](https://docs.llamaindex.ai/en/stable/understanding/rag/)
- [Anthropic RAG Tutorial](https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation)

---

## Final Checklist

Before marking this project complete:

### Artifacts
- [ ] ADR completed with 3+ decisions
- [ ] Evaluation config is complete and runnable
- [ ] Cost model has all sections filled
- [ ] Golden dataset has 20+ examples

### Understanding
- [ ] Can explain trade-offs in your architecture
- [ ] Can calculate cost per query
- [ ] Can describe how you'd detect drift
- [ ] Can present to stakeholders

### Reflection
- [ ] Completed self-assessment honestly
- [ ] Identified areas for improvement
- [ ] Know what project to do next

---

## Completion

Congratulations on completing the RAG Evaluation Pipeline project.

You've practiced the most important skill in AI systems development: **defining and measuring success before declaring victory.**

This skill transfers to every AI project you'll work on. The specific tools will change — embeddings, models, frameworks — but the discipline of evaluation-first design remains.

---

**What's Next?**

Return to [Projects Overview](../00_overview.md) to choose your next project, or explore the [Patterns Library](../../patterns/) to see how evaluation-first thinking applies across domains.

---

*Project completed: [DATE]*

*Time invested: [HOURS]*

*Key learning: [ONE SENTENCE]*
