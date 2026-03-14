---
workflow: Optimize Existing Funnel
agents: [conversion-scientist, landing-page-psychologist, copy-legend, ad-creative-genius]
duration: 1-2 weeks
complexity: medium
---

# Workflow: Optimize Existing Funnel

Systematic workflow for improving an existing funnel's conversion rate using data-driven optimization.

## Prerequisites

- [ ] Funnel has been running for 30+ days
- [ ] Minimum 1,000 visitors collected
- [ ] Analytics tracking configured
- [ ] Baseline metrics established

---

## PHASE 1: DIAGNOSIS (Days 1-2)

### Step 1.1: Analyze Current Metrics
**Agent:** @conversion-scientist
**Task:** `*analyze-metrics`

**Data to collect:**
```
Traffic Metrics:
- Impressions: _______
- Clicks: _______
- CPC: $_______
- CTR: _______%

Funnel Metrics:
- Landing page visits: _______
- Opt-ins: _______ (Rate: ____%)
- Sales page visits: _______
- Purchases: _______ (Rate: ____%)
- Overall conversion: _______%

Revenue Metrics:
- Revenue: $_______
- AOV: $_______
- ROAS: _______x
- LTV: $_______
- CAC: $_______
- LTV:CAC: _______:1
```

**Identify the BIGGEST leak:**
```
Ad → Landing: ___% (Target: 30-50%)
Landing → Sales: ___% (Target: varies)
Sales → Purchase: ___% (Target: 2-5% cold, 10-20% warm)
```

**Output:** Leak identification report + top 3-5 optimization opportunities

---

### Step 1.2: Heatmap Analysis (if available)
**Agent:** @landing-page-psychologist
**Task:** `*heatmap-analysis`

**Tools:** Hotjar, Microsoft Clarity

**Analyze:**
- Where users click (click maps)
- How far users scroll (scroll maps)
- Where users rage-click (frustration)
- Where users drop off (exit points)

**Key insights:**
- Is CTA getting clicked?
- Are users reading key sections?
- Where do they abandon?

---

## PHASE 2: PRIORITIZE FIXES (Day 2)

### Step 2.1: Impact vs Effort Matrix

**Quick Wins (High Impact, Low Effort):**
1. Add order bump (+10-20% AOV, 1-2 days)
2. Reduce form fields (-2 fields = +20-40% CR, 1 hour)
3. Add/strengthen guarantee (+20-30% CR, 2 hours)
4. Fix slow load time (+25-50% CR if >3 sec, 1 day)

**Major Projects (High Impact, High Effort):**
5. Rewrite headline (+10-50% CR, 1 week with testing)
6. Redesign sales page (+20-50% CR, 1-2 weeks)
7. Add video testimonials (+30-50% CR, 1 week)
8. Rebuild email sequence (+10-30% sales, 1 week)

**Select Top 3:**
Based on current data, prioritize:
1. _______________
2. _______________
3. _______________

---

## PHASE 3: IMPLEMENT FIXES (Days 3-7)

### Quick Win #1: Add Order Bump
**Agent:** @funnel-architect
**Task:** Add checkbox offer on checkout

**Implementation:**
```
On checkout page, add:
☐ YES! Add [Complement Product] for just $[Price]
   (Normally $[Higher Price], save $[Savings])
```

**Best practices:**
- Related to main offer
- Price: 20-40% of main offer
- Clear value (what they get)
- Default unchecked (ethical)

**Expected lift:** +10-20% AOV
**Test:** A/B test with/without bump

---

### Quick Win #2: Reduce Form Friction
**Agent:** @landing-page-psychologist
**Task:** Minimize form fields

**Current fields:** _______
**Remove:** _______
**New total:** ≤3 fields (name, email, payment)

**Progressive profiling:**
- Collect only essentials now
- Get more data later (email, surveys)

**Expected lift:** +20-40% conversion

---

### Quick Win #3: Strengthen Guarantee
**Agent:** @copy-legend
**Task:** Upgrade guarantee copy

**Current:** 30-day money-back
**Upgrade to:** 60-90 day "Better-Than-Risk-Free"

**Example:**
> "60-Day Better-Than-Risk-Free Guarantee
>
> Try [Product] for 60 days. If you don't see [specific result], not only will we refund every penny, but we'll also [bonus/extra] as our apology for wasting your time. You literally cannot lose."

**Placement:**
- Above-the-fold (landing page)
- Before main CTA (sales page)
- In email sequence

**Expected lift:** +20-30% conversion

---

### Major Project: Headline A/B Test
**Agent:** @copy-legend
**Task:** `*write-headline`

**Create 5-10 variations:**
1. Current (control)
2. Benefit-focused ("Get [Result] in [Timeframe]")
3. Curiosity ("The [Adjective] Secret to [Result]")
4. Contrarian ("Stop [Common Approach], Do This Instead")
5. Question ("What if [Intriguing Possibility]?")
6-10. Additional variations

**Testing protocol:**
- A/B test vs control
- Run until 95% confidence
- Minimum 1,000 conversions per variant
- Pick winner, test next

**Expected lift:** +10-50% (huge variance)

---

### Major Project: Optimize Landing Page
**Agent:** @landing-page-psychologist
**Task:** `*optimize-page`

**Run full audit:**
- `landing-page-checklist.md` (70 points)
- LIFT Model score
- Cialdini 7 Principles check

**Common fixes:**
1. **Above-the-fold:**
   - Headline stronger (benefit + curiosity)
   - Subhead clarifies (who it's for)
   - CTA visible (contrasting color)
   - Trust signals present

2. **Friction removal:**
   - Form fields ≤3
   - Page load <3 sec
   - Mobile-optimized
   - Clear next step

3. **Anxiety reduction:**
   - Guarantee prominent
   - Testimonials visible
   - Trust badges present
   - FAQ addresses objections

**Expected lift:** +20-50% (if currently weak)

---

## PHASE 4: TEST & MEASURE (Days 8-14)

### Step 4.1: A/B Testing Protocol

**For each change:**

**Setup:**
- Control (original)
- Variant (optimized)
- 50/50 traffic split

**Run until:**
- 95% statistical significance
- OR 1,000 conversions per variant
- OR 2 weeks (whichever comes first)

**Measure:**
- Conversion rate
- Revenue per visitor
- AOV (if order bump test)

**Decision:**
- Winner = deploy to 100%
- Loser = archive and try next

---

### Step 4.2: Monitor Key Metrics

**Daily checks (first week):**
- [ ] Conversion rate (vs baseline)
- [ ] Revenue (vs baseline)
- [ ] Errors/bugs (fix immediately)

**Weekly checks:**
- [ ] Traffic quality (same sources?)
- [ ] Seasonal effects (holidays, events)
- [ ] Competition changes

---

## PHASE 5: ITERATE (Week 2+)

### Step 5.1: Compound Wins

After first win, test next priority:

**Round 1:** Quick wins (order bump, form, guarantee)
**Round 2:** Headlines + copy
**Round 3:** Page design + layout
**Round 4:** Email sequences
**Round 5:** Ad creatives (refresh)

**Compound effect:**
- Order bump: +15% AOV
- Form optimization: +30% CR
- Headline: +20% CR
- **Combined:** ~75% improvement!

---

### Step 5.2: Monthly Review
**Agent:** @conversion-scientist
**Task:** `*analyze-metrics` (full analysis)

**Compare:**
- Month 1 (baseline) vs Month 2 (optimized)
- Traffic sources (which improved most?)
- Cohorts (new customers better?)

**Plan next month:**
- What to test next?
- What to scale?
- What to kill?

---

## SUCCESS CRITERIA

### Week 1 (Quick Wins):
- ✅ At least 1 improvement deployed
- ✅ Metrics stable (no breaks)
- ✅ Data collecting for tests

### Week 2 (A/B Tests):
- ✅ First winner identified
- ✅ 10-30% improvement vs baseline
- ✅ Next tests queued

### Month 2 (Compounding):
- ✅ 50-100%+ total improvement
- ✅ Multiple winners deployed
- ✅ Continuous testing process

---

## COMMON OPTIMIZATION PLAYBOOK

### If CTR is low (<2%):
**Agent:** @ad-creative-genius
**Fix:** Refresh ad creatives
- Test new hooks
- Try different angles
- Use UGC-style videos
- Add social proof to ads

---

### If Opt-in Rate is low (<30%):
**Agent:** @landing-page-psychologist
**Fix:** Optimize squeeze page
- Stronger headline
- Better lead magnet
- Reduce form fields
- Add social proof

---

### If Sales CR is low (<2% cold):
**Agent:** @copy-legend
**Fix:** Improve sales page
- Value stack clearer
- Guarantee stronger
- More social proof
- Address objections (FAQ)

---

### If AOV is low:
**Agent:** @funnel-architect
**Fix:** Invisible Funnel
- Add order bump
- Add upsell flow
- Add downsell (if declined)
- Bundle products

---

### If LTV:CAC is low (<3:1):
**Agent:** @conversion-scientist
**Fix:** Improve unit economics
- Increase LTV (upsells, retention)
- Decrease CAC (better targeting, creative)
- Add backend offers
- Improve retention

---

## BENCHMARKS TO BEAT

| Metric | Current | Target | Excellent |
|--------|---------|--------|-----------|
| CTR | ___% | 2%+ | 3%+ |
| Opt-in | ___% | 30-50% | 50%+ |
| Sales CR | ___% | 2-5% | 5%+ |
| AOV | $___ | +20% | +50% |
| ROAS | ___x | 3x+ | 5x+ |
| LTV:CAC | ___:1 | 3:1+ | 5:1+ |

---

## ANTI-PATTERNS (Don't Do This)

❌ **Testing multiple things at once** (can't isolate what works)
❌ **Stopping tests too early** (<95% confidence = false winner)
❌ **Changing too many things** (break what's working)
❌ **Ignoring mobile** (60%+ traffic)
❌ **No baseline** (can't measure improvement)
❌ **Analysis paralysis** (test something, don't just plan)

---

## OPTIMIZATION CHECKLIST

**Before starting:**
- [ ] Baseline metrics documented
- [ ] Tracking verified accurate
- [ ] Traffic sources stable
- [ ] Minimum 1,000 visitors

**During optimization:**
- [ ] One variable per test
- [ ] 95% confidence before calling winner
- [ ] Monitor for bugs/breaks
- [ ] Document all changes

**After optimization:**
- [ ] Results documented
- [ ] Winners deployed to 100%
- [ ] Next tests queued
- [ ] Team informed of wins

---

**Remember:** Optimization is a continuous process. 1% improvement every week = 67% improvement in a year!

📈 Always be testing, always be improving.

— Squad, optimizing relentlessly
