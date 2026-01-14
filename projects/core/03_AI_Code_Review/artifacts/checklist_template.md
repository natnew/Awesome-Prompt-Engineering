# AI Code Review Checklist Template

Use this checklist when reviewing AI-generated code. Customize based on your experience and domain.

---

## Quick Scan (30 seconds)

### Does it make sense?
- [ ] Does the code do what was asked?
- [ ] Are the function/class names appropriate?
- [ ] Is the overall structure reasonable?

### Obvious issues?
- [ ] Are there syntax errors?
- [ ] Are all imports present?
- [ ] Are all variables defined before use?

---

## Input Handling (Critical)

### Validation
- [ ] Are all inputs validated?
- [ ] Are type checks in place where needed?
- [ ] Are ranges/bounds checked?

### Edge Cases
- [ ] What happens with `None`/`null`?
- [ ] What happens with empty input (empty string, empty list)?
- [ ] What happens with very large input?
- [ ] What happens with negative numbers (if applicable)?

### Injection Risks
- [ ] Is user input used in SQL queries? (Use parameterized queries)
- [ ] Is user input used in shell commands? (Use list form, not shell=True)
- [ ] Is user input used in file paths? (Check for path traversal)
- [ ] Is user input rendered in HTML? (Check for XSS)

---

## Error Handling

### Exception Handling
- [ ] Are exceptions caught appropriately?
- [ ] Are exceptions too broad? (Catching `Exception` hides bugs)
- [ ] Are errors logged with enough context?
- [ ] Does the code fail gracefully?

### Resource Management
- [ ] Are files closed properly? (Use `with` statements)
- [ ] Are database connections closed?
- [ ] Are network connections handled correctly?

### Error Messages
- [ ] Are error messages helpful for debugging?
- [ ] Do error messages avoid leaking sensitive information?

---

## Security

### Authentication & Authorization
- [ ] Is authentication required where needed?
- [ ] Is authorization checked before sensitive operations?
- [ ] Are session tokens generated securely?

### Sensitive Data
- [ ] Are passwords hashed (not stored plaintext)?
- [ ] Are secrets (API keys, tokens) not hardcoded?
- [ ] Is sensitive data encrypted at rest/in transit?
- [ ] Is PII handled appropriately?

### Common Vulnerabilities
- [ ] SQL injection (parameterized queries?)
- [ ] Command injection (avoiding shell=True?)
- [ ] Path traversal (validating file paths?)
- [ ] XSS (escaping output?)
- [ ] CSRF (tokens in place?)

---

## Logic Correctness

### Boundary Conditions
- [ ] Are loop boundaries correct? (off-by-one errors)
- [ ] Are comparisons correct? (< vs <=)
- [ ] Are array indices valid?

### Algorithm
- [ ] Is the algorithm appropriate for the data size?
- [ ] Does it handle the worst case acceptably?
- [ ] Are there unnecessary nested loops?

### State Management
- [ ] Is state mutated when it shouldn't be?
- [ ] Are there unintended side effects?
- [ ] Is the function pure when it should be?

---

## Concurrency (If Applicable)

### Thread Safety
- [ ] Is shared state protected (locks, atomic operations)?
- [ ] Are there race conditions?
- [ ] Is the code deadlock-free?

### Async Code
- [ ] Are async resources properly cleaned up?
- [ ] Are there proper timeouts?
- [ ] Is error handling correct in async context?

---

## Performance

### Complexity
- [ ] What's the time complexity? Is it acceptable?
- [ ] What's the space complexity? Is it acceptable?
- [ ] Are there unnecessary operations in loops?

### Memory
- [ ] Are there potential memory leaks?
- [ ] Is caching bounded?
- [ ] Are large objects cleaned up when done?

### I/O
- [ ] Are there N+1 query patterns?
- [ ] Is I/O batched where appropriate?
- [ ] Are there unnecessary network calls?

---

## Maintainability

### Readability
- [ ] Are variable names clear?
- [ ] Is the code structure logical?
- [ ] Are there comments where needed?

### Simplicity
- [ ] Is there dead code?
- [ ] Is there duplicated code?
- [ ] Could this be simpler?

### Dependencies
- [ ] Are imports appropriate?
- [ ] Is there unnecessary coupling?
- [ ] Are dependencies up to date and secure?

---

## Testing Considerations

### Testability
- [ ] Can this code be unit tested?
- [ ] Are dependencies injectable?
- [ ] Is state isolated?

### Test Coverage
- [ ] What tests should exist?
- [ ] Are edge cases covered?
- [ ] Are error cases tested?

---

## AI-Specific Concerns

### Plausibility vs Correctness
- [ ] Does this look right but might be wrong?
- [ ] Is there a subtle bug that "looks like" valid code?
- [ ] Did the AI mix up similar concepts?

### Missing Context
- [ ] Does the AI know about your specific requirements?
- [ ] Does it know about your codebase conventions?
- [ ] Does it know about your production environment?

### Verification
- [ ] Can you verify this works? (tests, REPL)
- [ ] Do you understand what every line does?
- [ ] Would you be comfortable debugging this at 2 AM?

---

## Final Decision

### Ship Criteria
- [ ] Does it pass all existing tests?
- [ ] Have you tested edge cases manually?
- [ ] Would you approve this in a code review?
- [ ] Are you comfortable being on-call for this?

### Confidence Rating

Rate your confidence in this code (1-5):
- **1**: Very uncertain, needs extensive review
- **2**: Some concerns, needs testing
- **3**: Probably fine, standard review
- **4**: Confident, minor tweaks only
- **5**: High confidence, ready to ship

**My confidence: ___**

**Reasoning:**

---

## My Personal Additions

*Add checks specific to your domain, stack, or common issues you've encountered:*

- [ ] ____
- [ ] ____
- [ ] ____
- [ ] ____
- [ ] ____

---

*Template version: 1.0*
*Last updated: ____*
