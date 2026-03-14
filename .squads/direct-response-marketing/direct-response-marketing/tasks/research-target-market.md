# Task: Research Target Market

**Agent:** eugene-schwartz
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Conduct deep market research before writing any copy. Eugene Schwartz's principle:
"The copywriter's job is not to create desire — it's to channel desire that already exists."
You cannot channel what you don't understand.

## Prerequisites
- Product/service to be marketed defined
- Target audience broadly identified

## Inputs Required
- Product or service category
- Known target audience (broad description is fine)
- Specific research question or copy challenge
- Access to research tools (Amazon, Reddit, forums, YouTube)

## Research Source Hierarchy

```
TIER 1 — Highest quality (use first):
├── Amazon reviews (1-star and 5-star — both reveal truth)
├── Reddit threads (r/[niche] — raw, unfiltered conversation)
├── Customer support tickets / FAQ archives
└── Your own customer interviews / survey responses

TIER 2 — High quality:
├── YouTube comments on relevant videos
├── Quora threads on the specific problem
├── Forum posts (niche-specific forums)
└── Facebook group discussions

TIER 3 — Supporting data:
├── Google search autocomplete (reveals exact questions)
├── Answer The Public
├── SEMrush / Ahrefs keyword data
└── Competitor reviews on G2, Trustpilot, Yelp
```

## Execution Steps

### Step 1: Amazon Review Mining

**For physical products:** Search Amazon for your product category + top competitors.

**Review mining protocol:**
1. Filter for 1-star reviews → read the specific complaints (reveals problems NOT being solved)
2. Filter for 5-star reviews → read what they loved most (reveals the real purchase motivation)
3. Look for "but..." in 3-4 star reviews (reveals the gap between expectation and reality)
4. Extract verbatim phrases — exact words, not paraphrases

**Document in this format:**
```yaml
amazon_findings:
  source: "Amazon — [Product Category]"
  1_star_themes:
    - quote: "[exact quote]"
      theme: "[category: expectations, quality, results, etc.]"
  5_star_themes:
    - quote: "[exact quote]"
      theme: "[what drove the purchase or created loyalty]"
  golden_phrases:
    - "[verbatim phrase that perfectly captures a truth about the market]"
```

### Step 2: Reddit Research

**Search:** r/[niche] + relevant keywords

**Best threads to mine:**
- "I've tried everything and nothing works..." → reveals frustration and failed solutions
- "Finally found something that..." → reveals what motivates purchase
- "Does anyone else feel like..." → reveals hidden frustrations
- "Honest question about [topic]..." → reveals skepticism and objections
- "What do you wish you'd known before..." → reveals buyer's remorse data = future objections

**Document patterns:**
```yaml
reddit_findings:
  subreddits_mined: []
  recurring_frustrations: []
  recurring_desires: []
  objections_expressed: []
  solutions_mentioned_as_failed: []
  language_patterns: []  # The specific words/phrases they use
```

### Step 3: YouTube Comment Mining

Search YouTube for videos about the problem (not the solution) in your niche.

**Best video types to mine:**
- "I tried [solution] for 30 days — honest review"
- "[Problem] — my story"
- "Why [common approach] doesn't work"

**Comments to prioritize:**
- Comments with many likes (resonates with many)
- Long comments (high emotional investment)
- Comments that mention failed solutions
- Comments asking for help or expressing frustration

### Step 4: Synthesis — The Market Dossier

Compile all research into a structured dossier:

```yaml
market_dossier:
  market: "[Product/Service category]"
  research_date: "[Date]"
  sources_analyzed: [number]
  total_data_points: [number]

  # SECTION 1: THE PROBLEM
  primary_problem:
    how_they_describe_it: "[Their exact words — not marketing language]"
    emotional_intensity: "[1-10 — how much does this hurt?]"
    duration: "[How long have they been suffering with this?]"
    previous_attempts:
      - solution: "[What they tried]"
        why_failed: "[Their stated reason for failure]"

  # SECTION 2: THE DREAM OUTCOME
  dream_outcome:
    surface_desire: "[What they say they want]"
    deep_desire: "[What they really want underneath that]"
    transformation: "[How their life changes if solved]"
    specific_language: "[Verbatim phrases describing desired outcome]"

  # SECTION 3: BELIEFS AND OBJECTIONS
  current_beliefs:
    - "[What they believe about the problem category]"
    - "[What they believe about solutions in this space]"
  objections:
    - objection: "[Specific objection]"
      frequency: "[common/occasional/rare]"
      underlying_fear: "[What fear is this really about?]"

  # SECTION 4: GOLDEN PHRASES (for copy)
  golden_phrases:
    for_problem_description: []
    for_dream_outcome: []
    for_testimonials: []
    for_objection_handling: []
```

### Step 5: Awareness Stage Diagnosis
Based on research findings, diagnose the market's awareness level:

- **Stage 1 (Unaware):** They haven't named the problem yet
- **Stage 2 (Problem Aware):** They know the problem but don't know solutions exist
- **Stage 3 (Solution Aware):** They know solutions exist but haven't found the right one
- **Stage 4 (Product Aware):** They know your category but haven't committed
- **Stage 5 (Most Aware):** They know you and just need an offer

This diagnosis determines the entire copy strategy.

## Quality Standards
- Minimum 3 distinct source types mined
- Minimum 50 individual data points (reviews, comments, posts) analyzed
- Minimum 20 verbatim "golden phrases" documented
- Awareness stage diagnosed with evidence (not assumed)
- All findings attributed to source (for credibility in briefing)

## Veto Conditions
- VETO if research is based on assumptions, not actual source data
- VETO if fewer than 3 source types used
- VETO if golden phrases are paraphrased (must be verbatim)
- VETO if awareness stage is assumed without evidence from the data
- VETO if dossier does not include failed solutions (critical for positioning)

## Completion Criteria
- [ ] Amazon reviews mined (minimum 50 reviews across category)
- [ ] Reddit threads mined (minimum 3 relevant subreddits or threads)
- [ ] YouTube comments mined (minimum 3 videos)
- [ ] Additional sources as needed
- [ ] Market dossier compiled with all sections complete
- [ ] Minimum 20 golden phrases documented
- [ ] Awareness stage diagnosed with evidence cited

## Handoff
- → create-customer-avatar.md (dossier feeds avatar creation)
- → diagnose-awareness-stage.md (dossier confirms or revises diagnosis)
- → develop-unique-mechanism.md (failed solutions reveal positioning opportunity)
- → build-rmbc-brief.md (dossier is primary research input for brief)

---
*Task: DRM_RES_001 | Agent: eugene-schwartz | Version: 1.0*
