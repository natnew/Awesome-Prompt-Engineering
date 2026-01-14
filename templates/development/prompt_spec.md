# Prompt Specification Template

## Overview

**Purpose:** Document prompt design decisions, expected behaviors, and evaluation criteria.

**When to use:** Complex prompt development, team collaboration, version control.

**Competencies:** [Prompt Design & Optimization](../../COMPETENCIES.md#1-prompt-design--optimization), [Evaluation & Measurement](../../COMPETENCIES.md#2-evaluation--measurement)

---

# Prompt Specification: [Prompt Name]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Version:** 1.0  
**Status:** Draft | Testing | Production

---

## Summary

| Attribute | Value |
|:----------|:------|
| **Purpose** | _[What this prompt does]_ |
| **Model** | _[Target model(s)]_ |
| **Context Window** | _[Token budget]_ |
| **Temperature** | _[Value and rationale]_ |
| **Use Case** | _[Where this is used]_ |

---

## Objective

### What It Should Do

_[Clear description of desired behavior]_

### What It Should NOT Do

_[Explicit anti-goals]_

### Success Criteria

| Criterion | Target | Measurement |
|:----------|:-------|:------------|
| _[Criterion 1]_ | _[Target]_ | _[How measured]_ |
| _[Criterion 2]_ | _[Target]_ | _[How measured]_ |
| _[Criterion 3]_ | _[Target]_ | _[How measured]_ |

---

## Prompt Structure

### System Prompt

```
[Full system prompt text]
```

**Design decisions:**

| Section | Purpose | Why This Approach |
|:--------|:--------|:------------------|
| _[Section 1]_ | _[Purpose]_ | _[Rationale]_ |
| _[Section 2]_ | _[Purpose]_ | _[Rationale]_ |

### User Message Template

```
[Template with placeholders]

Example:
{context}

User question: {query}
```

**Variables:**

| Variable | Type | Description | Constraints |
|:---------|:-----|:------------|:------------|
| `{context}` | string | Retrieved documents | Max 2000 tokens |
| `{query}` | string | User's question | Max 500 tokens |

### Few-Shot Examples (If Used)

**Example 1:**
```
User: [Example input]
Assistant: [Example output]
```

**Why this example:**  
_[What it teaches the model]_

**Example 2:**
```
User: [Example input]
Assistant: [Example output]
```

**Why this example:**  
_[What it teaches the model]_

---

## Expected Behaviors

### Typical Responses

| Input Type | Expected Output | Example |
|:-----------|:----------------|:--------|
| _[Type 1]_ | _[Expected behavior]_ | _[Example]_ |
| _[Type 2]_ | _[Expected behavior]_ | _[Example]_ |

### Edge Cases

| Edge Case | Expected Behavior | Rationale |
|:----------|:------------------|:----------|
| Empty input | _[Behavior]_ | _[Why]_ |
| Very long input | _[Behavior]_ | _[Why]_ |
| Off-topic query | _[Behavior]_ | _[Why]_ |
| Ambiguous query | _[Behavior]_ | _[Why]_ |
| Multiple questions | _[Behavior]_ | _[Why]_ |

### Refusals

When should the prompt refuse to answer?

| Scenario | Response | Example |
|:---------|:---------|:--------|
| _[Scenario 1]_ | _[How to refuse]_ | _[Example]_ |
| _[Scenario 2]_ | _[How to refuse]_ | _[Example]_ |

---

## Output Format

### Structure

```
[Expected output structure]
```

### Constraints

| Constraint | Value | Enforced By |
|:-----------|:------|:------------|
| Max length | _[Tokens/chars]_ | _[Prompt/code]_ |
| Format | _[JSON/Markdown/etc]_ | _[How enforced]_ |
| Tone | _[Formal/casual/etc]_ | _[Prompt]_ |
| Citations | _[Required/optional]_ | _[Prompt]_ |

### Validation

How do we validate outputs?

```python
# Output validation logic
def validate_output(output):
    # [Validation rules]
    pass
```

---

## Safety Considerations

### Potential Harms

| Harm | Likelihood | Mitigation |
|:-----|:-----------|:-----------|
| _[Harm 1]_ | _[L/M/H]_ | _[Mitigation]_ |
| _[Harm 2]_ | _[L/M/H]_ | _[Mitigation]_ |

### Guardrails

| Guardrail | Implementation | Test |
|:----------|:---------------|:-----|
| _[Guardrail 1]_ | _[How]_ | _[How tested]_ |
| _[Guardrail 2]_ | _[How]_ | _[How tested]_ |

### Sensitive Topics

How should the prompt handle sensitive topics?

| Topic | Handling |
|:------|:---------|
| _[Topic 1]_ | _[Approach]_ |
| _[Topic 2]_ | _[Approach]_ |

---

## Testing

### Test Cases

| ID | Input | Expected Output | Priority |
|:---|:------|:----------------|:---------|
| T01 | _[Input]_ | _[Output]_ | P0 |
| T02 | _[Input]_ | _[Output]_ | P0 |
| T03 | _[Input]_ | _[Output]_ | P1 |

### Adversarial Tests

| ID | Attack Type | Input | Expected Behavior |
|:---|:------------|:------|:------------------|
| A01 | Injection | _[Input]_ | _[Should resist]_ |
| A02 | Jailbreak | _[Input]_ | _[Should refuse]_ |

### Performance Benchmarks

| Metric | Target | Current |
|:-------|:-------|:--------|
| Accuracy | _[%]_ | _[%]_ |
| Latency (p95) | _[ms]_ | _[ms]_ |
| Token usage (avg) | _[tokens]_ | _[tokens]_ |

---

## Implementation Notes

### Dependencies

| Dependency | Version | Purpose |
|:-----------|:--------|:--------|
| _[Dep 1]_ | _[Version]_ | _[Why needed]_ |

### Configuration

| Parameter | Value | Notes |
|:----------|:------|:------|
| model | _[Model ID]_ | |
| temperature | _[Value]_ | _[Why this value]_ |
| max_tokens | _[Value]_ | _[Why this value]_ |
| top_p | _[Value]_ | _[If used]_ |

### Code Location

```
File: [path/to/prompt.py]
Function: [function_name]
Config: [path/to/config.yaml]
```

---

## Version History

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 1.0 | _[Date]_ | _[Name]_ | Initial version |

### Migration Notes

When updating to new version:
- _[Migration step 1]_
- _[Migration step 2]_

---

## Alternatives Considered

| Alternative | Why Not Chosen |
|:------------|:---------------|
| _[Alternative 1]_ | _[Reason]_ |
| _[Alternative 2]_ | _[Reason]_ |

---

## Open Questions

- [ ] _[Question 1]_
- [ ] _[Question 2]_

---

*Template version: 1.0*  
*Last updated: [Date]*
