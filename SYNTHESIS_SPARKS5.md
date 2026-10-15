# SYNTHESIS_SPARKS5 — cross-combinations of wave Y ((J)39–(J)56) (task O230, synthesis V)

**ES is not solved here, and no infinite case of it is claimed.** Labels as in DISCOVERIES.md. Memos:
`BRAINSTORM/s5_*.md`; scripts `scripts/s5_*`. Notation as SYNTHESIS_SPARKS4: words w = (t, u, v), tuv − u − v = p,
A = tu − 1, B = tv − 1, AB = tp + 1, A·v = p + u, B·u = p + v, χ(w) = (−A/p); ψ(r) := (r/p).

## 0. Iteration log
(I1) Start: (J)53/(J)55 explain near-square hardness on the t-side only; R225's spark S2 (depletion on unclean levels)
is open. Observation: each word sits on three "side numbers" N_t = tp + 1 = AB, N_u = p + u = Av, N_v = p + v = Bu, and
on each one χ is the restriction of a genus character ((−t/·), (−u/·), (−v/·)). → §1.
(I2) Kill/steer: cleanliness only ever forces χ = +1 (anti-existence), so the three-side theory cannot produce a
certificate (B2). Construction pivot: use it the other way round, as an exact *explanation of hardness*, which is the
STATUS target "near-square hardness" ((J)53/(J)55, R225 spark S2). → §2.
(I3) A residual survives at K0 = 8. Hypothesis "square-defect sides deplete": REFUTED in general, but confirmed at
K0 = 8 as the *defective deformation* (gcd 3 forced by primality). → §2.
(I4) Pivot to per-prime structure: split words into forced/unforced. Hard primes = fully forced; N₋ ≈ ¾U. Tried to
upgrade to an exact inequality N₋ ≥ U/2 (would make ES-five ⟺ U ≥ 1). Held at all primes < 5·10⁶ (min 0.506), but
REFUTED at p = 5 270 849 and two more primes < 3·10⁷. → §3.
(I5) Mandatory combinations (ii)–(v): every one gave an exact dictionary and no forcing; the precise negative for
(ii)/(iii) is the locality lemma (Prop R). → §4.

## 1. Three side numbers (PROVED; memo s5_three_sides)
**Lemma S.** p ≡ 1 (4) prime. χ(w) = ψ(A) = ψ(B). For an odd prime r | N_X (X ∈ {t, u, v}), ψ(r) = (−X/r). If every
prime factor of N_X has ψ = +1 (side X *clean*), every word with that X-value has χ = +1.
**Side deformations.** p = m² + K: the t-side is clean if tK + 1 = c² ((J)53) and the u-side (v-side) if u(K + u) = □ (new
form; R225's K + u = s² is a different sub-case), under the gcd conditions, for p ≡ 1 (8). At K = 0 all sides are clean
(T1). t-side solutions form Pell-type infinite families; u-side ones are finite (≈ τ(K)).
**Lemma G** (s5_gcd_sides). gcd(tp + 1, p + u) = tu − 1 = A, so χ = ψ(gcd(N_t, N_u)): ES-five(p) ⟺ some pair of
side numbers has a ψ-odd gcd of the exact form tu − 1 (H-A in its purest form).

## 2. Near-square hardness: three-side cleanliness explains most of the residual (EVIDENCE)
Census `scripts/s5_sides.c` (169 410 primes p ≡ 1 (4) in (10⁵, 5·10⁶); 0 violations of Lemma S; the (10⁵, 10⁶) totals reproduce
ns_census exactly). Words on clean sides: t 2.31 M, u/v 3.54 M, any 4.25 M of 32.9 M. Within adelic cells (refined by
p mod 9, 16), the residual depletion of χ = −1 at 10 ≤ K0 < 300 drops by ≈ 70–80 % once all clean sides are removed
(t-side alone: ≈ 40 %). K0 = 16 and 24 are explained completely (−0.060 → +0.008, −0.169 → +0.014). Full table in
s5_three_sides.
**K0 = 8** keeps −0.074. Mechanism (EVIDENCE, `scripts/s5_defect.c`): primality forces 3 | m, so the deformation sides
(u = 1; t ≡ 1 (9) with 8t + 1 = □) are clean *except for an exact 3²*, ψ(3) = −1. 45 % of words at K0 = 8 lie on such
square-defect sides, with a χ = −1 rate of 0.485 (vs 0.784 on its other unclean words). Generic square-defect sides
are not depleted (0.743 vs 0.755), so the depleting object is the **defective deformation**, not square defect as
such (CONJECTURE D, tested only at K0 = 8).
Methodological note: refining cells by p mod 9 and 16 already moves the K0 = 8 residual from −0.137 to −0.094. The
earlier "beyond the adelic cell" residuals used Legendre-symbol cells only; prime-power residues matter at small K0.

## 3. Forced vs unforced words: a hardness law (EVIDENCE; memos s5_unforced_words, s5_scale_law) — SHARP (descriptive)
U(p) = #words with no clean side; N₋ ≤ U (PROVED, Lemma S).
* corr(N₋, U) = 0.966 over primes < 10⁶. All 13 hard primes of (J)48 (N₊ ≥ 4N₋) have N₊ − N_forced ∈ {0, 2}, and every
  dyadic block's least-N₋ prime up to 3·10⁷ has forced fraction 0.55–0.89 (median ≈ 0.12) with N₋ = U or nearly.
* **Scale law.** N₋/U = 0.747 → 0.754 (2¹⁰ to 2²⁴, 928 779 primes, 220.7 M words), stable per class
  (0.770 at p ≡ 1 (8), 0.739 at p ≡ 5 (8)). N₋/N drifts 0.59 → 0.67, and the drift is the forced fraction ≈ 0.5/√log p.
  At a prime, the certificate lottery runs only over unforced words, with a stable success rate ≈ ¾ per word, the
  (J)39 cell average.
* **CONJECTURE U.** For odd non-square n ≡ 1 (4): U(n) = 0 ⟺ n = 105. EVIDENCE: `scripts/s5_U.c`, all n ≤ 2·10⁵ (Jacobi
  ψ; T1 control: at squares all sides are clean by definition, U = 0). Weaker than SQ₅ (N₋ ≤ U) with the same exception.
* **N₋ ≥ U/2 is REFUTED.** It holds at all primes ≡ 1 (4) below 5·10⁶ (min 0.506) and fails at 5 270 849 (192/389),
  17 188 937, 21 387 257 and at the composite 110 897. So there is no pairing of unforced χ = +1 words with certificates.

## 4. Mandatory combinations (ii)–(v): verdicts
| combo | memo | result | label |
|---|---|---|---|
| (i) ℤ³ × near-square deformation | s5_three_sides | the deformation is the binary (norm-form) shadow of (J)48's ternary embedding, on three sides; no canonical non-embeddable lattice from unclean levels (B2) | PROVED + EVIDENCE |
| (ii) Maslov/Dedekind index × SQ_± | s5_reciprocity_forcing | Prop R: every local-invariant index of a word is a function of (w mod 8, sgn w), so index sums are cell-occupation counts; reciprocity relocates signs, never creates points | PROVED (negative, exact scope) |
| (iii) ℚ(√j) T1 × ℤ[ω] order-3 T1 | s5_reciprocity_forcing | anti-T1 exists only as the five-slice cells themselves (= ES); a field forcing χ = −1 on a whole family = a B1 covering | PROVED/Assessment |
| (iv) Frob = c_∞ × (h±1) × supersingular | s5_cm_frobenius | certificate primes split completely in the CM field F_M = ℚ(ζ_M)⁺(√(p(θ²−4))) with Frob = c_∞σ_p; T1 = the twisted conjugation ceases to exist; Chebotarev + divisibility = B2 | PROVED dictionary |
| (v) FF vs ℤ sterility | s5_sterile_uniform | one profinite statement; the unavoidable global input is the size/degree coupling of the certificate modulus, not sign (SQ_±) and not congruences | PROVED (formal) + Assessment |

## 5. Verdict
No existence mechanism. The new results are on the hardness side: (a) three-side cleanliness (PROVED) explains most of
the near-square depletion and all of it at K0 = 16, 24, with K0 = 8 traced to a defective deformation; (b) the
forced/unforced split turns the sign lottery into a scale-stable ¾-per-unforced-word lottery whose hardness is the
forced fraction; (c) the tempting exact inequality N₋ ≥ U/2 is false. Combinations (ii)–(v) end in exact dictionaries
with precise negative scope.

## 6. Numerics index (tiny outputs; heavy files only in /tmp)
| claim | script | range |
|---|---|---|
| Lemma S, side census | s5_sides.c, s5_sides_hardness.py | primes ≡ 1 (4), 5 < p < 3·10⁷; 0 violations |
| square-defect | s5_defect.c | (10⁵, 5·10⁶) |
| CONJECTURE U | s5_U.c | n ≡ 1 (4) ≤ 2·10⁵ |
| Lemma G | s5_gcd_check.py | p < 1500 |
| Prop C | s5_cm_check.py | p < 3000, h < 5000 |
Reproduce the scale table: `gcc -O2 -o s5_sides scripts/s5_sides.c -lm; ./s5_sides 5 30000000 | awk` (dyadic blocks of
columns 2, 3, 6), split into ranges as needed (≈ 6 min on 2 cores).
