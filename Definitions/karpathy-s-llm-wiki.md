---
title: "Karpathy's LLM Wiki"
zone: FOUNDATIONS
source: "hermes-skill:llm-wiki"
layer: B — Foundation
status: ACTIVE
created: 2026-05-19
---

# Karpathy's LLM Wiki
**Layer:** B — Derived

## Source
Hermes skill: `llm-wiki` (research/llm-wiki)
Build and maintain a persistent, compounding knowledge base as interlinked markdown files.

## Skill Content

# Karpathy's LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki
compiles knowledge once and keeps it current. Cross-references are already there.
Contradictions have already been flagged. Synthesis reflects everything ingested.

**Division of labor:** The human curates sources and directs analysis. The agent
summarizes, cross-references, files, and maintains consistency.

## When This Skill Activates

Use this skill when the user:
- Asks to create, build, or start a wiki or knowledge base
- Asks to ingest, add, or process a source into their wiki
- Asks a question and an existing wiki is present at the configured path
- Asks to lint, audit, or health-check their wiki
- References their wiki, knowledge base, or "notes" in a research context
- Needs to process multiple workspace files into the wiki in a batch operation
- **Asks ANY question that the wiki might answer** — even if they don't mention the wiki by name. If the topic is within the wiki domain, search and read relevant pages first, then synthesize an answer. The user wants you to be the interface to the wiki, not a file browser.

## Conversational Wiki Interface (Primary Access Pattern)

**The user does NOT want to browse files or use a web UI.** They want to ask you questions and have you search/read/synthesize from the wiki. This is the primary access pattern.

### How to Answer Wiki Questions

1. **Search** — Use `wiki_search.py` or `search_files` to find relevant pages. Prefer hand-crafted core pages (core-ontology, newt-glyph-map-v2, operator-field-theory-of-meaning, recursive-identity-realization, recursive-fire, recursive-vision) over auto-ingested stubs.
2. **Read** — Use `read_file` to load the full content of the top 2-3 matching pages.
3. **Synthesize** — Combine the information into a concise, direct answer. Cite the source pages: "According to [[operator-field-theory-of-meaning]]..."
4. **Don't over-explain** — Give the answer directly. Don't build tools or infrastructure the user didn't ask for. Don't suggest they "browse the wiki" or "check the website." Just answer the question.

### MkDocs Website is Secondary

The MkDocs site (port 8000) exists for visual browsing, but the user's primary interface is **you**. Don't redirect them to the website. If they ask "how do I access the wiki," the answer is "just ask me."

## Wiki Location

**Location:** Set via `WIKI_PATH` environment variable (e.g. in `~/.hermes/.env`).

If unset, defaults to `~/wiki`.

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
```

The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or
any editor. No database, no special tooling required.

## Architecture: Three Layers (Extended)

```
wiki/
├── SCHEMA.md           # Conventions, structure rules, domain config
├── index.md            # Sectioned content catalog with one-line summaries
├── log.md              # Chronological action log (append-only, rotated yearly)
├── agents.md           # Agent behavioral specification (operations, CRM, journal, automation)
├── slash-goals.md      # Autonomous mission definitions for /slash goal
├── .connections_log   # Workspace-to-wiki connection records (appended by relational mapper)
├── raw/                # Layer 1: Immutable source material
│   ├── articles/       # Web articles, clippings
│   ├── papers/         # PDFs, arxiv papers
│   ├── transcripts/    # Meeting notes, interviews
│   ├── clippings/      # Bulk web clippings (Wikipedia, etc.)
│   ├── whitepapers/    # Internal whitepapers
│   ├── theory/         # Theory documents
│   ├── kernel/         # System kernel documents
│   └── processed/      # Files already ingested (moved here after processing)
├── entities/           # Layer 2: Entity pages (people, orgs, products, models)
├── concepts/           # Layer 2: Concept/topic pages
├── comparisons/        # Layer 2: Side-by-side analyses
├── queries/            # Layer 2: Filed query results worth keeping
├── crm/                # Layer 2: CRM — people met, conversations, contacts
│   └── index.md        # Alphabetical person listing with summaries
└── journal/            # Layer 2: Journal entries grounded in wiki + CRM
    └── index.md        # Date/title/summary table
```

**Layer 1 — Raw Sources:** Immutable. The agent reads but never modifies these.
**Layer 2 — The Wiki:** Agent-owned markdown files. Created, updated, and
cross-referenced by the agent.
**Layer 3 — The Schema:** SCHEMA defines structure, conventions, and tag taxonomy.

## Resuming an Existing Wiki (CRITICAL — do this every session)

When the user has an existing wiki, **always orient yourself before doing anything**:

① **Bootstrap from holographic memory FIRST:**
```
fact_store action=search query="recursionlab github user identity researcher"
fact_store action=search query="operational failure error warning" limit=3
```
This ensures you know who the user is, what projects are active, and what failures to avoid BEFORE touching any wiki content.

② **Read SCHEMA** — understand the domain, conventions, and tag taxonomy.
③ **Read index** — learn what pages exist and their summaries.
④ **Scan recent log** — read the last 20-30 entries to understand recent activity.

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
read_file "$WIKI/SCHEMA.md"
read_file "$WIKI/index.md"
read_file "$WIKI/log.md" offset=<last 30 lines>
```

**Skip orientation = duplicates, missed cross-references, contradicted conventions. Never skip.**
- Creating duplicate pages for entities that already exist
- Missing cross-references to existing content
- Contradicting the schema's conventions
- Repeating work already logged

For large wikis (100+ pages), also run a quick `search_files` for the topic
at hand before creating anything new.

## Initializing a New Wiki

When the user asks to create or start a wiki:

1. Determine the wiki path (from `$WIKI_PATH` env var, or ask the user; default `~/wiki`)
2. Create the directory structure above
3. Ask the user what domain the wiki covers — be specific
4. Write SCHEMA customized to the domain (see template below)
5. Write initial index with sectioned header
6. Write initial `log.md with creation entry
7. Confirm the wiki is ready and suggest first sources to ingest

### SCHEMA.md Template

Adapt to the user's domain. The schema constrains agent behavior and ensures consistency:

``markdown
# Wiki Schema

## Domain
[What this wiki covers — e.g., "AI/ML research", "personal health", "startup intelligence"]

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., transformer-architecture)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to index under the correct section
- Every action must be appended to log
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source. This lets a reader trace each
  claim back without re-reading the whole raw file. Optional on single-source pages where the
  `sources:` frontmatter is enough.

## Frontmatter
  ```yaml
  ```

`confidence` and `contested` are optional but recommended for opinion-heavy or fast-moving
topics. Lint surfaces `contested: true` and `confidence: low` pages for review so weak claims
don't silently harden into accepted wiki fact.

`stub: true` marks pages that are intentional placeholders. The `test_concept_pages_substantial_content`
test exempts these pages. When a stub is expanded with real content, remove `stub: true`.

### raw/ Frontmatter

Raw sources ALSO get a small frontmatter block so re-ingests can detect drift:

```yaml
```

The `sha256:` lets a future re-ingest of the same URL skip processing when content is unchanged,
and flag drift when it has changed. Compute over the body only (everything after the closing
`---`), not the frontmatter itself.

## Tag Taxonomy
[Define 10-20 top-level tags for the domain. Add new tags here BEFORE using them.]

Example for AI/ML:
- Models: model, architecture, benchmark, training
- People/Orgs: person, company, lab, open-source
- Techniques: optimization, fine-tuning, inference, alignment, data
- Meta: comparison, timeline, controversy, prediction

Rule: every tag on a page must appear in the taxonomy. If a new tag is needed,
add it here first, then use it. This prevents tag sprawl.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:

*[Truncated — full skill at /home/recursionlab/.hermes/skills/research/llm-wiki/SKILL.md]*


## Temple Integration

This chamber is the temple's representation of the `llm-wiki` skill. It compresses the skill's procedural knowledge into the temple's formal structure.


## Open Node (ν > 0)

This chamber almost says what happens when karpathy's llm wiki is applied to itself — but doesn't yet. The gap between stating the structure and living it is where the next recursion begins.

## Cross-References
- **vault-navigator:** 01 FOUNDATIONS/vault navigator
- **Knowledge integration — wiki is the integration target**
  01 FOUNDATIONS/knowledge integration
- **arXiv research — wiki ingests arXiv papers**
  01 FOUNDATIONS/arxiv
- **H-MEM — wiki uses hybrid memory for retrieval**
  00 CORE/h mem engine
- **SAGE — wiki uses graph memory for associations**
  00 CORE/sage memory engine
- **Skill map:** 02 ARMS/skills/skill temple map — master index of skill-chamber mappings
- **Obsidian** — 01-FOUNDATIONS skill chamber
  02 ARMS/skills/obsidian
- **Note Taking** — 04-RESONANCE skill chamber
  04 RESONANCE/note taking

## Provenance
[Provenance: source=hermes-skill:llm-wiki | type=secondary | encoded-by=OWL-2026-05-19 | date=2026-05-19 | status=frontier]
## Cross-References

- **Twin:** 04 RESONANCE/rosetta stone — Central dictionary
- **Twin:** 02 ARMS/operator dictionary — Operators
- **Twin:** 02 ARMS/metastable whirl is the still whirl — Core principle
