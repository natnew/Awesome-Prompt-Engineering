# Code Review Checklist Template

## Overview

**Purpose:** Systematic checklist for reviewing AI-generated or AI-assisted code.

**When to use:** Any code review, especially for AI-generated code.

**Competencies:** [AI Output Review](../../COMPETENCIES.md#2-evaluation--measurement)

---

# Code Review Checklist

**Reviewer:** [Name]  
**Date:** YYYY-MM-DD  
**Code:** [PR/file reference]  
**AI-Generated:** Yes / No / Partially

---

## Quick Scan (30 seconds)

First impressions before deep review.

- [ ] Does the code attempt to solve the right problem?
- [ ] Are there obvious syntax errors?
- [ ] Are all necessary imports present?
- [ ] Does the overall structure make sense?
- [ ] Is there anything that looks "off"?

**Initial impression:** ✅ Looks reasonable / ⚠️ Has concerns / ❌ Major issues

---

## Correctness

### Logic

- [ ] Does the algorithm correctly solve the problem?
- [ ] Are boundary conditions handled? (off-by-one, empty, null)
- [ ] Are comparisons correct? (< vs <=, == vs ===)
- [ ] Do loops terminate in all cases?
- [ ] Are recursive base cases correct?
- [ ] Is the return value correct in all paths?

### Types & Data

- [ ] Are types used correctly?
- [ ] Are type conversions safe?
- [ ] Are nullable values handled?
- [ ] Are collections iterated safely?

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Input Handling

### Validation

- [ ] Are all inputs validated before use?
- [ ] Are there type checks where needed?
- [ ] Are null/None/undefined values handled?
- [ ] Are empty collections handled?

### Edge Cases Tested

- [ ] Empty input (`[]`, `""`, `{}`, `None`)
- [ ] Single element input
- [ ] Very large input
- [ ] Negative numbers (if applicable)
- [ ] Special characters / Unicode
- [ ] Boundary values (0, -1, MAX_INT)

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Error Handling

- [ ] Are exceptions caught at appropriate levels?
- [ ] Are error messages helpful and specific?
- [ ] Does the code fail gracefully?
- [ ] Are errors logged appropriately?
- [ ] Are resources cleaned up in error cases? (finally blocks)
- [ ] Is there a catch-all for unexpected errors?

### Specific Checks

- [ ] File operations: FileNotFoundError handled?
- [ ] Network operations: Timeouts and connection errors?
- [ ] Database operations: Connection failures?
- [ ] API calls: Rate limits and service errors?

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Security

### Input Sanitization

- [ ] Is user input sanitized before use?
- [ ] SQL queries use parameterization? (No string interpolation)
- [ ] Shell commands avoid user input? (Or properly escaped)
- [ ] File paths are validated? (No path traversal)
- [ ] HTML output is escaped? (No XSS)
- [ ] URLs are validated? (No SSRF)

### Authentication & Authorization

- [ ] Credentials not hardcoded?
- [ ] Auth checked before sensitive operations?
- [ ] Permissions verified?
- [ ] Tokens/sessions handled securely?

### Data Protection

- [ ] Sensitive data encrypted when needed?
- [ ] PII handled appropriately?
- [ ] Secrets not logged or exposed in errors?
- [ ] Secure random used for security purposes?

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Performance

### Complexity

- [ ] Is time complexity appropriate for the use case?
- [ ] Is space complexity acceptable?
- [ ] Are there unnecessary nested loops?
- [ ] Are there redundant operations?

### Resource Usage

- [ ] Are connections/handles closed?
- [ ] Are there potential memory leaks?
- [ ] Is caching used appropriately?
- [ ] Are there N+1 query patterns?

### Patterns to Watch

- [ ] String concatenation in loops (use StringBuilder/join)
- [ ] Repeated expensive operations (cache results)
- [ ] Loading entire files into memory (stream instead)
- [ ] Synchronous operations that could be async

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Concurrency (If Applicable)

- [ ] Is shared state protected by locks?
- [ ] Are there potential race conditions?
- [ ] Are there potential deadlocks?
- [ ] Are atomic operations used where needed?
- [ ] Is thread-safe data structures used?
- [ ] Are resources released in finally blocks?

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Maintainability

### Readability

- [ ] Are names descriptive and consistent?
- [ ] Is the code self-documenting?
- [ ] Are complex sections commented?
- [ ] Is formatting consistent with codebase?

### Structure

- [ ] Are functions focused (single responsibility)?
- [ ] Is the code DRY (no unnecessary duplication)?
- [ ] Are dependencies explicit?
- [ ] Is the code testable?

### Documentation

- [ ] Are public functions documented?
- [ ] Are non-obvious behaviors explained?
- [ ] Are assumptions documented?
- [ ] Are examples provided where helpful?

**Issues found:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## AI-Specific Concerns

If this code was AI-generated:

- [ ] Does it actually solve the stated problem? (Not just look like it)
- [ ] Are there "plausible but wrong" patterns?
- [ ] Are standard library functions used correctly?
- [ ] Are there hallucinated APIs or methods?
- [ ] Is error handling real or cosmetic?
- [ ] Are security measures actual or theater?

**AI-specific issues:**
- [ ] _[Issue 1]_
- [ ] _[Issue 2]_

---

## Testing

- [ ] Are there tests for this code?
- [ ] Do tests cover happy path?
- [ ] Do tests cover edge cases?
- [ ] Do tests cover error cases?
- [ ] Are tests actually testing the right things?

**Missing tests:**
- [ ] _[Test case 1]_
- [ ] _[Test case 2]_

---

## Summary

### Issues by Severity

| Severity | Count | Issues |
|:---------|:------|:-------|
| Critical | | |
| High | | |
| Medium | | |
| Low | | |

### Recommendation

- [ ] **Approve** — Ready to merge
- [ ] **Approve with comments** — Minor issues, can merge
- [ ] **Request changes** — Must address issues before merge
- [ ] **Reject** — Fundamental problems, needs rewrite

### Key Feedback

_[Most important points for the author]_

1. _[Point 1]_
2. _[Point 2]_
3. _[Point 3]_

---

## Personal Notes

### Issues I Almost Missed

_[Track to improve future reviews]_

### Patterns to Watch For

_[Patterns specific to this codebase/team]_

---

*Template version: 1.0*  
*Last updated: [Date]*
