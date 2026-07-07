---
title: "Operator norm"
source: "https://en.wikipedia.org/wiki/Operator_norm"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2003-06-15
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **operator norm** measures the "size" of certain [linear operators](https://en.wikipedia.org/wiki/Linear_operator "Linear operator") by assigning each a [real number](https://en.wikipedia.org/wiki/Real_number "Real number") called its *operator norm*. Formally, it is a [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") defined on the space of [bounded linear operators](https://en.wikipedia.org/wiki/Bounded_linear_operator "Bounded linear operator") between two given [normed vector spaces](https://en.wikipedia.org/wiki/Normed_vector_space "Normed vector space"). Informally, the operator norm ${\displaystyle \|T\|}$ of a linear map ${\displaystyle T:X\to Y}$ is the maximum factor by which it "lengthens" vectors. It is also called the **bound norm**.[^1]

## Introduction and definition

Given two normed vector spaces ${\displaystyle V}$ and ${\displaystyle W}$ (over the same base [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)"), either the [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") ${\displaystyle \mathbb {R} }$ or the [complex numbers](https://en.wikipedia.org/wiki/Complex_number "Complex number") ${\displaystyle \mathbb {C} }$), a [linear map](https://en.wikipedia.org/wiki/Linear_map "Linear map") ${\displaystyle A:V\to W}$ is continuous [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") there exists a real number ${\displaystyle c}$ such that [^2] 
$$
{\displaystyle \|Av\|\leq c\|v\|\quad {\text{ for all }}v\in V.}
$$

The norm on the left is the one in ${\displaystyle W}$ and the norm on the right is the one in ${\displaystyle V}$. Intuitively, the continuous operator ${\displaystyle A}$ never increases the length of any vector by more than a factor of ${\displaystyle c.}$ Thus the [image](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)") of a bounded set under a continuous operator is also bounded. Because of this property, the continuous linear operators are also known as [bounded operators](https://en.wikipedia.org/wiki/Bounded_operator "Bounded operator"). In order to "measure the size" of ${\displaystyle A,}$ one can take the [infimum](https://en.wikipedia.org/wiki/Infimum "Infimum") of the numbers ${\displaystyle c}$ such that the above inequality holds for all ${\displaystyle v\in V.}$ This number represents the maximum scalar factor by which ${\displaystyle A}$ "lengthens" vectors. In other words, the "size" of ${\displaystyle A}$ is measured by how much it "lengthens" vectors in the "biggest" case. So we define the operator norm of ${\displaystyle A}$ as 
$$
{\displaystyle \|A\|_{\text{op}}=\inf\{c\geq 0:\|Av\|\leq c\|v\|{\text{ for all }}v\in V\}.}
$$

The infimum is attained as the set of all such ${\displaystyle c}$ is [closed](https://en.wikipedia.org/wiki/Closed_set "Closed set"), [nonempty](https://en.wikipedia.org/wiki/Empty_set "Empty set"), and [bounded](https://en.wikipedia.org/wiki/Bounded_set "Bounded set") from below.[^3]

It is important to bear in mind that this operator norm depends on the choice of norms for the normed vector spaces ${\displaystyle V}$ and ${\displaystyle W}$.

## Examples

Every real ${\displaystyle m}$ -by- ${\displaystyle n}$ [matrix](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)") corresponds to a linear map from ${\displaystyle \mathbb {R} ^{n}}$ to ${\displaystyle \mathbb {R} ^{m}.}$ Each pair of the plethora of (vector) [norms](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)") applicable to real vector spaces induces an operator norm for all ${\displaystyle m}$ -by- ${\displaystyle n}$ matrices of real numbers; these induced norms form a subset of [matrix norms](https://en.wikipedia.org/wiki/Matrix_norm "Matrix norm").

If we specifically choose the [Euclidean norm](https://en.wikipedia.org/wiki/Euclidean_norm "Euclidean norm") on both ${\displaystyle \mathbb {R} ^{n}}$ and ${\displaystyle \mathbb {R} ^{m},}$ then the matrix norm given to a matrix ${\displaystyle A}$ is the [square root](https://en.wikipedia.org/wiki/Square_root "Square root") of the largest [eigenvalue](https://en.wikipedia.org/wiki/Eigenvalue "Eigenvalue") of the matrix ${\displaystyle A^{*}A}$ (where ${\displaystyle A^{*}}$ denotes the [conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") of ${\displaystyle A}$).[^4] This is equivalent to assigning the largest [singular value](https://en.wikipedia.org/wiki/Singular_value "Singular value") of ${\displaystyle A.}$

Passing to a typical infinite-dimensional example, consider the [sequence space](https://en.wikipedia.org/wiki/Sequence_space "Sequence space") ${\displaystyle \ell ^{2},}$ which is an [L <sup><i>p</i></sup> space](https://en.wikipedia.org/wiki/Lp_space "Lp space"), defined by 
$$
{\displaystyle \ell ^{2}=\left\{(a_{n})_{n\geq 1}:\;a_{n}\in \mathbb {C} ,\;\sum _{n}|a_{n}|^{2}<\infty \right\}.}
$$

This can be viewed as an infinite-dimensional analogue of the [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space") ${\displaystyle \mathbb {C} ^{n}.}$ Now consider a bounded sequence ${\displaystyle s_{\bullet }=\left(s_{n}\right)_{n=1}^{\infty }.}$ The sequence ${\displaystyle s_{\bullet }}$ is an element of the space ${\displaystyle \ell ^{\infty },}$ with a norm given by 
$$
{\displaystyle \left\|s_{\bullet }\right\|_{\infty }=\sup _{n}\left|s_{n}\right|.}
$$

Define an operator ${\displaystyle T_{s}}$ by pointwise multiplication: 
$$
{\displaystyle \left(a_{n}\right)_{n=1}^{\infty }\;{\stackrel {T_{s}}{\mapsto }}\;\ \left(s_{n}\cdot a_{n}\right)_{n=1}^{\infty }.}
$$

The operator ${\displaystyle T_{s}}$ is bounded with operator norm 
$$
{\displaystyle \left\|T_{s}\right\|_{\text{op}}=\left\|s_{\bullet }\right\|_{\infty }.}
$$

This discussion extends directly to the case where ${\displaystyle \ell ^{2}}$ is replaced by a general ${\displaystyle L^{p}}$ space with ${\displaystyle p>1}$ and ${\displaystyle \ell ^{\infty }}$ replaced by ${\displaystyle L^{\infty }.}$

## Equivalent definitions

Let ${\displaystyle A:V\to W}$ be a linear operator between normed spaces. The first four definitions are always equivalent, and if in addition ${\displaystyle V\neq \{0\}}$ then they are all equivalent:

${\displaystyle {\begin{alignedat}{4}\|A\|_{\text{op}}&=\inf &&\{c\geq 0~&&:~\|Av\|\leq c\|v\|~&&~{\text{ for all }}~&&v\in V\}\\&=\sup &&\{\|Av\|~&&:~\|v\|\leq 1~&&~{\mbox{ and }}~&&v\in V\}\\&=\sup &&\{\|Av\|~&&:~\|v\|<1~&&~{\mbox{ and }}~&&v\in V\}\\&=\sup &&\{\|Av\|~&&:~\|v\|\in \{0,1\}~&&~{\mbox{ and }}~&&v\in V\}\\&=\sup &&\{\|Av\|~&&:~\|v\|=1~&&~{\mbox{ and }}~&&v\in V\}\;\;\;{\text{ this equality holds if and only if }}V\neq \{0\}\\&=\sup &&{\bigg \{}{\frac {\|Av\|}{\|v\|}}~&&:~v\neq 0~&&~{\mbox{ and }}~&&v\in V{\bigg \}}\;\;\;{\text{ this equality holds if and only if }}V\neq \{0\}.\\\end{alignedat}}}$

If ${\displaystyle V=\{0\}}$ then the sets in the last two rows will be empty, and consequently their [supremums](https://en.wikipedia.org/wiki/Supremum "Supremum") over the set ${\displaystyle [-\infty ,\infty ]}$ will equal ${\displaystyle -\infty }$ instead of the correct value of ${\displaystyle 0.}$ If the supremum is taken over the set ${\displaystyle [0,\infty ]}$ instead, then the supremum of the empty set is ${\displaystyle 0}$ and the formulas hold for any ${\displaystyle V.}$

Importantly, a linear operator ${\displaystyle A:V\to W}$ is not, in general, guaranteed to achieve its norm ${\displaystyle \|A\|_{\text{op}}=\sup\{\|Av\|:\|v\|\leq 1,v\in V\}}$ on the closed unit ball ${\displaystyle \{v\in V:\|v\|\leq 1\},}$ meaning that there might not exist any vector ${\displaystyle u\in V}$ of norm ${\displaystyle \|u\|\leq 1}$ such that ${\displaystyle \|A\|_{\text{op}}=\|Au\|}$ (if such a vector does exist and if ${\displaystyle A\neq 0,}$ then ${\displaystyle u}$ would necessarily have unit norm ${\displaystyle \|u\|=1}$). R.C. James proved [James's theorem](https://en.wikipedia.org/wiki/James%27s_theorem "James's theorem") in 1964, which states that a [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space") ${\displaystyle V}$ is [reflexive](https://en.wikipedia.org/wiki/Reflexive_space "Reflexive space") if and only if every [bounded linear functional](https://en.wikipedia.org/wiki/Bounded_linear_functional "Bounded linear functional") ${\displaystyle f\in V^{*}}$ achieves its [norm](https://en.wikipedia.org/wiki/Dual_norm "Dual norm") on the closed unit ball.[^5] It follows, in particular, that every non-reflexive Banach space has some bounded linear functional (a type of bounded linear operator) that does not achieve its norm on the closed unit ball.

If ${\displaystyle A:V\to W}$ is bounded then [^6] 
$$
{\displaystyle \|A\|_{\text{op}}=\sup \left\{\left|w^{*}(Av)\right|:\|v\|\leq 1,\left\|w^{*}\right\|\leq 1{\text{ where }}v\in V,w^{*}\in W^{*}\right\}}
$$
 and [^6] 
$$
{\displaystyle \|A\|_{\text{op}}=\left\|{}^{t}A\right\|_{\text{op}}}
$$
 where ${\displaystyle {}^{t}A:W^{*}\to V^{*}}$ is the [transpose](https://en.wikipedia.org/wiki/Transpose_of_a_linear_map "Transpose of a linear map") of ${\displaystyle A:V\to W,}$ which is the linear operator defined by ${\displaystyle w^{*}\,\mapsto \,w^{*}\circ A.}$

## Properties

The operator norm is indeed a norm on the space of all [bounded operators](https://en.wikipedia.org/wiki/Bounded_operator "Bounded operator") between ${\displaystyle V}$ and ${\displaystyle W}$. This means 
$$
{\displaystyle \|A\|_{\text{op}}\geq 0{\mbox{ and }}\|A\|_{\text{op}}=0{\mbox{ if and only if }}A=0,}
$$
 
$$
{\displaystyle \|aA\|_{\text{op}}=|a|\|A\|_{\text{op}}{\mbox{ for every scalar }}a,}
$$
 
$$
{\displaystyle \|A+B\|_{\text{op}}\leq \|A\|_{\text{op}}+\|B\|_{\text{op}}.}
$$

The following inequality is an immediate consequence of the definition: 
$$
{\displaystyle \|Av\|\leq \|A\|_{\text{op}}\|v\|\ {\mbox{ for every }}\ v\in V.}
$$

The operator norm is also compatible with the composition, or multiplication, of operators: if ${\displaystyle V}$, ${\displaystyle W}$ and ${\displaystyle X}$ are three normed spaces over the same base field, and ${\displaystyle A:V\to W}$ and ${\displaystyle B:W\to X}$ are two bounded operators, then it is a [sub-multiplicative norm](https://en.wikipedia.org/wiki/Sub-multiplicative_norm "Sub-multiplicative norm"), that is: 
$$
{\displaystyle \|BA\|_{\text{op}}\leq \|B\|_{\text{op}}\|A\|_{\text{op}}.}
$$

For bounded operators on ${\displaystyle V}$, this implies that operator multiplication is jointly continuous.

It follows from the definition that if a sequence of operators converges in operator norm, it [converges uniformly](https://en.wikipedia.org/wiki/Converges_uniformly "Converges uniformly") on bounded sets.

## Table of common operator norms

By choosing different norms for the codomain, used in computing ${\displaystyle \|Av\|}$, and the domain, used in computing ${\displaystyle \|v\|}$, we obtain different values for the operator norm. Some common operator norms are easy to calculate, and others are [NP-hard](https://en.wikipedia.org/wiki/NP-hard "NP-hard"). Except for the NP-hard norms, all these norms can be calculated in ${\displaystyle N^{2}}$ operations (for an ${\displaystyle N\times N}$ matrix), with the exception of the ${\displaystyle \ell _{2}-\ell _{2}}$ norm (which requires ${\displaystyle N^{3}}$ operations for the exact answer, or fewer if you approximate it with the [power method](https://en.wikipedia.org/wiki/Power_iteration "Power iteration") or [Lanczos iterations](https://en.wikipedia.org/wiki/Lanczos_algorithm "Lanczos algorithm")).

<table><caption>Computability of Operator Norms <sup><a href="#fn:7">7</a></sup></caption><tbody><tr><th colspan="2" rowspan="2"></th><th colspan="3">Co-domain</th></tr><tr><th><math>{\displaystyle \ell _{1}}</math></th><th><math>{\displaystyle \ell _{2}}</math></th><th><math>{\displaystyle \ell _{\infty }}</math></th></tr><tr><th rowspan="3">Domain</th><th><math>{\displaystyle \ell _{1}}</math></th><td>Maximum <math>{\displaystyle \ell _{1}}</math> norm of a column</td><td>Maximum <math>{\displaystyle \ell _{2}}</math> norm of a column</td><td>Maximum <math>{\displaystyle \ell _{\infty }}</math> norm of a column</td></tr><tr><th><math>{\displaystyle \ell _{2}}</math></th><td>NP-hard</td><td>Maximum singular value</td><td>Maximum <math>{\displaystyle \ell _{2}}</math> norm of a row</td></tr><tr><th><math>{\displaystyle \ell _{\infty }}</math></th><td>NP-hard</td><td>NP-hard</td><td>Maximum <math>{\displaystyle \ell _{1}}</math> norm of a row</td></tr></tbody></table>

The norm of the [adjoint](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") or transpose can be computed as follows. We have that for any ${\displaystyle p,q,}$ then ${\displaystyle \|A\|_{p\rightarrow q}=\|A^{*}\|_{q'\rightarrow p'}}$ where ${\displaystyle p',q'}$ are [Hölder conjugate](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality "Hölder's inequality") to ${\displaystyle p,q,}$ that is, ${\displaystyle 1/p+1/p'=1}$ and ${\displaystyle 1/q+1/q'=1.}$

## Operators on a Hilbert space

Suppose ${\displaystyle H}$ is a real or complex [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"). If ${\displaystyle A:H\to H}$ is a bounded linear operator, then we have 
$$
{\displaystyle \|A\|_{\text{op}}=\left\|A^{*}\right\|_{\text{op}}}
$$
 and 
$$
{\displaystyle \left\|A^{*}A\right\|_{\text{op}}=\|A\|_{\text{op}}^{2},}
$$
 where ${\displaystyle A^{*}}$ denotes the [adjoint operator](https://en.wikipedia.org/wiki/Adjoint_operator "Adjoint operator") of ${\displaystyle A}$ (which in [Euclidean spaces](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space") with the standard [inner product](https://en.wikipedia.org/wiki/Inner_product "Inner product") corresponds to the [conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") of the matrix ${\displaystyle A}$).

In general, the [spectral radius](https://en.wikipedia.org/wiki/Spectral_radius "Spectral radius") of ${\displaystyle A}$ is bounded above by the operator norm of ${\displaystyle A}$: 
$$
{\displaystyle \rho (A)\leq \|A\|_{\text{op}}.}
$$

To see why equality may not always hold, consider the [Jordan canonical form](https://en.wikipedia.org/wiki/Jordan_canonical_form "Jordan canonical form") of a matrix in the finite-dimensional case. Because there are non-zero entries on the superdiagonal, equality may be violated. The [quasinilpotent operators](https://en.wikipedia.org/wiki/Quasinilpotent_operator "Quasinilpotent operator") is one class of such examples. A nonzero quasinilpotent operator ${\displaystyle A}$ has spectrum ${\displaystyle \{0\}.}$ So ${\displaystyle \rho (A)=0}$ while ${\displaystyle \|A\|_{\text{op}}>0.}$

However, when a matrix ${\displaystyle N}$ is [normal](https://en.wikipedia.org/wiki/Normal_matrix "Normal matrix"), its [Jordan canonical form](https://en.wikipedia.org/wiki/Jordan_canonical_form "Jordan canonical form") is diagonal (up to unitary equivalence); this is the [spectral theorem](https://en.wikipedia.org/wiki/Spectral_theorem "Spectral theorem"). In that case it is easy to see that 
$$
{\displaystyle \rho (N)=\|N\|_{\text{op}}.}
$$

This formula can sometimes be used to compute the operator norm of a given bounded operator ${\displaystyle A}$: define the [Hermitian operator](https://en.wikipedia.org/wiki/Hermitian_operator "Hermitian operator") ${\displaystyle B=A^{*}A,}$ determine its spectral radius, and take the [square root](https://en.wikipedia.org/wiki/Square_root_of_a_matrix "Square root of a matrix") to obtain the operator norm of ${\displaystyle A.}$

The space of bounded operators on ${\displaystyle H,}$ with the [topology](https://en.wikipedia.org/wiki/Topological_space "Topological space") induced by operator norm, is not [separable](https://en.wikipedia.org/wiki/Separable_space "Separable space"). For example, consider the [Lp space](https://en.wikipedia.org/wiki/Lp_space "Lp space") ${\displaystyle L^{2}[0,1],}$ which is a Hilbert space. For ${\displaystyle 0<t\leq 1,}$ let ${\displaystyle \Omega _{t}}$ be the [characteristic function](https://en.wikipedia.org/wiki/Indicator_function "Indicator function") of ${\displaystyle [0,t],}$ and ${\displaystyle P_{t}}$ be the [multiplication operator](https://en.wikipedia.org/wiki/Multiplication_operator "Multiplication operator") given by ${\displaystyle \Omega _{t},}$ that is, 
$$
{\displaystyle P_{t}(f)=f\cdot \Omega _{t}.}
$$

Then each ${\displaystyle P_{t}}$ is a bounded operator with operator norm 1 and 
$$
{\displaystyle \left\|P_{t}-P_{s}\right\|_{\text{op}}=1\quad {\mbox{ for all }}\quad t\neq s.}
$$

But ${\displaystyle \{P_{t}:0<t\leq 1\}}$ is an [uncountable set](https://en.wikipedia.org/wiki/Uncountable_set "Uncountable set"). This implies the space of bounded operators on ${\displaystyle L^{2}([0,1])}$ is not separable, in operator norm. One can compare this with the fact that the sequence space ${\displaystyle \ell ^{\infty }}$ is not separable.

[^1]: ([Bhatia 1997](#CITEREFBhatia1997), p. 7)

[^2]: Kreyszig, Erwin (1978), *Introductory functional analysis with applications*, John Wiley & Sons, p. 97, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9971-51-381-1](https://en.wikipedia.org/wiki/Special:BookSources/9971-51-381-1 "Special:BookSources/9971-51-381-1")

[^3]: See e.g. Lemma 6.2 of [Aliprantis & Border (2007)](#CITEREFAliprantisBorder2007).

[^4]: [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein") ["Operator Norm"](https://mathworld.wolfram.com/OperatorNorm.html). *mathworld.wolfram.com*. Retrieved 2020-03-14.

[^5]: [Diestel 1984](#CITEREFDiestel1984), p. 6.

[^6]: [Rudin 1991](#CITEREFRudin1991), pp. 92–115.

[^7]: section 4.3.1, [Joel Tropp](https://en.wikipedia.org/wiki/Joel_Tropp "Joel Tropp") 's PhD thesis, [\[1\]](http://users.cms.caltech.edu/~jtropp/papers/Tro04-Topics-Sparse.pdf)