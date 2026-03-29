# Slide Deck Critique — Round 1

## Part A: Text-Based Review (3 agents: Correctness, Clarity, Devil's Advocate)

### Critical (must fix)

| # | Finding | Source |
|---|---------|--------|
| 1 | ~~**Sessions 3 and 4 are missing `---` slide separators**~~ — **FALSE POSITIVE.** Browser rendering confirms slides separate correctly. Quarto/revealjs treats `##` headings as implicit slide breaks. No action needed. | Clarity (retracted) |
| 2 | **Session 1 Meridian systems list has 4 wrong systems** (Coupa, SAP Concur, Jira, SharePoint) and omits 4 real ones (SAP Operations, QuickBooks, Oracle SCM, NetSuite Consolidation). Students will try to query nonexistent systems. | Correctness + Devil's Advocate |
| 3 | **Sessions 3 and 4 are completely missing homework slides**, breaking the cascade: Session 5's flipped format requires Morgan Stanley/AIMultiple/data security pre-readings assigned in Session 4 homework. | Correctness |
| 4 | **Homework in Sessions 1, 2, 5, 6, 7 doesn't match course design** — wrong counts, wrong readings, missing assignments (e.g., Session 6 doesn't assign Atherton case, breaking Session 7's opening debrief). | Correctness + Devil's Advocate |
| 5 | **Wrong next-session teasers**: Session 2 says "Can I Trust This Answer?" (should be Session 3: "How Does This Work?"); Session 4 says "When AI Gets It Wrong" (should be Session 5: "Deployment"); Session 6 says "Making It Stick" (should be Session 7: "Document AI"). | Correctness |
| 6 | **Session 8 timeline describes Session 4 as "The Competitive Landscape"** — should be "From Data to Deliverable." | Correctness |
| 7 | **Session 5 DUNNIXER: title says "Six Dimensions" but lists 8 items** (D-U-N-N-I-X-E-R). Misrepresents the source framework. | Devil's Advocate |
| 8 | **Session 7 RAG step-flow uses `.step-flow` (4-col) but has 5 items** — 5th card wraps to new row. Should use `.step-flow-5`. | Clarity |

### Warning

| # | Finding | Source |
|---|---------|--------|
| 9 | **Session 8 Monday Morning Actions uses `.stat-cards` (3-col) with 4 items** — 4th card wraps awkwardly. | Clarity |
| 10 | **Sessions 3 and 4 lack closing "Key Takeaway" quote slides**, breaking the pattern established in all other decks. | Clarity |
| 11 | **Multiple unsourced statistics** presented as facts: "70% dashboards never viewed," "60-70% warehouse projects fail," "60-90 days pre-work," "$2.3M understated," "3,000+ lines." | Devil's Advocate |
| 12 | **Warehouse vs. Agent comparison table is structurally biased** — unfairly favorable to agents. A CTO with a warehouse will notice. | Devil's Advocate |
| 13 | **Quote attributions inconsistent** — some quotes have `.quote-source`, others don't. Instructor-voice quotes use the same format as external quotes. | Clarity + Devil's Advocate |
| 14 | **No "wait/not ready" option** in Session 5 build-vs-buy. Missing the honest answer for companies lacking data readiness. | Devil's Advocate |
| 15 | **Capstone format mismatch**: Session 7 homework says 2-min pitch; course design says 5-min presentation + 1-2 page document. | Correctness |

### Suggestion

| # | Finding |
|---|---------|
| 16 | Session 7 deploying RAG step-flow uses emoji icons that render inconsistently across platforms. |
| 17 | Session 8 timeline with 8 items may be too cramped for Zoom viewing. |
| 18 | The hypothesis annotation script in all decks may be distracting during Zoom. |

---

## Part B: Visual Review (4 agents with Playwright screenshots of all rendered slides)

Screenshots captured at 1920x1080 for all 8 decks (143 slides total). Sessions 1-2 had 40 slides, Sessions 3-4 had 50 slides, Sessions 5-6 had 43 slides, Sessions 7-8 had 37 slides.

### Critical

| # | Session | Slide | Finding |
|---|---------|-------|---------|
| V1 | 3 | 9 (Pseudocode) | **Code block clipped at bottom** — the `else: return response.text` block is cut off, with a scrollbar visible. Audience misses the final logic of the agent loop. Fix: reduce code or split slide. |
| V2 | 7 | 8 (How RAG Works) | **5th step-card wraps to orphan row** — confirms text-review finding #8. The "Generate" card sits alone on row 2 with a stray arrow. Bottom explainer text also clipped. Fix: use `.step-flow-5`. |
| V3 | 7 | 8 (How RAG Works) | **Bottom text clipped** — "RAG = Retrieval-Augmented Generation..." second line cut off at viewport edge. |

### Warning

| # | Session | Slide | Finding |
|---|---------|-------|---------|
| V4 | 1 | 11 (Hands-On step-flow) | **Step-card description text too small** for Zoom — ~14-16px effective size. Same issue on S2 slide 7. |
| V5 | 2 | 10 (Four Patterns) | **Four-column cards dense** — 4 cards with 3 bullets each; hard to read on Zoom. |
| V6 | 2 | 11 (Traditional Answer) | **"$500K--$5M" line break** — stat value wraps mid-range, reducing visual impact. |
| V7 | 2 | 17 & 20 | **Vertical density** — content pushes to top/bottom margins. Zoom toolbar could obscure bottom text. |
| V8 | 3 | 18 (Other 2,950 Lines) | **Dense two-column + paragraph** — tight for Zoom if presenter webcam overlay is large. |
| V9 | 4 | 2 (Opening) | **Light-background section divider** missing gold underline, inconsistent with dark dividers. |
| V10 | 4 | 8 (Customizable Steps) | **Dense slide** — two columns of 4-5 bullets + closing paragraph; minimal bottom margin. |
| V11 | 5 | 14 (DUNNIXER) | **"Six Dimensions" but 8 items** — confirms text-review finding #7. Visible on rendered slide. |
| V12 | 6 | 16 (Why Governance) | **Densest slide in S5-S6** — blockquote + four-column cards; card text noticeably small. |
| V13 | 8 | 2 (Course Journey) | **Timeline numbers overlap circle markers** — numbers render through/on top of the blue dots. |
| V14 | 8 | 11 (Synthesis) | **Dense paragraph text in four-cards** — borderline readability on Zoom. |
| V15 | 8 | 14 (Monday Morning) | **4th stat-card wraps to orphan row** — confirms text-review finding #9. Asymmetric layout. |

### Suggestion

| # | Session | Slide | Finding |
|---|---------|-------|---------|
| V16 | 1 & 2 | 1 (Title) | Author name center-aligned while title/subtitle are left-aligned — minor inconsistency. |
| V17 | 1 | 6 (What If 30 Seconds) | White interstitial breaks dark-background pattern for transition slides. |
| V18 | 2 | 12 (Two Approaches) | 7-row comparison table is data-heavy for a single Zoom view. |
| V19 | 3 | 1 (Title) | Title wraps with orphaned "Work?" on second line. |
| V20 | 4 | 6 (Pipeline) | 6-column step-flow text is small (~14-16px) but acceptable for the layout constraint. |
| V21 | 4 | 20 (HPE quote) | Attribution text low-contrast gray on dark background. |
| V22 | 5 | 9 (Cost Comparison) | "$0.01--0.05" stat-card value wraps to two lines. |
| V23 | 7 | 14 (Context Window) | Section divider on light background, inconsistent with dark dividers elsewhere. |
| V24 | 8 | 6 (Capstone Format) | 3 cards in 4-col step-flow grid leaves empty right column.
