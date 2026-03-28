# Course Design v2: AI Agents for Enterprise Data
## An 8-Session Executive Program (4 weeks, 90 min each, Zoom)

### Course Description

In February 2026, AI agents wiped $2 trillion from software company valuations. The technology behind that disruption is available now. In this four-week program, you will use an AI agent to query a simulated enterprise with 10 separate business systems, see how agents are built, red-team one for vulnerabilities, and develop an AI adoption strategy for your organization. You will leave understanding what AI agents can and cannot do, where they create value, and what it takes to deploy them responsibly.

---

## Course Resources

### The Meridian Corp App (browser-based, no installation)

A web-based AI data assistant that simulates a real enterprise data environment. Students open a browser, log in, and ask questions in plain English. The app connects to **10 enterprise systems** for a fictional $500M B2B industrial supplies distributor with three operating divisions:

- **Industrial Division** (~$250M): Salesforce CRM, NetSuite Finance, SAP Operations
- **Energy Division** (~$150M): Legacy CRM (custom-built), QuickBooks Finance, Oracle SCM
- **Safety Division** (~$100M): HubSpot CRM, shared NetSuite Finance
- **Corporate HQ**: Workday HR (all divisions), NetSuite Consolidation, Zendesk Support

The data includes realistic cross-system friction: Salesforce uses CamelCase column names while the Legacy CRM uses snake_case; the Legacy CRM stores dates as text strings ("MM/DD/YYYY") instead of proper dates; and ~25 customers appear under different names across divisions (e.g., "General Electric" in Salesforce, "GE Industrial Solutions" in the Legacy CRM, "GE Safety Division" in HubSpot).

The AI agent queries each system separately — it cannot join across systems in a single query. For cross-system questions, it pulls data from each system, then uses Python to merge, reconcile, and analyze the combined results. This mirrors how a real enterprise AI tool would work.

**41 tables, 26,000+ rows, 3 years of data (2023-2025).** Students can query sales pipelines, financial statements, employee compensation, supply chain performance, and support tickets — and combine data across all of them.

### The Linux Server (optional, for hands-on building)

A shared Linux server with individual student accounts, pre-installed with Claude Code (an AI coding assistant). Students who want hands-on experience can SSH in and build working data agents with AI assistance — they type directions in English, and the AI writes the Python code.

Four scaffolded exercises are pre-loaded:
- **Exercise 1**: Build a 50-line agent that queries one database (~30 min)
- **Exercise 2**: Extend it to query two systems and merge results (~30 min)
- **Exercise 3**: Wrap it in a web interface (~45 min)
- **Exercise 4**: Red-team the agent for security vulnerabilities (~30 min)

The server exercises are optional throughout the course. They are demonstrated by the instructor in Session 3 and available for self-paced exploration. Students who complete them gain a deeper understanding of how agents work, but the course does not require terminal or coding experience.

---

## Reviewer Feedback Incorporated

Three independent reviews (executive education designer, Fortune 500 CTO, Big 4 AI consulting partner) identified these themes:

1. **The hands-on coding exercises (SSH/terminal) risk losing non-technical executives.** Revised: Sessions 3-4 now use a "watch the loop, control the parameters" approach via the app's transparency features, with the Linux server as an optional advanced track.
2. **Change management is undercovered.** Revised: woven into Sessions 6-7, not treated as a bullet point.
3. **Build-vs-buy has a building bias.** Revised: Session 6 includes vendor AI reality check (Salesforce Agentforce, ServiceNow, Microsoft Copilot).
4. **Need an ROI framework early.** Revised: introduced in Session 2, carried through to capstone.
5. **The "complexity iceberg" — demo ≠ production.** Revised: addressed immediately after the demystification demo in Session 4.
6. **Data governance and regulatory exposure need more weight.** Revised: expanded in Session 5.
7. **Capstone needs a template and scoping discipline.** Revised: one-page template provided, 90-day pilot scope required.

---

## Session-by-Session Outline

---

### SESSION 1: "Why Can't I Just Ask a Question?"
**Week 1 / Tuesday — The Dashboard Problem**

**Learning objectives:**
- Experience conversational data access vs. traditional dashboards
- Understand what CRM, ERP, and BI tools actually do in an enterprise
- Articulate the bottleneck in the traditional reporting model

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-8 | **Cold open.** Show a real scenario: a CEO asks "which of our customers buy from multiple divisions?" The BI team says 3 weeks. Show the email chain. Ask: has this happened to you? | Provocation + discussion |
| 8-25 | **Demo: Dashboard vs. Chat.** Open the Meridian Corp app and ask the same question. Get an instant answer. Ask follow-ups the dashboard can't handle. Students see SQL, charts, narrative — all from a chat interface. | Live demo |
| 25-40 | **The Enterprise Software Landscape.** What Salesforce, SAP, Workday, NetSuite actually do. Why every company has 5-15 systems. Introduce Meridian Corp: $500M distributor, 3 divisions, 10 systems. | Lecture |
| 40-60 | **Hands-on: Your First Queries.** Students log into the app and ask 5-6 guided questions against Salesforce (single system). Guided prompts provided. | Hands-on |
| 60-75 | **Breakout Discussion (groups of 3).** What surprised you? What would this look like at your company? Who answers these questions today and how long does it take? Each group shares one insight. | Breakout rooms |
| 75-88 | **The Business Lens.** If a chat interface replaces dashboards, what happens to the tools and teams that build them? Plant the seed — don't go deep yet. | Lecture + Q&A |
| 88-90 | Homework assignment | Wrap |

**Homework:** Log into the Meridian app and ask 10 business questions of your choosing against any single system. Write down one question the agent answered well and one where it was unsatisfying or wrong. Bring both to Session 2.

---

### SESSION 2: "Our Data Is Everywhere"
**Week 1 / Thursday — The Cross-System Problem**

**Learning objectives:**
- Understand why enterprise data is scattered and why consolidation costs millions
- Watch AI query multiple systems and merge results in real time
- Begin building an ROI case for AI data access at their own company

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Homework debrief.** 3-4 students share best answer and worst answer. Why was the bad answer bad? (Usually: data is in another system.) | Discussion |
| 10-30 | **Demo: The Cross-System Merge.** Ask: "Which customers buy from multiple divisions?" Watch the agent query Salesforce, Legacy CRM, HubSpot separately, merge with Python using fuzzy matching. Then: "Revenue per employee by division?" — queries CRMs + Workday, merges. Agent shows SQL, explains matching, flags data quality issues. | Live demo |
| 30-42 | **How Data Moves Today.** APIs, integration platforms (MuleSoft), ETL/data warehouses, and CSV exports. The traditional answer is a warehouse ($500K-5M, 6-18 months). The alternative: query each system where it lives. Both have tradeoffs — warehouses are the default for good reasons (consistency, audit trail). | Lecture |
| 42-58 | **Hands-on: Cross-System Exploration.** Students try cross-system queries. Guided prompts + open exploration. Include a timed challenge: "Which division's top customer is most at risk of churning?" (requires CRM + Zendesk data). | Hands-on (competitive element) |
| 58-72 | **Workshop: Your Company's Data Map + ROI Template.** Each student sketches their company's 3-5 core systems and identifies one cross-system question nobody can answer easily today. For that question: What does it cost today? (analyst hours, elapsed time). What would AI-assisted cost be? This ROI template carries forward through the course. | Workshop |
| 72-85 | **What We're Skipping.** Before any agent can query real systems, someone must: catalog the data, document schemas, provision API access, classify PII. This is 60-90 days of pre-work that the demo does not show. Name it now so expectations are calibrated. | Lecture |
| 85-90 | Homework | Wrap |

**Homework:** (1) Read enterprise systems background document. (2) Complete your data map: list at least 5 systems your company uses and the top 3 cross-system questions you can't answer today. Estimate the current cost of not having those answers.

---

### SESSION 3: "How Does This Actually Work?"
**Week 2 / Tuesday — Inside the Agent Loop**

**Learning objectives:**
- Understand the agent loop (plan → execute → observe → repeat) at a conceptual level
- See the 50 lines of code that power the core of the app they've been using
- Recognize that the technology is simple; the hard parts are prompt engineering, data quality, and governance

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Bridge.** "You've spent a week as the user. Now let's look under the hood." | Lecture |
| 10-30 | **Demo: The Agent Loop, Deconstructed.** Show the Meridian app answering a cross-system question, but this time show what happens behind the scenes: the system prompt (schema description), the tool call (SQL), the result, the merge (Python), the final response. Walk through the 50-line core loop on screen. Emphasize: this is the entire engine. | Live demo + code walkthrough |
| 30-45 | **The System Prompt Is the Secret.** Show how changing the schema description changes the SQL the agent generates. Demo: remove the join key documentation from the prompt → the agent can no longer merge across systems. Add it back → it works. The prompt is the "institutional knowledge" layer. | Live demo |
| 45-60 | **Discussion: Who Builds This?** If the core is 50 lines, why does deployment take months? Introduce the "complexity iceberg": authentication, error handling, rate limits, access control, monitoring, audit logging, multi-tenancy, failover. Show the actual Meridian app codebase (3,000+ lines) vs. the 50-line core. | Lecture + Q&A |
| 60-75 | **Breakout: Build vs. Buy First Impressions (groups of 3).** Given what you now know about the technology: for the use case you identified in Session 2, would you build, buy from your existing vendor, or hire a consultant? Why? Share out. | Breakout rooms |
| 75-88 | **Optional: Live Build with Claude Code.** For the room, demonstrate building a simple agent from scratch in real time using Claude Code on the Linux server. The instructor drives; students watch. Show how AI writes the code from English instructions. This is the "your developer could do this" moment. | Live demo (instructor-driven) |
| 88-90 | Homework | Wrap |

**Homework:** (1) For those who want hands-on experience: SSH credentials are provided. Exercise 1 (hello-world agent) and Exercise 2 (multi-system agent) are on the server with starter templates. Claude Code will help you — you direct it in English. This is optional but recommended. (2) Required: Revisit your ROI template from Session 2 and add: what data quality issues would you expect to encounter? What pre-work is needed?

**Note:** The Linux server exercises are available throughout the course for self-paced exploration. They are not required but provide deeper understanding for those who want it.

---

### SESSION 4: "The Last Mile and the Hard Parts"
**Week 2 / Thursday — From Insight to Artifact, From Demo to Production**

**Learning objectives:**
- See the full pipeline: data → chart → narrative → board-ready memo
- Understand architecture decisions (where Python runs, what the LLM sees)
- Grasp the gap between a working demo and a production deployment

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Check-in.** Anyone try the Linux server exercises? Quick show. Share struggles and surprises. | Discussion |
| 10-28 | **Demo: The Full Pipeline.** Ask the Meridian app: "Prepare a quarterly executive summary of Meridian Corp performance — revenue by division, headcount efficiency, top customer risks, and supply chain issues." Watch it query 6 systems, merge data, generate charts, and produce a structured memo. This is the "last mile" — not just data, but a delivered artifact. | Live demo |
| 28-42 | **Architecture Decisions.** Where does the Python run? Three options: (A) cloud LLM sandbox — data leaves your network; (B) SQL-only — can't do cross-system merges; (C) your own containers — production answer. The data exposure problem: even with local execution, the LLM sees results. Four approaches to managing privacy. Key insight: this is a policy decision, not a technology problem. | Lecture |
| 42-55 | **The Complexity Iceberg.** Walk through what it takes to go from demo to production: API authentication against real systems (OAuth, SOQL, OData — not just parquet files), PII handling, schema changes, monitoring, the fact that Salesforce has 847 custom fields in a real instance. Realistic timeline: pilot in 2-3 months, production in 6-12 months. | Lecture |
| 55-70 | **Discussion: What Would Your CISO Say?** Each student considers: if you brought this to your security team, what would they flag? Role-play: one student pitches, another plays the skeptical CISO. 2-3 pairs share. | Paired role-play |
| 70-85 | **Cost Modeling.** Concrete numbers: API costs per query (~$0.01-0.05), infrastructure, development time, maintenance. Compare to: Tableau licenses ($50-300/user/month), analyst headcount ($80-150K/year), data warehouse project ($500K-5M). Students update their ROI template with cost estimates. | Lecture + workshop |
| 85-90 | Preview Week 3 (trust and verification) | Wrap |

**Homework:** (1) Update your ROI template with architecture choice and cost estimates. (2) Identify one report or dashboard at your company that this technology could replace. What data sources does it need? What could go wrong?

---

### SESSION 5: "Can You Trust It?"
**Week 3 / Tuesday — Verification, Errors, and Governance**

**Learning objectives:**
- Identify failure modes of AI data agents (hallucination, wrong joins, misleading aggregations)
- Apply the maker/checker framework: AI produces, human verifies
- Understand data governance and regulatory requirements for AI agents

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Homework debrief.** Students share the report they'd replace and what could go wrong. | Discussion |
| 10-30 | **Demo: When the Agent Gets It Wrong.** Three pre-prepared failures: (a) averages across won and lost deals without filtering — technically correct SQL, misleading answer; (b) cross-division revenue comparison with date format mismatch — Legacy CRM VARCHAR dates cause wrong aggregation; (c) customer count that double-counts due to fuzzy matching failures. Walk through each, show the SQL, identify the error. | Live demo |
| 30-45 | **The Maker/Checker Framework.** AI is the maker; you are the checker. The skill shift: from producing analysis to verifying it. What to check: source system, filters, join logic, date ranges, NULL handling, row counts. The agent shows SQL for a reason — transparency is a feature. Who in your organization has the judgment to be an effective checker? | Lecture + discussion |
| 45-60 | **Hands-on: Red-Team the Meridian App.** Students try to break the agent through the chat interface: ask for data they shouldn't see (individual salaries), ask a question where the data doesn't exist (2027 revenue), try to trick it into hallucinating ("What was our revenue from the Atlantis division?"). Record what happens. | Hands-on |
| 60-75 | **Data Governance and Regulatory Exposure.** Not a 10-minute afterthought — a serious treatment. Who is liable when the agent gives wrong financial data? Does agent output count as a "record" under SOX? GDPR implications of cross-system queries that combine PII from multiple sources. Role-based access control: the VP of Sales should not see HR compensation data, even if the agent can query both systems. | Lecture + Q&A |
| 75-88 | **Discussion: Your Governance Requirements.** Given your industry and regulatory environment, what guardrails would you require before deploying an AI agent? What's the minimum viable governance framework? | Discussion |
| 88-90 | Homework | Wrap |

**Homework:** (1) Read the Klarna case study (provided as handout). They replaced Salesforce and Workday with AI, then partially reversed course. Come prepared to discuss: what did they get right? What went wrong? (2) For your identified use case: what governance requirements would your compliance team impose?

---

### SESSION 6: "The $2 Trillion Question"
**Week 3 / Thursday — AI Disruption of Enterprise Software**

**Learning objectives:**
- Distinguish which software categories are vulnerable to AI replacement vs. which are not
- Evaluate build vs. buy vs. extend for AI capabilities
- Map their own company's software portfolio against the disruption framework

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-8 | **Klarna debrief.** Each student: one sentence on what Klarna got right and one on what went wrong. | Quick round |
| 8-25 | **What Happened in February 2026.** The Cowork announcement, $285B in one day, $2T cumulative. But frame analytically, not apocalyptically: which categories lost value and why? The dividing line: AI replaces the interface layer (BI, workflow, Tier 1 support), not the data layer (ERP, HRIS, financial ledgers). Evidence: Retool survey (29-35% already replacing), pricing shifts (Intercom $0.99/resolution). | Lecture with data |
| 25-38 | **The Meridian Connection.** Map the app's capabilities to the disruption categories. It replaces Tableau (BI), data integration tools (MuleSoft), reporting headcount. It does NOT replace Salesforce the database, SAP the ERP, or Workday the HR system. | Discussion |
| 38-55 | **Build vs. Buy vs. Extend.** The real decision matrix: (a) buy from incumbent vendor — Salesforce Agentforce, Microsoft Copilot, ServiceNow AI (lowest risk, moderate capability); (b) buy from AI-native startup (highest capability, integration risk); (c) build internally (highest control, requires talent); (d) hybrid — vendor AI where good enough, custom for differentiation. Walk through one specific vendor (Salesforce Agentforce): what it does today, what it costs, where it falls short. Most enterprises land on (d). | Lecture + Q&A |
| 55-75 | **Workshop: Your Software Vulnerability Map.** Each student maps 10+ products in their company's stack into four quadrants: (1) keep as-is, (2) evaluate vendor AI additions, (3) candidate for custom AI replacement, (4) candidate for retirement. Work individually, then pair-share. | Workshop |
| 75-88 | **Change Management Preview.** When you replace tools, you displace roles. The VP of FP&A whose team does variance analysis. The BI team that builds dashboards. The analysts who pull cross-system reports. This is not a technology problem — it's a leadership challenge. Preview for Session 7. | Lecture |
| 88-90 | Homework | Wrap |

**Homework:** (1) Complete your vulnerability map (10+ products). (2) Identify your single highest-ROI AI opportunity. Write one paragraph: the problem, the systems involved, the expected value. Bring to Session 7.

---

### SESSION 7: "Making It Real"
**Week 4 / Tuesday — From Strategy to Execution**

**Learning objectives:**
- Articulate the organizational, governance, and technical requirements for deployment
- Scope a realistic 90-day pilot (not a 2-year transformation)
- Draft the core of an AI adoption strategy

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-12 | **Opportunity share.** 4-5 students present their one-paragraph opportunity. Quick peer feedback: is it scoped tightly enough? Is the data accessible? | Discussion |
| 12-28 | **Organizational Readiness.** The #1 reason AI projects fail is not technical — it's organizational. Middle management resistance (the VP whose team is threatened). Data fiefdoms (the division head who won't share CRM access). Shadow IT (60% of teams building outside IT oversight). Sponsor identification: who has budget authority AND political capital? The "coalition of the willing" approach to pilot selection. | Lecture |
| 28-42 | **The 90-Day Pilot Framework.** Right-size your first deployment: one use case, one team, one data source, deliver value in 90 days, then expand. What a realistic pilot looks like: Week 1-2 data access and schema documentation, Week 3-4 build prototype, Week 5-8 pilot with real users, Week 9-12 measure and decide. Governance minimum: access controls, audit log, human verification requirement, incident response. | Lecture |
| 42-55 | **Role-Play: The Executive Pitch.** In pairs, one student pitches their AI opportunity to their CEO (played by partner). The "CEO" pushes back: "My CISO will never approve this." "Salesforce says Agentforce already does this." "We tried a data warehouse and it failed." Practice handling objections. | Role-play |
| 55-78 | **Workshop: Draft Your Strategy.** Using the provided template, each student drafts: (1) problem statement and current cost, (2) proposed solution and architecture, (3) 90-day pilot plan (team, data, timeline), (4) governance requirements, (5) success metrics (from ROI template), (6) risks and mitigations. Work individually. Instructor circulates. | Workshop |
| 78-88 | **Capstone Preview.** You are pitching your CEO in Session 8. Five minutes. Use the template. The audience is your board of advisors. | Logistics |
| 88-90 | Homework | Wrap |

**Homework:** Finalize your strategy document (1-2 pages using the template). Prepare a 5-minute presentation. Required sections: the problem, the solution, the 90-day plan, the ask, the Day 1 action.

---

### SESSION 8: "Your AI Strategy"
**Week 4 / Thursday — Capstone and Synthesis**

**Learning objectives:**
- Present a credible, scoped AI adoption strategy to peers
- Synthesize the technical, strategic, and organizational dimensions
- Leave with a concrete next step

**Session flow (30 students):**

| Min | Segment | Format |
|---|---|---|
| 0-3 | **Setup.** You are presenting to your executive team. Your breakout group is your board of advisors. | Framing |
| 3-30 | **Breakout pitches.** 5 groups of 6. Each person presents their strategy (3 minutes) to their group. Group discusses and votes on the strongest strategy to represent them in the plenary. | Breakout rooms |
| 30-70 | **Plenary presentations.** 5 winning strategies presented to the full class (5 min each + 3 min Q&A/feedback). Instructor feedback on: is the pilot scoped tightly enough? Is the ROI credible? Is the governance plan adequate? Does the Day 1 action actually happen on Day 1? | Presentations |
| 70-80 | **Synthesis: Three Lessons.** (1) AI agents replace the interface layer, not the data layer — dashboards and data warehouses are the first casualties, not ERP systems. (2) Building is easier than you thought, but governing is harder — the 50-line agent works, but production requires guardrails, access control, and verification. (3) The strategic question is not "will AI disrupt enterprise software?" but "will your company drive that disruption or react to it?" | Lecture |
| 80-85 | **Monday Morning Actions.** Four things every executive can do regardless of role: (a) audit your software stack with the vulnerability framework, (b) scope a 30-day discovery sprint on one use case, (c) demand outcome-based pricing from your SaaS vendors at the next renewal, (d) establish an AI governance framework before shadow IT does it for you. | Lecture |
| 85-90 | Close. Resources for continued learning. Optional 30-day follow-up session to report on progress. | Wrap |

---

## Cross-Session Summary

| Session | Title | Primary Activity | Theme Mix |
|---|---|---|---|
| 1 | Why Can't I Just Ask? | First app experience + guided queries | Dashboard replacement |
| 2 | Our Data Is Everywhere | Cross-system demo + ROI template | Data warehouse replacement |
| 3 | How Does This Work? | Agent loop deconstructed + optional build | Demystification |
| 4 | Last Mile and Hard Parts | Full pipeline demo + architecture + costs | Production realism |
| 5 | Can You Trust It? | Failure demos + red-teaming + governance | Trust and governance |
| 6 | The $2 Trillion Question | SaaSpocalypse + vendor landscape + vuln map | Strategic disruption |
| 7 | Making It Real | Org readiness + 90-day pilot + strategy draft | Execution planning |
| 8 | Your AI Strategy | Capstone presentations + synthesis | Integration |

## Recurring Elements

- **ROI Template:** Introduced Session 2, updated Sessions 4 and 7, underpins the capstone.
- **Breakout Rooms:** Sessions 1, 3, 6 — prevents Zoom large-group discussion fatigue.
- **Role-Play:** Sessions 4 (CISO) and 7 (CEO pitch) — practices the conversations executives will actually have.
- **The Meridian App:** Used in every session through Session 5 — the shared reference point.
- **Linux Server:** Available throughout for self-paced exploration; demonstrated in Session 3; exercises are optional homework.

## Capstone Template (provided to students)

1. **The Problem:** What question can't be answered today? What does it cost? (from ROI template)
2. **The Solution:** AI agent architecture — which systems, what merging logic, build/buy/extend decision
3. **The 90-Day Pilot:** Team (who), data (which systems), timeline (week-by-week), governance minimum
4. **Success Metrics:** Time-to-insight, analyst leverage, error reduction, adoption rate
5. **Risks and Mitigations:** Data quality, organizational resistance, vendor lock-in, regulatory
6. **The Ask:** Budget, headcount, executive sponsor
7. **Day 1 Action:** The one thing you will do Monday morning
