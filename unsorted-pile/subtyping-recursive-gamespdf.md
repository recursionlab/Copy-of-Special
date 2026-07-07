---
title: "Subtyping Recursive Games.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Subtyping Recursive Games.pdf.md"]
psi_tier: unclassified
---
stub: true

# Subtyping Recursive Games.Pdf

# Subtyping Recursive Games.pdf

Subtyping Recursive Games

Juliusz Chroboczek
Université de Paris VII Paris, France
Abstract. Using methods drawn from Game Semantics, we build a sound and computationally adequate model of a simple calculus that includes both subtyping and recursive types. Our model solves recursive type equations up to equality, and is shown to validate a subtyping rule for recursive types proposed by Amadio and Cardelli.
Introduction
Subtyping is an ordering relation over types that is an essential feature of a wide range of programming languages. While at first order subtyping corresponds to inclusion of the carriers, there is no simple set-theoretic interpretation of subtyping at higher order.
Many programming languages also include recursive types — types that are defined implicitly, as fixpoints of maps over types. The interaction of recur-sive types with subtyping has been studied before [4], and shown to present a number of interesting challenges. While both are important features of many programming languages, there are only few interpretations that satisfactorily model both.
Game Semantics is a framework for modelling programming languages that combines the elegant mathematical structure of Denotational Semantics with explicitly operational notions. Due to the blend of the two, Game Semantics has been successful at modelling a wide range of programming language features. In a previous work [7], we have shown how the simple feature of adding explicit error elements to Game Semantics allows us to model subtyping; in this paper, we extend this model to include recursive types, and show that it validates the subtyping rule for recursive types proposed by Amadio and Cardelli [4].
There are two main new results in this paper. First, we show how a minor modification of the operational semantics of the untyped model presented in an earlier makes the model computationally adequate (Sections 1.1 and 2.2), thus solving the main open problem in our previous paper [7]. Second, we show how the space of games, used for modelling types, can be equipped with a metric that allows us to construct recursive types; the metric is shown to interact with the order structure related to subtyping so as to validate the desired subtyping rules (Sections 4 and 5).

1 A λ-calculus with errors

We consider an untyped λ-calculus with ground values, defined by the following syntax:

M, N, N ′ ::= x | λx.M | (M N) | (M, N) | πl(M) | πr(M) | tt | f f | top | if M then N else N ′ fi.

The only unusual feature of this calculus is the presence of a ground value top that will be used for representing the result of badly-typed terms.

Our calculus may be equipped with an operational semantics e.g. by defining a one step reduction relation on terms. For our calculus, a common choice — the call-by-name semantics — consists of the rules

((λx.M) N) M [x\N ]

πl((M, N)) M πr((M, N)) N

if tt then N else N ′ fi N if f f then N else N ′ fi N ′

M  M ′

E[M ] E[M ′]

where the set of evaluation contexts E[·] is defined by

E[·] ::= ([·] N) | πl([·]) | πr([·]) | if [·] then N else N ′ fi.

In general, we will be interested in computations that take more than one step. The reduction relation  ∗ is the transitive reflexive closure of  .

We say that a term M reduces to value V , written M ↓ V , if M  ∗ V where V is a value. We write M ↓ when there exists a value V such that M ↓ V , and M ↑ otherwise.

1.1 Errors in the calculus

The relation ↓ is not total; a number of terms do not reduce to values. This is expected, as we have done nothing whatsoever to prevent the formation of meaningless terms.

Let δ be the term λx.(x x). The term (δ δ) does not reduce to a value; (δ δ) leads to an infinite sequence of one-step reductions:

(δ δ) (δ δ) (δ δ) · · · A very different example of a term that fails to reduce to a value is

M = if λx.x then tt else ff fi

In this case, small-step semantics shows that the reduction remains “stuck” at a non-value term: there is no M ′ such that M  M ′. In our view, this situation

corresponds to a runtime error — an exceptional situation detected during the reduction of a term. As our calculus contains no constructs that allow us to handle (“trap”) such errors, we shall use the term untrappable error.

We will use the term top to represent untrappable errors. Intuitively, a term should reduce to top whenever its reduction gets “stuck” with no applicable rule; unfortunately, such a simple extension does not quite work. Indeed, consider the “identity on the Booleans” IBool = λx.if x then tt else ff fi; this term behaves as the identity when applied to a Boolean, but returns an error when applied to a function or a pair. Let now Y be a fixpoint combinator, and consider the “looping Boolean” (Y IBool); intuitively, we would expect this term to loop when invoked in a Boolean context, but return an error when e.g. applied. The reduction relation ↓, augmented as suggested above, causes it to loop (this problem is expressed technically by the failure of computational adequacy of our model w.r.t. ↓ [7, Section 2.3]).

We therefore define a different reduction relation, written ⇓, which is ex-plicitly decorated with the locus of the computation. To do so, we introduce a notion of initial component, a finite sequence over {1, l, r} (the empty sequence is written ε). Walking the syntax tree of a type, computation happening on the right-hand-side of an arrow is marked by 1; computation happening on the left-hand-side (resp. right-hand-side) of a product is marked by l (resp. r). A family of reduction relations, indexed by initial components, is defined in Fig. 1.

As usual, we write M ⇑c when there is no V such that M ⇓c V . We write ε for the empty component, and |c| for the length of component c.

To clarify this definition, note that the form of a value resulting from reduc-tion at initial component c is determined by c. More precisely, if M is a closed term and c an initial component such that M ⇓c V , then one of the following is true:

– V = top; or – c = ε and V = f f or V = tt; or – c is of the form 1 · c′ and V is of the form λx.M ′; or – c is of the form l · c′ or r · c′, and V is of the form (N, P ).

Conversely,

– if (M, N) ⇓c P , then either c is of the form l · c′ or r · c′, or P = top; – if λx.M ⇓c N , then either c is of the form 1 · c′ or N = top; – tt ⇓c N or f f ⇓c N , then either c = ε or N = top.

There is also a simple relationship between ⇓ and the simple reduction re-lation ↓; it shows that the extension that we introduce only concerns erroneous reductions. Roughly speaking, the relations ⇓ and ↓ coincide, except in the case in which ⇓ yields an untrappable error and ↓ diverges. More precisely, M ↓ V implies that for some initial component c, M ⇓c V . Conversely, M ↑ implies that for all c, either M ⇑c or M ⇓c top. Finally, if for some c, M ⇑c, then M ↑.

tt ⇓ε tt ff ⇓ε ff tt ⇓c top (c 6= ε) ff ⇓c top (c 6= ε)

λx.M ⇓1·c λx.M λx.M ⇓c top (c 6= 1 · c′)

(M, N) ⇓l·c (M,N) (M, N) ⇓r·c (M, N) (M, N) ⇓c top (c = ε or c = 1 · c′)

M ⇓1·c λx.M ′ M ′[x\N ] ⇓c P

(M N) ⇓c P

M ⇓1·c top

(M N) ⇓c top

M ⇓l·c (N, P ) N ⇓c N ′

πl(M) ⇓c N ′ M ⇓r·c (N, P ) P ⇓c P ′

πr(M) ⇓c P ′

M ⇓l·c top

πl(M) ⇓c top

M ⇓r·c top

πr(M) ⇓c top

M ⇓ε tt N ⇓ε N ′

if M then N else P fi ⇓ε N ′

M ⇓ε ff P ⇓ε P ′

if M then N else P fi ⇓ε P ′

M ⇓ε top

if M then N else P fi ⇓ε top if M then N else P fi ⇓c top (c 6= ε)

Fig. 1. Big-step semantics with errors and initial components

1.2 Errors and denotational semantics

It is not immediately obvious how to model errors in Denotational Semantics. Consider for example the domain of Booleans. One choice would be to add an error value error “on the side” (Fig. 2(a)); another one would be to add a value top as a top element (Fig. 2(b)).

It is our view that errors on the side model (trappable) exceptions, while errors at top model untrappable errors. Consider, indeed, the addition to our calculus of a term ignore-errors that would satisfy

ignore-errors tt ⇓ε tt

ignore-errors ff ⇓ε tt ignore-errors top ⇓ε f f

Denotationally, such a term would have to map tt to tt while mapping top to f f , which would be a non-monotone semantics. On the other hand, modelling an analogous term using error instead of top would cause no problem at all.

tt ff error

⊥
@@@@@@@@

mmmmmmmmmmmmmmm
(a)
top
{{ {{
{{ {{
CC CC
CC CC
**tt ff**
⊥
CCCCCCCC
{{{{{{{{
(b)
**Fig. 2. Two domains of Booleans with errors**
Errors “on the side,” or exceptions, have been studied before [6]; in this paper, we adopt the domain in Fig. 2(b).
The addition of a top value to Scott domains was a common feature of early Denotational Semantics. However, this value does not seem to be used for modelling anything, but is just added to domains in order to turn them into complete lattices.
**1.3 Observational preorder**
***In order to complete the definition of the semantics of our calculus, we need to introduce a notion of equivalence of terms. This is usually done by defining a set of observations, which is then used to define a congruent preorder on terms known as the observational preorder. We choose our set of observations to consist of the observations “reduction to top at ε,” “reduction to tt at ε” and “reduction to f f at ε,” ordered analogously to Fig. 2(b).***
***Definition 1. (Observational preorder)***
*M . N iff ∀C[·]  *
***C[M ] ⇓ε top ⇒ C[N ] ⇓ε top; C[M ] ⇓ε tt ⇒ C[N ] ⇓ε tt or C[N ] ⇓ε top; C[M ] ⇓ε f f ⇒ C[N ] ⇓ε f f or C[N ] ⇓ε top.***
*We say that two terms M and N are observationally equivalent, and write M ∼= N , when M . N and N .M .*
***As usual in calculi with ground values, the observational preorder can be defined by just one well-chosen observation; one possible choice is reduction to top at ε.***
***Lemma 2. M . N if and only if***
***∀C[·] C[M ] ⇓ε top ⇒ C[N ] ⇓ε top.***
Informally, this lemma says that terms are equivalent if and only if they generate errors in the same set of contexts.
*It is worthwhile to compare our calculus with Abramsky’s lazy λ-calculus [1]. Writing Ω for the looping term (e.g. Ω = ((λx.(x x)) λx.(x x))), notice that Ω and λx.Ω are observationally distinct. Indeed, taking*
***C[·] = if · then tt else ff fi***
***we have C[Ω] ⇑ε, while C[λx.Ω] ⇓ε top. On the other hand, as we shall see in Section 2, we introduce no explicit lifting in a sound and computationally adequate model. Thus, we believe that our calculus combines the most desirable characteristics of what Abramsky calls the standard interpretation of the λ-calculus with those of the lazy calculus. The fundamentally call-by-name nature of the construction is reflected in the syntax by the fact that the terms top and λx.top are observationally equivalent (see the end of Section 2.2).***
**2 A game semantics for the untyped calculus**
This section roughly outlines the semantic framework used for modelling untyped terms. As Game Semantics has been described before [2, 11], and so has our particular framework [7, 8], this section remains informal.
*In Game Semantics, a term is represented by a strategy, the set of its be-haviours in all possible contexts. A behaviour is modelled as a play between two players, Player, who represents the term under consideration, and Opponent, who represents its environment (the context it is in). The two players exchange tokens of information known as moves — one may think of these as (visible) actions in process calculi, or messages in message-passing object-oriented lan-guages. By convention, Opponent plays first when modelling a call-by-name calculus.*
***Moves are structured into components which correspond to paths in the syn-tax tree of a type. For example, a strategy corresponding to a term of type Bool → Bool exchanges moves in components 0 (the left-hand-side of the ar-row) and 1. Precisely, a move is of the form mc, where m is one of q, the question, att, the answer true, or aff , the answer false, and c, the component of the move, is a finite string over 0, 1, l, r. In addition, moves are decorated with justification pointers which, while absolutely necessary for the correction of the interpreta-tion, are not essential for the ideas in this paper.***
*A position is an alternating sequence of moves — odd-ordered moves played by Opponent, even-ordered ones by Player. A strategy is a set of positions that specify the moves played by Player in response to a given sequence of moves from Opponent.*
The main novelty of the formalism used in this work and introduced in [8, 7] is that we allow strategies to refuse moves, which is used for modelling untrappable errors. Concretely, this is realised by allowing strategies to contain both even- and odd-length positions. In a spirit similar to that of Harmer [9, Chapter 4], even-length positions represent moves that are played by Player, while odd-length positions represent situations in which player loops.
***Definition 3. A set s of positions is***
***– prefix-closed if p · q ∈ s implies p ∈ s for any positions p and q; – even-prefix-closed if p · q ∈ s and |p| even imply p ∈ s for any positions p***
***and q; – deterministic if for any position p ∈ s, if |p| is odd then, for any moves m***
*and n,*
*   *p · m ∈ s and p · n ∈ s imply m = n; and*
*   *p · m ∈ s implies p 6∈ s.*
*A strategy is a non-empty even-prefix-closed deterministic set of positions.*
*For any collection of positions A, we write Pref A for the prefix completion of A. The even-prefix-closedness condition in this definition says that a strategy*
*cannot mandate that Opponent should play at a given position: a strategy must allow for the situation in which Opponent never plays a move. As to the deter-minacy condition, it states that a strategy cannot mandate either playing two distinct moves or both playing and not playing a move at a given position. Taken together, even-prefix-closedness and determinacy imply that an odd-length po-sition in a strategy cannot be extended (i.e. if p ∈ s and |p| is odd, then no p · q is in s): once a strategy has refused to play a move, the play will not proceed further.*
***In [7], we define a certain number of strategies. The strategy top consists of the single empty position ε; this strategy never accepts an Opponent’s move. The strategy Ω consists of all positions of length 1; thus, it always accepts an initial move from Opponent, but never plays a move. The strategy tt consists of all even-length positions composed of alternations of the moves q and att; thus, it always accepts an initial question, and replies with the answer true (f f is analogous).***
***The class of strategies that copy moves between components are known as the copy-cat strategies; this class includes the identity I, the projections πr and πl, and, to a certain extent, the “if-then-else” strategy ite. In addition, we use a number of operations on strategies, including (functional) pairing 〈·, ·〉, currying Λ(·), as well as the injection K(·) which “shifts” a strategy into component 1.***
*Composition of strategies s and t is performed by ranging over all behaviours in s and t, selecting those that are agree on a common component, and composing them, similarly to Baillot et al. [5]. However, we cannot just use their formalism, as we need to take into account livelock, or infinite chattering, the situation in which two strategies never disagree but never have positions that coincide. Indeed, suppose that when composing s with t, after the initial move is played in component 1 of t, both t and s keep playing in the common component. In this case, the two strategies would never ultimately reach agreement, and yet neither would ever play a move that is not accepted by the other.*
***Definition 4. Given a natural integer n, we say that two positions p and q agree at depth n if p and q only contain moves within components 1 and 0, and the prefix of length n of p  1 is equal to the prefix of same length of q  0 (or p  1 = q  0 if both projections are of length smaller than n).***
*Given two strategies s and t, the strategy s; t is the set of all positions p such that for any natural integer n, there exist positions q ∈ s and q′ ∈ t such that q and q′ agree at depth n, q  0 = p  0 and q′  1 = p  1.*
**2.1 The liveness ordering**
*We now introduce an ordering — the liveness ordering 4 — which will model the observational preorder, the typing relation, and the subtyping relation (Lem-mata 10 and 21 and Theorem 22), and is inspired by Abramsky’s “back-and-forth inclusion relation” [2]. The definition of the liveness ordering is analogous to that of the observational preorder. Just like for terms M and N we have M . N when M produces errors in less contexts than N , and N produces results in more con-texts than M (Definition 1), we will want strategies s and t to satisfy s 4 t if and only if s accepts more positions and produces less positions than t when playing against any given opponent. We define 4 on prefix-closed sets of positions, and deduce a suitable definition for strategies from that.*
*For any non-empty position p, we write p−1 for the prefix of p of length |p|−1 (i.e. p without its last move).*
***Definition 5. Given non-empty prefix-closed sets of positions A and B, we say that B is more live than A, or A is safer than B, and write A 4 B, if***
***– for every position of odd length q ∈ B, if q−1 ∈ A then q ∈ A; and – for every position of even length p ∈ A (p 6= ε), if p−1 ∈ B, then p ∈ B.***
*The definition of 4 may be paraphrased as follows. Given a prefix-closed collec-tion of positions A, a position p is said to be reachable at A if p−1 ∈ A or p = ε. In order to have A 4 B, the set of odd-length positions (positions ending in an Opponent’s move) in A that are reachable at A needs to be a superset of the set of odd-length positions in B; and, dually, the set of even-length positions in B that are reachable at B should be a superset of the even-length positions in A. A clarification of the intuitions behind the liveness ordering may be found in [8, 7].*
***Theorem 6. The relation 4 is a partial order on non-empty prefix-closed col-lections of positions.***
*The definition of 4 above does not yield a transitive or antireflexive relation on arbitrary sets of positions. We may, however, extend 4 to all non-empty sets of positions by writing A 4 B whenever Pref(A) 4 Pref(B); while this only makes 4 into a preorder on arbitrary sets of positions, it does actually make it into a partial order on strategies.*
***Lemma 7. If s and t are strategies, then Pref(s) = Pref(t) implies s = t. The relation 4 is therefore a partial order on strategies.***
This property does depend on the fact that we have restricted ourselves to deterministic strategies.
**2.2 Interpretation of the calculus**
*We interpret a couple Γ ` M , where Γ is an (ordered) list of variables, and M a term such that FV(M) ⊆ Γ . The interpretation is defined as follows.*
***[[x ` x]] = I [[Γ ` λx.M ]] = Λ([[Γ, x ` M ]])***
***[[Γ, x ` x]] = πr [[Γ ` (M N)]] = 〈[[Γ ` M ]], [[Γ ` N ]]〉; eval [[Γ, y ` x]] = πl; [[Γ ` x]] [[Γ ` (M, N)]] = 〈[[Γ ` M ]], [[Γ ` N ]]〉 [[Γ ` tt]] = K(tt) [[Γ ` πl(M)]] = [[Γ ` M ]]; πl***
***[[Γ ` f f ]] = K(f f) [[Γ ` πr(M)]] = [[Γ ` M ]]; πr***
***[[Γ ` top]] = top Γ ` if M then N else N ′ fi = = 〈[[Γ ` M ]], 〈[[Γ ` N ]], [[Γ ` N ′]]〉〉; ite***
*The notion of soundness that we use is somewhat complicated by the fact that we use a family of reduction relations. Given a component c, we say that two strategies s and t are equal at component c, and write s =c t, when the sets of positions starting with qc in s and t coincide.*
***Lemma 8. (Equational Soundness) If [[Γ ` M ]] is defined and M ⇓c N , then [[Γ ` N ]] is defined and [[Γ ` N ]] =1·c [[Γ ` M ]].***
The interpretation is also computationally adequate.
***Lemma 9. (Computational Adequacy) If [[Γ ` M ]] is defined and there is no term N such that M ⇓ε N , then [[Γ ` M ]] =1 ⊥.***
*In order to prove this property, we use a variant of Plotkin’s method of formal approximation relations. We say that a family /c of relations between strategies and terms, indexed by initial components, is a family of formal approximation relations when it satisfies a number of fairly natural properties that imply in particular that s /ε M implies s =1 ⊥ or M ⇓ε. We then show the existence of such a family, and that for any closed term M and initial component c, [[Γ ` M ]] /c M , which allows us to conclude by a standard argument.*
Soundness, computational adequacy and Lemma 2 imply inequational sound-ness.

[... content truncated ...]

---

*Source: `Subtyping Recursive Games.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
