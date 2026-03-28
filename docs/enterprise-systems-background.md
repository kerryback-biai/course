# Enterprise Systems Background

Context for teaching executives about the enterprise software landscape simulated in the Meridian Corp app.

## The shift: on-premise to cloud

**15 years ago**, most enterprise software was installed on company-owned servers. IT departments managed hardware, databases, upgrades, and backups. The company owned the data and infrastructure.

**Today**, almost all are **SaaS** (Software as a Service) — the vendor hosts everything in the cloud. The company pays a per-user monthly subscription and accesses it through a browser. The vendor stores the data, manages uptime, and pushes updates automatically.

## The major systems

**Salesforce** — CRM (Customer Relationship Management). Tracks accounts, contacts, sales pipeline, and deals. Sales reps log their activity here. The company's entire customer relationship history lives in Salesforce. Pure cloud/SaaS from day one (founded 1999, they pioneered the SaaS model). ~$35B/year revenue. Pricing: $25-300/user/month depending on tier.

**SAP** — Enterprise Resource Planning (ERP). The backbone system for large manufacturers and distributors. Handles procurement, inventory, manufacturing, logistics, and finance all in one integrated system. Historically the quintessential on-premise software — companies would spend $50-500M on multi-year SAP implementations running on their own servers. Now pushing hard to move customers to their cloud version (S/4HANA Cloud), but many large companies still run on-premise. ~$35B/year revenue. German company.

**Oracle** — Two things: (1) the Oracle database, which is the most widely used enterprise database in the world, and (2) Oracle's cloud applications (ERP, SCM, HCM). Many companies run SAP *on* Oracle databases. Oracle's Supply Chain Management (SCM) cloud competes with SAP for operations/logistics. Also historically on-premise, now pushing cloud. ~$53B/year revenue.

**NetSuite** — Cloud ERP for mid-market companies (owned by Oracle since 2016). Does what SAP does but for smaller companies ($10M-$1B revenue). Finance, inventory, orders, CRM all in one system. Pure cloud. Popular with companies too big for QuickBooks but not big enough for SAP. ~$2B/year revenue within Oracle.

**QuickBooks** — Accounting software from Intuit. The default for small businesses. Invoicing, bill pay, payroll, basic reporting. Desktop and cloud versions. When a company gets acquired by a larger one (like our Energy division scenario), their QuickBooks data often needs to be integrated with the parent's ERP — a common and painful real-world problem.

**Workday** — Cloud HR and Finance. The dominant modern HR system for large companies. Employee records, payroll, benefits, performance reviews, org charts, hiring. Replaced older on-premise systems like PeopleSoft and Oracle HCM. ~$7B/year revenue. Almost every Fortune 500 company uses Workday or is migrating to it.

**HubSpot** — CRM and marketing automation for small/mid-market companies. Simpler and cheaper than Salesforce. Many companies start on HubSpot and migrate to Salesforce as they grow — or an acquired division runs HubSpot while the parent runs Salesforce. ~$2.5B/year revenue.

**Zendesk** — Customer support ticketing. When a customer emails, calls, or chats with support, a ticket is created in Zendesk. Tracks issue resolution, SLAs, customer satisfaction. Cloud SaaS. ~$1.7B/year revenue (acquired by private equity in 2022).

## How data moves between systems

There are several mechanisms, all imperfect:

### 1. APIs (Application Programming Interfaces)
Every modern SaaS product exposes REST APIs. You can programmatically read and write data. For example, Salesforce's API lets you pull all opportunities closed this quarter, or push a new contact into the system. This is how most integrations work — but someone has to build and maintain the integration code.

### 2. Integration platforms (iPaaS)
Tools like **MuleSoft** (owned by Salesforce), **Boomi** (owned by Dell), **Workato**, and **Zapier** provide pre-built connectors between systems. You configure "when a deal closes in Salesforce, create an invoice in NetSuite." These handle the plumbing but still require configuration and maintenance. This is a huge market (~$10B+) because the integration problem is so universal.

### 3. ETL / Data warehouses
For analytics (not transactional operations), companies extract data from each system nightly, transform it into a common format, and load it into a central data warehouse (**Snowflake**, **BigQuery**, **Databricks**, **Redshift**). This is where "single source of truth" reporting happens. It's expensive, requires a data engineering team, and the data is always at least a day old. This is the traditional approach to the problem our app solves.

### 4. CSV exports (the reality)
Despite all the above, a shocking amount of enterprise data integration still happens via people downloading CSV files, opening them in Excel, and manually reconciling. This is exactly what our app replaces.

## Why the data is always scattered

No company chooses to have scattered data. It happens because:

- Different departments buy different best-of-breed tools (Sales wants Salesforce, Finance wants NetSuite, HR wants Workday)
- Acquisitions bring in whatever the acquired company was using
- Different regions or business units may have adopted different systems at different times
- Nobody wants to rip out a working system just for data consistency
- Data warehouse projects take years and cost millions

## What our app demonstrates

**The alternative**: instead of moving all the data into one place (expensive, slow, fragile), bring an AI agent that can query each system where the data already lives and merge on demand.

Our app is realistic in that:
- Each "system" has its own naming conventions (Salesforce CamelCase, SAP material_number, etc.)
- Customer identities don't match across systems (the #1 real-world problem)
- The AI queries each system's API separately and merges in Python — exactly what a real integration would do

The one simplification is that in real life, each system's API has different authentication, rate limits, pagination, and query languages (Salesforce uses SOQL, not SQL). We abstract all of that behind DuckDB/SQL, which is fair for a teaching tool.
