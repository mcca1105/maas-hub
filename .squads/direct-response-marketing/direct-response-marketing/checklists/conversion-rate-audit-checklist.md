# Conversion Rate Audit Checklist
**Agent:** `@drm:robert-cialdini` / `@drm:ryan-deiss`
**Purpose:** Systematic diagnostic for any page that is underperforming
**Standard:** Cialdini Persuasion Audit + Deiss CVO Diagnostic
**Run:** When any funnel step has conversion rate below benchmark

---

## CONVERSION BENCHMARKS (Target Ranges)

| Funnel Step | Cold Traffic | Warm Traffic | Hot Traffic |
|------------|-------------|-------------|------------|
| Opt-in page | 15-25% | 25-45% | 40-60% |
| Tripwire page | 1-3% total | 5-10% total | 10-20% total |
| Sales page (Core Offer) | 0.5-2% total | 2-5% total | 5-10% total |
| Upsell page | 15-25% of buyers | 20-35% of buyers | 25-40% of buyers |
| Email open rate | 15-25% | 25-40% | 40-60% |
| Email click rate | 1-3% | 3-8% | 8-15% |

**Current metric being audited:** ___________________
**Current rate:** ____% | **Target:** ____% | **Gap:** ____%

---

## 🔴 CRITICAL — Root Cause Layer

### Layer 1: Traffic Quality (Halbert — Market First)
- [ ] Traffic source confirmed: ___________________
- [ ] Traffic temperature matches page type: Cold → Lead Magnet / Core Offer → Warm only
- [ ] Are there signals of bot/low-quality traffic? (High bounce rate <5 seconds, no scroll)
- [ ] Geographic targeting appropriate (not sending US offer to global untargeted)

**Traffic quality verdict:** Good / Suspect / Unknown

### Layer 2: Awareness Mismatch (Schwartz)
- [ ] Awareness stage of traffic confirmed
- [ ] Copy is calibrated to that stage
- [ ] Common mismatch: Cold Facebook ads → directly to sales page (Stage 1-2 audience hit with Stage 4-5 copy)

**Awareness match verdict:** MATCH / MISMATCH (copy is [X] stages above/below)

### Layer 3: Offer Weakness (Deiss)
- [ ] The value-to-price ratio is obvious without thinking
- [ ] The guarantee removes all perceived risk
- [ ] Competitors offer something this doesn't (bonuses, better guarantee, lower price)
- [ ] Price is appropriate for the traffic temperature

**Offer strength verdict:** Strong / Adequate / Weak

---

## 🟡 HIGH PRIORITY — Persuasion Layer

### Cialdini Persuasion Gaps
Score each principle 0-3 in the page being audited:

| Principle | Score (0-3) | Primary Gap |
|-----------|------------|-------------|
| Reciprocity — value given before ask | | |
| Commitment — small steps before big ask | | |
| Social Proof — specific results, right placement | | |
| Authority — relevant credentials | | |
| Liking — personal, relatable voice | | |
| Scarcity — real urgency/deadline | | |
| Unity — shared identity | | |

**Total Persuasion Score: ___/21**
**Lowest score principle (primary fix):** ___________________

### Specific Copy Weaknesses
- [ ] Headline passes the "would I stop scrolling?" test: YES / NO
- [ ] First paragraph earns the second paragraph: YES / NO
- [ ] All claims are specific (numbers, names, timeframes): YES / NO
- [ ] "You" outnumbers "we/I" 3:1: YES / NO
- [ ] No passive voice ("it can be seen" → "you'll see"): YES / NO
- [ ] Guarantee is bold and stated clearly: YES / NO
- [ ] CTA is specific ("Click the yellow button below"): YES / NO

---

## 🟢 BEST PRACTICE — Technical Layer

### Page Performance
- [ ] Page load time under 3 seconds (check PageSpeed Insights)
- [ ] Mobile experience verified (conversion on mobile vs. desktop compared)
- [ ] No broken images, videos that don't load, or form errors
- [ ] SSL certificate active (padlock visible in browser)

### Friction Points
- [ ] Number of fields in opt-in form: ___
  - Opt-in: should be 1 field (email only) or 2 max (name + email)
  - Checkout: minimal required fields only
- [ ] Number of clicks to complete desired action: ___
  - Should be 1-2 clicks maximum for any conversion event
- [ ] Is there anything on the page that takes the visitor AWAY from converting?
  - [ ] Navigation menu? (Should be removed from conversion pages)
  - [ ] Social media links? (Remove from conversion pages)
  - [ ] Multiple CTAs pointing to different offers? (Dilutes focus)

---

## CONVERSION AUDIT DIAGNOSIS MATRIX

After completing all layers, identify the single most likely cause:

| Root Cause | Likely If... | Fix |
|-----------|------------|-----|
| Wrong traffic source | High traffic, near-zero conversion | Change traffic targeting |
| Awareness mismatch | Good traffic, early page exits | Rewrite to match stage |
| Weak offer | People read but don't buy | Improve guarantee/bonuses/price |
| Social proof insufficient | People read, hesitate, leave | Add specific testimonials |
| Headline failure | High bounce rate, short session | A/B test 5 headlines |
| CTA unclear | People reach bottom but don't act | Rewrite CTA, add multiple |
| Page speed / mobile | Mobile conversion <<< desktop | Fix technical issues |

**Primary diagnosis:** ___________________
**Recommended single fix to test first:** ___________________

---

## AUDIT REPORT FORMAT

```
CONVERSION RATE AUDIT REPORT

Page/Step: ___________________
Current Rate: ____% | Target: ____% | Gap: ____%
Date: ___________________

LAYER 1 — TRAFFIC: PASS / FAIL / FLAG
Notes: ___________________

LAYER 2 — AWARENESS: MATCH / MISMATCH
Notes: ___________________

LAYER 3 — OFFER: Strong / Adequate / Weak
Notes: ___________________

PERSUASION SCORE: ___/21
Lowest principle: ___________________

TOP 3 FIXES (in priority order):
1. ___________________
2. ___________________
3. ___________________

NEXT TEST: ___________________
Expected impact: ____%
```

---

*Checklist by Robert Cialdini (Persuasion Framework) + Ryan Deiss (CVO Diagnostic)*
*DRM Squad — Direct Response Marketing*
