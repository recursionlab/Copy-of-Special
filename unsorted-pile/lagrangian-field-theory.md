---
stub: true
title: "Lagrangian Field Theory"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Lagrangian Field Theory.md"]
psi_tier: unclassified
---

# Lagrangian Field Theory

# Lagrangian Field Theory

Lagrangian Field Theory

Diffeology, Variational Cohomology, Multisymplectic Geometry
Christian Blohmann
Max Planck Institute for Mathematics, Bonn

blohmann@mpim-bonn.mpg.de

Draft version 24.0 (February 2, 2024)
The newest version and older versions are available at:
https://people.mpim-bonn.mpg.de/blohmann/LFT/

Contents

1 What is a Lagrangian Field Theory? 6
1.1 Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.2 The action principle in its “mythological” form . . . . . . . . . . . . 7
1.3 Classical mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3.1 The action principle in classical mechanics . . . . . . . . . . . 8
1.3.2 Lagrangians . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3.3 Presymplectic structure . . . . . . . . . . . . . . . . . . . . . 10
1.4 Maxwell theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.4.1 Minkowski space . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.4.2 Charges and currents . . . . . . . . . . . . . . . . . . . . . . . 13
1.4.3 Gauge symmetry . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.5 General relativity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.5.1 Hilbert–Einstein lagrangian and field equations . . . . . . . . 15
1.5.2 Mathematical features of general relativity . . . . . . . . . . . 16
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2 Diffeological spaces of fields 19
2.1 Diffeology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.1.1 From plots to concrete sheaves . . . . . . . . . . . . . . . . . . 19
2.1.2 Categorical properties of diffeological spaces . . . . . . . . . . 24
2.1.3 Categorical properties in terms of plots . . . . . . . . . . . . . 26
2.1.4 Computing limits and colimits . . . . . . . . . . . . . . . . . . 32
2.2 The tangent functor . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.2.1 Differential forms and tangent vectors . . . . . . . . . . . . . . 34
2.2.2 The tangent functor as left Kan extension . . . . . . . . . . . 36
2.2.3 The bundle of cones . . . . . . . . . . . . . . . . . . . . . . . 38
2.2.4 Compatibility with products, coproducts, and subductions . . 41
2.2.5 Representing tangent vectors by paths . . . . . . . . . . . . . 46
2.3 The diffeological space of fields . . . . . . . . . . . . . . . . . . . . . 50
2.3.1 The tangent functor of mapping spaces . . . . . . . . . . . . . 50
2.3.2 The tangent functor of the space of fields . . . . . . . . . . . . 53
2.3.3 Elastic diffeological spaces . . . . . . . . . . . . . . . . . . . . 58
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
CONTENTS 3
3 Locality and jets 67 3.1 Jets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.1.1 Jet bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67 3.1.2 Jet evaluation and prolongation . . . . . . . . . . . . . . . . . 71 3.1.3 The affine structure of jet bundles . . . . . . . . . . . . . . . . 74
3.2 Local maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 3.2.1 Local maps and differential operators . . . . . . . . . . . . . . 77 3.2.2 Local maps of products . . . . . . . . . . . . . . . . . . . . . . 80 3.2.3 Linear local maps of jet order 0 and 1 . . . . . . . . . . . . . . 81
3.3 The theorems of Peetre and Slovák . . . . . . . . . . . . . . . . . . . 82 3.3.1 Locality in topology . . . . . . . . . . . . . . . . . . . . . . . 82 3.3.2 Peetre’s theorem . . . . . . . . . . . . . . . . . . . . . . . . . 83 3.3.3 The nonlinear case . . . . . . . . . . . . . . . . . . . . . . . . 85
3.4 Infinite jets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
4 Pro-manifolds 90 4.1 Ind-categories and pro-categories . . . . . . . . . . . . . . . . . . . . 90
4.1.1 Filtered and cofiltered categories . . . . . . . . . . . . . . . . 90 4.1.2 Definition of ind/pro-categories . . . . . . . . . . . . . . . . . 94 4.1.3 Functoriality and naturality of the ind/pro-extension . . . . . 96 4.1.4 Finite limits and colimits in ind/pro-categories . . . . . . . . . 99 4.1.5 Ind/pro-objects versus colimits/limits . . . . . . . . . . . . . . 101 4.1.6 Concrete structures . . . . . . . . . . . . . . . . . . . . . . . . 103 4.1.7 Tensor products, algebras, derivations . . . . . . . . . . . . . . 104
4.2 Sequential ind/pro-objects . . . . . . . . . . . . . . . . . . . . . . . . 109 4.2.1 Representation of morphisms . . . . . . . . . . . . . . . . . . 110 4.2.2 Sections, retracts, isomorphisms, derivations . . . . . . . . . . 112
4.3 Differential geometry on pro-manifolds . . . . . . . . . . . . . . . . . 114 4.3.1 Tangent bundle and vector fields . . . . . . . . . . . . . . . . 115 4.3.2 Vector fields as derivations . . . . . . . . . . . . . . . . . . . . 117 4.3.3 Differential forms . . . . . . . . . . . . . . . . . . . . . . . . . 120 4.3.4 Inner derivative . . . . . . . . . . . . . . . . . . . . . . . . . . 121 4.3.5 Cartan calculus . . . . . . . . . . . . . . . . . . . . . . . . . . 122
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
5 Variational cohomology 126 5.1 De Rham complex of the pro-manifold of infinite jets . . . . . . . . . 126
5.1.1 Vertical and horizontal tangent vectors . . . . . . . . . . . . . 127 5.1.2 The variational bicomplex . . . . . . . . . . . . . . . . . . . . 133 5.1.3 Strictly vertical and horizontal vector fields . . . . . . . . . . . 137 5.1.4 Equivalence of strictly vertical and local vector fields . . . . . 140 5.1.5 Basic forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
5.2 Cohomology of the variational bicomplex . . . . . . . . . . . . . . . . 145 5.2.1 Cohomological partial integration . . . . . . . . . . . . . . . . 145 5.2.2 The acyclicity theorem . . . . . . . . . . . . . . . . . . . . . . 147 5.2.3 The cohomology of the Euler–Lagrange complex . . . . . . . . 148
4 CONTENTS
6 The cohomological action principle 150 6.1 Local diffeological forms . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.1.1 Differential forms on elastic diffeological spaces . . . . . . . . 151 6.1.2 Local forms on F ×M . . . . . . . . . . . . . . . . . . . . . . 152
6.2 The action principle . . . . . . . . . . . . . . . . . . . . . . . . . . . 155 6.2.1 Euler–Lagrange form . . . . . . . . . . . . . . . . . . . . . . . 155 6.2.2 The Euler–Lagrange theorem . . . . . . . . . . . . . . . . . . 156 6.2.3 The cohomological Euler–Lagrange theorem . . . . . . . . . . 157 6.2.4 The inverse problem of Lagrangian Field Theory . . . . . . . . 159
7 Symmetries 160 7.1 Noether’s theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
7.1.1 Symmetries of the action class . . . . . . . . . . . . . . . . . . 160 7.1.2 Currents and charges . . . . . . . . . . . . . . . . . . . . . . . 161 7.1.3 Noether’s first theorem . . . . . . . . . . . . . . . . . . . . . . 163 7.1.4 Noether’s second theorem . . . . . . . . . . . . . . . . . . . . 164
7.2 Jacobi fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167 7.2.1 Linearization of the Euler-Lagrange equation . . . . . . . . . . 167 7.2.2 Tangent vectors on shell . . . . . . . . . . . . . . . . . . . . . 170 7.2.3 Jacobi fields in riemannian geometry . . . . . . . . . . . . . . 171 7.2.4 Symmetries and Jacobi fields . . . . . . . . . . . . . . . . . . 171 7.2.5 Presymplectic structures . . . . . . . . . . . . . . . . . . . . . 173
8 Multisymplectic structure 176 8.1 Operads and homotopy algebraic structures . . . . . . . . . . . . . . 176
8.1.1 Linear operads . . . . . . . . . . . . . . . . . . . . . . . . . . 176 8.1.2 Symmetric linear operads . . . . . . . . . . . . . . . . . . . . 181 8.1.3 Homotopy algebras . . . . . . . . . . . . . . . . . . . . . . . . 185 8.1.4 Morphisms of homotopy algebras . . . . . . . . . . . . . . . . 189 8.1.5 L∞-algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
8.2 The L∞-algebra of conserved currents . . . . . . . . . . . . . . . . . . 195 8.2.1 The Poisson algebra of a presymplectic manifold . . . . . . . . 195 8.2.2 The L∞-algebra of a premultisymplectic form . . . . . . . . . 197 8.2.3 Premultisymplectic structure of a Lagrangian Field Theory . . 197
8.3 Homotopy momentum maps . . . . . . . . . . . . . . . . . . . . . . . 200 8.3.1 Hamiltonian actions on presymplectic manifolds . . . . . . . . 200 8.3.2 Obstruction cohomology . . . . . . . . . . . . . . . . . . . . . 201 8.3.3 Homotopy momentum maps . . . . . . . . . . . . . . . . . . . 206 8.3.4 Manifest diffeomorphism symmetries . . . . . . . . . . . . . . 208
9 Examples 211 9.1 Particle in a potential . . . . . . . . . . . . . . . . . . . . . . . . . . . 211 9.2 Free particle on a curved background . . . . . . . . . . . . . . . . . . 212 9.3 Gauge theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
9.3.1 Review of connections on principal bundles . . . . . . . . . . . 212 9.3.2 Yang-Mills gauge theory . . . . . . . . . . . . . . . . . . . . . 220
9.4 Chern-Simons theory . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
CONTENTS 5
9.5 General relativity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223 9.5.1 The action of spacetime vector fields . . . . . . . . . . . . . . 224 9.5.2 Jet coordinates . . . . . . . . . . . . . . . . . . . . . . . . . . 224 9.5.3 Action of spacetime vector fields on infinite jets . . . . . . . . 226 9.5.4 Covariant and contravariant families of forms . . . . . . . . . 227 9.5.5 Covariant derivative of families of forms . . . . . . . . . . . . 229 9.5.6 Divergence formulas . . . . . . . . . . . . . . . . . . . . . . . 230 9.5.7 Euler-Lagrange and boundary form . . . . . . . . . . . . . . . 233 9.5.8 Invariance of the Lepage form . . . . . . . . . . . . . . . . . . 234
9.6 Poisson sigma models . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
A Graded algebra 237 A.1 Graded vector spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
A.1.1 Tensor product . . . . . . . . . . . . . . . . . . . . . . . . . . 237 A.1.2 Décalage isomorphism . . . . . . . . . . . . . . . . . . . . . . 238 A.1.3 Graded mapping space . . . . . . . . . . . . . . . . . . . . . . 239 A.1.4 Total vector space of a graded vector space . . . . . . . . . . . 240 A.1.5 Bigraded mapping space . . . . . . . . . . . . . . . . . . . . . 241
A.2 Graded algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241 A.2.1 Graded associative algebras . . . . . . . . . . . . . . . . . . . 241 A.2.2 Graded Lie algebras . . . . . . . . . . . . . . . . . . . . . . . 242
A.3 Differential graded vector spaces . . . . . . . . . . . . . . . . . . . . . 242 A.3.1 Differentials . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242 A.3.2 Chain complexes . . . . . . . . . . . . . . . . . . . . . . . . . 244
B Useful facts 245
Bibliography 248

Chapter 1

What is a Lagrangian Field Theory?

1.1 Fields
In classical physics, a field describes the state of a system by assigning to every point of a geometric space or object the value of some physical quantity at that point. An example of a field is the function that assigns to every point of a solid the temperature at that point. Another example is the field that assigns the wind velocity to every point on the surface of the Earth. Such assignments are generally assumed to be smooth maps. This is an idealization, of course, as the two examples show, in which the physical systems consist of discrete atoms. But it has led to very accurate descriptions of physical phenomena. In mathematics, the idealization is promoted to a definition.
Definition 1.1.1. A field is a smooth section of a smooth fiber bundle F → M . The set of all fields is denoted by F := Γ∞(M,F ).
Example 1.1.2. In the example of the temperature field, the fiber bundle is F = M × [0,∞)→M , where M is the manifold describing the solid. This shows that F is generally not a vector bundle. In the example of the air velocity field, the fiber bundle is the tangent bundle F = TS2 → S2 of the sphere, which shows that F is generally not a trivial bundle.
Terminology 1.1.3. In physics, the base manifold of the fiber bundle is called the background geometry or the spacetime, the latter especially in fundamental theories such as gauge theory or general relativity. F is sometimes called the con-figuration bundle or configuration space bundle, and the typical fiber of F the configuration space or the field content. F is usually called the space of fields, although it often remains unclear or implicit what “space” means mathematically.
Example 1.1.4. Let M = R and F := Q × R be a trivial bundle. Then F = C∞(R, Q) is the space of smooth paths in Q. If we replace R with S1 then F is the free loop space of Q.
1.2 The action principle in its “mythological” form 7
1.2 The action principle in its “mythological” form
In a field theory, the fields are usually subject to a field equation f(φ) = 0, where f : F → V is a map to a vector space V . The solutions of the field equation are those fields that are governed by the laws of physics or that possess some desired mathematical properties. Typically, f is a differential operator.
Example 1.2.1. Let M ⊂ R3 be a 3-dimensional submanifold with boundary ∂M . Let F := M × R → M , so that F = C∞(M). In electrostatics, φ ∈ C∞(M) is viewed as the electric potential. The field equation is ∆φ = 0, where ∆ is the Laplace operator. The solutions of the field equation are harmonic functions subject to boundary conditions on ∂M .
Terminology 1.2.2. In physics, the fields that solve the field equations are often called on-shell and those that do not off-shell. This terminology comes from the so-called mass-shell (German: Massenschale), which is the positive energy sheet of the hyperboloid of the 4-momentum (p0, p1, p2, p3) ∈ R4 of a relativistic particle of rest mass m2 = (p0)
2− (p1) 2− (p2)
2− (p3) 2. In this sense “shell” is a mistranslation
of “Schale”. In early quantum field theory, where the momenta are represented by partial derivatives on the wave functions, the mass-shell has come to denote the space of solutions of the equation of motion □φ = m2 of the free relativistic particle.
The set of solutions of the field equation will be denoted by Fshell := f−1(0). In general, Fshell ⊂ F is not a smooth variety, but has singularities. The field equations are often quite complicated. The main tool to study them is the action principle. In its ideal form it is stated as follows.
Action principle 1.2.3. There is a smooth function
S : F −→ R ,
called the action, such that φ ∈ F is a solution of the field equation if and only if it is a critical point of S.
The value of this principle is that it is usually much easier to construct and study a field theory via its action than via its field equations. For example, a diffeomorphism Φ ∈ Diff(F) acts naturally on functions on F by pullback. So Φ is a symmetry of the field theory given by an action S if Φ∗S = S. It follows that Φ maps critical points of S to critical points, i.e. Φ(Fshell) = Fshell. Conversely, if the symmetries are known, like the Lorentz transformations of special relativity, the requirement for S to be invariant restricts the possible actions of the theory. For such reasons, the action principle is one of the most important guiding principles in both classical and quantum field theory.
Mathematically, however, the action principle 1.2.3 is often not rigorously true. In his 2011 Felix Klein lectures Graeme Segal called it the “mythological picture” of field theory. One of the main goal of these notes is to explain how the action principle can be restated so that it is rigorously true, sufficiently general to cover the most relevant field theories, such as general relativity, and compatible with the current mathematical tools used in field theory.
8 1. What is a Lagrangian Field Theory?
1.3 Classical mechanics
1.3.1 The action principle in classical mechanics
What is the action? And how do we get from the action to the field equations? The basic example is a classical mechanical system, where M = R is time and F = Q×R, so that a field is a smooth path q : R→ Q. Let us assume for simplicity that Q = Rn. When the system is at rest, it will have to be at a critical point of the potential energy V : Q→ R. When the system moves, the kinetic energy has to be taken into account as well. The action turns out to be given by the difference of kinetic and potential energy,
S(q) :=
∫ R
{ 1 2 q̇i(t)q̇i(t)− V
( q(t)
)} dt ,
where qi(t) are the components of the path, where repeated indices are being summed over, q̇i(t)q̇i(t) =
∑n i=1 q̇
i(t)q̇i(t), and where we have chosen units in which the mass is m = 1.
Problem 1.3.1. The integral over R that defines the action is generally divergent.
In a first attempt to avoid problem 1.3.1, we could consider only those q that have a finite action, but the solutions of the field equation may not satisfy this condition. For example, consider the case of a free particle where V (q) = 0. The solutions of the equations of motion are paths of constant velocity. So only if the velocity is zero the action is finite.
In a second attempt to solve problem 1.3.1, we as mathematicians could assume M to be closed, that is, compact without boundary [Abb01]. In the case of classical mechanics this would mean, however, that time is S1 so that we would only consider periodic solutions. The assumption that M is closed will also exclude some of the most interesting spacetimes, like Minkowski spacetime or many realistic physical models for the curved spacetime of the universe we live in.
In a third attempt, we can restrict the domain of integration to a compact interval [a, b] for the action to be finite. We will denote this action by S[a,b]. Following the action principle 1.2.3, we now have to compute the critical points of S[a,b]. Let q : [a, b] → Q be a smooth path. Since we have assumed for simplicity that Q is a vector space, TqF ∼= F. Therefore, a tangent vector ξ ∈ TqF can be represented by smooth family of paths R ∋ ε 7→ qε ∈ C∞(R, Q) given by qε = q+εξ. The derivative of S[a,b] in the direction of ξ is obtained by inserting q+ εξ and expanding the result to first order in ε.
S[a,b](q + εξ)− S
a,b

= ε
∫ b
a
{ q̇i(t)ξ̇i(t)− ∂V
∂qi ( q(t)
) ξi(t)
} dt+ O(ε2)
= ε
∫ b
a
{ d dt
( q̇i(t)ξi(t)
) −q̈i(t)ξi(t)− ∂V
∂qi ( q(t)
) ξi(t)
} dt+ O(ε2)
= − ε ∫ b
a
{ q̈i(t) +
∂V
∂qi ( q(t)
)} ξi(t) dt+ ε
∫ b
a
d
dt
( q̇i(t)ξi(t)
) dt+ O(ε2) .
1.3 Classical mechanics 9
Let us first consider variations ξi that have compact support in [a, b], so that the second integral vanishes. The first integral vanishes for all ξi if and only if qi satisfies the field equation
q̈i = −∂V ∂qi
,
which is the equation of motion of a point particle in a potential V . The second integral is given by∫ b
a
d
dt
( q̇i(t)ξi(t)
) dt = q̇i(b) ξi(b)− q̇i(a) ξi(a) .
Now we consider variations ξi that have their support concentrated in small neigh-borhoods around the boundary points a and b. By keeping ξi(a) and ξi(b) constant while shrinking the support, we can make the first integral arbitrarily small. The conclusion is that the second integral has to vanish for all ξi independently of the first, which is the case if and only if
q̇i(a) = 0 and q̇i(b) = 0 .
This is certainly not a condition we want to impose on q. We can modify the action principle by requiring ξi(a) = 0 = ξi(b). But then
the solutions of the field equation are not the critical points of S but rather points where the derivative of S vanishes on a subset of vectors in TqF. Moreover, we have to require the conditions for all compact intervals [a, b]. In terms of differential topology, we are pairing the de Rham 1-cocycle represented by the integrand with the 1-cycle represented by the interval. In light of the Poincaré duality between cohomology and homology on a manifold, this suggest that the derivation of the field equation might be formulated in the framework of cohomology. We will return to this point of view in Chapter 5 and Chapter 6.
1.3.2 Lagrangians
In the example of classical mechanics we have seen that the action is obtained by integrating for every field q a volume form over the spacetime manifold R.
Definition 1.3.2. A smooth function L : F → Ωn(M), where n = dimM , is called a lagrangian.
Remark 1.3.3. For simplicity, we shall assume that M is oriented. If M is non-orientable, we have to tensor before integration with the determinant bundle of M as it is done in [DF99].
Given a lagrangian L, we tentatively define the action by
S(φ) :=
∫ M
L(φ) .
But, as we have seen, even for classical mechanics the action is generally not finite, so it is certainly not a smooth map to R. The issues come from the integration over the non-closed manifold R.
10 1. What is a Lagrangian Field Theory?
When we review the derivation of the equation of motion carefully, we see that we did not need to compute any integrals. All we did is to discard exact terms under the integral. This means that we can just as well study the cohomology class of the integrand without ever pairing it with the fundamental class [M ]. We will return to this idea in Chapter 6.
Definition 1.3.4. A Lagrangian Field Theory (LFT) consists of a smooth fiber bundle F →M and a lagrangian L : F → Ωn(M).
For a general action F → R there is no mathematical reason why the critical points should be the solution of a PDE, as is the case for most LFTs that come to mind. The following condition guarantees that the Euler–Lagrange equation is a PDE.
Definition 1.3.5. A lagrangian L : F → Ωn(M) is called local if there is a natural number k ≥ 0, such that the value of L(φ) at m depends smoothly on m and only the partial derivatives of φ at m up to order k.
1.3.3 Presymplectic structure
The vertical tangent bundle of πQ : TQ→ Q is given by
V TQ = ker(TπQ : TTQ→ TQ) ∼= TQ×Q TQ .
Let f : TQ → R be a smooth function. Restricting the differential df : TTQ → R to the vertical tangent bundle yields a map
df ∣∣ V TQ
: TQ×Q TQ −→ R .
Since this map is linear in the second factor (the one that can be identified with the vertical tangent vectors), we can identify it with a smooth map
Legf : TQ −→ T ∗Q ,
which is the Legendre transformation generated by f . Let ωT ∗Q denote the canonical symplectic form on T ∗Q. Its pullback by the
Legendre transformation,
ω = Leg∗fωT ∗Q ,
is a presymplectic form on TQ, which is symplectic if and only if Legf is a local diffeomorphism.
Definition 1.3.6. The function f : TQ → R is said to satisfy the Legendre condition if Legf is a local diffeomorphism.
The lagrangian function for a particle in a time-dependent potential,
L = 1

[... content truncated ...]

---

*Source: `Lagrangian Field Theory.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
