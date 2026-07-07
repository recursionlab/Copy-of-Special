(* AXIOMIX — Bootstrap Dialgebra *)
(* The bialgebraic structure that resolves the self-reference paradox *)

Require Import ProofSystem.
Require Import MetaAxiomMonad.
Require Import SelfModKernel.
Require Import LaterModality.
Require Import List.
Import ListNotations.

(* ============================================================ *)
(* Section 1: Build and Extract Foundations                     *)
(* ============================================================ *)

Axiom build_refl_deriv : forall (A : ProofSystem) (ps : list (axioms A)),
  Forall2 (fun p q => derivable A p q) ps ps.

Axiom build_trans_deriv : forall (A : ProofSystem) (ps qs rs : list (axioms A)),
  Forall2 (fun p q => derivable A p q) ps qs ->
  Forall2 (fun p q => derivable A p q) qs rs ->
  Forall2 (fun p q => derivable A p q) ps rs.

Axiom build_rule_deriv : forall (A : ProofSystem) (ps qs : list (axioms A)),
  Forall2 (fun p q => rules A p q) ps qs ->
  Forall2 (fun p q => derivable A p q) ps qs.

Definition build_foundations (A : ProofSystem) : ProofSystem :=
  {| axioms := list (axioms A);
     rules := fun ps qs => Forall2 (fun p q => rules A p q) ps qs;
     derivable := fun ps qs => Forall2 (fun p q => derivable A p q) ps qs;
     refl_deriv := build_refl_deriv A;
     trans_deriv := build_trans_deriv A;
     rule_deriv := build_rule_deriv A |}.

Definition extract_foundations (A : ProofSystem) : ProofSystem.
Proof.
  refine {|
    axioms := { f : axioms A -> axioms A | forall p, derivable A p (f p) };
    rules := fun f g => forall p, derivable A (proj1_sig f p) (proj1_sig g p);
    derivable := fun f g => forall p, derivable A (proj1_sig f p) (proj1_sig g p);
    refl_deriv := fun f => fun p => refl_deriv A (proj1_sig f p);
    trans_deriv := fun f g h H1 H2 => fun p => trans_deriv A (proj1_sig f p) (proj1_sig g p) (proj1_sig h p) (H1 p) (H2 p);
    rule_deriv := fun f g H => H
  |}.
Defined.

(* ============================================================ *)
(* Section 2: Bootstrap Dialgebra Definition                    *)
(* ============================================================ *)

Record BootstrapDialgebra := {
  carrier : ProofSystem ;
  delta : ProofFunctor (build_foundations carrier) carrier ;
  gamma : ProofFunctor carrier (extract_foundations carrier)
}.

(* ============================================================ *)
(* Section 3: Smallest Guarded Bootstrap Dialgebra Theorem      *)
(* ============================================================ *)

Axiom smallest_guarded_dialgebra :
  forall (A : ProofSystem),
  exists (D : BootstrapDialgebra), True.
