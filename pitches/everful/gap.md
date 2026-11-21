# Gap Analysis: Everful

## Candidate Gaps Identified

| Gap | Evidence Strength | Fit with Manicule | Urgency |
|-----|-------------------|-------------------|---------|
| **No public developer documentation for platform/API** | High — No `/developers`, `/docs`, `/api` on marketing site; Shopify integration + "infrastructure platform" vision requires it | **Perfect** — Core offering is dev-tool docs | **High** — Series A funds platform expansion; integrations need docs *now* |
| AI agent/ML model documentation for internal & external use | Medium — Blog mentions AI agents but no technical docs visible | Good — We do AI/ML docs | Medium — Internal need first |
| Mobile app developer docs (iOS/Android SDKs) | Low — Apps exist but no evidence of third-party dev surface | Moderate — Not core ICP | Low |
| Internal engineering docs/onboarding for 45-person R&D team | Low — Inferred from team size, no direct evidence | Moderate — We do internal docs | Low |

## Selected Primary Gap: **Missing Developer Documentation for Platform Integrations**

### The Gap (in their words)
> "We're deepening integrations with e-commerce platforms, building on its Shopify integration as it works toward becoming an **end-to-end infrastructure platform for global sourcing**." — TechCrunch, Nov 19 2026

> "We take care of everything. We handle sourcing, order consolidation, quality control, and logistics. That's something the marketplaces don't offer." — Kevin Han, co-founder

### Evidence Trail
1. **Shopify integration is live** but no public API reference, webhook guide, or authentication docs visible
2. **Series A explicitly funds** "deepening integrations with e-commerce platforms" — more integrations = more developer surfaces
3. **45 R&D engineers** building platform features with no public documentation home
4. **"Infrastructure platform" vision** means third-party developers will build on Everful — they need docs *before* launch
5. **AI agents automate sourcing workflows** — these workflows likely expose APIs/webhooks retailers' developers consume
6. **Competitive pressure**: Faire, Alibaba have developer portals; Everful's differentiation ("operational responsibility") extends to DX

### Why It Hurts Them Now
- **Integration friction**: Every new e-commerce platform integration (Shopify today, BigCommerce/WooCommerce/Magento tomorrow) requires developer onboarding — without docs, each partnership is a custom engineering project
- **Retailer developer adoption**: Boutiques/brands with dev teams want to automate ordering, sync inventory, build custom workflows — no docs = no adoption
- **Series A milestone risk**: Investors expect platform revenue; platform revenue requires developer adoption; developer adoption requires documentation
- **AI agent exposure**: "AI agents automate labor-intensive sourcing tasks" — if these agents are exposed via API, developers need prompt/parameter docs, error handling guides, rate limits

### Our Fix
**Manicule builds the developer documentation layer Everful needs to turn its platform into a platform others build on.**

We deliver:
1. **API reference** — auto-generated from code, human-curated for clarity
2. **Integration guides** — Shopify (audit + extend), BigCommerce, WooCommerce, Magento templates
3. **Webhook documentation** — event catalog, retry logic, signature verification, testing sandbox
4. **Authentication/authorization docs** — OAuth flows, API keys, scopes, rotation
5. **SDK/quickstart** — Node, Python, Ruby samples; "first call in 5 minutes"
6. **AI agent API docs** — prompt schemas, tool definitions, streaming responses, error codes
7. **Ongoing maintenance** — docs stay in sync with code via CI-integrated AI audits

### Our Proof Point (from profile.md)
> **Supermemory**: +30% answer success rate, multiple enterprise deals closed, **23-day turnaround** from kickoff to published docs
> **DevRel impact**: 1M+ SEO impressions, 90% traffic growth in 3 months, #1–#2 rankings on competitive queries

We don't just write — we ship a living documentation system that compounds value as Everful ships.

### Pitch Angle
**"You're building the infrastructure layer for global sourcing. The best infrastructure has the best developer experience. We make your docs the reason developers choose your API over Faire's."**