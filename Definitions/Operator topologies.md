---
title: "Operator topologies"
source: "https://en.wikipedia.org/wiki/Operator_topologies"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2004-02-29
created: 2026-04-10
description:
tags:
  - "clippings"
---
In the [mathematical](https://en.wikipedia.org/wiki/Mathematics "Mathematics") field of [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis "Functional analysis") there are several standard [topologies](https://en.wikipedia.org/wiki/Topology "Topology") which are given to the algebra B(*X*) of [bounded linear operators](https://en.wikipedia.org/wiki/Bounded_linear_operator "Bounded linear operator") on a [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space") X.

## Introduction

Let ${\displaystyle (T_{n})_{n\in \mathbb {N} }}$ be a sequence of linear operators on the Banach space ${\displaystyle X}$. Consider the statement that ${\displaystyle (T_{n})_{n\in \mathbb {N} }}$ converges to some operator ${\displaystyle T}$ on ${\displaystyle X}$. This could have several different meanings:

- If ${\displaystyle \|T_{n}-T\|\to 0}$, that is, the [operator norm](https://en.wikipedia.org/wiki/Operator_norm "Operator norm") of ${\displaystyle T_{n}-T}$ (the supremum of ${\displaystyle \|T_{n}x-Tx\|_{X}}$, where ${\displaystyle x}$ ranges over the [unit ball](https://en.wikipedia.org/wiki/Unit_ball "Unit ball") in ${\displaystyle X}$) converges to ${\displaystyle 0}$, we say that ${\displaystyle T_{n}\to T}$ in the **[uniform operator topology](https://en.wikipedia.org/wiki/Uniform_operator_topology "Uniform operator topology")**.
- If ${\displaystyle T_{n}x\to Tx}$ for all ${\displaystyle x\in X}$, then we say ${\displaystyle T_{n}\to T}$ in the **[strong operator topology](https://en.wikipedia.org/wiki/Strong_operator_topology "Strong operator topology")**.
- Finally, suppose that for all ${\displaystyle x\in X}$ we have ${\displaystyle T_{n}x\to Tx}$ in the [weak topology](https://en.wikipedia.org/wiki/Weak_topology "Weak topology") of ${\displaystyle X}$. This means that ${\displaystyle F(T_{n}x)\to F(Tx)}$ for all continuous linear functionals ${\displaystyle F}$ on ${\displaystyle X}$. In this case we say that ${\displaystyle T_{n}\to T}$ in the **[weak operator topology](https://en.wikipedia.org/wiki/Weak_operator_topology "Weak operator topology")**.

## List of topologies on B(H)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Optop.svg/250px-Optop.svg.png)

Diagram of relations among topologies on the space B( X ) of bounded operators

There are many topologies that can be defined on B(*X*) besides the ones used above; most are at first only defined when *X* = *H* is a Hilbert space, even though in many cases there are appropriate generalisations. The topologies listed below are all locally convex, which implies that they are defined by a family of [seminorms](https://en.wikipedia.org/wiki/Seminorm "Seminorm").

In analysis, a topology is called strong if it has many open sets and weak if it has few open sets, so that the corresponding modes of convergence are, respectively, strong and weak. (In topology proper, these terms can suggest the opposite meaning, so strong and weak are replaced with, respectively, fine and coarse.) The diagram on the right is a summary of the relations, with the arrows pointing from strong to weak.

If H is a Hilbert space, the linear space of [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space") operators B(*X*) has a (unique) [predual](https://en.wikipedia.org/wiki/Predual "Predual") ${\displaystyle B(H)_{*}}$, consisting of the trace class operators, whose dual is B(*X*). The seminorm *p* <sub><i>w</i></sub> (*x*) for *w* positive in the predual is defined to be B(*w*, *x <sup>*</sup> x*) <sup>1/2</sup>.

If B is a vector space of linear maps on the vector space A, then σ(*A*, *B*) is defined to be the weakest topology on A such that all elements of B are continuous.

- The **[norm topology](https://en.wikipedia.org/wiki/Norm_topology "Norm topology")** or **uniform topology** or **uniform operator topology** is defined by the usual norm || *x* || on B(*H*). It is stronger than all the other topologies below.
- The **[weak (Banach space) topology](https://en.wikipedia.org/wiki/Weak_topology "Weak topology")** is σ(B(*H*), B(*H*) <sup>*</sup>), in other words the weakest topology such that all elements of the dual B(*H*) <sup>*</sup> are continuous. It is the weak topology on the Banach space B(*H*). It is stronger than the ultraweak and weak operator topologies. (Warning: the weak Banach space topology and the weak operator topology and the ultraweak topology are all sometimes called the weak topology, but they are different.)
- The **[Mackey topology](https://en.wikipedia.org/wiki/Mackey_topology "Mackey topology")** or **Arens-Mackey topology** is the strongest locally convex topology on B(*H*) such that the dual is B(*H*) <sub>*</sub>, and is also the uniform convergence topology on Bσ(B(*H*) <sub>*</sub>, B(*H*)-compact convex subsets of B(*H*) <sub>*</sub>. It is stronger than all topologies below.
- The **σ-strong- <sup>*</sup> topology** or **ultrastrong- <sup>*</sup> topology** is the weakest topology stronger than the ultrastrong topology such that the adjoint map is continuous. It is defined by the family of seminorms *p* <sub><i>w</i></sub> (*x*) and *p* <sub><i>w</i></sub> (*x* <sup>*</sup>) for positive elements w of B(*H*) <sub>*</sub>. It is stronger than all topologies below.
- The **σ-strong topology** or **[ultrastrong topology](https://en.wikipedia.org/wiki/Ultrastrong_topology "Ultrastrong topology")** or **strongest topology** or **strongest operator topology** is defined by the family of seminorms *p* <sub><i>w</i></sub> (*x*) for positive elements w of B(*H*) <sub>*</sub>. It is stronger than all the topologies below other than the strong <sup>*</sup> topology. Warning: in spite of the name "strongest topology", it is weaker than the norm topology.)
- The **σ-weak topology** or **ultraweak topology** or **[weak- <sup>*</sup> operator topology](https://en.wikipedia.org/wiki/Weak-star_operator_topology "Weak-star operator topology")** or **weak-\* topology** or **weak topology** or **σ(B(*H*), B(*H*) <sub>*</sub>) topology** is defined by the family of seminorms |(*w*, *x*)| for elements *w* of B(*H*) <sub>*</sub>. It is stronger than the weak operator topology. (Warning: the weak Banach space topology and the weak operator topology and the ultraweak topology are all sometimes called the weak topology, but they are different.)
- The **[strong- <sup>*</sup> operator topology](https://en.wikipedia.org/w/index.php?title=Strong-*_operator_topology&action=edit&redlink=1 "Strong-* operator topology (page does not exist)")** or **strong- <sup>*</sup> topology** is defined by the seminorms || *x* (*h*)|| and || *x* <sup>*</sup> (*h*)|| for *h* ∈ *H*. It is stronger than the strong and weak operator topologies.
- The **[strong operator topology](https://en.wikipedia.org/wiki/Strong_operator_topology "Strong operator topology")** (SOT) or **strong topology** is defined by the seminorms || *x* (*h*)|| for *h* ∈ *H*. It is stronger than the weak operator topology.
- The **[weak operator topology](https://en.wikipedia.org/wiki/Weak_operator_topology "Weak operator topology")** (WOT) or **weak topology** is defined by the seminorms |(*x* (*h* <sub>1</sub>), *h* <sub>2</sub>)| for *h* <sub>1</sub>, *h* <sub>2</sub> ∈ *H*. (Warning: the weak Banach space topology, the weak operator topology, and the ultraweak topology are all sometimes called the weak topology, but they are different.)

## Relations between the topologies

The continuous linear functionals on B(*H*) for the weak, strong, and strong <sup>*</sup> (operator) topologies are the same, and are the finite linear combinations of the linear functionals (x *h* <sub>1</sub>, *h* <sub>2</sub>) for *h* <sub>1</sub>, *h* <sub>2</sub> ∈ *H*. The continuous linear functionals on B(*H*) for the ultraweak, ultrastrong, ultrastrong <sup>*</sup> and Arens-Mackey topologies are the same, and are the elements of the predual B(*H*) <sub>*</sub>.

By definition, the continuous linear functionals in the norm topology are the same as those in the weak Banach space topology. This dual is a rather large space with many pathological elements.

On norm bounded sets of B(*H*), the weak (operator) and ultraweak topologies coincide. This can be seen via, for instance, the [Banach–Alaoglu theorem](https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem "Banach–Alaoglu theorem"). For essentially the same reason, the ultrastrong topology is the same as the strong topology on any (norm) bounded subset of B(*H*). Same is true for the Arens-Mackey topology, the ultrastrong <sup>*</sup>, and the strong <sup>*</sup> topology.

In locally convex spaces, closure of convex sets can be characterized by the continuous linear functionals. Therefore, for a [convex](https://en.wikipedia.org/wiki/Convex_set "Convex set") subset K of B(*H*), the conditions that K be closed in the ultrastrong <sup>*</sup>, ultrastrong, and ultraweak topologies are all equivalent and are also equivalent to the conditions that for all *r* > 0, K has closed intersection with the closed ball of radius r in the strong <sup>*</sup>, strong, or weak (operator) topologies.

The norm topology is metrizable and the others are not; in fact they fail to be [first-countable](https://en.wikipedia.org/wiki/First-countable "First-countable"). However, when H is separable, all the topologies above are metrizable when restricted to the unit ball (or to any norm-bounded subset).

## Topology to use

The most commonly used topologies are the norm, strong, and weak operator topologies. The weak operator topology is useful for compactness arguments, because the unit ball is compact by the [Banach–Alaoglu theorem](https://en.wikipedia.org/wiki/Banach%E2%80%93Alaoglu_theorem "Banach–Alaoglu theorem"). The norm topology is fundamental because it makes B(*H*) into a Banach space, but it is too strong for many purposes; for example, B(*H*) is not separable in this topology. The strong operator topology could be the most commonly used.

The ultraweak and ultrastrong topologies are better-behaved than the weak and strong operator topologies, but their definitions are more complicated, so they are usually not used unless their better properties are really needed. For example, the dual space of B(*H*) in the weak or strong operator topology is too small to have much analytic content.

The adjoint map is not continuous in the strong operator and ultrastrong topologies, while the strong\* and ultrastrong\* topologies are modifications so that the adjoint becomes continuous. They are not used very often.

The Arens–Mackey topology and the weak Banach space topology are relatively rarely used.