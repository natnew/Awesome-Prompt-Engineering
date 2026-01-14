[← Back: Why AI Code Fails](01_why_ai_code_fails.md) | [Next: Synthesis →](03_synthesis.md)

# Module 2: Review Methodology

A systematic approach to reviewing AI-generated code.

---

## The Review Process

Reviewing AI code is different from reviewing human code. Human code has intent you can ask about. AI code has patterns you must interrogate.

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI CODE REVIEW PROCESS                       │
│                                                                 │
│   1. QUICK SCAN              2. DEEP ANALYSIS                   │
│   ────────────               ──────────────                     │
│   Does it make sense?        Input validation                   │
│   Obvious issues?            Error handling                     │
│   Right structure?           Security                           │
│                              Logic correctness                  │
│                              Performance                        │
│                                                                 │
│   3. VERIFICATION            4. DECISION                        │
│   ────────────               ────────                           │
│   Test edge cases            Ship as-is                         │
│   Trace through              Ship with changes                  │
│   Challenge assumptions      Reject and rewrite                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Quick Scan (30 seconds)

Before diving deep, get the big picture.

### Questions to Answer

1. **Does this code do what was asked?**
   - Read the original prompt/request
   - Does the code address that?
   - Is anything obviously missing?

2. **Is the structure reasonable?**
   - Does the organization make sense?
   - Are functions/classes appropriately sized?
   - Is the naming clear?

3. **Are there obvious issues?**
   - Missing imports?
   - Syntax errors?
   - Undefined variables?

### Quick Scan Red Flags

| Red Flag | What It Suggests |
|:---------|:-----------------|
| Code is much longer than expected | Over-engineered or wrong approach |
| Code is much shorter than expected | Missing functionality or edge cases |
| Unusual library imports | Verify the library is appropriate |
| No error handling visible | Missing error handling |
| Magic numbers | Missing validation or configuration |

### Quick Scan Outcome

After 30 seconds, you should know:
- [ ] This looks reasonable, proceed to deep analysis
- [ ] This has obvious problems, needs rewrite
- [ ] This is the wrong approach entirely

---

## Phase 2: Deep Analysis

Go through the code systematically. Don't rely on intuition.

### Layer 1: Input Handling

**For every input, ask:**

1. What if it's `None`/`null`?
2. What if it's empty?
3. What if it's negative (for numbers)?
4. What if it's very large?
5. Is it user-controlled? (security implications)

**Mark each input as:**
- [ ] Validated
- [ ] Needs validation
- [ ] Inherently safe (e.g., constant)

### Layer 2: Error Handling

**For every operation that can fail, ask:**

1. What exceptions can this throw?
2. Are they caught?
3. Is the catch too broad? (e.g., `except Exception`)
4. What happens after the error?

**Mark error handling as:**
- [ ] Appropriate
- [ ] Too broad
- [ ] Missing
- [ ] Wrong recovery action

### Layer 3: Security

**Check each security concern:**

| Concern | What to Check | Red Flags |
|:--------|:--------------|:----------|
| SQL Injection | User input in queries | String interpolation, concatenation |
| Command Injection | User input in shell commands | `shell=True`, string building |
| Path Traversal | User input in file paths | `..` not blocked, no validation |
| XSS | User input in HTML | No escaping |
| Secrets | Hardcoded credentials | Strings that look like keys/passwords |
| Auth | Access control | Missing permission checks |

### Layer 4: Logic Correctness

**For the core algorithm:**

1. Trace through with a normal input
2. Trace through with boundary inputs (0, 1, max)
3. Verify the algorithm is correct for the problem
4. Check for off-by-one errors in loops

**Questions:**
- What's the expected output for input X?
- Does this code produce that output?
- What happens at the boundaries?

### Layer 5: Performance

**Consider:**

1. What's the time complexity? Is it acceptable?
2. What's the space complexity? Is it acceptable?
3. Are there unnecessary operations inside loops?
4. Are there N+1 query patterns?

**Questions:**
- What happens with 10 items? 1,000? 1,000,000?
- Is this acceptable for expected load?

### Layer 6: Concurrency (if applicable)

**For any shared state, ask:**

1. What happens if two threads access this simultaneously?
2. Is there a read-modify-write pattern without protection?
3. Are there potential deadlocks?

---

## Phase 3: Verification

Don't just read — verify.

### Technique 1: Trace Through

Pick specific inputs and trace through the code manually:

```
Input: [3, 1, 4, 1, 5]
Expected output: ???

Line 1: x = 3
Line 2: y = 1
Line 3: ...
```

Especially trace through:
- Empty input
- Single element
- Boundary values
- A "normal" case

### Technique 2: Test Edge Cases

Actually run the code with:

| Category | Test Cases |
|:---------|:-----------|
| Empty | `""`, `[]`, `{}`, `None` |
| Single | `"a"`, `[1]`, `{"a": 1}` |
| Boundary | `0`, `-1`, `MAX_INT` |
| Special | Unicode, whitespace, newlines |
| Large | 10K elements, long strings |

### Technique 3: Challenge Assumptions

For each assumption the code makes, ask:
- Is this assumption always true?
- When could it be false?
- What happens if it's false?

**Common hidden assumptions:**
- Input is not empty
- Input is sorted
- Input is unique
- Network is available
- File exists
- User is authenticated

### Technique 4: Security Testing

For code handling user input:
- Try `'; DROP TABLE users; --` in text fields
- Try `../../../etc/passwd` in file paths
- Try `<script>alert('xss')</script>` in text that might be rendered

---

## Phase 4: Decision

Based on your review, decide:

### Option 1: Ship As-Is

**Criteria:**
- No issues found
- Confidence is high
- You would be comfortable debugging this at 2 AM

### Option 2: Ship with Changes

**Criteria:**
- Issues found are fixable
- Changes are clear and localized
- Core logic is sound

**Document:**
- What changes you made
- Why you made them
- What you verified after

### Option 3: Reject and Rewrite

**Criteria:**
- Fundamental approach is wrong
- Too many issues to fix
- Would require more effort to fix than rewrite

**Document:**
- Why you rejected it
- What approach you'll take instead

---

## Review Documentation

For non-trivial reviews, document your findings:

```markdown
## Code Review: [Function/Module Name]

**Date:** ____
**Reviewer:** ____
**Source:** AI-generated / Human / Unknown

### Summary
[One paragraph summary of what this code does]

### Issues Found

| # | Severity | Description | Line | Resolution |
|:--|:---------|:------------|:-----|:-----------|
| 1 | Critical | SQL injection | 15 | Fixed |
| 2 | High | Missing null check | 8 | Fixed |
| 3 | Medium | Inefficient algorithm | 20-30 | Noted for future |

### Tests Added
- [ ] Empty input
- [ ] Boundary values
- [ ] Security test cases

### Decision
[ ] Ship as-is
[x] Ship with changes
[ ] Reject

### Confidence: 4/5
[Explanation of confidence level]
```

---

## Building Review Speed

With practice, you'll review faster without sacrificing quality.

### Review Speed Progression

| Experience | Typical Time | Focus |
|:-----------|:-------------|:------|
| Beginner | 15-30 min per 50 lines | Checklist-driven, thorough |
| Intermediate | 5-15 min per 50 lines | Pattern recognition + spot checks |
| Expert | 2-5 min per 50 lines | Rapid pattern matching + targeted deep dives |

### Building Intuition

Over time, you'll develop intuition for:
- Where bugs hide (boundaries, error paths)
- What AI gets wrong (edge cases, security)
- What to trust (simple, well-defined operations)
- What to scrutinize (complex logic, user input handling)

But don't skip verification just because intuition says it's fine. Intuition guides where to look; verification confirms.

---

## Review Anti-Patterns

### Anti-Pattern 1: The Rubber Stamp

**Problem:** "Looks fine" without actually reviewing.

**Fix:** Use a checklist. Don't approve without verifying at least one test case.

### Anti-Pattern 2: The Perfectionist

**Problem:** Spending hours on code that's "good enough."

**Fix:** Prioritize by risk. Ship with known minor issues if they're documented.

### Anti-Pattern 3: The Trust Fall

**Problem:** "AI is smart, it's probably right."

**Fix:** AI is not smart; it's pattern matching. Verify.

### Anti-Pattern 4: The Blame Game

**Problem:** Assuming you can blame AI if something goes wrong.

**Fix:** You approved it. You're responsible. Review accordingly.

---

## Your Task

Before moving to synthesis:

1. **Practice the methodology** on the code samples in the README and extended exercises.

2. **Time yourself** on each review. Note where you spend the most time.

3. **Track your accuracy:**
   - Issues you found
   - Issues you missed (revealed in answers)
   - False positives (things you flagged that weren't issues)

4. **Identify your weaknesses:**
   - What types of issues do you miss?
   - What takes you the longest?
   - What do you need to add to your checklist?

---

[← Back: Why AI Code Fails](01_why_ai_code_fails.md) | [Next: Synthesis →](03_synthesis.md)
