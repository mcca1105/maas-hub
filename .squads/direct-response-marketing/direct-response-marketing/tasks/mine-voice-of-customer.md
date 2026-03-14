# Task: Mine Voice of Customer

**Agent:** gary-halbert
**Tier:** 1
**Type:** Analysis
**Elicit:** false

## Purpose
Extract the exact language of customers — verbatim phrases that go directly into copy.
Gary Halbert's principle: "Don't write with YOUR words. Write with THEIR words."
The most persuasive copy sounds like the reader wrote it themselves.

## Prerequisites
- Sources identified (Amazon, reviews, surveys, support tickets, interviews)
- Product category or problem space defined

## The Golden Rule
Every "golden phrase" in this document must be VERBATIM.
Paraphrasing kills the power. "I was desperate and had tried everything" is powerful.
"The customer felt frustrated after multiple failed attempts" is copy-killing paraphrase.

## Execution Steps

### Step 1: Source Inventory
List all sources available before mining:

```yaml
available_sources:
  internal:
    - customer_surveys: "[date range, n=]"
    - support_tickets: "[volume and date range]"
    - interview_transcripts: "[number of interviews]"
    - nps_comments: "[n=, date range]"
  external:
    - amazon_reviews: "[product category, competitors]"
    - google_reviews: "[business names]"
    - reddit: "[subreddits]"
    - facebook_groups: "[group names]"
    - youtube_comments: "[video types]"
    - trustpilot_g2: "[companies]"
```

### Step 2: Mining Protocol by Source

**Amazon Review Mining:**
Process: 1-star reviews → 3-star reviews → 5-star reviews

For each review, capture:
- The exact emotional phrase (not the whole review)
- What category it falls into
- The star rating (1 star = what's wrong, 5 star = what drives purchase)

**Reddit Thread Mining:**
Search strings: "[niche] frustrated" | "[niche] doesn't work" | "I've tried everything [niche]" | "[niche] success story"

**YouTube Comment Mining:**
Best comment sections: Honest review videos, "I tried X for 30 days" videos, "My [niche] transformation" videos

### Step 3: Categorize by Copy Use

```yaml
voice_of_customer_library:

  # CATEGORY 1: Problem Description (use in problem section of copy)
  problem_phrases:
    - phrase: "[Exact verbatim phrase]"
      source: "[Amazon review / Reddit r/X / YouTube video]"
      emotion: "[frustration/shame/anger/desperation]"
      copy_use: "[headline / problem agitation / email subject]"

    - phrase: "[Another verbatim phrase]"
      source: "..."
      emotion: "..."
      copy_use: "..."

  # CATEGORY 2: Failed Solutions (use to position against alternatives)
  failed_solution_phrases:
    - phrase: "[Exact quote about something they tried that didn't work]"
      solution_mentioned: "[Product/approach they tried]"
      why_failed: "[Their stated reason — verbatim]"
      source: "..."

  # CATEGORY 3: Dream Outcome (use in headline, promise, CTA)
  dream_outcome_phrases:
    - phrase: "[Exact quote about what they want]"
      source: "..."
      emotion: "[hope/excitement/relief/determination]"

  # CATEGORY 4: Transformation Stories (use as testimonial models)
  transformation_phrases:
    - phrase: "[Quote describing their before/after]"
      source: "..."
      structure: "before | turning point | after"

  # CATEGORY 5: Objection Language (use to pre-handle objections)
  objection_phrases:
    - phrase: "[Exact expression of hesitation or doubt]"
      objection_type: "[price/time/skepticism/spouse/timing]"
      source: "..."

  # CATEGORY 6: Emotional Intensity (words that carry weight)
  power_words_from_market:
    - word_or_phrase: "[Term the market uses that carries emotional weight]"
      context: "[How they use it]"
      use_in_copy: "[Where this should appear]"
```

### Step 4: The Top 20 Golden Phrases

From all collected material, select the 20 most powerful, most usable phrases:

```yaml
top_20_golden_phrases:
  headline_candidates:
    1. "[Phrase that could become a headline]"
    2. "[Phrase that could become a headline]"
    3. "[Phrase that could become a headline]"

  bullet_candidates:
    4. "[Phrase that reveals a specific desire or insight]"
    5. "[Phrase that reveals a specific desire or insight]"

  testimonial_models:
    6. "[Phrase that perfectly describes a transformation]"
    7. "[Phrase that perfectly describes a transformation]"

  objection_handlers:
    8. "[Phrase expressing objection — use to anticipate in copy]"
    9. "[Phrase expressing objection]"

  problem_agitation:
    10-15: [phrases that make the problem feel real and vivid]

  dream_language:
    16-20: [phrases that capture the desired outcome in their words]
```

### Step 5: Pattern Identification

After mining, identify patterns:

```yaml
patterns:
  # What metaphors do they use?
  recurring_metaphors:
    - "[They describe the problem like 'drowning' / 'stuck in quicksand' / etc.]"

  # What emotions dominate?
  dominant_emotions:
    before_solution: "[frustration/shame/desperation/anger/hope]"
    after_solution: "[relief/pride/excitement/confidence]"

  # What words are overused by competitors (to avoid)
  saturated_language:
    - "[Word that appears in every competitor's copy and now means nothing]"

  # What language is their own (not marketers')
  authentic_market_language:
    - "[Word they use that marketers would never use but prospects immediately recognize]"
```

## Quality Standards
- Minimum 100 sources analyzed (individual reviews, comments, posts)
- Minimum 30 verbatim golden phrases documented
- Every phrase has its source documented
- Phrases are categorized by copy use
- No paraphrasing — if it's not their exact words, it doesn't belong here
- Pattern section identifies authentic language vs. saturated competitor language

## Veto Conditions
- VETO if any phrase is paraphrased (must be verbatim)
- VETO if fewer than 3 distinct source types used
- VETO if source documentation is missing for any phrase
- VETO if fewer than 20 golden phrases identified
- VETO if patterns section is skipped

## Completion Criteria
- [ ] Source inventory complete
- [ ] Minimum 100 individual data points analyzed
- [ ] All 6 phrase categories populated
- [ ] Minimum 30 golden phrases documented (all verbatim)
- [ ] Top 20 golden phrases selected and categorized by copy use
- [ ] Pattern section complete

## Handoff
- → create-customer-avatar.md (golden phrases populate the language section)
- → build-rmbc-brief.md (library is primary copywriting reference)
- → write-headlines.md (headline candidates from category 1 and 3)
- → write-fascination-bullets.md (bullet candidates from category 2 and 3)

---
*Task: DRM_VOC_001 | Agent: gary-halbert | Version: 1.0*
