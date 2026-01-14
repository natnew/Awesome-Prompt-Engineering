# How LLMs Work

*Mental models for language models—no ML background required.*

**Time:** 20 minutes  
**Competencies:** All (foundational understanding)

---

## The One-Sentence Version

Large Language Models (LLMs) predict what text comes next, based on patterns learned from massive amounts of human-written text.

That's it. Everything else is elaboration.

---

## Mental Model 1: The Autocomplete Machine

You've used autocomplete on your phone. Type "I'm running" and it suggests "late" or "out of" or "a marathon." It learned these predictions from text patterns.

LLMs are autocomplete at massive scale:
- Trained on billions of documents
- Can complete any text, not just common phrases
- Good enough to seem intelligent

**Key insight:** LLMs don't "know" things the way you do. They predict what text would plausibly come next based on patterns they've seen.

---

## Mental Model 2: The Pattern Matcher

Imagine you've read every book, article, and website ever written. Someone shows you the beginning of a sentence. Based on everything you've read, what word is most likely to come next?

LLMs do this statistically:

```
Input: "The capital of France is"
Model thinks: Based on patterns...
  - "Paris" appeared after similar text 99% of the time
  - "London" appeared 0.01% of the time
  - "pizza" appeared 0.0001% of the time
Output: "Paris"
```

**Key insight:** LLMs are incredibly good pattern matchers. They match patterns in your prompt against patterns from training data.

---

## Mental Model 3: The Stochastic Parrot

This term (originally somewhat critical) captures an important truth: LLMs generate text that sounds like the text they trained on.

- Scientific papers in → scientific-sounding text out
- Code comments in → code-comment-style text out
- Reddit arguments in → Reddit-argument-style text out

**Key insight:** The "style" of output reflects the style of training data. If you want different output, provide different input patterns.

---

## How Generation Actually Works

### Step by Step

1. **You provide a prompt**
   ```
   "Write a haiku about debugging"
   ```

2. **Model converts to tokens** (see [Tokens and Context](tokens_and_context.md))
   ```
   ["Write", " a", " ha", "iku", " about", " debug", "ging"]
   ```

3. **Model predicts next token**
   - Considers all patterns that match this context
   - Assigns probability to every possible next token
   - Selects one (selection method varies)

4. **Repeat until done**
   - Generated token becomes part of context
   - Predict next token
   - Continue until stop condition

### The Probability Distribution

At each step, the model produces probabilities:

```
After "Write a haiku about debugging":

Next token probabilities:
  "\n" (newline)     → 45%
  "Code"             → 12%
  "Silent"           → 8%
  "Error"            → 6%
  "The"              → 5%
  ... thousands more options
```

### Temperature: Controlling Randomness

**Temperature** controls how the model samples from this distribution:

| Temperature | Behavior | Use Case |
|:------------|:---------|:---------|
| 0.0 | Always pick highest probability | Factual tasks, consistency |
| 0.7 | Usually pick high probability, some variation | General use, creativity |
| 1.0 | Sample according to distribution | Creative writing |
| 1.5+ | Flatten distribution, more random | Brainstorming, exploration |

```
Temperature 0.0: "Code fails silently in the dark..."
Temperature 0.7: "Bugs hide in logic, waiting to emerge..."
Temperature 1.5: "Quantum semicolons dance through functions..."
```

**Key insight:** Temperature doesn't make the model "more creative"—it makes selection more random. Sometimes that produces creative results; sometimes nonsense.

---

## What LLMs Are Good At

### Pattern Completion
If the pattern exists in training data, LLMs can complete it:
- Code following conventions
- Text in specific formats
- Responses to common questions

### Style Transfer
Converting content from one form to another:
- Formal ↔ casual
- Technical ↔ simple
- Long ↔ summarized

### In-Context Learning
Learning from examples you provide in the prompt:
```
Example: "happy" → "joyful"
Example: "sad" → "melancholy"
Task: "angry" → ?

Model: "furious"
```

### Synthesis
Combining information in novel ways:
- Explaining concept A in terms of concept B
- Mixing styles or formats
- Connecting disparate ideas

---

## What LLMs Are Bad At

### Reliable Factual Recall
LLMs don't "look up" facts. They predict plausible-sounding facts.

```
Q: "When was the Eiffel Tower built?"
A: "1889" (correct—pattern is strong)

Q: "When was the Treaty of Westphalia signed?"
A: "1648" (correct—pattern exists)

Q: "Who was the 14th employee at Anthropic?"
A: "[plausible-sounding name]" (wrong—no pattern)
```

**Key insight:** Confidence in output doesn't correlate with correctness. The model speaks with equal confidence about things it "knows" and things it's making up.

### Consistent Counting and Math
LLMs process text, not numbers as mathematical objects.

```
Q: "How many r's in strawberry?"
A: "2" (often wrong—requires character-level processing)

Q: "What's 23 × 47?"
A: "1081" (often wrong—text pattern matching isn't arithmetic)
```

### True Reasoning
What looks like reasoning is often pattern matching against reasoning patterns in training data.

```
Good: Standard logic puzzles (seen similar in training)
Bad: Novel logical problems (no pattern to match)
```

### Knowing What They Don't Know
LLMs can't reliably distinguish "I know this" from "this sounds plausible."

---

## The Training Process (Simplified)

### Phase 1: Pre-training
- Feed model enormous amounts of text
- Model learns to predict next tokens
- Captures language patterns, facts, reasoning patterns
- Creates a base model that's good at completing text

### Phase 2: Fine-tuning
- Train on specific formats (instruction-following, conversation)
- Model learns to respond helpfully to prompts
- Creates an assistant-like model

### Phase 3: RLHF (Reinforcement Learning from Human Feedback)
- Humans rate model outputs
- Model learns to produce outputs humans prefer
- Improves helpfulness, reduces harm

**Key insight:** The model you interact with has been specifically trained to be helpful. Base models (pre-training only) aren't naturally conversational.

---

## Implications for Prompt Engineering

### 1. Prompt as Context
Your prompt is the start of a text the model will complete. To get good completions, provide context that makes the desired completion likely.

**Weak:** "Write code"
**Strong:** "Write a Python function that takes a list of integers and returns their sum. Include docstring and type hints."

### 2. Examples are Powerful
In-context learning lets you teach the model patterns on the fly.

```
Format examples like:
Input: X
Output: Y

Input: A
Output: B

Input: [actual task]
Output:
```

### 3. Specificity Matters
Vague prompts get vague completions. The model completes what you give it.

**Vague:** "Help me with my email"
**Specific:** "Write a professional email declining a meeting invitation due to a scheduling conflict. Keep it under 100 words."

### 4. Format Influences Output
If your prompt looks like code, output looks like code. If it looks like a formal letter, output looks formal.

---

## Common Misconceptions

### "The model understands what I mean"
It predicts what text would follow yours. Understanding is a useful metaphor, not literal truth.

### "More tokens = better thinking"
More tokens = more predictions. Each prediction can accumulate errors. Longer isn't always better.

### "The model reasons step by step"
It generates text that looks like step-by-step reasoning, which often produces better answers. But it's generating patterns, not "reasoning" in the human sense.

### "The model has a personality"
It produces text consistent with a persona pattern. The pattern can be shifted with prompting.

### "Newer/bigger is always better"
Different models have different trade-offs. Newer isn't always better for your specific use case.

---

## Summary

LLMs are statistical pattern matchers that predict text continuations based on training data.

**This means:**
- They complete patterns, not answer questions (though it looks similar)
- Confidence doesn't equal correctness
- Your prompt is context that shapes the completion
- Examples in prompts teach patterns on the fly
- Output style follows input style

**Practical takeaways:**
- Be specific in prompts
- Provide examples when format matters
- Don't trust outputs without verification
- Use the right model for the task
- Understand that "magic" is statistics at scale

---

## Further Reading

- [Tokens and Context](tokens_and_context.md) — The mechanics of input/output
- [Prompt Engineering Principles](prompt_principles.md) — Applying these mental models
- [Evaluation Fundamentals](evaluation_fundamentals.md) — Measuring output quality
