# Detection Thresholds

## Overview

This document defines the thresholds and metrics for event detection and evaluation.

---

## Classification Thresholds

### Category Assignment

| Category | Significance Score | Confidence | Additional Criteria |
|:---------|:-------------------|:-----------|:--------------------|
| **Critical** | >0.9 | >0.9 | AND urgency >0.9 |
| **Significant** | >0.7 | >0.8 | - |
| **Interesting** | >0.3 | >0.6 | - |
| **Known Type** | any | >0.8 | Matches known pattern |
| **Unknown** | any | <0.5 | Can't classify |
| **Routine** | <0.3 | >0.7 | Normal variation |
| **Artifact** | - | >0.9 | Matches artifact pattern |

### Score Definitions

| Score | Range | Meaning |
|:------|:------|:--------|
| Significance | 0-1 | Scientific importance if real |
| Confidence | 0-1 | Certainty in classification |
| Urgency | 0-1 | Time sensitivity for follow-up |
| Anomaly | 0-1 | Deviation from normal patterns |

---

## Alert Thresholds

### Alert Triggers

| Alert Level | Trigger Condition | Response Time Target |
|:------------|:------------------|:---------------------|
| **CRITICAL** | Category=critical | <5 minutes |
| **HIGH** | Significance>0.8 AND confidence>0.7 | <30 minutes |
| **MEDIUM** | Significance>0.5 AND confidence>0.6 | <4 hours |
| **LOW** | Significance>0.3 | <24 hours |

### Alert Channels

| Level | Channels |
|:------|:---------|
| CRITICAL | SMS, Phone, Slack, Email |
| HIGH | Slack, Email |
| MEDIUM | Email, Queue |
| LOW | Queue only |

---

## Filtering Thresholds

### Quality Filter

| Check | Threshold | Action if Fail |
|:------|:----------|:---------------|
| SNR | >3 | Reject |
| Position uncertainty | <10 arcsec | Flag |
| Timing accuracy | <1 sec | Flag |
| Calibration status | Applied | Reject |

### Artifact Filter

| Artifact Type | Detection Method | Threshold |
|:--------------|:-----------------|:----------|
| Cosmic ray | Sharp PSF, single pixel | Confidence >0.9 |
| Satellite trail | Linear feature | Confidence >0.8 |
| Hot pixel | Fixed position, persistent | Confidence >0.95 |
| Chip edge | Position near edge | Distance <50px |
| Bad column | Column pattern | Confidence >0.9 |

### Known Object Filter

| Check | Parameters |
|:------|:-----------|
| Cross-match radius | 2 arcsec |
| Magnitude tolerance | ±1 mag |
| Catalog priority | Gaia > PS1 > 2MASS |

---

## Performance Targets

### Detection Performance

| Metric | Target | Warning | Critical |
|:-------|:-------|:--------|:---------|
| Critical recall | >99.9% | <99.5% | <99% |
| Significant recall | >99% | <98% | <95% |
| Interesting recall | >95% | <90% | <85% |
| Alert precision | >50% | <40% | <30% |
| Queue precision | >10% | <8% | <5% |

### Latency Performance

| Metric | Target | Warning | Critical |
|:-------|:-------|:--------|:---------|
| Critical alert (p99) | <5min | >4min | >5min |
| Significant (p99) | <30min | >25min | >30min |
| Processing (p50) | <1min | >45s | >1min |
| Processing (p99) | <5min | >4min | >5min |

### System Performance

| Metric | Target | Warning | Critical |
|:-------|:-------|:--------|:---------|
| Throughput | >1000/s | <800/s | <500/s |
| Queue depth | <10,000 | >10,000 | >50,000 |
| Error rate | <0.1% | >0.1% | >1% |
| Uptime | >99.9% | <99.9% | <99.5% |

---

## Calibration Requirements

### Confidence Calibration

| Bin | Expected Accuracy | Tolerance |
|:----|:------------------|:----------|
| 0.0-0.1 | 5% | ±5% |
| 0.1-0.2 | 15% | ±5% |
| 0.2-0.3 | 25% | ±5% |
| 0.3-0.4 | 35% | ±5% |
| 0.4-0.5 | 45% | ±5% |
| 0.5-0.6 | 55% | ±5% |
| 0.6-0.7 | 65% | ±5% |
| 0.7-0.8 | 75% | ±5% |
| 0.8-0.9 | 85% | ±5% |
| 0.9-1.0 | 95% | ±5% |

**Target ECE:** <0.1

### Calibration Method

```python
def calibrate_confidence(raw_scores: np.ndarray, labels: np.ndarray) -> Calibrator:
    """Train confidence calibrator."""
    
    # Isotonic regression for calibration
    calibrator = IsotonicRegression(out_of_bounds='clip')
    calibrator.fit(raw_scores, labels)
    
    return calibrator

def compute_ece(predictions: np.ndarray, labels: np.ndarray, n_bins: int = 10) -> float:
    """Compute Expected Calibration Error."""
    
    bin_boundaries = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    
    for i in range(n_bins):
        in_bin = (predictions >= bin_boundaries[i]) & (predictions < bin_boundaries[i+1])
        if in_bin.sum() > 0:
            bin_confidence = predictions[in_bin].mean()
            bin_accuracy = labels[in_bin].mean()
            bin_weight = in_bin.sum() / len(predictions)
            ece += bin_weight * abs(bin_confidence - bin_accuracy)
    
    return ece
```

---

## Threshold Tuning

### Tuning Process

1. **Baseline measurement** - Measure current performance
2. **Identify gaps** - Where are we missing targets?
3. **Adjust thresholds** - Change one threshold at a time
4. **A/B test** - Run both in parallel
5. **Measure impact** - Compare metrics
6. **Deploy or revert** - Based on results

### Tuning Constraints

| Constraint | Description |
|:-----------|:------------|
| Critical recall | Never reduce below 99% |
| Alert volume | Max 2x baseline per day |
| Latency | Never exceed hard limits |

### Tuning Schedule

| Review | Frequency | Scope |
|:-------|:----------|:------|
| Operational | Weekly | Latency, throughput |
| Performance | Monthly | Recall, precision |
| Calibration | Quarterly | Confidence calibration |

---

## Monitoring Thresholds

### Real-Time Alerts

| Metric | Condition | Alert Level |
|:-------|:----------|:------------|
| Critical latency | >5min | CRITICAL |
| Processing errors | >1% | HIGH |
| Queue depth | >50,000 | HIGH |
| Throughput drop | <50% baseline | HIGH |
| Injection test fail | Any | MEDIUM |

### Dashboard Indicators

| Indicator | Green | Yellow | Red |
|:----------|:------|:-------|:----|
| Latency | <target | <warning | >warning |
| Recall | >target | >warning | <warning |
| Precision | >target | >warning | <warning |
| Queue | <10k | <50k | >50k |

---

## Threshold Documentation

### Change Log

| Date | Threshold | Old Value | New Value | Reason |
|:-----|:----------|:----------|:----------|:-------|
| [Date] | [Name] | [Old] | [New] | [Why changed] |

### Approval Requirements

| Change Type | Approver |
|:------------|:---------|
| Critical thresholds | Science Lead + Ops Lead |
| Alert thresholds | Ops Lead |
| Filter thresholds | Science Lead |
| Performance targets | System Owner |

---

## Sign-Off

| Role | Name | Date |
|:-----|:-----|:-----|
| Science Lead | | |
| Operations Lead | | |
| System Owner | | |
