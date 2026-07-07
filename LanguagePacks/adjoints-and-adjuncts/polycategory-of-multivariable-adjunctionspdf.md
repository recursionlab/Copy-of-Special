---
stub: true
title: "Polycategory Of Multivariable Adjunctions.Pdf"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [zero_divisor, "ingested"]
sources: ["polycategory of multivariable adjunctions.pdf.md"]
psi_tier: zero_divisor
---

# Polycategory Of Multivariable Adjunctions.Pdf

# polycategory of multivariable adjunctions.pdf

THE 2-CHU-DIALECTICA CONSTRUCTION AND THE POLYCATEGORY OF MULTIVARIABLE ADJUNCTIONS
MICHAEL SHULMAN
Abstract. Cheng, Gurski, and Riehl constructed a cyclic double multicategory of multivariable adjunctions. We show that the same information is carried by a poly double category, in which opposite categories are polycategorical duals. Moreover, this poly double category is a full substructure of a double Chu construction, whose objects are a sort of polarized category, and which is a natural home for 2-categorical dualities.
We obtain the double Chu construction using a general “Chu-Dialectica” construction on polycategories, which includes both the Chu construction and the categorical Dialectica construction of de Paiva. The Chu and Dialectica constructions each impose additional hypotheses making the resulting polycategory representable (hence ∗-autonomous), but for different reasons; this leads to their apparent differences.
Contents
1 Introductions 1 2 Presheaves of polycategories 16 3 Dimension (1, 1): the 2-Chu-Dialectica construction 20 4 Dimension (0, 1): the Dialectica construction 22 5 Dimension (0, 0): the Chu construction 25 6 Dimension (1, 0): the 2-Chu and double Chu constructions 28 7 Cyclic multicategories and parametrized mates 36

Introductions
I have written two introductions to this paper, each of which can be read independently. If you are interested in Dialectica and Chu constructions, please continue with section 1.1; but if you are more interested in multivariable adjunctions, I suggest skipping ahead to read section 1.4 first.
This material is based on research sponsored by The United States Air Force Research Laboratory under agreement number FA9550-15-1-0053 and FA9550-16-1-0292. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright notation thereon. The views and conclusions contained herein are those of the author and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the United States Air Force Research Laboratory, the U.S. Government, or Carnegie Mellon University.
2010 Mathematics Subject Classification: 18D10,18D05. Key words and phrases: multivariable adjunction, polycategory, Dialectica construction, Chu con-
struction. c© Michael Shulman, 2020. Permission to copy for private use granted.
1
2 MICHAEL SHULMAN
1.1. First Introduction: Unifying the Dialectica and Chu constructions.
The categorical Dialectica constructions were introduced by [dP89a, dP89b] as an abstrac-tion of Gödel’s “Dialectica interpretation” [Göd58]. Although Gödel’s interpretation mod-eled intuitionistic logic, de Paiva’s categorical analysis revealed that it factors naturally through Girard’s classical linear logic [Gir87], which categorically means a ∗-autonomous category [Bar91, CS97b].
On the other hand, the Chu construction [Chu78, Chu79, Bar06] was introduced specif-ically as a way to produce ∗-autonomous categories. Anyone familiar with both construc-tions can tell that they have a very similar feel, and one formal functorial comparison was given in [dP06]. In this paper we compare them in a new way, by giving such a general construction that includes both Dialectica and Chu constructions as special cases.
One reason it is hard to compare the Dialectica and Chu constructions is that while their underlying categories are defined very similarly, their monoidal structures are defined rather differently. This suggests that a fruitful way to compare them would be to perform them both in a more general context where these monoidal structures need not exist, but can be characterized up to isomorphism by universal properties. In other words, instead of monoidal categories we will use multicategories, and instead of ∗-autonomous categories we will use polycategories [Sza75].1
To define a multi- or polycategorical version of the Dialectica or Chu constructions, we need to start by asking what universal property is possessed by their tensor products, i.e. what functor they represent, in the way that the tensor product of abelian groups represents bilinear maps. In other words, if ⊠ denotes these tensor products, then what does a morphism A⊠ B → C look like if we “beta-reduce away” the definition of ⊠?
First, let us consider the Chu construction, which in its basic form applies to a closed symmetric monoidal category C with pullbacks, equipped with an arbitrary object Ω. In the resulting category Chu(C,Ω),

The objects are triples A = (A+, A−, A) where A+, A− are objects of C and A : A+ ⊗ A− → Ω is a morphism in C.

The morphisms f : (A+, A−, A) → (B+, B−, B) are pairs (f+, f−) where f+ : A+ → B+ and f− : B− → A− are morphisms in C such that
A ◦ (1⊗ f−) = B ◦ (f+ ⊗ 1).
The tensor product of two objects A,B ∈ Chu(C,Ω) is defined by
(A⊠ B)+ = A+ ⊗ B+
(A⊠ B)− = [A+, B−]×[A+⊗B+,Ω] [B +, A−]
A⊠ B = ((
[A+,B−]×[A+⊗B+,Ω][B +,A−]
) ⊗A+⊗B+→[A+⊗B+,Ω]⊗A+⊗B+→Ω
)
1A polycategorical viewpoint on the Chu construction, in the case of non-symmetric “cyclic” poly-bicategories, can also be found in [CKS03, Example 1.8(2)]. In this paper we will consider only the symmetric case.
THE 2-CHU-DIALECTICA CONSTRUCTION 3
By definition of the morphisms in Chu(C,Ω), a morphism A ⊠ B → C consists of C-morphisms f+ : A+ ⊗ B+ → C+ and f− : C− → [A+, B−]×[A+⊗B+,Ω] [B
+, A−] such that some diagram commutes. But by the universal property of pullbacks and internal-homs, to give f− is equivalent to giving f−
1 : A+ ⊗ C− → B− and f− 2 : B+ ⊗ C− → A− such
that B ◦ (1B+ ⊗ f− 1 ) = A ◦ (1A+ ⊗ f−
2 ) (modulo a symmetry in the domain). And the commutative diagram then simply asserts that this joint composite is also equal (again, modulo symmetry) to C ◦ (f+ ⊗ 1C−).
Thus, in total a morphism A⊠B → C in Chu(C,Ω) consists of morphisms
f+ : A+ ⊗ B+ → C+
f− 1 : A+ ⊗ C− → B−
f− 2 : B+ ⊗ C− → A−
such that B ◦ (1B+ ⊗ f−
1 ) = A ◦ (1A+ ⊗ f− 2 ) = C ◦ (f+ ⊗ 1C−).
There are several things to note about this:

It is certainly a “two-variable” generalization of the definition of ordinary morphisms A→ B in Chu(C,Ω).

It makes sense even if C is only a multicategory, with f+ : (A+, B+) → C+ and so on.

With a little thought, one can guess the correct n-variable version, dualize to describe maps A → B ⊠ C, where B ⊠ C = (B∗
⊠ C∗)∗ is the dual “cotensor product” (the “par” of linear logic), and then generalize to maps from an n-ary tensor to an m-ary cotensor. This leads to our polycategorical definition.

If we write the above equalities in the internal type theory ofC, using formal variables a : A+, b : B+, and c : C−, they become
C(f+(a, b), c) = B(b, f− 1 (a, c)) = A(a, f−
2 (b, c)),
which is highly reminiscent of the hom-set isomorphisms in a two-variable adjunction. We will pick up this thread in section 1.4.
Moving on to the Dialectica construction, we will describe the version from [dP06], which looks the most like the Chu construction. This Dialectica construction applies to a closed symmetric monoidal category C with finite products, equipped with an object Ω that internally has the structure of a closed monoidal poset. In the resulting category Dial(C,Ω),

The objects are the same as those of Chu(C,Ω): triples A = (A+, A−, A) where A+, A− are objects of C and A : A+ ⊗ A− → Ω is a morphism in C.
4 MICHAEL SHULMAN

The morphisms f : (A+, A−, A) → (B+, B−, B) are pairs (f+, f−) where f+ : A+ → B+ and f− : B− → A− are morphisms in C such that
A ◦ (1⊗ f−) ≤ B ◦ (f+ ⊗ 1)
in the internal order of Ω (applied pointwise to morphisms A+ ⊗B− → Ω).
The tensor product of two objects A,B ∈ Dial(C,Ω) is defined by
(A⊠ B)+ = A+ ⊗ B+
(A⊠ B)− = [A+, B−]× [B+, A−]
with A⊠ B being the tensor product (in the internal monoidal structure of Ω) of the two morphisms
A+ ⊗B+ ⊗ ([A+, B−]× [B+, A−]) → A+ ⊗B+ ⊗ [A+, B−] → B+ ⊗B− B −→ Ω
A+ ⊗ B+ ⊗ ([A+, B−]× [B+, A−]) → A+ ⊗ B+ ⊗ [B+, A−] → A+ ⊗A− A −→ Ω
Now by definition of the morphisms in Dial(C,Ω), a morphism A ⊠ B → C consists of C-morphisms f+ : A+ ⊗ B+ → C+ and f− : C− → [A+, B−]× [B+, A−] such that some inequality holds. But by the universal property of products and internal-homs, to give f−
is equivalent to giving f− 1 : A+ ⊗ C− → B− and f−
2 : B+ ⊗C− → A−, and the inequality then asserts that
(A ◦ (1A+ ⊗ f− 2 ))⊠ (B ◦ (1B+ ⊗ f−
1 )) ≤ (C ◦ (f+ ⊗ 1C−)) (1.2)
in the internal order of Ω (applied pointwise to morphisms A+⊗B+⊗C− → Ω). We now note similarly that:

This is also certainly a “two-variable” generalization of the definition of ordinary morphisms A→ B in Dial(C,Ω).

It also makes sense if C is only a multicategory, with f+ : (A+, B+) → C+ etc.

In fact, it makes sense even if Ω is only a multi-poset (a multicategory having at most one morphism with any given domain and codomain, just as a poset is a category with this property), with (1.2) replaced by
( A ◦ (1A+ ⊗ f−
2 ) , B ◦ (1B+ ⊗ f− 1 )
) ≤ (C ◦ (f+ ⊗ 1C−)) (1.3)

One can again guess the correct n-to-m-variable version and write down a polycat-egorical definition, with Ω replaced by a poly-poset (a polycategory having at most one morphism in each hom-set).
THE 2-CHU-DIALECTICA CONSTRUCTION 5
Furthermore, the descriptions of morphisms A⊠B → C in Chu(C,Ω) and Dial(C,Ω) are very similar, indeed they are related in essentially the same way as the descriptions of ordinary morphisms A→ B. Specifically, the Chu construction asks for an equality, while the Dialectica construction asks for an inequality — where an “inequality” between more than two elements is interpreted with respect to a multi-poset or poly-poset structure.
This leads to our common generalization: just as equalities φ = ψ are inequalities in a discrete poset (where φ ≤ ψ is defined to mean φ = ψ), “multi-variable equalities” φ = ψ = ξ can be regarded as “multi-variable inequalities” in a “discrete poly-poset”, where an inequality (φ, ψ) ≤ (ξ) is defined to mean φ = ψ = ξ. Thus, the polycategorical Dialectica construction includes the polycategorical Chu construction. The reason the original constructions look different is that they make different additional assumptions, each of which implies that the polycategorical result is “representable” and hence defines a ∗-autonomous category — but this representability happens in different ways for the original Dialectica and Chu constructions.
In fact, we will generalize further in a few ways:

We allow Ω to be a polycategory rather than a polyposet, i.e. our construction will be “proof-relevant” in the strongest sense.

We will replace the object Ω by a not-necessarily-representable presheaf with the same structure. This allows us to include the original Dialectica constructions [dP89a, dP89b], where instead of morphisms into Ω we use subobjects, without supposing C to have a subobject classifier.

We will generalize the output of the construction to be a C-indexed family of poly-categories rather than a single one, as in [Bie08, Hof11]. This amounts to building a model of first-order rather than merely propositional linear logic.
Taken together, these generalizations imply that the output of our “Chu-Dialectica con-struction” is the same kind of thing as its input: a multicategory equipped with a presheaf of polycategories, which we call a virtual linear hyperdoctrine. I do not know whether this endomorphism of the category of virtual linear hyperdoctrines has a universal property (see [Pav93, Hof11] for universal properties of the Chu and Dialectica constructions re-spectively).
From the perspective of higher category theory, we can regard our construction as a categorification. In the original Chu construction, Ω is a discrete object, i.e. a 0-category. In the original Dialectica construction, Ω is a posetal object, a.k.a. a (0, 1)-category (where a set or 0-category is more verbosely called a (0, 0)-category). Our construction (as well as other categorified Dialectica constructions, e.g. [Bie08, Hof11]) allows Ω to be a categorical object, i.e. a (1, 1)-category.
This suggests that our construction should also specialize to a version involving (1, 0)-categories, i.e. groupoids. It seems appropriate to call this a 2-Chu construction, since it replaces the equalities in the ordinary Chu constructions by isomorphisms. The “pro-totypical” 2-Chu construction Chu(Cat , Set) (which directly categorifies the prototypical
6 MICHAEL SHULMAN
Chu construction Chu(Set, 2)) is particularly interesting as its morphisms are a “polarized” sort of multivariable adjunction.
The second introduction to the paper, which follows, reverses the flow of motivation by starting with multivariable adjunctions.
1.4. Second Introduction: The polycategory of multivariable adjunctions.
In view of the well-known importance of adjunctions in category theory, it is perhaps sur-prising that it has taken so long for multivariable adjunctions to be systematically studied. To be sure, two-variable adjunctions have a long history, and include some of the earli-est examples of adjunctions. For instance, in a biclosed monoidal category each functor (A⊗−) has a right adjoint [A,−]l, and each functor (−⊗B) has a right adjoint [B,−]r; but this is more symmetrically expressed by saying that the two-variable functor ⊗ has [−,−]l and [−,−]r as two-variable right adjoints. To be precise, in this case we have three functors
⊗ : A×A → A [−,−]l : Aop ×A → A [−,−]r : Aop ×A → A
with natural isomorphisms
A(A⊗ B,C) ∼= A(B, [A,C]l) ∼= A(A, [B,C]r).
In general, a two-variable adjunction (A,B) → C consists of functors
f : A× B → C g : Aop × C → B h : Bop × C → A
and natural isomorphisms
C(f(a, b), c) ∼= B(b, g(a, c)) ∼= A(a, h(b, c)).
In addition to biclosed monoidal structures, another well-known example is the “tensor-hom-cotensor” (or “copower-hom-power”) situation of an enriched category, which in-spired the terminology THC-situation for the general case in [Gra80]. The name ad-junction of two variables from [Hov99] was shortened in [Rie13, CGR14] to two-variable adjunction; in [Gui13] the term used is trijunction (though see below).
Of course when we have one-variable and two-variable versions of something, it is natural to expect an n-variable version. If we go back to the fact that the functors g and h in a two-variable adjunction are determined up to unique isomorphism by f , we can define an n-variable adjunction (A1, . . . ,An) → B to be a functor A1 × · · · × An → B such that if we fix its value on all but one (say Ai) of the input categories, the resulting functor Ai → B has a right adjoint. Each such right adjoint then automatically becomes contravariantly functorial on the categories Aj for j 6= i.
Unsurprisingly, multivariable adjunctions of this sort can be assembled into a multicat-egory: we can compose a two-variable adjunction (A,B) → C with another one (C,D) → E to obtain a three-variable adjunction (A,B,D) → E , and so on. However, one-variable
THE 2-CHU-DIALECTICA CONSTRUCTION 7
adjunctions are the morphisms not only of a category but of a 2-category Adj , whose 2-cells are mate-pairs of natural transformations. More generally, one-variable adjunctions form the horizontal morphisms in a double category Adj, whose vertical morphisms are single functors, and whose 2-cells are a more general kind of mate-pairs. (Recall that if f ⊣ g and h ⊣ k are adjunctions, then the “mate correspondence” is a bijection between natural transformations fu → vh and uk → gv obtained by pasting with the adjunction unit and counit. The functoriality of this bijection is conveniently expressed in terms of the double category Adj; see [KS74].)
The first step towards a similar calculus for multivariable adjunctions was taken by [CGR14], who exhibited them as the horizontal2 morphisms in a cyclic multi dou-ble category3 MAdj (i.e. an internal category in the category of cyclic multicategories). The multicategory structure of MAdj is unsurprising. Its vertical arrows of MAdj are functors and its 2-cells are natural transformations, while its cyclic structure encodes a calculus of multivariable mates, describing the behavior of multivariable adjunctions with respect to passage to opposite categories. In general, a cyclic structure on a multicategory consists of an involution (−)• on objects together with a cyclic action on morphism sets
M(A1, . . . , An;B) → M(A2, . . . , An, B

;A•

satisfying appropriate axioms. In MAdj we define A• = Aop, and the cyclic action gener-alizes the observation that a two-variable adjunction (A,B) → C is essentially the same as a two-variable adjunction (Cop,A) → Bop or (B, Cop) → Aop. The extension of this cyclic action to 2-cells then encodes the mate correspondence.
In practice, three- and higher-variable adjunctions seem to arise mainly as composites of two-variable adjunctions. But the whole multicategory structure is nevertheless useful, because it gives an abstract context in which to express conditions and axioms regarding such composites. For instance, the associativity of the tensor product in a closed monoidal category has an equivalent form involving the internal-hom [EK66]; they are 2-cells in MAdj related by the mate correspondence. Put differently, just as a monoidal category can be defined as a pseudomonoid in the 2-category Cat , a closed monoidal category can be defined as a pseudomonoid in MAdj , the horizontal 2-multicategory of MAdj. Similarly, a module over a pseudomonoid A in MAdj is an A-enriched category with powers and copowers, and so on.
In this paper I will propose a different viewpoint on MAdj: rather than a cyclic multicategory, we can regard it as a polycategory. A polycategory is like a multicategory, but it allows the codomain of a morphism to contain multiple objects, as well as the domain; thus we have morphisms like f : (A,B) → (C,D). Such morphisms can be composed only “along single objects”, with the “leftover” objects in the codomain of f
2Actually, their double categories are transposed from ours, so for them the multivariable adjunctions are the vertical morphisms.
3They called it a cyclic double multicategory, but the phrase “double multicategory” may suggest an internal multicategory in multicategories rather than the intended meaning of an internal category in multicategories, so we have chosen to order the modifiers differently.
8 MICHAEL SHULMAN
and the domain of g surviving into the codomain and domain of g ◦f . For instance, given f : (A,B) → (C,D) and g : (E,C) → (F,G) we get g ◦C f : (E,A,B) → (F,G,D).
What is a multivariable adjunction (A1, . . . ,Am) → (B1, . . . ,Bn)? There are several ways to figure out the answer. One is to inspect the definition of a multivariable adjunction (A1, . . . ,Am) → B1 and rephrase it in a way that doesn’t depend on the assumption n = 1. The functors involved in such an adjunction are
f1 : A1 × · · · × Am → B1
gi : A op 1 × · · · Âop
i · · · × Aop m × B1 → Ai (1 ≤ i ≤ m)
where Âop i indicates that Aop
i is omitted. This can be described as “for each category Ai or Bj , a functor with that codomain, whose domain is the product of all the other categories, with opposites applied to those denoted by the same letter as the codomain”. That is, the functor gi with codomain Ai depends contravariantly on all the other A’s and covariantly on the (single) B, while the functor f with codomain B1 depends contravariantly on the (zero) other B’s and covariantly on all the A’s. If we apply this description in the case n > 1 as well, we see that a multivariable adjunction (A1, . . . ,Am) → (B1, . . . ,Bn) should involve functors
fj : A1 × · · · × Am × Bop 1 × · · · B̂op
j · · · × Bop n → Bj (1 ≤ j ≤ n)
gi : A op 1 × · · · Âop
i · · · × Aop m × B1 × · · · × Bn → Ai (1 ≤ i ≤ m)
with an appropriate family of natural isomorphisms. For instance, a multivariable adjunc-tion (A,B) → (C,D) consists of four functors
f : Cop ×A× B → D g : A× B ×Dop → C
h : Aop × C × D → B k : C × D × Bop → A
and natural isomorphisms
D(f(c, a, b), d) ∼= C(g(a, b, d), c) ∼= B(b, h(a, c, d)) ∼= A(a, k(c, d, b)).
I find this definition quite illuminating already. One of the odd things about a two-variable adjunction, as usually defined, is the asymmetric placement of opposites. The polycategorical perspective reveals that this arises simply from the asymmetry of having a 2-ary domain but a 1-ary codomain: a “(2, 2)-variable adjunction” as above looks much more symmetrical.
With this definition of (m,n)-variable adjunctions in hand, it is a nice exercise to write down a composition law making them into a polycategory. For instance, suppose in addition to (f, g, h, k) : (A,B) → (C,D) as above, we have a two-variable adjunction (ℓ,m, n) : (D, E) → Z with Z(ℓ(d, e), z) ∼= D(d,m(e, z)) ∼= E(e, n(d, z)). Then we have a composite multivariable adjunction (A,B, E) → (C,Z) defined by
C(g(a, b,m(e, z)), c) ∼= Z(ℓ(f(c, a, b), e), z) ∼= A(a, k(c,m(e, z), b)) ∼= · · · .
THE 2-CHU-DIALECTICA CONSTRUCTION 9
Of course, a (1, 1)-variable adjunction is an ordinary adjunction, while a (2, 1)-variable adjunction is a two-variable adjunction as above. A (2, 0)-variable adjunction (A,B) → () consists of functors f : Aop → B and g : Bop → A and a natural isomorphism B(b, f(a)) ∼= A(a, g(b)). This is sometimes called a mutual right adjunction or dual adjunction, and arises frequently in examples, such as Galois connections betwen posets or the self-adjunction of the contravariant powerset functor. Similarly, a (0, 2)-variable adjunction () → (A,B) is a mutual left adjunction B(f(a), b) ∼= A(g(b), a). Of course a mutual right or left adjunction can also be described as an ordinary adjunction between Aop and B, or between A and Bop, but the choice of which category to oppositize is arbitrary; the polycategorical approach respects mutual right and left adjunctions as independent objects.4
More generally, an (n, 0)-variable adjunction (A1, . . . ,An) → () is a “mutual right multivariable adjunction” between n contravariant functors
fi : Ai+1 × · · · × An ×A1 × · · · × Ai−1 → Aop i .
In fact, the “mutual right” version is the formal definition of n-variable adjunction given in [CGR14] (and, in the case n = 3, of “trijunction” in [Gui13]). This makes the cyclic structure more apparent, but the enforced contravariance makes for a mismatch with many standard examples.
A further advantage of the polycategorical framework is the way that opposite cate-gories enter the picture: rather than imposed by the structure of a cyclic action, they are characterized by a universal property. Specifically, they are duals in the polycategorical sense: we have multivariable adjunctions η : () → (A,Aop) and ε : (Aop,A) → () sat-isfying analogues of the triangle identities. Opposite categories are also dual objects in the monoidal bicategory of profunctors, but the polycategory of multivariable adjunctions provides a new perspective, which in particular characterizes them up to equivalence (not just Morita equivalence).
In fact, the characterization of Aop as a polycategorical dual of A encodes almost exactly the same information as the cyclic action of [CGR14]. Any polycategory P with strict duals (a.k.a. a “∗-polycategory” [Hyl02]) has an underlying cyclic symmetric multi-category, in which the cyclic action
P(A1, . . . , An;B) → P(A2, . . . , An, B

;A•

is obtained by composing with εB and ηA1. Conversely, any cyclic symmetric multicategory M can be extended to a polycategory by defining
M(A1, . . . , Am;B1, . . . , Bn) = M(A1, . . . , Am, B

1 , . . . , B̂

j , . . . , B

n;Bj).
The cyclic structure ensures that this is independent, up to isomorphism, of j. The polycategorical composition can then be induced from the multicategorical one and the
4At this point I encourage the reader to stop and think for a while about what a (0, 0)-variable adjunction should be. The answer will be given in Remark 1.5.
10 MICHAEL SHULMAN
cyclic action, and the cyclic “duals” A• indeed turn out to be abstract polycategorical duals.
Thus symmetric polycategories with duals are almost5 equivalent to cyclic symmetric multicategories, and our polycategorical MAdj corresponds under this almost-equivalence to the cyclic MAdj of [CGR14]. This provides another a posteriori explanation of the defi-nition of (m,n)-variable adjunctions: they are exactly the morphisms in the polycategory we obtain by passing the cyclic multicategory MAdj across this equivalence. For instance, the reader may check that a (2, 2)-variable adjunction (A,B) → (C,D) could equivalently be defined to be simply a three-variable adjunction (A,B, Cop) → D (or, equivalently, (A,B,Dop) → C).
Finally, like the cyclic multicategory MAdj of [CGR14], the polycategory MAdj is in fact a poly double category (meaning an internal category in the category of polycat-egories), whose vertical arrows are functors and whose 2-cells are an appropriate sort of multivariable mate tuple. Thus, it is equally appropriate for studying the multi-variable mate correspondence. It also suggests new applications: for instance, in a 2-polycategory we can define pseudo-comonoids and Frobenius pseudomonoids, and in a future paper [Shu19] (building on [DS04, Str04, Egg10]) I will show that Frobenius pseu-domonoids in MAdj are ∗-autonomous categories.
However, there is still something unsatisfying about the picture. The double category Adj of ordinary adjunctions can actually be constructed out of internal adjunctions in any 2-category K instead of Cat ; but it is unclear exactly what the analogous statement should be for multivariable adjunctions. In particular, the definition of multivariable adjunction involves the notion of opposite category, which despite its apparent simplicity is actually one of the more mysterious and difficult-to-abstract properties of Cat . At the “one-variable” level it is simply a 2-contravariant involution Cat co ∼= Cat [Shu18], but its multivariable nature is still not fully understood (despite important progress such as [DS97, Web07]).
However, it turns out that we can avoid this question entirely if we are willing to settle for constructing something rather larger than MAdj. Upon inspection, the definition of multivariable adjunction uses very little information about the relation of a category to its opposite: basically nothing other than the existence of the hom-functors Aop ×A → Set, and nothing at all about the structure of their codomain Set. Thus, instead of trying to characterize the opposite of a category, we can simply consider “categories equipped with a formal opposite”.
Let K be a symmetric monoidal 2-category with a specified object Ω. We define an Ω-polarized object to be a triple (A+, A−, A) where A+, A− are objects of K and A : A+⊗A− → Ω. If K = Cat and Ω = Set, every category A induces a representable Set-polarized object [A] with [A]+ = Aop, [A]− = A, and [A] = homA (but see Remark 1.6).
A polarized adjunction f : A → B between polarized objects consists of morphisms f+ : A+ → B+ and f− : B− → A− and an isomorphism A ◦ (1 ⊗ f−) ∼= B ◦ (f+ ⊗ 1).
5See Remark 1.5 for why the “almost”.
THE 2-CHU-DIALECTICA CONSTRUCTION 11
Similarly, a polarized two-variable adjunction (A,B) → C consists of morphisms
f : A+ ⊗B+ → C+ g : A+ ⊗ C− → B− h : B+ ⊗ C− → A−
and isomorphisms (modulo appropriate symmetric actions)
A ◦ (1⊗ h) ∼= B ◦ (1⊗ g) ∼= C ◦ (f ⊗ 1).
We can similarly define polarized (n,m)-variable adjunctions and assemble them into a polycategory. More generally, we can take them to be the horizontal morphisms in a poly double category PolMAdj(K ,Ω); its vertical morphisms are polarized functors h : A→ B
consisting of morphisms f+ : A+ → B+ and f− : A− → B− (note that both go in the same direction) and a 2-cell A ⇒ B ◦ (f+ ⊗ f−), and its 2-cells are families of 2-cells in K satisfying a “polarized mate” relationship.
In the case K = Cat , Ω = Set, a polarized adjunction between representable polarized categories [A] → [B] reduces to an ordinary adjunction, and likewise a polarized two-variable adjunction ([A], [B]) → [C] reduces to an ordinary two-variable adjunction. More generally, we can say that PolMAdj(Cat , Set) contains our originalMAdj as a “horizontally full” subcategory (but see Remark 1.6). So there is a general 2-categorical construction that at least comes close to reproducing MAdj.
On the other hand, PolMAdj(Cat , Set) is also interesting in its own right! Its objects and vertical arrows are (modulo replacement of A+ by its opposite) the “polarized cat-egories” and functors of [CS07], which were studied as semantics for polarized logic and games. It also provides a formal context for relative adjunctions, in which one or both adjoints are only defined on a subcategory of their domain. Furthermore, at least if K is closed monoidal with pseudo-pullbacks (like Cat), the polycategory PolMAdj(K ,Ω) has (bicategorical) tensor and cotensor products (the appropriate sort of “representability” condition for a polycategory).
For instance, for polarized objects A,B there is a polarized object A ⊠ B such that polarized two-variable adjunctions (A,B) → C are naturally equivalent to polarized one-variable adjunctions A⊠ B → C. This universal property, like most others, tells us how to construct A⊠B, as follows. A polarized adjunction A⊠B → C consists of morphisms (A ⊠ B)+ → C+ and C− → (A ⊠ B)− together with a certain isomorphism; whereas in a polarized two-variable adjunction (A,B) → C as above we can apply the internal-hom isomorphism to obtain
f : A+ ⊗B+ → C+ g̃ : C− → [A+, B−] h̃ : C− → [B+, A−].
Comparing the two suggests (A⊠B)+ = A+ ⊗B+ and (A⊠B)− = [A+, B−]× [B+, A−]. The first is correct, but the second is not quite right: to incorporate the two isomor-phisms of a two-variable adjunction, we have to let (A ⊠ B)− be the pseudo-pullback [A+, B−]×ps
[A+⊗B+,Ω] [B +, A−]. The third datum is the composite
A⊠ B = ((
[A+,B−]×ps
[A+⊗B+,Ω] [B+,A−]
) ⊗A+⊗B+→[A+⊗B+,Ω]⊗A+⊗B+→Ω
) .
12 MICHAEL SHULMAN

[... content truncated ...]

---

*Source: `polycategory of multivariable adjunctions.pdf.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
