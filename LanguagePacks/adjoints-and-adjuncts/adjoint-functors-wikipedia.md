---
stub: false
title: Adjoint functors - Wikipedia
created: 2026-05-11
updated: 2026-05-13
type: concept
tags: ['category-theory', 'operator-theory', 'omega-point', 'torsion-theory', 'logic', 'mathematics', 'linguistics']
confidence: medium
sources: [Adjoint functors - Wikipedia.md]
---

# Adjoint functors - Wikipedia

Jump to contentMain menu    Navigation

Main page

Contents

Current events

Random article

About Wikipedia

Contact us
Contribute

Help

Learn to edit

Community portal

Recent changes

Upload file

Special pages

Search  Donate

Create account

Log in

Donate

Create account

Log in

(Top)
1   Terminology and notation
2   Introduction and motivation  2.1   Solutions to optimization problems
2.2   Symmetry of optimization problems
3   Formal definitions  3.1   Conventions
3.2   Definition via universal morphisms
3.3   Definition via Hom-sets
3.4   Definition via counit–unit
4   History
5   Examples  5.1   Free groups
5.2   Free constructions and forgetful functors
5.3   Diagonal functors and limits
5.4   Colimits and diagonal functors
5.5   Further examples  5.5.1   Algebra
5.5.2   Topology
5.5.3   Posets
5.5.4   Category theory
5.5.5   Categorical logic
5.5.6   Probability
6   Adjunctions in full  6.1   Universal morphisms induce hom-set adjunction
6.2   counit–unit adjunction induces hom-set adjunction
6.3   Hom-set adjunction induces all of the above
7   Properties  7.1   Existence
7.2   Uniqueness
7.3   Composition
7.4   Limit preservation
7.5   Additivity
8   Relationships  8.1   Universal constructions
8.2   Equivalences of categories
8.3   Monads
9   Notes
10   References
11   External links

Adjoint functors

Čeština

Deutsch

Español

Français

한국어

Italiano

עברית

日本語

Polski

Português

Русский

Українська

中文
Edit links
Tools    Actions

Read

Edit

View history
General

What links here

Related changes

Upload file

Permanent link

Page information

Cite this page

Get shortened URL

Download QR code
Print/export

Download as PDF

Printable version
In other projects

Wikidata item
From Wikipedia, the free encyclopedia   Relationship between two functors abstracting many common constructions   For the construction in field theory, see Adjunction (field theory). For the construction in topology, see Adjunction space.   This article includes a list of general references, but it lacks sufficient corresponding inline citations.  Please help to improve this article by introducing more precise citations.
( January 2025 )
(Learn how and when to remove this message
)
In mathematics, specifically category theory,
adjunction
is a relationship that two functors may exhibit, intuitively corresponding to a weak form of equivalence between two related categories. Two functors that stand in this relationship are known as
adjoint functors
, one being the
left adjoint
and the other the
right adjoint
.[ 1 ] Pairs of adjoint functors are ubiquitous in mathematics and often arise from constructions of "optimal solutions" to certain problems (i.e., constructions of objects having a certain universal property), such as the construction of a free group on a set in algebra, or the construction of the Stone–Čech compactification of a topological space in topology.
By definition, an adjunction between categories  C   {\displaystyle {\mathcal {C}}}    and  D   {\displaystyle {\mathcal {D}}}    is a pair of functors (assumed to be covariant)
F   :   D   →   C   {\displaystyle F:{\mathcal {D}}\rightarrow {\mathcal {C}}}    and  G   :   C   →   D   {\displaystyle G:{\mathcal {C}}\rightarrow {\mathcal {D}}}
and, for all objects  c   {\displaystyle c}    in  C   {\displaystyle {\mathcal {C}}}    and  d   {\displaystyle d}    in  D   {\displaystyle {\mathcal {D}}}   , a bijection between the respective morphism sets
h   o   m   C   (   F   d   ,   c   )   ≅   h   o   m   D   (   d   ,   G   c   )   {\displaystyle \mathrm {hom} _{\mathcal {C}}(Fd,c)\cong \mathrm {hom} _{\mathcal {D}}(d,Gc)}
such that this family of bijections is natural in  c   {\displaystyle c}    and  d   {\displaystyle d}   .[ 1 ] For locally small categories, naturality here means that there are natural isomorphisms between the pair of functors  C   (   F   −   ,   c   )   :   D   →   S   e   t   op   {\displaystyle {\mathcal {C}}(F-,c):{\mathcal {D}}\to \mathrm {Set^{\text{op}}} }    and  D   (   −   ,   G   c   )   :   D   →   S   e   t   op   {\displaystyle {\mathcal {D}}(-,Gc):{\mathcal {D}}\to \mathrm {Set^{\text{op}}} }    for a fixed  c   {\displaystyle c}    in  C   {\displaystyle {\mathcal {C}}}   , and also the pair of functors  C   (   F   d   ,   −   )   :   C   →   S   e   t   {\displaystyle {\mathcal {C}}(Fd,-):{\mathcal {C}}\to \mathrm {Set} }    and  D   (   d   ,   G   −   )   :   C   →   S   e   t   {\displaystyle {\mathcal {D}}(d,G-):{\mathcal {C}}\to \mathrm {Set} }    for a fixed  d   {\displaystyle d}    in  D   {\displaystyle {\mathcal {D}}}   . For other categories, naturality is defined as a generalisation of this.[ 1 ]
The functor  F   {\displaystyle F}    is called a
left adjoint functor
or
left adjoint to  G   {\displaystyle G}
, while  G   {\displaystyle G}    is called a
right adjoint functor
or
right adjoint to  F   {\displaystyle F}
. We write  F   ⊣   G   {\displaystyle F\dashv G}   .[ 1 ]
An adjunction between categories  C   {\displaystyle {\mathcal {C}}}    and  D   {\displaystyle {\mathcal {D}}}    is somewhat akin to a "weak form" of an equivalence between  C   {\displaystyle {\mathcal {C}}}    and  D   {\displaystyle {\mathcal {D}}}   , and indeed every equivalence gives an adjunction, though the equivalence itself is not necessarily an adjunction.[ 2 ] In many situations, an adjunction can be "upgraded" to an equivalence, by a suitable natural modification of the involved categories and functors.

Terminology and notation

[edit]
The terms adjoint and adjunct are both used, and are cognates: one is taken directly from Latin, the other from Latin via French. In the classic text
Categories for the Working Mathematician
, Mac Lane makes a distinction between the two.[ 3 ] Given a family
φ   c   d   :   h   o   m   C   (   F   d   ,   c   )   ≅   h   o   m   D   (   d   ,   G   c   )   {\displaystyle \varphi _{cd}:\mathrm {hom} _{\mathcal {C}}(Fd,c)\cong \mathrm {hom} _{\mathcal {D}}(d,Gc)}
of hom-set bijections, we call  φ   {\displaystyle \varphi }    an
adjunction
or an
adjunction between  F   {\displaystyle F}    and  G   {\displaystyle G}
.[ 1 ][ 3 ] If  f   {\displaystyle f}    is an arrow in  h   o   m   C   (   F   d   ,   c   )   {\displaystyle \mathrm {hom} _{\mathcal {C}}(Fd,c)}   , Mac Lane calls  φ   f   {\displaystyle \varphi f}    the right
adjunct
of  f   {\displaystyle f}   .[ 3 ] The functor  F   {\displaystyle F}    is
left adjoint
to  G   {\displaystyle G}   , and  G   {\displaystyle G}    is
right adjoint
to  F   {\displaystyle F}   .[ 1 ][ 3 ] (Note that  G   {\displaystyle G}    may have itself a right adjoint that is quite different from  F   {\displaystyle F}   ; see below for an example.)
In general, the phrases "   F   {\displaystyle F}    is a left adjoint" and "   F   {\displaystyle F}    has a right adjoint" are equivalent. We call  F   {\displaystyle F}    a left adjoint because it is applied to the left argument of  h   o   m   C   {\displaystyle \mathrm {hom} _{\mathcal {C}}}   , and  G   {\displaystyle G}    a right adjoint because it is applied to the right argument of  h   o   m   D   {\displaystyle \mathrm {hom} _{\mathcal {D}}}   .
If
F
is left adjoint to
G
, we also write
F   ⊣   G   .   {\displaystyle F\dashv G.}  [ 1 ]The terminology comes from the Hilbert space idea of adjoint operatorsT   {\displaystyle T}   ,  U   {\displaystyle U}    with  ⟨   T   y   ,   x   ⟩   =   ⟨   y   ,   U   x   ⟩   {\displaystyle \langle Ty,x\rangle =\langle y,Ux\rangle }   , which is formally similar to the above relation between hom-sets. The analogy to adjoint maps of Hilbert spaces can be made precise in certain contexts.[ 4 ]

Introduction and motivation

[edit]
The slogan is "Adjoint functors arise everywhere".
— Saunders Mac Lane, Categories for the Working Mathematician
Common mathematical constructions are very often adjoint functors. Consequently, general theorems about left/right adjoint functors encode the details of many useful and otherwise non-trivial results. Such general theorems include the equivalence of the various definitions of adjoint functors, the uniqueness of a right adjoint for a given left adjoint, the fact that left/right adjoint functors respectively preserve colimits/limits (which are also found in every area of mathematics), and the general adjoint functor theorems giving conditions under which a given functor is a left/right adjoint.

Solutions to optimization problems

[edit]
In a sense, an adjoint functor is a way of giving the
most efficient
solution to some problem via a method that is
formulaic
. For example, an elementary problem in ring theory is how to turn a rng (which is like a ring that might not have a multiplicative identity) into a ring. The
most efficient
way is to adjoin an element '1' to the rng, adjoin all (and only) the elements that are necessary for satisfying the ring axioms (e.g.
r
+1 for each
r
in the ring), and impose no relations in the newly formed ring that are not forced by axioms. Moreover, this construction is
formulaic
in the sense that it works in essentially the same way for any rng.
This is rather vague, though suggestive, and can be made precise in the language of category theory: a construction is
most efficient
if it satisfies a universal property, and is
formulaic
if it defines a functor. Universal properties come in two types: initial properties and terminal properties. Since these are dual notions, it is only necessary to discuss one of them.
The idea of using an initial property is to set up the problem in terms of some auxiliary category
E
, so that the problem at hand corresponds to finding an initial object of
E
. This has an advantage that the
optimization
—the sense that the process finds the
most efficient
solution—means something rigorous and recognisable, rather like the attainment of a supremum. The category
E
is also formulaic in this construction, since it is always the category of elements of the functor to which one is constructing an adjoint.
Back to our example: take the given rng
R
, and make a category
E
whose
objects
are rng homomorphisms
R
→
S
, with
S
a ring having a multiplicative identity. The
morphisms
in
E
between
R
→
S
1 and
R
→
S
2 are commutative triangles of the form (
R
→
S
1,
R
→
S
2,
S
1 →
S
2) where  S1 → S2 is a ring map (which preserves the identity). (Note that this is precisely the definition of the comma category of
R
over the inclusion of unitary rings into rng.) The existence of a morphism between
R
→
S
1 and
R
→
S
2 implies that
S
1 is at least as efficient a solution as
S
2 to our problem:
S
2 can have more adjoined elements and/or more relations not imposed by axioms than
S
1. Therefore, the assertion that an object
R
→
R
∗ is initial in
E
, that is, that there is a morphism from it to any other element of
E
, means that the ring
R
* is a
most efficient
solution to our problem.
The two facts that this method of turning rngs into rings is
most efficient
and
formulaic
can be expressed simultaneously by saying that it defines an
adjoint functor
. More explicitly: Let
F
denote the above process of adjoining an identity to a rng, so
F
(
R
)=
R
∗. Let
G
denote the process of "forgetting" whether a ring
S
has an identity and considering it simply as a rng, so essentially
G
(
S
)=
S
. Then
F
is the
left adjoint functor
of
G
.
Note however that we haven't actually constructed
R
∗ yet; it is an important and not altogether trivial algebraic fact that such a left adjoint functor
R
→
R
∗ actually exists.

Symmetry of optimization problems

[edit]
It is also possible to
start
with the functor
F
, and pose the following (vague) question: is there a problem to which
F
is the most efficient solution?
The notion that
F
is the
most efficient solution
to the problem posed by
G
is, in a certain rigorous sense, equivalent to the notion that
G
poses the
most difficult problem
that
F
solves.
This gives the intuition behind the fact that adjoint functors occur in pairs: if
F
is left adjoint to
G
, then
G
is right adjoint to
F
.

Formal definitions

[edit]
There are various equivalent definitions for adjoint functors:

The definitions via universal morphisms are easy to state, and require minimal verifications when constructing an adjoint functor or proving two functors are adjoint. They are also the most analogous to our intuition involving optimizations.

The definition via hom-sets makes symmetry the most apparent, and is the reason for using the word
adjoint
.

The definition via counit–unit adjunction is convenient for proofs about functors that are known to be adjoint, because they provide formulas that can be directly manipulated.
The equivalency of these definitions is quite useful. Adjoint functors arise everywhere, in all areas of mathematics. Since the structure in any of these definitions gives rise to the structures in the others, switching between them makes implicit use of many details that would otherwise have to be repeated separately in every subject area.

Conventions

[edit]
The theory of adjoints has the terms
left
and
right
at its foundation, and there are many components that live in one of two categories
C
and
D
that are under consideration. Therefore it can be helpful to choose letters in alphabetical order according to whether they live in the "lefthand" category
C
or the "righthand" category
D
, and also to write them down in this order whenever possible.
In this article for example, the letters
X
,
F
,
f
, ε will consistently denote things that live in the category
C
, the letters
Y
,
G
,
g
, η will consistently denote things that live in the category
D
, and whenever possible such things will be referred to in order from left to right (a functor
F
:
D
→
C
can be thought of as "living" where its outputs are, in
C
). If the arrows for the left adjoint functor F were drawn they would be pointing to the left; if the arrows for the right adjoint functor G were drawn they would be pointing to the right.

Definition via universal morphisms

[edit]
By definition, a functor  F   :   D   →   C   {\displaystyle F:{\mathcal {D}}\to {\mathcal {C}}}    is a
left adjoint functor
if for each object  X   {\displaystyle X}    in  C   {\displaystyle {\mathcal {C}}}    there exists a universal morphism from  F   {\displaystyle F}    to  X   {\displaystyle X}   . Spelled out, this means that for each object  X   {\displaystyle X}    in  C   {\displaystyle {\mathcal {C}}}    there exists an object  G   (   X   )   {\displaystyle G(X)}    in  D   {\displaystyle {\mathcal {D}}}    and a morphism  ε   X   :   F   (   G   (   X   )   )   →   X   {\displaystyle \varepsilon _{X}:F(G(X))\to X}    such that for every object  Y   {\displaystyle Y}    in  D   {\displaystyle {\mathcal {D}}}    and every morphism  f   :   F   (   Y   )   →   X   {\displaystyle f:F(Y)\to X}    there exists a unique morphism  g   :   Y   →   G   (   X   )   {\displaystyle g:Y\to G(X)}    with  ε   X   ∘   F   (   g   )   =   f   {\displaystyle \varepsilon _{X}\circ F(g)=f}   .
The latter equation is expressed by the following commutative diagram:
Here the counit is a universal morphism.
In this situation, one can show that  G   {\displaystyle G}    can be turned into a functor  G   :   C   →   D   {\displaystyle G:{\mathcal {C}}\to {\mathcal {D}}}    in a unique way such that  ε   X   ∘   F   (   G   (   f   )   )   =   f   ∘   ε   X   ′   {\displaystyle \varepsilon _{X}\circ F(G(f))=f\circ \varepsilon _{X'}}    for all morphisms  f   :   X   ′   →   X   {\displaystyle f:X'\to X}    in  C   {\displaystyle {\mathcal {C}}}   ;  F   {\displaystyle F}    is then called a
left adjoint
to  G   {\displaystyle G}   .
Similarly, we may define right-adjoint functors. A functor  G   :   C   →   D   {\displaystyle G:{\mathcal {C}}\to {\mathcal {D}}}    is a
right adjoint functor
if for each object  Y   {\displaystyle Y}    in  D   {\displaystyle {\mathcal {D}}}   , there exists a universal morphism from  Y   {\displaystyle Y}    to  G   {\displaystyle G}   . Spelled out, this means that for each object  Y   {\displaystyle Y}    in  D   {\displaystyle {\mathcal {D}}}   , there exists an object  F   (   Y   )   {\displaystyle F(Y)}    in  C   {\displaystyle C}    and a morphism  η   Y   :   Y   →   G   (   F   (   Y   )   )   {\displaystyle \eta _{Y}:Y\to G(F(Y))}    such that for every object  X   {\displaystyle X}    in  C   {\displaystyle {\mathcal {C}}}    and every morphism  g   :   Y   →   G   (   X   )   {\displaystyle g:Y\to G(X)}    there exists a unique morphism  f   :   F   (   Y   )   →   X   {\displaystyle f:F(Y)\to X}    with  G   (   f   )   ∘   η   Y   =   g   {\displaystyle G(f)\circ \eta _{Y}=g}   .
The existence of the unit, a universal morphism, can prove the existence of an adjunction.
Again, this  F   {\displaystyle F}    can be uniquely turned into a functor  F   :   D   →   C   {\displaystyle F:{\mathcal {D}}\to {\mathcal {C}}}    such that  G   (   F   (   g   )   )   ∘   η   Y   =   η   Y   ′   ∘   g   {\displaystyle G(F(g))\circ \eta _{Y}=\eta _{Y'}\circ g}    for  g   :   Y   →   Y   ′   {\displaystyle g:Y\to Y'}    a morphism in  D   {\displaystyle {\mathcal {D}}}   ;  G   {\displaystyle G}    is then called a
right adjoint
to  F   {\displaystyle F}   .
It is true, as the terminology implies, that  F   {\displaystyle F}    is left adjoint to  G   {\displaystyle G}    if and only if  G   {\displaystyle G}    is right adjoint to  F   {\displaystyle F}   .
These definitions via universal morphisms are often useful for establishing that a given functor is left or right adjoint, because they are minimalistic in their requirements. They are also intuitively meaningful in that finding a universal morphism is like solving an optimization problem.

Definition via Hom-sets

[edit]
Using hom-sets, an adjunction between two categories  C   {\displaystyle {\mathcal {C}}}    and  D   {\displaystyle {\mathcal {D}}}    can be defined as consisting of two functorsF   :   D   →   C   {\displaystyle F:{\mathcal {D}}\to {\mathcal {C}}}    and  G   :   C   →   D   {\displaystyle G:{\mathcal {C}}\to {\mathcal {D}}}    and a natural isomorphism
Φ   :   h   o   m   C   (   F   −   ,   −   )   →   h   o   m   D   (   −   ,   G   −   )   {\displaystyle \Phi :\mathrm {hom}
{\mathcal {C}}(F-,-)\to \mathrm {hom}
{\mathcal {D}}(-,G-)}   .
This specifies a family of bijections
Φ   Y   ,   X   :   h   o   m   C   (   F   Y   ,   X   )   →   h   o   m   D   (   Y   ,   G   X   )   {\displaystyle \Phi
{Y,X}:\mathrm {hom}
{\mathcal {C}}(FY,X)\to \mathrm {hom}
{\mathcal {D}}(Y,GX)}
for all objects  X   ∈   C   {\displaystyle X\in {\mathcal {C}}}    and  Y   ∈   D   {\displaystyle Y\in {\mathcal {D}}}   .
In this situation,  F   {\displaystyle F}    is left adjoint to  G   {\displaystyle G}    and
G   {\displaystyle G}    is right adjoint to  F   {\displaystyle F}
.
This definition is a logical compromise in that it is more difficult to establish its satisfaction than the universal morphism definitions, and has fewer immediate implications than the counit–unit definition. It is useful because of its obvious symmetry, and as a stepping-stone between the other definitions.
In order to interpret  Φ   {\displaystyle \Phi }    as a
natural isomorphism
, one must recognize  hom   C   (   F   −   ,   −   )   {\displaystyle {\text{hom}}
{\mathcal {C}}(F-,-)}    and  hom   D   (   −   ,   G   −   )   {\displaystyle {\text{hom}}
{\mathcal {D}}(-,G-)}    as functors. In fact, they are both bifunctors from  D   op   ×   C   {\displaystyle {\mathcal {D}}^{\text{op}}\times {\mathcal {C}}}    to  S   e   t   {\displaystyle \mathbf {Set} }    (the category of sets). For details, see the article on hom functors. Spelled out, the naturality of  Φ   {\displaystyle \Phi }    means that for all morphismsf   :   X   →   X   ′   {\displaystyle f:X\to X'}    in  C   {\displaystyle {\mathcal {C}}}    and all morphisms  g   :   Y   ′   →   Y   {\displaystyle g:Y'\to Y}    in  D   {\displaystyle {\mathcal {D}}}    the following diagram commutes:
Naturality of Φ
The vertical arrows in this diagram are those induced by composition. Formally,  Hom   (   F   g   ,   f   )   :   Hom   C   (   F   Y   ,   X   )   →   Hom   C   (   F   Y   ′   ,   X   ′   )   {\displaystyle {\text{Hom}}(Fg,f):{\text{Hom}}
{\mathcal {C}}(FY,X)\to {\text{Hom}}
{\mathcal {C}}(FY',X')}    is given by  h   ↦   f   ∘   h   ∘   F   g   {\displaystyle h\mapsto f\circ h\circ Fg}    for each  h   ∈   Hom   C   (   F   Y   ,   X   )   .   {\displaystyle h\in {\text{Hom}}
{\mathcal {C}}(FY,X).}   Hom   (   g   ,   G   f   )   {\displaystyle {\text{Hom}}(g,Gf)}    is similar.

Definition via counit–unit

[edit]
A third way of defining an adjunction between two categories  C   {\displaystyle {\mathcal {C}}}    and  D   {\displaystyle {\mathcal {D}}}    consists of two functorsF   :   D   →   C   {\displaystyle F:{\mathcal {D}}\to {\mathcal {C}}}    and  G   :   C   →   D   {\displaystyle G:{\mathcal {C}}\to {\mathcal {D}}}    and two natural transformations
ε   :   F   G   →   1   C   η   :   1   D   →   G   F   {\displaystyle {\begin{aligned}\varepsilon &:FG\to 1_{\mathcal {C}}\\eta &:1_{\mathcal {D}}\to GF\end{aligned}}}
respectively called the
counit
and the
unit
of the adjunction (terminology from universal algebra), such that the compositions
F   →   F   η   F   G   F   →   ε   F   F   {\displaystyle F\xrightarrow {\overset {}{;F\eta ;}} FGF\xrightarrow {\overset {}{;\varepsilon F,}} F}   G   →   η   G   G   F   G   →   G   ε   G   {\displaystyle G\xrightarrow {\overset {}{;\eta G;}} GFG\xrightarrow {\overset {}{;G\varepsilon ,}} G}
are the identity morphisms  1   F   {\displaystyle 1_{F}}    and  1   G   {\displaystyle 1_{G}}    on  F  and  G  respectively.
In this situation we say that  F
is left adjoint to
G  and  G
is right adjoint to
F , and may indicate this relationship by writing  (   ε   ,   η   )   :   F   ⊣   G   {\displaystyle (\varepsilon ,\eta ):F\dashv G}    , or, simply  F   ⊣   G   {\displaystyle F\dashv G}    .
In equational form, the above conditions on  (   ε   ,   η   )   {\displaystyle (\varepsilon ,\eta )}    are the
counit–unit equations

1   F   =   ε   F   ∘   F   η   1   G   =   G   ε   ∘   η   G   {\displaystyle {\begin{aligned}1_{F}&=\varepsilon F\circ F\eta \1_{G}&=G\varepsilon \circ \eta G\end{aligned}}}
which imply that for each  X   ∈   C   {\displaystyle X\in {\mathcal {C}}}    and each  Y   ∈   D   ,   {\displaystyle Y\in {\mathcal {D}},}
1   F   Y   =   ε   F   Y   ∘   F   (   η   Y   )   1   G   X   =   G   (   ε   X   )   ∘   η   G   X   {\displaystyle {\begin{aligned}1_{FY}&=\varepsilon
{FY}\circ F(\eta
{Y})\1
{GX}&=G(\varepsilon
{X})\circ \eta
{GX}\end{aligned}}}   .
Note that  1   C   {\displaystyle 1
{\mathcal {C}}}    denotes the identify functor on the category  C   {\displaystyle {\mathcal {C}}}   ,  1   F   {\displaystyle 1
{F}}    denotes the identity natural transformation from the functor  F  to itself, and  1   F   Y   {\displaystyle 1
{FY}}    denotes the identity morphism of the object  F   Y   .   {\displaystyle FY.}
String diagram for adjunction.
These equations are useful in reducing proofs about adjoint functors to algebraic manipulations. They are sometimes called the
triangle identities
, or sometimes the
zig-zag equations
because of the appearance of the corresponding string diagrams. A way to remember them is to first write down the nonsensical equation  1   =   ε   ∘   η   {\displaystyle 1=\varepsilon \circ \eta }    and then fill in either  F  or  G  in one of the two simple ways that make the compositions defined.
Note: The use of the prefix "co" in counit here is not consistent with the terminology of limits and colimits, because a colimit satisfies an
initial
property whereas the counit morphisms satisfy
terminal
properties, and dually for limit versus unit. The term
unit
here is borrowed from the theory of monads, where it looks like the insertion of the identity  1  into a monoid.

History

[edit]
The idea of adjoint functors was introduced by Daniel Kan in 1958.[ 5 ] Like many of the concepts in category theory, it was suggested by the needs of homological algebra, which was at the time devoted to computations. Those faced with giving tidy, systematic presentations of the subject would have noticed relations such as
hom(
F
(
X
),
Y
) = hom(
X
,
G
(
Y
))
in the category of abelian groups, where
F
was the functor  −   ⊗   A   {\displaystyle -\otimes A}    (i.e. take the tensor product with
A
), and
G
was the functor hom(
A
,–) (this is now known as the tensor-hom adjunction). The use of the
equals
sign is an abuse of notation; those two groups are not really identical but there is a way of identifying them that is
natural
. It can be seen to be natural on the basis, firstly, that these are two alternative descriptions of the bilinear mappings from
X
×
A
to
Y
. That is, however, something particular to the case of tensor product. In category theory the 'naturality' of the bijection is subsumed in the concept of a natural isomorphism.

Examples

[edit]

Free groups

[edit]
The construction of free groups is a common and illuminating example.
Let
F
: Set → Grp be the functor assigning to each set
Y
the free group generated by the elements of
Y
, and let
G
:
Grp
→
Set
be the forgetful functor, which assigns to each group
X
its underlying set. Then
F
is left adjoint to
G
:
Initial morphisms.   For each set
Y
, the set
GFY
is just the underlying set of the free group
FY
generated by
Y
. Let  η   Y   :   Y   →   G   F   Y   {\displaystyle \eta _{Y}:Y\to GFY}    be the set map given by "inclusion of generators". This is an initial morphism from
Y
to
G
, because any set map from
Y
to the underlying set
GW
of some group
W
will factor through  η   Y   :   Y   →   G   F   Y   {\displaystyle \eta _{Y}:Y\to GFY}    via a unique group homomorphism from
FY
to
W
. This is precisely the universal property of the free group on
Y
.   Terminal morphisms.   For each group
X
, the group
FGX
is the free group generated freely by
GX
, the elements of
X
. Let  ε   X   :   F   G   X   →   X   {\displaystyle \varepsilon _{X}:FGX\to X}    be the group homomorphism that sends the generators of
FGX
to the elements of
X
they correspond to, which exists by the universal property of free groups. Then each  (   G   X   ,   ε   X   )   {\displaystyle (GX,\varepsilon _{X})}    is a terminal morphism from
F
to
X
, because any group homomorphism from a free group
FZ
to
X
will factor through  ε   X   :   F   G   X   →   X   {\displaystyle \varepsilon
{X}:FGX\to X}    via a unique set map from
Z
to
GX
. This means that (
F
,
G
) is an adjoint pair.   Hom-set adjunction.   Group homomorphisms from the free group
FY
to a group
X
correspond precisely to maps from the set
Y
to the set
GX
: each homomorphism from
FY
to
X
is fully determined by its action on generators, another restatement of the universal property of free groups. One can verify directly that this correspondence is a natural transformation, which means it is a hom-set adjunction for the pair (
F
,
G
).   counit–unit adjunction.   One can also verify directly that ε and η are natural. Then, a direct verification that they form a counit–unit adjunction  (   ε   ,   η   )   :   F   ⊣   G   {\displaystyle (\varepsilon ,\eta ):F\dashv G}    is as follows:   The first counit–unit equation   1   F   =   ε   F   ∘   F   η   {\displaystyle 1
{F}=\varepsilon F\circ F\eta }    says that for each set
Y
the composition  F   Y   →   F   (   η   Y   )   F   G   F   Y   →   ε   F   Y   F   Y   {\displaystyle FY\xrightarrow {\overset {}{;F(\eta _{Y});}} FGFY\xrightarrow {;\varepsilon _{FY},} FY}   should be the identity. The intermediate group
FGFY
is the free group generated freely by the words of the free group
FY
. (Think of these words as placed in parentheses to indicate that they are independent generators.) The arrow  F   (   η   Y   )   {\displaystyle F(\eta _{Y})}    is the group homomorphism from
FY
into
FGFY
sending each generator
y
of
FY
to the corresponding word of length one (
y
) as a generator of
FGFY
. The arrow  ε   F   Y   {\displaystyle \varepsilon
{FY}}    is the group homomorphism from
FGFY
to
FY
sending each generator to the word of
FY
it corresponds to (so this map is "dropping parentheses"). The composition of these maps is indeed the identity on
FY
.   The second counit–unit equation   1   G   =   G   ε   ∘   η   G   {\displaystyle 1
{G}=G\varepsilon \circ \eta G}    says that for each group
X
the composition  G   X   →   η   G   X   G   F   G   X   →   G   (   ε   X   )   G   X   {\displaystyle GX\xrightarrow {;\eta _{GX};} GFGX\xrightarrow {\overset {}{;G(\varepsilon _{X}),}} GX}   should be the identity. The intermediate set
GFGX
is just the underlying set of
FGX
. The arrow  η   G   X   {\displaystyle \eta _{GX}}    is the "inclusion of generators" set map from the set
GX
to the set
GFGX
. The arrow  G   (   ε   X   )   {\displaystyle G(\varepsilon _{X})}    is the set map from
GFGX
to
GX
, which underlies the group homomorphism sending each generator of
FGX
to the element of
X
it corresponds to ("dropping parentheses"). The composition of these maps is indeed the identity on
GX
.

Free constructions and forgetful functors

[edit]
Free objects are all examples of a left adjoint to a forgetful functor, which assigns to an algebraic object its underlying set. These algebraic free functors have generally the same description as in the detailed description of the free group situation above.

Diagonal functors and limits

[edit]
Products, fibred products, equalizers, and kernels are all examples of the categorical notion of a limit. Any limit functor is right adjoint to a corresponding diagonal functor (provided the category has the type of limits in question), and the counit of the adjunction provides the defining maps from the limit object (i.e. from the diagonal functor on the limit, in the functor category). Below are some specific examples.

Products
Let Π : Grp2 →
Grp
be the functor that assigns to each pair (
X
1, X2) the product group
X
1×
X
2, and let Δ :
Grp →
Grp2 be the diagonal functor that assigns to every group
X
the pair (
X
,
X
) in the product category Grp2. The universal property of the product group shows that Π is right-adjoint to Δ. The counit of this adjunction is the defining pair of projection maps from
X
1×
X
2 to
X
1 and
X
2 which define the limit, and the unit is the
diagonal inclusion
of a group X into
X
×
X
(mapping x to (x,x)).
The cartesian product of sets, the product of rings, the product of topological spaces etc. follow the same pattern; it can also be extended in a straightforward manner to more than just two factors. More generally, any type of limit is right adjoint to a diagonal functor.

Kernels.
Consider the category
D
of homomorphisms of abelian groups. If
f
1 :
A
1 →
B
1 and
f
2 :
A
2 →
B
2 are two objects of
D
, then a morphism from
f
1 to
f
2 is a pair (
g

A
,
g

B
) of morphisms such that
g

B

f
1 =
f
2
g

A
. Let
G
:
D
→
Ab
be the functor which assigns to each homomorphism its kernel and let
F
:
Ab →

D
be the functor which maps the group
A
to the homomorphism
A
→ 0. Then
G
is right adjoint to
F
, which expresses the universal property of kernels. The counit of this adjunction is the defining embedding of a homomorphism's kernel into the homomorphism's domain, and the unit is the morphism identifying a group
A
with the kernel of the homomorphism
A
→ 0.
A suitable variation of this example also shows that the kernel functors for vector spaces and for modules are right adjoints. Analogously, one can show that the cokernel functors for abelian groups, vector spaces and modules are left adjoints.

Colimits and diagonal functors

[edit]
Coproducts, fibred coproducts, coequalizers, and cokernels are all examples of the categorical notion of a colimit. Any colimit functor is left adjoint to a corresponding diagonal functor (provided the category has the type of colimits in question), and the unit of the adjunction provides the defining maps into the colimit object. Below are some specific examples.

Coproducts.
If
F
:
Ab

2

→

Ab
assigns to every pair (
X
1,
X
2) of abelian groups their direct sum, and if
G
:
Ab
→
Ab

2
is the functor which assigns to every abelian group
Y
the pair (
Y
,
Y
), then
F
is left adjoint to
G
, again a consequence of the universal property of direct sums. The unit of this adjoint pair is the defining pair of inclusion maps from
X
1 and
X
2 into the direct sum, and the counit is the additive map from the direct sum of (
X
,
X
) to back to
X
(sending an element (
a
,
b
) of the direct sum to the element
a
+
b
of
X
).
Analogous examples are given by the direct sum of vector spaces and modules, by the free product of groups and by the disjoint union of sets.

Further examples

[edit]

Algebra

[edit]

Adjoining an identity to a rng
.
This example was discussed in the motivation section above. Given a rng
R
, a multiplicative identity element can be added by taking
R
x
Z
and defining a
Z
-bilinear product with (r,0)(0,1) = (0,1)(r,0) = (r,0), (r,0)(s,0) = (rs,0), (0,1)(0,1) = (0,1). This constructs a left adjoint to the functor taking a ring to the underlying rng.

Adjoining an identity to a semigroup
.
Similarly, given a semigroup
S
, we can add an identity element and obtain a monoid by taking the disjoint union
S
⊔   {\displaystyle \sqcup }    {1} and defining a binary operation on it such that it extends the operation on
S
and 1 is an identity element. This construction gives a functor that is a left adjoint to the functor taking a monoid to the underlying semigroup.

Ring extensions.
Suppose
R
and
S
are rings, and ρ :
R
→
S
is a ring homomorphism. Then
S
can be seen as a (left)
R
-module, and the tensor product with
S
yields a functor
F
:
R
-
Mod
→
S
-
Mod
. Then
F
is left adjoint to the forgetful functor
G
:
S
-
Mod
→
R
-
Mod
.

Tensor products
.
If
R
is a ring and
M
is a right
R
-module, then the tensor product with
M
yields a functor
F
:
R
-
Mod
→
Ab
. The functor
G
:
Ab
→
R
-
Mod
, defined by
G
(
A
) = hom
Z
(
M
,
A
) for every abelian group
A
, is a right adjoint to
F
.

From monoids and groups to rings.
The integral monoid ring construction gives a functor from monoids to rings. This functor is left adjoint to the functor that associates to a given ring its underlying multiplicative monoid. Similarly, the integral group ring construction yields a functor from groups to rings, left adjoint to the functor that assigns to a given ring its group of units. One can also start with a field
K
and consider the category of
K
-algebras instead of the category of rings, to get the monoid and group rings over
K
.

Field of fractions.
Consider the category
Dom
m of integral domains with injective morphisms. The forgetful functor
Field
→
Dom
m from fields has a left adjoint—it assigns to every integral domain its field of fractions.

Polynomial rings
. Let
Ring
* be the category of pointed commutative rings with unity (pairs (A,a) where A is a ring, a ∈ A and morphisms preserve the distinguished elements). The forgetful functor G:
Ring
* →
Ring
has a left adjoint – it assigns to every ring R the pair (R[x],x) where R[x] is the polynomial ring with coefficients from R.

Abelianization
. Consider the inclusion functor
G
:
Ab
→
Grp
from the category of abelian groups to category of groups. It has a left adjoint called abelianization which assigns to every group
G
the quotient group
G
ab=
G
/[
G
,
G
].

The Grothendieck group
. In K-theory, the point of departure is to observe that the category of vector bundles on a topological space has a commutative monoid structure under direct sum. One may make an abelian group out of this monoid, the Grothendieck group, by formally adding an additive inverse for each bundle (or equivalence class). Alternatively one can observe that the functor that for each group takes the underlying monoid (ignoring inverses) has a left adjoint. This is a once-for-all construction, in line with the third section discussion above. That is, one can imitate the construction of negative numbers; but there is the other option of an existence theorem. For the case of finitary algebraic structures, the existence by itself can be referred to universal algebra, or model theory; naturally there is also a proof adapted to category theory, too.

Frobenius reciprocity
in the representation theory of groups: see induced representation. This example foreshadowed the general theory by about half a century.

Topology

[edit]

A functor with a left and a right adjoint.
Let
G
be the functor from topological spaces to sets that associates to every topological space its underlying set (forgetting the topology, that is).
G
has a left adjoint
F
, creating the discrete space on a set
Y
, and a right adjoint
H
creating the trivial topology on
Y
.

Suspensions and loop spaces.
Given topological spaces
X
and
Y
, the space [
SX
,
Y
] of homotopy classes of maps from the suspension
SX
of
X
to
Y
is naturally isomorphic to the space [
X
, Ω
Y
] of homotopy classes of maps from
X
to the loop space Ω
Y
of
Y
. The suspension functor is therefore left adjoint to the loop space functor in the homotopy category, an important fact in homotopy theory.

Stone–Čech compactification.
Let
KHaus
be the category of compactHausdorff spaces and
G
:
KHaus
→
Top
be the inclusion functor to the category of topological spaces. Then
G
has a left adjoint
F
:
Top
→
KHaus
, the Stone–Čech compactification. The unit of this adjoint pair yields a continuous map from every topological space
X
into its Stone–Čech compactification.

Direct and inverse images of sheaves.
Every continuous map
f
:
X
→
Y
between topological spaces induces a functor
f
∗ from the category of sheaves (of sets, or abelian groups, or rings...) on
X
to the corresponding category of sheaves on
Y
, the direct image functor. It also induces a functor
f
−1 from the category of sheaves of abelian groups on
Y
to the category of sheaves of abelian groups on
X
, the inverse image functor.
f
−1 is left adjoint to
f
∗. Here a more subtle point is that the left adjoint for coherent sheaves will differ from that for sheaves (of sets).

Soberification.
The article on Stone duality describes an adjunction between the category of topological spaces and the category of sober spaces that is known as soberification. Notably, the article also contains a detailed description of another adjunction that prepares the way for the famous duality of sober spaces and spatial locales, exploited in pointless topology.

Posets

[edit]
Every partially ordered set can be viewed as a category (where the elements of the poset become the category's objects and we have a single morphism from
x
to
y
if and only if
x
≤
y
). A pair of adjoint functors between two partially ordered sets is called a Galois connection (or, if it is contravariant, an
antitone
Galois connection). See that article for a number of examples: the case of Galois theory of course is a leading one. Any Galois connection gives rise to closure operators and to inverse order-preserving bijections between the corresponding closed elements.
As is the case for Galois groups, the real interest lies often in refining a correspondence to a duality (i.e.
antitone
order isomorphism). A treatment of Galois theory along these lines by Kaplansky was influential in the recognition of the general structure here.
The partial order case collapses the adjunction definitions quite noticeably, but can provide several themes:

adjunctions may not be dualities or isomorphisms, but are candidates for upgrading to that status

closure operators may indicate the presence of adjunctions, as corresponding monads (cf. the Kuratowski closure axioms)

a very general comment of William Lawvere[ 6 ] is that
syntax and semantics
are adjoint: take
C
to be the set of all logical theories (axiomatizations), and
D
the power set of the set of all mathematical structures. For a theory
T
in
C
, let
G
(
T
) be the set of all structures that satisfy the axioms
T
; for a set of mathematical structures
S
, let
F
(
S
) be the minimal axiomatization of
S
. We can then say that
S
is a subset of
G
(
T
) if and only if
F
(
S
) logically implies
T
: the "semantics functor"
G
is right adjoint to the "syntax functor"
F
.

division is (in general) the attempt to
invert
multiplication, but in situations where this is not possible, we often attempt to construct an
adjoint
instead: the ideal quotient is adjoint to the multiplication by ring ideals, and the implication in propositional logic is adjoint to logical conjunction.

Category theory

[edit]

Equivalences.
If
F
:
D
→
C
is an equivalence of categories, then we have an inverse equivalence
G
:
C
→
D
, and the two functors
F
and
G
form an adjoint pair. The unit and counit are natural isomorphisms in this case. If η : id →
GF
and ε :
GF
→ id are natural isomorphisms, then there exist unique natural isomorphisms ε' :
GF
→ id and η' : id →
GF
for which (η, ε') and (η', ε) are counit–unit pairs for
F
and
G
; they are  ε   ′   =   ε   ∘   (   F   η   −   1   G   )   ∘   (   F   G   ε   −   1   )   {\displaystyle \varepsilon '=\varepsilon \circ (F\eta ^{-1}G)\circ (FG\varepsilon ^{-1})}   η   ′   =   (   G   F   η   −   1   )   ∘   (   G   ε   −   1   F   )   ∘   η   {\displaystyle \eta '=(GF\eta ^{-1})\circ (G\varepsilon ^{-1}F)\circ \eta }

A series of adjunctions.
The functor π0 which assigns to a category its set of connected components is left-adjoint to the functor
D
which assigns to a set the discrete category on that set. Moreover,
D
is left-adjoint to the object functor
U
which assigns to each category its set of objects, and finally
U
is left-adjoint to
A
which assigns to each set the indiscrete category[ 7 ] on that set.

Exponential object
. In a cartesian closed category the endofunctor
C
→
C
given by –×
A
has a right adjoint –
A
. This pair is often referred to as currying and uncurrying; in many special cases, they are also continuous and form a homeomorphism.

Categorical logic

[edit]

Quantification.
If  ϕ   Y   {\displaystyle \phi _{Y}}    is a unary predicate expressing some property, then a sufficiently strong set theory may prove the existence of the set  Y   =   {   y   ∣   ϕ   Y   (   y   )   }   {\displaystyle Y={y\mid \phi _{Y}(y)}}    of terms that fulfill the property. A proper subset  T   ⊂   Y   {\displaystyle T\subset Y}    and the associated injection of  T   {\displaystyle T}    into  Y   {\displaystyle Y}    is characterized by a predicate  ϕ   T   (   y   )   =   ϕ   Y   (   y   )   ∧   φ   (   y   )   {\displaystyle \phi _{T}(y)=\phi _{Y}(y)\land \varphi (y)}    expressing a strictly more restrictive property.

The role of quantifiers in predicate logics is in forming propositions and also in expressing sophisticated predicates by closing formulas with possibly more variables. For example, consider a predicate  ψ   f   {\displaystyle \psi _{f}}    with two open variables of sort  X   {\displaystyle X}    and  Y   {\displaystyle Y}   . Using a quantifier to close  X   {\displaystyle X}   , we can form the set  {   y   ∈   Y   ∣   ∃   x   .   ψ   f   (   x   ,   y   )   ∧   ϕ   S   (   x   )   }   {\displaystyle {y\in Y\mid \exists x.,\psi _{f}(x,y)\land \phi _{S}(x)}}   of all elements  y   {\displaystyle y}    of  Y   {\displaystyle Y}    for which there is an  x   {\displaystyle x}    to which it is  ψ   f   {\displaystyle \psi _{f}}   -related, and which itself is characterized by the property  ϕ   S   {\displaystyle \phi _{S}}   . Set theoretic operations like the intersection  ∩   {\displaystyle \cap }    of two sets directly corresponds to the conjunction  ∧   {\displaystyle \land }    of predicates. In categorical logic, a subfield of topos theory, quantifiers are identified with adjoints to the pullback functor. Such a realization can be seen in analogy to the discussion of propositional logic using set theory but the general definition make for a richer range of logics.   So consider an object  Y   {\displaystyle Y}    in a category with pullbacks. Any morphism  f   :   X   →   Y   {\displaystyle f:X\to Y}    induces a functor  f   ∗   :   Sub   (   Y   )   ⟶   Sub   (   X   )   {\displaystyle f^{
}:{\text{Sub}}(Y)\longrightarrow {\text{Sub}}(X)}   on the category that is the preorder of  subobjects. It maps subobjects  T   {\displaystyle T}    of  Y   {\displaystyle Y}    (technically: monomorphism classes of  T   →   Y   {\displaystyle T\to Y}   ) to the pullback  X   ×   Y   T   {\displaystyle X\times _{Y}T}   . If this functor has a left- or right adjoint, they are called  ∃   f   {\displaystyle \exists _{f}}    and  ∀   f   {\displaystyle \forall _{f}}   , respectively.[ 8 ] They both map from  Sub   (   X   )   {\displaystyle {\text{Sub}}(X)}    back to  Sub   (   Y   )   {\displaystyle {\text{Sub}}(Y)}   . Very roughly, given a domain  S   ⊂   X   {\displaystyle S\subset X}    to quantify a relation expressed via  f   {\displaystyle f}    over, the functor/quantifier closes  X   {\displaystyle X}    in  X   ×   Y   T   {\displaystyle X\times _{Y}T}    and returns the thereby specified subset of  Y   {\displaystyle Y}   .
Example
: In  Set   {\displaystyle \operatorname {Set} }   , the category of sets and functions, the canonical subobjects are the subset (or rather their canonical injections). The pullback  f   ∗   T   =   X   ×   Y   T   {\displaystyle f^{
}T=X\times _{Y}T}    of an injection of a subset  T   {\displaystyle T}    into  Y   {\displaystyle Y}    along  f   {\displaystyle f}    is characterized as the largest set which knows all about  f   {\displaystyle f}    and the injection of  T   {\displaystyle T}    into  Y   {\displaystyle Y}   . It therefore turns out to be (in bijection with) the inverse image  f   −   1   [   T   ]   ⊆   X   {\displaystyle f^{-1}[T]\subseteq X}   .   For  S   ⊆   X   {\displaystyle S\subseteq X}   , let us figure out the left adjoint, which is defined via  Hom   (   ∃   f   S   ,   T   )   ≅   Hom   (   S   ,   f   ∗   T   )   ,   {\displaystyle {\operatorname {Hom} }(\exists _{f}S,T)\cong {\operatorname {Hom} }(S,f^{
}T),}   which here just means  ∃   f   S   ⊆   T   ↔   S   ⊆   f   −   1   [   T   ]   {\displaystyle \exists _{f}S\subseteq T\leftrightarrow S\subseteq f^{-1}[T]}   .   Consider  f   [   S   ]   ⊆   T   {\displaystyle f[S]\subseteq T}   . We see  S   ⊆   f   −   1   [   f   [   S   ]   ]   ⊆   f   −   1   [   T   ]   {\displaystyle S\subseteq f^{-1}[f[S]]\subseteq f^{-1}[T]}   . Conversely, If for an  x   ∈   S   {\displaystyle x\in S}    we also have  x   ∈   f   −   1   [   T   ]   {\displaystyle x\in f^{-1}[T]}   , then clearly  f   (   x   )   ∈   T   {\displaystyle f(x)\in T}   . So  S   ⊆   f   −   1   [   T   ]   {\displaystyle S\subseteq f^{-1}[T]}    implies  f   [   S   ]   ⊆   T   {\displaystyle f[S]\subseteq T}   . We conclude that left adjoint to the inverse image functor  f   ∗   {\displaystyle f^{
}}    is given by the direct image. Here is a characterization of this result, which matches more the logical interpretation: The image of  S   {\displaystyle S}    under  ∃   f   {\displaystyle \exists _{f}}    is the full set of  y   {\displaystyle y}   's, such that  f   −   1   [   {   y   }   ]   ∩   S   {\displaystyle f^{-1}[{y}]\cap S}    is non-empty. This works because it neglects exactly those  y   ∈   Y   {\displaystyle y\in Y}    which are in the complement of  f   [   S   ]   {\displaystyle f[S]}   . So  ∃   f   S   =   {   y   ∈   Y   ∣   ∃   (   x   ∈   f   −   1   [   {   y   }   ]   )   .   x   ∈   S   }   =   f   [   S   ]   .   {\displaystyle \exists _{f}S={y\in Y\mid \exists (x\in f^{-1}[{y}]).,x\in S;}=f[S].}   Put this in analogy to our motivation  {   y   ∈   Y   ∣   ∃   x   .   ψ   f   (   x   ,   y   )   ∧   ϕ   S   (   x   )   }   {\displaystyle {y\in Y\mid \exists x.,\psi _{f}(x,y)\land \phi _{S}(x)}}   .   The right adjoint to the inverse image functor is given (without doing the computation here) by  ∀   f   S   =   {   y   ∈   Y   ∣   ∀   (   x   ∈   f   −   1   [   {   y   }   ]   )   .   x   ∈   S   }   .   {\displaystyle \forall _{f}S={y\in Y\mid \forall (x\in f^{-1}[{y}]).,x\in S;}.}   The subset  ∀   f   S   {\displaystyle \forall _{f}S}    of  Y   {\displaystyle Y}    is characterized as the full set of  y   {\displaystyle y}   's with the property that the inverse image of  {   y   }   {\displaystyle {y}}    with respect to  f   {\displaystyle f}    is fully contained within  S   {\displaystyle S}   . Note how the predicate determining the set is the same as above, except that  ∃   {\displaystyle \exists }    is replaced by  ∀   {\displaystyle \forall }   .  See also powerset
.
Probability

[edit]
The twin fact in probability can be understood as an adjunction: that expectation commutes with affine transform, and that the expectation is in some sense the best
solution
to the problem of finding a real-valued approximation to a distribution on the real numbers.
Define a category based on  R   {\displaystyle \mathbb {R} }   , with objects being the real numbers, and the morphisms being "affine functions evaluated at a point". That is, for any affine function  f   (   x   )   =   a   x   +   b   {\displaystyle f(x)=ax+b}    and any real number  r   {\displaystyle r}   , define a morphism  (   r   ,   f   )   :   r   →   f   (   r   )   {\displaystyle (r,f):r\to f(r)}   .
Define a category based on  M   (   R   )   {\displaystyle M(\mathbb {R} )}   , the set of probability distribution on  R   {\displaystyle \mathbb {R} }    with finite expectation. Define morphisms on  M   (   R   )   {\displaystyle M(\mathbb {R} )}    as "affine functions evaluated at a distribution". That is, for any affine function  f   (   x   )   =   a   x   +   b   {\displaystyle f(x)=ax+b}    and any  μ   ∈   M   (   R   )   {\displaystyle \mu \in M(\mathbb {R} )}   , define a morphism  (   μ   ,   f   )   :   μ   →   μ   ∘   f   −   1   {\displaystyle (\mu ,f):\mu \to \mu \circ f^{-1}}   .
Then, the Dirac delta measure defines a functor:  δ   :   x   ↦   δ   x   {\displaystyle \delta :x\mapsto \delta _{x}}   , and the expectation defines another functor  E   :   μ   ↦   E   [   μ   ]   {\displaystyle \mathbb {E} :\mu \mapsto \mathbb {E} [\mu ]}   , and they are adjoint:  E   ⊣   δ   {\displaystyle \mathbb {E} \dashv \delta }   . (Somewhat disconcertingly,  E   {\displaystyle \mathbb {E} }    is the left adjoint, even though  E   {\displaystyle \mathbb {E} }    is "forgetful" and  δ   {\displaystyle \delta }    is "free".)

Adjunctions in full

[edit]
There are hence numerous functors and natural transformations associated with every adjunction, and only a small portion is sufficient to determine the rest.
An
adjunction
between categories
C
and
D
consists of

A functor
F
:
D
→
C
called the
left adjoint

A functor
G
:
C
→
D
called the
right adjoint

A natural isomorphism Φ : hom
C
(
F
–,–) → hom
D
(–,
G
–)

A natural transformation ε :
FG
→ 1
C
called the
counit

A natural transformation η : 1
D
→
GF
called the
unit

An equivalent formulation, where
X
denotes any object of
C
and
Y
denotes any object of
D
, is as follows:
For every
C
-morphism
f
:
FY
→
X
, there is a unique
D
-morphism Φ
Y
,
X
(
f
) =
g
:
Y
→
GX
such that the diagrams below commute, and for every
D
-morphism
g
:
Y
→
GX
, there is a unique
C
-morphism Φ−1
Y
,
X
(
g
) =
f
:
FY
→
X
in
C
such that the diagrams below commute:  From this assertion, one can recover that:

The transformations ε, η, and Φ are related by the equations
f   =   Φ   Y   ,   X   −   1   (   g   )   =   ε   X   ∘   F   (   g   )   ∈   h   o   m   C   (   F   (   Y   )   ,   X   )   g   =   Φ   Y   ,   X   (   f   )   =   G   (   f   )   ∘   η   Y   ∈   h   o   m   D   (   Y   ,   G   (   X   )   )   Φ   G   X   ,   X   −   1   (   1   G   X   )   =   ε   X   ∈   h   o   m   C   (   F   G   (   X   )   ,   X   )   Φ   Y   ,   F   Y   (   1   F   Y   )   =   η   Y   ∈   h   o   m   D   (   Y   ,   G   F   (   Y   )   )   {\displaystyle {\begin{aligned}f=\Phi _{Y,X}^{-1}(g)&=\varepsilon _{X}\circ F(g)&\in &,,\mathrm {hom} _{C}(F(Y),X)\g=\Phi _{Y,X}(f)&=G(f)\circ \eta _{Y}&\in &,,\mathrm {hom} _{D}(Y,G(X))\\Phi
{GX,X}^{-1}(1
{GX})&=\varepsilon _{X}&\in &,,\mathrm {hom} _{C}(FG(X),X)\\Phi
{Y,FY}(1
{FY})&=\eta _{Y}&\in &,,\mathrm {hom} _{D}(Y,GF(Y))\\end{aligned}}}

The transformations ε, η satisfy the counit–unit equations
1   F   Y   =   ε   F   Y   ∘   F   (   η   Y   )   1   G   X   =   G   (   ε   X   )   ∘   η   G   X   {\displaystyle {\begin{aligned}1_{FY}&=\varepsilon _{FY}\circ F(\eta
{Y})\1
{GX}&=G(\varepsilon _{X})\circ \eta _{GX}\end{aligned}}}

Each pair (
GX
, ε
X
) is a terminal morphism from
F
to
X
in
C

Each pair (
FY
, η
Y
) is an initial morphism from
Y
to
G
in
D

In particular, the equations above allow one to define Φ, ε, and η in terms of any one of the three. However, the adjoint functors
F
and
G
alone are in general not sufficient to determine the adjunction. The equivalence of these situations is demonstrated below.

Universal morphisms induce hom-set adjunction

[edit]
Given a right adjoint functor
G
:
C
→
D
; in the sense of initial morphisms, one may construct the induced hom-set adjunction by doing the following steps.
Construct a functor
F
:
D
→
C
and a natural transformation
η
.

For each object
Y
in
D
, choose an initial morphism (
F
(
Y
),
η

Y
) from
Y
to
G
, so that
η

Y
:
Y
→
G
(
F
(
Y
)). We have the map of
F
on objects and the family of morphisms
η
.

For each
f
:
Y
0 →
Y
1, as (
F
(
Y
0),
η

Y
0) is an initial morphism, then factorize
η

Y
1 ∘
F
with
η

Y
0 and get
F
(
f
) :
F
(
Y
0) →
F
(
Y
1). This is the map of
F
on morphisms.

The commuting diagram of that factorization implies the commuting diagram of natural transformations, so
η
: 1
D
→
G
∘
F
is a natural transformation.

Uniqueness of that factorization and that
G
is a functor implies that the map of
F
on morphisms preserves compositions and identities.
Construct a natural isomorphism Φ : hom
C
(
F
−,−) → hom
D
(−,
G
−).

For each object
X
in
C
, each object
Y
in
D
, as (
F
(
Y
),
η

Y
) is an initial morphism, then Φ
Y
,
X
is a bijection, where Φ
Y
,
X
(
f
:
F
(
Y
) →
X
) =
G
(
F
) ∘
η

Y
.

η
is a natural transformation,
G
is a functor, then for any objects
X
0,
X
1 in
C
, any objects
Y
0,
Y
1 in
D
, any
x
:
X
0 →
X
1, any
y
:
Y
1 →
Y
0, we have Φ
Y
1,
X
1(
x
∘
f
∘
F
(
y
)) = G(
x
) ∘
G
(
f
) ∘
G
(
f
(
y
)) ∘
η

Y
1 =
G
(
x
) ∘
G
(
f
) ∘
η

Y
0 ∘
y
=
G
(
x
) ∘ Φ
Y
0,
X
0(∘) ∘
y
, and then Φ is natural in both arguments.
A similar argument allows one to construct a hom-set adjunction from the terminal morphisms to a left adjoint functor. (The construction that starts with a right adjoint is slightly more common, since the right adjoint in many adjoint pairs is a trivially defined inclusion or forgetful functor.)

counit–unit adjunction induces hom-set adjunction

[edit]
Given functors
F
:
D
→
C
,
G
:
C
→
D
, and a counit–unit adjunction (ε, η) :
F
⊣
G
, we can construct a hom-set adjunction by finding the natural transformation Φ : hom
C
(
F
−,−) → hom
D
(−,
G
−) in the following steps:

For each
f
:
FY
→
X
and each
g
:
Y
→
GX
, define
Φ   Y   ,   X   (   f   )   =   G   (   f   )   ∘   η   Y   Ψ   Y   ,   X   (   g   )   =   ε   X   ∘   F   (   g   )   {\displaystyle {\begin{aligned}\Phi _{Y,X}(f)=G(f)\circ \eta _{Y}\\Psi _{Y,X}(g)=\varepsilon _{X}\circ F(g)\end{aligned}}}   The transformations Φ and Ψ are natural because η and ε are natural.

Using, in order, that
F
is a functor, that ε is natural, and the counit–unit equation 1
FY
= ε
FY
∘
F
(η
Y
), we obtain
Ψ   Φ   f   =   ε   X   ∘   F   G   (   f   )   ∘   F   (   η   Y   )   =   f   ∘   ε   F   Y   ∘   F   (   η   Y   )   =   f   ∘   1   F   Y   =   f   {\displaystyle {\begin{aligned}\Psi \Phi f&=\varepsilon _{X}\circ FG(f)\circ F(\eta _{Y})\&=f\circ \varepsilon _{FY}\circ F(\eta
{Y})\&=f\circ 1
{FY}=f\end{aligned}}}   hence ΨΦ is the identity transformation.

Dually, using that
G
is a functor, that η is natural, and the counit–unit equation 1
GX
=
G
(ε
X
) ∘ η
GX
, we obtain
Φ   Ψ   g   =   G   (   ε   X   )   ∘   G   F   (   g   )   ∘   η   Y   =   G   (   ε   X   )   ∘   η   G   X   ∘   g   =   1   G   X   ∘   g   =   g   {\displaystyle {\begin{aligned}\Phi \Psi g&=G(\varepsilon _{X})\circ GF(g)\circ \eta _{Y}\&=G(\varepsilon _{X})\circ \eta
{GX}\circ g\&=1
{GX}\circ g=g\end{aligned}}}   hence ΦΨ is the identity transformation. Thus Φ is a natural isomorphism with inverse Φ−1 = Ψ.

Hom-set adjunction induces all of the above

[edit]
Given functors
F
:
D
→
C
,
G
:
C
→
D
, and a hom-set adjunction Φ : hom
C
(
F
−,−) → hom
D
(−,
G
−), one can construct a counit–unit adjunction
(   ε   ,   η   )   :   F   ⊣   G   {\displaystyle (\varepsilon ,\eta ):F\dashv G}    ,
which defines families of initial and terminal morphisms, in the following steps:

Let  ε   X   =   Φ   G   X   ,   X   −   1   (   1   G   X   )   ∈   h   o   m   C   (   F   G   X   ,   X   )   {\displaystyle \varepsilon _{X}=\Phi
{GX,X}^{-1}(1
{GX})\in \mathrm {hom}
{C}(FGX,X)}    for each
X
in
C
, where  1   G   X   ∈   h   o   m   D   (   G   X   ,   G   X   )   {\displaystyle 1
{GX}\in \mathrm {hom} _{D}(GX,GX)}    is the identity morphism.

Let  η   Y   =   Φ   Y   ,   F   Y   (   1   F   Y   )   ∈   h   o   m   D   (   Y   ,   G   F   Y   )   {\displaystyle \eta _{Y}=\Phi
{Y,FY}(1
{FY})\in \mathrm {hom}
{D}(Y,GFY)}    for each
Y
in
D
, where  1   F   Y   ∈   h   o   m   C   (   F   Y   ,   F   Y   )   {\displaystyle 1
{FY}\in \mathrm {hom} _{C}(FY,FY)}    is the identity morphism.

The bijectivity and naturality of Φ imply that each (
GX
, ε
X
) is a terminal morphism from
F
to
X
in
C
, and each (
FY
,
η

Y
) is an initial morphism from
Y
to
G
in
D
.

The naturality of Φ implies the naturality of ε and
η
, and the two formulas
Φ   Y   ,   X   (   f   )   =   G   (   f   )   ∘   η   Y   Φ   Y   ,   X   −   1   (   g   )   =   ε   X   ∘   F   (   g   )   {\displaystyle {\begin{aligned}\Phi _{Y,X}(f)=G(f)\circ \eta _{Y}\\Phi _{Y,X}^{-1}(g)=\varepsilon _{X}\circ F(g)\end{aligned}}}   for each
f
:
FY
→
X
and
g
:
Y
→
GX
(which completely determine Φ).

Substituting
FY
for
X
and
η

Y
= Φ
Y
,
FY
(1
FY
) for
g
in the second formula gives the first counit–unit equation
1   F   Y   =   ε   F   Y   ∘   F   (   η   Y   )   {\displaystyle 1_{FY}=\varepsilon _{FY}\circ F(\eta
{Y})}   ,   and substituting
GX
for
Y
and εX = Φ−1
GX, X
(1
GX
) for
f
in the first formula gives the second counit–unit equation   1   G   X   =   G   (   ε   X   )   ∘   η   G   X   {\displaystyle 1
{GX}=G(\varepsilon _{X})\circ \eta _{GX}}   .

Properties

[edit]

Existence

[edit]   See also: Formal criteria for adjoint functorsNot every functor
G
:
C
→
D
admits a left adjoint. If
C
is a complete category, then the functors with left adjoints can be characterized by the
adjoint functor theorem
of Peter J. Freyd:
G
has a left adjoint if and only if it is continuous and a certain smallness condition is satisfied: for every object
Y
of
D
there exists a family of morphisms

f

i
:
Y
→
G
(
X

i
)
where the indices
i
come from a
set
I , not a proper class, such that every morphism

h
:
Y
→
G
(
X
)
can be written as

h
=
G
(
t
)  ∘   {\displaystyle \circ }
f

i
for some
i
in  I  and some morphism

t
:
X

i
→
X
∈
C
.
An analogous statement characterizes those functors with a right adjoint.
An important special case is that of locally presentable categories. If  F   :   C   →   D   {\displaystyle F:C\to D}    is a functor between locally presentable categories, then

F
has a right adjoint if and only if
F
preserves small colimits

F
has a left adjoint if and only if
F
preserves small limits and is an accessible functor

Uniqueness

[edit]
If the functor
F
:
D
→
C
has two right adjoints
G
and
G ′
, then
G
and
G ′
are naturally isomorphic. The same is true for left adjoints.
Conversely, if
F
is left adjoint to
G
, and
G
is naturally isomorphic to
G ′
then
F
is also left adjoint to
G ′
. More generally, if 〈
F
,
G
, ε, η〉 is an adjunction (with counit–unit (ε,η)) and
σ :
F
→
F ′
τ :
G
→
G ′
are natural isomorphisms then 〈
F ′
,
G ′
, ε ′ , η ′ 〉 is an adjunction where
η   ′   =   (   τ   ∗   σ   )   ∘   η   ε   ′   =   ε   ∘   (   σ   −   1   ∗   τ   −   1   )   .   {\displaystyle {\begin{aligned}\eta '&=(\tau \ast \sigma )\circ \eta \\varepsilon '&=\varepsilon \circ (\sigma ^{-1}\ast \tau ^{-1}).\end{aligned}}}
Here  ∘   {\displaystyle \circ }    denotes vertical composition of natural transformations, and  ∗   {\displaystyle \ast }    denotes horizontal composition.

Composition

[edit]
Adjunctions can be composed in a natural fashion. Specifically, if 〈
F
,
G
,
ε
,
η
〉 is an adjunction between
C
and
D
and 〈
F ′
,
G ′
,
ε ′
,
η ′
〉 is an adjunction between
D
and
E
then the functor
F   ∘   F   ′   :   E   →   C   {\displaystyle F\circ F':E\rightarrow C}
is left adjoint to
G   ′   ∘   G   :   C   →   E   .   {\displaystyle G'\circ G:C\to E.}
More precisely, there is an adjunction between
F F′
and
G′ G
with unit and counit given respectively by the compositions:
1   E   →   η   ′   G   ′   F   ′   →   G   ′   η   F   ′   G   ′   G   F   F   ′   F   F   ′   G   ′   G   →   F   ε   ′   G   F   G   →   ε   1   C   .   {\displaystyle {\begin{aligned}&1_{\mathcal {E}}{\xrightarrow {\eta '}}G'F'{\xrightarrow {G'\eta F'}}G'GFF'\&FF'G'G{\xrightarrow {F\varepsilon 'G}}FG{\xrightarrow {\varepsilon }}1_{\mathcal {C}}.\end{aligned}}}
This new adjunction is called the
composition
of the two given adjunctions.
Since there is also a natural way to define an identity adjunction between a category
C
and itself, one can then form a category whose objects are all small categories and whose morphisms are adjunctions.

Limit preservation

[edit]
The most important property of adjoints is their continuity: every functor that has a left adjoint (and therefore
is
a right adjoint) is
continuous
(i.e. commutes with limits in the category theoretical sense); every functor that has a right adjoint (and therefore
is
a left adjoint) is
cocontinuous
(i.e. commutes with colimits).
Since many common constructions in mathematics are limits or colimits, this provides a wealth of information. For example:

applying a right adjoint functor to a product of objects yields the product of the images;

applying a left adjoint functor to a coproduct of objects yields the coproduct of the images;

every right adjoint functor between two abelian categories is left exact;

every left adjoint functor between two abelian categories is right exact.

Additivity

[edit]
If
C
and
D
are preadditive categories and
F
:
D
→
C
is an additive functor with a right adjoint
G
:
C
→
D
, then
G
is also an additive functor and the hom-set bijections
Φ   Y   ,   X   :   h   o   m   C   (   F   Y   ,   X   )   ≅   h   o   m   D   (   Y   ,   G   X   )   {\displaystyle \Phi _{Y,X}:\mathrm {hom} _{\mathcal {C}}(FY,X)\cong \mathrm {hom} _{\mathcal {D}}(Y,GX)}
are, in fact, isomorphisms of abelian groups. Dually, if
G
is additive with a left adjoint
F
, then
F
is also additive.
Moreover, if both
C
and
D
are additive categories (i.e. preadditive categories with all finite biproducts), then any pair of adjoint functors between them are automatically additive.

Relationships

[edit]

Universal constructions

[edit]
As stated earlier, an adjunction between categories
C
and
D
gives rise to a family of universal morphisms, one for each object in
C
and one for each object in
D
. Conversely, if there exists a universal morphism to a functor
G
:
C
→
D
from every object of
D
, then
G
has a left adjoint.
However, universal constructions are more general than adjoint functors: a universal construction is like an optimization problem; it gives rise to an adjoint pair if and only if this problem has a solution for every object of
D
(equivalently, every object of
C
).

Equivalences of categories

[edit]
If a functor
F
:
D
→
C
is one half of an equivalence of categories then it is the left adjoint in an adjoint equivalence of categories, i.e. an adjunction whose unit and counit are isomorphisms.
Every adjunction 〈
F
,
G
, ε, η〉 extends an equivalence of certain subcategories. Define
C
1 as the full subcategory of
C
consisting of those objects
X
of
C
for which ε
X
is an isomorphism, and define
D
1 as the full subcategory of
D
consisting of those objects
Y
of
D
for which η
Y
is an isomorphism. Then
F
and
G
can be restricted to
D
1 and
C
1 and yield inverse equivalences of these subcategories.
In a sense, then, adjoints are "generalized" inverses. Note however that a right inverse of
F
(i.e. a functor
G
such that
FG
is naturally isomorphic to 1
D
) need not be a right (or left) adjoint of
F
. Adjoints generalize
two-sided
inverses.

Monads

[edit]
Every adjunction 〈
F
,
G
, ε, η〉 gives rise to an associated monad 〈
T
, η, μ〉 in the category
D
. The functor
T   :   D   →   D   {\displaystyle T:{\mathcal {D}}\to {\mathcal {D}}}
is given by
T
=
GF
. The unit of the monad
η   :   1   D   →   T   {\displaystyle \eta :1_{\mathcal {D}}\to T}
is just the unit η of the adjunction and the multiplication transformation
μ   :   T   2   →   T   {\displaystyle \mu :T^{2}\to T,}
is given by μ =
G
ε
F
. Dually, the triple 〈
FG
, ε,
F
η
G
〉 defines a comonad in
C
.
Every monad arises from some adjunction—in fact, typically from many adjunctions—in the above fashion. Two constructions, called the category of Eilenberg–Moore algebras and the Kleisli category are two extremal solutions to the problem of constructing an adjunction that gives rise to a given monad.

Notes

[edit]

^
a

b

c

d

e

f

g
Leinster, Tom (2025-08-26), "2 Adjoints",
Basic Category Theory
, arXiv:1612.09375, retrieved  2025-09-02

^Leinster, Tom (2025-08-26), "Remark 2.2.8",
Basic Category Theory
, arXiv:1612.09375, retrieved  2025-09-02

^
a

b

c

d
Mac Lane, Saunders (1998). Categories for the Working Mathematician. Graduate Texts in Mathematics. Vol. 5 (2nd ed.). Springer-Verlag. pp.  80– 82. ISBN0-387-98403-8. Zbl0906.18001.

^Baez, John C. (1996). "Higher-Dimensional Algebra II: 2-Hilbert Spaces". arXiv:q-alg/9609018.

^Kan, Daniel M. (1958). "Adjoint Functors"(PDF) . Transactions of the American Mathematical Society.
87
(2):  294– 329. doi:10.2307/1993102. JSTOR1993102.

^Lawvere, F. William, "Adjointness in foundations",
Dialectica
, 1969. The notation is different nowadays; an easier introduction by Peter Smith in these lecture notes, which also attribute the concept to the article cited.

^"Indiscrete category".
nLab
.

^Mac Lane, Saunders; Moerdijk, Ieke (1992)
Sheaves in Geometry and Logic
, Springer-Verlag. ISBN0-387-97710-4
See page 58

References

[edit]

Adámek, Jiří; Herrlich, Horst; Strecker, George E. (1990).
Abstract and Concrete Categories. The joy of cats
(PDF) . John Wiley & Sons. ISBN0-471-60922-6. Zbl0695.18001.

Borceux, Francis (1994).
Handbook of Categorical Algebra: Basic category theory
. Cambridge University Press. ISBN978-0-521-44178-0.

Mac Lane, Saunders (1998). Categories for the Working Mathematician. Graduate Texts in Mathematics. Vol. 5 (2nd ed.). Springer-Verlag. ISBN0-387-98403-8. Zbl0906.18001.

External links

[edit]

Adjunctions playlist on YouTube – seven short lectures on adjunctions by Eugenia Cheng of The Catsters

WildCats is a category theory package for Mathematica. Manipulation and visualization of objects, morphisms, categories, functors, natural transformations, universal properties.

v

t

e
Category theoryKey concepts Key concepts

CategoryAbelian

Additive

Concrete

Pre-abelian

Preadditive

Bicategory
Adjoint functors
CCC
Commutative diagram
End
Exponential
Functor
Kan extension
Morphism
Natural transformation
Universal property
Yoneda lemma

Universal constructionsLimitsTerminal objects

Products

EqualizersKernels
Pullbacks
Inverse limit

ColimitsInitial objects

Coproducts

CoequalizersCokernels and quotients
Pushout
Direct limit

Algebraic categoriesSets

Relations

Magmas

Groups

Abelian groups

Rings (Fields)

Modules (Vector spaces)
Constructions on categories

Free category

Functor category

Kleisli category

Opposite category

Quotient category

Product category

Comma category

Subcategory

Higher category theory
Key concepts  Categorification
Enriched category
Higher-dimensional algebra
Homotopy hypothesis
Model category
Simplex category
String diagram
Topos

n-categoriesWeak  n -categoriesBicategory (pseudofunctor)

Tricategory

Tetracategory

Kan complex

∞-groupoid

∞-topos

Strict  n -categories2-category (2-functor)

3-category
Categorified concepts

2-group

2-ring

En-ring

(Traced)(Symmetric) monoidal category

n-group

n-monoid

Category

Outline

Glossary

v

t

e
Functor types

Additive

Adjoint

Conservative

Derived

Diagonal

Enriched

Essentially surjective

Exact

Forgetful

Full and faithful

Logical

Monoidal

Representable

Smooth
Retrieved from "
https://en.wikipedia.org/w/index.php?title=Adjoint_functors&oldid=1323887640
"  Category:

Adjoint functors
Hidden categories:

Articles with short description

Short description is different from Wikidata

Articles lacking in-text citations from January 2025

All articles lacking in-text citations

## Related

- [[A Source Book In Self Reference Reflexivitypd]]

## Related

- [[Recursive Identity]]

---

*Source: `Adjoint functors - Wikipedia.md` | Ingested: 2026-05-11*
