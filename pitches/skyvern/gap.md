# Skyvern — gap analysis & pitch angle (2026-08-15)

## Scoring the candidate gaps against Manicule's offering

| Gap | Evidence | Fit with Manicule | Urgency |
|---|---|---|---|
| Docs quality + broken onboarding | ★★★ (#4584 "Docs are not good enough", quickstart issue cluster, "contact us" gates, Workflows→Agents rename churn) | ★★★ docs rewrite + code verification is our core | ★★★ every broken quickstart bleeds OSS adoption vs Browser Use (4.8x stars) |
| Content/tutorial debt | ★★★ (#105 UI-testing tutorial = most-upvoted issue, open 2.5 yrs; 3 cookbooks vs 8 marketed use cases) | ★★★ cookbooks, video, verified samples | ★★★ their #1 asked-for thing, unanswered |
| DevRel/GTM from zero | ★★★ (hiring Founding Developer Marketing, "make Skyvern impossible to ignore"; engineers writing SEO posts) | ★★★ DevRel strategy + execution service | ★★★ budget already allocated (the job posting IS the budget) |
| Speed/cost of AI path | ★★★ | ✗ engineering problem, not ours | — |
| Missing SDKs / integrations | ★★ | ✗ engineering | — |
| Reliability vs benchmarks | ★★ | ~ (could be content: honest eval content) | — |

## Chosen gap (ONE): developer experience debt — docs, onboarding, and tutorials
are losing them the open-source developers their new GTM hires are supposed to win.

The three top-scoring gaps are actually one gap wearing three coats: Skyvern ships
product monthly, but the words around the product don't keep up. Evidence trail
(their users' and their own words):

1. Issue #4584 — literally titled **"Docs are not good enough / Env files are
   missing"** — required env files undocumented, circular Docker dependency.
2. Issue #105 — **"Add tutorial for utilizing skyvern for automated UI testing"** —
   their most-upvoted, most-commented open issue, unanswered since **March 2024**.
   Browser testing is marketed on their homepage; there are no docs for it.
3. Quickstart breakage cluster across Linux (#3915), Windows (#4666), pip (#5756,
   #3806) — first-run failures for self-hosters.
4. **3 cookbooks vs 8 marketed use cases**; observability docs outsourced to a
   third party (Laminar); no SSO/RBAC/rate-limit/SLA docs despite selling to
   Healthcare/Insurance/Fintech enterprises.
5. June 2026: "Workflows renamed to Agents" — an API-wide rename that multiplies
   stale-docs risk overnight.
6. Meanwhile: they're hiring **Founding Developer Marketing** ($100–150K + 0.1–0.3%)
   to "make Skyvern impossible to ignore", and engineers are hand-writing 19+ SEO
   posts. The budget and intent exist; the capacity doesn't.

Why it matters to them (the cost): Browser Use has 4.8x their stars and is growing
faster. Skyvern wins on hard sites ("Reddit consensus for hard real-world flows tends
to land on Skyvern + Claude") but loses the first 30 minutes: a developer who can't
get the quickstart running never learns Skyvern is better on the hard 20%. Every
broken `.env` is a silent churn to a competitor with 108K stars.

## Our fix (from profile.md)

- Docs restructure + rewrite with AI agents that **run and verify every code sample**
  — precisely the class of failure in #4584/#5756/#4666 (untested, drifting samples).
- Cookbook production for the 8 marketed use cases — starting with the UI-testing
  tutorial their community has begged for since 2024 (issue #105 becomes a PR).
- Ongoing maintenance — the Workflows→Agents rename is exactly the churn a
  maintenance retainer absorbs.
- DevRel execution with receipts: 1M+ SEO impressions, 90% traffic growth in 3 months
  — complements (or de-risks) the Founding DevMarketing hire; 23-day turnaround vs
  ~3-month hire ramp.

## Proof point to feature
Supermemory (also a YC devtool): +30% answer success rate after docs rebuild,
enterprise deals attributed, 23-day turnaround.

## CTA
Free teardown of docs.skyvern.com + the top-10 doc-shaped GitHub issues, walked
through on a 30-minute call. swaroop@manicule.dev
