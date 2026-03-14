# DRM Squad — Documentation Index

Complete reference library for the Direct Response Marketing Squad.

---

## Frameworks (6 documents)

Foundational methodologies from each DRM specialist. Read these to understand the intellectual foundation of the squad.

| Document | Agent | What It Covers |
|----------|-------|----------------|
| [Awareness 5 Stages Framework](frameworks/awareness-5-stages-framework.md) | `@drm:eugene-schwartz` | The 5 levels of market awareness, market sophistication, mass desire. Core diagnostic for ALL copy work. |
| [RMBC Method Framework](frameworks/rmbc-method-framework.md) | `@drm:stefan-georgi` | Research → Mechanism → Brief → Copy. Complete VSL/sales letter pre-writing system. |
| [Halbert Copy Principles Framework](frameworks/halbert-copy-principles-framework.md) | `@drm:gary-halbert` | 40/40/20 rule, RFU formula, AIDA, Mel Martin bullets, headline system, Hamburger Stand. |
| [Cialdini 7 Principles Framework](frameworks/cialdini-7-principles-framework.md) | `@drm:robert-cialdini` | All 7 influence principles with audit checklist. Pre-Suasion channel concept. |
| [CVO Framework](frameworks/cvo-framework.md) | `@drm:ryan-deiss` | 7-step Customer Value Optimization: Lead Magnet → Tripwire → Core Offer → Profit Maximizers → Return Path. |
| [Frank Kern Behavioral Framework](frameworks/frank-kern-behavioral-framework.md) | `@drm:frank-kern` | Behavioral Dynamic Response, Intent Based Branding, Three Story System, Star Story Solution. |

---

## SOPs (4 documents)

Step-by-step execution guides for the most common DRM tasks. Each SOP is a complete, executable workflow.

| Document | Lead Agent | When to Use |
|----------|-----------|-------------|
| [SOP: VSL Creation](sops/sop-vsl-creation.md) | `@drm:stefan-georgi` | Creating or rewriting any Video Sales Letter |
| [SOP: Sales Letter Creation](sops/sop-sales-letter-creation.md) | `@drm:gary-halbert` | Long-form sales page, direct mail, email copy |
| [SOP: Avatar Research & Awareness Mapping](sops/sop-avatar-research.md) | `@drm:eugene-schwartz` | Any new project requiring prospect understanding |
| [SOP: Funnel Audit](sops/sop-funnel-audit.md) | `@drm:robert-cialdini` | Diagnosing existing funnel that is underperforming |

---

## Quick Decision Tree

**I need to start a new copy project:**
→ Begin with [Avatar Research SOP](sops/sop-avatar-research.md)
→ Then consult [Awareness 5 Stages Framework](frameworks/awareness-5-stages-framework.md)

**I need to write a VSL:**
→ Follow [SOP: VSL Creation](sops/sop-vsl-creation.md)
→ Reference [RMBC Method Framework](frameworks/rmbc-method-framework.md)

**I need to write a sales letter:**
→ Follow [SOP: Sales Letter Creation](sops/sop-sales-letter-creation.md)
→ Reference [Halbert Copy Principles Framework](frameworks/halbert-copy-principles-framework.md)

**I need to audit existing copy:**
→ Follow [SOP: Funnel Audit](sops/sop-funnel-audit.md)
→ Reference [Cialdini 7 Principles Framework](frameworks/cialdini-7-principles-framework.md)

**I need to design a funnel:**
→ Reference [CVO Framework](frameworks/cvo-framework.md)
→ Reference [Frank Kern Behavioral Framework](frameworks/frank-kern-behavioral-framework.md)

**I need to build an email campaign:**
→ Reference [Frank Kern Behavioral Framework](frameworks/frank-kern-behavioral-framework.md)
→ Reference [CVO Framework](frameworks/cvo-framework.md) (Return Path section)

---

## Agent-Framework Mapping

| Agent | Primary Frameworks | Primary SOPs |
|-------|--------------------|-------------|
| `@drm:drm-chief` | All (orchestration) | All (routing) |
| `@drm:eugene-schwartz` | Awareness 5 Stages | Avatar Research |
| `@drm:gary-halbert` | Halbert Copy Principles | Sales Letter Creation |
| `@drm:stefan-georgi` | RMBC Method | VSL Creation |
| `@drm:frank-kern` | Frank Kern Behavioral | — |
| `@drm:robert-cialdini` | Cialdini 7 Principles | Funnel Audit |
| `@drm:ryan-deiss` | CVO Framework | — |

---

## Validation Scripts

Located in `scripts/`:

| Script | Purpose | Usage |
|--------|---------|-------|
| `validate-copy-quality.py` | Score copy quality (Halbert standards) | `python validate-copy-quality.py --file copy.md` |
| `score-awareness-stage.py` | Diagnose awareness stage of copy or research | `python score-awareness-stage.py --copy copy.md --research voc.md` |
| `drm-cohesion-validator.py` | Check message consistency across funnel assets | `python drm-cohesion-validator.py --dir funnel/` |

---

*DRM Squad — Direct Response Marketing*
*Squad Registry: `squads/direct-response-marketing/`*
