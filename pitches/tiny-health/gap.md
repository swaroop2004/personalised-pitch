# Tiny Health — Gap Analysis

**Primary Gap:** **Developer-facing documentation for the Powered by Tiny API suite, bioinformatics pipeline (thMP/thDB/thDD/thMAP), and TinyAI — enabling partner integrations, researcher onboarding, and internal engineering velocity.**

---

## Evidence Trail (Their Own Words)

| Signal | Source | Quote |
|--------|--------|-------|
| **API suite exists but undocumented** | Powered by Tiny | "Turnkey co-branded gut and vaginal microbiome testing solution with **API suite**, partner portal, and volume discounts." |
| **Bioinformatics pipeline is core IP but opaque** | Technology page | "Our proprietary bioinformatics platform (eg **thMP, thDB, thDD**) allows us to create custom metrics... run through **thMAP** to plot the right reference ranges. We then use **machine learning** to personalize the recommendations..." |
| **TinyAI needs developer surfaces** | Series B Letter | "We're also introducing **TinyAI**, the world's first AI trained on Tiny Health's proprietary dataset of nearly 200,000 microbiome profiles. TinyAI is designed to turn a person's microbiome results into personalized, science-backed guidance..." |
| **Research program needs pipeline access** | Series B Letter | "$5M to the Tiny Health Microbiome Research Program to give researchers, clinicians and scientific partners access to our testing, data, **bioinformatics pipeline** and microbiome expertise." |
| **B2B scaling fast — 4x YoY** | Series B Letter | "Its B2B arm, **Powered by Tiny**, which sells tests through healthcare providers and other companies, **grew fourfold last year**." |
| **Hiring 30 engineers** | Series B Letter | "Presently, the company has about 40 employees and **plans to hire 30 more**." |
| **No public developer portal** | GitHub org | Only 1 repo: `fullstack-challenge` (hiring test). No SDKs, API docs, example apps, or open-source tooling. |
| **Support site inaccessible** | support.tinyhealth.com | Returns 403. FAQ scattered across Webflow pages. No searchable technical knowledge base. |

---

## Why This Gap Is Urgent

1. **Revenue-dependent:** Powered by Tiny is their fastest-growing segment (4x YoY). Every new partner (Superpower, Mayo Clinic, Fullscript, future "your brand") needs to integrate via API. Undocumented APIs = slower deals, higher support burden, churn risk.

2. **Research program blocked:** $5M Microbiome Research Program promises researchers access to the bioinformatics pipeline. Without docs, researchers can't use it. Grant money sits idle.

3. **TinyAI go-to-market:** An AI model without API docs, model cards, or integration guides is unsellable to practitioners and partners.

4. **Engineering onboarding:** Hiring 30 people into a codebase with proprietary components (thMP, thDB, thDD, thMAP) but no internal technical documentation = months of ramp time per hire.

5. **Compliance/Enterprise sales:** Enterprise partners (hospital systems, longevity clinics) require security questionnaires, data processing addenda, API authentication specs. None visible publicly.

---

## Our Fix (Manicule)

**We build the missing developer documentation layer:**

| Deliverable | Manicule Service | Value to Tiny Health |
|-------------|------------------|---------------------|
| **API Reference & Guides** | New docs from scratch + ongoing maintenance | Partners integrate in days not weeks; reduces support tickets |
| **Bioinformatics Pipeline Docs** (thMP/thDB/thDD/thMAP) | Technical writing + code verification | Researchers onboard faster; internal engineers ramp in weeks not months |
| **TinyAI Model Cards & Integration Guides** | Docs + DevRel strategy | Practitioners trust & adopt AI guidance; partners embed confidently |
| **Partner Developer Portal** | DevRel execution (SEO, content, structure) | Self-serve onboarding for "turnkey co-branded" promise |
| **Compliance & Security Docs** | Technical writing + architecture review | Enterprise deals close faster (Mayo, hospital systems) |
| **GitHub Presence & SDKs** | Code verification + video production | Public credibility; partners copy-paste instead of reverse-engineer |

---

## Proof Points from Profile.md

| Manicule Proof | Maps to Tiny Health Need |
|----------------|-------------------------|
| **Supermemory: +30% answer success rate, 23-day turnaround** | API reference + pipeline docs delivered fast — partners integrate before next quarter |
| **DevRel: 1M+ SEO impressions, 90% traffic growth in 3 months, #1–#2 rankings** | Developer portal ranks for "microbiome API", "gut health API", "metagenomics integration" — inbound partner leads |
| **Clients: Supermemory, Greptile, Reducto, Rootly, PromptLayer** | All developer-tool companies. We know how to document APIs, SDKs, pipelines for technical audiences |
| **Code verification of every sample** | Bioinformatics code (Python/R/Nextflow) tested — examples in docs actually run |
| **Video/screenshot production** | TinyAI demo videos, API walkthroughs, partner onboarding recordings |

---

## Why NOT Other Gaps

| Candidate Gap | Why Rejected |
|---------------|--------------|
| Consumer UX / conversion | Not our wheelhouse (we do dev tools, not CRO) |
| Lab operations / CLIA compliance | Deep domain expertise we lack |
| Clinical study design | We're not a CRO |
| Marketing content / blog | They have a content team (blog is active) |
| Hiring / recruiting | Not a service we offer |

---

## Pitch Angle

**"You've built the world's most comprehensive microbiome intelligence platform. Now you need the developer layer so partners, researchers, and your own engineers can actually use it at scale."**

- Hook: Their Series B letter *literally promises* API access, pipeline access, and AI access to partners/researchers
- Gap: None of those interfaces are documented
- Fix: Manicule builds the docs, portals, and DevRel that turn "API suite" from marketing claim into revenue engine
- CTA: Free 30-minute teardown of their current API/pipeline docs (or lack thereof) — walk through findings on a call

---

## Chosen Gap Summary

**One-liner:** Tiny Health's B2B platform (Powered by Tiny), research program, and TinyAI all depend on undocumented APIs and proprietary bioinformatics pipelines. Manicule builds the developer documentation, portals, and DevRel to unblock partner integrations, researcher onboarding, and engineering hiring — turning their $33M Series B promises into shipped product.