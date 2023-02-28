Require Import Utf8.
Require Import Coq.Init.Nat.
Require Import Lia.

Lemma zero_plus_zero : 0 = 0.
Proof.
    reflexivity.
Qed.

Lemma one_plus_one : 1 = 1.
Proof.
    reflexivity.
Qed.

Lemma zero_plus_zero_eq_zero : 0 + 0 = 0.
Proof.
    reflexivity.
Qed.

Lemma n_plus_zero_eq_n : forall n : nat, n + 0 = n.
Proof.
    intros n.
    induction n.
    - reflexivity. 
    - simpl. rewrite IHn. reflexivity.
Qed.

Lemma n_plus_one_eq_sn : forall n : nat, n + 1 = S n.
Proof.
    intros n.
    induction n.
    - simpl. reflexivity.
    - simpl. rewrite IHn. reflexivity.
Qed.

Lemma n_minus_zero_eq_n : forall n : nat, n - 0 = n.
Proof.
    intros n.
    induction n.
    - simpl. reflexivity. 
    - simpl. reflexivity.
Qed.

Lemma n_plus_one_greater_n : forall n : nat, n + 1 > n.
Proof.
    intros n.
    induction n.
    - simpl. lia.
    - simpl. rewrite n_plus_one_eq_sn. lia.
Qed.

Lemma n_plus_one_exists : forall n : nat, exists m : nat, n + 1 = m.
Proof.
    intros n.
    exists (S n).
    lia.
Qed.