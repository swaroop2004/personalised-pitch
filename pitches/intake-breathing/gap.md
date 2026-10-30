# Gap Analysis: Intake Breathing → Manicule

**Target:** Intake Breathing (DTC nasal wellness, $62M Series A, scaling to retail + B2B)  
**Us:** Manicule — AI-native technical documentation studio for developer tools  

---

## Candidate Gaps (Scored)

| Gap | Evidence Strength | Fit with Manicule | Urgency | Score |
|-----|-------------------|-------------------|---------|-------|
| **No developer docs for B2B/partner platform** (intakepartners.com, dental.*, hospitality.*) | High — 4+ subdomains, no public API docs, no integration guides | High — Manicule's core offering | High — retail/B2B scaling funded | **9/10** |
| Help center (Gorgias) is consumer-facing only; no partner/developer knowledge base | High — observed | Medium — adjacent to our skillset | Medium | 6/10 |
| No technical content for provider onboarding (317 medical, 123 fitness) | High — provider network exists, no technical onboarding observed | Medium — we do "video/screenshot production" + docs | Medium | 6/10 |
| No engineering blog/changelog for a brand claiming "patented technology" | Medium — patents page exists but no technical depth | Low — not our core | Low | 4/10 |
| Shopify theme-only architecture; no headless/composable docs for future retail APIs | Medium — inferred from "Powered by Shopify" | Medium — we do API/SDK docs | Medium | 5/10 |

---

## Primary Gap: **Zero Developer Documentation for a Nascent B2B Platform**

### The Evidence Trail (Their Own Words)

> **"We're preparing our operations, product lineup and supply chain for the order sizes that come with mass retail, and working on smart retail partnerships that put Intake in front of people beyond the drugstore cold-and-flu aisle."**  
> — Alex Hauck, CEO, *Intake Breathing Raises $62M* blog post (Oct 29, 2026)

> **"Camino works hands-on with the founders it backs on strategy, operations and growth... Its portfolio includes consumer brands like CAVA, Prose and Barry's, and it focuses on companies that are enhancing people's everyday lives, with a growing emphasis on health and longevity."**  
> — Intake funding blog (describing their new investor's operating model)

> **"74% of Intake consumers have not been legacy category consumers."**  
> — Elle Lanning, President, Camino Partners, *Modern Retail* (Oct 28, 2026)

> **"We're bringing on experienced operators across marketing, product and operations, people who have scaled consumer brands before."**  
> — Alex Hauck, funding blog

### The Gap, Plainly Stated

Intake is **a consumer brand becoming a platform**. They operate:
- `intakepartners.com` — wholesale/B2B portal
- `dental.intakebreathing.com` — dental provider portal  
- `hospitality.intakepartners.com` — hospitality portal
- `app.intakeb2b.com` — corporate gifting
- `gifts.intakepartners.com` — bulk gifting

**None of these have:** public API documentation, integration guides, webhook specs, authentication docs, SDKs, or a developer portal. Their only "docs" are a consumer-facing Gorgias help center (returns, sizing, shipping).

As they onboard 317+ medical providers and 123+ fitness locations — and prepare for mass retail APIs (EDI, catalog sync, inventory feeds) — **they have no technical documentation layer.**

---

## Our Fix: Manicule Builds Their Developer Documentation Layer

### What We Deliver
| Deliverable | Manicule Capability | Proof Point |
|-------------|---------------------|-------------|
| **API Reference Docs** (OpenAPI/Spec-driven) | New docs from scratch; code verification of every sample | Supermemory: +30% answer success rate, 23-day turnaround |
| **Partner Integration Guides** (dental, fitness, hospitality) | Restructure + ongoing maintenance; video/screenshot production | DevRel: 1M+ SEO impressions, 90% traffic growth |
| **Developer Portal** (unified: auth, quickstarts, SDKs) | Architecture + writing + creative direction | Philosophy: "Navigation > Writing" — structure beats prose |
| **Changelog / Release Notes** (for platform updates) | Ongoing maintenance; AI agents audit at scale | Clients: Supermemory, Greptile, Reducto, Rootly, PromptLayer |
| **Provider Onboarding Technical Content** | "Docs are marketing" — turn technical onboarding into a product feature | Supermemory: multiple enterprise deals closed via docs |

### Why This Fits *Us* (Manicule)

1. **We do developer tools docs** — Intake's B2B portals *are* becoming developer tools (APIs for retail partners, provider integrations, webhook feeds).
2. **We ship fast with AI + human review** — 23-day turnaround for complete rewrites (Supermemory). Intake needs this *now* with $62M burning.
3. **We treat docs as a product feature** — "Navigation > Writing" aligns with Intake's design-first brand (magnetic band, sweat-proof tabs, NY Fashion Week).
4. **We verify every code sample** — Critical for retail APIs (EDI, inventory, catalog) where broken integrations = lost POs.

---

## Specific Proof Point from Profile.md

> **Supermemory:** +30% answer success rate, multiple enterprise deals, 23-day turnaround.  
> **DevRel:** 1M+ SEO impressions, 90% traffic growth in 3 months, #1–#2 rankings on competitive queries.

**Applied to Intake:** We build their developer portal → their retail partners integrate faster → fewer support tickets → faster retail onboarding → Camino's "smart retail partnerships" actually ship.

---

## Pitch Angle (One Sentence)

> **Intake is turning a nasal dilator into a breathing platform — but the platform has no developer docs. We build them.**

---

## Call to Action (from Profile)

**Free teardown/audit of their developer-facing surfaces** — 30-minute call to walk through findings.  
Contact: `swaroop@manicule.dev` / `founders@manicule.dev`