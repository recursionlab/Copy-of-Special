---
created: 2026-05-11
psi_tier: zero_divisor
sources:
- Typed lambda calculus - Wikipedia.md
tags:
- zero_divisor
- ingested
title: Typed Lambda Calculus   Wikipedia
type: concept
updated: 2026-05-11
---

# Typed Lambda Calculus   Wikipedia

# Typed lambda calculus - Wikipedia

Jump to contentMain menu    Navigation

Main page

Contents

Current events

Random article

About Wikipedia

Contact us
Contribute

Help

Learn to edit

Community portal

Recent changes

Upload file

Special pages

Search  Donate

Create account

Log in

Donate

Create account

Log in

(Top)
1   Kinds of typed lambda calculi
2   Applications to programming languages
3   See also
4   Notes
5   Further reading

Typed lambda calculus

Ελληνικά

Hrvatski

Íslenska

日本語

Polski

Русский

Українська

中文
Edit links
Tools    Actions

Read

Edit

View history
General

What links here

Related changes

Upload file

Permanent link

Page information

Cite this page

Get shortened URL

Download QR code
Print/export

Download as PDF

Printable version
In other projects

Wikidata item
From Wikipedia, the free encyclopedia   Formalism in computer science
In mathematics and computer science, a typed lambda calculus is a typed formalism that uses the lambda symbol (   λ   {\displaystyle \lambda }   ) to denote anonymous function abstraction. In this context, types are usually objects of a syntactic nature that are assigned to lambda terms; the exact nature of a type depends on the calculus considered (see kinds below). From a certain point of view, typed lambda calculi can be seen as refinements of the untyped lambda calculus, but from another point of view, they can also be considered the more fundamental theory and
untyped lambda calculus
a special case with only one type.[ 1 ]
Typed lambda calculi are foundational programming languages and are the base of typed functional programming languages such as ML and Haskell and, more indirectly, typed imperative programming languages. Typed lambda calculi play an important role in the design of type systems for programming languages; here, typability usually captures desirable properties of the program (e.g., the program will not cause a memory access violation).
Typed lambda calculi are closely related to mathematical logic and proof theory via the Curry–Howard isomorphism and they can be considered as the internal language of certain classes of categories. For example, the simply typed lambda calculus is the language of Cartesian closed categories (CCCs).[ 2 ]

Kinds of typed lambda calculi

[edit]
Various typed lambda calculi have been studied. The simply typed lambda calculus has only one type constructor, the arrow  →   {\displaystyle \to }   , and its only types are basic types and function typesσ   →   τ   {\displaystyle \sigma \to \tau }   . System T extends the simply typed lambda calculus with a type of natural numbers and higher-order primitive recursion; in this system all functions provably computable in Peano arithmetic are definable. System F allows polymorphism by using universal quantification over all types; from a logical perspective it can describe all functions that are provably total in second-order logic. Lambda calculi with dependent types are the base of intuitionistic type theory, the calculus of constructions and the logical framework (LF), a pure lambda calculus with dependent types. Based on work by Berardi on pure type systems, Henk Barendregt proposed the lambda cube to systematize the relations of pure typed lambda calculi (including simply typed lambda calculus, System F, LF and the calculus of constructions).[ 3 ]
Some typed lambda calculi introduce a notion of subtyping, i.e. if  A   {\displaystyle A}    is a subtype of  B   {\displaystyle B}   , then all terms of type  A   {\displaystyle A}    also have type  B   {\displaystyle B}   . Typed lambda calculi with subtyping are the simply typed lambda calculus with conjunctive types and System F<:.
All the systems mentioned so far, with the exception of the untyped lambda calculus, are strongly normalizing: all computations terminate. Therefore, they cannot describe all Turing-computable functions.[ 4 ] As another consequence they are consistent as a logic, i.e. there are uninhabited types. There exist, however, typed lambda calculi that are not strongly normalizing. For example the dependently typed lambda calculus with a type of all types (Type : Type) is not normalizing due to Girard's paradox. This system is also the simplest pure type system, a formalism which generalizes the lambda cube. Systems with explicit recursion combinators, such as Plotkin's "Programming language for Computable Functions" (PCF), are not normalizing, but they are not intended to be interpreted as a logic. Indeed, PCF is a prototypical, typed functional programming language, where types are used to ensure that programs are well-behaved but not necessarily that they are terminating.

Applications to programming languages

[edit]
In computer programming, the routines (functions, procedures, methods) of strongly typed programming languages closely correspond to typed lambda expressions.[ 5 ]

See also

[edit]

Kappa calculus—an analogue of typed lambda calculus which excludes higher-order functions

Notes

[edit]

^Brandl, Helmut (27 April 2024). "Typed Lambda Calculus / Calculus of Constructions"(PDF) .
Calculus of Constructions
. Retrieved  27 April  2024 .

^Lambek, J.; Scott, P. J. (1986),
Introduction to Higher Order Categorical Logic
, Cambridge University Press, ISBN978-0-521-35653-4, MR0856915

^Barendregt, Henk (1991). "Introduction to generalized type systems". Journal of Functional Programming.
1
(2):  125– 154. doi:10.1017/S0956796800020025. hdl:2066/17240. ISSN0956-7968.

^since the halting problem for the latter class was proven to be undecidable

^"What to know before debating type systems | Ovid [blogs.perl.org]".
blogs.perl.org
. Retrieved  2024-04-26 .

Further reading

[edit]

Barendregt, Henk (1992). "Lambda Calculi with Types". In Abramsky, S. (ed.).
Background: Computational Structures
. Handbook of Logic in Computer Science. Vol. 2. Oxford University Press. pp.  117– 309. ISBN9780198537618.

Brandl, Helmut (2022). Calculus of Constructions / Typed Lambda Calculus
Retrieved from "
https://en.wikipedia.org/w/index.php?title=Typed_lambda_calculus&oldid=1318206586
"  Categories:

Lambda calculus

Logic in computer science

Theory of computation

Type theory
Hidden categories:

Articles with short description

Short description is different from Wikidata


## Related

- [[The Calculus of Recursive Collapse and Stabili]]
- [[Paradox Handling Frameworks in Recursive Logic]]

- [[Lambda Coherence Engine]]
- [[Type System]]



---

*Source: `Typed lambda calculus - Wikipedia.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
