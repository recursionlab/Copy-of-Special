---
title: "Cayley–Dickson construction - Wikipedia"
source: "https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2003-01-28
created: 2026-02-03
description:
tags:
  - "clippings"
---
[

![Wiki Loves Folklore Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/Wiki_Loves_Folklore_Logo.svg)

Wiki Loves Folklore Logo

Wiki Loves Folklore Photograph your local culture, help Wikipedia and win!

\[Help with translations!\]

](https://commons.wikimedia.org/wiki/Special:MyLanguage/Commons:Wiki_Loves_Folklore_2026)

In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **Cayley–Dickson construction**, sometimes also known as the **Cayley–Dickson process** or the **Cayley–Dickson procedure** produces a sequence of [algebras](https://en.wikipedia.org/wiki/Algebra_over_a_field "Algebra over a field") over the [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)") of [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number"), each with twice the [dimension](https://en.wikipedia.org/wiki/Dimension_of_a_vector_space "Dimension of a vector space") of the previous one. It is named after [Arthur Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley "Arthur Cayley") and [Leonard Eugene Dickson](https://en.wikipedia.org/wiki/Leonard_Eugene_Dickson "Leonard Eugene Dickson"). The algebras produced by this process are known as **Cayley–Dickson algebras**, for example [complex numbers](https://en.wikipedia.org/wiki/Complex_number "Complex number"), [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion"), and [octonions](https://en.wikipedia.org/wiki/Octonion "Octonion"). These examples are useful [composition algebras](https://en.wikipedia.org/wiki/Composition_algebra "Composition algebra") frequently applied in [mathematical physics](https://en.wikipedia.org/wiki/Mathematical_physics "Mathematical physics").

The Cayley–Dickson construction defines a new algebra as a [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product "Cartesian product") of an algebra with itself, with [multiplication](https://en.wikipedia.org/wiki/Multiplication "Multiplication") defined in a specific way (different from the [componentwise](https://en.wikipedia.org/wiki/Componentwise_operation "Componentwise operation") multiplication) and an [involution](https://en.wikipedia.org/wiki/Involution_\(mathematics\) "Involution (mathematics)") known as *conjugation*. The product of an element and its [conjugate](https://en.wikipedia.org/wiki/Complex_conjugate "Complex conjugate") (or sometimes the square root of this product) is called the [norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)").

The symmetries of the real field disappear as the Cayley–Dickson construction is repeatedly applied: first losing [order](https://en.wikipedia.org/wiki/Ordered_field "Ordered field"), then [commutativity](https://en.wikipedia.org/wiki/Commutativity "Commutativity") of multiplication, [associativity](https://en.wikipedia.org/wiki/Associativity "Associativity") of multiplication, and finally [alternativity](https://en.wikipedia.org/wiki/Alternativity "Alternativity").

More generally, the Cayley–Dickson construction takes any algebra with involution to another algebra with involution of twice the dimension.[^1]<sup><span title="Page / location: 45">: 45 </span></sup> 

[Hurwitz's theorem](https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_\(composition_algebras\) "Hurwitz's theorem (composition algebras)") states that the reals, complex numbers, quaternions, and octonions are the only finite-dimensional [normed](https://en.wikipedia.org/wiki/Normed_algebra "Normed algebra") [division algebras](https://en.wikipedia.org/wiki/Division_algebra "Division algebra") over the real numbers, while the [Frobenius theorem](https://en.wikipedia.org/wiki/Frobenius_theorem_\(real_division_algebras\) "Frobenius theorem (real division algebras)") states that the first three are the only finite-dimensional associative division algebras over the real numbers.

## Synopsis

<table><caption>Cayley–Dickson algebras properties</caption><tbody><tr><th rowspan="2"><a href="https://en.wikipedia.org/wiki/Algebra_over_a_field">Algebra</a></th><th rowspan="2"><a href="https://en.wikipedia.org/wiki/Dimension_(vector_space)">Dimension</a></th><th rowspan="2"><a href="https://en.wikipedia.org/wiki/Ordered_field">Ordered</a></th><th colspan="4"><a href="https://en.wikipedia.org/wiki/Multiplication">Multiplication</a> properties</th><th rowspan="2">Nontriv.<br><a href="https://en.wikipedia.org/wiki/Zero_divisor">zero<br>divisors</a></th></tr><tr><th><a href="https://en.wikipedia.org/wiki/Commutative">Commutative</a></th><th><a href="https://en.wikipedia.org/wiki/Associative">Associative</a></th><th><a href="https://en.wikipedia.org/wiki/Alternative_algebra">Alternative</a></th><th><a href="https://en.wikipedia.org/wiki/Power_associativity">Power-assoc.</a></th></tr><tr><th><a href="https://en.wikipedia.org/wiki/Real_number">Real numbers</a></th><td>1</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Complex_number">Complex num.</a></th><td>2</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Quaternion">Quaternions</a></th><td>4</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Octonion">Octonions</a></th><td>8</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Sedenion">Sedenions</a></th><td>16</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><th><a href="https://en.wikipedia.org/wiki/Trigintaduonion">Trigintaduonions</a><br>and higher</th><td>≥ 32</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr></tbody></table>

The **Cayley–Dickson construction** is due to [Leonard Dickson](https://en.wikipedia.org/wiki/Leonard_Dickson "Leonard Dickson") in 1919 showing how the [octonions](https://en.wikipedia.org/wiki/Octonion "Octonion") can be constructed as a two-dimensional algebra over [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion"). In fact, starting with a field *F*, the construction yields a sequence of *F* -algebras of dimension 2 <sup><i>n</i></sup>. For *n* = 2 it is an associative algebra called a [quaternion algebra](https://en.wikipedia.org/wiki/Quaternion_algebra "Quaternion algebra"), and for *n* = 3 it is an [alternative algebra](https://en.wikipedia.org/wiki/Alternative_algebra "Alternative algebra") called an [octonion algebra](https://en.wikipedia.org/wiki/Octonion_algebra "Octonion algebra"). These instances *n* = 1, 2 and 3 produce [composition algebras](https://en.wikipedia.org/wiki/Composition_algebra "Composition algebra") as shown below.

The case *n* = 1 starts with elements (*a*, *b*) in *F* × *F* and defines the conjugate (*a*, *b*)\* to be (*a* \*, – *b*) where *a* \* = *a* in case *n* = 1, and subsequently determined by the formula. The essence of the *F* -algebra lies in the definition of the product of two elements (*a*, *b*) and (*c*, *d*):

${\displaystyle (a,b)\times (c,d)=(ac-d^{*}b,da+bc^{*}).}$

**Proposition 1:** For ${\displaystyle z=(a,b)}$ and ${\displaystyle w=(c,d),}$ the conjugate of the product is ${\displaystyle w^{*}z^{*}=(zw)^{*}.}$

proof: ${\displaystyle (c^{*},-d)(a^{*},-b)=(c^{*}a^{*}+b^{*}(-d),-bc^{*}-da)=(zw)^{*}.}$

**Proposition 2:** If the *F* -algebra is associative and ${\displaystyle N(z)=zz^{*}}$ ,then ${\displaystyle N(zw)=N(z)N(w).}$

proof: ${\displaystyle N(zw)=(ac-d^{*}b,da+bc^{*})(c^{*}a^{*}-b^{*}d,-da-bc^{*})=(aa^{*}+bb^{*})(cc^{*}+dd^{*})}$ + terms that cancel by the associative property.

Details of the construction of the classical real algebras are as follows:

The [complex numbers](https://en.wikipedia.org/wiki/Complex_numbers "Complex numbers") can be written as [ordered pairs](https://en.wikipedia.org/wiki/Ordered_pair "Ordered pair") (*a*, *b*) of [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") a and b, with the addition operator being component-wise and with multiplication defined by

${\displaystyle (a,b)(c,d)=(ac-bd,ad+bc).\,}$

A complex number whose second component is zero is associated with a real number: the complex number (*a*, 0) is associated with the real number a.

The [complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate "Complex conjugate") (*a*, *b*)\* of (*a*, *b*) is given by

${\displaystyle (a,b)^{*}=(a^{*},-b)=(a,-b)}$

since a is a real number and is its own conjugate.

The conjugate has the property that

${\displaystyle (a,b)^{*}(a,b)=(aa+bb,ab-ba)=\left(a^{2}+b^{2},0\right),\,}$

which is a non-negative real number. In this way, conjugation defines a *[norm](https://en.wikipedia.org/wiki/Norm_\(mathematics\) "Norm (mathematics)")*, making the complex numbers a [normed vector space](https://en.wikipedia.org/wiki/Normed_vector_space "Normed vector space") over the real numbers: the norm of a complex number  z is

${\displaystyle |z|=\left(z^{*}z\right)^{\frac {1}{2}}.\,}$

Furthermore, for any non-zero complex number z, conjugation gives a [multiplicative inverse](https://en.wikipedia.org/wiki/Inverse_element "Inverse element"),

${\displaystyle z^{-1}={\frac {z^{*}}{|z|^{2}}}.}$

As a complex number consists of two independent real numbers, they form a two-dimensional [vector space](https://en.wikipedia.org/wiki/Vector_space "Vector space") over the real numbers.

Besides being of higher dimension, the complex numbers can be said to lack one algebraic property of the real numbers: a real number is its own conjugate.

### Quaternions

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Cayley_Q8_multiplication_graph.svg/500px-Cayley_Q8_multiplication_graph.svg.png)

Cayley Q8 graph of quaternion multiplication showing cycles of multiplication of i (red), j (green) and k (blue). In the SVG file, hover over or click a path to highlight it.

The next step in the construction is to generalize the multiplication and conjugation operations.

Form ordered pairs (*a*, *b*) of complex numbers a and b, with multiplication defined by

${\displaystyle (a,b)(c,d)=(ac-d^{*}b,da+bc^{*}).\,}$

Slight variations on this formula are possible; the resulting constructions will yield structures identical up to the signs of bases.

The order of the factors seems odd now, but will be important in the next step.

Define the conjugate (*a*, *b*)\* of (*a*, *b*) by

${\displaystyle (a,b)^{*}=(a^{*},-b).\,}$

These operators are direct extensions of their complex analogs: if a and b are taken from the real subset of complex numbers, the appearance of the conjugate in the formulas has no effect, so the operators are the same as those for the complex numbers.

The product of a nonzero element with its conjugate is a non-negative real number:

${\displaystyle {\begin{aligned}(a,b)^{*}(a,b)&=(a^{*},-b)(a,b)\\&=(a^{*}a+b^{*}b,ba^{*}-ba^{*})\\&=\left(|a|^{2}+|b|^{2},0\right).\,\end{aligned}}}$

As before, the conjugate thus yields a norm and an inverse for any such ordered pair. So in the sense we explained above, these pairs constitute an algebra something like the real numbers. They are the [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion"), named by [Hamilton](https://en.wikipedia.org/wiki/William_Rowan_Hamilton "William Rowan Hamilton") in 1843.

As a quaternion consists of two independent complex numbers, they form a four-dimensional vector space over the real numbers.

The multiplication of quaternions is not quite like the multiplication of real numbers, though; it is not [commutative](https://en.wikipedia.org/wiki/Commutative "Commutative") – that is, if p and q are quaternions, it is not always true that *pq* = *qp*.

### Octonions

All the steps to create further algebras are the same from octonions onwards.

This time, form ordered pairs (*p*, *q*) of quaternions p and q, with multiplication and conjugation defined exactly as for the quaternions:

${\displaystyle (p,q)(r,s)=(pr-s^{*}q,sp+qr^{*}).\,}$

Note, however, that because the quaternions are not commutative, the order of the factors in the multiplication formula becomes important—if the last factor in the multiplication formula were *r* \* *q* rather than *qr* \*, the formula for multiplication of an element by its conjugate would not yield a real number.

For exactly the same reasons as before, the conjugation operator yields a norm and a multiplicative inverse of any nonzero element.

This algebra was discovered by [John T. Graves](https://en.wikipedia.org/wiki/John_T._Graves "John T. Graves") in 1843, and is called the [octonions](https://en.wikipedia.org/wiki/Octonion "Octonion") or the " [Cayley](https://en.wikipedia.org/wiki/Arthur_Cayley "Arthur Cayley") numbers".[^2]

As an octonion consists of two independent quaternions, they form an eight-dimensional vector space over the real numbers.

The multiplication of octonions is even stranger than that of quaternions; besides being non-commutative, it is not [associative](https://en.wikipedia.org/wiki/Associative "Associative") – that is, if p, q, and r are octonions, it is not always true that (*pq*) *r* = *p* (*qr*).

For the reason of this non-associativity, octonions have [no matrix representation](https://en.wikipedia.org/wiki/Octonion#Properties "Octonion").

### Sedenions

The algebra immediately following the octonions is called the [sedenions](https://en.wikipedia.org/wiki/Sedenion "Sedenion").[^3] It retains the algebraic property of [power associativity](https://en.wikipedia.org/wiki/Power_associativity "Power associativity"), meaning that if s is a sedenion, *s <sup>n</sup> s <sup>m</sup>* = *s* <sup><i>n</i> + <i>m</i></sup>, but loses the property of being an [alternative algebra](https://en.wikipedia.org/wiki/Alternative_algebra "Alternative algebra") and hence cannot be a [composition algebra](https://en.wikipedia.org/wiki/Composition_algebra "Composition algebra"). It is also at this point that the algebras formed by the Cayley-Dickson construction begin to have nontrivial [zero divisors](https://en.wikipedia.org/wiki/Zero_divisor "Zero divisor"), in that this and every further algebra created by the construction will have pairs of nonzero values (for example,⁠ ⁠ ${\displaystyle (e_{3}+e_{10})}$ ⁠ and ⁠ ⁠ ${\displaystyle (e_{6}-e_{15})}$ ⁠) which when multiplied give ${\displaystyle 0}$ ⁠.

### Trigintaduonions

The algebra immediately following the [sedenions](https://en.wikipedia.org/wiki/Sedenion "Sedenion") is the [trigintaduonions](https://en.wikipedia.org/wiki/Trigintaduonion "Trigintaduonion"),[^4] [^5] [^6] which form a 32- [dimensional](https://en.wikipedia.org/wiki/Dimension_of_a_vector_space "Dimension of a vector space") [algebra](https://en.wikipedia.org/wiki/Algebra_over_a_field "Algebra over a field") over the [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number") [^7] and can be represented by [blackboard bold](https://en.wikipedia.org/wiki/Blackboard_bold "Blackboard bold") ${\displaystyle \mathbb {T} }$ .[^8]

### Further algebras

The Cayley–Dickson construction can be carried on *[ad infinitum](https://en.wikipedia.org/wiki/Ad_infinitum "Ad infinitum")*, at each step producing a power-associative algebra whose dimension is double that of the algebra of the preceding step. These include the 64-dimensional sexagintaquatronions (or 64-nions), the 128-dimensional centumduodetrigintanions (or 128-nions), the 256-dimensional ducentiquinquagintasexions (or 256-nions), and *ad infinitum*.[^9] All the algebras generated in this way over a field are *quadratic*: that is, each element satisfies a quadratic equation with coefficients from the field.[^1]<sup><span title="Page / location: 50">: 50 </span></sup> 

In 1954, [R. D. Schafer](https://en.wikipedia.org/wiki/Richard_D._Schafer "Richard D. Schafer") proved that the algebras generated by the Cayley–Dickson process over a field F satisfy the [flexible identity](https://en.wikipedia.org/wiki/Flexible_identity "Flexible identity"). He also proved that any [derivation algebra](https://en.wikipedia.org/wiki/Derivation_algebra "Derivation algebra") of a Cayley–Dickson algebra is isomorphic to the derivation algebra of Cayley numbers, a 14-dimensional [Lie algebra](https://en.wikipedia.org/wiki/Lie_algebra "Lie algebra") over F.[^10]

The Cayley–Dickson construction, starting from the real numbers ${\displaystyle \mathbb {R} }$ , generates the [composition algebras](https://en.wikipedia.org/wiki/Composition_algebra "Composition algebra") ${\displaystyle \mathbb {C} }$ (the [complex numbers](https://en.wikipedia.org/wiki/Complex_number "Complex number")), ${\displaystyle \mathbb {H} }$ (the [quaternions](https://en.wikipedia.org/wiki/Quaternion "Quaternion")), and ${\displaystyle \mathbb {O} }$ (the [octonions](https://en.wikipedia.org/wiki/Octonion "Octonion")). There are also composition algebras whose norm is an [isotropic quadratic form](https://en.wikipedia.org/wiki/Isotropic_quadratic_form "Isotropic quadratic form"), which are obtained through a slight modification, by replacing the minus sign in the definition of the product of ordered pairs with a plus sign, as follows:
$$
{\displaystyle (a,b)(c,d)=(ac+d^{*}b,da+bc^{*}).}
$$

When this modified construction is applied to ${\displaystyle \mathbb {R} }$ , one obtains the [split-complex numbers](https://en.wikipedia.org/wiki/Split-complex_number "Split-complex number"), which are [ring-isomorphic](https://en.wikipedia.org/wiki/Ring_isomorphism "Ring isomorphism") to the [direct product](https://en.wikipedia.org/wiki/Direct_product "Direct product") ${\displaystyle \mathbb {R} \times \mathbb {R} ;}$ following that, one obtains the [split-quaternions](https://en.wikipedia.org/wiki/Split-quaternion "Split-quaternion"), an [associative algebra](https://en.wikipedia.org/wiki/Associative_algebra "Associative algebra") [isomorphic](https://en.wikipedia.org/wiki/Isomorphic "Isomorphic") to that of the 2 × 2 real [matrices](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)"); and the [split-octonions](https://en.wikipedia.org/wiki/Split-octonion "Split-octonion"), which are isomorphic to [Zorn(**R**)](https://en.wikipedia.org/wiki/Split-octonion#Zorn's_vector-matrix_algebra "Split-octonion"). Applying the original Cayley–Dickson construction to the split-complexes also results in the split-quaternions and then the split-octonions.[^11]

[Albert (1942](https://en.wikipedia.org/wiki/#CITEREFAlbert1942), p. 171) gave a slight generalization, defining the product and involution on *B* = *A* ⊕ *A* for A an [algebra with involution](https://en.wikipedia.org/wiki/*-algebra "*-algebra") (with (*xy*)\* = *y* \* *x* \*) to be

${\displaystyle {\begin{aligned}(p,q)(r,s)&=(pr-\gamma s^{*}q,sp+qr^{*})\,\\(p,q)^{*}&=(p^{*},-q)\,\end{aligned}}}$

for γ an additive map that commutes with \* and left and right multiplication by any element. (Over the reals all choices of γ are equivalent to −1, 0 or 1.) In this construction, A is an algebra with involution, meaning:

- A is an [abelian group](https://en.wikipedia.org/wiki/Abelian_group "Abelian group") under +
- A has a product that is left and right [distributive](https://en.wikipedia.org/wiki/Distributive_property "Distributive property") over +
- A has an involution \*, with (*x* \*)\* = *x*, (*x* + *y*)\* = *x* \* + *y* \*, (*xy*)\* = *y* \* *x* \*.

The algebra *B* = *A* ⊕ *A* produced by the Cayley–Dickson construction is also an algebra with involution.

B inherits properties from A unchanged as follows.

- If A has an identity 1 <sub><i>A</i></sub>, then B has an identity (1 <sub><i>A</i></sub>, 0).
- If A has the property that *x* + *x* \*, *xx* \* associate and commute with all elements, then so does B. This property implies that any element generates a commutative associative \*-algebra, so in particular the algebra is power associative.

Other properties of A only induce weaker properties of B:

- If A is commutative and has trivial involution, then B is commutative.
- If A is commutative and associative then B is associative.
- If A is associative and *x* + *x* \*, *xx* \* associate and commute with everything, then B is an [alternative algebra](https://en.wikipedia.org/wiki/Alternative_algebra "Alternative algebra").

## Notes

## References

- [Albert, A. A.](https://en.wikipedia.org/wiki/Abraham_Adrian_Albert "Abraham Adrian Albert") (1942), "Quadratic forms permitting composition", *[Annals of Mathematics](https://en.wikipedia.org/wiki/Annals_of_Mathematics "Annals of Mathematics")*, Second Series, **43** (1): 161– 177, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/1968887](https://doi.org/10.2307%2F1968887), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [1968887](https://www.jstor.org/stable/1968887), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0006140](https://mathscinet.ams.org/mathscinet-getitem?mr=0006140) (see p. 171)
- [Baez, John](https://en.wikipedia.org/wiki/John_Baez "John Baez") (2002), ["The Octonions"](http://math.ucr.edu/home/baez/octonions/octonions.html), *[Bulletin of the American Mathematical Society](https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society "Bulletin of the American Mathematical Society")*, **39** (2): 145– 205, [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0105155](https://arxiv.org/abs/math/0105155), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/S0273-0979-01-00934-X](https://doi.org/10.1090%2FS0273-0979-01-00934-X), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [586512](https://api.semanticscholar.org/CorpusID:586512). *(See " [Section 2.2, The Cayley–Dickson Construction](http://math.ucr.edu/home/baez/octonions/node5.html) ")*
- [Dickson, L. E.](https://en.wikipedia.org/wiki/Leonard_Dickson "Leonard Dickson") (1919), "On Quaternions and Their Generalization and the History of the Eight Square Theorem", *[Annals of Mathematics](https://en.wikipedia.org/wiki/Annals_of_Mathematics "Annals of Mathematics")*, Second Series, **20** (3), Annals of Mathematics: 155– 171, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/1967865](https://doi.org/10.2307%2F1967865), [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [1967865](https://www.jstor.org/stable/1967865)
- Biss, Daniel K.; Christensen, J. Daniel; Dugger, Daniel; Isaksen, Daniel C. (2007). "Large annihilators in Cayley–Dickson algebras II". *Boletin de la Sociedad Matematica Mexicana*. **3**: 269– 292. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0702075](https://arxiv.org/abs/math/0702075). [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2007math......2075B](https://ui.adsabs.harvard.edu/abs/2007math......2075B).
- [Hamilton, William Rowan](https://en.wikipedia.org/wiki/William_Rowan_Hamilton "William Rowan Hamilton") (1847), ["On Quaternions"](http://www.maths.tcd.ie/pub/HistMath/People/Hamilton/Quatern2/Quatern2.html), *Proceedings of the Royal Irish Academy*, **3**: 1– 16, [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1393-7197](https://search.worldcat.org/issn/1393-7197)
- Kantor, I. L.; Solodownikow, A. S. (1978), *Hyperkomplexe Zahlen*, Leipzig: B.G. Teubner (the following reference gives the English translation of this book)
- Kantor, I. L.; Solodovnikov, A. S. (1989), [*Hypercomplex numbers*](https://archive.org/details/hypercomplexnumb0000kant), Berlin, New York: [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-96980-0](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-96980-0 "Special:BookSources/978-0-387-96980-0"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [0996029](https://mathscinet.ams.org/mathscinet-getitem?mr=0996029)
- Roos, Guy (2008). "Exceptional symmetric domains §1: Cayley algebras". In Gilligan, Bruce; Roos, Guy (eds.). *Symmetries in Complex Analysis*. Contemporary Mathematics. Vol. 468. [American Mathematical Society](https://en.wikipedia.org/wiki/American_Mathematical_Society "American Mathematical Society"). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8218-4459-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-4459-5 "Special:BookSources/978-0-8218-4459-5").

## Further reading

- Daboul, Jamil; Delbourgo, Robert (1999). "Matrix representations of octonions and generalizations". *[Journal of Mathematical Physics](https://en.wikipedia.org/wiki/Journal_of_Mathematical_Physics "Journal of Mathematical Physics")*. **40** (8): 4134– 50. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[hep-th/9906065](https://arxiv.org/abs/hep-th/9906065). [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[1999JMP....40.4134D](https://ui.adsabs.harvard.edu/abs/1999JMP....40.4134D). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1063/1.532950](https://doi.org/10.1063%2F1.532950). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [16932871](https://api.semanticscholar.org/CorpusID:16932871).

[^1]: Schafer, Richard D. (1995) \[1966\], [*An introduction to non-associative algebras*](https://archive.org/details/introductiontono0000scha), [Dover Publications](https://en.wikipedia.org/wiki/Dover_Publications "Dover Publications"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-486-68813-5](https://en.wikipedia.org/wiki/Special:BookSources/0-486-68813-5 "Special:BookSources/0-486-68813-5"), [Zbl](https://en.wikipedia.org/wiki/Zbl_\(identifier\) "Zbl (identifier)") [0145.25601](https://zbmath.org/?format=complete&q=an:0145.25601)

[^2]: [Baez, John C.](https://en.wikipedia.org/wiki/John_Baez "John Baez") (2002). ["The Octonions"](http://math.ucr.edu/home/baez/octonions/). *Bulletin of the American Mathematical Society*. New Series. **39** (2): 145– 205. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[math/0105155](https://arxiv.org/abs/math/0105155). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/S0273-0979-01-00934-X](https://doi.org/10.1090%2FS0273-0979-01-00934-X). [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1886087](https://mathscinet.ams.org/mathscinet-getitem?mr=1886087). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [586512](https://api.semanticscholar.org/CorpusID:586512).

[^3]: Imaeda, K.; Imaeda, M. (2000). "Sedenions: algebra and analysis". *Applied Mathematics and Computation*. **115** (2): 77– 88. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/S0096-3003(99)00140-X](https://doi.org/10.1016%2FS0096-3003%2899%2900140-X). [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1786945](https://mathscinet.ams.org/mathscinet-getitem?mr=1786945).

[^4]: ["Trigintaduonion"](https://ece.uwaterloo.ca/~dwharder/Java/doc/ca/uwaterloo/alumni/dwharder/Numbers/Trigintaduonion.html). *University of Waterloo*. Retrieved 2024-10-08.

[^5]: Cawagas, Raoul E.; Carrascal, Alexander S.; Bautista, Lincoln A.; Maria, John P. Sta.; Urrutia, Jackie D.; Nobles, Bernadeth (2009). "The Subalgebra Structure of the Cayley-Dickson Algebra of Dimension 32 (trigintaduonion)". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[0907.2047v3](https://arxiv.org/abs/0907.2047v3) \[[math.RA](https://arxiv.org/archive/math.RA)\].

[^6]: Cariow, A.; Cariowa, G. (2014). ["An algorithm for multiplication of trigintaduonions"](https://www.infona.pl/resource/bwmeta1.element.baztech-0c72d8f6-14c2-4959-8640-58b568cfaa97). *Journal of Theoretical and Applied Computer Science*. **8** (1): 50– 75. [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [2299-2634](https://search.worldcat.org/issn/2299-2634). Retrieved 2024-10-10.

[^7]: Saini, Kavita; Raj, Kuldip (2021). "On generalization for Tribonacci Trigintaduonions". *Indian Journal of Pure and Applied Mathematics*. **52** (2). Springer Science and Business Media LLC: 420– 428. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/s13226-021-00067-y](https://doi.org/10.1007%2Fs13226-021-00067-y). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0019-5588](https://search.worldcat.org/issn/0019-5588).

[^8]: Cawagas, Raoul E.; Carrascal, Alexander S.; Bautista, Lincoln A.; Maria, John P. Sta.; Urrutia, Jackie D.; Nobles, Bernadeth (2009-07-12). "The Subalgebra Structure of the Cayley-Dickson Algebra of Dimension 32 (trigintaduonion)". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[0907.2047](https://arxiv.org/abs/0907.2047) \[[math.RA](https://arxiv.org/archive/math.RA)\].

[^9]: Cariow, Aleksandr (2015). "An unified approach for developing rationalized algorithms for hypercomplex number multiplication". *Przegląd Elektrotechniczny*. **1** (2). Wydawnictwo SIGMA-NOT: 38– 41. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.15199/48.2015.02.09](https://doi.org/10.15199%2F48.2015.02.09). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0033-2097](https://search.worldcat.org/issn/0033-2097).

[^10]: Richard D. Schafer (1954) "On the algebras formed by the Cayley–Dickson process", [American Journal of Mathematics](https://en.wikipedia.org/wiki/American_Journal_of_Mathematics "American Journal of Mathematics") 76: 435–46 [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2372583](https://doi.org/10.2307%2F2372583)

[^11]: Kevin McCrimmon (2004) *A Taste of Jordan Algebras*, pp 64, Universitext, Springer [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-95447-3](https://en.wikipedia.org/wiki/Special:BookSources/0-387-95447-3 "Special:BookSources/0-387-95447-3") [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [2014924](https://mathscinet.ams.org/mathscinet-getitem?mr=2014924)