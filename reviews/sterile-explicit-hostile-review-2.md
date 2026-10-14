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
   True (max p = 2 after aggregation; successive odd-K tail terms decay by ≈ 2^{2(b+1/4)·0.4797 − b} ≤ 0.48 at b = 32, measured 0.155
   at K = 19 and 0.4796 at K = 101, 201; smaller for larger b), so the remainder is < 10^{−30}; but the bound is unstated: minor m-A1.
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
300 trials (seed 223): **0 violations**, 10 tight, Coppersmith beats the trivial bound in 126; 3000 trials (seed 7): **0 violations**,
138 tight, Coppersmith beats trivial in 1312.
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
author's by more than the 7-digit precision of the SE_DUMP printout (0 of 4760 boxes at relative tolerance 10⁻⁶). So the author's numbers are reproduced from independent code, and in the safe direction.
Independent S(b = 32) ≤ 0.35036 + 0.02298 + 0.10930 + (author's remaining terms 0.00235) ≈ 0.4850 < 1/2.
Verdict C: the dominant terms are **CONFIRMED** (independent exact/interval recomputation). I did not rerun the 3.5 h certificate;
the remaining ~1350 table cells are trusted on the author's engine (whose rounding was repaired after R-self-review M1; I found no
rounding-direction bug in the current se_box.c, see §D.3).

## D. Route tables, code audit, other claims and labels

**D.1 Table 2 (P routes) and Table 3.2Q (Q routes).** Each row re-derived: H (b = (Nc + a)/f); A (e ≡ −N mod 4ad, then b, c);
C (f | N + 4a²d, f ≡ −1 mod 4ad, n ≤ 3N); D (f | 4c²dN + 1, f ≡ −1 mod 4cd); E (f | Nc + a, f ≡ −1 mod 4ac, cofactor b);
F ((e, a) with 4a | N + e; b | (N+e)/(4a), b ≡ −a (e); or d ≡ (N+e)/(4a)·(−a)^{−1} (e), a unit by 1.1(iv)); G (a² ≡ −N(4d)^{−1}
≡ −(N+e)/(4d) mod e, ≤ 2^{ω(e)} roots, e odd); τ₃ (abd = (N+e)/4, ordered triples); I (b = ce − a); J (a, b roots of
t² − ce·t + (N+e)/(4d): in fact ≤ 2 without the 2^{ω} factor se_box multiplies in — harmless over-count). Q: AD (≤ 2 per (a, d),
M17C 2.1(iv) re-proved: f ≤ √t is the least residue of its class mod 4ad > √t, f > √t has cofactor < √t in a fixed class);
fa, AC, CD, Ea, Ed, τ₃ and the f-routes fac, fca, fda (c ≡ −aF, d ≡ −(4a²)^{−1}, a ≡ −cF^{−1} mod f; 4a, 4c, 4d | f + F;
gcd(f, F) = 1 in-cell) ✓; f ≤ F + 2 (from ef = 4a²d + 1 ≤ eF + 2) ✓. Lemma 1.2's sizes ✓ (incl. the strict e > N/(4acd)).
All brute-force checked (§A.1). Verdict: **SOUND**.

**D.2 se_box.c numerics (outward rounding, 1e-15 padding, long double, dyadic boxes).** Line-by-line: box corners are exact powers
of two (`ldexpl`), counts n_A etc. are exact (or within 1 ulp ≈ 10⁻¹⁹ relative once ≥ 2^{64}, absorbed by the final 10⁻⁹ pad);
every lower bound (N₀, E₀, b₀, a₀, D₀, s_min) is DN-padded and every upper bound (N₁, E₁, b₁, a₁, D₁, ln n) UP-padded by 10⁻¹⁵
before any floor/ceil/comparison; pruning tests compare exact powers of two against the UP-padded N₁ (prunes only provably empty
boxes); where 4ACD − 1 is not representable (≥ 2^{64}) the D₀ := DN(4ACD) < 4ACD − 1 holds because 4ACD·10⁻¹⁵ > 1; τ envelopes carry
UP + 10⁻¹² absolute padding in log space (≫ x87 libm error); the (Cop) test is re-verified for the final J with a 10⁻¹²-relative
margin; table values are printed with 11 digits and re-inflated by 10⁻⁹ in se_r0. I found **no rounding in the unsafe direction**.
Residual assumptions (glibc x87 `logl/expl/powl` accurate to a few ulp; 64-bit mantissa, checked at runtime) are documented in the
header. My exact/interval recomputation (§C) is the stronger evidence. Verdict: **SOUND** for the cells I recomputed; the others
inherit the same code path.

**D.3 se_tail.py.** Re-derived every route bound in normalised form (P: H, A, C, D, E, F, G, τ₃, I; Q: AD, AC, CD, fac, fca with the
caps a ≤ (N/(2d))^{1/2}, acd < N, resp. cd ≤ (F+1)/2, f ≤ F + 2, a ≤ (F+1)/(2cd)); the e lower bound N^{1−σ⁺}/4 (σ⁺ capped at 1 is
still valid as e ≥ 1); the J = ⌈N^κ⌉ handling and the +1/2 of X_J (m-C1). Exponents are multiples of 1/320 except κ (padded 10⁻⁷),
and the combiner rounds up to a 10⁻⁶ grid that contains all multiples of 1/320, so the float exponents cannot round below the
intended ones. The independent exact-exponent re-implementation reproduces the P tail to 5 digits (§C). Verdict: **SOUND**.

**D.4 Prop 2.1 / (I3): "θ* = 2/5 exactly … tolerated up to η = 0.3".** Labelled grid EVIDENCE / Assessment — correctly *not* used in
Theorem 3.4 (whose tail is certified at exponent 0.4797, not 2/5). Independent continuum optimiser (`scripts/review_se2_rate.py`:
my own route exponents incl. the trivial window/modulus bound, 1/120 grid + 240 Nelder–Mead refinements): θ*(0.25) = θ*(0.3) = 0.4000,
θ*(0.4) = 0.4500, θ*(0.5) = 0.5000 (agree), but **θ*(0.35) = 0.4250, not 0.417** — the author's 1/60 grid misses the corner
(α, γ, δ, ε) = (1/3, 0.2583, 1/3, 0.075) (confirmed with the author's own `se_rate2.routes`: min = 0.425 there; `se_rate2.theta(0.35, n=120)`
also gives 0.425). Near the threshold θ*(η) = 0.4 + (η − 0.3)/2 for η ∈ [0.3, 0.4], i.e. η = 0.3 is exactly the break point (two-corner tie:
ET's point and (1/3, 0.233, 1/3, 0.1) with the τ₃ route = ε + η = 0.4). So "tolerated up to η = 0.3" survives refinement, but "exactly"
is not grid-provable (the objective is not piecewise linear: Cor 1.4 contributes β(1 − β)), and one tabulated value is wrong (m-D1).
Also (I3) says "no divisor bound at all except τ₃": route G (and the certificate) also uses 2^{ω(e)} ≤ C_ω e^{0.1}; exponent-free in
the continuum, but a divisor-type bound nonetheless (m-D2).

**D.5 (I1) dictionary.** The *equations* match under (m', g', w, C, v, T^s, L', E) ↔ (4d, c, a, b, e, N, 4cd, f): m'wC = T^s + v ↔
4abd = N + e, w + C = g'v ↔ a + b = ce, Ev = T^s + m'w² ↔ ef = N + 4a²d ✓. But O216's Case B has side conditions T ∥ w, T ∥ C
(FF_STERILE_PUSH (B)), whereas the in-cell ℤ data have r ∤ ab; T ∤ m'g' ↔ r ∤ cd matches. "Literally the ℤ P-data" overstates (m-D3).
The dictionary is not used in any proof.

**D.6 r = 13 and r = 17 statements.** From-scratch level-1 coverage (`scripts/review_se2_level1.py`: P-data of N = r and Σ^I_r points,
in-cell): r = 13: all six non-residue cells {2, 5, 6, 7, 8, 11} covered at level 1 ✓ (POINTWISE_MORDELL §1); r = 17: survivors {5, 7}
of eight ✓. "Any union bound needs a P-count with constant ≲ 2.5 at θ = 0.4 (M17D §1)" abbreviates M17D's precise statement
(no log loss, from K = 15 on, *given* the exact data through K = 13, pointwise 2.48 / cumulative 2.64); acceptable as a pointer,
better quoted with its conditions (m-D4).

**D.7 Labels and presentation.** Theorem 3.4 "PROVED, computer-assisted" — acceptable (it is PROVED relative to the listed lemmas +
CERTIFIED tables). But: (i) the header says "relative to the same inputs as (J)26 Thm 3.1 minus …" — it actually uses *more* M17 inputs
(Lemma 1.3, 5.1, 5.2, M17B 1.1, M17C 2.1(iv)); DEPTH_ASPECT §3 states Lemma 1.3 is *not* used there and Lemma 5.2 is optional, so the
general-r versions of 1.3/5.1/5.2 had not been reviewed before (R187 covered 1.1, 2.1–2.3). They are r-free (re-derived and brute-forced
here, §A.1), so this is a citation repair (m-D5). (ii) "→ 1/2 as r → ∞" is not an output of se_r0; it follows from the tail lists
(each term × weight ≤ c·r^{−1/2−0.02K}·polylog, and the Q terms ≤ c r^{−1/4}) — add the sentence (m-D6). (iii) Section order: "## 5.
Feedback to F_q[T]" sits between §3.3 and §3.4 (Theorem 3.4 appears under §5; there is no §4) (m-D7). (iv) Prop 2.1: "Q … 0.65 (grid;
`/tmp`-prototype, to be committed)" — se_rateQ.py is committed; stale (m-D8). (v) §5 FF claims ("closes q = 27") are labelled EVIDENCE ✓.
