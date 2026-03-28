# Course Design: AI for Enterprise Data

## Unified Narrative: "From Question to Answer"

Two themes, same story at different scales:
- **Theme 1** (dashboards → natural language): "I shouldn't have to wait for someone to build me a report"
- **Theme 2** (cross-system integration): "I shouldn't have to wait for someone to build me a data warehouse"

Both are about eliminating the middleman between a business question and an answer.

## Four-Week Structure

### Week 1: The Single-System Problem
You have data in one system but getting answers requires a BI team, a dashboard backlog, and weeks of waiting.

**Key demo:** Natural language queries against a single database, instant charts, written memos. The "replace dashboards" pitch.

**Exercise:** Ask 10 business questions, get instant answers.

### Week 2: The Multi-System Problem
Real companies don't have one database. They have 10. Getting a cross-functional answer (revenue per employee, customer profitability including support costs) currently requires a data warehouse project.

**Key demo:** The AI agent querying Salesforce + Workday + NetSuite separately and merging with Python. The "aha" moment is watching it do in 30 seconds what would normally take a data team weeks.

**Exercise:** "Consolidated revenue by customer" across divisions.

### Week 3: Trust and Verify
The hard problems. Customer names don't match. Dates are in different formats. Account codes differ. How do you verify the AI's work? Red-teaming, verification protocols, the "maker/checker" framework.

**Key insight:** AI doesn't eliminate the need for judgment — it shifts the work from *producing* analysis to *verifying* it.

**Exercise:** Red-team the agent, catch errors, verify claims.

### Week 4: Build the Business Case
How does their company actually adopt this? Architecture decisions, governance, build vs. buy, organizational change.

**Key demo:** Full pipeline: data → chart → narrative → memo/deck.

**Exercise:** Draft an adoption roadmap for their company.

## Additional Themes

### 1. The "Last Mile" — Delivering Insights, Not Just Data
Executives want the chart *in a PowerPoint deck*, the analysis *in an email to the board*, the numbers *in a formatted Excel workbook*. The reporting pipeline (query → chart → narrative → document assembly) is a distinct capability.

### 2. Natural Language as Universal API Surface
The AI agent is essentially a universal API adapter. It translates English into Salesforce queries, SAP queries, Oracle queries — each with their own naming conventions. The user doesn't need to know SQL, doesn't need to know which system has the data, doesn't need to know the schema. Fundamentally different from dashboards, which require you to know exactly what you're looking for in advance.

### 3. The Cost/Speed Tradeoff

| Approach | Time to answer | Cost to build | Maintenance |
|---|---|---|---|
| Ask a BI analyst | Days to weeks | Low per query, high cumulative | Ongoing headcount |
| Build a dashboard | Weeks to months | $50K-500K | Continuous updates |
| Build a data warehouse | 6-18 months | $500K-5M+ | Large team |
| AI agent (this app) | Seconds | $50K-200K to build | Low (API costs) |

### 4. What AI Can't Do — The Human Judgment Layer
AI is excellent at: pulling data, writing SQL, making charts, drafting narrative, fuzzy-matching customer names.

AI is bad at: knowing whether the *question* is the right one, understanding political context, judging whether an anomaly is a data error or a real insight, making decisions with incomplete information.

The course should have exercises where the AI produces a technically correct but misleading analysis, and students have to catch it.

### 5. Privacy and Access Control
Not everyone should see everything. The VP of Sales shouldn't see individual compensation data. The regional manager should only see their region. The AI agent needs to enforce the same access controls as the underlying systems. A governance topic that most AI demos ignore.

### 6. Code Execution Architecture — Where Does the Python Run?

When the AI agent merges data from multiple systems, it runs Python code. In production, where that code executes is an important architectural decision. Three options:

**Option A: Cloud LLM sandbox (e.g., Anthropic's code execution tool).** The LLM vendor runs the Python code on their infrastructure. Zero infrastructure for the company. But query results are sent to the vendor's servers for processing — fine for non-sensitive data, typically rejected by compliance teams (HIPAA, SOX, GDPR) for real customer/financial/HR data.

**Option B: SQL-only with client-side charting.** Skip Python entirely. The LLM generates SQL; the database does the computation; the frontend renders charts with a JavaScript library. Simpler and avoids code execution security concerns entirely. But this cannot work for multi-system integration — there's no single database to query when data is scattered across Salesforce, Workday, and SAP.

**Option C: Vendor data platforms (Databricks, Snowflake, ThoughtSpot).** The AI agent, database, and code execution all run within the vendor's managed platform under the company's security boundary. The "buy not build" path. But these are designed around their own data warehouse, not querying 10 external systems directly.

**For multi-system integration (the core use case of this course), only Option A works** — you need Python to merge data from separate systems, and it must run within the company's own infrastructure. In production, this means Docker containers on the company's servers: each request spins up a sandboxed container with limited CPU/memory/time, no network access, and read-only data mounts. The data never leaves the company's network.

**Note for the teaching app:** Our demo uses Anthropic's cloud sandbox (Option A) because the data is synthetic. In production, the Python execution would move to the company's own servers. The user experience is identical — the only difference is where the code runs.

### 7. The Data Exposure Problem — What Does the LLM See?

Even when Python executes on your own servers, the LLM still needs to see results to do its job. If Claude generates a query, your server runs it, and the results include salary figures or customer records — those results must be sent back to Claude (at Anthropic's servers) so it can interpret the data, fix errors, or write a narrative summary. Running code locally doesn't solve the data privacy problem by itself.

**The core tension:** The more the LLM sees, the better the analysis. The less it sees, the safer the data. Four approaches to managing this:

**Approach 1: Aggregated results with guardrails (most common in practice).** The LLM sees aggregated results (total revenue by region, average compensation by level) but not individual records. A data loss prevention (DLP) layer scans what's sent back to the LLM and redacts anything that looks like PII (SSNs, email addresses, individual names). Row limits prevent bulk data extraction. The company's compliance team signs off on which data categories the LLM can see. This is where most real enterprise deployments land.

**Approach 2: The LLM never sees actual data.** Claude generates SQL and Python code, but results are rendered directly to the user's browser without passing through the LLM. Claude writes "blind" templates: "The top region by revenue is {region_1} at {revenue_1}." The server fills in values. The LLM can't adapt its analysis, notice anomalies, or provide insight — it's a code generator, not an analyst. Used in highly regulated environments (banking, healthcare).

**Approach 3: On-premise LLM.** Run an open-source model (Llama, Mistral) on your own hardware. No data ever leaves your network. The tradeoff: dramatically worse quality at SQL generation, multi-step reasoning, and natural language analysis. This gap is closing but still significant.

**Approach 4: Schema-only with sanitized errors.** The LLM only sees database schemas and synthetic sample rows, never real data. It generates all code blind. Results go directly to the user. For the debug loop, error messages are sanitized before being sent back (strip data values from tracebacks, keep only error types and line numbers). A practical middle ground used by some financial services companies.

**The key insight for executives:** This is a policy decision, not a technology problem. The technology to filter, redact, or restrict is straightforward. The hard part is deciding what level of data exposure to the LLM is acceptable for your organization — and that depends on your industry, your regulators, and your risk tolerance.

### 8. Hands-On Building: The Linux Server + Claude Code

Students use two tools in the course. The **Meridian Corp web app** is the polished end-user experience (Weeks 1-2). A **Linux server with Claude Code** is the builder experience (Weeks 3-4), where students create small working agents themselves — with AI assistance.

**Why this matters:** When executives see that the core agent loop is ~50 lines of Python, they stop thinking "we need to hire a team of AI consultants" and start thinking "our internal developer could build this." They also experience being the "checker" while AI is the "maker" — the central skill shift the course teaches.

#### Two-Tool Structure

| Tool | Used in | Purpose |
|---|---|---|
| Meridian Corp web app | Weeks 1-2 | The end-user experience. "This is what your employees would use." |
| Linux server + Claude Code | Weeks 3-4 | The builder experience. "Here's how you'd create this." |

#### Build Exercises (scaffolded, AI-assisted)

**Exercise 1: "Hello World" agent (~30 min).** A Python script that takes a question, sends it to Claude with a schema description, gets back SQL, runs it against a single parquet file, returns the answer. Students use Claude Code to help write it. The parquet file is pre-loaded; they just write the agent loop.

**Exercise 2: Add a second database (~30 min).** Modify the script to handle two databases (e.g., CRM + HR). Claude must query each separately and merge with pandas. The "aha" moment — they see the multi-system merge happen in code they wrote.

**Exercise 3: Add a web interface (~45 min).** Wrap the agent in a simple FastAPI endpoint. Claude Code generates most of it — the student provides direction. They end up with a working chat app built (with AI help) in under an hour.

**Exercise 4: Red-team your agent (~30 min).** Try to break the agent: SQL injection, asking for data they shouldn't see, nonsensical questions. Discover what guardrails are missing and add them.

#### What This Teaches That the App Alone Doesn't

1. **The agent loop is simple** — plan, execute, observe, repeat. Not magic.
2. **The hard part is prompt engineering** — the system prompt describing the schema is what makes SQL accurate.
3. **Guardrails are not automatic** — the first version has no SQL validation, no row limits, no error handling. Students discover vulnerabilities by testing.
4. **AI writes most of the code** — students direct Claude Code, experiencing the maker/checker dynamic firsthand.

#### Server Setup

- Ubuntu VM with Claude Code pre-installed
- One user account per student, shared API key
- Pre-loaded parquet files in a shared directory
- Starter templates with blanks for students to fill in
- Per-user working directories
- API costs: ~$1-2 per student for the build exercises

### 9. The SaaSpocalypse — AI Disruption of Enterprise Software

Belongs in **Week 4 (Build the Business Case)**. See `docs/saaspocalypse-research.md` for full research.

**The framing:** The tool students have been using for three weeks — querying enterprise systems with natural language, merging data across divisions, generating charts and memos — is what wiped $2 trillion off software stocks in February 2026. Their companies are paying per-seat licenses for tools that do a fraction of this.

**Key points to cover:**

1. **What's vulnerable:** BI dashboards, workflow automation, internal admin tools, Tier 1 support, simple CRM — the interface/task layer. 29-35% of teams are already replacing these with custom builds (Retool 2026 survey).

2. **What's not vulnerable:** Systems of record (ERP, HRIS, financial ledgers), regulatory platforms, complex multi-stakeholder workflows — the data/process layer. AI replaces the interface, not the data store.

3. **The Klarna cautionary tale:** Replaced Salesforce and Workday with AI, then partially reversed when quality dropped. Lesson: replace the right things, keep the systems of record, govern the transition.

4. **Pricing model shift:** Per-seat pricing is structurally broken when AI reduces headcount. Expect outcome-based pricing (Intercom: $0.99/resolution, Zendesk: $1.50-2.00/resolved ticket).

5. **The Meridian Corp connection:** The app students have been using IS the threat. It replaces Tableau (BI), data integration tools (cross-system merging), and reporting headcount — all from a chat interface. The question for executives: will you drive this change or react to it?

6. **Architect agents above applications:** The strategic move is placing AI agents as an orchestration layer across existing systems — exactly what the Meridian Corp app demonstrates. Don't rip out SAP; put an AI agent on top of it.
