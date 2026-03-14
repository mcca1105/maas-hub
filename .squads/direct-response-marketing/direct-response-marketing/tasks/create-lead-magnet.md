# Task: Create Lead Magnet

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Create a lead magnet that attracts QUALIFIED leads — not just anyone with an email address.
Frank Kern's principle: the lead magnet should deliver a "result in advance" — a real win
that makes the prospect experience what it feels like to succeed with your help.

## The Qualification Principle
A lead magnet that attracts "anyone" is worth nothing.
The goal: attract only the people who are most likely to buy the core offer.

**The qualification test:** Would someone who is NOT your ideal buyer also want this lead magnet?
If yes, the lead magnet is too broad.

## Execution Steps

### Step 1: Define the "Result in Advance"

```yaml
result_in_advance:
  core_offer: "[What you ultimately sell]"
  core_offer_result: "[The big transformation your product delivers]"
  lead_magnet_result: "[The small, fast version of that transformation — 15-25% of the full result]"
  delivery_time: "[How fast can they get this result? <30 minutes is ideal]"

  the_taste_test: |
    "After consuming this lead magnet, the prospect should feel:
    'Wow, if the FREE version does this much, what does the paid version do?'"
```

### Step 2: Format Selection

```yaml
format_options:
  checklist:
    best_for: "[Complex processes that benefit from step-by-step accountability]"
    conversion_rate: "High — perceived value vs. effort to create is excellent"
    delivery_time: "3-10 minutes to consume"

  template:
    best_for: "[Creative work where people fear the blank page]"
    conversion_rate: "Very high — immediate utility"
    delivery_time: "Fill in the blanks — 15-30 minutes"

  swipe_file:
    best_for: "[Copy, design, email, social — anything with proven examples]"
    conversion_rate: "High for marketers and creators"
    delivery_time: "Reference tool — ongoing use"

  mini_guide:
    best_for: "[Complex topics that need explanation, not just steps]"
    conversion_rate: "Medium — high-value but more commitment"
    delivery_time: "20-60 minutes to read"

  video_training:
    best_for: "[Demonstrations, tutorials, personal brand building]"
    conversion_rate: "Medium-high — deepens relationship"
    delivery_time: "15-45 minutes"

  calculator_or_quiz:
    best_for: "[Personalization — makes generic content feel specific]"
    conversion_rate: "Very high — interactive, immediate insight"
    delivery_time: "2-5 minutes"

selected_format: "[Format selected]"
rationale: "[Why this format for this audience and offer]"
```

### Step 3: Name the Lead Magnet

The name must promise a specific result.

**Formula:** "[Specific Result/Outcome] [in Timeframe] [for Specific Avatar] [Without Sacrifice]"

Examples:
- ❌ "The Marketing Guide" (generic, no promise)
- ✅ "The 7-Step Email Template That Gets 40% Open Rates — Ready in 15 Minutes" (specific, fast, result)
- ✅ "The Restaurant Keto Cheat Sheet: 50 Meals at Any Chain Restaurant Under 20 Net Carbs" (specific, immediately useful)

```yaml
lead_magnet_names:
  option_1: "[Name]"
  option_2: "[Name]"
  option_3: "[Name]"
  selected: "[Best option]"
  rationale: "[Why this name will attract the right leads]"
```

### Step 4: Content Creation

The lead magnet content must be genuinely valuable — not a teaser for the paid offer.

```yaml
content_requirements:
  must_deliver_real_value: true  # No fluff, no "stay tuned for more"
  must_be_actionable: true  # They can implement immediately
  must_not_teach_everything: true  # Deliver the "what" and basic "how" — advanced "how" is the paid offer
  must_reference_the_gap: true  # Naturally shows what more could be done with full support
```

**Content structure for a checklist (example):**
1. Overview (1 page max — what this checklist does and how to use it)
2. The checklist itself (numbered, actionable items)
3. "What's next" page (natural bridge to the core offer — not a hard sell)

**Content structure for a template:**
1. Instructions (how to use the template — 1 page)
2. The template itself (fill-in-the-blank format)
3. Example of template completed (shows what success looks like)

### Step 5: Qualification Filter Check

Before finalizing:

```yaml
qualification_filter:
  would_a_non_buyer_want_this: [yes/no]
  if_yes_how_to_filter:
    - "[Add more specificity to the topic]"
    - "[Make the name more specific to the avatar]"
    - "[Require a specific situation to benefit from this]"

  does_it_create_urgency_to_buy_core_offer: [yes/no]
  does_it_demonstrate_your_methodology: [yes/no]
  does_it_attract_people_ready_to_pay: [yes/no]
```

### Step 6: Delivery Mechanism
How does the prospect receive the lead magnet?

```yaml
delivery:
  method: "[Email autoresponder / Instant download / Access page]"
  timing: "[Immediate after opt-in]"
  format: "[PDF / Video / Spreadsheet / Web page]"
  follow_up: "[Sequence that starts after delivery — see write-email-sequence.md]"
```

## Quality Standards
- Lead magnet delivers a real, actionable result in under 30 minutes
- Name promises a specific outcome (not just describes content)
- Qualified leads only — would NOT appeal to people who can't buy the core offer
- Content is genuinely useful (passes the "would I pay for this?" test)
- Naturally demonstrates the methodology without giving away everything

## Veto Conditions
- VETO if lead magnet is just a teaser ("download this to learn more about our services")
- VETO if name is generic ("Marketing Guide," "Free Ebook")
- VETO if content could attract unqualified leads equally as qualified ones
- VETO if lead magnet has no connection to the core offer's mechanism
- VETO if delivery time for the result is more than 1 hour (reduces perceived value)

## Completion Criteria
- [ ] "Result in advance" defined (small version of core offer's transformation)
- [ ] Format selected with rationale
- [ ] 3 name options written, best selected
- [ ] Content created (genuinely valuable, not teaser)
- [ ] Qualification filter check passed
- [ ] Delivery mechanism defined
- [ ] Natural bridge to core offer included (not a hard sell)

## Handoff
- → write-squeeze-page.md (squeeze page promotes this lead magnet)
- → write-email-sequence.md (welcome sequence starts after delivery)
- → write-facebook-ad-copy.md (ads drive traffic to squeeze page)

---
*Task: DRM_LM_001 | Agent: frank-kern | Version: 1.0*
