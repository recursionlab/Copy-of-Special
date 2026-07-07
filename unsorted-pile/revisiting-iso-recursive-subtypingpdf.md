---
stub: true
title: "Revisiting Iso Recursive Subtyping.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["revisiting Iso-Recursive Subtyping.pdf.md"]
psi_tier: unclassified
---

# Revisiting Iso Recursive Subtyping.Pdf

# revisiting Iso-Recursive Subtyping.pdf

223
Revisiting Iso-Recursive Subtyping
YAODA ZHOU, The University of Hong Kong, China
BRUNO C. D. S. OLIVEIRA, The University of Hong Kong, China
JINXU ZHAO, The University of Hong Kong, China
The Amber rules are well-known and widely used for subtyping iso-recursive types. They were first briefly
and informally introduced in 1985 by Cardelli in a manuscript describing the Amber language. Despite their
use over many years, important aspects of the metatheory of the iso-recursive style Amber rules have not
been studied in depth or turn out to be quite challenging to formalize.
This paper aims to revisit the problem of subtyping iso-recursive types. We start by introducing a novel
declarative specification that we believe captures the “spirit” of Amber-style iso-recursive subtyping. Informally,
the specification states that two recursive types are subtypes if all their finite unfoldings are subtypes. The Amber rules are shown to be sound with respect to this declarative specification. We then derive a sound, complete and decidable algorithmic formulation of subtyping that employs a novel double unfolding rule.
Compared to the Amber rules, the double unfolding rule has the advantage of: 1) being modular; 2) not
requiring reflexivity to be built in; and 3) leading to an easy proof of transitivity of subtyping. This work sheds
new insights on the theory of subtyping iso-recursive types, and the new double unfolding rule has important
advantages over the original Amber rules for both implementations and metatheoretical studies involving
recursive types. All results are mechanically formalized in the Coq theorem prover. As far as we know, this is
the first comprehensive treatment of iso-recursive subtyping dealing with unrestricted recursive types in a
theorem prover.
CCS Concepts: • Theory of computation → Type theory; • Software and its engineering → Object oriented languages.
Additional Key Words and Phrases: Iso-recursive types, Formalization, Subtyping
ACM Reference Format: Yaoda Zhou, Bruno C. d. S. Oliveira, and Jinxu Zhao. 2020. Revisiting Iso-Recursive Subtyping. Proc. ACM Program. Lang. 4, OOPSLA, Article 223 (November 2020), 28 pages.
https://doi.org/10.1145/3428291

1 INTRODUCTION Recursive types are used in nearly all languages to define recursive data structures like sequences or
trees. They are also used in Object-Oriented Programming every time a method needs an argument
or return type of the enclosing class.
Recursive types come in two flavours: equi-recursive types and iso-recursive types [Crary et al.
1999]. With equi-recursive types a recursive type is equal to its unfolding. With iso-recursive types,
a recursive type and its unfolding are only isomorphic. To convert between the (iso-)recursive
type and its isomorphic unfolding explicit folding and unfolding constructs are necessary. The
main advantage of equi-recursive types is convenience, as no explicit conversions are necessary.
Authors’ addresses: Yaoda Zhou, Department of Computer Science, The University of Hong Kong, Hong Kong, China,

ydzhou@cs.hku.hk
; Bruno C. d. S. Oliveira, Department of Computer Science, The University of Hong Kong, Hong Kong,
China,
bruno@cs.hku.hk
; Jinxu Zhao, Department of Computer Science, The University of Hong Kong, Hong Kong, China,

jxzhao@cs.hku.hk
.
Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses,
contact the owner/author(s).
© 2020 Copyright held by the owner/author(s).
2475-1421/2020/11-ART223

https://doi.org/10.1145/3428291

Proc. ACM Program. Lang., Vol. 4, No. OOPSLA, Article 223. Publication date: November 2020.
223:2 Yaoda Zhou, Bruno C. d. S. Oliveira, and Jinxu Zhao
data List = Nil | Cons Int List
map :: (Int -> Int) -> List -> List map f Nil =
Nil map f (Cons x xs) =
Cons (f x) (map f xs)
class Shape { int area() {...} boolean compareArea(Shape s) {
return s.area() == area(); } Shape clone() {return new Shape();}
}
Fig. 1. Recursive types in Haskell (left) and Java (right).
However, a disadvantage is that algorithms for languages with equi-recursive types are quite
complex. Furthermore, integrating equi-recursive types in type systems with advanced type fea-
tures, while retaining desirable properties such as decidable type-checking, can be hard (or even
impossible) [Colazzo and Ghelli 1999; Ghelli 1993; Solomon 1978].
Many languages adopt an iso-recursive formulation. The inconvenience of iso-recursive types is
mostly eliminated by “hiding” the explicit folding and unfolding in other constructs. For example,
in functional languages, such as Haskell or ML, iso-recursive types are provided via datatypes.
Figure 1 (left) illustrates a simple recursive type in Haskell. The List datatype is recursive, as
the Cons constructor requires a List as the second argument. Functions such as map, can then be
defined by pattern matching. While there are no explicit folding or unfolding operations in the
program above, every use of the constructors (Nil and Cons) triggers folding of the recursive type.
Conversely, the patterns on Nil and Cons trigger unfolding of the recursive type. Similarly, in
nominal Object-Oriented (OO) languages such as Java, iso-recursive types can be introduced in class
definitions such as the one to the right of Figure 1. This class definition requires recursive types
because both compareArea and clone need to refer to the enclosing class. Like the Haskell program above, there are no explicit uses of folding and unfolding. Instead, constructors trigger folding
of the recursive type; while method calls (such as area()) trigger recursive type unfolding. The relationship between iso-recursive types, algebraic datatypes and pattern matching, and nominal
OO class definitions is well-understood in the research literature [Lee et al. 2015; Pierce 2002; Stone
and Harper 1996; Vanderwaart et al. 2003; Yang and Oliveira 2019].
The Amber rules are well-known and widely used for subtyping iso-recursive types. They
were briefly and informally introduced in 1985 by Cardelli in a manuscript describing the Amber
language [Cardelli 1985]. Later on, Amadio and Cardelli [1993] made a comprehensive study of
the theory of recursive subtyping for a system with equi-recursive types employing Amber-style
rules. One nice result of their study is a declarative model for specifying when two recursive types
are in a subtyping relation. In essence, two (equi-)recursive types are subtypes if their infinite
unfoldings are subtypes. Amadio and Cardelli’s study remains to the day a standard reference
for the theory of equi-recursive subtyping, although newer work simplifies and improves on the
original theory [Brandt and Henglein 1997; Gapeyev et al. 2003]. Since then variants of the Amber
rules have been employed multiple times in a variety of calculi and languages, but often in an
iso-recursive setting [Bengtson et al. 2011; Chugh 2015; Duggan 2002; Lee et al. 2015; Swamy et al.
2011]. From this point onwards, in the context of this paper, whenever we use the term Amber
rules we refer to a subtyping relation, modelling iso-recursive subtyping, with at least the following
rules:
Γ,α ≤ β ⊢ A ≤ B
Γ ⊢ µα . A ≤ µβ . B S-Amber
α ≤ β ∈ Γ
Γ ⊢ α ≤ β S-Assumption
Γ ⊢ A ≤ A S-Refl
Proc. ACM Program. Lang., Vol. 4, No. OOPSLA, Article 223. Publication date: November 2020.
Revisiting Iso-Recursive Subtyping 223:3
These rules are found in nearly all the literature modelling subtyping for iso-recursive types with
the Amber rules. The first rule states that two recursive types are subtypes if their bodies are
subtypes under the assumption that the two distinct recursive variables α and β are subtypes. The
second rule states that two recursive variables are subtypes if they are related in the environment.
We also consider the reflexivity rule to be an essential part of the formulation of iso-recursive style
Amber rules for two different reasons. Without the reflexivity rule (or some similar rule) built-in,
reflexivity cannot be proved. Indeed, it is well-known [Amadio and Cardelli 1993] that equal types
with negative (or contravariant) recursive occurrences cannot be shown to be subtypes without
reflexivity. A concrete example is µα . α → nat <: µα . α → nat. Secondly, the reflexivity rule is the
main difference to an equi-recursive formulation employing the Amber rules. In an equi-recursive
formulation, reflexivity is replaced by a much more powerful rule that employs an equivalence
relation on types where two types are considered equal if their infinite unfoldings are equal. This
enables showing, for instance, that µα . nat → α <: µα . nat → nat → α holds in an equi-recursive
formulation, while this clearly fails if we only employ syntactic equality as in the reflexivity rule.
The Amber rules are appealing due to their apparent simplicity, but their metatheory is not well
studied. Clearly, from an implementation point of view, the Amber rules are rather simple and
easy to implement. However, unlike an equi-recursive formulation, which has a clear declarative
specification, there is no similar declarative specification for an iso-recursive formulation so far.
Moreover, there are fundamental differences between equi-recursive and iso-recursive subtyping:
while equi-recursive subtyping deals with infinite trees and is naturally understood in a coinductive
setting [Brandt and Henglein 1997; Gapeyev et al. 2003], an Amber-style iso-recursive formulation
deals with finite trees and ought to be understood in an inductive setting. Furthermore, important
properties for algorithmic versions of the Amber rules are lacking or are quite difficult to prove. In
particular, there is very little work in the literature regarding proof of transitivity for algorithmic
formulations of the Amber rules. Indeed, the only proof for transitivity that we are aware of is by
Bengtson et al. [2011]. However, the proof relies on a complex inductive argument, and attempts
to formalize the proof in a theorem prover have been unsuccessful so far [Backes et al. 2014].
Finally, a fundamental lemma that arises in proofs of type preservation for calculi with iso-recursive
subtyping is:
If µα . A ≤ µα . B then [α 7→ µα . A] A ≤ [α 7→ µα . B] B
We call this lemma the unfolding lemma. The unfolding lemma plays a similar role in preservation
to the substitution lemma (which is needed for proving preservation of beta-reduction), and is
used to prove the case dealing with recursive type unfolding. The proof for the unfolding lemma is
non-trivial, but there is also little work on proofs of this lemma for the Amber rules. While there
are some interesting alternatives for iso-recursive subtyping [Hofmann and Pierce 1996; Ligatti
et al. 2017], Amber-style subtyping strikes a good balance between expressive power and simplicity,
and is widely used. Thus understanding Amber-style subtyping further is worthwhile.
This paper aims to revisit the problem of subtyping iso-recursive types. We start by introducing
a novel declarative specification that we believe captures the “spirit” of Amber-style iso-recursive
subtyping. Informally, the specification states that two recursive types are subtypes if all their finite
unfoldings are subtypes. More formally, the subtyping rule for recursive types is:
Γ,α ⊢ [α 7→ A]n A ≤ [α 7→ B]n B ∀n = 1 · · · ∞
Γ ⊢ µα . A ≤ µα . B S-Rec
Here the notation [α 7→ A]n denotes the n-times finite unfolding of a type. Essentially, n times
unfolding applies n−1 substitutions to the typeA, and the rule checks that all n-times unfoldings are
Proc. ACM Program. Lang., Vol. 4, No. OOPSLA, Article 223. Publication date: November 2020.
223:4 Yaoda Zhou, Bruno C. d. S. Oliveira, and Jinxu Zhao
subtypes. Such a declarative formulation plays a similar role to Amadio and Cardelli’s declarative
specification for equi-recursive types. Because the specification is defined with respect to the finite
unfoldings, this naturally leads to an inductive treatment of the theory. For example, the proof of
transitivity of subtyping is fairly straightforward, with the more significant challenge being the
unfolding lemma. With all the metatheory in place, proving subject-reduction for a typed lambda
calculus with recursive types is a routine exercise. Furthermore, the Amber rules are shown to be
sound with respect to this declarative specification.
The declarative specification of subtyping is not directly implementable because it has to consider
all finite unfoldings. Furthermore, showing completeness of the Amber rules is hindered by the
complexities involved their formalization. Therefore, to obtain a sound, complete and decidable
algorithmic formulation, we follow a different route. We employ a novel double unfolding rule:
Γ,α ⊢ A ≤ B Γ,α ⊢ [α 7→ A] A ≤ [α 7→ B] B
Γ ⊢ µα . A ≤ µα . B S-Double
This rule says that for determining if two recursive types are subtypes, checking 1-time and 2-times
finite unfolding is enough. This rule accepts all valid subtyping statements that the Amber rules
accept, but it has important advantages. In particular, the rule is modular in the sense that it does
not require changes to other rules or definitions involved in subtyping. The environments are just a
standard collection of type variables, and the rule for type variables is also standard. Consequently,
proofs for properties such as transitivity only need to account for the new recursive case, while
all the other cases remain essentially the same as in a subtyping relation without recursive types.
In contrast, the Amber rules have a pervasive impact in the subtyping relation, which is the root
cause of the difficulties in doing proofs such as transitivity. Moreover, an additional benefit is
that reflexivity does not have to be built in, but it can be derived instead. Built-in reflexivity can
be problematic in some settings, including calculi with record subtyping or intersection types.
Such calculi can have “isomorphic” subtyping where two syntactically different types A and B can
be subtypes of each other. For instance, in calculi with records, the types {x : Int,y : Bool} and {y : Bool, x : Int} are subtypes of each other. Avoiding built-in reflexivity makes the rules easier to
apply in such settings. The main difficulty with the algorithmic formulation is proving soundness
with respect to the declarative specification. For getting over this difficulty, we employ an inductive
relation that captures valid subtyping subderivations. To validate all our results we have mechanically formalized all our results in the Coq theorem
prover. As far as we know this is the first comprehensive treatment of iso-recursive subtyping
dealing with unrestricted recursive types in a theorem prover.
In summary, the contributions of this paper are:

A declarative specification for iso-recursive subtyping: We propose a new declarative
specification for iso-recursive subtyping, where two recursive types are subtypes if all the
finite unfoldings are subtypes (Section 3).

Algorithmic subtyping with the double unfolding rule: We show a sound, complete
and decidable algorithmic formulation of subtyping employing a new double-unfolding rule
(Section 4).

Induction on subderivations: As part of the soundness proof for our algorithmic formula-
tion we employ a novel technique of induction over subderivations of subtyping, which is
independently useful as a proof technique (Section 4).

Soundness of the Amber rules: We prove that the Amber rules are sound with respect to
our new formulation of subtyping (Section 5).
Proc. ACM Program. Lang., Vol. 4, No. OOPSLA, Article 223. Publication date: November 2020.
Revisiting Iso-Recursive Subtyping 223:5

Subject-reduction for a typed lambda calculus with recursive types: To illustrate the

[... content truncated ...]

---

*Source: `revisiting Iso-Recursive Subtyping.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
