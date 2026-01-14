# Structured Skepticism

*Systematic doubt for AI outputs. Trust, but verify—methodically.*

**Competencies:** [Evaluation & Measurement](../COMPETENCIES.md#2-evaluation--measurement)  
**Source:** [AI Code Review](../projects/core/03_ai_code_review/README.md)

---

## The Problem

AI outputs look confident. They're grammatically correct, well-structured, and plausible. This creates a trust trap: the more professional something looks, the less critically we examine it. But AI systems are optimized for plausibility, not correctness. They generate text that sounds right, which isn't the same as being right.

The deeper problem: our cognitive shortcuts work against us. We're wired to trust fluent, confident communication. AI exploits this unintentionally.

---

## The Solution

**Apply systematic, methodical doubt to AI outputs. Use structured processes that counteract the plausibility bias. Verify categories of issues, not just surface impressions.**

Skepticism isn't distrust—it's a process. You can trust AI to be helpful while verifying its outputs are correct.

---

## How It Works

### The Core Principle

**AI code is optimized for plausibility, not correctness.**

This manifests as:
- Syntactically correct but logically wrong
- Handles happy path, misses edge cases
- Security that looks right but has gaps
- Error handling that's cosmetic, not functional

### The Review Process

#### 1. Resist First Impressions

Don't let fluency create false confidence.

**Wrong approach:**
```
[Read code]
"This looks clean and well-structured. LGTM."
```

**Right approach:**
```
[Read code]
"This looks clean. Now let me systematically check..."
```

#### 2. Use Categories, Not Intuition

Check each category regardless of impressions:

| Category | Key Questions |
|:---------|:--------------|
| **Correctness** | Does it actually do what it claims? |
| **Edge Cases** | What happens with empty, null, huge, negative inputs? |
| **Error Handling** | What happens when things fail? |
| **Security** | What can be exploited? |
| **Performance** | What's the complexity? What scales poorly? |
| **Concurrency** | Is shared state protected? |

#### 3. Trace the Data

Follow data through the code:

```
1. Where does input come from? (Trust boundary)
2. Is it validated before use?
3. How is it transformed?
4. Where does output go?
5. What could go wrong at each step?
```

#### 4. Check the Claims

AI often states things that aren't true:

```
AI says: "This is thread-safe"
Check: Where are the locks? What's protected?

AI says: "This handles all edge cases"
Check: What about null? Empty? Negative? Max int?

AI says: "This is secure"
Check: Against what? SQL injection? XSS? Path traversal?
```

#### 5. Test Mentally or Actually

For each function, think through:
- What's the simplest input? Does it work?
- What's the emptiest input? Does it handle it?
- What's the biggest input? Does it scale?
- What's the weirdest input? Does it validate?

---

## Common AI Failure Patterns

### Pattern 1: Plausible But Wrong

Code looks correct on the surface but has subtle logic errors.

```python
# AI-generated: Find average
def average(numbers):
    return sum(numbers) / len(numbers)

# Problem: Division by zero if numbers is empty
```

**How to catch:** Always check empty/null cases.

### Pattern 2: Confident But Incomplete

Handles the obvious case, misses edge cases.

```python
# AI-generated: Parse date
def parse_date(date_string):
    parts = date_string.split('-')
    return datetime(int(parts[0]), int(parts[1]), int(parts[2]))

# Problems: 
# - No validation of input format
# - No handling of invalid dates (2024-02-31)
# - IndexError if not enough parts
```

**How to catch:** Ask "what could go wrong?"

### Pattern 3: Security Theater

Looks secure but isn't.

```python
# AI-generated: "Secure" authentication
def authenticate(username, password):
    user = db.query(f"SELECT * FROM users WHERE username='{username}'")
    if user and user.password == password:
        return True
    return False

# Problems:
# - SQL injection (unsanitized username)
# - Plain text password comparison
# - Timing attack (early return on no user)
```

**How to catch:** Check every trust boundary.

### Pattern 4: Error Handling Theater

Has try/except but doesn't handle errors meaningfully.

```python
# AI-generated: File operations
def read_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}  # Silently swallow ALL errors

# Problems:
# - Catches everything, including KeyboardInterrupt
# - Returns misleading empty dict on error
# - No logging or notification
```

**How to catch:** Trace what happens when things fail.

### Pattern 5: Concurrency Blindness

Single-threaded thinking in multi-threaded context.

```python
# AI-generated: Rate limiter
class RateLimiter:
    def __init__(self):
        self.requests = {}
    
    def is_allowed(self, user_id):
        now = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = now
            return True
        # Race condition: not thread-safe
```

**How to catch:** Ask "what if this runs twice simultaneously?"

---

## When to Use

**Always use for:**
- Any AI-generated code going to production
- Security-sensitive operations
- Financial or high-stakes logic
- Code that will be maintained long-term

**Especially important when:**
- Time pressure exists (pressure → less scrutiny)
- Code is complex
- You're not expert in the domain
- Stakes are high

---

## When NOT to Use

- Throwaway prototypes
- Learning exercises where correctness doesn't matter
- When you'll manually test everything anyway

Even then, building the habit serves you well.

---

## Checklists

### Quick Review (5 minutes)

- [ ] Does it solve the stated problem?
- [ ] What happens with empty input?
- [ ] Are errors handled or silently swallowed?
- [ ] Is there any user input used without validation?

### Standard Review (15 minutes)

All of quick review, plus:
- [ ] Trace input from entry to use
- [ ] Verify each claim the AI makes
- [ ] Check for hardcoded values that should be configurable
- [ ] Look for magic numbers without explanation
- [ ] Verify types are handled correctly

### Security-Focused Review (30 minutes)

All of standard review, plus:
- [ ] Identify all trust boundaries
- [ ] Check SQL queries for injection
- [ ] Check file paths for traversal
- [ ] Check URLs for SSRF
- [ ] Check for hardcoded secrets
- [ ] Verify authentication/authorization
- [ ] Check for timing vulnerabilities

---

## Building the Skill

### Track Your Blind Spots

Keep a log of issues you missed:

| Date | Issue Missed | Category | Why I Missed It |
|:-----|:-------------|:---------|:----------------|
| | | | |

Review periodically. Patterns will emerge.

### Calibrate Over Time

After reviews, check what you found vs. what testing found. Adjust focus to your weaknesses.

### Practice on Known-Bad Code

Review intentionally buggy code. Check your hit rate. The [AI Code Review project](../projects/core/03_ai_code_review/README.md) provides samples.

---

## Anti-Patterns

### Checkbox Review

**What happens:** Go through checklist mechanically without thinking. Check boxes, miss issues.

**Fix:** Checklists guide attention, not replace thought.

### Trust The Tests

**What happens:** "Tests pass, so it's correct." But tests don't cover edge cases either.

**Fix:** Review tests too. Are they testing the right things?

### Expertise Assumption

**What happens:** "I'm not a security expert, so I'll skip that." AI doesn't know you'll skip it.

**Fix:** Check anyway. Use checklists. Flag for expert review.

### Fatigue-Driven Approval

**What happens:** After 10 files, scrutiny drops. "This one looks fine."

**Fix:** Recognize fatigue. Take breaks. Review most critical code first.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Catches AI errors | Takes time |
| Builds verification skills | Can feel slow |
| Reduces downstream bugs | Requires discipline |
| Creates defensible process | May feel distrustful |

---

## Implementation Checklist

- [ ] Review process defined (which checklist for which code)
- [ ] Time allocated for review (not squeezed)
- [ ] Blind spot tracking active
- [ ] Regular practice on known-bad examples
- [ ] Escalation path for uncertain cases

---

## Related Patterns

- **[Evaluation-First](evaluation_first.md)** — Define what correct means before checking
- **[Defense in Depth](defense_in_depth.md)** — Review as one defensive layer
- **[Confidence-Weighted](confidence_weighted.md)** — How confident are you in your review?

---

## Key Insight

> "The problem isn't that AI is untrustworthy. It's that AI's failures are plausible-looking. Skepticism is the tool that surfaces them."

Structured skepticism isn't distrust—it's the discipline to verify what looks trustworthy.
