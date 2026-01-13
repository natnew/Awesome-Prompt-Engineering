[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Basic Prompting

Basic prompting is the foundation of effective communication with large language models (LLMs). Whether you're working with Claude, GPT, Gemini, or other models, understanding how to structure your prompts determines the quality and relevance of the outputs you receive.

At its core, prompting is about providing clear context, specific instructions, and well-defined constraints. The techniques covered here apply across all major LLMs, though each model may have slight preferences in formatting and structure.

---

### The Prompt Structure Formula

A well-structured prompt typically contains three elements:

```
[ROLE/PERSONA] + [TASK/INSTRUCTION] + [CONSTRAINTS/FORMAT]
```

**Example:**
> You are a **senior data scientist**. Your task is to **explain the concept of overfitting to a non-technical stakeholder**. Keep your explanation **under 150 words and use a real-world analogy**.

---

### System Prompts vs User Prompts

Understanding the distinction between system and user prompts is fundamental:

| Type | Purpose | Example |
|------|---------|---------|
| **System Prompt** | Sets the model's behavior, persona, and rules for the entire conversation | "You are a helpful coding assistant. Always explain your code with comments." |
| **User Prompt** | The specific request or question in a single turn | "Write a Python function to calculate factorial." |

**System Prompt Example:**
```
You are a professional technical writer. You specialize in creating clear, 
concise documentation for software APIs. Always use active voice, include 
code examples where relevant, and structure responses with clear headings.
```

**User Prompt Example:**
```
Document the following Python function for our API reference guide:

def calculate_discount(price: float, percentage: float) -> float:
    return price * (1 - percentage / 100)
```

---

### Role-Based Prompting

Assigning a specific role or persona helps the model adopt appropriate expertise, tone, and perspective.

#### AI Engineer
> You are an **AI Engineer** preparing a presentation for executives. Create a concise, compelling introduction (3-4 sentences) explaining the business value of implementing retrieval-augmented generation (RAG) in customer support.

#### Technical Writer
> You are a **Technical Writer** creating documentation for developers. Explain how API rate limiting works, including a code example showing how to handle rate limit errors gracefully.

#### Data Analyst
> You are a **Data Analyst** performing exploratory analysis. Given the following sales data, identify three key insights and explain their business implications:
> 
> ```csv
> month,revenue,customers
> Jan,50000,120
> Feb,48000,115
> Mar,62000,145
> ```

#### Language Translator
> You are a **Professional Translator** specializing in technical documents. Translate the following English text to French, preserving technical terminology:
> 
> ```
> The API endpoint accepts JSON payloads with a maximum size of 10MB.
> ```

---

### Output Format Specification

Explicitly requesting a specific output format dramatically improves consistency and usability.

#### JSON Output
> Analyze the following customer review and return your analysis as JSON with the fields: `sentiment` (positive/negative/neutral), `confidence` (0-1), `key_topics` (array), and `summary` (string).
> 
> Review: "The product arrived quickly and works great, but the instructions were confusing."

**Expected Output:**
```json
{
  "sentiment": "positive",
  "confidence": 0.75,
  "key_topics": ["delivery", "product quality", "documentation"],
  "summary": "Customer satisfied with product and shipping but found instructions unclear."
}
```

#### Markdown Table
> Compare Python, JavaScript, and Go for building REST APIs. Present your comparison as a markdown table with columns for: Language, Learning Curve, Performance, Ecosystem, and Best Use Case.

#### Bullet Points
> List the top 5 considerations when choosing a cloud provider for a machine learning workload. Use bullet points with a brief explanation for each.

#### Step-by-Step
> Explain how to set up a Python virtual environment. Format your response as numbered steps that a beginner could follow.

---

### Using Delimiters

Delimiters clearly separate different parts of your prompt, especially when including input data. This prevents prompt injection and improves clarity.

#### XML Tags (Recommended for Claude)
```
Summarize the following article:

<article>
Artificial intelligence has transformed how businesses operate...
</article>

Provide your summary in 2-3 sentences.
```

#### Triple Backticks
```
Translate the following code from Python to JavaScript:

```python
def greet(name):
    return f"Hello, {name}!"
```

Maintain the same functionality and add appropriate type hints.
```

#### Triple Quotes
```
Proofread the following text for grammar and spelling errors:

"""
Their going to the store tommorow to by some grocerys.
"""

Return the corrected text and list the errors you found.
```

---

### Positive vs Negative Constraints

Both telling the model what TO do and what NOT to do are effective strategies.

#### Positive Constraints (Do This)
> Write a product description for wireless headphones. **Include** the following: battery life, noise cancellation features, and comfort for extended use. **Use** an enthusiastic but professional tone. **Keep** the description under 100 words.

#### Negative Constraints (Don't Do This)
> Write a product description for wireless headphones. **Do not** use hyperbole or unsubstantiated claims. **Avoid** technical jargon that consumers wouldn't understand. **Don't** mention competitor products.

#### Combined Approach (Most Effective)
> Write a product description for wireless headphones.
> 
> **Include:**
> - Battery life and charging speed
> - Key features (noise cancellation, comfort)
> - Target use cases
> 
> **Avoid:**
> - Superlatives without evidence ("best ever")
> - Technical specifications (leave for spec sheet)
> - Pricing information
> 
> **Format:** 75-100 words, 2 paragraphs

---

### Providing Context

Context helps the model understand the situation and tailor its response appropriately.

#### Audience Context
> Explain how neural networks learn. Your audience is **high school students with no prior programming experience**. Use analogies they would understand.

#### Purpose Context
> Write an email requesting a project deadline extension. **Context:** You're a project manager, the delay is due to unexpected API changes from a vendor, and you need 5 additional days. The recipient is your direct supervisor who values brevity.

#### Domain Context
> Review this code for security vulnerabilities. **Context:** This is a Python Flask application handling user authentication for a healthcare platform. HIPAA compliance is required.

---

### Common Patterns

#### The Question-Context-Format Pattern
```
[Question]: What are the main differences between SQL and NoSQL databases?
[Context]: I'm choosing a database for a new e-commerce application that needs to handle product catalogs, user sessions, and order transactions.
[Format]: Provide a comparison table followed by a recommendation with reasoning.
```

#### The Task-Input-Output Pattern
```
[Task]: Extract all company names mentioned in the text.
[Input]: "Yesterday, Microsoft announced a partnership with OpenAI, while Google revealed their collaboration with Anthropic on safety research."
[Output Format]: Return as a JSON array of strings.
```

#### The Persona-Situation-Action Pattern
```
[Persona]: You are a senior software architect.
[Situation]: A junior developer has proposed using microservices for a small internal tool with 3 users.
[Action]: Provide constructive feedback on their architectural decision, suggesting alternatives if appropriate.
```

---

### Quick Reference: Basic Prompting Checklist

- [ ] **Clear role/persona** — Who should the model act as?
- [ ] **Specific task** — What exactly should it do?
- [ ] **Input data clearly delimited** — Are inputs separated from instructions?
- [ ] **Output format specified** — How should the response be structured?
- [ ] **Constraints defined** — Length, tone, what to include/exclude?
- [ ] **Context provided** — Audience, purpose, domain?

---

### Notes

Feedback and suggestions are welcome!

**Try these techniques with:**
- [Claude](https://claude.ai)
- [ChatGPT](https://chat.openai.com)
- [Gemini](https://gemini.google.com)
- [Other LLMs via API](https://docs.anthropic.com)