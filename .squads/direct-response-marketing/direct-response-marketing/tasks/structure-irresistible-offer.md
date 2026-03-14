# Task: Structure Irresistible Offer

**Agent:** gary-halbert
**Tier:** 1
**Type:** Creation
**Elicit:** true

## Purpose
Build an offer so compelling that refusing it would feel like a mistake.
Gary Halbert's principle: the offer is the copy — if the offer is weak, no amount of
brilliant writing will save it.

## The Core Principle
People don't buy products — they buy outcomes. The offer packages the outcome in
a way that makes the price feel insignificant compared to the value received.

## Execution Steps

### Step 1: Define the Dream Outcome
The offer starts with what the buyer ultimately wants — not what you sell:

```yaml
dream_outcome:
  surface_want: "[What they say they want]"
  deep_want: "[What they actually want underneath]"
  transformation: "[Before state → After state]"
  how_their_life_looks_after: "[Vivid specific description]"
  timeframe_they_want: "[How fast do they want the result?]"
```

### Step 2: Build the Core Value Stack

List every component of the offer. For each component:

```yaml
value_stack:
  core_product:
    name: "[Product name]"
    description: "[What it is and what it does]"
    if_bought_separately: "$[dollar amount]"
    perceived_value: "$[what it's truly worth to buyer]"

  bonus_1:
    name: "[Bonus name — specific, not 'Bonus 1']"
    purpose: "[Which specific obstacle does this bonus remove?]"
    if_bought_separately: "$[dollar amount]"

  bonus_2:
    name: "[Bonus name]"
    purpose: "[Specific obstacle removed]"
    if_bought_separately: "$[dollar amount]"

  # Add more bonuses...

  guarantee:
    type: "[money-back / results-based / conditional]"
    length: "[number of days]"
    value: "[What does this guarantee remove in terms of risk?]"

  total_value_stack: "$[sum of all components]"
  actual_price: "$[what they pay]"
  value_to_price_ratio: "[Xd:1 — should be minimum 10:1 perceived]"
```

### Step 3: Bonus Strategy

Bonuses must earn their place. The "no-brainer bonus" rule:

**A good bonus:**
- Removes a specific obstacle to using the core product
- Would be worth buying even without the core product
- Is logical given the context of the purchase

**A bad bonus:**
- Is thrown in to inflate perceived value without real utility
- Has no connection to the core use case
- Makes the buyer suspicious of the real price

**3 Types of Strategic Bonuses:**
1. **Accelerator:** Makes the core result come faster
2. **Complementary:** Solves the "next problem" after the core product works
3. **Safety net:** Protects against the most common failure mode

### Step 4: Guarantee Engineering

The guarantee is part of the offer, not fine print.

```yaml
guarantee_options:
  money_back:
    template: "[N]-Day Money-Back Guarantee — Try [Product] for [N] full days.
                If you're not [specific outcome], just email us and we'll refund
                every penny. No questions asked."
    best_for: "[Digital products, information products, low-risk purchases]"

  results_based:
    template: "If you don't [specific measurable result] within [timeframe],
                we'll [specific action — refund AND let you keep it, work with you
                until you get it, etc.]"
    best_for: "[Coaching, services, high-ticket products]"

  double_money_back:
    template: "If [Product] doesn't [specific result], we'll refund double your investment.
                That's how confident we are."
    best_for: "[When you have overwhelming proof — reserved for strong track records]"

selected_guarantee:
  type: "[Selected type]"
  reasoning: "[Why this type fits this product and market]"
  written_copy: "[Full guarantee text]"
```

### Step 5: Urgency and Scarcity

Every offer needs a reason to act now. And it must be real.

```yaml
urgency_scarcity:
  type: "[genuine_deadline / quantity_limit / bonus_expiry]"
  mechanism: "[Exactly what goes away or changes]"
  reason: "[WHY is there a limit — must be genuine]"
  deadline: "[Specific date/time]"
  copy_line: "[How this is communicated in the offer]"

  reality_check:
    is_this_real: [yes/no]
    if_no: "STOP — create a real mechanism or remove urgency entirely. Fake urgency destroys trust."
```

### Step 6: The "No-Brainer Test"

Before finalizing the offer, run this test:

**Question 1:** If someone showed you this offer and you were the target avatar, would you feel stupid NOT buying it?

**Question 2:** Does the total perceived value feel at least 10x the price?

**Question 3:** Is the guarantee strong enough to remove the fear of being wrong?

**Question 4:** Is the urgency/deadline real enough to compel action today?

If any answer is "no" — strengthen the weak element before writing a single word of copy.

### Step 7: Offer Naming (MAGICO Formula)

The offer name is the first copy element. Apply:
- **M**ecanismo único (what makes it different)
- **A**lvo específico (who it's for)
- **G**rafia diferenciada (memorable element)
- **I**deia que ajuda (the benefit)
- **C**onvergência temporal (the timeframe)
- **O**bjetivo final (the result)

```
Template: "O [Mecanismo] de [Benefício] para [Avatar]: [Resultado] em [Prazo]"
```

## Quality Standards
- Value stack has minimum 5 components (core + 3 bonuses + guarantee)
- Every bonus solves a specific obstacle (not generic value-padding)
- Guarantee is named and written as copy (not fine print)
- Urgency has a real mechanism and stated reason
- Offer passes the no-brainer test (all 4 questions answered "yes")

## Veto Conditions
- VETO if value-to-price ratio is less than 5:1 (10:1 is the target)
- VETO if urgency is fake (no deadline, no mechanism, or mechanism is fabricated)
- VETO if guarantee is buried in terms and conditions
- VETO if bonuses don't address specific obstacles to using the core product
- VETO if offer has no name (unnamed offers are harder to sell and remember)

## Completion Criteria
- [ ] Dream outcome defined
- [ ] Complete value stack with perceived values
- [ ] Minimum 3 bonuses, each solving a specific obstacle
- [ ] Guarantee type selected and copy written
- [ ] Urgency/scarcity mechanism identified (and is real)
- [ ] No-brainer test passed (all 4 questions = yes)
- [ ] Offer named using MAGICO or equivalent formula

## Handoff
- → craft-guarantee.md (deep work on guarantee copy)
- → craft-price-anchoring.md (present the offer price correctly)
- → build-rmbc-brief.md (offer architecture feeds the brief)
- → write-vsl-script.md or write-sales-letter.md (offer section)

---
*Task: DRM_OFFER_001 | Agent: gary-halbert | Version: 1.0*
