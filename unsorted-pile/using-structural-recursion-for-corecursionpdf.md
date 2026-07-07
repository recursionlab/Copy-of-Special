---
created: 2026-05-11
psi_tier: zero_divisor
sources:
- Using Structural Recursion for Corecursion.pdf.md
tags:
- zero_divisor
- ingested
title: Using Structural Recursion For Corecursion.Pdf
type: concept
updated: 2026-05-11
---

# Using Structural Recursion For Corecursion.Pdf

# Using Structural Recursion for Corecursion.pdf

Using Structural Recursion for Corecursion
Yves Bertot1 and Ekaterina Komendantskaya2
1 INRIA Sophia Antipolis, France
Yves.Bertot@inria.fr

2 School of Computer Science, University of St Andrews, UK
ek@cs.st-andrews.ac.uk

⋆
Abstract. We propose a (limited) solution to the problem of construct-ing stream values defined by recursive equations that do not respect the guardedness condition. The guardedness condition is imposed on defi-nitions of corecursive functions in Coq, AGDA, and other higher-order proof assistants. In this paper, we concentrate in particular on those non-guarded equations where recursive calls appear under functions. We use a correspondence between streams and functions over natural numbers to show that some classes of non-guarded definitions can be modelled through the encoding as structural recursive functions. In practice, this work extends the class of stream values that can be defined in a construc-tive type theory-based theorem prover with inductive and coinductive types, structural recursion and guarded corecursion. Key words: Constructive Type Theory, Structural Recursion, Coinduc-tive types, Guarded Corecursion, Coq
1 Introduction
Interactive theorem provers with inductive types [27, 28, 20, 16] provide a re-stricted programming language together with a formal meta-theory for reason-ing about the language. This language is very close to functional programming languages, so that the verification of a program in a conventional functional programming language can often be viewed as a simple matter of adapting the program’s formulation to a theorem prover’s syntax, thus obtaining a faithful prover-level model. Then one can reason about this model in the theorem prover. This approach has inspired studies of a large collection of algorithms, starting from simple examples like sorting algorithms to more complex algorithms, like the ones used in the computation of Gröbner bases, the verification of the four-colour theorem, or compilers.

However, the prover’s programming language is restricted, especially con-cerning recursion. For instance, structural restriction ensures that all programs terminate, so that values are never undefined; we give details in Section 2. Ap-proaches to cope with potentially non-terminating programs are available, espe-cially by encoding domain theory as in HOLCF [24], but these approaches tend

⋆ Work is partially supported by the INRIA CORDI post-doctoral program, the ANR project “A3Pat” ANR-05-BLAN-0146 and by EPSRC postdoctoral grant EP/F044046/1.
to make the description of programs more cumbersome, because the exceptional case where a computation may not terminate needs to be covered at every stage. An alternative is to manage a larger class of terminating functions, mainly using well-founded recursion [22, 26], and this approach is now widely spread among all interactive theorem provers.
A few theorem provers [27, 28, 20] also support coinduction. Coinductive datatypes provide a way to look at infinite data objects. In particular, streams of data can be viewed as infinite lists. Coinductive datatypes also provide room for a new class of recursive objects, known as corecursive objects.

Termination is not required anymore for these functions, but termination still plays a role, since every finite value should still be computable in finite time, even if the computation involves an interaction with a corecursive value. This constraint boils down to a concept of productivity. Roughly speaking, infinite sequences of recursive calls where no data is being produced must be avoided. For recursive programs, productivity is undecidable for the same reason that termination is. For this reason, a more restrictive criterion is used to describe corecursive functions that are legitimate in theorem provers.

A theorem prover like Coq provides two kinds of recursion: terminating re-cursion, initially based on structural recursion for inductive types, which can also handle well-founded recursion; and productive corecursion, based on “guarded” corecursion [10, 15]. Efforts have been made to extend the basic guarded corecur-sion in the same spirit that well-founded recursion extends the basic structural re-cursion. We can mention [14] and [4, 7], which basically incorporate well-founded recursion to make sure several non-productive recursive calls are allowed as long as they ultimately become productive. In particular, [14] introduces a gener-alization of the concept of well-founded relation that uses an extra dimension to cover at the same time recursive or co-recursive functions; since there is an extra dimension, two notions of limits can be used and recursive values can mix terminating recursive and productive co-recursive aspects in a seamless fashion.
One essential characteristic of well-founded induction and the complete or-dered families of equivalences in [14] is that the well-founded relation or families of equivalences must be given as extra data to make it possible to start the definition process. In the alternative approach described in this paper, we want to avoid this extra burden imposed on the user, and we attempt to develop a methodology that remains syntactic in nature.

We will concentrate on a class of recursive definitions where mapping func-tions interfere in the recursive equation, thus preventing the recursive equation to be recognised as guarded by constructors. The infinite sequences of Fibonacci numbers (considered e.g., in [1]) and of natural numbers (see Example 5) are famous representatives of the class. Many of the corecursive values studied, for example, in [25, 12, 13] fail to satisfy the guardedness condition, precisely because functions like map interfere in the recursive definition. A very elegant method of lazy differentiation [19] also gives rise to a function of multiplication for infinite streams of derivatives in the same class of definitions.

A simple example is the following recursive equation (studied later as Exam-ple 5):
nats = 1::map S nats
A quick analysis shows that we can use this equation to infer the value of each element in the stream: the first value is given directly, the second element is obtained from the first one through the behaviour of the map function, and so on. This recursive equation is a legitimate specification of a stream, and it can actually be used as a definition in a conventional lazy functional programming language like Haskell.
Thus the question studied in this article is: given a recursive equation like the one concerning nats, can we build a corecursive value that satisfies this equa-tion, using only structural recursion and guarded corecursion? We will describe a partial solution to this problem. We will also show that this solution can in-corporate other interfering functions than map. In Section 3, we briefly overview the class of the functions we target.
Our proposed approach is to map every stream value to a function over natu-ral numbers in a reversible way: a stream s0::s1::· · · is mapped to the function JsK : i 7→ si, and the reverse map is an easily defined guarded corecursive function. It appears that all legitimate guarded corecursive values are mapped to struc-turally recursive functions and that the question of productivity is transformed into a question of termination. We discuss it in Section 5.
Moreover, uses of the map function and similar operations are transformed into program fragments that still respect the constraints of structural recursion. Thus, there are stream values whose recursive definitions as streams are mapped to structural recursive definitions, even though the initial equations did not re-spect guardedness constraints. For these stream values, we propose to define the corresponding recursive function using structural recursion, and then to produce the stream value using the reverse map from functions over natural numbers to streams. We present this method in Section 6.
2 Structurally Recursive Functions
We start with defining the notions of inductive and coinductive types, and recur-sive/corecursive functions. We will use the syntax of Coq throughout. For a more detailed introduction to Coq, see [5]. One can also handle inductive and coin-ductive types within HOL (proof assistant Isabelle) [23], and within Martin-Löf type theory (proof assistant AGDA) [27].
Inductive data types are defined by introducing a few basic constructors that generate elements of the new type.

Definition 1. The definition of the inductive type of natural numbers is built using two constructors O and S:

Inductive nat : Set := O : nat | S : nat -> nat.
This definition also implies that the type supports both pattern-matching and recursion: on the one hand, all values in the type are either of the form O or of the form (S x); on the other hand, all values are finite and a function is well defined when its value on O is given and the value for S x can be computed from the value for x.
After the inductive type is defined, one can define its inhabitants and func-tions on it. Most functions defined on the inductive type must be defined recur-sively, that is, by describing values for different patterns of the constructors and by allowing calls to the same function on variables taken from the patterns.

Example 1. The recursive function below computes the n-th Fibonacci number.

Fixpoint fib (n:nat) : nat :=
match n with
| O => 1
| S O => 1
| S (S p as q) => fib p + fib q
end.

There is one important property we wish every function defined in Coq to possess: it is termination. To guarantee this, Coq uses a syntactic restriction on definitions of functions, called structural recursion. A structurally recursive definition is such that every recursive call is performed on a structurally smaller argument. The function fib is structurally recursive: all recursive calls are made on variables (here p and q) that were obtained through pattern-matching from the initial argument.

There are many useful functions and algorithms that are not structurally recursive, but general recursive. They are not accepted by Coq or similar proof assistants directly, but they can be defined using various forms of well-founded induction or induction with respect to a predicate [5, 8].

It is perhaps worth mentioning that there exists an approach to termina-tion called “type-based termination” [1, 3, 17]. The essence of different methods proposed under this name is rejection of the structural recursion as being a too restrictive and narrow method for guaranteeing termination. Instead, this job is delegated to sized higher-order types. The type-based termination promises to be a powerful tool, but it is not easy to implement it. As for today, the major proof assistants still rely on structural recursion. Some non-guarded functions we formalise in this paper, can also be handled by methods of type-based termina-tion. However, yet it gives little from the point of view of practical programming and automated proving. Therefore the value of this paper, as well as (e.g.) [5, 7, 8] is in the technical elegance and practical implementation in the existing proof assistants.
3 Guardedness
We now consider corecursion.
The following is the definition of a coinductive type of infinite streams, built using one constructor Cons.

Definition 2. The type of streams is given by

CoInductive Stream (A:Set) : Set :=
Cons: A -> Stream A -> Stream A.
In the rest of this paper, we will write a::tl for Cons a tl, leaving the argu-ment A to be inferred from the context.
While a structurally recursive function is supposed to rely on an inductive type for its domain and is restricted in the way recursive calls are using this input, a corecursive function is supposed to rely on a co-inductive type for its co-domain and is restricted in the way recursive calls are used for producing the output.

Definition 3 (Guardedness). A position in an expression is pre-guarded if it occurs as the root of the expression, or if it is a direct sub-term of a pattern-matching construct or a conditional statement, which is itself in a pre-guarded position.

A position is guarded if it occurs as a direct sub-term of a constructor for the co-inductive type that is being defined and if this constructor occurs in a pre-guarded position or a guarded position. A corecursive function is guarded if all its corecursive calls occur in guarded positions.

Example 2. The coinductive function map applies a given function f to a given infinite stream.

CoFixpoint map (A B :Type)(f: A -> B)(s: Stream A): Stream B :=
match s with x::s’ => f x::map A B f s’ end.
In this definition’s right-hand side the match construct and the expression f
x::... are in pre-guarded positions, the expression map A B f s’ is in guarded position, and the definition is guarded.

Example 3. The coinductive function nums takes as argument a natural number n and produces a stream of natural numbers starting from n.

CoFixpoint nums (n: nat): Stream nat := n::nums (S n).
In this definition’s right-hand side, the expression n::nums (S n) is in a pre-guarded position, the expression nums (S n) is in a guarded position.

Example 4. The following function zipWith is guarded:

CoFixpoint zipWith (A B C: Set)(f: A -> B -> C)
(s: Stream A)(t: Stream B) : Stream C :=
match (s, t) with (x :: s’, y :: t’) =>
(f x y):: (zipWith A B C f s’ t’)
end.
Informally speaking, the guardedness condition insures that

each corecursive call is made under at least one constructor; ** if the recursive call is under a constructor, it does not appear as an argument
of any function.
Violation of any of these two conditions makes a function non-guarded. Ac-cording to the two guardedness conditions above, we will be talking about the two classes of non-guarded functions - (*) and (**).
A more subtle analysis of the corecursive functions that fail to satisfy the guardedness condition * can be found in [14, 4, 21, 7]. In particular, the men-tioned papers offer a solution to the problem of formalising productive corecur-sive functions of this kind.
Till the rest of the paper, we shall restrict our attention to the second class of functions. To the extent of our knowledge, this paper is the first attempt to systematically formulate the functions of this class in the language of a higher-order proof assistant with guarded corecursion.

Example 5. Consider the following equation:

nats = 1::map S nats
This definition is not guarded, the expression map S nats occurs in a guarded position, but nats is not; see the guardedness condition **. Despite of this, the value nats is well-defined.

Example 6. The following definition describes the stream of Fibonacci numbers:

fib = 0 :: 1 :: (zipWith nat nat plus (tl fib) fib).
Again, this recursive equation fails to satisfy **.

Example 7. The next example shows the function dTimes that multiplies the sequences of derivatives in the elegant method of lazy differentiation of [19, 9].

dTimes x y = match x, y with
| x0 :: x’, y0 :: y’ =>
(x0 * y0) :: (zipWith Z Z plus (dTimes x’ y) (dTimes x y’))
end.
Again, this function fails to satisfy **.
In the next section, we will develop a method that makes it possible to express Examples 5 - 7 as guarded corecursive values.

Values in co-inductive types usually cannot be observed as a whole, because of their infiniteness. To prove some properties of infinite streams, we use a method of observation. For example, to prove that the two streams are bisimilar, we must observe that their first elements are the same, and continue the process with the rest.

Definition 4. Bisimilarity is expressed in the definition of the following coin-ductive type:

CoInductive EqSt: Stream A -> Stream A -> Prop :=
| eqst : forall (a : A) (s s’ : Stream A), EqSt s s’ ->
EqSt (a::s)(a::s’).

In the rest of this paper, we will write a==b for EqSt a b. The definition of a==b corresponds to the conventional notion of bisimilarity as given, e.g. in [18]. Lemmas and theorems analogous to the coinductive proof principle of [18] are proved in Coq and can be found in [5].

Bisimilarity expresses that two streams are observationally equal. Very often, we will only be able to prove this form of equality, but for most purposes this will be sufficient.
4 Soundness of recursive transformations for streams
In this section, we show that streams can be replaced by functions. Because there is a wide variety of techniques to define functions, this will make it possible to increase the class of streams we can reason about. Our approach will be to start with a (possibly non-guarded) recursive equation known to describe a stream, to transform it systematically into a recursive equation for a structurally recursive function, and then to transform this function back into a stream using a guarded corecursive scheme.
As a first step, we observe how to construct a stream from a function over natural numbers:

Definition 5. Given a function f over natural numbers, it can be transformed into a stream using the following function:

Cofixpoint stroff (A:Type)(f:nat->Type) : Stream A :=
f 0 :: stroff A (fun x => f (1+x)).
This definition is guarded by constructors. In the rest of this paper, we will write 〈s〉 for stroff s leaving the argument A to be inferred from the context.
The function stroff has a natural inverse, the function nth which returns the element of a stream at a given rank:

Definition 6. The function nth3 is defined as follows:

Fixpoint nth (A:Type) (n:nat) (s: Stream A) {struct n}: A :=
match s with a :: s’ =>
match n with | O => a | S p => nth A p s’ end
end.
In the rest of this paper, we will omit the first argument (the type argument) of nth, following Coq’s approach to implicit arguments. We will use notation JsK when talking about (fun n => nth n s).
It is easy to prove that J·K and 〈·〉 are inverse of each other. Composing these two functions is the essence of the method we develop here. The lemmas below are essential for guaranteeing the soundness of our method.
3 In Coq’s library, this function is defined under the name Str nth.

Lemma 1. For any function f over natural numbers, ∀n, nth n 〈f〉 = f n.

Lemma 2. For any stream s, s == 〈JsK〉.

Proof. Both proofs are done in Coq and available in [6].
We now want to describe a transformation for (non-guarded) recursive equa-tions for streams. A recursive equation for a stream would normally have the form
a = e (1)
where both a and e are streams, and a can also occur in the expression e; see Examples 5 - 7. We use this initial non-guarded equation to formulate a guarded equation for a of the form:
a = 〈e′〉 (2)
where e′ is a function extensionally equivalent to JeK. As we show later in this section, we often need to evaluate nth only partially or only at a certain depth, this is why the job cannot be fully delegated to nth.
The definition of e′ will have the form
e′ n = E (3)
where e′ can again occur in the expression E.

Example 8 (zeroes). For simple examples, we can go through steps (1)-(3) in-tuitively. Consider the corecursive guarded definition of a stream zeroes that contains an infinite repetition of 0.

CoFixpoint zeroes := 0 :: zeroes.
We can model the body of this corecursive definition as follows:
Fixpoint nzeroes (n:nat) : nat :=
match n with 0 => 0 | S p => nzeroes p end.
This is a legitimate structurally recursive definition for a function that maps any natural number to zero. Note that the obtained function is extensionally equal to JzeroesK.
Lemma nth_zeroes: forall n, nth n zeroes = nzeroes n.
Thus, a stream that is bisimilar to zeroes can be obtained by the following commands:
Definition zeroes’ := stroff _ nzeroes.
By Lemma nth zeroes and Lemma 2, zeroes and zeroes’ are bismilar, see [6] for a proof.
The main issue is to describe a systematic transformation from the expression e in the equation 1 to the expression E in the equation (3). This ”recursive” part of the work will be the main focus of the next section.
5 Recursive Analysis of Corecursive Functions
We continue to systematise the steps (1)-(3) of the transformation for a recursive equation a = e.
The expression e can be seen as the application of a function F to a. In this sense, the recursive definition of a expresses that a is fixpoint of F . The type of F is Stream A → Stream A for some type A. We will derive a new function F ′ of type (nat → A) → (nat → A); the recursive function a′ that we want to define is a fixed point of F ′. We obtain F ′ from F in two stages:
Step 1. We compose F on the left with 〈·〉 and on the right with J·K. This naturally yields a new function of the required type. In practice, we do not use an explicit composition function, but perform the syntactic replacement of the formal parameter with the 〈·〉 expression everywhere.

Example 9. For instance, when considering the zeroes example, the initial func-tion

Definition zeroes_F (zeroes:Stream nat) := 0::zeroes
is recursively transformed into the function:
Definition zeroes_F’ (nzeroes : nat -> nat) :=
nth n (0::stroff nzeroes).
The corecursive value we consider may be a function taking arguments in types t1, . . . , tn, that is, the function F may actually be defined as a function of type (t1 → · · · → tn → StreamA) → (t1 → · · · → tn → StreamA). The reformu-lated function F ′ that is obtained after composition with 〈·〉 and J·K has the corresponding type where Stream A is replaced with nat → A. Thus, it is the first argument that incurs a type modification. When one of the types ti is itself a stream type, we can choose to leave it as a stream type, or we can choose to replace it also with a function type. When replacing ti with a function type, we have to add compositions with J·K and 〈·〉 at all positions where the first argu-ment f of F is used, to express that the argument of f at the rank i must be converted from a stream type to a function type and at all positions where the argument of the rank i+ 1 of F is used, to express that this argument must be converted from a function type to a stream type.
We choose to perform this transformation of a stream argument into a func-tion argument only when the function being defined is later used for another recursive definition. In this paper, this happens only for the functions map and zipWith.

Example 10. Consider the function map from Example 2. The function F for this case has the following form:

Definition map_F
(map : forall (A B:Type)(f: A -> B), Stream A -> Stream B) :=
fun A B f s => match s with a::s’ => f a::map A B f s’ end.
The fourth argument to map and the fifth argument to map F have type Stream A
and we choose to replace this type with a function type. We obtain the following new function:
Definition map_F’
(map : forall (A B:Type)(f:A -> B), (nat -> A) -> nat -> B :=

[... content truncated ...]


## Related
- [[Core Ontology]]


- [[Axiomatic Collapse and Recursive Ontology]]

- [[Recursive Identity]]
- [[Agi Foundations]]


---

*Source: `Using Structural Recursion for Corecursion.pdf.md` | Ingested: 2026-05-11 | Ψ-tier: zero_divisor*
