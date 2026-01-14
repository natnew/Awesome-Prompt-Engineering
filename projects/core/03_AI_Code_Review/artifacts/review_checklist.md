# AI Code Review Checklist

A systematic approach to reviewing AI-generated code. Customize based on your experience.

---

## Quick Scan (30 seconds)

First impressions matter. Catch obvious issues before going deeper.

- [ ] Does the code attempt to solve the right problem?
- [ ] Are there obvious syntax errors?
- [ ] Are all necessary imports present?
- [ ] Does the overall structure make sense?
- [ ] Is there anything that looks "off"?

**Red flags to watch for:**
- Unused variables or imports
- Inconsistent naming conventions
- Suspiciously complex or simple solutions
- Comments that don't match the code

---

## Input Handling

AI often generates code that assumes perfect inputs.

### Validation
- [ ] Are all inputs validated before use?
- [ ] Are there type checks where needed?
- [ ] Are null/None values handled?
- [ ] Are empty collections handled?

### Edge Cases
- [ ] Empty input ([], "", {}, None)
- [ ] Single element input
- [ ] Very large input
- [ ] Negative numbers (if applicable)
- [ ] Unicode/special characters (if applicable)
- [ ] Boundary values (0, -1, MAX_INT, etc.)

### Injection Risks
- [ ] Is user input sanitized before use in:
  - [ ] SQL queries
  - [ ] Shell commands
  - [ ] File paths
  - [ ] HTML/JavaScript output
  - [ ] Regular expressions

---

## Error Handling

AI-generated code often has the "happy path" but misses error cases.

- [ ] Are exceptions caught at appropriate levels?
- [ ] Are error messages helpful and specific?
- [ ] Does the code fail gracefully?
- [ ] Are errors logged appropriately?
- [ ] Are resources cleaned up in error cases?
- [ ] Is there a catch-all for unexpected errors?

### Specific Checks
- [ ] File operations: Does it handle file not found?
- [ ] Network operations: Does it handle timeouts and connection errors?
- [ ] Database operations: Does it handle connection failures?
- [ ] API calls: Does it handle rate limits and service errors?

---

## Security

Security issues are easy to miss because the code "works."

### Authentication & Authorization
- [ ] Are credentials handled securely (not hardcoded)?
- [ ] Is authentication checked before sensitive operations?
- [ ] Are permissions verified?
- [ ] Are tokens/sessions handled properly?

### Data Protection
- [ ] Is sensitive data encrypted when needed?
- [ ] Is PII handled appropriately?
- [ ] Are secrets not logged or exposed in errors?
- [ ] Is data sanitized before output?

### Common Vulnerabilities
- [ ] SQL Injection: Using parameterized queries?
- [ ] XSS: Escaping user input in HTML?
- [ ] Path Traversal: Validating file paths?
- [ ] SSRF: Validating URLs?
- [ ] Deserialization: Using safe methods?

---

## Logic & Correctness

The hardest issues to catch because the code looks right.

### Algorithm
- [ ] Is the algorithm correct for the problem?
- [ ] Are loop conditions correct (off-by-one)?
- [ ] Are recursive base cases correct?
- [ ] Are comparisons correct (< vs <=)?
- [ ] Is the return value correct in all cases?

### State Management
- [ ] Is state initialized correctly?
- [ ] Is state updated correctly?
- [ ] Are there race conditions?
- [ ] Is state cleaned up appropriately?

### Control Flow
- [ ] Are all code paths reachable?
- [ ] Are all cases in switch/match handled?
- [ ] Are early returns correct?
- [ ] Does the code terminate in all cases?

---

## Concurrency (If Applicable)

AI often generates code that's not thread-safe.

- [ ] Is shared state protected by locks?
- [ ] Are there potential race conditions?
- [ ] Are there potential deadlocks?
- [ ] Is the code safe for concurrent access?
- [ ] Are atomic operations used where needed?
- [ ] Is cleanup happening in finally blocks?

---

## Performance

Code that works may not scale.

### Complexity
- [ ] Is time complexity appropriate?
- [ ] Is space complexity appropriate?
- [ ] Are there unnecessary nested loops?
- [ ] Are there redundant operations?

### Resource Usage
- [ ] Are connections/handles closed?
- [ ] Is memory freed/garbage collected?
- [ ] Are there memory leaks?
- [ ] Is caching used appropriately?

### Patterns to Watch
- [ ] N+1 query patterns
- [ ] String concatenation in loops
- [ ] Repeated expensive operations
- [ ] Loading entire files into memory

---

## Maintainability

Code you accept today you'll maintain tomorrow.

### Readability
- [ ] Are names descriptive?
- [ ] Is the code self-documenting?
- [ ] Are complex sections commented?
- [ ] Is formatting consistent?

### Structure
- [ ] Are functions focused (single responsibility)?
- [ ] Is the code DRY (no unnecessary duplication)?
- [ ] Are dependencies explicit?
- [ ] Is the code testable?

### Documentation
- [ ] Are public functions documented?
- [ ] Are non-obvious behaviors documented?
- [ ] Are assumptions documented?
- [ ] Are examples provided where helpful?

---

## Testing Checklist

What to verify when running the code.

### Basic Functionality
- [ ] Does it work with typical input?
- [ ] Does it produce expected output?
- [ ] Does it match the specification?

### Edge Cases
- [ ] Empty input
- [ ] Minimal input
- [ ] Maximum/large input
- [ ] Invalid input (should fail gracefully)

### Error Conditions
- [ ] Does it handle errors appropriately?
- [ ] Are error messages helpful?
- [ ] Does it clean up on failure?

---

## Meta-Review

Step back and assess overall.

### Trust Assessment
- [ ] Would I be comfortable deploying this?
- [ ] Would I be comfortable debugging this at 3 AM?
- [ ] Would I be comfortable if a junior developer modified this?

### Gaps
- [ ] What could still be wrong that I didn't check?
- [ ] What assumptions am I making?
- [ ] What would a security auditor find?
- [ ] What would a performance engineer find?

### Decision
- [ ] **ACCEPT**: Code is ready to use
- [ ] **MODIFY**: Code needs specific changes (list them)
- [ ] **REJECT**: Code has fundamental issues (explain why)
- [ ] **REGENERATE**: Better to start over with clearer prompt

---

## My Personal Blind Spots

_Fill in based on your review experience:_

Issues I frequently miss:
1. 
2. 
3. 

Checks I should always do:
1. 
2. 
3. 

---

## Review Log

Track your reviews to improve over time.

| Date | Code Type | Issues Found | Issues Missed | Notes |
|:-----|:----------|:-------------|:--------------|:------|
| | | | | |
| | | | | |
| | | | | |

---

*Last updated: [DATE]*
*Version: 1.0*
