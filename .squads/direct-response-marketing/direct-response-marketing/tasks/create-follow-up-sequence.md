# Task: Create Follow-Up Sequence

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Design and write post-purchase follow-up sequences that convert buyers into repeat customers,
reduce refund rates, and generate referrals. Frank Kern's principle: the money is in
the relationship AFTER the sale — most businesses abandon customers at exactly the
wrong moment.

## Prerequisites
- Customer avatar defined (create-customer-avatar.md)
- Product/service fully understood (what does the customer experience in first 30 days?)
- Email platform configured with automation

## Inputs Required
- Product or service purchased
- Typical onboarding timeline (when do they first use it? see results?)
- Common sticking points (where do buyers give up?)
- Refund window (how long do you have to prove value before refund deadline?)
- Upsell opportunities (what's the logical next product/service?)

## Execution Steps

### Step 1: Map the Post-Purchase Journey
Understand what actually happens AFTER someone buys:

```yaml
post_purchase_journey:
  day_0: "Purchase confirmed — emotional high (buyer's excitement)"
  day_1: "Product received/access granted — first interaction"
  day_3: "First attempt to use — potential friction point"
  day_7: "First week check — did they get any results yet?"
  day_14: "Midpoint — are they still engaged or already disengaged?"
  day_21: "Habit formation window — 21 days to form new habit"
  day_30: "Refund window typically closes — but relationship continues"
  day_45: "Point where referrals become natural to ask for"
  day_60: "Logical time for upsell to next level"
```

Identify the 3 most common points where customers abandon or become unhappy.
These become the priority intervention points.

### Step 2: Define Sequence Objectives
Each follow-up sequence has one primary objective:

**Type A — Onboarding Sequence (Days 1-14):**
- Reduce refund rate
- Ensure first success (quick win)
- Build relationship before selling anything else

**Type B — Engagement Sequence (Days 14-30):**
- Maintain momentum after initial excitement wanes
- Address sticking points proactively
- Deepen relationship with stories and value

**Type C — Referral Sequence (Days 30-45):**
- Ask for referrals at peak satisfaction
- Make referral process easy
- Reward referrers

**Type D — Re-engagement Sequence (For disengaged buyers):**
- Identify subscribers who haven't opened in 21+ days
- Re-engage with pattern interrupt
- Prevent churn before it's formalized

**Type E — Upsell Sequence (Days 45-60):**
- Natural bridge from current product to next
- Only offer upsell after demonstrating value of original purchase
- Frame as "logical next step," not "more money"

Select which type(s) this task is building.

### Step 3: Quick Win Engineering
The most important email in any onboarding sequence:
**The Quick Win Email (Send within 48 hours of purchase)**

Goal: Get the customer to experience one small, real win as fast as possible.

Structure:
1. Celebrate their decision (validation — they made the right choice)
2. Set expectations (what to do FIRST — not overwhelm with everything)
3. Deliver the quick win (one specific, achievable action with immediate result)
4. Ask for confirmation ("Reply 'done' when you complete this")

Example quick win: "Before you do anything else, complete this one 5-minute exercise.
When you finish it, you'll [specific outcome]. Here's exactly what to do: [step-by-step]"

### Step 4: Email Architecture Per Sequence Type

**Onboarding Sequence (12 emails over 14 days):**
- Day 0: Confirmation + What to expect
- Day 1: The Quick Win (most important email)
- Day 2: Story email (build relationship — share relevant story)
- Day 3: First sticking point preempted ("By now you might be wondering...")
- Day 5: Social proof (share a customer story similar to their situation)
- Day 7: Check-in ("How is it going? Here's what to do if you're stuck")
- Day 9: The "why" email (deeper insight into the mechanism)
- Day 11: Second sticking point preempted
- Day 13: Celebration + what's coming next
- Day 14: Gratitude + community invitation (if applicable)

**Re-engagement Sequence (5 emails):**
- Email 1: Pattern interrupt subject line ("I give up")
- Email 2: Value drop (free resource, no selling)
- Email 3: Direct question ("Are you still interested in [result]?")
- Email 4: Case study from someone like them
- Email 5: The break-up email ("This is the last email I'll send...")

### Step 5: Email Writing Formula Per Type

**Relationship Emails (onboarding days 2, 5, 9):**
Structure: Story → Lesson → Application → Soft CTA
- Open with story (relevant to avatar's journey)
- Extract the lesson the story teaches
- Show how to apply it to their situation
- Soft CTA (open the product, join the community, reply with a question)

**Problem-Anticipation Emails (days 3, 11):**
Structure: Acknowledge → Validate → Solution → Action
- "By now, you might be experiencing [specific sticking point]"
- "That's completely normal and here's why it happens"
- "Here's exactly what to do when this happens: [specific instructions]"
- "Do this right now: [single action]"

**Social Proof Emails (day 5, 13):**
Structure: Similar situation → Journey → Result → Bridge to reader
- "Meet [Name], who was exactly where you are now..."
- Describe their journey (relatable struggle)
- Share the specific result
- "You're on the same path. Here's your next step..."

### Step 6: Subject Line Strategy

Subject lines for follow-up sequences differ from cold email:
These people KNOW you — use familiarity to your advantage.

**High-performing subject line formulas for follow-up:**
- "[First name], did you try this yet?"
- "Quick question about your progress"
- "The mistake most people make in week 1 (and how to avoid it)"
- "I was thinking about you"
- "This took me 3 years to figure out (it'll take you 3 minutes)"
- "Bad news about [product benefit]" (opens a loop they need to close)
- "I give up" (re-engagement)
- "Last email about this"

Never use: "SALE INSIDE," excessive caps, emoji strings, misleading clickbait

### Step 7: Automation Setup Notes

```yaml
automation_requirements:
  trigger: "Tag applied at purchase — '[Product Name] Buyer'"
  suppression: "Remove from sequence if they purchase next product (don't double-message)"
  timing: "Business days for high-value content; can use any day for check-ins"
  personalization:
    - "[First name]" in every email
    - "[Product name]" referenced specifically
    - Segment by: product tier, referral source, engagement level
  goal_tracking:
    - Open rate per email (benchmark: >25% for buyer sequences)
    - Click rate per email (benchmark: >3%)
    - Reply rate (high reply rate = relationship is working)
    - Refund rate vs. control (does sequence reduce refunds?)
    - Upsell conversion (does engagement sequence improve upsell take rate?)
```

## Quality Standards
- Quick win email delivers an actual win, not just motivation
- No email in the sequence tries to sell something before value is established
- Each email has one purpose and one CTA
- Sticking points identified from real data (support tickets, survey responses)
- Subject lines avoid spam triggers
- Sequence length matches the complexity of the product (simple product = shorter sequence)

## Veto Conditions
- VETO if first email after purchase is selling an upsell (before any value delivered)
- VETO if quick win is vague or takes more than 15 minutes to complete
- VETO if sequence has no mechanism to identify engaged vs. disengaged buyers
- VETO if emails are all the same format (all story, all tips, all promos)
- VETO if subject lines are salesy or manipulative ("URGENT: Your account is at risk")

## Completion Criteria
- [ ] Post-purchase journey mapped with friction points identified
- [ ] Sequence type(s) selected with rationale
- [ ] Quick win email written and tested
- [ ] All emails written with specific subject lines
- [ ] Automation logic documented (triggers, suppressions, tags)
- [ ] Success metrics defined with benchmarks
- [ ] Sequence reviewed for tone consistency (Frank Kern: warm, personal, never corporate)

## Handoff
- → Email platform specialist for technical setup
- → design-upsell-sequence.md when sequence reaches upsell window
- → write-email-sequence.md for promotional campaigns layered on top

---
*Task: DRM_EMAIL_002 | Agent: frank-kern | Version: 1.0*
