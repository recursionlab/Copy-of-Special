---
title: "Atlas (topology)"
source: "https://en.wikipedia.org/wiki/Atlas_(topology)"
author:
  - "[[Wikipedia]]"
published: 2002-02-25
created: 2026-04-29
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), particularly [topology](https://en.wikipedia.org/wiki/Topology "Topology"), an **atlas** is a concept used to describe a [manifold](https://en.wikipedia.org/wiki/Manifold "Manifold"). An atlas consists of individual *charts* that, roughly speaking, describe individual regions of the manifold. In general, the notion of atlas underlies the formal definition of a [manifold](https://en.wikipedia.org/wiki/Manifold "Manifold") and related structures such as [vector bundles](https://en.wikipedia.org/wiki/Vector_bundle "Vector bundle") and other [fiber bundles](https://en.wikipedia.org/wiki/Fiber_bundle "Fiber bundle").

## Charts

The definition of an atlas depends on the notion of a *chart*. A **chart** for a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") *M* is a [homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") ${\displaystyle \varphi }$ from an [open subset](https://en.wikipedia.org/wiki/Open_set "Open set") *U* of *M* to an open subset of a [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space"). The chart is traditionally recorded as the ordered pair ${\displaystyle (U,\varphi )}$.[^1]

When a coordinate system is chosen in the Euclidean space, this defines coordinates on ${\displaystyle U}$: the coordinates of a point ${\displaystyle P}$ of ${\displaystyle U}$ are defined as the coordinates of ${\displaystyle \varphi (P).}$ The pair formed by a chart and such a coordinate system is called a **local coordinate system**, **coordinate chart**, **coordinate patch**, **coordinate map**, or **local frame**.

## Formal definition of atlas

An **atlas** for a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") ${\displaystyle M}$ is an [indexed family](https://en.wikipedia.org/wiki/Indexed_family "Indexed family") ${\displaystyle \{(U_{\alpha },\varphi _{\alpha }):\alpha \in I\}}$ of charts on ${\displaystyle M}$ which [covers](https://en.wikipedia.org/wiki/Cover_\(topology\) "Cover (topology)") ${\displaystyle M}$ (that is, ${\textstyle \bigcup _{\alpha \in I}U_{\alpha }=M}$). If for some fixed *n*, the [image](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)") of each chart is an open subset of *n* -dimensional [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space"), then ${\displaystyle M}$ is said to be an *n* -dimensional [manifold](https://en.wikipedia.org/wiki/Manifold "Manifold").

The plural of atlas is *atlases*, although some authors use *atlantes*.[^2] [^3]

An atlas ${\displaystyle \left(U_{i},\varphi _{i}\right)_{i\in I}}$ on an ${\displaystyle n}$ -dimensional manifold ${\displaystyle M}$ is called an **adequate atlas** if the following conditions hold:

- The [image](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)") of each chart is either ${\displaystyle \mathbb {R} ^{n}}$ or ${\displaystyle \mathbb {R} _{+}^{n}}$, where ${\displaystyle \mathbb {R} _{+}^{n}}$ is the [closed half-space](https://en.wikipedia.org/wiki/Closed_half-space "Closed half-space"),
- ${\displaystyle \left(U_{i}\right)_{i\in I}}$ is a [locally finite](https://en.wikipedia.org/wiki/Locally_finite_collection "Locally finite collection") open cover of ${\displaystyle M}$, and
- ${\textstyle M=\bigcup _{i\in I}\varphi _{i}^{-1}\left(B_{1}\right)}$, where ${\displaystyle B_{1}}$ is the open ball of radius 1 centered at the origin.

Every [second-countable](https://en.wikipedia.org/wiki/Second-countable "Second-countable") manifold admits an adequate atlas.[^4] Moreover, if ${\displaystyle {\mathcal {V}}=\left(V_{j}\right)_{j\in J}}$ is an open covering of the second-countable manifold ${\displaystyle M}$, then there is an adequate atlas ${\displaystyle \left(U_{i},\varphi _{i}\right)_{i\in I}}$ on ${\displaystyle M}$, such that ${\displaystyle \left(U_{i}\right)_{i\in I}}$ is a [refinement](https://en.wikipedia.org/wiki/Refinement_of_a_cover "Refinement of a cover") of ${\displaystyle {\mathcal {V}}}$.[^4]

## Transition maps

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Two_coordinate_charts_on_a_manifold.svg/250px-Two_coordinate_charts_on_a_manifold.svg.png)

${\displaystyle M}$

${\displaystyle U_{\alpha }}$

${\displaystyle U_{\beta }}$

${\displaystyle \varphi _{\alpha }}$

${\displaystyle \varphi _{\beta }}$

${\displaystyle \tau _{\alpha ,\beta }}$

${\displaystyle \tau _{\beta ,\alpha }}$

${\displaystyle \mathbf {R} ^{n}}$

${\displaystyle \mathbf {R} ^{n}}$

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Two_coordinate_charts_on_a_manifold.svg/250px-Two_coordinate_charts_on_a_manifold.svg.png)

Two charts on a manifold, and their respective **transition map**

A transition map provides a way of comparing two charts of an atlas. To make this comparison, we consider the composition of one chart with the [inverse](https://en.wikipedia.org/wiki/Inverse_function "Inverse function") of the other. This composition is not well-defined unless we restrict both charts to the [intersection](https://en.wikipedia.org/wiki/Intersection_\(set_theory\) "Intersection (set theory)") of their [domains](https://en.wikipedia.org/wiki/Domain_of_a_function "Domain of a function") of definition. (For example, if we have a chart of Europe and a chart of Russia, then we can compare these two charts on their overlap, namely the European part of Russia.)

To be more precise, suppose that ${\displaystyle (U_{\alpha },\varphi _{\alpha })}$ and ${\displaystyle (U_{\beta },\varphi _{\beta })}$ are two charts for a manifold *M* such that ${\displaystyle U_{\alpha }\cap U_{\beta }}$ is [non-empty](https://en.wikipedia.org/wiki/Empty_set "Empty set"). The **transition map** ${\displaystyle \tau _{\alpha ,\beta }:\varphi _{\alpha }(U_{\alpha }\cap U_{\beta })\to \varphi _{\beta }(U_{\alpha }\cap U_{\beta })}$ is the map defined by 
$$
{\displaystyle \tau _{\alpha ,\beta }=\varphi _{\beta }\circ \varphi _{\alpha }^{-1}.}
$$

Note that since ${\displaystyle \varphi _{\alpha }}$ and ${\displaystyle \varphi _{\beta }}$ are both homeomorphisms, the transition map ${\displaystyle \tau _{\alpha ,\beta }}$ is also a homeomorphism.

## More structure

One often desires more structure on a manifold than simply the topological structure. For example, if one would like an unambiguous notion of [differentiation](https://en.wikipedia.org/wiki/Differentiation_\(mathematics\) "Differentiation (mathematics)") of functions on a manifold, then it is necessary to construct an atlas whose transition functions are [differentiable](https://en.wikipedia.org/wiki/Differentiable_function "Differentiable function"). Such a manifold is called [differentiable](https://en.wikipedia.org/wiki/Differentiable_manifold "Differentiable manifold"). Given a differentiable manifold, one can unambiguously define the notion of [tangent vectors](https://en.wikipedia.org/wiki/Tangent_vectors "Tangent vectors") and then [directional derivatives](https://en.wikipedia.org/wiki/Directional_derivative "Directional derivative").

If each transition function is a [smooth map](https://en.wikipedia.org/wiki/Smooth_map "Smooth map"), then the atlas is called a [smooth atlas](https://en.wikipedia.org/wiki/Smooth_structure "Smooth structure"), and the manifold itself is called [smooth](https://en.wikipedia.org/wiki/Differentiable_manifold#Definition "Differentiable manifold"). Alternatively, one could require that the transition maps have only *k* continuous derivatives in which case the atlas is said to be ${\displaystyle C^{k}}$.

Very generally, if each transition function belongs to a [pseudogroup](https://en.wikipedia.org/wiki/Pseudogroup "Pseudogroup") ${\displaystyle {\mathcal {G}}}$ of homeomorphisms of Euclidean space, then the atlas is called a ${\displaystyle {\mathcal {G}}}$ -atlas. If the transition maps between charts of an atlas preserve a [local trivialization](https://en.wikipedia.org/wiki/Local_trivialization "Local trivialization"), then the atlas defines the structure of a fibre bundle.

[^1]: Jänich, Klaus (2005). *Vektoranalysis* (in German) (5 ed.). Springer. p. 1. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [3-540-23741-0](https://en.wikipedia.org/wiki/Special:BookSources/3-540-23741-0 "Special:BookSources/3-540-23741-0").

[^2]: Jost, Jürgen (11 November 2013). [*Riemannian Geometry and Geometric Analysis*](https://books.google.com/books?id=VRz2CAAAQBAJ&pg=PA1). Springer Science & Business Media. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9783662223857](https://en.wikipedia.org/wiki/Special:BookSources/9783662223857 "Special:BookSources/9783662223857"). Retrieved 16 April 2018 – via Google Books.

[^3]: Giaquinta, Mariano; Hildebrandt, Stefan (9 March 2013). [*Calculus of Variations II*](https://books.google.com/books?id=_ZT_CAAAQBAJ&pg=PA418). Springer Science & Business Media. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9783662062012](https://en.wikipedia.org/wiki/Special:BookSources/9783662062012 "Special:BookSources/9783662062012"). Retrieved 16 April 2018 – via Google Books.

[^4]: Kosinski, Antoni (2007). *Differential manifolds*. Mineola, N.Y: Dover Publications. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-486-46244-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-46244-8 "Special:BookSources/978-0-486-46244-8"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC (identifier)") [853621933](https://search.worldcat.org/oclc/853621933).