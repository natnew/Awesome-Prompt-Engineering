[← Back: Recovery](05_recovery.md) | [Next: Synthesis →](07_synthesis.md)

# Module 6: Learning

Turn incidents into improvements.

---

## The Post-Mortem

A post-mortem is a blameless analysis of what happened, why, and how to prevent it.

**Goals:**
- Understand what happened (facts)
- Identify root causes (not just immediate causes)
- Generate action items (preventive measures)
- Share learnings (organizational knowledge)

---

## Post-Mortem Structure

### 1. Summary

- What happened in one paragraph
- Impact (duration, users affected, business impact)
- Severity level

### 2. Timeline

Detailed timeline of events:
```
TIME        EVENT
────────    ─────────────────────────────────────────
14:00       Alert triggered
14:05       On-call acknowledged
...
15:30       Incident resolved
```

### 3. Root Cause Analysis

**Ask "why" five times:**

1. Why did users get wrong answers?
   → Because the model returned hallucinations
2. Why did the model return hallucinations?
   → Because the context retrieval failed
3. Why did context retrieval fail?
   → Because the vector database was unreachable
4. Why was the vector database unreachable?
   → Because its certificate expired
5. Why did the certificate expire?
   → Because certificate renewal wasn't automated

**Root cause:** Lack of automated certificate renewal for vector database.

### 4. Contributing Factors

What else made this worse?
- No alert for certificate expiration
- Fallback to no-context wasn't graceful
- On-call wasn't familiar with vector DB

### 5. What Went Well

What worked as expected?
- Alert fired quickly
- Team assembled fast
- Communication was clear

### 6. Action Items

| Action | Owner | Priority | Due Date | Status |
|:-------|:------|:---------|:---------|:-------|
| Automate cert renewal | [Name] | P1 | [Date] | Open |
| Add cert expiry alert | [Name] | P1 | [Date] | Open |
| Update runbook | [Name] | P2 | [Date] | Open |
| Train team on VDB | [Name] | P3 | [Date] | Open |

---

## Blameless Culture

### What Blameless Means

- Focus on **systems**, not individuals
- Ask "why did the system allow this?" not "who screwed up?"
- Assume people acted reasonably given what they knew

### What Blameless Doesn't Mean

- No accountability
- No consequences for negligence
- Ignoring patterns of problems

### Reframing

| Blaming | Blameless |
|:--------|:----------|
| "Bob deployed broken code" | "The deployment process allowed broken code to reach production" |
| "Nobody was monitoring" | "Our monitoring didn't catch this failure mode" |
| "Alice made a mistake" | "The UI made it easy to make this mistake" |

---

## Running a Post-Mortem Meeting

### Before the Meeting

- Incident commander writes draft post-mortem
- Timeline is documented
- Participants are identified

### During the Meeting (30-60 min)

1. **Review timeline** (10 min)
   - Walk through events
   - Fill in gaps
   - Correct errors

2. **Root cause analysis** (15 min)
   - "Five whys" exercise
   - Identify contributing factors

3. **What went well/poorly** (10 min)
   - Acknowledge successes
   - Note areas for improvement

4. **Action items** (15 min)
   - Brainstorm preventive measures
   - Assign owners and priorities
   - Set due dates

### After the Meeting

- Publish post-mortem document
- Track action items to completion
- Share learnings with broader organization

---

## Your Task

Practice by completing a post-mortem for one of the scenarios:

1. Write the timeline
2. Perform root cause analysis
3. Identify contributing factors
4. Generate action items with owners

Use the template in `artifacts/postmortem_template.md`.

---

[← Back: Recovery](05_recovery.md) | [Next: Synthesis →](07_synthesis.md)
