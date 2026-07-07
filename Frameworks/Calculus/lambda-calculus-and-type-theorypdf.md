---
created: 2026-05-11
psi_tier: zero_divisor
sources:
- Lambda-Calculus and Type Theory.pdf.md
tags:
- zero_divisor
- ingested
title: Lambda Calculus And Type Theory.Pdf
type: concept
updated: 2026-05-11
---

# Lambda Calculus And Type Theory.Pdf

# Lambda-Calculus and Type Theory.pdf

Lambda-Calculus and Type Theory
ISR 2024 Obergurgl, Austria
Herman Geuvers & Niels van der Weide
Radboud University Nijmegen, The Netherlands
Lecture 7
Higher order logic in the Calculus of constructions and in Coq
The Barendregt cube
Barendregt cube: 8 typed λ-calculi, defined in one coherent way. Generalization: Berardi & Terlouw: Pure Type Systems
framework for defining and studying typed λ-calculi PTS = pure type system
the PTS rules are basically the λP rules as presented before.
variations on the product rule
Γ ⊢ A : s1 Γ, x : A ⊢ B : s2
Γ ⊢ Πx : A.B : s2
λP s1 = ∗ , s2 ∈ {∗,□}
(s1, s2) ∈ {(∗, ∗), (∗,□)} λ→ (s1, s2) ∈ {(∗, ∗)} λ2 (s1, s2) ∈ {(∗, ∗), (□, ∗)} λC (s1, s2) ∈ {(∗, ∗), (∗,□), (□, ∗), (□,□)}
(axiom) ⊢ ∗ : □
(var) Γ ⊢ A : s
Γ, x :A ⊢ x : A (weak)
Γ ⊢ A : s Γ ⊢ M : C
Γ, x :A ⊢ M : C
(Π) Γ ⊢ A : s1 Γ, x :A ⊢ B : s2
Γ ⊢ Πx :A.B : s2
if (s1, s2) ∈ R
(λ) Γ, x :A ⊢ M : B Γ ⊢ Πx :A.B : s
Γ ⊢ λx :A.M : Πx :A.B
(app) Γ ⊢ M : Πx :A.B Γ ⊢ N : A
Γ ⊢ MN : B[N/x ]
(conv) Γ ⊢ M : A Γ ⊢ B : s
Γ ⊢ M : B if A =β B
(Π) Γ ⊢ A : s1 Γ, x :A ⊢ B : s2
Γ ⊢ Πx :A.B : s2 if (s1, s2) ∈ R
System R λ→ (∗, ∗) λ2 (system F) (∗, ∗) (□, ∗) λP (LF) (∗, ∗) (∗,□) λω (∗, ∗) (□,□) λP2 (∗, ∗) (□, ∗) (∗,□) λω (system Fω) (∗, ∗) (□, ∗) (□,□) λPω (∗, ∗) (∗,□) (□,□) λPω (CC) (∗, ∗) (□, ∗) (∗,□) (□,□)
the Barendregt cube
λω // OO λCOO
λ2
??
// OO
(□, ∗)
λP2
??
OO
λω // λPω
λ→ (∗,□) //
(□,□)
??
λP
??
Calculus of Constructions
λ→ in this presentation is equivalent to λ→ as presented before. Similarly for λ2, λP, . . . This cube also gives a fine structure for the
Calculus of Constructions, CC (Coquand and Huet) ▶ Polymorphic data types on the ∗-level,
e.g. Πα: ∗ .α→(α→α)→α : ∗ .
▶ Predicate domains on the □-level, e.g. N→N→∗ : □
▶ Logic on the ∗-level, e.g. φ ∧ ψ := Πα: ∗ .(φ→ψ→α)→α : ∗.
▶ Universal quantification (first and higher order), e.g. ΠP:N→∗ .Πx :N.Px→Px : ∗.
Examples
▶ Induction
∀P:N→∗ ( (P 0) → (∀x :N.(P x → P(S x))) → ∀x :N.P x )
▶ Defining the smallest subset of A containing P : A → ∗ and closed under f : A → A.
S := λy : A. ∀Q : A→∗ .(P ⊆ Q) → (∀x : A.Q x → Q (f x)) → Q y
where P ⊆ Q := ∀x : A.P x → Q x . To prove:

S is closed under f , 2. S contains P, 3. S is the smallest such.
Examples ctd.
▶ Higher order predicates/functions: transitive closure of a relation R
λR : A→A→∗ . λx , y : A. (∀Q : A→A→∗ . (trans(Q) → (R ⊆ Q) → Q x y))
of type (A→A→∗)→(A→A→∗)
Example trans clos higher order and inductively
▶ transitive closure in higher order logic:
λR : A→A→∗ . λx , y : A. (∀Q : A→A→∗ . (trans(Q) → (R ⊆ Q) → Q x y))
of type (A→A→∗)→(A→A→∗)
▶ transitive closure inductively:
Inductive TrclosInd (R : A->A->Prop) : A -> A -> Prop :=
| sub : forall x y : A, R x y -> TrclosInd x y
| trans : forall x y z : A,
TrclosInd x y -> TrclosInd y z -> TrclosInd x z.
Exercise trans clos higher order
Given the transitive closure of a binary relation, defined in higher order logic:
trclosR := λx , y :A.
(∀Q:A→A→∗ .(trans(Q)→(R ⊆ Q)→(Q x y))).

Prove that the transitive closure is transitive.

Prove that the transitive closure of R contains R.
Higher order logic HOL
In higher order logic (originally due to Church[1940]) we have:
▶ higher order domains: D, D→Prop, (D→Prop)→Prop, etc (sets of predicates over predicates over . . . ).
▶ higher order function domains: (D→D)→D, ((D→D)→D)→D, etc.
▶ ∀-quantification over all domains
We can do Higher Order Logic in Coq In Coq we often have the choice to define sets/predicates/relations inductively or via higher order logic. The Standard Library uses inductive representations.
Definability of other connectives (constructively)
⊥ := ∀α: ∗ .α φ∧ψ := ∀α: ∗ .(φ→ ψ → α) → α
φ∨ψ := ∀α: ∗ .(φ→ α) → (ψ → α) → α
∃x :σ.φ := ∀α: ∗ .(∀x :σ.φ→ α) → α
Idea: The definition of a connective is an encoding of the elimination rule.
Existential quantifier
∃x :σ.φ := ∀α: ∗ .(∀x :σ.φ→ α) → α
Derivation of the elimination rule in HOL.
∃x :σ.φ
[φ] ... C
x /∈ FV(C , ass.) C
∃x :σ.φ
(∀x :σ.φ→ C ) → C
[φ] ... C
∀x :σ.φ→ C
C
Equality
Equality is definable in higher order logic: t and q terms are equal if they share the same properties (Leibniz equality)
Definition in HOL (for t, q : A):
t=Aq := ∀P:A→∗.(Pt → Pq)
▶ This equality is reflexive and transitive (easy)
▶ It is also symmetric(!) Trick: find a “smart” predicate P
Exercise: Prove reflexivity, transitivity and symmetry of =A.
CC versus HOL
Question: is the type theory CC really isomorphic with HOL? No: only if we disambiguate ∗ into Set and Prop (or ∗s and ∗p). This is the type theory of Coq.
Properties of CC
▶ Uniqueness of types If Γ ⊢ M : A and Γ ⊢ M : B, then A=βB.
▶ Subject Reduction If Γ ⊢ M : A and M →β N, then Γ ⊢ N : A.
▶ Strong Normalization If Γ ⊢ M : A, then all β-reductions from M terminate.
Proof of SN is a really difficult.
Decidability Questions
Γ ⊢ M : σ? TCP Γ ⊢ M : ? TSP Γ ⊢? : σ TIP
For CC:
▶ TIP is undecidable
▶ TCP/TSP: simultaneously. The type checking algorithm is close to the one for λP. (In λP we had a judgement of correct context; this form of judgement could also be introduced for CC)


## Related
- [[Reflexive Operator Calculus]]
- [[The Calculus of Recursive Collapse and Stabili]]


- [[Lambda Coherence Engine]]
- [[Type System]]



---

*Source: `Lambda-Calculus and Type Theory.pdf.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
