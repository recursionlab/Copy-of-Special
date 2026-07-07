---
title: "Class (set theory)"
source: "https://en.wikipedia.org/wiki/Class_(set_theory)"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2001-12-08
created: 2026-04-10
description:
tags:
  - "clippings"
---
In [set theory](https://en.wikipedia.org/wiki/Set_theory "Set theory") and its applications throughout [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), a **class** is a collection of mathematical objects (often [sets](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)")) that can be unambiguously defined by a [property](https://en.wikipedia.org/wiki/Property_\(mathematics\) "Property (mathematics)") that all its members share. Classes act as a way to have set-like collections while differing from sets so as to avoid paradoxes, especially [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox "Russell's paradox") (see *[§ Paradoxes](#Paradoxes)*). The precise definition of "class" depends on foundational context. In work on [Zermelo–Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory "Zermelo–Fraenkel set theory"), the notion of class is informal, whereas other set theories, such as [von Neumann–Bernays–Gödel set theory](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Bernays%E2%80%93G%C3%B6del_set_theory "Von Neumann–Bernays–Gödel set theory"), axiomatize the notion of "proper class", e.g., as entities that are not members of another entity.

A class that is not a set (informally in Zermelo–Fraenkel) is called a **proper class**, and a class that is a set is sometimes called a **small class**. For instance, the class of all [ordinal numbers](https://en.wikipedia.org/wiki/Ordinal_number "Ordinal number"), and the class of all sets, are proper classes in many formal systems.

In [Quine](https://en.wikipedia.org/wiki/Willard_Van_Orman_Quine "Willard Van Orman Quine") 's set-theoretical writing, the phrase "ultimate class" is often used instead of the phrase "proper class" emphasising that in the systems he considers, certain classes cannot be members, and are thus the final term in any membership chain to which they belong.

Outside set theory, the word "class" is sometimes used synonymously with "set". This usage dates from a historical period when classes and sets were not distinguished as they are in modern set-theoretic terminology.[^1] Many discussions of "classes" in the 19th century and earlier are really referring to sets, or rather perhaps take place without considering that certain classes can fail to be sets.

## Examples

The collection of all [algebraic structures](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure") of a given type will usually be a proper class. Examples include the class of all [groups](https://en.wikipedia.org/wiki/Group_\(mathematics\) "Group (mathematics)"), the class of all [vector spaces](https://en.wikipedia.org/wiki/Vector_space "Vector space"), and many others. In [category theory](https://en.wikipedia.org/wiki/Category_theory "Category theory"), a [category](https://en.wikipedia.org/wiki/Category_\(mathematics\) "Category (mathematics)") whose collection of [objects](https://en.wikipedia.org/wiki/Object_\(category_theory\) "Object (category theory)") forms a proper class (or whose collection of [morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism") forms a proper class) is called a [large category](https://en.wikipedia.org/wiki/Large_category "Large category").

The [surreal numbers](https://en.wikipedia.org/wiki/Surreal_number "Surreal number") are a proper class of objects that have the properties of a [field](https://en.wikipedia.org/wiki/Field_\(mathematics\) "Field (mathematics)").

Within set theory, many collections of sets turn out to be proper classes. Examples include the class of all sets (the universal class), the class of all ordinal numbers, and the class of all [cardinal numbers](https://en.wikipedia.org/wiki/Cardinal_number "Cardinal number").

One way to prove that a class is proper is to place it in [bijection](https://en.wikipedia.org/wiki/Bijection "Bijection") with the class of all ordinal numbers. This method is used, for example, in the proof that there is no [free](https://en.wikipedia.org/wiki/Free_lattice#The_complete_free_lattice "Free lattice") [complete lattice](https://en.wikipedia.org/wiki/Complete_lattice#Free_complete_lattices "Complete lattice") on three or more [generators](https://en.wikipedia.org/wiki/Generator_\(mathematics\) "Generator (mathematics)").

## Paradoxes

The [paradoxes of naive set theory](https://en.wikipedia.org/wiki/Naive_set_theory#Paradoxes "Naive set theory") can be explained in terms of the inconsistent [tacit assumption](https://en.wikipedia.org/wiki/Tacit_assumption "Tacit assumption") that "all classes are sets". With a rigorous foundation, these paradoxes instead suggest [proofs](https://en.wikipedia.org/wiki/Proof_\(mathematics\) "Proof (mathematics)") that certain classes are proper (i.e., that they are not sets). For example, [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox "Russell's paradox") suggests a proof that the class of all sets which do not contain themselves is proper, and the [Burali-Forti paradox](https://en.wikipedia.org/wiki/Burali-Forti_paradox "Burali-Forti paradox") suggests that the class of all [ordinal numbers](https://en.wikipedia.org/wiki/Ordinal_numbers "Ordinal numbers") is proper. The paradoxes do not arise with classes because there is no notion of classes containing classes. Otherwise, one could, for example, define a class of all classes that do not contain themselves, which would lead to a Russell paradox for classes. A [conglomerate](https://en.wikipedia.org/wiki/Conglomerate_\(category_theory\) "Conglomerate (category theory)"), on the other hand, can have proper classes as members.[^2]

## Classes in formal set theories

[ZF set theory](https://en.wikipedia.org/wiki/ZF_set_theory "ZF set theory") does not formalize the notion of classes, so each formula with classes must be reduced syntactically to a formula without classes.[^3] For example, one can reduce the formula ${\displaystyle A=\{x\mid x=x\}}$ to ${\displaystyle \forall x(x\in A\leftrightarrow x=x)}$. For a class ${\displaystyle A}$ and a set variable symbol ${\displaystyle x}$, it is necessary to be able to expand each of the formulas ${\displaystyle x\in A}$, ${\displaystyle x=A}$, ${\displaystyle A\in x}$, and ${\displaystyle A=x}$ into a formula without an occurrence of a class.[^4] <sup>p. 339</sup>

Semantically, in a [metalanguage](https://en.wikipedia.org/wiki/Metalanguage "Metalanguage"), the classes can be described as [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_classes "Equivalence classes") of [logical formulas](https://en.wikipedia.org/wiki/Well-formed_formula "Well-formed formula"): If ${\displaystyle {\mathcal {A}}}$ is a [structure](https://en.wikipedia.org/wiki/Structure_\(mathematical_logic\) "Structure (mathematical logic)") interpreting ZF, then the object language "class-builder expression" ${\displaystyle \{x\mid \phi \}}$ is interpreted in ${\displaystyle {\mathcal {A}}}$ by the collection of all the elements from the domain of ${\displaystyle {\mathcal {A}}}$ on which ${\displaystyle \phi (x)}$ holds; thus, the class can be described as the set of all predicates equivalent to ${\displaystyle \phi }$ (which includes ${\displaystyle \phi }$ itself). In particular, one can identify the "class of all sets" with the set of all predicates equivalent to ${\displaystyle x=x}$.

Because classes do not have any formal status in the theory of ZF, the axioms of ZF do not immediately apply to classes. However, if an [inaccessible cardinal](https://en.wikipedia.org/wiki/Inaccessible_cardinal "Inaccessible cardinal") ${\displaystyle \kappa }$ is assumed, then the sets of smaller [rank](https://en.wikipedia.org/wiki/Rank_\(set_theory\) "Rank (set theory)") form a model of ZF (a [Grothendieck universe](https://en.wikipedia.org/wiki/Grothendieck_universe "Grothendieck universe")), and its subsets can be thought of as "classes".

In ZF, the concept of a [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)") can also be generalised to classes. A class function is not a function in the usual sense, since it is not a set; it is rather a formula ${\displaystyle \Phi (x,y)}$ with the property that for any set ${\displaystyle x}$ there is no more than one set ${\displaystyle y}$ such that the pair ${\displaystyle (x,y)}$ satisfies ${\displaystyle \Phi }$. For example, the class function mapping each set to its powerset may be expressed as the formula ${\displaystyle y={\mathcal {P}}(x)}$. The fact that the ordered pair ${\displaystyle (x,y)}$ satisfies ${\displaystyle \Phi }$ may be expressed with the shorthand notation ${\displaystyle \Phi (x)=y}$.

Another approach is taken by the [von Neumann–Bernays–Gödel axioms](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Bernays%E2%80%93G%C3%B6del_axioms "Von Neumann–Bernays–Gödel axioms") (NBG); classes are the basic objects in this theory, and a set is then defined to be a class that is an element of some other class. However, the class existence axioms of NBG are restricted so that they only quantify over sets, rather than over all classes. This causes NBG to be a [conservative extension](https://en.wikipedia.org/wiki/Conservative_extension "Conservative extension") of ZFC.

[Morse–Kelley set theory](https://en.wikipedia.org/wiki/Morse%E2%80%93Kelley_set_theory "Morse–Kelley set theory") admits proper classes as basic objects, like NBG, but also allows quantification over all proper classes in its class existence axioms. This causes Morse–Kelley set theory to be strictly stronger than both NBG and ZFC.

Other set theories, such as [New Foundations](https://en.wikipedia.org/wiki/New_Foundations "New Foundations") or the theory of [semisets](https://en.wikipedia.org/wiki/Semiset "Semiset"), still give rise to "proper classes" (insofar as they require classes that are not sets), because they do not postulate that all subclasses of a set are themselves sets. For example, any set theory with a [universal set](https://en.wikipedia.org/wiki/Universal_set "Universal set") must include proper classes that are subclasses of sets.

## Notes

## References

- [Jech, Thomas](https://en.wikipedia.org/wiki/Thomas_Jech "Thomas Jech") (2003), *Set Theory*, Springer Monographs in Mathematics (third millennium ed.), Berlin, New York: [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-44085-7](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-44085-7 "Special:BookSources/978-3-540-44085-7")
- [Levy, A.](https://en.wikipedia.org/wiki/Azriel_Levy "Azriel Levy") (1979), *Basic Set Theory*, Berlin, New York: [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag")
- [Smullyan, Raymond M.](https://en.wikipedia.org/wiki/Raymond_Smullyan "Raymond Smullyan"); [Fitting, Melvin](https://en.wikipedia.org/wiki/Melvin_Fitting "Melvin Fitting") (2010), *Set Theory And The Continuum Problem*, Dover Publications, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-486-47484-7](https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-47484-7 "Special:BookSources/978-0-486-47484-7")
- Monk, Donald J. (1969), *Introduction to Set Theory*, McGraw-Hill Book Co., [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780070427150](https://en.wikipedia.org/wiki/Special:BookSources/9780070427150 "Special:BookSources/9780070427150")

## External links

- [Weisstein, Eric W.](https://en.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), ["Set Class"](https://mathworld.wolfram.com/SetClass.html), *[MathWorld](https://en.wikipedia.org/wiki/MathWorld "MathWorld")*

[^1]: [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell "Bertrand Russell") (1903). *[The Principles of Mathematics](https://en.wikipedia.org/wiki/The_Principles_of_Mathematics "The Principles of Mathematics")*, [Chapter VI: Classes](https://archive.org/details/principlesofmath005807mbp/page/n109/mode/2up), via [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive "Internet Archive")

[^2]: [Herrlich, Horst](https://en.wikipedia.org/wiki/Horst_Herrlich "Horst Herrlich"); Strecker, George (2007), ["Sets, classes, and conglomerates"](http://www.heldermann.de/SSPM/SSPM01/Chapter-2.pdf) (PDF), [*Category theory*](http://www.heldermann.de/SSPM/SSPM01/sspm01.htm) (3rd ed.), Heldermann Verlag, pp. 9–12

[^3]: [*eqabb – Metamath Proof Explorer*](https://us.metamath.org/mpeuni/eqabb.html), us.metamath.org, 1993-08-05, retrieved 2026-01-01

[^4]: [J. R. Shoenfield](https://en.wikipedia.org/wiki/Joseph_R._Shoenfield "Joseph R. Shoenfield"), "Axioms of Set Theory". In *Handbook of Mathematical Logic*, Studies in Logic and the Foundations of mathematical vol. 90, ed. J. Barwise (1977)