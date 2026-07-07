(* AXIOMIX — Self-Modification Kernel R *)
(* The operator that rewrites a proof system's axioms *)

Require Import ProofSystem.
Require Import MetaAxiomMonad.

(* ============================================================ *)
(* Section 1: SelfModKernel Definition                          *)
(* ============================================================ *)

Record SelfModKernel (A : ProofSystem) := {
  modify : axioms A -> axioms A ;
  consistency_preserving : forall p,
    derivable A p p -> derivable A (modify p) (modify p) ;
  guarded : forall p,
    derivable A p p -> derivable A p (modify p)
}.

(* ============================================================ *)
(* Section 2: Distributive Law (Axiom)                          *)
(* Meta-rewriting and self-rewriting commute: lambda: M R = R M  *)
(* ============================================================ *)

Axiom distributive_law :
  forall (A : ProofSystem) (R : SelfModKernel A)
    (p q : axioms A) (H : rules A p q),
  rules A (@modify A R p) (@modify A R q).

Axiom distributive_law_deriv :
  forall (A : ProofSystem) (R : SelfModKernel A)
    (p q : axioms A) (H : derivable A p q),
  derivable A (@modify A R p) (@modify A R q).
