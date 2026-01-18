---
layout: default
title: AI Cheat Sheet
description: Quick reference for prompts, parameters, and patterns.
nav_order: 13
---

[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## AI Cheat Sheet

Quick reference for working with LLMs. Copy-paste patterns, parameter settings, and practical formulas.

---

### Contents

- [Prompt Patterns](#prompt-patterns)
- [API Parameters](#api-parameters)
- [Token Estimation](#token-estimation)
- [Model Selection](#model-selection)
- [Cost Optimization](#cost-optimization)
- [Evaluation Metrics](#evaluation-metrics)
- [Common Patterns](#common-patterns)
- [Troubleshooting](#troubleshooting)

---

## Prompt Patterns

### Basic Structure

```
[ROLE/PERSONA]
You are a [role] who [key trait]. Your goal is to [objective].

[CONTEXT]
Background information the model needs.

[TASK]
Specific instruction for what to do.

[FORMAT]
How to structure the output.

[CONSTRAINTS]
What NOT to do or boundaries to respect.
```

### System Prompt Template

```
You are [role] with expertise in [domain].

Your responsibilities:
- [Primary task]
- [Secondary task]

Guidelines:
- [Behavior 1]
- [Behavior 2]

Constraints:
- Never [prohibited action]
- Always [required action]

Output format: [format specification]
```

### Few-Shot Template

```
Here are examples of the task:

Example 1:
Input: [example input]
Output: [example output]

Example 2:
Input: [example input]
Output: [example output]

Now complete this:
Input: [actual input]
Output:
```

### Chain-of-Thought Triggers

| Trigger Phrase | Use Case |
|:---------------|:---------|
| "Let's think step by step" | General reasoning |
| "First, let's break this down" | Complex problems |
| "Walk through your reasoning" | Explanations needed |
| "Consider each option carefully" | Decision making |
| "Show your work" | Math/calculations |

### Output Format Specifiers

```markdown
# JSON
Respond in JSON format:
{"field1": "value", "field2": "value"}

# Markdown
Use markdown with headers and bullet points.

# XML
Wrap your response in <response></response> tags.

# Structured
Use this exact format:
ANALYSIS: [your analysis]
RECOMMENDATION: [your recommendation]
CONFIDENCE: [high/medium/low]
```

---

## API Parameters

### Temperature Guide

| Temperature | Behavior | Use Case |
|:------------|:---------|:---------|
| 0.0 | Deterministic | Factual Q&A, code, data extraction |
| 0.3 | Low variance | Technical writing, analysis |
| 0.7 | Balanced | General conversation, creative but grounded |
| 1.0 | High variance | Brainstorming, creative writing |
| 1.5+ | Very random | Experimental, often incoherent |

### Top-p (Nucleus Sampling)

| Top-p | Effect |
|:------|:-------|
| 0.1 | Very focused, limited vocabulary |
| 0.5 | Moderately diverse |
| 0.9 | Standard setting, good diversity |
| 1.0 | Consider all tokens |

### Common Parameter Combinations

| Task | Temperature | Top-p | Max Tokens |
|:-----|:------------|:------|:-----------|
| Code generation | 0.0-0.2 | 0.95 | 2000-4000 |
| Data extraction | 0.0 | 1.0 | 500-1000 |
| Summarization | 0.3 | 0.9 | 500-1500 |
| Creative writing | 0.8-1.0 | 0.95 | 2000+ |
| Chat/conversation | 0.7 | 0.9 | 500-1000 |
| Analysis/reasoning | 0.2-0.5 | 0.95 | 1000-2000 |

### Stop Sequences

```python
# Common stop sequences
stop_sequences = [
    "\n\n",           # Double newline
    "Human:",         # Conversation boundary
    "```",            # End of code block
    "</response>",    # XML tag closure
    "---",            # Section break
]
```

---

## Token Estimation

### Quick Rules of Thumb

| Content Type | Tokens per Unit |
|:-------------|:----------------|
| English text | ~0.75 tokens/word |
| Code | ~0.4 tokens/character |
| JSON | ~1.3 tokens/character |
| Non-English | 1.5-4x English |

### Estimation Formulas

```python
# English text
tokens ≈ words × 1.3
tokens ≈ characters / 4

# Code
tokens ≈ characters / 2.5

# Quick estimate
tokens ≈ len(text.split()) * 1.3
```

### Context Window Budgeting

```
Total Context = System Prompt + Conversation History + Retrieved Context + User Message + Output Buffer

Example for 128K context:
- System prompt: 2,000 tokens
- Conversation history: 10,000 tokens  
- Retrieved context (RAG): 50,000 tokens
- User message: 1,000 tokens
- Output buffer: 4,000 tokens
- Safety margin (10%): 12,800 tokens
─────────────────────────────────
Available for retrieval: ~48,200 tokens
```

### Model Context Limits (January 2026)

| Model | Context Window | Output Limit |
|:------|:---------------|:-------------|
| GPT-4 Turbo | 128K | 4K |
| GPT-4o | 128K | 16K |
| Claude 3.5 Sonnet | 200K | 8K |
| Claude 3 Opus | 200K | 4K |
| Gemini 1.5 Pro | 1M | 8K |
| Llama 3.1 405B | 128K | 4K |

---

## Model Selection

### Decision Matrix

| Need | Best Choice | Why |
|:-----|:------------|:----|
| Highest quality | Claude 3 Opus, GPT-4 | Best reasoning |
| Best value | Claude 3.5 Sonnet, GPT-4o | Quality/cost balance |
| Speed critical | Claude 3 Haiku, GPT-4o mini | Low latency |
| Long documents | Gemini 1.5 Pro | 1M context |
| Code generation | Claude 3.5 Sonnet | Best benchmarks |
| Self-hosted | Llama 3.1 70B | Open weights |
| Cost sensitive | Llama 3.1 8B, Mixtral | Free/cheap |

### Pricing Quick Reference (per 1M tokens, approximate)

| Model | Input | Output |
|:------|:------|:-------|
| GPT-4o | $2.50 | $10.00 |
| GPT-4o mini | $0.15 | $0.60 |
| Claude 3.5 Sonnet | $3.00 | $15.00 |
| Claude 3 Haiku | $0.25 | $1.25 |
| Gemini 1.5 Pro | $1.25 | $5.00 |
| Llama 3.1 (hosted) | $0.50-2.00 | $0.50-2.00 |

*Prices change frequently — verify current rates*

---

## Cost Optimization

### Strategies

| Strategy | Savings | Trade-off |
|:---------|:--------|:----------|
| Prompt caching | 50-90% | Cache invalidation |
| Smaller models for routing | 70-90% | Accuracy on complex tasks |
| Batch processing | 50% | Latency |
| Output length limits | Variable | May truncate |
| Semantic caching | 30-60% | Cache misses |

### Prompt Caching Pattern

```python
# Structure prompts with static content first
prompt = f"""
{STATIC_SYSTEM_PROMPT}      # Cached
{STATIC_EXAMPLES}           # Cached
{STATIC_INSTRUCTIONS}       # Cached
---
{dynamic_user_input}        # Not cached
"""
```

### Cost Estimation Formula

```python
cost = (input_tokens / 1_000_000 * input_price) + 
       (output_tokens / 1_000_000 * output_price)

# Example: GPT-4o, 2000 input, 500 output
cost = (2000 / 1_000_000 * 2.50) + (500 / 1_000_000 * 10.00)
cost = $0.005 + $0.005 = $0.01 per request
```

---

## Evaluation Metrics

### Classification Metrics (for LLM outputs)

| Metric | Formula | Use When |
|:-------|:--------|:---------|
| Accuracy | (TP + TN) / Total | Balanced classes |
| Precision | TP / (TP + FP) | False positives costly |
| Recall | TP / (TP + FN) | False negatives costly |
| F1 Score | 2 × (P × R) / (P + R) | Balance P and R |

### Generation Quality Metrics

| Metric | What It Measures | Range |
|:-------|:-----------------|:------|
| BLEU | N-gram overlap with reference | 0-1 (higher = better) |
| ROUGE | Recall of reference n-grams | 0-1 (higher = better) |
| Perplexity | Model confidence | Lower = better |
| BERTScore | Semantic similarity | 0-1 (higher = better) |

### RAG-Specific Metrics

| Metric | Formula | Target |
|:-------|:--------|:-------|
| Context Precision | Relevant chunks / Retrieved chunks | > 0.8 |
| Context Recall | Retrieved relevant / Total relevant | > 0.9 |
| Faithfulness | Claims supported by context / Total claims | > 0.95 |
| Answer Relevancy | Semantic similarity to question | > 0.8 |

### LLM-as-Judge Template

```
You are evaluating an AI response on a scale of 1-5.

Criteria:
- Accuracy: Is the information correct?
- Completeness: Does it fully address the question?
- Clarity: Is it well-organized and easy to understand?
- Relevance: Does it stay on topic?

Response to evaluate:
{response}

Original question:
{question}

Provide scores for each criterion and an overall score with brief justification.
```

---

## Common Patterns

### RAG Pattern

```python
# 1. Embed query
query_embedding = embed(user_query)

# 2. Retrieve relevant chunks
chunks = vector_db.search(query_embedding, top_k=5)

# 3. Construct prompt
prompt = f"""
Use the following context to answer the question.
If the context doesn't contain the answer, say so.

Context:
{format_chunks(chunks)}

Question: {user_query}

Answer:
"""

# 4. Generate response
response = llm.generate(prompt)
```

### ReAct Agent Pattern

```
Thought: I need to [reasoning about what to do]
Action: tool_name(param1="value1", param2="value2")
Observation: [result from tool]
Thought: Based on this, I should [next reasoning]
Action: another_tool(param="value")
Observation: [result]
Thought: I now have enough information
Answer: [final response to user]
```

### Tool Definition (OpenAI Format)

```python
tools = [{
    "type": "function",
    "function": {
        "name": "search_database",
        "description": "Search the product database for items",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query"
                },
                "category": {
                    "type": "string",
                    "enum": ["electronics", "clothing", "home"],
                    "description": "Product category filter"
                },
                "max_results": {
                    "type": "integer",
                    "default": 10
                }
            },
            "required": ["query"]
        }
    }
}]
```

### Retry with Exponential Backoff

```python
import time
import random

def call_with_retry(func, max_retries=5, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)
```

---

## Troubleshooting

### Common Issues and Fixes

| Problem | Likely Cause | Solution |
|:--------|:-------------|:---------|
| Repetitive output | Temperature too low | Increase temperature to 0.7+ |
| Nonsense/gibberish | Temperature too high | Decrease temperature to 0.3-0.5 |
| Ignores instructions | Prompt too long | Move key instructions to end |
| Wrong format | Unclear specification | Add explicit format example |
| Hallucinations | No grounding | Add RAG or fact-checking |
| Cuts off mid-response | max_tokens too low | Increase max_tokens |
| Rate limit errors | Too many requests | Add retry logic with backoff |
| Context overflow | Input too long | Summarize or chunk input |

### Prompt Debugging Checklist

```
□ Is the instruction clear and unambiguous?
□ Is there an example of the expected output?
□ Are constraints explicitly stated?
□ Is the most important instruction near the end?
□ Is the context relevant and not too long?
□ Are delimiters used to separate sections?
□ Is the output format specified?
□ Are edge cases addressed?
```

### Error Messages Quick Reference

| Error | Meaning | Fix |
|:------|:--------|:----|
| `context_length_exceeded` | Input + output > limit | Reduce input or max_tokens |
| `rate_limit_exceeded` | Too many requests | Add delays, use backoff |
| `invalid_api_key` | Auth failed | Check API key |
| `model_not_found` | Wrong model name | Verify model string |
| `content_filter` | Safety triggered | Rephrase request |

---

## Quick Reference Cards

### Prompt Engineering Principles

```
1. Be specific, not vague
2. Show, don't just tell (use examples)
3. Structure with clear sections
4. Put critical instructions last
5. Specify what NOT to do
6. Request step-by-step for complex tasks
7. Define output format explicitly
8. Test with edge cases
```

### Token-Saving Tips

```
1. Remove redundant phrases ("I want you to", "Please")
2. Use abbreviations in system prompts
3. Compress examples to minimum needed
4. Summarize conversation history
5. Use structured formats over prose
6. Cache static prompt components
```

---

### Notes

This cheat sheet is maintained for quick reference. For deeper explanations, see:
- [Deep Learning Guide](Deep_Learning_Guide.md) — Conceptual understanding
- [Advanced Prompting](Advanced_Prompting.md) — Detailed techniques
- [AI Tools](AI_Tools.md) — Tool recommendations

Feedback and suggestions are welcome!

*Last updated: January 2026*