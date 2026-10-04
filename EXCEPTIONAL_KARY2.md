# EXCEPTIONAL_KARY2 — the 3/4 cap without the B-hypothesis, for ℛ(M), (a,D) and Case-A classes (task O14)

Status: **checkpoint 1 (draft, not yet reviewed).** Labels follow
`DISCOVERIES.md`. Notation follows `EXCEPTIONAL_KARY.md` (EK),
`EXCEPTIONAL_TWIN.md` (ETw), `EXCEPTIONAL_TWIN4.md` (TW4) and
`EXCEPTIONAL_THETA.md` (ET).

## 0. Summary

(filled in at the end)

## 1. Where EK Theorem 4.5 uses B, and where it does not

EK Thm 4.5 is assembled from EK Thm 4.1 (abstract sequential limit with
random costs), the base (ETw Lemma 1.3), singleton steps below `e^{s₁}`
(ETw Prop 4.1), sequential blocks `(e^s, e^{2s}]` with EK Thm 2.5 as the
step inequality, one linear block `(e^{λ/2}, e^λ]` (ETw Cor 4.3), and the
leak (EK Lemma 4.3). The hypothesis `M ≤ P(M)^{1+B}` enters at exactly
three places:

* **(B1) block first moment** (EK Lemma 4.2′, Step 3): the partial
  summation runs over `M ≤ e^{2(1+B)s}`;
* **(B2) singleton first moment** (ETw Prop 4.1): the same over
  `M ≤ e^{(1+B)s₁}`;
* **(B3) second moment / leak** (ETw Lemmas 2.4, 4.0, used in EK Lemma
  4.2(3) and 4.3): the pointwise bound `τ(A_q²) ≤ ℓ^{o(1)}`, valid because
  the cofactor q of the top prime power is `≤ ℓ^B`; and the constants
  `W₀(B)`, `C(B)`.

Everything else is B-free:
* EK Thm 2.5 is arithmetic-free and has no arity bound;
* EK Thm 4.1, ETw Thm 2.3′, ETw Cor 4.3 are B-free;
* the base: `Q₀` may be astronomically large; only `log(Q₀/|R|) = O(W)`
  enters (ETw Lemma 1.3(2));
* the leak mechanism (Lemma 2.1′ of ETw: every class is decided at its
  top prime) is B-free.

**The number of large primes per modulus never enters.** The level
gives d-locality (`d = ⌊λ/s⌋` block primes per term of ν), and EK Thm 2.5
accepts patterns of any arity. The arithmetic inputs are first moments
(sums over *all* classes with top prime in a range) and the second moment
of `p_ℓ` (a sum over cofactors). Neither sees `ω(M)`. This is the
difference from the Λ² route of TW4, where `ω_L(M)` controls the
noise-stability losses (`2^r`, `(log L)^r`).

So, to drop B, it suffices to replace (B1)–(B3) by bounds over *all*
classes with `P(G) ≤ y`, and over all cofactors of `ℓ^v`. That is §§3–4.
To add (a,D)- and Case-A classes, the base must also avoid their
W-smooth classes; that is §2.
