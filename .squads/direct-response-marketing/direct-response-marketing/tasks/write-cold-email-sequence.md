# Task: Write Cold Email Sequence

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** true

## Purpose
Create cold email sequences that open conversations — not pitch decks.
Frank Kern's principle applied to cold outreach: the goal of cold email is NOT to sell —
it's to earn the right to have a conversation. Selling comes in the conversation.

## Prerequisites
- Target prospect profile defined (company size, role, industry, trigger events)
- Value proposition clear (what do you offer and why should THEY care?)
- Goal of the sequence defined (reply, call booked, trial started, etc.)

## Inputs Required
- Target prospect description (specific role, industry, company type)
- What trigger event or context makes them a good prospect right now?
- Sequence goal (reply, call, demo, visit, download)
- What you offer and the specific value to THIS type of prospect
- Number of emails in sequence and maximum send window

## The Cold Email Mindset

Cold email is not mass spam. It is targeted, personalized outreach.
The ratio that determines success: **Relevance / Friction**

- Higher relevance = higher response rate
- Lower friction (what you ask them to do) = higher response rate
- The goal is to MAXIMIZE relevance and MINIMIZE friction

## The 4-Email Cold Sequence Structure

```
Email 1: The Relevance Email (Day 1)
Email 2: The Value Email (Day 3-4)
Email 3: The Case Study Email (Day 7-8)
Email 4: The Permission Break-Up (Day 12-14)
```

Maximum 4 emails before removing prospect from sequence.
Beyond 4 without response = low relevance or wrong prospect.

## Execution Steps

### Step 1: Pre-Writing Prospect Research
Before writing a single email, research the specific prospect (or prospect type):

```yaml
prospect_intelligence:
  company: "[Company Name]"
  role: "[Their specific title]"
  recent_trigger: "[Funding? New hire? Job post? Content they published? Award?]"
  specific_pain: "[Based on their role/industry, what problem do they likely have?]"
  your_connection: "[How is what you do directly relevant to THEIR situation?]"
  personalization_hook: "[The one specific thing that makes this email about THEM, not you]"
```

Personalization hook examples:
- "I saw your team is hiring [role] — that usually means [implication related to your offer]"
- "I read your article on [topic] — your point about [specific point] resonated"
- "Congratulations on the Series B — companies at this stage often face [specific challenge]"
- "I noticed [Company] just entered [market] — I worked with [similar company] when they did the same"

### Step 2: Email 1 — The Relevance Email

**Goal:** Get a reply. Nothing else.
**Length:** 75-100 words maximum.
**Tone:** Human, curious, not salesy.

**Structure:**
1. Opening hook (one personalized line — about THEM, not you)
2. One-sentence reason for reaching out (what you noticed or why now)
3. One-sentence value proposition (not a pitch — a hypothesis)
4. Low-friction CTA (question or simple yes/no)

**Template:**
```
Subject: [Their company] + [Relevant trigger/observation]

[First name],

[Personalized opening about them — 1 sentence]

[Reason for reaching out — connects your observation to a potential problem]

[Hypothesis: "I've helped [similar companies] solve [specific problem].
Wondering if [specific aspect] is something on your radar?"]

[Simple CTA: "Worth a quick chat?" OR "Is this relevant to what you're
working on?" OR "Happy to share more if useful."]

[Name]
```

**Real example:**
```
Subject: Noticei que a [Empresa] está contratando 3 SDRs

João,

Vi que vocês estão contratando 3 SDRs — geralmente isso significa uma
meta agressiva de outbound à frente.

Trabalhei com a [Empresa Similar] quando eles escalaram o time de 12 para
40 SDRs no ano passado. O maior gargalo foi velocidade de resposta a leads —
o tempo médio de 6h para primeiro contato estava matando a conversão.

Isso é algo que está no radar de vocês?

[Nome]
```

### Step 3: Email 2 — The Value Email

**Goal:** Deliver value before asking for anything.
**Length:** 100-150 words.
**Tone:** Generous, helpful, no strings attached.

**Trigger:** Send only if Email 1 was opened but not replied to (or 3-4 days after, regardless).

**Structure:**
1. Brief reference to previous email (not "just following up")
2. Deliver a genuine piece of value (insight, resource, data, observation)
3. No CTA except "thought this might be useful"

**Template:**
```
Subject: Something that might be useful for [their company/initiative]

[First name],

Reaching out again quickly — I put together [specific resource/insight]
that I think is directly relevant to what you're working on.

[Deliver the value: a data point, a short insight, a link to something
genuinely useful, a specific observation]

[How it connects to their situation in one sentence]

No need to reply — just thought you'd want to have this.

[Name]
```

### Step 4: Email 3 — The Case Study Email

**Goal:** Make the outcome tangible with a specific example.
**Length:** 150-200 words.
**Tone:** Story-driven, specific, evidence-based.

**Structure:**
1. One line acknowledging they're probably busy
2. Specific case study (company like theirs + their problem + your solution + specific result)
3. Soft question: does this resonate?

**Template:**
```
Subject: How [Similar Company Type] went from [Problem] to [Result] in [Timeframe]

[First name],

Quick one — I wanted to share a specific example that might be relevant.

[Similar Company Type] came to us when [specific situation that mirrors
likely prospect situation].

We [specific action taken]. In [timeframe], they achieved [specific
measurable result].

The key insight: [one sentence that applies to the prospect's situation].

I'm guessing [Prospect Company] faces a similar situation given [observation].
Does this resonate at all?

[Name]
```

### Step 5: Email 4 — The Permission Break-Up

**Goal:** One last genuine attempt — or a clean ending.
**Length:** 75-100 words.
**Tone:** Direct, honest, zero pressure.

The break-up email often gets the highest response rate in the sequence.
People respond when they feel the pressure is off.

**Template:**
```
Subject: Closing the loop

[First name],

I've reached out a few times and haven't heard back — so I'll assume
the timing isn't right.

I won't follow up again after this.

If [specific problem] ever becomes a priority, I'm happy to reconnect.
Here's a resource in the meantime that you might find useful when
that happens: [link to something genuinely valuable]

Take care,
[Name]
```

### Step 6: Subject Lines

Cold email subject lines must:
- Be short (3-6 words)
- Feel personal (not broadcast)
- Create curiosity without clickbait
- Reference something specific

**Strong subject line formulas:**
- "[Their company] + [relevant observation]"
- "Quick question about [specific topic]"
- "Idea for [their company/initiative]"
- "How [similar company] solved [problem]"
- "Relevant to [their role/initiative]"
- "[First name] — [specific observation]"

**Avoid:**
- ALL CAPS
- Exclamation points
- "Check this out!"
- Vague: "Following up" (the most deleted subject line in existence)
- Misleading: "Re: our conversation" (when there was none)

## Quality Standards
- Email 1 is under 100 words — no exceptions
- Each email has ONE low-friction CTA
- At least 1 personalized element per email (not just first name)
- No email begins with "My name is..." or company introduction
- Break-up email gives them something useful (not just "goodbye")
- Subject lines are 3-6 words and personal in tone

## Veto Conditions
- VETO if any email opens with "My name is [X] and I work at [Company]"
- VETO if Email 1 is longer than 100 words
- VETO if sequence has more than 4 emails (spam territory)
- VETO if subject lines use "Re:" deceptively
- VETO if CTA asks for a meeting before establishing any relationship
- VETO if emails are clearly templates with obvious personalization tokens (like "[COMPANY NAME]" left in)

## Completion Criteria
- [ ] Prospect profile and personalization hooks documented
- [ ] Email 1 (relevance) written — under 100 words, personalized
- [ ] Email 2 (value) written — genuine value, no CTA
- [ ] Email 3 (case study) written — specific result, relatable company
- [ ] Email 4 (break-up) written — direct, clean, no guilt
- [ ] Subject lines written for each (primary + backup)
- [ ] Sending schedule documented
- [ ] Follow-up trigger conditions documented (open-based vs. time-based)

## Handoff
- → write-email-sequence.md (if prospect converts to warm lead, shifts to nurture)
- → create-customer-avatar.md (if prospect research reveals gaps in avatar understanding)
- → create-split-test-plan.md (test subject lines and Email 1 variations)

---
*Task: DRM_COLD_001 | Agent: frank-kern | Version: 1.0*
