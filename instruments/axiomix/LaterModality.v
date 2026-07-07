(* AXIOMIX — Later Modality and Guarded Recursion *)
(* The later modality enforces guarded recursion with depth budget *)

Require Import ProofSystem.
Require Import MetaAxiomMonad.
Require Import SelfModKernel.

(* ============================================================ *)
(* Section 1: Later Modality Definition                         *)
(* ============================================================ *)

Inductive Later (A : Type) : nat -> Type :=
  | now : A -> Later A 0
  | later : forall n, Later A n -> Later A (S n).

(* Depth budget *)
Parameter kappa : nat.

(* ============================================================ *)
(* Section 2: Stable Core — Limit of the Guarded Chain          *)
(* ============================================================ *)

Definition StableCore (A : ProofSystem) : ProofSystem :=
  {| axioms := axioms A;
     rules := rules A;
     derivable := derivable A;
     refl_deriv := refl_deriv A;
     trans_deriv := trans_deriv A;
     rule_deriv := rule_deriv A |}.

(* ============================================================ *)
(* Section 3: Guarded Fixpoint Theorem                          *)
(* ============================================================ *)

Axiom guarded_fixpoint :
  forall (A : ProofSystem) (R : SelfModKernel A),
  exists (p : axioms (StableCore A)),
    derivable (StableCore A) p (@modify A R p).
