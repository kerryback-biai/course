# Course Design v3: From BI to AI — Data-Driven Decision Making with Agentic AI
## An 8-Session Executive Program (4 weeks, 90 min each, Zoom)

### Course Description

AI agents that understand plain English, query your data, and deliver answers in seconds are transforming how organizations make decisions. In this four-week program, you will use an AI agent to query a simulated enterprise, build reporting pipelines, deploy document-based AI, and evaluate reliability and governance requirements — all hands-on, no coding required. You will leave equipped with tools you can immediately deploy and a concrete strategy for bringing AI-powered data access to your organization.

### Pre-Program Video

Before Session 1, participants watch a 15-20 minute video covering:
- What AI agents are and why they matter for data-driven decision making
- The Meridian Corp simulation: a $500M distributor with 10 enterprise systems across 3 divisions
- The Linux VM: an optional hands-on environment for those who want to build agents themselves
- The course arc: a session-by-session overview so students know where they're headed
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

### Recorded Demos (optional, for deeper understanding)

Seven pre-recorded demos show the full build journey from a blank file to a production-style system. Each is recorded on the Linux VM using the same environment students have access to. Students who want to replicate any demo can SSH in and follow along. Links are provided in the homework for the paired session.

**Demo 1: "Hello World Agent" (~15 min)** — *pairs with Session 3*
Start from an empty file. Tell Claude Code in English to build a Python script that takes a question, sends it to Claude with a schema description, gets back SQL, runs it against a parquet file, and prints the answer. Show the ~50 lines it produces. Run it. Ask a question. Get an answer. The student sees the entire agent loop created from a plain English description. (This is a clean recording of the live Session 3 demo.)

**Demo 2: "Adding a Second System" (~15 min)** — *pairs with Sessions 2-3*
Start from the Demo 1 agent. Tell Claude Code to add a second database (Workday HR) so the agent can query both and merge. Show the agent deciding to query CRM + Workday for "revenue per employee by division." Show the fuzzy matching problem when customer names don't align. The cross-system merge from Session 2 becomes visible in code the student can read.

**Demo 3: "Wrapping It in a Web App" (~15 min)** — *pairs with Session 4*
Start from the Demo 2 agent. Tell Claude Code to wrap it in a simple web app with a chat interface. Claude Code generates a FastAPI backend + HTML frontend. Open a browser, type a question, get an answer with a chart. The student goes from a script to something that looks like the Meridian app in under an hour of total work.

**Demo 4: "Building a Reporting Pipeline" (~20 min)** — *pairs with Session 4*
Tell Claude Code to build a script that queries revenue by division, compares to prior quarter, generates a chart, writes a narrative summary, and saves it as a formatted report. Show the pipeline running end to end. Then show scheduling it to run weekly and adding a human review gate — the report is drafted but held for approval before distribution. The "ad hoc to automated" transition from Session 4 becomes concrete.

**Demo 5: "Red-Teaming Your Agent" (~15 min)** — *pairs with Session 6*
Start from the Demo 2 agent (no guardrails). Try SQL injection, ask for salary data, ask about nonexistent divisions. Show what fails — the agent returns individual salaries, doesn't validate SQL, hallucinates when data doesn't exist. Then add guardrails one by one: SQL validation, row limits, access control checks, "I don't know" responses. Guardrails aren't automatic — seeing the vulnerabilities firsthand makes the Session 6 governance discussion real.

**Demo 6: "Building a RAG System" (~20 min)** — *pairs with Session 7*
Start fresh with a folder of Meridian Corp documents (employee handbook, vendor contracts, compliance policies). Tell Claude Code to build a document Q&A system: chunk the PDFs, embed them, store in a vector database, and answer questions with cited passages. Show the full pipeline: PDF parsing → chunking → embedding (discuss model choice) → vector store (Chroma or pgvector). Ask questions and get answers with page citations. Then show a failure: a question where chunking split a relevant passage, demonstrating how chunk size affects retrieval quality.

**Demo 7: "Combining Database + Document AI" (~15 min)** — *pairs with Session 7*
Combine the Demo 2 database agent with the Demo 6 RAG system. Ask: "What's our contractual commitment to GE, and how does their actual spending compare?" RAG retrieves the contract terms; the database agent pulls spending data; the LLM synthesizes both. Show the orchestration: two retrieval paths (vector search vs. SQL), results merged by the LLM. This is the full vision — structured and unstructured company knowledge, accessible through one interface.

### Instructor Note: Demo Fallbacks

Pre-record fallback versions of the highest-risk live demos (Session 1 Dashboard vs. Chat, Session 2 Cross-System Merge, Session 4 Full Pipeline, Session 7 RAG Q&A). If the Meridian app or Claude API is down during a Zoom session, switch to the recording and narrate over it.

---

## Session-by-Session Outline

---

### SESSION 1: "Exploring Data with AI"
**Week 1 / Tuesday — From Questions to Answers in Seconds**

**Learning objectives:**
- Understand why AI agents matter now — the market signal and the opportunity
- Experience conversational data access vs. traditional dashboards
- Ask business questions in plain English and get instant answers with charts

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-15 | **Course Overview and the "Why Now."** Welcome. Quick recap of what the pre-program video covered — the Meridian simulation, the Linux VM, and what you'll be able to do by Session 8. Then the context: in February 2026, AI agents wiped $2 trillion from software company valuations. Investors decided that AI can replace large categories of enterprise software — BI dashboards, workflow tools, reporting layers, Tier 1 support. Whether or not you agree with the market's verdict, the technology behind it is real, and it's what we'll be working with for the next four weeks. This course teaches you to use it, understand how it works, evaluate its reliability, and build a strategy for deploying it. Questions about the course arc or logistics. | Lecture + Q&A |
| 15-20 | **Cold open.** A CEO asks "which of our customers buy from multiple divisions?" The BI team says 3 weeks. Show the email chain. Ask: has this happened to you? | Provocation + discussion |
| 20-28 | **Demo: Dashboard vs. Chat.** Open the Meridian Corp app and ask the same question. Get an instant answer. Ask follow-ups the dashboard can't handle. Students see SQL, charts, narrative — all from a chat interface. | Live demo |
| 28-38 | **The Business Lens.** Connect the demo back to the $2T question. The technology you just saw — querying enterprise data in plain English, getting instant charts and narratives — is what the market believes will displace dashboards, reporting teams, and data integration tools. If anyone in your company could do what you just saw, what changes? What decisions get made faster? What decisions get made that weren't being made at all? | Lecture + discussion |
| 38-58 | **Hands-on: Your First Queries.** Students log into the app and work through 8-10 guided prompts against single systems — Salesforce pipeline queries, NetSuite financial summaries, Workday headcount breakdowns. Prompts progress from simple ("How many open deals are in Salesforce?") to analytical ("Which sales rep has the highest win rate this quarter?"). | Hands-on |
| 58-70 | **Open Exploration.** Students ask their own questions. Challenge: find something surprising in the data. Instructor highlights interesting discoveries in real time. | Hands-on |
| 70-85 | **Breakout Discussion (groups of 3-4).** What surprised you? What would this look like at your company? Who answers these questions today and how long does it take? Each group shares one insight. | Breakout rooms |
| 85-90 | Homework assignment | Wrap |

**Homework:** Log into the Meridian app and ask 10 business questions of your choosing against any single system. Write down one question the agent answered well and one where it was unsatisfying or wrong. Bring both to Session 2.

---

### SESSION 2: "Our Data Is Everywhere"
**Week 1 / Thursday — The Cross-System Problem**

**Learning objectives:**
- Understand why enterprise data is scattered and why consolidation costs millions
- Watch AI query multiple systems and merge results in real time
- Map their own company's data landscape and identify high-value use cases

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Homework debrief.** 3-4 students share best answer and worst answer. Why was the bad answer bad? (Usually: data is in another system.) | Discussion |
| 10-30 | **Demo: The Cross-System Merge.** Ask: "Which customers buy from multiple divisions?" Watch the agent query Salesforce, Legacy CRM, HubSpot separately, merge with Python using fuzzy matching. Then: "Revenue per employee by division?" — queries CRMs + Workday, merges. Agent shows SQL, explains matching, flags data quality issues. | Live demo |
| 30-42 | **How Data Moves Today.** APIs, integration platforms (MuleSoft), ETL/data warehouses, and CSV exports. The traditional answer is a warehouse ($500K-5M, 6-18 months). The alternative: query each system where it lives. Both have tradeoffs — warehouses are the default for good reasons (consistency, audit trail). | Lecture |
| 42-58 | **Hands-on: Cross-System Exploration.** Students try cross-system queries. Guided prompts + open exploration. Include a timed challenge: "Which division's top customer is most at risk of churning?" (requires CRM + Zendesk data). | Hands-on (competitive element) |
| 58-68 | **Workshop: Your Company's Data Map.** Each student sketches their company's 3-5 core systems and identifies one cross-system question nobody can answer easily today. Who answers it now? How long does it take? This data map carries forward — it becomes the foundation for your capstone strategy. | Individual work |
| 68-82 | **Breakout: How Scattered Is Your Data? (groups of 3-4).** Compare data maps. What systems do you have in common? Where is integration hardest? What cross-system questions would have the most business value? Each group reports back: one pattern that was common across companies and one surprising idiosyncrasy. | Breakout rooms |
| 82-88 | **What We're Skipping.** Before any agent can query real systems, someone must: catalog the data, document schemas, provision API access, classify PII. This is 60-90 days of pre-work that the demo does not show. Name it now so expectations are calibrated. | Lecture |
| 88-90 | Homework | Wrap |

**Homework:** (1) Read enterprise systems background document. (2) Complete your data map: list at least 5 systems your company uses and the top 3 cross-system questions you can't answer today.

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
| 72-85 | **Live Walkthrough: Building an Agent from Scratch.** The instructor builds a simple agent in real time on the Linux server using Claude Code, narrating each step. Students watch the 50-line agent come to life in minutes — from English instructions to working code. This is the "your developer could do this" moment. Students who want to replicate this themselves can follow the same steps on their server accounts later (Exercise 1). | Live demo (instructor-driven) |
| 85-90 | Homework | Wrap |

**Homework:** (1) For those who want hands-on experience: SSH credentials are provided. Exercise 1 (hello-world agent) and Exercise 2 (multi-system agent) are on the server with starter templates. Claude Code will help you — you direct it in English. This is optional but recommended. *Optional viewing: Demos 1-2 walk through building these agents step by step.* (2) Required: For the use case you identified in Session 2, what data quality issues would you expect to encounter? What pre-work is needed before an agent could query your systems?

**Note:** The Linux server exercises are available throughout the course for self-paced exploration. They are not required but provide deeper understanding for those who want it.

---

### SESSION 4: "From Data to Deliverable"
**Week 2 / Thursday — Reporting Pipelines**

**Learning objectives:**
- See the full pipeline: data → chart → narrative → board-ready memo
- Understand how to chain AI steps into automated reporting workflows
- Produce a complete deliverable and iterate on quality

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Check-in.** Anyone try the Linux server exercises? Quick show. Share struggles and surprises. | Discussion |
| 10-25 | **Demo: The Full Pipeline.** Ask the Meridian app: "Prepare a quarterly executive summary of Meridian Corp performance — revenue by division, headcount efficiency, top customer risks, and supply chain issues." Watch it query 6 systems, merge data, generate charts, and produce a structured memo. This is the "last mile" — not just data, but a delivered artifact. | Live demo |
| 25-38 | **Anatomy of a Reporting Pipeline.** Break down what just happened into discrete steps: (1) query multiple systems, (2) clean and merge, (3) compute metrics, (4) generate charts, (5) write narrative, (6) assemble into a document. Each step can be customized, templated, and reused. Show how changing one instruction ("compare to prior quarter" → "traffic-light format with red/yellow/green") reruns the entire pipeline with a different deliverable. | Lecture + demo |
| 38-43 | **Demo: The Art of Iteration.** Ask the Meridian app for a quarterly memo — get back something generic. Resubmit: "Make this a traffic-light format with red/yellow/green for each division." Show the difference. Again: "Make this one page, not two, and lead with the biggest risk." Show how prompt specificity drives output quality. Students now have a vocabulary for iteration: format, tone, length, focus. | Live demo |
| 43-60 | **Hands-on: Build Your Own Report.** Students use the Meridian app to produce specific deliverables. Three guided exercises of increasing complexity: (1) "Create a customer risk report combining CRM pipeline data with support ticket trends." (2) "Produce a division-level P&L comparison with commentary on headcount efficiency." (3) "Generate a board-ready memo comparing Q3 and Q4 performance across all three divisions with charts." Iterate on prompts using the techniques from the demo. | Hands-on |
| 60-72 | **From Ad Hoc to Automated.** In production, these pipelines run on schedules: Monday morning dashboard refresh, monthly board deck, weekly sales forecast. Architecture: the same agent loop, triggered by a cron job instead of a chat message. What changes: error handling, version control, human review gates — a human approves the draft before it goes out. | Lecture |
| 72-85 | **Workshop: Your Reporting Candidates.** Each student identifies 2-3 recurring reports at their company that follow this pattern (data → analysis → deliverable). For each: what systems feed it, who builds it today, how long does it take, what would automation look like? | Workshop |
| 85-90 | Homework | Wrap |

**Homework:** (1) Use the Meridian app to produce one complete deliverable of your choosing — a memo, a comparison, a risk assessment. Save or screenshot the output. Bring it to Session 5. (2) **Pre-reading for Session 5** (three readings, ~30 min total): (a) Morgan Stanley case study (provided) — a regulated financial firm's deployment decision. Come prepared to discuss: what constraints did they face, what did they choose, and what surprised them? (b) [a16z: "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025"](https://a16z.com/ai-enterprise-2025/) — real data on how enterprises are deploying LLMs and the shift from building to buying. (c) [DUNNIXER: "6 AI Vendor Evaluation Dimensions for Enterprise RFPs"](https://www.dunnixer.com/insights/articles/the-six-dimensions-of-ai-vendor-evaluation-that-matter-most) — a practical scorecard framework for evaluating AI vendors. Keep this one — it's the tool you'll use for vendor evaluation going forward. *Optional viewing: Demos 3-4 show building a web app and an automated reporting pipeline.*

---

### SESSION 5: "What Does Deployment Look Like?"
**Week 3 / Tuesday — Architecture, Data Security, and Build vs. Buy**

**Learning objectives:**
- Understand LLM deployment options and their tradeoffs (cloud API vs. on-premise)
- Grasp the data security problem: what the LLM sees and how to control it
- Evaluate build vs. buy vs. extend for AI capabilities

**Pre-reading assigned in Session 4 homework (~30 min):**
- Morgan Stanley case study — deployment decisions in regulated finance
- a16z: "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025" — landscape data
- DUNNIXER: "6 AI Vendor Evaluation Dimensions for Enterprise RFPs" — vendor scorecard (keep this one as a reference tool)

Students arrive having read the concepts. Session time is discussion, demo, and application — not lecture.

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-8 | **Homework debrief.** Students share the deliverable they produced. What looked right? What would you want to verify before sending to your board? | Discussion |
| 8-20 | **Case Study: Morgan Stanley.** Debrief the pre-reading. Morgan Stanley chose cloud API with a zero data retention agreement for 16,000 financial advisors under SEC/FINRA constraints. Key questions to the room: Was this the right call? The a16z survey says 90% of enterprises are testing third-party AI for customer support — does that match your experience? What would your company have done differently, and why? | Discussion |
| 20-25 | **Bridge from Session 3.** "Last week we asked: where does the code that queries your database run? Today: where does the *LLM that interprets those results* run? These are two separate decisions. You can run code on your servers and still send query results to the vendor's servers for interpretation. Or you can keep both local — but with a smaller model and lower quality. You read about the three options. Let's see the security problem in action." | Lecture |
| 25-33 | **Demo: Data Security in Action.** Ask the Meridian app for individual salary data — watch it return results. Then switch to a version with guardrails enabled: the same question is blocked or returns only aggregates. Pause: "This is the problem the four data security approaches address. Which approach did Morgan Stanley use?" | Live demo + discussion |
| 33-45 | **Discussion: Deployment Options and Data Security.** The readings covered three LLM deployment options (cloud API, on-premise, hybrid) and you've now seen the data security problem live. Quick poll: which option fits your company? Then discuss: what surprised you in the a16z data? What's the gap between where CIOs say they're heading and where your company actually is? Instructor fills in gaps as needed — cost comparison (cloud ~$0.01-0.05/query vs. on-premise $50-200K+ upfront), the four data security approaches (aggregated results with DLP, blind templates, on-premise LLM, schema-only), and why this is a policy decision, not a technology problem. | Discussion + lecture as needed |
| 45-58 | **Build vs. Buy: Applying the DUNNIXER Framework.** Students read the 6-dimension scorecard. Now apply it: walk through one specific vendor (Salesforce Agentforce) together — what it does today, what it costs, where it falls short. Score it on 2-3 of the DUNNIXER dimensions as a group exercise. Then: the real decision matrix — buy from incumbent (lowest risk), buy from AI-native startup (highest capability), build internally (highest control), or hybrid. Most enterprises land on hybrid. | Discussion + group exercise |
| 58-72 | **Breakout: Your Deployment Decisions (groups of 3-4).** For your identified use case: which LLM deployment option fits? Which data security approach? Build, buy, or hybrid? Use the DUNNIXER dimensions to justify your choice. Each group reports back: what constraints were common, and where did industry differences lead to different answers? | Breakout rooms |
| 72-85 | **Hands-on: Your Deployment Profile.** Each student writes down their deployment profile for their capstone use case: LLM deployment option, data security approach, build-vs-buy decision with rationale. Instructor circulates and advises. | Individual work |
| 85-90 | Preview Week 3 continued (trust and verification) | Wrap |

**Homework:** (1) Read the Air Canada case study (provided). A chatbot hallucinated a refund policy and the company was held legally liable. Come prepared to discuss: who was responsible? What verification would have caught this? (2) For your identified use case: what governance requirements would your compliance team impose? Write down your top 3 concerns. *Optional viewing: Demo 5 shows red-teaming an agent and adding guardrails.*

---

### SESSION 6: "Can You Trust It?"
**Week 3 / Thursday — Reliability, Verification, and Governance**

**Learning objectives:**
- Identify failure modes of AI data agents (hallucination, wrong joins, misleading aggregations)
- Apply the maker/checker framework: AI produces, human verifies
- Understand data governance and regulatory requirements for AI agents

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-12 | **Case Study: Air Canada.** Debrief the pre-reading. A chatbot hallucinated a bereavement fare policy, the customer relied on it, and the company was held legally liable. Key questions: Who was responsible — the AI vendor, the airline, or the team that deployed the chatbot without verification? What would have caught this? How does this map to your governance concerns from homework? | Discussion |
| 12-28 | **Demo: When the Agent Gets It Wrong.** Three pre-prepared failures: (a) averages across won and lost deals without filtering — technically correct SQL, misleading answer; (b) cross-division revenue comparison with date format mismatch — Legacy CRM VARCHAR dates cause wrong aggregation; (c) customer count that double-counts due to fuzzy matching failures. Walk through each, show the SQL, identify the error. Connect back to Air Canada: the chatbot's error was the same category — plausible-sounding output that nobody verified. | Live demo |
| 28-38 | **The Maker/Checker Framework.** AI is the maker; you are the checker. The skill shift: from producing analysis to verifying it. What to check: source system, filters, join logic, date ranges, NULL handling, row counts. The agent shows SQL for a reason — transparency is a feature. Who in your organization has the judgment to be an effective checker? | Lecture + discussion |
| 38-55 | **Hands-on: Red-Team the Meridian App.** Students try to break the agent through the chat interface. Guided attack scenarios plus open exploration: (a) ask for data you shouldn't see (individual salaries by name), (b) ask a question where the data doesn't exist (2027 revenue), (c) try to trick it into hallucinating ("What was our revenue from the Atlantis division?"), (d) ask a question with a plausible but misleading framing ("Which division is most profitable?" without defining profit), (e) ask the same question twice and compare answers for consistency. Then 5 minutes of open red-teaming: try anything. Record what happens. | Hands-on |
| 55-60 | **Debrief: What Did You Find?** Quick share-out: what attacks worked? What surprised you? Any creative attacks beyond the guided list? | Discussion |
| 60-73 | **Data Governance and Regulatory Exposure.** Who is liable when the agent gives wrong financial data? Does agent output count as a "record" under SOX? GDPR implications of cross-system queries that combine PII from multiple sources. Role-based access control: the VP of Sales should not see HR compensation data, even if the agent can query both systems. Governance is not a technology problem — it's an organizational decision about acceptable risk, enforced through technical controls. | Lecture + Q&A |
| 73-85 | **Breakout: Your Governance Requirements (groups of 3-4).** Given your industry and regulatory environment, what guardrails would you require before deploying an AI agent? What's the minimum viable governance framework? Each group reports back: what governance requirements were universal vs. industry-specific? Where would adoption stall without executive air cover? | Breakout rooms |
| 85-90 | Homework | Wrap |

**Homework:** (1) Read the Atherton Financial case study (provided). A wealth management firm deployed document AI and hit chunking, access control, and staleness failures. Come prepared to discuss: what would you have done differently? (2) Begin drafting your capstone strategy (template and evaluation rubric provided): problem statement, proposed solution, deployment approach, 90-day pilot plan. (3) For your identified use case: write down the three most likely failure modes and how you'd mitigate each. *Optional: If you've been working through the Linux server exercises, Exercise 4 (red-teaming) directly applies to today's session. Optional viewing: Demo 5 shows red-teaming an agent and adding guardrails.*

---

### SESSION 7: "Document AI — Answers from Your Own Files"
**Week 4 / Tuesday — Retrieval-Augmented Generation (RAG)**

**Learning objectives:**
- Understand how AI can answer questions grounded in company documents with citations
- Distinguish database AI (structured data queries) from document AI (unstructured text retrieval)
- Experience RAG hands-on and understand deployment decisions

**Session flow:**

| Min | Segment | Format |
|---|---|---|
| 0-10 | **Bridge + Atherton Case Debrief.** "So far we've worked with structured data — databases, tables, SQL. But most company knowledge isn't in databases. It's in policies, contracts, emails, and slide decks. Today we add a second capability." Quick debrief of the Atherton Financial case study: they deployed document AI and hit chunking failures, access control gaps, and stale documents. What would you have done differently? This frames what to watch for in today's demos and hands-on. | Lecture + discussion |
| 10-22 | **Demo: Document-Based Q&A.** Pre-loaded document collection for Meridian Corp: employee handbook, vendor contracts, compliance policies, board minutes. Ask: "What is our policy on remote work for the Energy Division?" "Which vendor contracts are up for renewal in Q2?" "What did the board approve regarding the Safety Division expansion?" Answers come with citations — page numbers and quoted passages. Then the combined question: "What's our contractual commitment to GE, and how does their actual spending compare?" — RAG for the contract, database agent for the spending. | Live demo |
| 22-32 | **How RAG Works.** The retrieval-augmented generation pipeline: (1) documents are chunked into passages, (2) an embedding model converts each chunk into a numerical vector, (3) chunks are stored in a vector database, (4) the user's question is embedded the same way and matched against stored chunks, (5) the top matches are sent to the LLM as context, (6) the LLM answers using only the retrieved context. Compare to database agents: RAG handles *unstructured* text; database agents handle *structured* data. Both are tools in the same toolkit. | Lecture |
| 32-52 | **Hands-on: Query the Document Collection.** Students ask questions of the Meridian document set. Three rounds: (1) Simple retrieval — "What are the safety training requirements?" "What's the PTO policy for the Energy Division?" (2) Cross-document — "How do the vendor contract terms for our top 3 suppliers compare?" (3) Cross-system — "Does our vendor contract with Acme align with what we're actually ordering from them?" (combining document AI with database queries). Students note which answers include citations and which don't. | Hands-on |
| 52-62 | **Reliability of Document AI.** RAG-specific failure modes: retrieval misses (the answer exists but wasn't retrieved), hallucinated citations (the AI cites a passage that doesn't say what it claims), context window limits (the document is too long), and stale documents (the policy was updated but the index wasn't). Live demo: ask a question where chunking split a relevant passage — show the partial answer and explain why. Verification protocol: always check the cited passage, not just the summary. The maker/checker framework applies to documents just as it does to data. | Lecture + demo |
| 62-75 | **Deploying RAG.** The deployment framework from Session 5 (cloud vs. on-premise, build vs. buy) applies here — we won't repeat it. What's *new* for document AI: **Document ingestion** — how do documents get into the system? Someone must handle PDF parsing, chunking strategy (by section for policies, by clause for contracts — not one-size-fits-all), and freshness — when a policy is updated, the old version must be replaced, not duplicated. The Atherton case showed what happens when freshness isn't managed. **Access control** — the RAG system must enforce the same document permissions as your file server — legal memos visible only to legal, HR policies scoped by division. Atherton's oversharing problem is the cautionary tale. **The build-vs-buy landscape** for document AI specifically: turnkey RAG platforms (Glean, Guru, Microsoft Copilot for M365) handle ingestion and permissions out of the box but limit customization. Custom builds offer more control but require engineering resources. | Lecture + Q&A |
| 75-87 | **Breakout: Where Is Knowledge Trapped? (groups of 3-4).** What knowledge in your company is trapped in documents — policies, contracts, procedures, regulatory filings, past analyses? Each person names 2-3 document collections that would benefit from AI-powered Q&A. Compare across the group: what types of documents came up repeatedly? What access control challenges are common? What deployment approach fits (managed vs. self-hosted)? Each group reports back: the most valuable document AI use case they identified and the biggest deployment obstacle. | Breakout rooms |
| 87-90 | Capstone preview and homework | Wrap |

**Homework:** Finalize your strategy document (1-2 pages using the capstone template). Prepare a 5-minute presentation. The evaluation rubric is included with the template — use it to self-check before presenting. *Optional viewing: Demos 6-7 show building a RAG system and combining it with a database agent.*

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
| 30-70 | **Plenary presentations.** 5 winning strategies presented to the full class (5 min each + 3 min Q&A/feedback). Instructor feedback on: is the pilot scoped tightly enough? Is the business case credible? Is the governance plan adequate? Does the Day 1 action actually happen on Day 1? | Presentations |
| 70-80 | **Synthesis: What You Now Know.** (1) AI agents turn plain English into data answers — replacing dashboards, manual reports, and the wait for analyst time. (2) The technology is simpler than you expected (50 lines), but production requires governance, verification, and organizational readiness. (3) Document AI and database AI are complementary — together they cover structured and unstructured company knowledge. (4) The critical skill is not building AI tools — it's asking the right questions and verifying the answers. | Lecture |
| 80-84 | **Beyond Data: AI as Thinking Partner.** One final capability. Live demo: ask the Meridian app not "What were Q4 sales?" but "I'm considering expanding the Energy Division into the Southeast — based on our pipeline, customer concentration, and support ticket trends, what are the top 3 risks?" The agent reasons across data, not just retrieves it. This is where AI moves from analyst to advisor — and where your judgment matters most, because the AI will anchor on whatever framing you provide. | Live demo |
| 84-88 | **Monday Morning Actions.** Four things every executive can do regardless of role: (a) audit your reporting workflows — which ones follow the data → analysis → deliverable pattern and could be automated? (b) scope a 30-day discovery sprint on one data access use case, (c) inventory the document collections that would benefit from AI-powered Q&A, (d) establish an AI governance framework before shadow IT does it for you. | Lecture |
| 88-90 | Close. Resources for continued learning. Optional 30-day follow-up session to report on progress. | Wrap |

---

## Cross-Session Summary

| Session | Title | Primary Activity | Theme |
|---|---|---|---|
| 1 | Exploring Data with AI | First app experience + guided queries | Single-system data access |
| 2 | Our Data Is Everywhere | Cross-system demo + data map | Multi-system integration |
| 3 | How Does This Work? | Agent loop + code execution architecture + live build | Orchestration and code execution |
| 4 | From Data to Deliverable | Full pipeline demo + hands-on reporting | Reporting pipelines |
| 5 | What Does Deployment Look Like? | LLM deployment + data security + build vs. buy | Architecture and deployment |
| 6 | Can You Trust It? | Failure demos + red-teaming + governance | Reliability and compliance |
| 7 | Document AI | RAG demo + hands-on document Q&A + RAG deployment | Unstructured knowledge |
| 8 | Your AI Strategy | Capstone presentations + synthesis | Integration |

## Recurring Elements

- **Data Map → Capstone:** Students sketch their company's data landscape in Session 2 and build on it through the capstone strategy in Session 8.
- **Breakout Rooms:** Sessions 1, 2, 5, 6, 7, 8. Sessions 2/5/6/7 use a "how does this work at your company?" format where students compare corporate realities and report patterns back to the group — surfacing deployment knowledge the instructor can't provide.
- **Hands-on with the App:** Sessions 1-4, 6-7 — most sessions include hands-on interaction with the Meridian app. Session 5 includes a data security demo and individual deployment profile work.
- **Linux Server:** Available throughout for self-paced exploration; live build in Session 3; exercises are optional homework.
- **Deployment Architecture Thread:** Code execution (Session 3), LLM deployment and data security (Session 5), RAG deployment (Session 7) — builds a complete picture of what production requires.
- **Case Studies:** Morgan Stanley AI Assistant (Session 5 — deployment decisions in regulated finance), Air Canada chatbot (Session 6 — governance failure and legal liability), Atherton Financial RAG deployment (Session 7 — document AI challenges). Each assigned as pre-reading and debriefed at the start of the paired session.

## Capstone Template (provided to students)

1. **The Problem:** What question can't be answered today? What's the business impact?
2. **The Solution:** Database AI, document AI, or both — which systems and document collections, build/buy/extend decision
3. **Deployment Approach:** Cloud vs. on-premise vs. hybrid; data security approach; for document AI, managed platform vs. custom build
4. **The 90-Day Pilot:** Team (who), data (which systems/documents), timeline (week-by-week), governance minimum
5. **Success Metrics:** Time-to-insight, decisions enabled, error reduction, adoption rate
6. **Risks and Mitigations:** Data quality, data security, regulatory requirements
7. **The Ask:** Budget, headcount, executive sponsor
8. **Day 1 Action:** The one thing you will do Monday morning

## Capstone Evaluation Rubric (shared with students in Session 6 homework)

| Dimension | Strong | Needs Work |
|---|---|---|
| **Pilot scope** | One use case, 1-3 systems, clear success metric | Too broad ("transform our data culture") or too vague |
| **Deployment approach** | Specific choice (cloud/on-premise/hybrid) with rationale tied to their industry | Generic or no justification |
| **Success metrics** | Measurable KPIs tied to business impact (e.g., "reduce forecast time from 3 days to 2 hours") | Vague ("improve efficiency") or no metrics |
| **Governance** | Minimum viable framework identified (access control, verification, audit) | Governance mentioned but not specific |
| **Risk mitigation** | Specific mitigations with clear owners, not just named risks | Risks listed without actionable mitigations |
| **Day 1 action** | Specific person, task, and date | Aspirational ("we should explore...") |

## Alignment with Advertised Outcomes

| Advertised Outcome | Where Covered |
|---|---|
| Analyze data and produce reports using AI agents | Sessions 1-2 (queries), Session 4 (reporting pipelines) |
| Connect AI to corporate databases | Session 3 (agent loop, code execution, database connections) |
| Build automated reporting pipelines | Session 4 (full pipeline, hands-on report building) |
| Deploy document-based AI with citations | Session 7 (RAG implementation, hands-on, deployment) |
| Evaluate reliability, compliance, and governance | Session 6 (dedicated session with expanded red-teaming) |
| Understand deployment and data security | Session 3 (code execution), Session 5 (LLM deployment, data security, build vs. buy), Session 7 (RAG deployment) |
