# Task: Write Ad Variations

**Agent:** frank-kern
**Tier:** 2
**Type:** Creation
**Elicit:** false

## Purpose
Systematically create multiple ad variations that test different angles, hooks, and
emotional triggers — without reinventing the wheel for each one.
Frank Kern's principle: "Find one thing that works. Then make 50 versions of that
one thing. That's your testing strategy."

## The Variation Framework

Variations are NOT random rewrites. Each variation tests ONE specific variable
while keeping everything else constant.

```
WHAT TO VARY:
├── Hook type (problem / curiosity / social proof / story / contrarian)
├── Emotional driver (fear / aspiration / anger / hope / pride)
├── Avatar segment (different sub-avatar, same offer)
├── Angle / frame (same offer, different lens)
└── Proof element (different testimonial, different statistic)

WHAT STAYS CONSTANT (per batch):
├── Offer
├── Landing page
└── CTA
```

## Execution Steps

### Step 1: Identify the Control Ad

Before writing variations, document the control:

```yaml
control_ad:
  id: "CTRL-001"
  format: "[Facebook/YouTube/Google/Native/Email]"
  hook: "[First 1-2 lines or 5 seconds]"
  angle: "[Core angle — what problem/desire is it speaking to?]"
  emotional_driver: "[Primary emotion — fear/aspiration/curiosity/etc.]"
  avatar_segment: "[Which sub-avatar is this for?]"
  current_performance:
    ctr: "[%]"
    conversion_rate: "[%]"
    cpl_or_roas: "[$]"
  verdict: "[Is this our baseline to beat?]"
```

### Step 2: Variation Matrix

**Matrix A — Hook Type Variations (same angle, different opening):**

```yaml
hook_variations:
  var_A1:
    hook_type: "Problem/Pain"
    hook_script: "[Opens with the specific problem]"
    emotional_driver: "Pain avoidance"
    rest_of_ad: "[Same as control]"
    test_hypothesis: "Problem hook converts better than [control hook type] for this audience"

  var_A2:
    hook_type: "Curiosity/Mystery"
    hook_script: "[Opens with a gap they need to close]"
    emotional_driver: "Curiosity"
    rest_of_ad: "[Same as control]"
    test_hypothesis: "Curiosity hook outperforms direct problem hook for cold traffic"

  var_A3:
    hook_type: "Social Proof"
    hook_script: "[Opens with a number or result]"
    emotional_driver: "FOMO / validation"
    rest_of_ad: "[Same as control]"

  var_A4:
    hook_type: "Story"
    hook_script: "[Opens mid-scene in a relatable situation]"
    emotional_driver: "Identification"
    rest_of_ad: "[Same as control]"

  var_A5:
    hook_type: "Contrarian"
    hook_script: "[Opens by challenging a common belief]"
    emotional_driver: "Cognitive dissonance"
    rest_of_ad: "[Same as control]"
```

**Matrix B — Angle Variations (same avatar, different frame):**

```yaml
angle_variations:
  var_B1:
    angle: "Fear angle — what happens if they DON'T solve this"
    core_claim: "[How the offer appears through this lens]"
    hook: "[Hook for this angle]"
    body_summary: "[1-2 sentence summary of body copy for this angle]"

  var_B2:
    angle: "Aspiration angle — the dream life / outcome"
    core_claim: "[Offer through aspiration lens]"
    hook: "[Hook]"
    body_summary: "[Body summary]"

  var_B3:
    angle: "Authority angle — expert validation + mechanism"
    core_claim: "[Offer through authority lens]"
    hook: "[Hook]"
    body_summary: "[Body summary]"

  var_B4:
    angle: "Speed angle — fastest path to the result"
    core_claim: "[Offer through speed/shortcut lens]"
    hook: "[Hook]"
    body_summary: "[Body summary]"

  var_B5:
    angle: "Identity angle — who they become"
    core_claim: "[Offer through identity/transformation lens]"
    hook: "[Hook]"
    body_summary: "[Body summary]"
```

**Matrix C — Avatar Segment Variations (same offer, different who):**

```yaml
avatar_variations:
  var_C1:
    segment: "[Sub-avatar 1 — e.g., beginners]"
    specific_language: "[Their exact words and situation]"
    hook: "[Hook speaking directly to this segment]"
    proof: "[Testimonial from someone identical to this segment]"

  var_C2:
    segment: "[Sub-avatar 2 — e.g., people who tried and failed]"
    specific_language: "[Their vocabulary — frustrated, skeptical]"
    hook: "[Hook acknowledging their experience]"
    proof: "[Testimonial from skeptic-turned-believer]"

  var_C3:
    segment: "[Sub-avatar 3 — e.g., successful in one area but struggling in another]"
    specific_language: "[Their context-specific language]"
    hook: "[Hook]"
    proof: "[Testimonial from this segment]"
```

### Step 3: Full Ad Copy for Priority Variations

Write complete, production-ready copy for the top 5 priority variations:

```yaml
priority_variations:
  # Determine priority by: which variable we're testing in Phase 1 of split test plan

  priority_1:
    id: "VAR-001"
    variable_tested: "[Hook type]"
    reasoning: "[Why this is the highest-priority test]"

    facebook_primary_text: |
      "[Complete primary text — all lines, including hook, body, CTA]"

    headline: "[40 chars max]"
    description: "[30 chars max]"
    cta_button: "[Learn More / Get Started / Download / etc.]"
    visual_direction: "[Specific image/video direction for this variation]"

  priority_2:
    id: "VAR-002"
    variable_tested: "[Angle]"
    reasoning: "[Why]"
    facebook_primary_text: |
      "[Complete text]"
    headline: "[Headline]"
    description: "[Description]"
    cta_button: "[CTA]"
    visual_direction: "[Visual direction]"

  # Continue through priority_5...
```

### Step 4: Winning Signal Criteria

```yaml
winner_criteria:
  primary_metric: "[CTR / CPL / ROAS — what determines winner]"
  minimum_spend_before_decision: "$[amount per variation — based on CPL]"
  kill_threshold: "[If CTR < X% after $Y spent, pause]"
  scale_threshold: "[If CTR > X% or ROAS > Y, scale budget]"
  test_duration: "[Minimum days before decision — minimum 3-7 days]"

  learning_protocol:
    after_loser: "[Why did it lose? What does this teach about the audience?]"
    after_winner: "[What specifically drove the win? How can we extend this principle?]"
    documentation: "[Where to log learnings for future campaigns]"
```

### Step 5: Rapid Variation Template

For high-volume testing (50+ variations from a winning control):

```yaml
rapid_variation_protocol:
  # Take the winning hook. Change ONE element per variation.

  headline_swaps:
    # Keep everything, just change the headline
    - "[Benefit headline]"
    - "[Social proof headline]"
    - "[Question headline]"
    - "[How-to headline]"

  social_proof_swaps:
    # Keep everything, swap the testimonial used
    - from_avatar: "[Sub-avatar A testimonial]"
    - from_avatar: "[Sub-avatar B testimonial]"
    - data_point: "[Stat-based proof replacing testimonial]"

  cta_swaps:
    - "[Learn More]"
    - "[Get Started]"
    - "[Download Free Guide]"
    - "[See How It Works]"

  image_swaps:
    - "[Image concept A]"
    - "[Image concept B]"
    - "[Image concept C]"
```

## Quality Standards
- Each variation tests exactly ONE variable
- Control is documented before any variations are written
- Complete copy written for top 5 priority variations (not just concepts)
- Visual direction is specific for each variation
- Winner criteria defined before testing begins

## Veto Conditions
- VETO if multiple variables differ between control and variant
- VETO if variations are just different word choices (too micro — test bigger things first)
- VETO if no visual direction (creative team needs specific guidance)
- VETO if winner criteria not defined before testing
- VETO if fewer than 5 hook variations and 5 angle variations written

## Completion Criteria
- [ ] Control documented with current performance
- [ ] Hook variation matrix (5 variations)
- [ ] Angle variation matrix (5 variations)
- [ ] Avatar segment variations (2-3 segments)
- [ ] Complete copy for top 5 priority variations
- [ ] Winner criteria defined

## Handoff
- → create-split-test-plan.md (structure the actual test sequence)
- → write-facebook-ad-copy.md / write-youtube-ad-script.md (for full ad copy)
- → diagnose-funnel-leak.md (if all variations underperform — may be a funnel issue)

---
*Task: DRM_AVAR_001 | Agent: frank-kern | Version: 1.0*
