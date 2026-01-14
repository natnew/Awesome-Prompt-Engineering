# Prompt Engineering Principles

*Core principles that transfer across models and use cases.*

**Time:** 25 minutes  
**Competencies:** [Prompt Design & Optimization](../COMPETENCIES.md#1-prompt-design--optimization)

---

## What Is Prompt Engineering?

Prompt engineering is the practice of crafting inputs to AI models to get useful outputs. It's part writing, part psychology, part engineering—shaping context to influence generation.

**The core insight:** The model completes your prompt. Better prompts make better completions more likely.

---

## Principle 1: Be Specific

Vague prompts produce vague outputs. Specificity reduces ambiguity and guides the model toward what you want.

### Dimensions of Specificity

| Dimension | Vague | Specific |
|:----------|:------|:---------|
| Task | "Help with my code" | "Debug this Python function that should return prime numbers" |
| Format | "Summarize this" | "Summarize in 3 bullet points, max 20 words each" |
| Tone | "Write an email" | "Write a formal email appropriate for a senior executive" |
| Scope | "Explain machine learning" | "Explain gradient descent for someone who knows algebra but not calculus" |
| Output | "Give me ideas" | "List 5 specific, actionable marketing strategies for a B2B SaaS product" |

### The Specificity Test

Ask: "Could two reasonable people interpret this prompt differently?" If yes, add specificity.

---

## Principle 2: Provide Context

Models work with what you give them. Context shapes everything.

### Types of Context

**Background:** What the model needs to know
```
"You are helping a senior software engineer who prefers concise answers."
```

**Constraints:** What limits apply
```
"The solution must work in Python 3.8 without external dependencies."
```

**Examples:** What good looks like
```
"Here's an example of the format I want: [example]"
```

**History:** What's happened before
```
"Previously we discussed X and decided Y. Now..."
```

### Context Placement

Put context before the task:

```
❌ "Write a function. By the way, use Python."

✓ "Using Python 3.8+, write a function that..."
```

---

## Principle 3: Use Examples (Few-Shot Learning)

Examples are often more effective than descriptions. Show, don't just tell.

### Few-Shot Structure

```
Here are examples of the task:

Input: [example input 1]
Output: [example output 1]

Input: [example input 2]
Output: [example output 2]

Input: [actual task input]
Output:
```

### How Many Examples?

| Situation | Examples Needed |
|:----------|:----------------|
| Format is clear, task is common | 0-1 |
| Format needs demonstration | 2-3 |
| Task is unusual | 3-5 |
| Complex transformation | 5+ |

### Example Selection

Good examples:
- Cover typical cases
- Include edge cases if important
- Are correct (the model learns your mistakes too)
- Are diverse (not all identical)

---

## Principle 4: Structure Your Prompts

Organized prompts produce organized outputs. Structure reduces ambiguity.

### Common Structures

**Role-Task-Format:**
```
ROLE: You are a senior code reviewer.

TASK: Review the following code for security issues.

FORMAT: List each issue with:
- Line number
- Issue description
- Severity (High/Medium/Low)
- Suggested fix

CODE:
[code here]
```

**Context-Instructions-Input:**
```
CONTEXT:
We're building a customer support chatbot for an e-commerce site.

INSTRUCTIONS:
Generate a response that:
1. Acknowledges the customer's concern
2. Provides a solution
3. Offers additional help

CUSTOMER MESSAGE:
"My order hasn't arrived and it's been 10 days."
```

### XML Tags for Structure

Many models respond well to XML-style structure:

```xml
<task>Summarize the key points</task>

<context>
This is a technical document about database optimization.
The audience is senior engineers.
</context>

<document>
[document content]
</document>

<requirements>
- Maximum 5 bullet points
- Focus on actionable recommendations
- Technical detail is appropriate
</requirements>
```

---

## Principle 5: Think Step-by-Step

For complex reasoning, ask the model to show its work.

### Chain-of-Thought Prompting

```
❌ "What's 15% of $847.50?"

✓ "What's 15% of $847.50? Show your calculation step by step."
```

### Why It Works

Step-by-step generation:
- Reduces errors that compound
- Makes reasoning visible (debuggable)
- Follows patterns from training data where step-by-step solutions are common

### When to Use

| Task Type | Step-by-Step Helps? |
|:----------|:--------------------|
| Complex reasoning | Yes |
| Multi-step problems | Yes |
| Simple factual recall | No |
| Creative writing | Sometimes |
| Format transformation | Usually no |

---

## Principle 6: Specify Output Format

Explicitly state what format you want. Don't leave it to chance.

### Format Specifications

```
Respond in JSON:
{
  "summary": "string",
  "key_points": ["string", "string"],
  "sentiment": "positive|negative|neutral"
}
```

```
Format as a markdown table with columns:
| Feature | Benefit | Limitation |
```

```
Respond with ONLY the corrected code. No explanations.
```

### Positive vs. Negative Framing

```
✓ "Include only the relevant information."
✓ "Do not include personal opinions."

Both work, but positive framing is often clearer.
```

---

## Principle 7: Set Boundaries

Tell the model what NOT to do, not just what to do.

### Common Boundaries

```
- Do not make up information. If unsure, say "I don't know."
- Do not include personal opinions on controversial topics.
- Do not provide medical/legal advice.
- If the task is unclear, ask for clarification rather than guessing.
```

### Scope Boundaries

```
Focus only on:
- Frontend performance issues
- React-specific optimizations

Do not discuss:
- Backend changes
- Database optimization
- Infrastructure
```

---

## Principle 8: Iterate and Refine

Prompt engineering is empirical. Test, observe, refine.

### The Iteration Loop

```
1. Write initial prompt
2. Test with representative inputs
3. Observe failures/suboptimal outputs
4. Identify patterns in failures
5. Adjust prompt to address patterns
6. Test again
7. Repeat until satisfactory
```

### What to Adjust

| Problem | Potential Adjustment |
|:--------|:--------------------|
| Wrong format | Add format examples |
| Too verbose | Add length constraints |
| Missing information | Add to context |
| Off-topic content | Add scope boundaries |
| Inconsistent | Increase specificity |
| Too conservative | Adjust constraints |

---

## Principle 9: Match Prompt to Model

Different models have different strengths and training. Adjust accordingly.

### Model Considerations

| Consideration | Implication |
|:--------------|:------------|
| Context window | How much you can include |
| Training data | What patterns exist |
| Instruction tuning | How well it follows directions |
| System prompt support | Where to put role/instructions |

### Model-Specific Optimizations

What works for Claude might not work for GPT-4, and vice versa. When switching models:
- Test your existing prompts
- Adjust based on output differences
- Consult model-specific documentation

---

## Anti-Patterns

### The Politeness Tax

```
❌ "Could you please, if it's not too much trouble, maybe 
    help me with summarizing this document? Thank you so 
    much in advance!"

✓ "Summarize this document in 3 bullet points."
```

Politeness is fine, but don't let it obscure the task.

### Prompt Stuffing

```
❌ "You are the world's best expert in everything, with 
    perfect knowledge, infinite wisdom, and the ability 
    to solve any problem..."

✓ "You are a senior software engineer."
```

More adjectives doesn't mean better output.

### Ambiguous Pronouns

```
❌ "Compare them and tell me which is better."

✓ "Compare Python and JavaScript for web development. 
    Recommend which is better for a beginner building 
    their first interactive website."
```

What is "them"? What is "better"?

### Implicit Assumptions

```
❌ "Continue the story."

✓ "Continue this fantasy story, maintaining the 
    first-person perspective and ominous tone."
```

What story? What style? What perspective?

---

## Putting It Together

### Example: Complete Prompt

```
ROLE:
You are a technical writer creating documentation for 
a software library.

CONTEXT:
The library is a Python package for data validation.
The audience is intermediate Python developers.
Documentation style should be clear and practical.

TASK:
Write documentation for the following function.

REQUIREMENTS:
- Include a brief description (1-2 sentences)
- Document all parameters with types
- Document return value
- Provide 2 usage examples
- Note any exceptions that may be raised

FORMAT:
Use NumPy-style docstrings.

FUNCTION:
[function code here]
```

### Checklist

Before finalizing a prompt:

- [ ] Is the task clearly stated?
- [ ] Is the output format specified?
- [ ] Is necessary context provided?
- [ ] Are constraints/boundaries set?
- [ ] Would examples help?
- [ ] Is it as specific as it needs to be?
- [ ] Have I tested with representative inputs?

---

## Summary

| Principle | Key Idea |
|:----------|:---------|
| Be Specific | Remove ambiguity |
| Provide Context | Give background, constraints, history |
| Use Examples | Show, don't just tell |
| Structure Prompts | Organize for clarity |
| Think Step-by-Step | For complex reasoning |
| Specify Format | Explicitly state output structure |
| Set Boundaries | Define what NOT to do |
| Iterate | Test and refine empirically |
| Match to Model | Adjust for model capabilities |

---

## Further Reading

- [How LLMs Work](how_llms_work.md) — Why these principles work
- [Tokens and Context](tokens_and_context.md) — Mechanics of prompts
- [Evaluation Fundamentals](evaluation_fundamentals.md) — Measuring prompt effectiveness
