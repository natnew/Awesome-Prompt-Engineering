# Awesome-Prompt-Engineering 
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![All Contributors](https://img.shields.io/github/all-contributors/natnew/Awesome-Prompt-Engineering?color=success=flat-square)](#contributors) ![GitHub last commit](https://img.shields.io/github/last-commit/natnew/Awesome-Prompt-Engineering) ![GitHub Repo stars](https://img.shields.io/github/stars/natnew/Awesome-Prompt-Engineering?style=social) ![GitHub forks](https://img.shields.io/github/forks/natnew/Awesome-Prompt-Engineering?style=social) ![Static Badge](https://img.shields.io/badge/Maintained%20-%20Yes%20-%20lightgreen) ![Static Badge](https://img.shields.io/badge/Release%20-%20PROD%20-%20lightblue) ![Static Badge](https://img.shields.io/badge/License%20-%20MIT%20-%20orange) ![Static Badge](https://img.shields.io/badge/Language%20-%20MULTI%20-%20grey)

**Prompt engineering** is the foundational practice of crafting effective instructions to guide AI models toward accurate, useful, and reliable outputs. As AI systems have evolved, prompt engineering has expanded into **context engineering**—the broader discipline of architecting the full information environment that shapes model behaviour, including system prompts, conversation history, retrieved knowledge, tool definitions, and memory.

Whether you're writing your first prompt or orchestrating complex multi-agent systems, understanding how to communicate effectively with AI models remains essential. This repository provides resources spanning fundamental prompting techniques through to advanced context engineering strategies for production AI applications.

Effective prompt and context engineering requires understanding natural language processing, model capabilities, and user needs. As AI becomes increasingly integrated into scientific discovery, agentic systems, and enterprise applications, these skills are critical for developers, researchers, and AI practitioners. **Star, watch, and share** this repository to stay current with evolving best practices.🔥

---
## Contents
|  Name  |  Description  |  URL  |
| :-----:| :------------:| :----:|
| **Introduction**|  An Introduction to designing and optimizing textual prompts used to generate or influence the output of Artificial Intelligence models.  | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Introduction.html)|
| **Basic Prompting**|   Beginner-level material about designing and optimizing textual prompts used to generate or influence the output of Artificial Intelligence models. | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Basic_Prompting.html)|
| **Intermediate Prompting**| Intermediate-level material about designing and optimizing textual prompts used to generate or influence the output of Artificial Intelligence models.     | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Intermediate_Prompting.html)|
| **Advanced Prompting**| Advanced-level material about designing and optimizing textual prompts used to generate or influence the output of Artificial Intelligence models.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Advanced_Prompting.html)|
| **Image Prompting**| Material about a technique in which a machine learning model is used to generate images based on a given textual prompt.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Image_Prompting.html)|
|**Chatbot** | Provides resources on creating a chatbot. | [GITHub](https://natnew.github.io/Awesome-Prompt-Engineering/Chatbot.html)
| **AI Tools**| A collection of software, applications, frameworks, and libraries designed to support the development and implementation of Artificial Intelligence algorithms and applications.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/AI_Tools.html)|
| **Talks/Slides**| Presentations, speeches, or discussions that revolve around topics related to Artificial Intelligence.     | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Talks_Slides.html)|
| **Articles**| AI articles are written pieces of content that explore topics related to Artificial Intelligence. These articles cover various subjects such as AI technologies, applications, research, trends, challenges, and ethical considerations.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Articles.html)|
| **Resources**| A collection of resources that provide information, guidance, and tools related to the field of Artificial Intelligence.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/Resources.html)|
| **Ethical Charter**| Ethical Charter   | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/ethical_charter.html)|
| **Glossary**| A collection of terms and definitions related to the field of Artificial Intelligence.    | [GitHub](https://natnew.github.io/Awesome-Prompt-Engineering/AI_Glossary.html)|

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
|  Topic  |  Description  |  Date  | URL
| :-----:| :------------:| :----:|:--------:
|📘eBook | eBook published | 17th April 2023 | [URL](https://natashanewbold.gumroad.com/l/zctxdh)
|📘eBook | eBook published | 28th April 2023 | [URL](https://natashanewbold.gumroad.com/l/kjxpip)
|💻Website| Website is live | 2nd May 2023| [URL](https://natnew.github.io/Awesome-Prompt-Engineering/)
|📄New Page| Ethical Charter | 14th May 2023 | [URL](https://natnew.github.io/Awesome-Prompt-Engineering/ethical_charter.html)
|📚Guide|A - Z Machine Learning Guide | 15th May 2023| [URL](https://natnew.github.io/Awesome-Prompt-Engineering/ML_Guide.html)|
|🔍Cheat Sheet |ML CheatSheet | 16th May 2023| [URL](https://natnew.github.io/Awesome-Prompt-Engineering/ML_CheatSheet.html)|

---
## Prompt Engineering Ebooks, Guides and Cheat Sheets

##### [EBook: The Creative Side of AI: Mastering the Art of Prompt Engineering](https://natashanewbold.gumroad.com/l/zctxdh)
##### [Mastering Prompt Engineering: A Free eBook](https://natashanewbold.gumroad.com/l/kjxpip)
##### [A - Z Machine Learning Guide](https://natnew.github.io/Awesome-Prompt-Engineering/ML_Guide.html)
##### [ML CheatSheet](https://natnew.github.io/Awesome-Prompt-Engineering/ML_CheatSheet.html)
##### [100 Projects For Beginners Using Python](https://medium.com/@natashanewbold/100-projects-for-beginners-using-python-8b7f55bbd1ad?sk=ff4103731ceecffa845df3e632447964)
##### [An Introduction to Prompt Engineering: Key Concepts & Tips For Beginners](https://medium.com/ai-vanguard/ai-prompt-engineering-tips-for-beginners-9ccb5b54243?sk=b6a83e29c3fd82496b78f8e5849512eb)
##### [100 chats for veterans](https://chatgpt.com/use-cases/veterans)
##### [100 chats for college students](https://chatgpt.com/use-cases/students)

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
##### Many thanks to our contributors. Want to contribute? Visit the Workflow documentation.  [here](https://github.com/natnew/Awesome-Prompt-Engineering/blob/main/Workflow.md).

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
