[Home](https://natnew.github.io/Awesome-Prompt-Engineering/) | [Competencies](../../../COMPETENCIES.md) | [AI for Science](../README.md) | [Core Projects](../../core/README.md)

# Project: Scientific Event Engine

Build an event-driven discovery infrastructure for scientific observatories and research facilities.

---

## What You'll Build

An event-driven system that processes streams of scientific observations, prioritises anomalies, coordinates multi-agent analysis, and maintains provenance — the quiet infrastructure that accelerates discovery without drama.

This is the **invisible backbone** of modern scientific discovery: systems that watch, filter, flag, and route interesting observations to the right analysis pipelines.

---

## Project Overview

| Attribute | Value |
|:----------|:------|
| **Time Estimate** | 14-18 hours |
| **Difficulty** | Advanced |
| **Prerequisites** | Complete 3+ Core Projects, ideally Drug Discovery Pipeline |

### Primary Competencies

| Competency | Depth | Why |
|:-----------|:------|:----|
| Systems Design | ●●●●● | Event-driven architecture, multi-agent coordination |
| Evaluation & Measurement | ●●●● | Measuring discovery acceleration |
| Governance & Defensibility | ●●●● | Scientific provenance, reproducibility |
| Safety & Reliability | ●●● | Avoiding missed discoveries, false positives |
| Output Review & Oversight | ●●● | Human-in-the-loop for significant detections |

---

## Why This Project Matters

Modern scientific facilities generate torrents of data — far more than humans can review.

**The opportunity:** AI can watch data streams continuously, flag anomalies worth human attention, and route observations to appropriate analysis pipelines. This is how we find gravitational waves, detect transient astronomical events, and identify particles in collider data.

**The risk:** AI that misses important events delays discovery. AI that generates too many false positives wastes human attention and erodes trust. AI without provenance can't support scientific claims.

**What you'll learn:** How to build event-driven systems that balance sensitivity and specificity, coordinate multiple analysis agents, and maintain the provenance trail that science requires.

---

## The Mental Model

Think of this system as a **vigilant research assistant with perfect memory**.

A vigilant assistant:
- Watches streams of data continuously
- Knows what "normal" looks like
- Notices when something is different
- Prioritises what deserves attention
- Routes observations to the right expert
- Keeps perfect records of everything

Your system should embody these qualities for scientific event processing.

---

## Scientific Event Processing

### The Event Processing Challenge

```
Data Source                    Events per Second           Human Review Capacity
────────────────────────────────────────────────────────────────────────────────
Radio Telescope Array          10,000+                     ~100/day (detailed)
Particle Collider              40,000,000                  ~1,000/day
Genomics Sequencer             1,000,000+                  ~500/day
Security Camera Network        100+                        ~50/day (flagged)
────────────────────────────────────────────────────────────────────────────────

The gap: Machines generate millions of events; humans can review hundreds.

The solution: Intelligent filtering, prioritisation, and routing.
```

### Event Categories

| Category | Definition | Response |
|:---------|:-----------|:---------|
| **Routine** | Expected, matches normal patterns | Log, no action |
| **Interesting** | Unusual but not urgent | Queue for review |
| **Significant** | Potentially important discovery | Alert, prioritise analysis |
| **Critical** | Time-sensitive, rare event | Immediate notification |

---

## What You'll Deliver

### 1. Event Processing Pipeline

Design and implement:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     RAW EVENT STREAM                                │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  INGESTION LAYER                                                    │
│  - Stream parsing                                                  │
│  - Basic validation                                                │
│  - Metadata extraction                                             │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  FILTERING LAYER                                                    │
│  - Noise rejection                                                 │
│  - Quality checks                                                  │
│  - Known artifact removal                                          │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│  CLASSIFICATION LAYER                                               │
│  - Pattern matching                                                │
│  - Anomaly detection                                               │
│  - Category assignment                                             │
└─────────────────────────────────────────────────────────────────────┘
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                    ▼           ▼           ▼
              ┌─────────┐ ┌─────────┐ ┌─────────┐
              │ Routine │ │Interesting│ │Critical│
              │  → Log  │ │→ Queue  │ │→ Alert │
              └─────────┘ └─────────┘ └─────────┘
```

### 2. Multi-Agent Analysis System

Specialised agents for different analysis types:

| Agent | Role | Trigger |
|:------|:-----|:--------|
| **Triage Agent** | Initial assessment, routing | All flagged events |
| **Pattern Agent** | Known pattern matching | Structured events |
| **Anomaly Agent** | Novelty detection | Unclassified events |
| **Context Agent** | Historical/environmental context | Significant events |
| **Coordination Agent** | Multi-instrument follow-up | Multi-source events |

### 3. Provenance System

Every detection traceable:
- Raw data reference
- Processing steps applied
- Classification decisions
- Confidence scores
- Human review status

### 4. Evaluation Framework

Measuring what matters:
- Detection sensitivity (don't miss important events)
- Specificity (don't waste attention on false positives)
- Latency (how fast from event to alert)
- Provenance completeness

---

## What "Done" Looks Like

| Deliverable | Evidence |
|:------------|:---------|
| Event pipeline design | Handles streaming data with appropriate latency |
| Multi-agent system | Specialised agents coordinate on analysis |
| Provenance system | Every detection fully traceable |
| Evaluation framework | Sensitivity, specificity, latency measured |
| Workflow integration | Fits into scientific operations |
| Reflection | Synthesis document with honest assessment |

---

## Project Structure

```
03_scientific_event_engine/
├── README.md                      # This file
├── 01_problem_framing.md          # Observatory context, event types
├── 02_event_architecture.md       # Stream processing, filtering
├── 03_agent_design.md             # Multi-agent analysis system
├── 04_provenance_system.md        # Scientific traceability
├── 05_evaluation_framework.md     # Detection metrics
├── synthesis.md                   # Reflection and portfolio artifact
├── artifacts/
│   ├── event_schema.md            # Event data model
│   ├── agent_specification.md     # Agent roles and protocols
│   ├── detection_thresholds.md    # Sensitivity/specificity tuning
│   └── operations_guide.md        # Integration with facility operations
└── reference/
    └── (optional implementation)
```

---

## Domain Context: Astronomical Transients

This project uses astronomical transient detection as the primary domain, but the patterns apply broadly to any event-driven scientific system.

### What Are Transients?

Astronomical transients are events that appear, change, or disappear on human-relevant timescales:

| Event Type | Timescale | Science Value |
|:-----------|:----------|:--------------|
| Supernovae | Days-weeks | Stellar evolution, cosmology |
| Gamma-ray bursts | Seconds-minutes | Extreme physics |
| Gravitational waves | Milliseconds | Fundamental physics |
| Fast radio bursts | Milliseconds | Unknown origin |
| Near-Earth objects | Hours-days | Planetary defense |

### Why This Domain?

Transient astronomy exemplifies event-driven science:
- High event rates
- Time-critical response
- Multi-instrument coordination
- Provenance requirements
- Balance of automation and human judgment

The patterns you learn here transfer to:
- Particle physics event selection
- Genomics variant calling
- Security anomaly detection
- Industrial process monitoring

---

## Before You Begin

### Mindset

Event-driven systems require different thinking:
- **Streams, not queries** — Data arrives continuously
- **Latency matters** — Delays cost discoveries
- **False positives cost attention** — Human time is precious
- **False negatives cost science** — Missed events may never recur

### Technical Grounding

Helpful background:
- Stream processing concepts
- Time-series anomaly detection
- Message queues and event buses
- Distributed systems basics

You don't need to be an expert, but familiarity helps.

### Scientific Grounding

Understanding helps but isn't required:
- What makes an observation "interesting"
- Why provenance matters in science
- How discoveries move from detection to publication

---

## Ready?

[Start with Problem Framing →](01_problem_framing.md)

---

## Navigation

| Previous | Up | Next |
|:---------|:---|:-----|
| [Drug Discovery Pipeline](../02_drug_discovery_pipeline/README.md) | [AI for Science Overview](../README.md) | [Problem Framing](01_problem_framing.md) |
