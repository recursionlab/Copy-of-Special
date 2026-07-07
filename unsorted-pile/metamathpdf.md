---
stub: true
title: "Metamath.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Metamath.pdf.md"]
psi_tier: unclassified
---

# Metamath.Pdf

# Metamath.pdf

Metamath

A Computer Language for Mathematical Proofs
Norman Megill
with extensive revisions by
David A. Wheeler
2019-06-02
∼ Public Domain ∼
This book (including its later revisions) has been released into the Public Domain by Norman Megill per the Creative Commons CC0 1.0 Universal
(CC0 1.0) Public Domain Dedication (
https://creativecommons.org/publicdomain/zero/1.0/
). David A.
Wheeler has done the same. The public domain release applies worldwide. In case this is not legally possible, the right is granted to use the work for any purpose, without any conditions, unless such conditions are required by
law.
Several short, attributed quotations from copyrighted works appear in this book under the “fair use” provision of Section 107 of the United States Copyright Act (Title 17 of the United States Code). The public-domain
status of this book is not applicable to those quotations.
Any trademarks used in this book are the property of their owners.
ISBN: 978-0-359-70223-7
Lulu Press Morrisville, North Carolina
USA
Norman Megill 93 Bridge St., Lexington, MA 02421 E-mail address:
nm@alum.mit.edu

David A. Wheeler E-mail address:
dwheeler@dwheeler.com

http://metamath.org

Contents

Preface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ix
1 Introduction 1 1.1 Mathematics as a Computer Language . . . . . . . . . . . . . 4
1.1.1 Is Mathematics “User-Friendly”? . . . . . . . . . . . . 4 1.1.2 Mathematics and the Non-Specialist . . . . . . . . . . 12 1.1.3 An Impossible Dream? . . . . . . . . . . . . . . . . . . 14 1.1.4 Beauty . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 1.1.5 Simplicity . . . . . . . . . . . . . . . . . . . . . . . . . 16 1.1.6 Rigor . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1.2 Computers and Mathematicians . . . . . . . . . . . . . . . . . 20 1.2.1 Trusting the Computer . . . . . . . . . . . . . . . . . 21 1.2.2 Trusting the Mathematician . . . . . . . . . . . . . . . 22
1.3 The Use of Computers in Mathematics . . . . . . . . . . . . . 24 1.3.1 Computer Algebra Systems . . . . . . . . . . . . . . . 24 1.3.2 Automated Theorem Provers . . . . . . . . . . . . . . 25 1.3.3 Interactive Theorem Provers . . . . . . . . . . . . . . 27 1.3.4 Proof Verifiers . . . . . . . . . . . . . . . . . . . . . . 28 1.3.5 Creating a Database of Formalized Mathematics . . . 29 1.3.6 In Summary . . . . . . . . . . . . . . . . . . . . . . . 31
1.4 Mathematics and Metamath . . . . . . . . . . . . . . . . . . . 31 1.4.1 Standard Mathematics . . . . . . . . . . . . . . . . . . 31 1.4.2 Other Formal Systems . . . . . . . . . . . . . . . . . . 32 1.4.3 Metamath and Its Philosophy . . . . . . . . . . . . . . 33 1.4.4 A History of the Approach Behind Metamath . . . . . 33 1.4.5 Metamath and First-Order Logic . . . . . . . . . . . . 34
2 Using the Metamath Program 37 2.1 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 2.2 Your First Formal System . . . . . . . . . . . . . . . . . . . . 38
2.2.1 From Nothing to Zero . . . . . . . . . . . . . . . . . . 38 2.2.2 Converting It to Metamath . . . . . . . . . . . . . . . 40
2.3 A Trial Run . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 2.3.1 Some Hints for Using the Command Line Interface . . 49
iv CONTENTS
2.4 Your First Proof . . . . . . . . . . . . . . . . . . . . . . . . . 50 2.5 A Note About Editing a Database File . . . . . . . . . . . . . 57
3 Abstract Mathematics Revealed 59 3.1 Logic and Set Theory . . . . . . . . . . . . . . . . . . . . . . 59 3.2 The Axioms for All of Mathematics . . . . . . . . . . . . . . . 62
3.2.1 Propositional Calculus . . . . . . . . . . . . . . . . . . 62 3.2.2 Predicate Calculus . . . . . . . . . . . . . . . . . . . . 64 3.2.3 Set Theory . . . . . . . . . . . . . . . . . . . . . . . . 68 3.2.4 Other Axioms . . . . . . . . . . . . . . . . . . . . . . . 70
3.3 The Axioms in the Metamath Language . . . . . . . . . . . . 70 3.3.1 Propositional Calculus . . . . . . . . . . . . . . . . . . 70 3.3.2 Axioms of Predicate Calculus with Equality—Tarski’s
S2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71 3.3.3 Axioms of Predicate Calculus with Equality—Auxiliary 71 3.3.4 Set Theory . . . . . . . . . . . . . . . . . . . . . . . . 71 3.3.5 That’s It . . . . . . . . . . . . . . . . . . . . . . . . . 72
3.4 A Hierarchy of Definitions . . . . . . . . . . . . . . . . . . . . 72 3.4.1 Definitions for Propositional Calculus . . . . . . . . . 74 3.4.2 Definitions for Predicate Calculus . . . . . . . . . . . . 76 3.4.3 Definitions for Set Theory . . . . . . . . . . . . . . . . 77
3.5 Tricks of the Trade . . . . . . . . . . . . . . . . . . . . . . . . 85 3.6 A Theorem Sampler . . . . . . . . . . . . . . . . . . . . . . . 86 3.7 Axioms for Real and Complex Numbers . . . . . . . . . . . . 89
3.7.1 The Axioms for Real and Complex Numbers Themselves 90 3.7.2 Complex Number Axioms in Analysis Texts . . . . . . 91 3.7.3 Eliminating Unnecessary Complex Number Axioms . . 92
3.8 Two Plus Two Equals Four . . . . . . . . . . . . . . . . . . . 92 3.9 Deduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.9.1 The Standard Deduction Theorem . . . . . . . . . . . 94 3.9.2 Weak Deduction Theorem . . . . . . . . . . . . . . . . 95 3.9.3 Deduction Style . . . . . . . . . . . . . . . . . . . . . . 97 3.9.4 Natural Deduction . . . . . . . . . . . . . . . . . . . . 98 3.9.5 Strengths of Our Approach . . . . . . . . . . . . . . . 101
3.10 Exploring the Set Theory Database . . . . . . . . . . . . . . . 101 3.10.1 A Note on the “Compact” Proof Format . . . . . . . . 109
4 The Metamath Language 111 4.1 Specification of the Metamath Language . . . . . . . . . . . . 112
4.1.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . 112 4.1.2 Preprocessing . . . . . . . . . . . . . . . . . . . . . . . 113 4.1.3 Basic Syntax . . . . . . . . . . . . . . . . . . . . . . . 113 4.1.4 Proof Verification . . . . . . . . . . . . . . . . . . . . . 115
4.2 The Basic Keywords . . . . . . . . . . . . . . . . . . . . . . . 116 4.2.1 User-Defined Tokens . . . . . . . . . . . . . . . . . . . 117
CONTENTS v
4.2.2 Constants and Variables . . . . . . . . . . . . . . . . . 119 4.2.3 The $c and $v Declaration Statements . . . . . . . . . 119 4.2.4 The $d Statement . . . . . . . . . . . . . . . . . . . . 120 4.2.5 The $f and $e Statements . . . . . . . . . . . . . . . . 125 4.2.6 Assertions ($a and $p Statements) . . . . . . . . . . . 127 4.2.7 Frames . . . . . . . . . . . . . . . . . . . . . . . . . . 129 4.2.8 Scoping Statements (${ and $}) . . . . . . . . . . . . 132
4.3 The Anatomy of a Proof . . . . . . . . . . . . . . . . . . . . . 135 4.3.1 The Concept of Unification . . . . . . . . . . . . . . . 139
4.4 Extensions to the Metamath Language . . . . . . . . . . . . . 139 4.4.1 Comments in the Metamath Language . . . . . . . . . 139 4.4.2 The Typesetting Comment ($t) . . . . . . . . . . . . 144 4.4.3 Additional Information Comment ($j) . . . . . . . . . 147 4.4.4 Including Other Files in a Metamath Source File . . . 148 4.4.5 Compressed Proof Format . . . . . . . . . . . . . . . . 149 4.4.6 Specifying Unknown Proofs or Subproofs . . . . . . . 150
4.5 Axioms vs. Definitions . . . . . . . . . . . . . . . . . . . . . . 150 4.5.1 What is a Definition? . . . . . . . . . . . . . . . . . . 151 4.5.2 The Approach to Definitions in set.mm . . . . . . . . 152 4.5.3 Adding Constraints on Definitions . . . . . . . . . . . 154 4.5.4 Summary of Approach to Definitions . . . . . . . . . . 155
5 The Metamath Program 157 5.1 Invoking Metamath . . . . . . . . . . . . . . . . . . . . . . . . 157 5.2 Controlling Metamath . . . . . . . . . . . . . . . . . . . . . . 158
5.2.1 exit Command . . . . . . . . . . . . . . . . . . . . . . 159 5.2.2 open log Command . . . . . . . . . . . . . . . . . . . 159 5.2.3 close log Command . . . . . . . . . . . . . . . . . . 160 5.2.4 submit Command . . . . . . . . . . . . . . . . . . . . 160 5.2.5 erase Command . . . . . . . . . . . . . . . . . . . . . 160 5.2.6 set echo Command . . . . . . . . . . . . . . . . . . . 160 5.2.7 set scroll Command . . . . . . . . . . . . . . . . . . 160 5.2.8 set width Command . . . . . . . . . . . . . . . . . . 161 5.2.9 set height Command . . . . . . . . . . . . . . . . . . 161 5.2.10 beep Command . . . . . . . . . . . . . . . . . . . . . . 161 5.2.11 more Command . . . . . . . . . . . . . . . . . . . . . . 161 5.2.12 Operating System Commands . . . . . . . . . . . . . . 161 5.2.13 Size Limitations in Metamath . . . . . . . . . . . . . . 162
5.3 Reading and Writing Files . . . . . . . . . . . . . . . . . . . . 162 5.3.1 read Command . . . . . . . . . . . . . . . . . . . . . . 162 5.3.2 write source Command . . . . . . . . . . . . . . . . 163
5.4 Showing Status and Statements . . . . . . . . . . . . . . . . . 163 5.4.1 show settings Command . . . . . . . . . . . . . . . . 163 5.4.2 show memory Command . . . . . . . . . . . . . . . . . 163 5.4.3 show labels Command . . . . . . . . . . . . . . . . . 163
vi CONTENTS
5.4.4 show statement Command . . . . . . . . . . . . . . . 164 5.4.5 search Command . . . . . . . . . . . . . . . . . . . . 164
5.5 Displaying and Verifying Proofs . . . . . . . . . . . . . . . . . 165 5.5.1 show proof Command . . . . . . . . . . . . . . . . . . 165 5.5.2 show usage Command . . . . . . . . . . . . . . . . . . 166 5.5.3 show trace back Command . . . . . . . . . . . . . . 166 5.5.4 verify proof Command . . . . . . . . . . . . . . . . 166 5.5.5 verify markup Command . . . . . . . . . . . . . . . . 167 5.5.6 save proof Command . . . . . . . . . . . . . . . . . . 167
5.6 Creating Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . 168 5.6.1 prove Command . . . . . . . . . . . . . . . . . . . . . 170 5.6.2 set unification timeout Command . . . . . . . . . 170 5.6.3 set empty substitution Command . . . . . . . . . . 171 5.6.4 set search limit Command . . . . . . . . . . . . . . 171 5.6.5 show new proof Command . . . . . . . . . . . . . . . 171 5.6.6 assign Command . . . . . . . . . . . . . . . . . . . . 172 5.6.7 match Command . . . . . . . . . . . . . . . . . . . . . 172 5.6.8 let Command . . . . . . . . . . . . . . . . . . . . . . 173 5.6.9 unify Command . . . . . . . . . . . . . . . . . . . . . 173 5.6.10 initialize Command . . . . . . . . . . . . . . . . . . 174 5.6.11 delete Command . . . . . . . . . . . . . . . . . . . . 174 5.6.12 improve Command . . . . . . . . . . . . . . . . . . . . 175 5.6.13 save new proof Command . . . . . . . . . . . . . . . 175
5.7 Creating LATEX Output . . . . . . . . . . . . . . . . . . . . . 176 5.7.1 open tex Command . . . . . . . . . . . . . . . . . . . 176 5.7.2 close tex Command . . . . . . . . . . . . . . . . . . 177
5.8 Creating HTML Output . . . . . . . . . . . . . . . . . . . . . 177 5.8.1 write theorem list Command . . . . . . . . . . . . 178 5.8.2 write bibliography Command . . . . . . . . . . . . 178 5.8.3 write recent additions Command . . . . . . . . . . 178
5.9 Text File Utilities . . . . . . . . . . . . . . . . . . . . . . . . . 179 5.9.1 tools Command . . . . . . . . . . . . . . . . . . . . . 179 5.9.2 help Command (in tools) . . . . . . . . . . . . . . . 179 5.9.3 Using tools to Build Metamath submit Scripts . . . 180 5.9.4 Example of a tools Session . . . . . . . . . . . . . . . 180
A Sample Representations 183
B Compressed Proofs 187
C Metamath’s Formal System 189 C.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189 C.2 The Formal Description . . . . . . . . . . . . . . . . . . . . . 190
C.2.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . 190 C.2.2 Constants, Variables, and Expressions . . . . . . . . . 190
CONTENTS vii
C.2.3 Substitution . . . . . . . . . . . . . . . . . . . . . . . . 191 C.2.4 Statements . . . . . . . . . . . . . . . . . . . . . . . . 191 C.2.5 Formal Systems . . . . . . . . . . . . . . . . . . . . . . 193
C.3 Examples of Formal Systems . . . . . . . . . . . . . . . . . . 194 C.3.1 Example 1—Propositional Calculus . . . . . . . . . . . 194 C.3.2 Example 2—Predicate Calculus with Equality . . . . . 196 C.3.3 Free Variables and Proper Substitution . . . . . . . . 198 C.3.4 Metalogical Completeness . . . . . . . . . . . . . . . . 199 C.3.5 Example 3—Metalogically Complete Predicate Calcu-
lus with Equality . . . . . . . . . . . . . . . . . . . . . 199 C.3.6 Example 4—Adding Definitions . . . . . . . . . . . . . 201 C.3.7 Example 5—ZFC Set Theory . . . . . . . . . . . . . . 202 C.3.8 Example 6—Class Notation in Set Theory . . . . . . . 202
C.4 Metamath as a Formal System . . . . . . . . . . . . . . . . . 204
D The MIU System 207
E Metamath Language EBNF 211
Bibliography 215
Index 221
viii CONTENTS

Preface

Overview
Metamath is a computer language and an associated computer program for archiving, verifying, and studying mathematical proofs at a very detailed level. The Metamath language incorporates no mathematics per se but treats all mathematical statements as mere sequences of symbols. You provide Metamath with certain special sequences (axioms) that tell it what rules of inference are allowed. Metamath is not limited to any specific field of mathematics. The Metamath language is simple and robust, with an almost total absence of hard-wired syntax, and we1 believe that it provides about the simplest possible framework that allows essentially all of mathematics to be expressed with absolute rigor.
Using the Metamath language, you can build formal or mathematical systems2 that involve inferences from axioms. Although a database is pro-vided that includes a recommended set of axioms for standard mathematics, if you wish you can supply your own symbols, syntax, axioms, rules, and definitions.
The name “Metamath” was chosen to suggest that the language provides a means for describing mathematics rather than being the mathematics itself. Actually in some sense any mathematical language is metamathematical. Symbols written on paper, or stored in a computer, are not mathematics itself but rather a way of expressing mathematics. For example “7” and “VII” are symbols for denoting the number seven in Arabic and Roman numerals; neither is the number seven.
If you are able to understand and write computer programs, you should be able to follow abstract mathematics with the aid of Metamath. Used in
1Unless otherwise noted, the words “I,” “me,” and “my” refer to Norman Megill, while “we,” “us,” and “our” refer to Norman Megill and David A. Wheeler.
2A formal or mathematical system consists of a collection of symbols (such as 2, 4, + and =), syntax rules that describe how symbols may be combined to form a legal expression (called a well-formed formula or wff, pronounced “whiff”), some starting wffs called axioms, and inference rules that describe how theorems may be derived (proved) from the axioms. A theorem is a mathematical fact such as 2 + 2 = 4. Strictly speaking, even an obvious fact such as this must be proved from axioms to be formally acceptable to a mathematician.
x PREFACE
conjunction with standard textbooks, Metamath can guide you step-by-step towards an understanding of abstract mathematics from a very rigorous viewpoint, even if you have no formal abstract mathematics background. By using a single, consistent notation to express proofs, once you grasp its basic concepts Metamath provides you with the ability to immediately follow and dissect proofs even in totally unfamiliar areas.
Of course, just being able follow a proof will not necessarily give you an intuitive familiarity with mathematics. Memorizing the rules of chess does not give you the ability to appreciate the game of a master, and knowing how the notes on a musical score map to piano keys does not give you the ability to hear in your head how it would sound. But each of these can be a first step.
Metamath allows you to explore proofs in the sense that you can see the theorem referenced at any step expanded in as much detail as you want, right down to the underlying axioms of logic and set theory (in the case of the set theory database provided). While Metamath will not replace the higher-level understanding that can only be acquired through exercises and hard work, being able to see how gaps in a proof are filled in can give you increased confidence that can speed up the learning process and save you time when you get stuck.
The Metamath language breaks down a mathematical proof into its tiniest possible parts. These can be pieced together, like interlocking pieces in a puzzle, only in a way that produces correct and absolutely rigorous mathematics.
The nature of Metamath enforces very precise mathematical thinking, similar to that involved in writing a computer program. A crucial difference, though, is that once a proof is verified (by the Metamath program) to be correct, it is definitely correct; it can never have a hidden “bug.” After getting used to the kind of rigor and accuracy provided by Metamath, you might even be tempted to adopt the attitude that a proof should never be considered correct until it has been verified by a computer, just as you would not completely trust a manual calculation until you have verified it on a calculator.
My goal for Metamath was a system for describing and verifying mathe-matics that is completely universal yet conceptually as simple as possible. In approaching mathematics from an axiomatic, formal viewpoint, I wanted Metamath to be able to handle almost any mathematical system, not nec-essarily with ease, but at least in principle and hopefully in practice. I wanted it to verify proofs with absolute rigor, and for this reason Metamath is what might be thought of as a “compile-only” language rather than an algorithmic or Turing-machine language (Pascal, C, Prolog, Mathematica, etc.). In other words, a database written in the Metamath language doesn’t “do” anything; it merely exhibits mathematical knowledge and permits this knowledge to be verified as being correct. A program in an algorithmic
PREFACE xi
language can potentially have hidden bugs as well as possibly being hard to understand. But each token in a Metamath database must be consistent with the database’s earlier contents according to simple, fixed rules. If a database is verified to be correct,3 then the mathematical content is correct if the verifier is correct and the axioms are correct. The verification program could be incorrect, but the verification algorithm is relatively simple (making it unlikely to be implemented incorrectly by the Metamath program), and there are over a dozen Metamath database verifiers written by different people in different programming languages (so these different verifiers can act as multiple reviewers of a database). The most-used Metamath database, the Metamath Proof Explorer (aka set.mm), is currently verified by four different Metamath verifiers written by four different people in four different languages, including the original Metamath program described in this book. The only “bugs” that can exist are in the statement of the axioms, for example if the axioms are inconsistent (a famous problem shown to be unsolvable by Gödel’s incompleteness theorem). However, real mathematical systems have very few axioms, and these can be carefully studied. All of this provides extraordinarily high confidence that the verified database is in fact correct.
The Metamath program doesn’t prove theorems automatically but is designed to verify proofs that you supply to it. The underlying Metamath language is completely general and has no built-in, preconceived notions about your formal system, its logic or its syntax. For constructing proofs, the Metamath program has a Proof Assistant which helps you fill in some of a proof step’s details, shows you what choices you have at any step, and verifies the proof as you build it; but you are still expected to provide the proof.
There are many other programs that can process or generate information in the Metamath language, and more continue to be written. This is in part because the Metamath language itself is very simple and intentionally easy to automatically process. Some programs, such as mmj2, include a proof assistant that can automate some steps beyond what the Metamath program can do. Mario Carneiro has developed an algorithm for converting proofs from the OpenTheory interchange format, which can be translated to and from any of the HOL family of proof languages (HOL4, HOL Light, ProofPower, and Isabelle), into the Metamath language [10]. Daniel Whalen has developed Holophrasm, which can automatically prove many Metamath proofs using machine learning approaches (including multiple neural net-works)[72]. However, a discussion of these other programs is beyond the scope of this book.
Like most computer languages, the Metamath language uses the standard (ascii) characters on a computer keyboard, so it cannot directly represent many of the special symbols that mathematicians use. A useful feature
3This includes verification that a sequential list of proof steps results in the specified theorem.
xii PREFACE
of the Metamath program is its ability to convert its notation into the LATEX typesetting language. This feature lets you convert the ascii tokens you’ve defined into standard mathematical symbols, so you end up with symbols and formulas you are familiar with instead of somewhat cryptic ascii representations of them. The Metamath program can also generate HTML, making it easy to view results on the web and to see related information by using hypertext links.
Metamath is probably conceptually different from anything you’ve seen before and some aspects may take some getting used to. This book will help you decide whether Metamath suits your specific needs.
Setting Your Expectations
It is important for you to understand what Metamath is and is not. As mentioned, the Metamath program is not an automated theorem prover but rather a proof verifier. Developing a database can be tedious, hard work, especially if you want to make the proofs as short as possible, but it becomes easier as you build up a collection of useful theorems. The purpose of Metamath is simply to document existing mathematics in an absolutely rigorous, computer-verifiable way, not to aid directly in the creation of new mathematics. It also is not a magic solution for learning abstract mathematics, although it may be helpful to be able to actually see the implied rigor behind what you are learning from textbooks, as well as providing hints to work out proofs that you are stumped on.
As of this writing, a sizable set theory database has been developed to provide a foundation for many fields of mathematics, but much more work would be required to develop useful databases for specific fields.
Metamath “knows no math;” it just provides a framework in which to express mathematics. Its language is very small. You can define two kinds of symbols, constants and variables. The only thing Metamath knows how to do is to substitute strings of symbols for the variables in an expression based on instructions you provide it in a proof, subject to certain constraints you specify for the variables. Even the decimal representation of a number is merely a string of certain constants (digits) which together, in a specific context, correspond to whatever mathematical object you choose to define for it; unlike other computer languages, there is no actual number stored inside the computer. In a proof, you in effect instruct Metamath what symbol substitutions to make in previous axioms or theorems and join a sequence of them together to result in the desired theorem. This kind of symbol manipulation captures the essence of mathematics at a preaxiomatic level.
Metamath and Mathematical Literature
In advanced mathematical literature, proofs are usually presented in the form of short outlines that often only an expert can follow. This is partly out
PREFACE xiii
of a desire for brevity, but it would also be unwise (even if it were practical) to present proofs in complete formal detail, since the overall picture would be lost.
A solution I envision that would allow mathematics to remain acceptable to the expert, yet increase its accessibility to non-specialists, consists of a combination of the traditional short, informal proof in print accompanied by a complete formal proof stored in a computer database. In an analogy with a computer program, the informal proof is like a set of comments that describe the overall reasoning and content of the proof, whereas the computer database is like the actual program and provides a means for anyone, even a non-expert, to follow the proof in as much detail as desired, exploring it back through layers of theorems (like subroutines that call other subroutines) all the way back to the axioms of the theory. In addition, the computer database would have the advantage of providing absolute assurance that the proof is correct, since each step can be verified automatically.
There are several other approaches besides Metamath to a project such as this. Section 1.3.4 discusses some of these.
To us, a noble goal would be a database with hundreds of thousands of theorems and their computer-verifiable proofs, encompassing a significant fraction of known mathematics and available for instant access. These would be fully verified by multiple independently-implemented verifiers, to provide extremely high confidence that the proofs are completely correct. The database would allow people to investigate whatever details they were interested in, so that they could confirm whatever portions they wished. Whether or not Metamath is an appropriate choice remains to be seen, but in principle we believe it is sufficient.
Formalism
Over the past fifty years, a group of French mathematicians working col-lectively under the pseudonym of Bourbaki have co-authored a series of monographs that attempt to rigorously and consistently formalize large bod-ies of mathematics from foundations. On the one hand, certainly such an effort has its merits; on the other hand, the Bourbaki project has been criti-cized for its “scholasticism” and “hyperaxiomatics” that hide the intuitive steps that lead to the results [3, p. 191].
Metamath unabashedly carries this philosophy to its extreme and no doubt is subject to the same kind of criticism. Nonetheless I think that in conjunction with conventional approaches to mathematics Metamath can serve a useful purpose. The Bourbaki approach is essentially pedagogic, requiring the reader to become intimately familiar with each detail in a very large hierarchy before he or she can proceed to the next step. The difference with Metamath is that the “reader” (user) knows that all details are contained in its computer database, available as needed; it does not demand that the user know everything but conveniently makes available those portions that
xiv PREFACE
are of interest. As the body of all mathematical knowledge grows larger and larger, no one individual can have a thorough grasp of its entirety. Metamath can finalize and put to rest any questions about the validity of any part of it and can make any part of it accessible, in principle, to a non-specialist.
A Personal Note
Why did I develop Metamath? I enjoy abstract mathematics, but I sometimes get lost in a barrage of definitions and start to lose confidence that my proofs are correct. Or I reach a point where I lose sight of how anything I’m doing relates to the axioms that a theory is based on and am sometimes suspicious that there may be some overlooked implicit axiom accidentally introduced along the way (as happened historically with Euclidean geometry, whose omission of Pasch’s axiom went unnoticed for 2000 years [15, p. 160]!). I’m also somewhat lazy and wish to avoid the effort involved in re-verifying the gaps in informal proofs “left to the reader;” I prefer to figure them out just once and not have to go through the same frustration a year from now when I’ve forgotten what I did. Metamath provides better recovery of my efforts than scraps of paper that I can’t decipher anymore. But mostly I find very appealing the idea of rigorously archiving mathematical knowledge in a computer database, providing precision, certainty, and elimination of human error.
Note on Bibliography and Index
The Bibliography usually includes the Library of Congress classification for a work to make it easier for you to find it in on a university library shelf. The Index has author references to pages where their works are cited, even though the authors’ names may not appear on those pages.
Acknowledgments
Acknowledgments are first due to my wife, Deborah (who passed away on September 4, 1998), for critiquing the manuscript but most of all for her patience and support. I also wish to thank Joe Wright, Richard Becker, Clarke Evans, Buddha Buck, and Jeremy Henty for helpful comments. Any errors, omissions, and other shortcomings are of course my responsibility.
Note Added June 22, 2005
The original, unpublished version of this book was written in 1997 and distributed via the web. The present edition has been updated to reflect the current Metamath program and databases, as well as more current urls for Internet sites. Thanks to Josh Purinton, One Hand Clapping, Mel L. O’Cat, and Roy F. Longton for pointing out typographical and other errors. I have also benefitted from numerous discussions with Raph Levien, who
PREFACE xv
has extended Metamath’s philosophy of rigor to result in his Ghilbert proof language (
http://ghilbert.org
).
Robert (Bob) Solovay communicated a new result of A. R. D. Mathias on the system of Bourbaki, and the text has been updated accordingly (p. 15).
Bob also pointed out a clarification of the literature regarding category theory and inaccessible cardinals (p. 34), and a misleading statement was removed from the text. Specifically, contrary to a statement in previous editions, it is possible to express “There is a proper class of inaccessible cardinals” in the language of ZFC. This can be done as follows: “For every set x there is an inaccessible cardinal κ such that κ is not in x.” Bob writes:4
This axiom is how Grothendieck presents category theory. To each inaccessible cardinal κ one associates a Grothendieck universe U(κ). U(κ) consists of those sets which lie in a transitive set of cardinality less than κ. Instead of the “category of all groups,” one works relative to a universe [considering the category of groups of cardinality less than κ]. Now the category whose objects are all categories “relative to the universe U(κ)” will be a category not relative to this universe but to the next universe.
All of the things category theorists like to do can be done in this framework. The only controversial point is whether the Grothendieck axiom is too strong for the needs of category the-orists. Mac Lane argues that “one universe is enough” and Feferman has argued that one can get by with ordinary ZFC. I don’t find Feferman’s arguments persuasive. Mac Lane may be right, but when I think about category theory I do it à la Grothendieck.
By the way Mizar adds the axiom “there is a proper class of inaccessibles” precisely so as to do category theory.
The most current information on the Metamath program and databases can always be found at
http://metamath.org
.
Note Added June 24, 2006
The Metamath spec was restricted slightly to make parsers easier to write. See the footnote on p. 114.
Note Added March 10, 2007
I am grateful to Anthony Williams for writing the LATEX package called realref.sty and contributing it to the public domain. This package allows the internal hyperlinks in a pdf file to anchor to specific page numbers instead of just section titles, making the navigation of the pdf file for this book much more pleasant and “logical.”
4Private communication, Nov. 30, 2002.
xvi PREFACE
A typographical error found by Martin Kiselkov was corrected. A confus-ing remark about unification was deleted per suggestion of Mel O’Cat.
Note Added May 27, 2009
Several typos found by Kim Sparre were corrected. A note was added that the Poincaré conjecture has been proved (p. 24).
Note Added Nov. 17, 2014
The statement of the Schröder–Bernstein theorem was corrected in Sec-tion 1.2.2. Thanks to Bob Solovay for pointing out the error.
Note Added May 25, 2016
Thanks to Jerry James for correcting 16 typos.
Note Added February 25, 2019
David A. Wheeler made a large number of improvements and updates, in coordination with Norman Megill. The predicate calculus axioms were renumbered, and the text makes it clear that they are based on Tarski’s system S2; the one slight deviation in axiom ax-6 is explained and justi-fied. The real and complex number axioms were modified to be consistent with set.mm. Long-awaited specification changes “1–8” were made, which clarified previously ambiguous points. Some errors in the text involving $f
and $d statements were corrected (the spec was correct, but the in-book explanations unintentionally contradicted the spec). We now have a system for automatically generating narrow PDFs, so that those with smartphones can have easy access to the current version of this document. A new section on deduction was added; it discusses the standard deduction theorem, the weak deduction theorem, deduction style, and natural deduction. Many minor corrections (too numerous to list here) were also made.
Note Added March 7, 2019
This added a description of the Matamath language syntax in Extended Backus–Naur Form (EBNF) in Appendix E, added a brief explanation about typecodes, inserted more examples in the deduction section, and added a variety of smaller improvements.
Note Added April 7, 2019
This version clarified the proper substitution notation, improved the discus-sion on the weak deduction theorem and natural deduction, documented the undo command, updated the information on write source, changed
PREFACE xvii
the typecode from set to setvar to be consistent with the current version of set.mm, added more documentation about comment markup (e.g., docu-mented how to create headings), and clarified the differences between various assertion forms (in particular deduction form).
Note Added June 2, 2019
This version fixes a large number of small issues reported by Benôıt Jubin, such as editorial issues and the need to document verify markup (thank you!). This version also includes specific examples of forms (deduction form, inference form, and closed form).
xviii PREFACE

Chapter 1

Introduction

I.M.: No, no. There’s nothing subjective about it! Everybody knows what a proof is. Just read some books, take courses from a competent mathematician, and you’ll catch on.
Student: Are you sure? I.M.: Well—it is possible that you won’t, if you don’t have
any aptitude for it. That can happen, too. Student: Then you decide what a proof is, and if I don’t learn
to decide in the same way, you decide I don’t have any aptitude. I.M.: If not me, then who?
“The Ideal Mathematician” 1
Brilliant mathematicians have discovered almost unimaginably profound results that rank among the crowning intellectual achievements of mankind. However, there is a sense in which modern abstract mathematics is behind the times, stuck in an era before computers existed. While no one disputes the remarkable results that have been achieved, communicating these results in a precise way to the uninitiated is virtually impossible. To describe these results, a terse informal language is used which despite its elegance is very difficult to learn. This informal language is not imprecise, far from it, but rather it often has omitted detail and symbols with hidden context that are implicitly understood by an expert but few others. Extremely complex technical meanings are associated with innocent-sounding English words such as “compact” and “measurable” that barely hint at what is actually being said. Anyone who does not keep the precise technical meaning constantly in mind is bound to fail, and acquiring the ability to do this can be achieved only through much practice and hard work. Only the few who complete the painful learning experience can join the small in-group of pure mathematicians. The informal language effectively cuts off the true nature of their knowledge from most everyone else.
1[15], p. 40.
2 CHAPTER 1. INTRODUCTION
Metamath makes abstract mathematics more concrete. It allows a com-puter to keep track of the complexity associated with each word or symbol with absolute rigor. You can explore this complexity at your leisure, to whatever degree you desire. Whether or not you believe that concepts such as infinity actually “exist” outside of the mind, Metamath lets you get to the foundation for what’s really being said.
Metamath also enables completely rigorous and thorough proof verifica-tion. Its language is simple enough so that you don’t have to rely on the authority of experts but can verify the results yourself, step by step. If you want to attempt to derive your own results, Metamath will not let you make a mistake in reasoning. Even professional mathematicians make mistakes; Metamath makes it possible to thoroughly verify that proofs are correct.
Metamath is a computer language and an associated computer program for archiving, verifying, and studying mathematical proofs at a very detailed level. The Metamath language describes formal mathematical systems and expresses proofs of theorems in those systems. Such a language is called a metalanguage by mathematicians. The Metamath program is a computer program that verifies proofs expressed in the Metamath language. The Metamath program does not have the built-in ability to make logical inferences; it just makes a series of symbol substitutions according to instructions given to it in a proof and verifies that the result matches the expected theorem. It makes logical inferences based only on rules of logic that are contained in a set of axioms, or first principles, that you provide to it as the starting point for proofs.
The complete specification of the Metamath language is only four pages long (Section 4.1, p. 112). Its simplicity may at first make you wonder how it can do much of anything at all. But in fact the kinds of symbol manipulations it performs are the ones that are implicitly done in all mathematical systems at the lowest level. You can learn it relatively quickly and have complete confidence in any mathematical proof that it verifies. On the other hand, it is powerful and general enough so that virtually any mathematical theory, from the most basic to the deeply abstract, can be described with it.
Although in principle Metamath can be used with any kind of mathe-matics, it is best suited for abstract or “pure” mathematics that is mostly concerned with theorems and their proofs, as opposed to the kind of math-ematics that deals with the practical manipulation of numbers. Examples of branches of pure mathematics are logic,2 set theory,3 number theory,4
2Logic is the study of statements that are universally true regardless of the objects being described by the statements. An example is the statement, “if P implies Q, then either P is false or Q is true.”
3Set theory is the study of general-purpose mathematical objects called “sets,” and from it essentially all of mathematics can be derived. For example, numbers can be defined as specific sets, and their properties can be explored using the tools of set theory.
4Number theory deals with the properties of positive and negative integers (whole numbers).
3 group theory,5 abstract algebra,6, analysis 7 and topology.8 Even in physics, Metamath could be applied to certain branches that make use of abstract mathematics, such as quantum logic (used to study aspects of quantum mechanics).
On the other hand, Metamath is less suited to applications that deal primarily with intensive numeric computations. Metamath does not have any built-in representation of numbers; instead, a specific string of symbols (digits) must be syntactically constructed as part of any proof in which an ordinary number is used. For this reason, numbers in Metamath are best limited to specific constants that arise during the course of a theorem or its proof. Numbers are only a tiny part of the world of abstract mathematics. The exclusion of built-in numbers was a conscious decision to help achieve Metamath’s simplicity, and there are other software tools if you have dif-ferent mathematical needs. If you wish to quickly solve algebraic problems, the computer algebra programs macsyma, Mathematica, and Maple are specifically suited to handling numbers and algebra efficiently. If you wish to simply calculate numeric or matrix expressions easily, tools such as Octave may be a better choice.
After learning Metamath’s basic statement types, any technically oriented person, mathematician or not, can immediately trace any theorem proved in the language as far back as he or she wants, all the way to the axioms on which the theorem is based. This ability suggests a non-traditional way of learning about pure mathematics. Used in conjunction with traditional methods, Metamath could make pure mathematics accessible to people who are not sufficiently skilled to figure out the implicit detail in ordinary textbook proofs. Once you learn the axioms of a theory, you can have complete confidence that everything you need to understand a proof you are studying is all there, at your beck and call, allowing you to focus in on any proof step you don’t understand in as much depth as you need, without worrying about getting stuck on a step you can’t figure out.9
5Group theory studies the properties of mathematical objects called groups that obey a simple set of axioms and have properties of symmetry that make them useful in many other fields.
6Abstract algebra includes group theory and also studies groups with additional properties that qualify them as “rings” and “fields.” The set of real numbers is a familiar example of a field.
7Analysis is the study of real and complex numbers. 8One area studied by topology are properties that remain unchanged when geometrical

[... content truncated ...]

---

*Source: `Metamath.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
