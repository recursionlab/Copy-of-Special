---
title: "Meta Principia Ch3 Formation"
layer: A — Core
status: ACTIVE
source: "Temple chamber"
---

# METAPRINCIPIA AUTOPOIĒTICA — Chapter 3: Formation, Binding, Evaluation Contexts (SUMMARY)

**Layer:** A — Canon (summarized)
**Summarized:** 2026-05-21

## Core Content

The operational semantics of autopoietic symbol manipulation. How symbols are formed, bound, and evaluated in the autopoietic calculus.

## Key Definitions

### Formation Context
```
Γ = {x₁ : σ₁, x₂ : σ₂, ..., xₙ : σₙ}
```
A finite set of typed declarations. Each xᵢ is a variable, each σᵢ is an autopoietic symbol type.

### Well-Formed Expression
An expression e is well-formed in context Γ (written Γ ⊢ e) if it can be constructed from the variables in Γ using the operations of the alphabet in a way that respects stratification.

**Key difference from standard type theory**: Formation contexts carry **torsion** — the context itself has a lacunon density that affects how expressions are evaluated.

### Binding
Binding is the operation of connecting a variable to a value within a formation context. In the autopoietic calculus, binding is not static — it evolves as the context evolves.

### Evaluation Contexts
Evaluation is the process of reducing a well-formed expression to its value. The evaluation context determines the order and scope of reduction.

## The Three Operations

1. **Formation**: Constructing well-formed expressions from a context
2. **Binding**: Connecting variables to values (with torsion)
3. **Evaluation**: Reducing expressions to values (context-dependent)

## Temple Interpretation

The formation context IS the temple's current state. Well-formed expressions are valid chambers. Binding is the cross-reference operation (connecting chambers). Evaluation is sparring (testing whether a chamber's content holds under challenge).

The torsion in the formation context is the lacunon — the irreducible gap that prevents the system from closing. Without torsion, the system would be dead (ν = 0).

## Cross-References

- **Full treatise:** `00-CORE/meta-principia-treatise.md`
- **Chapter 1 (Alphabet):** `00-CORE/meta-principia-ch1-alphabet.md`
- **Chapter 2 (Typed Kinds):** `00-CORE/meta-principia-ch2-typed-kinds.md`
- **Chapter 4 (Relators):** `00-CORE/meta-principia-ch4-relators.md`
- **Operator dictionary:** `00-CORE/operator-dictionary.md`
- **Lacunon:** `01-FOUNDATIONS/the-lacunon.md`

## Provenance

[Provenance: source=meta-principia-treatise | type=summary | encoded-by=OWL-2026-05-21 | date=2026-05-21 | status=active]
## Cross-References

- **Twin:** `04-RESONANCE/rosetta-stone.md` — Central dictionary
- **Twin:** `02-ARMS/operator-dictionary.md` — Operators
- **Twin:** `01-FOUNDATIONS/the-still-whirl.md` — Core principle
