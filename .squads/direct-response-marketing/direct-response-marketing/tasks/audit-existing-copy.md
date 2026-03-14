# Task: Audit Existing Copy

**Agent:** drm-chief
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Systematically audit existing copy to diagnose conversion problems and prioritize fixes.
The drm-chief's role: triage the copy bleeding before prescribing the treatment.
Gary Halbert's principle: "Specificity is the cure for almost everything wrong with copy."

## Prerequisites
- Existing copy accessible (sales letter, VSL script, landing page, email, ad)
- Conversion data available (current CVR, benchmark for the industry)
- Traffic source identified (knowing the source helps diagnose copy vs. traffic issues)

## Inputs Required
- The copy asset to audit (file or pasted text)
- Current conversion metrics (CVR, open rate, CTR — whatever is available)
- Industry benchmark for comparison
- Traffic source and temperature

## Execution Steps

### Step 1: Structural Audit
Check if all critical elements are present:

```yaml
structural_checklist:
  headline:
    present: [yes/no]
    specific: [yes/no — has number, name, timeframe, or mechanism?]
    grade: "[A/B/C/D/F]"
    note: "[What's wrong or what's working?]"

  subheadline:
    present: [yes/no]
    supports_headline: [yes/no]
    grade: "[A/B/C/D/F]"

  lead_hook:
    present: [yes/no]
    type: "[story/question/bold claim/news/testimonial]"
    grabs_attention: [yes/no]
    grade: "[A/B/C/D/F]"

  problem_section:
    present: [yes/no]
    emotional_resonance: "[low/medium/high]"
    uses_their_language: [yes/no]
    grade: "[A/B/C/D/F]"

  mechanism:
    present: [yes/no]
    specific: [yes/no]
    credible: [yes/no]
    grade: "[A/B/C/D/F]"

  proof_stack:
    present: [yes/no]
    types_present: ["[testimonial/data/authority/demonstration]"]
    testimonial_quality: "[generic/specific/highly specific]"
    grade: "[A/B/C/D/F]"

  offer_presentation:
    present: [yes/no]
    value_stack_clear: [yes/no]
    guarantee_present: [yes/no]
    grade: "[A/B/C/D/F]"

  urgency_scarcity:
    present: [yes/no]
    genuine: [yes/no]
    reason_given: [yes/no]
    grade: "[A/B/C/D/F]"

  cta:
    present: [yes/no]
    specific: [yes/no]
    above_fold: [yes/no]
    grade: "[A/B/C/D/F]"
```

### Step 2: Specificity Audit
Count specifics vs. generics throughout the copy:

**Scan for:**
```
GENERIC (problems): "many people," "great results," "significant improvement," "high quality"
SPECIFIC (good): "47 people," "lost 31 pounds," "in 6 weeks," "published in JAMA 2024"
```

```yaml
specificity_audit:
  total_claims_found: [number]
  specific_claims: [number]
  generic_claims: [number]
  specificity_ratio: "[XX%]"
  benchmark: "Good copy = >70% specific claims"
  verdict: "[Pass/Fail]"

  worst_generic_examples:
    - "[Line from copy that is dangerously generic]"
    - "[Another example]"

  best_specific_examples:
    - "[Line that models great specificity — keep this approach]"
```

### Step 3: Flow Analysis
Does the copy move logically from opening to CTA?

Evaluate the narrative arc:
```yaml
flow_analysis:
  does_opening_match_avatar: [yes/no]
  is_problem_emotionally_charged: [yes/no]
  does_mechanism_follow_problem_naturally: [yes/no]
  is_proof_placed_before_price: [yes/no]
  does_urgency_appear_before_cta: [yes/no]
  overall_flow: "[smooth/choppy/broken]"
  biggest_flow_break: "[Where does the copy lose momentum?]"
```

### Step 4: Objection Coverage
Are the 5 most common objections handled?

```yaml
objection_audit:
  primary_objections:
    - objection: "Price — 'It's too expensive'"
      addressed_in_copy: [yes/no]
      where_addressed: "[Section or line number]"
      quality_of_response: "[strong/weak/missing]"

    - objection: "Skepticism — 'This probably won't work for me'"
      addressed_in_copy: [yes/no]
      where_addressed: "[Section or line number]"
      quality_of_response: "[strong/weak/missing]"

    - objection: "Time — 'I don't have time for this'"
      addressed_in_copy: [yes/no]
      quality_of_response: "[strong/weak/missing]"

    - objection: "Past failure — 'I've tried similar things before'"
      addressed_in_copy: [yes/no]
      quality_of_response: "[strong/weak/missing]"

    - objection: "Risk — 'What if I buy and it doesn't work?'"
      addressed_in_copy: [yes/no]
      guarantee_quality: "[strong/weak/missing]"
```

### Step 5: Priority Fixes (Ranked by Expected CVR Impact)

Diagnose and prioritize:

```yaml
audit_results:
  overall_grade: "[A/B/C/D/F]"
  current_cvr: "[X%]"
  expected_cvr_with_fixes: "[Y%]"
  estimated_revenue_impact: "[approximate %]"

  critical_fixes:  # Fix these FIRST — biggest CVR impact
    1:
      problem: "[Specific problem]"
      current: "[What the copy says now]"
      fix: "[Specific recommendation]"
      expected_impact: "[high]"

    2:
      problem: "[Specific problem]"
      fix: "[Specific recommendation]"
      expected_impact: "[high]"

  important_fixes:  # Fix after critical
    3:
      problem: "[Specific problem]"
      fix: "[Specific recommendation]"
      expected_impact: "[medium]"

  minor_fixes:  # Nice to have
    4-6:
      - "[Quick fix with small impact]"

  what_is_working:  # Don't touch these
    - "[Element that is strong — preserve it]"
    - "[Another strong element]"
```

## Quality Standards
- Audit is based on the actual copy (not memory or assumption)
- Specificity ratio calculated quantitatively (not subjectively)
- Priority order based on estimated CVR impact (not personal preference)
- "What is working" section is mandatory (don't recommend destroying everything)
- Each recommended fix is specific (not "add more proof" — say exactly what proof)

## Veto Conditions
- VETO if audit doesn't have access to actual CVR data (can still audit structure, but must note limitation)
- VETO if specificity audit is done without counting claims
- VETO if all 5 objections are not audited
- VETO if priority order is not established (random list of problems = useless)
- VETO if "what is working" section is skipped (avoid throwing out the good with the bad)

## Completion Criteria
- [ ] Structural checklist complete (all 9 sections graded)
- [ ] Specificity ratio calculated
- [ ] Flow analysis complete
- [ ] All 5 objections audited
- [ ] Priority fix list created (critical / important / minor)
- [ ] "What is working" documented
- [ ] Overall grade and expected CVR impact estimated

## Handoff
- → write-headlines.md (if headline is critical fix)
- → build-proof-stack.md (if proof is critical fix)
- → craft-guarantee.md (if guarantee is critical fix)
- → create-split-test-plan.md (to test recommended fixes systematically)

---
*Task: DRM_AUDIT_001 | Agent: drm-chief | Version: 1.0*
