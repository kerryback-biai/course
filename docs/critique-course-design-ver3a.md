# Critique: course-design-ver3a.md (Round 2)

Synthesized from three independent reviewers (Correctness & Completeness, Clarity & Persuasiveness, Devil's Advocate). Deduplicated and prioritized.

---

## Critical

### 1. Session 5 is lecture-heavy and breaks the hands-on rhythm (all 3 reviewers)

47 minutes of lecture (LLM deployment + data security + build vs. buy) before students engage. Sessions 1-4 established a hands-on-first pattern; Session 5 abandons it. The Devil's Advocate proposes restructuring with problem-first sequencing: open with a real scenario ("your data scientist says use OpenAI API, your CISO says no — what now?"), collect constraints in a quick breakout, *then* lecture as a response to those constraints.

### 2. No case studies remain (Devil's Advocate + Clarity)

Klarna was dropped with no replacement. The course relies entirely on the Meridian simulation for real-world grounding. Executives need at least 1-2 brief vignettes (5 min each) of real companies — a deployment that worked, a governance failure that didn't get caught. These anchor the simulation in reality.

---

## Warning

### 3. Capstone weaker without any value quantification (Devil's Advocate)

ROI template was dropped, but the capstone template still has "Success Metrics" without teaching executives to quantify business impact. Consider adding an ROI/value column to the rubric ("Strong: quantified business impact with realistic assumptions" vs. "Needs Work: vague metrics") rather than restoring a full ROI module.

### 4. Cross-session summary table (line 287) still says "optional build" for Session 3 (Correctness)

Session 3's live build was changed to required, but the summary table still reads "Agent loop + code execution architecture + optional build."

### 5. Deployment architecture discussed three times (Clarity)

Session 3 (where code runs), Session 5 (where LLM runs), Session 7 (RAG deployment) — the cloud-vs-on-premise tradeoff is repeated each time. Session 7 should assume students understand it by now and just note "the same tradeoffs from Session 5 apply" without re-explaining.

### 6. Session 5 should open by connecting to Session 3 (Devil's Advocate)

Students may think "code runs on my servers, so data is safe" from Session 3. Session 5 needs a 2-minute tie-back: "Last week we asked where the code runs. Today: where does the LLM that reads the results run? These are two separate decisions."

### 7. Session 1 cold open is thin at 5 minutes (Clarity)

The CEO email chain scenario could be more vivid — a concrete business failure, not just a slow turnaround. Also, "The Business Lens" (min 28-38) partly repeats the same message from the course overview (min 0-15).

### 8. Capstone rubric missing success metrics and risk mitigation dimensions (Clarity)

The rubric grades pilot scope, deployment approach, governance, and Day 1 action — but not whether success metrics are measurable or whether risk mitigations are specific. Two additional rows would strengthen it.

### 9. Session 3 live build framing (Devil's Advocate)

It's "required" but students watch — they don't participate. 13 minutes of instructor-driven coding is not meaningfully different from the old "optional" label. Consider reframing: "Live Walkthrough — watch now, replicate on the server later."

---

## Suggestion

### 10. Session 5 breakouts could be sharper

Instead of "What would your CISO say?" (which yields predictable answers), try a comparative frame: "A financial services company needs on-premise. A SaaS startup chose cloud API. Both are right. Where does your company land, and why?"

### 11. Session 7 RAG lecture could be more strategic, less technical

The 6-step pipeline explanation (chunk, embed, store, retrieve, generate) is implementation detail. Executives need to understand *what can go wrong* (failure modes) and *what decisions matter* (document freshness, access control, build vs. buy) more than the mechanics.

### 12. Vary breakout format across sessions

Six breakouts in eight sessions risks repetition. Consider pair-and-share, structured debate, or silent reflection + large-group discussion as alternatives for some sessions.

### 13. "Thinking partner" gap exists

The course teaches data access but never shows an executive using an agent iteratively to reason through a decision. A 10-minute segment in Session 8 synthesis could close this.

### 14. Session 4 hands-on could use a brief iteration demo first

Students are asked to produce deliverables but haven't been taught how to iterate on quality (tone, format, level of detail). A 5-minute live iteration example would help.

---

## Also noted (Correctness — minor)

### 15. Demo 5 description (line 67) says "Session 5 governance discussion" but Demo 5 pairs with Session 6

The demo pairing on line 66 correctly says Session 6, but the description text on line 67 still references "Session 5."

### 16. Session 7 bridge (line 247) says "five sessions" of structured data

Sessions 1-6 is six sessions of structured data work (even though Session 5 is deployment-focused, it still references the Meridian app). Minor wording issue.
