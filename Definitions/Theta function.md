---
title: "Theta function"
source: "https://en.wikipedia.org/wiki/Theta_function"
author:
  - "[[Wikipedia]]"
published: 2004-01-31
created: 2026-06-23
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), **theta functions** are [special functions](https://en.wikipedia.org/wiki/Special_function "Special function") of [several complex variables](https://en.wikipedia.org/wiki/Several_complex_variables "Several complex variables"). Fundamentally, they are a family of *continuous* functions which encode the behavior of *discrete* multi-dimensional [periodic](https://en.wikipedia.org/wiki/Periodic_function "Periodic function") systems, such as [crystal lattices](https://en.wikipedia.org/wiki/Bravais_lattice "Bravais lattice") or points on a [torus](https://en.wikipedia.org/wiki/Torus "Torus"). Because they are smooth, they allow the study and manipulation of discrete combinatorial systems using the tools of [analysis](https://en.wikipedia.org/wiki/Complex_analysis "Complex analysis").

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Cplot_of_Jacobi_theta_1.svg/500px-Cplot_of_Jacobi_theta_1.svg.png)

Jacobi's theta function θ 1 with nome q = e i π τ = 0.1 0.1: {\\displaystyle {\\begin{aligned}\\theta \_{1}(z,q)&=2q^{\\frac {1}{4}}\\sum \_{n=0}^{\\infty }(-1)^{n}q^{n(n+1)}\\sin(2n+1)z\\\\&=\\sum \_{n=-\\infty }^{\\infty }(-1)^{n-{\\frac {1}{2}}}q^{\\left(n+{\\frac {1}{2}}\\right)^{2}}e^{(2n+1)iz}.\\end{aligned}}}

For this reason, theta functions have useful applications in topics such as

- [number theory](https://en.wikipedia.org/wiki/Number_theory "Number theory"): "in how many ways can a number be written as a sum of squares?"
- [physics](https://en.wikipedia.org/wiki/Physics "Physics"): "how does heat flow on a toroidal ring?", "how do quantum particles behave when arranged in a lattice?"
- [geometry](https://en.wikipedia.org/wiki/Geometry "Geometry"): "what are the shape properties of [elliptic curves](https://en.wikipedia.org/wiki/Elliptic_curve "Elliptic curve")?"

and others, including [abelian varieties](https://en.wikipedia.org/wiki/Abelian_variety "Abelian variety"), [moduli spaces](https://en.wikipedia.org/wiki/Moduli_space "Moduli space"), [quadratic forms](https://en.wikipedia.org/wiki/Quadratic_form "Quadratic form"), and [solitons](https://en.wikipedia.org/wiki/Soliton "Soliton").

Theta functions in two dimensions are functions of two complex arguments. In one choice of parameter, for example, ${\displaystyle z}$ encodes position on a two-dimensional lattice, and ${\displaystyle \tau }$ or ${\displaystyle q}$ encodes the shape of the lattice. In higher dimensions, the shape of the lattice is dictated by a matrix; in general, theta functions are parametrized by points in a [tube domain](https://en.wikipedia.org/wiki/Tube_domain "Tube domain") inside a complex [Lagrangian Grassmannian](https://en.wikipedia.org/wiki/Lagrangian_Grassmannian "Lagrangian Grassmannian"),[^3] namely the [Siegel upper half space](https://en.wikipedia.org/wiki/Siegel_upper_half_space "Siegel upper half space").

## Basic example

One example of a theta function is

${\displaystyle \theta (z,q)\equiv \sum _{n=-\infty }^{\infty }q^{n^{2}}\exp {(2\pi inz)}}$,

where ${\displaystyle z}$ and ${\displaystyle q}$ are complex numbers and ${\displaystyle |q|<1}$ so that the sum converges.

This [analytic function](https://en.wikipedia.org/wiki/Analytic_function "Analytic function") can be used to solve a combinatorics problem: in how many different ways can an integer be written as the sum of two squares? When ${\displaystyle z=0}$, we have

${\displaystyle \theta (0,q)=\sum _{n=-\infty }^{\infty }q^{n^{2}}=1+2q+2q^{4}+2q^{9}+\ldots +2q^{n^{2}}+\ldots }$

This is a [generating function](https://en.wikipedia.org/wiki/Generating_function "Generating function") where the coefficient of ${\displaystyle q^{k}}$ represents how many ways there are to write ${\displaystyle k}$ as a perfect square: when ${\displaystyle k=0}$, there is just one way. When ${\displaystyle k}$ is any other perfect square, there are two ways: ${\displaystyle n^{2}=(-n)^{2}}$. When ${\displaystyle k}$ is not a perfect square, there are zero ways.

Squaring this generating function, we obtain

${\displaystyle \theta (0,q)^{2}={\Bigl (}\sum _{m}q^{m^{2}}{\Bigr )}{\Bigl (}\sum _{n}q^{n^{2}}{\Bigr )}=\sum _{m,n}q^{m^{2}+n^{2}}}$.

Collecting terms by exponent, we find that ${\displaystyle \theta (0,q)^{2}}$ is a generating function where the coefficient of ${\displaystyle q^{k}}$ counts how many ways there are to write ${\displaystyle k}$ as the sum of any two squares. This count includes negative integers and order, such that ${\displaystyle (3,4)}$, ${\displaystyle (4,3)}$, and ${\displaystyle (-3,4)}$: each count as separate ways of making ${\displaystyle 3^{2}+4^{2}=25}$.

### Application to elliptic functions

Theta functions occur most commonly in the theory of [elliptic functions](https://en.wikipedia.org/wiki/Elliptic_function "Elliptic function"). With respect to one of the complex variables ${\displaystyle z}$, a theta function has a property expressing its behavior with respect to the addition of a period of the associated elliptic functions, making it a [quasiperiodic function](https://en.wikipedia.org/wiki/Quasiperiodic_function "Quasiperiodic function"). Abstractly, this quasiperiodicity comes from the [cohomology class](https://en.wikipedia.org/wiki/Group_cohomology "Group cohomology") of a [line bundle on a complex torus](https://en.wikipedia.org/wiki/Complex_torus "Complex torus"), a condition of [descent](https://en.wikipedia.org/wiki/Descent_\(category_theory\) "Descent (category theory)").

One interpretation of theta functions when dealing with the heat equation is that "a theta function is a special function that describes the evolution of temperature on a segment domain subject to certain boundary conditions".[^4]

Throughout this article, ${\displaystyle (e^{\pi i\tau })^{\alpha }}$ should be interpreted as ${\displaystyle e^{\alpha \pi i\tau }}$ (in order to resolve issues of choice of [branch](https://en.wikipedia.org/wiki/Branch_point#Branch_cuts "Branch point")).[^1]

## Jacobi theta function

There are several closely related functions called Jacobi theta functions, and [many different and incompatible systems of notation](https://en.wikipedia.org/wiki/Jacobi_theta_functions_\(notational_variations\) "Jacobi theta functions (notational variations)") for them. One **Jacobi theta function** (named after [Carl Gustav Jacob Jacobi](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi "Carl Gustav Jacob Jacobi")) is a function defined for two complex variables z and τ, where z can be any [complex number](https://en.wikipedia.org/wiki/Complex_number "Complex number") and τ is the [half-period ratio](https://en.wikipedia.org/wiki/Half-period_ratio "Half-period ratio"), confined to the [upper half-plane](https://en.wikipedia.org/wiki/Upper_half-plane "Upper half-plane"), which means it has a positive imaginary part. It is given by the formula

${\displaystyle {\begin{aligned}\vartheta (z;\tau )&=\sum _{n=-\infty }^{\infty }\exp \left(\pi in^{2}\tau +2\pi inz\right)\\&=1+2\sum _{n=1}^{\infty }q^{n^{2}}\cos(2\pi nz)\\&=\sum _{n=-\infty }^{\infty }q^{n^{2}}\eta ^{n}\end{aligned}}}$

where *q* = exp(*πiτ*) is the [nome](https://en.wikipedia.org/wiki/Nome_\(mathematics\) "Nome (mathematics)") and *η* = exp(2 *πiz*). It is a [Jacobi form](https://en.wikipedia.org/wiki/Jacobi_form "Jacobi form"). The restriction ensures that it is an [absolutely convergent](https://en.wikipedia.org/wiki/Absolute_convergence "Absolute convergence") series. At fixed τ, this is a [Fourier series](https://en.wikipedia.org/wiki/Fourier_series "Fourier series") for a 1-periodic [entire function](https://en.wikipedia.org/wiki/Entire_function "Entire function") of z. Accordingly, the theta function is 1-periodic in z:

${\displaystyle \vartheta (z+1;\tau )=\vartheta (z;\tau ).}$

By [completing the square](https://en.wikipedia.org/wiki/Completing_the_square "Completing the square"), it is also τ-quasiperiodic in z, with

${\displaystyle \vartheta (z+\tau$

Thus, in general,

${\displaystyle \vartheta (z+a+b\tau$

for any integers a and b.

For any fixed ${\displaystyle \tau }$, the function is an entire function on the complex plane, so by [Liouville's theorem](https://en.wikipedia.org/wiki/Liouville's_theorem_\(complex_analysis\) "Liouville's theorem (complex analysis)"), it cannot be doubly periodic in ${\displaystyle 1,\tau }$ unless it is constant, and so the best we can do is to make it periodic in ${\displaystyle 1}$ and quasi-periodic in ${\displaystyle \tau }$. Indeed, since 
$$
{\displaystyle \left|{\frac {\vartheta (z+a+b\tau
$$
 and ${\displaystyle \Im (\tau )>0}$, the function ${\displaystyle \vartheta (z,\tau )}$ is unbounded, as required by Liouville's theorem.

It is in fact the most general entire function with 2 quasi-periods, in the following sense:[^5]

**Theorem** —If ${\displaystyle f:\mathbb {C} \to \mathbb {C} }$ is entire and nonconstant, and satisfies the functional equations ${\displaystyle {\begin{cases}f(z+1)=f(z)\\f(z+\tau )=e^{az+2\pi ib}f(z)\end{cases}}}$ for some constant ${\displaystyle a,b\in \mathbb {C} }$.

If ${\displaystyle a=0}$, then ${\displaystyle b=\tau }$ and ${\displaystyle f(z)=e^{2\pi iz}}$. If ${\displaystyle a=-2\pi i}$, then ${\displaystyle f(z)=C\vartheta (z+{\frac {1}{2}}\tau +b,\tau )}$ for some nonzero ${\displaystyle C\in \mathbb {C} }$.

![](https://upload.wikimedia.org/wikipedia/commons/a/ab/Complex_theta_animated1.gif)

Theta function θ 1 with different nome q = e iπτ. The black dot in the right-hand picture indicates how changes with τ.

![](https://upload.wikimedia.org/wikipedia/commons/4/43/Complex_theta_animated2.gif)

Theta function θ 1 with different nome q = e iπτ. The black dot in the right-hand picture indicates how changes with τ.

## Auxiliary functions

The Jacobi theta function defined above is sometimes considered along with three auxiliary theta functions, in which case it is written with a double 0 subscript:

${\displaystyle \vartheta _{00}(z;\tau )=\vartheta (z;\tau )}$

The auxiliary (or half-period) functions are defined by

${\displaystyle {\begin{aligned}\vartheta _{01}(z;\tau )&=\vartheta \left(z+{\tfrac {1}{2}};\tau \right)\\[3pt]\vartheta _{10}(z;\tau )&=\exp \left({\tfrac {1}{4}}\pi i\tau +\pi iz\right)\vartheta \left(z+{\tfrac {1}{2}}\tau$

This notation follows [Riemann](https://en.wikipedia.org/wiki/Bernhard_Riemann "Bernhard Riemann") and [Mumford](https://en.wikipedia.org/wiki/David_Mumford "David Mumford"); [Jacobi](https://en.wikipedia.org/wiki/Carl_Gustav_Jacobi "Carl Gustav Jacobi") 's original formulation was in terms of the [nome](https://en.wikipedia.org/wiki/Nome_\(mathematics\) "Nome (mathematics)") *q* = *e* <sup><i>iπτ</i></sup> rather than τ. In Jacobi's notation the θ-functions are written:

${\displaystyle {\begin{aligned}\theta _{1}(z;q)&=\theta _{1}(\pi z,q)=-\vartheta _{11}(z;\tau )\\\theta _{2}(z;q)&=\theta _{2}(\pi z,q)=\vartheta _{10}(z;\tau )\\\theta _{3}(z;q)&=\theta _{3}(\pi z,q)=\vartheta _{00}(z;\tau )\\\theta _{4}(z;q)&=\theta _{4}(\pi z,q)=\vartheta _{01}(z;\tau )\end{aligned}}}$

![](https://en.wikipedia.org/wiki/File:Jacobi_theta_1.png)

Jacobi theta 1

![](https://en.wikipedia.org/wiki/File:Jacobi_theta_2.png)

Jacobi theta 2

![](https://en.wikipedia.org/wiki/File:Jacobi_theta_3.png)

Jacobi theta 3

![](https://en.wikipedia.org/wiki/File:Jacobi_theta_4.png)

Jacobi theta 4

The above definitions of the Jacobi theta functions are by no means unique. See [Jacobi theta functions (notational variations)](https://en.wikipedia.org/wiki/Jacobi_theta_functions_\(notational_variations\) "Jacobi theta functions (notational variations)") for further discussion.

If we set *z* = 0 in the above theta functions, we obtain four functions of τ only, defined on the upper half-plane. These functions are called *Theta Nullwert* functions, based on the German term for *zero value* because of the annullation of the left entry in the theta function expression. Alternatively, we obtain four functions of q only, defined on the [unit disk](https://en.wikipedia.org/wiki/Unit_disk "Unit disk") ${\displaystyle |q|<1}$. They are sometimes called [theta constants](https://en.wikipedia.org/wiki/Theta_constant "Theta constant"):[^2]

${\displaystyle {\begin{aligned}\vartheta _{11}(0;\tau )&=-\theta _{1}(q)=-\sum _{n=-\infty }^{\infty }(-1)^{n-1/2}q^{(n+1/2)^{2}}\\\vartheta _{10}(0;\tau )&=\theta _{2}(q)=\sum _{n=-\infty }^{\infty }q^{(n+1/2)^{2}}\\\vartheta _{00}(0;\tau )&=\theta _{3}(q)=\sum _{n=-\infty }^{\infty }q^{n^{2}}\\\vartheta _{01}(0;\tau )&=\theta _{4}(q)=\sum _{n=-\infty }^{\infty }(-1)^{n}q^{n^{2}}\end{aligned}}}$

with the [nome](https://en.wikipedia.org/wiki/Nome_\(mathematics\) "Nome (mathematics)") *q* = *e* <sup><i>iπτ</i></sup>. Observe that ${\displaystyle \theta _{1}(q)=0}$. These can be used to define a variety of [modular forms](https://en.wikipedia.org/wiki/Modular_forms "Modular forms"), and to parametrize certain curves; in particular, the **Jacobi identity** is

${\displaystyle \theta _{2}(q)^{4}+\theta _{4}(q)^{4}=\theta _{3}(q)^{4}}$

or equivalently,

${\displaystyle \vartheta _{01}(0;\tau )^{4}+\vartheta _{10}(0;\tau )^{4}=\vartheta _{00}(0;\tau )^{4}}$

which is the [Fermat curve](https://en.wikipedia.org/wiki/Fermat_curve "Fermat curve") of degree four.

## Jacobi identities

Jacobi's identities describe how theta functions transform under the [modular group](https://en.wikipedia.org/wiki/Modular_group "Modular group"), which is generated by *τ* ↦ *τ* + 1 and *τ* ↦ −⁠1 *τ* ⁠. Equations for the first transform are easily found since adding one to τ in the exponent has the same effect as adding ⁠12⁠ to z (*n* ≡ *n* <sup>2</sup> [mod](https://en.wikipedia.org/wiki/Modular_arithmetic "Modular arithmetic") 2). For the second, let

${\displaystyle \alpha =(-i\tau )^{\frac {1}{2}}\exp \left({\frac {\pi }{\tau }}iz^{2}\right).}$

Then

${\displaystyle {\begin{aligned}\vartheta _{00}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{00}(z;\tau )\quad &\vartheta _{01}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{10}(z;\tau )\\[3pt]\vartheta _{10}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=\alpha \,\vartheta _{01}(z;\tau )\quad &\vartheta _{11}\!\left({\frac {z}{\tau }};{\frac {-1}{\tau }}\right)&=-i\alpha \,\vartheta _{11}(z;\tau ).\end{aligned}}}$

## Theta functions in terms of the nome

Instead of expressing the Theta functions in terms of z and τ, we may express them in terms of arguments w and the [nome](https://en.wikipedia.org/wiki/Nome_\(mathematics\) "Nome (mathematics)") q, where *w* = *e* <sup><i>πiz</i></sup> and *q* = *e* <sup><i>πiτ</i></sup>. In this form, the functions become

${\displaystyle {\begin{aligned}\vartheta _{00}(w,q)&=\sum _{n=-\infty }^{\infty }\left(w^{2}\right)^{n}q^{n^{2}}\quad &\vartheta _{01}(w,q)&=\sum _{n=-\infty }^{\infty }(-1)^{n}\left(w^{2}\right)^{n}q^{n^{2}}\\[3pt]\vartheta _{10}(w,q)&=\sum _{n=-\infty }^{\infty }\left(w^{2}\right)^{n+{\frac {1}{2}}}q^{\left(n+{\frac {1}{2}}\right)^{2}}\quad &\vartheta _{11}(w,q)&=i\sum _{n=-\infty }^{\infty }(-1)^{n}\left(w^{2}\right)^{n+{\frac {1}{2}}}q^{\left(n+{\frac {1}{2}}\right)^{2}}.\end{aligned}}}$

We see that the theta functions can also be defined in terms of w and q, without a direct reference to the exponential function. These formulas can, therefore, be used to define the Theta functions over other [fields](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") where the exponential function might not be everywhere defined, such as fields of [p-adic numbers](https://en.wikipedia.org/wiki/P-adic_number "P-adic number").

## Product representations

The [Jacobi triple product](https://en.wikipedia.org/wiki/Jacobi_triple_product "Jacobi triple product") (a special case of the [Macdonald identities](https://en.wikipedia.org/wiki/Macdonald_identities "Macdonald identities")) tells us that for complex numbers w and q with | *q* | < 1 and *w* ≠ 0 we have

${\displaystyle \prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+w^{2}q^{2m-1}\right)\left(1+w^{-2}q^{2m-1}\right)=\sum _{n=-\infty }^{\infty }w^{2n}q^{n^{2}}.}$

It can be proven by elementary means, as for instance in Hardy and Wright's *[An Introduction to the Theory of Numbers](https://en.wikipedia.org/wiki/An_Introduction_to_the_Theory_of_Numbers "An Introduction to the Theory of Numbers")*.

If we express the theta function in terms of the nome *q* = *e* <sup><i>πiτ</i></sup> (noting some authors instead set *q* = *e* <sup>2 <i>πiτ</i></sup>) and take *w* = *e* <sup><i>πiz</i></sup> then

${\displaystyle \vartheta (z;\tau )=\sum _{n=-\infty }^{\infty }\exp(\pi i\tau n^{2})\exp(2\pi izn)=\sum _{n=-\infty }^{\infty }w^{2n}q^{n^{2}}.}$

We therefore obtain a product formula for the theta function in the form

${\displaystyle \vartheta (z;\tau )=\prod _{m=1}^{\infty }{\big (}1-\exp(2m\pi i\tau ){\big )}{\Big (}1+\exp {\big (}(2m-1)\pi i\tau +2\pi iz{\big )}{\Big )}{\Big (}1+\exp {\big (}(2m-1)\pi i\tau -2\pi iz{\big )}{\Big )}.}$

In terms of w and q:

${\displaystyle {\begin{aligned}\vartheta (z;\tau )&=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+q^{2m-1}w^{2}\right)\left(1+{\frac {q^{2m-1}}{w^{2}}}\right)\\&=\left(q^{2};q^{2}\right)_{\infty }\,\left(-w^{2}q;q^{2}\right)_{\infty }\,\left(-{\frac {q}{w^{2}}};q^{2}\right)_{\infty }\\&=\left(q^{2};q^{2}\right)_{\infty }\,\theta \left(-w^{2}q;q^{2}\right)\end{aligned}}}$

where (; ) <sub>∞</sub> is the [q-Pochhammer symbol](https://en.wikipedia.org/wiki/Q-Pochhammer_symbol "Q-Pochhammer symbol") and *θ* (; ) is the [q-theta function](https://en.wikipedia.org/wiki/Q-theta_function "Q-theta function"). Expanding terms out, the Jacobi triple product can also be written

${\displaystyle \prod _{m=1}^{\infty }\left(1-q^{2m}\right){\Big (}1+\left(w^{2}+w^{-2}\right)q^{2m-1}+q^{4m-2}{\Big )},}$

which we may also write as

${\displaystyle \vartheta (z\mid q)=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+2\cos(2\pi z)q^{2m-1}+q^{4m-2}\right).}$

This form is valid in general but clearly is of particular interest when z is real. Similar product formulas for the auxiliary theta functions are

${\displaystyle {\begin{aligned}\vartheta _{01}(z\mid q)&=\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1-2\cos(2\pi z)q^{2m-1}+q^{4m-2}\right),\\[3pt]\vartheta _{10}(z\mid q)&=2q^{\frac {1}{4}}\cos(\pi z)\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1+2\cos(2\pi z)q^{2m}+q^{4m}\right),\\[3pt]\vartheta _{11}(z\mid q)&=-2q^{\frac {1}{4}}\sin(\pi z)\prod _{m=1}^{\infty }\left(1-q^{2m}\right)\left(1-2\cos(2\pi z)q^{2m}+q^{4m}\right).\end{aligned}}}$

In particular, 
$$
{\displaystyle \lim _{q\to 0}{\frac {\vartheta _{10}(z\mid q)}{2q^{\frac {1}{4}}}}=\cos(\pi z),\quad \lim _{q\to 0}{\frac {-\vartheta _{11}(z\mid q)}{2q^{\frac {1}{4}}}}=\sin(\pi z)}
$$
 so we may interpret them as one-parameter deformations of the periodic functions ${\displaystyle \sin ,\cos }$, again validating the interpretation of the theta function as the most general 2 quasi-period function.

## Integral representations

The Jacobi theta functions have the following integral representations:

${\displaystyle {\begin{aligned}\vartheta _{00}(z;\tau )&=-i\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi u)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{01}(z;\tau )&=-i\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{10}(z;\tau )&=-ie^{i\pi z+{\frac {1}{4}}i\pi \tau }\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi u+\pi \tau u)}{\sin(\pi u)}}\mathrm {d} u;\\[6pt]\vartheta _{11}(z;\tau )&=e^{i\pi z+{\frac {1}{4}}i\pi \tau }\int _{i-\infty }^{i+\infty }e^{i\pi \tau u^{2}}{\frac {\cos(2\pi uz+\pi \tau u)}{\sin(\pi u)}}\mathrm {d} u.\end{aligned}}}$

The Theta Nullwert function ${\displaystyle \theta _{3}(q)}$ as this integral identity:

${\displaystyle \theta _{3}(q)=1+{\frac {4q{\sqrt {\ln(1/q)}}}{\sqrt {\pi }}}\int _{0}^{\infty }{\frac {\exp[-\ln(1/q)\,x^{2}]\{1-q^{2}\cos[2\ln(1/q)\,x]\}}{1-2q^{2}\cos[2\ln(1/q)\,x]+q^{4}}}\,\mathrm {d} x}$

This formula was discussed in the essay *Square series generating function transformations* by the mathematician Maxie Schmidt from Georgia in Atlanta.

Based on this formula following three eminent examples are given:

${\displaystyle {\biggl [}{\frac {2}{\pi }}K{\bigl (}{\frac {1}{2}}{\sqrt {2}}{\bigr )}{\biggr ]}^{1/2}=\theta _{3}{\bigl [}\exp(-\pi ){\bigr ]}=1+4\exp(-\pi )\int _{0}^{\infty }{\frac {\exp(-\pi x^{2})[1-\exp(-2\pi )\cos(2\pi x)]}{1-2\exp(-2\pi )\cos(2\pi x)+\exp(-4\pi )}}\,\mathrm {d} x}$

${\displaystyle {\biggl [}{\frac {2}{\pi }}K({\sqrt {2}}-1){\biggr ]}^{1/2}=\theta _{3}{\bigl [}\exp(-{\sqrt {2}}\,\pi ){\bigr ]}=1+4\,{\sqrt[{4}]{2}}\exp(-{\sqrt {2}}\,\pi )\int _{0}^{\infty }{\frac {\exp(-{\sqrt {2}}\,\pi x^{2})[1-\exp(-2{\sqrt {2}}\,\pi )\cos(2{\sqrt {2}}\,\pi x)]}{1-2\exp(-2{\sqrt {2}}\,\pi )\cos(2{\sqrt {2}}\,\pi x)+\exp(-4{\sqrt {2}}\,\pi )}}\,\mathrm {d} x}$

${\displaystyle {\biggl \{}{\frac {2}{\pi }}K{\bigl [}\sin {\bigl (}{\frac {\pi }{12}}{\bigr )}{\bigr ]}{\biggr \}}^{1/2}=\theta _{3}{\bigl [}\exp(-{\sqrt {3}}\,\pi ){\bigr ]}=1+4\,{\sqrt[{4}]{3}}\exp(-{\sqrt {3}}\,\pi )\int _{0}^{\infty }{\frac {\exp(-{\sqrt {3}}\,\pi x^{2})[1-\exp(-2{\sqrt {3}}\,\pi )\cos(2{\sqrt {3}}\,\pi x)]}{1-2\exp(-2{\sqrt {3}}\,\pi )\cos(2{\sqrt {3}}\,\pi x)+\exp(-4{\sqrt {3}}\,\pi )}}\,\mathrm {d} x}$

Furthermore, the theta examples ${\displaystyle \theta _{3}({\tfrac {1}{2}})}$ and ${\displaystyle \theta _{3}({\tfrac {1}{3}})}$ shall be displayed:

${\displaystyle \theta _{3}\left({\frac {1}{2}}\right)=1+2\sum _{n=1}^{\infty }{\frac {1}{2^{n^{2}}}}=1+2\pi ^{-1/2}{\sqrt {\ln(2)}}\int _{0}^{\infty }{\frac {\exp[-\ln(2)\,x^{2}]\{16-4\cos[2\ln(2)\,x]\}}{17-8\cos[2\ln(2)\,x]}}\,\mathrm {d} x}$

${\displaystyle \theta _{3}\left({\frac {1}{2}}\right)=2.128936827211877158669\ldots }$

${\displaystyle \theta _{3}\left({\frac {1}{3}}\right)=1+2\sum _{n=1}^{\infty }{\frac {1}{3^{n^{2}}}}=1+{\frac {4}{3}}\pi ^{-1/2}{\sqrt {\ln(3)}}\int _{0}^{\infty }{\frac {\exp[-\ln(3)\,x^{2}]\{81-9\cos[2\ln(3)\,x]\}}{82-18\cos[2\ln(3)\,x]}}\,\mathrm {d} x}$

${\displaystyle \theta _{3}\left({\frac {1}{3}}\right)=1.691459681681715341348\ldots }$

[^1]: See e.g. [https://dlmf.nist.gov/20.1](https://dlmf.nist.gov/20.1). Note that this is, in general, not equivalent to the usual interpretation ${\displaystyle (e^{z})^{\alpha }=e^{\alpha \operatorname {Log} e^{z}}}$ when ${\displaystyle z}$ is outside the strip ${\displaystyle -\pi <\operatorname {Im} z\leq \pi }$. Here, ${\displaystyle \operatorname {Log} }$ denotes the principal branch of the [complex logarithm](https://en.wikipedia.org/wiki/Complex_logarithm#Properties "Complex logarithm").

[^2]: ${\displaystyle \theta _{1}(q)=0}$ for all ${\displaystyle q\in \mathbb {C} }$ with ${\displaystyle |q|<1}$.

[^3]: Tyurin, Andrey N. (30 October 2002). "Quantization, Classical and Quantum Field Theory and Theta-Functions". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0210466v1](https://arxiv.org/abs/math/0210466v1).

[^4]: Chang, Der-Chen (2011). *Heat Kernels for Elliptic and Sub-elliptic Operators*. Birkhäuser. p. 7.

[^5]: [*Tata Lectures on Theta I*](http://link.springer.com/10.1007/978-0-8176-4577-9). Modern Birkhäuser Classics. Boston, MA: Birkhäuser Boston. 2007. p. 4. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-0-8176-4577-9](https://doi.org/10.1007%2F978-0-8176-4577-9). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8176-4572-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8176-4572-4 "Special:BookSources/978-0-8176-4572-4").

[^6]: Yi, Jinhee (2004). ["Theta-function identities and the explicit formulas for theta-function and their applications"](https://doi.org/10.1016%2Fj.jmaa.2003.12.009). *Journal of Mathematical Analysis and Applications*. **292** (2): 381–400. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.jmaa.2003.12.009](https://doi.org/10.1016%2Fj.jmaa.2003.12.009).

[^7]: Berndt, Bruce C; Rebák, Örs (9 January 2022). ["Explicit Values for Ramanujan's Theta Function ϕ(q)"](https://doi.org/10.46298%2Fhrj.2022.8923). *Hardy-Ramanujan Journal*. **44** 8923. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[2112.11882](https://arxiv.org/abs/2112.11882). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.46298/hrj.2022.8923](https://doi.org/10.46298%2Fhrj.2022.8923). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [245851672](https://api.semanticscholar.org/CorpusID:245851672).

[^8]: Yi, Jinhee (15 April 2004). ["Theta-function identities and the explicit formulas for theta-function and their applications"](https://doi.org/10.1016%2Fj.jmaa.2003.12.009). *Journal of Mathematical Analysis and Applications*. **292** (2): 381–400. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.jmaa.2003.12.009](https://doi.org/10.1016%2Fj.jmaa.2003.12.009).

[^9]: Andreas Dieckmann: *[Table of Infinite Products Infinite Sums Infinite Series, Elliptic Theta.](http://www-elsa.physik.uni-bonn.de/~dieckman/InfProd/InfProd.html#InfinitexProducts)* Physikalisches Institut Universität Bonn, Abruf am 1. Oktober 2021.

[^10]: Landau (1899) zitiert nach [Borwein](https://en.wikipedia.org/wiki/Fibonacci-Folge?action=edit&redlink=1#Borwein "Fibonacci-Folge (page does not exist)"), Page 94, Exercise 3.

[^11]: ["Number-theoretical, combinatorial and integer functions – mpmath 1.1.0 documentation"](https://mpmath.org/doc/1.1.0/functions/numtheory.html). Retrieved 2021-07-18.

[^12]: Mező, István (2013), "Duplication formulae involving Jacobi theta functions and Gosper's q-trigonometric functions", *[Proceedings of the American Mathematical Society](https://en.wikipedia.org/wiki/Proceedings_of_the_American_Mathematical_Society "Proceedings of the American Mathematical Society")*, **141** (7): 2401–2410, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/s0002-9939-2013-11576-5](https://doi.org/10.1090%2Fs0002-9939-2013-11576-5)

[^13]: Mező, István (2012). ["A q-Raabe formula and an integral of the fourth Jacobi theta function"](https://doi.org/10.1016%2Fj.jnt.2012.08.025). *Journal of Number Theory*. **133** (2): 692–704. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.jnt.2012.08.025](https://doi.org/10.1016%2Fj.jnt.2012.08.025). [hdl](https://en.wikipedia.org/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[2437/166217](https://hdl.handle.net/2437%2F166217).

[^14]: [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein") ["Elliptic Alpha Function"](https://mathworld.wolfram.com/EllipticAlphaFunction.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld "MathWorld")*.

[^15]: ["integration - Curious integrals for Jacobi Theta Functions $\\int\_0^1 \\vartheta\_n(0,q)dq$"](https://math.stackexchange.com/q/1865615). 2022-08-13.

[^16]: Ohyama, Yousuke (1995). ["Differential relations of theta functions"](https://projecteuclid.org/euclid.ojm/1200786061). *Osaka Journal of Mathematics*. **32** (2): 431–450. [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0030-6126](https://search.worldcat.org/issn/0030-6126).

[^17]: Shimura, On modular forms of half integral weight

[^18]: ["Elliptic Integral Singular Value"](https://archive.lib.msu.edu/crcmath/math/math/e/e103.htm). *msu.edu*. Retrieved 2023-04-07.

[^19]: [Ramanujan's theta-function identities involving Lambert series](https://www.researchgate.net/publication/235432739_Ramanujan%27s_theta-function_identities_involving_Lambert_series)

[^20]: ["code golf - Strict partitions of a positive integer"](https://codegolf.stackexchange.com/questions/71941/strict-partitions-of-a-positive-integer). Retrieved 2022-03-09.

[^21]: ["A000009 - OEIS"](https://oeis.org/A000009). 2022-03-09.

[^22]: Mahlburg, Karl (2004). "The overpartition function modulo small powers of 2". *Discrete Mathematics*. **286** (3): 263–267. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.disc.2004.03.014](https://doi.org/10.1016%2Fj.disc.2004.03.014).

[^23]: Kim, Byungchan (28 April 2009). ["Elsevier Enhanced Reader"](https://doi.org/10.1016%2Fj.disc.2008.05.007). *Discrete Mathematics*. **309** (8): 2528–2532. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.disc.2008.05.007](https://doi.org/10.1016%2Fj.disc.2008.05.007).

[^24]: Eric W. Weisstein (2022-03-11). ["Partition Function P"](https://mathworld.wolfram.com/PartitionFunctionP.html).

[^25]: Eric W. Weisstein (2022-03-11). ["Partition Function Q"](https://mathworld.wolfram.com/PartitionFunctionQ.html).