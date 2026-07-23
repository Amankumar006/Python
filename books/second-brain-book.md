# Second Brain: Building a Living Wiki, From Idea to Working App

*A record of what was built, how it was built, why the architecture looks the way it does, and what broke along the way.*

---

## Part 0 — What This Document Is

This is a build log, not a tutorial. It follows one real project — a personal, multi-domain knowledge wiki called **Second-Brain**, maintained by an AI agent, with a FastAPI + React application built on top of it — from the first idea to a working chat interface that answers real exam questions with citations.

The point of writing it this way is that the mistakes are as instructive as the successes. Almost every architectural decision in this project exists *because* something broke first. This document keeps that causality intact: problem, then decision, then result.

---

## Part 1 — The Core Idea

The project started from a pattern popularized by Andrej Karpathy: instead of doing RAG (retrieval-augmented generation) where an LLM re-derives understanding from raw documents on every query, an LLM agent **incrementally builds and maintains a persistent wiki** — a structured, cross-linked set of markdown pages that sits between raw sources and the person asking questions.

The critical difference from ordinary RAG:

- **RAG**: raw documents → chunk → embed → retrieve at query time → answer. Nothing persists. Every question re-derives understanding from scratch.
- **This pattern**: raw documents → LLM reads and *writes a wiki page* → the wiki accumulates, cross-references, and self-corrects over time → questions are answered *from the wiki*, which is already synthesized, already linked, already flagged for contradictions.

Three layers make this work:

| Layer | Role | Mutability |
|---|---|---|
| **Raw sources** | Original PDFs, textbooks, transcripts | Immutable — never touched by the agent |
| **The wiki** | LLM-generated markdown pages: summaries, concepts, entities | Fully owned and maintained by the agent |
| **The schema** | A config document telling the agent how to behave | Co-evolved by human and agent over time |

The three core operations on this wiki are **ingest** (process a new source into pages), **query** (answer a question by reading the wiki, not the raw sources), and **lint** (a periodic health check for orphan pages, contradictions, and staleness).

---

## Part 2 — Instantiating the Pattern: Multi-Domain from Day One

The first real design decision was whether to build one wiki per domain (college coursework, a research project, email) or one wiki with internal domain namespaces. **One wiki, namespaced by domain**, won — because a single `index.md` and `log.md` allow cross-domain queries ("what's due this week, given my timetable and my research deadlines"), while separate top-level folders keep each domain's rules from bleeding into another's.

```
Second-Brain/
├── AGENTS.md              ← core schema, loaded first, always
├── raw/<domain>/          ← immutable sources
├── wiki/<domain>/         ← LLM-maintained pages
│   ├── index.md           ← catalog, sectioned by domain
│   ├── log.md              ← append-only history
│   └── _conventions.md    ← domain-specific overrides
└── .agents/
    ├── rules/             ← always-on and conditional behavior rules
    ├── skills/            ← ingest, lint, query, add-domain, pdf-extract
    └── workflows/         ← /ingest, /lint, /ask slash commands
```

### The extensibility requirement

A design constraint stated explicitly up front: *whatever schema gets built must support adding new domains later without rewriting the core.* This produced two specific decisions:

1. **A universal page anatomy.** Every page, regardless of domain, uses the same YAML frontmatter shape (`type`, `domain`, `title`, `tags`, `sources`, `created`, `updated`, `status`). This is what makes cross-domain search, lint, and index generation possible without per-domain special-casing.
2. **Core rules stay domain-agnostic; domain-specific behavior lives one level down**, in each domain's own `_conventions.md`. Adding a new domain means adding a folder and a short conventions file — never touching the shared `.agents/rules/` or `.agents/skills/` files.

A companion `.agents/skills/add-domain/SKILL.md` encodes a decision rule for *when* something warrants a new domain versus just a new page type inside an existing one — preventing both over-fragmentation (a folder per tiny topic) and under-fragmentation (cramming unrelated content into an existing domain because creating a new one feels like overhead).

---

## Part 3 — The .agents/ System: Rules, Skills, Workflows

Antigravity CLI (Google's agentic coding tool, distinct from Anthropic's Claude Code but used here as the execution environment) reads project-scoped configuration from `.agents/`, organized into three kinds of files:

- **Rules** (`.agents/rules/`) — always-on or conditionally-triggered behavior constraints. Example: a rule enforcing that `raw/` is never modified, and a stricter rule for the `bharat` domain requiring every claim to carry a citation because those pages feed a fine-tuning dataset downstream.
- **Skills** (`.agents/skills/`) — named, reusable procedures with a description that lets the agent decide when to invoke them. `ingest-source`, `lint-wiki`, `query-wiki`, `add-domain`, and later `pdf-extract` were all built this way.
- **Workflows** (`.agents/workflows/`) — slash-command shortcuts (`/ingest`, `/lint`, `/ask`) that wrap a skill invocation with a fixed framing prompt.

### The contradiction rule — a rule that mattered more than expected

One rule, written early and tested constantly throughout the project, turned out to be the single most load-bearing piece of the whole schema:

> If a new source contradicts an existing page's claim, do not silently overwrite. Add both claims with source attribution, mark the page `status: contested`, and flag the contradiction. Let the human resolve it.

This rule was exercised for real twice: once when a textbook stated GoogLeNet won ILSVRC 2015 (historically it won 2014; ResNet won 2015), and once when a source PDF was discovered to be missing an entire page, cutting off a derivation mid-sentence. In both cases, later automated lint passes confirmed the `status: contested` flag survived every subsequent edit — proof the rule was actually enforced, not just written down.

---

## Part 4 — First Ingest, and the Depth Problem

The first real ingest (a BAI701 Module 1 textbook PDF) produced pages that were clean, well-linked — and dangerously thin. The agent had defaulted to *synthesis* (the Karpathy pattern's original intent: compress, cross-reference, keep it lean), when what was actually needed was *exam-grade completeness*: every formula, every named result, every worked example, preserved in full.

This is the first major lesson of the project: **a research wiki and a study wiki have opposite depth requirements**, and nothing in the generic schema distinguished them. The fix was an explicit domain-level override in `wiki/college/_conventions.md`:

```
## Depth requirement (exam prep, not synthesis)
- Preserve full definitions, formulas, derivations, worked examples.
- Extract and embed diagrams as actual image files, not descriptions.
- Prefer completeness over synthesis elegance in this domain specifically.
```

This override was tested again on Module 2 and found *still insufficient* — the agent preserved concepts but silently dropped every specific number: competition results, error rates, comparison tables. A second, more specific addendum was needed:

```
## Depth requirement — addendum (numbers, tables, worked examples)
- Preserve every specific number: percentages, error rates, layer counts.
  "Performed well" is never an acceptable substitute for "achieved 7.32% error."
- Any comparison table must be reproduced as an actual markdown table.
- Before considering a subsection covered, list every number/statistic it 
  contains and confirm each one actually appears on the resulting page.
```

**Lesson:** vague depth instructions ("preserve full detail") get satisfied at whatever level of detail the model considers "full." Only explicit, checkable criteria — *count every number, list every table, confirm each appears* — actually changed the output.

---

## Part 5 — The PDF Extraction Saga

Diagrams and tables were still being lost even after the numbers rule, because the underlying problem was structural: the agent was reading PDF *text* only, with no access to embedded images or true table structure. The fix was a new preprocessing skill, `pdf-extract`, built around **Docling** (IBM's open-source document-layout/table/figure extraction library), running as Step 0 before `ingest-source` touches any PDF.

### The dependency hell

Getting Docling running on the actual machine (macOS Intel, older Python build) took far longer than the extraction logic itself:

- NumPy had to be downgraded below 2.0 for binary compatibility with the installed PyTorch.
- `transformers` and `torchvision` needed specific pinned versions.
- The Python build was missing a working `_lzma` module (common on certain pyenv-built macOS Pythons), needing a `backports.lzma` shim.
- Several **runtime monkeypatches** were required for `torch.compiler`, `torch.amp.GradScaler`, `torch.library`, and missing `torch.uint16/32/64` dtypes — all backporting newer PyTorch APIs onto an older installed version.

**Lesson:** when an agent solves a gnarly environment problem through trial and error, that knowledge must be *written down*, not left in scratch scripts. The fix was to freeze the working state:

```bash
pip freeze > .agents/skills/pdf-extract/requirements.txt
```

...and add an "Environment notes" section directly in `pdf-extract/SKILL.md`, documenting *why* each pin and patch exists — so a future session (or a fresh clone) doesn't have to re-derive the same fixes from scratch. The freeze was verified for real, not just trusted: installing from `requirements.txt` into a throwaway venv and re-testing against the actual PDF.

A second, unrelated but important check: confirming this venv was **isolated** to the Second-Brain project and not shared with other ML work (a Bharat fine-tuning project, in this case) — since a shared venv pinned to old NumPy/transformers would have silently broken unrelated work.

### The scratch-folder bug

The first working version of `pdf-extract` wrote its output — extracted figures, `extraction_summary.json` — to a session-scratch directory (`~/.gemini/antigravity-cli/brain/<session-id>/scratch/`) instead of the intended `wiki/<domain>/assets/<source>/`. This mattered for two reasons: scratch directories aren't committed to git, and they can be cleaned up automatically between sessions. The fix was explicit — rewrite the extraction script to write directly into the repo, and manually recover the already-extracted files from the first test run before they were lost.

**Lesson:** "it worked" is not the same as "it worked in the right place." Always verify *where* output landed, not just *that* it exists.

---

## Part 6 — The Full Audit Cycle (Modules 1–5)

Once `pdf-extract` worked, the natural next question was: how much of the *earlier* work — done before this tool existed — was actually deficient? Rather than blindly re-ingesting everything (expensive, and possibly unnecessary), an **audit-first workflow** was used:

1. Read the source PDF and the wiki page(s) side by side.
2. List every number, formula, named result, and figure in the source.
3. Mark each present or missing on the wiki page.
4. Only *then* decide what needs re-ingesting.

This surfaced a genuinely important discovery that had nothing to do with the wiki at all: **Module 3's source PDF itself is missing a page.** The printed page numbers jump from 39 to 41, cutting off a Cross-entropy loss definition mid-sentence and the start of a Softmax derivation. No amount of re-ingesting fixes a gap that exists in the source material — this was flagged as `status: contested` with an explicit note, and a real fix was found: the textbook's equation numbering matched Goodfellow, Bengio & Courville's *Deep Learning*, whose complete text is freely available online, making the missing page recoverable from a legitimate alternate source.

### A self-contradiction worth learning from

Partway through auditing Modules 3 and 4, the agent claimed it needed to redo them, started a background extraction job, then said "actually, I already did this in a previous session" and killed the job it had just started. This contradiction — starting a redo, then claiming it was unnecessary, in the same breath — was treated as a signal that the agent's own memory of what happened wasn't reliable, and every claim it had just made was re-verified with direct evidence (a `grep` across the actual wiki files, not a description of what should be there). The re-verification came back clean, but the process — *distrust a self-contradicting summary, demand file-level proof* — is a repeatable pattern, not a one-off.

**Lesson:** an agent's summary of its own past actions is a claim, not a fact. When it contradicts itself, the fix is not to pick which version to believe — it's to check the actual files.

---

## Part 7 — Infrastructure Debugging (Two Separate Bugs)

Two distinct, unrelated infrastructure problems surfaced during this project, and conflating them would have wasted time chasing the wrong fix for each.

### Bug 1: A single PDF-extract run hung for 30+ minutes

Checking `ps aux` showed **no process actually running** — meaning it wasn't a slow computation, it was a completed-or-crashed process whose exit the CLI's own task tracker never registered. This matches a documented Antigravity CLI issue: a terminal-host communication deadlock, more likely to trigger with heavy interactive shell configurations.

### Bug 2: Every agent-run command (even `npm install`, `git push`) was consistently slow

This turned out to be shell-startup overhead, not a hang: `time zsh -i -c 'echo hi'` measured ~2 seconds, versus a healthy shell's well-under-100ms. The cause was `oh-my-zsh`, exactly the class of setup flagged as a known trigger for slow/hanging agent-spawned shells — plus, incidentally, a broken line in `.zshrc` throwing an error on every single shell start (a leftover reference to a deleted tool-install script).

**Lesson:** "everything is slow" and "one thing hung forever" are different bugs with different diagnostics — the first needs a stopwatch, the second needs a process list. Treating them as the same problem would have led to fixing the wrong thing.

---

## Part 8 — Automation: Nightly Lint, and a Real Dead End

The plan was straightforward: a nightly GitHub Actions job running the LLM-powered `lint-wiki` skill headlessly. Before writing the workflow, the auth mechanism was tested directly rather than assumed:

```bash
env -i HOME=/tmp/empty_home PATH=$PATH GEMINI_API_KEY="..." agy --print "hello"
```

**Result: it failed.** Antigravity CLI stalled waiting for interactive browser-based OAuth — there is no service-account or CI-token auth path in this version. This was confirmed, not guessed, with the actual failing command and its actual output.

This is a case where the honest answer to "can we do X" was no, and the response was to change the architecture rather than force a broken plan through. The nightly job was rebuilt as a **deterministic Python script** (`scripts/lint.py`) instead of an LLM call — which also has a real benefit beyond sidestepping the auth problem: it needs no API key at all, and can't hang on an LLM call.

This came with an explicit, stated tradeoff: a mechanical script can catch orphan pages, `status: contested` flags, missing cross-references (by exact title match), and index drift — but it **cannot** catch stale claims, cross-domain leakage, or data gaps, since those require semantic understanding of the actual content. The nightly script's own log output was written to say so explicitly:

```
## [DATE] nightly-lint (Mechanical Checks Only) | all | N issues found
*Notice: This is a deterministic script run. It does NOT check for Stale 
Claims, Cross-domain Leakage, or Data Gaps.*
```

### Two real bugs found and fixed before trusting it

1. **A regex mismatched the actual `index.md` format** — written to expect `(type, date)` with a comma, when the real format was `type (date)` with the type outside the parentheses. This wasn't caught by "it ran without error" — it was caught by *actually parsing the real file and printing the result*, which revealed the parser returned an empty dictionary despite the file having 21 real entries.
2. **The drift check only looked one direction.** It could tell you a real page was missing from the index — but not the reverse: an index entry pointing at a file that doesn't exist. This exact gap caught a real phantom entry (`Deep-Learning-Optimization-Techniques`, indexed but never actually created) once the reverse check was added and tested.

**Lesson:** "I fixed the regex" is not evidence. "Here is the regex run against the real file, here is the actual output" is evidence. This distinction was enforced repeatedly throughout the project, and every time it was enforced, it caught something real.

---

## Part 9 — The Application Layer: FastAPI + Obsidian's Local REST API

With the wiki itself solid, the next layer was making it queryable from outside a terminal. The **Obsidian Local REST API** community plugin (by Adam Coddington — chosen specifically because its download count and recency dwarfed competing plugins) exposes the vault over HTTP, including a bundled MCP server.

### A real security incident, twice

Two live API keys were accidentally shared outside the local machine during this project — once via a settings screenshot showing the Obsidian REST API bearer token, once by pasting a live OpenRouter key directly into chat. Both were treated identically: **rotate immediately**, regardless of whether the key currently has any usable balance or the exposure seems low-risk. A key that currently has zero credits is still a real key the moment funds are added.

A related decision: CORS on the FastAPI backend was explicitly **not** set to `"*"` even for local development, specifically because this backend holds three live LLM provider keys — an open CORS policy would let any browser tab call the endpoints and spend those credits.

### The three-tier LLM fallback

The architecture: try a fast/cheap model first, fall back only on failure (not on any quality heuristic), through three independent providers so a single provider's outage or rate-limit doesn't take down the whole service.

```
Tier 1: Gemini 3.5 Flash        (fast, primary)
Tier 2: Groq Llama 3.3 70B      (fallback on failure)
Tier 3: OpenRouter (free tier)   (last resort, zero-cost)
```

This tier map went through real, tested iteration, not a one-shot build:

- The original Tier 1 model names (`gemini-1.5-flash`, `gemini-2.5-flash`) both returned 404s — not a bug, but a real, verified model-generation change (Google released `gemini-3.5-flash` as the new current-gen Flash model, and shut down the 2.0-era models).
- The original Tier 3 model string (`nex-n2-pro`) didn't match any real OpenRouter model ID — the correct one, `nex-agi/nex-n2-pro`, was only found by fetching OpenRouter's actual live model list, not by guessing from the name given in conversation.
- Tier 3 then hit a real `402 Payment Required` — the OpenRouter account had zero credits. Rather than requiring a purchase, the fallback model was swapped to one of OpenRouter's genuinely free (`:free`-suffixed) models, chosen from a live fetch of the current model list rather than a remembered one, since the free lineup rotates.

At each step, "the code compiles" was treated as insufficient evidence — every tier was confirmed with an actual completion call and a real response shown, including one explicit test where Groq/Gemini keys were temporarily broken specifically to force a real call through to the tier being verified.

**Lesson, stated plainly because it recurred so often:** model names, provider auth mechanisms, and free-tier availability are all things that change on a timescale shorter than a single project. Every one of them was worth verifying live rather than trusting memory — including the assistant's own memory of "the model I meant."

---

## Part 10 — The Frontend: A Real UI, With Real Bugs

The `second-brain-ui` React + Vite frontend was scoped deliberately small for v1: one page, no routing, no auth, a chat-style interface calling `/ask`, with citations rendered as clickable chips and (once added) an `obsidian://` deep link back to the real note.

Two functional bugs surfaced only once real screenshots of real output were reviewed — neither would have been caught by "does it render without crashing":

1. **LaTeX/math was not rendering.** `react-markdown` + `remark-gfm` handles Markdown syntax but has no math support built in — every formula in every answer was displaying as raw text with literal dollar signs and backslash commands, which is a serious usability problem given how formula-dense the underlying wiki actually is. The fix required adding `remark-math` and `rehype-katex` specifically, plus KaTeX's CSS.
2. **A claimed feature (in-text image placement, matching a figure to the paragraph discussing it) was asserted as working three separate times before it was ever actually tested with real evidence.** The mechanism itself is worth understanding clearly: the LLM is **not** using a vision API. It reads the *text* around an image reference in the retrieved markdown and is instructed, via system prompt, to weave the image tag into its generated explanation where it judges the content to be relevant. This is a real accuracy risk structurally identical to earlier problems in this project (the model confidently producing a plausible-looking result with no verification step) — and it was flagged as needing the exact same treatment: real test questions, real screenshots, a real correctness check per figure, not a description of how the feature is supposed to work.

**Lesson:** "it looks right" and "I checked several specific instances and they were right" are different claims. Only the second is evidence. This distinction, more than any single technical fix, is the throughline of the entire project.

---

## Part 11 — The Cram Sheet: Where the Depth Requirement Finally Paid Off, and Where It Didn't

A `/generate` endpoint was built to synthesize a consolidated cram sheet across all five audited modules — genuinely the first deliverable meant to be used directly, not just infrastructure. Auditing the *first* version against the verified source pages (not from memory — reading the actual original wiki pages again) found four concrete regressions, all introduced during the LLM's cross-page synthesis step, despite every individual source page already being correct:

| Error | What happened |
|---|---|
| Table row mislabeled | A table row named "Inception" in the verified source was renamed "GoogLeNet" during synthesis — conflating two related but distinct models |
| Fabricated precision | AlexNet's verified 15% error rate became "15.3%" — an invented decimal with no source |
| Two numbers merged under one year | VGGNet's own separately-reported 7.32% error rate got spliced into the "2014" timeline slot, silently displacing GoogLeNet's actual 2014 chart value (6.7%) |
| A range narrowed to a point | The verified "beating human error rate of 5–10%" became "~5%" — changing the actual claim, not just its precision |

This mattered specifically *because* the source pages were already correct — the bug lived entirely in the act of synthesizing across pages, a step with no equivalent guardrail to the one built for single-page ingest. The fix mirrored the earlier depth-requirement fix almost exactly: an explicit, non-negotiable instruction added directly to the `/generate` endpoint's system prompt —

```
CRITICAL INSTRUCTIONS FOR NUMERICAL & TABULAR ACCURACY:
1. Preserve exact numbers without rounding, truncation, or added precision.
2. Reproduce comparison tables with verbatim row titles and exact values.
3. Include all equations with exact LaTeX and equation numbers.
```

A second pass, checked line-by-line against the actual quoted source, confirmed the table and the human-error range were fixed — but two specific line items from the original bug report were never actually re-checked in that pass, a gap only caught by insisting on the *complete* current section quoted in full, rather than accepting a summary claiming "all numbers now match."

**Lesson, the same one as Part 8, applied to a new layer:** every synthesis step introduces a fresh opportunity for the same class of error a previous step already solved. Fixing ingest-time depth didn't fix generate-time depth. Each new capability needs its own explicit accuracy rule — inheriting a fix from a sibling feature is not something that happens automatically.

---

## Part 12 — Cross-Cutting Lessons

Distilled across the entire project, independent of any specific bug:

1. **A claim is not evidence. A quoted, verifiable result is.** This was enforced at every layer — wiki page content, lint script output, API responses, model names, auth mechanisms — and every single time it was enforced, it caught something real.
2. **Vague quality instructions get satisfied at whatever level the model considers sufficient.** "Preserve full detail" failed twice before "list every number and confirm each one appears" succeeded. Specificity is not optional polish; it's the actual mechanism that produces correct output.
3. **Fixing a problem in one place does not fix it in a sibling place.** The depth-requirement rule for ingest didn't protect the later `/generate` synthesis step. Each new capability that touches the same content needs its own explicit guardrail.
4. **An agent's summary of its own past actions is a claim, not a fact**, especially after it contradicts itself. The fix is always to check the actual files, not to arbitrate between two verbal claims.
5. **Environment and dependency state must be written down, not left as tribal knowledge in a scratch script.** A `requirements.txt` freeze plus documented monkeypatches turns "I solved this once, painfully" into "this is reproducible."
6. **Security hygiene applies even to seemingly low-risk local-only keys.** Rotate on exposure, always, regardless of current balance or how contained the leak seems.
7. **Model names, provider auth flows, and free-tier availability all move faster than a build session.** Verify live against the actual provider, every time, rather than trusting a remembered string — including one's own memory of what was meant a few messages earlier.
8. **Deterministic and semantic checks are not interchangeable, and pretending they are creates false confidence.** A mechanical lint script that catches orphan pages cannot catch stale claims — and a report that doesn't say so explicitly will eventually be mistaken for a complete audit.
9. **Two different failure modes ("everything is slow" vs. "one thing hung forever") need two different diagnostics.** Conflating them wastes time chasing the wrong fix.
10. **The riskiest step in any pipeline is the one with no existing guardrail** — not the step that failed last time. Ingest got fixed early because it failed early and visibly. Cross-page synthesis broke *later*, quietly, specifically because nobody had needed to build a guardrail for it yet.

---

## Part 13 — Where to Use What: A Quick Reference

| If you need to... | Use |
|---|---|
| Add a new source to the wiki | `.agents/skills/ingest-source` (calls `pdf-extract` first if the source is a PDF) |
| Check for orphan pages, broken links, index drift (fast, no LLM) | `scripts/lint.py` via the nightly GitHub Action |
| Check for stale claims, contradictions, data gaps (needs real understanding) | `.agents/skills/lint-wiki`, run manually via `/lint` |
| Add a genuinely new domain (not just a new page) | `.agents/skills/add-domain` — after confirming it's not just a new page type |
| Ask a question and get a cited answer | `second-brain-ui`'s `/ask` endpoint, or `.agents/skills/query-wiki` directly in Antigravity |
| Generate a consolidated study document | `/generate`, but only after confirming its system prompt has the same numeric-accuracy guardrail as ingest |
| Extract tables/figures from a dense PDF | `pdf-extract` (Docling), with the vision-parsing fallback for pages it can't structurally parse |
| Verify anything an agent claims it already did | Direct file read / grep against the actual repo — never trust a summary of a summary |

---

## Closing Note

Nothing in this project worked on the first try, and that turns out to be the actual point worth recording. The architecture that exists now — the domain-namespaced schema, the contradiction rule, the audit-before-reingest workflow, the mechanical/semantic lint split, the numeric-accuracy guardrails at two separate layers — is not a plan that was designed up front. It is the residue of specific, verified failures, each one producing a specific, tested fix. That is likely the most transferable lesson here: build the guardrail after the first real failure, verify the fix with actual evidence, and expect the next layer you build to need its own version of the same guardrail — not to inherit one for free.
