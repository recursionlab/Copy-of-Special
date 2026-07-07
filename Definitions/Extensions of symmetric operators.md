---
title: "Extensions of symmetric operators"
source: "https://en.wikipedia.org/wiki/Extensions_of_symmetric_operators"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2007-04-23
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis "Functional analysis"), one is interested in **extensions of symmetric operators** acting on a [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"). Of particular importance is the existence, and sometimes explicit constructions, of [self-adjoint](https://en.wikipedia.org/wiki/Self-adjoint "Self-adjoint") extensions. This problem arises, for example, when one needs to specify domains of self-adjointness for formal expressions of [observables](https://en.wikipedia.org/wiki/Observable "Observable") in [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics "Quantum mechanics"). Other applications of solutions to this problem can be seen in various [moment problems](https://en.wikipedia.org/wiki/Moment_problem "Moment problem").

This article discusses a few related problems of this type. The unifying theme is that each problem has an operator-theoretic characterization which gives a corresponding parametrization of solutions. More specifically, finding self-adjoint extensions, with various requirements, of [symmetric operators](https://en.wikipedia.org/wiki/Symmetric_operator "Symmetric operator") is equivalent to finding unitary extensions of suitable [partial isometries](https://en.wikipedia.org/wiki/Partial_isometry "Partial isometry").

## Symmetric operators

Let ${\displaystyle H}$ be a Hilbert space. A [linear operator](https://en.wikipedia.org/wiki/Linear_operator "Linear operator") ${\displaystyle A}$ acting on ${\displaystyle H}$ with [dense](https://en.wikipedia.org/wiki/Dense_set "Dense set") [domain](https://en.wikipedia.org/wiki/Domain_of_a_function "Domain of a function") ${\displaystyle \operatorname {dom} (A)}$ is **symmetric** if

${\displaystyle \langle Ax,y\rangle =\langle x,Ay\rangle ,\quad \forall x,y\in \operatorname {dom} (A).}$

If ${\displaystyle \operatorname {dom} (A)=H}$, the [Hellinger-Toeplitz theorem](https://en.wikipedia.org/wiki/Hellinger-Toeplitz_theorem "Hellinger-Toeplitz theorem") says that ${\displaystyle A}$ is a [bounded operator](https://en.wikipedia.org/wiki/Bounded_operator "Bounded operator"), in which case ${\displaystyle A}$ is [self-adjoint](https://en.wikipedia.org/wiki/Self-adjoint_operator "Self-adjoint operator") and the extension problem is trivial. In general, a symmetric operator is self-adjoint if the domain of its adjoint, ${\displaystyle \operatorname {dom} (A^{*})}$, lies in ${\displaystyle \operatorname {dom} (A)}$.

When dealing with [unbounded operators](https://en.wikipedia.org/wiki/Unbounded_operator "Unbounded operator"), it is often desirable to be able to assume that the operator in question is [closed](https://en.wikipedia.org/wiki/Closed_operator "Closed operator"). In the present context, it is a convenient fact that every densely defined, symmetric operator ${\displaystyle A}$ is [closable](https://en.wikipedia.org/wiki/Closable_operator "Closable operator"). That is, ${\displaystyle A}$ has the smallest closed extension, called the *closure* of ${\displaystyle A}$. This can be shown by invoking the symmetric assumption and [Riesz representation theorem](https://en.wikipedia.org/wiki/Riesz_representation_theorem "Riesz representation theorem"). Since ${\displaystyle A}$ and its closure have the same closed extensions, it can always be assumed that the symmetric operator of interest is closed.

In the next section, a symmetric operator will be assumed to be [densely defined](https://en.wikipedia.org/wiki/Densely_defined "Densely defined") and closed.

### Self-adjoint extensions of symmetric operators

If an operator ${\displaystyle A}$ on the Hilbert space ${\displaystyle H}$ is symmetric, when does it have self-adjoint extensions? An operator that has a unique self-adjoint extension is said to be **essentially self-adjoint**; equivalently, an operator is essentially self-adjoint if its closure (the operator whose graph is the closure of the [graph](https://en.wikipedia.org/wiki/Graph_of_a_function "Graph of a function") of ${\displaystyle A}$) is self-adjoint. In general, a symmetric operator could have many self-adjoint extensions or none at all. Thus, we would like a classification of its self-adjoint extensions.

The first basic criterion for essential self-adjointness is the following:[^1]

**Theorem** — If ${\displaystyle A}$ is a symmetric operator on ${\displaystyle H}$, then ${\displaystyle A}$ is essentially self-adjoint if and only if the [range](https://en.wikipedia.org/wiki/Image_\(mathematics\)#Image_of_a_function "Image (mathematics)") of the operators ${\displaystyle A-i}$ and ${\displaystyle A+i}$ are dense in ${\displaystyle H}$.

Equivalently, ${\displaystyle A}$ is essentially self-adjoint if and only if the operators ${\displaystyle A^{*}\pm i}$ have trivial [kernels](https://en.wikipedia.org/wiki/Kernel_\(linear_algebra\) "Kernel (linear algebra)").[^2] That is to say, ${\displaystyle A}$ *fails to be* self-adjoint if and only if ${\displaystyle A^{*}}$ has an eigenvector with [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number") eigenvalues ${\displaystyle \pm i}$.

Another way of looking at the issue is provided by the **[Cayley transform](https://en.wikipedia.org/wiki/Cayley_transform "Cayley transform")** of a self-adjoint operator and the deficiency indices.[^3]

**Theorem** —Suppose ${\displaystyle A}$ is a symmetric operator. Then there is a unique densely defined linear operator 
$$
{\displaystyle W(A):\operatorname {ran} (A+i)\to \operatorname {ran} (A-i)}
$$
 such that 
$$
{\displaystyle W(A)(Ax+ix)=Ax-ix,\quad x\in \operatorname {dom} (A).}
$$

${\displaystyle W(A)}$ is [isometric](https://en.wikipedia.org/wiki/Isometry "Isometry") on its domain. Moreover, ${\displaystyle \operatorname {ran} (1-W(A))}$ is dense in ${\displaystyle A}$.

Conversely, given any densely defined operator ${\displaystyle U}$ which is isometric on its (not necessarily closed) domain and such that ${\displaystyle 1-U}$ is dense, then there is a (unique) densely defined symmetric operator

${\displaystyle S(U):\operatorname {ran} (1-U)\to \operatorname {ran} (1+U)}$

such that

${\displaystyle S(U)(x-Ux)=i(x+Ux),\quad x\in \operatorname {dom} (U).}$

The mappings ${\displaystyle W}$ and ${\displaystyle S}$ are inverses of each other, i.e., ${\displaystyle S(W(A))=A}$.

The mapping ${\displaystyle A\mapsto W(A)}$ is called the **Cayley transform**. It associates a [partially defined isometry](https://en.wikipedia.org/wiki/Partial_isometry "Partial isometry") to any symmetric densely defined operator. Note that the mappings ${\displaystyle W}$ and ${\displaystyle S}$ are [monotone](https://en.wikipedia.org/wiki/Monotone_convergence_theorem "Monotone convergence theorem"): This means that if ${\displaystyle B}$ is a symmetric operator that extends the densely defined symmetric operator ${\displaystyle A}$, then ${\displaystyle W(B)}$ extends ${\displaystyle W(A)}$, and similarly for ${\displaystyle S}$.

**Theorem** —A necessary and sufficient condition for ${\displaystyle A}$ to be self-adjoint is that its Cayley transform ${\displaystyle W(A)}$ be [unitary](https://en.wikipedia.org/wiki/Unitary_operator "Unitary operator") on ${\displaystyle H}$.

This immediately gives us a necessary and sufficient condition for ${\displaystyle A}$ to have a self-adjoint extension, as follows:

**Theorem** —A necessary and sufficient condition for ${\displaystyle A}$ to have a self-adjoint extension is that ${\displaystyle W(A)}$ have a unitary extension to ${\displaystyle H}$.

A partially defined isometric operator ${\displaystyle V}$ on a Hilbert space ${\displaystyle H}$ has a unique isometric extension to the norm closure of ${\displaystyle \operatorname {dom} (V)}$. A partially defined isometric operator with closed domain is called a [partial isometry](https://en.wikipedia.org/wiki/Partial_isometry "Partial isometry").

Define the **deficiency subspaces** of *A* by

${\displaystyle {\begin{aligned}K_{+}&=\operatorname {ran} (A+i)^{\perp }\\K_{-}&=\operatorname {ran} (A-i)^{\perp }\end{aligned}}}$

In this language, the description of the self-adjoint extension problem given by the theorem can be restated as follows: a symmetric operator ${\displaystyle A}$ has self-adjoint extensions if and only if the deficiency subspaces ${\displaystyle K_{+}}$ and ${\displaystyle K_{-}}$ have the same dimension.[^4]

The **deficiency indices** of a partial isometry ${\displaystyle V}$ are defined as the dimension of the [orthogonal complements](https://en.wikipedia.org/wiki/Orthogonal_complement "Orthogonal complement") of the domain and range:

${\displaystyle {\begin{aligned}n_{+}(V)&=\dim \operatorname {dom} (V)^{\perp }\\n_{-}(V)&=\dim \operatorname {ran} (V)^{\perp }\end{aligned}}}$

**Theorem** —A partial isometry ${\displaystyle V}$ has a unitary extension if and only if the deficiency indices are identical. Moreover, ${\displaystyle V}$ has a *unique* unitary extension if and only if the deficiency indices are both zero.

We see that there is a bijection between symmetric extensions of an operator and isometric extensions of its Cayley transform. The symmetric extension is self-adjoint if and only if the corresponding isometric extension is unitary.

A symmetric operator has a unique self-adjoint extension if and only if both its deficiency indices are zero. Such an operator is said to be **essentially self-adjoint**. Symmetric operators which are not essentially self-adjoint may still have a [canonical](https://en.wikipedia.org/wiki/Canonical_form "Canonical form") self-adjoint extension. Such is the case for *non-negative* symmetric operators (or more generally, operators which are bounded below). These operators always have a canonically defined [Friedrichs extension](https://en.wikipedia.org/wiki/Friedrichs_extension "Friedrichs extension") and for these operators we can define a canonical functional calculus. Many operators that occur in analysis are bounded below (such as the negative of the [Laplacian](https://en.wikipedia.org/wiki/Laplacian "Laplacian") operator), so the issue of essential adjointness for these operators is less critical.

Suppose ${\displaystyle A}$ is symmetric densely defined. Then any symmetric extension of ${\displaystyle A}$ is a restriction of ${\displaystyle A^{*}}$. Indeed, ${\displaystyle A\subseteq B}$ and ${\displaystyle B}$ symmetric yields ${\displaystyle B\subseteq A^{*}}$ by applying the definition of ${\displaystyle \operatorname {dom} (A^{*})}$. This notion leads to the **von Neumann formulae**:[^5]

**Theorem** — Suppose ${\displaystyle A}$ is a densely defined symmetric operator, with domain ${\displaystyle \operatorname {dom} (A)}$. Let 
$$
{\displaystyle N_{\pm }=\operatorname {ran} (A\pm i)^{\perp },}
$$
 be any pair of its deficiency subspaces. Then 
$$
{\displaystyle N_{\pm }=\operatorname {ker} (A^{*}\mp i),}
$$
 and 
$$
{\displaystyle \operatorname {dom} \left(A^{*}\right)=\operatorname {dom} \left({\overline {A}}\right)\oplus N_{+}\oplus N_{-},}
$$
 where the decomposition is orthogonal relative to the graph inner product of ${\displaystyle \operatorname {dom} (A^{*})}$: 
$$
{\displaystyle \langle \xi \mid \eta \rangle _{\text{graph}}=\langle \xi \mid \eta \rangle +\left\langle A^{*}\xi \mid A^{*}\eta \right\rangle .}
$$

### Example

Consider the Hilbert space ${\displaystyle L^{2}([0,1])}$. On the subspace of absolutely continuous function that vanish on the boundary, define the operator ${\displaystyle A}$ by

${\displaystyle Af=i{\frac {d}{dx}}f.}$

Integration by parts shows ${\displaystyle A}$ is symmetric. Its adjoint ${\displaystyle A^{*}}$ is the same operator with ${\displaystyle \operatorname {dom} (A^{*})}$ being the [absolutely continuous functions](https://en.wikipedia.org/wiki/Absolutely_continuous_function "Absolutely continuous function") with no boundary condition. We will see that extending *A* amounts to modifying the boundary conditions, thereby enlarging ${\displaystyle \operatorname {dom} (A)}$ and reducing ${\displaystyle \operatorname {dom} (A^{*})}$, until the two coincide.

Direct calculation shows that ${\displaystyle K_{+}}$ and ${\displaystyle K_{-}}$ are one-dimensional subspaces given by

${\displaystyle {\begin{aligned}K_{+}&=\operatorname {span} \{\phi _{+}=c\cdot e^{x}\}\\K_{-}&=\operatorname {span} \{\phi _{-}=c\cdot e^{-x}\}\end{aligned}}}$

where ${\displaystyle c}$ is a normalizing constant. The self-adjoint extensions ${\displaystyle A_{\alpha }}$ of ${\displaystyle A}$ are parametrized by the [circle group](https://en.wikipedia.org/wiki/Circle_group "Circle group") ${\displaystyle \mathbb {T} =\{\alpha \in \mathbb {C} :|\alpha |=1\}}$. Since ${\displaystyle ||e^{-x}||=||e^{\,x-1}||}$, a [unitary transformation](https://en.wikipedia.org/wiki/Unitary_transformation "Unitary transformation") ${\displaystyle U_{\alpha }:K_{-}\to K_{+}}$ defined by

${\displaystyle U_{\alpha }(\phi _{-})=\alpha \,c\,e^{-1}\phi _{+},\qquad |\alpha |=1.}$

there corresponds an extension ${\displaystyle A_{\alpha }}$ with domain

${\displaystyle \operatorname {dom} (A_{\alpha })=\{f+\beta (\phi _{-}+\alpha e^{-1}\phi _{+})|f\in \operatorname {dom} (A),\;\beta \in \mathbb {C} \}.}$

If ${\displaystyle f\in \operatorname {dom} (A_{\alpha })}$, then ${\displaystyle f}$ is absolutely continuous and

${\displaystyle \left|{\frac {f(0)}{f(1)}}\right|=\left|{\frac {e+\alpha }{1+e\alpha }}\right|=1.}$

Conversely, if ${\displaystyle f}$ is absolutely continuous and ${\displaystyle f(0)=\gamma f(1)}$ for some ${\displaystyle \gamma \in \mathbb {T} }$, then ${\displaystyle f}$ lies in the above domain.

The self-adjoint operators ${\displaystyle A_{\alpha }}$ are instances of the [momentum operator](https://en.wikipedia.org/wiki/Momentum_operator "Momentum operator") in quantum mechanics.

## Self-adjoint extension on a larger space

Every partial isometry can be extended, on a possibly larger space, to a unitary operator. Consequently, every symmetric operator has a self-adjoint extension, on a possibly larger space.

## Positive symmetric operators

A symmetric operator ${\displaystyle A}$ is called **positive** if

${\displaystyle \langle Ax,x\rangle \geq 0,\quad \forall x\in \operatorname {dom} (A).}$

It is known that for every such ${\displaystyle A}$, one has ${\displaystyle \operatorname {dim} K_{+}=\operatorname {dim} K_{-}}$. Therefore, every positive symmetric operator has self-adjoint extensions. The more interesting question in this direction is whether ${\displaystyle A}$ has positive self-adjoint extensions.

For two positive operators ${\displaystyle A}$ and ${\displaystyle B}$, we put ${\displaystyle A\leq B}$ if

${\displaystyle (A+1)^{-1}\geq (B+1)^{-1}}$

in the sense of bounded operators.

### Structure of 2 × 2 matrix contractions

While the extension problem for general symmetric operators is essentially that of extending partial isometries to unitaries, for positive symmetric operators the question becomes one of extending [contractions](https://en.wikipedia.org/wiki/Contraction_\(operator_theory\) "Contraction (operator theory)"): by "filling out" certain unknown entries of a 2 × 2 self-adjoint contraction, we obtain the positive self-adjoint extensions of a positive symmetric operator.

Before stating the relevant result, we first fix some terminology. For a contraction ${\displaystyle \Gamma }$, acting on ${\displaystyle H}$, we define its **defect operators** by

${\displaystyle {\begin{aligned}&D_{\Gamma }\;=(1-\Gamma ^{*}\Gamma )^{\frac {1}{2}}\\&D_{\Gamma ^{*}}=(1-\Gamma \Gamma ^{*})^{\frac {1}{2}}\end{aligned}}}$

The **defect spaces** of ${\displaystyle \Gamma }$ are

${\displaystyle {\begin{aligned}&{\mathcal {D}}_{\Gamma }\;=\operatorname {ran} (D_{\Gamma })\\&{\mathcal {D}}_{\Gamma ^{*}}=\operatorname {ran} (D_{\Gamma ^{*}})\end{aligned}}}$

The defect operators indicate the non-unitarity of ${\displaystyle \Gamma }$, while the defect spaces ensure uniqueness in some parameterizations. Using this machinery, one can explicitly describe the structure of general matrix contractions. We will only need the 2 × 2 case. Every 2 × 2 contraction ${\displaystyle \Gamma }$ can be uniquely expressed as

${\displaystyle \Gamma ={\begin{bmatrix}\Gamma _{1}&D_{\Gamma _{1}^{*}}\Gamma _{2}\\\Gamma _{3}D_{\Gamma _{1}}&-\Gamma _{3}\Gamma _{1}^{*}\Gamma _{2}+D_{\Gamma _{3}^{*}}\Gamma _{4}D_{\Gamma _{2}}\end{bmatrix}}}$

where each ${\displaystyle \Gamma _{i}}$ is a contraction.

### Extensions of Positive symmetric operators

The Cayley transform for general symmetric operators can be adapted to this special case. For every non-negative number ${\displaystyle a}$,

${\displaystyle \left|{\frac {a-1}{a+1}}\right|\leq 1.}$

This suggests we assign to every positive symmetric operator ${\displaystyle A}$ a contraction

${\displaystyle C_{A}:\operatorname {ran} (A+1)\rightarrow \operatorname {ran} (A-1)\subset H}$

defined by

${\displaystyle C_{A}(A+1)x=(A-1)x.\quad {\mbox{i.e.}}\quad C_{A}=(A-1)(A+1)^{-1}.\,}$

which have matrix representation

${\displaystyle C_{A}={\begin{bmatrix}\Gamma _{1}\\\Gamma _{3}D_{\Gamma _{1}}\end{bmatrix}}:\operatorname {ran} (A+1)\rightarrow {\begin{matrix}\operatorname {ran} (A+1)\\\oplus \\\operatorname {ran} (A+1)^{\perp }\end{matrix}}.}$

It is easily verified that the ${\displaystyle \Gamma _{1}}$ entry, ${\displaystyle C_{A}}$ projected onto ${\displaystyle \operatorname {ran} (A+1)=\operatorname {dom} (C_{A})}$, is self-adjoint. The operator ${\displaystyle A}$ can be written as

${\displaystyle A=(1+C_{A})(1-C_{A})^{-1}\,}$

with ${\displaystyle \operatorname {dom} (A)=\operatorname {ran} (C_{A}-1)}$. If ${\displaystyle {\tilde {C}}}$ is a contraction that extends ${\displaystyle C_{A}}$ and its projection onto its domain is self-adjoint, then it is clear that its inverse Cayley transform

${\displaystyle {\tilde {A}}=(1+{\tilde {C}})(1-{\tilde {C}})^{-1}}$

defined on ${\displaystyle \operatorname {ran} (1-{\tilde {C}})}$ is a positive symmetric extension of ${\displaystyle A}$. The symmetric property follows from its projection onto its own domain being self-adjoint and positivity follows from contractivity. The converse is also true: given a positive symmetric extension of ${\displaystyle A}$, its Cayley transform is a contraction satisfying the stated "partial" self-adjoint property.

**Theorem** —The positive symmetric extensions of ${\displaystyle A}$ are in one-to-one correspondence with the extensions of its Cayley transform where, if ${\displaystyle C}$ is such an extension, we require ${\displaystyle C}$ projected onto ${\displaystyle \operatorname {dom} (C)}$ be self-adjoint.

The unitarity criterion of the Cayley transform is replaced by self-adjointness for positive operators.

**Theorem** —A symmetric positive operator ${\displaystyle A}$ is self-adjoint if and only if its Cayley transform is a self-adjoint contraction defined on all of ${\displaystyle H}$, i.e. when ${\displaystyle \operatorname {ran} (A+1)=H}$.

Therefore, finding self-adjoint extension for a positive symmetric operator becomes a " [matrix completion](https://en.wikipedia.org/wiki/Matrix_completion "Matrix completion") problem". Specifically, we need to embed the column contraction ${\displaystyle C_{A}}$ into a 2 × 2 self-adjoint contraction. This can always be done and the structure of such contractions gives a parametrization of all possible extensions.

By the preceding subsection, all self-adjoint extensions of ${\displaystyle C_{A}}$ takes the form

${\displaystyle {\tilde {C}}(\Gamma _{4})={\begin{bmatrix}\Gamma _{1}&D_{\Gamma _{1}}\Gamma _{3}^{*}\\\Gamma _{3}D_{\Gamma _{1}}&-\Gamma _{3}\Gamma _{1}\Gamma _{3}^{*}+D_{\Gamma _{3}^{*}}\Gamma _{4}D_{\Gamma _{3}^{*}}\end{bmatrix}}.}$

So the self-adjoint positive extensions of ${\displaystyle A}$ are in bijective correspondence with the self-adjoint contractions ${\displaystyle \Gamma _{4}}$ on the defect space ${\displaystyle {\mathcal {D}}_{\Gamma _{3}^{*}}}$ of ${\displaystyle \Gamma _{3}}$. The contractions ${\displaystyle {\tilde {C}}(-1)}$ and ${\displaystyle {\tilde {C}}(1)}$ give rise to positive extensions ${\displaystyle A_{0}}$ and ${\displaystyle A_{\infty }}$ respectively. These are the *smallest* and *largest* positive extensions of ${\displaystyle A}$ in the sense that

${\displaystyle A_{0}\leq B\leq A_{\infty }}$

for any positive self-adjoint extension ${\displaystyle B}$ of ${\displaystyle A}$. The operator ${\displaystyle A_{\infty }}$ is the **[Friedrichs extension](https://en.wikipedia.org/wiki/Friedrichs_extension "Friedrichs extension")** of ${\displaystyle A}$ and ${\displaystyle A_{0}}$ is the **von Neumann-Krein extension** of ${\displaystyle A}$.

Similar results can be obtained for [accretive operators](https://en.wikipedia.org/wiki/Accretive_operator "Accretive operator").

## Notes

## References

- Akhiezer, Naum Ilʹich (1981). *Theory of Linear Operators in Hilbert Space*. Boston: Pitman. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-273-08496-8](https://en.wikipedia.org/wiki/Special:BookSources/0-273-08496-8 "Special:BookSources/0-273-08496-8").
- A. Alonso and B. Simon, The Birman-Krein-Vishik theory of self-adjoint extensions of semibounded operators. *J. Operator Theory* **4** (1980), 251-270.
- Gr. Arsene and A. Gheondea, Completing matrix contractions, *J. Operator Theory* **7** (1982), 179-189.
- N. Dunford and J.T. Schwartz, *Linear Operators*, Part II, Interscience, 1958.
- Hall, B. C. (2013), *Quantum Theory for Mathematicians*, Graduate Texts in Mathematics, vol. 267, Springer, [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2013qtm..book.....H](https://ui.adsabs.harvard.edu/abs/2013qtm..book.....H), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1461471158](https://en.wikipedia.org/wiki/Special:BookSources/978-1461471158 "Special:BookSources/978-1461471158")
- Jørgensen, Palle E. T.; Kornelson, Keri A.; Shuman, Karen L. (2011). *Iterated Function Systems, Moments, and Transformations of Infinite Matrices*. Providence, RI: American Mathematical Soc. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8218-5248-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-5248-4 "Special:BookSources/978-0-8218-5248-4").
- Reed, M.; Simon, B. (1980). *Methods of Modern Mathematical Physics: Vol 1: Functional analysis*. Academic Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-12-585050-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-12-585050-6 "Special:BookSources/978-0-12-585050-6").
- [Reed, M.](https://en.wikipedia.org/wiki/Michael_C._Reed "Michael C. Reed"); [Simon, B.](https://en.wikipedia.org/wiki/Barry_Simon "Barry Simon") (1972), *Methods of Mathematical Physics: Vol 2: Fourier Analysis, Self-Adjointness*, Academic Press
- Rudin, Walter (1991). *Functional Analysis*. Boston, Mass.: McGraw-Hill Science, Engineering & Mathematics. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-07-054236-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-07-054236-5 "Special:BookSources/978-0-07-054236-5").

[^1]: [Hall 2013](#CITEREFHall2013) Theorem 9.21

[^2]: [Hall 2013](#CITEREFHall2013) Corollary 9.22

[^3]: [Rudin 1991](#CITEREFRudin1991), p. 356-357 §13.17.

[^4]: [Jørgensen, Kornelson & Shuman 2011](#CITEREFJørgensenKornelsonShuman2011), p. 85.

[^5]: [Akhiezer 1981](#CITEREFAkhiezer1981), p. 354.