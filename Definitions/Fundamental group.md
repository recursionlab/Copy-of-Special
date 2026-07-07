---
title: Fundamental group
source: https://en.wikipedia.org/wiki/Fundamental_group
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2001-08-22
created: 2026-04-10
description:
tags:
  - clippings
  - ΦΩCore
---
In the [mathematical](https://en.wikipedia.org/wiki/Mathematics "Mathematics") field of [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology"), the **fundamental group** of a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") is the [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)") of the [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class "Equivalence class") under [homotopy](https://en.wikipedia.org/wiki/Homotopy "Homotopy") of the [loops](https://en.wikipedia.org/wiki/Loop_\(topology\) "Loop (topology)") contained in the space. It records information about the basic shape, or holes, of the topological space. The fundamental group is the first and simplest [homotopy group](https://en.wikipedia.org/wiki/Homotopy_group "Homotopy group"). The fundamental group is a [homotopy invariant](https://en.wikipedia.org/wiki/Homotopy_invariant "Homotopy invariant") —topological spaces that are [homotopy equivalent](https://en.wikipedia.org/wiki/Homotopy_equivalent "Homotopy equivalent") (or the stronger case of [homeomorphic](https://en.wikipedia.org/wiki/Homeomorphic "Homeomorphic")) have [isomorphic](https://en.wikipedia.org/wiki/Group_isomorphism "Group isomorphism") fundamental groups. The fundamental group of a topological space ${\displaystyle X}$ is denoted by ${\displaystyle \pi _{1}(X)}$.

## Intuition

Start with a space (for example, a [surface](https://en.wikipedia.org/wiki/Surface_\(mathematics\) "Surface (mathematics)")), and some point in it, and all the loops both starting and ending at this point— [paths](https://en.wikipedia.org/wiki/Path_\(topology\) "Path (topology)") that start at this point, wander around and eventually return to the starting point. Two loops can be combined in an obvious way: travel along the first loop, then along the second. Two loops are considered equivalent if one can be deformed into the other without breaking. The set of all such loops with this method of combining and this equivalence between them is the fundamental group for that particular space.

## History

[Henri Poincaré](https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9 "Henri Poincaré") defined the fundamental group in 1895 in his paper " [Analysis situs](https://en.wikipedia.org/wiki/Analysis_Situs_\(paper\) "Analysis Situs (paper)") ".[^1] The concept emerged in the theory of [Riemann surfaces](https://en.wikipedia.org/wiki/Riemann_surface "Riemann surface"), in the work of [Bernhard Riemann](https://en.wikipedia.org/wiki/Bernhard_Riemann "Bernhard Riemann"), Poincaré, and [Felix Klein](https://en.wikipedia.org/wiki/Felix_Klein "Felix Klein"). It describes the [monodromy](https://en.wikipedia.org/wiki/Monodromy "Monodromy") properties of [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number") -valued functions, as well as providing a complete topological [classification of closed surfaces](https://en.wikipedia.org/wiki/Classification_of_surfaces "Classification of surfaces").

## Definition

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Double_torus_illustration.png/250px-Double_torus_illustration.png)

Throughout this article, ${\displaystyle X}$ is a topological space. A typical example is a surface such as the one depicted at the right. Moreover, ${\displaystyle x_{0}}$ is a point in ${\displaystyle X}$ called the *base-point*. (As is explained below, its role is rather auxiliary.) The idea of the definition of the homotopy group is to measure how many (broadly speaking) curves on ${\displaystyle X}$ can be deformed into each other. The precise definition depends on the notion of the homotopy of loops, which is explained first.

### Homotopy of loops

Given a topological space ${\displaystyle X}$, a *[loop](https://en.wikipedia.org/wiki/Loop_\(topology\) "Loop (topology)") based at ${\displaystyle x_{0}}$* is defined to be a [continuous function](https://en.wikipedia.org/wiki/Continuous_function_\(topology\) "Continuous function (topology)") (also known as a continuous map)

${\displaystyle \gamma \colon [0,1]\to X}$

such that the starting point ${\displaystyle \gamma (0)}$ and the end point ${\displaystyle \gamma (1)}$ are both equal to ${\displaystyle x_{0}}$.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Homotopy_of_pointed_circle_maps.png/250px-Homotopy_of_pointed_circle_maps.png)

Homotopy of loops. Black loops are interpolation loops at time {\\displaystyle t}.

A *[homotopy](https://en.wikipedia.org/wiki/Homotopy "Homotopy")* is a continuous interpolation between two loops. More precisely, a homotopy between two loops ${\displaystyle \gamma ,\gamma '\colon [0,1]\to X}$ (based at the same point ${\displaystyle x_{0}}$) is a continuous map 
$$
{\displaystyle h\colon [0,1]\times [0,1]\to X,}
$$
 such that

- ${\displaystyle h(0,t)=x_{0}}$ for all ${\displaystyle t\in [0,1]}$, that is, the starting point of the homotopy is ${\displaystyle x_{0}}$ for all ${\displaystyle t}$ (which is often thought of as a time parameter).
- ${\displaystyle h(1,t)=x_{0}}$ for all ${\displaystyle t\in [0,1]}$, that is, similarly the end point stays at ${\displaystyle x_{0}}$ for all ${\displaystyle t}$.
- ${\displaystyle h(r,0)=\gamma (r)}$, ${\displaystyle h(r,1)=\gamma '(r)}$ for all ${\displaystyle r\in [0,1]}$.

If such a homotopy ${\displaystyle h}$ exists, ${\displaystyle \gamma }$ and ${\displaystyle \gamma '}$ are said to be *homotopic*. The relation " ${\displaystyle \gamma }$ is homotopic to ${\displaystyle \gamma '}$ " is an [equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation "Equivalence relation") so that the set of equivalence classes can be considered: 
$$
{\displaystyle \pi _{1}(X,x_{0}):=\{{\text{all loops }}\gamma {\text{ based at }}x_{0}\}/{\text{homotopy}}.}
$$
 This set (with the group structure described below) is called the *fundamental group* of the topological space ${\displaystyle X}$ at the base point ${\displaystyle x_{0}}$. The purpose of considering the equivalence classes of loops [up to](https://en.wikipedia.org/wiki/Up_to "Up to") homotopy, as opposed to the set of all loops (the so-called [loop space](https://en.wikipedia.org/wiki/Loop_space "Loop space") of ${\displaystyle X}$) is that the latter, while being useful for various purposes, is a rather big and unwieldy object. By contrast the above [quotient](https://en.wikipedia.org/wiki/Quotient_set "Quotient set") is, in many cases, more manageable and computable.

### Group structure

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Homotopy_group_addition.svg/250px-Homotopy_group_addition.svg.png)

Addition of loops

By the above definition, ${\displaystyle \pi _{1}(X,x_{0})}$ is just a set. It becomes a [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)") (and therefore deserves the name fundamental *group*) using the concatenation of loops. More precisely, given two loops ${\displaystyle \gamma _{0},\gamma _{1}}$, their product is defined as the loop

${\displaystyle \gamma _{0}\cdot \gamma _{1}\colon [0,1]\to X}$

${\displaystyle (\gamma _{0}\cdot \gamma _{1})(t)={\begin{cases}\gamma _{0}(2t)&0\leq t\leq {\tfrac {1}{2}}\\\gamma _{1}(2t-1)&{\tfrac {1}{2}}\leq t\leq 1.\end{cases}}}$

Thus the loop ${\displaystyle \gamma _{0}\cdot \gamma _{1}}$ first follows the loop ${\displaystyle \gamma _{0}}$ with "twice the speed" and then follows ${\displaystyle \gamma _{1}}$ with "twice the speed".

The product of two homotopy classes of loops ${\displaystyle [\gamma _{0}]}$ and ${\displaystyle [\gamma _{1}]}$ is then defined as ${\displaystyle [\gamma _{0}\cdot \gamma _{1}]}$. It can be shown that this product does not depend on the choice of representatives and therefore gives a [well-defined](https://en.wikipedia.org/wiki/Equivalence_relation#Well-definedness_under_an_equivalence_relation "Equivalence relation") operation on the set ${\displaystyle \pi _{1}(X,x_{0})}$. This operation turns ${\displaystyle \pi _{1}(X,x_{0})}$ into a group. Its [neutral element](https://en.wikipedia.org/wiki/Neutral_element "Neutral element") is the equivalence (homotopy) class of the constant loop, which stays at ${\displaystyle x_{0}}$ for all times ${\displaystyle t}$ (i.e. this class consists of all loops that can be continuously deformed into the constant loop; intuitively speaking of all the loops that do not "wrap around a hole"). The [inverse](https://en.wikipedia.org/wiki/Inverse_element "Inverse element") of a (homotopy class of a) loop is the same loop, but traversed in the opposite direction (which is in a different homotopy class). More formally,

${\displaystyle \gamma ^{-1}(t):=\gamma (1-t).}$

Given three based loops ${\displaystyle \gamma _{0},\gamma _{1},\gamma _{2},}$ the product

${\displaystyle (\gamma _{0}\cdot \gamma _{1})\cdot \gamma _{2}}$

is the concatenation of these loops, traversing ${\displaystyle \gamma _{0}}$ and then ${\displaystyle \gamma _{1}}$ with quadruple speed, and then ${\displaystyle \gamma _{2}}$ with double speed. By comparison,

${\displaystyle \gamma _{0}\cdot (\gamma _{1}\cdot \gamma _{2})}$

traverses the same paths (in the same order), but ${\displaystyle \gamma _{0}}$ with double speed, and ${\displaystyle \gamma _{1},\gamma _{2}}$ with quadruple speed. Thus, because of the differing speeds, the two paths are not identical. The [associativity](https://en.wikipedia.org/wiki/Associativity "Associativity") axiom

${\displaystyle [\gamma _{0}]\cdot \left([\gamma _{1}]\cdot [\gamma _{2}]\right)=\left([\gamma _{0}]\cdot [\gamma _{1}]\right)\cdot [\gamma _{2}]}$

therefore crucially depends on the fact that paths are considered up to homotopy. Indeed, both above composites are homotopic, for example, to the loop that traverses all three loops ${\displaystyle \gamma _{0},\gamma _{1},\gamma _{2}}$ with triple speed. The set of based loops up to homotopy, equipped with the above operation therefore does turn ${\displaystyle \pi _{1}(X,x_{0})}$ into a group.

### Dependence of the base point

Although the fundamental group in general depends on the choice of base point, it turns out that, up to [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism"), this choice makes no difference as long as the space ${\displaystyle X}$ is [path-connected](https://en.wikipedia.org/wiki/Connected_space#Path_connectedness "Connected space"): more precisely, one obtains an isomorphism by pre- and post-concatenating with a path between the two basepoints. This isomorphism is, in general, not unique: it depends on the choice of path up to homotopy. However changing the path results in changing the isomorphism between the two fundamental groups only by composition with an [inner automorphism](https://en.wikipedia.org/wiki/Inner_automorphism "Inner automorphism"). It is therefore customary to write ${\displaystyle \pi _{1}(X)}$ instead of ${\displaystyle \pi _{1}(X,x_{0})}$ when the choice of basepoint does not matter.

## Concrete examples

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Star_domain.svg/250px-Star_domain.svg.png)

A star domain is simply connected since any loop can be contracted to the center of the domain, denoted {\\displaystyle x\_{0}}.

This section lists some basic examples of fundamental groups. To begin with, in [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space") (${\displaystyle \mathbb {R} ^{n}}$) or any [convex subset](https://en.wikipedia.org/wiki/Convex_set "Convex set") of ${\displaystyle \mathbb {R} ^{n},}$ there is only one homotopy class of loops, and the fundamental group is therefore the [trivial group](https://en.wikipedia.org/wiki/Trivial_group "Trivial group") with one element. More generally, any [star domain](https://en.wikipedia.org/wiki/Star_domain "Star domain") – and yet more generally, any [contractible space](https://en.wikipedia.org/wiki/Contractible_space "Contractible space") – has a trivial fundamental group. Thus, the fundamental group does not distinguish between such spaces.

### The 2-sphere

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/P1S2all.jpg/500px-P1S2all.jpg)

A loop on a 2-sphere (the surface of a ball) being contracted to a point

A path-connected space whose fundamental group is trivial is called [simply connected](https://en.wikipedia.org/wiki/Simply_connected_space "Simply connected space"). For example, the [2-sphere](https://en.wikipedia.org/wiki/2-sphere "2-sphere") ${\displaystyle S^{2}=\left\{(x,y,z)\in \mathbb {R} ^{3}\mid x^{2}+y^{2}+z^{2}=1\right\}}$ depicted on the right, and also all the [higher-dimensional spheres](https://en.wikipedia.org/wiki/N-sphere "N-sphere"), are simply-connected. The figure illustrates a homotopy contracting one particular loop to the constant loop. This idea can be adapted to all loops ${\displaystyle \gamma }$ such that there is a point ${\displaystyle (x,y,z)\in S^{2}}$ that is *not* in the image of ${\displaystyle \gamma .}$ However, since there are loops such that ${\displaystyle \gamma ([0,1])=S^{2}}$ (constructed from the [Peano curve](https://en.wikipedia.org/wiki/Peano_curve "Peano curve"), for example), a complete [proof](https://en.wikipedia.org/wiki/Mathematical_proof "Mathematical proof") requires more careful analysis with tools from algebraic topology, such as the [Seifert–van Kampen theorem](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem "Seifert–van Kampen theorem") or the [cellular approximation theorem](https://en.wikipedia.org/wiki/Cellular_approximation_theorem "Cellular approximation theorem").

### The circle

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Fundamental_group_of_the_circle.svg/250px-Fundamental_group_of_the_circle.svg.png)

Elements of the homotopy group of the circle

The [circle](https://en.wikipedia.org/wiki/Circle "Circle") (also known as the 1-sphere)

${\displaystyle S^{1}=\left\{(x,y)\in \mathbb {R} ^{2}\mid x^{2}+y^{2}=1\right\}}$

is not simply connected. Instead, each homotopy class consists of all loops that wind around the circle a given number of times (which can be positive or negative, depending on the direction of winding). The product of a loop that winds around ${\displaystyle m}$ times and another that winds around ${\displaystyle n}$ times is a loop that winds around ${\displaystyle m+n}$ times. Therefore, the fundamental group of the circle is [isomorphic](https://en.wikipedia.org/wiki/Group_isomorphism "Group isomorphism") to ${\displaystyle (\mathbb {Z} ,+),}$ the additive group of [integers](https://en.wikipedia.org/wiki/Integer#Algebraic_properties "Integer"). This fact can be used to give proofs of the [Brouwer fixed point theorem](https://en.wikipedia.org/wiki/Brouwer_fixed_point_theorem "Brouwer fixed point theorem") [^2] and the [Borsuk–Ulam theorem](https://en.wikipedia.org/wiki/Borsuk%E2%80%93Ulam_theorem "Borsuk–Ulam theorem") in dimension 2.[^3]

### The figure eight

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Marked_2-rose.svg/250px-Marked_2-rose.svg.png)

The fundamental group of the figure eight is the free group on two generators a and b.

The fundamental group of the [figure eight](https://en.wikipedia.org/wiki/Rose_\(topology\) "Rose (topology)") is the [free group](https://en.wikipedia.org/wiki/Free_group "Free group") on two letters. The idea to prove this is as follows: choosing the base point to be the point where the two circles meet (dotted in black in the picture at the right), any loop ${\displaystyle \gamma }$ can be decomposed as 
$$
{\displaystyle \gamma =a^{n_{1}}b^{m_{1}}\cdots a^{n_{k}}b^{m_{k}}}
$$
 where a and b are the two loops winding around each half of the figure as depicted, and the exponents ${\displaystyle n_{1},\dots ,n_{k},m_{1},\dots ,m_{k}}$ are integers. Unlike ${\displaystyle \pi _{1}(S^{1})}$, the fundamental group of the figure eight is *not* [abelian](https://en.wikipedia.org/wiki/Abelian_group "Abelian group"): the two ways of composing ${\displaystyle a}$ and ${\displaystyle b}$ are not homotopic to each other: 
$$
{\displaystyle [a]\cdot [b]\neq [b]\cdot [a]}
$$

More generally, the fundamental group of a [bouquet of ${\displaystyle r}$ circles](https://en.wikipedia.org/wiki/Rose_\(topology\) "Rose (topology)") is the free group on ${\displaystyle r}$ letters.

The fundamental group of a [wedge sum](https://en.wikipedia.org/wiki/Wedge_sum "Wedge sum") of two [path connected spaces](https://en.wikipedia.org/wiki/Path_connected_space "Path connected space") ${\displaystyle X}$ and ${\displaystyle Y}$ can be computed as the [free product](https://en.wikipedia.org/wiki/Free_product "Free product") of the individual fundamental groups: 
$$
{\displaystyle \pi _{1}(X\vee Y)\cong \pi _{1}(X)*\pi _{1}(Y)}
$$
 This generalizes the above observations since the figure eight is the wedge sum of two circles.

The fundamental group of the plane punctured at ${\displaystyle n}$ points is also the free group with ${\displaystyle n}$ generators. The ${\displaystyle i}$ -th generator is the class of the loop that goes around the ${\displaystyle i}$ -th puncture without going around any other punctures.

### Graphs

The fundamental group can be defined for discrete structures too. In particular, consider a [connected](https://en.wikipedia.org/wiki/Connectivity_\(graph_theory\) "Connectivity (graph theory)") [graph](https://en.wikipedia.org/wiki/Graph_\(discrete_mathematics\) "Graph (discrete mathematics)") ${\displaystyle G=(V,E)}$, with a designated vertex ${\displaystyle v_{0}}$ in ${\displaystyle V}$. The loops in ${\displaystyle G}$ are the [cycles](https://en.wikipedia.org/wiki/Cycle_\(graph_theory\) "Cycle (graph theory)") that start and end at ${\displaystyle v_{0}}$.[^4] Let ${\displaystyle T}$ be a [spanning tree](https://en.wikipedia.org/wiki/Spanning_tree "Spanning tree") of ${\displaystyle G}$. Every simple loop in ${\displaystyle G}$ contains exactly one edge in ${\displaystyle E\setminus T}$; every loop in ${\displaystyle G}$ is a concatenation of such simple loops. Therefore, the fundamental group of a [graph](https://en.wikipedia.org/wiki/Graph_\(discrete_mathematics\) "Graph (discrete mathematics)") is a [free group](https://en.wikipedia.org/wiki/Free_group "Free group"), in which the number of generators is exactly the number of edges in ${\displaystyle E\setminus T}$. This number equals ${\displaystyle |E|-|V|+1}$.[^5]

For example, suppose ${\displaystyle G}$ has 16 vertices arranged in 4 rows of 4 vertices each, with edges connecting vertices that are adjacent horizontally or vertically. Then ${\displaystyle G}$ has 24 edges overall, and the number of edges in each spanning tree is 16 − 1 = 15, so the fundamental group of ${\displaystyle G}$ is the free group with 9 generators.[^6] Note that ${\displaystyle G}$ has 9 "holes", similarly to a bouquet of 9 circles, which has the same fundamental group.

### Knot groups

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Trefoil_knot_left.svg/250px-Trefoil_knot_left.svg.png)

A trefoil knot

*[Knot groups](https://en.wikipedia.org/wiki/Knot_group "Knot group")* are by definition the fundamental group of the [complement](https://en.wikipedia.org/wiki/Complement_\(set_theory\) "Complement (set theory)") of a [knot](https://en.wikipedia.org/wiki/Knot_\(mathematics\) "Knot (mathematics)") ${\displaystyle K}$ embedded in ${\displaystyle \mathbb {R} ^{3}}$. For example, the knot group of the [trefoil knot](https://en.wikipedia.org/wiki/Trefoil_knot "Trefoil knot") is known to be the [braid group](https://en.wikipedia.org/wiki/Braid_group "Braid group") ${\displaystyle B_{3}}$, which gives another example of a non-abelian fundamental group. The [Wirtinger presentation](https://en.wikipedia.org/wiki/Wirtinger_presentation "Wirtinger presentation") explicitly describes knot groups in terms of [generators and relations](https://en.wikipedia.org/wiki/Generators_and_relations "Generators and relations") based on a diagram of the knot. Therefore, knot groups have some usage in [knot theory](https://en.wikipedia.org/wiki/Knot_theory "Knot theory") to distinguish between knots: if ${\displaystyle \pi _{1}(\mathbb {R} ^{3}\setminus K)}$ is not isomorphic to some other knot group ${\displaystyle \pi _{1}(\mathbb {R} ^{3}\setminus K')}$ of another knot ${\displaystyle K'}$, then ${\displaystyle K}$ can not be transformed into ${\displaystyle K'}$. Thus the trefoil knot can not be continuously transformed into the circle (also known as the [unknot](https://en.wikipedia.org/wiki/Unknot "Unknot")), since the latter has knot group ${\displaystyle \mathbb {Z} }$. There are, however, knots that can not be deformed into each other, but have isomorphic knot groups.

### Oriented surfaces

The fundamental group of a [genus- *n* orientable surface](https://en.wikipedia.org/wiki/Genus_\(mathematics\)#Orientable_surface "Genus (mathematics)") can be computed in terms of [generators and relations](https://en.wikipedia.org/wiki/Generators_and_relations "Generators and relations") as 
$$
{\displaystyle \left\langle A_{1},B_{1},\ldots ,A_{n},B_{n}\left|A_{1}B_{1}A_{1}^{-1}B_{1}^{-1}\cdots A_{n}B_{n}A_{n}^{-1}B_{n}^{-1}\right.\right\rangle .}
$$

This includes the [torus](https://en.wikipedia.org/wiki/Torus_\(mathematics\) "Torus (mathematics)"), being the case of genus 1, whose fundamental group is 
$$
{\displaystyle \left\langle A_{1},B_{1}\left|A_{1}B_{1}A_{1}^{-1}B_{1}^{-1}\right.\right\rangle \cong \mathbb {Z} ^{2}.}
$$

### Topological groups

The fundamental group of a [topological group](https://en.wikipedia.org/wiki/Topological_group "Topological group") ${\displaystyle X}$ (with respect to the base point being the neutral element) is always commutative. In particular, the fundamental group of a [Lie group](https://en.wikipedia.org/wiki/Lie_group "Lie group") is commutative. In fact, the group structure on ${\displaystyle X}$ endows ${\displaystyle \pi _{1}(X)}$ with another group structure: given two loops ${\displaystyle \gamma }$ and ${\displaystyle \gamma '}$ in ${\displaystyle X}$, another loop ${\displaystyle \gamma \star \gamma '}$ can defined by using the group multiplication in ${\displaystyle X}$:

${\displaystyle (\gamma \star \gamma ')(x)=\gamma (x)\cdot \gamma '(x).}$

This binary operation ${\displaystyle \star }$ on the set of all loops is *a priori* independent from the one described above. However, the [Eckmann–Hilton argument](https://en.wikipedia.org/wiki/Eckmann%E2%80%93Hilton_argument "Eckmann–Hilton argument") shows that it does in fact agree with the above concatenation of loops, and moreover that the resulting group structure is abelian.[^7] [^8]

An inspection of the proof shows that, more generally, ${\displaystyle \pi _{1}(X)}$ is abelian for any [H-space](https://en.wikipedia.org/wiki/H-space "H-space") ${\displaystyle X}$, i.e., the multiplication need not have an inverse, nor does it have to be associative. For example, this shows that the fundamental group of a [loop space](https://en.wikipedia.org/wiki/Loop_space "Loop space") of another topological space ${\displaystyle Y}$, ${\displaystyle X=\Omega (Y),}$ is abelian. Related ideas lead to [Heinz Hopf](https://en.wikipedia.org/wiki/Heinz_Hopf "Heinz Hopf") 's computation of the [cohomology of a Lie group](https://en.wikipedia.org/wiki/Hopf_algebra#Cohomology_of_Lie_groups "Hopf algebra").

## Functoriality

If ${\displaystyle f\colon X\to Y}$ is a [continuous map](https://en.wikipedia.org/wiki/Continuous_function_\(topology\) "Continuous function (topology)"), ${\displaystyle x_{0}\in X}$ and ${\displaystyle y_{0}\in Y}$ with ${\displaystyle f(x_{0})=y_{0},}$ then every loop in ${\displaystyle X}$ with base point ${\displaystyle x_{0}}$ can be composed with ${\displaystyle f}$ to yield a loop in ${\displaystyle Y}$ with base point ${\displaystyle y_{0}.}$ This operation is compatible with the homotopy equivalence relation and with composition of loops. The resulting [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism "Group homomorphism"), called the [induced homomorphism](https://en.wikipedia.org/wiki/Induced_homomorphism_\(fundamental_group\) "Induced homomorphism (fundamental group)"), is written as ${\displaystyle \pi (f)}$ or, more commonly,

${\displaystyle f_{*}\colon \pi _{1}(X,x_{0})\to \pi _{1}(Y,y_{0}).}$

This mapping from continuous maps to group homomorphisms is compatible with composition of maps and [identity morphisms](https://en.wikipedia.org/wiki/Identity_morphism "Identity morphism"). In the parlance of [category theory](https://en.wikipedia.org/wiki/Category_theory "Category theory"), the formation of associating to a topological space its fundamental group is therefore a [functor](https://en.wikipedia.org/wiki/Functor "Functor")

${\displaystyle {\begin{aligned}\pi _{1}\colon \mathbf {Top} _{*}&\to \mathbf {Grp} \\(X,x_{0})&\mapsto \pi _{1}(X,x_{0})\end{aligned}}}$

from the [category of topological spaces together with a base point](https://en.wikipedia.org/wiki/Category_of_pointed_spaces "Category of pointed spaces") to the [category of groups](https://en.wikipedia.org/wiki/Category_of_groups "Category of groups"). It turns out that this functor does not distinguish maps that are [homotopic](https://en.wikipedia.org/wiki/Homotopic "Homotopic") relative to the base point: if ${\displaystyle f,g:X\to Y}$ are continuous maps with ${\displaystyle f(x_{0})=g(x_{0})=y_{0}}$, and ${\displaystyle f}$ and ${\displaystyle g}$ are homotopic relative to ${\displaystyle \{x_{0}\}}$, then ${\displaystyle f_{*}=g_{*}}$. As a consequence, two [homotopy equivalent](https://en.wikipedia.org/wiki/Homotopy_equivalent "Homotopy equivalent") path-connected spaces have isomorphic fundamental groups:

${\displaystyle X\simeq Y\implies \pi _{1}(X,x_{0})\cong \pi _{1}(Y,y_{0}).}$

For example, the inclusion of the circle in the punctured plane

${\displaystyle S^{1}\subset \mathbb {R} ^{2}\setminus \{0\}}$

is a [homotopy equivalence](https://en.wikipedia.org/wiki/Homotopy_equivalence "Homotopy equivalence") and therefore yields an isomorphism of their fundamental groups.

The fundamental group functor takes [products](https://en.wikipedia.org/wiki/Product_topology "Product topology") to [products](https://en.wikipedia.org/wiki/Direct_product "Direct product") and [coproducts](https://en.wikipedia.org/wiki/Wedge_sum "Wedge sum") to [coproducts](https://en.wikipedia.org/wiki/Free_product_of_groups "Free product of groups"). That is, if ${\displaystyle X}$ and ${\displaystyle Y}$ are path connected, then

${\displaystyle \pi _{1}(X\times Y,(x_{0},y_{0}))\cong \pi _{1}(X,x_{0})\times \pi _{1}(Y,y_{0})}$

and if they are also [locally contractible](https://en.wikipedia.org/wiki/Locally_contractible "Locally contractible"), then

${\displaystyle \pi _{1}(X\vee Y)\cong \pi _{1}(X)*\pi _{1}(Y).}$

(In the latter formula, ${\displaystyle \vee }$ denotes the [wedge sum](https://en.wikipedia.org/wiki/Wedge_sum "Wedge sum") of pointed topological spaces, and ${\displaystyle *}$ the [free product](https://en.wikipedia.org/wiki/Free_product "Free product") of groups.) The latter formula is a special case of the [Seifert–van Kampen theorem](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem "Seifert–van Kampen theorem"), which states that the fundamental group functor takes [pushouts](https://en.wikipedia.org/wiki/Pushout_\(category_theory\) "Pushout (category theory)") along inclusions to pushouts.

## Abstract results

As was mentioned above, computing the fundamental group of even relatively simple topological spaces tends to be not entirely trivial, but requires some methods of [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology").

### Relationship to first homology group

The [abelianization](https://en.wikipedia.org/wiki/Abelianization "Abelianization") of the fundamental group can be identified with the first [homology group](https://en.wikipedia.org/wiki/Homology_group "Homology group") of the space.

A special case of the [Hurewicz theorem](https://en.wikipedia.org/wiki/Hurewicz_theorem "Hurewicz theorem") asserts that the first [singular homology group](https://en.wikipedia.org/wiki/Singular_homology "Singular homology") ${\displaystyle H_{1}(X)}$ is, colloquially speaking, the closest approximation to the fundamental group by means of an abelian group. In more detail, mapping the homotopy class of each loop to the homology class of the loop gives a [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism "Group homomorphism")

${\displaystyle \pi _{1}(X)\to H_{1}(X)}$

from the fundamental group of a topological space ${\displaystyle X}$ to its first singular homology group ${\displaystyle H_{1}(X).}$ This homomorphism is not in general an isomorphism since the fundamental group may be non-abelian, but the homology group is, by definition, always abelian. This difference is, however, the only one: if ${\displaystyle X}$ is path-connected, this homomorphism is [surjective](https://en.wikipedia.org/wiki/Surjective "Surjective") and its [kernel](https://en.wikipedia.org/wiki/Kernel_\(algebra\) "Kernel (algebra)") is the [commutator subgroup](https://en.wikipedia.org/wiki/Commutator_subgroup "Commutator subgroup") of the fundamental group, so that ${\displaystyle H_{1}(X)}$ is isomorphic to the [abelianization](https://en.wikipedia.org/wiki/Abelianization "Abelianization") of the fundamental group.[^9]

### Gluing topological spaces

Generalizing the statement above, for a family of path connected spaces ${\displaystyle X_{i},}$ the fundamental group ${\textstyle \pi _{1}\left(\bigvee _{i\in I}X_{i}\right)}$ is the [free product](https://en.wikipedia.org/wiki/Free_product "Free product") of the fundamental groups of the ${\displaystyle X_{i}.}$ [^10] This fact is a special case of the [Seifert–van Kampen theorem](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem "Seifert–van Kampen theorem"), which allows to compute, more generally, fundamental groups of spaces that are glued together from other spaces. For example, the 2-sphere ${\displaystyle S^{2}}$ can be obtained by gluing two copies of slightly overlapping half-spheres along a [neighborhood](https://en.wikipedia.org/wiki/Neighborhood_\(mathematics\) "Neighborhood (mathematics)") of the [equator](https://en.wikipedia.org/wiki/Equator "Equator"). In this case the theorem yields ${\displaystyle \pi _{1}(S^{2})}$ is trivial, since the two half-spheres are contractible and therefore have trivial fundamental group. The fundamental groups of surfaces, as mentioned above, can also be computed using this theorem.

In the parlance of category theory, the theorem can be concisely stated by saying that the fundamental group functor takes [pushouts](https://en.wikipedia.org/wiki/Pushout_\(category_theory\) "Pushout (category theory)") (in the category of topological spaces) along inclusions to pushouts (in the category of groups).[^11]

### Coverings

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Covering_map.svg/250px-Covering_map.svg.png)

The map {\\displaystyle \\mathbb {R} \\times \[0,1\]\\to S^{1}\\times \[0,1\]} is a covering: the preimage of {\\displaystyle U} (highlighted in gray) is a disjoint union of copies of. Moreover, it is a universal covering since {\\displaystyle \\mathbb {R} \\times \[0,1\]} is contractible and therefore simply connected.

Given a topological space ${\displaystyle B}$, a [continuous map](https://en.wikipedia.org/wiki/Continuous_function_\(topology\) "Continuous function (topology)")

${\displaystyle f:E\to B}$

is called a *covering* or ${\displaystyle E}$ is called a *[covering space](https://en.wikipedia.org/wiki/Covering_space "Covering space")* of ${\displaystyle B}$ if every point ${\displaystyle b}$ in ${\displaystyle B}$ admits an [open neighborhood](https://en.wikipedia.org/wiki/Open_neighborhood "Open neighborhood") ${\displaystyle U}$ such that there is a [homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") between the [preimage](https://en.wikipedia.org/wiki/Preimage "Preimage") of ${\displaystyle U}$ and a [disjoint union](https://en.wikipedia.org/wiki/Disjoint_union "Disjoint union") of copies of ${\displaystyle U}$ (indexed by some set ${\displaystyle I}$),

${\displaystyle \varphi :\bigsqcup _{i\in I}U\to f^{-1}(U)}$

in such a way that ${\displaystyle f\circ \varphi }$ is the standard projection map ${\displaystyle \bigsqcup _{i\in I}U\to U.}$ [^12]

#### Universal covering

A covering is called a [universal covering](https://en.wikipedia.org/wiki/Universal_covering "Universal covering") if ${\displaystyle E}$ is, in addition to the preceding condition, simply connected.[^13] It is universal in the sense that all other coverings can be constructed by suitably identifying points in ${\displaystyle E}$. Knowing a universal covering

${\displaystyle p:{\widetilde {X}}\to X}$

of a topological space ${\displaystyle X}$ is helpful in understanding its fundamental group in several ways: first, ${\displaystyle \pi _{1}(X)}$ identifies with the group of [deck transformations](https://en.wikipedia.org/wiki/Deck_transformations "Deck transformations"), i.e., the group of [homeomorphisms](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") ${\displaystyle \varphi :{\widetilde {X}}\to {\widetilde {X}}}$ that commute with the map to ${\displaystyle X}$, i.e., ${\displaystyle p\circ \varphi =p.}$ Another relation to the fundamental group is that ${\displaystyle \pi _{1}(X,x)}$ can be identified with the fiber ${\displaystyle p^{-1}(x).}$ For example, the map

${\displaystyle p:\mathbb {R} \to S^{1},\,t\mapsto \exp(2\pi it)}$

(or, equivalently, ${\displaystyle \pi :\mathbb {R} \to \mathbb {R} /\mathbb {Z} ,\ t\mapsto [t]}$) is a universal covering. The deck transformations are the maps ${\displaystyle t\mapsto t+n}$ for ${\displaystyle n\in \mathbb {Z} .}$ This is in line with the identification ${\displaystyle p^{-1}(1)=\mathbb {Z} ,}$ in particular this proves the above claim ${\displaystyle \pi _{1}(S^{1})\cong \mathbb {Z} .}$

Any path connected, [locally path connected](https://en.wikipedia.org/wiki/Locally_connected_space#Definitions "Locally connected space") and [locally simply connected](https://en.wikipedia.org/wiki/Locally_simply_connected "Locally simply connected") topological space ${\displaystyle X}$ admits a universal covering.[^14] An abstract construction proceeds analogously to the fundamental group by taking pairs ${\displaystyle (x,\gamma )}$, where ${\displaystyle x}$ is a point in ${\displaystyle X}$ and ${\displaystyle \gamma }$ is a homotopy class of paths from ${\displaystyle x_{0}}$ to ${\displaystyle x}$. The passage from a topological space to its universal covering can be used in understanding the geometry of ${\displaystyle X}$. For example, the [uniformization theorem](https://en.wikipedia.org/wiki/Uniformization_theorem "Uniformization theorem") shows that any simply connected [Riemann surface](https://en.wikipedia.org/wiki/Riemann_surface "Riemann surface") is (isomorphic to) either ${\displaystyle S^{2},}$ ${\displaystyle \mathbb {C} ,}$ or the [upper half-plane](https://en.wikipedia.org/wiki/Upper_half-plane "Upper half-plane").[^15] General Riemann surfaces then arise as quotients of [group actions](https://en.wikipedia.org/wiki/Group_action "Group action") on these three surfaces.

The [quotient](https://en.wikipedia.org/wiki/Quotient_topology "Quotient topology") of a [free action](https://en.wikipedia.org/wiki/Group_action#Remarkable_properties_of_actions "Group action") of a [discrete](https://en.wikipedia.org/wiki/Discrete_topology "Discrete topology") group ${\displaystyle G}$ on a simply connected space ${\displaystyle Y}$ has fundamental group

${\displaystyle \pi _{1}(Y/G)\cong G.}$

As an example, the real ${\displaystyle n}$ -dimensional real [projective space](https://en.wikipedia.org/wiki/Projective_space "Projective space") ${\displaystyle \mathbb {R} \mathrm {P} ^{n}}$ is obtained as the quotient of the ${\displaystyle n}$ -dimensional unit sphere ${\displaystyle S^{n}}$ by the antipodal action of the group ${\displaystyle \mathbb {Z} /2}$ sending ${\displaystyle x\in S^{n}}$ to ${\displaystyle -x.}$ As ${\displaystyle S^{n}}$ is simply connected for ${\displaystyle n\geq 2}$, it is a universal cover of ${\displaystyle \mathbb {R} \mathrm {P} ^{n}}$ in these cases, which implies ${\displaystyle \pi _{1}(\mathbb {R} \mathrm {P} ^{n})\cong \mathbb {Z} /2}$ for ${\displaystyle n\geq 2}$.

#### Lie groups

Let ${\displaystyle G}$ be a connected, simply connected [compact Lie group](https://en.wikipedia.org/wiki/Compact_Lie_group "Compact Lie group"), for example, the [special unitary group](https://en.wikipedia.org/wiki/Special_unitary_group "Special unitary group") ${\displaystyle {\text{SU}}(n)}$, and let ${\displaystyle \Gamma }$ be a finite subgroup of ${\displaystyle G}$. Then the [homogeneous space](https://en.wikipedia.org/wiki/Homogeneous_space "Homogeneous space") ${\displaystyle X=G/\Gamma }$ has fundamental group ${\displaystyle \Gamma }$, which acts by right multiplication on the universal covering space ${\displaystyle G}$. Among the many variants of this construction, one of the most important is given by [locally symmetric spaces](https://en.wikipedia.org/wiki/Locally_symmetric_space "Locally symmetric space") ${\displaystyle X=\Gamma \setminus G/K}$, where

- ${\displaystyle G}$ is a non-compact simply connected, connected [Lie group](https://en.wikipedia.org/wiki/Lie_group "Lie group") (often [semisimple](https://en.wikipedia.org/wiki/Semisimple_Lie_group "Semisimple Lie group")),
- ${\displaystyle K}$ is a maximal compact subgroup of ${\displaystyle G}$
- ${\displaystyle \Gamma }$ is a discrete [countable](https://en.wikipedia.org/wiki/Countable_set "Countable set") [torsion-free](https://en.wikipedia.org/wiki/Torsion-free_group "Torsion-free group") subgroup of ${\displaystyle G}$.

In this case the fundamental group is ${\displaystyle \Gamma }$ and the universal covering space ${\displaystyle G/K}$ is actually [contractible](https://en.wikipedia.org/wiki/Contractible "Contractible") (by the [Cartan decomposition](https://en.wikipedia.org/wiki/Cartan_decomposition "Cartan decomposition") for Lie groups).

As an example take ${\displaystyle G={\text{SL}}(2,\mathbb {R} )}$, ${\displaystyle K={\text{SO}}(2)}$ and ${\displaystyle \Gamma }$ any torsion-free [congruence subgroup](https://en.wikipedia.org/wiki/Congruence_subgroup "Congruence subgroup") of the [modular group](https://en.wikipedia.org/wiki/Modular_group "Modular group") ${\displaystyle {\text{SL}}(2,\mathbb {Z} )}$.

From the explicit realization, it also follows that the universal covering space of a path connected [topological group](https://en.wikipedia.org/wiki/Topological_group "Topological group") ${\displaystyle H}$ is again a path connected topological group ${\displaystyle G}$. Moreover, the covering map is a continuous [open](https://en.wikipedia.org/wiki/Open_map "Open map") homomorphism of ${\displaystyle G}$ onto ${\displaystyle H}$ with kernel ${\displaystyle \Gamma }$, a closed discrete [normal subgroup](https://en.wikipedia.org/wiki/Normal_subgroup "Normal subgroup") of ${\displaystyle G}$:

${\displaystyle 1\to \Gamma \to G\to H\to 1.}$

Since ${\displaystyle G}$ is a connected group with a continuous action by conjugation on a discrete group ${\displaystyle \Gamma }$, it must act trivially, so that ${\displaystyle \Gamma }$ has to be a subgroup of the [center](https://en.wikipedia.org/wiki/Center_\(group_theory\) "Center (group theory)") of ${\displaystyle G}$. In particular ${\displaystyle \pi _{1}(H)=\Gamma }$ is an [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group"); this can also easily be seen directly without using covering spaces. The group ${\displaystyle G}$ is called the *[universal covering group](https://en.wikipedia.org/wiki/Universal_covering_group "Universal covering group")* of ${\displaystyle H}$.

As the universal covering group suggests, there is an analogy between the fundamental group of a topological group and the center of a group; this is elaborated at [Lattice of covering groups](https://en.wikipedia.org/wiki/Covering_group#Lattice_of_covering_groups "Covering group").

### Fibrations

*[Fibrations](https://en.wikipedia.org/wiki/Fibrations "Fibrations")* provide a very powerful means to compute homotopy groups. A fibration ${\displaystyle f}$ the so-called *total space*, and the base space ${\displaystyle B}$ has, in particular, the property that all its fibers ${\displaystyle f^{-1}(b)}$ are homotopy equivalent and therefore can not be distinguished using fundamental groups (and higher homotopy groups), provided that ${\displaystyle B}$ is path-connected.[^16] Therefore, the space ${\displaystyle E}$ can be regarded as a " [twisted](https://en.wikipedia.org/wiki/Dehn_twist "Dehn twist") product" of the [base space](https://en.wikipedia.org/wiki/Fibration "Fibration") ${\displaystyle B}$ and the [fiber](https://en.wikipedia.org/wiki/Fiber_\(algebraic_geometry\) "Fiber (algebraic geometry)") ${\displaystyle F=f^{-1}(b).}$ The great importance of fibrations to the computation of homotopy groups stems from a [long exact sequence](https://en.wikipedia.org/wiki/Homotopy_group#Long_exact_sequence_of_a_fibration "Homotopy group")

${\displaystyle \dots \to \pi _{2}(B)\to \pi _{1}(F)\to \pi _{1}(E)\to \pi _{1}(B)\to \pi _{0}(F)\to \pi _{0}(E)}$

provided that ${\displaystyle B}$ is path-connected.[^17] The term ${\displaystyle \pi _{2}(B)}$ is the second [homotopy group](https://en.wikipedia.org/wiki/Homotopy_group "Homotopy group") of ${\displaystyle B}$, which is defined to be the set of homotopy classes of maps from ${\displaystyle S^{2}}$ to ${\displaystyle B}$, in direct analogy with the definition of ${\displaystyle \pi _{1}.}$

If ${\displaystyle E}$ happens to be path-connected and simply connected, this sequence reduces to an isomorphism

${\displaystyle \pi _{1}(B)\cong \pi _{0}(F)}$

which generalizes the above fact about the universal covering (which amounts to the case where the fiber ${\displaystyle F}$ is also discrete). If instead ${\displaystyle F}$ happens to be connected and simply connected, it reduces to an isomorphism

${\displaystyle \pi _{1}(E)\cong \pi _{1}(B).}$

What is more, the sequence can be continued at the left with the higher homotopy groups ${\displaystyle \pi _{n}}$ of the three spaces, which gives some access to computing such groups in the same vein.

#### Classical Lie groups

Such fiber sequences can be used to inductively compute fundamental groups of compact [classical Lie groups](https://en.wikipedia.org/wiki/Classical_Lie_groups "Classical Lie groups") such as the [special unitary group](https://en.wikipedia.org/wiki/Special_unitary_group "Special unitary group") ${\displaystyle \mathrm {SU} (n),}$ with ${\displaystyle n\geq 2.}$ This group acts [transitively](https://en.wikipedia.org/wiki/Group_action#Remarkable_properties_of_actions "Group action") on the unit sphere ${\displaystyle S^{2n-1}}$ inside ${\displaystyle \mathbb {C} ^{n}=\mathbb {R} ^{2n}.}$ The [stabilizer](https://en.wikipedia.org/wiki/Stabilizer_subgroup "Stabilizer subgroup") of a point in the sphere is isomorphic to ${\displaystyle \mathrm {SU} (n-1).}$ It then can be shown [^18] that this yields a fiber sequence

${\displaystyle \mathrm {SU} (n-1)\to \mathrm {SU} (n)\to S^{2n-1}.}$

Since ${\displaystyle n\geq 2,}$ the sphere ${\displaystyle S^{2n-1}}$ has dimension at least 3, which implies

${\displaystyle \pi _{1}(S^{2n-1})\cong \pi _{2}(S^{2n-1})=1.}$

The long exact sequence then shows an isomorphism

${\displaystyle \pi _{1}(\mathrm {SU} (n))\cong \pi _{1}(\mathrm {SU} (n-1)).}$

Since ${\displaystyle \mathrm {SU} (1)}$ is a single point, so that ${\displaystyle \pi _{1}(\mathrm {SU} (1))}$ is trivial, this shows that ${\displaystyle \mathrm {SU} (n)}$ is simply connected for all ${\displaystyle n.}$

The fundamental group of noncompact Lie groups can be reduced to the compact case, since such a group is homotopic to its maximal compact subgroup.[^19] These methods give the following results:[^20]

| Compact classical Lie group *G* | Non-compact Lie group | ${\displaystyle \pi _{1}}$ |
| --- | --- | --- |
| special unitary group ${\displaystyle \mathrm {SU} (n)}$ | ${\displaystyle \mathrm {SL} (n,\mathbb {C} )}$ | 1 |
| [unitary group](https://en.wikipedia.org/wiki/Unitary_group "Unitary group") ${\displaystyle \mathrm {U} (n)}$ | ${\displaystyle \mathrm {GL} (n,\mathbb {C} ),\mathrm {Sp} (n,\mathbb {R} )}$ | ${\displaystyle \mathbb {Z} }$ |
| [special orthogonal group](https://en.wikipedia.org/wiki/Special_orthogonal_group "Special orthogonal group") ${\displaystyle \mathrm {SO} (n)}$ | ${\displaystyle \mathrm {SO} (n,\mathbb {C} )}$ | ${\displaystyle \mathbb {Z} /2}$ for ${\displaystyle n\geq 3}$ and ${\displaystyle \mathbb {Z} }$ for ${\displaystyle n=2}$ |
| compact [symplectic group](https://en.wikipedia.org/wiki/Symplectic_group "Symplectic group") ${\displaystyle \mathrm {Sp} (n)}$ | ${\displaystyle \mathrm {Sp} (n,\mathbb {C} )}$ | 1 |

A second method of computing fundamental groups applies to all connected compact Lie groups and uses the machinery of the [maximal torus](https://en.wikipedia.org/wiki/Maximal_torus "Maximal torus") and the associated [root system](https://en.wikipedia.org/wiki/Root_system "Root system"). Specifically, let ${\displaystyle T}$ be a maximal torus in a connected compact Lie group ${\displaystyle K,}$ and let ${\displaystyle {\mathfrak {t}}}$ be the [Lie algebra](https://en.wikipedia.org/wiki/Lie_algebra "Lie algebra") of ${\displaystyle T.}$ The [exponential map](https://en.wikipedia.org/wiki/Exponential_map_\(Lie_theory\) "Exponential map (Lie theory)")

${\displaystyle \exp :{\mathfrak {t}}\to T}$

is a fibration and therefore its kernel ${\displaystyle \Gamma \subset {\mathfrak {t}}}$ identifies with ${\displaystyle \pi _{1}(T).}$ The map

${\displaystyle \pi _{1}(T)\to \pi _{1}(K)}$

can be shown to be surjective [^21] with kernel given by the set ${\displaystyle I}$ of integer linear combination of [coroots](https://en.wikipedia.org/wiki/Coroot "Coroot"). This leads to the computation

${\displaystyle \pi _{1}(K)\cong \Gamma /I.}$ [^22]

This method shows, for example, that any connected compact Lie group for which the associated root system is of [type ${\displaystyle G_{2}}$](https://en.wikipedia.org/wiki/G2_\(mathematics\) "G2 (mathematics)") is simply connected.[^23] Thus, there is (up to isomorphism) only one connected compact Lie group having Lie algebra of type ${\displaystyle G_{2}}$; this group is simply connected and has trivial center.

## Edge-path group of a simplicial complex

When the topological space is homeomorphic to a [simplicial complex](https://en.wikipedia.org/wiki/Simplicial_complex "Simplicial complex"), its fundamental group can be described explicitly in terms of [generators and relations](https://en.wikipedia.org/wiki/Presentation_of_a_group "Presentation of a group").

If ${\displaystyle X}$ is a [connected](https://en.wikipedia.org/wiki/Connected_space "Connected space") simplicial complex, an *edge-path* in ${\displaystyle X}$ is defined to be a chain of vertices connected by edges in ${\displaystyle X}$. Two edge-paths are said to be *edge-equivalent* if one can be obtained from the other by successively switching between an edge and the two opposite edges of a triangle in ${\displaystyle X}$. If ${\displaystyle v}$ is a fixed vertex in ${\displaystyle X}$, an *edge-loop* at ${\displaystyle v}$ is an edge-path starting and ending at ${\displaystyle v}$. The **edge-path group** ${\displaystyle E(X,v)}$ is defined to be the set of edge-equivalence classes of edge-loops at ${\displaystyle v}$, with product and inverse defined by concatenation and reversal of edge-loops.

The edge-path group is naturally isomorphic to ${\displaystyle \pi _{1}(|X|,v)}$, the fundamental group of the [geometric realisation](https://en.wikipedia.org/wiki/Simplicial_set "Simplicial set") ${\displaystyle |X|}$ of ${\displaystyle X}$.[^24] Since it depends only on the [2-skeleton](https://en.wikipedia.org/wiki/N-skeleton "N-skeleton") ${\displaystyle X^{2}}$ of ${\displaystyle X}$ (that is, the vertices, edges, and triangles of ${\displaystyle X}$), the groups ${\displaystyle \pi _{1}(|X|,v)}$ and ${\displaystyle \pi _{1}(|X^{2}|,v)}$ are isomorphic.

The edge-path group can be described explicitly in terms of [generators and relations](https://en.wikipedia.org/wiki/Generators_and_relations "Generators and relations"). If ${\displaystyle T}$ is a [maximal spanning tree](https://en.wikipedia.org/wiki/Spanning_tree "Spanning tree") in the [1-skeleton](https://en.wikipedia.org/wiki/N-skeleton "N-skeleton") of ${\displaystyle X}$, then ${\displaystyle E(X,v)}$ is canonically isomorphic to the group with generators (the oriented edge-paths of ${\displaystyle X}$ not occurring in ${\displaystyle T}$) and relations (the edge-equivalences corresponding to triangles in ${\displaystyle X}$). A similar result holds if ${\displaystyle T}$ is replaced by any [simply connected](https://en.wikipedia.org/wiki/Simply_connected "Simply connected") —in particular [contractible](https://en.wikipedia.org/wiki/Contractible "Contractible") —subcomplex of ${\displaystyle X}$. This often gives a practical way of computing fundamental groups and can be used to show that every [finitely presented group](https://en.wikipedia.org/wiki/Finitely_presented_group "Finitely presented group") arises as the fundamental group of a finite simplicial complex. It is also one of the classical methods used for [topological surfaces](https://en.wikipedia.org/wiki/Surface_\(topology\) "Surface (topology)"), which are classified by their fundamental groups.

The *universal covering space* of a finite connected simplicial complex ${\displaystyle X}$ can also be described directly as a simplicial complex using edge-paths. Its vertices are pairs ${\displaystyle (w,\gamma )}$ where ${\displaystyle w}$ is a vertex of ${\displaystyle X}$ and γ is an edge-equivalence class of paths from ${\displaystyle v}$ to ${\displaystyle w}$. The ${\displaystyle k}$ -simplices containing ${\displaystyle (w,\gamma )}$ correspond naturally to the ${\displaystyle k}$ -simplices containing ${\displaystyle w}$. Each new vertex ${\displaystyle u}$ of the ${\displaystyle k}$ -simplex gives an edge ${\displaystyle wu}$ and hence, by concatenation, a new path ${\displaystyle \gamma _{u}}$ from ${\displaystyle v}$ to ${\displaystyle u}$. The points ${\displaystyle (w,\gamma )}$ and ${\displaystyle (u,\gamma _{u})}$ are the vertices of the "transported" simplex in the universal covering space. The edge-path group acts naturally by concatenation, preserving the simplicial structure, and the quotient space is just ${\displaystyle X}$.

It is well known that this method can also be used to compute the fundamental group of an arbitrary topological space. This was doubtless known to [Eduard Čech](https://en.wikipedia.org/wiki/Eduard_%C4%8Cech "Eduard Čech") and [Jean Leray](https://en.wikipedia.org/wiki/Jean_Leray "Jean Leray") and explicitly appeared as a remark in a paper by [André Weil](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil "André Weil");[^25] various other authors such as Lorenzo Calabi, [Wu Wen-tsün](https://en.wikipedia.org/wiki/Wu_Wenjun "Wu Wenjun"), and Nodar Berikashvili have also published proofs. In the simplest case of a compact space ${\displaystyle X}$ with a finite open covering in which all [non-empty](https://en.wikipedia.org/wiki/Empty_set "Empty set") finite [intersections](https://en.wikipedia.org/wiki/Intersection_\(set_theory\) "Intersection (set theory)") of open sets in the covering are contractible, the fundamental group can be identified with the edge-path group of the simplicial complex corresponding to the [nerve of the covering](https://en.wikipedia.org/wiki/Nerve_of_an_open_covering "Nerve of an open covering").

## Realizability

- Every group can be realized as the fundamental group of a [connected](https://en.wikipedia.org/wiki/Connected_space "Connected space") [CW-complex](https://en.wikipedia.org/wiki/CW-complex "CW-complex") of dimension 2 (or higher). As noted above, though, only [free groups](https://en.wikipedia.org/wiki/Free_group "Free group") can occur as fundamental groups of 1-dimensional CW-complexes (that is, graphs).
- Every [finitely presented group](https://en.wikipedia.org/wiki/Finitely_presented_group "Finitely presented group") can be realized as the fundamental group of a [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space"), connected, [smooth manifold](https://en.wikipedia.org/wiki/Smooth_manifold "Smooth manifold") of dimension 4 (or higher). But there are severe restrictions on which groups occur as fundamental groups of low-dimensional manifolds. For example, no [free abelian group](https://en.wikipedia.org/wiki/Free_abelian_group "Free abelian group") of rank 4 or higher can be realized as the fundamental group of a manifold of dimension 3 or less. It can be proved that every group can be realized as the fundamental group of a compact [Hausdorff space](https://en.wikipedia.org/wiki/Hausdorff_space "Hausdorff space") [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") there is no [measurable cardinal](https://en.wikipedia.org/wiki/Measurable_cardinal "Measurable cardinal").[^26]

## Related concepts

### Higher homotopy groups

Roughly speaking, the fundamental group detects the 1-dimensional hole structure of a space, but not higher-dimensional holes such as for the 2-sphere. Such "higher-dimensional holes" can be detected using the higher [homotopy groups](https://en.wikipedia.org/wiki/Homotopy_group "Homotopy group") ${\displaystyle \pi _{n}(X)}$, which are defined to consist of homotopy classes of (basepoint-preserving) maps from ${\displaystyle S^{n}}$ to ${\displaystyle X}$. For example, the [Hurewicz theorem](https://en.wikipedia.org/wiki/Hurewicz_theorem "Hurewicz theorem") implies that for all ${\displaystyle n\geq 1}$ the [${\displaystyle n}$ -th homotopy group of the *n* -sphere](https://en.wikipedia.org/wiki/Homotopy_groups_of_spheres "Homotopy groups of spheres") is

${\displaystyle \pi _{n}(S^{n})=\mathbb {Z} .}$ [^27]

As was mentioned in the above computation of ${\displaystyle \pi _{1}}$ of classical Lie groups, higher homotopy groups can be relevant even for computing fundamental groups.

### Loop space

The set of based loops (as is, i.e. not taken up to homotopy) in a [pointed space](https://en.wikipedia.org/wiki/Pointed_space "Pointed space") ${\displaystyle X}$, endowed with the [compact open topology](https://en.wikipedia.org/wiki/Compact_open_topology "Compact open topology"), is known as the [loop space](https://en.wikipedia.org/wiki/Loop_space "Loop space"), denoted ${\displaystyle \Omega X.}$ The fundamental group of ${\displaystyle X}$ is in [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") with the set of [path components](https://en.wikipedia.org/wiki/Path_component "Path component") of its loop space:[^28]

${\displaystyle \pi _{1}(X)\cong \pi _{0}(\Omega X).}$

### Fundamental groupoid

The *[fundamental groupoid](https://en.wikipedia.org/wiki/Fundamental_groupoid "Fundamental groupoid")* is a variant of the fundamental group that is useful in situations where the choice of a base point ${\displaystyle x_{0}\in X}$ is undesirable. It is defined by first considering the [category](https://en.wikipedia.org/wiki/Category_\(mathematics\) "Category (mathematics)") of [paths](https://en.wikipedia.org/wiki/Moore_path "Moore path") in ${\displaystyle X,}$ i.e., continuous functions

${\displaystyle \gamma \colon [0,r]\to X}$,

where ${\displaystyle r}$ is an arbitrary non-negative real number. Since the length ${\displaystyle r}$ is variable in this approach, such paths can be concatenated as is (i.e., not up to homotopy) and therefore yield a category.[^29] Two such paths ${\displaystyle \gamma ,\gamma '}$ with the same endpoints and length ${\displaystyle r}$, resp. ${\displaystyle r}$ ' are considered equivalent if there exist real numbers ${\displaystyle u,v\geqslant 0}$ such that ${\displaystyle r+u=r'+v}$ and ${\displaystyle \gamma _{u},\gamma '_{v}\colon [0,r+u]\to X}$ are homotopic relative to their end points, where ${\displaystyle \gamma _{u}(t)={\begin{cases}\gamma (t),&t\in [0,r]\\\gamma (r),&t\in [r,r+u].\end{cases}}}$ [^30] [^31]

The category of paths up to this equivalence relation is denoted ${\displaystyle \Pi (X).}$ Each morphism in ${\displaystyle \Pi (X)}$ is an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism"), with inverse given by the same path traversed in the opposite direction. Such a category is called a [groupoid](https://en.wikipedia.org/wiki/Groupoid "Groupoid"). It reproduces the fundamental group since

${\displaystyle \pi _{1}(X,x_{0})=\mathrm {Hom} _{\Pi (X)}(x_{0},x_{0})}$.

More generally, one can consider the fundamental groupoid on a set ${\displaystyle A}$ of base points, chosen according to the geometry of the situation; for example, in the case of the circle, which can be represented as the [union](https://en.wikipedia.org/wiki/Union_\(set_theory\) "Union (set theory)") of two connected open sets whose intersection has two components, one can choose one base point in each component. The [van Kampen theorem](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem "Seifert–van Kampen theorem") admits a version for fundamental groupoids which gives, for example, another way to compute the fundamental group(oid) of ${\displaystyle S^{1}.}$ [^32]

### Local systems

Generally speaking, [representations](https://en.wikipedia.org/wiki/Group_representation "Group representation") may serve to exhibit features of a group by its actions on other mathematical objects, often [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space"). Representations of the fundamental group have a very geometric significance: any *[local system](https://en.wikipedia.org/wiki/Local_system "Local system")* (i.e., a [sheaf](https://en.wikipedia.org/wiki/Sheaf_\(mathematics\) "Sheaf (mathematics)") ${\displaystyle {\mathcal {F}}}$ on ${\displaystyle X}$ with the property that locally in a sufficiently small neighborhood ${\displaystyle U}$ of any point on ${\displaystyle X}$, the restriction of ${\displaystyle F}$ is a [constant sheaf](https://en.wikipedia.org/wiki/Constant_sheaf "Constant sheaf") of the form ${\displaystyle {\mathcal {F}}|_{U}=\mathbb {Q} ^{n}}$) gives rise to the so-called [monodromy representation](https://en.wikipedia.org/w/index.php?title=Monodromy_representation&action=edit&redlink=1 "Monodromy representation (page does not exist)"), a representation of the fundamental group on an ${\displaystyle n}$ - [dimensional](https://en.wikipedia.org/wiki/Dimension_\(vector_space\) "Dimension (vector space)") ${\displaystyle \mathbb {Q} }$ -vector space. [Conversely](https://en.wikipedia.org/wiki/Converse_\(logic\) "Converse (logic)"), any such representation on a path-connected space ${\displaystyle X}$ arises in this manner.[^33] This [equivalence of categories](https://en.wikipedia.org/wiki/Equivalence_of_categories "Equivalence of categories") between representations of ${\displaystyle \pi _{1}(X)}$ and local systems is used, for example, in the study of [differential equations](https://en.wikipedia.org/wiki/Differential_equation "Differential equation"), such as the [Knizhnik–Zamolodchikov equations](https://en.wikipedia.org/wiki/Knizhnik%E2%80%93Zamolodchikov_equations "Knizhnik–Zamolodchikov equations").

### Étale fundamental group

In [algebraic geometry](https://en.wikipedia.org/wiki/Algebraic_geometry "Algebraic geometry"), the so-called [étale fundamental group](https://en.wikipedia.org/wiki/%C3%89tale_fundamental_group "Étale fundamental group") is used as a replacement for the fundamental group.[^34] Since the [Zariski topology](https://en.wikipedia.org/wiki/Zariski_topology "Zariski topology") on an [algebraic variety](https://en.wikipedia.org/wiki/Algebraic_variety "Algebraic variety") or [scheme](https://en.wikipedia.org/wiki/Scheme_\(mathematics\) "Scheme (mathematics)") ${\displaystyle X}$ is much [coarser](https://en.wikipedia.org/wiki/Comparison_of_topologies "Comparison of topologies") than, say, the [topology](https://en.wikipedia.org/wiki/Topological_space "Topological space") of open subsets in ${\displaystyle \mathbb {R} ^{n},}$ it is no longer meaningful to consider continuous maps from an [interval](https://en.wikipedia.org/wiki/Interval_\(mathematics\) "Interval (mathematics)") to ${\displaystyle X}$. Instead, the approach developed by [Grothendieck](https://en.wikipedia.org/wiki/Grothendieck "Grothendieck") consists in constructing ${\displaystyle \pi _{1}^{\text{et}}}$ by considering all [finite](https://en.wikipedia.org/wiki/Finite_morphism "Finite morphism") [étale covers](https://en.wikipedia.org/wiki/%C3%89tale_morphism "Étale morphism") of ${\displaystyle X}$. These serve as an algebro-geometric analogue of coverings with finite fibers.

This yields a theory applicable in situations where no great generality classical topological intuition whatsoever is available, for example for varieties defined over a [finite field](https://en.wikipedia.org/wiki/Finite_field "Finite field"). Also, the étale fundamental group of a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") is its ([absolute](https://en.wikipedia.org/wiki/Absolute_Galois_group "Absolute Galois group")) [Galois group](https://en.wikipedia.org/wiki/Galois_group "Galois group"). On the other hand, for smooth varieties ${\displaystyle X}$ over the complex numbers, the étale fundamental group retains much of the information inherent in the classical fundamental group: the former is the [profinite completion](https://en.wikipedia.org/wiki/Profinite_completion "Profinite completion") of the latter.[^35]

### Fundamental group of algebraic groups

The fundamental group of a [root system](https://en.wikipedia.org/wiki/Root_system "Root system") is defined in analogy to the computation for Lie groups.[^36] This allows to define and use the fundamental group of a semisimple [linear algebraic group](https://en.wikipedia.org/wiki/Linear_algebraic_group "Linear algebraic group") ${\displaystyle G}$, which is a useful basic tool in the classification of linear algebraic groups.[^37]

### Fundamental group of simplicial sets

The homotopy relation between 1-simplices of a [simplicial set](https://en.wikipedia.org/wiki/Simplicial_set "Simplicial set") ${\displaystyle X}$ is an equivalence relation if ${\displaystyle X}$ is a [Kan complex](https://en.wikipedia.org/wiki/Kan_complex "Kan complex") but not necessarily so in general.[^38] Thus, ${\displaystyle \pi _{1}}$ of a Kan complex can be defined as the set of homotopy classes of 1-simplices. The fundamental group of an arbitrary simplicial set ${\displaystyle X}$ are defined to be the homotopy group of its [topological realization](https://en.wikipedia.org/w/index.php?title=Topological_realization&action=edit&redlink=1 "Topological realization (page does not exist)"), ${\displaystyle |X|,}$ i.e., the topological space obtained by gluing topological simplices as prescribed by the simplicial set structure of ${\displaystyle X}$.[^39]

[^1]: [Poincaré, Henri](https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9 "Henri Poincaré") (1895). ["Analysis situs"](http://gallica.bnf.fr/ark:/12148/bpt6k4337198/f7.image). *Journal de l'École Polytechnique*. (2) (in French). **1**: 1–123. Translated in Poincaré, Henri (2009). ["Analysis situs"](http://www.maths.ed.ac.uk/~aar/papers/poincare2009.pdf) (PDF). *Papers on Topology: Analysis Situs and Its Five Supplements*. Translated by [John Stillwell](https://en.wikipedia.org/wiki/John_Stillwell "John Stillwell"). pp. 18–99. [Archived](https://web.archive.org/web/20120327043041/http://www.maths.ed.ac.uk/~aar/papers/poincare2009.pdf) (PDF) from the original on 2012-03-27.

[^2]: [May (1999](#CITEREFMay1999), Ch. 1, §6)

[^3]: [Massey (1991](#CITEREFMassey1991), Ch. V, §9)

[^4]: ["Meaning of Fundamental group of a graph"](https://math.stackexchange.com/questions/515896/meaning-of-fundamental-group-of-a-graph). *Mathematics Stack Exchange*. Retrieved 2020-07-28.

[^5]: Simon, J (2008). ["Example of calculating the fundamental group of a graph G"](https://web.archive.org/web/20200728164140/http://homepage.divms.uiowa.edu/~jsimon/COURSES/M201Fall08/HandoutsAndHomework/Graph1.pdf) (PDF). Archived from [the original](http://homepage.divms.uiowa.edu/~jsimon/COURSES/M201Fall08/HandoutsAndHomework/Graph1.pdf) (PDF) on 2020-07-28. Retrieved 2020-07-28.

[^6]: ["The Fundamental Groups of Connected Graphs - Mathonline"](http://mathonline.wikidot.com/the-fundamental-groups-of-connected-graphs). *mathonline.wikidot.com*. Retrieved 2020-07-28.

[^7]: [Strom (2011](#CITEREFStrom2011), Problem 9.30, 9.31), [Hall (2015](#CITEREFHall2015), Exercise 13.7)

[^8]: Proof: Given two loops ${\displaystyle \alpha ,\beta :[0,1]\to G}$ in ${\displaystyle \pi _{1}(G),}$ define the mapping ${\displaystyle A\colon [0,1]\times [0,1]\to G}$ by ${\displaystyle A(s,t)=\alpha (s)\cdot \beta (t),}$ multiplied pointwise in ${\displaystyle G.}$ Consider the homotopy family of paths in the rectangle from ${\displaystyle (s,t)=(0,0)}$ to ${\displaystyle (1,1)}$ that starts with the horizontal-then-vertical path, moves through various diagonal paths, and ends with the vertical-then-horizontal path. Composing this family with ${\displaystyle A}$ gives a homotopy ${\displaystyle \alpha *\beta \sim \beta *\alpha ,}$ which shows the fundamental group is abelian.

[^9]: [Fulton (1995](#CITEREFFulton1995), Prop. 12.22)

[^10]: [May (1999](#CITEREFMay1999), Ch. 2, §8, Proposition)

[^11]: [May (1999](#CITEREFMay1999), Ch. 2, §7)

[^12]: [Hatcher (2002](#CITEREFHatcher2002), §1.3)

[^13]: [Hatcher (2002](#CITEREFHatcher2002), p. 65)

[^14]: [Hatcher (2002](#CITEREFHatcher2002), Proposition 1.36)

[^15]: [Forster (1981](#CITEREFForster1981), Theorem 27.9)

[^16]: [Hatcher (2002](#CITEREFHatcher2002), Prop. 4.61)

[^17]: [Hatcher (2002](#CITEREFHatcher2002), Theorem 4.41)

[^18]: [Hall (2015](#CITEREFHall2015), Proposition 13.8)

[^19]: [Hall (2015](#CITEREFHall2015), Section 13.3)

[^20]: [Hall (2015](#CITEREFHall2015), Proposition 13.10)

[^21]: [Bump (2013](#CITEREFBump2013), Prop. 23.7)

[^22]: [Hall (2015](#CITEREFHall2015), Corollary 13.18)

[^23]: [Hall (2015](#CITEREFHall2015), Example 13.45)

[^24]: [Singer, Isadore](https://en.wikipedia.org/wiki/Isadore_Singer "Isadore Singer"); Thorpe, John A. (1967). [*Lecture notes on elementary topology and geometry*](https://archive.org/details/lecturenotesonel00sing_949). Springer-Verlag. p. [98](https://archive.org/details/lecturenotesonel00sing_949/page/n101). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-90202-3](https://en.wikipedia.org/wiki/Special:BookSources/0-387-90202-3 "Special:BookSources/0-387-90202-3").

[^25]: [André Weil](https://en.wikipedia.org/wiki/Andr%C3%A9_Weil "André Weil"), *On discrete subgroups of Lie groups*, [Annals of Mathematics](https://en.wikipedia.org/wiki/Annals_of_Mathematics "Annals of Mathematics") **72** (1960), 369-384.

[^26]: Adam Przezdziecki, Measurable cardinals and fundamental groups of compact spaces, Fundamenta Mathematicae 192 (2006), 87-92 [\[1\]](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/192/1/89233/measurable-cardinals-and-fundamental-groups-of-compact-spaces)

[^27]: [Hatcher (2002](#CITEREFHatcher2002), §4.1)

[^28]: [Adams (1978](#CITEREFAdams1978), p. 5)

[^29]: [Brown (2006](#CITEREFBrown2006), §6.1)

[^30]: [Brown (2006](#CITEREFBrown2006), §6.2)

[^31]: [Crowell & Fox (1963)](#CITEREFCrowellFox1963) use a different definition by reparametrizing the paths to length *1*.

[^32]: [Brown (2006](#CITEREFBrown2006), §6.7)

[^33]: [El Zein et al. (2010](#CITEREFEl_ZeinSuciuTosunUludağ2010), p. 117, Prop. 1.7)

[^34]: [Grothendieck & Raynaud (2003)](#CITEREFGrothendieckRaynaud2003).

[^35]: [Grothendieck & Raynaud (2003](#CITEREFGrothendieckRaynaud2003), Exposé XII, Cor. 5.2).

[^36]: [Humphreys (1972](#CITEREFHumphreys1972), §13.1)

[^37]: [Humphreys (2004](#CITEREFHumphreys2004), §31.1)

[^38]: [Goerss & Jardine (1999](#CITEREFGoerssJardine1999), §I.7)

[^39]: [Goerss & Jardine (1999](#CITEREFGoerssJardine1999), §I.11)