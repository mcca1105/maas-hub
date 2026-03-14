# Task: Design Upsell Sequence

**Agent:** ryan-deiss
**Tier:** 2
**Type:** Planning
**Elicit:** true

## Purpose
Architect the complete post-purchase upsell sequence — OTOs, downsells, and thank-you page logic —
to maximize Average Order Value without damaging the buyer relationship.

## The "Ascension Ladder" Principle
Each product in the sequence solves the next problem the buyer will face.
The sequence is not about extracting maximum money — it's about serving the buyer
through their full transformation journey.

## Execution Steps

### Step 1: Map the Customer Journey Problems

```yaml
customer_journey:
  core_purchase: "[What they just bought]"
  core_problem_solved: "[Problem the core product addresses]"

  problems_in_sequence:
    problem_1:
      timing: "[What happens in first 24-48 hours of using core product?]"
      obstacle: "[What challenge do they immediately face?]"
      solution_product: "[OTO1 — solves this specific obstacle]"
      format: "[Digital / physical / coaching / etc.]"
      price_range: "[10-30% of core product price]"

    problem_2:
      timing: "[What happens after problem 1 is solved?]"
      obstacle: "[Next obstacle on the journey]"
      solution_product: "[OTO2 — if applicable]"
      price_range: "[Can be higher than OTO1 if buyer has proven commitment]"

    fallback_problem:
      if_oto1_rejected: "[What smaller need can still be served?]"
      downsell_product: "[Stripped or priced-down version of OTO1]"
      downsell_format: "[Payment plan / smaller package]"
```

### Step 2: Sequence Architecture

```yaml
sequence_design:
  step_1:
    page: "Order Confirmation / OTO1 Page"
    timing: "Immediately after purchase"
    offer: "[OTO1 product]"
    price: "$[amount]"
    reasoning: "[Why this is the logical next step immediately]"
    if_accepted: "→ OTO2 or Thank You"
    if_rejected: "→ Downsell 1"

  step_2a:
    page: "OTO2 Page (for buyers who accepted OTO1)"
    offer: "[OTO2 product]"
    price: "$[amount]"
    if_accepted: "→ Thank You"
    if_rejected: "→ Thank You (or downsell OTO2)"

  step_2b:
    page: "Downsell 1 (for buyers who rejected OTO1)"
    offer: "[Stripped OTO1 or payment plan]"
    price: "$[lower amount]"
    if_accepted: "→ Thank You"
    if_rejected: "→ Thank You"

  final:
    page: "Thank You / Member Access"
    elements:
      - "Access to all purchased products"
      - "Next steps guidance"
      - "Community invitation (if applicable)"
      - "Referral ask (after delivering value)"
```

### Step 3: Revenue Model

```yaml
revenue_projection:
  monthly_buyers: [number]
  core_product_price: "$[amount]"
  baseline_revenue: "$[monthly_buyers × core_price]"

  with_upsells:
    oto1_take_rate: "[15-35%]"
    oto1_revenue_add: "$[monthly_buyers × take_rate × price]"
    downsell_take_rate: "[20-40% of those who rejected OTO1]"
    downsell_revenue_add: "$[calculation]"
    oto2_take_rate: "[10-25% of OTO1 buyers]"
    oto2_revenue_add: "$[calculation]"
    projected_aov: "$[total revenue / monthly_buyers]"
    revenue_increase: "[% over baseline]"
```

### Step 4: Sequence Copy Brief
Brief for each OTO script:

```yaml
oto1_brief:
  for_task: "write-upsell-script.md"
  product_name: "[OTO1 name]"
  next_problem: "[Exact problem this solves — specific, not vague]"
  opening: "[How to transition from 'congratulations on your purchase' to this offer]"
  key_benefits: ["[Benefit 1]", "[Benefit 2]", "[Benefit 3]"]
  price: "$[amount]"
  guarantee: "[Terms]"
  urgency: "[Real mechanism]"

downsell_brief:
  for_task: "write-upsell-script.md (downsell section)"
  trigger: "Buyer declines OTO1"
  approach: "[Price reduction / payment plan / stripped version]"
  copy_tone: "Non-pressuring — just checking if investment was the barrier"
```

## Quality Standards
- Each OTO addresses the specific "next problem" on the journey (not random upsell)
- Sequence has a maximum of 3 steps before thank you page (more = abandonment)
- Revenue model calculated before launching (no guessing)
- Downsell exists for every OTO (catching "maybe" buyers)
- Thank you page optimized (not just access links)

## Veto Conditions
- VETO if OTO product is unrelated to the problem the core product solves
- VETO if sequence has more than 3 steps (buyer fatigue = lower all conversion rates)
- VETO if no downsell is planned
- VETO if OTO price creates "price shock" given the core purchase amount
- VETO if revenue model is not calculated before implementation

## Completion Criteria
- [ ] Customer journey problems mapped
- [ ] Full sequence architecture defined
- [ ] Revenue model calculated
- [ ] Copy brief created for each OTO
- [ ] Downsell path confirmed for each OTO
- [ ] Thank you page elements defined

## Handoff
- → write-upsell-script.md (to write scripts for each OTO)
- → write-order-bump-copy.md (bump is first element in sequence)
- → create-follow-up-sequence.md (post-purchase email follows the sequence)

---
*Task: DRM_UPS_001 | Agent: ryan-deiss | Version: 1.0*
