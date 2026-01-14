[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../COMPETENCIES.md) | [Projects](../projects/00_overview.md) | [Patterns](../patterns/README.md) | [Templates](../templates/README.md) | [Foundations](../foundations/README.md)

# Resources

Curated references for going deeper. Quality over quantity.

---

## How to Use This Section

These resources supplement the curriculum. They're organized by topic and annotated with:

- **Difficulty:** Beginner / Intermediate / Advanced
- **Time:** Estimated reading/watching time
- **Why it's here:** What you'll gain

Start with resources marked 🌟 — these are particularly high-value.

---

## Quick Links by Need

| I want to... | Go to |
|:-------------|:------|
| Understand how LLMs work | [Technical Foundations](#technical-foundations) |
| Write better prompts | [Prompt Engineering](#prompt-engineering) |
| Evaluate AI systems | [Evaluation & Testing](#evaluation--testing) |
| Build safer AI | [Safety & Alignment](#safety--alignment) |
| Design AI systems | [System Design](#system-design) |
| Keep up with the field | [Staying Current](#staying-current) |
| Find tools | [Tools & Libraries](#tools--libraries) |

---

## Technical Foundations

Understanding how LLMs work under the hood.

### For Beginners

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [What Is ChatGPT Doing?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) | Article | 45 min | Stephen Wolfram's accessible explanation |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Article | 30 min | Visual guide to transformer architecture |
| [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Video | 1 hr | Excellent visual intuition builder |

### For Intermediate

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Paper | 2 hr | The transformer paper. Dense but foundational |
| [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) | Tutorial | 3 hr | Line-by-line implementation walkthrough |
| [Andrej Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | Video | 2 hr | Build a small GPT from scratch |

### For Advanced

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | Paper | 1 hr | How model size affects capability |
| [Training Compute-Optimal LLMs](https://arxiv.org/abs/2203.15556) | Paper | 1 hr | Chinchilla scaling laws |
| [Andrej Karpathy: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Course | 20 hr | Full deep learning from scratch |

---

## Prompt Engineering

Practical techniques for getting better outputs.

### Guides & Tutorials

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Docs | 2 hr | Official guide, excellent |
| 🌟 [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Docs | 1 hr | Official OpenAI guidance |
| [Learn Prompting](https://learnprompting.org/) | Course | 5 hr | Comprehensive free course |
| [Prompt Engineering Guide](https://www.promptingguide.ai/) | Guide | 3 hr | Community-maintained reference |

### Research Papers

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Paper | 30 min | Step-by-step reasoning technique |
| [Self-Consistency](https://arxiv.org/abs/2203.11171) | Paper | 30 min | Sample multiple reasoning paths |
| [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Paper | 45 min | Structured reasoning exploration |
| [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629) | Paper | 45 min | Foundation for agent architectures |

### Advanced Techniques

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | Paper | 1 hr | Self-improvement through principles |
| [Prompt Injection Defenses](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) | Article | 20 min | Simon Willison's practical guide |

---

## Evaluation & Testing

Measuring and validating AI system quality.

### Frameworks & Methods

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [RAGAS: RAG Evaluation](https://docs.ragas.io/) | Docs | 1 hr | Framework for RAG evaluation |
| [DeepEval](https://docs.confident-ai.com/) | Docs | 1 hr | LLM evaluation framework |
| [LangSmith Evaluation](https://docs.smith.langchain.com/) | Docs | 1 hr | LangChain's evaluation tools |
| [OpenAI Evals](https://github.com/openai/evals) | Repo | 2 hr | OpenAI's evaluation framework |

### Research

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) | Paper | 45 min | Using LLMs to evaluate LLMs |
| [HELM Benchmark](https://crfm.stanford.edu/helm/) | Benchmark | 1 hr | Holistic evaluation of language models |
| [BIG-bench](https://github.com/google/BIG-bench) | Benchmark | 1 hr | Diverse capability benchmark |

### Practical Guides

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| [Evaluating LLM Applications](https://hamel.dev/blog/posts/evals/) | Article | 30 min | Hamel Husain's practical guide |
| [A Guide to LLM Evaluation](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation) | Article | 20 min | Metrics overview |

---

## Safety & Alignment

Building AI systems that behave as intended.

### Introductory

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Anthropic Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) | Article | 20 min | Anthropic's safety philosophy |
| [Introduction to AI Safety](https://aisafetyfundamentals.com/) | Course | 10 hr | Comprehensive introduction |
| [AI Alignment Forum](https://www.alignmentforum.org/) | Forum | Ongoing | Research discussion community |

### Security

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Guide | 1 hr | Security risks and mitigations |
| [Prompt Injection](https://simonwillison.net/series/prompt-injection/) | Articles | 2 hr | Simon Willison's comprehensive series |
| [LLM Security](https://llmsecurity.net/) | Collection | 2 hr | Curated security resources |

### Research

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Constitutional AI](https://arxiv.org/abs/2212.08073) | Paper | 1 hr | Training AI with principles |
| [RLHF](https://arxiv.org/abs/2203.02155) | Paper | 1 hr | Training LLMs with human feedback |
| [Sleeper Agents](https://arxiv.org/abs/2401.05566) | Paper | 1 hr | Hidden model behaviors |
| [Representation Engineering](https://arxiv.org/abs/2310.01405) | Paper | 1 hr | Controlling model behavior |

### Interpretability

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Anthropic Interpretability Research](https://www.anthropic.com/research#702702) | Articles | 3 hr | Leading interpretability work |
| [Transformer Circuits](https://transformer-circuits.pub/) | Articles | 5 hr | Deep dives into model internals |
| [Neel Nanda's Tutorials](https://www.neelnanda.io/mechanistic-interpretability/getting-started) | Tutorials | 10 hr | Hands-on interpretability |

---

## System Design

Building production AI systems.

### Architecture

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Building LLM Applications](https://www.oreilly.com/library/view/building-llm-apps/9781835462317/) | Book | 10 hr | Comprehensive system design |
| [Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) | Article | 30 min | Eugene Yan's patterns catalog |
| [What We've Learned From A Year of Building with LLMs](https://www.oreilly.com/radar/what-weve-learned-from-a-year-of-building-with-llms-part-i/) | Article | 45 min | Hard-won lessons |

### RAG Systems

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) | Videos | 5 hr | LangChain's comprehensive series |
| [Advanced RAG Techniques](https://www.pinecone.io/learn/advanced-rag-techniques/) | Guide | 1 hr | Beyond basic RAG |
| [Retrieval Augmented Generation](https://arxiv.org/abs/2005.11401) | Paper | 45 min | Original RAG paper |

### Agents

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| 🌟 [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | Article | 30 min | Anthropic's agent guidance |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Docs | 3 hr | Framework for agent workflows |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Repo | 2 hr | Autonomous agent reference |

### Operations

| Resource | Type | Time | Notes |
|:---------|:-----|:-----|:------|
| [LLMOps](https://fullstackdeeplearning.com/llm-bootcamp/) | Course | 10 hr | Full Stack Deep Learning |
| [Monitoring LLM Applications](https://www.honeycomb.io/blog/monitoring-llm-applications) | Article | 20 min | Observability guidance |

---

## Tools & Libraries

Practical tools for building AI systems.

### Frameworks

| Tool | Purpose | Notes |
|:-----|:--------|:------|
| [LangChain](https://python.langchain.com/) | LLM application framework | Most popular, comprehensive |
| [LlamaIndex](https://docs.llamaindex.ai/) | Data framework for LLMs | Strong RAG focus |
| [Haystack](https://haystack.deepset.ai/) | NLP framework | Production-oriented |
| [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) | Microsoft's LLM framework | Enterprise focus |

### Evaluation

| Tool | Purpose | Notes |
|:-----|:--------|:------|
| [RAGAS](https://docs.ragas.io/) | RAG evaluation | Standard metrics |
| [DeepEval](https://docs.confident-ai.com/) | LLM testing | Unit testing for LLMs |
| [Promptfoo](https://promptfoo.dev/) | Prompt testing | CLI-based evaluation |
| [Weights & Biases](https://wandb.ai/) | Experiment tracking | ML lifecycle |

### Vector Databases

| Tool | Purpose | Notes |
|:-----|:--------|:------|
| [Pinecone](https://www.pinecone.io/) | Managed vector DB | Easy to start |
| [Weaviate](https://weaviate.io/) | Open-source vector DB | Full-featured |
| [Chroma](https://www.trychroma.com/) | Lightweight vector DB | Good for prototypes |
| [Qdrant](https://qdrant.tech/) | Vector search engine | High performance |

### Monitoring & Observability

| Tool | Purpose | Notes |
|:-----|:--------|:------|
| [LangSmith](https://smith.langchain.com/) | LLM tracing | LangChain ecosystem |
| [Weights & Biases Prompts](https://wandb.ai/site/prompts) | Prompt tracking | Experiment management |
| [Helicone](https://www.helicone.ai/) | LLM observability | Request logging |
| [Arize Phoenix](https://phoenix.arize.com/) | LLM observability | Open source |

### Security

| Tool | Purpose | Notes |
|:-----|:--------|:------|
| [Rebuff](https://github.com/protectai/rebuff) | Prompt injection detection | Open source |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Programmable guardrails | NVIDIA |
| [Guardrails AI](https://www.guardrailsai.com/) | Output validation | Structured outputs |

---

## Staying Current

The field moves fast. These help you keep up.

### Newsletters

| Newsletter | Frequency | Notes |
|:-----------|:----------|:------|
| 🌟 [The Batch](https://www.deeplearning.ai/the-batch/) | Weekly | Andrew Ng's newsletter |
| [Import AI](https://importai.substack.com/) | Weekly | Jack Clark's analysis |
| [The Gradient](https://thegradient.pub/) | Weekly | Research summaries |
| [AI Weekly](https://aiweekly.co/) | Weekly | Curated links |

### Podcasts

| Podcast | Notes |
|:--------|:------|
| [Latent Space](https://www.latent.space/podcast) | Technical depth, practitioner focus |
| [Practical AI](https://changelog.com/practicalai) | Applied AI |
| [The Gradient Podcast](https://thegradientpub.substack.com/s/podcast) | Research interviews |
| [TWIML AI](https://twimlai.com/) | Interviews with researchers |

### Blogs to Follow

| Blog | Author | Focus |
|:-----|:-------|:------|
| 🌟 [Simon Willison](https://simonwillison.net/) | Simon Willison | LLMs, practical |
| [Lilian Weng](https://lilianweng.github.io/) | Lilian Weng | Research summaries |
| [Eugene Yan](https://eugeneyan.com/) | Eugene Yan | Applied ML |
| [Chip Huyen](https://huyenchip.com/blog/) | Chip Huyen | MLOps |
| [Hamel Husain](https://hamel.dev/) | Hamel Husain | LLM engineering |

### Research Sources

| Source | Notes |
|:-------|:------|
| [arXiv cs.CL](https://arxiv.org/list/cs.CL/recent) | NLP papers |
| [arXiv cs.AI](https://arxiv.org/list/cs.AI/recent) | AI papers |
| [Papers With Code](https://paperswithcode.com/) | Papers + implementations |
| [Semantic Scholar](https://www.semanticscholar.org/) | Paper search |

---

## Books

For deeper study.

| Book | Author | Level | Notes |
|:-----|:-------|:------|:------|
| 🌟 [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) | Chip Huyen | Intermediate | System design |
| [Natural Language Processing with Transformers](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) | Tunstall et al. | Intermediate | Hands-on NLP |
| [Deep Learning](https://www.deeplearningbook.org/) | Goodfellow et al. | Advanced | Foundational theory |
| [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) | Jurafsky & Martin | Advanced | NLP textbook (free) |

---

## Contributing

Found a great resource? Contributions welcome:

1. Must be high-quality and relevant
2. Include difficulty level and time estimate
3. Explain why it's valuable
4. Check that links work

---

*Last updated: January 2025*
