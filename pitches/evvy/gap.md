# Evvy — Gap Analysis

## Candidate Gaps (from research + profile.md)

| Gap | Evidence Strength | Fit with Manicule | Urgency | Notes |
|-----|-------------------|-------------------|---------|-------|
| **Provider Portal API docs & integration guides** | High — 3,000+ clinicians, active IVF study with 10+ clinics, Labcorp partnership, EHR integration needs | High — Manicule specializes in developer tool docs, API reference, integration guides | High — $40M Series B scaling, B2B provider growth | Strongest fit |
| **Public developer portal / API reference** | Medium — no visible `/docs`, `/developers`, `/api` routes; provider portal exists but no public dev docs | High — core Manicule offering | Medium — needed as partnerships scale | Greenfield opportunity |
| **EvvyAI developer documentation** | Medium — launched May 2026; AI assistant for patients + clinicians | Medium — Manicule does AI/dev tool docs | Medium — new feature, needs docs | Niche but credible |
| **Clinical decision support integration docs** | Medium — "200+ clinical data fields" + molecular results → treatment prediction | Medium — involves API + clinical workflow docs | Medium — core IP, may be internal | Requires clinical domain knowledge |
| **Patient portal / mobile app API docs** | Low-Medium — portal exists at my.evvy.com/login; subscription mgmt, results tracking | Low-Medium — consumer-facing, less dev-tool-like | Low — lower priority for B2B scaling | |
| **Content/SEO technical documentation** | Low — 200+ blog articles, strong SEO; but not "technical documentation" | Low — Manicule does DevRel/SEO but for dev tools | Low — not core gap | |

---

## Selected Primary Gap: **Provider Portal API Documentation & Integration Guides**

### The Gap (in their words)

> "Evvy provides women and people with vaginas access to data-driven insights on their own bodies, while finally pioneering the research to improve diagnostics and treatments for underserved conditions in the female body." — About page

> "Trusted by over 100,000 patients and 3,000 clinicians... Through our platform, Evvy has also built the world's largest vaginal microbiome dataset — a proprietary asset unlocking more accurate diagnoses, targeted treatments, and improved outcomes at scale." — Provider page

> "Our peer-reviewed study on >1k patients shows significant outcome improvements across symptom resolution, microbiome restoration, and recurrence rates — even though Evvy often sees the most complex patients." — Provider page

> "We provide pharmacy services (ability to order and fulfill targeted Rx) and coaching through our provider and patient platform." — Provider page

> "Landmark Study Uncovering the Role of the Vaginal Microbiome in IVF Outcomes... Designed with leading fertility doctors including Dr. David Sable, Dr. Peter Klatsky, & Dr. Eduardo Hariton." — Science page

**Translation:** Evvy is rapidly scaling a B2B provider platform (3,000+ clinicians, 10+ fertility clinic partners in active IVF study, Labcorp partnership, pharmacy fulfillment network). This platform *requires* robust API documentation, integration guides, and a developer portal for:
- EHR/EMR integrations (Epic, Cerner, Athena, fertility-specific EMRs)
- Lab system integrations (Labcorp, other reference labs)
- Pharmacy/fulfillment APIs
- Fertility clinic data exchange for the IVF study
- Future partner onboarding (health systems, telehealth platforms)

**No public developer documentation exists today.** The provider portal (`my.evvy.com/provider`) is a gated clinical tool, but the *integration layer* that lets health systems, labs, and fertility clinics connect programmatically is undocumented — or documented only in private PDFs/Notion pages that don't scale.

---

### Our Fix (from profile.md)

**Manicule delivers:** AI-native technical documentation studio for developer tools.
- New docs from scratch, complete rewrites, ongoing maintenance
- **Code verification and testing of every sample in the docs**
- **Video/screenshot production** (integration walkthroughs)
- **DevRel strategy and execution (SEO, social, content)** — drive partner adoption

**Philosophy match:** "Navigation > Writing" — structure beats prose. Provider integration docs need clear navigation: authentication → endpoints → webhooks → error handling → testing sandbox. "Docs are marketing" — great integration docs *are* the partner onboarding experience.

**Proof point:** Supermemory engagement — **+30% answer success rate**, multiple enterprise deals closed, **23-day turnaround**. DevRel: **1M+ SEO impressions, 90% traffic growth in 3 months, #1–#2 rankings** on competitive queries.

**CTA alignment:** Free teardown/audit of their provider API docs — 30-minute call to walk through findings. Contact: swaroop@manicule.dev / founders@manicule.dev

---

## Why This Gap Wins

1. **Revenue-critical:** Provider partnerships drive test volume (B2B → B2C flywheel). Poor integration docs = slower partner onboarding = lost revenue.
2. **Series B scaling signal:** $40M raise explicitly for "further women's health research" and scaling care platform. Provider network expansion is a stated priority.
3. **Competitive moat:** First-mover in vaginal microbiome testing. Developer experience for partners becomes a switching cost.
4. **Manicule credibility:** We document developer tools and APIs daily. Provider portal *is* a developer tool for health tech integrators.
5. **Audible personalization in 5 seconds:** "I saw your Series B announcement — congratulations. I was reading about the IVF study with Dr. Sable and Dr. Klatsky..." — specific, recent, credible.