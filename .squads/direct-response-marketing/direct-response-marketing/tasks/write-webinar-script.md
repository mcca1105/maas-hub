# Task: Write Webinar Script

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write a live or auto-webinar script that delivers genuine value and transitions naturally
to the offer without feeling like a pitch fest.
Frank Kern's principle: "The best webinar doesn't feel like a webinar. It feels like
a conversation where someone accidentally gave you their best stuff for free —
and then mentioned they have more."

## Inputs Required
- Webinar format (live / evergreen auto-webinar)
- Topic and avatar profile
- Core teaching content (3-4 main lessons)
- Offer to pitch (price, what's included, guarantee)
- Awareness level of expected audience (warm list vs. cold traffic)
- Target attendance duration (60-90 min is standard)

## Webinar Architecture

```
STANDARD 90-MINUTE WEBINAR STRUCTURE:
├── Pre-Webinar (before start time)
│   ├── Holding page content
│   └── Text while waiting
│
├── INTRO (0-15 min): Why this matters + credibility
│   ├── Hook/Opening statement
│   ├── Promise (what they'll get today)
│   ├── Credibility story (personal)
│   └── Preview of content
│
├── CONTENT (15-60 min): The teaching — genuine value
│   ├── Lesson 1: [Core insight — changes their worldview]
│   ├── Lesson 2: [Mechanism or process]
│   ├── Lesson 3: [The part that makes them need what you sell]
│   └── Optional Lesson 4: [Advanced or bonus insight]
│
├── TRANSITION (60-70 min): Bridge to offer
│   ├── "Now, if you want to go even further..."
│   ├── Acknowledge what they could do on their own
│   └── Introduce the offer context
│
├── OFFER (70-85 min): The close
│   ├── Introduce product/program
│   ├── What's included (value stack)
│   ├── Bonuses (time-limited)
│   ├── Price + payment options
│   ├── Guarantee
│   └── CTA (with urgency if genuine)
│
└── Q&A (85-90 min): Address objections + remind of offer
```

## Execution Steps

### Step 1: Define Webinar Parameters

```yaml
webinar_brief:
  title: "[Compelling webinar title — the promise]"
  format: "[Live / Evergreen auto-webinar]"
  target_duration: "[60 / 75 / 90 minutes]"
  audience_temperature: "[Cold / Warm list / Hot buyers]"

  core_promise:
    headline: "[What they'll discover/learn/be able to do]"
    result: "[The transformation or capability they gain]"
    timeframe: "[When they'll apply it — in the next 90 minutes / this week]"

  teaching_framework:
    lesson_1_title: "[Core insight that shifts perspective]"
    lesson_2_title: "[The process or mechanism]"
    lesson_3_title: "[The thing that makes them want the offer]"
    lesson_4_title: "[Optional: advanced concept]"

  offer:
    name: "[Program/product name]"
    price: "$[amount]"
    value: "$[total value stack]"
    guarantee: "[Guarantee details]"
```

### Step 2: Write the Pre-Webinar Content

```yaml
pre_webinar_content:
  holding_page_text:
    countdown: "Starts in [X] minutes"
    instruction: "Get a pen and paper — you'll want to take notes"
    credibility_line: "[One sentence about host credibility]"
    social_proof: "[If live: 'X people registered' / '[City names] joining']"

  opening_loop: |
    "While we wait for everyone to arrive, drop in the chat:
    [1] Where are you watching from?
    [2] What's the one thing you most want to get from today?

    I'll be going through the chat and answering questions as we start."
```

### Step 3: Write the Intro Section (0-15 min)

```yaml
intro_section:
  opening_hook:
    # First words they hear — must immediately signal value
    type: "[Bold claim / Controversial statement / Counterintuitive question]"
    script: |
      "[Opening line that immediately communicates the core promise]

      [1-2 sentences of context — what makes this different or why now]"

  big_promise:
    script: |
      "By the end of today's training, you're going to [specific outcome].

      Not [vague promise], but [specific, tangible, credible promise].

      And here's how we're going to do that..."

  overview_of_content:
    script: |
      "Here's exactly what we're covering today:

      First, [Lesson 1 — described as a benefit, not a topic]
      Then, [Lesson 2 — benefit]
      And finally, [Lesson 3 — the one they'll be most excited about]

      But before we do — let me quickly tell you why this stuff actually works."

  credibility_story:
    # Frank Kern's approach: credibility through authenticity, not authority
    format: "[Story of your own struggle + transformation, OR specific results you've generated]"
    length: "3-5 minutes max"
    elements:
      - "Relatable starting point (not so different from them)"
      - "The specific problem you faced (identical to theirs)"
      - "What you discovered (teaser of your mechanism)"
      - "The result (specific, measurable)"
      - "Why you're sharing this today"
    script: |
      "[Write complete credibility story — 400-600 words]"
```

### Step 4: Write Each Lesson (15-60 min)

**Lesson Template (write one per lesson):**

```yaml
lesson_1:
  title: "[What they're learning]"
  duration: "10-15 minutes per lesson"
  objective: "[What they should be able to DO after this lesson]"

  opening:
    script: |
      "Okay, let's get into Lesson 1: [Title].

      [The single most important thing to understand here is...]"

  core_content:
    main_point: "[The insight or concept]"
    explanation: |
      "[Full explanation — be specific. Use analogies, examples, numbers]"

    example:
      story_or_case: "[Real example — specific person, specific result]"
      script: |
        "[Write the teaching example — 100-200 words]"

    common_mistake:
      script: |
        "Here's where most people get this wrong...
        [Specific mistake they're probably making]
        [Why this keeps them stuck]
        [What to do instead — your approach]"

  interactive_element:
    type: "[Worksheet / Poll / Chat question / Exercise]"
    script: |
      "I want you to [specific action — write down / type in chat / complete the exercise].
      [What to write/type]
      [Brief pause]"

  transition:
    script: |
      "Good. Now that you have [what they just learned], you're ready for Lesson 2..."

# Repeat structure for Lesson 2, Lesson 3, Lesson 4
```

### Step 5: Write the Transition to Offer (60-70 min)

```yaml
transition_section:
  acknowledge_the_content:
    script: |
      "Now, everything I've shown you today — [summarize the 3 lessons in 2-3 sentences] —
      you could go implement this yourself starting today.

      Seriously. Take what we covered, apply it, and you will see [result].
      The principles work."

  introduce_the_next_level:
    script: |
      "But here's what I've found after working with [number] of [avatars]...

      The people who get the fastest results aren't the ones who figure this out alone.
      They're the ones who have [what you provide — community/coaching/done-for-you/system].

      So I want to tell you about something I put together specifically for people in your situation."
```

### Step 6: Write the Offer Presentation (70-85 min)

```yaml
offer_section:
  introduce_the_offer:
    script: |
      "It's called [Program Name], and here's what it is...

      [2-3 sentence description of what the program does and who it's for]"

  value_stack:
    script: |
      "When you join [Program Name] today, here's exactly what you get:

      [Component 1]: [Benefit-focused description] — valued at $[X]
      [Component 2]: [Description] — valued at $[X]
      [Component 3]: [Description] — valued at $[X]
      [Bonus 1 — limited time]: [Description] — valued at $[X]
      [Bonus 2 — limited time]: [Description] — valued at $[X]

      If you went out and got all of this separately, you'd pay $[total value].
      But I'm not going to charge you that."

  price_reveal:
    script: |
      "Today — for people who are watching this training — the investment is [price].

      [If payment plan: Or if you'd prefer, you can split that into [X] payments of $[amount].]

      [Genuine reason why this price is what it is]"

  guarantee:
    script: |
      "And here's what I want you to know: this comes with our [Guarantee Name].

      [Guarantee terms — specific, not vague]

      [What this means for them — they have zero risk]"

  cta_and_urgency:
    script: |
      "Here's what to do right now:

      Click the button on your screen [or: go to [URL]].
      Fill out the order form — it takes 2 minutes.
      And you'll get immediate access to [first thing they receive].

      [If genuine urgency: This price / this bonus is available until [specific date and time]]

      The link is right there on your screen. Click it now."
```

### Step 7: Write Q&A / Objection Handling (85-90 min)

```yaml
qa_section:
  common_objections_to_handle:
    price_objection:
      question: "Is this worth the investment?"
      answer_script: |
        "Great question. Let me ask you this: what's it worth to you to [achieve the result]?
        [Cost of not solving the problem — specific]
        The investment is [price]. But the cost of NOT solving this is [ongoing cost].
        This isn't a cost — it's the end of a much bigger cost."

    time_objection:
      question: "I don't have time for this."
      answer_script: |
        "I hear this all the time, and here's the truth:
        [Problem they're trying to solve] is probably the thing stealing your time right now.
        [Program] requires [specific time commitment]. That's it.
        Most people spend [X minutes] and see [result] in [timeframe]."

    works_for_me_objection:
      question: "Will this work for my situation?"
      answer_script: |
        "Yes, if [qualifying criterion — what they need to have/be].
        Here's [testimonial from someone in a similar 'unique' situation].
        If you have [what they need], this will work."

  close_with_reminder:
    script: |
      "Alright, we're coming up on time. A couple of things before I let you go:

      [Summary of the offer — 2-3 sentences]
      [Restate CTA and URL]
      [Genuine deadline if applicable]

      If you have any questions, just [contact method].

      Thank you so much for spending your time with me today.
      Go take action — and I'll see you inside [Program Name]."
```

## Quality Standards
- Teaching content is 50-60% of webinar length (not 20% content, 80% pitch)
- Credibility established through story, not credential list
- Transition to offer is natural — not "okay now for the sales part"
- All objections addressed in Q&A section
- Scripts are conversational (not "read-aloud" formal)

## Veto Conditions
- VETO if content section is under 40 minutes
- VETO if credibility is just a list of achievements (no story)
- VETO if transition to offer is abrupt ("Okay! Now let me tell you about my program")
- VETO if guarantee is vague ("satisfaction guaranteed")
- VETO if no interactive elements in teaching section (people disengage)

## Completion Criteria
- [ ] Webinar parameters defined
- [ ] Pre-webinar content written
- [ ] Intro section (hook, promise, overview, credibility story)
- [ ] All 3-4 lessons written with interactive elements
- [ ] Transition to offer written
- [ ] Offer presentation (value stack, price, guarantee, CTA)
- [ ] Q&A section with objection handlers

## Handoff
- → write-email-sequence.md (webinar promotion sequence + follow-up)
- → write-sales-letter.md (if offer needs separate sales page)
- → craft-urgency-scarcity.md (for genuine webinar close urgency mechanism)

---
*Task: DRM_WEB_001 | Agent: frank-kern | Version: 1.0*
