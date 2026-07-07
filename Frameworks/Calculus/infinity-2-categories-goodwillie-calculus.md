---
stub: true
title: "Infinity 2 Categories Goodwillie Calculus"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [zero_divisor, "ingested"]
sources: ["infinity-2-categories-goodwillie-calculus.md"]
psi_tier: zero_divisor
---

# Infinity 2 Categories Goodwillie Calculus

# (∞, 2)-Categories.pdf

(∞, 2)-Categories and the Goodwillie Calculus I

October 8, 2009
Contents
1 Complete Segal Spaces 6 1.1 Category Objects and Groupoid Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 1.2 Segal Spaces and Complete Segal Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 1.3 Higher-Dimensional Complete Segal Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 1.4 Cat∞ as an Absolute Distributor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 1.5 Models for Complete Segal Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2 Segal Categories 36 2.1 Basic Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 2.2 The Projective Model Structure on SegA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40 2.3 The Injective Model Structure on SegA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3 Straightening for Locally coCartesian Fibrations 65 3.1 Scaled Simplicial Sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 3.2 Locally coCartesian Model Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72 3.3 Flat Inner Fibrations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88 3.4 Functoriality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 3.5 Scaled Straightening and Unstraightening . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114 3.6 Straightening over a Point . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121 3.7 Straightening over a Simplex . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123 3.8 Straightening in General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
4 ∞-Bicategories 133 4.1 The Scaled Slice Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133 4.2 ∞-Bicategories and Set+
∆-Enriched Categories . . . . . . . . . . . . . . . . . . . . . . . . . . . 141 4.3 Subdivision . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145 4.4 Application: Automorphisms of Cat∞ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152 4.5 Application: Comparison of Universal Fibrations . . . . . . . . . . . . . . . . . . . . . . . . . 156
5 The Goodwillie Calculus 159 5.1 Derivatives and Linearizations of Functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160 5.2 Linearization in Families . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169 5.3 Linearization as a Functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176 5.4 Adjoint Functors and Linearization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
1
Introduction
The theory of higher categories is notorious for having an excessive proliferation of definitions, many of which are difficult to compare with one another. Nevertheless, a general consensus has emerged in some special cases. Let us use the term (∞, n)-category to indicate a higher category in which all k-morphisms are assumed to be invertible for k > n. It has long been understood that the theory of (∞, 0)-categories (that is, higher categories in which all morphisms are required to be invertible) should be equivalent to classical homotopy theory. Consequently, for practical purposes one can define an (∞, 0)-category to be a topological space, or a simplicial set which satisfies the Kan extension condition.
The theory of (∞, 1)-categories is also quite well understood, though in this case there is a variety of possible approaches. Arguably the simplest of these is the Boardman-Vogt theory weak Kan complexes: that is, simplicial sets which satisfy a weaker version of the Kan extension condition (these are also known as quasicategories in the literature; we will follow the terminology of [40] and refer to them simply as ∞-categories). However, there are a number of other possible approaches: for example, one could define an (∞, 1)-category to be a topological category (that is, a category C in which every mapping set HomC(X,Y ) is endowed with a topology, such that the composition of morphisms is continuous), a simplicial category, a Segal category, or a complete Segal space. These notions are equivalent to one another. More precisely, we have the following:
Theorem 0.0.1. There is a diagram of right Quillen equivalences
Set∆ Cat∆ Noo
 Fun(∆op, Set∆)
G0
OO
// SegSet∆ ,
with the following features:
(A1) In the upper left hand corner, we have the category Set∆ of simplicial sets, endowed with the Joyal model structure (see §T.2.2.5). The fibrant objects of Set∆ are precisely the ∞-categories.
(A2) In the upper right corner, we have the category Cat∆ of simplicial categories, with the model structure constructed by Bergner in [7]; see also §T.A.3.2.
(A3) In the lower right corner, we have the category SegSet∆ of preSegal categories: that is, bisimplicial sets X•• with the property that the 0th column X•0 is a constant simplicial set. These we endow with the projective model structure (see Theorem 2.2.16).
(A4) In the lower left corner, we have the category Fun(∆op, Set∆) of all bisimplicial sets, which we endow with the complete Segal model structure introduced by Rezk (see [57] or Proposition 1.5.4).
(B1) The upper horizontal arrow is given by the homotopy coherent nerve functor N : Cat∆ → Set∆ of Cordier and Porter. This is a right Quillen equivalence by virtue of Theorem T.2.2.5.1 (an alternative proof is given in [32]). We denote the left adjoint of this functor by C : Set∆ → Cat∆.
(B2) The left vertical arrow is given by the forgetful functor G0 : Fun(∆op, Set∆) → Set∆ which carries a bisimplicial set X•• to the 0th row X0•. Joyal and Tierney have shown that this functor is a right Quillen equivalence (see [33]); we will reprove this result as Corollary 4.3.14.
(B3) The right vertical arrow associates to every simplicial category C• the bisimplicial set N(C•)• obtained by applying the nerve construction degreewise. It determines a fully faithful embedding from the category Cat∆ of simplicial categories to the category SegSet∆ of preSegal categories, and is a right Quillen equivalence (a proof of this result is given in [10]; we will prove a generalization of this result as Theorem 2.2.16).
2
(B4) The lower horizontal arrow denotes a right adjoint to the inclusion SegSet∆ ⊆ Fun(∆op, Set∆). Bergner has shown that this functor is a right Quillen equivalence (see [10]; we will prove a generalization of this result as Proposition 2.3.1).
Remark 0.0.2. There is a sense in which the diagram of Theorem 0.0.1 is commutative up to homotopy. Let F0 : Set∆ → Fun(∆op, Set∆) be a left adjoint to G0, and let F1 : Set∆ → Fun(∆op, Set∆) denote the composition
Set∆ C→ Cat∆ ⊆ SegSet∆ ⊆ Fun(∆op, Set∆).
There exists another functor F : Set∆ → Fun(∆op, Set∆) and a pair of natural transformations F0 ← F → F1
with the following property: for every simplicial set X, the induced maps F0(X) ← F (X) → F1(X) are weak equivalences (with respect to the complete Segal model structure on Fun(∆op, Set∆)).
To describe the functor F : Set∆ → Fun(∆op, Set∆), it is convenient to introduce yet another object: the category (Set∆)/N(∆op) of simplicial sets X equipped with a map X → N(∆op), where ∆ denotes the category of simplices. This category is related to the category Fun(∆op, Set∆) by a pair of adjoint functors
(Set∆)/N(∆)op F•(∆
op)// Fun(∆op, Set∆) N•(∆
op) oo
where N•(∆op) denotes the relative nerve functor introduced in §T.3.2.5. It follows from Proposition T.3.2.5.18 that these adjoint functors determine a Quillen equivalence between (Set∆)/N(∆)op (endowed with the covariant model structure) and Fun(∆op, Set∆) (endowed with the injective model structure). Passing to localizations, we deduce the existence of a Quillen equivalence between the category Fun(∆op, Set∆) (en-dowed with the complete Segal model structure) and (Set∆)/N(∆)op (endowed with a suitable localization of the covariant model structure).
Let X be a simplicial set, viewed as a covariant functor from ∆op into the category of sets. By means of a Grothendieck construction, we can think of X in a different way: as a category cofibered in sets over ∆op. More precisely, let ∆X denote the category of simplices of X: the objects of ∆X are given by maps of simplicial sets ∆n → X where n ≥ 0, and morphisms by commutative diagrams
∆m
!!DDDDDDDD // ∆n
}}{{{{{{{{
X.
We can then view the nerve N(∆X)op as an object of (Set∆)/N(∆)op . This construction determines a fully faithful embedding of Set∆ into (Set∆)/N(∆)op , which we will denote by sd. The functor F is defined to be the composition
Set∆ sd→ (Set∆)/N(∆)op
F•(∆ op)→ Fun(∆op, Set∆).
(For a definition of the natural transformations F0 ← F → F1, and the verification that they have the asserted properties, we refer the reader to §4.3).
We can describe the situation informally as follows: there are a number of models for the theory of (∞, 1)-categories which are known to be equivalent to one another, via more-or-less explicit combinatorial constructions. The main goal of this paper is to establish an analogous picture for the theory of (∞, 2)-categories; moreover, all of the essential players are slightly more elaborate versions of their (∞, 1)-categorical counterparts. There is one exception: we do not have an obvious analogue of the adjoint functors (F0, G0) in the (∞, 2)-categorical setting. However, we do have an analogue of the functor F , which serves as an adequate replacement. Our main results can be summarized as follows:
3
Theorem 0.0.3. There is a diagram of model categories and right Quillen equivalences
Setsc ∆
CatSet+ ∆
oo
 (Set+∆)/N(∆)op
OO
SegSet+ ∆
Fun(∆op, Set+ ∆) //
OO
SegSet+ ∆
OO
where:
(A1) In the upper left hand corner, we have the category Setsc ∆ of scaled simplicial sets: that is, pairs (X,T )
where X is a simplicial set and T is a collection of 2-simplices in X, which includes all degenerate 2-simplices.
(A2) In the upper right hand corner, we have the category CatSet+ ∆
of Set+ ∆-enriched categories, or marked
simplicial categories. Here Set+ ∆ denotes the category of marked simplicial sets: that is, pairs (X,M)
where X is a simplicial set and M a collection of 1-simplices of X, which includes all degenerate 1-simplices. (We can think of an object of CatSet+
∆ as a simplicial category C, such that for every pair of
objects x, y ∈ C, the simplicial set MapC(x, y) comes equipped with a distinguished class of edges, which are required to be stable under composition.)
(A3) In the lower right corner of the diagram, we have the category SegSet+ ∆
of Set+ ∆-enriched preSegal
categories, endowed with the projective model structure of Theorem 2.2.16. This can be viewed as the full subcategory of Fun(∆op, Set+
∆) spanned by those marked bisimplicial sets X•• such that each X•0 is a constant simplicial set.
(A4) In the lower left corner of the diagram, we have the category Fun(∆op, Set+ ∆) of simplicial objects of
Set+ ∆. We regard this category as endowed with a localization of the injective model structure which we
will refer to as the complete Segal model structure (see Proposition 1.5.4).
(A5) In the middle left side of the diagram, we have the category (Set+∆)/N(∆)op whose objects are simplicial sets X equipped with both a marking and a map X → N(∆)op. We endow this category with a suitable localization of the coCartesian model structure, which is described in Proposition 1.5.7.
(A6) In the middle right side of the diagram, we have the category SegSet+ ∆
of Set+ ∆-enriched preSegal cate-
gories, endowed with the injective model structure of Proposition 2.3.1.
(B1) The upper horizontal functor Nsc : CatSet+ ∆ → Setsc
∆ is a decorated version of the homotopy coherent nerve N: it carries a marked simplicial category C to the pair (N(C), T ), where T is a collection of 2-simplices in C which depends on the collection of marked edges in the mapping spaces MapC(x, y) (for the complete definition, we refer the reader to Definition 3.1.10). The functor Nsc admits a left adjoint, which we will denote by Csc.
(B2) The upper left vertical arrow (Set+∆)/N(∆)op → Setsc ∆ is defined as the right adjoint to a functor sd+ :
Setsc ∆ → (Set+∆)/N(∆)op , which is a decorated version of the functor sd : Set∆ → (Set∆)/N(∆)op described
in Remark 0.0.2 (in other words, we have sd+(X,T ) = (sd(X),M), where M is a collection of edges in sd(X) = N(∆X)op which depends on the collection T of 2-simplices in X).
(B3) The upper right vertical arrow is a fully faithful embedding CatSet+ ∆ ↪→ SegSet+
∆ , which is a decorated
version of the embedding CatSet∆ → SegSet∆ : to a marked simplicial category C•, it associates the bisimplicial set N(C•)• obtained by applying the nerve construction degreewise (endowed with a suitable marking).
4
(B4) The bottom horizontal arrow is a right adjoint to the inclusion functor SegSet+ ∆ ↪→ Fun(∆op, Set+
∆).
(B5) The lower left vertical arrow is given by the marked relative nerve functor N+

(∆op) described in
§T.3.2.5. We denote the left adjoint to this functor by F+

(∆op).
(B6) The lower right vertical arrow is the identity functor, which is a right Quillen equivalence by virtue of Proposition 2.3.9.
Moreover, this diagram is commutative in the following sense: there exists a natural transformation of functors α : F → F ′ where F denotes the composition
Setsc ∆ sd+
→ (Set+∆)/N(∆)op F+

(∆op)→ Fun(∆op, Set+
∆)
and F ′ the composition Setsc
∆ Csc
→ CatSet+ ∆ ↪→ SegSet+
∆ ↪→ Fun(∆op, Set+
∆).
Furthermore, for every scaled simplicial set X, the map α(X) : F (X)→ F ′(X) is a weak equivalence (with respect to the complete Segal model structure on Fun(∆op, Set+
∆)).
Remark 0.0.4. In Theorem 0.0.3, the category Set+ ∆ of marked simplicial sets plays the role of a good
model for the theory of (∞, 1)-categories. Some of the assertions of Theorem 0.0.3 continue to hold if we replace Set+
∆ by other models. For example, the forgetful functor Set+ ∆ → Set∆ determines a right Quillen
equivalence if we endow Set∆ with the Joyal model structure (Theorem T.3.1.5.1). This gives rise to a commutative diagram of right Quillen equivalences
CatSet+ ∆
//

CatSet∆
 SegSet+
∆ // SegSet∆
Fun(∆op, Set+ ∆)
OO
// Fun(∆op, Set∆)
OO
which gives us another three models for the theory of (∞, 2)-categories. (Here the left column consists of Quillen equivalences appearing Theorem 0.0.3, and the right column is defined analogously.)
The bulk of this paper will be devoted to constructing the diagram described in Theorem 0.0.3 and verifying that it has the desired properties. We begin in §1 by reviewing Rezk’s theory of complete Segal spaces. We will present a variation on his definitions, which will allow us to define the model categories described in (A3) and (A5), and to establish the Quillen equivalence described in (B5). In §2, we will review the formalism of Segal categories, which we will use to define the model categories described in (A4) and (A6) and to establish the Quillen equivalences of (B3), (B4), and (B6).
The notions of Segal categories and complete Segal spaces have the virtue of generalizing to higher dimensions: using the work of Simpson-Tamsamani or Barwick, one can give a definition of (∞, n)-category for any nonnegative integer n, using induction on n. However, in either case, the resulting theory describes an (∞, n)-category as an (n + 1)-uple simplicial set. Consequently, these definitions increase in complexity with n, and become somewhat cumbersome to work with directly. Our goal in §4 is to provide an alternative definition in the case n = 2 which does not share this defect. We will achieve this goal by introducing a theory of scaled simplicial sets. Our definition was inspired by Verity’s work on stratified simplicial sets (see [73] and [74]), though our goals are considerably less ambitious. We will use it to define the model category described in (A1), and to construct the Quillen equivalences of (B1) and (B2). In order to carry out the details, we will need an analogue of straightening and unstraightening constructions of §T.3.2 to the setting
5
of locally coCartesian fibrations, which we provide in §3. These constructions will be presecan be regarded as providing a higher-categorical version of the Grothendieck construction for lax functors, and should be useful in a variety of other contexts.
Our original goal in developing the theory described in this paper is to have an adequate higher-categorical language for describing Goodwillie’s calculus of functors. In §5, we will review the rudiments of Goodwillie’s theory (namely, the theory of first derivatives) from a higher-categorical point of view. The material of §5 is almost entirely independent of the remainder of the paper, except for the final section (§5.3) where we explain how to interpret the theory of Goodwillie derivatives as giving rise to a functor between (∞, 2)-categories.
Remark 0.0.5. The material presented here is really only the first step in a much larger project, whose aim is to understand the Goodwillie calculus in terms of higher category theory. We plan to return to this subject in [49].
1 Complete Segal Spaces
In this section, we will review Rezk’s theory of complete Segal spaces, and the higher dimensional gen-eralization thereof (due to Barwick). Let us begin by sketching the basic idea. Suppose that C is an (∞, n)-category. We would like to describe C in terms of invariants of a less sophisticated nature: for exam-ple, (∞, k)-categories for k < n. We can begin by extracting an (∞, 0)-category C0 from C, by discarding all of the noninvertible morphisms in C at all levels. The passage from C to C0 involves a loss of information: C0 knows everything about the objects of C, but nothing about noninvertible morphisms between them. To retain this information, we first note that for every pair of objects X,Y ∈ C, we expect to have an (∞, n−1)-category of morphisms MapC(X,Y ). This (∞, n − 1)-category depends functorially on the pair X,Y ∈ C0. Consequently, we can organize the collection of all of the (∞, n − 1)-categories {MapC(X,Y )}X,Y ∈C into a single (∞, n− 1)-category C1, whose objects are given by triples (X ∈ C0, Y ∈ C0, f ∈ MapC(X,Y )). More generally, for each k ≥ 0, we can consider an (∞, n− 1)-category Ck consisting of (2k + 1)-tuples
(X0 ∈ C0, X1 ∈ C0, . . . , Xk ∈ C0, f1 ∈ MapC(X0, X1), . . . , fk ∈ MapC(Xk−1, Xk))}
in other words, composable sequences of morphisms
X0 f1→ X1
f2→ X2 f2→ . . .
fk→ Xk.
The collection of (∞, n − 1)-categories {Ck}k≥0 forms a simplicial (∞, n − 1)-category C• satisfying the following Segal condition:
(A1) For each k ≥ 0, the canonical map
Ck → C1×C0 C1×C0 . . .×C0 C1
is an equivalence of (∞, n− 1)-categories.
This simply encodes the idea that an object of Ck consists of a sequence of k morphisms {fi}1≤i≤k in C, constrained only by the requirement that the domain of each fi+1 is the codomain of fi.
Conversely, if we are given a simplicial (∞, n− 1)-category C• satisfying the Segal condition (A1), then we should be able to extract an (∞, n)-category C as follows:

The objects of C are the objects of C0.

Given a pair of objects X,Y ∈ C0, the (∞, n− 1)-category of maps MapC(X,Y ) is given by the fiber product {X} ×C0 C1×C0{Y }.
6

Given a sequence of objects X0, . . . , Xk ∈ C0, the composition law
MapC(X0, X1)× . . .MapC(Xk−1, Xk)→ MapC(X0, Xk)
is given by the composite map
({X0} ×C0 C1×C0{X1})× . . .× ({Xk−1} ×C0 C1×C0{Xk}) ∼← Ck ×C0×...×C0({X0} × . . .× {Xk}) → {X0} ×C0 C1×C0{Xk}.
Here the invertibility of the first map follows from assumption (A1).
This construction determines a left inverse (up to equivalence) to the earlier process which extracts a sim-plicial (∞, n − 1)-category from an (∞, n)-category. However, it is not generally a right inverse, because generally the underlying (∞, 0)-category of C does not agree with the C0. To rule out this phenomenon, we need to make two additional assumptions on C•:
(A2) The (∞, n− 1)-category C0 is an (∞, 0)-category.
(A3) The simplicial (∞, n− 1)-category C• is complete (see Definition 1.2.10).
Our objective is to make the above ideas precise, working in a general ∞-categorical context. We begin in §1.1 by introducing the notion of a category object of an ∞-category Y: that is, a simplicial object of Y
satisfying axiom (A1) (the case of interest is that in which Y is some version of the theory of (∞, n − 1)-categories). In order to formulate axiom (A2), we need need to assume that Y is equipped with a suitable subcategory X ⊆ Y of “∞-groupoids”. In §1.2, we will formulate analogues of (A2) and (A3) under the assumption that the inclusion X ⊆ Y is a distributor (see Definition 1.2.1). By imposing (A1), (A2), and (A3), we will obtain a full subcategory CSSX⊆Y ⊆ Fun(N(∆)op,Y) which we will refer to as the ∞-category of complete Segal space objects of Y. In §1.3, we will show that the diagonal embedding X → CSSX⊆Y
gives rise to another distributor, so the construction Y 7→ CSSX⊆Y can be iterated. To obtain the theory of (∞, n)-categories, we simply apply this construction n times, with initial data X = Y = S. In §1.4 we will present an alternative construction: we can begin instead with the distributor S ⊆ Cat∞ and apply the above construction (n− 1) times. (The fact that these two constructions give the same result is not obvious: it depends on the equivalence between our theory of ∞-categories and the theory of complete Segal spaces. This is a result of Joyal and Tierney which we will later reprove as Corollary 4.3.14.)
We will conclude this section with §1.5, where we reformulate the theory of complete Segal space objects in the language of model categories and use it to explain part of Theorem 0.0.3.
1.1 Category Objects and Groupoid Objects
Let E be an ordinary category. Then E is determined (up to canonical isomorphism) by the simplicial set N(E). In other words, we can regard the ordinary category Cat of small categories as a full subcategory of the category Set∆ of simplicial sets. Moreover, we can give a simple explicit characterization of this subcategory: a simplicial set X• is isomorphic to the nerve of a category if and only if, for every n ≥ 0, the canonical map Xn → X1 ×X0 X1 ×X0 . . .×X0 X1 is a bijection. Motivated by this observation, we introduce the following definition:
Definition 1.1.1. Let C be an∞-category. A category object of C is a simplicial object X ∈ Fun(N(∆)op,C) with the following property: for every integer n ≥ 0, the functor X exhibits X([n]) as a limit of the diagram
X({0, 1})
$$HHHHHHHHHH
yyrrrrrrrrrr . . .
~~ ~~~~~~~~~
@@@@@@@@@@ X({n− 1, n})
yyrrrrrrrrrrr
''OOOOOOOOOOO
X({0}) . . . . . . X({n}).
(Here abuse notation identifing a nonempty finite linearly ordered set I with the corresponding object of ∆op.) Let Cat(C) denote the full subcategory of Fun(N(∆)op,C) spanned by the category objects.
7
Example 1.1.2. Let C be (the nerve of) the category of sets. Then we can identify category objects of C
with ordinary categories.
In other words, a simplicial object X• is a category object if, for each n ≥ 0, the canonical map
Xn → X1 ×X0 X1 ×X0 × . . .×X0 X1
is an equivalence in C; here the right hand side is well-defined so long as C admits pullbacks.
Example 1.1.3. Let C be an ∞-category, and let Gpd(C) denote the full subcategory of Fun(N(∆)op,C) spanned by the groupoid objects of C (see Definition T.6.1.2.7). Then Gpd(C) ⊆ Cat(C).
Example 1.1.4. Let C be an∞-category. For every object C ∈ C, the constant functor N(∆)op → {C} ⊆ C
is a groupoid object of C. This construction determines a fully faithful embedding δ : C→ Gpd(C). We will say that a groupoid object of C is constant if it lies in the essential image of δ.
If C admits small colimits, then the functor δ admits a left adjoint, given by the geometric realization construction
Gpd(C) ⊆ Fun(N(∆)op,C) colim→ C .
It follows that if C is presentable, then the full subcategory of constant groupoid objects of C is an accessible localization Gpd(C) (see §T.5.5.4).
Remark 1.1.5. Since the simplicial set N(∆)op is weakly contractible, a simplicial object X• of an ∞-category C is constant if and only if, for every morphism [m]→ [n] in ∆, the induced map Xn → Xm is an equivalence.
For our purposes, the most important special case of Definition 1.1.1 is that in which C is the∞-category S of spaces. A category object of S is usually called a Segal space. We will later see that every Segal space X• determines an∞-category. In particular, we can extract a homotopy category from X•, which is enriched over the homotopy category H of spaces. Our next goal is to explain how to extract this homotopy category directly from X•:
Definition 1.1.6. Let X• be a category object of S, and let H = hS denote the homotopy category of spaces. We define a H-enriched category, the homotopy category hX•, as follows:
(1) The objects of hX• are the points of X0.
(2) Given a pair of points x, y ∈ X0, we define MaphX•(x, y) to be the homotopy fiber product
{x} ×X0 X1 ×X0 {y} ∈ H .
(3) Given a sequence of points x0, . . . , xn ∈ X0, the associated composition law is given by the composition∏ 1≤i≤n
MaphX•(xi−1, xi) ∼→ {x0} ×X0 X1 ×X0 {x1} ×X0 X1 ×X0 . . .×X0 {xn−1} ×X0 X1 ×X0 {xn}
→ {x0} ×X0 X1 ×X0 X1 ×X0 . . .×X0 X1 ×X0 {xn} ∼← {x0} ×X0 Xn ×X0 {xn} ' MaphX•(x0, xn).
Note that every point f ∈ X1 determines a morphism in the homotopy category hX•, which we will denote by [f ].

[... content truncated ...]

---

*Source: `infinity-2-categories-goodwillie-calculus.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
