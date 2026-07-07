---
title: "Field (mathematics)"
source: "https://en.wikipedia.org/wiki/Field_(mathematics)"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2001-10-14
created: 2026-04-10
description:
tags:
  - "clippings"
---
![Diagram of symbols of arithmetic operations](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Arithmetic_operations.svg/250px-Arithmetic_operations.svg.png)

A field is an algebraic structure that is closed under the four usual arithmetic operations.

In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), a **field** is a [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") on which [addition](https://en.wikipedia.org/wiki/Addition "Addition"), [subtraction](https://en.wikipedia.org/wiki/Subtraction "Subtraction"), [multiplication](https://en.wikipedia.org/wiki/Multiplication "Multiplication"), and [division](https://en.wikipedia.org/wiki/Division_\(mathematics\) "Division (mathematics)") are defined and behave as the corresponding operations on [rational numbers](https://en.wikipedia.org/wiki/Rational_number "Rational number") do. A field is thus a fundamental [algebraic structure](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure") that is widely used in [algebra](https://en.wikipedia.org/wiki/Algebra "Algebra"), [number theory](https://en.wikipedia.org/wiki/Number_theory "Number theory"), and many other areas of mathematics.

The best known fields are the field of rational numbers, the field of [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number"), and the field of [complex numbers](https://en.wikipedia.org/wiki/Complex_number "Complex number"). Many other fields, such as [fields of rational functions](https://en.wikipedia.org/wiki/Field_of_rational_functions "Field of rational functions"), [algebraic function fields](https://en.wikipedia.org/wiki/Algebraic_function_field "Algebraic function field"), [algebraic number fields](https://en.wikipedia.org/wiki/Algebraic_number_field "Algebraic number field"), [finite fields](https://en.wikipedia.org/wiki/Finite_field "Finite field"), and [*p* -adic fields](https://en.wikipedia.org/wiki/P-adic_number "P-adic number") are commonly used and studied in mathematics, particularly in number theory and [algebraic geometry](https://en.wikipedia.org/wiki/Algebraic_geometry "Algebraic geometry").

The theory of fields proves that [angle trisection](https://en.wikipedia.org/wiki/Angle_trisection "Angle trisection") and [squaring the circle](https://en.wikipedia.org/wiki/Squaring_the_circle "Squaring the circle") cannot be done with a [compass and straightedge](https://en.wikipedia.org/wiki/Compass_and_straightedge "Compass and straightedge") alone. [Galois theory](https://en.wikipedia.org/wiki/Galois_theory "Galois theory"), devoted to understanding the symmetries of [field extensions](https://en.wikipedia.org/wiki/Field_extension "Field extension"), provides an elegant proof of the [Abel–Ruffini theorem](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem "Abel–Ruffini theorem") that general [quintic equations](https://en.wikipedia.org/wiki/Quintic_equation "Quintic equation") cannot be [solved in radicals](https://en.wikipedia.org/wiki/Solution_in_radicals "Solution in radicals").

Fields serve as foundational notions in several mathematical domains. This includes different branches of [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis "Mathematical analysis"), which are based on fields with additional structure. Basic theorems in analysis hinge on the structural properties of the field of real numbers. Most importantly for algebraic purposes, any field may be used as the [scalars](https://en.wikipedia.org/wiki/Scalar_\(mathematics\) "Scalar (mathematics)") for a [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space"), which is the standard general context for [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra "Linear algebra"). [Number fields](https://en.wikipedia.org/wiki/Number_field "Number field"), the siblings of the field of rational numbers, are studied in depth in [number theory](https://en.wikipedia.org/wiki/Number_theory "Number theory"). [Function fields](https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety "Function field of an algebraic variety") can help describe properties of geometric objects. Finite fields are used for [error correction codes](https://en.wikipedia.org/wiki/Error_correction_code "Error correction code") and [cryptography](https://en.wikipedia.org/wiki/Cryptography "Cryptography").

## Definition

Informally, a field is a set with an addition [operation](https://en.wikipedia.org/wiki/Binary_operation "Binary operation") *a* + *b* and a multiplication operation *a* ⋅ *b* that behave as they do for [rational numbers](https://en.wikipedia.org/wiki/Rational_number "Rational number") and [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number"). The requirements include the existence of an [additive inverse](https://en.wikipedia.org/wiki/Additive_inverse "Additive inverse") − *a* for each element a and of a [multiplicative inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse") *b* <sup>−1</sup> for each nonzero element b. This allows the definition of the so-called *inverse operations*, subtraction *a* − *b* and division *a* / *b*, as *a* − *b* = *a* + (− *b*) and *a* / *b* = *a* ⋅ *b* <sup>−1</sup>. Often the product *a* ⋅ *b* is represented by juxtaposition, as ab.

### Classic definition

Formally, a field is a [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") F together with two [binary operations](https://en.wikipedia.org/wiki/Binary_operation "Binary operation") on F, called *addition* and *multiplication*, satisfying the axioms given below.[^8] A binary operation on F is a mapping *F* × *F* → *F*; it sends each ordered pair of elements of F to a uniquely determined element of F.[^9] [^10] The result of the addition of a and b is called the *sum* of a and b, and is denoted *a* + *b*. The result of the multiplication of a and b is called the *product* of a and b, and is denoted *a* ⋅ *b*. These operations are required to satisfy the following properties, called *[field axioms](https://en.wikipedia.org/wiki/Axiom#Non-logical_axioms "Axiom")*.

These axioms are required to hold for all [elements](https://en.wikipedia.org/wiki/Element_\(mathematics\) "Element (mathematics)") a, b, c of the field F:

- [Associativity](https://en.wikipedia.org/wiki/Associativity "Associativity") of addition and multiplication: *a* + (*b* + *c*) = (*a* + *b*) + *c*, and *a* ⋅ (*b* ⋅ *c*) = (*a* ⋅ *b*) ⋅ *c*.
- [Commutativity](https://en.wikipedia.org/wiki/Commutativity "Commutativity") of addition and multiplication: *a* + *b* = *b* + *a*, and *a* ⋅ *b* = *b* ⋅ *a*.
- [Additive](https://en.wikipedia.org/wiki/Additive_identity "Additive identity") and [multiplicative identity](https://en.wikipedia.org/wiki/Multiplicative_identity "Multiplicative identity"): there exist distinct elements 0 and 1 in F such that *a* + 0 = *a* and *a* ⋅ 1 = *a*.
- [Additive inverses](https://en.wikipedia.org/wiki/Additive_inverse "Additive inverse"): for every a in F, there exists an element in F, denoted − *a*, called the *additive inverse* of a, such that *a* + (− *a*) = 0.
- [Multiplicative inverses](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse"): for every *a* ≠ 0 in F, there exists an element in F, denoted by *a* <sup>−1</sup> or 1/ *a*, called the *multiplicative inverse* of a, such that *a* ⋅ *a* <sup>−1</sup> = 1.
- [Distributivity](https://en.wikipedia.org/wiki/Distributivity "Distributivity") of multiplication over addition: *a* ⋅ (*b* + *c*) = (*a* ⋅ *b*) + (*a* ⋅ *c*).

An equivalent but more succinct definition is: a field is a set with two commutative operations, called addition and multiplication, such that

- it is a [group](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)") under addition, with additive identity called 0;
- the nonzero elements form a group under multiplication; and
- multiplication distributes over addition.

Even more succinctly: a field is a [commutative ring](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring") in which 0 ≠ 1 and all nonzero elements are [invertible](https://en.wikipedia.org/wiki/Unit_\(ring_theory\) "Unit (ring theory)") under multiplication.

### Alternative definitions

Fields can also be defined in different, but equivalent, ways. One can alternatively define a field by four binary operations (addition, subtraction, multiplication, and division) and their required properties. [Division by zero](https://en.wikipedia.org/wiki/Division_by_zero "Division by zero") is, by definition, excluded.[^11] In order to avoid [existential quantifiers](https://en.wikipedia.org/wiki/Existential_quantifier "Existential quantifier"), fields can be defined by two binary operations (addition and multiplication), two unary operations (yielding the additive and multiplicative inverses respectively), and two [nullary](https://en.wikipedia.org/wiki/Arity#Nullary "Arity") operations (the constants 0 and 1). These operations are then subject to the conditions above. Avoiding existential quantifiers is important in [constructive mathematics](https://en.wikipedia.org/wiki/Constructive_mathematics "Constructive mathematics") and [computing](https://en.wikipedia.org/wiki/Computing "Computing").[^12] One may equivalently define a field by the same two binary operations, one unary operation (the multiplicative inverse), and two (not necessarily distinct) constants 1 and −1, since 0 = 1 + (−1) and − *a* = (−1) *a*.[^1]

## Examples

### Rational numbers

Rational numbers have been widely used a long time before the elaboration of the concept of field. They are numbers that can be written as [fractions](https://en.wikipedia.org/wiki/Fraction_\(mathematics\) "Fraction (mathematics)") *a* / *b*, where a and b are [integers](https://en.wikipedia.org/wiki/Integer "Integer"), and *b* ≠ 0. The additive inverse of such a fraction is − *a* / *b*, and the multiplicative inverse (provided that *a* ≠ 0) is *b* / *a*, which can be seen as follows:

${\displaystyle {\frac {b}{a}}\cdot {\frac {a}{b}}={\frac {ba}{ab}}=1.}$

The abstractly required field axioms reduce to standard properties of rational numbers. For example, the law of distributivity can be proven as follows:[^13]

${\displaystyle {\begin{aligned}&{\frac {a}{b}}\cdot \left({\frac {c}{d}}+{\frac {e}{f}}\right)\\[6pt]={}&{\frac {a}{b}}\cdot \left({\frac {c}{d}}\cdot {\frac {f}{f}}+{\frac {e}{f}}\cdot {\frac {d}{d}}\right)\\[6pt]={}&{\frac {a}{b}}\cdot \left({\frac {cf}{df}}+{\frac {ed}{fd}}\right)={\frac {a}{b}}\cdot {\frac {cf+ed}{df}}\\[6pt]={}&{\frac {a(cf+ed)}{bdf}}={\frac {acf}{bdf}}+{\frac {aed}{bdf}}={\frac {ac}{bd}}+{\frac {ae}{bf}}\\[6pt]={}&{\frac {a}{b}}\cdot {\frac {c}{d}}+{\frac {a}{b}}\cdot {\frac {e}{f}}.\end{aligned}}}$

### Real and complex numbers

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Complex_multi.svg/330px-Complex_multi.svg.png)

The multiplication of complex numbers can be visualized geometrically by rotations and scalings.

The [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") **R**, with the usual operations of addition and multiplication, also form a field. The [complex numbers](https://en.wikipedia.org/wiki/Complex_number "Complex number") **C** consist of expressions

*a* + *bi*, with *a*, *b* real,

where i is the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit "Imaginary unit"), i.e., a (non-real) number satisfying *i* <sup>2</sup> = −1. Addition and multiplication of real numbers are defined in such a way that expressions of this type satisfy all field axioms and thus hold for **C**. For example, the distributive law enforces

(*a* + *bi*)(*c* + *di*) = *ac* + *bci* + *adi* + *bdi* <sup>2</sup> = (*ac* − *bd*) + (*bc* + *ad*) *i*.

It is immediate that this is again an expression of the above type, and so the complex numbers form a field. Complex numbers can be geometrically represented as points in the [plane](https://en.wikipedia.org/wiki/Plane_\(geometry\) "Plane (geometry)"), with [Cartesian coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinates "Cartesian coordinates") given by the real numbers of their describing expression, or as the arrows from the origin to these points, specified by their length and an angle enclosed with some distinct direction. Addition then corresponds to combining the arrows to the intuitive parallelogram (adding the Cartesian coordinates), and the multiplication is – less intuitively – combining rotating and scaling of the arrows (adding the angles and multiplying the lengths). The fields of real and complex numbers are used throughout mathematics, physics, engineering, statistics, and many other scientific disciplines.

### Constructible numbers

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Root_construction_geometric_mean5.svg/330px-Root_construction_geometric_mean5.svg.png)

The geometric mean theorem asserts that h 2 = pq. Choosing q = 1 allows construction of the square root of a given constructible number p.

In antiquity, several geometric problems concerned the (in)feasibility of constructing certain numbers with [compass and straightedge](https://en.wikipedia.org/wiki/Compass_and_straightedge "Compass and straightedge"). For example, it was unknown to the Greeks that it is, in general, impossible to trisect a given angle in this way. These problems can be settled using the field of [constructible numbers](https://en.wikipedia.org/wiki/Constructible_numbers "Constructible numbers").[^14] Real constructible numbers are, by definition, lengths of line segments that can be constructed from the points 0 and 1 in finitely many steps using only [compass](https://en.wikipedia.org/wiki/Compass_\(drawing_tool\) "Compass (drawing tool)") and [straightedge](https://en.wikipedia.org/wiki/Straightedge "Straightedge"). These numbers, endowed with the field operations of real numbers, restricted to the constructible numbers, form a field, which properly includes the field **Q** of rational numbers. The illustration shows the construction of [square roots](https://en.wikipedia.org/wiki/Square_root "Square root") of constructible numbers, not necessarily contained within **Q**. Using the labeling in the illustration, construct the segments *AD*, *DB*, and a [semicircle](https://en.wikipedia.org/wiki/Semicircle "Semicircle") over *AB* (center at the [midpoint](https://en.wikipedia.org/wiki/Midpoint "Midpoint") O), which intersects the [perpendicular](https://en.wikipedia.org/wiki/Perpendicular "Perpendicular") line through D in a point C, at a distance of exactly ${\displaystyle h={\sqrt {p}}}$ from B when *BD* has length one.

Not all real numbers are constructible. It can be shown that ${\displaystyle {\sqrt[{3}]{2}}}$ is not a constructible number, which implies that it is impossible to construct with compass and straightedge the length of the side of a [cube with volume 2](https://en.wikipedia.org/wiki/Doubling_the_cube "Doubling the cube"), another problem posed by the ancient Greeks.

### A field with four elements

| Addition | Multiplication |
| --- | --- |
| \| + \| O \| I \| A \| B \| \| --- \| --- \| --- \| --- \| --- \| \| O \| O \| I \| A \| B \| \| I \| I \| O \| B \| A \| \| A \| A \| B \| O \| I \| \| B \| B \| A \| I \| O \| | \| ⋅ \| O \| I \| A \| B \| \| --- \| --- \| --- \| --- \| --- \| \| O \| O \| O \| O \| O \| \| I \| O \| I \| A \| B \| \| A \| O \| A \| B \| I \| \| B \| O \| B \| I \| A \| |

In addition to familiar number systems such as the rationals, there are other, less immediate examples of fields. The following example is a field consisting of four elements called O, I, A, and B. The notation is chosen such that O plays the role of the additive identity element (denoted 0 in the axioms above), and I is the multiplicative identity (denoted 1 in the axioms above). The field axioms can be verified by using some more field theory, or by direct computation. For example,

*A* ⋅ (*B* + *A*) = *A* ⋅ *I* = *A*, which equals *A* ⋅ *B* + *A* ⋅ *A* = *I* + *B* = *A*, as required by the distributivity.

This field is called a [finite field](https://en.wikipedia.org/wiki/Finite_field "Finite field") or **Galois field** with four elements, and is denoted **F** <sub>4</sub> or GF(4).[^15] The [subset](https://en.wikipedia.org/wiki/Subset "Subset") consisting of O and I (highlighted in red in the tables at the right) is also a field, known as the *[binary field](https://en.wikipedia.org/wiki/Binary_field "Binary field")* **F** <sub>2</sub> or GF(2).

## Elementary notions

In this section, F denotes an arbitrary field and a and b are arbitrary [elements](https://en.wikipedia.org/wiki/Element_\(set_theory\) "Element (set theory)") of F.

### Consequences of the definition

One has *a* ⋅ 0 = 0 and − *a* = (−1) ⋅ *a*.[^16]

If *ab* = 0 then *a* or b must be 0, since, if *a* ≠ 0, then *b* = (*a* <sup>−1</sup> *a*) *b* = *a* <sup>−1</sup> (*ab*) = *a* <sup>−1</sup> ⋅ 0 = 0. This means that every field is an [integral domain](https://en.wikipedia.org/wiki/Integral_domain "Integral domain").

In addition, the following properties are true for any elements a and b:

−0 = 0

1 <sup>−1</sup> = 1

−(− *a*) = *a*

(*a* <sup>−1</sup>) <sup>−1</sup> = *a* if *a* ≠ 0

(− *a*) ⋅ *b* = *a* ⋅ (− *b*) = −(*a* ⋅ *b*)

### Additive and multiplicative groups of a field

The axioms of a field F imply that it is an [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") under addition. This group is called the [additive group](https://en.wikipedia.org/wiki/Additive_group "Additive group") of the field, and is sometimes denoted by (*F*, +) when denoting it simply as F could be confusing.

Similarly, the *nonzero* elements of F form an abelian group under multiplication, called the [multiplicative group](https://en.wikipedia.org/wiki/Multiplicative_group "Multiplicative group"), and denoted by ${\displaystyle (F\smallsetminus \{0\},\cdot )}$ or just ${\displaystyle F\smallsetminus \{0\}}$, or *F* <sup>×</sup>.

A field may thus be defined as set F equipped with two operations denoted as an addition and a multiplication such that F is an abelian group under addition, ${\displaystyle F\smallsetminus \{0\}}$ is an abelian group under multiplication (where 0 is the identity element of the addition), and multiplication is [distributive](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") over addition.[^2] Some elementary statements about fields can therefore be obtained by applying general facts of [groups](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)"). For example, the additive and multiplicative inverses − *a* and *a* <sup>−1</sup> are uniquely determined by a.

The requirement 1 ≠ 0 is imposed by convention to exclude the [trivial ring](https://en.wikipedia.org/wiki/Trivial_ring "Trivial ring"), which consists of a single element; indeed, the nonzero elements of the trivial ring (there are none) do not form a group, since a group must have at least one element.[^3]

Every finite [subgroup](https://en.wikipedia.org/wiki/Subgroup "Subgroup") of the multiplicative group of a field is [cyclic](https://en.wikipedia.org/wiki/Cyclic_group "Cyclic group") (see *[Root of unity § Cyclic groups](https://en.wikipedia.org/wiki/Root_of_unity#Cyclic_groups "Root of unity")*).

### Characteristic

In addition to the multiplication of two elements of F, it is possible to define the product *n* ⋅ *a* of an arbitrary element a of F by a positive [integer](https://en.wikipedia.org/wiki/Integer "Integer") n to be the n-fold sum

*a* + *a* +... + *a* (which is an element of F.)

If there is no positive integer such that

*n* ⋅ 1 = 0,

then F is said to have [characteristic](https://en.wikipedia.org/wiki/Characteristic_\(algebra\) "Characteristic (algebra)") 0.[^18] For example, the field of rational numbers **Q** has characteristic 0 since no positive integer n is zero. Otherwise, if there *is* a positive integer n satisfying this equation, the smallest such positive integer can be shown to be a [prime number](https://en.wikipedia.org/wiki/Prime_number "Prime number"). It is usually denoted by p and the field is said to have characteristic p then. For example, the field **F** <sub>4</sub> has characteristic 2 since (in the notation of the above addition table) *I* + *I* = O.

If F has characteristic p, then *p* ⋅ *a* = 0 for all a in F. This implies that

(*a* + *b*) <sup><i>p</i></sup> = *a* <sup><i>p</i></sup> + *b* <sup><i>p</i></sup>,

since all other [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient "Binomial coefficient") appearing in the [binomial formula](https://en.wikipedia.org/wiki/Binomial_formula "Binomial formula") are divisible by p. Here, *a* <sup><i>p</i></sup>:= *a* ⋅ *a* ⋅ ⋯ ⋅ *a* (p factors) is the pth power, i.e., the p-fold product of the element a. Therefore, the [Frobenius map](https://en.wikipedia.org/wiki/Frobenius_map "Frobenius map")

*F* → *F*: *x* ↦ *x* <sup><i>p</i></sup>

is compatible with the addition in F (and also with the multiplication), and is therefore a field homomorphism.[^19] The existence of this homomorphism makes fields in characteristic p quite different from fields of characteristic 0.

### Subfields and prime fields

A *[subfield](https://en.wikipedia.org/wiki/Field_extension "Field extension")* E of a field F is a subset of F that is a field with respect to the field operations of F. Equivalently E is a subset of F that contains 1, and is closed under addition, multiplication, additive inverse and multiplicative inverse of a nonzero element. This means that 1 ∊ *E*, that for all *a*, *b* ∊ *E* both *a* + *b* and *a* ⋅ *b* are in E, and that for all *a* ≠ 0 in E, both − *a* and 1/ *a* are in E.

[Field homomorphisms](https://en.wikipedia.org/wiki/Field_homomorphism "Field homomorphism") are maps *φ*: *E* → *F* between two fields such that *φ* (*e* <sub>1</sub> + *e* <sub>2</sub>) = *φ* (*e* <sub>1</sub>) + *φ* (*e* <sub>2</sub>), *φ* (*e* <sub>1</sub> *e* <sub>2</sub>) = *φ* (*e* <sub>1</sub>)  *φ* (*e* <sub>2</sub>), and *φ* (1 <sub><i>E</i></sub>) = 1 <sub><i>F</i></sub>, where *e* <sub>1</sub> and *e* <sub>2</sub> are arbitrary elements of E. All field homomorphisms are [injective](https://en.wikipedia.org/wiki/Injective "Injective").[^20] If *φ* is also [surjective](https://en.wikipedia.org/wiki/Surjective "Surjective"), it is called an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism") (or the fields E and F are called isomorphic).

A field is called a **prime field** if it has no proper (i.e., strictly smaller) subfields. Any field F contains a prime field. If the [characteristic](https://en.wikipedia.org/wiki/Characteristic_\(algebra\) "Characteristic (algebra)") of F is p (a prime number), the prime field is isomorphic to the finite field **F** <sub><i>p</i></sub> introduced below. Otherwise the prime field is isomorphic to **Q**.[^21]

## Finite fields

*Finite fields* (also called *Galois fields*) are fields with finitely many elements, whose number is also referred to as the order of the field. The above introductory example **F** <sub>4</sub> is a field with four elements. Its subfield **F** <sub>2</sub> is the smallest field, because by definition a field has at least two distinct elements, 0 and 1.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Clock_group.svg/250px-Clock_group.svg.png)

In modular arithmetic modulo 12, 9 + 4 = 1 since 9 + 4 = 13 in Z, which divided by 12 leaves remainder 1. However, /12 is not a field because is not a prime number.

The simplest finite fields, with prime order, are most directly accessible using [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic "Modular arithmetic"). For a fixed positive integer n, arithmetic "modulo n" means to work with the numbers

**Z** / *n* **Z** = {0, 1,..., *n* − 1}.

The addition and multiplication on this set are done by performing the operation in question in the set **Z** of integers, dividing by n and taking the remainder as result. This construction yields a field precisely if n is a [prime number](https://en.wikipedia.org/wiki/Prime_number "Prime number"). For example, taking the prime *n* = 2 results in the above-mentioned field **F** <sub>2</sub>. For *n* = 4 and more generally, for any [composite number](https://en.wikipedia.org/wiki/Composite_number "Composite number") (i.e., any number n which can be expressed as a product *n* = *r* ⋅ *s* of two strictly smaller natural numbers), **Z** / *n* **Z** is not a field: the product of two non-zero elements is zero since *r* ⋅ *s* = 0 in **Z** / *n* **Z**, which, as was explained [above](#Consequences_of_the_definition), prevents **Z** / *n* **Z** from being a field. The field **Z** / *p* **Z** with p elements (p being prime) constructed in this way is usually denoted by **F** <sub><i>p</i></sub>.

Every finite field F has *q* = *p* <sup><i>n</i></sup> elements, where *p* is prime and *n* ≥ 1. This statement holds since F may be viewed as a [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") over its prime field. The [dimension](https://en.wikipedia.org/wiki/Dimension_of_a_vector_space "Dimension of a vector space") of this vector space is necessarily finite, say n, which implies the asserted statement.[^22]

A field with *q* = *p* <sup><i>n</i></sup> elements can be constructed as the [splitting field](https://en.wikipedia.org/wiki/Splitting_field "Splitting field") of the [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial")

*f* (*x*) = *x* <sup><i>q</i></sup> − *x*.

Such a splitting field is an extension of **F** <sub><i>p</i></sub> in which the polynomial f has q zeros. This means f has as many zeros as possible since the [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial "Degree of a polynomial") of f is q. For *q* = 2 <sup>2</sup> = 4, it can be checked case by case using the above multiplication table that all four elements of **F** <sub>4</sub> satisfy the equation *x* <sup>4</sup> = *x*, so they are zeros of f. By contrast, in **F** <sub>2</sub>, f has only two zeros (namely 0 and 1), so f does not split into linear factors in this smaller field. Elaborating further on basic field-theoretic notions, it can be shown that two finite fields with the same order are isomorphic.[^23] It is thus customary to speak of *the* finite field with q elements, denoted by **F** <sub><i>q</i></sub> or GF(*q*).

## History

Historically, three algebraic disciplines led to the concept of a field: the question of solving polynomial equations, [algebraic number theory](https://en.wikipedia.org/wiki/Algebraic_number_theory "Algebraic number theory"), and [algebraic geometry](https://en.wikipedia.org/wiki/Algebraic_geometry "Algebraic geometry").[^24] A first step towards the notion of a field was made in 1770 by [Joseph-Louis Lagrange](https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange "Joseph-Louis Lagrange"), who observed that permuting the zeros *x* <sub>1</sub>, *x* <sub>2</sub>, *x* <sub>3</sub> of a [cubic polynomial](https://en.wikipedia.org/wiki/Cubic_polynomial "Cubic polynomial") in the expression

(*x* <sub>1</sub> + *ωx* <sub>2</sub> + *ω* <sup>2</sup> *x* <sub>3</sub>) <sup>3</sup>

(with *ω* being a third [root of unity](https://en.wikipedia.org/wiki/Root_of_unity "Root of unity")) only yields two values. This way, Lagrange conceptually explained the classical solution method of [Scipione del Ferro](https://en.wikipedia.org/wiki/Scipione_del_Ferro "Scipione del Ferro") and [François Viète](https://en.wikipedia.org/wiki/Fran%C3%A7ois_Vi%C3%A8te "François Viète"), which proceeds by reducing a cubic equation for an unknown x to a quadratic equation for *x* <sup>3</sup>.[^25] Together with a similar observation for [equations of degree 4](https://en.wikipedia.org/wiki/Quartic_polynomial "Quartic polynomial"), Lagrange thus linked what eventually became the concept of fields and the concept of groups.[^26] [Vandermonde](https://en.wikipedia.org/wiki/Alexandre-Th%C3%A9ophile_Vandermonde "Alexandre-Théophile Vandermonde"), also in 1770, and to a fuller extent, [Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss "Carl Friedrich Gauss"), in his *[Disquisitiones Arithmeticae](https://en.wikipedia.org/wiki/Disquisitiones_Arithmeticae "Disquisitiones Arithmeticae")* (1801), studied the equation

*x* <sup><i>p</i></sup> = 1

for a prime p and, again using modern language, the resulting cyclic [Galois group](https://en.wikipedia.org/wiki/Galois_group "Galois group"). Gauss deduced that a [regular p-gon](https://en.wikipedia.org/wiki/Regular_polygon "Regular polygon") can be constructed if *p* = 2 <sup>2 <sup><i>k</i></sup></sup> + 1. Building on Lagrange's work, [Paolo Ruffini](https://en.wikipedia.org/wiki/Paolo_Ruffini_\(mathematician\) "Paolo Ruffini (mathematician)") claimed (1799) that [quintic equations](https://en.wikipedia.org/wiki/Quintic_equation "Quintic equation") (polynomial equations of degree 5) cannot be solved algebraically; however, his arguments were incomplete. These gaps were filled by [Niels Henrik Abel](https://en.wikipedia.org/wiki/Niels_Henrik_Abel "Niels Henrik Abel") in 1824.[^27] [Évariste Galois](https://en.wikipedia.org/wiki/%C3%89variste_Galois "Évariste Galois"), in 1832, devised necessary and sufficient criteria for a polynomial equation to be algebraically solvable, thus establishing in effect what is known as [Galois theory](https://en.wikipedia.org/wiki/Galois_theory "Galois theory") today. Both Abel and Galois worked with what is today called an [algebraic number field](https://en.wikipedia.org/wiki/Algebraic_number_field "Algebraic number field"), but they conceived neither an explicit notion of a field, nor of a group.

In 1871 [Richard Dedekind](https://en.wikipedia.org/wiki/Richard_Dedekind "Richard Dedekind") introduced, for a set of real or complex numbers that is closed under the four arithmetic operations, the [German](https://en.wikipedia.org/wiki/German_\(language\) "German (language)") word *Körper*, which means "body" or "corpus" (to suggest an organically closed entity). The English term "field" was introduced by [Moore (1893)](#CITEREFMoore1893).[^28]

> By a field we will mean every infinite system of real or complex numbers so closed in itself and perfect that addition, subtraction, multiplication, and division of any two of these numbers again yields a number of the system.

— Richard Dedekind, 1871 [^29]

In 1881 [Leopold Kronecker](https://en.wikipedia.org/wiki/Leopold_Kronecker "Leopold Kronecker") defined what he called a *domain of rationality*, which is a field of [rational fractions](https://en.wikipedia.org/wiki/Rational_fraction "Rational fraction") in modern terms. Kronecker's notion did not cover the field of all algebraic numbers (which is a field in Dedekind's sense), but on the other hand was more abstract than Dedekind's in that it made no specific assumption on the nature of the elements of a field. Kronecker interpreted a field such as **Q** (π) abstractly as the rational function field **Q** (*X*). Prior to this, examples of transcendental numbers were known since [Joseph Liouville](https://en.wikipedia.org/wiki/Joseph_Liouville "Joseph Liouville") 's work in 1844, until [Charles Hermite](https://en.wikipedia.org/wiki/Charles_Hermite "Charles Hermite") (1873) and [Ferdinand von Lindemann](https://en.wikipedia.org/wiki/Ferdinand_von_Lindemann "Ferdinand von Lindemann") (1882) proved the transcendence of e and *π*, respectively.[^30]

The first clear definition of an abstract field is due to [Weber (1893)](#CITEREFWeber1893).[^31] In particular, [Heinrich Martin Weber](https://en.wikipedia.org/wiki/Heinrich_Martin_Weber "Heinrich Martin Weber") 's notion included the field **F** <sub><i>p</i></sub>. [Giuseppe Veronese](https://en.wikipedia.org/wiki/Giuseppe_Veronese "Giuseppe Veronese") (1891) studied the field of formal power series, which led [Hensel (1904)](#CITEREFHensel1904) to introduce the field of p-adic numbers. [Steinitz (1910)](#CITEREFSteinitz1910) synthesized the knowledge of abstract field theory accumulated so far. He axiomatically studied the properties of fields and defined many important field-theoretic concepts. The majority of the theorems mentioned in the sections [Galois theory](#Galois_theory), [Constructing fields](#Constructing_fields) and [Elementary notions](#Elementary_notions) can be found in Steinitz's work. [Artin & Schreier (1927)](#CITEREFArtinSchreier1927) linked the notion of [orderings in a field](https://en.wikipedia.org/wiki/Ordered_field "Ordered field"), and thus the area of analysis, to purely algebraic properties.[^32] [Emil Artin](https://en.wikipedia.org/wiki/Emil_Artin "Emil Artin") redeveloped Galois theory from 1928 through 1942, eliminating the dependency on the [primitive element theorem](https://en.wikipedia.org/wiki/Primitive_element_theorem "Primitive element theorem").

## Constructing fields

### Constructing fields from rings

A [commutative ring](https://en.wikipedia.org/wiki/Commutative_ring "Commutative ring") is a set that is equipped with an addition and multiplication operation and satisfies all the axioms of a field, except for the existence of multiplicative inverses *a* <sup>−1</sup>.[^33] For example, the integers **Z** form a commutative ring, but not a field: the [reciprocal](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse") of an integer n is not itself an integer, unless *n* = ±1.

In the hierarchy of algebraic structures fields can be characterized as the commutative rings R in which every nonzero element is a [unit](https://en.wikipedia.org/wiki/Unit_\(ring_theory\) "Unit (ring theory)") (which means every element is invertible). Similarly, fields are the commutative rings with precisely two distinct [ideals](https://en.wikipedia.org/wiki/Ideal_\(ring_theory\) "Ideal (ring theory)"), (0) and R. Fields are also precisely the commutative rings in which (0) is the only [prime ideal](https://en.wikipedia.org/wiki/Prime_ideal "Prime ideal").

Given a commutative ring R, there are two ways to construct a field related to R, i.e., two ways of modifying R such that all nonzero elements become invertible: forming the field of fractions, and forming residue fields. The field of fractions of **Z** is **Q**, the rationals, while the residue fields of **Z** are the finite fields **F** <sub><i>p</i></sub>.

#### Field of fractions

Given an [integral domain](https://en.wikipedia.org/wiki/Integral_domain "Integral domain") R, its [field of fractions](https://en.wikipedia.org/wiki/Field_of_fractions "Field of fractions") *Q* (*R*) is built with the fractions of two elements of R exactly as **Q** is constructed from the integers. More precisely, the elements of *Q* (*R*) are the fractions *a* / *b* where a and b are in R, and *b* ≠ 0. Two fractions *a* / *b* and *c* / *d* are equal if and only if *ad* = *bc*. The operation on the fractions work exactly as for rational numbers. For example,

${\displaystyle {\frac {a}{b}}+{\frac {c}{d}}={\frac {ad+bc}{bd}}.}$

It is straightforward to show that, if the ring is an integral domain, the set of the fractions form a field.[^34]

The field *F* (*x*) of the [rational fractions](https://en.wikipedia.org/wiki/Rational_fraction "Rational fraction") over a field (or an integral domain) F is the field of fractions of the [polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring "Polynomial ring") *F* \[*x*\]. The field *F* ((*x*)) of formal [Laurent series](https://en.wikipedia.org/wiki/Laurent_series "Laurent series")

${\displaystyle \sum _{i=k}^{\infty }a_{i}x^{i}\ (k\in \mathbb {Z} ,a_{i}\in F)}$

over a field F is the field of fractions of the ring *F* \[\[*x*\]\] of [formal power series](https://en.wikipedia.org/wiki/Formal_power_series "Formal power series") (in which *k* ≥ 0). Since any Laurent series is a fraction of a power series divided by a power of x (as opposed to an arbitrary power series), the representation of fractions is less important in this situation, though.

#### Residue fields

In addition to the field of fractions, which embeds R [injectively](https://en.wikipedia.org/wiki/Injective_map "Injective map") into a field, a field can be obtained from a commutative ring R by means of a [surjective map](https://en.wikipedia.org/wiki/Surjective_map "Surjective map") onto a field F. Any field obtained in this way is a [quotient](https://en.wikipedia.org/wiki/Quotient_ring "Quotient ring") *R* / *m*, where m is a [maximal ideal](https://en.wikipedia.org/wiki/Maximal_ideal "Maximal ideal") of R. If R [has only one maximal ideal](https://en.wikipedia.org/wiki/Local_ring "Local ring") m, this field is called the [residue field](https://en.wikipedia.org/wiki/Residue_field "Residue field") of R.[^35]

The [ideal generated by a single polynomial](https://en.wikipedia.org/wiki/Principal_ideal "Principal ideal") f in the polynomial ring *R* = *E* \[*X*\] (over a field E) is maximal if and only if f is [irreducible](https://en.wikipedia.org/wiki/Irreducible_polynomial "Irreducible polynomial") in E, i.e., if f cannot be expressed as the product of two polynomials in *E* \[*X*\] of smaller [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial "Degree of a polynomial"). This yields a field

*K* = *E* \[*X*\] / (*f* (*X*)).

This field K contains an element x (namely the [residue class](https://en.wikipedia.org/wiki/Residue_class "Residue class") of X) which satisfies the equation

*f* (*x*) = 0.

For example, **C** is obtained from **R** by [adjoining](https://en.wikipedia.org/wiki/Adjunction_\(field_theory\) "Adjunction (field theory)") the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit "Imaginary unit") symbol i, which satisfies *f* (*i*) = 0, where *f* (*X*) = *X* <sup>2</sup> + 1. Moreover, f is irreducible over **R**, which implies that the map that sends a polynomial *f* (*X*) ∊ **R** \[*X*\] to *f* (*i*) yields an isomorphism

${\displaystyle \mathbf {R} [X]{\big /}\left(X^{2}+1\right)\ {\stackrel {\cong }{\longrightarrow }}\ \mathbf {C} .}$

### Constructing fields within a bigger field

Fields can be constructed inside a given bigger container field. Suppose given a field E, and a field F containing E as a subfield. For any element x of F, there is a smallest subfield of F containing E and x, called the subfield of *F* generated by x and denoted *E* (*x*).[^36] The passage from E to *E* (*x*) is referred to by *[adjoining](https://en.wikipedia.org/wiki/Adjunction_\(field_theory\) "Adjunction (field theory)") an element* to E. More generally, for a subset *S* ⊂ *F*, there is a minimal subfield of F containing E and S, denoted by *E* (*S*).

The [compositum](https://en.wikipedia.org/wiki/Compositum "Compositum") of two subfields E and *E* ′ of some field F is the smallest subfield of F containing both E and *E* ′. The compositum can be used to construct the biggest subfield of F satisfying a certain property, for example the biggest subfield of F, which is, in the language introduced below, algebraic over E.[^4]

### Field extensions

The notion of a subfield *E* ⊂ *F* can also be regarded from the opposite point of view, by referring to F being a *[field extension](https://en.wikipedia.org/wiki/Field_extension "Field extension")* (or just extension) of E, denoted by

*F* / *E*,

and read "F over E".

A basic datum of a field extension is its [degree](https://en.wikipedia.org/wiki/Degree_of_a_field_extension "Degree of a field extension") \[*F*: *E*\], i.e., the dimension of F as an E-vector space. It satisfies the formula [^37]

\[*G*: *E*\] = \[*G*: *F*\] \[*F*: *E*\].

Extensions whose degree is finite are referred to as finite extensions. The extensions **C** / **R** and **F** <sub>4</sub> / **F** <sub>2</sub> are of degree 2, whereas **R** / **Q** is an infinite extension.

#### Algebraic extensions

A pivotal notion in the study of field extensions *F* / *E* are [algebraic elements](https://en.wikipedia.org/wiki/Algebraic_element "Algebraic element"). An element *x* ∈ *F* is *algebraic* over E if it is a [root](https://en.wikipedia.org/wiki/Zero_of_a_function "Zero of a function") of a [polynomial](https://en.wikipedia.org/wiki/Polynomial "Polynomial") with [coefficients](https://en.wikipedia.org/wiki/Coefficient "Coefficient") in E, that is, if it satisfies a [polynomial equation](https://en.wikipedia.org/wiki/Polynomial_equation "Polynomial equation")

*e* <sub><i>n</i></sub>   *x* <sup><i>n</i></sup> + *e* <sub><i>n</i> −1</sub> *x* <sup><i>n</i> −1</sup> + ⋯ + *e* <sub>1</sub> *x* + *e* <sub>0</sub> = 0,

with *e* <sub><i>n</i></sub>,..., *e* <sub>0</sub> in E, and *e* <sub><i>n</i></sub> ≠ 0. For example, the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit "Imaginary unit") i in **C** is algebraic over **R**, and even over **Q**, since it satisfies the equation

*i* <sup>2</sup> + 1 = 0.

A field extension in which every element of F is algebraic over E is called an [algebraic extension](https://en.wikipedia.org/wiki/Algebraic_extension "Algebraic extension"). Any finite extension is necessarily algebraic, as can be deduced from the above multiplicativity formula.[^38]

The subfield *E* (*x*) generated by an element x, as above, is an algebraic extension of E if and only if x is an algebraic element. That is to say, if x is algebraic, all other elements of *E* (*x*) are necessarily algebraic as well. Moreover, the degree of the extension *E* (*x*) / *E*, i.e., the dimension of *E* (*x*) as an E-vector space, equals the minimal degree n such that there is a polynomial equation involving x, as above. If this degree is n, then the elements of *E* (*x*) have the form

${\displaystyle \sum _{k=0}^{n-1}a_{k}x^{k},\ \ a_{k}\in E.}$

For example, the field **Q** (*i*) of [Gaussian rationals](https://en.wikipedia.org/wiki/Gaussian_rational "Gaussian rational") is the subfield of **C** consisting of all numbers of the form *a* + *bi* where both a and b are rational numbers: summands of the form *i* <sup>2</sup> (and similarly for higher exponents) do not have to be considered here, since *a* + *bi* + *ci* <sup>2</sup> can be simplified to *a* − *c* + *bi*.

#### Transcendence bases

The above-mentioned field of [rational fractions](https://en.wikipedia.org/wiki/Rational_fraction "Rational fraction") *E* (*X*), where X is an [indeterminate](https://en.wikipedia.org/wiki/Indeterminate_\(variable\) "Indeterminate (variable)"), is not an algebraic extension of E since there is no polynomial equation with coefficients in E whose zero is X. Elements, such as X, which are not algebraic are called [transcendental](https://en.wikipedia.org/wiki/Algebraic_element "Algebraic element"). Informally speaking, the indeterminate X and its powers do not interact with elements of E. A similar construction can be carried out with a set of indeterminates, instead of just one.

Once again, the field extension *E* (*x*) / *E* discussed above is a key example: if x is not algebraic (i.e., x is not a [root](https://en.wikipedia.org/wiki/Root_of_a_function "Root of a function") of a polynomial with coefficients in E), then *E* (*x*) is isomorphic to *E* (*X*). This isomorphism is obtained by substituting x to X in rational fractions.

A subset S of a field F is a [transcendence basis](https://en.wikipedia.org/wiki/Transcendence_basis "Transcendence basis") if it is [algebraically independent](https://en.wikipedia.org/wiki/Algebraically_independent "Algebraically independent") (do not satisfy any polynomial relations) over E and if F is an algebraic extension of *E* (*S*). Any field extension *F* / *E* has a transcendence basis.[^39] Thus, field extensions can be split into ones of the form *E* (*S*) / *E* ([purely transcendental extensions](https://en.wikipedia.org/wiki/Transcendental_extension "Transcendental extension")) and algebraic extensions.

### Closure operations

A field is [algebraically closed](https://en.wikipedia.org/wiki/Algebraically_closed "Algebraically closed") if it does not have any strictly bigger algebraic extensions or, equivalently, if any [polynomial equation](https://en.wikipedia.org/wiki/Polynomial_equation "Polynomial equation")

*f* <sub><i>n</i></sub>   *x* <sup><i>n</i></sup> + *f* <sub><i>n</i> −1</sub> *x* <sup><i>n</i> −1</sup> + ⋯ + *f* <sub>1</sub> *x* + *f* <sub>0</sub> = 0, with coefficients *f* <sub><i>n</i></sub>,..., *f* <sub>0</sub> ∈ *F*, *n* > 0,

has a solution *x* ∊ *F*.[^40] By the [fundamental theorem of algebra](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra "Fundamental theorem of algebra"), **C** is algebraically closed, i.e., *any* polynomial equation with complex coefficients has a complex solution. The rational and the real numbers are *not* algebraically closed since the equation

*x* <sup>2</sup> + 1 = 0

does not have any rational or real solution. A field containing F is called an *[algebraic closure](https://en.wikipedia.org/wiki/Algebraic_closure "Algebraic closure")* of F if it is [algebraic](https://en.wikipedia.org/wiki/Algebraic_extension "Algebraic extension") over F (roughly speaking, not too big compared to F) and is algebraically closed (big enough to contain solutions of all polynomial equations).

By the above, **C** is an algebraic closure of **R**. The situation that the algebraic closure is a finite extension of the field F is quite special: by the [Artin–Schreier theorem](https://en.wikipedia.org/wiki/Artin%E2%80%93Schreier_theorem "Artin–Schreier theorem"), the degree of this extension is necessarily 2, and F is [elementarily equivalent](https://en.wikipedia.org/wiki/Elementarily_equivalent "Elementarily equivalent") to **R**. Such fields are also known as [real closed fields](https://en.wikipedia.org/wiki/Real_closed_field "Real closed field").

Any field F has an algebraic closure, which is moreover unique up to (non-unique) isomorphism. It is commonly referred to as *the* algebraic closure and denoted *F*. For example, the algebraic closure **Q** of **Q** is called the field of [algebraic numbers](https://en.wikipedia.org/wiki/Algebraic_number "Algebraic number"). The field *F* is usually rather implicit since its construction requires the [ultrafilter lemma](https://en.wikipedia.org/wiki/Ultrafilter_lemma "Ultrafilter lemma"), a set-theoretic axiom that is weaker than the [axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice "Axiom of choice").[^41] In this regard, the algebraic closure of **F** <sub><i>q</i></sub>, is exceptionally simple. It is the union of the finite fields containing **F** <sub><i>q</i></sub> (the ones of order *q* <sup><i>n</i></sup>). For any algebraically closed field F of characteristic 0, the algebraic closure of the field *F* ((*t*)) of [Laurent series](https://en.wikipedia.org/wiki/Laurent_series "Laurent series") is the field of [Puiseux series](https://en.wikipedia.org/wiki/Puiseux_series "Puiseux series"), obtained by adjoining roots of t.[^42]

## Fields with additional structure

Since fields are ubiquitous in mathematics and beyond, several refinements of the concept have been adapted to the needs of particular mathematical areas.

### Ordered fields

A field *F* is called an *ordered field* if any two elements can be compared, so that *x* + *y* ≥ 0 and *xy* ≥ 0 whenever *x* ≥ 0 and *y* ≥ 0. For example, the real numbers form an ordered field, with the usual ordering ≥. The [Artin–Schreier theorem](https://en.wikipedia.org/wiki/Artin%E2%80%93Schreier_theorem "Artin–Schreier theorem") states that a field can be ordered if and only if it is a [formally real field](https://en.wikipedia.org/wiki/Formally_real_field "Formally real field"), which means that any quadratic equation

${\displaystyle x_{1}^{2}+x_{2}^{2}+\dots +x_{n}^{2}=0}$

only has the solution *x* <sub>1</sub> = *x* <sub>2</sub> = ⋯ = *x* <sub><i>n</i></sub> = 0.[^43] The set of all possible orders on a fixed field F is isomorphic to the set of [ring homomorphisms](https://en.wikipedia.org/wiki/Ring_homomorphism "Ring homomorphism") from the [Witt ring](https://en.wikipedia.org/wiki/Witt_ring_\(forms\) "Witt ring (forms)") W(*F*) of [quadratic forms](https://en.wikipedia.org/wiki/Quadratic_form "Quadratic form") over F, to **Z**.[^44]

An [Archimedean field](https://en.wikipedia.org/wiki/Archimedean_field "Archimedean field") is an ordered field such that for each element there exists a finite expression

1 + 1 + ⋯ + 1

whose value is greater than that element, that is, there are no infinite elements. Equivalently, the field contains no [infinitesimals](https://en.wikipedia.org/wiki/Infinitesimals "Infinitesimals") (elements smaller than all rational numbers); or, yet equivalent, the field is isomorphic to a subfield of **R**.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Illustration_of_supremum.svg/330px-Illustration_of_supremum.svg.png)

Each bounded real set has a least upper bound.

An ordered field is [Dedekind-complete](https://en.wikipedia.org/wiki/Dedekind-complete "Dedekind-complete") if all [upper bounds](https://en.wikipedia.org/wiki/Upper_bound "Upper bound"), [lower bounds](https://en.wikipedia.org/wiki/Lower_bound "Lower bound") (see *[Dedekind cut](https://en.wikipedia.org/wiki/Dedekind_cut "Dedekind cut")*) and limits, which should exist, do exist. More formally, each [bounded subset](https://en.wikipedia.org/wiki/Bounded_set "Bounded set") of F is required to have a least upper bound. Any complete field is necessarily Archimedean,[^45] since in any non-Archimedean field there is neither a greatest infinitesimal nor a least positive rational, whence the sequence 1/2, 1/3, 1/4,..., every element of which is greater than every infinitesimal, has no limit.

Since every proper subfield of the reals also contains such gaps, **R** is the unique complete ordered field, up to isomorphism.[^46] Several foundational results in [calculus](https://en.wikipedia.org/wiki/Calculus "Calculus") follow directly from this characterization of the reals.

The [hyperreals](https://en.wikipedia.org/wiki/Hyperreals "Hyperreals") **R** <sup>*</sup> form an ordered field that is not Archimedean. It is an extension of the reals obtained by including infinite and infinitesimal numbers. These are larger, respectively smaller than any real number. The hyperreals form the foundational basis of [non-standard analysis](https://en.wikipedia.org/wiki/Non-standard_analysis "Non-standard analysis").

### Topological fields

Another refinement of the notion of a field is a **topological field**, in which the set F is a [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space"), such that all operations of the field (addition, multiplication, the maps *a* ↦ − *a* and *a* ↦ *a* <sup>−1</sup>) are [continuous maps](https://en.wikipedia.org/wiki/Continuous_map "Continuous map") with respect to the topology of the space.[^47] The topology of all the fields discussed below is induced from a [metric](https://en.wikipedia.org/wiki/Metric_\(mathematics\) "Metric (mathematics)"), i.e., a [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)")

*d*: *F* × *F* → **R**,

that measures a *distance* between any two elements of F.

The [completion](https://en.wikipedia.org/wiki/Completion_\(metric_space\) "Completion (metric space)") of F is another field in which, informally speaking, the "gaps" in the original field F are filled, if there are any. For example, any [irrational number](https://en.wikipedia.org/wiki/Irrational_number "Irrational number") x, such as *x* = √2, is a "gap" in the rationals **Q** in the sense that it is a real number that can be approximated arbitrarily closely by rational numbers *p* / *q*, in the sense that distance of x and *p* / *q* given by the [absolute value](https://en.wikipedia.org/wiki/Absolute_value "Absolute value") | *x* − *p* / *q* | is as small as desired. The following table lists some examples of this construction. The fourth column shows an example of a zero [sequence](https://en.wikipedia.org/wiki/Sequence "Sequence"), i.e., a sequence whose limit (for *n* → ∞) is zero.

| Field | Metric | Completion | zero sequence |
| --- | --- | --- | --- |
| **Q** | \| *x* − *y* \| (usual [absolute value](https://en.wikipedia.org/wiki/Absolute_value "Absolute value")) | **R** | 1/ *n* |
| **Q** | obtained using the [*p* -adic valuation](https://en.wikipedia.org/wiki/P-adic_valuation "P-adic valuation"), for a prime number p | **Q** <sub><i>p</i></sub> ([p-adic numbers](https://en.wikipedia.org/wiki/P-adic_number "P-adic number")) | *p* <sup><i>n</i></sup> |
| *F* (*t*)   (F any field) | obtained using the t-adic valuation | *F* ((*t*)) | *t* <sup><i>n</i></sup> |

The field **Q** <sub><i>p</i></sub> is used in number theory and [p-adic analysis](https://en.wikipedia.org/wiki/P-adic_analysis "P-adic analysis"). The algebraic closure **Q** <sub><i>p</i></sub> carries a unique norm extending the one on **Q** <sub><i>p</i></sub>, but is not complete. The completion of this algebraic closure, however, is algebraically closed. Because of its rough analogy to the complex numbers, it is sometimes called the *[complex p-adic numbers](https://en.wikipedia.org/wiki/Complex_p-adic_number "Complex p-adic number")* and is denoted **C** <sub><i>p</i></sub>.[^48]

#### Local fields

The following topological fields are called *[local fields](https://en.wikipedia.org/wiki/Local_field "Local field")*:[^49] [^5]

- finite extensions of **Q** <sub><i>p</i></sub> (local fields of characteristic zero)
- finite extensions of **F** <sub><i>p</i></sub> ((*t*)), the field of Laurent series over **F** <sub><i>p</i></sub> (local fields of characteristic p).

These two types of local fields share some fundamental similarities. In this relation, the elements *p* ∈ **Q** <sub><i>p</i></sub> and *t* ∈ **F** <sub><i>p</i></sub> ((*t*)) (referred to as [uniformizer](https://en.wikipedia.org/wiki/Uniformizer "Uniformizer")) correspond to each other. The first manifestation of this is at an elementary level: the elements of both fields can be expressed as power series in the uniformizer, with coefficients in **F** <sub><i>p</i></sub>. (However, since the addition in **Q** <sub><i>p</i></sub> is done using [carrying](https://en.wikipedia.org/wiki/Carry_\(arithmetic\) "Carry (arithmetic)"), which is not the case in **F** <sub><i>p</i></sub> ((*t*)), these fields are not isomorphic.) The following facts show that this superficial similarity goes much deeper:

- Any [first-order](https://en.wikipedia.org/wiki/First-order_logic "First-order logic") statement that is true for almost all **Q** <sub><i>p</i></sub> is also true for almost all **F** <sub><i>p</i></sub> ((*t*)). An application of this is the [Ax–Kochen theorem](https://en.wikipedia.org/wiki/Ax%E2%80%93Kochen_theorem "Ax–Kochen theorem") describing zeros of homogeneous polynomials in **Q** <sub><i>p</i></sub>.
- [Tamely ramified extensions](https://en.wikipedia.org/wiki/Splitting_of_prime_ideals_in_Galois_extensions "Splitting of prime ideals in Galois extensions") of both fields are in bijection to one another.
- Adjoining arbitrary p-power roots of p (in **Q** <sub><i>p</i></sub>), respectively of t (in **F** <sub><i>p</i></sub> ((*t*))), yields (infinite) extensions of these fields known as [perfectoid fields](https://en.wikipedia.org/wiki/Perfectoid_field "Perfectoid field"). Strikingly, the Galois groups of these two fields are isomorphic, which is the first glimpse of a remarkable parallel between these two fields:[^50] 
	$$
	{\displaystyle \operatorname {Gal} \left(\mathbf {Q} _{p}{\bigl (}p^{1/p^{\infty }}{\bigr )}\right)\cong \operatorname {Gal} \left(\mathbf {F} _{p}((t)){\bigl (}t^{1/p^{\infty }}{\bigr )}\right).}
	$$

### Differential fields

[Differential fields](https://en.wikipedia.org/wiki/Differential_field "Differential field") are fields equipped with a [derivation](https://en.wikipedia.org/wiki/Derivation_\(abstract_algebra\) "Derivation (abstract algebra)"), i.e., allow to take derivatives of elements in the field.[^51] For example, the field **R** (*X*), together with the standard derivative of polynomials forms a differential field. These fields are central to [differential Galois theory](https://en.wikipedia.org/wiki/Differential_Galois_theory "Differential Galois theory"), a variant of Galois theory dealing with [linear differential equations](https://en.wikipedia.org/wiki/Linear_differential_equation "Linear differential equation").

## Galois theory

Galois theory studies [algebraic extensions](https://en.wikipedia.org/wiki/Algebraic_extension "Algebraic extension") of a field by studying the [symmetry](https://en.wikipedia.org/wiki/Symmetry_group#Symmetry_groups_in_general "Symmetry group") in the arithmetic operations of addition and multiplication. An important notion in this area is that of [finite](https://en.wikipedia.org/wiki/Finite_extension "Finite extension") [Galois extensions](https://en.wikipedia.org/wiki/Galois_extension "Galois extension") *F* / *E*, which are, by definition, those that are [separable](https://en.wikipedia.org/wiki/Separable_extension "Separable extension") and [normal](https://en.wikipedia.org/wiki/Normal_extension "Normal extension"). The [primitive element theorem](https://en.wikipedia.org/wiki/Primitive_element_theorem "Primitive element theorem") shows that finite separable extensions are necessarily [simple](https://en.wikipedia.org/wiki/Simple_extension "Simple extension"), i.e., of the form

*F* = *E* \[*X*\] / *f* (*X*),

where f is an irreducible polynomial (as above).[^52] For such an extension, being normal and separable means that all zeros of f are contained in F and that f has only simple zeros. The latter condition is always satisfied if E has characteristic 0.

For a finite Galois extension, the [Galois group](https://en.wikipedia.org/wiki/Galois_group "Galois group") Gal(*F* / *E*) is the group of [field automorphisms](https://en.wikipedia.org/wiki/Field_automorphism "Field automorphism") of F that are trivial on E (i.e., the [bijections](https://en.wikipedia.org/wiki/Bijection "Bijection") *σ*: *F* → *F* that preserve addition and multiplication and that send elements of E to themselves). The importance of this group stems from the [fundamental theorem of Galois theory](https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory "Fundamental theorem of Galois theory"), which constructs an explicit [one-to-one correspondence](https://en.wikipedia.org/wiki/One-to-one_correspondence "One-to-one correspondence") between the set of [subgroups](https://en.wikipedia.org/wiki/Subgroup "Subgroup") of Gal(*F* / *E*) and the set of intermediate extensions of the extension *F* / *E*.[^53] By means of this correspondence, group-theoretic properties translate into facts about fields. For example, if the Galois group of a Galois extension as above is not [solvable](https://en.wikipedia.org/wiki/Solvable_group "Solvable group") (cannot be built from [abelian groups](https://en.wikipedia.org/wiki/Abelian_group "Abelian group")), then the zeros of f *cannot* be expressed in terms of addition, multiplication, and radicals, i.e., expressions involving ${\displaystyle {\sqrt[{n}]{~}}}$. For example, the [symmetric groups](https://en.wikipedia.org/wiki/Symmetric_group "Symmetric group") S <sub><i>n</i></sub> is not solvable for *n* ≥ 5. Consequently, as can be shown, the zeros of the following polynomials are not expressible by sums, products, and radicals. For the latter polynomial, this fact is known as the [Abel–Ruffini theorem](https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem "Abel–Ruffini theorem"):

*f* (*X*) = *X* <sup>5</sup> − 4 *X* + 2 (and *E* = **Q**),[^54]

*f* (*X*) = *X* <sup><i>n</i></sup> + *a* <sub><i>n</i> −1</sub> *X* <sup><i>n</i> −1</sup> + ⋯ + *a* <sub>0</sub> (where f is regarded as a polynomial in *E* (*a* <sub>0</sub>,..., *a* <sub><i>n</i> −1</sub>), for some indeterminates *a* <sub><i>i</i></sub>, E is any field, and *n* ≥ 5).

The [tensor product of fields](https://en.wikipedia.org/wiki/Tensor_product_of_fields "Tensor product of fields") is not usually a field. For example, a finite extension *F* / *E* of degree n is a Galois extension if and only if there is an isomorphism of F-algebras

*F* ⊗ <sub><i>E</i></sub> *F* ≅ *F* <sup><i>n</i></sup>.

This fact is the beginning of [Grothendieck's Galois theory](https://en.wikipedia.org/wiki/Grothendieck%27s_Galois_theory "Grothendieck's Galois theory"), a far-reaching extension of Galois theory applicable to algebro-geometric objects.[^55]

## Invariants of fields

Basic invariants of a field F include the characteristic and the [transcendence degree](https://en.wikipedia.org/wiki/Transcendence_degree "Transcendence degree") of F over its prime field. The latter is defined as the maximal number of elements in F that are algebraically independent over the prime field. Two algebraically closed fields E and F are isomorphic precisely if these two data agree.[^56] This implies that any two [uncountable](https://en.wikipedia.org/wiki/Uncountable "Uncountable") algebraically closed fields of the same [cardinality](https://en.wikipedia.org/wiki/Cardinality "Cardinality") and the same characteristic are isomorphic. For example, **Q** <sub><i>p</i></sub>, **C** <sub><i>p</i></sub> and **C** are isomorphic (but *not* isomorphic as topological fields).

### Model theory of fields

In [model theory](https://en.wikipedia.org/wiki/Model_theory "Model theory"), a branch of [mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic "Mathematical logic"), two fields E and F are called [elementarily equivalent](https://en.wikipedia.org/wiki/Elementarily_equivalent "Elementarily equivalent") if every mathematical statement that is true for E is also true for F and conversely. The mathematical statements in question are required to be [first-order](https://en.wikipedia.org/wiki/First-order_logic "First-order logic") sentences (involving 0, 1, the addition and multiplication). A typical example, for *n* > 0, n an integer, is

*φ* (*E*) = "any polynomial of degree n in E has a zero in E"

The set of such formulas for all n expresses that E is algebraically closed. The [Lefschetz principle](https://en.wikipedia.org/wiki/Lefschetz_principle "Lefschetz principle") states that **C** is elementarily equivalent to any algebraically closed field F of characteristic zero. Moreover, any fixed statement *φ* holds in **C** if and only if it holds in any algebraically closed field of sufficiently high characteristic.[^57]

If U is an [ultrafilter](https://en.wikipedia.org/wiki/Ultrafilter "Ultrafilter") on a set I, and *F* <sub><i>i</i></sub> is a field for every i in I, the [ultraproduct](https://en.wikipedia.org/wiki/Ultraproduct "Ultraproduct") of the *F* <sub><i>i</i></sub> with respect to U is a field.[^58] It is denoted by

ulim <sub><i>i</i> →∞</sub> *F* <sub><i>i</i></sub>,

since it behaves in several ways as a limit of the fields *F* <sub><i>i</i></sub>: [Łoś's theorem](https://en.wikipedia.org/wiki/%C5%81o%C5%9B%27s_theorem "Łoś's theorem") states that any first order statement that holds for all but finitely many *F* <sub><i>i</i></sub>, also holds for the ultraproduct. Applied to the above sentence φ, this shows that there is an isomorphism [^6]

${\displaystyle \operatorname {ulim} _{p\to \infty }{\overline {\mathbf {F} }}_{p}\cong \mathbf {C} .}$

The Ax–Kochen theorem mentioned above also follows from this and an isomorphism of the ultraproducts (in both cases over all primes p)

ulim <sub><i>p</i></sub> **Q** <sub><i>p</i></sub> ≅ ulim <sub><i>p</i></sub> **F** <sub><i>p</i></sub> ((*t*)).

In addition, model theory also studies the logical properties of various other types of fields, such as [real closed fields](https://en.wikipedia.org/wiki/Real_closed_field "Real closed field") or [exponential fields](https://en.wikipedia.org/wiki/Exponential_field "Exponential field") (which are equipped with an exponential function exp: *F* → *F* <sup>×</sup>).[^59]

### Absolute Galois group

For fields that are not algebraically closed (or not separably closed), the [absolute Galois group](https://en.wikipedia.org/wiki/Absolute_Galois_group "Absolute Galois group") Gal(*F*) is fundamentally important: extending the case of finite Galois extensions outlined above, this group governs *all* finite separable extensions of F. By elementary means, the group Gal(**F** <sub><i>q</i></sub>) can be shown to be the [Prüfer group](https://en.wikipedia.org/wiki/Pr%C3%BCfer_group "Prüfer group"), the [profinite completion](https://en.wikipedia.org/wiki/Profinite_completion "Profinite completion") of **Z**. This statement subsumes the fact that the only algebraic extensions of Gal(**F** <sub><i>q</i></sub>) are the fields Gal(**F** <sub><i>q</i> <sup><i>n</i></sup></sub>) for *n* > 0, and that the Galois groups of these finite extensions are given by

Gal(**F** <sub><i>q</i> <sup><i>n</i></sup></sub> / **F** <sub><i>q</i></sub>) = **Z** / *n* **Z**.

A description in terms of generators and relations is also known for the Galois groups of p-adic number fields (finite extensions of **Q** <sub><i>p</i></sub>).[^60]

[Representations of Galois groups](https://en.wikipedia.org/wiki/Galois_representation "Galois representation") and of related groups such as the [Weil group](https://en.wikipedia.org/wiki/Weil_group "Weil group") are fundamental in many branches of arithmetic, such as the [Langlands program](https://en.wikipedia.org/wiki/Langlands_program "Langlands program"). The cohomological study of such representations is done using [Galois cohomology](https://en.wikipedia.org/wiki/Galois_cohomology "Galois cohomology").[^61] For example, the [Brauer group](https://en.wikipedia.org/wiki/Brauer_group "Brauer group"), which is classically defined as the group of [central simple F-algebras](https://en.wikipedia.org/wiki/Central_simple_algebra "Central simple algebra"), can be reinterpreted as a Galois cohomology group, namely

Br(*F*) = H <sup>2</sup> (*F*, **G** <sub>m</sub>).

### K-theory

[Milnor K-theory](https://en.wikipedia.org/wiki/Milnor_K-theory "Milnor K-theory") is defined as

${\displaystyle K_{n}^{M}(F)=F^{\times }\otimes \cdots \otimes F^{\times }/\left\langle x\otimes (1-x)\mid x\in F\smallsetminus \{0,1\}\right\rangle .}$

The [norm residue isomorphism theorem](https://en.wikipedia.org/wiki/Norm_residue_isomorphism_theorem "Norm residue isomorphism theorem"), proved around 2000 by [Vladimir Voevodsky](https://en.wikipedia.org/wiki/Vladimir_Voevodsky "Vladimir Voevodsky"), relates this to Galois cohomology by means of an isomorphism

${\displaystyle K_{n}^{M}(F)/p=H^{n}(F,\mu _{l}^{\otimes n}).}$

[Algebraic K-theory](https://en.wikipedia.org/wiki/Algebraic_K-theory "Algebraic K-theory") is related to the group of [invertible matrices](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix") with coefficients the given field. For example, the process of taking the [determinant](https://en.wikipedia.org/wiki/Determinant_\(mathematics\) "Determinant (mathematics)") of an invertible matrix leads to an isomorphism *K* <sub>1</sub> (*F*) = *F* <sup>×</sup>. [Matsumoto's theorem](https://en.wikipedia.org/wiki/Matsumoto%27s_theorem_\(K-theory\) "Matsumoto's theorem (K-theory)") shows that *K* <sub>2</sub> (*F*) agrees with *K* <sub>2</sub> <sup><i>M</i></sup> (*F*). In higher degrees, K-theory diverges from Milnor K-theory and remains hard to compute in general.

## Applications

### Linear algebra and commutative algebra

If *a* ≠ 0, then the [equation](https://en.wikipedia.org/wiki/Equation "Equation")

*ax* = *b*

has a unique solution x in a field F, namely ${\displaystyle x=a^{-1}b.}$ This immediate consequence of the definition of a field is fundamental in [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra "Linear algebra"). For example, it is an essential ingredient of [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination "Gaussian elimination") and of the proof that any [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") has a [basis](https://en.wikipedia.org/wiki/Basis_\(linear_algebra\) "Basis (linear algebra)").[^62]

The theory of [modules](https://en.wikipedia.org/wiki/Module_\(mathematics\) "Module (mathematics)") (the analogue of vector spaces over [rings](https://en.wikipedia.org/wiki/Ring_\(mathematics\) "Ring (mathematics)") instead of fields) is much more complicated, because the above equation may have several or no solutions. In particular [systems of linear equations over a ring](https://en.wikipedia.org/wiki/Linear_equation_over_a_ring "Linear equation over a ring") are much more difficult to solve than in the case of fields, even in the specially simple case of the ring **Z** of the integers.

### Finite fields: cryptography and coding theory

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/ECClines.svg/250px-ECClines.svg.png)

The sum of three points P, Q, and R on an elliptic curve E (red) is zero if there is a line (blue) passing through these points.

A widely applied cryptographic routine uses the fact that discrete exponentiation, i.e., computing

*a* <sup><i>n</i></sup> = *a* ⋅ *a* ⋅ ⋯ ⋅ *a* (n factors, for an integer *n* ≥ 1)

in a (large) finite field **F** <sub><i>q</i></sub> can be performed much more efficiently than the [discrete logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm "Discrete logarithm"), which is the inverse operation, i.e., determining the solution n to an equation

*a* <sup><i>n</i></sup> = *b*.

In [elliptic curve cryptography](https://en.wikipedia.org/wiki/Elliptic_curve_cryptography "Elliptic curve cryptography"), the multiplication in a finite field is replaced by the operation of adding points on an [elliptic curve](https://en.wikipedia.org/wiki/Elliptic_curve "Elliptic curve"), i.e., the solutions of an equation of the form

*y* <sup>2</sup> = *x* <sup>3</sup> + *ax* + *b*.

Finite fields are also used in [coding theory](https://en.wikipedia.org/wiki/Coding_theory "Coding theory") and [combinatorics](https://en.wikipedia.org/wiki/Combinatorics "Combinatorics").

### Geometry: field of functions

![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Double_torus_illustration.png/250px-Double_torus_illustration.png)

A compact Riemann surface of genus two (two handles). The genus can be read off the field of meromorphic functions on the surface.

[Functions](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)") on a suitable [topological space](https://en.wikipedia.org/wiki/Topological_space "Topological space") X into a field F can be added and multiplied pointwise, e.g., the product of two functions is defined by the product of their values within the domain:

(*f* ⋅ *g*)(*x*) = *f* (*x*) ⋅ *g* (*x*).

This makes these functions a F- [commutative algebra](https://en.wikipedia.org/wiki/Associative_algebra "Associative algebra").

For having a *field* of functions, one must consider algebras of functions that are [integral domains](https://en.wikipedia.org/wiki/Integral_domains "Integral domains"). In this case the ratios of two functions, i.e., expressions of the form

${\displaystyle {\frac {f(x)}{g(x)}},}$

form a field, called field of functions.

This occurs in two main cases. When X is a [complex manifold](https://en.wikipedia.org/wiki/Complex_manifold "Complex manifold") X. In this case, one considers the algebra of [holomorphic functions](https://en.wikipedia.org/wiki/Holomorphic_functions "Holomorphic functions"), i.e., complex differentiable functions. Their ratios form the field of [meromorphic functions](https://en.wikipedia.org/wiki/Meromorphic_function "Meromorphic function") on X.

The [function field of an algebraic variety](https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety "Function field of an algebraic variety") X (a geometric object defined as the common zeros of polynomial equations) consists of ratios of [regular functions](https://en.wikipedia.org/wiki/Regular_function "Regular function"), i.e., ratios of polynomial functions on the variety. The function field of the n-dimensional [space](https://en.wikipedia.org/wiki/Affine_space "Affine space") over a field F is *F* (*x* <sub>1</sub>,..., *x* <sub><i>n</i></sub>), i.e., the field consisting of ratios of polynomials in n indeterminates. The function field of X is the same as the one of any [open](https://en.wikipedia.org/wiki/Zariski_topology "Zariski topology") dense subvariety. In other words, the function field is insensitive to replacing X by a (slightly) smaller subvariety.

The function field is invariant under [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism") and [birational equivalence](https://en.wikipedia.org/wiki/Birational_equivalence "Birational equivalence") of varieties. It is therefore an important tool for the study of [abstract algebraic varieties](https://en.wikipedia.org/wiki/Abstract_algebraic_variety "Abstract algebraic variety") and for the classification of algebraic varieties. For example, the [dimension](https://en.wikipedia.org/wiki/Dimension_of_an_algebraic_variety "Dimension of an algebraic variety"), which equals the transcendence degree of *F* (*X*), is invariant under birational equivalence.[^63] For [curves](https://en.wikipedia.org/wiki/Algebraic_curve "Algebraic curve") (i.e., the dimension is one), the function field *F* (*X*) is very close to X: if X is [smooth](https://en.wikipedia.org/wiki/Smooth_variety "Smooth variety") and [proper](https://en.wikipedia.org/wiki/Proper_map "Proper map") (the analogue of being [compact](https://en.wikipedia.org/wiki/Compact_topological_space "Compact topological space")), X can be reconstructed, up to isomorphism, from its field of functions.[^7] In higher dimension the function field remembers less, but still decisive information about X. The study of function fields and their geometric meaning in higher dimensions is referred to as [birational geometry](https://en.wikipedia.org/wiki/Birational_geometry "Birational geometry"). The [minimal model program](https://en.wikipedia.org/wiki/Minimal_model_program "Minimal model program") attempts to identify the simplest (in a certain precise sense) algebraic varieties with a prescribed function field.

### Number theory: global fields

[Global fields](https://en.wikipedia.org/wiki/Global_field "Global field") are in the limelight in [algebraic number theory](https://en.wikipedia.org/wiki/Algebraic_number_theory "Algebraic number theory") and [arithmetic geometry](https://en.wikipedia.org/wiki/Arithmetic_geometry "Arithmetic geometry"). They are, by definition, [number fields](https://en.wikipedia.org/wiki/Number_field "Number field") (finite extensions of **Q**) or function fields over **F** <sub><i>q</i></sub> (finite extensions of **F** <sub><i>q</i></sub> (*t*)). As for local fields, these two types of fields share several similar features, even though they are of characteristic 0 and positive characteristic, respectively. This [function field analogy](https://en.wikipedia.org/wiki/Function_field_analogy "Function field analogy") can help to shape mathematical expectations, often first by understanding questions about function fields, and later treating the number field case. The latter is often more difficult. For example, the [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis "Riemann hypothesis") concerning the zeros of the [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function "Riemann zeta function") (open as of 2017) can be regarded as being parallel to the [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures "Weil conjectures") (proven in 1974 by [Pierre Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne "Pierre Deligne")).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/One5Root.svg/250px-One5Root.svg.png)

The fifth roots of unity form a regular pentagon.

[Cyclotomic fields](https://en.wikipedia.org/wiki/Cyclotomic_field "Cyclotomic field") are among the most intensely studied number fields. They are of the form **Q** (*ζ* <sub><i>n</i></sub>), where *ζ* <sub><i>n</i></sub> is a primitive nth [root of unity](https://en.wikipedia.org/wiki/Root_of_unity "Root of unity"), i.e., a complex number *ζ* that satisfies *ζ* <sup><i>n</i></sup> = 1 and *ζ* <sup><i>m</i></sup> ≠ 1 for all 0 < *m* < *n*.[^64] For n being a [regular prime](https://en.wikipedia.org/wiki/Regular_prime "Regular prime"), [Kummer](https://en.wikipedia.org/wiki/Ernst_Kummer "Ernst Kummer") used cyclotomic fields to prove [Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem "Fermat's Last Theorem"), which asserts the non-existence of rational nonzero solutions to the equation

*x* <sup><i>n</i></sup> + *y* <sup><i>n</i></sup> = *z* <sup><i>n</i></sup>.

Local fields are completions of global fields. [Ostrowski's theorem](https://en.wikipedia.org/wiki/Ostrowski%27s_theorem "Ostrowski's theorem") asserts that the only completions of **Q**, a global field, are the local fields **Q** <sub><i>p</i></sub> and **R**. Studying arithmetic questions in global fields may sometimes be done by looking at the corresponding questions locally. This technique is called the [local–global principle](https://en.wikipedia.org/wiki/Local%E2%80%93global_principle "Local–global principle"). For example, the [Hasse–Minkowski theorem](https://en.wikipedia.org/wiki/Hasse%E2%80%93Minkowski_theorem "Hasse–Minkowski theorem") reduces the problem of finding rational solutions of quadratic equations to solving these equations in **R** and **Q** <sub><i>p</i></sub>, whose solutions can easily be described.[^65]

Unlike for local fields, the Galois groups of global fields are not known. [Inverse Galois theory](https://en.wikipedia.org/wiki/Inverse_Galois_theory "Inverse Galois theory") studies the (unsolved) problem whether any finite group is the Galois group Gal(*F* / **Q**) for some number field F.[^66] [Class field theory](https://en.wikipedia.org/wiki/Class_field_theory "Class field theory") describes the [abelian extensions](https://en.wikipedia.org/wiki/Abelian_extension "Abelian extension"), i.e., ones with abelian Galois group, or equivalently the abelianized Galois groups of global fields. A classical statement, the [Kronecker–Weber theorem](https://en.wikipedia.org/wiki/Kronecker%E2%80%93Weber_theorem "Kronecker–Weber theorem"), describes the maximal abelian **Q** <sup>ab</sup> extension of **Q**: it is the field

**Q** (*ζ* <sub><i>n</i></sub>, *n* ≥ 2)

obtained by adjoining all primitive nth roots of unity. [Kronecker's Jugendtraum](https://en.wikipedia.org/wiki/Kronecker_Jugendtraum "Kronecker Jugendtraum") asks for a similarly explicit description of *F* <sup>ab</sup> of general number fields F. For [imaginary quadratic fields](https://en.wikipedia.org/wiki/Imaginary_quadratic_field "Imaginary quadratic field"), ${\displaystyle F=\mathbf {Q} ({\sqrt {-d}})}$, *d* > 0, the theory of [complex multiplication](https://en.wikipedia.org/wiki/Complex_multiplication "Complex multiplication") describes *F* <sup>ab</sup> using [elliptic curves](https://en.wikipedia.org/wiki/Elliptic_curves "Elliptic curves"). For general number fields, no such explicit description is known.

## Related notions

In addition to the additional structure that fields may enjoy, fields admit various other related notions. Since in any field 0 ≠ 1, any field has at least two elements. Nonetheless, there is a concept of [field with one element](https://en.wikipedia.org/wiki/Field_with_one_element "Field with one element"), which is suggested to be a limit of the finite fields **F** <sub><i>p</i></sub>, as p tends to 1.[^67] In addition to division rings, there are various other weaker algebraic structures related to fields such as [quasifields](https://en.wikipedia.org/wiki/Quasifield "Quasifield"), [near-fields](https://en.wikipedia.org/wiki/Near-field_\(mathematics\) "Near-field (mathematics)") and [semifields](https://en.wikipedia.org/wiki/Semifield "Semifield").

There are also [proper classes](https://en.wikipedia.org/wiki/Proper_class "Proper class") with field structure, which are sometimes called **Field** s, with a capital 'F'. The [surreal numbers](https://en.wikipedia.org/wiki/Surreal_number "Surreal number") form a Field containing the reals, and would be a field except for the fact that they are a proper class, not a set. The [nimbers](https://en.wikipedia.org/wiki/Nimber "Nimber"), a concept from [game theory](https://en.wikipedia.org/wiki/Game_theory "Game theory"), form such a Field as well.[^68]

### Division rings

Dropping one or several axioms in the definition of a field leads to other algebraic structures. As was mentioned above, commutative rings satisfy all field axioms except for the existence of multiplicative inverses. Dropping instead commutativity of multiplication leads to the concept of a *[division ring](https://en.wikipedia.org/wiki/Division_ring "Division ring")* or *skew field*; sometimes associativity is weakened as well. Historically, division rings were sometimes referred to as fields, while fields were called "commutative fields". The only division rings that are finite-dimensional **R** -vector spaces are **R** itself, **C** (which is a field), and the [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion") **H** (in which multiplication is non-commutative). This result is known as the [Frobenius theorem](https://en.wikipedia.org/wiki/Frobenius_theorem_\(real_division_algebras\) "Frobenius theorem (real division algebras)"). The [octonions](https://en.wikipedia.org/wiki/Octonion "Octonion") **O**, for which multiplication is neither commutative nor associative, is a normed [alternative](https://en.wikipedia.org/wiki/Alternative_algebra "Alternative algebra") division algebra, but is not a division ring. This fact was proved using methods of [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology") in 1958 by [Michel Kervaire](https://en.wikipedia.org/wiki/Michel_Kervaire "Michel Kervaire"), [Raoul Bott](https://en.wikipedia.org/wiki/Raoul_Bott "Raoul Bott"), and [John Milnor](https://en.wikipedia.org/wiki/John_Milnor "John Milnor").[^69]

[Wedderburn's little theorem](https://en.wikipedia.org/wiki/Wedderburn%27s_little_theorem "Wedderburn's little theorem") states that all finite [division rings](https://en.wikipedia.org/wiki/Division_ring "Division ring") are fields.

## Notes

## Citations

## References

- Adamson, I. T. (2007), *Introduction to Field Theory*, Dover Publications, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-486-46266-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-46266-0 "Special:BookSources/978-0-486-46266-0")
- Allenby, R. B. J. T. (1991), *Rings, Fields and Groups*, Butterworth-Heinemann, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-340-54440-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-340-54440-2 "Special:BookSources/978-0-340-54440-2")
- [Artin, Michael](https://en.wikipedia.org/wiki/Michael_Artin "Michael Artin") (1991), *Algebra*, [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall "Prentice Hall"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-13-004763-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-004763-2 "Special:BookSources/978-0-13-004763-2"), especially Chapter 13
- [Artin, Emil](https://en.wikipedia.org/wiki/Emil_Artin "Emil Artin"); [Schreier, Otto](https://en.wikipedia.org/wiki/Otto_Schreier "Otto Schreier") (1927), "Eine Kennzeichnung der reell abgeschlossenen Körper", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* (in German), **5**: 225–231, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BF02952522](https://doi.org/10.1007%2FBF02952522), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0025-5858](https://search.worldcat.org/issn/0025-5858), [JFM](https://en.wikipedia.org/wiki/JFM_\(identifier\) "JFM (identifier)") [53.0144.01](https://zbmath.org/?format=complete&q=an:53.0144.01), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [121547404](https://api.semanticscholar.org/CorpusID:121547404)
- [Ax, James](https://en.wikipedia.org/wiki/James_Ax "James Ax") (1968), "The elementary theory of finite fields", *Ann. of Math.*, 2, **88** (2): 239–271, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/1970573](https://doi.org/10.2307%2F1970573), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [1970573](https://www.jstor.org/stable/1970573)
- [Baez, John C.](https://en.wikipedia.org/wiki/John_C._Baez "John C. Baez") (2002), "The octonions", *[Bulletin of the American Mathematical Society](https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society "Bulletin of the American Mathematical Society")*, **39** (2): 145–205, [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0105155](https://arxiv.org/abs/math/0105155), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/S0273-0979-01-00934-X](https://doi.org/10.1090%2FS0273-0979-01-00934-X), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [586512](https://api.semanticscholar.org/CorpusID:586512)
- Banaschewski, Bernhard (1992), "Algebraic closure without choice.", *Z. Math. Logik Grundlagen Math.*, **38** (4): 383–385, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1002/malq.19920380136](https://doi.org/10.1002%2Fmalq.19920380136), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0739.03027](https://zbmath.org/?format=complete&q=an:0739.03027)
- Beachy, John. A; Blair, William D. (2006), *Abstract Algebra* (3 ed.), Waveland Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [1-57766-443-4](https://en.wikipedia.org/wiki/Special:BookSources/1-57766-443-4 "Special:BookSources/1-57766-443-4")
- Blyth, T. S.; [Robertson, E. F.](https://en.wikipedia.org/wiki/Edmund_F._Robertson "Edmund F. Robertson") (1985), *Groups, rings and fields: Algebra through practice*, [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press "Cambridge University Press"). See especially Book 3 ([ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-27288-2](https://en.wikipedia.org/wiki/Special:BookSources/0-521-27288-2 "Special:BookSources/0-521-27288-2")) and Book 6 ([ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-27291-2](https://en.wikipedia.org/wiki/Special:BookSources/0-521-27291-2 "Special:BookSources/0-521-27291-2")).
- Borceux, Francis; Janelidze, George (2001), *Galois theories*, Cambridge University Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-80309-8](https://en.wikipedia.org/wiki/Special:BookSources/0-521-80309-8 "Special:BookSources/0-521-80309-8"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0978.12004](https://zbmath.org/?format=complete&q=an:0978.12004)
- [Bourbaki, Nicolas](https://en.wikipedia.org/wiki/Nicolas_Bourbaki "Nicolas Bourbaki") (1994), *Elements of the history of mathematics*, Springer, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-642-61693-8](https://doi.org/10.1007%2F978-3-642-61693-8), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [3-540-19376-6](https://en.wikipedia.org/wiki/Special:BookSources/3-540-19376-6 "Special:BookSources/3-540-19376-6"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1290116](https://mathscinet.ams.org/mathscinet-getitem?mr=1290116)
- [Bourbaki, Nicolas](https://en.wikipedia.org/wiki/Nicolas_Bourbaki "Nicolas Bourbaki") (1988), *Algebra II. Chapters 4–7*, Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-19375-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-19375-8 "Special:BookSources/0-387-19375-8")
- [Cassels, J. W. S.](https://en.wikipedia.org/wiki/J._W._S._Cassels "J. W. S. Cassels") (1986), *Local fields*, London Mathematical Society Student Texts, vol. 3, Cambridge University Press, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1017/CBO9781139171885](https://doi.org/10.1017%2FCBO9781139171885), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-30484-9](https://en.wikipedia.org/wiki/Special:BookSources/0-521-30484-9 "Special:BookSources/0-521-30484-9"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0861410](https://mathscinet.ams.org/mathscinet-getitem?mr=0861410)
- Clark, A. (1984), [*Elements of Abstract Algebra*](https://books.google.com/books?id=bj1kOY8gOfcC), Dover Books on Mathematics Series, Dover, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-486-64725-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-64725-8 "Special:BookSources/978-0-486-64725-8")
- [Conway, John Horton](https://en.wikipedia.org/wiki/John_Horton_Conway "John Horton Conway") (1976), [*On Numbers and Games*](https://en.wikipedia.org/wiki/On_Numbers_and_Games "On Numbers and Games"), [Academic Press](https://en.wikipedia.org/wiki/Academic_Press "Academic Press")
- [Corry, Leo](https://en.wikipedia.org/wiki/Leo_Corry "Leo Corry") (2004), *Modern algebra and the rise of mathematical structures* (2nd ed.), Birkhäuser, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [3-7643-7002-5](https://en.wikipedia.org/wiki/Special:BookSources/3-7643-7002-5 "Special:BookSources/3-7643-7002-5"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [1044.01008](https://zbmath.org/?format=complete&q=an:1044.01008)
- [Dirichlet, Peter Gustav Lejeune](https://en.wikipedia.org/wiki/Peter_Gustav_Lejeune_Dirichlet "Peter Gustav Lejeune Dirichlet") (1871), [Dedekind, Richard](https://en.wikipedia.org/wiki/Richard_Dedekind "Richard Dedekind") (ed.), [*Vorlesungen über Zahlentheorie (Lectures on Number Theory)*](https://books.google.com/books?id=SRJTAAAAcAAJ&pg=PA424) (in German), vol. 1 (2nd ed.), Braunschweig, Germany: Friedrich Vieweg und Sohn
- [Eisenbud, David](https://en.wikipedia.org/wiki/David_Eisenbud "David Eisenbud") (1995), *Commutative algebra with a view toward algebraic geometry*, [Graduate Texts in Mathematics](https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics"), vol. 150, New York: [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag"), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4612-5350-1](https://doi.org/10.1007%2F978-1-4612-5350-1), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-94268-8](https://en.wikipedia.org/wiki/Special:BookSources/0-387-94268-8 "Special:BookSources/0-387-94268-8"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1322960](https://mathscinet.ams.org/mathscinet-getitem?mr=1322960)
- Escofier, J. P. (2012), *Galois Theory*, Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4613-0191-2](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4613-0191-2 "Special:BookSources/978-1-4613-0191-2")
- Fraleigh, John B. (1976), *A First Course In Abstract Algebra* (2nd ed.), Reading: [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley "Addison-Wesley"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-201-01984-1](https://en.wikipedia.org/wiki/Special:BookSources/0-201-01984-1 "Special:BookSources/0-201-01984-1")
- [Fricke, Robert](https://en.wikipedia.org/wiki/Robert_Fricke "Robert Fricke"); [Weber, Heinrich Martin](https://en.wikipedia.org/wiki/Heinrich_Martin_Weber "Heinrich Martin Weber") (1924), [*Lehrbuch der Algebra*](http://resolver.sub.uni-goettingen.de/purl?PPN234788267) (in German), Vieweg, [JFM](https://en.wikipedia.org/wiki/JFM_\(identifier\) "JFM (identifier)") [50.0042.03](https://zbmath.org/?format=complete&q=an:50.0042.03)
- [Gouvêa, Fernando Q.](https://en.wikipedia.org/wiki/Fernando_Q._Gouv%C3%AAa "Fernando Q. Gouvêa") (1997), p *\-adic numbers*, Universitext (2nd ed.), Springer
- [Gouvêa, Fernando Q.](https://en.wikipedia.org/wiki/Fernando_Q._Gouv%C3%AAa "Fernando Q. Gouvêa") (2012), *A Guide to Groups, Rings, and Fields*, Mathematical Association of America, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-88385-355-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-88385-355-9 "Special:BookSources/978-0-88385-355-9")
- ["Field"](https://www.encyclopediaofmath.org/index.php?title=Field), *[Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics "Encyclopedia of Mathematics")*, [EMS Press](https://en.wikipedia.org/wiki/European_Mathematical_Society "European Mathematical Society"), 2001 \[1994\]
- [Hensel, Kurt](https://en.wikipedia.org/wiki/Kurt_Hensel "Kurt Hensel") (1904), ["Über eine neue Begründung der Theorie der algebraischen Zahlen"](https://eudml.org/doc/149187), *Journal für die Reine und Angewandte Mathematik* (in German), **128**: 1–32, [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0075-4102](https://search.worldcat.org/issn/0075-4102), [JFM](https://en.wikipedia.org/wiki/JFM_\(identifier\) "JFM (identifier)") [35.0227.01](https://zbmath.org/?format=complete&q=an:35.0227.01)
- [Jacobson, Nathan](https://en.wikipedia.org/wiki/Nathan_Jacobson "Nathan Jacobson") (2009), *Basic algebra*, vol. 1 (2nd ed.), Dover, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-486-47189-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-47189-1 "Special:BookSources/978-0-486-47189-1")
- Jannsen, Uwe; Wingberg, Kay (1982), ["Die Struktur der absoluten Galoisgruppe 𝔭-adischer Zahlkörper. \[The structure of the absolute Galois group of 𝔭-adic number fields\]"](http://epub.uni-regensburg.de/26689/), *Invent. Math.*, **70** (1): 71–98, [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[1982InMat..70...71J](https://ui.adsabs.harvard.edu/abs/1982InMat..70...71J), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/bf01393199](https://doi.org/10.1007%2Fbf01393199), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0679774](https://mathscinet.ams.org/mathscinet-getitem?mr=0679774), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [119378923](https://api.semanticscholar.org/CorpusID:119378923)
- [Kleiner, Israel](https://en.wikipedia.org/wiki/Israel_Kleiner_\(mathematician\) "Israel Kleiner (mathematician)") (2007), Kleiner, Israel (ed.), *A history of abstract algebra*, Birkhäuser, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-0-8176-4685-1](https://doi.org/10.1007%2F978-0-8176-4685-1), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8176-4684-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8176-4684-4 "Special:BookSources/978-0-8176-4684-4"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [2347309](https://mathscinet.ams.org/mathscinet-getitem?mr=2347309)
- Kiernan, B. Melvin (1971), "The development of Galois theory from Lagrange to Artin", *Archive for History of Exact Sciences*, **8** (1–2): 40–154, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BF00327219](https://doi.org/10.1007%2FBF00327219), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1554154](https://mathscinet.ams.org/mathscinet-getitem?mr=1554154), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [121442989](https://api.semanticscholar.org/CorpusID:121442989)
- Kuhlmann, Salma (2000), *Ordered exponential fields*, Fields Institute Monographs, vol. 12, American Mathematical Society, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-8218-0943-1](https://en.wikipedia.org/wiki/Special:BookSources/0-8218-0943-1 "Special:BookSources/0-8218-0943-1"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1760173](https://mathscinet.ams.org/mathscinet-getitem?mr=1760173)
- [Lang, Serge](https://en.wikipedia.org/wiki/Serge_Lang "Serge Lang") (2002), *Algebra*, Graduate Texts in Mathematics, vol. 211 (3rd ed.), Springer, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4613-0041-0](https://doi.org/10.1007%2F978-1-4613-0041-0), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-95385-X](https://en.wikipedia.org/wiki/Special:BookSources/0-387-95385-X "Special:BookSources/0-387-95385-X")
- Lidl, Rudolf; [Niederreiter, Harald](https://en.wikipedia.org/wiki/Harald_Niederreiter "Harald Niederreiter") (2008), *Finite fields* (2nd ed.), Cambridge University Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-06567-2](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-06567-2 "Special:BookSources/978-0-521-06567-2"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [1139.11053](https://zbmath.org/?format=complete&q=an:1139.11053)
- Lorenz, Falko (2008), *Algebra, Volume II: Fields with Structures, Algebras and Advanced Topics*, Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-72487-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-72487-4 "Special:BookSources/978-0-387-72487-4")
- Marker, David; Messmer, Margit; Pillay, Anand (2006), [*Model theory of fields*](https://archive.org/details/modeltheoryoffie0000mark), Lecture Notes in Logic, vol. 5 (2nd ed.), Association for Symbolic Logic, [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.36.8448](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.36.8448), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-56881-282-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-56881-282-3 "Special:BookSources/978-1-56881-282-3"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [2215060](https://mathscinet.ams.org/mathscinet-getitem?mr=2215060)
- McCoy, Neal H. (1968), *Introduction To Modern Algebra, Revised Edition*, Boston: [Allyn and Bacon](https://en.wikipedia.org/wiki/Allyn_and_Bacon "Allyn and Bacon"), [LCCN](https://en.wikipedia.org/wiki/LCCN_\(identifier\) "LCCN (identifier)") [68015225](https://lccn.loc.gov/68015225)
- Mines, Ray; Richman, Fred; Ruitenburg, Wim (1988), *A course in constructive algebra*, Universitext, Springer, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4419-8640-5](https://doi.org/10.1007%2F978-1-4419-8640-5), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-96640-4](https://en.wikipedia.org/wiki/Special:BookSources/0-387-96640-4 "Special:BookSources/0-387-96640-4"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0919949](https://mathscinet.ams.org/mathscinet-getitem?mr=0919949)
- [Moore, E. Hastings](https://en.wikipedia.org/wiki/E._H._Moore "E. H. Moore") (1893), "A doubly-infinite system of simple groups", *[Bulletin of the American Mathematical Society](https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society "Bulletin of the American Mathematical Society")*, **3** (3): 73–78, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/S0002-9904-1893-00178-X](https://doi.org/10.1090%2FS0002-9904-1893-00178-X), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1557275](https://mathscinet.ams.org/mathscinet-getitem?mr=1557275)
- Prestel, Alexander (1984), *Lectures on Formally Real Fields*, Lecture Notes in Mathematics, vol. 1093, Springer, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BFb0101548](https://doi.org/10.1007%2FBFb0101548), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [3-540-13885-4](https://en.wikipedia.org/wiki/Special:BookSources/3-540-13885-4 "Special:BookSources/3-540-13885-4"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0769847](https://mathscinet.ams.org/mathscinet-getitem?mr=0769847)
- [Ribenboim, Paulo](https://en.wikipedia.org/wiki/Paulo_Ribenboim "Paulo Ribenboim") (1999), *The theory of classical valuations*, Springer Monographs in Mathematics, Springer, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4612-0551-7](https://doi.org/10.1007%2F978-1-4612-0551-7), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-98525-5](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98525-5 "Special:BookSources/0-387-98525-5"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1677964](https://mathscinet.ams.org/mathscinet-getitem?mr=1677964)
- [Scholze, Peter](https://en.wikipedia.org/wiki/Peter_Scholze "Peter Scholze") (2014), ["Perfectoid spaces and their Applications"](http://www.math.uni-bonn.de/people/scholze/ICM.pdf) (PDF), [*Proceedings of the International Congress of Mathematicians 2014*](http://www.icm2014.org/en/vod/proceedings.html), Kyung Moon SA, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-89-6105-804-9](https://en.wikipedia.org/wiki/Special:BookSources/978-89-6105-804-9 "Special:BookSources/978-89-6105-804-9")
- Schoutens, Hans (2002), *The Use of Ultraproducts in Commutative Algebra*, Lecture Notes in Mathematics, vol. 1999, Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-642-13367-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-13367-1 "Special:BookSources/978-3-642-13367-1")
- [Serre, Jean-Pierre](https://en.wikipedia.org/wiki/Jean-Pierre_Serre "Jean-Pierre Serre") (1996) \[1978\], [*A course in arithmetic. Translation of* Cours d'arithmetique](https://archive.org/details/courseinarithmet00serr), Graduate Text in Mathematics, vol. 7 (2nd ed.), Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780387900407](https://en.wikipedia.org/wiki/Special:BookSources/9780387900407 "Special:BookSources/9780387900407"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0432.10001](https://zbmath.org/?format=complete&q=an:0432.10001)
- [Serre, Jean-Pierre](https://en.wikipedia.org/wiki/Jean-Pierre_Serre "Jean-Pierre Serre") (1979), *Local fields*, Graduate Texts in Mathematics, vol. 67, Springer, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-90424-7](https://en.wikipedia.org/wiki/Special:BookSources/0-387-90424-7 "Special:BookSources/0-387-90424-7"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0554237](https://mathscinet.ams.org/mathscinet-getitem?mr=0554237)
- [Serre, Jean-Pierre](https://en.wikipedia.org/wiki/Jean-Pierre_Serre "Jean-Pierre Serre") (1992), *Topics in Galois theory*, Jones and Bartlett Publishers, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-86720-210-6](https://en.wikipedia.org/wiki/Special:BookSources/0-86720-210-6 "Special:BookSources/0-86720-210-6"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0746.12001](https://zbmath.org/?format=complete&q=an:0746.12001)
- [Serre, Jean-Pierre](https://en.wikipedia.org/wiki/Jean-Pierre_Serre "Jean-Pierre Serre") (2002), *Galois cohomology*, Springer Monographs in Mathematics, Translated from the French by [Patrick Ion](https://en.wikipedia.org/wiki/Patrick_Ion "Patrick Ion"), Berlin, New York: [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-42192-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-42192-4 "Special:BookSources/978-3-540-42192-4"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1867431](https://mathscinet.ams.org/mathscinet-getitem?mr=1867431), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [1004.12003](https://zbmath.org/?format=complete&q=an:1004.12003)
- Sharpe, David (1987), [*Rings and factorization*](https://archive.org/details/ringsfactorizati0000shar), Cambridge University Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-521-33718-6](https://en.wikipedia.org/wiki/Special:BookSources/0-521-33718-6 "Special:BookSources/0-521-33718-6"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0674.13008](https://zbmath.org/?format=complete&q=an:0674.13008)
- [Steinitz, Ernst](https://en.wikipedia.org/wiki/Ernst_Steinitz "Ernst Steinitz") (1910), ["Algebraische Theorie der Körper"](http://resolver.sub.uni-goettingen.de/purl?GDZPPN002167042) \[Algebraic Theory of Fields\], *[Journal für die reine und angewandte Mathematik](https://en.wikipedia.org/wiki/Journal_f%C3%BCr_die_reine_und_angewandte_Mathematik "Journal für die reine und angewandte Mathematik")*, **1910** (137): 167–309, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1515/crll.1910.137.167](https://doi.org/10.1515%2Fcrll.1910.137.167), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0075-4102](https://search.worldcat.org/issn/0075-4102), [JFM](https://en.wikipedia.org/wiki/JFM_\(identifier\) "JFM (identifier)") [41.0445.03](https://zbmath.org/?format=complete&q=an:41.0445.03), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [120807300](https://api.semanticscholar.org/CorpusID:120807300)
- [Tits, Jacques](https://en.wikipedia.org/wiki/Jacques_Tits "Jacques Tits") (1957), "Sur les analogues algébriques des groupes semi-simples complexes", *Colloque d'algèbre supérieure, tenu à Bruxelles du 19 au 22 décembre 1956, Centre Belge de Recherches Mathématiques Établissements Ceuterick, Louvain*, Paris: Librairie Gauthier-Villars, pp. 261–289
- van der Put, M.; Singer, M. F. (2003), [*Galois Theory of Linear Differential Equations*](http://www4.ncsu.edu/~singer/papers/dbook2.ps), Grundlehren der mathematischen Wissenschaften, vol. 328, Springer
- [von Staudt, Karl Georg Christian](https://en.wikipedia.org/wiki/Karl_Georg_Christian_von_Staudt "Karl Georg Christian von Staudt") (1857), [*Beiträge zur Geometrie der Lage (Contributions to the Geometry of Position)*](https://books.google.com/books?id=XwEHAAAAcAAJ&pg=PA127), vol. 2, Nürnberg (Germany): Bauer and Raspe
- Wallace, D. A. R. (1998), *Groups, Rings, and Fields*, SUMS, vol. 151, Springer
- Warner, Seth (1989), *Topological fields*, North-Holland, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-444-87429-1](https://en.wikipedia.org/wiki/Special:BookSources/0-444-87429-1 "Special:BookSources/0-444-87429-1"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0683.12014](https://zbmath.org/?format=complete&q=an:0683.12014)
- [Washington, Lawrence C.](https://en.wikipedia.org/wiki/Lawrence_C._Washington "Lawrence C. Washington") (1997), *Introduction to Cyclotomic Fields*, Graduate Texts in Mathematics, vol. 83 (2nd ed.), Springer-Verlag, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-1-4612-1934-7](https://doi.org/10.1007%2F978-1-4612-1934-7), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-94762-0](https://en.wikipedia.org/wiki/Special:BookSources/0-387-94762-0 "Special:BookSources/0-387-94762-0"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1421575](https://mathscinet.ams.org/mathscinet-getitem?mr=1421575)
- [Weber, Heinrich](https://en.wikipedia.org/wiki/Heinrich_Martin_Weber "Heinrich Martin Weber") (1893), ["Die allgemeinen Grundlagen der Galois'schen Gleichungstheorie"](https://eudml.org/doc/157689), *Mathematische Annalen* (in German), **43** (4): 521–549, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/BF01446451](https://doi.org/10.1007%2FBF01446451), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0025-5831](https://search.worldcat.org/issn/0025-5831), [JFM](https://en.wikipedia.org/wiki/JFM_\(identifier\) "JFM (identifier)") [25.0137.01](https://zbmath.org/?format=complete&q=an:25.0137.01), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [120528969](https://api.semanticscholar.org/CorpusID:120528969)

## External links

[^1]: The a priori twofold use of the symbol "−" for denoting one part of a constant and for the additive inverses is justified by this latter condition.

[^2]: Equivalently, a field is an [algebraic structure](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure") ⟨ *F*, +, ⋅, −, <sup>−1</sup>, 0, 1⟩ of type ⟨2, 2, 1, 1, 0, 0⟩, such that 0 <sup>−1</sup> is not defined, ⟨ *F*, +, −, 0⟩ and ${\displaystyle \left\langle F\smallsetminus \{0\},\cdot ,{}^{-1}\right\rangle }$ are abelian groups, and ⋅ is distributive over +.[^17]

[^3]: There are other reasons for this convention, which are generally more technical.

[^4]: Further examples include the maximal [unramified extension](https://en.wikipedia.org/wiki/Unramified_extension "Unramified extension") or the maximal [abelian extension](https://en.wikipedia.org/wiki/Abelian_extension "Abelian extension") within F.

[^5]: Some authors also consider the fields **R** and **C** to be local fields. On the other hand, these two fields, also called Archimedean local fields, share little similarity with the local fields considered here, to a point that [Cassels (1986](#CITEREFCassels1986), p. vi) calls them "completely anomalous".

[^6]: Both **C** and ulim <sub><i>p</i></sub> **F** <sub><i>p</i></sub> are algebraically closed by Łoś's theorem. For the same reason, they both have characteristic zero. Finally, they are both uncountable, so that they are isomorphic.

[^7]: More precisely, there is an [equivalence of categories](https://en.wikipedia.org/wiki/Equivalence_of_categories "Equivalence of categories") between smooth proper algebraic curves over an algebraically closed field F and finite field extensions of *F* (*T*).

[^8]: [Beachy & Blair (2006)](#CITEREFBeachyBlair2006), Definition 4.1.1, p. 181

[^9]: [Fraleigh (1976)](#CITEREFFraleigh1976), p. 10

[^10]: [McCoy (1968)](#CITEREFMcCoy1968), p. 16

[^11]: [Clark (1984)](#CITEREFClark1984), Chapter 3

[^12]: [Mines, Richman & Ruitenburg (1988)](#CITEREFMinesRichmanRuitenburg1988), §II.2. See also [Heyting field](https://en.wikipedia.org/wiki/Heyting_field "Heyting field").

[^13]: [Beachy & Blair (2006)](#CITEREFBeachyBlair2006), p. 120, Ch. 3

[^14]: [Artin (1991)](#CITEREFArtin1991), Chapter 13.4

[^15]: [Lidl & Niederreiter (2008)](#CITEREFLidlNiederreiter2008), Example 1.62

[^16]: [Beachy & Blair (2006)](#CITEREFBeachyBlair2006), p. 120, Ch. 3

[^17]: [Wallace (1998)](#CITEREFWallace1998), Th. 2

[^18]: [Adamson (2007)](#CITEREFAdamson2007), §I.2, p. 10

[^19]: [Escofier (2012)](#CITEREFEscofier2012), 14.4.2

[^20]: [Adamson (2007)](#CITEREFAdamson2007), §I.3

[^21]: [Adamson (2007)](#CITEREFAdamson2007), p. 17, Theorem 3.2

[^22]: [Lidl & Niederreiter (2008)](#CITEREFLidlNiederreiter2008), Lemma 2.1, Theorem 2.2

[^23]: [Lidl & Niederreiter (2008)](#CITEREFLidlNiederreiter2008), Theorem 1.2.5

[^24]: [Kleiner (2007)](#CITEREFKleiner2007), p. 63

[^25]: [Kiernan (1971)](#CITEREFKiernan1971), p. 50

[^26]: [Bourbaki (1994)](#CITEREFBourbaki1994), pp. 75–76

[^27]: [Corry (2004)](#CITEREFCorry2004), p. 24

[^28]: [" *Earliest Known Uses of Some of the Words of Mathematics (F)* "](http://jeff560.tripod.com/f.html).

[^29]: [Dirichlet (1871)](#CITEREFDirichlet1871), p. 42, translation by [Kleiner (2007)](#CITEREFKleiner2007), p. 66

[^30]: [Bourbaki (1994)](#CITEREFBourbaki1994), p. 81

[^31]: [Corry (2004)](#CITEREFCorry2004), p. 33. See also [Fricke & Weber (1924)](#CITEREFFrickeWeber1924).

[^32]: [Bourbaki (1994)](#CITEREFBourbaki1994), p. 92

[^33]: [Lang (2002)](#CITEREFLang2002), §II.1

[^34]: [Artin (1991)](#CITEREFArtin1991), §10.6

[^35]: [Eisenbud (1995)](#CITEREFEisenbud1995), p. 60

[^36]: [Jacobson (2009)](#CITEREFJacobson2009), p. 213

[^37]: [Artin (1991)](#CITEREFArtin1991), Theorem 13.3.4

[^38]: [Artin (1991)](#CITEREFArtin1991), Corollary 13.3.6

[^39]: [Bourbaki (1988)](#CITEREFBourbaki1988), Chapter V, §14, No. 2, Theorem 1

[^40]: [Artin (1991)](#CITEREFArtin1991), §13.9

[^41]: [Banaschewski (1992)](#CITEREFBanaschewski1992). [Mathoverflow post](https://mathoverflow.net/questions/46566/is-the-statement-that-every-field-has-an-algebraic-closure-known-to-be-equivalent)

[^42]: [Ribenboim (1999)](#CITEREFRibenboim1999), p. 186, §7.1

[^43]: [Bourbaki (1988)](#CITEREFBourbaki1988), Chapter VI, §2.3, Corollary 1

[^44]: [Lorenz (2008)](#CITEREFLorenz2008), §22, Theorem 1

[^45]: [Prestel (1984)](#CITEREFPrestel1984), Proposition 1.22

[^46]: [Prestel (1984)](#CITEREFPrestel1984), Theorem 1.23

[^47]: [Warner (1989)](#CITEREFWarner1989), Chapter 14

[^48]: [Gouvêa (1997)](#CITEREFGouvêa1997), §5.7

[^49]: [Serre (1979)](#CITEREFSerre1979)

[^50]: [Scholze (2014)](#CITEREFScholze2014)

[^51]: [van der Put & Singer (2003)](#CITEREFvan_der_PutSinger2003), §1

[^52]: [Lang (2002)](#CITEREFLang2002), Theorem V.4.6

[^53]: [Lang (2002)](#CITEREFLang2002), §VI.1

[^54]: [Lang (2002)](#CITEREFLang2002), Example VI.2.6

[^55]: [Borceux & Janelidze (2001)](#CITEREFBorceuxJanelidze2001). See also [Étale fundamental group](https://en.wikipedia.org/wiki/%C3%89tale_fundamental_group "Étale fundamental group").

[^56]: [Gouvêa (2012)](#CITEREFGouvêa2012), Theorem 6.4.8

[^57]: [Marker, Messmer & Pillay (2006)](#CITEREFMarkerMessmerPillay2006), Corollary 1.2

[^58]: [Schoutens (2002)](#CITEREFSchoutens2002), §2

[^59]: [Kuhlmann (2000)](#CITEREFKuhlmann2000)

[^60]: [Jannsen & Wingberg (1982)](#CITEREFJannsenWingberg1982)

[^61]: [Serre (2002)](#CITEREFSerre2002)

[^62]: [Artin (1991)](#CITEREFArtin1991), §3.3

[^63]: [Eisenbud (1995)](#CITEREFEisenbud1995), §13, Theorem A

[^64]: [Washington (1997)](#CITEREFWashington1997)

[^65]: [Serre (1996)](#CITEREFSerre1996), Chapter IV

[^66]: [Serre (1992)](#CITEREFSerre1992)

[^67]: [Tits (1957)](#CITEREFTits1957)

[^68]: [Conway (1976)](#CITEREFConway1976)

[^69]: [Baez (2002)](#CITEREFBaez2002)