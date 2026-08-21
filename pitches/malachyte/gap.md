# Malachyte — Gap Analysis

**Primary Gap:** **Developer documentation for their Vector AI platform is thin relative to the technical complexity of integration** — and they're actively scaling distribution to Shopify developers and enterprise API consumers.

---

## Evidence Trail (their own words)

| Signal | Source | Quote |
|--------|--------|-------|
| **Complex integration surface** | `/technology` + Google Cloud blog | "Visual transformer technology eliminates the need for manual tagging" — but Shopify Theme App Extension + headless API + CDP/CRM connectors + Intelligems A/B = 4+ integration paths |
| **Developer-facing product** | `docs.malachyte.com` | Public docs: Overview, Shopify install, Headless, Recommend, Search, Pages — **no API reference, no SDK docs, no webhook specs, no error codes** |
| **Hiring signal** | `/careers` | Only open role: **Senior Data/Backend Engineer** — building the core infra that developers integrate *against* |
| **Distribution push** | Pilot page + blog | "GA June 2026 for Shopify merchants" + 21-day pilot program = actively onboarding Shopify devs *now* |
| **Enterprise motion** | Homepage logos + case studies | Mercado Libre, Simon = enterprise API integrations needing deeper technical docs |
| **Competitive pressure** | `/competitive-comparison/rebuy` | Rebuy has 19/36 capabilities live; Malachyte 28/36 — but Rebuy has **years of developer mindshare and docs** |

---

## The Gap in One Sentence

Malachyte has built a **genuinely novel real-time ML platform** (Vector AI, 100ms updates, Bigtable+Kafka, visual transformers) but their **public developer documentation is a "getting started" brochure, not a technical reference** — exactly when they're opening the floodgates to Shopify developers and enterprise API consumers.

---

## Why This Gap Hurts Them *Now*

1. **Shopify GA = developer onboarding at scale** — Every new merchant install is a developer (agency or in-house) reading `docs.malachyte.com/get-started/shopify/overview`. If they hit a wall, pilot stalls.
2. **Enterprise deals need technical due diligence** — Mercado Libre / Simon-class buyers demand API specs, SLA docs, webhook contracts, error taxonomies *before* legal signs.
3. **Competitive displacement requires migration docs** — Comparison pages target Rebuy/Nosto/Dynamic Yield users — but **no "Switching from Rebuy" guide exists**.
4. **Their own content strategy proves the need** — They publish deep technical blogs (Google Cloud architecture, Vector AI math) but **don't connect that depth to the developer docs**.
5. **AI-era expectation** — Developers expect AI-verified code samples, interactive playgrounds, auto-generated SDKs. Malachyte's docs have none of this.

---

## Our Fix (per Manicule profile)

**We are an AI-native technical documentation studio for developer tools.**  
We write, restructure, and maintain docs — AI agents audit and test every code sample at scale; humans do architecture, writing, creative direction.

### Specific Deliverables We'd Build

| Deliverable | Why It Matters for Malachyte |
|-------------|------------------------------|
| **Complete API Reference** (OpenAPI → generated + human-curated) | Enterprise buyers require it; Shopify app devs need it for headless builds |
| **SDK / Client Library Docs** (TypeScript, Python, Ruby) | "Visual transformer eliminates manual tagging" — but devs need typed clients to *use* it |
| **Verified Code Samples** (AI-tested against live API) | Every sample in Shopify install guide, headless guide, webhook handler — actually runs |
| **Migration Guides** (Rebuy → Malachyte, Nosto → Malachyte) | Turns competitive comparison pages into conversion tools |
| **Troubleshooting / Debugging Guide** | 100ms latency budget means devs *will* hit edge cases; need self-serve debug paths |
| **Architecture Decision Records** (ADRs) for integrators | "Why Bigtable? Why Kafka? How to size?" — reduces support load, builds trust |

---

## Proof Point from Profile

> **Supermemory:** +30% answer success rate, multiple enterprise deals, **23-day turnaround**  
> **DevRel:** 1M+ SEO impressions, 90% traffic growth in 3 months, #1–#2 rankings on competitive queries

We've done this for **developer-tool companies at similar stage** (Supermemory, Greptile, Reducto, Rootly, PromptLayer — all AI/ML devtools, seed-to-A). Malachyte is the same profile: technical product, developer audience, scaling distribution post-seed.

---

## Pitch Angle

**"You've built the best real-time ML infrastructure in commerce. Your docs should be as good as your vectors."**

- Open with: *I was reading your Google Cloud blog post about the 100ms Vector AI loop…*
- Gap: *But when a Shopify dev tries to go headless, or an enterprise architect does technical due diligence, the docs stop at "Overview."*
- Fix: *We'll build the API reference, verified SDK samples, migration guides, and debugging playbook — AI-tested, shipping in 23 days.*
- CTA: *Free teardown of your current docs — 30-minute call, we walk through exactly what's missing and what it costs to fix.*

---

## Alternative Gaps Considered (rejected)

| Gap | Why Rejected |
|-----|--------------|
| Merchandiser enablement/training | Not our domain (we're dev docs, not retail ops) |
| Post-purchase retention loops | Product gap, not docs gap |
| Multi-store management | Product gap; no evidence they're building it yet |
| Observability dashboard | Product gap; they may have internal tools not public |

---

## Confidence Score

**9/10** — Gap is evidenced by *their own public artifacts* (docs site, hiring, GA timing, competitive pages), aligns *exactly* with our proven offering, and is *urgent* given their distribution push.