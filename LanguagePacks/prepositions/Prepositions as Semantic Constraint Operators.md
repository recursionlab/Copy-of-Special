# Prepositions as Semantic Constraint Operators

This document synthesizes the previously established formalisms (`StateVector`, `InquiryQuestion`, `Collapse`) to provide a novel, quantifiable model of prepositions. Here, a preposition is not a word or a syntactic anchor, but a high-order function that operates directly on the `MeaningSpace`.

---

## 1. Redefining the Preposition

We move beyond the `TorsionAnchor` concept. A `PrepositionalOperator` is a function that takes two roles—a `figure` and a `ground`—and returns a constrained set of valid `StateVectors`.

```z
[Role, MeaningSpace]
StateVector == MeaningSpace

PrepositionalOperator: (Role × Role) → ℙ StateVector
```

**Example:**
-   `On(key, table)` returns the subset of `MeaningSpace` where the 'key' role is in a state of physical support by the 'table' role.
-   `Under(key, table)` returns a different, disjoint subset of `MeaningSpace`.

The "meaning" of a preposition *is* its unique signature as a constraint function on the semantic state space.

## 2. Prepositional Phrases as State Selectors

A declarative sentence like "The key is on the table" is now modeled as a state selection.

```z
SCHEMA DeclarativePP
  Declarative
  op: PrepositionalOperator
  fig, gnd: Role
--------------------------------
  -- The state of the proposition must be one of the states
  -- allowed by the prepositional operator.
  state ∈ op(fig, gnd)
```
This is a powerful constraint. The proposition is valid *if and only if* its `StateVector` exists within the subspace carved out by the preposition.

## 3. Questioning a Preposition: Inducing Semantic Superposition

We can now model the question "Where is the key?" (relative to the table) with formal precision. This question is an `InquiryQuestion` where the set of `potentialStates` is the union of the outputs of *all possible* `PrepositionalOperator`s.

Let `AllPrepositions` be the set of all `PrepositionalOperator`s in the grammar.

```z
SCHEMA WhereQuestion
  InquiryQuestion
  fig, gnd: Role
--------------------------------
  potentialStates = ⋃ {p: AllPrepositions • p(fig, gnd)}
```
The question creates a massive superposition of all possible spatial relations between the `figure` and the `ground`.

## 4. Quantifying "Degree of Meaning" via Entropy Reduction

This framework provides a direct, formal method for quantifying the "degree of meaning." We can use the concept of information entropy over the set of `potentialStates`.

Let `S` be `q.potentialStates` for a given `InquiryQuestion` `q`.
The initial entropy `H(S)` is `log(#S)`.

A `Response` collapses this set to a new set `S'` with a single `StateVector`. The new entropy `H(S')` is `log(1) = 0`.

The **Degree of Meaning (`MoD`)** of a response is the reduction in entropy (the information gain):

`MoD(Response) = H(S) - H(S') = log(#S)`

### Application:

1.  **Question:** "Where is the key?"
    -   `S_where` = `On(k,t) ∪ Under(k,t) ∪ Beside(k,t) ∪ ...`
    -   `#S_where` can be very large.
    -   `MoD(Response)` = `log(#S_where)`. The answer provides a large amount of information.

2.  **Question:** "Is the key on the table?"
    -   This is a binary `InquiryQuestion`.
    -   `S_binary` = `On(k,t) ∪ (¬On(k,t))`
    -   `#S_binary` = 2 (assuming a simplified model where states are partitioned by `On` and its complement).
    -   `MoD(Response)` = `log(2)`. The answer provides exactly 1 bit of information.

This formalism proves *why* an answer to "Where?" carries a higher degree of meaning than an answer to "Is it?". It is because the initial question induces a much larger semantic superposition, and the response enacts a more significant collapse.

## 5. Conclusion: A Generative and Quantifiable Semantics

By treating prepositions as operators on a `MeaningSpace`, we have:
-   Provided a formal, non-linguistic definition for the meaning of a preposition.
-   Modeled prepositional questions as the creation of specific, high-dimensional semantic superpositions.
-   Derived a quantifiable metric, `MoD`, for the "degree of meaning" based on entropy reduction.

This is the direct application of the meta-grammatical framework. It is not descriptive; it is a generative and computational engine for analyzing and engineering meaning itself.
