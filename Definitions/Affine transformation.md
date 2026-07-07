---
title: "Affine transformation"
source: "https://en.wikipedia.org/wiki/Affine_transformation"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2002-02-25
created: 2026-04-10
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Fractal_fern_explained.png/250px-Fractal_fern_explained.png)

An image of a fern-like fractal ( Barnsley's fern ) that exhibits affine self-similarity. Each of the leaves of the fern is related to each other leaf by an affine transformation. For instance, the red leaf can be transformed into both the dark blue leaf and any of the light blue leaves by a combination of reflection, rotation, scaling, and translation.

In [Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry "Euclidean geometry"), an **affine transformation** or **affinity** (from the Latin, *[affinis](https://en.wiktionary.org/wiki/affine "wikt:affine")*, "connected with") is a [geometric transformation](https://en.wikipedia.org/wiki/Geometric_transformation "Geometric transformation") that preserves [lines](https://en.wikipedia.org/wiki/Line_\(geometry\) "Line (geometry)") and [parallelism](https://en.wikipedia.org/wiki/Parallel_\(geometry\) "Parallel (geometry)"), but not necessarily [Euclidean distances](https://en.wikipedia.org/wiki/Euclidean_distance "Euclidean distance") and [angles](https://en.wikipedia.org/wiki/Angle "Angle").

More generally, an affine transformation is an [automorphism](https://en.wikipedia.org/wiki/Automorphism "Automorphism") of an [affine space](https://en.wikipedia.org/wiki/Affine_space "Affine space") (Euclidean spaces are specific affine spaces), that is, a [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)") which [maps](https://en.wikipedia.org/wiki/Map_\(mathematics\) "Map (mathematics)") an affine space onto itself while preserving both the [dimension](https://en.wikipedia.org/wiki/Dimension "Dimension") of any [affine subspaces](https://en.wikipedia.org/wiki/Affine_subspace "Affine subspace") (meaning that it sends points to points, lines to lines, planes to planes, and so on) and the ratios of the lengths of [parallel](https://en.wikipedia.org/wiki/Parallel_\(geometry\) "Parallel (geometry)") line segments. Consequently, sets of parallel affine subspaces remain parallel after an affine transformation. An affine transformation does not necessarily preserve angles between lines or distances between points, though it does preserve ratios of distances between points lying on a straight line.

If X is the point set of an affine space, then every affine transformation on X can be represented as the [composition](https://en.wikipedia.org/wiki/Function_composition "Function composition") of a [linear transformation](https://en.wikipedia.org/wiki/Linear_transformation "Linear transformation") on X and a [translation](https://en.wikipedia.org/wiki/Translation_\(geometry\) "Translation (geometry)") of X. Unlike a purely linear transformation, an affine transformation need not preserve the origin of the affine space. Thus, every linear transformation is affine, but not every affine transformation is linear.

Examples of affine transformations include translation, [scaling](https://en.wikipedia.org/wiki/Scaling_\(geometry\) "Scaling (geometry)"), [homothety](https://en.wikipedia.org/wiki/Homothety "Homothety"), [similarity](https://en.wikipedia.org/wiki/Similarity_\(geometry\) "Similarity (geometry)"), [reflection](https://en.wikipedia.org/wiki/Reflection_\(mathematics\) "Reflection (mathematics)"), [rotation](https://en.wikipedia.org/wiki/Rotation_\(mathematics\) "Rotation (mathematics)"), [hyperbolic rotation](https://en.wikipedia.org/wiki/Hyperbolic_rotation "Hyperbolic rotation"), [shear mapping](https://en.wikipedia.org/wiki/Shear_mapping "Shear mapping"), and compositions of them in any combination and sequence.

Viewing an affine space as the complement of a [hyperplane at infinity](https://en.wikipedia.org/wiki/Hyperplane_at_infinity "Hyperplane at infinity") of a [projective space](https://en.wikipedia.org/wiki/Projective_space "Projective space"), the affine transformations are the [projective transformations](https://en.wikipedia.org/wiki/Projective_transformation "Projective transformation") of that projective space that leave the hyperplane at infinity [invariant](https://en.wikipedia.org/wiki/Invariant_\(mathematics\) "Invariant (mathematics)"), restricted to the complement of that hyperplane.

A [generalization](https://en.wikipedia.org/wiki/Generalization "Generalization") of an affine transformation is an **affine map** [^1] (or **affine homomorphism** or **affine mapping**) between two (potentially different) affine spaces over the same [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") k. Let (*X*, *V*, *k*) and (*Z*, *W*, *k*) be two affine spaces with X and Z the point sets and V and W the respective associated [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space") over the field k. A map *f*: *X* → *Z* is an affine map if there exists a [linear map](https://en.wikipedia.org/wiki/Linear_map "Linear map") *m* <sub><i>f</i></sub>: *V* → *W* such that *m* <sub><i>f</i></sub> (*x* − *y*) = *f* (*x*) − *f* (*y*) for all x, y in X.[^2]

## Definition

Let X be an affine space over a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") k, and V be its associated vector space. An **affine transformation** is a [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") f from X onto itself that is an [affine map](https://en.wikipedia.org/wiki/Affine_space#Affine_map "Affine space"); this means that a [linear map](https://en.wikipedia.org/wiki/Linear_map "Linear map") g from V to V is well defined by the equation ${\displaystyle g(y-x)=f(y)-f(x);}$ here, as usual, the subtraction of two points denotes the [free vector](https://en.wikipedia.org/wiki/Free_vector "Free vector") from the second point to the first one, and " [well-defined](https://en.wikipedia.org/wiki/Well-defined "Well-defined") " means that ${\displaystyle y-x=y'-x'}$ implies that ${\displaystyle f(y)-f(x)=f(y')-f(x').}$

If the dimension of X is at least two, a *semiaffine transformation* f of X is a [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") from X onto itself satisfying:[^3]

1. For every *d* -dimensional [affine subspace](https://en.wikipedia.org/wiki/Affine_subspace "Affine subspace") S of X, then *f* (*S*) is also a *d* -dimensional affine subspace of X.
2. If S and T are parallel affine subspaces of X, then *f* (*S*) and *f* (*T*) are parallel.

These two conditions are satisfied by affine transformations, and express what is precisely meant by the expression that "f preserves parallelism".

These conditions are not independent as the second follows from the first.[^4] Furthermore, if the field k has at least three elements, the first condition can be simplified to: f is a [collineation](https://en.wikipedia.org/wiki/Collineation "Collineation"), that is, it maps lines to lines.[^5]

## Structure

By the definition of an affine space, V acts on X, so that, for every pair ${\displaystyle (x,\mathbf {v} )}$ in *X* × *V* there is associated a point y in X. We can denote this action by ${\displaystyle {\vec {v}}(x)=y}$. Here we use the convention that ${\displaystyle {\vec {v}}={\textbf {v}}}$ are two interchangeable notations for an element of V. By fixing a point c in X one can define a function *m* <sub><i>c</i></sub>: *X* → *V* by *m* <sub><i>c</i></sub> (*x*) = *cx* →. For any c, this function is one-to-one, and so, has an inverse function *m* <sub><i>c</i></sub> <sup>−1</sup>: *V* → *X* given by ${\displaystyle m_{c}^{-1}({\textbf {v}})={\vec {v}}(c)}$. These functions can be used to turn X into a vector space (with respect to the point c) by defining:[^6]

- ${\displaystyle x+y=m_{c}^{-1}\left(m_{c}(x)+m_{c}(y)\right),{\text{ for all }}x,y{\text{ in }}X,}$ and
- ${\displaystyle rx=m_{c}^{-1}\left(rm_{c}(x)\right),{\text{ for all }}r{\text{ in }}k{\text{ and }}x{\text{ in }}X.}$

This vector space has origin c and formally needs to be distinguished from the affine space X, but common practice is to denote it by the same symbol and mention that it is a vector space *after* an origin has been specified. This identification permits points to be viewed as vectors and vice versa.

For any [linear transformation](https://en.wikipedia.org/wiki/Linear_transformation "Linear transformation") λ of V, we can define the function *L* (*c*, *λ*): *X* → *X* by 
$$
{\displaystyle L(c,\lambda )(x)=m_{c}^{-1}\left(\lambda (m_{c}(x))\right)=c+\lambda ({\vec {cx}}).}
$$

Then *L* (*c*, *λ*) is an affine transformation of X which leaves the point c fixed.[^7] It is a linear transformation of X, viewed as a vector space with origin c.

Let σ be any affine transformation of X. Pick a point c in X and consider the translation of X by the vector ${\displaystyle {\mathbf {w}}={\overrightarrow {c\sigma (c)}}}$, denoted by *T* <sub><b>w</b></sub>. Translations are affine transformations and the composition of affine transformations is an affine transformation. For this choice of c, there exists a unique linear transformation λ of V such that [^8] 
$$
{\displaystyle \sigma (x)=T_{\mathbf {w}}\left(L(c,\lambda )(x)\right).}
$$
 That is, an arbitrary affine transformation of X is the composition of a linear transformation of X (viewed as a vector space) and a translation of X.

This representation of affine transformations is often taken as the definition of an affine transformation (with the choice of origin being implicit).[^9] [^10] [^11]

## Representation

As shown above, an affine map is the composition of two functions: a translation and a linear map. Ordinary vector algebra uses [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication "Matrix multiplication") to represent linear maps, and [vector addition](https://en.wikipedia.org/wiki/Vector_addition "Vector addition") to represent translations. Formally, in the finite-dimensional case, if the linear map is represented as a multiplication by an invertible matrix ${\displaystyle A}$ and the translation as the addition of a vector ${\displaystyle \mathbf {b} }$, an affine map ${\displaystyle f}$ acting on a vector ${\displaystyle \mathbf {x} }$ can be represented as

$$
{\displaystyle \mathbf {y} =f(\mathbf {x} )=A\mathbf {x} +\mathbf {b} .}
$$

### Augmented matrix

<video width="250" height="250" controls=""></video>

Affine transformations on the 2D plane can be performed by linear transformations in three dimensions. Translation is done by shearing along over the z axis, and rotation is performed around the z axis.

Using an [augmented matrix](https://en.wikipedia.org/wiki/Augmented_matrix "Augmented matrix") and an augmented vector, it is possible to represent both the translation and the linear map using a single [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication "Matrix multiplication"). The technique requires that all vectors be augmented with a "1" at the end, and all matrices be augmented with an extra row of zeros at the bottom, an extra column—the translation vector—to the right, and a "1" in the lower right corner. If ${\displaystyle A}$ is a matrix,

$$
{\displaystyle {\begin{bmatrix}\mathbf {y} \\1\end{bmatrix}}=\left[{\begin{array}{ccc|c}&A&&\mathbf {b} \\0&\cdots &0&1\end{array}}\right]{\begin{bmatrix}\mathbf {x} \\1\end{bmatrix}}}
$$

is equivalent to the following

$$
{\displaystyle \mathbf {y} =A\mathbf {x} +\mathbf {b} .}
$$

The above-mentioned augmented matrix is called an *[affine transformation matrix](https://en.wikipedia.org/wiki/Transformation_matrix#Affine_transformations "Transformation matrix")*. In the general case, when the last row vector is not restricted to be ${\displaystyle \left[{\begin{array}{ccc|c}0&\cdots &0&1\end{array}}\right]}$, the matrix becomes a *projective transformation matrix* (as it can also be used to perform [projective transformations](https://en.wikipedia.org/wiki/Projective_transformation "Projective transformation")).

This representation exhibits the [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") of all [invertible](https://en.wikipedia.org/wiki/Inverse_function "Inverse function") affine transformations as the [semidirect product](https://en.wikipedia.org/wiki/Semidirect_product "Semidirect product") of ${\displaystyle K^{n}}$ and ${\displaystyle \operatorname {GL} (n,K)}$. This is a [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)") under the operation of composition of functions, called the [affine group](https://en.wikipedia.org/wiki/Affine_group "Affine group").

Ordinary matrix-vector multiplication always maps the origin to the origin, and could therefore never represent a translation, in which the origin must necessarily be mapped to some other point. By appending the additional coordinate "1" to every vector, one essentially considers the space to be mapped as a subset of a space with an additional dimension. In that space, the original space occupies the subset in which the additional coordinate is 1. Thus the origin of the original space can be found at ${\displaystyle (0,0,\dotsc ,0,1)}$. A translation within the original space by means of a linear transformation of the higher-dimensional space is then possible (specifically, a shear transformation). The coordinates in the higher-dimensional space are an example of [homogeneous coordinates](https://en.wikipedia.org/wiki/Homogeneous_coordinates "Homogeneous coordinates"). If the original space is [Euclidean](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space"), the higher dimensional space is a [real projective space](https://en.wikipedia.org/wiki/Real_projective_space "Real projective space").

The advantage of using homogeneous coordinates is that one can [combine](https://en.wikipedia.org/wiki/Function_composition "Function composition") any number of affine transformations into one by multiplying the respective matrices. This property is used extensively in [computer graphics](https://en.wikipedia.org/wiki/Computer_graphics "Computer graphics"), [computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision") and [robotics](https://en.wikipedia.org/wiki/Robotics "Robotics").

#### Example augmented matrix

Suppose you have three points that define a non-degenerate triangle in a plane, or four points that define a non-degenerate tetrahedron in 3-dimensional space, or generally *n* + 1 points **x** <sub>1</sub>,..., **x** <sub><i>n</i> +1</sub> that define a non-degenerate [simplex](https://en.wikipedia.org/wiki/Simplex "Simplex") in n-dimensional space. Suppose you have corresponding destination points **y** <sub>1</sub>,..., **y** <sub><i>n</i> +1</sub>, where these new points can lie in a space with any number of dimensions. (Furthermore, the new points need not form a non-degenerate simplex, nor even be distinct from each other.) The unique augmented matrix M that achieves the affine transformation 
$$
{\displaystyle {\begin{bmatrix}\mathbf {y} _{i}\\1\end{bmatrix}}=M{\begin{bmatrix}\mathbf {x} _{i}\\1\end{bmatrix}}}
$$
 for every i is 
$$
{\displaystyle M={\begin{bmatrix}\mathbf {y} _{1}&\cdots &\mathbf {y} _{n+1}\\1&\cdots &1\end{bmatrix}}{\begin{bmatrix}\mathbf {x} _{1}&\cdots &\mathbf {x} _{n+1}\\1&\cdots &1\end{bmatrix}}^{-1},}
$$
 using [matrix inversion](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix").

## Properties

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Hyperbolic_rotation.gif/250px-Hyperbolic_rotation.gif)

The one-parameter group of squeeze mappings preserves areas, here illustrated with hyperbolic sectors.

### Properties preserved

An affine transformation preserves:

1. [collinearity](https://en.wikipedia.org/wiki/Collinearity "Collinearity") between points: three or more points which lie on the same line (called collinear points) continue to be collinear after the transformation.
2. [parallelism](https://en.wikipedia.org/wiki/Parallel_\(geometry\) "Parallel (geometry)"): two or more lines which are parallel, continue to be parallel after the transformation.
3. [convexity](https://en.wikipedia.org/wiki/Convex_set "Convex set") of sets: a convex set continues to be convex after the transformation. Moreover, the [extreme points](https://en.wikipedia.org/wiki/Extreme_point "Extreme point") of the original set are mapped to the extreme points of the transformed set.[^12]
4. ratios of lengths of parallel line segments: for distinct parallel segments defined by points ${\displaystyle p_{1},p_{2}}$ and ${\displaystyle p_{3},p_{4}}$, respectively, the ratio of ${\displaystyle {\overrightarrow {p_{1}p_{2}}}}$ to ${\displaystyle {\overrightarrow {p_{3}p_{4}}}}$ is the same as that of ${\displaystyle {\overrightarrow {f(p_{1})f(p_{2})}}}$ to ${\displaystyle {\overrightarrow {f(p_{3})f(p_{4})}}}$.
5. [barycenters](https://en.wikipedia.org/wiki/Barycentric_coordinate_system "Barycentric coordinate system") of weighted collections of points.

### Groups

As an affine transformation is [invertible](https://en.wikipedia.org/wiki/Invertible_function "Invertible function"), the [square matrix](https://en.wikipedia.org/wiki/Square_matrix "Square matrix") ${\displaystyle A}$ appearing in its [matrix representation](#Representation) is [invertible](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix"). The matrix representation of the inverse transformation is thus 
$$
{\displaystyle \left[{\begin{array}{ccc|c}&A^{-1}&&-A^{-1}{\vec {b}}\ \\0&\ldots &0&1\end{array}}\right].}
$$

The invertible affine transformations (of an affine space onto itself) form the [affine group](https://en.wikipedia.org/wiki/Affine_group "Affine group"), which has the [general linear group](https://en.wikipedia.org/wiki/General_linear_group "General linear group") of degree ${\displaystyle n}$ as subgroup and is itself a subgroup of the general linear group of degree ${\displaystyle n+1}$.

The [similarity transformations](https://en.wikipedia.org/wiki/Similarity_transformation_\(geometry\) "Similarity transformation (geometry)") form the subgroup where ${\displaystyle A}$ is a scalar times an [orthogonal matrix](https://en.wikipedia.org/wiki/Orthogonal_matrix "Orthogonal matrix"). For example, if the affine transformation acts on the plane and if the [determinant](https://en.wikipedia.org/wiki/Determinant "Determinant") of ${\displaystyle A}$ is 1 or −1 then the transformation is an [equiareal mapping](https://en.wikipedia.org/wiki/Equiareal_map "Equiareal map"). Such transformations form a subgroup called the *equi-affine group*.[^13] A transformation that is both equi-affine and a similarity is an [isometry](https://en.wikipedia.org/wiki/Isometry "Isometry") of the plane taken with [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance "Euclidean distance").

Each of these groups has a subgroup of *[orientation](https://en.wikipedia.org/wiki/Orientability "Orientability") -preserving* or *positive* affine transformations: those where the determinant of ${\displaystyle A}$ is positive. In the last case this is in 3D the group of [rigid transformations](https://en.wikipedia.org/wiki/Rigid_transformation "Rigid transformation") ([proper rotations](https://en.wikipedia.org/wiki/Improper_rotation "Improper rotation") and pure translations).

If there is a fixed point, we can take that as the origin, and the affine transformation reduces to a linear transformation. This may make it easier to classify and understand the transformation. For example, describing a transformation as a rotation by a certain angle with respect to a certain axis may give a clearer idea of the overall behavior of the transformation than describing it as a combination of a translation and a rotation. However, this depends on application and context.

## Affine maps

An affine map ${\displaystyle f\colon {\mathcal {A}}\to {\mathcal {B}}}$ between two [affine spaces](https://en.wikipedia.org/wiki/Affine_space "Affine space") is a map on the points that acts [linearly](https://en.wikipedia.org/wiki/Linear_transformation "Linear transformation") on the vectors (that is, the vectors between points of the space). In symbols, *${\displaystyle f}$* determines a linear transformation *${\displaystyle \varphi }$* such that, for any pair of points ${\displaystyle P,Q\in {\mathcal {A}}}$:

$$
{\displaystyle {\overrightarrow {f(P)~f(Q)}}=\varphi ({\overrightarrow {PQ}})}
$$
 or 
$$
{\displaystyle f(Q)-f(P)=\varphi (Q-P).}
$$

We can interpret this definition in a few other ways, as follows.

If an origin ${\displaystyle O\in {\mathcal {A}}}$ is chosen, and ${\displaystyle B}$ denotes its image ${\displaystyle f(O)\in {\mathcal {B}}}$, then this means that for any vector ${\displaystyle {\vec {x}}}$:

$$
{\displaystyle f\colon (O+{\vec {x}})\mapsto (B+\varphi ({\vec {x}})).}
$$

If an origin ${\displaystyle O'\in {\mathcal {B}}}$ is also chosen, this can be decomposed as an affine transformation ${\displaystyle g\colon {\mathcal {A}}\to {\mathcal {B}}}$ that sends ${\displaystyle O\mapsto O'}$, namely

$$
{\displaystyle g\colon (O+{\vec {x}})\mapsto (O'+\varphi ({\vec {x}})),}
$$
 followed by the translation by a vector ${\displaystyle {\vec {b}}={\overrightarrow {O'B}}}$.

The conclusion is that, intuitively, ${\displaystyle f}$ consists of a translation and a linear map.

### Alternative definition

Given two [affine spaces](https://en.wikipedia.org/wiki/Affine_space "Affine space") ${\displaystyle {\mathcal {A}}}$ and ${\displaystyle {\mathcal {B}}}$, over the same field, a function ${\displaystyle f\colon {\mathcal {A}}\to {\mathcal {B}}}$ is an affine map [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") for every family ${\displaystyle \{(P_{i},\lambda _{i})\}_{i\in I}}$ of weighted points in ${\displaystyle {\mathcal {A}}}$ such that 
$$
{\displaystyle \sum _{i\in I}\lambda _{i}=1,}
$$
 we have [^14] 
$$
{\displaystyle f\left(\sum _{i\in I}\lambda _{i}P_{i}\right)=\sum _{i\in I}\lambda _{i}f(P_{i}).}
$$
 In other words, ${\displaystyle f}$ preserves [barycenters](https://en.wikipedia.org/wiki/Barycentric_coordinate_system "Barycentric coordinate system").

### Example

Let ${\displaystyle {\mathcal {A}}}$ be the [three-dimensional Euclidean space](https://en.wikipedia.org/wiki/Three-dimensional_Euclidean_space "Three-dimensional Euclidean space"), ${\displaystyle {\mathcal {B}}\subseteq {\mathcal {A}}}$ a [plane](https://en.wikipedia.org/wiki/Three-dimensional_Euclidean_space#Lines_and_planes "Three-dimensional Euclidean space"), and both be equipped with a [Cartesian coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system "Cartesian coordinate system"). If ${\displaystyle f\colon \,{\mathcal {A}}\to {\mathcal {B}}}$ is a [parallel projection](https://en.wikipedia.org/wiki/Parallel_projection "Parallel projection") or, more generally, is generated by an [axonometry](https://en.wikipedia.org/wiki/Axonometry "Axonometry"), then ${\displaystyle f}$ is affine and [surjective](https://en.wikipedia.org/wiki/Surjective "Surjective"). Hence it can be represented by 
$$
{\displaystyle {\begin{bmatrix}x\\y\\z\end{bmatrix}}\longmapsto {\begin{bmatrix}x'\\y'\end{bmatrix}}=A{\begin{bmatrix}x\\y\\z\end{bmatrix}}+\,b}
$$
 with a [matrix](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)") ${\displaystyle A\in \mathbb {R} ^{2\times 3}}$ of [rank](https://en.wikipedia.org/wiki/Rank_\(linear_algebra\) "Rank (linear algebra)") 2 and a [column vector](https://en.wikipedia.org/wiki/Column_vector "Column vector") ${\displaystyle b\in \mathbb {R} ^{2}.}$ In case ${\displaystyle b=(0,0)^{\mathsf {T}},}$ this is treated in more detail in the [section Coordinate calculation](https://en.wikipedia.org/wiki/Axonometry#Coordinate_calculation "Axonometry") at Axonometry.

## History

The word "affine" as a mathematical term is defined in connection with tangents to curves in [Euler](https://en.wikipedia.org/wiki/Leonhard_Euler "Leonhard Euler") 's 1748 [Introductio in analysin infinitorum](https://en.wikipedia.org/wiki/Introductio_in_analysin_infinitorum "Introductio in analysin infinitorum").[^15] [Felix Klein](https://en.wikipedia.org/wiki/Felix_Klein "Felix Klein") attributes the term "affine transformation" to [Möbius](https://en.wikipedia.org/wiki/August_Ferdinand_M%C3%B6bius "August Ferdinand Möbius") and [Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss "Carl Friedrich Gauss").[^10]

## Image transformation

In their applications to [digital image processing](https://en.wikipedia.org/wiki/Digital_image_processing "Digital image processing"), the affine transformations are analogous to printing on a sheet of rubber and stretching the sheet's edges parallel to the plane. This transform relocates pixels requiring intensity interpolation to approximate the value of moved pixels, bicubic [interpolation](https://en.wikipedia.org/wiki/Interpolation "Interpolation") is the standard for image transformations in image processing applications. Affine transformations scale, rotate, translate, mirror and shear images as shown in the following examples:[^16]

| Transformation name | Affine matrix | Example |
| --- | --- | --- |
| **[Identity](https://en.wikipedia.org/wiki/Identity_operation "Identity operation")** (transform to original image) | ${\displaystyle {\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Checkerboard_identity.svg/250px-Checkerboard_identity.svg.png) |
| **[Translation](https://en.wikipedia.org/wiki/Translation_\(geometry\) "Translation (geometry)")** | ${\displaystyle {\begin{bmatrix}1&0&v_{x}>0\\0&1&v_{y}=0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Checkerboard_identity.svg/250px-Checkerboard_identity.svg.png) |
| **[Reflection](https://en.wikipedia.org/wiki/Reflection_\(mathematics\) "Reflection (mathematics)")** | ${\displaystyle {\begin{bmatrix}-1&0&0\\0&1&0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Checkerboard_reflection.svg/250px-Checkerboard_reflection.svg.png) |
| **[Scale](https://en.wikipedia.org/wiki/Scaling_\(geometry\) "Scaling (geometry)")** | ${\displaystyle {\begin{bmatrix}c_{x}=2&0&0\\0&c_{y}=1&0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Checkerboard_scale.svg/250px-Checkerboard_scale.svg.png) |
| **[Rotate](https://en.wikipedia.org/wiki/Rotate "Rotate")** | ${\displaystyle {\begin{bmatrix}\cos(\theta )&-\sin(\theta )&0\\\sin(\theta )&\cos(\theta )&0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Checkerboard_rotate.svg/250px-Checkerboard_rotate.svg.png)   where *θ* = ⁠π6⁠ =30° |
| **[Shear](https://en.wikipedia.org/wiki/Shear_matrix "Shear matrix")** | ${\displaystyle {\begin{bmatrix}1&c_{x}=0.5&0\\c_{y}=0&1&0\\0&0&1\end{bmatrix}}}$ | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Checkerboard_shear.svg/250px-Checkerboard_shear.svg.png) |

The affine transforms are applicable to the registration process where two or more images are aligned (registered). An example of [image registration](https://en.wikipedia.org/wiki/Image_registration "Image registration") is the generation of panoramic images that are the product of multiple images [stitched](https://en.wikipedia.org/wiki/Image_stitching "Image stitching") together.

### Affine warping

The affine transform preserves parallel lines. However, the stretching and shearing transformations warp shapes, as the following example shows:

| ![](https://upload.wikimedia.org/wikipedia/en/a/a7/White_on_black_circle_image_256_by_256.png) | ![](https://upload.wikimedia.org/wikipedia/en/7/7a/Affine_transform_sheared_circle.png) |
| --- | --- |

This is an example of image warping. However, the affine transformations do not facilitate projection onto a curved surface or [radial distortions](https://en.wikipedia.org/wiki/Distortion_\(optics\) "Distortion (optics)").

## In the plane

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Central_dilation.svg/330px-Central_dilation.svg.png)

A homothety. The triangles A 1 B Z, B C Z, and A Z get mapped to A 2 Z, respectively.

Every affine transformations in a [Euclidean plane](https://en.wikipedia.org/wiki/Euclidean_plane "Euclidean plane") is the composition of a [translation](https://en.wikipedia.org/wiki/Translation_\(geometry\) "Translation (geometry)") and an affine transformation that fixes a point; the latter may be

- a [homothety](https://en.wikipedia.org/wiki/Homothety "Homothety"),
- [rotations](https://en.wikipedia.org/wiki/Rotation "Rotation") around the fixed point,
- a [scaling](https://en.wikipedia.org/wiki/Scaling_\(geometry\) "Scaling (geometry)"), with possibly negative scaling factors, in two directions (not necessarily perpendicular); this includes [reflections](https://en.wikipedia.org/wiki/Reflection_\(mathematics\) "Reflection (mathematics)"),
- a [shear mapping](https://en.wikipedia.org/wiki/Shear_mapping "Shear mapping")
- a [squeeze mapping](https://en.wikipedia.org/wiki/Squeeze_mapping "Squeeze mapping").

Given two non-degenerate [triangles](https://en.wikipedia.org/wiki/Triangle "Triangle") *ABC* and *A′B′C′* in a Euclidean plane, there is a unique affine transformation *T* that maps *A* to *A′*, *B* to *B′* and *C* to *C′*. Each of *ABC* and *A′B′C′* defines an [affine coordinate system](https://en.wikipedia.org/wiki/Affine_coordinate_system "Affine coordinate system") and a [barycentric coordinate system](https://en.wikipedia.org/wiki/Barycentric_coordinate_system "Barycentric coordinate system"). Given a point *P*, the point *T* (P) is the point that has the same coordinates on the second system as the coordinates of *P* on the first system.

Affine transformations do not respect lengths or angles; they multiply areas by the constant factor

area of *A′B′C′* / area of *ABC*.

A given *T* may either be *direct* (respect orientation), or *indirect* (reverse orientation), and this may be determined by comparing the orientations of the triangles.

## Examples

### Over the real numbers

The functions ${\displaystyle f\colon \mathbb {R} \to \mathbb {R} ,\;f(x)=mx+c}$ with ${\displaystyle m}$ and ${\displaystyle c}$ in ${\displaystyle \mathbb {R} }$ and ${\displaystyle m\neq 0}$, are precisely the affine transformations of the [real line](https://en.wikipedia.org/wiki/Real_line "Real line").

### In plane geometry

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Geometric_affine_transformation_example.png/250px-Geometric_affine_transformation_example.png)

A simple affine transformation on the real plane

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/2D_affine_transformation_matrix.svg/250px-2D_affine_transformation_matrix.svg.png)

Effect of applying various 2D affine transformation matrices on a unit square. Note that the reflection matrices are special cases of the scaling matrix.

In ${\displaystyle \mathbb {R} ^{2}}$, the transformation shown at left is accomplished using the map given by:

$$
{\displaystyle {\begin{bmatrix}x\\y\end{bmatrix}}\mapsto {\begin{bmatrix}0&1\\2&1\end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}+{\begin{bmatrix}-100\\-100\end{bmatrix}}}
$$

Transforming the three corner points of the original triangle (in red) gives three new points which form the new triangle (in blue). This transformation skews and translates the original triangle.

In fact, all triangles are related to one another by affine transformations. This is also true for all parallelograms, but not for all quadrilaterals.

[^1]: [Berger 1987](#CITEREFBerger1987), p. 38.

[^2]: [Samuel 1988](#CITEREFSamuel1988), p. 11.

[^3]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 65.

[^4]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 66.

[^5]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 69.

[^6]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 59.

[^7]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 76,87.

[^8]: [Snapper & Troyer 1989](#CITEREFSnapperTroyer1989), p. 86.

[^9]: [Wan 1993](#CITEREFWan1993), pp. 19–20.

[^10]: [Klein 1948](#CITEREFKlein1948), p. 70.

[^11]: [Brannan, Esplen & Gray 1999](#CITEREFBrannanEsplenGray1999), p. 53.

[^12]: Reinhard Schultz. ["Affine transformations and convexity"](http://math.ucr.edu/~res/math145A-2014/affine+convex.pdf) (PDF). Retrieved 27 February 2017.

[^13]: [Oswald Veblen](https://en.wikipedia.org/wiki/Oswald_Veblen "Oswald Veblen") (1918) *Projective Geometry*, volume 2, pp. 105–7.

[^14]: Schneider, Philip K.; Eberly, David H. (2003). [*Geometric Tools for Computer Graphics*](https://books.google.com/books?id=3Q7HGBx1uLIC&pg=PA98). Morgan Kaufmann. p. 98. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-55860-594-7](https://en.wikipedia.org/wiki/Special:BookSources/978-1-55860-594-7 "Special:BookSources/978-1-55860-594-7").

[^15]: Euler, Leonhard (1748). [*Introductio in analysin infinitorum*](https://gallica.bnf.fr/ark:/12148/bpt6k33529/f240.image) (in Latin). Vol. II. Book II, sect. XVIII, art. 442

[^16]: Gonzalez, Rafael (2008). *'Digital Image Processing, 3rd'*. Pearson Hall. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780131687288](https://en.wikipedia.org/wiki/Special:BookSources/9780131687288 "Special:BookSources/9780131687288").