# Direct Response Marketing - Source Tree

```
squads/direct-response-marketing/
│
├── squad.yaml                          # Squad manifest
├── README.md                           # Squad documentation
│
├── config/                             # Configuration files
│   ├── coding-standards.md             # Copy, VSL, ad standards
│   ├── tech-stack.md                   # Tools and platforms
│   └── source-tree.md                  # This file
│
├── agents/                             # Agent definitions (6 minds)
│   ├── vsl-master.md                   # Stefan Georgi clone - VSL scripts
│   ├── copy-legend.md                  # Schwartz/Halbert clone - Sales copy
│   ├── ad-creative-genius.md           # Kern/Hormozi clone - Ad creatives
│   ├── funnel-architect.md             # Brunson clone - Funnel strategy
│   ├── conversion-scientist.md         # Deiss/Belcher clone - Analytics
│   └── landing-page-psychologist.md    # Cialdini clone - Persuasion design
│
├── tasks/                              # Task definitions (task-first!)
│   ├── vsl-master-create-vsl-script.md               # Create VSL script
│   ├── copy-legend-write-sales-letter.md             # Write long-form sales letter
│   ├── ad-creative-genius-create-ad-campaign.md      # Create ad campaign
│   ├── funnel-architect-design-funnel.md             # Design conversion funnel
│   ├── conversion-scientist-analyze-metrics.md       # Analyze metrics & optimize
│   └── landing-page-psychologist-optimize-page.md    # Optimize landing page
│
├── workflows/                          # Multi-step workflows
│   ├── launch-new-product.md           # Complete product launch workflow
│   ├── optimize-existing-funnel.md     # Funnel optimization workflow
│   └── ab-test-campaign.md             # A/B testing workflow
│
├── checklists/                         # Validation checklists
│   ├── vsl-review-checklist.md         # VSL quality checklist
│   ├── ad-review-checklist.md          # Ad creative checklist
│   ├── funnel-review-checklist.md      # Funnel structure checklist
│   └── pre-launch-checklist.md         # Pre-launch validation
│
├── templates/                          # Document templates
│   ├── vsl-script-template.md          # VSL script structure
│   ├── sales-letter-template.md        # Long-form sales letter
│   ├── ad-brief-template.md            # Ad creative brief
│   ├── funnel-map-template.md          # Funnel visualization
│   └── analytics-report-template.md    # Weekly/monthly report
│
├── tools/                              # Custom tools
│   ├── headline-analyzer.js            # Headline scoring
│   ├── readability-checker.js          # Copy readability
│   ├── cta-extractor.js                # Extract CTAs from copy
│   └── swipe-file-organizer.js         # Organize swipe files
│
├── scripts/                            # Utility scripts
│   ├── generate-utm-links.js           # Generate UTM parameters
│   ├── export-ga4-data.js              # Export analytics data
│   ├── scrape-competitor-ads.js        # Competitor research
│   └── calculate-funnel-metrics.js     # Funnel KPI calculator
│
└── data/                               # Static data
    ├── swipe-files/                    # Proven ads & copy
    │   ├── vsl-scripts/
    │   ├── sales-letters/
    │   ├── ad-creatives/
    │   └── landing-pages/
    │
    ├── frameworks/                     # Framework documentation
    │   ├── rmbc-method.md              # Stefan Georgi's RMBC
    │   ├── 5-stages-awareness.md       # Eugene Schwartz framework
    │   ├── grand-slam-offer.md         # Alex Hormozi framework
    │   ├── value-ladder.md             # Russell Brunson framework
    │   ├── cvo-framework.md            # Ryan Deiss framework
    │   └── cialdini-principles.md      # Robert Cialdini principles
    │
    ├── benchmarks/                     # Industry benchmarks
    │   ├── conversion-rates.json       # Average conversion rates by industry
    │   ├── cpc-benchmarks.json         # Cost per click by platform
    │   └── ltv-benchmarks.json         # Lifetime value by niche
    │
    └── glossary/                       # Terminology
        └── direct-response-terms.md    # DR marketing glossary
```

## Directory Purpose

### `/agents`
Contains the 6 core agent definitions, each cloning a real-world expert:
- Each agent has specific frameworks, methodologies, and voice
- Agents collaborate on campaigns but have distinct specializations

### `/tasks`
Task-first architecture - executable workflows for each agent:
- Each task is atomic and well-defined
- Tasks can be chained in workflows
- Include elicitation for user input when needed

### `/workflows`
Multi-step processes that orchestrate multiple agents/tasks:
- Product launches
- Campaign optimization
- A/B testing protocols

### `/checklists`
Quality assurance and review checklists:
- Pre-launch validation
- Copy review criteria
- Performance audit

### `/templates`
Reusable document structures:
- VSL scripts
- Sales letters
- Ad briefs
- Analytics reports

### `/tools`
Custom JavaScript tools for automation:
- Headline analysis
- Readability scoring
- Link generation

### `/scripts`
Utility scripts for common operations:
- UTM generation
- Data export
- Metric calculation

### `/data`
Static reference data:
- Swipe files (proven examples)
- Framework documentation
- Industry benchmarks
- Terminology glossary

## File Naming Conventions

### Agents
`{specialization}-{variation}.md`
- Examples: `vsl-master.md`, `copy-legend.md`

### Tasks
`{agent-name}-{action}-{object}.md`
- Examples: `vsl-master-create-vsl-script.md`

### Workflows
`{verb}-{object}.md`
- Examples: `launch-new-product.md`, `optimize-existing-funnel.md`

### Templates
`{document-type}-template.md`
- Examples: `vsl-script-template.md`, `ad-brief-template.md`

### Data Files
`{category}-{description}.{ext}`
- Examples: `conversion-rates.json`, `rmbc-method.md`

## Growth Pattern

As the squad evolves:
1. **More agents** → Add specialists (Email Sequence Writer, Webinar Expert, etc.)
2. **More tasks** → Granular tasks for specific scenarios
3. **More workflows** → Campaign types (Challenge funnel, Summit funnel, etc.)
4. **More templates** → Specific to offers/niches
5. **More data** → Swipe files, case studies, benchmarks

## Integration Points

### With AIOS Core
- Uses core task execution engine
- Inherits base agent architecture (if config.extends = extend)
- Leverages core utilities (file handling, etc.)

### With Other Squads
- Can collaborate with `content-creation` squad for content
- Can use `analytics` squad for deep data analysis
- Can integrate with `automation` squad for workflow automation

## Maintenance

### Regular Updates
- [ ] Update benchmarks quarterly
- [ ] Add new swipe files weekly
- [ ] Review framework docs monthly
- [ ] Update tech stack as tools evolve

### Version Control
- Major version bump for breaking changes
- Minor version bump for new agents/tasks
- Patch version bump for fixes/improvements
