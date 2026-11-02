# Z54_BILINDIV — depth lane BILINDIV (FRONTIER §7.1, gap 1, divisor/geometry angle): the balanced block by divisor sums and strip geometry

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Everything here concerns an **upper bound** (a power saving for one block); it cannot give positivity, and its value is
the §7.1 benchmark and method. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal
results, internally reviewed only.

Brief: `z52bbriefs/z53_depth.md` (wave z54), kickoff `z52bbriefs/z54_lanes.md` §BILINDIV (target as §BILINJAC).
Scripts `scripts/z54_bilindiv_*`, data `data/z54/bilindiv/`. Checkpoint 1: commit 525f71c3.

**Verdict: narrowed, with one new sufficient condition** (§8). No power saving for the balanced block is proved. A
power saving follows from a first-order hypothesis TD on a smooth phase summed over the lattice points of the thin
hyperbolic strip (Theorem T, a new sufficient condition alongside Z53_HYP2CYCLE's second-order MIX). Each divisor/geometry
tool class of the kickoff is closed by a scoped statement with its exact deficit (§5). The common reason is that every
first-order filter retains ≍ U candidates, while the tie is a probability-1/U event that only a *joint* (bilinear)
cancellation can see.

## 0. Notation

p is an odd prime (most statements hold for odd n ≥ 5), U ≥ 2 an integer with 16U³ ≤ p, and 𝔅 = (U, 2U]². The
*fourth-root range* is c₁p^{1/4} ≤ U ≤ c₂p^{1/4} with fixed 0 < c₁ ≤ c₂, and p ≥ p₀(c₂) so that 16U³ ≤ p (for
U = ⌊p^{1/4}⌋ this is p ≥ 2¹⁶).
* N₂(p, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | p + u + B} counts the 2-cycles of the remainder map (Z53_HYP2CYCLE).
  N₄ ≤ N₂ is the sub-count with 4 | k, where k := (p+u+B)/(uB) is the *level*. The balanced (★) block is
  N(U, U) = 2N₄ (Z52D Prop 2).
* Trivial bound: N₄ ≤ N₂ ≤ U/2. Expected size O(1): E N₂ ≈ 0.36 (Z53_HYP2CYCLE §4).
* **Target R2 (FRONTIER §7.1).** There is η > 0 with N₂(p, U) ≪ U^{1−η} for all primes p and all U in the fourth-root
  range. This implies N(U, U) ≪ U^{1−η}.
* Strip variables (Z53_HYP2CYCLE Lemma A). For a level k put s_k := (−p mod k), m_k := (p + s_k)/k and
  D_k := s_k² − 4m_k. Let **E1** := {k : s_k ∈ (2U, 4U], m_k ∈ (U², 4U²]}. Equivalently, E1 is the set of lattice points
  (k, m) of the thin hyperbolic strip p + 2U < km ≤ p + 4U with U² < m ≤ 4U². Let E1⁺ := {k ∈ E1 : D_k ≥ 1} and
  w_k := √D_k ∈ ℝ.
* **Lemma A** (Z53_HYP2CYCLE; requires 16U³ ≤ p, so every level exceeds 4U). Under that condition
  N₂ = #{k ∈ E1⁺ : D_k = w² with w ∈ ℕ, and (s_k ± w)/2 ∈ (U, 2U]}, and the map {u,B} ↦ k is injective.
  The condition m_k ∈ (U², 4U²] holds for every 2-cycle, since m = uB.

## 1. Statements attacked

(A) **Target R2** (OPEN). For each tool class of the kickoff, we either turn it into a power saving or close it with a
scoped statement and the exact deficit:
1. divisor function in APs (Selberg–Hooley, Fouvry–Iwaniec beyond x^{2/3}) → §5.1;
2. divisors in short intervals and the Dirichlet-divisor exponent → §5.2;
3. anatomy, i.e. Tenenbaum/Ford H(x,y,z) ("has a divisor in a range") → §5.3;
4. determinant method (Bombieri–Pila / Heath-Brown) with occupancy pruning → §5.4;
5. lattice points near curves in the thin strip, exponent pairs / Bombieri–Iwaniec → §5.5 and §4.3.

(B) **Theorem T** (PROVED reduction; §4). A power saving (not beyond-square-root) in the strip sums
  T(h) := Σ_{k ∈ E1⁺} e(h·w_k) = Σ_{(k,m) ∈ ℤ²: p+2U < km ≤ p+4U, U² < m ≤ 4U², D ≥ 1} e(h√((km − p)² − 4m))
for 1 ≤ h ≤ U^η implies R2 (hypothesis **TD(η)**). T(h) is a *first-order* object: a smooth phase summed over the
≍ U lattice points of the strip, or equivalently over the divisors near √n of the integers n of an interval of length
n^{1/4}. Z53_HYP2CYCLE's MIX is second order in the remainder map.

(C) **Exact forms** of the balanced block in divisor and strip language, with supports and sizes (§3, PROVED).

## 2. Why this is not already closed

* Z52D closed three things: one-step dualization at fixed conductor, ET/Fejér with max|S_h| and square-root input, and
  Cauchy–Schwarz in the function variable. Its R1 (beyond-square-root 2D sums) is numerically false at 10¹². None of
  these is a strip or divisor-sum argument.
* Z53_HYP2CYCLE closed only the *black-box* determinant method: the HB14/HB15 bound times a uniform per-curve bound, on
  the full box or a full grid. It reduced R2 to MIX, which is second order. Occupancy pruning, specific curves and every
  first-order strip formulation were left open (Prop D scope).
* Z53_SQSIEVE Prop B2 closed the k-Poisson square sieve with triangle inequality over frequencies. It names as the
  missing input "χ_Q-twisted divisor sums near √m of integers in an interval of length m^{1/4}". That is the same strip
  as here, but with multiplicative twists; this lane uses additive twists e(h·w) and pure counting tools.
* No scoped statement about the balanced block exists in the repo for these tools. `git grep` finds Ford's H(x,y,2y)
  only in literature catalogues (`BRAINSTORM/z52_lit_divisor_class.md`, as an ambient B6 count). Sargos appears only as
  a lemma inside Bourgain's exponent-pair proof (`data/z53/sqsieve/LIT_CHECK.md`). Hooley, Shiu and Tenenbaum appear
  only in brainstorm lists or unrelated memos.

## 3. Exact forms and sizes at the balanced block (PROVED; elementary)

**Lemma 3.1 (five forms).** Let 16U³ ≤ p. N₂(p, U) equals each of the following:
(a) *pair form:* #{{u,B} ⊂ (U,2U] : u | p + B, B | p + u} (at primes, gcd(u,B) | p forces coprimality, so the two
    divisibilities give uB | p + u + B);
(b) *strip form:* #{(k, m) ∈ ℤ² : p + 2U < km ≤ p + 4U, D := (km−p)² − 4m = w² with w ≥ 1, (km − p ± w)/2 ∈ (U, 2U]};
(c) *divisor form:* Σ_{s ∈ (2U, 4U]} #{d | p + s : s² − 4d = w² with w ≥ 1, (s ± w)/2 ∈ (U, 2U]}. Here d = uB ∈ (U², 4U²]
    ranges over divisors within a factor 4 of √(p+s), and the integers p + s run over an interval of length 2U ≍ (p+s)^{1/4};
(d) *trial form:* #{(u, k) : u ∈ (U, 2U], (ku − 1) | (p + u), (p + u)/(ku − 1) ∈ (U, 2U], (p+u)/(ku−1) > u};
(e) *modular-hyperbola form:* #{(X, Y) : XY ≡ 1 (mod p), k := (XY − 1)/p, k | X + 1, (X+1)/k and (Y+1)/k ∈ (U, 2U],
    X < Y}. Here X = ku − 1 and Y = kB − 1 are both ≍ kU ≍ p^{3/4}.
*Proof.* (a) is Z52D Prop 2. (b) is Lemma A with m = km/k; (c) substitutes d = m and s = km − p. (d): kuB − u − B = p
⟺ B(ku − 1) = p + u. (e): (ku − 1)(kB − 1) = kp + 1, and conversely XY = kp + 1 with k | X + 1 gives
Y ≡ −1 (mod k), because XY ≡ 1 (mod k). ∎

**Quadratic-order reading (PROVED).** For k ∈ E1 let α := (s_k + √D_k)/2, an algebraic integer with trace s_k and norm
m_k. Then m_k | p + s_k, so α | p + s_k − α = p + ᾱ in ℤ[α]. Thus E1 is the set of "2-cycles over quadratic orders",
and N₂ counts the split ones (D a nonzero square with the size condition).

**Table 3.2 (candidates × probability; sizes PROVED or cited, probabilities heuristic).**

| parametrisation | candidate set (first filter) | its size | tie event | order of the event in the remainder map |
|---|---|---|---|---|
| u ↦ f(u) (HYP2CYCLE) | dom f | U log 2 + O(U^{1−1/15}) (first order, window width Θ(1)) | f(f(u)) = u, prob ≍ 1/U | **second** (MIX) |
| level k (this memo) | E1 | ≤ Σ_{s∈(2U,4U]} τ(p+s) ≪ U^{1+ε}; measured 2.72U | w_k ∈ ℤ, prob ≍ 1/U | **first**, but window width 1/U (critical) |
| (u, B) ∈ 𝔅 (Z52D R1) | all of 𝔅 | U² | uB \| p+u+B, prob ≍ 1/U² | first in each variable; needs beyond-√ |
| (X, Y) mod-p hyperbola | XY ≡ 1 (p) in [p^{3/4}]² | ≍ U² (Weil-critical box) | k \| X+1, prob ≍ 1/U² | — |
| k-form AP n = kp+1 | divisors X ∈ (kU,2kU] of n ≡ 1 (mod p) | ≍ U² (EVIDENCE, §6.3) | X ≡ −1 (mod (n−1)/p) | tied modulus |

**Exponent bookkeeping in p.** U ≍ p^{1/4}, levels k ≍ p^{1/2}, m = uB ≍ p^{1/2}, X, Y ≍ p^{3/4}, n = kp+1 ≍ p^{3/2}. The
trivial bound is p^{1/4} and the expected count is p^{0}.

## 4. Theorem T: the strip sums suffice (PROVED reduction) and why they are hard

### 4.1 Statement

Fix ψ ∈ C_c^∞(−2, 2) with 0 ≤ ψ ≤ 1 and ψ = 1 on [−1, 1]. For 0 < δ ≤ 1/2 put χ_δ(x) := Σ_{j∈ℤ} ψ((x + j)/δ), a smooth
1-periodic function with χ_δ ≥ 1 on ℤ + [−δ, δ] and Fourier coefficients χ̂_δ(h) = δψ̂(δh).

**Theorem T (PROVED).** For every ε > 0 and A ≥ 2 there is C = C(ψ, ε, A) such that for every odd n ≥ 5, every integer
U ≥ 2 with 16U³ ≤ n, and every 0 < δ ≤ 1/2, with H := U^ε/δ,

  N₂(n, U) ≤ 4δ·|E1⁺| + 8δ·Σ_{1≤h≤H} |T(h)| + C·|E1⁺|·U^{−εA}.

*Proof.* By Lemma A, each 2-cycle gives a distinct k ∈ E1⁺ with w_k ∈ ℤ, and χ_δ(w_k) ≥ 1 there. Since χ_δ ≥ 0,
N₂ ≤ Σ_{k∈E1⁺} χ_δ(w_k). The Fourier series of χ_δ converges absolutely (ψ̂ is Schwartz), so the right side equals
Σ_{h∈ℤ} δψ̂(δh)T(h), with T(0) = |E1⁺| and T(−h) the complex conjugate of T(h).
* |ψ̂| ≤ ‖ψ‖₁ ≤ 4 bounds the h = 0 term by 4δ|E1⁺| and each 1 ≤ |h| ≤ H term by 4δ|T(h)|.
* For |h| > H: |ψ̂(ξ)| ≤ C_A|ξ|^{−A}, so Σ_{|h|>H} δ|ψ̂(δh)||T(h)| ≤ |E1⁺|·2C_A Σ_{h>H} δ(δh)^{−A}
  ≤ 4C_A|E1⁺|(δH)^{1−A}/(A−1) ≤ C|E1⁺|U^{−ε(A−1)}.
Renaming A − 1 → A gives the claim. ∎

**Hypothesis TD(η).** There is C₀ such that |T(h)| ≤ C₀U^{1−η} for all 1 ≤ h ≤ U^η, uniformly for primes p and U in the
fourth-root range.

**Corollary T (CONDITIONAL on TD(η)).** For every ε > 0: N₄ ≤ N₂ ≪_{η,ε,C₀} U^{1−η/2+ε}, uniformly in the fourth-root
range. Hence N(U, U) ≪ p^{(1−η/2)/4+ε}.
*Proof.* Each k ∈ E1 is a divisor of p + s_k with s_k ∈ (2U, 4U], and k determines s_k. Hence
|E1⁺| ≤ |E1| ≤ Σ_{s∈(2U,4U]} τ(p + s) ≪_ε U·p^{ε/8} ≪ U^{1+ε/2}. Take δ = U^{−η/2} and Theorem T with ε′ = η/4, so
H = U^{3η/4} ≤ U^η. Then N₂ ≤ 4U^{−η/2}U^{1+ε/2} + 8U^{−η/2}·U^{3η/4}·C₀U^{1−η} + O(1) ≪ U^{1−η/2+ε}. ∎
(With Shiu's theorem the factor U^{ε} becomes log p; Shiu's exact statement was not re-verified here,
`data/z54/bilindiv/LIT_CHECK.md` item 2, so we use τ(n) ≪ n^{o(1)}.)

### 4.2 What TD is, and how it compares with MIX (Assessment, with PROVED identities)

* **First order.** T(h) = Σ_k G_h(k, θ_k), where θ_k := {−p/k} and G_h(k, θ) := 1[kθ ∈ (2U, 4U], ...]·e(h W_k(θ)),
  with W_k(θ) := √(k²θ² − 4(p + kθ)/k). It is a function of the level and of a *single* remainder phase. MIX
  (Z53_HYP2CYCLE Thm R) needs the joint law of (θ_u, θ_{f(u)}).
* **But at the critical scale.** The window for θ_k has width ≍ 1/U, and inside it hW_k oscillates fast:
  W_k″(θ) = −4(kp + 1)/W_k(θ)³ (PROVED by differentiating W² = k²θ² − 4p/k − 4θ). So |hW_k″| ≍ hU³ and W_k sweeps an
  interval of length ≍ U across the window. Resolving the event needs the joint law of (k, θ_k) at resolution
  ≍ 1/(hU²), i.e. Weyl sums Σ_k e(νp/k) with ν up to ≍ hU² and k ≍ U². There the phase f(k) = νp/k has f′ ≍ hU²
  and f″ = 2νp/k³ ≍ h ≥ 1: the B-process maps the k-sum (length ≍ U²) to a dual of length ≍ f″·U² ≍ hU², which is
  self-dual at h ≍ 1 (the regime of Σ_{k≍x^{1/3}} e(x/k), not the hyperbola point of the divisor problem).
* **Equivalent reading.** {w_k} is equidistributed mod 1 ⟺ the real root u*_k = (s_k − w_k)/2 of z² − s_kz + m_k is
  equidistributed mod 1 ⟺ the divisors d = m of p + s are equidistributed, at scale ≍ U^{1−η}, relative to the
  quadratic grid {u(s − u)}. This is a fine-scale "divisors near √n" statement averaged over n in an interval of length
  n^{1/4}.
* **Double dual (Assessment; stationary-phase heuristic, not used anywhere).** After the θ-expansion of §4.3 and a
  further Poisson step in k (phase −νp/k − μk, stationary at k* = √(νp/μ)), T(h) becomes a 2D sum over (ν, μ) ≍ (hU², hU²)
  with leading phase −2√(p·νμ) and amplitude ≍ U^{−3/2}h^{−1}: a Voronoi-type piece of the divisor problem at x ≍ p,
  n = νμ ≍ h²p, at the hyperbola point ν ≍ μ ≍ √n, with factorisation-dependent lower-order phases. Square-root
  cancellation there gives ≍ U^{1/2}; per-ν exponent pairs give ≫ U^{3/2} (any pair has κ + λ ≥ 1/2). So the missing joint cancellation is a
  bilinear divisor-problem-type estimate.
* **Relation to MIX.** Neither TD nor MIX is shown to imply the other. Both ask only for a power saving in a sum of
  ≍ U terms, and both are numerically of square-root size (§6.1; Z53_HYP2CYCLE §5.3).

### 4.3 Proposition 4.3 (per-variable implementations of TD give no saving; PROVED, scoped)

This is the strip analogue of Z53_SQSIEVE Prop B2. Fix φ ∈ C_c^∞((5/2, 7/2)) with 0 ≤ φ ≤ 1, φ ≢ 0, and the level range
𝒦′ := [p/(1.5U²), 0.99p/U²]. Consider the smoothed sub-sum
  T_φ(h) := Σ_{k∈𝒦′} φ(s_k/U)·e(h·w_k).
On its support s_k ∈ (2.5U, 3.5U) and m_k ≤ 1.5U²(1 + o(1)), so D_k ≥ 0.2U² > 0 and m_k > U² (for U ≥ U₀). Hence these
k lie in E1⁺, and T_φ is a positively weighted sub-sum of T.
Put G_k(θ) := φ(kθ/U)·e(h W_k(θ)). It is smooth and supported in (2.5U/k, 3.5U/k) ⊂ (0, 1); extend it 1-periodically
and write G_k(θ) = Σ_ν c_ν(k) e(νθ). Then (exact identity)
  T_φ(h) = Σ_{ν∈ℤ} Σ_{k∈𝒦′} c_ν(k) e(−νp/k).
Call an *implementation* any argument that
* (i) uses this expansion,
* (ii) applies the triangle inequality over ν, and
* (iii) bounds each k-sum by some b_ν ≥ c₀·(Σ_k |c_ν(k)|²)^{1/2} for a fixed c₀ > 0, i.e. no better than square root
  in the k-sum.

Condition (iii) holds for exponent-pair, derivative-test and Bombieri–Iwaniec bounds applied after partial summation,
since there the phase derivative νp/k² ≍ ν ≥ 1 on the relevant ν. These bounds are then ≥ max|c_ν|·(length)^{1/2} ≥
‖c_ν‖₂.

**Proposition 4.3.** In the fourth-root range, for U ≥ U₀ and 1 ≤ h ≤ U, every implementation gives
|T_φ(h)| ≤ Σ_ν b_ν with Σ_ν b_ν ≥ c·h^{1/2}U^{3/2}, where c > 0 depends on φ, c₀, c₁, c₂. The other order (sum over
ν first) returns exactly Σ_k φ(s_k/U), the trivial bound. So no per-variable implementation beats the trivial bound
≍ U; the missing input is a *joint* (ν, k) cancellation of size h^{1/2}U^{1/2+η} beyond per-line square root. This is the
additive-twist analogue of SQSIEVE's missing bilinear (ℓ, C) estimate.
*Proof.*
* Parseval: Σ_ν |c_ν(k)|² = ∫₀¹ φ(kθ/U)²dθ = (U/k)‖φ‖₂². Summing over k ∈ 𝒦′ gives
  Σ_ν Σ_k |c_ν(k)|² ≥ ‖φ‖₂²·U·Σ_{k∈𝒦′}1/k ≥ c₃U (the range has ratio 1.485).
* Pointwise bound. c_ν(k) = ∫ φ(kθ/U)e(hW_k(θ) − νθ)dθ. The phase has second derivative hW_k″ = −4h(kp+1)/W_k³, and
  W_k ≤ s ≤ 3.5U on the support. So |hW_k″| ≥ 4hkp/(3.5U)³ ≥ hp²/(16.1U⁵) ≥ hU³/(16.1c₂⁸) =: λ.
* The second-derivative lemma for oscillatory integrals (Titchmarsh, *Theory of the Riemann zeta-function*, Lemma 4.4,
  with the amplitude handled by integration by parts: bound (8/√(2πλ))·(sup|amp| + total variation)) gives
  |c_ν(k)| ≤ C₄(hU³)^{−1/2}. The total variation of θ ↦ φ(kθ/U) equals that of φ.
* Hence for every ν: Σ_k |c_ν(k)|² ≤ |𝒦′|·C₄²/(hU³) ≤ C₅/(hU), since |𝒦′| ≤ p/U² ≤ U²/c₁⁴.
* Therefore Σ_ν b_ν ≥ c₀Σ_ν‖c_ν‖₂ ≥ c₀(Σ_ν‖c_ν‖₂²)/max_ν‖c_ν‖₂ ≥ c₀c₃U·(hU/C₅)^{1/2}.
* Summing over ν first gives Σ_ν c_ν(k)e(−νp/k) = G_k(θ_k) (the Fourier series converges absolutely), whose modulus is
  φ(s_k/U). ∎

## 5. Tool classes: scoped statements with exact deficits

### 5.1 Divisor function in arithmetic progressions (Selberg–Hooley; Fouvry–Iwaniec beyond x^{2/3})

**Proposition 5.1 (PROVED arithmetic; the reading is Assessment).** In the k-form (Lemma 3.1(e)),
  N₂ = Σ_{n ≡ 1 (mod p)} #{X | n : X, n/X ∈ (kU, 2kU], X ≡ −1 (mod k), X < n/X},  k := (n−1)/p,
(n ranging over p𝒦 + 1 with 𝒦 the level range; X ≡ −1 (mod k) forces n/X ≡ −1 (mod k), since n ≡ 1 (mod k)).
The progression has modulus q = p and length x/q ≍ U², with x ≍ U²p ≍ p^{3/2} = q^{3/2}. So q = x^{2/3} exactly.
(a) *Endpoint.* The classical asymptotic for Σ_{n≤x, n≡a (q)} τ(n) holds uniformly for q < x^{2/3−ε}, with error
    (q^{1/2} + x^{1/3})x^ε (Fouvry–Iwaniec, Acta Arith. 61 (1992), quoting the classical bound; VERIFIED-PRIMARY,
    `LIT_CHECK.md` item 3). Here both error terms are ≍ p^{1/2+ε}, against a main term ≍ U² log p ≍ p^{1/2} log p.
    So even the *untied* divisor sum along this progression sits exactly at the endpoint of the Selberg–Hooley range.
    Fouvry–Iwaniec's Theorem 1 goes beyond x^{2/3} only *on average* over special moduli rs² (r squarefree,
    r ≤ x^{3/8}), not for one prime modulus.
(b) *Tie invisible.* The inner congruence has modulus (n−1)/p ≍ x^{1/3}, which varies with n. A fixed-modulus AP tool
    can impose it only through a fixed Q, as X ≡ −1 (mod gcd(k, Q)). The relaxed count
    N_rel(Q) = Σ_k #{X | kp+1 : X ∈ (kU, 2kU], X ≡ −1 (mod gcd(k,Q))} ≥ N₂ has model main term
    ≍ U²·E[1/φ(gcd(k,Q))] ≥ (φ(Q)/Q)·c·U² ≫ U²/log log Q, which exceeds the trivial bound by ≍ U.
    EVIDENCE (§6.3): at p ≈ 10⁸ (U = 100), N_rel(1) ≈ 0.48–0.53U² and N_rel(27720) ≈ 0.28–0.30U².
**Deficit.** The best such a tool could output is ≍ U²/log log Q. That exceeds the trivial bound by a full factor
p^{1/4}, and the untied asymptotic is at the x^{2/3} endpoint.

### 5.2 Divisors in short intervals; the Dirichlet-divisor exponent

By Lemma 3.1(c), E1 ⊂ {(s, d) : d | p + s, s ∈ (2U, 4U]}: these are divisors within a factor 4 of √n for n in an
interval of length y = 2U ≍ n^{1/4}.
* (PROVED) |E1| ≤ Σ_{s} τ(p+s) ≪ U^{1+ε}. No asymptotic is needed for upper bounds.
* (PROVED relative to Huxley's exponent; Assessment beyond) An asymptotic for |E1| would need short-interval control of
  restricted divisor sums at y = x^{1/4}. The bound Δ(x) ≪ x^{131/416+ε} (Huxley 2003; `LIT_CHECK.md` item 5 — the
  Bourgain–Watt improvement is withdrawn and is **not** used) gives Σ_{x<n≤x+y}τ(n) ~ y log x for
  y ≥ x^{131/416+ε}; our y = x^{1/4} is short of that by 131/416 − 1/4 = 27/416 ≈ 0.065 in the exponent of x = p (and
  Δ(x) = Ω(x^{1/4}), so no bound on Δ alone can reach y = x^{1/4}). The sharper short-interval
  threshold quoted in `LIT_CHECK.md` item 7 (≈ x^{1/3}) is UNVERIFIED and not used.
* The tie is the *square* condition on top of E1. Short-interval divisor tools bound E1 but are blind to it, since
  s² − 4d = □ is not a divisor condition on p + s. TD (§4) is precisely the additively twisted short-interval divisor
  sum that would be needed. Prop 4.3 shows that its per-variable Fourier implementations fail by h^{1/2}U^{1/2}.
**Deficit.** Untwisted tools reach only |E1| ≍ U, which equals the trivial bound. Twisted ones need TD.

### 5.3 Anatomy filters (Tenenbaum/Ford H(x,y,z))

**Proposition 5.3 (PROVED).** In the fourth-root range, for U ≥ U₀(c₁, c₂), each one-sided divisibility filter
retains a positive power of U:
(a) |dom f| = #{u ∈ (U,2U] : some B ∈ (U,2U] has u | p + B} ≥ U/6 − O(U^{14/15});
(b) #{u ∈ (U,2U] : p + u has a divisor in (U, 2U]} ≫_ε U^{1−ε}.
So any argument that bounds N₂ by the number of u passing one of the two divisibility conditions, or an anatomy
condition implied by it ("p + u has a divisor in (U, 2U]", Ford's H-type event), cannot save more than U^{o(1)}. The tie
is the *coincidence* of the two conditions.
*Proof.*
(a) Let θ_u := {−p/u}. If u ∈ (1.5U, 2U] and θ_u ∈ (2/3, 1), then B := uθ_u = (−p mod u) satisfies
    B > (2/3)(1.5U) = U and B < u ≤ 2U. So u ∈ dom f.
  * The number of such u is (1/3)(U/2) + O(U·𝒟), where 𝒟 is the discrepancy of (θ_u)_{u∈(1.5U,2U]}.
  * Erdős–Turán gives 𝒟 ≪ 1/H + Σ_{h≤H}h^{−1}U^{−1}|Σ_{u} e(hp/u)|.
  * The fourth-derivative test (Titchmarsh, Thm 5.13 with k = 4, K = 8) applies with f(u) = hp/u, f⁗ = 24hp/u⁵, and
    λ₄ ≍ hp/U⁵ ≍ h/U in the fourth-root range. It gives
    Σ_u e(hp/u) ≪ Uλ₄^{1/14} + U^{3/4}λ₄^{−1/14} ≪ h^{1/14}U^{13/14} + U^{11/14}.
  * So 𝒟 ≪ 1/H + H^{1/14}U^{−1/14} + U^{−3/14}log H, and H = U^{1/15} gives 𝒟 ≪ U^{−1/15}.
(b) Let P₁ := #{(u, B) ∈ (U,2U]² : B | p + u}. Each B has at most one u ≡ −p (mod B) in an interval of length U < B,
    so P₁ = #{B : some u ∈ (U,2U] has u ≡ −p (mod B)}. This is |dom f| with the roles of the letters exchanged, hence
    P₁ ≥ U/6 − O(U^{14/15}) by (a).
    Cauchy–Schwarz gives P₁² ≤ #{u : p+u has a divisor in (U,2U]}·Σ_u τ(p+u)², and Σ_u τ(p+u)² ≤ U·max_{n≤2p}τ(n)²
    ≪ U^{1+ε}. ∎
EVIDENCE (§6.2): P₁/U = |dom f|/U = 0.66–0.73 (expected log 2 ≈ 0.693), and (b)'s count is 0.33–0.38U at 10¹² and 10¹⁴.
The values are identical in law at primes, odd squares and near-squares.
**Deficit.** The full power U^{1−o(1)}. Ford's (log y)^{−δ}(log log y)^{−3/2} saving is for the ambient density over all
n ≤ x; at a single p it is at most logarithmic, and Prop 5.3(b) shows nothing better than U^{1−ε} can come from the
one-sided event.

### 5.4 Determinant method with occupancy pruning (Bombieri–Pila / Heath-Brown)

Z53_HYP2CYCLE Prop D: for F = kuB − u − B − p on any translated box with sides 2 ≤ B₁, B₂, B₃ (for u, B, k), the
auxiliary-surface bound X of Heath-Brown's Theorem 15 (statement as restated by Reuss and by Browning–Heath-Brown;
the multi-affine F keeps T = B₁B₂B₃ under translation) satisfies X ≥ min(B_i)^{2/√3}.

**Proposition 5.4 (domination by the elementary per-fibre bound; PROVED relative to HB15 as restated).** Let
16U³ ≤ p. In the balanced block every value of u, every value of B and every value of k carries at most one solution
(u, B, k). Consequently every sub-box Q with sides a, b, c satisfies |Q ∩ Sol| ≤ min(a, b, c) + 1. If a, b, c ≥ 2, then
  X(Q) ≥ min(a, b, c)^{2/√3} ≥ (min(a, b, c) + 1)/2 ≥ |Q ∩ Sol|/2.
Hence, for every family 𝒬′ of sub-boxes covering the solutions, *with any occupancy pruning*, any per-box bound obtained
from HB15 as a black box (X(Q) times a per-curve bound ≥ 1) is at least half the elementary per-fibre bound
Σ_{Q∈𝒬′}(min side + 1) on the same family. The black-box determinant method is dominated, box by box, by
"≤ 1 solution per u". A power saving through it therefore requires an independent bound on occupancy,
#{Q ∈ 𝒬′} ≪ U^{1−η}/min side — which is the target itself at a coarser scale.
*Proof.*
* Same u: u(k₁B₁ − k₂B₂) = B₁ − B₂ with |B₁ − B₂| < U < u, so B₁ = B₂ and then k₁ = k₂. Same B: symmetric.
* Same k: Lemma A (16U³ ≤ p).
* A side of length a contains ≤ a + 1 integers.
* For t ≥ 2, t^{2/√3} ≥ t^{1.15} ≥ (t + 1)/2. ∎
*Scope.* This covers black-box HB15 with arbitrary pruning. It does not cover arguments that bound the *actual* number
of auxiliary curves below X(Q), nor Salberger's global method, nor p-adic/Coppersmith variants. Remark: any three points
of S lie on a common plane cubic section of S, so "few curves" can only come from arithmetic, not from degrees of
freedom.

### 5.5 Lattice points near curves in the thin strip; exponent pairs

**Proposition 5.5 (PROVED, elementary).**
(a) *(Pick collinearity.)* Let L := ⌊c·U^{2/3}⌋ with c = c(c₂) > 0 small and U ≥ U₀. The E1 points (k, m) with k in
    any window [k₀, k₀ + L] are collinear.
(b) *(Per-line bound.)* A line with primitive direction (a, −b), a, b ≥ 1, contains at most 2√(2U/(ab)) + 2 points of E1.
    A line with a = 0 or b = 0 contains at most one. Along such a line, s(t) = s₀ + σt − abt² and m(t) = m₀ − bt, so the
    tie becomes integral points on the genus-≤1 quartic w² = s(t)² − 4m(t).
*Proof.*
(a) Write g_j(k) := (p + 2jU)/k (j = 1, 2); E1 points with k ∈ [k₀, k₀+L] lie in {g₁(k) < m ≤ g₂(k)}. As g_j is convex,
    g₁ lies above its tangent t₁ at k₀ and g₂ below its chord c₂ over [k₀, k₀+L]; so the points lie in the convex
    trapezoid {t₁(k) < m ≤ c₂(k), k₀ ≤ k ≤ k₀+L}, of vertical width ≤ 2U/k₀ + (1/2 + 1/8)·max g_j″·L²
    ≤ 2U/k₀ + 1.4pL²/k₀³. Since k₀ ≥ p/(4U²) and p ≥ U⁴/c₂⁴, its area is ≤ 16c₂⁴L/U + 90c₂⁸L³/U², which is < 1/2 for
    L ≤ cU^{2/3}, c = c(c₂) small, U ≥ U₀. A lattice triangle has area ≥ 1/2 (Pick), so no three non-collinear lattice
    points lie in the trapezoid.
(b) Along the line, s(t) is a concave quadratic with leading coefficient −ab. {t ∈ ℝ : s(t) > 2U} is an interval of
    length 2√(Δ/(ab)) (Δ := max s − 2U) and {s(t) > 4U} a sub-interval of length 2√((Δ − 2U)₊/(ab)); since
    √x − √(x − y) ≤ √y, the set {2U < s(t) ≤ 4U} has total length ≤ 2√(2U/(ab)) and contains ≤ 2√(2U/(ab)) + 2
    integers. A fixed k determines m, since the strip has vertical width 2U/k < 1 (k ≥ p/(4U²) > 4U); a fixed m
    determines k (horizontal width 2U/m < 1). ∎
EVIDENCE (§6.2): lines with ≥ 3 points of E1 exist ("major arcs" at rational slopes b/a of small height, e.g.
directions (5, −11), (2, −21), (7, −29)). The longest have 6–18 points. They carry 2.9–6.9 % of E1 at primes with
U = 1000 (4–10 % at odd squares and near-squares) and 2.5–3.4 % at U = 3162; the absolute number grows only like
≈ U^{1/4}. The remaining ≳ 90–97 % of E1 points lie on no line with ≥ 3 points of E1.
*Assessment (near-curve bounds).* Bounds for R(f, N, δ) = #{n ~ N : ‖f(n)‖ < δ} that depend only on derivative sizes
have, for f = p/k, N = U², δ ≍ 1/U and λ₂ ≍ U^{−2}, a natural second-derivative term Nλ₂^{1/3} ≍ U^{4/3}. This exceeds
the divisor bound |E1| ≪ U^{1+ε}. The exact Huxley–Sargos statements were not retrieved (`LIT_CHECK.md` item 1, UNVERIFIED),
so this is not stated as a theorem.
**Deficit.** Geometry gives a power saving only on the major-arc part. On the major arcs the per-line count is
≪ (U/ab)^{1/2}, and the tie is a genus-1 condition per line. The isolated minor-arc points carry no structure that any
line covering can exploit: covering them by lines needs ≳ |E1|/2 lines (EVIDENCE). Exponent pairs and Bombieri–Iwaniec
enter only through Prop 4.3, at f″ = 2νp/k³ ≍ h ≥ 1 (the B-process is self-dual for h ≍ 1).

## 6. Computations (scripts `scripts/z54_bilindiv_*`, data `data/z54/bilindiv/`, ≈ 40 kB)

### 6.1 TD falsifier (EVIDENCE; `z54_bilindiv_td.c`)
Columns: n, U, |E1|, |E1⁺|, N₂, N₄, max_h|T(h)|/√|E1⁺|, argmax, rms_h, |T(1)|/√|E1⁺| (`td_falsifier.txt`, `td_extended.txt`).

| sample | U | H | \|E1\| / \|E1⁺\| | rms_h \|T\|/√\|E1⁺\| | max |
|---|---|---|---|---|---|
| 20 primes ≡ 1 (24) from 10¹² | 1000 | 20 | 2650–2890 / 1450–1640 | 0.83–1.26 | 2.60 |
| 10 odd squares (control) from 10¹² | 1000 | 20 | 2570–2900 / 1390–1650 | 0.92–1.16 | 2.55 |
| 10 near-squares m²+4 from 10¹² | 1000 | 20 | similar | 0.80–1.16 | 2.32 |
| 14 FRONTIER §4 item-14 test primes (U = 3–54; Lemma A needs p ≥ 2¹⁶, so only the shape of T is tested) | 3–54 | 20 | 5–161 / 3–83 | 0.88–1.17 | 2.23 |
| 10 primes ≡ 1 (24) from 10¹⁴ | 3162 | 20 | ≈ 8 650 / 4 800 | 0.79–1.18 | 2.18 |
| 6 primes ≡ 1 (24) from 10¹⁶ | 10⁴ | 20 | ≈ 27 100 / 15 100 | 0.90–1.15 | 2.26 |
| 3 primes from 10¹⁶, extended | 10⁴ | 100 | — | 0.97–1.01 | 2.44 |
| 3 primes ≡ 1 (24) from 10¹⁸, extended | 31 622 | 178 | ≈ 89 250 / 49 750 | 1.02–1.05 | 3.19 |

* |T(h)| is of square-root size at every scale and for every control, up to h ≈ U^{1/2}. This is consistent with TD(η)
  for each η < 1/2, which would give N₂ ≪ U^{3/4+ε} (the same conditional output as MIX).
* |E1| ≈ 2.72U, close to Z53_HYP2CYCLE's model 4 log 2·U = 2.77U for the unrestricted first filter.
* Cross-check: N₂ from the strip form agrees with brute force at 300 consecutive primes > 10⁸
  (`z54_bilindiv_brute.py`; 0 mismatches, ΣN₂ = 113).

### 6.2 Geometry and anatomy filters (EVIDENCE; `z54_bilindiv_geom.c`, `geom.txt`)
Columns: n, U, |E1|, L3 (#lines with ≥ 3 points of E1), Lmax, W (max # of points in a k-window of length ⌊U^{2/3}⌋),
P₁, A1, A2, their ratios to U, cov3 (#points on lines with ≥ 3 points), and the direction of a longest line.
* 10¹² (U = 1000), 20 primes: L3 = 20–46, Lmax = 7–18, W = Lmax in 13/20 cases and W ≤ Lmax in all
  (the script's window ⌊U^{2/3}⌋ is larger than Prop 5.5(a)'s cU^{2/3}, so this is only consistent with, not a test of, (a)), cov3/|E1| = 2.9–6.9 %; odd squares and near-squares: 4.0–9.7 %. A2/U = P₁/U = 0.66–0.73 (identical by Prop 5.3(b)'s symmetry), A1/U = 0.33–0.37.
* 10¹⁴ (U = 3162), 10 primes: L3 = 60–79, Lmax = 6–7, cov3/|E1| ≈ 2.5–3.4 %, A1/U ≈ 0.345.
* Odd squares and near-squares at 10¹² look like primes in every column (cov3 slightly higher). Note that n and n + 4
  have almost the same strip, so the near-square control m² + 4 nearly duplicates the odd square m² here.

### 6.3 Fixed-modulus relaxation of the AP form (EVIDENCE; `z54_bilindiv_untied.py`, `untied.txt`)
At p = 100000081 and 100000097 (U = 100, 7 500 levels): N_rel(1) = 5253 and 4792 (0.53U², 0.48U²); N_rel(4) ≈ 0.45–0.49U²;
N_rel(12) ≈ 0.40–0.44U²; N_rel(840) ≈ 0.31–0.34U²; N_rel(27720) ≈ 0.28–0.30U². The true count is N₂ = O(1).

### 6.4 Do tie events sit on the major arcs? (EVIDENCE; `z54_bilindiv_cyclines.c`, `cyclines.txt.gz`)
For every 2-cycle level k, r(k) := the largest number of E1 points on a line through (k, m_k); control: one E1 point per
prime chosen by index n mod |E1|.
* 8 000 consecutive primes from 10¹⁰ (U = 316): 2 921 cycles; r ≥ 3 for 10.0 % of cycles vs 10.8 % of controls (r ≥ 4:
  5.5 % vs 6.4 %).
* 4 000 consecutive primes from 10¹² (U = 1000): 1 437 cycles; r ≥ 3 for 4.8 % vs 5.2 % (r ≥ 4: 2.6 % vs 3.0 %).
Tie events are *not* concentrated on the strip's major arcs: they are distributed like generic E1 points, so line
geometry has no bias to exploit (falsifier for a "major-arc" route: negative).

## 7. FRONTIER §4 hard screens (best idea: Theorem T / TD)
1. **T1 (odd squares).** Theorem T is an n-uniform upper bound and holds at odd squares, where N₂ can be positive
   (Z53_HYP2CYCLE Prop S). It is silent on positivity by design. EVIDENCE: T(h) is square-root size at odd squares as at
   primes (§6.1), as it must be for an n-uniform input.
2. **8/131.** The argument uses only the strip structure km − n ∈ (2U, 4U] and a square test, so it transfers to other
   numerators: harmless for an upper bound.
3. **Tied modulus.** The tie is the square condition D_k = □ on the strip. The modulus k appears only through
   s_k = −p mod k, a first-order remainder. TD does not break the tie; it would *count* tie events from above.
4. **Fixed p.** Passed: everything is pointwise in p, with averages only over h, k and the strip.

## 8. Verdict

**Narrowed, with one new sufficient condition.**
* **New sufficient condition (PROVED reduction; Theorem T).** A power saving in the first-order strip sums T(h) for
  h ≤ U^η gives N(U, U) ≪ p^{(1−η/2)/4+ε}. EVIDENCE: T(h) is of square-root size at 10¹²–10¹⁸, at primes, odd squares,
  near-squares and test primes. This is compatible with TD(η) for each η < 1/2, which would give N₂ ≪ U^{3/4+ε}.
  TD is an alternative to MIX (first order, but at the self-dual scale). Neither is shown to imply the other.
* **Closed, as scoped statements with exact deficits:**
  * per-variable Fourier implementations of TD are short by h^{1/2}U^{1/2} (Prop 4.3);
  * AP divisor tools are at the x^{2/3} endpoint even for the untied count, and are blind to the tie except through a
    fixed modulus. Their relaxation's main term ≫ U²/log log Q exceeds the trivial bound by p^{1/4} (Prop 5.1;
    Assessment + EVIDENCE);
  * short-interval divisor tools see only E1, of size ≍ U = trivial. An asymptotic for E1 would need Δ-exponent
    ≤ 1/4 against Huxley's 131/416 (§5.2);
  * one-sided anatomy filters retain ≫ U^{1−ε} (Prop 5.3);
  * the black-box determinant method with any pruning is dominated box by box by the elementary per-fibre count
    (Prop 5.4);
  * strip geometry is collinear at scale U^{2/3} (Prop 5.5). Its major arcs carry ≈ 3–10 % of E1, and tie events sit
    on them at the generic rate (EVIDENCE §6.4); the rest lies on no line with ≥ 3 points.
* **Survives:** joint (ν, k) cancellation (the additive analogue of SQSIEVE's bilinear (ℓ, C) estimate); TD or MIX
  themselves; the major-arc part (a power saving there looks reachable, Assessment, but buys nothing on the minor arcs);
  counting the actual auxiliary curves; Salberger/p-adic determinant variants.

## 9. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1 under the z53 bullets:
> * **Balanced block, divisor/geometry angle (`Z54_BILINDIV.md`, z54; internal).** *Theorem T (PROVED reduction):* with
>   E1 the ≍ U lattice points (k, m) of the strip p + 2U < km ≤ p + 4U, m ∈ (U², 4U²], and w_k = √((km−p)² − 4m), a
>   power saving |Σ_{E1} e(h w_k)| ≤ U^{1−η} for h ≤ U^η (hypothesis TD, *first order*: one remainder phase per level,
>   unlike MIX) gives N(U,U) ≪ p^{(1−η/2)/4+ε}. EVIDENCE: square-root size at 10¹²–10¹⁸ incl. odd squares. Scoped
>   closures: per-variable Fourier implementations of TD are short by h^{1/2}U^{1/2} (Prop 4.3, the additive analogue of
>   SQSIEVE B2); divisor-in-AP tools sit at the Selberg–Hooley endpoint q = x^{2/3} and see the tie only through a fixed
>   modulus (relaxed main term ≍ U²); one-sided anatomy (H(x,y,z)) filters keep ≫ U^{1−ε} (Prop 5.3); black-box HB15
>   with any occupancy pruning is dominated box-by-box by "≤ 1 solution per u" (Prop 5.4); strip points are collinear at
>   scale U^{2/3}, major arcs carry ≈ 3–10 % of E1 (EVIDENCE). Missing: a joint (ν, k) cancellation (or TD/MIX).
In §6 add: "balanced block via divisor-in-AP / short-interval divisor / anatomy / black-box determinant (pruned) →
scoped no-gos, `Z54_BILINDIV` §5".

## 10. Bottom line
The balanced block is a count of rare events (probability ≍ 1/U) among ≍ U candidates in every parametrisation. Divisor
and geometry tools control the candidate sets (the strip E1, dom f, the AP n ≡ 1 mod p), but each is blind to the tie.
AP tools see the tie only through a fixed modulus and are at their x^{2/3} endpoint. Anatomy filters keep U^{1−ε}. The
black-box determinant method is dominated by "one solution per u". Strip geometry is collinear only at scale U^{2/3}, and
most points are isolated. What survives is a clean first-order sufficient condition: square-root-sized sums of
e(h√((km−p)² − 4m)) over the strip's lattice points. That condition is numerically true at 10¹²–10¹⁸, but it sits at
the self-dual point, where per-variable methods fall short by U^{1/2}. A joint (ν, k) cancellation is the missing
ingredient, mirroring the bilinear (ℓ, C) gap of the square sieve. Nothing here bears on positivity; ES remains open.

## 11. Reproduction
```
cd $REPO; D=data/z54/bilindiv
gcc -O2 -o /tmp/z54td scripts/z54_bilindiv_td.c -lm; gcc -O2 -o /tmp/z54geom scripts/z54_bilindiv_geom.c -lm
# prime lists: 20/10/6/3 primes = 1 (mod 24) after 1e12/1e14/1e16/1e18 (sympy nextprime), odd squares (m+2i)^2 with
# m = isqrt(1e12)|1, near-squares (m+2i)^2+4, the 14 FRONTIER test primes  (see the inline generator in §6 commands)
ulimit -v 4000000; timeout 900 /tmp/z54td 20 < /tmp/p12.txt        # ~1 s per prime at 1e12, ~1 s at 1e16, ~4 s at 1e18
timeout 1500 /tmp/z54td 178 < /tmp/p18.txt
timeout 1500 /tmp/z54geom < /tmp/p14.txt                           # O(|E1|^2 log): ~10 s per prime at 1e14
timeout 600 uv run python scripts/z54_bilindiv_brute.py < /tmp/p8.txt   # cross-check
timeout 900 uv run --with sympy python scripts/z54_bilindiv_untied.py 100000081 1 4 12 840 27720
gcc -O2 -o /tmp/z54cyc scripts/z54_bilindiv_cyclines.c -lm
timeout 1500 /tmp/z54cyc < /tmp/p10big.txt; timeout 1500 /tmp/z54cyc < /tmp/p12big.txt   # 8000 / 4000 consecutive primes after 1e10 / 1e12; ~10 s
```

## 12. Review log
(pending: hostile review)
