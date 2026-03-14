---
workflow: A/B Test Campaign
agents: [conversion-scientist, landing-page-psychologist, ad-creative-genius, copy-legend]
duration: 2-4 weeks per test cycle
complexity: medium
---

# Workflow: A/B Test Campaign

Systematic testing protocol for continuous conversion rate optimization.

## Core Principle

> "Test one variable at a time, run until statistical significance, deploy winners, test next."

---

## TESTING PHASES

### Phase 1: Big Swings (Week 1-2)
**Expected lift:** 10-50% per win
**Tests:** Headlines, offers, hero images

### Phase 2: Elements (Week 3-4)
**Expected lift:** 5-20% per win
**Tests:** Form fields, CTAs, social proof placement

### Phase 3: Polish (Week 5+)
**Expected lift:** 2-10% per win
**Tests:** Button colors, micro-copy, layout tweaks

---

## STATISTICAL REQUIREMENTS

### Minimum Standards (CRITICAL):
- ✅ **Sample size:** 1,000+ conversions per variant (or 95% confidence)
- ✅ **Confidence level:** 95% minimum
- ✅ **Test duration:** Minimum 1 week (account for day-of-week variance)
- ✅ **Traffic split:** 50/50 (equal distribution)

### When to Stop:
- ✅ 95%+ confidence reached
- ✅ Clear winner emerged
- ✅ Minimum 1 week passed

### When to Keep Running:
- ⚠️ < 95% confidence
- ⚠️ Results flip-flopping
- ⚠️ < 1 week duration

---

## PHASE 1: BIG SWINGS

### Test 1: Headlines
**Agent:** @copy-legend
**Task:** `*write-headline`

**Hypothesis:** Different headline will increase conversion

**Variants to test (pick 2-3):**
1. **Control:** Current headline
2. **Benefit-focused:** "Get [Specific Result] in [Timeframe]"
3. **Curiosity:** "The [Surprising] Secret to [Desired Outcome]"
4. **Question:** "What if [Intriguing Possibility]?"
5. **Contrarian:** "Stop [Common Approach], Do This Instead"

**Example:**
```
Control: "Welcome to Our Course"
Variant A: "Get Your First $10k Client in 30 Days"
Variant B: "The 'Backwards' Method Top Consultants Use to Land Clients"
```

**Expected lift:** 10-50%
**Run time:** 1-2 weeks or 1,000 conversions

---

### Test 2: Hero Image/Video
**Agent:** @landing-page-psychologist
**Task:** `*ab-test-plan`

**Hypothesis:** Video outperforms static image

**Variants:**
1. **Control:** Static image (current)
2. **Variant A:** Testimonial video (30-60 sec)
3. **Variant B:** Product demo video (30-60 sec)
4. **Variant C:** Transformation before/after (static)

**Best practices:**
- Video must have captions (80% watch muted)
- Auto-play on mute
- Clear CTA at end

**Expected lift:** 10-30%
**Run time:** 1-2 weeks

---

### Test 3: Offer/Value Stack
**Agent:** @ad-creative-genius
**Task:** Test offer presentation

**Hypothesis:** Clearer value stack increases conversion

**Variants:**
1. **Control:** Simple price
2. **Variant A:** Value stack breakdown (each component priced)
3. **Variant B:** Value stack + discount percentage
4. **Variant C:** Value stack + scarcity ("Only X left")

**Example:**
```
Control:
"Get access for $297"

Variant A:
✓ Core Course ($997 value)
✓ Bonus 1 ($297 value)
✓ Bonus 2 ($197 value)
Total Value: $1,491
Your Price: $297 (80% OFF)
```

**Expected lift:** 15-40%
**Run time:** 1-2 weeks

---

## PHASE 2: ELEMENTS

### Test 4: Form Fields
**Agent:** @landing-page-psychologist
**Task:** Reduce friction

**Hypothesis:** Fewer fields = higher conversion

**Variants:**
1. **Control:** 5 fields (name, email, phone, company, size)
2. **Variant A:** 3 fields (name, email, phone)
3. **Variant B:** 2 fields (name, email)

**Rule:** Every field you remove = +10-20% conversion

**Expected lift:** 20-40% (5 → 2 fields)
**Run time:** 1 week

---

### Test 5: Guarantee Placement
**Agent:** @copy-legend
**Task:** Test guarantee visibility

**Hypothesis:** Guarantee above-the-fold increases trust

**Variants:**
1. **Control:** Guarantee at bottom only
2. **Variant A:** Guarantee above-the-fold + bottom
3. **Variant B:** Guarantee badge visible throughout scroll

**Expected lift:** 10-20%
**Run time:** 1-2 weeks

---

### Test 6: Social Proof Format
**Agent:** @landing-page-psychologist
**Task:** Test proof type

**Hypothesis:** Video testimonials outperform text

**Variants:**
1. **Control:** Text testimonials with photos
2. **Variant A:** Video testimonials (30-60 sec each)
3. **Variant B:** Mixed (video + text)
4. **Variant C:** Live counter ("Join 10,482 customers...")

**Expected lift:** 20-40%
**Run time:** 1-2 weeks

---

## PHASE 3: POLISH

### Test 7: CTA Button Copy
**Agent:** @copy-legend
**Task:** Test button text

**Hypothesis:** Benefit-focused CTA converts better

**Variants:**
1. **Control:** "Submit"
2. **Variant A:** "Get Instant Access"
3. **Variant B:** "Start My Transformation"
4. **Variant C:** "Claim My Spot"

**Rule:** Use action verb + benefit

**Expected lift:** 2-10%
**Run time:** 1 week

---

### Test 8: Button Color
**Agent:** @landing-page-psychologist
**Task:** Test color psychology

**Hypothesis:** High contrast color increases clicks

**Variants:**
1. **Control:** Blue (current)
2. **Variant A:** Orange (urgency)
3. **Variant B:** Green (go/trust)
4. **Variant C:** Red (urgency/action)

**Rule:** Must contrast with page (4.5:1 minimum)

**Expected lift:** 2-5%
**Run time:** 1 week

---

### Test 9: Micro-Copy
**Agent:** @copy-legend
**Task:** Test supporting copy

**Hypothesis:** Better subheads increase engagement

**Elements to test:**
- Subheadlines
- Bullet points
- Image captions
- Form helper text

**Example:**
```
Control: "Enter your email"
Variant: "Get instant access (we never spam)"
```

**Expected lift:** 3-8%
**Run time:** 1 week

---

## AD CREATIVE TESTING

### Test 10: Ad Angles
**Agent:** @ad-creative-genius
**Task:** `*test-angles`

**Hypothesis:** Different angles appeal to different segments

**Angles to test (10+):**
1. **Problem/Pain:** "Still struggling with X?"
2. **Solution:** "This solves X without Y"
3. **Transformation:** "From A to B in C days"
4. **Authority:** "As featured on X"
5. **Urgency:** "Last chance to X"
6. **Contrarian:** "Stop doing X, do Y instead"
7. **Story:** "How I went from X to Y"
8. **Question:** "What if X were possible?"
9. **News:** "New study reveals X"
10. **Intention-based:** "Not for X, only for Y"

**Testing protocol:**
- $100-200 per angle
- 48-72 hours each
- Kill: CTR < 2% or CPA > target
- Scale: CTR > 2% AND CPA < target

**Expected:** 2-3 winners from 10 tests
**Run time:** 2 weeks

---

### Test 11: Creative Variations
**Agent:** @ad-creative-genius
**Task:** Test creative formats

**For each winning angle, test:**
1. **Static image** (single)
2. **Carousel** (3-5 images)
3. **Video** (15-30 sec)
4. **Video** (60-90 sec)
5. **UGC-style** (phone camera, authentic)

**Testing protocol:**
- 3-5 variations per angle
- $200-300 per creative
- 48-72 hours each

**Expected lift:** 20-50% (format matters)
**Run time:** 1-2 weeks

---

## TESTING PROTOCOL (STEP-BY-STEP)

### Step 1: Hypothesis
```
Hypothesis: Changing [variable] from [control] to [variant] will increase [metric] by [expected %]

Example:
"Changing headline from generic to benefit-focused will increase opt-in rate by 20-30%"
```

---

### Step 2: Setup Test
**Tools:** Google Optimize, VWO, Optimizely, or platform native

**Configuration:**
- Control (original): 50% traffic
- Variant (new): 50% traffic
- Primary metric: Conversion rate
- Secondary metrics: Revenue, AOV, time on page

---

### Step 3: Run Test
**Monitor daily:**
- [ ] Traffic split is 50/50 (not skewed)
- [ ] No technical errors
- [ ] Data collecting properly

**Check for significance:**
- Use calculator: https://www.optimizely.com/sample-size-calculator/
- Or tool built-in significance test

---

### Step 4: Analyze Results
**Agent:** @conversion-scientist
**Task:** `*analyze-test-results`

**Questions:**
1. Did we reach 95% confidence? (Yes/No)
2. What's the conversion lift? (____%)
3. Is the lift meaningful? (>10% = yes)
4. Any unexpected side effects? (bounce rate, time on page)

**Decision matrix:**
```
IF confidence ≥ 95% AND lift ≥ 10%:
  → WINNER! Deploy to 100%

IF confidence ≥ 95% AND lift < 10%:
  → Small win. Deploy if easy, or archive.

IF confidence < 95%:
  → Keep running (or abandon if taking too long)

IF variant LOSES:
  → Archive. Try next idea.
```

---

### Step 5: Deploy Winner
**Actions:**
- [ ] Turn off test (send 100% to winner)
- [ ] Document results (what won, why, lift %)
- [ ] Update baseline metrics
- [ ] Plan next test

---

### Step 6: Compound Wins
**Example cascade:**
```
Baseline CR: 10%

Test 1 (Headline): +20% → 12% CR
Test 2 (Hero video): +15% → 13.8% CR
Test 3 (Value stack): +25% → 17.25% CR
Test 4 (Form fields): +30% → 22.4% CR

Total lift: 124% (10% → 22.4%)
```

**Result:** 2.24x more conversions from same traffic!

---

## TESTING CALENDAR (Sample)

### Month 1: Big Swings
- **Week 1-2:** Headlines (3 variants)
- **Week 3-4:** Hero image/video

### Month 2: Elements
- **Week 5-6:** Form fields + Guarantee placement
- **Week 7-8:** Social proof format

### Month 3: Polish
- **Week 9:** CTA button (copy + color)
- **Week 10:** Micro-copy tests
- **Week 11-12:** Ad creative variations

### Ongoing:
- Always have 1-2 tests running
- Review monthly: what worked, what didn't
- Plan next quarter tests

---

## TOOLS & RESOURCES

### A/B Testing Tools:
- **Google Optimize** (free, discontinued but alternatives exist)
- **VWO** (Visual Website Optimizer)
- **Optimizely** (enterprise)
- **Convert** (privacy-focused)
- **Unbounce** (built-in for landing pages)

### Statistical Calculators:
- Optimizely Sample Size Calculator
- Evan Miller A/B Test Calculator
- VWO Duration Calculator

### Analytics:
- **Google Analytics 4** (conversion tracking)
- **Hotjar** (heatmaps, see what people do)
- **Microsoft Clarity** (free heatmaps)

---

## COMMON MISTAKES

❌ **Testing too many things at once** (can't isolate winner)
❌ **Stopping too early** (<95% confidence = false positive)
❌ **Declaring winner with <100 conversions** (not enough data)
❌ **Testing tiny things first** (start with big swings)
❌ **Ignoring mobile** (60%+ traffic - test mobile versions!)
❌ **No hypothesis** (test blindly = no learning)
❌ **Not documenting results** (can't build on wins)

---

## TESTING CHECKLIST

**Before test:**
- [ ] Clear hypothesis defined
- [ ] One variable only
- [ ] Baseline metrics documented
- [ ] Tool configured correctly
- [ ] Traffic split 50/50

**During test:**
- [ ] Monitor daily (no breaks)
- [ ] Check significance
- [ ] Watch for anomalies

**After test:**
- [ ] 95%+ confidence reached
- [ ] Results documented
- [ ] Winner deployed
- [ ] Next test planned

---

## SUCCESS METRICS

**Good testing program:**
- ✅ 1-2 tests running always
- ✅ 1-2 wins per month
- ✅ 50-100%+ improvement per quarter
- ✅ Continuous learning & iteration

**Excellent testing program:**
- ✅ 2-3 tests running always
- ✅ 2-4 wins per month
- ✅ 100-200%+ improvement per quarter
- ✅ Team culture of testing

---

**Remember:** Every test is a win. Even "losers" teach you what doesn't work. Keep testing, keep learning, keep improving.

📊 Test everything. Trust data, not opinions.

— Squad, always testing
