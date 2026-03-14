# Task: Write Order Bump Copy

**Agent:** ryan-deiss
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Create the copy for an order bump — the checkbox offer that appears on the checkout page
to increase Average Order Value. The order bump must feel like an obvious "yes" given
what the buyer just decided to purchase.

## Prerequisites
- Core product clearly defined
- Buyer's "next problem" identified (what will they face immediately after using the core product?)
- Order bump product selected (must be complementary and priced at 10-30% of core)

## The Order Bump Logic

The order bump works because the buyer is already in "yes" mode.
The only question is: does this bump feel like a logical addition?

**The "Next Problem" Framework:**
When someone buys Product A, they immediately face the next obstacle on the path.
The order bump solves THAT obstacle.

Example:
- Buys: "Email Marketing Course" → Next problem: "I don't know what to write"
- Order bump: "Done-For-You Email Swipe File — 47 Proven Emails to Model"

Example:
- Buys: "Keto Diet Plan" → Next problem: "I don't know what to eat when traveling"
- Order bump: "The Keto Travel Guide — 50 Restaurant Meals and Airport Options"

## The Order Bump Box Structure

The order bump appears as a checkbox on the checkout page, inside a bordered box:

```
┌─────────────────────────────────────────────────────────────────┐
│ ☐  YES! Add [Bump Product Name] for just $[price]              │
│                                                                  │
│ [HEADLINE — what they get and why they need it NOW]             │
│                                                                  │
│ • [Bullet 1 — specific benefit]                                 │
│ • [Bullet 2 — specific benefit]                                 │
│ • [Bullet 3 — specific benefit]                                 │
│                                                                  │
│ [One-line urgency or value reinforcement]                       │
│                                                                  │
│ Normally $[anchor price]. Yours today for only $[bump price].   │
└─────────────────────────────────────────────────────────────────┘
```

## Execution Steps

### Step 1: Identify the "Next Problem"
Before writing a word, answer:
- What does the buyer do FIRST after accessing the core product?
- What will they struggle with or need next?
- What would make the core product work FASTER or EASIER?

Document:
```yaml
next_problem_analysis:
  core_product: "[What they just bought]"
  first_action_after_purchase: "[What do they do first?]"
  primary_next_obstacle: "[What will trip them up?]"
  order_bump_solution: "[How does the bump solve that specific obstacle?]"
  relationship: "[Complementary / Accelerator / Safety net]"
```

### Step 2: Validate Pricing
Order bump pricing rules:
- Sweet spot: 15-25% of core product price
- Maximum effective price: 30% of core price
- If core is under $50: bump should be $9-$19
- If core is $97-$297: bump should be $27-$67
- If core is $497+: bump should be $97-$147

Higher prices = lower take rates. Test price points systematically.

### Step 3: Write the Checkbox Headline
The checkbox text is the most-read element. It must:
- Confirm the action with enthusiasm ("YES!")
- Name the product specifically
- State the price clearly
- Imply a deal (vs. normal price)

Formula: "YES! Add [Specific Product Name] to my order for just $[price] (normally $[anchor])"

Example: "YES! Add the Email Swipe File Library to my order for just $27 (normally $97)"

### Step 4: Write the Headline Inside the Box
The headline below the checkbox. This is what sells the bump.

**Formula options:**
- "Get [Specific Result] [Timeframe] Faster with [Product Name]"
- "Solve [Specific Next Problem] Before It Slows You Down"
- "The [Logical Next Step] That Makes [Core Product] Work Even Better"

Examples:
- "Write Your First 30 Emails in the Next 2 Hours — Not 2 Weeks"
- "Never Stare at a Blank Email Screen Again"
- "The Restaurant and Travel Guide That Makes Keto Actually Sustainable"

### Step 5: Write the 3 Bullets
Each bullet = one specific benefit. Not features — benefits.

**Format:** "So you can [outcome] even if [objection/obstacle]"

Examples:
- "47 done-for-you email templates so you can start sending sequences today — even if you've never written a marketing email in your life"
- "Exact subject lines that get 35-50% open rates — just copy and customize in minutes"
- "30-day send calendar mapped out — so you always know exactly what to send and when"

### Step 6: Write the Urgency/Value Line
One line that reinforces why they should add it NOW:

Options:
- "This offer is ONLY available on this page — it won't appear again"
- "We include this with every [Tier] order for free — not available separately"
- "Normally sold separately for $97 — add it now for just $27 while you're here"

### Step 7: Final Price Presentation
Clear, simple, with anchoring:
"Normally $[X]. Add it to your order right now for just $[Y]."

Always show the anchor price. Even if the "normal price" is the regular retail, the
contrast makes $Y feel like a bargain.

## Quality Standards
- The bump solves a specific "next problem" — not a generic add-on
- Pricing is 10-30% of core product
- Three bullets are specific benefits (not features)
- Checkbox headline has anchor price vs. bump price
- Box copy reads in under 30 seconds
- The word "YES!" is in the checkbox text (commitment consistency)

## Veto Conditions
- VETO if bump is not clearly related to the core product
- VETO if bump price exceeds 30% of core product price
- VETO if bullets are features, not benefits
- VETO if no anchor price shown
- VETO if bump creates cognitive friction (makes them second-guess the core purchase)
- VETO if copy inside the box exceeds 150 words (too long for a bump)

## Completion Criteria
- [ ] "Next problem" analysis completed
- [ ] Bump pricing validated (10-30% of core)
- [ ] Checkbox headline written (YES! + Product Name + Price + Anchor)
- [ ] Box headline written (benefit-focused)
- [ ] 3 bullets written (specific outcomes, not features)
- [ ] Urgency/value line written
- [ ] Price presentation with anchoring
- [ ] Full box reads in under 30 seconds

## Handoff
- → design-upsell-sequence.md (order bump is first step of upsell sequence)
- → write-upsell-script.md (OTO1 comes after the order bump)
- → create-split-test-plan.md (test bump headlines and pricing)

---
*Task: DRM_BUMP_001 | Agent: ryan-deiss | Version: 1.0*
