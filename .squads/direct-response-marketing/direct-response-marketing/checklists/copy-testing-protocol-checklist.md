# Copy Testing Protocol Checklist
**Agent:** `@drm:drm-chief`
**Purpose:** Validate split test setup before running — ensures clean, actionable data
**Standard:** Halbert "test obsessively" principle + conversion rate optimization best practices
**Run:** Before ANY A/B or split test goes live

---

## 🔴 CRITICAL — Test Design Validity

### Single Variable Rule
- [ ] Only ONE variable is being tested (headline, CTA, price, image, etc.)
- [ ] ALL other page elements are identical between variants
- [ ] If two things were changed, it's not a split test — it's a redesign (restart)

**Variable being tested:** ___________________
**Hypothesis:** "Changing [variable] from [A] to [B] will increase [metric] because [reason]"
```
_______________________________________________________________
```

### Statistical Requirements
- [ ] Minimum sample size calculated before starting:
  - For 5% significance improvement: ~1,600 visitors per variant
  - For 10% significance improvement: ~400 visitors per variant
  - Use VWO or Optimizely's sample size calculator
- [ ] Expected test duration calculated (based on current traffic)
  - Test runs minimum 7 days (to capture weekly patterns)
  - Test does NOT end before reaching minimum sample size
- [ ] Win condition defined BEFORE test starts (not changed mid-test)

**Win condition:** "[Variant B wins if] conversion rate exceeds [threshold] with [confidence level]% confidence"
```
_______________________________________________________________
```

### Tracking Setup
- [ ] Conversion goal configured correctly in testing tool
- [ ] Goal fires ONLY on success (purchase confirmation, opt-in thank-you)
- [ ] Goal does NOT fire on page reload (duplicate conversion prevention)
- [ ] Both variants confirmed loading correctly (visual check)
- [ ] Traffic split is 50/50 (or documented non-50/50 ratio with reason)

---

## 🟡 HIGH PRIORITY — Test Prioritization

### PIE Framework (Pre-Test Validation)
Before running the test, score the hypothesis:
- **Potential:** How much could this improve conversion? (1-10)
- **Importance:** How much traffic goes through this page? (1-10)
- **Ease:** How easy is this to implement? (1-10)

**PIE Score:** (P + I + E) / 3 = _____ / 10
- Score 7+: High priority test — run immediately
- Score 4-6: Medium priority — run after high-priority tests
- Score below 4: Low priority — skip for now

### Test Priority Queue
Tests in order of expected impact (highest PIE first):
1. Headline (highest impact)
2. CTA button text and color
3. Hero image / video vs. no video
4. Price point
5. Guarantee terms
6. Offer structure (bonuses included/excluded)
7. Long-form vs. short-form copy
8. Social proof placement

---

## 🟢 BEST PRACTICE — Documentation

### Pre-Test Documentation
- [ ] Current (control) metrics documented BEFORE test starts:
  - Current conversion rate: ____%
  - Current traffic: ____ visitors/week
  - Current revenue per visitor: $____
- [ ] Hypothesis and expected improvement documented
- [ ] Test start date recorded

### Post-Test Documentation
- [ ] Winner recorded with final conversion rates for both variants
- [ ] Statistical confidence level at test end: ____%
- [ ] If Winner = B: implement on control immediately
- [ ] If Winner = A (no change): document WHY hypothesis was wrong (learning)
- [ ] Learning documented in split-test results swipe file

### Split Test Results Log
All test results logged in:
```
Test: [Variable tested]
Date: [Start] – [End]
Control (A): [Description] — Conversion: ____%
Variant (B): [Description] — Conversion: ____%
Winner: A / B
Confidence: ____%
Learning: _______________
```

---

## ❌ AUTO-FAIL CONDITIONS

- [ ] ❌ More than one variable changed between variants
- [ ] ❌ Test ended before minimum sample size reached
- [ ] ❌ Win condition changed after test started (p-hacking)
- [ ] ❌ Test ran for less than 7 days (seasonal/weekly variation not captured)
- [ ] ❌ Conversion goal fires on page reload (inflated conversions)
- [ ] ❌ Test results not documented (learning lost)
- [ ] ❌ Winning variant not implemented within 72 hours of test end

---

## COPY TEST PRIORITY LIST (DRM Standard)

Test in this order for maximum impact:
| Priority | Element | Expected Impact |
|---------|---------|----------------|
| 1 | Headline | 20-40% conversion swing |
| 2 | Main CTA (text + color) | 10-20% swing |
| 3 | Hero image / video present | 10-30% swing |
| 4 | Guarantee terms | 5-15% swing |
| 5 | Price point | 10-50% swing |
| 6 | Lead copy (first 200 words) | 10-20% swing |
| 7 | Bullet positioning | 5-10% swing |
| 8 | P.S. copy | 3-8% swing |

---

*Checklist — Split Test Protocol (Gary Halbert "test obsessively" principle)*
*DRM Squad — Direct Response Marketing*
