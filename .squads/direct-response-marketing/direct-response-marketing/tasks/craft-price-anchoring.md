# Task: Craft Price Anchoring

**Agent:** robert-cialdini
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Structure the presentation of price so the actual cost feels small relative to perceived value.
Robert Cialdini's contrast principle: the brain doesn't evaluate price in absolute terms —
it compares price to the first number it sees.

## Execution Steps

### Step 1: Calculate the Real Value Stack

Before writing any price presentation, quantify each element:

```yaml
value_calculation:
  core_product:
    name: "[Product name]"
    if_bought_separately_or_comparable: "$[amount]"
    proof_of_value: "[How you justify this number — market rate, comparable products]"

  bonus_1:
    name: "[Bonus name]"
    comparable_value: "$[amount]"
    how_justified: "[Course sells for X / Template is valued at X / etc.]"

  bonus_2:
    name: "[Bonus name]"
    comparable_value: "$[amount]"

  # Continue for all bonuses...

  total_value: "$[sum of all]"
  actual_price: "$[real price]"
  ratio: "[X:1 — should be at least 5:1, target 10:1+]"
```

### Step 2: Select the Anchor Strategy

```yaml
anchor_strategies:
  value_stack_anchor:
    formula: "Total value = $[X]. Today: $[Y]."
    best_for: "Products with multiple components, bundles, courses with bonuses"
    example: "Everything included is worth $3,497. But you pay just $297 today."

  cost_comparison_anchor:
    formula: "Competitors charge $[X] for less. We offer [more] for $[Y]."
    best_for: "Markets with known competitors and pricing"
    example: "One-on-one coaching costs $500/hour. This gives you the same frameworks for $197."

  cost_of_problem_anchor:
    formula: "The problem costs you $[X/year]. The solution costs $[Y one-time]."
    best_for: "Problems with quantifiable financial, health, or time costs"
    example: "Bad sleep costs the average professional $3,000 in lost productivity. This costs $47."

  daily_cost_breakdown:
    formula: "That's just $[Y/365] per day — less than [relatable comparison]."
    best_for: "Annual products or when daily breakdown sounds trivial"
    example: "Less than $1.30 a day — less than a cup of coffee."

  previous_investment_anchor:
    formula: "You've already spent $[X] on [solutions that didn't work]. This is $[Y]."
    best_for: "Sophisticated markets where buyers have spent money before"
    example: "Most of our customers spent $2,000+ on programs that didn't work before finding us."

selected_strategy: "[Best for this product/market]"
```

### Step 3: Write the Price Presentation Copy

**The full sequence:**

```
1. DELIVER ANCHOR FIRST (never reveal price first)
2. BUILD THE VALUE STACK
3. REVEAL THE ANCHOR PRICE (the "retail" value)
4. CONTRAST WITH THE REAL PRICE
5. JUSTIFY THE DISCOUNT (WHY is it cheaper?)
6. ADD PAYMENT PLAN IF APPLICABLE
7. COST OF INACTION (what does NOT buying cost them?)

Template:
"Here's everything you get when you join [Product Name] today:

[List each component with specific value]

If you went out and found all of this on your own, you'd pay:
• [Component 1]: $[value]
• [Component 2]: $[value]
• [Bonus 1]: $[value]
• [Bonus 2]: $[value]
Total value: $[total]

But today, because [genuine reason for the discount — launch pricing /
we're testing a new model / you're a [list source] subscriber], you're
not going to pay $[total].

You're not going to pay half of that at $[half].

Today, you can get access to everything for just $[price].

[If payment plan available]: Or 3 easy payments of $[amount].

[Cost of inaction]: Consider this: [quantify the cost of NOT solving
the problem — in money, time, or pain]."
```

### Step 4: Payment Plan Logic

When to offer payment plans:
- Product price is $297+
- Target market is cash-flow sensitive
- Lower payment creates more "yes" decisions than lower total price

```yaml
payment_plan_options:
  one_payment:
    amount: "$[full price]"
    best_for: "Best value for buyer"

  installment_plan:
    payments: "[2-3 payments]"
    amount_per_payment: "$[amount]"
    total: "$[slightly more than one-payment — accounts for admin cost and payment risk]"
    note: "Typically charge 10-20% more for installments"

  which_to_offer:
    primary: "[Single payment — featured prominently]"
    secondary: "[Payment plan — presented as the accessible option]"
    sequence: "Show single payment first (anchor to full price), then offer plan"
```

### Step 5: The "Cost of Inaction" Close

After presenting the price, quantify what NOT buying costs:

```yaml
cost_of_inaction:
  financial_cost: "[$ amount lost per month/year by not solving the problem]"
  time_cost: "[Hours/months/years wasted continuing with current approach]"
  emotional_cost: "[The ongoing pain, frustration, missed experiences]"

  copy_line: |
    "Think about it this way: [Problem] is costing you approximately
    $[amount] per [period]. That's $[annual] every year.
    This solution is $[price] — a fraction of what the problem
    is already costing you. The real question is: what's the cost
    of NOT taking action today?"
```

## Quality Standards
- Anchor is established before price is revealed (never price first)
- Every component value in the stack is justifiable (not invented)
- Payment plan total is slightly higher than single payment (not same price)
- Cost of inaction is quantified (specific number, not vague "it costs you")
- Price presentation follows the anchor → value → contrast → justification sequence

## Veto Conditions
- VETO if price is revealed before establishing anchor value
- VETO if value stack contains invented values with no justification
- VETO if payment plan total equals single payment (makes the plan seem like a trap)
- VETO if "cost of inaction" section is missing from high-ticket products
- VETO if anchor is not at least 3x the actual price

## Completion Criteria
- [ ] Value stack calculated with justified per-component values
- [ ] Anchor strategy selected
- [ ] Full price presentation copy written (anchor → value → price → plan)
- [ ] Payment plan options defined (if applicable)
- [ ] Cost of inaction copy written
- [ ] Ratio confirmed: perceived value at least 5:1 vs. price

## Handoff
- → structure-irresistible-offer.md (price anchoring is part of offer architecture)
- → write-sales-letter.md or write-vsl-script.md (price section)
- → write-order-bump-copy.md (bump needs its own anchoring logic)

---
*Task: DRM_PRICE_001 | Agent: robert-cialdini | Version: 1.0*
