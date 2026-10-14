# STERILE_EXPLICIT (O219) — independent hostile review #2 (R223)

Reviewer: R223 (side agent, branch side-agent/review-sterile-explicit-2). Round 1, document not edited.
Scope: STERILE_EXPLICIT.md as merged from side-agent/sterile-explicit; scripts se_box.c, se_tail.py, se_r0.py;
data/se/*. From-scratch scripts: scripts/review_se2_*.py. The parallel review (R222) was NOT read before writing this.

## Summary verdicts (filled in progressively)

(in progress)

## A. The reduction Theorem 3.4 → (S) → finite certificate (task focus (a))

**A.1 Sterility ⇐ (S).** I re-derived the chain for a general odd prime r:
* Box types: M17 Lemma 1.1 (general r: R187's re-derivation + brute force r ≤ 23 from the literal Prop 1.9 classes; I did
  not redo the literal-class brute force). Level-0 boxes are impossible (M17 Cor 2.4, r-free: 4/1 has no solution).
* M17 Lemma 1.3 is **used** here (√Q = ∅; Q only at odd k; P only at odd K; this is what lets (S) carry 2D_Q instead of the
  6f(r^k) of DEPTH_ASPECT §3, which explicitly says "Lemma 1.3 is not used"). I re-derived it for general r: the proof uses
  only Jacobi symbols at f and g ((−1/f) = −1, (d/f) = 1 from f ≡ −1 (mod 4d), (−d/g) = 1 from g | 4a²d + 1, hence
  (−d/r)^k = −1; for P, (r^K/f) = −1). r-free. ✓
* M17 Lemma 5.1 (Q-box ≡ −a/b, P-box ≡ −a/b) and its in-cell consequences: for Q, r ∤ a, b, d always (4abd ≡ 1 mod F),
  r | c ⇒ box ≡ 1·(residue) (since a ≡ −b); for P with r ∤ cd, r | b ⇔ r | a and then −f ≡ −f' ≡ 1. Hence restricting D_P to
  r ∤ ab and D_Q to r ∤ abcde loses nothing **in the non-residue cells**. r-free. ✓
* U ⊂ P (M17 Lemma 5.2): both cases r-free (α > β: reduction to a Σ^II_{r^{α−β}} point (b', c', a', i) with r ∤ a'i; the P-box of
  level ⌈(α−β)/2⌉ = (K'+1)/2 is one of the two boxes counted for the ordered datum or its reflection; α = β impossible since
  4i ≤ 3). ✓ Q⁻¹ = Q as sets (reflection a ↔ b). ✓
* Weights: P-datum boxes of level (K+1)/2 (M17 Lemma 2.3: every (P)-datum box of level k lies in the box of its Σ^II point at level
  ⌈K/2⌉ ≤ k), Q-boxes of level k; Haar measure r^{−level}; non-residue cells have measure (r−1)/(2r). Total box measure < cell
  measure ⇒ a non-residue u in no box (positive measure of such u). Cor 4.2 for general r: the neighbourhood class
  {x ≡ u (r^L), x ≡ 1 (Q)} with 8·3·∏_{q<r} q | Q is primitive, contains infinitely many primes, all with least QNR exactly r
  (QR mod every q < r incl. 2 via p ≡ 1 (8); x_r ≡ u non-residue). ✓
* From-scratch brute force (`scripts/review_se2_identities.py`, all P-data for r^K ≤ 2·10⁶ and all Σ^I_F points for F = r^k ≤ 6000,
  13 primes 3 ≤ r ≤ 43): Lemma 1.1 (i)–(iv), Lemma 1.2 sizes, the Q identities, f ≤ F + 2, ≤ 2 Q-points per (a, d) (M17C 2.1(iv)),
  the three f-route congruences of §3.2, 4a, 4c, 4d | f + F, P-data only at odd K and Q-data only at odd k (in fact *no* data at all
  at even exponents), every in-cell Q-box a non-residue, the −a/b centres, and the in-cell exclusions: **0 failures**; it reproduces
  D_P(17³) = 32, D_P(17⁵) = 121, D_Q(17³) = 73 (M17).
Verdict A.1: **SOUND** (relative to M17 Lemma 1.1 for general r, which rests on R187).

**A.2 Quantifier "for every prime r ≥ 2³²".** How infinitely many r are covered (`se_r0.py`, re-read line by line):
1. r ∈ [2^b, 2^{b+1/4}), b = 32, 32.25, …, 600 (2273 ranges). For each odd K the term 2D_P(r^K)r^{−(K+1)/2} is bounded by
   (max over the table cells covering N ∈ [2^{Kb}, 2^{K(b+1/4)})) × 2·2^{−b(K+1)/2}: the tables bound D_P(N) for **every** integer N in
   a cell (se_box takes the box bounds at the cell's N-enclosure, and nothing in se_box depends on r), and the weight is maximal at
   the bottom of the r-range. Same for Q with weight 2·2^{−bk}. ✓
2. For N ≥ 2^{600} (P) resp. 2^{100} (Q) the tail term lists Σ c N^e (ln N)^p (all e ≥ 0, p ≥ 0 after the m1 capping, hence
   nondecreasing in N) are evaluated at the top N of the range. Cells straddling 2^{600} take max(table, tail). ✓
3. r ≥ 2^{600.25}: every N = r^K is in the tail, and d/d(ln r) of r^{Ke−(K+1)/2}(K ln r)^p is ≤ 0 iff p ≤ ((K+1)/(2K) − e)·ln N; the
   checked condition p ≤ (1/2 − e)·600 ln 2 implies it for all K ≥ 1, N ≥ 2^{600}. Likewise for Q (p ≤ (1 − e)·100 ln 2). So each term
   of S(r) is ≤ its value at b = 600, while (r−1)/(2r) increases. ✓
4. The per-range series in K: the loop stops when a tail term is < 10^{−30} and adds 10^{−20} "geometric remainder" without proof.
   True (successive odd-K tail terms decay by a factor ≤ 2^{2(b+1/4)·0.4797 − b}·((K+2)/K)^{p} ≤ 0.7 for b ≥ 32), but unstated: minor m-A1.
Verdict A.2: **SOUND** (minor m-A1). The quantifier is handled by a finite grid in log r plus a monotone tail, not by scaling.

**A.3 What the certificate actually depends on numerically at r ≈ 2³²** (decomposition with the author's own tables/tails,
`/tmp`-free recomputation in §C): S(b = 32) = 0.486702 = Q(k=1) 0.35044 + P tail (K ≥ 19, N ≥ 2^{600}) 0.10932 [of which K = 19 alone
0.0924, K = 21 0.0143] + P(K=1) 0.02460 + P(K=3) 0.00232 + P(K=5..17) 3·10⁻⁵ + Q(k≥3) 1.4·10⁻⁸. Margin to 1/2: 0.0133.
Remark (not a defect): the tail is extremely lossy against the tables — the *table* term at K = 17 (N ≈ 2^{544}) is < 10⁻⁶ while the
*tail* term at K = 19 is 0.092. Extending P_q1 to 2^{700} would remove ≈ 0.1 from S and is the cheapest way to lower r₀.

## B. Lemma 1.3 and Corollary 1.4 (Coppersmith interpolation via Minkowski)

Re-proved from scratch. Lemma 1.3: every E is prime to s, so E | n₁ (s-free part of n); with st ≡ 1 (n₁) and
E = σ₀ + s(x̂ + y), sF(y) ≡ E (mod n₁), so E | F(y) (gcd(E, s) = 1); E^m divides every element of 𝓛 = ⟨n₁^{m−i}F^i, y^jF^m⟩; the basis is
triangular in degree with leading coefficients n₁^{m−i}, 1, so det of the X-scaled coefficient lattice is n₁^{m(m+1)/2}X^{w(w−1)/2};
Minkowski's convex body theorem for the closed cube of volume 2^w·det gives g ≠ 0 with all |g_l|X^l ≤ det^{1/w}, hence
|g(y)| ≤ w·det^{1/w} < D₀^m ≤ E^m on |y| ≤ X; g(y) ∈ ℤ is divisible by E^m, so g(y) = 0, ≤ w − 1 roots, E ↦ y injective. |y| ≤ X with
X = (D₁ − D₀)/(2s) + 1/2 is right (window length (D₁−D₀)/s in x, x̂ nearest integer to the midpoint). D₀ ≥ 1 is not even needed.
Cor 1.4: sub-windows of length (D₁−D₀)/J have lower ends ≥ D₀, so (Cop) with D₀ and X_J covers each; endpoints may be double
counted (upper bound, harmless). Asymptotics: with w = τm, logs/ln n: 1/2 + τ²(β − ρ − j)/2 < τβ, optimum τ = β/(β−ρ−j) gives
β − ρ − j < β², i.e. ρ + j > β(1 − β). ✓ (the o(1) is an ε with w = w(ε); the J(w−1) count is n^{max(0, β(1−β)−ρ)+ε}.)
From-scratch test (`scripts/review_se2_cop.py`): exact integer (Cop) with the least J per (m, k) by bisection (Cop is monotone in J),
w ≤ 14, against brute-force divisor counts; half the trials adversarial (n = lcm of several class-mates inside the window).
300 trials: **0 violations**, 10 tight, Coppersmith beats the trivial bound in 126.
Verdict: **Lemma 1.3 SOUND, Cor 1.4 SOUND** (PROVED is the right label). Minor m-B1: Cor 1.4 says "≤ J(w−1) as soon as (Cop) holds
with X replaced by X_J" — the hypotheses gcd(σ, s) = 1, D₀ ≤ D₁ are inherited; fine. Minor m-B2: "for ρ ≤ 1/4 it is new to the
campaign" is a priority claim I cannot check; it is the standard "split the search interval" trick of Coppersmith/Howgrave-Graham
(e.g. the exhaustive-search-on-high-bits step), so it should be called elementary/standard, not new.

## C. Independent re-implementation of the dominant terms (task focus (b))

Scripts written without reusing the author's code paths (only the route *list* is shared, each route re-derived in §D):
* `scripts/review_se2_boxbound.py P|Q j` — the dyadic box bound for every integer N ∈ [2^{j/4}, 2^{(j+1)/4}), in exact
  Fractions; N-range enclosed by exact integer 4th roots; all logs/exps (ln 2, ln(a₁/a₀), divisor envelopes C_k(η)n^η, 2^{ω})
  in mpmath interval arithmetic rounded outward; every Coppersmith condition used is verified **exactly in big integers**
  (least J found by a float pre-screen, then checked/raised exactly). The e-modulus lower bound uses the exact strict inequality
  e > N/(4acd) > N₀/(32ACD) (se_box uses floor(DN(E₀)) + 1, one less at exact powers of two — conservative).
* `scripts/review_se2_tail.py` — the all-N ≥ 2^{600} P tail with **exact rational exponents**; (Cop) checked as a linear function
  of L = ln N (slope ≤ 0 exactly, value < 0 at the interval lower end of 600 ln 2), using X_J ≤ max(1, c₁N^{x₁−x_s−κ}/c_s) (this
  absorbs the +1/2 of X_J — se_tail.py silently relies on the same fact via its use of c₁/c_s instead of c₁/(2c_s); it is correct
  but undocumented: minor m-C1).

| quantity | author (tables / se_tail) | R223 independent | |
|---|---|---|---|
| D_Q bound, N ∈ [2^{32}, 2^{32.25}) (j = 128) | 7.5256·10⁸ | 7.5239·10⁸ | Q level-1 term 2D/r at r = 2^{32}: **0.35044 vs 0.35036** |
| D_P bound, j = 128 | 5.2821·10⁷ | 4.9348·10⁷ | P K = 1 term: **0.02460 vs 0.02298** |
| D_Q bound, j = 192 (r ≈ 2^{48}) | 6.4816·10¹¹ | 6.4695·10¹¹ | Q level-1 term at 2^{48}: 0.004605 vs 0.004597 |
| P tail: max exponent, #terms, G = bound/√N at 2^{600} | 0.4797, 13393, 873.57 | 0.47969, 13393, 873.58 | all terms e ∈ [0, 1/2), p ≤ (1/2 − e)·L₀ ✓ |
| P tail contribution to S, r ∈ [2^{32}, 2^{32.25}) | 0.10932 | **0.10930** | summed to K = 233 (last term 8·10⁻⁴¹) |

The P(j=128) gap (6.6 %) was traced box by box (se_box SE_DUMP vs my values): it comes entirely from se_box's conservative
modulus se = 1 instead of 2 at boxes with N₀/(32ACD) = 1 exactly (trivial count Δ/s + 1 doubles); no box of mine exceeds the
author's except by rounding. So the author's numbers are reproduced from independent code, and in the safe direction.
Independent S(b = 32) ≤ 0.35036 + 0.02298 + 0.10930 + (author's remaining terms 0.00235) ≈ 0.4850 < 1/2.
Verdict C: the dominant terms are **CONFIRMED** (independent exact/interval recomputation). I did not rerun the 3.5 h certificate;
the remaining ~1350 table cells are trusted on the author's engine (whose rounding was repaired after R-self-review M1; I found no
rounding-direction bug in the current se_box.c, see §D.3).
