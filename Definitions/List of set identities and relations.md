---
title: "List of set identities and relations"
source: "https://en.wikipedia.org/wiki/List_of_set_identities_and_relations"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2020-11-01
created: 2026-04-10
description:
tags:
  - "clippings"
---
This article lists [mathematical](https://en.wikipedia.org/wiki/Mathematics "Mathematics") properties and laws of [sets](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)"), involving the set-theoretic [operations](https://en.wikipedia.org/wiki/Operation_\(mathematics\) "Operation (mathematics)") of [union](https://en.wikipedia.org/wiki/Union_\(set_theory\) "Union (set theory)"), [intersection](https://en.wikipedia.org/wiki/Intersection_\(set_theory\) "Intersection (set theory)"), and [complementation](https://en.wikipedia.org/wiki/Complement_\(set_theory\) "Complement (set theory)") and the [relations](https://en.wikipedia.org/wiki/Binary_relation "Binary relation") of set [equality](https://en.wikipedia.org/wiki/Equality_\(mathematics\) "Equality (mathematics)") and set [inclusion](https://en.wikipedia.org/wiki/Subset "Subset"). It also provides systematic procedures for evaluating expressions, and performing calculations, involving these operations and relations.

The [binary operations](https://en.wikipedia.org/wiki/Binary_operation "Binary operation") of set union (${\displaystyle \cup }$) and intersection (${\displaystyle \cap }$) satisfy many identities. Several of these identities or "laws" have well established names.

## Notation

Throughout this article, capital letters (such as ${\displaystyle A,B,C,L,M,R,S,}$ and ${\displaystyle X}$) will denote sets. On the left hand side of an identity, typically,

- ${\displaystyle L}$ will be the leftmost set,
- ${\displaystyle M}$ will be the middle set, and
- ${\displaystyle R}$ will be the rightmost set.

This is to facilitate applying identities to expressions that are complicated or use the same symbols as the identity.[^1] For example, the identity 
$$
{\displaystyle (L\,\setminus \,M)\,\setminus \,R~=~(L\,\setminus \,R)\,\setminus \,(M\,\setminus \,R)}
$$
 may be read as: 
$$
{\displaystyle ({\text{Left set}}\,\setminus \,{\text{Middle set}})\,\setminus \,{\text{Right set}}~=~({\text{Left set}}\,\setminus \,{\text{Right set}})\,\setminus \,({\text{Middle set}}\,\setminus \,{\text{Right set}}).}
$$

### Elementary set operations

For sets ${\displaystyle L}$ and ${\displaystyle R,}$ define: 
$$
{\displaystyle {\begin{alignedat}{4}L\cup R&&~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{~x~:~x\in L\;&&{\text{ or }}\;\,&&\;x\in R~\}\\L\cap R&&~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{~x~:~x\in L\;&&{\text{ and }}&&\;x\in R~\}\\L\setminus R&&~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{~x~:~x\in L\;&&{\text{ and }}&&\;x\notin R~\}\\\end{alignedat}}}
$$
 and 
$$
{\displaystyle L\triangle R~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{~x~:~x{\text{ belongs to exactly one of }}L{\text{ and }}R~\}}
$$
 where the *[symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference "Symmetric difference")* ${\displaystyle L\triangle R}$ is sometimes denoted by ${\displaystyle L\ominus R}$ and equals:[^11] [^12] 
$$
{\displaystyle {\begin{alignedat}{4}L\;\triangle \;R~&=~(L~\setminus ~&&R)~\cup ~&&(R~\setminus ~&&L)\\~&=~(L~\cup ~&&R)~\setminus ~&&(L~\cap ~&&R).\end{alignedat}}}
$$

One set ${\displaystyle L}$ is said to *intersect* another set ${\displaystyle R}$ if ${\displaystyle L\cap R\neq \varnothing .}$ Sets that do not intersect are said to be *[disjoint](https://en.wikipedia.org/wiki/Disjoint_sets "Disjoint sets")*.

The [power set](https://en.wikipedia.org/wiki/Power_set "Power set") of ${\displaystyle X}$ is the set of all subsets of ${\displaystyle X}$ and will be denoted by 
$$
{\displaystyle {\mathcal {P}}(X)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{~L~:~L\subseteq X~\}.}
$$

**Universe set and complement notation**

The notation 
$$
{\displaystyle L^{\complement }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~X\setminus L.}
$$
 may be used if ${\displaystyle L}$ is a subset of some set ${\displaystyle X}$ that is understood (say from context, or because it is clearly stated what the superset ${\displaystyle X}$ is). It is emphasized that the definition of ${\displaystyle L^{\complement }}$ depends on context. For instance, had ${\displaystyle L}$ been declared as a subset of ${\displaystyle Y,}$ with the sets ${\displaystyle Y}$ and ${\displaystyle X}$ not necessarily related to each other in any way, then ${\displaystyle L^{\complement }}$ would likely mean ${\displaystyle Y\setminus L}$ instead of ${\displaystyle X\setminus L.}$

If it is needed then unless indicated otherwise, it should be assumed that ${\displaystyle X}$ denotes the [universe set](https://en.wikipedia.org/wiki/Universe_\(mathematics\) "Universe (mathematics)"), which means that all sets that are used in the formula are subsets of ${\displaystyle X.}$ In particular, the [complement of a set](https://en.wikipedia.org/wiki/Complement_\(set_theory\) "Complement (set theory)") ${\displaystyle L}$ will be denoted by ${\displaystyle L^{\complement }}$ where unless indicated otherwise, it should be assumed that ${\displaystyle L^{\complement }}$ denotes the complement of ${\displaystyle L}$ in (the universe) ${\displaystyle X.}$

## One subset involved

Assume ${\displaystyle L\subseteq X.}$

**[Identity](https://en.wikipedia.org/wiki/Identity_element "Identity element")**:[^13]

**Definition**: ${\displaystyle e}$ is called a **[left identity element](https://en.wikipedia.org/wiki/Left_identity_element "Left identity element")** of a [binary operator](https://en.wikipedia.org/wiki/Binary_operator "Binary operator") ${\displaystyle \,\ast \,}$ if ${\displaystyle e\,\ast \,R=R}$ for all ${\displaystyle R}$ and it is called a **[right identity element](https://en.wikipedia.org/wiki/Right_identity_element "Right identity element")** of ${\displaystyle \,\ast \,}$ if ${\displaystyle L\,\ast \,e=L}$ for all ${\displaystyle L.}$ A left identity element that is also a right identity element if called an **[identity element](https://en.wikipedia.org/wiki/Identity_element "Identity element")**.

The empty set ${\displaystyle \varnothing }$ is an identity element of binary union ${\displaystyle \cup }$ and symmetric difference ${\displaystyle \triangle ,}$ and it is also a right identity element of set subtraction ${\displaystyle \,\setminus :}$

$$
{\displaystyle {\begin{alignedat}{10}L\cap X&\;=\;&&L&\;=\;&X\cap L~~~~{\text{ where }}L\subseteq X\\[1.4ex]L\cup \varnothing &\;=\;&&L&\;=\;&\varnothing \cup L\\[1.4ex]L\,\triangle \varnothing &\;=\;&&L&\;=\;&\varnothing \,\triangle L\\[1.4ex]L\setminus \varnothing &\;=\;&&L\\[1.4ex]\end{alignedat}}}
$$
 but ${\displaystyle \varnothing }$ is not a left identity element of ${\displaystyle \,\setminus \,}$ since 
$$
{\displaystyle \varnothing \setminus L=\varnothing }
$$
 so ${\textstyle \varnothing \setminus L=L}$ if and only if ${\displaystyle L=\varnothing .}$

**[Idempotence](https://en.wikipedia.org/wiki/Idempotent "Idempotent")** [^13] ${\displaystyle L\ast L=L}$ and **[Nilpotence](https://en.wikipedia.org/wiki/Nilpotent "Nilpotent")** ${\displaystyle L\ast L=\varnothing }$:

$$
{\displaystyle {\begin{alignedat}{10}L\cup L&\;=\;&&L&&\quad {\text{ (Idempotence)}}\\[1.4ex]L\cap L&\;=\;&&L&&\quad {\text{ (Idempotence)}}\\[1.4ex]L\,\triangle \,L&\;=\;&&\varnothing &&\quad {\text{ (Nilpotence of index 2)}}\\[1.4ex]L\setminus L&\;=\;&&\varnothing &&\quad {\text{ (Nilpotence of index 2)}}\\[1.4ex]\end{alignedat}}}
$$

**Domination** [^13] / [Absorbing element](https://en.wikipedia.org/wiki/Absorbing_element "Absorbing element"):

**Definition**: ${\displaystyle z}$ is called a **[left absorbing element](https://en.wikipedia.org/wiki/Left_absorbing_element "Left absorbing element")** of a [binary operator](https://en.wikipedia.org/wiki/Binary_operator "Binary operator") ${\displaystyle \,\ast \,}$ if ${\displaystyle z\,\ast \,R=z}$ for all ${\displaystyle R}$ and it is called a **[right absorbing element](https://en.wikipedia.org/wiki/Right_absorbing_element "Right absorbing element")** of ${\displaystyle \,\ast \,}$ if ${\displaystyle L\,\ast \,z=z}$ for all ${\displaystyle L.}$ A left absorbing element that is also a right absorbing element if called an **[absorbing element](https://en.wikipedia.org/wiki/Absorbing_element "Absorbing element")**. Absorbing elements are also sometime called **annihilating elements** or **zero elements**.

A universe set is an absorbing element of binary union ${\displaystyle \cup .}$ The empty set ${\displaystyle \varnothing }$ is an absorbing element of binary intersection ${\displaystyle \cap }$ and binary Cartesian product ${\displaystyle \times ,}$ and it is also a left absorbing element of set subtraction ${\displaystyle \,\setminus :}$

$$
{\displaystyle {\begin{alignedat}{10}X\cup L&\;=\;&&X&\;=\;&L\cup X~~~~{\text{ where }}L\subseteq X\\[1.4ex]\varnothing \cap L&\;=\;&&\varnothing &\;=\;&L\cap \varnothing \\[1.4ex]\varnothing \times L&\;=\;&&\varnothing &\;=\;&L\times \varnothing \\[1.4ex]\varnothing \setminus L&\;=\;&&\varnothing &\;\;&\\[1.4ex]\end{alignedat}}}
$$
 but ${\displaystyle \varnothing }$ is not a right absorbing element of set subtraction since 
$$
{\displaystyle L\setminus \varnothing =L}
$$
 where ${\textstyle L\setminus \varnothing =\varnothing }$ if and only if ${\textstyle L=\varnothing .}$

**Double complement** or **[involution](https://en.wikipedia.org/wiki/Involution_\(mathematics\) "Involution (mathematics)") law**:

$$
{\displaystyle {\begin{alignedat}{10}X\setminus (X\setminus L)&=L&&\qquad {\text{ Also written }}\quad &&\left(L^{\complement }\right)^{\complement }=L&&\quad &&{\text{ where }}L\subseteq X\quad {\text{ (Double complement/Involution law)}}\\[1.4ex]\end{alignedat}}}
$$

$$
{\displaystyle L\setminus \varnothing =L}
$$
 
$$
{\displaystyle {\begin{alignedat}{4}\varnothing &=L&&\setminus L\\&=\varnothing &&\setminus L\\&=L&&\setminus X~~~~{\text{ where }}L\subseteq X\\\end{alignedat}}}
$$
 [^13]

$$
{\displaystyle L^{\complement }=X\setminus L\quad {\text{ (definition of notation)}}}
$$

$$
{\displaystyle {\begin{alignedat}{10}L\,\cup (X\setminus L)&=X&&\qquad {\text{ Also written }}\quad &&L\cup L^{\complement }=X&&\quad &&{\text{ where }}L\subseteq X\\[1.4ex]L\,\triangle (X\setminus L)&=X&&\qquad {\text{ Also written }}\quad &&L\,\triangle L^{\complement }=X&&\quad &&{\text{ where }}L\subseteq X\\[1.4ex]L\,\cap (X\setminus L)&=\varnothing &&\qquad {\text{ Also written }}\quad &&L\cap L^{\complement }=\varnothing &&\quad &&\\[1.4ex]\end{alignedat}}}
$$
 [^13]

$$
{\displaystyle {\begin{alignedat}{10}X\setminus \varnothing &=X&&\qquad {\text{ Also written }}\quad &&\varnothing ^{\complement }=X&&\quad &&{\text{ (Complement laws for the empty set))}}\\[1.4ex]X\setminus X&=\varnothing &&\qquad {\text{ Also written }}\quad &&X^{\complement }=\varnothing &&\quad &&{\text{ (Complement laws for the universe set)}}\\[1.4ex]\end{alignedat}}}
$$

## Two sets involved

In the left hand sides of the following identities, ${\displaystyle L}$ is the *L*  eft most set and ${\displaystyle R}$ is the *R*  ight most set. Assume both ${\displaystyle L{\text{ and }}R}$ are subsets of some universe set ${\displaystyle X.}$

### Formulas for binary set operations ⋂, ⋃, \\, and ∆

In the left hand sides of the following identities, L is the *L*  eft most set and R is the *R*  ight most set. Whenever necessary, both L and R should be assumed to be subsets of some universe set X, so that ${\displaystyle L^{\complement }:=X\setminus L{\text{ and }}R^{\complement }:=X\setminus R.}$

$$
{\displaystyle {\begin{alignedat}{9}L\cap R&=L&&\,\,\setminus \,&&(L&&\,\,\setminus &&R)\\&=R&&\,\,\setminus \,&&(R&&\,\,\setminus &&L)\\&=L&&\,\,\setminus \,&&(L&&\,\triangle \,&&R)\\&=L&&\,\triangle \,&&(L&&\,\,\setminus &&R)\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{9}L\cup R&=(&&L\,\triangle \,R)&&\,\,\cup &&&&L&&&&\\&=(&&L\,\triangle \,R)&&\,\triangle \,&&(&&L&&\cap \,&&R)\\&=(&&R\,\setminus \,L)&&\,\,\cup &&&&L&&&&~~~~~{\text{ (union is disjoint)}}\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{9}L\,\triangle \,R&=&&R\,\triangle \,L&&&&&&&&\\&=(&&L\,\cup \,R)&&\,\setminus \,&&(&&L\,\,\cap \,R)&&\\&=(&&L\,\setminus \,R)&&\cup \,&&(&&R\,\,\setminus \,L)&&~~~~~{\text{ (union is disjoint)}}\\&=(&&L\,\triangle \,M)&&\,\triangle \,&&(&&M\,\triangle \,R)&&~~~~~{\text{ where }}M{\text{ is an arbitrary set. }}\\&=(&&L^{\complement })&&\,\triangle \,&&(&&R^{\complement })&&\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{9}L\setminus R&=&&L&&\,\,\setminus &&(L&&\,\,\cap &&R)\\&=&&L&&\,\,\cap &&(L&&\,\triangle \,&&R)\\&=&&L&&\,\triangle \,&&(L&&\,\,\cap &&R)\\&=&&R&&\,\triangle \,&&(L&&\,\,\cup &&R)\\\end{alignedat}}}
$$

### De Morgan's laws

**[De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws")** state that for ${\displaystyle L,R\subseteq X:}$

$$
{\displaystyle {\begin{alignedat}{10}X\setminus (L\cap R)&=(X\setminus L)\cup (X\setminus R)&&\qquad {\text{ Also written }}\quad &&(L\cap R)^{\complement }=L^{\complement }\cup R^{\complement }&&\quad &&{\text{ (De Morgan's law)}}\\[1.4ex]X\setminus (L\cup R)&=(X\setminus L)\cap (X\setminus R)&&\qquad {\text{ Also written }}\quad &&(L\cup R)^{\complement }=L^{\complement }\cap R^{\complement }&&\quad &&{\text{ (De Morgan's law)}}\\[1.4ex]\end{alignedat}}}
$$

### Commutativity

Unions, intersection, and symmetric difference are **[commutative operations](https://en.wikipedia.org/wiki/Commutative_operation "Commutative operation")**:[^13]

$$
{\displaystyle {\begin{alignedat}{10}L\cup R&\;=\;&&R\cup L&&\quad {\text{ (Commutativity)}}\\[1.4ex]L\cap R&\;=\;&&R\cap L&&\quad {\text{ (Commutativity)}}\\[1.4ex]L\,\triangle R&\;=\;&&R\,\triangle L&&\quad {\text{ (Commutativity)}}\\[1.4ex]\end{alignedat}}}
$$

Set subtraction is not commutative. However, the commutativity of set subtraction can be characterized: from ${\displaystyle (L\,\setminus \,R)\cap (R\,\setminus \,L)=\varnothing }$ it follows that: 
$$
{\displaystyle L\,\setminus \,R=R\,\setminus \,L\quad {\text{ if and only if }}\quad L=R.}
$$
 Said differently, if distinct symbols always represented distinct sets, then the *only* true formulas of the form ${\displaystyle \,\cdot \,\,\setminus \,\,\cdot \,=\,\cdot \,\,\setminus \,\,\cdot \,}$ that could be written would be those involving a single symbol; that is, those of the form: ${\displaystyle S\,\setminus \,S=S\,\setminus \,S.}$ But such formulas are necessarily true for *every* binary operation ${\displaystyle \,\ast \,}$ (because ${\displaystyle x\,\ast \,x=x\,\ast \,x}$ must hold by definition of [equality](https://en.wikipedia.org/wiki/Equality_\(mathematics\) "Equality (mathematics)")), and so in this sense, set subtraction is as diametrically opposite to being commutative as is possible for a binary operation. Set subtraction is also neither [left alternative](https://en.wikipedia.org/wiki/Left_alternative "Left alternative") nor [right alternative](https://en.wikipedia.org/wiki/Right_alternative "Right alternative"); instead, ${\displaystyle (L\setminus L)\setminus R=L\setminus (L\setminus R)}$ if and only if ${\displaystyle L\cap R=\varnothing }$ if and only if ${\displaystyle (R\setminus L)\setminus L=R\setminus (L\setminus L).}$ Set subtraction is [quasi-commutative](https://en.wikipedia.org/wiki/Quasi-commutative "Quasi-commutative") and satisfies the [Jordan identity](https://en.wikipedia.org/wiki/Jordan_identity "Jordan identity").

### Other identities involving two sets

**[Absorption laws](https://en.wikipedia.org/wiki/Absorption_law "Absorption law")**:

$$
{\displaystyle {\begin{alignedat}{4}L\cup (L\cap R)&\;=\;&&L&&\quad {\text{ (Absorption)}}\\[1.4ex]L\cap (L\cup R)&\;=\;&&L&&\quad {\text{ (Absorption)}}\\[1.4ex]\end{alignedat}}}
$$

**Other properties**

$$
{\displaystyle {\begin{alignedat}{10}L\setminus R&=L\cap (X\setminus R)&&\qquad {\text{ Also written }}\quad &&L\setminus R=L\cap R^{\complement }&&\quad &&{\text{ where }}L,R\subseteq X\\[1.4ex]X\setminus (L\setminus R)&=(X\setminus L)\cup R&&\qquad {\text{ Also written }}\quad &&(L\setminus R)^{\complement }=L^{\complement }\cup R&&\quad &&{\text{ where }}R\subseteq X\\[1.4ex]L\setminus R&=(X\setminus R)\setminus (X\setminus L)&&\qquad {\text{ Also written }}\quad &&L\setminus R=R^{\complement }\setminus L^{\complement }&&\quad &&{\text{ where }}L,R\subseteq X\\[1.4ex]\end{alignedat}}}
$$

**Intervals**:

$$
{\displaystyle (a,b)\cap (c,d)=(\max\{a,c\},\min\{b,d\})}
$$
 
$$
{\displaystyle [a,b)\cap [c,d)=[\max\{a,c\},\min\{b,d\})}
$$

### Subsets ⊆ and supersets ⊇

The following statements are equivalent for any ${\displaystyle L,R\subseteq X:}$ [^13]

1. ${\displaystyle L\subseteq R}$
	- Definition of *[subset](https://en.wikipedia.org/wiki/Subset "Subset")*: if ${\displaystyle l\in L}$ then ${\displaystyle l\in R}$
2. ${\displaystyle L\cap R=L}$
3. ${\displaystyle L\cup R=R}$
4. ${\displaystyle L\,\triangle \,R=R\setminus L}$
5. ${\displaystyle L\,\triangle \,R\subseteq R\setminus L}$
6. ${\displaystyle L\setminus R=\varnothing }$
7. ${\displaystyle L}$ and ${\displaystyle X\setminus R}$ are disjoint (that is, ${\displaystyle L\cap (X\setminus R)=\varnothing }$)
8. ${\displaystyle X\setminus R\subseteq X\setminus L\qquad }$ (that is, ${\displaystyle R^{\complement }\subseteq L^{\complement }}$)

The following statements are equivalent for any ${\displaystyle L,R\subseteq X:}$

1. ${\displaystyle L\not \subseteq R}$
2. There exists some ${\displaystyle l\in L\setminus R.}$

#### Set equality

The following statements are equivalent:

1. ${\displaystyle L=R}$
2. ${\displaystyle L\,\triangle \,R=\varnothing }$
3. ${\displaystyle L\,\setminus \,R=R\,\setminus \,L}$
- If ${\displaystyle L\cap R=\varnothing }$ then ${\displaystyle L=R}$ if and only if ${\displaystyle L=\varnothing =R.}$
- **Uniqueness of complements**: If ${\textstyle L\cup R=X{\text{ and }}L\cap R=\varnothing }$ then ${\displaystyle R=X\setminus L}$

##### Empty set

A set ${\displaystyle L}$ is **[empty](https://en.wikipedia.org/wiki/Axiom_of_empty_set "Axiom of empty set")** if the sentence ${\displaystyle \forall x(x\not \in L)}$ is true, where the notation ${\displaystyle x\not \in L}$ is shorthand for ${\displaystyle \lnot (x\in L).}$

If ${\displaystyle L}$ is any set then the following are equivalent:

1. ${\displaystyle L}$ is not empty, meaning that the sentence ${\displaystyle \lnot [\forall x(x\not \in L)]}$ is true (literally, the [logical negation](https://en.wikipedia.org/wiki/Logical_negation "Logical negation") of " ${\displaystyle L}$ is empty" holds true).
2. (In [classical mathematics](https://en.wikipedia.org/wiki/Constructivism_\(philosophy_of_mathematics\) "Constructivism (philosophy of mathematics)")) ${\displaystyle L}$ is [inhabited](https://en.wikipedia.org/wiki/Inhabited_set "Inhabited set"), meaning: ${\displaystyle \exists x(x\in L)}$
	- In [constructive mathematics](https://en.wikipedia.org/wiki/Constructive_mathematics "Constructive mathematics"), "not empty" and "inhabited" are not equivalent: every inhabited set is not empty but the converse is not always guaranteed; that is, in constructive mathematics, a set ${\displaystyle L}$ that is not empty (where by definition, " ${\displaystyle L}$ is empty" means that the statement ${\displaystyle \forall x(x\not \in L)}$ is true) might not have an [inhabitant](https://en.wiktionary.org/wiki/inhabitant#English "wiktionary:inhabitant") (which is an ${\displaystyle x}$ such that ${\displaystyle x\in L}$).
3. ${\displaystyle L\not \subseteq R}$ for some set ${\displaystyle R}$

If ${\displaystyle L}$ is any set then the following are equivalent:

1. ${\displaystyle L}$ is empty (${\displaystyle L=\varnothing }$), meaning: ${\displaystyle \forall x(x\not \in L)}$
2. ${\displaystyle L\cup R\subseteq R}$ for every set ${\displaystyle R}$
3. ${\displaystyle L\subseteq R}$ for every set ${\displaystyle R}$
4. ${\displaystyle L\subseteq R\setminus L}$ for some/every set ${\displaystyle R}$
5. ${\displaystyle \varnothing /L=L}$

Given any ${\displaystyle x,}$ the following are equivalent:

1. ${\textstyle x\not \in L\setminus R}$
2. ${\textstyle x\in L\cap R\;{\text{ or }}\;x\not \in L.}$
3. ${\textstyle x\in R\;{\text{ or }}\;x\not \in L.}$

Moreover, 
$$
{\displaystyle (L\setminus R)\cap R=\varnothing \qquad {\text{ always holds}}.}
$$

#### Meets, Joins, and lattice properties

**Inclusion is a [partial order](https://en.wikipedia.org/wiki/Partial_order "Partial order")**: Explicitly, this means that [inclusion](https://en.wikipedia.org/wiki/Subset "Subset") ${\displaystyle \,\subseteq ,\,}$ which is a [binary operation](https://en.wikipedia.org/wiki/Binary_operation "Binary operation"), has the following three properties:[^13]

- **[Reflexivity](https://en.wikipedia.org/wiki/Reflexive_relation "Reflexive relation")**: ${\textstyle L\subseteq L}$
- **[Antisymmetry](https://en.wikipedia.org/wiki/Antisymmetric_relation "Antisymmetric relation")**: ${\textstyle (L\subseteq R{\text{ and }}R\subseteq L){\text{ if and only if }}L=R}$
- **[Transitivity](https://en.wikipedia.org/wiki/Transitive_relation "Transitive relation")**: ${\textstyle {\text{If }}L\subseteq M{\text{ and }}M\subseteq R{\text{ then }}L\subseteq R}$

The following proposition says that for any set ${\displaystyle S,}$ the [power set](https://en.wikipedia.org/wiki/Power_set "Power set") of ${\displaystyle S,}$ ordered by inclusion, is a [bounded lattice](https://en.wikipedia.org/wiki/Lattice_\(order\) "Lattice (order)"), and hence together with the distributive and complement laws above, show that it is a [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra_\(structure\) "Boolean algebra (structure)").

**Existence of a [least element](https://en.wikipedia.org/wiki/Least_element "Least element") and a [greatest element](https://en.wikipedia.org/wiki/Greatest_element "Greatest element")**: 
$$
{\displaystyle \varnothing \subseteq L\subseteq X}
$$

**[Joins](https://en.wikipedia.org/wiki/Join_\(mathematics\) "Join (mathematics)") /supremums exist**:[^13] 
$$
{\displaystyle L\subseteq L\cup R}
$$

The union ${\displaystyle L\cup R}$ is the join/supremum of ${\displaystyle L}$ and ${\displaystyle R}$ with respect to ${\displaystyle \,\subseteq \,}$ because:

1. ${\displaystyle L\subseteq L\cup R}$ and ${\displaystyle R\subseteq L\cup R,}$ and
2. if ${\displaystyle Z}$ is a set such that ${\displaystyle L\subseteq Z}$ and ${\displaystyle R\subseteq Z}$ then ${\displaystyle L\cup R\subseteq Z.}$

The intersection ${\displaystyle L\cap R}$ is the join/supremum of ${\displaystyle L}$ and ${\displaystyle R}$ with respect to ${\displaystyle \,\supseteq .\,}$

**[Meets](https://en.wikipedia.org/wiki/Meet_\(mathematics\) "Meet (mathematics)") /infimums exist**:[^13] 
$$
{\displaystyle L\cap R\subseteq L}
$$

The intersection ${\displaystyle L\cap R}$ is the meet/infimum of ${\displaystyle L}$ and ${\displaystyle R}$ with respect to ${\displaystyle \,\subseteq \,}$ because:

1. if ${\displaystyle L\cap R\subseteq L}$ and ${\displaystyle L\cap R\subseteq R,}$ and
2. if ${\displaystyle Z}$ is a set such that ${\displaystyle Z\subseteq L}$ and ${\displaystyle Z\subseteq R}$ then ${\displaystyle Z\subseteq L\cap R.}$

The union ${\displaystyle L\cup R}$ is the meet/infimum of ${\displaystyle L}$ and ${\displaystyle R}$ with respect to ${\displaystyle \,\supseteq .\,}$

**Other inclusion properties**:

$$
{\displaystyle L\setminus R\subseteq L}
$$
 
$$
{\displaystyle (L\setminus R)\cap L=L\setminus R}
$$

- If ${\displaystyle L\subseteq R}$ then ${\displaystyle L\,\triangle \,R=R\setminus L.}$
- If ${\displaystyle L\subseteq X}$ and ${\displaystyle R\subseteq Y}$ then ${\displaystyle L\times R\subseteq X\times Y}$ [^13]

## Three sets involved

In the left hand sides of the following identities, ${\displaystyle L}$ is the *L*  eft most set, ${\displaystyle M}$ is the *M*  iddle set, and ${\displaystyle R}$ is the *R*  ight most set.

### Precedence rules

There is no universal agreement on the [order of precedence](https://en.wikipedia.org/wiki/Precedence_rule "Precedence rule") of the basic set operators. Nevertheless, many authors use [precedence rules](https://en.wikipedia.org/wiki/Precedence_rule "Precedence rule") for set operators, although these rules vary with the author.

One common convention is to associate intersection ${\displaystyle L\cap R=\{x:(x\in L)\land (x\in R)\}}$ with [logical conjunction (and)](https://en.wikipedia.org/wiki/Logical_conjunction "Logical conjunction") ${\displaystyle L\land R}$ and associate union ${\displaystyle L\cup R=\{x:(x\in L)\lor (x\in R)\}}$ with [logical disjunction (or)](https://en.wikipedia.org/wiki/Logical_disjunction "Logical disjunction") ${\displaystyle L\lor R,}$ and then transfer the [precedence of these logical operators](https://en.wikipedia.org/wiki/Logical_connective#Order_of_precedence "Logical connective") (where ${\displaystyle \,\land \,}$ has precedence over ${\displaystyle \,\lor \,}$) to these set operators, thereby giving ${\displaystyle \,\cap \,}$ precedence over ${\displaystyle \,\cup .\,}$ So for example, ${\displaystyle L\cup M\cap R}$ would mean ${\displaystyle L\cup (M\cap R)}$ since it would be associated with the logical statement ${\displaystyle L\lor M\land R~=~L\lor (M\land R)}$ and similarly, ${\displaystyle L\cup M\cap R\cup Z}$ would mean ${\displaystyle L\cup (M\cap R)\cup Z}$ since it would be associated with ${\displaystyle L\lor M\land R\lor Z~=~L\lor (M\land R)\lor Z.}$

Sometimes, set complement (subtraction) ${\displaystyle \,\setminus \,}$ is also associated with [logical complement (not)](https://en.wikipedia.org/wiki/Logical_complement "Logical complement") ${\displaystyle \,\lnot ,\,}$ in which case it will have the highest precedence. More specifically, ${\displaystyle L\setminus R=\{x:(x\in L)\land \lnot (x\in R)\}}$ is rewritten ${\displaystyle L\land \lnot R}$ so that for example, ${\displaystyle L\cup M\setminus R}$ would mean ${\displaystyle L\cup (M\setminus R)}$ since it would be rewritten as the logical statement ${\displaystyle L\lor M\land \lnot R}$ which is equal to ${\displaystyle L\lor (M\land \lnot R).}$ For another example, because ${\displaystyle L\land \lnot M\land R}$ means ${\displaystyle L\land (\lnot M)\land R,}$ which is equal to both ${\displaystyle (L\land (\lnot M))\land R}$ and ${\displaystyle L\land ((\lnot M)\land R)~=~L\land (R\land (\lnot M))}$ (where ${\displaystyle (\lnot M)\land R}$ was rewritten as ${\displaystyle R\land (\lnot M)}$), the formula ${\displaystyle L\setminus M\cap R}$ would refer to the set ${\displaystyle (L\setminus M)\cap R=L\cap (R\setminus M);}$ moreover, since ${\displaystyle L\land (\lnot M)\land R=(L\land R)\land \lnot M,}$ this set is also equal to ${\displaystyle (L\cap R)\setminus M}$ (other set identities can similarly be deduced from [propositional calculus](https://en.wikipedia.org/wiki/Propositional_calculus "Propositional calculus") [identities](https://en.wikipedia.org/wiki/Logical_equivalence "Logical equivalence") in this way). However, because set subtraction is not associative ${\displaystyle (L\setminus M)\setminus R\neq L\setminus (M\setminus R),}$ a formula such as ${\displaystyle L\setminus M\setminus R}$ would be ambiguous; for this reason, among others, set subtraction is often not assigned any precedence at all.

[Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference "Symmetric difference") ${\displaystyle L\triangle R=\{x:(x\in L)\oplus (x\in R)\}}$ is sometimes associated with [exclusive or (xor)](https://en.wikipedia.org/wiki/Exclusive_or "Exclusive or") ${\displaystyle L\oplus R}$ (also sometimes denoted by ${\displaystyle \,\veebar }$), in which case if the order of precedence from highest to lowest is ${\displaystyle \,\lnot ,\,\oplus ,\,\land ,\,\lor \,}$ then the order of precedence (from highest to lowest) for the set operators would be ${\displaystyle \,\setminus ,\,\triangle ,\,\cap ,\,\cup .}$ There is no universal agreement on the precedence of exclusive disjunction ${\displaystyle \,\oplus \,}$ with respect to the other logical connectives, which is why symmetric difference ${\displaystyle \,\triangle \,}$ is not often assigned a precedence.

### Associativity

**Definition**: A [binary operator](https://en.wikipedia.org/wiki/Binary_operator "Binary operator") ${\displaystyle \,\ast \,}$ is called **[associative](https://en.wikipedia.org/wiki/Associativity "Associativity")** if ${\displaystyle (L\,\ast \,M)\,\ast \,R=L\,\ast \,(M\,\ast \,R)}$ always holds.

The following set operators are associative:[^13]

$$
{\displaystyle {\begin{alignedat}{5}(L\cup M)\cup R&\;=\;\;&&L\cup (M\cup R)\\[1.4ex](L\cap M)\cap R&\;=\;\;&&L\cap (M\cap R)\\[1.4ex](L\,\triangle M)\,\triangle R&\;=\;\;&&L\,\triangle (M\,\triangle R)\\[1.4ex]\end{alignedat}}}
$$

For set subtraction, instead of associativity, only the following is always guaranteed: 
$$
{\displaystyle (L\,\setminus \,M)\,\setminus \,R\;~~{\color {red}{\subseteq }}~~\;L\,\setminus \,(M\,\setminus \,R)}
$$
 where equality holds if and only if ${\displaystyle L\cap R=\varnothing }$ (this condition does not depend on ${\displaystyle M}$). Thus ${\textstyle \;(L\setminus M)\setminus R=L\setminus (M\setminus R)\;}$ if and only if ${\displaystyle \;(R\setminus M)\setminus L=R\setminus (M\setminus L),\;}$ where the only difference between the left and right hand side set equalities is that the locations of ${\displaystyle L{\text{ and }}R}$ have been swapped.

### Distributivity

**Definition**: If ${\displaystyle \ast {\text{ and }}\bullet }$ are [binary operators](https://en.wikipedia.org/wiki/Binary_operator "Binary operator") then *${\displaystyle \,\ast \,}$ [**left distributes** over](https://en.wikipedia.org/wiki/Distributivity "Distributivity") ${\displaystyle \,\bullet \,}$* if 
$$
{\displaystyle L\,\ast \,(M\,\bullet \,R)~=~(L\,\ast \,M)\,\bullet \,(L\,\ast \,R)\qquad \qquad {\text{ for all }}L,M,R}
$$
 while *${\displaystyle \,\ast \,}$ [**right distributes** over](https://en.wikipedia.org/wiki/Distributivity "Distributivity") ${\displaystyle \,\bullet \,}$* if 
$$
{\displaystyle (L\,\bullet \,M)\,\ast \,R~=~(L\,\ast \,R)\,\bullet \,(M\,\ast \,R)\qquad \qquad {\text{ for all }}L,M,R.}
$$
 The operator *${\displaystyle \,\ast \,}$ [**distributes** over](https://en.wikipedia.org/wiki/Distributivity "Distributivity") ${\displaystyle \,\bullet \,}$* if it both left distributes and right distributes over ${\displaystyle \,\bullet \,.\,}$ In the definitions above, to transform one side to the other, the innermost operator (the operator inside the parentheses) becomes the outermost operator and the outermost operator becomes the innermost operator.

**[Right distributivity](https://en.wikipedia.org/wiki/Right_distributivity "Right distributivity")**:[^13]

$$
{\displaystyle {\begin{alignedat}{9}(L\,\cap \,M)\,\cup \,R~&~~=~~&&(L\,\cup \,R)\,&&\cap \,&&(M\,\cup \,R)\qquad &&{\text{ (Right-distributivity of }}\,\cup \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex](L\,\cup \,M)\,\cup \,R~&~~=~~&&(L\,\cup \,R)\,&&\cup \,&&(M\,\cup \,R)\qquad &&{\text{ (Right-distributivity of }}\,\cup \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex](L\,\cup \,M)\,\cap \,R~&~~=~~&&(L\,\cap \,R)\,&&\cup \,&&(M\,\cap \,R)\qquad &&{\text{ (Right-distributivity of }}\,\cap \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex](L\,\cap \,M)\,\cap \,R~&~~=~~&&(L\,\cap \,R)\,&&\cap \,&&(M\,\cap \,R)\qquad &&{\text{ (Right-distributivity of }}\,\cap \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex](L\,\triangle \,M)\,\cap \,R~&~~=~~&&(L\,\cap \,R)\,&&\triangle \,&&(M\,\cap \,R)\qquad &&{\text{ (Right-distributivity of }}\,\cap \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex](L\,\cap \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\cap \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex](L\,\cup \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\cup \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex](L\,\setminus \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\setminus \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\setminus \,{\text{)}}\\[1.4ex](L\,\triangle \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\triangle \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex](L\,\cup \,M)\,\setminus \,R~&~~=~~&&(L\,\setminus \,R)\,&&\cup \,&&(M\,\setminus \,R)\qquad &&{\text{ (Right-distributivity of }}\,\setminus \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex](L\,\cap \,M)\,\setminus \,R~&~~=~~&&(L\,\setminus \,R)\,&&\cap \,&&(M\,\setminus \,R)\qquad &&{\text{ (Right-distributivity of }}\,\setminus \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex](L\,\triangle \,M)\,\setminus \,R~&~~=~~&&(L\,\setminus \,R)&&\,\triangle \,&&(M\,\setminus \,R)\qquad &&{\text{ (Right-distributivity of }}\,\setminus \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex](L\,\setminus \,M)\,\setminus \,R~&~~=~~&&(L\,\setminus \,R)&&\,\setminus \,&&(M\,\setminus \,R)\qquad &&{\text{ (Right-distributivity of }}\,\setminus \,{\text{ over }}\,\setminus \,{\text{)}}\\[1.4ex]~&~~=~~&&~~\;~~\;~~\;~L&&\,\setminus \,&&(M\cup R)\\[1.4ex]\end{alignedat}}}
$$

**[Left distributivity](https://en.wikipedia.org/wiki/Left_distributivity "Left distributivity")**:[^13]

$$
{\displaystyle {\begin{alignedat}{5}L\cup (M\cap R)&\;=\;\;&&(L\cup M)\cap (L\cup R)\qquad &&{\text{ (Left-distributivity of }}\,\cup \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex]L\cup (M\cup R)&\;=\;\;&&(L\cup M)\cup (L\cup R)&&{\text{ (Left-distributivity of }}\,\cup \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]L\cap (M\cup R)&\;=\;\;&&(L\cap M)\cup (L\cap R)&&{\text{ (Left-distributivity of }}\,\cap \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]L\cap (M\cap R)&\;=\;\;&&(L\cap M)\cap (L\cap R)&&{\text{ (Left-distributivity of }}\,\cap \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex]L\cap (M\,\triangle \,R)&\;=\;\;&&(L\cap M)\,\triangle \,(L\cap R)&&{\text{ (Left-distributivity of }}\,\cap \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex]L\times (M\cap R)&\;=\;\;&&(L\times M)\cap (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex]L\times (M\cup R)&\;=\;\;&&(L\times M)\cup (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]L\times (M\,\setminus R)&\;=\;\;&&(L\times M)\,\setminus (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\setminus \,{\text{)}}\\[1.4ex]L\times (M\,\triangle R)&\;=\;\;&&(L\times M)\,\triangle (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex]\end{alignedat}}}
$$

#### Distributivity and symmetric difference ∆

Intersection distributes over symmetric difference: 
$$
{\displaystyle {\begin{alignedat}{5}L\,\cap \,(M\,\triangle \,R)~&~~=~~&&(L\,\cap \,M)\,\triangle \,(L\,\cap \,R)~&&~\\[1.4ex]\end{alignedat}}}
$$
 
$$
{\displaystyle {\begin{alignedat}{5}(L\,\triangle \,M)\,\cap \,R~&~~=~~&&(L\,\cap \,R)\,\triangle \,(M\,\cap \,R)~&&~\\[1.4ex]\end{alignedat}}}
$$

Union does not distribute over symmetric difference because only the following is guaranteed in general: 
$$
{\displaystyle {\begin{alignedat}{5}L\cup (M\,\triangle \,R)~~{\color {red}{\supseteq }}~~\color {black}{\,}(L\cup M)\,\triangle \,(L\cup R)~&~=~&&(M\,\triangle \,R)\,\setminus \,L&~=~&&(M\,\setminus \,L)\,\triangle \,(R\,\setminus \,L)\\[1.4ex]\end{alignedat}}}
$$

Symmetric difference does not distribute over itself: 
$$
{\displaystyle L\,\triangle \,(M\,\triangle \,R)~~{\color {red}{\neq }}~~\color {black}{\,}(L\,\triangle \,M)\,\triangle \,(L\,\triangle \,R)~=~M\,\triangle \,R}
$$
 and in general, for any sets ${\displaystyle L{\text{ and }}A}$ (where ${\displaystyle A}$ represents ${\displaystyle M\,\triangle \,R}$), ${\displaystyle L\,\triangle \,A}$ might not be a subset, nor a superset, of ${\displaystyle L}$ (and the same is true for ${\displaystyle A}$).

#### Distributivity and set subtraction \\

**Failure of set subtraction to left distribute**:

Set subtraction is *right* distributive over itself. However, set subtraction is *not* left distributive over itself because only the following is guaranteed in general: 
$$
{\displaystyle {\begin{alignedat}{5}L\,\setminus \,(M\,\setminus \,R)&~~{\color {red}{\supseteq }}~~&&\color {black}{\,}(L\,\setminus \,M)\,\setminus \,(L\,\setminus \,R)~~=~~L\cap R\,\setminus \,M\\[1.4ex]\end{alignedat}}}
$$
 where equality holds if and only if ${\displaystyle L\,\setminus \,M=L\,\cap \,R,}$ which happens [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") ${\displaystyle L\cap M\cap R=\varnothing {\text{ and }}L\setminus M\subseteq R.}$

For symmetric difference, the sets ${\displaystyle L\,\setminus \,(M\,\triangle \,R)}$ and ${\displaystyle (L\,\setminus \,M)\,\triangle \,(L\,\setminus \,R)=L\,\cap \,(M\,\triangle \,R)}$ are always disjoint. So these two sets are equal if and only if they are both equal to ${\displaystyle \varnothing .}$ Moreover, ${\displaystyle L\,\setminus \,(M\,\triangle \,R)=\varnothing }$ if and only if ${\displaystyle L\cap M\cap R=\varnothing {\text{ and }}L\subseteq M\cup R.}$

To investigate the left distributivity of set subtraction over unions or intersections, consider how the sets involved in (both of) De Morgan's laws are all related: 
$$
{\displaystyle {\begin{alignedat}{5}(L\,\setminus \,M)\,\cap \,(L\,\setminus \,R)~~=~~L\,\setminus \,(M\,\cup \,R)~&~~{\color {red}{\subseteq }}~~&&\color {black}{\,}L\,\setminus \,(M\,\cap \,R)~~=~~(L\,\setminus \,M)\,\cup \,(L\,\setminus \,R)\\[1.4ex]\end{alignedat}}}
$$
 always holds (the equalities on the left and right are De Morgan's laws) but equality is not guaranteed in general (that is, the containment ${\displaystyle {\color {red}{\subseteq }}}$ might be strict). Equality holds if and only if ${\displaystyle L\,\setminus \,(M\,\cap \,R)\;\subseteq \;L\,\setminus \,(M\,\cup \,R),}$ which happens if and only if ${\displaystyle L\,\cap \,M=L\,\cap \,R.}$

This observation about De Morgan's laws shows that ${\displaystyle \,\setminus \,}$ is *not* left distributive over ${\displaystyle \,\cup \,}$ or ${\displaystyle \,\cap \,}$ because only the following are guaranteed in general: 
$$
{\displaystyle {\begin{alignedat}{5}L\,\setminus \,(M\,\cup \,R)~&~~{\color {red}{\subseteq }}~~&&\color {black}{\,}(L\,\setminus \,M)\,\cup \,(L\,\setminus \,R)~~=~~L\,\setminus \,(M\,\cap \,R)\\[1.4ex]\end{alignedat}}}
$$
 
$$
{\displaystyle {\begin{alignedat}{5}L\,\setminus \,(M\,\cap \,R)~&~~{\color {red}{\supseteq }}~~&&\color {black}{\,}(L\,\setminus \,M)\,\cap \,(L\,\setminus \,R)~~=~~L\,\setminus \,(M\,\cup \,R)\\[1.4ex]\end{alignedat}}}
$$
 where equality holds for one (or equivalently, for both) of the above two inclusion formulas if and only if ${\displaystyle L\,\cap \,M=L\,\cap \,R.}$

The following statements are equivalent:

1. ${\displaystyle L\cap M\,=\,L\cap R}$
2. ${\displaystyle L\,\setminus \,M\,=\,L\,\setminus \,R}$
3. ${\displaystyle L\,\setminus \,(M\,\cap \,R)=(L\,\setminus \,M)\,\cap \,(L\,\setminus \,R);}$ that is, ${\displaystyle \,\setminus \,}$ left distributes over ${\displaystyle \,\cap \,}$ for these three particular sets
4. ${\displaystyle L\,\setminus \,(M\,\cup \,R)=(L\,\setminus \,M)\,\cup \,(L\,\setminus \,R);}$ that is, ${\displaystyle \,\setminus \,}$ left distributes over ${\displaystyle \,\cup \,}$ for these three particular sets
5. ${\displaystyle L\,\setminus \,(M\,\cap \,R)\,=\,L\,\setminus \,(M\,\cup \,R)}$
6. ${\displaystyle L\cap (M\cup R)\,=\,L\cap M\cap R}$
7. ${\displaystyle L\cap (M\cup R)~\subseteq ~M\cap R}$
8. ${\displaystyle L\cap R~\subseteq ~M\;}$ and ${\displaystyle \;L\cap M~\subseteq ~R}$
9. ${\displaystyle L\setminus (M\setminus R)\,=\,L\setminus (R\setminus M)}$
10. ${\displaystyle L\setminus (M\setminus R)\,=\,L\setminus (R\setminus M)\,=\,L}$

**[Quasi-commutativity](https://en.wikipedia.org/wiki/Quasi-commutative_property "Quasi-commutative property")**: 
$$
{\displaystyle (L\setminus M)\setminus R~=~(L\setminus R)\setminus M\qquad {\text{ (Quasi-commutative)}}}
$$
 always holds but in general, 
$$
{\displaystyle L\setminus (M\setminus R)~~{\color {red}{\neq }}~~L\setminus (R\setminus M).}
$$
 However, ${\displaystyle L\setminus (M\setminus R)~\subseteq ~L\setminus (R\setminus M)}$ if and only if ${\displaystyle L\cap R~\subseteq ~M}$ if and only if ${\displaystyle L\setminus (R\setminus M)~=~L.}$

**Set subtraction complexity**: To manage the many identities involving set subtraction, this section is divided based on where the set subtraction operation and parentheses are located on the left hand side of the identity. The great variety and (relative) complexity of formulas involving set subtraction (compared to those without it) is in part due to the fact that unlike ${\displaystyle \,\cup ,\,\cap ,}$ and ${\displaystyle \triangle ,\,}$ set subtraction is neither associative nor commutative and it also is not left distributive over ${\displaystyle \,\cup ,\,\cap ,\,\triangle ,}$ or even over itself.

### Two set subtractions

Set subtraction is *not* associative in general: 
$$
{\displaystyle (L\,\setminus \,M)\,\setminus \,R\;~~{\color {red}{\neq }}~~\;L\,\setminus \,(M\,\setminus \,R)}
$$
 since only the following is always guaranteed: 
$$
{\displaystyle (L\,\setminus \,M)\,\setminus \,R\;~~{\color {red}{\subseteq }}~~\;L\,\setminus \,(M\,\setminus \,R).}
$$

#### (L\\M)\\R

$$
{\displaystyle {\begin{alignedat}{4}(L\setminus M)\setminus R&=&&L\setminus (M\cup R)\\[0.6ex]&=(&&L\setminus R)\setminus M\\[0.6ex]&=(&&L\setminus M)\cap (L\setminus R)\\[0.6ex]&=(&&L\setminus R)\setminus M\\[0.6ex]&=(&&L\,\setminus \,R)\,\setminus \,(M\,\setminus \,R)\\[1.4ex]\end{alignedat}}}
$$

#### L\\(M\\R)

$$
{\displaystyle {\begin{alignedat}{4}L\setminus (M\setminus R)&=(L\setminus M)\cup (L\cap R)\\[1.4ex]\end{alignedat}}}
$$

- If ${\displaystyle L\subseteq M{\text{ then }}L\setminus (M\setminus R)=L\cap R}$
- ${\textstyle L\setminus (M\setminus R)\subseteq (L\setminus M)\cup R}$ with equality if and only if ${\displaystyle R\subseteq L.}$

### One set subtraction

#### (L\\M) ⁎ R

**Set subtraction on the *left*, and parentheses on the *left***

$$
{\displaystyle {\begin{alignedat}{4}\left(L\setminus M\right)\cup R&=(L\cup R)\setminus (M\setminus R)\\&=(L\setminus (M\cup R))\cup R~~~~~{\text{ (the outermost union is disjoint) }}\\\end{alignedat}}}
$$

${\displaystyle {\begin{alignedat}{4}(L\setminus M)\cap R&=(&&L\cap R)\setminus (M\cap R)~~~{\text{ (Distributive law of }}\cap {\text{ over }}\setminus {\text{ )}}\\&=(&&L\cap R)\setminus M\\&=&&L\cap (R\setminus M)\\\end{alignedat}}}$ [^14]

$$
{\displaystyle {\begin{alignedat}{5}(L\,\setminus \,M)\,\cap \,(L\,\setminus \,R)~~=~~L\,\setminus \,(M\,\cup \,R)~&~~{\color {red}{\subseteq }}~~&&\color {black}{\,}L\,\setminus \,(M\,\cap \,R)~~=~~(L\,\setminus \,M)\,\cup \,(L\,\setminus \,R)\\[1.4ex]\end{alignedat}}}
$$
 
$$
{\displaystyle {\begin{alignedat}{4}(L\setminus M)~\triangle ~R&=(L\setminus (M\cup R))\cup (R\setminus L)\cup (L\cap M\cap R)~~~{\text{ (the three outermost sets are pairwise disjoint) }}\\\end{alignedat}}}
$$

$$
{\displaystyle (L\,\setminus M)\times R=(L\times R)\,\setminus (M\times R)~~~~~{\text{ (Distributivity)}}}
$$

#### L\\(M ⁎ R)

**Set subtraction on the *left*, and parentheses on the *right***

$$
{\displaystyle {\begin{alignedat}{3}L\setminus (M\cup R)&=(L\setminus M)&&\,\cap \,(&&L\setminus R)~~~~{\text{ (De Morgan's law) }}\\&=(L\setminus M)&&\,\,\setminus &&R\\&=(L\setminus R)&&\,\,\setminus &&M\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{4}L\setminus (M\cap R)&=(L\setminus M)\cup (L\setminus R)~~~~{\text{ (De Morgan's law) }}\\\end{alignedat}}}
$$
 where the above two sets that are the subjects of [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws") always satisfy ${\displaystyle L\,\setminus \,(M\,\cup \,R)~~{\color {red}{\subseteq }}~~\color {black}{\,}L\,\setminus \,(M\,\cap \,R).}$

$$
{\displaystyle {\begin{alignedat}{4}L\setminus (M~\triangle ~R)&=(L\setminus (M\cup R))\cup (L\cap M\cap R)~~~{\text{ (the outermost union is disjoint) }}\\\end{alignedat}}}
$$

#### (L ⁎ M)\\R

**Set subtraction on the *right*, and parentheses on the *left***

$$
{\displaystyle {\begin{alignedat}{4}(L\cup M)\setminus R&=(L\setminus R)\cup (M\setminus R)\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{4}(L\cap M)\setminus R&=(&&L\setminus R)&&\cap (M\setminus R)\\&=&&L&&\cap (M\setminus R)\\&=&&M&&\cap (L\setminus R)\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{4}(L\,\triangle \,M)\setminus R&=(L\setminus R)~&&\triangle ~(M\setminus R)\\&=(L\cup R)~&&\triangle ~(M\cup R)\\\end{alignedat}}}
$$

#### L ⁎ (M\\R)

**Set subtraction on the *right*, and parentheses on the *right***

$$
{\displaystyle {\begin{alignedat}{3}L\cup (M\setminus R)&=&&&&L&&\cup \;&&(M\setminus (R\cup L))&&~~~{\text{ (the outermost union is disjoint) }}\\&=[&&(&&L\setminus M)&&\cup \;&&(R\cap L)]\cup (M\setminus R)&&~~~{\text{ (the outermost union is disjoint) }}\\&=&&(&&L\setminus (M\cup R))\;&&\;\cup &&(R\cap L)\,\,\cup (M\setminus R)&&~~~{\text{ (the three outermost sets are pairwise disjoint) }}\\\end{alignedat}}}
$$

${\displaystyle {\begin{alignedat}{4}L\cap (M\setminus R)&=(&&L\cap M)&&\setminus (L\cap R)~~~{\text{ (Distributive law of }}\cap {\text{ over }}\setminus {\text{ )}}\\&=(&&L\cap M)&&\setminus R\\&=&&M&&\cap (L\setminus R)\\&=(&&L\setminus R)&&\cap (M\setminus R)\\\end{alignedat}}}$ [^14]

$$
{\displaystyle L\times (M\,\setminus R)=(L\times M)\,\setminus (L\times R)~~~~~{\text{ (Distributivity)}}}
$$

### Three operations on three sets

#### (L • M) ⁎ (M • R)

**Operations of the form ${\displaystyle (L\bullet M)\ast (M\bullet R)}$**:

$$
{\displaystyle {\begin{alignedat}{9}(L\cup M)&\,\cup \,&&(&&M\cup R)&&&&\;=\;\;&&L\cup M\cup R\\[1.4ex](L\cup M)&\,\cap \,&&(&&M\cup R)&&&&\;=\;\;&&M\cup (L\cap R)\\[1.4ex](L\cup M)&\,\setminus \,&&(&&M\cup R)&&&&\;=\;\;&&L\,\setminus \,(M\cup R)\\[1.4ex](L\cup M)&\,\triangle \,&&(&&M\cup R)&&&&\;=\;\;&&(L\,\setminus \,(M\cup R))\,\cup \,(R\,\setminus \,(L\cup M))\\[1.4ex]&\,&&\,&&\,&&&&\;=\;\;&&(L\,\triangle \,R)\,\setminus \,M\\[1.4ex](L\cap M)&\,\cup \,&&(&&M\cap R)&&&&\;=\;\;&&M\cap (L\cup R)\\[1.4ex](L\cap M)&\,\cap \,&&(&&M\cap R)&&&&\;=\;\;&&L\cap M\cap R\\[1.4ex](L\cap M)&\,\setminus \,&&(&&M\cap R)&&&&\;=\;\;&&(L\cap M)\,\setminus \,R\\[1.4ex](L\cap M)&\,\triangle \,&&(&&M\cap R)&&&&\;=\;\;&&[(L\,\cap M)\cup (M\,\cap R)]\,\setminus \,(L\,\cap M\,\cap R)\\[1.4ex](L\,\setminus M)&\,\cup \,&&(&&M\,\setminus R)&&&&\;=\;\;&&(L\,\cup M)\,\setminus (M\,\cap \,R)\\[1.4ex](L\,\setminus M)&\,\cap \,&&(&&M\,\setminus R)&&&&\;=\;\;&&\varnothing \\[1.4ex](L\,\setminus M)&\,\setminus \,&&(&&M\,\setminus R)&&&&\;=\;\;&&L\,\setminus M\\[1.4ex](L\,\setminus M)&\,\triangle \,&&(&&M\,\setminus R)&&&&\;=\;\;&&(L\,\setminus M)\cup (M\,\setminus R)\\[1.4ex]&\,&&\,&&\,&&&&\;=\;\;&&(L\,\cup M)\setminus (M\,\cap R)\\[1.4ex](L\,\triangle \,M)&\,\cup \,&&(&&M\,\triangle \,R)&&&&\;=\;\;&&(L\,\cup \,M\,\cup \,R)\,\setminus \,(L\,\cap \,M\,\cap \,R)\\[1.4ex](L\,\triangle \,M)&\,\cap \,&&(&&M\,\triangle \,R)&&&&\;=\;\;&&((L\,\cap \,R)\,\setminus \,M)\,\cup \,(M\,\setminus \,(L\,\cup \,R))\\[1.4ex](L\,\triangle \,M)&\,\setminus \,&&(&&M\,\triangle \,R)&&&&\;=\;\;&&(L\,\setminus \,(M\,\cup \,R))\,\cup \,((M\,\cap \,R)\,\setminus \,L)\\[1.4ex](L\,\triangle \,M)&\,\triangle \,&&(&&M\,\triangle \,R)&&&&\;=\;\;&&L\,\triangle \,R\\[1.7ex]\end{alignedat}}}
$$

#### (L • M) ⁎ (R\\M)

**Operations of the form ${\displaystyle (L\bullet M)\ast (R\,\setminus \,M)}$**:

$$
{\displaystyle {\begin{alignedat}{9}(L\cup M)&\,\cup \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&L\cup M\cup R\\[1.4ex](L\cup M)&\,\cap \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\cap R)\,\setminus \,M\\[1.4ex](L\cup M)&\,\setminus \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&M\cup (L\,\setminus \,R)\\[1.4ex](L\cup M)&\,\triangle \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&M\cup (L\,\triangle \,R)\\[1.4ex](L\cap M)&\,\cup \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&[L\cap (M\cup R)]\cup [R\,\setminus \,(L\cup M)]\qquad {\text{ (disjoint union)}}\\[1.4ex]&\,&&\,&&\,&&&&\;=\;\;&&(L\cap M)\,\triangle \,(R\,\setminus \,M)\\[1.4ex](L\cap M)&\,\cap \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&\varnothing \\[1.4ex](L\cap M)&\,\setminus \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&L\cap M\\[1.4ex](L\cap M)&\,\triangle \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\cap M)\cup (R\,\setminus \,M)\qquad {\text{ (disjoint union)}}\\[1.4ex](L\,\setminus \,M)&\,\cup \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&L\cup R\,\setminus \,M\\[1.4ex](L\,\setminus \,M)&\,\cap \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\cap R)\,\setminus \,M\\[1.4ex](L\,\setminus \,M)&\,\setminus \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&L\,\setminus \,(M\cup R)\\[1.4ex](L\,\setminus \,M)&\,\triangle \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\,\triangle \,R)\,\setminus \,M\\[1.4ex](L\,\triangle \,M)&\,\cup \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\cup M\cup R)\,\setminus \,(L\cap M)\\[1.4ex](L\,\triangle \,M)&\,\cap \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&(L\cap R)\,\setminus \,M\\[1.4ex](L\,\triangle \,M)&\,\setminus \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&[L\,\setminus \,(M\cup R)]\cup (M\,\setminus \,L)\qquad {\text{ (disjoint union)}}\\[1.4ex]&\,&&\,&&\,&&&&\;=\;\;&&(L\,\triangle \,M)\setminus (L\,\cap R)\\[1.4ex](L\,\triangle \,M)&\,\triangle \,&&(&&R\,\setminus \,M)&&&&\;=\;\;&&L\,\triangle \,(M\cup R)\\[1.7ex]\end{alignedat}}}
$$

#### (L\\M) ⁎ (L\\R)

**Operations of the form ${\displaystyle (L\,\setminus \,M)\ast (L\,\setminus \,R)}$**:

$$
{\displaystyle {\begin{alignedat}{9}(L\,\setminus M)&\,\cup \,&&(&&L\,\setminus R)&&\;=\;&&L\,\setminus \,(M\,\cap \,R)\\[1.4ex](L\,\setminus M)&\,\cap \,&&(&&L\,\setminus R)&&\;=\;&&L\,\setminus \,(M\,\cup \,R)\\[1.4ex](L\,\setminus M)&\,\setminus \,&&(&&L\,\setminus R)&&\;=\;&&(L\,\cap \,R)\,\setminus \,M\\[1.4ex](L\,\setminus M)&\,\triangle \,&&(&&L\,\setminus R)&&\;=\;&&L\,\cap \,(M\,\triangle \,R)\\[1.4ex]&\,&&\,&&\,&&\;=\;&&(L\cap M)\,\triangle \,(L\cap R)\\[1.4ex]\end{alignedat}}}
$$

### Other simplifications

**Other properties**:

$$
{\displaystyle L\cap M=R\;{\text{ and }}\;L\cap R=M\qquad {\text{ if and only if }}\qquad M=R\subseteq L.}
$$

- If ${\displaystyle L\subseteq M}$ then ${\displaystyle L\setminus R=L\cap (M\setminus R).}$ [^14]
- ${\displaystyle L\times (M\,\setminus R)=(L\times M)\,\setminus (L\times R)}$
- If ${\displaystyle L\subseteq R}$ then ${\displaystyle M\setminus R\subseteq M\setminus L.}$
- ${\displaystyle L\cap M\cap R=\varnothing }$ if and only if for any ${\displaystyle x\in L\cup M\cup R,}$ ${\displaystyle x}$ belongs to *at most two* of the sets ${\displaystyle L,M,{\text{ and }}R.}$

## Symmetric difference ∆ of finitely many sets

Given finitely many sets ${\displaystyle L_{1},\ldots ,L_{n},}$ something belongs to their [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference "Symmetric difference") if and only if it belongs to an odd number of these sets. Explicitly, for any ${\displaystyle x,}$ ${\displaystyle x\in L_{1}\triangle \cdots \triangle L_{n}}$ if and only if the cardinality ${\displaystyle \left|\left\{i:x\in L_{i}\right\}\right|}$ is odd. (Recall that symmetric difference is associative so parentheses are not needed for the set ${\displaystyle L_{1}\triangle \cdots \triangle L_{n}}$).

Consequently, the symmetric difference of three sets satisfies: 
$$
{\displaystyle {\begin{alignedat}{4}L\,\triangle \,M\,\triangle \,R&=(L\cap M\cap R)\cup \{x:x{\text{ belongs to exactly one of the sets }}L,M,R\}~~~~~~{\text{ (the union is disjoint) }}\\&=[L\cap M\cap R]\cup [L\setminus (M\cup R)]\cup [M\setminus (L\cup R)]\cup [R\setminus (L\cup M)]~~~~~~~~~{\text{ (all 4 sets enclosed by [ ] are pairwise disjoint) }}\\\end{alignedat}}}
$$

## Cartesian products ⨯ of finitely many sets

### Binary ⨯ distributes over ⋃ and ⋂ and \\ and ∆

The binary [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") ⨯ [distributes over](#Distributivity) unions, intersections, set subtraction, and symmetric difference:

$$
{\displaystyle {\begin{alignedat}{9}(L\,\cap \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\cap \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex](L\,\cup \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\cup \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex](L\,\setminus \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\setminus \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\setminus \,{\text{)}}\\[1.4ex](L\,\triangle \,M)\,\times \,R~&~~=~~&&(L\,\times \,R)\,&&\triangle \,&&(M\,\times \,R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex]\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{5}L\times (M\cap R)&\;=\;\;&&(L\times M)\cap (L\times R)\qquad &&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\cap \,{\text{)}}\\[1.4ex]L\times (M\cup R)&\;=\;\;&&(L\times M)\cup (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]L\times (M\setminus R)&\;=\;\;&&(L\times M)\setminus (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\setminus \,{\text{)}}\\[1.4ex]L\times (M\triangle R)&\;=\;\;&&(L\times M)\triangle (L\times R)&&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\triangle \,{\text{)}}\\[1.4ex]\end{alignedat}}}
$$

But in general, ⨯ does not distribute over itself: 
$$
{\displaystyle L\times (M\times R)~\color {Red}{\neq }\color {Black}{}~(L\times M)\times (L\times R)}
$$
 
$$
{\displaystyle (L\times M)\times R~\color {Red}{\neq }\color {Black}{}~(L\times R)\times (M\times R).}
$$

### Binary ⋂ of finite ⨯

$$
{\displaystyle (L\times R)\cap \left(L_{2}\times R_{2}\right)~=~\left(L\cap L_{2}\right)\times \left(R\cap R_{2}\right)}
$$
 
$$
{\displaystyle (L\times M\times R)\cap \left(L_{2}\times M_{2}\times R_{2}\right)~=~\left(L\cap L_{2}\right)\times \left(M\cap M_{2}\right)\times \left(R\cap R_{2}\right)}
$$

### Binary ⋃ of finite ⨯

$$
{\displaystyle {\begin{alignedat}{9}\left(L\times R\right)~\cup ~\left(L_{2}\times R_{2}\right)~&=~\left[\left(L\setminus L_{2}\right)\times R\right]~\cup ~\left[\left(L_{2}\setminus L\right)\times R_{2}\right]~\cup ~\left[\left(L\cap L_{2}\right)\times \left(R\cup R_{2}\right)\right]\\[0.5ex]~&=~\left[L\times \left(R\setminus R_{2}\right)\right]~\cup ~\left[L_{2}\times \left(R_{2}\setminus R\right)\right]~\cup ~\left[\left(L\cup L_{2}\right)\times \left(R\cap R_{2}\right)\right]\\\end{alignedat}}}
$$

### Difference \\ of finite ⨯

$$
{\displaystyle {\begin{alignedat}{9}\left(L\times R\right)~\setminus ~\left(L_{2}\times R_{2}\right)~&=~\left[\left(L\,\setminus \,L_{2}\right)\times R\right]~\cup ~\left[L\times \left(R\,\setminus \,R_{2}\right)\right]\\\end{alignedat}}}
$$
 and 
$$
{\displaystyle (L\times M\times R)~\setminus ~\left(L_{2}\times M_{2}\times R_{2}\right)~=~\left[\left(L\,\setminus \,L_{2}\right)\times M\times R\right]~\cup ~\left[L\times \left(M\,\setminus \,M_{2}\right)\times R\right]~\cup ~\left[L\times M\times \left(R\,\setminus \,R_{2}\right)\right]}
$$

### Finite ⨯ of differences \\

$$
{\displaystyle \left(L\,\setminus \,L_{2}\right)\times \left(R\,\setminus \,R_{2}\right)~=~\left(L\times R\right)\,\setminus \,\left[\left(L_{2}\times R\right)\cup \left(L\times R_{2}\right)\right]}
$$

$$
{\displaystyle \left(L\,\setminus \,L_{2}\right)\times \left(M\,\setminus \,M_{2}\right)\times \left(R\,\setminus \,R_{2}\right)~=~\left(L\times M\times R\right)\,\setminus \,\left[\left(L_{2}\times M\times R\right)\cup \left(L\times M_{2}\times R\right)\cup \left(L\times M\times R_{2}\right)\right]}
$$

### Symmetric difference ∆ and finite ⨯

$$
{\displaystyle L\times \left(R\,\triangle \,R_{2}\right)~=~\left[L\times \left(R\,\setminus \,R_{2}\right)\right]\,\cup \,\left[L\times \left(R_{2}\,\setminus \,R\right)\right]}
$$
 
$$
{\displaystyle \left(L\,\triangle \,L_{2}\right)\times R~=~\left[\left(L\,\setminus \,L_{2}\right)\times R\right]\,\cup \,\left[\left(L_{2}\,\setminus \,L\right)\times R\right]}
$$

$$
{\displaystyle {\begin{alignedat}{4}\left(L\,\triangle \,L_{2}\right)\times \left(R\,\triangle \,R_{2}\right)~&=~&&&&\,\left[\left(L\cup L_{2}\right)\times \left(R\cup R_{2}\right)\right]\;\setminus \;\left[\left(\left(L\cap L_{2}\right)\times R\right)\;\cup \;\left(L\times \left(R\cap R_{2}\right)\right)\right]\\[0.7ex]&=~&&&&\,\left[\left(L\,\setminus \,L_{2}\right)\times \left(R_{2}\,\setminus \,R\right)\right]\,\cup \,\left[\left(L_{2}\,\setminus \,L\right)\times \left(R_{2}\,\setminus \,R\right)\right]\,\cup \,\left[\left(L\,\setminus \,L_{2}\right)\times \left(R\,\setminus \,R_{2}\right)\right]\,\cup \,\left[\left(L_{2}\,\setminus \,L\right)\cup \left(R\,\setminus \,R_{2}\right)\right]\\\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{4}\left(L\,\triangle \,L_{2}\right)\times \left(M\,\triangle \,M_{2}\right)\times \left(R\,\triangle \,R_{2}\right)~&=~\left[\left(L\cup L_{2}\right)\times \left(M\cup M_{2}\right)\times \left(R\cup R_{2}\right)\right]\;\setminus \;\left[\left(\left(L\cap L_{2}\right)\times M\times R\right)\;\cup \;\left(L\times \left(M\cap M_{2}\right)\times R\right)\;\cup \;\left(L\times M\times \left(R\cap R_{2}\right)\right)\right]\\\end{alignedat}}}
$$

In general, ${\displaystyle \left(L\,\triangle \,L_{2}\right)\times \left(R\,\triangle \,R_{2}\right)}$ need not be a subset nor a superset of ${\displaystyle \left(L\times R\right)\,\triangle \,\left(L_{2}\times R_{2}\right).}$

$$
{\displaystyle {\begin{alignedat}{4}\left(L\times R\right)\,\triangle \,\left(L_{2}\times R_{2}\right)~&=~&&\left(L\times R\right)\cup \left(L_{2}\times R_{2}\right)\;\setminus \;\left[\left(L\cap L_{2}\right)\times \left(R\cap R_{2}\right)\right]\\[0.7ex]\end{alignedat}}}
$$

$$
{\displaystyle {\begin{alignedat}{4}\left(L\times M\times R\right)\,\triangle \,\left(L_{2}\times M_{2}\times R_{2}\right)~&=~&&\left(L\times M\times R\right)\cup \left(L_{2}\times M_{2}\times R_{2}\right)\;\setminus \;\left[\left(L\cap L_{2}\right)\times \left(M\cap M_{2}\right)\times \left(R\cap R_{2}\right)\right]\\[0.7ex]\end{alignedat}}}
$$

## Arbitrary families of sets

Let ${\displaystyle \left(L_{i}\right)_{i\in I},}$ ${\displaystyle \left(R_{j}\right)_{j\in J},}$ and ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J}}$ be indexed [families of sets](https://en.wikipedia.org/wiki/Family_of_sets "Family of sets"). Whenever the assumption is needed, then all [indexing sets](https://en.wikipedia.org/wiki/Indexing_set "Indexing set"), such as ${\displaystyle I}$ and ${\displaystyle J,}$ are assumed to be non-empty.

### Definitions

A *[family of sets](https://en.wikipedia.org/wiki/Family_of_sets "Family of sets")* or (more briefly) a *family* refers to a set whose elements are sets.

An *[indexed family](https://en.wikipedia.org/wiki/Indexed_family "Indexed family") of sets* is a function from some set, called its *[indexing set](https://en.wikipedia.org/wiki/Indexing_set "Indexing set")*, into some family of sets. An indexed family of sets will be denoted by ${\displaystyle \left(L_{i}\right)_{i\in I},}$ where this notation assigns the symbol ${\displaystyle I}$ for the indexing set and for every index ${\displaystyle i\in I,}$ assigns the symbol ${\displaystyle L_{i}}$ to the value of the function at ${\displaystyle i.}$ The function itself may then be denoted by the symbol ${\displaystyle L_{\bullet },}$ which is obtained from the notation ${\displaystyle \left(L_{i}\right)_{i\in I}}$ by replacing the index ${\displaystyle i}$ with a bullet symbol ${\displaystyle \bullet \,;}$ explicitly, ${\displaystyle L_{\bullet }}$ is the function: 
$$
{\displaystyle {\begin{alignedat}{4}L_{\bullet }:\;&&I&&\;\to \;&\left\{L_{i}:i\in I\right\}\\[0.3ex]&&i&&\;\mapsto \;&L_{i}\\\end{alignedat}}}
$$
 which may be summarized by writing ${\displaystyle L_{\bullet }=\left(L_{i}\right)_{i\in I}.}$

Any given indexed family of sets ${\displaystyle L_{\bullet }=\left(L_{i}\right)_{i\in I}}$ (which is a [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)")) can be canonically associated with its image/range ${\displaystyle \operatorname {Im} L_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\left\{L_{i}:i\in I\right\}}$ (which is a family of sets). Conversely, any given family of sets ${\displaystyle {\mathcal {B}}}$ may be associated with the ${\displaystyle {\mathcal {B}}}$ -indexed family of sets ${\displaystyle (B)_{B\in {\mathcal {B}}},}$ which is technically the [identity map](https://en.wikipedia.org/wiki/Identity_map "Identity map") ${\displaystyle {\mathcal {B}}\to {\mathcal {B}}.}$ However, this is *not* a bijective correspondence because an indexed family of sets ${\displaystyle L_{\bullet }=\left(L_{i}\right)_{i\in I}}$ is *not* required to be injective (that is, there may exist distinct indices ${\displaystyle i\neq j}$ such as ${\displaystyle L_{i}=L_{j}}$), which in particular means that it is possible for distinct indexed families of sets (which are functions) to be associated with the same family of sets (by having the same image/range).

**Arbitrary unions defined** [^13]

| $$ {\displaystyle \bigcup _{i\in I}L_{i}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{x~:~{\text{ there exists }}i\in I{\text{ such that }}x\in L_{i}\}} $$ |  | Def. 1 |
| --- | --- | --- |

If ${\displaystyle I=\varnothing }$ then ${\displaystyle \bigcup _{i\in \varnothing }L_{i}=\{x~:~{\text{ there exists }}i\in \varnothing {\text{ such that }}x\in L_{i}\}=\varnothing ,}$ which is somethings called the *nullary union convention* (despite being called a convention, this equality follows from the definition).

If ${\displaystyle {\mathcal {B}}}$ is a family of sets then ${\displaystyle \cup {\mathcal {B}}}$ denotes the set: 
$$
{\displaystyle \bigcup {\mathcal {B}}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcup _{B\in {\mathcal {B}}}B~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{x~:~{\text{ there exists }}B\in {\mathcal {B}}{\text{ such that }}x\in B\}.}
$$

**Arbitrary intersections defined**

If ${\displaystyle I\neq \varnothing }$ then [^13]

| $$ {\displaystyle \bigcap _{i\in I}L_{i}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{x~:~x\in L_{i}{\text{ for every }}i\in I\}~=~\{x~:~{\text{ for all }}i,{\text{ if }}i\in I{\text{ then }}x\in L_{i}\}.} $$ |  | Def. 2 |
| --- | --- | --- |

If ${\displaystyle {\mathcal {B}}\neq \varnothing }$ is a *non-empty* family of sets then ${\displaystyle \cap {\mathcal {B}}}$ denotes the set: 
$$
{\displaystyle \bigcap {\mathcal {B}}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcap _{B\in B}B~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{x~:~x\in B{\text{ for every }}B\in {\mathcal {B}}\}~=~\{x~:~{\text{ for all }}B,{\text{ if }}B\in {\mathcal {B}}{\text{ then }}x\in B\}.}
$$

**Nullary intersections**

If ${\displaystyle I=\varnothing }$ then 
$$
{\displaystyle \bigcap _{i\in \varnothing }L_{i}=\{x~:~{\text{ for all }}i,{\text{ if }}i\in \varnothing {\text{ then }}x\in L_{i}\}}
$$
 where every possible thing ${\displaystyle x}$ in the universe [vacuously](https://en.wikipedia.org/wiki/Vacuous_truth "Vacuous truth") satisfied the condition: "if ${\displaystyle i\in \varnothing }$ then ${\displaystyle x\in L_{i}}$ ". Consequently, ${\displaystyle {\textstyle \bigcap \limits _{i\in \varnothing }}L_{i}=\{x:{\text{ true }}\}}$ consists of *everything* in the universe.

So if ${\displaystyle I=\varnothing }$ and:

1. if you are working in a [model](https://en.wikipedia.org/wiki/Model_theory "Model theory") in which there exists some [universe ***set***](https://en.wikipedia.org/wiki/Universe_set "Universe set") ${\displaystyle X}$ then ${\displaystyle {\textstyle \bigcap \limits _{i\in \varnothing }}L_{i}=\{x~:~x\in L_{i}{\text{ for every }}i\in \varnothing \}~=~X.}$
2. otherwise, if you are working in a [model](https://en.wikipedia.org/wiki/Model_theory "Model theory") in which "the class of all things ${\displaystyle x}$ " is not a set (by far the most common situation) then ${\displaystyle {\textstyle \bigcap \limits _{i\in \varnothing }}L_{i}}$ is *undefined* because ${\displaystyle {\textstyle \bigcap \limits _{i\in \varnothing }}L_{i}}$ consists of *everything*, which makes ${\displaystyle {\textstyle \bigcap \limits _{i\in \varnothing }}L_{i}}$ a [proper class](https://en.wikipedia.org/wiki/Proper_class "Proper class") and *not* a set.

**Assumption**: Henceforth, whenever a formula requires some indexing set to be non-empty in order for an arbitrary intersection to be well-defined, then this will automatically be assumed without mention.

A consequence of this is the following assumption/definition:

A ***finite intersection* of sets** or an ***intersection of finitely many sets*** refers to the intersection of a finite collection of *one or more* sets.

Some authors adopt the so called ***[nullary intersection](https://en.wikipedia.org/wiki/Nullary_intersection "Nullary intersection") convention***, which is the convention that an empty intersection of sets is equal to some canonical set. In particular, if all sets are subsets of some set ${\displaystyle X}$ then some author may declare that the empty intersection of these sets be equal to ${\displaystyle X.}$ However, the nullary intersection convention is not as commonly accepted as the nullary union convention and this article will not adopt it (this is due to the fact that unlike the empty union, the value of the empty intersection depends on ${\displaystyle X}$ so if there are multiple sets under consideration, which is commonly the case, then the value of the empty intersection risks becoming ambiguous).

**Multiple index sets** 
$$
{\displaystyle \bigcup _{\stackrel {i\in I,}{j\in J}}S_{i,j}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcup _{(i,j)\in I\times J}S_{i,j}}
$$
 
$$
{\displaystyle \bigcap _{\stackrel {i\in I,}{j\in J}}S_{i,j}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcap _{(i,j)\in I\times J}S_{i,j}}
$$

### Distributing unions and intersections

#### Binary ⋂ of arbitrary ⋃'s

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\cap R~=~\bigcup _{i\in I}\left(L_{i}\cap R\right)} $$ |  | Eq. 3a |
| --- | --- | --- |

and [^14]

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\cap \left(\bigcup _{j\in J}R_{j}\right)~=~\bigcup _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\cap R_{j}\right)} $$ |  | Eq. 3b |
| --- | --- | --- |

- If all ${\displaystyle \left(L_{i}\right)_{i\in I}}$ are [pairwise disjoint](https://en.wikipedia.org/wiki/Pairwise_disjoint "Pairwise disjoint") and all ${\displaystyle \left(R_{j}\right)_{j\in J}}$ are also pairwise disjoint, then so are all ${\displaystyle \left(L_{i}\cap R_{j}\right)_{(i,j)\in I\times J}}$ (that is, if ${\displaystyle (i,j)\neq \left(i_{2},j_{2}\right)}$ then ${\displaystyle \left(L_{i}\cap R_{j}\right)\cap \left(L_{i_{2}}\cap R_{j_{2}}\right)=\varnothing }$).
- **Importantly**, if ${\displaystyle I=J}$ then in general, 
	$$
	{\displaystyle ~\left(\bigcup _{i\in I}L_{i}\right)\cap \left(\bigcup _{i\in I}R_{i}\right)~~\color {Red}{\neq }\color {Black}{}~~\bigcup _{i\in I}\left(L_{i}\cap R_{i}\right)~}
	$$
	 (an [example of this](#CounterExampleToEqualityInterOfUnionsWhenIequalsJ) is given below). The single union on the right hand side *must* be over all pairs ${\displaystyle (i,j)\in I\times I:}$ 
	$$
	{\displaystyle ~\left(\bigcup _{i\in I}L_{i}\right)\cap \left(\bigcup _{i\in I}R_{i}\right)~~=~~\bigcup _{\stackrel {i\in I,}{j\in I}}\left(L_{i}\cap R_{j}\right).~}
	$$
	 The same is usually true for other similar non-trivial set equalities and relations that depend on two (potentially unrelated) indexing sets ${\displaystyle I}$ and ${\displaystyle J}$ (such as **[Eq. 4b](#math_Eq._4b)** or **[Eq. 7g](#math_Eq._7g)** [^14]). Two exceptions are **[Eq. 2c](#math_Eq._2c)** (unions of unions) and **[Eq. 2d](#math_Eq._2d)** (intersections of intersections), but both of these are among the most trivial of set equalities (although even for these equalities there is still something that must be proven [^2]).
- **Example where equality fails**: Let ${\displaystyle X\neq \varnothing }$ and let ${\displaystyle I=\{1,2\}.}$ Let ${\displaystyle L_{1}\colon =R_{2}\colon =X}$ and let ${\displaystyle L_{2}\colon =R_{1}\colon =\varnothing .}$ Then 
	$$
	{\displaystyle X=X\cap X=\left(L_{1}\cup L_{2}\right)\cap \left(R_{2}\cup R_{2}\right)=\left(\bigcup _{i\in I}L_{i}\right)\cap \left(\bigcup _{i\in I}R_{i}\right)~\neq ~\bigcup _{i\in I}\left(L_{i}\cap R_{i}\right)=\left(L_{1}\cap R_{1}\right)\cup \left(L_{2}\cap R_{2}\right)=\varnothing \cup \varnothing =\varnothing .}
	$$
	 Furthermore, 
	$$
	{\displaystyle \varnothing =\varnothing \cup \varnothing =\left(L_{1}\cap L_{2}\right)\cup \left(R_{2}\cap R_{2}\right)=\left(\bigcap _{i\in I}L_{i}\right)\cup \left(\bigcap _{i\in I}R_{i}\right)~\neq ~\bigcap _{i\in I}\left(L_{i}\cup R_{i}\right)=\left(L_{1}\cup R_{1}\right)\cap \left(L_{2}\cup R_{2}\right)=X\cap X=X.}
	$$

#### Binary ⋃ of arbitrary ⋂'s

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\cup R~=~\bigcap _{i\in I}\left(L_{i}\cup R\right)} $$ |  | Eq. 4a |
| --- | --- | --- |

and [^14]

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\cup \left(\bigcap _{j\in J}R_{j}\right)~=~\bigcap _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\cup R_{j}\right)} $$ |  | Eq. 4b |
| --- | --- | --- |

- **Importantly**, if ${\displaystyle I=J}$ then in general, 
	$$
	{\displaystyle ~\left(\bigcap _{i\in I}L_{i}\right)\cup \left(\bigcap _{i\in I}R_{i}\right)~~\color {Red}{\neq }\color {Black}{}~~\bigcap _{i\in I}\left(L_{i}\cup R_{i}\right)~}
	$$
	 (an [example of this](#CounterExampleToEqualityUnionOfIntersWhenIequalsJ) is given above). The single intersection on the right hand side *must* be over all pairs ${\displaystyle (i,j)\in I\times I:}$ 
	$$
	{\displaystyle ~\left(\bigcap _{i\in I}L_{i}\right)\cup \left(\bigcap _{i\in I}R_{i}\right)~~=~~\bigcap _{\stackrel {i\in I,}{j\in I}}\left(L_{i}\cup R_{j}\right).~}
	$$

#### Arbitrary ⋂'s and arbitrary ⋃'s

##### Incorrectly distributing by swapping ⋂ and ⋃

**Naively swapping ${\displaystyle \;{\textstyle \bigcup \limits _{i\in I}}\;}$ and ${\displaystyle \;{\textstyle \bigcap \limits _{j\in J}}\;}$ may produce a different set**

The following inclusion always holds:

<table><tbody><tr><td><math>{\displaystyle \bigcup _{i\in I}\left(\bigcap _{j\in J}S_{i,j}\right)~~\color {Red}{\subseteq }\color {Black}{}~~\bigcap _{j\in J}\left(\bigcup _{i\in I}S_{i,j}\right)}</math></td><td><table><tbody><tr><td rowspan="2"></td><td></td><td rowspan="2"></td></tr><tr><td></td></tr></tbody></table></td><td>Inclusion 1 ∪∩ is a subset of ∩∪</td></tr></tbody></table>

In general, equality need not hold and moreover, the right hand side depends on how for each fixed ${\displaystyle i\in I,}$ the sets ${\displaystyle \left(S_{i,j}\right)_{j\in J}}$ are labelled; and analogously, the left hand side depends on how for each fixed ${\displaystyle j\in J,}$ the sets ${\displaystyle \left(S_{i,j}\right)_{i\in I}}$ are labelled. An example demonstrating this is now given.

- **Example of dependence on labeling and failure of equality**: To see why equality need not hold when ${\displaystyle \cup }$ and ${\displaystyle \cap }$ are swapped, let ${\displaystyle I\colon =J\colon =\{1,2\},}$ and let ${\displaystyle S_{11}=\{1,2\},~S_{12}=\{1,3\},~S_{21}=\{3,4\},}$ and ${\displaystyle S_{22}=\{2,4\}.}$ Then 
	$$
	{\displaystyle \{1,4\}=\{1\}\cup \{4\}=\left(S_{11}\cap S_{12}\right)\cup \left(S_{21}\cap S_{22}\right)=\bigcup _{i\in I}\left(\bigcap _{j\in J}S_{i,j}\right)~\neq ~\bigcap _{j\in J}\left(\bigcup _{i\in I}S_{i,j}\right)=\left(S_{11}\cup S_{21}\right)\cap \left(S_{12}\cup S_{22}\right)=\{1,2,3,4\}.}
	$$
	 If ${\displaystyle S_{11}}$ and ${\displaystyle S_{21}}$ are swapped while ${\displaystyle S_{12}}$ and ${\displaystyle S_{22}}$ are unchanged, which gives rise to the sets ${\displaystyle {\hat {S}}_{11}\colon =\{3,4\},~{\hat {S}}_{12}\colon =\{1,3\},~{\hat {S}}_{21}\colon =\{1,2\},}$ and ${\displaystyle {\hat {S}}_{22}\colon =\{2,4\},}$ then 
	$$
	{\displaystyle \{2,3\}=\{3\}\cup \{2\}=\left({\hat {S}}_{11}\cap {\hat {S}}_{12}\right)\cup \left({\hat {S}}_{21}\cap {\hat {S}}_{22}\right)=\bigcup _{i\in I}\left(\bigcap _{j\in J}{\hat {S}}_{i,j}\right)~\neq ~\bigcap _{j\in J}\left(\bigcup _{i\in I}{\hat {S}}_{i,j}\right)=\left({\hat {S}}_{11}\cup {\hat {S}}_{21}\right)\cap \left({\hat {S}}_{12}\cup {\hat {S}}_{22}\right)=\{1,2,3,4\}.}
	$$
	 In particular, the left hand side is no longer ${\displaystyle \{1,4\},}$ which shows that the left hand side ${\displaystyle {\textstyle \bigcup \limits _{i\in I}}\;{\textstyle \bigcap \limits _{j\in J}}S_{i,j}}$ depends on how the sets are labelled. If instead ${\displaystyle S_{11}}$ and ${\displaystyle S_{12}}$ are swapped while ${\displaystyle S_{21}}$ and ${\displaystyle S_{22}}$ are unchanged, which gives rise to the sets ${\displaystyle {\overline {S}}_{11}\colon =\{1,3\},~{\overline {S}}_{12}\colon =\{1,2\},~{\overline {S}}_{21}\colon =\{3,4\},}$ and ${\displaystyle {\overline {S}}_{22}\colon =\{2,4\},}$ then both the left hand side and right hand side are equal to ${\displaystyle \{1,4\},}$ which shows that the right hand side also depends on how the sets are labeled.

Equality in **[Inclusion 1 ∪∩ is a subset of ∩∪](#math_In._1)** can hold under certain circumstances, such as in **[7e](#math_Eq._7e)**, which is the special case where ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J}}$ is ${\displaystyle \left(L_{i}\setminus R_{j}\right)_{(i,j)\in I\times J}}$ (that is, ${\displaystyle S_{i,j}\colon =L_{i}\setminus R_{j}}$ with the same indexing sets ${\displaystyle I}$ and ${\displaystyle J}$), or such as in **[7f](#math_Eq._7f)**, which is the special case where ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J}}$ is ${\displaystyle \left(L_{i}\setminus R_{j}\right)_{(j,i)\in J\times I}}$ (that is, ${\displaystyle {\hat {S}}_{j,i}\colon =L_{i}\setminus R_{j}}$ with the indexing sets ${\displaystyle I}$ and ${\displaystyle J}$ swapped). For a correct formula that extends the distributive laws, an approach other than just switching ${\displaystyle \cup }$ and ${\displaystyle \cap }$ is needed.

##### Correct distributive laws

Suppose that for each ${\displaystyle i\in I,}$ ${\displaystyle J_{i}}$ is a non-empty index set and for each ${\displaystyle j\in J_{i},}$ let ${\displaystyle T_{i,j}}$ be any set (for example, to apply this law to ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J},}$ use ${\displaystyle J_{i}\colon =J}$ for all ${\displaystyle i\in I}$ and use ${\displaystyle T_{i,j}\colon =S_{i,j}}$ for all ${\displaystyle i\in I}$ and all ${\displaystyle j\in J_{i}=J}$). Let 
$$
{\displaystyle {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\prod _{i\in I}J_{i}}
$$
 denote the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product"), which can be interpreted as the set of all functions ${\displaystyle f~:~I~\to ~{\textstyle \bigcup \limits _{i\in I}}J_{i}}$ such that ${\displaystyle f(i)\in J_{i}}$ for every ${\displaystyle i\in I.}$ Such a function may also be denoted using the [tuple](https://en.wikipedia.org/wiki/Tuple "Tuple") notation ${\displaystyle \left(f_{i}\right)_{i\in I}}$ where ${\displaystyle f_{i}~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~f(i)}$ for every ${\displaystyle i\in I}$ and conversely, a tuple ${\displaystyle \left(f_{i}\right)_{i\in I}}$ is just notation for the function with domain ${\displaystyle I}$ whose value at ${\displaystyle i\in I}$ is ${\displaystyle f_{i};}$ both notations can be used to denote the elements of ${\displaystyle {\textstyle \prod }J_{\bullet }.}$ Then

<table><tbody><tr><td><math>{\displaystyle \bigcap _{i\in I}\left[\;\bigcup _{j\in J_{i}}T_{i,j}\right]=\bigcup _{f\in \prod J_{\bullet }}\left[\;\bigcap _{i\in I}T_{i,f(i)}\right]}</math></td><td><table><tbody><tr><td rowspan="2"></td><td></td><td rowspan="2"></td></tr><tr><td></td></tr></tbody></table></td><td>Eq. 5 ∩∪ to ∪∩</td></tr></tbody></table>

<table><tbody><tr><td><math>{\displaystyle \bigcup _{i\in I}\left[\;\bigcap _{j\in J_{i}}T_{i,j}\right]=\bigcap _{f\in \prod J_{\bullet }}\left[\;\bigcup _{i\in I}T_{i,f(i)}\right]}</math></td><td><table><tbody><tr><td rowspan="2"></td><td></td><td rowspan="2"></td></tr><tr><td></td></tr></tbody></table></td><td>Eq. 6 ∪∩ to ∩∪</td></tr></tbody></table>

where ${\displaystyle {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~{\textstyle \prod \limits _{i\in I}}J_{i}.}$

##### Applying the distributive laws

***Example application***: In the particular case where all ${\displaystyle J_{i}}$ are equal (that is, ${\displaystyle J_{i}=J_{i_{2}}}$ for all ${\displaystyle i,i_{2}\in I,}$ which is the case with the family ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J},}$ for example), then letting ${\displaystyle J}$ denote this common set, the Cartesian product will be ${\displaystyle {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~{\textstyle \prod \limits _{i\in I}}J_{i}={\textstyle \prod \limits _{i\in I}}J=J^{I},}$ which is the [set of all functions](https://en.wikipedia.org/wiki/Function_space "Function space") of the form ${\displaystyle f~:~I~\to ~J.}$ The above set equalities **[Eq. 5 ∩∪ to ∪∩](#math_5)** and **[Eq. 6 ∪∩ to ∩∪](#math_6)**, respectively become:[^13] 
$$
{\displaystyle \bigcap _{i\in I}\;\bigcup _{j\in J}S_{i,j}=\bigcup _{f\in J^{I}}\;\bigcap _{i\in I}S_{i,f(i)}}
$$
 
$$
{\displaystyle \bigcup _{i\in I}\;\bigcap _{j\in J}S_{i,j}=\bigcap _{f\in J^{I}}\;\bigcup _{i\in I}S_{i,f(i)}}
$$

which when combined with **[Inclusion 1 ∪∩ is a subset of ∩∪](#math_In._1)** implies: 
$$
{\displaystyle \bigcup _{i\in I}\;\bigcap _{j\in J}S_{i,j}~=~\bigcap _{f\in J^{I}}\;\bigcup _{i\in I}S_{i,f(i)}~~\color {Red}{\subseteq }\color {Black}{}~~\bigcup _{g\in I^{J}}\;\bigcap _{j\in J}S_{g(j),j}~=~\bigcap _{j\in J}\;\bigcup _{i\in I}S_{i,j}}
$$
 where

- on the left hand side, the indices ${\displaystyle f{\text{ and }}i}$ range over ${\displaystyle f\in J^{I}{\text{ and }}i\in I}$ (so the subscripts of ${\displaystyle S_{i,f(i)}}$ range over ${\displaystyle i\in I{\text{ and }}f(i)\in f(I)\subseteq J}$)
- on the right hand side, the indices ${\displaystyle g{\text{ and }}j}$ range over ${\displaystyle g\in I^{J}{\text{ and }}j\in J}$ (so the subscripts of ${\displaystyle S_{g(j),j}}$ range over ${\displaystyle j\in J{\text{ and }}g(j)\in g(J)\subseteq I}$).

  
***Example application***: To apply the general formula to the case of ${\displaystyle \left(C_{k}\right)_{k\in K}}$ and ${\displaystyle \left(D_{l}\right)_{l\in L},}$ use ${\displaystyle I\colon =\{1,2\},}$ ${\displaystyle J_{1}\colon =K,}$ ${\displaystyle J_{2}\colon =L,}$ and let ${\displaystyle T_{1,k}\colon =C_{k}}$ for all ${\displaystyle k\in J_{1}}$ and let ${\displaystyle T_{2,l}\colon =D_{l}}$ for all ${\displaystyle l\in J_{2}.}$ Every map ${\displaystyle f\in {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~{\textstyle \prod \limits _{i\in I}}J_{i}=J_{1}\times J_{2}=K\times L}$ can be [bijectively](https://en.wikipedia.org/wiki/Bijection "Bijection") identified with the pair ${\displaystyle \left(f(1),f(2)\right)\in K\times L}$ (the inverse sends ${\displaystyle (k,l)\in K\times L}$ to the map ${\displaystyle f_{(k,l)}\in {\textstyle \prod }J_{\bullet }}$ defined by ${\displaystyle 1\mapsto k}$ and ${\displaystyle 2\mapsto l;}$ this is technically just a change of notation). Recall that **[Eq. 5 ∩∪ to ∪∩](#math_5)** was 
$$
{\displaystyle ~\bigcap _{i\in I}\;\bigcup _{j\in J_{i}}T_{i,j}=\bigcup _{f\in {\textstyle \prod }J_{\bullet }}\;\bigcap _{i\in I}T_{i,f(i)}.~}
$$
 Expanding and simplifying the left hand side gives 
$$
{\displaystyle \bigcap _{i\in I}\;\bigcup _{j\in J_{i}}T_{i,j}=\left(\bigcup _{j\in J_{1}}T_{1,j}\right)\cap \left(\;\bigcup _{j\in J_{2}}T_{2,j}\right)=\left(\bigcup _{k\in K}T_{1,k}\right)\cap \left(\;\bigcup _{l\in L}T_{2,l}\right)=\left(\bigcup _{k\in K}C_{k}\right)\cap \left(\;\bigcup _{l\in L}D_{l}\right)}
$$
 and doing the same to the right hand side gives: 
$$
{\displaystyle \bigcup _{f\in \prod J_{\bullet }}\;\bigcap _{i\in I}T_{i,f(i)}=\bigcup _{f\in \prod J_{\bullet }}\left(T_{1,f(1)}\cap T_{2,f(2)}\right)=\bigcup _{f\in \prod J_{\bullet }}\left(C_{f(1)}\cap D_{f(2)}\right)=\bigcup _{(k,l)\in K\times L}\left(C_{k}\cap D_{l}\right)=\bigcup _{\stackrel {k\in K,}{l\in L}}\left(C_{k}\cap D_{l}\right).}
$$

Thus the general identity **[Eq. 5 ∩∪ to ∪∩](#math_5)** reduces down to the previously given set equality **[Eq. 3b](#math_Eq._3b)**: 
$$
{\displaystyle \left(\bigcup _{k\in K}C_{k}\right)\cap \;\bigcup _{l\in L}D_{l}=\bigcup _{\stackrel {k\in K,}{l\in L}}\left(C_{k}\cap D_{l}\right).}
$$

### Distributing subtraction over ⋃ and ⋂

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\;\setminus \;R~=~\bigcup _{i\in I}\left(L_{i}\;\setminus \;R\right)} $$ |  | Eq. 7a |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\;\setminus \;R~=~\bigcap _{i\in I}\left(L_{i}\;\setminus \;R\right)} $$ |  | Eq. 7b |
| --- | --- | --- |

The next identities are known as [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws").[^14]

| $$ {\displaystyle L\;\setminus \;\bigcup _{j\in J}R_{j}~=~\bigcap _{j\in J}\left(L\;\setminus \;R_{j}\right)~~\;~~{\text{ De Morgan's law }}} $$ |  | Eq. 7c |
| --- | --- | --- |

| $$ {\displaystyle L\;\setminus \;\bigcap _{j\in J}R_{j}~=~\bigcup _{j\in J}\left(L\;\setminus \;R_{j}\right)~~\;~~{\text{ De Morgan's law }}} $$ |  | Eq. 7d |
| --- | --- | --- |

The following four set equalities can be deduced from the equalities **[7a](#math_Eq._7a)** - **[7d](#math_Eq._7d)** above.

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\;\setminus \;\bigcup _{j\in J}R_{j}~=~\bigcup _{i\in I}\left(\bigcap _{j\in J}\left(L_{i}\;\setminus \;R_{j}\right)\right)~=~\bigcap _{j\in J}\left(\bigcup _{i\in I}\left(L_{i}\;\setminus \;R_{j}\right)\right)} $$ |  | Eq. 7e |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\;\setminus \;\bigcap _{j\in J}R_{j}~=~\bigcup _{j\in J}\left(\bigcap _{i\in I}\left(L_{i}\;\setminus \;R_{j}\right)\right)~=~\bigcap _{i\in I}\left(\bigcup _{j\in J}\left(L_{i}\;\setminus \;R_{j}\right)\right)} $$ |  | Eq. 7f |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\;\setminus \;\bigcap _{j\in J}R_{j}~=~\bigcup _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\;\setminus \;R_{j}\right)} $$ |  | Eq. 7g |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\;\setminus \;\bigcup _{j\in J}R_{j}~=~\bigcap _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\;\setminus \;R_{j}\right)} $$ |  | Eq. 7h |
| --- | --- | --- |

In general, naively swapping ${\displaystyle \;\cup \;}$ and ${\displaystyle \;\cap \;}$ may produce a different set (see [this note](#Arbitrary_unions/intersections_and_switching_symbols) for more details). The equalities 
$$
{\displaystyle \bigcup _{i\in I}\;\bigcap _{j\in J}\left(L_{i}\setminus R_{j}\right)~=~\bigcap _{j\in J}\;\bigcup _{i\in I}\left(L_{i}\setminus R_{j}\right)\quad {\text{ and }}\quad \bigcup _{j\in J}\;\bigcap _{i\in I}\left(L_{i}\setminus R_{j}\right)~=~\bigcap _{i\in I}\;\bigcup _{j\in J}\left(L_{i}\setminus R_{j}\right)}
$$
 found in **[Eq. 7e](#math_Eq._7e)** and **[Eq. 7f](#math_Eq._7f)** are thus unusual in that they state exactly that swapping ${\displaystyle \;\cup \;}$ and ${\displaystyle \;\cap \;}$ will *not* change the resulting set.

### Commutativity and associativity of ⋃ and ⋂

**Commutativity**:[^13]

$$
{\displaystyle \bigcup _{\stackrel {i\in I,}{j\in J}}S_{i,j}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcup _{(i,j)\in I\times J}S_{i,j}~=~\bigcup _{i\in I}\left(\bigcup _{j\in J}S_{i,j}\right)~=~\bigcup _{j\in J}\left(\bigcup _{i\in I}S_{i,j}\right)}
$$

$$
{\displaystyle \bigcap _{\stackrel {i\in I,}{j\in J}}S_{i,j}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\bigcap _{(i,j)\in I\times J}S_{i,j}~=~\bigcap _{i\in I}\left(\bigcap _{j\in J}S_{i,j}\right)~=~\bigcap _{j\in J}\left(\bigcap _{i\in I}S_{i,j}\right)}
$$

**Unions of unions and intersections of intersections**:[^13]

$$
{\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\cup R~=~\bigcup _{i\in I}\left(L_{i}\cup R\right)}
$$
 
$$
{\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\cap R~=~\bigcap _{i\in I}\left(L_{i}\cap R\right)}
$$
 and [^13]

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\cup \left(\bigcup _{j\in J}R_{j}\right)~=~\bigcup _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\cup R_{j}\right)} $$ |  | Eq. 2a |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\cap \left(\bigcap _{j\in J}R_{j}\right)~=~\bigcap _{\stackrel {i\in I,}{j\in J}}\left(L_{i}\cap R_{j}\right)} $$ |  | Eq. 2b |
| --- | --- | --- |

and if ${\displaystyle I=J}$ then also:[^2] [^13]

| $$ {\displaystyle \left(\bigcup _{i\in I}L_{i}\right)\cup \left(\bigcup _{i\in I}R_{i}\right)~=~\bigcup _{i\in I}\left(L_{i}\cup R_{i}\right)} $$ |  | Eq. 2c |
| --- | --- | --- |

| $$ {\displaystyle \left(\bigcap _{i\in I}L_{i}\right)\cap \left(\bigcap _{i\in I}R_{i}\right)~=~\bigcap _{i\in I}\left(L_{i}\cap R_{i}\right)} $$ |  | Eq. 2d |
| --- | --- | --- |

### Cartesian products Π of arbitrarily many sets

#### Intersections ⋂ of Π

If ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J}}$ is a family of sets then

| $$ {\displaystyle \bigcap _{j\in J}\;\prod _{i\in I}S_{i,j}~~=~~\prod _{i\in I}\;\bigcap _{j\in J}S_{i,j}} $$ |  | Eq. 8 |
| --- | --- | --- |

- Moreover, a tuple ${\displaystyle \left(x_{i}\right)_{i\in I}}$ belongs to the set in **[Eq. 8](#math_Eq._8)** above if and only if ${\displaystyle x_{i}\in S_{i,j}}$ for all ${\displaystyle i\in I}$ and all ${\displaystyle j\in J.}$

In particular, if ${\displaystyle \left(L_{i}\right)_{i\in I}}$ and ${\displaystyle \left(R_{i}\right)_{i\in I}}$ are two families indexed by the same set then 
$$
{\displaystyle \left(\prod _{i\in I}L_{i}\right)\cap \prod _{i\in I}R_{i}~=~\prod _{i\in I}\left(L_{i}\cap R_{i}\right)}
$$
 So for instance, 
$$
{\displaystyle (L\times R)\cap \left(L_{2}\times R_{2}\right)~=~\left(L\cap L_{2}\right)\times \left(R\cap R_{2}\right)}
$$
 
$$
{\displaystyle (L\times R)\cap \left(L_{2}\times R_{2}\right)\cap \left(L_{3}\times R_{3}\right)~=~\left(L\cap L_{2}\cap L_{3}\right)\times \left(R\cap R_{2}\cap R_{3}\right)}
$$
 and 
$$
{\displaystyle (L\times M\times R)\cap \left(L_{2}\times M_{2}\times R_{2}\right)~=~\left(L\cap L_{2}\right)\times \left(M\cap M_{2}\right)\times \left(R\cap R_{2}\right)}
$$

**Intersections of products indexed by different sets**

Let ${\displaystyle \left(L_{i}\right)_{i\in I}}$ and ${\displaystyle \left(R_{j}\right)_{j\in J}}$ be two families indexed by different sets.

Technically, ${\displaystyle I\neq J}$ implies ${\displaystyle \left({\textstyle \prod \limits _{i\in I}}L_{i}\right)\cap {\textstyle \prod \limits _{j\in J}}R_{j}=\varnothing .}$ However, sometimes these products are somehow identified as the same set through some [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") or one of these products is identified as a subset of the other via some [injective map](https://en.wikipedia.org/wiki/Injective_map "Injective map"), in which case (by [abuse of notation](https://en.wikipedia.org/wiki/Abuse_of_notation "Abuse of notation")) this intersection may be equal to some other (possibly non-empty) set.

- For example, if ${\displaystyle I:=\{1,2\}}$ and ${\displaystyle J:=\{1,2,3\}}$ with all sets equal to ${\displaystyle \mathbb {R} }$ then ${\displaystyle {\textstyle \prod \limits _{i\in I}}L_{i}={\textstyle \prod \limits _{i\in \{1,2\}}}\mathbb {R} =\mathbb {R} ^{2}}$ and ${\displaystyle {\textstyle \prod \limits _{j\in J}}R_{j}={\textstyle \prod \limits _{j\in \{1,2,3\}}}\mathbb {R} =\mathbb {R} ^{3}}$ where ${\displaystyle \mathbb {R} ^{2}\cap \mathbb {R} ^{3}=\varnothing }$ *unless*, for example, ${\displaystyle {\textstyle \prod \limits _{i\in \{1,2\}}}\mathbb {R} =\mathbb {R} ^{2}}$ is identified as a subset of ${\displaystyle {\textstyle \prod \limits _{j\in \{1,2,3\}}}\mathbb {R} =\mathbb {R} ^{3}}$ through some [injection](https://en.wikipedia.org/wiki/Injective_map "Injective map"), such as maybe ${\displaystyle (x,y)\mapsto (x,y,0)}$ for instance; however, in this particular case the product ${\displaystyle {\textstyle \prod \limits _{i\in I=\{1,2\}}}L_{i}}$ actually represents the ${\displaystyle J}$ -indexed product ${\displaystyle {\textstyle \prod \limits _{j\in J=\{1,2,3\}}}L_{i}}$ where ${\displaystyle L_{3}:=\{0\}.}$
- For another example, take ${\displaystyle I:=\{1,2\}}$ and ${\displaystyle J:=\{1,2,3\}}$ with ${\displaystyle L_{1}:=\mathbb {R} ^{2}}$ and ${\displaystyle L_{2},R_{1},R_{2},{\text{ and }}R_{3}}$ all equal to ${\displaystyle \mathbb {R} .}$ Then ${\displaystyle {\textstyle \prod \limits _{i\in I}}L_{i}=\mathbb {R} ^{2}\times \mathbb {R} }$ and ${\displaystyle {\textstyle \prod \limits _{j\in J}}R_{j}=\mathbb {R} \times \mathbb {R} \times \mathbb {R} ,}$ which can both be identified as the same set via the bijection that sends ${\displaystyle ((x,y),z)\in \mathbb {R} ^{2}\times \mathbb {R} }$ to ${\displaystyle (x,y,z)\in \mathbb {R} \times \mathbb {R} \times \mathbb {R} .}$ Under this identification, ${\displaystyle \left({\textstyle \prod \limits _{i\in I}}L_{i}\right)\cap \,{\textstyle \prod \limits _{j\in J}}R_{j}~=~\mathbb {R} ^{3}.}$

#### Binary ⨯ distributes over arbitrary ⋃ and ⋂

The binary [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") ⨯ [distributes over](#Distributivity) arbitrary intersections (when the indexing set is not empty) and over arbitrary unions:

$$
{\displaystyle {\begin{alignedat}{5}L\times \left(\bigcup _{i\in I}R_{i}\right)&\;=\;\;&&\bigcup _{i\in I}(L\times R_{i})\qquad &&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]L\times \left(\bigcap _{i\in I}R_{i}\right)&\;=\;\;&&\bigcap _{i\in I}(L\times R_{i})\qquad &&{\text{ (Left-distributivity of }}\,\times \,{\text{ over }}\,\bigcap _{i\in I}\,{\text{ when }}I\neq \varnothing \,{\text{)}}\\[1.4ex]\left(\bigcup _{i\in I}L_{i}\right)\times R&\;=\;\;&&\bigcup _{i\in I}(L_{i}\times R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\cup \,{\text{)}}\\[1.4ex]\left(\bigcap _{i\in I}L_{i}\right)\times R&\;=\;\;&&\bigcap _{i\in I}(L_{i}\times R)\qquad &&{\text{ (Right-distributivity of }}\,\times \,{\text{ over }}\,\bigcap _{i\in I}\,{\text{ when }}I\neq \varnothing \,{\text{)}}\\[1.4ex]\end{alignedat}}}
$$

#### Distributing arbitrary Π over arbitrary ⋃

Suppose that for each ${\displaystyle i\in I,}$ ${\displaystyle J_{i}}$ is a non-empty index set and for each ${\displaystyle j\in J_{i},}$ let ${\displaystyle T_{i,j}}$ be any set (for example, to apply this law to ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J},}$ use ${\displaystyle J_{i}\colon =J}$ for all ${\displaystyle i\in I}$ and use ${\displaystyle T_{i,j}\colon =S_{i,j}}$ for all ${\displaystyle i\in I}$ and all ${\displaystyle j\in J_{i}=J}$). Let 
$$
{\displaystyle {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\prod _{i\in I}J_{i}}
$$
 denote the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product"), which (as [mentioned above](#Correctly_distributing_arbitrary_intersections_and_arbitrary_unions)) can be interpreted as the set of all functions ${\displaystyle f~:~I~\to ~{\textstyle \bigcup \limits _{i\in I}}J_{i}}$ such that ${\displaystyle f(i)\in J_{i}}$ for every ${\displaystyle i\in I}$. Then

<table><tbody><tr><td><math>{\displaystyle \prod _{i\in I}\left[\;\bigcup _{j\in J_{i}}T_{i,j}\right]=\bigcup _{f\in \prod J_{\bullet }}\left[\;\prod _{i\in I}T_{i,f(i)}\right]}</math></td><td><table><tbody><tr><td rowspan="2"></td><td></td><td rowspan="2"></td></tr><tr><td></td></tr></tbody></table></td><td>Eq. 11 Π∪ to ∪Π</td></tr></tbody></table>

where ${\displaystyle {\textstyle \prod }J_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~{\textstyle \prod \limits _{i\in I}}J_{i}.}$

#### Unions ⋃ of Π

For unions, only the following is guaranteed in general: 
$$
{\displaystyle \bigcup _{j\in J}\;\prod _{i\in I}S_{i,j}~~\color {Red}{\subseteq }\color {Black}{}~~\prod _{i\in I}\;\bigcup _{j\in J}S_{i,j}\qquad {\text{ and }}\qquad \bigcup _{i\in I}\;\prod _{j\in J}S_{i,j}~~\color {Red}{\subseteq }\color {Black}{}~~\prod _{j\in J}\;\bigcup _{i\in I}S_{i,j}}
$$
 where ${\displaystyle \left(S_{i,j}\right)_{(i,j)\in I\times J}}$ is a family of sets.

- **Example where equality fails**: Let ${\displaystyle I=J=\{1,2\},}$ let ${\displaystyle S_{1,1}=S_{2,2}=\varnothing ,}$ let ${\displaystyle X\neq \varnothing ,}$ and let ${\displaystyle S_{1,2}=S_{2,1}=X.}$ Then 
	$$
	{\displaystyle \varnothing =\varnothing \cup \varnothing =\left(\prod _{i\in I}S_{i,1}\right)\cup \left(\prod _{i\in I}S_{i,2}\right)=\bigcup _{j\in J}\;\prod _{i\in I}S_{i,j}~~\color {Red}{\neq }\color {Black}{}~~\prod _{i\in I}\;\bigcup _{j\in J}S_{i,j}=\left(\bigcup _{j\in J}S_{1,j}\right)\times \left(\bigcup _{j\in J}S_{2,j}\right)=X\times X.}
	$$
	 More generally, ${\textstyle \varnothing =\bigcup _{j\in J}\;\prod _{i\in I}S_{i,j}}$ if and only if for each ${\displaystyle j\in J,}$ at least one of the sets in the ${\displaystyle I}$ -indexed collections of sets ${\displaystyle S_{\bullet ,j}=\left(S_{i,j}\right)_{i\in I}}$ is empty, while ${\textstyle \prod _{i\in I}\;\bigcup _{j\in J}S_{i,j}\neq \varnothing }$ if and only if for each ${\displaystyle i\in I,}$ at least one of the sets in the ${\displaystyle J}$ -indexed collections of sets ${\displaystyle S_{i,\bullet }=\left(S_{i,j}\right)_{j\in J}}$ is not empty.

However, 
$$
{\displaystyle {\begin{alignedat}{9}\left(L\times R\right)~\cup ~\left(L_{2}\times R_{2}\right)~&=~\left[\left(L\setminus L_{2}\right)\times R\right]~\cup ~\left[\left(L_{2}\setminus L\right)\times R_{2}\right]~\cup ~\left[\left(L\cap L_{2}\right)\times \left(R\cup R_{2}\right)\right]\\[0.5ex]~&=~\left[L\times \left(R\setminus R_{2}\right)\right]~\cup ~\left[L_{2}\times \left(R_{2}\setminus R\right)\right]~\cup ~\left[\left(L\cup L_{2}\right)\times \left(R\cap R_{2}\right)\right]\\\end{alignedat}}}
$$

#### Difference \\ of Π

If ${\displaystyle \left(L_{i}\right)_{i\in I}}$ and ${\displaystyle \left(R_{i}\right)_{i\in I}}$ are two families of sets then: 
$$
{\displaystyle {\begin{alignedat}{9}\left(\prod _{i\in I}L_{i}\right)~\setminus ~\prod _{i\in I}R_{i}~&=~\;~\bigcup _{j\in I}\;~\prod _{i\in I}{\begin{cases}L_{j}\,\setminus \,R_{j}&{\text{ if }}i=j\\L_{i}&{\text{ if }}i\neq j\\\end{cases}}\\[0.5ex]~&=~\;~\bigcup _{j\in I}\;~{\Big [}\left(L_{j}\,\setminus \,R_{j}\right)~\times ~\prod _{\stackrel {i\in I,}{j\neq i}}L_{i}{\Big ]}\\[0.5ex]~&=~\bigcup _{\stackrel {j\in I,}{L_{j}\not \subseteq R_{j}}}{\Big [}\left(L_{j}\,\setminus \,R_{j}\right)~\times ~\prod _{\stackrel {i\in I,}{j\neq i}}L_{i}{\Big ]}\\[0.3ex]\end{alignedat}}}
$$
 so for instance, 
$$
{\displaystyle {\begin{alignedat}{9}\left(L\times R\right)~\setminus ~\left(L_{2}\times R_{2}\right)~&=~\left[\left(L\,\setminus \,L_{2}\right)\times R\right]~\cup ~\left[L\times \left(R\,\setminus \,R_{2}\right)\right]\\\end{alignedat}}}
$$
 and 
$$
{\displaystyle (L\times M\times R)~\setminus ~\left(L_{2}\times M_{2}\times R_{2}\right)~=~\left[\left(L\,\setminus \,L_{2}\right)\times M\times R\right]~\cup ~\left[L\times \left(M\,\setminus \,M_{2}\right)\times R\right]~\cup ~\left[L\times M\times \left(R\,\setminus \,R_{2}\right)\right]}
$$

#### Symmetric difference ∆ of Π

$$
{\displaystyle {\begin{alignedat}{9}\left(\prod _{i\in I}L_{i}\right)~\triangle ~\left(\prod _{i\in I}R_{i}\right)~&=~\;~\left(\prod _{i\in I}L_{i}\right)~\cup ~\left(\prod _{i\in I}R_{i}\right)\;\setminus \;\prod _{i\in I}L_{i}\cap R_{i}\\[0.5ex]\end{alignedat}}}
$$

## Functions and sets

Let ${\displaystyle f:X\to Y}$ be any function.

Let ${\displaystyle L{\text{ and }}R}$ be completely arbitrary sets. Assume ${\displaystyle A\subseteq X{\text{ and }}C\subseteq Y.}$

### Definitions

Let ${\displaystyle f:X\to Y}$ be any function, where we denote its *domain* ${\displaystyle X}$ by ${\displaystyle \operatorname {domain} f}$ and denote its *codomain* ${\displaystyle Y}$ by ${\displaystyle \operatorname {codomain} f.}$

Many of the identities below do not actually require that the sets be somehow related to ${\displaystyle f}$ 's domain or [codomain](https://en.wikipedia.org/wiki/Codomain "Codomain") (that is, to ${\displaystyle X}$ or ${\displaystyle Y}$) so when some kind of relationship is necessary then it will be clearly indicated. Because of this, in this article, if ${\displaystyle L}$ is declared to be " *any set*," and it is not indicated that ${\displaystyle L}$ must be somehow related to ${\displaystyle X}$ or ${\displaystyle Y}$ (say for instance, that it be a subset ${\displaystyle X}$ or ${\displaystyle Y}$) then it is meant that ${\displaystyle L}$ is truly arbitrary.[^3] This generality is useful in situations where ${\displaystyle f:X\to Y}$ is a map between two subsets ${\displaystyle X\subseteq U}$ and ${\displaystyle Y\subseteq V}$ of some larger sets ${\displaystyle U}$ and ${\displaystyle V,}$ and where the set ${\displaystyle L}$ might not be entirely contained in ${\displaystyle X=\operatorname {domain} f}$ and/or ${\displaystyle Y=\operatorname {codomain} f}$ (e.g. if all that is known about ${\displaystyle L}$ is that ${\displaystyle L\subseteq U}$); in such a situation it may be useful to know what can and cannot be said about ${\displaystyle f(L)}$ and/or ${\displaystyle f^{-1}(L)}$ without having to introduce a (potentially unnecessary) intersection such as: ${\displaystyle f(L\cap X)}$ and/or ${\displaystyle f^{-1}(L\cap Y).}$

**Images and preimages of sets**

If ${\displaystyle L}$ is *any* set then the *[*image*](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)") of ${\displaystyle L}$ under ${\displaystyle f}$* is defined to be the set: 
$$
{\displaystyle f(L)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{\,f(l)~:~l\in L\cap \operatorname {domain} f\,\}}
$$
 while the *[preimage](https://en.wikipedia.org/wiki/Preimage "Preimage") of ${\displaystyle L}$ under ${\displaystyle f}$* is: 
$$
{\displaystyle f^{-1}(L)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\{\,x\in \operatorname {domain} f~:~f(x)\in L\,\}}
$$
 where if ${\displaystyle L=\{s\}}$ is a singleton set then the *[fiber](https://en.wikipedia.org/wiki/Fiber_\(mathematics\) "Fiber (mathematics)")* or *[preimage](https://en.wikipedia.org/wiki/Preimage "Preimage") of ${\displaystyle s}$ under ${\displaystyle f}$* is 
$$
{\displaystyle f^{-1}(s)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~f^{-1}(\{s\})~=~\{\,x\in \operatorname {domain} f~:~f(x)=s\,\}.}
$$

Denote by ${\displaystyle \operatorname {Im} f}$ or ${\displaystyle \operatorname {image} f}$ the *image* or *[range](https://en.wikipedia.org/wiki/Range_of_a_function "Range of a function")* of ${\displaystyle f:X\to Y,}$ which is the set: 
$$
{\displaystyle \operatorname {Im} f~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~f(X)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~f(\operatorname {domain} f)~=~\{f(x)~:~x\in \operatorname {domain} f\}.}
$$

**Saturated sets**

A set ${\displaystyle A}$ is said to be *${\displaystyle f}$ - **saturated*** or a ***[saturated set](https://en.wikipedia.org/wiki/Saturated_set "Saturated set")*** if any of the following equivalent conditions are satisfied:[^13]

1. There exists a set ${\displaystyle R}$ such that ${\displaystyle A=f^{-1}(R).}$
	- Any such set ${\displaystyle R}$ necessarily contains ${\displaystyle f(A)}$ as a subset.
		- Any set not entirely contained in the domain of ${\displaystyle f}$ cannot be ${\displaystyle f}$ -saturated.
2. ${\displaystyle A=f^{-1}(f(A)).}$
3. ${\displaystyle A\supseteq f^{-1}(f(A))}$ and ${\displaystyle A\subseteq \operatorname {domain} f.}$
	- The inclusion ${\displaystyle L\cap \operatorname {domain} f\subseteq f^{-1}(f(L))}$ always holds, where if ${\displaystyle A\subseteq \operatorname {domain} f}$ then this becomes ${\displaystyle A\subseteq f^{-1}(f(A)).}$
4. ${\displaystyle A\subseteq \operatorname {domain} f}$ and if ${\displaystyle a\in A}$ and ${\displaystyle x\in \operatorname {domain} f}$ satisfy ${\displaystyle f(x)=f(a),}$ then ${\displaystyle x\in A.}$
5. Whenever a fiber of ${\displaystyle f}$ intersects ${\displaystyle A,}$ then ${\displaystyle A}$ contains the entire fiber. In other words, ${\displaystyle A}$ contains every ${\displaystyle f}$ -fiber that intersects it.
- Explicitly: whenever ${\displaystyle y\in \operatorname {Im} f}$ is such that ${\displaystyle A\cap f^{-1}(y)\neq \varnothing ,}$ then ${\displaystyle f^{-1}(y)\subseteq A.}$
	- In both this statement and the next, the set ${\displaystyle \operatorname {Im} f}$ may be replaced with any superset of ${\displaystyle \operatorname {Im} f}$ (such as ${\displaystyle \operatorname {codomain} f}$) and the resulting statement will still be equivalent to the rest.
7. The intersection of ${\displaystyle A}$ with a fiber of ${\displaystyle f}$ is equal to the empty set or to the fiber itself.
	- Explicitly: for every ${\displaystyle y\in \operatorname {Im} f,}$ the intersection ${\displaystyle A\cap f^{-1}(y)}$ is equal to the [empty set](https://en.wikipedia.org/wiki/Empty_set "Empty set") ${\displaystyle \varnothing }$ or to ${\displaystyle f^{-1}(y)}$ (that is, ${\displaystyle A\cap f^{-1}(y)=\varnothing }$ or ${\displaystyle A\cap f^{-1}(y)=f^{-1}(y)}$).

For a set ${\displaystyle A}$ to be ${\displaystyle f}$ -saturated, it is necessary that ${\displaystyle A\subseteq \operatorname {domain} f.}$

**Compositions and restrictions of functions**

If ${\displaystyle f}$ and ${\displaystyle g}$ are maps then ${\displaystyle g\circ f}$ denotes the *[composition](https://en.wikipedia.org/wiki/Function_composition "Function composition")* map 
$$
{\displaystyle g\circ f~:~\{\,x\in \operatorname {domain} f~:~f(x)\in \operatorname {domain} g\,\}~\to ~\operatorname {codomain} g}
$$
 with domain and codomain 
$$
{\displaystyle {\begin{alignedat}{4}\operatorname {domain} (g\circ f)&=\{\,x\in \operatorname {domain} f~:~f(x)\in \operatorname {domain} g\,\}\\[0.4ex]\operatorname {codomain} (g\circ f)&=\operatorname {codomain} g\\[0.7ex]\end{alignedat}}}
$$
 defined by 
$$
{\displaystyle (g\circ f)(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~g(f(x)).}
$$

The *[restriction](https://en.wikipedia.org/wiki/Restriction_\(mathematics\) "Restriction (mathematics)") of ${\displaystyle f:X\to Y}$ to ${\displaystyle L,}$* denoted by ${\displaystyle f{\big \vert }_{L},}$ is the map 
$$
{\displaystyle f{\big \vert }_{L}~:~L\cap \operatorname {domain} f~\to ~Y}
$$
 with ${\displaystyle \operatorname {domain} f{\big \vert }_{L}~=~L\cap \operatorname {domain} f}$ defined by sending ${\displaystyle x\in L\cap \operatorname {domain} f}$ to ${\displaystyle f(x);}$ that is, 
$$
{\displaystyle f{\big \vert }_{L}(x)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~f(x).}
$$
 Alternatively, ${\displaystyle ~f{\big \vert }_{L}~=~f\circ \operatorname {In} ~}$ where ${\displaystyle ~\operatorname {In} ~:~L\cap X\to X~}$ denotes the [inclusion map](https://en.wikipedia.org/wiki/Inclusion_map "Inclusion map"), which is defined by ${\displaystyle \operatorname {In} (s)~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~s.}$

### (Pre)Images of arbitrary unions ⋃'s and intersections ⋂'s

If ${\displaystyle \left(L_{i}\right)_{i\in I}}$ is a family of arbitrary sets indexed by ${\displaystyle I\neq \varnothing }$ then:[^15] 
$$
{\displaystyle {\begin{alignedat}{4}f\left(\bigcap _{i\in I}L_{i}\right)\;&~\;\color {Red}{\subseteq }\color {Black}{}~\;\;\;\bigcap _{i\in I}f\left(L_{i}\right)\\f\left(\bigcup _{i\in I}L_{i}\right)\;&~=~\;\bigcup _{i\in I}f\left(L_{i}\right)\\f^{-1}\left(\bigcup _{i\in I}L_{i}\right)\;&~=~\;\bigcup _{i\in I}f^{-1}\left(L_{i}\right)\\f^{-1}\left(\bigcap _{i\in I}L_{i}\right)\;&~=~\;\bigcap _{i\in I}f^{-1}\left(L_{i}\right)\\\end{alignedat}}}
$$

So of these four identities, it is *only* ***images of intersections*** that are not always preserved. Preimages preserve all basic set operations. Unions are preserved by both images and preimages.

If all ${\displaystyle L_{i}}$ are ${\displaystyle f}$ -saturated then ${\displaystyle \bigcap _{i\in I}L_{i}}$ be will be ${\displaystyle f}$ -saturated and equality will hold in the first relation above; explicitly, this means:

| $$ {\displaystyle f\left(\bigcap _{i\in I}L_{i}\right)~=~\bigcap _{i\in I}f\left(L_{i}\right)\qquad {\textit {IF}}\qquad X\cap L_{i}=f^{-1}\left(f\left(L_{i}\right)\right)\quad {\text{ for all }}\quad i\in I.} $$ |  | Conditional Equality 10a |
| --- | --- | --- |

If ${\displaystyle \left(A_{i}\right)_{i\in I}}$ is a family of arbitrary subsets of ${\displaystyle X=\operatorname {domain} f,}$ which means that ${\displaystyle A_{i}\subseteq X}$ for all ${\displaystyle i,}$ then **[Conditional Equality 10a](#math_Conditional_Equality_10a)** becomes:

| $$ {\displaystyle f\left(\bigcap _{i\in I}A_{i}\right)~=~\bigcap _{i\in I}f\left(A_{i}\right)\qquad {\textit {IF}}\qquad A_{i}=f^{-1}\left(f\left(A_{i}\right)\right)\quad {\text{ for all }}\quad i\in I.} $$ |  | Conditional Equality 10b |
| --- | --- | --- |

### (Pre)Images of binary set operations

Throughout, let ${\displaystyle L}$ and ${\displaystyle R}$ be any sets and let ${\displaystyle f:X\to Y}$ be any function.

**Summary**

As the table below shows, set equality is *not* guaranteed *only* for *images* of: intersections, set subtractions, and symmetric differences.

| Image | Preimage | Additional assumptions on sets |
| --- | --- | --- |
| ${\displaystyle \,~~~~f(L\cup R)~=~f(L)\cup f(R)}$ [^16] | ${\displaystyle f^{-1}(L\cup R)~=~f^{-1}(L)\cup f^{-1}(R)}$ [^13] | None |
| $$ {\displaystyle f(L\cap R)~\subseteq ~f(L)\cap f(R)} $$ | ${\displaystyle f^{-1}(L\cap R)~=~f^{-1}(L)\cap f^{-1}(R)}$ [^13] | None |
| $$ {\displaystyle f(L\setminus R)~\supseteq ~f(L)\setminus f(R)} $$ | ${\displaystyle {\begin{alignedat}{4}f^{-1}(L)\setminus f^{-1}(R)&=f^{-1}&&(&&L&&\setminus &&R)\\&=f^{-1}&&(&&L&&\setminus [&&R\cap \operatorname {Im} f])\\&=f^{-1}&&([&&L\cap \operatorname {Im} f]&&\setminus &&R)\\&=f^{-1}&&([&&L\cap \operatorname {Im} f]&&\setminus [&&R\cap \operatorname {Im} f])\end{alignedat}}}$ [^15] [^13] | None |
| $$ {\displaystyle f(X\setminus R)~\supseteq ~f(X)\setminus f(R)} $$ | ${\displaystyle {\begin{alignedat}{4}X\setminus f^{-1}(R)&=f^{-1}(&&Y&&\setminus &&R)\\&=f^{-1}(&&Y&&\setminus [&&R\cap \operatorname {Im} f])\\&=f^{-1}(&&\operatorname {Im} f&&\setminus &&R)\\&=f^{-1}(&&\operatorname {Im} f&&\setminus [&&R\cap \operatorname {Im} f])\end{alignedat}}}$ [^4] | None |
| $$ {\displaystyle f\left(L~\triangle ~R\right)~\supseteq ~f(L)~\triangle ~f(R)} $$ | ${\displaystyle f^{-1}\left(L~\triangle ~R\right)~=~f^{-1}(L)~\triangle ~f^{-1}(R)}$ | None |

**Preimages preserve set operations**

Preimages of sets are well-behaved with respect to all basic set operations:

$$
{\displaystyle {\begin{alignedat}{4}f^{-1}(L\cup R)~&=~f^{-1}(L)\cup f^{-1}(R)\\f^{-1}(L\cap R)~&=~f^{-1}(L)\cap f^{-1}(R)\\f^{-1}(L\setminus \,R)~&=~f^{-1}(L)\setminus \,f^{-1}(R)\\f^{-1}(L\,\triangle \,R)~&=~f^{-1}(L)\,\triangle \,f^{-1}(R)\\\end{alignedat}}}
$$

In words, preimages [distribute over](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") unions, intersections, set subtraction, and symmetric difference.

**Images *only* preserve unions**

Images of unions are well-behaved:

$$
{\displaystyle {\begin{alignedat}{4}f(L\cup R)~&=~f(L)\cup f(R)\\\end{alignedat}}}
$$

but images of the other basic set operations are *not* since only the following are guaranteed in general:

$$
{\displaystyle {\begin{alignedat}{4}f(L\cap R)~&\subseteq ~f(L)\cap f(R)\\f(L\setminus R)~&\supseteq ~f(L)\setminus f(R)\\f(L\triangle R)~&\supseteq ~f(L)\,\triangle \,f(R)\\\end{alignedat}}}
$$

In words, images [distribute over](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") unions but not necessarily over intersections, set subtraction, or symmetric difference. What these latter three operations have in common is set subtraction: they either *are* [set subtraction](https://en.wikipedia.org/wiki/Set_subtraction "Set subtraction") ${\displaystyle L\setminus R}$ or else they can naturally *be defined* as the set subtraction of two sets: 
$$
{\displaystyle L\cap R=L\setminus (L\setminus R)\quad {\text{ and }}\quad L\triangle R=(L\cup R)\setminus (L\cap R).}
$$

If ${\displaystyle L=X}$ then ${\displaystyle f(X\setminus R)\supseteq f(X)\setminus f(R)}$ where as in the more general case, equality is not guaranteed. If ${\displaystyle f}$ is surjective then ${\displaystyle f(X\setminus R)~\supseteq ~Y\setminus f(R),}$ which can be rewritten as: ${\displaystyle f\left(R^{\complement }\right)~\supseteq ~f(R)^{\complement }}$ if ${\displaystyle R^{\complement }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~X\setminus R}$ and ${\displaystyle f(R)^{\complement }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~Y\setminus f(R).}$

#### Counter-examples: images of operations not distributing

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Image_preimage_conterexample_intersection.gif/500px-Image_preimage_conterexample_intersection.gif)

Picture showing {\\displaystyle f} failing to distribute over set intersection: {\\displaystyle f\\left(A\_{1}\\cap A\_{2}\\right)\\subsetneq f\\left(A\_{1}\\right)\\cap f\\left(A\_{2}\\right).} The map {\\displaystyle f:\\mathbb {R} \\to \\mathbb {R} } is defined by {\\displaystyle x\\mapsto x^{2},} where {\\displaystyle \\mathbb {R} } denotes the real numbers. The sets {\\displaystyle A\_{1}=\[-4,2\]} and {\\displaystyle A\_{2}=\[-2,4\]} are shown in blue immediately below the {\\displaystyle x} -axis while their intersection {\\displaystyle A\_{3}=\[-2,2\]} is shown in green.

If ${\displaystyle f:\{1,2\}\to Y}$ is constant, ${\displaystyle L=\{1\},}$ and ${\displaystyle R=\{2\}}$ then all four of the set containments 
$$
{\displaystyle {\begin{alignedat}{4}f(L\cap R)~&\subsetneq ~f(L)\cap f(R)\\f(L\setminus R)~&\supsetneq ~f(L)\setminus f(R)\\f(X\setminus R)~&\supsetneq ~f(X)\setminus f(R)\\f(L\triangle R)~&\supsetneq ~f(L)\triangle f(R)\\\end{alignedat}}}
$$
 are [strict/proper](https://en.wikipedia.org/wiki/Proper_subset "Proper subset") (that is, the sets are not equal) since one side is the empty set while the other is non-empty. Thus equality is not guaranteed for even the simplest of functions. The example above is now generalized to show that these four set equalities can fail for any [constant function](https://en.wikipedia.org/wiki/Constant_function "Constant function") whose domain contains at least two (distinct) points.

***Example***: Let ${\displaystyle f:X\to Y}$ be any constant function with image ${\displaystyle f(X)=\{y\}}$ and suppose that ${\displaystyle L,R\subseteq X}$ are non-empty disjoint subsets; that is, ${\displaystyle L\neq \varnothing ,R\neq \varnothing ,}$ and ${\displaystyle L\cap R=\varnothing ,}$ which implies that all of the sets ${\displaystyle L~\triangle ~R=L\cup R,}$ ${\displaystyle \,L\setminus R=L,}$ and ${\displaystyle X\setminus R\supseteq L\setminus R}$ are not empty and so consequently, their images under ${\displaystyle f}$ are all equal to ${\displaystyle \{y\}.}$

1. The containment ${\displaystyle ~f(L\setminus R)~\supsetneq ~f(L)\setminus f(R)~}$ is strict: 
	$$
	{\displaystyle \{y\}~=~f(L\setminus R)~\neq ~f(L)\setminus f(R)~=~\{y\}\setminus \{y\}~=~\varnothing }
	$$
	 In words: functions might not [distribute over set subtraction ${\displaystyle \,\setminus \,}$](https://en.wikipedia.org/wiki/Distributive_property "Distributive property")
2. The containment ${\displaystyle ~f(X\setminus R)~\supsetneq ~f(X)\setminus f(R)~}$ is strict: 
	$$
	{\displaystyle \{y\}~=~f(X\setminus R)~\neq ~f(X)\setminus f(R)~=~\{y\}\setminus \{y\}~=~\varnothing .}
	$$
3. The containment ${\displaystyle ~f(L~\triangle ~R)~\supsetneq ~f(L)~\triangle ~f(R)~}$ is strict: 
	$$
	{\displaystyle \{y\}~=~f\left(L~\triangle ~R\right)~\neq ~f(L)~\triangle ~f(R)~=~\{y\}\triangle \{y\}~=~\varnothing }
	$$
	 In words: functions might not [distribute over symmetric difference ${\displaystyle \,\triangle \,}$](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") (which can be defined as the set subtraction of two sets: ${\displaystyle L\triangle R=(L\cup R)\setminus (L\cap R)}$).
4. The containment ${\displaystyle ~f(L\cap R)~\subsetneq ~f(L)\cap f(R)~}$ is strict: 
	$$
	{\displaystyle \varnothing ~=~f(\varnothing )~=~f(L\cap R)~\neq ~f(L)\cap f(R)~=~\{y\}\cap \{y\}~=~\{y\}}
	$$
	 In words: functions might not [distribute over set intersection ${\displaystyle \,\cap \,}$](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") (which can be defined as the set subtraction of two sets: ${\displaystyle L\cap R=L\setminus (L\setminus R)}$).

What the set operations in these four examples have in common is that they either *are* [set subtraction](https://en.wikipedia.org/wiki/Set_subtraction "Set subtraction") ${\displaystyle \setminus }$ (examples (1) and (2)) or else they can naturally *be defined* as the set subtraction of two sets (examples (3) and (4)).

**Mnemonic**: In fact, for each of the above four set formulas for which equality is not guaranteed, the direction of the containment (that is, whether to use ${\displaystyle \,\subseteq {\text{ or }}\supseteq \,}$) can always be deduced by imagining the function ${\displaystyle f}$ as being *constant* and the two sets (${\displaystyle L}$ and ${\displaystyle R}$) as being non-empty disjoint subsets of its domain. This is because *every* equality fails for such a function and sets: one side will be always be ${\displaystyle \varnothing }$ and the other non-empty − from this fact, the correct choice of ${\displaystyle \,\subseteq {\text{ or }}\supseteq \,}$ can be deduced by answering: "which side is empty?" For example, to decide if the ${\displaystyle ?}$ in 
$$
{\displaystyle f(L\triangle R)\setminus f(R)~\;~?~\;~f((L\triangle R)\setminus R)}
$$
 should be ${\displaystyle \,\subseteq {\text{ or }}\supseteq ,\,}$ pretend [^5] that ${\displaystyle f}$ is constant and that ${\displaystyle L\triangle R}$ and ${\displaystyle R}$ are non-empty disjoint subsets of ${\displaystyle f}$ 's domain; then the *left* hand side would be empty (since ${\displaystyle f(L\triangle R)\setminus f(R)=\{f{\text{'s single value}}\}\setminus \{f{\text{'s single value}}\}=\varnothing }$), which indicates that ${\displaystyle \,?\,}$ should be ${\displaystyle \,\subseteq \,}$ (the resulting statement is always guaranteed to be true) because this is the choice that will make 
$$
{\displaystyle \varnothing ={\text{left hand side}}~\;~?~\;~{\text{right hand side}}}
$$
 true. Alternatively, the correct direction of containment can also be deduced by consideration of any constant ${\displaystyle f:\{1,2\}\to Y}$ with ${\displaystyle L=\{1\}}$ and ${\displaystyle R=\{2\}.}$

Furthermore, this mnemonic can also be used to correctly deduce whether or not a set operation always distribute over images or preimages; for example, to determine whether or not ${\displaystyle f(L\cap R)}$ always equals ${\displaystyle f(L)\cap f(R),}$ or alternatively, whether or not ${\displaystyle f^{-1}(L\cap R)}$ always equals ${\displaystyle f^{-1}(L)\cap f^{-1}(R)}$ (although ${\displaystyle \,\cap \,}$ was used here, it can replaced by ${\displaystyle \,\cup ,\,\setminus ,{\text{ or }}\,\triangle }$). The answer to such a question can, as before, be deduced by consideration of this constant function: the answer for the general case (that is, for arbitrary ${\displaystyle f,L,}$ and ${\displaystyle R}$) is always the same as the answer for this choice of (constant) function and disjoint non-empty sets.

#### Conditions guaranteeing that images distribute over set operations

**Characterizations of when equality holds for *all* sets**:

For any function ${\displaystyle f:X\to Y,}$ the following statements are equivalent:

1. ${\displaystyle f:X\to Y}$ is [injective](https://en.wikipedia.org/wiki/Injective_function "Injective function").
	- This means: ${\displaystyle f(x)\neq f(y)}$ for all distinct ${\displaystyle x,y\in X.}$
2. ${\displaystyle f(L\cap R)=f(L)\,\cap \,f(R)\,{\text{ for all }}\,L,R\subseteq X.}$ (The equals sign ${\displaystyle \,=\,}$ can be replaced with ${\displaystyle \,\supseteq \,}$).
3. ${\displaystyle f(L\,\setminus R)=f(L)\,\setminus \,f(R)\;{\text{ for all }}\,L,R\subseteq X.}$ (The equals sign ${\displaystyle \,=\,}$ can be replaced with ${\displaystyle \,\subseteq \,}$).
4. ${\displaystyle f(X\setminus R)=f(X)\setminus \,f(R)\;{\text{ for all }}\,~~~~~R\subseteq X.}$ (The equals sign ${\displaystyle \,=\,}$ can be replaced with ${\displaystyle \,\subseteq \,}$).
5. ${\displaystyle f(L\,\triangle \,R)=f(L)\,\triangle \,f(R)\;{\text{ for all }}\,L,R\subseteq X.}$ (The equals sign ${\displaystyle \,=\,}$ can be replaced with ${\displaystyle \,\subseteq \,}$).
6. Any one of the four statements (b) - (e) but with the words "for all" replaced with any one of the following:
	1. "for all [singleton subsets](https://en.wikipedia.org/wiki/Singleton_set "Singleton set") "
		- In particular, the statement that results from (d) gives a characterization of injectivity that explicitly involves only one point (rather than two): ${\displaystyle f}$ is injective if and only if ${\displaystyle f(x)\not \in f(X\setminus \{x\})\;{\text{ for every }}\,x\in X.}$
		2. "for all [disjoint](https://en.wikipedia.org/wiki/Disjoint_sets "Disjoint sets") singleton subsets"
		- For statement (d), this is the same as: "for all singleton subsets" (because the definition of " [pairwise disjoint](https://en.wikipedia.org/wiki/Pairwise_disjoint "Pairwise disjoint") " is satisfies vacuously by any family that consists of exactly 1 set).
		3. "for all disjoint subsets"

In particular, if a map is not known to be injective then barring additional information, there is no guarantee that any of the equalities in statements (b) - (e) hold.

[An example above](#ConstantFunctionWithDisjointSubsetsExample) can be used to help prove this characterization. Indeed, comparison of that example with such a proof suggests that the example is representative of the fundamental reason why one of these four equalities in statements (b) - (e) might not hold (that is, representative of "what goes wrong" when a set equality does not hold).

##### Conditions for f(L⋂R) = f(L)⋂f(R)

$$
{\displaystyle f(L\cap R)~\subseteq ~f(L)\cap f(R)\qquad \qquad {\text{ always holds}}}
$$

*Characterizations of equality*: The following statements are equivalent:

1. ${\displaystyle f(L\cap R)~=~f(L)\cap f(R)}$
2. ${\displaystyle f(L\cap R)~\supseteq ~f(L)\cap f(R)}$
3. ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~f^{-1}(f(L\cap R))}$
	- The left hand side ${\displaystyle L\cap f^{-1}(f(R))}$ is always equal to ${\displaystyle L\cap f^{-1}(f(L)\cap f(R))}$ (because ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~f^{-1}(f(L))}$ always holds).
4. ${\displaystyle R\cap f^{-1}(f(L))~\subseteq ~f^{-1}(f(L\cap R))}$
5. ${\displaystyle L\cap f^{-1}(f(R))~=~f^{-1}(f(L\cap R))\cap L}$
6. ${\displaystyle R\cap f^{-1}(f(L))~=~f^{-1}(f(L\cap R))\cap R}$
7. If ${\displaystyle l\in L}$ satisfies ${\displaystyle f(l)\in f(R)}$ then ${\displaystyle f(l)\in f(L\cap R).}$
8. If ${\displaystyle y\in f(L)}$ but ${\displaystyle y\notin f(L\cap R)}$ then ${\displaystyle y\notin f(R).}$
9. ${\displaystyle f(L)\,\setminus \,f(L\cap R)~\subseteq ~f(L)\,\setminus \,f(R)}$
10. ${\displaystyle f(R)\,\setminus \,f(L\cap R)~\subseteq ~f(R)\,\setminus \,f(L)}$
11. ${\displaystyle f(L\cup R)\setminus f(L\cap R)~\subseteq ~f(L)\,\triangle \,f(R)}$
12. Any of the above three conditions (i) - (k) but with the subset symbol ${\displaystyle \,\subseteq \,}$ replaced with an equals sign ${\displaystyle \,=.\,}$

*Sufficient conditions for equality*: Equality holds if any of the following are true:

1. ${\displaystyle f}$ is injective.[^17]
2. The restriction ${\displaystyle f{\big \vert }_{L\cup R}}$ is injective.
3. ${\displaystyle f^{-1}(f(R))~\subseteq ~R}$ [^6]
4. ${\displaystyle f^{-1}(f(L))~\subseteq ~L}$
5. ${\displaystyle R}$ is ${\displaystyle f}$ -saturated; that is, ${\displaystyle f^{-1}(f(R))=R}$ [^6]
6. ${\displaystyle L}$ is ${\displaystyle f}$ -saturated; that is, ${\displaystyle f^{-1}(f(L))=L}$
7. ${\displaystyle f(L)~\subseteq ~f(L\cap R)}$
8. ${\displaystyle f(R)~\subseteq ~f(L\cap R)}$
9. ${\displaystyle f(L\,\setminus \,R)~\subseteq ~f(L)\setminus \,f(R)}$ or equivalently, ${\displaystyle f(L\,\setminus \,R)~=~f(L)\setminus f(R)}$
10. ${\displaystyle f(R\,\setminus \,L)~\subseteq ~f(R)\setminus \,f(L)}$ or equivalently, ${\displaystyle f(R\,\setminus \,L)~=~f(R)\setminus f(L)}$
11. ${\displaystyle f\left(L~\triangle ~R\right)\subseteq f(L)~\triangle ~f(R)}$ or equivalently, ${\displaystyle f\left(L~\triangle ~R\right)=f(L)~\triangle ~f(R)}$
12. ${\displaystyle R\cap \operatorname {domain} f\,\subseteq L}$
13. ${\displaystyle L\cap \operatorname {domain} f\,\subseteq R}$
14. ${\displaystyle R\subseteq L}$
15. ${\displaystyle L\subseteq R}$

In addition, the following always hold: 
$$
{\displaystyle f\left(f^{-1}(L)\cap R\right)~=~L\cap f(R)}
$$
 
$$
{\displaystyle f\left(f^{-1}(L)\cup R\right)~=~(L\cap \operatorname {Im} f)\cup f(R)}
$$

##### Conditions for f(L\\R) = f(L)\\f(R)

$$
{\displaystyle f(L\setminus R)~\supseteq ~f(L)\setminus f(R)\qquad \qquad {\text{ always holds}}}
$$

*Characterizations of equality*: The following statements are equivalent:[^9]

1. ${\displaystyle f(L\setminus R)~=~f(L)\setminus f(R)}$
2. ${\displaystyle f(L\setminus R)~\subseteq ~f(L)\setminus f(R)}$
3. ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~R}$
4. ${\displaystyle L\cap f^{-1}(f(R))~=~L\cap R\cap \operatorname {domain} f}$
5. Whenever ${\displaystyle y\in f(L)\cap f(R)}$ then ${\displaystyle L\cap f^{-1}(y)\subseteq R.}$
6. ${\textstyle f(L)\cap f(R)~\subseteq ~\left\{y\in f(L):L\cap f^{-1}(y)\subseteq R\right\}}$
	- The set on the right hand side is always equal to ${\displaystyle \left\{y\in f(L\cap R):L\cap f^{-1}(y)\,\subseteq R\right\}.}$
7. ${\textstyle f(L)\cap f(R)~=~\left\{y\in f(L):L\cap f^{-1}(y)\subseteq R\right\}}$
	- This is the above condition (f) but with the subset symbol ${\displaystyle \,\subseteq \,}$ replaced with an equals sign ${\displaystyle \,=.\,}$

*Necessary conditions for equality* (excluding characterizations): If equality holds then the following are necessarily true:

1. ${\displaystyle f(L\cap R)=f(L)\cap f(R),}$ or equivalently ${\displaystyle f(L\cap R)\supseteq f(L)\cap f(R).}$
2. ${\displaystyle L\cap f^{-1}(f(R))~=~L\cap f^{-1}(f(L\cap R))}$ or equivalently, ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~f^{-1}(f(L\cap R))}$
3. ${\displaystyle R\cap f^{-1}(f(L))~=~R\cap f^{-1}(f(L\cap R))}$

*Sufficient conditions for equality*: Equality holds if any of the following are true:

1. ${\displaystyle f}$ is injective.
2. The restriction ${\displaystyle f{\big \vert }_{L\cup R}}$ is injective.
3. ${\displaystyle f^{-1}(f(R))~\subseteq ~R}$ [^6] or equivalently, ${\displaystyle R\cap \operatorname {domain} f~=~f^{-1}(f(R))}$
4. ${\displaystyle R}$ is ${\displaystyle f}$ -saturated; that is, ${\displaystyle R=f^{-1}(f(R)).}$ [^6]
5. ${\displaystyle f\left(L~\triangle ~R\right)\subseteq f(L)~\triangle ~f(R)}$ or equivalently, ${\displaystyle f\left(L~\triangle ~R\right)=f(L)~\triangle ~f(R)}$

##### Conditions for f(X\\R) = f(X)\\f(R)

$$
{\displaystyle f(X\setminus R)~\supseteq ~f(X)\setminus f(R)\qquad \qquad {\text{ always holds, where }}f:X\to Y}
$$

*Characterizations of equality*: The following statements are equivalent:[^9]

1. ${\displaystyle f(X\setminus R)~=~f(X)\setminus f(R)}$
2. ${\displaystyle f(X\setminus R)~\subseteq ~f(X)\setminus f(R)}$
3. ${\displaystyle f^{-1}(f(R))\,\subseteq \,R}$
4. ${\displaystyle f^{-1}(f(R))\,=\,R\cap \operatorname {domain} f}$
5. ${\displaystyle R\cap \operatorname {domain} f}$ is ${\displaystyle f}$ -saturated.
6. Whenever ${\displaystyle y\in f(R)}$ then ${\displaystyle f^{-1}(y)\subseteq R.}$
7. ${\textstyle f(R)~\subseteq ~\left\{y\in f(R):f^{-1}(y)\subseteq R\right\}}$
8. ${\textstyle f(R)~=~\left\{y\in f(R):f^{-1}(y)\subseteq R\right\}}$

where if ${\displaystyle R\subseteq \operatorname {domain} f}$ then this list can be extended to include:

1. ${\displaystyle R}$ is ${\displaystyle f}$ -saturated; that is, ${\displaystyle R=f^{-1}(f(R)).}$

*Sufficient conditions for equality*: Equality holds if any of the following are true:

1. ${\displaystyle f}$ is injective.
2. ${\displaystyle R}$ is ${\displaystyle f}$ -saturated; that is, ${\displaystyle R=f^{-1}(f(R)).}$

##### Conditions for f(L∆R) = f(L)∆f(R)

$$
{\displaystyle f\left(L~\triangle ~R\right)~\supseteq ~f(L)~\triangle ~f(R)\qquad \qquad {\text{ always holds}}}
$$

*Characterizations of equality*: The following statements are equivalent:

1. ${\displaystyle f\left(L~\triangle ~R\right)=f(L)~\triangle ~f(R)}$
2. ${\displaystyle f\left(L~\triangle ~R\right)\subseteq f(L)~\triangle ~f(R)}$
3. ${\displaystyle f(L\,\setminus \,R)=f(L)\,\setminus \,f(R)}$ and ${\displaystyle f(R\,\setminus \,L)=f(R)\,\setminus \,f(L)}$
4. ${\displaystyle f(L\,\setminus \,R)\subseteq f(L)\,\setminus \,f(R)}$ and ${\displaystyle f(R\,\setminus \,L)\subseteq f(R)\,\setminus \,f(L)}$
5. ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~R}$ and ${\displaystyle R\cap f^{-1}(f(L))~\subseteq ~L}$
	- The inclusions ${\displaystyle L\cap f^{-1}(f(R))~\subseteq ~f^{-1}(f(L))}$ and ${\displaystyle R\cap f^{-1}(f(L))~\subseteq ~f^{-1}(f(R))}$ always hold.
6. ${\displaystyle L\cap f^{-1}(f(R))~=~R\cap f^{-1}(f(L))}$
	- If this above set equality holds, then this set will also be equal to both ${\displaystyle L\cap R\cap \operatorname {domain} f}$ and ${\displaystyle L\cap R\cap f^{-1}(f(L\cap R)).}$
7. ${\displaystyle L\cap f^{-1}(f(L\cap R))~=~R\cap f^{-1}(f(L\cap R))}$ and ${\displaystyle f(L\cap R)~\supseteq ~f(L)\cap f(R).}$

*Necessary conditions for equality* (excluding characterizations): If equality holds then the following are necessarily true:

1. ${\displaystyle f(L\cap R)=f(L)\cap f(R),}$ or equivalently ${\displaystyle f(L\cap R)\supseteq f(L)\cap f(R).}$
2. ${\displaystyle L\cap f^{-1}(f(L\cap R))~=~R\cap f^{-1}(f(L\cap R))}$

*Sufficient conditions for equality*: Equality holds if any of the following are true:

1. ${\displaystyle f}$ is injective.
2. The restriction ${\displaystyle f{\big \vert }_{L\cup R}}$ is injective.

#### Exact formulas/equalities for images of set operations

##### Formulas for f(L\\R) =

For any function ${\displaystyle f:X\to Y}$ and any sets ${\displaystyle L}$ and ${\displaystyle R,}$ [^10] 
$$
{\displaystyle {\begin{alignedat}{4}f(L\setminus R)&=Y~~~\;\,\,\setminus \left\{y\in Y~~~~~~~~~~\;\,~:~L\cap f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(L)\setminus \left\{y\in f(L)~~~~~~~\,~:~L\cap f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(L)\setminus \left\{y\in f(L\cap R)~:~L\cap f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(L)\setminus \left\{y\in V~~~~~~~~~~~~\,~:~L\cap f^{-1}(y)\subseteq R\right\}\qquad &&{\text{ for any superset }}\quad V\supseteq f(L\cap R)\\[0.4ex]&=f(S)\setminus \left\{y\in f(S)~~~~~~~\,~:~L\cap f^{-1}(y)\subseteq R\right\}\qquad &&{\text{ for any superset }}\quad S\supseteq L\cap X.\\[0.7ex]\end{alignedat}}}
$$

##### Formulas for f(X\\R) =

Taking ${\displaystyle L:=X=\operatorname {domain} f}$ in the above formulas gives: 
$$
{\displaystyle {\begin{alignedat}{4}f(X\setminus R)&=Y~~~\;\,\,\setminus \left\{y\in Y~~~~\;\,\,:~f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(X)\setminus \left\{y\in f(X)~:~f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(X)\setminus \left\{y\in f(R)~:~f^{-1}(y)\subseteq R\right\}\\[0.4ex]&=f(X)\setminus \left\{y\in W~~~\;\,\,:~f^{-1}(y)\subseteq R\right\}\qquad {\text{ for any superset }}\quad W\supseteq f(R)\\[0.4ex]\end{alignedat}}}
$$
 where the set ${\displaystyle \left\{y\in f(R):f^{-1}(y)\subseteq R\right\}}$ is equal to the image under ${\displaystyle f}$ of the largest ${\displaystyle f}$ -saturated subset of ${\displaystyle R.}$

- In general, only ${\displaystyle f(X\setminus R)\,\supseteq \,f(X)\setminus f(R)}$ always holds and equality is not guaranteed; but replacing " ${\displaystyle f(R)}$ " with its subset " ${\displaystyle \left\{y\in f(R):f^{-1}(y)\subseteq R\right\}}$ " results in a formula in which equality is *always* guaranteed: 
	$$
	{\displaystyle f(X\setminus R)\,=\,f(X)\setminus \left\{y\in f(R):f^{-1}(y)\subseteq R\right\}.}
	$$
	 From this it follows that:[^9] 
	$$
	{\displaystyle f(X\setminus R)=f(X)\setminus f(R)\quad {\text{ if and only if }}\quad f(R)=\left\{y\in f(R):f^{-1}(y)\subseteq R\right\}\quad {\text{ if and only if }}\quad f^{-1}(f(R))\subseteq R.}
	$$
- If ${\displaystyle f_{R}:=\left\{y\in f(X):f^{-1}(y)\subseteq R\right\}}$ then ${\displaystyle f(X\setminus R)=f(X)\setminus f_{R},}$ which can be written more symmetrically as ${\displaystyle f(X\setminus R)=f_{X}\setminus f_{R}}$ (since ${\displaystyle f_{X}=f(X)}$).

##### Formulas for f(L∆R) =

It follows from ${\displaystyle L\,\triangle \,R=(L\cup R)\setminus (L\cap R)}$ and the above formulas for the image of a set subtraction that for any function ${\displaystyle f:X\to Y}$ and any sets ${\displaystyle L}$ and ${\displaystyle R,}$ 
$$
{\displaystyle {\begin{alignedat}{4}f(L\,\triangle \,R)&=Y~~~\;~~~\;~~~\;\setminus \left\{y\in Y~~~\,~~~\;~~~\,~~:~L\cap f^{-1}(y)=R\cap f^{-1}(y)\right\}\\[0.4ex]&=f(L\cup R)\setminus \left\{y\in f(L\cup R)~:~L\cap f^{-1}(y)=R\cap f^{-1}(y)\right\}\\[0.4ex]&=f(L\cup R)\setminus \left\{y\in f(L\cap R)~:~L\cap f^{-1}(y)=R\cap f^{-1}(y)\right\}\\[0.4ex]&=f(L\cup R)\setminus \left\{y\in V~~~\,~~~~~~~~~~:~L\cap f^{-1}(y)=R\cap f^{-1}(y)\right\}\qquad &&{\text{ for any superset }}\quad V\supseteq f(L\cap R)\\[0.4ex]&=f(S)~~\,~~~\,~\,\setminus \left\{y\in f(S)~~~\,~~~\;~:~L\cap f^{-1}(y)=R\cap f^{-1}(y)\right\}\qquad &&{\text{ for any superset }}\quad S\supseteq (L\cup R)\cap X.\\[0.7ex]\end{alignedat}}}
$$

##### Formulas for f(L) =

It follows from the above formulas for the image of a set subtraction that for any function ${\displaystyle f:X\to Y}$ and any set ${\displaystyle L,}$ 
$$
{\displaystyle {\begin{alignedat}{4}f(L)&=Y~~~\;\,\setminus \left\{y\in Y~~~\;\,~:~f^{-1}(y)\cap L=\varnothing \right\}\\[0.4ex]&=\operatorname {Im} f\setminus \left\{y\in \operatorname {Im} f~:~f^{-1}(y)\cap L=\varnothing \right\}\\[0.4ex]&=W~~~\,\setminus \left\{y\in W~~\;\,~:~f^{-1}(y)\cap L=\varnothing \right\}\qquad {\text{ for any superset }}\quad W\supseteq f(L)\\[0.7ex]\end{alignedat}}}
$$

This is more easily seen as being a consequence of the fact that for any ${\displaystyle y\in Y,}$ ${\displaystyle f^{-1}(y)\cap L=\varnothing }$ if and only if ${\displaystyle y\not \in f(L).}$

##### Formulas for f(L⋂R) =

It follows from the above formulas for the image of a set that for any function ${\displaystyle f:X\to Y}$ and any sets ${\displaystyle L}$ and ${\displaystyle R,}$ 
$$
{\displaystyle {\begin{alignedat}{4}f(L\cap R)&=Y~~~~~\setminus \left\{y\in Y~~~~~~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}&&\\[0.4ex]&=f(L)\setminus \left\{y\in f(L)~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}&&\\[0.4ex]&=f(L)\setminus \left\{y\in U~~~~~~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}\qquad &&{\text{ for any superset }}\quad U\supseteq f(L)\\[0.4ex]&=f(R)\setminus \left\{y\in f(R)~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}&&\\[0.4ex]&=f(R)\setminus \left\{y\in V~~~~~~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}\qquad &&{\text{ for any superset }}\quad V\supseteq f(R)\\[0.4ex]&=f(L)\cap f(R)\setminus \left\{y\in f(L)\cap f(R)~:~L\cap R\cap f^{-1}(y)=\varnothing \right\}&&\\[0.7ex]\end{alignedat}}}
$$
 where moreover, for any ${\displaystyle y\in Y,}$

${\displaystyle L\cap f^{-1}(y)\subseteq L\setminus R~}$ if and only if ${\displaystyle ~L\cap R\cap f^{-1}(y)=\varnothing ~}$ if and only if ${\displaystyle ~R\cap f^{-1}(y)\subseteq R\setminus L~}$ if and only if ${\displaystyle ~y\not \in f(L\cap R).}$

The sets ${\displaystyle U}$ and ${\displaystyle V}$ mentioned above could, in particular, be any of the sets ${\displaystyle f(L\cup R),\;\operatorname {Im} f,}$ or ${\displaystyle Y,}$ for example.

### (Pre)Images of set operations on (pre)images

Let ${\displaystyle L}$ and ${\displaystyle R}$ be arbitrary sets, ${\displaystyle f:X\to Y}$ be any map, and let ${\displaystyle A\subseteq X}$ and ${\displaystyle C\subseteq Y.}$

| Image of preimage | Preimage of image | Additional assumptions on sets |
| --- | --- | --- |
| ${\displaystyle f\left(f^{-1}(L)\cap R\right)=L\cap f(R)}$ [^15] | ${\displaystyle f^{-1}(f(L)\cap R)~\supseteq ~L\cap f^{-1}(R)}$ | None |
| ${\displaystyle f\left(f^{-1}(L)\cup R\right)~=~(L\cap \operatorname {Im} f)\cup f(R)~\subseteq ~L\cup f(R)}$ | ${\displaystyle f^{-1}(f(A)\cup R)~\supseteq ~A\cup f^{-1}(R)}$ [^18]    Equality holds if any of the following are true:  1. ${\displaystyle f(A)\subseteq R.}$ 2. ${\displaystyle A\subseteq f^{-1}(R).}$ | ${\displaystyle A\subseteq X}$ |

**(Pre)Images of operations on images**

Since ${\displaystyle f(L)\setminus f(L\setminus R)~=~\left\{y\in f(L\cap R)~:~L\cap f^{-1}(y)\subseteq R\right\},}$

$$
{\displaystyle {\begin{alignedat}{4}f^{-1}(f(L)\setminus f(L\setminus R))&=&&f^{-1}\left(\left\{y\in f(L\cap R)~:~L\cap f^{-1}(y)\subseteq R\right\}\right)\\&=&&\left\{x\in f^{-1}(f(L\cap R))~:~L\cap f^{-1}(f(x))\subseteq R\right\}\\\end{alignedat}}}
$$

Since ${\displaystyle f(X)\setminus f(L\setminus R)~=~\left\{y\in f(X)~:~L\cap f^{-1}(y)\subseteq R\right\},}$ 
$$
{\displaystyle {\begin{alignedat}{4}f^{-1}(Y\setminus f(L\setminus R))&~=~&&f^{-1}(f(X)\setminus f(L\setminus R))\\&=&&f^{-1}\left(\left\{y\in f(X)~:~L\cap f^{-1}(y)\subseteq R\right\}\right)\\&=&&\left\{x\in X~:~L\cap f^{-1}(f(x))\subseteq R\right\}\\&~=~&&X\setminus f^{-1}(f(L\setminus R))\\\end{alignedat}}}
$$

Using ${\displaystyle L:=X,}$ this becomes ${\displaystyle ~f(X)\setminus f(X\setminus R)~=~\left\{y\in f(R)~:~f^{-1}(y)\subseteq R\right\}~}$ and 
$$
{\displaystyle {\begin{alignedat}{4}f^{-1}(Y\setminus f(X\setminus R))&~=~&&f^{-1}(f(X)\setminus f(X\setminus R))\\&=&&f^{-1}\left(\left\{y\in f(R)~:~f^{-1}(y)\subseteq R\right\}\right)\\&=&&\left\{r\in R\cap X~:~f^{-1}(f(r))\subseteq R\right\}\\&\subseteq &&R\\\end{alignedat}}}
$$
 and so 
$$
{\displaystyle {\begin{alignedat}{4}f^{-1}(Y\setminus f(L))&~=~&&f^{-1}(f(X)\setminus f(L))\\&=&&f^{-1}\left(\left\{y\in f(X\setminus L)~:~f^{-1}(y)\cap L=\varnothing \right\}\right)\\&=&&\{x\in X\setminus L~:~f(x)\not \in f(L)\}\\&=&&X\setminus f^{-1}(f(L))\\&\subseteq &&X\setminus L\\\end{alignedat}}}
$$

### (Pre)Images and Cartesian products Π

Let ${\displaystyle \prod Y_{\bullet }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\prod _{j\in J}Y_{j}}$ and for every ${\displaystyle k\in J,}$ let 
$$
{\displaystyle \pi _{k}~:~\prod _{j\in J}Y_{j}~\to ~Y_{k}}
$$
 denote the canonical projection onto ${\displaystyle Y_{k}.}$

**Definitions**

Given a collection of maps ${\displaystyle F_{j}:X\to Y_{j}}$ indexed by ${\displaystyle j\in J,}$ define the map 
$$
{\displaystyle {\begin{alignedat}{4}\left(F_{j}\right)_{j\in J}:\;&&X&&\;\to \;&\prod _{j\in J}Y_{j}\\[0.3ex]&&x&&\;\mapsto \;&\left(F_{j}\left(x_{j}\right)\right)_{j\in J},\\\end{alignedat}}}
$$
 which is also denoted by ${\displaystyle F_{\bullet }=\left(F_{j}\right)_{j\in J}.}$ This is the unique map satisfying 
$$
{\displaystyle \pi _{j}\circ F_{\bullet }=F_{j}\quad {\text{ for all }}j\in J.}
$$

Conversely, if given a map 
$$
{\displaystyle F~:~X~\to ~\prod _{j\in J}Y_{j}}
$$
 then ${\displaystyle F=\left(\pi _{j}\circ F\right)_{j\in J}.}$ Explicitly, what this means is that if 
$$
{\displaystyle F_{k}~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\pi _{k}\circ F~:~X~\to ~Y_{k}}
$$
 is defined for every ${\displaystyle k\in J,}$ then ${\displaystyle F}$ the unique map satisfying: ${\displaystyle \pi _{j}\circ F=F_{j}}$ for all ${\displaystyle j\in J;}$ or said more briefly, ${\displaystyle F=\left(F_{j}\right)_{j\in J}.}$

The map ${\displaystyle F_{\bullet }=\left(F_{j}\right)_{j\in J}~:~X~\to ~\prod _{j\in J}Y_{j}}$ should not be confused with the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") ${\displaystyle \prod _{j\in J}F_{j}}$ of these maps, which is by definition is the map 
$$
{\displaystyle {\begin{alignedat}{4}\prod _{j\in J}F_{j}:\;&&\prod _{j\in J}X&&~\;\to \;~&\prod _{j\in J}Y_{j}\\[0.3ex]&&\left(x_{j}\right)_{j\in J}&&~\;\mapsto \;~&\left(F_{j}\left(x_{j}\right)\right)_{j\in J}\\\end{alignedat}}}
$$
 with domain ${\displaystyle \prod _{j\in J}X=X^{J}}$ rather than ${\displaystyle X.}$

**Preimage and images of a Cartesian product**

Suppose ${\displaystyle F_{\bullet }=\left(F_{j}\right)_{j\in J}~:~X~\to ~\prod _{j\in J}Y_{j}.}$

If ${\displaystyle A~\subseteq ~X}$ then 
$$
{\displaystyle F_{\bullet }(A)~~\;\color {Red}{\subseteq }\color {Black}{}\;~~\prod _{j\in J}F_{j}(A).}
$$

If ${\displaystyle B~\subseteq ~\prod _{j\in J}Y_{j}}$ then 
$$
{\displaystyle F_{\bullet }^{-1}(B)~~\;\color {Red}{\subseteq }\color {Black}{}\;~~\bigcap _{j\in J}F_{j}^{-1}\left(\pi _{j}(B)\right)}
$$
 where equality will hold if ${\displaystyle B=\prod _{j\in J}\pi _{j}(B),}$ in which case ${\textstyle F_{\bullet }^{-1}(B)=\displaystyle \bigcap _{j\in J}F_{j}^{-1}\left(\pi _{j}(B)\right)}$ and

| $$ {\displaystyle F_{\bullet }^{-1}\left(\prod _{j\in J}\pi _{j}(B)\right)~=~\bigcap _{j\in J}F_{j}^{-1}\left(\pi _{j}(B)\right).} $$ |  | Eq. 11a |
| --- | --- | --- |

For equality to hold, it suffices for there to exist a family ${\displaystyle \left(B_{j}\right)_{j\in J}}$ of subsets ${\displaystyle B_{j}\subseteq Y_{j}}$ such that ${\displaystyle B=\prod _{j\in J}B_{j},}$ in which case:

| $$ {\displaystyle F_{\bullet }^{-1}\left(\prod _{j\in J}B_{j}\right)~=~\bigcap _{j\in J}F_{j}^{-1}\left(B_{j}\right)} $$ |  | Eq. 11b |
| --- | --- | --- |

and ${\displaystyle \pi _{j}(B)=B_{j}}$ for all ${\displaystyle j\in J.}$

### (Pre)Image of a single set

| Image | Preimage | Additional assumptions |
| --- | --- | --- |
| ${\displaystyle {\begin{alignedat}{4}f(L)&=f(L\cap \operatorname {domain} f)\\&=f(L\cap X)\\&=Y~~~~\,\setminus \left\{y\in Y~~~~\,:f^{-1}(y)\subseteq X\setminus L\right\}\\&=\operatorname {Im} f\setminus \left\{y\in \operatorname {Im} f:f^{-1}(y)\subseteq X\setminus L\right\}\\\end{alignedat}}}$ | ${\displaystyle {\begin{alignedat}{4}f^{-1}(L)&=f^{-1}(L\cap \operatorname {Im} f)\\&=f^{-1}(L\cap Y)\end{alignedat}}}$ | None |
| ${\displaystyle f(X)=\operatorname {Im} f\subseteq Y}$ | ${\displaystyle {\begin{alignedat}{4}f^{-1}(Y)&=X\\f^{-1}(\operatorname {Im} f)&=X\end{alignedat}}}$ | None |
| ${\displaystyle {\begin{alignedat}{4}f(L)&=f(L\cap R~&&\cup ~&&(&&L\setminus R))\\&=f(L\cap R)~&&\cup ~f&&(&&L\setminus R)\end{alignedat}}}$ | ${\displaystyle {\begin{alignedat}{4}f^{-1}(L)&=f^{-1}(L\cap R&&\cup &&(&&L&&\setminus &&R))\\&=f^{-1}(L\cap R)&&\cup f^{-1}&&(&&L&&\setminus &&R)\\&=f^{-1}(L\cap R)&&\cup f^{-1}&&(&&L&&\setminus [&&R\cap \operatorname {Im} f])\\&=f^{-1}(L\cap R)&&\cup f^{-1}&&([&&L\cap \operatorname {Im} f]&&\setminus &&R)\\&=f^{-1}(L\cap R)&&\cup f^{-1}&&([&&L\cap \operatorname {Im} f]&&\setminus [&&R\cap \operatorname {Im} f])\end{alignedat}}}$ | None |
| ${\displaystyle \operatorname {Im} f=f(X)~=~f(L)\cup f(X\setminus L)}$ | ${\displaystyle {\begin{alignedat}{4}X&=f^{-1}(L)\cup f^{-1}(Y&&\setminus L)\\&=f^{-1}(L)\cup f^{-1}(\operatorname {Im} f&&\setminus L)\end{alignedat}}}$ | None |
| ${\displaystyle f{\big \vert }_{L}(R)=f(L\cap R)}$ | ${\displaystyle \left(f{\big \vert }_{L}\right)^{-1}(R)=L\cap f^{-1}(R)}$ | None |
| ${\displaystyle (g\circ f)(L)~=~g(f(L))}$ | ${\displaystyle (g\circ f)^{-1}(L)~=~f^{-1}\left(g^{-1}(L)\right)}$ | None (${\displaystyle f}$ and ${\displaystyle g}$ are arbitrary functions). |
| ${\displaystyle f\left(f^{-1}(L)\right)=L\cap \operatorname {Im} f}$ | ${\displaystyle f^{-1}(f(L))~\supseteq ~L\cap f^{-1}(\operatorname {Im} f)=L\cap f^{-1}(Y)}$ [^15] | None |
| ${\displaystyle f\left(f^{-1}(Y)\right)=f\left(f^{-1}(\operatorname {Im} f)\right)=f(X)}$ | ${\displaystyle f^{-1}(f(X))=f^{-1}(\operatorname {Im} f)=X}$ | None |
| ${\displaystyle f\left(f^{-1}(f(L))\right)=f(L)}$ | ${\displaystyle f^{-1}\left(f\left(f^{-1}(L)\right)\right)=f^{-1}(L)}$ | None |

#### Containments ⊆ and intersections ⋂ of images and preimages

**Equivalences and implications of images and preimages**

| Image | Preimage | Additional assumptions on sets |
| --- | --- | --- |
| ${\displaystyle f(L)\subseteq \operatorname {Im} f\subseteq Y}$ | ${\displaystyle f^{-1}(L)=X}$ if and only if ${\displaystyle \operatorname {Im} f\subseteq L}$ | None |
| ${\displaystyle f(L)=\varnothing }$ if and only if ${\displaystyle L\cap \operatorname {domain} f=\varnothing }$ | ${\displaystyle f^{-1}(L)=\varnothing }$ if and only if ${\displaystyle L\cap \operatorname {Im} f=\varnothing }$ | None |
| ${\displaystyle f(A)=\varnothing }$ if and only if ${\displaystyle A=\varnothing }$ | ${\displaystyle f^{-1}(C)=\varnothing }$ if and only if ${\displaystyle C\subseteq Y\setminus \operatorname {Im} f}$ | ${\displaystyle A\subseteq X}$ and ${\displaystyle C\subseteq Y}$ |
| ${\displaystyle L\subseteq R}$ implies ${\displaystyle f(L)\subseteq f(R)}$ [^15] | ${\displaystyle L\subseteq R}$ implies ${\displaystyle f^{-1}(L)\subseteq f^{-1}(R)}$ [^15] | None |
| The following are equivalent: 1. ${\displaystyle f(L)\subseteq f(R)}$ 2. ${\displaystyle f(L\cup R)=f(R)}$ 3. ${\displaystyle L\cap \operatorname {domain} f~\subseteq ~f^{-1}(f(R))}$ | The following are equivalent: 1. ${\displaystyle f^{-1}(L)\subseteq f^{-1}(R)}$ 2. ${\displaystyle f^{-1}(L\cup R)=f^{-1}(R)}$ 3. ${\displaystyle L\cap \operatorname {Im} f\subseteq R}$  If ${\displaystyle C~\subseteq ~\operatorname {Im} f}$ then ${\displaystyle f^{-1}(C)~\subseteq ~f^{-1}(R)}$ if and only if ${\displaystyle C~\subseteq ~R.}$ | ${\displaystyle C\subseteq \operatorname {Im} f}$ |
| The following are equivalent when ${\displaystyle C\subseteq Y:}$  1. ${\displaystyle C\subseteq f(R)}$ 2. ${\displaystyle f(B)=C}$ for some ${\displaystyle B\subseteq R}$ 3. ${\displaystyle f(B)=C}$ for some ${\displaystyle B\subseteq R\cap \operatorname {domain} f}$ | The following are equivalent: 1. ${\displaystyle L\subseteq f^{-1}(R)}$ 2. ${\displaystyle f(L)\subseteq R}$ and ${\displaystyle L\subseteq \operatorname {domain} f}$  The following are equivalent when ${\displaystyle A\subseteq X:}$  1. ${\displaystyle A\subseteq f^{-1}(R)}$ 2. ${\displaystyle f(A)\subseteq R}$ | ${\displaystyle A\subseteq X}$ and ${\displaystyle C\subseteq Y}$ |
| The following are equivalent: 1. ${\displaystyle f(A)~\supseteq ~f(X\setminus A)}$ 2. ${\displaystyle f(A)=\operatorname {Im} f}$ | The following are equivalent: 1. ${\displaystyle f^{-1}(C)~\supseteq ~f^{-1}(Y\setminus C)}$ 2. ${\displaystyle f^{-1}(C)=X}$ | ${\displaystyle A\subseteq X}$ and ${\displaystyle C\subseteq Y}$ |
| ${\displaystyle f\left(f^{-1}(L)\right)\subseteq L}$ [^15]    Equality holds if *and only if* the following is true:  1. ${\displaystyle L\subseteq \operatorname {Im} f.}$ [^19] [^20]  Equality holds if any of the following are true:  1. ${\displaystyle L\subseteq Y}$ and ${\displaystyle f:X\to Y}$ is surjective. | ${\displaystyle f^{-1}(f(A))\supseteq A}$    Equality holds if *and only if* the following is true:  1. ${\displaystyle A}$ is ${\displaystyle f}$ -saturated.  Equality holds if any of the following are true:  1. ${\displaystyle f}$ is injective.[^19] [^20] | ${\displaystyle A\subseteq X}$ |

**Intersection of a set and a (pre)image**

The following statements are equivalent:

1. ${\displaystyle \varnothing =f(L)\cap R}$
2. ${\displaystyle \varnothing =L\cap f^{-1}(R)}$ [^15]
3. ${\displaystyle \varnothing =f^{-1}(f(L))\cap f^{-1}(R)}$
4. ${\displaystyle \varnothing =f^{-1}(f(L)\cap R)}$

Thus for any ${\displaystyle t,}$ [^15] 
$$
{\displaystyle t\not \in f(L)\quad {\text{ if and only if }}\quad L\cap f^{-1}(t)=\varnothing .}
$$

## Sequences and collections of families of sets

### Definitions

A *[family of sets](https://en.wikipedia.org/wiki/Family_of_sets "Family of sets")* or simply a *family* is a set whose elements are sets. A *family over ${\displaystyle X}$* is a family of subsets of ${\displaystyle X.}$

The *[power set](https://en.wikipedia.org/wiki/Power_set "Power set")* of a set ${\displaystyle X}$ is the set of all subsets of ${\displaystyle X}$: 
$$
{\displaystyle {\mathcal {P}}(X)~\colon =~\{\;S~:~S\subseteq X\;\}.}
$$

**Notation for sequences of sets**

Throughout, ${\displaystyle S{\text{ and }}T}$ will be arbitrary sets and ${\displaystyle S_{\bullet }}$ and will denote a [net](https://en.wikipedia.org/wiki/Net_\(mathematics\) "Net (mathematics)") or a [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence") of sets where if it is a sequence then this will be indicated by either of the notations 
$$
{\displaystyle S_{\bullet }=\left(S_{i}\right)_{i=1}^{\infty }\qquad {\text{ or }}\qquad S_{\bullet }=\left(S_{i}\right)_{i\in \mathbb {N} }}
$$
 where ${\displaystyle \mathbb {N} }$ denotes the [natural numbers](https://en.wikipedia.org/wiki/Natural_numbers "Natural numbers"). A notation ${\displaystyle S_{\bullet }=\left(S_{i}\right)_{i\in I}}$ indicates that ${\displaystyle S_{\bullet }}$ is a [net](https://en.wikipedia.org/wiki/Net_\(mathematics\) "Net (mathematics)") [directed](https://en.wikipedia.org/wiki/Directed_set "Directed set") by ${\displaystyle (I,\leq ),}$ which (by definition) is a [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence") if the set ${\displaystyle I,}$ which is called the net's [indexing set](https://en.wikipedia.org/wiki/Indexing_set "Indexing set"), is the natural numbers (that is, if ${\displaystyle I=\mathbb {N} }$) and ${\displaystyle \,\leq \,}$ is the natural order on ${\displaystyle \mathbb {N} .}$

**Disjoint and monotone sequences of sets**

If ${\displaystyle S_{i}\cap S_{j}=\varnothing }$ for all distinct indices ${\displaystyle i\neq j}$ then ${\displaystyle S_{\bullet }}$ is called a *[pairwise disjoint](https://en.wikipedia.org/wiki/Pairwise_disjoint "Pairwise disjoint")* or simply a *disjoint*. A sequence or net ${\displaystyle S_{\bullet }}$ of set is called *[increasing](https://en.wikipedia.org/wiki/Increasing "Increasing")* or *non-decreasing* if (resp. *[decreasing](https://en.wikipedia.org/wiki/Decreasing "Decreasing")* or *[non-increasing](https://en.wikipedia.org/wiki/Non-increasing "Non-increasing")*) if for all indices ${\displaystyle i\leq j,}$ ${\displaystyle S_{i}\subseteq S_{j}}$ (resp. ${\displaystyle S_{i}\supseteq S_{j}}$). A sequence or net ${\displaystyle S_{\bullet }}$ of set is called *[strictly increasing](https://en.wikipedia.org/wiki/Strictly_increasing "Strictly increasing")* (resp. *[strictly decreasing](https://en.wikipedia.org/wiki/Strictly_decreasing "Strictly decreasing")*) if it is non-decreasing (resp. is non-increasing) and also ${\displaystyle S_{i}\neq S_{j}}$ for all *distinct* indices ${\displaystyle i{\text{ and }}j.}$ It is called *[monotone](https://en.wikipedia.org/wiki/Monotone_sequence "Monotone sequence")* if it is non-decreasing or non-increasing and it is called *strictly monotone* if it is strictly increasing or strictly decreasing.

A sequences or net ${\displaystyle S_{\bullet }}$ is said to *increase to ${\displaystyle S,}$* denoted by ${\displaystyle S_{\bullet }\uparrow S}$ [^21] or ${\displaystyle S_{\bullet }\nearrow S,}$ if ${\displaystyle S_{\bullet }}$ is increasing and the union of all ${\displaystyle S_{i}}$ is ${\displaystyle S;}$ that is, if 
$$
{\displaystyle \bigcup _{n}S_{n}=S\qquad {\text{ and }}\qquad S_{i}\subseteq S_{j}\quad {\text{ whenever }}i\leq j.}
$$
 It is said to *decrease to ${\displaystyle S,}$* denoted by ${\displaystyle S_{\bullet }\downarrow S}$ [^21] or ${\displaystyle S_{\bullet }\searrow S,}$ if ${\displaystyle S_{\bullet }}$ is increasing and the intersection of all ${\displaystyle S_{i}}$ is ${\displaystyle S}$ that is, if 
$$
{\displaystyle \bigcap _{n}S_{n}=S\qquad {\text{ and }}\qquad S_{i}\supseteq S_{j}\quad {\text{ whenever }}i\leq j.}
$$

**Definitions of elementwise operations on families**

If ${\displaystyle {\mathcal {L}}{\text{ and }}{\mathcal {R}}}$ are families of sets and if ${\displaystyle S}$ is any set then define:[^22] 
$$
{\displaystyle {\mathcal {L}}\;(\cup )\;{\mathcal {R}}~\colon =~\{~L\cup R~:~L\in {\mathcal {L}}~{\text{ and }}~R\in {\mathcal {R}}~\}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cap )\;{\mathcal {R}}~\colon =~\{~L\cap R~:~L\in {\mathcal {L}}~{\text{ and }}~R\in {\mathcal {R}}~\}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\setminus )\;{\mathcal {R}}~\colon =~\{~L\setminus R~:~L\in {\mathcal {L}}~{\text{ and }}~R\in {\mathcal {R}}~\}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\triangle )\;{\mathcal {R}}~\colon =~\{~L\;\triangle \;R~:~L\in {\mathcal {L}}~{\text{ and }}~R\in {\mathcal {R}}~\}}
$$
 
$$
{\displaystyle {\mathcal {L}}{\big \vert }_{S}~\colon =~\{L\cap S~:~L\in {\mathcal {L}}\}={\mathcal {L}}\;(\cap )\;\{S\}}
$$
 which are respectively called ***elementwise* *union***, ***elementwise* *intersection***, ***elementwise*** (***set***) ***difference***, ***elementwise* *symmetric difference***, and the ***trace*** / ***restriction of ${\displaystyle {\mathcal {L}}}$ to ${\displaystyle S.}$*** The regular union, intersection, and set difference are all defined as usual and are denoted with their usual notation: ${\displaystyle {\mathcal {L}}\cup {\mathcal {R}},{\mathcal {L}}\cap {\mathcal {R}},{\mathcal {L}}\;\triangle \;{\mathcal {R}},}$ and ${\displaystyle {\mathcal {L}}\setminus {\mathcal {R}},}$ respectively. These elementwise operations on families of sets play an important role in, among other subjects, the theory of [filters](https://en.wikipedia.org/wiki/Filter_on_a_set "Filter on a set") and prefilters on sets.

The *[upward closure](https://en.wikipedia.org/wiki/Upward_closed_set "Upward closed set") in ${\displaystyle X}$* of a family ${\displaystyle {\mathcal {L}}\subseteq {\mathcal {P}}(X)}$ is the family: 
$$
{\displaystyle {\mathcal {L}}^{\uparrow X}~\colon =~\bigcup _{L\in {\mathcal {L}}}\{\;S~:~L\subseteq S\subseteq X\;\}~=~\{\;S\subseteq X~:~{\text{ there exists }}L\in {\mathcal {L}}{\text{ such that }}L\subseteq S\;\}}
$$
 and the *downward closure of ${\displaystyle {\mathcal {L}}}$* is the family: 
$$
{\displaystyle {\mathcal {L}}^{\downarrow }~\colon =~\bigcup _{L\in {\mathcal {L}}}{\mathcal {P}}(L)~=~\{\;S~:~{\text{ there exists }}L\in {\mathcal {L}}{\text{ such that }}S\subseteq L\;\}.}
$$

#### Definitions of categories of families of sets

The following table lists some well-known categories of families of sets having applications in [general topology](https://en.wikipedia.org/wiki/General_topology "General topology") and [measure theory](https://en.wikipedia.org/wiki/Measure_theory "Measure theory").

<table><tbody><tr><th colspan="11"><a href="https://en.wikipedia.org/wiki/Family_of_sets">Families <math>{\displaystyle {\mathcal {F}}}</math> of sets</a> over <math>{\displaystyle \Omega }</math><div><ul><li><a href="https://en.wikipedia.org/wiki/Template:Families_of_sets"><abbr>v</abbr></a></li><li><a href="https://en.wikipedia.org/wiki/Template_talk:Families_of_sets"><abbr>t</abbr></a></li><li><a href="https://en.wikipedia.org/wiki/Special:EditPage/Template:Families_of_sets"><abbr>e</abbr></a></li></ul></div></th></tr><tr><th>Is necessarily true of <math>{\displaystyle {\mathcal {F}}\colon }</math><br>or, is <math>{\displaystyle {\mathcal {F}}}</math> <a href="https://en.wikipedia.org/wiki/Closure_(mathematics)">closed under:</a></th><td><a href="https://en.wikipedia.org/wiki/Directed_set">Directed<br>by <math>{\displaystyle \,\supseteq }</math></a></td><td><math>{\displaystyle A\cap B}</math></td><td><math>{\displaystyle A\cup B}</math></td><td><math>{\displaystyle B\setminus A}</math></td><td><math>{\displaystyle \Omega \setminus A}</math></td><td><math>{\displaystyle A_{1}\cap A_{2}\cap \cdots }</math></td><td><math>{\displaystyle A_{1}\cup A_{2}\cup \cdots }</math></td><td><math>{\displaystyle \Omega \in {\mathcal {F}}}</math></td><td><math>{\displaystyle \varnothing \in {\mathcal {F}}}</math></td><td><a href="https://en.wikipedia.org/wiki/Finite_intersection_property">F.I.P.</a></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Pi-system">π-system</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Ring_of_sets#semiring">Semiring</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Ring_of_sets#semialgebra">Semialgebra (semifield)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Monotone_class">Monotone class</a></th><td></td><td></td><td></td><td></td><td></td><td>only if <math>{\displaystyle A_{i}\searrow }</math></td><td>only if <math>{\displaystyle A_{i}\nearrow }</math></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Dynkin_system">𝜆-system (Dynkin system)</a></th><td></td><td></td><td></td><td>only if<br><math>{\displaystyle A\subseteq B}</math></td><td></td><td></td><td>only if <math>{\displaystyle A_{i}\nearrow }</math> or<br>they are <a href="https://en.wikipedia.org/wiki/Disjoint_sets">disjoint</a></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Ring_of_sets">Ring (order theory)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Ring_of_sets">Ring (measure theory)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Delta-ring">δ-ring</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Sigma-ring">𝜎-ring</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Field_of_sets">Algebra (field)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/%CE%A3-algebra">𝜎-algebra (𝜎-field)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Filter_on_a_set">Filter</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Proper_filter_on_a_set">Proper filter</a></th><td></td><td></td><td></td><td>Never</td><td>Never</td><td></td><td></td><td></td><td>Never</td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Prefilter">Prefilter (filter base)</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Filter_subbase">Filter subbase</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Topology_(structure)">Open topology</a></th><td></td><td></td><td></td><td></td><td></td><td></td><td><br>(even arbitrary <math>{\displaystyle \cup }</math>)</td><td></td><td></td><td>Never</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Topology_(structure)">Closed topology</a></th><td></td><td></td><td></td><td></td><td></td><td><br>(even arbitrary <math>{\displaystyle \cap }</math>)</td><td></td><td></td><td></td><td>Never</td></tr><tr><th>Is necessarily true of <math>{\displaystyle {\mathcal {F}}\colon }</math><br>or, is <math>{\displaystyle {\mathcal {F}}}</math> <a href="https://en.wikipedia.org/wiki/Closure_(mathematics)">closed under:</a></th><td><a href="https://en.wikipedia.org/wiki/Directed_downward">directed<br>downward</a></td><td>finite<br>intersections</td><td>finite<br>unions</td><td>relative<br>complements</td><td>complements<br>in <math>{\displaystyle \Omega }</math></td><td>countable<br>intersections</td><td>countable<br>unions</td><td>contains <math>{\displaystyle \Omega }</math></td><td>contains <math>{\displaystyle \varnothing }</math></td><td><a href="https://en.wikipedia.org/wiki/Finite_intersection_property">Finite<br>intersection<br>property</a></td></tr><tr><td colspan="11"><p>Additionally, a <b><em><a href="https://en.wikipedia.org/wiki/Ring_of_sets#semiring">semiring</a></em></b> is a <a href="https://en.wikipedia.org/wiki/Pi-system">π-system</a> where every complement <math>{\displaystyle B\setminus A}</math> is equal to a finite <a href="https://en.wikipedia.org/wiki/Disjoint_union">disjoint union</a> of sets in <math>{\displaystyle {\mathcal {F}}.}</math><br>A <b><em><a href="https://en.wikipedia.org/wiki/Ring_of_sets#semialgebra">semialgebra</a></em></b> is a semiring where every complement <math>{\displaystyle \Omega \setminus A}</math> is equal to a finite <a href="https://en.wikipedia.org/wiki/Disjoint_union">disjoint union</a> of sets in <math>{\displaystyle {\mathcal {F}}.}</math><br><math>{\displaystyle A,B,A_{1},A_{2},\ldots }</math> are arbitrary elements of <math>{\displaystyle {\mathcal {F}}}</math> and it is assumed that <math>{\displaystyle {\mathcal {F}}\neq \varnothing.}</math><br></p></td></tr></tbody></table>

A family ${\displaystyle {\mathcal {L}}}$ is called *isotone*, *ascending*, or *[upward closed](https://en.wikipedia.org/wiki/Upward_closed_set "Upward closed set")* in ${\displaystyle X}$ if ${\displaystyle {\mathcal {L}}\subseteq {\mathcal {P}}(X)}$ and ${\displaystyle {\mathcal {L}}={\mathcal {L}}^{\uparrow X}.}$ [^22] A family ${\displaystyle {\mathcal {L}}}$ is called *downward closed* if ${\displaystyle {\mathcal {L}}={\mathcal {L}}^{\downarrow }.}$

A family ${\displaystyle {\mathcal {L}}}$ is said to be:

- *closed under finite intersections* (resp. *closed under finite unions*) if whenever ${\displaystyle L,R\in {\mathcal {L}}}$ then ${\displaystyle L\cap R\in {\mathcal {L}}}$ (respectively, ${\displaystyle L\cup R\in {\mathcal {L}}}$).
- *closed under [countable](https://en.wikipedia.org/wiki/Countable_set "Countable set") intersections* (resp. *closed under countable unions*) if whenever ${\displaystyle L_{1},L_{2},L_{3},\ldots }$ are elements of ${\displaystyle {\mathcal {L}}}$ then so is their intersections ${\displaystyle \bigcap _{i=1}^{\infty }L_{i}:=L_{1}\cap L_{2}\cap L_{3}\cap \cdots }$ (resp. so is their union ${\displaystyle \bigcup _{i=1}^{\infty }L_{i}:=L_{1}\cup L_{2}\cup L_{3}\cup \cdots }$).
- *closed under [complementation](https://en.wikipedia.org/wiki/Complement_\(set_theory\) "Complement (set theory)") in* (or *with respect to*) *${\displaystyle X}$* if whenever ${\displaystyle L\in {\mathcal {L}}}$ then ${\displaystyle X\setminus L\in {\mathcal {L}}.}$

A family ${\displaystyle {\mathcal {L}}}$ of sets is called a/an:

- *[π−system](https://en.wikipedia.org/wiki/Pi-system "Pi-system")* if ${\displaystyle {\mathcal {L}}\neq \varnothing }$ and ${\displaystyle {\mathcal {L}}}$ is closed under finite-intersections.
	- Every non-empty family ${\displaystyle {\mathcal {L}}}$ is contained in a unique smallest (with respect to ${\displaystyle \subseteq }$) π−system that is denoted by ${\displaystyle \pi ({\mathcal {L}})}$ and called *the π−system generated by ${\displaystyle {\mathcal {L}}.}$*
- *[filter subbase](https://en.wikipedia.org/wiki/Filter_subbase "Filter subbase")* and is said to have *the [finite intersection property](https://en.wikipedia.org/wiki/Finite_intersection_property "Finite intersection property")* if ${\displaystyle {\mathcal {L}}\neq \varnothing }$ and ${\displaystyle \varnothing \not \in \pi ({\mathcal {L}}).}$
- *[filter](https://en.wikipedia.org/wiki/Filter_on_a_set "Filter on a set") on ${\displaystyle X}$* if ${\displaystyle {\mathcal {L}}\neq \varnothing }$ is a family of subsets of ${\displaystyle X}$ that is a π−system, is upward closed in ${\displaystyle X,}$ and is also *proper*, which by definition means that it does not contain the empty set as an element.
- *prefilter* or *filter base* if it is a non-empty family of subsets of some set ${\displaystyle X}$ whose upward closure in ${\displaystyle X}$ is a filter on ${\displaystyle X.}$
- *[algebra on ${\displaystyle X}$](https://en.wikipedia.org/wiki/Field_of_sets "Field of sets")* is a non-empty family of subsets of ${\displaystyle X}$ that contains the empty set, forms a π−system, and is also closed under complementation with respect to ${\displaystyle X.}$
- *[σ-algebra](https://en.wikipedia.org/wiki/%CE%A3-algebra "Σ-algebra") on ${\displaystyle X}$* is an algebra on ${\displaystyle X}$ that is closed under countable unions (or equivalently, closed under countable intersections).

[Sequences](https://en.wikipedia.org/wiki/Sequence "Sequence") of sets often arise in [measure theory](https://en.wikipedia.org/wiki/Measure_theory "Measure theory").

**Algebra of sets**

A [family](https://en.wikipedia.org/wiki/Family_of_sets "Family of sets") ${\displaystyle \Phi }$ of subsets of a set ${\displaystyle X}$ is said to be ***[an algebra of sets](https://en.wikipedia.org/wiki/An_algebra_of_sets "An algebra of sets")*** if ${\displaystyle \varnothing \in \Phi }$ and for all ${\displaystyle L,R\in \Phi ,}$ all three of the sets ${\displaystyle X\setminus R,\,L\cap R,}$ and ${\displaystyle L\cup R}$ are elements of ${\displaystyle \Phi .}$ [^23] The [article on this topic](https://en.wikipedia.org/wiki/Algebra_of_sets "Algebra of sets") lists set identities and other relationships these three operations.

Every algebra of sets is also a [ring of sets](https://en.wikipedia.org/wiki/Ring_of_sets "Ring of sets") [^23] and a [π-system](https://en.wikipedia.org/wiki/Pi-system "Pi-system").

**Algebra generated by a family of sets**

Given any family ${\displaystyle {\mathcal {S}}}$ of subsets of ${\displaystyle X,}$ there is a unique smallest [^7] algebra of sets in ${\displaystyle X}$ containing ${\displaystyle {\mathcal {S}}.}$ [^23] It is called ***the algebra generated by ${\displaystyle {\mathcal {S}}}$*** and it will be denote it by ${\displaystyle \Phi _{\mathcal {S}}.}$ This algebra can be constructed as follows:[^23]

1. If ${\displaystyle {\mathcal {S}}=\varnothing }$ then ${\displaystyle \Phi _{\mathcal {S}}=\{\varnothing ,X\}}$ and we are done. Alternatively, if ${\displaystyle {\mathcal {S}}}$ is empty then ${\displaystyle {\mathcal {S}}}$ may be replaced with ${\displaystyle \{\varnothing \},\{X\},{\text{ or }}\{\varnothing ,X\}}$ and continue with the construction.
2. Let ${\displaystyle {\mathcal {S}}_{0}}$ be the family of all sets in ${\displaystyle {\mathcal {S}}}$ together with their complements (taken in ${\displaystyle X}$).
3. Let ${\displaystyle {\mathcal {S}}_{1}}$ be the family of all possible finite intersections of sets in ${\displaystyle {\mathcal {S}}_{0}.}$ [^8]
4. Then the algebra generated by ${\displaystyle {\mathcal {S}}}$ is the set ${\displaystyle \Phi _{\mathcal {S}}}$ consisting of all possible finite unions of sets in ${\displaystyle {\mathcal {S}}_{1}.}$

#### Elementwise operations on families

Let ${\displaystyle {\mathcal {L}},{\mathcal {M}},}$ and ${\displaystyle {\mathcal {R}}}$ be families of sets over ${\displaystyle X.}$ On the left hand sides of the following identities, ${\displaystyle {\mathcal {L}}}$ is the *L*  eft most family, ${\displaystyle {\mathcal {M}}}$ is in the *M*  iddle, and ${\displaystyle {\mathcal {R}}}$ is the *R*  ight most set.

**[Commutativity](https://en.wikipedia.org/wiki/Commutative_operation "Commutative operation")**:[^22] 
$$
{\displaystyle {\mathcal {L}}\;(\cup )\;{\mathcal {R}}={\mathcal {R}}\;(\cup )\;{\mathcal {L}}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cap )\;{\mathcal {R}}={\mathcal {R}}\;(\cap )\;{\mathcal {L}}}
$$

**[Associativity](https://en.wikipedia.org/wiki/Associativity "Associativity")**:[^22] 
$$
{\displaystyle [{\mathcal {L}}\;(\cup )\;{\mathcal {M}}]\;(\cup )\;{\mathcal {R}}={\mathcal {L}}\;(\cup )\;[{\mathcal {M}}\;(\cup )\;{\mathcal {R}}]}
$$
 
$$
{\displaystyle [{\mathcal {L}}\;(\cap )\;{\mathcal {M}}]\;(\cap )\;{\mathcal {R}}={\mathcal {L}}\;(\cap )\;[{\mathcal {M}}\;(\cap )\;{\mathcal {R}}]}
$$

**Identity**: 
$$
{\displaystyle {\mathcal {L}}\;(\cup )\;\{\varnothing \}={\mathcal {L}}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cap )\;\{X\}={\mathcal {L}}}
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\setminus )\;\{\varnothing \}={\mathcal {L}}}
$$

**Domination**: 
$$
{\displaystyle {\mathcal {L}}\;(\cup )\;\{X\}=\{X\}~~~~{\text{ if }}{\mathcal {L}}\neq \varnothing }
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cap )\;\{\varnothing \}=\{\varnothing \}~~~~{\text{ if }}{\mathcal {L}}\neq \varnothing }
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cup )\;\varnothing =\varnothing }
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\cap )\;\varnothing =\varnothing }
$$
 
$$
{\displaystyle {\mathcal {L}}\;(\setminus )\;\varnothing =\varnothing }
$$
 
$$
{\displaystyle \varnothing \;(\setminus )\;{\mathcal {R}}=\varnothing }
$$

### Power set

$$
{\displaystyle {\mathcal {P}}(L\cap R)~=~{\mathcal {P}}(L)\cap {\mathcal {P}}(R)}
$$
 
$$
{\displaystyle {\mathcal {P}}(L\cup R)~=~{\mathcal {P}}(L)\ (\cup )\ {\mathcal {P}}(R)~\supseteq ~{\mathcal {P}}(L)\cup {\mathcal {P}}(R).}
$$

If ${\displaystyle L}$ and ${\displaystyle R}$ are subsets of a vector space ${\displaystyle X}$ and if ${\displaystyle s}$ is a scalar then 
$$
{\displaystyle {\mathcal {P}}(sL)~=~s{\mathcal {P}}(L)}
$$
 
$$
{\displaystyle {\mathcal {P}}(L+R)~\supseteq ~{\mathcal {P}}(L)+{\mathcal {P}}(R).}
$$

### Sequences of sets

Suppose that ${\displaystyle L}$ is any set such that ${\displaystyle L\supseteq R_{i}}$ for every index ${\displaystyle i.}$ If ${\displaystyle R_{\bullet }}$ decreases to ${\displaystyle R}$ then ${\displaystyle L\setminus R_{\bullet }:=\left(L\setminus R_{i}\right)_{i}}$ increases to ${\displaystyle L\setminus R}$ [^21] whereas if instead ${\displaystyle R_{\bullet }}$ increases to ${\displaystyle R}$ then ${\displaystyle L\setminus R_{\bullet }}$ decreases to ${\displaystyle L\setminus R.}$

If ${\displaystyle L{\text{ and }}R}$ are arbitrary sets and if ${\displaystyle L_{\bullet }=\left(L_{i}\right)_{i}}$ increases (resp. decreases) to ${\displaystyle L}$ then ${\displaystyle \left(L_{i}\setminus R\right)_{i}}$ increase (resp. decreases) to ${\displaystyle L\setminus R.}$

#### Partitions

Suppose that ${\displaystyle S_{\bullet }=\left(S_{i}\right)_{i=1}^{\infty }}$ is any sequence of sets, that ${\displaystyle S\subseteq \bigcup _{i}S_{i}}$ is any subset, and for every index ${\displaystyle i,}$ let ${\displaystyle D_{i}=\left(S_{i}\cap S\right)\setminus \bigcup _{m=1}^{i}\left(S_{m}\cap S\right).}$ Then ${\displaystyle S=\bigcup _{i}D_{i}}$ and ${\displaystyle D_{\bullet }:=\left(D_{i}\right)_{i=1}^{\infty }}$ is a sequence of pairwise disjoint sets.[^21]

Suppose that ${\displaystyle S_{\bullet }=\left(S_{i}\right)_{i=1}^{\infty }}$ is non-decreasing, let ${\displaystyle S_{0}=\varnothing ,}$ and let ${\displaystyle D_{i}=S_{i}\setminus S_{i-1}}$ for every ${\displaystyle i=1,2,\ldots .}$ Then ${\displaystyle \bigcup _{i}S_{i}=\bigcup _{i}D_{i}}$ and ${\displaystyle D_{\bullet }=\left(D_{i}\right)_{i=1}^{\infty }}$ is a sequence of pairwise disjoint sets.[^21]

[^1]: For example, the expression ${\displaystyle (M\setminus R)\setminus A}$ uses two of the same symbols (${\displaystyle M}$ and ${\displaystyle R}$) that appear in the identity 
$$
{\displaystyle (L\,\setminus \,M)\,\setminus \,R~=~(L\,\setminus \,R)\,\setminus \,(M\,\setminus \,R)}
$$
 but they refer to different sets in each expression. To apply this identity to ${\displaystyle (M\setminus R)\setminus A,}$ substitute ${\displaystyle {\text{Left set}}:=M,\;}$ ${\displaystyle {\text{Middle set}}:=R,\;}$ and ${\displaystyle {\text{Right set}}:=A}$ (since these are the left, middle, and right sets in ${\displaystyle (M\setminus R)\setminus A}$) to obtain: 
$$
{\displaystyle {\begin{alignedat}{4}(M\setminus R)\setminus A&=({\text{Left set }}&&\setminus {\text{Right set}}&&)&&\setminus ({\text{Middle set }}&&\setminus {\text{Right set}})\\&=(M&&\setminus A&&)&&\setminus (R&&\setminus A).\\\end{alignedat}}}
$$
 For a second example, this time applying the identity to ${\displaystyle ((M\cap R\setminus L)\setminus (A\triangle L))\setminus L,}$ is now given. The identity ${\textstyle (L\setminus M)\setminus R=(L\setminus R)\setminus (M\setminus R)}$ can be applied to ${\displaystyle ((M\cap R\setminus L)\setminus (A\triangle L))\setminus L}$ by reading ${\displaystyle L,M,}$ and ${\displaystyle R}$ as ${\displaystyle {\text{Left}},{\text{Middle}},}$ and ${\displaystyle {\text{Right}}}$ and then substituting ${\displaystyle {\text{Left}}=(M\cap R\setminus L),}$ ${\displaystyle {\text{Middle}}=(A\triangle L),}$ and ${\displaystyle {\text{Right}}=L}$ to obtain: 
$$
{\displaystyle {\begin{alignedat}{4}((M\cap R\setminus L)\setminus (A\triangle L))\setminus L&=({\text{Left }}&&\setminus {\text{Right}}&&)&&\setminus ({\text{Middle }}&&\setminus {\text{Right}})\\&=((M\cap R\setminus L)&&\setminus L&&)&&\setminus ((A\triangle L)&&\setminus L).\\\end{alignedat}}}
$$

[^2]: To deduce **[Eq. 2c](#math_Eq._2c)** from **[Eq. 2a](#math_Eq._2a)**, it must still be shown that ${\displaystyle {\textstyle \bigcup \limits _{\stackrel {i\in I,}{j\in I}}}\left(L_{i}\cup R_{j}\right)~=~{\textstyle \bigcup \limits _{i\in I}}\left(L_{i}\cup R_{i}\right)}$ so **[Eq. 2c](#math_Eq._2c)** is not a completely immediate consequence of **[Eq. 2a](#math_Eq._2a)**. (Compare this to the commentary about **[Eq. 3b](#math_Eq._3b)**).

[^3]: So for instance, it's even possible that ${\displaystyle L\cap (X\cup Y)=\varnothing ,}$ or that ${\displaystyle L\cap X\neq \varnothing }$ *and* ${\displaystyle L\cap Y\neq \varnothing }$ (which happens, for instance, if ${\displaystyle X=Y}$), etc.

[^4]: The conclusion ${\displaystyle X\setminus f^{-1}(R)=f^{-1}(Y\setminus R)}$ can also be written as: ${\displaystyle f^{-1}(R)^{\complement }~=~f^{-1}\left(R^{\complement }\right).}$

[^5]: Whether or not it is even feasible for the function ${\displaystyle f}$ to be constant and the sets ${\displaystyle L\triangle R}$ and ${\displaystyle R}$ to be non-empty and disjoint is irrelevant for reaching the correct conclusion about whether to use ${\displaystyle \,\subseteq {\text{ or }}\supseteq .\,}$

[^6]: Note that this condition depends entirely on ${\displaystyle R}$ and *not* on ${\displaystyle L.}$

[^7]: Here "smallest" means relative to subset containment. So if ${\displaystyle \Phi }$ is any algebra of sets containing ${\displaystyle {\mathcal {S}},}$ then ${\displaystyle \Phi _{\mathcal {S}}\subseteq \Phi .}$

[^8]: Since ${\displaystyle {\mathcal {S}}\neq \varnothing ,}$ there is some ${\displaystyle S\in {\mathcal {S}}_{0}}$ such that its complement also belongs to ${\displaystyle {\mathcal {S}}_{0}.}$ The intersection of these two sets implies that ${\displaystyle \varnothing \in {\mathcal {S}}_{1}.}$ The union of these two sets is equal to ${\displaystyle X,}$ which implies that ${\displaystyle X\in \Phi _{\mathcal {S}}.}$

[^9]: Let ${\displaystyle f_{R}:=\left\{y\in f(L):L\cap f^{-1}(y)\subseteq R\right\}}$ where because ${\displaystyle f_{R}\subseteq f(R\cap L),}$ ${\displaystyle f_{R}}$ is also equal to ${\displaystyle f_{R}=\left\{y\in f(R\cap L):L\cap f^{-1}(y)\subseteq R\right\}.}$ As proved above, ${\displaystyle f(L\setminus R)=f(L)\setminus f_{R}}$ so that ${\displaystyle f(L)\setminus f(R)=f(L\setminus R)}$ if and only if ${\displaystyle f(L)\setminus f(R)=f(L)\setminus f_{R}.}$ Since ${\displaystyle f(L)\setminus f(R)=f(L)\setminus (f(L)\cap f(R)),}$ this happens if and only if ${\displaystyle f(L)\setminus (f(L)\cap f(R))=f(L)\setminus f_{R}.}$ Because ${\displaystyle f(L)\cap f(R){\text{ and }}f_{R}}$ are both subsets of ${\displaystyle f(L),}$ the condition on the right hand side happens if and only if ${\displaystyle f(L)\cap f(R)=f_{R}.}$ Because ${\displaystyle f_{R}\subseteq f(R\cap L)\subseteq f(L)\cap f(R),}$ the equality ${\displaystyle f(L)\cap f(R)=f_{R}}$ holds if and only if ${\displaystyle f(L)\cap f(R)\subseteq f_{R}.}$ ${\displaystyle \blacksquare }$ If ${\displaystyle f(R)\subseteq f(L)}$ (such as when ${\displaystyle L=X}$ or ${\displaystyle R\subseteq L}$) then ${\displaystyle f(L)\cap f(R)\subseteq f_{R}}$ if and only if ${\displaystyle f(R)\subseteq f_{R}.}$ In particular, taking ${\displaystyle L=X}$ proves: ${\displaystyle f(X\setminus R)=f(X)\setminus f(R)}$ if and only if ${\displaystyle f(R)\subseteq \left\{y\in f(R\cap X):f^{-1}(y)\subseteq R\right\},}$ where ${\displaystyle f(R\cap X)=f(R).}$ ${\displaystyle \blacksquare }$

[^10]: Let ${\displaystyle P:=\left\{y\in Y:L\cap f^{-1}(y)\subseteq R\right\}}$ and let ${\displaystyle (\star )}$ denote the set equality ${\displaystyle f(L\setminus R)=Y\setminus P,}$ which will now be proven. If ${\displaystyle y\in Y\setminus P}$ then ${\displaystyle L\cap f^{-1}(y)\not \subseteq R}$ so there exists some ${\displaystyle x\in L\cap f^{-1}(y)\setminus R;}$ now ${\displaystyle f^{-1}(y)\subseteq X}$ implies ${\displaystyle x\in L\cap X\setminus R}$ so that ${\displaystyle y=f(x)\in f(L\cap X\setminus R)=f(L\setminus R).}$ To prove the reverse inclusion ${\displaystyle f(L\setminus R)\subseteq Y\setminus P,}$ let ${\displaystyle y\in f(L\setminus R)}$ so that there exists some ${\displaystyle x\in X\cap L\setminus R}$ such that ${\displaystyle y=f(x).}$ Then ${\displaystyle x\in L\cap f^{-1}(y)\setminus R}$ so that ${\displaystyle L\cap f^{-1}(y)\not \subseteq R}$ and thus ${\displaystyle y\not \in P,}$ which proves that ${\displaystyle y\in Y\setminus P,}$ as desired. ${\displaystyle \blacksquare }$ Defining ${\displaystyle Q:=f(L)\cap P=\left\{y\in f(L):L\cap f^{-1}(y)\subseteq R\right\},}$ the identity ${\displaystyle f(L\setminus R)=f(L)\setminus Q}$ follows from ${\displaystyle (\star )}$ and the inclusions ${\displaystyle f(L\setminus R)\subseteq f(L)\subseteq Y.}$ ${\displaystyle \blacksquare }$

[^11]: Taylor, Courtney (March 31, 2019). ["What Is Symmetric Difference in Math?"](https://www.thoughtco.com/what-is-the-symmetric-difference-3126594). *ThoughtCo*. Retrieved 2020-09-05.

[^12]: Weisstein, Eric W. ["Symmetric Difference"](https://mathworld.wolfram.com/SymmetricDifference.html). *mathworld.wolfram.com*. Retrieved 2020-09-05.

[^13]: [Monk 1969](#CITEREFMonk1969), pp. 24–54.

[^14]: [Császár 1978](#CITEREFCsászár1978), pp. 15–26.

[^15]: [Császár 1978](#CITEREFCsászár1978), pp. 102–120.

[^16]: [Kelley 1985](#CITEREFKelley1985), p. [85](https://books.google.com/books?id=-goleb9Ov3oC&pg=PA85&dq=%22The+image+of+the+union+of+a+family+of+subsets+of+X+is+the+union+of+the+images%2C+but%2C+in+general%2C+the+image+of+the+intersection+is+not+the+intersection+of+the+images%22)

[^17]: See [Munkres 2000](#CITEREFMunkres2000), p. 21

[^18]: Lee p.388 of Lee, John M. (2010). Introduction to Topological Manifolds, 2nd Ed.

[^19]: Lee [Halmos 1960](#CITEREFHalmos1960), p. 39

[^20]: Lee [Munkres 2000](#CITEREFMunkres2000), p. 19

[^21]: [Durrett 2019](#CITEREFDurrett2019), pp. 1–8.

[^22]: [Császár 1978](#CITEREFCsászár1978), pp. 53–65.

[^23]: ["Algebra of sets"](https://encyclopediaofmath.org/wiki/Algebra_of_sets). *Encyclopediaofmath.org*. 16 August 2013. Retrieved 8 November 2020.