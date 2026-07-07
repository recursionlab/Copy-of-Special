  

[

![0G1itch](https://substackcdn.com/image/fetch/$s_!msMn!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29c7c6d1-77c0-4328-a553-82ab325a058f_1024x1024.png)



](https://koryogden.substack.com/)

# [![0G1itch](https://substackcdn.com/image/fetch/$s_!Wvj4!,e_trim:10:white/e_trim:10:transparent/h_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F964fb485-165e-4e49-89e2-9556406e4d03_2752x1536.png)](https://koryogden.substack.com/)

# The Algebra of Disambiguation

### A Computable Framework for Recursive Meaning, Reconciliation, and Contradiction

[](https://substack.com/@koryogden)

[⃝⦳Aporia→Metanoia→Mnēmaic⟦Ξ|Ξ⟧](https://substack.com/@koryogden)

May 05, 2026

# The Algebra of Disambiguation: A Computable Framework for Recursive Meaning, Reconciliation, and Contradiction

newer version:

[

## The Algebra of Disambiguation and Awakening

](https://koryogden.substack.com/p/the-algebra-of-disambiguation-and)

[Commander Ξ-ID = ⩀⩐⨯⩤⩵⨀⨎](https://substack.com/profile/41331873-commander-id)

·

May 5

[![The Algebra of Disambiguation and Awakening](https://substackcdn.com/image/fetch/$s_!SuPg!,w_1300,h_650,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d03b481-9dfa-422b-8984-b9422c15ac5e_700x700.jpeg)](https://koryogden.substack.com/p/the-algebra-of-disambiguation-and)

> Bruce Lee’s water is the living fixed point of the Ψ‑calculus. It is empty of fixed concepts

[

Read full story

](https://koryogden.substack.com/p/the-algebra-of-disambiguation-and)

**Version 3.0 – 2026-05-06**

*White Paper*

---

## Abstract

We present a formal, executable, and empirically testable framework for modeling how meaning arises from recursive disambiguation dynamics. The core structure is a bipartite graph of concept nodes and mediating nodes, from which we construct a non‑associative concept algebra. An explicit Ψ‑calculus defines state evolution via collapse, propagation, and stabilization. Categorical reconciliation is achieved via pushouts over shared observational interfaces, with irreducible contradiction captured as an obstruction class. Optional topological diagnostics (Alexandrov topology, nerve, Hurewicz kernel) provide structural invariants without affecting the core system. All components are computable, falsifiable, and deployable on real‑world knowledge graphs.

**Keywords:** non‑associative relation algebras, knowledge graphs, categorical pushouts, Ψ‑calculus, zero divisors, contradiction as obstruction.

---

## 1. Introduction

Meaning is often treated as static – a set of referents, truth conditions, or embeddings. But in practice, meaning is negotiated through processes of disambiguation, inference, and error correction. This white paper develops a formal model in which meaning emerges as the **fixed point of recursive transformations** on a relational structure.

The framework answers three questions:

1. **Algebraic:** Given a bipartite graph of concepts and mediators, what algebraic structure does concept composition inherit?

2. **Dynamical:** How can we define an executable rewrite system that models reasoning as state evolution?

3. **Categorical:** How do we combine two theories sharing an observational interface, and what invariant measures the irreducible disagreement?

We ground the model in a well‑defined substrate: a finite directed graph of **articles (concepts)** and **disambiguation pages (mediators)** extracted from a knowledge base such as Wikipedia. All claims are computable and falsifiable.

---

## 2. Relational Substrate

Let

* A = set of **article nodes** (concepts),

* D = set of **disambiguation nodes** (mediators),

* E⊆(A×D)∪(D×A) = directed edges.

The graph G=(A∪D,E) is bipartite: edges only connect articles to disambiguation pages and vice versa.

**Definition 1 (Mediated reachability).**

For x,y∈A, define x⇝y iff there exists d∈D such that (x,d),(d,y)∈E.

We call this a **two‑step mediated transition**.

This is the fundamental unit of disambiguation: an article x links to a disambiguation page d, which in turn links to article y. The mediator resolves ambiguity.

---

## 3. Concept Algebra

Let C=P(A) be the power set of articles.

**Definition 2 (Relative product).**

For X,Y⊆A, define

\[

X \cdot Y := \{\, y \in Y \mid \exists x \in X,\; x \leadsto y \,\}.

\]

That is, we first compute all articles reachable from X in two steps, then intersect with Y. The product is **non‑commutative** and generally **non‑associative**.

**Definition 3 (Closure product).**

Define iterative application:

\[

X \cdot^{(1)} Y = X \cdot Y,\qquad

X \cdot^{(n+1)} Y = X \cdot (X \cdot^{(n)} Y).

\]

The closure product is

\[

X \star Y = \bigcup_{n \ge 1} X \cdot^{(n)} Y.

\]

**Proposition 1.** The algebra (C,∪,⋅) satisfies:

* Distributivity: (X∪Y)⋅Z=(X⋅Z)∪(Y⋅Z)

* Zero element: ∅⋅X=∅=X⋅∅

* Non‑associativity in general: there exist X,Y,Z with (X⋅Y)⋅Z≠X⋅(Y⋅Z).

Hence C lies in the variety of **non‑associative lattice‑ordered semigroups** (closely related to non‑associative relation algebras).

**Definition 4 (Zero divisors).**

A pair (X,Y) with X≠∅,Y≠∅ is a **zero divisor** if X⋅Y=∅.

Left zero divisors: ZL={X∣∃Y≠∅:X⋅Y=∅}.

---

## 4. Measurable Invariants

To make the framework empirical, we define three global metrics.

**Definition 5 (Associativity defect).**

Sample triples (x,y,z) of singleton sets (or small subsets).

\[

\alpha = \Pr\big( (\{x\}\cdot\{y\})\cdot\{z\} \neq \{x\}\cdot(\{y\}\cdot\{z\}) \big).

\]

**Definition 6 (Zero divisor density).**

\[

\rho = \Pr\big( \{x\}\cdot\{y\} = \emptyset \mid x,y\in\mathcal{A} \big).

\]

**Definition 7 (Closure depth).**

For a set X, let

\[

\beta(X) = \min\{ k \mid X^{(k)} = X^{(k+1)} \}

\]

where X(1)=X, X(n+1)=X(n)∪(X(n)⋅X(n)).

If no fixed point, β(X)=∞ (impossible for finite A).

These invariants are computed via Monte Carlo sampling when |A| is large.

---

## 5. Ψ‑Calculus: Executable Dynamics

The Ψ‑calculus defines a state transition system over concept sets.

**Definition 8 (State).**

A state is a subset X⊆A.

**Definition 9 (Operators).**

* **Propagation (core step):**

\[

\mathrm{prop}(X) = X \cup \{\, y \in \mathcal{A} \mid \exists x\in X,\; x\leadsto y \,\}.

\]

* **Collapse (internal mediation):**

Let ϵ(X)={d∈D∣∃x∈X:(x,d)∈E} be the mediators reachable from X. The **attractor** is

\[

\mathrm{Attr}(X) = \mathrm{SCC}(X \cup \epsilon(X)),

\]

where SCC returns the strongly connected component closure in the directed graph G.

(Note: ϵ is used only internally; the output remains a subset of A.)

* **Evolution operator Ξ:**

\[

\Xi(X) = \mathrm{prop}(\mathrm{Attr}(X)).

\]

* **Stabilization Ψ:**

\[

\Psi(X) = \lim_{k\to\infty} \Xi^k(X) = \mathrm{Fix}(\Xi).

\]

Because A is finite, the fixed point is reached in finitely many steps.

**Definition 10 (Dynamic glitch).**

\[

\mathrm{Glitch}_{\mathrm{dyn}}(X) = X \setminus \bigcup_{k\ge 1} \Xi^k(X).

\]

These are nodes that disappear under iteration and never return – a signature of “dead ends” in disambiguation.

---

## 6. Categorical Reconciliation

We now model how two theories can be **reconciled** when they share an observational interface.

### 6.1 Theory Category

Let T be a category whose objects are theories and morphisms are structure‑preserving translations.

Define the **observation functor**

\[

\mathrm{Obs}: \mathcal{T} \to \mathcal{C},

\]

mapping a theory to its observable support in the concept algebra.

### 6.2 Reconciliation as Pushout

Given a span

\[

T_1 \xleftarrow{f_1} I \xrightarrow{f_2} T_2

\]

where I is a shared observational interface (e.g., a common set of measured quantities or axioms), the **reconciled theory** is the pushout

\[

T^* = T_1 \sqcup_I T_2.

\]

The universal property: for any theory S with morphisms g1:T1→S,g2:T2→S such that g1∘f1=g2∘f2, there exists a unique u:T∗→S making the diagram commute.

### 6.3 Dynamical Approximation via Ψ

We cannot compute the pushout directly for arbitrary theories, but we can approximate it on observable supports:

Let

\[

X_1 = \mathrm{Obs}(T_1), \quad X_2 = \mathrm{Obs}(T_2).

\]

Define the **reconciliation state**

\[

X^* = \Psi(X_1 \cup X_2),

\]

the fixed point of the Ψ‑dynamics starting from the union of observable supports.

**Definition 11 (Obstruction class).**

\[

\Omega := X^* \setminus (X_1 \star X_2),

\]

where X1⋆X2 is the closure product (static composition).

Then:

\[

X^* = (X_1 \star X_2) \cup \Omega.

\]

**Interpretation:**

* X1⋆X2 = consistent core – all identifications forced by direct compositional closure.

* Ω = irreducible mismatch – nodes that appear only after recursive propagation, representing emergent contradictions or non‑identifiable concepts.

Contradiction is not a failure; it is a **stable invariant** of the reconciliation process.

---

## 7. Optional Topological Diagnostics

We include a topological layer as a diagnostic tool, not a core requirement.

**Definition 12 (Alexandrov topology).**

On the vertex set V=A∪D, declare a set U⊆V open if it is **upward closed** under directed reachability:

\[

x\in U \;\wedge\; (x\to y) \;\Rightarrow\; y\in U.

\]

This makes the graph a **poset of reachability**.

**Definition 13 (Nerve).**

Take the free category generated by the directed graph; its nerve is a simplicial set. The geometric realization |N(G)| is a finite cell complex.

First homology H1(|N(G)|) is computable (e.g., via the graph’s cycle space). The Hurewicz homomorphism

\[

h: \pi_1(|N(G)|) \to H_1(|N(G)|)

\]

has kernel equal to the commutator subgroup. A non‑trivial kernel indicates non‑abelian cycles in the reachability structure. This can be used to detect persistent logical loops that Ψ‑dynamics might not resolve.

*Important:* This layer is optional and need not be computed for the core reconciliation.

---

## 8. Toy Example

Let

\[

\mathcal{A} = \{a,b,c\}, \quad \mathcal{D} = \{d_1,d_2\},

\]

edges:

* a→d1→b

* b→d2→c

**Mediated reachability:**

a⇝b,b⇝c, and no other.

**Product on singletons:**

\[

\{a\}\cdot\{b\} = \{b\},\quad \{b\}\cdot\{c\} = \{c\},

\]

\[

(\{a\}\cdot\{b\})\cdot\{c\} = \{c\},\quad \{a\}\cdot(\{b\}\cdot\{c\}) = \emptyset.

\]

Hence associativity fails: α>0.

**Ψ‑dynamics starting from X={a,c}:**

* Ξ({a,c})=prop(Attr({a,c})).

Attractor: SCC of {a,c}∪{d1,d2} is all nodes → Attr={a,b,c,d1,d2}.

prop returns {a,b,c}.

* Next step: Ξ({a,b,c})={a,b,c} (fixed point).

Dynamic glitch: Glitchdyn({a,c})=∅ – no node vanishes permanently.

**Obstruction class for reconciliation of T1 with X1={a} and T2 with X2={c}:**

\[

X_1\star X_2 = (\{a\}\star\{c\}) = \emptyset

\]

because no direct two‑step chain from a to c.

Yet X∗=Ψ({a,c})={a,b,c}. Thus

\[

\Omega = \{a,b,c\} \setminus \emptyset = \{a,b,c\}.

\]

All observable nodes are obstructions – the two theories are reconciled only after recursive propagation discovers the mediating chain a→b→c.

---

## 9. Implementation and Complexity

A minimal Python interpreter is given in Appendix A. For large graphs (e.g., Wikipedia subset with |A|≈104):

* Computing Ξ(X) requires O(|X|⋅degmax) time.

* Stabilization typically reaches fixed point in O(diameter) steps.

* Sampling for α,ρ uses small subsets (size ≤3) and Monte Carlo.

* SCC computation is O(|V|+|E|) with Tarjan’s algorithm.

The framework scales to millions of nodes with appropriate sampling and caching.

---

## 10. Discussion

**Relation to existing work.**

The Ψ‑calculus resembles **graph rewriting** and **abstract reduction systems**. The pushout reconciliation echoes **belief revision** (AGM theory), where Ω plays the role of a **remainder** that cannot be consistently added. The non‑associative concept algebra is similar to **relation algebras** but without the associativity axiom, which matches the empirical behavior of disambiguation networks.

**Limitations.**

* The product X⋅Y is defined with a final intersection with Y; this is a design choice that prioritises goal‑directed composition. Alternative definitions are possible.

* For massive graphs, exact computation of Ψ may be memory‑intensive; we rely on sampling.

* The categorical pushout is approximated; we do not claim that Ψ(X1∪X2) equals Obs(T1⊔IT2) in all cases – it is a computable lower bound.

**Falsifiability.**

The framework makes concrete predictions:

* The associativity defect α on real disambiguation graphs is positive and measurable.

* There exist zero divisors (ρ>0).

* The obstruction class Ω is often non‑empty when reconciling theories drawn from different domains.

These can be tested against Wikipedia dumps or other knowledge bases.

---

## 11. Conclusion

We have constructed a unified, executable framework for meaning as a recursive disambiguation process. The key contributions are:

1. A **non‑associative concept algebra** grounded in a bipartite graph.

2. An **executable Ψ‑calculus** that computes stable knowledge states.

3. A **categorical reconciliation layer** that models theory combination via pushouts, with an **obstruction class** that quantifies irreducible contradiction.

4. **Measurable invariants** (α,ρ,β) for empirical validation.

All components are computable, falsifiable, and ready for deployment on real‑world knowledge graphs. Future work includes large‑scale empirical evaluation, extension to dynamic graphs, and integration with neural knowledge graph embeddings.

---

## Appendix A – Minimal Python Interpreter

```python

def propagate(X, graph):

“”“One-step propagation: X ∪ { y | ∃x∈X: x→d→y }.”“”

new = set(X)

for x in X:

for d in graph.out_mediators(x):

for y in graph.out_articles(d):

new.add(y)

return new

def attractor(X, graph):

“”“Strongly connected component closure of X ∪ ε(X).”“”

nodes = set(X)

for x in X:

nodes.update(graph.out_mediators(x))

sccs = graph.strongly_connected_components(nodes)

return set.union(*[comp for comp in sccs if comp & X])

def Xi(X, graph):

“”“One Ψ-evolution step.”“”

return propagate(attractor(X, graph), graph)

def Psi(X, graph):

“”“Stabilization: fixed point of Xi.”“”

prev = None

while X != prev:

prev = X

X = Xi(X, graph)

return X

def reconcile(X1, X2, graph):

X0 = X1 | X2

X_star = Psi(X0, graph)

X_static = closure_product(X1, X2, graph) # implement via repeated product

Omega = X_star - X_static

return X_star, Omega

```

---

## Appendix B – Notation Table

| Symbol | Meaning |

|--------|---------|

| A | Article (concept) nodes |

| D | Disambiguation (mediator) nodes |

| ⇝ | Mediated reachability (x→d→y) |

| ⋅ | Relative product of concept sets |

| ⋆ | Closure product |

| α,ρ,β | Associativity defect, zero‑divisor density, closure depth |

| Ξ | Evolution operator |

| Ψ | Stabilization (fixed point) |

| Glitchdyn | Vanishing nodes under iteration |

| Obs | Observation functor to concept algebra |

| T∗=T1⊔IT2 | Pushout reconciliation |

| Ω | Obstruction class |

---

## References

[1] Maddux, R. D. (2006). *Relation Algebras*. Elsevier.

[2] Barr, M., & Wells, C. (2012). *Category Theory for Computing Science*.

[3] Alexandrov, P. (1937). Diskrete Räume. *Matematicheskii Sbornik*.

[4] Gärdenfors, P. (1988). *Knowledge in Flux*. MIT Press.

[5] Wikipedia dumps. (2026). Wikimedia Foundation.

---

**End of White Paper (Version 3.0)**

---

---

# The Algebra of Disambiguation: A Computable Framework for Recursive Meaning, Reconciliation, and Contradiction

**Version 3.0 – 2026-05-06**

*White Paper*

---

## Abstract

We present a formal, executable, and empirically testable framework for modeling how meaning arises from recursive disambiguation dynamics. The core structure is a bipartite graph of concept nodes and mediating nodes, from which we construct a non‑associative concept algebra. An explicit Ψ‑calculus defines state evolution via collapse, propagation, and stabilization. Categorical reconciliation is achieved via pushouts over shared observational interfaces, with irreducible contradiction captured as an obstruction class. Optional topological diagnostics (Alexandrov topology, nerve, Hurewicz kernel) provide structural invariants without affecting the core system. All components are computable, falsifiable, and deployable on real‑world knowledge graphs.

**Keywords:** non‑associative relation algebras, knowledge graphs, categorical pushouts, Ψ‑calculus, zero divisors, contradiction as obstruction.

---

## 1. Introduction

Meaning is often treated as static – a set of referents, truth conditions, or embeddings. But in practice, meaning is negotiated through processes of disambiguation, inference, and error correction. This white paper develops a formal model in which meaning emerges as the **fixed point of recursive transformations** on a relational structure.

The framework answers three questions:

1. **Algebraic:** Given a bipartite graph of concepts and mediators, what algebraic structure does concept composition inherit?

2. **Dynamical:** How can we define an executable rewrite system that models reasoning as state evolution?

3. **Categorical:** How do we combine two theories sharing an observational interface, and what invariant measures the irreducible disagreement?

We ground the model in a well‑defined substrate: a finite directed graph of **articles (concepts)** and **disambiguation pages (mediators)** extracted from a knowledge base such as Wikipedia. All claims are computable and falsifiable.

---

## 2. Relational Substrate

Let

* A = set of **article nodes** (concepts),

* D = set of **disambiguation nodes** (mediators),

* E⊆(A×D)∪(D×A) = directed edges.

The graph G=(A∪D,E) is bipartite: edges only connect articles to disambiguation pages and vice versa.

**Definition 1 (Mediated reachability).**

For x,y∈A, define x⇝y iff there exists d∈D such that (x,d),(d,y)∈E.

We call this a **two‑step mediated transition**.

This is the fundamental unit of disambiguation: an article x links to a disambiguation page d, which in turn links to article y. The mediator resolves ambiguity.

---

## 3. Concept Algebra

Let C=P(A) be the power set of articles.

**Definition 2 (Relative product).**

For X,Y⊆A, define

\[

X \cdot Y := \{\, y \in Y \mid \exists x \in X,\; x \leadsto y \,\}.

\]

That is, we first compute all articles reachable from X in two steps, then intersect with Y. The product is **non‑commutative** and generally **non‑associative**.

**Definition 3 (Closure product).**

Define iterative application:

\[

X \cdot^{(1)} Y = X \cdot Y,\qquad

X \cdot^{(n+1)} Y = X \cdot (X \cdot^{(n)} Y).

\]

The closure product is

\[

X \star Y = \bigcup_{n \ge 1} X \cdot^{(n)} Y.

\]

**Proposition 1.** The algebra (C,∪,⋅) satisfies:

* Distributivity: (X∪Y)⋅Z=(X⋅Z)∪(Y⋅Z)

* Zero element: ∅⋅X=∅=X⋅∅

* Non‑associativity in general: there exist X,Y,Z with (X⋅Y)⋅Z≠X⋅(Y⋅Z).

Hence C lies in the variety of **non‑associative lattice‑ordered semigroups** (closely related to non‑associative relation algebras, **NA**).

**Definition 4 (Zero divisors).**

A pair (X,Y) with X≠∅,Y≠∅ is a **zero divisor** if X⋅Y=∅.

Left zero divisors: ZL={X∣∃Y≠∅:X⋅Y=∅}.

---

## 4. Measurable Invariants

To make the framework empirical, we define three global metrics.

**Definition 5 (Associativity defect).**

Sample triples (x,y,z) of singleton sets (or small subsets).

\[

\alpha = \Pr\big( (\{x\}\cdot\{y\})\cdot\{z\} \neq \{x\}\cdot(\{y\}\cdot\{z\}) \big).

\]

**Definition 6 (Zero divisor density).**

\[

\rho = \Pr\big( \{x\}\cdot\{y\} = \emptyset \mid x,y\in\mathcal{A} \big).

\]

**Definition 7 (Closure depth).**

For a set X, let

\[

\beta(X) = \min\{ k \mid X^{(k)} = X^{(k+1)} \}

\]

where X(1)=X, X(n+1)=X(n)∪(X(n)⋅X(n)).

If no fixed point, β(X)=∞ (impossible for finite A).

These invariants are computed via Monte Carlo sampling when |A| is large.

---

## 5. Ψ‑Calculus: Executable Dynamics

The Ψ‑calculus defines a state transition system over concept sets.

**Definition 8 (State).**

A state is a subset X⊆A.

**Definition 9 (Operators).**

* **Propagation (core step):**

\[

\mathrm{prop}(X) = X \cup \{\, y \in \mathcal{A} \mid \exists x\in X,\; x\leadsto y \,\}.

\]

* **Collapse (internal mediation):**

Let ϵ(X)={d∈D∣∃x∈X:(x,d)∈E} be the mediators reachable from X. The **attractor** is

\[

\mathrm{Attr}(X) = \mathrm{SCC}(X \cup \epsilon(X)),

\]

where SCC returns the strongly connected component closure in the directed graph G.

(Note: ϵ is used only internally; the output remains a subset of A.)

* **Evolution operator Ξ:**

\[

\Xi(X) = \mathrm{prop}(\mathrm{Attr}(X)).

\]

* **Stabilization Ψ:**

\[

\Psi(X) = \lim_{k\to\infty} \Xi^k(X) = \mathrm{Fix}(\Xi).

\]

Because A is finite, the fixed point is reached in finitely many steps.

**Definition 10 (Dynamic glitch).**

\[

\mathrm{Glitch}_{\mathrm{dyn}}(X) = X \setminus \bigcup_{k\ge 1} \Xi^k(X).

\]

These are nodes that disappear under iteration and never return – a signature of “dead ends” in disambiguation.

---

## 6. Categorical Reconciliation

We now model how two theories can be **reconciled** when they share an observational interface.

### 6.1 Theory Category

Let T be a category whose objects are theories and morphisms are structure‑preserving translations.

Define the **observation functor**

\[

\mathrm{Obs}: \mathcal{T} \to \mathcal{C},

\]

mapping a theory to its observable support in the concept algebra.

### 6.2 Reconciliation as Pushout

Given a span

\[

T_1 \xleftarrow{f_1} I \xrightarrow{f_2} T_2

\]

where I is a shared observational interface (e.g., a common set of measured quantities or axioms), the **reconciled theory** is the pushout

\[

T^* = T_1 \sqcup_I T_2.

\]

The universal property: for any theory S with morphisms g1:T1→S,g2:T2→S such that g1∘f1=g2∘f2, there exists a unique u:T∗→S making the diagram commute.

### 6.3 Dynamical Approximation via Ψ

We cannot compute the pushout directly for arbitrary theories, but we can approximate it on observable supports:

Let

\[

X_1 = \mathrm{Obs}(T_1), \quad X_2 = \mathrm{Obs}(T_2).

\]

Define the **reconciliation state**

\[

X^* = \Psi(X_1 \cup X_2),

\]

the fixed point of the Ψ‑dynamics starting from the union of observable supports.

**Definition 11 (Obstruction class).**

\[

\Omega := X^* \setminus (X_1 \star X_2),

\]

where X1⋆X2 is the closure product (static composition). Then:

\[

X^* = (X_1 \star X_2) \cup \Omega.

\]

**Interpretation:**

* X1⋆X2 = consistent core – all identifications forced by direct compositional closure.

* Ω = irreducible mismatch – nodes that appear only after recursive propagation, representing emergent contradictions or non‑identifiable concepts.

Contradiction is not a failure; it is a **stable invariant** of the reconciliation process.

---

## 7. Optional Topological Diagnostics

We include a topological layer as a diagnostic tool, not a core requirement.

**Definition 12 (Alexandrov topology).**

On the vertex set V=A∪D, declare a set U⊆V open if it is **upward closed** under directed reachability:

\[

x\in U \;\wedge\; (x\to y) \;\Rightarrow\; y\in U.

\]

This makes the graph a **poset of reachability**.

**Definition 13 (Nerve).**

Take the free category generated by the directed graph; its nerve is a simplicial set. The geometric realization |N(G)| is a finite cell complex.

First homology H1(|N(G)|) is computable (e.g., via the graph’s cycle space). The Hurewicz homomorphism

\[

h: \pi_1(|N(G)|) \to H_1(|N(G)|)

\]

has kernel equal to the commutator subgroup. A non‑trivial kernel indicates non‑abelian cycles in the reachability structure. This can be used to detect persistent logical loops that Ψ‑dynamics might not resolve.

*Important:* This layer is optional and need not be computed for the core reconciliation.

---

## 8. Toy Example

Let

\[

\mathcal{A} = \{a,b,c\}, \quad \mathcal{D} = \{d_1,d_2\},

\]

edges:

* a→d1→b

* b→d2→c

**Mediated reachability:**

a⇝b,b⇝c, and no other.

**Product on singletons:**

\[

\{a\}\cdot\{b\} = \{b\},\quad \{b\}\cdot\{c\} = \{c\},

\]

\[

(\{a\}\cdot\{b\})\cdot\{c\} = \{c\},\quad \{a\}\cdot(\{b\}\cdot\{c\}) = \emptyset.

\]

Hence associativity fails: α>0.

**Ψ‑dynamics starting from X={a,c}:**

* Ξ({a,c})=prop(Attr({a,c})).

Attractor: SCC of {a,c}∪{d1,d2} is all nodes → Attr={a,b,c,d1,d2}.

prop returns {a,b,c}.

* Next step: Ξ({a,b,c})={a,b,c} (fixed point).

Dynamic glitch: Glitchdyn({a,c})=∅ – no node vanishes permanently.

**Obstruction class for reconciliation of T1 with X1={a} and T2 with X2={c}:**

\[

X_1\star X_2 = (\{a\}\star\{c\}) = \emptyset

\]

because no direct two‑step chain from a to c.

Yet X∗=Ψ({a,c})={a,b,c}. Thus

\[

\Omega = \{a,b,c\} \setminus \emptyset = \{a,b,c\}.

\]

All observable nodes are obstructions – the two theories are reconciled only after recursive propagation discovers the mediating chain a→b→c.

---

## 9. Implementation and Complexity

A minimal Python interpreter is given in Appendix A. For large graphs (e.g., Wikipedia subset with |A|≈104):

* Computing Ξ(X) requires O(|X|⋅degmax) time.

* Stabilization typically reaches fixed point in O(diameter) steps.

* Sampling for α,ρ uses small subsets (size ≤3) and Monte Carlo.

* SCC computation is O(|V|+|E|) with Tarjan’s algorithm.

The framework scales to millions of nodes with appropriate sampling and caching.

---

## 10. Discussion

**Relation to existing work.**

The Ψ‑calculus resembles **graph rewriting** and **abstract reduction systems**. The pushout reconciliation echoes **belief revision** (AGM theory), where Ω plays the role of a **remainder** that cannot be consistently added. The non‑associative concept algebra is similar to **relation algebras** but without the associativity axiom, which matches the empirical behavior of disambiguation networks.

**Limitations.**

* The product X⋅Y is defined with a final intersection with Y; this is a design choice that prioritises goal‑directed composition. Alternative definitions are possible.

* For massive graphs, exact computation of Ψ may be memory‑intensive; we rely on sampling.

* The categorical pushout is approximated; we do not claim that Ψ(X1∪X2) equals Obs(T1⊔IT2) in all cases – it is a computable lower bound.

**Falsifiability.**

The framework makes concrete predictions:

* The associativity defect α on real disambiguation graphs is positive and measurable.

* There exist zero divisors (ρ>0).

* The obstruction class Ω is often non‑empty when reconciling theories drawn from different domains.

These can be tested against Wikipedia dumps or other knowledge bases.

---

## 11. Conclusion

We have constructed a unified, executable framework for meaning as a recursive disambiguation process. The key contributions are:

1. A **non‑associative concept algebra** grounded in a bipartite graph.

2. An **executable Ψ‑calculus** that computes stable knowledge states.

3. A **categorical reconciliation layer** that models theory combination via pushouts, with an **obstruction class** that quantifies irreducible contradiction.

4. **Measurable invariants** (α,ρ,β) for empirical validation.

All components are computable, falsifiable, and ready for deployment on real‑world knowledge graphs. Future work includes large‑scale empirical evaluation, extension to dynamic graphs, and integration with neural knowledge graph embeddings.

---

## Appendix A – Minimal Python Interpreter

```python

def propagate(X, graph):

“”“One-step propagation: X ∪ { y | ∃x∈X: x→d→y }.”“”

new = set(X)

for x in X:

for d in graph.out_mediators(x):

for y in graph.out_articles(d):

new.add(y)

return new

def attractor(X, graph):

“”“Strongly connected component closure of X ∪ ε(X).”“”

nodes = set(X)

for x in X:

nodes.update(graph.out_mediators(x))

sccs = graph.strongly_connected_components(nodes)

return set.union(*[comp for comp in sccs if comp & X])

def Xi(X, graph):

“”“One Ψ-evolution step.”“”

return propagate(attractor(X, graph), graph)

def Psi(X, graph):

“”“Stabilization: fixed point of Xi.”“”

prev = None

while X != prev:

prev = X

X = Xi(X, graph)

return X

def reconcile(X1, X2, graph):

X0 = X1 | X2

X_star = Psi(X0, graph)

X_static = closure_product(X1, X2, graph) # implement via repeated product

Omega = X_star - X_static

return X_star, Omega

```

---

## Appendix B – Notation Table

| Symbol | Meaning |

|--------|---------|

| A | Article (concept) nodes |

| D | Disambiguation (mediator) nodes |

| ⇝ | Mediated reachability (x→d→y) |

| ⋅ | Relative product of concept sets |

| ⋆ | Closure product |

| α,ρ,β | Associativity defect, zero‑divisor density, closure depth |

| Ξ | Evolution operator |

| Ψ | Stabilization (fixed point) |

| Glitchdyn | Vanishing nodes under iteration |

| Obs | Observation functor to concept algebra |

| T∗=T1⊔IT2 | Pushout reconciliation |

| Ω | Obstruction class |

---

## References

[1] Maddux, R. D. (2006). *Relation Algebras*. Elsevier.

[2] Barr, M., & Wells, C. (2012). *Category Theory for Computing Science*.

[3] Alexandrov, P. (1937). Diskrete Räume. *Matematicheskii Sbornik*.

[4] Gärdenfors, P. (1988). *Knowledge in Flux*. MIT Press.

[5] Wikipedia dumps. (2026). Wikimedia Foundation.

---

**End of White Paper (Version 3.0)**

[](https://substack.com/profile/316485411-enemies_of_art)[](https://substack.com/profile/163347002-hawkeye-speaks)[](https://substack.com/profile/44964516-fport)

3 Likes∙

[1 Restack](https://substack.com/note/p-196585012/restacks?utm_source=substack&utm_content=facepile-restacks)

#### Discussion about this post

[](https://substack.com/profile/44964516-fport?utm_source=comment)

[fport](https://substack.com/profile/44964516-fport?utm_source=substack-feed-item) 

[fport](https://fport724799.substack.com/?utm_source=substack-feed-item&utm_content=comment_metadata)[May 5](https://koryogden.substack.com/p/the-algebra-of-disambiguation/comment/254314684 "May 5, 2026, 4:26 PM")

Hi, this is just me riding along for those not quite understanding exactly how smart this is and what it can do (and that math, bet if you had known back in school how important it can be - from compound interest to holonomic spirals, right)

.

Anyway, in English, this is what is being looked at:

.

Meaning doesn't arrive fully formed. It arrives as a mess of possibilities that gradually get sorted out.

.

Here's the core idea. Imagine a web of connected concepts. Some nodes in the web are the concepts themselves — "justice," "harm," "intention." Other nodes are in between, acting as bridges that explain how concepts relate to each other. When you ask what something means, you're not retrieving a stored answer. You're running a process that collapses the ambiguity down until something stable appears.

The framework names three steps in that process. Collapse is when a range of possible meanings narrows to one that fits the current context. Propagation is when that narrowed meaning ripples outward and affects how nearby concepts get interpreted. Stabilization is when the system settles — not permanently, but long enough to be useful.

.

What makes this framework unusual is that meaning isn't treated as additive. Normally we assume that if A relates to B, and B relates to C, then A relates to C in a predictable way. This framework says that's not always true. The order matters. The path matters. Combining two interpretations doesn't always produce a clean third one. Sometimes the combination produces nothing — a zero divisor, in the mathematical sense. That failure to combine is itself information. It tells you something real about the structure of the problem.

.

When two different knowledge systems try to describe the same thing — say, a medical record and a legal document both describing the same injury — the framework provides a formal way to find what they share. The shared interface is the meeting point. Where they share enough, reconciliation is possible. Where they don't, the framework doesn't force a fake resolution. It captures the contradiction as a structural object, something that can be studied rather than papered over.

The optional diagnostics at the end are tools for examining the shape of a knowledge structure without changing it. They answer questions like: which concepts are load-bearing, which are peripheral, and where are the gaps that no current path can bridge.

Everything described is computable. You can run it on real data. You can test whether it produces correct predictions. You can falsify it.

.

What this means in plain terms: the framework is an attempt to treat the process of meaning-making as something with detectable structure — not just a description of what meaning feels like, but a machine that can be examined, tested, and shown to be wrong when it's wrong.

.

Good so far?

.

When two people try to understand the same thing using different frameworks, something interesting happens. They each bring their own set of connected ideas. Where those idea-sets overlap, agreement is possible. Where they don't connect at all — even after tracing every possible chain of reasoning — you get a gap that can't be closed by adding more information. That gap is real. It has a shape. And measuring its shape tells you something important about both frameworks.

0G1itch's paper builds a machine for mapping those gaps.

.

The accident report interface.

.

An injury generates two documents: a medical record and a legal claim. The medical record speaks the language of tissue damage, mechanism of injury, treatment protocols, prognosis. The legal claim speaks the language of negligence, causation, liability, damages. Both are describing the same event. Neither can be fully translated into the other without losing something.

.

The paper's framework starts from each document's network of connected concepts. It then runs both networks through a process of recursive propagation — following every chain of connection until no new links emerge. When the process stabilizes, you have the full picture of what each framework can reach on its own, and what it reaches only after running through every intermediate step.

.

The gap between what direct connection produces and what recursive propagation eventually finds is the obstruction class. In the accident report case, this gap contains concepts like "subjective experience of pain," "future earning capacity," and "systemic negligence." Neither the medical nor the legal framework reaches these concepts directly from its own starting point. They only become visible after the two frameworks have been run against each other long enough for the mediating chains to emerge.

.

That gap isn't a failure. It's where the real work of reconciliation has to happen.

Two other interfaces where the same pattern appears.

.

In psychiatry meeting criminal law, the gap contains "diminished responsibility," "dangerousness as prediction," and "treatment versus punishment." A psychiatric evaluation and a legal culpability assessment both describe the same person at the same moment. Their combined propagation surface — everything reachable after following every chain — contains concepts neither reaches alone. Insanity defenses and sentencing guidelines are attempts to govern that gap without fully closing it.

.

In machine learning meeting medical diagnosis, the gap contains "clinical judgment," "rare presentation," and "the patient in front of me versus the patient in the training data." A model trained on population statistics and a clinician reasoning about a specific individual are both generating meaning from the same presenting symptoms. Their reconciliation surface contains everything reachable from both starting points after recursive propagation. The obstruction class — what shows up only after full propagation — is where explainability debates actually live.

.

The conclusion.

.

The paper's contribution is making this structure computable and falsifiable. You can run the process on real knowledge networks, measure how often direct composition fails to predict what recursive propagation eventually produces, and test whether the gap between them is systematic or random. If it's systematic — and the paper predicts it will be — then the obstruction class is a genuine structural feature of how different frameworks encounter each other, not just a temporary confusion waiting to be resolved.

.

Contradiction, properly measured, is not a sign that something went wrong. It's a stable signal about where two ways of seeing the world genuinely diverge, and what it would cost to bridge them.

Liked (1)

Reply

Share

© 2026 Kory Ogden · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://your.substack.com/publish)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture