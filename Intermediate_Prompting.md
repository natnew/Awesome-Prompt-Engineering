---
layout: default
title: Intermediate Prompting
description: Reasoning techniques including Chain-of-Thought and Few-Shot.
nav_order: 3
---

[Home](https://natnew.github.io/Awesome-Prompt-Engineering/)

## Intermediate Prompting

Intermediate prompting techniques enable language models to tackle more complex tasks that require reasoning, examples, and structured thinking. These methods bridge the gap between simple instructions and advanced agentic patterns, and are essential for building reliable AI applications.

The techniques covered here focus on improving accuracy, consistency, and reasoning quality through strategic prompt design.

---

### Few-Shot Prompting

Few-shot prompting provides the model with examples of the desired input-output pattern before asking it to perform the task. This is one of the most effective techniques for improving output quality and consistency.

#### Basic Few-Shot Pattern
```
Classify the sentiment of customer reviews as positive, negative, or neutral.

Review: "Absolutely love this product! Best purchase I've made all year."
Sentiment: positive

Review: "It works okay, nothing special but gets the job done."
Sentiment: neutral

Review: "Broke after two days. Complete waste of money."
Sentiment: negative

Review: "The delivery was fast but the packaging was damaged. Product itself is fine."
Sentiment:
```

#### Few-Shot for Format Consistency
```
Convert natural language queries to SQL.

Question: "How many users signed up last month?"
SQL: SELECT COUNT(*) FROM users WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);

Question: "What are the top 5 products by revenue?"
SQL: SELECT product_name, SUM(revenue) as total_revenue FROM sales GROUP BY product_name ORDER BY total_revenue DESC LIMIT 5;

Question: "Which customers haven't made a purchase in 90 days?"
SQL:
```

#### Few-Shot with Reasoning
```
Determine if the conclusion logically follows from the premise.

Premise: "All mammals are warm-blooded. Whales are mammals."
Conclusion: "Whales are warm-blooded."
Analysis: The conclusion follows logically. If all mammals are warm-blooded (major premise) and whales are mammals (minor premise), then whales must be warm-blooded.
Answer: Valid

Premise: "Some birds can fly. Penguins are birds."
Conclusion: "Penguins can fly."
Analysis: The conclusion does not follow. "Some birds can fly" doesn't mean all birds can fly. Penguins being birds doesn't guarantee they can fly.
Answer: Invalid

Premise: "All prime numbers greater than 2 are odd. 17 is a prime number greater than 2."
Conclusion: "17 is odd."
Analysis:
```

---

### Chain-of-Thought (CoT) Prompting

Chain-of-thought prompting encourages the model to break down complex problems into intermediate reasoning steps, significantly improving accuracy on tasks requiring logic, math, or multi-step reasoning.

#### Explicit CoT Request
```
Solve this problem step by step:

A store sells notebooks for $4 each and pens for $2 each. Maria bought some notebooks 
and pens for a total of $26. If she bought 4 notebooks, how many pens did she buy?

Think through this step by step before giving your final answer.
```

**Model Response Pattern:**
```
Let me solve this step by step:

Step 1: Calculate the cost of notebooks
- Maria bought 4 notebooks at $4 each
- Cost of notebooks = 4 × $4 = $16

Step 2: Calculate remaining money for pens
- Total spent = $26
- Remaining for pens = $26 - $16 = $10

Step 3: Calculate number of pens
- Each pen costs $2
- Number of pens = $10 ÷ $2 = 5

Answer: Maria bought 5 pens.
```

#### CoT for Code Debugging
```
Debug the following code. Think through what each line does and identify where the bug is:

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

result = calculate_average([])
print(result)

Walk through the execution step by step, then explain the bug and provide a fix.
```

---

### Zero-Shot Chain-of-Thought

Zero-shot CoT uses a simple trigger phrase to encourage reasoning without providing examples. Simply adding "Let's think step by step" or "Let's work through this" can significantly improve performance.

#### The Magic Phrase
```
The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, 
how many apples do they have?

Let's think step by step.
```

#### Zero-Shot CoT for Analysis
```
A company's revenue increased by 15% in Q1, decreased by 10% in Q2, and increased 
by 20% in Q3. If they started with $1,000,000 in revenue, what was their Q3 ending revenue?

Let's work through this carefully, calculating each quarter's revenue.
```

#### Zero-Shot CoT for Decision Making
```
Should a startup with $500K runway, 3 engineers, and a B2B SaaS product focus on 
adding new features or improving existing ones?

Let's reason through this systematically, considering the tradeoffs.
```

---

### Self-Consistency

Self-consistency improves reliability by generating multiple reasoning paths and selecting the most common answer. This is particularly useful for problems where the model might make errors.

#### Conceptual Approach
```
I'll ask you to solve this problem 3 times with different reasoning approaches. 
Then we'll check if the answers agree.

Problem: A train travels from City A to City B at 60 mph, then returns at 40 mph. 
What is the average speed for the round trip?

Approach 1: Solve using the harmonic mean formula.
Approach 2: Solve by assuming a specific distance and calculating total time.
Approach 3: Solve using algebraic variables.

After all three approaches, state whether the answers are consistent and provide 
the final answer.
```

#### Self-Consistency for Classification
```
Classify this email as spam or not spam. Provide three independent analyses 
considering different aspects:

Email: "Congratulations! You've been selected for a $1000 gift card. Click here 
to claim within 24 hours. This offer expires soon!"

Analysis 1: Examine the language and urgency signals.
Analysis 2: Consider the sender's claims and what they're asking for.
Analysis 3: Compare to known spam patterns.

Final classification (based on majority of analyses):
```

---

### Step-Back Prompting

Step-back prompting asks the model to first consider the broader context, principles, or concepts before tackling the specific problem. This improves performance on complex questions.

#### Step-Back for Technical Questions
```
Question: Why does adding salt to ice make it colder?

Before answering directly, first step back and answer:
- What are the general principles of freezing point depression?
- What happens at the molecular level when salt dissolves in water?

Then use these principles to explain the specific phenomenon.
```

#### Step-Back for Strategy Questions
```
Question: Should our company adopt a microservices architecture?

Before answering directly, first step back and consider:
- What are the general principles of software architecture decisions?
- What factors typically determine whether microservices is appropriate?
- What are the organizational prerequisites for microservices success?

Then apply these principles to provide a framework for the decision.
```

---

### Least-to-Most Prompting

Least-to-most prompting breaks complex problems into simpler subproblems, solving them in order of increasing difficulty. Each solution builds on the previous ones.

#### Example: Complex Calculation
```
Problem: Calculate the compound interest on $10,000 at 5% annual rate, 
compounded quarterly, for 3 years.

Let's break this into subproblems:

Subproblem 1 (easiest): What is the quarterly interest rate?
Subproblem 2: How many compounding periods are there in 3 years?
Subproblem 3: What is the compound interest formula?
Subproblem 4 (hardest): Apply the formula and calculate the final amount.

Solve each subproblem in order, using previous answers to help with later ones.
```

#### Example: Code Generation
```
Build a Python function that validates an email address.

Let's break this into subproblems:

Subproblem 1: What are the basic rules for a valid email format?
Subproblem 2: Write a regex pattern for the local part (before @).
Subproblem 3: Write a regex pattern for the domain part (after @).
Subproblem 4: Combine into a complete validation function with error handling.

Solve each subproblem, building up to the final solution.
```

---

### Structured Reasoning with Tags

Using XML or markdown structure helps organize complex reasoning and makes outputs more parseable.

#### Structured Analysis Template
```
Analyze the following business proposal using this structure:

<proposal>
Launch a subscription meal-kit service targeting busy professionals in urban areas.
Initial investment: $500,000. Target market: 25-45 year olds in cities over 1M population.
</proposal>

Provide your analysis in this format:

<analysis>
  <strengths>
  [List 3-4 strengths of the proposal]
  </strengths>
  
  <weaknesses>
  [List 3-4 weaknesses or risks]
  </weaknesses>
  
  <assumptions>
  [What assumptions is this proposal making?]
  </assumptions>
  
  <recommendation>
  [Your overall recommendation with reasoning]
  </recommendation>
</analysis>
```

#### Structured Code Review
```
Review the following code using this framework:

<code>
def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] > 0:
            result.append(data[i] * 2)
    return result
</code>

<review>
  <correctness>[Does it work correctly?]</correctness>
  <efficiency>[Are there performance concerns?]</efficiency>
  <readability>[Is it easy to understand?]</readability>
  <improvements>[Suggested refactoring]</improvements>
  <refactored_code>[Improved version]</refactored_code>
</review>
```

---

### Instruction Extraction

Converting unstructured text into structured instructions or steps—useful for processing procedures, recipes, and documentation.

#### Example
```
Extract step-by-step instructions from the following text. If the text doesn't 
contain a clear sequence of instructions, respond with "No sequential instructions found."

Text:
"""
To deploy your application, you first need to ensure all tests pass locally. 
After that, commit your changes and push to the main branch. The CI pipeline 
will automatically run. Once it passes, create a pull request for review. 
After approval, merge the PR, which triggers the deployment to staging. 
Verify everything works in staging, then promote to production using the 
deploy script.
"""

Format your response as:
Step 1: [action]
Step 2: [action]
...
```

---

### Quick Reference: When to Use Each Technique

| Technique | Best For | Example Use Case |
|-----------|----------|------------------|
| **Few-Shot** | Consistent formatting, classification | Sentiment analysis, data extraction |
| **Chain-of-Thought** | Math, logic, multi-step reasoning | Word problems, debugging |
| **Zero-Shot CoT** | Quick reasoning boost | Any complex question |
| **Self-Consistency** | High-stakes decisions | Medical, financial, legal analysis |
| **Step-Back** | Questions requiring principles | Architecture decisions, science explanations |
| **Least-to-Most** | Complex multi-part problems | Code generation, complex calculations |
| **Structured Reasoning** | Parseable outputs, analysis | Business analysis, code review |

---

### Notes

Feedback and suggestions are welcome!

These techniques can be combined—for example, few-shot examples with chain-of-thought reasoning, or step-back prompting followed by structured output.

**Try these techniques with:**
- [Claude](https://claude.ai)
- [ChatGPT](https://chat.openai.com)
- [Gemini](https://gemini.google.com)