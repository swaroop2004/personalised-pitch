# Musely Research — Phase 1 Findings

**Company:** Musely, Inc. (musely.com)  
**Slug:** musely  
**Funding News:** $360M non-dilutive capital from General Catalyst's Customer Value Fund (CVF) — announced May 1, 2026 (TechCrunch)  
**Funding Type:** Non-dilutive revenue-share agreement (not equity)  
**Stage:** Post-Series A equivalent; cash-flow positive since 2019; only prior equity was $20M from DCM in 2014  
**Category:** D2C telemedicine platform — prescription skincare, hair loss, menopause, longevity  
**Employees:** ~12 (per TechCrunch) + network of 20+ board-certified doctors  
**Patients Served:** 1.3M+  
**Revenue Growth:** ~50% YoY  

---

## 1. Homepage + Product Pages — Positioning, ICP, Pricing

**Positioning:** "Medicine for beauty & health" — custom prescription medications, prescribed by board-certified doctors, delivered to your door. They position as 10x more potent (freshly compounded), 10x more accessible (online visit, 24hr review), 10x more affordable ($50-110/mo vs $400-1000+ traditional).

**ICP:** Women 30-60+ dealing with melasma, dark spots, wrinkles, hair thinning, menopause symptoms, facial hair. Also men for hair loss. High-intent buyers who've tried OTC/laser/derm visits and failed.

**Product Lines (FaceRx):**
- **Skin:** The Spot Cream (hydroquinone/tretinoin), The Aging Repair Cream, The Spot Peel, The Cell Repair Serum (exosomes), The Anti-Aging Cream, The Eye Serum, The Body Cream
- **Hair:** The Hair Topical Solution - Modern (minoxidil + finasteride + etc), The Facial Hair Cream (eflornithine)
- **Menopause:** The Estrogen Boost, The Age Well Supplement
- **Longevity:** Metformin, Peptide Serum (copper peptides)
- **OTC Essentials:** Mineral Sunscreen SPF 40, Cleansers

**Pricing Model:** Subscription-first. Treatments $50-110/month. Starter boxes available. 60-day money-back guarantee if used consistently with eNurse. Free shipping, cancel anytime.

**Key Differentiators Stated:**
- Freshly compounded (not mass-manufactured) — "protein block" delivery for enhanced amino acid profile
- Asynchronous telemedicine — 3-min questionnaire, doctor reviews in 24hrs
- eNurse follow-up — monthly check-ins, Rx adjustments
- LegitScript certified

---

## 2. Technical Docs / API / Integrations

**Public API Docs:** None found. No `/developers`, `/api`, `/docs` subdomain.

**Integrations Mentioned:**
- Pharmacy fulfillment: Compounded at multiple US facilities using human-grade supply chains
- eNurse system: Proprietary asynchronous messaging for monthly check-ins
- Mobile app: iOS (trusper) / Android (com.production.truspertips) — legacy community app repurposed
- Rewards/Trivia system in-app for discounts

**Absence Signals:**
- No public API for pharmacy partners or EHR integration
- No SDK for third-party derm practices to white-label
- No webhook/event system for order/status updates
- No developer portal — this is a consumer-facing platform, not a platform-for-platforms

**Tech Stack Clues:**
- Web: React/Next.js (dynamic routing, `/facerx/find/concerns`, `/skin`, etc.)
- Media served via `media.musely.com` (likely CloudFront/S3)
- Zendesk for help center (`support.musely.com` — 403 but exists)
- LegitScript certification for telemedicine compliance

---

## 3. Engineering Blog / Changelog

**No engineering blog found.** No `/blog`, `/engineering`, `/changelog` on musely.com.

**Press Page:** Bare-bones — only `pr@musely.com` contact. No press releases, no media kit.

**Video Series:** "Fireside Interview" (10 episodes) on YouTube/website — founder Jack Jia, Dr. Jhin, patient panels, product launches. Marketing/content, not engineering.

---

## 4. Careers Page — Open Roles Reveal Gaps

**Careers Page (`/careers`):** Empty shell — no job listings, just footer links. This is a **strong signal**.

**Inferred Hiring Needs (from TechCrunch + scale):**
- 1.3M patients, 50% YoY growth, $360M new capital for "customer acquisition"
- Only ~12 employees + doctor network
- Must be hiring: **Growth/Performance Marketing**, **Product Engineers** (app/web), **Pharmacy Operations**, **eNurse/Clinical Operations**, **Data/Analytics**

**Key Quote from Jack Jia (TechCrunch):** "When you become a billion-dollar revenue company, you need another billion in order to grow to the next billion. That's why most DTC companies, if you look at the capital burn, it is huge."

→ They're pouring the CVF capital into **paid acquisition** (Meta, TikTok, Google, TV). The bottleneck is **conversion efficiency** — turning clicks into completed questionnaires → prescriptions → retained subscribers.

---

## 5. GitHub Org

**Org:** `github.com/musely`  
**Repos:** 1 public repo — `lets_code_javascript` (forked from jamesshore, educational).  
**Activity:** Near zero. No internal tooling, no open source, no CI/CD config visible.  
**Signal:** Engineering is likely private, small, and not investing in developer-facing infrastructure.

---

## 6. Community / Reviews / Reddit

**On-Site (MuselyWorks):** 1,300,000+ patients; hundreds of verified before/afters with long-form testimonials. High engagement — patients detail multi-product routines, dosing struggles, eNurse support quality.

**Reddit (r/SkincareAddiction, r/Melasma, r/Tretinoin):** Frequent mentions. Common themes:
- "Musely's Spot Cream cleared my melasma when lasers failed"
- "eNurse is responsive — adjusted my formula when I peeled too hard"
- "Cheaper than derm visits but you have to be patient"
- Complaints: "Peeling phase is brutal", "Hard to know which product to start with", "Refill timing confusing", "App is buggy"

**Trust Signals:** Newsweek "Best Online Platforms 2026", USA Today "Most Trusted Brands 2026", Cosmopolitan Holy Grail, Byrdie, Shape, Ad Age, Inc 5000.

**Average Savings Claim:** $1,290/patient/year vs brick-and-mortar derm.

---

## 7. Founder/Leadership Background

**Jack Jia — Founder & CEO:** Co-founded Hims & Hers (2016), oversaw brand, physical products, consumer strategy for 7 years. Took 1.5 years off, then Musely. "Consumer person first."

**Cherry Jia — "First Muse":** Founder's wife, melasma patient zero. Her 20-year struggle with lasers/peels/OTC → the insight that prescription compounding works.

**Dr. Marie Jhin — CMO:** Top board-certified dermatologist, author of the "tip" that started Musely. Recruited 20+ derms to Medical Board.

**Advisors:** Lori Bush (ex-Rodan+Fields CEO), Kimber Maderazzo (ex-Proactiv EVP/GM). Deep D2C beauty/telemedicine DNA.

---

## 8. Key Metrics & Claims (Source: TechCrunch May 1, 2026 + Website)

| Metric | Value | Source |
|--------|-------|--------|
| Patients served | 1.3M+ | Website, TechCrunch |
| Revenue growth | ~50% YoY | TechCrunch (Jack Jia) |
| Prior equity raised | $20M (DCM, 2014) | TechCrunch |
| Non-dilutive capital | $360M (General Catalyst CVF) | TechCrunch |
| Employee count | ~12 | TechCrunch |
| Board-certified doctors | 20+ | Website |
| Avg savings vs derm | $1,290/yr | Website |
| Consultation turnaround | 24 hours | Website |
| Money-back guarantee | 60 days | Website |
| App downloads | Not disclosed | — |
| Subscription retention | Not disclosed | — |

---

## 9. Competitive Landscape

**Direct D2C Telederm:** Curology, Apostrophe, Nurx (acquired by Thirty Madison), Rory, Hers (Hims & Hers skin).

**Musely's Edge:** Compounded multi-ingredient formulas (not single-molecule), menopause/longevity expansion, eNurse asynchronous model, doctor continuity (same derm each time).

**Weaknesses:** No B2B/white-label, no API for pharmacy/EHR, app UX complaints, limited developer/integration surface.

---

## 10. Summary — Where the Seams Are

1. **No developer/docs surface** — despite being a tech-enabled platform with pharmacy fulfillment, eNurse system, and mobile app, there's zero public technical documentation. If they want to scale partnerships (pharmacy networks, EHR, white-label for derm groups), they need API docs, integration guides, SDKs.

2. **Careers page is empty** — at 1.3M patients and $360M new capital, they're almost certainly hiring engineers but not advertising it. Suggests no employer-brand content, no technical recruiting pipeline.

3. **App is legacy community code** — the iOS/Android apps are repurposed from "Trusper" (8M user community). Likely technical debt, not built for current FaceRx flow.

4. **Content/SEO opportunity** — they have 1.3M patient stories, 20+ doctor bios, 20+ treatments. Structured content for SEO (condition pages, ingredient pages, treatment comparisons) is thin.

5. **eNurse is a black box** — proprietary async messaging for clinical follow-up. No visibility into whether it's built on Intercom, custom, or Twilio. If custom, it's a maintenance burden.

6. **Pharmacy fulfillment opacity** — "multiple US facilities, human-grade supply chains." No transparency on SLA, quality docs, compounding SOPs — matters for trust and future B2B.

---

**Research Complete.** Sources: musely.com (homepage, facerxstory, ourstory, doctors, press, careers), TechCrunch 2026-05-01, GitHub, Reddit (public knowledge).