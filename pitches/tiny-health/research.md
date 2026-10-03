# Tiny Health — Research Findings

**Company:** Tiny Health (tinyhealth.com)  
**Slug:** tiny-health  
**Funding:** $33M Series B (Sept 29, 2026), led by B Capital. Total raised: $46M ($4.5M seed 2021, $8.5M Series A late 2023)  
**Source:** [Crunchbase News](https://news.crunchbase.com/venture/tiny-health-33m-microbiome-tests-sew-hoy/) + [Founder Letter](https://tinyhealth.com/blog/tiny-health-series-b-letter-from-cheryl-sew-hoy)  
**HQ:** Austin, TX  
**Founder/CEO:** Cheryl Sew Hoy (serial entrepreneur, sold Reclip.It to Walmart Labs 2013)  
**Employees:** ~40 currently, planning to hire 30 more  
**Stage:** Series B (Seed → Series C range ✓)

---

## Product & Positioning

**Core offering:** At-home gut & vaginal microbiome tests using **shotgun metagenomic sequencing** (gold standard). Tests identify **120,000+ microbes** (bacteria, viruses, fungi, parasites) down to **0.005% relative abundance** with **strain-level resolution**.

**Product lines:**
- **Baby Gut Health Test** ($249) — ages 0-3, first research-backed test for this age group
- **Child Gut Health Test** ($249) — ages 3-17
- **Adult Gut Health Test** ($249)
- **Vaginal Health Test** ($249)
- **Pregnancy Gut Health Test** ($249)
- **PRO Gut Health Test** — expanded markers (sIgA, calprotectin, elastase, etc.), practitioner-ordered
- **Memberships (Tiny+)** — subscription with 2 tests/year + coaching: Family ($399/yr), Adult, Baby, Child, Vaginal

**Key differentiators from website:**
- Largest repository of longitudinal pregnancy & baby microbiome samples globally
- Mom & baby reference ranges (others use adult ranges for kids)
- Unbiased supplement recommendations (don't sell their own probiotics)
- Expert 1:1 consult call with microbiome expert included
- CLIA-certified, CAP-accredited, HIPAA-compliant lab partners
- 3-4 week turnaround

**Target conditions:** Eczema, allergies, asthma, IBS/IBD, constipation, bloating, fertility, pregnancy/postpartum, chronic conditions, digestive issues, vaginal health (BV, yeast, STIs)

**Traction (from Series B letter):**
- Nearly **200,000 customers** served
- **6,000+ healthcare practitioners** across independent practices, hospital systems, longevity clinics, precision medicine orgs
- Partners: **Mayo Clinic Executive Health & Longevity**, Atria, Superpower, Fullscript
- Revenue **more than doubled each year**; B2B arm ("Powered by Tiny") grew **4x last year**
- Published **4 scientific papers** including RCT in *Pediatric Allergy and Immunology* showing **83% lower odds of eczema/allergic conditions** in infants in their personalized program
- **$5M committed** to Microbiome Research Program for researcher/clinician access
- **TinyAI** in development — AI trained on proprietary dataset of ~200k microbiome profiles

---

## Technology Stack & Technical Surface

**Sequencing & Bioinformatics (from /technology page):**
- **Shotgun metagenomic sequencing** — unbiased, hypothesis-free, complete picture
- **Proprietary bioinformatics platform** components named:
  - **thMP** — metagenomic processing
  - **thDB** — database
  - **thDD** — data delivery
  - **thMAP** — reference range mapping
- **Machine learning** for personalized recommendations based on results + survey data
- **Quality control checks** at multiple stages
- **Expert highlight process** — human review before results delivery

**B2B Platform — "Powered by Tiny" (poweredbytiny.com):**
- **For Practitioners:** Advanced testing, free training on results interpretation, practitioner portal
- **For Health & Wellness Partners:** Turnkey co-branded testing, **API suite**, partner portal, volume discounts, customizations
- **For Researchers:** High-compliance collection kits, patented bioinformatics, affordable research-grade pricing
- **Partner logos shown:** Superpower, Mayo Clinic, "your brand" placeholder
- **Integrations:** Partner login (partner.tinyhealth.com), Practitioner login (practitioner.tinyhealth.com)

**Consumer-facing tech:**
- **Account portal:** account.tinyhealth.com (kit activation, results)
- **Store:** store.tinyhealth.com (Webflow + ecommerce)
- **Quiz funnel:** take-the-gut-health-quiz
- **Sample report:** interactive sample report via email capture

**GitHub:** github.com/TinyHealth — only 1 public repo (`fullstack-challenge`, a TypeScript hiring challenge, updated Oct 2025). No public SDKs, API docs, or open-source tooling visible.

**Website:** Built on **Webflow** (evident from CDN paths: `cdn.prod.website-files.com`). Blog, store, and marketing pages all Webflow.

---

## Team & Hiring Signals

**Leadership:**
- **Cheryl Sew Hoy** — Founder/CEO, mom of 3, serial entrepreneur
- **Donald Koo** — Co-founder, leads technology (joined 2 years in)
- **Kimberley Sukhum** — Chief Science Officer (joined 2021), leads scientific work
- **Dr. Elisa Song** — Chief Medical Officer, integrative pediatrician, Stanford/NYU/UCSF

**Hiring (from Series B letter + careers page):**
- Currently ~40 employees
- **Planning to hire 30 more** with Series B capital
- Priorities: expand work with healthcare providers & companies, fund research, clinician training
- Careers page: jobs.ashbyhq.com/tiny-health (JS-heavy, couldn't scrape roles)

**Engineering/Technical roles implied:**
- Bioinformatics pipeline (thMP/thDB/thDD/thMAP) maintenance & scaling
- API development for Powered by Tiny partner integrations
- TinyAI/ML development
- Consumer web/app experience (Webflow + custom account portal)
- Lab integration & data pipeline

---

## Competitive Landscape (from /technology comparison charts)

| Competitor | Technology | Price | Resolution | Key Gap |
|------------|-----------|-------|------------|---------|
| **Tiny Health** | Shotgun metagenomics | $249 | Strain-level, 120k+ microbes | — |
| **Viome** | mRNA/RNA (metatranscriptomics) | $279 | Species-level, no ref ranges | High variability, no long-term intervention evidence |
| **Floré** | Metagenomics | $299 | Species-level, no baby ref ranges | Smaller DB, upsells own supplements |
| **Jona** | Metagenomics | — | Species-level | — |
| **GI Map / GI Effects / Gut Zoomer** | qPCR | ~$400 | Limited to 30-80 probed microbes | Misses bigger picture, pathogen-focused |
| **Snapi / Ombre** | 16S amplicon | $99-129 | Family/genus level only | Low resolution, high false positives, bacteria only |

**Tiny Health wins on:** Strain-level resolution, largest microbe DB (120k+), mom/baby reference ranges, unbiased recs, expert consult included, CLIA/CAP lab.

---

## Gaps & Opportunities (Raw Signals)

1. **Developer Experience / API Documentation** — Powered by Tiny offers "API suite" and partner portal but **no public API docs, SDKs, or developer portal visible**. Partners (Superpower, Mayo, Fullscript) need integration guides. As B2B scales 4x YoY, this becomes critical.

2. **Bioinformatics Pipeline Documentation** — Proprietary pipeline (thMP, thDB, thDD, thMAP) is core IP but **no technical documentation visible** for internal onboarding, external collaborators, or researcher partners in the $5M Microbiome Research Program.

3. **TinyAI / ML Documentation** — Building "world's first AI trained on 200k microbiome profiles" — needs model cards, API docs, integration guides for practitioners/researchers.

4. **GitHub Presence** — Only a hiring challenge repo. No public SDKs, example integrations, or open-source tooling for partners/researchers.

5. **Support/Knowledge Base** — support.tinyhealth.com returns 403. FAQ lives on Webflow pages, not a structured docs site. No searchable technical knowledge base for practitioners or partners.

6. **Partner Onboarding** — "Turnkey co-branded solution with API suite" suggests partners need to integrate. No visible partner developer portal, authentication guides, webhook docs, or sandbox environment.

7. **Regulatory/Compliance Docs** — CLIA, CAP, HIPAA compliance mentioned but no technical compliance documentation for enterprise partners (BaaS agreements, data processing addenda, security questionnaires).

---

## Relevant Quotes (for Gap.md evidence trail)

> "We're also introducing TinyAI, the world's first AI trained on Tiny Health's proprietary dataset of nearly 200,000 microbiome profiles. TinyAI is designed to turn a person's microbiome results into personalized, science-backed guidance..." — Cheryl Sew Hoy, [Series B Letter](https://tinyhealth.com/blog/tiny-health-series-b-letter-from-cheryl-sew-hoy)

> "Powered by Tiny... Turnkey co-branded gut and vaginal microbiome testing solution with **API suite**, partner portal, and volume discounts. Further customizations available." — [Powered by Tiny](https://www.poweredbytiny.com/)

> "Our proprietary bioinformatics platform (eg thMP, thDB, thDD) allows us to create custom metrics and reports that pull in your survey data... Next it is run through thMAP to plot the right reference ranges. We then use machine learning to personalize the recommendations..." — [Technology page](https://tinyhealth.com/technology)

> "With this round, we're committing $5 million to the Tiny Health Microbiome Research Program to give researchers, clinicians and scientific partners access to our testing, data, **bioinformatics pipeline** and microbiome expertise." — Series B Letter

> "We want to lower those barriers, accelerate the pace of research and help generate more rigorous clinical data." — Nick Whitehead, B Capital (Series B Letter)

> Revenue more than doubled each year; **B2B arm ("Powered by Tiny") grew fourfold last year** — Series B Letter

---

## Sources Index

1. **Crunchbase News** — "Tiny Health Raises $33M To Explore What Gut Data Can Reveal About Future Health" (Sept 29, 2026) — https://news.crunchbase.com/venture/tiny-health-33m-microbiome-tests-sew-hoy/
2. **Tiny Health Blog** — "Celebrating Tiny Health's Series B: A Letter From Cheryl Sew Hoy" (Sept 29, 2026) — https://tinyhealth.com/blog/tiny-health-series-b-letter-from-cheryl-sew-hoy
3. **Tiny Health Technology Page** — https://tinyhealth.com/technology
4. **Powered by Tiny (B2B)** — https://www.poweredbytiny.com/
5. **Tiny Health Homepage** — https://tinyhealth.com/
6. **Tiny Health Blog Index** — https://tinyhealth.com/blog
7. **GitHub Org** — https://github.com/TinyHealth
8. **Careers** — https://jobs.ashbyhq.com/tiny-health (JS, limited scrape)

---

## Research Complete

All facts above are sourced from primary sources (company website, founder letter, Crunchbase News). No fabrication. Thin evidence areas noted in Gaps section.