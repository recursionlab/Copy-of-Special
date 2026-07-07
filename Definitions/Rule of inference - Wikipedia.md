---
title: "Rule of inference - Wikipedia"
source: "https://en.wikipedia.org/wiki/Rule_of_inference"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2003-06-24
created: 2026-04-09
description:
tags:
  - "clippings"
---
![Diagram of an inference](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Modus_ponens2.svg/250px-Modus_ponens2.svg.png)

Modus ponens is one of the main rules of inference.

**Rules of inference** are ways of deriving conclusions from [premises](https://en.wikipedia.org/wiki/Premise "Premise"). They are integral parts of [formal logic](https://en.wikipedia.org/wiki/Formal_logic "Formal logic"), serving as the [logical structure](https://en.wikipedia.org/wiki/Logical_form "Logical form") of [valid](https://en.wikipedia.org/wiki/Validity_\(logic\) "Validity (logic)") arguments. If an argument with true premises follows a rule of inference then the conclusion cannot be false. *[Modus ponens](https://en.wikipedia.org/wiki/Modus_ponens "Modus ponens")*, an influential rule of inference, connects two premises of the form "if ${\displaystyle P}$ then ${\displaystyle Q}$ " and " ${\displaystyle P}$ " to the conclusion " ${\displaystyle Q}$ ", as in the argument "If it rains, then the ground is wet. It rains. Therefore, the ground is wet." There are many other rules of inference for different patterns of valid arguments, such as *[modus tollens](https://en.wikipedia.org/wiki/Modus_tollens "Modus tollens")*, [disjunctive syllogism](https://en.wikipedia.org/wiki/Disjunctive_syllogism "Disjunctive syllogism"), [constructive dilemma](https://en.wikipedia.org/wiki/Constructive_dilemma "Constructive dilemma"), and [existential generalization](https://en.wikipedia.org/wiki/Existential_generalization "Existential generalization").

Rules of inference include rules of implication, which operate only in one direction from premises to conclusions, and [rules of replacement](https://en.wikipedia.org/wiki/Rules_of_replacement "Rules of replacement"), which state that two expressions are equivalent and can be freely swapped. They contrast with [formal fallacies](https://en.wikipedia.org/wiki/Formal_fallacies "Formal fallacies") —invalid argument forms involving logical errors.

Logicians construct [formal systems](https://en.wikipedia.org/wiki/Formal_systems "Formal systems") to precisely capture and codify valid patterns of reasoning, with distinct systems using different rules of inference. For example, [propositional logic](https://en.wikipedia.org/wiki/Propositional_logic "Propositional logic") examines how [statements](https://en.wikipedia.org/wiki/Proposition "Proposition") formed through logical operators like "not" and "if...then..." support conclusions. [First-order logic](https://en.wikipedia.org/wiki/First-order_logic "First-order logic") extends propositional logic by analyzing how the internal structure of propositions, like names and [predicates](https://en.wikipedia.org/wiki/Predicate_\(logic\) "Predicate (logic)"), influences reasoning. Other logical systems explore inferential patterns associated with [what is possible and necessary](https://en.wikipedia.org/wiki/Modal_logic "Modal logic"), with [what people believe](https://en.wikipedia.org/wiki/Doxastic_logic "Doxastic logic"), and with [what happened at different times](https://en.wikipedia.org/wiki/Temporal_logic "Temporal logic"). Various formalisms are used to express logical systems. [Natural deduction](https://en.wikipedia.org/wiki/Natural_deduction "Natural deduction") systems employ many intuitive rules of inference to reflect how people naturally reason, while [Hilbert systems](https://en.wikipedia.org/wiki/Hilbert_system "Hilbert system") provide minimalistic frameworks to represent foundational principles without redundancy.

Rules of inference are relevant to many areas, such as [proofs](https://en.wikipedia.org/wiki/Mathematical_proof "Mathematical proof") in [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics") and [automated reasoning](https://en.wikipedia.org/wiki/Automated_reasoning "Automated reasoning") in [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"). Their conceptual and psychological underpinnings are studied by [philosophers of logic](https://en.wikipedia.org/wiki/Philosophy_of_logic "Philosophy of logic") and [cognitive psychologists](https://en.wikipedia.org/wiki/Cognitive_psychology "Cognitive psychology").

## Definition

A rule of [inference](https://en.wikipedia.org/wiki/Inference "Inference") is a way of drawing a conclusion from a set of [premises](https://en.wikipedia.org/wiki/Premise "Premise").[^16] Also called *inference rule* and *transformation rule*,[^17] it is a norm of correct inferences that can be used to guide [reasoning](https://en.wikipedia.org/wiki/Logical_reasoning "Logical reasoning"), justify conclusions, and criticize [arguments](https://en.wikipedia.org/wiki/Argument "Argument"). As part of [deductive](https://en.wikipedia.org/wiki/Deductive_reasoning "Deductive reasoning") logic, rules of inference are argument forms that preserve the [truth](https://en.wikipedia.org/wiki/Truth "Truth") of the premises, meaning that the conclusion is always true if the premises are true.[^1] An inference is deductively [valid](https://en.wikipedia.org/wiki/Validity_\(logic\) "Validity (logic)") if it follows a correct rule of inference. Whether this is the case depends only on the [form or syntactic structure](https://en.wikipedia.org/wiki/Logical_form "Logical form") of the premises and the conclusion, that is, the actual content or concrete meaning of the statements does not affect validity. For instance, *[modus ponens](https://en.wikipedia.org/wiki/Modus_ponens "Modus ponens")* is a rule of inference that connects two premises of the form "if ${\displaystyle P}$ then ${\displaystyle Q}$ " and " ${\displaystyle P}$ " to the conclusion " ${\displaystyle Q}$ ". The letters ${\displaystyle P}$ and ${\displaystyle Q}$ in this example and in later formulas are so-called [metavariables](https://en.wikipedia.org/wiki/Metavariable "Metavariable"): they stand for any simple or compound [proposition](https://en.wikipedia.org/wiki/Proposition "Proposition").[^19] Any argument following *modus ponens* is valid, independent of the specific meanings of ${\displaystyle P}$ and ${\displaystyle Q}$, such as the argument "If it is day, then it is light. It is day. Therefore, it is light." [^20] In addition to ' *modus ponens*, there are many other rules of inference, such as *[modus tollens](https://en.wikipedia.org/wiki/Modus_tollens "Modus tollens")*, [disjunctive syllogism](https://en.wikipedia.org/wiki/Disjunctive_syllogism "Disjunctive syllogism"), and [constructive dilemma](https://en.wikipedia.org/wiki/Constructive_dilemma "Constructive dilemma").[^19]

There are different formats to represent rules of inference. A common approach is to use a new line for each premise and to separate the premises from the conclusion using a horizontal line. With this format, *modus ponens* is written as:[^21] [^2] 
$$
{\displaystyle {\begin{array}{l}P\to Q\\P\\\hline Q\end{array}}}
$$

Some logicians employ the [therefore sign](https://en.wikipedia.org/wiki/Therefore_sign "Therefore sign") (${\displaystyle \therefore }$) either together with or instead of the horizontal line to indicate where the conclusion begins.[^23] The [sequent](https://en.wikipedia.org/wiki/Sequent "Sequent") notation, a different approach, uses a single line in which the premises are separated by commas and connected to the conclusion with the [turnstile symbol](https://en.wikipedia.org/wiki/Turnstile_symbol "Turnstile symbol") (${\displaystyle \vdash }$), as in ${\displaystyle P\to Q,P\vdash Q}$.[^24]

Rules of inference are part of [logical systems](https://en.wikipedia.org/wiki/Formal_system "Formal system") and different systems employ distinct sets of rules. For example, [universal instantiation](https://en.wikipedia.org/wiki/Universal_instantiation "Universal instantiation") [^3] is a rule of inference in the system of [first-order logic](https://en.wikipedia.org/wiki/First-order_logic "First-order logic") but not in [propositional logic](https://en.wikipedia.org/wiki/Propositional_logic "Propositional logic").[^26] Rules of inference play a central role in [proofs](https://en.wikipedia.org/wiki/Formal_proof "Formal proof") as explicit procedures for deriving new lines of a proof from preceding lines. Proofs involve a series of inferential steps and often use various rules of inference to establish the [theorem](https://en.wikipedia.org/wiki/Theorem "Theorem") they intend to demonstrate.[^27] [^4] Rules of inference are definitory rules—rules about which inferences are allowed. They contrast with strategic rules, which govern the inferential steps needed to prove a certain theorem from a specific set of premises. Mastering definitory rules by itself is not sufficient for effective reasoning since they provide little guidance on how to reach the intended conclusion.[^29] [^5] As standards or procedures governing the transformation of symbolic expressions, rules of inference are similar to [mathematical functions](https://en.wikipedia.org/wiki/Mathematical_function "Mathematical function") taking premises as input and producing a conclusion as output. According to one interpretation, rules of inference are inherent in [logical operators](https://en.wikipedia.org/wiki/Logical_operator "Logical operator") [^6] found in statements, making the meaning and function of these operators explicit without adding any additional information.[^32]

![Black-and-white drawing of a man with sideburns, dressed in a dark formal attire with a white high-collared shirt](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/PSM_V17_D740_George_Boole.jpg/250px-PSM_V17_D740_George_Boole.jpg)

George Boole (1815–1864) made key contributions to symbolic logic in general and propositional logic in particular. 33

Logicians distinguish two types of rules of inference: rules of implication and [rules of replacement](https://en.wikipedia.org/wiki/Rules_of_replacement "Rules of replacement").[^7] Rules of implication, like *modus ponens*, operate only in one direction, meaning that the conclusion can be deduced from the premises, but the premises cannot be deduced from the conclusion. Rules of replacement, by contrast, operate in both directions, stating that two expressions are equivalent and can be freely replaced with each other. In classical logic, for example, a proposition (${\displaystyle P}$) is equivalent to the negation [^8] of its negation (${\displaystyle \lnot \lnot P}$).[^9] As a result, one can infer one from the other in either direction, making it a rule of replacement. Other rules of replacement include [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws") as well as the [commutative](https://en.wikipedia.org/wiki/Commutative_property "Commutative property") and [associative properties](https://en.wikipedia.org/wiki/Associative_property "Associative property") of [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction "Logical conjunction") and [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction "Logical disjunction"). While rules of implication apply only to complete statements, rules of replacement can be applied to any part of a compound statement.[^37]

Deductive rules of inference differ from defeasible [argumentation schemes](https://en.wikipedia.org/wiki/Argumentation_scheme "Argumentation scheme"), which describe patterns of reasoning that provide some support to a conclusion without guaranteeing its truth, such as the [argument from authority](https://en.wikipedia.org/wiki/Argument_from_authority "Argument from authority") and the [argument from analogy](https://en.wikipedia.org/wiki/Argument_from_analogy "Argument from analogy"). However, the term "rule of inference" is sometimes used in a looser sense to include non-deductive argumentation schemes.[^38] Similarly, the term is occasionally interpreted broadly to include general standards of research, such as the principle that [scientific experiments](https://en.wikipedia.org/wiki/Scientific_experiments "Scientific experiments") should be [replicable](https://en.wikipedia.org/wiki/Reproducibility "Reproducibility").[^39]

One of the first discussions of formal rules of inference dates to [antiquity](https://en.wikipedia.org/wiki/Ancient_history "Ancient history"), in [Aristotle's logic](https://en.wikipedia.org/wiki/Aristotle%27s_logic "Aristotle's logic"). His explanations of valid [syllogisms](https://en.wikipedia.org/wiki/Syllogisms "Syllogisms") were further refined in [medieval](https://en.wikipedia.org/wiki/Medieval_philosophy "Medieval philosophy") and [early modern philosophy](https://en.wikipedia.org/wiki/Early_modern_philosophy "Early modern philosophy"). The development of [symbolic logic](https://en.wikipedia.org/wiki/Symbolic_logic "Symbolic logic") in the 19th century, such as [George Boole](https://en.wikipedia.org/wiki/George_Boole "George Boole") 's articulation of [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra "Boolean algebra"), led to the formulation of many additional rules of inference belonging to [classical](https://en.wikipedia.org/wiki/Classical_logic "Classical logic") propositional and first-order logic. In the 20th and 21st centuries, logicians developed various [non-classical](https://en.wikipedia.org/wiki/Non-classical_logic "Non-classical logic") systems of logic with alternative rules of inference.[^40]

## Basic concepts

Rules of inference describe the structure of arguments, which consist of premises that support a conclusion.[^41] Premises and conclusions are statements or propositions about what is true. For instance, the assertion "The door is open." is a statement that is either true or false, while the question "Is the door open?" and the command "Open the door!" are not statements and have no truth value.[^42] An inference is a step of reasoning from premises to a conclusion, while an argument is the outward expression of an inference.[^43]

[Logic](https://en.wikipedia.org/wiki/Logic "Logic") is the study of correct reasoning and examines how to distinguish good from bad arguments.[^44] Deductive logic is the branch that investigates the strongest arguments, called deductively valid arguments, for which the conclusion cannot be false if all the premises are true. This is expressed by saying that the conclusion is a [logical consequence](https://en.wikipedia.org/wiki/Logical_consequence "Logical consequence") of the premises. Rules of inference belong to deductive logic and describe argument forms that fulfill this requirement.[^45] In order to precisely assess whether an argument follows a rule of inference, logicians use [formal languages](https://en.wikipedia.org/wiki/Formal_languages "Formal languages") to express statements in a rigorous manner, similar to [mathematical formulas](https://en.wikipedia.org/wiki/Mathematical_formula "Mathematical formula").[^46] They combine formal languages with rules of inference to construct [formal systems](https://en.wikipedia.org/wiki/Formal_systems "Formal systems") —frameworks for formulating propositions and drawing conclusions.[^10] Different formal systems may employ different formal languages or different rules of inference.[^48] [^11] The basic rules of inference within a formal system can often be expanded by introducing new rules, known as *[admissible rules](https://en.wikipedia.org/wiki/Admissible_rule "Admissible rule")*. Admissible rules do not change which arguments in a formal system are valid but can simplify proofs. If an admissible rule can be expressed through a combination of the system's basic rules, it is called a *derived* or *derivable rule*.[^50] Statements that can be deduced in a formal system are called *[theorems](https://en.wikipedia.org/wiki/Theorem "Theorem")* of this formal system.[^51] Widely used systems of logic include [propositional logic](https://en.wikipedia.org/wiki/Propositional_logic "Propositional logic"), [first-order logic](https://en.wikipedia.org/wiki/First-order_logic "First-order logic"), and [modal logic](https://en.wikipedia.org/wiki/Modal_logic "Modal logic").[^52]

Rules of inference only ensure that the conclusion is true if the premises are true. An argument with false premises can still be valid, but its conclusion may be false. For example, the argument "If pigs can fly, then the sky is purple. Pigs can fly. Therefore, the sky is purple." is valid because it follows *modus ponens*, even though it contains false premises. A valid argument is called a *[sound argument](https://en.wikipedia.org/wiki/Soundness "Soundness")* if all of its premises are true.[^53]

Rules of inference are closely related to [tautologies](https://en.wikipedia.org/wiki/Tautology_\(logic\) "Tautology (logic)") or [logical truths](https://en.wikipedia.org/wiki/Logical_truth "Logical truth"). In logic, a tautology is a statement that is true only because of the logical vocabulary it uses, independent of the meanings of its non-logical vocabulary. For example, the statement "if the tree is green and the sky is blue then the tree is green" is true independently of the meanings of terms like *tree* and *green*, making it a tautology. Every argument following a rule of inference can be transformed into a tautology. This is achieved by forming a [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction "Logical conjunction") (*and*) of all premises and connecting it through [implication](https://en.wikipedia.org/wiki/Material_conditional "Material conditional") (*if... then...*) to the conclusion, thereby combining all the individual statements of the argument into a single statement. For example, the valid argument "The tree is green and the sky is blue. Therefore, the tree is green." can be transformed into the tautology "if the tree is green and the sky is blue then the tree is green".[^54]

Rules of inference are not the only way to demonstrate that an argument is valid. Alternative methods include the use of [truth tables](https://en.wikipedia.org/wiki/Truth_table "Truth table"), which apply to propositional logic, and [truth trees](https://en.wikipedia.org/wiki/Truth_tree "Truth tree"), which can also be employed in first-order logic.[^55]

## Systems of logic

### Classical

#### Propositional logic

Propositional logic examines the inferential patterns of simple and compound [propositions](https://en.wikipedia.org/wiki/Proposition "Proposition"). It uses letters, such as ${\displaystyle P}$ and ${\displaystyle Q}$, to represent simple propositions. Compound propositions are formed by modifying or combining simple propositions with [logical operators](https://en.wikipedia.org/wiki/Logical_operator "Logical operator"), such as ${\displaystyle \lnot }$ (*not*), ${\displaystyle \land }$ (*and*), ${\displaystyle \lor }$ (*or*), and ${\displaystyle \to }$ (*if... then...*). For example, if ${\displaystyle P}$ stands for the statement "it is raining" and ${\displaystyle Q}$ stands for the statement "the streets are wet", then ${\displaystyle \lnot P}$ expresses "it is not raining" and ${\displaystyle P\to Q}$ expresses "if it is raining then the streets are wet". These logical operators are [truth-functional](https://en.wikipedia.org/wiki/Truth-functional "Truth-functional"), meaning that the truth value of a compound proposition depends only on the truth values of the simple propositions composing it. For instance, the compound proposition ${\displaystyle P\land Q}$ is only true if both ${\displaystyle P}$ and ${\displaystyle Q}$ are true; in all other cases, it is false. Propositional logic is not concerned with the concrete meaning of propositions other than their truth values.[^56] Key rules of inference in propositional logic are *[modus ponens](https://en.wikipedia.org/wiki/Modus_ponens "Modus ponens")*, *[modus tollens](https://en.wikipedia.org/wiki/Modus_tollens "Modus tollens")*, [hypothetical syllogism](https://en.wikipedia.org/wiki/Hypothetical_syllogism "Hypothetical syllogism"), [disjunctive syllogism](https://en.wikipedia.org/wiki/Disjunctive_syllogism "Disjunctive syllogism"), and [double negation elimination](https://en.wikipedia.org/wiki/Double_negation_elimination "Double negation elimination"). Further rules include [conjunction introduction](https://en.wikipedia.org/wiki/Conjunction_introduction "Conjunction introduction"), [conjunction elimination](https://en.wikipedia.org/wiki/Conjunction_elimination "Conjunction elimination"), [disjunction introduction](https://en.wikipedia.org/wiki/Disjunction_introduction "Disjunction introduction"), [disjunction elimination](https://en.wikipedia.org/wiki/Disjunction_elimination "Disjunction elimination"), [constructive dilemma](https://en.wikipedia.org/wiki/Constructive_dilemma "Constructive dilemma"), [destructive dilemma](https://en.wikipedia.org/wiki/Destructive_dilemma "Destructive dilemma"), [absorption](https://en.wikipedia.org/wiki/Absorption_\(logic\) "Absorption (logic)"), and [De Morgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws "De Morgan's laws").[^57]

| Rule of inference | Form | Example |
| --- | --- | --- |
| *Modus ponens* | ${\displaystyle {\begin{array}{l}P\to Q\\P\\\hline Q\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{If Kim is in Seoul, then Kim is in South Korea.}}\\{\text{Kim is in Seoul.}}\\\hline {\text{Therefore, Kim is in South Korea.}}\end{array}}}$ |
| *Modus tollens* | ${\displaystyle {\begin{array}{l}P\to Q\\\lnot Q\\\hline \lnot P\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{If Koko is a koala, then Koko is cuddly.}}\\{\text{Koko is not cuddly.}}\\\hline {\text{Therefore, Koko is not a koala.}}\end{array}}}$ |
| Hypothetical syllogism | ${\displaystyle {\begin{array}{l}P\to Q\\Q\to R\\\hline P\to R\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{If Leo is a lion, then Leo roars.}}\\{\text{If Leo roars, then Leo is fierce.}}\\\hline {\text{Therefore, if Leo is a lion, then Leo is fierce.}}\end{array}}}$ |
| Disjunctive syllogism | ${\displaystyle {\begin{array}{l}P\lor Q\\\lnot P\\\hline Q\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{The book is on the shelf or on the table.}}\\{\text{The book is not on the shelf.}}\\\hline {\text{Therefore, the book is on the table. }}\end{array}}}$ |
| Double negation elimination | ${\displaystyle {\begin{array}{l}\lnot \lnot P\\\hline P\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{We were not unable to meet the deadline.}}\\\hline {\text{We were able to meet the deadline. }}\end{array}}}$ |

#### First-order logic

![Photo of a bronze bust of a bearded man](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Wismar_Marienkirche_Bronzeb%C3%BCste_Gottlob_Frege_%2801-1%29.JPG/250px-Wismar_Marienkirche_Bronzeb%C3%BCste_Gottlob_Frege_%2801-1%29.JPG)

As one of the founding fathers of modern logic, Gottlob Frege (1848–1925) explored some of the foundational concepts of first-order logic. 59

First-order logic also employs the logical operators from propositional logic but includes additional devices to articulate the internal structure of propositions. Basic propositions in first-order logic consist of a [predicate](https://en.wikipedia.org/wiki/Predicate_\(logic\) "Predicate (logic)"), symbolized with uppercase letters like ${\displaystyle P}$ and ${\displaystyle Q}$, which is applied to [singular terms](https://en.wikipedia.org/wiki/Singular_term "Singular term"), symbolized with lowercase letters like ${\displaystyle a}$ and ${\displaystyle b}$. For example, if ${\displaystyle a}$ stands for "Aristotle" and ${\displaystyle P}$ stands for "is a philosopher", then the formula ${\displaystyle P(a)}$ means that "Aristotle is a philosopher". Another innovation of first-order logic is the use of the [quantifiers](https://en.wikipedia.org/wiki/Quantifier_\(logic\) "Quantifier (logic)") ${\displaystyle \exists }$ and ${\displaystyle \forall }$, which express that a predicate applies to some or all individuals. For instance, the formula ${\displaystyle \exists xP(x)}$ expresses that philosophers exist, while ${\displaystyle \forall xP(x)}$ expresses that everyone is a philosopher. The rules of inference from propositional logic are also valid in first-order logic.[^60] Additionally, first-order logic introduces new rules of inference that govern the role of singular terms, predicates, and quantifiers in arguments. Key rules of inference are [universal instantiation](https://en.wikipedia.org/wiki/Universal_instantiation "Universal instantiation") and [existential generalization](https://en.wikipedia.org/wiki/Existential_generalization "Existential generalization"). Other rules of inference include [universal generalization](https://en.wikipedia.org/wiki/Universal_generalization "Universal generalization") and [existential instantiation](https://en.wikipedia.org/wiki/Existential_instantiation "Existential instantiation").[^25]

| Rule of inference | Form | Example |
| --- | --- | --- |
| Universal instantiation | ${\displaystyle {\begin{array}{l}\forall xP(x)\\\hline P(a)\end{array}}}$ [^12] | ${\displaystyle {\begin{array}{l}{\text{Everyone must pay taxes.}}\\\hline {\text{Therefore, Wesley must pay taxes.}}\end{array}}}$ |
| Existential generalization | ${\displaystyle {\begin{array}{l}P(a)\\\hline \exists xP(x)\end{array}}}$ | ${\displaystyle {\begin{array}{l}{\text{Socrates is mortal.}}\\\hline {\text{Therefore, someone is mortal.}}\end{array}}}$ |

### Modal logics

Modal logics are formal systems that extend propositional logic and first-order logic with additional operators. Alethic modal logic introduces the operator ${\displaystyle \Diamond }$ to express that something is possible and the operator ${\displaystyle \Box }$ to express that something is necessary. For example, if ${\displaystyle P}$ means that "Parvati works", then ${\displaystyle \Diamond P}$ means that "It is possible that Parvati works", while ${\displaystyle \Box P}$ means that "It is necessary that Parvati works". These two operators are related by a rule of replacement stating that ${\displaystyle \Box P}$ is equivalent to ${\displaystyle \lnot \Diamond \lnot P}$. In other words: if something is necessarily true then it is not possible that it is not true. Further rules of inference include the necessitation rule, which asserts that a statement is necessarily true if it is provable in a formal system without any additional premises, and the distribution axiom, which allows one to derive ${\displaystyle \Diamond P\to \Diamond Q}$ from ${\displaystyle \Diamond (P\to Q)}$. These rules of inference belong to system K, a weak form of modal logic with only the most basic rules of inference. Many formal systems of alethic modal logic include additional rules of inference, such as system T, which allows one to deduce ${\displaystyle P}$ from ${\displaystyle \Box P}$.[^61]

Non-alethic systems of modal logic introduce operators that behave like ${\displaystyle \Diamond }$ and ${\displaystyle \Box }$ in alethic modal logic, following similar rules of inference but with different meanings. [Deontic logic](https://en.wikipedia.org/wiki/Deontic_logic "Deontic logic") is one type of non-alethic logic. It uses the operator ${\displaystyle \mathbf {P} }$ to express that an action is permitted and the operator ${\displaystyle \mathbf {O} }$ to express that an action is required, where ${\displaystyle \mathbf {P} }$ behaves similarly to ${\displaystyle \Diamond }$ and ${\displaystyle \mathbf {O} }$ behaves similarly to ${\displaystyle \Box }$. For instance, the rule of replacement in alethic modal logic, which asserts that ${\displaystyle \Box Q}$ is equivalent to ${\displaystyle \lnot \Diamond \lnot Q}$, also applies to deontic logic. As a result, one can deduce from ${\displaystyle \mathbf {O} Q}$ (e.g., Quinn has an obligation to help) that ${\displaystyle \lnot \mathbf {P} \lnot Q}$ (e.g., Quinn is not permitted not to help).[^62] Other systems of modal logic include [temporal modal logic](https://en.wikipedia.org/wiki/Temporal_logic "Temporal logic"), which has operators for what is always or sometimes the case, as well as [doxastic](https://en.wikipedia.org/wiki/Doxastic_logic "Doxastic logic") and [epistemic modal logics](https://en.wikipedia.org/wiki/Epistemic_modal_logic "Epistemic modal logic"), which have operators for what people believe and know.[^63]

### Other systems

![Photo of a marble bust of a bearded man](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Aristotle_Altemps_Inv8575.jpg/250px-Aristotle_Altemps_Inv8575.jpg)

The rules of inference in Aristotle 's (384–322 BCE) logic have the form of syllogisms. 64

Many other systems of logic have been proposed.[^65] In [ancient Greece](https://en.wikipedia.org/wiki/Ancient_Greece "Ancient Greece"), one of the earliest systems was [Aristotelian logic](https://en.wikipedia.org/wiki/Aristotelian_logic "Aristotelian logic"), according to which each statement is made up of two [terms](https://en.wikipedia.org/wiki/Term_logic "Term logic"), a subject and a predicate, connected by a [copula](https://en.wikipedia.org/wiki/Copula_\(linguistics\) "Copula (linguistics)"). For example, the statement "all humans are mortal" has the subject "all humans", the predicate "mortal", and the copula "is". All rules of inference in Aristotelian logic have the form of [syllogisms](https://en.wikipedia.org/wiki/Syllogism "Syllogism"), which consist of two premises and a conclusion. For instance, the *Barbara* rule of inference describes the validity of arguments of the form "All men are mortal. All Greeks are men. Therefore, all Greeks are mortal." [^66] The [Nyaya](https://en.wikipedia.org/wiki/Nyaya "Nyaya") school in [ancient India](https://en.wikipedia.org/wiki/Ancient_India "Ancient India") also explored rules of inference in the form of syllogisms, such as the argument "All things which have smoke have fire. This hill has smoke. Therefore, this hill has fire." [^67]

[Second-order logic](https://en.wikipedia.org/wiki/Second-order_logic "Second-order logic") extends first-order logic by allowing quantifiers to apply to predicates in addition to singular terms. For example, to express that the individuals Adam (${\displaystyle a}$) and Bianca (${\displaystyle b}$) share a property, one can use the formula ${\displaystyle \exists X(X(a)\land X(b))}$.[^68] Second-order logic also comes with new rules of inference.[^13] For instance, one can infer ${\displaystyle P(a)}$ (Adam is a philosopher) from ${\displaystyle \forall XX(a)}$ (every property applies to Adam).[^70]

[Intuitionistic logic](https://en.wikipedia.org/wiki/Intuitionistic_logic "Intuitionistic logic") is a non-classical variant of propositional and first-order logic. It shares with them many rules of inference, such as *modus ponens*, but excludes certain rules. For example, in classical logic, one can infer ${\displaystyle P}$ from ${\displaystyle \lnot \lnot P}$ using the rule of double negation elimination. However, in intuitionistic logic, this inference is invalid. As a result, every theorem that can be deduced in intuitionistic logic can also be deduced in classical logic, but some theorems provable in classical logic cannot be proven in intuitionistic logic.[^71] One motivation for this modification is the idea that proofs should demonstrate that an object exists or can be [constructed](https://en.wikipedia.org/wiki/Constructive_proof "Constructive proof"), not merely that its nonexistence would lead to a contradiction.[^72]

[Paraconsistent logics](https://en.wikipedia.org/wiki/Paraconsistent_logics "Paraconsistent logics") revise classical logic to allow the existence of [contradictions](https://en.wikipedia.org/wiki/Contradiction_\(logic\) "Contradiction (logic)"). In logic, a contradiction happens if the same proposition is both affirmed and denied, meaning that a formal system contains both ${\displaystyle P}$ and ${\displaystyle \lnot P}$ as theorems. Classical logic prohibits contradictions because classical rules of inference bring with them the [principle of explosion](https://en.wikipedia.org/wiki/Principle_of_explosion "Principle of explosion"), an admissible rule of inference that makes it possible to infer ${\displaystyle Q}$ from the premises ${\displaystyle P}$ and ${\displaystyle \lnot P}$. Since ${\displaystyle Q}$ is unrelated to ${\displaystyle P}$, any arbitrary statement can be deduced from a contradiction, making the affected systems useless for deciding what is true and false.[^73] [^14] Paraconsistent logics solve this problem by modifying the rules of inference in such a way that the principle of explosion is not an admissible rule of inference. As a result, it is possible to reason about inconsistent information without deriving absurd conclusions.[^75]

[Many-valued logics](https://en.wikipedia.org/wiki/Many-valued_logics "Many-valued logics") modify classical logic by introducing additional truth values. In classical logic, a proposition is either true or false with nothing in between. In many-valued logics, some propositions are neither true nor false. [Kleene logic](https://en.wikipedia.org/wiki/Kleene_logic "Kleene logic"), for example, is a [three-valued logic](https://en.wikipedia.org/wiki/Three-valued_logic "Three-valued logic") that introduces the additional truth value *undefined* to describe situations where information is incomplete or uncertain.[^76] Many-valued logics have adjusted rules of inference to accommodate the additional truth values. For instance, the classical rule of replacement stating that ${\displaystyle P\to Q}$ is equivalent to ${\displaystyle \lnot P\lor Q}$ is invalid in many three-valued systems.[^77] Some many-valued logics take the form of [probability logics](https://en.wikipedia.org/wiki/Probabilistic_logic "Probabilistic logic"), which make it possible to reason from uncertain information to [probabilistic](https://en.wikipedia.org/wiki/Probability "Probability") conclusions.[^78]

## Formalisms

Various formalisms or [proof systems](https://en.wikipedia.org/wiki/Proof_system "Proof system") have been suggested as distinct ways of codifying reasoning and demonstrating the validity of arguments. Unlike different systems of logic, these formalisms do not impact what can be proven; they only influence how proofs are formulated. Influential frameworks include [natural deduction](https://en.wikipedia.org/wiki/Natural_deduction "Natural deduction") systems, [Hilbert systems](https://en.wikipedia.org/wiki/Hilbert_systems "Hilbert systems"), and [sequent calculi](https://en.wikipedia.org/wiki/Sequent_calculi "Sequent calculi").[^79]

Natural deduction systems aim to reflect how people naturally reason by introducing many intuitive rules of inference to make logical derivations more accessible. They break complex arguments into simple steps, often using subproofs based on temporary premises. The rules of inference in natural deduction target specific logical operators, governing how an operator can be added with introduction rules or removed with elimination rules. For example, the rule of [conjunction introduction](https://en.wikipedia.org/wiki/Conjunction_introduction "Conjunction introduction") asserts that one can infer ${\displaystyle P\land Q}$ from the premises ${\displaystyle P}$ and ${\displaystyle Q}$, thereby producing a conclusion with the conjunction operator from premises that do not contain it. Conversely, the rule of [conjunction elimination](https://en.wikipedia.org/wiki/Conjunction_elimination "Conjunction elimination") asserts that one can infer ${\displaystyle P}$ from ${\displaystyle P\land Q}$, thereby producing a conclusion that no longer includes the conjunction operator. Similar rules of inference are [disjunction introduction](https://en.wikipedia.org/wiki/Disjunction_introduction "Disjunction introduction") and [elimination](https://en.wikipedia.org/wiki/Disjunction_elimination "Disjunction elimination"), [implication introduction](https://en.wikipedia.org/wiki/Implication_introduction "Implication introduction") and [elimination](https://en.wikipedia.org/wiki/Implication_elimination "Implication elimination"), [negation introduction](https://en.wikipedia.org/wiki/Negation_introduction "Negation introduction") and [elimination](https://en.wikipedia.org/wiki/Negation_elimination "Negation elimination"), and [biconditional introduction](https://en.wikipedia.org/wiki/Biconditional_introduction "Biconditional introduction") and [elimination](https://en.wikipedia.org/wiki/Biconditional_elimination "Biconditional elimination"). As a result, systems of natural deduction usually include many rules of inference.[^80] [^15]

Hilbert systems, by contrast, aim to provide a minimal and efficient framework of logical reasoning by including as few rules of inference as possible. Many Hilbert systems only have *modus ponens* as the sole rule of inference. To ensure that all theorems can be deduced from this minimal foundation, they introduce [axiom schemes](https://en.wikipedia.org/wiki/Axiom_schema "Axiom schema").[^82] An axiom scheme is a template to create axioms or true statements. It uses metavariables—placeholders that can be replaced by specific terms or formulas to generate an infinite number of true statements.[^83] For example, propositional logic can be defined with the following three axiom schemes: (1) ${\displaystyle P\to (Q\to P)}$, (2) ${\displaystyle (P\to (Q\to R))\to ((P\to Q)\to (P\to R))}$, and (3) ${\displaystyle (\lnot P\to \lnot Q)\to (Q\to P)}$.[^84] To formulate proofs, logicians create new statements from axiom schemes and then apply *modus ponens* to these statements to derive conclusions. Compared to natural deduction, this procedure tends to be less intuitive since its heavy reliance on symbolic manipulation can obscure the underlying logical reasoning.[^85]

Sequent calculi, another approach, introduce [sequents](https://en.wikipedia.org/wiki/Sequent "Sequent") as formal representations of arguments. A sequent has the form ${\displaystyle A_{1},\dots ,A_{m}\vdash B_{1},\dots ,B_{n}}$, where ${\displaystyle A_{i}}$ and ${\displaystyle B_{i}}$ stand for propositions. Sequents are conditional assertions stating that at least one ${\displaystyle B_{i}}$ is true if all ${\displaystyle A_{i}}$ are true. Rules of inference operate on sequents to produce additional sequents. Sequent calculi define two rules of inference for each logical operator: one to introduce it on the left side of a sequent and another to introduce it on the right side. For example, through the rule for introducing the operator ${\displaystyle \lnot }$ on the left side, one can infer ${\displaystyle \lnot R,P\vdash Q}$ from ${\displaystyle P\vdash Q,R}$. The [cut rule](https://en.wikipedia.org/wiki/Cut_rule "Cut rule"), an additional rule of inference, makes it possible to simplify sequents by removing certain propositions.[^86]

## Formal fallacies

![Diagram of modus ponens and affirming the consequent](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Modus_ponens_%26_affirming_the_consequent.svg/250px-Modus_ponens_%26_affirming_the_consequent.svg.png)

Affirming the consequent is a formal fallacy that resembles the valid rule of inference modus ponens. 87

While rules of inference describe valid patterns of deductive reasoning, formal fallacies are invalid argument forms that involve [logical errors](https://en.wikipedia.org/wiki/Fallacy "Fallacy"). The premises of a formal fallacy do not properly support its conclusion: the conclusion can be false even if all premises are true. Formal fallacies often mimic the structure of valid rules of inference and can thereby mislead people into unknowingly committing them and accepting their conclusions.[^88]

The formal fallacy of [affirming the consequent](https://en.wikipedia.org/wiki/Affirming_the_consequent "Affirming the consequent") concludes ${\displaystyle P}$ from the premises ${\displaystyle P\to Q}$ and ${\displaystyle Q}$, as in the argument "If Leo is a cat, then Leo is an animal. Leo is an animal. Therefore, Leo is a cat." This fallacy resembles valid inferences following *modus ponens*, with the key difference that the fallacy swaps the second premise and the conclusion.[^87] The formal fallacy of [denying the antecedent](https://en.wikipedia.org/wiki/Denying_the_antecedent "Denying the antecedent") concludes ${\displaystyle \lnot Q}$ from the premises ${\displaystyle P\to Q}$ and ${\displaystyle \lnot P}$, as in the argument "If Laya saw the movie, then Laya had fun. Laya did not see the movie. Therefore, Laya did not have fun." This fallacy resembles valid inferences following *modus tollens*, with the key difference that the fallacy swaps the second premise and the conclusion.[^89] Other formal fallacies include [affirming a disjunct](https://en.wikipedia.org/wiki/Affirming_a_disjunct "Affirming a disjunct"), the [existential fallacy](https://en.wikipedia.org/wiki/Existential_fallacy "Existential fallacy"), and the [fallacy of the undistributed middle](https://en.wikipedia.org/wiki/Fallacy_of_the_undistributed_middle "Fallacy of the undistributed middle").[^90]

## In various fields

Rules of inference are relevant to many fields, especially the [formal sciences](https://en.wikipedia.org/wiki/Formal_science "Formal science"), such as [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics") and [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), where they are used to prove theorems.[^91] [Mathematical proofs](https://en.wikipedia.org/wiki/Mathematical_proofs "Mathematical proofs") often start with a set of axioms to describe the logical relationships between mathematical constructs. To establish theorems, mathematicians apply rules of inference to these axioms, aiming to demonstrate that the theorems are logical consequences.[^92] They distinguish various [types of proof](https://en.wikipedia.org/wiki/Mathematical_proof "Mathematical proof") based on the inferential strategy to arrive at a conclusion such as [direct proof](https://en.wikipedia.org/wiki/Direct_proof "Direct proof"), [proof by contradiction](https://en.wikipedia.org/wiki/Proof_by_contradiction "Proof by contradiction"), and [mathematical induction](https://en.wikipedia.org/wiki/Mathematical_induction "Mathematical induction").[^93] [Mathematical logic](https://en.wikipedia.org/wiki/Mathematical_logic "Mathematical logic"), a subfield of mathematics and logic, uses mathematical methods and frameworks to study rules of inference and other logical concepts.[^94]

Computer science also relies on deductive reasoning, employing rules of inference to establish theorems and validate [algorithms](https://en.wikipedia.org/wiki/Algorithms "Algorithms").[^95] [Logic programming](https://en.wikipedia.org/wiki/Logic_programming "Logic programming") frameworks, such as [Prolog](https://en.wikipedia.org/wiki/Prolog "Prolog"), allow developers to [represent knowledge](https://en.wikipedia.org/wiki/Knowledge_representation "Knowledge representation") and use [computation](https://en.wikipedia.org/wiki/Computation "Computation") to draw inferences and solve problems.[^96] These frameworks often include an [automated theorem prover](https://en.wikipedia.org/wiki/Automated_theorem_prover "Automated theorem prover"), a program that uses rules of inference to generate or verify proofs automatically.[^97] [Expert systems](https://en.wikipedia.org/wiki/Expert_system "Expert system") utilize [automated reasoning](https://en.wikipedia.org/wiki/Automated_reasoning "Automated reasoning") to simulate the [decision-making](https://en.wikipedia.org/wiki/Decision-making "Decision-making") processes of human [experts](https://en.wikipedia.org/wiki/Experts "Experts") in specific fields, such as [medical diagnosis](https://en.wikipedia.org/wiki/Medical_diagnosis "Medical diagnosis"), and assist in complex problem-solving tasks. They have a [knowledge base](https://en.wikipedia.org/wiki/Knowledge_base "Knowledge base") to represent the facts and rules of the field and use an [inference engine](https://en.wikipedia.org/wiki/Inference_engine "Inference engine") to extract relevant information and respond to user queries.[^98]

Rules of inference are central to the [philosophy of logic](https://en.wikipedia.org/wiki/Philosophy_of_logic "Philosophy of logic") regarding the definition of [logical consequence](https://en.wikipedia.org/wiki/Logical_consequence "Logical consequence"), which describes the [relation](https://en.wikipedia.org/wiki/Relation_\(philosophy\) "Relation (philosophy)") between the premises of a deductively valid argument and its conclusion. Different theories of this concept debate its nature and the conditions under which it exists. According to the deductive-theoretic conception, logical consequence is defined in terms of rules of inference: a conclusion follows logically from a set of premises if it can be deduced through a series of inferential steps. The [model-theoretic](https://en.wikipedia.org/wiki/Model_theory "Model theory") conception, by contrast, focuses on how the non-logical vocabulary of statements can be [interpreted](https://en.wikipedia.org/wiki/Interpretation_\(logic\) "Interpretation (logic)"). According to this view, logical consequence means that no counterexamples are possible: under no interpretation are the premises true and the conclusion false.[^99] A related topic in the [epistemology of logic](https://en.wikipedia.org/wiki/Epistemology_of_logic "Epistemology of logic") concerns the question of how to justify that *modus ponens* and other rules of inference are acceptable forms of correct reasoning.[^100]

[Cognitive psychologists](https://en.wikipedia.org/wiki/Cognitive_psychology "Cognitive psychology") study mental processes, including [logical reasoning](https://en.wikipedia.org/wiki/Logical_reasoning "Logical reasoning"). They are interested in how humans use rules of inference to draw conclusions, examining the factors that influence correctness and efficiency. They observe, for example, that people are better at using *modus ponens* than *modus tollens*, resulting in a higher rate of successful inferences. A related topic focuses on [biases](https://en.wikipedia.org/wiki/Cognitive_bias "Cognitive bias") that lead individuals to mistake formal fallacies for valid arguments. For instance, fallacies of the types affirming the consequent and denying the antecedent are often mistakenly accepted as valid. The assessment of arguments also depends on the concrete meaning of the propositions: individuals are more likely to accept a fallacy if its conclusion sounds plausible.[^101]

Rules of inference are also relevant to the field of [law](https://en.wikipedia.org/wiki/Law "Law") for establishing the validity of one's argument or undermining the opponent's case by exposing logical fallacies. However, legal reasoning is not limited to strict deductive inferences, incorporating aspects such as [legal norms](https://en.wikipedia.org/wiki/Legal_norms "Legal norms") and [evidentiary standards](https://en.wikipedia.org/wiki/Evidentiary_standard "Evidentiary standard") that go beyond pure formal logic.[^102]

[^1]: Non-deductive arguments, by contrast, support the conclusion without ensuring that it is true, such as and. Non-deductive reasoning plays a central role in the empirical sciences, whereas deductive reasoning following rules of inference is more characteristically employed in the.[^18]

[^2]: The symbol in this formula means, expressing.[^22]

[^3]: Universal instantiation infers a statement about a specific individual from a universal claim, as in the argument "Everyone must pay taxes. Therefore, Wesley must pay taxes." [^25]

[^4]: The expression (abbreviated as ) is sometimes placed at the end of proofs to indicate that the original hypothesis has been demonstrated.[^28]

[^5]: There are different strategies used to formulate proofs. For example, seeks to establish a conclusion by showing that its negation is contradictory.[^30]

[^6]: Logical operators or constants are expressions used to form and connect propositions, such as,, and.[^31]

[^7]: According to a narrow definition, rules of inference only encompass rules of implication but do not include rules of replacement.[^34]

[^8]: Logicians use the symbols or to express negation.[^35]

[^9]: Rules of replacement are sometimes expressed using a double semi-colon. For instance, the double negation rule can be written as.[^36]

[^10]: Additionally, formal systems may also define or.[^47]

[^11]: Formal systems can have limitations about what can and cannot be proven in them, such as regarding formal systems that encode.[^49]

[^12]: This example assumes that ${\displaystyle a}$ refers to an individual in the [domain of discourse](https://en.wikipedia.org/wiki/Domain_of_discourse "Domain of discourse").

[^13]: An important difference between first-order and second-order logic is that second-order logic is, meaning that it is not possible to provide a finite set of rules of inference with which every theorem can be deduced.[^69]

[^14]: This situation is also known as a.[^74]

[^15]: The is an influential way of presenting proofs in natural deduction systems.[^81]

[^16]: - [Hurley 2016](#CITEREFHurley2016), p. 303
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Carlson 2017](#CITEREFCarlson2017), p. 20
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 244–245, 447

[^17]: - [Shanker 2003](#CITEREFShanker2003), p. [442](https://books.google.com/books?id=jIzT7AT3ILIC&pg=PA442)
- [Cook 2009](#CITEREFCook2009), p. 152

[^18]: - [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Löwe 2002](#CITEREFLöwe2002), pp. 5–6
- [Agazzi 2016](#CITEREFAgazzi2016), p. [27](https://books.google.com/books?id=nd0eEAAAQBAJ&pg=PA27)
- [Nunes 2011](#CITEREFNunes2011), pp. 2066–2069

[^19]: - [Hurley 2016](#CITEREFHurley2016), pp. 54–55, 283–287
- [Arthur 2016](#CITEREFArthur2016), p. 165
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Carlson 2017](#CITEREFCarlson2017), p. 20
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 244–245
- [Baker & Hacker 2014](#CITEREFBakerHacker2014), pp. [88–90](https://books.google.com/books?id=vEFVAgAAQBAJ&pg=PA88)
- [Reynolds 1998](#CITEREFReynolds1998), p. [12](https://books.google.com/books?id=X_ToAwAAQBAJ&pg=PA12)

[^20]: [Schumann 2023](#CITEREFSchumann2023), pp. [301–302](https://books.google.com/books?id=sqEIEQAAQBAJ&pg=PA301)

[^21]: [Hurley 2016](#CITEREFHurley2016), p. 303

[^22]: [Magnus & Button 2021](#CITEREFMagnusButton2021), p. 32

[^23]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 137, 245–246
- [Magnus & Button 2021](#CITEREFMagnusButton2021), p. 109

[^24]: [Sørensen & Urzyczyn 2006](#CITEREFSørensenUrzyczyn2006), pp. [161–162](https://books.google.com/books?id=_mtnm-9KtbEC&pg=PA161)

[^25]: - [Hurley 2016](#CITEREFHurley2016), pp. 374–377
- [Shapiro & Kouri Kissel 2024](#CITEREFShapiroKouri_Kissel2024), § 3. Deduction

[^26]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 295–299
- [Cook 2009](#CITEREFCook2009), pp. 124, 251–252
- [Hurley 2016](#CITEREFHurley2016), pp. 374–375

[^27]: - [Cook 2009](#CITEREFCook2009), pp. 124, 230, 251–252
- [Magnus & Button 2021](#CITEREFMagnusButton2021), pp. 112–113
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 244–245

[^28]: [MW staff 2026](#CITEREFMW_staff2026)

[^29]: - [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Hintikka 2013](#CITEREFHintikka2013), p. [98](https://books.google.com/books?id=rUDsCAAAQBAJ&pg=PA98)

[^30]: [DeBonis 2025](#CITEREFDeBonis2025), pp. [32–33, 56](https://books.google.com/books?id=RYdBEQAAQBAJ&pg=PA32)

[^31]: [Hurley 2016](#CITEREFHurley2016), pp. 238–239

[^32]: - [Baker & Hacker 2014](#CITEREFBakerHacker2014), pp. [88–90](https://books.google.com/books?id=vEFVAgAAQBAJ&pg=PA88)
- [Tourlakis 2011](#CITEREFTourlakis2011), p. [40](https://books.google.com/books?id=8jAwgCTgnycC&pg=PA40)
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [McKeon 2010](#CITEREFMcKeon2010), pp. [128–129](https://books.google.com/books?id=76SH_DI3yyoC&pg=PA128)

[^33]: - [Burris 2024](#CITEREFBurris2024), Lead section
- [O'Regan 2017](#CITEREFO'Regan2017), pp. 95–96, 103

[^34]: [Arthur 2016](#CITEREFArthur2016), pp. 165–166

[^35]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), p. 446
- [Magnus & Button 2021](#CITEREFMagnusButton2021), p. 32

[^36]: [Hurley 2016](#CITEREFHurley2016), pp. 323–252

[^37]: - [Arthur 2016](#CITEREFArthur2016), pp. 165–166
- [Hurley 2016](#CITEREFHurley2016), pp. 302–303, 323–252
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 257–258
- [Hurley & Watson 2018](#CITEREFHurleyWatson2018), pp. 403–404, 426–428

[^38]: - [Walton 2013](#CITEREFWalton2013), pp. 5–7, 265
- [Roy & Chakraborty 2013](#CITEREFRoyChakraborty2013), p. [92](https://books.google.com/books?id=Ujw8BAAAQBAJ&pg=PA92)

[^39]: [Epstein & King 2002](#CITEREFEpsteinKing2002), pp. 1–2, 38

[^40]: - [Hintikka & Spade 2020](#CITEREFHintikkaSpade2020), § Aristotle, § Medieval Logic, § Boole and De Morgan, § Gottlob Frege
- [O'Regan 2017](#CITEREFO'Regan2017), pp. 95–96, 103
- [Gensler 2012](#CITEREFGensler2012), p. [362](https://books.google.com/books?id=jpteBwAAQBAJ&pg=PA362)
- [Burris 2024](#CITEREFBurris2024), Lead section

[^41]: - [Hurley 2016](#CITEREFHurley2016), pp. 303, 429–430
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Carlson 2017](#CITEREFCarlson2017), p. 20
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 244–245, 447

[^42]: - [Bonevac 1999](#CITEREFBonevac1999), pp. 679–681
- [Lowe 2005](#CITEREFLowe2005), pp. 699–701
- [Dowden 2020](#CITEREFDowden2020), p. 24
- [Copi, Cohen & Rodych 2019](#CITEREFCopiCohenRodych2019), p. [4](https://books.google.com/books?id=38bADwAAQBAJ&pg=PA4)

[^43]: - [Hintikka 2019](#CITEREFHintikka2019), § Nature and Varieties of Logic
- [Haack 1978](#CITEREFHaack1978), pp. 1–10
- [Schlesinger, Keren-Portnoy & Parush 2001](#CITEREFSchlesingerKeren-PortnoyParush2001), p. 220

[^44]: - [Hintikka 2019](#CITEREFHintikka2019), Lead section, § Nature and Varieties of Logic
- [Bonevac 1999](#CITEREFBonevac1999), p. 679

[^45]: - [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14
- [Bonevac 1999](#CITEREFBonevac1999), pp. 679–681
- [Cannon 2002](#CITEREFCannon2002), pp. [14–15](https://books.google.com/books?id=79qb93CQE2AC&pg=PA14)

[^46]: - [Tully 2005](#CITEREFTully2005), pp. 532–533
- [Hodges 2005](#CITEREFHodges2005), pp. 533–536
- [Walton 1996](#CITEREFWalton1996)
- [Johnson 1999](#CITEREFJohnson1999), pp. 265–268

[^47]: [Hodel 2013](#CITEREFHodel2013), p. [7](https://books.google.com/books?id=SxRYdzWio84C&pg=PA7)

[^48]: - [Cook 2009](#CITEREFCook2009), p. 124
- [Jacquette 2006](#CITEREFJacquette2006), pp. 2–4
- [Hodel 2013](#CITEREFHodel2013), p. [7](https://books.google.com/books?id=SxRYdzWio84C&pg=PA7)

[^49]: [Moore 2022](#CITEREFMoore2022), pp. [1–9](https://books.google.com/books?id=ZwuYEAAAQBAJ&pg=PA1)

[^50]: - [Cook 2009](#CITEREFCook2009), pp. 9–10
- [Fitting & Mendelsohn 2012](#CITEREFFittingMendelsohn2012), pp. [68–69](https://books.google.com/books?id=5IxqCQAAQBAJ&pg=PA68)
- [Boyer & Moore 2014](#CITEREFBoyerMoore2014), pp. [144–146](https://books.google.com/books?id=eMHSBQAAQBAJ&pg=PA144)

[^51]: [Cook 2009](#CITEREFCook2009), p. 287

[^52]: - [Asprino 2020](#CITEREFAsprino2020), p. [4](https://books.google.com/books?id=H6EGEAAAQBAJ&pg=PA4)
- [Hodges 2005](#CITEREFHodges2005), pp. 533–536
- [Bonevac 1999](#CITEREFBonevac1999), pp. 679–681

[^53]: - [Copi, Cohen & Rodych 2019](#CITEREFCopiCohenRodych2019), p. [30](https://books.google.com/books?id=38bADwAAQBAJ&pg=PA30)
- [Hurley 2016](#CITEREFHurley2016), pp. 42–43, 434–435

[^54]: - [Gossett 2009](#CITEREFGossett2009), pp. [50–51](https://books.google.com/books?id=NuFeW8N2hlkC&pg=PA50)
- [Carlson 2017](#CITEREFCarlson2017), p. 20
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), p. 16
- [Makridis 2022](#CITEREFMakridis2022), p. [478](https://books.google.com/books?id=DoBgEAAAQBAJ&pg=PA478)

[^55]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 244–245, 447
- [Hurley 2016](#CITEREFHurley2016), pp. 267–270

[^56]: - [Klement](#CITEREFKlement), Lead section, § 1. Introduction, § 3. The Language of Propositional Logic
- [Sider 2010](#CITEREFSider2010), pp. [25–30](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA25)

[^57]: - [Hurley 2016](#CITEREFHurley2016), pp. 303, 315
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), p. 247
- [Klement](#CITEREFKlement), § Deduction: Rules of Inference and Replacement

[^58]: - [Hurley 2016](#CITEREFHurley2016), pp. 303, 315
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), p. 247

[^59]: - [O'Regan 2017](#CITEREFO'Regan2017), pp. 101–103
- [Zalta 2024](#CITEREFZalta2024), Lead section

[^60]: - [Shapiro & Kouri Kissel 2024](#CITEREFShapiroKouri_Kissel2024), Lead section, § 2. Language
- [Sider 2010](#CITEREFSider2010), pp. [90–95](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA90)
- [Cook 2009](#CITEREFCook2009), pp. 119–120

[^61]: - [Garson 2024](#CITEREFGarson2024), Lead section, § 2. Modal Logics
- [Sider 2010](#CITEREFSider2010), pp. [133–136, 227–228](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA133)

[^62]: [Garson 2024](#CITEREFGarson2024), § 3. Deontic Logics

[^63]: - [Garson 2024](#CITEREFGarson2024), § 1. What is Modal Logic?, § 4. Temporal Logics
- [Sider 2010](#CITEREFSider2010), pp. [183–187](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA183)

[^64]: [O'Regan 2017](#CITEREFO'Regan2017), pp. 90–91, 103

[^65]: [Barrio & Pailos 2021](#CITEREFBarrioPailos2021), pp. 261–262

[^66]: - [Smith 2022](#CITEREFSmith2022), Lead section, § 3. The Subject of Logic: "Syllogisms"
- [Groarke](#CITEREFGroarke), Lead section, § 3. From Words into Propositions, § 4. Kinds of Propositions, § 9. The Syllogism

[^67]: - [Sharma 2000](#CITEREFSharma2000), pp. 199–200
- [Dasti](#CITEREFDasti), § 1.b.ii. The Structure of Inference
- [Chatterjee 2022](#CITEREFChatterjee2022), p. [129](https://books.google.com/books?id=V1qaEAAAQBAJ&pg=PA129)

[^68]: [Väänänen 2024](#CITEREFVäänänen2024), Lead section, § 1. Introduction

[^69]: - [Väänänen 2024](#CITEREFVäänänen2024), § 1. Introduction
- [Grandy 1979](#CITEREFGrandy1979), p. [122](https://books.google.com/books?id=ItgJhsGE-RAC&pg=PA122)
- [Linnebo 2014](#CITEREFLinnebo2014), p. [123](https://books.google.com/books?id=EKZOBAAAQBAJ&pg=PA123)

[^70]: [Pollard 2015](#CITEREFPollard2015), p. [98](https://books.google.com/books?id=6cY-CgAAQBAJ&pg=PA98)

[^71]: - [Moschovakis 2024](#CITEREFMoschovakis2024), Lead section, § 1. Rejection of *Tertium Non Datur*
- [Sider 2010](#CITEREFSider2010), pp. [86–89](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA86)
- [Kleene 2000](#CITEREFKleene2000), p. [81](https://books.google.com/books?id=q-LG8Ep7WFcC&pg=PA81)

[^72]: [Montiel et al. 2007](#CITEREFMontielCastilloMelinSepulveda2007), p. [137](https://books.google.com/books?id=fFGs1RY8zNwC&pg=PA137)

[^73]: - [Shapiro & Kouri Kissel 2024](#CITEREFShapiroKouri_Kissel2024), § 3. Deduction
- [Sider 2010](#CITEREFSider2010), pp. [80–82](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA80)
- [Priest, Tanaka & Weber 2025](#CITEREFPriestTanakaWeber2025), Lead section
- [Pérez-Gaspar, Borja-Macías & Barcenas 2021](#CITEREFPérez-GasparBorja-MacíasBarcenas2021), pp. 435–436

[^74]: [Carnielli & Coniglio 2016](#CITEREFCarnielliConiglio2016), p. [ix](https://books.google.com/books?id=VApkDAAAQBAJ&pg=PR9)

[^75]: - [Weber](#CITEREFWeber), Lead section, § 2. Logical Background
- [Sider 2010](#CITEREFSider2010), pp. [80–82](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA80)
- [Priest, Tanaka & Weber 2025](#CITEREFPriestTanakaWeber2025), Lead section

[^76]: - [Sider 2010](#CITEREFSider2010), pp. [73–74, 77–79](https://books.google.com/books?id=-KkPEAAAQBAJ&pg=PA73)
- [Gottwald 2022](#CITEREFGottwald2022), Lead section, § 3.4 Three-valued Systems
- [Salatiel 2022](#CITEREFSalatiel2022), pp. 79–86

[^77]: - [Egré & Rott 2021](#CITEREFEgréRott2021), § 2. Three-Valued Conditionals
- [Gottwald 2022](#CITEREFGottwald2022), Lead section, § 2. Proof Theory

[^78]: - [Demey, Kooi & Sack 2023](#CITEREFDemeyKooiSack2023), Lead section, § 1. Combining Logic and Probability Theory, § 2.1 Probabilistic Semantics
- [Boričić 2016](#CITEREFBoričić2016), pp. 77–78

[^79]: - [Nederpelt & Geuvers 2014](#CITEREFNederpeltGeuvers2014), pp. [159–162](https://books.google.com/books?id=orsrBQAAQBAJ&pg=PA159)
- [Sørensen & Urzyczyn 2006](#CITEREFSørensenUrzyczyn2006), pp. [161–162](https://books.google.com/books?id=_mtnm-9KtbEC&pg=PA161)

[^80]: - [Pelletier & Hazen 2024](#CITEREFPelletierHazen2024), Lead section, § 2.2 Modern Versions of Jaśkowski's Method, § 5.1 Normalization of Intuitionistic Logic
- [Nederpelt & Geuvers 2014](#CITEREFNederpeltGeuvers2014), pp. [159–162](https://books.google.com/books?id=orsrBQAAQBAJ&pg=PA159)
- [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), p. 244

[^81]: [Akiba 2024](#CITEREFAkiba2024), p. [7](https://books.google.com/books?id=ftksEQAAQBAJ&pg=PA7)

[^82]: - [Bacon 2023](#CITEREFBacon2023), pp. [423–424](https://books.google.com/books?id=qa3WEAAAQBAJ&pg=PA423)
- [Nederpelt & Geuvers 2014](#CITEREFNederpeltGeuvers2014), pp. [159–162](https://books.google.com/books?id=orsrBQAAQBAJ&pg=PA159)
- [Sørensen & Urzyczyn 2006](#CITEREFSørensenUrzyczyn2006), pp. [161–162](https://books.google.com/books?id=_mtnm-9KtbEC&pg=PA161)

[^83]: - [Reynolds 1998](#CITEREFReynolds1998), p. [12](https://books.google.com/books?id=X_ToAwAAQBAJ&pg=PA12)
- [Cook 2009](#CITEREFCook2009), p. 26

[^84]: [Smullyan 2014](#CITEREFSmullyan2014), pp. [102–103](https://books.google.com/books?id=n6S-AwAAQBAJ&pg=PA102)

[^85]: - [Metcalfe, Paoli & Tsinakis 2023](#CITEREFMetcalfePaoliTsinakis2023), pp. [36–37](https://books.google.com/books?id=CkPsEAAAQBAJ&pg=PA36)
- [Nederpelt & Geuvers 2014](#CITEREFNederpeltGeuvers2014), pp. [159–162](https://books.google.com/books?id=orsrBQAAQBAJ&pg=PA159)
- [Sørensen & Urzyczyn 2006](#CITEREFSørensenUrzyczyn2006), pp. [161–162](https://books.google.com/books?id=_mtnm-9KtbEC&pg=PA161)

[^86]: - [Rathjen & Sieg 2024](#CITEREFRathjenSieg2024), § 2.2 Sequent Calculi
- [Sørensen & Urzyczyn 2006](#CITEREFSørensenUrzyczyn2006), pp. [161–165](https://books.google.com/books?id=_mtnm-9KtbEC&pg=PA161)

[^87]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 224, 439
- [Hurley & Watson 2018](#CITEREFHurleyWatson2018), pp. 385–386, 720

[^88]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 46–47, 227
- [Cook 2009](#CITEREFCook2009), p. 123
- [Hurley & Watson 2018](#CITEREFHurleyWatson2018), pp. 125–126, 723

[^89]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 46, 228, 442
- [Hurley & Watson 2018](#CITEREFHurleyWatson2018), pp. 385–386, 722

[^90]: - [Copi, Cohen & Flage 2016](#CITEREFCopiCohenFlage2016), pp. 443, 449
- [Hurley & Watson 2018](#CITEREFHurleyWatson2018), pp. 723, 728
- [Cohen 2009](#CITEREFCohen2009), p. [254](https://books.google.com/books?id=4aGIsKmkODgC&pg=PA254)

[^91]: - [Fetzer 1996](#CITEREFFetzer1996), pp. [241–243](https://books.google.com/books?id=JbNI3b-j0mkC&pg=PA241)
- [Dent 2024](#CITEREFDent2024), p. [36](https://books.google.com/books?id=NbA0EQAAQBAJ&pg=PA36)

[^92]: - [Horsten 2023](#CITEREFHorsten2023), Lead section, § 5.4 Mathematical Proof
- [Polkinghorne 2011](#CITEREFPolkinghorne2011), p. [65](https://books.google.com/books?id=AJV0P1pPBNoC&pg=PA65)

[^93]: [DeBonis 2025](#CITEREFDeBonis2025), pp. [17–18](https://books.google.com/books?id=RYdBEQAAQBAJ&pg=PA17)

[^94]: - [Cook 2009](#CITEREFCook2009), pp. 174, 185
- [Porta et al. 2011](#CITEREFPortaMailletMasMartinez2011), p. [237](https://books.google.com/books?id=NDMID6mWcZcC&pg=PA237)

[^95]: - [Butterfield & Ngondi 2016](#CITEREFButterfieldNgondi2016), § Computer Science
- [Cook 2009](#CITEREFCook2009), p. 174
- [Dent 2024](#CITEREFDent2024), p. [36](https://books.google.com/books?id=NbA0EQAAQBAJ&pg=PA36)

[^96]: - [Butterfield & Ngondi 2016](#CITEREFButterfieldNgondi2016), § Logic Programming Languages, § Prolog
- [Williamson & Russo 2010](#CITEREFWilliamsonRusso2010), p. [45](https://books.google.com/books?id=SmYu9-1HGtYC&pg=PA45)

[^97]: - [Butterfield & Ngondi 2016](#CITEREFButterfieldNgondi2016), § Theorem Proving, § Mechanical Verifier
- [Lavalle et al. 2018](#CITEREFLavalleMontesJiménezVillaseñor2018), pp. 119–120

[^98]: - [Butterfield & Ngondi 2016](#CITEREFButterfieldNgondi2016), § Expert System, § Knowledge Base, § Inference Engine
- [Fetzer 1996](#CITEREFFetzer1996), pp. [241–243](https://books.google.com/books?id=JbNI3b-j0mkC&pg=PA241)

[^99]: - [McKeon](#CITEREFMcKeon), Lead section, § 1. Introduction, § 2b. Logical and Non-Logical Terminology
- [McKeon 2010](#CITEREFMcKeon2010), pp. [24–25, 126–128](https://books.google.com/books?id=76SH_DI3yyoC&pg=PA24)
- [Hintikka & Sandu 2006](#CITEREFHintikkaSandu2006), pp. 13–14, 17–18
- [Beall, Restall & Sagi 2024](#CITEREFBeallRestallSagi2024), § 3. Mathematical Tools: Models and Proofs