---
stub: true
title: "The Univalence Axiom For Elegant Reedy Preshea"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [zero_divisor, "ingested"]
sources: ["The univalence axiom for elegant Reedy preshea.md"]
psi_tier: zero_divisor
---

# The Univalence Axiom For Elegant Reedy Preshea

# The univalence axiom for elegant Reedy preshea

THE UNIVALENCE AXIOM FOR ELEGANT REEDY
PRESHEAVES
MICHAEL SHULMAN
Abstract. We show that Voevodsky’s univalence axiom for homotopy type theory is valid in categories of simplicial presheaves on elegant Reedy cate-gories. In addition to diagrams on inverse categories, as considered in previ-ous work of the author, this includes bisimplicial sets and Θn-spaces. This has potential applications to the study of homotopical models for higher categories.

Introduction

Type theory is a formal syntax for mathematical reasoning, with roots in con-structive logic and computer science. Its types are traditionally viewed as set-like, but can more generally be interpreted as objects of any sufficiently structured cat-egory [See84,CD11]; thus formal derivations in type theory yield theorems in cat-egory theory. Recently it has emerged (see e.g. [HS98,War08,AW09,AK11, vG12, Voe11, LW14,Awo14]) that this correspondence can be extended to certain model categories, so that formal derivations in type theory can also yield theorems in homotopy theory. The resulting subject is known as homotopy type theory.

The collection of homotopical theorems that have been proven using type the-ory is small but growing; see [Uni13, Chapter 8] for a list as of its publication. So far, all such theorems were already known by methods of classical homotopy theory, but there are several advantages to the type-theoretic approach. One sig-nificant one is that type theory can be interpreted in many model categories, so that a type-theoretic proof of a theorem such as π1(S

= Z [LS13] is much more general than a classical proof using topological spaces or simplicial sets. For ex-ample, Lumsdaine, Finster, and Licata have already used type theory to produce a new proof of the Blakers–Massey theorem [Fav13], which thus applies in more general categories. When translated across the categorical interpretation of type theory [Rez14], this proof becomes a model-categorical one, which could in principle have been discovered by classical homotopy theorists; but in practice it was not.
Type theory also brings a more “internal” perspective to homotopy theory, yield-ing more general constructions of various objects. For instance, in classical homo-topy theory one may consider the space hAut(X) of self-homotopy equivalences of a space X , defined simply as the obvious subspace of the function space XX . Homotopy type theory shows that an equivalent space to hAut(X) can be obtained

Key words and phrases. homotopy type theory, univalence axiom, elegant Reedy category. This material is based upon work supported by the National Science Foundation under a

postdoctoral fellowship and agreement No. DMS-1128155. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author and do not necessarily reflect the views of the National Science Foundation.
1
2 MICHAEL SHULMAN
by purely categorical constructions, which is thereby applicable in more generality. (We will describe this example in more detail in section 4.)

Finally, another advantage of type-theoretic homotopy theory is its convenient treatment of fibrations. In type theory, a fibration over a space A is represented by a type family indexed by A, which is a map from A into the universe type U . The correctness of this representation is guaranteed by Voevodsky’s univalence axiom, which identifies the path space of U with a certain space of equivalences, implying that U is a “classifying space for fibrations”. Of course, classifying spaces also exist in classical homotopy theory, but the systematic representation of fibrations as functions in type theory simplifies many things, especially when working with spaces defined as colimits (for example, the “encode-decode method” described in [Uni13, Chapter 8]), or when doing parametrized homotopy theory.

With these two advantages of type theory in mind, it becomes important to know in which model categories we can interpret type theory, and in particular the univalence axiom. Since univalence says that the universe is a classifying space for fibrations, one natural categorical analogue would be the object classifiers of Rezk and Lurie (see [Lur09, §6.1.6] and also [GK12]). Thus, we may expect that type theory with the univalence axiom could be interpreted in any model category with object classifiers, and in particular in any presentation of an “(∞, 1)-topos”.

The main problem with this, and with the interpretation of type theory more generally, is that its formal syntax is stricter than the categorical structure available in the desired models. The first model of the univalence axiom to overcome this difficulty was also due to Voevodsky [KLV12a], using the model category sSet of simplicial sets, which presents the (∞, 1)-category of ∞-groupoids (the most basic (∞, 1)-topos).
In [Shu14], starting from Voevodsky’s model in sSet, I constructed a model of

type theory satisfying univalence in the Reedy model category sSetI , whenever I is an inverse category. This paper will generalize that result to the Reedy model struc-ture on sSetC

op

whenever C is an elegant Reedy category, as in [BR13]. (This result has now been further generalized by Cisinski [Cis14].) Elegant Reedy categories include direct categories (the opposites of inverse categories), but also categories such as the simplex category ∆, the n-fold simplex category ∆n, and Joyal’s cat-egories Θn. Thus, the (∞, 1)-toposes of n-fold simplicial spaces and Θn-spaces admit models of type theory satisfying the univalence axiom. We will not study such particular models further in this paper, but since these toposes have been used as models for higher categories (see e.g. [Rez01,Rez10]), their internal type theories may be useful in extending the interpretation of type theory from (∞, 1)-categories to (∞, n)-categories.

The proof given in this paper does not depend on that of [Shu14], and is more similar in flavor to that of [KLV12a]. In particular, it is purely model-category-theoretic; no knowledge of type theory is required. (Note that the model-categorical parts of the construction of [KLV12a] are reproduced in the shorter pa-per [KLV12b].) However, this new proof does not replace [Shu14], since it applies only to presheaves of simplicial sets, whereas that of [Shu14] applies to diagrams in any category which models type theory with univalence (such as the syntac-tic category of type theory itself) and also generalizes to oplax limits and gluing constructions.
THE UNIVALENCE AXIOM FOR ELEGANT REEDY PRESHEAVES 3

Remark 1.1. Most aspects of type theory aside from univalence (e.g. Σ-types, Π-types, and identity types) are now known to admit models in all (∞, 1)-toposes, and indeed in all locally presentable, locally cartesian closed (∞, 1)-categories. By the coherence theorem of [LW14] (see also [Awo14]), it suffices to present such an (∞, 1)-category by a “type-theoretic model category” in the sense of [Shu14], such as a right proper Cininski model category [Cis02,Cis06]. That this is always possible has been proven by Cisinski [Cis12] and by Gepner–Kock [GK12]. Moreover, if the (∞, 1)-category is an (∞, 1)-topos, then we can choose fibrations of fibrant objects representing its object classifiers, which will behave almost like universes and satisfy the univalence axiom. What is missing is that such “universes” need not be strictly closed under the type-forming operations; that is, the operation taking elements of the universe to types only respects these operations up to equivalence. It is this extra missing bit of strictness which we aim to provide here, in the special case of elegant Reedy presheaves.

In fact, a good deal of the proof that we will present is not special to elegant Reedy categories: it applies to any cofibrantly generated right proper model struc-ture on a presheaf category whose cofibrations are the monomorphisms and such that the codomains of the generating acyclic cofibrations are representable. The structure of the paper reflects this fact. We begin in §2 with some remarks on how to construct univalent universes (that is, universe objects satisfying the uni-valence axiom). In particular, we recall a method due to [KLV12a] which enables us to reduce statements about the universe, such as its univalence and fibrancy, to statements about fibrations.
In the next three sections §3–5, we show that any presheaf model category with the properties mentioned above satisfies almost all the requirements to represent a univalent universe in the internal type theory; the only thing missing is a proof that it is a fibrant object. Specifically, in §3 we construct such universes in three ways (two of which are due to [KLV12a] and in [Str14]); in §4 we prove a postponed lemma from §2; and in §5 we verify the remaining requirements for modeling universes in type theory, using [LW14,KLV12a].
Finally, in §6 we complete the proof in the case of elegant Reedy presheaves, showing that such presheaf categories satisfy the above conditions, and that more-over their universes are fibrant. This depends on the explicit nature of the Reedy model structure.
A remark about notation: we will denote fibrations and cofibrations in any model category by A ։ B and A ֌ B, respectively. Similarly, we write A ∼
։ B and A ∼
֌ B for acyclic fibrations and acyclic cofibrations.
Acknowledgments. I am grateful to Peter Lumsdaine for many very helpful dis-cussions, and for emphasizing the essential outline of the proof in [KLV12a], as described in §2. I am also grateful to Bas Spitters, and to the referee, for helpful comments and suggestions.

On proofs of univalence
The univalence axiom, when interpreted in a model category, is a statement about a “universe object” U , which is fibrant and comes equipped with a fibration
p : Ũ ։ U that is generic, in the sense that any fibration with “small fibers” is a pullback of p. (The meaning of “small” will vary with the model; the important
4 MICHAEL SHULMAN
thing for modeling type theory is that the small fibrations be closed under the category-theoretic analogues of all the type forming operations. Thus, we usually take the small fibrations to be those of cardinality smaller than some inaccessible cardinal, for some appropriate meaning of “cardinality”. We will return to this in §5.)

In homotopy theory, it would be natural to ask for the stronger property that U is a classifying space for small fibrations, i.e. that homotopy classes of maps A → U are in bijection with (rather than merely surjecting onto) equivalence classes of small fibrations over A. The univalence axiom is a further strengthening of this: it says that the path space of U is equivalent to the “universal space of equivalences” between fibers of p (which we will define in §4). In particular, therefore, if two pullbacks of p are equivalent, then their classifying maps are homotopic.

It is not difficult to obtain a fibrant univalent universe that classifies small fi-brations up to homotopy, i.e. such that any fibration with small fibers is a ho-motopy pullback of the generic one. For instance, one can simply choose any fibration between fibrant objects that represents an object classifier in the sense of [Lur09, §6.1.6]. However, for modeling type theory we are concerned with the class of fibrations occurring as strict pullbacks of the generic one. Finding a fibrant universe that classifies all fibrations with small fibers in this strict sense is where the difficulties lie in modeling the univalence axiom.

Naively, we might expect that the construction of such an object would take place in four steps:
(1) Construct a particular small fibration p : Ũ ։ U . (2) Prove that every small fibration is a (strict) pullback of p. (3) Prove that U is fibrant. (4) Prove that the univalence axiom holds.
The proof in [Shu14] that univalence lifts to inverse diagrams follows this outline: we construct a Reedy fibration p which satisfies (2) and (3) almost by definition, and then (4) follows by a somewhat lengthy, but direct, analysis of exactly what the univalence axiom claims.
The proof of univalence for simplicial sets in [KLV12a], by contrast, follows a
slightly different route. They first construct a fibration p : Ũ ։ U which satisfies the following stronger version of (2):
(2′) Given the solid arrows in the following diagram, where A ֌ B is a cofibration, P ։ B is a small fibration, and both squares of solid arrows are pullbacks:
A
Q
U
Ũ
P
B
there exist the dashed arrows rendering the diagram commutative and the third square also a pullback.
In a context (such as simplicial sets) where all objects are cofibrant, taking A = ∅ in (2′) yields (2).
THE UNIVALENCE AXIOM FOR ELEGANT REEDY PRESHEAVES 5
Condition (2′) can be rephrased in the following suggestive way: suppose for the sake of argument that there were a thing called U such that maps A → U were
precisely small fibrations over A. Then the small fibration p : Ũ ։ U would be classified by a map U → U, and (2′) asserts that this map is an acyclic fibration. (One can even make this precise by regarding U as a fibered category or groupoid.)
With (2′) in hand, (3) and (4) can be reduced to statements not referring to U at all. For instance, suppose we can show:
(3′) If i : A ֌ B is an acyclic cofibration and P ։ A a small fibration, then there exists a small fibration Q ։ B such that P ∼= i∗Q. In other words, the solid arrows below can be completed to a pullback square as shown:
A B
P Q
i
∼
Then given an acyclic cofibration i : A ֌ B and a map f : A → U , (3′) gives us a
fibration Q over B which pulls back to f∗Ũ over A, and by (2′) we have g : B → U
with g∗Ũ ∼= Q and gi = f . Thus, (3) follows. Intuitively, we are saying that since U → U is an acyclic fibration, if U is fibrant then so is U .
For (4), we need to know the category-theoretic expression of the univalence
axiom. This asserts that a canonical map PU → Eq(Ũ) is an equivalence, where
PU denotes the path object of U and Eq(Ũ) is the universal space of equivalences over U × U ; we will define the latter precisely in §4. By the 2-out-of-3 property,
this is equivalent to U → Eq(Ũ) being an equivalence, and therefore also to either
projection Eq(Ũ) → U being an equivalence. Since these projections are always fibrations, we want them to be acyclic fibrations; but acyclic fibrations are charac-terized by a lifting property. If we rephrase this property of the second projection in terms of actual fibrations and equivalences (i.e. using the hypothetical U), we obtain:
(4′) Suppose given a cofibration i : A ֌ B, small fibrations D2 ։ B and E1 ։ A, and an equivalence w : E1
∼−→ E2 of fibrations over A, where E2 := i∗D2. Then there exists a small fibration D1 over B and an equivalence v : D1
∼−→ D2 over B, which yields w when pulled back along i.
A B
E1
E2
i
w
D2
D1
v
If (4′) holds, then for any commutative square
A
B U
Eq(Ũ)
i
6 MICHAEL SHULMAN
with i a cofibration, the given maps A → Eq(Ũ) and B → U respectively classify w and D2 as in (4′). Then (4′) gives D1 and v, condition (2′) yields a classifying map
for D1 extending the composite A → Ũ → U , and using the following lemma, we
can construct a lift in the above square, so that Eq(Ũ) → U is an acyclic fibration.

Lemma 2.1. In a suitable model category, let D1 ։ B and D2 ։ B be fibrations classified by maps B ⇒ U , let v : D1 → D2 be a weak equivalence over B, let

i : A ֌ B be a cofibration, and suppose we have a lift of A i −→ B → U ×U to Eq(Ũ)

which classifies i∗(v). Then this lift can be extended to B so as to classify v.

In particular, if all objects are cofibrant (as will be the case in all our exam-ples), then taking A = ∅ in Lemma 2.1 implies that any weak equivalence between
fibrations over B is classified by some map B → Eq(Ũ). The proof of Lemma 2.1 is the only place where we need to know the actual

definition of Eq(Ũ). This definition is determined by the specific formulation of the univalence axiom in type theory and is somewhat technical, so we will consider it separately in §4, postponing the proof of Lemma 2.1 until then. For now, it suffices to take Lemma 2.1 as a (hopefully plausible) black box. In fact, one might argue that just as (2′) determines a good notion of what it means to be a universe object in a model category, the conclusion of Lemma 2.1 is a good definition of what it

means for Eq(Ũ) to be a “universal space of equivalences” therein.

Constructing univalent universes
Let us now consider in what level of generality we can prove (2′), (3′), and (4′). Perhaps surprisingly, given that (4′) is a modification of the actual statement (4) of univalence, it seems to be the easiest to prove in the most generality. The proof in [KLV12a] for simplicial sets carries through almost word-for-word in a much more general context.
Let C be a small category. We say a morphism f : A → B in the presheaf category SetC
op
is κ-small, for some cardinal number κ, if for all c ∈ C and b ∈ Bc we have |f−1
c (b)| < κ. We denote by |C| the cardinality of the coproduct set ∑
c,c′∈C C(c, c ′)
consisting of all arrows in C.

Theorem 3.1. If SetC op

is a presheaf category that is a simplicial model category whose cofibrations are exactly the monomorphisms, and κ is a cardinal number

larger than |C|, then the κ-small fibrations in SetC op

satisfy (4 ′).

Proof (from [KLV12a]). Suppose given a cofibration i : A ֌ B, a κ-small fibration D2 ։ B, and an equivalence w : E1

∼−→ E2 := i∗D2 of κ-small fibrations over A; we want to constructD1 and the dashed arrows shown in the diagram shown below (4′).
Define D1 and v as the following pullback in SetC op
/B, where i∗ denotes the right adjoint of pullback i∗:
D1 //
v

❴ ✤ i∗E1
i∗(w)

D2 η // i∗i
∗D2 ∼= i∗E2.
Since i∗ preserves this pullback, and i∗ is fully faithful, v pulls back to w. It is straightforward to check that D1 → B is κ-small; it remains to show it is a fibration and that v is an equivalence.
THE UNIVALENCE AXIOM FOR ELEGANT REEDY PRESHEAVES 7
We factor w as an acyclic cofibration followed by an acyclic fibration and treat the two cases separately. In the second case, i∗(w) is an acyclic fibration and thus so is v. In the first case, since E1 and E2 are fibrations over A, by [Hir03, 7.6.11 and 9.5.24], we have a simplicial deformation retraction H : ∆1 ⊗ E2 → E2 of E2
onto E1 in SetC op
/A, where ⊗ denotes the tensor for the simplicial enrichment. Now η and v are monic, so if P denotes the pushout
E1 //
w

D1
 v
 ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶ ✶
E2 //
((◗ ◗◗
◗◗ ◗◗
◗◗ ◗◗
◗◗ ◗◗ P
j ❈
!!❈ ❈❈
❈❈ ❈
❴✤
D2,
then j is also a monomorphism. Since we are in a simplicial model category, the pushout product on the left of the following square is an acyclic cofibration:
(∆0 ⊗D2) ∪∆0⊗P (∆1 ⊗ P ) //

D2

∆1 ⊗D2 //
H
66
B.
The map at the top is induced by the identity on ∆0⊗D2 ∼= D2, and on ∆1⊗P by
a combination of ηH on E2 and the constant homotopy at v on D1 (which agree in E1 since H is a deformation retraction). Since D2 → B is a fibration, H exists, and since i∗(H) = H is a deformation retraction into E1, H is a deformation retraction into D1. Thus v is the inclusion of a deformation retract, hence a weak equivalence; and D1 → B, being a retract of D2 → B, is a fibration. 
I do not know any general context of this sort in which one can prove (3′). However, the situation with (2′) is better:

Theorem 3.2. Suppose SetC op

is a presheaf category that is a cofibrantly gen-erated model category in which all cofibrations are monomorphisms, and that the codomains of the generating acyclic cofibrations are representable. Then there exists a κ-small fibration satisfying (2 ′).

In the special case of simplicial sets, this theorem has been proven by [KLV12a] and [Str14], and their proofs generalize immediately to any category satisfying the stated hypotheses. I will present a third, new, proof of this theorem, which I believe makes the connection to (∞, 1)-categorical object classifiers rather clearer. But to facilitate comparisons, I will first sketch the main ideas of the proofs of [KLV12a] and [Str14].
The basic idea of both of these proofs is that a presheaf U is (of course) defined by giving its values at each object c ∈ C, while by the Yoneda lemma, elements of U(c) are in bijective correspondence with maps Yc → U , where Yc is the representable presheaf at c. Since maps into U are supposed to classify small fibrations, we should define U(c) to be some set of small fibrations over Yc. The problem is to choose a small set of representatives for this collection of fibrations in such a way that U becomes a strict functor (rather than a pseudofunctor). In [KLV12a] this is done
8 MICHAEL SHULMAN
by imposing well-orderings on the fibers, while in [Str14] it is done by considering presheaves on the category of elements of Yc (i.e. the slice category C/c).
By contrast, in the proof I will now present, we do not define U by giving its value at each object. Indeed, the fact that we are in a presheaf category makes no overt appearance; we will only need to know that the codomains of the generating acyclic cofibrations X ∼
֌ Y have the property that hom(Y,−) preserves small colimits. In addition, we will need the following “exactness properties” of any Grothendieck topos.
(a) Given a family
Xi //

[... content truncated ...]

---

*Source: `The univalence axiom for elegant Reedy preshea.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
