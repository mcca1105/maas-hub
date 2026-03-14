# Task: Write Testimonial Request

**Agent:** robert-cialdini
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Create systematic processes and copy for collecting specific, conversion-ready testimonials
from customers. Generic testimonials ("Great product! — John") are worthless.
Cialdini's principle: social proof is most powerful when it's specific, credible, and
comes from people similar to the prospect.

## Prerequisites
- Customer avatar defined (create-customer-avatar.md)
- Post-purchase sequence active (create-follow-up-sequence.md)
- Product delivered with sufficient time for results

## When to Request Testimonials

The timing determines the quality of testimonials received:

```yaml
optimal_timing:
  digital_products: "Day 14-21 after purchase (first wins achieved)"
  coaching_programs: "After first month, after completing first milestone"
  physical_products: "Day 7-14 after estimated delivery"
  SaaS_tools: "After first meaningful workflow completed (not just signup)"
  services: "Immediately after delivery while satisfaction is highest"

avoid:
  - "Immediately after purchase (no results yet)"
  - "Months later (memory fades, details lost)"
  - "After a support issue (negative recency bias)"
```

## Execution Steps

### Step 1: Design the Testimonial Collection System

A system, not a one-time ask. Three channels:

**Channel A — Email Survey (Primary)**
Automated trigger at optimal timing point.
Collects structured responses that translate directly to usable testimonials.

**Channel B — Video Testimonial Request (High Value)**
For engaged customers with strong results. Video testimonials convert 2-3x better than text.
Lower response rate but higher impact per testimonial.

**Channel C — Support/Success Conversation Mining**
Train support team to flag exceptional positive interactions.
Ask for testimonial permission in the moment of peak satisfaction.

### Step 2: Write the Email Survey Request

**Subject line options (test):**
- "Quick favor? (2 minutes)"
- "[First name], can I feature your results?"
- "A quick question about your experience"

**Email body structure:**
```
Hi [First name],

[Acknowledgment of time + brief description of why you're asking]

You've been using [Product] for [X weeks/days] now, and I'd love to
hear how it's going.

Your experience could help someone exactly like you who's on the fence
about [Product]. Real results from real people matter far more than
anything I could say.

It takes less than 2 minutes:

[LINK TO SURVEY]

I genuinely appreciate it — and if you give me permission to share your
response, I'll [small thank-you: credit, bonus, first look at X].

Thank you,
[Name]

P.S. No purchase necessary to share your experience. Honest feedback —
positive or negative — is what actually helps people decide.
```

### Step 3: Design the Testimonial Survey

The survey questions determine the quality of testimonials.
NEVER ask: "What do you think of our product?" (gets generic responses)
ALWAYS ask questions that elicit specific, story-driven answers.

**7-Question Structure:**

```
Q1: Before you [bought/joined/used] [Product], what was the main problem or
    frustration you were experiencing?
    (This becomes the "before" state in the testimonial)

Q2: What made you hesitant to try [Product]? What were you worried about?
    (This addresses future prospects' objections)

Q3: What specific results or changes have you experienced since using [Product]?
    Please be as specific as possible — numbers, timelines, comparisons.
    (This is the core of the testimonial — specificity is everything)

Q4: What surprised you most about [Product]?
    (Reveals unexpected benefits worth highlighting)

Q5: Who would you recommend [Product] to? What would you tell them?
    (Often the best testimonial language — peer-to-peer recommendation)

Q6: Is there anything you wish you'd known before starting?
    (Reveals common misconceptions to address in marketing)

Q7: May we use your response as a testimonial, with your name and [city/profession]?
    [ ] Yes, use my full name and location
    [ ] Yes, but first name and last initial only
    [ ] Yes, but keep me anonymous
    [ ] No, this is private feedback only
```

### Step 4: Write the Video Testimonial Request

For high-engagement customers with specific results:

**Email approach:**
```
Subject: [First name] — would you be willing to spend 5 minutes on camera?

Hi [First name],

I noticed [specific result they achieved / specific engagement signal].

I'd love to share your story with people who are where you were [X weeks ago].

I'm not asking for a polished production. A smartphone video in your
living room is perfect. Just answer 3 questions, 5 minutes total:

1. Where were you before [Product]? What was your main challenge?
2. What happened after you started using it?
3. Who would you recommend it to?

That's it. I'll handle the editing.

In return: [specific thank-you — discount, bonus, early access].

Interested? Just reply "yes" and I'll send the exact instructions.

[Name]
```

### Step 5: Testimonial Editing for Maximum Impact

Raw testimonials need editing to be maximally persuasive, while staying 100% truthful.

**Editing principles:**
- Extract the most specific, result-focused sentence
- Lead with the result, not the journey ("I lost 31 pounds" before the story)
- Remove qualifiers that weaken impact ("kind of," "sort of," "I think," "maybe")
- Add context if missing (with permission): full name, city, profession, timeframe
- Format for scanability: bold the key result

**Before editing:**
"I've been really happy with this, it's helped me a lot with my business and I feel
like things are going in the right direction. Would recommend."

**After editing (with permission to adjust):**
"In 60 days, our close rate went from 12% to 31%. [Product] changed how I think
about sales entirely."
— Maria Santos, Sales Director, São Paulo, SP

**Testimonial display formats:**
- Short quote (for above the fold): 1-2 sentences, bold result, name + credential
- Long testimonial (for sales pages): full story arc (before → journey → result)
- Video embed (highest converting): 60-90 seconds, autoplay off, transcript available
- Star rating + quote (for review-style sections): ★★★★★ + key sentence

### Step 6: Testimonial Organization System

```yaml
testimonial_library:
  categories:
    by_result:
      - "[Primary result type] testimonials"
      - "[Secondary result type] testimonials"
    by_avatar_similarity:
      - "[Avatar type A] testimonials"
      - "[Avatar type B] testimonials"
    by_objection_addressed:
      - "Price objection testimonials ('I was worried about the investment...')"
      - "Skepticism testimonials ('I was skeptical at first...')"
      - "Time objection testimonials ('I thought I was too busy...')"
    by_format:
      - "Video testimonials"
      - "Text testimonials"
      - "Screenshot testimonials"
      - "Case studies (long form)"

  metadata_per_testimonial:
    name: "Full name"
    credential: "Job title / Location / Relevant qualifier"
    result: "Specific result in numbers"
    timeframe: "How long to achieve result"
    permission: "What they authorized"
    date_collected: "YYYY-MM-DD"
    used_in: "Which pages/campaigns use this testimonial"
```

## Quality Standards
- Every collected testimonial has: name (at minimum first name + last initial), location or profession, specific result
- Testimonials organized by objection they address (not just generic positive sentiment)
- Video testimonials have captions (accessibility + silent viewing)
- Testimonial request timing is based on results window, not arbitrary
- Permission documented for every testimonial (GDPR/LGPD compliance)

## Veto Conditions
- VETO if testimonials are collected without permission documentation
- VETO if editing changes the meaning (only clarify, never invent)
- VETO if testimonials are anonymous without reason (reduces credibility 60%)
- VETO if survey asks generic questions ("What do you think of our product?")
- VETO if testimonial request comes before customer has had time for results

## Completion Criteria
- [ ] Testimonial collection timing defined per product
- [ ] Email survey written with 7-question structure
- [ ] Video testimonial request written for high-engagement customers
- [ ] Testimonial editing guidelines documented
- [ ] Testimonial library categories defined
- [ ] Permission tracking system specified
- [ ] Minimum 5 testimonials collected, edited, and categorized

## Handoff
- → build-proof-stack.md (testimonials feed the proof stack)
- → write-sales-letter.md or write-vsl-script.md (use testimonials in copy)
- → write-landing-page-copy.md (above-fold testimonials)

---
*Task: DRM_SOCIAL_001 | Agent: robert-cialdini | Version: 1.0*
