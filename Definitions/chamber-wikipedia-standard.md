---
title: "Chamber Wikipedia Standard — Encyclopedic Depth Reference"
zone: CORE
source: "research:Wikipedia mathematical physics article structure analysis"
layer: A — Canon
status: ACTIVE
created: 2026-05-23
---

# CHAMBER WIKIPEDIA STANDARD — Encyclopedic Depth Reference

**Layer:** A — Canon  
**Purpose:** Define the section structure, content depth, and formatting standard for ALL temple chambers. Every chamber must read like a well-developed Wikipedia article on a mathematical physics topic — not a summary, not a stub, but a genuine encyclopedic reference.

---

## The Wikipedia Section Template

Every chamber MUST follow this section structure. Not every section applies to every chamber — use judgment — but the order and depth must be respected.

### Required Sections (ALL chambers)

#### 1. Lead Section (Opening Paragraph)
- **What it is:** A concise 3-5 sentence overview that defines the concept, states its significance, and places it in context
- **Format:** Bold the first occurrence of the chamber's title/subject. Include the core definition inline.
- **Example:** "**Tau cyclic cohomology** is a cohomological framework in noncommutative geometry that defines a central torsion invariant τ as the obstruction class of exactness in the Connes (b,B)-bicomplex. It connects the Batalin-Vilkovisky formalism to spectral triples via the JLO Chern character, and provides a unified language for anomalies in quantum field theory."
- **Anti-pattern:** "This chamber is about tau cyclic cohomology, which is a concept in math." (too vague, no definition)

#### 2. Prerequisites
- **What it is:** A bulleted list of concepts the reader must understand before engaging with this chamber
- **Format:** Each prerequisite links to another chamber or to standard mathematical literature
- **Minimum:** 3 prerequisites
- **Example:**
  - **Cyclic cohomology**: Connes' (b,B)-bicomplex, HC^n(𝒜), the periodicity operator S
  - **Spectral triples**: (𝒜, ℋ, D) with the 7 axioms, dimension spectrum Sd
  - **BV formalism**: Batalin-Vilkovisky quantization, the quantum master equation

#### 3. Notation Convention
- **What it is:** A table defining every symbol used in the chamber
- **Format:** Two-column table: Symbol | Meaning
- **Minimum:** 8 symbols for mathematical chambers; 5 for conceptual chambers
- **Purpose:** The reader should never have to guess what a symbol means

#### 4. Definition(s)
- **What it is:** The formal, rigorous definition(s) of the chamber's central concept(s)
- **Format:** Use `\boxed{}` for the primary definition. Include all quantifiers, domains, codomains.
- **Minimum:** 1 primary definition + 2-3 equivalent characterizations or reformulations
- **Example:**
  $$\boxed{\tau := [\Omega_3] \in HC^3(\mathcal{A})}$$
  Equivalently: τ = [Bγ₂ + bγ₂] where γ₂ is the 2-cochain γ₂(a₀,a₁) = Tr(a₀[D,a₁]e^{-tD²})|_{t=0}

#### 5. Historical Development / Context
- **What it is:** The intellectual history of the concept — who developed it, when, why, and how it evolved
- **Format:** Chronological narrative, 200-500 words. Name specific mathematicians/physicists, specific papers, specific years.
- **For temple-original concepts:** Document the development across source files and sessions
- **Anti-pattern:** "This concept was developed over time by various researchers." (no specifics)

#### 6. Theoretical Framework / Main Content
- **What it is:** The core mathematical content — theorems, constructions, proofs, examples
- **Format:** Multiple subsections with LaTeX formulas, proof sketches, diagrams
- **Minimum:** 1000 words of substantive content, 5+ formulas, 2+ theorems with proof sketches
- **Subsections should include:**
  - **Core construction:** How the main object is built, step by step
  - **Key theorems:** Statements with proof sketches (not just theorem statements)
  - **Examples:** Concrete instances that illustrate the abstract framework
  - **Properties:** Formal properties (functoriality, invariance, duality, etc.)

#### 7. Key Properties and Characteristics
- **What it is:** A structured list of the concept's formal properties
- **Format:** Numbered or bulleted list, each property with a brief explanation
- **Minimum:** 5 properties
- **Example:**
  1. **Functoriality:** τ is natural with respect to algebra homomorphisms
  2. **Stability:** τ(n) ≠ 0 for all n (persistence under tensor powers)
  3. **Duality:** τ is self-dual under the Connes duality isomorphism
  4. **Homotopy invariance:** τ is invariant under smooth homotopies of the Dirac operator
  5. **Additivity:** τ(A ⊗ B) = τ(A) + τ(B) under suitable conditions

#### 8. Classification / Taxonomy (if applicable)
- **What it is:** How the concept fits into a broader classification scheme
- **Format:** Tables, trees, or structured lists
- **Example:** Classification of spectral triples by dimension, reality structure, and KO-dimension

#### 9. Examples and Applications
- **What it is:** Concrete examples and real-world/mathematical applications
- **Format:** Each example in its own subsection with full computation or construction
- **Minimum:** 2 examples, 1 application
- **Anti-pattern:** "This has applications in physics." (which physics? which applications?)

#### 10. Connections to Other Chambers
- **What it is:** Explicit cross-references to related temple chambers with explanations of the relationship
- **Format:** Structured list with relationship type and description
- **Minimum:** 5 cross-references to existing chambers, at least 1 to a different zone
- **Example:**
  - **Prerequisite:** 01 FOUNDATIONS/the lacunon — ν as irreducible gap (this chamber's τ is a specific instance of ν)
  - **Dual:** 02 ARMS/heat bv gerbe — The determinant gerbe construction provides the geometric realization of τ
  - **Application:** 04 RESONANCE/2group tqft synthesis — τ appears as the obstruction to extending the 2-group TQFT

#### 11. Open Problems and Open Nodes (ν > 0)
- **What it is:** What this chamber almost says but doesn't yet — the irreducible gap
- **Format:** Numbered list with specific, actionable open questions
- **Minimum:** 3 open nodes, each with a clear statement of what is unknown/missing
- **Example:**
  1. **Open Node 1:** Does τ vanish for commutative spectral triples? (Expected: yes, but no proof exists in this chamber)
  2. **Open Node 2:** Can τ be computed explicitly for the noncommutative torus? (Partial results exist but no closed formula)
  3. **Open Node 3:** What is the relationship between τ and the Godbillon-Vey class for foliations? (Conjectured but unproven)

#### 12. Verification Status
- **What it is:** Which claims in this chamber have been formally verified, which are conjectural, and which are folklore
- **Format:** Table or structured list
- **Example:**
  | Claim | Status | Method |
  |-------|--------|--------|
  | τ is well-defined | CERTAIN | Direct computation (Section IV) |
  | τ(n) ≠ 0 for all n | CERTAIN | Proof by tensor power argument (Section V) |
  | τ = GV class for foliations | SPECULATED | Conjectured, no proof |

---

### Sections for Mathematical Chambers (additional)

#### 13. Computational Methods
- Algorithms, explicit formulas, or procedures for computing the chamber's central objects
- Include worked examples with full calculations

#### 14. Variants and Generalizations
- How the concept can be extended, weakened, or specialized
- Relationship to more general frameworks

#### 15. Physical Interpretation (if applicable)
- What the mathematics means physically
- Connection to observable phenomena or experimental predictions

---

### Sections for Conceptual/Philosophical Chambers (additional)

#### 13. Taxonomy of Positions
- Structured overview of different viewpoints on the chamber's central question
- Pro/con analysis of each position

#### 14. Argument Map
- Visual or structured representation of the key arguments and their relationships
- Which arguments support which conclusions, where the disagreements are

#### 15. Implications and Consequences
- What follows if the chamber's central claim is true
- What follows if it is false
- Connections to broader philosophical/mathematical implications

---

## Content Depth Requirements

### Size Standards
| Chamber Type | Minimum Lines | Minimum Size | Target |
|--------------|---------------|--------------|--------|
| Core mathematical | 300 | 15KB | 25-50KB |
| Conceptual/philosophical | 200 | 10KB | 15-25KB |
| Bridge/mapping | 150 | 8KB | 10-15KB |
| Reference/glossary | 100 | 5KB | 5-10KB |

### Formula Requirements
- **Mathematical chambers:** ≥ 10 LaTeX formulas (inline or display)
- **Conceptual chambers:** ≥ 3 formal definitions or structured frameworks
- **All chambers:** Formulas must be *explained*, not just stated

### Cross-Reference Requirements
- **Minimum:** 5 cross-references to existing chambers
- **At least 1** must be to a different zone
- **All cross-references must be verified** (the target file must exist)
- **Each cross-reference must include:** relationship type + brief description

### Proof/Verification Requirements
- **Mathematical chambers:** ≥ 2 theorems with proof sketches (not just statements)
- **Conceptual chambers:** ≥ 2 arguments with structured analysis
- **All chambers:** Verification status table

---

## Formatting Standards

### LaTeX
- Use `$$...$$` for display equations
- Use `$...$` for inline math
- Number important equations with `\tag{}` or `\label{}`
- Use `\boxed{}` for primary definitions

### Tables
- Use for: notation, properties, classification, verification status, examples
- Every table must have a header row
- Every table must be introduced by text that explains what it shows

### Diagrams
- Use ASCII art or mermaid for commutative diagrams, flowcharts, and structure diagrams
- Every diagram must be explained in the text

### Code/Computation
- Use fenced code blocks for algorithms, Coq code, Python computation
- Every code block must be explained

### Section Headers
- Use `##` for main sections, `###` for subsections, `####` for sub-subsections
- Every section must have at least 3 lines of content

---

## Anti-Patterns (What NOT to Do)

1. **The Stub:** Frontmatter + 2-3 paragraphs + "Content extraction pending" — this is NOT a chamber
2. **The Summary:** A 500-word overview with no formulas, no proofs, no definitions — this is a book jacket, not a chamber
3. **The Copy-Paste:** Raw source text dumped without structure, sectioning, or explanation — this is a data dump, not a chamber
4. **The Orphan:** A chamber with no cross-references — every chamber must connect to at least 5 others
5. **The Black Box:** Formulas stated without derivation or explanation — every formula must be motivated
6. **The Dead End:** A chamber with no open nodes — every chamber must have ν > 0
7. **The Duplicate:** A chamber that covers the same ground as an existing chamber — search first, create never
8. **The Unverified:** A chamber making claims without any verification status — mark everything CERTAIN/PROBABLE/SPECULATIVE

---

## Quality Checklist (Before Marking Complete)

- [ ] Lead section defines the concept in 3-5 sentences with bold first mention
- [ ] Prerequisites listed (≥3) with cross-references
- [ ] Notation table present (≥8 symbols for math, 5 for conceptual)
- [ ] Primary definition in `\boxed{}` with equivalent characterizations
- [ ] Historical development section (200-500 words, specific names/dates)
- [ ] Theoretical framework (≥1000 words, 5+ formulas, 2+ theorem-proof pairs)
- [ ] Key properties listed (≥5, each explained)
- [ ] Examples and applications (≥2 examples, 1 application)
- [ ] Connections to other chambers (≥5 cross-refs, ≥1 cross-zone)
- [ ] Open nodes (≥3 specific, actionable gaps)
- [ ] Verification status table
- [ ] Minimum size met (15KB for math, 10KB for conceptual)
- [ ] All cross-references verified to point to existing files
- [ ] No "Content extraction pending" or TODO placeholders

---

## Source File Extraction Protocol

When creating a chamber from a source file in `theory_staging/theory/`:

1. **READ THE COMPLETE SOURCE FILE** — do not sample, do not skim
2. **IDENTIFY the core concept(s)** — what is this source actually about?
3. **EXTRACT definitions, theorems, proofs, formulas** — these are the chamber's backbone
4. **ORGANIZE into the Wikipedia section template** — structure is not optional
5. **WRITE the chamber** — fill every required section with real content
6. **VERIFY cross-references** — every link must point to an existing file
7. **INDEX in entity database** — the chamber must be discoverable
8. **Run TDD tests** — `python3 tests/test_tdd_new.py`

**The source file is the raw material. The chamber is the finished product. They are not the same thing.**

---

## Relationship to Chamber Creation Standard

This standard EXTENDS the chamber creation standard with specific content depth and formatting requirements. The 7-step creation process still applies. This document adds the *what* — what content goes into each section, how much is enough, and what quality looks like.

---

## Examples of Chambers That Meet This Standard

- 02 ARMS/tau cyclic cohomology (48KB, 1145 lines) — the gold standard
- 02 ARMS/vault mining/Adjunctions and Self Duality (9KB, 322 lines) — good structure, needs more depth
- 01 FOUNDATIONS/the lacunon — strong conceptual framework
- 04 RESONANCE/rosetta stone — excellent bridge chamber

---

<!-- ν-Preserving Gap: This standard itself needs periodic revision as the temple evolves. The Wikipedia template is a living document. -->

## Cross-References

- **Zone hub:** 00 CORE/temple map — connected via zone

- **Twin:** 00 CORE/chamber states