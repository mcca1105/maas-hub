# Task: Create Split Test Plan

**Agent:** ryan-deiss
**Tier:** 2
**Type:** Analysis + Planning
**Elicit:** true

## Purpose
Design a structured A/B testing sequence that generates reliable data and systematic
improvements — not random tests that produce noise.
Ryan Deiss's principle: "You don't test to find winners. You test to understand WHY
something works, so you can replicate and scale it."

## The Testing Hierarchy

```
LEVEL 1 — Biggest Impact (test these first):
├── Offer (what you're offering)
├── Audience (who you're targeting)
└── Big Idea / Angle (the core promise)

LEVEL 2 — High Impact (test after Level 1):
├── Headline / Hook (how you open)
├── Price point
└── Lead type (VSL vs. long-form vs. webinar)

LEVEL 3 — Optimization (test after Level 2):
├── Copy elements (bullets, subheads, CTAs)
├── Visual design (colors, images, layout)
└── Minor copy variations (word choices, formats)
```

**Rule:** Never test Level 3 variables before Level 1-2 are validated.
Optimizing the wrong offer is a waste of budget.

## Inputs Required
- Current baseline metrics (existing conversion rates, if any)
- Campaign type (email / landing page / ad / full funnel)
- Traffic volume available for testing
- Budget per test
- Primary conversion goal

## Execution Steps

### Step 1: Test Readiness Assessment

Before testing, assess if you have sufficient traffic for valid results:

```yaml
traffic_assessment:
  current_daily_visitors: "[Number]"
  current_conversion_rate: "[% or 'no baseline']"
  monthly_conversions: "[Current count]"

  minimum_sample_size_calc:
    # Rule: Need 200+ conversions per variant minimum for statistical significance
    baseline_cr: "[e.g., 2%]"
    min_daily_traffic_needed: "[200 / (CR × days) = daily traffic needed]"

  test_readiness:
    status: "[READY / NOT READY — need more traffic first]"
    if_not_ready: "[Action: increase traffic before testing; test traffic acquisition first]"
```

### Step 2: Define the Test Hierarchy for This Campaign

```yaml
test_roadmap:
  phase_1_macro_tests:
    # What to test first — big swings
    test_1:
      variable: "[Offer A vs. Offer B]"
      hypothesis: "[If we change X, then Y will happen because Z]"
      control: "[Current version — describe]"
      variant: "[New version — describe]"
      primary_metric: "[Conversion rate / CPL / ROAS]"
      secondary_metrics: "[CTR / AOV / LTV]"
      traffic_split: "50/50"
      sample_needed: "[Number per variant for 95% confidence]"
      duration: "[Days to reach sample size]"

    test_2:
      variable: "[Audience Segment A vs. B — if offer test passes]"
      hypothesis: "[Hypothesis]"
      # Continue...

  phase_2_mid_tests:
    # After Phase 1 winner identified
    test_3:
      variable: "[Headline — 3-4 variations]"
      hypothesis: "[Hypothesis]"
      duration: "[Timeline]"

  phase_3_micro_tests:
    # Fine-tuning after Phase 2 winner
    test_4:
      variable: "[CTA button text / copy element]"
      hypothesis: "[Hypothesis]"
```

### Step 3: Statistical Validity Requirements

```yaml
statistical_requirements:
  confidence_level: "95% minimum (99% for large-scale decisions)"
  minimum_conversions_per_variant: 200
  maximum_simultaneous_variables: 1
  # Never test 2 variables at once — can't know what caused the difference

  runtime_rules:
    minimum: "14 days regardless of traffic (day-of-week effects)"
    stop_early_only_if: "One variant is clearly hurting (50%+ worse) — stop to prevent damage"
    never_stop_early_because: "One is winning — regression to mean is real"

  results_interpretation:
    winner_criteria: "Statistical significance + business significance (delta large enough to matter)"
    inconclusive: "[If results show <5% difference — not worth deploying; test bigger variables]"
    loser_analysis: "[Why did the loser lose? What does this tell us about the audience?]"
```

### Step 4: Define Metrics and Tracking

```yaml
metrics_framework:
  primary_metric:
    name: "[Conversion rate / CPL / ROAS — single primary]"
    definition: "[Exact action counted as conversion]"
    tracking: "[How it's tracked — pixel / UTM / server-side]"

  secondary_metrics:
    - name: "[CTR]"
      role: "Diagnostic — if CTR increases but CR doesn't, issue is landing page"
    - name: "[Time on page]"
      role: "Diagnostic — if low, copy isn't engaging"
    - name: "[Scroll depth]"
      role: "Diagnostic — where are people abandoning"
    - name: "[Revenue per visitor]"
      role: "Business metric — secondary to CR for initial tests"

  tracking_setup:
    tool: "[Google Analytics / Facebook Pixel / Custom — what to use]"
    utm_structure: "[Standard UTM params for this test]"
    conversion_window: "[How long after click to count conversion — 1 day / 7 day / 30 day]"
    attribution_model: "[Last click / first click / data-driven — and why]"
```

### Step 5: Write the Test Plan Document

```yaml
test_plan:
  test_id: "TEST-[YYYYMM]-[sequence number]"
  test_name: "[Descriptive name]"
  created_by: "[Agent/person]"
  start_date: "[Date]"
  end_date: "[Projected — based on sample size needed]"

  hypothesis:
    if: "[We change X]"
    then: "[Y metric will improve by Z%]"
    because: "[Reasoning — what do we believe about buyer psychology here?]"

  control:
    description: "[What the control version is]"
    url: "[URL if applicable]"
    screenshot: "[File path if applicable]"

  variant:
    description: "[What the variant version is]"
    change_made: "[Specifically what is different — nothing else]"
    url: "[URL]"

  traffic_split: "[50/50 or other — specify]"
  traffic_source: "[Where traffic is coming from]"

  success_criteria:
    winner_if: "[Variant converts at X% higher with 95% confidence]"
    no_change_if: "[Difference < 5% after minimum sample reached]"
    loser_if: "[Variant converts at X% lower — stop early trigger]"

  actions_after_test:
    if_variant_wins: "[Deploy winner, begin Phase 2 test]"
    if_no_change: "[Move up test hierarchy — test bigger variable]"
    if_control_wins: "[Investigate variant. What did this tell us?]"
```

### Step 6: Testing Calendar

```yaml
testing_calendar:
  month_1:
    week_1_2: "Macro test 1 — Offer"
    week_3_4: "Analyze results + set up Macro test 2"

  month_2:
    week_1_2: "Macro test 2 — Audience or Angle"
    week_3_4: "Analyze + set up Mid test"

  month_3:
    week_1_2: "Mid test — Headline"
    week_3_4: "Mid test — Price (if applicable)"

  ongoing: "Micro tests (copy elements) running in background"

  parallel_testing_rules:
    allowed: "Test different elements on DIFFERENT pages/campaigns simultaneously"
    not_allowed: "Test 2 variables on the SAME page at the same time"
```

## Quality Standards
- One variable tested at a time (no multi-variable tests)
- Minimum 200 conversions per variant before calling winner
- 14-day minimum regardless of traffic volume
- Hypothesis includes causal reasoning (not just "we think this will work better")
- Test hierarchy follows Level 1 → Level 2 → Level 3 order

## Veto Conditions
- VETO if testing Level 3 variables before Level 1-2 are validated
- VETO if fewer than 200 conversions planned per variant
- VETO if test runs fewer than 14 days
- VETO if two variables are changed in one test
- VETO if no hypothesis is written (fishing expeditions produce noise)

## Completion Criteria
- [ ] Traffic assessment done (is there enough traffic to test?)
- [ ] Test hierarchy defined (Level 1 first)
- [ ] Statistical requirements set (confidence level, minimum sample)
- [ ] Metrics and tracking configured
- [ ] Test plan document complete for first test
- [ ] Testing calendar mapped for 3 months

## Handoff
- → write-ad-variations.md (create the actual ad variants to test)
- → diagnose-funnel-leak.md (if baseline is unknown — diagnose first)
- → write-facebook-ad-copy.md / write-landing-page-copy.md (for copy variant creation)

---
*Task: DRM_SPLIT_001 | Agent: ryan-deiss | Version: 1.0*
