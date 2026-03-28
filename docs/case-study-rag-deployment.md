# Case Study: Atherton Financial Services — "Ask Atherton" Policy Assistant

*A composite case study for Session 7: Document AI — Answers from Your Own Files*

---

## Background

Atherton Financial Services, a mid-size wealth management firm with 4,200 employees across twelve offices, had a familiar problem: employees couldn't find answers in their own documents. The compliance team fielded hundreds of routine questions each week — "What's our gift policy for client-facing staff?" "Which vendor onboarding documents do we need for a sub-adviser?" "What changed in the updated Business Continuity Plan?" HR saw the same pattern: open enrollment questions, parental leave policies, remote work guidelines. The information existed, scattered across a SharePoint document library of roughly 18,000 files — compliance manuals, HR handbooks, regulatory filings, investment policy statements, and board minutes going back a decade.

In early 2025, Atherton's CTO launched "Ask Atherton," an internal document Q&A assistant powered by retrieval-augmented generation. The team evaluated turnkey platforms (Microsoft 365 Copilot, Glean) and a custom-build approach. They chose a hybrid path: Microsoft 365 Copilot for general productivity across Office apps, plus a custom RAG system — built on Azure OpenAI with a vector database — specifically for the compliance and HR policy corpus, where they needed tighter control over which documents were indexed, how answers were cited, and who could see what.

## The First Three Months

The pilot launched with the compliance team and 300 users in the home office. Early results were encouraging. For straightforward, single-document queries — "What is the maximum gift value under the personal trading policy?" — the system returned accurate answers with page-level citations 85% of the time. Compliance analysts estimated they saved 5–8 hours per week on routine inquiries. Employee satisfaction surveys showed that 70% of pilot users preferred the assistant over searching SharePoint manually.

But three problems emerged quickly. First, **stale documents**. The SharePoint library contained multiple versions of the same policy — a 2022 Business Continuity Plan alongside the 2024 revision. The RAG system retrieved whichever version was semantically closer to the query, not the most current. In one incident, an employee preparing for a regulatory exam received outdated disaster-recovery procedures and didn't realize they had been superseded. Second, **chunking failures on complex documents**. The investment policy statements — dense, 40-page PDFs with nested tables and cross-references — were split into chunks that severed critical context. A question about permitted asset classes returned a paragraph that listed equity categories but omitted the exceptions table on the following page, producing an answer that was technically accurate but materially incomplete. Third, **access control gaps**. When the team expanded the pilot to include HR policy documents, they discovered that the system's permission model didn't mirror SharePoint's access controls precisely. A junior analyst's query about "compensation guidelines" surfaced a summary of the executive bonus structure — a document restricted to HR leadership in SharePoint but inadvertently indexed without those restrictions in the vector store.

## What Worked and What Didn't

**What worked:**

- **Routine, single-document queries** performed well. Questions with clear answers in a single policy document — gift limits, PTO accrual rates, expense reimbursement thresholds — were answered accurately and cited correctly the large majority of the time.
- **Time savings were real.** The compliance help desk saw a 40% reduction in Tier 1 tickets (questions answerable directly from policy documents) within the first quarter.
- **Citations built trust.** Because the system returned the specific document name, section, and page number, employees could verify answers themselves — and they did, which paradoxically increased confidence in the tool over time.

**What didn't work:**

- **Document versioning was the biggest headache.** With 18,000 files and no consistent versioning or archival discipline, the vector store became a time-scrambled soup. The team had to build a metadata pipeline to tag documents with effective dates and deprecation flags — work they hadn't budgeted for.
- **Complex, multi-section questions failed.** "Compare our current proxy voting guidelines with last year's" required reasoning across two documents and multiple sections. The chunking strategy couldn't support this, and the answers were often incomplete or hallucinated a comparison that wasn't grounded in the text.
- **Access control required a separate workstream.** The team assumed SharePoint permissions would "flow through" to the RAG system. They didn't. Rebuilding permission-aware retrieval added two months and a dedicated security engineer to the project.
- **Hallucinated citations appeared under pressure.** In roughly 5–8% of queries, the system cited a real document but attributed a claim to it that the document didn't actually contain — a pattern consistent with the Stanford study that found leading RAG-based legal research tools hallucinate between 17% and 33% of the time, even with retrieval grounding.

## Lessons for Deployment

1. **RAG is a data-quality project, not just an AI project.** Atherton spent more engineering time on document curation, version control, and metadata tagging than on the LLM or vector database. Organizations that skip the "boring" work of cleaning their document library will get confidently wrong answers.

2. **Permissions don't transfer automatically.** Enterprise document repositories have layered, often inconsistent access controls. A RAG system that indexes everything and filters at query time is architecturally different from one that indexes per-permission-group. The choice matters enormously, and getting it wrong creates compliance risk. Microsoft's own internal Copilot deployment team reported that oversharing was their single biggest governance challenge, with a Gartner survey finding that 40% of organizations delayed Copilot rollouts specifically over data governance concerns.

3. **Start with a narrow, well-curated corpus.** Atherton's success correlated directly with corpus quality. The compliance policy set — 200 curated, current documents — performed far better than the full SharePoint library. A 2025 medical study found that restricting a RAG chatbot to high-quality, curated content dropped hallucinations to near zero, compared to 52% fabrication rates on unvetted data.

4. **Chunking strategy is a design decision, not a default setting.** Fixed-size chunking destroyed the meaning of complex documents. The team eventually moved to document-structure-aware chunking that respected section boundaries, tables, and cross-references — an approach that required understanding the documents, not just the technology.

5. **Budget for ongoing maintenance.** Documents change. Policies are revised, regulations are updated, people leave and new people arrive. A RAG system is not a one-time deployment — it requires a pipeline for re-ingestion, version deprecation, and regular accuracy audits.

## Discussion Questions

1. **Build vs. buy.** Atherton chose a turnkey platform (Copilot) for general productivity but built a custom RAG system for compliance documents. What factors in your organization would push you toward one approach or the other? What would you need to know about your document corpus before making that decision?

2. **The access control problem.** The case describes a junior analyst surfacing executive compensation data through the Q&A system. How does your organization manage document permissions today, and how confident are you that those permissions would hold up if you layered an AI search tool on top? Who in your organization would own this risk?

3. **Accuracy vs. completeness trade-offs.** The system worked well for simple, single-document queries but struggled with complex, multi-document questions. If you were deploying a document AI system, would you limit it to the queries it handles well (and route complex questions to humans), or would you try to solve the harder problem? How would you set expectations with users about what the system can and can't do?

---

## Sources

- Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C.D., & Ho, D.E. (2025). [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://law.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/). *Journal of Empirical Legal Studies*, 22, 1–27.
- Microsoft Inside Track Blog. [How we're tackling Microsoft 365 Copilot governance internally at Microsoft](https://www.microsoft.com/insidetrack/blog/how-were-tackling-microsoft-365-copilot-governance-internally-at-microsoft/).
- Microsoft Tech Community. [Mitigate Oversharing to Govern Microsoft 365 Copilot and Agents](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/mitigate-oversharing-to-govern-microsoft-365-copilot-and-agents/4448744).
- Concentric AI. [2026 Microsoft Copilot Security Concerns Explained](https://concentric.ai/too-much-access-microsoft-copilot-data-risks-explained/) (includes Gartner survey data on delayed rollouts).
- AIM Consulting. [Case Study: AI-Powered Self-Service Employee Chatbot](https://aimconsulting.com/insights/ai-powered-chatbot-for-enterprise-case-study/) (defense/aerospace HR chatbot with 135K monthly interactions).
- Innoflexion. [Why Your RAG Implementation Will Fail Without Data Readiness](https://www.innoflexion.com/blog/rag-data-readiness-audit) (stale document versioning and re-ingestion challenges).
- Analytics Vidhya. [Enterprise RAG Failures: The 5-Part Framework to Avoid the 80%](https://www.analyticsvidhya.com/blog/2025/07/silent-killers-of-production-rag/) (chunking failures account for 80% of RAG issues).
- Binariks. [Why Enterprise RAG Fails and How to Fix It for Real ROI](https://binariks.com/blog/why-enterprise-rag-fails/) (document version coexistence in vector stores).
- Lighthouse. [What Microsoft 365 Copilot Adoption Really Looks Like](https://www.lighthouseglobal.com/blog/microsoft-365-copilot-adoption) (5% pilot-to-scale conversion rate).
- Vectara. [Enterprise RAG Predictions for 2025](https://www.vectara.com/blog/top-enterprise-rag-predictions) ("cannot live without RAG, yet remain unsatisfied").
