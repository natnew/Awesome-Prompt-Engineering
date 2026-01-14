[← Back: Communication](04_communication.md) | [Next: Learning →](06_learning.md)

# Module 5: Recovery

Getting back to normal — safely.

---

## Recovery Is Not Just "Turning It Back On"

Recovery requires:
1. Verifying the fix actually works
2. Restoring service gradually
3. Confirming the problem is truly gone
4. Monitoring for recurrence

---

## Recovery Stages

### Stage 1: Fix Verified

Before restoring:
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Fix tested in staging (if possible)
- [ ] Rollback plan ready

### Stage 2: Gradual Restoration

Don't go 0→100. Go 0→10→25→50→100.

**Methods:**
- Feature flags (enable for % of users)
- Canary deployment
- Geographic rollout
- Customer tier rollout

**Monitor at each stage:**
- Error rates
- Latency
- Quality metrics
- User feedback

### Stage 3: Full Restoration

When confidence is high:
- Enable for all users
- Continue monitoring
- Keep rollback ready

### Stage 4: Stabilization

For 24-48 hours after:
- Enhanced monitoring
- Lower alert thresholds
- Faster response if issues recur

---

## Recovery Checklist

```markdown
## Recovery Checklist

### Before Enabling

- [ ] Fix is deployed
- [ ] Fix is tested
- [ ] Rollback plan documented
- [ ] Monitoring dashboards ready
- [ ] Stakeholders notified

### Gradual Rollout

- [ ] Enabled for 10% of traffic
- [ ] Monitored for 15 minutes
- [ ] Metrics look normal
- [ ] Increased to 25%
- [ ] Monitored for 15 minutes
- [ ] [Continue until 100%]

### After Full Restoration

- [ ] All metrics normal
- [ ] No user complaints
- [ ] Resolution communication sent
- [ ] Incident marked resolved
- [ ] Post-mortem scheduled

### Next 24-48 Hours

- [ ] Enhanced monitoring active
- [ ] Team aware to watch for recurrence
```

---

## AI-Specific Recovery Considerations

### Quality Verification

How do you know AI responses are good again?

**Approaches:**
- Run evaluation suite before enabling
- Compare sample responses to known-good
- Start with low-stakes queries
- Enable human review initially

### State and Cache

AI systems may have state that needs clearing:
- Vector database updates
- Model caches
- Conversation history
- User preferences

**Ask:** "Is there stale state that needs clearing?"

---

## Your Task

Create a recovery procedure:
1. Verification steps for your AI system
2. Gradual rollout plan
3. Monitoring checklist
4. Stabilization period procedures

---

[← Back: Communication](04_communication.md) | [Next: Learning →](06_learning.md)
