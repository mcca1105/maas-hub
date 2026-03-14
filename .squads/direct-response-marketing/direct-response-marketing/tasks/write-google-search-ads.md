# Task: Write Google Search Ads

**Agent:** ryan-deiss
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write Google Search Ad copy that captures high-intent buyers at the moment of search.
Ryan Deiss's principle: Google Search is pull media — the prospect is telling you exactly
what they want. Your only job is to prove you have it better than anyone else on the page.

## Inputs Required
- Target keywords (primary + long-tail)
- Campaign type (brand/competitive/problem-aware/solution-aware)
- Landing page destination
- Offer and key differentiator
- Geographic targeting

## Google Search Ad Structure (Responsive Search Ads — RSA)

```
┌─────────────────────────────────────────────────────────────────┐
│  Ad · www.domain.com › path1 › path2                           │
│                                                                   │
│  HEADLINE 1 | HEADLINE 2 | HEADLINE 3                           │
│  (30 chars each — Google rotates 3 from your 15 options)        │
│                                                                   │
│  Description 1 (90 chars)                                        │
│  Description 2 (90 chars)                                        │
└─────────────────────────────────────────────────────────────────┘
```

**RSA Limits:**
- Headlines: 15 options provided, Google selects/rotates best 3
- Descriptions: 4 options provided, Google selects best 2
- Headline length: 30 characters (hard limit)
- Description length: 90 characters (hard limit)
- Display path: 2 fields × 15 characters

## Execution Steps

### Step 1: Keyword Intelligence

```yaml
keyword_brief:
  primary_keyword: "[Exact match keyword — highest buyer intent]"
  keyword_intent: "[informational/navigational/commercial/transactional]"
  monthly_volume: "[Est. searches/month]"
  competition: "[low/medium/high]"
  estimated_cpc: "$[amount]"

  keyword_groups:
    branded:
      - "[Brand name keywords]"
      strategy: "Own these — protect brand searches"

    competitor:
      - "[Competitor name keywords]"
      strategy: "Intercept competitor searches"

    problem_keywords:
      - "[How to fix X / X not working / X problem]"
      strategy: "Educate and redirect to solution"

    solution_keywords:
      - "[Best X / X software / X service]"
      strategy: "Position as the answer they're looking for"

    transactional_keywords:
      - "[Buy X / X price / X near me / X for sale]"
      strategy: "Direct conversion — bottom of funnel"
```

### Step 2: Competitive Ad Analysis

Before writing, research what's on the SERP:

```yaml
competitor_ad_analysis:
  top_ads_on_serp:
    - competitor: "[Company name]"
      headline_pattern: "[What they emphasize]"
      cta_type: "[What action they ask for]"
      differentiator: "[Their key claim]"

  saturation_gaps:
    - "[What no one is saying — your opportunity]"

  differentiation_angle: "[How you win on this SERP]"
```

### Step 3: Write 15 Headlines

For Responsive Search Ads, write 15 headlines across different categories:

**Category 1 — Keyword Match (3 headlines):**
Include the target keyword for Quality Score and relevance.
```
1. "[Primary keyword | 30 chars max]"
2. "[Keyword + qualifier | 30 chars max]"
3. "[Keyword + benefit | 30 chars max]"
```

**Category 2 — Benefit/Outcome (3 headlines):**
```
4. "[Specific measurable result]"
5. "[Timeframe + result]"
6. "[Outcome without pain point]"
```

**Category 3 — Differentiator (3 headlines):**
```
7. "[What makes you different from competitors]"
8. "[Your unique mechanism or approach]"
9. "[Proof number + differentiator]"
```

**Category 4 — Social Proof (3 headlines):**
```
10. "[# customers / reviews / year in business]"
11. "[Specific result achieved by customers]"
12. "[Authority or certification]"
```

**Category 5 — CTA (3 headlines):**
```
13. "[Action + benefit — Get Free X / Start X Today]"
14. "[Urgency + CTA — Limited Spots / Ends X]"
15. "[Low-commitment CTA — See How / Learn More]"
```

**Headline Specifications:**
```yaml
headlines:
  h1: "[text | X chars]"
  h2: "[text | X chars]"
  h3: "[text | X chars]"
  h4: "[text | X chars]"
  h5: "[text | X chars]"
  h6: "[text | X chars]"
  h7: "[text | X chars]"
  h8: "[text | X chars]"
  h9: "[text | X chars]"
  h10: "[text | X chars]"
  h11: "[text | X chars]"
  h12: "[text | X chars]"
  h13: "[text | X chars]"
  h14: "[text | X chars]"
  h15: "[text | X chars]"

  pinned:
    position_1: "[H1 or H2 — keyword must appear here]"
    position_3: "[CTA headline — should be here]"
    rationale: "[Why these are pinned]"
```

### Step 4: Write 4 Descriptions

```yaml
descriptions:
  d1: |
    "[Lead with the key benefit or differentiator — 90 chars max]"
    # Best for: awareness campaigns, problem keywords

  d2: |
    "[Lead with social proof + CTA — 90 chars max]"
    # Best for: competitive keywords

  d3: |
    "[Lead with offer or guarantee + CTA — 90 chars max]"
    # Best for: transactional keywords

  d4: |
    "[Lead with urgency or special offer — 90 chars max]"
    # Best for: retargeting or promotional campaigns
```

### Step 5: Display Path and Extensions

```yaml
display_path:
  path1: "[Category/Product — 15 chars max]"
  path2: "[Qualifier/CTA — 15 chars max]"
  example: "www.site.com/Free-Trial/Start-Today"

ad_extensions:
  sitelinks:
    - title: "[Feature/page — 25 chars]"
      description: "[Benefit — 35 chars each, 2 lines]"
    - title: "[Feature/page]"
      description: "[Benefit]"
    # Add 4-6 sitelinks

  callout_extensions:
    # Short phrases — no links, no CTAs, just claims
    - "[Free Shipping]"
    - "[No Contract]"
    - "[24/7 Support]"
    - "[X-Day Trial]"
    # Add 4-8 callouts

  structured_snippets:
    header: "[Services/Features/Types — choose one]"
    values:
      - "[Value 1]"
      - "[Value 2]"
      - "[Value 3]"

  call_extension:
    phone: "[If phone calls are a conversion action]"
    hours: "[Call hours if applicable]"

  price_extension:
    # If offering tiered pricing
    items:
      - header: "[Plan name]"
        description: "[What's included]"
        price: "$[X/unit]"
```

### Step 6: Ad Group Architecture

```yaml
ad_group_structure:
  campaign: "[Campaign name]"

  ad_groups:
    - name: "[Ad Group 1 — keyword cluster]"
      match_types: "[broad match modified / phrase / exact]"
      keywords:
        - "[keyword 1]"
        - "[keyword 2]"
      headline_pins: "[Which headlines to pin for this group]"
      landing_page: "[URL — must match keyword intent]"

    - name: "[Ad Group 2 — different intent]"
      match_types: "[types]"
      keywords:
        - "[keyword 3]"
        - "[keyword 4]"
      landing_page: "[URL]"

  negative_keywords:
    - "[free — if not a lead magnet campaign]"
    - "[DIY — if selling a service]"
    - "[jobs — if not hiring]"
    - "[cheap — if premium positioning]"
```

## Quality Standards
- Every headline is under 30 characters (non-negotiable)
- Primary keyword appears in at least 3 headlines (Quality Score)
- At least 1 headline pinned per position (control distribution)
- Descriptions end with period (Google auto-adds if missing, looks better with)
- 4-6 sitelinks written with descriptions (increases CTR 10-20%)

## Veto Conditions
- VETO if any headline exceeds 30 characters
- VETO if primary keyword doesn't appear in headlines
- VETO if descriptions exceed 90 characters
- VETO if no sitelink extensions written
- VETO if all headlines are the same tone/type (need variety for RSA to optimize)

## Completion Criteria
- [ ] Keyword brief complete with intent classification
- [ ] Competitor SERP analysis done
- [ ] 15 headlines written across 5 categories
- [ ] 4 descriptions written
- [ ] Display path specified
- [ ] 4 extension types written (sitelinks, callouts, snippets, call)
- [ ] Ad group structure defined with negative keywords

## Handoff
- → write-landing-page-copy.md (landing page must match ad keyword and intent)
- → diagnose-funnel-leak.md (if CTR is high but conversions low — landing page mismatch)
- → create-split-test-plan.md (headline and description A/B testing)

---
*Task: DRM_GSEARCH_001 | Agent: ryan-deiss | Version: 1.0*
