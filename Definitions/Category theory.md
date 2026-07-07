---
title: "Category theory"
source: "https://en.wikipedia.org/wiki/Category_theory"
author:
  - "[[Wikipedia]]"
published: 2001-10-31
created: 2026-04-29
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Commutative_diagram_for_morphism.svg/250px-Commutative_diagram_for_morphism.svg.png)

Schematic representation of three objects and three morphisms of a category, which form a commutative diagram

**Category theory** is a general theory of [mathematical structures](https://en.wikipedia.org/wiki/Mathematical_structure "Mathematical structure") and their relations. It was introduced by [Samuel Eilenberg](https://en.wikipedia.org/wiki/Samuel_Eilenberg "Samuel Eilenberg") and [Saunders Mac Lane](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane") in the mid-20th century in their foundational work on [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology").[^4] Category theory can be used in most areas of mathematics. In particular, many constructions of new [mathematical objects](https://en.wikipedia.org/wiki/Mathematical_object "Mathematical object") from previous ones that appear similarly in several contexts are conveniently expressed and unified in terms of categories. Examples include [quotient spaces](https://en.wikipedia.org/wiki/Quotient_space_\(disambiguation\) "Quotient space (disambiguation)"), [direct products](https://en.wikipedia.org/wiki/Direct_product "Direct product"), completion, and [duality](https://en.wikipedia.org/wiki/Duality_\(mathematics\) "Duality (mathematics)").

Many areas of [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science") also rely on category theory, such as [functional programming](https://en.wikipedia.org/wiki/Functional_programming "Functional programming") and [semantics](https://en.wikipedia.org/wiki/Semantics_\(computer_science\) "Semantics (computer science)").

A [category](https://en.wikipedia.org/wiki/Category_\(mathematics\) "Category (mathematics)") is formed by two sorts of [objects](https://en.wikipedia.org/wiki/Mathematical_object "Mathematical object"): the [objects](https://en.wikipedia.org/wiki/Object_\(category_theory\) "Object (category theory)") of the category, and the [morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism"), which relate two objects called the *source* and the *target* of the morphism. A morphism is often represented by an arrow from its source to its target (see the figure). Morphisms can be composed if the target of the first morphism equals the source of the second one. Morphism composition has similar properties as [function composition](https://en.wikipedia.org/wiki/Function_composition "Function composition") ([associativity](https://en.wikipedia.org/wiki/Associativity "Associativity") and existence of an [identity morphism](https://en.wikipedia.org/wiki/Identity_element "Identity element") for each object). Morphisms are often some sort of [functions](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)"), but this is not always the case. For example, a [monoid](https://en.wikipedia.org/wiki/Monoid "Monoid") may be viewed as a category with a single object, whose morphisms are the elements of the monoid.

The second fundamental concept of category theory is the concept of a [functor](https://en.wikipedia.org/wiki/Functor "Functor"), which plays the role of a morphism between two categories ${\displaystyle {\mathcal {C}}_{1}}$ and ${\displaystyle {\mathcal {C}}_{2}}$: it maps objects of ${\displaystyle {\mathcal {C}}_{1}}$ to objects of ${\displaystyle {\mathcal {C}}_{2}}$ and morphisms of ${\displaystyle {\mathcal {C}}_{1}}$ to morphisms of ${\displaystyle {\mathcal {C}}_{2}}$ in such a way that sources are mapped to sources, and targets are mapped to targets (or, in the case of a [contravariant functor](https://en.wikipedia.org/wiki/Contravariant_functor "Contravariant functor"), sources are mapped to targets and *vice-versa*). A third fundamental concept is a [natural transformation](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation") that may be viewed as a morphism of functors.

## Categories, objects, and morphisms

### Categories

A *category* ${\displaystyle {\mathcal {C}}}$ consists of the following three mathematical entities:

- A [class](https://en.wikipedia.org/wiki/Class_\(set_theory\) "Class (set theory)") ${\displaystyle {\text{ob}}({\mathcal {C}})}$, whose elements are called *objects*;
- A class ${\displaystyle {\text{hom}}({\mathcal {C}})}$, whose elements are called [morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism") or [maps](https://en.wikipedia.org/wiki/Map_\(mathematics\) "Map (mathematics)") or *arrows*.
	Each morphism **${\displaystyle f}$** has a *source object* **${\displaystyle a}$** and *target object* **${\displaystyle b}$**.
	The expression ${\displaystyle f\colon a\rightarrow b}$ would be verbally stated as " ${\displaystyle f}$ is a morphism from a to b".
	The expression ${\displaystyle {\text{hom}}(a,b)}$ – alternatively expressed as ${\displaystyle {\text{hom}}_{\mathcal {C}}(a,b)}$, ${\displaystyle {\text{mor}}(a,b)}$, or ${\displaystyle {\mathcal {C}}(a,b)}$ – denotes the *hom-class* of all morphisms from ${\displaystyle a}$ to ${\displaystyle b}$.[^1]
- A [binary operation](https://en.wikipedia.org/wiki/Binary_operation "Binary operation") ${\displaystyle \circ }$, called *composition of morphisms*, such that for any three objects *a*, *b*, and *c*, we have 
	$$
	{\displaystyle \circ \colon {\text{hom}}(b,c)\times {\text{hom}}(a,b)\to {\text{hom}}(a,c)}
	$$
	 The composition of ${\displaystyle f\colon a\rightarrow b}$ and ${\displaystyle g\colon b\rightarrow c}$ is written as ${\displaystyle g\circ f}$ or ${\displaystyle gf}$,[^2] governed by two axioms:
	1. [Associativity](https://en.wikipedia.org/wiki/Associativity "Associativity"): If ${\displaystyle f\colon a\rightarrow b}$, ${\displaystyle g\colon b\rightarrow c}$, and ${\displaystyle h\colon c\rightarrow d}$ then 
		$$
		{\displaystyle h\circ (g\circ f)=(h\circ g)\circ f}
		$$
		2. [Identity](https://en.wikipedia.org/wiki/Identity_\(mathematics\) "Identity (mathematics)"): For every object x, there exists a morphism ${\displaystyle 1_{x}\colon x\rightarrow x}$ (also denoted as ${\displaystyle {\text{id}}_{x}}$) called the *[identity morphism](https://en.wikipedia.org/wiki/Identity_morphism "Identity morphism") for x*, such that for every morphism ${\displaystyle f\colon a\rightarrow b}$, we have 
		$$
		{\displaystyle 1_{b}\circ f=f=f\circ 1_{a}}
		$$
		From the axioms, it can be proved that there is exactly one identity morphism for every object.

#### Example

A prototypical example of a category is **Set**, the [category of sets](https://en.wikipedia.org/wiki/Category_of_sets "Category of sets") and functions between them. The objects of **Set** are just [sets](https://en.wikipedia.org/wiki/Set_\(mathematics\) "Set (mathematics)"), and a morphism from a set *X* to a set *Y* is a [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)") *f*: *X* → *Y*. The category axioms are satisfied since every set has an [identity function](https://en.wikipedia.org/wiki/Identity_function "Identity function"), and since [composition of functions](https://en.wikipedia.org/wiki/Composition_of_functions "Composition of functions") is associative.

### Morphisms

Relations among morphisms (such as *fg* = *h*) are often depicted using [commutative diagrams](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram"), with "points" (corners) representing objects and "arrows" representing morphisms.

[Morphisms](https://en.wikipedia.org/wiki/Morphism "Morphism") can have any of the following properties. A morphism *f*: *a* → *b* is:

- a [monomorphism](https://en.wikipedia.org/wiki/Monomorphism "Monomorphism") (or *monic*) if *f* ∘ *g* <sub>1</sub> = *f* ∘ *g* <sub>2</sub> implies *g* <sub>1</sub> = *g* <sub>2</sub> for all morphisms *g* <sub>1</sub>, *g <sub>2</sub>*: *x* → *a*.
- an [epimorphism](https://en.wikipedia.org/wiki/Epimorphism "Epimorphism") (or *epic*) if *g* <sub>1</sub> ∘ *f* = *g* <sub>2</sub> ∘ *f* implies *g <sub>1</sub>* = *g <sub>2</sub>* for all morphisms *g* <sub>1</sub>, *g* <sub>2</sub>: *b* → *x*.
- a *bimorphism* if *f* is both epic and monic.
- an [isomorphism](https://en.wikipedia.org/wiki/Isomorphism "Isomorphism") if there exists a morphism *g*: *b* → *a* such that *f* ∘ *g* = 1 <sub><i>b</i></sub> and *g* ∘ *f* = 1 <sub><i>a</i></sub>.[^3]
- an [endomorphism](https://en.wikipedia.org/wiki/Endomorphism "Endomorphism") if *a* = *b*. end(*a*) denotes the class of endomorphisms of *a*.
- an [automorphism](https://en.wikipedia.org/wiki/Automorphism "Automorphism") if *f* is both an endomorphism and an isomorphism. aut(*a*) denotes the class of automorphisms of *a*.
- a [retraction](https://en.wikipedia.org/wiki/Retract_\(category_theory\) "Retract (category theory)") if a right inverse of *f* exists, i.e. if there exists a morphism *g*: *b* → *a* with *f* ∘ *g* = 1 <sub><i>b</i></sub>.
- a [section](https://en.wikipedia.org/wiki/Section_\(category_theory\) "Section (category theory)") if a left inverse of *f* exists, i.e. if there exists a morphism *g*: *b* → *a* with *g* ∘ *f* = 1 <sub><i>a</i></sub>.

Every retraction is an epimorphism, and every section is a monomorphism. Furthermore, the following three statements are equivalent:

- *f* is a monomorphism and a retraction;
- *f* is an epimorphism and a section;
- *f* is an isomorphism.

## Functors

[Functors](https://en.wikipedia.org/wiki/Functor "Functor") are structure-preserving maps between categories. They can be thought of as morphisms in the category of all (small) categories.

A (**covariant**) functor *F* from a category *C* to a category *D*, written *F*: *C* → *D*, consists of:

- for each object *x* in *C*, an object *F* (*x*) in *D*; and
- for each morphism *f*: *x* → *y* in *C*, a morphism *F* (*f*): *F* (*x*) → *F* (*y*) in *D*,

such that the following two properties hold:

- For every object *x* in *C*, *F* (1 <sub><i>x</i></sub>) = 1 <sub><i>F</i> (<i>x</i>)</sub>;
- For all morphisms *f*: *x* → *y* and *g*: *y* → *z*, *F* (*g* ∘ *f*) = *F* (*g*) ∘ *F* (*f*).

A **contravariant** functor *F*: *C* → *D* is like a covariant functor, except that it "turns morphisms around" ("reverses all the arrows"). More specifically, every morphism *f*: *x* → *y* in *C* must be assigned to a morphism *F* (*f*): *F* (*y*) → *F* (*x*) in *D*. In other words, a contravariant functor acts as a covariant functor from the [opposite category](https://en.wikipedia.org/wiki/Opposite_category "Opposite category") *C* <sup>op</sup> to *D*.

## Natural transformations

A *natural transformation* is a relation between two functors. Functors often describe "natural constructions" and natural transformations then describe "natural homomorphisms" between two such constructions. Sometimes two quite different constructions yield "the same" result; this is expressed by a natural isomorphism between the two functors.

If *F* and *G* are (covariant) functors between the categories *C* and *D*, then a natural transformation *η* from *F* to *G* associates to every object *X* in *C* a morphism *η* <sub><i>X</i></sub>: *F* (*X*) → *G* (*X*) in *D* such that for every morphism *f*: *X* → *Y* in *C*, we have *η* <sub><i>Y</i></sub> ∘ *F* (*f*) = *G* (*f*) ∘ *η* <sub><i>X</i></sub>; this means that the following diagram is [commutative](https://en.wikipedia.org/wiki/Commutative_diagram "Commutative diagram"):

![Commutative diagram defining natural transformations](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Natural_transformation.svg/250px-Natural_transformation.svg.png)

Commutative diagram defining natural transformations

The two functors *F* and *G* are called *naturally isomorphic* if there exists a natural transformation from *F* to *G* such that *η* <sub><i>X</i></sub> is an isomorphism for every object *X* in *C*.

## Other concepts

### Universal constructions, limits, and colimits

Using the language of category theory, many areas of mathematical study can be categorized. Categories include sets, groups and topologies.

Each category is distinguished by properties that all its objects have in common, such as the [empty set](https://en.wikipedia.org/wiki/Empty_set "Empty set") or the [product of two topologies](https://en.wikipedia.org/wiki/Product_topology "Product topology"), yet in the definition of a category, objects are considered atomic, i.e., we *do not know* whether an object *A* is a set, a topology, or any other abstract concept. Hence, the challenge is to define special objects without referring to the internal structure of those objects. To define the empty set without referring to elements, or the product topology without referring to open sets, one can characterize these objects in terms of their relations to other objects, as given by the morphisms of the respective categories. Thus, the task is to find *[universal properties](https://en.wikipedia.org/wiki/Universal_property "Universal property")* that uniquely determine the objects of interest.

Numerous important constructions can be described in a purely categorical way if the *category limit* can be developed and dualized to yield the notion of a *colimit*.

### Equivalent categories

It is a natural question to ask: under which conditions can two categories be considered *essentially the same*, in the sense that theorems about one category can readily be transformed into theorems about the other category? The major tool one employs to describe such a situation is called *equivalence of categories*, which is given by appropriate functors between two categories. Categorical equivalence has found [numerous applications](https://en.wikipedia.org/wiki/Equivalence_of_categories#Examples "Equivalence of categories") in mathematics.

### Further concepts and results

The definitions of categories and functors provide only the very basics of categorical algebra; additional important topics are listed below. Although there are strong interrelations between all of these topics, the given order can be considered as a guideline for further reading.

- The [functor category](https://en.wikipedia.org/wiki/Functor_category "Functor category") *D* <sup><i>C</i></sup> has as objects the functors from *C* to *D* and as morphisms the natural transformations of such functors. The [Yoneda lemma](https://en.wikipedia.org/wiki/Yoneda_lemma "Yoneda lemma") is one of the most famous basic results of category theory; it describes representable functors in functor categories.
- [Duality](https://en.wikipedia.org/wiki/Dual_\(category_theory\) "Dual (category theory)"): Every statement, theorem, or definition in category theory has a *dual* which is essentially obtained by "reversing all the arrows". If one statement is true in a category *C* then its dual is true in the dual category *C* <sup>op</sup>. This duality, which is transparent at the level of category theory, is often obscured in applications and can lead to surprising relationships.
- [Adjoint functors](https://en.wikipedia.org/wiki/Adjoint_functors "Adjoint functors"): A functor can be left (or right) adjoint to another functor that maps in the opposite direction. Such a pair of adjoint functors typically arises from a construction defined by a universal property; this can be seen as a more abstract and powerful view on universal properties.

### Higher-dimensional categories

Many of the above concepts, especially equivalence of categories, adjoint functor pairs, and functor categories, can be situated into the context of *higher-dimensional categories*. Briefly, if we consider a morphism between two objects as a "process taking us from one object to another", then higher-dimensional categories allow us to profitably generalize this by considering "higher-dimensional processes".

For example, a (strict) [2-category](https://en.wikipedia.org/wiki/2-category "2-category") is a category together with "morphisms between morphisms", i.e., processes which allow us to transform one morphism into another. We can then "compose" these "bimorphisms" both horizontally and vertically, and we require a 2-dimensional "exchange law" to hold, relating the two composition laws. In this context, the standard example is **Cat**, the 2-category of all (small) categories, and in this example, bimorphisms of morphisms are simply [natural transformations](https://en.wikipedia.org/wiki/Natural_transformation "Natural transformation") of morphisms in the usual sense. Another basic example is to consider a 2-category with a single object; these are essentially [monoidal categories](https://en.wikipedia.org/wiki/Monoidal_category "Monoidal category"). [Bicategories](https://en.wikipedia.org/wiki/Bicategory "Bicategory") are a weaker notion of 2-dimensional categories in which the composition of morphisms is not strictly associative, but only associative "up to" an isomorphism.

This process can be extended for all [natural numbers](https://en.wikipedia.org/wiki/Natural_number "Natural number") *n*, and these are called [*n* -categories](https://en.wikipedia.org/wiki/N-category "N-category"). There is even a notion of *[ω-category](https://en.wikipedia.org/wiki/Quasi-category "Quasi-category")* corresponding to the [ordinal number](https://en.wikipedia.org/wiki/Ordinal_number "Ordinal number") [ω](https://en.wikipedia.org/wiki/%CE%A9_\(ordinal_number\) "Ω (ordinal number)").

Higher-dimensional categories are part of the broader mathematical field of [higher-dimensional algebra](https://en.wikipedia.org/wiki/Higher-dimensional_algebra "Higher-dimensional algebra"), a concept introduced by [Ronald Brown](https://en.wikipedia.org/wiki/Ronald_Brown_\(mathematician\) "Ronald Brown (mathematician)"). For a conversational introduction to these ideas, see [John Baez, 'A Tale of *n* -categories' (1996).](http://math.ucr.edu/home/baez/week73.html)

## Historical notes

> It should be observed first that the whole concept of a category is essentially an auxiliary one; our basic concepts are essentially those of a functor and of a natural transformation \[...\]

—  [Eilenberg](https://en.wikipedia.org/wiki/Samuel_Eilenberg "Samuel Eilenberg") and [Mac Lane](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane") (1945) [^5]

Whilst specific examples of functors and natural transformations had been given by [Samuel Eilenberg](https://en.wikipedia.org/wiki/Samuel_Eilenberg "Samuel Eilenberg") and [Saunders Mac Lane](https://en.wikipedia.org/wiki/Saunders_Mac_Lane "Saunders Mac Lane") in a 1942 paper on [group theory](https://en.wikipedia.org/wiki/Group_theory "Group theory"),[^6] these concepts were introduced in a more general sense, together with the additional notion of categories, in a 1945 paper by the same authors [^5] (who discussed applications of category theory to the field of [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology")).[^7] Their work was an important part of the transition from intuitive and geometric [homology](https://en.wikipedia.org/wiki/Homology_\(mathematics\) "Homology (mathematics)") to [homological algebra](https://en.wikipedia.org/wiki/Homological_algebra "Homological algebra"), Eilenberg and Mac Lane later writing that their goal was to understand natural transformations, which first required the definition of functors, then categories.

[Stanisław Ulam](https://en.wikipedia.org/wiki/Stanis%C5%82aw_Ulam "Stanisław Ulam"), and some writing on his behalf, have claimed that related ideas were current in the late 1930s in Poland. Eilenberg was Polish, and studied mathematics in Poland in the 1930s.[^8] Category theory is also, in some sense, a continuation of the work of [Emmy Noether](https://en.wikipedia.org/wiki/Emmy_Noether "Emmy Noether") (one of Mac Lane's teachers) in formalizing abstract processes;[^9] Noether realized that understanding a type of mathematical structure requires understanding the processes that preserve that structure ([homomorphisms](https://en.wikipedia.org/wiki/Homomorphism "Homomorphism")). Eilenberg and Mac Lane introduced categories for understanding and formalizing the processes ([functors](https://en.wikipedia.org/wiki/Functor "Functor")) that relate [topological structures](https://en.wikipedia.org/wiki/Topology "Topology") to algebraic structures ([topological invariants](https://en.wikipedia.org/wiki/Topological_invariant "Topological invariant")) that characterize them.

Category theory was originally introduced for the need of [homological algebra](https://en.wikipedia.org/wiki/Homological_algebra "Homological algebra"), and widely extended for the need of modern [algebraic geometry](https://en.wikipedia.org/wiki/Algebraic_geometry "Algebraic geometry") ([scheme theory](https://en.wikipedia.org/wiki/Scheme_theory "Scheme theory")). Category theory may be viewed as an extension of [universal algebra](https://en.wikipedia.org/wiki/Universal_algebra "Universal algebra"), as the latter studies [algebraic structures](https://en.wikipedia.org/wiki/Algebraic_structure "Algebraic structure"), and the former applies to any kind of [mathematical structure](https://en.wikipedia.org/wiki/Mathematical_structure "Mathematical structure") and studies also the relationships between structures of different nature. For this reason, it is used throughout mathematics. Applications to [mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic "Mathematical logic") and [semantics](https://en.wikipedia.org/wiki/Semantics_\(computer_science\) "Semantics (computer science)") ([categorical abstract machine](https://en.wikipedia.org/wiki/Categorical_abstract_machine "Categorical abstract machine")) came later.

Certain categories called [topoi](https://en.wikipedia.org/wiki/Topos "Topos") (singular *topos*) can even serve as an alternative to [axiomatic set theory](https://en.wikipedia.org/wiki/Axiomatic_set_theory "Axiomatic set theory") as a foundation of mathematics. A topos can also be considered as a specific type of category with two additional topos axioms. These foundational applications of category theory have been worked out in fair detail as a basis for, and justification of, [constructive mathematics](https://en.wikipedia.org/wiki/Constructivism_\(mathematics\) "Constructivism (mathematics)"). [Topos theory](https://en.wikipedia.org/wiki/Topos "Topos") is a form of abstract [sheaf theory](https://en.wikipedia.org/wiki/Sheaf_\(mathematics\) "Sheaf (mathematics)"), with geometric origins, and leads to ideas such as [pointless topology](https://en.wikipedia.org/wiki/Pointless_topology "Pointless topology").

[Categorical logic](https://en.wikipedia.org/wiki/Categorical_logic "Categorical logic") is now a well-defined field based on [type theory](https://en.wikipedia.org/wiki/Type_theory "Type theory") for [intuitionistic logics](https://en.wikipedia.org/wiki/Intuitionistic_logic "Intuitionistic logic"), with applications in [functional programming](https://en.wikipedia.org/wiki/Functional_programming "Functional programming") and [domain theory](https://en.wikipedia.org/wiki/Domain_theory "Domain theory"), where a [cartesian closed category](https://en.wikipedia.org/wiki/Cartesian_closed_category "Cartesian closed category") is taken as a non-syntactic description of a [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus "Lambda calculus"). At the very least, category theoretic language clarifies what exactly these related areas have in common (in some [abstract](https://en.wiktionary.org/wiki/abstract "wikt:abstract") sense).

Category theory has been applied in other fields as well, see [applied category theory](https://en.wikipedia.org/wiki/Applied_category_theory "Applied category theory"). For example, [John Baez](https://en.wikipedia.org/wiki/John_Baez "John Baez") has shown a link between [Feynman diagrams](https://en.wikipedia.org/wiki/Feynman_diagrams "Feynman diagrams") in [physics](https://en.wikipedia.org/wiki/Physics "Physics") and monoidal categories.[^10] Another application of category theory, more specifically topos theory, has been made in mathematical music theory, see for example the book *The Topos of Music, Geometric Logic of Concepts, Theory, and Performance* by [Guerino Mazzola](https://en.wikipedia.org/wiki/Guerino_Mazzola "Guerino Mazzola").

[^1]: The name "hom" derives from the fact that the notion of morphism is a generalisation of the notion of [homomorphism](https://en.wikipedia.org/wiki/Homomorphism "Homomorphism"). But even in categories whose objects have no notion of homomorphism or where the morphisms are explicitly not (or not precisely) homomorphisms, the classes ${\displaystyle {\text{hom}}(a,b)}$ are still referred to as hom-classes.

[^2]: Some authors compose in the opposite order, writing *fg* or *f* ∘ *g* for *g* ∘ *f*. Computer scientists using category theory very commonly write *f*; *g* for *g* ∘ *f*

[^3]: A morphism that is both epic and monic is not necessarily an isomorphism. An elementary counterexample: in the category consisting of two objects *A* and *B*, the identity morphisms, and a single morphism *f* from *A* to *B*, *f* is both epic and monic but is not an isomorphism.

[^4]: Marquis, Jean-Pierre (2023), ["Category Theory"](https://plato.stanford.edu/archives/fall2023/entries/category-theory/), in Zalta, Edward N.; Nodelman, Uri (eds.), *The Stanford Encyclopedia of Philosophy* (Fall 2023 ed.), Metaphysics Research Lab, Stanford University, retrieved 2024-04-23

[^5]: Eilenberg, Samuel; Mac Lane, Saunders (1945). ["General theory of natural equivalences"](https://www.ams.org/journals/tran/1945-058-00/S0002-9947-1945-0013131-6/S0002-9947-1945-0013131-6.pdf) (PDF). *Transactions of the American Mathematical Society*. **58**: 247. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/S0002-9947-1945-0013131-6](https://doi.org/10.1090%2FS0002-9947-1945-0013131-6). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0002-9947](https://search.worldcat.org/issn/0002-9947). [Archived](https://ghostarchive.org/archive/20221010/https://www.ams.org/journals/tran/1945-058-00/S0002-9947-1945-0013131-6/S0002-9947-1945-0013131-6.pdf) (PDF) from the original on 2022-10-10.

[^6]: Eilenberg, S.; Mac Lane, S. (1942). ["Group Extensions and Homology"](https://www.jstor.org/stable/1968966). *Annals of Mathematics*. **43** (4): 757–831. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/1968966](https://doi.org/10.2307%2F1968966). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0003-486X](https://search.worldcat.org/issn/0003-486X). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [1968966](https://www.jstor.org/stable/1968966).

[^7]: Marquis, Jean-Pierre (2019). ["Category Theory"](https://plato.stanford.edu/entries/category-theory/). *[Stanford Encyclopedia of Philosophy](https://en.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy")*. Department of Philosophy, [Stanford University](https://en.wikipedia.org/wiki/Stanford_University "Stanford University"). Retrieved 26 September 2022.

[^8]: ["Samuel Eilenberg – Biography"](https://mathshistory.st-andrews.ac.uk/Biographies/Eilenberg/).

[^9]: Reck, Erich (2020). *The Prehistory of Mathematical Structuralism* (1st ed.). Oxford University Press. pp. 215–219. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780190641221](https://en.wikipedia.org/wiki/Special:BookSources/9780190641221 "Special:BookSources/9780190641221").

[^10]: Baez, J.C.; Stay, M. (2010). "Physics, Topology, Logic and Computation: A Rosetta Stone". *New Structures for Physics*. Lecture Notes in Physics. Vol. 813. pp. 95–172. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[0903.0340](https://arxiv.org/abs/0903.0340). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-642-12821-9\_2](https://doi.org/10.1007%2F978-3-642-12821-9_2). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-642-12820-2](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-12820-2 "Special:BookSources/978-3-642-12820-2"). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [115169297](https://api.semanticscholar.org/CorpusID:115169297).

[^11]: [Lawvere, F. William](https://en.wikipedia.org/wiki/William_Lawvere "William Lawvere"); Rosebrugh, Robert (2003). [*Sets for Mathematics*](https://archive.org/details/setsformathemati0000lawv). Cambridge University Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-01060-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-01060-3 "Special:BookSources/978-0-521-01060-3").