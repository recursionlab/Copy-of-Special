---
title: "Invertible matrix"
source: "https://en.wikipedia.org/wiki/Invertible_matrix"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2003-04-26
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra "Linear algebra"), an **invertible matrix** (*non-singular*, *non-degenerate* or *regular*) is a [square matrix](https://en.wikipedia.org/wiki/Square_matrix "Square matrix") that has an [inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse"). In other words, if a matrix is invertible, it can be multiplied by its inverse matrix to yield the [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix"). Invertible matrices are the same size as their inverse.

The inverse of a matrix represents the inverse operation, meaning if a matrix is applied to a particular vector, followed by applying the matrix's inverse, the result is the original vector.

## Definition

An n-by-n [square matrix](https://en.wikipedia.org/wiki/Square_matrix "Square matrix") **A** is called **invertible** if there exists an n-by-n square matrix **B** such that 
$$
{\displaystyle \mathbf {AB} =\mathbf {BA} =\mathbf {I} _{n},}
$$
 where **I** <sub><i>n</i></sub> denotes the n-by-n [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix") and the multiplication used is ordinary [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication "Matrix multiplication").[^1] If this is the case, then the matrix **B** is uniquely determined by **A**, and is called the [*inverse*](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse") of **A**, denoted by **A** <sup>−1</sup>. **Matrix inversion** is the process of finding the matrix which when multiplied by the original matrix gives the identity matrix.[^2]

## Examples

Consider the following 2-by-2 matrix:

${\displaystyle \mathbf {A} ={\begin{pmatrix}-1&{\tfrac {3}{2}}\\1&-1\end{pmatrix}}}$

The matrix ${\displaystyle \mathbf {A} }$ is invertible, as it has inverse ${\displaystyle \mathbf {B} ={\begin{pmatrix}2&3\\2&2\end{pmatrix}},}$ which can be confirmed by computing

${\displaystyle \mathbf {A} \mathbf {B} ={\begin{pmatrix}-1&{\tfrac {3}{2}}\\1&-1\end{pmatrix}}{\begin{pmatrix}2&3\\2&2\end{pmatrix}}={\begin{pmatrix}(-1)\times 2+{\tfrac {3}{2}}\times 2&(-1)\times 3+{\tfrac {3}{2}}\times 2\\1\times 2+(-1)\times 2&1\times 3+(-1)\times 2\end{pmatrix}}={\begin{pmatrix}1&0\\0&1\end{pmatrix}}=\mathbf {I} _{2}}$

To check that it is invertible without finding an inverse, ${\textstyle \det \mathbf {A} =-{\frac {1}{2}}}$ can be computed, which is non-zero.

On the other hand, this is a non-invertible matrix:

${\displaystyle \mathbf {C} ={\begin{pmatrix}2&4\\2&4\end{pmatrix}}}$

We can see the rank of this 2-by-2 matrix is 1, which is *n* − 1 ≠ *n*, so it is non-invertible. Additionally, we can compute that the [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") of ${\displaystyle \mathbf {C} }$ is 0, which is a [necessary and sufficient condition](https://en.wikipedia.org/wiki/Necessary_and_sufficient_condition "Necessary and sufficient condition") for a matrix to be non-invertible.

## Methods of matrix inversion

### Gaussian elimination

[Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination "Gaussian elimination") is a useful and easy way to compute the inverse of a matrix. To compute a matrix inverse using this method, an [augmented matrix](https://en.wikipedia.org/wiki/Augmented_matrix "Augmented matrix") is first created with the left side being the matrix to invert and the right side being the [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix"). Then, Gaussian elimination is used to convert the left side into the identity matrix, which causes the right side to become the inverse of the input matrix.

For example, take the following matrix: 
$$
{\displaystyle \mathbf {A} ={\begin{pmatrix}-1&{\tfrac {3}{2}}\\1&-1\end{pmatrix}}}
$$

The first step to compute its inverse is to create the augmented matrix 
$$
{\displaystyle \left(\!\!{\begin{array}{cc|cc}-1&{\tfrac {3}{2}}&1&0\\1&-1&0&1\end{array}}\!\!\right)}
$$

Call the first row of this matrix ${\displaystyle R_{1}}$ and the second row ${\displaystyle R_{2}}$. Then, add row 1 to row 2 ${\displaystyle (R_{1}+R_{2}\to R_{2}).}$ This yields 
$$
{\displaystyle \left(\!\!{\begin{array}{cc|cc}-1&{\tfrac {3}{2}}&1&0\\0&{\tfrac {1}{2}}&1&1\end{array}}\!\!\right)}
$$

Next, subtract row 2, multiplied by 3, from row 1 ${\displaystyle (R_{1}-3\,R_{2}\to R_{1}),}$ which yields 
$$
{\displaystyle \left(\!\!{\begin{array}{cc|cc}-1&0&-2&-3\\0&{\tfrac {1}{2}}&1&1\end{array}}\!\!\right)}
$$

Finally, multiply row 1 by −1 ${\displaystyle (-R_{1}\to R_{1})}$ and row 2 by 2 ${\displaystyle (2\,R_{2}\to R_{2}).}$ This yields the identity matrix on the left side and the inverse matrix on the right:
$$
{\displaystyle \left(\!\!{\begin{array}{cc|cc}1&0&2&3\\0&1&2&2\end{array}}\!\!\right)}
$$

Thus, 
$$
{\displaystyle \mathbf {A} ^{-1}={\begin{pmatrix}2&3\\2&2\end{pmatrix}}}
$$
 It works because the process of Gaussian elimination can be viewed as a sequence of applying left matrix multiplication using elementary row operations using [elementary matrices](https://en.wikipedia.org/wiki/Elementary_matrix "Elementary matrix") (${\displaystyle \mathbf {E} _{n}}$), such as ${\displaystyle \mathbf {E} _{n}\mathbf {E} _{n-1}\cdots \mathbf {E} _{2}\mathbf {E} _{1}\mathbf {A} =\mathbf {I} }$

Applying right-multiplication using ${\displaystyle \mathbf {A} ^{-1},}$ we get ${\displaystyle \mathbf {E} _{n}\mathbf {E} _{n-1}\cdots \mathbf {E} _{2}\mathbf {E} _{1}\mathbf {I} =\mathbf {I} \mathbf {A} ^{-1}.}$ And the right side ${\displaystyle \mathbf {I} \mathbf {A} ^{-1}=\mathbf {A} ^{-1},}$ which is the inverse we want.

To obtain ${\displaystyle \mathbf {E} _{n}\mathbf {E} _{n-1}\cdots \mathbf {E} _{2}\mathbf {E} _{1}\mathbf {I} ,}$ we create the augmented matrix by combining **A** with **I** and applying [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination "Gaussian elimination"). The two portions will be transformed using the same sequence of elementary row operations. When the left portion becomes **I**, the right portion applied the same elementary row operation sequence will become **A** <sup>−1</sup>.

### Newton's method

A generalization of [Newton's method](https://en.wikipedia.org/wiki/Newton%27s_method "Newton's method") as used for a [multiplicative inverse algorithm](https://en.wikipedia.org/wiki/Multiplicative_inverse#Algorithms "Multiplicative inverse") may be convenient if it is convenient to find a suitable starting seed:

${\displaystyle X_{k+1}=2X_{k}-X_{k}AX_{k}}$

[Victor Pan](https://en.wikipedia.org/wiki/Victor_Pan "Victor Pan") and [John Reif](https://en.wikipedia.org/wiki/John_Reif "John Reif") have done work that includes ways of generating a starting seed.[^3] [^4]

Newton's method is particularly useful when dealing with [families](https://en.wikipedia.org/wiki/Family_\(set_theory\) "Family (set theory)") of related matrices that behave enough like the sequence manufactured for the [homotopy](https://en.wikipedia.org/wiki/Homotopy "Homotopy") above: sometimes a good starting point for refining an approximation for the new inverse can be the already obtained inverse of a previous matrix that nearly matches the current matrix. For example, the pair of sequences of inverse matrices used in obtaining [matrix square roots by Denman–Beavers iteration](https://en.wikipedia.org/wiki/Matrix_square_root#By_Denman%E2%80%93Beavers_iteration "Matrix square root"). That may need more than one pass of the iteration at each new matrix, if they are not close enough together for just one to be enough. Newton's method is also useful for "touch up" corrections to the Gauss–Jordan algorithm which has been contaminated by small errors from [imperfect computer arithmetic](https://en.wikipedia.org/wiki/Round-off_error "Round-off error").

### Cayley–Hamilton method

The [Cayley–Hamilton theorem](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem "Cayley–Hamilton theorem") allows the inverse of **A** to be expressed in terms of det(**A**), traces and powers of **A**:[^5]

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}\sum _{s=0}^{n-1}\mathbf {A} ^{s}\sum _{k_{1},k_{2},\ldots ,k_{n-1}}\prod _{l=1}^{n-1}{\frac {(-1)^{k_{l}+1}}{l^{k_{l}}k_{l}!}}\operatorname {tr} \left(\mathbf {A} ^{l}\right)^{k_{l}},}$

where n is size of **A**, and tr(**A**) is the [trace](https://en.wikipedia.org/wiki/Trace_\(linear_algebra\) "Trace (linear algebra)") of matrix **A** given by the sum of the [main diagonal](https://en.wikipedia.org/wiki/Main_diagonal "Main diagonal"). The sum is taken over s and the sets of all ${\displaystyle k_{l}\geq 0}$ satisfying the linear [Diophantine equation](https://en.wikipedia.org/wiki/Diophantine_equation "Diophantine equation")

${\displaystyle s+\sum _{l=1}^{n-1}lk_{l}=n-1}$

The formula can be rewritten in terms of complete [Bell polynomials](https://en.wikipedia.org/wiki/Bell_polynomials "Bell polynomials") of arguments ${\displaystyle t_{l}=-(l-1)!\operatorname {tr} \left(A^{l}\right)}$ as

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}\sum _{s=1}^{n}\mathbf {A} ^{s-1}{\frac {(-1)^{n-1}}{(n-s)!}}B_{n-s}(t_{1},t_{2},\ldots ,t_{n-s})}$

That is described in more detail under [Cayley–Hamilton method](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem#Determinant_and_inverse_matrix "Cayley–Hamilton theorem").

### Eigendecomposition

If matrix **A** can be eigendecomposed, and if none of its eigenvalues are zero, then **A** is invertible and its inverse is given by

${\displaystyle \mathbf {A} ^{-1}=\mathbf {Q} \mathbf {\Lambda } ^{-1}\mathbf {Q} ^{-1},}$

where **Q** is the square (*N* × *N*) matrix whose ith column is the [eigenvector](https://en.wikipedia.org/wiki/Eigenvector "Eigenvector") ${\displaystyle q_{i}}$ of **A**, and **Λ** is the [diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix "Diagonal matrix") whose diagonal entries are the corresponding eigenvalues, that is, ${\displaystyle \Lambda _{ii}=\lambda _{i}.}$ If **A** is symmetric, **Q** is guaranteed to be an [orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix "Orthogonal matrix"), therefore ${\displaystyle \mathbf {Q} ^{-1}=\mathbf {Q} ^{\mathrm {T} }.}$ Furthermore, because **Λ** is a diagonal matrix, its inverse is easy to calculate:

${\displaystyle \left[\Lambda ^{-1}\right]_{ii}={\frac {1}{\lambda _{i}}}}$

### Cholesky decomposition

If matrix **A** is [positive definite](https://en.wikipedia.org/wiki/Positive_definite_matrix "Positive definite matrix"), then its inverse can be obtained as

${\displaystyle \mathbf {A} ^{-1}=\left(\mathbf {L} ^{*}\right)^{-1}\mathbf {L} ^{-1},}$

where **L** is the [lower triangular](https://en.wikipedia.org/wiki/Lower_triangular "Lower triangular") [Cholesky decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition "Cholesky decomposition") of **A**, and **L** \* denotes the [conjugate transpose](https://en.wikipedia.org/wiki/Conjugate_transpose "Conjugate transpose") of **L**.

### Analytic solution

Writing the transpose of the [matrix of cofactors](https://en.wikipedia.org/wiki/Matrix_of_cofactors "Matrix of cofactors"), known as an [adjugate matrix](https://en.wikipedia.org/wiki/Adjugate_matrix "Adjugate matrix"), may also be an efficient way to calculate the inverse of *small* matrices, but the [recursive](https://en.wikipedia.org/wiki/Recursion "Recursion") method is inefficient for large matrices. To determine the inverse, we calculate a matrix of cofactors:

${\displaystyle \mathbf {A} ^{-1}={1 \over {\begin{vmatrix}\mathbf {A} \end{vmatrix}}}\mathbf {C} ^{\mathrm {T} }={1 \over {\begin{vmatrix}\mathbf {A} \end{vmatrix}}}{\begin{pmatrix}\mathbf {C} _{11}&\mathbf {C} _{21}&\cdots &\mathbf {C} _{n1}\\\mathbf {C} _{12}&\mathbf {C} _{22}&\cdots &\mathbf {C} _{n2}\\\vdots &\vdots &\ddots &\vdots \\\mathbf {C} _{1n}&\mathbf {C} _{2n}&\cdots &\mathbf {C} _{nn}\\\end{pmatrix}}}$

so that

${\displaystyle \left(\mathbf {A} ^{-1}\right)_{ij}={1 \over {\begin{vmatrix}\mathbf {A} \end{vmatrix}}}\left(\mathbf {C} ^{\mathrm {T} }\right)_{ij}={1 \over {\begin{vmatrix}\mathbf {A} \end{vmatrix}}}\left(\mathbf {C} _{ji}\right)}$

where | **A** | is the [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") of **A**, **C** is the matrix of cofactors, and **C** <sup>T</sup> represents the matrix [transpose](https://en.wikipedia.org/wiki/Transpose "Transpose").

#### Inversion of 2 × 2 matrices

The *cofactor equation* listed above yields the following result for 2 × 2 matrices. Inversion of these matrices can be done as follows:[^6]

${\displaystyle \mathbf {A} ^{-1}={\begin{bmatrix}a&b\\c&d\\\end{bmatrix}}^{-1}={\frac {1}{\det \mathbf {A} }}{\begin{bmatrix}\,\,\,d&\!\!-b\\-c&\,a\\\end{bmatrix}}={\frac {1}{ad-bc}}{\begin{bmatrix}\,\,\,d&\!\!-b\\-c&\,a\\\end{bmatrix}}}$

This is possible because 1/(*ad* − *bc*) is the [reciprocal](https://en.wikipedia.org/wiki/Reciprocal_\(mathematics\) "Reciprocal (mathematics)") of the determinant of the matrix in question, and the same strategy could be used for other matrix sizes.

The Cayley–Hamilton method gives

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det \mathbf {A} }}\left[\left(\operatorname {tr} \mathbf {A} \right)\mathbf {I} -\mathbf {A} \right]}$

#### Inversion of 3 × 3 matrices

A [computationally efficient](https://en.wikipedia.org/wiki/Computationally_efficient "Computationally efficient") 3 × 3 matrix inversion is given by

${\displaystyle \mathbf {A} ^{-1}={\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\\\end{bmatrix}}^{-1}={\frac {1}{\det(\mathbf {A} )}}{\begin{bmatrix}\,A&\,B&\,C\\\,D&\,E&\,F\\\,G&\,H&\,I\\\end{bmatrix}}^{\mathrm {T} }={\frac {1}{\det(\mathbf {A} )}}{\begin{bmatrix}\,A&\,D&\,G\\\,B&\,E&\,H\\\,C&\,F&\,I\\\end{bmatrix}}}$

(where the [scalar](https://en.wikipedia.org/wiki/Scalar_\(mathematics\) "Scalar (mathematics)") A is not to be confused with the matrix **A**).

If the determinant is non-zero, the matrix is invertible, with the entries of the intermediary matrix on the right side above given by

${\displaystyle {\begin{alignedat}{6}A&={}&(ei-fh),&\quad &D&={}&-(bi-ch),&\quad &G&={}&(bf-ce),\\B&={}&-(di-fg),&\quad &E&={}&(ai-cg),&\quad &H&={}&-(af-cd),\\C&={}&(dh-eg),&\quad &F&={}&-(ah-bg),&\quad &I&={}&(ae-bd).\\\end{alignedat}}}$

The determinant of **A** can be computed by applying the [rule of Sarrus](https://en.wikipedia.org/wiki/Rule_of_Sarrus "Rule of Sarrus") as follows:

${\displaystyle \det(\mathbf {A} )=aA+bB+cC}$

The Cayley–Hamilton decomposition gives

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}\left({\tfrac {1}{2}}\left[(\operatorname {tr} \mathbf {A} )^{2}-\operatorname {tr} (\mathbf {A} ^{2})\right]\mathbf {I} -\mathbf {A} \operatorname {tr} \mathbf {A} +\mathbf {A} ^{2}\right)}$

The general 3 × 3 inverse can be expressed concisely in terms of the [cross product](https://en.wikipedia.org/wiki/Cross_product "Cross product") and [triple product](https://en.wikipedia.org/wiki/Triple_product "Triple product"). If a matrix ${\displaystyle \mathbf {A} ={\begin{bmatrix}\mathbf {x} _{0}&\mathbf {x} _{1}&\mathbf {x} _{2}\end{bmatrix}}}$ (consisting of three column vectors, ${\displaystyle \mathbf {x} _{0}}$, ${\displaystyle \mathbf {x} _{1}}$, and ${\displaystyle \mathbf {x} _{2}}$) is invertible, its inverse is given by

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}{\begin{bmatrix}{(\mathbf {x} _{1}\times \mathbf {x} _{2})}^{\mathrm {T} }\\{(\mathbf {x} _{2}\times \mathbf {x} _{0})}^{\mathrm {T} }\\{(\mathbf {x} _{0}\times \mathbf {x} _{1})}^{\mathrm {T} }\end{bmatrix}}}$

The determinant of **A**, det(**A**), is equal to the triple product of **x** <sub>0</sub>, **x** <sub>1</sub>, and **x** <sub>2</sub> —the volume of the [parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped "Parallelepiped") formed by the rows or columns:

${\displaystyle \det(\mathbf {A} )=\mathbf {x} _{0}\cdot (\mathbf {x} _{1}\times \mathbf {x} _{2})}$

The correctness of the formula can be checked by using cross- and triple-product properties and by noting that for groups, left and right inverses always coincide. Intuitively, because of the cross products, each row of **A** <sup>–1</sup> is orthogonal to the non-corresponding two columns of **A** (causing the off-diagonal terms of ${\displaystyle \mathbf {I} =\mathbf {A} ^{-1}\mathbf {A} }$ be zero). Dividing by

${\displaystyle \det(\mathbf {A} )=\mathbf {x} _{0}\cdot (\mathbf {x} _{1}\times \mathbf {x} _{2})}$

causes the diagonal entries of **I** = **A** <sup>−1</sup> **A** to be unity. For example, the first diagonal is:

${\displaystyle 1={\frac {1}{\mathbf {x_{0}} \cdot (\mathbf {x} _{1}\times \mathbf {x} _{2})}}\mathbf {x_{0}} \cdot (\mathbf {x} _{1}\times \mathbf {x} _{2})}$

#### Inversion of 4 × 4 matrices

With increasing dimension, expressions for the inverse of **A** get complicated. For *n* = 4, the Cayley–Hamilton method leads to an expression that is still tractable:

${\displaystyle {\begin{aligned}\mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}{\Bigl (}&{\tfrac {1}{6}}{\bigl (}(\operatorname {tr} \mathbf {A} )^{3}-3\operatorname {tr} \mathbf {A} \operatorname {tr} (\mathbf {A} ^{2})+2\operatorname {tr} (\mathbf {A} ^{3}){\bigr )}\mathbf {I} \\[-3mu]&\ \ \ -{\tfrac {1}{2}}\mathbf {A} {\bigl (}(\operatorname {tr} \mathbf {A} )^{2}-\operatorname {tr} (\mathbf {A} ^{2}){\bigr )}+\mathbf {A} ^{2}\operatorname {tr} \mathbf {A} -\mathbf {A} ^{3}{\Bigr )}\end{aligned}}}$

### Blockwise inversion

Let

${\displaystyle \mathbf {M} ={\begin{bmatrix}\mathbf {A} &\mathbf {B} \\\mathbf {C} &\mathbf {D} \end{bmatrix}}}$

where **A**, **B**, **C** and **D** are [matrix sub-blocks](https://en.wikipedia.org/wiki/Block_matrix "Block matrix") of arbitrary size and ${\displaystyle \mathbf {M} /\mathbf {A} :=\mathbf {D} -\mathbf {C} \mathbf {A} ^{-1}\mathbf {B} }$ is the [Schur complement](https://en.wikipedia.org/wiki/Schur_complement "Schur complement") of **A**. (**A** must be square, so that it can be inverted. Furthermore, **A** and **D** − **CA** <sup>−1</sup> **B** must be nonsingular.[^7])

Matrices can also be *inverted blockwise* by using the analytic inversion formula:[^8]

| ${\displaystyle {\begin{bmatrix}\mathbf {A} &\mathbf {B} \\\mathbf {C} &\mathbf {D} \end{bmatrix}}^{-1}={\begin{bmatrix}\mathbf {A} ^{-1}+\mathbf {A} ^{-1}\mathbf {B} \ (\mathbf {M} /\mathbf {A} )^{-1}\mathbf {CA} ^{-1}&-\mathbf {A} ^{-1}\mathbf {B} \left(\mathbf {M} /\mathbf {A} \right)^{-1}\\-\left(\mathbf {M} /\mathbf {A} \right)^{-1}\mathbf {CA} ^{-1}&\left(\mathbf {M} /\mathbf {A} \right)^{-1}\end{bmatrix}},}$ |  | 1 |
| --- | --- | --- |

The strategy is particularly advantageous if **A** is diagonal and **M** / **A** is a small matrix, since they are the only matrices requiring inversion.

The [nullity theorem](https://en.wikipedia.org/wiki/Nullity_theorem "Nullity theorem") says that the nullity of **A** equals the nullity of the sub-block in the lower right of the inverse matrix, and that the nullity of **B** equals the nullity of the sub-block in the upper right of the inverse matrix.

The inversion procedure that led to Equation (**[1](#math_1)**) performed matrix block operations that operated on **C** and **D** first. Instead, if **A** and **B** are operated on first, and provided **D** and **M** / **D**:= **A** − **BD** <sup>−1</sup> **C** are nonsingular,[^9] the result is

| ${\displaystyle {\begin{bmatrix}\mathbf {A} &\mathbf {B} \\\mathbf {C} &\mathbf {D} \end{bmatrix}}^{-1}={\begin{bmatrix}\left(\mathbf {M} /\mathbf {D} \right)^{-1}&-\left(\mathbf {M} /\mathbf {D} \right)^{-1}\mathbf {BD} ^{-1}\\-\mathbf {D} ^{-1}\mathbf {C} \left(\mathbf {M} /\mathbf {D} \right)^{-1}&\quad \mathbf {D} ^{-1}+\mathbf {D} ^{-1}\mathbf {C} \left(\mathbf {M} /\mathbf {D} \right)^{-1}\mathbf {BD} ^{-1}\end{bmatrix}}.}$ |  | 2 |
| --- | --- | --- |

Equating the upper-left sub-matrices of Equations (**[1](#math_1)**) and (**[2](#math_2)**) leads to

| ${\displaystyle {\begin{aligned}\left(\mathbf {A} -\mathbf {BD} ^{-1}\mathbf {C} \right)^{-1}&=\mathbf {A} ^{-1}+\mathbf {A} ^{-1}\mathbf {B} \left(\mathbf {D} -\mathbf {CA} ^{-1}\mathbf {B} \right)^{-1}\mathbf {CA} ^{-1}\\\left(\mathbf {A} -\mathbf {BD} ^{-1}\mathbf {C} \right)^{-1}\mathbf {BD} ^{-1}&=\mathbf {A} ^{-1}\mathbf {B} \left(\mathbf {D} -\mathbf {CA} ^{-1}\mathbf {B} \right)^{-1}\\\mathbf {D} ^{-1}\mathbf {C} \left(\mathbf {A} -\mathbf {BD} ^{-1}\mathbf {C} \right)^{-1}&=\left(\mathbf {D} -\mathbf {CA} ^{-1}\mathbf {B} \right)^{-1}\mathbf {CA} ^{-1}\\\mathbf {D} ^{-1}+\mathbf {D} ^{-1}\mathbf {C} \left(\mathbf {A} -\mathbf {BD} ^{-1}\mathbf {C} \right)^{-1}\mathbf {BD} ^{-1}&=\left(\mathbf {D} -\mathbf {CA} ^{-1}\mathbf {B} \right)^{-1}\end{aligned}}}$ |  | 3 |
| --- | --- | --- |

where Equation (**[3](#math_3)**) is the [Woodbury matrix identity](https://en.wikipedia.org/wiki/Woodbury_matrix_identity "Woodbury matrix identity"), which is equivalent to the [binomial inverse theorem](https://en.wikipedia.org/wiki/Binomial_inverse_theorem "Binomial inverse theorem").

If **A** and **D** are both invertible, then the above two block matrix inverses can be combined to provide the simple factorization

| ${\displaystyle {\begin{bmatrix}\mathbf {A} &\mathbf {B} \\\mathbf {C} &\mathbf {D} \end{bmatrix}}^{-1}={\begin{bmatrix}\left(\mathbf {A} -\mathbf {B} \mathbf {D} ^{-1}\mathbf {C} \right)^{-1}&\mathbf {0} \\\mathbf {0} &\left(\mathbf {D} -\mathbf {C} \mathbf {A} ^{-1}\mathbf {B} \right)^{-1}\end{bmatrix}}{\begin{bmatrix}\mathbf {I} &-\mathbf {B} \mathbf {D} ^{-1}\\-\mathbf {C} \mathbf {A} ^{-1}&\mathbf {I} \end{bmatrix}}.}$ |  | 2 |
| --- | --- | --- |

By the [Weinstein–Aronszajn identity](https://en.wikipedia.org/wiki/Weinstein%E2%80%93Aronszajn_identity "Weinstein–Aronszajn identity"), one of the two matrices in the block-diagonal matrix is invertible exactly when the other is.

This formula simplifies significantly when the upper right block matrix **B** is the [zero matrix](https://en.wikipedia.org/wiki/Zero_matrix "Zero matrix"). This formulation is useful when the matrices **A** and **D** have relatively simple inverse formulas (or [pseudo inverses](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse "Moore–Penrose inverse") in the case where the blocks are not all square. In this special case, the block matrix inversion formula stated in full generality above becomes

${\displaystyle {\begin{bmatrix}\mathbf {A} &\mathbf {0} \\\mathbf {C} &\mathbf {D} \end{bmatrix}}^{-1}={\begin{bmatrix}\mathbf {A} ^{-1}&\mathbf {0} \\-\mathbf {D} ^{-1}\mathbf {CA} ^{-1}&\mathbf {D} ^{-1}\end{bmatrix}}}$

If the given invertible matrix is a symmetric matrix with invertible block **A** the following block inverse formula holds [^10]

| ${\displaystyle {\begin{bmatrix}\mathbf {A} &\mathbf {C} ^{T}\\\mathbf {C} &\mathbf {D} \end{bmatrix}}^{-1}={\begin{bmatrix}\mathbf {A} ^{-1}+\mathbf {A} ^{-1}\mathbf {C} ^{T}\mathbf {S} ^{-1}\mathbf {C} \mathbf {A} ^{-1}&-\mathbf {A} ^{-1}\mathbf {C} ^{T}\mathbf {S} ^{-1}\\-\mathbf {S} ^{-1}\mathbf {C} \mathbf {A} ^{-1}&\mathbf {S} ^{-1}\end{bmatrix}},}$ |  | 4 |
| --- | --- | --- |

where ${\displaystyle \mathbf {S} =\mathbf {D} -\mathbf {C} \mathbf {A} ^{-1}\mathbf {C} ^{T}}$. This requires 2 inversions of the half-sized matrices **A** and **S** and only 4 multiplications of half-sized matrices, if organized properly 
$$
{\displaystyle {\begin{aligned}\mathbf {W} _{1}&=\mathbf {C} \mathbf {A} ^{-1},\\[3mu]\mathbf {W} _{2}&=\mathbf {W} _{1}\mathbf {C} ^{T}=\mathbf {C} \mathbf {A} ^{-1}\mathbf {C} ^{T},\\[3mu]\mathbf {W} _{3}&=\mathbf {S} ^{-1}\mathbf {W} _{1}=\mathbf {S} ^{-1}\mathbf {C} \mathbf {A} ^{-1},\\[3mu]\mathbf {W} _{4}&=\mathbf {W} _{1}^{T}\mathbf {W} _{3}=\mathbf {A} ^{-1}\mathbf {C} ^{T}\mathbf {S} ^{-1}\mathbf {C} \mathbf {A} ^{-1},\end{aligned}}}
$$
 together with some additions, subtractions, negations and transpositions of negligible complexity. Any matrix ${\displaystyle \mathbf {M} }$ has an associated positive semidefinite, symmetric matrix ${\displaystyle \mathbf {M} ^{T}\mathbf {M} }$, which is exactly invertible (and positive definite), if and only if ${\displaystyle \mathbf {M} }$ is invertible. By writing ${\displaystyle \mathbf {M} ^{-1}=\left(\mathbf {M} ^{T}\mathbf {M} \right)^{-1}\mathbf {M} ^{T}}$ matrix inversion can be reduced to inverting symmetric matrices and 2 additional matrix multiplications, because the [positive definite matrix](https://en.wikipedia.org/wiki/Definite_matrix#Decomposition "Definite matrix") ${\displaystyle \mathbf {M} ^{T}\mathbf {M} }$ satisfies the invertibility condition for its left upper block **A**.

Those formulas together allow to construct a [divide and conquer algorithm](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm "Divide and conquer algorithm") that uses blockwise inversion of associated symmetric matrices to invert a matrix with the same time complexity as the [matrix multiplication algorithm](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm "Matrix multiplication algorithm") that is used internally.[^10] [Research into matrix multiplication complexity](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication "Computational complexity of matrix multiplication") shows that there exist matrix multiplication algorithms with a complexity of *O* (*n* <sup>2.371552</sup>) operations, while the best proven lower bound is [Ω](https://en.wikipedia.org/wiki/Big_O_notation#Family_of_Bachmann%E2%80%93Landau_notations "Big O notation") (*n* <sup>2</sup> log *n*).[^11]

### By Neumann series

If a matrix **A** has the property that

${\displaystyle \lim _{n\to \infty }(\mathbf {I} -\mathbf {A} )^{n}=0}$

then **A** is nonsingular and its inverse may be expressed by a [Neumann series](https://en.wikipedia.org/wiki/Neumann_series "Neumann series"):[^12]

${\displaystyle \mathbf {A} ^{-1}=\sum _{n=0}^{\infty }(\mathbf {I} -\mathbf {A} )^{n}}$

Truncating the sum results in an "approximate" inverse which may be useful as a [preconditioner](https://en.wikipedia.org/wiki/Preconditioner "Preconditioner"). Note that a truncated series can be accelerated exponentially by noting that the Neumann series is a [geometric sum](https://en.wikipedia.org/wiki/Geometric_sum "Geometric sum"). As such, it satisfies

${\displaystyle \sum _{n=0}^{2^{L}-1}(\mathbf {I} -\mathbf {A} )^{n}=\prod _{l=0}^{L-1}\left(\mathbf {I} +(\mathbf {I} -\mathbf {A} )^{2^{l}}\right)}$

Therefore, only 2 *L* − 2 matrix multiplications are needed to compute 2 <sup><i>L</i></sup> terms of the sum.

More generally, if **A** is "near" the invertible matrix **X** in the sense that

${\displaystyle \lim _{n\to \infty }\left(\mathbf {I} -\mathbf {X} ^{-1}\mathbf {A} \right)^{n}=0\mathrm {~~or~~} \lim _{n\to \infty }\left(\mathbf {I} -\mathbf {A} \mathbf {X} ^{-1}\right)^{n}=0}$

then **A** is nonsingular and its inverse is

${\displaystyle \mathbf {A} ^{-1}=\sum _{n=0}^{\infty }\left(\mathbf {X} ^{-1}(\mathbf {X} -\mathbf {A} )\right)^{n}\mathbf {X} ^{-1}~}$

If it is also the case that **A** − **X** has [rank](https://en.wikipedia.org/wiki/Rank_\(linear_algebra\) "Rank (linear algebra)") 1 then this simplifies to

${\displaystyle \mathbf {A} ^{-1}=\mathbf {X} ^{-1}-{\frac {\mathbf {X} ^{-1}(\mathbf {A} -\mathbf {X} )\mathbf {X} ^{-1}}{1+\operatorname {tr} \left(\mathbf {X} ^{-1}(\mathbf {A} -\mathbf {X} )\right)}}~}$

### p-adic approximation

If **A** is a matrix with [integer](https://en.wikipedia.org/wiki/Integer "Integer") or [rational](https://en.wikipedia.org/wiki/Rational_number "Rational number") entries, and we seek a solution in [arbitrary-precision](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic "Arbitrary-precision arithmetic") rationals, a [p-adic](https://en.wikipedia.org/wiki/P-adic "P-adic") approximation method converges to an exact solution in O(*n* <sup>4</sup> log <sup>2</sup> *n*), assuming standard O(*n* <sup>3</sup>) matrix multiplication is used.[^13] The method relies on solving n linear systems via Dixon's method of p-adic approximation (each in O(*n* <sup>3</sup> log <sup>2</sup> *n*)) and is available as such in software specialized in arbitrary-precision matrix operations, for example, in IML.[^14]

### Reciprocal basis vectors method

Given an *n* × *n* square matrix ${\displaystyle \mathbf {X} =\left[x^{ij}\right]}$, ${\displaystyle 1\leq i,j\leq n}$, with n rows interpreted as n vectors ${\displaystyle \mathbf {x} _{i}=x^{ij}\mathbf {e} _{j}}$ ([Einstein summation](https://en.wikipedia.org/wiki/Einstein_summation "Einstein summation") assumed) where the ${\displaystyle \mathbf {e} _{j}}$ are a standard [orthonormal basis](https://en.wikipedia.org/wiki/Orthonormal_basis "Orthonormal basis") of [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space") ${\displaystyle \mathbb {R} ^{n}}$ (${\displaystyle \mathbf {e} _{i}=\mathbf {e} ^{i},\mathbf {e} _{i}\cdot \mathbf {e} ^{j}=\delta _{i}^{j}}$), then using [Clifford algebra](https://en.wikipedia.org/wiki/Clifford_algebra "Clifford algebra") (or [geometric algebra](https://en.wikipedia.org/wiki/Geometric_algebra "Geometric algebra")) we compute the reciprocal (sometimes called [dual](https://en.wikipedia.org/wiki/Geometric_algebra#Dual_basis "Geometric algebra")) column vectors:

${\displaystyle \mathbf {x} ^{i}=x_{ji}\mathbf {e} ^{j}=(-1)^{i-1}(\mathbf {x} _{1}\wedge \cdots \wedge ()_{i}\wedge \cdots \wedge \mathbf {x} _{n})\cdot (\mathbf {x} _{1}\wedge \ \mathbf {x} _{2}\wedge \cdots \wedge \mathbf {x} _{n})^{-1}}$

as the columns of the inverse matrix ${\displaystyle \mathbf {X} ^{-1}=[x_{ji}].}$ Note that, the place " ${\displaystyle ()_{i}}$ " indicates that " ${\displaystyle \mathbf {x} _{i}}$ " is removed from that place in the above expression for ${\displaystyle \mathbf {x} ^{i}}$. We then have ${\displaystyle \mathbf {X} \mathbf {X} ^{-1}=\left[\mathbf {x} _{i}\cdot \mathbf {x} ^{j}\right]=\left[\delta _{i}^{j}\right]=\mathbf {I} _{n}}$, where ${\displaystyle \delta _{i}^{j}}$ is the [Kronecker delta](https://en.wikipedia.org/wiki/Kronecker_delta "Kronecker delta"). We also have ${\displaystyle \mathbf {X} ^{-1}\mathbf {X} =\left[\left(\mathbf {e} _{i}\cdot \mathbf {x} ^{k}\right)\left(\mathbf {e} ^{j}\cdot \mathbf {x} _{k}\right)\right]=\left[\mathbf {e} _{i}\cdot \mathbf {e} ^{j}\right]=\left[\delta _{i}^{j}\right]=\mathbf {I} _{n}}$, as required. If the vectors ${\displaystyle \mathbf {x} _{i}}$ are not linearly independent, then ${\displaystyle (\mathbf {x} _{1}\wedge \mathbf {x} _{2}\wedge \cdots \wedge \mathbf {x} _{n})=0}$ and the matrix ${\displaystyle \mathbf {X} }$ is not invertible (has no inverse).

## Properties

### Singularity

Over a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)"), a square matrix that is *not* invertible is called **singular** or **degenerate**. A square matrix with entries in a field is singular [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") its [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") is zero.

### Invertible matrix theorem

Let **A** be a square n-by-n matrix over a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") K (e.g., the field ⁠ ${\displaystyle \mathbb {R} }$ ⁠ of real numbers). The following statements are equivalent, i.e., they are either all true or all false for any given matrix:[^15]

- **A** is invertible, i.e. it has an inverse under matrix multiplication, i.e., there exists a **B** such that **AB** = **I** <sub><i>n</i></sub> = **BA**. (In that statement, "invertible" can equivalently be replaced with "left-invertible" or "right-invertible" in which one-sided inverses are considered.)
- The linear transformation mapping **x** to **Ax** is invertible, i.e., it has an inverse under function composition. (There, again, "invertible" can equivalently be replaced with either "left-invertible" or "right-invertible".)
- The [transpose](https://en.wikipedia.org/wiki/Transpose "Transpose") **A** <sup>T</sup> is an invertible matrix.
- **A** is [row-equivalent](https://en.wikipedia.org/wiki/Row_equivalence "Row equivalence") to the n-by-n [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix "Identity matrix") **I** <sub><i>n</i></sub>.
- **A** is [column-equivalent](https://en.wikipedia.org/wiki/Row_equivalence "Row equivalence") to the n-by-n identity matrix **I** <sub><i>n</i></sub>.
- **A** has n [pivot positions](https://en.wikipedia.org/wiki/Pivot_position "Pivot position").
- **A** has full [rank](https://en.wikipedia.org/wiki/Rank_\(linear_algebra\) "Rank (linear algebra)"): rank **A** = *n*.
- **A** has a trivial [kernel](https://en.wikipedia.org/wiki/Kernel_\(linear_algebra\) "Kernel (linear algebra)"): ker(**A**) = { **0** }.
- The linear transformation mapping **x** to **Ax** is bijective; that is, the equation **Ax** = **b** has exactly one solution for each **b** in K <sup>n</sup>. (There, "bijective" can equivalently be replaced with " [injective](https://en.wikipedia.org/wiki/Injective "Injective") " or " [surjective](https://en.wikipedia.org/wiki/Surjective "Surjective") ".)
- The columns of **A** form a [basis](https://en.wikipedia.org/wiki/Basis_of_a_vector_space "Basis of a vector space") of K <sup>n</sup>. (In this statement, "basis" can equivalently be replaced with either "linearly independent set" or "spanning set")
- The rows of **A** form a basis of K <sup>n</sup>. (Similarly, here, "basis" can equivalently be replaced with either "linearly independent set" or "spanning set")
- The [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") of **A** is nonzero: det **A** ≠ 0. In general, a square matrix over a [commutative ring](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring") is invertible if and only if its determinant is a [unit](https://en.wikipedia.org/wiki/Unit_\(ring_theory\) "Unit (ring theory)") (i.e. multiplicatively invertible element) of that ring.
- The number 0 is not an [eigenvalue](https://en.wikipedia.org/wiki/Eigenvalue "Eigenvalue") of **A**. (More generally, a number ${\displaystyle \lambda }$ is an eigenvalue of **A** if the matrix ${\displaystyle \mathbf {A} -\lambda \mathbf {I} }$ is singular, where **I** is the identity matrix.)
- The matrix **A** can be expressed as a finite product of [elementary matrices](https://en.wikipedia.org/wiki/Elementary_matrix "Elementary matrix").

### Other properties

Furthermore, the following properties hold for an invertible matrix **A**:

- ${\displaystyle (\mathbf {A} ^{-1})^{-1}=\mathbf {A} }$
- ${\displaystyle (k\mathbf {A} )^{-1}=k^{-1}\mathbf {A} ^{-1}}$ for nonzero scalar k
- ${\displaystyle (\mathbf {Ax} )^{+}=\mathbf {x} ^{+}\mathbf {A} ^{-1}}$ if **A** has orthonormal columns, where <sup>+</sup> denotes the [Moore–Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse "Moore–Penrose inverse") and **x** is a vector
- ${\displaystyle (\mathbf {A} ^{\mathrm {T} })^{-1}=(\mathbf {A} ^{-1})^{\mathrm {T} }}$
- For any invertible n-by-n matrices **A** and **B**, ${\displaystyle (\mathbf {AB} )^{-1}=\mathbf {B} ^{-1}\mathbf {A} ^{-1}.}$ More generally, if ${\displaystyle \mathbf {A} _{1},\dots ,\mathbf {A} _{k}}$ are invertible n-by-n matrices, then ${\displaystyle (\mathbf {A} _{1}\mathbf {A} _{2}\cdots \mathbf {A} _{k-1}\mathbf {A} _{k})^{-1}=\mathbf {A} _{k}^{-1}\mathbf {A} _{k-1}^{-1}\cdots \mathbf {A} _{2}^{-1}\mathbf {A} _{1}^{-1}.}$
- ${\displaystyle \det \mathbf {A} ^{-1}=(\det \mathbf {A} )^{-1}.}$
- Left and right inverses are equal. That is, if ${\displaystyle \mathbf {LA} =\mathbf {I} }$ and ${\displaystyle \mathbf {AR} =\mathbf {I} }$ then ${\displaystyle \mathbf {L} =\mathbf {L} (\mathbf {AR} )=(\mathbf {LA} )\mathbf {R} =\mathbf {R} }$.

The rows of the inverse matrix **V** of a matrix **U** are [orthonormal](https://en.wikipedia.org/wiki/Orthonormal "Orthonormal") to the columns of **U** (and vice versa interchanging rows for columns). To see this, suppose that **UV** = **VU** = **I** where the rows of **V** are denoted as ${\displaystyle v_{i}^{\mathrm {T} }}$ and the columns of **U** as ${\displaystyle u_{j}}$ for ${\displaystyle 1\leq i,j\leq n.}$ Then clearly, the [Euclidean inner product](https://en.wikipedia.org/wiki/Dot_product "Dot product") of any two ${\displaystyle v_{i}^{\mathrm {T} }u_{j}=\delta _{i,j}.}$ This property can also be useful in constructing the inverse of a square matrix in some instances, where a set of [orthogonal](https://en.wikipedia.org/wiki/Orthogonal "Orthogonal") vectors (but not necessarily orthonormal vectors) to the columns of **U** are known. In which case, one can apply the iterative [Gram–Schmidt process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process "Gram–Schmidt process") to this initial set to determine the rows of the inverse **V**.

A matrix that is its own inverse (i.e., a matrix **A** such that **A** = **A** <sup>−1</sup> and consequently **A** <sup>2</sup> = **I**) is called an [involutory matrix](https://en.wikipedia.org/wiki/Involutory_matrix "Involutory matrix").

### In relation to its adjugate

The [adjugate](https://en.wikipedia.org/wiki/Adjugate_matrix "Adjugate matrix") of a matrix **A** can be used to find the inverse of **A** as follows:

If **A** is an invertible matrix, then

${\displaystyle \mathbf {A} ^{-1}={\frac {1}{\det(\mathbf {A} )}}\operatorname {adj} (\mathbf {A} )}$

### In relation to the identity matrix

It follows from the [associativity](https://en.wikipedia.org/wiki/Associativity "Associativity") of matrix multiplication that if

${\displaystyle \mathbf {AB} =\mathbf {I} \ }$

for *finite square* matrices **A** and **B**, then also

${\displaystyle \mathbf {BA} =\mathbf {I} \ }$ [^16]

### Density

Over the field of real numbers, the set of singular n-by-n matrices, considered as a [subset](https://en.wikipedia.org/wiki/Subset "Subset") of ⁠ ${\displaystyle \mathbb {R} ^{n\times n},}$ ⁠ is a [null set](https://en.wikipedia.org/wiki/Null_set "Null set"), that is, has [Lebesgue measure](https://en.wikipedia.org/wiki/Lebesgue_measure "Lebesgue measure") zero. That is true because singular matrices are the roots of the [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") function. It is a [continuous function](https://en.wikipedia.org/wiki/Continuous_function "Continuous function") because it is a [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") in the entries of the matrix. Thus in the language of [measure theory](https://en.wikipedia.org/wiki/Measure_theory "Measure theory"), [almost all](https://en.wikipedia.org/wiki/Almost_all "Almost all") n-by-n matrices are invertible.

Furthermore, the set of n-by-n invertible matrices is [open](https://en.wikipedia.org/wiki/Open_set "Open set") and [dense](https://en.wikipedia.org/wiki/Dense_set "Dense set") in the [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") of all n-by-n matrices. Equivalently, the set of singular matrices is [closed](https://en.wikipedia.org/wiki/Closed_set "Closed set") and [nowhere dense](https://en.wikipedia.org/wiki/Nowhere_dense "Nowhere dense") in the space of n-by-n matrices.

In practice, however, non-invertible matrices may be encountered. In [numerical calculations](https://en.wikipedia.org/wiki/Numerical_analysis "Numerical analysis"), matrices that are invertible but close to a non-invertible matrix may still be problematic and are said to be [ill-conditioned](https://en.wikipedia.org/wiki/Condition_number#Matrices "Condition number").

## Derivative of the matrix inverse

Suppose that the invertible matrix **A** depends on a parameter *t*. Then the [derivative](https://en.wikipedia.org/wiki/Derivative_of_matrix "Derivative of matrix") of the inverse of **A** with respect to *t* is given by [^17]

${\displaystyle {\frac {\mathrm {d} }{\mathrm {d} t}}\mathbf {A} ^{-1}=-\mathbf {A} ^{-1}{\frac {\mathrm {d} \mathbf {A} }{\mathrm {d} t}}\mathbf {A} ^{-1}}$

To derive the above expression for the derivative of the inverse of **A**, one can differentiate the definition of the matrix inverse ${\displaystyle \mathbf {A} ^{-1}\mathbf {A} =\mathbf {I} }$ using the [product rule](https://en.wikipedia.org/wiki/Product_rule "Product rule"), and then solve for the derivative of the inverse of **A**:

${\displaystyle \mathbf {0} ={\frac {\mathrm {d} \mathbf {I} }{\mathrm {d} t}}={\frac {\mathrm {d} (\mathbf {A} ^{-1}\mathbf {A} )}{\mathrm {d} t}}={\frac {\mathrm {d} (\mathbf {A} ^{-1})}{\mathrm {d} t}}\mathbf {A} +\mathbf {A} ^{-1}{\frac {\mathrm {d} \mathbf {A} }{\mathrm {d} t}}}$

Subtracting ${\displaystyle \mathbf {A} ^{-1}{\frac {\mathrm {d} \mathbf {A} }{\mathrm {d} t}}}$ from both ends of this formula, and multiplying on the right by ${\displaystyle \mathbf {A} ^{-1}}$ finishes the derivation.

If ${\displaystyle \varepsilon }$ is a small number then the derivative formula gives:

${\displaystyle \left(\mathbf {A} +\varepsilon \mathbf {X} \right)^{-1}=\mathbf {A} ^{-1}-\varepsilon \mathbf {A} ^{-1}\mathbf {X} \mathbf {A} ^{-1}+{\mathcal {O}}(\varepsilon ^{2})\,}$

Given a positive integer ${\displaystyle n}$,

${\displaystyle {\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} t}}\mathbf {A} ^{n}&=\sum _{i=1}^{n}\mathbf {A} ^{i-1}{\frac {\mathrm {d} \mathbf {A} }{\mathrm {d} t}}\mathbf {A} ^{n-i},\\{\frac {\mathrm {d} }{\mathrm {d} t}}\mathbf {A} ^{-n}&=-\sum _{i=1}^{n}\mathbf {A} ^{-i}{\frac {\mathrm {d} \mathbf {A} }{\mathrm {d} t}}\mathbf {A} ^{-(n+1-i)}\end{aligned}}}$

In particular,

${\displaystyle {\begin{aligned}(\mathbf {A} +\varepsilon \mathbf {X} )^{n}&=\mathbf {A} ^{n}+\varepsilon \sum _{i=1}^{n}\mathbf {A} ^{i-1}\mathbf {X} \mathbf {A} ^{n-i}+{\mathcal {O}}\left(\varepsilon ^{2}\right),\\(\mathbf {A} +\varepsilon \mathbf {X} )^{-n}&=\mathbf {A} ^{-n}-\varepsilon \sum _{i=1}^{n}\mathbf {A} ^{-i}\mathbf {X} \mathbf {A} ^{-(n+1-i)}+{\mathcal {O}}\left(\varepsilon ^{2}\right)\end{aligned}}}$

## Generalizations

### Non-square matrices

Non-square matrices, i.e. m-by-n matrices for which *m* ≠ *n*, do not have an inverse. However, in some cases such a matrix may have a [left inverse](https://en.wikipedia.org/wiki/Inverse_element#Matrices "Inverse element") or [right inverse](https://en.wikipedia.org/wiki/Inverse_element#Matrices "Inverse element"). If **A** is m-by-n and the [rank](https://en.wikipedia.org/wiki/Rank_\(linear_algebra\) "Rank (linear algebra)") of **A** is equal to *n*, (*n* ≤ *m*), then **A** has a left inverse, an *n* -by- *m* matrix **B** such that **BA** = **I** <sub><i>n</i></sub>. If **A** has rank *m* (*m* ≤ *n*), then it has a right inverse, an n-by-m matrix **B** such that **AB** = **I** <sub><i>m</i></sub>.

Some of the properties of inverse matrices are shared by [generalized inverses](https://en.wikipedia.org/wiki/Generalized_inverse "Generalized inverse") (such as the [Moore–Penrose inverse](https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse "Moore–Penrose inverse")), which can be defined for any *m* -by- *n* matrix.[^18]

### In Abstract algebra

While the most common case is that of matrices over the [real](https://en.wikipedia.org/wiki/Real_number "Real number") or [complex](https://en.wikipedia.org/wiki/Complex_number "Complex number") numbers, all of those definitions can be given for matrices over any [algebraic structure](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure") equipped with [addition](https://en.wikipedia.org/wiki/Addition "Addition") and [multiplication](https://en.wikipedia.org/wiki/Multiplication "Multiplication") (i.e. [rings](https://en.wikipedia.org/wiki/Ring_\(mathematics\) "Ring (mathematics)")). However, in the case of a ring being [commutative](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring"), the condition for a square matrix to be invertible is that its determinant is invertible in the ring, which in general is a stricter requirement than it being nonzero. For a [noncommutative ring](https://en.wikipedia.org/wiki/Noncommutative_ring "Noncommutative ring"), the usual determinant is not defined. The conditions for existence of left-inverse or right-inverse are more complicated, since a notion of rank does not exist over rings.

The set of *n* × *n* invertible matrices together with the operation of [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication "Matrix multiplication") and entries from ring R form a [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)"), the [general linear group](https://en.wikipedia.org/wiki/General_linear_group "General linear group") of degree n, denoted GL <sub><i>n</i></sub> (*R*).

## Applications

For most practical applications, it is not necessary to invert a matrix to solve a [system of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations "System of linear equations"); however, for a unique solution, it is necessary for the matrix involved to be invertible.

Decomposition techniques like [LU decomposition](https://en.wikipedia.org/wiki/LU_decomposition "LU decomposition") are much faster than inversion, and various fast algorithms for special classes of linear systems have also been developed.

### Regression/least squares

Although an explicit inverse is not necessary to estimate the vector of unknowns, it is the easiest way to estimate their accuracy and is found in the diagonal of a matrix inverse (the posterior covariance matrix of the vector of unknowns). However, faster algorithms to compute only the diagonal entries of a matrix inverse are known in many cases.[^19]

### Matrix inverses in real-time simulations

Matrix inversion plays a significant role in [computer graphics](https://en.wikipedia.org/wiki/Computer_graphics "Computer graphics"), particularly in [3D graphics](https://en.wikipedia.org/wiki/3D_graphics "3D graphics") rendering and [3D simulations](https://en.wikipedia.org/w/index.php?title=3D_simulations&action=edit&redlink=1 "3D simulations (page does not exist)"). Examples include screen-to-world [ray casting](https://en.wikipedia.org/wiki/Ray_casting "Ray casting"), world-to-subspace-to-world object transformations, and physical simulations.

### Matrix inverses in MIMO wireless communication

Matrix inversion also plays a significant role in the [MIMO](https://en.wikipedia.org/wiki/MIMO "MIMO") (Multiple-Input, Multiple-Output) technology in [wireless communications](https://en.wikipedia.org/wiki/Wireless_communications "Wireless communications"). The MIMO system consists of *N* transmit and *M* receive antennas. Unique signals, occupying the same [frequency band](https://en.wikipedia.org/wiki/Frequency_band "Frequency band"), are sent via *N* transmit antennas and are received via *M* receive antennas. The signal arriving at each receive antenna will be a [linear combination](https://en.wikipedia.org/wiki/Linear_combination "Linear combination") of the *N* transmitted signals forming an *N* × *M* transmission matrix **H**. It is crucial for the matrix **H** to be invertible so that the receiver can figure out the transmitted information.[^20]

[^1]: [Axler, Sheldon](https://en.wikipedia.org/wiki/Sheldon_Axler "Sheldon Axler") (18 December 2014). *Linear Algebra Done Right*. [Undergraduate Texts in Mathematics](https://en.wikipedia.org/wiki/Undergraduate_Texts_in_Mathematics "Undergraduate Texts in Mathematics") (3rd ed.). [Springer Publishing](https://en.wikipedia.org/wiki/Springer_Publishing "Springer Publishing") (published 2015). p. 296. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-319-11079-0](https://en.wikipedia.org/wiki/Special:BookSources/978-3-319-11079-0 "Special:BookSources/978-3-319-11079-0").

[^2]: J.-S. Roger Jang (March 2001). ["Matrix Inverse in Block Form"](https://www.cs.nthu.edu.tw/~jang/book/addenda/matinv/matinv/).

[^3]: Pan, Victor; Reif, John (1985), *Efficient Parallel Solution of Linear Systems*, Proceedings of the 17th Annual ACM Symposium on Theory of Computing, Providence: [ACM](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery "Association for Computing Machinery")

[^4]: Pan, Victor; Reif, John (1985), *Harvard University Center for Research in Computing Technology Report TR-02-85*, Cambridge, MA: [Aiken Computation Laboratory](https://en.wikipedia.org/w/index.php?title=Aiken_Computation_Laboratory&action=edit&redlink=1 "Aiken Computation Laboratory (page does not exist)")

[^5]: A proof can be found in the Appendix B of Kondratyuk, L. A.; Krivoruchenko, M. I. (1992). ["Superconducting quark matter in SU(2) color group"](https://www.researchgate.net/publication/226920070). *Zeitschrift für Physik A*. **344** (1): 99–115. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[1992ZPhyA.344...99K](https://ui.adsabs.harvard.edu/abs/1992ZPhyA.344...99K). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BF01291027](https://doi.org/10.1007%2FBF01291027). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [120467300](https://api.semanticscholar.org/CorpusID:120467300).

[^6]: Strang, Gilbert (2003). [*Introduction to linear algebra*](https://books.google.com/books?id=Gv4pCVyoUVYC) (3rd ed.). SIAM. p. 71. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-9614088-9-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-9614088-9-3 "Special:BookSources/978-0-9614088-9-3")., [Chapter 2, page 71](https://books.google.com/books?id=Gv4pCVyoUVYC&pg=PA71)

[^7]: Bernstein, Dennis (2005). *Matrix Mathematics*. Princeton University Press. p. 44. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-691-11802-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-691-11802-4 "Special:BookSources/978-0-691-11802-4").

[^8]: Tzon-Tzer, Lu; Sheng-Hua, Shiou (2002). "Inverses of 2 × 2 block matrices". *Computers & Mathematics with Applications*. **43** (1–2): 119–129. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S0898-1221(01)00278-4](https://doi.org/10.1016%2FS0898-1221%2801%2900278-4).

[^9]: Bernstein, Dennis (2005). *Matrix Mathematics*. Princeton University Press. p. 45. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-691-11802-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-691-11802-4 "Special:BookSources/978-0-691-11802-4").

[^10]: T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein, *Introduction to Algorithms*, 3rd ed., MIT Press, Cambridge, MA, 2009, §28.2.

[^11]: [Ran Raz](https://en.wikipedia.org/wiki/Ran_Raz "Ran Raz"). On the complexity of matrix product. In Proceedings of the thirty-fourth annual ACM symposium on Theory of computing. ACM Press, 2002. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/509907.509932](https://doi.org/10.1145%2F509907.509932).

[^12]: Stewart, Gilbert (1998). *Matrix Algorithms: Basic decompositions*. SIAM. p. 55. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-89871-414-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-89871-414-2 "Special:BookSources/978-0-89871-414-2").

[^13]: Haramoto, H.; Matsumoto, M. (2009). ["A p-adic algorithm for computing the inverse of integer matrices"](https://doi.org/10.1016%2Fj.cam.2008.07.044). *Journal of Computational and Applied Mathematics*. **225** (1): 320–322. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2009JCoAM.225..320H](https://ui.adsabs.harvard.edu/abs/2009JCoAM.225..320H). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.cam.2008.07.044](https://doi.org/10.1016%2Fj.cam.2008.07.044).

[^14]: ["IML - Integer Matrix Library"](https://cs.uwaterloo.ca/~astorjoh/iml.html). *cs.uwaterloo.ca*. Retrieved 14 April 2018.

[^15]: Weisstein, Eric W. ["Invertible Matrix Theorem"](https://mathworld.wolfram.com/InvertibleMatrixTheorem.html). *mathworld.wolfram.com*. Retrieved 2020-09-08.

[^16]: Horn, Roger A.; Johnson, Charles R. (1985). *Matrix Analysis*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press "Cambridge University Press"). p. 14. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-38632-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-38632-6 "Special:BookSources/978-0-521-38632-6")..

[^17]: Magnus, Jan R.; Neudecker, Heinz (1999). *Matrix Differential Calculus: with Applications in Statistics and Econometrics* (Revised ed.). New York: John Wiley & Sons. pp. 151–152. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-471-98633-X](https://en.wikipedia.org/wiki/Special:BookSources/0-471-98633-X "Special:BookSources/0-471-98633-X").

[^18]: [Roman, Stephen](https://en.wikipedia.org/wiki/Steven_Roman "Steven Roman") (2008), *Advanced Linear Algebra*, [Graduate Texts in Mathematics](https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics") (Third ed.), Springer, p. 446, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-72828-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-72828-5 "Special:BookSources/978-0-387-72828-5").

[^19]: Lin, Lin; Lu, Jianfeng; Ying, Lexing; Car, Roberto; E, Weinan (2009). ["Fast algorithm for extracting the diagonal of the inverse matrix with application to the electronic structure analysis of metallic systems"](https://doi.org/10.4310%2FCMS.2009.v7.n3.a12). *Communications in Mathematical Sciences*. **7** (3): 755–777. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.4310/CMS.2009.v7.n3.a12](https://doi.org/10.4310%2FCMS.2009.v7.n3.a12).

[^20]: Albreem, M.; Juntti, M.; Shahabuddin, S. (January 2020). "Efficient initialisation of iterative linear massive MIMO detectors using a stair matrix". *[Electronics Letters](https://en.wikipedia.org/wiki/Electronics_Letters "Electronics Letters")*. **56** (1): 50–52. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2020ElL....56...50A](https://ui.adsabs.harvard.edu/abs/2020ElL....56...50A). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1049/el.2019.2938](https://doi.org/10.1049%2Fel.2019.2938).