# Evvy — Research Findings

**Company:** Evvy (evvy.com)
**Funding:** $40M Series B (Sep 15, 2026) led by Catalio Capital Management; $60M+ total raised
**Stage:** Series B (seed through Series C per criteria)
**Slug:** evvy
**Source URL:** https://techcrunch.com/2026/09/15/evvy-raises-40m-as-it-seeks-to-further-womens-health-research-with-vaginal-microbiome-data/

---

## Company Overview

Evvy is a women's health D2C company offering at-home vaginal microbiome testing and precision clinical care. Founded in 2021 by Priyanka Jain (CEO), Laine Bruzek (CMO), and Pita Navarro (CSO). Mission: "Close the gender health gap by leveraging overlooked female biomarkers, starting with the vaginal microbiome."

**Core Products (D2C):**
- **Evvy Vaginal Health Test** — $159 one-time / $129 subscribe & save. At-home mNGS test, CLIA/CAP/CLEP certified, screens 700+ bacteria & fungi. Results in <7 days.
- **UTI+ Test** — $248. PCR-based pathogen + resistance gene identification.
- **Women's Complete Probiotic** — $55. 3-in-1 gut, urinary, vaginal support.
- **Vaginal Probiotic Suppositories** — $59. Rx-icon flagged (clinician-prescribed).
- **Pure Boric Acid Suppositories** — $39. Rx-icon flagged.
- **Hyaluronic Acid Suppositories** — $59. Rx-icon flagged.

**Business Model:** D2C subscription + one-time test sales + clinician-reviewed results + prescription fulfillment via affiliated providers + provider portal for B2B clinician partnerships.

---

## Key Metrics (from website + TechCrunch)

- **100,000+ patients** served across US
- **3,000+ clinicians** on platform
- **15+ peer-reviewed publications** and abstracts
- **World's largest vaginal microbiome dataset** (proprietary asset)
- **75% symptom resolution** in peer-reviewed study (>1,000 patients)
- **50% reduction in BV recurrence** vs standard of care
- **60% increase in protective bacteria**
- **98% sensitivity / 99% specificity** (CLEP analytical validation)
- **<7 day turnaround** for mNGS results; 1-3 days for PCR add-on
- **$40M Series B** (Sep 15, 2026) at undisclosed valuation; Catalio Capital led
- **Total funding $60M+** from General Catalyst, Left Lane, US Fertility, Catalio, Labcorp Venture Fund, G9, BBGV, Box Group, Foreground Capital, Amboy St. Ventures, Human Ventures, Virtue, Ingeborg, Rethink Impact, Muse Capital, others

---

## Product & Technical Architecture

**Testing Platform:**
- Metagenomic sequencing (mNGS) with proprietary vaginal-specific wet-lab protocols and bioinformatics algorithms
- Validated LDT, CLIA-certified, NYS CLEP approved, approved in all 50 states
- Test methodology published in *Diagnostics* (Thomas-White et al., 2024)
- Patient outcomes study published in *Microorganisms* (Thomas-White et al., 2025)

**Clinical Care Platform:**
- Combines molecular results with 200+ clinical data fields
- Predicts personalized treatment programs (vaginal antibiotics, probiotics, estradiol, hyaluronic acid, etc.)
- Pharmacy services: ordering, compounding, delivery of targeted Rx
- Coaching through provider/patient platform
- **EvvyAI** — AI assistant translating microbiome data into real-time guidance; directs to clinicians for expert questions

**Provider Portal (B2B):**
- Bulk/individual test ordering for patients
- Payment options: upfront or upon activation
- Results sent to both patient and provider with clear interpretation
- Access to custom compounded formulations
- Integration with fertility clinics (ongoing IVF outcomes study with US Fertility, Spring Fertility, RMA of NY, PositivIVF, etc.)
- Trusted by 3,000+ clinicians

**Fertility Expansion (active):**
- Landmark prospective study on vaginal microbiome role in IVF outcomes
- Fertility Insights in test results: Protective Score, Diversity Score, Fertility Disruptors, STI Status
- Fertility Advisory Board: 20+ REIs from CCRM, Kindbody, Inception, Spring Fertility, Northwestern, Stanford, etc.

---

## Content & Marketing

**#AskEvvy Blog:** 200+ "shame-free, science-backed articles" across categories: Vaginal Microbiome 101, Vaginal & Hormonal Health, Sex & Relationships, Fertility & Pregnancy, Menopause, Stories & Culture, Company News.

**SEO/Content Strategy:** Comparison articles (Evvy vs Daye, Wisp, MicroGenDX, AZO, Acon Labs, Fertilysis, UTI strips), symptom-focused content, educational guides. Strong long-tail SEO presence.

**Social Proof:** Vogue, TechCrunch, Fast Company, Inc. logos on homepage. 100k+ users, 5-star reviews featured.

**Equal Research Day** initiative + book on gender health gap.

---

## Technical / Developer Surface (Gap Opportunities)

1. **Provider Portal API / Integration Layer** — Portal at `my.evvy.com/provider` handles test ordering, results delivery, Rx fulfillment. Likely needs / has APIs for:
   - EHR integrations (Epic, Cerner, Athena, etc.)
   - Lab system integrations (Labcorp partnership noted)
   - Pharmacy/fulfillment integrations
   - Fertility clinic EMR integrations (active IVF study with 10+ clinics)

2. **Partner / Lab Integration Docs** — Labcorp Venture Fund investor; Labcorp logo on homepage. Lab integration documentation likely needed.

3. **EvvyAI / AI Features Documentation** — New AI assistant launched May 2026. Developer-facing docs for AI capabilities, API access, prompt engineering for clinical use cases.

4. **Patient Portal / Consumer App** — `my.evvy.com/login` — results tracking, subscription management, quiz, progress tracking. May need API docs for mobile app or third-party integrations.

5. **Developer Portal / Public API Docs** — No visible public developer portal (`/developers`, `/docs`, `/api` not found in nav). This is a gap.

6. **Clinical Decision Support Integration** — "200+ clinical data fields" combined with molecular results → treatment prediction. This logic likely exposed via API for partner clinical tools.

---

## Competitors / Comparables (from blog comparison posts)

- **Daye** — at-home vaginal microbiome test (tampon-based collection)
- **Wisp** — telehealth + prescription delivery for vaginal health
- **MicroGenDX** — NGS testing for chronic infections
- **Tiny Health** — gut/vaginal microbiome testing (baby/mom focus)
- **Juno Bio** — vaginal microbiome test
- **AZO / Acon Labs / UTI strips** — OTC dipstick screening (lower accuracy)
- **Fertilysis** — fertility-focused microbiome testing

---

## Open Roles / Hiring Signals (from /careers)

Careers page states: "Based in NYC... open to remote work for the right candidate." No specific roles listed in rendered HTML (likely loaded via JS). Page emphasizes: "unique opportunity to get in on the ground floor... building our team in NYC." Company has "deep experience building science-based products, companies, and teams... AI and healthcare startups that have raised over $130M+ in funding."

---

## Recent News & Momentum

- **Sep 15, 2026:** $40M Series B (TechCrunch)
- **May 2026:** EvvyAI assistant launched
- **Apr 2025:** Landmark IVF microbiome study launched with leading fertility clinics (Business Wire)
- **2024-2025:** Multiple presentations at ACOG, ASRM, IDSOG, ISSVD, ISSWSH
- **2025:** Peer-reviewed publications in *Nature Communications*, *Diagnostics*, *Microorganisms*, *mSystems*, *AJOG*, *Fertility & Sterility*
- **Fast Company:** Most Innovative Companies 2024

---

## Source URLs

1. TechCrunch funding announcement: https://techcrunch.com/2026/09/15/evvy-raises-40m-as-it-seeks-to-further-womens-health-research-with-vaginal-microbiome-data/
2. Homepage: https://www.evvy.com/
3. About: https://www.evvy.com/about
4. Science: https://www.evvy.com/science
5. Careers: https://www.evvy.com/careers
6. Blog (#AskEvvy): https://www.evvy.com/ask
7. Provider Portal: https://www.evvy.com/provider
8. Vaginal Health Test product: https://www.evvy.com/vaginal-microbiome-test
9. Women's Complete Probiotic: https://www.evvy.com/womens-complete-probiotic
10. UTI+ Test: https://www.evvy.com/uti-test