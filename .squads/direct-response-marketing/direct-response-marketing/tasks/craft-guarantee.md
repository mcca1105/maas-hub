# Task: Craft Guarantee

**Agent:** robert-cialdini
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Write the guarantee as a copy element that removes risk and increases conversion.
Robert Cialdini's principle: a strong guarantee signals confidence in the product.
Gary Halbert's principle: "The stronger the guarantee, the more you sell and the fewer refunds you get."

## Execution Steps

### Step 1: Diagnose the Buyer's Risk Fear

```yaml
risk_diagnosis:
  primary_fear: "[What are they most afraid of losing? Money / Time / Looking foolish]"
  past_trauma: "[Have they been burned by similar promises before? Evidence from VOC research]"
  risk_threshold: "[High ticket = need stronger guarantee. Low ticket = standard guarantee works]"
  sophistication: "[More sophisticated market = needs more specific guarantee]"
```

### Step 2: Select Guarantee Type

```yaml
guarantee_types:
  satisfaction_guarantee:
    formula: "If you're not completely satisfied for ANY reason within [N] days, get a full refund."
    best_for: "Mass market, lower sophistication, trust is the primary obstacle"
    refund_risk: "Low to moderate"

  results_guarantee:
    formula: "If you do [specific action] and don't get [specific result] within [timeframe], we'll [specific action]."
    best_for: "High sophistication, results-driven markets, when proof is strong"
    refund_risk: "Low — people who qualify are rare"

  double_money_back:
    formula: "If [Product] doesn't [specific result], we'll refund 200% of your investment."
    best_for: "When track record is exceptional and you want to signal extreme confidence"
    refund_risk: "Low — bold claim pre-qualifies buyers"

  keep_it_guarantee:
    formula: "Try [Product] for [N] days. If it's not right, return it for a full refund AND keep [bonus] as our gift."
    best_for: "Digital products where "return" is not possible — the bonus compensates"
    refund_risk: "Low — generosity builds trust, most don't refund"

  pay_only_if:
    formula: "Don't pay a single cent until you've [seen results / completed module 1 / etc.]."
    best_for: "High-ticket services, coaching, where proof is the primary objection"
    refund_risk: "Low — filters highly committed buyers"

selected_type: "[Based on product, market, and risk tolerance]"
```

### Step 3: Write the Guarantee Copy

The guarantee must:
1. Have a specific name (not just "Our Guarantee")
2. Be written in confident, not defensive language
3. Make claiming it sound EASY and HONORED
4. Appear at least twice in any sales copy

**Template:**

```
THE [GUARANTEE NAME]:

[Statement of confidence in the product]

Here's what I'm offering you: Try [Product Name] for [N] full days.
[What they can do / experience / achieve in those N days]

If at the end of those [N] days you're not [specific positive state
or result], just [simple action — email us, call us, etc.] and we'll
[refund / double your money / etc.] — [friendly, non-hostile condition].

No hassle. No questions. No hard feelings.

[Reason for the guarantee — why are you offering this? Because the results
speak for themselves / because you believe in this completely / etc.]
```

**Real example:**
```
THE 60-DAY "EMPTY BOTTLE" GUARANTEE:

I'm so confident that [Product Name] will work for you that I'm giving you
60 full days to try it — that's two complete bottles.

Use it daily as directed. If you don't notice [specific result] by the
end of 60 days, just email our support team at [address] with your order
number and we'll refund every penny. Keep the bottles. Keep the [bonus].
They're yours regardless.

Why am I doing this? Because I've seen what [Product Name] does for people
like [brief avatar description], and I know it works. The risk is on me.
```

### Step 4: Position the Guarantee in Copy

The guarantee appears twice:
1. **In the offer section** — immediately after price presentation (reduces purchase risk)
2. **Near the final CTA** — as the last objection handler before the buy button

**Position 1 template:**
"Still thinking about it? Here's the thing: [Guarantee name]. [2-3 sentence guarantee summary]. You literally can't lose."

**Position 2 template:**
"Remember: [Guarantee name] means you're 100% protected. Click below with confidence."

## Quality Standards
- Guarantee has a specific name
- Language is confident and buyer-friendly (not defensive)
- Claiming is made to sound easy (not a bureaucratic process)
- Appears minimum 2 times in the full copy
- Refund terms are crystal clear (no hidden conditions)

## Veto Conditions
- VETO if guarantee is unnamed (just "Our Guarantee" or buried in terms)
- VETO if language sounds suspicious or defensive ("subject to approval," "in our discretion")
- VETO if the process to claim is complicated
- VETO if guarantee contradicts itself or has fine print that negates the headline
- VETO if guarantee appears only once in the copy

## Completion Criteria
- [ ] Buyer's risk fear diagnosed
- [ ] Guarantee type selected with rationale
- [ ] Guarantee named specifically
- [ ] Full guarantee copy written
- [ ] Position 1 (offer section) copy written
- [ ] Position 2 (near CTA) copy written
- [ ] Claiming process made clear and easy

## Handoff
- → structure-irresistible-offer.md (guarantee is part of the complete offer)
- → write-sales-letter.md or write-vsl-script.md (for positioning in full copy)
- → build-proof-stack.md (guarantee confidence should match proof strength)

---
*Task: DRM_GUAR_001 | Agent: robert-cialdini | Version: 1.0*
