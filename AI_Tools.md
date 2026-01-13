[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## AI Tools

A practitioner's guide to tools for building, deploying, evaluating, monitoring, and governing AI systems. Organized by what problem each tool solves and who uses it.

**This guide answers three questions for every tool:**
1. What real problem does this solve?
2. Who uses it in a serious organization?
3. How does it connect to frontier AI systems?

---

### Contents

- [Foundation Models & APIs](#foundation-models--apis)
- [Development Frameworks](#development-frameworks)
- [Agent Orchestration](#agent-orchestration)
- [Prompt Management & Versioning](#prompt-management--versioning)
- [RAG & Knowledge Infrastructure](#rag--knowledge-infrastructure)
- [Evaluation & Testing](#evaluation--testing)
- [Observability & Monitoring](#observability--monitoring)
- [Safety & Guardrails](#safety--guardrails)
- [Deployment & MLOps](#deployment--mlops)
- [Governance & Compliance](#governance--compliance)
- [No-Code & Business Platforms](#no-code--business-platforms)
- [Data & Compute Infrastructure](#data--compute-infrastructure)
- [Research & Learning](#research--learning)

---

## Foundation Models & APIs

*The AI systems themselves. These are what you're integrating, not building.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **OpenAI API** | Access to GPT-4, GPT-4o, o1, o3 models for text, vision, and reasoning | Developers, product teams | [platform.openai.com](https://platform.openai.com/) |
| **Anthropic API** | Access to Claude models with strong instruction-following and safety | Developers, enterprise teams | [anthropic.com](https://www.anthropic.com/api) |
| **Google Vertex AI** | Unified access to Gemini models with enterprise security | Enterprise ML teams, GCP users | [cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai) |
| **Amazon Bedrock** | Single API to multiple foundation models (Claude, Llama, Titan) | AWS enterprise customers | [aws.amazon.com/bedrock](https://aws.amazon.com/bedrock/) |
| **Azure OpenAI Service** | OpenAI models with enterprise compliance and data residency | Enterprise teams on Azure | [azure.microsoft.com/products/ai-services/openai-service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) |
| **Mistral AI** | Open-weight and commercial models, EU-based | Teams needing EU data sovereignty | [mistral.ai](https://mistral.ai/) |
| **Cohere** | Enterprise LLMs optimized for RAG and search | Enterprise search teams | [cohere.com](https://cohere.com/) |
| **Groq** | Ultra-fast inference for open models (Llama, Mixtral) | Latency-sensitive applications | [groq.com](https://groq.com/) |
| **Together AI** | Inference and fine-tuning for 100+ open models | Teams using open-source models | [together.ai](https://www.together.ai/) |
| **Replicate** | Run open-source models via API without infrastructure | Prototypers, small teams | [replicate.com](https://replicate.com/) |
| **Fireworks AI** | Fast, cost-efficient inference for open models | Production teams optimizing cost | [fireworks.ai](https://fireworks.ai/) |

---

## Development Frameworks

*Libraries and SDKs for building AI-powered applications.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **LangChain** | Composable framework for LLM applications (chains, agents, RAG) | AI engineers, backend developers | [langchain.com](https://www.langchain.com/) |
| **LlamaIndex** | Data framework for connecting LLMs to external data sources | Developers building RAG systems | [llamaindex.ai](https://www.llamaindex.ai/) |
| **Haystack** | End-to-end framework for search and RAG pipelines | Search/NLP engineers | [haystack.deepset.ai](https://haystack.deepset.ai/) |
| **Semantic Kernel** | Microsoft's SDK for AI orchestration (.NET, Python, Java) | Enterprise .NET developers | [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) |
| **DSPy** | Programming framework that compiles prompts from examples | ML researchers, prompt optimizers | [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |
| **Instructor** | Structured outputs from LLMs with Pydantic validation | Developers needing reliable JSON | [github.com/jxnl/instructor](https://github.com/jxnl/instructor) |
| **Marvin** | Lightweight AI functions for Python applications | Python developers | [askmarvin.ai](https://www.askmarvin.ai/) |
| **Guidance** | Constrained generation with templates and grammars | Developers needing precise control | [github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance) |
| **Outlines** | Structured text generation with guaranteed JSON/regex output | Production ML engineers | [github.com/outlines-dev/outlines](https://github.com/outlines-dev/outlines) |
| **Vercel AI SDK** | React/Next.js SDK for streaming AI chat interfaces | Frontend developers | [sdk.vercel.ai](https://sdk.vercel.ai/) |

---

## Agent Orchestration

*Frameworks for building autonomous AI agents that reason, plan, and use tools.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **LangGraph** | Build stateful, multi-step agent workflows with cycles | AI engineers building complex agents | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) |
| **CrewAI** | Multi-agent collaboration with role-based agents | Teams building agent teams | [crewai.com](https://www.crewai.com/) |
| **AutoGen** | Microsoft's framework for multi-agent conversations | Researchers, enterprise teams | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) |
| **OpenAI Agents SDK** | Build agents with OpenAI's native tooling | OpenAI API users | [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python) |
| **Anthropic MCP** | Model Context Protocol for standardized tool integration | Developers building tool-using agents | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |
| **Letta (MemGPT)** | Agents with persistent memory and self-editing | Long-running agent applications | [letta.com](https://www.letta.com/) |
| **Agency Swarm** | Framework for creating collaborative agent swarms | Agent developers | [github.com/VRSEN/agency-swarm](https://github.com/VRSEN/agency-swarm) |
| **Composio** | 150+ tool integrations for AI agents (GitHub, Slack, etc.) | Agent builders needing integrations | [composio.dev](https://composio.dev/) |
| **Agentops** | Agent observability and debugging | Teams debugging agent behavior | [agentops.ai](https://www.agentops.ai/) |

---

## Prompt Management & Versioning

*Track, version, test, and optimize prompts as engineering artifacts.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Langfuse** | Open-source LLM observability, prompt management, evals | ML teams wanting self-hosted option | [langfuse.com](https://langfuse.com/) |
| **PromptLayer** | Prompt versioning, A/B testing, and analytics | Product teams iterating on prompts | [promptlayer.com](https://www.promptlayer.com/) |
| **Humanloop** | Prompt management with evaluation and fine-tuning | Enterprise AI product teams | [humanloop.com](https://humanloop.com/) |
| **Agenta** | Open-source prompt engineering and LLMOps platform | Teams wanting prompt CI/CD | [agenta.ai](https://www.agenta.ai/) |
| **Helicone** | LLM observability with cost tracking and caching | Teams monitoring API spend | [helicone.ai](https://www.helicone.ai/) |
| **Pezzo** | Open-source AI development toolkit | DevOps teams managing prompts | [pezzo.ai](https://www.pezzo.ai/) |
| **Portkey** | AI gateway with prompt management and fallbacks | Production teams needing reliability | [portkey.ai](https://portkey.ai/) |
| **Keywords AI** | Unified LLM API with built-in prompt management | Startups, small teams | [keywordsai.co](https://www.keywordsai.co/) |

---

## RAG & Knowledge Infrastructure

*Connect AI to your organization's data. Vector databases, embeddings, and retrieval.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Pinecone** | Managed vector database for production RAG | Teams needing managed vector search | [pinecone.io](https://www.pinecone.io/) |
| **Weaviate** | Open-source vector database with hybrid search | Teams wanting self-hosted vectors | [weaviate.io](https://weaviate.io/) |
| **Chroma** | Lightweight, open-source embedding database | Prototypers, small projects | [trychroma.com](https://www.trychroma.com/) |
| **Qdrant** | High-performance vector database (Rust-based) | Performance-critical applications | [qdrant.tech](https://qdrant.tech/) |
| **Milvus** | Scalable open-source vector database | Large-scale enterprise deployments | [milvus.io](https://milvus.io/) |
| **pgvector** | Vector similarity search in PostgreSQL | Teams already using PostgreSQL | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| **LanceDB** | Serverless vector database for multimodal data | Edge/embedded applications | [lancedb.com](https://lancedb.com/) |
| **Voyage AI** | High-quality embeddings for enterprise RAG | Teams needing better retrieval | [voyageai.com](https://www.voyageai.com/) |
| **Cohere Embed** | Multilingual embeddings optimized for search | Global enterprise search | [cohere.com/embed](https://cohere.com/embed) |
| **Unstructured** | ETL for documents (PDF, DOCX, HTML) into LLM-ready chunks | Data engineers building RAG | [unstructured.io](https://unstructured.io/) |
| **Docling** | IBM's document understanding for RAG pipelines | Enterprise document processing | [github.com/DS4SD/docling](https://github.com/DS4SD/docling) |

---

## Evaluation & Testing

*Measure AI quality, catch regressions, and ensure reliability before deployment.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Promptfoo** | Open-source prompt testing and red-teaming | Developers testing prompt changes | [promptfoo.dev](https://www.promptfoo.dev/) |
| **Inspect AI** | UK AISI's framework for rigorous AI evaluations | Safety researchers, evaluators | [inspect.ai-safety-institute.org.uk](https://inspect.ai-safety-institute.org.uk/) |
| **Braintrust** | End-to-end evaluation platform with datasets and scoring | ML teams building eval pipelines | [braintrust.dev](https://www.braintrust.dev/) |
| **Ragas** | Evaluation framework specifically for RAG systems | RAG developers | [ragas.io](https://ragas.io/) |
| **DeepEval** | Unit testing framework for LLM outputs | Developers wanting pytest-style evals | [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval) |
| **TruLens** | Evaluation and tracking for LLM applications | Teams debugging RAG quality | [trulens.org](https://www.trulens.org/) |
| **Weave** | Weights & Biases tool for LLM evaluation and tracing | W&B users, ML teams | [wandb.ai/site/weave](https://wandb.ai/site/weave) |
| **Patronus AI** | Automated LLM testing for hallucination and safety | Enterprise compliance teams | [patronus.ai](https://www.patronus.ai/) |
| **Maxim AI** | Evaluation platform for production LLM quality | Product teams tracking quality | [getmaxim.ai](https://www.getmaxim.ai/) |
| **Galileo** | LLM debugging, evaluation, and fine-tuning | ML engineers diagnosing issues | [rungalileo.io](https://www.rungalileo.io/) |
| **Arize Phoenix** | Open-source LLM observability and evaluation | Teams wanting free tracing | [phoenix.arize.com](https://phoenix.arize.com/) |

---

## Observability & Monitoring

*See what your AI is doing in production. Trace requests, debug failures, track costs.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **LangSmith** | Tracing, debugging, and monitoring for LangChain apps | LangChain users | [smith.langchain.com](https://smith.langchain.com/) |
| **Langfuse** | Open-source tracing and analytics for LLM apps | Teams wanting self-hosted observability | [langfuse.com](https://langfuse.com/) |
| **Helicone** | Request logging, cost tracking, caching | Teams monitoring API costs | [helicone.ai](https://www.helicone.ai/) |
| **Arize AI** | ML observability for production models | MLOps teams | [arize.com](https://arize.com/) |
| **Weights & Biases** | Experiment tracking and model monitoring | ML researchers and engineers | [wandb.ai](https://wandb.ai/) |
| **Datadog LLM Observability** | Enterprise APM with LLM-specific tracing | Enterprise DevOps teams | [datadoghq.com/product/llm-observability](https://www.datadoghq.com/product/llm-observability/) |
| **New Relic AI Monitoring** | LLM monitoring integrated with existing APM | Teams using New Relic | [newrelic.com/platform/ai-monitoring](https://newrelic.com/platform/ai-monitoring/) |
| **Honeycomb** | High-cardinality observability for AI traces | SRE teams debugging production | [honeycomb.io](https://www.honeycomb.io/) |
| **OpenLLMetry** | Open-source OpenTelemetry for LLMs | Teams standardizing on OTel | [github.com/traceloop/openllmetry](https://github.com/traceloop/openllmetry) |

---

## Safety & Guardrails

*Protect against jailbreaks, harmful outputs, data leakage, and policy violations.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Guardrails AI** | Input/output validation with programmable rules | Developers adding safety checks | [guardrailsai.com](https://www.guardrailsai.com/) |
| **NeMo Guardrails** | NVIDIA's toolkit for conversational safety rails | Enterprise chatbot teams | [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) |
| **Lakera Guard** | Real-time protection against prompt injection | Security-conscious teams | [lakera.ai](https://www.lakera.ai/) |
| **Rebuff** | Self-hardening prompt injection detector | Developers building public-facing AI | [rebuff.ai](https://www.rebuff.ai/) |
| **Llama Guard** | Meta's safety classifier for LLM inputs/outputs | Teams using Llama models | [ai.meta.com/llama](https://ai.meta.com/research/publications/llama-guard-llm-based-input-output-safeguard-for-human-ai-conversations/) |
| **Arthur Shield** | Enterprise AI firewall with policy enforcement | Enterprise security teams | [arthur.ai](https://www.arthur.ai/) |
| **Robust Intelligence** | AI security and validation platform | Enterprise ML security | [robustintelligence.com](https://www.robustintelligence.com/) |
| **Protect AI** | ML security scanning and vulnerability detection | MLOps security teams | [protectai.com](https://protectai.com/) |
| **Garak** | LLM vulnerability scanner (open-source) | Red teamers, security researchers | [github.com/leondz/garak](https://github.com/leondz/garak) |
| **LLM Guard** | Open-source input/output sanitization | Developers needing free guardrails | [llm-guard.com](https://llm-guard.com/) |

---

## Deployment & MLOps

*Get AI into production: serving, scaling, versioning, and infrastructure.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **vLLM** | High-throughput LLM inference engine | Teams self-hosting models | [vllm.ai](https://vllm.ai/) |
| **TensorRT-LLM** | NVIDIA's optimized LLM inference | Teams with NVIDIA GPUs | [github.com/NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| **Ollama** | Run LLMs locally with simple CLI | Developers, local experimentation | [ollama.com](https://ollama.com/) |
| **LM Studio** | Desktop app for running local LLMs | Non-technical users, prototypers | [lmstudio.ai](https://lmstudio.ai/) |
| **Text Generation Inference** | Hugging Face's production inference server | HF model deployers | [github.com/huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) |
| **BentoML** | Build and deploy ML services as APIs | ML engineers productionizing | [bentoml.com](https://www.bentoml.com/) |
| **Modal** | Serverless infrastructure for ML workloads | ML engineers avoiding DevOps | [modal.com](https://modal.com/) |
| **Anyscale** | Managed Ray for scalable AI applications | Teams needing distributed compute | [anyscale.com](https://www.anyscale.com/) |
| **Baseten** | Deploy and scale custom models | ML teams needing fast deployment | [baseten.co](https://www.baseten.co/) |
| **MLflow** | Open-source MLOps lifecycle management | ML teams tracking experiments | [mlflow.org](https://mlflow.org/) |
| **Kubeflow** | ML workflows on Kubernetes | Enterprise Kubernetes teams | [kubeflow.org](https://www.kubeflow.org/) |
| **SageMaker** | End-to-end ML platform on AWS | AWS enterprise customers | [aws.amazon.com/sagemaker](https://aws.amazon.com/pm/sagemaker) |

---

## Governance & Compliance

*Manage AI at the organizational level: policies, access control, audit trails, risk.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Credo AI** | AI governance, risk assessment, and compliance | AI governance teams, legal | [credo.ai](https://www.credo.ai/) |
| **Holistic AI** | AI risk management and auditing platform | Compliance officers, auditors | [holisticai.com](https://www.holisticai.com/) |
| **IBM AI Governance** | Enterprise AI lifecycle governance | Large enterprise IT | [ibm.com/products/ai-governance](https://www.ibm.com/products/ai-governance) |
| **Fiddler AI** | Model performance monitoring and explainability | ML teams needing explainability | [fiddler.ai](https://www.fiddler.ai/) |
| **Arthur AI** | AI monitoring with bias detection and explainability | Enterprise compliance teams | [arthur.ai](https://www.arthur.ai/) |
| **Truera** | AI quality management and monitoring | Regulated industry ML teams | [truera.com](https://truera.com/) |
| **DataRobot MLOps** | Enterprise model deployment and monitoring | Enterprise data science teams | [datarobot.com](https://www.datarobot.com/) |
| **Domino Data Lab** | Enterprise MLOps with governance built-in | Large enterprise ML teams | [dominodatalab.com](https://www.dominodatalab.com/) |
| **Cleanlab** | Data-centric AI for finding label errors | ML teams improving data quality | [cleanlab.ai](https://cleanlab.ai/) |

---

## No-Code & Business Platforms

*AI tools for non-developers: analysts, operators, knowledge workers, executives.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **ChatGPT** | General-purpose AI assistant with web access | Everyone | [chat.openai.com](https://chat.openai.com/) |
| **Claude** | AI assistant with document analysis and coding | Knowledge workers, analysts | [claude.ai](https://claude.ai/) |
| **Gemini** | Google's AI assistant integrated with Workspace | Google Workspace users | [gemini.google.com](https://gemini.google.com/) |
| **Microsoft Copilot** | AI assistant across Microsoft 365 | Enterprise Microsoft users | [copilot.microsoft.com](https://copilot.microsoft.com/) |
| **Notion AI** | AI writing and summarization in Notion | Notion users, PMs, writers | [notion.so/product/ai](https://www.notion.so/product/ai) |
| **Jasper** | AI content generation for marketing | Marketing teams | [jasper.ai](https://www.jasper.ai/) |
| **Copy.ai** | AI copywriting and workflow automation | Marketing, sales teams | [copy.ai](https://www.copy.ai/) |
| **Glean** | Enterprise AI search across all company data | Enterprise knowledge workers | [glean.com](https://www.glean.com/) |
| **Dust** | Build AI assistants with company knowledge | Operations teams, analysts | [dust.tt](https://dust.tt/) |
| **Zapier AI** | AI automation in workflow pipelines | Business operations, no-code builders | [zapier.com/ai](https://zapier.com/ai) |
| **Dify** | Open-source platform for building AI apps | Low-code developers | [dify.ai](https://dify.ai/) |
| **Flowise** | Drag-and-drop LLM flow builder | Non-developers building AI flows | [flowiseai.com](https://flowiseai.com/) |
| **n8n** | Workflow automation with AI nodes | Technical operations teams | [n8n.io](https://n8n.io/) |
| **Relevance AI** | No-code AI agent builder | Business users building agents | [relevanceai.com](https://relevanceai.com/) |
| **Voiceflow** | Build conversational AI without code | Product teams building chatbots | [voiceflow.com](https://www.voiceflow.com/) |

---

## Data & Compute Infrastructure

*The foundation: data processing, compute, and ML infrastructure.*

| Tool | Problem Solved | Primary Users | URL |
|:-----|:---------------|:--------------|:----|
| **Hugging Face Hub** | Model and dataset repository | All ML practitioners | [huggingface.co](https://huggingface.co/) |
| **PyTorch** | Deep learning framework | ML researchers and engineers | [pytorch.org](https://pytorch.org/) |
| **TensorFlow** | End-to-end ML platform | ML engineers, production teams | [tensorflow.org](https://www.tensorflow.org/) |
| **JAX** | High-performance ML research framework | ML researchers | [github.com/google/jax](https://github.com/google/jax) |
| **Keras** | High-level neural network API | ML practitioners wanting simplicity | [keras.io](https://keras.io/) |
| **scikit-learn** | Classical ML algorithms | Data scientists, analysts | [scikit-learn.org](https://scikit-learn.org/) |
| **Pandas** | Data manipulation and analysis | Data analysts, scientists | [pandas.pydata.org](https://pandas.pydata.org/) |
| **Polars** | Fast DataFrame library (Rust-based) | Performance-critical data work | [pola.rs](https://pola.rs/) |
| **NumPy** | Numerical computing foundation | All Python ML practitioners | [numpy.org](https://numpy.org/) |
| **Databricks** | Unified data and AI platform | Enterprise data teams | [databricks.com](https://www.databricks.com/) |
| **Snowflake Cortex** | AI/ML on Snowflake data | Snowflake users | [snowflake.com/en/data-cloud/cortex](https://www.snowflake.com/en/data-cloud/cortex/) |
| **BigQuery ML** | ML directly in BigQuery SQL | GCP data analysts | [cloud.google.com/bigquery-ml](https://cloud.google.com/bigquery-ml/docs) |
| **Lambda Labs** | GPU cloud for ML training | Teams needing GPU compute | [lambdalabs.com](https://lambdalabs.com/) |
| **RunPod** | GPU cloud with serverless options | Cost-conscious ML teams | [runpod.io](https://www.runpod.io/) |
| **Vast.ai** | GPU marketplace | Budget ML experimentation | [vast.ai](https://vast.ai/) |

---

## Research & Learning

*Stay current: papers, courses, communities, and documentation.*

| Resource | Purpose | URL |
|:---------|:--------|:----|
| **arXiv (cs.AI, cs.LG, cs.CL)** | Latest research papers | [arxiv.org/list/cs.AI/recent](https://arxiv.org/list/cs.AI/recent) |
| **Papers With Code** | Papers with implementation code | [paperswithcode.com](https://paperswithcode.com/) |
| **Hugging Face Papers** | Curated ML paper discussions | [huggingface.co/papers](https://huggingface.co/papers) |
| **Anthropic Research** | Claude and AI safety research | [anthropic.com/research](https://www.anthropic.com/research) |
| **OpenAI Research** | GPT and reasoning research | [openai.com/research](https://openai.com/research) |
| **Google DeepMind** | Frontier AI research | [deepmind.google/research](https://deepmind.google/research/) |
| **Prompt Engineering Guide** | Comprehensive prompting documentation | [promptingguide.ai](https://www.promptingguide.ai/) |
| **LangChain Documentation** | Building LLM applications | [docs.langchain.com](https://docs.langchain.com/) |
| **Anthropic Docs** | Claude best practices | [docs.anthropic.com](https://docs.anthropic.com/) |
| **OpenAI Cookbook** | Practical OpenAI examples | [cookbook.openai.com](https://cookbook.openai.com/) |
| **AI Engineer World's Fair** | Conference recordings and resources | [ai.engineer](https://www.ai.engineer/) |
| **Latent Space Podcast** | AI engineering discussions | [latent.space](https://www.latent.space/) |

---

## Quick Navigation by Role

| If you are a... | Start with these categories |
|:----------------|:----------------------------|
| **Developer building AI apps** | Development Frameworks → Agent Orchestration → Evaluation |
| **ML Engineer in production** | Deployment & MLOps → Observability → Safety |
| **Data Scientist exploring AI** | Foundation Models → RAG Infrastructure → Evaluation |
| **Product Manager** | No-Code Platforms → Prompt Management → Observability |
| **Security/Compliance Lead** | Safety & Guardrails → Governance → Observability |
| **Executive/Decision Maker** | No-Code Platforms → Governance → Research |

---

## The Integration Challenge

> **Companies will not struggle to access AI.**  
> **They will struggle to integrate, trust, measure, and govern it under pressure.**

This is why the tools in **Evaluation**, **Observability**, **Safety**, and **Governance** matter as much as the models themselves. The organizations that succeed with AI will be those that:

1. **Measure** what their AI systems actually do (not just what they're supposed to do)
2. **Trace** decisions back to inputs, prompts, and context
3. **Protect** against adversarial inputs and harmful outputs
4. **Govern** AI use with clear policies and audit trails
5. **Iterate** based on real production data, not assumptions

---

### Notes

Feedback and suggestions are welcome!

This list is maintained as part of the [Awesome Prompt Engineering](https://natnew.github.io/Awesome-Prompt-Engineering/) collection. For contributions, please see the repository guidelines.

*Last updated: January 2026*