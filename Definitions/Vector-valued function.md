---
title: "Vector-valued function"
source: "https://en.wikipedia.org/wiki/Vector-valued_function"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2006-01-10
created: 2026-04-10
description:
tags:
  - "clippings"
---
A **vector-valued function**, also referred to as a **vector function**, is a [mathematical function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)") of one or more [variables](https://en.wikipedia.org/wiki/Variable_\(mathematics\) "Variable (mathematics)") whose [range](https://en.wikipedia.org/wiki/Range_of_a_function "Range of a function") is a set of multidimensional [vectors](https://en.wikipedia.org/wiki/Vector_\(mathematics_and_physics\) "Vector (mathematics and physics)") or [infinite-dimensional vectors](https://en.wikipedia.org/wiki/Infinite-dimensional-vector-valued_function "Infinite-dimensional-vector-valued function"). The input of a vector-valued function could be a scalar or a vector (that is, the [dimension](https://en.wikipedia.org/wiki/Dimension "Dimension") of the [domain](https://en.wikipedia.org/wiki/Domain_of_a_function "Domain of a function") could be 1 or greater than 1); the dimension of the function's domain has no relation to the dimension of its range.

## Example: Helix

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Vector-valued_function-2.png/330px-Vector-valued_function-2.png)

A graph of the vector-valued function r ( z ) = ⟨2 cos, 4 sin, ⟩ indicating a range of solutions and the vector when evaluated near = 19.5

A common example of a vector-valued function is one that depends on a single [real](https://en.wikipedia.org/wiki/Real_number "Real number") parameter t, often representing [time](https://en.wikipedia.org/wiki/Time "Time"), producing a [vector](https://en.wikipedia.org/wiki/Euclidean_vector "Euclidean vector") **v** (*t*) as the result. In terms of the standard [unit vectors](https://en.wikipedia.org/wiki/Unit_vector "Unit vector") **i**, **j**, **k** of [Cartesian 3-space](https://en.wikipedia.org/wiki/Cartesian_space "Cartesian space"), these specific types of vector-valued functions are given by expressions such as 
$$
{\displaystyle \mathbf {r} (t)=f(t)\mathbf {i} +g(t)\mathbf {j} +h(t)\mathbf {k} }
$$
 where *f* (*t*), *g* (*t*) and *h* (*t*) are the **coordinate functions** of the parameter t, and the domain of this vector-valued function is the [intersection](https://en.wikipedia.org/wiki/Intersection_\(set_theory\) "Intersection (set theory)") of the domains of the functions *f*, *g*, and *h*. It can also be referred to in a different notation: 
$$
{\displaystyle \mathbf {r} (t)=\langle f(t),g(t),h(t)\rangle }
$$
 The vector **r** (*t*) has its tail at the origin and its head at the coordinates evaluated by the function.

The vector shown in the graph to the right is the evaluation of the function ${\displaystyle \langle 2\cos t,\,4\sin t,\,t\rangle }$ near *t* = 19.5 (between 6π and 6.5π; i.e., somewhat more than 3 rotations). The [helix](https://en.wikipedia.org/wiki/Helix "Helix") is the path traced by the tip of the vector as t increases from zero through 8 *π*.

In 2D, we can analogously speak about vector-valued functions as: 
$$
{\displaystyle \mathbf {r} (t)=f(t)\mathbf {i} +g(t)\mathbf {j} }
$$
 or 
$$
{\displaystyle \mathbf {r} (t)=\langle f(t),g(t)\rangle }
$$

## Linear case

In the [linear](https://en.wikipedia.org/wiki/Linear_map "Linear map") case the function can be expressed in terms of [matrices](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)"): 
$$
{\displaystyle \mathbf {y} =A\mathbf {x} ,}
$$
 where **y** is an *n* × 1 output vector, **x** is a *k* × 1 vector of inputs, and *A* is an *n* × *k* matrix of [parameters](https://en.wikipedia.org/wiki/Parameter "Parameter"). Closely related is the affine case (linear up to a [translation](https://en.wikipedia.org/wiki/Translation_\(geometry\) "Translation (geometry)")) where the function takes the form 
$$
{\displaystyle \mathbf {y} =A\mathbf {x} +\mathbf {b} ,}
$$
 where in addition *b''* is an *n* × 1 vector of parameters.

The linear case arises often, for example in [multiple regression](https://en.wikipedia.org/wiki/Multiple_regression "Multiple regression"), where for instance the *n* × 1 vector ${\displaystyle {\hat {y}}}$ of predicted values of a [dependent variable](https://en.wikipedia.org/wiki/Dependent_variable "Dependent variable") is expressed linearly in terms of a *k* × 1 vector ${\displaystyle {\hat {\boldsymbol {\beta }}}}$ (*k* < *n*) of estimated values of model parameters: 
$$
{\displaystyle {\hat {\mathbf {y} }}=X{\hat {\boldsymbol {\beta }}},}
$$
 in which *X* (playing the role of *A* in the previous generic form) is an *n* × *k* matrix of fixed (empirically based) numbers.

## Parametric representation of a surface

A [surface](https://en.wikipedia.org/wiki/Surface_\(mathematics\) "Surface (mathematics)") is a 2-dimensional set of points embedded in (most commonly) 3-dimensional space. One way to represent a surface is with [parametric equations](https://en.wikipedia.org/wiki/Parametric_equation "Parametric equation"), in which two parameters s and t determine the three [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinates "Cartesian coordinates") of any point on the surface: 
$$
{\displaystyle (x,y,z)=(f(s,t),g(s,t),h(s,t))\equiv \mathbf {F} (s,t).}
$$
 Here **F** is a vector-valued function. For a surface embedded in n-dimensional space, one similarly has the representation 
$$
{\displaystyle (x_{1},x_{2},\dots ,x_{n})=(f_{1}(s,t),f_{2}(s,t),\dots ,f_{n}(s,t))\equiv \mathbf {F} (s,t).}
$$

## Derivative of a three-dimensional vector function

Many vector-valued functions, like [scalar-valued functions](https://en.wikipedia.org/wiki/Scalar-valued_function "Scalar-valued function"), can be [differentiated](https://en.wikipedia.org/wiki/Derivative "Derivative") by simply differentiating the components in the Cartesian coordinate system. Thus, if 
$$
{\displaystyle \mathbf {r} (t)=f(t)\mathbf {i} +g(t)\mathbf {j} +h(t)\mathbf {k} }
$$
 is a vector-valued function, then 
$$
{\displaystyle {\frac {d\mathbf {r} }{dt}}=f'(t)\mathbf {i} +g'(t)\mathbf {j} +h'(t)\mathbf {k} .}
$$
 The vector derivative admits the following physical interpretation: if **r** (*t*) represents the [position](https://en.wikipedia.org/wiki/Position_\(vector\) "Position (vector)") of a particle, then the derivative is the [velocity](https://en.wikipedia.org/wiki/Velocity "Velocity") of the particle 
$$
{\displaystyle \mathbf {v} (t)={\frac {d\mathbf {r} }{dt}}.}
$$
 Likewise, the derivative of the velocity is the [acceleration](https://en.wikipedia.org/wiki/Acceleration "Acceleration") 
$$
{\displaystyle {\frac {d\mathbf {v} }{dt}}=\mathbf {a} (t).}
$$

### Partial derivative

The [partial derivative](https://en.wikipedia.org/wiki/Partial_derivative "Partial derivative") of a vector function **a** with respect to a scalar variable q is defined as [^2] 
$$
{\displaystyle {\frac {\partial \mathbf {a} }{\partial q}}=\sum _{i=1}^{n}{\frac {\partial a_{i}}{\partial q}}\mathbf {e} _{i}}
$$
 where *a* <sub><i>i</i></sub> is the *scalar component* of **a** in the direction of **e** <sub><i>i</i></sub>. It is also called the [direction cosine](https://en.wikipedia.org/wiki/Direction_cosine#Cartesian_coordinates "Direction cosine") of **a** and **e** <sub><i>i</i></sub> or their [dot product](https://en.wikipedia.org/wiki/Dot_product "Dot product"). The vectors **e** <sub>1</sub>, **e** <sub>2</sub>, **e** <sub>3</sub> form an [orthonormal basis](https://en.wikipedia.org/wiki/Orthonormal_basis "Orthonormal basis") fixed in the [reference frame](https://en.wikipedia.org/wiki/Frame_of_reference "Frame of reference") in which the derivative is being taken.

### Ordinary derivative

If **a** is regarded as a vector function of a single scalar variable, such as time t, then the equation above reduces to the first [ordinary time derivative](https://en.wikipedia.org/wiki/Derivative "Derivative") of **a** with respect to t,[^2] 
$$
{\displaystyle {\frac {d\mathbf {a} }{dt}}=\sum _{i=1}^{n}{\frac {da_{i}}{dt}}\mathbf {e} _{i}.}
$$

### Total derivative

If the vector **a** is a function of a number n of scalar variables *q* <sub><i>r</i></sub> (*r* = 1,..., *n*), and each *q* <sub><i>r</i></sub> is only a function of time t, then the ordinary derivative of **a** with respect to t can be expressed, in a form known as the [total derivative](https://en.wikipedia.org/wiki/Total_derivative "Total derivative"), as [^2] 
$$
{\displaystyle {\frac {d\mathbf {a} }{dt}}=\sum _{r=1}^{n}{\frac {\partial \mathbf {a} }{\partial q_{r}}}{\frac {dq_{r}}{dt}}+{\frac {\partial \mathbf {a} }{\partial t}}.}
$$

Some authors prefer to use capital *D* to indicate the total derivative operator, as in *D* / *Dt*. The total derivative differs from the partial time derivative in that the total derivative accounts for changes in **a** due to the time variance of the variables *q* <sub><i>r</i></sub>.

### Reference frames

Whereas for scalar-valued functions there is only a single possible [reference frame](https://en.wikipedia.org/wiki/Frame_of_reference "Frame of reference"), to take the derivative of a vector-valued function requires the choice of a reference frame (at least when a fixed Cartesian coordinate system is not implied as such). Once a reference frame has been chosen, the derivative of a vector-valued function can be computed using techniques similar to those for computing derivatives of scalar-valued functions. A different choice of reference frame will, in general, produce a different derivative function. The derivative functions in different reference frames have a specific [kinematical relationship](#Derivative_of_a_vector_function_with_nonfixed_bases).

### Derivative of a vector function with nonfixed bases

The above formulas for the derivative of a vector function rely on the assumption that the [basis](https://en.wikipedia.org/wiki/Basis_\(linear_algebra\) "Basis (linear algebra)") vectors **e** <sub>1</sub>, **e** <sub>2</sub>, **e** <sub>3</sub> are constant, that is, fixed in the reference frame in which the derivative of **a** is being taken, and therefore the **e** <sub>1</sub>, **e** <sub>2</sub>, **e** <sub>3</sub> each has a derivative of identically zero. This often holds true for problems dealing with [vector fields](https://en.wikipedia.org/wiki/Vector_field "Vector field") in a fixed coordinate system, or for simple problems in [physics](https://en.wikipedia.org/wiki/Physics "Physics"). However, many complex problems involve the derivative of a vector function in multiple moving reference frames, which means that the basis vectors will not necessarily be constant. In such a case where the basis vectors **e** <sub>1</sub>, **e** <sub>2</sub>, **e** <sub>3</sub> are fixed in reference frame E, but not in reference frame N, the more general formula for the [ordinary time derivative](#Ordinary_derivative) of a vector in reference frame N is [^2] 
$$
{\displaystyle {\frac {{}^{\mathrm {N} }d\mathbf {a} }{dt}}=\sum _{i=1}^{3}{\frac {da_{i}}{dt}}\mathbf {e} _{i}+\sum _{i=1}^{3}a_{i}{\frac {{}^{\mathrm {N} }d\mathbf {e} _{i}}{dt}}}
$$
 where the superscript N to the left of the derivative operator indicates the reference frame in which the derivative is taken. [As shown previously](#Ordinary_derivative), the first term on the right hand side is equal to the derivative of **a** in the reference frame where **e** <sub>1</sub>, **e** <sub>2</sub>, **e** <sub>3</sub> are constant, reference frame E. It also can be shown that the second term on the right hand side is equal to the relative [angular velocity](https://en.wikipedia.org/wiki/Angular_velocity "Angular velocity") of the two reference frames [cross multiplied](#Cross_product) with the vector **a** itself.[^2] Thus, after substitution, the formula relating the derivative of a vector function in two reference frames is [^2] 
$$
{\displaystyle {\frac {{}^{\mathrm {N} }d\mathbf {a} }{dt}}={\frac {{}^{\mathrm {E} }d\mathbf {a} }{dt}}+{}^{\mathrm {N} }\mathbf {\omega } ^{\mathrm {E} }\times \mathbf {a} }
$$
 where <sup>N</sup> ***ω*** <sup>E</sup> is the [angular velocity](https://en.wikipedia.org/wiki/Angular_velocity "Angular velocity") of the reference frame E relative to the reference frame N.

One common example where this formula is used is to find the velocity of a space-borne object, such as a [rocket](https://en.wikipedia.org/wiki/Rocket "Rocket"), in the [inertial reference frame](https://en.wikipedia.org/wiki/Inertial_reference_frame "Inertial reference frame") using measurements of the rocket's velocity relative to the ground. The velocity <sup>N</sup> **v** <sup>R</sup> in inertial reference frame N of a rocket R located at position **r** <sup>R</sup> can be found using the formula 
$$
{\displaystyle {\frac {{}^{\mathrm {N} }d}{dt}}(\mathbf {r} ^{\mathrm {R} })={\frac {{}^{\mathrm {E} }d}{dt}}(\mathbf {r} ^{\mathrm {R} })+{}^{\mathrm {N} }\mathbf {\omega } ^{\mathrm {E} }\times \mathbf {r} ^{\mathrm {R} }.}
$$
 where <sup>N</sup> ***ω*** <sup>E</sup> is the [angular velocity](https://en.wikipedia.org/wiki/Angular_velocity "Angular velocity") of the Earth relative to the inertial frame N. Since velocity is the derivative of position, <sup>N</sup> **v** <sup>R</sup> and <sup>E</sup> **v** <sup>R</sup> are the derivatives of **r** <sup>R</sup> in reference frames N and E, respectively. By substitution, 
$$
{\displaystyle {}^{\mathrm {N} }\mathbf {v} ^{\mathrm {R} }={}^{\mathrm {E} }\mathbf {v} ^{\mathrm {R} }+{}^{\mathrm {N} }\mathbf {\omega } ^{\mathrm {E} }\times \mathbf {r} ^{\mathrm {R} }}
$$
 where <sup>E</sup> **v** <sup>R</sup> is the velocity vector of the rocket as measured from a reference frame E that is fixed to the Earth.

### Derivative and vector multiplication

The derivative of a product of vector functions behaves similarly to the [derivative of a product](https://en.wikipedia.org/wiki/Product_rule "Product rule") of scalar functions.[^1] Specifically, in the case of [scalar multiplication](#Scalar_multiplication) of a vector, if *p* is a scalar variable function of *q*,[^2] 
$$
{\displaystyle {\frac {\partial }{\partial q}}(p\mathbf {a} )={\frac {\partial p}{\partial q}}\mathbf {a} +p{\frac {\partial \mathbf {a} }{\partial q}}.}
$$

In the case of [dot multiplication](#Dot_product), for two vectors **a** and **b** that are both functions of *q*,[^2] 
$$
{\displaystyle {\frac {\partial }{\partial q}}(\mathbf {a} \cdot \mathbf {b} )={\frac {\partial \mathbf {a} }{\partial q}}\cdot \mathbf {b} +\mathbf {a} \cdot {\frac {\partial \mathbf {b} }{\partial q}}.}
$$

Similarly, the derivative of the [cross product](#Cross_product) of two vector functions is [^2] 
$$
{\displaystyle {\frac {\partial }{\partial q}}(\mathbf {a} \times \mathbf {b} )={\frac {\partial \mathbf {a} }{\partial q}}\times \mathbf {b} +\mathbf {a} \times {\frac {\partial \mathbf {b} }{\partial q}}.}
$$

### Derivative of an n-dimensional vector function

A function **f** of a real number t with values in the space ${\displaystyle \mathbb {R} ^{n}}$ can be written as ${\displaystyle \mathbf {f} (t)=(f_{1}(t),f_{2}(t),\ldots ,f_{n}(t))}$. Its derivative equals 
$$
{\displaystyle \mathbf {f} '(t)=(f_{1}'(t),f_{2}'(t),\ldots ,f_{n}'(t)).}
$$
 If **f** is a function of several variables, say of ${\displaystyle t\in \mathbb {R} ^{m}}$, then the partial derivatives of the components of **f** form a ${\displaystyle n\times m}$ matrix called the *[Jacobian matrix](https://en.wikipedia.org/wiki/Jacobian_matrix "Jacobian matrix") of **f***.

## Infinite-dimensional vector functions

If the values of a function **f** lie in an [infinite-dimensional](https://en.wikipedia.org/wiki/Dimension_\(vector_space\) "Dimension (vector space)") [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") *X*, such as a [Hilbert space](https://en.wikipedia.org/wiki/Hilbert_space "Hilbert space"), then **f** may be called an *infinite-dimensional vector function*.

### Functions with values in a Hilbert space

If the [argument](https://en.wikipedia.org/wiki/Argument_of_a_function "Argument of a function") of **f** is a real number and *X* is a Hilbert space, then the derivative of **f** at a point t can be defined as in the finite-dimensional case: 
$$
{\displaystyle \mathbf {f} '(t)=\lim _{h\to 0}{\frac {\mathbf {f} (t+h)-\mathbf {f} (t)}{h}}.}
$$
 Most results of the finite-dimensional case also hold in the infinite-dimensional case too, [mutatis mutandis](https://en.wikipedia.org/wiki/Mutatis_mutandis "Mutatis mutandis"). Differentiation can also be defined to functions of several variables (e.g., ${\displaystyle t\in \mathbb {R} ^{n}}$ or even ${\displaystyle t\in Y}$, where *Y* is an infinite-dimensional vector space).

N.B. If *X* is a Hilbert space, then one can easily show that any derivative (and any other [limit](https://en.wikipedia.org/wiki/Limit_\(mathematics\) "Limit (mathematics)")) can be computed componentwise: if 
$$
{\displaystyle \mathbf {f} =(f_{1},f_{2},f_{3},\ldots )}
$$
 (i.e., ${\displaystyle \mathbf {f} =f_{1}\mathbf {e} _{1}+f_{2}\mathbf {e} _{2}+f_{3}\mathbf {e} _{3}+\cdots }$, where ${\displaystyle \mathbf {e} _{1},\mathbf {e} _{2},\mathbf {e} _{3},\ldots }$ is an [orthonormal basis](https://en.wikipedia.org/wiki/Orthonormal_basis "Orthonormal basis") of the space *X*  ), and ${\displaystyle f'(t)}$ exists, then 
$$
{\displaystyle \mathbf {f} '(t)=(f_{1}'(t),f_{2}'(t),f_{3}'(t),\ldots ).}
$$
 However, the existence of a componentwise derivative does not guarantee the existence of a derivative, as componentwise convergence in a Hilbert space does not guarantee convergence with respect to the actual [topology](https://en.wikipedia.org/wiki/Topological_space "Topological space") of the Hilbert space.

### Other infinite-dimensional vector spaces

Most of the above hold for other [topological vector spaces](https://en.wikipedia.org/wiki/Topological_vector_space "Topological vector space") *X* too. However, not as many classical results hold in the [Banach space](https://en.wikipedia.org/wiki/Banach_space "Banach space") setting, e.g., an [absolutely continuous](https://en.wikipedia.org/wiki/Absolutely_continuous "Absolutely continuous") function with values in a [suitable Banach space](https://en.wikipedia.org/wiki/Radon%E2%80%93Nikodym_property "Radon–Nikodym property") need not have a derivative anywhere. Moreover, in most Banach spaces setting there are no orthonormal bases.

## Vector field

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/VectorField.svg/250px-VectorField.svg.png)

A portion of a vector field ( sin y, sin x )

In [vector calculus](https://en.wikipedia.org/wiki/Vector_calculus "Vector calculus") and [physics](https://en.wikipedia.org/wiki/Physics "Physics"), a [vector field](https://en.wikipedia.org/wiki/Vector_field "Vector field") is an assignment of a [vector](https://en.wikipedia.org/wiki/Vector_\(mathematics_and_physics\) "Vector (mathematics and physics)") to each point in a [space](https://en.wikipedia.org/wiki/Space_\(mathematics\) "Space (mathematics)"), most commonly [Euclidean space](https://en.wikipedia.org/wiki/Euclidean_space "Euclidean space") ${\displaystyle \mathbb {R} ^{n}}$.[^3] A vector field on a [plane](https://en.wikipedia.org/wiki/Plane_\(geometry\) "Plane (geometry)") can be visualized as a collection of arrows with given magnitudes and directions, each attached to a point on the plane. Vector fields often have [unit of measurement](https://en.wikipedia.org/wiki/Unit_of_measurement "Unit of measurement") (for example, metres or kilometres per hour), forming a [vector physical quantity](https://en.wikipedia.org/wiki/Vector_physical_quantity "Vector physical quantity"). They may be used to model, for example, the speed and direction of a moving fluid throughout [three dimensional space](https://en.wikipedia.org/wiki/Three_dimensional_space "Three dimensional space"), such as the [wind](https://en.wikipedia.org/wiki/Wind "Wind"), or the strength and direction of some [force](https://en.wikipedia.org/wiki/Force "Force"), such as the [magnetic](https://en.wikipedia.org/wiki/Magnetic_field "Magnetic field") or [gravitational](https://en.wikipedia.org/wiki/Gravity "Gravity") force, as it changes from one point to another point.

The elements of [differential and integral calculus](https://en.wikipedia.org/wiki/Differential_and_integral_calculus "Differential and integral calculus") extend naturally to vector fields. When a vector field represents [force](https://en.wikipedia.org/wiki/Force "Force"), the [line integral](https://en.wikipedia.org/wiki/Line_integral "Line integral") of a vector field represents the [work](https://en.wikipedia.org/wiki/Work_\(physics\) "Work (physics)") done by a force moving along a path, and under this interpretation [conservation of energy](https://en.wikipedia.org/wiki/Conservation_of_energy "Conservation of energy") is exhibited as a special case of the [fundamental theorem of calculus](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus "Fundamental theorem of calculus"). Vector fields can usefully be thought of as representing the velocity of a moving flow in space, and this physical intuition leads to notions such as the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") (which represents the rate of change of [volume](https://en.wikipedia.org/wiki/Volume "Volume") of a flow) and [curl](https://en.wikipedia.org/wiki/Curl_\(mathematics\) "Curl (mathematics)") (which represents the rotation of a flow).

A vector field is a special case of a *vector-valued function*, whose domain's dimension has no relation to the dimension of its range; for example, the [position vector](https://en.wikipedia.org/wiki/Position_vector "Position vector") of a [space curve](https://en.wikipedia.org/wiki/Space_curve "Space curve") is defined only for smaller subset of the ambient space. Likewise, n [coordinates](https://en.wikipedia.org/wiki/Coordinate_system "Coordinate system"), a vector field on a domain in *n* -dimensional Euclidean space ${\displaystyle \mathbb {R} ^{n}}$ can be represented as a vector-valued function that associates an *n* -tuple of real numbers to each point of the domain. This representation of a vector field depends on the coordinate system, and there is a well-defined transformation law (*[covariance and contravariance of vectors](https://en.wikipedia.org/wiki/Covariance_and_contravariance_of_vectors "Covariance and contravariance of vectors")*) in passing from one coordinate system to the other.

Vector fields are often discussed on [open subsets](https://en.wikipedia.org/wiki/Open_set "Open set") of Euclidean space, but also make sense on other subsets such as [surfaces](https://en.wikipedia.org/wiki/Surface_\(topology\) "Surface (topology)"), where they associate an arrow tangent to the surface at each point (a [tangent vector](https://en.wikipedia.org/wiki/Differential_geometry_of_curves "Differential geometry of curves")). More generally, vector fields are defined on [differentiable manifolds](https://en.wikipedia.org/wiki/Differentiable_manifold "Differentiable manifold"), which are spaces that look like Euclidean space on small scales, but may have more complicated structure on larger scales. In this setting, a vector field gives a tangent vector at each point of the manifold (that is, a [section](https://en.wikipedia.org/wiki/Section_\(fiber_bundle\) "Section (fiber bundle)") of the [tangent bundle](https://en.wikipedia.org/wiki/Tangent_bundle "Tangent bundle") to the manifold). Vector fields are one kind of [tensor field](https://en.wikipedia.org/wiki/Tensor_field "Tensor field").

[^1]: In fact, these relations are derived applying the [product rule](https://en.wikipedia.org/wiki/Product_rule "Product rule") componentwise.

[^2]: Kane, Thomas R.; Levinson, David A. (1996). "1–9 Differentiation of Vector Functions". *Dynamics: Theory and Applications*. Sunnyvale, California: McGraw-Hill. pp. 29–37.

[^3]: Galbis, Antonio; Maestre, Manuel (2012). [*Vector Analysis Versus Vector Calculus*](https://books.google.com/books?id=tdF8uTn2cnMC&pg=PA12). Springer. p. 12. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4614-2199-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4614-2199-3 "Special:BookSources/978-1-4614-2199-3").