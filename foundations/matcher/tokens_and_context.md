# Tokens and Context

*The currency of LLM interaction.*

**Time:** 15 minutes  
**Competencies:** [Prompt Design](../COMPETENCIES.md#1-prompt-design--optimization), [Systems Design](../COMPETENCIES.md#5-systems-design--integration)

---

## What Are Tokens?

Tokens are the units LLMs read and write. Not quite words, not quite characters—something in between.

```
"Hello, world!" → ["Hello", ",", " world", "!"]  (4 tokens)
"tokenization" → ["token", "ization"]  (2 tokens)
"ChatGPT" → ["Chat", "G", "PT"]  (3 tokens)
```

### Why Tokens Matter

1. **Pricing:** You pay per token (input and output)
2. **Limits:** Context windows are measured in tokens
3. **Performance:** More tokens = more computation = slower

### Tokenization Rules of Thumb

| Content Type | Rough Estimate |
|:-------------|:---------------|
| English text | ~1 token per 4 characters |
| English text | ~1 token per 0.75 words |
| Code | Often more tokens (syntax, punctuation) |
| Other languages | Varies (can be 2-3x more tokens) |
| Numbers | Each digit often a separate token |

```
"The quick brown fox" → ~4 tokens
"def calculate_sum():" → ~6 tokens  
"東京" (Tokyo) → ~2 tokens (but varies by model)
```

### Checking Token Counts

Most providers offer tokenizers:
- OpenAI: [tiktoken](https://github.com/openai/tiktoken)
- Anthropic: Built into API responses
- Many online tools available

**Always verify token counts for cost-sensitive applications.**

---

## The Context Window

The **context window** is the maximum tokens a model can process in one request (input + output combined).

```
┌────────────────────────────────────────────────────┐
│                 CONTEXT WINDOW                      │
│  ┌──────────────────┐  ┌───────────────────────┐   │
│  │   Input Tokens   │  │    Output Tokens      │   │
│  │    (your prompt) │  │  (model's response)   │   │
│  └──────────────────┘  └───────────────────────┘   │
└────────────────────────────────────────────────────┘
```

### Current Context Windows (as of 2024-2025)

| Model Family | Typical Window |
|:-------------|:---------------|
| GPT-4o | 128K tokens |
| Claude 3.5 | 200K tokens |
| Gemini 1.5 | 1M+ tokens |
| Smaller/older models | 4K-32K tokens |

### What Happens at the Limit?

If your prompt exceeds the context window:
- Request fails (error)
- Or: Content is truncated (some systems)

If input + output would exceed:
- Output is cut off mid-response
- Or: Model stops generating earlier

---

## Context Window Strategies

### Strategy 1: Know Your Budget

```
Available: 128K tokens
System prompt: 2K
User history: 10K
Retrieved docs: 20K
Response budget: 4K
─────────────────
Total: 36K (under budget ✓)
```

**Always reserve space for the response.**

### Strategy 2: Prioritize Information

Not all context is equally valuable. Prioritize:

| Priority | Content Type |
|:---------|:-------------|
| Highest | Task instructions |
| High | Most relevant retrieved content |
| Medium | Recent conversation history |
| Lower | Background context |
| Lowest | Examples (if space tight) |

### Strategy 3: Summarize Older Context

For long conversations:

```
[Full system prompt]
[Summary of conversation so far: "User asked about X, Y, Z..."]
[Last 3 exchanges in full]
[Current user message]
```

### Strategy 4: Chunk Large Documents

For documents exceeding context:

```
Option 1: Process in chunks, combine results
Option 2: Use retrieval to select relevant chunks
Option 3: Pre-summarize, then use summary
```

---

## Input vs. Output Token Costs

Most providers charge differently:

| Token Type | Relative Cost |
|:-----------|:--------------|
| Input tokens | 1x |
| Output tokens | 2-4x (varies) |

**Implication:** Long prompts with short outputs are cheaper than short prompts with long outputs.

### Cost Optimization Strategies

1. **Cache repeated content** — Don't resend static prompts every time
2. **Limit output length** — Set max_tokens appropriately
3. **Be specific** — Vague prompts generate longer, rambling outputs
4. **Use appropriate models** — Don't use GPT-4 for GPT-3.5 tasks

---

## Context and Memory

LLMs have **no memory between requests**. Each request is independent.

```
Request 1: "My name is Alice"
Response 1: "Nice to meet you, Alice!"

Request 2: "What's my name?"
Response 2: "I don't know your name."  // No memory of Request 1
```

### Simulating Memory

To maintain conversation context, include history in each request:

```
Request 2 (with context):
[System: You are a helpful assistant]
[User: My name is Alice]
[Assistant: Nice to meet you, Alice!]
[User: What's my name?]

Response 2: "Your name is Alice."  // "Remembers" via context
```

**Key insight:** Memory is illusion. Previous exchanges are passed as context, consuming tokens.

### Memory Implications

| Conversation Length | Context Used | Cost Implication |
|:--------------------|:-------------|:-----------------|
| 5 exchanges | ~2K tokens | Low |
| 20 exchanges | ~10K tokens | Medium |
| 100 exchanges | ~50K tokens | High |

Long conversations can become expensive. Summarization helps.

---

## System Prompts vs. User Prompts

Most APIs distinguish:

### System Prompt
- Sets behavior, persona, instructions
- Often cached/reused across requests
- Typically placed first in context
- Higher "authority" in some models

### User Prompt
- The actual request
- Changes each interaction
- What the user typed

### Assistant Responses
- Previous model outputs
- Included for conversation continuity

```
Context structure:
┌─────────────────────────┐
│ System: "You are..."    │  ← Sets behavior
├─────────────────────────┤
│ User: "First message"   │  ← Conversation
│ Assistant: "Response 1" │     history
│ User: "Second message"  │
│ Assistant: "Response 2" │
├─────────────────────────┤
│ User: "Current message" │  ← Current request
└─────────────────────────┘
```

---

## Position Matters

Where information appears in context affects how the model uses it.

### Primacy Effect
Information at the start of context tends to be weighted more heavily.

### Recency Effect
Information at the end (closest to where generation starts) is also weighted heavily.

### The "Lost in the Middle" Problem
Information in the middle of very long contexts may be underweighted.

**Practical advice:**
- Put critical instructions at start AND end
- Put most relevant retrieved content near the end
- Don't bury important information in the middle of long contexts

---

## Token-Efficient Prompting

### Verbose vs. Concise

```
Verbose (42 tokens):
"I would like you to please help me write a professional 
email message that I can send to my colleague to inform 
them about the upcoming meeting that is scheduled for Friday."

Concise (18 tokens):
"Write a professional email informing a colleague about 
Friday's meeting."
```

Same intent, half the tokens.

### When to Be Verbose

- Complex reasoning tasks benefit from detailed instructions
- Few-shot examples improve quality (worth the tokens)
- Ambiguous tasks need clarification

### When to Be Concise

- Simple, clear tasks
- Repeated/high-volume requests
- Cost-sensitive applications

---

## Practical Exercises

### Exercise 1: Estimate Tokens
Before checking, estimate tokens for:
- A 500-word email
- A Python function (30 lines)
- This page

### Exercise 2: Context Budgeting
Design context allocation for:
- Customer support bot (128K window)
- Code assistant (32K window)
- Document Q&A (200K window)

### Exercise 3: Cost Comparison
Calculate cost for:
- 100K requests with 500 input + 200 output tokens
- Compare across different model tiers

---

## Summary

**Tokens:**
- Basic units of LLM processing
- ~4 characters or ~0.75 words in English
- Input and output both count
- Different pricing for input vs. output

**Context Window:**
- Maximum tokens per request
- Must fit prompt + response
- Larger ≠ always better (cost, latency)

**Memory:**
- LLMs have no memory between requests
- "Memory" is context included in each request
- Long conversations consume many tokens

**Optimization:**
- Be concise when possible
- Reserve space for outputs
- Prioritize information by relevance
- Position matters (start and end preferred)

---

## Further Reading

- [How LLMs Work](how_llms_work.md) — Why tokenization matters
- [Prompt Engineering Principles](prompt_principles.md) — Applying token knowledge
- Provider-specific tokenizer documentation
