[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Ethical Charter

Ethics in AI development is not optional — it's foundational. As AI systems become more capable and autonomous, the decisions we make in designing prompts, building agents, and deploying applications have real consequences for individuals and society.

This charter provides guiding principles for the Awesome Prompt Engineering community. It applies whether you're crafting prompts, building RAG systems, or orchestrating multi-agent workflows.

---

### Contents

- [Why Ethics Matters](#why-ethics-matters)
- [Core Values](#core-values)
- [Responsible AI Practices](#responsible-ai-practices)
- [Community Standards](#community-standards)
- [Acknowledgments](#acknowledgments)

---

## Why Ethics Matters

AI systems can:
- **Amplify biases** present in training data or prompt design
- **Generate misinformation** that appears authoritative
- **Enable harm** when safety measures are bypassed
- **Erode trust** when deployed without transparency
- **Concentrate power** when access is inequitable

As practitioners, we shape how these systems behave through the prompts we write, the guardrails we implement, and the applications we build. This responsibility extends beyond technical correctness to ethical consideration.

---

## Core Values

### Human-Centeredness

We design AI systems that serve human needs and enhance human capabilities, not replace human judgment on decisions that matter.

**In practice:**
- Design for human oversight, not full automation of consequential decisions
- Consider accessibility and usability for diverse users
- Preserve human agency and informed consent

### Honesty & Transparency

We are truthful about AI capabilities, limitations, and uncertainties. We don't present AI outputs as human-generated without disclosure.

**In practice:**
- Acknowledge when outputs are AI-generated
- Don't claim certainty where uncertainty exists
- Be transparent about how systems make decisions
- Document prompts and system behaviors

### Fairness & Equity

We design systems that treat all users equitably and don't perpetuate discrimination based on race, gender, age, disability, socioeconomic status, or other protected characteristics.

**In practice:**
- Test prompts and systems across demographic groups
- Audit outputs for bias and harmful patterns
- Consider who benefits and who might be harmed
- Ensure diverse representation in examples and training

### Privacy & Data Protection

We respect user privacy and handle data responsibly. We don't use AI to surveil, track, or manipulate without consent.

**In practice:**
- Minimize data collection to what's necessary
- Don't include personal data in prompts unnecessarily
- Be transparent about data usage
- Implement appropriate data retention limits

### Safety & Security

We build systems that are robust, secure, and fail gracefully. We don't deploy applications that pose unnecessary risks.

**In practice:**
- Implement guardrails against harmful outputs
- Test for prompt injection and other attacks
- Design for graceful degradation
- Monitor deployed systems for misuse

### Accountability

We take responsibility for the systems we build and their impacts. We don't hide behind "the AI did it" when things go wrong.

**In practice:**
- Maintain audit trails for consequential decisions
- Establish clear ownership of AI systems
- Create feedback mechanisms for affected users
- Commit to addressing harms when they occur

---

## Responsible AI Practices

### For Prompt Engineers

**Do:**
- Include safety guidelines in system prompts
- Test prompts with adversarial inputs
- Document intended use and limitations
- Consider edge cases and failure modes
- Use appropriate output constraints

**Don't:**
- Share prompts designed to bypass safety measures
- Create prompts for deception or manipulation
- Ignore potential for misuse
- Assume the model will "do the right thing"

### For Agent Builders

**Do:**
- Implement appropriate permission boundaries
- Add human-in-the-loop for consequential actions
- Log agent actions for auditability
- Set iteration limits and safety stops
- Test extensively before deployment

**Don't:**
- Give agents unnecessary capabilities
- Deploy autonomous agents without oversight
- Skip testing on edge cases
- Ignore failure modes

### For Application Developers

**Do:**
- Be transparent about AI use to end users
- Implement rate limiting and abuse prevention
- Monitor for misuse patterns
- Provide feedback mechanisms
- Plan for model updates and deprecations

**Don't:**
- Misrepresent AI capabilities
- Deploy without adequate testing
- Ignore security vulnerabilities
- Collect unnecessary user data

### For RAG Systems

**Do:**
- Cite sources appropriately
- Verify retrieval quality
- Handle missing information gracefully
- Respect intellectual property
- Consider source bias

**Don't:**
- Present retrieved content as original
- Ignore source credibility
- Skip attribution requirements
- Mix facts with speculation without distinction

---

## Community Standards

### Contributions

When contributing to this repository:
- Share techniques that promote responsible AI use
- Don't contribute prompts designed to bypass safety measures
- Include safety considerations in examples
- Flag potential misuse risks
- Respect intellectual property

### Discussions

When participating in community discussions:
- Be respectful of diverse perspectives
- Engage in good faith
- Acknowledge uncertainty
- Share knowledge generously
- Welcome newcomers

### Reporting

If you identify:
- Safety vulnerabilities in shared prompts
- Content that violates these principles
- Potential for misuse

Please report via GitHub issues or contact the maintainers directly.

---

## Acknowledgments

These principles draw from:
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/index/anthropics-responsible-scaling-policy)
- [OpenAI Usage Policies](https://openai.com/policies/usage-policies)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [EU AI Act](https://artificialintelligenceact.eu/)
- [Partnership on AI](https://partnershiponai.org/)
- [IEEE Ethically Aligned Design](https://ethicsinaction.ieee.org/)

---

## Commitment

By participating in this community, we commit to:

1. **Building responsibly** — Considering impacts before deployment
2. **Sharing openly** — Contributing knowledge that advances the field
3. **Acting with integrity** — Being honest about capabilities and limitations
4. **Serving humanity** — Prioritizing human wellbeing in our work
5. **Evolving continuously** — Updating practices as the field develops

---

### Notes

This charter is a living document. As AI capabilities evolve, so must our ethical frameworks. We welcome suggestions for improvements.

Feedback and suggestions are welcome!

*Last updated: January 2026*