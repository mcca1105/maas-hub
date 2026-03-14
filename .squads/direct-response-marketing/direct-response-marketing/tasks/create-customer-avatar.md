# Task: Create Customer Avatar

**Agent:** ryan-deiss
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Build a single, ultra-specific customer avatar that directs all copy decisions.
Ryan Deiss's principle: you cannot write to "everyone" — you write to ONE person.
When copy speaks to everyone, it speaks to no one.

## Prerequisites
- Market research complete (research-target-market.md)
- Voice of customer data collected

## The Avatar Is ONE Person
Not a segment. Not a demographic. One specific human being with a name, a life situation,
fears that keep them awake at 3am, and a dream they haven't told anyone about.

## Execution Steps

### Step 1: Demographics — Be Specific

```yaml
demographics:
  name: "[Give them a name — makes them real]"
  age: "[Specific number, not range]"
  gender: "[If relevant to the product]"
  location: "[City/region — specific]"
  relationship_status: "[Single / Married / etc.]"
  children: "[Yes/No — ages if yes]"
  occupation: "[Specific job title]"
  income: "[Specific range — $XX,000-$XX,000/year]"
  education: "[Highest level]"
  living_situation: "[Owns home / rents / etc.]"
```

### Step 2: Psychographics — The Inner Life

```yaml
psychographics:
  # Their daily life
  typical_day: "[Walk through their day — morning to night]"
  biggest_time_constraints: "[What eats their time?]"
  information_sources: "[Where do they get their information? Podcasts, YouTube, Facebook?]"

  # Their fears
  primary_fear: "[The fear they think about most related to the problem]"
  secret_fear: "[The fear they wouldn't admit out loud]"
  fear_at_3am: "[What wakes them up or keeps them awake?]"

  # Their desires
  surface_desire: "[What they say they want]"
  deep_desire: "[What they actually want underneath that]"
  identity_desire: "[Who do they want to BECOME?]"

  # Their frustrations
  biggest_frustration_with_current_situation: "[Specific]"
  what_they_have_tried_and_failed: "[List, with why it failed from their perspective]"
  what_they_blame_for_failure: "[Themselves? The solution? The market? Timing?]"

  # Their beliefs
  what_they_believe_about_the_problem: "[Their current mental model]"
  what_they_believe_about_solutions: "[Skeptical? Open? Desperate?]"
  biggest_objection_to_your_solution: "[Why they might say no]"
```

### Step 3: Purchase Psychology

```yaml
purchase_psychology:
  # What makes them buy
  buying_triggers:
    - "[Specific event or emotion that triggers purchase mode]"
    - "[What would make them buy TODAY?]"

  # What makes them hesitate
  buying_obstacles:
    price: "[Is price a genuine concern or cover story?]"
    time: "[Is time genuinely limited or excuse?]"
    skepticism: "[Specific doubt about this type of solution]"
    spouse_partner: "[Do they need to consult someone?]"
    past_failure: "[Did a similar product fail them?]"

  # Decision-making style
  decision_style: "[Analytical/Emotional/Social/Cautious]"
  who_they_trust: "[Peers? Experts? Data? Personal experience?]"
  what_proof_they_need: "[Data? Testimonials? Track record? Trial?]"

  # What they say to rationalize the purchase
  rational_justification: "[The story they'll tell themselves/spouse to justify buying]"
```

### Step 4: Their Language

This section is the most valuable for copywriters:

```yaml
their_language:
  # How they describe the problem
  problem_phrases:
    - "[Exact phrase they use — verbatim from research]"
    - "[Another phrase]"

  # How they describe the dream outcome
  desire_phrases:
    - "[Exact phrase they use to describe what they want]"
    - "[Another phrase]"

  # Words they use that you should use in copy
  vocabulary_to_use:
    - "[Word/phrase common in their world]"

  # Words that feel wrong / too technical / off-brand for them
  vocabulary_to_avoid:
    - "[Word that sounds too salesy, too technical, or too formal for them]"

  # The question they are silently asking when reading copy
  the_question_in_their_mind: "[What are they thinking as they read your copy?]"
```

### Step 5: The Avatar Card (1-Page Summary)

Compile everything into a 1-page "Avatar Card" that any copywriter on the team can use:

```
┌─────────────────────────────────────────────────────────────┐
│  AVATAR: [Name], [Age]                                      │
│  [Occupation] | [Location] | [Income range]                 │
├─────────────────────────────────────────────────────────────┤
│  PRIMARY PROBLEM:                                           │
│  [One sentence — their exact words]                         │
├─────────────────────────────────────────────────────────────┤
│  DREAM OUTCOME:                                             │
│  [One sentence — what life looks like solved]               │
├─────────────────────────────────────────────────────────────┤
│  HAS TRIED AND FAILED:                                      │
│  • [Solution 1] — failed because [reason]                   │
│  • [Solution 2] — failed because [reason]                   │
├─────────────────────────────────────────────────────────────┤
│  BIGGEST OBJECTION:                                         │
│  "[Their exact words expressing hesitation]"                │
├─────────────────────────────────────────────────────────────┤
│  BUYING TRIGGER:                                            │
│  [What finally pushes them to buy]                          │
├─────────────────────────────────────────────────────────────┤
│  GOLDEN PHRASES (use these in copy):                        │
│  • "[Verbatim phrase from their language]"                  │
│  • "[Another verbatim phrase]"                              │
│  • "[Another verbatim phrase]"                              │
└─────────────────────────────────────────────────────────────┘
```

### Step 6: Avatar Validation Test
Answer these questions — if you can't, the avatar is not specific enough:

1. What is this person doing at 7am on a Tuesday?
2. What podcast are they listening to on their commute?
3. What do they say when their spouse asks "why did you buy that?"
4. What product did they buy 3 months ago that didn't work?
5. What would make them close a browser tab within 5 seconds?

If you can answer all 5 with specificity, the avatar is ready.

## Quality Standards
- Avatar is ONE person with a name (not a segment or demographic)
- Golden phrases section contains verbatim research findings (not invented)
- Avatar card fits on 1 page and can be used as a briefing document
- Buying obstacles include what's real (not just the stated excuse)
- Validation test passes (all 5 questions answerable)

## Veto Conditions
- VETO if avatar is described as "women aged 35-55" (demographic, not avatar)
- VETO if golden phrases are paraphrased (must be verbatim from research)
- VETO if the avatar has no name
- VETO if objections are generic ("price" without specificity)
- VETO if avatar doesn't have documented failed solutions

## Completion Criteria
- [ ] Demographics section complete (specific, not ranges)
- [ ] Psychographics section complete (inner life documented)
- [ ] Purchase psychology documented
- [ ] Language section complete with verbatim phrases
- [ ] 1-page Avatar Card compiled
- [ ] Validation test passed (all 5 questions answerable)

## Handoff
- → build-rmbc-brief.md (avatar is primary input)
- → write-vsl-script.md (avatar determines hook, language, proof)
- → write-facebook-ad-copy.md (avatar determines targeting + messaging)
- → write-email-sequence.md (avatar determines tone and content)

---
*Task: DRM_AVT_001 | Agent: ryan-deiss | Version: 1.0*
