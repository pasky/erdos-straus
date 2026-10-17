# z29_dickson_least_shift — smooth p − 1 freezes the small shifts; the least shift is unbounded under Dickson (O259; B1_LINE §4)

**Idea.** Explain why the three b = 1 failures (and the census records) have smooth p − 1, by asking what p ≡ 1 (mod M) does
to the pairs of small shift s.
**Literature.** Dickson's k-tuples conjecture; redteam-automorphic-2 Thm 2.2 (B2: fixed finite slice sets fail i.o. under H);
AMPLIFY_EXCEPTION Thm 3.2 (p ≡ □ mod L ⟹ no witness of modulus | L).
**Result.** Prop 4.1 (PROVED): if M_σ | p − 1, then for each shift s ≤ σ, Q_s = (p + s)/(1 + s) ≡ 1 (mod s) has only primes
> σ + 1. The pairs at shift s are exactly the divisors t ≡ −1 (mod s) of (1 + s)Q_s with 4 | st. Pairs supported on M_σ
are dead, and Q_s prime kills the shift. Theorem 4.2 (CONDITIONAL on Dickson): the forms 1 + M_σ k and 1 + (M_σ/(1 + s))k
are admissible (all = 1 at k = 0). So infinitely many p have no pair of shift ≤ σ.
**Barrier screen.** This is B2 in its sharpest b = 1 form, and it is a barrier, not a route. It does not reach the full line,
which uses ≍ √p shifts; a Dickson construction would need M_σ > p. T1: p ≡ 1 (mod M_σ) is the profinite T1 point 1 at small
moduli.
**Cheap numerics.** `z29_freeze_check.py 2e9` (p ≡ 1 mod 176 400 and mod 64 033 200): exact agreement, and no pair whenever
Q_s is prime. Census record 215 at p = 22 010 483 881 with p − 1 = 2³·3²·5·7·11·19·23²·79 (all primes < 41 are QRs mod p).
**Assessment.** PROVED (Prop 4.1) + CONDITIONAL (Thm 4.2). It explains the smooth-(p − 1) pattern mechanistically.
Prediction: the least shift is unbounded (census: record 119 ≤ 10⁸, 215 at 2.2·10¹⁰), while full failures stay finite (§3).
