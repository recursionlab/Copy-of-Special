---
title: "Dependency grammar"
source: "https://en.wikipedia.org/wiki/Dependency_grammar"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2004-10-12
created: 2026-04-10
description:
tags:
  - "clippings"
---
**Dependency grammar** (**DG**) is a class of modern [grammatical](https://en.wikipedia.org/wiki/Grammar "Grammar") theories that are all based on the dependency relation (as opposed to the *constituency relation* of [phrase structure](https://en.wikipedia.org/wiki/Phrase_structure_grammar "Phrase structure grammar")) and that can be traced back primarily to the work of [Lucien Tesnière](https://en.wikipedia.org/wiki/Lucien_Tesni%C3%A8re "Lucien Tesnière"). Dependency is the notion that linguistic units, e.g. words, are connected to each other by directed links. The (finite) verb is taken to be the structural center of clause structure. All other syntactic units (words) are either directly or indirectly connected to the verb in terms of the directed links, which are called *dependencies*. Dependency grammar differs from [phrase structure grammar](https://en.wikipedia.org/wiki/Phrase_structure_grammar "Phrase structure grammar") in that while it can identify phrases it tends to overlook phrasal nodes. A dependency structure is determined by the relation between a word (a [head](https://en.wikipedia.org/wiki/Head_\(linguistics\) "Head (linguistics)")) and its dependents. Dependency structures are flatter than phrase structures in part because they lack a [finite](https://en.wikipedia.org/wiki/Finite_verb "Finite verb") [verb phrase](https://en.wikipedia.org/wiki/Verb_phrase "Verb phrase") [constituent](https://en.wikipedia.org/wiki/Constituent_\(linguistics\) "Constituent (linguistics)"), and they are thus well suited for the analysis of languages with free word order, such as [Czech](https://en.wikipedia.org/wiki/Czech_language "Czech language") or [Warlpiri](https://en.wikipedia.org/wiki/Warlpiri_language "Warlpiri language").

## History

The notion of dependencies between grammatical units has existed since the earliest recorded grammars, e.g. [Pāṇini](https://en.wikipedia.org/wiki/P%C4%81%E1%B9%87ini "Pāṇini"), and the dependency concept therefore arguably predates that of phrase structure by many centuries.[^1] [Ibn Maḍāʾ](https://en.wikipedia.org/wiki/Ibn_Ma%E1%B8%8D%C4%81%CA%BE "Ibn Maḍāʾ"), a 12th-century [linguist](https://en.wikipedia.org/wiki/Linguist "Linguist") from [Córdoba, Andalusia](https://en.wikipedia.org/wiki/C%C3%B3rdoba,_Andalusia "Córdoba, Andalusia"), may have been the first grammarian to use the term *dependency* in the grammatical sense that we use it today. In early modern times, the dependency concept seems to have coexisted side by side with that of phrase structure, the latter having entered Latin, French, English and other grammars from the widespread study of [term logic](https://en.wikipedia.org/wiki/Term_logic "Term logic") of antiquity.[^2] Dependency is also concretely present in the works of [Sámuel Brassai](https://en.wikipedia.org/wiki/S%C3%A1muel_Brassai "Sámuel Brassai") (1800–1897), a Hungarian linguist, [Franz Kern](https://de.wikipedia.org/wiki/Franz_Kern_\(Philologe\) "de:Franz Kern (Philologe)") (1830–1894), a German philologist, and of [Heimann Hariton Tiktin](https://en.wikipedia.org/wiki/Heimann_Hariton_Tiktin "Heimann Hariton Tiktin") (1850–1936), a Romanian linguist.[^3]

Modern dependency grammars, however, begin primarily with the work of Lucien Tesnière. Tesnière was a Frenchman, a [polyglot](https://en.wikipedia.org/wiki/Polyglot "Polyglot"), and a professor of linguistics at the universities in Strasbourg and Montpellier. His major work *Éléments de syntaxe structurale* was published posthumously in 1959 – he died in 1954. The basic approach to syntax he developed has at least partially influenced the work of others in the 1960s, although it is not clear in what way these works were inspired by other sources.[^4] A number of other dependency-based grammars have gained prominence since those early works.[^5] DG has generated a lot of interest in Germany [^6] in both theoretical syntax and language pedagogy. In recent years, the great development surrounding dependency-based theories has come from [computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics "Computational linguistics") and is due, in part, to the influential work that [David Hays](https://en.wikipedia.org/wiki/David_G._Hays "David G. Hays") did in machine translation at the [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation "RAND Corporation") in the 1950s and 1960s. Dependency-based systems are increasingly being used to parse natural language and generate [tree banks](https://en.wikipedia.org/wiki/Treebank "Treebank"). Interest in dependency grammar is growing at present, international conferences on dependency linguistics being a relatively recent development ([Depling 2011](http://depling.org/), [Depling 2013](http://ufal.mff.cuni.cz/depling13/), [Depling 2015](http://depling.org/depling2015/), [Depling 2017](http://www.depling.org/depling2017/call.html), [Depling 2019](http://www.depling.org/depling2019/) [Archived](https://web.archive.org/web/20190306111358/http://www.depling.org/depling2019/) 2019-03-06 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")).

## Dependency vs. phrase structure

Dependency is a one-to-one correspondence: for every element (e.g. word or morph) in the sentence, there is exactly one node in the structure of that sentence that corresponds to that element. The result of this one-to-one correspondence is that dependency grammars are word (or morph) grammars. All that exist are the elements and the dependencies that connect the elements into a structure. This situation should be compared with [phrase structure](https://en.wikipedia.org/wiki/Phrase_structure_grammar "Phrase structure grammar"). Phrase structure is a one-to-one-or-more correspondence, which means that, for every element in a sentence, there are one or more nodes in the structure that correspond to that element. The result of this difference is that dependency structures are minimal [^7] compared to their phrase structure counterparts, since they tend to contain many fewer nodes.

![Dependency vs. phrase structure](https://upload.wikimedia.org/wikipedia/commons/0/0d/Wearetryingtounderstandthedifference_%282%29.jpg)

Dependency vs. phrase structure

These trees illustrate two possible ways to render the dependency and phrase structure relations (see below). This dependency tree is an "ordered" tree, i.e. it reflects actual word order. Many dependency trees abstract away from linear order and focus just on hierarchical order, which means they do not show actual word order. This constituency (= phrase structure) tree follows the conventions of [bare phrase structure](https://en.wikipedia.org/wiki/Minimalist_program "Minimalist program") (BPS), whereby the words themselves are employed as the node labels.

The distinction between dependency and phrase structure grammars derives in large part from the initial division of the clause. The phrase structure relation derives from an initial binary division, whereby the clause is split into a subject [noun phrase](https://en.wikipedia.org/wiki/Noun_phrase "Noun phrase") (NP) and a [predicate](https://en.wikipedia.org/wiki/Predicate_\(grammar\) "Predicate (grammar)") [verb phrase](https://en.wikipedia.org/wiki/Verb_phrase "Verb phrase") (VP). This division is certainly present in the basic analysis of the clause that we find in the works of, for instance, [Leonard Bloomfield](https://en.wikipedia.org/wiki/Leonard_Bloomfield "Leonard Bloomfield") and [Noam Chomsky](https://en.wikipedia.org/wiki/Noam_Chomsky "Noam Chomsky"). Tesnière, however, argued vehemently against this binary division, preferring instead to position the verb as the root of all clause structure. Tesnière's stance was that the subject-predicate division stems from [term logic](https://en.wikipedia.org/wiki/Term_logic "Term logic") and has no place in linguistics.[^8] The importance of this distinction is that if one acknowledges the initial subject-predicate division in syntax as real, then one is likely to go down the path of phrase structure grammar, while if one rejects this division, then one must consider the verb as the root of all structure, and so go down the path of dependency grammar.

## Dependency grammars

The following frameworks are dependency-based:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Quranic-arabic-corpus.png/250px-Quranic-arabic-corpus.png)

Hybrid constituency/dependency tree from the Quranic Arabic Corpus

- [Algebraic syntax](https://en.wikipedia.org/wiki/Algebraic_syntax "Algebraic syntax")
- [Operator grammar](https://en.wikipedia.org/wiki/Operator_grammar "Operator grammar")
- [Link grammar](https://en.wikipedia.org/wiki/Link_grammar "Link grammar")
- [Functional generative description](https://en.wikipedia.org/wiki/Functional_generative_description "Functional generative description")
- [Lexicase](https://en.wikipedia.org/wiki/Lexicase "Lexicase")
- [Meaning–text theory](https://en.wikipedia.org/wiki/Meaning%E2%80%93text_theory "Meaning–text theory")
- [Word grammar](https://en.wikipedia.org/wiki/Word_grammar "Word grammar")
- [Extensible dependency grammar](http://www.ps.uni-saarland.de/~rade/xdg.html)
- [Universal Dependencies](https://en.wikipedia.org/wiki/Universal_Dependencies "Universal Dependencies")

[Link grammar](https://en.wikipedia.org/wiki/Link_grammar "Link grammar") is similar to dependency grammar, but link grammar does not include directionality between the linked words, and thus does not describe head-dependent relationships. Hybrid dependency/phrase structure grammar uses dependencies between words, but also includes dependencies between phrasal nodes – see for example the [Quranic Arabic Dependency Treebank](https://en.wikipedia.org/wiki/Quranic_Arabic_Corpus "Quranic Arabic Corpus"). The derivation trees of [tree-adjoining grammar](https://en.wikipedia.org/wiki/Tree-adjoining_grammar "Tree-adjoining grammar") are dependency structures, although the full trees of TAG rendered in terms of phrase structure, so in this regard, it is not clear whether TAG should be viewed more as a dependency or phrase structure grammar.

There are major differences between the grammars just listed. In this regard, the dependency relation is compatible with other major tenets of theories of grammar. Thus like phrase structure grammars, dependency grammars can be mono- or multistratal, representational or derivational, construction- or rule-based.

## Representing dependencies

There are various conventions that DGs employ to represent dependencies. The following schemata (in addition to the tree above and the trees further below) illustrate some of these conventions:

![Conventions for illustrating dependencies](https://upload.wikimedia.org/wikipedia/commons/9/9e/Conventions.jpg)

Conventions for illustrating dependencies

The representations in (a–d) are trees, whereby the specific conventions employed in each tree vary. Solid lines are *dependency edges* and lightly dotted lines are *projection lines*. The only difference between tree (a) and tree (b) is that tree (a) employs the category class to label the nodes whereas tree (b) employs the words themselves as the node labels.[^9] Tree (c) is a reduced tree insofar as the string of words below and projection lines are deemed unnecessary and are hence omitted. Tree (d) abstracts away from linear order and reflects just hierarchical order.[^10] The arrow arcs in (e) are an alternative convention used to show dependencies and are favored by [Word Grammar](https://en.wikipedia.org/wiki/Word_grammar "Word grammar").[^11] The brackets in (f) are seldom used, but are nevertheless quite capable of reflecting the dependency hierarchy; dependents appear enclosed in more brackets than their heads. And finally, the indentations like those in (g) are another convention that is sometimes employed to indicate the hierarchy of words.[^12] Dependents are placed underneath their heads and indented. Like tree (d), the indentations in (g) abstract away from linear order.

The point to these conventions is that they are just that, namely conventions. They do not influence the basic commitment to dependency as the relation that is grouping syntactic units.

## Types of dependencies

The dependency representations above (and further below) show syntactic dependencies. Indeed, most work in dependency grammar focuses on syntactic dependencies. Syntactic dependencies are, however, just one of three or four types of dependencies. [Meaning–text theory](https://en.wikipedia.org/wiki/Meaning%E2%80%93text_theory "Meaning–text theory"), for instance, emphasizes the role of semantic and morphological dependencies in addition to syntactic dependencies.[^13] A fourth type, prosodic dependencies, can also be acknowledged. Distinguishing between these types of dependencies can be important, in part because if one fails to do so, the likelihood that semantic, morphological, and/or prosodic dependencies will be mistaken for syntactic dependencies is great. The following four subsections briefly sketch each of these dependency types. During the discussion, the existence of syntactic dependencies is taken for granted and used as an orientation point for establishing the nature of the other three dependency types.

### Semantic dependencies

Semantic dependencies are understood in terms of [predicates](https://en.wikipedia.org/wiki/Predicate_\(grammar\) "Predicate (grammar)") and their [arguments](https://en.wikipedia.org/wiki/Argument_\(linguistics\) "Argument (linguistics)").[^14] The arguments of a predicate are semantically dependent on that predicate. Often, semantic dependencies overlap with and point in the same direction as syntactic dependencies. At times, however, semantic dependencies can point in the opposite direction of syntactic dependencies, or they can be entirely independent of syntactic dependencies. The hierarchy of words in the following examples show standard syntactic dependencies, whereas the arrows indicate semantic dependencies:

![Semantic dependencies](https://upload.wikimedia.org/wikipedia/commons/a/ac/Semantic_dependencies.png)

Semantic dependencies

The two arguments *Sam* and *Sally* in tree (a) are dependent on the predicate *likes*, whereby these arguments are also syntactically dependent on *likes*. What this means is that the semantic and syntactic dependencies overlap and point in the same direction (down the tree). Attributive adjectives, however, are predicates that take their head noun as their argument, hence *big* is a predicate in tree (b) that takes *bones* as its one argument; the semantic dependency points up the tree and therefore runs counter to the syntactic dependency. A similar situation obtains in (c), where the preposition predicate *on* takes the two arguments *the picture* and *the wall*; one of these semantic dependencies points up the syntactic hierarchy, whereas the other points down it. Finally, the predicate *to help* in (d) takes the one argument *Jim* but is not directly connected to *Jim* in the syntactic hierarchy, which means that semantic dependency is entirely independent of the syntactic dependencies.

### Morphological dependencies

Morphological dependencies obtain between words or parts of words.[^15] When a given word or part of a word influences the form of another word, then the latter is morphologically dependent on the former. Agreement and concord are therefore manifestations of morphological dependencies. Like semantic dependencies, morphological dependencies can overlap with and point in the same direction as syntactic dependencies, overlap with and point in the opposite direction of syntactic dependencies, or be entirely independent of syntactic dependencies. The arrows are now used to indicate morphological dependencies.

![Morphological dependencies 1](https://upload.wikimedia.org/wikipedia/commons/6/6b/Mophological_dependencies_1.png)

Morphological dependencies 1

The plural *houses* in (a) demands the plural of the demonstrative determiner, hence *these* appears, not *this*, which means there is a morphological dependency that points down the hierarchy from *houses* to *these*. The situation is reversed in (b), where the singular subject *Sam* demands the appearance of the agreement suffix *\-s* on the finite verb *works*, which means there is a morphological dependency pointing up the hierarchy from *Sam* to *works*. The type of determiner in the German examples (c) and (d) influences the inflectional suffix that appears on the adjective *alt*. When the indefinite article *ein* is used, the strong masculine ending *\-er* appears on the adjective. When the definite article *der* is used, in contrast, the weak ending *\-e* appears on the adjective. Thus since the choice of determiner impacts the morphological form of the adjective, there is a morphological dependency pointing from the determiner to the adjective, whereby this morphological dependency is entirely independent of the syntactic dependencies. Consider further the following French sentences:

![Morphological dependencies 2'](https://upload.wikimedia.org/wikipedia/commons/e/e5/Morphological_dependencies_2%27.png)

Morphological dependencies 2'

The masculine subject *le chien* in (a) demands the masculine form of the predicative adjective *blanc*, whereas the feminine subject *la maison* demands the feminine form of this adjective. A morphological dependency that is entirely independent of the syntactic dependencies therefore points again across the syntactic hierarchy.

Morphological dependencies play an important role in [typological studies](https://en.wikipedia.org/wiki/Linguistic_typology "Linguistic typology"). Languages are classified as mostly [head-marking](https://en.wikipedia.org/wiki/Head-marking_language "Head-marking language") (*Sam work-s*) or mostly [dependent-marking](https://en.wikipedia.org/wiki/Dependent-marking_language "Dependent-marking language") (*these houses*), whereby most if not all languages contain at least some minor measure of both head and dependent marking.[^16]

### Prosodic dependencies

Prosodic dependencies are acknowledged in order to accommodate the behavior of [clitics](https://en.wikipedia.org/wiki/Clitic "Clitic").[^17] A clitic is a syntactically autonomous element that is prosodically dependent on a host. A clitic is therefore integrated into the prosody of its host, meaning that it forms a single word with its host. Prosodic dependencies exist entirely in the linear dimension (horizontal dimension), whereas standard syntactic dependencies exist in the hierarchical dimension (vertical dimension). Classic examples of clitics in English are reduced auxiliaries (e.g. *\-ll*, *\-s*, *\-ve*) and the possessive marker *\-s*. The prosodic dependencies in the following examples are indicated with hyphens and the lack of a vertical projection line:

![Prosodic dependencies'](https://upload.wikimedia.org/wikipedia/commons/5/55/Prosodic_dependencies%27.png)

Prosodic dependencies'

A hyphen that appears on the left of the clitic indicates that the clitic is prosodically dependent on the word immediately to its left (*He'll*, *There's*), whereas a hyphen that appears on the right side of the clitic (not shown here) indicates that the clitic is prosodically dependent on the word that appears immediately to its right. A given clitic is often prosodically dependent on its syntactic dependent (*He'll*, *There's*) or on its head (*would've*). At other times, it can depend prosodically on a word that is neither its head nor its immediate dependent (*Florida's*).

### Syntactic dependencies

Syntactic dependencies are the focus of most work in DG, as stated above. How the presence and the direction of syntactic dependencies are determined is of course often open to debate. In this regard, it must be acknowledged that the validity of syntactic dependencies in the trees throughout this article is being taken for granted. However, these hierarchies are such that many DGs can largely support them, although there will certainly be points of disagreement. The basic question about how syntactic dependencies are discerned has proven difficult to answer definitively. One should acknowledge in this area, however, that the basic task of identifying and discerning the presence and direction of the syntactic dependencies of DGs is no easier or harder than determining the constituent groupings of phrase structure grammars. A variety of heuristics are employed to this end, basic [tests for constituents](https://en.wikipedia.org/wiki/Constituent_\(linguistics\) "Constituent (linguistics)") being useful tools; the syntactic dependencies assumed in the trees in this article are grouping words together in a manner that most closely matches the results of standard permutation, substitution, and ellipsis tests for constituents. [Etymological](https://en.wikipedia.org/wiki/Etymology "Etymology") considerations also provide helpful clues about the direction of dependencies. A promising principle upon which to base the existence of syntactic dependencies is distribution.[^18] When one is striving to identify the root of a given phrase, the word that is most responsible for determining the distribution of that phrase as a whole is its root.

## Linear order and discontinuities

Traditionally, DGs have had a different approach to linear order (word order) than phrase structure grammars. Dependency structures are minimal compared to their phrase structure counterparts, and these minimal structures allow one to focus intently on the two ordering dimensions.[^19] Separating the vertical dimension (hierarchical order) from the horizontal dimension (linear order) is easily accomplished. This aspect of dependency structures has allowed DGs, starting with Tesnière (1959), to focus on hierarchical order in a manner that is hardly possible for phrase structure grammars. For Tesnière, linear order was secondary to hierarchical order insofar as hierarchical order preceded linear order in the mind of a speaker. The stemmas (trees) that Tesnière produced reflected this view; they abstracted away from linear order to focus almost entirely on hierarchical order. Many DGs that followed Tesnière adopted this practice, that is, they produced tree structures that reflect hierarchical order alone, e.g.

![Two unordered trees](https://upload.wikimedia.org/wikipedia/commons/3/39/Dg-new-1.jpg)

Two unordered trees

The traditional focus on hierarchical order generated the impression that DGs have little to say about linear order, and it has contributed to the view that DGs are particularly well-suited to examine languages with free word order. A negative result of this focus on hierarchical order, however, is that there is a dearth of DG explorations of particular word order phenomena, such as of standard [discontinuities](https://en.wikipedia.org/wiki/Discontinuity_\(linguistics\) "Discontinuity (linguistics)"). Comprehensive dependency grammar accounts of [topicalization](https://en.wikipedia.org/wiki/Topicalization "Topicalization"), [*wh* -fronting](https://en.wikipedia.org/wiki/Wh-movement "Wh-movement"), [scrambling](https://en.wikipedia.org/wiki/Scrambling_\(linguistics\) "Scrambling (linguistics)"), and [extraposition](https://en.wikipedia.org/wiki/Extraposition "Extraposition") are mostly absent from many established DG frameworks. This situation can be contrasted with phrase structure grammars, which have devoted tremendous effort to exploring these phenomena.

The nature of the dependency relation does not, however, prevent one from focusing on linear order. Dependency structures are as capable of exploring word order phenomena as phrase structures. The following trees illustrate this point; they represent one way of exploring discontinuities using dependency structures. The trees suggest the manner in which common discontinuities can be addressed. An example from German is used to illustrate a scrambling [discontinuity](https://en.wikipedia.org/wiki/Discontinuity_\(linguistics\) "Discontinuity (linguistics)"):

![8 ordered trees](https://upload.wikimedia.org/wikipedia/commons/6/6d/Dg-new-2.jpg)

8 ordered trees

The a-trees on the left show [projectivity](https://en.wikipedia.org/wiki/Discontinuity_\(linguistics\) "Discontinuity (linguistics)") violations (= crossing lines), and the b-trees on the right demonstrate one means of addressing these violations. The displaced constituent takes on a word as its [head](https://en.wikipedia.org/wiki/Head_\(linguistics\) "Head (linguistics)") that is not its [governor](https://en.wikipedia.org/wiki/Government_\(linguistics\) "Government (linguistics)"). The words in red mark the [catena](https://en.wikipedia.org/wiki/Catena_\(linguistics\) "Catena (linguistics)") (=chain) of words that extends from the root of the displaced constituent to the [governor](https://en.wikipedia.org/wiki/Government_\(linguistics\) "Government (linguistics)") of that constituent.[^20] Discontinuities are then explored in terms of these catenae. The limitations on topicalization, *wh* -fronting, scrambling, and extraposition can be explored and identified by examining the nature of the catenae involved.

## Syntactic functions

Traditionally, DGs have treated the syntactic functions (= grammatical functions, [grammatical relations](https://en.wikipedia.org/wiki/Grammatical_relation "Grammatical relation")) as primitive. They posit an inventory of functions (e.g. subject, object, oblique, determiner, attribute, predicative, etc.). These functions can appear as labels on the dependencies in the tree structures, e.g.[^21]

![Syntactic functions 1](https://upload.wikimedia.org/wikipedia/commons/c/c3/Syntactic_functions_1.png)

Syntactic functions 1

The syntactic functions in this tree are shown in green: ATTR (attribute), COMP-P (complement of preposition), COMP-TO (complement of to), DET (determiner), P-ATTR (prepositional attribute), PRED (predicative), SUBJ (subject), TO-COMP (to complement). The functions chosen and abbreviations used in the tree here are merely representative of the general stance of DGs toward the syntactic functions. The actual inventory of functions and designations employed vary from DG to DG.

As a primitive of the theory, the status of these functions is very different from that in some phrase structure grammars. Traditionally, phrase structure grammars derive the syntactic functions from the constellation. For instance, the object is identified as the NP appearing inside finite VP, and the subject as the NP appearing outside of finite VP. Since DGs reject the existence of a finite VP constituent, they were never presented with the option to view the syntactic functions in this manner. The issue is a question of what comes first: traditionally, DGs take the syntactic functions to be primitive and they then derive the constellation from these functions, whereas phrase structure grammars traditionally take the constellation to be primitive and they then derive the syntactic functions from the constellation.

This question about what comes first (the functions or the constellation) is not an inflexible matter. The stances of both grammar types (dependency and phrase structure) are not narrowly limited to the traditional views. Dependency and phrase structure are both fully compatible with both approaches to the syntactic functions. Indeed, monostratal systems, that are solely based on dependency or phrase structure, will likely reject the notion that the functions are derived from the constellation or that the constellation is derived from the functions. They will take both to be primitive, which means neither can be derived from the other.

[^1]: Concerning the history of the dependency concept, see Percival (1990).

[^2]: Concerning the influence of term logic on the theory of grammar, see Percival (1976).

[^3]: Concerning dependency in the works of Brassai, see Imrényi (2013). Concerning dependency in the works of Kern, see Kern's essays (e.g. Kern 1883, 1884). Concerning dependency in the works of Tiktin, see Coseriu (1980).

[^4]: There are explicit references to Tesnière's work in Hays (1961), Hays (1962), Hays (1963) and [Robinson](https://en.wikipedia.org/wiki/Jane_J._Robinson "Jane J. Robinson") (1970). In other papers, such as Hays (1960) and Gaifman (1965), there are no references to Tesnière's work. Nevertheless, it is not clear whether the earlier papers by Hays were also inspired by Tesnière or if he discovered the concept of dependency from other sources. In Hays (1963), he wrote that "the theory of dependency, as used here, is familiar to anyone who has studied grammar in school.".

[^5]: Some prominent dependency grammars that were well established by the 1980s are from Hudson (1984), Sgall, Hajičová et Panevova (1986), Mel’čuk (1988), and Starosta (1988).

[^6]: Some prominent dependency grammars from the German schools are from Heringer (1996), Engel (1994), Eroms (2000), and Ágel et al. (2003/6) is a massive two volume collection of essays on dependency grammar and valency theory from more than 100 authors.

[^7]: The minimality of dependency structures is emphasized, for instance, by Ninio (2006), Hudson 2007: 117, and by Osborne et al. (2011).

[^8]: Concerning Tesnière's rejection of the subject-predicate division of the clause, see Tesnière (1959:103–105), and for discussion of empirical considerations that support Tesnière's point, see Matthews (2007:17ff.), Miller (2011:54ff.), and Osborne et al. (2011:323f.).

[^9]: The conventions illustrated with trees (a) and (b) are preferred by Osborne et al. (2011, 2013).

[^10]: Unordered trees like (d) are associated above all with Tesnière's stemmas and with the syntactic strata of Mel’čuk's Meaning-Text Theory.

[^11]: Three major works on Word Grammar are Hudson (1984, 1990, 2007).

[^12]: Lobin (2003) makes heavy use of these indentations.

[^13]: For a discussion of semantic, morphological, and syntactic dependencies in Meaning-Text Theory, see Melʹc̆uk (2003:191ff.) and Osborne 2019: Ch. 5).

[^14]: Concerning semantic dependencies, see Melʹc̆uk (2003:192f.).

[^15]: Concerning morphological dependencies, see Melʹc̆uk (2003:193ff.).

[^16]: The distinction between head- and dependent-marking was established by Nichols (1986). Nichols was using a dependency-based understanding of these distinctions.

[^17]: Concerning prosodic dependencies and the analysis of clitics, see Groß (2011).

[^18]: Distribution is primary principle used by Owens (1984:36), Schubert (1988:40), and Melʹc̆uk (2003:200) for discerning syntactic dependencies.

[^19]: Concerning the importance of the two ordering dimensions, see Tesnière (1959:16ff).

[^20]: See Osborne et al. (2012) concerning catenae.

[^21]: For discussion and examples of the labels for syntactic functions that are attached to dependency edges and arcs, see for instance Mel'cuk (1988:22, 69) and van Valin (2001:102ff.).