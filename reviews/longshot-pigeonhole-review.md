# R135 — hostile review of O135 (LONGSHOT_PIGEONHOLE.md)

Reviewer: R135 side agent. Scope: §§1–2 lemmas, Theorem 2.2, §3 numerics (sample), §5 labels.
From-scratch scripts: `scripts/review_r135_*.py` (no author code reused).

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (e-slice) | SOUND (fibre-of-V statement); MINOR wording on "bijection" (D1) |
| Lemma 1.2 (genus incl. ℓ = 2) | (see below) |
| Lemma 1.3 (collisions → signed solutions) | (see below) |
| Prop 1.4 (Kneser criterion, sharpness) | (see below) |
| Lemma 2.1 (forcing cost) | (see below) |
| Theorem 2.2 | (see below) |
| Lemma 2.3 | (see below) |
| §3 numerics | (see below) |

## Lemma 1.1 — SOUND

Re-derived: (i) `4N^I ≡ 1`, `4N^II ≡ p (mod e)`, e odd ⇒ gcd(N,e) = 1 (p ∤ e). (ii)/(iii) immediate from the
defining equations; `e | a+b ⟺ ab⁻¹ ≡ −1`. (iv) exponent bookkeeping correct, every `t ∈ [−v, v]` realised.

From scratch (`scripts/review_r135_slices.py`):
* all primes 5 ≤ p < 2000: ES(p) by a direct `4/p = 1/x+1/y+1/z` solver ⟺ some e-slice (either type) has
  `−1 ∈ Σ_e(N)`: **0 mismatches**.
* all primes 5 ≤ p < 110 (both residues mod 4): complete enumeration of ordered solution triples, split by the
  number of coordinates divisible by p, versus `3·Σ_e #{(a,b): ab | N_e, e | a+b}`. No solution has 0 or 3
  coordinates divisible by p. **With the extra condition gcd(a,b) = 1 the counts agree exactly for every p;
  without it the fibre counts are strictly larger for 18 of 27 primes** (e.g. p = 71, Type I: 171 solutions vs
  210 fibre points; `(1,1,2,18;e=1)` and `(3,3,6,2;e=1)` both give (1278, 36, 36)). This is the dilation symmetry
  `(a,b,c,d) ↦ (λa, λb, λc, λ⁻²d)` of Elsholtz–Tao §2 (checked in sources/elsholtz-tao-1107.1010.pdf, Prop 2.2:
  uniqueness needs gcd(a,b,c) = 1).

Lemma 1.1 as stated is about the fibres of V_T(p), and there it is correct; ES(p) ⟺ V(p) ≠ ∅ is correct. See D1.
