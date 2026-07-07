---
title: "Simplicial complex"
source: "https://en.wikipedia.org/wiki/Simplicial_complex"
author:
  - "[[Wikipedia]]"
published: 2003-06-25
created: 2026-06-02
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), a **simplicial complex** is a structured [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") of *[simplices](https://en.wikipedia.org/wiki/Simplex "Simplex")* (for example, [points](https://en.wikipedia.org/wiki/Point_\(geometry\) "Point (geometry)"), [line segments](https://en.wikipedia.org/wiki/Line_segment "Line segment"), [triangles](https://en.wikipedia.org/wiki/Triangle "Triangle"), and their *n* -dimensional counterparts) such that all the [faces](https://en.wikipedia.org/wiki/Face_\(geometry\) "Face (geometry)") and intersections of the elements are also included in the set (see illustration). Simplicial complexes should not be confused with the more abstract notion of a [simplicial set](https://en.wikipedia.org/wiki/Simplicial_set "Simplicial set") appearing in modern simplicial [homotopy theory](https://en.wikipedia.org/wiki/Homotopy_theory "Homotopy theory"). The purely [combinatorial](https://en.wikipedia.org/wiki/Combinatorics "Combinatorics") counterpart to a simplicial complex is an [abstract simplicial complex](https://en.wikipedia.org/wiki/Abstract_simplicial_complex "Abstract simplicial complex"). To distinguish a simplicial complex from an abstract simplicial complex, the former is often called a **geometric simplicial complex**.[^1]<sup><span title="Page: 7">: 7</span></sup>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Simplicial_complex_example.svg/250px-Simplicial_complex_example.svg.png)

A simplicial 3-complex.

## Definitions

A **simplicial complex** ${\displaystyle {\mathcal {K}}}$ is a set of [simplices](https://en.wikipedia.org/wiki/Simplex "Simplex") that satisfies the following conditions:

1. Every [face](https://en.wikipedia.org/wiki/Simplex#Elements "Simplex") of a simplex from ${\displaystyle {\mathcal {K}}}$ is also in ${\displaystyle {\mathcal {K}}}$.
2. The non-empty [intersection](https://en.wikipedia.org/wiki/Set_intersection "Set intersection") of any two simplices ${\displaystyle \sigma _{1},\sigma _{2}\in {\mathcal {K}}}$ is a face of both ${\displaystyle \sigma _{1}}$ and ${\displaystyle \sigma _{2}}$.

See also the definition of an [abstract simplicial complex](https://en.wikipedia.org/wiki/Abstract_simplicial_complex "Abstract simplicial complex"), which loosely speaking is a simplicial complex without an associated geometry.

A **simplicial *k* -complex** ${\displaystyle {\mathcal {K}}}$ is a simplicial complex where the largest dimension of any simplex in ${\displaystyle {\mathcal {K}}}$ equals *k*. For instance, a simplicial 2-complex must contain at least one triangle, and must not contain any [tetrahedra](https://en.wikipedia.org/wiki/Tetrahedra "Tetrahedra") or higher-dimensional simplices.

A **pure** or **homogeneous** simplicial *k* -complex ${\displaystyle {\mathcal {K}}}$ is a simplicial complex where every simplex of dimension less than *k* is a face of some simplex ${\displaystyle \sigma \in {\mathcal {K}}}$ of dimension exactly *k*. Informally, a pure 1-complex "looks" like it's made of a bunch of lines, a 2-complex "looks" like it's made of a bunch of triangles, etc. An example of a *non* -homogeneous complex is a triangle with a line segment attached to one of its vertices. Pure simplicial complexes can be thought of as [triangulations](https://en.wikipedia.org/wiki/Triangulation_\(topology\) "Triangulation (topology)") and provide a definition of [polytopes](https://en.wikipedia.org/wiki/Polytope "Polytope").

A **facet** is a maximal simplex, i.e., any simplex in a complex that is *not* a face of any larger simplex.[^2] (Note the difference from a ["face" of a simplex](https://en.wikipedia.org/wiki/Face_of_a_simplex "Face of a simplex")). A pure simplicial complex can be thought of as a complex where all facets have the same dimension. For (boundary complexes of) [simplicial polytopes](https://en.wikipedia.org/wiki/Simplicial_polytope "Simplicial polytope") this coincides with the meaning from polyhedral combinatorics.

Sometimes the term *face* is used to refer to a simplex of a complex, not to be confused with a face of a simplex.

For a simplicial complex [embedded](https://en.wikipedia.org/wiki/Embedding "Embedding") in a *k* -dimensional space, the *k* -faces are sometimes referred to as its **cells**. The term *cell* is sometimes used in a broader sense to denote a set [homeomorphic](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") to a simplex, leading to the definition of [cell complex](https://en.wikipedia.org/wiki/Cell_complex "Cell complex").

The **underlying space**, sometimes called the **carrier** of a simplicial complex, is the [union](https://en.wikipedia.org/wiki/Union_\(set_theory\) "Union (set theory)") of its simplices. It is usually denoted by ${\displaystyle |{\mathcal {K}}|}$ or ${\displaystyle \|{\mathcal {K}}\|}$.

## Support

The [relative interiors](https://en.wikipedia.org/wiki/Relative_interior "Relative interior") of all simplices in ${\displaystyle {\mathcal {K}}}$ form a partition of its underlying space ${\displaystyle |{\mathcal {K}}|}$: for each point ${\displaystyle x\in |{\mathcal {K}}|}$, there is exactly one simplex in ${\displaystyle {\mathcal {K}}}$ containing ${\displaystyle x}$ in its relative interior. This simplex is called the **support** of *x* and denoted ${\displaystyle \operatorname {supp} (x)}$.[^3]<sup><span title="Page: 9">: 9</span></sup>

## Closure, star, and link

- ![Two simplices and their closure.](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Simplicial_complex_closure.svg/960px-Simplicial_complex_closure.svg.png)
	Two simplices and their closure.
	Two simplices and their **closure**.
- ![A vertex and its star.](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Simplicial_complex_star.svg/960px-Simplicial_complex_star.svg.png)
	A vertex and its star.
	A vertex and its **star**.
- ![A vertex and its link.](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Simplicial_complex_link.svg/960px-Simplicial_complex_link.svg.png)
	A vertex and its link.
	A vertex and its **link**.

Let *K* be a simplicial complex and let *S* be a collection of simplices in *K*.

The **closure** of *S* (denoted ${\displaystyle \mathrm {Cl} \ S}$) is the smallest simplicial subcomplex of *K* that contains each simplex in *S*. ${\displaystyle \mathrm {Cl} \ S}$ is obtained by repeatedly adding to *S* each face of every simplex in *S*.

The **[star](https://en.wikipedia.org/wiki/Star_\(simplicial_complex\) "Star (simplicial complex)")** of *S* (denoted ${\displaystyle \mathrm {st} \ S}$) is the union of the stars of each simplex in *S*. For a single simplex *s*, the star of *s* is the set of simplices in *K* that have *s* as a face. The star of *S* is generally not a simplicial complex itself, so some authors define the **closed star** of S (denoted ${\displaystyle \mathrm {St} \ S}$) as ${\displaystyle \mathrm {Cl} \ \mathrm {st} \ S}$ the closure of the star of S.

The **[link](https://en.wikipedia.org/wiki/Link_\(simplicial_complex\) "Link (simplicial complex)")** of *S* (denoted ${\displaystyle \mathrm {Lk} \ S}$) equals ${\displaystyle \mathrm {Cl} {\big (}\mathrm {st} (S){\big )}\setminus \mathrm {st} {\big (}\mathrm {Cl} (S){\big )}}$. It is the closed star of *S* minus the stars of all faces of *S*.

## Algebraic topology

In [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology"), simplicial complexes are often useful for concrete calculations. For the definition of [homology groups](https://en.wikipedia.org/wiki/Homology_group "Homology group") of a simplicial complex, one can read the corresponding [chain complex](https://en.wikipedia.org/wiki/Chain_complex "Chain complex") directly, provided that consistent orientations are made of all simplices. The requirements of [homotopy theory](https://en.wikipedia.org/wiki/Homotopy_theory "Homotopy theory") lead to the use of more general spaces, the [CW complexes](https://en.wikipedia.org/wiki/CW_complex "CW complex"). Infinite complexes are a technical tool basic in algebraic topology. In algebraic topology, a [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space") [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") which is homeomorphic to the geometric realization of a finite simplicial complex is usually called a [polyhedron](https://en.wikipedia.org/wiki/Polyhedron "Polyhedron") (see [Spanier 1966](#CITEREFSpanier1966), [Maunder 1996](#CITEREFMaunder1996), [Hilton & Wylie 1967](#CITEREFHiltonWylie1967)).

## Combinatorics

[Combinatorialists](https://en.wikipedia.org/wiki/Combinatorics "Combinatorics") often study the ***f* -vector** of a simplicial d-complex Δ, which is the [integer](https://en.wikipedia.org/wiki/Integer "Integer") sequence ${\displaystyle (f_{0},f_{1},f_{2},\ldots ,f_{d+1})}$, where *f* <sub><i>i</i></sub> is the number of (*i* −1)-dimensional faces of Δ (by convention, *f* <sub>0</sub> = 1 unless Δ is the empty complex). For instance, if Δ is the boundary of the [octahedron](https://en.wikipedia.org/wiki/Octahedron "Octahedron"), then its *f* -vector is (1, 6, 12, 8), and if Δ is the first simplicial complex pictured above, its *f* -vector is (1, 18, 23, 8, 1). A complete characterization of the possible *f* -vectors of simplicial complexes is given by the [Kruskal–Katona theorem](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Katona_theorem "Kruskal–Katona theorem").

By using the *f* -vector of a simplicial *d* -complex Δ as coefficients of a [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") (written in decreasing order of exponents), we obtain the **f-polynomial** of Δ. In our two examples above, the *f* -polynomials would be ${\displaystyle x^{3}+6x^{2}+12x+8}$ and ${\displaystyle x^{4}+18x^{3}+23x^{2}+8x+1}$, respectively.

Combinatorists are often quite interested in the **h-vector** of a simplicial complex Δ, which is the sequence of coefficients of the polynomial that results from plugging *x* − 1 into the *f* -polynomial of Δ. Formally, if we write *F* <sub>Δ</sub> (*x*) to mean the *f* -polynomial of Δ, then the **h-polynomial** of Δ is

${\displaystyle F_{\Delta }(x-1)=h_{0}x^{d+1}+h_{1}x^{d}+h_{2}x^{d-1}+\cdots +h_{d}x+h_{d+1}}$

and the *h* -vector of Δ is

${\displaystyle (h_{0},h_{1},h_{2},\cdots ,h_{d+1}).}$

We calculate the h-vector of the octahedron boundary (our first example) as follows:

${\displaystyle F(x-1)=(x-1)^{3}+6(x-1)^{2}+12(x-1)+8=x^{3}+3x^{2}+3x+1.}$

So the *h* -vector of the boundary of the octahedron is (1, 3, 3, 1). It is not an accident this *h* -vector is symmetric. In fact, this happens whenever Δ is the boundary of a simplicial [polytope](https://en.wikipedia.org/wiki/Polytope "Polytope") (these are the [Dehn–Sommerville equations](https://en.wikipedia.org/wiki/Dehn%E2%80%93Sommerville_equations "Dehn–Sommerville equations")). In general, however, the *h* -vector of a simplicial complex is not even necessarily positive. For instance, if we take Δ to be the 2-complex given by two triangles intersecting only at a common vertex, the resulting *h* -vector is (1, 3, −2).

A complete characterization of all simplicial polytope *h* -vectors is given by the celebrated [g-theorem](https://en.wikipedia.org/wiki/G-theorem "G-theorem") of [Stanley](https://en.wikipedia.org/wiki/Richard_P._Stanley "Richard P. Stanley"), Billera, and Lee.

Simplicial complexes can be seen to have the same geometric structure as the [contact graph](https://en.wikipedia.org/wiki/Contact_graph "Contact graph") of a [sphere packing](https://en.wikipedia.org/wiki/Sphere_packing "Sphere packing") (a graph where vertices are the centers of spheres and edges exist if the corresponding packing elements touch each other) and as such can be used to determine the combinatorics of sphere packings, such as the number of touching pairs (1-simplices), touching triplets (2-simplices), and touching quadruples (3-simplices) in a sphere packing.

## Triangulation

A triangulation of a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") ${\displaystyle X}$ is a [homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") ${\displaystyle t:|{\mathcal {T}}|\rightarrow X}$ where ${\displaystyle {\mathcal {T}}}$ is a simplicial complex.

Topological spaces do not necessarily admit a triangulation and if they do, it is never unique. [Topological manifolds](https://en.wikipedia.org/wiki/Topological_manifold "Topological manifold") of dimension ${\displaystyle d\leq 3}$ are always triangulable,[^4] [^5] [^6] but not necessarily for ${\displaystyle d>3}$.[^7] [^8]

[Differentiable manifolds](https://en.wikipedia.org/wiki/Differentiable_manifold "Differentiable manifold") of any dimension ${\displaystyle d\geq 1}$ admit triangulations.[^9]

## Embedding

Any abstract ${\displaystyle d}$ -dimensional simplicial complex can be embedded in a ${\displaystyle (2d+1)}$ -dimensional space.[^10]<sup><span title="Page / location: Ch. I Th. 3">: Ch. I Th. 3</span> </sup> [^11]<sup><span title="Page / location: Ch. IV §1.9">: Ch. IV §1.9</span> </sup> This result is piecewise linear counterpart of the (weak) [Whitney embedding theorem](https://en.wikipedia.org/wiki/Whitney_embedding_theorem "Whitney embedding theorem").

## Computational problems

The [simplicial complex recognition problem](https://en.wikipedia.org/wiki/Simplicial_complex_recognition_problem "Simplicial complex recognition problem") is: given a finite simplicial complex, decide whether it is homeomorphic to a given geometric object. This problem is [undecidable](https://en.wikipedia.org/wiki/Undecidable_problem "Undecidable problem") for any *d* -dimensional manifolds for ${\displaystyle d\geq 5}$.[^12] [^13]<sup><span title="Pages: 9–11">: 9–11</span></sup>

[^1]: [Matoušek, Jiří](https://en.wikipedia.org/wiki/Ji%C5%99%C3%AD_Matou%C5%A1ek_\(mathematician\) "Jiří Matoušek (mathematician)") (2007). *[Using the Borsuk-Ulam Theorem](https://en.wikipedia.org/wiki/Using_the_Borsuk-Ulam_Theorem "Using the Borsuk-Ulam Theorem"): Lectures on Topological Methods in Combinatorics and Geometry* (2nd ed.). Berlin-Heidelberg: Springer-Verlag. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-00362-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-00362-5 "Special:BookSources/978-3-540-00362-5"). Written in cooperation with [Anders Björner](https://en.wikipedia.org/wiki/Anders_Bj%C3%B6rner "Anders Björner") and [Günter M. Ziegler](https://en.wikipedia.org/wiki/G%C3%BCnter_M._Ziegler "Günter M. Ziegler"), Section 4.3

[^2]: [De Loera, Jesús A.](https://en.wikipedia.org/wiki/Jes%C3%BAs_A._De_Loera "Jesús A. De Loera"); Rambau, Jörg; [Santos, Francisco](https://en.wikipedia.org/wiki/Francisco_Santos_Leal "Francisco Santos Leal") (2010), [*Triangulations: Structures for Algorithms and Applications*](https://books.google.com/books?id=SxY1Xrr12DwC&pg=PA493), Algorithms and Computation in Mathematics, vol. 25, Springer, p. 493, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9783642129711](https://en.wikipedia.org/wiki/Special:BookSources/9783642129711 "Special:BookSources/9783642129711")

[^3]: [Matoušek, Jiří](https://en.wikipedia.org/wiki/Ji%C5%99%C3%AD_Matou%C5%A1ek_\(mathematician\) "Jiří Matoušek (mathematician)") (2007). *[Using the Borsuk-Ulam Theorem](https://en.wikipedia.org/wiki/Using_the_Borsuk-Ulam_Theorem "Using the Borsuk-Ulam Theorem"): Lectures on Topological Methods in Combinatorics and Geometry* (2nd ed.). Berlin-Heidelberg: Springer-Verlag. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-00362-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-00362-5 "Special:BookSources/978-3-540-00362-5"). Written in cooperation with [Anders Björner](https://en.wikipedia.org/wiki/Anders_Bj%C3%B6rner "Anders Björner") and [Günter M. Ziegler](https://en.wikipedia.org/wiki/G%C3%BCnter_M._Ziegler "Günter M. Ziegler"), Section 4.3

[^4]: Edwin Moise (1977), *Geometric Topology in Dimensions 2 and 3*, New York: Springer Verlag

[^5]: Rado, Tibor. ["Über den Begriff der Riemannschen Fläche"](https://www.maths.ed.ac.uk/~v1ranick/papers/rado.pdf) (PDF) (in German).

[^6]: John M. Lee (2000), *Introduction to Topological manifolds*, New York/Berlin/Heidelberg: Springer Verlag, p. 92, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-98759-2](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98759-2 "Special:BookSources/0-387-98759-2")

[^7]: R. C. Kirby; L. C. Siebenmann (1977-12-31), "Annex B. On The Triangulation of Manifolds and the Hauptvermutung", *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations. (AM-88)*, Princeton University Press, pp. 299–306

[^8]: Akbulut, Selman; McCarthy, John D. (19 April 2016). "Chapter IV: Casson's Invariant for Oriented Homology 3-spheres". *Casson's Invariant for Oriented Homology Three-Spheres | Princeton University Press*. Princeton University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780691636085](https://en.wikipedia.org/wiki/Special:BookSources/9780691636085 "Special:BookSources/9780691636085").

[^9]: J. H. C. Whitehead (1940), "On C1-Complexes", *Annals of Mathematics*, vol. 41, no. 4, pp. 809–824, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/1968861](https://doi.org/10.2307%2F1968861), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0003-486X](https://search.worldcat.org/issn/0003-486X), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [1968861](https://www.jstor.org/stable/1968861)

[^10]: [Pontryagin, LS](https://en.wikipedia.org/wiki/Lev_Pontryagin "Lev Pontryagin") (1952). *Foundations of combinatorial topology*. Rochester N.Y.: Graylock Press.

[^11]: [Alexandrov, Pavel Sergeyevich](https://en.wikipedia.org/wiki/Lev_Pontryagin "Lev Pontryagin") (1956). *Combinatorial topology*. Rochester N.Y.: Graylock Press.

[^12]: [Stillwell, John](https://en.wikipedia.org/wiki/John_Stillwell "John Stillwell") (1993), [*Classical Topology and Combinatorial Group Theory*](https://books.google.com/books?id=265lbM42REMC&pg=PA247), Graduate Texts in Mathematics, vol. 72, Springer, p. 247, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780387979700](https://en.wikipedia.org/wiki/Special:BookSources/9780387979700 "Special:BookSources/9780387979700").

[^13]: Poonen, Bjorn (2014-10-25). "Undecidable problems: a sampler". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1204.0299](https://arxiv.org/abs/1204.0299) \[[math.LO](https://arxiv.org/archive/math.LO)\].