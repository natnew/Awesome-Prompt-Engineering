---
layout: default
title: AI Agents
description: Building autonomous systems with tools, memory, and planning.
nav_order: 6
---

[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## AI Agents

AI agents are systems that use LLMs to reason, plan, and take actions autonomously. They represent the evolution from single-turn chatbots to multi-step, tool-using systems that can accomplish complex tasks.

Understanding agent architectures is essential for modern prompt and context engineering — agents are where prompting meets system design.

---

### Contents

- [What Makes an Agent](#what-makes-an-agent)
- [Agent Patterns](#agent-patterns)
- [Orchestration Frameworks](#orchestration-frameworks)
- [Tool Integration](#tool-integration)
- [Memory & State](#memory--state)
- [Multi-Agent Systems](#multi-agent-systems)
- [Evaluation & Debugging](#evaluation--debugging)
- [Example Projects](#example-projects)

---

## What Makes an Agent

An AI agent combines four core capabilities:

```
┌─────────────────────────────────────────────────────────┐
│                      AI AGENT                           │
├─────────────────────────────────────────────────────────┤
│  🧠 REASONING    │  Plan steps, analyze results        │
│  🔧 TOOL USE     │  Call APIs, search, execute code    │
│  💾 MEMORY       │  Remember context across steps      │
│  🔄 ITERATION    │  Loop until task complete           │
└─────────────────────────────────────────────────────────┘
```

**Chatbot vs Agent:**

| Capability | Chatbot | Agent |
|:-----------|:--------|:------|
| Turns | Single response | Multiple steps |
| Tools | None or limited | Dynamic tool selection |
| Memory | Session only | Persistent state |
| Planning | None | Explicit reasoning |
| Autonomy | Reactive | Proactive |

---

## Agent Patterns

Core architectural patterns for building agents.

### ReAct (Reasoning + Acting)

The foundational pattern: interleave thinking with action.

```
Thought: I need to find the current weather in Tokyo
Action: weather_api(location="Tokyo")
Observation: 15°C, partly cloudy
Thought: Now I can answer the user's question
Answer: It's currently 15°C and partly cloudy in Tokyo.
```

**Use when:** Tasks require dynamic tool selection based on intermediate results.

### Plan-and-Execute

Separate planning from execution for complex tasks.

```
PLAN:
1. Search for recent AI safety papers
2. Summarize top 3 findings
3. Compare to last year's research
4. Write synthesis report

EXECUTE:
[Step 1] Searching... found 47 papers
[Step 2] Summarizing top 3...
[Step 3] Comparing...
[Step 4] Writing report...
```

**Use when:** Tasks have clear phases and benefit from upfront planning.

### Reflection / Self-Critique

Agent evaluates and improves its own output.

```
INITIAL OUTPUT: [first attempt]
CRITIQUE: The code doesn't handle edge cases for empty input
REVISION: [improved version with edge case handling]
VERIFY: Now passes all test cases
```

**Use when:** Quality is critical and errors are costly.

### Multi-Agent Collaboration

Multiple specialized agents working together.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Researcher │ ──► │   Writer    │ ──► │   Editor    │
│  (gathers)  │     │  (drafts)   │     │  (refines)  │
└─────────────┘     └─────────────┘     └─────────────┘
```

**Use when:** Tasks benefit from specialized roles or perspectives.

---

## Orchestration Frameworks

Tools for building agent systems.

| Framework | Best For | Key Features | Link |
|:----------|:---------|:-------------|:-----|
| **LangGraph** | Complex workflows with cycles | State management, conditional edges, persistence | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) |
| **CrewAI** | Role-based multi-agent teams | Agent personas, task delegation, collaboration | [crewai.com](https://www.crewai.com/) |
| **AutoGen** | Conversational multi-agent | Microsoft-backed, group chat patterns | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) |
| **OpenAI Agents SDK** | OpenAI-native agents | Handoffs, guardrails, tracing | [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python) |
| **Anthropic MCP** | Standardized tool integration | Model Context Protocol, universal tool format | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |
| **Letta (MemGPT)** | Long-term memory | Persistent memory, self-editing context | [letta.com](https://www.letta.com/) |
| **DSPy** | Optimized prompts | Compile prompts from examples, auto-optimization | [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |

---

## Tool Integration

Agents need tools to interact with the world.

### Common Tool Categories

| Category | Examples | Use Case |
|:---------|:---------|:---------|
| **Search** | Web search, document search, code search | Information retrieval |
| **Code** | Python REPL, shell, sandboxed execution | Computation, automation |
| **APIs** | Weather, stocks, databases, SaaS | External data and actions |
| **Files** | Read, write, parse documents | Document processing |
| **Communication** | Email, Slack, calendar | User-facing actions |

### Tool Definition Example

```python
# OpenAI Function Calling format
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country, e.g., 'Tokyo, Japan'"
                },
                "units": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "default": "celsius"
                }
            },
            "required": ["location"]
        }
    }
}]
```

### Tool Platforms

| Platform | What It Provides | Link |
|:---------|:-----------------|:-----|
| **Composio** | 150+ pre-built integrations (GitHub, Slack, etc.) | [composio.dev](https://composio.dev/) |
| **Toolhouse** | Managed tool infrastructure | [toolhouse.ai](https://toolhouse.ai/) |
| **Browserbase** | Browser automation for agents | [browserbase.com](https://www.browserbase.com/) |

---

## Memory & State

Agents need memory to work across multiple steps and sessions.

### Memory Types

| Type | Scope | Use Case |
|:-----|:------|:---------|
| **Working Memory** | Current task | Intermediate results, scratchpad |
| **Short-Term** | Current session | Conversation history |
| **Long-Term** | Across sessions | User preferences, learned facts |
| **Episodic** | Past interactions | Similar past tasks, outcomes |
| **Semantic** | Domain knowledge | Facts, relationships, embeddings |

### State Management Patterns

**Explicit State Object:**
```python
state = {
    "task": "Research AI safety",
    "steps_completed": ["search", "summarize"],
    "current_step": "compare",
    "artifacts": {"papers": [...], "summary": "..."},
    "errors": []
}
```

**Conversation History:**
```python
messages = [
    {"role": "system", "content": "You are a research assistant..."},
    {"role": "user", "content": "Find recent AI safety papers"},
    {"role": "assistant", "content": "I'll search for...", "tool_calls": [...]},
    {"role": "tool", "content": "Found 47 papers..."},
    {"role": "assistant", "content": "I found 47 papers. The top 3 are..."}
]
```

---

## Multi-Agent Systems

Patterns for agents working together.

### Hierarchical

```
         ┌──────────────┐
         │  Supervisor  │
         └──────┬───────┘
        ┌───────┼───────┐
        ▼       ▼       ▼
    ┌──────┐ ┌──────┐ ┌──────┐
    │Agent1│ │Agent2│ │Agent3│
    └──────┘ └──────┘ └──────┘
```

Supervisor delegates and coordinates.

### Collaborative

```
    ┌──────┐     ┌──────┐
    │Agent1│◄───►│Agent2│
    └──┬───┘     └───┬──┘
       │             │
       └──────┬──────┘
              ▼
         ┌──────┐
         │Agent3│
         └──────┘
```

Agents communicate peer-to-peer.

### Pipeline

```
Agent1 ──► Agent2 ──► Agent3 ──► Output
```

Sequential handoffs with specialization.

---

## Evaluation & Debugging

Agents are harder to evaluate than single-turn models.

### What to Measure

| Metric | What It Tells You |
|:-------|:------------------|
| **Task completion rate** | Does it finish the job? |
| **Step efficiency** | How many steps to complete? |
| **Tool accuracy** | Right tool, right parameters? |
| **Error recovery** | Handles failures gracefully? |
| **Cost per task** | Token usage, API calls |
| **Latency** | Time to completion |

### Debugging Tools

| Tool | Purpose | Link |
|:-----|:--------|:-----|
| **LangSmith** | Tracing, debugging LangChain agents | [smith.langchain.com](https://smith.langchain.com/) |
| **AgentOps** | Agent-specific observability | [agentops.ai](https://www.agentops.ai/) |
| **Langfuse** | Open-source LLM tracing | [langfuse.com](https://langfuse.com/) |
| **Braintrust** | Evaluation and logging | [braintrust.dev](https://www.braintrust.dev/) |

### Common Failure Modes

| Failure | Cause | Mitigation |
|:--------|:------|:-----------|
| **Infinite loops** | No termination condition | Max steps, explicit exit |
| **Tool hallucination** | Inventing non-existent tools | Strict tool validation |
| **Context overflow** | Too much history | Summarization, pruning |
| **Goal drift** | Losing track of objective | Explicit goal in state |
| **Premature termination** | Stopping before complete | Completion verification |

---

## Example Projects

Open-source agent implementations to learn from.

| Project | Description | Link |
|:--------|:------------|:-----|
| **GPT-Researcher** | Autonomous research agent | [github.com/assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) |
| **AutoGPT** | General-purpose autonomous agent | [github.com/Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) |
| **BabyAGI** | Minimal task-driven agent | [github.com/yoheinakajima/babyagi](https://github.com/yoheinakajima/babyagi) |
| **Voyager** | Minecraft agent with lifelong learning | [github.com/MineDojo/Voyager](https://github.com/MineDojo/Voyager) |
| **Open Interpreter** | Code execution agent | [github.com/OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) |
| **SWE-agent** | Software engineering agent | [github.com/princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent) |
| **Devon** | Open-source AI software engineer | [github.com/entropy-research/Devon](https://github.com/entropy-research/Devon) |

---

## Key Resources

### Essential Reading

- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic's official guide
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng's deep dive
- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) — Academic framework

### Courses

- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — DeepLearning.AI
- [Multi AI Agent Systems with CrewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) — DeepLearning.AI

---

### Notes

Feedback and suggestions are welcome!

*Last updated: January 2026*