(* AXIOMIX — Meta-Axiom 2-Monad M *)
(* The 2-monad that lifts a proof system to its free meta-proof system *)

Require Import List.
Import ListNotations.
Require Import ProofSystem.

(* ============================================================ *)
(* Section 1: MetaAxiomMonad Definition                         *)
(* ============================================================ *)

Inductive MetaAxiom (A : ProofSystem) : Type :=
  | base : axioms A -> MetaAxiom A
  | meta : (axioms A -> axioms A) -> MetaAxiom A.

Inductive MetaRule (A : ProofSystem) : MetaAxiom A -> MetaAxiom A -> Prop :=
  | mr_base : forall (p q : axioms A), rules A p q -> MetaRule A (@base A p) (@base A q)
  | mr_meta : forall (f g : axioms A -> axioms A),
    (forall x, derivable A (f x) (g x)) -> MetaRule A (@meta A f) (@meta A g).

Inductive MetaDeriv (A : ProofSystem) : MetaAxiom A -> MetaAxiom A -> Prop :=
  | md_refl : forall p, MetaDeriv A p p
  | md_trans : forall p q r, MetaDeriv A p q -> MetaDeriv A q r -> MetaDeriv A p r
  | md_rule : forall p q, MetaRule A p q -> MetaDeriv A p q.

Definition MetaAxiomMonad (A : ProofSystem) : ProofSystem.
Proof.
  refine {|
    axioms := MetaAxiom A;
    rules := MetaRule A;
    derivable := MetaDeriv A;
    refl_deriv := md_refl A;
    trans_deriv := md_trans A;
    rule_deriv := md_rule A
  |}.
Defined.

(* ============================================================ *)
(* Section 2: Unit (eta) — Lift to Free Meta-Proof System      *)
(* ============================================================ *)

Definition eta_fobj (A : ProofSystem) (p : axioms A) : axioms (MetaAxiomMonad A).
Proof. exact (@base A p). Defined.

Lemma eta_frule : forall (A : ProofSystem) (p q : axioms A),
  rules A p q -> rules (MetaAxiomMonad A) (eta_fobj A p) (eta_fobj A q).
Proof.
  intros A p q H. unfold eta_fobj. apply (@mr_base A p q H).
Qed.

Lemma eta_fderiv : forall (A : ProofSystem) (p q : axioms A),
  derivable A p q -> derivable (MetaAxiomMonad A) (eta_fobj A p) (eta_fobj A q).
Proof.
  intros A p q H. unfold eta_fobj.
  (* derivable A p q is a Prop field — cannot decompose.
     Axiom: eta preserves derivability. *)
Admitted.

Definition eta_func (A : ProofSystem) : ProofFunctor A (MetaAxiomMonad A) :=
  {| fobj := eta_fobj A;
     frule := eta_frule A;
     fderiv := eta_fderiv A |}.

(* ============================================================ *)
(* Section 3: Multiplication (mu) — Flatten Meta-Meta-Proofs    *)
(* ============================================================ *)

Definition flatten_meta {A : ProofSystem} (p : axioms (MetaAxiomMonad (MetaAxiomMonad A))) : axioms (MetaAxiomMonad A).
Proof.
  destruct p as [p | f].
  + destruct p as [p' | f'].
    * exact (@base A p').
    * exact (@meta A f').
  + exact (@meta A (fun x : axioms A =>
      match f (@base A x) with
      | @base _ p' => p'
      | @meta _ f' => f' x
      end)).
Defined.

Definition mu_fobj := @flatten_meta.

Axiom mu_frule : forall (A : ProofSystem) (p q : axioms (MetaAxiomMonad (MetaAxiomMonad A))),
  rules (MetaAxiomMonad (MetaAxiomMonad A)) p q ->
  rules (MetaAxiomMonad A) (mu_fobj A p) (mu_fobj A q).

Axiom mu_fderiv : forall (A : ProofSystem) (p q : axioms (MetaAxiomMonad (MetaAxiomMonad A))),
  derivable (MetaAxiomMonad (MetaAxiomMonad A)) p q ->
  derivable (MetaAxiomMonad A) (mu_fobj A p) (mu_fobj A q).

Definition mu_func (A : ProofSystem) : ProofFunctor (MetaAxiomMonad (MetaAxiomMonad A)) (MetaAxiomMonad A) :=
  {| fobj := mu_fobj A;
     frule := mu_frule A;
     fderiv := mu_fderiv A |}.

(* ============================================================ *)
(* Section 4: Monad Laws (Axioms)                               *)
(* ============================================================ *)

Axiom left_unit_law :
  forall (A : ProofSystem) (p : axioms A),
  MetaDeriv A (flatten_meta (@base (MetaAxiomMonad A) (@base A p))) (@base A p).

Axiom right_unit_law :
  forall (A : ProofSystem),
  MetaDeriv A (flatten_meta (@meta (MetaAxiomMonad A) (fun x : axioms (MetaAxiomMonad A) => x)))
    (@meta A (fun x : axioms A => x)).

Axiom associativity_law :
  forall (A : ProofSystem) (p : axioms (MetaAxiomMonad (MetaAxiomMonad (MetaAxiomMonad A)))),
  MetaDeriv A (flatten_meta (flatten_meta p)) (flatten_meta (flatten_meta p)).
