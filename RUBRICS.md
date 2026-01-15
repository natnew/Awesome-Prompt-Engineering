[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

# Competency Rubrics

This document defines **observable performance indicators** for each competency in the curriculum. These rubrics transform vague "I understand this" claims into concrete, demonstrable evidence.

---

## Why Rubrics Matter

When you say "I can design AI systems," what does that actually mean? Without clear criteria:

- **You** can't accurately assess your own growth
- **Interviewers** can't evaluate your claims
- **Teams** can't calibrate expectations

These rubrics make competency **visible and verifiable**.

---

## How to Use This Document

### For Self-Assessment

After completing a project, review the relevant competency rubrics. For each indicator:

| Rating | Meaning | Evidence Required |
|--------|---------|-------------------|
| ☐ Not Yet | Haven't attempted this | — |
| ☐ Developing | Can do with guidance/reference | Artifact exists but required significant external help |
| ☐ Met | Can do independently | Artifact demonstrates independent application |

**Be honest.** The goal isn't to check boxes—it's to identify where you need more practice.

### For Portfolio Building

Each indicator suggests **evidence types**. Your portfolio artifacts should demonstrate these indicators without you having to explain them. If someone reviews your ADR and can't tell whether you considered trade-offs, you haven't met that criterion.

### For Interviewers/Reviewers

These rubrics provide a shared vocabulary. When evaluating someone's work:

1. Identify which competencies the work claims to demonstrate
2. Look for evidence of specific indicators
3. Calibrate to the appropriate level (don't expect Advanced indicators from a first project)

---

## Competency Levels

Each competency has three progressive levels:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   DEVELOPING              PROFICIENT              ADVANCED          │
│                                                                     │
│   Can follow              Can adapt               Can create        │
│   established             patterns for            novel solutions   │
│   patterns                new contexts            for complex       │
│                                                   problems          │
│                                                                     │
│   "I can apply            "I can modify           "I can design     │
│    what I've learned"      approaches when         new approaches   │
│                            the situation           when existing    │
│                            requires it"            ones don't fit"  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Most professionals operate at Proficient level.** Advanced level typically requires years of experience and exposure to edge cases. Don't rush—depth at Proficient is more valuable than superficial breadth at Advanced.

---

## Competency 1: Systems Design for AI

> The ability to architect AI systems that are modular, maintainable, and resilient.

### Developing Level

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Decompose problems into agent responsibilities** | System diagram shows distinct components with clear boundaries |
| **Identify appropriate tool interfaces** | Each agent has defined inputs, outputs, and tool access |
| **Document system components** | ADR exists with component descriptions and relationships |
| **Select appropriate model for task** | Justification for model choice exists (not just "GPT-4 is best") |
| **Define system boundaries** | Clear statement of what the system does and doesn't do |

**Evidence artifacts:** System architecture diagram, component specifications, basic ADR

### Proficient Level

*Includes all Developing indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Justify architectural choices with trade-off analysis** | ADR includes alternatives considered and reasons for rejection |
| **Design for graceful degradation** | Documented fallback behavior when components fail |
| **Identify single points of failure** | Risk assessment with mitigation strategies |
| **Design for observability** | Logging, tracing, and monitoring hooks specified |
| **Optimize for appropriate constraints** | Explicit prioritization of latency vs. cost vs. accuracy |
| **Version control prompt/system changes** | Change management strategy documented |

**Evidence artifacts:** Trade-off analysis document, failure mode documentation, observability specification

### Advanced Level

*Includes all Proficient indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design multi-agent coordination for novel domains** | Original coordination patterns with justification |
| **Anticipate emergent system behaviors** | Documentation of potential emergent risks and mitigations |
| **Optimize across competing constraints simultaneously** | Pareto analysis or multi-objective optimization evidence |
| **Design for evolution** | Architecture accommodates future capability changes |
| **Create reusable architectural patterns** | Patterns abstracted for use in other contexts |

**Evidence artifacts:** Novel architecture documentation, emergent behavior analysis, reusable pattern definitions

---

## Competency 2: Evaluation & Measurement

> The ability to define, implement, and interpret meaningful assessments of AI system performance.

### Developing Level

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Define success metrics for an AI task** | Written metrics with clear definitions (not just "accuracy") |
| **Implement basic evaluation harness** | Runnable code that computes metrics on test data |
| **Distinguish accuracy from other quality dimensions** | Awareness that "correct" isn't the only measure |
| **Create representative test cases** | Test set covers expected input distribution |
| **Interpret evaluation results** | Written analysis identifying what results mean |

**Evidence artifacts:** Metrics definition document, evaluation script, test dataset, results analysis

### Proficient Level

*Includes all Developing indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design multi-dimensional evaluation suites** | Metrics cover accuracy, safety, cost, latency, user satisfaction |
| **Distinguish evaluation metrics from business metrics** | Clear mapping between technical and business outcomes |
| **Implement regression testing for prompt changes** | Automated tests that catch capability regressions |
| **Identify failure modes from evaluation data** | Systematic analysis categorizing error types |
| **Design evaluation for edge cases** | Explicit adversarial and boundary condition testing |
| **Calibrate confidence thresholds** | Data-driven threshold selection with justification |

**Evidence artifacts:** Multi-dimensional evaluation suite, regression test pipeline, failure mode taxonomy

### Advanced Level

*Includes all Proficient indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design evaluation frameworks for novel capabilities** | Original metrics for capabilities without established measures |
| **Quantify uncertainty in evaluation results** | Confidence intervals, statistical significance testing |
| **Design evaluation that scales with model improvements** | Metrics that remain meaningful as capabilities increase |
| **Identify evaluation gaming/Goodhart risks** | Analysis of how metrics could be gamed |
| **Create evaluation frameworks others can adopt** | Documented, generalizable evaluation methodology |

**Evidence artifacts:** Novel evaluation framework, statistical analysis, evaluation methodology documentation

---

## Competency 3: Safety & Reliability Engineering

> The ability to build AI systems that fail gracefully, resist misuse, and maintain appropriate boundaries.

### Developing Level

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Implement basic input validation** | Code that rejects malformed or out-of-scope inputs |
| **Implement basic output filtering** | Code that catches and handles problematic outputs |
| **Identify common failure modes** | Written list of hallucination, injection, drift risks |
| **Document safety boundaries** | Clear statement of what the system should never do |
| **Implement basic rate limiting** | Protection against resource exhaustion |

**Evidence artifacts:** Validation code, filter code, failure mode documentation, safety boundary specification

### Proficient Level

*Includes all Developing indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Implement circuit breakers** | Automatic disabling when error rates exceed thresholds |
| **Design multi-layer safety boundaries** | Defense in depth across input, process, output stages |
| **Create fallback strategies** | Documented degradation paths when primary approach fails |
| **Implement prompt injection defenses** | Specific mitigations for injection attacks |
| **Design human escalation workflows** | Clear criteria and process for human intervention |
| **Create incident response procedures** | Runbook for handling AI system failures |

**Evidence artifacts:** Circuit breaker implementation, layered defense documentation, escalation workflow, incident runbook

### Advanced Level

*Includes all Proficient indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Anticipate novel failure modes** | Analysis of failure modes specific to new system designs |
| **Design safety systems that degrade gracefully under attack** | Adversarial robustness analysis and mitigations |
| **Balance safety constraints with capability** | Documented trade-offs between safety and usefulness |
| **Design for safe capability expansion** | Framework for safely adding new capabilities |
| **Create safety patterns others can adopt** | Reusable safety components with documentation |

**Evidence artifacts:** Novel failure mode analysis, adversarial robustness report, safety/capability trade-off analysis

---

## Competency 4: AI Output Review & Oversight

> The ability to design and implement effective human oversight of AI-generated content.

### Developing Level

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Identify outputs requiring human review** | Classification of output types by review necessity |
| **Implement confidence thresholds for escalation** | Code that routes low-confidence outputs to humans |
| **Document review criteria** | Written standards for what makes an output acceptable |
| **Create basic review interfaces** | UI or workflow that surfaces outputs for review |
| **Track review decisions** | Logging of what was reviewed and outcomes |

**Evidence artifacts:** Output classification scheme, escalation code, review criteria document, review interface

### Proficient Level

*Includes all Developing indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design review workflows for high-stakes outputs** | End-to-end process for critical decision review |
| **Implement calibrated confidence scoring** | Confidence scores that correlate with actual accuracy |
| **Create reviewer training materials** | Documentation that enables consistent review quality |
| **Design for reviewer efficiency** | Workflow optimizations that reduce review burden |
| **Implement review quality metrics** | Measurement of inter-rater reliability, review accuracy |
| **Design feedback loops from review to system** | Process for review insights to improve the system |

**Evidence artifacts:** High-stakes review workflow, calibration analysis, training materials, efficiency metrics

### Advanced Level

*Includes all Proficient indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design adaptive review systems** | Systems that learn which outputs need more review |
| **Optimize review coverage vs. efficiency** | Data-driven decisions about review sampling |
| **Identify systematic biases in review** | Analysis of reviewer bias patterns and mitigations |
| **Design for reviewer wellbeing** | Consideration of cognitive load, exposure to harmful content |
| **Create review frameworks for novel output types** | Original review methodologies for new AI capabilities |

**Evidence artifacts:** Adaptive review system design, coverage optimization analysis, bias analysis, wellbeing considerations

---

## Competency 5: Governance & Defensibility

> The ability to document, justify, and communicate AI system decisions to diverse stakeholders.

### Developing Level

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Document system decisions and rationale** | ADRs or decision logs with reasoning |
| **Create stakeholder-appropriate explanations** | Different explanations for technical vs. non-technical audiences |
| **Maintain audit trails** | Logging that enables reconstruction of decision history |
| **Identify key stakeholders** | Stakeholder map with interests and concerns |
| **Document system limitations** | Honest accounting of what the system cannot do |

**Evidence artifacts:** Decision log/ADR, stakeholder communications, audit log design, limitations document

### Proficient Level

*Includes all Developing indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Design governance frameworks** | Policies and procedures for AI system oversight |
| **Translate technical constraints to policy** | Documentation that non-technical stakeholders can act on |
| **Identify regulatory requirements** | Analysis of applicable regulations and compliance status |
| **Create accountability structures** | Clear ownership and escalation paths |
| **Design for explainability** | System features that support explanation of decisions |
| **Manage stakeholder expectations** | Proactive communication about capabilities and limits |

**Evidence artifacts:** Governance framework, policy documents, regulatory analysis, accountability matrix

### Advanced Level

*Includes all Proficient indicators, plus:*

| Indicator | Observable Evidence |
|-----------|---------------------|
| **Anticipate governance challenges in novel applications** | Proactive identification of governance gaps |
| **Design governance that scales** | Frameworks that work as organization/system grows |
| **Navigate transparency vs. competitive advantage** | Thoughtful trade-offs in what to disclose |
| **Influence policy development** | Contributions to internal or external policy discussions |
| **Create governance frameworks others can adopt** | Reusable governance templates and methodologies |

**Evidence artifacts:** Governance gap analysis, scalability analysis, transparency trade-off documentation

---

## Cross-Competency Integration

Real AI systems require **multiple competencies working together**. Advanced practitioners demonstrate integration:

| Integration Pattern | Competencies Combined | Evidence |
|---------------------|----------------------|----------|
| **Evaluated Safety** | Evaluation + Safety | Safety metrics in evaluation suite |
| **Governed Systems** | Systems Design + Governance | ADRs that include governance considerations |
| **Reviewable Outputs** | Output Review + Evaluation | Review decisions feed back into evaluation |
| **Defensible Reliability** | Safety + Governance | Incident response with stakeholder communication |
| **Full Stack** | All five | End-to-end system with all competencies visible |

The [AI for Science projects](projects/ai_for_science/) specifically require cross-competency integration.

---

## Using Rubrics in Projects

Each project README includes a **Competency Assessment** section structured like this:

```markdown
## Competency Assessment

This project develops the following competencies:

### Primary: Evaluation & Measurement — Proficient Level

| Indicator | Evidence Location | Self-Assessment |
|-----------|-------------------|-----------------|
| Design multi-dimensional evaluation suites | `evaluation/suite.py` | ☐ Not yet / ☐ Developing / ☐ Met |
| Implement regression testing | `tests/regression/` | ☐ Not yet / ☐ Developing / ☐ Met |
| Identify failure modes from data | `docs/failure_analysis.md` | ☐ Not yet / ☐ Developing / ☐ Met |

### Secondary: Systems Design — Developing Level

| Indicator | Evidence Location | Self-Assessment |
|-----------|-------------------|-----------------|
| Document system components | `docs/architecture.md` | ☐ Not yet / ☐ Developing / ☐ Met |
| Define system boundaries | `README.md#scope` | ☐ Not yet / ☐ Developing / ☐ Met |
```

Your artifacts should provide **evidence** for each indicator without additional explanation.

---

## Calibration Examples

To help you calibrate self-assessment, here are examples of what each level looks like in practice:

### Example: "Justify architectural choices with trade-off analysis"

**Developing (Not yet met):**
> "We chose LangChain because it's popular."

**Developing (Partially met):**
> "We chose LangChain because it has good documentation and supports multiple LLMs."

**Proficient (Met):**
> "We evaluated LangChain, LlamaIndex, and direct API calls. LangChain was selected because: (1) our team has existing experience, reducing ramp-up time by ~2 weeks; (2) the abstraction layer allows model switching without code changes, important given our multi-provider requirement; (3) the debugging overhead is acceptable for our latency budget (p99 < 2s). We rejected LlamaIndex because our use case is orchestration-heavy rather than retrieval-heavy. We rejected direct API calls because the maintenance burden of handling retries, rate limits, and provider differences exceeds our team capacity."

### Example: "Implement circuit breakers"

**Developing (Not yet met):**
> No circuit breaker implementation.

**Developing (Partially met):**
> Basic try/catch with logging.

**Proficient (Met):**
> Circuit breaker that: (1) tracks error rate over sliding window; (2) opens circuit when threshold exceeded; (3) implements half-open state for recovery testing; (4) logs state transitions; (5) exposes metrics for monitoring; (6) has documented threshold rationale.

---

## Frequently Asked Questions

### "What if I meet some indicators but not others at a level?"

That's normal. Competency development is uneven. Focus on the indicators most relevant to your current project. Use gaps to guide future learning.

### "How do I know if I'm being honest in self-assessment?"

Ask: "Could someone reviewing my artifacts independently reach the same conclusion?" If you need to explain why an artifact demonstrates something, it probably doesn't demonstrate it clearly enough.

### "What if my work demonstrates something not in the rubrics?"

These rubrics aren't exhaustive. If you've demonstrated something valuable that isn't captured here, document it. Consider proposing an addition to the rubrics.

### "How do these rubrics relate to job levels?"

Roughly:
- **Developing** → Entry-level / Junior (0-2 years)
- **Proficient** → Mid-level / Senior (2-5 years)  
- **Advanced** → Staff / Principal (5+ years)

But context matters. Someone can be Advanced in one competency and Developing in another.

---

## Contributing to Rubrics

These rubrics evolve based on community input. To suggest changes:

1. Open an issue with the `rubrics` label
2. Describe the indicator you'd add/modify/remove
3. Provide rationale based on real-world experience
4. Include calibration examples if possible

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution process.

---

## Related Documents

- [COMPETENCIES.md](COMPETENCIES.md) — Competency definitions and project mapping
- [LEARNING_PATHS.md](LEARNING_PATHS.md) — Role-based routes through the curriculum
- [projects/](projects/) — Hands-on projects that develop these competencies