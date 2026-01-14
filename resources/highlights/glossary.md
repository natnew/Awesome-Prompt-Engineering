# Glossary

Key terms used throughout this curriculum.

---

## A

**Agent**  
An AI system that can take actions in an environment, often using tools and making decisions autonomously. Agents typically follow patterns like ReAct (Reasoning + Acting).

**Alignment**  
Ensuring AI systems behave in accordance with human intentions and values. A system is "aligned" when it does what we actually want, not just what we literally asked.

**Attention Mechanism**  
The core innovation in transformer models. Allows the model to weigh the importance of different parts of the input when generating each output token.

---

## B

**Baseline**  
A reference point for comparison. In evaluation, the baseline is the simplest reasonable approach, against which improvements are measured.

**BLEU Score**  
Bilingual Evaluation Understudy. An automatic metric measuring n-gram overlap between generated and reference text. Useful but limited.

---

## C

**Chain-of-Thought (CoT)**  
A prompting technique where the model is asked to show reasoning steps before giving a final answer. Often improves accuracy on complex tasks.

**Circuit Breaker**  
A design pattern that automatically stops operations when failure thresholds are exceeded, preventing cascade failures.

**Context Window**  
The maximum number of tokens a model can process in a single request. Includes both input and output tokens.

**Constitutional AI**  
A training approach where the model is given principles (a "constitution") and learns to self-critique and revise outputs to align with those principles.

---

## D

**Defense in Depth**  
A security pattern using multiple independent safety layers, each assuming others might fail.

**Deterministic**  
Producing the same output for the same input every time. LLMs are non-deterministic by default due to sampling.

---

## E

**Embedding**  
A numerical vector representation of text (or other data). Embeddings capture semantic meaning and enable similarity search.

**Evaluation (Eval)**  
The process of measuring AI system quality against defined criteria. Can be automatic, human, or hybrid.

---

## F

**Few-Shot Learning**  
Providing examples in the prompt to teach the model a pattern or format. "Few-shot" typically means 2-5 examples.

**Fine-Tuning**  
Additional training on a pre-trained model to specialize it for specific tasks or domains.

**Faithfulness**  
In RAG systems, whether the generated answer is supported by the retrieved documents. High faithfulness = no hallucination beyond sources.

---

## G

**Guardrail**  
A safety constraint that limits AI system behavior. Can operate on input, processing, or output.

**Grounding**  
Connecting AI outputs to verifiable sources. RAG is a grounding technique—answers are grounded in retrieved documents.

---

## H

**Hallucination**  
When a model generates false information presented as fact. A fundamental LLM failure mode.

**Human-in-the-Loop (HITL)**  
System design where humans review or approve AI decisions at strategic points.

---

## I

**In-Context Learning**  
The ability of LLMs to learn patterns from examples provided in the prompt, without weight updates.

**Inference**  
Running a trained model to generate outputs. Distinct from training.

---

## J

**Jailbreak**  
Techniques to bypass safety guidelines in AI models, often through creative prompting.

---

## L

**LLM (Large Language Model)**  
Neural networks trained on large text corpora to predict and generate text. Examples: GPT-4, Claude, Llama.

**Latency**  
Time from request to response. Often measured as p50 (median), p95, p99 percentiles.

---

## M

**Model Provider**  
Company providing LLM access via API. Examples: Anthropic, OpenAI, Google.

---

## N

**N-gram**  
A contiguous sequence of N tokens. Used in some evaluation metrics.

---

## P

**Prompt**  
The input text sent to an LLM. Includes system prompts (instructions) and user prompts (the actual request).

**Prompt Injection**  
An attack where malicious instructions in user input attempt to override system instructions.

**Pre-training**  
Initial training of an LLM on large text corpora. Creates the base model that is later fine-tuned.

---

## R

**RAG (Retrieval-Augmented Generation)**  
Architecture that retrieves relevant documents and includes them in context before generation. Reduces hallucination and enables up-to-date responses.

**RLHF (Reinforcement Learning from Human Feedback)**  
Training technique where human preferences guide model improvement. Key to making LLMs helpful and safe.

**ReAct**  
Reasoning + Acting. An agent pattern where the model alternates between reasoning about what to do and taking actions.

**Recall**  
In retrieval, the fraction of relevant documents that were retrieved. High recall = finding everything relevant.

**Relevance**  
How well output addresses what was actually asked. A key quality dimension.

---

## S

**System Prompt**  
Instructions that set model behavior, persona, and constraints. Typically hidden from end users.

**Sampling**  
The process of selecting tokens during generation. Temperature controls sampling randomness.

**Sycophancy**  
When models agree with users even when they're wrong. A known LLM failure mode.

---

## T

**Temperature**  
Parameter controlling randomness in token selection. Lower = more deterministic; higher = more random.

**Token**  
The basic unit of text processing for LLMs. Roughly 4 characters or 0.75 words in English.

**Transformer**  
The neural network architecture underlying modern LLMs. Introduced in "Attention Is All You Need" (2017).

**Tool Use**  
LLM capability to call external functions or APIs. Enables actions beyond text generation.

---

## V

**Vector Database**  
Database optimized for storing and searching embeddings. Used in RAG systems.

---

## Z

**Zero-Shot**  
Asking a model to perform a task without providing examples. Relies on pre-training knowledge.

---

*See also: [How LLMs Work](../foundations/how_llms_work.md), [Tokens and Context](../foundations/tokens_and_context.md)*
