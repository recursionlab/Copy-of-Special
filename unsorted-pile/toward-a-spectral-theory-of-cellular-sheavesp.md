---
stub: true
title: "Toward A Spectral Theory Of Cellular Sheaves.P"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Toward a Spectral Theory of Cellular Sheaves.p.md"]
psi_tier: unclassified
---

# Toward A Spectral Theory Of Cellular Sheaves.P

# Toward a Spectral Theory of Cellular Sheaves.p

manuscript No. (will be inserted by the editor)
Toward a Spectral Theory of Cellular Sheaves
Jakob Hansen · Robert Ghrist
Received: date / Accepted: date
Abstract This paper outlines a program in what one might call spectral sheaf theory — an extension of spectral graph theory to cellular sheaves. By lifting the combinatorial graph Laplacian to the Hodge Laplacian on a cellular sheaf of vector spaces over a regular cell complex, one can relate spectral data to the sheaf cohomology and cell structure in a manner reminiscent of spectral graph theory. This work gives an exploratory introduction, and includes discussion of eigenvalue interlacing, sparsification, effective resistance, synchronization, and sheaf approximation. These results and subsequent applications are prefaced by an introduction to cellular sheaves and Laplacians.
Keywords Cohomology · Cellular sheaf theory · Spectral graph theory · Effective resistance · Eigenvalue interlacing
Mathematics Subject Classification (2000) MSC 55N30 · MSC 05C50
J. Hansen Department of Mathematics University of Pennsylvania David Rittenhouse Lab. 209 South 33rd Street Philadelphia, PA 19104-6395 E-mail:
jhansen@math.upenn.edu

R. Ghrist Departments of Mathematics and Electrical & Systems Engineering University of Pennsylvania David Rittenhouse Lab. 209 South 33rd Street Philadelphia, PA 19104-6395 E-mail:
ghrist@math.upenn.edu

2 Jakob Hansen, Robert Ghrist
1 Introduction
In spectral graph theory, one associates to a combinatorial graph additional algebraic structures in the form of square matrices whose spectral data is then investigated and related to the graph. These matrices come in several variants, most particularly degree and adjacency matrices, Laplacian matrices, and weighted or normalized versions thereof. In most cases, the size of the implicated matrix is based on the vertex set, while the structure of the matrix encodes data carried by the edges.
To say that spectral graph theory is useful is an understatement. Spectral methods are key in such disparate fields as data analysis [BN03,CL06], the-oretical computer science [HLW06,CS11], probability theory [LP16], control theory [Bul18], numerical linear algebra [ST14], coding theory [Spi96], and graph theory itself [Chu92,BH12].
Much of spectral graph theory focuses on the Laplacian, leveraging its unique combination of analytic, geometric, and probabilistic interpretations in the discrete setting. This is not the complete story. Many of the most well-known and well-used results on the spectrum of the graph Laplacian return features that are neither exclusively geometric nor even combinatorial in na-ture, but rather more qualitative. For example, it is among the first facts of spectral graph theory that the multiplicity of the zero eigenvalue of the graph Laplacian enumerates connected components of the graph, and the relative size of the smallest nonzero eigenvalue in a connected graph is a measure of approximate dis-connectivity. Such features are topological.
There is another branch of mathematics in which Laplacians hold sway: Hodge theory. This is the slice of algebraic and differential geometry that uses Laplacians on (complex) Riemannian manifolds to characterize global features. The classical initial result is that one recovers the cohomology of the manifold as the kernel of the Laplacian on differential forms [AMR88]. For example, the dimension of the kernel of the Laplacian on 0-forms (R-valued functions) is equal to the rank of H0, the 0-th cohomology group (with coefficients in R), whose dimension is the number of connected components. In spirit, then, Hodge theory categorifies elements of spectral graph theory.
Hodge theory, like much of algebraic topology, survives the discretization from Riemannian manifolds to (weighted) cell complexes [Eck45,Fri98]. The classical boundary operator for a cell complex and its formal adjoint combine to yield a generalization of the graph Laplacian which, like the Laplacian of Hodge theory, acts on higher dimensional objects (cellular cochains, as opposed to differential forms). The kernel of this discrete Laplacian is isomorphic to the cellular cohomology of the complex with coefficients in the reals, generalizing the connectivity detection of the graph Laplacian in grading zero. As such, the spectral theory of the discrete Laplacian offers a geometric perspective on algebraic-topological features of higher-dimensional complexes. Laplacians of higher-dimensional complexes have been the subject of recent investiga-tion [Par13,Ste13,HJ13].
Toward a Spectral Theory of Cellular Sheaves 3
This is not the end. Our aim is a generalization of both spectral graph theory and discrete Hodge theory which ties in to recent developments in topological data analysis. The past two decades have witnessed a burst of activity in computing the homology of cell complexes (and sequences thereof) to extract robust global features, leading to the development of specialized tools, such as persistent homology, barcodes, and more, as descriptors for cell complexes [Car12,EH10,KMM04,OPT+17].
Topological data analysis is evolving rapidly. One particular direction of evolution concerns a change in perspective from working with cell complexes as topological spaces in and of themselves to focusing instead on data over a cell complex — viewing the cell complex as a base on which data to be in-vestigated resides. For example, one can consider scalar-valued data over cell complexes, as occurs in weighted networks and complexes; or sensor data, as occurs in target enumeration problems [CGR12]. Richer data involves vector spaces and linear transformations, as with recent work in cryo-EM [HS11] and synchronization problems [Ban15]. Recent work in TDA points to a general-ization of these and related data structures over topological spaces. This is the theory of sheaves.
We will work exclusively with cellular sheaves [Cur14]. Fix a (regular, lo-cally finite) cell complex — a triangulated surface will suffice for purposes of imagination. A cellular sheaf of vector spaces is, in essence, a data structure on this domain, assigning local data (in the form of vector spaces) to cells and compatibility relations (linear transformations) between cells of incident as-cending dimension. These structure maps send data over vertices to data over incident edges, data over edges to data over incident 2-cells, etc. As a trivial example, the constant sheaf assigns a rank-one vector space to each cell and identity isomorphisms according to boundary faces. More interesting is the cel-lular analogue of a vector bundle: a cellular sheaf which assigns a fixed vector space of dimension n to each cell and isomorphisms as linear transformations (with specializations to O(n) or SO(n) as desired).
The data assigned to a cellular sheaf naturally arranges into a cochain com-plex graded by dimension of cells. As such, cellular sheaves possess a Laplacian that specializes to the graph Laplacian and the Hodge Laplacian for the con-stant sheaf. For cellular sheaves of real vector spaces, a spectral theory — an examination of the eigenvalues and eigenvectors of the sheaf Laplacian — is natural, motivated, and, to date, unexamined apart from a few special cases (see §3.6).
This paper sketches an emerging spectral theory for cellular sheaves. Given the motivation as a generalization of spectral graph theory, we will often spe-cialize to cellular sheaves over a 1-dimensional cell complex (that is, a graph, allowing when necessary multiple edges between a pair of vertices). This is mostly for the sake of simplicity and initial applications, as zero- and one-dimensional homological invariants are the most readily applicable. However, as the theory is general, we occasionally point to higher-dimensional side-quests.
4 Jakob Hansen, Robert Ghrist
The plan of this paper is as follows. In §2, we cover the necessary topologi-cal and algebraic preliminaries, including definitions of cellular sheaves. Next, §3 gives definitions of the various matrices involved in the extension of spectral theory to cellular sheaves. Section 4 uses these to explore issues related to har-monic functions and cochains on sheaves. In §5, we extend various elementary results from spectral graph theory to cellular sheaves. The subsequent two sec-tions treat more sophisticated topics, effective resistance (§6) and the Cheeger inequality (§7), for which we have some preliminary results. We conclude with outlines of potential applications for the theory in §8 and directions for future inquiry in §9.
The results and applications we sketch are at the beginnings of the subject, and a great deal more in way of fundamental and applied work remains.
This paper has been written in order to be readable without particular ex-pertise in algebraic topology beyond the basic ideas of cellular homology and cohomology. Category-theoretic terminology is used sparingly and for conci-sion. Given the well-earned reputation of sheaf theory as difficult for the non-specialist, we have provided an introductory section with terminology and core concepts, noting that much more is available in the literature [Bre97,KS90]. Our recourse to the cellular theory greatly increases simplicity, readability, and applicability, while resonating with the spirit of spectral graph theory. There are abundant references available for the reader who requires more information on algebraic topology [Hat01], applications thereof [EH10,Ghr14], and cellular sheaf theory [Cur14,Ghr14].
2 Preliminaries
2.1 Cell Complexes
Definition 2.1 A regular cell complex is a topological space X with a parti-tion into subspaces {Xα}α∈PX satisfying the following conditions:

For each x ∈ X, every sufficiently small neighborhood of x intersects finitely many Xα.

For all α, β, Xα ∩Xβ 6= ∅ only if Xβ ⊆ Xα. 3. Every Xα is homeomorphic to Rnα for some nα. 4. For every α, there is a homeomorphism of a closed ball in Rnα to Xα that
maps the interior of the ball homeomorphically onto Xα.
Condition (2) implies that the set PX has a poset structure, given by β ≤ α iff Xβ ⊆ Xα. This is known as the face poset of X. The regularity condition (4) implies that all topological information about X is encoded in the poset structure of PX . For our purposes, we will identify a regular cell complex with its face poset, writing the incidence relation βPα. The class of posets that arise in this way can be characterized combinatorially [Bjö84]. For our pur-poses, a morphism of cell complexes is a morphism of posets between their
Toward a Spectral Theory of Cellular Sheaves 5
face incidence posets that arises from a continuous map between their asso-ciated topological spaces. In particular, morphisms of simplicial and cubical complexes will qualify as morphisms of regular cell complexes.
The class of regular cell complexes includes simplicial complexes, cubi-cal complexes, and so-called multigraphs (as 1-dimensional cell complexes). As nearly every space that can be characterized combinatorially can be repre-sented as a regular cell complex, these will serve well as a default class of spaces over which to develop a combinatorial spectral theory of sheaves. We note that the spectral theory of complexes has heretofore been largely restricted to the study of simplicial complexes [SBH+18]. A number of our results will special-ize to results about the spectra of Hodge Laplacians of regular cell complexes by restricting to the constant sheaf.
A few notions associated to cell complexes will be useful.
Definition 2.2 The k-skeleton of a cell complex X, denoted X(k), is the sub-complex of X consisting of cells of dimension at most k.
Definition 2.3 Let σ be a cell of a regular cell complex X. The star of σ, denoted st(σ), is the set of cells τ such that σPτ .
Topologically, st(σ) is the smallest open collection of cells containing σ, a role we might denote as the “smallest cellular neighborhood” of σ. Stars serve an important purpose in giving combinatorial analogues of topological notions for maps. For instance, a morphism f : X → Y of cell complexes may be locally injective as defined on the topological spaces. Topologically, the condition for local injectivity is simply that every point in X have a neighborhood on which f is injective. Translating this to cell complexes, we require that for every cell σ ∈ X, f is injective on st(σ).
Topological continuity ensures that the preimage of a star st(σ) under a cell morphism f : X → Y is a union of stars; if f is locally injective, we see that it must be a disjoint union of stars. A locally injective map is, further, a covering map if on each component of f−1(st(σ)), f is an isomorphism. That is, the fiber of a star consists of a disjoint union of copies of that star.
2.2 Cellular Sheaves
Let X be a regular cell complex. A cellular sheaf attaches data spaces to the cells of X together with relations that specify when assignments to these data spaces are consistent.
Definition 2.4 A cellular sheaf of vector spaces on a regular cell complex X is an assignment of a vector space F(σ) to each cell σ of X together with a linear transformation FσPτ : F(σ) → F(τ) for each incident cell pair σP τ . These must satisfy both an identity relation FσPσ = id and the composition condition:
ρPσP τ ⇒ FρPτ = FσPτ ◦ FρPσ.
6 Jakob Hansen, Robert Ghrist
The vector space F(σ) is called the stalk of F at σ. The maps FσPτ are called the restriction maps.
For experts, this definition at first seems only reminiscent of the notion of sheaves familiar to topologists. The depth of the relationship is explained in detail in [Cur14], but the essence is this: the data of a cellular sheaf on X specifies spaces of local sections on a cover of X given by open stars of cells. This translates in two different ways into a genuine sheaf on a topological space. One may either take the Alexandrov topology on the face incidence poset of the complex, or one may view the open stars of cells and their natural refinements a basis for the topology of X. There then exists a natural completion of the data specified by the cellular sheaf to a constructible sheaf on X.
One may compress the definition of a cellular sheaf to the following: If X is a regular cell complex with face incidence poset PX , viewed as a category, a cellular sheaf is a functor F : PX → Vectk to the category of vector spaces over a field k.
Definition 2.5 Let F be a cellular sheaf on X. A global section x of F is a choice xσ ∈ F(σ) for each cell σ of X such that xτ = FσPτxσ for all σP τ . The space of global sections of F is denoted Γ (X;F).
Perhaps the simplest sheaf on any complex is the constant sheaf with stalk V, which we will denote V. This is the sheaf with all stalks equal to V and all restriction maps equal to the identity.
2.2.1 Cosheaves
In many situations it is more natural to consider a dual construction to a cellular sheaf. A cellular cosheaf preserves stalk data but reverses the direction of the face poset, and with it, the restriction maps.
Definition 2.6 A cellular cosheaf of vector spaces on a regular cell complexX is an assignment of a vector space F(σ) to each cell σ of X together with linear maps FσPτ : F(τ)→ F(σ) for each incident cell pair σP τ which satisfies the identity (FσPσ = id) and composition condition:
ρPσP τ ⇒ FρPτ = FρPσ ◦ FσPτ .
More concisely, a cellular cosheaf is a functor P op X → Vectk. The con-
travariant functor Hom(•,k) : Vectopk → Vectk gives every cellular sheaf F a dual cosheaf F̂ whose stalks are Hom(F(σ),k).
2.2.2 Homology and Cohomology
The cells of a regular cell complex have a natural grading by dimension. By regularity of the cell complex, this grading can be extracted from the face
Toward a Spectral Theory of Cellular Sheaves 7
incidence poset as the height of a cell in the poset. This means that a cellular sheaf has a graded vector space of cochains
Ck(X;F) = ⊕
dim(σ)=k
F(σ).
To develop this into a chain complex, we need a boundary operator and a notion of orientation — a signed incidence relation on PX . This is a map [• : •] : PX × PX → {0,±1} satisfying the following conditions:

If [σ : τ ] 6= 0, then σPτ and there are no cells between σ and τ in the incidence poset.

For any σPτ , ∑ γ∈PX [σ : γ][γ : τ ] = 0.
Given a signed incidence relation on PX , there exist coboundary maps δk : Ck(X;F)→ Ck+1(X;F). These are given by the formula
δk|F(σ) = ∑
dim(τ)=k+1
[σ : τ ]FσPτ ,
or equivalently, (δkx)τ =
∑ dim(σ)=k
[σ : τ ]FσPτ (xσ).
Here we use subscripts to denote the value of a cochain in a particular stalk; that is, xσ is the value of the cochain x in the stalk F(σ).
It is a simple consequence of the properties of the incidence relation and the commutativity of the restriction maps that δk ◦δk−1 = 0, so these coboundary maps define a cochain complex and hence a cohomology theory for cellular sheaves. In particular, H0(X;F) is naturally isomorphic to Γ (X;F), the space of global sections. An analogous construction defines a homology theory for cosheaves. Cosheaf homology may be thought of as dual to sheaf cohomology in a Poincaré-like sense. That is, frequently the natural analogue of degree zero sheaf cohomology is degree n cosheaf homology. A deeper formal version of this fact, exploiting an equivalence of derived categories, may be found in [Cur14, ch. 12].
There is a relative version of cellular sheaf cohomology. Let A be a sub-complex of X. There is a natural subspace of Ck(X;F) consisting of cochains which vanish on stalks over cells in A. The coboundary of a cochain which van-ishes on A also vanishes on A, since any cell in A(k+1) has only cells in A(k) on its boundary. We therefore get a subcomplex C•(X,A;F) of C•(X;F). The cohomology of this subcomplex is the relative sheaf cohomology H•(X,A;F). The natural maps between these spaces of cochains constitute a short exact sequence of complexes
0→ C•(X,A;F)→ C•(X;F)→ C•(A;F)→ 0,
from which a long exact sequence for relative sheaf cohomology arises:
0→ H0(X,A;F)→ H0(X;F)→ H0(A;F)→ H1(X,A;F)→ · · ·
8 Jakob Hansen, Robert Ghrist
2.2.3 Sheaf Morphisms
Definition 2.7 If F and G are sheaves on a cell complex X, a sheaf morphism ϕ : F → G is a collection of maps ϕσ : F(σ)→ G(σ) for each cell σ of X, such that for any σPτ , ϕτ ◦ FσPτ = GσPτ ◦ ϕσ. Equivalently, all diagrams of the following form commute:
F(σ) G(σ)
F(τ) G(τ)
FσPτ
ϕσ
GσPτ
ϕτ
This commutativity condition assures that a sheaf morphism ϕ : F → G induces maps ϕk : Ck(X;F) → Ck(X;G) which commute with the cobound-ary maps, resulting in the induced maps on cohomology Hkϕ : Hk(X;F) → Hk(X;G).
2.2.4 Sheaf Operations
There are several standard operations that act on sheaves to produce new sheaves.
Definition 2.8 (Direct sum) If F and G are sheaves on X, their direct sum F ⊕ G is a sheaf on X with (F ⊕ G)(σ) = F(σ)⊕ G(σ). The restriction maps are (F ⊕ G)σPτ = FσPτ ⊕ GσPτ .
Definition 2.9 (Tensor product) If F and G are sheaves on X, their tensor product F ⊗G is a sheaf on X with (F ⊗G)(σ) = F(σ)⊗G(σ). The restriction maps are (F ⊗ G)σPτ = FσPτ ⊗ GσPτ .
Definition 2.10 (Pullback) If f : X → Y is a morphism of cell complexes and F is a sheaf on Y , the pullback f∗F is a sheaf onX with f∗F(σ) = F(f(σ)) and (f∗F)σPτ = Ff(σ)Pf(τ).
Definition 2.11 (Pushforward) The full definition of the pushforward of a cellular sheaf is somewhat more categorically involved than the previous constructions. If f : X → Y is a morphism of cell complexes and F is a sheaf on X, the pushforward f∗F is a sheaf on Y with stalks f∗F(σ) given as the limit limσPf(τ) F(τ). The restriction maps are induced by the restriction maps of F , since whenever σPσ′, the cone for the limit defining f∗F(σ) contains the cone for the limit defining f∗F(σ′), inducing a unique map f∗F(σ)→ f∗F(σ′).
In this paper, we will mainly work with pushforwards over locally injective cell maps, that is, those whose geometric realizations are locally injective (see §2.1). If f : X → Y is locally injective, every cell σ ∈ X maps to a cell of the same dimension, and for every cell σ ∈ Y , f−1(st(σ)) is a disjoint union of subcomplexes, each of which maps injectively to Y . In this case, f∗F(σ) '
⊕ σ′∈f−1(σ) F(σ′), and (f∗F)σPτ =
⊕ (σ′Pτ ′)∈f−1(σPτ) Fσ′Pτ ′ . This
computational formula in fact holds more generally, if the stars of cells in f−1(σ) are disjoint.
Toward a Spectral Theory of Cellular Sheaves 9
Those familiar with the definitions of pushforward and pullback for sheaves over topological spaces will note a reversal of fates when we define sheaves over cell complexes. Here the pullback is simple to define, while the pushforward is more involved. This complication arises because cellular sheaves are in a sense defined pointwise rather than over open sets.
3 Definitions
3.1 Weighted Cellular Sheaves
Let k = R or C. A weighted cellular sheaf is a cellular sheaf with values in k-vector spaces where the stalks have additionally been given an inner product structure. Adding the condition of completeness to the stalks, one may view this as a functor PX → Hilbk, where Hilbk is the category whose objects are Hilbert spaces over k and whose morphisms are (bounded) linear maps.
The inner products on stalks of F extend by the orthogonal direct sum to inner products on Ck(X;F), making these Hilbert spaces as well. The canon-ical inner products on direct sums and subspaces of Hilbert spaces give the direct sum and tensor product of weighted cellular sheaves weighted struc-tures. Similarly, the pullbacks and pushforwards (over locally injective maps) of a weighted sheaf have canonical weighted structures given by their compu-tational formulae in §2.2.4.
Every morphism T : V → W between Hilbert spaces admits an adjoint map T ∗ : W → V , determined by the property that for all v ∈ V,w ∈ W , 〈w, Tv〉 = 〈T ∗w, v〉. One may readily check that (T ∗)∗ = T . This fact gives the category Hilbk a dagger structure, that is, a contravariant endofunctor † (here the adjoint operation ∗) which acts as the identity on objects and squares to the identity. In a dagger category, the notion of unitary isomorphisms makes sense: they are the invertible morphisms T such that T † = T−1.
The dagger structure of Hilbk introduces some categorical subtleties into the study of weighted cellular sheaves. The space of global sections of a cellu-lar sheaf is defined in categorical terms as the limit of the functor X → Vect defining the sheaf. This defines the space of global sections up to unique iso-morphism. We might want a weighted space of global sections to be a sort of limit in Hilbk which is defined up to unique unitary isomorphism. This is the notion of dagger limit, recently studied in [HK19]. Unfortunately, this work showed that Hilbk does not have all dagger limits; in particular, pullbacks over spans of noninjective maps do not exist. As a result, there is no single canonical way to define an inner product on the space of global sections of a cellular sheaf F . There are two approaches that seem most natural, however. One is to view the space of global sections of F as ker δ0F with the natural inner product given by inclusion into C0(X;F). The other is to view global sections as lying in
⊕ σ F(σ). We will generally take the view that global
sections are a subspace of C0(X;F); that is, we will weight Γ (X;F) by its canonical isomorphism with H0(X;F), as defined in §3.2.
10 Jakob Hansen, Robert Ghrist
The dagger structure on Hilbk gives a slightly different way to construct a dual cosheaf from a weighted cellular sheaf F . Taking the adjoint of each restriction map reverses their directions and hence yields a cosheaf with the same stalks as the original sheaf. From a categorical perspective, this amounts to composing the functor F with the dagger endofunctor on Hilbk. When stalks are finite dimensional, this dual cosheaf is isomorphic to the cosheaf F̂ defined in §2.2.1 via the dual vector spaces of stalks. In this situation, we have an isomorphism between the stalks of F and its dual cosheaf. This is reminis-cent of the bisheaves recently introduced by MacPherson and Patel [MP18]. However, the structure maps F(σ) → F̂(σ) will rarely commute with the re-striction and extension maps as required by the definition of the bisheaf — this only holds in general if all restriction maps are unitary. The bisheaf con-struction is meant to give a generalization of local systems, and as such fits better with our discussion of discrete vector bundles in §3.5.
3.2 The Sheaf Laplacian
Given a chain complex of Hilbert spaces C0 → C1 → · · · we can construct the Hodge Laplacian ∆ = (δ+ δ∗)2 = δ∗δ+ δδ∗. This operator is naturally graded into components ∆k : Ck → Ck, with ∆k = (δk)∗δk + δk−1(δk−1)∗. This op-erator can be further separated into up- (coboundary) and down- (boundary) Laplacians ∆k

= (δk)∗δk and ∆k − = δk−1(δk−1)∗ respectively.
A key observation is that on a finite-dimensional Hilbert space, ker δ∗ = (im δ)⊥. For if δ∗x = 0, then for all y, 0 = 〈δ∗x, y〉 = 〈x, δy〉, so that x ⊥ im δ. This allows us to express the kernels and images necessary to compute coho-mology purely in terms of kernels. This is the content of the central theorem of discrete Hodge theory:
Theorem 3.1 Let C0 → C1 → · · · be a chain complex of finite-dimensional Hilbert spaces, with Hodge Laplacians ∆k. Then ker∆k ∼= Hk(C•).
Proof. By definition,Hk(C•) = ker δk/ im δk−1. In a finite dimensional Hilbert space, ker δk/ im δk−1 is isomorphic to the orthogonal complement of im δk−1
in ker δk, which we may write (ker δk) ∩ (im δk−1)⊥ = (ker δk) ∩ (ker(δk−1)∗). So it suffices to show that ker∆k = (ker δk)∩ (ker(δk−1)∗). Note that ker δk = ker(δk)∗δk = ker∆k

and similarly for ∆k −. So we need to show that ker(∆k

∆k −) = ker∆k

∩ ker∆k −, which will be true if im∆k

∩ im∆k − = 0. But this is
true because im∆k + = im(δk)∗ = (ker δk)⊥ and im∆k
− = im δk−1 ⊆ ker δk.
The upshot of this theorem is that the kernel of ∆k gives a set of canonical representatives for elements of Hk(C•). This is commonly known as the space of harmonic cochains, denoted Hk(C•). In particular, the proof above implies that there is an orthogonal decomposition Ck = Hk ⊕ im δk−1 ⊕ im(δk)∗.
When the chain complex in question is the complex of cochains for a weighted cellular sheaf F , the Hodge construction produces the sheaf Lapla-cians. The Laplacian which is easiest to study and most immediately in-teresting is the degree-0 Laplacian, which is a generalization of the graph
Toward a Spectral Theory of Cellular Sheaves 11
Laplacian. We can represent it as a symmetric block matrix with blocks in-dexed by the vertices of the complex. The entries on the diagonal are ∆0
v,v =∑ vPe F∗vPeFvPe and the entries on the off-diagonal are ∆0
u,v = −F∗uPeFvPe, where e is the edge between v and u. Laplacians of other degrees have similar block structures.
The majority of results in combinatorial spectral theory have to do with up-Laplacians. We will frequently denote these Lk by analogy with spectral graph theory, where L typically denotes the (non-normalized) graph Laplacian. In particular, we will further elide the index k when k = 0, denoting the graph sheaf Laplacian by simply L. A subscript will be added when necessary to identify the sheaf, e.g. LF or ∆k
F . Weighted labeled graphs are in one-to-one correspondence with graph Lapla-
cians. The analogous statement is not true of sheaves on a graph. For instance, the sheaves in Figure 3.1 have coboundary maps with matrix representations1 −11 0
0 1
 and
[ 1√ 2
1√ 2√
3 2 −
√ 3 2
] ,
which means that the Laplacian for each is equal to[ 2 −1 −1 2
] .
However, these sheaves are not unitarily isomorphic, as can be seen immedi-ately by checking the stalk dimensions. More pithily, one cannot hear the shape of a sheaf. One source of the lossiness in the sheaf Laplacian representation is that restriction maps may be the zero morphism, effectively allowing for edges that are only attached to one vertex. More generally, restriction maps may fail to be full rank, which means that it is impossible to identify the dimensions of edge stalks from the Laplacian.
R RR
RR
0
1 1
1 1
R RR 2
00
0
[
1 √
2 √
3
2
] [
−
1 √
2 √
3
2
]
Fig. 3.1 Two nonisomorphic sheaves with the same Laplacian.
12 Jakob Hansen, Robert Ghrist
3.2.1 Harmonic Cochains
The elements of ker∆k = Hk are known as harmonic k-cochains. More gener-ally, a k-cochain may be harmonic on a subcomplex:
Definition 3.2 A k-cochain x of a sheaf F on a cell complex X is harmonic on a set S of k-cells if (∆k
Fx)|S = 0.
When k = 0 and F is the constant sheaf (i.e., in spectral graph theory), this can be expressed as a local averaging property: For each v ∈ S, xv = 1 dv
∑ u∼v xu, where ∼ indicates adjacency and dv is the degree of the vertex v.
3.2.2 Identifying Sheaf Laplacians
Given a regular cell complex X and a choice of dimension for each stalk, one can identify the collection of matrices which arise as coboundary maps for a sheaf on X as those matrices satisfying a particular block sparsity pattern. This sparsity pattern controls the number of nonzero blocks in each row of the matrix. Restricting to δ0, we get a matrix whose rows have at most two nonzero blocks. The space of matrices which arise as sheaf Laplacians is then the space of matrices which have a factorization L = δ∗δ, where δ is a matrix satisfying this block sparsity condition. Boman et al. studied this class of ma-trices when the blocks have size 1 × 1, calling them matrices of factor width two [BCPT05]. They showed that this class coincides with the class of sym-metric generalized diagonally dominant matrices, those matrices L for which there exists a positive diagonal matrix D such that DLD is diagonally domi-nant. Indeed, the fact that sheaves on graphs are not in general determined by their Laplacians is in part a consequence of the nonuniqueness of width-two factorizations.
3.3 Approaching Infinite-Dimensional Laplacians
The definitions given in this paper are adapted to the case of sheaves of finite dimensional Hilbert spaces over finite cell complexes. Relaxing these finiteness constraints introduces new complications.
The spaces of cochains naturally acquire inner products by taking the Hilbert space direct sum. These are not the same as taking the algebraic direct sum or product of stalks. However, there is a sequence of inclusions of complexes
C•c (X;F) ⊆ L2C•(X;F) ⊆ C•(X;F)
inducing algebraic maps between the corresponding compactly supported, L2, and standard sheaf cohomology theories.
The theory of abstract complexes of possibly infinite-dimensional Hilbert spaces has been developed in [BL92]. This paper explains conditions for the spaces of harmonic cochains of a complex to be isomorphic with the algebraic
Toward a Spectral Theory of Cellular Sheaves 13
cohomology of the complex. A particularly nice condition is that the complex have finitely generated cohomology, which implies that the total coboundary map is a Fredholm operator. More generally, if the images of the coboundary and its adjoint are closed, the spaces of harmonic cochains will be isomorphic to the cohomology.
Further issues arise when we consider the coboundary maps δk. For spec-tral purposes, it is in general desirable for these to be bounded linear maps, for which we must make some further stipulations. Sufficient conditions for coboundary maps to be bounded are as follows:
Proposition 3.3 Let F be a sheaf of Hilbert spaces on a cell complex X. Suppose that there exists some Mk such that for every pair of cells σPτ with dimσ = k and dim τ = k+1, ‖FσPτ‖ ≤Mk. Further suppose that every k-cell in X has at most dk cofaces of dimension k + 1, and every (k + 1)-cell in X has at most dk+1 faces of dimension k. Then δkF is a bounded linear operator.
Proof. We compute:

[... content truncated ...]

---

*Source: `Toward a Spectral Theory of Cellular Sheaves.p.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
