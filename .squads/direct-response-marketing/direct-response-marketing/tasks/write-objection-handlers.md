# Task: Write Objection Handlers

**Agent:** robert-cialdini
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write responses to the top objections that prevent conversion — positioned naturally
within copy rather than as a separate FAQ. Robert Cialdini's commitment principle:
"Handle objections before they arise. An unvoiced objection is a lost sale."

## Execution Steps

### Step 1: Objection Inventory

Source objections from real data (not assumed):

```yaml
objection_sources:
  sales_team_data: "[Top objections heard on calls — verbatim]"
  support_tickets: "[Common pre-purchase questions]"
  voc_research: "[Objections from reviews, forums, comments]"
  competitor_reviews: "[Why people didn't buy or returned competitor products]"
  abandoned_cart_surveys: "[If email survey exists — why didn't they complete?]"
```

Top 7 objections for this product (rank by frequency):

```yaml
objection_inventory:
  1:
    objection: "[Exact phrasing in their words]"
    type: "[price/time/skepticism/wrong-person/spouse/timing/risk]"
    underlying_fear: "[What are they really afraid of?]"
    frequency: "[very common / common / occasional]"

  2:
    objection: "[Exact phrasing]"
    type: "[type]"
    underlying_fear: "[real fear]"
    frequency: "[frequency]"

  # Continue for top 7...
```

### Step 2: Handler Frameworks by Objection Type

**PRICE OBJECTIONS:**
"It's too expensive / I can't afford it"
Framework: Feel → Felt → Found + Value Reframe + Cost of Inaction

```
"If the investment feels significant, I completely understand.
Many of our most successful clients felt exactly the same way before they started.
What they found was that [result achieved] more than paid for the investment within [timeframe].

Think of it this way: [the problem] is already costing you [specific cost].
This isn't a cost — it's the end of a much bigger cost."
```

**SKEPTICISM OBJECTIONS:**
"This probably won't work for me / I've tried similar things before"
Framework: Acknowledge History → Explain Why Different → Proof from Similar Situation

```
"If you've been disappointed before, you deserve to be skeptical.
[Name specific things they've likely tried that didn't work — not naming competitors, just the category]

Here's why this is different: [The mechanism — explain WHY it addresses the root cause
that made previous attempts fail]

Here's what [Name], who was in exactly your situation [describe similar situation],
experienced: [specific testimonial]"
```

**TIME OBJECTIONS:**
"I don't have time for this"
Framework: Acknowledge → Time Investment vs. Time Saved + Minimum Viable Use

```
"The irony is that [the problem you're solving] is probably the thing stealing your time right now.

[Product] takes [specific minimum time commitment per day/week].
Most people spend [X time] and see [Y result].

If time is genuinely the constraint, here's the minimum viable approach: [specific minimum]"
```

**WRONG PERSON OBJECTIONS:**
"I'm not sure this is for someone like me"
Framework: Identify the specific "not like me" concern → Match with similar proof → Invitation

```
"If you're wondering whether this works for [their specific situation],
let me introduce you to [Name], who was [describe their specific similar situation].

[Testimonial — as close to their exact situation as possible]

The truth is, [mechanism] doesn't care about [their perceived limitation].
What it does care about is [what it requires — which they have]."
```

**TIMING OBJECTIONS:**
"Now's not the right time / I'll come back to this later"
Framework: Validate + Cost of Delay + Decision vs. Implementation

```
"I completely understand — life is busy.

But consider: [Problem] has been affecting you for [how long?].
Every [week/month] you wait is another [cost — financial, emotional, time].

You don't have to start using [product] today.
You just have to make the decision today, so you stop losing [cost of delay]."
```

**SPOUSE/PARTNER OBJECTIONS:**
"I need to talk to my spouse/partner"
Framework: Honor the Relationship + Make It Easy + Provide the Tool

```
"Absolutely — major decisions are better made together.

Here's what I suggest: show your partner this [specific page/video/section].
The key points they'll want to know: [3 bullet points covering the most common spouse concerns:
price, time commitment, and evidence it works]

If they have questions, we're happy to get on a call with both of you."
```

**RISK OBJECTIONS:**
"What if it doesn't work?"
Framework: Acknowledge Risk + Guarantee + Reverse the Risk + Shift Responsibility

```
"That's exactly why we offer [Guarantee Name].

If [Product] doesn't [specific result], [specific guarantee terms].
You're fully protected.

The only real risk here is [cost of NOT acting — what they lose by continuing to live with the problem]."
```

### Step 3: Position Handlers in Copy

```yaml
handler_positioning:
  within_copy_flow:
    - "[Handle 'this won't work for me' in the proof section]"
    - "[Handle price in the price section immediately after price reveal]"
    - "[Handle risk in the guarantee section]"

  dedicated_faq_section:
    for_objections: "[Use FAQ for timing and spouse objections — need more space]"
    format: "Question → Answer (bold Q, plain text A)"

  ps_of_letter:
    use_for: "[Final urgency + most common objection handled briefly]"
```

### Step 4: Write Final Handler Copy

For each objection, write the polished handler ready to embed in copy:

```yaml
polished_handlers:
  objection_1:
    placement: "[Where in copy]"
    copy: |
      "[Full handler text — ready to insert]"

  objection_2:
    placement: "[Where in copy]"
    copy: |
      "[Full handler text]"

  # Continue for top 5-7...
```

## Quality Standards
- Handlers sourced from real data (not assumed objections)
- Each handler uses empathy before reframe (acknowledge, don't dismiss)
- Handlers are positioned where the objection naturally arises (not all in a FAQ)
- Proof (testimonials, data) supports each handler
- Handlers are written in the buyer's language (not corporate)

## Veto Conditions
- VETO if objections are assumed (must come from real data)
- VETO if handlers dismiss the objection without acknowledging it
- VETO if all handlers are in a FAQ (some belong inline in the copy flow)
- VETO if handlers use corporate language ("We value your concerns...")
- VETO if top 5 objections are not all handled somewhere in the copy

## Completion Criteria
- [ ] Top 7 objections sourced from real data and inventoried
- [ ] Each objection typed (price/time/skepticism/etc.)
- [ ] Framework selected for each objection type
- [ ] Polished handler copy written for each
- [ ] Placement in copy confirmed for each handler
- [ ] Final review: every common objection is handled somewhere

## Handoff
- → build-rmbc-brief.md (objections and handlers feed the brief)
- → write-sales-letter.md or write-vsl-script.md (handlers embedded in copy)
- → write-email-sequence.md (objection emails in nurture sequence)

---
*Task: DRM_OBJ_001 | Agent: robert-cialdini | Version: 1.0*
