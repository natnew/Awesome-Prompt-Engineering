---
layout: default
title: Home
description: The ultimate guide to prompt engineering, context engineering, and AI agents.
nav_order: 1
---

# Awesome-Prompt-Engineering 
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![All Contributors](https://img.shields.io/github/all-contributors/natnew/Awesome-Prompt-Engineering?color=success=flat-square)](#contributors) ![GitHub last commit](https://img.shields.io/github/last-commit/natnew/Awesome-Prompt-Engineering) ![GitHub Repo stars](https://img.shields.io/github/stars/natnew/Awesome-Prompt-Engineering?style=social) ![GitHub forks](https://img.shields.io/github/forks/natnew/Awesome-Prompt-Engineering?style=social) ![Maintained Status](https://img.shields.io/badge/Maintained%20-%20Yes%20-%20lightgreen) ![Release Status](https://img.shields.io/badge/Release%20-%20PROD%20-%20lightblue) ![License](https://img.shields.io/badge/License%20-%20MIT%20-%20orange) ![Language](https://img.shields.io/badge/Language%20-%20MULTI%20-%20grey)

**Prompt engineering** is the foundational practice of crafting effective instructions to guide AI models toward accurate, useful, and reliable outputs. As AI systems have evolved, prompt engineering has expanded into **context engineering**—the broader discipline of architecting the full information environment that shapes model behaviour, including system prompts, conversation history, retrieved knowledge, tool definitions, and memory.

Whether you're writing your first prompt or orchestrating complex multi-agent systems, understanding how to communicate effectively with AI models remains essential. This repository provides resources spanning fundamental prompting techniques through to advanced context engineering strategies for production AI applications.

Effective prompt and context engineering requires understanding natural language processing, model capabilities, and user needs. As AI becomes increasingly integrated into scientific discovery, agentic systems, and enterprise applications, these skills are critical for developers, researchers, and AI practitioners. **Star, watch, and share** this repository to stay current with evolving best practices.🔥

---
## Contents

|  Name  |  Description  |  URL  |
| :-----:| :------------:| :----:|
| **Introduction** | Timeline of AI from foundations to frontier models. Context for how we got here. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Introduction.html) |
| **Basic Prompting** | Core techniques: prompt structure, roles, delimiters, output formatting, constraints. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Basic_Prompting.html) |
| **Intermediate Prompting** | Reasoning techniques: few-shot, chain-of-thought, self-consistency, structured reasoning. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Intermediate_Prompting.html) |
| **Advanced Prompting** | Agentic patterns: ReAct, tool use, prompt chaining, self-reflection, meta-prompting. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Advanced_Prompting.html) |
| **Multi-Modal Prompting** | Visual AI: text-to-image, image analysis, video generation, model-specific syntax. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Multi_Modal_Prompting.html) |
| **AI Agents** | Building autonomous systems: patterns, orchestration frameworks, tools, memory, debugging. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Agents.html) |
| **AI Tools** | Comprehensive guide to tools for building, deploying, evaluating, and governing AI. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/AI_Tools.html) |
| **Deep Learning Guide** | LLM-relevant concepts: transformers, attention, training, tokenization, inference. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Deep_Learning_Guide.html) |
| **Articles** | Curated reading list organized by topic: agents, RAG, evaluation, safety, production. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Articles.html) |
| **Resources** | Learning resources: courses, papers, communities, podcasts, newsletters by role. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Resources.html) |
| **Talks/Slides** | Presentations and discussions on AI topics from researchers and practitioners. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Talks_Slides.html) |
| **FAQ** | Answers to common questions about LLMs, prompting, agents, RAG, and production. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/FAQ.html) |
| **AI Cheat Sheet** | Quick reference: prompt patterns, API parameters, token estimation, cost optimization. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/AI_CheatSheet.html) |
| **Glossary** | 148 terms and definitions covering LLMs, agents, safety, and context engineering. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/AI_Glossary.html) |
| **Ethical Charter** | Community values: human-centeredness, fairness, transparency, safety, accountability. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/ethical_charter.html) |

---
## Context Engineering: The Evolution of Prompt Engineering

The field has evolved from crafting individual prompts to architecting complete context systems. Context engineering encompasses everything that shapes model behaviour at inference time.

### Core Concepts

- **System Prompts** — High-level instructions that define model behaviour, persona, and constraints
- **Few-Shot Examples** — Demonstrating desired input-output patterns through curated examples
- **Chain-of-Thought** — Encouraging step-by-step reasoning for complex problems
- **Retrieved Context (RAG)** — Dynamically injecting relevant knowledge from external sources
- **Tool Definitions** — Specifying available actions and their schemas for agentic systems
- **Memory Management** — Handling conversation history and long-term state effectively

### Recommended Reading

- [Context Engineering Guide](https://www.promptingguide.ai/guides/context-engineering-guide) — Comprehensive guide from DAIR.AI
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic's engineering best practices
- [Prompt Engineering Best Practices](https://claude.com/blog/best-practices-for-prompt-engineering) — Claude's official guide
- [OpenAI Prompt Engineering Guide](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) — OpenAI's official documentation

---
## Modern Tools & Frameworks

### Prompt Management & Versioning

- [PromptLayer](https://promptlayer.com/) — Version control, logging, and analytics for prompts
- [Agenta](https://agenta.ai/) — Open-source platform for prompt testing with side-by-side LLM comparisons
- [Langfuse](https://langfuse.com/) — Open-source LLM engineering platform with prompt management
- [Opik](https://github.com/comet-ml/opik) — Open-source platform for LLM observability, evaluations, and prompt optimization
- [Helicone](https://helicone.ai/) — Lightweight prompt logging and analytics

### Development Frameworks

- [LangChain](https://langchain.com/) — Framework for building applications with LLMs
- [LangSmith](https://smith.langchain.com/) — Debugging, testing, and monitoring for LLM applications
- [Haystack](https://haystack.deepset.ai/) — Framework for building NLP and RAG pipelines
- [DSPy](https://dspy-docs.vercel.app/) — Programmatic prompting and optimization framework

### Testing & Evaluation

- [Promptfoo](https://promptfoo.dev/) — Open-source prompt testing and evaluation
- [TruLens](https://www.trulens.org/) — Feedback and evaluation for LLM applications
- [Weave](https://wandb.ai/site/weave) — Trace-based debugging and scoring from Weights & Biases
- [Maxim AI](https://www.getmaxim.ai/) — Systematic evaluation and benchmarking platform

### Safety & Guardrails

- [Guardrails AI](https://www.guardrailsai.com/) — Define schemas and constraints for model outputs
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — NVIDIA's toolkit for LLM safety
- [Rebuff](https://github.com/protectai/rebuff) — Prompt injection detection and prevention
- [Lakera Guard](https://www.lakera.ai/) — Real-time protection against prompt attacks

---
## Announcements :eyes:
##### Watch this repository to keep up-to-date with the latest updates and announcements.

|  Topic  |  Description  |  Date  | URL |
| :-----:| :------------:| :----:| :----: |
| 📘eBook | eBook published | 17th April 2023 | [URL](https://natashanewbold.gumroad.com/l/zctxdh) |
| 📘eBook | eBook published | 28th April 2023 | [URL](https://natashanewbold.gumroad.com/l/kjxpip) |
| 💻Website | Website is live | 2nd May 2023 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/) |
| 📄New Page | Ethical Charter | 14th May 2023 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/ethical_charter.html) |
| 🔄Update | Context Engineering section added | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/) |
| 🤖New Page | AI Agents guide | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/Agents.html) |
| 🧠New Page | Deep Learning for LLMs guide | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/Deep_Learning_Guide.html) |
| 📚Update | Glossary expanded to 148 terms | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/AI_Glossary.html) |
| 📋New Page | AI Cheat Sheet | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/AI_CheatSheet.html) |
| ❓New Page | FAQ updated with modern questions | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/FAQ.html) |
| 🎤Update | Talks/Slides updated with LLM-era content | January 2026 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/Talks_Slides.html) |

---
## Guides and Learning Resources

##### [EBook: The Creative Side of AI: Mastering the Art of Prompt Engineering](https://natashanewbold.gumroad.com/l/zctxdh)
##### [Mastering Prompt Engineering: A Free eBook](https://natashanewbold.gumroad.com/l/kjxpip)
##### [AI Cheat Sheet](https://natnew.github.io/Awesome-Prompt-Engineering/AI_CheatSheet.html)
##### [Deep Learning for LLMs Guide](https://natnew.github.io/Awesome-Prompt-Engineering/Deep_Learning_Guide.html)
##### [AI Agents Guide](https://natnew.github.io/Awesome-Prompt-Engineering/Agents.html)
##### [Prompt Engineering Guide by Learn Prompting](https://learnprompting.org/docs/introduction)
##### [DAIR.AI Prompt Engineering Guide](https://www.promptingguide.ai/)
##### [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
##### [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---
## Additional Resources

<table>
  <tr>
    <td width="100%">
         Join the <a href="https://github.com/natnew/Awesome-Data-Science">Artificial Intelligence First</a> newsletter today. You'll be kept informed about open source frameworks, carefully selected tutorials, and articles compiled by experts in artificial intelligence.
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="100%">
      Explore <a href="https://github.com/natnew/Awesome-Data-Science">Awesome Data Science.</a> A carefully curated list of awesome Data Science resources.
    </td>
  </tr>
</table>

---
## More Awesome Lists

- [Awesome Data Science](https://github.com/natnew/Awesome-Data-Science) — Curated data science resources
- [Awesome Generative AI](https://github.com/natnew/Awesome-Generative-AI) — Comprehensive generative AI resources
- [Awesome AI Scientists](https://github.com/natnew/Awesome-AI-Scientists) — AI for scientific discovery
- [Awesome Physical AI](https://github.com/natnew/awesome-physical-ai) — Robotics + AI resources for Physical AI / Embodied AI
- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts) — ChatGPT prompt examples
- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM) — Large language model resources
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) — DAIR.AI's comprehensive guide

---
## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/natnew"><img src="https://avatars.githubusercontent.com/u/37782009?v=4?s=100" width="100px;" alt="Natasha"/><br /><sub><b>Natasha</b></sub></a><br /><a href="#design-natnew" title="Design">🎨</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/issues?q=author%3Anatnew" title="Bug reports">🐛</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/commits?author=natnew" title="Code">💻</a> <a href="#content-natnew" title="Content">🖋</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/commits?author=natnew" title="Documentation">📖</a> <a href="#ideas-natnew" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-natnew" title="Project Management">📆</a> <a href="#question-natnew" title="Answering Questions">💬</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/pulls?q=is%3Apr+reviewed-by%3Anatnew" title="Reviewed Pull Requests">👀</a> <a href="#security-natnew" title="Security">🛡️</a> <a href="#tool-natnew" title="Tools">🔧</a> <a href="#research-natnew" title="Research">🔬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.deamarialeon.com/"><img src="https://avatars.githubusercontent.com/u/11835246?v=4?s=100" width="100px;" alt="Dea María Léon"/><br /><sub><b>Dea María Léon</b></sub></a><br /><a href="https://github.com/natnew/Awesome-Prompt-Engineering/commits?author=DeaMariaLeon" title="Documentation">📖</a> <a href="#research-DeaMariaLeon" title="Research">🔬</a> <a href="#question-DeaMariaLeon" title="Answering Questions">💬</a> <a href="#ideas-DeaMariaLeon" title="Ideas, Planning, & Feedback">🤔</a> <a href="#research-DeaMariaLeon" title="Research">🔬</a> <a href="#content-DeaMariaLeon" title="Content">🖋</a> <a href="#ideas-DeaMariaLeon" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://bartolomeu-rodrigues.com/"><img src="https://avatars.githubusercontent.com/u/13721983?v=4?s=100" width="100px;" alt="Bartolomeu Rodrigues"/><br /><sub><b>Bartolomeu Rodrigues</b></sub></a><br /><a href="#ideas-Bartmr" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/commits?author=Bartmr" title="Documentation">📖</a> <a href="https://github.com/natnew/Awesome-Prompt-Engineering/issues?q=author%3ABartmr" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ElitePete"><img src="https://avatars.githubusercontent.com/u/105971332?v=4?s=100" width="100px;" alt="ElitePete"/><br /><sub><b>ElitePete</b></sub></a><br /><a href="#content-ElitePete" title="Content">🖋</a> <a href="#ideas-ElitePete" title="Ideas, Planning, & Feedback">🤔</a> <a href="#question-ElitePete" title="Answering Questions">💬</a> <a href="#tool-ElitePete" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jaimboh"><img src="https://avatars.githubusercontent.com/u/110313204?v=4?s=100" width="100px;" alt="Jaimboh"/><br /><sub><b>Jaimboh</b></sub></a><br /><a href="#tool-Jaimboh" title="Tools">🔧</a> <a href="#question-Jaimboh" title="Answering Questions">💬</a> <a href="#content-Jaimboh" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kkahadze"><img src="https://avatars.githubusercontent.com/u/85003299?v=4?s=100" width="100px;" alt="Konstantine"/><br /><sub><b>Konstantine</b></sub></a><br /><a href="#content-kkahadze" title="Content">🖋</a> <a href="#ideas-kkahadze" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Contributions ⭐

We believe that feedback and suggestions are crucial to improving our content and making it more useful for our readers. That's why we encourage you to share your thoughts with us and let us know what you think about our content.

Your feedback can help us identify areas where we can improve and provide more value to our readers. Whether you have suggestions for new topics, ideas for interactive elements, or feedback on our existing content, we would love to hear from you.

By sharing your thoughts and ideas with us, you can help shape the direction of our GitHub repo page and make it a more valuable resource for the prompt engineering community. So please don't hesitate to reach out and let us know what you think. We're looking forward to hearing from you!

This project follows the [all-contributors](https://allcontributors.org/) specification. Contributions of any kind are welcome!

##### Many thanks to our contributors. Want to contribute? Visit the Workflow documentation [here](https://github.com/natnew/Awesome-Prompt-Engineering/blob/main/Workflow.md).

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
