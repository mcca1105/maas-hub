# Task: Write Print Ad

**Agent:** gary-halbert
**Tier:** 1
**Type:** Creation
**Elicit:** true

## Purpose
Create direct response print advertisements for magazines, newspapers, and insert media.
Gary Halbert's principle: print ads must do the entire sales job in the space available —
every word, image, and white space must earn its place.

## Prerequisites
- Avatar research complete (create-customer-avatar.md)
- Offer defined (structure-irresistible-offer.md)
- Publication selected (audience profile matches avatar)

## Inputs Required
- Publication name and typical reader profile
- Ad size (full page, half page, quarter page, insert)
- Primary offer and CTA mechanism (phone, URL, coupon, QR)
- Budget and deadline for placement
- Proof elements available

## Execution Steps

### Step 1: Publication Context Analysis
Understand the environment where the ad will live:
- What editorial content surrounds the ad? (Ads in context of editorial content get 2x readership)
- What other advertisers are in this publication? (Differentiate)
- What tone matches readers' expectations?
- What page placement is available? (Right-hand page = premium, back cover = prime)

### Step 2: Format Strategy
Different sizes require different copy strategies:

**Full Page:** Can run long copy — use it. Direct response full-page ads often outperform
"brand-style" full-page ads by 3-5x when they include enough copy to sell.
- Headline: Bold, large, takes up top 25-33% of page
- Body copy: Tell the whole story — 300-800 words is appropriate
- Tracking: Unique phone number or URL per publication

**Half Page:** Economy of language required
- Headline must carry more weight
- Body copy: 150-300 words
- Visual if used must support, not compete with copy

**Quarter Page:** Almost all headline and CTA
- 2-3 headlines tested in rotation
- 50-100 words max
- Clear single CTA only

### Step 3: Headline Engineering
The headline is 80% of the ad. If the headline fails, nothing else matters.

Generate 5 headline variations using these proven structures:

**Structure A — Specific Benefit + Timeframe:**
"How [Avatar] Can [Specific Result] in [Specific Timeframe] — Even If [Biggest Objection]"
Example: "How Any Homeowner Can Cut Their Electric Bill By 43% in 30 Days — Even in a Small Apartment"

**Structure B — Provocative Question:**
"[Question that the avatar is already asking themselves at 2am]"
Example: "Why Do 87% of Diets Fail After the First 3 Weeks — and What Finally Works?"

**Structure C — News/Discovery:**
"[City] [Profession] Discovers [Unexpected Solution] to [Common Problem]"
Example: "Tampa Accountant Discovers Forgotten IRS Loophole That's Saving Retirees $6,200/Year"

**Structure D — Warning/Negative:**
"WARNING: If You're Still [Common Mistake], Read This Before It's Too Late"

**Structure E — Story:**
"I Was [Relatable Painful Situation] Until I Discovered [Mechanism]"

Select primary headline and keep 2 alternates for A/B testing across publications.

### Step 4: Body Copy Structure
For any ad with sufficient space:

**Lead (first paragraph):** Expand the headline promise. Make the reader commit to reading.
- Confirm they are the right person ("If you're a [avatar]...")
- Validate their problem ("You already know the frustration of...")
- Promise the revelation ("In the next 3 minutes, you'll discover...")

**Problem Agitation:** Make the pain real (2-3 paragraphs)
- The cost of NOT solving this (money, time, health, relationships)
- What they've probably already tried and why it didn't work
- The real reason the problem persists (hint at mechanism)

**Solution Reveal:** The mechanism (1-2 paragraphs)
- What it is (simple, specific, different from what they've tried)
- Why it works when other things don't (logic they can follow)
- One specific result as proof of concept

**Proof Stack:** (1-2 paragraphs or bulleted testimonials)
- Minimum 2 testimonials with: full name + city + specific result
- "John M., Tampa, FL" is NOT acceptable. "John Martinez, 54, Tampa FL, lost 31 pounds" IS.
- One data point or study if available

**Offer Presentation:** (clear box or section)
- What they get (specific)
- Normal value vs. today's price (anchoring)
- Bonus if acting by deadline
- Guarantee (strong and specific)

**CTA:** (large, impossible to miss)
- Exactly what to do: "Call 1-800-XXX-XXXX before [date]" or "Mail coupon below"
- Deadline with real reason ("We can only handle 50 new clients per month")
- What happens next ("You'll receive a call from our office within 24 hours")

### Step 5: Tracking Setup
Every print ad must be trackable:

```yaml
tracking_options:
  phone: "Unique phone number per publication — call tracking"
  url: "Unique URL per publication (e.g., yourbrand.com/mag23)"
  coupon: "Coupon code unique to publication and issue"
  qr_code: "QR code that redirects to tracked URL"
  address: "PO Box unique to publication (for mail-in response)"

tracking_metadata:
  publication: "[Name]"
  issue_date: "[Month/Year]"
  placement: "[Full page, half page, etc.]"
  page_position: "[Right-hand, left-hand, back cover]"
  unique_identifier: "[Code that identifies this specific placement]"
```

### Step 6: Visual Direction (if applicable)
Copy drives, visual supports. Never let art department make copy decisions.

**When to use images:**
- Before/after (if relevant and ethical)
- Product in use (shows context)
- Credibility visual (doctor, celebrity, results chart)
- Avoid: purely decorative images, stock photos of happy people unrelated to product

**Typography rules:**
- Headline: serif for readability in print, 36pt minimum for full page
- Body copy: 10-12pt, serif preferred for readability
- CTA: Must be largest element after headline
- White space: generous margins improve readability

## Quality Standards
- Every claim has a number, name, date, or specific detail
- The PS (if present) contains the complete CTA — it's read before the body
- Guarantee is prominently displayed, not buried
- Single CTA mechanism (not "call OR visit OR mail")
- Tracking element confirmed before print submission

## Veto Conditions
- VETO if headline is generic (no specificity, no differentiation)
- VETO if no tracking mechanism (can't measure ROI)
- VETO if no guarantee displayed
- VETO if CTA has multiple options without priority (decision paralysis)
- VETO if testimonials are initials-only or without specific results
- VETO if body copy starts with company name or logo

## Completion Criteria
- [ ] 5 headline variations written and primary selected
- [ ] Body copy complete (appropriate for ad size)
- [ ] Proof stack with 2+ specific testimonials
- [ ] Offer clearly presented with value anchoring
- [ ] Guarantee displayed prominently
- [ ] Single CTA with tracking mechanism
- [ ] Visual direction notes provided (if applicable)
- [ ] Deadline confirmed with publication

## Handoff
- → Production team with complete copy + tracking specs
- → audit-existing-copy.md if revising existing print campaign
- → create-split-test-plan.md for testing headlines across publications

---
*Task: DRM_PRINT_001 | Agent: gary-halbert | Version: 1.0*
