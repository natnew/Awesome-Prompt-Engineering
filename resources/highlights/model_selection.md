# Model Selection Guide

Practical guidance for choosing the right model for your use case.

*Note: This field moves fast. Verify current capabilities and pricing before making decisions.*

---

## Decision Framework

### Step 1: Define Requirements

| Question | Why It Matters |
|:---------|:---------------|
| What task type? | Models have different strengths |
| What quality bar? | Determines model tier needed |
| What latency requirement? | Smaller models are faster |
| What cost constraint? | Pricing varies 100x between models |
| What context length? | Limits which models work |
| What privacy requirements? | May require self-hosted |

### Step 2: Match to Model Tier

| Tier | Best For | Examples |
|:-----|:---------|:---------|
| Frontier | Complex reasoning, nuanced tasks | Claude 3.5 Opus, GPT-4o |
| Standard | General tasks, good balance | Claude 3.5 Sonnet, GPT-4o-mini |
| Fast/Cheap | High volume, simpler tasks | Claude Haiku, GPT-3.5 |
| Specialized | Specific domains | Code models, embedding models |
| Open Source | Privacy, customization | Llama, Mistral, Qwen |

### Step 3: Test and Validate

Never choose based on benchmarks alone. Test with YOUR data on YOUR tasks.

---

## Model Comparison by Capability

### General Reasoning

| Model | Strength | Consideration |
|:------|:---------|:--------------|
| Claude 3.5 Sonnet | Nuanced reasoning, long context | Excellent all-rounder |
| GPT-4o | Broad capabilities, multimodal | Strong ecosystem |
| Gemini 1.5 Pro | Very long context (1M+) | Good for document processing |

### Code Generation

| Model | Strength | Consideration |
|:------|:---------|:--------------|
| Claude 3.5 Sonnet | Strong code understanding | Good at explaining |
| GPT-4o | Broad language support | Strong ecosystem |
| DeepSeek Coder | Code-specialized | Open weights available |
| Codestral | Code-focused | Mistral's code model |

### Long Context

| Model | Context Window | Notes |
|:------|:---------------|:------|
| Gemini 1.5 Pro | 1M+ tokens | Best for massive documents |
| Claude 3.5 | 200K tokens | Strong recall |
| GPT-4o | 128K tokens | Good balance |

### Cost Efficiency

For high-volume, simpler tasks:

| Model | Relative Cost | Best For |
|:------|:--------------|:---------|
| Claude Haiku | $ | Classification, extraction |
| GPT-3.5 Turbo | $ | Simple generation |
| GPT-4o-mini | $$ | Balance of capability/cost |
| Mistral Small | $ | Self-hostable option |

---

## Model Comparison by Use Case

### Customer Support Bot

| Priority | Recommended | Why |
|:---------|:------------|:----|
| Quality first | Claude 3.5 Sonnet | Nuanced, helpful responses |
| Cost first | Claude Haiku | Good enough, much cheaper |
| Latency first | Claude Haiku | Fastest response |

### Document Analysis

| Priority | Recommended | Why |
|:---------|:------------|:----|
| Very long docs | Gemini 1.5 Pro | 1M token context |
| Quality analysis | Claude 3.5 Sonnet | Strong reasoning |
| High volume | GPT-4o-mini | Good balance |

### Code Assistant

| Priority | Recommended | Why |
|:---------|:------------|:----|
| Complex code | Claude 3.5 Sonnet or GPT-4o | Best reasoning |
| Simple tasks | DeepSeek Coder, Codestral | Cheaper, specialized |
| Privacy required | Open source code models | Self-hosted |

### Creative Writing

| Priority | Recommended | Why |
|:---------|:------------|:----|
| Quality | Claude 3.5 Sonnet | Nuanced, creative |
| Style control | GPT-4o | Good instruction following |
| Experimental | Higher temperature settings | More variation |

### Data Extraction

| Priority | Recommended | Why |
|:---------|:------------|:----|
| Structured output | Claude or GPT-4o | Reliable JSON |
| High volume | Claude Haiku, GPT-3.5 | Cost efficient |
| Complex schemas | Frontier models | Better reasoning |

---

## Self-Hosted vs. API

### When to Use APIs

- Getting started quickly
- Variable/unpredictable load
- Wanting latest capabilities
- Limited ML infrastructure

### When to Self-Host

- Strict data privacy requirements
- Predictable high volume (cost savings)
- Need for customization
- Regulatory requirements
- Offline/air-gapped environments

### Popular Open Models

| Model | Parameters | Notes |
|:------|:-----------|:------|
| Llama 3 | 8B, 70B | Meta's open model |
| Mistral | 7B, 8x7B | Strong efficiency |
| Qwen 2 | Various | Alibaba's model |
| Phi-3 | 3.8B, 14B | Microsoft, compact |

---

## Cost Optimization Strategies

### 1. Right-Size Your Model

Don't use GPT-4 for tasks GPT-3.5 can handle. Test to find the minimum viable model.

### 2. Prompt Efficiency

Shorter prompts = lower cost. Remove unnecessary verbosity.

### 3. Caching

Cache responses for repeated queries. Many providers offer prompt caching.

### 4. Batching

Batch requests where possible. Often cheaper than real-time.

### 5. Output Length Limits

Set max_tokens appropriately. Don't generate more than needed.

### 6. Model Routing

Use different models for different query types:
- Simple queries → Cheap model
- Complex queries → Capable model

---

## Evaluation Before Commitment

### Minimum Evaluation

1. Test with 50+ representative examples
2. Measure key quality metrics
3. Check latency distribution
4. Calculate cost at expected volume

### Comparison Template

| Metric | Model A | Model B | Model C |
|:-------|:--------|:--------|:--------|
| Accuracy | | | |
| Latency p50 | | | |
| Latency p95 | | | |
| Cost per 1K | | | |
| Context limit | | | |
| Failure rate | | | |

### Red Flags

- Dramatically different behavior on similar inputs
- Frequent refusals on legitimate requests
- Inconsistent formatting
- High variance in quality

---

## Staying Current

Model capabilities change rapidly. To stay informed:

1. **Follow provider blogs** — Announcements of new capabilities
2. **Track benchmarks** — [LMSYS Chatbot Arena](https://chat.lmsys.org/), [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
3. **Test regularly** — Re-evaluate when new models release
4. **Monitor costs** — Pricing changes, new tiers appear

---

## Summary

1. **Define requirements first** — Task, quality, latency, cost, context
2. **Match to model tier** — Don't over-spec or under-spec
3. **Test with your data** — Benchmarks lie; your use case matters
4. **Consider trade-offs** — Capability vs. cost vs. latency
5. **Stay flexible** — The best model today may not be best tomorrow

---

*See also: [How LLMs Work](../foundations/how_llms_work.md), [Tokens and Context](../foundations/tokens_and_context.md)*

*Last updated: January 2025. Verify current capabilities and pricing.*
