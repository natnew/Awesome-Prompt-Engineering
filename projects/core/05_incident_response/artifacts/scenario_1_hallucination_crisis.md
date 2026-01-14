[← Back to Project](../README.md)

# Scenario 1: Hallucination Crisis

**Time to complete:** 45-60 minutes

---

## The Setup

**Date:** Tuesday, 2:30 PM

**Your system:** A customer service AI assistant for an e-commerce company. It answers questions about orders, returns, and product information.

**What happens:**

Your monitoring shows everything is normal. Then you receive this message from the Customer Success team:

> "Hey, we're getting complaints from customers. Three different people say the AI told them they could get full refunds on items after 90 days. Our policy is 30 days. One customer is demanding we honor what the AI said. Can you check what's going on?"

You check the conversation logs. The AI did indeed tell multiple customers:

> "You can return this item for a full refund within 90 days of purchase. Simply go to your order history and select 'Request Refund.'"

Your return policy clearly states 30 days.

---

## Your Task

Work through this incident as if it were real. Document your actions at each step.

### Part 1: Detection & Assessment

**Questions to answer:**

1. How would you verify this is real and not a misunderstanding?

2. What's the severity? (SEV1/2/3/4) Why?

3. How many customers might be affected?

4. Is this ongoing or was it a past event?

**Your answers:**
```
1. Verification approach:


2. Severity assessment:


3. Impact scope:


4. Current status:

```

### Part 2: Response

**Questions to answer:**

1. What's your immediate mitigation action?

2. What do you tell the customer success team right now?

3. What do you tell the customers who were given wrong information?

4. Do you disable the AI system? Why or why not?

**Your answers:**
```
1. Immediate action:


2. To customer success:


3. To affected customers:


4. Disable decision:

```

### Part 3: Investigation

**Questions to answer:**

1. What are the possible causes of this hallucination?
   - Model issue?
   - Context retrieval issue?
   - Outdated content?
   - Prompt issue?

2. What logs/data would you examine?

3. What's your initial hypothesis?

**Your answers:**
```
1. Possible causes:


2. Data to examine:


3. Hypothesis:

```

### Part 4: Resolution

**Assume investigation reveals:** The vector database had indexed an old FAQ page that mentioned a "90-day satisfaction guarantee" from a promotion that ended 2 years ago. This outdated content was being retrieved and used by the AI.

**Questions to answer:**

1. What's the fix?

2. How do you verify the fix works?

3. How do you prevent this from happening again?

**Your answers:**
```
1. The fix:


2. Verification:


3. Prevention:

```

### Part 5: Communication

**Write actual messages for:**

1. **Status page update** (if you would post one)

2. **Email to affected customers** (the three who were given wrong info)

3. **Internal summary** to leadership

**Your drafts:**
```
Status page:



Customer email:



Leadership summary:


```

### Part 6: Post-Mortem

Complete a brief post-mortem:

**Timeline:**
```
TIME        EVENT
────        ─────
2:30 PM     
...
```

**Root cause:**
```

```

**Action items:**
```
| Action | Owner | Priority |
|:-------|:------|:---------|
|        |       |          |
|        |       |          |
|        |       |          |
```

---

## Debrief Questions

After completing the scenario:

1. **What was the hardest decision you had to make?**

2. **What information did you wish you had?**

3. **How would you detect this faster next time?**

4. **What should be in a runbook for this scenario?**

---

## Key Learnings

This scenario illustrates:

- **AI hallucinations can have business consequences** (customers demanding honored)
- **Outdated content is a common RAG failure mode**
- **Detection often comes from users, not monitoring**
- **Communication to affected parties is as important as the technical fix**

---

[← Back to Project](../README.md)
