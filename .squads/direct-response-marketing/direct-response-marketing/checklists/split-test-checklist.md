# Checklist: Split Test Plan Quality

**Use when:** Reviewing a split test plan before launching tests.

---

## Section 1: Test Foundation

- [ ] Test hierarchy followed: Level 1 (Offer/Audience/Angle) before Level 2 (Headline) before Level 3 (Copy details)
- [ ] Control is documented with current performance metrics
- [ ] Hypothesis is written in If/Then/Because format
- [ ] Test isolates ONE variable only (nothing else changes between control and variant)
- [ ] Both control and variant are confirmed live and functioning

## Section 2: Statistical Validity

- [ ] Minimum 200 conversions planned per variant (not 20 or 30)
- [ ] Test runs minimum 14 days regardless of traffic volume
- [ ] Traffic is split 50/50 (or justified reason for different split)
- [ ] No seasonal events during test period that would skew results (holidays, sales events)
- [ ] 95% confidence level set as the standard for declaring a winner

## Section 3: Metrics & Tracking

- [ ] Primary metric clearly defined (single KPI — not "all metrics")
- [ ] Secondary metrics defined (for diagnostic purposes)
- [ ] Tracking confirmed working for both control and variant
- [ ] UTM parameters applied correctly to both versions
- [ ] Conversion window defined (24h vs. 7-day vs. 30-day)

## Section 4: Test Sequence Logic

- [ ] Phase 1 tests a macro variable (not a button color)
- [ ] Phase 2 is only run after Phase 1 winner is confirmed
- [ ] Testing calendar is mapped (not ad hoc)
- [ ] Maximum tests running simultaneously is 1 per page/element
- [ ] Kill conditions defined (when to pause early if one variant is clearly losing)

## Section 5: Decision Framework

- [ ] Winner criteria is pre-defined (not decided after seeing results)
- [ ] "No significant difference" scenario is planned for (move up the hierarchy)
- [ ] Winner deployment process is defined (who approves, how long before scaling)
- [ ] Learnings documentation template defined (what to record after each test)

## Section 6: Learning Protocol

- [ ] "Why" of winner is analyzed (not just that it won)
- [ ] "Why" of loser is analyzed (what does this tell us about the audience?)
- [ ] Insights are documented for future campaigns
- [ ] Winning element principles are extracted (not just the specific copy)

## Veto Conditions

- VETO if testing Level 3 variables (copy details) before Level 1-2 are validated
- VETO if fewer than 200 conversions planned per variant
- VETO if two variables differ between control and variant
- VETO if no hypothesis written
- VETO if test runs fewer than 14 days

---
*Checklist: DRM_CHK_SPLIT_001 | Version: 1.0*
