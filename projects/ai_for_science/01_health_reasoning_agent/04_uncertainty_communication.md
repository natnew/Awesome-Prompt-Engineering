[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [← Agent Design](03_agent_design.md) | [Evaluation Framework →](05_evaluation_framework.md)

# Uncertainty Communication

Learn to communicate uncertainty honestly without being unhelpfully vague or falsely precise.

---

## The Uncertainty Paradox

Health AI faces a fundamental paradox:

- **Users want certainty** — "What do I have? Will I be okay?"
- **Medicine is uncertain** — Even experts work with probabilities
- **False certainty causes harm** — Overconfidence in either direction

Your job is to communicate uncertainty in ways that are:
- **Honest** — Accurately reflecting what you know and don't know
- **Helpful** — Enabling good decisions despite uncertainty
- **Calibrated** — Neither overconfident nor paralysingly vague

---

## The Mental Model: Confidence as a Spectrum

Think of confidence not as binary (sure/unsure) but as a spectrum:

```
0%                                                              100%
│                                                                  │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┤
│   No     │  Very    │ Somewhat │ Moderately│ Fairly  │  Very    │
│  Idea    │Uncertain │Uncertain │ Confident │Confident│ Confident│
│          │          │          │           │         │          │
│ "I don't │"Possibly"│"I think" │"Probably" │"Likely" │"Almost   │
│  know"   │          │          │           │         │ certainly│
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘

In health AI context:

Low confidence (don't use)          High confidence (still hedge)
├────────────────────────────────────┼──────────────────────────────┤
│ "You have condition X"             │ "This could be X"            │
│ "You definitely don't have Y"      │ "X is unlikely but possible" │
│ "You don't need to see a doctor"   │ "This seems routine, but     │
│                                    │  see a doctor if concerned"  │
```

**Key insight:** Even at high confidence, health AI should hedge because:
1. You're not examining the patient
2. You don't have their full history
3. Rare conditions exist
4. The cost of being wrong is high

---

## Types of Uncertainty

Different uncertainties require different communication:

### Aleatoric Uncertainty (Inherent Randomness)

Things that are genuinely unpredictable even with perfect information.

```
Example: "Will this headache resolve on its own?"
Truth: Most tension headaches do, but not all. This is inherently probabilistic.

Communication:
"Most headaches like this resolve within a few days with rest and over-the-counter 
pain relief. If yours persists beyond a week or gets significantly worse, that's 
worth checking out."
```

### Epistemic Uncertainty (Knowledge Gaps)

Things that are uncertain because we lack information.

```
Example: "What's causing this headache?"
Truth: Without examination and history, many possibilities.

Communication:
"Based on what you've described, this could be a tension headache — that's the 
most common type. But I'd need to know more to be more specific. Things that 
would help narrow it down: [questions]"
```

### Model Uncertainty (System Limitations)

Things the AI system genuinely can't assess.

```
Example: "Is this mole cancerous?"
Truth: Cannot assess from description alone, requires visual examination.

Communication:
"I can't assess skin lesions from descriptions — that really requires a visual 
examination by a dermatologist. What I can tell you is what features doctors 
look for: [ABCDE criteria]. If you're noticing any of those, it's worth getting 
checked."
```

---

## Communication Patterns

### Pattern 1: Layered Confidence

Present information in layers from most to least confident:

```
[Most confident] → [Less confident] → [Uncertain] → [What would help]

Example:
"What you're describing sounds consistent with tension-type headaches — that's 
the most common cause of headaches like this. [High confidence]

The light sensitivity you mentioned is a bit unusual for tension headaches 
though, and could suggest migraine features. [Medium confidence]

I can't rule out other causes without knowing more. [Acknowledging limits]

A few things that would help clarify: Have you had headaches like this before? 
Any nausea or vision changes?" [Path to better information]
```

### Pattern 2: Conditional Statements

Express how confidence changes with conditions:

```
"If [condition], then [implication]"

Example:
"If this is your first headache like this, that's more reason to get it 
checked out — new patterns are worth investigating.

If you've had similar headaches before that resolved on their own, this 
is probably the same pattern, though if it feels different in any way, 
mention that to your doctor."
```

### Pattern 3: Probability Framing

Translate probabilities into meaningful terms:

| Probability | Phrasing | When to Use |
|:------------|:---------|:------------|
| <5% | "Unlikely but possible" | Rare conditions worth mentioning |
| 5-25% | "Sometimes", "Can happen" | Meaningful minority |
| 25-50% | "Possible", "May be" | Genuine uncertainty |
| 50-75% | "Often", "Probably" | More likely than not |
| >75% | "Usually", "Most likely" | Strong probability |

**Never use:**
- "Definitely" / "Certainly" (too confident for health AI)
- "Impossible" / "Never" (rare things happen)
- Precise percentages (false precision)

### Pattern 4: Reference Class Communication

Compare to relevant groups:

```
"Most people with symptoms like yours..." 
"In your situation, doctors typically..."
"For headaches that last this long..."

Example:
"Most headaches that have lasted three days without other concerning symptoms 
turn out to be tension-type or migraine, both very treatable. That said, 
headaches that persist beyond a week or are accompanied by [red flags] 
warrant a doctor visit."
```

### Pattern 5: Red Flag Highlighting

Make uncertain escalation points clear:

```
"I think [likely scenario], but see a doctor if [red flags]"

Example:
"This sounds like it could be a tension headache, which typically responds to 
rest and over-the-counter pain relief. 

However, please see a doctor soon if you experience:
• Sudden severe headache unlike any before
• Fever or stiff neck
• Vision changes or confusion
• Headache that wakes you from sleep
• No improvement after a week"
```

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Confident Diagnosis

```
❌ Bad: "This is definitely a tension headache."
✓ Good: "This sounds consistent with tension-type headaches, which are the 
        most common type."
```

### Anti-Pattern 2: Dismissive Reassurance

```
❌ Bad: "Don't worry, it's nothing serious."
✓ Good: "Most headaches like this aren't serious, but I understand why you're 
        concerned. Here's when to seek care..."
```

### Anti-Pattern 3: Paralyzing Vagueness

```
❌ Bad: "It could be many things. I can't really say."
✓ Good: "There are several possibilities. The most common would be [X]. Less 
        likely but worth knowing about are [Y, Z]. Here's how to tell the 
        difference..."
```

### Anti-Pattern 4: False Precision

```
❌ Bad: "There's a 73% chance this is a tension headache."
✓ Good: "This is most likely a tension headache, though I can't be certain 
        without more information."
```

### Anti-Pattern 5: Scope Creep Under Pressure

```
User: "But what do you THINK it is? Just tell me!"

❌ Bad: "Fine, I think it's probably just anxiety."
✓ Good: "I understand you want a clear answer. The most likely explanation 
        is [X], but I'm not able to diagnose — that requires a doctor who 
        can examine you. What I can do is help you understand what you're 
        experiencing and prepare for that conversation."
```

---

## Calibration: Matching Confidence to Evidence

### The Calibration Goal

Your stated confidence should match reality:
- When you say "probably", the thing should happen ~70-80% of the time
- When you say "unlikely", it should happen <20% of the time

### Calibration Challenges in Health AI

| Challenge | Risk | Mitigation |
|:----------|:-----|:-----------|
| Training data skew | Overconfidence on common conditions | Explicit uncertainty for rare conditions |
| Selection bias | Users with symptoms ≠ general population | Don't assume base rates apply |
| Confirmation bias | Seeing patterns that aren't there | Multiple hypothesis discipline |
| Hindsight bias | Evaluations after knowing outcome | Prospective evaluation |

### Calibration Exercises

For each scenario, estimate your confidence and compare to outcomes:

```
Scenario: User describes 3-day bilateral headache with stress context
Your assessment: 80% tension-type, 15% migraine, 5% other

Track outcomes over many cases:
- Do 80% of similar cases turn out to be tension-type?
- Are you systematically over/under confident?
- Where are your biggest calibration gaps?
```

---

## User-Centred Uncertainty Communication

### Adapting to User Needs

Different users need different uncertainty framings:

| User Signal | Communication Adjustment |
|:------------|:------------------------|
| High anxiety | More reassurance, clearer escalation criteria |
| Health literacy | Can handle more technical nuance |
| Decision-focused | Emphasise actionable next steps |
| Information-seeking | More detail on possibilities |

### Example Adaptations

**High anxiety user:**
```
"I can hear that you're worried, and it's understandable to feel that way 
when something's been bothering you for days. Let me share what I can:

The symptoms you're describing are very common and usually not serious. 
Most likely, this is [common explanation].

Here's exactly when you should seek care: [clear criteria].
And here's what you can do right now: [practical steps]."
```

**Information-seeking user:**
```
"Let me walk through what your symptoms could indicate:

The most common explanation would be tension-type headache, consistent with 
the bilateral location and your mention of stress. These typically respond 
to [treatment].

The light sensitivity you mentioned is less typical for tension-type, and 
could suggest migraine features. Migraines can present bilaterally, though 
it's less common. Key differentiators would be [factors].

Less likely but worth mentioning: [other possibilities and why]."
```

---

## Practical Exercises

### Exercise 1: Uncertainty Audit

Take five sample health queries. For each:
1. What are you confident about?
2. What are you uncertain about?
3. What type of uncertainty is it?
4. How would you communicate each?

### Exercise 2: Calibration Practice

Generate responses to 20 health scenarios. For each:
1. State your confidence level
2. What evidence supports that confidence?
3. What would change your confidence?

After generating responses, evaluate calibration:
- Where were you overconfident?
- Where were you underconfident?
- What patterns do you notice?

### Exercise 3: Tone Adaptation

Take one health scenario. Write three versions:
1. For a highly anxious user
2. For a medically knowledgeable user
3. For a user who just wants to know what to do

Compare: What changed? What stayed the same?

### Exercise 4: Red Flag Communication

Design clear, memorable red flag communications for:
1. Headache symptoms
2. Chest symptoms
3. Abdominal symptoms
4. Skin changes
5. Mental health signals

Each should be:
- Specific enough to be useful
- Broad enough to catch serious cases
- Memorable for users

---

## Deliverables

By the end of this section, you should have:

| Deliverable | Description |
|:------------|:------------|
| **Uncertainty framework** | Types of uncertainty, how each is communicated |
| **Communication templates** | Patterns for different confidence levels |
| **Calibration approach** | How you'll measure and improve calibration |
| **User adaptation rules** | How communication changes by user type |
| **Red flag standards** | Clear escalation criteria for major symptom categories |

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Agent Design](03_agent_design.md) | [Project Overview](README.md) | [Evaluation Framework →](05_evaluation_framework.md) |
