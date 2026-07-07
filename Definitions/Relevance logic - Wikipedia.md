---
title: Relevance logic - Wikipedia
source: https://en.wikipedia.org/wiki/Relevance_logic
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2003-02-18
created: 2026-04-09
description:
tags:
  - clippings
aliases:
---
**Relevance logic**, also called **relevant logic**, is a kind of [non-classical logic](https://en.wikipedia.org/wiki/Non-classical_logic "Non-classical logic") requiring the [antecedent](https://en.wikipedia.org/wiki/Antecedent_\(logic\) "Antecedent (logic)") and [consequent](https://en.wikipedia.org/wiki/Consequent "Consequent") of [implications](https://en.wikipedia.org/wiki/Entailment "Entailment") to be relevantly related. They may be viewed as a family of [substructural](https://en.wikipedia.org/wiki/Substructural_logic "Substructural logic") or [modal](https://en.wikipedia.org/wiki/Modal_logic "Modal logic") logics. It is generally, but not universally, called *relevant logic* by British and, especially, Australian [logicians](https://en.wikipedia.org/wiki/Logician "Logician"), and *relevance logic* by American logicians.

In terms of a syntactical constraint for a [propositional calculus](https://en.wikipedia.org/wiki/Propositional_calculus "Propositional calculus"), it is necessary, but not sufficient, that premises and conclusion share [atomic formulae](https://en.wikipedia.org/wiki/Atomic_formula "Atomic formula") (formulae that do not contain any [logical connectives](https://en.wikipedia.org/wiki/Logical_connective "Logical connective")). In a [predicate calculus](https://en.wikipedia.org/wiki/Predicate_calculus "Predicate calculus"), relevance requires sharing of variables and constants between premises and conclusion. This can be ensured (along with stronger conditions) by, e.g., placing certain restrictions on the rules of a natural deduction system. In particular, a Fitch-style [natural deduction](https://en.wikipedia.org/wiki/Natural_deduction "Natural deduction") can be adapted to accommodate relevance by introducing tags at the end of each line of an application of an inference indicating the premises relevant to the conclusion of the inference. [Gentzen](https://en.wikipedia.org/wiki/Gentzen "Gentzen") -style [sequent calculi](https://en.wikipedia.org/wiki/Sequent_calculus "Sequent calculus") can be modified by removing the weakening rules that allow for the introduction of arbitrary formulae on the right or left side of the [sequents](https://en.wikipedia.org/wiki/Sequent "Sequent").

A notable feature of relevance logics is that they are [paraconsistent logics](https://en.wikipedia.org/wiki/Paraconsistent_logic "Paraconsistent logic"): the existence of a contradiction will not necessarily cause an " [explosion](https://en.wikipedia.org/wiki/Principle_of_explosion "Principle of explosion")." This follows from the fact that a conditional with a contradictory antecedent that does not share any propositional or predicate letters with the consequent cannot be true (or derivable).

## Motivation

Classical accounts of implication validate a range of "paradoxes"—for example, that any truth follows from a contradiction, or that any statement implies a tautology—because material and strict conditionals ignore whether antecedent and consequent are about the same topic.[^1] [^2] Relevance logic addresses this by requiring a suitable connection between premises and conclusion. A familiar syntactic proxy is *variable sharing* (or "topic sharing"): no valid inference (and no true conditional ${\displaystyle A\to B}$) unless antecedent and consequent share atoms; natural–deduction and sequent systems enforce this by tracking the *actual use* of premises and by restricting structural rules such as weakening.[^3] [^2] Variable sharing is *necessary but not sufficient* for relevance, so contemporary formulations combine proof-theoretic constraints with model-theoretic conditions.[^1]

A notable consequence is *paraconsistency*: contradictions do not trigger the principle of explosion. In relevance logics, a conditional with a contradictory antecedent that does not share propositional (or predicate) letters with its consequent is not automatically valid, blocking triviality while preserving meaningful inferential links.[^2] [^1]

### Criticism

[David Lewis](https://en.wikipedia.org/wiki/David_Lewis_\(philosopher\) "David Lewis (philosopher)"), a defender of [classical logic](https://en.wikipedia.org/wiki/Classical_logic "Classical logic"), has criticized the idea of relevance that motivates relevance logic (at least to [Anderson](https://en.wikipedia.org/wiki/Alan_Ross_Anderson "Alan Ross Anderson") and [Belnap](https://en.wikipedia.org/wiki/Nuel_Belnap "Nuel Belnap"), whose work is the most influential on the subject) by creating a formal analysis of " [aboutness](https://en.wikipedia.org/wiki/Aboutness "Aboutness") " via a formal construct of "subject matters" and showing that, if a premise classically [truth-preserves](https://en.wikipedia.org/wiki/Logical_consequence "Logical consequence") a conclusion, then it's automatically relevant to it, so that, on Lewis's view, there are no classically truth-preserving [fallacies of relevance](https://en.wikipedia.org/wiki/Irrelevant_conclusion "Irrelevant conclusion").[^4]

## History

Early complaints about classical implication predate relevance logic. Hugh MacColl questioned the identification of "if" with truth-functional implication;[^5] [C. I. Lewis](https://en.wikipedia.org/wiki/C._I._Lewis "C. I. Lewis") was led to invent modal logic, and specifically [strict implication](https://en.wikipedia.org/wiki/Strict_implication "Strict implication"), on the grounds that classical logic grants [paradoxes of material implication](https://en.wikipedia.org/wiki/Paradoxes_of_material_implication "Paradoxes of material implication") such as the principle that [a falsehood implies any proposition](https://en.wikipedia.org/wiki/Vacuous_truth "Vacuous truth").[^6] [^7] (For instance, "if this article is an [Uncyclopedia](https://en.wikipedia.org/wiki/Uncyclopedia "Uncyclopedia") article, then two and two is five" is true when translated as a material implication, since this article is a [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia "Wikipedia") article. But it seems intuitively false if one assumes that a true implication must tie the antecedent and consequent together by some notion of relevance; and whether or not this article is from Uncyclopedia seems in no way relevant to whether two and two is five.) Lewis's strict implication still licensed some irrelevant inferences, however, known as the [paradoxes of strict implication](https://en.wikipedia.org/wiki/Paradoxes_of_material_implication "Paradoxes of material implication").

Relevance logic was proposed in 1928 by Soviet philosopher [Ivan E. Orlov](https://en.wikipedia.org/wiki/Ivan_E._Orlov "Ivan E. Orlov") (1886 – circa 1936) in his strictly mathematical paper "The Logic of Compatibility of Propositions" published in *Matematicheskii Sbornik*. The basic idea of relevant implication appears in medieval logic, and some pioneering work was done by [Ackermann](https://en.wikipedia.org/wiki/Wilhelm_Ackermann "Wilhelm Ackermann"),[^8] [Moh](https://en.wikipedia.org/w/index.php?title=Moh_Shaw-Kwei&action=edit&redlink=1 "Moh Shaw-Kwei (page does not exist)"),[^9] and [Church](https://en.wikipedia.org/wiki/Alonzo_Church "Alonzo Church") [^10] in the 1950s. Drawing on them, [Nuel Belnap](https://en.wikipedia.org/wiki/Nuel_Belnap "Nuel Belnap") and [Alan Ross Anderson](https://en.wikipedia.org/wiki/Alan_Ross_Anderson "Alan Ross Anderson") (with others) wrote the *magnum opus* of the subject, *Entailment: The Logic of Relevance and Necessity* in the 1970s (the second volume being published in the nineties). They focused on both systems of [entailment](https://en.wikipedia.org/wiki/Entailment "Entailment") and systems of relevance, where implications of the former kinds are supposed to be both relevant and necessary.

> Once upon a time, [modal logics](https://en.wikipedia.org/wiki/Modal_logic "Modal logic") "had no semantics". Bearing a real world G, a set of worlds K, and a relation R of relative possibility between worlds, [Saul Kripke](https://en.wikipedia.org/wiki/Saul_Kripke "Saul Kripke") beheld this situation and saw that it was formally explicable, and made [model structures](https://en.wikipedia.org/wiki/Kripke_semantics "Kripke semantics"). It came to pass that soon everyone was making model structures, and some were [deontic](https://en.wikipedia.org/wiki/Deontic_logic "Deontic logic"), and some were [temporal](https://en.wikipedia.org/wiki/Temporal_logic "Temporal logic"), and some were [epistemic](https://en.wikipedia.org/wiki/Epistemic_logic "Epistemic logic"), according to the conditions on the [binary relation](https://en.wikipedia.org/wiki/Binary_relation "Binary relation") R.
> 
> None of the model structures that Kripke made, nor that [Hintikka](https://en.wikipedia.org/wiki/Jaakko_Hintikka "Jaakko Hintikka") made, nor that [Thomason](https://en.wikipedia.org/wiki/Richmond_Thomason "Richmond Thomason") made, nor that their co-workers and colleagues made, were, however, relevant. This caused great sadness in the city of [Pittsburgh](https://en.wikipedia.org/wiki/Pittsburgh "Pittsburgh"), where dwelt the captains of [American](https://en.wikipedia.org/wiki/United_States "United States") Industry. The logic industry was there represented by [Anderson](https://en.wikipedia.org/wiki/Alan_Ross_Anderson "Alan Ross Anderson"), [Belnap](https://en.wikipedia.org/wiki/Nuel_Belnap "Nuel Belnap") & Sons, discoverers of entailment and scourge of [material impliers](https://en.wikipedia.org/wiki/Material_implication_\(rule_of_inference\) "Material implication (rule of inference)"), [strict impliers](https://en.wikipedia.org/wiki/Strict_conditional "Strict conditional"), and of [all that to which their falsehoods and contradictions led](https://en.wikipedia.org/wiki/Paradoxes_of_material_implication "Paradoxes of material implication"). Yea, every year or so Anderson & Belnap turned out a new logic, and they did call it E, or R, or E₁, or P–W, and they beheld each such logic, and they were called relevant. And these logics were looked upon with favor by many, for they captureth the intuitions, but by many more they were scorned, in that they hadeth no [semantics](https://en.wikipedia.org/wiki/Semantics_\(logic\) "Semantics (logic)").
> 
> Word that Anderson & Belnap had made a logic without semantics leaked out. Some thought it wondrous and rejoiced, that the One True Logic should make its appearance among us in the Form of Pure Syntax, unencumbered by all that [set-theoretical](https://en.wikipedia.org/wiki/Set_theory "Set theory") garbage. Others said that relevant logics were Mere Syntax. Surveying the situation [Routley](https://en.wikipedia.org/wiki/Richard_Sylvan "Richard Sylvan"), and quite independently [Urquhart](https://en.wikipedia.org/wiki/Alasdair_Urquhart "Alasdair Urquhart"), found an explication of the key concept of relevant implication. Building on Routley \[1972\], and with a little help from our friends – [Dunn](https://en.wikipedia.org/wiki/Jon_Michael_Dunn "Jon Michael Dunn") and Urquhart in particular, with thanks also due to Anderson, Belnap, V. Routley, and Woodruff – we use these insights to present here a formal semantics for the system R of relevant implication, and to provide it with proofs of consistency and completeness relative to that semantics.

[Richard Sylvan](https://en.wikipedia.org/wiki/Richard_Sylvan "Richard Sylvan") (then Routley) and Robert K. Meyer, *The Semantics of Entailment* [^11]

A breakthrough in model theory came in the 1970s with *Routley–Meyer* ternary-relational semantics, together with the Routley (star) treatment of negation, providing sound/complete frames for many relevance systems and explaining how relevance blocks classical paradoxes.[^12] [^1] In parallel, Alasdair Urquhart developed *operational/semilattice* models for positive fragments,[^13] and Kit Fine provided alternative model constructions and algebraic perspectives that further clarified the space of relevant conditionals.[^14]

From the late 1970s onward, a family of systems crystallized—ranging from weaker logics such as *B* (often taken as a minimal relevance base) up through *R*, *E*, and their extensions—together with algebraic semantics (e.g., De Morgan monoids) and proof systems (display calculi, natural deduction).[^15] [^2] Subsequent work connected relevance logic with paraconsistency and substructural logics more broadly, refined contraction-free systems to avoid Curry-style triviality, and explored applications in deontic, modal, and computational settings.[^1] [^2]

## Axioms

The early developments in relevance logic focused on the stronger systems. The development of the Routley–Meyer semantics brought out a range of weaker logics. The weakest of these logics is the relevance logic B. It is axiomatized with the following axioms and rules.

1. ${\displaystyle A\to A}$
2. ${\displaystyle A\land B\to A}$
3. ${\displaystyle A\land B\to B}$
4. ${\displaystyle (A\to B)\land (A\to C)\to (A\to B\land C)}$
5. ${\displaystyle A\to A\lor B}$
6. ${\displaystyle B\to A\lor B}$
7. ${\displaystyle (A\to C)\land (B\to C)\to (A\lor B\to C)}$
8. ${\displaystyle A\land (B\lor C)\to (A\land B)\lor (A\land C)}$
9. ${\displaystyle \lnot \lnot A\to A}$

The rules are the following.

1. ${\displaystyle A,A\to B\vdash B}$
2. ${\displaystyle A,B\vdash A\land B}$
3. ${\displaystyle A\to B\vdash (C\to A)\to (C\to B)}$
4. ${\displaystyle A\to B\vdash (B\to C)\to (A\to C)}$
5. ${\displaystyle A\to \lnot B\vdash B\to \lnot A}$

Stronger logics can be obtained by adding any of the following axioms.

1. ${\displaystyle (A\to B)\to (\lnot B\to \lnot A)}$
2. ${\displaystyle (A\to B)\land (B\to C)\to (A\to C)}$
3. ${\displaystyle (A\to B)\to ((B\to C)\to (A\to C))}$
4. ${\displaystyle (A\to B)\to ((C\to A)\to (C\to B))}$
5. ${\displaystyle (A\to (A\to B))\to (A\to B)}$
6. ${\displaystyle (A\land (A\to B))\to B}$
7. ${\displaystyle (A\to \lnot A)\to \lnot A}$
8. ${\displaystyle (A\to (B\to C))\to (B\to (A\to C))}$
9. ${\displaystyle A\to ((A\to B)\to B)}$
10. ${\displaystyle ((A\to A)\to B)\to B}$
11. ${\displaystyle A\lor \lnot A}$
12. ${\displaystyle A\to (A\to A)}$

There are some notable logics stronger than B that can be obtained by adding axioms to B as follows.

- For DW, add axiom 1.
- For DJ, add axioms 1, 2.
- For TW, add axioms 1, 2, 3, 4.
- For RW, add axioms 1, 2, 3, 4, 8, 9.
- For T, add axioms 1, 2, 3, 4, 5, 6, 7, 11.
- For R, add axioms 1-11.
- For E, add axioms 1-7, 10, 11, ${\displaystyle ((A\to A)\land (B\to B)\to C)\to C}$, and ${\displaystyle \Box A\land \Box B\to \Box (A\land B)}$, where ${\displaystyle \Box A}$ is defined as ${\displaystyle (A\to A)\to A}$.
- For RM, add all the additional axioms.

## Models

### Routley–Meyer models

The standard model theory for relevance logics is the Routley-Meyer ternary-relational semantics developed by [Richard Routley](https://en.wikipedia.org/wiki/Richard_Sylvan "Richard Sylvan") and [Robert Meyer](https://en.wikipedia.org/wiki/Bob_Meyer_\(logician\) "Bob Meyer (logician)"). A Routley–Meyer frame F for a propositional language is a quadruple (W,R,\*,0), where W is a non-empty set, R is a ternary relation on W, and \* is a function from W to W, and ${\displaystyle 0\in W}$. A Routley-Meyer model M is a Routley-Meyer frame F together with a valuation, ${\displaystyle \Vdash }$, that assigns a truth value to each atomic proposition relative to each point ${\displaystyle a\in W}$. There are some conditions placed on Routley-Meyer frames. Define ${\displaystyle a\leq b}$ as ${\displaystyle R0ab}$.

- ${\displaystyle a\leq a}$.
- If ${\displaystyle a\leq b}$ and ${\displaystyle b\leq c}$, then ${\displaystyle a\leq c}$.
- If ${\displaystyle d\leq a}$ and ${\displaystyle Rabc}$, then ${\displaystyle Rdbc}$.
- ${\displaystyle a^{**}=a}$.
- If ${\displaystyle a\leq b}$, then ${\displaystyle b^{*}\leq a^{*}}$.

Write ${\displaystyle M,a\Vdash A}$ and ${\displaystyle M,a\nVdash A}$ to indicate that the formula ${\displaystyle A}$ is true, or not true, respectively, at point ${\displaystyle a}$ in ${\displaystyle M}$. One final condition on Routley-Meyer models is the hereditariness condition.

- If ${\displaystyle M,a\Vdash p}$ and ${\displaystyle a\leq b}$, then ${\displaystyle M,b\Vdash p}$, for all atomic propositions ${\displaystyle p}$.

By an inductive argument, hereditariness can be shown to extend to complex formulas, using the truth conditions below.

- If ${\displaystyle M,a\Vdash A}$ and ${\displaystyle a\leq b}$, then ${\displaystyle M,b\Vdash A}$, for all formulas ${\displaystyle A}$.

The truth conditions for complex formulas are as follows.

- ${\displaystyle M,a\Vdash A\land B\iff M,a\Vdash A}$ and ${\displaystyle M,a\Vdash B}$
- ${\displaystyle M,a\Vdash A\lor B\iff M,a\Vdash A}$ or ${\displaystyle M,a\Vdash B}$
- ${\displaystyle M,a\Vdash A\to B\iff \forall b,c((Rabc\land M,b\Vdash A)\Rightarrow M,c\Vdash B)}$
- ${\displaystyle M,a\Vdash \lnot A\iff M,a^{*}\nVdash A}$

A formula ${\displaystyle A}$ holds in a model ${\displaystyle M}$ just in case ${\displaystyle M,0\Vdash A}$. A formula ${\displaystyle A}$ holds on a frame ${\displaystyle F}$ iff A holds in every model ${\displaystyle (F,\Vdash )}$. A formula ${\displaystyle A}$ is valid in a class of frames iff A holds on every frame in that class. The class of all Routley–Meyer frames satisfying the above conditions validates that relevance logic B. One can obtain Routley-Meyer frames for other relevance logics by placing appropriate restrictions on R and on \*. These conditions are easier to state using some standard definitions. Let ${\displaystyle Rabcd}$ be defined as ${\displaystyle \exists x(Rabx\land Rxcd)}$, and let ${\displaystyle Ra(bc)d}$ be defined as ${\displaystyle \exists x(Rbcx\land Raxd)}$. Some of the frame conditions and the axioms they validate are the following.

| Name | Frame condition | Axiom |
| --- | --- | --- |
| Pseudo-modus ponens | ${\displaystyle Raaa}$ | ${\displaystyle (A\land (A\to B))\to B}$ |
| Prefixing | ${\displaystyle Rabcd\Rightarrow Ra(bc)d}$ | ${\displaystyle (A\to B)\to ((C\to A)\to (C\to B))}$ |
| Suffixing | ${\displaystyle Rabcd\Rightarrow Rb(ac)d}$ | ${\displaystyle (A\to B)\to ((B\to C)\to (A\to C))}$ |
| Contraction | ${\displaystyle Rabc\Rightarrow Rabbc}$ | ${\displaystyle (A\to (A\to B))\to (A\to B)}$ |
| Hypothetical syllogism | ${\displaystyle Rabc\Rightarrow Ra(ab)c}$ | ${\displaystyle (A\to B)\land (B\to C)\to (A\to C)}$ |
| Assertion | ${\displaystyle Rabc\Rightarrow Rbac}$ | ${\displaystyle A\to ((A\to B)\to B)}$ |
| E axiom | ${\displaystyle Ra0a}$ | ${\displaystyle ((A\to A)\to B)\to B}$ |
| Mingle axiom | ${\displaystyle Rabc\Rightarrow a\leq c}$ or ${\displaystyle b\leq c}$ | ${\displaystyle A\to (A\to A)}$ |
| Reductio | ${\displaystyle Raa^{*}a}$ | ${\displaystyle (A\to \lnot A)\to \lnot A}$ |
| Contraposition | ${\displaystyle Rabc\Rightarrow Rac^{*}b^{*}}$ | ${\displaystyle (A\to B)\to (\lnot B\to \lnot A)}$ |
| Excluded middle | ${\displaystyle 0^{*}\leq 0}$ | ${\displaystyle A\lor \lnot A}$ |
| Strict implication weakening | ${\displaystyle 0\leq a}$ | ${\displaystyle A\to (B\to B)}$ |
| Weakening | ${\displaystyle Rabc\Rightarrow b\leq c}$ | ${\displaystyle A\to (B\to A)}$ |

The last two conditions validate forms of weakening that relevance logics were originally developed to avoid. They are included to show the flexibility of the Routley–Meyer models.

### Operational models

#### Urquhart models

Operational models for negation-free fragments of relevance logics were developed by [Alasdair Urquhart](https://en.wikipedia.org/wiki/Alasdair_Urquhart "Alasdair Urquhart") in his PhD thesis and in subsequent work. The intuitive idea behind the operational models is that points in a model are pieces of information, and combining information supporting a conditional with the information supporting its antecedent yields some information that supports the consequent. Since the operational models do not generally interpret negation, this section will consider only languages with a conditional, conjunction, and disjunction.

An operational frame ${\displaystyle F}$ is a triple ${\displaystyle (K,\cdot ,0)}$, where ${\displaystyle K}$ is a non-empty set, ${\displaystyle 0\in K}$, and ${\displaystyle \cdot }$ is a binary operation on ${\displaystyle K}$. Frames have conditions, some of which may be dropped to model different logics. The conditions Urquhart proposed to model the conditional of the relevance logic R are the following.

- ${\displaystyle x\cdot x=x}$
- ${\displaystyle (x\cdot y)\cdot z=x\cdot (y\cdot z)}$
- ${\displaystyle x\cdot y=y\cdot x}$
- ${\displaystyle 0\cdot x=x}$

Under these conditions, the operational frame is a [join-semilattice](https://en.wikipedia.org/wiki/Join-semilattice "Join-semilattice").

An operational model ${\displaystyle M}$ is a frame ${\displaystyle F}$ with a valuation ${\displaystyle V}$ that maps pairs of points and atomic propositions to truth values, T or F. ${\displaystyle V}$ can be extended to a valuation ${\displaystyle \Vdash }$ on complex formulas as follows.

- ${\displaystyle M,a\Vdash p\iff V(a,p)=T}$, for atomic propositions
- ${\displaystyle M,a\Vdash A\land B\iff M,a\Vdash A}$ and ${\displaystyle M,a\Vdash B}$
- ${\displaystyle M,a\Vdash A\lor B\iff M,a\Vdash A}$ or ${\displaystyle M,a\Vdash B}$
- ${\displaystyle M,a\Vdash A\to B\iff \forall b(M,b\Vdash A\Rightarrow M,a\cdot b\Vdash B)}$

A formula ${\displaystyle A}$ holds in a model ${\displaystyle M}$ iff ${\displaystyle M,0\Vdash A}$. A formula ${\displaystyle A}$ is valid in a class of models ${\displaystyle C}$ iff it holds in each model ${\displaystyle M\in C}$.

The conditional fragment of R is sound and complete with respect to the class of semilattice models. The logic with conjunction and disjunction is properly stronger than the conditional, conjunction, disjunction fragment of R. In particular, the formula ${\displaystyle (A\to (B\lor C))\land (B\to C)\to (A\to C)}$ is valid for the operational models but it is invalid in R. The logic generated by the operational models for R has a complete axiomatic proof system, due [Kit Fine](https://en.wikipedia.org/wiki/Kit_Fine "Kit Fine") and to Gerald Charlwood. Charlwood also provided a natural deduction system for the logic, which he proved equivalent to the axiomatic system. Charlwood showed that his natural deduction system is equivalent to a system provided by [Dag Prawitz](https://en.wikipedia.org/wiki/Dag_Prawitz "Dag Prawitz").

The operational semantics can be adapted to model the conditional of E by adding a non-empty set of worlds ${\displaystyle W}$ and an accessibility relation ${\displaystyle \leq }$ on ${\displaystyle W\times W}$ to the frames. The accessibility relation is required to be reflexive and transitive, to capture the idea that E's conditional has an S4 necessity. The valuations then map triples of atomic propositions, points, and worlds to truth values. The truth condition for the conditional is changed to the following.

- ${\displaystyle M,a,w\Vdash A\to B\iff \forall b,\forall w'\geq w(M,b,w'\Vdash A\Rightarrow M,a\cdot b,w'\Vdash B)}$

The operational semantics can be adapted to model the conditional of T by adding a relation ${\displaystyle \leq }$ on ${\displaystyle K\times K}$. The relation is required to obey the following conditions.

- ${\displaystyle 0\leq x}$
- If ${\displaystyle x\leq y}$ and ${\displaystyle y\leq z}$, then ${\displaystyle x\leq z}$
- If ${\displaystyle x\leq y}$, then ${\displaystyle x\cdot z\leq y\cdot z}$

The truth condition for the conditional is changed to the following.

- ${\displaystyle M,a\Vdash A\to B\iff \forall b((a\leq b\land M,b\Vdash A)\Rightarrow M,a\cdot b\Vdash B)}$

There are two ways to model the contraction-less relevance logics TW and RW with the operational models. The first way is to drop the condition that ${\displaystyle x\cdot x=x}$. The second way is to keep the semilattice conditions on frames and add a binary relation, ${\displaystyle J}$, of disjointness to the frame. For these models, the truth conditions for the conditional is changed to the following, with the addition of the ordering in the case of TW.

- ${\displaystyle M,a\Vdash A\to B\iff \forall b((Jab\land M,b\Vdash A)\Rightarrow M,a\cdot b\Vdash B)}$

#### Humberstone models

Urquhart showed that the semilattice logic for R is properly stronger than the positive fragment of R. Lloyd Humberstone provided an enrichment of the operational models that permitted a different truth condition for disjunction. The resulting class of models generates exactly the positive fragment of R.

An operational frame ${\displaystyle F}$ is a quadruple ${\displaystyle (K,\cdot ,+,0)}$, where ${\displaystyle K}$ is a non-empty set, ${\displaystyle 0\in K}$, and { ${\displaystyle \cdot }$, ${\displaystyle +}$ } are binary operations on ${\displaystyle K}$. Let ${\displaystyle a\leq b}$ be defined as ${\displaystyle \exists x(a+x=b)}$. The frame conditions are the following.

1. ${\displaystyle 0\cdot x=x}$
2. ${\displaystyle x\cdot y=y\cdot x}$
3. ${\displaystyle (x\cdot y)\cdot z=x\cdot (y\cdot z)}$
4. ${\displaystyle x\leq x\cdot x}$
5. ${\displaystyle x+y=y+x}$
6. ${\displaystyle (x+y)+z=x+(y+z)}$
7. ${\displaystyle x+x=x}$
8. ${\displaystyle x\cdot (y+z)=x\cdot y+x\cdot z}$
9. ${\displaystyle x\leq y+z\Rightarrow \exists y',z'\in K(y'\leq y}$, ${\displaystyle z'\leq z}$ and ${\displaystyle x=y'+z')}$

An operational model ${\displaystyle M}$ is a frame ${\displaystyle F}$ with a valuation ${\displaystyle V}$ that maps pairs of points and atomic propositions to truth values, T or F. ${\displaystyle V}$ can be extended to a valuation ${\displaystyle \Vdash }$ on complex formulas as follows.

- ${\displaystyle M,a\Vdash p\iff V(a,p)=T}$, for atomic propositions
- ${\displaystyle M,a+b\Vdash p\iff M,a\Vdash p}$ and ${\displaystyle M,b\Vdash p}$
- ${\displaystyle M,a\Vdash A\land B\iff M,a\Vdash A}$ and ${\displaystyle M,a\Vdash B}$
- ${\displaystyle M,a\Vdash A\lor B\iff M,a\Vdash A}$ or ${\displaystyle M,a\Vdash B}$ or ${\displaystyle \exists b,c(a=b+c}$; ${\displaystyle M,b\Vdash A}$ and ${\displaystyle M,c\Vdash B)}$
- ${\displaystyle M,a\Vdash A\to B\iff \forall b(M,b\Vdash A\Rightarrow M,a\cdot b\Vdash B)}$

A formula ${\displaystyle A}$ holds in a model ${\displaystyle M}$ iff ${\displaystyle M,0\Vdash A}$. A formula ${\displaystyle A}$ is valid in a class of models ${\displaystyle C}$ iff it holds in each model ${\displaystyle M\in C}$.

The positive fragment of R is sound and complete with respect to the class of these models. Humberstone's semantics can be adapted to model different logics by dropping or adding frame conditions as follows.

<table><tbody><tr><th>System</th><th colspan="2">Frame conditions</th></tr><tr><th>B</th><td>1, 5-9, 14</td><td rowspan="8"><div><ol><li><math>{\displaystyle x\leq x\cdot 0}</math></li><li><math>{\displaystyle (x\cdot y)\cdot z\leq y\cdot (x\cdot z)}</math></li><li><math>{\displaystyle (x\cdot y)\cdot z\leq x\cdot (y\cdot z)}</math></li><li><math>{\displaystyle x\cdot y\leq (x\cdot y)\cdot y}</math></li><li><math>{\displaystyle (y+z)\cdot x=y\cdot x+z\cdot x}</math></li><li><math>{\displaystyle x\cdot x=x}</math></li></ol></div></td></tr><tr><th>TW</th><td>1, 11, 12, 5-9, 14</td></tr><tr><th>EW</th><td>1, 10, 11, 5-9, 14</td></tr><tr><th>RW</th><td>1-3, 5-9</td></tr><tr><th>T</th><td>1, 11, 12, 13, 5-9, 14</td></tr><tr><th>E</th><td>1, 10, 11, 13, 5-9, 14</td></tr><tr><th>R</th><td>1-9</td></tr><tr><th>RM</th><td>1-3, 5-9, 15</td></tr></tbody></table>

### Algebraic models

Some relevance logics can be given algebraic models, such as the logic R. The algebraic structures for R are de Morgan monoids, which are sextuples ${\displaystyle (D,\land ,\lor ,\lnot ,\circ ,e)}$ where

- ${\displaystyle (D,\land ,\lor ,\lnot )}$ is a distributive [lattice](https://en.wikipedia.org/wiki/Lattice_\(order\) "Lattice (order)") with a unary operation, ${\displaystyle \lnot }$ obeying the laws ${\displaystyle \lnot \lnot x=x}$ and if ${\displaystyle x\leq y}$ then ${\displaystyle \lnot y\leq \lnot x}$;
- ${\displaystyle e\in D}$, the binary operation ${\displaystyle \circ }$ is [commutative](https://en.wikipedia.org/wiki/Commutative_property "Commutative property") (${\displaystyle x\circ y=y\circ x}$) and [associative](https://en.wikipedia.org/wiki/Associative_property "Associative property") (${\displaystyle (x\circ y)\circ z=x\circ (y\circ z)}$), and ${\displaystyle e\circ x=x}$, i.e. ${\displaystyle (D,\circ ,e)}$ is an [Abelian monoid](https://en.wikipedia.org/wiki/Monoid#Commutative_monoid "Monoid") with [identity](https://en.wikipedia.org/wiki/Identity_element "Identity element") ${\displaystyle e}$;
- the monoid is lattice-ordered and satisfies ${\displaystyle x\circ (y\lor z)=(x\circ y)\lor (x\circ z)}$;
- ${\displaystyle x\leq x\circ x}$; and
- if ${\displaystyle x\circ y\leq z}$, then ${\displaystyle x\circ \lnot z\leq \lnot y}$.

The operation ${\displaystyle x\to y}$ interpreting the conditional of R is defined as ${\displaystyle \lnot (x\circ \lnot y)}$. A de Morgan monoid is a [residuated lattice](https://en.wikipedia.org/wiki/Residuated_lattice "Residuated lattice"), obeying the following residuation condition.

${\displaystyle x\circ y\leq z\iff x\leq y\to z}$

An interpretation ${\displaystyle v}$ is a [homomorphism](https://en.wikipedia.org/wiki/Homomorphism "Homomorphism") from the propositional language to a de Morgan monoid ${\displaystyle M}$ such that

- ${\displaystyle v(p)\in D}$ for all atomic propositions,
- ${\displaystyle v(\lnot A)=\lnot v(A)}$
- ${\displaystyle v(A\lor B)=v(A)\lor v(B)}$
- ${\displaystyle v(A\land B)=v(A)\land v(B)}$
- ${\displaystyle v(A\to B)=v(A)\to v(B)}$

Given a de Morgan monoid ${\displaystyle M}$ and an interpretation ${\displaystyle v}$, one can say that formula ${\displaystyle A}$ holds on ${\displaystyle v}$ just in case ${\displaystyle e\leq v(A)}$. A formula ${\displaystyle A}$ is valid just in case it holds on all interpretations on all de Morgan monoids. The logic R is sound and complete for de Morgan monoids.

[^1]: Mares, Edwin (1998). ["Relevance Logic"](https://plato.stanford.edu/entries/logic-relevance/). *Stanford Encyclopedia of Philosophy* (Substantive revision 2020 ed.). Metaphysics Research Lab, Stanford University.

[^2]: Dunn, J. Michael; Restall, Greg (2002). "Relevance Logic". In Dov M. Gabbay; Franz Guenthner (eds.). *Handbook of Philosophical Logic*. Vol. 6. Kluwer. pp. 1–136.

[^3]: Anderson, Alan Ross; Belnap, Nuel D. (1975). *Entailment: The Logic of Relevance and Necessity*. Vol. I. Princeton University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-691-07192-6](https://en.wikipedia.org/wiki/Special:BookSources/0-691-07192-6 "Special:BookSources/0-691-07192-6").

[^4]: Lewis, David (Dec 1988). ["Relevant implication"](https://onlinelibrary.wiley.com/doi/10.1111/j.1755-2567.1988.tb00716.x). *Theoria*. **54** (3): 161–174. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1111/j.1755-2567.1988.tb00716.x](https://doi.org/10.1111%2Fj.1755-2567.1988.tb00716.x). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0040-5825](https://search.worldcat.org/issn/0040-5825).

[^5]: MacColl, Hugh (1908). "'If' and 'imply'". *Mind*. **17**: 151–152, 453–455. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1093/mind/XVII.1.151](https://doi.org/10.1093%2Fmind%2FXVII.1.151).

[^6]: Lewis, C. I. (1912). "Implication and the Algebra of Logic." *[Mind](https://en.wikipedia.org/wiki/Mind_\(journal\) "Mind (journal)")*, **21** (84):522–531.

[^7]: Lewis, C. I. (1917). "The issues concerning material implication." *Journal of Philosophy, Psychology, and Scientific Methods*, **14**:350–356.

[^8]: [Ackermann, W.](https://en.wikipedia.org/wiki/Wilhelm_Ackermann "Wilhelm Ackermann") (1956), "Begründung einer strengen Implikation", *[Journal of Symbolic Logic](https://en.wikipedia.org/wiki/Journal_of_Symbolic_Logic "Journal of Symbolic Logic")*, **21** (2): 113–128, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2268750](https://doi.org/10.2307%2F2268750), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2268750](https://www.jstor.org/stable/2268750)

[^9]: Moh, Shaw-kwei (1950), "The Deduction Theorems and Two New Logical Systems", *Methodos*, **2**: 56–75 Moh Shaw-Kwei, 1950, "," Methodos 2 56–75.

[^10]: Church, A. (1951), *The Weak Theory of Implication* in *Kontroliertes Denken: Untersuchungen zum Logikkalkül und zur Logik der Einzelwissenschaften*, Kommissions-Verlag Karl Alber, edited by A. Menne, A. Wilhelmy and H. Angsil, pp. 22–37.

[^11]: Routley, Richard; Meyer, Robertk. (1973-01-01), ["The Semantics of Entailment"](https://www.sciencedirect.com/science/article/pii/S0049237X08715416), in Leblanc, Hugues (ed.), *Truth, Syntax and Modality*, Studies in Logic and the Foundations of Mathematics, vol. 68, Elsevier, pp. 199–243, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/s0049-237x(08)71541-6](https://doi.org/10.1016%2Fs0049-237x%2808%2971541-6), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-7204-2269-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-7204-2269-6 "Special:BookSources/978-0-7204-2269-6"), retrieved 2025-11-04

[^12]: Routley, Richard; Routley, Val (1972). "The Semantics of First Degree Entailment". *Noûs*. **6** (4): 335–359. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2214309](https://doi.org/10.2307%2F2214309). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2214309](https://www.jstor.org/stable/2214309).

[^13]: Urquhart, Alasdair (1972). "Semantics for Relevant Logics". *Journal of Symbolic Logic*. **37** (1): 159–169. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2272559](https://doi.org/10.2307%2F2272559). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2272559](https://www.jstor.org/stable/2272559).

[^14]: Fine, Kit (1974). "Models for Entailment". *Journal of Philosophical Logic*. **3**: 347–372. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BF00650195](https://doi.org/10.1007%2FBF00650195).

[^15]: Routley, Richard; Meyer, Robert K.; Plumwood, Val; Brady, Ross T. (1982). *Relevant Logics and their Rivals*. Ridgeview.