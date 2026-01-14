[← Back to Project](README.md) | [Next: Success Metrics →](02_success_metrics.md)

# Module 1: Problem Framing

Before building anything, understand what you're building and why.

---

## The Scenario

You're a senior engineer at a mid-sized B2B software company. Your team has been asked to build a customer support assistant that can answer questions about your product using your documentation.

**The request from leadership:**
> "We're spending too much on support tickets. Can we build something with AI that handles the easy questions automatically?"

**What you know:**
- Documentation: ~500 pages across user guides, API docs, troubleshooting guides, release notes
- Current support volume: ~2,000 tickets/month
- "Easy" questions (could be answered from docs): estimated 40-60% of tickets
- Support team cost: significant, but you don't have exact numbers yet
- Timeline expectation: "as fast as possible" (leadership's words)

**What you don't know:**
- What "good enough" looks like
- How users will actually interact with it
- What happens when it's wrong
- Whether it will actually reduce tickets or just create different problems

---

## The Real Problem

Notice what happened in this request: leadership defined a solution (AI assistant) before defining success criteria.

This is normal. It's also dangerous.

The questions you need to answer before writing any code:

| Question | Why It Matters |
|:---------|:---------------|
| What does "working" mean? | You can't improve what you can't measure |
| How will we know if it's helping? | Anecdotes aren't evidence |
| What's the cost of being wrong? | Determines how careful you need to be |
| What's the cost of building this? | Needs to be less than the benefit |
| What happens when it fails? | It will fail — what then? |

---

## Constraints That Matter

### Accuracy Stakes

**When the assistant is wrong:**
- User gets frustrated
- User opens a support ticket anyway (no savings)
- User loses trust in the product
- In worst case: user makes a mistake based on bad information

**Assessment:** Medium stakes. Not life-or-death, but wrong answers have real costs beyond just "didn't help."

### User Context

**Who uses this:**
- Mix of technical and non-technical users
- Various levels of familiarity with your product
- Some are troubleshooting urgent issues
- Some are exploring features

**Assessment:** Diverse users means diverse queries. Simple FAQ-style won't be sufficient.

### Documentation Reality

**What's actually in those 500 pages:**
- Some content is current
- Some is outdated
- Some is duplicated across docs
- Some contradicts other parts
- Quality varies significantly

**Assessment:** Garbage in, garbage out. RAG won't fix bad docs — it will surface them.

### Organizational Context

**Who needs to be convinced:**
- Leadership wants ROI
- Support team may feel threatened
- Legal may have concerns about AI giving advice
- Users have expectations set by consumer AI tools

**Assessment:** Multiple stakeholders with different success criteria.

---

## Failure Modes to Consider

Before defining success, consider how this system can fail:

### Retrieval Failures

| Failure Mode | What Happens | User Experience |
|:-------------|:-------------|:----------------|
| **Wrong documents retrieved** | System answers based on irrelevant content | Confident wrong answer |
| **No documents retrieved** | System has nothing to work with | "I don't know" or hallucination |
| **Partial retrieval** | Gets some relevant docs but misses key ones | Incomplete answer |
| **Outdated content retrieved** | Old docs rank higher than new | Correct answer for wrong version |

### Generation Failures

| Failure Mode | What Happens | User Experience |
|:-------------|:-------------|:----------------|
| **Hallucination** | Model invents information | Confident false answer |
| **Misinterpretation** | Model misunderstands retrieved content | Plausible wrong answer |
| **Over-generalization** | Model gives generic advice instead of specific | Unhelpful answer |
| **Context overflow** | Too much retrieved content for context window | Truncated or confused answer |
| **Citation failure** | Can't point to source of information | User can't verify |

### System Failures

| Failure Mode | What Happens | User Experience |
|:-------------|:-------------|:----------------|
| **Latency** | Slow response times | User abandonment |
| **API errors** | Upstream service failures | No answer at all |
| **Cost spikes** | Complex queries use many tokens | Budget exceeded |

---

## Your Task

Before moving to the next module, write down your answers to these questions:

### 1. Stakeholder Success Criteria

What would each stakeholder consider "success"?

| Stakeholder | Their Definition of Success |
|:------------|:---------------------------|
| Leadership | |
| Support Team | |
| Users | |
| Your Engineering Team | |

### 2. Risk Assessment

Rank the failure modes by:
- **Likelihood** (how often will this happen?)
- **Impact** (how bad is it when it happens?)

Which 3 failure modes should you focus on preventing?

### 3. Scope Definition

What is explicitly **out of scope** for v1?

Being clear about what you won't do is as important as what you will do.

---

## Key Insight

The scenario didn't come with success metrics. Neither will most real requests.

**Your job is to define what "working" means before building.** If you skip this step, you'll build something that "works" by someone's definition — but maybe not the right one.

The next module will help you define those metrics rigorously.

---

## Reflection

Before moving on, consider:

- Did the scenario feel realistic? (It's based on real projects)
- What would you have done differently if you'd received this request?
- What additional information would you want before starting?

---

[← Back to Project](README.md) | [Next: Success Metrics →](02_success_metrics.md)