# Behavioral Sequence Checklist
**Agent:** `@drm:frank-kern`
**Purpose:** Validate Behavioral Dynamic Response (BDR) email sequences
**Standard:** Frank Kern — Behavioral Dynamic Response Framework
**Run:** Before activating any automated email sequence

---

## 🔴 CRITICAL — BDR Foundation

### Behavior-Trigger Architecture
- [ ] Every email in the sequence has a clear Response Indicator defined
  - (What action indicates engagement/interest/purchase intent?)
- [ ] Triggered actions are set for each Response Indicator:
  - [ ] "Clicked link" → tagged and moved to [sequence name]
  - [ ] "Visited sales page" → tagged and moved to [sequence name]
  - [ ] "Did NOT open after 3 emails" → moved to re-engagement
  - [ ] "Purchased" → moved to buyer onboarding, removed from prospect sequence
- [ ] No prospect receives two conflicting sequences simultaneously

### Sequence Purpose Clarity
Each sequence has ONE objective. Identify the objective:
- [ ] Welcome/Nurture (purpose: build trust, deliver value)
- [ ] Conversion (purpose: sell a specific offer)
- [ ] Post-Purchase Onboarding (purpose: ensure first result, reduce churn)
- [ ] Re-Engagement (purpose: wake up dormant subscribers)
- [ ] Objection Handling (purpose: address specific objections that prevented purchase)
- [ ] Upsell (purpose: sell next product to existing buyers)

**Sequence objective confirmed:** ___________________

---

## 🟡 HIGH PRIORITY — Sequence Structure

### Welcome/Nurture Sequence (if applicable)
- [ ] Email 1 (Day 0): Delivers what was promised. No pitch. Who you are.
- [ ] Email 2 (Day 1): Pure value. Solves one specific problem. No pitch.
- [ ] Email 3 (Day 3): Social proof. Specific case study. Response Indicator: click to story.
- [ ] Email 4 (Day 5): More value + soft mention of paid offer
- [ ] Email 5 (Day 7): Direct offer with full details

### Conversion Sequence (if applicable)
- [ ] Email 1: Problem agitation. "Here's what happens if you stay stuck."
- [ ] Email 2: Mechanism. "Here's why [product] works differently."
- [ ] Email 3: Proof. "Here's what happened for [specific person]."
- [ ] Email 4: Objection handling. "I know you might be thinking..."
- [ ] Email 5: Urgency. Deadline/bonus reminder.
- [ ] Email 6: Last chance. Real consequence of deadline.

### Buyer Onboarding Sequence (if applicable)
- [ ] Email 1 (Immediate): Welcome + how to get started (step 1 only)
- [ ] Email 2 (Day 1): Quick win tutorial (deliver one result fast)
- [ ] Email 3 (Day 3): How to use [feature/step 2] for best results
- [ ] Email 4 (Day 7): Community/support introduction
- [ ] Email 5 (Day 14): Check-in + referral ask

---

## 🟢 BEST PRACTICE — Behavioral Logic

### Segmentation Logic
- [ ] Each behavioral fork has been mapped out visually (or documented in CRM)
- [ ] "Did not engage" path has a consequence (re-engagement or removal)
- [ ] High-engagement path routes to higher-intent conversion sequence
- [ ] Buyer path is completely separate from prospect path
- [ ] Unsubscribe is suppressed from all non-essential sequences

### Elmer Wheeler Binary Gates
At least one binary choice gate present in the funnel (not just yes/no):
- [ ] "Which describes you better: [Option A] or [Option B]?"
- [ ] Each option routes to a more specific, relevant sequence
- [ ] Gate is presented naturally (as quiz, survey, or content choice)

### Timing Calibration
- [ ] Email spacing matches urgency level:
  - Nurture: every 2-3 days
  - Conversion: every 1-2 days
  - Deadline sequence: daily (last 48 hours)
- [ ] Sending time optimized for audience (typically 8-10am local, or 12-2pm)
- [ ] Weekend sends reduced for B2B, normal for B2C

---

## ❌ AUTO-FAIL CONDITIONS

- [ ] ❌ Buyers still receiving prospect/conversion emails after purchase
- [ ] ❌ No behavioral fork — same email sequence for all subscribers
- [ ] ❌ No "purchased" trigger removes them from close sequence
- [ ] ❌ Sequence continues sending after unsubscribe (CAN-SPAM violation)
- [ ] ❌ Re-engagement sequence not present for 60+ day inactives
- [ ] ❌ No Response Indicator defined for any email (untraceable)

---

## BDR SEQUENCE AUDIT SCORECARD

| Criterion | Score (1-3) |
|-----------|------------|
| Behavioral triggers defined | |
| Buyer removed from prospect sequence | |
| At least 2 behavioral forks mapped | |
| Each email has one clear goal | |
| Timing appropriate to sequence type | |
| Re-engagement path exists | |
| Binary gate present | |

**Total: ___/21**
- 18-21: Activate sequence
- 14-17: Fix gaps before activation
- Below 14: Rebuild sequence architecture

---

*Checklist by Frank Kern — Behavioral Dynamic Response (Mass Control, 2008)*
*DRM Squad — Direct Response Marketing*
