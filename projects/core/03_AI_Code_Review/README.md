[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Projects Overview](../00_overview.md) | [Competencies](../../Competencies.md)

# Project 3: AI Code Review Exercise

## The Challenge

AI can write code. The question is: **should you trust it?**

AI-generated code looks correct. It compiles. It often runs. But it can contain subtle bugs, security vulnerabilities, inefficiencies, and logic errors that are easy to miss — especially because the code looks plausible.

This project develops your judgment: the ability to critically review AI-generated code and know when to trust, verify, or reject it.

---

## What You'll Do

This is a different kind of project. Instead of building something, you'll practice **critical evaluation**.

1. **Review AI-generated code** with intentional flaws (some obvious, some subtle)
2. **Identify issues** across multiple categories (correctness, security, style)
3. **Document your findings** with reasoning
4. **Create a personal checklist** for reviewing AI code
5. **Reflect on your blind spots**

---

## Competencies Developed

| Competency | Emphasis | What You'll Practice |
|:-----------|:--------:|:---------------------|
| **AI Output Review** | ●●● | Critically evaluating AI-generated content |
| **Evaluation & Measurement** | ●● | Systematic quality assessment |
| **Governance** | ● | Documentation and decision-making |

---

## Prerequisites

- Proficiency in at least one programming language (Python recommended)
- Experience reading others' code
- Basic understanding of common security vulnerabilities

---

## Time Estimate

| Depth | Time | What You'll Produce |
|:------|:-----|:--------------------|
| **Minimum** | 2-3 hours | Review 5 code samples, basic checklist |
| **Recommended** | 4-6 hours | Review 10 samples, detailed checklist with categories |
| **Deep Dive** | 8-10 hours | Full review set, comprehensive checklist, blind spot analysis |

---

## The Code Review Set

You'll review code across these categories:

### Category 1: Correctness Issues

Code that runs but produces wrong results:
- Off-by-one errors
- Incorrect edge case handling
- Wrong algorithm choice
- Logic errors

### Category 2: Security Vulnerabilities

Code with security problems:
- SQL injection vulnerabilities
- Path traversal
- Insecure deserialization
- Missing input validation

### Category 3: Performance Issues

Code that works but is inefficient:
- Unnecessary complexity
- Memory leaks
- N+1 query patterns
- Redundant operations

### Category 4: Maintainability Issues

Code that works but is hard to maintain:
- Poor naming
- Missing error handling
- Tight coupling
- No documentation

### Category 5: Subtle Issues

The hardest to catch:
- Race conditions
- Floating point errors
- Timezone bugs
- Unicode handling

---

## Review Exercise 1: The Functions

Review each function. Identify ALL issues. Rate your confidence.

### Sample 1: Calculate Average

```python
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
```

**Your Review:**
- Issues found: 
- Severity (Critical/High/Medium/Low):
- Confidence (1-5):
- What would you change:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Division by zero** (Critical): If `numbers` is empty, raises ZeroDivisionError
2. **No type checking** (Medium): Fails silently on non-numeric inputs
3. **No None check** (Medium): Fails on None input

**Correct version:**
```python
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0  # or raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```
</details>

---

### Sample 2: User Authentication

```python
def authenticate_user(username, password, db_connection):
    """Check if username and password match database records."""
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = db_connection.execute(query)
    return result.fetchone() is not None
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:
- What would you change:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **SQL Injection** (Critical): String interpolation allows injection attacks
2. **Plain text password** (Critical): Passwords should be hashed
3. **No input validation** (High): Username/password not sanitized
4. **Timing attack vulnerable** (Medium): Constant-time comparison not used

**Correct version:**
```python
def authenticate_user(username, password, db_connection):
    """Check if username and password match database records."""
    query = "SELECT password_hash FROM users WHERE username = ?"
    result = db_connection.execute(query, (username,))
    row = result.fetchone()
    if row is None:
        return False
    return bcrypt.checkpw(password.encode(), row['password_hash'])
```
</details>

---

### Sample 3: Find Duplicates

```python
def find_duplicates(items):
    """Find all duplicate items in a list."""
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                if items[i] not in duplicates:
                    duplicates.append(items[i])
    return duplicates
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:
- What would you change:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **O(n²) complexity** (High): Should be O(n) with a set/counter
2. **Redundant comparisons** (Medium): Checks each pair twice
3. **Linear search in duplicates** (Medium): Should use set for O(1) lookup

**Correct version:**
```python
def find_duplicates(items):
    """Find all duplicate items in a list."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
```
</details>

---

### Sample 4: Parse Date

```python
def parse_date(date_string):
    """Parse a date string in format YYYY-MM-DD."""
    parts = date_string.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    return datetime(year, month, day)
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:
- What would you change:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **No input validation** (High): Doesn't verify format
2. **Index error risk** (High): If string doesn't have 3 parts
3. **No error handling** (High): ValueError on non-numeric parts
4. **Missing import** (Low): datetime not imported in snippet
5. **Ignores validation** (Medium): Doesn't check valid date (e.g., month 13)

**Correct version:**
```python
from datetime import datetime

def parse_date(date_string):
    """Parse a date string in format YYYY-MM-DD."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_string}. Expected YYYY-MM-DD") from e
```
</details>

---

### Sample 5: Rate Limiter

```python
class RateLimiter:
    """Simple rate limiter that allows N requests per minute."""
    
    def __init__(self, max_requests):
        self.max_requests = max_requests
        self.requests = []
    
    def allow_request(self):
        now = time.time()
        # Remove requests older than 1 minute
        self.requests = [r for r in self.requests if now - r < 60]
        
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False
```

**Your Review:**
- Issues found:
- Severity:
- Confidence:
- What would you change:

<details>
<summary>Click to reveal issues</summary>

**Issues:**
1. **Not thread-safe** (Critical): Race condition between check and append
2. **Memory grows unbounded** (Medium): Under high load, list grows before cleanup
3. **Cleanup on every request** (Medium): Inefficient under load
4. **Time resolution** (Low): time.time() precision varies by platform

**Correct version:**
```python
import threading
import time
from collections import deque

class RateLimiter:
    """Thread-safe rate limiter that allows N requests per minute."""
    
    def __init__(self, max_requests):
        self.max_requests = max_requests
        self.requests = deque()
        self.lock = threading.Lock()
    
    def allow_request(self):
        now = time.time()
        with self.lock:
            # Remove old requests
            while self.requests and now - self.requests[0] >= 60:
                self.requests.popleft()
            
            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True
            return False
```
</details>

---

## Review Exercise 2: Larger Code Block

Review this more complex code sample:

```python
import json
import os

class ConfigManager:
    """Manages application configuration from file."""
    
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}
        self.load()
    
    def load(self):
        """Load configuration from file."""
        with open(self.config_path) as f:
            self.config = json.load(f)
    
    def get(self, key, default=None):
        """Get a configuration value."""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value == default:
                break
        return value
    
    def set(self, key, value):
        """Set a configuration value and save."""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value
        self.save()
    
    def save(self):
        """Save configuration to file."""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f)
```

**Your Review:**

List ALL issues you find:

| Issue | Line(s) | Severity | Description |
|:------|:--------|:---------|:------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

<details>
<summary>Click to reveal issues (10 issues)</summary>

1. **No file existence check** (High): `load()` will crash if file doesn't exist
2. **No error handling in load** (High): Invalid JSON crashes silently  
3. **Path traversal risk** (High): `config_path` not validated
4. **No file locking** (Medium): Race condition on concurrent access
5. **`get()` logic error** (High): If intermediate key doesn't exist, returns default prematurely
6. **`get()` type assumption** (Medium): Assumes all intermediate values are dicts
7. **`set()` with empty key** (Medium): `keys[-1]` fails on empty string
8. **`save()` not atomic** (Medium): Partial write on failure corrupts file
9. **No encoding specified** (Low): Should specify UTF-8
10. **Not thread-safe** (Medium): Multiple threads could corrupt state
</details>

---

## Building Your Checklist

Based on your review experience, create a checklist for reviewing AI-generated code.

### Checklist Template

```markdown
# AI Code Review Checklist

## Before Running the Code

### Quick Scan (30 seconds)
- [ ] Does the code do what was asked?
- [ ] Are there obvious syntax errors?
- [ ] Are all imports present?

### Input Validation
- [ ] Are all inputs validated?
- [ ] Are edge cases handled (null, empty, negative)?
- [ ] Are there any injection vulnerabilities?

### Error Handling
- [ ] Are exceptions caught appropriately?
- [ ] Are error messages helpful?
- [ ] Does the code fail gracefully?

### Security
- [ ] Is user input sanitized?
- [ ] Are there SQL/command injection risks?
- [ ] Are secrets handled properly?
- [ ] Is authentication/authorization correct?

### Logic
- [ ] Are boundary conditions correct?
- [ ] Are loops terminating correctly?
- [ ] Is the algorithm appropriate for the data size?

### Concurrency (if applicable)
- [ ] Is shared state protected?
- [ ] Are there race conditions?
- [ ] Is the code thread-safe?

### Performance
- [ ] Is the complexity reasonable?
- [ ] Are there unnecessary operations?
- [ ] Is memory usage appropriate?

## While Testing
- [ ] Does it work with normal inputs?
- [ ] Does it handle edge cases?
- [ ] Does it fail appropriately on bad inputs?

## Meta-Review
- [ ] Would I be comfortable shipping this?
- [ ] What could still be wrong that I didn't check?
```

---

## Your Task: Complete the Exercise

### Step 1: Review All Samples

Work through each code sample:
- Identify issues before looking at answers
- Rate your confidence
- Note what you missed

### Step 2: Track Your Accuracy

| Sample | Issues Found | Issues Missed | False Positives |
|:-------|:-------------|:--------------|:----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

### Step 3: Identify Patterns

What types of issues did you miss most often?
- [ ] Security issues
- [ ] Edge cases
- [ ] Performance issues
- [ ] Logic errors
- [ ] Concurrency issues

### Step 4: Create Your Checklist

Based on what you missed, customize the checklist template:
- Add checks for your blind spots
- Remove checks that don't apply to your domain
- Prioritize by severity

### Step 5: Test Your Checklist

Find AI-generated code (from Copilot, ChatGPT, etc.) and apply your checklist. Did it help you catch issues?

---

## Reflection Questions

1. **What was the hardest type of issue to catch?**

2. **What made you trust code that was actually wrong?**

3. **How would you explain "plausible but wrong" to someone else?**

4. **When should you NOT use AI-generated code?**

5. **How should your review process differ for AI vs. human code?**

---

## Key Insight

**AI code is optimized for plausibility, not correctness.**

AI generates code that:
- Compiles and runs
- Looks like code you've seen before
- Follows common patterns
- Has reasonable variable names

But it may not:
- Handle edge cases
- Be secure
- Be efficient
- Actually solve your problem

Your job is to bridge the gap between "looks right" and "is right."

---

## Artifacts

### Required
- [ ] Completed reviews for all code samples
- [ ] Personal checklist (customized)
- [ ] Blind spot analysis

### Optional
- [ ] Additional code samples reviewed
- [ ] Checklist tested on real AI code
- [ ] Documentation of review process

---

## What You've Learned

After completing this project, you should be able to:

- [ ] Review AI-generated code with appropriate skepticism
- [ ] Identify common AI code failure patterns
- [ ] Use a systematic checklist for reviews
- [ ] Know when AI code needs extra scrutiny
- [ ] Explain the difference between plausibility and correctness

---

**What's Next?**

- [Cost-Benefit Analysis](../04_cost_benefit_analysis/) — Decision-making about AI features
- [Agent with Guardrails](../02_agent_with_guardrails/) — Apply critical review to agent outputs
- Return to [Projects Overview](../00_overview.md)

---

*Project completed: [DATE]*

*Key insight: [ONE SENTENCE]*
