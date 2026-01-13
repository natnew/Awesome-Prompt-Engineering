[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Deep Learning for LLMs

A practitioner's guide to the deep learning concepts that power large language models. This isn't a comprehensive ML course — it's the specific knowledge you need to understand, use, and troubleshoot LLM systems.

---

### Contents

- [Why This Matters](#why-this-matters)
- [Core Concepts](#core-concepts)
- [The Transformer Architecture](#the-transformer-architecture)
- [Training & Optimization](#training--optimization)
- [Tokenization & Embeddings](#tokenization--embeddings)
- [Scaling & Emergence](#scaling--emergence)
- [Alignment & Safety](#alignment--safety)
- [Inference & Deployment](#inference--deployment)
- [Fine-Tuning & Adaptation](#fine-tuning--adaptation)

---

## Why This Matters

You don't need to train your own LLM to benefit from understanding how they work. This knowledge helps you:

- **Debug unexpected behavior** — Why is it generating nonsense? (temperature, tokenization)
- **Optimize costs** — Why are some prompts expensive? (token count, context length)
- **Choose models wisely** — What's the difference between Claude and GPT? (architecture, training)
- **Design better prompts** — Why does chain-of-thought work? (attention patterns, reasoning)
- **Anticipate limitations** — Why does it hallucinate? (training data, probability)

---

## Core Concepts

<details>
<summary><b>Neural Network</b></summary>

A computational system inspired by biological neurons. Consists of layers of connected nodes that transform input data through weighted connections and activation functions.

**LLM relevance:** LLMs are massive neural networks (billions of parameters) that learn to predict the next token from vast amounts of text.

```
Input → [Layer 1] → [Layer 2] → ... → [Layer N] → Output
           ↓           ↓                  ↓
        weights     weights            weights
```

</details>

<details>
<summary><b>Parameters</b></summary>

The learnable values in a neural network — the weights and biases that are adjusted during training. Model size is often described by parameter count.

**LLM relevance:** 
- GPT-3: 175B parameters
- GPT-4: ~1.8T parameters (estimated)
- Claude 3 Opus: ~200B+ parameters (estimated)
- Llama 3.1: 405B parameters

More parameters generally means more capacity to learn, but also more compute and cost.

</details>

<details>
<summary><b>Loss Function</b></summary>

A mathematical function that measures how wrong the model's predictions are. Training minimizes this loss.

**LLM relevance:** LLMs typically use **cross-entropy loss** — measuring how different the model's predicted probability distribution is from the actual next token. Lower loss = better predictions.

</details>

<details>
<summary><b>Gradient Descent</b></summary>

The optimization algorithm that adjusts parameters to minimize loss. Computes the gradient (direction of steepest increase) and moves parameters in the opposite direction.

**LLM relevance:** Training LLMs requires distributed gradient descent across thousands of GPUs, with sophisticated techniques like gradient accumulation and mixed precision.

</details>

<details>
<summary><b>Backpropagation</b></summary>

The algorithm for computing gradients efficiently by propagating error backwards through the network. Essential for training deep networks.

**LLM relevance:** Enables training of transformer models with hundreds of layers. The chain rule applied recursively through attention mechanisms.

</details>

<details>
<summary><b>Overfitting</b></summary>

When a model memorizes training data instead of learning generalizable patterns. Performs well on training data but poorly on new data.

**LLM relevance:** LLMs can memorize training text verbatim (copyright concerns). Regularization and diverse training data help prevent this.

</details>

---

## The Transformer Architecture

The architecture behind all modern LLMs.

<details>
<summary><b>Transformer</b></summary>

The neural network architecture introduced in "Attention Is All You Need" (2017). Uses self-attention instead of recurrence to process sequences.

**Key innovation:** Processes all tokens in parallel, enabling efficient training on long sequences and massive parallelism on GPUs.

```
Input Tokens → [Embedding] → [Transformer Blocks × N] → [Output Head] → Predictions
                                      ↓
                              [Self-Attention]
                              [Feed-Forward]
                              [Layer Norm]
```

</details>

<details>
<summary><b>Self-Attention</b></summary>

The mechanism that allows each token to "attend to" (consider relationships with) every other token in the sequence.

**How it works:**
1. Each token creates Query (Q), Key (K), and Value (V) vectors
2. Attention scores = softmax(Q × K^T / √d)
3. Output = weighted sum of Values based on attention scores

**LLM relevance:** This is why LLMs understand context — attention allows "it" to connect to "the cat" across many tokens.

```
"The cat sat on the mat. It was comfortable."
                              ↑
                    Attention connects "It" to "cat"
```

</details>

<details>
<summary><b>Multi-Head Attention</b></summary>

Running multiple attention mechanisms in parallel, each learning different relationship types.

**LLM relevance:** Different heads might learn syntax, semantics, coreference, etc. GPT-3 has 96 attention heads per layer.

</details>

<details>
<summary><b>Context Window / Context Length</b></summary>

The maximum number of tokens the model can process in a single forward pass. Determines how much information the model can "see" at once.

**Current limits:**
- GPT-4 Turbo: 128K tokens
- Claude 3: 200K tokens
- Gemini 1.5 Pro: 1M tokens

**LLM relevance:** Longer context = more information available, but quadratic memory cost with standard attention.

</details>

<details>
<summary><b>Positional Encoding</b></summary>

Information added to token embeddings to convey position in the sequence. Without this, transformers wouldn't know word order.

**Types:**
- **Absolute:** Fixed position encodings (original transformer)
- **Relative:** Encode distance between tokens
- **RoPE:** Rotary position embeddings (used by Llama, modern models)

**LLM relevance:** RoPE enables better generalization to longer sequences than seen in training.

</details>

<details>
<summary><b>Feed-Forward Network (FFN)</b></summary>

Dense layers applied to each token position after attention. Where much of the "knowledge" is stored.

**LLM relevance:** Recent research suggests FFN layers store factual knowledge, while attention handles reasoning patterns.

</details>

<details>
<summary><b>Layer Normalization</b></summary>

Normalizes activations across features to stabilize training. Applied before or after attention and FFN.

**LLM relevance:** Essential for training very deep transformer models (100+ layers).

</details>

---

## Training & Optimization

<details>
<summary><b>Pre-training</b></summary>

Training a model on vast amounts of unlabeled text to learn general language patterns. The foundation of all modern LLMs.

**Objective:** Predict the next token (causal language modeling) or masked tokens (BERT-style).

**Scale:** GPT-4 reportedly trained on trillions of tokens from the internet, books, code.

</details>

<details>
<summary><b>Fine-tuning</b></summary>

Additional training on a smaller, task-specific dataset to specialize a pre-trained model.

**Types:**
- **Full fine-tuning:** Update all parameters
- **LoRA/QLoRA:** Update only small adapter layers
- **Instruction tuning:** Train on instruction-following examples

</details>

<details>
<summary><b>RLHF (Reinforcement Learning from Human Feedback)</b></summary>

Training technique that aligns models with human preferences. Uses human ratings to train a reward model, then optimizes the LLM to maximize that reward.

**Process:**
1. Collect human comparisons of model outputs
2. Train a reward model on these preferences
3. Fine-tune LLM using PPO to maximize reward

**LLM relevance:** This is what makes ChatGPT/Claude helpful rather than just completing text. Critical for safety and alignment.

</details>

<details>
<summary><b>Constitutional AI</b></summary>

Anthropic's approach to alignment. Model critiques its own outputs against a set of principles and revises accordingly.

**LLM relevance:** How Claude is trained to be helpful, harmless, and honest without as much human labeling.

</details>

<details>
<summary><b>Learning Rate</b></summary>

How much to adjust parameters in response to gradients. Too high = unstable training; too low = slow learning.

**LLM relevance:** LLM training uses careful learning rate schedules — warmup, then decay. Critical hyperparameter.

</details>

<details>
<summary><b>Batch Size</b></summary>

Number of examples processed before updating parameters. Larger batches = more stable gradients, more memory.

**LLM relevance:** LLMs use huge effective batch sizes (millions of tokens) through gradient accumulation across many GPUs.

</details>

---

## Tokenization & Embeddings

<details>
<summary><b>Token</b></summary>

The basic unit of text that LLMs process. Not words — typically subword units that balance vocabulary size and sequence length.

**Examples:**
- "unhappiness" → ["un", "happiness"] or ["un", "hap", "pi", "ness"]
- "ChatGPT" → ["Chat", "G", "PT"]
- Spaces often included: " the" is one token

**LLM relevance:** Token count determines cost and context usage. Code/non-English text often uses more tokens per character.

</details>

<details>
<summary><b>Tokenizer</b></summary>

The algorithm that converts text to tokens and back. Different models use different tokenizers.

**Common types:**
- **BPE (Byte Pair Encoding):** GPT models
- **SentencePiece:** Llama, many open models
- **Tiktoken:** OpenAI's fast BPE implementation

**LLM relevance:** Same text = different token counts across models. Tokenizer determines vocabulary and edge cases.

</details>

<details>
<summary><b>Embedding</b></summary>

Dense vector representation of a token. Maps discrete tokens to continuous space where similar meanings are nearby.

**LLM relevance:** 
- Input: Tokens → Embeddings (lookup table)
- Output: Embeddings → Probabilities (linear layer)

Embeddings are how models represent meaning mathematically.

</details>

<details>
<summary><b>Vocabulary Size</b></summary>

The number of unique tokens the model knows. Larger vocabulary = more tokens but shorter sequences.

**Typical sizes:**
- GPT-4: ~100K tokens
- Claude: ~100K tokens
- Llama 3: 128K tokens

</details>

---

## Scaling & Emergence

<details>
<summary><b>Scaling Laws</b></summary>

Empirical observations that model performance improves predictably with more compute, data, and parameters.

**Key insight:** Performance follows power laws. 10× more compute ≈ predictable improvement.

**LLM relevance:** This is why labs keep building bigger models — returns remain positive at massive scale.

</details>

<details>
<summary><b>Emergent Capabilities</b></summary>

Abilities that appear suddenly at certain scales, not present in smaller models.

**Examples:**
- Chain-of-thought reasoning
- In-context learning
- Code generation
- Multilingual transfer

**LLM relevance:** You can't predict what a larger model will be able to do from smaller model behavior.

</details>

<details>
<summary><b>In-Context Learning</b></summary>

The ability to learn new tasks from examples in the prompt without weight updates. One of GPT-3's breakthrough capabilities.

**LLM relevance:** This is why few-shot prompting works. The model "learns" from examples in context, not through training.

</details>

<details>
<summary><b>Mixture of Experts (MoE)</b></summary>

Architecture where only a subset of parameters activates for each input. Enables larger models with lower compute.

**Examples:** GPT-4 (rumored), Mixtral, DBRX

**LLM relevance:** MoE models can be much larger but similar cost per token.

</details>

---

## Alignment & Safety

<details>
<summary><b>Alignment</b></summary>

Ensuring AI systems pursue goals that match human intentions. The challenge of making AI do what we actually want.

**Approaches:**
- RLHF
- Constitutional AI
- Debate
- Interpretability

</details>

<details>
<summary><b>Hallucination</b></summary>

When models generate plausible-sounding but factually incorrect information. A fundamental limitation of current LLMs.

**Why it happens:** Models optimize for plausibility (matching training distribution), not truth. No built-in fact-checking.

**Mitigations:** RAG, grounding, verification, citations.

</details>

<details>
<summary><b>Jailbreaking</b></summary>

Techniques to bypass safety measures and elicit restricted outputs from aligned models.

**Types:**
- Prompt injection
- Many-shot attacks
- Persona manipulation
- Encoding tricks

</details>

<details>
<summary><b>Red Teaming</b></summary>

Systematic adversarial testing to find model vulnerabilities before deployment.

**LLM relevance:** Essential practice before launching LLM applications. Find failures before users do.

</details>

---

## Inference & Deployment

<details>
<summary><b>Inference</b></summary>

Running a trained model to generate predictions. What happens when you send a prompt to an API.

**Cost factors:**
- Input tokens (processed in parallel)
- Output tokens (generated sequentially)
- Model size
- Hardware (GPU type)

</details>

<details>
<summary><b>Temperature</b></summary>

Parameter controlling randomness in token selection. Applied to logits before sampling.

**Values:**
- 0.0: Deterministic (always pick highest probability)
- 0.7: Balanced creativity
- 1.0+: More random, potentially incoherent

**LLM relevance:** Low temperature for factual tasks, higher for creative tasks.

</details>

<details>
<summary><b>Top-p (Nucleus Sampling)</b></summary>

Sample from the smallest set of tokens whose cumulative probability exceeds p. Alternative to temperature.

**Example:** top_p=0.9 means sample from tokens comprising top 90% of probability mass.

</details>

<details>
<summary><b>Top-k Sampling</b></summary>

Sample only from the k most likely tokens. Simple alternative to top-p.

**LLM relevance:** Often used with temperature for controlled randomness.

</details>

<details>
<summary><b>Logits</b></summary>

Raw, unnormalized scores output by the model before softmax. Higher logit = higher probability after normalization.

**LLM relevance:** Temperature operates on logits. Some APIs expose log-probabilities for analysis.

</details>

<details>
<summary><b>Quantization</b></summary>

Reducing numerical precision of model weights (e.g., 32-bit → 8-bit or 4-bit) to reduce memory and increase speed.

**Trade-off:** Smaller/faster but slight quality loss.

**LLM relevance:** Enables running large models on consumer hardware. Llama 3 70B runs on a single GPU with 4-bit quantization.

</details>

<details>
<summary><b>KV Cache</b></summary>

Caching key-value pairs from previous tokens to avoid recomputation during autoregressive generation.

**LLM relevance:** Essential optimization for inference. Why "prefill" is faster than generation.

</details>

---

## Fine-Tuning & Adaptation

<details>
<summary><b>LoRA (Low-Rank Adaptation)</b></summary>

Efficient fine-tuning method that adds small trainable matrices to frozen model weights. Dramatically reduces compute and memory.

**LLM relevance:** Makes fine-tuning accessible without massive GPU clusters. Can create custom models affordably.

</details>

<details>
<summary><b>QLoRA</b></summary>

Combines LoRA with quantization for even more efficient fine-tuning. Fine-tune 65B models on a single GPU.

</details>

<details>
<summary><b>Instruction Tuning</b></summary>

Fine-tuning on (instruction, response) pairs to make models follow instructions better.

**Datasets:** FLAN, Alpaca, OpenAssistant, Dolly

**LLM relevance:** Why "base" models just complete text while "instruct" models follow instructions.

</details>

<details>
<summary><b>Preference Tuning (DPO)</b></summary>

Direct Preference Optimization — alternative to RLHF that directly optimizes on preference data without a reward model.

**LLM relevance:** Simpler, more stable than RLHF. Used in recent open models.

</details>

---

## Quick Reference

### Model Size & Capability

| Parameters | Example Models | Typical Use |
|:-----------|:---------------|:------------|
| 1-7B | Llama 3.2, Phi-3 | Local deployment, edge |
| 7-13B | Llama 3.1 8B, Mistral 7B | Balanced cost/capability |
| 30-70B | Llama 3.1 70B, Mixtral 8x22B | High capability, self-hosted |
| 100B+ | GPT-4, Claude 3 Opus | Frontier capabilities |

### Inference Parameters Cheat Sheet

| Parameter | Low Value | High Value | Use Case |
|:----------|:----------|:-----------|:---------|
| Temperature | 0.0-0.3 | 0.7-1.0 | Factual → Creative |
| Top-p | 0.1-0.5 | 0.9-1.0 | Focused → Diverse |
| Max tokens | Task-dependent | — | Control output length |

---

### Notes

This guide focuses on concepts relevant to LLM practitioners. For comprehensive deep learning education, see [Resources](Resources.md).

Feedback and suggestions are welcome!

*Last updated: January 2026*