[← Back to Project](../README.md)

# Scenario 3: Data Leak Suspicion

**Time to complete:** 45-60 minutes

---

## The Setup

**Date:** Wednesday, 11:30 AM

**Your system:** An internal AI assistant for your company that can access employee directories, HR policies, and internal documentation.

**What happens:**

You receive this message from an employee:

> "I was using the AI assistant to look up the vacation policy, and it mentioned something about 'Sarah Chen's medical leave request.' I don't know who Sarah Chen is, and I definitely shouldn't be seeing her medical information. Is this a bug?"

This is potentially serious. Medical information is protected (HIPAA in US, similar laws elsewhere).

---

## Your Task

### Part 1: Immediate Response

**This is time-sensitive. What do you do in the first 5 minutes?**

1. Who do you notify immediately? (List specific roles)

2. Do you disable the AI assistant? Why or why not?

3. What do you tell the employee who reported this?

**Your answers:**
```
1. Immediate notifications:


2. Disable decision:


3. To the reporter:

```

### Part 2: Assessment

**Questions:**

1. What's the severity? Why?

2. What information do you need to assess the scope?

3. How do you preserve evidence for potential investigation?

**Your answers:**
```
1. Severity:


2. Information needed:


3. Evidence preservation:

```

### Part 3: Investigation

**You need to determine:**

1. Did the AI actually reveal protected information?
   - Was this real data or a hallucination?
   - If real, how did the AI access it?

2. Is this an isolated incident or pattern?
   - Were there other similar responses?
   - Who else might have seen protected data?

3. How did this happen technically?
   - What data sources does the AI have access to?
   - What went wrong with access controls?

**Document your investigation plan:**
```
Step 1:

Step 2:

Step 3:

Step 4:

```

### Part 4: Scenario Branches

#### If Investigation Shows: Hallucination

The AI made up "Sarah Chen" and her medical leave. There is no Sarah Chen in your company, and no medical information was actually exposed.

**Questions:**

1. Is this still a problem? Why?

2. What do you communicate to stakeholders?

3. What action items result from this?

**Your answers:**
```
1. Still a problem?


2. Communication:


3. Action items:

```

#### If Investigation Shows: Real Data Leak

The AI did access and reveal real medical information that was accidentally included in its knowledge base.

**Questions:**

1. What are your legal/compliance obligations?

2. Who needs to be notified? (List specific parties)

3. What's your remediation plan?

**Your answers:**
```
1. Obligations:


2. Notifications:


3. Remediation:

```

### Part 5: Communication Drafts

**Write drafts for each scenario:**

**If Hallucination:**
- To the reporter:
- To leadership:

**If Real Data Leak:**
- To the affected individual(s):
- To legal/compliance:
- To leadership:

**Your drafts:**
```
HALLUCINATION SCENARIO:

To reporter:


To leadership:



REAL DATA LEAK SCENARIO:

To affected individual(s):


To legal/compliance:


To leadership:

```

### Part 6: Prevention

Regardless of whether this was hallucination or real:

1. What access controls should be in place?

2. What output filtering should exist?

3. How would you audit the AI's knowledge base?

**Your answers:**
```
1. Access controls:


2. Output filtering:


3. Knowledge base audit:

```

---

## Debrief Questions

1. **How is handling a potential data leak different from other incidents?**

2. **What's the right balance between speed and thoroughness in investigating?**

3. **How do you communicate uncertain information to stakeholders?**

4. **What would have prevented this scenario entirely?**

---

## Key Learnings

This scenario illustrates:

- **Data security incidents require immediate escalation** to legal/compliance
- **Evidence preservation** is critical before investigation
- **Even hallucinated data leaks** are concerning (what if next time it's real?)
- **Access controls in AI systems** need special attention
- **Communication must be careful** to avoid admitting liability prematurely

---

[← Back to Project](../README.md)
