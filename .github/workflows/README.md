# GitHub Workflows

This directory contains automated workflows for maintaining the Awesome-Prompt-Engineering repository.

## Continuous Documentation Workflows

These workflows automate documentation maintenance, ensuring accuracy, consistency, and user-friendliness.

### 1. Daily Documentation Updater

**File**: `daily-doc-updater.yml` / `daily-doc-updater.md`  
**Schedule**: Daily at midnight UTC  
**Trigger**: `workflow_dispatch` (manual trigger also available)

Reviews and updates documentation to ensure:
- Technical accuracy and correctness
- Consistency in terminology, formatting, and style
- Valid links and current references
- Completeness of information

**Expected Merge Rate**: ~96%

**How it works**:
1. Reviews all major documentation files
2. Identifies outdated information, broken links, and inconsistencies
3. Creates a pull request with updates when issues are found
4. Skips PR creation if no updates are needed

---

### 2. Glossary Maintainer

**File**: `glossary-maintainer.yml` / `glossary-maintainer.md`  
**Trigger**: Push to main branch (when .md files change)  
**Also runs on**: Pull requests modifying .md files

Keeps the AI_Glossary.md synchronized with the codebase by:
- Detecting new technical terms in documentation
- Adding missing definitions to the glossary
- Updating existing definitions to match current usage
- Maintaining alphabetical order and consistent formatting

**Expected Merge Rate**: ~100%

**How it works**:
1. Analyzes recently changed documentation files
2. Identifies new AI/ML/prompt engineering terms
3. Adds missing terms with clear, concise definitions
4. Creates a pull request when glossary updates are needed

---

### 3. Documentation Unbloat

**File**: `doc-unbloat.yml` / `doc-unbloat.md`  
**Schedule**: Weekly on Sunday at midnight UTC  
**Trigger**: `workflow_dispatch` (manual trigger also available)

Reviews documentation to reduce verbosity and improve clarity by:
- Eliminating redundant information
- Simplifying complex sentences
- Removing unnecessary jargon
- Improving readability and flow

**Expected Merge Rate**: ~85%

**How it works**:
1. Identifies verbose or overly complex content
2. Simplifies language while maintaining technical accuracy
3. Improves structure with better headings and formatting
4. Creates a pull request with simplification suggestions

**Targets ~15-20% word count reduction** where bloat exists.

---

### 4. Documentation Noob Tester

**File**: `doc-noob-tester.yml` / `doc-noob-tester.md`  
**Schedule**: Monthly on the 1st at midnight UTC  
**Trigger**: `workflow_dispatch` (manual trigger also available)

Simulates a new user journey to identify:
- Confusing or unclear explanations
- Missing prerequisites or assumed knowledge
- Broken or circular navigation
- Gaps in the learning journey
- Examples that don't work or are hard to follow

**How it works**:
1. Walks through documentation as a beginner would
2. Tests the learning path from basic to advanced topics
3. Identifies pain points and unclear sections
4. Creates GitHub issues for genuine problems (limited to 3-5 most important issues)

**Issues created are labeled**: `documentation`, `beginner-experience`

---

## Issue Triage Workflow

### Issue Triage Agent

**File**: `issue-triage-agent.yml` / `issue-triage-agent.md`  
**Trigger**: Issues opened or reopened

Automatically triages new issues by:
- Analyzing issue title and body
- Adding appropriate labels
- Commenting with context and suggestions

---

## Security Workflow

### Daily Secrets Analysis

**File**: `daily-secrets-analysis.md`

Scans the repository for exposed secrets and credentials.

---

## Manual Triggers

All documentation workflows support manual triggering via `workflow_dispatch`. To run a workflow manually:

1. Go to the **Actions** tab in GitHub
2. Select the workflow you want to run
3. Click **Run workflow**
4. Confirm the run

---

## Workflow Philosophy

These workflows challenge conventional wisdom about AI-generated technical content. While human review remains essential, these agents provide a dramatically better baseline than the alternative (no documentation at all), effectively addressing documentation drift.

### Key Principles

- **Accuracy**: Content must be technically correct
- **Clarity**: Use simple, direct language
- **Conciseness**: Get to the point, avoid fluff
- **Consistency**: Follow established structure and formatting

### Review Process

1. Workflows create pull requests or issues
2. Maintainers review the suggestions
3. Accept valuable changes, reject or modify others
4. Human oversight ensures quality control

---

## Contributing

When adding new workflows:

1. Create both a `.yml` file (GitHub Actions configuration) and a `.md` file (agent instructions)
2. Follow the existing pattern (see `issue-triage-agent.yml` as reference)
3. Set appropriate permissions
4. Use the `github/gh-aw` action for agent-based workflows
5. Document the workflow in this README

---

## Questions?

For questions about these workflows, please open an issue or refer to the [Contributing Guide](../../Contributing.md).
