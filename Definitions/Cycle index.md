---
title: "Cycle index"
source: "https://en.wikipedia.org/wiki/Cycle_index"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2006-04-12
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [combinatorial](https://en.wikipedia.org/wiki/Combinatorics "Combinatorics") [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics") a **cycle index** is a [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") in several variables which is structured in such a way that information about how a [group of permutations](https://en.wikipedia.org/wiki/Permutation_group "Permutation group") [acts](https://en.wikipedia.org/wiki/Group_action "Group action") on a [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") can be simply read off from the [coefficients](https://en.wikipedia.org/wiki/Coefficient "Coefficient") and exponents. This compact way of storing information in an [algebraic](https://en.wikipedia.org/wiki/Algebra "Algebra") form is frequently used in [combinatorial enumeration](https://en.wikipedia.org/wiki/Combinatorial_enumeration "Combinatorial enumeration").

Each permutation π of a [finite set](https://en.wikipedia.org/wiki/Finite_set "Finite set") of objects [partitions](https://en.wikipedia.org/wiki/Partition_of_a_set "Partition of a set") that set into [cycles](https://en.wikipedia.org/wiki/Cyclic_permutation "Cyclic permutation"); the **cycle index monomial** of π is a [monomial](https://en.wikipedia.org/wiki/Monomial "Monomial") in variables *a* <sub>1</sub>, *a* <sub>2</sub>, … that describes the [cycle type](https://en.wikipedia.org/wiki/Permutation#Cycle_type "Permutation") of this partition: the exponent of *a* <sub><i>i</i></sub> is the number of cycles of π of size *i*. The **cycle index polynomial** of a permutation group is the average of the cycle index monomials of its elements. The phrase **cycle indicator** is also sometimes used in place of *cycle index*.

Knowing the cycle index polynomial of a permutation group, one can enumerate [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class "Equivalence class") due to the [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)") 's [action](https://en.wikipedia.org/wiki/Group_action "Group action"). This is the main ingredient in the [Pólya enumeration theorem](https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem "Pólya enumeration theorem"). Performing formal algebraic and [differential](https://en.wikipedia.org/wiki/Derivative "Derivative") operations on these polynomials and then interpreting the results combinatorially lies at the core of [species theory](https://en.wikipedia.org/wiki/Combinatorial_species "Combinatorial species").

## Permutation groups and group actions

A [bijective](https://en.wikipedia.org/wiki/Bijective "Bijective") map from a set *X* onto itself is called a permutation of *X*, and the set of all permutations of *X* forms a group under the [composition](https://en.wikipedia.org/wiki/Function_composition "Function composition") of mappings, called the [symmetric group](https://en.wikipedia.org/wiki/Symmetric_group "Symmetric group") of *X*, and denoted Sym(*X*  ). Every [subgroup](https://en.wikipedia.org/wiki/Subgroup "Subgroup") of Sym(*X*  ) is called a [permutation group](https://en.wikipedia.org/wiki/Permutation_group "Permutation group") of *degree* | *X*  |.[^1] Let *G* be an [abstract group](https://en.wikipedia.org/wiki/Abstract_group "Abstract group") with a [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism "Group homomorphism") φ from *G* into Sym(*X*  ). The [image](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)"), φ(*G*), is a permutation group. The group homomorphism can be thought of as a means for permitting the group *G* to "act" on the set *X* (using the permutations associated with the elements of *G*). Such a group homomorphism is formally called a *[permutation representation](https://en.wikipedia.org/wiki/Permutation_representation "Permutation representation")* of *G*. A given group can have many different permutation representations, corresponding to different actions.[^2]

Suppose that group *G* acts on set *X* (that is, a group action exists). In combinatorial applications the interest is in the set *X*; for instance, counting things in *X* and knowing what structures might be left invariant by *G*. Little is lost by working with permutation groups in such a setting, so in these applications, when a group is considered, it is a permutation representation of the group which will be worked with, and thus, a group action must be specified. Algebraists, on the other hand, are more interested in the groups themselves and would be more concerned with the [kernels](https://en.wikipedia.org/wiki/Kernel_\(algebra\) "Kernel (algebra)") of the group actions, which measure how much is lost in passing from the group to its permutation representation.[^3]

## Disjoint cycle representation of permutations

Finite permutations are most often represented as group actions on the set *X* = {1,2,..., *n* }. A permutation in this setting can be represented by a two-line notation. Thus,

${\displaystyle \left({\begin{matrix}1&2&3&4&5\\2&3&4&5&1\end{matrix}}\right)}$

corresponds to a bijection on *X* = {1, 2, 3, 4, 5} which sends 1 ↦ 2, 2 ↦ 3, 3 ↦ 4, 4 ↦ 5 and 5 ↦ 1. This can be read off from the columns of the notation. When the top row is understood to be the elements of *X* in an appropriate order, only the second row need be written. In this one-line notation, our example would be \[2 3 4 5 1\].[^4] This example is known as a *[cyclic permutation](https://en.wikipedia.org/wiki/Cyclic_permutation "Cyclic permutation")* because it "cycles" the numbers around, and a third notation for it would be (1 2 3 4 5). This *cycle notation* is to be read as: each element is sent to the element on its right, but the last element is sent to the first one (it "cycles" to the beginning). With cycle notation, it does not matter where a cycle starts, so (1 2 3 4 5) and (3 4 5 1 2) and (5 1 2 3 4) all represent the same permutation. The *length of a cycle* is the number of elements in the cycle.

Not all permutations are cyclic permutations, but every permutation can be written as a product [^5] of disjoint (having no common element) cycles in essentially one way.[^6] As a permutation may have *[fixed points](https://en.wikipedia.org/wiki/Fixed_point_\(mathematics\) "Fixed point (mathematics)")* (elements that are unchanged by the permutation), these will be represented by cycles of length one. For example:[^7]

${\displaystyle \left({\begin{matrix}1&2&3&4&5&6\\2&1&3&5&6&4\end{matrix}}\right)=(12)(3)(456).}$

This permutation is the product of three cycles, one of length two, one of length three, and a fixed point. The elements in these cycles are disjoint subsets of *X* and form a partition of *X*.

The cycle structure of a permutation can be coded as an algebraic monomial in several ([dummy](https://en.wikipedia.org/wiki/Free_variables_and_bound_variables "Free variables and bound variables")) variables in the following way: a variable is needed for each distinct cycle length of the cycles that appear in the cycle decomposition of the permutation. In the previous example there were three different cycle lengths, so we will use three variables, *a* <sub>1</sub>, *a* <sub>2</sub> and *a* <sub>3</sub> (in general, use the variable *a* <sub><i>k</i></sub> to correspond to length *k* cycles). The variable *a* <sub><i>i</i></sub> will be raised to the *j* <sub><i>i</i></sub>  (*g*) power where *j* <sub><i>i</i></sub>  (*g*) is the number of cycles of length *i* in the cycle decomposition of permutation *g*. We can then associate the *cycle index monomial*

${\displaystyle \prod _{k=1}^{n}a_{k}^{j_{k}(g)}}$

to the permutation *g*. The cycle index monomial of our example would be *a* <sub>1</sub> *a* <sub>2</sub> *a* <sub>3</sub>, while the cycle index monomial of the permutation (1 2)(3 4)(5)(6 7 8 9)(10 11 12 13) would be *a* <sub>1</sub> *a* <sub>2</sub> <sup>2</sup> *a* <sub>4</sub> <sup>2</sup>.

## Definition

The **cycle index** of a [permutation group](https://en.wikipedia.org/wiki/Permutation_group "Permutation group") *G* is the average of the cycle index monomials of all the permutations *g* in *G*.

More formally, let *G* be a permutation group of [order](https://en.wikipedia.org/wiki/Order_of_a_group "Order of a group") *m* and degree *n*. Every permutation *g* in *G* has a unique decomposition into disjoint cycles, say *c* <sub>1</sub> *c* <sub>2</sub> *c* <sub>3</sub>.... Let the length of a cycle *c* be denoted by | *c*  |.

Now let *j* <sub><i>k</i></sub> (*g*) be the number of cycles of *g* of length *k*, where

${\displaystyle 0\leq j_{k}(g)\leq \lfloor n/k\rfloor {\mbox{ and }}\sum _{k=1}^{n}k\,j_{k}(g)=n.}$

We associate to *g* the monomial

${\displaystyle \prod _{c\in g}a_{|c|}=\prod _{k=1}^{n}a_{k}^{j_{k}(g)}}$

in the variables *a* <sub>1</sub>, *a* <sub>2</sub>,..., *a* <sub><i>n</i></sub>.

Then the cycle index *Z* (*G*) of *G* is given by

${\displaystyle Z(G)={\frac {1}{|G|}}\sum _{g\in G}\prod _{k=1}^{n}a_{k}^{j_{k}(g)}.}$

## Example

Consider the group *G* of [rotational symmetries](https://en.wikipedia.org/wiki/Rotational_symmetries "Rotational symmetries") of a [square](https://en.wikipedia.org/wiki/Square "Square") in the [Euclidean plane](https://en.wikipedia.org/wiki/Euclidean_plane "Euclidean plane"). Its elements are completely determined by the images of just the corners of the square. By labeling these corners 1, 2, 3 and 4 (consecutively going clockwise, say) we can represent the elements of *G* as permutations of the set *X* = {1,2,3,4}.[^8] The permutation representation of *G* consists of the four permutations (1 4 3 2), (1 3)(2 4), (1 2 3 4) and e = (1)(2)(3)(4) which represent the counter-clockwise [rotations](https://en.wikipedia.org/wiki/Rotation "Rotation") by 90°, 180°, 270° and 360° respectively. Notice that the [identity](https://en.wikipedia.org/wiki/Identity_map "Identity map") permutation e is the only permutation with fixed points in this representation of *G*. As an abstract group, *G* is known as the [cyclic group](https://en.wikipedia.org/wiki/Cyclic_group "Cyclic group") *C* <sub>4</sub>, and this permutation representation of it is its *regular representation*. The cycle index monomials are *a* <sub>4</sub>, *a* <sub>2</sub> <sup>2</sup>, *a* <sub>4</sub>, and *a* <sub>1</sub> <sup>4</sup> respectively. Thus, the cycle index of this permutation group is:

${\displaystyle Z(C_{4})={\frac {1}{4}}\left(a_{1}^{4}+a_{2}^{2}+2a_{4}\right).}$

The group *C* <sub>4</sub> also acts on the unordered pairs of elements of *X* in a natural way. Any permutation *g* would send { *x*,*y* } → { *x* <sup><i>g</i></sup>, *y* <sup><i>g</i></sup> } (where *x* <sup><i>g</i></sup> is the image of the element *x* under the permutation *g*).[^9] The set *X* is now { *A*, *B*, *C*, *D*, *E*, *F* } where *A* = {1,2}, *B* = {2,3}, *C* = {3,4}, *D* = {1,4}, *E* = {1,3} and *F* = {2,4}. These elements can be thought of as the sides and diagonals of the square or, in a completely different setting, as the edges of the [complete graph](https://en.wikipedia.org/wiki/Complete_graph "Complete graph") *K* <sub>4</sub>. Acting on this new set, the four group elements are now represented by (*A* *D* *C* *B*)(*E* *F*), (*A C*)(*B D*)(*E*)(*F*), (*A B C D*)(*E F*) and e = (*A*)(*B*)(*C*)(*D*)(*E*)(*F*), and the cycle index of this action is:

${\displaystyle Z(C_{4})={\frac {1}{4}}\left(a_{1}^{6}+a_{1}^{2}a_{2}^{2}+2a_{2}a_{4}\right).}$

The group *C* <sub>4</sub> can also act on the ordered pairs of elements of *X* in the same natural way. Any permutation *g* would send (*x*,*y*) → (*x* <sup><i>g</i></sup>, *y* <sup><i>g</i></sup>) (in this case we would also have ordered pairs of the form (*x*, *x*)). The elements of *X* could be thought of as the arcs of the [complete digraph](https://en.wikipedia.org/wiki/Complete_digraph "Complete digraph") *D* <sub>4</sub> (with [loops](https://en.wikipedia.org/wiki/Loop_\(graph_theory\) "Loop (graph theory)") at each vertex). The cycle index in this case would be:

${\displaystyle Z(C_{4})={\frac {1}{4}}\left(a_{1}^{16}+a_{2}^{8}+2a_{4}^{4}\right).}$

## Types of actions

As the above example shows, the cycle index depends on the group action and not on the abstract group. Since there are many permutation representations of an abstract group, it is useful to have some terminology to distinguish them.

When an abstract group is defined in terms of permutations, it is a permutation group and the group action is the [identity](https://en.wikipedia.org/wiki/Identity_map "Identity map") homomorphism. This is referred to as the *natural action*.

The symmetric group *S* <sub>3</sub> in its natural action has the elements [^10]

${\displaystyle S_{3}=\{e,(23),(12),(123),(132),(13)\}}$

and so, its cycle index is:

${\displaystyle Z(S_{3})={\frac {1}{6}}\left(a_{1}^{3}+3a_{1}a_{2}+2a_{3}\right).}$

A permutation group *G* on the set *X* is *transitive* if for every pair of elements *x* and *y* in *X* there is at least one *g* in *G* such that *y* = *x* <sup><i>g</i></sup>. A transitive permutation group is *regular* (or sometimes referred to as *sharply transitive*) if the only permutation in the group that has fixed points is the identity permutation.

A [finite](https://en.wikipedia.org/wiki/Finite_group "Finite group") transitive permutation group *G* on the set *X* is regular [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") | *G* | = | *X*  |.[^11] [Cayley's theorem](https://en.wikipedia.org/wiki/Cayley%27s_theorem "Cayley's theorem") states that every abstract group has a regular permutation representation given by the group acting on itself (as a set) by (right) multiplication. This is called the *regular representation* of the group.

The cyclic group *C* <sub>6</sub> in its [regular representation](https://en.wikipedia.org/wiki/Regular_representation "Regular representation") contains the six permutations (one-line form of the permutation is given first):

\[1 2 3 4 5 6\] = (1)(2)(3)(4)(5)(6)

\[2 3 4 5 6 1\] = (1 2 3 4 5 6)

\[3 4 5 6 1 2\] = (1 3 5)(2 4 6)

\[4 5 6 1 2 3\] = (1 4)(2 5)(3 6)

\[5 6 1 2 3 4\] = (1 5 3)(2 6 4)

\[6 1 2 3 4 5\] = (1 6 5 4 3 2).

Thus its cycle index is:

${\displaystyle Z(C_{6})={\frac {1}{6}}\left(a_{1}^{6}+a_{2}^{3}+2a_{3}^{2}+2a_{6}\right).}$

Often, when an author does not wish to use the group action terminology, the permutation group involved is given a name which implies what the action is. The following three examples illustrate this point.

### The cycle index of the edge permutation group of the complete graph on three vertices

We will identify the complete graph *K* <sub>3</sub> with an [equilateral triangle](https://en.wikipedia.org/wiki/Equilateral_triangle "Equilateral triangle") in the Euclidean plane. This permits us to use geometric language to describe the permutations involved as [symmetries](https://en.wikipedia.org/wiki/Symmetry "Symmetry") of the triangle. Every permutation in the group *S* <sub>3</sub> of *vertex permutations* (*S* <sub>3</sub> in its natural action, given above) induces an edge permutation. These are the permutations:

- The identity: No vertices are permuted, and no edges; the contribution is ${\displaystyle a_{1}^{3}.}$
- Three [reflections](https://en.wikipedia.org/wiki/Reflection_\(mathematics\) "Reflection (mathematics)") in an axis passing through a vertex and the midpoint of the opposite edge: These fix one edge (the one not incident on the vertex) and exchange the remaining two; the contribution is ${\displaystyle 3a_{1}a_{2}.}$
- Two rotations, one clockwise, the other counterclockwise: These create a cycle of three edges; the contribution is ${\displaystyle 2a_{3}.}$

The cycle index of the group *G* of edge permutations induced by vertex permutations from *S* <sub>3</sub> is

${\displaystyle Z(G)={\frac {1}{6}}\left(a_{1}^{3}+3a_{1}a_{2}+2a_{3}\right).}$

It happens that the complete graph *K* <sub>3</sub> is [isomorphic](https://en.wikipedia.org/wiki/Isomorphic "Isomorphic") to its own [line graph](https://en.wikipedia.org/wiki/Line_graph "Line graph") (vertex-edge dual) and hence the edge permutation group induced by the vertex permutation group is the same as the vertex permutation group, namely *S* <sub>3</sub> and the cycle index is *Z* (*S* <sub>3</sub>). This is not the case for complete graphs on more than three vertices, since these have strictly more edges (${\displaystyle {\binom {n}{2}}}$) than vertices (${\displaystyle n}$).

### The cycle index of the edge permutation group of the complete graph on four vertices

This is entirely analogous to the three-vertex case. These are the vertex permutations (*S* <sub>4</sub> in its natural action) and the edge permutations (*S* <sub>4</sub> acting on unordered pairs) that they induce:

- The identity: This permutation maps all vertices (and hence, edges) to themselves and the contribution is ${\displaystyle a_{1}^{6}.}$
- Six permutations that exchange two vertices: These permutations preserve the edge that connects the two vertices as well as the edge that connects the two vertices not exchanged. The remaining edges form two two-cycles and the contribution is ${\displaystyle 6a_{1}^{2}a_{2}^{2}.}$
- Eight permutations that fix one vertex and produce a three-cycle for the three vertices not fixed: These permutations create two three-cycles of edges, one containing those not incident on the vertex, and another one containing those incident on the vertex; the contribution is ${\displaystyle 8a_{3}^{2}.}$
- Three permutations that exchange two vertex pairs at the same time: These permutations preserve the two edges that connect the two pairs. The remaining edges form two two-cycles and the contribution is ${\displaystyle 3a_{1}^{2}a_{2}^{2}.}$
- Six permutations that cycle the vertices in a four-cycle: These permutations create a four-cycle of edges (those that lie on the cycle) and exchange the remaining two edges; the contribution is ${\displaystyle 6a_{2}a_{4}.}$

We may visualize the types of permutations geometrically as [symmetries of a regular tetrahedron](https://en.wikipedia.org/wiki/Tetrahedral_symmetry "Tetrahedral symmetry"). This yields the following description of the permutation types.

- The identity.
- Reflection in the plane that contains one edge and the midpoint of the edge opposing it.
- Rotation by 120 degrees about the axis passing through a vertex and the midpoint of the opposite face.
- Rotation by 180 degrees about the axis connecting the midpoints of two opposite edges.
- Six [rotoreflections](https://en.wikipedia.org/wiki/Rotoreflection "Rotoreflection") by 90 degrees.

The cycle index of the edge permutation group *G* of *K* <sub>4</sub> is:

${\displaystyle Z(G)={\frac {1}{24}}\left(a_{1}^{6}+9a_{1}^{2}a_{2}^{2}+8a_{3}^{2}+6a_{2}a_{4}\right).}$

### The cycle index of the face permutations of a cube

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Face_colored_cube.png/250px-Face_colored_cube.png)

Cube with colored faces

Consider an ordinary [cube](https://en.wikipedia.org/wiki/Cube "Cube") in three-space and its group of symmetries, call it *C*. It permutes the six faces of the cube. (We could also consider edge permutations or vertex permutations.) There are twenty-four symmetries.

- The identity:

There is one such permutation and its contribution is ${\displaystyle a_{1}^{6}.}$

- Six 90-degree face rotations:

We rotate about the axis passing through the centers of the face and the face opposing it. This will fix the face and the face opposing it and create a four-cycle of the faces [parallel](https://en.wikipedia.org/wiki/Parallel_\(geometry\) "Parallel (geometry)") to the axis of rotation. The contribution is ${\displaystyle 6a_{1}^{2}a_{4}.}$

- Three 180-degree face rotations:

We rotate about the same axis as in the previous case, but now there is no four cycle of the faces parallel to the axis, but rather two two-cycles. The contribution is ${\displaystyle 3a_{1}^{2}a_{2}^{2}.}$

- Eight 120-degree vertex rotations:

This time we rotate about the axis passing through two opposite vertices (the endpoints of a [main diagonal](https://en.wikipedia.org/wiki/Main_diagonal "Main diagonal")). This creates two three-cycles of faces (the faces incident on the same vertex form a cycle). The contribution is ${\displaystyle 8a_{3}^{2}.}$

- Six 180-degree edge rotations:

These edge rotations rotate about the axis that passes through the midpoints of opposite edges not incident on the same face and parallel to each other and exchanges the two faces that are incident on the first edge, the two faces incident on the second edge, and the two faces that share two vertices but no edge with the two edges, i.e. there are three two-cycles and the contribution is ${\displaystyle 6a_{2}^{3}.}$

The conclusion is that the cycle index of the group *C* is

${\displaystyle Z(C)={\frac {1}{24}}\left(a_{1}^{6}+6a_{1}^{2}a_{4}+3a_{1}^{2}a_{2}^{2}+8a_{3}^{2}+6a_{2}^{3}\right).}$

## Cycle indices of some permutation groups

### Identity group En

This group contains one permutation that fixes every element (this must be a natural action).

${\displaystyle Z(E_{n})=a_{1}^{n}.}$

### Cyclic group Cn

A [cyclic group](https://en.wikipedia.org/wiki/Cyclic_group "Cyclic group"), *C* <sub><i>n</i></sub> is the group of rotations of a [regular *n* -gon](https://en.wikipedia.org/wiki/Regular_polygon "Regular polygon"), that is, *n* elements equally spaced around a circle. This group has φ(*d*  ) elements of [order](https://en.wikipedia.org/wiki/Order_\(group_theory\) "Order (group theory)") *d* for each [divisor](https://en.wikipedia.org/wiki/Divisor "Divisor") *d* of *n*, where φ(*d*  ) is the [Euler φ-function](https://en.wikipedia.org/wiki/Euler%27s_totient_function "Euler's totient function"), giving the number of natural numbers less than *d* which are [relatively prime](https://en.wikipedia.org/wiki/Relatively_prime "Relatively prime") to *d*. In the regular representation of *C* <sub><i>n</i></sub>, a permutation of order *d* has *n* / *d* cycles of length *d*, thus:[^12]

${\displaystyle Z(C_{n})={\frac {1}{n}}\sum _{d|n}\varphi (d)a_{d}^{n/d}.}$

### Dihedral group Dn

The [dihedral group](https://en.wikipedia.org/wiki/Dihedral_group "Dihedral group") is like the [cyclic group](https://en.wikipedia.org/wiki/Cyclic_group "Cyclic group"), but also includes reflections. In its natural action,

${\displaystyle Z(D_{n})={\frac {1}{2}}Z(C_{n})+{\begin{cases}{\frac {1}{2}}a_{1}a_{2}^{(n-1)/2},&n{\mbox{ odd, }}\\{\frac {1}{4}}\left(a_{1}^{2}a_{2}^{(n-2)/2}+a_{2}^{n/2}\right),&n{\mbox{ even.}}\end{cases}}}$

### Alternating group An

The cycle index of the [alternating group](https://en.wikipedia.org/wiki/Alternating_group "Alternating group") in its natural action as a permutation group is

${\displaystyle Z(A_{n})=\sum _{j_{1}+2j_{2}+3j_{3}+\cdots +nj_{n}=n}{\frac {1+(-1)^{j_{2}+j_{4}+\cdots }}{\prod _{k=1}^{n}k^{j_{k}}j_{k}!}}\prod _{k=1}^{n}a_{k}^{j_{k}}.}$

The numerator is 2 for the [even permutations](https://en.wikipedia.org/wiki/Even_permutation "Even permutation"), and 0 for the [odd permutations](https://en.wikipedia.org/wiki/Odd_permutation "Odd permutation"). The 2 is needed because ${\displaystyle {\frac {1}{|A_{n}|}}={\frac {2}{n!}}}$.

### Symmetric group Sn

The cycle index of the [symmetric group](https://en.wikipedia.org/wiki/Symmetric_group "Symmetric group") *S* <sub><i>n</i></sub> in its natural action is given by the formula:

${\displaystyle Z(S_{n})=\sum _{j_{1}+2j_{2}+3j_{3}+\cdots +nj_{n}=n}{\frac {1}{\prod _{k=1}^{n}k^{j_{k}}j_{k}!}}\prod _{k=1}^{n}a_{k}^{j_{k}}}$

that can be also stated in terms of complete [Bell polynomials](https://en.wikipedia.org/wiki/Bell_polynomial "Bell polynomial"):

${\displaystyle Z(S_{n})={\frac {B_{n}(0!\,a_{1},1!\,a_{2},\dots ,(n-1)!\,a_{n})}{n!}}.}$

This formula is obtained by counting how many times a given permutation shape can occur. There are three steps: first partition the set of *n* labels into subsets, where there are ${\displaystyle j_{k}}$ subsets of size *k*. Every such subset generates ${\displaystyle k!/k}$ cycles of length *k*. But we do not distinguish between cycles of the same size, i.e. they are permuted by ${\displaystyle S_{j_{k}}}$. This yields

${\displaystyle {\frac {n!}{\prod _{k=1}^{n}(k!)^{j_{k}}}}\prod _{k=1}^{n}\left({\frac {k!}{k}}\right)^{j_{k}}\prod _{k=1}^{n}{\frac {1}{j_{k}!}}={\frac {n!}{\prod _{k=1}^{n}k^{j_{k}}j_{k}!}}.}$

The formula may be further simplified if we sum up cycle indices over every ${\displaystyle n}$, while using an extra variable ${\displaystyle y}$ to keep track of the total size of the cycles:

${\displaystyle \sum \limits _{n\geq 1}y^{n}Z(S_{n})=\sum \limits _{n\geq 1}\sum _{j_{1}+2j_{2}+3j_{3}+\cdots +nj_{n}=n}\prod _{k=1}^{n}{\frac {a_{k}^{j_{k}}y^{kj_{k}}}{k^{j_{k}}j_{k}!}}=\prod \limits _{k\geq 1}\sum \limits _{j_{k}\geq 0}{\frac {(a_{k}y^{k})^{j_{k}}}{k^{j_{k}}j_{k}!}}=\prod \limits _{k\geq 1}\exp \left({\frac {a_{k}y^{k}}{k}}\right),}$

thus giving a simplified form for the cycle index of ${\displaystyle S_{n}}$:

${\displaystyle {\begin{aligned}Z(S_{n})&=[y^{n}]\prod \limits _{k\geq 1}\exp \left({\frac {a_{k}y^{k}}{k}}\right)\\&=[y^{n}]\exp \left(\sum \limits _{k\geq 1}{\frac {a_{k}y^{k}}{k}}\right).\end{aligned}}}$

There is a useful recursive formula for the cycle index of the symmetric group. Set ${\displaystyle Z(S_{0})=1}$ and consider the size *l* of the cycle that contains *n*, where ${\displaystyle {\begin{matrix}1\leq l\leq n.\end{matrix}}}$ There are ${\textstyle {n-1 \choose l-1}}$ ways to choose the remaining ${\displaystyle l-1}$ elements of the cycle and every such choice generates ${\displaystyle {\begin{matrix}{\frac {l!}{l}}=(l-1)!\end{matrix}}}$ different cycles.

This yields the recurrence

${\displaystyle Z(S_{n})={\frac {1}{n!}}\sum _{g\in S_{n}}\prod _{k=1}^{n}a_{k}^{j_{k}(g)}={\frac {1}{n!}}\sum _{l=1}^{n}{n-1 \choose l-1}\;(l-1)!\;a_{l}\;(n-l)!\;Z(S_{n-l})}$

or

${\displaystyle Z(S_{n})={\frac {1}{n}}\sum _{l=1}^{n}a_{l}\;Z(S_{n-l}).}$

## Applications

Throughout this section we will modify the notation for cycle indices slightly by explicitly including the names of the variables. Thus, for the permutation group *G* we will now write:

${\displaystyle Z(G)=Z(G;a_{1},a_{2},\ldots ,a_{n}).}$

Let *G* be a group acting on the set *X*. *G* also induces an action on the *k* -subsets of *X* and on the *k* -tuples of distinct elements of *X* (see [#Example](#Example) for the case *k* = 2), for 1 ≤ *k* ≤ *n*. Let *f* <sub><i>k</i></sub> and *F* <sub><i>k</i></sub> denote the number of [orbits](https://en.wikipedia.org/wiki/Orbit_\(group_theory\) "Orbit (group theory)") of *G* in these actions respectively. By convention we set *f* <sub>0</sub> = *F* <sub>0</sub> = 1. We have:[^13]

a) The [ordinary generating function](https://en.wikipedia.org/wiki/Ordinary_generating_function "Ordinary generating function") for *f* <sub><i>k</i></sub> is given by:

${\displaystyle \sum _{k=0}^{n}f_{k}t^{k}=Z(G;1+t,1+t^{2},\ldots ,1+t^{n}),}$ and

b) The [exponential generating function](https://en.wikipedia.org/wiki/Exponential_generating_function "Exponential generating function") for *F* <sub><i>k</i></sub> is given by:

${\displaystyle \sum _{k=0}^{n}F_{k}t^{k}/k!=Z(G;1+t,1,1,\ldots ,1).}$

Let *G* be a group acting on the set *X* and *h* a function from *X* to *Y*. For any *g* in *G*, *h* (*x* <sup><i>g</i></sup>) is also a function from *X* to *Y*. Thus, *G* induces an action on the set *Y* <sup><i>X</i></sup> of all functions from *X* to *Y*. The number of orbits of this action is Z(*G*; *b*, *b*,..., *b*) where *b* = | *Y*  |.[^14]

This result follows from the [orbit counting lemma](https://en.wikipedia.org/wiki/Burnside%27s_lemma "Burnside's lemma") (also known as the Not Burnside's lemma, but traditionally called Burnside's lemma) and the weighted version of the result is [Pólya's enumeration theorem](https://en.wikipedia.org/wiki/P%C3%B3lya%27s_enumeration_theorem "Pólya's enumeration theorem").

The cycle index is a polynomial in several variables and the above results show that certain evaluations of this polynomial give combinatorially significant results. As polynomials they may also be formally added, subtracted, differentiated and [integrated](https://en.wikipedia.org/wiki/Integral "Integral"). The area of [symbolic combinatorics](https://en.wikipedia.org/wiki/Symbolic_combinatorics "Symbolic combinatorics") provides combinatorial interpretations of the results of these formal operations.

The question of what the cycle structure of a random permutation looks like is an important question in the [analysis of algorithms](https://en.wikipedia.org/wiki/Analysis_of_algorithms "Analysis of algorithms"). An overview of the most important results may be found at [random permutation statistics](https://en.wikipedia.org/wiki/Random_permutation_statistics "Random permutation statistics").

## Notes

## References

- Brualdi, Richard A. (2010), "14. Pólya Counting", *Introductory Combinatorics* (5th ed.), Upper Saddle River, NJ: Prentice Hall, pp. 541–575, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-13-602040-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-602040-0 "Special:BookSources/978-0-13-602040-0")
- Cameron, Peter J. (1994), "15. Enumeration under group action", *Combinatorics:Topics, Techniques, Algorithms*, Cambridge: Cambridge University Press, pp. 245–256, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-45761-0](https://en.wikipedia.org/wiki/Special:BookSources/0-521-45761-0 "Special:BookSources/0-521-45761-0")
- Dixon, John D.; Mortimer, Brian (1996), [*Permutation Groups*](https://archive.org/details/permutationgroup0000dixo), New York: Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-94599-7](https://en.wikipedia.org/wiki/Special:BookSources/0-387-94599-7 "Special:BookSources/0-387-94599-7")
- Roberts, Fred S.; Tesman, Barry (2009), "8.5 The Cycle Index", *Applied Combinatorics* (2nd ed.), Boca Raton: CRC Press, pp. 472–479, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4200-9982-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4200-9982-9 "Special:BookSources/978-1-4200-9982-9")
- [Tucker, Alan](https://en.wikipedia.org/wiki/Alan_Tucker "Alan Tucker") (1995), "9.3 The Cycle Index", *Applied Combinatorics* (3rd ed.), New York: Wiley, pp. 365–371, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-471-59504-7](https://en.wikipedia.org/wiki/Special:BookSources/0-471-59504-7 "Special:BookSources/0-471-59504-7")
- van Lint, J.H.; Wilson, R.M. (1992), "35.Pólya theory of counting", *A Course in Combinatorics*, Cambridge: Cambridge University Press, pp. 461–474, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-42260-4](https://en.wikipedia.org/wiki/Special:BookSources/0-521-42260-4 "Special:BookSources/0-521-42260-4")

## External links

- Marko Riedel, *[Pólya's enumeration theorem and the symbolic method](https://combinatorialsums.risc.jku.at/papers/collier.pdf)*
- Marko Riedel, *[Cycle indices of the set / multiset operator and the exponential formula](https://combinatorialsums.risc.jku.at/papers/exponential.pdf)*
- Harald Fripertinger (1997). ["Cycle indices of linear, affine and projective groups"](https://doi.org/10.1016%2FS0024-3795%2896%2900530-7). *Linear Algebra and Its Applications*. **263**: 133–156. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S0024-3795(96)00530-7](https://doi.org/10.1016%2FS0024-3795%2896%2900530-7).
- Harald Fripertinger (1992). ["Enumeration in Musical Theory"](https://imsc.uni-graz.at/fripertinger/musical_theory.html). *Beiträge zur Elektronischen Musik*. **1**.

[^1]: [Dixon & Mortimer 1996](#CITEREFDixonMortimer1996), pg. 2, section 1.2 Symmetric groups

[^2]: [Cameron 1994](#CITEREFCameron1994), pp. 227–228

[^3]: [Cameron 1994](#CITEREFCameron1994), pg. 231, section 14.3

[^4]: This notational style is frequently found in the computer science literature.

[^5]: Cyclic permutations are functions and the term *product* really means *composition* of these functions.

[^6]: Up to the different ways one can write a cycle and the fact that disjoint cycles commute so they can be written in any order.

[^7]: [Roberts & Tesman 2009](#CITEREFRobertsTesman2009), pg. 473

[^8]: Technically we are using the notion of equivalence of group actions, replacing *G* acting on the corners of the square by the permutation representation of *G* acting on *X*. For the purposes of exposition, it is better to slide over these details.

[^9]: This notation is common amongst geometers and combinatorialists. It is used instead of the more common g(x) for traditional reasons.

[^10]: There is a convention to not write the fixed points in the cycle notation for a permutation, but these must be represented in the cycle index.

[^11]: [Dixon & Mortimer 1996](#CITEREFDixonMortimer1996), pg. 9, Corollary 1.4A(iii)

[^12]: [van Lint & Wilson 1992](#CITEREFvan_LintWilson1992), pg. 464, Example 35.1

[^13]: [Cameron 1994](#CITEREFCameron1994), pg. 248, Proposition 15.3.1

[^14]: [van Lint & Wilson 1992](#CITEREFvan_LintWilson1992), pg. 463, Theorem 35.1