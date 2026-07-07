---
title: "Appendix:Glossary of graph theory - Wiktionary, the free dictionary"
source: "https://en.wiktionary.org/wiki/Appendix:Glossary_of_graph_theory"
author:
published:
created: 2026-04-10
description:
tags:
  - "clippings"
---
This is a glossary of [graph theory](https://en.wiktionary.org/wiki/graph_theory "graph theory") —a mathematical theory of graphs consisting of vertices and edges that connect vertices.

**Contents:** [A](#A) [B](#B) [C](#C) [D](#D) [E](#E) [F](#F) [G](#G) [H](#H) [I](#I) [J](#J) [K](#K) [L](#L) [M](#M) [N](#N) [O](#O) [P](#P) [Q](#Q) [R](#R) [S](#S) [T](#T) [U](#U) [V](#V) [W](#W) [X](#X) [Y](#Y) [Z](#Z)

## A

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/250px-6n-graf.svg.png)

An illustration of a graph

acyclic

Of graph, such one that it does not contain any directed cycle. A finite, acyclic digraph with no isolated vertices necessarily contain at least one source and at least one sink. See also [directed acyclic graph](https://en.wiktionary.org/wiki/directed_acyclic_graph "directed acyclic graph") (DAG for short) for more.

acyclic graph

A graph that contains no cycles.

adjacent

Two edges are adjacent if they have a node in common; two nodes are adjacent if they have an edge in common.

anti-edge

An edge that "is not there". More formally, for two vertices ${\displaystyle u}$ and ${\displaystyle v}$, ${\displaystyle \{u,v\}}$ is an **anti-edge** in a graph ${\displaystyle G}$ if ${\displaystyle (u,v)}$ is not an edge in ${\displaystyle G}$. This means that there is either no edge between the two vertices or there is only an edge ${\displaystyle (v,u)}$ from ${\displaystyle v}$ to ${\displaystyle u}$ if ${\displaystyle G}$ is directed.

anti-triangle

A set of three vertices none of which are connected.

arborescence

(also *out-tree* or *branching*) An oriented tree in which all vertices are reachable from a single vertex. Likewise, an *in-tree* is an oriented tree in which a single vertex is reachable from every other one.

adjacency matrix

In computers, a finite, directed or undirected graph (with *n* vertices, say) is often represented by its **[adjacency matrix](https://en.wiktionary.org/wiki/adjacency_matrix "adjacency matrix")**: an *n* -by- *n* [matrix](https://en.wiktionary.org/w/index.php?title=matrix_\(mathematics\)&action=edit&redlink=1 "matrix (mathematics) (page does not exist)") whose entry in row *i* and column *j* gives the number of edges from the *i* -th to the *j* -th vertex.

adjacent

Two vertices *u* and *v* are considered **adjacent** if an edge exists between them. We denote this by *u* ↓ *v*. In the above graph, vertices 1 and 2 are adjacent, but vertices 2 and 4 are not. The set of **neighbors**, called a **(open) neighborhood** *N <sub>G</sub>* (*v*) for a vertex *v* in a graph *G*, consists of all vertices adjacent to *v* but not including *v*. When *v* is also included, it is called a **closed neighborhood**, denoted by *N <sub>G</sub>* \[*v*\]. When stated without any qualification, a neighborhood is assumed to be open. The subscript *G* is usually dropped when there is no danger of confusion. In the example graph, vertex 1 has two neighbors: vertices 2 and 5. For a simple graph, the number of neighbors that a vertex has coincides with its degree.

arc

(also *directed edge*) An ordered pair of endvertices.

articulation point

A cut vertex.

## B

balanced *k* -partite graph

A *k* -partite graph such that each partite set differs in size by at most 1 with any other.

biclique

A [*complete bipartite graph*](https://en.wiktionary.org/wiki/complete_bipartite_graph "complete bipartite graph").

biconnected component

A maximal set of edges in which any two members lie on a common simple cycle.

bipartite graph

A graph that can be decomposed into two partite sets but not fewer.

biregular graph

A graph that has unequal maximum and minimum degrees and every vertex has one of those two degrees.

block

Either a maximally 2-connected subgraph or a bridge with its endvertices.

bond

A minimal (but not necessarily minimum), nonempty set of edges whose removal disconnects a graph.

bridge

An edge whose removal disconnects a graph. (For example, a tree is made entirely of bridges.)

## C

center

A vertex with minimum eccentricity.

circuit

A circuit of *n* vertices, denoted by *C <sub>n</sub>*, is usually assumed to be a **simple cycle**, or a *simple circuit*, meaning that every vertex is incident to exactly two edges. In the above graph (1, 5, 2, 1) is a simple cycle.

circumference

The length of a longest (simple) cycle, or infinity if the graph is acyclic.

claw

An induced star with 3 edges.

[clique](https://en.wiktionary.org/wiki/clique "clique")

In a graph, a set of pairwise adjacent vertices. Since any subgraph induced by a clique is a complete subgraph, the two terms and their notations are usually used interchangeably.

*k* -clique

A clique of order *k*. In the example graph above, vertices 1, 2 and 5 form a 3-clique, or a *triangle*.

clique number

ω(*G*) of a graph *G*, the order of a largest clique in *G*.

color, colored, identified

Nodes or edges which are considered as individuals. Although they may actually be rendered in diagrams in different colors, working mathematicians generally pencil in numbers or letters.

*k* -colorable graph'

A graph that can be decomposed into *k* partite sets.

complement

${\displaystyle {\bar {G}}}$ of a graph *G* is a graph with the same vertex set as *G* but with an edge set such that *xy* is an edge in ${\displaystyle {\bar {G}}}$ if and only if *xy* is not an edge in *G*.

complete

A graph in which every node is linked to every other node. For a complete digraph, this means one link in either direction.

[complete graph](https://en.wiktionary.org/wiki/complete_graph "complete graph")

*K <sub>n</sub>* of order *n*, a simple graph with *n* vertices in which every vertex is adjacent to every other. The example graph is not complete. The complete graph on *n* vertices is often denoted by *K <sub>n</sub>*. It has *n* (*n* -1)/2 edges (corresponding to all possible choices of pairs of vertices).

complete multipartite graph

A graph in which vertices are adjacent if and only if they belong to different partite sets.

component

A maximally connected subgraph.

connected

If some route exists from every node to every other, the graph is connected. Note that some graphs are *not* connected. A diagram of an unconnected graph may look like two or more unrelated diagrams, but all the nodes and edges shown are considered as one graph.

[connectivity](https://en.wiktionary.org/wiki/connectivity "connectivity")

extends the concept of adjacency and is essentially a form (and measure) of *concatenated adjacency*.

connected graph

If it is possible to establish a path from any vertex to any other vertex of a graph, the graph is said to be **connected**.

k-connected

If it is always possible to establish a path from any vertex to every other one even after removing any *k* - 1 vertices, then the graph is said to be ***k* -connected**. Note that a graph is *k* -connected if and only if it contains *k* internally disjoint paths between any two vertices. The example graph above is connected (and therefore 1-connected), but not 2-connected.

connectivity

κ(*G*) of a graph *G* is the minimum number of vertices needed to disconnect *G*. By convention, *K <sub>n</sub>* has connectivity *n* - 1; and a disconnected graph has connectivity 0.

crossing

A pair of intersecting edges.

crossing number

The minimum number of crossings that must appear when a graph is drawn on a plane is called the **crossing number**.

[cut](https://en.wiktionary.org/wiki/cut "cut")

A partition of the vertices of a graph into two disjoint subsets.

cut edge

A bridge.

cut set

A set of vertices whose removal disconnects the graph.

[cut vertex](https://en.wiktionary.org/w/index.php?title=cut_vertex&action=edit&redlink=1 "cut vertex (page does not exist)")

A vertex whose removal disconnects a graph. Also known as Cut Point or Articulation Point. See also cut set and bridge.

[cycle](https://en.wiktionary.org/wiki/cycle "cycle")

In a graph was a closed walk.

## D

[DAG](https://en.wiktionary.org/wiki/DAG "DAG")

A directed acyclic graph.

[degree](https://en.wiktionary.org/wiki/degree "degree")

The number of edges which connect a node.

degree

d <sub>G</sub> (*v*) of a vertex *v* in a graph *G* is the number of edges incident to *v*, with loops being counted twice. A vertex of degree 0 is an isolated vertex. A vertex of degree 1 is a leaf. In the example graph vertices 1 and 3 have a degree of 2, vertices 2,4 and 5 have a degree of 3 and vertex 6 has a degree of 1. If *E* is finite, then the total sum of vertex degrees is equal to twice the number of edges.

degree sequence

A list of degrees of a graph in non-increasing order (e.g. *d* <sub>1</sub> ≥ *d* <sub>2</sub> ≥ … ≥ *d <sub>n</sub>*). A sequence of non-increasing integers is **realizable** if it is a degree sequence of some graph.

[diagram](https://en.wiktionary.org/wiki/diagram "diagram")

A visible rendering of the abstract concept of a graph.

[diameter](https://en.wiktionary.org/wiki/diameter "diameter")

The maximum eccentricity over all vertices in a graph. It is denoted diam(*G*) of a graph *G*.

[digraph](https://en.wiktionary.org/wiki/digraph "digraph")

A directed graph.

directed cycle

(also *cycle*) An oriented simple cycle such that all arcs go the same direction, meaning all vertices have in- and out-degrees 1.

directed

A graph in which each edge symbolizes an ordered, non-transitive relationship between two nodes. Such edges are rendered with an arrowhead at one end of a line or arc.

directed graph

A graph whose edges are directed, possibly represented as ordered pairs of vertices; synonyms: digraph. Alternative models of *graph* exist; e.g., a graph may be thought as a [Boolean](https://en.wiktionary.org/wiki/Boolean "Boolean") [binary function](https://en.wiktionary.org/wiki/binary_function "binary function") over the set of vertices or as a square (0,1)- [matrix](https://en.wiktionary.org/wiki/matrix "matrix").

disconnected graph

A graph that is not connected.

disconnecting set

A set of edges whose removal increases the number of components.

distance

*d* <sub><i>G</i></sub> (*u*, *v*) between two (not necessary distinct) vertices *u* and *v* in a graph *G* is the length of a shortest path between them. The subscript *G* is usually dropped when there is no danger of confusion. When *u* and *v* are identical, their distance is 0. When *u* and *v* are unreachable from each other, their distance is defined to be [infinity](https://en.wiktionary.org/wiki/infinity "infinity") ∞.

dominate

A vertex *v* **dominates** another vertex *u* if there is an arc from *v* to *u*. A vertex subset *S* is **out-dominating** if every vertex not in *S* is dominated by some vertex in *S*; and **in-dominating** if every vertex in *S* is dominated by some vertex not in *S*.

dominating set

Of a graph, a vertex subset whose closed neighborhood include all vertices of the graph. A vertex *v* **dominates** another vertex *u* if there is an edge from *v* to *u*. A vertex subset *V* **dominates** another vertex subset *U* if every vertex in *U* is adjacent to some vertex in *V*. The minimum size of a dominating set is the **domination number** γ(*G*).

dual

A **dual**, or *planar dual* when the context needs to be clarified, *G* <sup>*</sup> of a plane graph *G* is a graph whose vertices represent the faces, including any outerface, of *G* and are adjacent in *G* <sup>*</sup> if and only if their corresponding faces are adjacent in *G*. The dual of a planar graph is always a planar *pseudograph* (e.g. consider the dual of a triangle). In the familiar case of a 3-connected simple planar graph *G* (isomorphic to a convex [polyhedron](https://en.wiktionary.org/wiki/polyhedron "polyhedron") *P*), the dual *G* <sup>*</sup> is also a 3-connected simple planar graph (and isomorphic to the dual polyhedron *P* <sup>*</sup>).

## E

eccentricity

ε <sub><i>G</i></sub> (*v*) of a vertex *v* in a graph *G* is the maximum distance from *v* to any other vertex.

edge

A set of two elements, drawn as a *line* connecting two vertices, called **endvertices**, or *endpoints*. An edge with endvertices *x* and *y* is denoted by *xy* without any symbol in between, so, do not write *x* ⋅ *y*. The **edge set** of *G* is usually denoted by *E* (*G*), or *E* when there is no danger of confusion.

edge, link, arc

Relationships represented in a graph. These are always rendered as straight or curved lines. The term "arc" may be misleading.

edge cut

The set of all edges having one endvertex in some proper vertex subset *S* and another endvertex in *V* (*G*)\\ *S*. Edges of *K* <sub>3</sub> form a disconnecting set but not an edge cut. Any two edges of *K* <sub>3</sub> form a minimal disconnecting set as well as an edge cut. An edge cut is necessarily a disconnecting set; and a minimal disconnecting set of an nonempty graph is necessarily an edge cut.

edgeless graph

(**empty graph**) A graph possibly with some vertices, but no edges. Or, it is a graph with no vertices and no edges.

k-edge-connected

Of a graph, such that if any subgraph formed by removing any *k* - 1 edges is still connected. The **edge connectivity** κ′(*G*) of a graph *G* is the minimum number of edges needed to disconnect *G*. One well-known result is that κ(*G*) ≤ κ′(*G*) ≤ δ(*G*).

embeddable

A graph is **embeddable** on a surface if its vertices and edges can be arranged on it without any crossing. The **genus** of a graph is the lowest [genus](https://en.wiktionary.org/w/index.php?title=genus_\(mathematics\)&action=edit&redlink=1 "genus (mathematics) (page does not exist)") of any surface on which the graph can embed.

embedding

${\displaystyle G_{1}=(V_{1},E_{1})}$ of ${\displaystyle G_{2}=(V_{2},E_{2})}$ is an [injection](https://en.wiktionary.org/wiki/injective_function "injective function") from ${\displaystyle V_{2}}$ to ${\displaystyle V_{1}}$ such that every edge in ${\displaystyle E_{2}}$ corresponds to a path(disjoint from all other such paths) in ${\displaystyle G_{1}}$.

equipartite graph

A *k* -partite graph such that each partite set has the same size.

Eulerian circuit

Eulerian cycle.

[Eulerian cycle](https://en.wiktionary.org/wiki/Eulerian_cycle "Eulerian cycle")

A closed walk which uses each edge precisely once.

Eulerian digraph

A digraph with equal in- and out-degrees at every vertex.

[Eulerian path](https://en.wiktionary.org/wiki/Eulerian_path "Eulerian path")

A path which passes through every edge (once and only once). If the starting and ending nodes are the same, it is an **Euler cycle** or an **Euler circuit**. If the starting and ending nodes are different, it is an **Euler trail**.

[Eulerian path](https://en.wiktionary.org/wiki/Eulerian_path "Eulerian path")

A graph is a walk that uses each edge precisely once; that is, a trail that uses all the edges. If such a trail exists, the graph is called **traversable**.

Eulerian trail

Eulerian path.

Eulerian tour

Eulerian cycle.

even cycle

A cycle that has an even length.

## F

face

When a graph is drawn without any crossing, any cycle that surrounds a region without any edge reaching from the cycle inside to such region forms a **face**. Two faces on a plane graph are **adjacent** if they share a common edge.

factor

A spanning subgraph.

*k* -factor

A *k* -regular spanning subgraph. An 1-factor is a *perfect matching*. A partition of edges of a graph into *k* -factors is called a ***k* -factorization**. A ***k* -factorable graph** is a graph that admits a *k* -factorization.

forest

A vertex-disjoint union of trees; or, equivalently, an acyclic graph.

## G

[girth](https://en.wiktionary.org/wiki/girth "girth")

Of a graph, the length of a shortest (simple) cycle in the graph, or infinity if the graph is acyclic.

graph, network

An abstraction of relationships among objects. Graphs consist exclusively of nodes and edges. All characteristics of a system are either eliminated or subsumed into these elements.

graph

A mathematical structure costiting of two types of elements, namely *vertices* and *edges*. Every edge has two *endpoints* in the set of vertices, ans is said to **connect** or **join** the two endpoints. The set of edges can thus be defined as a subset of the family of all two-element sets of vertices. Often, however, the set of vertices is considered as a set, and there is an **incidence relation** which maps each edge to the pair of vertices that are its endpoints.

[graph invariant](https://en.wiktionary.org/w/index.php?title=graph_invariant&action=edit&redlink=1 "graph invariant (page does not exist)")

A property of a graph *G*, usually a number or a polynomial, that depends only on the isomorphism class of *G*; examples are genus and graph order.

[graph labeling](https://en.wiktionary.org/w/index.php?title=graph_labeling&action=edit&redlink=1 "graph labeling (page does not exist)")

The assignment of unique labels (usually [natural numbers](https://en.wiktionary.org/wiki/natural_numbers "natural numbers")) to the edges and vertices of a graph. Graphs with labeled edges or vertices are known as **labeled**, those without as **unlabeled**. More specifically, graphs with labeled vertices only are **vertex-labeled**, those with labeled edges only are **edge-labeled**. (This usage is to distinguish between graphs with identifiable vertex or edge sets on the one hand, and isomorphism types or classes of graphs on the other.)

## H

[Hamiltonian cycle](https://en.wiktionary.org/wiki/Hamiltonian_cycle "Hamiltonian cycle")

A *spanning cycle*.

Hamiltonian graph

A graph that contains a Hamiltonian cycle.

[Hamiltonian path](https://en.wiktionary.org/wiki/Hamiltonian_path "Hamiltonian path")

A (simple) path that contains every vertex.

[Hamiltonian path](https://en.wiktionary.org/wiki/Hamiltonian_path "Hamiltonian path")

A path which passes through every node once and only once. If the starting and ending nodes are adjacent, it is a **Hamiltonian cycle**.

Hamiltonian path

A *spanning path*.

Hamiltonian connected graph

A graph that, given any pair of (distinct) vertices, contains a Hamiltonian path using them as endvertices.

H-free graf

A graph that does *not* contain *H* as an induced subgraph is said to be ***H* -free**.

head

The first vertex in the arc AKA directed edge. See also tail.

homomorphic

Likewise, a graph *G* is said to be **homomorphic** to a graph *H* if there is a mapping, called a [**homomorphism**](https://en.wiktionary.org/w/index.php?title=Graph_homomorphism&action=edit&redlink=1 "Graph homomorphism (page does not exist)"), from *V* (*G*) to *V* (*H*) such that if two vertices are adjacent in *G* then their corresponding vertices are adjacent in *H*.

hyperedge

An edge that is allowed to take on any number of vertices, possibly more than 2. A graph that allows any hyperedge is called a [**hypergraph**](https://en.wiktionary.org/wiki/hypergraph "hypergraph"). A simple graph can be considered a special case of the hypergraph, namely the 2-uniform hypergraph. However, when stated without any qualification, an edge is always assumed to consist of at most 2 vertices, and a graph is never confused with a hypergraph.

## I

in degree

The number of edges entering a vertex. Is denoted as *d* <sub>Γ</sub> <sup>-</sup> (*v*). The degree *d* <sub>Γ</sub> (*v*) of a vertex *v* is equal to the sum of its out- and in- degrees. When the context is clear, the subscript Γ can be dropped. Maximum and minimum out degrees are denoted by Δ <sup>+</sup> (Γ) and δ <sup>+</sup> (Γ); and maximum and minimum in degrees, Δ <sup>-</sup> (Γ) and δ <sup>-</sup> (Γ).

in-neighborhood

(*predecessor set*) *N* <sup>-</sup> <sub>Γ</sub> (*v*) of a vertex *v* is the set of heads of arc going into *v*.

incident

An edgee connects two vertices; these two vertices are said to be **incident** to that edge, or, equivalently, that edge incident to those two vertices. All degree-related concepts have to do with adjacency or incidence.

independence number

α(*G*) of a graph *G* is the size of a largest independent set of *G*.

independent

In graph theory, the word *independent* usually carries the connotation of *pairwise disjoint* or *mutually nonadjacent*. In this sense, independence is a form of *immediate nonadjacency*.

independent set

A set of isolated vertices. Since the graph induced by any independent set is an empty graph, the two terms are usually used interchangeably. In the example above, vertices 1, 3, and 6 form an independent set; and 3, 5, and 6 form another one.

induced subgraph

A subgraph *H* of a graph *G* is said to be **induced** if, for any pair of vertices *x* and *y* of H, *xy* is an edge of *H* if and only if *xy* is an edge of G. In other words, *H* is an induced subgraph of *G* if it has the most edges that appear in *G* over the same vertex set. If *H* is chosen based on a vertex subset *S* of *V(G)*, then *H* can be written as *G* \[*S*\] and is said to be **induced by *S***.

infinite

A graph is **infinite** if it has infinitely many vertices or edges or both; otherwise the graph is **finite**. An infinite graph where every vertex has finite degree is called **locally finite**. When stated without any qualification, a graph is usually assumed to be finite.

initial vertex

A head.

internally disjoint

Two paths are **internally disjoint** (some people call it *independent*) if they do not have any vertex in common, except the first and last ones.

isolated vertex

A vertex not incident to any edges.

isomorphic

Two graphs *G* and *H* are said to be **isomorphic**, denoted by *G* ~ *H*, if there is a one-to-one correspondence, called an **isomorphism**, between the vertices of the graph such that two vertices are adjacent in *G* if and only if their corresponding vertices are adjacent in *H*.

isthmus

A bridge.

## K

k-ary tree

A ***k* -ary** tree is a rooted tree in which every internal vertex has *k* *children*. An 1-ary tree is just a path. A 2-ary tree is also called a **binary tree**.

kernel

An independent out-dominating set. A digraph is **kernel perfect** if every induced sub-digraph has a kernel.

knot

In a directed graph, a collection of vertices and edges with the property that every vertex in the knot has outgoing edges, and all outgoing edges from vertices in the knot have other vertices in the knot as destinations. Thus it is impossible to leave the knot while following the directions of the edges.

## L

length of a cycle

The number of its edges. *C <sub>n</sub>* has length *n*. A cycle, unlike a path, is not allowed to have length 0.

length of a path or walk

The number of edges that the path uses. *P <sub>n</sub>* has length *n* - 1. Some people count multiple edges multiple times. In the example graph, (1, 2, 5, 1, 2, 3) is a path with length 5, and (5, 2, 1) is a simple path of length 2.

link

has two distinct endvertices.

digon

A cycle of length 2. In the example graph, (1, 2, 3, 4, 5, 1) is a cycle of length 5.

loop

An edge whose endvertices are the same vertex.

loop, cycle

A path which ends at the node where it began.

## M

matching number

α′(*G*) of a graph *G* is a the size of a largest **matching**, or pairwise vertex disjoint edges, of *G*.

maximum degree

Δ(*G*) of a graph *G*, the largest degree over all vertices; the **minimum degree** δ(*G*), the smallest.

[minor](https://en.wiktionary.org/wiki/minor "minor")

${\displaystyle G_{2}=(V_{2},E_{2})}$ of ${\displaystyle G_{1}=(V_{1},E_{1})}$ is an [injection](https://en.wiktionary.org/wiki/injective_function "injective function") from ${\displaystyle V_{2}}$ to ${\displaystyle V_{1}}$ such that every edge in ${\displaystyle E_{2}}$ corresponds to a path(disjoint from all other such paths) in ${\displaystyle G_{1}}$ such that every vertex in ${\displaystyle V_{1}}$ is in one or more paths, or is part of the injection from ${\displaystyle V_{1}}$ to ${\displaystyle V_{2}}$. This can alternatively be phrased in terms of *contractions*, which are operations which collapse a path and all vertices on it into a single edge (see [edge contraction](https://en.wiktionary.org/wiki/edge_contraction "edge contraction")).

multiple

A set of arcs are **multiple**, or *parallel*, if they share the same head and the same tail. A pair of arcs are **anti-parallel** if one's head/tail is the other's tail/head.

multiple edge

An edge such that there is another edge with the same endvertices; antonyms: **simple edge**. The **multiplicity of an edge** is the number of multiple edges sharing the same endvertices; the **multiplicity of a graph**, the maximum multiplicity of its edges.

multigraph

A graph that has multiple edges, but no loops.

multipartite graph

A graph that can be decomposed into an unspecific number of partite sets but not fewer.

## N

network

A weighted graph, possibly directed or undirected, possibly containing special vertices (nodes), such as **source** or **sink**.

null graph

The graph with no vertices and no edges. Or, it is a graph with no edges and any number ${\displaystyle n}$ of vertices, in which case it may be called the **null graph on ${\displaystyle n}$ vertices**. (There is no consistency at all in the literature.)

## O

odd cycle

A cycle that has odd length.

order

The order of a graph is the number of its vertices, i.e. | *V* (*G*)|.

orientation

An assignment of directions to the edges of an undirected or partially directed graph. When stated without any qualification, it is usually assumed that all undirected edges are replaced by a directed one in an orientation. Also, the underlying graph is usually assumed to be undirected and simple.

oriented graph

A graph that contains only arcs. When stated without any qualification, a graph is almost always assumed to be undirected. Also, a digraph is usually assumed to contain no undirected edges.

out degree

The number of edges leaving a vertex. Is denoted *d* <sub>Γ</sub> <sup>+</sup> (*v*), given a digraph Γ. See also in degree.

out-neighborhood

(*successor set*) *N* <sup>+</sup> <sub>Γ</sub> (*v*) of a vertex *v* is the set of tails of arcs going from *v*.

outer face

Furthermore, since we can establish a sense of "inside" and "outside" on a plane, we can identify an "outermost" region that contains the entire graph if the graph does not cover the entire plane. Such outermost region is called an **outer face**.

outerplanar graph

A graph that *can be* drawn in the planar fashion such that its vertices are all adjacent to the outer face. See also outerplane graph.

outerplane graph

A graph that *is* drawn in the planar fashion such that its vertices are all adjacent to the outer face. See also outerplanar graph.

## P

pancyclic graph

A graph that contains cycles of every possible length (from 3 to the order of the graph).

*k* -partite graph

A graph that can be decomposed into *k* partite sets but not fewer.

partite set

A graph can be **decomposed** into independent sets in the sense that the entire vertex set of the graph can be partitioned into pairwise disjoint independent subsets. Such independent subsets are called **partite sets**, or simply *parts*.

path

A **directed path**, or just a *path* when the context is clear, is an oriented simple path such that all arcs go the same direction, meaning all internal vertices have in- and out-degrees 1.

path

A route that does not pass any edge more than once. If the path does not pass any node more than once, it is a **simple path**.

path

In a graph was what is now usually known as an *open walk*. Nowadays, when stated without any qualification, a **path** of *n* vertices, denoted by *P* <sub><i>n</i></sub> (but some write *P* <sub><i>n</i> -1</sub>), is usually defined to be a **simple path** or a *simple trail* in the old sense, meaning that every vertex is incident to at most two edges.

perfect matching

A spanning matching.

peripheral vertex

A vertex with maximum eccentricity.

[planar graph](https://en.wiktionary.org/wiki/planar_graph "planar graph")

A graph that *can be* drawn on the (Euclidean) plane without any crossing; a graph of genus 0.

plane graph

A graph that *is* drawn on the (Euclidean) plane without any crossing.

point, node, vertex

Objects ("things") represented in a graph. These are almost always rendered as round dots.

k-th power

*G <sup>k</sup>* of a graph *G* is a supergraph formed by adding an edge between all pairs of vertices of *G* with distance at most *k*. A *second power* of a graph is also called a **square**.

pseudograph

A graph that contains both multiple edges and loops (the literature is highly inconsistent).

## R

radius

The minimum eccentricity over all vertices in a graph. It is denoted rad(*G*) of a graph *G*. When there are two components in *G*, diam(*G*) and rad(*G*) defined to be infinity ∞.

reachable

Of a vertex *v* from a given vertex *u* in a directed graph, such that there is a directed path that starts from *u* and ends at *v*.

regular

A graph in which each node has the same degree.

regular graph

A graph in which every vertex has the same degree.

*k* -regular graph

A graph in which every vertex has degree *k*. A 0-regular graph is an independent set. A 1-regular graph is a matching. A 2-regular graph is a vertex disjoint union of cycles. A 3-regular graph is said to be **cubic**, or *trivalent*.

route

A sequence of edges and nodes from one node to another. Any given edge or node might be used more than once.

## S

separating set

A cut set.

simple

A digraph is called **simple** if it has no loops and at most one arc between any pair of vertices. When stated without any qualification, a digraph is usually assumed to be simple.

simple graph

A graph that has no multiple edges or loops. When stated without any qualification, a graph is almost always assumed to be simple. See also multigraph.

sink

A vertex of a network with out-degree of zero; see also source.

size of a graph

The number of its edges, i.e. | *E* (*G*)|.

source

A vertex of a network with in-degree of zero; see also sink.

k-spanner

A spanning subgraph in which every two vertices are at most *k* times as far apart on S than on G. The number *k* is the **dilation**. *k* -spanner is used for studying geometric network optimization.

spanning subgraph

A subgraph *H* of a graph *G* such that it has the same vertex set as *G*. We say *H* spans *G*.

[spanning tree](https://en.wiktionary.org/wiki/spanning_tree "spanning tree")

A spanning subgraph that is a tree. Every graph has a spanning forest. But only a connected graph has a spanning tree.

star

A special kind of tree called **star** is *K* <sub>1,<i>k</i></sub>; see also claw.

strongly connected

A digraph is **strongly connected** if every vertex is reachable from every other following the directions of the arcs. On the contrary, a diagraph is **weakly connected** if its underlying undirected graph is connected. A weakly connected graph can be thought of as a digraph in which every vertex is "reachable" from every other but not necessarily following the directions of the arcs. A **strong orientation** is an orientation that produces a strongly connected digraph.

strongly connected component

Informally, a subgraph where all nodes in the subgraph are reachable by all other nodes in the subgraph.

subtree

of the graph *G* is a subgraph that is a tree.

subgraph

Of a graph *G* is a graph whose vertex and edge sets are subsets of those of *G*. In the other direction, a **supergraph** of a graph *G* is a graph that contains *G* as a subgraph. We say a graph *G* **contains** another graph *H* if some subgraph of *G* is *H* or is isomorphic to *H* (depending on the needs of the situation).

semiregular

A *k* -partite graph is **semiregular** if each of its partite set has a uniform degree

spanning matching

A matching that covers all vertices of a graph.

stable set

An independent set.

staset

A stable set.

strongly regular graph

A regular graph such that any adjacent vertices have the same number of common neighbors as other adjacent pairs and that any nonadjacent vertices have the same number of common neighbors as other nonadjacent pairs.

## T

tail

The second vertex in the arc AKA directed edge. See also head.

terminal vertex

tail.

theta graph

The union of three internally disjoint (simple) paths that have the same two distinct endvertices. A **theta <sub>0</sub> graph** has seven vertices which can be arranged as the vertices of a regular hexagon plus an additional vertex in the center. The eight edges are the perimeter of the hexagon plus one diameter.

thickness

The minimum number of planar graphs needed to cover a graph is the **thickness** of the graph.

totally disconnected graph

A graph is **totally disconnected** if there is no path connecting any pair of vertices. This is just another name to describe an empty graph or independent set.

tournament

A digraph in which each pair of vertices is connected by exactly one arc. In other words, it is an oriented complete graph.

traceable graph

A graph that contains a Hamiltonian path.

traceable path

A *spanning path*.

trail

A walk in which all the edges are distinct. (A closed trail has been called a **tour** or **circuit**, but these are uncommon and the latter is usually reserved for a regular subgraph of degree two.)

tree

A connected graph with no loops.

[tree](https://en.wiktionary.org/wiki/tree "tree")

A connected acyclic simple graph. A vertex of degree 1 is called a **leaf**, or *pendant vertex*. An edge incident to a leaf is an **leaf edge**, or *pendant edge*. (Some people define a leaf edge as a *leaf* and then define a *leaf vertex* on top of it. These two sets of definitions are often used interchangeably.) A non-leaf vertex is an **internal vertex**. Sometimes, one vertex of the tree is distinguished, and called the **root**. A **rooted tree** is a tree with a root. **Rooted trees** are often treated as **directed acyclic graphs** with the edges pointing away from the root. Trees are commonly used as [data structures](https://en.wiktionary.org/wiki/data_structure "data structure") in computer science (see [tree data structure](https://en.wiktionary.org/w/index.php?title=tree_data_structure&action=edit&redlink=1 "tree data structure (page does not exist)")).

triangle

*C* <sub>3</sub> is called a **triangle**.

tripartite graph

A graph that can be decomposed into three partite sets but not fewer.

## U

undirected edge

An edge that disregards any sense of direction and treats both endvertices interchangeably.

undirected

A graph in which each edge symbolizes an unordered, transitive relationship between two nodes. Such edges are rendered as plain lines or arcs.

unicyclic graph

A graph that contains exactly one cycle.

unidentified

Nodes or edges which are not considered as individuals. Only the way in which they connect to the rest of the graph characterize unidentified nodes and edges.

universal graph

In a class ***K*** of graphs, a simple graph in which every element in ***K*** can be embedded as a subgraph.

unweighted

A graph in which all the relationships symbolized by edges are considered equivalent. Such edges are rendered as plain lines or arcs.

## V

valency

A degree.

vertex

A basic element of a graph, drawn as a *node* or a *dot*. The **vertex set** of *G* is usually denoted by *V* (*G*), or *V* when there is no danger of confusion.

vertex cut

A cut set.

## W

walk

An alternating sequence of vertices and edges, beginning and ending with a vertex, in which each vertex is incident to the two edges that precede and follow it in the sequence, and the vertices that precede and follow an edge are the endvertices of that edge. A walk is **closed** if its first and last vertices are the same, and **open** if they are different.

weighted

Weighted edges symbolize relationships between nodes which are considered to have some value, for instance, distance or lag time. Such edges are usually annotated by a number or letter placed beside the edge. Weighted nodes also have some value; this must be distinguished from identification.

weighted graph

A graph that associates a label (**weight**) with every edge in the graph. Weights are usually [real numbers](https://en.wiktionary.org/wiki/real_number "real number"). They may be restricted to rational numbers or integers. Certain algorithms require further restrictions on weights; for instance, the Dijkstra algorithm works properly only for positive weights.

weight of a subgraph

The sum of the weights of the edges of the subgraph.

Wiener index of a vertex

*v* in a graph *G*, denoted by *W <sub>G</sub>* (*v*) is the sum of distances between *v* and all others.

Wiener index of a graph

*G*, denoted by *W* (*G*), is the sum of distances over all pairs of vertices.