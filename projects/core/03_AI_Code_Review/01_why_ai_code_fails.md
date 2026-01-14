[← Back to Project](README.md) | [Next: Review Methodology →](02_review_methodology.md)

# Module 1: Why AI Code Fails

Understanding failure patterns helps you catch them.

---

## The Fundamental Problem

AI-generated code is optimized for **plausibility**, not **correctness**.

Language models learn patterns from vast amounts of code. They produce code that:
- Looks like code they've seen before
- Uses common idioms and patterns
- Has reasonable structure and naming
- Compiles and often runs

But the model doesn't "understand" code the way you do. It doesn't:
- Execute the code mentally
- Reason about edge cases systematically
- Know your specific requirements
- Understand your production environment

This creates a dangerous gap: code that **looks right** but **isn't right**.

---

## Failure Pattern Categories

### Pattern 1: The Confident Wrong Answer

**What it looks like:** Clean, well-structured code that produces incorrect results.

**Why it happens:** The model learned a pattern that's similar but not identical to what's needed. It generates confidently because the pattern is familiar.

**Example:**
```python
# AI-generated: Calculate business days between two dates
def business_days_between(start, end):
    days = (end - start).days
    weeks = days // 7
    remaining = days % 7
    
    # Subtract weekends
    return days - (weeks * 2)  # WRONG: doesn't account for start day
```

**How to catch:** Trace through with specific examples, especially edge cases.

---

### Pattern 2: The Missing Edge Case

**What it looks like:** Code that works for common inputs but fails on boundaries.

**Why it happens:** Training data contains mostly "happy path" code. Edge cases are underrepresented.

**Common missing edge cases:**
- Empty input (empty string, empty list, None)
- Single element (list of one, string of one character)
- Maximum/minimum values
- Zero and negative numbers
- Unicode and special characters
- Very large inputs

**Example:**
```python
# AI-generated: Find the most common element
def most_common(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)  # CRASH: empty list
```

**How to catch:** Always test with empty input, single element, and boundary values.

---

### Pattern 3: The Security Blind Spot

**What it looks like:** Functional code with security vulnerabilities.

**Why it happens:** Security is about what *shouldn't* happen. Models optimize for what *should* happen.

**Common vulnerabilities:**
- SQL injection (string interpolation in queries)
- Command injection (shell=True with user input)
- Path traversal (user input in file paths)
- Missing authentication/authorization
- Hardcoded secrets
- Insecure deserialization

**Example:**
```python
# AI-generated: Search users by name
def search_users(db, name):
    query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"  # SQL INJECTION
    return db.execute(query).fetchall()
```

**How to catch:** Flag any user input flowing into SQL, shell commands, file paths, or HTML.

---

### Pattern 4: The Plausible Algorithm

**What it looks like:** Code that implements an algorithm that seems right but isn't optimal or correct for the problem.

**Why it happens:** The model matches pattern to pattern, not problem to solution. It might use an algorithm from a similar problem that doesn't apply.

**Example:**
```python
# AI-generated: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # INEFFICIENT: should be sqrt(n)
        if n % i == 0:
            return False
    return True
```

Or worse:
```python
# AI-generated: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True  # Looks right... but is it? (It actually is, but would you bet on it?)
```

**How to catch:** Verify the algorithm is correct for your requirements. Don't trust that it's optimal.

---

### Pattern 5: The Concurrency Nightmare

**What it looks like:** Code that works in single-threaded tests but fails in production.

**Why it happens:** Concurrency bugs are rare in training data because most code is single-threaded or the concurrency is hidden in frameworks.

**Common issues:**
- Race conditions
- Missing locks
- Deadlocks
- Thread-unsafe data structures
- Shared mutable state

**Example:**
```python
# AI-generated: Simple counter
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1  # NOT THREAD-SAFE: read-modify-write race
    
    def get(self):
        return self.count
```

**How to catch:** Ask "what happens if two threads call this simultaneously?"

---

### Pattern 6: The Library Misuse

**What it looks like:** Code that uses a library incorrectly or unsafely.

**Why it happens:** The model has seen many uses of the library, but not all uses are correct. It may combine patterns that don't work together.

**Example:**
```python
# AI-generated: Parse YAML config
import yaml

def load_config(path):
    with open(path) as f:
        return yaml.load(f)  # UNSAFE: yaml.load can execute arbitrary code
```

**How to catch:** Know your libraries' security implications. When in doubt, check the docs.

---

### Pattern 7: The Subtle Logic Error

**What it looks like:** Code that's almost right, with a small error that's hard to spot.

**Why it happens:** These are the hardest to catch because the code looks correct at a glance.

**Common subtle errors:**
- Off-by-one errors
- Wrong comparison operator (< vs <=)
- Incorrect variable in expression
- Wrong return value
- Inverted condition

**Example:**
```python
# AI-generated: Binary search
def binary_search(arr, target):
    left, right = 0, len(arr)  # SUBTLE: should be len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  # SUBTLE: with right = len(arr), this is wrong
    return -1
```

**How to catch:** Trace through with specific examples. Test boundary conditions exhaustively.

---

## The Trust Spectrum

Not all AI code needs the same scrutiny:

| Scenario | Trust Level | Review Intensity |
|:---------|:------------|:-----------------|
| Prototype/exploration | Higher | Light |
| Internal tool | Medium | Standard |
| Production, non-critical | Lower | Thorough |
| Production, critical | Lowest | Exhaustive |
| Security-sensitive | Lowest | Exhaustive + expert review |
| Safety-critical | Do not use | N/A |

**Rule of thumb:** The more consequential the failure, the less you should trust AI code.

---

## Why "It Works" Isn't Enough

"I tested it and it works" is not sufficient because:

1. **You tested the happy path.** Edge cases are where bugs hide.
2. **Your test environment isn't production.** Concurrency, scale, real data.
3. **You tested what you expected.** Security bugs come from unexpected inputs.
4. **You tested now.** What about when requirements change?

"It works" means "it worked for the tests I thought to run."

---

## Your Task

Before moving to the review exercises, reflect:

1. **Which failure pattern are you most likely to miss?**

2. **What's your testing blind spot?** (Edge cases? Security? Concurrency?)

3. **What would make you trust AI code more or less?**

4. **What's the worst bug you've ever shipped? Would AI code review have caught it?**

---

## Key Insight

**AI code is optimized for plausibility, not correctness.**

Your job as a reviewer is to bridge that gap — to verify that plausible code is actually correct code.

---

[← Back to Project](README.md) | [Next: Review Methodology →](02_review_methodology.md)
