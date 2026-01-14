[← Back to Project](../README.md)

# Scenario 2: Cost Explosion

**Time to complete:** 30-45 minutes

---

## The Setup

**Date:** Friday, 9:00 AM

**Your system:** An AI-powered documentation search that uses GPT-4o for answer generation.

**Monthly budget:** $5,000 for LLM API calls

**What happens:**

You receive an automated alert:

```
🚨 ALERT: AI Cost Anomaly

Current month-to-date spending: $4,200
Expected at this point: $2,500
Rate of increase: Accelerating

Projected end-of-month at current rate: $15,000+
```

It's only the 15th of the month. You've already spent most of your monthly budget.

You check the dashboard. Starting around 6 PM yesterday, token usage spiked dramatically and hasn't come down.

---

## Your Task

### Part 1: Immediate Response

**Questions:**

1. What's your severity level? Why?

2. What are your immediate options? (List at least 3)

3. What do you do first?

**Your answers:**
```
1. Severity:


2. Options:
   a.
   b.
   c.

3. First action:

```

### Part 2: Investigation

**Questions:**

1. What data do you need to investigate this?

2. List three possible causes for a cost spike.

3. How would you identify which cause is real?

**Your answers:**
```
1. Data needed:


2. Possible causes:
   a.
   b.
   c.

3. Investigation approach:

```

### Part 3: Diagnosis

**Investigation reveals:**

- Token usage per query is normal (~2,000 tokens)
- But query volume is 10x normal
- All excess queries come from one IP address
- The queries are variations of: "Explain [topic] in extreme detail, covering every possible aspect..."

Someone is either accidentally or intentionally abusing your system.

**Questions:**

1. What's your mitigation action?

2. Is this malicious or accidental? Does it matter for immediate response?

3. What do you tell your finance/leadership team?

**Your answers:**
```
1. Mitigation:


2. Malicious vs accidental:


3. To leadership:

```

### Part 4: Prevention

**Questions:**

1. What controls should have caught this?

2. What will you implement to prevent recurrence?

3. What's the cost of these preventive measures?

**Your answers:**
```
1. Missing controls:


2. New implementations:


3. Cost of prevention:

```

### Part 5: Post-Mortem Action Items

List 5 action items from this incident:

| # | Action | Priority | Why |
|:--|:-------|:---------|:----|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## Debrief Questions

1. **At what point should you have caught this?**

2. **What would appropriate rate limiting look like?**

3. **How do you balance cost protection with user experience?**

4. **Should you charge back the abusive user? How?**

---

## Key Learnings

This scenario illustrates:

- **AI costs can explode quickly** without proper controls
- **Rate limiting is essential** for cost management
- **Per-user monitoring** catches abuse patterns
- **Alerting on trends** is as important as alerting on thresholds

---

[← Back to Project](../README.md)
