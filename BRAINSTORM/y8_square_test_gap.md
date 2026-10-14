# y8_square_test_gap — "n is a square ⟺ every level is clean", and ES-five as the admissible version of this square test (O217)

## Idea
**Prop 1 (PROVED, elementary).** For odd n ≥ 1 call level t *clean* if (n/r) = +1 (Legendre) for every ODD prime
r | tn + 1 (r ∤ n automatically; the prime 2 is excluded by convention — e.g. 3·1² + 1 = 4 with 2 inert in ℚ(√−3)). Then n is a perfect square ⟺ every level t ≥ 1 is clean.
*Proof.* ⇒: (m²/r) = 1. ⇐: if n is not a square, (n/·) is a non-principal character, so some odd prime r has
(n/r) = −1 (Dirichlet, or elementary: a non-square is a non-residue mod some prime); with t ≡ −n⁻¹ (mod r),
t ∈ [1, r − 1], r | tn + 1. ∎ (For p prime, r | tp + 1 ⇒ (p/r) = (−t/r), so "clean" = "all primes of tp + 1 split in
ℚ(√−t)"; equivalently (r/p) = +1 by reciprocity when p ≡ 1 mod 4.)
**Prop 2 (PROVED; restatement of (J)33 + TWO_FIBRES Thm A).** For p ≡ 1 (4) prime: ES-five(p) ⟺ some level t has an
*admissible* divisor A | tp + 1, A ≡ −1 (mod t) (then automatically (tp + 1)/A ≡ −1), with (A/p) = −1.
For t ∈ {1, 2} every divisor is admissible, so there "unclean ⟺ carries a χ = −1 word"; for t | 24 admissible means
one residue class (units of ℤ/t are 2-torsion).
So SQ₅ at primes is exactly the square test of Prop 1 with "all prime factors" weakened to "admissible divisors":
**the whole ES content is the admissibility gap**. At composite n, 3SQ (y8_three_squares_sq) is the analogous
weakening with (−A/ℓ) for each odd-exponent ℓ | n.

## Literature
Elementary; ET (2013) §2 for the divisor forms; LONGSHOT_PIGEONHOLE, redteam-automorphic-2 Thm 2.2 (B2).

## Barrier screen
Prop 1 is proved by exhibiting ONE unclean level from one non-residue prime; Prop 2 needs that prime (or another
non-residue product) inside a divisor in the class −1 mod t: B2 exactly (the modulus t is part of the solution, and
the level from Prop 1 is t₀ < r with no control on the class of the cofactors). B4: pigeonhole over divisors of
tp + 1 mod t fails when tp + 1 has few prime factors, which is precisely what happens near profinite squares
(y8_adelic_continuity: small primes cannot divide tp + 1 in the wrong genus). T1-safe (Prop 1 ⇐ fails at squares).

## Cheap numerics (`scripts/y8_admissible.py`)
All primes p ≡ 1 (4) in (10⁵, 1.2·10⁵), levels t ≤ 30 (25 260 levels): unclean 69.2 %, carrying a χ = −1 word 31.6 %;
admissible/unclean = 0.456.

## Assessment
PROVED (Props 1–2) — a precise statement of where ES sits relative to a trivial square test. No mechanism to close
the gap (B2). Useful as steering: any proof must manufacture admissibility, not uncleanness.
