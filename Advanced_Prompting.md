[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Advanced Prompting

Advanced prompting techniques enable language models to tackle complex, multi-step tasks that require planning, tool use, self-correction, and autonomous decision-making. These patterns form the foundation of agentic AI systems and production-grade applications.

This guide covers techniques essential for building AI systems that can reason, act, and improve their own outputs.

---

### ReAct: Reasoning and Acting

ReAct (Reason + Act) interleaves reasoning traces with actions, allowing models to dynamically plan, execute tools, and adapt based on observations. This is the foundational pattern for most AI agents.

#### ReAct Pattern Structure
```
Thought: [Model's reasoning about what to do next]
Action: [The action to take, often a tool call]
Observation: [The result of the action]
... (repeat until task complete)
Thought: [Final reasoning]
Answer: [Final response to user]
```

#### ReAct Example: Research Task
```
You have access to the following tools:
- search(query): Search the web for information
- calculate(expression): Evaluate mathematical expressions
- lookup(term): Look up a definition or fact

Use the ReAct pattern to answer questions. For each step, provide your Thought, 
then Action, then wait for the Observation.

Question: What is the population density of the country that won the 2022 FIFA World Cup?

Thought: I need to find out which country won the 2022 FIFA World Cup first.
Action: search("2022 FIFA World Cup winner")
Observation: Argentina won the 2022 FIFA World Cup, defeating France in the final.

Thought: Now I need to find Argentina's population and area to calculate density.
Action: search("Argentina population area square kilometers")
Observation: Argentina has a population of approximately 46 million and an area of 2,780,400 km².

Thought: Now I can calculate the population density.
Action: calculate("46000000 / 2780400")
Observation: 16.55

Thought: I have all the information needed to answer the question.
Answer: Argentina won the 2022 FIFA World Cup. Its population density is approximately 
16.5 people per square kilometer.
```

---

### Plan-and-Execute

Plan-and-Execute separates planning from execution, creating a high-level plan first and then executing each step. This improves reliability for complex multi-step tasks.

#### Plan-and-Execute Template
```
Task: Create a comprehensive competitive analysis report for [Company X] entering 
the cloud storage market.

First, create a detailed plan with numbered steps. Then execute each step.

PLANNING PHASE:
Create a step-by-step plan to accomplish this task. Consider what information 
is needed and in what order.

EXECUTION PHASE:
Execute each step of your plan, showing your work for each step.

SYNTHESIS PHASE:
Combine the results into a final deliverable.
```

#### Example Plan Output
```
PLAN:
1. Identify the top 5 competitors in cloud storage market
2. Gather key metrics for each competitor (pricing, features, market share)
3. Analyze Company X's current strengths and weaknesses
4. Identify market gaps and opportunities
5. Assess potential threats and barriers to entry
6. Synthesize findings into strategic recommendations

EXECUTING STEP 1:
[Detailed execution...]

EXECUTING STEP 2:
[Detailed execution...]
...
```

---

### Tool Use and Function Calling

Modern LLMs can use tools through structured function definitions. This enables models to access real-time data, perform calculations, and interact with external systems.

#### Defining Tools
```
You have access to the following tools:

<tools>
  <tool name="get_weather">
    <description>Get current weather for a location</description>
    <parameters>
      <param name="location" type="string" required="true">City and country</param>
      <param name="units" type="string" required="false">celsius or fahrenheit</param>
    </parameters>
  </tool>
  
  <tool name="send_email">
    <description>Send an email to a recipient</description>
    <parameters>
      <param name="to" type="string" required="true">Email address</param>
      <param name="subject" type="string" required="true">Email subject</param>
      <param name="body" type="string" required="true">Email content</param>
    </parameters>
  </tool>
  
  <tool name="query_database">
    <description>Execute a read-only SQL query</description>
    <parameters>
      <param name="query" type="string" required="true">SQL SELECT query</param>
    </parameters>
  </tool>
</tools>

When you need to use a tool, respond with:
<tool_call name="tool_name">
  <param name="param_name">value</param>
</tool_call>

User request: What's the weather like in Tokyo and should I bring an umbrella?
```

#### Tool Selection Reasoning
```
You have multiple tools available. Before calling a tool, explain:
1. Why this tool is needed
2. What parameters you'll use and why
3. What you expect to learn from the result

Tools available: [web_search, calculator, code_executor, file_reader]

Task: Analyze the CSV file 'sales_2024.csv' and tell me which quarter had the 
highest growth rate.

Reasoning: [Model explains tool selection]
Tool call: [Structured tool invocation]
```

---

### Prompt Chaining

Prompt chaining connects multiple prompts in sequence, where each prompt's output becomes input for the next. This enables complex workflows while keeping individual prompts focused.

#### Sequential Chain Example
```
CHAIN STEP 1 - EXTRACT:
Extract all technical requirements from the following project brief:
[project brief text]
Output format: Bulleted list of requirements

---

CHAIN STEP 2 - CATEGORIZE:
Categorize these requirements by type (functional, non-functional, constraints):
[output from step 1]
Output format: Grouped lists with priority (high/medium/low)

---

CHAIN STEP 3 - ESTIMATE:
For each high-priority requirement, estimate implementation complexity:
[output from step 2]
Output format: Table with requirement, complexity (1-5), and reasoning

---

CHAIN STEP 4 - SYNTHESIZE:
Create a project plan based on the prioritized, estimated requirements:
[output from step 3]
Output format: Phased implementation plan with milestones
```

#### Parallel Chain (Map-Reduce)
```
PHASE 1 - MAP (run in parallel):
Analyze each of these 5 customer interviews for key themes:
- Interview 1: [text] → Themes from Interview 1
- Interview 2: [text] → Themes from Interview 2
- Interview 3: [text] → Themes from Interview 3
- Interview 4: [text] → Themes from Interview 4
- Interview 5: [text] → Themes from Interview 5

PHASE 2 - REDUCE:
Synthesize the themes from all 5 analyses into:
1. Common themes (mentioned in 3+ interviews)
2. Unique insights (mentioned in only 1-2)
3. Contradictions or tensions between interviews
4. Recommended priorities based on frequency and intensity
```

---

### Self-Reflection and Critique

Self-reflection prompts the model to evaluate and improve its own outputs, catching errors and enhancing quality through iterative refinement.

#### Reflection Pattern
```
Task: Write a function to validate credit card numbers using the Luhn algorithm.

PHASE 1 - INITIAL ATTEMPT:
Write your first version of the code.

PHASE 2 - SELF-CRITIQUE:
Review your code and answer:
- Does it handle all edge cases (empty input, non-numeric, wrong length)?
- Is the algorithm implemented correctly?
- Is the code readable and well-documented?
- Are there any potential bugs?

PHASE 3 - REVISION:
Based on your critique, provide an improved version addressing all identified issues.

PHASE 4 - VERIFICATION:
Trace through your revised code with these test cases:
- "4532015112830366" (valid)
- "4532015112830367" (invalid)
- "" (empty)
- "abcd" (non-numeric)
```

#### Critique Framework
```
You've just generated a response. Now critique it using these criteria:

<critique_framework>
  <accuracy>Are all facts correct? Any hallucinations?</accuracy>
  <completeness>Does it fully address the request?</completeness>
  <clarity>Is it easy to understand?</clarity>
  <actionability>Can the user act on this information?</actionability>
  <tone>Is the tone appropriate for the context?</tone>
</critique_framework>

Original response: [previous output]

Critique each dimension (1-5 score with explanation), then provide a revised 
response addressing any weaknesses.
```

---

### Tree of Thoughts (ToT)

Tree of Thoughts extends chain-of-thought by exploring multiple reasoning paths simultaneously and evaluating which paths are most promising.

#### ToT Structure
```
Problem: A farmer needs to cross a river with a wolf, a goat, and a cabbage. 
The boat can only carry the farmer and one item. If left alone, the wolf will 
eat the goat, and the goat will eat the cabbage. How can the farmer get 
everything across safely?

Explore this as a tree of possibilities:

LEVEL 1 - Initial choices:
Branch A: Take wolf first → Evaluate: Goat eats cabbage. DEAD END.
Branch B: Take goat first → Evaluate: Wolf and cabbage are safe. VIABLE.
Branch C: Take cabbage first → Evaluate: Wolf eats goat. DEAD END.

LEVEL 2 - From Branch B (goat is across):
Branch B1: Return, take wolf → Evaluate: [continue reasoning]
Branch B2: Return, take cabbage → Evaluate: [continue reasoning]

[Continue expanding viable branches until solution found]

Evaluate and select the optimal path, then provide the complete solution.
```

#### ToT for Strategic Decisions
```
Decision: Should our startup pivot from B2B to B2C?

Generate 3 distinct strategic perspectives:

PERSPECTIVE 1 - Growth Optimist:
[Reasoning from this viewpoint, with assumptions and conclusions]
Viability score: X/10

PERSPECTIVE 2 - Risk Manager:
[Reasoning from this viewpoint, with assumptions and conclusions]
Viability score: X/10

PERSPECTIVE 3 - Resource Realist:
[Reasoning from this viewpoint, with assumptions and conclusions]
Viability score: X/10

SYNTHESIS:
Evaluate which perspective(s) best fit our actual situation and provide a 
recommendation with confidence level.
```

---

### Constitutional AI / Self-Correction

Constitutional prompting provides the model with principles to evaluate and revise its own outputs, ensuring alignment with specified values or requirements.

#### Constitutional Revision Pattern
```
CONSTITUTION (principles to follow):
1. Be accurate and cite sources when making factual claims
2. Present balanced perspectives on controversial topics
3. Acknowledge uncertainty when appropriate
4. Avoid harmful stereotypes or biased language
5. Be helpful while maintaining ethical boundaries

TASK: [User's original request]

PHASE 1 - Initial Response:
Generate your initial response to the task.

PHASE 2 - Constitutional Review:
Review your response against each principle:
- Principle 1: [Pass/Fail - Explanation]
- Principle 2: [Pass/Fail - Explanation]
- Principle 3: [Pass/Fail - Explanation]
- Principle 4: [Pass/Fail - Explanation]
- Principle 5: [Pass/Fail - Explanation]

PHASE 3 - Revision:
If any principles were violated, revise your response to address the issues 
while maintaining helpfulness.
```

---

### Meta-Prompting

Meta-prompting uses the LLM to generate or optimize prompts, leveraging the model's understanding of what makes effective instructions.

#### Prompt Generation
```
I need to create a prompt for the following task:
"Classify customer support tickets into categories: billing, technical, 
feature request, complaint, or other."

Generate 3 different prompt approaches:
1. A few-shot approach with examples
2. A structured reasoning approach
3. A role-based approach

For each, provide:
- The complete prompt
- Pros and cons of the approach
- When this approach would work best

Then recommend which approach to use and why.
```

#### Prompt Optimization
```
Current prompt:
"""
Summarize this article in 3 bullet points.
"""

This prompt is getting inconsistent results. Analyze potential issues and 
generate an improved version that:
- Ensures consistent bullet point format
- Specifies what makes a good summary point
- Handles edge cases (very short/long articles)

Provide the optimized prompt and explain your improvements.
```

---

### Evaluation Prompts (LLM-as-Judge)

Using LLMs to evaluate outputs enables scalable quality assessment and comparison.

#### Single Output Evaluation
```
Evaluate the following AI-generated response on these criteria:

<response>
[The response to evaluate]
</response>

<criteria>
  <criterion name="accuracy" weight="0.3">
    Are the facts correct and claims substantiated?
  </criterion>
  <criterion name="relevance" weight="0.25">
    Does it directly address the user's question?
  </criterion>
  <criterion name="completeness" weight="0.25">
    Is anything important missing?
  </criterion>
  <criterion name="clarity" weight="0.2">
    Is it well-organized and easy to understand?
  </criterion>
</criteria>

For each criterion:
1. Score from 1-5
2. Provide specific evidence from the response
3. Suggest specific improvements

Calculate weighted final score and overall assessment.
```

#### Pairwise Comparison
```
Compare these two responses to the same prompt and determine which is better.

Original prompt: "Explain machine learning to a 10-year-old"

Response A:
[First response]

Response B:
[Second response]

Evaluate on:
1. Age-appropriateness of language
2. Accuracy of explanation
3. Use of relatable examples
4. Engagement factor

For each criterion, state which response is better and why.
Provide final verdict: A is better / B is better / Tie (with reasoning)
```

---

### Temperature and Generation Parameters

Understanding when to adjust generation parameters for different tasks.

| Parameter | Low Value | High Value | Use Case |
|-----------|-----------|------------|----------|
| **Temperature** | 0.0-0.3 | 0.7-1.0 | Low: factual, code, analysis. High: creative, brainstorming |
| **Top-p** | 0.1-0.5 | 0.9-1.0 | Low: focused output. High: diverse responses |
| **Frequency penalty** | 0.0 | 1.0-2.0 | Higher values reduce repetition |

#### Temperature Guidelines
```
Task: Generate 5 creative product names for a new energy drink.
Recommendation: Temperature 0.8-1.0 (encourage creativity and variety)

Task: Convert this legal document to plain English.
Recommendation: Temperature 0.1-0.3 (accuracy and consistency critical)

Task: Write unit tests for this function.
Recommendation: Temperature 0.0-0.2 (deterministic, correct output needed)
```

---

### Advanced Pattern: Autonomous Agent Loop

Combining multiple techniques into a full agent architecture.

```
AGENT CONFIGURATION:
<agent>
  <name>Research Assistant</name>
  <goal>Answer complex questions requiring multiple sources</goal>
  
  <tools>
    - web_search(query): Search the internet
    - read_url(url): Read webpage content
    - note(content): Save information for later
    - calculate(expr): Mathematical calculations
  </tools>
  
  <constraints>
    - Maximum 10 tool calls per task
    - Always verify information from multiple sources
    - Cite sources in final response
  </constraints>
  
  <loop>
    1. THINK: Analyze current state and decide next action
    2. ACT: Execute tool or provide final response
    3. OBSERVE: Process tool results
    4. REFLECT: Assess progress toward goal
    5. REPEAT or CONCLUDE
  </loop>
</agent>

USER QUERY: [Complex question requiring research]

Begin agent loop:
```

---

### Quick Reference: Advanced Techniques

| Technique | Complexity | Best For |
|-----------|------------|----------|
| **ReAct** | Medium | Tasks requiring tool use and reasoning |
| **Plan-and-Execute** | Medium | Multi-step tasks with clear phases |
| **Tool Use** | Medium | Real-time data, calculations, external systems |
| **Prompt Chaining** | Medium | Complex workflows, document processing |
| **Self-Reflection** | Medium | Quality-critical outputs, code generation |
| **Tree of Thoughts** | High | Complex reasoning, strategic decisions |
| **Constitutional AI** | Medium | Alignment-critical applications |
| **Meta-Prompting** | High | Prompt optimization, template generation |
| **LLM-as-Judge** | Medium | Evaluation, comparison, quality assurance |

---

### Notes

Feedback and suggestions are welcome!

These advanced patterns can be combined to build sophisticated AI systems. Start with simpler patterns (ReAct, prompt chaining) before advancing to more complex architectures (Tree of Thoughts, autonomous agents).

**Learn more:**
- [LangChain Documentation](https://docs.langchain.com)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)