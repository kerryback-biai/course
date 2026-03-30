# Critique: demo-scripts.md

Synthesized from three independent reviewers (Correctness & Completeness, Clarity & Persuasiveness, Devil's Advocate). Deduplicated and prioritized.

---

## Critical

### 1. The "I never wrote code" claim is misleading (Devil's Advocate + Clarity)

The instructor types prompts specifying database schemas, column names, embedding models, and architectural decisions. This requires technical fluency, not just English. The demos show "a technical person using AI to write code faster," not "a non-technical person directing AI." Students may feel the gap between what the instructor does and what they could replicate.

### 2. Demo 5 (red-teaming) conflates parquet immutability with security (Devil's Advocate + Correctness)

The SQL injection demo uses `DROP TABLE` against read-only parquet files. The attack "fails" because of the storage backend, not because of guardrails. The narrative then adds a SQL validator and says "Guardrail one: in place" — but the attack was already blocked by the environment. This could mislead executives about what their actual risk surface looks like against real read/write databases.

### 3. Demo 7 (combined agent) shows synthesis without showing failure (Devil's Advocate)

The GE contract example works perfectly — RAG retrieves terms, database returns spending, LLM synthesizes. But LLMs can confidently synthesize wrong conclusions from partial information (e.g., is the $2M minimum annual or monthly? Per-division or consolidated?). The demo doesn't show what happens when synthesis is subtly wrong, which undermines the maker/checker message from Session 5.

### 4. Scripts assume deterministic Claude Code output (Devil's Advocate + Correctness)

Every demo narrates specific function names, variable names, and code structure ("it creates `query_revenue()`, `query_headcount()`..."). But Claude Code is non-deterministic — filming twice produces different code. Students following along will see different output, breaking the narrative. The fuzzy matching experiment (Demo 2) is especially brittle — the 80% match score and specific false positives depend on which algorithm Claude generates.

---

## Warning

### 5. Narration reads like lecture notes, not conversation (Clarity)

The SAYS sections are dense paragraphs that will sound stilted when read aloud. Natural speech uses shorter sentences and pauses. Example from Demo 1: "Remember Session 3's diagram of the agent loop? Question goes to LLM, LLM generates a tool call, system executes it, results go back to the LLM, LLM either makes another tool call or gives a final answer." Should be broken into shorter, spoken-rhythm sentences.

### 6. Visual monotony — nearly all terminal (Clarity)

Demos 1-2, 4-7 are pure terminal. Only Demo 3 briefly shows a browser. By Demo 5, executives will fatigue on black-background/white-text. Need screen annotations (arrows, highlights, callout boxes), diagrams, formatted report viewers, and side-by-side comparisons.

### 7. Demo 2 missing HubSpot as third CRM (Correctness)

Course design Session 2 explicitly demos "Salesforce, Legacy CRM, HubSpot separately." Demo 2 shows Salesforce + Workday, then adds Legacy CRM. HubSpot (Safety Division CRM) is never shown. This is a misalignment with the course design.

### 8. Demo 6 oversimplifies chunking (Devil's Advocate + Correctness)

Character-count chunking is a fallback. Real documents need section-aware (policies), clause-aware (contracts), or agenda-aware (meeting minutes) chunking. The experiment shows parameter tuning but not the harder design question. Students may think RAG is "parse, chunk by character count, embed, search."

### 9. Seven demos = ~2 hours of optional content (Devil's Advocate)

Realistically, busy executives watch 1-2 demos max. The deep material (Demos 5-7) gets the smallest audience. Consider consolidating to 4-5 demos.

### 10. No "what happens when things go wrong" in Demos 1-4 (Devil's Advocate)

Every demo shows the happy path. No agent getting stuck in a loop, no stale schema, no slow API response. Demo 5 covers security failures, but operational failures are unaddressed.

### 11. Production complexity understated (Devil's Advocate)

Demo 3: "from script to web app in two minutes." Demo 4: "core workflow is exactly what we built." The 3,000+ lines of production code (auth, error handling, streaming, audit) is mentioned but not felt. Executives may underestimate deployment effort.

### 12. Timing realism — demos assume first-try success (Correctness)

The scripts don't account for API latency, debugging, or Claude Code producing code that needs revision. All 7 demos assume correct output on first prompt. A caveat ("In this demo, Claude Code produces correct code on the first request; in practice, expect iterations") would be honest.

### 13. Embedding model choice unexplained (Correctness)

Demo 6 uses `all-MiniLM-L6-v2` "for simplicity" but doesn't explain the tradeoff vs. cloud embedding APIs (OpenAI, Cohere, Voyage). The course design Session 7 discusses this choice, but the demo doesn't reinforce it.

### 14. Document update/freshness not addressed in Demo 6 (Correctness + Devil's Advocate)

The RAG demo builds an index once and queries it. No discussion of what happens when the employee handbook is revised, or when new board minutes arrive. Course design mentions this (line 246: "when a policy is updated, the old version must be replaced, not duplicated") but the demo doesn't demonstrate it.

---

## Suggestion

### 15. Add "why 50 lines matters" business framing to Demo 1

Not "it's technically simple" but "this means lower maintenance cost and faster prototyping." Connect the technical fact to the business implication.

### 16. Show the system ID mapping table visually in Demo 2

A 5-row table showing `worker_id | system_name | external_id` makes "identity resolution" concrete rather than abstract.

### 17. Make Demo 4's review gate real

Show catching an actual error during review (e.g., wrong fiscal period filter), not just running `--approve`. This makes the review gate feel like a governance mechanism, not a checkbox.

### 18. Add token/cost estimates to Demos 6-7

Embedding 157 chunks costs ~$0.01, cross-system synthesis costs ~$0.05-0.10 per query. Executives need these numbers for ROI discussions.

### 19. Show one routing failure in Demo 7

An ambiguous question the agent handles poorly (e.g., "What is GE's annual revenue?" — contractual minimum or actual spending?) to balance the happy path.

### 20. Create companion worksheets

"For Your Company" sheets for each demo that ground XYZ examples in students' real systems: list your data sources, map your entities, identify your document collections, estimate your chunking strategy.

### 21. Add a "production reality check" sidebar to each demo

Something like: "This demo shows the core 50 lines. A production system typically adds 3-5x the code for error handling, logging, authentication, and UI. Time estimate: 2-3 hours to proof-of-concept, 2-3 weeks to production-ready."

### 22. Reframe the "never wrote code" claim honestly

Instead of "I never wrote a line of code," say: "I didn't write Python syntax, but I specified the technical requirements precisely. In your company, a developer or data engineer would provide the schema knowledge; an executive would provide the business question. The AI bridges the gap."

### 23. Add performance/latency expectations

None of the demos mention query response time. A note like "typical response: 3-5 seconds for a single-system query, 8-15 seconds for cross-system with merge" sets realistic expectations.

### 24. Show the chunk boundaries visually in Demo 6

A document with colored regions showing where chunk breaks fall would make the chunking concept much more tangible than terminal output alone.
