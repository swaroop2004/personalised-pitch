# Feel Goods — Research Brief

**Company:** Feel Goods (feelgoods.co)  
**Slug:** feel-goods  
**Funding News:** $4.7M seed round, announced August 28, 2025 (Modern Retail)  
**Funding Source:** https://www.modernretail.co/operations/how-supplements-brand-feel-goods-raised-a-4-7-million-round-in-a-challenging-vc-landscape/  
**Lead Investor:** Cutting Horse  
**Other Investors:** Adapt VC, SuperAngel.Fund, Air Ventures, TA Ventures, OpenSky Ventures  
**Stage:** Seed (D2C, profitable growth)

---

## Company Overview

Feel Goods is a D2C supplements brand selling drink-mix remedies targeting gut health, hydration, immunity, and sleep. Launched early 2021 by co-founders **Brian Wong** (CEO) and **Dustin Pourbaba**, both former tech-industry professionals. Based in California.

**Product Lines (all "+" branded):**
- **Sleep+** — plant-powered gummies for sleep (newest launch, gummy format)
- **Hydration+** — daily electrolytes (1,100mg per serving) with organic fruit, trace minerals
- **Digestion+** — organic fiber, probiotics, enzymes for gut health/bloating
- **Immunity+** — advanced vitamin complex + organic adaptogens
- **The Full House** — bundle of all four (50+ core nutrients)

**Key Claims (from homepage):**
- 20M+ mixes sipped nationwide
- 1,000+ research publications on PubMed backing ingredients
- 40+ microbials/contaminants tested per batch (80+ benchmarks)
- 1,000+ clinicians support Feel Goods
- 4.8 stars from 4,000+ reviews
- Made in California, cGMP/NSF/FDA/QAI certified facility
- 100% natural, zero sugar, non-GMO, vegan, 3rd-party tested

---

## Business Model & Traction (from Modern Retail article + site)

- **Revenue:** "Eight-figure range" (i.e., $10M–$99M ARR), growing profitably
- **Units shipped:** 4M+ servings in 3 years
- **Channel:** DTC-only (Shopify), subscription-heavy (most orders recurring)
- **Social:** ~200K followers across platforms, 5M+ TikTok likes
- **Content strategy:** Shifted from paid ads to in-house TikTok content (~1 year ago)
- **Wholesale:** Live on Faire (40% off for retailers); targeting gym owners, pilates studios, chiropractors, doctors, mom-and-pop shops
- **Retail expansion:** Actively planning physical retail launch in early 2026; Walmart already reached out but they declined (not ready operationally)
- **Product roadmap:** Moving *out of powder mixes* into new formats (liquid or gummies) in 2026 — Sleep+ gummies are the first step

---

## Technical / Digital Surface Area

| Surface | Status | Notes |
|---------|--------|-------|
| **Shopify store** | Live | Custom theme, bundles (build-your-own), subscription management (likely Recharge) |
| **Health Quiz** | Live | `/pages/health-quiz` — 90-second questionnaire matching users to products |
| **Wholesale portal** | Live | Powered by Faire (replo-based landing page at `/pages/wholesale-lander`) |
| **Blog/CMS** | Live | Shopify blog at `/blogs/all` — educational content by category (Digestion, Hydration, Immunity) |
| **Email/SMS** | Implied | Klaviyo/Attentive typical for DTC at this scale |
| **Developer/API docs** | **Absent** | No public API, no developer portal, no integration docs for wholesale partners |
| **Technical documentation** | **Absent** | No onboarding guides for wholesale partners, no API reference, no webhook docs |

---

## Team & Hiring Signals

- Co-founders: Brian Wong (CEO), Dustin Pourbaba (co-founder)
- Advisors: Dr. Tanja Johnston (Harvard MD, PhD Natural Health), Paula Simpson (homeopathic expert)
- **No public careers page** — no open roles visible on site
- Modern Retail article notes: "We don't have the team, capital or operations built out for a launch that big [Walmart]" — explicit admission of operational/team gap for retail scaling

---

## Funding Context & Stated Priorities (per Modern Retail)

1. **Leverage new investors to plan/execute physical retail strategy** — "start rolling out in retail in early 2026"
2. **Change product formats** — "Next year, we're actually going out of powder mixes and moving into new formats" (liquid/gummies)
3. **Build wholesale operations** — currently on Faire only, no dedicated B2B portal or partner onboarding infrastructure
4. **Content/TikTok** — continue in-house content production as primary acquisition channel

---

## Competitive Landscape Notes

- Crowded "better-for-you functional powders/beverages" category (per Mike Duda, Bullish)
- Investors skeptical: "there are a bunch that are treading water or doing just OK"
- Differentiation: "Kool-Aid-esque supplement" branding — humorous, provocative, approachable vs. clinical/serious competitors
- Subscription-heavy model is a strength in consumables category

---

## Evidence Trail (Direct Quotes)

> "We got a ton of 'nos' [from investors]... many investors passed on Feel Goods because they're looking for established omnichannel businesses, ones ideally already selling at big-box retailers like Target and Walmart." — Brian Wong, Modern Retail

> "We had Walmart reach out to us, but we don't have the team, capital or operations built out for a launch that big... And you only get one shot at retail." — Brian Wong

> "Feel Goods plans to leverage some of its new investors to plan and execute a physical retail strategy. The company plans to start rolling out in retail in early 2026." — Modern Retail

> "Next year, we're actually going out of powder mixes and moving into new formats... The company is considering a light liquid or gummies for its next line." — Brian Wong

> "Now we do a lot of it ourselves in-house, and TikTok has been a huge driver of awareness and revenue." — Brian Wong

> "It's really hard to do DTC right now unless you're a repeat-heavy consumable product. Supplements happen to be one of these categories." — Brian Wong

---

## Gaps Identified (Preliminary)

1. **Wholesale/Retail Technical Infrastructure** — No developer documentation, partner onboarding guides, API specs, or integration docs for the coming retail/wholesale push. Faire is a marketplace, not a dedicated B2B portal.
2. **Health Quiz as Embeddable Service** — The quiz is a key conversion tool but lives only on their site. No API/embed docs for partners (retailers, clinics, gyms) to integrate it.
3. **Subscription Platform Docs** — Managing 4M+ servings via subscription implies complex recurring logic; no technical docs for internal team or external partners.
4. **Content/DevRel Scale** — In-house TikTok production is working but unsystematized; no documented content operations playbook.
5. **Product Format Transition** — Moving to gummies/liquid requires new manufacturing docs, QC specs, regulatory documentation — currently undocumented.

---

## Sources

1. Modern Retail: "How supplements brand Feel Goods raised a $4.7 million round..." — Aug 28, 2025
2. feelgoods.co homepage, /pages/about, /pages/our-process, /pages/wholesale-lander, /blogs/all, /pages/health-quiz — fetched Nov 17, 2026
3. Faire wholesale landing page (replo cdn assets) — referenced from wholesale-lander page