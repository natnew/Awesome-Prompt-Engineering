# Blameless Post-Mortem

*Learn from failures without blame. Focus on systems, not individuals.*

**Competencies:** [Safety & Reliability](../COMPETENCIES.md#3-safety--reliability), [Governance & Defensibility](../COMPETENCIES.md#4-governance--defensibility)  
**Source:** [Incident Response](../projects/core/05_incident_response/README.md)

---

## The Problem

When incidents happen, organizations often look for someone to blame. "Who made this mistake?" This feels productive—accountability matters. But blame creates fear. Fear creates hiding. Hiding means you never learn what actually happened, and the same incidents repeat.

The deeper problem: complex systems fail for complex reasons. Rarely is there a single "root cause" or one person at fault. Blaming individuals gives false closure while missing systemic issues.

---

## The Solution

**Conduct post-mortems that focus on what happened and why, not who is at fault. Assume people made reasonable decisions given their information and constraints.**

Blameless doesn't mean "no accountability." It means accountability for systems and processes, not punishment for individuals. The goal is learning, not justice.

---

## How It Works

### The Blameless Mindset

Start with these assumptions:

1. **People tried to do the right thing.** Given their information, context, and constraints, their decisions made sense to them.

2. **Systems allowed the failure.** If one person's action could cause an incident, the system has a design flaw.

3. **Hindsight is 20/20.** What seems obvious after the fact wasn't obvious before.

4. **Blame stops learning.** Once someone is blamed, investigation stops. Real causes remain hidden.

### The Post-Mortem Process

#### 1. Gather Facts (Not Judgments)

Collect what happened, in sequence:

```
Timeline:
14:32 - Deployment started
14:35 - Error rate increased
14:40 - Alert fired
14:42 - On-call acknowledged
14:50 - Root cause identified
15:05 - Rollback completed
15:15 - Error rate normalized
```

**Avoid:** "Bob carelessly deployed without testing."  
**Instead:** "Deployment occurred. Testing step was not run."

#### 2. Ask "Why" (Not "Who")

Use the 5 Whys technique, focused on systems:

```
Why did the error rate increase?
  → A null pointer exception in the new code.
Why wasn't this caught in testing?
  → The test suite didn't cover this edge case.
Why wasn't this edge case covered?
  → No one knew this input pattern existed.
Why didn't we know?
  → Production data patterns weren't visible in test.
Why wasn't production data visible?
  → No tooling to sample production inputs for testing.
```

Notice: No "why did Bob do X?" questions. Systems focus.

#### 3. Identify Contributing Factors

Rarely is there one root cause. List all contributing factors:

| Factor | Type | Contribution |
|:-------|:-----|:-------------|
| Edge case in code | Technical | Primary trigger |
| Missing test case | Process | Didn't catch |
| Time pressure | Organizational | Reduced review |
| No staging environment | Infrastructure | Couldn't test realistically |
| Unclear rollback procedure | Documentation | Slow recovery |

#### 4. Generate Action Items

For each contributing factor, propose improvements:

| Factor | Action Item | Owner | Priority |
|:-------|:------------|:------|:---------|
| Missing test case | Add regression test | Engineering | P0 |
| No production data sampling | Build sampling tool | Platform | P1 |
| Unclear rollback | Document rollback procedure | SRE | P1 |
| Time pressure | Review release schedule | Management | P2 |

**Good action items:**
- Specific and actionable
- Have an owner
- Improve the system
- Prevent recurrence

**Bad action items:**
- "Be more careful"
- "Train Bob better"
- Vague or unowned

#### 5. Share Widely

The learning only has value if it spreads. Share the post-mortem:
- With the immediate team
- With related teams
- In a searchable archive
- In regular review meetings

---

## When to Use

**Always use for:**
- Any SEV1 or SEV2 incident
- Incidents that surprised you
- Incidents that could have been worse
- Near-misses

**Consider using for:**
- SEV3 incidents with learning value
- Repeated minor issues
- Customer complaints with systemic causes

---

## When NOT to Use

- Genuine malfeasance (separate HR process)
- Trivial incidents with no learning value
- When it would become checkbox exercise

Even minor incidents benefit from lightweight post-mortems.

---

## Examples

### Example: The Blame-Full Version (Don't Do This)

```
Incident Summary:
Bob deployed code without running tests. This caused an outage.

Root Cause:
Bob's negligence.

Action Items:
- Remind Bob to run tests
- Add Bob to deployment review process
```

**Problems:**
- Bob will hide future mistakes
- Others won't share their near-misses
- Systemic issues (why was testless deploy possible?) unexplored

### Example: The Blameless Version (Do This)

```
Incident Summary:
A deployment introduced a null pointer exception that increased error 
rates from 0.1% to 15% for 43 minutes.

Contributing Factors:
1. Code path not covered by existing tests
2. Deployment process doesn't require test run
3. No pre-deployment staging check
4. Production input patterns not in test data
5. Alert threshold too high (fired late)

What Went Well:
- Quick identification once investigated
- Rollback procedure worked
- Team mobilized effectively

What Went Poorly:
- 8 minutes before alert fired
- Test gap existed for 6 months
- No automated deployment gates

Action Items:
1. [P0] Add regression test for this case
2. [P1] Require test pass before deployment (automation)
3. [P1] Lower alert threshold to 5%
4. [P2] Add production input sampling to test suite
5. [P2] Implement staging deployment step
```

---

## Anti-Patterns

### Blame in Disguise

**What happens:** "We're being blameless" but action items are "retrain Bob" or "add review for Bob's work."

**Fix:** Action items should improve systems, not surveil individuals.

### Shallow Analysis

**What happens:** Stop at the first "why." "The code had a bug" → "Fix the bug." Done.

**Fix:** Keep asking why. Why could that bug exist? Why wasn't it caught? Why did it have this impact?

### No Action Items

**What happens:** Great post-mortem, no follow-up. Same incident happens again.

**Fix:** Every contributing factor needs an action item. Track completion.

### Too Many Action Items

**What happens:** Post-mortem generates 47 action items. None get done.

**Fix:** Prioritize ruthlessly. Better to do 3 high-impact items than list 47.

### Performative Blamelessness

**What happens:** Official post-mortem is blameless. Hallway conversations are not. Bob is quietly sidelined.

**Fix:** Culture change requires consistent application. Leadership must model it.

---

## Trade-Offs

| Benefit | Cost |
|:--------|:-----|
| Psychological safety | Feels like no accountability |
| More honest reporting | Takes practice to internalize |
| Systemic improvements | May miss individual skill gaps |
| Better learning | Requires time and effort |

---

## Making It Work

### Leadership Requirements

- Explicitly commit to blamelessness
- Never punish based on post-mortem content
- Participate in post-mortems visibly
- Celebrate learning from failures

### Facilitation Tips

- Start by stating blameless ground rules
- Redirect "who" questions to "what enabled"
- Use passive voice for human actions ("A deployment was made" not "Bob deployed")
- Thank people for sharing mistakes

### Measuring Success

| Metric | What It Shows |
|:-------|:--------------|
| Incident reports filed | Psychological safety (more is better) |
| Near-miss reports | Trust in process |
| Action items completed | Post-mortem value |
| Repeat incidents | Learning effectiveness |

---

## Implementation Checklist

- [ ] Leadership committed to blameless culture
- [ ] Post-mortem template focuses on systems
- [ ] Facilitation training for leads
- [ ] Action items tracked to completion
- [ ] Post-mortems archived and searchable
- [ ] Regular review of patterns across incidents
- [ ] Metrics track participation and completion

---

## Related Patterns

- **[Graceful Degradation](graceful_degradation.md)** — Systems that fail safely need less blame
- **[Circuit Breaker](circuit_breaker.md)** — Automatic containment reduces incident scope
- **[Defense in Depth](defense_in_depth.md)** — Multiple layers mean single failures don't cause incidents

---

## Key Insight

> "The goal isn't to find who failed. It's to build systems where individual failures don't become systemic failures."

Blameless post-mortems aren't soft or lenient. They're more rigorous—they insist on understanding systems deeply, rather than settling for easy scapegoats.
