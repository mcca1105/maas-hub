# Task: Write Native Ad

**Agent:** eugene-schwartz
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write native ads (Taboola, Outbrain, MGID, Revcontent) that blend with editorial content
and redirect buyer attention toward your offer.
Eugene Schwartz's principle: "The copy must fit the context so perfectly that the
reader doesn't realize they've been sold to — until they already want to buy."

## What Native Ads Are

Native ads appear in content feeds as "recommended reading."
They look like editorial headlines, not ads.
The reader is in editorial mode — consuming content, not shopping.
The job of native copy is: interrupt this mode without triggering ad-blindness.

```
[Publisher's Article]     [Publisher's Article]     [Publisher's Article]

[Recommended for You ▼]
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  [IMAGE]     │  │  [IMAGE]     │  │  [IMAGE]     │
│              │  │              │  │              │
│ Headline     │  │ Headline     │  │ Headline     │
│ text here    │  │ text here    │  │ text here    │
│ [Source]     │  │ [Source]     │  │ [Source]     │
└──────────────┘  └──────────────┘  └──────────────┘
```

## Inputs Required
- Target avatar and awareness stage
- Offer category and mechanism
- Destination: advertorial or direct landing page
- Publisher context (news site / lifestyle / finance / health)
- Budget and primary metric (CPL or CPC)

## The Native Ad Funnel

```
Native Ad (curiosity hook)
    ↓
Advertorial (educates, builds belief, introduces mechanism)
    ↓
Landing Page / VSL (converts)
```

Native ads rarely convert to direct sale. They move warm traffic into the funnel
via the advertorial — the bridge between curiosity and conviction.

## Execution Steps

### Step 1: Audience-Context Mapping

```yaml
context_analysis:
  publisher_type: "[News / Finance / Health / Lifestyle / Tech]"
  reader_mindset: "[What are they consuming when they see this? What's their emotional state?]"
  awareness_level: "[Unaware / Problem Aware / Solution Aware]"

  reading_context_examples:
    news_reader: "Stressed, attention scattered, habit of quick scanning"
    health_reader: "Worried about a symptom, hoping for solution"
    finance_reader: "Anxious about money, looking for an edge"
    lifestyle_reader: "Bored, aspirational, receptive to new ideas"

  hook_emotion: "[Which emotion best interrupts this mindset?]"
  hook_strategy: "[What angle is most likely to stop the scroll here?]"
```

### Step 2: Select Headline Formula

Native ad headlines must sound like editorial content, not ads.

**Formula Library:**

**CURIOSITY:**
```
"The [Specific Thing] That [Surprising Claim]"
"Why [Common Belief] Is [Contradiction]"
"[Specific Number] [Avatars] Are Switching to This [Category]"
"[Expert Category] Say This Is the New [Topic]"
```

**WARNING/ALERT:**
```
"Stop [Common Action] Before Reading This"
"Warning: [Common Thing] May Be [Unexpected Problem]"
"[Authority] Issues Warning About [Category]"
```

**DISCOVERY:**
```
"Scientists Discover [Claim About Topic]"
"Doctors Finally Admit: [Contrarian Claim]"
"[Location] Man/Woman Discovers [Mechanism]"
"Little-Known [Thing] Does [Result]"
```

**STORY:**
```
"How [Relatable Person] [Achieved Result] Without [Sacrifice]"
"[Avatar Type] Reveals [Secret/Method]"
"[Relatable Person] Was [Struggling With Problem] Until [Discovery]"
```

**SOCIAL PROOF:**
```
"[Number] [Avatars] Can't Be Wrong About [Topic]"
"Why [Number] [Avatars] Are Doing [Behavior] Differently"
```

**Write 10 headline options (test at least 5):**
```yaml
headlines:
  h1:
    formula: "[Which formula]"
    text: "[Headline — 60-80 characters ideal]"
    emotion: "[Primary emotion triggered]"

  h2:
    formula: "[formula]"
    text: "[Headline]"
    emotion: "[emotion]"

  # Continue through h10...
```

### Step 3: Image Direction

Native ad images determine CTR more than headlines. Images must:
1. Fit the editorial environment (not look like an ad)
2. Create visual curiosity (make the viewer want to understand the context)
3. Relate to the headline (but not explain it — curiosity gap)

```yaml
image_concepts:
  concept_1:
    description: "[What the image shows]"
    why_it_works: "[Why this stops scroll in the publishing context]"
    curiosity_gap: "[What question does the image pose?]"
    production: "[Photo / illustration / screenshot / before-after]"

  concept_2:
    description: "[Image description]"
    why_it_works: "[Rationale]"

  concept_3:
    description: "[Image description]"
    why_it_works: "[Rationale]"

  winning_concept: "[Which concept to test first and why]"
```

**Image Rules:**
- NO red arrows or circles (ad platform flags these as too ad-like)
- NO celebrity faces without permission
- NO stock photo clichés (handshake, business meeting)
- YES to authentic-looking images
- YES to before/after if genuine
- YES to surprising or counterintuitive visuals

### Step 4: Write the Landing Destination Copy

**Option A — Direct to Advertorial:**

The advertorial is the bridge. It handles the reader at low trust (they just clicked a clickbait-style headline) and builds credibility before the sell.

```yaml
advertorial_brief:
  headline: "[Editorial-style headline — not a sales headline]"
  lead_type: "[Story / Discovery / Report / Investigation]"
  lead_length: "[50-100 words — establish credibility fast]"
  core_content_structure:
    - "[Problem validation — they're not alone]"
    - "[Why common solutions fail — builds credibility]"
    - "[Discovery of mechanism — the interesting part]"
    - "[Evidence — research, expert, case study]"
    - "[Product reveal — natural, not forced]"
    - "[Soft CTA — curiosity-driven, not sales-driven]"
  editorial_ratio: "70% educational content, 30% commercial"
  recommended_length: "[800-1200 words for health/finance, 500-800 for lifestyle]"
```

**Option B — Direct to Landing Page (warm retargeting only):**

For native retargeting to warm traffic, can send directly to landing page.
Headline should reference the specific angle of the ad they previously engaged with.

### Step 5: Platform-Specific Specs

```yaml
platform_specs:
  taboola:
    headline_limit: 70 characters
    description: Optional (60 chars on some placements)
    image_ratio: "1:1 (600x600) or 16:9 (1200x628)"
    ctr_benchmark: "0.1-0.3% average, 0.5%+ is excellent"

  outbrain:
    headline_limit: 60 characters
    description: Optional
    image_ratio: "1200x800 (3:2 ratio preferred)"
    ctr_benchmark: "0.05-0.2% average"

  mgid:
    headline_limit: 100 characters
    description: Required in some formats
    image_ratio: "300x300 or 600x450"

  revcontent:
    headline_limit: 120 characters
    description: Optional
    image_ratio: "600x400 preferred"
```

### Step 6: Testing Matrix

Native ads require volume testing — headlines and images drive dramatically different CTR.

```yaml
test_matrix:
  phase_1_creative_testing:
    headlines: "Test 5+ headlines with same image"
    images: "Test 3+ images with winning headline"
    budget: "$50-100 per variation minimum to get data"
    decision_criteria: "Kill anything with CTR < 0.1% after $50 spend"

  phase_2_funnel_testing:
    advertorial_angles: "Test 2-3 different advertorial angles"
    landing_page: "Test headline on LP matches native ad angle"
    decision_criteria: "Optimize for CPL or ROAS, not just CTR"

  tracking:
    utm_structure: "utm_source=taboola&utm_medium=native&utm_campaign=[campaign]&utm_content=[headline-id]"
    conversions: "[What is tracked as conversion — click to advertorial, opt-in, purchase]"
```

## Quality Standards
- Headlines sound like editorial content (read aloud — does it sound like journalism?)
- Image is genuinely interesting/curious (not stock-ad-looking)
- Advertorial structure maintained (editorial ratio respected)
- Platform character limits respected
- Testing matrix includes both image and headline variables

## Veto Conditions
- VETO if headline sounds like an obvious ad ("Buy now" / "Click here" / "Sale")
- VETO if image is a stock photo business cliché
- VETO if sending cold native traffic directly to sales page (needs advertorial bridge)
- VETO if fewer than 5 headline variations written (native CTR requires volume testing)
- VETO if no advertorial brief included (headlines without landing destination are incomplete)

## Completion Criteria
- [ ] Context analysis complete (publisher type + reader mindset)
- [ ] 10 headline options written across different formulas
- [ ] 3 image concepts specified
- [ ] Advertorial brief (or landing page direction) complete
- [ ] Platform specs noted for selected platform(s)
- [ ] Testing matrix defined

## Handoff
- → write-advertorial.md (full advertorial content from native ad brief)
- → write-landing-page-copy.md (if warm traffic going direct)
- → create-split-test-plan.md (volume headline/image testing plan)

---
*Task: DRM_NATIVE_001 | Agent: eugene-schwartz | Version: 1.0*
