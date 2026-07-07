---
title: "Cayley transform"
source: "https://en.wikipedia.org/wiki/Cayley_transform"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2004-08-06
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **Cayley transform**, named after [Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley "Arthur Cayley"), is any of a cluster of related things. As originally described by [Cayley (1846)](#CITEREFCayley1846), the Cayley transform is a mapping between [skew-symmetric matrices](https://en.wikipedia.org/wiki/Skew-symmetric_matrix "Skew-symmetric matrix") and [special orthogonal matrices](https://en.wikipedia.org/wiki/Special_orthogonal_matrix "Special orthogonal matrix"). The transform is a [homography](https://en.wikipedia.org/wiki/Homography "Homography") used in [real analysis](https://en.wikipedia.org/wiki/Real_analysis "Real analysis"), [complex analysis](https://en.wikipedia.org/wiki/Complex_analysis "Complex analysis"), and [quaternionic analysis](https://en.wikipedia.org/wiki/Quaternionic_analysis "Quaternionic analysis"). In the theory of [Hilbert spaces](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"), the Cayley transform is a mapping between [linear operators](https://en.wikipedia.org/wiki/Linear_operator "Linear operator") ([Nikolski 1988](#CITEREFNikolski1988)).

## Real homography

A simple example of a Cayley transform can be done on the [real projective line](https://en.wikipedia.org/wiki/Real_projective_line "Real projective line"). The Cayley transform here will permute the elements of {1, 0, −1, ∞} in sequence. For example, it maps the [positive real numbers](https://en.wikipedia.org/wiki/Positive_real_numbers "Positive real numbers") to the interval \[−1, 1\]. Thus the Cayley transform is used to adapt [Legendre polynomials](https://en.wikipedia.org/wiki/Legendre_polynomials "Legendre polynomials") for use with functions on the positive real numbers with [Legendre rational functions](https://en.wikipedia.org/wiki/Legendre_rational_functions "Legendre rational functions").

As a real [homography](https://en.wikipedia.org/wiki/Homography "Homography"), points are described with [projective coordinates](https://en.wikipedia.org/wiki/Projective_coordinates "Projective coordinates"), and the mapping is

${\displaystyle [y,\ 1]=\left[{\frac {x-1}{x+1}},\ 1\right]\thicksim [x-1,\ x+1]=[x,\ 1]{\begin{pmatrix}1&1\\-1&1\end{pmatrix}}.}$

## Complex homography

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Cayley_transform_in_complex_plane.png/330px-Cayley_transform_in_complex_plane.png)

Cayley transform of upper complex half-plane to unit disk

On the [upper half](https://en.wikipedia.org/wiki/Upper_half-plane "Upper half-plane") of the [complex plane](https://en.wikipedia.org/wiki/Complex_plane "Complex plane"), the Cayley transform is:[^1] [^2]

${\displaystyle f(z)={\frac {z-i}{z+i}}.}$

Since ${\displaystyle \{\infty ,1,-1\}}$ is mapped to ${\displaystyle \{1,-i,i\}}$, and [Möbius transformations](https://en.wikipedia.org/wiki/M%C3%B6bius_transformation "Möbius transformation") permute the [generalised circles](https://en.wikipedia.org/wiki/Generalised_circle "Generalised circle") in the [complex plane](https://en.wikipedia.org/wiki/Complex_plane "Complex plane"), ${\displaystyle f}$ maps the real line to the [unit circle](https://en.wikipedia.org/wiki/Unit_circle "Unit circle"). Furthermore, since ${\displaystyle f}$ is a [homeomorphism](https://en.wikipedia.org/wiki/Homeomorphism "Homeomorphism") and ${\displaystyle i}$ is taken to 0 by ${\displaystyle f}$, the upper half-plane is mapped to the [unit disk](https://en.wikipedia.org/wiki/Unit_disk "Unit disk").

In terms of the [models](https://en.wikipedia.org/wiki/Mathematical_model "Mathematical model") of [hyperbolic geometry](https://en.wikipedia.org/wiki/Hyperbolic_geometry "Hyperbolic geometry"), this Cayley transform relates the [Poincaré half-plane model](https://en.wikipedia.org/wiki/Poincar%C3%A9_half-plane_model "Poincaré half-plane model") to the [Poincaré disk model](https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model "Poincaré disk model").

In electrical engineering the Cayley transform has been used to map a [reactance](https://en.wikipedia.org/wiki/Electrical_reactance "Electrical reactance") half-plane to the [Smith chart](https://en.wikipedia.org/wiki/Smith_chart "Smith chart") used for [impedance matching](https://en.wikipedia.org/wiki/Impedance_matching "Impedance matching") of transmission lines.

## Quaternion homography

In the [four-dimensional space](https://en.wikipedia.org/wiki/Four-dimensional_space "Four-dimensional space") of [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion") ${\displaystyle a+b{\vec {i}}+c{\vec {j}}+d{\vec {k}}}$, the [versors](https://en.wikipedia.org/wiki/Versor "Versor")

${\displaystyle u(\theta ,r)=\cos \theta +r\sin \theta }$ form the unit [3-sphere](https://en.wikipedia.org/wiki/3-sphere "3-sphere").

Since quaternions are non-commutative, elements of its [projective line](https://en.wikipedia.org/wiki/Projective_line_over_a_ring "Projective line over a ring") have homogeneous coordinates written ${\displaystyle U[a,b]}$ to indicate that the homogeneous factor multiplies on the left. The quaternion transform is

${\displaystyle f(u,q)=U[q,1]{\begin{pmatrix}1&1\\-u&u\end{pmatrix}}=U[q-u,\ q+u]\sim U[(q+u)^{-1}(q-u),\ 1].}$

The real and complex homographies described above are instances of the quaternion homography where ${\displaystyle \theta }$ is zero or ${\displaystyle \pi /2}$, respectively. Evidently the transform takes ${\displaystyle u\to 0\to -1}$ and takes ${\displaystyle -u\to \infty \to 1}$.

Evaluating this homography at ${\displaystyle q=1}$ maps the versor ${\displaystyle u}$ into its axis:

${\displaystyle f(u,1)=(1+u)^{-1}(1-u)=(1+u)^{*}(1-u)/|1+u|^{2}.}$

But ${\displaystyle |1+u|^{2}=(1+u)(1+u^{*})=2+2\cos \theta ,\quad {\text{and}}\quad (1+u^{*})(1-u)=-2r\sin \theta .}$

Thus ${\displaystyle f(u,1)=-r{\frac {\sin \theta }{1+\cos \theta }}=-r\tan {\frac {\theta }{2}}.}$

In this form the Cayley transform has been described as a rational parametrization of rotation: Let ${\displaystyle t=\tan \phi /2}$ in the complex number identity [^3]

${\displaystyle e^{-i\varphi }={\frac {1-ti}{1+ti}}}$

where the right hand side is the transform of ${\displaystyle ti}$ and the left hand side represents the rotation of the plane by negative ${\displaystyle \phi }$ radians.

### Inverse

Let ${\displaystyle u^{*}=\cos \theta -r\sin \theta =u^{-1}.}$ Since

${\displaystyle {\begin{pmatrix}1&1\\-u&u\end{pmatrix}}\ {\begin{pmatrix}1&-u^{*}\\1&u^{*}\end{pmatrix}}\ =\ {\begin{pmatrix}2&0\\0&2\end{pmatrix}}\ \sim \ {\begin{pmatrix}1&0\\0&1\end{pmatrix}}\ ,}$

where the equivalence is in the [projective linear group](https://en.wikipedia.org/wiki/Projective_linear_group "Projective linear group") over quaternions, the [inverse](https://en.wikipedia.org/wiki/Inverse_function "Inverse function") of ${\displaystyle f(u,1)}$ is

${\displaystyle U[p,1]{\begin{pmatrix}1&-u^{*}\\1&u^{*}\end{pmatrix}}\ =\ U[p+1,\ (1-p)u^{*}]\sim U[u(1-p)^{-1}(p+1),\ 1].}$

Since homographies are [bijections](https://en.wikipedia.org/wiki/Bijection "Bijection"), ${\displaystyle f^{-1}(u,1)}$ maps the vector quaternions to the 3-sphere of versors. As versors represent rotations in 3-space, the homography ${\displaystyle f^{-1}}$ produces rotations from the ball in ${\displaystyle \mathbb {R} ^{3}}$.

## Matrix map

Among *n* × *n* [square matrices](https://en.wikipedia.org/wiki/Square_matrix "Square matrix") over the [reals](https://en.wikipedia.org/wiki/Real_number "Real number"), with *I* the [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix"), let *A* be any [skew-symmetric matrix](https://en.wikipedia.org/wiki/Skew-symmetric_matrix "Skew-symmetric matrix") (so that *A* <sup>T</sup> = − *A*).

Then *I* + *A* is [invertible](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix"), and the Cayley transform

${\displaystyle Q=(I-A)(I+A)^{-1}\,\!}$

produces an [orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix "Orthogonal matrix"), *Q* (so that *Q* <sup>T</sup> *Q* = *I*). The matrix multiplication in the definition of *Q* above is commutative, so *Q* can be alternatively defined as ${\displaystyle Q=(I+A)^{-1}(I-A)}$. In fact, *Q* must have determinant +1, so is special orthogonal.

Conversely, let *Q* be any orthogonal matrix which does not have −1 as an [eigenvalue](https://en.wikipedia.org/wiki/Eigenvalue "Eigenvalue"); then

${\displaystyle A=(I-Q)(I+Q)^{-1}\,\!}$

is a skew-symmetric matrix. (See also: [Involution](https://en.wikipedia.org/wiki/Involution_\(mathematics\) "Involution (mathematics)").) The condition on *Q* automatically excludes matrices with determinant −1, but also excludes certain special orthogonal matrices.

However, any rotation (special orthogonal) matrix *Q* can be written as

${\displaystyle Q={\bigl (}(I-A)(I+A)^{-1}{\bigr )}^{2}}$

for some skew-symmetric matrix *A*; more generally any orthogonal matrix *Q* can be written as

${\displaystyle Q=E(I-A)(I+A)^{-1}}$

for some skew-symmetric matrix *A* and some diagonal matrix *E* with ±1 as entries.[^4]

A slightly different form is also seen,[^5] [^6] requiring different mappings in each direction,

${\displaystyle {\begin{aligned}Q&=(I-A)^{-1}(I+A),\\[5mu]A&=(Q-I)(Q+I)^{-1}.\end{aligned}}}$

The mappings may also be written with the order of the factors reversed;[^7] [^8] however, *A* always commutes with (μ *I* ± *A*) <sup>−1</sup>, so the reordering does not affect the definition.

### Examples

In the 2×2 case, we have

${\displaystyle {\begin{bmatrix}0&\tan {\frac {\theta }{2}}\\-\tan {\frac {\theta }{2}}&0\end{bmatrix}}\leftrightarrow {\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}.}$

The 180° [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix "Rotation matrix"), − *I*, is excluded, though it is the limit as tan <sup>θ</sup> ⁄ <sub>2</sub> goes to infinity.

In the 3×3 case, we have

${\displaystyle {\begin{bmatrix}0&z&-y\\-z&0&x\\y&-x&0\end{bmatrix}}\leftrightarrow {\frac {1}{K}}{\begin{bmatrix}w^{2}+x^{2}-y^{2}-z^{2}&2(xy-wz)&2(wy+xz)\\2(xy+wz)&w^{2}-x^{2}+y^{2}-z^{2}&2(yz-wx)\\2(xz-wy)&2(wx+yz)&w^{2}-x^{2}-y^{2}+z^{2}\end{bmatrix}},}$

where *K* = *w* <sup>2</sup> + *x* <sup>2</sup> + *y* <sup>2</sup> + *z* <sup>2</sup>, and where *w* = 1. This we recognize as the rotation matrix corresponding to [quaternion](https://en.wikipedia.org/wiki/Quaternion "Quaternion")

${\displaystyle w+\mathbf {i} x+\mathbf {j} y+\mathbf {k} z\,\!}$

(by a formula Cayley had published the year before), except scaled so that *w* = 1 instead of the usual scaling so that *w* <sup>2</sup> + *x* <sup>2</sup> + *y* <sup>2</sup> + *z* <sup>2</sup> = 1. Thus vector (*x*,*y*,*z*) is the unit axis of rotation scaled by tan <sup>θ</sup> ⁄ <sub>2</sub>. Again excluded are 180° rotations, which in this case are all *Q* which are [symmetric](https://en.wikipedia.org/wiki/Symmetric_matrix "Symmetric matrix") (so that *Q* <sup>T</sup> = *Q*).

### Other matrices

One can extend the mapping to [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number") matrices by substituting " [unitary](https://en.wikipedia.org/wiki/Unitary_matrix "Unitary matrix") " for "orthogonal" and " [skew-Hermitian](https://en.wikipedia.org/wiki/Skew-Hermitian_matrix "Skew-Hermitian matrix") " for "skew-symmetric", the difference being that the transpose (· <sup>T</sup>) is replaced by the [conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") (· <sup>H</sup>). This is consistent with replacing the standard real [inner product](https://en.wikipedia.org/wiki/Inner_product "Inner product") with the standard complex inner product. In fact, one may extend the definition further with choices of [adjoint](https://en.wikipedia.org/wiki/Hermitian_adjoint "Hermitian adjoint") other than transpose or conjugate transpose.

Formally, the definition only requires some invertibility, so one can substitute for *Q* any matrix *M* whose eigenvalues do not include −1. For example,

${\displaystyle {\begin{bmatrix}0&-a&ab-c\\0&0&-b\\0&0&0\end{bmatrix}}\leftrightarrow {\begin{bmatrix}1&2a&2c\\0&1&2b\\0&0&1\end{bmatrix}}.}$

Note that *A* is skew-symmetric (respectively, skew-Hermitian) if and only if *Q* is orthogonal (respectively, unitary) with no eigenvalue −1.

## Operator map

An infinite-dimensional version of an [inner product space](https://en.wikipedia.org/wiki/Inner_product_space "Inner product space") is a [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"), and one can no longer speak of [matrices](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)"). However, matrices are merely representations of [linear operators](https://en.wikipedia.org/wiki/Linear_operator "Linear operator"), and these can be used. So, generalizing both the matrix mapping and the complex plane mapping, one may define a Cayley transform of operators.[^9]

${\displaystyle {\begin{aligned}U&{}=(A-\mathbf {i} I)(A+\mathbf {i} I)^{-1}\\A&{}=\mathbf {i} (I+U)(I-U)^{-1}\end{aligned}}}$

[^1]: Robert Everist Green & [Steven G. Krantz](https://en.wikipedia.org/wiki/Steven_G._Krantz "Steven G. Krantz") (2006) *Function Theory of One Complex Variable*, page 189, [Graduate Studies in Mathematics](https://en.wikipedia.org/wiki/Graduate_Studies_in_Mathematics "Graduate Studies in Mathematics") #40, [American Mathematical Society](https://en.wikipedia.org/wiki/American_Mathematical_Society "American Mathematical Society") [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780821839621](https://en.wikipedia.org/wiki/Special:BookSources/9780821839621 "Special:BookSources/9780821839621")

[^2]: [Erwin Kreyszig](https://en.wikipedia.org/wiki/Erwin_Kreyszig "Erwin Kreyszig") (1983) *Advanced Engineering Mathematics*, 5th edition, page 611, Wiley [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0471862517](https://en.wikipedia.org/wiki/Special:BookSources/0471862517 "Special:BookSources/0471862517")

[^3]: See [Tangent half-angle formula](https://en.wikipedia.org/wiki/Tangent_half-angle_formula "Tangent half-angle formula")

[^4]: [Gallier, Jean](https://en.wikipedia.org/wiki/Jean_Gallier "Jean Gallier") (2006). "Remarks on the Cayley Representation of Orthogonal Matrices and on Perturbing the Diagonal of a Matrix to Make it Invertible". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0606320](https://arxiv.org/abs/math/0606320). As described by Gallier, the first of these results is a sharpened variant of [Weyl, Hermann](https://en.wikipedia.org/wiki/Hermann_Weyl "Hermann Weyl") (1946). *The Classical Groups* (2nd ed.). Princeton University Press. Lemma 2.10.D, p. 60.

The second appeared as an exercise in Bellman, Richard (1960). *Introduction to Matrix Analysis*. SIAM Publications. §6.4 exercise 11, p. 91–92.

[^5]: [Golub, Gene H.](https://en.wikipedia.org/wiki/Gene_H._Golub "Gene H. Golub"); [Van Loan, Charles F.](https://en.wikipedia.org/wiki/Charles_F._Van_Loan "Charles F. Van Loan") (1996), *Matrix Computations* (3rd ed.), [Johns Hopkins University Press](https://en.wikipedia.org/wiki/Johns_Hopkins_University_Press "Johns Hopkins University Press"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8018-5414-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8018-5414-9 "Special:BookSources/978-0-8018-5414-9")

[^6]: F. Chong (1971) "A Geometric Note on the Cayley Transform", pages 84,5 in *A Spectrum of Mathematics: Essays Presented to H. G. Forder*, [John C. Butcher](https://en.wikipedia.org/wiki/John_C._Butcher "John C. Butcher") editor, [Auckland University Press](https://en.wikipedia.org/wiki/Auckland_University_Press "Auckland University Press")

[^7]: [Courant, Richard](https://en.wikipedia.org/wiki/Richard_Courant "Richard Courant"); [Hilbert, David](https://en.wikipedia.org/wiki/David_Hilbert "David Hilbert") (1989), *Methods of Mathematical Physics*, vol. 1 (1st English ed.), New York: Wiley-Interscience, pp. 536, 7, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-471-50447-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-471-50447-4 "Special:BookSources/978-0-471-50447-4") Ch.VII, §7.2

[^8]: [Howard Eves](https://en.wikipedia.org/wiki/Howard_Eves "Howard Eves") (1966) *Elementary Matrix Theory*, § 5.4A Cayley’s Construction of Real Orthogonal Matrices, pages 365–7, [Allyn & Bacon](https://en.wikipedia.org/wiki/Allyn_%26_Bacon "Allyn & Bacon")

[^9]: [Rudin 1991](#CITEREFRudin1991), p. 356-357 §13.17.