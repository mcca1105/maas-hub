# Task: Write Upsell Script (OTO)

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write the One-Time Offer (OTO) scripts for post-purchase upsells. Frank Kern's principle:
the upsell is not a second sale — it's a natural extension of the first "yes."
The buyer is already committed and wants to win. Your job is to show them how the
upsell helps them win faster.

## Prerequisites
- Core product purchased (buyer is on the thank-you/upsell page)
- Order bump defined if applicable (write-order-bump-copy.md)
- Next logical problem identified for each OTO

## OTO Sequence Architecture

A typical upsell sequence:

```
PURCHASE → Order Bump (checkout) → Thank You Page → OTO1 → OTO1 Accepted?
                                                            ├── YES → OTO2 (or Thank You)
                                                            └── NO → Downsell 1
                                                                      ├── YES → Thank You
                                                                      └── NO → Thank You
```

Maximum recommended OTOs: 2 (3 maximum — beyond that, buyer fatigue)

## The OTO Psychology

The buyer just said yes to something. They are in "buying mode."
Every sentence of the OTO script must maintain the momentum of that yes.

**NEVER start with:**
- A new sales pitch ("Hi, now let me tell you about...")
- Congratulations followed by a hard sell

**ALWAYS start with:**
- Confirmation of the great decision they just made
- Expansion of what that decision is going to do for them
- Then: "Before you access [Product], there's one more thing I need to show you..."

## Execution Steps

### Step 1: Position in Sequence
Define which OTO this script is for:

```yaml
oto_position:
  type: "OTO1 / OTO2 / Downsell"
  trigger: "After purchase of [Core Product] / After acceptance/rejection of [OTO1]"
  product_being_offered: "[Product Name]"
  price: "$[amount]"
  core_product_purchased: "[What they just bought]"
  next_problem_solved: "[What this OTO solves that the core doesn't]"
```

### Step 2: Script Structure (VSL Format, 3-7 minutes)

**SECTION 1 — CONFIRMATION (30-60 seconds)**
Celebrate the decision without being sycophantic.

Formula:
"Congratulations — you just made [decision description]. And here's what that means for you: [the outcome they're moving toward].

Before you go access [Product Name], I need to share something with you that I think is going to make this work even better."

**SECTION 2 — BRIDGE (30-60 seconds)**
Acknowledge what they have, then identify what's still missing.

Formula:
"[Core Product] is going to [specific outcome it delivers]. That's absolutely going to happen.

But there's one thing I've noticed that separates the people who get [result] quickly from the ones who take much longer. And it's [the specific gap that this OTO fills]."

**SECTION 3 — THE PROBLEM THEY'RE ABOUT TO FACE (60-90 seconds)**
Be specific about the next obstacle. They've never thought about this — make it real.

Formula:
"Once you start using [Core Product], you're going to run into [specific next challenge]. It happens to almost everyone. And when it does, most people [common mistake / frustration / plateau].

[Tell a short story about someone who faced this exact problem — either yourself or a customer. Make it relatable.]"

**SECTION 4 — THE SOLUTION (OTO Introduction) (60-90 seconds)**
Name the product and what it does. Simple, specific, connected to the problem just described.

Formula:
"That's exactly why I created [OTO Product Name]. It's [one-sentence description]. Specifically, it [key mechanism/what it does differently].

Here's what's inside: [List 3-5 key components with one-sentence benefit each]"

**SECTION 5 — PROOF (30-60 seconds)**
One testimonial or result that specifically speaks to the problem just described.

"Here's what [Name, credential] said after using this: [specific testimonial with result]"

**SECTION 6 — THE OFFER (60-90 seconds)**
Price, value, and the one-time nature of the offer.

Formula:
"Normally, [OTO Product] is available for $[regular price]. But because you just invested in [Core Product], I'm able to offer this to you right now for just $[OTO price].

But here's the thing — this offer is ONLY available right now, on this page. Once you leave, I cannot offer you this price again. [Explain why — and make it real: "this pricing structure only works at this point in the funnel"]"

**SECTION 7 — GUARANTEE**
Reassure without over-engineering.

Formula:
"And of course, this is backed by the same [X]-day guarantee as your original purchase. If you're not completely satisfied for any reason, just let us know and we'll take care of you."

**SECTION 8 — THE CTA**
Clear. Specific. Two options presented.

Formula:
"Click the button below to add [OTO Product] to your order right now for $[price].

If you decide this isn't for you right now, click [the smaller link/button below] and you'll go right to your [Core Product] access.

[This is important: never make "no" feel like failure. Just let them pass cleanly.]"

### Step 3: Downsell Version

If they click "No" on the OTO, present a downsell.

Downsell options:
- **Price reduction:** Same product, lower price ("I understand — let me see if I can do better")
- **Stripped version:** Core version of the OTO at lower price
- **Payment plan:** Break the OTO into 2-3 payments
- **Smaller product:** Different, cheaper product that solves part of the same problem

**Downsell script is shorter (90-120 seconds):**

"Wait — before you go, I want to make sure this isn't about the investment.

If [price] was the reason for stepping back, I want to see if we can work something out.

[Option A: Price cut] What if I could offer you [OTO Product] for just $[lower price] right now?

[Option B: Payment plan] What if we split this into [2-3] payments of just $[amount]?

Does that work better for you? Click YES below if so, or click NO to continue to your purchase."

### Step 4: Script Review
Check the script as a whole:
- Does Section 1 genuinely celebrate without being hollow?
- Is the problem in Section 3 specific enough to feel real?
- Is the transition from problem to solution natural?
- Is the OTO priced correctly (not shocking given core purchase)?
- Does the "no" path feel clean, not punishing?

## Quality Standards
- Script opens with CELEBRATION of the core purchase — never a new pitch
- The "next problem" is specific and feels inevitable
- Price is not revealed until after proof is presented
- "No" path is clean and non-pressuring (guilt doesn't sell, it refunds)
- Total script duration: 3-5 minutes for OTO1, 90-120 seconds for downsell
- Single CTA — not multiple options

## Veto Conditions
- VETO if script opens with company intro or product pitch before celebrating the purchase
- VETO if OTO price is more than 2x the core product price (typically)
- VETO if there is no downsell version planned
- VETO if "no" path shames or guilt-trips the buyer
- VETO if OTO product is unrelated to the core purchase
- VETO if guarantee is not mentioned

## Completion Criteria
- [ ] OTO position in sequence confirmed
- [ ] Full OTO script written (all 8 sections)
- [ ] Downsell script written
- [ ] Pricing confirmed (appropriate to core product)
- [ ] Guarantee language included
- [ ] "No" path scripted without guilt
- [ ] Script reviewed for total duration

## Handoff
- → design-upsell-sequence.md (for full sequence architecture)
- → write-order-bump-copy.md (if bump comes before this OTO)
- → create-split-test-plan.md (test OTO headlines and price points)

---
*Task: DRM_OTO_001 | Agent: frank-kern | Version: 1.0*
