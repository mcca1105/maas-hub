# Task: Map Market Sophistication

**Agent:** eugene-schwartz
**Tier:** 1
**Type:** Analysis
**Elicit:** false

## Purpose
Diagnose the exact stage of market sophistication using Eugene Schwartz's 5-stage framework.
This diagnosis determines the entire copy strategy — getting this wrong means your copy
will either bore an advanced market or overwhelm a naive one.

## Eugene Schwartz's 5 Stages of Market Sophistication

The market grows MORE sophisticated over time as more claims are made:

```
Stage 1: UNAWARE
The product exists but no one knows about it yet.
The market hasn't been exposed to claims in this category.
Strategy: Make the claim boldly. "You can [result]."
Example: First weight loss pill — "Lose weight!"

Stage 2: AWARE (Early market)
The claim has been made. Prospects know the solution exists.
Strategy: Bigger promise. "Lose TWICE as much weight."
Example: Weight loss category getting competitive.

Stage 3: SATURATED (Mechanism stage)
Every claim has been made. Big promises no longer move the needle.
Strategy: Introduce a new mechanism. "Lose weight with [NEW METHOD]."
Example: Low-carb, intermittent fasting, keto — new mechanisms break through.

Stage 4: ADVANCED (Mechanism comparison)
Multiple mechanisms compete. Prospects have tried mechanisms.
Strategy: Make your mechanism the best, easiest, most proven.
Example: "Keto — but FASTER and without counting macros."

Stage 5: MOST SOPHISTICATED (Tribal/brand)
Market has been through everything. Deep skepticism.
Strategy: Direct identification, community, brand personality.
Example: "For women who've tried everything else."
```

## Execution Steps

### Step 1: Gather Evidence Indicators

For each indicator, document what you find in the market:

```yaml
sophistication_evidence:
  # INDICATOR 1: Dominant claim type in competitor ads
  competitor_claims:
    primary_claim_type: "[pure benefit / mechanism-led / brand/community]"
    examples:
      - "[Quote from competitor ad — what type of claim?]"
      - "[Another example]"

  # INDICATOR 2: Market history
  category_age:
    years_in_market: "[Approximately how long has this category existed?]"
    major_claim_waves:
      - "[First wave of claims — what was promised?]"
      - "[Second wave — what new mechanism emerged?]"
      - "[Current wave — what are people saying now?]"

  # INDICATOR 3: Consumer language (from VOC research)
  consumer_sophistication_signals:
    phrases_showing_experience:
      - "[e.g., 'I've tried everything' = high sophistication]"
      - "[e.g., 'I've done keto, paleo, and now...' = Stage 4-5]"
    phrases_showing_naivety:
      - "[e.g., 'I had no idea this was possible' = Stage 1-2]"

  # INDICATOR 4: Proof requirements
  proof_intensity_observed:
    what_works_in_the_market: "[Data? Testimonials? Celebrity? Case studies?]"
    what_no_longer_works: "[Generic 'as seen on TV'? Single testimonial?]"

  # INDICATOR 5: Price sensitivity
  price_range_accepted: "[What are people paying? High prices = sophisticated?]"
```

### Step 2: Stage Diagnosis

Using the evidence, diagnose the stage:

```yaml
stage_diagnosis:
  stage: "[1 / 2 / 3 / 4 / 5]"
  confidence: "[high / medium / low]"
  primary_evidence:
    - "[Most compelling piece of evidence for this diagnosis]"
    - "[Supporting evidence]"
  counter_evidence:
    - "[Any evidence that might suggest a different stage?]"
  final_reasoning: "[2-3 sentence explanation of the diagnosis]"
```

### Step 3: Strategy Recommendation

Based on diagnosed stage, define the copy strategy:

```yaml
copy_strategy:
  stage: "[Confirmed stage]"

  # STAGE 1 → Benefit-first, bold claims
  # STAGE 2 → Amplified benefit, competitive promise
  # STAGE 3 → Mechanism-first, "why everything else fails"
  # STAGE 4 → Mechanism differentiation, "better than other mechanisms"
  # STAGE 5 → Identity, community, brand, direct offer

  headline_approach: "[What type of headline works for this stage?]"
  lead_approach: "[How should copy open?]"
  proof_requirements: "[What proof does this stage demand?]"

  what_to_avoid:
    - "[The approach that works for a LOWER stage — will bore this audience]"
    - "[The approach that works for a HIGHER stage — will confuse this audience]"

  claim_limitations:
    saturated_claims_to_avoid:
      - "[Claim that no longer differentiates]"
    claims_that_still_work:
      - "[Claim that's still believable and differentiating]"
```

### Step 4: The "Claim History" Map

Document the progression of claims in this market over time:

```yaml
claim_history:
  wave_1_original_claims:
    era: "[Decade/year]"
    example_claims:
      - "[What the first ads promised]"
    why_worked: "[Market hadn't heard this before]"

  wave_2:
    era: "[When competitors entered]"
    example_claims:
      - "[Amplified version of original claims]"
    why_worked: "Bigger promise beat original"

  wave_3_current:
    era: "Now"
    dominant_claims:
      - "[What everyone is saying today]"
    problem: "[Why these claims are now ineffective / skepticism level]"

  wave_4_opportunity:
    the_unclaimed_space: "[What has NOT been said that is true and powerful?]"
    mechanism_opportunity: "[What new mechanism could break through?]"
```

## Quality Standards
- Diagnosis is based on evidence (not assumed from category age alone)
- Both confirming and counter evidence documented
- Stage diagnosis includes reasoning (not just the number)
- Copy strategy is specific to the diagnosed stage
- Claim history reveals the progression logic

## Veto Conditions
- VETO if diagnosis is based solely on "this seems like a mature market" (not evidence)
- VETO if counter evidence is ignored
- VETO if copy strategy is generic (not calibrated to the specific stage)
- VETO if claim history skips the evolution logic
- VETO if mechanism opportunity is not identified for Stage 3+ markets

## Completion Criteria
- [ ] All 5 evidence indicators documented
- [ ] Stage diagnosis made with confidence level
- [ ] Primary and counter evidence both documented
- [ ] Copy strategy defined (approach, what to avoid, claim limitations)
- [ ] Claim history mapped with progression logic
- [ ] Mechanism opportunity identified (for Stage 3+ markets)

## Handoff
- → develop-unique-mechanism.md (Stage 3+ markets require mechanism)
- → write-headlines.md (stage determines headline approach)
- → build-rmbc-brief.md (stage is critical input to the brief)
- → diagnose-awareness-stage.md (cross-reference — different but related frameworks)

---
*Task: DRM_SOPH_001 | Agent: eugene-schwartz | Version: 1.0*
