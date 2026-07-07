---
title: "Quaternionic projective space"
source: "https://en.wikipedia.org/wiki/Quaternionic_projective_space"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2005-10-01
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), **quaternionic projective space** is an extension of the ideas of [real projective space](https://en.wikipedia.org/wiki/Real_projective_space "Real projective space") and [complex projective space](https://en.wikipedia.org/wiki/Complex_projective_space "Complex projective space"), to the case where coordinates lie in the ring of [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion") ${\displaystyle \mathbb {H} .}$ Quaternionic projective space of dimension *n* is usually denoted by

${\displaystyle \mathbb {HP} ^{n}}$

and is a [closed manifold](https://en.wikipedia.org/wiki/Closed_manifold "Closed manifold") of (real) dimension 4 *n*. It is a [homogeneous space](https://en.wikipedia.org/wiki/Homogeneous_space "Homogeneous space") for a [Lie group](https://en.wikipedia.org/wiki/Lie_group "Lie group") action, in more than one way. The quaternionic projective line ${\displaystyle \mathbb {HP} ^{1}}$ is homeomorphic to the 4-sphere.

## In coordinates

Its direct construction is as a special case of the [projective space over a division algebra](https://en.wikipedia.org/wiki/Projective_space_over_a_division_algebra "Projective space over a division algebra"). The [homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "Homogeneous coordinates") of a point can be written

${\displaystyle [q_{0},q_{1},\ldots ,q_{n}]}$

where the ${\displaystyle q_{i}}$ are quaternions, not all zero. Two sets of coordinates represent the same point if they are 'proportional' by a left multiplication by a non-zero quaternion *c*; that is, we identify all the

${\displaystyle [cq_{0},cq_{1}\ldots ,cq_{n}]}$.

In the language of [group actions](https://en.wikipedia.org/wiki/Group_action_\(mathematics\) "Group action (mathematics)"), ${\displaystyle \mathbb {HP} ^{n}}$ is the [orbit space](https://en.wikipedia.org/wiki/Orbit_space "Orbit space") of ${\displaystyle \mathbb {H} ^{n+1}\setminus \{(0,\ldots ,0)\}}$ by the action of ${\displaystyle \mathbb {H} ^{\times }}$, the multiplicative group of non-zero quaternions. By first projecting onto the unit sphere inside ${\displaystyle \mathbb {H} ^{n+1}}$ one may also regard ${\displaystyle \mathbb {HP} ^{n}}$ as the orbit space of ${\displaystyle S^{4n+3}}$ by the action of ${\displaystyle {\text{Sp}}(1)}$, the group of unit quaternions.[^1] The sphere ${\displaystyle S^{4n+3}}$ then becomes a [principal Sp(1)-bundle](https://en.wikipedia.org/wiki/Principal_bundle "Principal bundle") over ${\displaystyle \mathbb {HP} ^{n}}$:

${\displaystyle \mathrm {Sp} (1)\to S^{4n+3}\to \mathbb {HP} ^{n}.}$

This bundle is sometimes called a (generalized) [Hopf fibration](https://en.wikipedia.org/wiki/Hopf_fibration "Hopf fibration").

There is also a construction of ${\displaystyle \mathbb {HP} ^{n}}$ by means of two-dimensional complex subspaces of ${\displaystyle \mathbb {H} ^{2n}}$, meaning that ${\displaystyle \mathbb {HP} ^{n}}$ lies inside a complex [Grassmannian](https://en.wikipedia.org/wiki/Grassmannian "Grassmannian").

## Topology

### Homotopy theory

The space ${\displaystyle \mathbb {HP} ^{\infty }}$, defined as the union of all finite ${\displaystyle \mathbb {HP} ^{n}}$ 's under inclusion, is the [classifying space](https://en.wikipedia.org/wiki/Classifying_space "Classifying space") *BS* <sup>3</sup>. The homotopy groups of ${\displaystyle \mathbb {HP} ^{\infty }}$ are given by ${\displaystyle \pi _{i}(\mathbb {HP} ^{\infty })=\pi _{i}(BS^{3})\cong \pi _{i-1}(S^{3}).}$ These groups are known to be very complex and in particular they are non-zero for infinitely many values of ${\displaystyle i}$. However, we do have that

${\displaystyle \pi _{i}(\mathbb {HP} ^{\infty })\otimes \mathbb {Q} \cong {\begin{cases}\mathbb {Q} &i=4\\0&i\neq 4\end{cases}}}$

It follows that rationally, i.e. after [localisation of a space](https://en.wikipedia.org/w/index.php?title=Localisation_of_a_space&action=edit&redlink=1 "Localisation of a space (page does not exist)"), ${\displaystyle \mathbb {HP} ^{\infty }}$ is an [Eilenberg–Maclane space](https://en.wikipedia.org/wiki/Eilenberg%E2%80%93Maclane_space "Eilenberg–Maclane space") ${\displaystyle K(\mathbb {Q} ,4)}$. That is ${\displaystyle \mathbb {HP} _{\mathbb {Q} }^{\infty }\simeq K(\mathbb {Z} ,4)_{\mathbb {Q} }.}$ (cf. the example [K(Z,2)](https://en.wikipedia.org/wiki/K\(Z,2\) "K(Z,2)")). See [rational homotopy theory](https://en.wikipedia.org/wiki/Rational_homotopy_theory "Rational homotopy theory").

In general, ${\displaystyle \mathbb {HP} ^{n}}$ has a cell structure with one cell in each dimension which is a multiple of 4, up to ${\displaystyle 4n}$. Accordingly, its cohomology ring is ${\displaystyle \mathbb {Z} [v]/v^{n+1}}$, where ${\displaystyle v}$ is a 4-dimensional generator. This is analogous to complex projective space. It also follows from rational homotopy theory that ${\displaystyle \mathbb {HP} ^{n}}$ has infinite homotopy groups only in dimensions 4 and ${\displaystyle 4n+3}$.

## Differential geometry

${\displaystyle \mathbb {HP} ^{n}}$ carries a natural [Riemannian metric](https://en.wikipedia.org/wiki/Riemannian_metric "Riemannian metric") analogous to the [Fubini-Study metric](https://en.wikipedia.org/wiki/Fubini-Study_metric "Fubini-Study metric") on ${\displaystyle \mathbb {CP} ^{n}}$, with respect to which it is a compact [quaternion-Kähler symmetric space](https://en.wikipedia.org/wiki/Quaternion-K%C3%A4hler_symmetric_space "Quaternion-Kähler symmetric space") with positive curvature.

Quaternionic projective space can be represented as the coset space

${\displaystyle \mathbb {HP} ^{n}=\operatorname {Sp} (n+1)/\operatorname {Sp} (n)\times \operatorname {Sp} (1)}$

where ${\displaystyle \operatorname {Sp} (n)}$ is the compact [symplectic group](https://en.wikipedia.org/wiki/Symplectic_group "Symplectic group").

### Characteristic classes

Since ${\displaystyle \mathbb {HP} ^{1}=S^{4}}$, its tangent bundle is stably trivial. The tangent bundles of the rest have nontrivial [Stiefel–Whitney](https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class "Stiefel–Whitney class") and [Pontryagin classes](https://en.wikipedia.org/wiki/Pontryagin_class "Pontryagin class"). The total classes are given by the following formulas:

${\displaystyle w(\mathbb {HP} ^{n})=(1+u)^{n+1}}$

${\displaystyle p(\mathbb {HP} ^{n})=(1+v)^{2n+2}(1+4v)^{-1}}$

where ${\displaystyle v}$ is the generator of ${\displaystyle H^{4}(\mathbb {HP} ^{n};\mathbb {Z} )}$ and ${\displaystyle u}$ is its reduction mod 2.[^2]

## Special cases

### Quaternionic projective line

The one-dimensional projective space over ${\displaystyle \mathbb {H} }$ is called the "projective line" in generalization of the [complex projective line](https://en.wikipedia.org/wiki/Complex_projective_line "Complex projective line"). For example, it was used (implicitly) in 1947 by P. G. Gormley to extend the [Möbius group](https://en.wikipedia.org/wiki/M%C3%B6bius_group "Möbius group") to the quaternion context with [linear fractional transformations](https://en.wikipedia.org/wiki/Linear_fractional_transformation "Linear fractional transformation"). For the linear fractional transformations of an associative [ring](https://en.wikipedia.org/wiki/Ring_\(mathematics\) "Ring (mathematics)") with 1, see [projective line over a ring](https://en.wikipedia.org/wiki/Projective_line_over_a_ring "Projective line over a ring") and the homography group GL(2,*A*).

From the topological point of view the quaternionic projective line is the 4-sphere, and in fact these are [diffeomorphic](https://en.wikipedia.org/wiki/Diffeomorphic "Diffeomorphic") manifolds. The fibration mentioned previously is from the 7-sphere, and is an example of a [Hopf fibration](https://en.wikipedia.org/wiki/Hopf_fibration "Hopf fibration").

Explicit expressions for coordinates for the 4-sphere can be found in the article on the [Fubini–Study metric](https://en.wikipedia.org/wiki/Fubini%E2%80%93Study_metric "Fubini–Study metric").

### Quaternionic projective plane

The 8-dimensional ${\displaystyle \mathbb {HP} ^{2}}$ has a [circle action](https://en.wikipedia.org/wiki/Circle_action "Circle action"), by the group of complex scalars of absolute value 1 acting on the other side (so on the right, as the convention for the action of *c* above is on the left). Therefore, the [quotient manifold](https://en.wikipedia.org/wiki/Quotient_manifold "Quotient manifold")

${\displaystyle \mathbb {HP} ^{2}/\mathrm {U} (1)}$

may be taken, writing [U(1)](https://en.wikipedia.org/wiki/U\(1\) "U(1)") for the [circle group](https://en.wikipedia.org/wiki/Circle_group "Circle group"). It has been shown that this quotient is the 7- [sphere](https://en.wikipedia.org/wiki/Sphere "Sphere"), a result of [Vladimir Arnold](https://en.wikipedia.org/wiki/Vladimir_Arnold "Vladimir Arnold") from 1996, later rediscovered by [Edward Witten](https://en.wikipedia.org/wiki/Edward_Witten "Edward Witten") and [Michael Atiyah](https://en.wikipedia.org/wiki/Michael_Atiyah "Michael Atiyah").

## References

[^1]: Naber, Gregory L. (2011) \[1997\]. ["Physical and Geometrical Motivation"](https://books.google.com/books?id=MObgBwAAQBAJ&pg=PR1). *Topology, Geometry and Gauge fields*. Texts in Applied Mathematics. Vol. 25. Springer. p. 50. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4419-7254-5\_0](https://doi.org/10.1007%2F978-1-4419-7254-5_0). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4419-7254-5](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4419-7254-5 "Special:BookSources/978-1-4419-7254-5").

[^2]: Szczarba, R.H. (1964). ["On tangent bundles of fibre spaces and quotient spaces"](https://www.maths.ed.ac.uk/~v1ranick/papers/szczarba.pdf) (PDF). *American Journal of Mathematics*. **86** (4): 685–697. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2373152](https://doi.org/10.2307%2F2373152). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2373152](https://www.jstor.org/stable/2373152).