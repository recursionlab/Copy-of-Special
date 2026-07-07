---
title: "Lp space"
source: "https://en.wikipedia.org/wiki/Lp_space"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2002-03-20
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the ***L* <sup><i>p</i></sup> spaces** are [function spaces](https://en.wikipedia.org/wiki/Function_space "Function space") defined using a natural generalization of the [*p* -norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\)#p-norm "Norm (mathematics)") for finite-dimensional [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space"). They are sometimes called **Lebesgue spaces**, named after [Henri Lebesgue](https://en.wikipedia.org/wiki/Henri_Lebesgue "Henri Lebesgue") ([Dunford & Schwartz 1958](#CITEREFDunfordSchwartz1958), III.3), although according to the [Bourbaki](https://en.wikipedia.org/wiki/Nicolas_Bourbaki "Nicolas Bourbaki") group ([Bourbaki 1987](#CITEREFBourbaki1987)) they were first introduced by [Frigyes Riesz](https://en.wikipedia.org/wiki/Frigyes_Riesz "Frigyes Riesz") ([Riesz 1910](#CITEREFRiesz1910)).

*L* <sup><i>p</i></sup> spaces form an important class of [Banach spaces](https://en.wikipedia.org/wiki/Banach_space "Banach space") in [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis "Functional analysis"), and of [topological vector spaces](https://en.wikipedia.org/wiki/Topological_vector_space "Topological vector space"). Because of their key role in the mathematical analysis of measure and probability spaces, Lebesgue spaces are used also in the theoretical discussion of problems in physics, statistics, economics, finance, engineering, and other disciplines.

## Preliminaries

### The p-norm in finite dimensions

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Vector-p-Norms_qtl1.svg/250px-Vector-p-Norms_qtl1.svg.png)

Illustrations of unit circles (see also superellipse ) in {\\displaystyle \\mathbb {R} ^{2}} based on different {\\displaystyle p} -norms (every vector from the origin to the unit circle has a length of one, the length being calculated with length-formula of the corresponding ).

The Euclidean length of a vector ${\displaystyle x=(x_{1},x_{2},\dots ,x_{n})}$ in the ${\displaystyle n}$ -dimensional [real](https://en.wikipedia.org/wiki/Real_number "Real number") [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") ${\displaystyle \mathbb {R} ^{n}}$ is given by the [Euclidean norm](https://en.wikipedia.org/wiki/Euclidean_norm "Euclidean norm"): 
$$
{\displaystyle \|x\|_{2}=\left({x_{1}}^{2}+{x_{2}}^{2}+\dotsb +{x_{n}}^{2}\right)^{1/2}.}
$$

The Euclidean distance between two points ${\displaystyle x}$ and ${\displaystyle y}$ is the length ${\displaystyle \|x-y\|_{2}}$ of the straight line between the two points. In many situations, the Euclidean distance is appropriate for capturing the actual distances in a given space. In contrast, consider taxi drivers in a grid street plan who should measure distance not in terms of the length of the straight line to their destination, but in terms of the [rectilinear distance](https://en.wikipedia.org/wiki/Taxicab_geometry "Taxicab geometry"), which takes into account that streets are either orthogonal or parallel to each other. The class of ${\displaystyle p}$ -norms generalizes these two examples and has an abundance of applications in many parts of [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), [physics](https://en.wikipedia.org/wiki/Physics "Physics"), and [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science").

For a [real number](https://en.wikipedia.org/wiki/Real_number "Real number") ${\displaystyle p\geq 1,}$ the **${\displaystyle p}$ -norm** or **${\displaystyle L^{p}}$ -norm** of ${\displaystyle x}$ is defined by 
$$
{\displaystyle \|x\|_{p}=\left(|x_{1}|^{p}+|x_{2}|^{p}+\dotsb +|x_{n}|^{p}\right)^{1/p}.}
$$
 The absolute value bars can be dropped when ${\displaystyle p}$ is a rational number with an even numerator in its reduced form, and ${\displaystyle x}$ is drawn from the set of real numbers, or one of its subsets.

The Euclidean norm from above falls into this class and is the ${\displaystyle 2}$ -norm, and the ${\displaystyle 1}$ -norm is the norm that corresponds to the [rectilinear distance](https://en.wikipedia.org/wiki/Taxicab_geometry "Taxicab geometry").

The **${\displaystyle L^{\infty }}$ -norm** or [maximum norm](https://en.wikipedia.org/wiki/Chebyshev_distance "Chebyshev distance") (or uniform norm) is the limit of the ${\displaystyle L^{p}}$ -norms for ${\displaystyle p\to \infty }$, given by: 
$$
{\displaystyle \|x\|_{\infty }=\max \left\{|x_{1}|,|x_{2}|,\dotsc ,|x_{n}|\right\}}
$$

For all ${\displaystyle p\geq 1,}$ the ${\displaystyle p}$ -norms and maximum norm satisfy the properties of a "length function" (or [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)")), that is:

- only the zero vector has zero length,
- the length of the vector is positive homogeneous with respect to multiplication by a scalar ([positive homogeneity](https://en.wikipedia.org/wiki/Euler%27s_homogeneous_function_theorem "Euler's homogeneous function theorem")), and
- the length of the sum of two vectors is no larger than the sum of lengths of the vectors ([triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality "Triangle inequality")).

Abstractly speaking, this means that ${\displaystyle \mathbb {R} ^{n}}$ together with the ${\displaystyle p}$ -norm is a [normed vector space](https://en.wikipedia.org/wiki/Normed_vector_space "Normed vector space"). Moreover, it turns out that this space is [complete](https://en.wikipedia.org/wiki/Complete_metric_space "Complete metric space"), thus making it a [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space").

#### Relations between p-norms

The grid distance or rectilinear distance (sometimes called the " [Manhattan distance](https://en.wikipedia.org/wiki/Manhattan_distance "Manhattan distance") ") between two points is never shorter than the length of the line segment between them (the Euclidean or "as the crow flies" distance). Formally, this means that the Euclidean norm of any vector is bounded by its 1-norm: 
$$
{\displaystyle \|x\|_{2}\leq \|x\|_{1}.}
$$

This fact generalizes to ${\displaystyle p}$ -norms in that the ${\displaystyle p}$ -norm ${\displaystyle \|x\|_{p}}$ of any given vector ${\displaystyle x}$ does not grow with ${\displaystyle p}$:

${\displaystyle \|x\|_{p+a}\leq \|x\|_{p}}$ for any vector ${\displaystyle x}$ and real numbers ${\displaystyle p\geq 1}$ and ${\displaystyle a\geq 0.}$ (In fact this remains true for ${\displaystyle 0<p<1}$ and ${\displaystyle a\geq 0}$.)

For the opposite direction, the following relation between the ${\displaystyle 1}$ -norm and the ${\displaystyle 2}$ -norm is known: 
$$
{\displaystyle \|x\|_{1}\leq {\sqrt {n}}\|x\|_{2}~.}
$$

This inequality depends on the dimension ${\displaystyle n}$ of the underlying vector space and follows directly from the [Cauchy–Schwarz inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality "Cauchy–Schwarz inequality").

In general, for vectors in ${\displaystyle \mathbb {C} ^{n}}$ where ${\displaystyle 0<r<p:}$ 
$$
{\displaystyle \|x\|_{p}\leq \|x\|_{r}\leq n^{{\frac {1}{r}}-{\frac {1}{p}}}\|x\|_{p}~.}
$$

This is a consequence of [Hölder's inequality](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality "Hölder's inequality").

#### When 0 < p < 1

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Astroid.svg/250px-Astroid.svg.png)

Astroid, unit circle in {\\displaystyle p={\\tfrac {2}{3}}} metric

In ${\displaystyle \mathbb {R} ^{n}}$ for ${\displaystyle n>1,}$ the formula 
$$
{\displaystyle \|x\|_{p}=\left(|x_{1}|^{p}+|x_{2}|^{p}+\cdots +|x_{n}|^{p}\right)^{1/p}}
$$
 defines an absolutely [homogeneous function](https://en.wikipedia.org/wiki/Homogeneous_function "Homogeneous function") for ${\displaystyle 0<p<1;}$ however, the resulting function does not define a norm, because it is not [subadditive](https://en.wikipedia.org/wiki/Subadditivity "Subadditivity"). On the other hand, the formula 
$$
{\displaystyle |x_{1}|^{p}+|x_{2}|^{p}+\dotsb +|x_{n}|^{p}}
$$
 defines a subadditive function at the cost of losing absolute homogeneity. It does define an [F-norm](https://en.wikipedia.org/wiki/F-space "F-space"), though, which is homogeneous of degree ${\displaystyle p.}$

Hence, the function 
$$
{\displaystyle d_{p}(x,y)=\sum _{i=1}^{n}|x_{i}-y_{i}|^{p}}
$$
 defines a [metric](https://en.wikipedia.org/wiki/Metric_space "Metric space"). The [metric space](https://en.wikipedia.org/wiki/Metric_space "Metric space") ${\displaystyle (\mathbb {R} ^{n},d_{p})}$ is denoted by ${\displaystyle \ell _{n}^{p}.}$

Although the ${\displaystyle p}$ -unit ball ${\displaystyle B_{n}^{p}}$ around the origin in this metric is "concave", the topology defined on ${\displaystyle \mathbb {R} ^{n}}$ by the metric ${\displaystyle B_{p}}$ is the usual vector space topology of ${\displaystyle \mathbb {R} ^{n},}$ hence ${\displaystyle \ell _{n}^{p}}$ is a [locally convex](https://en.wikipedia.org/wiki/Locally_convex "Locally convex") topological vector space. Beyond this qualitative statement, a quantitative way to measure the lack of convexity of ${\displaystyle \ell _{n}^{p}}$ is to denote by ${\displaystyle C_{p}(n)}$ the smallest constant ${\displaystyle C}$ such that the scalar multiple ${\displaystyle C\,B_{n}^{p}}$ of the ${\displaystyle p}$ -unit ball contains the convex hull of ${\displaystyle B_{n}^{p},}$ which is equal to ${\displaystyle B_{n}^{1}.}$ The fact that for fixed ${\displaystyle p<1}$ we have 
$$
{\displaystyle C_{p}(n)=n^{{\tfrac {1}{p}}-1}\to \infty ,\quad {\text{as }}n\to \infty }
$$
 shows that the infinite-dimensional sequence space ${\displaystyle \ell ^{p}}$ defined below, is no longer locally convex.

#### When p = 0

There is one ${\displaystyle \ell _{0}}$ norm and another function called the ${\displaystyle \ell _{0}}$ "norm" (with quotation marks).

The mathematical definition of the ${\displaystyle \ell _{0}}$ norm was established by [Banach](https://en.wikipedia.org/wiki/Stefan_Banach "Stefan Banach") 's *[Theory of Linear Operations](https://en.wikipedia.org/w/index.php?title=Theory_of_Linear_Operations&action=edit&redlink=1 "Theory of Linear Operations (page does not exist)")*. The [space](https://en.wikipedia.org/wiki/F-space "F-space") of sequences has a complete metric topology provided by the [F-norm](https://en.wikipedia.org/wiki/F-space "F-space") on the [product metric](https://en.wikipedia.org/wiki/Metric_space#Product_metric_spaces "Metric space"): 
$$
{\displaystyle (x_{n})\mapsto \|x\|:=d(0,x)=\sum _{n}2^{-n}{\frac {|x_{n}|}{1+|x_{n}|}}.}
$$
 The ${\displaystyle \ell _{0}}$ -normed space is studied in functional analysis, probability theory, and harmonic analysis.

Another function was called the ${\displaystyle \ell _{0}}$ "norm" by [David Donoho](https://en.wikipedia.org/wiki/David_Donoho "David Donoho") —whose quotation marks warn that this function is not a proper norm—is the number of non-zero entries of the vector ${\displaystyle x.}$ Many authors [abuse terminology](https://en.wikipedia.org/wiki/Abuse_of_terminology "Abuse of terminology") by omitting the quotation marks. Defining [${\displaystyle 0^{0}=0,}$](https://en.wikipedia.org/wiki/Zero_to_the_power_of_zero "Zero to the power of zero") the zero "norm" of ${\displaystyle x}$ is equal to 
$$
{\displaystyle |x_{1}|^{0}+|x_{2}|^{0}+\cdots +|x_{n}|^{0}.}
$$

![An animated gif of unit circles in p-norms 0.1 through 2 with a step of 0.05.](https://upload.wikimedia.org/wikipedia/commons/1/1f/Lp_space_animation.gif)

An animated gif of p-norms 0.1 through 2 with a step of 0.05.

This is not a [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") because it is not [homogeneous](https://en.wikipedia.org/wiki/Homogeneous_function "Homogeneous function"). For example, scaling the vector ${\displaystyle x}$ by a positive constant does not change the "norm". Despite these defects as a mathematical norm, the non-zero counting "norm" has uses in [scientific computing](https://en.wikipedia.org/wiki/Scientific_computing "Scientific computing"), [information theory](https://en.wikipedia.org/wiki/Information_theory "Information theory"), and [statistics](https://en.wikipedia.org/wiki/Statistics "Statistics") –notably in [compressed sensing](https://en.wikipedia.org/wiki/Compressed_sensing "Compressed sensing") in [signal processing](https://en.wikipedia.org/wiki/Signal_processing "Signal processing") and computational [harmonic analysis](https://en.wikipedia.org/wiki/Harmonic_analysis "Harmonic analysis"). Despite not being a norm, the associated metric, known as [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance "Hamming distance"), is a valid distance, since homogeneity is not required for distances.

## ℓp spaces and sequence spaces

The ${\displaystyle p}$ -norm can be extended to vectors that have an infinite number of components ([sequences](https://en.wikipedia.org/wiki/Sequence "Sequence")), which yields the space ${\displaystyle \ell ^{p}.}$ This contains as special cases:

- ${\displaystyle \ell ^{1},}$ the space of sequences whose series are [absolutely convergent](https://en.wikipedia.org/wiki/Absolute_convergence "Absolute convergence"),
- ${\displaystyle \ell ^{2},}$ the space of **square-summable** sequences, which is a [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"), and
- ${\displaystyle \ell ^{\infty },}$ the space of [bounded sequences](https://en.wikipedia.org/wiki/Bounded_sequence "Bounded sequence").

The space of sequences has a natural vector space structure by applying scalar addition and multiplication. Explicitly, the vector sum and the scalar action for infinite [sequences](https://en.wikipedia.org/wiki/Sequence "Sequence") of real (or [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number")) numbers are given by: 
$$
{\displaystyle {\begin{aligned}&(x_{1},x_{2},\ldots ,x_{n},x_{n+1},\ldots )+(y_{1},y_{2},\ldots ,y_{n},y_{n+1},\ldots )\\={}&(x_{1}+y_{1},x_{2}+y_{2},\ldots ,x_{n}+y_{n},x_{n+1}+y_{n+1},\ldots ),\\[6pt]&\lambda \cdot \left(x_{1},x_{2},\ldots ,x_{n},x_{n+1},\ldots \right)\\={}&(\lambda x_{1},\lambda x_{2},\ldots ,\lambda x_{n},\lambda x_{n+1},\ldots ).\end{aligned}}}
$$

Define the ${\displaystyle p}$ -norm: 
$$
{\displaystyle \|x\|_{p}=\left(|x_{1}|^{p}+|x_{2}|^{p}+\cdots +|x_{n}|^{p}+|x_{n+1}|^{p}+\cdots \right)^{1/p}}
$$

Here, a complication arises, namely that the [series](https://en.wikipedia.org/wiki/Series_\(mathematics\) "Series (mathematics)") on the right is not always convergent, so for example, the sequence made up of only ones, ${\displaystyle (1,1,1,\ldots ),}$ will have an infinite ${\displaystyle p}$ -norm for ${\displaystyle 1\leq p<\infty .}$ The space ${\displaystyle \ell ^{p}}$ is then defined as the set of all infinite sequences of real (or complex) numbers such that the ${\displaystyle p}$ -norm is finite.

One can check that as ${\displaystyle p}$ increases, the set ${\displaystyle \ell ^{p}}$ grows larger. For example, the sequence 
$$
{\displaystyle \left(1,{\frac {1}{2}},\ldots ,{\frac {1}{n}},{\frac {1}{n+1}},\ldots \right)}
$$
 is not in ${\displaystyle \ell ^{1},}$ but it is in ${\displaystyle \ell ^{p}}$ for ${\displaystyle p>1,}$ as the series 
$$
{\displaystyle 1^{p}+{\frac {1}{2^{p}}}+\cdots +{\frac {1}{n^{p}}}+{\frac {1}{(n+1)^{p}}}+\cdots ,}
$$
 diverges for ${\displaystyle p=1}$ (the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_\(mathematics\) "Harmonic series (mathematics)")), but is convergent for ${\displaystyle p>1.}$

One also defines the ${\displaystyle \infty }$ -norm using the [supremum](https://en.wikipedia.org/wiki/Supremum "Supremum"): 
$$
{\displaystyle \|x\|_{\infty }=\sup(|x_{1}|,|x_{2}|,\dotsc ,|x_{n}|,|x_{n+1}|,\ldots )}
$$
 and the corresponding space ${\displaystyle \ell ^{\infty }}$ of all bounded sequences. It turns out that [^1] 
$$
{\displaystyle \|x\|_{\infty }=\lim _{p\to \infty }\|x\|_{p}}
$$
 if the right-hand side is finite, or the left-hand side is infinite. Thus, we will consider ${\displaystyle \ell ^{p}}$ spaces for ${\displaystyle 1\leq p\leq \infty .}$

The ${\displaystyle p}$ -norm thus defined on ${\displaystyle \ell ^{p}}$ is indeed a norm, and ${\displaystyle \ell ^{p}}$ together with this norm is a [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space").

### General ℓp-space

In complete analogy to the preceding definition one can define the space ${\displaystyle \ell ^{p}(I)}$ over a general [index set](https://en.wikipedia.org/wiki/Index_set "Index set") ${\displaystyle I}$ (and ${\displaystyle 1\leq p<\infty }$) as 
$$
{\displaystyle \ell ^{p}(I)=\left\{(x_{i})_{i\in I}\in \mathbb {K} ^{I}:\sum _{i\in I}|x_{i}|^{p}<+\infty \right\},}
$$
 where convergence on the right requires that only countably many summands are nonzero (see also [Absolute convergence over sets](https://en.wikipedia.org/wiki/Absolute_convergence#Absolute_convergence_over_sets "Absolute convergence")). With the norm 
$$
{\displaystyle \|x\|_{p}=\left(\sum _{i\in I}|x_{i}|^{p}\right)^{1/p}}
$$
 the space ${\displaystyle \ell ^{p}(I)}$ becomes a Banach space. In the case where ${\displaystyle I}$ is finite with ${\displaystyle n}$ elements, this construction yields ${\displaystyle \mathbb {R} ^{n}}$ with the ${\displaystyle p}$ -norm defined above. If ${\displaystyle I}$ is countably infinite, this is exactly the sequence space ${\displaystyle \ell ^{p}}$ defined above. For uncountable sets ${\displaystyle I}$ this is a non- [separable](https://en.wikipedia.org/wiki/Separable_space "Separable space") Banach space which can be seen as the [locally convex](https://en.wikipedia.org/wiki/Locally_convex_topological_vector_space "Locally convex topological vector space") [direct limit](https://en.wikipedia.org/wiki/Direct_limit "Direct limit") of ${\displaystyle \ell ^{p}}$ -sequence spaces.[^2]

For ${\displaystyle p=2,}$ the ${\displaystyle \|\,\cdot \,\|_{2}}$ -norm is even induced by a canonical [inner product](https://en.wikipedia.org/wiki/Inner_product "Inner product") ${\displaystyle \langle \,\cdot ,\,\cdot \rangle ,}$ called the *Euclidean inner product*, which means that ${\displaystyle \|\mathbf {x} \|_{2}={\sqrt {\langle \mathbf {x} ,\mathbf {x} \rangle }}}$ holds for all vectors ${\displaystyle \mathbf {x} .}$ This inner product can be expressed in terms of the norm by using the [polarization identity](https://en.wikipedia.org/wiki/Polarization_identity "Polarization identity"). On ${\displaystyle \ell ^{2},}$ it can be defined by 
$$
{\displaystyle \langle \left(x_{i}\right)_{i},\left(y_{n}\right)_{i}\rangle _{\ell ^{2}}~=~\sum _{i}x_{i}{\overline {y_{i}}}.}
$$
 Now consider the case ${\displaystyle p=\infty .}$ Define [^15] 
$$
{\displaystyle \ell ^{\infty }(I)=\{x\in \mathbb {K} ^{I}:\sup \operatorname {range} |x|<+\infty \},}
$$
 where for all ${\displaystyle x}$ [^3] [^16] 
$$
{\displaystyle \|x\|_{\infty }\equiv \inf\{C\in \mathbb {R} _{\geq 0}:|x_{i}|\leq C{\text{ for all }}i\in I\}={\begin{cases}\sup \operatorname {range} |x|&{\text{if }}X\neq \varnothing ,\\0&{\text{if }}X=\varnothing .\end{cases}}}
$$

The index set ${\displaystyle I}$ can be turned into a [measure space](https://en.wikipedia.org/wiki/Measure_space "Measure space") by giving it the [discrete σ-algebra](https://en.wikipedia.org/wiki/%CE%A3-algebra#Simple_set-based_examples "Σ-algebra") and the [counting measure](https://en.wikipedia.org/wiki/Counting_measure "Counting measure"). Then the space ${\displaystyle \ell ^{p}(I)}$ is just a special case of the more general ${\displaystyle L^{p}}$ -space (defined below).

## Lp spaces and Lebesgue integrals

An ${\displaystyle L^{p}}$ space may be defined as a space of measurable functions for which the ${\displaystyle p}$ -th power of the [absolute value](https://en.wikipedia.org/wiki/Absolute_value "Absolute value") is [Lebesgue integrable](https://en.wikipedia.org/wiki/Lebesgue_integrable "Lebesgue integrable"), where functions which agree almost everywhere are identified. More generally, let ${\displaystyle (S,\Sigma ,\mu )}$ be a [measure space](https://en.wikipedia.org/wiki/Measure_space "Measure space") and ${\displaystyle 1\leq p\leq \infty .}$ [^17] When ${\displaystyle p\neq \infty }$, consider the set ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ of all [measurable functions](https://en.wikipedia.org/wiki/Measurable_function "Measurable function") ${\displaystyle f}$ from ${\displaystyle S}$ to ${\displaystyle \mathbb {C} }$ or ${\displaystyle \mathbb {R} }$ whose [absolute value](https://en.wikipedia.org/wiki/Absolute_value "Absolute value") raised to the ${\displaystyle p}$ -th power has a finite integral, or in symbols:[^4] 
$$
{\displaystyle \|f\|_{p}~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\left(\int _{S}|f|^{p}\;\mathrm {d} \mu \right)^{1/p}<\infty .}
$$

To define the set for ${\displaystyle p=\infty ,}$ recall that two functions ${\displaystyle f}$ and ${\displaystyle g}$ defined on ${\displaystyle S}$ are said to be *equal [almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere "Almost everywhere")*, written *${\displaystyle f=g}$ a.e.*, if the set ${\displaystyle \{s\in S:f(s)\neq g(s)\}}$ is measurable and has measure zero. Similarly, a measurable function ${\displaystyle f}$ (and its [absolute value](https://en.wikipedia.org/wiki/Absolute_value "Absolute value")) is *bounded* (or *dominated*) *almost everywhere* by a real number ${\displaystyle C,}$ written *${\displaystyle |f|\leq C}$ a.e.*, if the (necessarily) measurable set ${\displaystyle \{s\in S:|f(s)|>C\}}$ has measure zero. The space ${\displaystyle {\mathcal {L}}^{\infty }(S,\mu )}$ is the set of all measurable functions ${\displaystyle f}$ that are bounded almost everywhere (by some real ${\displaystyle C}$) and ${\displaystyle \|f\|_{\infty }}$ is defined as the [infimum](https://en.wikipedia.org/wiki/Infimum "Infimum") of these bounds: 
$$
{\displaystyle \|f\|_{\infty }~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~\inf\{C\in \mathbb {R} _{\geq 0}:|f(s)|\leq C{\text{ for almost every }}s\}.}
$$
 When ${\displaystyle \mu (S)\neq 0}$ then this is the same as the [essential supremum](https://en.wikipedia.org/wiki/Essential_supremum "Essential supremum") of the absolute value of ${\displaystyle f}$:[^18] 
$$
{\displaystyle \|f\|_{\infty }~=~{\begin{cases}\operatorname {esssup} |f|&{\text{if }}\mu (S)>0,\\0&{\text{if }}\mu (S)=0.\end{cases}}}
$$

For example, if ${\displaystyle f}$ is a measurable function that is equal to ${\displaystyle 0}$ almost everywhere [^19] then ${\displaystyle \|f\|_{p}=0}$ for every ${\displaystyle p}$ and thus ${\displaystyle f\in {\mathcal {L}}^{p}(S,\,\mu )}$ for all ${\displaystyle p.}$

For every positive ${\displaystyle p,}$ the value under ${\displaystyle \|\,\cdot \,\|_{p}}$ of a measurable function ${\displaystyle f}$ and its absolute value ${\displaystyle |f|:S\to [0,\infty ]}$ are always the same (that is, ${\displaystyle \|f\|_{p}=\||f|\|_{p}}$ for all ${\displaystyle p}$) and so a measurable function belongs to ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ if and only if its absolute value does. Because of this, many formulas involving ${\displaystyle p}$ -norms are stated only for non-negative real-valued functions. Consider for example the identity ${\displaystyle \|f\|_{p}^{r}=\|f^{r}\|_{p/r},}$ which holds whenever ${\displaystyle f\geq 0}$ is measurable, ${\displaystyle r>0}$ is real, and ${\displaystyle 0<p\leq \infty }$ (here ${\displaystyle \infty /r\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;\infty }$ when ${\displaystyle p=\infty }$). The non-negativity requirement ${\displaystyle f\geq 0}$ can be removed by substituting ${\displaystyle |f|}$ in for ${\displaystyle f,}$ which gives ${\displaystyle \|\,|f|\,\|_{p}^{r}=\|\,|f|^{r}\,\|_{p/r}.}$ Note in particular that when ${\displaystyle p=r}$ is finite then the formula ${\displaystyle \|f\|_{p}^{p}=\||f|^{p}\|_{1}}$ relates the ${\displaystyle p}$ -norm to the ${\displaystyle 1}$ -norm.

**Seminormed space of ${\displaystyle p}$ -th power integrable functions**

Each set of functions ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ forms a [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") when addition and scalar multiplication are defined pointwise.[^20] That the sum of two ${\displaystyle p}$ -th power integrable functions ${\displaystyle f}$ and ${\displaystyle g}$ is again ${\displaystyle p}$ -th power integrable follows from ${\textstyle \|f+g\|_{p}^{p}\leq 2^{p-1}\left(\|f\|_{p}^{p}+\|g\|_{p}^{p}\right),}$ [^22] although it is also a consequence of *[Minkowski's inequality](https://en.wikipedia.org/wiki/Minkowski_inequality "Minkowski inequality")* 
$$
{\displaystyle \|f+g\|_{p}\leq \|f\|_{p}+\|g\|_{p}}
$$
 which establishes that ${\displaystyle \|\cdot \|_{p}}$ satisfies the [triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality "Triangle inequality") for ${\displaystyle 1\leq p\leq \infty }$ (the triangle inequality does not hold for ${\displaystyle 0<p<1}$). That ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ is closed under scalar multiplication is due to ${\displaystyle \|\cdot \|_{p}}$ being [absolutely homogeneous](https://en.wikipedia.org/wiki/Absolute_homogeneity "Absolute homogeneity"), which means that ${\displaystyle \|sf\|_{p}=|s|\|f\|_{p}}$ for every scalar ${\displaystyle s}$ and every function ${\displaystyle f.}$

[Absolute homogeneity](https://en.wikipedia.org/wiki/Absolute_homogeneity "Absolute homogeneity"), the [triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality "Triangle inequality"), and non-negativity are the defining properties of a [seminorm](https://en.wikipedia.org/wiki/Seminorm "Seminorm"). Thus ${\displaystyle \|\cdot \|_{p}}$ is a seminorm and the set ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ of ${\displaystyle p}$ -th power integrable functions together with the function ${\displaystyle \|\cdot \|_{p}}$ defines a [seminormed vector space](https://en.wikipedia.org/wiki/Seminormed_vector_space "Seminormed vector space"). In general, the [seminorm](https://en.wikipedia.org/wiki/Seminorm "Seminorm") ${\displaystyle \|\cdot \|_{p}}$ is not a [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") because there might exist measurable functions ${\displaystyle f}$ that satisfy ${\displaystyle \|f\|_{p}=0}$ but are not *identically* equal to ${\displaystyle 0}$ [^19] (${\displaystyle \|\cdot \|_{p}}$ is a norm if and only if no such ${\displaystyle f}$ exists).

**Zero sets of ${\displaystyle p}$ -seminorms**

If ${\displaystyle f}$ is measurable and equals ${\displaystyle 0}$ a.e. then ${\displaystyle \|f\|_{p}=0}$ for all positive ${\displaystyle p\leq \infty .}$ On the other hand, if ${\displaystyle f}$ is a measurable function for which there exists some ${\displaystyle 0<p\leq \infty }$ such that ${\displaystyle \|f\|_{p}=0}$ then ${\displaystyle f=0}$ almost everywhere. When ${\displaystyle p}$ is finite then this follows from the ${\displaystyle p=1}$ case and the formula ${\displaystyle \|f\|_{p}^{p}=\||f|^{p}\|_{1}}$ mentioned above.

Thus if ${\displaystyle p\leq \infty }$ is positive and ${\displaystyle f}$ is any measurable function, then ${\displaystyle \|f\|_{p}=0}$ if and only if ${\displaystyle f=0}$ [almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere "Almost everywhere"). Since the right hand side (${\displaystyle f=0}$ a.e.) does not mention ${\displaystyle p,}$ it follows that all ${\displaystyle \|\cdot \|_{p}}$ have the same [zero set](https://en.wikipedia.org/wiki/Zero_set "Zero set") (it does not depend on ${\displaystyle p}$). So denote this common set by 
$$
{\displaystyle {\mathcal {N}}\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;\{f:f=0\ \mu {\text{-almost everywhere}}\}=\{f\in {\mathcal {L}}^{p}(S,\,\mu ):\|f\|_{p}=0\}\qquad \forall \ p.}
$$
 This set is a vector subspace of ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ for every positive ${\displaystyle p\leq \infty .}$

**Quotient vector space**

Like every [seminorm](https://en.wikipedia.org/wiki/Seminorm "Seminorm"), the seminorm ${\displaystyle \|\cdot \|_{p}}$ induces a [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") (defined shortly) on the canonical [quotient vector space](https://en.wikipedia.org/wiki/Quotient_space_\(linear_algebra\) "Quotient space (linear algebra)") of ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ by its vector subspace ${\textstyle {\mathcal {N}}=\{f\in {\mathcal {L}}^{p}(S,\,\mu ):\|f\|_{p}=0\}.}$ This normed quotient space is called *Lebesgue space* and it is the subject of this article. We begin by defining the quotient vector space.

Given any ${\displaystyle f\in {\mathcal {L}}^{p}(S,\,\mu ),}$ the [coset](https://en.wikipedia.org/wiki/Coset "Coset") ${\displaystyle f+{\mathcal {N}}\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;\{f+h:h\in {\mathcal {N}}\}}$ consists of all measurable functions ${\displaystyle g}$ that are equal to ${\displaystyle f}$ [almost everywhere](https://en.wikipedia.org/wiki/Almost_everywhere "Almost everywhere"). The set of all cosets, typically denoted by 
$$
{\displaystyle {\mathcal {L}}^{p}(S,\mu )/{\mathcal {N}}~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~~\{f+{\mathcal {N}}:f\in {\mathcal {L}}^{p}(S,\mu )\},}
$$
 forms a vector space with origin ${\displaystyle 0+{\mathcal {N}}={\mathcal {N}}}$ when vector addition and scalar multiplication are defined by ${\displaystyle (f+{\mathcal {N}})+(g+{\mathcal {N}})\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;(f+g)+{\mathcal {N}}}$ and ${\displaystyle s(f+{\mathcal {N}})\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;(sf)+{\mathcal {N}}.}$ This particular quotient vector space will be denoted by 
$$
{\displaystyle L^{p}(S,\,\mu )~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~{\mathcal {L}}^{p}(S,\mu )/{\mathcal {N}}.}
$$
 Two cosets are equal ${\displaystyle f+{\mathcal {N}}=g+{\mathcal {N}}}$ if and only if ${\displaystyle g\in f+{\mathcal {N}}}$ (or equivalently, ${\displaystyle f-g\in {\mathcal {N}}}$), which happens if and only if ${\displaystyle f=g}$ almost everywhere; if this is the case then ${\displaystyle f}$ and ${\displaystyle g}$ are identified in the quotient space. Hence, strictly speaking ${\displaystyle L^{p}(S,\,\mu )}$ consists of [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class "Equivalence class") of functions.[^5]

**The ${\displaystyle p}$ -norm on the quotient vector space**

Given any ${\displaystyle f\in {\mathcal {L}}^{p}(S,\,\mu ),}$ the value of the seminorm ${\displaystyle \|\cdot \|_{p}}$ on the [coset](https://en.wikipedia.org/wiki/Coset "Coset") ${\displaystyle f+{\mathcal {N}}=\{f+h:h\in {\mathcal {N}}\}}$ is constant and equal to ${\displaystyle \|f\|_{p};}$ denote this unique value by ${\displaystyle \|f+{\mathcal {N}}\|_{p},}$ so that: 
$$
{\displaystyle \|f+{\mathcal {N}}\|_{p}\;{\stackrel {\scriptscriptstyle {\text{def}}}{=}}\;\|f\|_{p}.}
$$
 This assignment ${\displaystyle f+{\mathcal {N}}\mapsto \|f+{\mathcal {N}}\|_{p}}$ defines a map, which will also be denoted by ${\displaystyle \|\cdot \|_{p},}$ on the [quotient vector space](https://en.wikipedia.org/wiki/Quotient_space_\(linear_algebra\) "Quotient space (linear algebra)") 
$$
{\displaystyle L^{p}(S,\mu )~~{\stackrel {\scriptscriptstyle {\text{def}}}{=}}~~{\mathcal {L}}^{p}(S,\mu )/{\mathcal {N}}~=~\{f+{\mathcal {N}}:f\in {\mathcal {L}}^{p}(S,\mu )\}.}
$$
 This map is a [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") on ${\displaystyle L^{p}(S,\mu )}$ called the *${\displaystyle p}$ -norm*. The value ${\displaystyle \|f+{\mathcal {N}}\|_{p}}$ of a coset ${\displaystyle f+{\mathcal {N}}}$ is independent of the particular function ${\displaystyle f}$ that was chosen to represent the coset, meaning that if ${\displaystyle {\mathcal {C}}\in L^{p}(S,\mu )}$ is any coset then ${\displaystyle \|{\mathcal {C}}\|_{p}=\|f\|_{p}}$ for every ${\displaystyle f\in {\mathcal {C}}}$ (since ${\displaystyle {\mathcal {C}}=f+{\mathcal {N}}}$ for every ${\displaystyle f\in {\mathcal {C}}}$).

**The Lebesgue ${\displaystyle L^{p}}$ space**

The [normed vector space](https://en.wikipedia.org/wiki/Normed_vector_space "Normed vector space") ${\displaystyle \left(L^{p}(S,\mu ),\|\cdot \|_{p}\right)}$ is called *${\displaystyle L^{p}}$ space* or the *Lebesgue space* of ${\displaystyle p}$ -th power integrable functions and it is a [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space") for every ${\displaystyle 1\leq p\leq \infty }$ (meaning that it is a [complete metric space](https://en.wikipedia.org/wiki/Complete_metric_space "Complete metric space"), a result that is sometimes called the [Riesz–Fischer theorem](https://en.wikipedia.org/wiki/Riesz%E2%80%93Fischer_theorem#Completeness_of_Lp,_0_%3C_p_%E2%89%A4_%E2%88%9E "Riesz–Fischer theorem")). When the underlying measure space ${\displaystyle S}$ is understood then ${\displaystyle L^{p}(S,\mu )}$ is often abbreviated ${\displaystyle L^{p}(\mu ),}$ or even just ${\displaystyle L^{p}.}$ Depending on the author, the subscript notation ${\displaystyle L_{p}}$ might denote either ${\displaystyle L^{p}(S,\mu )}$ or ${\displaystyle L^{1/p}(S,\mu ).}$

If the seminorm ${\displaystyle \|\cdot \|_{p}}$ on ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ happens to be a norm (which happens if and only if ${\displaystyle {\mathcal {N}}=\{0\}}$) then the normed space ${\displaystyle \left({\mathcal {L}}^{p}(S,\,\mu ),\|\cdot \|_{p}\right)}$ will be [linearly](https://en.wikipedia.org/wiki/Linear_map "Linear map") [isometrically isomorphic](https://en.wikipedia.org/wiki/Isometrically_isomorphic "Isometrically isomorphic") to the normed quotient space ${\displaystyle \left(L^{p}(S,\mu ),\|\cdot \|_{p}\right)}$ via the canonical map ${\displaystyle g\in {\mathcal {L}}^{p}(S,\,\mu )\mapsto \{g\}}$ (since ${\displaystyle g+{\mathcal {N}}=\{g\}}$); in other words, they will be, [up to](https://en.wikipedia.org/wiki/Up_to "Up to") a [linear isometry](https://en.wikipedia.org/wiki/Linear_isometry "Linear isometry"), the same normed space and so they may both be called " ${\displaystyle L^{p}}$ space".

The above definitions generalize to [Bochner spaces](https://en.wikipedia.org/wiki/Bochner_space "Bochner space").

In general, this process cannot be reversed: there is no consistent way to define a "canonical" representative of each coset of ${\displaystyle {\mathcal {N}}}$ in ${\displaystyle L^{p}.}$ For ${\displaystyle L^{\infty },}$ however, there is a [theory of lifts](https://en.wikipedia.org/wiki/Lifting_theory "Lifting theory") enabling such recovery.

### Special cases

For ${\displaystyle 1\leq p\leq \infty }$ the ${\displaystyle \ell ^{p}}$ spaces are a special case of ${\displaystyle L^{p}}$ spaces; when ${\displaystyle S}$ are the [natural numbers](https://en.wikipedia.org/wiki/Natural_number "Natural number") ${\displaystyle \mathbb {N} }$ and ${\displaystyle \mu }$ is the [counting measure](https://en.wikipedia.org/wiki/Counting_measure "Counting measure"). More generally, if one considers any set ${\displaystyle S}$ with the counting measure, the resulting ${\displaystyle L^{p}}$ space is denoted ${\displaystyle \ell ^{p}(S).}$ For example, ${\displaystyle \ell ^{p}(\mathbb {Z} )}$ is the space of all sequences indexed by the integers, and when defining the ${\displaystyle p}$ -norm on such a space, one sums over all the integers. The space ${\displaystyle \ell ^{p}(n),}$ where ${\displaystyle n}$ is the set with ${\displaystyle n}$ elements, is ${\displaystyle \mathbb {R} ^{n}}$ with its ${\displaystyle p}$ -norm as defined above.

Similar to ${\displaystyle \ell ^{2}}$ spaces, ${\displaystyle L^{2}}$ is the only [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space") among ${\displaystyle L^{p}}$ spaces. In the complex case, the inner product on ${\displaystyle L^{2}}$ is defined by 
$$
{\displaystyle \langle f,g\rangle =\int _{S}f(x){\overline {g(x)}}\,\mathrm {d} \mu (x).}
$$
 Functions in ${\displaystyle L^{2}}$ are sometimes called **[square-integrable functions](https://en.wikipedia.org/wiki/Square-integrable_function "Square-integrable function")**, **quadratically integrable functions** or **square-summable functions**, but sometimes these terms are reserved for functions that are square-integrable in some other sense, such as in the sense of a [Riemann integral](https://en.wikipedia.org/wiki/Riemann_integral "Riemann integral") ([Titchmarsh 1976](#CITEREFTitchmarsh1976)).

As any Hilbert space, every space ${\displaystyle L^{2}}$ is linearly isometric to a suitable ${\displaystyle \ell ^{2}(I),}$ where the cardinality of the set ${\displaystyle I}$ is the cardinality of an arbitrary basis for this particular ${\displaystyle L^{2}.}$

If we use complex-valued functions, the space ${\displaystyle L^{\infty }}$ is a [commutative](https://en.wikipedia.org/wiki/Commutative "Commutative") [C\*-algebra](https://en.wikipedia.org/wiki/C*-algebra "C*-algebra") with pointwise multiplication and conjugation. For many measure spaces, including all sigma-finite ones, it is in fact a commutative [von Neumann algebra](https://en.wikipedia.org/wiki/Von_Neumann_algebra "Von Neumann algebra"). An element of ${\displaystyle L^{\infty }}$ defines a [bounded operator](https://en.wikipedia.org/wiki/Bounded_operator "Bounded operator") on any ${\displaystyle L^{p}}$ space by [multiplication](https://en.wikipedia.org/wiki/Multiplication_operator "Multiplication operator").

### When 0 < p < 1

If ${\displaystyle 0<p<1,}$ then ${\displaystyle L^{p}(\mu )}$ can be defined as above, that is: 
$$
{\displaystyle N_{p}(f)=\int _{S}|f|^{p}\,d\mu <\infty .}
$$
 In this case, however, the ${\displaystyle p}$ -norm ${\displaystyle \|f\|_{p}=N_{p}(f)^{1/p}}$ does not satisfy the triangle inequality and defines only a [quasi-norm](https://en.wikipedia.org/wiki/Quasi-norm "Quasi-norm"). The inequality ${\displaystyle (a+b)^{p}\leq a^{p}+b^{p},}$ valid for ${\displaystyle a,b\geq 0,}$ implies that 
$$
{\displaystyle N_{p}(f+g)\leq N_{p}(f)+N_{p}(g)}
$$
 and so the function 
$$
{\displaystyle d_{p}(f,g)=N_{p}(f-g)=\|f-g\|_{p}^{p}}
$$
 is a metric on ${\displaystyle L^{p}(\mu ).}$ The resulting metric space is [complete](https://en.wikipedia.org/wiki/Complete_metric_space "Complete metric space").[^6]

In this setting ${\displaystyle L^{p}}$ satisfies a *reverse Minkowski inequality*, that is for ${\displaystyle u,v\in L^{p}}$ 
$$
{\displaystyle {\Big \|}|u|+|v|{\Big \|}_{p}\geq \|u\|_{p}+\|v\|_{p}}
$$

This result may be used to prove [Clarkson's inequalities](https://en.wikipedia.org/wiki/Clarkson%27s_inequalities "Clarkson's inequalities"), which are in turn used to establish the [uniform convexity](https://en.wikipedia.org/wiki/Uniformly_convex_space "Uniformly convex space") of the spaces ${\displaystyle L^{p}}$ for ${\displaystyle 1<p<\infty }$ ([Adams & Fournier 2003](#CITEREFAdamsFournier2003)).

The space ${\displaystyle L^{p}}$ for ${\displaystyle 0<p<1}$ is an [F-space](https://en.wikipedia.org/wiki/F-space "F-space"): it admits a complete translation-invariant metric with respect to which the vector space operations are continuous. It is the prototypical example of an [F-space](https://en.wikipedia.org/wiki/F-space "F-space") that, for most reasonable measure spaces, is not [locally convex](https://en.wikipedia.org/wiki/Locally_convex_topological_vector_space "Locally convex topological vector space"): in ${\displaystyle \ell ^{p}}$ or ${\displaystyle L^{p}([0,1]),}$ every open convex set containing the ${\displaystyle 0}$ function is unbounded for the ${\displaystyle p}$ -quasi-norm; therefore, the ${\displaystyle 0}$ vector does not possess a fundamental system of convex neighborhoods. Specifically, this is true if the measure space ${\displaystyle S}$ contains an infinite family of disjoint measurable sets of finite positive measure.

The only nonempty convex open set in ${\displaystyle L^{p}([0,1])}$ is the entire space. Consequently, there are no nonzero continuous linear functionals on ${\displaystyle L^{p}([0,1]);}$ the [continuous dual space](https://en.wikipedia.org/wiki/Continuous_dual_space "Continuous dual space") is the zero space. In the case of the [counting measure](https://en.wikipedia.org/wiki/Counting_measure "Counting measure") on the natural numbers (i.e. ${\displaystyle L^{p}(\mu )=\ell ^{p}}$), the bounded linear functionals on ${\displaystyle \ell ^{p}}$ are exactly those that are bounded on ${\displaystyle \ell ^{1}}$, i.e., those given by sequences in ${\displaystyle \ell ^{\infty }.}$ Although ${\displaystyle \ell ^{p}}$ does contain non-trivial convex open sets, it fails to have enough of them to give a base for the topology.

Having no linear functionals is highly undesirable for the purposes of doing analysis. In case of the Lebesgue measure on ${\displaystyle \mathbb {R} ^{n},}$ rather than work with ${\displaystyle L^{p}}$ for ${\displaystyle 0<p<1,}$ it is common to work with the [Hardy space](https://en.wikipedia.org/wiki/Hardy_space "Hardy space") *H <sup>p</sup>* whenever possible, as this has quite a few linear functionals: enough to distinguish points from one another. However, the [Hahn–Banach theorem](https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem "Hahn–Banach theorem") still fails in *H <sup>p</sup>* for ${\displaystyle p<1}$ ([Duren 1970](#CITEREFDuren1970), §7.5).

## Properties

### Hölder's inequality

Suppose ${\displaystyle p,q,r\in [1,\infty ]}$ satisfy ${\displaystyle {\tfrac {1}{p}}+{\tfrac {1}{q}}={\tfrac {1}{r}}}$. If ${\displaystyle f\in L^{p}(S,\mu )}$ and ${\displaystyle g\in L^{q}(S,\mu )}$ then ${\displaystyle fg\in L^{r}(S,\mu )}$ and [^7] 
$$
{\displaystyle \|fg\|_{r}~\leq ~\|f\|_{p}\,\|g\|_{q}.}
$$

This inequality, called [Hölder's inequality](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality "Hölder's inequality"), is in some sense optimal since if ${\displaystyle r=1}$ and ${\displaystyle f}$ is a measurable function such that 
$$
{\displaystyle \sup _{\|g\|_{q}\leq 1}\,\int _{S}|fg|\,\mathrm {d} \mu ~<~\infty }
$$
 where the [supremum](https://en.wikipedia.org/wiki/Supremum "Supremum") is taken over the closed unit ball of ${\displaystyle L^{q}(S,\mu ),}$ then ${\displaystyle f\in L^{p}(S,\mu )}$ and 
$$
{\displaystyle \|f\|_{p}~=~\sup _{\|g\|_{q}\leq 1}\,\int _{S}fg\,\mathrm {d} \mu .}
$$

### Generalized Minkowski inequality

[Minkowski inequality](https://en.wikipedia.org/wiki/Minkowski_inequality "Minkowski inequality"), which states that ${\displaystyle \|\cdot \|_{p}}$ satisfies the [triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality "Triangle inequality"), can be generalized: If the measurable function ${\displaystyle F:M\times N\to \mathbb {R} }$ is non-negative (where ${\displaystyle (M,\mu )}$ and ${\displaystyle (N,\nu )}$ are measure spaces) then for all ${\displaystyle 1\leq p\leq q\leq \infty ,}$ [^8] 
$$
{\displaystyle \left\|\left\|F(\,\cdot ,n)\right\|_{L^{p}(M,\mu )}\right\|_{L^{q}(N,\nu )}~\leq ~\left\|\left\|F(m,\cdot )\right\|_{L^{q}(N,\nu )}\right\|_{L^{p}(M,\mu )}\ .}
$$

### Atomic decomposition

If ${\displaystyle 1\leq p<\infty }$ then every non-negative ${\displaystyle f\in L^{p}(\mu )}$ has an *atomic decomposition*,[^9] meaning that there exist a sequence ${\displaystyle (r_{n})_{n\in \mathbb {Z} }}$ of non-negative real numbers and a sequence of non-negative functions ${\displaystyle (f_{n})_{n\in \mathbb {Z} },}$ called *the atoms*, whose supports ${\displaystyle \left(\operatorname {supp} f_{n}\right)_{n\in \mathbb {Z} }}$ are [pairwise disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets "Disjoint sets") of measure ${\displaystyle \mu \left(\operatorname {supp} f_{n}\right)\leq 2^{n+1},}$ such that 
$$
{\displaystyle f~=~\sum _{n\in \mathbb {Z} }r_{n}\,f_{n}\,,}
$$
 and for every integer ${\displaystyle n\in \mathbb {Z} ,}$ 
$$
{\displaystyle \|f_{n}\|_{\infty }~\leq ~2^{-{\tfrac {n}{p}}}\,,}
$$
 and 
$$
{\displaystyle {\tfrac {1}{2}}\|f\|_{p}^{p}~\leq ~\sum _{n\in \mathbb {Z} }r_{n}^{p}~\leq ~2\|f\|_{p}^{p}\,,}
$$
 and where moreover, the sequence of functions ${\displaystyle (r_{n}f_{n})_{n\in \mathbb {Z} }}$ depends only on ${\displaystyle f}$ (it is independent of ${\displaystyle p}$).[^9] These inequalities guarantee that ${\displaystyle \|f_{n}\|_{p}^{p}\leq 2}$ for all integers ${\displaystyle n}$ while the supports of ${\displaystyle (f_{n})_{n\in \mathbb {Z} }}$ being pairwise disjoint implies [^9] 
$$
{\displaystyle \|f\|_{p}^{p}~=~\sum _{n\in \mathbb {Z} }r_{n}^{p}\,\|f_{n}\|_{p}^{p}\,.}
$$

An atomic decomposition can be explicitly given by first defining for every integer ${\displaystyle n\in \mathbb {Z} ,}$ [^9] [^21] 
$$
{\displaystyle t_{n}=\inf\{t\in \mathbb {R} :\mu (f>t)<2^{n}\}}
$$
 and then letting 
$$
{\displaystyle r_{n}~=~2^{n/p}\,t_{n}~{\text{ and }}\quad f_{n}~=~{\frac {f}{r_{n}}}\,\mathbf {1} _{(t_{n+1}<f\leq t_{n})}}
$$
 where ${\displaystyle \mu (f>t)=\mu (\{s:f(s)>t\})}$ denotes the measure of the set ${\displaystyle (f>t):=\{s\in S:f(s)>t\}}$ and ${\displaystyle \mathbf {1} _{(t_{n+1}<f\leq t_{n})}}$ denotes the [indicator function](https://en.wikipedia.org/wiki/Indicator_function "Indicator function") of the set ${\displaystyle (t_{n+1}<f\leq t_{n}):=\{s\in S:t_{n+1}<f(s)\leq t_{n}\}.}$ The sequence ${\displaystyle (t_{n})_{n\in \mathbb {Z} }}$ is decreasing and converges to ${\displaystyle 0}$ as ${\displaystyle n\to \infty .}$ [^9] Consequently, if ${\displaystyle t_{n}=0}$ then ${\displaystyle t_{n+1}=0}$ and ${\displaystyle (t_{n+1}<f\leq t_{n})=\varnothing }$ so that ${\displaystyle f_{n}={\frac {1}{r_{n}}}\,f\,\mathbf {1} _{(t_{n+1}<f\leq t_{n})}}$ is identically equal to ${\displaystyle 0}$ (in particular, the division ${\displaystyle {\tfrac {1}{r_{n}}}}$ by ${\displaystyle r_{n}=0}$ causes no issues).

The [complementary cumulative distribution function](https://en.wikipedia.org/wiki/Complementary_cumulative_distribution_function "Complementary cumulative distribution function") ${\displaystyle t\in \mathbb {R} \mapsto \mu (|f|>t)}$ of ${\displaystyle |f|=f}$ that was used to define the ${\displaystyle t_{n}}$ also appears in the definition of the weak ${\displaystyle L^{p}}$ -norm (given below) and can be used to express the ${\displaystyle p}$ -norm ${\displaystyle \|\cdot \|_{p}}$ (for ${\displaystyle 1\leq p<\infty }$) of ${\displaystyle f\in L^{p}(S,\mu )}$ as the integral [^9] 
$$
{\displaystyle \|f\|_{p}^{p}~=~p\,\int _{0}^{\infty }t^{p-1}\mu (|f|>t)\,\mathrm {d} t\,,}
$$
 where the integration is with respect to the usual Lebesgue measure on ${\displaystyle (0,\infty ).}$

### Dual spaces

The [dual space](https://en.wikipedia.org/wiki/Continuous_dual "Continuous dual") of ${\displaystyle L^{p}(\mu )}$ for ${\displaystyle 1<p<\infty }$ has a natural isomorphism with ${\displaystyle L^{q}(\mu ),}$ where ${\displaystyle q}$ is such that ${\displaystyle {\tfrac {1}{p}}+{\tfrac {1}{q}}=1}$. This isomorphism associates ${\displaystyle g\in L^{q}(\mu )}$ with the functional ${\displaystyle \kappa _{p}(g)\in L^{p}(\mu )^{*}}$ defined by 
$$
{\displaystyle f\mapsto \kappa _{p}(g)(f)=\int fg\,\mathrm {d} \mu }
$$
 for every ${\displaystyle f\in L^{p}(\mu ).}$

${\displaystyle \kappa _{p}:L^{q}(\mu )\to L^{p}(\mu )^{*}}$ is a well defined continuous linear mapping which is an [isometry](https://en.wikipedia.org/wiki/Isometry "Isometry") by the [extremal case](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality#Extremal_equality "Hölder's inequality") of Hölder's inequality. If ${\displaystyle (S,\Sigma ,\mu )}$ is a [${\displaystyle \sigma }$ -finite measure space](https://en.wikipedia.org/wiki/Measure_space#Important_classes_of_measure_spaces "Measure space") one can use the [Radon–Nikodym theorem](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem "Radon–Nikodym theorem") to show that any ${\displaystyle G\in L^{p}(\mu )^{*}}$ can be expressed this way, i.e., ${\displaystyle \kappa _{p}}$ is an [isometric isomorphism](https://en.wikipedia.org/wiki/Isometry#Definition "Isometry") of [Banach spaces](https://en.wikipedia.org/wiki/Banach_space "Banach space").[^10] Hence, it is usual to say simply that ${\displaystyle L^{q}(\mu )}$ is the [continuous dual space](https://en.wikipedia.org/wiki/Continuous_dual_space "Continuous dual space") of ${\displaystyle L^{p}(\mu ).}$

For ${\displaystyle 1<p<\infty ,}$ the space ${\displaystyle L^{p}(\mu )}$ is [reflexive](https://en.wikipedia.org/wiki/Reflexive_space "Reflexive space"). Let ${\displaystyle \kappa _{p}}$ be as above and let ${\displaystyle \kappa _{q}:L^{p}(\mu )\to L^{q}(\mu )^{*}}$ be the corresponding linear isometry. Consider the map from ${\displaystyle L^{p}(\mu )}$ to ${\displaystyle L^{p}(\mu )^{**},}$ obtained by composing ${\displaystyle \kappa _{q}}$ with the [transpose](https://en.wikipedia.org/wiki/Dual_space#Transpose_of_a_continuous_linear_map "Dual space") (or adjoint) of the inverse of ${\displaystyle \kappa _{p}:}$

$$
{\displaystyle j_{p}:L^{p}(\mu )\mathrel {\overset {\kappa _{q}}{\longrightarrow }} L^{q}(\mu )^{*}\mathrel {\overset {\left(\kappa _{p}^{-1}\right)^{*}}{\longrightarrow }} L^{p}(\mu )^{**}}
$$

This map coincides with the [canonical embedding](https://en.wikipedia.org/wiki/Reflexive_space#Definitions "Reflexive space") ${\displaystyle J}$ of ${\displaystyle L^{p}(\mu )}$ into its bidual. Moreover, the map ${\displaystyle j_{p}}$ is onto, as composition of two onto isometries, and this proves reflexivity.

If the measure ${\displaystyle \mu }$ on ${\displaystyle S}$ is [sigma-finite](https://en.wikipedia.org/wiki/Sigma-finite "Sigma-finite"), then the dual of ${\displaystyle L^{1}(\mu )}$ is isometrically isomorphic to ${\displaystyle L^{\infty }(\mu )}$ (more precisely, the map ${\displaystyle \kappa _{1}}$ corresponding to ${\displaystyle p=1}$ is an isometry from ${\displaystyle L^{\infty }(\mu )}$ onto ${\displaystyle L^{1}(\mu )^{*}.}$

The dual of ${\displaystyle L^{\infty }(\mu )}$ is subtler. Elements of ${\displaystyle L^{\infty }(\mu )^{*}}$ can be identified with bounded signed *finitely* additive measures on ${\displaystyle S}$ that are [absolutely continuous](https://en.wikipedia.org/wiki/Absolutely_continuous "Absolutely continuous") with respect to ${\displaystyle \mu .}$ See [ba space](https://en.wikipedia.org/wiki/Ba_space "Ba space") for more details. If we assume the axiom of choice, this space is much bigger than ${\displaystyle L^{1}(\mu )}$ except in some trivial cases. However, [Saharon Shelah](https://en.wikipedia.org/wiki/Saharon_Shelah "Saharon Shelah") proved that there are relatively consistent extensions of [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory "Zermelo–Fraenkel set theory") (ZF + [DC](https://en.wikipedia.org/wiki/Axiom_of_dependent_choice "Axiom of dependent choice") + "Every subset of the real numbers has the [Baire property](https://en.wikipedia.org/wiki/Baire_property "Baire property") ") in which the dual of ${\displaystyle \ell ^{\infty }}$ is ${\displaystyle \ell ^{1}.}$ [^11]

### Embeddings

Colloquially, if ${\displaystyle 1\leq p<q\leq \infty ,}$ then ${\displaystyle L^{p}(S,\mu )}$ contains functions that are more locally singular, while elements of ${\displaystyle L^{q}(S,\mu )}$ can be more spread out. Consider the [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure "Lebesgue measure") on the half line ${\displaystyle (0,\infty ).}$ A continuous function in ${\displaystyle L^{1}}$ might blow up near ${\displaystyle 0}$ but must decay sufficiently fast toward infinity. On the other hand, continuous functions in ${\displaystyle L^{\infty }}$ need not decay at all but no blow-up is allowed. More formally:[^12]

1. If ${\displaystyle 0<p<q<\infty }$: ${\displaystyle L^{q}(S,\mu )\subseteq L^{p}(S,\mu )}$ if and only if ${\displaystyle S}$ does not contain sets of finite but arbitrarily large measure (e.g. any [finite measure](https://en.wikipedia.org/wiki/Finite_measure "Finite measure")).
2. If ${\displaystyle 0<p<q\leq \infty }$: ${\displaystyle L^{p}(S,\mu )\subseteq L^{q}(S,\mu )}$ if and only if ${\displaystyle S}$ does not contain sets of non-zero but arbitrarily small measure (e.g. the [counting measure](https://en.wikipedia.org/wiki/Counting_measure "Counting measure")).

Neither condition holds for the Lebesgue measure on the real line while both conditions holds for the [counting measure](https://en.wikipedia.org/wiki/Counting_measure "Counting measure") on any finite set. As a consequence of the [closed graph theorem](https://en.wikipedia.org/wiki/Closed_graph_theorem "Closed graph theorem"), the embedding is continuous, i.e., the [identity operator](https://en.wikipedia.org/wiki/Identity_operator "Identity operator") is a bounded linear map from ${\displaystyle L^{q}}$ to ${\displaystyle L^{p}}$ in the first case and ${\displaystyle L^{p}}$ to ${\displaystyle L^{q}}$ in the second. Indeed, if the domain ${\displaystyle S}$ has finite measure, one can make the following explicit calculation using [Hölder's inequality](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality "Hölder's inequality") 
$$
{\displaystyle \ \|\mathbf {1} f^{p}\|_{1}\leq \|\mathbf {1} \|_{q/(q-p)}\|f^{p}\|_{q/p}}
$$
 leading to 
$$
{\displaystyle \ \|f\|_{p}\leq \mu (S)^{1/p-1/q}\|f\|_{q}.}
$$

The constant appearing in the above inequality is optimal, in the sense that the [operator norm](https://en.wikipedia.org/wiki/Operator_norm "Operator norm") of the identity ${\displaystyle I:L^{q}(S,\mu )\to L^{p}(S,\mu )}$ is precisely 
$$
{\displaystyle \|I\|_{q,p}=\mu (S)^{1/p-1/q}}
$$
 the case of equality being achieved exactly when ${\displaystyle f=1}$ ${\displaystyle \mu }$ -almost-everywhere.

### Dense subspaces

Let ${\displaystyle 1\leq p<\infty }$ and ${\displaystyle (S,\Sigma ,\mu )}$ be a measure space and consider an integrable [simple function](https://en.wikipedia.org/wiki/Simple_function "Simple function") ${\displaystyle f}$ on ${\displaystyle S}$ given by 
$$
{\displaystyle f=\sum _{j=1}^{n}a_{j}\mathbf {1} _{A_{j}},}
$$
 where ${\displaystyle a_{j}}$ are scalars, ${\displaystyle A_{j}\in \Sigma }$ has finite measure and ${\displaystyle {\mathbf {1} }_{A_{j}}}$ is the [indicator function](https://en.wikipedia.org/wiki/Indicator_function "Indicator function") of the set ${\displaystyle A_{j},}$ for ${\displaystyle j=1,\dots ,n.}$ By construction of the [integral](https://en.wikipedia.org/wiki/Lebesgue_integration "Lebesgue integration"), the vector space of integrable simple functions is [dense](https://en.wikipedia.org/wiki/Dense_set "Dense set") in ${\displaystyle L^{p}(S,\Sigma ,\mu ).}$

More can be said when ${\displaystyle S}$ is a [normal](https://en.wikipedia.org/wiki/Normal_space "Normal space") [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") and ${\displaystyle \Sigma }$ its [Borel 𝜎–algebra](https://en.wikipedia.org/wiki/Borel_algebra "Borel algebra").

Suppose ${\displaystyle V\subseteq S}$ is an open set with ${\displaystyle \mu (V)<\infty .}$ Then for every Borel set ${\displaystyle A\in \Sigma }$ contained in ${\displaystyle V}$ there exist a closed set ${\displaystyle F}$ and an open set ${\displaystyle U}$ such that 
$$
{\displaystyle F\subseteq A\subseteq U\subseteq V\quad {\text{and}}\quad \mu (U\setminus F)=\mu (U)-\mu (F)<\varepsilon ,}
$$
 for every ${\displaystyle \varepsilon >0}$. Subsequently, there exists a [Urysohn function](https://en.wikipedia.org/wiki/Urysohn_function "Urysohn function") ${\displaystyle 0\leq \varphi \leq 1}$ on ${\displaystyle S}$ that is ${\displaystyle 1}$ on ${\displaystyle F}$ and ${\displaystyle 0}$ on ${\displaystyle S\setminus U,}$ with 
$$
{\displaystyle \int _{S}|\mathbf {1} _{A}-\varphi |\,\mathrm {d} \mu <\varepsilon \,.}
$$

If ${\displaystyle S}$ can be covered by an increasing sequence ${\displaystyle (V_{n})}$ of open sets that have finite measure, then the space of ${\displaystyle p}$ –integrable continuous functions is dense in ${\displaystyle L^{p}(S,\Sigma ,\mu ).}$ More precisely, one can use bounded continuous functions that vanish outside one of the open sets ${\displaystyle V_{n}.}$

This applies in particular when ${\displaystyle S=\mathbb {R} ^{d}}$ and when ${\displaystyle \mu }$ is the Lebesgue measure. For example, the space of continuous and compactly supported functions as well as the space of integrable [step functions](https://en.wikipedia.org/wiki/Step_function "Step function") are dense in ${\displaystyle L^{p}(\mathbb {R} ^{d})}$.

### Closed subspaces

If ${\displaystyle 0<p<\infty }$ is any positive real number, ${\displaystyle \mu }$ is a [probability measure](https://en.wikipedia.org/wiki/Probability_measure "Probability measure") on a measurable space ${\displaystyle (S,\Sigma )}$ (so that ${\displaystyle L^{\infty }(\mu )\subseteq L^{p}(\mu )}$), and ${\displaystyle V\subseteq L^{\infty }(\mu )}$ is a vector subspace, then ${\displaystyle V}$ is a closed subspace of ${\displaystyle L^{p}(\mu )}$ if and only if ${\displaystyle V}$ is finite-dimensional [^13] (${\displaystyle V}$ was chosen independent of ${\displaystyle p}$). In this theorem, which is due to [Alexander Grothendieck](https://en.wikipedia.org/wiki/Alexander_Grothendieck "Alexander Grothendieck"),[^13] it is crucial that the vector space ${\displaystyle V}$ be a subset of ${\displaystyle L^{\infty }}$ since it is possible to construct an infinite-dimensional closed vector subspace of ${\displaystyle L^{1}\left(S^{1},{\tfrac {1}{2\pi }}\lambda \right)}$ (which is even a subset of ${\displaystyle L^{4}}$), where ${\displaystyle \lambda }$ is [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure "Lebesgue measure") on the [unit circle](https://en.wikipedia.org/wiki/Unit_circle "Unit circle") ${\displaystyle S^{1}}$ and ${\displaystyle {\tfrac {1}{2\pi }}\lambda }$ is the probability measure that results from dividing it by its mass ${\displaystyle \lambda (S^{1})=2\pi .}$ [^13]

## Applications

### Statistics

In statistics, measures of [central tendency](https://en.wikipedia.org/wiki/Central_tendency "Central tendency") and [statistical dispersion](https://en.wikipedia.org/wiki/Statistical_dispersion "Statistical dispersion"), such as the [mean](https://en.wikipedia.org/wiki/Mean "Mean"), [median](https://en.wikipedia.org/wiki/Median "Median"), and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation "Standard deviation"), can be defined in terms of ${\displaystyle L^{p}}$ metrics, and measures of central tendency can be characterized as [solutions to variational problems](https://en.wikipedia.org/wiki/Central_tendency#Solutions_to_variational_problems "Central tendency").

In [penalized regression](https://en.wikipedia.org/wiki/Penalized_regression "Penalized regression"), "L1 penalty" and "L2 penalty" refer to penalizing either the [${\displaystyle L^{1}}$ norm](https://en.wikipedia.org/wiki/Taxicab_geometry "Taxicab geometry") of a solution's vector of parameter values (i.e. the sum of its absolute values), or its squared ${\displaystyle L^{2}}$ norm (its [Euclidean length](https://en.wikipedia.org/wiki/Euclidean_norm "Euclidean norm")). Techniques which use an L1 penalty, like [LASSO](https://en.wikipedia.org/wiki/LASSO "LASSO"), encourage sparse solutions (where the many parameters are zero).[^14] [Elastic net regularization](https://en.wikipedia.org/wiki/Elastic_net_regularization "Elastic net regularization") uses a penalty term that is a combination of the ${\displaystyle L^{1}}$ norm and the squared ${\displaystyle L^{2}}$ norm of the parameter vector.

### Hausdorff–Young inequality

The [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform "Fourier transform") for the real line (or, for [periodic functions](https://en.wikipedia.org/wiki/Periodic_functions "Periodic functions"), see [Fourier series](https://en.wikipedia.org/wiki/Fourier_series "Fourier series")), maps ${\displaystyle L^{p}(\mathbb {R} )}$ to ${\displaystyle L^{q}(\mathbb {R} )}$ (or ${\displaystyle L^{p}(\mathbf {T} )}$ to ${\displaystyle \ell ^{q}}$) respectively, where ${\displaystyle 1\leq p\leq 2}$ and ${\displaystyle {\tfrac {1}{p}}+{\tfrac {1}{q}}=1.}$ This is a consequence of the [Riesz–Thorin interpolation theorem](https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem#Hausdorff%E2%80%93Young_inequality "Riesz–Thorin theorem"), and is made precise with the [Hausdorff–Young inequality](https://en.wikipedia.org/wiki/Hausdorff%E2%80%93Young_inequality "Hausdorff–Young inequality").

By contrast, if ${\displaystyle p>2,}$ the Fourier transform does not map into ${\displaystyle L^{q}.}$

### Hilbert spaces

[Hilbert spaces](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space") are central to many applications, from [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics "Quantum mechanics") to [stochastic calculus](https://en.wikipedia.org/wiki/Stochastic_calculus "Stochastic calculus"). The spaces ${\displaystyle L^{2}}$ and ${\displaystyle \ell ^{2}}$ are both Hilbert spaces. In fact, by choosing a Hilbert basis ${\displaystyle E,}$ i.e., a maximal orthonormal subset of ${\displaystyle L^{2}}$ or any Hilbert space, one sees that every Hilbert space is isometrically isomorphic to ${\displaystyle \ell ^{2}(E)}$ (same ${\displaystyle E}$ as above), i.e., a Hilbert space of type ${\displaystyle \ell ^{2}.}$

## Generalizations and extensions

### Weak Lp

Let ${\displaystyle (S,\Sigma ,\mu )}$ be a measure space, and ${\displaystyle f}$ a [measurable function](https://en.wikipedia.org/wiki/Measurable_function "Measurable function") with real or complex values on ${\displaystyle S.}$ The [distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function "Cumulative distribution function") of ${\displaystyle f}$ is defined for ${\displaystyle t\geq 0}$ by 
$$
{\displaystyle \lambda _{f}(t)=\mu \{x\in S:|f(x)|>t\}.}
$$

If ${\displaystyle f}$ is in ${\displaystyle L^{p}(S,\mu )}$ for some ${\displaystyle p}$ with ${\displaystyle 1\leq p<\infty ,}$ then by [Markov's inequality](https://en.wikipedia.org/wiki/Markov%27s_inequality "Markov's inequality"), 
$$
{\displaystyle \lambda _{f}(t)\leq {\frac {\|f\|_{p}^{p}}{t^{p}}}}
$$

A function ${\displaystyle f}$ is said to be in the space **weak ${\displaystyle L^{p}(S,\mu )}$**, or ${\displaystyle L^{p,w}(S,\mu ),}$ if there is a constant ${\displaystyle C>0}$ such that, for all ${\displaystyle t>0,}$ 
$$
{\displaystyle \lambda _{f}(t)\leq {\frac {C^{p}}{t^{p}}}}
$$

The best constant ${\displaystyle C}$ for this inequality is the ${\displaystyle L^{p,w}}$ -norm of ${\displaystyle f,}$ and is denoted by 
$$
{\displaystyle \|f\|_{p,w}=\sup _{t>0}~t\lambda _{f}^{1/p}(t).}
$$

The weak ${\displaystyle L^{p}}$ coincide with the [Lorentz spaces](https://en.wikipedia.org/wiki/Lorentz_space "Lorentz space") ${\displaystyle L^{p,\infty },}$ so this notation is also used to denote them.

The ${\displaystyle L^{p,w}}$ -norm is not a true norm, since the [triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality "Triangle inequality") fails to hold. Nevertheless, for ${\displaystyle f}$ in ${\displaystyle L^{p}(S,\mu ),}$ 
$$
{\displaystyle \|f\|_{p,w}\leq \|f\|_{p}}
$$
 and in particular ${\displaystyle L^{p}(S,\mu )\subset L^{p,w}(S,\mu ).}$

In fact, one has 
$$
{\displaystyle \|f\|_{L^{p}}^{p}=\int |f(x)|^{p}d\mu (x)\geq \int _{\{|f(x)|>t\}}t^{p}+\int _{\{|f(x)|\leq t\}}|f|^{p}\geq t^{p}\mu (\{|f|>t\}),}
$$
 and raising to power ${\displaystyle 1/p}$ and taking the supremum in ${\displaystyle t}$ one has 
$$
{\displaystyle \|f\|_{L^{p}}\geq \sup _{t>0}t\;\mu (\{|f|>t\})^{1/p}=\|f\|_{L^{p,w}}.}
$$

Under the convention that two functions are equal if they are equal ${\displaystyle \mu }$ almost everywhere, then the spaces ${\displaystyle L^{p,w}}$ are complete ([Grafakos 2004](#CITEREFGrafakos2004)).

For any ${\displaystyle 0<r<p}$ the expression 
$$
{\displaystyle \||f|\|_{L^{p,\infty }}=\sup _{0<\mu (E)<\infty }\mu (E)^{-1/r+1/p}\left(\int _{E}|f|^{r}\,d\mu \right)^{1/r}}
$$
 is comparable to the ${\displaystyle L^{p,w}}$ -norm. Further in the case ${\displaystyle p>1,}$ this expression defines a norm if ${\displaystyle r=1.}$ Hence for ${\displaystyle p>1}$ the weak ${\displaystyle L^{p}}$ spaces are [Banach spaces](https://en.wikipedia.org/wiki/Banach_space "Banach space") ([Grafakos 2004](#CITEREFGrafakos2004)).

A major result that uses the ${\displaystyle L^{p,w}}$ -spaces is the [Marcinkiewicz interpolation theorem](https://en.wikipedia.org/wiki/Marcinkiewicz_interpolation "Marcinkiewicz interpolation"), which has broad applications to [harmonic analysis](https://en.wikipedia.org/wiki/Harmonic_analysis "Harmonic analysis") and the study of [singular integrals](https://en.wikipedia.org/wiki/Singular_integrals "Singular integrals").

### Weighted Lp spaces

As before, consider a [measure space](https://en.wikipedia.org/wiki/Measure_space "Measure space") ${\displaystyle (S,\Sigma ,\mu ).}$ Let ${\displaystyle w:S\to [a,\infty ),a>0}$ be a measurable function. The ${\displaystyle w}$ - **weighted ${\displaystyle L^{p}}$ space** is defined as ${\displaystyle L^{p}(S,w\,\mathrm {d} \mu ),}$ where ${\displaystyle w\,\mathrm {d} \mu }$ means the measure ${\displaystyle \nu }$ defined by 
$$
{\displaystyle \nu (A)\equiv \int _{A}w(x)\,\mathrm {d} \mu (x),\qquad A\in \Sigma ,}
$$

or, in terms of the [Radon–Nikodym derivative](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_theorem "Radon–Nikodym theorem"), ${\displaystyle w={\tfrac {\mathrm {d} \nu }{\mathrm {d} \mu }}}$ the [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") for ${\displaystyle L^{p}(S,w\,\mathrm {d} \mu )}$ is explicitly 
$$
{\displaystyle \|u\|_{L^{p}(S,w\,\mathrm {d} \mu )}\equiv \left(\int _{S}w(x)|u(x)|^{p}\,\mathrm {d} \mu (x)\right)^{1/p}}
$$

As ${\displaystyle L^{p}}$ -spaces, the weighted spaces have nothing special, since ${\displaystyle L^{p}(S,w\,\mathrm {d} \mu )}$ is equal to ${\displaystyle L^{p}(S,\mathrm {d} \nu ).}$ But they are the natural framework for several results in harmonic analysis ([Grafakos 2004](#CITEREFGrafakos2004)); they appear for example in the [Muckenhoupt theorem](https://en.wikipedia.org/wiki/Muckenhoupt_weights "Muckenhoupt weights"): for ${\displaystyle 1<p<\infty ,}$ the classical [Hilbert transform](https://en.wikipedia.org/wiki/Hilbert_transform "Hilbert transform") is defined on ${\displaystyle L^{p}(\mathbf {T} ,\lambda )}$ where ${\displaystyle \mathbf {T} }$ denotes the [unit circle](https://en.wikipedia.org/wiki/Unit_circle "Unit circle") and ${\displaystyle \lambda }$ the Lebesgue measure; the (nonlinear) [Hardy–Littlewood maximal operator](https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_operator "Hardy–Littlewood maximal operator") is bounded on ${\displaystyle L^{p}(\mathbb {R} ^{n},\lambda ).}$ Muckenhoupt's theorem describes weights ${\displaystyle w}$ such that the Hilbert transform remains bounded on ${\displaystyle L^{p}(\mathbf {T} ,w\,\mathrm {d} \lambda )}$ and the maximal operator on ${\displaystyle L^{p}(\mathbb {R} ^{n},w\,\mathrm {d} \lambda ).}$

### Lp spaces on manifolds

One may also define spaces ${\displaystyle L^{p}(M)}$ on a manifold, called the **intrinsic ${\displaystyle L^{p}}$ spaces** of the manifold, using [densities](https://en.wikipedia.org/wiki/Density_on_a_manifold "Density on a manifold").

### Vector-valued Lp spaces

Given a measure space ${\displaystyle (\Omega ,\Sigma ,\mu )}$ and a [locally convex space](https://en.wikipedia.org/wiki/Locally_convex_topological_vector_space "Locally convex topological vector space") ${\displaystyle E}$ (here assumed to be [complete](https://en.wikipedia.org/wiki/Complete_topological_vector_space "Complete topological vector space")), it is possible to define spaces of ${\displaystyle p}$ -integrable ${\displaystyle E}$ -valued functions on ${\displaystyle \Omega }$ in a number of ways. One way is to define the spaces of [Bochner integrable](https://en.wikipedia.org/wiki/Bochner_integral "Bochner integral") and [Pettis integrable](https://en.wikipedia.org/wiki/Pettis_integral "Pettis integral") functions, and then endow them with [locally convex](https://en.wikipedia.org/wiki/Locally_convex_topological_vector_space "Locally convex topological vector space") [TVS-topologies](https://en.wikipedia.org/wiki/Vector_topology "Vector topology") that are (each in their own way) a natural generalization of the usual ${\displaystyle L^{p}}$ topology. Another way involves [topological tensor products](https://en.wikipedia.org/wiki/Topological_tensor_product "Topological tensor product") of ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu )}$ with ${\displaystyle E.}$ Element of the vector space ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu )\otimes E}$ are finite sums of simple tensors ${\displaystyle f_{1}\otimes e_{1}+\cdots +f_{n}\otimes e_{n},}$ where each simple tensor ${\displaystyle f\times e}$ may be identified with the function ${\displaystyle \Omega \to E}$ that sends ${\displaystyle x\mapsto ef(x).}$ This [tensor product](https://en.wikipedia.org/wiki/Tensor_product "Tensor product") ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu )\otimes E}$ is then endowed with a locally convex topology that turns it into a [topological tensor product](https://en.wikipedia.org/wiki/Topological_tensor_product "Topological tensor product"), the most common of which are the [projective tensor product](https://en.wikipedia.org/wiki/Projective_tensor_product "Projective tensor product"), denoted by ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu )\otimes _{\pi }E,}$ and the [injective tensor product](https://en.wikipedia.org/wiki/Injective_tensor_product "Injective tensor product"), denoted by ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu )\otimes _{\varepsilon }E.}$ In general, neither of these space are complete so their [completions](https://en.wikipedia.org/wiki/Complete_topological_vector_space "Complete topological vector space") are constructed, which are respectively denoted by ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu ){\widehat {\otimes }}_{\pi }E}$ and ${\displaystyle L^{p}(\Omega ,\Sigma ,\mu ){\widehat {\otimes }}_{\varepsilon }E}$ (this is analogous to how the space of scalar-valued [simple functions](https://en.wikipedia.org/wiki/Simple_function "Simple function") on ${\displaystyle \Omega ,}$ when seminormed by any ${\displaystyle \|\cdot \|_{p},}$ is not complete so a completion is constructed which, after being quotiented by ${\displaystyle \ker \|\cdot \|_{p},}$ is isometrically isomorphic to the Banach space ${\displaystyle L^{p}(\Omega ,\mu )}$). [Alexander Grothendieck](https://en.wikipedia.org/wiki/Alexander_Grothendieck "Alexander Grothendieck") showed that when ${\displaystyle E}$ is a [nuclear space](https://en.wikipedia.org/wiki/Nuclear_space "Nuclear space") (a concept he introduced), then these two constructions are, respectively, canonically TVS-isomorphic with the spaces of Bochner and Pettis integral functions mentioned earlier; in short, they are indistinguishable.

### L0 space of measurable functions

The vector space of ([equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class "Equivalence class") of) measurable functions on ${\displaystyle (S,\Sigma ,\mu )}$ is denoted ${\displaystyle L^{0}(S,\Sigma ,\mu )}$ ([Kalton, Peck & Roberts 1984](#CITEREFKaltonPeckRoberts1984)). By definition, it contains all the ${\displaystyle L^{p},}$ and is equipped with the topology of *[convergence in measure](https://en.wikipedia.org/wiki/Convergence_in_measure "Convergence in measure")*. When ${\displaystyle \mu }$ is a probability measure (i.e., ${\displaystyle \mu (S)=1}$), this mode of convergence is named *[convergence in probability](https://en.wikipedia.org/wiki/Convergence_in_probability "Convergence in probability")*. The space ${\displaystyle L^{0}}$ is always a [topological abelian group](https://en.wikipedia.org/wiki/Topological_abelian_group "Topological abelian group") but is only a [topological vector space](https://en.wikipedia.org/wiki/Topological_vector_space "Topological vector space") if ${\displaystyle \mu (S)<\infty .}$ This is because scalar multiplication is continuous if and only if ${\displaystyle \mu (S)<\infty .}$ If ${\displaystyle (S,\Sigma ,\mu )}$ is ${\displaystyle \sigma }$ -finite then the [weaker topology](https://en.wikipedia.org/wiki/Weaker_topology "Weaker topology") of [local convergence in measure](https://en.wikipedia.org/wiki/Local_convergence_in_measure "Local convergence in measure") is an [F-space](https://en.wikipedia.org/wiki/F-space "F-space"), i.e. a [completely](https://en.wikipedia.org/wiki/Complete_topological_vector_space "Complete topological vector space") [metrizable topological vector space](https://en.wikipedia.org/wiki/Metrizable_topological_vector_space "Metrizable topological vector space"). Moreover, this topology is isometric to global convergence in measure ${\displaystyle (S,\Sigma ,\nu )}$ for a suitable choice of [probability measure](https://en.wikipedia.org/wiki/Probability_measure "Probability measure") ${\displaystyle \nu .}$

The description is easier when ${\displaystyle \mu }$ is finite. If ${\displaystyle \mu }$ is a [finite measure](https://en.wikipedia.org/wiki/Finite_measure "Finite measure") on ${\displaystyle (S,\Sigma ),}$ the ${\displaystyle 0}$ function admits for the convergence in measure the following [fundamental system of neighborhoods](https://en.wikipedia.org/wiki/Fundamental_system_of_neighborhoods "Fundamental system of neighborhoods") 
$$
{\displaystyle V_{\varepsilon }={\Bigl \{}f:\mu {\bigl (}\{x:|f(x)|>\varepsilon \}{\bigr )}<\varepsilon {\Bigr \}},\qquad \varepsilon >0.}
$$

The topology can be defined by any metric ${\displaystyle d}$ of the form 
$$
{\displaystyle d(f,g)=\int _{S}\varphi {\bigl (}|f(x)-g(x)|{\bigr )}\,\mathrm {d} \mu (x)}
$$
 where ${\displaystyle \varphi }$ is bounded continuous concave and non-decreasing on ${\displaystyle [0,\infty ),}$ with ${\displaystyle \varphi (0)=0}$ and ${\displaystyle \varphi (t)>0}$ when ${\displaystyle t>0}$ (for example, ${\displaystyle \varphi (t)=\min(t,1).}$ Such a metric is called [Lévy](https://en.wikipedia.org/wiki/Paul_L%C3%A9vy_\(mathematician\) "Paul Lévy (mathematician)") -metric for ${\displaystyle L^{0}.}$ Under this metric the space ${\displaystyle L^{0}}$ is complete. However, as mentioned above, scalar multiplication is continuous with respect to this metric only if ${\displaystyle \mu (S)<\infty }$. To see this, consider the Lebesgue measurable function ${\displaystyle f:\mathbb {R} \rightarrow \mathbb {R} }$ defined by ${\displaystyle f(x)=x}$. Then clearly ${\displaystyle \lim _{c\rightarrow 0}d(cf,0)=\infty }$. The space ${\displaystyle L^{0}}$ is in general not locally bounded, and not locally convex.

For the infinite Lebesgue measure ${\displaystyle \lambda }$ on ${\displaystyle \mathbb {R} ^{n},}$ the definition of the fundamental system of neighborhoods could be modified as follows 
$$
{\displaystyle W_{\varepsilon }=\left\{f:\lambda \left(\left\{x:|f(x)|>\varepsilon {\text{ and }}|x|<{\tfrac {1}{\varepsilon }}\right\}\right)<\varepsilon \right\}}
$$

The resulting space ${\displaystyle L^{0}(\mathbb {R} ^{n},\lambda )}$, with the topology of local convergence in measure, is isomorphic to the space ${\displaystyle L^{0}(\mathbb {R} ^{n},g\,\lambda ),}$ for any positive ${\displaystyle \lambda }$ –integrable density ${\displaystyle g.}$

[^1]: Maddox, I. J. (1988), *Elements of Functional Analysis* (2nd ed.), Cambridge: CUP, page 16

[^2]: Rafael Dahmen, Gábor Lukács: *Long colimits of topological groups I: Continuous maps and homeomorphisms.* in: *Topology and its Applications* Nr. 270, 2020. Example 2.14

[^3]: Garling, D. J. H. (2007). *Inequalities: A Journey into Linear Analysis*. Cambridge University Press. p. 54. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-87624-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-87624-7 "Special:BookSources/978-0-521-87624-7").

[^4]: [Rudin 1987](#CITEREFRudin1987), p. 65.

[^5]: [Stein & Shakarchi 2012](#CITEREFSteinShakarchi2012), p. 2.

[^6]: [Rudin 1991](#CITEREFRudin1991), p. 37.

[^7]: [Bahouri, Chemin & Danchin 2011](#CITEREFBahouriCheminDanchin2011), pp. 1–4.

[^8]: [Bahouri, Chemin & Danchin 2011](#CITEREFBahouriCheminDanchin2011), p. 4.

[^9]: [Bahouri, Chemin & Danchin 2011](#CITEREFBahouriCheminDanchin2011), pp. 7–8.

[^10]: [Rudin 1987](#CITEREFRudin1987), Theorem 6.16.

[^11]: Schechter, Eric (1997), *Handbook of Analysis and its Foundations*, London: Academic Press Inc. See Sections 14.77 and 27.44–47

[^12]: Villani, Alfonso (1985), "Another note on the inclusion *L <sup>p</sup>* (*μ*) ⊂ *L <sup>q</sup>* (*μ*)", *Amer. Math. Monthly*, **92** (7): 485–487, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2322503](https://doi.org/10.2307%2F2322503), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2322503](https://www.jstor.org/stable/2322503), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0801221](https://mathscinet.ams.org/mathscinet-getitem?mr=0801221)

[^13]: [Rudin 1991](#CITEREFRudin1991), pp. 117–119.

[^14]: [Hastie, T. J.](https://en.wikipedia.org/wiki/Trevor_Hastie "Trevor Hastie"); [Tibshirani, R.](https://en.wikipedia.org/wiki/Robert_Tibshirani "Robert Tibshirani"); Wainwright, M. J. (2015). *Statistical Learning with Sparsity: The Lasso and Generalizations*. CRC Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4987-1216-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4987-1216-3 "Special:BookSources/978-1-4987-1216-3").

[^15]: The condition ${\displaystyle \sup \operatorname {range} |x|<+\infty .}$ is not equivalent to ${\displaystyle \sup \operatorname {range} |x|}$ being finite, unless ${\displaystyle X\neq \varnothing .}$

[^16]: If ${\displaystyle X=\varnothing }$ then ${\displaystyle \sup \operatorname {range} |x|=-\infty .}$

[^17]: The definitions of ${\displaystyle \|\cdot \|_{p},}$ ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu ),}$ and ${\displaystyle L^{p}(S,\,\mu )}$ can be extended to all ${\displaystyle 0<p\leq \infty }$ (rather than just ${\displaystyle 1\leq p\leq \infty }$), but it is only when ${\displaystyle 1\leq p\leq \infty }$ that ${\displaystyle \|\cdot \|_{p}}$ is guaranteed to be a norm (although ${\displaystyle \|\cdot \|_{p}}$ is a [quasi-seminorm](https://en.wikipedia.org/wiki/Quasi-seminorm "Quasi-seminorm") for all ${\displaystyle 0<p\leq \infty ,}$).

[^18]: If ${\displaystyle \mu (S)=0}$ then ${\displaystyle \operatorname {esssup} |f|=-\infty .}$

[^19]: For example, if a non-empty measurable set ${\displaystyle N\neq \varnothing }$ of measure ${\displaystyle \mu (N)=0}$ exists then its [indicator function](https://en.wikipedia.org/wiki/Indicator_function "Indicator function") ${\displaystyle \mathbf {1} _{N}}$ satisfies ${\displaystyle \|\mathbf {1} _{N}\|_{p}=0}$ although ${\displaystyle \mathbf {1} _{N}\neq 0.}$

[^20]: Explicitly, the vector space operations are defined by: 
$$
{\displaystyle {\begin{aligned}(f+g)(x)&=f(x)+g(x),\\(sf)(x)&=sf(x)\end{aligned}}}
$$
 for all ${\displaystyle f,g\in {\mathcal {L}}^{p}(S,\,\mu )}$ and all scalars ${\displaystyle s.}$ These operations make ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu )}$ into a vector space because if ${\displaystyle s}$ is any scalar and ${\displaystyle f,g\in {\mathcal {L}}^{p}(S,\,\mu )}$ then both ${\displaystyle sf}$ and ${\displaystyle f+g}$ also belong to ${\displaystyle {\mathcal {L}}^{p}(S,\,\mu ).}$

[^21]: This [infimum](https://en.wikipedia.org/wiki/Infimum "Infimum") is attained by ${\displaystyle t_{n};}$ that is, ${\displaystyle \mu (f>t_{n})<2^{n}}$ holds.

[^22]: When ${\displaystyle 1\leq p<\infty ,}$ the inequality ${\displaystyle \|f+g\|_{p}^{p}\leq 2^{p-1}\left(\|f\|_{p}^{p}+\|g\|_{p}^{p}\right)}$ can be deduced from the fact that the function ${\displaystyle F:[0,\infty )\to \mathbb {R} }$ defined by ${\displaystyle F(t)=t^{p}}$ is [convex](https://en.wikipedia.org/wiki/Convex_function "Convex function"), which by definition means that ${\displaystyle F(tx+(1-t)y)\leq tF(x)+(1-t)F(y)}$ for all ${\displaystyle 0\leq t\leq 1}$ and all ${\displaystyle x,y}$ in the domain of ${\displaystyle F.}$ Substituting ${\displaystyle |f|,|g|,}$ and ${\displaystyle {\tfrac {1}{2}}}$ in for ${\displaystyle x,y,}$ and ${\displaystyle t}$ gives ${\displaystyle \left({\tfrac {1}{2}}|f|+{\tfrac {1}{2}}|g|\right)^{p}\leq {\tfrac {1}{2}}|f|^{p}+{\tfrac {1}{2}}|g|^{p},}$ which proves that ${\displaystyle (|f|+|g|)^{p}\leq 2^{p-1}(|f|^{p}+|g|^{p}).}$ The triangle inequality ${\displaystyle |f+g|\leq |f|+|g|}$ now implies ${\displaystyle |f+g|^{p}\leq 2^{p-1}(|f|^{p}+|g|^{p}).}$ The desired inequality follows by integrating both sides. ${\displaystyle \blacksquare }$