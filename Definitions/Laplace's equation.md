---
title: "Laplace's equation"
source: "https://en.wikipedia.org/wiki/Laplace%27s_equation"
author:
  - "[[Wikipedia]]"
published: 2002-01-28
created: 2026-05-06
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics") and [physics](https://en.wikipedia.org/wiki/Physics "Physics"), **Laplace's equation** is a second-order [partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation "Partial differential equation") named after [Pierre-Simon Laplace](https://en.wikipedia.org/wiki/Pierre-Simon_Laplace "Pierre-Simon Laplace"), who first studied its properties in 1786. This is often written as 
$$
{\displaystyle \nabla ^{2}\!f=0}
$$
 or 
$$
{\displaystyle \Delta f=0,}
$$
 where ${\displaystyle \Delta =\nabla \cdot \nabla =\nabla ^{2}}$ is the [Laplace operator](https://en.wikipedia.org/wiki/Laplace_operator "Laplace operator"),[^1] ${\displaystyle \nabla \cdot }$ is the [divergence](https://en.wikipedia.org/wiki/Divergence "Divergence") operator (also symbolized "div"), ${\displaystyle \nabla }$ is the [gradient](https://en.wikipedia.org/wiki/Gradient "Gradient") operator (also symbolized "grad"), and ${\displaystyle f(x,y,z)}$ is a twice-differentiable real-valued function. The Laplace operator therefore maps a scalar function to another scalar function.

If the right-hand side is specified as a given function, ${\displaystyle h(x,y,z)}$, we have 
$$
{\displaystyle \Delta f=h}
$$

This is called [Poisson's equation](https://en.wikipedia.org/wiki/Poisson%27s_equation "Poisson's equation"), a generalization of Laplace's equation. Laplace's equation and Poisson's equation are the simplest examples of [elliptic partial differential equations](https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation "Elliptic partial differential equation"). Laplace's equation is also a special case of the [Helmholtz equation](https://en.wikipedia.org/wiki/Helmholtz_equation "Helmholtz equation").

The general theory of solutions to Laplace's equation is known as [potential theory](https://en.wikipedia.org/wiki/Potential_theory "Potential theory"). The twice continuously differentiable solutions of Laplace's equation are the [harmonic functions](https://en.wikipedia.org/wiki/Harmonic_function "Harmonic function"),[^3] which are important in multiple branches of physics, notably electrostatics, gravitation, and [fluid dynamics](https://en.wikipedia.org/wiki/Fluid_dynamics "Fluid dynamics"). In the study of [heat conduction](https://en.wikipedia.org/wiki/Heat_conduction "Heat conduction"), the Laplace equation is the [steady-state](https://en.wikipedia.org/wiki/Steady-state "Steady-state") [heat equation](https://en.wikipedia.org/wiki/Heat_equation "Heat equation").[^4] In general, Laplace's equation describes situations of equilibrium, or those that do not depend explicitly on time.

## Forms in different coordinate systems

In [rectangular coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinates "Cartesian coordinates"),[^5] 
$$
{\displaystyle \nabla ^{2}f={\frac {\partial ^{2}f}{\partial x^{2}}}+{\frac {\partial ^{2}f}{\partial y^{2}}}+{\frac {\partial ^{2}f}{\partial z^{2}}}=0.}
$$

In [cylindrical coordinates](https://en.wikipedia.org/wiki/Cylindrical_coordinates "Cylindrical coordinates"),[^5] 
$$
{\displaystyle \nabla ^{2}f={\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}}}{\frac {\partial ^{2}f}{\partial \phi ^{2}}}+{\frac {\partial ^{2}f}{\partial z^{2}}}=0.}
$$

In [spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinates "Spherical coordinates"), using the ${\displaystyle (r,\theta ,\varphi )}$ convention,[^5] 
$$
{\displaystyle \nabla ^{2}f={\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial f}{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}}=0.}
$$

More generally, in arbitrary [curvilinear coordinates](https://en.wikipedia.org/wiki/Curvilinear_coordinates "Curvilinear coordinates") (ξ <sup><i>i</i></sup>), 
$$
{\displaystyle \nabla ^{2}f={\frac {\partial }{\partial \xi ^{j}}}\left({\frac {\partial f}{\partial \xi ^{k}}}g^{kj}\right)+{\frac {\partial f}{\partial \xi ^{j}}}g^{jm}\Gamma _{mn}^{n}=0,}
$$
 or 
$$
{\displaystyle \nabla ^{2}f={\frac {1}{\sqrt {|g|}}}{\frac {\partial }{\partial \xi ^{i}}}\!\left({\sqrt {|g|}}g^{ij}{\frac {\partial f}{\partial \xi ^{j}}}\right)=0,\qquad (g=\det\{g_{ij}\})}
$$
 where *g* <sub><i>ij</i></sub> is the Euclidean [metric tensor](https://en.wikipedia.org/wiki/Metric_tensor "Metric tensor") relative to the new coordinates and Γ denotes its [Christoffel symbols](https://en.wikipedia.org/wiki/Christoffel_symbols "Christoffel symbols").

## Boundary conditions

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Laplace%27s_equation_on_an_annulus.svg/500px-Laplace%27s_equation_on_an_annulus.svg.png)

Laplace's equation on an annulus (inner radius r = 2 and outer radius R = 4 ) with Dirichlet boundary conditions u ( =2) = 0 and =4) = 4 sin(5 θ )

The [Dirichlet problem](https://en.wikipedia.org/wiki/Dirichlet_problem "Dirichlet problem") for Laplace's equation consists of finding a solution *φ* on some domain D such that *φ* on the boundary of D is equal to some given function. Since the Laplace operator appears in the [heat equation](https://en.wikipedia.org/wiki/Heat_equation "Heat equation"), one physical interpretation of this problem is as follows: fix the temperature on the boundary of the domain according to the given specification of the boundary condition. Allow heat to flow until a stationary state is reached in which the temperature at each point on the domain does not change anymore. The temperature distribution in the interior will then be given by the solution to the corresponding Dirichlet problem.

The [Neumann boundary conditions](https://en.wikipedia.org/wiki/Neumann_boundary_condition "Neumann boundary condition") for Laplace's equation specify not the function *φ* itself on the boundary of D but its [normal derivative](https://en.wikipedia.org/wiki/Normal_derivative "Normal derivative"). Physically, this corresponds to the construction of a potential for a vector field whose effect is known at the boundary of *D* alone. For the example of the heat equation it amounts to prescribing the heat flux through the boundary. In particular, at an adiabatic boundary, the normal derivative of *φ* is zero.

Solutions of Laplace's equation are called [harmonic functions](https://en.wikipedia.org/wiki/Harmonic_function "Harmonic function"); they are all [analytic](https://en.wikipedia.org/wiki/Analytic_function "Analytic function") within the domain where the equation is satisfied. If any two functions are solutions to Laplace's equation (or any linear homogeneous differential equation), their sum (or any linear combination) is also a solution. This property, called the [principle of superposition](https://en.wikipedia.org/wiki/Superposition_principle "Superposition principle"), is very useful. For example, solutions to complex problems can be constructed by summing simple solutions.

### Details

For a domain ${\displaystyle D\subset \mathbf {R} ^{n}}$, the most common boundary value problems for Laplace's equation are the [Dirichlet problem](https://en.wikipedia.org/wiki/Dirichlet_problem "Dirichlet problem"), in which the boundary values of the unknown function are prescribed, and the [Neumann problem](https://en.wikipedia.org/wiki/Neumann_problem "Neumann problem"), in which its outward normal derivative is prescribed.[^6] [^7]

If ${\displaystyle D}$ is bounded and connected, then a harmonic function is uniquely determined by its Dirichlet boundary values; this follows from the [maximum principle](https://en.wikipedia.org/wiki/Maximum_principle "Maximum principle").[^6] For the Neumann problem, uniqueness holds only up to an additive constant. Moreover, if ${\displaystyle u}$ is harmonic in ${\displaystyle D}$, then the divergence theorem implies the compatibility condition 
$$
{\displaystyle \int _{\partial D}{\frac {\partial u}{\partial \nu }}\,dS=0.}
$$
 Hence a necessary condition for solvability of the Neumann problem with prescribed flux ${\displaystyle g}$ is 
$$
{\displaystyle \int _{\partial D}g\,dS=0.}
$$
 [^6] A third classical boundary condition is the [Robin boundary condition](https://en.wikipedia.org/wiki/Robin_boundary_condition "Robin boundary condition"), which prescribes a linear combination of the function and its normal derivative on the boundary.[^6]

In special domains, solutions can be written explicitly by integral formulas. For the unit disk ${\displaystyle \mathbb {D} \subset \mathbf {C} }$, the solution of the Dirichlet problem with continuous boundary data ${\displaystyle f}$ is given by the [Poisson kernel](https://en.wikipedia.org/wiki/Poisson_kernel "Poisson kernel") formula 
$$
{\displaystyle u(re^{i\theta })={\frac {1}{2\pi }}\int _{0}^{2\pi }{\frac {1-r^{2}}{1-2r\cos(\theta -\varphi )+r^{2}}}\,f(e^{i\varphi })\,d\varphi .}
$$
 Similarly, in the upper half-space ${\displaystyle \mathbf {R} _{+}^{n}=\{(x',x_{n})\in \mathbf {R} ^{n-1}\times \mathbf {R} :x_{n}>0\}}$, harmonic functions with suitable boundary data are represented by the Poisson integral 
$$
{\displaystyle u(x',x_{n})=c_{n}\int _{\mathbf {R} ^{n-1}}{\frac {x_{n}}{{\bigl (}|x'-y|^{2}+x_{n}^{2}{\bigr )}^{n/2}}}\,f(y)\,dy.}
$$
 These kernels are densities of the [harmonic measure](https://en.wikipedia.org/wiki/Harmonic_measure "Harmonic measure") with respect to boundary measure in these model domains.[^7]

### Existence theory and boundary regularity

A classical approach to the Dirichlet problem for Laplace's equation is the [Perron method](https://en.wikipedia.org/wiki/Perron_method "Perron method"), which constructs a candidate solution as the supremum of all subharmonic functions lying below the prescribed boundary data.[^8] The resulting Perron solution is harmonic in the domain; the subtle question is whether it attains the desired boundary values at every boundary point.

This leads to the notion of a regular *boundary point*. A boundary point is regular if the solution of the Dirichlet problem converges to the prescribed boundary value there. A sufficient condition is the existence of a *barrier* at that point, namely a superharmonic function that vanishes at the point and is positive elsewhere near the boundary.[^9]

For Laplace's equation, regularity of boundary points is characterized by the classical *Wiener criterion*, which gives a necessary and sufficient condition in terms of capacity. In this way, solvability of the Dirichlet problem is tied to the fine geometric structure of the boundary.[^10]

## Weak solutions and Dirichlet principle

Laplace's equation can also be interpreted in a [weak sense](https://en.wikipedia.org/wiki/Weak_solution "Weak solution"). A function ${\displaystyle u\in H_{\mathrm {loc} }^{1}(\Omega )}$ is called **weakly harmonic** if 
$$
{\displaystyle \int _{\Omega }\nabla u\cdot \nabla \varphi \,dx=0}
$$
 for every test function ${\displaystyle \varphi \in C_{c}^{\infty }(\Omega )}$.[^11] By [Weyl's lemma](https://en.wikipedia.org/wiki/Weyl%27s_lemma_\(Laplace_equation\) "Weyl's lemma (Laplace equation)"), every weakly harmonic function is in fact smooth, and indeed real analytic.[^11] [^6]

Harmonic functions also admit a variational characterization. Among functions with fixed boundary values, the solutions of Laplace's equation are exactly the minimizers of the [Dirichlet energy](https://en.wikipedia.org/wiki/Dirichlet_energy "Dirichlet energy") 
$$
{\displaystyle E(u)={\frac {1}{2}}\int _{\Omega }|\nabla u|^{2}\,dx.}
$$
 This is known as [Dirichlet's principle](https://en.wikipedia.org/wiki/Dirichlet%27s_principle "Dirichlet's principle").[^11] [^7]

## Kelvin transform

A classical symmetry of Laplace's equation is inversion in the unit sphere. If ${\displaystyle u}$ is harmonic in a domain ${\displaystyle \Omega \subset \mathbf {R} ^{n}\setminus \{0\}}$, then its *[Kelvin transform](https://en.wikipedia.org/wiki/Kelvin_transform "Kelvin transform")* 
$$
{\displaystyle (Ku)(x)=|x|^{2-n}u\!\left({\frac {x}{|x|^{2}}}\right)}
$$
 is harmonic in the inverted domain 
$$
{\displaystyle \Omega ^{\ast }=\left\{{\frac {x}{|x|^{2}}}:x\in \Omega \right\}.}
$$
 In dimension ${\displaystyle n=2}$, the factor ${\displaystyle |x|^{2-n}}$ is equal to ${\displaystyle 1}$, so the transform reduces to composition with inversion.[^7]

The Kelvin transform is useful for converting interior problems into exterior problems, for studying isolated singularities, and for analyzing the behavior of harmonic functions at infinity.[^7] [^6]

## In two dimensions

Laplace's equation in two independent variables in rectangular coordinates has the form 
$$
{\displaystyle {\frac {\partial ^{2}\psi }{\partial x^{2}}}+{\frac {\partial ^{2}\psi }{\partial y^{2}}}\equiv \psi _{xx}+\psi _{yy}=0.}
$$

### Analytic functions

The real and imaginary parts of a complex [analytic function](https://en.wikipedia.org/wiki/Analytic_function "Analytic function") both satisfy the Laplace equation. That is, if *z* = *x* + *iy*, and if 
$$
{\displaystyle f(z)=u(x,y)+iv(x,y),}
$$
 then the necessary condition that *f* (*z*) be analytic is that *u* and *v* be differentiable and that the [Cauchy–Riemann equations](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations "Cauchy–Riemann equations") be satisfied: 
$$
{\displaystyle u_{x}=v_{y},\quad v_{x}=-u_{y}}
$$
 where *u <sub>x</sub>* is the first partial derivative of *u* with respect to x. It follows that 
$$
{\displaystyle u_{yy}=(-v_{x})_{y}=-(v_{y})_{x}=-(u_{x})_{x}.}
$$
 Therefore *u* satisfies the Laplace equation. A similar calculation shows that *v* also satisfies the Laplace equation. Conversely, given a harmonic function, it is the real part of an analytic function, *f* (*z*) (at least locally). If a trial form is 
$$
{\displaystyle f(z)=\varphi (x,y)+i\psi (x,y),}
$$
 then the Cauchy–Riemann equations will be satisfied if we set 
$$
{\displaystyle \psi _{x}=-\varphi _{y},\quad \psi _{y}=\varphi _{x}.}
$$
 This relation does not determine *ψ*, but only its increments: 
$$
{\displaystyle d\psi =-\varphi _{y}\,dx+\varphi _{x}\,dy.}
$$
 The Laplace equation for *φ* implies that the integrability condition for *ψ* is satisfied: 
$$
{\displaystyle \psi _{xy}=\psi _{yx},}
$$
 and thus *ψ* may be defined by a line integral. The integrability condition and [Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem "Stokes' theorem") implies that the value of the line integral connecting two points is independent of the path. The resulting pair of solutions of the Laplace equation are called **conjugate harmonic functions**. This construction is only valid locally, or provided that the path does not loop around a singularity. For example, if r and θ are polar coordinates and 
$$
{\displaystyle \varphi =\log r,}
$$
 then a corresponding analytic function is 
$$
{\displaystyle f(z)=\log z=\log r+i\theta .}
$$

However, the angle θ is single-valued only in a region that does not enclose the origin.

The close connection between the Laplace equation and analytic functions implies that any solution of the Laplace equation has derivatives of all orders, and can be expanded in a [power series](https://en.wikipedia.org/wiki/Power_series "Power series"), at least inside a circle that does not enclose a singularity. This is in sharp contrast to solutions of the [wave equation](https://en.wikipedia.org/wiki/Wave_equation "Wave equation"), which generally have less regularity.

There is an intimate connection between power series and [Fourier series](https://en.wikipedia.org/wiki/Fourier_series "Fourier series"). If we expand a function *f* in a power series inside a circle of radius R, this means that 
$$
{\displaystyle f(z)=\sum _{n=0}^{\infty }c_{n}z^{n},}
$$
 with suitably defined coefficients whose real and imaginary parts are given by 
$$
{\displaystyle c_{n}=a_{n}+ib_{n}.}
$$
 Therefore 
$$
{\displaystyle f(z)=\sum _{n=0}^{\infty }\left[a_{n}r^{n}\cos n\theta -b_{n}r^{n}\sin n\theta \right]+i\sum _{n=1}^{\infty }\left[a_{n}r^{n}\sin n\theta +b_{n}r^{n}\cos n\theta \right],}
$$
 which is a Fourier series for *f*. These trigonometric functions can themselves be expanded, using [multiple angle formulae](https://en.wikipedia.org/wiki/De_Moivre%27s_formula#Formulas_for_cosine_and_sine_individually "De Moivre's formula").

### Fluid flow

Let the quantities *u* and *v* be the horizontal and vertical components of the velocity field of a steady incompressible, irrotational flow in two dimensions. The continuity condition for an incompressible flow is that 
$$
{\displaystyle u_{x}+v_{y}=0,}
$$
 and the condition that the flow be irrotational is that 
$$
{\displaystyle \nabla \times \mathbf {V} =v_{x}-u_{y}=0.}
$$
 If we define the differential of a function *ψ* by 
$$
{\displaystyle d\psi =u\,dy-v\,dx,}
$$
 then the continuity condition is the integrability condition for this differential: the resulting function is called the [stream function](https://en.wikipedia.org/wiki/Stream_function "Stream function") because it is constant along [flow lines](https://en.wikipedia.org/wiki/Streamlines,_streaklines_and_pathlines "Streamlines, streaklines and pathlines"). The first derivatives of *ψ* are given by 
$$
{\displaystyle \psi _{x}=-v,\quad \psi _{y}=u,}
$$
 and the irrotationality condition implies that *ψ* satisfies the Laplace equation. The harmonic function *φ* that is conjugate to *ψ* is called the [velocity potential](https://en.wikipedia.org/wiki/Velocity_potential "Velocity potential"). The Cauchy–Riemann equations imply that 
$$
{\displaystyle \varphi _{x}=\psi _{y}=u,\quad \varphi _{y}=-\psi _{x}=v.}
$$
 Thus every analytic function corresponds to a steady incompressible, irrotational, inviscid fluid flow in the plane. The real part is the velocity potential, and the imaginary part is the stream function.

### Electrostatics

According to [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations "Maxwell's equations"), an electric field (*u*, *v*) in two space dimensions that is independent of time satisfies 
$$
{\displaystyle \nabla \times (u,v,0)=(v_{x}-u_{y}){\hat {\mathbf {k} }}=\mathbf {0} ,}
$$
 and 
$$
{\displaystyle \nabla \cdot (u,v)=\rho ,}
$$
 where *ρ* is the charge density. The first Maxwell equation is the integrability condition for the differential 
$$
{\displaystyle d\varphi =-u\,dx-v\,dy,}
$$
 so the electric potential *φ* may be constructed to satisfy 
$$
{\displaystyle \varphi _{x}=-u,\quad \varphi _{y}=-v.}
$$
 The second of Maxwell's equations then implies that 
$$
{\displaystyle \varphi _{xx}+\varphi _{yy}=-\rho ,}
$$
 which is the [Poisson equation](https://en.wikipedia.org/wiki/Poisson_equation "Poisson equation"). The Laplace equation can be used in three-dimensional problems in electrostatics and fluid flow just as in two dimensions.

## In three dimensions

### Fundamental solution

A [fundamental solution](https://en.wikipedia.org/wiki/Fundamental_solution "Fundamental solution") of Laplace's equation satisfies 
$$
{\displaystyle \Delta u=u_{xx}+u_{yy}+u_{zz}=-\delta (x-x',y-y',z-z'),}
$$
 where the [Dirac delta function](https://en.wikipedia.org/wiki/Dirac_delta_function "Dirac delta function") *δ* denotes a unit source concentrated at the point (*x* ′, *y* ′, *z* ′). No function has this property: in fact it is a [distribution](https://en.wikipedia.org/wiki/Distribution_\(mathematics\) "Distribution (mathematics)") rather than a function; but it can be thought of as a limit of functions whose integrals over space are unity, and whose support (the region where the function is non-zero) shrinks to a point (see [weak solution](https://en.wikipedia.org/wiki/Weak_solution "Weak solution")). It is common to take a different sign convention for this equation than one typically does when defining fundamental solutions. This choice of sign is often convenient to work with because −Δ is a [positive operator](https://en.wikipedia.org/wiki/Positive_operator "Positive operator"). The definition of the fundamental solution thus implies that, if the Laplacian of *u* is integrated over any volume that encloses the source point, then 
$$
{\displaystyle \iiint _{V}\nabla \cdot \nabla u\,dV=-1.}
$$

The Laplace equation is unchanged under a rotation of coordinates, and hence we can expect that a fundamental solution may be obtained among solutions that only depend upon the distance r from the source point. If we choose the volume to be a ball of radius a around the source point, then Gauss's [divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem "Divergence theorem") implies that 
$$
{\displaystyle -1=\iiint _{V}\nabla \cdot \nabla u\,dV=\iint _{S}{\frac {du}{dr}}\,dS=\left.4\pi a^{2}{\frac {du}{dr}}\right|_{r=a}.}
$$

It follows that 
$$
{\displaystyle {\frac {du}{dr}}=-{\frac {1}{4\pi r^{2}}},}
$$
 on a sphere of radius r that is centered on the source point, and hence 
$$
{\displaystyle u={\frac {1}{4\pi r}}.}
$$

Note that, with the opposite sign convention (used in [physics](https://en.wikipedia.org/wiki/Physics "Physics")), this is the [potential](https://en.wikipedia.org/wiki/Potential "Potential") generated by a [point particle](https://en.wikipedia.org/wiki/Point_particle "Point particle"), for an [inverse-square law](https://en.wikipedia.org/wiki/Inverse-square_law "Inverse-square law") force, arising in the solution of the [Poisson equation](https://en.wikipedia.org/wiki/Poisson_equation "Poisson equation"). A similar argument shows that in two dimensions 
$$
{\displaystyle u=-{\frac {\log(r)}{2\pi }}.}
$$
 where log(*r*) denotes the [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm "Natural logarithm"). Note that, with the opposite sign convention, this is the [potential](https://en.wikipedia.org/wiki/Potential "Potential") generated by a pointlike [sink](https://en.wikipedia.org/wiki/Potential_flow "Potential flow") (see [point particle](https://en.wikipedia.org/wiki/Point_particle "Point particle")), which is the solution of the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_\(fluid_dynamics\) "Euler equations (fluid dynamics)") in two-dimensional [incompressible flow](https://en.wikipedia.org/wiki/Incompressible_flow "Incompressible flow").

### Green's function

A [Green's function](https://en.wikipedia.org/wiki/Green%27s_function "Green's function") is a fundamental solution that also satisfies a suitable condition on the boundary S of a volume V. For instance, 
$$
{\displaystyle G(x,y,z;x',y',z')}
$$
 may satisfy 
$$
{\displaystyle \nabla \cdot \nabla G=-\delta (x-x',y-y',z-z')\qquad {\text{in }}V,}
$$
 
$$
{\displaystyle G=0\quad {\text{if}}\quad (x,y,z)\qquad {\text{on }}S.}
$$

Now if *u* is any solution of the Poisson equation in V: 
$$
{\displaystyle \nabla \cdot \nabla u=-f,}
$$

and *u* assumes the boundary values *g* on S, then we may apply [Green's identity](https://en.wikipedia.org/wiki/Green%27s_identities "Green's identities"), (a consequence of the divergence theorem) which states that

$$
{\displaystyle \iiint _{V}\left[G\,\nabla \cdot \nabla u-u\,\nabla \cdot \nabla G\right]\,dV=\iiint _{V}\nabla \cdot \left[G\nabla u-u\nabla G\right]\,dV=\iint _{S}\left[Gu_{n}-uG_{n}\right]\,dS.\,}
$$

The notations *u <sub>n</sub>* and *G <sub>n</sub>* denote normal derivatives on *S*. In view of the conditions satisfied by *u* and *G*, this result simplifies to

$$
{\displaystyle u(x',y',z')=\iiint _{V}Gf\,dV-\iint _{S}G_{n}g\,dS.\,}
$$

Thus the Green's function describes the influence at (*x* ′, *y* ′, *z* ′) of the data *f* and *g*. For the case of the interior of a sphere of radius *a*, the Green's function may be obtained by means of a reflection ([Sommerfeld 1949](#CITEREFSommerfeld1949)): the source point *P* at distance *ρ* from the center of the sphere is reflected along its radial line to a point *P'* that is at a distance

$$
{\displaystyle \rho '={\frac {a^{2}}{\rho }}.\,}
$$

Note that if *P* is inside the sphere, then *P′* will be outside the sphere. The Green's function is then given by 
$$
{\displaystyle {\frac {1}{4\pi R}}-{\frac {a}{4\pi \rho R'}},\,}
$$
 where R denotes the distance to the source point *P* and *R* ′ denotes the distance to the reflected point *P* ′. A consequence of this expression for the Green's function is the **[Poisson integral formula](https://en.wikipedia.org/wiki/Poisson_integral_formula "Poisson integral formula")**. Let ρ, θ, and φ be [spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinates "Spherical coordinates") for the source point *P*. Here θ denotes the angle with the vertical axis, which is contrary to the usual American mathematical notation, but agrees with standard European and physical practice. Then the solution of the Laplace equation with Dirichlet boundary values *g* inside the sphere is given by ([Zachmanoglou & Thoe 1986](#CITEREFZachmanoglouThoe1986), p. 228) 
$$
{\displaystyle u(P)={\frac {1}{4\pi }}a^{3}\left(1-{\frac {\rho ^{2}}{a^{2}}}\right)\int _{0}^{2\pi }\int _{0}^{\pi }{\frac {g(\theta ',\varphi ')\sin \theta '}{(a^{2}+\rho ^{2}-2a\rho \cos \Theta )^{\frac {3}{2}}}}d\theta '\,d\varphi '}
$$
 where 
$$
{\displaystyle \cos \Theta =\cos \theta \cos \theta '+\sin \theta \sin \theta '\cos(\varphi -\varphi ')}
$$
 is the cosine of the angle between (*θ*, *φ*) and (*θ* ′, *φ* ′). A simple consequence of this formula is that if *u* is a harmonic function, then the value of *u* at the center of the sphere is the mean value of its values on the sphere. This mean value property immediately implies that a non-constant harmonic function cannot assume its maximum value at an interior point.

### Laplace's spherical harmonics

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Rotating_spherical_harmonics.gif/250px-Rotating_spherical_harmonics.gif)

Real (Laplace) spherical harmonics Y ℓ m for = 0,..., 4 (top to bottom) and = 0,..., (left to right). Zonal, sectoral, and tesseral harmonics are depicted along the left-most column, the main diagonal, and elsewhere, respectively. (The negative order harmonics {\\displaystyle Y\_{\\ell }^{-m}} would be shown rotated about the z axis by {\\displaystyle 90^{\\circ }/m} with respect to the positive order ones.)

Laplace's equation in [spherical coordinates](https://en.wikipedia.org/wiki/Spherical_coordinate_system "Spherical coordinate system") is:[^12]

$$
{\displaystyle \nabla ^{2}f={\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial f}{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}}=0.}
$$

Consider the problem of finding solutions of the form *f* (*r*, *θ*, *φ*) = *R* (*r*) *Y* (*θ*, *φ*). By [separation of variables](https://en.wikipedia.org/wiki/Separation_of_variables#pde "Separation of variables"), two differential equations result by imposing Laplace's equation:

$$
{\displaystyle {\frac {1}{R}}{\frac {d}{dr}}\left(r^{2}{\frac {dR}{dr}}\right)=\lambda ,\qquad {\frac {1}{Y}}{\frac {1}{\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial Y}{\partial \theta }}\right)+{\frac {1}{Y}}{\frac {1}{\sin ^{2}\theta }}{\frac {\partial ^{2}Y}{\partial \varphi ^{2}}}=-\lambda .}
$$

The second equation can be simplified under the assumption that *Y* has the form *Y* (*θ*, *φ*) = Θ(*θ*) Φ(*φ*). Applying separation of variables again to the second equation gives way to the pair of differential equations

$$
{\displaystyle {\frac {1}{\Phi }}{\frac {d^{2}\Phi }{d\varphi ^{2}}}=-m^{2}}
$$
 
$$
{\displaystyle \lambda \sin ^{2}\theta +{\frac {\sin \theta }{\Theta }}{\frac {d}{d\theta }}\left(\sin \theta {\frac {d\Theta }{d\theta }}\right)=m^{2}}
$$

for some number *m*. A priori, *m* is a complex constant, but because Φ must be a [periodic function](https://en.wikipedia.org/wiki/Periodic_function "Periodic function") whose period evenly divides 2 *π*, *m* is necessarily an integer and Φ is a linear combination of the complex exponentials *e* <sup>± <i>imφ</i></sup>. The solution function *Y* (*θ*, *φ*) is regular at the poles of the sphere, where *θ* = 0, *π*. Imposing this regularity in the solution Θ of the second equation at the boundary points of the domain is a [Sturm–Liouville problem](https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_problem "Sturm–Liouville problem") that forces the parameter *λ* to be of the form *λ* = *ℓ* (*ℓ* + 1) for some non-negative integer with *ℓ* ≥ | *m* |; this is also explained [below](https://en.wikipedia.org/wiki/Spherical_harmonics#Orbital_angular_momentum "Spherical harmonics") in terms of the [orbital angular momentum](https://en.wikipedia.org/wiki/Angular_momentum_operator "Angular momentum operator"). Furthermore, a change of variables *t* = cos *θ* transforms this equation into the [Legendre equation](https://en.wikipedia.org/wiki/Associated_Legendre_function "Associated Legendre function"), whose solution is a multiple of the [associated Legendre polynomial](https://en.wikipedia.org/wiki/Associated_Legendre_polynomial "Associated Legendre polynomial") *P <sub>ℓ</sub> <sup>m</sup>* (cos *θ*). Finally, the equation for *R* has solutions of the form *R* (*r*) = *A r <sup>ℓ</sup>* + *B r* <sup>− <i>ℓ</i> − 1</sup>; requiring the solution to be regular throughout **R** <sup>3</sup> forces *B* = 0.[^2]

Here the solution was assumed to have the special form *Y* (*θ*, *φ*) = Θ(*θ*) Φ(*φ*). For a given value of *ℓ*, there are 2 *ℓ* + 1 independent solutions of this form, one for each integer *m* with − *ℓ* ≤ *m* ≤ *ℓ*. These angular solutions are a product of [trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_function "Trigonometric function"), here represented as a [complex exponential](https://en.wikipedia.org/wiki/Euler%27s_formula "Euler's formula"), and associated Legendre polynomials: 
$$
{\displaystyle Y_{\ell }^{m}(\theta ,\varphi )=Ne^{im\varphi }P_{\ell }^{m}(\cos {\theta })}
$$
 which fulfill 
$$
{\displaystyle r^{2}\nabla ^{2}Y_{\ell }^{m}(\theta ,\varphi )=-\ell (\ell +1)Y_{\ell }^{m}(\theta ,\varphi ).}
$$

Here *Y <sub>ℓ</sub> <sup>m</sup>* is called a spherical harmonic function of degree ℓ and order m, *P <sub>ℓ</sub> <sup>m</sup>* is an [associated Legendre polynomial](https://en.wikipedia.org/wiki/Associated_Legendre_polynomial "Associated Legendre polynomial"), *N* is a normalization constant, and θ and φ represent colatitude and longitude, respectively. In particular, the [colatitude](https://en.wikipedia.org/wiki/Colatitude "Colatitude") θ, or polar angle, ranges from 0 at the North Pole, to *π* /2 at the Equator, to *π* at the South Pole, and the [longitude](https://en.wikipedia.org/wiki/Longitude "Longitude") φ, or [azimuth](https://en.wikipedia.org/wiki/Azimuth "Azimuth"), may assume all values with 0 ≤ *φ* < 2 *π*. For a fixed integer ℓ, every solution *Y* (*θ*, *φ*) of the eigenvalue problem 
$$
{\displaystyle r^{2}\nabla ^{2}Y=-\ell (\ell +1)Y}
$$
 is a [linear combination](https://en.wikipedia.org/wiki/Linear_combination "Linear combination") of *Y <sub>ℓ</sub> <sup>m</sup>*. In fact, for any such solution, *r <sup>ℓ</sup> Y* (*θ*, *φ*) is the expression in spherical coordinates of a [homogeneous polynomial](https://en.wikipedia.org/wiki/Homogeneous_polynomial "Homogeneous polynomial") that is harmonic (see [below](https://en.wikipedia.org/wiki/Spherical_harmonics#Higher_dimensions "Spherical harmonics")), and so counting dimensions shows that there are 2 *ℓ* + 1 linearly independent such polynomials.

The general solution to Laplace's equation in a ball centered at the origin is a [linear combination](https://en.wikipedia.org/wiki/Linear_combination "Linear combination") of the spherical harmonic functions multiplied by the appropriate scale factor *r <sup>ℓ</sup>*, 
$$
{\displaystyle f(r,\theta ,\varphi )=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }f_{\ell }^{m}r^{\ell }Y_{\ell }^{m}(\theta ,\varphi ),}
$$
 where the *f <sub>ℓ</sub> <sup>m</sup>* are constants and the factors *r <sup>ℓ</sup> Y <sub>ℓ</sub> <sup>m</sup>* are known as [solid harmonics](https://en.wikipedia.org/wiki/Solid_harmonics "Solid harmonics"). Such an expansion is valid in the [ball](https://en.wikipedia.org/wiki/Ball_\(mathematics\) "Ball (mathematics)") 
$$
{\displaystyle r<R={\frac {1}{\limsup _{\ell \to \infty }|f_{\ell }^{m}|^{{1}/{\ell }}}}.}
$$

For ${\displaystyle r>R}$, the solid harmonics with negative powers of ${\displaystyle r}$ are chosen instead. In that case, one needs to expand the solution of known regions in [Laurent series](https://en.wikipedia.org/wiki/Laurent_series "Laurent series") (about ${\displaystyle r=\infty }$), instead of [Taylor series](https://en.wikipedia.org/wiki/Taylor_series "Taylor series") (about ${\displaystyle r=0}$), to match the terms and find ${\displaystyle f_{\ell }^{m}}$.

### Electrostatics and magnetostatics

Let ${\displaystyle \mathbf {E} }$ be the electric field, ${\displaystyle \rho }$ be the electric charge density, and ${\displaystyle \varepsilon _{0}}$ be the permittivity of free space. Then [Gauss's law](https://en.wikipedia.org/wiki/Gauss%27s_law "Gauss's law") for electricity (Maxwell's first equation) in differential form states [^13] 
$$
{\displaystyle \nabla \cdot \mathbf {E} ={\frac {\rho }{\varepsilon _{0}}}.}
$$

Now, the electric field can be expressed as the negative gradient of the electric potential ${\displaystyle V}$, 
$$
{\displaystyle \mathbf {E} =-\nabla V,}
$$
 if the field is irrotational, ${\displaystyle \nabla \times \mathbf {E} =\mathbf {0} }$. The irrotationality of ${\displaystyle \mathbf {E} }$ is also known as the electrostatic condition.[^13]

$$
{\displaystyle \nabla \cdot \mathbf {E} =\nabla \cdot (-\nabla V)=-\nabla ^{2}V}
$$
 
$$
{\displaystyle \nabla ^{2}V=-\nabla \cdot \mathbf {E} }
$$

Plugging this relation into Gauss's law, we obtain Poisson's equation for electricity,[^13] 
$$
{\displaystyle \nabla ^{2}V=-{\frac {\rho }{\varepsilon _{0}}}.}
$$

In the particular case of a source-free region, ${\displaystyle \rho =0}$ and Poisson's equation reduces to Laplace's equation for the electric potential.[^13]

If the electrostatic potential ${\displaystyle V}$ is specified on the boundary of a region ${\displaystyle {\mathcal {R}}}$, then it is uniquely determined. If ${\displaystyle {\mathcal {R}}}$ is surrounded by a conducting material with a specified charge density ${\displaystyle \rho }$, and if the total charge ${\displaystyle Q}$ is known, then ${\displaystyle V}$ is also unique.[^14]

For the magnetic field, when there is no free current, 
$$
{\displaystyle \nabla \times \mathbf {H} =\mathbf {0} .}
$$
 We can thus define a [magnetic scalar potential](https://en.wikipedia.org/wiki/Magnetic_scalar_potential "Magnetic scalar potential"), *ψ*, as 
$$
{\displaystyle \mathbf {H} =-\nabla \psi .}
$$
 With the definition of **H**: 
$$
{\displaystyle \nabla \cdot \mathbf {B} =\mu _{0}\nabla \cdot \left(\mathbf {H} +\mathbf {M} \right)=0,}
$$
 it follows that 
$$
{\displaystyle \nabla ^{2}\psi =-\nabla \cdot \mathbf {H} =\nabla \cdot \mathbf {M} .}
$$

Similar to electrostatics, in a source-free region, ${\displaystyle \mathbf {M} =0}$ and Poisson's equation reduces to Laplace's equation for the magnetic scalar potential, 
$$
{\displaystyle \nabla ^{2}\psi =0}
$$

A potential that does not satisfy Laplace's equation together with the boundary condition is an invalid electrostatic or magnetic scalar potential.

## Gravitation

Let ${\displaystyle \mathbf {g} }$ be the gravitational field, ${\displaystyle \rho }$ the mass density, and ${\displaystyle G}$ the gravitational constant. Then Gauss's law for gravitation in differential form is [^15] 
$$
{\displaystyle \nabla \cdot \mathbf {g} =-4\pi G\rho .}
$$

The gravitational field is conservative and can therefore be expressed as the negative gradient of the gravitational potential: 
$$
{\displaystyle {\begin{aligned}\mathbf {g} &=-\nabla V,\\\nabla \cdot \mathbf {g} &=\nabla \cdot (-\nabla V)=-\nabla ^{2}V,\\\implies \nabla ^{2}V&=-\nabla \cdot \mathbf {g} .\end{aligned}}}
$$

Using the differential form of Gauss's law of gravitation, we have 
$$
{\displaystyle \nabla ^{2}V=4\pi G\rho ,}
$$
 which is Poisson's equation for gravitational fields.[^15]

In empty space, ${\displaystyle \rho =0}$ and we have 
$$
{\displaystyle \nabla ^{2}V=0,}
$$
 which is Laplace's equation for gravitational fields.

## Brownian motion and harmonic measure

There is a probabilistic interpretation of Laplace's equation in terms of [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion "Brownian motion"). Let ${\displaystyle D\subset \mathbf {R} ^{n}}$ be a bounded domain, let ${\displaystyle B_{t}}$ be Brownian motion started at a point ${\displaystyle x\in D}$, and let 
$$
{\displaystyle \tau _{D}=\inf\{t>0:B_{t}\notin D\}}
$$
 be its first exit time from ${\displaystyle D}$. If ${\displaystyle u}$ is harmonic in ${\displaystyle D}$ and extends continuously to ${\displaystyle {\overline {D}}}$, then 
$$
{\displaystyle u(x)=\mathbf {E} _{x}\!\left[u(B_{\tau _{D}})\right].}
$$
 This is known as [Kakutani's formula](https://en.wikipedia.org/w/index.php?title=Kakutani%27s_formula&action=edit&redlink=1 "Kakutani's formula (page does not exist)"). It expresses the value of a harmonic function at an interior point as the expected value of its boundary data at the random point where Brownian motion first exits the domain.[^16]

The distribution of the exit point ${\displaystyle B_{\tau _{D}}}$ on ${\displaystyle \partial D}$ is called the [harmonic measure](https://en.wikipedia.org/wiki/Harmonic_measure "Harmonic measure") of ${\displaystyle D}$. Thus harmonic measure gives a probabilistic solution of the [Dirichlet problem](https://en.wikipedia.org/wiki/Dirichlet_problem "Dirichlet problem"): the harmonic extension of a boundary function is obtained by averaging the boundary values against the exit distribution of Brownian motion.[^17]

This probabilistic viewpoint also gives short proofs of several basic properties of harmonic functions, including the mean value property, the maximum principle, and uniqueness for the Dirichlet problem.[^18]

### Harmonic measure

For a bounded domain ${\displaystyle D\subset \mathbf {R} ^{n}}$ and a point ${\displaystyle x\in D}$, the solution of the Dirichlet problem with boundary data ${\displaystyle f}$ can be represented in the form 
$$
{\displaystyle u(x)=\int _{\partial D}f(\xi )\,d\omega _{D}^{x}(\xi ),}
$$
 where ${\displaystyle \omega _{D}^{x}}$ is a probability measure on ${\displaystyle \partial D}$ called the **harmonic measure** of ${\displaystyle D}$ with pole at ${\displaystyle x}$. In this way, harmonic measure encodes the influence of the boundary values on the interior solution.[^19]

In classical domains such as the disk or ball, harmonic measure is absolutely continuous with respect to surface measure, and its density is the [Poisson kernel](https://en.wikipedia.org/wiki/Poisson_kernel "Poisson kernel"). Probabilistically, the harmonic measure is the distribution of the point where [Brownian motion](https://en.wikipedia.org/wiki/Brownian_motion "Brownian motion") started at ${\displaystyle x}$ first exits the domain.[^20]

## In the Schwarzschild metric

S. Persides [^21] solved the Laplace equation in [Schwarzschild spacetime](https://en.wikipedia.org/wiki/Schwarzschild_metric "Schwarzschild metric") on hypersurfaces of constant t. Using the canonical variables r, θ, φ the solution is 
$$
{\displaystyle \Psi (r,\theta ,\varphi )=R(r)Y_{l}(\theta ,\varphi ),}
$$
 where *Y <sub>l</sub>* (*θ*, *φ*) is a [spherical harmonic function](https://en.wikipedia.org/wiki/Spherical_harmonics "Spherical harmonics"), and 
$$
{\displaystyle R(r)=(-1)^{l}{\frac {(l!)^{2}r_{s}^{l}}{(2l)!}}P_{l}\left(1-{\frac {2r}{r_{s}}}\right)+(-1)^{l+1}{\frac {2(2l+1)!}{(l)!^{2}r_{s}^{l+1}}}Q_{l}\left(1-{\frac {2r}{r_{s}}}\right).}
$$

[^1]: The delta symbol, Δ, is also commonly used to represent a finite change in some quantity, for example, ${\displaystyle \Delta x=x_{1}-x_{2}}$. Its use to represent the Laplacian should not be confused with this use.

[^2]: Physical applications often take the solution that vanishes at infinity, making *A* = 0. This does not affect the angular portion of the spherical harmonics.

[^3]: Stewart, James. *[Calculus: Early Transcendentals](https://books.google.com/books?id=QyOYWR9RLI8C&q=%22Laplace%27s+equation%22)*. 7th ed., Brooks/Cole, Cengage Learning, 2012. Chapter 14: Partial Derivatives. p. 908. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-538-49790-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-538-49790-9 "Special:BookSources/978-0-538-49790-9").

[^4]: Zill, Dennis G, and Michael R Cullen. *Differential Equations with Boundary-Value Problems*. 8th edition / ed., Brooks/Cole, Cengage Learning, 2013. Chapter 12: Boundary-value Problems in Rectangular Coordinates. p. 462. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-111-82706-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-111-82706-9 "Special:BookSources/978-1-111-82706-9").

[^5]: Griffiths, David J. *[Introduction to Electrodynamics](https://books.google.com/books?id=ndAoDwAAQBAJ&q=%22Laplace%27s+equation%22)*. 4th ed., Pearson, 2013. Inner front cover. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-108-42041-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-108-42041-9 "Special:BookSources/978-1-108-42041-9").

[^6]: Gilbarg, David; Trudinger, Neil S. (2001). *Elliptic Partial Differential Equations of Second Order*. Springer. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-41160-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-41160-4 "Special:BookSources/978-3-540-41160-4").

[^7]: Axler, Sheldon; Bourdon, Paul; Ramey, Wade (2001). *Harmonic Function Theory* (2nd ed.). Springer. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-95218-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-95218-5 "Special:BookSources/978-0-387-95218-5").

[^8]: DiBenedetto, Emmanuele (2016). *Partial Differential Equations*. Birkhäuser.

[^9]: Kellogg, O. D. (1953). *Foundations of Potential Theory*. Dover.

[^10]: Maz'ya, Vladimir. ["Topics on Wiener regularity for elliptic equations"](https://users.mai.liu.se/vlama82/pdf/Mazya-Topics-Wiener.pdf) (PDF). Retrieved 2026-03-21.

[^11]: Evans, L. C. (2010). *Partial Differential Equations* (2nd ed.). American Mathematical Society. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8218-4974-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-4974-3 "Special:BookSources/978-0-8218-4974-3").

[^12]: The approach to spherical harmonics taken here is found in ([Courant & Hilbert 1962](#CITEREFCourantHilbert1962), §V.8, §VII.5).

[^13]: Griffiths, David J. *Introduction to Electrodynamics*. 4th ed., Pearson, 2013. Chapter 2: Electrostatics. p. 83-4. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-108-42041-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-108-42041-9 "Special:BookSources/978-1-108-42041-9").

[^14]: Griffiths, David J. *Introduction to Electrodynamics*. 4th ed., Pearson, 2013. Chapter 3: Potentials. p. 119-121. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-108-42041-9](https://en.wikipedia.org/wiki/Special:BookSources/978-1-108-42041-9 "Special:BookSources/978-1-108-42041-9").

[^15]: Chicone, C.; Mashhoon, B. (2011-11-20). "Nonlocal Gravity: Modified Poisson's Equation". *Journal of Mathematical Physics*. **53** (4): 042501. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1111.4702](https://arxiv.org/abs/1111.4702). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1063/1.3702449](https://doi.org/10.1063%2F1.3702449). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [118707082](https://api.semanticscholar.org/CorpusID:118707082).

[^16]: Berestycki, Nathanaël. ["Lectures on Schramm–Loewner Evolution"](https://people.math.harvard.edu/~ctm/home/text/class/harvard/219/21/html/home/sources/berestycki.pdf) (PDF). Retrieved 2026-03-21.

[^17]: Bishop, Christopher J. (2018). ["Harmonic measure: algorithms and applications"](https://www.math.stonybrook.edu/~bishop/papers/icm_proof.pdf) (PDF). *Proceedings of the International Congress of Mathematicians*. **2**: 1507–1534. Retrieved 2026-03-21.

[^18]: Berestycki, Nathanaël. ["Lectures on Schramm–Loewner Evolution"](https://people.math.harvard.edu/~ctm/home/text/class/harvard/219/21/html/home/sources/berestycki.pdf) (PDF). Retrieved 2026-03-21.

[^19]: Axler, Sheldon; Bourdon, Paul; Ramey, Wade (2001). *Harmonic Function Theory* (2nd ed.). Springer. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-95218-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-95218-5 "Special:BookSources/978-0-387-95218-5").

[^20]: Kakutani, S. (1944). ["On Brownian motion in ${\displaystyle n}$ -space"](https://doi.org/10.3792%2Fpia%2F1195572742). *Proceedings of the Imperial Academy*. **20** (9): 648–652. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.3792/pia/1195572742](https://doi.org/10.3792%2Fpia%2F1195572742).

[^21]: Persides, S. (1973). ["The Laplace and poisson equations in Schwarzschild's space-time"](https://doi.org/10.1016%2F0022-247X%2873%2990277-1). *Journal of Mathematical Analysis and Applications*. **43** (3): 571–578. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[1973JMAA...43..571P](https://ui.adsabs.harvard.edu/abs/1973JMAA...43..571P). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/0022-247X(73)90277-1](https://doi.org/10.1016%2F0022-247X%2873%2990277-1).