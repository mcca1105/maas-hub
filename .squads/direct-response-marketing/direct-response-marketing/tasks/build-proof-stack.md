# Task: Build Proof Stack

**Agent:** robert-cialdini
**Tier:** 1
**Type:** Analysis
**Elicit:** true

## Purpose
Compile and organize all available proof elements in a hierarchy that matches the
market's sophistication level and the buyer's primary objections.
Robert Cialdini's principle: social proof is most powerful when it matches
the prospect's identity and specific situation.

## Proof Hierarchy (by credibility)

```
TIER 1 — Most credible:
├── Scientific studies (peer-reviewed, named institutions)
├── Expert endorsements (credentials visible, relevant to the claim)
└── Verifiable data (specific numbers, verifiable sources)

TIER 2 — High credibility:
├── Testimonials (full name + location + specific result)
├── Case studies (before/after with timeline)
└── Before/after demonstrations

TIER 3 — Supporting:
├── Media coverage (press mentions, interviews)
├── Volume/social proof ("47,000 customers")
└── Awards or certifications
```

## Execution Steps

### Step 1: Proof Inventory

```yaml
proof_inventory:
  # SCIENTIFIC PROOF
  studies_available:
    - study: "[Study title or description]"
      institution: "[Where published/conducted]"
      finding: "[Specific relevant finding]"
      relevance: "[Why this supports our specific claim]"
      citation: "[Author, Year, Publication]"

  # AUTHORITY PROOF
  expert_endorsements:
    - name: "[Expert name]"
      credential: "[Relevant credential + institution]"
      quote: "[Specific endorsement quote]"
      permission: "[Do we have permission to use this?]"

  # TESTIMONIALS
  testimonials:
    - name: "[Full name]"
      location: "[City, State/Country]"
      credential: "[Relevant detail — occupation, age, situation]"
      before: "[Their situation before]"
      result: "[Specific measurable result]"
      timeframe: "[How long to achieve result]"
      quote: "[Their exact words — verbatim]"
      format_available: "[text/video/audio]"
      permission: "[Documented yes/no]"

  # DATA/VOLUME PROOF
  data_points:
    - claim: "[Specific data point]"
      source: "[Where from]"
      relevance: "[Which objection does this address?]"

  # MEDIA COVERAGE
  media:
    - outlet: "[Publication/show name]"
      coverage: "[What was said or type of coverage]"
      date: "[When]"
      usable_as: "[Logo / quote / mention in copy]"
```

### Step 2: Proof Gap Analysis

Compare proof available vs. proof needed for the market's sophistication:

```yaml
proof_gap_analysis:
  market_stage: "[Stage 1-5]"
  stage_proof_requirements:
    stage_1_2: "Social proof + basic credibility sufficient"
    stage_3: "Mechanism proof required — studies or expert validation"
    stage_4: "Comparison proof — better than alternatives with evidence"
    stage_5: "Overwhelming volume + specific identity-matching testimonials"

  current_strengths: ["[Types of proof you have in abundance]"]
  current_gaps: ["[Types of proof you're missing]"]

  acquisition_plan:  # How to fill the gaps
    gap_1:
      missing: "[Type of proof]"
      how_to_get: "[Action to acquire it — survey customers, reach out to expert, find studies]"
      timeline: "[Days/weeks]"
```

### Step 3: Proof-to-Objection Mapping

Match each piece of proof to the objection it handles:

```yaml
objection_proof_map:
  "This won't work for me specifically":
    best_proof: "[Testimonial from someone identical to the prospect]"
    copy_placement: "[Problem section / testimonial block]"

  "I've tried similar things before":
    best_proof: "[Testimonial that explicitly says 'I tried X, Y, Z before this' + mechanism proof]"
    copy_placement: "[Failed solutions section]"

  "The price is too high":
    best_proof: "[ROI data / cost of problem vs. cost of solution / value stack total]"
    copy_placement: "[Price section / price anchoring]"

  "I don't believe the claims are real":
    best_proof: "[Scientific study + multiple verifiable testimonials]"
    copy_placement: "[Proof section — before price reveal]"

  "What if it doesn't work for me":
    best_proof: "[Strong guarantee + diverse testimonials showing range of results]"
    copy_placement: "[Guarantee section]"
```

### Step 4: Testimonial Formatting for Maximum Impact

**Full testimonial format (long-form, for sales page):**
```
"[Compelling first sentence that grabs attention — their key result or
transformation in their words]

[2-3 sentences about where they were before]

[2-3 sentences about the turning point or experience with the product]

[The specific result — as specific as possible: numbers, timeframes, comparisons]"

— [Full Name], [Age if relevant], [City, State]
  [Relevant credential: "Mother of 3" / "Former skeptic" / "Marketing Director at X"]
```

**Short testimonial format (for above fold, bullets):**
```
"[One or two sentences capturing the key transformation]"
— [Full Name], [City]
  [Key result in bold]
```

## Quality Standards
- All testimonials have: full name + location + specific result (no initials)
- Each proof element mapped to at least one specific objection it addresses
- Proof is sequenced by credibility tier (scientific first, then social)
- Testimonials represent diverse segments of the avatar (not all the same type)
- Video testimonials prioritized where available

## Veto Conditions
- VETO if any testimonial uses only initials or is anonymous without reason
- VETO if proof is generic (results not specific to the mechanism claimed)
- VETO if proof is presented before understanding what objections to address
- VETO if scientific proof is cited without verifiable source
- VETO if all testimonials are from the same type of person (ignores avatar diversity)

## Completion Criteria
- [ ] Proof inventory complete (all types cataloged)
- [ ] Proof gap analysis done (missing proof identified)
- [ ] Acquisition plan for missing proof documented
- [ ] Objection-to-proof mapping complete
- [ ] Testimonials formatted (long and short versions)
- [ ] Proof sequenced for copy use (which goes where)

## Handoff
- → build-rmbc-brief.md (proof stack feeds proof inventory section)
- → write-vsl-script.md or write-sales-letter.md (proof section)
- → write-testimonial-request.md (if gaps require more testimonials)

---
*Task: DRM_PROOF_001 | Agent: robert-cialdini | Version: 1.0*
