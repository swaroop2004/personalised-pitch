# Skyvern — research notes (2026-08-15)

## Part 1: Product, docs, blog, careers

### Positioning & business
- Tagline: "AI agents to automate workflows on any website"; vision-based automation pitched against "brittle DOM selectors" / traditional RPA. (https://www.skyvern.com)
- Target verticals: Healthcare, Insurance, Fintech & Banking, HR Tech.
- Claimed traction: 22.8K GitHub stars, "500+ Enterprise users", "30,000+ users & customers", "10M+ workflows run", 99.9% uptime SLA. Logos: CarEdge, Pilot, Valence Intelligence, rapidAND, Legion Health, ONLAYER, Pathmonk.
- YC S23, founded 2023, **team of 10**, SF. Founders: Suchintan Singh (CEO), Shuchang Zheng (CTO). (https://www.ycombinator.com/companies/skyvern)
- Pricing: credit-based — Free $0 / Hobby $29 / Pro $149 / Enterprise custom. HIPAA + human-in-the-loop gated to Enterprise. (https://www.skyvern.com/pricing)
- Compliance: SOC2 Type II, HIPAA, trust.skyvern.com.
- Benchmark claim: 85.8% on WebVoyager Eval.

### Docs (https://www.skyvern.com/docs/ — index at /docs/llms.txt)
What exists:
- SDKs: **Python and TypeScript only**, REST API (OpenAPI), MCP server.
- Rich SDK surface: page methods (act/extract/click/fill...), agent methods (run_task, login, download_files), cloud browser + CDP connect, workflows, browser sessions/profiles, credentials.
- Self-host: Docker, K8s, LLM config, local LLMs, storage config; June 2026 added GCP backends.
- Integrations documented: Zapier, Make.com, n8n, Workato only.
- Observability outsourced to third party: "Observability with Laminar" doc.
- **Only 3 cookbooks** (bulk invoice downloader, job application filler, healthcare portal data) vs 8 marketed use cases; no browser-testing/QA docs despite it being a homepage use case.

Their own admissions in docs:
- FAQ: max_steps >75 → "Contact support"; custom cloud LLMs → "Contact support"; 504s → "contact support with your run IDs"; anti-bot: "some sites use advanced anti-bot measures" that beat the CAPTCHA solver. (faq.md)
- Reliability tips: "Direct keyboard shortcuts... not currently supported"; "One bad item can take down your entire loop"; AI "second-guesses itself, erasing and retyping"; "Elements are visibly present but not detected." (reliability-tips.md)
- Cost control: main cost driver is LLM steps; fix is cached code (`run_with="code"`) — "faster, deterministic, and significantly cheaper". (cost-control.md)

Conspicuously absent:
- No Go/Java/Ruby/.NET SDKs (Rustwright bindings "planned").
- No vertical/system-of-record integrations (no ERP/AP, CRM, EHR connectors) despite regulated-industry positioning.
- No rate-limits page, no SLA terms, no SSO/SAML/RBAC/audit-log docs, no first-party observability docs.

### Blog / changelog (last 12 months)
- Fast monthly shipping cadence. July 2026: Workflow Studio GA, human-in-the-loop approvals, Code-First Browser Recording (Preview), credential rotation, Email Inbox/Split PDF blocks, SFTP/S3/Azure/GDrive delivery, org default LLMs, self-heal panel, reliability badges. (skyvern-changelog-july-2026)
- June 2026: **"Workflows renamed to Agents"** API rebrand (docs churn!), Workflow Studio Beta, code blocks Beta, multi-tab, 1Password/Bitwarden/Gmail-OTP, GCP self-host. (skyvern-changelog-june-2026)
- Rustwright (Jul 15, 2026): Playwright rewritten in Rust — 70% less memory, 2.55x faster, Alpha, Chromium-only. (rustwright blog post)
- Token-cost post: "How We Cut Token Count by 11% Using HTML Instead of JSON".
- **Content strategy is heavy SEO**: 9+ head-to-head comparison posts (UiPath, Airtop, CloudCruise, Firecrawl, Sola, Kernel, Browse AI, Axiom) + ~10 "Agentic Process Automation (APA)" category-creation posts since July — engineering-led marketing trying to own the "APA" keyword.

### Careers — the tell
- No careers page on site; hiring via YC/workatastartup. **All 3 open roles are founding GTM hires, zero engineering:**
  - Founding SDR ($60–75K)
  - Founding Account Executive ($120–300K)
  - **Founding Developer Marketing, Open Source AI ($100–150K + 0.1–0.3%) — "make Skyvern impossible to ignore"**
- Implication: 10-person engineering-heavy team building GTM from zero while claiming 500+ enterprise users; the SEO blitz is engineers filling the marketing gap.

### Candidate gaps (product-side)
1. GTM machinery built from zero — all 3 open roles are founding GTM.
2. SDK/language coverage stops at Python + TS.
3. No vertical/system-of-record integrations.
4. Reliability/determinism of AI path acknowledged in own docs.
5. LLM/infra cost pressure (Rustwright, token posts).
6. Enterprise self-serve gaps — "contact support" gates, no SSO/RBAC/audit-log/rate-limit docs, 3 cookbooks vs 8 use cases, docs churn from Workflows→Agents rename.

## Part 2: GitHub & community

### Repo health
- 22,755 stars, 2,140 forks, 214 open issues, AGPL-3.0; very high commit cadence by a small core team. Latest release v1.0.48 (Aug 5, 2026). (api.github.com/repos/Skyvern-AI/skyvern)
- Competitive scale gap: Browser Use ~108.8K stars vs Skyvern ~22.7K (4.8x), growing faster (+4.2%/30d vs +2.4%). (openalternative.co/compare/browser-use/vs/skyvern)
- New bet: rustwright repo (847 stars, active). Archived predecessors: wyvern, wyvern-docs.

### Most-demanded open issues
- #105 "Add tutorial for utilizing skyvern for automated UI testing" — MOST commented/upvoted open issue, open since March 2024 (~2.5 years). (github.com/Skyvern-AI/skyvern/issues/105)
- #6226 expose balance/token-usage via API (May 2026).
- #3897 cookies not persisting between workflows (Nov 2025).
- #1863 per-step timestamps (Mar 2025).
- #3260 VNC/CDP visual debugging epic (Aug 2025).

### Self-hosting/docs pain cluster
- #4584 "Docs are not good enough / Env files are missing" — their users' own words.
- #4953 hardcoded OpenAI startup checks break non-OpenAI deploys.
- #3782/#4220 misleading API-key errors in self-hosted UI.
- Quickstart breakage: #5756 (migrations+pip), #3915 (Linux Mint), #4666 (Windows 11), #3806 (pip chaos).
- #7762 broken `skyvern run server` on main (Jul 2026).
- Perf complaints CLOSED as "not planned": #4375, #4439 ("5-6 input fields... 4-5 minutes end-to-end").
- CVE-2025-49619: SSTI→RCE in workflow prompts (≤0.1.85).

### Sentiment
- HN: launches did well (422 pts Mar 2024; 327 pts Oct 2024) but no major thread since early 2025. Cost complaints: "pricing is utterly insane"; "$3.20 after using this on a few different pages". Mobile UI "practically unusable".
- Jan 2026 Ask HN: both Skyvern and Browser Use "inconsistent" for a real 80-site task.
- dev.to Framework Wars: Skyvern wins on legacy/canvas sites; loses on speed/cost ("screenshots at every step"); self-hosting "you're on your own for the infrastructure bits".
- May 2026 review: "Reddit consensus for hard real-world flows tends to land on Skyvern + Claude" — reputation is good where content is thin.
- Product Hunt: 5.0 but only 7 reviews, mostly old. G2 essentially empty.

### Candidate gaps (community-side)
1. Speed/cost of routine workflows (closed "not planned").
2. Self-hosted onboarding/deployment reliability — dense issue cluster.
3. Observability/cost transparency (#6226, #1863, #3260).
4. Session/state persistence (#3897).
5. QA/CI-CD use case unserved for 2.5 years (#105).
6. Real-world reliability vs outdated benchmark claims (WebVoyager now ~12th).
