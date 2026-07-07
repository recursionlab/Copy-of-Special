---
title: "Genetic programming"
source: "https://en.wikipedia.org/wiki/Genetic_programming"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2001-08-06
created: 2026-04-10
description:
tags:
  - "clippings"
---
**Genetic programming** (**GP**) is an [evolutionary algorithm](https://en.wikipedia.org/wiki/Evolutionary_algorithm "Evolutionary algorithm"), an artificial intelligence technique mimicking natural evolution, which operates on a population of programs. It applies the [genetic operators](https://en.wikipedia.org/wiki/Genetic_operators "Genetic operators") [selection](https://en.wikipedia.org/wiki/Selection_\(evolutionary_algorithm\) "Selection (evolutionary algorithm)") according to a predefined [fitness measure](https://en.wikipedia.org/wiki/Fitness_function "Fitness function"), [mutation](https://en.wikipedia.org/wiki/Mutation_\(evolutionary_algorithm\) "Mutation (evolutionary algorithm)") and [crossover](https://en.wikipedia.org/wiki/Crossover_\(evolutionary_algorithm\) "Crossover (evolutionary algorithm)").

The crossover operation involves swapping specified parts of selected pairs (parents) to produce new and different offspring that become part of the new generation of programs. Some programs not selected for reproduction are copied from the current generation to the new generation. Mutation involves substitution of some random part of a program with some other random part of a program. Then the selection and other operations are recursively applied to the new generation of programs.

Typically, members of each new generation are on average more fit than the members of the previous generation, and the best-of-generation program is often better than the best-of-generation programs from previous generations. Termination of the evolution usually occurs when some individual program reaches a predefined proficiency or fitness level.

It may and often does happen that a particular run of the algorithm results in premature convergence to some local maximum that is not a globally optimal or even good solution. Multiple runs (dozens to hundreds) are usually necessary to produce a very good result. It may also be necessary to have a large starting population size and variability of the individuals to avoid pathologies.

## History

The first record of the proposal to evolve programs is probably that of [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing "Alan Turing") in 1950 in " [Computing Machinery and Intelligence](https://en.wikipedia.org/wiki/Computing_Machinery_and_Intelligence "Computing Machinery and Intelligence") ". There was a gap of 25 years before the publication of John Holland's 'Adaptation in Natural and Artificial Systems' laid out the theoretical and empirical foundations of the science. In 1981, Richard Forsyth demonstrated the successful evolution of small programs, represented as trees, to perform classification of crime scene evidence for the UK Home Office.[^1]

Although the idea of evolving programs, initially in the computer language [Lisp](https://en.wikipedia.org/wiki/Lisp_\(programming_language\) "Lisp (programming language)"), was current amongst John Holland's students,[^2] it was not until they organised the first [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm "Genetic algorithm") (GA) conference in Pittsburgh that Nichael Cramer [^3] published evolved programs in two specially designed languages, which included the first statement of modern "tree-based" genetic programming (that is, procedural languages organized in tree-based structures and operated on by suitably defined GA-operators). In 1988, [John Koza](https://en.wikipedia.org/wiki/John_Koza "John Koza") (also a PhD student of John Holland) patented his invention of a GA for program evolution.[^4] This was followed by publication in the International Joint Conference on Artificial Intelligence IJCAI-89.[^5]

Koza followed this with 205 publications on "genetic programming", a term coined by David Goldberg, also a PhD student of John Holland.[^6] However, it is the series of 4 books by Koza, starting in 1992 [^7] with accompanying videos,[^8] that really established GP. Subsequently, there was an enormous expansion of the number of publications with the Genetic Programming Bibliography, surpassing 10,000 entries.[^9] In 2010, Koza [^10] listed 77 results where genetic programming was human competitive.

The departure of GP from the rigid, fixed-length representations typical of early GA models was not entirely without precedent. Early work on variable-length representations laid the groundwork. One notable example is messy genetic algorithms, which introduced irregular, variable-length chromosomes to address building block disruption and positional bias in standard GAs.[^11] Another precursor was robot trajectory programming, where genome representations encoded program instructions for robotic movements—structures inherently variable in length.[^12] Even earlier, unfixed-length representations were proposed in a doctoral dissertation by Cavicchio, who explored adaptive search using simulated evolution. His work provided foundational ideas for flexible program structures.[^13]

In 1996, Koza started the annual Genetic Programming conference,[^14] which was followed in 1998 by the annual EuroGP conference,[^15] and the first book [^16] in a GP series edited by Koza. 1998 also saw the first GP textbook.[^17] GP continued to flourish, leading to the first specialist GP journal [^18] and three years later (2003) the annual Genetic Programming Theory and Practice (GPTP) workshop was established by Rick Riolo.[^19] [^20] Genetic programming papers continue to be published at a diversity of conferences and associated journals. Today there are nineteen GP books including several for students.[^17]

| Year | Description | Reference |
| --- | --- | --- |
| 1992 | Introduction of GP as genetically bred populations of computer programs | [^22] |
| 2000 | [Cartesian genetic programming](https://en.wikipedia.org/wiki/Cartesian_genetic_programming "Cartesian genetic programming") | [^23] |
| 2000 | Grammar-guided GP – Dynamic grammar pruning is applied in initialization | [^24] |
| 2001 | [Gene expression programming](https://en.wikipedia.org/wiki/Gene_expression_programming "Gene expression programming") | [^25] |
| 2012 | Multi-gene GP – Combination of classical method for parameter estimation and structure selection | [^26] |
| 2012 | Geometric semantic GP – Direct search in the space of the underlying semantics of the programs | [^27] |
| 2015 | Surrogate GP | [^28] |
| 2015 | Memetic semantic GP | [^29] |
| 2017 | Statistical GP – statistical information used to generate well-structured subtrees | [^30] |
| 2018 | Multi-dimensional GP – novel program representation for multi-dimensional features | [^31] |

### Foundational work in GP

Early work that set the stage for current genetic programming research topics and applications is diverse, and includes [software synthesis](https://en.wikipedia.org/wiki/Program_synthesis "Program synthesis") and repair, predictive modeling, data mining,[^32] financial modeling,[^33] soft sensors,[^34] design,[^35] and image processing.[^36] Applications in some areas, such as design, often make use of intermediate representations,[^37] such as Fred Gruau's cellular encoding.[^38] Industrial uptake has been significant in several areas including finance, the chemical industry, bioinformatics [^39] [^40] and the steel industry.[^41]

## Methods

### Program representation

![](https://upload.wikimedia.org/wikipedia/commons/7/77/Genetic_Program_Tree.png)

A function represented as a tree structure

GP evolves computer programs, traditionally represented in memory as [tree structures](https://en.wikipedia.org/wiki/Tree_\(data_structure\) "Tree (data structure)").[^42] Trees can be easily evaluated in a recursive manner. Every internal node has an operator function and every terminal node has an operand, making mathematical expressions easy to evolve and evaluate. Thus traditionally GP favors the use of [programming languages](https://en.wikipedia.org/wiki/Programming_language "Programming language") that naturally embody tree structures (for example, [Lisp](https://en.wikipedia.org/wiki/Lisp_\(programming_language\) "Lisp (programming language)"); other [functional programming languages](https://en.wikipedia.org/wiki/Functional_programming "Functional programming") are also suitable).

Non-tree representations have been suggested and successfully implemented, such as [linear genetic programming](https://en.wikipedia.org/wiki/Linear_genetic_programming "Linear genetic programming"), which perhaps suits the more traditional [imperative languages](https://en.wikipedia.org/wiki/Imperative_languages "Imperative languages").[^43] [^44] The commercial GP software *Discipulus* uses automatic induction of binary machine code ("AIM") [^45] to achieve better performance. *μGP* [^46] uses [directed multigraphs](https://en.wikipedia.org/wiki/Directed_multigraph "Directed multigraph") to generate programs that fully exploit the syntax of a given [assembly language](https://en.wikipedia.org/wiki/Assembly_language "Assembly language"). [Multi expression programming](https://en.wikipedia.org/wiki/Multi_expression_programming "Multi expression programming") uses [three-address code](https://en.wikipedia.org/wiki/Three-address_code "Three-address code") for encoding solutions. Other program representations on which significant research and development have been conducted include programs for stack-based virtual machines,[^47] [^48] [^49] and sequences of integers that are mapped to arbitrary programming languages via grammars.[^50] [^51] [Cartesian genetic programming](https://en.wikipedia.org/wiki/Cartesian_genetic_programming "Cartesian genetic programming") is another form of GP, which uses a graph representation instead of the usual tree based representation to encode computer programs.

Most representations have structurally noneffective code ([introns](https://en.wikipedia.org/wiki/Intron "Intron")). Such non-coding genes may seem to be useless because they have no effect on the performance of any one individual. However, they alter the probabilities of generating different offspring under the variation operators, and thus alter the individual's [variational properties](https://en.wikipedia.org/wiki/Variational_properties "Variational properties"). Experiments seem to show faster convergence when using program representations that allow such non-coding genes, compared to program representations that do not have any non-coding genes.[^52] [^53] Instantiations may have both trees with introns and those without; the latter are called canonical trees. Special canonical crossover operators are introduced that maintain the canonical structure of parents in their children.

### Initialisation

The methods for creation of the initial population include:[^54]

- **Grow** creates the individuals sequentially. Every GP tree is created starting from the root, creating functional nodes with children as well as terminal nodes up to a certain depth.
- **Full** is similar to the *Grow*. The difference is that all brunches in a tree are of same predetermined depth.
- **Ramped half-and-half** creates a population consisting of ${\displaystyle md-1}$ parts and a maximum depth of ${\displaystyle md}$ for its trees. The first part has a maximum depth of 2, second of 3 and so on up to the ${\displaystyle md-1}$ -th part with maximum depth ${\displaystyle md}$. Half of every part is created by *Grow*, while the other part is created by *Full*.

### Selection

Selection is a process whereby certain individuals are selected from the current generation that would serve as parents for the next generation. The individuals are selected probabilistically such that the better performing individuals have a higher chance of getting selected.[^20] The most commonly used selection method in GP is [tournament selection](https://en.wikipedia.org/wiki/Tournament_selection "Tournament selection"), although other methods such as [fitness proportionate selection](https://en.wikipedia.org/wiki/Fitness_proportionate_selection "Fitness proportionate selection"), lexicase selection,[^55] and others have been demonstrated to perform better for many GP problems.

Elitism, which involves seeding the next generation with the best individual (or best *n* individuals) from the current generation, is a technique sometimes employed to avoid regression.

### Crossover

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Genetic_programming_subtree_crossover.gif/250px-Genetic_programming_subtree_crossover.gif)

Genetic programming subtree crossover

In genetic programming two fit individuals are chosen from the population to be parents for one or two children. In tree genetic programming, these parents are represented as inverted lisp like trees, with their root nodes at the top. In subtree crossover in each parent a subtree is randomly chosen. (Highlighted with yellow in the animation.) In the root donating parent (in the animation on the left) the chosen subtree is removed and replaced with a copy of the randomly chosen subtree from the other parent, to give a new child tree.

Sometimes two child crossover is used, in which case the removed subtree (in the animation on the left) is not simply deleted but is copied to a copy of the second parent (here on the right) replacing (in the copy) its randomly chosen subtree. Thus this type of subtree crossover takes two fit trees and generates two child trees.

The tree-based approach in genetic programming also shares structural and procedural similarities with earlier knowledge-based and topology-oriented crossover methods. Specifically, analogous crossover and homologous crossover, both implemented in robot trajectory planning, exhibit a resemblance to subtree operations in tree GP. These crossover mechanisms were described in the context of heuristic optimisation strategies in robotics.[^56]

### Replication

Some individuals selected according to fitness criteria do not participate in crossover, but are copied into the next generation, akin to asexual reproduction in the natural world. They may be further subject to mutation.

### Mutation

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Genetic_programming_mutation.gif/250px-Genetic_programming_mutation.gif)

Animation of creating genetic programing child by mutating parent removing subtree and replacing with random code

There are many types of mutation in genetic programming. They start from a fit syntactically correct parent and aim to randomly create a syntactically correct child. In the animation a subtree is randomly chosen (highlighted by yellow). It is removed and replaced by a randomly generated subtree.

Other mutation operators select a leaf (external node) of the tree and replace it with a randomly chosen leaf. Another mutation is to select at random a function (internal node) and replace it with another function with the same arity (number of inputs). Hoist mutation randomly chooses a subtree and replaces it with a subtree within itself. Thus hoist mutation is guaranteed to make the child smaller. Leaf and same arity function replacement ensure the child is the same size as the parent. Whereas subtree mutation (in the animation) may, depending upon the function and terminal sets, have a bias to either increase or decrease the tree size. Other subtree based mutations try to carefully control the size of the replacement subtree and thus the size of the child tree.

Similarly there are many types of linear genetic programming mutation, each of which tries to ensure the mutated child is still syntactically correct.

## Applications

GP has been successfully used as an [automatic programming](https://en.wikipedia.org/wiki/Automatic_programming "Automatic programming") tool, a machine learning tool and an automatic problem-solving engine.[^20] GP is especially useful in the domains where the exact form of the solution is not known in advance or an approximate solution is acceptable (possibly because finding the exact solution is very difficult). Some of the applications of GP are curve fitting, data modeling, [symbolic regression](https://en.wikipedia.org/wiki/Symbolic_regression "Symbolic regression"), [feature selection](https://en.wikipedia.org/wiki/Feature_selection "Feature selection"), and classification. John R. Koza mentions 76 instances where genetic programming has been able to produce results that are competitive with human-produced results (called human-competitive results).[^57] Since 2004, the annual Genetic and Evolutionary Computation Conference ([GECCO](https://en.wikipedia.org/wiki/GECCO "GECCO")) holds a Human Competitive Awards (called Humies) competition,[^58] where cash awards are presented to human-competitive results produced by any form of genetic and evolutionary computation. GP has won many awards in this competition over the years.

## Meta-genetic programming

Meta-genetic programming is the proposed [meta-learning](https://en.wikipedia.org/wiki/Meta-learning_\(computer_science\) "Meta-learning (computer science)") technique of evolving a genetic programming system using genetic programming itself. It suggests that chromosomes, crossover, and mutation were themselves evolved, therefore like their real life counterparts should be allowed to change on their own rather than being determined by a human programmer. Meta-GP was formally proposed by [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") in 1987.[^59] [Doug Lenat](https://en.wikipedia.org/wiki/Douglas_Lenat "Douglas Lenat") 's [Eurisko](https://en.wikipedia.org/wiki/Eurisko "Eurisko") is an earlier effort that may be the same technique. It is a recursive but terminating algorithm, allowing it to avoid infinite recursion. In the "autoconstructive evolution" approach to meta-genetic programming, the methods for the production and variation of offspring are encoded within the evolving programs themselves, and programs are executed to produce new programs to be added to the population.[^48] [^60]

Critics of this idea often say this approach is overly broad in scope. However, it might be possible to constrain the fitness criterion onto a general class of results, and so obtain an evolved GP that would more efficiently produce results for sub-classes. This might take the form of a meta evolved GP for producing human walking algorithms, which is then used to evolve human running, jumping, etc. The fitness criterion applied to the meta GP would simply be one of efficiency.

[^1]: ["BEAGLE A Darwinian Approach to Pattern Recognition"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/kybernetes_forsyth.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^2]: A personal communication with [Tom Westerdale](http://www.dcs.bbk.ac.uk/~tom/)

[^3]: ["A representation for the Adaptive Generation of Simple Sequential Programs"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/icga85_cramer.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^4]: ["Non-Linear Genetic Algorithms for Solving Problems"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/Koza_1990_pat-GAsp.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^5]: ["Hierarchical genetic algorithms operating on populations of computer programs"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/Koza89.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^6]: Goldberg. D.E. (1983), Computer-aided gas pipeline operation using genetic algorithms and rule learning. Dissertation presented to the University of Michigan at Ann Arbor, Michigan, in partial fulfillment of the requirements for Ph.D.

[^7]: ["Genetic Programming: On the Programming of Computers by Means of Natural Selection"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/koza_book.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^8]: ["Genetic Programming:The Movie"](https://www.youtube.com/watch?v=tTMpKrKkYXo). *gpbib.cs.ucl.ac.uk*. 16 December 2020. [Archived](https://ghostarchive.org/varchive/youtube/20211211/tTMpKrKkYXo) from the original on 2021-12-11. Retrieved 2021-05-20.

[^9]: ["The effects of recombination on phenotypic exploration and robustness in evolution"](http://gpbib.cs.ucl.ac.uk/gp-html/Hu_2014_Alife.html). *gpbib.cs.ucl.ac.uk*. Retrieved 2021-05-20.

[^10]: ["Human-competitive results produced by genetic programming"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/Koza_2010_GPEM.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^11]: Goldberg, D.E., Korb, B., & Deb, K. (1989). Messy Genetic Algorithms: Motivation, Analysis, and First Results. Complex Systems, 3, 493–530.

[^12]: Davidor, Y. (1989). Analogous Crossover. In Proceedings of the 3rd International Conference on Genetic Algorithms (pp. 98–103). Morgan Kaufmann.

[^13]: Cavicchio, D.J. (1970). Adaptive Search Using Simulated Evolution. Doctoral dissertation, University of Michigan, Ann Arbor.

[^14]: ["Genetic Programming 1996: Proceedings of the First Annual Conference"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/koza_gp96.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^15]: ["Genetic Programming"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/banzhaf_1998_GP.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-19.

[^16]: ["Genetic Programming and Data Structures: Genetic Programming + Data Structures = Automatic Programming!"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/langdon_book.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^17]: ["Genetic Programming – An Introduction; On the Automatic Evolution of Computer Programs and its Applications"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/banzhaf_1997_book.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^18]: Banzhaf, Wolfgang (2000-04-01). "Editorial Introduction". *Genetic Programming and Evolvable Machines*. **1** (1–2): 5–6. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1023/A:1010026829303](https://doi.org/10.1023%2FA%3A1010026829303). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1389-2576](https://search.worldcat.org/issn/1389-2576).

[^19]: ["Genetic Programming Theory and Practice"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/RioloWorzel_2003.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^20]: ["A Field Guide to Genetic Programming"](http://www.gp-field-guide.org.uk/). *www.gp-field-guide.org.uk*. Retrieved 2018-05-20.

[^21]: Slowik, Adam; Kwasnicka, Halina (1 August 2020). ["Evolutionary algorithms and their applications to engineering problems"](https://doi.org/10.1007%2Fs00521-020-04832-8). *Neural Computing and Applications*. **32** (16): 12363–12379. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/s00521-020-04832-8](https://doi.org/10.1007%2Fs00521-020-04832-8). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1433-3058](https://search.worldcat.org/issn/1433-3058).

[^22]: Koza, J. R. G. P. (1992). "On the programming of computers by means of natural selection". *Genetic Programming*.

[^23]: Miller, Julian F. (2011). ["Cartesian Genetic Programming"](https://link.springer.com/chapter/10.1007/978-3-642-17310-3_2). Natural Computing Series. Springer. pp. 17–34. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-642-17310-3\_2](https://doi.org/10.1007%2F978-3-642-17310-3_2). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-642-17309-7](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-17309-7 "Special:BookSources/978-3-642-17309-7").

[^24]: Ratle, Alain; Sebag, Michèle (2000). ["Genetic Programming and Domain Knowledge: Beyond the Limitations of Grammar-Guided Machine Discovery"](https://link.springer.com/chapter/10.1007/3-540-45356-3_21). [*Parallel Problem Solving from Nature PPSN VI*](https://hal.science/hal-00116116). Lecture Notes in Computer Science. Vol. 1917. Springer. pp. 211–220. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/3-540-45356-3\_21](https://doi.org/10.1007%2F3-540-45356-3_21). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-41056-0](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-41056-0 "Special:BookSources/978-3-540-41056-0").

[^25]: Ferreira, Candida (2001). "Gene Expression Programming: a New Adaptive Algorithm for Solving Problems". [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv (identifier)"):[cs/0102027](https://arxiv.org/abs/cs/0102027).

[^26]: Gandomi, Amir Hossein; Alavi, Amir Hossein (1 February 2012). ["A new multi-gene genetic programming approach to nonlinear system modeling. Part I: materials and structural engineering problems"](https://link.springer.com/article/10.1007/s00521-011-0734-z). *Neural Computing and Applications*. **21** (1): 171–187. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/s00521-011-0734-z](https://doi.org/10.1007%2Fs00521-011-0734-z). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1433-3058](https://search.worldcat.org/issn/1433-3058).

[^27]: Moraglio, Alberto; Krawiec, Krzysztof; Johnson, Colin G. (2012). ["Geometric Semantic Genetic Programming"](https://link.springer.com/chapter/10.1007/978-3-642-32937-1_3). *Parallel Problem Solving from Nature – PPSN XII*. Lecture Notes in Computer Science. Vol. 7491. Springer. pp. 21–31. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-642-32937-1\_3](https://doi.org/10.1007%2F978-3-642-32937-1_3). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-642-32936-4](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-32936-4 "Special:BookSources/978-3-642-32936-4").

[^28]: Kattan, Ahmed; Ong, Yew-Soon (1 March 2015). ["Surrogate Genetic Programming: A semantic aware evolutionary search"](https://www.sciencedirect.com/science/article/abs/pii/S0020025514010421). *Information Sciences*. **296**: 345–359. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.ins.2014.10.053](https://doi.org/10.1016%2Fj.ins.2014.10.053). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0020-0255](https://search.worldcat.org/issn/0020-0255).

[^29]: Ffrancon, Robyn; Schoenauer, Marc (11 July 2015). ["Memetic Semantic Genetic Programming"](https://dl.acm.org/doi/10.1145/2739480.2754697). [*Proceedings of the 2015 Annual Conference on Genetic and Evolutionary Computation*](https://hal.inria.fr/hal-01169074/file/8parV_errors_old_vs_new.pdf) (PDF). Association for Computing Machinery. pp. 1023–1030. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/2739480.2754697](https://doi.org/10.1145%2F2739480.2754697). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4503-3472-3](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4503-3472-3 "Special:BookSources/978-1-4503-3472-3").

[^30]: Amir Haeri, Maryam; Ebadzadeh, Mohammad Mehdi; Folino, Gianluigi (1 November 2017). ["Statistical genetic programming for symbolic regression"](https://www.sciencedirect.com/science/article/abs/pii/S1568494617303939). *Applied Soft Computing*. **60**: 447–469. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.asoc.2017.06.050](https://doi.org/10.1016%2Fj.asoc.2017.06.050). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1568-4946](https://search.worldcat.org/issn/1568-4946).

[^31]: La Cava, William; Silva, Sara; Danai, Kourosh; Spector, Lee; Vanneschi, Leonardo; Moore, Jason H. (1 February 2019). ["Multidimensional genetic programming for multiclass classification"](https://doi.org/10.1016%2Fj.swevo.2018.03.015). *Swarm and Evolutionary Computation*. **44**: 260–272. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.swevo.2018.03.015](https://doi.org/10.1016%2Fj.swevo.2018.03.015). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [2210-6502](https://search.worldcat.org/issn/2210-6502).

[^32]: ["Data Mining and Knowledge Discovery with Evolutionary Algorithms"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/freitas_2002_book.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^33]: ["EDDIE beats the bookies"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/tsang_1998_eddie.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^34]: ["Applying Computational Intelligence How to Create Value"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/Kordon_book.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^35]: ["Human-competitive machine invention by means of genetic programming"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/DBLP_journals_aiedam_Koza08.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^36]: Lam, Brian; Ciesielski, Vic (2004). Deb, Kalyanmoy (ed.). ["Discovery of Human-Competitive Image Texture Feature Extraction Programs Using Genetic Programming"](https://link.springer.com/chapter/10.1007/978-3-540-24855-2_121?error=cookies_not_supported&code=f8219d96-15e2-4c6c-ab95-779543bbb11d). *Genetic and Evolutionary Computation – GECCO 2004*. Berlin, Heidelberg: Springer: 1114–1125. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-3-540-24855-2\_121](https://doi.org/10.1007%2F978-3-540-24855-2_121). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-540-24855-2](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-24855-2 "Special:BookSources/978-3-540-24855-2").

[^37]: ["Three Ways to Grow Designs: A Comparison of Embryogenies for an Evolutionary Design Problem"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/bentley_1999_TWGDACEEDP.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^38]: ["Cellular encoding as a graph grammar – IET Conference Publication"](https://ieeexplore.ieee.org/document/243137). *[IEEE](https://en.wikipedia.org/wiki/IEEE "IEEE")*: 17/1–1710. April 1993. Retrieved 2018-05-20.

[^39]: ["Genetic Algorithm Decoding for the Interpretation of Infra-red Spectra in Analytical Biotechnology"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/taylor_1998_gadiirsab.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^40]: ["Genetic Programming for Mining DNA Chip data from Cancer Patients"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/langdon_2004_GPEM.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^41]: ["Genetic Programming and Jominy Test Modeling"](https://www.cs.bham.ac.uk/~wbl/biblio/gp-html/Kovacic_2009_MMP2.html). *www.cs.bham.ac.uk*. Retrieved 2018-05-20.

[^42]: Nichael L. Cramer ["A Representation for the Adaptive Generation of Simple Sequential Programs"](http://www.sover.net/~nichael/nlc-publications/icga85/index.html) [Archived](https://web.archive.org/web/20051204112804/http://www.sover.net/~nichael/nlc-publications/icga85/index.html) 2005-12-04 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine").

[^43]: Genetic Programming: An Introduction, Wolfgang Banzhaf, Peter Nordin, Robert E. Keller, Frank D. Francone, Morgan Kaufmann, 1999. ISBN 978-1558605107

[^44]: Garnett Wilson and Wolfgang Banzhaf. ["A Comparison of Cartesian Genetic Programming and Linear Genetic Programming"](http://www.cs.mun.ca/~banzhaf/papers/eurogp08_clgp.pdf)

[^45]: ([Peter Nordin](https://en.wikipedia.org/wiki/Peter_Nordin "Peter Nordin"), 1997, Banzhaf et al., 1998, Section 11.6.2-11.6.3)

[^46]: Giovanni Squillero. ["μGP (MicroGP)"](https://ugp3.sourceforge.net/).

[^47]: ["Stack-Based Genetic Programming"](http://gpbib.cs.ucl.ac.uk/gp-html/ieee94_perkis.html). *gpbib.cs.ucl.ac.uk*. Retrieved 2021-05-20.

[^48]: Spector, Lee; Robinson, Alan (2002-03-01). "Genetic Programming and Autoconstructive Evolution with the Push Programming Language". *Genetic Programming and Evolvable Machines*. **3** (1): 7–40. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1023/A:1014538503543](https://doi.org/10.1023%2FA%3A1014538503543). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1389-2576](https://search.worldcat.org/issn/1389-2576). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [5584377](https://api.semanticscholar.org/CorpusID:5584377).

[^49]: Spector, Lee; Klein, Jon; Keijzer, Maarten (2005-06-25). "The Push3 execution stack and the evolution of control". *Proceedings of the 7th annual conference on Genetic and evolutionary computation*. ACM. pp. 1689–1696. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.153.384](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.153.384). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/1068009.1068292](https://doi.org/10.1145%2F1068009.1068292). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1595930101](https://en.wikipedia.org/wiki/Special:BookSources/978-1595930101 "Special:BookSources/978-1595930101"). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [11954638](https://api.semanticscholar.org/CorpusID:11954638).

[^50]: Ryan, Conor; Collins, JJ; Neill, Michael O (1998). *Lecture Notes in Computer Science*. Berlin, Heidelberg: Springer Berlin Heidelberg. pp. 83–96. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.38.7697](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.7697). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/bfb0055930](https://doi.org/10.1007%2Fbfb0055930). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9783540643609](https://en.wikipedia.org/wiki/Special:BookSources/9783540643609 "Special:BookSources/9783540643609").

[^51]: O'Neill, M.; Ryan, C. (2001). "Grammatical evolution". *IEEE Transactions on Evolutionary Computation*. **5** (4): 349–358. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2001ITEC....5..349O](https://ui.adsabs.harvard.edu/abs/2001ITEC....5..349O). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/4235.942529](https://doi.org/10.1109%2F4235.942529). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [1089-778X](https://search.worldcat.org/issn/1089-778X). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [10391383](https://api.semanticscholar.org/CorpusID:10391383).

[^52]: Julian F. Miller. ["Cartesian Genetic Programming"](https://www.springer.com/cda/content/document/cda_downloaddocument/9783642173097-c2.pdf) [Archived](https://web.archive.org/web/20150924123354/http://www.springer.com/cda/content/document/cda_downloaddocument/9783642173097-c2.pdf) 2015-09-24 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"). p. 19.

[^53]: Janet Clegg; James Alfred Walker; Julian Francis Miller. [A New Crossover Technique for Cartesian Genetic Programming"](http://www.cs.bham.ac.uk/~wbl/biblio/gecco2007/docs/p1580.pdf). 2007.

[^54]: Walker, Matthew (2001). "Introduction to Genetic Programming". *Massey University*.

[^55]: Spector, Lee (2012). "Assessment of problem modality by differential performance of lexicase selection in genetic programming". [*Proceedings of the 14th annual conference companion on Genetic and evolutionary computation*](https://dl.acm.org/citation.cfm?id=2330846). Gecco '12. ACM. pp. 401–408. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1145/2330784.2330846](https://doi.org/10.1145%2F2330784.2330846). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9781450311786](https://en.wikipedia.org/wiki/Special:BookSources/9781450311786 "Special:BookSources/9781450311786"). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [3258264](https://api.semanticscholar.org/CorpusID:3258264).

[^56]: Davidor, Y. (1991). Genetic Algorithms and Robotics: A Heuristic Strategy for Optimization. World Scientific Series in Robotics and Intelligent Systems: Volume 1.

[^57]: Koza, John R (2010). ["Human-competitive results produced by genetic programming"](https://doi.org/10.1007%2Fs10710-010-9112-3). *Genetic Programming and Evolvable Machines*. **11** (3–4): 251–284. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/s10710-010-9112-3](https://doi.org/10.1007%2Fs10710-010-9112-3).

[^58]: ["Humies =Human-Competitive Awards"](http://www.human-competitive.org/awards).

[^59]: ["1987 THESIS ON LEARNING HOW TO LEARN, METALEARNING, META GENETIC PROGRAMMING, CREDIT-CONSERVING MACHINE LEARNING ECONOMY"](http://www.idsia.ch/~juergen/diploma.html).

[^60]: *GECCO '16 Companion: proceedings of the 2016 Genetic and Evolutionary Computation Conference: July 20-24, 2016, Denver, Colorado, USA*. Neumann, Frank (Computer scientist), Association for Computing Machinery. SIGEVO. New York, New York. 20 July 2016. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9781450343237](https://en.wikipedia.org/wiki/Special:BookSources/9781450343237 "Special:BookSources/9781450343237"). [OCLC](https://en.wikipedia.org/wiki/OCLC_\(identifier\) "OCLC (identifier)") [987011786](https://search.worldcat.org/oclc/987011786).