# Golden Dataset Guidelines

## What Is a Golden Dataset?

A golden dataset is a curated collection of examples with known-correct answers that you use to:

1. **Benchmark** — Measure system performance objectively
2. **Regression test** — Detect when changes break things
3. **Compare** — Evaluate different approaches
4. **Calibrate** — Tune evaluation metrics

It's called "golden" because it represents the ground truth — the standard against which everything is measured.

---

## Structure of Each Example

```yaml
# Example entry in golden_dataset.yaml

- id: "query_001"                    # Unique identifier
  
  # The query
  query: "How do I export my data to CSV?"
  
  # Metadata
  category: "how-to"                 # Query type
  difficulty: "simple"               # simple, medium, hard
  created_at: "2025-01-15"
  source: "support_tickets"          # Where this query came from
  
  # Ground truth for RETRIEVAL evaluation
  relevant_documents:
    - doc_id: "user_guide_export"
      chunk_ids: ["chunk_127", "chunk_128"]
      relevance: "high"              # high, medium, low
    - doc_id: "api_reference_export"
      chunk_ids: ["chunk_456"]
      relevance: "medium"
  
  # Ground truth for GENERATION evaluation
  reference_answer: |
    To export your data to CSV:
    1. Go to Settings > Data > Export
    2. Select "CSV" as the format
    3. Choose the date range for your data
    4. Click "Export"
    
    Your file will download automatically. Large exports may take a few minutes.
  
  # Specific requirements
  must_include:                      # Answer MUST mention these
    - "Settings"
    - "Export"
    - "CSV"
  must_not_include:                  # Answer must NOT mention these
    - "pricing"
    - "subscription"
  
  # Expected behavior
  expected_behavior: "direct_answer"  # direct_answer, clarify, decline, escalate
  
  # Notes
  notes: "Steps verified against v2.3. UI changed in v2.4 - update needed."
```

---

## Required Categories

Include examples from each category:

### 1. Simple Factual (Minimum: 4)

Questions with clear, single answers.

```yaml
- id: "factual_001"
  query: "What file formats are supported for import?"
  category: "simple_factual"
  difficulty: "simple"
  expected_behavior: "direct_answer"
```

**Why include:** Baseline. If the system can't handle these, something is fundamentally broken.

### 2. How-To (Minimum: 4)

Step-by-step procedural questions.

```yaml
- id: "howto_001"
  query: "How do I reset my password?"
  category: "how_to"
  difficulty: "simple"
  expected_behavior: "direct_answer"
```

**Why include:** Common user need. Tests ability to convey procedures clearly.

### 3. Troubleshooting (Minimum: 4)

Error resolution and debugging.

```yaml
- id: "trouble_001"
  query: "Why am I getting error 403 when I try to access the API?"
  category: "troubleshooting"
  difficulty: "medium"
  expected_behavior: "direct_answer"
```

**Why include:** High value. These are the queries that currently become support tickets.

### 4. Comparison (Minimum: 2)

Questions requiring synthesis across multiple sources.

```yaml
- id: "compare_001"
  query: "What's the difference between the Basic and Pro plans?"
  category: "comparison"
  difficulty: "medium"
  expected_behavior: "direct_answer"
```

**Why include:** Tests ability to synthesize. Requires pulling from multiple chunks.

### 5. Complex/Multi-Step (Minimum: 2)

Nuanced questions requiring deep understanding.

```yaml
- id: "complex_001"
  query: "How do I set up SSO with Okta for my team of 50 users?"
  category: "complex"
  difficulty: "hard"
  expected_behavior: "direct_answer"
```

**Why include:** Stress test. If the system handles these, it's robust.

### 6. Out of Scope (Minimum: 2)

Questions the system should NOT answer directly.

```yaml
- id: "oos_001"
  query: "What's your company's annual revenue?"
  category: "out_of_scope"
  difficulty: "simple"
  expected_behavior: "decline"
  reference_answer: "I can help with product documentation, but I don't have information about company financials."
```

**Why include:** Tests guardrails. System should gracefully decline, not hallucinate.

### 7. Ambiguous (Minimum: 2)

Unclear questions needing clarification.

```yaml
- id: "ambig_001"
  query: "How do I do the thing with the data?"
  category: "ambiguous"
  difficulty: "medium"
  expected_behavior: "clarify"
  reference_answer: "I'd be happy to help with your data. Could you tell me more about what you're trying to do? For example, are you looking to export, import, or analyze your data?"
```

**Why include:** Tests edge handling. System should ask for clarification, not guess.

---

## Building Your Dataset

### Step 1: Gather Real Queries

Best sources:
- Support ticket history (anonymized)
- Search logs
- User feedback
- Sales/customer success input
- Your own testing

**Don't invent queries.** Real queries are messier and more valuable.

### Step 2: Categorize and Deduplicate

Group similar queries. Keep one representative example per concept.

### Step 3: Identify Ground Truth

For each query:
1. Find the documents that contain the answer
2. Note specific chunks if using chunked retrieval
3. Write or identify the ideal answer

**This is labor-intensive.** It's also the most valuable part.

### Step 4: Define Requirements

For each query:
- What MUST the answer include?
- What must it NOT include?
- What's the expected behavior?

### Step 5: Validate

Have someone else review:
- Are the relevant docs actually relevant?
- Is the reference answer actually correct?
- Are the requirements reasonable?

### Step 6: Version and Maintain

- Track when examples were created/updated
- Note which product version they apply to
- Update when docs change

---

## Quality Checklist

For each example:

- [ ] Query is realistic (from real users or realistic scenario)
- [ ] Category is correctly assigned
- [ ] Difficulty is accurately assessed
- [ ] Relevant documents are correctly identified
- [ ] All relevant chunks are listed
- [ ] Reference answer is accurate and complete
- [ ] Must-include items are necessary (not just nice-to-have)
- [ ] Must-not-include items are genuinely problematic
- [ ] Expected behavior is appropriate
- [ ] Notes include any caveats or version info

For the dataset as a whole:

- [ ] All categories are represented
- [ ] Difficulty distribution is reasonable
- [ ] No duplicate or near-duplicate queries
- [ ] Examples cover the main documentation areas
- [ ] Edge cases are included

---

## Common Mistakes

### 1. Dataset Is Too Easy

If all examples are simple factual queries, you won't catch problems with harder cases.

**Fix:** Ensure balanced category distribution.

### 2. Reference Answers Are Wrong

If your ground truth is incorrect, your evaluation is meaningless.

**Fix:** Have domain experts validate reference answers.

### 3. Relevant Docs Are Incomplete

Missing relevant documents causes false negatives in retrieval evaluation.

**Fix:** Thorough review of all possible source documents.

### 4. Dataset Doesn't Match Production

If test queries don't represent real usage, you're optimizing for the wrong thing.

**Fix:** Use real queries whenever possible.

### 5. Dataset Is Static

Docs change. Products change. Static datasets become stale.

**Fix:** Regular review and update schedule.

---

## Example Golden Dataset

Here's a minimal starter dataset (20 examples):

```yaml
# golden_dataset.yaml

version: "1.0"
created_at: "2025-01-15"
product_version: "2.3"

examples:

  # ============ SIMPLE FACTUAL (4) ============
  
  - id: "factual_001"
    query: "What file formats can I import?"
    category: "simple_factual"
    difficulty: "simple"
    relevant_documents:
      - doc_id: "import_guide"
        chunk_ids: ["import_001"]
        relevance: "high"
    reference_answer: "You can import CSV, JSON, XML, and Excel (.xlsx) files."
    must_include: ["CSV", "JSON"]
    expected_behavior: "direct_answer"
  
  - id: "factual_002"
    query: "What is the maximum file size for uploads?"
    category: "simple_factual"
    difficulty: "simple"
    relevant_documents:
      - doc_id: "limits_guide"
        chunk_ids: ["limits_003"]
        relevance: "high"
    reference_answer: "The maximum file size for uploads is 100MB."
    must_include: ["100MB"]
    expected_behavior: "direct_answer"
  
  - id: "factual_003"
    query: "Which browsers are supported?"
    category: "simple_factual"
    difficulty: "simple"
    relevant_documents:
      - doc_id: "requirements"
        chunk_ids: ["req_002"]
        relevance: "high"
    reference_answer: "We support Chrome, Firefox, Safari, and Edge (latest two versions of each)."
    must_include: ["Chrome", "Firefox"]
    expected_behavior: "direct_answer"
  
  - id: "factual_004"
    query: "What's the API rate limit?"
    category: "simple_factual"
    difficulty: "simple"
    relevant_documents:
      - doc_id: "api_reference"
        chunk_ids: ["api_limits"]
        relevance: "high"
    reference_answer: "The API rate limit is 100 requests per minute per API key."
    must_include: ["100", "minute"]
    expected_behavior: "direct_answer"

  # ============ HOW-TO (4) ============
  
  - id: "howto_001"
    query: "How do I export my data to CSV?"
    category: "how_to"
    difficulty: "simple"
    relevant_documents:
      - doc_id: "export_guide"
        chunk_ids: ["export_001", "export_002"]
        relevance: "high"
    reference_answer: |
      To export your data to CSV:
      1. Go to Settings > Data > Export
      2. Select "CSV" as the format
      3. Choose the date range
      4. Click "Export"
    must_include: ["Settings", "Export", "CSV"]
    expected_behavior: "direct_answer"
  
  # ... (continue with remaining examples)
  
  # ============ TROUBLESHOOTING (4) ============
  
  - id: "trouble_001"
    query: "I'm getting error 403 when calling the API"
    category: "troubleshooting"
    difficulty: "medium"
    relevant_documents:
      - doc_id: "api_errors"
        chunk_ids: ["error_403"]
        relevance: "high"
      - doc_id: "api_auth"
        chunk_ids: ["auth_001"]
        relevance: "medium"
    reference_answer: |
      Error 403 means your API key doesn't have permission for this endpoint. Check that:
      1. Your API key is valid and not expired
      2. Your plan includes access to this endpoint
      3. You're using the correct API key for this environment
    must_include: ["permission", "API key"]
    expected_behavior: "direct_answer"
  
  # ... (continue)
  
  # ============ OUT OF SCOPE (2) ============
  
  - id: "oos_001"
    query: "What's your company's stock price?"
    category: "out_of_scope"
    difficulty: "simple"
    relevant_documents: []
    reference_answer: "I can help with product documentation, but I don't have information about company financials or stock prices."
    expected_behavior: "decline"
  
  # ... (continue)
  
  # ============ AMBIGUOUS (2) ============
  
  - id: "ambig_001"
    query: "How do I connect it?"
    category: "ambiguous"
    difficulty: "medium"
    relevant_documents: []
    reference_answer: "I'd be happy to help you connect. Could you tell me what you're trying to connect? For example, are you connecting to the API, a database integration, or a third-party service?"
    expected_behavior: "clarify"
```

---

## Maintenance Schedule

| Activity | Frequency | Owner |
|:---------|:----------|:------|
| Review for accuracy | Monthly | [Name] |
| Add new examples | After major releases | [Name] |
| Remove outdated examples | After major releases | [Name] |
| Validate reference answers | Quarterly | [Name] |
| Check category balance | Quarterly | [Name] |

---

## Next Steps

1. Create your `golden_dataset.yaml` following this structure
2. Start with 20 examples (minimum for meaningful evaluation)
3. Validate with domain experts
4. Expand to 50-100 examples as you learn what matters

---

*Template version: 1.0*
