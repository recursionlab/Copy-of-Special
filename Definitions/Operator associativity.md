---
title: "Operator associativity"
source: "https://en.wikipedia.org/wiki/Operator_associativity"
author:
  - "[[Wikipedia]]"
published: 2004-02-07
created: 2026-05-16
description:
tags:
  - "clippings"
---
In [programming language theory](https://en.wikipedia.org/wiki/Programming_language_theory "Programming language theory"), the **associativity** of an [operator](https://en.wikipedia.org/wiki/Operator_\(programming\) "Operator (programming)") is a property that determines how operators of the same [precedence](https://en.wikipedia.org/wiki/Order_of_operations "Order of operations") are grouped in the absence of [parentheses](https://en.wikipedia.org/wiki/Bracket_\(mathematics\) "Bracket (mathematics)"). If an [operand](https://en.wikipedia.org/wiki/Operand "Operand") is both preceded and followed by operators (for example, `^ 3 ^`), and those operators have equal precedence, then the operand may be used as input to two different operations (i.e. the two operations indicated by the two operators). The choice of which operations to apply the operand to, is determined by the **associativity** of the operators. Operators may be **associative** (meaning the operations can be grouped arbitrarily), **left-associative** (meaning the operations are grouped from the left), **right-associative** (meaning the operations are grouped from the right) or **non-associative** (meaning operations cannot be chained, often because the output type is incompatible with the input types). The associativity and precedence of an operator is a part of the definition of the programming language; different programming languages may have different associativity and precedence for the same type of operator.

Consider the expression `a ~ b ~ c`. If the operator `~` has left associativity, this expression would be interpreted as `(a ~ b) ~ c`. If the operator has right associativity, the expression would be interpreted as `a ~ (b ~ c)`. If the operator is non-associative, the expression might be a [syntax error](https://en.wikipedia.org/wiki/Syntax_error "Syntax error"), or it might have some special meaning. Some mathematical operators have inherent associativity. For example, subtraction and division, as used in conventional math notation, are inherently left-associative. Addition and multiplication, by contrast, are both left and right associative. (e.g. `(a * b) * c = a * (b * c)`).

Many programming language manuals provide a table of operator precedence and associativity; see, for example, [the table for C and C++](https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B#Operator_precedence "Operators in C and C++").

The concept of notational associativity described here is related to, but different from, the mathematical [associativity](https://en.wikipedia.org/wiki/Associativity "Associativity"). An operation that is mathematically associative, by definition requires no notational associativity. (For example, addition has the associative property, therefore it does not have to be either left associative or right associative.) An operation that is not mathematically associative, however, must be notationally left-, right-, or non-associative. (For example, subtraction does not have the associative property, therefore it must have notational associativity.)

## Examples

Associativity is only needed when the operators in an expression have the same precedence. Usually `+` and `-` have the same precedence. Consider the expression `7 - 4 + 2`. The result could be either `(7 - 4) + 2 = 5` or `7 - (4 + 2) = 1`. The former result corresponds to the case when `+` and `-` are left-associative, the latter to when `+` and `-` are right-associative.

In order to reflect normal usage, [addition](https://en.wikipedia.org/wiki/Addition "Addition"), [subtraction](https://en.wikipedia.org/wiki/Subtraction "Subtraction"), [multiplication](https://en.wikipedia.org/wiki/Multiplication "Multiplication"), and [division](https://en.wikipedia.org/wiki/Division_\(mathematics\) "Division (mathematics)") operators are usually left-associative,[^2] [^3] [^4] while for an [exponentiation](https://en.wikipedia.org/wiki/Exponentiation "Exponentiation") operator (if present) [^5] there is no general agreement. Any [assignment](https://en.wikipedia.org/wiki/Assignment_\(computer_science\) "Assignment (computer science)") operators are typically right-associative. To prevent cases where operands would be associated with two operators, or no operator at all, operators with the same precedence must have the same associativity.

### A detailed example

Consider the expression `5^4^3^2`, in which `^` is taken to be a right-associative exponentiation operator. A parser reading the tokens from left to right would apply the associativity rule to a branch, because of the right-associativity of `^`, in the following way:

1. Term `5` is read.
2. Nonterminal `^` is read. Node: " `5^` ".
3. Term `4` is read. Node: " `5^4` ".
4. Nonterminal `^` is read, triggering the right-associativity rule. Associativity decides node: " `5^(4^` ".
5. Term `3` is read. Node: " `5^(4^3` ".
6. Nonterminal `^` is read, triggering the re-application of the right-associativity rule. Node " `5^(4^(3^` ".
7. Term `2` is read. Node " `5^(4^(3^2` ".
8. No tokens to read. Apply associativity to produce parse tree " `5^(4^(3^2))` ".

This can then be evaluated depth-first, starting at the top node (the first `^`):

1. The evaluator walks down the tree, from the first, over the second, to the third `^` expression.
2. It evaluates as: 3 <sup>2</sup> = 9. The result replaces the expression branch as the second operand of the second `^`.
3. Evaluation continues one level up the [parse tree](https://en.wikipedia.org/wiki/Parse_tree "Parse tree") as: 4 <sup>9</sup> = 262,144. Again, the result replaces the expression branch as the second operand of the first `^`.
4. Again, the evaluator steps up the tree to the root expression and evaluates as: 5 <sup>262144</sup> ≈ 6.2060699×10 <sup>183230</sup>. The last remaining branch collapses and the result becomes the overall result, therefore completing overall evaluation.

A left-associative evaluation would have resulted in the parse tree `((5^4)^3)^2` and the completely different result (625 <sup>3</sup>) <sup>2</sup> = 244,140,625 <sup>2</sup> ≈ 5.9604645×10 <sup>16</sup>.

## Right-associativity of assignment operators

In many [imperative programming languages](https://en.wikipedia.org/wiki/Imperative_programming_language "Imperative programming language"), the [assignment operator](https://en.wikipedia.org/wiki/Assignment_operator "Assignment operator") is defined to be right-associative, and assignment is defined to be an expression (which evaluates to a value), not just a statement. This allows [chained assignment](https://en.wikipedia.org/wiki/Assignment_\(computer_science\)#Chained_assignment "Assignment (computer science)") by using the value of one assignment expression as the right operand of the next assignment expression.

In [C](https://en.wikipedia.org/wiki/C_\(programming_language\) "C (programming language)"), the assignment `a = b` is an expression that evaluates to the same value as the expression `b` converted to the type of `a`, with the [side effect](https://en.wikipedia.org/wiki/Side_effect_\(computer_science\) "Side effect (computer science)") of storing the [R-value](https://en.wikipedia.org/wiki/Value_\(computer_science\)#lrvalue "Value (computer science)") of `b` into the [L-value](https://en.wikipedia.org/wiki/Value_\(computer_science\)#lrvalue "Value (computer science)") of `a`.[^1] Therefore the expression `a = (b = c)` can be interpreted as `b = c; a = b;`. The alternative expression `(a = b) = c` raises an error because `a = b` is not an L-value expression, i.e. it has an R-value but not an L-value where to store the R-value of `c`. The right-associativity of the `=` operator allows expressions such as `a = b = c` to be interpreted as `a = (b = c)`.

In [C++](https://en.wikipedia.org/wiki/C%2B%2B "C++"), the assignment `a = b` is an expression that evaluates to the same value as the expression `a`, with the side effect of storing the R-value of `b` into the L-value of `a`. Therefore the expression `a = (b = c)` can still be interpreted as `b = c; a = b;`. And the alternative expression `(a = b) = c` can be interpreted as `a = b; a = c;` instead of raising an error. The right-associativity of the `=` operator allows expressions such as `a = b = c` to be interpreted as `a = (b = c)`.

## Non-associative operators

Non-associative operators are operators that have no defined behavior when used in sequence in an expression. In [Prolog](https://en.wikipedia.org/wiki/Prolog "Prolog") the infix operator `:-` is **non-associative** because constructs such as " `a :- b :- c` " constitute syntax errors.

Another possibility is that sequences of certain operators are interpreted in some other way, which cannot be expressed as associativity. This generally means that syntactically, there is a special rule for sequences of these operations, and semantically the behavior is different. A good example is in [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\) "Python (programming language)"), which has several such constructs.[^6] Since assignments are statements, not operations, the assignment operator does not have a value and is not associative. [Chained assignment](https://en.wikipedia.org/wiki/Assignment_\(computer_science\)#Chained_assignment "Assignment (computer science)") is instead implemented by having a grammar rule for sequences of assignments `a = b = c`, which are then assigned left-to-right. Further, combinations of assignment and [augmented assignment](https://en.wikipedia.org/wiki/Augmented_assignment "Augmented assignment"), like `a = b += c` are not legal in Python, though they are legal in C. Another example are comparison operators, such as `>`, `==`, and `<=`. A chained comparison like `a < b < c` is interpreted as `(a < b) and (b < c)`, not equivalent to either `(a < b) < c` or `a < (b < c)`.[^7]

[^1]: An expression can be made into a [statement](https://en.wikipedia.org/wiki/Statement_\(programming\) "Statement (programming)") by following it with a semicolon; i.e. `a = b` is an expression but `a = b;` is a statement.

[^2]: Education Place: [The Order of Operations](http://eduplace.com/math/mathsteps/4/a/index.html)

[^3]: [Khan Academy](https://en.wikipedia.org/wiki/Khan_Academy "Khan Academy"): [The Order of Operations](https://www.khanacademy.org/math/pre-algebra/pre-algebra-arith-prop/pre-algebra-order-of-operations/v/introduction-to-order-of-operations), timestamp [5m40s](https://www.youtube.com/watch?v=ClYdw4d4OmA&t=5m40s)

[^4]: Virginia Department of Education: [Using Order of Operations and Exploring Properties](http://www.doe.virginia.gov/instruction/mathematics/middle/algebra_readiness/curriculum_companion/order-operations.pdf#page=3) [Archived](https://web.archive.org/web/20220716062834/http://www.doe.virginia.gov/instruction/mathematics/middle/algebra_readiness/curriculum_companion/order-operations.pdf#page=3) 2022-07-16 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine"), section 9

[^5]: [Exponentiation Associativity and Standard Math Notation](https://codeplea.com/exponentiation-associativity-options) Codeplea. 23 Aug 2016. Retrieved 20 Sep 2016.

[^6]: *[The Python Language Reference](https://docs.python.org/3/reference/),* " [6\. Expressions](https://docs.python.org/3/reference/expressions.html) "

[^7]: *[The Python Language Reference](https://docs.python.org/3/reference/),* " [6\. Expressions](https://docs.python.org/3/reference/expressions.html) ": [6.9. Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)