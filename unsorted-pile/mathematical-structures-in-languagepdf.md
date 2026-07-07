---
stub: true
title: "Mathematical Structures In Language.Pdf"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [obstruction_class, "ingested"]
sources: ["Mathematical Structures in Language.pdf.md"]
psi_tier: obstruction_class
---

# Mathematical Structures In Language.Pdf

# Mathematical Structures in Language.pdf

Mathematical Structures in

Language

Edward L. Keenan Lawrence S. Moss
December 9, 2009
CENTER FOR THE STUDY OF LANGUAGE AND INFORMATION

Contents

1 The Roots of Infinity 1
1.1 The Roots of Infinity in Natural Language 2
1.2 Boolean Compounding 22
1.3 References 24
2 Some Mathematical Background 25
2.1 More about Sets 25
2.2 Sequences 31
2.3 Functions and Sequences 35
2.4 Arbitrary Unions and Intersections 38
2.5 Definitions by Closure (Recursion) 38
2.6 Bijections and the Sizes of Cross Products 42
2.7 Suggestions for Further Study 45
2.8 Addendum: Russell’s Paradox 45
3 Syntax I: Trees and Order Relations 47
3.1 Trees 48
3.2 C-command 60
3.3 Sameness of Structure: Isomorphism 63
3.4 Labeled Trees 67
3.5 Ordered Trees 72
4 Syntax II: Design for a Language 87
4.1 Beginning Grammar 88
4.2 Manner Adverbs 95
4.3 Relative Clauses 106
v
vi / Mathematical Structures in Language
5 Syntax III: Linguistic Invariants and Language Variation 115
5.1 A Model Grammar and Some Basic Theorems 116
5.2 A Semantic Definition of Anaphor 124
5.3 A Model of Korean 126
5.4 Toba Batak 131
5.5 Some Mathematical Properties of Grammars and their Invariants 134
5.6 Invariants of Type 0 136
5.7 Invariants of Type (1) 138
5.8 Invariants of Type (2) and higher 140
5.9 Structure Preserving Operations on Grammars 146
5.10 Addendum 147
6 A Taste of Mathematical linguistics 149
6.1 Regular Expressions and Languages 151
6.2 Simple Categorial Grammars 153
6.3 Finite-state Automata 156
6.4 More About Regular Languages 162
6.5 An Argument Why English is Not Regular 165
6.6 Context-Free Grammars and Languages 166
7 Semantics I: Compositionality and Sentential Logic 171
7.1 Compositionality and Natural Language Semantics 171
7.2 Sentential Logic 179
7.3 Interpreting a Fragment of English 192
8 Semantics II: Coordination, Negation and Lattices 209
8.1 Coordination: Syntax 210
8.2 Coordination: Semantics 212
8.3 Negation and Additional Properties of Natural Language Lattices 221
8.4 Properties versus Sets: Lattice Isomorphisms 226
8.5 Theorems on Boolean Lattices 230
8.6 A Concluding Note on Point of View 230
8.7 Further Reading 232
Contents / vii
9 Semantics III: Logic and Variable Binding Operators 233
9.1 Translation Semantics 233
9.2 Some General Linguistic Properties of First Order Logic (FOL) 250
9.3 Extending the Class of VBO’s: the Lambda Operator 261
10 Semantics IV: DPs, Monotonicity and Semantic Generalizations 279
10.1 Negative Polarity Items 279
10.2 Monotonicity 283
10.3 Semantic Generalizations 291
10.4 Historical Background 295
11 Semantics V: Classifying Quantifiers 301
11.1 Quantifier Types 303
11.2 Generalizations Concerning Det denotations 313
11.3 k-Place Dets 318
11.4 Crossing the Frege Boundary 322
11.5 A Classic Syntactic Problem 323
11.6 Adverbial Quantification 325
11.7 Concluding Remarks 329
11.8 Historical Background 329
11.9 Appendix: Some types of English Determiners 330
References 333

Preface

The purpose of this book is twofold: First, we present elementary math-ematical background to help the student of linguistics formulate gener-alizations concerning the structure of languages, most particularly syn-tactic and semantic structure. This is a goal we fully share with Partee et al. (1990), a book with similar goals to our own. And to stress a basic point: the background mathematical work we present is well known and well understood. The primary loci of this material is in Chapters 2, 3, 6, 7 and 9. But the linguistic phenomena we study are much less well understood—they are what we are trying to understand. A major step in understanding is formulating what we are trying to understand in terms of things we already understand, hence the drive towards mathe-matical formulation. This enables us to notice and formulate linguistic regularities in a clear and precise way, enabling us to study, correct, test and generalize them. So this is the core answer to a question we’re frequently asked “Why study language mathematically?”.
Our second purpose follows upon the first but is considerably more speculative. Namely, once our mathematical description of linguistic phenomena is sufficiently developed, we can not only model properties of natural language, we can study our models to derive properties and generalizations that were largely unthought of in the absence of a way to say them. Sometimes these generalizations are quite simple: “Lexi-cal NPs (proper nouns) denote monotone increasing functions”. Others are deeper: “Lexical NP denotations are complete boolean generators for the full set of possible NP denotations”. Chapters 5, 8, 10, and 11 here focus on such generalizations. Formulating them is exciting: looking at our world through mathematical lenses enables us to see vistas heretofore unsuspected. But of course, no sooner are new gener-alizations formulated than new empirical work challenges them, forcing refinements and extensions, so the half-life of a new generalization is
ix
x / Mathematical Structures in Language
relatively short. But this is the result of a healthy feedback relation between theory and observation.
We invite you to criticize our proposed generalizations and welcome you to Linguistics!
Helpful Hints on How to Read this Book Chapter 1 just intro-duces the reader to iterative processes in natural language. Learning a few good examples plus the form of argument that the set of expres-sions of English is infinite is all that is needed from this chapter. The material in Chapter 2 is used throughout the book, but it is standard, and readers with some mathematics background should read it quickly. Chapters 3 and 4 illustrate some basic syntactic formalization, broadly presupposed in Chapter 5. Chapter 5 itself, especially the second half, is a bit advanced for an introductory work and might be omitted on first reading. The chapter on formal language theory is largely self contained (though it uses the earlier formal work from Chapter 2). Chapters 7 through 11 are all semantic with each presupposing the previous ones, though Chapter 9 is relatively self-contained. Chapters 10 and 11 have fewer exercises than the others and focus more on empirical generaliza-tions we can make using the mathematical notions we have developed.
Words of Thanks We thank our classes over the years for helping us to develop the material. Both authors would like to thank Uwe Moennich, Richard Oehrle, and Jeff Heinz for comments on a much earlier version of this manuscript. As well we both owe a debt to Nico-las LaCasse not only for the fine LaTeX presentation, but for several reorganizational changes that improved the clarity of presentation. In addition, Edward Keenan would like especially to thank his wife Carol Archie for having made it all possible and suffering through endless weekends of an apparently endless effort. She still thinks we should call the book Sex, Lies and Language. Larry Moss thanks Hans-Joerg Tiede for teaching a version of the material many years ago and for many discussions over the years about pedagogic issues in the area. He also thanks Madi Hirschland for her unfailing love and support, and for continuing to remind him that as beautiful as language and math-ematics are, there are many other aspects of the world that need to be understood and even changed.
1

The Roots of Infinity

We begin our study with a fundamental query of modern Linguistics:
(1) How do speakers of a natural language produce and understand novel expressions?

Natural languages
are ones like English, Japanese, Swahili, . . . which human beings grow up speaking naturally as their normal means of communication. There are about 5,500 such languages currently spo-ken in the world1. Natural languages contrast with
artificial languages
consciously created for special purposes. These include
programming languages
such as Lisp, C++ and Prolog and
mathematical languages
such as Sentential Logic and Elementary Arithmetic studied in math-ematical logic. The study of natural language syntax and semantics has benefited much from the study of these much simpler and better understood artificial languages.
The crucial phrase in (1) is
novel.
An ordinary speaker is
competent
to produce and understand arbitrarily many expressions he or she has never specifically heard before and so certainly has never explicitly learned. This chapter is devoted to supporting this claim, introducing some descriptive mathematical notions and notations as needed.
In the next chapter we initiate the study of the linguists’ response to the fundamental query: namely, that speakers have internalized a
grammar
for their language. That grammar consists of a set of
lexical items
– meaningful words and morphemes – and some
rules
which allow us to combine lexical items to form arbitrarily many complex expressions whose semantic interpretation is determined by that of the expressions they are formed from. We produce, recognize and interpret novel expressions by using our internalized grammar to recognize how
1This figure is “rough” for both empirical and conceptual reasons. For example, how different may two speech varieties be and still count as dialects of the same language as opposed to different languages?
1
2 / Mathematical Structures in Language
the expressions are constructed, and how expressions constructed in that way take their meaning as a function of the meanings of what they are constructed from – ultimately the lexical items they are built from. This last feature is known as
Compositionality.

In designing grammars of this sort for natural languages we are pulled by several partially antagonistic forces: Empirical Adequacy (Completeness, Soundness, Interpretability) on the one hand, and Uni-versality on the other. Regarding the former, for each natural language L the grammar we design for L must be
complete:
it generates
all
the expressions native speakers judge grammatical; it must be
sound:
it
only
generates expressions judged grammatical, and it must be
inter-pretable:
the lexical items and derived expressions must be semantically interpreted. Even in this chapter we see cases where different ways of constructing the same expression may lead to different ways of semanti-cally interpreting it. Finally, linguists feel strongly that the structure of our languages reflects the structure of our minds, and in consequence, at some deep level, grammars of different languages should share many structural properties. Thus in designing a grammar for one language we are influenced by work that linguists do with other languages and we try to design our (partial) grammars so that they are similar (they cannot of course be identical, since English, Japanese, Swahili, . . . are not identical).
1.1 The Roots of Infinity in Natural Language
Here we exhibit a variety of types of expression in English which support the conclusion that competent speakers of English can pro-duce, recognize and understand unboundedly many expressions. What is meant by
unboundedly many
or
arbitrarily many?
In the present context we mean simply
infinitely many
in the mathematical sense. Consider for example the set N of natural numbers, that set whose members (elements) are the familiar 0, 1, 2, . . .. Clearly N has in-finitely many members, as they “continue forever, without end”. A less poetic way to say that is: a set L is
infinite
if and only if for each natu-ral number k, L has more than k members. By this informal but usable definition we can reason that N is infinite: no matter what number k we pick, the numbers 0, 1,. . . , k constitute more than k elements of N; in fact precisely k + 1 elements. So for any k, N has more than k ele-ments. This
proves
that N is an infinite set according to our definition of
infinite.

Jargon In mathematical discourse
if and only if,
usually abbreviated
iff,
combines two sentences to form a third. P
iff
Q means that P and
The Roots of Infinity / 3
Q always have the same truth value: in an arbitrary situation s they are both true in s or both false in s.
iff
is often used in definitions, as there the term we are defining occurs in the sentence on the left of
iff
and the sentence we use to define that term occurs on the right, and the purpose of the definition is to say that whenever we use the word being defined, we may replace it by the definition which follows.
When are sets the same? In what follows we shall often be inter-ested in defining sets—for example, sets of English expressions with various properties. So it will be important to know when two appar-ently different definitions define the
same
set. We say that sets X and Y are
the same
iff they have the same members2. For example, let X be the set whose members are the numbers 1, 2, 3, and 4. And let Y be the set whose members are the positive integers less than 5. Clearly X and Y have the same members and so are the same set. To say that X and Y are the same set we write X = Y read as “X equals Y ”. And to say that X and Y are
different
sets we write X 6= Y , read as “X does not equal Y ”. Observe that X 6= Y iff one of the sets X,Y has a member the other doesn’t have. Were this condition to fail then X and Y would have the same members and thus be the same set (X = Y ).
On sets and their sizes. The number of elements in a set X is noted |X| and is called the
cardinality
of X. We first consider finite sets. A set X is
finite
iff for some natural number k, X has exactly k elements. That is, |X| = k. This definition is in practice useful and easy to apply. For example, the set whose elements are just the letters a, b, and c is finite, as it has exactly three elements. This set is usually noted {a, b, c}, where we list the names of the elements separated by commas, with the whole list enclosed in curly brackets (not angled brackets, not round brackets or parentheses). To say that an object x is a member (element) of a set A we write x ∈ A, using a stylized Greek epsilon to denote the membership relation. For example, 3 ∈ {1, 3, 5, 7}. To say that x is not a member of A we write x /∈ A. For example, 2 /∈ {1, 3, 5, 7}.
One finite set of special interest is the
empty
set, also called the
null
set, and noted ∅. It is that set with no members. Note that there could not be two different empty sets, for then one would have to have a member that the other didn’t, so it would have a member and thus not be empty.
We have already mentioned that the set N of natural numbers is infinite. Sometimes we refer to it with a
pseudolist
such as {0, 1, 2, . . .}
2In fact this criterion for identity of sets is one of the axioms (the Axiom of
Extensionality) of Set Theory. It reads: For all sets A,B A = B iff for all x, x ∈ A iff x ∈ B.
4 / Mathematical Structures in Language
where the three dots means simply that “the reader knows how to continue the list”. This is a useful notation when in fact we know how to continue the list. But it does not count as a definition since there are many ways the initial explicitly given segment of the list, namely 0, 1, 2, could be continued. Here we take it that in practice the reader has a working familiarity of the natural numbers. For example 2 ∈ N, but 1
2 /∈ N. We demonstrate shortly that English has infinitely many expres-
sions. To show this we consider three ways of showing that a set A is infinite. The first we have already seen: show that for every natural number k, A has more than k elements. This is how we convinced our-selves (if we needed convincing) that the set N of natural numbers was infinite. A second way uses the very useful subset relation, defined as follows:
Definition 1.1. A set A is a
subset
of a set B, noted A ⊆ B, iff every element of A is also an element of B. More formally, A ⊆ B iff for all objects x, if x ∈ A then x ∈ B.
When A ⊆ B, it is possible that A = B, for then every element of A is, trivially, an element of B. But it is also possible that B has some element(s) not in A, in which case we say that A is a

[... content truncated ...]

---

*Source: `Mathematical Structures in Language.pdf.md` | Ingested: 2026-05-11 | Ψ-tier: obstruction_class*
