---
title: "Eigenvalue algorithm"
source: "https://en.wikipedia.org/wiki/Eigenvalue_algorithm"
author:
  - "[[Wikipedia]]"
published: 2004-03-09
created: 2026-05-16
description:
tags:
  - "clippings"
---
In [numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis "Numerical analysis"), one of the most important problems is designing efficient and [stable](https://en.wikipedia.org/wiki/Numerical_stability "Numerical stability") [algorithms](https://en.wikipedia.org/wiki/Algorithm "Algorithm") for finding the [eigenvalues](https://en.wikipedia.org/wiki/Eigenvalue "Eigenvalue") of a [matrix](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)"). These **eigenvalue algorithms** may also find eigenvectors.

## Eigenvalues and eigenvectors

Given an *n* × *n* [square matrix](https://en.wikipedia.org/wiki/Square_matrix#Square_matrices "Square matrix") *A* of [real](https://en.wikipedia.org/wiki/Real_number "Real number") or [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number") numbers, an *λ* and its associated *[generalized eigenvector](https://en.wikipedia.org/wiki/Generalized_eigenvector "Generalized eigenvector")* **v** are a pair obeying the relation [^4]

${\displaystyle \left(A-\lambda I\right)^{k}{\mathbf {v} }=0,}$

where **v** is a nonzero *n* × 1 column vector, *I* is the *n* × *n* [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix"), *k* is a positive integer, and both *λ* and **v** are allowed to be complex even when *A* is real. When *k* = 1, the vector is called simply an *[eigenvector](https://en.wikipedia.org/wiki/Eigenvector "Eigenvector")*, and the pair is called an *eigenpair*. In this case, *A* **v** = *λ* **v**. Any eigenvalue *λ* of *A* has ordinary [^1] eigenvectors associated to it, for if *k* is the smallest integer such that (*A* − *λI*) <sup><i>k</i></sup> **v** = 0 for a generalized eigenvector **v**, then (*A* − *λI*) <sup><i>k</i> −1</sup> **v** is an ordinary eigenvector. The value *k* can always be taken as less than or equal to *n*. In particular, (*A* − *λI*) <sup><i>n</i></sup> **v** = 0 for all generalized eigenvectors **v** associated with *λ*.

For each eigenvalue λ of *A*, the [kernel](https://en.wikipedia.org/wiki/Kernel_\(matrix\) "Kernel (matrix)") ker(*A* − *λI*) consists of all eigenvectors associated with *λ* (along with 0), called the *[eigenspace](https://en.wikipedia.org/wiki/Eigenspace "Eigenspace")* of *λ*, while the vector space ker((*A* − *λI*) <sup><i>n</i></sup>) consists of all generalized eigenvectors, and is called the *[generalized eigenspace](https://en.wikipedia.org/wiki/Generalized_eigenspace "Generalized eigenspace")*. The *[geometric multiplicity](https://en.wikipedia.org/wiki/Geometric_multiplicity "Geometric multiplicity")* of *λ* is the dimension of its eigenspace. The *[algebraic multiplicity](https://en.wikipedia.org/wiki/Algebraic_multiplicity "Algebraic multiplicity")* of *λ* is the dimension of its generalized eigenspace. The latter terminology is justified by the equation

${\displaystyle p_{A}\left(z\right)=\det \left(zI-A\right)=\prod _{i=1}^{k}(z-\lambda _{i})^{\alpha _{i}},}$

where det is the [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") function, the *λ* <sub><i>i</i></sub> are all the distinct eigenvalues of *A* and the *α* <sub><i>i</i></sub> are the corresponding algebraic multiplicities. The function *p <sub>A</sub>* (*z*) is the *[characteristic polynomial](https://en.wikipedia.org/wiki/Characteristic_polynomial "Characteristic polynomial")* of *A*. So the algebraic multiplicity is the multiplicity of the eigenvalue as a [zero](https://en.wikipedia.org/wiki/Properties_of_polynomial_roots "Properties of polynomial roots") of the characteristic polynomial. Since any eigenvector is also a generalized eigenvector, the geometric multiplicity is less than or equal to the algebraic multiplicity. The algebraic multiplicities sum up to *n*, the degree of the characteristic polynomial. The equation *p <sub>A</sub>* (*z*) = 0 is called the *characteristic equation*, as its roots are exactly the eigenvalues of *A*. By the [Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem "Cayley–Hamilton theorem"), *A* itself obeys the same equation: *p <sub>A</sub>* (*A*) = 0.[^2] As a consequence, the columns of the matrix ${\textstyle \prod _{i\neq j}(A-\lambda _{i}I)^{\alpha _{i}}}$ must be either 0 or generalized eigenvectors of the eigenvalue *λ* <sub><i>j</i></sub>, since they are annihilated by ${\displaystyle (A-\lambda _{j}I)^{\alpha _{j}}}$. In fact, the [column space](https://en.wikipedia.org/wiki/Column_space "Column space") is the generalized eigenspace of *λ* <sub><i>j</i></sub>.

Any collection of generalized eigenvectors of distinct eigenvalues is linearly independent, so a basis for all of **C** <sup><i>n</i></sup> can be chosen consisting of generalized eigenvectors. More particularly, this basis { **v** <sub><i>i</i></sub> } <sup><i>n</i></sup>  
<sub><i>i</i> =1</sub> can be chosen and organized so that

- if **v** <sub><i>i</i></sub> and **v** <sub><i>j</i></sub> have the same eigenvalue, then so does **v** <sub><i>k</i></sub> for each *k* between *i* and *j*, and
- if **v** <sub><i>i</i></sub> is not an ordinary eigenvector, and if *λ* <sub><i>i</i></sub> is its eigenvalue, then (*A* − *λ* <sub><i>i</i></sub> *I*) **v** <sub><i>i</i></sub> = **v** <sub><i>i</i> −1</sub> (in particular, **v** <sub>1</sub> must be an ordinary eigenvector).

If these basis vectors are placed as the column vectors of a matrix *V* = \[**v** <sub>1</sub> **v** <sub>2</sub> ⋯ **v** <sub><i>n</i></sub>\], then *V* can be used to convert *A* to its [Jordan normal form](https://en.wikipedia.org/wiki/Jordan_normal_form "Jordan normal form"):

${\displaystyle V^{-1}AV={\begin{bmatrix}\lambda _{1}&\beta _{1}&0&\ldots &0\\0&\lambda _{2}&\beta _{2}&\ldots &0\\0&0&\lambda _{3}&\ldots &0\\\vdots &\vdots &\vdots &\ddots &\vdots \\0&0&0&\ldots &\lambda _{n}\end{bmatrix}},}$

where the *λ* <sub><i>i</i></sub> are the eigenvalues, *β* <sub><i>i</i></sub> = 1 if (*A* − *λ* <sub><i>i</i> +1</sub>) **v** <sub><i>i</i> +1</sub> = **v** <sub><i>i</i></sub> and *β* <sub><i>i</i></sub> = 0 otherwise.

More generally, if *W* is any [invertible matrix](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix"), and *λ* is an eigenvalue of *A* with generalized eigenvector **v**, then (*W* <sup>−1</sup> *AW* − *λI*) <sup><i>k</i></sup> *W* <sup>− <i>k</i></sup> **v** = 0. Thus *λ* is an eigenvalue of *W* <sup>−1</sup> *AW* with generalized eigenvector *W* <sup>− <i>k</i></sup> **v**. That is, [similar matrices](https://en.wikipedia.org/wiki/Similar_matrices "Similar matrices") have the same eigenvalues.

### Normal, Hermitian, and real-symmetric matrices

The [adjoint](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") *M* <sup>*</sup> of a complex matrix *M* is the transpose of the conjugate of *M*: *M* <sup>*</sup> = *M* <sup>T</sup>. A square matrix *A* is called *[normal](https://en.wikipedia.org/wiki/Normal_matrix "Normal matrix")* if it commutes with its adjoint: *A* <sup>*</sup> *A* = *AA* <sup>*</sup>. It is called *[Hermitian](https://en.wikipedia.org/wiki/Hermitian_matrix "Hermitian matrix")* if it is equal to its adjoint: *A* <sup>*</sup> = *A*. All Hermitian matrices are normal. If *A* has only real elements, then the adjoint is just the transpose, and *A* is Hermitian [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") it is [symmetric](https://en.wikipedia.org/wiki/Symmetric_matrix "Symmetric matrix"). When applied to column vectors, the adjoint can be used to define the canonical inner product on **C** <sup><i>n</i></sup>: **w** ⋅ **v** = **w** <sup>*</sup> **v**.[^3] Normal, Hermitian, and real-symmetric matrices have several useful properties:

- Every generalized eigenvector of a normal matrix is an ordinary eigenvector.
- Any normal matrix is similar to a diagonal matrix, since its Jordan normal form is diagonal.
- Eigenvectors of distinct eigenvalues of a normal matrix are orthogonal.
- The null space and the image (or column space) of a normal matrix are orthogonal to each other.
- For any normal matrix *A*, **C** <sup><i>n</i></sup> has an orthonormal basis consisting of eigenvectors of *A*. The corresponding matrix of eigenvectors is [unitary](https://en.wikipedia.org/wiki/Unitary_matrix "Unitary matrix").
- The eigenvalues of a Hermitian matrix are real, since (*λ* − *λ*) **v** = (*A* <sup>*</sup> − *A*) **v** = (*A* − *A*) **v** = 0 for a non-zero eigenvector **v**.
- If *A* is real, there is an orthonormal basis for **R** <sup><i>n</i></sup> consisting of eigenvectors of *A* if and only if *A* is symmetric.

It is possible for a real or complex matrix to have all real eigenvalues without being Hermitian. For example, a real [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix "Triangular matrix") has its eigenvalues along its diagonal, but in general is not symmetric.

## Condition number

Any problem of numeric calculation can be viewed as the evaluation of some function *f* for some input *x*. The [condition number](https://en.wikipedia.org/wiki/Condition_number "Condition number") *κ* (*f*, *x*) of the problem is the ratio of the relative error in the function's output to the relative error in the input, and varies with both the function and the input. The condition number describes how error grows during the calculation. Its base-10 logarithm tells how many fewer digits of accuracy exist in the result than existed in the input. The condition number is a best-case scenario. It reflects the instability built into the problem, regardless of how it is solved. No algorithm can ever produce more accurate results than indicated by the condition number, except by chance. However, a poorly designed algorithm may produce significantly worse results. For example, as mentioned below, the problem of finding eigenvalues for normal matrices is always well-conditioned. However, the problem of finding the roots of a polynomial can be [very ill-conditioned](https://en.wikipedia.org/wiki/Wilkinson%27s_polynomial "Wilkinson's polynomial"). Thus eigenvalue algorithms that work by finding the roots of the characteristic polynomial can be ill-conditioned even when the problem is not.

For the problem of solving the linear equation *A* **v** = **b** where *A* is invertible, the [matrix condition number](https://en.wikipedia.org/wiki/Condition_number#Matrices "Condition number") *κ* (*A* <sup>−1</sup>, **b**) is given by || *A* || <sub>op</sub> || *A* <sup>−1</sup> || <sub>op</sub>, where || || <sub>op</sub> is the [operator norm](https://en.wikipedia.org/wiki/Operator_norm "Operator norm") subordinate to the normal [Euclidean norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\)#Euclidean_norm "Norm (mathematics)") on **C** <sup><i>n</i></sup>. Since this number is independent of **b** and is the same for *A* and *A* <sup>−1</sup>, it is usually just called the condition number *κ* (*A*) of the matrix *A*. This value *κ* (*A*) is also the absolute value of the ratio of the largest [singular value](https://en.wikipedia.org/wiki/Singular_value "Singular value") of *A* to its smallest. If *A* is [unitary](https://en.wikipedia.org/wiki/Unitary_matrix "Unitary matrix"), then || *A* || <sub>op</sub> = || *A* <sup>−1</sup> || <sub>op</sub> = 1, so *κ* (*A*) = 1. For general matrices, the operator norm is often difficult to calculate. For this reason, other [matrix norms](https://en.wikipedia.org/wiki/Matrix_norms "Matrix norms") are commonly used to estimate the condition number.

For the eigenvalue problem, [Bauer and Fike proved](https://en.wikipedia.org/wiki/Bauer%E2%80%93Fike_theorem "Bauer–Fike theorem") that if *λ* is an eigenvalue for a [diagonalizable](https://en.wikipedia.org/wiki/Diagonalizable_matrix "Diagonalizable matrix") *n* × *n* matrix *A* with [eigenvector matrix](https://en.wikipedia.org/wiki/Eigenvector_matrix "Eigenvector matrix") *V*, then the absolute error in calculating *λ* is bounded by the product of *κ* (*V*) and the absolute error in *A*.[^5] [As a result](https://en.wikipedia.org/wiki/Bauer-Fike_theorem#Corollary "Bauer-Fike theorem"), the condition number for finding *λ* is *κ* (*λ*, *A*) = *κ* (*V*) = || *V* || <sub>op</sub> || *V* <sup>−1</sup> || <sub>op</sub>. If *A* is normal, then *V* is unitary, and *κ* (*λ*, *A*) = 1. Thus the eigenvalue problem for all normal matrices is well-conditioned.

The condition number for the problem of finding the eigenspace of a normal matrix *A* corresponding to an eigenvalue *λ* has been shown to be inversely proportional to the minimum distance between *λ* and the other distinct eigenvalues of *A*.[^6] In particular, the eigenspace problem for normal matrices is well-conditioned for isolated eigenvalues. When eigenvalues are not isolated, the best that can be hoped for is to identify the span of all eigenvectors of nearby eigenvalues.

## Algorithms

The most reliable and most widely used algorithm for computing eigenvalues is [John G. F. Francis](https://en.wikipedia.org/wiki/John_G._F._Francis "John G. F. Francis") ' and [Vera N. Kublanovskaya](https://en.wikipedia.org/wiki/Vera_N._Kublanovskaya "Vera N. Kublanovskaya") 's [QR algorithm](https://en.wikipedia.org/wiki/QR_algorithm "QR algorithm"), considered one of the top ten algorithms of 20th century.[^7]

Any monic polynomial is the characteristic polynomial of its [companion matrix](https://en.wikipedia.org/wiki/Companion_matrix "Companion matrix"). Therefore, a general algorithm for finding eigenvalues could also be used to find the roots of polynomials. The [Abel–Ruffini theorem](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem "Abel–Ruffini theorem") shows that any such algorithm for dimensions greater than 4 must either be infinite, or involve functions of greater complexity than elementary arithmetic operations and fractional powers. For this reason algorithms that exactly calculate eigenvalues in a finite number of steps only exist for a few special classes of matrices. For general matrices, algorithms are [iterative](https://en.wikipedia.org/wiki/Iterative_method "Iterative method"), producing better approximate solutions with each iteration.

Some algorithms produce every eigenvalue, others will produce a few, or only one. However, even the latter algorithms can be used to find all eigenvalues. Once an eigenvalue *λ* of a matrix *A* has been identified, it can be used to either direct the algorithm towards a different solution next time, or to reduce the problem to one that no longer has *λ* as a solution.

Redirection is usually accomplished by shifting: replacing *A* with *A* − *μI* for some constant *μ*. The eigenvalue found for *A* − *μI* must have *μ* added back in to get an eigenvalue for *A*. For example, for [power iteration](https://en.wikipedia.org/wiki/Power_iteration "Power iteration"), *μ* = *λ*. Power iteration finds the largest eigenvalue in absolute value, so even when *λ* is only an approximate eigenvalue, power iteration is unlikely to find it a second time. Conversely, [inverse iteration](https://en.wikipedia.org/wiki/Inverse_iteration "Inverse iteration") based methods find the lowest eigenvalue, so *μ* is chosen well away from *λ* and hopefully closer to some other eigenvalue.

Reduction can be accomplished by restricting *A* to the column space of the matrix *A* − *λI*, which *A* carries to itself. Since *A* - *λI* is singular, the column space is of lesser dimension. The eigenvalue algorithm can then be applied to the restricted matrix. This process can be repeated until all eigenvalues are found.

If an eigenvalue algorithm does not produce eigenvectors, a common practice is to use an inverse iteration based algorithm with *μ* set to a close approximation to the eigenvalue. This will quickly converge to the eigenvector of the closest eigenvalue to *μ*. For small matrices, an alternative is to look at the column space of the product of *A* − *λ* ' *I* for each of the other eigenvalues *λ* '.

A formula for the norm of unit eigenvector components of normal matrices was discovered by Robert Thompson in 1966 and rediscovered independently by several others.[^8] [^9] [^10] [^11] [^12] If *A* is an ${\textstyle n\times n}$ normal matrix with eigenvalues *λ* <sub><i>i</i></sub> (*A*) and corresponding unit eigenvectors **v** <sub><i>i</i></sub> whose component entries are *v* <sub><i>i,j</i></sub>, let *A* <sub><i>j</i></sub> be the ${\textstyle n-1\times n-1}$ matrix obtained by removing the *i* -th row and column from *A*, and let *λ* <sub><i>k</i></sub> (*A* <sub><i>j</i></sub>) be its *k* -th eigenvalue. Then 
$$
{\displaystyle |v_{i,j}|^{2}\prod _{k=1,k\neq i}^{n}(\lambda _{i}(A)-\lambda _{k}(A))=\prod _{k=1}^{n-1}(\lambda _{i}(A)-\lambda _{k}(A_{j}))}
$$

If ${\displaystyle p,p_{j}}$ are the characteristic polynomials of ${\displaystyle A}$ and ${\displaystyle A_{j}}$, the formula can be re-written as 
$$
{\displaystyle |v_{i,j}|^{2}={\frac {p_{j}(\lambda _{i}(A))}{p'(\lambda _{i}(A))}}}
$$
 assuming the derivative ${\displaystyle p'}$ is not zero at ${\displaystyle \lambda _{i}(A)}$.

## Hessenberg and tridiagonal matrices

Because the eigenvalues of a triangular matrix are its diagonal elements, for general matrices there is no finite method like [gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination "Gaussian elimination") to convert a matrix to triangular form while preserving eigenvalues. But it is possible to reach something close to triangular. An [upper Hessenberg matrix](https://en.wikipedia.org/wiki/Hessenberg_matrix "Hessenberg matrix") is a square matrix for which all entries below the [subdiagonal](https://en.wikipedia.org/wiki/Subdiagonal "Subdiagonal") are zero. A lower Hessenberg matrix is one for which all entries above the [superdiagonal](https://en.wikipedia.org/wiki/Superdiagonal "Superdiagonal") are zero. Matrices that are both upper and lower Hessenberg are [tridiagonal](https://en.wikipedia.org/wiki/Tridiagonal_matrix "Tridiagonal matrix"). Hessenberg and tridiagonal matrices are the starting points for many eigenvalue algorithms because the zero entries reduce the complexity of the problem. Several methods are commonly used to convert a general matrix into a Hessenberg matrix with the same eigenvalues. If the original matrix was symmetric or Hermitian, then the resulting matrix will be tridiagonal.

When only eigenvalues are needed, there is no need to calculate the similarity matrix, as the transformed matrix has the same eigenvalues. If eigenvectors are needed as well, the similarity matrix may be needed to transform the eigenvectors of the Hessenberg matrix back into eigenvectors of the original matrix.

| Method | Applies to | Produces | Cost without similarity matrix | Cost with similarity matrix | Description |
| --- | --- | --- | --- | --- | --- |
| [Householder transformations](https://en.wikipedia.org/wiki/Householder_transformation "Householder transformation") | General | Hessenberg | 2 *n* <sup>3</sup> ⁄3 + *O* (*n* <sup>2</sup>) [^13]<sup><span title="Page: 474">: 474</span></sup> | 4 *n* <sup>3</sup> ⁄3 + *O* (*n* <sup>2</sup>) [^13]<sup><span title="Page: 474">: 474</span></sup> | Reflect each column through a subspace to zero out its lower entries. |
| [Givens rotations](https://en.wikipedia.org/wiki/Givens_rotation "Givens rotation") | General | Hessenberg | 4 *n* <sup>3</sup> ⁄3 + *O* (*n* <sup>2</sup>) [^13]<sup><span title="Page: 470">: 470</span></sup> |  | Apply planar rotations to zero out individual entries. Rotations are ordered so that later ones do not cause zero entries to become non-zero again. |
| [Arnoldi iteration](https://en.wikipedia.org/wiki/Arnoldi_iteration "Arnoldi iteration") | General | Hessenberg |  |  | Perform Gram–Schmidt orthogonalization on Krylov subspaces. |
| [Lanczos algorithm](https://en.wikipedia.org/wiki/Lanczos_algorithm "Lanczos algorithm") | Hermitian | Tridiagonal |  |  | Arnoldi iteration for Hermitian matrices, with shortcuts. |

For symmetric tridiagonal eigenvalue problems all eigenvalues (without eigenvectors) can be computed numerically in time O(n log(n)), using bisection on the characteristic polynomial.[^14]

## Iterative algorithms

Iterative algorithms solve the eigenvalue problem by producing sequences that converge to the eigenvalues. Some algorithms also produce sequences of vectors that converge to the eigenvectors. Most commonly, the eigenvalue sequences are expressed as sequences of similar matrices which converge to a triangular or diagonal form, allowing the eigenvalues to be read easily. The eigenvector sequences are expressed as the corresponding similarity matrices.

<table><tbody><tr><th>Method</th><th>Applies to</th><th>Produces</th><th>Cost per step</th><th>Convergence</th><th>Description</th></tr><tr><td><a href="https://en.wikipedia.org/wiki/Lanczos_algorithm">Lanczos algorithm</a></td><td>Hermitian</td><td><i>m</i> largest/smallest eigenpairs</td><td></td><td></td><td align="left"></td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Power_iteration">Power iteration</a></td><td>general</td><td>eigenpair with largest value</td><td><i>O</i> (<i>n</i> <sup>2</sup>)</td><td>linear</td><td align="left">Repeatedly applies the matrix to an arbitrary starting vector and renormalizes.</td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Inverse_iteration">Inverse iteration</a></td><td>general</td><td>eigenpair with value closest to <i>μ</i></td><td></td><td>linear</td><td align="left">Power iteration for (<i>A</i> − <i>μI</i>) <sup>−1</sup></td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration">Rayleigh quotient iteration</a></td><td>Hermitian</td><td>any eigenpair</td><td></td><td>cubic</td><td align="left">Power iteration for (<i>A</i> − <i>μ</i> <sub><i>i</i></sub> <i>I</i>) <sup>−1</sup>, where <i>μ</i> <sub><i>i</i></sub> for each iteration is the Rayleigh quotient of the previous iteration.</td></tr><tr><td width="200"><a href="https://en.wikipedia.org/w/index.php?title=Preconditioned_inverse_iteration&action=edit&redlink=1">Preconditioned inverse iteration</a> <sup><a href="#fn:15">15</a></sup> or <a href="https://en.wikipedia.org/wiki/LOBPCG">LOBPCG algorithm</a></td><td><a href="https://en.wikipedia.org/wiki/Positive-definite_matrix">positive-definite</a> real symmetric</td><td>eigenpair with value closest to <i>μ</i></td><td></td><td></td><td align="left">Inverse iteration using a <a href="https://en.wikipedia.org/wiki/Preconditioner">preconditioner</a> (an approximate inverse to <i>A</i>).</td></tr><tr><td><a href="https://en.wikipedia.org/w/index.php?title=Bisection_eigenvalue_algorithm&action=edit&redlink=1">Bisection method</a></td><td>real symmetric tridiagonal</td><td>any eigenvalue</td><td></td><td>linear</td><td align="left">Uses the <a href="https://en.wikipedia.org/wiki/Bisection_method">bisection method</a> to find roots of the characteristic polynomial, supported by the Sturm sequence.</td></tr><tr><td><a href="https://en.wikipedia.org/w/index.php?title=Laguerre_iteration&action=edit&redlink=1">Laguerre iteration</a></td><td>real symmetric tridiagonal</td><td>any eigenvalue</td><td></td><td>cubic <sup><a href="#fn:16">16</a></sup></td><td align="left">Uses <a href="https://en.wikipedia.org/wiki/Laguerre%27s_method">Laguerre's method</a> to find roots of the characteristic polynomial, supported by the Sturm sequence.</td></tr><tr><td rowspan="2"><a href="https://en.wikipedia.org/wiki/QR_algorithm">QR algorithm</a></td><td rowspan="2">Hessenberg</td><td>all eigenvalues</td><td><i>O</i> (<i>n</i> <sup>2</sup>)</td><td rowspan="2">cubic</td><td align="left" rowspan="2">Factors <i>A</i> = <i>QR</i>, where <i>Q</i> is orthogonal and <i>R</i> is triangular, then applies the next iteration to <i>RQ</i>.</td></tr><tr><td>all eigenpairs</td><td>6 <i>n</i> <sup>3</sup> + <i>O</i> (<i>n</i> <sup>2</sup>)</td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm">Jacobi eigenvalue algorithm</a></td><td>real symmetric</td><td>all eigenvalues</td><td><i>O</i> (<i>n</i> <sup>3</sup>)</td><td>quadratic</td><td align="left">Uses Givens rotations to attempt clearing all off-diagonal entries. This fails, but strengthens the diagonal.</td></tr><tr><td rowspan="2"><a href="https://en.wikipedia.org/wiki/Divide-and-conquer_eigenvalue_algorithm">Divide-and-conquer</a></td><td rowspan="2">Hermitian tridiagonal</td><td>all eigenvalues</td><td><i>O</i> (<i>n</i> <sup>2</sup>)</td><td rowspan="2"></td><td align="left" rowspan="2">Divides the matrix into submatrices that are diagonalized then recombined.</td></tr><tr><td>all eigenpairs</td><td>(4⁄3) <i>n</i> <sup>3</sup> + <i>O</i> (<i>n</i> <sup>2</sup>)</td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Homotopy_method">Homotopy method</a></td><td>real symmetric tridiagonal</td><td>all eigenpairs</td><td><i>O</i> (<i>n</i> <sup>2</sup>) <sup><a href="#fn:17">17</a></sup></td><td></td><td align="left">Constructs a computable homotopy path from a diagonal eigenvalue problem.</td></tr><tr><td><a href="https://en.wikipedia.org/wiki/Folded_spectrum_method">Folded spectrum method</a></td><td>real symmetric</td><td>eigenpair with value closest to <i>μ</i></td><td></td><td></td><td align="left">Preconditioned inverse iteration applied to (<i>A</i> − <i>μI</i>) <sup>2</sup></td></tr><tr><td><a href="https://en.wikipedia.org/w/index.php?title=MRRR_algorithm&action=edit&redlink=1">MRRR algorithm</a> <sup><a href="#fn:18">18</a></sup></td><td>real symmetric tridiagonal</td><td>some or all eigenpairs</td><td><i>O</i> (<i>n</i> <sup>2</sup>)</td><td></td><td align="left">"Multiple relatively robust representations" – performs inverse iteration on a <a href="https://en.wikipedia.org/wiki/Cholesky_decomposition"><i>LDL</i> <sup>T</sup> decomposition</a> of the shifted matrix.</td></tr><tr><td><a href="https://en.wikipedia.org/w/index.php?title=Gram_iteration&action=edit&redlink=1">Gram iteration</a> <sup><a href="#fn:19">19</a></sup></td><td>general</td><td>Eigenpair with largest eigenvalue</td><td></td><td>super-linear</td><td align="left">Repeatedly computes the Gram product and rescales, deterministically.</td></tr></tbody></table>

## Direct calculation

While there is no simple algorithm to directly calculate eigenvalues for general matrices, there are numerous special classes of matrices where eigenvalues can be directly calculated. These include:

### Triangular matrices

Since the determinant of a [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix "Triangular matrix") is the product of its diagonal entries, if *T* is triangular, then ${\textstyle \det(\lambda I-T)=\prod _{i}(\lambda -T_{ii})}$. Thus the eigenvalues of *T* are its diagonal entries.

### Factorable polynomial equations

If *p* is any polynomial and *p* (*A*) = 0, then the eigenvalues of *A* also satisfy the same equation. If *p* happens to have a known factorization, then the eigenvalues of *A* lie among its roots.

For example, a [projection](https://en.wikipedia.org/wiki/Projection_\(linear_algebra\) "Projection (linear algebra)") is a square matrix *P* satisfying *P* <sup>2</sup> = *P*. The roots of the corresponding scalar polynomial equation, *λ* <sup>2</sup> = *λ*, are 0 and 1. Thus any projection has 0 and 1 for its eigenvalues. The multiplicity of 0 as an eigenvalue is the [nullity](https://en.wikipedia.org/wiki/Kernel_\(linear_algebra\)#Representation_as_matrix_multiplication "Kernel (linear algebra)") of *P*, while the multiplicity of 1 is the rank of *P*.

Another example is a matrix *A* that satisfies *A* <sup>2</sup> = *α* <sup>2</sup> *I* for some scalar *α*. The eigenvalues must be ± *α*. The projection operators

${\displaystyle P_{+}={\frac {1}{2}}\left(I+{\frac {A}{\alpha }}\right)}$

${\displaystyle P_{-}={\frac {1}{2}}\left(I-{\frac {A}{\alpha }}\right)}$

satisfy

${\displaystyle AP_{+}=\alpha P_{+}\quad AP_{-}=-\alpha P_{-}}$

and

${\displaystyle P_{+}P_{+}=P_{+}\quad P_{-}P_{-}=P_{-}\quad P_{+}P_{-}=P_{-}P_{+}=0.}$

The [column spaces](https://en.wikipedia.org/wiki/Column_space "Column space") of *P* <sub>+</sub> and *P* <sub>−</sub> are the eigenspaces of *A* corresponding to + *α* and − *α*, respectively.

### 2×2 matrices

For dimensions 2 through 4, formulas involving radicals exist that can be used to find the eigenvalues. While a common practice for 2×2 and 3×3 matrices, for 4×4 matrices the increasing complexity of the [root formulas](https://en.wikipedia.org/wiki/Quartic_function#Ferrari's_solution "Quartic function") makes this approach less attractive.

For the 2×2 matrix

${\displaystyle A={\begin{bmatrix}a&b\\c&d\end{bmatrix}},}$

the characteristic polynomial is

${\displaystyle \det {\begin{bmatrix}\lambda -a&-b\\-c&\lambda -d\end{bmatrix}}=\lambda ^{2}\,-\,\left(a+d\right)\lambda \,+\,\left(ad-bc\right)=\lambda ^{2}\,-\,\lambda \,{\rm {tr}}(A)\,+\,\det(A).}$

Thus the eigenvalues can be found by using the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula "Quadratic formula"):

${\displaystyle \lambda ={\frac {{\rm {tr}}(A)\pm {\sqrt {{\rm {tr}}^{2}(A)-4\det(A)}}}{2}}.}$

Defining ${\textstyle {\rm {gap}}\left(A\right)={\sqrt {{\rm {tr}}^{2}(A)-4\det(A)}}}$ to be the distance between the two eigenvalues, it is straightforward to calculate

${\displaystyle {\frac {\partial \lambda }{\partial a}}={\frac {1}{2}}\left(1\pm {\frac {a-d}{{\rm {gap}}(A)}}\right),\qquad {\frac {\partial \lambda }{\partial b}}={\frac {\pm c}{{\rm {gap}}(A)}}}$

with similar formulas for *c* and *d*. From this it follows that the calculation is well-conditioned if the eigenvalues are isolated.

Eigenvectors can be found by exploiting the [Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem "Cayley–Hamilton theorem"). If *λ* <sub>1</sub>, *λ* <sub>2</sub> are the eigenvalues, then (*A* − *λ* <sub>1</sub> *I*)(*A* − *λ* <sub>2</sub> *I*) = (*A* − *λ* <sub>2</sub> *I*)(*A* − *λ* <sub>1</sub> *I*) = 0, so the columns of (*A* − *λ* <sub>2</sub> *I*) are annihilated by (*A* − *λ* <sub>1</sub> *I*) and vice versa. Assuming neither matrix is zero, the columns of each must include eigenvectors for the other eigenvalue. (If either matrix is zero, then *A* is a multiple of the identity and any non-zero vector is an eigenvector.)

For example, suppose

${\displaystyle A={\begin{bmatrix}4&3\\-2&-3\end{bmatrix}},}$

then tr(*A*) = 4 − 3 = 1 and det(*A*) = 4(−3) − 3(−2) = −6, so the characteristic equation is

${\displaystyle 0=\lambda ^{2}-\lambda -6=(\lambda -3)(\lambda +2),}$

and the eigenvalues are 3 and -2. Now,

${\displaystyle A-3I={\begin{bmatrix}1&3\\-2&-6\end{bmatrix}},\qquad A+2I={\begin{bmatrix}6&3\\-2&-1\end{bmatrix}}.}$

In both matrices, the columns are multiples of each other, so either column can be used. Thus, (1, −2) can be taken as an eigenvector associated with the eigenvalue -2, and (3, −1) as an eigenvector associated with the eigenvalue 3, as can be verified by multiplying them by *A*.

### Symmetric 3×3 matrices

The characteristic equation of a symmetric 3×3 matrix *A* is:

${\displaystyle \det \left(\alpha I-A\right)=\alpha ^{3}-\alpha ^{2}{\rm {tr}}(A)-\alpha {\frac {1}{2}}\left({\rm {tr}}(A^{2})-{\rm {tr}}^{2}(A)\right)-\det(A)=0.}$

This equation may be solved using the methods of [Cardano](https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_method "Cubic equation") or [Lagrange](https://en.wikipedia.org/wiki/Cubic_equation#Lagrange's_method "Cubic equation"), but an affine change to *A* will simplify the expression considerably, and lead directly to a [trigonometric solution](https://en.wikipedia.org/wiki/Cubic_equation#Trigonometric_and_hyperbolic_solutions "Cubic equation"). If *A* = *pB* + *qI*, then *A* and *B* have the same eigenvectors, and *β* is an eigenvalue of *B* if and only if *α* = *pβ* + *q* is an eigenvalue of *A*. Letting ${\textstyle q={\rm {tr}}(A)/3}$ and ${\textstyle p=\left({\rm {tr}}\left((A-qI)^{2}\right)/6\right)^{1/2}}$, gives

${\displaystyle \det \left(\beta I-B\right)=\beta ^{3}-3\beta -\det(B)=0.}$

The substitution *β* = 2cos *θ* and some simplification using the identity cos 3 *θ* = 4cos <sup>3</sup> *θ* − 3cos *θ* reduces the equation to cos 3 *θ* = det(*B*) / 2. Thus

${\displaystyle \beta =2{\cos }\left({\frac {1}{3}}{\arccos }\left(\det(B)/2\right)+{\frac {2k\pi }{3}}\right),\quad k=0,1,2.}$

If det(*B*) is complex or is greater than 2 in absolute value, the arccosine should be taken along the same branch for all three values of *k*. This issue doesn't arise when *A* is real and symmetric, resulting in a simple algorithm:[^20]

```
% Given a real symmetric 3x3 matrix A, compute the eigenvalues
% Note that acos and cos operate on angles in radians

p1 = A(1,2)^2 + A(1,3)^2 + A(2,3)^2
if (p1 == 0) 
   % A is diagonal.
   eig1 = A(1,1)
   eig2 = A(2,2)
   eig3 = A(3,3)
else
   q = trace(A)/3               % trace(A) is the sum of all diagonal values
   p2 = (A(1,1) - q)^2 + (A(2,2) - q)^2 + (A(3,3) - q)^2 + 2 * p1
   p = sqrt(p2 / 6)
   B = (1 / p) * (A - q * I)    % I is the identity matrix
   r = det(B) / 2

   % In exact arithmetic for a symmetric matrix  -1 <= r <= 1
   % but computation error can leave it slightly outside this range.
   if (r <= -1) 
      phi = pi / 3
   elseif (r >= 1)
      phi = 0
   else
      phi = acos(r) / 3
   end

   % the eigenvalues satisfy eig3 <= eig2 <= eig1
   eig1 = q + 2 * p * cos(phi)
   eig3 = q + 2 * p * cos(phi + (2*pi/3))
   eig2 = 3 * q - eig1 - eig3     % since trace(A) = eig1 + eig2 + eig3
end
```

Once again, the eigenvectors of *A* can be obtained by recourse to the [Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem "Cayley–Hamilton theorem"). If *α* <sub>1</sub>, *α* <sub>2</sub>, *α* <sub>3</sub> are distinct eigenvalues of *A*, then (*A* − *α* <sub>1</sub> *I*)(*A* − *α* <sub>2</sub> *I*)(*A* − *α* <sub>3</sub> *I*) = 0. Thus the columns of the product of any two of these matrices will contain an eigenvector for the third eigenvalue. However, if *α* <sub>3</sub> = *α* <sub>1</sub>, then (*A* − *α* <sub>1</sub> *I*) <sup>2</sup> (*A* − *α* <sub>2</sub> *I*) = 0 and (*A* − *α* <sub>2</sub> *I*)(*A* − *α* <sub>1</sub> *I*) <sup>2</sup> = 0. Thus the *generalized* eigenspace of *α* <sub>1</sub> is spanned by the columns of *A* − *α* <sub>2</sub> *I* while the ordinary eigenspace is spanned by the columns of (*A* − *α* <sub>1</sub> *I*)(*A* − *α* <sub>2</sub> *I*). The ordinary eigenspace of *α* <sub>2</sub> is spanned by the columns of (*A* − *α* <sub>1</sub> *I*) <sup>2</sup>.

For example, let

${\displaystyle A={\begin{bmatrix}3&2&6\\2&2&5\\-2&-1&-4\end{bmatrix}}.}$

The characteristic equation is

${\displaystyle 0=\lambda ^{3}-\lambda ^{2}-\lambda +1=(\lambda -1)^{2}(\lambda +1),}$

with eigenvalues 1 (of multiplicity 2) and -1. Calculating,

${\displaystyle A-I={\begin{bmatrix}2&2&6\\2&1&5\\-2&-1&-5\end{bmatrix}},\qquad A+I={\begin{bmatrix}4&2&6\\2&3&5\\-2&-1&-3\end{bmatrix}}}$

and

${\displaystyle (A-I)^{2}={\begin{bmatrix}-4&0&-8\\-4&0&-8\\4&0&8\end{bmatrix}},\qquad (A-I)(A+I)={\begin{bmatrix}0&4&4\\0&2&2\\0&-2&-2\end{bmatrix}}}$

Thus (−4, −4, 4) is an eigenvector for −1, and (4, 2, −2) is an eigenvector for 1. (2, 3, −1) and (6, 5, −3) are both generalized eigenvectors associated with 1, either one of which could be combined with (−4, −4, 4) and (4, 2, −2) to form a basis of generalized eigenvectors of *A*. Once found, the eigenvectors can be normalized if needed.

#### Eigenvectors of normal 3×3 matrices

If a 3×3 matrix ${\displaystyle A}$ is normal, then the cross-product can be used to find eigenvectors. If ${\displaystyle \lambda }$ is an eigenvalue of ${\displaystyle A}$, then the null space of ${\displaystyle A-\lambda I}$ is perpendicular to its column space. The [cross product](https://en.wikipedia.org/wiki/Cross_product "Cross product") of two independent columns of ${\displaystyle A-\lambda I}$ will be in the null space. That is, it will be an eigenvector associated with ${\displaystyle \lambda }$. Since the column space is two dimensional in this case, the eigenspace must be one dimensional, so any other eigenvector will be parallel to it.

If ${\displaystyle A-\lambda I}$ does not contain two independent columns but is not **0**, the cross-product can still be used. In this case ${\displaystyle \lambda }$ is an eigenvalue of multiplicity 2, so any vector perpendicular to the column space will be an eigenvector. Suppose ${\displaystyle \mathbf {v} }$ is a non-zero column of ${\displaystyle A-\lambda I}$. Choose an arbitrary vector ${\displaystyle \mathbf {u} }$ not parallel to ${\displaystyle \mathbf {v} }$. Then ${\displaystyle \mathbf {v} \times \mathbf {u} }$ and ${\displaystyle (\mathbf {v} \times \mathbf {u} )\times \mathbf {v} }$ will be perpendicular to ${\displaystyle \mathbf {v} }$ and thus will be eigenvectors of ${\displaystyle \lambda }$.

This does not work when ${\displaystyle A}$ is not normal, as the null space and column space do not need to be perpendicular for such matrices.

[^1]: The term "ordinary" is used here only to emphasize the distinction between "eigenvector" and "generalized eigenvector".

[^2]: where the constant term is multiplied by the identity matrix *I*.

[^3]: This ordering of the inner product (with the conjugate-linear position on the left), is preferred by physicists. Algebraists often place the conjugate-linear position on the right: **w** ⋅ **v** = **v** <sup>*</sup> **w**.

[^4]: [Axler, Sheldon](https://en.wikipedia.org/wiki/Sheldon_Axler "Sheldon Axler") (1995), ["Down with Determinants!"](https://web.archive.org/web/20120913111605/http://www.axler.net/DwD.pdf) (PDF), *American Mathematical Monthly*, **102** (2): 139–154, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2975348](https://doi.org/10.2307%2F2975348), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2975348](https://www.jstor.org/stable/2975348), archived from [the original](http://www.axler.net/DwD.pdf) (PDF) on 2012-09-13, retrieved 2012-07-31

[^5]: F. L. Bauer; C. T. Fike (1960), "Norms and exclusion theorems", *Numer. Math.*, **2**: 137–141, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/bf01386217](https://doi.org/10.1007%2Fbf01386217), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [121278235](https://api.semanticscholar.org/CorpusID:121278235)

[^6]: S.C. Eisenstat; I.C.F. Ipsen (1998), ["Relative Perturbation Results for Eigenvalues and Eigenvectors of Diagonalisable Matrices"](http://www.lib.ncsu.edu/resolver/1840.4/286), *BIT*, **38** (3): 502–9, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/bf02510256](https://doi.org/10.1007%2Fbf02510256), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [119886389](https://api.semanticscholar.org/CorpusID:119886389)

[^7]: J. Dongarra and F. Sullivan (2000). "Top ten algorithms of the century". *Computing in Science and Engineering*. **2**: 22-23. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/MCISE.2000.814652](https://doi.org/10.1109%2FMCISE.2000.814652).

[^8]: [Thompson, R. C.](https://en.wikipedia.org/wiki/Robert_Charles_Thompson "Robert Charles Thompson") (June 1966). ["Principal submatrices of normal and Hermitian matrices"](https://doi.org/10.1215%2Fijm%2F1256055111). *Illinois Journal of Mathematics*. **10** (2): 296–308. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1215/ijm/1256055111](https://doi.org/10.1215%2Fijm%2F1256055111).

[^9]: Peter Nylen; Tin-Yau Tam; Frank Uhlig (1993). "On the eigenvalues of principal submatrices of normal, hermitian and symmetric matrices". *Linear and Multilinear Algebra*. **36** (1): 69–78. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1080/03081089308818276](https://doi.org/10.1080%2F03081089308818276).

[^10]: Bebiano N, Furtado S, da Providência J (2011). ["On the eigenvalues of principal submatrices of J-normal matrices"](https://doi.org/10.1016%2Fj.laa.2011.05.033). *Linear Algebra and Its Applications*. **435** (12): 3101–3114. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.laa.2011.05.033](https://doi.org/10.1016%2Fj.laa.2011.05.033).

[^11]: Forrester PJ, Zhang J (2021). "Corank-1 projections and the randomised Horn problem". *Tunisian Journal of Mathematics*. **3**: 55–73. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1905.05314](https://arxiv.org/abs/1905.05314). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2140/tunis.2021.3.55](https://doi.org/10.2140%2Ftunis.2021.3.55). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [153312446](https://api.semanticscholar.org/CorpusID:153312446).

[^12]: Denton PB, Parke SJ, Tao T, Zhang X (2021). "Eigenvectors from eigenvalues: A survey of a basic identity in linear algebra". *Bulletin of the American Mathematical Society*. **59**: 1. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1908.03795](https://arxiv.org/abs/1908.03795). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/bull/1722](https://doi.org/10.1090%2Fbull%2F1722). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [213918682](https://api.semanticscholar.org/CorpusID:213918682).

[^13]: Press, William H.; Teukolsky, Saul A.; Vetterling, William T.; Flannery, Brian P. (1992). [*Numerical Recipes in C*](https://archive.org/details/numericalrecipes00pres_0) (2nd ed.). Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-43108-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-43108-8 "Special:BookSources/978-0-521-43108-8").

[^14]: Coakley, Ed S. (May 2013), "A fast divide-and-conquer algorithm for computing the spectra of real symmetric tridiagonal matrices.", *[Applied and Computational Harmonic Analysis](https://en.wikipedia.org/wiki/Applied_and_Computational_Harmonic_Analysis "Applied and Computational Harmonic Analysis")*, **34** (3): 379–414, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.acha.2012.06.003](https://doi.org/10.1016%2Fj.acha.2012.06.003)

[^15]: Neymeyr, K. (2006), "A geometric theory for preconditioned inverse iteration IV: On the fastest convergence cases.", *Linear Algebra Appl.*, **415** (1): 114–139, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.laa.2005.06.022](https://doi.org/10.1016%2Fj.laa.2005.06.022)

[^16]: Li, T. Y.; Zeng, Zhonggang (1992), "Laguerre's Iteration In Solving The Symmetric Tridiagonal Eigenproblem - Revisited", *[SIAM Journal on Scientific Computing](https://en.wikipedia.org/wiki/SIAM_Journal_on_Scientific_Computing "SIAM Journal on Scientific Computing")*

[^17]: Chu, Moody T. (1988), "A Note on the Homotopy Method for Linear Algebraic Eigenvalue Problems", *Linear Algebra Appl.*, **105**: 225–236, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/0024-3795(88)90015-8](https://doi.org/10.1016%2F0024-3795%2888%2990015-8)

[^18]: Dhillon, Inderjit S.; Parlett, Beresford N.; Vömel, Christof (2006), ["The Design and Implementation of the MRRR Algorithm"](http://www.cs.utexas.edu/users/inderjit/public_papers/DesignMRRR_toms06.pdf) (PDF), *[ACM Transactions on Mathematical Software](https://en.wikipedia.org/wiki/ACM_Transactions_on_Mathematical_Software "ACM Transactions on Mathematical Software")*, **32** (4): 533–560, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/1186785.1186788](https://doi.org/10.1145%2F1186785.1186788), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [2410736](https://api.semanticscholar.org/CorpusID:2410736)

[^19]: Delattre, B.; Barthélemy, Q.; Araujo, A.; Allauzen, A. (2023), ["Efficient Bound of Lipschitz Constant for Convolutional Layers by Gram Iteration"](https://proceedings.mlr.press/v202/delattre23a.html), *Proceedings of the 40th International Conference on Machine Learning*: 7513–7532

[^20]: Smith, Oliver K. (April 1961), "Eigenvalues of a symmetric 3 × 3 matrix.", *[Communications of the ACM](https://en.wikipedia.org/wiki/Communications_of_the_ACM "Communications of the ACM")*, **4** (4): 168, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/355578.366316](https://doi.org/10.1145%2F355578.366316), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [37815415](https://api.semanticscholar.org/CorpusID:37815415)