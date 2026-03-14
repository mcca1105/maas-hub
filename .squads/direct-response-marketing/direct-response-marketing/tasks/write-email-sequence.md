# Task: Write Email Sequence

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Write complete direct response email sequences — welcome series, nurture, promotional,
and re-engagement. Frank Kern's principle: the email relationship is built on value first,
story always, and selling only when the ground is prepared.

## Prerequisites
- Avatar defined (create-customer-avatar.md)
- Sequence type and goal identified
- Lead magnet or entry point defined

## Inputs Required
- Sequence type: welcome / nurture / promotional / cart-abandonment / re-engagement
- List temperature: new subscribers, engaged list, cold list
- Product or offer being supported (if any)
- Number of emails requested and send cadence
- Brand voice notes

## Execution Steps

### Step 1: Sequence Architecture
Define the structure before writing a single email.

```yaml
sequence_blueprint:
  type: "[welcome/nurture/promo/re-engagement]"
  total_emails: [number]
  send_schedule:
    email_1: "Immediately on trigger"
    email_2: "Day 1"
    email_3: "Day 3"
    # continue...
  primary_goal: "[What you want readers to DO at end of sequence]"
  secondary_goals:
    - "[Build trust]"
    - "[Establish authority]"
  key_objections_to_address: []
  stories_to_use: []
```

### Step 2: Subject Line Strategy
Subject lines are 50% of whether the email gets read. Write 3 options per email.

**Formula library:**
- Curiosity gap: "The thing most [avatars] get wrong about [topic]"
- Specific benefit: "How to [result] in [timeframe]"
- Story opener: "I almost quit [topic] until this happened"
- Question: "Are you making this [topic] mistake?"
- Number: "3 reasons your [effort] isn't working"
- Warning: "Stop doing this if you want [result]"
- Personal: "I need to tell you something about [topic]"

### Step 3: Email Structure (Frank Kern Format)
Every email in the sequence follows this flow:

**Opening Hook (Line 1-2):**
Never open with "Hey, it's [name] from [company]."
Open with a story fragment, a question, a bold statement, or a specific scenario.
Examples:
- "Yesterday I watched someone throw away $40,000."
- "Quick question: have you ever felt like you're the only one who [problem]?"
- "Three years ago I was [relatable painful situation]."

**Story Body:**
- One story per email (not multiple)
- Story must relate to the lesson being taught
- Story should feature relatable character (the sender, a customer, someone the avatar knows)
- Stakes must be clear — what was at risk?
- Resolution teaches the lesson

**The Pivot:**
Natural transition from story to lesson:
- "The reason I'm telling you this is..."
- "What I learned from that experience was..."
- "Here's why this matters to you..."

**The Value/Lesson:**
- One key takeaway (not three — one)
- Specific and actionable
- Something they can use TODAY

**The CTA:**
- ONE call to action per email
- Soft CTA for relationship emails: "Reply and tell me [question]"
- Hard CTA for promo emails: "Click here to [specific action]"
- Never: "Click here to learn more" (vague)
- Always: "Click here to [specific outcome they get]"

### Step 4: Sequence-Specific Writing Guidelines

**Welcome Sequence (5-7 emails, Days 0-14):**
Email 1 (immediate): Deliver the lead magnet + set expectations for what's coming
Email 2 (Day 1): Origin story — why you do what you do (makes you human)
Email 3 (Day 3): Your biggest mistake in this field (vulnerability builds trust)
Email 4 (Day 5): Teaching email — your best tip/strategy (demonstrates value)
Email 5 (Day 7): Social proof — customer story (makes outcomes real)
Email 6 (Day 10): Belief-shifting email (address the biggest misconception in the market)
Email 7 (Day 14): Soft introduction to offer (after 2 weeks of pure value)

**Promotional Sequence (5-7 emails, 7-day window):**
Email 1: Open cart — excitement, story of transformation, offer reveal
Email 2 (Day 2): Deep dive on one component of the offer (build desire)
Email 3 (Day 3): Social proof email (testimonials, case studies)
Email 4 (Day 4): Objection handler (answer the most common reason they don't buy)
Email 5 (Day 5): FAQ email (practical questions answered)
Email 6 (Day 6): Scarcity/urgency email ("closing tomorrow")
Email 7 (Day 7): Close — last chance email (morning and evening versions)

**Re-engagement Sequence (5 emails):**
Email 1: Pattern interrupt subject ("I give up")
Email 2: Pure value drop — no selling whatsoever
Email 3: Direct question — "Are you still interested in [specific result]?"
Email 4: Case study — someone who WAS disengaged and came back
Email 5: The breakup email — last email if no engagement

### Step 5: Write Each Email
For each email, produce:

```markdown
---
EMAIL [N] OF [TOTAL]
Subject Options:
  A: "[Option A]"
  B: "[Option B]"
  C: "[Option C]"
Primary Subject: A/B/C

---

[Body copy — written in conversational, direct style]

[Signature]
[Name]

P.S. [Strategic PS — often used for secondary CTA or key reinforcement]
---
```

### Step 6: Sequence Review
Before finalizing, check the sequence as a whole:
- Does each email feel like it comes from a person, not a brand?
- Is there a natural escalation of relationship?
- Does each email stand alone (in case someone misses a previous one)?
- Is the selling gradual and earned (not front-loaded)?
- Does the PS of each email reinforce or add value?

## Quality Standards
- Each email opens with hook — never company introduction
- Every email has exactly one CTA
- Story present in relationship emails (at minimum 60% of emails)
- Subject lines are specific — no "Newsletter Update" or "Weekly Tips"
- Sequence has clear emotional arc (trust building → value → offer)
- Total read time per email: 90-150 seconds (300-500 words)

## Veto Conditions
- VETO if any email opens with "Hi, I'm [name] from [company]"
- VETO if email has more than one CTA
- VETO if subject line is generic or could be sent by any brand
- VETO if promotional email comes before trust-building emails in welcome sequence
- VETO if re-engagement sequence is just a resend of previous emails

## Completion Criteria
- [ ] Sequence architecture documented before writing
- [ ] Subject line options (3 each) written for every email
- [ ] Every email follows hook → story → lesson → CTA structure
- [ ] Sequence reviewed as complete unit (arc makes sense)
- [ ] Sending cadence documented
- [ ] Automation trigger and suppression logic noted

## Handoff
- → Email platform specialist for technical setup
- → create-split-test-plan.md for subject line A/B testing
- → create-follow-up-sequence.md if this is a post-purchase sequence

---
*Task: DRM_EMAIL_001 | Agent: frank-kern | Version: 1.0*
