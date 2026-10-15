# R233 — hostile review of O231 (UNFORCED_WORDS.md, BRAINSTORM/z7_*.md)

Reviewer branch side-agent/review-unforced-words (merged side-agent/unforced-words). From-scratch scripts:
`scripts/review_r233_*`. ES is not solved; nothing below changes that.

## Summary verdicts (filled in progressively)

| # | claim | verdict |
|---|---|---|
| 1 | Lemma 1.1 (n ≡ 5 (8) trivial) | SOUND |
| 2 | Prop F, Cor 1.2 | SOUND (MINOR notation D2) |
| 3 | Prop F′ (s = 3, 4, 7), Cor 3.1 | pending numerics |
| 4 | Lemma 2.1, Flip Lemma 2.2 | pending |
| 5 | Thm 3.2 (Dickson) | pending |
| 6 | U2 sandwich, CONJECTURE U2 | pending |
| 7 | Remark 4.1 | pending |
| 8 | Prop 5.1 (Haar 3/4) | pending |
| 9 | Lemma 5.2 | pending |
| 10 | SHARP 1 (failures ⟹ ψ-odd part of n+1 = 3²) | pending |
| 11 | Lemma 6.1 / 105 genus collapse | pending |
| 12 | SQ_± split | pending |
| 13 | labels | pending |

## Claim 1 — Lemma 1.1: SOUND
Re-derived. (1, n+2, 2): 2(n+2) − (n+2) − 2 = n. A = n+1, B = 1; sides N_t = n+1 (≡ 6 (8), so 2 ∥ N_t with
ψ(2) = (2/n) = −1), N_u = 2(n+1), N_v = n+2 with ψ(n+2) = (2/n) = −1 (an odd number of ψ-odd prime factors).
χ = ψ(n+1) = ψ(1) = +1. Non-squareness is automatic for n ≡ 5 (8). Nothing to repair.

## Claim 2 — Prop F, Cor 1.2: SOUND
Re-derived the four parametrisations: t = 1 ⟺ (u−1)(v−1) = n+1 (A = u−1); u = 1 ⟺ (t−1)v = n+1 (A = t−1, N_u = n+1);
t = 2 ⟺ (2u−1)(2v−1) = 2n+1; u = 2 ⟺ (2t−1)v = n+2. In each, every positive divisor of the fixed side X is an
admissible D and gives a positive word. (iii)⇒(i) with D = r; (i)⇒(ii) Lemma S; (ii)⇒(iii) definition. Note the
proof never uses n ≡ 1 (8) (for n ≡ 5 (8) r = 2 is allowed) — harmless. The proof is valid for composite n as well
(X is coprime to n, so no ψ = 0 primes occur). Cor 1.2 ✓. Cor 3.1's "min = K(p)+1" for the certificate is also right:
the certificate of the s-family cannot have another coordinate < s, because that coordinate's side is clean by K(p) ≥ s−1.

## Claim 3 — Prop F′ (s = 3, 4, 7) and Cor 3.1: SOUND
Re-derived. Odd r | p+s or sp+1 has ψ(r) = (p/r) = (−s/r); ψ(2) = +1 at p ≡ 1 (8). s = 3: 4 ∥ X, D ∈ {r, 2r}
reaches the class 2 (3) (3 ∤ X). s = 4: ψ(D) = (−1/D) = −1 for every admissible D. s = 7: 8 | X, 7 ∤ X, ψ(r) = (r/7),
r·⟨2⟩ = the NR coset ∋ 6. The 2-adic remark ("every word is a certificate when 4 | s or s ≡ 7 (8)") is also right:
−s is then a fundamental-type discriminant whose Kronecker character is a character mod s with value −1 at −1, and
(−s/2) = +1 = ψ(2) when s ≡ 7 (8).
From-scratch brute force `scripts/review_r233_propF.py 100000` (all 2 384 primes p ≡ 1 (8) < 10⁵; every word of each
family enumerated, cleanliness by full factorisation, Lemma S asserted): 0 mismatches of
"unclean ⟺ certificate ⟺ unforced" for s ∈ {1, 2, 3, 4, 7}, both family kinds. Controls reproduce the author's
numbers exactly: unclean ≠ certificate at s = 5: 310 (t) / 280 (u); s = 6: 328 / 183; s = 8: 297 / 290;
unforced ≠ certificate only at s = 5: 24 (t) / 39 (u).
Cor 3.1 follows (U = 0 or N₋ = 0 ⟹ all nine sides clean ⟹ K(p) ≥ 4 and p+7, 7p+1 clean). The "min = K(p)+1"
clause is right (see Claim 2).

## Claim 5 — Thm 3.2 (CONDITIONAL on Dickson): SOUND-AFTER-REPAIRS (D3, MINOR)
Re-derived. With p = 1 + Mx and every prime power ℓ^{a_ℓ} ∥ M exceeding K+1, (s+1) | M and p+s = (s+1)L_s,
sp+1 = (s+1)L′_s; the 2K distinct forms all have constant term 1 (≢ 0 mod ℓ | M) and, for ℓ > 2K+1, cover ≤ 2K < ℓ
residues: admissible, no local obstruction, all leading coefficients positive. Prime factors of s+1 are ≤ K+1 and
divide p−1, so ψ = +1; ψ(L_s) = ψ(s) = +1, ψ(L′_s) = ψ(1)ψ(s+1) = +1; a prime with ψ = +1 is clean. Label
CONDITIONAL is correct. Illustration `scripts/review_r233_dickson.py K` finds the predicted primes:
K = 2: p = 25 561, 53 281, 156 241; K = 3: 15 555 961, …; K = 4: 36 070 209 001, … — all with K(p) ≥ K verified by
direct factorisation.
**D3 (MINOR).** UNFORCED_WORDS.md §3, Thm 3.2 proof: "M = 8·∏_{3 ≤ ℓ ≤ 2K+1} ℓ^{a_ℓ} … (also 2^{a_2} > K + 1)" —
as written the 2-part of M is 8, so for K ≥ 15 (s+1 = 16) (s+1) ∤ M and L_s is not integral. Repair: M =
2^{a_2}·∏_{3≤ℓ≤2K+1} ℓ^{a_ℓ} with a_2 ≥ 3 and 2^{a_2} > K+1.

## Census (from scratch): `scripts/review_r233_census.c` + `scripts/review_r233_post.py`
Global enumeration of all positive words (t, u, v) with n = tuv − u − v, binned by n; χ by a fresh Jacobi routine,
cleanliness of N_t = AB, N_u = Av, N_v = Bu via an SPF sieve. Runs: (a) all non-square n ≡ 1 (8) < 10⁷
(1 248 419 n, composites included, 29 s); (b) all 464 288 primes p ≡ 1 (8) < 3·10⁷ (31 s). Outputs /tmp/r233_*.txt
(not committed; regenerate with `review_r233_census N 0|1`). Results:
* U = 0 or U2 = 0: only n = 105 (N = 11, N₋ = U = U2 = 0) in (a); none in (b). **This extends CONJECTURE U2's evidence
  from 2·10⁵ to all n ≡ 1 (8) < 10⁷.**
* N₋ ≤ U2 ≤ U: 0 violations in (a) and (b).
* (b): Σ N₋/Σ U2 = 0.873, Σ U2/Σ U = 0.882, min N₋/U2 = 0.620 at 23 125 409 (364/587) — exact match.
  (a) adds composites: min N₋/U2 = 0.609 at 7 303 841 (182/299), Σ ratios 0.891 / 0.886. So "N₋ ≥ U2/2 unrefuted"
  also holds for composites < 10⁷ (the document only states primes).
* Failures 2N₋ < U at n ≡ 1 (8): (a) 110 897, 1 512 089, 2 152 097, 3 000 329, 5 270 849, 9 948 977; (b) 5 270 849,
  17 188 937, 21 387 257 — the author's 8, with R227's (N, N₋, U) values reproduced (e.g. 5 270 849: 505/192/389).
  ψ-odd part of n+1 is exactly {3: 2} in **all 8** (by factorisation). SHARP 1's data: CONFIRMED.
* Landau triple ⟺ (least min of an unforced word ≥ 3 or U = 0): 0 mismatches in (b) and in (a) (the author checked
  composites only to 2·10⁵).
* Landau depth histogram on (b): identical to §3 (356 992 / 96 788 / 7 619 / 1 965 / 715 / 153 / 37 / 6 / 8 / 4 / 1),
  least-min = K+1 at every K ∈ {2, 3, 6, 7, 9, 10}, exceedances 41/715 (K = 4), 29/153 (K = 5), 3/8 (K = 8),
  maximal excess 9 — exact match.
* Profile split of p+1 (b): odd-exp 320 343 / 0.564 / 0 failures; clean 107 296 / 0.600; 3²: 25 666 / 0.475 / 3;
  other-even 10 983 / 0.549 — exact match. Composites (a): odd-exp 754 595 / min 0.545 / 0; clean 414 515 / 0.56;
  3²: 49 890 / 0.454 / 6; other-even 29 419 / **0.505** / 0. The proposed CONJECTURE (N₋ ≥ U/2 when n+1 has a ψ-odd
  prime of odd exponent) survives on composites < 10⁷ (min 0.545); "other even profiles" come within 0.005 of failing.

## Claim 4 — Lemma 2.1 and Flip Lemma 2.2: SOUND-AFTER-REPAIRS (D4, MINOR)
Re-derived: ψ(N_u) = ((n+u)/n) = ψ(u), ψ(N_t) = ψ(1); ψ(A)ψ(B) = ψ(tn+1) = 1 and ψ(A)ψ(v) = ψ(u) give
ψ(u)ψ(v) = χ **provided ψ(u) ≠ 0**. Cases (a)–(c) are right. Flip Lemma: the parametrisations D ↦ word are right
(for X = t, AB ≡ 1 (mod t) makes B ≡ −1 automatic), and both moves preserve D mod X and flip ψ(D). The worry
"ψ(s) = 0" in the swap move cannot occur: s | n and s | N_u forces s | u, and then r ≡ s (mod u) forces s = r.
Numerics: Σ(U − N₋) over primes p ≡ 1 (8) < 2·10⁵ from my census = 94 262, matching the author's word count.
"Flippable ⟹ family certificate, 0 exceptions" is implied by the lemma (not independent evidence).
**D4 (MINOR).** §2 Lemma 2.1 is stated for the general (Jacobi) setting but ψ(u)ψ(v) = χ fails when gcd(u, n) > 1
(then also gcd(v, n) > 1, both symbols 0, while χ = ±1): e.g. n = 105, w = (1, 3, 54), χ = +1, ψ(3) = ψ(54) = 0. Such
words fall outside (a)–(c). For prime n ≥ 5 this never happens (u = pa, v = pb gives tpab − a − b = 1, impossible).
Repair: add "gcd(uv, n) = 1 (automatic for prime n)". Also the last sentence of Lemma 2.1 ("a congruence covering
cannot supply it … B1-type") is an Assessment inside a PROVED lemma; label it so.

## Claim 6 — U2 sandwich (PROVED) and CONJECTURE U2 (EVIDENCE): SOUND
N₋ ≤ U2: certificates have ψ(A) = ψ(B) = −1. U2 ≤ U: A | N_t, N_u and B | N_t, N_v, so A, B unclean makes every side
unclean. Census confirms (0 violations, U2 = 0 only at 105 for all n ≡ 1 (8) < 10⁷). The n ≡ 5 (8) word
(1, 3, (n+3)/2) is right (A = 2, B = (n+1)/2, both ψ = −1). Note the document writes "(1, 3, (n+1)/2 + 1)", equal.

## Claim 8 — Prop 5.1 (2-adic Haar mass 3/4): SOUND
`scripts/review_r233_haar.py`: for k = 2…7 and **every** odd class p mod 2^k, #solutions = 5·4^{k−1} (k = 5: 1280)
and the five-slice share is exactly 0.75 — also for p ≡ 3 (4), where the five-slice set is not the certificate set.
Conceptual proof (stronger than "finite computation"): the gradient (uv, B, A) never vanishes mod 2 on the 5 points
mod 2 (A ≡ B ≡ 0 forces t, u, v odd, so uv odd), so X_p is ℤ₂-smooth and every point mod 2^k lifts to exactly 4 points
mod 2^{k+1}; the five-slice condition depends only on w mod 4, so its share is constant for k ≥ 2. The identification
"five-slice = certificate" for positive words at n ≡ 1 (4) is the three-bit law (SPARKS4 §1); my Lemma 5.2 script
also checks it directly on all automatic-family words for n ≡ 1 (4) < 2·10⁴ (0 mismatches).

## Claim 9 — Lemma 5.2: SOUND
Re-derived: Σ_{D|X} ψ(D) = ∏_r Σ_{k ≤ e_r} ψ(r)^k (X coprime to n, so no ψ = 0 primes for X ∈ {n+1, n+2, 2n+1}), and
#cert = (τ − Σψ)/2. `scripts/review_r233_lemma52.py 20000`: all six automatic families of every odd non-square
n ≡ 1 (4) < 2·10⁴ (29 568 families), words found by *direct search* (not via divisors): |family| = τ(X) always and
0 mismatches with the formula. "N₋(F) ≥ U(F)/2 when a ψ-odd prime has odd exponent" follows since U(F) ≤ τ.

## Claim 11 — 105 genus collapse, Lemma 6.1: SOUND-AFTER-REPAIRS (D5, MINOR)
`scripts/review_r233_105.py`: 11 words, all χ = +1, side primes {2, 3, 53, 79, 107, 211}; every word has exactly two
ε_ℓ = (−A/ℓ) = −1, at {3, 7} or {5, 7}, matching THREE_SQUARES §5; (107, 1, 1) has (−1, +1, −1) ✓. Lemma 6.1 proof is
right (A or B divides N_X; (A/ℓ) = (B/ℓ) since AB ≡ 1 (mod ℓ)). Every word of 105 has the side 106 = 2·53 with
(2/7) = (53/7) = +1, so Lemma 6.1 forces ε₇ = (−1/7) = −1 on all 11 words — the explanation works.
**D5 (MINOR).** §6: "every prime factor of every side of all 11 words … has (r/3) = (r/5) (and (r/7) = +1)" is false
for r = 3, which divides the sides 108 and 159 of (1, 3, 54), (1, 54, 3): (3/3) = 0, (3/5) = −1, (3/7) = −1. It is
harmless (ψ(3) = 0 counts as clean, and those words also have the side 106). Repair: "every prime factor r ∤ 105 …".
