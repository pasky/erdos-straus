# R227 — hostile review of O230 Synthesis V (SYNTHESIS_SPARKS5.md + BRAINSTORM/s5_*.md)

Reviewer branch side-agent/review-synthesis-five (merged side-agent/synthesis-five at review start). All numerics below
were recomputed with FROM-SCRATCH code (`scripts/review_r227_census.c`, `scripts/review_r227_lemmas.py`, further
`scripts/review_r227_*.py` listed per claim); none of the author's scripts were reused except as a diff target.

## Summary verdicts (filled in claim by claim)
| # | claim | verdict |
|---|---|---|
| 1 | three side numbers, Lemma S, Lemma G, side deformations, N₋ ≤ U | SOUND-AFTER-REPAIRS (minor) |
| 2 | EVIDENCE: 70–80 % residual removal; K0 = 8 defective deformation; corr; N₋/U scale law; hard primes forced | (pending) |
| 3 | CONJECTURE U | (pending) |
| 4 | refutation of N₋ ≥ U/2 | (pending) |
| 5 | Prop R | (pending) |
| 6 | Prop C | (pending) |
| 7 | uniform profinite sterility, Prop V | (pending) |
| 8 | novelty vs (J)48/(J)53/(J)55/R225 | (pending) |

## Claim 1 — side numbers, Lemma S, Lemma G, deformations, N₋ ≤ U: SOUND-AFTER-REPAIRS

Re-derivation.
* AB = (tu−1)(tv−1) = t²uv − tu − tv + 1 = t(tuv − u − v) + 1 = tp + 1; Av = tuv − v = p + u; Bu = p + v. ✓
* Lemma G: gcd(tp+1, p+u) = gcd(tp+1 − t(p+u), p+u) = gcd(tu − 1, p+u) = A because A | p+u. Holds for every n, not
  only primes. Converse (A | p+u ⇒ word) trivial. ✓ (It is a dictionary: "gcd = tu − 1" is the same as "tu − 1 | p + u".)
* Lemma S(a): ψ(A)ψ(B) = ψ(tp+1) = 1, and (−1/p) = 1. ✓ S(b): t-side (p/r) = (−t⁻¹/r) = (−t/r); u-side (p/r) = (−u/r),
  with r ∤ u (else r | p). Reciprocity (r/p) = (p/r) uses p ≡ 1 (4); for the Jacobi version at composite n ≡ 1 (4) the
  same holds by Jacobi reciprocity. ✓ S(c): **does not need (b) or reciprocity at all** — it is just multiplicativity
  of ψ and A | N_t, N_u (B | N_t, N_v). ✓ Hence N₋ ≤ U is PROVED, at primes and (Jacobi, zeros allowed) at composites.
* Role of 2: cleanliness requires ψ(2) = +1, i.e. p ≡ 1 (8) whenever N_X is even; the census includes 2. ✓
* u-side deformation: p = m² + K, s = K + u, us = □, gcd(m, s) = 1 ⇒ N_u = m² + s; an odd prime r | N_u has r ∤ ms,
  (−s/r) = 1 and (u/r) = (s/r), so ψ(r) = (−u/r) = 1. ✓ The parametrisation u = d a², K + u = d b², K = d(b−a)(b+a) is
  correct; the solution set is finite (u ≤ K²/4).
* t-side ((J)53): tK + 1 = c², gcd(m, c) = 1 ⇒ N_t = t m² + c². ✓

From-scratch checks (`scripts/review_r227_lemmas.py`; brute-force word enumeration over (t, u), not divisor-based):
all 4 280 words of primes p ≡ 1 (4) < 1200: 0 violations of Lemma G, S(a), S(b) (every odd prime of every side), S(c).
Deformations: every p ≡ 1 (8) < 1200, **every** m < √p (not only ⌊√p⌋), the complete finite u-list (via the d | K
parametrisation) and t < 200: 0 unclean u-sides, 0 unclean t-sides under the gcd conditions. K = 24 u-list
{1, 3, 8, 25} and t-list {1, 2, 5, 7, 12, …} reproduced. `scripts/review_r227_census.c` (divisor enumeration over u,
sides cleaned via the factorisations A·B, A·v, B·u) reproduces s5_sides.c column for column at all 8 976 primes
p ≡ 1 (4) < 2·10⁵ (N, N₋, N_t-clean, N_any-clean; 0 mismatches), with 0 Lemma S violations up to 3·10⁷ (see claim 4).

Defects (claim 1).
* **D1 (MINOR) s5_three_sides, Lemma S proof (b).** "r = p would force p | u, and then v(tp − 1) = 2p" treats only
  u = p. Repair: "if u = kp then A = tkp − 1 is prime to p and divides p(k+1), so tkp − 1 ≤ k + 1, impossible for
  p > 3." (And note (c) does not need (b).)
* **D2 (MINOR) s5_three_sides "Side deformations" / SYNTHESIS §1.** "t-side solutions form Pell-type infinite
  families" — tK + 1 = c² is c² ≡ 1 (mod K), i.e. finitely many quadratic progressions t = (c² − 1)/K in c; no Pell
  equation is involved. Repair: "quadratic families t = (c² − 1)/K, c² ≡ 1 (mod K)". Likewise "about τ(K)" u-side
  solutions is a heuristic; the exact count is #{(d, e, f): d | K, ef = K/d, e < f, e ≡ f (2)} (Assessment).
* **D3 (MINOR) s5_three_sides "Mechanism" (K0 = 8) and SYNTHESIS §2.** "the t-sides with 8t + 1 = c², t ≡ 1 (mod 9),
  are clean apart from an exact factor 9" is false as stated. From scratch (p = m² + 8 prime, m < 3000, 159 primes,
  c < 400, c ≡ 3 (6)): when gcd(m, c) = 3 the side is exactly 3²·(clean) in 8 709/8 709 cases; when gcd(m, c) > 3
  (e.g. 9 | m, c) the 3-adic valuation is 2, 4, 6, 8, 10 and in 629 of 1 944 cases another ψ-odd prime appears.
  Repair: add "with gcd(m, c) = 3". (The u = 1 side is always 9·(clean): 159/159.) The census numbers are unaffected
  because s5_defect.c classifies sides by actual factorisation, not by this description.
