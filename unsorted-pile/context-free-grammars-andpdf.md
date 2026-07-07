---
stub: true
title: "Context Free Grammars And.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Context-Free Grammars and.pdf.md"]
psi_tier: unclassified
---

# Context Free Grammars And.Pdf

# Context-Free Grammars and.pdf

Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2024. All
rights reserved. Draft of January 12, 2025.
CHAPTER

18 Context-Free Grammars and

Constituency Parsing

Because the Night by Bruce Springsteen and Patti Smith The Fire Next Time by James Baldwin If on a winter’s night a traveler by Italo Calvino Love Actually by Richard Curtis Suddenly Last Summer by Tennessee Williams A Scanner Darkly by Philip K. Dick
Six titles that are not constituents, from Geoffrey K. Pullum on Language Log (who was pointing out their incredible rarity).
One morning I shot an elephant in my pajamas. How he got into my pajamas I don’t know.
Groucho Marx, Animal Crackers, 1930
The study of grammar has an ancient pedigree. The grammar of Sanskrit was described by the Indian grammarian Pān. ini sometime between the 7th and 4th cen-turies BCE, in his famous treatise the As.t.ādhyāyı̄ (‘8 books’). And our word syntaxsyntax
comes from the Greek sýntaxis, meaning “setting out together or arrangement”, and refers to the way words are arranged together. We have seen syntactic notions in pre-vious chapters like the use of part-of-speech categories (Chapter 17). In this chapter and the next one we introduce formal models for capturing more sophisticated no-tions of grammatical structure and algorithms for parsing these structures.
Our focus in this chapter is context-free grammars and the CKY algorithm for parsing them. Context-free grammars are the backbone of many formal mod-els of the syntax of natural language (and, for that matter, of computer languages). Syntactic parsing is the task of assigning a syntactic structure to a sentence. Parse trees (whether for context-free grammars or for the dependency or CCG formalisms we introduce in following chapters) can be used in applications such as grammar checking: sentence that cannot be parsed may have grammatical errors (or at least be hard to read). Parse trees can be an intermediate stage of representation for for-mal semantic analysis. And parsers and the grammatical structure they assign a sentence are a useful text analysis tool for text data science applications that require modeling the relationship of elements in sentences.
In this chapter we introduce context-free grammars, give a small sample gram-mar of English, introduce more formal definitions of context-free grammars and grammar normal form, and talk about treebanks: corpora that have been anno-tated with syntactic structure. We then discuss parse ambiguity and the problems it presents, and turn to parsing itself, giving the famous Cocke-Kasami-Younger (CKY) algorithm (Kasami 1965, Younger 1967), the standard dynamic program-ming approach to syntactic parsing. The CKY algorithm returns an efficient repre-sentation of the set of parse trees for a sentence, but doesn’t tell us which parse tree is the right one. For that, we need to augment CKY with scores for each possible constituent. We’ll see how to do this with neural span-based parsers. Finally, we’ll introduce the standard set of metrics for evaluating parser accuracy.
2 CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING

18.1 Constituency

Syntactic constituency is the idea that groups of words can behave as single units, or constituents. Part of developing a grammar involves building an inventory of the constituents in the language. How do words group together in English? Consider the noun phrase, a sequence of words surrounding at least one noun. Here are somenoun phrase
examples of noun phrases (thanks to Damon Runyon):
Harry the Horse a high-class spot such as Mindy’s the Broadway coppers the reason he comes into the Hot Box they three parties from Brooklyn
What evidence do we have that these words group together (or “form constituents”)? One piece of evidence is that they can all appear in similar syntactic environments, for example, before a verb.
three parties from Brooklyn arrive. . . a high-class spot such as Mindy’s attracts. . . the Broadway coppers love. . . they sit
But while the whole noun phrase can occur before a verb, this is not true of each of the individual words that make up a noun phrase. The following are not grammat-ical sentences of English (recall that we use an asterisk (*) to mark fragments that are not grammatical English sentences):
*from arrive. . . *as attracts. . . *the is. . . *spot sat. . .
Thus, to correctly describe facts about the ordering of these words in English, we must be able to say things like “Noun Phrases can occur before verbs”. Let’s now see how to do this in a more formal way!

18.2 Context-Free Grammars

A widely used formal system for modeling constituent structure in natural lan-guage is the context-free grammar, or CFG. Context-free grammars are also calledCFG
phrase-structure grammars, and the formalism is equivalent to Backus-Naur form, or BNF. The idea of basing a grammar on constituent structure dates back to the psy-chologist Wilhelm Wundt (1900) but was not formalized until Chomsky (1956) and, independently, Backus (1959).
A context-free grammar consists of a set of rules or productions, each of whichrules
expresses the ways that symbols of the language can be grouped and ordered to-gether, and a lexicon of words and symbols. For example, the following productionslexicon
express that an NP (or noun phrase) can be composed of either a ProperNoun orNP
a determiner (Det) followed by a Nominal; a Nominal in turn can consist of one or
18.2 • CONTEXT-FREE GRAMMARS 3
more Nouns.1
NP → Det Nominal NP → ProperNoun
Nominal → Noun | Nominal Noun
Context-free rules can be hierarchically embedded, so we can combine the previous rules with others, like the following, that express facts about the lexicon:
Det → a Det → the
Noun → flight
The symbols that are used in a CFG are divided into two classes. The symbols that correspond to words in the language (“the”, “nightclub”) are called terminalterminal
symbols; the lexicon is the set of rules that introduce these terminal symbols. The symbols that express abstractions over these terminals are called non-terminals. Innon-terminal
each context-free rule, the item to the right of the arrow (→) is an ordered list of one or more terminals and non-terminals; to the left of the arrow is a single non-terminal symbol expressing some cluster or generalization. The non-terminal associated with each word in the lexicon is its lexical category, or part of speech.
A CFG can be thought of in two ways: as a device for generating sentences and as a device for assigning a structure to a given sentence. Viewing a CFG as a generator, we can read the→ arrow as “rewrite the symbol on the left with the string of symbols on the right”.
So starting from the symbol: NP we can use our first rule to rewrite NP as: Det Nominal and then rewrite Nominal as: Noun and finally rewrite these parts-of-speech as: a flight
We say the string a flight can be derived from the non-terminal NP. Thus, a CFG can be used to generate a set of strings. This sequence of rule expansions is called a derivation of the string of words. It is common to represent a derivation by a parsederivation
tree (commonly shown inverted with the root at the top). Figure 18.1 shows the treeparse tree
representation of this derivation.
NP
Nom
Noun
flight
Det
a
Figure 18.1 A parse tree for “a flight”.
In the parse tree shown in Fig. 18.1, we can say that the node NP dominatesdominates
all the nodes in the tree (Det, Nom, Noun, a, flight). We can say further that it immediately dominates the nodes Det and Nom.
The formal language defined by a CFG is the set of strings that are derivable from the designated start symbol. Each grammar must have one designated startstart symbol
1 When talking about these rules we can pronounce the rightarrow → as “goes to”, and so we might read the first rule above as “NP goes to Det Nominal”.
4 CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING
symbol, which is often called S. Since context-free grammars are often used to define sentences, S is usually interpreted as the “sentence” node, and the set of strings that are derivable from S is the set of sentences in some simplified version of English.
Let’s add a few additional rules to our inventory. The following rule expresses the fact that a sentence can consist of a noun phrase followed by a verb phrase:verb phrase
S → NP VP I prefer a morning flight
A verb phrase in English consists of a verb followed by assorted other things; for example, one kind of verb phrase consists of a verb followed by a noun phrase:
VP → Verb NP prefer a morning flight
Or the verb may be followed by a noun phrase and a prepositional phrase:
VP → Verb NP PP leave Boston in the morning
Or the verb phrase may have a verb followed by a prepositional phrase alone:
VP → Verb PP leaving on Thursday
A prepositional phrase generally has a preposition followed by a noun phrase. For example, a common type of prepositional phrase in the ATIS corpus is used to indicate location or direction:
PP → Preposition NP from Los Angeles
The NP inside a PP need not be a location; PPs are often used with times and dates, and with other nouns as well; they can be arbitrarily complex. Here are ten examples from the ATIS corpus:
to Seattle on these flights in Minneapolis about the ground transportation in Chicago on Wednesday of the round trip flight on United Airlines in the evening of the AP fifty seven flight on the ninth of July with a stopover in Nashville
Figure 18.2 gives a sample lexicon, and Fig. 18.3 summarizes the grammar rules we’ve seen so far, which we’ll call L0. Note that we can use the or-symbol | to indicate that a non-terminal has alternate possible expansions.
Noun→ flights | flight | breeze | trip | morning Verb→ is | prefer | like | need | want | fly | do
Adjective→ cheapest | non-stop | first | latest | other | direct
Pronoun→ me | I | you | it Proper-Noun→ Alaska | Baltimore | Los Angeles
| Chicago | United | American Determiner→ the | a | an | this | these | that Preposition→ from | to | on | near | in
Conjunction→ and | or | but Figure 18.2 The lexicon for L0.
We can use this grammar to generate sentences of this “ATIS-language”. We start with S, expand it to NP VP, then choose a random expansion of NP (let’s say, to
18.2 • CONTEXT-FREE GRAMMARS 5
Grammar Rules Examples S → NP VP I + want a morning flight
NP → Pronoun I | Proper-Noun Los Angeles | Det Nominal a + flight
Nominal → Nominal Noun morning + flight | Noun flights
VP → Verb do | Verb NP want + a flight | Verb NP PP leave + Boston + in the morning | Verb PP leaving + on Thursday
PP → Preposition NP from + Los Angeles Figure 18.3 The grammar for L0, with example phrases for each rule.
S
VP
NP
Nom
Noun
flight
Nom
Noun
morning
Det
a
Verb
prefer
NP
Pro
I
Figure 18.4 The parse tree for “I prefer a morning flight” according to grammar L0.
I), and a random expansion of VP (let’s say, to Verb NP), and so on until we generate the string I prefer a morning flight. Figure 18.4 shows a parse tree that represents a complete derivation of I prefer a morning flight.
We can also represent a parse tree in a more compact format called bracketed notation; here is the bracketed representation of the parse tree of Fig. 18.4:bracketed
notation
(18.1) [S [NP [Pro I]] [VP [V prefer] [NP [Det a] [Nom [N morning] [Nom [N flight]]]]]]
A CFG like that of L0 defines a formal language. Sentences (strings of words) that can be derived by a grammar are in the formal language defined by that gram-mar, and are called grammatical sentences. Sentences that cannot be derived bygrammatical
a given formal grammar are not in the language defined by that grammar and are referred to as ungrammatical. This hard line between “in” and “out” characterizesungrammatical
all formal languages but is only a very simplified model of how natural languages really work. This is because determining whether a given sentence is part of a given natural language (say, English) often depends on the context. In linguistics, the use of formal languages to model natural languages is called generative grammar sincegenerative
grammar the language is defined by the set of possible sentences “generated” by the grammar. (Note that this is a different sense of the word ‘generate’ than when we talk about
6 CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING
language models generating text.)
18.2.1 Formal Definition of Context-Free Grammar We conclude this section with a quick, formal description of a context-free gram-mar and the language it generates. A context-free grammar G is defined by four parameters: N, Σ, R, S (technically it is a “4-tuple”).
N a set of non-terminal symbols (or variables) Σ a set of terminal symbols (disjoint from N) R a set of rules or productions, each of the form A→ β ,
where A is a non-terminal, β is a string of symbols from the infinite set of strings (Σ∪N)∗
S a designated start symbol and a member of N
For the remainder of the book we adhere to the following conventions when dis-cussing the formal properties of context-free grammars (as opposed to explaining particular facts about English or other languages).
Capital letters like A, B, and S Non-terminals S The start symbol Lower-case Greek letters like α , β , and γ Strings drawn from (Σ∪N)∗
Lower-case Roman letters like u, v, and w Strings of terminals
A language is defined through the concept of derivation. One string derives an-other one if it can be rewritten as the second one by some series of rule applications. More formally, following Hopcroft and Ullman (1979),
if A→ β is a production of R and α and γ are any strings in the set (Σ∪N)∗, then we say that αAγ directly derives αβγ , or αAγ ⇒ αβγ .directly derives
Derivation is then a generalization of direct derivation:
Let α1, α2, . . . , αm be strings in (Σ∪N)∗,m≥ 1, such that
α1⇒ α2,α2⇒ α3, . . . ,αm−1⇒ αm
We say that α1 derives αm, or α1 ∗⇒ αm.derives
We can then formally define the language LG generated by a grammar G as the set of strings composed of terminal symbols that can be derived from the designated start symbol S.
LG = {w|w is in Σ ∗ and S ∗⇒ w}
The problem of mapping from a string of words to its parse tree is called syn-tactic parsing, as we’ll see in Section 18.6.syntactic
parsing

18.3 Treebanks

A corpus in which every sentence is annotated with a parse tree is called a treebank.treebank
18.3 • TREEBANKS 7
Treebanks play an important role in parsing as well as in linguistic investigations of syntactic phenomena.
Treebanks are generally made by running a parser over each sentence and then having the resulting parse hand-corrected by human linguists. Figure 18.5 shows sentences from the Penn Treebank project, which includes various treebanks inPenn Treebank
English, Arabic, and Chinese. The Penn Treebank part-of-speech tagset was defined in Chapter 17, but we’ll see minor formatting differences across treebanks. The use of LISP-style parenthesized notation for trees is extremely common and resembles the bracketed notation we saw earlier in (18.1). For those who are not familiar with it we show a standard node-and-line tree representation in Fig. 18.6.
((S
(NP-SBJ (DT That)
(JJ cold) (, ,)
(JJ empty) (NN sky) )
(VP (VBD was)
(ADJP-PRD (JJ full)
(PP (IN of)
(NP (NN fire)
(CC and)
(NN light) ))))
(. .) ))
((S
(NP-SBJ The/DT flight/NN )
(VP should/MD
(VP arrive/VB
(PP-TMP at/IN
(NP eleven/CD a.m/RB ))
(NP-TMP tomorrow/NN )))))
(a) (b)
Figure 18.5 Parses from the LDC Treebank3 for (a) Brown and (b) ATIS sentences.
S
.
.
VP
ADJP-PRD
PP
NP
NN
light
CC
and
NN
fire
IN
of
JJ
full
VBD
was
NP-SBJ
NN
sky
JJ
empty
,
,
JJ
cold
DT
That
Figure 18.6 The tree corresponding to the Brown corpus sentence in the previous figure.
The sentences in a treebank implicitly constitute a grammar of the language. For example, from the parsed sentences in Fig. 18.5 we can extract the CFG rules shown in Fig. 18.7 (with rule suffixes (-SBJ) stripped for simplicity). The grammar used to parse the Penn Treebank is very flat, resulting in very many rules. For example,
8 CHAPTER 18 • CONTEXT-FREE GRAMMARS AND CONSTITUENCY PARSING
Grammar Lexicon S→ NP VP . DT→ the | that S→ NP VP JJ→ cold | empty | full NP→ CD RB NN→ sky | fire | light | flight | tomorrow NP→ DT NN CC→ and NP→ NN CC NN IN→ of | at NP→ DT JJ , JJ NN CD→ eleven NP→ NN RB→ a.m. VP→ MD VP VB→ arrive VP→ VBD ADJP VBD→ was | said VP→ MD VP MD→ should | would VP→ VB PP NP ADJP→ JJ PP PP→ IN NP
Figure 18.7 CFG grammar rules and lexicon from the treebank sentences in Fig. 18.5.
among the approximately 4,500 different rules for expanding VPs are separate rules for PP sequences of any length and every possible arrangement of verb arguments:

[... content truncated ...]

---

*Source: `Context-Free Grammars and.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
