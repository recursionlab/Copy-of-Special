---
title: "Reflexive relation"
source: "https://en.wikipedia.org/wiki/Reflexive_relation#Related_definitions"
author:
published:
created: 2026-04-10
description:
tags:
  - "clippings"
---
[Transitive](https://en.wikipedia.org/wiki/Transitive_relation "Transitive relation") [binary relations](https://en.wikipedia.org/wiki/Binary_relation "Binary relation")

In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), a [binary relation](https://en.wikipedia.org/wiki/Binary_relation "Binary relation") ${\displaystyle R}$ on a [set](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)") ${\displaystyle X}$ is **reflexive** if it relates every element of ${\displaystyle X}$ to itself.[^1] [^2]

An example of a reflexive relation is the relation " [is equal to](https://en.wikipedia.org/wiki/Equality_\(mathematics\) "Equality (mathematics)") " on the set of [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number"), since every real number is equal to itself. A reflexive relation is said to have the **reflexive property** or is said to possess **reflexivity**. Along with [symmetry](https://en.wikipedia.org/wiki/Symmetric_relation "Symmetric relation") and [transitivity](https://en.wikipedia.org/wiki/Transitive_relation "Transitive relation"), reflexivity is one of three properties defining [equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation "Equivalence relation").

## Etymology

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Arithmetices_principia_Properties_of_equality.png/250px-Arithmetices_principia_Properties_of_equality.png)

Giuseppe Peano's introduction of the reflexive property, along with symmetry and transitivity

The word *reflexive* is originally derived from the [Medieval Latin](https://en.wikipedia.org/wiki/Medieval_Latin "Medieval Latin") *reflexivus* ('recoiling' \[cf. \], or 'directed upon itself') (c. 1250 AD) from the [classical Latin](https://en.wikipedia.org/wiki/Classical_Latin "Classical Latin") *reflexus-* ('turn away', 'reflection') + *\-īvus* (suffix). The word entered [Early Modern English](https://en.wikipedia.org/wiki/Early_Modern_English "Early Modern English") in the 1580s. The sense of the word meaning 'directed upon itself', as now used in mathematics, surviving mostly by its use in philosophy and grammar (cf. *[Reflexive verb](https://en.wikipedia.org/wiki/Reflexive_verb "Reflexive verb")* and *[Reflexive pronoun](https://en.wikipedia.org/wiki/Reflexive_pronoun "Reflexive pronoun")*).[^3] [^4]

The first explicit use of "reflexivity", that is, describing a relation as having the property that every element is related to itself, is generally attributed to [Giuseppe Peano](https://en.wikipedia.org/wiki/Giuseppe_Peano "Giuseppe Peano") in his *[Arithmetices principia](https://en.wikipedia.org/wiki/Arithmetices_principia,_nova_methodo_exposita "Arithmetices principia, nova methodo exposita")* (1889), wherein he defines one of the fundamental properties of [equality](https://en.wikipedia.org/wiki/Equality_\(mathematics\) "Equality (mathematics)") being ${\displaystyle a=a}$.[^5] [^6] The first use of the word *reflexive* in the sense of mathematics and logic was by [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell "Bertrand Russell") in his *[Principles of Mathematics](https://en.wikipedia.org/wiki/Principles_of_Mathematics "Principles of Mathematics")* (1903).[^6] [^7]

## Definitions

A relation ${\displaystyle R}$ on the set ${\displaystyle X}$ is said to be *reflexive* if for every ${\displaystyle x\in X}$, ${\displaystyle (x,x)\in R}$.

Equivalently, letting ${\displaystyle \operatorname {I} _{X}:=\{(x,x)~:~x\in X\}}$ denote the [identity relation](https://en.wikipedia.org/wiki/Identity_relation "Identity relation") on ${\displaystyle X}$, the relation ${\displaystyle R}$ is reflexive if ${\displaystyle \operatorname {I} _{X}\subseteq R}$.

The *[reflexive closure](https://en.wikipedia.org/wiki/Reflexive_closure "Reflexive closure")* of ${\displaystyle R}$ is the union ${\displaystyle R\cup \operatorname {I} _{X},}$ which can equivalently be defined as the smallest (with respect to ${\displaystyle \subseteq }$) reflexive relation on ${\displaystyle X}$ that is a [superset](https://en.wikipedia.org/wiki/Superset "Superset") of ${\displaystyle R.}$ A relation ${\displaystyle R}$ is reflexive if and only if it is equal to its reflexive closure.

The *reflexive reduction* or *irreflexive kernel* of ${\displaystyle R}$ is the smallest (with respect to ${\displaystyle \subseteq }$) relation on ${\displaystyle X}$ that has the same reflexive closure as ${\displaystyle R.}$ It is equal to ${\displaystyle R\setminus \operatorname {I} _{X}=\{(x,y)\in R~:~x\neq y\}.}$ The reflexive reduction of ${\displaystyle R}$ can, in a sense, be seen as a construction that is the "opposite" of the reflexive closure of ${\displaystyle R.}$ For example, the reflexive closure of the canonical strict inequality ${\displaystyle <}$ on the [reals](https://en.wikipedia.org/wiki/Real_number "Real number") ${\displaystyle \mathbb {R} }$ is the usual non-strict inequality ${\displaystyle \leq }$ whereas the reflexive reduction of ${\displaystyle \leq }$ is ${\displaystyle <.}$

### Related definitions

There are several definitions related to the reflexive property. The relation ${\displaystyle R}$ is called:

irreflexive, anti-reflexive or aliorelative

[^8] if it does not relate any element to itself; that is, if ${\displaystyle xRx}$ holds for no ${\displaystyle x\in X.}$ A relation is irreflexive [if and only if](https://en.wikipedia.org/wiki/If_and_only_if "If and only if") its [complement](https://en.wikipedia.org/wiki/Complementary_relation "Complementary relation") in ${\displaystyle X\times X}$ is reflexive. An [asymmetric relation](https://en.wikipedia.org/wiki/Asymmetric_relation "Asymmetric relation") is necessarily irreflexive. A transitive and irreflexive relation is necessarily asymmetric.

left quasi-reflexive

if whenever ${\displaystyle x,y\in X}$ are such that ${\displaystyle xRy,}$ then necessarily ${\displaystyle xRx.}$ [^9]

right quasi-reflexive

if whenever ${\displaystyle x,y\in X}$ are such that ${\displaystyle xRy,}$ then necessarily ${\displaystyle yRy.}$

quasi-reflexive

if every element that is part of some relation is related to itself. Explicitly, this means that whenever ${\displaystyle x,y\in X}$ are such that ${\displaystyle xRy,}$ then necessarily ${\displaystyle xRx}$ and ${\displaystyle yRy.}$ Equivalently, a binary relation is quasi-reflexive if and only if it is both left quasi-reflexive and right quasi-reflexive. A relation ${\displaystyle R}$ is quasi-reflexive if and only if its [symmetric closure](https://en.wikipedia.org/wiki/Symmetric_closure "Symmetric closure") ${\displaystyle R\cup R^{\operatorname {T} }}$ is left (or right) quasi-reflexive.

[antisymmetric](https://en.wikipedia.org/wiki/Antisymmetric_relation "Antisymmetric relation")

if whenever ${\displaystyle x,y\in X}$ are such that ${\displaystyle xRy{\text{ and }}yRx,}$ then necessarily ${\displaystyle x=y.}$

coreflexive

if whenever ${\displaystyle x,y\in X}$ are such that ${\displaystyle xRy,}$ then necessarily ${\displaystyle x=y.}$ [^10] A relation ${\displaystyle R}$ is coreflexive if and only if its symmetric closure is [anti-symmetric](https://en.wikipedia.org/wiki/Antisymmetric_relation "Antisymmetric relation").

A reflexive relation on a nonempty set ${\displaystyle X}$ can neither be irreflexive, nor [asymmetric](https://en.wikipedia.org/wiki/Asymmetric_relation "Asymmetric relation") (${\displaystyle R}$ is called *asymmetric* if ${\displaystyle xRy}$ implies not ${\displaystyle yRx}$), nor [antitransitive](https://en.wikipedia.org/wiki/Antitransitive "Antitransitive") (${\displaystyle R}$ is *antitransitive* if ${\displaystyle xRy{\text{ and }}yRz}$ implies not ${\displaystyle xRz}$).

## Examples

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/GreaterThanOrEqualTo.png/250px-GreaterThanOrEqualTo.png) ![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/GreaterThan.png/250px-GreaterThan.png)

Examples of reflexive relations include:

- "is equal to" ([equality](https://en.wikipedia.org/wiki/Equality_\(mathematics\) "Equality (mathematics)"))
- "is a [subset](https://en.wikipedia.org/wiki/Subset "Subset") of" (set inclusion)
- "divides" ([divisibility](https://en.wikipedia.org/wiki/Divisor "Divisor"))
- "is greater than or equal to"
- "is less than or equal to"

Examples of irreflexive relations include:

- "is not equal to"
- "is [coprime](https://en.wikipedia.org/wiki/Coprime "Coprime") to" on the integers larger than 1
- "is a [proper subset](https://en.wikipedia.org/wiki/Proper_subset "Proper subset") of"
- "is greater than"
- "is less than"

An example of an irreflexive relation, which means that it does not relate any element to itself, is the "greater than" relation (${\displaystyle x>y}$) on the [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number"). Not every relation which is not reflexive is irreflexive; it is possible to define relations where some elements are related to themselves but others are not (that is, neither all nor none are). For example, the binary relation "the product of ${\displaystyle x}$ and ${\displaystyle y}$ is even" is reflexive on the set of [even numbers](https://en.wikipedia.org/wiki/Even_number "Even number"), irreflexive on the set of odd numbers, and neither reflexive nor irreflexive on the set of [natural numbers](https://en.wikipedia.org/wiki/Natural_number "Natural number").

An example of a quasi-reflexive relation ${\displaystyle R}$ is "has the same limit as" on the set of sequences of real numbers: not every sequence has a limit, and thus the relation is not reflexive, but if a sequence has the same limit as some sequence, then it has the same limit as itself. An example of a left quasi-reflexive relation is a left [Euclidean relation](https://en.wikipedia.org/wiki/Euclidean_relation "Euclidean relation"), which is always left quasi-reflexive but not necessarily right quasi-reflexive, and thus not necessarily quasi-reflexive.

An example of a coreflexive relation is the relation on [integers](https://en.wikipedia.org/wiki/Integer "Integer") in which each odd number is related to itself and there are no other relations. The equality relation is the only example of a both reflexive and coreflexive relation, and any coreflexive relation is a subset of the identity relation. The union of a coreflexive relation and a transitive relation on the same set is always transitive.

## Number of reflexive relations

The number of reflexive relations on an ${\displaystyle n}$ -element set is ${\displaystyle 2^{n^{2}-n}.}$ [^11]

| Elem­ents | [Any](https://en.wikipedia.org/wiki/Binary_relation "Binary relation") | [Transitive](https://en.wikipedia.org/wiki/Transitive_relation "Transitive relation") | Reflexive | [Symmetric](https://en.wikipedia.org/wiki/Symmetric_relation "Symmetric relation") | [Preorder](https://en.wikipedia.org/wiki/Preorder "Preorder") | [Partial order](https://en.wikipedia.org/wiki/Partially_ordered_set "Partially ordered set") | [Total preorder](https://en.wikipedia.org/wiki/Strict_weak_ordering "Strict weak ordering") | [Total order](https://en.wikipedia.org/wiki/Total_order "Total order") | [Equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation "Equivalence relation") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 1 |
| 2 | 16 | 13 | 4 | 8 | 4 | 3 | 3 | 2 | 2 |
| 3 | 512 | 171 | 64 | 64 | 29 | 19 | 13 | 6 | 5 |
| 4 | 65,536 | 3,994 | 4,096 | 1,024 | 355 | 219 | 75 | 24 | 15 |
| *n* | 2 <sup><i>n</i> <sup>2</sup></sup> |  | 2 <sup><i>n</i> (<i>n</i> −1)</sup> | 2 <sup><i>n</i> (<i>n</i> +1)/2</sup> |  |  | ∑ <sup><i>n</i></sup>   <sub><i>k</i> =0</sub> *k*!*S* (*n*, *k*) | *n*! | ∑ <sup><i>n</i></sup>   <sub><i>k</i> =0</sub> *S* (*n*, *k*) |
| [OEIS](https://en.wikipedia.org/wiki/OEIS "OEIS") | [A002416](https://oeis.org/A002416 "oeis:A002416") | [A006905](https://oeis.org/A006905 "oeis:A006905") | [A053763](https://oeis.org/A053763 "oeis:A053763") | [A006125](https://oeis.org/A006125 "oeis:A006125") | [A000798](https://oeis.org/A000798 "oeis:A000798") | [A001035](https://oeis.org/A001035 "oeis:A001035") | [A000670](https://oeis.org/A000670 "oeis:A000670") | [A000142](https://oeis.org/A000142 "oeis:A000142") | [A000110](https://oeis.org/A000110 "oeis:A000110") |

Note that *S* (*n*, *k*) refers to [Stirling numbers of the second kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind "Stirling numbers of the second kind").

## Philosophical logic

Authors in [philosophical logic](https://en.wikipedia.org/wiki/Philosophical_logic "Philosophical logic") often use different terminology. Reflexive relations in the mathematical sense are called **totally reflexive** in philosophical logic, and quasi-reflexive relations are called **reflexive**.[^12] [^13]

## Notes

## References

- Clarke, D.S.; Behling, Richard (1998). *Deductive Logic – An Introduction to Evaluation Techniques and Logical Theory*. University Press of America. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-7618-0922-8](https://en.wikipedia.org/wiki/Special:BookSources/0-7618-0922-8 "Special:BookSources/0-7618-0922-8").
- Fonseca de Oliveira, José Nuno; Pereira Cunha Rodrigues, César de Jesus (2004), "Transposing relations: from Maybe functions to hash tables", *Mathematics of Program Construction*, Lecture Notes in Computer Science, **3125**, Springer: 334–356, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-540-27764-4\_18](https://doi.org/10.1007%2F978-3-540-27764-4_18), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-22380-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-22380-1 "Special:BookSources/978-3-540-22380-1")
- Hausman, Alan; Kahane, Howard; Tidman, Paul (2013). *Logic and Philosophy – A Modern Introduction*. Wadsworth. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-133-05000-1](https://en.wikipedia.org/wiki/Special:BookSources/978-1-133-05000-1 "Special:BookSources/978-1-133-05000-1").
- Levy, A. (1979), *Basic Set Theory*, Perspectives in Mathematical Logic, Dover, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-486-42079-5](https://en.wikipedia.org/wiki/Special:BookSources/0-486-42079-5 "Special:BookSources/0-486-42079-5")
- Lidl, R.; Pilz, G. (1998), *Applied abstract algebra*, [Undergraduate Texts in Mathematics](https://en.wikipedia.org/wiki/Undergraduate_Texts_in_Mathematics "Undergraduate Texts in Mathematics"), Springer-Verlag, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-387-98290-6](https://en.wikipedia.org/wiki/Special:BookSources/0-387-98290-6 "Special:BookSources/0-387-98290-6")
- Quine, W. V. (1951), *Mathematical Logic*, Revised Edition, Reprinted 2003, Harvard University Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-674-55451-5](https://en.wikipedia.org/wiki/Special:BookSources/0-674-55451-5 "Special:BookSources/0-674-55451-5")
- [Russell, Bertrand](https://en.wikipedia.org/wiki/Bertrand_Russell "Bertrand Russell") (1920). [*Introduction to Mathematical Philosophy*](https://people.umass.edu/klement/imp/imp-ebk.pdf) (PDF) (2nd ed.). London: George Allen & Unwin, Ltd. (Online corrected edition, Feb 2010)
- Schmidt, Gunther (2010), *Relational Mathematics*, Cambridge University Press, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-76268-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-76268-7 "Special:BookSources/978-0-521-76268-7")

## External links

- ["Reflexivity"](https://www.encyclopediaofmath.org/index.php?title=Reflexivity), *[Encyclopedia of Mathematics](https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics "Encyclopedia of Mathematics")*, [EMS Press](https://en.wikipedia.org/wiki/European_Mathematical_Society "European Mathematical Society"), 2001 \[1994\]

[^1]: [Levy 1979](#CITEREFLevy1979), p. 74

[^2]: [Schmidt 2010](#CITEREFSchmidt2010)

[^3]: ["reflexive | Etymology of reflexive by etymonline"](https://www.etymonline.com/word/reflexive#etymonline_v_37000). *www.etymonline.com*. Retrieved 2024-12-22.

[^4]: *[Oxford English Dictionary](https://en.wikipedia.org/wiki/Oxford_English_Dictionary "Oxford English Dictionary")*, s.v. “ [Reflexive (*adj.* & *n.*), Etymology](https://doi.org/10.1093/OED/7005855243 "doi:10.1093/OED/7005855243"),” September 2024.

[^5]: [Peano, Giuseppe](https://en.wikipedia.org/wiki/Giuseppe_Peano "Giuseppe Peano") (1889). [*Arithmetices principia: nova methodo*](https://archive.org/details/arithmeticespri00peangoog/page/n18/mode/2up) (in Latin). Fratres Bocca. pp. XIII. Archived from [the original](https://books.google.com/books?id=z80GAAAAYAAJ) on 2009-07-15.

[^6]: [Russell, Bertrand](https://en.wikipedia.org/wiki/Bertrand_Russell "Bertrand Russell") (1903). [*Principles of Mathematics*](https://doi.org/10.4324/9780203864760). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.4324/9780203864760](https://doi.org/10.4324%2F9780203864760). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-135-22311-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-135-22311-3 "Special:BookSources/978-1-135-22311-3").

[^7]: *[Oxford English Dictionary](https://en.wikipedia.org/wiki/Oxford_English_Dictionary "Oxford English Dictionary")*, s.v. “ [Reflexive (*adj.*), sense 7 - *Mathematics and Logic*](https://doi.org/10.1093/OED/4192548146 "doi:10.1093/OED/4192548146") ”, " **1903–** ", September 2024.

[^8]: This term is due to [C S Peirce](https://en.wikipedia.org/wiki/C_S_Peirce "C S Peirce"); see [Russell 1920](#CITEREFRussell1920), p. 32. Russell also introduces two equivalent terms *to be contained in* or *imply diversity*.

[^9]: The [Encyclopædia Britannica](https://www.britannica.com/topic/formal-logic/Logical-manipulations-in-LPC#ref534730) calls this property quasi-reflexivity.

[^10]: [Fonseca de Oliveira & Pereira Cunha Rodrigues 2004](#CITEREFFonseca_de_OliveiraPereira_Cunha_Rodrigues2004), p. 337

[^11]: On-Line Encyclopedia of Integer Sequences [A053763](https://oeis.org/A053763 "oeis:A053763")

[^12]: [Hausman, Kahane & Tidman 2013](#CITEREFHausmanKahaneTidman2013), pp. 327–328

[^13]: [Clarke & Behling 1998](#CITEREFClarkeBehling1998), p. 187