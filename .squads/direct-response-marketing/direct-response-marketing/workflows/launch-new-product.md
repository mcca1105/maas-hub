---
workflow: Launch New Product
agents: [funnel-architect, vsl-master, copy-legend, ad-creative-genius, landing-page-psychologist, conversion-scientist]
duration: 2-4 weeks
complexity: high
---

# Workflow: Launch New Product

Complete workflow for launching a new product using all 6 agents in coordinated sequence.

## Prerequisites

- [ ] Product created and validated
- [ ] Target audience defined
- [ ] Pricing determined
- [ ] Offer components ready
- [ ] Launch timeline set

---

## PHASE 1: STRATEGY (Week 1)

### Step 1.1: Design Complete Funnel
**Agent:** @funnel-architect
**Task:** `*design-funnel`

**Input:**
- Business model
- Target audience
- Current offers (if any)
- Traffic source

**Output:**
- Complete Value Ladder (free → premium)
- Funnel architecture (page-by-page)
- Email sequences mapped
- Conversion targets set

**Checklist:** `funnel-review-checklist.md`

---

### Step 1.2: Define Grand Slam Offer
**Agent:** @ad-creative-genius
**Task:** `*create-offer` (using Hormozi framework)

**Input:**
- Product details
- Target audience pain/desire
- Competition analysis

**Output:**
- Dream Outcome defined
- Perceived Likelihood maximized
- Time Delay minimized
- Effort minimized
- Value Stack created

**Validation:** Total value should be 10x+ price

---

## PHASE 2: COPY CREATION (Week 1-2)

### Step 2.1: Create VSL Script (if webinar funnel)
**Agent:** @vsl-master
**Task:** `*create-vsl-script`

**Input:**
- Product/offer
- Target audience
- Research data (Amazon, forums)
- Unique mechanism
- Price point

**Output:**
- Complete 15-25 min VSL script
- Timing breakdown
- CTA placements (70%, 85%, 95%, 100%)
- Visual production notes

**Checklist:** `vsl-review-checklist.md`
**Template:** `vsl-script-template.md`

---

### Step 2.2: Write Sales Letter
**Agent:** @copy-legend
**Task:** `*write-sales-letter`

**Input:**
- Product/offer
- Awareness stage (Solution Aware recommended)
- Target audience
- Price point

**Output:**
- Long-form sales letter (3,000-10,000 words)
- 10+ headline variations (tested)
- 15-20 fascination bullets
- Complete with guarantee, P.S., CTAs

**Checklist:** `sales-letter-checklist.md`
**Template:** `sales-letter-template.md`

---

### Step 2.3: Write Email Sequences
**Agent:** @funnel-architect
**Task:** `*email-sequence`

**Sequences needed:**
1. **Soap Opera** (5 emails) - Pre-launch nurture
2. **Sales** (7 emails) - Open cart period
3. **Indoctrination** (3-5 emails) - New leads

**Checklist:** Validate each sequence for:
- Story arc (Soap Opera)
- Daily consistency (Sales)
- Value delivery (Indoctrination)

**Template:** `email-sequence-template.md`

---

## PHASE 3: CREATIVE PRODUCTION (Week 2)

### Step 3.1: Create Ad Campaign
**Agent:** @ad-creative-genius
**Task:** `*create-ad-campaign`

**Input:**
- Product/offer
- Target audience
- Platform (Meta, TikTok, YouTube)
- Budget

**Output:**
- 10+ angles for testing
- 3-5 creative variations per angle
- Hook-Story-Offer structure
- Testing roadmap (48-72h per variant)

**Checklist:** `ad-creative-checklist.md`
**Template:** `ad-creative-brief-template.md`

---

### Step 3.2: Optimize Landing Pages
**Agent:** @landing-page-psychologist
**Task:** `*design-page` or `*optimize-page`

**Pages needed:**
1. **Registration** (if webinar) - 30-50% opt-in target
2. **Sales page** - Value stack + guarantee
3. **Order form** - Minimal fields + order bump
4. **Thank you** - Next steps + upsell opportunity

**For each page:**
- Apply LIFT Model (Value + Incentive - Friction - Anxiety)
- Apply Cialdini 7 Principles
- Mobile-first design
- Load time < 3 seconds

**Checklist:** `landing-page-checklist.md` (each page)

---

## PHASE 4: SETUP & INTEGRATION (Week 2-3)

### Step 4.1: Configure Tracking
**Agent:** @conversion-scientist
**Task:** `*setup-tracking`

**Setup required:**
- [ ] Google Analytics 4 + GTM
- [ ] Conversion events (opt-in, purchase, upsell)
- [ ] Pixel tracking (Meta, Google, TikTok)
- [ ] UTM parameters (all ad links)
- [ ] Dashboard (Looker Studio)

**Validation:**
- Test all tracking fires correctly
- Verify conversions register
- Confirm dashboard populates

---

### Step 4.2: Build Funnel Pages
**Technical Implementation:**

1. **Landing pages** (Unbounce, Instapage, or custom)
2. **Email sequences** (ActiveCampaign, ConvertKit)
3. **Payment processing** (Stripe, ThriveCart)
4. **Order bumps** (checkbox on checkout)
5. **Upsell/downsell flows** (one-click)

**Test end-to-end:**
- [ ] Ad → Landing → Opt-in → Email → Webinar/Sales → Purchase → Upsell → Thank You
- [ ] All emails send correctly
- [ ] Payment processes successfully
- [ ] Order bumps add to cart
- [ ] Upsells show correctly

---

## PHASE 5: PRE-LAUNCH VALIDATION (Week 3)

### Step 5.1: Run All Checklists
**All Agents:**

- [ ] VSL validated (`vsl-review-checklist.md`)
- [ ] Sales letter validated (`sales-letter-checklist.md`)
- [ ] Ads validated (`ad-creative-checklist.md`)
- [ ] Funnel validated (`funnel-review-checklist.md`)
- [ ] Landing pages validated (`landing-page-checklist.md`)
- [ ] **MASTER CHECKLIST** (`pre-launch-master-checklist.md`)

**Pass threshold:** 90%+ on master checklist

---

### Step 5.2: Load Testing & Final Checks

**Traffic test:**
- Can site handle expected traffic?
- Load time under load < 3 seconds?

**Payment test:**
- Test transactions ($0.01 tests)
- Refund process works?

**Email test:**
- All sequences loaded?
- Links work?
- Unsubscribe functions?

---

## PHASE 6: LAUNCH (Week 3-4)

### Day 1: Soft Launch
- [ ] Turn on tracking
- [ ] Enable ads (small budget $100-500)
- [ ] Monitor dashboard (first 6 hours)
- [ ] Check for errors/bugs
- [ ] Verify conversions tracking

**Success criteria:**
- No critical bugs
- Conversions tracking correctly
- Funnel flows smoothly

---

### Day 2-7: Scale Testing
- [ ] Test ad angles (10+ variations)
- [ ] Monitor key metrics daily
- [ ] Kill losing angles (CTR < 2%, CPA > target)
- [ ] Scale winning angles (2x budget)

**Metrics to watch:**
- CTR: >2%
- CPA: < target
- Conversion rate: 1-5%
- ROAS: >3x

---

### Week 2-4: Optimization
- [ ] A/B test landing pages
- [ ] Test email subject lines
- [ ] Optimize ad creatives
- [ ] Adjust targeting
- [ ] Scale winners aggressively

**Agent:** @conversion-scientist
**Task:** `*analyze-metrics` (weekly)

---

## PHASE 7: POST-LAUNCH (Ongoing)

### Weekly Reviews
**Agent:** @conversion-scientist

Analyze:
- Funnel conversion rates
- LTV:CAC ratio
- Top-performing traffic sources
- Email performance
- Optimization opportunities

---

### Monthly Optimization
**All Agents:**

- [ ] Refresh ad creatives (ad fatigue)
- [ ] Test new VSL/sales letter variations
- [ ] Optimize funnel bottlenecks
- [ ] Review and improve email sequences
- [ ] Update benchmarks

---

## SUCCESS METRICS

### Week 1 (Soft Launch):
- ✅ No critical bugs
- ✅ Conversions tracking
- ✅ Positive initial metrics

### Week 2-4 (Scale):
- ✅ ROAS > 3x
- ✅ Funnel CR > 1%
- ✅ LTV:CAC > 3:1

### Month 2-3 (Optimize):
- ✅ ROAS > 5x
- ✅ Funnel CR > 2%
- ✅ LTV:CAC > 5:1

---

## ROLLBACK PLAN

If launch fails:

1. **Pause ads** (stop spending)
2. **Analyze data** (@conversion-scientist)
3. **Identify blocker** (conversion leak)
4. **Fix critical issue**
5. **Re-validate** (run checklists)
6. **Relaunch** (soft launch again)

---

## TOTAL TIMELINE

- **Week 1:** Strategy + Copy
- **Week 2:** Creative + Pages
- **Week 3:** Setup + Validation
- **Week 4:** Launch + Scale

**Total:** 3-4 weeks from start to scaled launch

---

**This workflow ensures every element is validated, tested, and optimized before and after launch.**

🚀 Ready to launch products that WIN.
