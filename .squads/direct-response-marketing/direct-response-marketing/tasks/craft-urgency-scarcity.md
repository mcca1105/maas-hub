# Task: Craft Urgency & Scarcity

**Agent:** robert-cialdini
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Create urgency and scarcity mechanisms that accelerate buying decisions without manipulation.
Robert Cialdini's scarcity principle: "People want more of things they can have less of."
Gary Halbert's rule: "Real deadlines work. Fake deadlines destroy trust permanently."

## The Ethics Principle
Fake urgency is:
1. Dishonest
2. Detectable (buyers have seen it 1,000 times)
3. Trust-destroying (if they notice it's fake, everything else becomes suspect)

This task creates GENUINE urgency and scarcity. If none exists, it creates mechanisms
that MAKE it genuine before writing a word of copy.

## Execution Steps

### Step 1: Diagnose Genuine Urgency/Scarcity

```yaml
genuine_urgency_audit:
  # Check each category — is any of these TRUE for this offer?

  time_based:
    launch_pricing: "[Yes/No — price genuinely increases after X date?]"
    cohort_enrollment: "[Yes/No — specific start date for group/course?]"
    promotional_window: "[Yes/No — discount genuinely expires on X date?]"
    seasonal: "[Yes/No — product relevance tied to a season or event?]"

  quantity_based:
    limited_inventory: "[Yes/No — physical product with real stock limit?]"
    limited_capacity: "[Yes/No — service/coaching limited by your time?]"
    limited_spots: "[Yes/No — group program with genuine capacity limit?]"

  bonus_based:
    bonus_expiry: "[Yes/No — specific bonus genuinely goes away?]"
    fast_action_bonus: "[Yes/No — first X buyers get extra bonus?]"

  result: "[List all genuine urgency/scarcity mechanisms that apply]"
```

### Step 2: Create Genuine Mechanisms (If None Exist)

If no natural urgency exists, MAKE it real through business structure:

```yaml
mechanism_creation:
  option_a_cohort:
    description: "Open enrollment for 7-day window, then close and reopen quarterly"
    genuine_reason: "Group programs work better with a defined cohort who start together"
    implementation: "Actually close enrollment — set up waitlist, reopen in 90 days"

  option_b_bonus_window:
    description: "Fast-action bonus for first [N] buyers OR within first [X] hours"
    genuine_reason: "You want to reward fast decision-makers"
    implementation: "Actually limit — track number, remove bonus when threshold reached"

  option_c_price_tiers:
    description: "Launch price expires on specific date, then reverts to full price"
    genuine_reason: "You want testimonials and case studies, incentivizing early buyers"
    implementation: "Actually raise price — honor the commitment publicly"

  option_d_capacity:
    description: "Limit clients/students to a number you can actually serve well"
    genuine_reason: "Quality of service genuinely degrades beyond X clients"
    implementation: "Actually close when full — maintain the standard"

selected_mechanism: "[Which mechanism will be implemented and is genuinely real]"
implementation_plan: "[How it will actually be enforced]"
```

### Step 3: Write the Urgency/Scarcity Copy

Different formats for different contexts:

**Format A — Countdown/Deadline (for sales pages and emails):**
```
"Important: This offer expires [specific date and time with timezone].

After [date], [exactly what changes — price goes to $X / bonus is removed / doors close].

[Genuine reason]: [1-2 sentences explaining WHY this deadline is real]

[Specific benefit of acting now vs. waiting]"
```

**Format B — Limited Quantity (for products with genuine stock limit):**
```
"Only [N] [units/spots] available.

[Current availability] as of [date]. [How fast they're going — if relevant]

[What happens when they're gone — how long until restock, or if it's permanent]"
```

**Format C — Fast Action Bonus (for launch windows):**
```
"ORDER IN THE NEXT [timeframe] AND GET [BONUS NAME] INCLUDED FREE.

[Bonus description and specific value]

After [deadline / limit], this bonus is removed — but your core access remains."
```

**Format D — Email Urgency (for deadline-based sequences):**
```
Subject: "[Timeframe] left to get [specific thing]"

Body: "Just a quick note — [exactly what expires and when].

[Genuine reason why]

If this is right for you, now is the time: [LINK]

If you have questions, just reply — but don't wait if you're already sure.

[Name]"
```

### Step 4: Urgency Positioning in Copy

Urgency appears in specific locations in the copy:

```yaml
urgency_placement:
  headline_or_subheadline: "[For limited-time launches — urgency drives the whole campaign]"
  end_of_offer_section: "[After presenting value — urgency closes the deal]"
  above_cta: "[Final push before the button — 1-2 sentence reminder]"
  ps_of_letter: "[PS is urgency-optimized — summarizes the deal and deadline]"
  final_email: "[Dedicated urgency email on last day / closing hours]"

placement_for_this_offer:
  primary: "[Where urgency appears most prominently]"
  supporting: "[Secondary locations]"
```

## Quality Standards
- Urgency mechanism is genuine (will actually be enforced)
- Reason for deadline is stated (not just "limited time offer")
- Countdown or deadline is specific (not "soon" or "limited time")
- Urgency doesn't feel desperate (confident tone, not fearful)
- Mechanism can be verified if buyer investigates (price actually rises, doors actually close)

## Veto Conditions
- VETO if urgency mechanism is fake ("closing soon" with no real close date)
- VETO if deadline is not specific (day, date, time, and timezone)
- VETO if reason for urgency is not stated
- VETO if urgency tone is desperate or guilt-inducing
- VETO if implementation plan doesn't actually enforce the mechanism

## Completion Criteria
- [ ] Genuine urgency/scarcity mechanisms identified (or created with implementation plan)
- [ ] Urgency copy written in 4 formats (deadline, quantity, fast action, email)
- [ ] Reason for urgency stated and genuine
- [ ] Placement positions identified in the copy
- [ ] Implementation plan documented (who enforces it, how)

## Handoff
- → structure-irresistible-offer.md (urgency is part of offer presentation)
- → write-email-sequence.md (urgency email sequence for deadline campaigns)
- → write-sales-letter.md / write-vsl-script.md (urgency section positioning)

---
*Task: DRM_URG_001 | Agent: robert-cialdini | Version: 1.0*
