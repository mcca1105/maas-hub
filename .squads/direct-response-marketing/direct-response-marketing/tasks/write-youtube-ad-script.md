# Task: Write YouTube Ad Script

**Agent:** stefan-georgi
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write YouTube ad scripts that hold attention past the skip button and drive action.
Stefan Georgi's principle: YouTube is direct response TV — you have 5 seconds to earn
the right to sell, and 60 seconds to close the deal before they lose interest.

## Inputs Required
- Campaign objective (traffic, leads, direct sale, retargeting)
- Traffic temperature (cold / warm / remarketing)
- Ad format (skippable in-stream / non-skippable 15s / bumper 6s / discovery)
- Avatar profile
- Offer summary and key mechanism
- Existing VSL or sales page (if driving to one)

## YouTube Ad Formats

```
SKIPPABLE IN-STREAM:
├── First 5 seconds: Non-skippable hook
├── Seconds 5-30: Must earn continued attention
├── Seconds 30-90: Core sell (most viewers lost here)
└── CTA before 60s for cold traffic (many won't make it to end)

NON-SKIPPABLE 15-SECOND:
└── Hook → Benefit → Single CTA only

BUMPER 6-SECOND:
└── Visual + single memorable claim only

DISCOVERY (shown in search results):
└── Thumbnail + title hook drives click, video earns view
```

## Execution Steps

### Step 1: Define Ad Parameters

```yaml
ad_brief:
  format: "[skippable/non-skippable/bumper/discovery]"
  length_target: "[15s/30s/60s/90s/120s]"
  objective: "[awareness/lead/sale/retargeting]"
  temperature: "[cold/warm/remarketing]"
  destination: "[landing page/VSL/product page/channel]"
  audience: "[avatar name and key characteristics]"
  key_claim: "[The single most compelling claim — what they get]"
  mechanism_tease: "[What makes this different — hint, not full reveal]"
```

### Step 2: Engineer the 5-Second Hook

The hook is everything. It must do one thing: make skipping feel like a mistake.

**Hook Formulas (by traffic temperature):**

**Cold Traffic — Pattern Interrupt:**
```
Option A (Problem): "[Specific relatable frustration] — if that's you, don't skip."
Option B (Contrarian): "Stop [doing commonly recommended thing]. Here's why..."
Option C (Bold Claim): "[Specific result] in [specific timeframe] — I'll show you exactly how."
Option D (Question): "What if [desired outcome] was actually simpler than you think?"
Option E (Curiosity): "Most [avatars] never find out about this because [reason]..."
```

**Warm/Retargeting — Direct Bridge:**
```
Option A: "You watched [previous video] — here's what I left out..."
Option B: "You've seen [product/offer] — here's what [X people] are saying..."
Option C: "Still thinking about [topic]? Let me settle this right now."
```

**Write 3 hook options:**
```yaml
hooks:
  hook_1:
    type: "[formula type]"
    script: "[Exact 5-second hook script]"
    visual_direction: "[What's on screen during these 5 seconds]"

  hook_2:
    type: "[formula type]"
    script: "[Exact 5-second hook script]"
    visual_direction: "[On-screen direction]"

  hook_3:
    type: "[formula type]"
    script: "[Exact 5-second hook script]"
    visual_direction: "[On-screen direction]"
```

### Step 3: Write Full Script by Format

**SKIPPABLE IN-STREAM (60-90 seconds — primary format):**

```
SECONDS 0-5: HOOK (non-skippable — earn the right to continue)
[Hook Option Selected]

SECONDS 5-15: BRIDGE (make the hook relevant to them)
"Here's what I mean..."
[Connect hook to their specific situation]

SECONDS 15-35: CORE ARGUMENT (the why and what)
"[Explain the problem or opportunity in 2-3 sentences]"
"[Introduce the mechanism — what makes this possible/different]"
"[Social proof or credibility — 1 sentence]"

SECONDS 35-55: PROOF + OFFER BRIDGE
"[Specific result story or statistic]"
"And that's exactly why I created [Product/Lead Magnet]..."
"[What they get — stated as outcome, not feature]"

SECONDS 55-75: CTA (MULTIPLE — on screen + verbal)
"Click the link below right now to [specific action]."
"[Reason why now — urgency if genuine]"
"[What happens when they click — reduce friction]"

[END CARD: 5-15 seconds with visual CTA overlay]
```

**Full 90-Second Script (final, production-ready):**

```yaml
script_90s:
  seconds_0_5:
    spoken: "[Exact hook words]"
    visual: "[What camera sees / graphic / text overlay]"
    tone: "[Energy level and delivery note]"

  seconds_5_15:
    spoken: "[Bridge script]"
    visual: "[Visual direction]"

  seconds_15_35:
    spoken: "[Core argument script]"
    visual: "[Visuals supporting claims]"

  seconds_35_55:
    spoken: "[Proof + offer bridge]"
    visual: "[Testimonial clip / results graphic / product reveal]"

  seconds_55_75:
    spoken: "[CTA script]"
    visual: "[CTA overlay / link visible on screen]"
    cta_overlay: "[Text on screen: button text and URL]"

  end_card:
    spoken: "[If speaking continues]"
    visual: "[End card with subscribe / link / offer]"
    duration: "[5-15 seconds]"
```

**NON-SKIPPABLE 15-SECOND:**

```yaml
script_15s:
  structure: "Hook (0-3s) → Core Claim (3-12s) → CTA (12-15s)"
  seconds_0_3:
    spoken: "[Immediate hook — no setup]"
    visual: "[Bold visual or text]"
  seconds_3_12:
    spoken: "[Single most compelling thing — no list, just the best one]"
    visual: "[Proof visual / demonstration / result]"
  seconds_12_15:
    spoken: "[Direct CTA — one action only]"
    visual: "[URL / button / text overlay]"
```

**BUMPER 6-SECOND:**

```yaml
script_6s:
  rule: "One idea only. Visual-led. Text overlay carries the message."
  concept: "[The single idea being planted]"
  visual: "[What happens on screen]"
  text_overlay: "[5-7 words max]"
  audio: "[Music or short spoken line — optional]"
```

### Step 4: Write Script Variations for Testing

For skippable ads, write 3 variations testing different hooks on same core:

```yaml
variations:
  variation_a:
    hook_type: "Problem/Pain"
    hook_script: "[5-second script]"
    rest_of_script: "[Same core, same CTA]"

  variation_b:
    hook_type: "Curiosity/Mechanism"
    hook_script: "[5-second script]"
    rest_of_script: "[Same core, same CTA]"

  variation_c:
    hook_type: "Social Proof / Results"
    hook_script: "[5-second script]"
    rest_of_script: "[Same core, same CTA]"
```

### Step 5: Production Notes

```yaml
production_brief:
  presenter: "[Founder/spokesperson/actor — who delivers]"
  location: "[Studio/office/outdoor — credibility signal]"
  b_roll_needed:
    - "[Shot 1: what visual supports seconds 15-35]"
    - "[Shot 2: what proof visual needed at 35-55]"
    - "[Shot 3: what CTA visual needed]"

  text_overlays:
    - timing: "[When]"
      text: "[Exact overlay text]"

  captions: "REQUIRED — 85% of YouTube watched without sound in feed"

  cta_elements:
    verbal_cta: "[What is spoken at CTA point]"
    screen_cta: "[What text appears on screen]"
    end_screen: "[What end card shows]"
    companion_banner: "[Desktop companion banner text — 300x60px]"
```

## Quality Standards
- Hook is complete in under 5 seconds with no setup required
- First 30 seconds works as a standalone 30s ad
- CTA appears at least twice (verbal + visual)
- Captions included (or direction to add in post)
- Production brief is specific enough to actually shoot the ad

## Veto Conditions
- VETO if hook requires context (if viewer must have seen prior ads to understand)
- VETO if CTA only appears at end (must appear by 60 seconds for cold traffic)
- VETO if no visual direction (production team needs guidance)
- VETO if 15s and bumper variations missing (multi-format approach required)
- VETO if captions not addressed

## Completion Criteria
- [ ] Ad parameters defined
- [ ] 3 hook options written
- [ ] Full 90-second script (production-ready with visual direction)
- [ ] 15-second version written
- [ ] 6-second bumper written
- [ ] 3 variations for split testing
- [ ] Production notes complete

## Handoff
- → write-vsl-script.md (if ad drives to VSL — ensure message match)
- → write-facebook-ad-copy.md (repurpose hooks and structure)
- → create-split-test-plan.md (structured testing of ad variations)

---
*Task: DRM_YT_001 | Agent: stefan-georgi | Version: 1.0*
