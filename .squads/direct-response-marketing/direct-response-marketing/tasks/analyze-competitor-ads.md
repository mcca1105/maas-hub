# Task: Analyze Competitor Ads

**Agent:** ryan-deiss
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Map the competitive advertising landscape to identify what's working, what's saturated,
and where the open territory lies. Ryan Deiss's principle: knowing what your competitors
are saying is as important as knowing what to say — you must differentiate or die.

## Prerequisites
- Market category defined
- List of top 5-10 competitors (direct and indirect)
- Access to ad intelligence tools

## Research Tools

```yaml
tools_by_priority:
  facebook_google:
    - "Meta Ad Library (free) — facebook.com/ads/library"
    - "Google Ads Transparency Center (free)"
    - "AdSpy (paid) — most comprehensive FB ad database"
    - "BigSpy (paid/freemium) — multi-platform"
  display_native:
    - "SimilarWeb — traffic sources"
    - "SpyFu — Google search ads"
    - "SEMrush — paid search intelligence"
  research:
    - "MagicBrief — creative swipe file"
    - "Moat (by Oracle) — display ad archive"
```

## Execution Steps

### Step 1: Build Competitor Inventory
List top competitors with initial classification:

```yaml
competitors:
  direct_competitors:
    - name: "[Competitor 1]"
      url: "[website]"
      estimated_monthly_ad_spend: "[low/medium/high — based on ad volume]"
      primary_platforms: "[Facebook, Google, YouTube, etc.]"

  indirect_competitors:
    - name: "[Alternative solution 1]"
      url: "[website]"
      why_indirect: "[They solve same problem differently]"
```

### Step 2: Facebook/Instagram Ad Intelligence

For each competitor, check Meta Ad Library:
1. Search their page name or domain
2. Record all ACTIVE ads (running = converting)
3. Note: how long has each ad been running? (Longer = more profitable)

For each active ad, document:

```yaml
competitor_ad_analysis:
  competitor: "[Name]"
  ad_id: "[From library]"
  estimated_runtime: "[Days/weeks/months]"
  format: "[Image/video/carousel]"
  hook:
    first_line: "[Exact first line of copy]"
    hook_type: "[curiosity/problem/proof/contrarian/story]"
  primary_text_summary: "[What angle does the copy take?]"
  headline: "[Ad headline]"
  cta_button: "[Learn More / Shop Now / etc.]"
  offer_visible: "[Free trial / lead magnet / direct sale / etc.]"
  visual_description: "[What does the image/video show?]"
  sophistication_level: "[1-5 — matches Eugene Schwartz stages]"
```

### Step 3: Google Search Ad Intelligence

Search the top 5-10 keywords in your category. Document:
- Headlines used across competitors
- Value propositions claimed
- What USPs appear in ad copy
- Price mentions or offers visible

### Step 4: Longevity Analysis

**The Longevity Principle:** An ad running for 3+ months is making money.
An ad pulled after 2 weeks failed.

For each competitor's ad:
- **Running 1-2 weeks:** Testing phase, don't draw conclusions
- **Running 1-3 months:** Likely profitable, note what makes it work
- **Running 3+ months:** Highly profitable control, analyze deeply

### Step 5: Pattern Recognition — The Competitive Map

Compile findings into a competitive landscape analysis:

```yaml
competitive_map:
  # ANGLE SATURATION ANALYSIS
  dominant_angles:
    - angle: "[Angle that 3+ competitors are using]"
      saturation_level: "[high/extreme]"
      verdict: "AVOID — market is tired of this"

  underused_angles:
    - angle: "[Angle only 0-1 competitors use]"
      opportunity: "[Why this could work]"
      verdict: "OPPORTUNITY — test this"

  # CLAIM SATURATION
  overused_claims:
    - claim: "[Promise every competitor makes]"
      verdict: "Cannot differentiate on this alone"

  unique_claims_available:
    - claim: "[True claim no one else is making]"
      requires: "[What proof/mechanism would support this]"

  # OFFER PATTERNS
  dominant_offer_types:
    - "[Free trial / lead magnet / direct sale / etc. — most common]"

  untested_offer_opportunities:
    - "[Offer type not seen in the category]"

  # SOPHISTICATION LEVEL
  market_sophistication_evidence:
    average_stage: "[Stage 1-5 based on what's working]"
    evidence: "[What in the ads proves this stage?]"
    implication: "[What copy strategy does this require?]"
```

### Step 6: Differentiation Report

Based on competitive analysis, define the open territory:

```yaml
differentiation_opportunities:
  positioning:
    avoid: "[The space everyone else occupies]"
    own: "[The empty space you can credibly claim]"

  messaging:
    saturated_phrases: ["[Phrase every competitor uses]"]
    fresh_angles: ["[Phrase/angle no one is using]"]

  offer:
    category_standard: "[What everyone offers]"
    differentiated_option: "[What you could offer differently]"

  audience_subsegment:
    over_served: "[Avatar type everyone is targeting]"
    under_served: "[Avatar type being ignored]"

strategic_recommendation: |
  [2-3 sentence summary: Given the competitive landscape,
  the biggest opportunity is [X]. The angle to test first is [Y].
  The claim to lead with is [Z].]
```

## Quality Standards
- Minimum 5 competitors analyzed (mix of direct and indirect)
- Minimum 20 individual ads cataloged
- Longevity data noted for each ad where possible
- Both saturated AND underused angles documented
- Strategic recommendation is specific and actionable (not just "be different")

## Veto Conditions
- VETO if fewer than 3 competitors analyzed
- VETO if analysis only looks at what exists (must identify gaps too)
- VETO if longevity is ignored (running ≠ converting without time data)
- VETO if strategic recommendation is generic ("use storytelling")
- VETO if awareness stage is not diagnosed from competitive evidence

## Completion Criteria
- [ ] Competitor inventory built (direct + indirect)
- [ ] Minimum 20 ads documented across 5+ competitors
- [ ] Longevity analysis completed
- [ ] Competitive map compiled (saturated angles, gaps, claims)
- [ ] Differentiation report with specific strategic recommendation
- [ ] Awareness stage diagnosed from competitive evidence

## Handoff
- → map-market-sophistication.md (confirm awareness stage)
- → develop-unique-mechanism.md (gaps identified here drive mechanism creation)
- → write-facebook-ad-copy.md (differentiation strategy informs ad angles)
- → write-headlines.md (competitor headlines show what to differentiate from)

---
*Task: DRM_COMP_001 | Agent: ryan-deiss | Version: 1.0*
