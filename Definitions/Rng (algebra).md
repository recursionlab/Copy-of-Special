---
title: "Rng (algebra)"
source: "https://en.wikipedia.org/wiki/Rng_(algebra)#Rng_of_square_zero"
author:
  - "[[Wikipedia]]"
published:
created: 2026-04-29
description:
tags:
  - "clippings"
---
In [abstract algebra](https://en.wikipedia.org/wiki/Abstract_algebra "Abstract algebra"), a **rng** ([IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet "International Phonetic Alphabet"): [/ r ʌ ŋ /](https://en.wikipedia.org/wiki/Help:IPA/English "Help:IPA/English"), like *rung*) or **non-unital ring** or **[pseudo-ring](https://en.wikipedia.org/wiki/Pseudo-ring "Pseudo-ring")** is an [algebraic structure](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure") satisfying the same properties as a [ring](https://en.wikipedia.org/wiki/Ring_\(mathematics\) "Ring (mathematics)"), but without assuming the existence of a [multiplicative identity](https://en.wikipedia.org/wiki/Multiplicative_identity "Multiplicative identity"). The term *rng* is meant to suggest that it is a ring without *i*, that is, without the requirement for an identity element.[^1]

There is no consensus in the community as to whether the existence of a multiplicative identity must be one of the [ring axioms](https://en.wikipedia.org/wiki/Ring_axioms "Ring axioms") (see *[Ring (mathematics) § History](https://en.wikipedia.org/wiki/Ring_\(mathematics\)#History "Ring (mathematics)")*). The term *rng* was coined to alleviate this ambiguity when people want to refer explicitly to a ring without the axiom of multiplicative identity.

A number of algebras of functions considered in [analysis](https://en.wikipedia.org/wiki/Mathematical_analysis "Mathematical analysis") are not unital, for instance the algebra of functions decreasing to zero at infinity, especially those with [compact support](https://en.wikipedia.org/wiki/Compact_support "Compact support") on some (non- [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space")) space.

Rngs appear in the following chain of [class inclusions](https://en.wikipedia.org/wiki/Subclass_\(set_theory\) "Subclass (set theory)"):

**rngs** ⊃ **[rings](https://en.wikipedia.org/wiki/Ring_\(mathematics\) "Ring (mathematics)")** ⊃ **[commutative rings](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring")** ⊃ **[integral domains](https://en.wikipedia.org/wiki/Integral_domain "Integral domain")** ⊃ **[integrally closed domains](https://en.wikipedia.org/wiki/Integrally_closed_domain "Integrally closed domain")** ⊃ **[GCD domains](https://en.wikipedia.org/wiki/GCD_domain "GCD domain")** ⊃ **[unique factorization domains](https://en.wikipedia.org/wiki/Unique_factorization_domain "Unique factorization domain")** ⊃ **[principal ideal domains](https://en.wikipedia.org/wiki/Principal_ideal_domain "Principal ideal domain")** ⊃ **[Euclidean domains](https://en.wikipedia.org/wiki/Euclidean_domain "Euclidean domain")** ⊃ **[fields](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)")** ⊃ **[algebraically closed fields](https://en.wikipedia.org/wiki/Algebraically_closed_field "Algebraically closed field")**

## Definition

Formally, a **rng** is a [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") *R* with two [binary operations](https://en.wikipedia.org/wiki/Binary_operations "Binary operations") (+, ·) called *addition* and *multiplication* such that

- (*R*, +) is an [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group"),
- (*R*, ·) is a [semigroup](https://en.wikipedia.org/wiki/Semigroup "Semigroup"),
- Multiplication [distributes](https://en.wikipedia.org/wiki/Distributive_law "Distributive law") over addition.

A **rng homomorphism** is a function *f*: *R* → *S* from one rng to another such that

- *f* (*x* + *y*) = *f* (*x*) + *f* (*y*)
- *f* (*x* · *y*) = *f* (*x*) · *f* (*y*)

for all *x* and *y* in *R*.

If *R* and *S* are rings, then a [ring homomorphism](https://en.wikipedia.org/wiki/Ring_homomorphism "Ring homomorphism") *R* → *S* is the same as a rng homomorphism *R* → *S* that maps 1 to 1.

## Examples

All rings are rngs. A simple example of a rng that is not a ring is given by the [even integers](https://en.wikipedia.org/wiki/Even_number "Even number") with the ordinary addition and multiplication of integers. Another example is given by the set of all 3-by-3 real [matrices](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)") whose bottom row is zero. Both of these examples are instances of the general fact that every (one- or two-sided) [ideal](https://en.wikipedia.org/wiki/Ideal_\(ring_theory\) "Ideal (ring theory)") is a rng.

Any [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") can be made a rng by defining the multiplication so that *xy* = 0 for all *x* and *y*. (See *[§ Rng of square zero](#Rng_of_square_zero)*)

Rngs often appear naturally in [functional analysis](https://en.wikipedia.org/wiki/Functional_analysis "Functional analysis") when [linear operators](https://en.wikipedia.org/wiki/Linear_operator "Linear operator") on infinite- [dimensional](https://en.wikipedia.org/wiki/Dimension_\(linear_algebra\) "Dimension (linear algebra)") [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space") are considered. Take for instance any infinite-dimensional vector space *V* and consider the set of all linear operators *f*: *V* → *V* with finite [rank](https://en.wikipedia.org/wiki/Rank_\(linear_algebra\) "Rank (linear algebra)") (i.e. dim *f* (*V*) < ∞). Together with addition and [composition](https://en.wikipedia.org/wiki/Functional_composition "Functional composition") of operators, this is a rng, but not a ring. Another example is the rng of all real [sequences](https://en.wikipedia.org/wiki/Sequence "Sequence") that [converge to](https://en.wikipedia.org/wiki/Limit_of_a_sequence "Limit of a sequence") 0, with component-wise operations.

Also, many test function spaces occurring in the [theory of distributions](https://en.wikipedia.org/wiki/Theory_of_distributions "Theory of distributions") consist of functions decreasing to zero at infinity, like e.g. [Schwartz space](https://en.wikipedia.org/wiki/Schwartz_space "Schwartz space"). Thus, the function everywhere equal to one, which would be the only possible identity element for pointwise multiplication, cannot exist in such spaces, which therefore are rngs (for pointwise addition and multiplication). In particular, the real-valued [continuous functions](https://en.wikipedia.org/wiki/Continuous_function "Continuous function") with [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space") [support](https://en.wikipedia.org/wiki/Support_\(mathematics\) "Support (mathematics)") defined on some [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space"), together with pointwise addition and multiplication, form a rng; this is not a ring unless the underlying space is [compact](https://en.wikipedia.org/wiki/Compact_space "Compact space").

### Example: even integers

The set 2 **Z** of even integers is closed under addition and multiplication and has an additive identity, 0, so it is a rng, but it does not have a multiplicative identity, so it is not a ring.

In 2 **Z**, the only multiplicative [idempotent](https://en.wikipedia.org/wiki/Idempotence "Idempotence") is 0, the only [nilpotent](https://en.wikipedia.org/wiki/Nilpotent "Nilpotent") is 0, and the only element with a [reflexive inverse](https://en.wikipedia.org/wiki/Generalized_inverse "Generalized inverse") is 0.

### Example: finite quinary sequences

The direct sum ${\textstyle {\mathcal {T}}=\bigoplus _{i=1}^{\infty }\mathbf {Z} /5\mathbf {Z} }$ equipped with coordinate-wise addition and multiplication is a rng with the following properties:

- Its [idempotent](https://en.wikipedia.org/wiki/Idempotence "Idempotence") elements form a lattice with no upper bound.
- Every element *x* has a [reflexive inverse](https://en.wikipedia.org/wiki/Generalized_inverse "Generalized inverse"), namely an element *y* such that *xyx* = *x* and *yxy* = *y*.
- For every finite subset of ${\displaystyle {\mathcal {T}}}$, there exists an idempotent in ${\displaystyle {\mathcal {T}}}$ that acts as an identity for the entire subset: the sequence with a one at every position where a sequence in the subset has a non-zero element at that position, and zero in every other position.

## Properties

- Ideals, [quotient rings](https://en.wikipedia.org/wiki/Quotient_ring "Quotient ring"), and [modules](https://en.wikipedia.org/wiki/Module_\(algebra\) "Module (algebra)") can be defined for rngs in the same manner as for rings.
- Working with rngs instead of rings complicates some related definitions, however. For example, in a ring *R*, the left ideal (*f*) generated by an element *f*, defined as the smallest left ideal containing *f*, is simply *Rf*, but if *R* is only a rng, then *Rf* might not contain *f*, so instead
	$$
	{\displaystyle (f)=Rf+\mathbf {Z} f=\{af+nf:a\in R~{\text{and}}~n\in \mathbf {Z} \},}
	$$
	 where *nf* must be interpreted using repeated addition/subtraction since *n* need not represent an element of *R*. Similarly, the left ideal generated by elements *f* <sub>1</sub>,..., *f* <sub><i>m</i></sub> of a rng *R* is 
	$$
	{\displaystyle (f_{1},\ldots ,f_{m})=\{a_{1}f_{1}+\cdots +a_{m}f_{m}+n_{1}f_{1}+\cdots n_{m}f_{m}:a_{i}\in R\;\mathrm {and} \;n_{i}\in \mathbf {Z} \},}
	$$
	a formula that goes back to [Emmy Noether](https://en.wikipedia.org/wiki/Emmy_Noether "Emmy Noether").[^2] Similar complications arise in the definition of [submodule](https://en.wikipedia.org/wiki/Submodule "Submodule") generated by a set of elements of a module.
- Some theorems for rings are false for rngs. For example, in a ring, every proper ideal is contained in a [maximal ideal](https://en.wikipedia.org/wiki/Maximal_ideal "Maximal ideal"), so a nonzero ring always has at least one maximal ideal. Both these statements fail for rngs.
- A rng homomorphism *f*: *R* → *S* maps any [idempotent element](https://en.wikipedia.org/wiki/Idempotent_element_\(ring_theory\) "Idempotent element (ring theory)") to an idempotent element.
- If *f*: *R* → *S* is a rng homomorphism from a ring to a rng, and the image of *f* contains a non-zero-divisor of *S*, then *S* is a ring, and *f* is a ring homomorphism.

## Adjoining an identity element (Dorroh extension)

Every rng *R* can be enlarged to a ring *R* ^ by adjoining an identity element. A general way in which to do this is to formally add an identity element 1 and let *R* ^ consist of integral linear combinations of 1 and elements of *R* with the premise that none of its nonzero integral multiples coincide or are contained in *R*. That is, elements of *R* ^ are of the form

*n* ⋅ 1 + *r*

where *n* is an [integer](https://en.wikipedia.org/wiki/Integer "Integer") and *r* ∈ *R*. Multiplication is defined by linearity:

(*n* <sub>1</sub> + *r* <sub>1</sub>) ⋅ (*n* <sub>2</sub> + *r* <sub>2</sub>) = *n* <sub>1</sub> *n* <sub>2</sub> + *n* <sub>1</sub> *r* <sub>2</sub> + *n* <sub>2</sub> *r* <sub>1</sub> + *r* <sub>1</sub> *r* <sub>2</sub>.

More formally, we can take *R* ^ to be the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") **Z** × *R* and define addition and multiplication by

(*n* <sub>1</sub>, *r* <sub>1</sub>) + (*n* <sub>2</sub>, *r* <sub>2</sub>) = (*n* <sub>1</sub> + *n* <sub>2</sub>, *r* <sub>1</sub> + *r* <sub>2</sub>),

(*n* <sub>1</sub>, *r* <sub>1</sub>) · (*n* <sub>2</sub>, *r* <sub>2</sub>) = (*n* <sub>1</sub> *n* <sub>2</sub>, *n* <sub>1</sub> *r* <sub>2</sub> + *n* <sub>2</sub> *r* <sub>1</sub> + *r* <sub>1</sub> *r* <sub>2</sub>).

The multiplicative identity of *R* ^ is then (1, 0). There is a natural rng homomorphism *j*: *R* → *R* ^ defined by *j* (*r*) = (0, *r*). This map has the following [universal property](https://en.wikipedia.org/wiki/Universal_property "Universal property"):

Given any ring *S* and any rng homomorphism *f*: *R* → *S*, there exists a unique ring homomorphism *g*: *R* ^ → *S* such that *f* = *gj*.

The map *g* can be defined by *g* (*n*, *r*) = *n* · 1 <sub><i>S</i></sub> + *f* (*r*).

There is a natural [surjective](https://en.wikipedia.org/wiki/Surjective "Surjective") ring homomorphism *R* ^ → **Z** which sends (*n*, *r*) to *n*. The [kernel](https://en.wikipedia.org/wiki/Kernel_\(ring_theory\) "Kernel (ring theory)") of this homomorphism is the image of *R* in *R* ^. Since *j* is [injective](https://en.wikipedia.org/wiki/Injective "Injective"), we see that *R* is embedded as a (two-sided) [ideal](https://en.wikipedia.org/wiki/Ideal_\(ring_theory\) "Ideal (ring theory)") in *R* ^ with the [quotient ring](https://en.wikipedia.org/wiki/Quotient_ring "Quotient ring") *R* ^/ *R* isomorphic to **Z**. It follows that

*Every rng is an ideal in some ring, and every ideal of a ring is a rng.*

Note that *j* is never surjective. So, even when *R* already has an identity element, the ring *R* ^ will be a larger one with a different identity. The ring *R* ^ is often called the **Dorroh extension** of *R* after the American mathematician Joe Lee Dorroh, who first constructed it.[^3]

The process of adjoining an identity element to a rng can be formulated in the language of [category theory](https://en.wikipedia.org/wiki/Category_theory "Category theory"). If we denote the [category of all rings](https://en.wikipedia.org/wiki/Category_of_all_rings "Category of all rings") and ring homomorphisms by **Ring** and the category of all rngs and rng homomorphisms by **Rng**, then **Ring** is a (nonfull) [subcategory](https://en.wikipedia.org/wiki/Subcategory "Subcategory") of **Rng**. The construction of *R* ^ given above yields a [left adjoint](https://en.wikipedia.org/wiki/Left_adjoint "Left adjoint") to the [inclusion functor](https://en.wikipedia.org/wiki/Inclusion_functor "Inclusion functor") *I*: **Ring** → **Rng**. Notice that **Ring** is not a [reflective subcategory](https://en.wikipedia.org/wiki/Reflective_subcategory "Reflective subcategory") of **Rng** because the inclusion functor is not full.

## Properties weaker than having an identity

There are several properties that have been considered in the literature that are weaker than having an identity element, but not so general. For example:

- Rings with enough idempotents: A rng *R* is said to be a ring with enough idempotents when there exists a subset *E* of *R* given by orthogonal (i.e. *ef* = 0 for all *e* ≠ *f* in *E*) idempotents (i.e. *e* <sup>2</sup> = *e* for all *e* in *E*) such that *R* = ⊕ <sub><i>e</i> ∈ <i>E</i></sub> *eR* = ⊕ <sub><i>e</i> ∈ <i>E</i></sub> *Re*.
- Rings with local units: A rng *R* is said to be a ring with local units in case for every finite set *r* <sub>1</sub>, *r* <sub>2</sub>,..., *r <sub>t</sub>* in *R* we can find *e* in *R* such that *e* <sup>2</sup> = *e* and *er <sub>i</sub>* = *r <sub>i</sub>* = *r <sub>i</sub> e* for every *i*.
- *s* -unital rings: A rng *R* is said to be *s* -unital in case for every finite set *r* <sub>1</sub>, *r* <sub>2</sub>,..., *r <sub>t</sub>* in *R* we can find *s* in *R* such that *sr <sub>i</sub>* = *r <sub>i</sub>* = *r <sub>i</sub> s* for every *i*.
- Firm rings: A rng *R* is said to be firm if the canonical homomorphism *R* ⊗ <sub><i>R</i></sub> *R* → *R* given by *r* ⊗ *s* ↦ *rs* is an isomorphism.
- Idempotent rings: A rng *R* is said to be idempotent (or an irng) in case *R* <sup>2</sup> = *R*, that is, for every element *r* of *R* we can find elements *r <sub>i</sub>* and *s <sub>i</sub>* in *R* such that ${\textstyle r=\sum _{i}r_{i}s_{i}}$.

It is not difficult to check that each of these properties is weaker than having an identity element and weaker than the property preceding it.

- Rings are rings with enough idempotents, using *E* = {1}. A ring with enough idempotents that has no identity is for example the ring of infinite matrices over a field with just a finite number of nonzero entries. Those matrices with a 1 in precisely one entry of the main diagonal and 0s in all other entries are the orthogonal idempotents.
- Rings with enough idempotents are rings with local units as can be seen by taking finite sums of the orthogonal idempotents to satisfy the definition.
- Rings with local units are in particular *s* -unital; *s* -unital rings are firm and firm rings are idempotent.

## Rng of square zero

A **rng of square zero** is a rng *R* such that *xy* = 0 for all *x* and *y* in *R*.[^4] Any [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") can be made a rng of square zero by defining the multiplication so that *xy* = 0 for all *x* and *y*;[^5] thus every abelian group is the additive group of some rng. The only rng of square zero with a multiplicative identity is the [zero ring](https://en.wikipedia.org/wiki/Zero_ring "Zero ring") {0}.[^5]

Any additive [subgroup](https://en.wikipedia.org/wiki/Subgroup "Subgroup") of a rng of square zero is an [ideal](https://en.wikipedia.org/wiki/Ideal_\(ring_theory\) "Ideal (ring theory)"). Thus a rng of square zero is [simple](https://en.wikipedia.org/wiki/Simple_ring "Simple ring") if and only if its additive group is a simple abelian group, i.e., a [cyclic group](https://en.wikipedia.org/wiki/Cyclic_group "Cyclic group") of prime order.[^6]

## Unital homomorphism

Given two unital algebras *A* and *B*, an algebra [homomorphism](https://en.wikipedia.org/wiki/Homomorphism "Homomorphism")

*f*: *A* → *B*

is **unital** if it maps the identity element of *A* to the identity element of *B*.

If the associative algebra *A* over the [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") *K* is *not* unital, one can adjoin an identity element as follows: take *A* × *K* as underlying *K* - [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") and define multiplication ∗ by

(*x*, *r*) ∗ (*y*, *s*) = (*xy* + *sx* + *ry*, *rs*)

for *x*, *y* in *A* and *r*, *s* in *K*. Then ∗ is an associative operation with identity element (0, 1). The old algebra *A* is contained in the new one, and in fact *A* × *K* is the "most general" unital algebra containing *A*, in the sense of [universal constructions](https://en.wikipedia.org/wiki/Universal_construction "Universal construction").

[^1]: [Jacobson (1989)](#CITEREFJacobson1989), pp. 155–156

[^2]: [Noether (1921)](#CITEREFNoether1921), p. 30, §1.2

[^3]: [Dorroh (1932)](#CITEREFDorroh1932)

[^4]: See [Bourbaki (1998)](#CITEREFBourbaki1998), p. 102, where it is called a pseudo-ring of square zero. Some other authors use the term "zero ring" to refer to any rng of square zero; see e.g. [Szele (1949)](#CITEREFSzele1949) and [Kreinovich (1995)](#CITEREFKreinovich1995).

[^5]: [Bourbaki (1998)](#CITEREFBourbaki1998), p. 102

[^6]: [Zariski & Samuel (1958)](#CITEREFZariskiSamuel1958), p. 133