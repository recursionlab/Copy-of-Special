---
title: "Order of operations"
source: "https://en.wikipedia.org/wiki/Order_of_operations"
author:
  - "[[Wikipedia]]"
published: 2003-04-19
created: 2026-05-19
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics") and [computer programming](https://en.wikipedia.org/wiki/Computer_programming "Computer programming"), the **order of operations** is a collection of conventions about which [arithmetic operations](https://en.wikipedia.org/wiki/Arithmetic_operations "Arithmetic operations") to perform first in order to evaluate a given [mathematical expression](https://en.wikipedia.org/wiki/Mathematical_expression "Mathematical expression").

These conventions are formalized with a ranking of the operations. The rank of an operation is called its **precedence**, and an operation with a *higher* precedence is performed before operations with *lower* precedence. [Calculators](https://en.wikipedia.org/wiki/Calculator "Calculator") generally perform operations with the same precedence from left to right,[^4] but some [programming languages](https://en.wikipedia.org/wiki/Programming_language "Programming language") and calculators adopt different conventions.

For example, multiplication is granted a higher precedence than addition, and it has been this way since the introduction of modern [algebraic notation](https://en.wikipedia.org/wiki/Mathematical_notation "Mathematical notation").[^5] [^6] Thus, in the expression 1 + 2 × 3, the multiplication is performed before addition, and the expression has the value 1 + (2 × 3) = 7, and not (1 + 2) × 3 = 9. When [exponents](https://en.wikipedia.org/wiki/Exponentiation "Exponentiation") were introduced in the 16th and 17th centuries, they were given precedence over both addition and multiplication and placed as a superscript to the right of their base.[^5] Thus 3 + 5 <sup>2</sup> = 28 and 3 × 5 <sup>2</sup> = 75.

These conventions exist to avoid notational [ambiguity](https://en.wikipedia.org/wiki/Ambiguity "Ambiguity") while allowing notation to remain brief.[^7] Where it is desired to override the precedence conventions, or even simply to emphasize them, [parentheses](https://en.wikipedia.org/wiki/Bracket#Parentheses "Bracket") ( ) can be used. For example, (2 + 3) × 4 = 20 forces addition to precede multiplication, while (3 + 5) <sup>2</sup> = 64 forces addition to precede [exponentiation](https://en.wikipedia.org/wiki/Exponentiation "Exponentiation"). If multiple pairs of parentheses are required in a mathematical expression (such as in the case of nested parentheses), the parentheses may be replaced by other types of [brackets](https://en.wikipedia.org/wiki/Bracket "Bracket") to avoid confusion, as in \[2 × (3 + 4)\] − 5 = 9.

These conventions are meaningful only when the usual notation (called [infix notation](https://en.wikipedia.org/wiki/Infix_notation "Infix notation")) is used. When [functional](https://en.wikipedia.org/wiki/Functional_notation "Functional notation") or [Polish notation](https://en.wikipedia.org/wiki/Polish_notation "Polish notation") are used for all operations, the order of operations results from the notation itself.

## Conventional order

The order of operations, that is, the order in which the operations in an expression are usually performed, results from a convention adopted throughout mathematics, science, technology and many computer [programming languages](https://en.wikipedia.org/wiki/Programming_language "Programming language"). It is summarized as:[^5] [^8]

1. [Parentheses](https://en.wikipedia.org/wiki/Bracket_\(mathematics\) "Bracket (mathematics)")
2. [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation "Exponentiation")
3. [Multiplication](https://en.wikipedia.org/wiki/Multiplication "Multiplication") and [division](https://en.wikipedia.org/wiki/Division_\(mathematics\) "Division (mathematics)")
4. [Addition](https://en.wikipedia.org/wiki/Addition "Addition") and [subtraction](https://en.wikipedia.org/wiki/Subtraction "Subtraction")

This means that to evaluate an expression, one first evaluates any sub-expression inside parentheses, working inside to outside if there is more than one set. Whether inside parentheses or not, the operation that is higher in the above list should be applied first. Operations of the same precedence are conventionally evaluated from left to right.

If each division is replaced with multiplication by the [reciprocal](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse") (multiplicative inverse) then the [associative](https://en.wikipedia.org/wiki/Associative_property "Associative property") and [commutative](https://en.wikipedia.org/wiki/Commutative_property "Commutative property") laws of multiplication allow the factors in each [term](https://en.wikipedia.org/wiki/Addend "Addend") to be multiplied together in any order. Sometimes multiplication and division are given equal precedence, or sometimes multiplication is given higher precedence than division; see [§ Mixed division and multiplication](#Mixed_division_and_multiplication) below. If each subtraction is replaced with addition of the [opposite](https://en.wikipedia.org/wiki/Additive_inverse "Additive inverse") (additive inverse), then the associative and commutative laws of addition allow terms to be added in any order.

The [radical symbol](https://en.wikipedia.org/wiki/Radical_symbol "Radical symbol") ⁠ ${\displaystyle \surd }$ ⁠ which signifies a [square root](https://en.wikipedia.org/wiki/Square_root "Square root") is traditionally extended by a bar (the [vinculum](https://en.wikipedia.org/wiki/Vinculum_\(symbol\) "Vinculum (symbol)")) over the radicand; this avoids the need for parentheses around the radicand. Other functions use parentheses around the input to avoid ambiguity.[^9] [^10] [^1] The parentheses can be omitted if the input is a single numerical variable or constant,[^5] as in the case of sin *x* = sin(*x*) and sin *π* = sin(*π*).[^1] Traditionally this convention extends to [monomials](https://en.wikipedia.org/wiki/Monomial "Monomial"); thus, sin 3 *x* = sin(3 *x*) and even sin ⁠12⁠ *xy* = sin(⁠12⁠ *xy*), but sin *x* + *y* = sin(*x*) + *y*, because *x* + *y* is not a monomial. However, this convention is not universally understood, and some authors prefer explicit parentheses.[^2] Some calculators and programming languages require parentheses around function inputs, while others do not.

Parentheses and alternate symbols of grouping can be used to override the usual order of operations or to make the intended order explicit. Grouped symbols can be treated as a single expression.[^5]

### Examples

Multiplication before addition:

${\displaystyle 1+2\times 3=1+6=7.}$

Parenthetical subexpressions are evaluated first:

${\displaystyle (1+2)\times 3=3\times 3=9.}$

Exponentiation before multiplication, multiplication before subtraction:

${\displaystyle 1-2\times 3^{4}=1-2\times 81=1-162=-161.}$

When an expression is written as a superscript, the superscript is considered to be grouped by its position above its base:

${\displaystyle 1+2^{3+4}=1+2^{7}=1+128=129.}$

The operand of a root symbol is determined by the overbar:

${\displaystyle {\sqrt {1+3}}+5={\sqrt {4}}+5=2+5=7.}$

A horizontal fractional line forms two grouped subexpressions, one above divided by another below:

${\displaystyle {\frac {1+2}{3+4}}+5={\frac {3}{7}}+5.}$

Parentheses can be nested, and should be evaluated from the inside outward. For legibility, outer parentheses can be made larger than inner parentheses. Alternately, other grouping symbols, such as curly braces { } or square brackets \[ \], are sometimes used along with parentheses ( ). For example:

${\displaystyle {\bigl [}(1+2)\div (3+4){\bigr ]}+5=(3\div 7)+5}$

## Special cases

### Unary minus sign

There are differing conventions concerning the [unary operation](https://en.wikipedia.org/wiki/Unary_operation "Unary operation") '−' (usually pronounced "minus"). In written or printed mathematics, the expression −3 <sup>2</sup> is interpreted to mean −(3 <sup>2</sup>) = −9.[^5] [^11]

In some applications and programming languages, notably [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel "Microsoft Excel") (and other spreadsheet applications), unary operations have a higher priority than binary operations, that is, the unary minus has higher precedence than exponentiation, so in those languages −3 <sup>2</sup> will be interpreted as (−3) <sup>2</sup> = 9.[^12] [^13] This does not apply to the binary minus operation '−'; for example in Microsoft Excel the formulas `=-2^2`, `=(-2)^2` and `=0+-2^2` return 4, but the formulas `=0-2^2` and `=-(2^2)` return −4.

### Mixed division and multiplication

There is no universal convention for interpreting an expression containing both division denoted by '÷' and multiplication denoted by '×'. Proposed conventions include assigning the operations equal precedence and evaluating them from left to right, or equivalently treating division as multiplication by the reciprocal and then evaluating in any order;[^14] evaluating all multiplications first followed by divisions from left to right; or eschewing such expressions and instead always disambiguating them by explicit parentheses.[^15]

Beyond primary education, the symbol '÷' for division is seldom used, but is replaced by the use of [algebraic fractions](https://en.wikipedia.org/wiki/Algebraic_fraction "Algebraic fraction").[^16] These are most explicitly and unambiguously written "vertically" with the numerator stacked above the denominator separated by a fraction bar. But they can also be written "horizontally" with the numerator and denominator separated by the [slash](https://en.wikipedia.org/wiki/Division_slash "Division slash") symbol '/'.[^17] That is, expressions such as *a* ÷ *b* are avoided in favor of ⁠ *a* *b* ⁠ or *a*  /  *b*.

Multiplication denoted by juxtaposition (also known as [implied multiplication](https://en.wikipedia.org/wiki/Implied_multiplication "Implied multiplication")) creates a visual unit and is often given higher precedence than most other operations. In academic literature, when inline fractions are combined with implied multiplication without explicit parentheses, the multiplication is conventionally interpreted as having higher precedence than division, so that e.g. 1 / 2 *n* is interpreted to mean 1 / (2 ·  *n*) rather than (1 / 2) ·  *n*.[^5] [^14] [^18] [^19] For instance, the manuscript submission instructions for the *[Physical Review](https://en.wikipedia.org/wiki/Physical_Review "Physical Review")* journals directly state that multiplication has precedence over division,[^20] and this is also the convention observed in physics textbooks such as the *[Course of Theoretical Physics](https://en.wikipedia.org/wiki/Course_of_Theoretical_Physics "Course of Theoretical Physics")* by [Landau](https://en.wikipedia.org/wiki/Lev_Landau "Lev Landau") and [Lifshitz](https://en.wikipedia.org/wiki/Evgeny_Lifshitz "Evgeny Lifshitz") [^3] and mathematics textbooks such as *[Concrete Mathematics](https://en.wikipedia.org/wiki/Concrete_Mathematics "Concrete Mathematics")* by [Graham](https://en.wikipedia.org/wiki/Ronald_Graham "Ronald Graham"), [Knuth](https://en.wikipedia.org/wiki/Donald_Knuth "Donald Knuth"), and [Patashnik](https://en.wikipedia.org/wiki/Oren_Patashnik "Oren Patashnik").[^21] However, some authors recommend against expressions such as *a*  /  *bc*, preferring the explicit use of parenthesis *a*  / (*bc*).[^6]

More complicated cases are more ambiguous. For instance, the notation 1 / 2 *π* (*a*  +  *b*) could plausibly mean either 1 / \[2 *π*  · (*a*  +  *b*)\] or \[1 / (2 *π*)\] · (*a*  +  *b*).[^22] Sometimes interpretation depends on context. The *Physical Review* submission instructions recommend against expressions of the form *a*  /  *b*  /  *c*; more explicit expressions (*a*  /  *b*) /  *c* or *a*  / (*b*  /  *c*) are unambiguous.[^20]

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Precedence62xplus.jpg/250px-Precedence62xplus.jpg)

6÷2(1+2) is interpreted as 6÷(2×(1+2)) by a fx-82MS (upper), and (6÷2)×(1+2) by a TI-83 Plus calculator (lower), respectively.

This ambiguity has been the subject of [Internet memes](https://en.wikipedia.org/wiki/Internet_meme "Internet meme") such as "8 ÷ 2(2 + 2)", for which there are two conflicting interpretations: 8 ÷ \[2 · (2 + 2)\] = 1 and (8 ÷ 2) · (2 + 2) = 16.[^19] [^23] Mathematics education researcher Hung-Hsi Wu points out that "one never gets a computation of this type in real life", and calls such contrived examples "a kind of Gotcha! parlor game designed to trap an unsuspecting person by phrasing it in terms of a set of unreasonably convoluted rules".[^16]

### Serial exponentiation

If [exponentiation](https://en.wikipedia.org/wiki/Exponentiation "Exponentiation") is indicated by stacked symbols using superscript notation, the usual rule is to work from the top down:[^5] [^10]

*a* <sup><i>b</i> <sup><i>c</i></sup></sup> = *a* <sup>(<i>b</i> <sup><i>c</i></sup>)</sup>,

which typically is not equal to (*a* <sup><i>b</i></sup>) <sup><i>c</i></sup>. This convention is useful because there is [a property of exponentiation](https://en.wikipedia.org/wiki/Exponentiation#Identities_and_properties "Exponentiation") that (*a* <sup><i>b</i></sup>) <sup><i>c</i></sup> = *a* <sup><i>bc</i></sup>, so it's unnecessary to use serial exponentiation for this.

However, when exponentiation is represented by an explicit symbol such as a [caret](https://en.wikipedia.org/wiki/Caret "Caret") (^) or [arrow](https://en.wikipedia.org/wiki/Arrow_\(symbol\) "Arrow (symbol)") (↑), there is no common standard. For example, [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel "Microsoft Excel") and computation programming language [MATLAB](https://en.wikipedia.org/wiki/MATLAB "MATLAB") evaluate `*a*^*b*^*c*` as (*a* <sup><i>b</i></sup>) <sup><i>c</i></sup>, but [Google Search](https://en.wikipedia.org/wiki/Google_Search "Google Search") and [Wolfram Alpha](https://en.wikipedia.org/wiki/Wolfram_Alpha "Wolfram Alpha") as *a* <sup>(<i>b</i> <sup><i>c</i></sup>)</sup>. Thus `4^3^2` is evaluated to 4,096 in the first case and to 262,144 in the second case.

## Mnemonics

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Order_of_operations_PEMDAS_and_BODMAS_acronyms.svg/250px-Order_of_operations_PEMDAS_and_BODMAS_acronyms.svg.png)

Meaning of the PEMDAS and BODMAS acronyms

[Mnemonic](https://en.wikipedia.org/wiki/Mnemonic "Mnemonic") [acronyms](https://en.wikipedia.org/wiki/Acronym "Acronym") are often taught in primary schools to help students remember the order of operations.[^24] [^25] The acronym ***PEMDAS***, which stands for **P** arentheses, **E** xponents, **M** ultiplication/ **D** ivision, **A** ddition/ **S** ubtraction,[^26] is common in the [United States](https://en.wikipedia.org/wiki/Mathematics_education_in_the_United_States "Mathematics education in the United States") [^27] and France.[^28] Sometimes the letters are expanded into words of a mnemonic sentence such as "Please Excuse My Dear Aunt Sally".[^29] The United Kingdom and other [Commonwealth](https://en.wikipedia.org/wiki/Commonwealth_of_Nations "Commonwealth of Nations") countries may use ***BODMAS*** (or sometimes ***BOMDAS***), standing for **B** rackets, **O** f, **D** ivision/ **M** ultiplication, **A** ddition/ **S** ubtraction, with "of" meaning fraction multiplication.[^30] [^31] Sometimes the **O** is instead expanded as **O** rder, meaning exponent or root,[^31] [^32] or replaced by **I** for **I** ndices in the alternative mnemonic ***BIDMAS***.[^31] [^33] In Canada and New Zealand ***BEDMAS*** is common.[^34]

These mnemonics may be misleading when written this way.[^29] For example, misinterpreting any of the above rules to mean "addition first, subtraction afterward" would incorrectly evaluate the expression [^29] ${\displaystyle a-b+c}$ as ${\displaystyle a-(b+c)}$, while the correct evaluation is ${\displaystyle (a-b)+c}$. These values are different when ${\displaystyle c\neq 0}$.

In Germany, the convention is simply taught as *[Punktrechnung vor Strichrechnung](https://de.wikipedia.org/wiki/Punktrechnung_vor_Strichrechnung "de:Punktrechnung vor Strichrechnung")*, "dot operations before line operations" referring to the graphical shapes of the symbols · (multiplication), ∶ (division), + (addition), and − (subtraction). This avoids the potential for the above misunderstanding.

Mnemonic acronyms have been criticized for not developing a conceptual understanding of the order of operations, and not addressing student questions about its purpose or flexibility.[^35] [^36] Students learning the order of operations via mnemonic acronyms routinely make mistakes,[^37] as do some pre-service teachers.[^38] Even when students correctly learn the acronym, a disproportionate focus on memorization of trivia crowds out substantive mathematical content.[^16] The acronym's procedural application does not match experts' intuitive understanding of mathematical notation: mathematical notation indicates groupings in ways other than parentheses or brackets and a mathematical expression is a [tree-like hierarchy](https://en.wikipedia.org/wiki/Binary_expression_tree "Binary expression tree") rather than a linearly "ordered" structure; furthermore, there is no single order by which mathematical expressions must be simplified or evaluated and no universal canonical simplification for any particular expression, and experts fluently apply valid transformations and substitutions in whatever order is convenient, so learning a rigid procedure can lead students to a misleading and limiting understanding of mathematical notation.[^39]

## Calculators

Different calculators follow different orders of operations.[^5] Many simple calculators without a [stack](https://en.wikipedia.org/wiki/Stack_machine "Stack machine") implement [chain input](https://en.wikipedia.org/wiki/Chain_input "Chain input"), working in button-press order without any priority given to different operations, give a different result from that given by more sophisticated calculators. For example, on a simple calculator, typing `1 + 2 × 3 =` yields 9, while a more sophisticated calculator will use a more standard priority, so typing `1 + 2 × 3 =` yields 7.

Calculators may associate exponents to the left or to the right. For example, the expression `*a*^*b*^*c*` is interpreted as *a* <sup>(<i>b</i> <sup><i>c</i></sup>)</sup> on the [TI-92](https://en.wikipedia.org/wiki/TI-92 "TI-92") and the [TI-30XS MultiView](https://en.wikipedia.org/wiki/TI-30XS_MultiView "TI-30XS MultiView") in "Mathprint mode", whereas it is interpreted as (*a* <sup><i>b</i></sup>) <sup><i>c</i></sup> on the [TI-30XII](https://en.wikipedia.org/wiki/TI-30XII "TI-30XII") and the TI-30XS MultiView in "Classic mode".

An expression like `1/2*x*` is interpreted as 1/(2 *x*) by [TI-82](https://en.wikipedia.org/wiki/TI-82 "TI-82"),[^6] as well as many modern [Casio](https://en.wikipedia.org/wiki/Casio "Casio") calculators [^40] (configurable on some like the [fx-9750GIII](https://en.wikipedia.org/wiki/Casio_fx-9750GIII "Casio fx-9750GIII")), but as (1/2) *x* by [TI-83](https://en.wikipedia.org/wiki/TI-83 "TI-83") and every other TI calculator released since 1996,[^41] [^6] as well as by all [Hewlett-Packard](https://en.wikipedia.org/wiki/Hewlett-Packard "Hewlett-Packard") calculators with algebraic notation. While the first interpretation may be expected by some users due to the nature of [implied multiplication](https://en.wikipedia.org/wiki/Implied_multiplication "Implied multiplication"),[^42] the latter is more in line with the rule that multiplication and division are of equal precedence.[^6]

When the user is unsure how a calculator will interpret an expression, parentheses can be used to remove the ambiguity.[^6]

Order of operations arose due to the adaptation of [infix notation](https://en.wikipedia.org/wiki/Infix_notation "Infix notation") in [standard mathematical notation](https://en.wikipedia.org/wiki/Standard_mathematical_notation "Standard mathematical notation"), which can be notationally ambiguous without such conventions, as opposed to [postfix notation](https://en.wikipedia.org/wiki/Postfix_notation "Postfix notation") or [prefix notation](https://en.wikipedia.org/wiki/Prefix_notation "Prefix notation"), which do not need orders of operations.[^43] [^44] Hence, calculators utilizing [reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation "Reverse Polish notation") (RPN) using a [stack](https://en.wikipedia.org/wiki/Stack_\(data_structure\) "Stack (data structure)") to enter expressions in the correct order of precedence do not need parentheses or any possibly model-specific order of execution.[^29] [^26]

## Programming languages

Most [programming languages](https://en.wikipedia.org/wiki/Programming_languages "Programming languages") use precedence levels that conform to the order commonly used in mathematics,[^45] though others, such as [APL](https://en.wikipedia.org/wiki/APL_\(programming_language\) "APL (programming language)"), [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk "Smalltalk"), [Occam](https://en.wikipedia.org/wiki/Occam_\(programming_language\) "Occam (programming language)") and [Mary](https://en.wikipedia.org/wiki/Mary_\(programming_language\) "Mary (programming language)"), have no [operator](https://en.wikipedia.org/wiki/Operator_\(programming\) "Operator (programming)") precedence rules (in APL, evaluation is strictly right to left; in Smalltalk, it is strictly left to right).

Furthermore, because many operators are not associative, the order within any single level is usually defined by grouping left to right so that `16/4/4` is interpreted as (16/4)/4 = 1 rather than 16/(4/4) = 16; such operators are referred to as "left associative". Exceptions exist; for example, languages with operators corresponding to the [cons](https://en.wikipedia.org/wiki/Cons "Cons") operation on lists usually make them group right to left ("right associative"), e.g. in [Haskell](https://en.wikipedia.org/wiki/Haskell "Haskell"), `1:2:3:4:[] == 1:(2:(3:(4:[]))) == [1,2,3,4]`.

[Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie "Dennis Ritchie"), creator of the [C language](https://en.wikipedia.org/wiki/C_\(programming_language\) "C (programming language)"), said of the precedence in C (shared by programming languages that borrow those rules from C, for example, [C++](https://en.wikipedia.org/wiki/C%2B%2B "C++"), [Perl](https://en.wikipedia.org/wiki/Perl "Perl") and [PHP](https://en.wikipedia.org/wiki/PHP "PHP")) that it would have been preferable to move the [bitwise operators](https://en.wikipedia.org/wiki/Bitwise_operation "Bitwise operation") above the [comparison operators](https://en.wikipedia.org/wiki/Relational_operator "Relational operator").[^46] Many programmers have become accustomed to this order, but more recent popular languages like [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\) "Python (programming language)") [^47] and [Ruby](https://en.wikipedia.org/wiki/Ruby_\(programming_language\) "Ruby (programming language)") [^48] do have this order reversed. The relative precedence levels of operators found in many C-style languages are as follows:

| 1 | `()` `[]` `->` `.` `::` | Function call, scope, array/member access |
| --- | --- | --- |
| 2 | `!` `~` `-` `+` `*` `&` [`sizeof`](https://en.wikipedia.org/wiki/Sizeof "Sizeof") *[type cast](https://en.wikipedia.org/wiki/Type_conversion "Type conversion")* `++` `--` | (most) unary operators, [sizeof](https://en.wikipedia.org/wiki/Sizeof "Sizeof") and [type casts](https://en.wikipedia.org/wiki/Type_conversion "Type conversion") (right to left) |
| 3 | `*` `/` `%` `MOD` | Multiplication, division, [modulo](https://en.wikipedia.org/wiki/Modular_arithmetic "Modular arithmetic") |
| 4 | `+` `-` | Addition and subtraction |
| 5 | `<<` `>>` | Bitwise shift left and right |
| 6 | `<` `<=` `>` `>=` | Comparisons: less-than and greater-than |
| 7 | `==` `!=` | Comparisons: equal and not equal |
| 8 | `&` | Bitwise AND |
| 9 | `^` | Bitwise exclusive OR (XOR) |
| 10 | `\|` | Bitwise inclusive (normal) OR |
| 11 | `&&` | Logical AND |
| 12 | `\|\|` | Logical OR |
| 13 | `?` `:` | Conditional expression (ternary) |
| 14 | `=` `+=` `-=` `*=` `/=` `%=` `&=` `\|=` `^=` `<<=` `>>=` | Assignment operators (right to left) |
| 15 | `,` | [Comma operator](https://en.wikipedia.org/wiki/Comma_operator "Comma operator") |

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Algol_grammar_expr_svg.svg/500px-Algol_grammar_expr_svg.svg.png)

Simplified formal grammar for arithmetical expressions in a programming language (left), 49 and derivation of the example expression (a+b)^2/2 (right). The latter corresponds to a hierarchical structure (" syntax tree ") which is unique for the given expression. The compiler generates machine code from the tree in such a way that operations originating at the lowest hierarchy level are executed first.

Examples:

- `!A + !B` is interpreted as `(!A) + (!B)`
- `++A + !B` is interpreted as `(++A) + (!B)`
- `A + B * C` is interpreted as `A + (B * C)`
- `A || B && C` is interpreted as `A || (B && C)`
- `A && B == C` is interpreted as `A && (B == C)`
- `A & B == C` is interpreted as `A & (B == C)`

(In [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\) "Python (programming language)"), [Ruby](https://en.wikipedia.org/wiki/Ruby_\(programming_language\) "Ruby (programming language)"), [PARI/GP](https://en.wikipedia.org/wiki/PARI/GP "PARI/GP") and other popular languages, `A & B == C` is interpreted as `(A & B) == C`.)

[Source-to-source compilers](https://en.wikipedia.org/wiki/Source-to-source_compiler "Source-to-source compiler") that compile to multiple languages need to explicitly deal with the issue of different order of operations across languages. [Haxe](https://en.wikipedia.org/wiki/Haxe "Haxe") for example standardizes the order and enforces it by inserting brackets where it is appropriate.

The accuracy of software developer knowledge about binary operator precedence has been found to closely follow their frequency of occurrence in source code.[^50]

## History

The order of operations emerged progressively over centuries. The rule that multiplication has precedence over addition was incorporated into the development of [algebraic notation](https://en.wikipedia.org/wiki/Mathematical_notation "Mathematical notation") in the 1600s, since the distributive property implies this as a natural hierarchy. As recently as the 1920s, the historian of mathematics [Florian Cajori](https://en.wikipedia.org/wiki/Florian_Cajori "Florian Cajori") identifies disagreement about whether multiplication should have precedence over division, or whether they should be treated equally. The term "order of operations" and the "PEMDAS/BEDMAS" mnemonics were formalized only in the late 19th or early 20th century, as demand for standardized textbooks grew. Ambiguity about issues such as whether implicit multiplication takes precedence over explicit multiplication and division in such expressions as *a* /2 *b*, which could be interpreted as *a* /(2 *b*) or (*a* /2) × *b*, imply that the conventions are not yet completely stable.[^51] [^52]

[^1]: Some authors deliberately avoid any omission of parentheses with functions even in the case of single numerical variable or constant arguments (i.e. [Oldham in *Atlas*](#CITEREFOldhamMylandSpanier2009)), whereas other authors (like [NIST](#CITEREFOlverLozierBoisvertClark2010)) apply this notational simplification only conditionally in conjunction with specific multi-character function names (like `sin`), but don't use it with generic function names (like `*f*`).

[^2]: To avoid any ambiguity, this notational simplification for [monomials](https://en.wikipedia.org/wiki/Monomial "Monomial") is deliberately avoided in works such as [Oldham's *Atlas of Functions*](#CITEREFOldhamMylandSpanier2009) or the [*NIST Handbook of Mathematical Functions*](#CITEREFOlverLozierBoisvertClark2010).

[^3]: For example, the third edition of *Mechanics* by [Landau and Lifshitz](https://en.wikipedia.org/wiki/Landau_and_Lifshitz_\(book\) "Landau and Lifshitz (book)") contains expressions such as *hP* <sub><i>z</i></sub> /2π (p. 22), and the first volume of the *[Feynman Lectures](https://en.wikipedia.org/wiki/Feynman_Lectures "Feynman Lectures")* contains expressions such as 1/2√ *N* [(p. 6–7)](https://feynmanlectures.caltech.edu/I_06.html). In both books, these expressions are written with the convention that the [solidus](https://en.wikipedia.org/wiki/Slash_\(punctuation\) "Slash (punctuation)") is evaluated last.

[^4]: ["Calculation operators and precedence: Excel"](https://support.microsoft.com/en-us/office/calculation-operators-and-precedence-36de9366-46fe-43a3-bfa8-cf6d8068eacc). *Microsoft Support*. [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft"). 2023. Retrieved 2023-09-17.

[^5]: [Bronstein, Ilja Nikolaevič](https://en.wikipedia.org/wiki/Ilya_Nikolaevich_Bronshtein "Ilya Nikolaevich Bronshtein"); [Semendjajew, Konstantin Adolfovič](https://en.wikipedia.org/wiki/Konstantin_Adolfovic_Semendyayev "Konstantin Adolfovic Semendyayev") (1987) \[1945\]. "2.4.1.1. Definition arithmetischer Ausdrücke" \[Definition of arithmetic expressions\]. In Grosche, Günter; Ziegler, Viktor; Ziegler, Dorothea (eds.). *[Taschenbuch der Mathematik](https://en.wikipedia.org/wiki/Bronstein_and_Semendjajew "Bronstein and Semendjajew")* \[*Pocketbook of mathematics*\] (in German). Vol. 1. Translated by Ziegler, Viktor (23rd ed.). Thun, Switzerland: [Harri Deutsch](https://en.wikipedia.org/wiki/Verlag_Harri_Deutsch "Verlag Harri Deutsch"). pp. 115–120, 802. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [3-87144-492-8](https://en.wikipedia.org/wiki/Special:BookSources/3-87144-492-8 "Special:BookSources/3-87144-492-8"). Regel 7: Ist *F* (*A*) Teilzeichenreihe eines arithmetischen Ausdrucks oder einer seiner Abkürzungen und *F* eine Funktionenkonstante und *A* eine Zahlenvariable oder Zahlenkonstante, so darf *F A* dafür geschrieben werden. \[Darüber hinaus ist noch die Abkürzung *F* <sup><i>n</i></sup> (*A*) für (*F* (*A*)) <sup><i>n</i></sup> üblich. Dabei kann *F* sowohl Funktionenkonstante als auch Funktionenvariable sein.\]

[^6]: Peterson, Dave (Sep–Oct 2019). *The Math Doctors* (blog). Order of Operations: ["Why?"](https://www.themathdoctors.org/order-of-operations-why/); ["Why These Rules?"](https://www.themathdoctors.org/order-of-operations-why-these-rules/); ["Subtle Distinctions"](https://www.themathdoctors.org/order-of-operations-subtle-distinctions/); ["Fractions, Evaluating, and Simplifying"](https://www.themathdoctors.org/order-of-operations-fractions-evaluating-and-simplifying/); ["Implicit Multiplication?"](https://www.themathdoctors.org/order-of-operations-implicit-multiplication/); ["Historical Caveats"](https://www.themathdoctors.org/order-of-operations-historical-caveats/). Retrieved 2024-02-11.  
Peterson, Dave (Aug–Sep 2023). *The Math Doctors* (blog). Implied Multiplication: ["Not as Bad as You Think"](https://www.themathdoctors.org/implied-multiplication-1-not-as-bad-as-you-think/); ["Is There a Standard?"](https://www.themathdoctors.org/implied-multiplication-2-is-there-a-standard/); ["You Can't Prove It"](https://www.themathdoctors.org/implied-multiplication-3-you-cant-prove-it/). Retrieved 2024-02-11.

[^7]: Swokowski, Earl William (1978). [*Fundamentals of Algebra and Trigonometry*](https://books.google.com/books?id=bZdfLRHFGw8C) (4 ed.). Boston: Prindle, Weber & Schmidt. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-87150-252-6](https://en.wikipedia.org/wiki/Special:BookSources/0-87150-252-6 "Special:BookSources/0-87150-252-6"). p. 1: The *language of algebra* \[...\] may be used as shorthand, to abbreviate and simplify long or complicated statements.

[^8]: [Weisstein, Eric Wolfgang](https://en.wikipedia.org/wiki/Eric_Wolfgang_Weisstein "Eric Wolfgang Weisstein"). ["Precedence"](https://mathworld.wolfram.com/Precedence.html). *[MathWorld](https://en.wikipedia.org/wiki/MathWorld "MathWorld")*. Retrieved 2020-08-22.

[^9]: Oldham, Keith B.; Myland, Jan C.; Spanier, Jerome (2009) \[1987\]. *An Atlas of Functions: with Equator, the Atlas Function Calculator* (2nd ed.). Springer. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1007/978-0-387-48807-3](https://doi.org/10.1007%2F978-0-387-48807-3). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-48806-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-48806-6 "Special:BookSources/978-0-387-48806-6").

[^10]: Olver, Frank W. J.; Lozier, Daniel W.; Boisvert, Ronald F.; Clark, Charles W., eds. (2010). [*NIST Handbook of Mathematical Functions*](https://en.wikipedia.org/wiki/NIST_Handbook_of_Mathematical_Functions "NIST Handbook of Mathematical Functions"). [National Institute of Standards and Technology](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology "National Institute of Standards and Technology"). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-19225-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-19225-5 "Special:BookSources/978-0-521-19225-5"). [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [2723248](https://mathscinet.ams.org/mathscinet-getitem?mr=2723248).

[^11]: Angel, Allen R.; Runde, Dennis C.; Gilligan, Lawrence; Semmler, Richard (2010). *Elementary Algebra for College Students* (8th ed.). [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall "Prentice Hall"). Ch. 1, §9, Objective 3. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-321-62093-4](https://en.wikipedia.org/wiki/Special:BookSources/978-0-321-62093-4 "Special:BookSources/978-0-321-62093-4").

[^12]: ["Formula Returns Unexpected Positive Value"](https://web.archive.org/web/20150419091629/https://support.microsoft.com/en-gb/kb/kbview/132686). [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft"). 15 Aug 2005. Archived from [the original](https://support.microsoft.com/en-gb/kb/kbview/132686) on 2015-04-19. Retrieved 2012-03-05.

[^13]: [Berger, Roger L.](https://en.wikipedia.org/wiki/Roger_Lee_Berger "Roger Lee Berger") (2007). "Nonstandard operator precedence in Excel". *Computational Statistics & Data Analysis*. **51** (6): 2788–2791. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.csda.2006.09.040](https://doi.org/10.1016%2Fj.csda.2006.09.040).

[^14]: [Chrystal, George](https://en.wikipedia.org/wiki/George_Chrystal "George Chrystal") (1904) \[1886\]. *Algebra*. Vol. 1 (5th ed.). ["Division", Ch. 1 §§19–26](https://archive.org/details/algebraelementar01chryuoft/page/14/), pp. 14–20.

Chrystal's book was the canonical source in English about secondary school algebra of the turn of the 20th century, and plausibly the source for many later descriptions of the order of operations. However, while Chrystal's book initially establishes a rigid rule for evaluating expressions involving '÷' and '×' symbols, it later consistently gives implicit multiplication higher precedence than division when writing inline fractions, without ever explicitly discussing the discrepancy between formal rule and common practice.

[^15]: [Cajori, Florian](https://en.wikipedia.org/wiki/Florian_Cajori "Florian Cajori") (1928). *[A History of Mathematical Notations](https://en.wikipedia.org/wiki/A_History_of_Mathematical_Notations "A History of Mathematical Notations")*. Vol. 1. La Salle, Illinois: Open Court. [§242. "Order of operations in terms containing both ÷ and ×"](https://archive.org/details/b29980343_0001/page/274/), p. 274.

[^16]: Wu, Hung-Hsi (2007) \[2004\]. ["'Order of operations' and other oddities in school mathematics"](https://math.berkeley.edu/~wu/order5.pdf) (PDF). Dept. of Mathematics, University of California. Retrieved 2007-07-03.

[^17]: In the [ISO 80000](https://en.wikipedia.org/wiki/ISO/IEC_80000 "ISO/IEC 80000") standard, the division symbol '÷' is entirely disallowed in favor of a slash symbol: ISO 80000-2:2019, ["Quantities and units – Part 2: Mathematics"](https://www.iso.org/obp/ui/#iso:std:iso:80000:-2:ed-2:v2:en). [International Standards Organization](https://en.wikipedia.org/wiki/International_Standards_Organization "International Standards Organization").

[^18]: Lennes, N. J. (1917). ["Discussions: Relating to the Order of Operations in Algebra"](https://archive.org/details/sim_american-mathematical-monthly_1917-02_24_2/page/92). *The American Mathematical Monthly*. **24** (2): 93–95. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/2972726](https://doi.org/10.2307%2F2972726). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [2972726](https://www.jstor.org/stable/2972726).

[^19]: [Strogatz, Steven](https://en.wikipedia.org/wiki/Steven_Strogatz "Steven Strogatz") (2 Aug 2019). ["The Math Equation That Tried to Stump the Internet"](https://www.nytimes.com/2019/08/02/science/math-equation-pedmas-bemdas-bedmas.html). *The New York Times*. Retrieved 2024-02-12. In this article, Strogatz describes the order of operations as taught in middle school. However, [in a comment](https://www.nytimes.com/2019/08/02/science/math-equation-pedmas-bemdas-bedmas.html), he points out, "Several commenters appear to be using a different (and more sophisticated) convention than the elementary PEMDAS convention I described in the article. In this more sophisticated convention, which is often used in algebra, implicit multiplication (also known as multiplication by juxtaposition) is given higher priority than explicit multiplication or explicit division (in which one explicitly writes operators like × \* / or ÷). Under this more sophisticated convention, the implicit multiplication in 2(2 + 2) is given higher priority than the explicit division implied by the use of ÷. That’s a very reasonable convention, and I agree that the answer is 1 if we are using this sophisticated convention. "But that convention is not universal. For example, the calculators built into Google and WolframAlpha use the less sophisticated convention that I described in the article; they make no distinction between implicit and explicit multiplication when they are asked to evaluate simple arithmetic expressions. \[...\]"

[^20]: ["Physical Review Style and Notation Guide"](https://publish.aps.org/files/styleguide-pr.pdf) (PDF). [American Physical Society](https://en.wikipedia.org/wiki/American_Physical_Society "American Physical Society"). 2012. § IV.E.2.e. Retrieved 2012-08-05.

[^21]: [Graham, Ronald L.](https://en.wikipedia.org/wiki/Ronald_L._Graham "Ronald L. Graham"); [Knuth, Donald E.](https://en.wikipedia.org/wiki/Donald_E._Knuth "Donald E. Knuth"); [Patashnik, Oren](https://en.wikipedia.org/wiki/Oren_Patashnik "Oren Patashnik") (1994). *Concrete Mathematics* (2nd ed.). Reading, Mass: Addison-Wesley. "A Note on Notation", p. xi. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-201-55802-5](https://en.wikipedia.org/wiki/Special:BookSources/0-201-55802-5 "Special:BookSources/0-201-55802-5"). [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1397498](https://mathscinet.ams.org/mathscinet-getitem?mr=1397498). An expression of the form *a* / *bc* means the same as *a* /(*bc*). Moreover, log *x* /log *y* = (log *x*)/(log *y*) and 2 *n*! = 2(*n*!).

[^22]: Fateman, R. J.; Caspi, E. (1999). [*Parsing TEX into mathematics*](https://people.eecs.berkeley.edu/~fateman/papers/parsing_tex.pdf) (PDF). International Symposium on Symbolic and Algebraic Computation, Vancouver, 28–31 July 1999.

[^23]: Haelle, Tara (12 Mar 2013). ["What *Is* the Answer to That Stupid Math Problem on Facebook? And why are people so riled up about it?"](https://slate.com/technology/2013/03/facebook-math-problem-why-pemdas-doesnt-always-give-a-clear-answer.html). *Slate*. Retrieved 2023-09-17.

[^24]: ["Rules of arithmetic"](http://www.mathcentre.ac.uk/resources/uploaded/mc-ty-rules-2009-1.pdf) (PDF). *Mathcentre.ac.uk*. 2009. Retrieved 2019-08-02.

[^25]: Ginsburg, David (1 Jan 2011). ["Please Excuse My Dear Aunt Sally (PEMDAS)--Forever!"](http://blogs.edweek.org/teachers/coach_gs_teaching_tips/2011/01/math_teachers_please_excuse_dear_aunt_sally--forever.html). *Education Week - Coach G's Teaching Tips*. Retrieved 2023-09-17.

[^26]: Vanderbeek, Greg (2007). [*Order of Operations and RPN*](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1045&context=mathmidexppap) (Expository paper). Master of Arts in Teaching (MAT) Exam Expository Papers. Lincoln: University of Nebraska. Paper 46. Retrieved 2020-06-14.

[^27]: Ali Rahman, Ernna Sukinnah; Shahrill, Masitah; Abbas, Nor Arifahwati; Tan, Abby (2017). ["Developing Students' Mathematical Skills Involving Order of Operations"](https://files.eric.ed.gov/fulltext/EJ1148460.pdf) (PDF). *International Journal of Research in Education and Science*. **3** (2): 373–382. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.21890/ijres.327896](https://doi.org/10.21890%2Fijres.327896) (inactive 12 Jul 2025). p. 373: The PEMDAS is an acronym or mnemonic for the order of operations that stands for Parenthesis, Exponents, Multiplication, Division, Addition and Subtraction. This acronym is widely used in the United States of America. Meanwhile, in other countries such as United Kingdom and Canada, the acronyms used are BODMAS (Brackets, Order, Division, Multiplication, Addition and Subtraction) and BIDMAS (Brackets, Indices, Division, Multiplication, Addition and Subtraction).

[^28]: ["Le calcul qui divise: 6÷2(1+2)"](https://www.youtube.com/watch?v=tYf3CpbqAVo). *Micmaths* (Video) (in French). 17 Nov 2020.

[^29]: Ball, John A. (1978). [*Algorithms for RPN calculators*](https://archive.org/details/algorithmsforrpn0000ball/page/31) (1st ed.). Cambridge, Mass: Wiley. p. 31. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-471-03070-8](https://en.wikipedia.org/wiki/Special:BookSources/0-471-03070-8 "Special:BookSources/0-471-03070-8").

[^30]: Davies, Peter (1979). "BODMAS Exposed". *Mathematics in School*. **8** (4): 27–28. [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [30213488](https://www.jstor.org/stable/30213488).

[^31]: Knight, I. S. (1997). "Why BODMAS?". *The Mathematical Gazette*. **81** (492): 426–427. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.2307/3619621](https://doi.org/10.2307%2F3619621). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [3619621](https://www.jstor.org/stable/3619621).

[^32]: ["Order of operations"](https://web.archive.org/web/20210224172758/https://syllabus.bos.nsw.edu.au/assets/global/files/maths_s3_sampleu1.doc). *Syllabus.bos.nsw.edu.au*. Archived from [the original](http://syllabus.bos.nsw.edu.au/assets/global/files/maths_s3_sampleu1.doc) (DOC) on 2021-02-24. Retrieved 2019-08-02.

[^33]: Foster, Colin (2008). ["Higher Priorities"](https://www.researchgate.net/publication/261812399). *Mathematics in School*. **37** (3): 17. [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [30216129](https://www.jstor.org/stable/30216129).

[^34]: Naddor, Josh (2020). [*Order of Operations: Please Excuse My Dear Aunt Sally as her rule is deceiving*](https://esploro.libs.uga.edu/esploro/outputs/9949365543302959) (MA thesis). University of Georgia.

[^35]: Ameis, Jerry A. (2011). "The Truth About PEDMAS". *Mathematics Teaching in the Middle School*. **16** (7): 414–420. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.5951/MTMS.16.7.0414](https://doi.org/10.5951%2FMTMS.16.7.0414). [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [41183631](https://www.jstor.org/stable/41183631).

[^36]: [Cheng, Eugenia](https://en.wikipedia.org/wiki/Eugenia_Cheng "Eugenia Cheng") (2023). *Is Math Real? How Simple Questions Lead Us to Mathematics' Deepest Truths*. Basic Books. pp. 235–238. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-541-60182-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-541-60182-6 "Special:BookSources/978-1-541-60182-6").

[^37]: Lee, Jae Ki; Licwinko, Susan; Taylor-Buckner, Nicole (2013). ["Exploring Mathematical Reasoning of the Order of Operations: Rearranging the Procedural Component PEMDAS"](https://journals.library.columbia.edu/index.php/jmetc/article/download/633/79). *[Journal of Mathematics Education at Teachers College](https://en.wikipedia.org/wiki/Journal_of_Mathematics_Education_at_Teachers_College "Journal of Mathematics Education at Teachers College")*. **4** (2): 73–78. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.7916/jmetc.v4i2.633](https://doi.org/10.7916%2Fjmetc.v4i2.633). p. 73: \[...\] students frequently make calculation errors with expressions which have either multiplication and division or addition and subtraction next to each other. \[...\]

[^38]: Dupree, Kami M. (2016). "Questioning the Order of Operations". *Mathematics Teaching in the Middle School*. **22** (3): 152–159. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.5951/mathteacmiddscho.22.3.0152](https://doi.org/10.5951%2Fmathteacmiddscho.22.3.0152).

[^39]: Taff, Jason (2017). "Rethinking the Order of Operations (or What Is the Matter with Dear Aunt Sally?)". *The Mathematics Teacher*. **111** (2): 126–132. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.5951/mathteacher.111.2.0126](https://doi.org/10.5951%2Fmathteacher.111.2.0126).

[^40]: ["Calculation Priority Sequence"](https://support.casio.com/global/en/calc/manual/fx-82MS_85MS_220PLUS_300MS_350MS_en/technical_informatoin/sequence.html). *support.casio.com*. [Casio](https://en.wikipedia.org/wiki/Casio "Casio"). Retrieved 2019-08-01.

[^41]: ["Implied Multiplication Versus Explicit Multiplication on TI Graphing Calculators"](https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/product-usage/11773). [Texas Instruments](https://en.wikipedia.org/wiki/Texas_Instruments "Texas Instruments"). 2011. Retrieved 2025-07-22.

[^42]: [*Announcing the TI Programmable 88!*](http://www.datamath.net/Leaflets/TI-88_Announcement.pdf) (PDF). [Texas Instruments](https://en.wikipedia.org/wiki/Texas_Instruments "Texas Instruments"). 1982. Retrieved 2017-08-03. Now, implied multiplication is recognized by the [AOS](https://en.wikipedia.org/wiki/Algebraic_Operating_System "Algebraic Operating System") and the square root, logarithmic, and trigonometric functions can be followed by their arguments as when working with pencil and paper. (NB. The TI-88 only existed as a prototype and was never released to the public.)

[^43]: [Simons, Peter Murray](https://en.wikipedia.org/wiki/Peter_Murray_Simons "Peter Murray Simons") (2021). ["Łukasiewicz's Parenthesis-Free or Polish Notation"](https://plato.stanford.edu/entries/lukasiewicz/polish-notation.html). *[Stanford Encyclopedia of Philosophy](https://en.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy")*. Dept. of Philosophy, Stanford University. Retrieved 2022-03-26.

[^44]: Krtolica, Predrag V.; Stanimirović, Predrag S. (1999). "On some properties of reverse Polish Notation". *Filomat*. **13**: 157–172. [JSTOR](https://en.wikipedia.org/wiki/JSTOR_\(identifier\) "JSTOR (identifier)") [43998756](https://www.jstor.org/stable/43998756).

[^45]: Henderson, Harry (2009) \[2003\]. ["Operator Precedence"](https://books.google.com/books?id=3Tla6d153uwC&pg=PA355). *Henderson's Encyclopedia of Computer Science and Technology* (Rev. ed.). New York: [Facts on File](https://en.wikipedia.org/wiki/Facts_On_File,_Inc. "Facts On File, Inc."). p. 355. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-8160-6382-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-8160-6382-6 "Special:BookSources/978-0-8160-6382-6"). Retrieved 2023-09-17.

[^46]: [Ritchie, Dennis M.](https://en.wikipedia.org/wiki/Dennis_M._Ritchie "Dennis M. Ritchie") (1996). "The Development of the C Language". [*History of Programming Languages*](https://www.bell-labs.com/usr/dmr/www/chist.html) (2 ed.). [ACM Press](https://en.wikipedia.org/wiki/ACM_Press "ACM Press").

[^47]: ["6. Expressions"](https://docs.python.org/3/reference/expressions.html). *Python documentation*. Retrieved 2023-12-31.

[^48]: ["precedence - RDoc Documentation"](https://docs.ruby-lang.org/en/master/syntax/precedence_rdoc.html).

[^49]: [Backus, John Warner](https://en.wikipedia.org/wiki/John_Warner_Backus "John Warner Backus"); et al. (1963). "§ 3.3.1: Arithmetic expressions". In [Naur, Peter](https://en.wikipedia.org/wiki/Peter_Naur "Peter Naur") (ed.). [Revised Report on the Algorithmic Language Algol 60](https://www.masswerk.at/algol60/report.htm) (Report). Retrieved 2023-09-17. (CACM Vol. 6 pp. 1–17; The Computer Journal, Vol. 9, p. 349; Numerische Mathematik, Vol. 4, p. 420.)

[^50]: Jones, Derek M. (2008) \[2006\]. ["Developer beliefs about binary operator precedence"](http://www.knosof.co.uk/cbook/accu06.html). *CVu*. **18** (4): 14–21. Retrieved 2023-09-17.

[^51]: Jensen, Patricia. ["History and Background"](http://5010.mathed.usu.edu/Fall2013/PJensen/History.html). *5010.mathed.usu.edu*. Utah State University. Retrieved 2024-10-04.

[^52]: Peterson, Dave (22 Nov 2000). ["History of the Order of Operations"](https://web.archive.org/web/20020619105005/http://mathforum.org/library/drmath/view/52582.html). *The Math Forum: Ask Dr Math*. Archived from [the original](http://mathforum.org/library/drmath/view/52582.html) on 2002-06-19.