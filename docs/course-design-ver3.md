# Course Design v3: From BI to AI — Data-Driven Decision Making with Agentic AI
## An 8-Session Executive Program (4 weeks, 90 min each, Zoom)

### Course Description

AI agents that understand plain English, query your data, and deliver answers in seconds are transforming how organizations make decisions. In this four-week program, you will use an AI agent to query a simulated enterprise, build reporting pipelines, deploy document-based AI, and evaluate reliability and governance requirements — all hands-on, no coding required. You will leave equipped with tools you can immediately deploy and a concrete strategy for bringing AI-powered data access to your organization.

### Pre-Program Video

Before Session 1, participants watch a 15-20 minute video covering:
- What AI agents are and why they matter for data-driven decision making
- The Meridian Corp simulation: a $500M distributor with 10 enterprise systems across 3 divisions
- The Linux VM: an optional hands-on environment for those who want to build agents themselves
- How to log in to both tools and what to expect in Session 1

This allows Session 1 to begin immediately with hands-on work.

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

## Session-by-Session Outline

---

### SESSION 1: "Exploring Data with AI"
**Week 1 / Tuesday — From Questions to Answers in Seconds**

**Learning objectives:**
- Experience conversational data access vs. traditional dashboards
- Ask business questions in plain English and get instant answers with charts
- Identify what AI data access changes about the speed of decision making

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-5 | **Cold open.** A CEO asks "which of our customers buy from multiple divisions?" The BI team says 3 weeks. Show the email chain. Ask: has this happened to you? | Provocation + discussion |
| 5-15 | **Demo: Dashboard vs. Chat.** Open the Meridian Corp app and ask the same question. Get an instant answer. Ask follow-ups the dashboard can't handle. Students see SQL, charts, narrative — all from a chat interface. | Live demo |
| 15-40 | **Hands-on: Your First Queries.** Students log into the app and work through 8-10 guided prompts against single systems — Salesforce pipeline queries, NetSuite financial summaries, Workday headcount breakdowns. Prompts progress from simple ("How many open deals are in Salesforce?") to analytical ("Which sales rep has the highest win rate this quarter?"). | Hands-on |
| 40-55 | **Open Exploration.** Students ask their own questions. Challenge: find something surprising in the data. Instructor highlights interesting discoveries in real time. | Hands-on |
| 55-70 | **Breakout Discussion (groups of 3).** What surprised you? What would this look like at your company? Who answers these questions today and how long does it take? Each group shares one insight. | Breakout rooms |
| 70-85 | **The Business Lens.** If anyone in your company could ask a data question and get an instant answer, what changes? Who benefits? What decisions get made faster? What decisions get made that weren't being made at all? | Lecture + discussion |
| 85-90 | Homework assignment | Wrap |

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
| 58-68 | **Workshop: Your Company's Data Map + ROI Template.** Each student sketches their company's 3-5 core systems and identifies one cross-system question nobody can answer easily today. For that question: What does it cost today? (analyst hours, elapsed time). What would AI-assisted cost be? This ROI template carries forward through the course. | Individual work |
| 68-82 | **Breakout: How Scattered Is Your Data? (groups of 3-4).** Compare data maps. What systems do you have in common? Where is integration hardest? What cross-system questions would have the most business value? Each group reports back: one pattern that was common across companies and one surprising idiosyncrasy. | Breakout rooms |
| 82-88 | **What We're Skipping.** Before any agent can query real systems, someone must: catalog the data, document schemas, provision API access, classify PII. This is 60-90 days of pre-work that the demo does not show. Name it now so expectations are calibrated. | Lecture |
| 85-90 | Homework | Wrap |

**Homework:** (1) Read enterprise systems background document. (2) Complete your data map: list at least 5 systems your company uses and the top 3 cross-system questions you can't answer today. Estimate the current cost of not having those answers.

---

### SESSION 3: "How Does This Actually Work?"
**Week 2 / Tuesday — Inside the Agent Loop**

**Learning objectives:**
- Understand the agent loop as an orchestrated test-and-review cycle between the LLM and code execution
- See the 50 lines of code that power the core of the app they've been using
- Understand where code executes and why that's an architectural decision with security implications

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Bridge.** "You've spent a week as the user. Now let's look under the hood." | Lecture |
| 10-30 | **Demo: The Agent Loop, Deconstructed.** Show the Meridian app answering a cross-system question, but this time show what happens behind the scenes: the system prompt (schema description), the tool call (SQL), the result, the merge (Python), the final response. Walk through the 50-line core loop on screen. Key insight: this is a **test-and-review cycle** — the LLM writes code, the system executes it, the LLM reviews the results, decides if they're correct, and either delivers the answer or tries again. The orchestration layer manages this loop. | Live demo + code walkthrough |
| 30-45 | **The System Prompt Is the Secret.** Show how changing the schema description changes the SQL the agent generates. Demo: remove the join key documentation from the prompt → the agent can no longer merge across systems. Add it back → it works. The prompt is the "institutional knowledge" layer. This is how you connect an agent to a database: describe the schema, give the agent a tool to execute SQL, and let the loop do the rest. | Live demo |
| 45-60 | **Where Does the Code Run?** The LLM generates SQL and Python. Something has to execute it. Three options: **(A) Cloud LLM sandbox** — the LLM vendor runs the code on their servers (simple, but your data leaves your network); **(B) Your own containers** — Docker on your servers, data never leaves (production answer for sensitive data); **(C) SQL-only** — the LLM generates queries but never runs Python (safe, but can't do cross-system merges). Our demo uses Option A with synthetic data; production deployments use Option B. This is the first of several deployment decisions executives need to understand. | Lecture |
| 60-72 | **Discussion: The Complexity Iceberg.** If the core is 50 lines, why does deployment take months? Authentication, error handling, rate limits, access control, monitoring, audit logging, multi-tenancy, failover. Show the actual Meridian app codebase (3,000+ lines) vs. the 50-line core. Where does your company's IT team fit in? | Lecture + Q&A |
| 72-85 | **Optional: Live Build with Claude Code.** Demonstrate building a simple agent from scratch in real time using Claude Code on the Linux server. The instructor drives; students watch. Show how AI writes the code from English instructions. This is the "your developer could do this" moment. | Live demo (instructor-driven) |
| 85-90 | Homework | Wrap |

**Homework:** (1) For those who want hands-on experience: SSH credentials are provided. Exercise 1 (hello-world agent) and Exercise 2 (multi-system agent) are on the server with starter templates. Claude Code will help you — you direct it in English. This is optional but recommended. (2) Required: Revisit your ROI template from Session 2 and add: what data quality issues would you expect to encounter? What pre-work is needed?

**Note:** The Linux server exercises are available throughout the course for self-paced exploration. They are not required but provide deeper understanding for those who want it.

---

### SESSION 4: "From Data to Deliverable"
**Week 2 / Thursday — Reporting Pipelines, Deployment, and Data Security**

**Learning objectives:**
- See the full pipeline: data → chart → narrative → board-ready memo
- Understand LLM deployment options and their tradeoffs (cloud API vs. on-premise)
- Grasp the data security problem: what the LLM sees and how to control it

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Check-in.** Anyone try the Linux server exercises? Quick show. Share struggles and surprises. | Discussion |
| 10-25 | **Demo: The Full Pipeline.** Ask the Meridian app: "Prepare a quarterly executive summary of Meridian Corp performance — revenue by division, headcount efficiency, top customer risks, and supply chain issues." Watch it query 6 systems, merge data, generate charts, and produce a structured memo. This is the "last mile" — not just data, but a delivered artifact. | Live demo |
| 25-35 | **Anatomy of a Reporting Pipeline.** Break down what just happened into discrete steps: (1) query multiple systems, (2) clean and merge, (3) compute metrics, (4) generate charts, (5) write narrative, (6) assemble into a document. Each step can be customized, templated, and reused. In production, these pipelines run on schedules — Monday morning dashboard refresh, monthly board deck, weekly sales forecast — with human review gates before delivery. | Lecture |
| 35-50 | **Hands-on: Build Your Own Report.** Students use the Meridian app to produce a specific deliverable. Guided prompts: "Create a customer risk report combining CRM pipeline data with support ticket trends" or "Produce a division-level P&L comparison with commentary." Students iterate on prompts to improve output quality. | Hands-on |
| 50-65 | **LLM Deployment Options.** Session 3 covered where *code* executes. Now: where does the *LLM* run? **(A) Cloud API** (Anthropic, OpenAI, Azure) — best quality, simplest to deploy, but prompts and results transit the vendor's servers. **(B) On-premise open-source** (Llama, Mistral on your hardware) — data never leaves your network, but significantly worse at SQL generation, multi-step reasoning, and narrative quality; this gap is closing but still large. **(C) Hybrid** — cloud LLM for non-sensitive analysis, on-premise for regulated data. Most enterprises will land on (A) or (C), with contractual data handling agreements. Concrete cost comparison: cloud API ~$0.01-0.05 per query vs. on-premise GPU infrastructure ($50-200K+ upfront). | Lecture |
| 65-80 | **The Data Security Problem.** Even when code runs on your servers (Session 3, Option B), the LLM still sees query results — salary figures, customer records, deal values — because it needs them to interpret data, fix errors, and write narratives. Running code locally does not solve data privacy by itself. Four approaches: **(1) Aggregated results with guardrails** — the LLM sees totals and averages, not individual records; a DLP layer redacts PII before results reach the LLM (most common in practice). **(2) Blind templates** — the LLM generates code but never sees actual data; results render directly to the user (used in banking/healthcare). **(3) On-premise LLM** — nothing leaves the network, but quality drops. **(4) Schema-only** — the LLM sees only schemas and synthetic samples; all code runs blind. The key insight: this is a policy decision, not a technology problem. The technology to filter and restrict is straightforward; the hard part is deciding what exposure is acceptable for your organization. | Lecture + Q&A |
| 80-88 | **Breakout: What Would Your CISO Say? (groups of 3-4).** Given your industry and regulatory environment: which LLM deployment option fits? Which data security approach? What would your security and compliance teams flag first? Each group reports back: what constraints were common, and where did industry differences lead to different answers? Update your ROI template with architecture choice and cost estimates. | Breakout rooms |
| 88-90 | Preview Week 3 (trust and verification) | Wrap |

**Homework:** (1) Use the Meridian app to produce one complete deliverable of your choosing — a memo, a comparison, a risk assessment. Save or screenshot the output. (2) Update your ROI template with deployment architecture, data security approach, and cost estimates. (3) Identify one report at your company this technology could replace. What data sources does it need? What could go wrong?

---

### SESSION 5: "Can You Trust It?"
**Week 3 / Tuesday — Reliability, Verification, and Compliance**

**Learning objectives:**
- Identify failure modes of AI data agents (hallucination, wrong joins, misleading aggregations)
- Apply the maker/checker framework: AI produces, human verifies
- Understand data governance and regulatory requirements for AI agents

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Homework debrief.** Students share the deliverable they produced. What looked right? What would you want to verify before sending to your board? | Discussion |
| 10-30 | **Demo: When the Agent Gets It Wrong.** Three pre-prepared failures: (a) averages across won and lost deals without filtering — technically correct SQL, misleading answer; (b) cross-division revenue comparison with date format mismatch — Legacy CRM VARCHAR dates cause wrong aggregation; (c) customer count that double-counts due to fuzzy matching failures. Walk through each, show the SQL, identify the error. | Live demo |
| 30-42 | **The Maker/Checker Framework.** AI is the maker; you are the checker. The skill shift: from producing analysis to verifying it. What to check: source system, filters, join logic, date ranges, NULL handling, row counts. The agent shows SQL for a reason — transparency is a feature. Who in your organization has the judgment to be an effective checker? | Lecture + discussion |
| 42-55 | **Hands-on: Red-Team the Meridian App.** Students try to break the agent through the chat interface: ask for data they shouldn't see (individual salaries), ask a question where the data doesn't exist (2027 revenue), try to trick it into hallucinating ("What was our revenue from the Atlantis division?"). Record what happens. | Hands-on |
| 55-72 | **Data Governance and Regulatory Exposure.** Not a 10-minute afterthought — a serious treatment. Who is liable when the agent gives wrong financial data? Does agent output count as a "record" under SOX? GDPR implications of cross-system queries that combine PII from multiple sources. Role-based access control: the VP of Sales should not see HR compensation data, even if the agent can query both systems. The data exposure problem: even with local execution, the LLM sees query results. Four approaches to managing privacy (aggregated results with guardrails, blind templates, on-premise LLM, schema-only with sanitized errors). | Lecture + Q&A |
| 72-85 | **Breakout: Your Governance Requirements (groups of 3-4).** Given your industry and regulatory environment, what guardrails would you require before deploying an AI agent? What's the minimum viable governance framework? Each group reports back: what governance requirements were universal vs. industry-specific? Where would adoption stall without executive air cover? | Breakout rooms |
| 85-90 | Homework | Wrap |

**Homework:** (1) Read the Klarna case study (provided as handout). They replaced Salesforce and Workday with AI, then partially reversed course. Come prepared to discuss: what did they get right? What went wrong? (2) For your identified use case: what governance requirements would your compliance team impose?

---

### SESSION 6: "AI as Thinking Partner"
**Week 3 / Thursday — Beyond Data Retrieval**

**Learning objectives:**
- Use AI to challenge assumptions, stress-test strategies, and run structured analyses
- Combine data analysis with strategic thinking frameworks
- Distinguish AI as analyst (retrieves data) from AI as advisor (reasons about data)

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-8 | **Klarna debrief.** Each student: one sentence on what Klarna got right and one on what went wrong. | Quick round |
| 8-25 | **Demo: From Analyst to Advisor.** Same Meridian app, different use. Instead of "What were Q4 sales?", ask: "I'm considering expanding the Energy Division into the Southeast. Based on our sales pipeline, customer concentration, and support ticket trends, what are the top 3 risks?" The agent pulls data from multiple systems and then *reasons* about it — identifying patterns, flagging concerns, suggesting what to investigate next. | Live demo |
| 25-40 | **Structured Thinking Moves.** Show how to use AI as a sparring partner for decisions: (1) Pre-mortem — "Assume this initiative fails in 12 months. What went wrong?" (2) Red team — "Argue against this investment." (3) Scenario analysis — "Model optimistic, base, and pessimistic cases using our actual data." (4) Assumption audit — "What assumptions am I making? Which ones can we test with data?" Each demonstrated live with Meridian data. | Live demo + discussion |
| 40-55 | **Hands-on: Stress-Test a Decision.** Each student picks a real business decision they're facing (or uses a provided scenario). Using the Meridian app as a proxy, they practice the thinking moves: ask the AI to challenge their assumptions, run a pre-mortem, identify data gaps. Focus on prompt craft — how to get substantive pushback rather than agreeable summaries. | Hands-on |
| 55-70 | **When AI Thinking Goes Wrong.** The limits: AI will confidently reason from bad data, it has no institutional memory, it can't read political dynamics, and it anchors on whatever framing you provide. Demo: give the same data with different framing and get opposite recommendations. The human role is providing context, judgment, and the right questions. | Lecture + demo |
| 70-85 | **Build vs. Buy Reality Check.** Given everything you've seen over five sessions — the technology, the failure modes, the governance requirements: for the use case you identified in Session 2, would you build, buy from your existing vendor (Salesforce Agentforce, Microsoft Copilot, ServiceNow), or hire a consultant? Quick framework: vendor AI where good enough, custom for differentiation. Most enterprises land on a hybrid. | Discussion |
| 85-90 | Homework | Wrap |

**Homework:** (1) Use the AI-as-thinking-partner approach on a real decision at your company. Document the exchange: what you asked, what was useful, what was wrong or unhelpful. (2) Begin drafting your capstone strategy (template provided): problem statement, proposed solution, 90-day pilot plan.

---

### SESSION 7: "Document AI — Answers from Your Own Files"
**Week 4 / Tuesday — Retrieval-Augmented Generation (RAG)**

**Learning objectives:**
- Understand how AI can answer questions grounded in company documents with citations
- Distinguish database AI (structured data queries) from document AI (unstructured text retrieval)
- Understand RAG deployment: embedding models, vector stores, document pipelines, and hosting

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Bridge.** "For six sessions, we've worked with structured data — databases, tables, SQL. But most company knowledge isn't in databases. It's in policies, contracts, emails, and slide decks." | Lecture |
| 10-25 | **Demo: Document-Based Q&A.** Pre-loaded document collection for Meridian Corp: employee handbook, vendor contracts, compliance policies, board minutes. Ask: "What is our policy on remote work for the Energy Division?" "Which vendor contracts are up for renewal in Q2?" "What did the board approve regarding the Safety Division expansion?" Answers come with citations — page numbers and quoted passages. | Live demo |
| 25-38 | **How RAG Works.** The retrieval-augmented generation pipeline: (1) documents are chunked into passages, (2) an embedding model converts each chunk into a numerical vector, (3) chunks are stored in a vector database, (4) the user's question is embedded the same way and matched against stored chunks, (5) the top matches are sent to the LLM as context, (6) the LLM answers using only the retrieved context. Compare to database agents: RAG handles *unstructured* text; database agents handle *structured* data. Both are tools in the same toolkit. When you need both: "What's our contractual obligation to GE, and how does their actual spending compare?" — RAG for the contract, database agent for the spending. | Lecture |
| 38-52 | **Hands-on: Query the Document Collection.** Students ask questions of the Meridian document set. Guided prompts progress from simple retrieval ("What are the safety training requirements?") to cross-referencing ("Does our vendor contract with Acme align with what we're actually ordering from them?" — combining document AI with database queries). | Hands-on |
| 52-62 | **Reliability of Document AI.** RAG-specific failure modes: retrieval misses (the answer exists but wasn't retrieved), hallucinated citations (the AI cites a passage that doesn't say what it claims), context window limits (the document is too long), and stale documents (the policy was updated but the index wasn't). Verification protocol: always check the cited passage, not just the summary. | Lecture + demo |
| 62-78 | **Deploying RAG.** The same deployment questions from Sessions 3-4 apply, plus RAG-specific decisions. **Embedding models:** cloud (OpenAI, Cohere, Voyage) vs. open-source (run locally, data stays on-premise) — the same cloud-vs-local tradeoff as the LLM itself. **Vector stores:** managed services (Pinecone, Weaviate Cloud) vs. self-hosted (pgvector in your existing Postgres, Chroma, Qdrant). **Document ingestion pipeline:** how do new documents get into the system? Someone must handle PDF parsing, chunking strategy (too small = lost context, too large = irrelevant noise), metadata tagging, and freshness — when a policy is updated, the old version must be replaced, not duplicated. **Access control:** the RAG system must enforce the same document permissions as your file server — legal memos visible only to legal, HR policies scoped by division. **The build-vs-buy landscape:** turnkey RAG platforms (Glean, Guru, Microsoft Copilot for M365) vs. custom builds. Turnkey platforms handle ingestion and permissions but lock you into their chunking and retrieval logic. | Lecture + Q&A |
| 78-88 | **Breakout: Where Is Knowledge Trapped? (groups of 3-4).** What knowledge in your company is trapped in documents — policies, contracts, procedures, regulatory filings, past analyses? Each person names 2-3 document collections that would benefit from AI-powered Q&A. Compare across the group: what types of documents came up repeatedly? What access control challenges are common? Each group reports back: the most valuable document AI use case they identified and the biggest deployment obstacle. | Breakout rooms |
| 88-90 | Capstone preview and homework | Wrap |

**Homework:** Finalize your strategy document (1-2 pages using the template). Prepare a 5-minute presentation. Required sections: the problem, the solution (database AI, document AI, or both), deployment architecture (LLM, code execution, data security, and — if applicable — RAG infrastructure), the 90-day pilot plan, governance requirements, success metrics, the ask, and the Day 1 action.

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
| 70-82 | **Synthesis: What You Now Know.** (1) AI agents turn plain English into data answers — replacing dashboards, manual reports, and the wait for analyst time. (2) The technology is simpler than you expected (50 lines), but production requires governance, verification, and organizational readiness. (3) Document AI and database AI are complementary — together they cover structured and unstructured company knowledge. (4) The critical skill is not building AI tools — it's asking the right questions and verifying the answers. | Lecture |
| 82-88 | **Monday Morning Actions.** Four things every executive can do regardless of role: (a) audit your reporting workflows — which ones follow the data → analysis → deliverable pattern and could be automated? (b) scope a 30-day discovery sprint on one data access use case, (c) inventory the document collections that would benefit from AI-powered Q&A, (d) establish an AI governance framework before shadow IT does it for you. | Lecture |
| 88-90 | Close. Resources for continued learning. Optional 30-day follow-up session to report on progress. | Wrap |

---

## Cross-Session Summary

| Session | Title | Primary Activity | Theme |
|---|---|---|---|
| 1 | Exploring Data with AI | First app experience + guided queries | Single-system data access |
| 2 | Our Data Is Everywhere | Cross-system demo + ROI template | Multi-system integration |
| 3 | How Does This Work? | Agent loop + code execution architecture + optional build | Orchestration and deployment |
| 4 | From Data to Deliverable | Pipeline demo + LLM deployment + data security | Reporting pipelines and architecture |
| 5 | Can You Trust It? | Failure demos + red-teaming + governance | Reliability and compliance |
| 6 | AI as Thinking Partner | Strategic reasoning + stress-testing | AI-assisted decision making |
| 7 | Document AI | RAG demo + RAG deployment + document Q&A | Unstructured knowledge and RAG architecture |
| 8 | Your AI Strategy | Capstone presentations + synthesis | Integration |

## Recurring Elements

- **ROI Template:** Introduced Session 2, updated Sessions 4 and 7, underpins the capstone.
- **Breakout Rooms:** Sessions 1, 2, 4, 5, 7, 8. Sessions 2/4/5/7 use a "how does this work at your company?" format where students compare corporate realities and report patterns back to the group — surfacing deployment knowledge the instructor can't provide.
- **Hands-on with the App:** Sessions 1-7 — every session includes live interaction with the Meridian app.
- **Linux Server:** Available throughout for self-paced exploration; demonstrated in Session 3; exercises are optional homework.
- **Maker/Checker Theme:** Introduced Session 5, reinforced in Sessions 6-7 — the core skill shift.
- **Deployment Architecture Thread:** Code execution (Session 3), LLM deployment and data security (Session 4), RAG deployment (Session 7) — builds a complete picture of what production requires.

## Capstone Template (provided to students)

1. **The Problem:** What question can't be answered today? What does it cost? (from ROI template)
2. **The Solution:** Database AI, document AI, or both — which systems and document collections, build/buy/extend decision
3. **Deployment Architecture:** LLM (cloud API vs. on-premise), code execution (cloud sandbox vs. own containers), data security approach, and — if applicable — RAG infrastructure (embedding model, vector store, document pipeline)
4. **The 90-Day Pilot:** Team (who), data (which systems/documents), timeline (week-by-week), governance minimum
5. **Success Metrics:** Time-to-insight, analyst leverage, error reduction, adoption rate
6. **Risks and Mitigations:** Data quality, data security, organizational resistance, vendor lock-in, regulatory
7. **The Ask:** Budget, headcount, executive sponsor
8. **Day 1 Action:** The one thing you will do Monday morning

## Alignment with Advertised Outcomes

| Advertised Outcome | Where Covered |
|---|---|
| Analyze data and produce reports using AI agents | Sessions 1-2 (queries), Session 4 (reporting pipelines) |
| Connect AI to corporate databases | Session 3 (agent loop, code execution, database connections) |
| Build automated reporting pipelines | Session 4 (full pipeline, deployment architecture) |
| Deploy document-based AI with citations | Session 7 (RAG implementation and deployment) |
| Evaluate reliability, compliance, and governance | Session 5 (dedicated session) + Session 7 (RAG reliability) |
| Understand deployment and data security | Session 3 (code execution), Session 4 (LLM deployment, data security), Session 7 (RAG deployment) |
