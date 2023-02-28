Require Import Arith.
Import Nat.
Require Import Lia.
Require Import Utf8.


Definition relation (X : Type) := X -> X -> Prop.

Inductive multi {X : Type} (R : relation X) : relation X :=
    | multi_refl : forall (x : X), multi R x x
    | multi_step : forall (x y z : X), R x y -> multi R y z -> multi R x z.

Theorem multi_R : 
    forall (X : Type) (R : relation X) (x y : X),
        R x y -> (multi R) x y.
Proof.
    intros.
    econstructor.
    - apply H.
    - apply multi_refl.
Qed.

Theorem multi_trans :
    forall (X : Type) (R : relation X) (x y z : X),
        multi R x y  ->
        multi R y z ->
        multi R x z.
Proof.
    intros X R x y z H0 H1.
    induction H0.
    - assumption.
    - apply IHmulti in H1. apply (multi_step R _ _ _ H H1).
Qed.

Inductive dexp : Type :=
 | d_var  : nat -> dexp
 | d_abs  : dexp -> dexp
 | d_app  : dexp -> dexp -> dexp.