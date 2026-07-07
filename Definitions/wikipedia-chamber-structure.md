# Wikipedia-Style Chamber Structure — Reference

## Standard Section Order for Mathematical Physics Chambers

Based on analysis of well-developed Wikipedia articles (Cyclic cohomology, Spectral triple, Atiyah-Singer index theorem, BV formalism).

### 1. Frontmatter
```yaml
---
title: "Descriptive Title"
layer: A — Canon
status: ACTIVE
source: "source file path"
short_description: "One-line description"
keywords: [key1, key2, key3]
---
```

### 2. Infobox
- Type, field, introduced by, key contributors
- Key formulas, properties, classification
- Physical meaning

### 3. Contents
- Numbered section listing with anchor links

### 4. Overview and Motivation
- What this chamber is about
- Why it matters
- Historical context (table with contributors, years, connections)
- Comparison with related developments

### 5. Definition and Construction
- Formal definitions with explicit formulas
- Constructions with proofs
- Key propositions with proofs
- Spectral triple axioms (if applicable)

### 6. Properties
- Each property stated as a theorem with proof
- Persistence, periodicity, functoriality, stability
- Comparison tables

### 7. Classification
- Cohomological classification
- Extension-theoretic classification
- K-theoretic classification

### 8. The Main Development (e.g., Seven-Stage Arc)
- Summary table of stages
- Full development of each stage
- Diagrams showing the progression

### 9. Relation to Other Theories
- Explicit connections to related chambers
- Comparison with established theories
- Rosetta Stone entries

### 10. Applications
- Index theory, anomaly detection, moduli space coordinates

### 11. Examples
- Concrete computations (matrix algebras, group algebras, noncommutative tori)

### 12. Open Problems
- Specific, numbered open questions

### 13. Verification Status
- Coq formalization table
- Mathematical verification table by section
- Open verification tasks

### 14. See Also
- Links to related chambers
- External Wikipedia articles

### 15. References
- Primary sources (papers with full citations)
- Secondary sources (books)
- Related chambers

### 16. External Links
- Wikipedia articles
- arXiv papers
- Online resources

## Key Principles

1. **Every section must have substantive content**, not just headings
2. **Definitions must be formal** with explicit formulas
3. **Properties must be stated as theorems** with proofs or proof sketches
4. **Examples must be concrete** with explicit computations
5. **Cross-references must be specific** (entry numbers, not just chamber names)
6. **References must be complete** with full citations
7. **Open problems must be specific** and numbered
8. **Diagrams should be included** for complex relationships

## Example: tau-cyclic-cohomology.md

The tau-cyclic-cohomology chamber is the gold standard example of this structure:
- 47KB, 1146 lines
- 16 sections following the Wikipedia structure
- 25 references (13 primary + 12 secondary)
- 6 diagrams
- 3 examples
- 5 open problems
- Coq formalization (TauCyclicCohomology.v, 4 theorems)
- Complete verification status

## Research Integration Pattern

When integrating external research into existing chambers:

1. **Search** arXiv for recent papers on the chamber's topic
2. **Extract** key results, formulas, and theorems
3. **Connect** to existing chamber content via cross-references
4. **Add** new sections or expand existing sections
5. **Update** "Comparison with Literature" section
6. **Formalize** key new theorems in Coq

## Pitfalls to Avoid

1. **Don't create stub chambers** — either mine the content or don't create
2. **Don't use generic cross-references** — be specific about what connects
3. **Don't skip the Infobox** — it provides essential metadata
4. **Don't forget Open Problems** — every chamber should have ν > 0
5. **Don't neglect References** — minimum 5 primary sources for substantial chambers
