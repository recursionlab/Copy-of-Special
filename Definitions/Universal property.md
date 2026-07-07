---
title: "Universal property"
source: "https://en.wikipedia.org/wiki/Universal_property"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2001-12-08
created: 2026-04-10
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Universal_morphism_definition.svg/250px-Universal_morphism_definition.svg.png)

The typical diagram of the definition of a universal morphism.

In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), more specifically in [category theory](https://en.wikipedia.org/wiki/Category_theory "Category theory"), a **universal property** is a property that characterizes [up to](https://en.wikipedia.org/wiki/Up_to "Up to") an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism") the result of some constructions. Thus, universal properties can be used for defining some objects independently from the method chosen for constructing them. For example, the definitions of the [integers](https://en.wikipedia.org/wiki/Integer "Integer") from the [natural numbers](https://en.wikipedia.org/wiki/Natural_number "Natural number"), of the [rational numbers](https://en.wikipedia.org/wiki/Rational_number "Rational number") from the integers, of the [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") from the rational numbers, and of [polynomial rings](https://en.wikipedia.org/wiki/Polynomial_ring "Polynomial ring") from the [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") of their coefficients can all be done in terms of universal properties. In particular, the concept of universal property allows a simple proof that all [constructions of real numbers](https://en.wikipedia.org/wiki/Constructions_of_real_numbers "Constructions of real numbers") are equivalent: it suffices to prove that they satisfy the same universal property.

Technically, a universal property is defined in terms of [categories](https://en.wikipedia.org/wiki/Category_\(mathematics\) "Category (mathematics)") and [functors](https://en.wikipedia.org/wiki/Functor "Functor") by means of a **universal morphism** (see [§ Formal definition](#Formal_definition), below). Universal morphisms can also be thought more abstractly as [initial or terminal objects](https://en.wikipedia.org/wiki/Initial_and_terminal_objects "Initial and terminal objects") of a [comma category](https://en.wikipedia.org/wiki/Comma_category "Comma category") (see [§ Connection with comma categories](#Connection_with_comma_categories), below).

Universal properties occur almost everywhere in mathematics, and the use of the concept allows the use of general properties of universal properties for easily proving some properties that would need boring verifications otherwise. For example, given a [commutative ring](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring") R, the [field of fractions](https://en.wikipedia.org/wiki/Field_of_fractions "Field of fractions") of the [quotient ring](https://en.wikipedia.org/wiki/Quotient_ring "Quotient ring") of R by a [prime ideal](https://en.wikipedia.org/wiki/Prime_ideal "Prime ideal") p can be identified with the [residue field](https://en.wikipedia.org/wiki/Residue_field "Residue field") of the [localization](https://en.wikipedia.org/wiki/Localization_\(commutative_algebra\) "Localization (commutative algebra)") of R at p; that is ${\displaystyle R_{p}/pR_{p}\cong \operatorname {Frac} (R/p)}$ (all these constructions can be defined by universal properties).

Other objects that can be defined by universal properties include: all [free objects](https://en.wikipedia.org/wiki/Free_object "Free object"), [direct products](https://en.wikipedia.org/wiki/Direct_product "Direct product") and [direct sums](https://en.wikipedia.org/wiki/Direct_sum "Direct sum"), [free groups](https://en.wikipedia.org/wiki/Free_group "Free group"), [free lattices](https://en.wikipedia.org/wiki/Free_lattice "Free lattice"), [Grothendieck group](https://en.wikipedia.org/wiki/Grothendieck_group "Grothendieck group"), [completion of a metric space](https://en.wikipedia.org/wiki/Completion_of_a_metric_space "Completion of a metric space"), [completion of a ring](https://en.wikipedia.org/wiki/Completion_of_a_ring "Completion of a ring"), [Dedekind–MacNeille completion](https://en.wikipedia.org/wiki/Dedekind%E2%80%93MacNeille_completion "Dedekind–MacNeille completion"), [product topologies](https://en.wikipedia.org/wiki/Product_topology "Product topology"), [Stone–Čech compactification](https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification "Stone–Čech compactification"), [tensor products](https://en.wikipedia.org/wiki/Tensor_product "Tensor product"), [inverse limit](https://en.wikipedia.org/wiki/Inverse_limit "Inverse limit") and [direct limit](https://en.wikipedia.org/wiki/Direct_limit "Direct limit"), [kernels](https://en.wikipedia.org/wiki/Kernel_\(linear_algebra\) "Kernel (linear algebra)") and [cokernels](https://en.wikipedia.org/wiki/Cokernel "Cokernel"), [quotient groups](https://en.wikipedia.org/wiki/Quotient_group "Quotient group"), [quotient vector spaces](https://en.wikipedia.org/wiki/Quotient_vector_space "Quotient vector space"), and other [quotient spaces](https://en.wikipedia.org/wiki/Quotient_space_\(disambiguation\) "Quotient space (disambiguation)").

## Motivation

Before giving a formal definition of universal properties, we offer some motivation for studying such constructions.

- The concrete details of a given construction may be messy, but if the construction satisfies a universal property, one can forget all those details: all there is to know about the construction is already contained in the universal property. Proofs often become short and elegant if the universal property is used rather than the concrete details. For example, the [tensor algebra](https://en.wikipedia.org/wiki/Tensor_algebra "Tensor algebra") of a [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") is slightly complicated to construct, but much easier to deal with by its universal property.
- Universal properties define objects uniquely up to a unique [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism").[^1] Therefore, one strategy to prove that two objects are isomorphic is to show that they satisfy the same universal property.
- Universal constructions are functorial in nature: if one can carry out the construction for every object in a category *C* then one obtains a [functor](https://en.wikipedia.org/wiki/Functor "Functor") on *C*. Furthermore, this functor is a [right or left adjoint](https://en.wikipedia.org/wiki/Adjoint_functors "Adjoint functors") to the functor *U* used in the definition of the universal property.[^2]
- Universal properties occur everywhere in mathematics. By understanding their abstract properties, one obtains information about all these constructions and can avoid repeating the same analysis for each individual instance.

## Formal definition

To understand the definition of a universal construction, it is important to look at examples. Universal constructions were not defined out of thin air, but were rather defined after mathematicians began noticing a pattern in many mathematical constructions (see Examples below). Hence, the definition may not make sense to one at first, but will become clear when one reconciles it with concrete examples.

Let ${\displaystyle F:{\mathcal {C}}\to {\mathcal {D}}}$ be a functor between categories ${\displaystyle {\mathcal {C}}}$ and ${\displaystyle {\mathcal {D}}}$. In what follows, let ${\displaystyle X}$ be an object of ${\displaystyle {\mathcal {D}}}$, ${\displaystyle A}$ and ${\displaystyle A'}$ be objects of ${\displaystyle {\mathcal {C}}}$, and ${\displaystyle h:A\to A'}$ be a morphism in ${\displaystyle {\mathcal {C}}}$.

Then, the functor ${\displaystyle F}$ maps ${\displaystyle A}$, ${\displaystyle A'}$ and ${\displaystyle h}$ in ${\displaystyle {\mathcal {C}}}$ to ${\displaystyle F(A)}$, ${\displaystyle F(A')}$ and ${\displaystyle F(h)}$ in ${\displaystyle {\mathcal {D}}}$.

A **universal morphism from ${\displaystyle X}$ to ${\displaystyle F}$** is a unique pair ${\displaystyle (A,u:X\to F(A))}$ which has the following property, commonly referred to as a **universal property**:

For any morphism of the form ${\displaystyle f:X\to F(A')}$ in ${\displaystyle {\mathcal {D}}}$, there exists a *unique* morphism ${\displaystyle h:A\to A'}$ in ${\displaystyle {\mathcal {C}}}$ such that the following diagram [commutes](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram"):

![The typical diagram of the definition of a universal morphism.](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Universal_morphism_definition.svg/330px-Universal_morphism_definition.svg.png)

The typical diagram of the definition of a universal morphism.

We can [dualize](https://en.wikipedia.org/wiki/Dual_\(category_theory\) "Dual (category theory)") this categorical concept. A **universal morphism from ${\displaystyle F}$ to ${\displaystyle X}$** is a unique pair ${\displaystyle (A,u:F(A)\to X)}$ that satisfies the following universal property:

For any morphism of the form ${\displaystyle f:F(A')\to X}$ in ${\displaystyle {\mathcal {D}}}$, there exists a *unique* morphism ${\displaystyle h:A'\to A}$ in ${\displaystyle {\mathcal {C}}}$ such that the following diagram commutes:

![The most important arrow here is '"`UNIQ--postMath-00000023-QINU`"' which establishes the universal property.](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Universal_definition_dualized.svg/330px-Universal_definition_dualized.svg.png)

The most important arrow here is {\\displaystyle u:F(A)\\to X} which establishes the universal property.

Note that in each definition, the arrows are reversed. Both definitions are necessary to describe universal constructions which appear in mathematics; but they also arise due to the inherent duality present in category theory. In either case, we say that the pair ${\displaystyle (A,u)}$ which behaves as above satisfies a universal property.

## Connection with comma categories

Universal morphisms can be described more concisely as initial and terminal objects in a [comma category](https://en.wikipedia.org/wiki/Comma_category "Comma category") (i.e. one where morphisms are seen as objects in their own right).

Let ${\displaystyle F:{\mathcal {C}}\to {\mathcal {D}}}$ be a functor and ${\displaystyle X}$ an object of ${\displaystyle {\mathcal {D}}}$. Then recall that the comma category ${\displaystyle (X\downarrow F)}$ is the category where

- Objects are pairs of the form ${\displaystyle (B,f:X\to F(B))}$, where ${\displaystyle B}$ is an object in ${\displaystyle {\mathcal {C}}}$
- A morphism from ${\displaystyle (B,f:X\to F(B))}$ to ${\displaystyle (B',f':X\to F(B'))}$ is given by a morphism ${\displaystyle h:B\to B'}$ in ${\displaystyle {\mathcal {C}}}$ such that the diagram commutes:
![A morphism in the comma category is given by the morphism '"`UNIQ--postMath-00000030-QINU`"' which also makes the diagram commute.](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Definition_of_a_morphism_in_a_comma_category.svg/330px-Definition_of_a_morphism_in_a_comma_category.svg.png)

A morphism in the comma category is given by the morphism {\\displaystyle h:B\\to B'} which also makes the diagram commute.

Now suppose that the object ${\displaystyle (A,u:X\to F(A))}$ in ${\displaystyle (X\downarrow F)}$ is initial. Then for every object ${\displaystyle (A',f:X\to F(A'))}$, there exists a unique morphism ${\displaystyle h:A\to A'}$ such that the following diagram commutes.

![This demonstrates the connection between a universal diagram being an initial object in a comma category.](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Connection_between_universal_diagrams_and_comma_categories.svg/960px-Connection_between_universal_diagrams_and_comma_categories.svg.png)

This demonstrates the connection between a universal diagram being an initial object in a comma category.

Note that the equality here simply means the diagrams are the same. Also note that the diagram on the right side of the equality is the exact same as the one offered in defining a **universal morphism from ${\displaystyle X}$ to ${\displaystyle F}$**. Therefore, we see that a universal morphism from ${\displaystyle X}$ to ${\displaystyle F}$ is equivalent to an initial object in the comma category ${\displaystyle (X\downarrow F)}$.

Conversely, recall that the comma category ${\displaystyle (F\downarrow X)}$ is the category where

- Objects are pairs of the form ${\displaystyle (B,f:F(B)\to X)}$ where ${\displaystyle B}$ is an object in ${\displaystyle {\mathcal {C}}}$
- A morphism from ${\displaystyle (B,f:F(B)\to X)}$ to ${\displaystyle (B',f':F(B')\to X)}$ is given by a morphism ${\displaystyle h:B\to B'}$ in ${\displaystyle {\mathcal {C}}}$ such that the diagram commutes:
![This simply demonstrates the definition of a morphism in a comma category.](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Definition_of_a_morphism_in_a_comma_category_1.svg/330px-Definition_of_a_morphism_in_a_comma_category_1.svg.png)

This simply demonstrates the definition of a morphism in a comma category.

Suppose ${\displaystyle (A,u:F(A)\to X)}$ is a terminal object in ${\displaystyle (F\downarrow X)}$. Then for every object ${\displaystyle (A',f:F(A')\to X)}$, there exists a unique morphism ${\displaystyle h:A'\to A}$ such that the following diagrams commute.

![This shows that a terminal object in a specific comma category corresponds to a universal morphism.](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Connection_between_comma_category_and_universal_properties.svg/960px-Connection_between_comma_category_and_universal_properties.svg.png)

This shows that a terminal object in a specific comma category corresponds to a universal morphism.

The diagram on the right side of the equality is the same diagram pictured when defining a **universal morphism from ${\displaystyle F}$ to ${\displaystyle X}$**. Hence, a universal morphism from ${\displaystyle F}$ to ${\displaystyle X}$ corresponds with a terminal object in the comma category ${\displaystyle (F\downarrow X)}$.

## Examples

Below are a few examples, to highlight the general idea. The reader can construct numerous other examples by consulting the articles mentioned in the introduction.

### Tensor algebras

Let ${\displaystyle {\mathcal {C}}}$ be the [category of vector spaces](https://en.wikipedia.org/wiki/Category_of_vector_spaces "Category of vector spaces") **${\displaystyle K}$ -Vect** over a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") ${\displaystyle K}$ and let ${\displaystyle {\mathcal {D}}}$ be the category of [algebras](https://en.wikipedia.org/wiki/Algebra_over_a_field "Algebra over a field") **${\displaystyle K}$ -Alg** over ${\displaystyle K}$ (assumed to be [unital](https://en.wikipedia.org/wiki/Unital_algebra "Unital algebra") and [associative](https://en.wikipedia.org/wiki/Associative_algebra "Associative algebra")). Let 
$$
{\displaystyle U:K{\text{-}}\mathbf {Alg} \to K{\text{-}}\mathbf {Vect} }
$$
 be the [forgetful functor](https://en.wikipedia.org/wiki/Forgetful_functor "Forgetful functor") which assigns to each algebra its underlying vector space.

Given any [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") ${\displaystyle V}$ over ${\displaystyle K}$ we can construct the [tensor algebra](https://en.wikipedia.org/wiki/Tensor_algebra "Tensor algebra") ${\displaystyle T(V)}$. The tensor algebra is characterized by the fact:

“Any linear map from ${\displaystyle V}$ to an algebra ${\displaystyle A}$ can be uniquely extended to an [algebra homomorphism](https://en.wikipedia.org/wiki/Algebra_homomorphism "Algebra homomorphism") from ${\displaystyle T(V)}$ to ${\displaystyle A}$.”

This statement is an initial property of the tensor algebra since it expresses the fact that the pair ${\displaystyle (T(V),i)}$, where ${\displaystyle i:V\to U(T(V))}$ is the inclusion map, is a universal morphism from the vector space ${\displaystyle V}$ to the functor ${\displaystyle U}$.

Since this construction works for any vector space ${\displaystyle V}$, we conclude that ${\displaystyle T}$ is a functor from **${\displaystyle K}$ -Vect** to **${\displaystyle K}$ -Alg**. This means that ${\displaystyle T}$ is *left adjoint* to the forgetful functor ${\displaystyle U}$ (see the section below on [relation to adjoint functors](#Relation_to_adjoint_functors)).

### Products

A [categorical product](https://en.wikipedia.org/wiki/Categorical_product "Categorical product") can be characterized by a universal construction. For concreteness, one may consider the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") in **[Set](https://en.wikipedia.org/wiki/Set_\(category_theory\) "Set (category theory)")**, the [direct product](https://en.wikipedia.org/wiki/Direct_product "Direct product") in **[Grp](https://en.wikipedia.org/wiki/Grp_\(category_theory\) "Grp (category theory)")**, or the [product topology](https://en.wikipedia.org/wiki/Product_topology "Product topology") in **[Top](https://en.wikipedia.org/wiki/Top_\(category_theory\) "Top (category theory)")**, where products exist.

Let ${\displaystyle X}$ and ${\displaystyle Y}$ be objects of a category ${\displaystyle {\mathcal {C}}}$ with finite products. The product of ${\displaystyle X}$ and ${\displaystyle Y}$ is an object ${\displaystyle X}$ × ${\displaystyle Y}$ together with two morphisms

${\displaystyle \pi _{1}}$: ${\displaystyle X\times Y\to X}$

${\displaystyle \pi _{2}}$: ${\displaystyle X\times Y\to Y}$

such that for any other object ${\displaystyle Z}$ of ${\displaystyle {\mathcal {C}}}$ and morphisms ${\displaystyle f:Z\to X}$ and ${\displaystyle g:Z\to Y}$ there exists a unique morphism ${\displaystyle h:Z\to X\times Y}$ such that ${\displaystyle f=\pi _{1}\circ h}$ and ${\displaystyle g=\pi _{2}\circ h}$.

To understand this characterization as a universal property, take the category ${\displaystyle {\mathcal {D}}}$ to be the [product category](https://en.wikipedia.org/wiki/Product_category "Product category") ${\displaystyle {\mathcal {C}}\times {\mathcal {C}}}$ and define the [diagonal functor](https://en.wikipedia.org/wiki/Diagonal_functor "Diagonal functor")

${\displaystyle \Delta :{\mathcal {C}}\to {\mathcal {C}}\times {\mathcal {C}}}$

by ${\displaystyle \Delta (X)=(X,X)}$ and ${\displaystyle \Delta (f:X\to Y)=(f,f)}$. Then ${\displaystyle (X\times Y,(\pi _{1},\pi _{2}))}$ is a universal morphism from ${\displaystyle \Delta }$ to the object ${\displaystyle (X,Y)}$ of ${\displaystyle {\mathcal {C}}\times {\mathcal {C}}}$: if ${\displaystyle (f,g)}$ is any morphism from ${\displaystyle (Z,Z)}$ to ${\displaystyle (X,Y)}$, then it must equal a morphism ${\displaystyle \Delta (h:Z\to X\times Y)=(h,h)}$ from ${\displaystyle \Delta (Z)=(Z,Z)}$ to ${\displaystyle \Delta (X\times Y)=(X\times Y,X\times Y)}$ followed by ${\displaystyle (\pi _{1},\pi _{2})}$. As a commutative diagram:

![Commutative diagram showing how products have a universal property.](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Universal-property-products.svg/500px-Universal-property-products.svg.png)

Commutative diagram showing how products have a universal property.

For the example of the Cartesian product in **Set**, the morphism ${\displaystyle (\pi _{1},\pi _{2})}$ comprises the two projections ${\displaystyle \pi _{1}(x,y)=x}$ and ${\displaystyle \pi _{2}(x,y)=y}$. Given any set ${\displaystyle Z}$ and functions ${\displaystyle f,g}$ the unique map such that the required diagram commutes is given by ${\displaystyle h=\langle x,y\rangle (z)=(f(z),g(z))}$.[^3]

### Limits and colimits

Categorical products are a particular kind of [limit](https://en.wikipedia.org/wiki/Limit_\(category_theory\) "Limit (category theory)") in category theory. One can generalize the above example to arbitrary limits and colimits.

Let ${\displaystyle {\mathcal {J}}}$ and ${\displaystyle {\mathcal {C}}}$ be categories with ${\displaystyle {\mathcal {J}}}$ a [small](https://en.wikipedia.org/wiki/Small_category "Small category") [index category](https://en.wikipedia.org/wiki/Index_category "Index category") and let ${\displaystyle {\mathcal {C}}^{\mathcal {J}}}$ be the corresponding [functor category](https://en.wikipedia.org/wiki/Functor_category "Functor category"). The *[diagonal functor](https://en.wikipedia.org/wiki/Diagonal_functor "Diagonal functor")*

${\displaystyle \Delta :{\mathcal {C}}\to {\mathcal {C}}^{\mathcal {J}}}$

is the functor that maps each object ${\displaystyle N}$ in ${\displaystyle {\mathcal {C}}}$ to the constant functor ${\displaystyle \Delta (N):{\mathcal {J}}\to {\mathcal {C}}}$ (i.e. ${\displaystyle \Delta (N)(X)=N}$ for each ${\displaystyle X}$ in ${\displaystyle {\mathcal {J}}}$ and ${\displaystyle \Delta (N)(f)=1_{N}}$ for each ${\displaystyle f:X\to Y}$ in ${\displaystyle {\mathcal {J}}}$) and each morphism ${\displaystyle f:N\to M}$ in ${\displaystyle {\mathcal {C}}}$ to the natural transformation ${\displaystyle \Delta (f):\Delta (N)\to \Delta (M)}$ in ${\displaystyle {\mathcal {C}}^{\mathcal {J}}}$ defined as, for every object ${\displaystyle X}$ of ${\displaystyle {\mathcal {J}}}$, the component 
$$
{\displaystyle \Delta (f)(X):\Delta (N)(X)\to \Delta (M)(X)=f:N\to M}
$$
 at ${\displaystyle X}$. In other words, the natural transformation is the one defined by having constant component ${\displaystyle f:N\to M}$ for every object of ${\displaystyle {\mathcal {J}}}$.

Given a functor ${\displaystyle F:{\mathcal {J}}\to {\mathcal {C}}}$ (thought of as an object in ${\displaystyle {\mathcal {C}}^{\mathcal {J}}}$), the *limit* of ${\displaystyle F}$, if it exists, is nothing but a universal morphism from ${\displaystyle \Delta }$ to ${\displaystyle F}$. Dually, the *colimit* of ${\displaystyle F}$ is a universal morphism from ${\displaystyle F}$ to ${\displaystyle \Delta }$.

## Properties

### Existence and uniqueness

Defining a quantity does not guarantee its existence. Given a functor ${\displaystyle F:{\mathcal {C}}\to {\mathcal {D}}}$ and an object ${\displaystyle X}$ of ${\displaystyle {\mathcal {D}}}$, there may or may not exist a universal morphism from ${\displaystyle X}$ to ${\displaystyle F}$. If, however, a universal morphism ${\displaystyle (A,u)}$ does exist, then it is essentially unique. Specifically, it is unique [up to](https://en.wikipedia.org/wiki/Up_to "Up to") a *unique* [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism"): if ${\displaystyle (A',u')}$ is another pair, then there exists a unique isomorphism ${\displaystyle k:A\to A'}$ such that ${\displaystyle u'=F(k)\circ u}$. This is easily seen by substituting ${\displaystyle (A,u')}$ in the definition of a universal morphism.

It is the pair ${\displaystyle (A,u)}$ which is essentially unique in this fashion. The object ${\displaystyle A}$ itself is only unique up to isomorphism. Indeed, if ${\displaystyle (A,u)}$ is a universal morphism and ${\displaystyle k:A\to A'}$ is any isomorphism then the pair ${\displaystyle (A',u')}$, where ${\displaystyle u'=F(k)\circ u}$ is also a universal morphism.

### Equivalent formulations

The definition of a universal morphism can be rephrased in a variety of ways. Let ${\displaystyle F:{\mathcal {C}}\to {\mathcal {D}}}$ be a functor and let ${\displaystyle X}$ be an object of ${\displaystyle {\mathcal {D}}}$. Then the following statements are equivalent:

- ${\displaystyle (A,u)}$ is a universal morphism from ${\displaystyle X}$ to ${\displaystyle F}$
- ${\displaystyle (A,u)}$ is an [initial object](https://en.wikipedia.org/wiki/Initial_object "Initial object") of the [comma category](https://en.wikipedia.org/wiki/Comma_category "Comma category") ${\displaystyle (X\downarrow F)}$
- ${\displaystyle (A,F(\bullet )\circ u)}$ is a [representation](https://en.wikipedia.org/wiki/Representable_functor "Representable functor") of ${\displaystyle {\text{Hom}}_{\mathcal {D}}(X,F(-))}$, where its components ${\displaystyle (F(\bullet )\circ u)_{B}:{\text{Hom}}_{\mathcal {C}}(A,B)\to {\text{Hom}}_{\mathcal {D}}(X,F(B))}$ are defined by

$$
{\displaystyle (F(\bullet )\circ u)_{B}(f:A\to B):X\to F(B)=F(f)\circ u:X\to F(B)}
$$

for each object ${\displaystyle B}$ in ${\displaystyle {\mathcal {C}}.}$

The dual statements are also equivalent:

- ${\displaystyle (A,u)}$ is a universal morphism from ${\displaystyle F}$ to ${\displaystyle X}$
- ${\displaystyle (A,u)}$ is a [terminal object](https://en.wikipedia.org/wiki/Terminal_object "Terminal object") of the comma category ${\displaystyle (F\downarrow X)}$
- ${\displaystyle (A,u\circ F(\bullet ))}$ is a representation of ${\displaystyle {\text{Hom}}_{\mathcal {D}}(F(-),X)}$, where its components ${\displaystyle (u\circ F(\bullet ))_{B}:{\text{Hom}}_{\mathcal {C}}(B,A)\to {\text{Hom}}_{\mathcal {D}}(F(B),X)}$ are defined by

$$
{\displaystyle (u\circ F(\bullet ))_{B}(f:B\to A):F(B)\to X=u\circ F(f):F(B)\to X}
$$

for each object ${\displaystyle B}$ in ${\displaystyle {\mathcal {C}}.}$

### Relation to adjoint functors

Suppose ${\displaystyle (A_{1},u_{1})}$ is a universal morphism from ${\displaystyle X_{1}}$ to ${\displaystyle F}$ and ${\displaystyle (A_{2},u_{2})}$ is a universal morphism from ${\displaystyle X_{2}}$ to ${\displaystyle F}$. By the universal property of universal morphisms, given any morphism ${\displaystyle h:X_{1}\to X_{2}}$ there exists a unique morphism ${\displaystyle g:A_{1}\to A_{2}}$ such that the following diagram commutes:

![Universal morphisms can behave like a natural transformation between functors under suitable conditions.](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Connection_between_universal_elements_inducing_a_functor.svg/500px-Connection_between_universal_elements_inducing_a_functor.svg.png)

Universal morphisms can behave like a natural transformation between functors under suitable conditions.

If *every* object ${\displaystyle X_{i}}$ of ${\displaystyle {\mathcal {D}}}$ admits a universal morphism to ${\displaystyle F}$, then the assignment ${\displaystyle X_{i}\mapsto A_{i}}$ and ${\displaystyle h\mapsto g}$ defines a functor ${\displaystyle G:{\mathcal {D}}\to {\mathcal {C}}}$. The maps ${\displaystyle u_{i}}$ then define a [natural transformation](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation") from ${\displaystyle 1_{\mathcal {D}}}$ (the identity functor on ${\displaystyle {\mathcal {D}}}$) to ${\displaystyle F\circ G}$. The functors ${\displaystyle (F,G)}$ are then a pair of [adjoint functors](https://en.wikipedia.org/wiki/Adjoint_functor "Adjoint functor"), with ${\displaystyle G}$ left-adjoint to ${\displaystyle F}$ and ${\displaystyle F}$ right-adjoint to ${\displaystyle G}$.

Similar statements apply to the dual situation of terminal morphisms from ${\displaystyle F}$. If such morphisms exist for every ${\displaystyle X}$ in ${\displaystyle {\mathcal {C}}}$ one obtains a functor ${\displaystyle G:{\mathcal {C}}\to {\mathcal {D}}}$ which is right-adjoint to ${\displaystyle F}$ (so ${\displaystyle F}$ is left-adjoint to ${\displaystyle G}$).

Indeed, all pairs of adjoint functors arise from universal constructions in this manner. Let ${\displaystyle F}$ and ${\displaystyle G}$ be a pair of adjoint functors with unit ${\displaystyle \eta }$ and co-unit ${\displaystyle \epsilon }$ (see the article on [adjoint functors](https://en.wikipedia.org/wiki/Adjoint_functors "Adjoint functors") for the definitions). Then we have a universal morphism for each object in ${\displaystyle {\mathcal {C}}}$ and ${\displaystyle {\mathcal {D}}}$:

- For each object ${\displaystyle X}$ in ${\displaystyle {\mathcal {C}}}$, ${\displaystyle (F(X),\eta _{X})}$ is a universal morphism from ${\displaystyle X}$ to ${\displaystyle G}$. That is, for all ${\displaystyle f:X\to G(Y)}$ there exists a unique ${\displaystyle g:F(X)\to Y}$ for which the following diagrams commute.
- For each object ${\displaystyle Y}$ in ${\displaystyle {\mathcal {D}}}$, ${\displaystyle (G(Y),\epsilon _{Y})}$ is a universal morphism from ${\displaystyle F}$ to ${\displaystyle Y}$. That is, for all ${\displaystyle g:F(X)\to Y}$ there exists a unique ${\displaystyle f:X\to G(Y)}$ for which the following diagrams commute.
![The unit and counit of an adjunction, which are natural transformations between functors, are an important example of universal morphisms.](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Universal_morphisms_appear_as_the_unit_and_counit_of_adjunctions.svg/960px-Universal_morphisms_appear_as_the_unit_and_counit_of_adjunctions.svg.png)

The unit and counit of an adjunction, which are natural transformations between functors, are an important example of universal morphisms.

Universal constructions are more general than adjoint functor pairs: a universal construction is like an optimization problem; it gives rise to an adjoint pair if and only if this problem has a solution for every object of ${\displaystyle {\mathcal {C}}}$ (equivalently, every object of ${\displaystyle {\mathcal {D}}}$).

## History

[^1]: Jacobson (2009), Proposition 1.6, p. 44.

[^2]: See for example, Polcino & Sehgal (2002), p. 133. exercise 1, about the universal property of [group rings](https://en.wikipedia.org/wiki/Group_ring "Group ring").

[^3]: Fong, Brendan; Spivak, David I. (2018-10-12). "Seven Sketches in Compositionality: An Invitation to Applied Category Theory". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[1803.05316](https://arxiv.org/abs/1803.05316) \[[math.CT](https://arxiv.org/archive/math.CT)\].