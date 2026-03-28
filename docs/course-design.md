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
