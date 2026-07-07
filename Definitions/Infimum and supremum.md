---
title: "Infimum and supremum"
source: "https://en.wikipedia.org/wiki/Infimum_and_supremum"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2002-02-16
created: 2026-04-10
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Infimum_illustration.svg/330px-Infimum_illustration.svg.png)

A set {\\displaystyle P} of real numbers (hollow and filled circles), a subset {\\displaystyle S} of (filled circles), and the infimum of {\\displaystyle S.} Note that for totally ordered finite sets, the infimum and the minimum are equal.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Supremum_illustration.svg/330px-Supremum_illustration.svg.png)

A set {\\displaystyle A} of real numbers (blue circles), a set of upper bounds of (red diamond and circles), and the smallest such upper bound, that is, the supremum of (red diamond).

In mathematics, the **infimum** (abbreviated **inf**; pl.: **infima**) of a [subset](https://en.wikipedia.org/wiki/Subset "Subset") ${\displaystyle S}$ of a [partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set "Partially ordered set") ${\displaystyle P}$ is the [greatest element](https://en.wikipedia.org/wiki/Greatest_element "Greatest element") in ${\displaystyle P}$ that is less than or equal to each element of ${\displaystyle S,}$ if such an element exists.[^3] If the infimum of ${\displaystyle S}$ exists, it is unique, and if *b* is a [lower bound](https://en.wikipedia.org/wiki/Upper_and_lower_bounds "Upper and lower bounds") of ${\displaystyle S}$, then *b* is less than or equal to the infimum of ${\displaystyle S}$. Consequently, the term *greatest lower bound* (abbreviated as *GLB*) is also commonly used.[^3] The **supremum** (abbreviated **sup**; pl.: **suprema**) of a subset ${\displaystyle S}$ of a partially ordered set ${\displaystyle P}$ is the [least element](https://en.wikipedia.org/wiki/Least_element "Least element") in ${\displaystyle P}$ that is greater than or equal to each element of ${\displaystyle S,}$ if such an element exists.[^3] If the supremum of ${\displaystyle S}$ exists, it is unique, and if *b* is an [upper bound](https://en.wikipedia.org/wiki/Upper_and_lower_bounds "Upper and lower bounds") of ${\displaystyle S}$, then the supremum of ${\displaystyle S}$ is less than or equal to *b*. Consequently, the supremum is also referred to as the *least upper bound* (or *LUB*).[^3]

The infimum is, in a precise sense, [dual](https://en.wikipedia.org/wiki/Duality_\(order_theory\) "Duality (order theory)") to the concept of a supremum. Infima and suprema of [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") are common special cases that are important in [analysis](https://en.wikipedia.org/wiki/Mathematical_analysis "Mathematical analysis"), and especially in [Lebesgue integration](https://en.wikipedia.org/wiki/Lebesgue_integration "Lebesgue integration"). However, the general definitions remain valid in the more abstract setting of [order theory](https://en.wikipedia.org/wiki/Order_theory "Order theory") where arbitrary partially ordered sets are considered.

The concepts of infimum and supremum are close to [minimum](https://en.wikipedia.org/wiki/Minimum "Minimum") and [maximum](https://en.wikipedia.org/wiki/Maximum "Maximum"), but are more useful in analysis because they better characterize special sets which may have *no minimum or maximum*. For instance, the set of [positive real numbers](https://en.wikipedia.org/wiki/Positive_real_numbers "Positive real numbers") ${\displaystyle \mathbb {R} ^{+}}$ (not including ${\displaystyle 0}$) does not have a minimum, because any given element of ${\displaystyle \mathbb {R} ^{+}}$ could simply be divided in half resulting in a smaller number that is still in ${\displaystyle \mathbb {R} ^{+}.}$ There is, however, exactly one infimum of the positive real numbers relative to the real numbers: ${\displaystyle 0,}$ which is smaller than all the positive real numbers and greater than any other real number which could be used as a lower bound. An infimum of a set is always and only defined relative to a superset of the set in question. For example, there is no infimum of the positive real numbers inside the positive real numbers (as their own superset), nor any infimum of the positive real numbers inside the complex numbers with positive real part.

## Formal definition

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Illustration_of_supremum.svg/330px-Illustration_of_supremum.svg.png)

supremum = least upper bound

A *lower bound* of a subset ${\displaystyle S}$ of a [partially ordered set](https://en.wikipedia.org/wiki/Partially_ordered_set "Partially ordered set") ${\displaystyle (P,\leq )}$ is an element ${\displaystyle y}$ of ${\displaystyle P}$ such that

- ${\displaystyle y\leq x}$ for all ${\displaystyle x\in S.}$

A lower bound ${\displaystyle a}$ of ${\displaystyle S}$ is called an *infimum* (or *greatest lower bound*, or [*meet*](https://en.wikipedia.org/wiki/Join_and_meet "Join and meet")) of ${\displaystyle S}$ if

- for all lower bounds ${\displaystyle y}$ of ${\displaystyle S}$ in ${\displaystyle P,}$ ${\displaystyle y\leq a}$ (${\displaystyle a}$ is larger than any other lower bound).

Similarly, an *upper bound* of a subset ${\displaystyle S}$ of a partially ordered set ${\displaystyle (P,\leq )}$ is an element ${\displaystyle z}$ of ${\displaystyle P}$ such that

- ${\displaystyle z\geq x}$ for all ${\displaystyle x\in S.}$

An upper bound ${\displaystyle b}$ of ${\displaystyle S}$ is called a *supremum* (or *least upper bound*, or [*join*](https://en.wikipedia.org/wiki/Join_and_meet "Join and meet")) of ${\displaystyle S}$ if

- for all upper bounds ${\displaystyle z}$ of ${\displaystyle S}$ in ${\displaystyle P,}$ ${\displaystyle z\geq b}$ (${\displaystyle b}$ is less than any other upper bound).

We can also define suprema and infima without restricting to sets. For example, there is no set containing all [cardinal numbers](https://en.wikipedia.org/wiki/Cardinal_number "Cardinal number") (and there is no greatest cardinal number), but the [axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice "Axiom of choice") implies that every set of cardinal numbers has a least upper bound among cardinal numbers. The axiom of choice is equivalent to the statement that every nonempty set of cardinal numbers has a minimum element (which is also the infimum of the set). The empty set of cardinal numbers has many lower bounds but no greatest lower bound among cardinal numbers.

## Existence and uniqueness

Infima and suprema do not necessarily exist. Existence of an infimum of a subset ${\displaystyle S}$ of ${\displaystyle P}$ can fail if ${\displaystyle S}$ has no lower bound at all, or if the set of lower bounds does not contain a greatest element. (An example of this is the subset ${\displaystyle \{x\in \mathbb {Q} :x^{2}<2\}}$ of ${\displaystyle \mathbb {Q} }$. It has upper bounds, such as 1.5, but no supremum in ${\displaystyle \mathbb {Q} }$.)

Consequently, partially ordered sets for which certain infima are known to exist become especially interesting. For instance, a [lattice](https://en.wikipedia.org/wiki/Lattice_\(order\) "Lattice (order)") is a partially ordered set in which all *nonempty finite* subsets have both a supremum and an infimum, and a [complete lattice](https://en.wikipedia.org/wiki/Complete_lattice "Complete lattice") is a partially ordered set in which *all* subsets have both a supremum and an infimum. More information on the various classes of partially ordered sets that arise from such considerations are found in the article on [completeness properties](https://en.wikipedia.org/wiki/Completeness_\(order_theory\) "Completeness (order theory)").

If the supremum of a subset ${\displaystyle S}$ exists, it is unique. If ${\displaystyle S}$ contains a greatest element, then that element is the supremum; otherwise, the supremum does not belong to ${\displaystyle S}$ (or does not exist). Likewise, if the infimum exists, it is unique. If ${\displaystyle S}$ contains a least element, then that element is the infimum; otherwise, the infimum does not belong to ${\displaystyle S}$ (or does not exist).

## Relation to maximum and minimum elements

The infimum of a subset ${\displaystyle S}$ of a partially ordered set ${\displaystyle P,}$ assuming it exists, does not necessarily belong to ${\displaystyle S.}$ If it does, it is a [minimum or least element](https://en.wikipedia.org/wiki/Least_element "Least element") of ${\displaystyle S.}$ Similarly, if the supremum of ${\displaystyle S}$ belongs to ${\displaystyle S,}$ it is a [maximum or greatest element](https://en.wikipedia.org/wiki/Greatest_element "Greatest element") of ${\displaystyle S.}$

For example, consider the set of negative real numbers (excluding zero). This set has no greatest element, since for every element of the set, there is another, larger, element. For instance, for any negative real number ${\displaystyle x,}$ there is another negative real number ${\displaystyle {\tfrac {x}{2}},}$ which is greater. On the other hand, every real number greater than or equal to zero is certainly an upper bound on this set. Hence, ${\displaystyle 0}$ is the least upper bound of the negative reals, so the supremum is 0. This set has a supremum but no greatest element.

However, the definition of [maximal and minimal elements](https://en.wikipedia.org/wiki/Maximal_element "Maximal element") is more general. In particular, a set can have many maximal and minimal elements, whereas infima and suprema are unique.

Whereas maxima and minima must be members of the subset that is under consideration, the infimum and supremum of a subset need not be members of that subset themselves.

### Minimal upper bounds

Finally, a partially ordered set may have many minimal upper bounds without having a least upper bound. Minimal upper bounds are those upper bounds for which there is no strictly smaller element that also is an upper bound. This does not say that each minimal upper bound is smaller than all other upper bounds, it merely is not greater. The distinction between "minimal" and "least" is only possible when the given order is not a [total](https://en.wikipedia.org/wiki/Totally_ordered_set "Totally ordered set") one. In a totally ordered set, like the real numbers, the concepts are the same.

As an example, let ${\displaystyle S}$ be the set of all finite subsets of natural numbers and consider the partially ordered set obtained by taking all sets from ${\displaystyle S}$ together with the set of [integers](https://en.wikipedia.org/wiki/Integer "Integer") ${\displaystyle \mathbb {Z} }$ and the set of positive real numbers ${\displaystyle \mathbb {R} ^{+},}$ ordered by subset inclusion as above. Then clearly both ${\displaystyle \mathbb {Z} }$ and ${\displaystyle \mathbb {R} ^{+}}$ are greater than all finite sets of natural numbers. Yet, neither is ${\displaystyle \mathbb {R} ^{+}}$ smaller than ${\displaystyle \mathbb {Z} }$ nor is the converse true: both sets are minimal upper bounds but none is a supremum.

### Least-upper-bound property

The *least-upper-bound property* is an example of the aforementioned [completeness properties](https://en.wikipedia.org/wiki/Completeness_\(order_theory\) "Completeness (order theory)") which is typical for the set of real numbers. This property is sometimes called *Dedekind completeness*.

If an ordered set ${\displaystyle S}$ has the property that every nonempty subset of ${\displaystyle S}$ having an upper bound also has a least upper bound, then ${\displaystyle S}$ is said to have the least-upper-bound property. As noted above, the set ${\displaystyle \mathbb {R} }$ of all real numbers has the least-upper-bound property. Similarly, the set ${\displaystyle \mathbb {Z} }$ of integers has the least-upper-bound property; if ${\displaystyle S}$ is a nonempty subset of ${\displaystyle \mathbb {Z} }$ and there is some number ${\displaystyle n}$ such that every element ${\displaystyle s}$ of ${\displaystyle S}$ is less than or equal to ${\displaystyle n,}$ then there is a least upper bound ${\displaystyle u}$ for ${\displaystyle S,}$ an integer that is an upper bound for ${\displaystyle S}$ and is less than or equal to every other upper bound for ${\displaystyle S.}$ A [well-ordered](https://en.wikipedia.org/wiki/Well-order "Well-order") set also has the least-upper-bound property, and the empty subset has also a least upper bound: the minimum of the whole set.

An example of a set that *lacks* the least-upper-bound property is ${\displaystyle \mathbb {Q} ,}$ the set of rational numbers. Let ${\displaystyle S}$ be the set of all rational numbers ${\displaystyle q}$ such that ${\displaystyle q^{2}<2.}$ Then ${\displaystyle S}$ has an upper bound (${\displaystyle 1000,}$ for example, or ${\displaystyle 6}$) but no least upper bound in ${\displaystyle \mathbb {Q} }$: If we suppose ${\displaystyle p\in \mathbb {Q} }$ is the least upper bound, a contradiction is immediately deduced because between any two reals ${\displaystyle x}$ and ${\displaystyle y}$ (including [${\displaystyle {\sqrt {2}}}$](https://en.wikipedia.org/wiki/Square_root_of_2 "Square root of 2") and ${\displaystyle p}$) there exists some rational ${\displaystyle r,}$ which itself would have to be the least upper bound (if ${\displaystyle p>{\sqrt {2}}}$) or a member of ${\displaystyle S}$ greater than ${\displaystyle p}$ (if ${\displaystyle p<{\sqrt {2}}}$). Another example is the [hyperreals](https://en.wikipedia.org/wiki/Hyperreals "Hyperreals"); there is no least upper bound of the set of positive infinitesimals.

There is a corresponding *greatest-lower-bound property*; an ordered set possesses the greatest-lower-bound property if and only if it also possesses the least-upper-bound property; the least-upper-bound of the set of lower bounds of a set is the greatest-lower-bound, and the greatest-lower-bound of the set of upper bounds of a set is the least-upper-bound of the set.

If in a partially ordered set ${\displaystyle P}$ every bounded subset has a supremum, this applies also, for any set ${\displaystyle X,}$ in the function space containing all functions from ${\displaystyle X}$ to ${\displaystyle P,}$ where ${\displaystyle f\leq g}$ if and only if ${\displaystyle f(x)\leq g(x)}$ for all ${\displaystyle x\in X.}$ For example, it applies for real functions, and, since these can be considered special cases of functions, for real ${\displaystyle n}$ -tuples and sequences of real numbers.

The [least-upper-bound property](https://en.wikipedia.org/wiki/Least-upper-bound_property "Least-upper-bound property") is an indicator of the suprema.

## Infima and suprema of real numbers

In [analysis](https://en.wikipedia.org/wiki/Mathematical_analysis "Mathematical analysis"), infima and suprema of subsets ${\displaystyle S}$ of the [real numbers](https://en.wikipedia.org/wiki/Real_numbers "Real numbers") are particularly important. For instance, the negative [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") do not have a greatest element, and their supremum is ${\displaystyle 0}$ (which is not a negative real number).[^3] The [completeness of the real numbers](https://en.wikipedia.org/wiki/Completeness_of_the_real_numbers "Completeness of the real numbers") implies (and is equivalent to) that any bounded nonempty subset ${\displaystyle S}$ of the real numbers has an infimum and a supremum. If ${\displaystyle S}$ is not bounded below, one often formally writes ${\displaystyle \inf _{}S=-\infty .}$ If ${\displaystyle S}$ is [empty](https://en.wikipedia.org/wiki/Empty_set "Empty set"), one writes ${\displaystyle \inf _{}S=+\infty .}$

### Properties

If ${\displaystyle A}$ is any set of real numbers then ${\displaystyle A\neq \varnothing }$ if and only if ${\displaystyle \sup A\geq \inf A,}$ and otherwise ${\displaystyle -\infty =\sup \varnothing <\inf \varnothing =\infty .}$ [^4]

**Set inclusion**

If ${\displaystyle A\subseteq B}$ are sets of real numbers then ${\displaystyle \inf A\geq \inf B}$ (if ${\displaystyle A=\varnothing }$ this reads as ${\displaystyle \inf B\leq \infty }$) and ${\displaystyle \sup A\leq \sup B.}$

**Image under functions** If ${\displaystyle f\colon \mathbb {R} \to \mathbb {R} }$ is a nondecreasing function and ${\displaystyle S}$ is a nonempty bounded subset of ${\displaystyle \mathbb {R} }$, then ${\displaystyle f(\inf(S))\leq \inf(f[S])}$ and ${\displaystyle f(\sup(S))\geq \sup(f[S])}$, where the image is defined as ${\displaystyle f[S]\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\{f(s):s\in S\}.}$

**Identifying infima and suprema**

If the infimum of ${\displaystyle A}$ exists (that is, ${\displaystyle \inf A}$ is a real number) and if ${\displaystyle p}$ is any real number then ${\displaystyle p=\inf A}$ if and only if ${\displaystyle p}$ is a lower bound and for every ${\displaystyle \epsilon >0}$ there is an ${\displaystyle a_{\epsilon }\in A}$ with ${\displaystyle a_{\epsilon }<p+\epsilon .}$ Similarly, if ${\displaystyle \sup A}$ is a real number and if ${\displaystyle p}$ is any real number then ${\displaystyle p=\sup A}$ if and only if ${\displaystyle p}$ is an upper bound and if for every ${\displaystyle \epsilon >0}$ there is an ${\displaystyle a_{\epsilon }\in A}$ with ${\displaystyle a_{\epsilon }>p-\epsilon .}$

**Relation to limits of sequences**

If ${\displaystyle S\neq \varnothing }$ is any non-empty set of real numbers then there always exists a non-decreasing sequence ${\displaystyle s_{1}\leq s_{2}\leq \cdots }$ in ${\displaystyle S}$ such that ${\displaystyle \lim _{n\to \infty }s_{n}=\sup S.}$ Similarly, there will exist a (possibly different) non-increasing sequence ${\displaystyle s_{1}\geq s_{2}\geq \cdots }$ in ${\displaystyle S}$ such that ${\displaystyle \lim _{n\to \infty }s_{n}=\inf S.}$ In particular, the infimum and supremum of a set belong to its [closure](https://en.wikipedia.org/wiki/Closure_\(topology\) "Closure (topology)") if ${\displaystyle \inf S\in \mathbb {R} }$ then ${\displaystyle \inf S\in {\bar {S}}}$ and if ${\displaystyle \sup S\in \mathbb {R} }$ then ${\displaystyle \sup S\in {\bar {S}}}$

Expressing the infimum and supremum as a limit of a such a sequence allows theorems from various branches of mathematics to be applied. Consider for example the well-known fact from [topology](https://en.wikipedia.org/wiki/Topology "Topology") that if ${\displaystyle f}$ is a [continuous function](https://en.wikipedia.org/wiki/Continuous_function_\(topology\) "Continuous function (topology)") and ${\displaystyle s_{1},s_{2},\ldots }$ is a sequence of points in its domain that converges to a point ${\displaystyle p,}$ then ${\displaystyle f\left(s_{1}\right),f\left(s_{2}\right),\ldots }$ necessarily converges to ${\displaystyle f(p).}$ It implies that if ${\displaystyle \lim _{n\to \infty }s_{n}=\sup S}$ is a real number (where all ${\displaystyle s_{1},s_{2},\ldots }$ are in ${\displaystyle S}$) and if ${\displaystyle f}$ is a continuous function whose domain contains ${\displaystyle S}$ and ${\displaystyle \sup S,}$ then 
$$
{\displaystyle f(\sup S)=f\left(\lim _{n\to \infty }s_{n}\right)=\lim _{n\to \infty }f\left(s_{n}\right),}
$$
 which (for instance) guarantees [^1] that ${\displaystyle f(\sup S)}$ is an [adherent point](https://en.wikipedia.org/wiki/Adherent_point "Adherent point") of the set ${\displaystyle f(S)\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\{f(s):s\in S\}.}$ If in addition to what has been assumed, the continuous function ${\displaystyle f}$ is also an increasing or [non-decreasing function](https://en.wikipedia.org/wiki/Non-decreasing_function "Non-decreasing function"), then it is even possible to conclude that ${\displaystyle \sup f(S)=f(\sup S).}$ This may be applied, for instance, to conclude that whenever ${\displaystyle g}$ is a real (or [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number")) valued function with domain ${\displaystyle \Omega \neq \varnothing }$ whose [sup norm](https://en.wikipedia.org/wiki/Sup_norm "Sup norm") ${\displaystyle \|g\|_{\infty }\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\sup _{x\in \Omega }|g(x)|}$ is finite, then for every non-negative real number ${\displaystyle q,}$ 
$$
{\displaystyle \|g\|_{\infty }^{q}~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\left(\sup _{x\in \Omega }|g(x)|\right)^{q}=\sup _{x\in \Omega }\left(|g(x)|^{q}\right)}
$$
 since the map ${\displaystyle f:[0,\infty )\to \mathbb {R} }$ defined by ${\displaystyle f(x)=x^{q}}$ is a continuous non-decreasing function whose domain ${\displaystyle [0,\infty )}$ always contains ${\displaystyle S:=\{|g(x)|:x\in \Omega \}}$ and ${\displaystyle \sup S\,{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\,\|g\|_{\infty }.}$

Although this discussion focused on ${\displaystyle \sup ,}$ similar conclusions can be reached for ${\displaystyle \inf }$ with appropriate changes (such as requiring that ${\displaystyle f}$ be non-increasing rather than non-decreasing). Other [norms](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") defined in terms of ${\displaystyle \sup }$ or ${\displaystyle \inf }$ include the [weak ${\displaystyle L^{p,w}}$ space](https://en.wikipedia.org/wiki/Weak_Lp_space "Weak Lp space") norms (for ${\displaystyle 1\leq p<\infty }$), the norm on [Lebesgue space](https://en.wikipedia.org/wiki/Lp_space "Lp space") ${\displaystyle L^{\infty }(\Omega ,\mu ),}$ and [operator norms](https://en.wikipedia.org/wiki/Operator_norm "Operator norm"). Monotone sequences in ${\displaystyle S}$ that converge to ${\displaystyle \sup S}$ (or to ${\displaystyle \inf S}$) can also be used to help prove many of the formula given below, since addition and multiplication of real numbers are continuous operations.

### Arithmetic operations on sets

The following formulas depend on a notation that conveniently generalizes arithmetic operations on sets. Throughout, ${\displaystyle A,B\subseteq \mathbb {R} }$ are sets of real numbers.

**Sum of sets**

The [Minkowski sum](https://en.wikipedia.org/wiki/Minkowski_sum "Minkowski sum") of two sets ${\displaystyle A}$ and ${\displaystyle B}$ of real numbers is the set 
$$
{\displaystyle A+B~:=~\{a+b:a\in A,b\in B\}}
$$
 consisting of all possible arithmetic sums of pairs of numbers, one from each set. The infimum and supremum of the Minkowski sum satisfy, if ${\displaystyle A\neq \varnothing \neq B}$ 
$$
{\displaystyle \inf(A+B)=(\inf A)+(\inf B)}
$$
 and 
$$
{\displaystyle \sup(A+B)=(\sup A)+(\sup B).}
$$

**Product of sets**

The multiplication of two sets ${\displaystyle A}$ and ${\displaystyle B}$ of real numbers is defined similarly to their Minkowski sum: 
$$
{\displaystyle A\cdot B~:=~\{a\cdot b:a\in A,b\in B\}.}
$$

If ${\displaystyle A}$ and ${\displaystyle B}$ are nonempty sets of positive real numbers then ${\displaystyle \inf(A\cdot B)=(\inf A)\cdot (\inf B)}$ and similarly for suprema ${\displaystyle \sup(A\cdot B)=(\sup A)\cdot (\sup B).}$ [^5]

**Scalar product of a set**

The product of a real number ${\displaystyle r}$ and a set ${\displaystyle B}$ of real numbers is the set 
$$
{\displaystyle rB~:=~\{r\cdot b:b\in B\}.}
$$

If ${\displaystyle r>0}$ then 
$$
{\displaystyle \inf(r\cdot A)=r(\inf A)\quad {\text{ and }}\quad \sup(r\cdot A)=r(\sup A),}
$$
 while if ${\displaystyle r<0}$ then 
$$
{\displaystyle \inf(r\cdot A)=r(\sup A)\quad {\text{ and }}\quad \sup(r\cdot A)=r(\inf A).}
$$
 In the case ${\displaystyle r=0}$, one has, if ${\displaystyle A\neq \varnothing }$ 
$$
{\displaystyle \inf(0\cdot A)=0\quad {\text{ and }}\quad \sup(0\cdot A)=0}
$$
 Using ${\displaystyle r=-1}$ and the notation ${\textstyle -A:=(-1)A=\{-a:a\in A\},}$ it follows that, 
$$
{\displaystyle \inf(-A)=-\sup A\quad {\text{ and }}\quad \sup(-A)=-\inf A.}
$$

**Multiplicative inverse of a set**

For any set ${\displaystyle S}$ that does not contain ${\displaystyle 0,}$ let 
$$
{\displaystyle {\frac {1}{S}}~:=\;\left\{{\tfrac {1}{s}}:s\in S\right\}.}
$$

If ${\displaystyle S\subseteq (0,\infty )}$ is non-empty then 
$$
{\displaystyle {\frac {1}{\sup _{}S}}~=~\inf _{}{\frac {1}{S}}}
$$
 where this equation also holds when ${\displaystyle \sup _{}S=\infty }$ if the definition ${\displaystyle {\frac {1}{\infty }}:=0}$ is used.[^2] This equality may alternatively be written as ${\displaystyle {\frac {1}{\displaystyle \sup _{s\in S}s}}=\inf _{s\in S}{\tfrac {1}{s}}.}$ Moreover, ${\displaystyle \inf _{}S=0}$ if and only if ${\displaystyle \sup _{}{\tfrac {1}{S}}=\infty ,}$ where if [^2] ${\displaystyle \inf _{}S>0,}$ then ${\displaystyle {\tfrac {1}{\inf _{}S}}=\sup _{}{\tfrac {1}{S}}.}$

## Duality

If one denotes by ${\displaystyle P^{\operatorname {op} }}$ the partially-ordered set ${\displaystyle P}$ with the [opposite order relation](https://en.wikipedia.org/wiki/Converse_relation "Converse relation"); that is, for all ${\displaystyle x{\text{ and }}y,}$ declare: 
$$
{\displaystyle x\leq y{\text{ in }}P^{\operatorname {op} }\quad {\text{ if and only if }}\quad x\geq y{\text{ in }}P,}
$$
 then infimum of a subset ${\displaystyle S}$ in ${\displaystyle P}$ equals the supremum of ${\displaystyle S}$ in ${\displaystyle P^{\operatorname {op} }}$ and vice versa.

For subsets of the real numbers, another kind of duality holds: ${\displaystyle \inf S=-\sup(-S),}$ where ${\displaystyle -S:=\{-s~:~s\in S\}.}$

## Examples

### Infima

- The infimum of the set of numbers ${\displaystyle \{2,3,4\}}$ is ${\displaystyle 2.}$ The number ${\displaystyle 1}$ is a lower bound, but not the greatest lower bound, and hence not the infimum.
- More generally, if a set has a smallest element, then the smallest element is the infimum for the set. In this case, it is also called the [minimum](https://en.wikipedia.org/wiki/Minimum "Minimum") of the set.
- ${\displaystyle \inf\{1,2,3,\ldots \}=1.}$
- ${\displaystyle \inf\{x\in \mathbb {R} :0<x<1\}=0.}$
- ${\displaystyle \inf \left\{x\in \mathbb {Q} :x^{3}>2\right\}={\sqrt[{3}]{2}}.}$
- ${\displaystyle \inf \left\{(-1)^{n}+{\tfrac {1}{n}}:n=1,2,3,\ldots \right\}=-1.}$
- If ${\displaystyle \left(x_{n}\right)_{n=1}^{\infty }}$ is a decreasing sequence with limit ${\displaystyle x,}$ then ${\displaystyle \inf x_{n}=x.}$

### Suprema

- The supremum of the set of numbers ${\displaystyle \{1,2,3\}}$ is ${\displaystyle 3.}$ The number ${\displaystyle 4}$ is an upper bound, but it is not the least upper bound, and hence is not the supremum.
- ${\displaystyle \sup\{x\in \mathbb {R} :0<x<1\}=\sup\{x\in \mathbb {R} :0\leq x\leq 1\}=1.}$
- ${\displaystyle \sup \left\{(-1)^{n}-{\tfrac {1}{n}}:n=1,2,3,\ldots \right\}=1.}$
- ${\displaystyle \sup\{a+b:a\in A,b\in B\}=\sup A+\sup B.}$
- ${\displaystyle \sup \left\{x\in \mathbb {Q} :x^{2}<2\right\}={\sqrt {2}}.}$

In the last example, the supremum of a set of [rationals](https://en.wikipedia.org/wiki/Rational_number "Rational number") is [irrational](https://en.wikipedia.org/wiki/Irrational_number "Irrational number"), which means that the rationals are [incomplete](https://en.wikipedia.org/wiki/Complete_space "Complete space").

One basic property of the supremum is 
$$
{\displaystyle \sup\{f(t)+g(t):t\in A\}~\leq ~\sup\{f(t):t\in A\}+\sup\{g(t):t\in A\}}
$$
 for any [functionals](https://en.wikipedia.org/wiki/Functional_\(mathematics\) "Functional (mathematics)") ${\displaystyle f}$ and ${\displaystyle g.}$

The supremum of a subset ${\displaystyle S}$ of ${\displaystyle (\mathbb {N} ,\mid \,)}$ where ${\displaystyle \,\mid \,}$ denotes " [divides](https://en.wikipedia.org/wiki/Divisor "Divisor") ", is the [lowest common multiple](https://en.wikipedia.org/wiki/Lowest_common_multiple "Lowest common multiple") of the elements of ${\displaystyle S.}$

The supremum of a set ${\displaystyle S}$ containing subsets of some set ${\displaystyle X}$ is the [union](https://en.wikipedia.org/wiki/Union_\(set_theory\) "Union (set theory)") of the subsets when considering the partially ordered set ${\displaystyle (P(X),\subseteq )}$, where ${\displaystyle P}$ is the [power set](https://en.wikipedia.org/wiki/Power_set "Power set") of ${\displaystyle X}$ and ${\displaystyle \,\subseteq \,}$ is [subset](https://en.wikipedia.org/wiki/Subset "Subset").

[^1]: Since ${\displaystyle f\left(s_{1}\right),f\left(s_{2}\right),\ldots }$ is a sequence in ${\displaystyle f(S)}$ that converges to ${\displaystyle f(\sup S),}$ this guarantees that ${\displaystyle f(\sup S)}$ belongs to the [closure](https://en.wikipedia.org/wiki/Closure_\(topology\) "Closure (topology)") of ${\displaystyle f(S).}$

[^2]: The definition ${\displaystyle {\tfrac {1}{\infty }}:=0}$ is commonly used with the [extended real numbers](https://en.wikipedia.org/wiki/Extended_real_number "Extended real number"); in fact, with this definition the equality ${\displaystyle {\tfrac {1}{\sup _{}S}}=\inf _{}{\tfrac {1}{S}}}$ will also hold for any non-empty subset ${\displaystyle S\subseteq (0,\infty ].}$ However, the notation ${\displaystyle {\tfrac {1}{0}}}$ is usually left undefined, which is why the equality ${\displaystyle {\tfrac {1}{\inf _{}S}}=\sup _{}{\tfrac {1}{S}}}$ is given only for when ${\displaystyle \inf _{}S>0.}$

[^3]: [Rudin, Walter](https://en.wikipedia.org/wiki/Walter_Rudin "Walter Rudin") (1976). "Chapter 1 The Real and Complex Number Systems". [*Principles of Mathematical Analysis*](https://archive.org/details/principlesofmath00rudi) (print) (3rd ed.). McGraw-Hill. p. [4](https://archive.org/details/principlesofmath00rudi/page/n15). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-07-054235-X](https://en.wikipedia.org/wiki/Special:BookSources/0-07-054235-X "Special:BookSources/0-07-054235-X").

[^4]: [Rockafellar & Wets 2009](#CITEREFRockafellarWets2009), pp. 1–2.

[^5]: Zakon, Elias (2004). [*Mathematical Analysis I*](http://www.trillia.com/zakon-analysisI.html). Trillia Group. pp. 39–42.