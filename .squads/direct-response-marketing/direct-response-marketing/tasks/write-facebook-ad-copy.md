# Task: Write Facebook Ad Copy

**Agent:** ryan-deiss
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Create Facebook/Instagram ad copy that stops the scroll and converts cold or warm traffic.
Ryan Deiss's principle: Facebook ads are the most measurable medium in history —
the feedback loop from copy to result is now measured in hours, not months.

## Inputs Required
- Campaign objective (awareness, lead gen, direct sale, retargeting)
- Traffic temperature (cold / warm retargeting / hot email-lookalike)
- Funnel destination (squeeze page, VSL, sales page, Messenger)
- Avatar profile
- Key mechanism or angle
- Offer details if direct conversion campaign

## Facebook Ad Anatomy

```
┌─────────────────────────────────────────────────┐
│  [Page Name]                    [Follow]        │
│  Sponsored                                      │
│                                                 │
│  PRIMARY TEXT (visible lines before "See more") │
│  [Lines 1-3 are critical — the hook]           │
│  [Rest expands on click]                        │
│                                                 │
│  [IMAGE or VIDEO]                               │
│                                                 │
│  HEADLINE (bold text below image)               │
│  DESCRIPTION (smaller text)                     │
│                                                 │
│  [LEARN MORE ▼]                                │
└─────────────────────────────────────────────────┘
```

**Character limits:**
- Primary text: 125 chars visible before "see more" (no hard limit after)
- Headline: 40 characters (longer gets truncated)
- Description: 30 characters

## Execution Steps

### Step 1: Define Campaign-Specific Parameters

```yaml
campaign_brief:
  objective: "[Awareness/Traffic/Leads/Sales/Retargeting]"
  temperature: "[cold/warm/hot]"
  destination_url: "[Where they go after clicking]"
  primary_kpi: "[CPL / ROAS / CTR]"
  target_cpm_range: "[Based on audience size — narrow = high CPM]"
  budget: "[Daily/lifetime]"
```

### Step 2: Select the Hook Strategy

The first 1-2 lines determine if they stop scrolling.
Based on traffic temperature:

**Cold Traffic Hooks:**
- Problem hook: "Do you [experience specific problem]?" — immediate identification
- Curiosity hook: "Most [avatars] don't know this about [topic]..." — compels reading
- Contrarian hook: "Stop [commonly recommended action]. Here's why..." — pattern interrupt
- Story hook: "3 months ago I [relatable situation]..." — narrative engagement
- Warning hook: "WARNING: If you're [situation], read this before you [action]"

**Warm/Retargeting Hooks:**
- Direct: "You visited [page] but didn't [action]. Here's why people hesitate..."
- Specific: Reference what they saw: "Still thinking about [product]? Here's what [similar people] say..."
- New angle: "You've seen the offer. Here's the one thing I should have mentioned..."

### Step 3: Write Ad Set (3 Variations per Angle)

For each variation, produce:

**Variation 1 — Problem/Solution:**
```yaml
ad_1:
  angle: "Problem identification"
  primary_text: |
    [Hook: Direct problem statement — 1-2 lines]
    [Body: 3-5 lines expanding problem + hint at solution]
    [CTA line: What to do and why now]
  headline: "[Benefit-focused — 40 chars max]"
  description: "[Urgency or supporting claim — 30 chars]"
  cta_button: "[Learn More / Get Started / Download / etc.]"
  visual_direction: "[What image/video would stop the scroll for this hook?]"
```

**Variation 2 — Social Proof / Results:**
```yaml
ad_2:
  angle: "Social proof lead"
  primary_text: |
    [Hook: Testimonial lead or number ("47,000 people have...")]
    [Body: Expand on the result — what changed for them]
    [CTA: Join / start / get access]
  headline: "[Result-focused]"
  description: "[Qualifier or urgency]"
```

**Variation 3 — Story / Curiosity:**
```yaml
ad_3:
  angle: "Story/curiosity"
  primary_text: |
    [Hook: Open a story mid-action or pose a counterintuitive question]
    [Body: Complete the story / answer the question — hint at mechanism]
    [CTA: Find out more / get the [result]]
  headline: "[Curiosity-driven]"
  description: "[What they get when they click]"
```

### Step 4: Headlines and CTAs

Write 5 headline options to test:
1. "[Specific benefit + timeframe]"
2. "[How-to promise]"
3. "[Social proof number + result]"
4. "[Mechanism name]"
5. "[Question that the avatar is already asking]"

CTA button selection:
- **Learn More:** Best for cold traffic, educational content, skeptical markets
- **Get Started:** Best for lead gen, lower-commitment first step
- **Download:** Best for lead magnets, checklists, tools
- **Shop Now:** Only for direct e-commerce
- **Sign Up:** Best for communities, challenges, events
- **Watch More:** Best when creative is a video clip

### Step 5: Copy for Different Placements

The same ad appears in multiple placements — copy must adapt:

```yaml
placement_adaptations:
  feed:
    character_count: "125 chars visible — invest all in the hook"
    tone: "Conversational, personal"
    primary_text: "[Full version]"

  story:
    character_count: "Less is more — 3-5 seconds to read"
    tone: "Urgent, direct"
    primary_text: "[Ultra-short version: headline + CTA only]"

  reels_short_video:
    script: "[Hook in first 3 seconds, key benefit in next 5, CTA last 3]"
    text_overlay: "[Mirror the spoken words]"
```

## Quality Standards
- First 125 characters are the hook — no wasted words
- Each variation tests ONE different variable (angle, hook type, or proof)
- Headline is under 40 characters AND contains the key benefit
- Visual direction is specific (not "use a relevant image")
- CTA button selection is justified by campaign objective and traffic temperature

## Veto Conditions
- VETO if primary text opens with company name or "Hi, I'm [name]"
- VETO if headline exceeds 40 characters (gets truncated)
- VETO if all 3 variations are the same angle (only words changed)
- VETO if CTA button doesn't match the destination (e.g., "Shop Now" going to opt-in page)
- VETO if no visual direction is specified (creative team needs this)

## Completion Criteria
- [ ] Campaign brief defined
- [ ] Hook strategy selected per traffic temperature
- [ ] 3 variations written (different angles)
- [ ] 5 headline options written
- [ ] CTA button selected with rationale
- [ ] Placement adaptations noted
- [ ] Visual direction specified for each variation

## Handoff
- → write-landing-page-copy.md (ensure message match between ad and destination)
- → create-split-test-plan.md (structured A/B testing of ad variations)
- → diagnose-funnel-leak.md (if CTR is high but conversions are low — mismatch issue)

---
*Task: DRM_FB_001 | Agent: ryan-deiss | Version: 1.0*
