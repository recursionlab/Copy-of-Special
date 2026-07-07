---
stub: true
title: "Full Iso Recursive Type.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Full Iso-recursive Type.pdf.md"]
psi_tier: unclassified
---

# Full Iso Recursive Type.Pdf

# Full Iso-recursive Type.pdf

111
Full Iso-recursive Types
LITAO ZHOU, The University of Hong Kong, China
QIANYONG WAN, The University of Hong Kong, China
BRUNO C. D. S. OLIVEIRA, The University of Hong Kong, China
There are twowell-known formulations of recursive types: iso-recursive and equi-recursive types. Abadi and Fiore
[1996] have shown that iso- and equi-recursive types have the same expressive power. However, their encod-
ing of equi-recursive types in terms of iso-recursive types requires explicit coercions. These coercions come
with significant additional computational overhead, and complicate reasoning about the equivalence of the
two formulations of recursive types.
This paper proposes a generalization of iso-recursive types called full iso-recursive types. Full iso-recursive
types allow encoding all programs with equi-recursive types without computational overhead. Instead of
explicit term coercions, all type transformations are captured by computationally irrelevant casts, which can
be erased at runtime without affecting the semantics of the program. Consequently, reasoning about the
equivalence between the two approaches can be greatly simplified. We present a calculus called _
8 , which extends the simply typed lambda calculus (STLC) with full iso-recursive types. The _

8 calculus is proved to
be type sound, and shown to have the same expressive power as a calculus with equi-recursive types. We
also extend our results to subtyping, and show that equi-recursive subtyping can be expressed in terms of
iso-recursive subtyping with cast operators.
CCS Concepts: • Theory of computation → Type theory; • Software and its engineering → Object
oriented languages.
Additional Key Words and Phrases: Recursive types, Subtyping, Type system
ACM Reference Format:
Litao Zhou, QianyongWan, and BrunoC. d. S. Oliveira. 2018. Full Iso-recursive Types. J. ACM 37, 4, Article 111
(August 2018), 25 pages.
https://doi.org/XXXXXXX.XXXXXXX

1 INTRODUCTION
Recursive types are used in many programming languages to express recursive data structures, or recursive interfaces. There are two well-known formulations of recursive types: iso-recursive and equi-recursive types. With equi-recursive types [Morris 1968], a recursive type
U.  and its un-folding [U ↦→
U. ] are equal, since they represent the same infinite tree [Amadio and Cardelli 1993]. With iso-recursive types, a recursive type is only isomorphic to its unfolding [Crary et al. 1999]. To witness the isomorphism, explicit fold and unfold operators are used.
Because both formulations provide alternative ways to model recursive types, the relationship between iso- and equi-recursive types has been a topic of study [Abadi and Fiore 1996; Patrignani et al. 2021; Urzyczyn 1995]. Understanding this relationship is important to answer questions such as
Authors’ addresses: Litao Zhou,
ltzhou@cs.hku.hk
, The University of Hong Kong, Pokfulam Road, Hong Kong, China;
Qianyong Wan, The University of Hong Kong, Pokfulam Road, Hong Kong, China,
qywan@cs.hku.hk
; Bruno C. d. S.
Oliveira, The University of Hong Kong, Pokfulam Road, Hong Kong, China,
bruno@cs.hku.hk
.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be
honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists,
requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org
.
© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
0004-5411/2018/8-ART111 $15.00

https://doi.org/XXXXXXX.XXXXXXX

J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:2 Litao Zhou, Qianyong Wan, and Bruno C. d. S. Oliveira
whether the expressive power of the two formulations is the same or not. Urzyczyn proved that these two formulations have the same expressive powerwhen the types considered are restricted to be positive. Abadi and Fiore extended Urzyczyn’s result and showed that unrestricted formulations of iso- and equi-recursive types also have the same expressive power, leading to the well-known statement that “iso-recursive types have the same expressive power as equi-recursive types”. In addition, Patrignani et al. showed that the translation from iso-recursive to equi-recursive types is fully abstract with respect to contextual equivalence. However, the encoding proposed by Abadi and Fiore requires explicit coercions, which are inter-
preted as functions to be evaluated at runtime. Iso-recursive types can only encode equi-recursive types with significant additional computational overhead. Moreover, these explicit coercions can-not be easily erased and therefore complicate the reasoning about behavioral equivalence. To ad-dress the latter challenge, Abadi and Fiore defined an axiomatized program logic and showed that the iso-recursive term obtained by their encoding behaves in the same way as the original equi-recursive term in the logic. However, the soundness of their program logic is left as a conjecture, since they did not consider an operational semantics in their work. Thus, behavioral equivalence between programs written with equi-recursive and iso-recursive types lacks a complete proof in the literature. Without introducing explicit coercions, iso-recursive types are strictly weaker than equi-recursive types, since the infinite tree view of equi-recursive types equates more types than isomorphic unfoldings of recursive types. This paper proposes a generalization of iso-recursive types called full iso-recursive types. Full
iso-recursive types overcome the challenges of traditional iso-recursive types in achieving the typing expressiveness and behavioral equivalence seen in equi-recursive types. Instead of fold and unfold operators and explicit coercions, we use amore general notion of computationally irrelevant cast operators [Cretin 2014; Sulzmann et al. 2007], which allow transformations on any types that are equivalent in an equi-recursive setting. Full iso-recursive types can encode all programs with equi-recursive typeswithout computational overhead, since casts can be erased at runtime without affecting the semantics of the program. Consequently, the semantic equivalence between programs written with equi-recursive and full iso-recursive types is also greatly simplified, and allows for a complete proof, compared to Abadi and Fiore’s work. We present a calculus called _

8 , which extends the simply typed lambda calculus (STLC) with full iso-recursive types. The _

8 calculus is proved to be type sound, and shown to have the same
typing power as a calculus with equi-recursive types. To prove the latter result, we define a type-directed elaboration from the calculus with equi-recursive types to _

8 , and an erasure function that removes all casts from full iso-recursive terms to obtain equi-recursive terms. Moreover, the termination and divergence behavior of programs is preserved under the elaboration and erasure operations. Therefore, _

8 is sound and complete w.r.t. the calculus with equi-recursive types in
terms of both typing and dynamic semantics. On the other hand, traditional iso-recursive types can be seen as a special case of full iso-recursive types. One can easily recover the traditional unfold and fold operators by using the corresponding cast operators accordingly. So all the results for iso-recursive types can be adapted to full iso-recursive types as well. We also extend our results to subtyping and show that equi-recursive subtyping can be ex-
pressed in terms of iso-recursive subtyping with cast operators. Although subtyping between equi-recursive types [Amadio and Cardelli 1993; Brandt and Henglein 1998; Gapeyev et al. 2002] and subtyping between iso-recursive types [Abadi and Cardelli 1996; Zhou et al. 2022] has been studied in depth respectively in the literature, the relationship between the two approaches has been largely unexplored. We revisit Amadio and Cardelli [1993]’s seminal work on equi-recursive
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Full Iso-recursive Types 111:3
subtyping and observe that an equi-recursive subtyping relation can be decomposed into a combi-nation of equi-recursive equalities and an iso-recursive subtyping relation. Since our cast operators can capture all the equi-recursive equalities, we can achieve a simple encoding of equi-recursive subtyping in the setting of full iso-recursive types with subtyping. Full iso-recursive types open the path for new applications. For example, in the design of re-
alistic compilers, it is common to have source languages that are lightweight in terms of type annotations; and target languages, which are used internally, that are heavy on annotations, but are simple to type-check. For instance, the GHC Haskell compiler works in this way: the source language (Haskell) has a lot of convenience via type inference, and no explicit casts are needed in source programs. A source program is then elaborated to a variant of System Fc [Sulzmann et al. 2007], which is a System F like language with explicit type annotations, type applications and also explicit casts. Our work enables designing source languages with equi-recursive types, which are elaborated to target languages with full iso-recursive types. Equi-recursive types offer con-venience because they can avoid explicit folds and unfolds, but type-checking is complex. With full iso-recursive types we need to write explicit casts, but type-checking is simple. Thus we can have an architecture similar to that of GHC. In this scenario it is important that no computational overhead is introduced during the elaboration, which is why using standard iso-recursive types would not be practical. In addition, source languages could also hide explicit casts into language constructs (such as constructors, method calls and/or pattern matching). This would be another way to use full iso-recursive types, which is similar to current applications of iso-recursive types.
The main contributions of this paper are as follows:

Full iso-recursive types.We propose a novel formulation of recursive types, called full iso-recursive types, which generalizes the traditional iso-recursive fold and unfold operators to cast operators.

The _
8 calculus. We introduce the _

8 calculus, which extends the simply typed lambda
calculus with full iso-recursive types. The calculus is equipped with a type system, a call-by-value operational semantics, and a type soundness proof.

Equivalence to equi-recursive types. We show that _ `
8 is equivalent to STLC extended
with equi-recursive types in terms of typing and dynamic semantics.

Extension to subtyping.We present _
<: 8 , an extension of _

8 with iso-recursive subtyping,
and show the same metatheory results for _ `<:
8 , namely, type soundness, typing equivalence
and behavioral equivalence to equi-recursive types with subtyping.

Coq formalization. We provide a mechanical formalization and proofs for all the new metatheory results of full iso-recursive types in Coq, except for Theorem5.5, which is adapted from the literature [Amadio and Cardelli 1993].
2 OVERVIEW
This section provides an overview of our work. We first briefly review the two main approaches to recursive types, namely iso-recursive types and equi-recursive types, and the relationship between the two approaches. Then we introduce our key ideas and results.
2.1 Equi-recursive Types
Equi-recursive types treat recursive types and their unfoldings as equal. The advantage of equi-recursive types is that they are simple to use, since there is no need to insert explicit annotations
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:4 Litao Zhou, Qianyong Wan, and Bruno C. d. S. Oliveira
   (Equi-recursive Equality)
Tyeq-contract
[U ↦→ 1]  1 [U ↦→ 2]  2  is contractive in U
1  2
Tyeq-unfold

U.   [U ↦→
U. ]
Tyeq-mu-cong
  

U.  
U. 
Tyeq-trans
     
  
Tyeq-refl
  
Tyeq-symm
  
  
Tyeq-arr
1  2 1  2
1 → 1  2 → 2
Fig. 1. Amadio and Cardelli’s equi-recursive type equality.
in the term language to transform between equal types, as shown in rule Typ-eq.
Typ-eq
Γ ⊢ 4 :    
Γ ⊢ 4 : 
Themetatheory of equi-recursive types has been comprehensively studied byAmadio and Cardelli [1993]. They proposed a tree model for specifying equality (or subtyping) between equi-recursive types. In essence, two recursive types are equal (or subtypes) if their infinite unfoldings are equal (or in a subtyping relation). The tree model provides a clear and solid foundation for the interpre-tation of equi-recursive types. Amadio and Cardelli also provided a rule-based axiomatization to compare equi-recursive types,
as shown in Figure 1. They proved the soundness and completeness of the rules to the tree-based interpretation. For example, rule Tyeq-unfold states that a recursive type is equal to its unfolding, and rule Tyeq-mu-cong states that the equality is congruent with respect to the recursive type operator. Rule Tyeq-contract states that two types are equal if they are the fixpoints of the same type function [U]. Note that  needs to be contractive in U , i.e. either U is not free in  or  can be unfolded to a type of the form 1 → 2. This is to prevent equating arbitrary types using non-contractive type functions, such as when  is U . Rule Tyeq-contract allows recursive types that have equal infinite unfoldings, but are not directly related by finite unfoldings, to be equal. For example, let [U] = Int → Int → U , then 1 =
U.Int → U and 2 =
U.Int → Int → U
are equal according to rule Tyeq-contract:
. . . 1  [U ↦→ 1]
Tyeq-unfold 2  [U ↦→ 2]  is contractive in U
Tyeq-contract
U.Int → U 
U.Int → Int → U
Here, the missing derivation is:
Tyeq-refl Int  Int
Tyeq-unfold
U. Int → U  Int →
U. Int → U
Tyeq-arrow Int → 1  Int → Int → 1
Tyeq-trans and Tyeq-unfold 1  [U ↦→ 1]
Despite its equivalence to the tree model, Amadio and Cardelli’s axiomatization is not easy to use in practice. In particular one needs to find a generating type function[U] in ruleTyeq-contract. Later on, there have been a few alternative axiomatizations of equi-recursive types [Brandt and Henglein 1998; Danielsson and Altenkirch 2010; Gapeyev et al. 2002], which are all proved to be equivalent to the tree model. Among them, Brandt and Henglein proposed an inductively defined relation
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Full Iso-recursive Types 111:5
⊢    (Inductive Equi-recursive Equality)
Tye-assump
 =  ∈
⊢   
Tye-refl
⊢   
Tye-trans
⊢     ⊢   
⊢   
Tye-unfold
⊢
U.   [U ↦→
U. ]
Tye-symm
⊢   
⊢   
Tye-arrfix
,1 → 1 = 2 → 2 ⊢ 1  2 ,1 → 1 = 2 → 2 ⊢ 1  2
⊢ 1 → 1  2 → 2
Fig. 2. Brandt and Henglein’s inductively defined equi-recursive type equality.
⊢    for equi-recursive type equality, shown in Figure 2.  is a list of type equality assump-tions that can be used to derive the equality   . New equalities are added to  every time function types are compared, as shown in rule Tye-arrfix. Compared to rule Tyeq-contract, rule Tye-arrfix encodes the coinductive essence of equi-recursive types in a simpler way. There-fore, we choose Brandt and Henglein’s axiomatization as the basis for our work.
2.2 Iso-recursive Types
Iso-recursive types [Crary et al. 1999] are a different approach that treats recursive types and their unfoldings as different, but isomorphic up to an unfold/fold operator. With iso-recursive types foldings and unfoldings of the recursive types must be explicitly triggered, and there is no typing rule Typ-eq to implicitly convert between equivalent types. Rule Typ-unfold and rule Typ-fold show the typing rules for unfolding and folding a term of recursive types. A fold expression con-structs a recursive type, while an unfold expression opens a recursive type to its unfolding.
Typ-unfold
Γ ⊢ 4 :
U.  Γ ⊢ unfold [
U. ] 4 : [U ↦→
U. ] Typ-fold Γ ⊢ 4 : [U ↦→
U. ]
Γ ⊢ fold [
U. ] 4 :
U. 
One advantage of iso-recursive types is that they are easier to extend to more complex type sys-tems, which may easily make the type equality relation undecidable. Instead, iso-recursive types provide explicit control over folding and unfolding, avoiding issues with undecidability. One disad-vantage of iso-recursive types is their inconvenience in use due to the explicit fold and unfold op-erators. However, this disadvantage can be mitigated by hiding folding and unfolding under other language constructs, such as pattern matching, constructors or method calls [Crary et al. 1999; Harper and Stone 2000; Lee et al. 2015; Pierce 2002; Vanderwaart et al. 2003; Yang and Oliveira 2019; Zhou et al. 2022]. As we shall see in Section 2.3, a further disadvantage of iso-recursive types is that folding and unfolding alone is not enough to provide all of the expressive power of the type equality rules. In some cases, explicit, computationally relevant, term coercions are necessary.
2.3 Relating Iso-recursive and Equi-recursive Types
The relationship between iso-recursive types and equi-recursive types has been a subject of study for a long time on the literature of recursive types [Abadi and Fiore 1996; Patrignani et al. 2021; Urzyczyn 1995]. This subsection reviews the existing approaches to relate the two approaches and their issues.
Encoding iso-recursive types. The encoding of iso-recursive types in equi-recursive types is straight-forward, simply by erasing the fold and unfold operators [Abadi and Fiore 1996]. Since the ruleTyeq-unfold
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:6 Litao Zhou, Qianyong Wan, and Bruno C. d. S. Oliveira
states that a recursive type is equal to its unfolding, it is easy to see that the encoding is type pre-serving. The encoding is also behavior preserving, since the reduction rules with fold and unfold operators will become no-ops when erased, as shown below:
Red-fld
4 ↩→ 4′
fold [] 4 ↩→ fold [] 4′
Red-ufd
4 ↩→ 4′
unfold [] 4 ↩→ unfold [] 4′

[... content truncated ...]

---

*Source: `Full Iso-recursive Type.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
