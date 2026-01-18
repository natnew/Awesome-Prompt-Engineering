---
layout: default
title: Learning Resources
description: Guide to courses, books, and papers for AI practitioners.
nav_order: 10
---

[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Resources

A practitioner's guide to learning resources for building, deploying, evaluating, and governing AI systems. Organized by what you need to learn and why.

**This guide answers three questions for every resource:**
1. What skill or knowledge does this build?
2. Who needs this in a serious organization?
3. How does it connect to working with frontier AI systems?

> **Note:** For tools and software, see [AI Tools](AI_Tools.md). This page focuses on learning resources.

---

### Contents

- [Learning Paths by Role](#learning-paths-by-role)
- [Prompt Engineering & Context Design](#prompt-engineering--context-design)
- [Agent Development & Orchestration](#agent-development--orchestration)
- [RAG & Knowledge Systems](#rag--knowledge-systems)
- [Evaluation & Testing](#evaluation--testing)
- [AI Safety & Alignment](#ai-safety--alignment)
- [AI Governance & Ethics](#ai-governance--ethics)
- [LLM Foundations](#llm-foundations)
- [Classical ML & Deep Learning](#classical-ml--deep-learning)
- [Landmark Research Papers](#landmark-research-papers)
- [Communities & Discussion](#communities--discussion)
- [Podcasts & Video Channels](#podcasts--video-channels)
- [Conferences & Events](#conferences--events)
- [Newsletters & Blogs](#newsletters--blogs)

---

## Learning Paths by Role

*Where to start based on what you're trying to accomplish.*

| Role | Core Skills Needed | Start Here |
|:-----|:-------------------|:-----------|
| **AI Product Manager** | Prompt design, evaluation, user research, cost modeling | [Prompt Engineering](#prompt-engineering--context-design) → [Evaluation](#evaluation--testing) |
| **Software Engineer (adding AI)** | API integration, prompt engineering, error handling | [LLM Foundations](#llm-foundations) → [Prompt Engineering](#prompt-engineering--context-design) |
| **AI/ML Engineer** | Agent architecture, RAG systems, evaluation, deployment | [Agent Development](#agent-development--orchestration) → [RAG](#rag--knowledge-systems) |
| **Data Scientist** | Fine-tuning, embeddings, evaluation metrics | [LLM Foundations](#llm-foundations) → [Evaluation](#evaluation--testing) |
| **Security Engineer** | Prompt injection, guardrails, red teaming | [AI Safety](#ai-safety--alignment) → [Evaluation](#evaluation--testing) |
| **Compliance/Legal** | AI governance frameworks, risk assessment, audit | [AI Governance](#ai-governance--ethics) |
| **Executive/Decision Maker** | AI strategy, risk, organizational change | [AI Governance](#ai-governance--ethics) → AI for Everyone course |
| **Researcher** | Architecture, training, alignment theory | [Landmark Papers](#landmark-research-papers) → [Classical ML](#classical-ml--deep-learning) |

---

## Prompt Engineering & Context Design

*The core skill for working with LLMs. How to communicate effectively with AI systems.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **Anthropic Prompt Engineering Guide** | Claude-specific best practices, system prompts, XML tags | Developers using Claude | [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) |
| **OpenAI Prompt Engineering Guide** | GPT best practices, few-shot, chain-of-thought | Developers using OpenAI | [platform.openai.com/docs](https://platform.openai.com/docs/guides/prompt-engineering) |
| **Prompt Engineering Guide (DAIR.AI)** | Comprehensive techniques across models | All practitioners | [promptingguide.ai](https://www.promptingguide.ai/) |
| **Learn Prompting** | Structured course from basics to advanced | Beginners to intermediate | [learnprompting.org](https://learnprompting.org/) |
| **DeepLearning.AI: ChatGPT Prompt Engineering** | Practical prompt engineering with Andrew Ng | Developers, data scientists | [deeplearning.ai](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) |
| **Google Prompt Design Guide** | Gemini-specific prompting strategies | Developers using Google AI | [ai.google.dev](https://ai.google.dev/gemini-api/docs/prompting-intro) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **"Prompt Engineering" (Lilian Weng)** | Deep technical overview of prompting techniques | [lilianweng.github.io](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) |
| **"What We Learned from a Year of Building with LLMs"** | Production lessons from practitioners | [oreilly.com](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/) |
| **Anthropic's Claude Character** | How Claude is designed to behave and why | [anthropic.com](https://www.anthropic.com/research/claude-character) |

---

## Agent Development & Orchestration

*Building AI systems that reason, plan, and take actions. The frontier of applied AI.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **DeepLearning.AI: AI Agents in LangGraph** | Multi-step agents with state and cycles | AI engineers | [deeplearning.ai](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) |
| **DeepLearning.AI: Multi AI Agent Systems with CrewAI** | Role-based multi-agent collaboration | Teams building agent teams | [deeplearning.ai](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) |
| **LangChain Academy** | Comprehensive LangChain/LangGraph training | LangChain users | [academy.langchain.com](https://academy.langchain.com/) |
| **Anthropic MCP Documentation** | Building tool-using agents with Model Context Protocol | Agent developers | [modelcontextprotocol.io](https://modelcontextprotocol.io/introduction) |
| **AutoGen Tutorial** | Microsoft's multi-agent framework | Enterprise teams | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/docs/tutorial/) |
| **OpenAI Function Calling Guide** | Tool use and structured outputs | OpenAI API users | [platform.openai.com](https://platform.openai.com/docs/guides/function-calling) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **"The Shift from Models to Compound AI Systems"** | Why agents and pipelines matter more than models | [bair.berkeley.edu](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) |
| **"Building Effective Agents" (Anthropic)** | Practical patterns for agent development | [anthropic.com](https://www.anthropic.com/research/building-effective-agents) |
| **"Cognitive Architectures for Language Agents"** | Academic framework for agent design | [arxiv.org](https://arxiv.org/abs/2309.02427) |
| **LangGraph Conceptual Guide** | When and how to use agentic patterns | [langchain-ai.github.io](https://langchain-ai.github.io/langgraph/concepts/) |

---

## RAG & Knowledge Systems

*Connecting AI to your organization's data. Essential for enterprise AI.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **DeepLearning.AI: Building and Evaluating Advanced RAG** | Production RAG with evaluation | ML engineers | [deeplearning.ai](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) |
| **LlamaIndex Documentation** | Data connectors, indexing, retrieval | RAG developers | [docs.llamaindex.ai](https://docs.llamaindex.ai/) |
| **Pinecone Learning Center** | Vector search fundamentals and best practices | Teams implementing RAG | [pinecone.io/learn](https://www.pinecone.io/learn/) |
| **DeepLearning.AI: Vector Databases** | Embeddings and similarity search | Data engineers | [deeplearning.ai](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/) |
| **Weaviate Academy** | Hands-on vector database training | Weaviate users | [weaviate.io/developers/academy](https://weaviate.io/developers/academy) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **"Patterns for Building LLM-based Systems"** | RAG, agents, and production patterns | [eugeneyan.com](https://eugeneyan.com/writing/llm-patterns/) |
| **"Chunking Strategies for LLM Applications"** | How to split documents for retrieval | [pinecone.io](https://www.pinecone.io/learn/chunking-strategies/) |
| **"A Survey on RAG for LLMs"** | Comprehensive academic overview | [arxiv.org](https://arxiv.org/abs/2312.10997) |
| **"Retrieval Augmented Generation: A Practical Guide"** | End-to-end RAG implementation | [docs.cohere.com](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) |

---

## Evaluation & Testing

*Measuring AI quality. The difference between demos and production systems.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **DeepLearning.AI: Evaluating and Debugging Generative AI** | Systematic evaluation methods | ML engineers | [deeplearning.ai](https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai/) |
| **Promptfoo Documentation** | Automated prompt testing and red teaming | Developers testing prompts | [promptfoo.dev/docs](https://www.promptfoo.dev/docs/intro/) |
| **Inspect AI Documentation** | UK AISI's evaluation framework | Safety researchers, evaluators | [inspect.ai-safety-institute.org.uk](https://inspect.ai-safety-institute.org.uk/docs/) |
| **Ragas Documentation** | RAG-specific evaluation metrics | RAG developers | [docs.ragas.io](https://docs.ragas.io/) |
| **Braintrust Documentation** | Building evaluation pipelines | Production ML teams | [braintrust.dev/docs](https://www.braintrust.dev/docs) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **"Your AI Product Needs Evals"** | Why and how to evaluate LLM applications | [hamel.dev](https://hamel.dev/blog/posts/evals/) |
| **"How to Evaluate LLMs"** | Practical evaluation strategies | [oreilly.com](https://www.oreilly.com/radar/how-to-evaluate-llms-a-complete-metric-framework/) |
| **"LLM-as-Judge"** | Using LLMs to evaluate LLM outputs | [arxiv.org](https://arxiv.org/abs/2306.05685) |
| **Anthropic's Evaluation Documentation** | How Anthropic thinks about evals | [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests) |

---

## AI Safety & Alignment

*Building AI systems that are robust, secure, and aligned with human values.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **AISF Fundamentals Course** | AI safety foundations | Researchers, engineers | [aisafetyfundamentals.com](https://www.aisafetyfundamentals.com/) |
| **DeepLearning.AI: Red Teaming LLM Applications** | Adversarial testing techniques | Security engineers | [deeplearning.ai](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) |
| **Center for AI Safety Course** | Technical AI safety concepts | Researchers | [course.mlsafety.org](https://course.mlsafety.org/) |
| **Guardrails AI Documentation** | Implementing input/output validation | Developers adding safety | [guardrailsai.com/docs](https://www.guardrailsai.com/docs) |
| **NeMo Guardrails Guide** | NVIDIA's conversational safety toolkit | Chatbot developers | [docs.nvidia.com](https://docs.nvidia.com/nemo/guardrails/) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **Anthropic Core Views on AI Safety** | How Anthropic approaches safety | [anthropic.com](https://www.anthropic.com/news/core-views-on-ai-safety) |
| **"Constitutional AI" (Anthropic)** | Self-correction against principles | [anthropic.com](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) |
| **"Prompt Injection Primer"** | Understanding prompt injection attacks | [simonwillison.net](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) |
| **OWASP Top 10 for LLM Applications** | Security risks in LLM systems | [owasp.org](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| **"Sleeper Agents"** | Research on deceptive AI behavior | [arxiv.org](https://arxiv.org/abs/2401.05566) |
| **UK AISI Evaluations** | Government AI safety assessment approach | [aisi.gov.uk](https://www.aisi.gov.uk/our-work) |

---

## AI Governance & Ethics

*Managing AI at the organizational level. Policy, risk, compliance, and accountability.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **AI for Everyone (Andrew Ng)** | Non-technical AI literacy for leaders | Executives, managers | [coursera.org](https://www.coursera.org/learn/ai-for-everyone) |
| **Responsible AI (Google)** | Principles for ethical AI development | All practitioners | [ai.google/responsibility](https://ai.google/responsibility/responsible-ai-practices/) |
| **Microsoft Responsible AI** | Enterprise responsible AI framework | Enterprise teams | [microsoft.com/ai/responsible-ai](https://www.microsoft.com/en-us/ai/responsible-ai) |
| **AI Ethics (MIT)** | Technical and philosophical foundations | Researchers, policy makers | [mitsloan.mit.edu](https://exec.mit.edu/s/artificial-intelligence-implications-for-business-strategy) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **NIST AI Risk Management Framework** | US government AI risk framework | [nist.gov](https://www.nist.gov/itl/ai-risk-management-framework) |
| **EU AI Act Summary** | European AI regulation overview | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) |
| **"Model Cards for Model Reporting"** | Standardized model documentation | [arxiv.org](https://arxiv.org/abs/1810.03993) |
| **Anthropic's Responsible Scaling Policy** | How to scale AI development responsibly | [anthropic.com](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) |
| **"On the Dangers of Stochastic Parrots"** | Critical perspective on large language models | [dl.acm.org](https://dl.acm.org/doi/10.1145/3442188.3445922) |

---

## LLM Foundations

*Understanding how large language models work. Essential context for practitioners.*

### Courses & Tutorials

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **Andrej Karpathy: Neural Networks - Zero to Hero** | Build GPT from scratch | Engineers wanting deep understanding | [youtube.com](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) |
| **Stanford CS324: Large Language Models** | Academic LLM foundations | Researchers, advanced engineers | [stanford-cs324.github.io](https://stanford-cs324.github.io/winter2022/) |
| **Hugging Face NLP Course** | Transformers, fine-tuning, deployment | ML engineers | [huggingface.co/course](https://huggingface.co/learn/nlp-course) |
| **DeepLearning.AI: Generative AI with LLMs** | LLM architecture, training, fine-tuning | ML practitioners | [coursera.org](https://www.coursera.org/learn/generative-ai-with-llms) |
| **Full Stack LLM Bootcamp** | End-to-end LLM application development | Full-stack developers | [fullstackdeeplearning.com](https://fullstackdeeplearning.com/llm-bootcamp/) |
| **LLM University (Cohere)** | Embeddings, RAG, fine-tuning fundamentals | All practitioners | [cohere.com/llmu](https://cohere.com/llmu) |

### Key Reading

| Resource | What You'll Learn | Link |
|:---------|:------------------|:-----|
| **"The Illustrated Transformer"** | Visual guide to transformer architecture | [jalammar.github.io](https://jalammar.github.io/illustrated-transformer/) |
| **"Attention Is All You Need" Annotated** | The foundational paper, explained | [nlp.seas.harvard.edu](https://nlp.seas.harvard.edu/annotated-transformer/) |
| **"A Survey of Large Language Models"** | Comprehensive LLM overview | [arxiv.org](https://arxiv.org/abs/2303.18223) |
| **State of GPT (Andrej Karpathy)** | How GPT models are trained and used | [youtube.com](https://www.youtube.com/watch?v=bZQun8Y4L2A) |

---

## Classical ML & Deep Learning

*Foundational knowledge. Still relevant for understanding and when LLMs aren't the right tool.*

### Courses

| Resource | What You'll Learn | Who It's For | Link |
|:---------|:------------------|:-------------|:-----|
| **Machine Learning (Andrew Ng)** | ML fundamentals: regression, classification, neural nets | Beginners | [coursera.org](https://www.coursera.org/learn/machine-learning) |
| **Deep Learning Specialization** | Neural networks, CNNs, RNNs, sequence models | Engineers building models | [coursera.org](https://www.coursera.org/specializations/deep-learning) |
| **Fast.ai Practical Deep Learning** | Hands-on deep learning with code | Practitioners wanting fast results | [fast.ai](https://course.fast.ai/) |
| **CS231n: CNNs for Visual Recognition** | Computer vision foundations | Vision ML engineers | [cs231n.stanford.edu](http://cs231n.stanford.edu/) |
| **CS224n: NLP with Deep Learning** | NLP foundations (pre-LLM techniques still useful) | NLP engineers | [web.stanford.edu/class/cs224n](http://web.stanford.edu/class/cs224n/) |
| **Elements of AI** | Non-technical AI introduction | Everyone | [elementsofai.com](https://www.elementsofai.com/) |
| **StatQuest (Josh Starmer)** | Intuitive statistics and ML explanations | Visual learners | [youtube.com/statquest](https://www.youtube.com/@statquest) |

### Books

| Book | What You'll Learn | Who It's For | Link |
|:-----|:------------------|:-------------|:-----|
| **Deep Learning (Goodfellow et al.)** | Comprehensive deep learning theory | Researchers, advanced practitioners | [deeplearningbook.org](https://www.deeplearningbook.org/) |
| **Hands-On Machine Learning (Géron)** | Practical ML with scikit-learn, Keras, TensorFlow | Practitioners | [oreilly.com](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) |
| **The Hundred-Page Machine Learning Book** | Concise ML overview | Everyone needing quick reference | [themlbook.com](http://themlbook.com/) |
| **Designing Machine Learning Systems (Huyen)** | Production ML system design | ML engineers | [oreilly.com](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) |
| **AI Engineering (Huyen)** | Building AI products and systems | AI/ML engineers | [oreilly.com](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) |
| **Build a Large Language Model (From Scratch)** | Implement an LLM step by step | Engineers wanting deep understanding | [manning.com](https://www.manning.com/books/build-a-large-language-model-from-scratch) |

---

## Landmark Research Papers

*Essential papers for understanding how we got here and where we're going.*

### Foundational (Pre-2020)

| Paper | Year | Significance | Link |
|:------|:-----|:-------------|:-----|
| **Attention Is All You Need** | 2017 | Introduced the Transformer architecture | [arxiv.org](https://arxiv.org/abs/1706.03762) |
| **BERT** | 2018 | Bidirectional pre-training for NLP | [arxiv.org](https://arxiv.org/abs/1810.04805) |
| **GPT-2 (Language Models are Unsupervised Multitask Learners)** | 2019 | Scaling and emergence in language models | [openai.com](https://openai.com/research/better-language-models) |
| **ImageNet Classification with Deep CNNs (AlexNet)** | 2012 | Launched the deep learning revolution | [papers.nips.cc](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) |
| **Deep Residual Learning (ResNet)** | 2016 | Enabled very deep networks | [arxiv.org](https://arxiv.org/abs/1512.03385) |
| **Generative Adversarial Networks** | 2014 | Generative modeling breakthrough | [arxiv.org](https://arxiv.org/abs/1406.2661) |
| **Playing Atari with Deep RL** | 2013 | Deep reinforcement learning | [arxiv.org](https://arxiv.org/abs/1312.5602) |

### LLM Era (2020-2023)

| Paper | Year | Significance | Link |
|:------|:-----|:-------------|:-----|
| **GPT-3 (Language Models are Few-Shot Learners)** | 2020 | In-context learning at scale | [arxiv.org](https://arxiv.org/abs/2005.14165) |
| **Scaling Laws for Neural Language Models** | 2020 | Predictable scaling behavior | [arxiv.org](https://arxiv.org/abs/2001.08361) |
| **Training Compute-Optimal LLMs (Chinchilla)** | 2022 | Optimal data/compute tradeoffs | [arxiv.org](https://arxiv.org/abs/2203.15556) |
| **Chain-of-Thought Prompting** | 2022 | Reasoning through intermediate steps | [arxiv.org](https://arxiv.org/abs/2201.11903) |
| **Constitutional AI** | 2022 | AI self-improvement with principles | [arxiv.org](https://arxiv.org/abs/2212.08073) |
| **RLHF (Training Language Models to Follow Instructions)** | 2022 | Human feedback for alignment | [arxiv.org](https://arxiv.org/abs/2203.02155) |
| **LLaMA** | 2023 | Open-weight foundation models | [arxiv.org](https://arxiv.org/abs/2302.13971) |
| **GPT-4 Technical Report** | 2023 | Multimodal frontier model | [arxiv.org](https://arxiv.org/abs/2303.08774) |
| **Retrieval-Augmented Generation (RAG)** | 2020 | Grounding LLMs with retrieval | [arxiv.org](https://arxiv.org/abs/2005.11401) |
| **LoRA: Low-Rank Adaptation** | 2021 | Efficient fine-tuning | [arxiv.org](https://arxiv.org/abs/2106.09685) |

### Agents & Reasoning (2023-2025)

| Paper | Year | Significance | Link |
|:------|:-----|:-------------|:-----|
| **ReAct: Reasoning and Acting in LLMs** | 2023 | Foundation for LLM agents | [arxiv.org](https://arxiv.org/abs/2210.03629) |
| **Toolformer** | 2023 | LLMs learning to use tools | [arxiv.org](https://arxiv.org/abs/2302.04761) |
| **Tree of Thoughts** | 2023 | Structured reasoning exploration | [arxiv.org](https://arxiv.org/abs/2305.10601) |
| **Self-Consistency** | 2023 | Multiple reasoning paths for reliability | [arxiv.org](https://arxiv.org/abs/2203.11171) |
| **Voyager: Minecraft Agent** | 2023 | Lifelong learning agent | [arxiv.org](https://arxiv.org/abs/2305.16291) |
| **DSPy** | 2023 | Programming (not prompting) LLMs | [arxiv.org](https://arxiv.org/abs/2310.03714) |
| **GAIA Benchmark** | 2023 | Evaluating general AI assistants | [arxiv.org](https://arxiv.org/abs/2311.12983) |
| **Let's Verify Step by Step** | 2023 | Process reward models for reasoning | [arxiv.org](https://arxiv.org/abs/2305.20050) |
| **The Claude 3 Model Family** | 2024 | Frontier model capabilities and safety | [anthropic.com](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) |

### Safety & Alignment

| Paper | Year | Significance | Link |
|:------|:-----|:-------------|:-----|
| **Concrete Problems in AI Safety** | 2016 | Foundational safety research agenda | [arxiv.org](https://arxiv.org/abs/1606.06565) |
| **Scaling Monosemanticity** | 2023 | Interpreting neural network features | [anthropic.com](https://transformer-circuits.pub/2023/monosemantic-features/) |
| **Sleeper Agents** | 2024 | Deceptive behavior in AI systems | [arxiv.org](https://arxiv.org/abs/2401.05566) |
| **Many-Shot Jailbreaking** | 2024 | Long-context safety vulnerabilities | [anthropic.com](https://www.anthropic.com/research/many-shot-jailbreaking) |
| **Towards Monosemanticity** | 2023 | Understanding neural network internals | [anthropic.com](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning) |

---

## Communities & Discussion

*Where practitioners share knowledge, debug problems, and stay current.*

### Technical Communities

| Community | Focus | Who It's For | Link |
|:----------|:------|:-------------|:-----|
| **Hugging Face Hub** | Model sharing, datasets, discussions | ML practitioners | [huggingface.co](https://huggingface.co/) |
| **LangChain Discord** | LangChain/LangGraph development | LangChain users | [discord.gg/langchain](https://discord.gg/langchain) |
| **r/LocalLLaMA** | Running LLMs locally | Self-hosting enthusiasts | [reddit.com/r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) |
| **r/MachineLearning** | ML research and news | Researchers, practitioners | [reddit.com/r/MachineLearning](https://www.reddit.com/r/MachineLearning/) |
| **Anthropic Discord** | Claude development and usage | Claude users | [discord.gg/anthropic](https://discord.gg/anthropic) |
| **OpenAI Developer Forum** | OpenAI API development | OpenAI API users | [community.openai.com](https://community.openai.com/) |
| **AI Stack Exchange** | Technical Q&A | All practitioners | [ai.stackexchange.com](https://ai.stackexchange.com/) |
| **MLOps Community** | Production ML systems | MLOps engineers | [mlops.community](https://mlops.community/) |
| **Eleuther AI Discord** | Open-source AI research | Researchers, open-source contributors | [discord.gg/eleutherai](https://discord.gg/eleutherai) |

### Professional Networks

| Community | Focus | Who It's For | Link |
|:----------|:------|:-------------|:-----|
| **AI Engineer Foundation** | Applied AI engineering | Professional AI engineers | [ai.engineer](https://www.ai.engineer/) |
| **Weights & Biases Community** | ML experiment tracking | W&B users | [wandb.ai/community](https://wandb.ai/site/community) |
| **dbt Community** | Data transformation (AI-adjacent) | Data engineers | [getdbt.com/community](https://www.getdbt.com/community/) |

---

## Podcasts & Video Channels

*Stay current with developments and learn from practitioners.*

### Podcasts

| Podcast | Focus | Who It's For | Link |
|:--------|:------|:-------------|:-----|
| **Latent Space** | AI engineering deep dives | AI engineers, technical practitioners | [latent.space](https://www.latent.space/) |
| **Practical AI** | Applied AI and ML | Practitioners | [changelog.com/practicalai](https://changelog.com/practicalai) |
| **The Gradient Podcast** | AI research interviews | Researchers, curious practitioners | [thegradientpub.substack.com](https://thegradientpub.substack.com/) |
| **Machine Learning Street Talk** | Technical ML discussions | Advanced practitioners | [youtube.com/@MachineLearningStreetTalk](https://www.youtube.com/@MachineLearningStreetTalk) |
| **Lex Fridman Podcast** | Long-form AI researcher interviews | General audience | [lexfridman.com/podcast](https://lexfridman.com/podcast/) |
| **TWIML AI Podcast** | ML industry interviews | ML practitioners | [twimlai.com](https://twimlai.com/) |
| **Cognitive Revolution** | AI implications and applications | Leaders, strategists | [theaibreakdown.com](https://www.cognitiverevolution.ai/) |
| **High Agency** | AI product development | Product managers, founders | [highagency.substack.com](https://www.highagency.com/) |

### YouTube Channels

| Channel | Focus | Who It's For | Link |
|:--------|:------|:-------------|:-----|
| **Andrej Karpathy** | Deep understanding of neural networks | Engineers wanting fundamentals | [youtube.com/@AndrejKarpathy](https://www.youtube.com/@AndrejKarpathy) |
| **3Blue1Brown** | Visual math and ML explanations | Visual learners | [youtube.com/@3blue1brown](https://www.youtube.com/@3blue1brown) |
| **Yannic Kilcher** | Paper explanations and ML news | Researchers, practitioners | [youtube.com/@YannicKilcher](https://www.youtube.com/@YannicKilcher) |
| **Two Minute Papers** | Research paper summaries | Everyone | [youtube.com/@TwoMinutePapers](https://www.youtube.com/@TwoMinutePapers) |
| **AI Explained** | AI developments explained | General technical audience | [youtube.com/@AIExplained](https://www.youtube.com/@aiaboratorium7168) |
| **StatQuest** | Statistics and ML fundamentals | Beginners, visual learners | [youtube.com/@statquest](https://www.youtube.com/@statquest) |

---

## Conferences & Events

*Where the field advances and practitioners connect.*

### Major Research Conferences

| Conference | Focus | Link |
|:-----------|:------|:-----|
| **NeurIPS** | Machine learning and AI research | [neurips.cc](https://neurips.cc/) |
| **ICML** | Machine learning | [icml.cc](https://icml.cc/) |
| **ICLR** | Representation learning | [iclr.cc](https://iclr.cc/) |
| **ACL** | Natural language processing | [aclweb.org](https://aclweb.org/) |
| **CVPR** | Computer vision | [cvpr.thecvf.com](https://cvpr.thecvf.com/) |
| **AAAI** | Artificial intelligence | [aaai.org](https://aaai.org/) |
| **IJCAI** | Artificial intelligence | [ijcai.org](https://www.ijcai.org/) |

### Applied AI Events

| Event | Focus | Link |
|:------|:------|:-----|
| **AI Engineer World's Fair** | Applied AI engineering | [ai.engineer](https://www.ai.engineer/) |
| **AI Summit** | Enterprise AI | [theaisummit.com](https://theaisummit.com/) |
| **MLOps Community Events** | Production ML | [mlops.community/events](https://mlops.community/events/) |
| **LangChain Events** | LLM application development | [langchain.com/events](https://www.langchain.com/events) |

---

## Newsletters & Blogs

*Curated updates and analysis.*

### Newsletters

| Newsletter | Focus | Link |
|:-----------|:------|:-----|
| **The Batch (DeepLearning.AI)** | Weekly AI news digest | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch/) |
| **Import AI** | AI research and policy | [jack-clark.net](https://jack-clark.net/) |
| **The Gradient** | AI research summaries | [thegradient.pub](https://thegradient.pub/) |
| **AI Tidbits** | Curated AI developments | [aitechtidbits.substack.com](https://aitidbits.substack.com/) |
| **Ahead of AI** | LLM research and applications | [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/) |
| **Interconnects** | AI research analysis | [interconnects.ai](https://www.interconnects.ai/) |
| **Simon Willison's Weblog** | LLM applications and tools | [simonwillison.net](https://simonwillison.net/) |

### Company Research Blogs

| Blog | Focus | Link |
|:-----|:------|:-----|
| **Anthropic Research** | Claude and AI safety research | [anthropic.com/research](https://www.anthropic.com/research) |
| **OpenAI Research** | GPT and capabilities research | [openai.com/research](https://openai.com/research) |
| **Google DeepMind** | Frontier AI research | [deepmind.google/research](https://deepmind.google/research/) |
| **Meta AI Research** | Open AI research | [ai.meta.com/research](https://ai.meta.com/research/) |
| **Hugging Face Blog** | Open-source ML | [huggingface.co/blog](https://huggingface.co/blog) |

### Individual Blogs

| Blog | Focus | Link |
|:-----|:------|:-----|
| **Lilian Weng** | Technical AI explainers | [lilianweng.github.io](https://lilianweng.github.io/) |
| **Jay Alammar** | Visual ML explanations | [jalammar.github.io](https://jalammar.github.io/) |
| **Eugene Yan** | Applied ML systems | [eugeneyan.com](https://eugeneyan.com/) |
| **Chip Huyen** | ML systems and engineering | [huyenchip.com](https://huyenchip.com/blog/) |
| **Hamel Husain** | LLM applications and evals | [hamel.dev](https://hamel.dev/) |
| **Sebastian Raschka** | ML fundamentals and LLMs | [sebastianraschka.com](https://sebastianraschka.com/blog/) |

---

## The Integration Challenge

> **Companies will not struggle to access AI.**  
> **They will struggle to integrate, trust, measure, and govern it under pressure.**

This is why resources on **Evaluation**, **Safety**, and **Governance** matter as much as resources on building. The practitioners who succeed will be those who invest in:

1. **Systematic evaluation** before deployment
2. **Safety engineering** as a core competency
3. **Governance frameworks** that scale with AI adoption
4. **Continuous learning** as the field evolves rapidly

---

### Notes

Feedback and suggestions are welcome!

This list is maintained as part of the [Awesome Prompt Engineering](https://natnew.github.io/Awesome-Prompt-Engineering/) collection. For tools and software, see [AI Tools](AI_Tools.md).

*Last updated: January 2026*