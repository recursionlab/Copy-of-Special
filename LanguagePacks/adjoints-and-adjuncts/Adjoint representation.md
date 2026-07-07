---
title: "Adjoint representation"
source: "https://en.wikipedia.org/wiki/Adjoint_representation"
author:
  - "[[Wikipedia]]"
published: 2003-08-22
created: 2026-04-29
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **adjoint representation** (or **adjoint action**) of a [Lie group](https://en.wikipedia.org/wiki/Lie_group "Lie group") *G* is a way of representing the elements of the group as [linear transformations](https://en.wikipedia.org/wiki/Linear_map "Linear map") of the group's [Lie algebra](https://en.wikipedia.org/wiki/Lie_algebra "Lie algebra"), considered as a [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space"). For example, if *G* is ${\displaystyle \mathrm {GL} (n,\mathbb {R} )}$, the Lie group of real [*n* -by- *n* invertible matrices](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix"), then the adjoint representation is the group homomorphism that sends an invertible *n* -by- *n* matrix ${\displaystyle g}$ to an [endomorphism](https://en.wikipedia.org/wiki/Endomorphism "Endomorphism") of the vector space of all linear transformations of ${\displaystyle \mathbb {R} ^{n}}$ defined by: ${\displaystyle x\mapsto gxg^{-1}}$.

For any Lie group, this natural [representation](https://en.wikipedia.org/wiki/Group_representation "Group representation") is obtained by linearizing (i.e. taking the [differential](https://en.wikipedia.org/wiki/Differential_of_a_function "Differential of a function") of) the [action](https://en.wikipedia.org/wiki/Group_action_\(mathematics\) "Group action (mathematics)") of *G* on itself by [conjugation](https://en.wikipedia.org/wiki/Conjugation_\(group_theory\) "Conjugation (group theory)"). The adjoint representation can be defined for [linear algebraic groups](https://en.wikipedia.org/wiki/Linear_algebraic_group "Linear algebraic group") over arbitrary [fields](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)").

## Definition

Let *G* be a [Lie group](https://en.wikipedia.org/wiki/Lie_group "Lie group"), and let

${\displaystyle \Psi :G\to \operatorname {Aut} (G)}$

be the mapping *g* ↦ Ψ <sub><i>g</i></sub>, with Aut(*G*) the [automorphism group](https://en.wikipedia.org/wiki/Automorphism_group "Automorphism group") of *G* and Ψ <sub><i>g</i></sub>: *G* → *G* given by the [inner automorphism](https://en.wikipedia.org/wiki/Inner_automorphism "Inner automorphism") (conjugation)

${\displaystyle \Psi _{g}(h)=ghg^{-1}~.}$

This Ψ is a group homomorphism (it is a [Lie group homomorphism](https://en.wikipedia.org/wiki/Lie_group#Homomorphisms_and_isomorphisms "Lie group") if ${\displaystyle G}$ is connected [^1]).

For each *g* in *G*, define Ad <sub><i>g</i></sub> to be the [derivative](https://en.wikipedia.org/wiki/Tangent_space "Tangent space") of Ψ <sub><i>g</i></sub> at the origin:

${\displaystyle \operatorname {Ad} _{g}=(d\Psi _{g})_{e}:T_{e}G\rightarrow T_{e}G}$

where d is the differential and ${\displaystyle {\mathfrak {g}}=T_{e}G}$ is the [tangent space](https://en.wikipedia.org/wiki/Tangent_space "Tangent space") at the origin e (e being the identity element of the group G). Since ${\displaystyle \Psi _{g}}$ is a Lie group automorphism, Ad <sub><i>g</i></sub> is a [Lie algebra automorphism](https://en.wikipedia.org/wiki/Lie_algebra_automorphism "Lie algebra automorphism"); i.e., an invertible [linear transformation](https://en.wikipedia.org/wiki/Linear_transformation "Linear transformation") of ${\displaystyle {\mathfrak {g}}}$ to itself that preserves the [Lie bracket](https://en.wikipedia.org/wiki/Lie_algebra#Definitions "Lie algebra"). Moreover, since ${\displaystyle g\mapsto \Psi _{g}}$ is a group homomorphism, ${\displaystyle g\mapsto \operatorname {Ad} _{g}}$ too is a group homomorphism.[^2] Hence, the map

${\displaystyle \mathrm {Ad} \colon G\to \mathrm {Aut} ({\mathfrak {g}}),\,g\mapsto \mathrm {Ad} _{g}}$

is a [group representation](https://en.wikipedia.org/wiki/Group_representation "Group representation") called the **adjoint representation** of *G*.

If *G* is a [linear Lie group](https://en.wikipedia.org/wiki/Lie_group#Matrix_Lie_groups "Lie group"), then the Lie algebra ${\displaystyle {\mathfrak {g}}}$ consists of matrices and the [exponential map](https://en.wikipedia.org/wiki/Exponential_map_\(Lie_theory\) "Exponential map (Lie theory)") is the matrix exponential ${\displaystyle \operatorname {exp} (X)=e^{X}}$ for matrices *X* with small operator norms. We will compute the derivative of ${\displaystyle \Psi _{g}}$ at ${\displaystyle e}$. For *g* in *G* and small *X* in ${\displaystyle {\mathfrak {g}}}$, the curve ${\displaystyle t\to \exp(tX)}$ has derivative ${\displaystyle X}$ at *t* = 0, one then gets:

${\displaystyle \operatorname {Ad} _{g}(X)=(d\Psi _{g})_{e}(X)=(\Psi _{g}\circ \exp(tX))'(0)=(g\exp(tX)g^{-1})'(0)=gXg^{-1}}$

where on the right we have the products of matrices. If ${\displaystyle G\subset \mathrm {GL} _{n}(\mathbb {C} )}$ is a closed subgroup (that is, *G* is a matrix Lie group), then this formula is valid for all *g* in *G* and all *X* in ${\displaystyle {\mathfrak {g}}}$.

Succinctly, an adjoint representation is an [isotropy representation](https://en.wikipedia.org/wiki/Isotropy_representation "Isotropy representation") associated to the conjugation action of *G* around the identity element of *G*.

### Derivative of Ad

One may always pass from a representation of a Lie group *G* to a [representation of its Lie algebra](https://en.wikipedia.org/wiki/Representation_of_a_Lie_algebra "Representation of a Lie algebra") by taking the derivative at the identity.

Taking the derivative of the adjoint map

${\displaystyle \mathrm {Ad} :G\to \mathrm {Aut} ({\mathfrak {g}})}$

at the identity element gives the **adjoint representation** of the Lie algebra ${\displaystyle {\mathfrak {g}}=\operatorname {Lie} (G)}$ of *G*:

${\displaystyle {\begin{aligned}\mathrm {ad} :&\,{\mathfrak {g}}\to \mathrm {Der} ({\mathfrak {g}})\\&\,x\mapsto \operatorname {ad} _{x}=d(\operatorname {Ad} )_{e}(x)\end{aligned}}}$

where ${\displaystyle \mathrm {Der} ({\mathfrak {g}})=\operatorname {Lie} (\operatorname {Aut} ({\mathfrak {g}}))}$ is the Lie algebra of ${\displaystyle \mathrm {Aut} ({\mathfrak {g}})}$ which may be identified with the [derivation algebra](https://en.wikipedia.org/wiki/Differential_algebra#Lie_algebra "Differential algebra") of ${\displaystyle {\mathfrak {g}}}$. One can show that

${\displaystyle \mathrm {ad} _{x}(y)=[x,y]\,}$

for all ${\displaystyle x,y\in {\mathfrak {g}}}$, where the right hand side is given (induced) by the [Lie bracket of vector fields](https://en.wikipedia.org/wiki/Lie_bracket_of_vector_fields "Lie bracket of vector fields"). Indeed,[^3] recall that, viewing ${\displaystyle {\mathfrak {g}}}$ as the Lie algebra of left-invariant vector fields on *G*, the bracket on ${\displaystyle {\mathfrak {g}}}$ is given as:[^4] for left-invariant vector fields *X*, *Y*,

${\displaystyle [X,Y]=\lim _{t\to 0}{1 \over t}(d\varphi _{-t}(Y)-Y)}$

where ${\displaystyle \varphi _{t}:G\to G}$ denotes the [flow](https://en.wikipedia.org/wiki/Flow_\(mathematics\) "Flow (mathematics)") generated by *X*. As it turns out, ${\displaystyle \varphi _{t}(g)=g\varphi _{t}(e)}$, roughly because both sides satisfy the same ODE defining the flow. That is, ${\displaystyle \varphi _{t}=R_{\varphi _{t}(e)}}$ where ${\displaystyle R_{h}}$ denotes the right multiplication by ${\displaystyle h\in G}$. On the other hand, since ${\displaystyle \Psi _{g}=R_{g^{-1}}\circ L_{g}}$, by the [chain rule](https://en.wikipedia.org/wiki/Chain_rule "Chain rule"),

${\displaystyle \operatorname {Ad} _{g}(Y)=d(R_{g^{-1}}\circ L_{g})(Y)=dR_{g^{-1}}(dL_{g}(Y))=dR_{g^{-1}}(Y)}$

as *Y* is left-invariant. Hence,

${\displaystyle [X,Y]=\lim _{t\to 0}{1 \over t}(\operatorname {Ad} _{\varphi _{t}(e)}(Y)-Y)}$,

which is what was needed to show.

Thus, ${\displaystyle \mathrm {ad} _{x}}$ coincides with the same one defined in [§ Adjoint representation of a Lie algebra](#Adjoint_representation_of_a_Lie_algebra) below. Ad and ad are related through the [exponential map](https://en.wikipedia.org/wiki/Exponential_map_\(Lie_theory\) "Exponential map (Lie theory)"): Specifically, Ad <sub>exp(<i>x</i>)</sub> = exp(ad <sub><i>x</i></sub>) for all *x* in the Lie algebra.[^5] It is a consequence of the general result relating Lie group and Lie algebra homomorphisms via the exponential map.[^6]

If *G* is a linear Lie group, then the above computation simplifies: indeed, as noted early, ${\displaystyle \operatorname {Ad} _{g}(Y)=gYg^{-1}}$ and thus with ${\displaystyle g=e^{tX}}$,

${\displaystyle \operatorname {Ad} _{e^{tX}}(Y)=e^{tX}Ye^{-tX}}$.

Taking the derivative of this at ${\displaystyle t=0}$, we have:

${\displaystyle \operatorname {ad} _{X}Y=XY-YX}$.

The general case can also be deduced from the linear case: indeed, let ${\displaystyle G'}$ be a linear Lie group having the same Lie algebra as that of *G*. Then the derivative of Ad at the identity element for *G* and that for *G'* coincide; hence, without loss of generality, *G* can be assumed to be *G'*.

The upper-case/lower-case notation is used extensively in the literature. Thus, for example, a vector x in the algebra ${\displaystyle {\mathfrak {g}}}$ generates a [vector field](https://en.wikipedia.org/wiki/Vector_field "Vector field") X in the group G. Similarly, the adjoint map ad <sub>x</sub> y = \[*x*,*y*\] of vectors in ${\displaystyle {\mathfrak {g}}}$ is homomorphic to the [Lie derivative](https://en.wikipedia.org/wiki/Lie_derivative "Lie derivative") L <sub><i>X</i></sub> *Y* = \[*X*,*Y*\] of vector fields on the group G considered as a [manifold](https://en.wikipedia.org/wiki/Manifold "Manifold").

Further see the [derivative of the exponential map](https://en.wikipedia.org/wiki/Derivative_of_the_exponential_map "Derivative of the exponential map").

## Adjoint representation of a Lie algebra

Let ${\displaystyle {\mathfrak {g}}}$ be a Lie algebra over some field. Given an element x of a Lie algebra ${\displaystyle {\mathfrak {g}}}$, one defines the adjoint action of x on ${\displaystyle {\mathfrak {g}}}$ as the map

${\displaystyle \operatorname {ad} _{x}:{\mathfrak {g}}\to {\mathfrak {g}}\qquad {\text{with}}\qquad \operatorname {ad} _{x}(y)=[x,y]}$

for all y in ${\displaystyle {\mathfrak {g}}}$. It is called the **adjoint endomorphism** or **adjoint action**. (${\displaystyle \operatorname {ad} _{x}}$ is also often denoted as ${\displaystyle \operatorname {ad} (x)}$.) Since a bracket is bilinear, this determines the [linear mapping](https://en.wikipedia.org/wiki/Linear_map "Linear map")

${\displaystyle \operatorname {ad} :{\mathfrak {g}}\to {\mathfrak {gl}}({\mathfrak {g}})=(\operatorname {End} ({\mathfrak {g}}),[\;,\;])}$

given by *x* ↦ ad <sub><i>x</i></sub>. Within End ${\displaystyle ({\mathfrak {g}})}$, the bracket is, by definition, given by the commutator of the two operators:

${\displaystyle [T,S]=T\circ S-S\circ T}$

where ${\displaystyle \circ }$ denotes composition of linear maps. Using the above definition of the bracket, the [Jacobi identity](https://en.wikipedia.org/wiki/Jacobi_identity "Jacobi identity")

${\displaystyle [x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0}$

takes the form

${\displaystyle \left([\operatorname {ad} _{x},\operatorname {ad} _{y}]\right)(z)=\left(\operatorname {ad} _{[x,y]}\right)(z)}$

where x, y, and z are arbitrary elements of ${\displaystyle {\mathfrak {g}}}$.

This last identity says that ad is a Lie algebra homomorphism; i.e., a linear mapping that takes brackets to brackets. Hence, ad is a [representation of a Lie algebra](https://en.wikipedia.org/wiki/Representation_of_a_Lie_algebra "Representation of a Lie algebra") and is called the **adjoint representation** of the algebra ${\displaystyle {\mathfrak {g}}}$.

If ${\displaystyle {\mathfrak {g}}}$ is finite-dimensional and a basis for it is chosen, then ${\displaystyle {\mathfrak {gl}}({\mathfrak {g}})}$ is the Lie algebra of square matrices and the composition corresponds to [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication "Matrix multiplication").

In a more module-theoretic language, the construction says that ${\displaystyle {\mathfrak {g}}}$ is a module over itself.

The kernel of ad is the [center](https://en.wikipedia.org/wiki/Center_\(algebra\) "Center (algebra)") of ${\displaystyle {\mathfrak {g}}}$ (that's just rephrasing the definition). On the other hand, for each element z in ${\displaystyle {\mathfrak {g}}}$, the linear mapping ${\displaystyle \delta =\operatorname {ad} _{z}}$ obeys the [Leibniz' law](https://en.wikipedia.org/wiki/General_Leibniz_rule "General Leibniz rule"):

${\displaystyle \delta ([x,y])=[\delta (x),y]+[x,\delta (y)]}$

for all x and y in the algebra (the restatement of the Jacobi identity). That is to say, ad <sub><i>z</i></sub> is a [derivation](https://en.wikipedia.org/wiki/Lie_algebra_extension#Derivations "Lie algebra extension") and the image of ${\displaystyle {\mathfrak {g}}}$ under ad is a subalgebra of Der ${\displaystyle ({\mathfrak {g}})}$, the space of all derivations of ${\displaystyle {\mathfrak {g}}}$.

When ${\displaystyle {\mathfrak {g}}=\operatorname {Lie} (G)}$ is the Lie algebra of a Lie group *G*, [ad is the differential of Ad](#Derivative_of_Ad) at the identity element of *G*.

There is the following formula similar to the [Leibniz formula](https://en.wikipedia.org/wiki/General_Leibniz_rule "General Leibniz rule"): for scalars ${\displaystyle \alpha ,\beta }$ and Lie algebra elements ${\displaystyle x,y,z}$,

${\displaystyle (\operatorname {ad} _{x}-\alpha -\beta )^{n}[y,z]=\sum _{i=0}^{n}{\binom {n}{i}}\left[(\operatorname {ad} _{x}-\alpha )^{i}y,(\operatorname {ad} _{x}-\beta )^{n-i}z\right].}$

## Structure constants

The explicit matrix elements of the adjoint representation are given by the [structure constants](https://en.wikipedia.org/wiki/Structure_constants "Structure constants") of the algebra. That is, let {e <sup>i</sup> } be a set of [basis vectors](https://en.wikipedia.org/wiki/Basis_vectors "Basis vectors") for the algebra, with

${\displaystyle [e^{i},e^{j}]=\sum _{k}{c^{ij}}_{k}e^{k}.}$

Then the matrix elements for ad <sub>e <sup>i</sup></sub> are given by

${\displaystyle {\left[\operatorname {ad} _{e^{i}}\right]_{k}}^{j}={c^{ij}}_{k}~.}$

Thus, for example, the adjoint representation of **su(2)** is the defining representation of **so(3)**.

## Examples

- If *G* is [abelian](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") of dimension *n*, the adjoint representation of *G* is the trivial *n* -dimensional representation.
- If *G* is a [matrix Lie group](https://en.wikipedia.org/wiki/Matrix_Lie_group "Matrix Lie group") (i.e. a closed subgroup of ${\displaystyle \mathrm {GL} (n,\mathbb {C} )}$), then its Lie algebra is an algebra of *n* × *n* matrices with the commutator for a Lie bracket (i.e. a subalgebra of ${\displaystyle {\mathfrak {gl}}_{n}(\mathbb {C} )}$). In this case, the adjoint map is given by Ad <sub><i>g</i></sub> (*x*) = *gxg* <sup>−1</sup>.
- If *G* is [SL(2, **R**)](https://en.wikipedia.org/wiki/SL2\(R\) "SL2(R)") (real 2×2 matrices with [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") 1), the Lie algebra of *G* consists of real 2×2 matrices with [trace](https://en.wikipedia.org/wiki/Trace_\(linear_algebra\) "Trace (linear algebra)") 0. The representation is equivalent to that given by the action of *G* by linear substitution on the space of binary (i.e., 2 variable) [quadratic forms](https://en.wikipedia.org/wiki/Quadratic_form "Quadratic form").

## Properties

The following table summarizes the properties of the various maps mentioned in the definition

| ${\displaystyle \Psi \colon G\to \operatorname {Aut} (G)\,}$ | ${\displaystyle \Psi _{g}\colon G\to G\,}$ |
| --- | --- |
| Lie group homomorphism: - ${\displaystyle \Psi _{gh}=\Psi _{g}\Psi _{h}}$ - ${\displaystyle (\Psi _{g})^{-1}=\Psi _{g^{-1}}}$ | Lie group automorphism: - ${\displaystyle \Psi _{g}(ab)=\Psi _{g}(a)\Psi _{g}(b)}$ |
| ${\displaystyle \operatorname {Ad} \colon G\to \operatorname {Aut} ({\mathfrak {g}})}$ | ${\displaystyle \operatorname {Ad} _{g}\colon {\mathfrak {g}}\to {\mathfrak {g}}}$ |
| Lie group homomorphism: - ${\displaystyle \operatorname {Ad} _{gh}=\operatorname {Ad} _{g}\operatorname {Ad} _{h}}$ - ${\displaystyle \left(\operatorname {Ad} _{g}\right)^{-1}=\operatorname {Ad} _{g^{-1}}}$ | Lie algebra automorphism: - ${\displaystyle \operatorname {Ad} _{g}}$ is linear - ${\displaystyle \operatorname {Ad} _{g}[x,y]=[\operatorname {Ad} _{g}x,\operatorname {Ad} _{g}y]}$ |
| ${\displaystyle \operatorname {ad} \colon {\mathfrak {g}}\to \operatorname {Der} ({\mathfrak {g}})}$ | ${\displaystyle \operatorname {ad} _{x}\colon {\mathfrak {g}}\to {\mathfrak {g}}}$ |
| Lie algebra homomorphism: - ${\displaystyle \operatorname {ad} }$ is linear - ${\displaystyle \operatorname {ad} _{[x,y]}=[\operatorname {ad} _{x},\operatorname {ad} _{y}]}$ | Lie algebra derivation: - ${\displaystyle \operatorname {ad} _{x}}$ is linear - ${\displaystyle \operatorname {ad} _{x}[y,z]=[\operatorname {ad} _{x}y,z]+[y,\operatorname {ad} _{x}z]}$ |

The [image](https://en.wikipedia.org/wiki/Image_\(mathematics\) "Image (mathematics)") of *G* under the adjoint representation is denoted by Ad(*G*). If *G* is [connected](https://en.wikipedia.org/wiki/Connected_space "Connected space"), the [kernel](https://en.wikipedia.org/wiki/Kernel_\(group_theory\) "Kernel (group theory)") of the adjoint representation coincides with the kernel of Ψ which is just the [center](https://en.wikipedia.org/wiki/Center_\(group_theory\) "Center (group theory)") of *G*. Therefore, the adjoint representation of a connected Lie group *G* is [faithful](https://en.wikipedia.org/wiki/Faithful_representation "Faithful representation") if and only if *G* is centerless. More generally, if *G* is not connected, then the kernel of the adjoint map is the [centralizer](https://en.wikipedia.org/wiki/Centralizer "Centralizer") of the [identity component](https://en.wikipedia.org/wiki/Identity_component "Identity component") *G* <sub>0</sub> of *G*. By the [first isomorphism theorem](https://en.wikipedia.org/wiki/First_isomorphism_theorem "First isomorphism theorem") we have

${\displaystyle \mathrm {Ad} (G)\cong G/Z_{G}(G_{0}).}$

Given a finite-dimensional real Lie algebra ${\displaystyle {\mathfrak {g}}}$, by [Lie's third theorem](https://en.wikipedia.org/wiki/Lie%27s_third_theorem "Lie's third theorem"), there is a connected Lie group ${\displaystyle \operatorname {Int} ({\mathfrak {g}})}$ whose Lie algebra is the image of the adjoint representation of ${\displaystyle {\mathfrak {g}}}$ (i.e., ${\displaystyle \operatorname {Lie} (\operatorname {Int} ({\mathfrak {g}}))=\operatorname {ad} ({\mathfrak {g}})}$.) It is called the **adjoint group** of ${\displaystyle {\mathfrak {g}}}$.

Now, if ${\displaystyle {\mathfrak {g}}}$ is the Lie algebra of a connected Lie group *G*, then ${\displaystyle \operatorname {Int} ({\mathfrak {g}})}$ is the image of the adjoint representation of *G*: ${\displaystyle \operatorname {Int} ({\mathfrak {g}})=\operatorname {Ad} (G)}$.

## Roots of a semisimple Lie group

If *G* is [semisimple](https://en.wikipedia.org/wiki/Semisimple_group "Semisimple group"), the non-zero [weights](https://en.wikipedia.org/wiki/Weight_\(representation_theory\) "Weight (representation theory)") of the adjoint representation form a [root system](https://en.wikipedia.org/wiki/Root_system "Root system").[^7] (In general, one needs to pass to the complexification of the Lie algebra before proceeding.) To see how this works, consider the case *G* = SL(*n*, **R**). We can take the group of diagonal matrices diag(*t* <sub>1</sub>,..., *t* <sub><i>n</i></sub>) as our [maximal torus](https://en.wikipedia.org/wiki/Maximal_torus "Maximal torus") *T*. Conjugation by an element of *T* sends

${\displaystyle {\begin{bmatrix}a_{11}&a_{12}&\cdots &a_{1n}\\a_{21}&a_{22}&\cdots &a_{2n}\\\vdots &\vdots &\ddots &\vdots \\a_{n1}&a_{n2}&\cdots &a_{nn}\\\end{bmatrix}}\mapsto {\begin{bmatrix}a_{11}&t_{1}t_{2}^{-1}a_{12}&\cdots &t_{1}t_{n}^{-1}a_{1n}\\t_{2}t_{1}^{-1}a_{21}&a_{22}&\cdots &t_{2}t_{n}^{-1}a_{2n}\\\vdots &\vdots &\ddots &\vdots \\t_{n}t_{1}^{-1}a_{n1}&t_{n}t_{2}^{-1}a_{n2}&\cdots &a_{nn}\\\end{bmatrix}}.}$

Thus, *T* acts trivially on the diagonal part of the Lie algebra of *G* and with eigenvectors *t* <sub><i>i</i></sub> *t* <sub><i>j</i></sub> <sup>−1</sup> on the various off-diagonal entries. The roots of *G* are the weights diag(*t* <sub>1</sub>,..., *t* <sub><i>n</i></sub>) → *t* <sub><i>i</i></sub> *t* <sub><i>j</i></sub> <sup>−1</sup>. This accounts for the standard description of the root system of *G* = SL <sub><i>n</i></sub> (**R**) as the set of vectors of the form *e <sub>i</sub>* − *e <sub>j</sub>*.

### Example SL(2, R)

When computing the root system for one of the simplest cases of Lie Groups, the group SL(2, **R**) of two dimensional matrices with determinant 1 consists of the set of matrices of the form:

${\displaystyle {\begin{bmatrix}a&b\\c&d\\\end{bmatrix}}}$

with *a*, *b*, *c*, *d* real and *ad* − *bc* = 1.

A maximal compact connected abelian Lie subgroup, or maximal torus *T*, is given by the subset of all matrices of the form

${\displaystyle {\begin{bmatrix}t_{1}&0\\0&t_{2}\\\end{bmatrix}}={\begin{bmatrix}t_{1}&0\\0&1/t_{1}\\\end{bmatrix}}={\begin{bmatrix}\exp(\theta )&0\\0&\exp(-\theta )\\\end{bmatrix}}}$

with ${\displaystyle t_{1}t_{2}=1}$. The Lie algebra of the maximal torus is the Cartan subalgebra consisting of the matrices

${\displaystyle {\begin{bmatrix}\theta &0\\0&-\theta \\\end{bmatrix}}=\theta {\begin{bmatrix}1&0\\0&0\\\end{bmatrix}}-\theta {\begin{bmatrix}0&0\\0&1\\\end{bmatrix}}=\theta (e_{1}-e_{2}).}$

If we conjugate an element of SL(2, *R*) by an element of the maximal torus we obtain

${\displaystyle {\begin{bmatrix}t_{1}&0\\0&1/t_{1}\\\end{bmatrix}}{\begin{bmatrix}a&b\\c&d\\\end{bmatrix}}{\begin{bmatrix}1/t_{1}&0\\0&t_{1}\\\end{bmatrix}}={\begin{bmatrix}at_{1}&bt_{1}\\c/t_{1}&d/t_{1}\\\end{bmatrix}}{\begin{bmatrix}1/t_{1}&0\\0&t_{1}\\\end{bmatrix}}={\begin{bmatrix}a&bt_{1}^{2}\\ct_{1}^{-2}&d\\\end{bmatrix}}}$

The matrices

${\displaystyle {\begin{bmatrix}1&0\\0&0\\\end{bmatrix}}{\begin{bmatrix}0&0\\0&1\\\end{bmatrix}}{\begin{bmatrix}0&1\\0&0\\\end{bmatrix}}{\begin{bmatrix}0&0\\1&0\\\end{bmatrix}}}$

are then 'eigenvectors' of the conjugation operation with eigenvalues ${\displaystyle 1,1,t_{1}^{2},t_{1}^{-2}}$. The function Λ which gives ${\displaystyle t_{1}^{2}}$ is a multiplicative character, or homomorphism from the group's torus to the underlying field R. The function λ giving θ is a weight of the Lie Algebra with weight space given by the span of the matrices.

It is satisfying to show the multiplicativity of the character and the linearity of the weight. It can further be proved that the differential of Λ can be used to create a weight. It is also educational to consider the case of SL(3, **R**).

## Variants and analogues

The adjoint representation can also be defined for [algebraic groups](https://en.wikipedia.org/wiki/Algebraic_group "Algebraic group") over any field.

The **[co-adjoint representation](https://en.wikipedia.org/wiki/Coadjoint_representation "Coadjoint representation")** is the [contragredient representation](https://en.wikipedia.org/wiki/Contragredient_representation "Contragredient representation") of the adjoint representation. [Alexandre Kirillov](https://en.wikipedia.org/wiki/Alexandre_Kirillov "Alexandre Kirillov") observed that the [orbit](https://en.wikipedia.org/wiki/Orbit_\(group_theory\) "Orbit (group theory)") of any vector in a co-adjoint representation is a [symplectic manifold](https://en.wikipedia.org/wiki/Symplectic_manifold "Symplectic manifold"). According to the philosophy in [representation theory](https://en.wikipedia.org/wiki/Representation_theory "Representation theory") known as the **orbit method** (see also the [Kirillov character formula](https://en.wikipedia.org/wiki/Kirillov_character_formula "Kirillov character formula")), the irreducible representations of a Lie group *G* should be indexed in some way by its co-adjoint orbits. This relationship is closest in the case of [nilpotent Lie groups](https://en.wikipedia.org/wiki/Nilpotent_Lie_group "Nilpotent Lie group").

[^1]: The "connected" is used to give a Lie group structure on the automorphism group; see [\[1\]](https://math.stackexchange.com/questions/3702700/does-the-automorphism-group-of-a-lie-group-always-have-a-lie-group-structure).

[^2]: Indeed, by the [chain rule](https://en.wikipedia.org/wiki/Chain_rule "Chain rule"), ${\displaystyle \operatorname {Ad} _{gh}=d(\Psi _{gh})_{e}=d(\Psi _{g}\circ \Psi _{h})_{e}=d(\Psi _{g})_{e}\circ d(\Psi _{h})_{e}=\operatorname {Ad} _{g}\circ \operatorname {Ad} _{h}.}$

[^3]: [Kobayashi & Nomizu 1996](#CITEREFKobayashiNomizu1996), page 41

[^4]: [Kobayashi & Nomizu 1996](#CITEREFKobayashiNomizu1996), Proposition 1.9.

[^5]: [Hall 2015](#CITEREFHall2015) Proposition 3.35

[^6]: [Hall 2015](#CITEREFHall2015) Theorem 3.28

[^7]: [Hall 2015](#CITEREFHall2015) Section 7.3