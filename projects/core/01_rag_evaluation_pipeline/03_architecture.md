[← Back: Success Metrics](02_success_metrics.md) | [Next: Evaluation Suite →](04_evaluation_suite.md)

# Module 3: Architecture

Make design decisions explicit and document your trade-offs.

---

## The Core Principle

**Every architectural decision is a trade-off.**

There are no "best practices" that apply universally. There are only decisions that make sense given your constraints — or don't.

This module teaches you to:
- Identify the decisions you're making (even implicit ones)
- Consider alternatives seriously
- Document trade-offs explicitly
- Produce an Architecture Decision Record (ADR)

---

## RAG Architecture: The Decisions

A RAG system involves many decisions. Here are the ones that matter most:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Documents → [CHUNKING] → Chunks → [EMBEDDING] → Vectors        │
│                                                                 │
│  Query → [EMBEDDING] → Vector → [RETRIEVAL] → Top-K Chunks      │
│                                                                 │
│  Query + Chunks → [GENERATION] → Answer                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Decision 1: Chunking Strategy

How do you split documents into retrievable pieces?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **Fixed size** (e.g., 500 tokens) | Simple, predictable | Breaks semantic units |
| **Semantic** (paragraphs, sections) | Preserves meaning | Variable sizes, complex |
| **Sentence-level** | Fine-grained | Too small for context |
| **Hierarchical** (parent-child) | Best of both | Complex to implement |
| **Sliding window** | Captures boundaries | Redundant storage |

**Questions to answer:**
- What's the typical structure of your documents?
- How long are meaningful semantic units?
- How much context does the LLM need to answer well?

### Decision 2: Embedding Model

What model converts text to vectors?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **OpenAI ada-002** | Easy, good quality | Cost, vendor lock-in |
| **OpenAI text-embedding-3-small/large** | Better quality, dimensions | Cost |
| **Cohere embed** | Good multilingual | Another vendor |
| **Open source** (e5, bge, etc.) | Free, self-hosted | Operational overhead |
| **Fine-tuned** | Domain-specific | Requires data, expertise |

**Questions to answer:**
- What's your budget for embeddings?
- Do you need multilingual support?
- Is self-hosting feasible?
- Do you have data to fine-tune?

### Decision 3: Vector Store

Where do you store and search embeddings?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **Pinecone** | Managed, scalable | Cost, vendor lock-in |
| **Weaviate** | Feature-rich, hybrid search | Complexity |
| **Qdrant** | Fast, self-hostable | Operational overhead |
| **Chroma** | Simple, local-first | Less scalable |
| **pgvector** | PostgreSQL integration | Performance limits |
| **FAISS** | Fast, local | No persistence by default |

**Questions to answer:**
- How many vectors?
- What latency do you need?
- Managed vs. self-hosted?
- Do you need hybrid (vector + keyword) search?

### Decision 4: Retrieval Strategy

How do you find relevant chunks?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **Pure vector similarity** | Simple | Misses keyword matches |
| **Hybrid (vector + BM25)** | Better recall | More complex |
| **Reranking** | Better precision | Additional latency, cost |
| **Query expansion** | Better recall | Can add noise |
| **Multi-query** | Handles ambiguity | Multiple retrievals |

**Questions to answer:**
- How important is keyword matching?
- Can you afford reranking latency?
- How often are queries ambiguous?

### Decision 5: Generation Model

What model produces the final answer?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **GPT-4o** | High quality | Cost |
| **GPT-4o-mini** | Good quality, cheaper | Slightly lower quality |
| **Claude 3.5 Sonnet** | High quality, good at instructions | Cost |
| **Claude 3.5 Haiku** | Fast, cheap | Lower quality |
| **Open source** (Llama, Mistral) | Free, self-hosted | Quality varies, overhead |

**Questions to answer:**
- What quality level do you need?
- What's your latency budget?
- What's your cost budget?
- Are there compliance requirements?

### Decision 6: Context Assembly

How do you present retrieved chunks to the LLM?

| Option | Pros | Cons |
|:-------|:-----|:-----|
| **Simple concatenation** | Easy | May confuse model |
| **Structured (with sources)** | Better attribution | More tokens |
| **Summarized** | Fits more info | Lossy |
| **Filtered by relevance** | Higher signal | May miss info |

**Questions to answer:**
- How many chunks fit in your context window?
- How important is source attribution?
- Can the model handle long contexts well?

---

## Making Decisions: A Framework

For each decision, work through:

### 1. State the Decision

What exactly are you deciding?

### 2. Identify Options

What are the realistic alternatives? (Not all possible options — the ones worth considering.)

### 3. Define Criteria

What matters for this decision?
- Cost
- Latency
- Quality
- Complexity
- Maintenance
- Vendor lock-in
- Team expertise

### 4. Evaluate Options

How does each option perform on your criteria?

### 5. Make the Call

Choose an option and document why.

### 6. Note What Could Change This

Under what circumstances would you revisit this decision?

---

## Your Task: Document Your Architecture

Complete an Architecture Decision Record for at least **three** key decisions.

Use the template in `artifacts/adr_template.md`.

### Minimum Required Decisions

1. **Chunking strategy** — How you split documents
2. **Embedding model** — What model you use for vectors
3. **Generation model** — What model produces answers

### Additional Decisions (If Time Permits)

4. Vector store selection
5. Retrieval strategy
6. Context assembly approach

---

## Example ADR: Chunking Strategy

Here's what a completed ADR looks like:

---

### ADR-001: Chunking Strategy

**Status:** Accepted

**Context:**
We need to split ~500 pages of documentation into chunks for retrieval. Documents include user guides (narrative), API docs (structured), and troubleshooting guides (Q&A format).

**Decision:**
Use **semantic chunking by section** with a maximum size of 1000 tokens and a minimum of 200 tokens.

**Alternatives Considered:**

| Option | Evaluation |
|:-------|:-----------|
| Fixed 500 tokens | Would break mid-sentence/paragraph. Simple but loses meaning. |
| Paragraph-level | Too granular. Many paragraphs lack sufficient context. |
| Document-level | Too large. Would exceed context windows and reduce precision. |
| Semantic by section | Preserves document structure. Sections are natural units. |

**Rationale:**
- Documentation has clear section structure (headers)
- Sections are typically self-contained
- 1000 token max ensures fit in context window (allows 5+ chunks)
- 200 token min ensures meaningful content

**Consequences:**
- Need section detection logic (using headers)
- Some sections will be split if >1000 tokens
- Very short sections may need to be combined with neighbors

**What Would Change This:**
- If retrieval precision is poor, may need finer granularity
- If context is often incomplete, may need larger chunks or parent-child approach

---

## Architecture Diagram

Sketch your architecture. It doesn't need to be pretty — it needs to be clear.

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR ARCHITECTURE                        │
│                                                                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐      │
│  │         │    │         │    │         │    │         │      │
│  │  Docs   │───▶│ Chunker │───▶│Embedder │───▶│ Vector  │      │
│  │         │    │         │    │         │    │   DB    │      │
│  └─────────┘    └─────────┘    └─────────┘    └────┬────┘      │
│                                                     │           │
│                                                     │           │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐         │           │
│  │         │    │         │    │         │         │           │
│  │  Query  │───▶│Embedder │───▶│Retriever│◀────────┘           │
│  │         │    │         │    │         │                      │
│  └─────────┘    └─────────┘    └────┬────┘                      │
│                                      │                          │
│                                      ▼                          │
│                               ┌─────────┐                       │
│                               │         │                       │
│                               │Generator│───▶ Answer            │
│                               │         │                       │
│                               └─────────┘                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Fill in:
- Specific tools/models for each component
- Key parameters (chunk size, top-k, model name)
- Data flow with volumes (docs/day, queries/day)

---

## Cost Estimation (Preview)

As you make decisions, start thinking about costs:

| Component | Cost Driver | Rough Estimate |
|:----------|:------------|:---------------|
| Embedding (indexing) | Tokens embedded | $ per 1M tokens |
| Embedding (query) | Queries × query length | $ per query |
| Vector storage | Vectors stored | $ per GB/month |
| Vector search | Queries | $ per 1M queries |
| Generation | Input + output tokens | $ per query |

We'll build a full cost model in Module 5.

---

## Checkpoint

### You Should Now Have

- [ ] At least 3 Architecture Decision Records completed
- [ ] An architecture diagram with specific components
- [ ] Understanding of trade-offs you've made

### You Should Be Able To Answer

- Why did you choose your chunking strategy?
- What would make you change your embedding model?
- What are the cost implications of your generation model choice?

---

[← Back: Success Metrics](02_success_metrics.md) | [Next: Evaluation Suite →](04_evaluation_suite.md)
