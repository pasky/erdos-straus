# R222 — hostile review #1 of O219 (STERILE_EXPLICIT.md)

Reviewer: R222 side agent (worktree branch side-agent/review-sterile-explicit, merged side-agent/sterile-explicit at d539a4a2).
Status: IN PROGRESS. Scripts: `scripts/review_se_*` (from scratch; none of the author's code is imported).

## Summary verdicts
(filled at the end)

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
RESULTS_PLACEHOLDER
