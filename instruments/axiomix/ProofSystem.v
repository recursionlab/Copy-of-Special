(* AXIOMIX — ProofSystem and 2-Category Structure *)
(* The 2-category Inf of proof systems *)

Require Import List.
Import ListNotations.

(* ============================================================ *)
(* Section 1: ProofSystem                                       *)
(* ============================================================ *)

Record ProofSystem := {
  axioms : Type;
  rules : axioms -> axioms -> Prop;
  derivable : axioms -> axioms -> Prop;
  refl_deriv : forall p, derivable p p;
  trans_deriv : forall p q r, derivable p q -> derivable q r -> derivable p r;
  rule_deriv : forall p q, rules p q -> derivable p q
}.

(* ============================================================ *)
(* Section 2: ProofFunctor                                      *)
(* ============================================================ *)

Record ProofFunctor (A B : ProofSystem) := {
  fobj : axioms A -> axioms B;
  frule : forall p q, rules A p q -> rules B (fobj p) (fobj q);
  fderiv : forall p q, derivable A p q -> derivable B (fobj p) (fobj q)
}.

(* Identity functor *)
Definition id_functor (A : ProofSystem) : ProofFunctor A A.
Proof.
  refine {| fobj := fun p => p |}.
  + intros p q H. exact H.
  + intros p q H. exact H.
Defined.

(* Functor composition *)
Definition functor_comp {A B C : ProofSystem}
  (F : ProofFunctor A B) (G : ProofFunctor B C) : ProofFunctor A C.
Proof.
  refine {| fobj := fun p => @fobj B C G (@fobj A B F p) |}.
  + intros p q H. exact (@frule B C G (@fobj A B F p) (@fobj A B F q) (@frule A B F p q H)).
  + intros p q H. exact (@fderiv B C G (@fobj A B F p) (@fobj A B F q) (@fderiv A B F p q H)).
Defined.

(* ============================================================ *)
(* Section 3: ProofTransform                                    *)
(* 2-cells of the 2-category Inf                                *)
(* ============================================================ *)

Record ProofTransform {A B : ProofSystem} (F G : ProofFunctor A B) := {
  component : forall p, derivable B (@fobj A B F p) (@fobj A B G p)
}.

(* ============================================================ *)
(* Section 4: Empty Proof System                                *)
(* The initial object in Inf                                     *)
(* ============================================================ *)

Inductive EmptyAxioms := .

Definition EmptyProofSystem : ProofSystem.
Proof.
  refine {|
    axioms := EmptyAxioms;
    rules := fun _ _ => False;
    derivable := fun _ _ => False;
    refl_deriv := fun p => match p with end;
    trans_deriv := fun p q r H _ => match H with end;
    rule_deriv := fun p q H => match H with end
  |}.
Defined.
