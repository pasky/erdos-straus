# R222 — hostile review #1 of O219 (STERILE_EXPLICIT.md)

Reviewer: R222 side agent (worktree branch side-agent/review-sterile-explicit, merged side-agent/sterile-explicit at d539a4a2).
Status: round 1 complete.
**Repairs applied** (author quiet ≥ 2 h): m1–m8 applied directly to STERILE_EXPLICIT.md (marked "(R222 repair mN)"; §5 moved after §3.4)
and m4/m6/m7 to AGENT_REPORT_O219.md. No mathematical content or certified number changed. Scripts: `scripts/review_se_*` (from scratch; none of the author's code is imported).

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 3.4 (every prime r ≥ 2³²: sterile points in the non-residue cells; no finite ET covering for least QNR r) | **SOUND** (MINOR text repairs m1–m4) |
| §3.1 reduction to (S) (inputs, r-uniformity, "for every r ≥ 2³²" quantifier) | **SOUND** |
| se_box.c route bounds / rounding / λ = 2^s boxes; se_tail.py all-N tail; se_r0.py combiner | **SOUND** (13 cells independently re-certified; independent combiner max Ŝ = 0.48668; λ = 2…16 per-box validation 0 violations) |
| Lemma 1.1, 1.2, Q identities | **SOUND** |
| Lemma 1.3, Cor 1.4 finite form | **SOUND**; asymptotic n^{max(0, β(1−β)−ρ)+o(1)}: **SOUND-AFTER-REPAIRS** (m5) |
| "P-count exponent 2/5 with only a τ₃ envelope, tolerated up to η = 0.3" | correctly **EVIDENCE** (grid); reproduced from scratch (θ* = 0.400 for η ≤ 0.3, 0.417, 0.450, 0.500 at 0.35, 0.4, 0.5); wording m6 |
| Dictionary O216 Case B ↔ ℤ P-data | **SOUND-AFTER-REPAIRS** (m7: equations coincide; side conditions do not — "literally" overclaims) |
| r = 13 (all six non-residue cells covered at level 1), r = 17 (cells 5, 7 survive; out of reach) | **SOUND** (level 1 recomputed from scratch) |
| Labels | SOUND-AFTER-REPAIRS (m4, m6, m8) |

No FATAL, no MAJOR.

## 1. Reduction sterility ⇐ (S) (§3.1, Thm 3.4 first half)

Re-derived from M17 Lemmas 1.1, 1.3, 2.1–2.3, 5.1, 5.2, M17B Lemma 1.1, M17C Lemma 2.1(iv), Cor 4.2, with r a general odd prime:
* Box types: P (ball −f_ET mod r^{⌈K/2⌉} for an N-point of Σ^II_{r^K} with r∤cd; nested union, M17 Lemma 2.3), Q (−4a²d ≡ −a/b
  mod r^k, M17 Lemma 5.1(i) under r∤e only), Q⁻¹ (= reflection a↔b of Q, so Q⁻¹ = Q as sets), √Q (empty: the Jacobi argument of
  M17 Lemma 1.3 is at the odd modulus f ≡ −1 (mod 4d), no residue symbol at r is used — also not needed for an upper bound), U, U⁻¹
  (inside P-boxes by M17 Lemma 5.2: the auxiliary datum (b′, c′, a′, i) of Σ^II_{r^{α−β}} is r-free in all four entries, so it is
  one of the data counted by D_P, and P is inversion-closed). Every step is r-free. I re-checked the reflection: Σ^I and Σ^II are
  symmetric in (a, b), so the factor 2 per a ≤ b datum is right (a = b is over-counted, harmless).
* Primitivity used by the engines: P in-cell ⇒ r∤ab (r|a ⇔ r|b by 4abcd = a+b+Nc with r∤c; then f ≡ −1, centre ≡ 1 is a residue);
  Q-datum ⇒ 4abd = eF+1 ⇒ r∤abd, and r|c ⇒ a ≡ −b ⇒ centre ≡ 1. So D_P, D_Q may legitimately be restricted to r∤abcd(e).
* Parity: K and k odd follow from the r-free reciprocity argument (and even levels could simply be included; they are 0).
* Measure: non-residue cells have Haar measure (r−1)/(2r) in ℤ_r; a P-box of level (K+1)/2 has measure r^{−(K+1)/2}, a Q-box
  of level k measure r^{−k}. Countable union of clopen balls of total measure < (r−1)/(2r) leaves a non-residue point uncovered.
* Cor 4.2 for general r: the clopen-neighbourhood + Dirichlet argument with 8·∏_{q<r} q | Q (R187 version) gives primes
  ≡ 1 mod every q < r and ≡ u (non-residue) mod r, i.e. least QNR exactly r. ✓
* Quantifier "for every prime r ≥ 2³²": se_r0 walks r-ranges [2^b, 2^{b+1/4}), b = 32, …, 600 (2273 ranges), bounding
  D(r^K) by the max of table cells meeting [2^{Kb}, 2^{K(b+1/4)}) and the weight by its value at 2^b; table bounds hold
  for *every* N in a cell (no r-dependence besides N = r^K and in-cell primitivity). For r ≥ 2^{600.25} every N = r^K is in the
  tail range and each weighted tail monomial c·r^{Ke−(K+1)/2}(K ln r)^p (resp. c·r^{K(e−1)}(K ln r)^p) has ln r-derivative
  K(e−h) − [h=½: ½] + p/ln r ≤ 0 because p ≤ (h−e)·ln N₀ ≤ (h−e)K ln r. So the finite grid + monotonicity covers all r. ✓
  (The 1e−20 geometric remainder is justified in the self-review; I agree with its ratio estimate.)

**Verdict on the reduction: SOUND.** Wording defect (MINOR, see D-list): §3.2 says se_box bounds D_P(N), D_Q(N) "for every
odd N"; the unit-class routes (F, G, I, J, Ea, Ed, AC, CD, f-routes) need gcd(e, abd) = 1, gcd(F, acd) = 1, which hold for
N = r^K with in-cell (r-free) data but not for general odd N.

## 2. Lemmas 1.1, 1.2 (identities, sizes) and the Q identities of §3.2

Re-derived by hand (all one-line expansions) and brute-forced from scratch: `scripts/review_se_lemmas.py` enumerates all
P-data of N = r^K for 12 (r, K) (incl. 3⁹, 7⁷, 17⁵, 101³) and all N-points of Σ^I_F for 11 (r, k) (incl. F = 23³, 1009, 9973),
and checks Lemma 1.1(i)–(iv), Lemma 1.2 with dyadic A, C, D, the facts used as pruning/windows by se_box/se_tail
(2a²d ≤ N, acd ≤ N, e ≤ N, N < 4acde ≤ 2(N+e); Q: cd ≤ F, 0 < f ≤ F+2, e, f odd, ≤ 2 points per (a, d)), the unit-class facts
(gcd(e, abd) = 1, gcd(f, F) = 1, gcd(F, 4ac) = 1 for in-cell data), the f-route congruences c ≡ −aF, a ≡ −cF⁻¹ (mod f), and the
box centres −f ≡ −a/b (P, mod r^{(K+1)/2}) and −4a²d ≡ −a/b (Q). **0 failures.** It reproduces D_P(17³) = 32, D_P(17⁵) = 121,
D_Q(17³) = 73 (M17's two-engine values), and finds no Q-point at the even level 101². **Verdict: SOUND.**

## 3. Lemma 1.3 and Corollary 1.4 (Coppersmith interpolation)

*Proof re-derived.* n₁ (s-free part) keeps every unit-class divisor; F(y) = y + x̂ + σ₀t satisfies sF(y) ≡ E (mod n₁) so E | F(y_E);
g_i = n₁^{m−i}F^i, h_j = y^jF^m all vanish to order m at y_E modulo E; the coefficient lattice (scaled by X^l) is triangular
with determinant n₁^{m(m+1)/2}X^{w(w−1)/2}; Minkowski with the closed cube gives a nonzero g with Σ|g_l|X^l ≤ w·det^{1/w}
< D₀^m ≤ E^m, hence g(y_E) = 0; |y_E| ≤ X since the x-interval has length (D₁−D₀)/s and x̂ is within ½ of its midpoint. No LLL
loss is needed because nothing is searched. Cor 1.4: J sub-windows of length (D₁−D₀)/J, each with the common lower bound D₀;
using a lower bound s_min ≤ s only enlarges X (monotone in (Cop)). Asymptotics: with w = τm, δ = β−ρ−j, (Cop)/(m² log n) →
½ + τ²δ/2 − τβ, minimised at τ = β/δ to ½ − β²/(2δ) < 0 ⇔ ρ + j > β(1−β). Correct for 0 < β < 1, δ > 0 (δ ≤ 0 is the
trivial window/s + 1 regime); m → ∞ slowly absorbs the w log w and m(m+1)/2 − m²/2 terms.
*Test (from scratch, exact integers):* `scripts/review_se_cop.py 30000 150 8` — for every n ≤ 30000, s ≤ 150, unit class, and
every run of t ≥ 2 consecutive class-divisors with the *tightest* window D₀ = first, D₁ = last, it checks that (Cop) fails for
every (m, k) with w − 1 < t (Lemma 1.3) and for every J ∈ {2, 3, 4} with J(w−1) < t (Cor 1.4): 2.1·10⁸ adversarial evaluations,
**0 violations**; closest approach log(RHS/LHS) = −0.75 (n = 30000, s = 1, divisors 1200, 1250, m = 1, w = 2).
**Verdict: Lemma 1.3, Cor 1.4 (finite form) SOUND; asymptotic form SOUND-AFTER-REPAIRS (state 0 < β < 1, treat δ ≤ 0
separately — the self-review's m4 point, still not repaired in the text).** Attribution (MINOR): the size-restricted
divisors-in-residue-classes bound is in Coppersmith–Howgrave-Graham–Nagaraj (Math. Comp. 77 (2008)), and cutting the
window into pieces below the threshold is standard there/Lenstra; "new to the campaign" is fine, but the text should cite CHN
rather than suggest novelty (not in sources/; I could not check the exact CHN statement).

## 4. Numerics of Theorem 3.4

### 4.1 se_box.c route bounds (code audit, every line of boxP/boxQ/cop/lC/Omega/main)
Re-derived each route from the identities (not from the author's comments):
* **P** (box a∈[A,λA), c∈[C,λC), d∈[D,λD), λ = 2^s exact): pruning 2A²D > N₁ or ACD > N₁ (valid: 2a²d ≤ N, acd ≤ (N+e)/(2e) ≤ N);
  E₀ = N₀/(4λ³ACD) < e (e ≥ b/c > N/(4acd)), e ≤ N/(acd) ≤ E₁, b ∈ (N₀/(4λ²AD), N₁/(2AD)], f ∈ [4ACD−1, 4λ³ACD); se = ⌊E₀⌋+1.
  H (triples), A (e ≡ −N mod 4ad, Σ1/a ≤ 1/A + ln λ), C (f | N+4a²d ≤ 3N, class −1 mod 4ad), D (f | 4c²dN+1 ≤ 4λ³C²DN₁+1),
  E (f | Nc+a), F (pairs (e,a) with 4a | N+e; b or d in a unit class mod e of m = (N+e)/(4a) ≤ (N₁+E₁)/(4A)), G (pairs (e,d);
  a² ≡ −m mod odd e, ≤ 2^{ω(e)} unit roots; Omega(E) = 2^{#odd primes with primorial ≤ E} ≥ max 2^{ω(e)} over odd e ≤ E),
  τ₃ (e ≡ −N mod 4, ordered abd = (N+e)/4), I (c, e, a ⇒ b, d), J (c, e, d ⇒ a root of x² − cex + m: ≤ 2; the extra Omega
  factor is harmless) — **all valid**. Row aggregation (fixed (a,d): datum ↦ f | N+4a²d injective) valid.
* **Q** (box c, d, f; a = (f+F)/(4cd)): cd ≤ F (2abcd ≤ c(4abd−1) = F(a+b) ≤ 2Fb), f ≤ F+2 (f = (aF+c)/b, c ≤ 2b); windows a₀,a₁,
  E₀ = 4a₀²D/(λP) < e, E₁, b₀ = max(a₀, E₀F₀/(4a₁λD)), b_max; AD (M17C 2.1(iv): s = 4ad, s² > 4a²d+1, one divisor below √t and one
  cofactor below √t, both in fixed classes — re-proved), fa, AC (class −F mod 4ac, unit since r∤ac), CD, Ea, Ed (e odd since
  eF+1 = 4abd), τ₃, fac/fca/fda (c ≡ −aF, d ≡ −(4a²)⁻¹, a ≡ −cF⁻¹ mod f; f odd, gcd(f, F) = 1) — **all valid**; row (c,d) valid.
* **cop()**: trivial ⌊Δ/s_min⌋+1; τ envelope C₂(η)n^η (lC: primes p > k^{1/η} contribute 1 because binom(j+k−1,k−1) ≤ k^j; the
  j-scan stops correctly because j ↦ log binom − ηj log p is concave); Cor 1.4 with J chosen from X_max and **(Cop) re-checked for
  that J** with relative margin 1e−12 and s_min ≤ s (monotone). Valid.
* **Floating point.** Box corners and λ are exact powers of 2 (g = 1 enforced, s integer); all window ends are padded outward by
  a relative 1e−15 ≫ the ~1e−19 relative error of a few long-double ops; floor/ceil only of padded quantities; the τ constant
  has +1e−12 in the log. Integers > 2⁶⁴ never need to be exact except powers of two. I find the error budget in the header
  adequate (MAJOR M1 of the self-review is repaired). Residual MINOR: the glibc x87 `powl/logl/expl` accuracy is an assumption
  (documented); N₀ = DN(powl(2, j/q)) is the only non-dyadic corner and is padded.
* **Coverage.** imax = ⌈(log₂N₁+2)/s⌉+1 covers a, c, d ≤ N (P) and c, d ≤ F, f ≤ F+2 (Q); the early `break`s fire only on boxes
  that are empty for every larger index. Half-open dyadic boxes partition the data. ✓

### 4.2 Independent re-certification of cells (from scratch, `scripts/review_se_cell.py`)
My own engine (Python, dyadic λ = 2 boxes, integer windows, rational arithmetic, **exact** max τ(n), max τ₃(n) over n ≤ X via
Hardy–Ramanujan exponent patterns up to 2¹³⁰ (my own C_k(η) envelope beyond), Coppersmith candidates verified in exact integer
arithmetic, routes as re-derived in 4.1) bounds D_P(N) / D_Q(F) for **every** integer in the cell. If my (valid) bound ≤ the
author's table value, the author's value is independently certified. Results (author / reviewer):
| cell (bits) | P: author / reviewer | Q: author / reviewer |
|---|---|---|
| j=128 (32–32.25) — the binding r-range | 5.282e7 / 4.632e7 (1.140) | 7.526e8 / 7.239e8 (1.040) |
| j=129 | 5.162e7 / 4.872e7 (1.060) | 8.207e8 / 7.925e8 (1.036) |
| j=131 | 7.349e7 / 5.416e7 (1.357) | 1.090e9 / 1.055e9 (1.033) |
| j=160 (40) | 9.363e8 / 8.185e8 (1.144) | 2.339e10 / 2.263e10 (1.033) |
| j=200 (50) | 2.630e10 / 2.323e10 (1.132) | 1.471e12 / 1.435e12 (1.025) |
| j=300 (75) | 5.166e13 / 4.688e13 (1.102) | 4.587e16 / 4.571e16 (1.004) |
All 12 cells above, and P j = 600 below: **author ≥ reviewer, so these cells — including the one carrying 0.375 of the 0.487 at b = 32 (Q k = 1 and
P K = 1) — are independently certified.** With my bound the level-1 Q term at r ∈ [2³², 2^{32.25}) is 0.337 (author 0.350).
Replay: the author's se_box (hashes match MANIFEST.txt) reproduces P j = 128–131 and Q j = 128, 129 bit-for-bit.
*Box ratios λ > 2.* All P_q1 cells (bits 200–600) and P_q4 j ≥ 512 use λ = 2^s, s = 2…9, a code path the author's
`se_box_check.py` never exercised (it runs s = 1). `scripts/review_se_boxcheck.py` runs the author's binary in SE_EXACT/SE_DUMP
mode with s = 1, 2, 3, 4 for P at N = 17⁵, 7⁷, 3¹³, 101³, 23⁵ and Q at F = 17³, 23³, 9973, 99991, 7⁵, buckets the reviewer's exact
enumeration into the dumped boxes and rows: **0 violations** (every occupied box and row dumped and bounded). I could not
independently re-certify a λ ≥ 8 cell at its real size (bits ≥ 192: ~10⁶ boxes in my exact-arithmetic Python); one λ = 4 cell
(P j = 600, bits 150, author λ = 4) gives author 5.926e22 / reviewer 4.758e22 (1.246): OK.

### 4.3 Combiner (from scratch, `scripts/review_se_combine.py`)
Independent of se_r0.py: exact rational location of table cells, per-monomial maxima of the tail list over each N-range (handles
the seven negative-exponent Q monomials exactly instead of capping), explicit geometric remainder with the monomial-wise ratio
2^{2(max(e,0)(b+¼) − hb)}((K+2)/K)^p computed at the stopping index, mpmath/float64-log evaluation with 1e−9 inflation.
Over all 2273 ranges b = 32, …, 600: **0 failures, max Ŝ = 0.486679 at b = 32** (author 0.486702; the difference is the
author's extra (1+1e−6) and capping). Top terms at b = 32: Q₁ 0.3504, P₁₉ 0.0923, P₁ 0.0246, P₂₁ 0.0143, P₃ 0.0023, P₂₃ 0.0022
— so "P tail ≈ 0.1" in §3.4 is right, and the margin 0.0133 is ~2.7% of S.

### 4.4 se_tail.py (all-N tail): audit
Line-by-line (same derivation work as 4.1, now with normalised boxes N^{x}, u = 1/M, valid for every N ≥ N₀ because each bound is a
fixed finite list of monomials with box-independent constants):
* P (M = 32, N₀ = 2^600): capped exponents (a ≤ N^{(1−x_d)/2}, d ≤ N^{1−2x_a}, acd ≤ N) valid; pe = ¼N^{1−s₃}; Σ1/a ≤ 1 + u ln N ≤
  (1/L₀ + u) ln N for N ≥ N₀; f ∈ [3N^{s₃}, 4N^{s₃′}]; n ≤ 3N (C), ≤ 5N^{1+2x_c′+x_d′} (D), ≤ 2N^{1+x_c′} (E), m ≤ ½N^{1−x_a}
  (F), ½N^{1−x_d} (G); e ≥ ¼N^{1−s₃′}; b ∈ [¼N^{1−x_a′−x_d′}, ½N^{1−x_a−x_d}]; 2^{ω(e)} ≤ C_ω(0.1)e^{0.1} with
  C_ω = ∏_{p<1024}2p^{−0.1} over primes with p^{0.1} < 2; τ₃ factor C₃(0.3)(N/2)^{0.3}. All valid.
* Q (M = 16, N₀ = 2^100): a ≤ ½N^{1+u−x_c−x_d} (uses f ≤ F+2 ≤ N^{1+u}), a ≥ ¼N^{1−x_c−x_d−2u}; the AC integer
  aF + c ≤ 1.51N^{2−x_c−x_d} ≤ N^{2+u−x_c−x_d} (needs c ≤ F/d ≤ N^{1−x_d} and N^u ≥ 1.51 — true, N^u ≥ 2^{6.25}, but this
  argument is **not written anywhere**; MINOR); CD n ≤ 5F² (c²d ≤ (cd)² ≤ F²); fac Σ_{a₀≤a≤a₁}1/a ≤ 1 + ln(2N^{3u}) ≤ 1 + ln 8 + 3u ln N;
  fca, AD valid.
* tail cop(): the linear-in-L argument (g(L) = g₀ + s₀(L−L₀) < 0 for L ≥ L₀; J = ⌈N^κ⌉ with κ ≥ k₁ (slope) and κ > k₂ (value);
  then window/(sJ) < X_max, X_J < (X_max+1)/2 < X_max) is correct; count ≤ (w−1)(N^κ+1) is what is emitted. ✓
* Decrease in r and the r ≥ 2^{600.25} extension: see §1. ✓
**Verdict on the numerics: SOUND** (MINOR documentation defects below).

## 5. Other claims

* **r = 13, 17** (`scripts/review_se_level1.py`, from scratch): level-1 centres −a/b mod r of P-data of N = r and Q-points of
  F = r (both orientations): r = 13 covers all of {2, 5, 6, 7, 8, 11}; r = 17 covers {3, 6, 10, 11, 12, 14} and leaves {5, 7}. ✓
  The "constant ≲ 2.5 at θ = 0.4" is M17D line 70 (pointwise 2.48). ✓ (Scope "in a non-residue cell" is now stated. ✓)
* **Continuum 2/5** (`scripts/review_se_rate.py`, from scratch, my own route exponents from Table 2 + Cor 1.4): reproduces the
  claimed θ*(η) exactly, binding point (1/5, 1/5, 1/5, 2/5) for η ≤ 0.3; dropping C, D, E or τ₃ gives 0.5, dropping F or G
  0.433, dropping A or I nothing — consistent with "five class routes + τ₃". It is a grid maximum (EVIDENCE), as labelled.
* **Dictionary** (FF_STERILE_PUSH (B), Lemma 1.1): m′wC = T^s + v, w + C = g′v ↔ 4d·a·b = N + e, a + b = ce and
  E = g′m′w − 1 ↔ f = 4acd − 1, Ev = T^s + m′w² ↔ ef = N + 4a²d are exact. But (B) has T ∥ w, T ∥ C (and T² | v), and even the
  reduced tuple (m′, Tg′, w₁, C₁, v₁) has T | (c-twin); the ℤ in-cell data have r ∤ abcde. So the twins are the *equations and
  routes*, not the counted sets (FF slices sit at the centre 1, ℤ cells at non-residues). See m7.

## Defects (all MINOR; none affects the truth of Theorem 3.4)

* **m1** (§3.2 first sentence; also se_box.c header "valid for EVERY odd N"): the table bounds hold for N = r^K / F = r^k with
  in-cell data (unit classes need gcd(e, abd) = 1, gcd(f, F) = 1 — Lemma 1.1(iv) uses N = r^K and r ∤ abd), not for every odd N.
  *Repair:* "for every N = r^K (r an odd prime, any K) in the range, counting in-cell (r-free) data".
* **m2** (§3.3 / se_tail.py docstring): the Q-tail AC integer bound aF + c ≤ N^{2+u−x_c−x_d} uses c ≤ F/d and N^u ≥ 1.51; the
  P/Q tail validity arguments (windows, capped exponents, the linear-in-L Coppersmith argument with κ ≥ k₁, κ > k₂) are only in the
  self-review. *Repair:* add a five-line "why each tail term is valid" paragraph to §3.3 (can be copied from §4.4 here).
* **m3** (§3.4 "→ 1/2 as r → ∞"): not given by the certificate (which shows S ≤ S(2^600-range) beyond). *Repair:* cite (J)26
  Thm 3.1 / note that each weighted tail monomial → 0 and the series is uniformly geometric.
* **m4** (stale text, self-review m4 not fully applied): §5 still sits between §3.3 and §3.4; §0 (I1) cites a nonexistent
  "Table 1.2"; Prop 2.1 still says the Q grid is a "/tmp-prototype, to be committed" (it is `scripts/se_rateQ.py`) and that it is
  "to be replaced by the certificate of §3" (the certificate proves exponent ≤ 0.4797 on the tail, not 2/5); the report says the
  engine's bound/√N peaks ≈ 820 near 2⁴⁰ — the certified P_q4 table peaks at 931 (j = 155, N ≈ 2^{38.75}).
* **m5** (Cor 1.4 asymptotic): add "0 < β < 1, fixed β, ρ; m → ∞ slowly; if β − ρ − j ≤ 0 use the trivial bound". Cite
  Coppersmith–Howgrave-Graham–Nagaraj (Math. Comp. 2008) for the size-restricted divisors-in-classes lattice; "new to the campaign" OK.
* **m6** (§0 (I3), report SHARP 3: "no divisor-function loss except a τ₃ envelope"): route G also uses 2^{ω(e)} (N^{o(1)}, charged
  as C_ω e^{0.1} in the tail). *Repair:* "no τ-loss except τ₃ and 2^{ω(e)} ≤ N^{o(1)}"; keep "(grid EVIDENCE)" next to "exactly 2/5".
* **m7** (§0 (I1), §1 notation, report SHARP 5: "literally the ℤ P-data", "Every FF route has a ℤ twin"): replace by "the defining
  equations and the reconstruction identities coincide under (m′, g′, w, C, v) ↔ (4d, c, a, b, e), T^s ↔ N; the side conditions
  differ (FF: T ∥ w, C, T² | v; ℤ in-cell: r ∤ abcde), so counts and box geometry do not transfer literally".
* **m8** (labels): Thm 3.4 "PROVED, computer-assisted" is acceptable; for the house style add "(tables CERTIFIED, data/se/,
  MANIFEST)". Also note that the floating-point argument assumes glibc x87 libm accuracy of a few ulp (stated in se_box.c, not in §3.2).

## Not done / limits of this review
* I did not rerun the 3.5 h certificate. I re-certified 12 table cells independently (bits 32–75); the λ ≥ 4 cells (P bits ≥ 128
  in P_q4, all of P_q1) were validated only by the small-N per-box test (λ = 2…16) and by code audit; P j = 600 (author λ = 4) was re-certified (13 cells total).
* The tail monomial lists were produced by the author's se_tail.py (fed as data to my combiner); their derivation is checked by
  audit (§4.4), not by an independent implementation.
* CHN (2008) and Browning–Elsholtz were not available in sources/.
