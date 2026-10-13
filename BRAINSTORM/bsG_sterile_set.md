# bsG_sterile_set — the profinite sterile set of (W) (O180)

## Idea
Every fixed-pair family (two letters fixed) is a residue class: (x,y) gives n ≡ −x (mod xy − 1), and (x,z) gives n ≡ −(x+z) (mod xz). Let S ⊂ Ẑ be the
closed set missed by all of them. By compactness, finite coverings of "everything outside a clopen V" exist iff S ⊂ V. The hope: S = {−1}.
Then every exception n ≥ C(M) would satisfy M | n + 1 for all M, which a growth argument might contradict.

## Results (LORENZINI_W §4)
* S ∩ Z = {−1} (PROVED, Prop 4.1).
* **S is infinite and −1 is an accumulation point (PROVED, Thm 4.2):** ν(ℓ, ℓ − 1) ∈ S for every prime ℓ ≥ 3. Here ν(ℓ, c) means −1 at all primes ≠ ℓ
  and c in Z_ℓ. The proof is a finite case analysis of the two family types.
* EVIDENCE: many more single-prime deviations (ℓ = 2: c = 3, 7, 15, …). Multi-prime deviations "c at all primes ≤ P" (integer c ≤ 2000, moduli ≤ 10⁵)
  are uncovered for P ≤ 5 (only c ≡ −1 mod 30 at P = 5) and never for P ≥ 7.
* Finite levels: |U_M| = 0.161 %, 0.0852 %, 0.0225 %, 0.00763 % for M = 720720, …, 151351200, but the projection mod 12 is stuck at {3, 6, 9, 11}.

## Literature
Lorenzini Prop 6.3 (congruence + one-letter slices). Analogue: FUNCTIONFIELD_ES sterile points (O-series), bsB_sterile_pretentious.

## Barrier screen
This is the B1 barrier made exact for (W). It is the (W)-analogue of POINTWISE_SIZE Thm M: congruence-only data cannot finish. It refines
HJ_DEEP Lemma 3.2 from "−1 escapes" to "an infinite closed set escapes, accumulating at −1".

## Cheap numerics
`scripts/bsG_sterile.py M`, `scripts/bsG_dev.c`, `scripts/bsG_devT.c`. Integers near sterile points are *not* hard: n = 3L′ − 1 has R = 264
(mean ≈ 300).

## Assessment
PROVED obstruction (compactness route closed). Open question: is every sterile point ≡ −1 at all but finitely many primes? (EVIDENCE says yes in the probe.)
Even if so, that would only say exceptions have n + 1 divisible by a large smooth number, with no contradiction. Promise 1/5.
