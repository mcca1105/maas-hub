# Task: Diagnose Funnel Leak

**Agent:** ryan-deiss
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Identify exactly where a funnel is bleeding conversion before touching any copy.
Ryan Deiss's principle: before optimizing anything, know WHERE to optimize.
Changing the wrong thing wastes time; finding the real leak saves campaigns.

## Prerequisites
- Funnel is live and receiving traffic
- Analytics installed and tracking (Google Analytics, Meta Pixel, etc.)
- Access to conversion data for each funnel step

## Execution Steps

### Step 1: Map the Complete Funnel

Document every step of the funnel with current data:

```yaml
funnel_map:
  name: "[Funnel name]"
  traffic_source: "[Facebook / Google / Email / etc.]"
  monthly_traffic: [number]
  monthly_revenue: "$[amount]"

  steps:
    step_1:
      name: "Ad Impression to Click"
      url: "[Ad]"
      metric: "CTR"
      current: "[X%]"
      benchmark: "Facebook cold: 0.5-2% | Google: 3-8%"
      status: "[above/at/below benchmark]"

    step_2:
      name: "Landing Page to Opt-in or Purchase"
      url: "[Landing page URL]"
      metric: "CVR"
      current: "[X%]"
      benchmark:
        squeeze_cold: "25-45%"
        squeeze_warm: "45-65%"
        sales_page: "1-5%"
        webinar_reg: "20-40%"
      status: "[above/at/below benchmark]"

    step_3:
      name: "Checkout Page"
      url: "[Checkout URL]"
      metric: "Checkout completion rate"
      current: "[X%]"
      benchmark: "50-70% of page visitors"
      status: "[above/at/below benchmark]"

    step_4:
      name: "OTO1 Take Rate"
      url: "[OTO1 URL]"
      metric: "Take rate"
      current: "[X%]"
      benchmark: "15-35%"
      status: "[above/at/below benchmark]"

    # Add all relevant steps
```

### Step 2: Benchmark Comparison

```yaml
benchmark_reference:
  # TRAFFIC METRICS
  ctr_benchmarks:
    facebook_cold: "0.5-2.0%"
    facebook_retargeting: "1.0-3.0%"
    google_search: "3-8%"
    youtube_instream: "View rate 15-30% before skip"

  # PAGE METRICS
  page_cvr_benchmarks:
    squeeze_page_cold_traffic: "25-45%"
    squeeze_page_warm_traffic: "45-65%"
    vsl_page_opt_in: "15-35%"
    webinar_registration: "20-40%"
    sales_page_cold: "0.5-2%"
    sales_page_warm: "2-5%"
    sales_page_hot: "5-15%"
    checkout_completion: "50-70%"
    order_bump_take_rate: "20-40%"
    oto1_take_rate: "15-35%"
    oto2_take_rate: "10-25%"

  # EMAIL METRICS
  email_benchmarks:
    open_rate_cold: "10-20%"
    open_rate_warm: "25-45%"
    ctr: "2-5%"
    unsubscribe_per_send: "<0.5%"
```

### Step 3: Identify the Primary Leak Point

The "primary leak" is the step with the LARGEST gap between current performance and benchmark.

```yaml
leak_analysis:
  primary_leak_step: "[Step name]"
  current_performance: "[X%]"
  benchmark: "[Y%]"
  gap: "[Z% below benchmark]"
  revenue_impact_of_fixing: |
    "If we fix this step to [benchmark], monthly revenue would increase by approximately $[amount]"

  secondary_leak_step: "[Step name — second biggest gap]"
  secondary_gap: "[Z% below benchmark]"
```

### Step 4: Root Cause Hypothesis

For each leak point, hypothesize causes in priority order:

```yaml
root_cause_analysis:
  primary_leak:
    step: "[Step name]"
    possible_causes:

      # ALWAYS CHECK TECHNICAL ISSUES FIRST
      technical_issues:
        - issue: "[Page load time >3 seconds?]"
          check: "Use GTmetrix or PageSpeed Insights"
          status: "[checked/unchecked]"
        - issue: "[Mobile rendering broken?]"
          check: "Test on actual mobile devices"
          status: "[checked/unchecked]"
        - issue: "[Pixel/tracking firing correctly?]"
          check: "Meta Pixel Helper / Google Tag Assistant"
          status: "[checked/unchecked]"
        - issue: "[Payment processor issues?]"
          check: "Test checkout manually with real card"
          status: "[checked/unchecked]"

      # THEN CHECK TRAFFIC QUALITY
      traffic_quality:
        - issue: "[Traffic source mismatch? (wrong audience)]"
          check: "Review demographic breakdown vs. avatar"
        - issue: "[Bot traffic? (unusually high CTR, zero conversions)]"
          check: "IP analysis, bounce rate, session duration"
        - issue: "[Message-to-market mismatch? (ad says X, page says Y)]"
          check: "Screenshot ad + landing page side by side"

      # THEN CHECK COPY/OFFER
      copy_and_offer:
        - issue: "[Headline not speaking to cold traffic?]"
        - issue: "[Offer not clear?]"
        - issue: "[Price shock without anchoring?]"
        - issue: "[No guarantee visible?]"
        - issue: "[CTA buried?]"
```

### Step 5: Prioritized Test Plan

Based on diagnosis, create a test plan in order:

```yaml
test_plan:
  rule: "Fix technical before testing copy. Fix traffic before testing offer."

  week_1_fixes:  # Low-hanging fruit — implement without A/B testing
    - fix: "[Technical issue — just fix it]"
      expected_impact: "[high/medium]"

  test_1:  # First A/B test after technical fixes
    hypothesis: "IF we [change X] THEN [metric] will increase by [Y%] BECAUSE [reason]"
    control: "[Current version]"
    challenger: "[New version]"
    primary_metric: "[CVR / CTR / Open rate]"
    sample_size_needed: "[Calculate: 95% confidence, 10% lift minimum]"
    estimated_duration: "[days]"

  test_2:  # After Test 1 concludes
    hypothesis: "..."
    # etc.

  what_not_to_test_yet:
    - "[Element that should wait until higher-priority leaks are fixed]"
```

### Step 6: Quick Wins Identification

Some issues can be fixed immediately without A/B testing:

```yaml
quick_wins:
  implement_immediately:
    - "[Technical fix that's clearly broken]"
    - "[Missing element — guarantee not showing, CTA below fold, etc.]"
    - "[Obvious mismatch between ad and landing page]"

  do_not_implement_without_testing:
    - "[Offer change — always A/B test offers]"
    - "[Headline rewrite — always test]"
    - "[Price change — significant business impact, test carefully]"
```

## Quality Standards
- Every funnel step has a benchmark for comparison (not just the number in isolation)
- Technical issues checked BEFORE assuming copy problems
- Traffic quality investigated BEFORE assuming offer problems
- Primary leak quantified in revenue impact (makes fixing it feel urgent)
- Test plan is sequenced (not random list of tests)

## Veto Conditions
- VETO if audit starts by changing copy before checking technical issues
- VETO if benchmarks are not used for comparison (numbers without context are meaningless)
- VETO if revenue impact is not calculated (leadership needs to understand the cost of the leak)
- VETO if more than 3 tests are planned before results from Test 1 are known
- VETO if traffic quality is not investigated (bad copy and bad traffic look the same in data)

## Completion Criteria
- [ ] Full funnel map with current metrics at every step
- [ ] Benchmark comparison for every step
- [ ] Primary and secondary leak points identified
- [ ] Root cause hypotheses documented (technical → traffic → copy order)
- [ ] Quick wins identified (implement immediately)
- [ ] Sequenced test plan (Test 1 → wait for results → Test 2)
- [ ] Revenue impact of fixing primary leak calculated

## Handoff
- → audit-existing-copy.md (if copy is diagnosed as the leak cause)
- → create-split-test-plan.md (to execute the test plan)
- → write-facebook-ad-copy.md (if ad-to-page mismatch is the issue)
- → write-landing-page-copy.md (if page copy is diagnosed as the leak)

---
*Task: DRM_DIAG_001 | Agent: ryan-deiss | Version: 1.0*
