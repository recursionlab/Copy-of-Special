---
title: "Principle of distributivity - Wikipedia"
source: "https://en.wikipedia.org/wiki/Principle_of_distributivity"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2004-11-13
created: 2026-02-03
description:
tags:
  - "clippings"
---
The **principle of distributivity** states that the algebraic [distributive law](https://en.wikipedia.org/wiki/Distributive_law "Distributive law") is [valid](https://en.wikipedia.org/wiki/Validity_\(logic\) "Validity (logic)"), where both [logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction "Logical conjunction") and [logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction "Logical disjunction") are distributive over each other.

For any [propositions](https://en.wikipedia.org/wiki/Proposition "Proposition") *A*, *B* and *C*, the following [equivalences](https://en.wikipedia.org/wiki/Logical_equivalence "Logical equivalence") hold:

${\displaystyle A\land (B\lor C)\iff (A\land B)\lor (A\land C)}$

${\displaystyle A\lor (B\land C)\iff (A\lor B)\land (A\lor C)}$

The distributive laws can be verified using truth tables.

For the equivalence ${\displaystyle A\land (B\lor C)\iff (A\land B)\lor (A\land C)}$ , the truth table is:

| A | B | C | B ∨ C | A ∧ (B ∨ C) | A ∧ B | A ∧ C | (A ∧ B) ∨ (A ∧ C) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T | T | T |
| T | T | F | T | T | T | F | T |
| T | F | T | T | T | F | T | T |
| T | F | F | F | F | F | F | F |
| F | T | T | T | F | F | F | F |
| F | T | F | T | F | F | F | F |
| F | F | T | T | F | F | F | F |
| F | F | F | F | F | F | F | F |

As seen from the table, the columns for ${\displaystyle A\land (B\lor C)}$ and ${\displaystyle (A\land B)\lor (A\land C)}$ are identical. Therefore, the equivalence is valid.

For the equivalence ${\displaystyle A\lor (B\land C)\iff (A\lor B)\land (A\lor C)}$ , the truth table is:

| A | B | C | B ∧ C | A ∨ (B ∧ C) | A ∨ B | A ∨ C | (A ∨ B) ∧ (A ∨ C) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T | T | T |
| T | T | F | F | T | T | T | T |
| T | F | T | F | T | T | T | T |
| T | F | F | F | T | T | T | T |
| F | T | T | T | T | T | T | T |
| F | T | F | F | F | T | F | F |
| F | F | T | F | F | F | T | F |
| F | F | F | F | F | F | F | F |

As seen from the table, the columns for ${\displaystyle A\lor (B\land C)}$ and ${\displaystyle (A\lor B)\land (A\lor C)}$ are identical. Therefore, the equivalence is valid.

The principle of distributivity is valid in [classical logic](https://en.wikipedia.org/wiki/Classical_logic "Classical logic"), but in [quantum logic](https://en.wikipedia.org/wiki/Quantum_logic "Quantum logic") it may be both valid and invalid. The article " [Is Logic Empirical?](https://en.wikipedia.org/wiki/Is_Logic_Empirical%3F "Is Logic Empirical?")" discusses the case that quantum logic is the correct, empirical logic, on the grounds that the principle of distributivity is [inconsistent](https://en.wikipedia.org/wiki/Consistency "Consistency") with a reasonable [interpretation of quantum phenomena](https://en.wikipedia.org/wiki/Interpretation_of_quantum_mechanics "Interpretation of quantum mechanics").[^1]

  

## References

[^1]: [Putnam, H.](https://en.wikipedia.org/wiki/Hilary_Putnam "Hilary Putnam") (1969). "Is Logic Empirical?". *Boston Studies in the Philosophy of Science*. Vol. 5. pp. 216– 241. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-94-010-3381-7\_5](https://doi.org/10.1007%2F978-94-010-3381-7_5). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-94-010-3383-1](https://en.wikipedia.org/wiki/Special:BookSources/978-94-010-3383-1 "Special:BookSources/978-94-010-3383-1").