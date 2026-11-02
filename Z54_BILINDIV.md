# Z54_BILINDIV — depth lane BILINDIV (FRONTIER §7.1, gap 1, divisor/geometry angle): the balanced block by divisor sums and strip geometry

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Everything here concerns an **upper bound** (a power saving for one block). It cannot give positivity; its value is
the §7.1 benchmark and method. Each claim carries exactly one label: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Results are internal and internally reviewed only.

Brief: `z52bbriefs/z53_depth.md` (wave z54), kickoff `z52bbriefs/z54_lanes.md` §BILINDIV (target as §BILINJAC).
Scripts `scripts/z54_bilindiv_*`, data `data/z54/bilindiv/`. Checkpoint 1: commit 525f71c3. Hostile review:
`reviews/z54_bilindiv_review1.md`, applied (§12).

**Verdict: narrowed, with one new sufficient condition** (§8). No power saving for the balanced block is proved.
* **New sufficient condition.** A power saving follows from a first-order hypothesis TD on a smooth phase summed over the
  lattice points of the thin hyperbolic strip. TD(η) gives N₂ ≪ U^{1−η+ε} (Theorem T). It stands alongside
  Z53_HYP2CYCLE's second-order MIX.
* **Tool classes.** Each divisor/geometry tool class of the kickoff gets a scoped statement for a specified
  implementation, with its deficit (§5).
* **Common pattern** (Assessment). In the two most economical parametrisations (dom f and the strip set E1), the
  candidate sets have size ≍ U, while the tie has probability ≍ 1/U. The specified one-variable implementations do not
  see it; a joint (bilinear) cancellation would be needed.

## 0. Notation

* p is an odd prime and U ≥ 2 an integer with 16U³ ≤ p; 𝔅 := (U, 2U]².
* The *fourth-root range* is c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, with fixed 0 < c₁ ≤ c₂ and p ≥ p₀(c₂) so that 16U³ ≤ p. For
  U = ⌊p^{1/4}⌋ this means p ≥ 2¹⁶. Implied constants may depend on c₁, c₂.
* N₂(p, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | p + u + B}, the 2-cycles of the remainder map (Z53_HYP2CYCLE). For
  composite odd n we use this product-divisibility definition, not the two separate divisibilities.
* k := (p+u+B)/(uB) is the *level*; N₄ ≤ N₂ is the sub-count with 4 | k. The balanced (★) block is N(U, U) = 2N₄
  (Z52D Prop 2).
* Trivial bound: N₄ ≤ N₂ ≤ U/2. EVIDENCE: mean N₂ ≈ 0.36 (Z53_HYP2CYCLE §4).
* **Target R2 (FRONTIER §7.1).** There is η > 0 such that N₂(p, U) ≪ U^{1−η} for all primes p and all U in the
  fourth-root range. This implies N(U, U) ≪ U^{1−η}.
* Strip variables (Z53_HYP2CYCLE Lemma A). For a level k put s_k := (−p mod k), m_k := (p + s_k)/k and
  D_k := s_k² − 4m_k.
  * **E1** := {k : s_k ∈ (2U, 4U], m_k ∈ (U², 4U²]}. Equivalently, E1 is the set of lattice points (k, m) of the thin
    hyperbolic strip p + 2U < km ≤ p + 4U with U² < m ≤ 4U².
  * E1⁺ := {k ∈ E1 : D_k ≥ 1} and w_k := √D_k ∈ ℝ for k ∈ E1⁺. On E1 the discriminant D_k can be negative; 42–45 %
    of E1 lies outside E1⁺ in the data.
* **Lemma A** (Z53_HYP2CYCLE; needs 16U³ ≤ p, so every level exceeds 4U). Under that condition
  N₂ = #{k ∈ E1⁺ : D_k = w² with w ∈ ℕ and (s_k ± w)/2 ∈ (U, 2U]}, and the map {u, B} ↦ k is injective. The condition
  m_k ∈ (U², 4U²] holds for every 2-cycle, since m = uB.

## 1. Statements attacked

(A) **Target R2** (OPEN). For each tool class of the kickoff we either turn it into a power saving, or close a
specified implementation of it by a scoped statement with its deficit:
1. divisor function in APs (Selberg–Hooley, Fouvry–Iwaniec) → §5.1;
2. divisors in short intervals and the Dirichlet-divisor exponent → §5.2;
3. anatomy, i.e. Tenenbaum/Ford H(x,y,z) ("has a divisor in a range") → §5.3;
4. determinant method (Bombieri–Pila / Heath-Brown) with occupancy pruning → §5.4;
5. lattice points near curves in the thin strip; exponent pairs / Bombieri–Iwaniec → §5.5 and §4.3.

(B) **Theorem T** (PROVED; §4). A power saving (not beyond-square-root) in the strip sums

  T(h) := Σ_{k ∈ E1⁺} e(h·w_k) = Σ_{(k,m) ∈ ℤ²: p+2U < km ≤ p+4U, U² < m ≤ 4U², (km−p)² − 4m ≥ 1} e(h√((km − p)² − 4m))

for 1 ≤ h ≤ U^η implies R2. We call this hypothesis **TD(η)**. T(h) is a *first-order* object: a smooth phase of one
remainder per level, summed over the lattice points of the strip. Equivalently, it is a sum over the divisors d of the
integers p + s, s ∈ (2U, 4U], with d ∈ (U², 4U²]. Z53_HYP2CYCLE's MIX is second order in the remainder map.

(C) **Exact forms** of the balanced block in divisor and strip language (§3, PROVED).

## 2. Why this is not already closed

* **Z52D.** It closed one-step dualization at fixed conductor, ET/Fejér with max|S_h| and square-root input, and
  Cauchy–Schwarz in the function variable. Its R1 (beyond-square-root 2D sums) is numerically false at 10¹². None of
  these is a strip or divisor-sum argument.
* **Z53_HYP2CYCLE.** It closed only the *black-box* determinant method: the HB14/HB15 bound times a uniform per-curve
  bound, on the full box or a full grid. It reduced R2 to MIX (second order). Occupancy pruning, specific curves and
  first-order strip formulations were left open (Prop D scope).
* **Z53_SQSIEVE Prop B2.** It closed the k-Poisson square sieve with triangle inequality over frequencies. It names as the
  missing input "χ_Q-twisted divisor sums near √m of integers in an interval of length m^{1/4}". That is the same
  strip, with multiplicative twists; this lane uses additive twists e(h·w) and pure counting tools.
* **Repo search.** No scoped statement about the balanced block exists for the five tool classes. `git grep` finds:
  * Ford's H(x,y,2y) only in literature catalogues (`BRAINSTORM/z52_lit_divisor_class.md`, as an ambient B6 count);
  * Sargos only as a lemma inside Bourgain's exponent-pair proof (`data/z53/sqsieve/LIT_CHECK.md`);
  * Hooley, Shiu and Tenenbaum only in brainstorm lists or unrelated memos.

## 3. Exact forms and sizes at the balanced block

**Lemma 3.1 (five forms; PROVED).** Let p be prime and 16U³ ≤ p. All variables below are positive integers, and w is
an integer. N₂(p, U) equals each of:
(a) *pair form:* #{{u,B} ⊂ (U,2U] : u | p + B, B | p + u}. At primes, gcd(u,B) | p forces coprimality, so the two
    divisibilities give uB | p + u + B.
(b) *strip form:* #{(k, m) : p + 2U < km ≤ p + 4U, D := (km−p)² − 4m = w² with w ≥ 1, (km − p ± w)/2 ∈ (U, 2U]}.
(c) *divisor form:* Σ_{s ∈ (2U, 4U]} #{d | p + s : s² − 4d = w² with w ≥ 1, (s ± w)/2 ∈ (U, 2U]}.
(d) *trial form:* #{(u, k) : u ∈ (U, 2U], (ku − 1) | (p + u), B := (p + u)/(ku − 1) ∈ (U, 2U], B > u}.
(e) *modular-hyperbola form:* #{(X, Y) : XY ≡ 1 (mod p), k := (XY − 1)/p, k | X + 1, (X+1)/k and (Y+1)/k ∈ (U, 2U],
    X < Y}.
*Proof.*
* (a) is Z52D Prop 2.
* (b) is Lemma A with m = m_k.
* (c) substitutes d = m and s = km − p.
* (d): kuB − u − B = p ⟺ B(ku − 1) = p + u.
* (e): (ku − 1)(kB − 1) = kp + 1. Conversely, XY = kp + 1 with k | X + 1 gives Y ≡ −1 (mod k), because XY ≡ 1 (mod k).
∎
*Sizes in the fourth-root range* (PROVED from the definitions):
* d = m = uB ∈ (U², 4U²], and d ≍ √p;
* the integers p + s run over an interval of length 2U ≍ p^{1/4};
* the levels satisfy k ≍ p/U² ≍ √p;
* X = ku − 1 and Y = kB − 1 satisfy X, Y ≍ p/U ≍ p^{3/4};
* n = kp + 1 ≍ p^{3/2}.

**Algebra reading (PROVED).** For k ∈ E1 let A_k := ℤ[t]/(t² − s_kt + m_k), with involution t ↦ s_k − t. Write α for
the class of t and ᾱ = s_k − α. Then p + ᾱ = p + s_k − α = kαᾱ − α = α(kᾱ − 1), so α | p + ᾱ in A_k. Thus E1 is the set
of "2-cycles in rank-two algebras".
* A_k is an order in a quadratic étale algebra when D_k ≠ 0.
* It is split, A_k ≅ ℤ × ℤ, exactly when D_k is a nonzero square. Lemma A's count consists of split k with the size
  condition.
* D_k = 0 gives a nonreduced algebra and corresponds to u = B, which is excluded.

**Table 3.2 (candidate sets and tie events).** Each entry carries its own label.

| parametrisation | candidate set | its size | tie event | remainder order |
|---|---|---|---|---|
| u ↦ f(u) (HYP2CYCLE) | dom f | ≥ U/6 − O(U^{14/15}) (PROVED, Prop 5.3); ≈ U log 2 (EVIDENCE) | f(f(u)) = u; heuristic prob ≍ 1/U | **second** (MIX) |
| level k (this memo) | E1 | ≪ U^{1+ε} (PROVED); ≈ 2.7–2.8U (EVIDENCE) | w_k ∈ ℤ; heuristic prob ≍ 1/U | **first**, but window width ≍ 1/U |
| (u, B) ∈ 𝔅 (Z52D R1) | all of 𝔅 | U² | uB \| p+u+B; heuristic prob ≍ 1/U² | first in each variable; needs beyond-√ |
| (X, Y), XY ≡ 1 (p) | points in a box of side ≍ p^{3/4} | ≍ U² (Assessment, model; Weil-critical box) | k \| X+1; heuristic prob ≍ 1/U² | — |
| k-form AP n = kp+1 | divisors X ∈ (kU,2kU] of n ≡ 1 (mod p) | ≈ 0.5U² at U = 100 (EVIDENCE, §6.3) | X ≡ −1 (mod (n−1)/p); heuristic prob ≍ 1/U² | tied modulus |

**Exponents in p.** U ≍ p^{1/4}, levels k ≍ p^{1/2}, m = uB ≍ p^{1/2}, X, Y ≍ p^{3/4} and n = kp + 1 ≍ p^{3/2}. The
trivial bound is p^{1/4}; the expected count is O(1).

## 4. Theorem T: the strip sums suffice, and why they are hard

### 4.1 Statement

Fix ψ ∈ C_c^∞(−2, 2) with 0 ≤ ψ ≤ 1 and ψ = 1 on [−1, 1]. For 0 < δ ≤ 1/2 put χ_δ(x) := Σ_{j∈ℤ} ψ((x + j)/δ). This is a
smooth 1-periodic function with χ_δ ≥ 1 on ℤ + [−δ, δ] and Fourier coefficients χ̂_δ(h) = δψ̂(δh).

**Theorem T (PROVED).** For every ε > 0 and A ≥ 2 there is C = C(ψ, ε, A) with the following property. For every prime p,
every integer U ≥ 2 with 16U³ ≤ p, and every 0 < δ ≤ 1/2, put H := U^ε/δ. Then

  N₂(p, U) ≤ 4δ·|E1⁺| + 8δ·Σ_{1≤h≤H} |T(h)| + C·|E1⁺|·U^{−εA}.

*Proof.*
* By Lemma A, each 2-cycle gives a distinct k ∈ E1⁺ with w_k ∈ ℤ, and χ_δ(w_k) ≥ 1 there. Since χ_δ ≥ 0,
  N₂ ≤ Σ_{k∈E1⁺} χ_δ(w_k).
* The Fourier series of χ_δ converges absolutely (ψ̂ is Schwartz), so the right side equals Σ_{h∈ℤ} δψ̂(δh)T(h). Here
  T(0) = |E1⁺| and T(−h) is the complex conjugate of T(h).
* Since |ψ̂| ≤ ‖ψ‖₁ ≤ 4, the h = 0 term is at most 4δ|E1⁺|, and the terms with 1 ≤ |h| ≤ H total at most
  8δΣ_{1≤h≤H}|T(h)|.
* For |h| > H use |ψ̂(ξ)| ≤ C_A|ξ|^{−A}. Then Σ_{|h|>H} δ|ψ̂(δh)||T(h)| ≤ 2C_A|E1⁺|Σ_{h>H} δ(δh)^{−A}
  ≪_A |E1⁺|(δH)^{1−A} = |E1⁺|U^{−ε(A−1)}.
* Renaming A − 1 → A gives the claim. ∎

**Hypothesis TD(η)** (0 < η ≤ 1/2). There is C₀ such that |T(h)| ≤ C₀U^{1−η} for all 1 ≤ h ≤ U^η, uniformly for primes p
and U in the fourth-root range.

**Corollary T (CONDITIONAL on TD(η)).** For every ε > 0, N₄ ≤ N₂ ≪_{η,ε,C₀} U^{1−η+ε} uniformly in the fourth-root
range. Hence N(U, U) ≪ p^{(1−η)/4+ε}, and TD(η) for every η < 1/2 would give N₂ ≪_ε U^{1/2+ε}.
*Proof.*
* *Size of E1.* Each k ∈ E1 is a divisor of p + s_k with s_k ∈ (2U, 4U], and k determines s_k. Hence
  |E1⁺| ≤ |E1| ≤ Σ_{s∈(2U,4U]} τ(p + s) ≪_ε U^{1+ε/2}, using τ(n) ≪ n^{o(1)} and p ≍ U⁴.
* *Parameters.* Fix 0 < ρ < min(η, ε)/2 and take δ := U^{−η+ρ}, which is ≤ 1/2 for U ≥ U₀(η, ρ). Apply Theorem T with ρ/2
  in place of ε, so that H = U^{η−ρ/2} ≤ U^{η}.
* *Main term.* 4δ|E1⁺| ≪ U^{1−η+ρ+ε/2}.
* *Frequency terms.* 8δΣ_{h≤H}|T(h)| ≤ 8δH·C₀U^{1−η} = 8C₀U^{1−η+ρ/2}.
* *Tail.* It is ≪ U^{1+ε/2−ρA/2}, which is ≤ U^{1−η} once A ≥ 4/ρ.
* *Small U.* For U < U₀ the bound is trivial (N₂ ≤ U/2). ∎

Shiu's theorem would replace U^{ε} by a power of log p; its exact statement was not re-verified here
(`data/z54/bilindiv/LIT_CHECK.md` item 2), so it is not used.

**Remark 4.1 (the small-difference range is free; smooth form of TD).**
* *Small differences (PROVED).* The 2-cycles with B − u = w ∈ [1, W₀] number at most Σ_{w≤W₀} τ(p + w) ≪ W₀U^{ε}.
  Indeed u | p + B = p + u + w gives u | p + w, so u is a divisor of p + w and B = u + w is then determined. With
  W₀ = U^{1−η} this range is within the target.
* *Consequence.* TD is needed only on {k ∈ E1 : D_k ≥ W₀²}, i.e. for W := w_k ∈ [U^{1−η}, 4U]. There the curvature
  |hW_k″| ≪ hU³·U^{3η}.
* *Smooth form.* Theorem T's proof works verbatim with the sharp indicator of E1⁺ replaced by a smooth partition of
  unity in (s/U, m/U², w/W) over dyadic W ∈ [U^{1−η}, 4U]. The hypothesis then reads |Σ_k Φ_W(k)e(hw_k)| ≤ U^{1−η}
  for each smooth piece Φ_W. Prop 4.3 below treats the top piece W ≍ U.

### 4.2 What TD is, and how it compares with MIX (Assessment unless labelled)

* **First order** (PROVED identity). T(h) = Σ_k G_h(k, θ_k), with θ_k := {−p/k}, s_k = kθ_k, and
  G_h(k, θ) := 1[kθ ∈ (2U, 4U], (p + kθ)/k ∈ (U², 4U²], W_k(θ)² ≥ 1]·e(hW_k(θ)), where
  W_k(θ) := √(k²θ² − 4(p + kθ)/k).
  So each term depends on the level and on a *single* remainder phase. MIX (Z53_HYP2CYCLE Thm R) needs the joint law of
  (θ_u, θ_{f(u)}).
* **Curvature** (PROVED identity: W_k″(θ) = −4(kp + 1)/W_k(θ)³, from differentiating W² = k²θ² − 4p/k − 4θ twice). In
  the top range W_k ≍ U (equivalently D_k ≍ U², which Prop 4.3 isolates) one has |hW_k″| ≍ hU³. Across the window of
  width ≍ 1/U the function hW_k sweeps an interval of length ≍ hU. Smaller W (pairs with u close to B) give larger
  curvature and need a dyadic decomposition in W. W ≤ U^{1−η} is free (Remark 4.1); the intermediate range is not
  analysed here.
* **Critical scale.** In the top range, resolving the event needs the joint law of (k, θ_k) at resolution ≍ 1/(hU²).
  That means Weyl sums Σ_k e(νp/k) with ν up to ≍ hU² and k ≍ U². The phase f(k) = νp/k has f′ ≍ hU² and
  f″ = 2νp/k³ ≍ h ≥ 1. The B-process maps the k-sum (length ≍ U²) to a dual of length ≍ f″·U² ≍ hU², so it is
  self-dual at h ≍ 1. This is the regime of Σ_{k≍x^{1/3}} e(x/k), not the hyperbola point of the divisor problem.
* **Reading in u*** (PROVED identity). For k ∈ E1⁺ let u*_k := (s_k − w_k)/2, the smaller real root of z² − s_kz + m_k.
  Since s_k ∈ ℤ, e(hw_k) = e(−2hu*_k). So TD controls exactly the *even* Fourier modes of u*_k mod 1. Translating this
  into a statement about divisors of p + s relative to the grid {u(s − u)} would need parity information and explicit
  discrepancy statements; this is not done here.
* **Double dual** (Assessment; stationary-phase heuristic, not used anywhere). After the θ-expansion of §4.3 and a
  further Poisson step in k (phase −νp/k − μk, stationary at k* = √(νp/μ)), T(h) becomes a 2D sum over
  (ν, μ) ≍ (hU², hU²). Its leading phase is −2√(p·νμ) and its amplitude is ≍ U^{−3/2}h^{−1}.
  * This is a Voronoi-type piece of the divisor problem at x ≍ p, with n = νμ ≍ h²p, at the hyperbola point
    ν ≍ μ ≍ √n, carrying factorisation-dependent lower-order phases.
  * Square-root cancellation there gives ≍ U^{1/2}. Per-ν exponent pairs give ≫ U^{3/2}, since any pair has κ + λ ≥ 1/2.
  * So the missing joint cancellation looks like a bilinear divisor-problem-type estimate.
* **Relation to MIX.**
  * Neither TD nor MIX is shown to imply the other.
  * Both ask only for a power saving in a sum of about U terms. EVIDENCE: both are numerically of square-root size
    (§6.1; Z53_HYP2CYCLE §5.3).
  * TD(η) gives N₂ ≪ U^{1−η+ε} because the detection is one-dimensional. Z53_HYP2CYCLE's stated MIX corollary is
    U^{1−η/2+3ε}, from a 2D torus majorant; we do not re-optimise it.

### 4.3 Proposition 4.3 (per-variable implementations for the smoothed top-range strip sum; PROVED)

This is the strip analogue of Z53_SQSIEVE Prop B2. It concerns a smoothed, localised sub-sum T_φ of T, not T itself.
* **Scope.** A positively weighted sub-sum of a complex sum is not bounded by the full sum's modulus, so this
  proposition says nothing about TD for T directly.
* **Why T_φ is the natural object** (Assessment). Theorem T holds verbatim with the sharp E1⁺ replaced by smooth weights
  that are ≥ 1 on the 2-cycle levels, after a dyadic decomposition in W. The pieces with W ≍ U are sums of the form T_φ.

**Setup.**
* Fix φ ∈ C_c^∞((5/2, 7/2)) with 0 ≤ φ ≤ 1 and φ ≢ 0, and the level range 𝒦′ := [p/(1.5U²), 0.99p/U²]. Put
  T_φ(h) := Σ_{k∈𝒦′} φ(s_k/U)·e(h·w_k).
* On its support, s_k ∈ (2.5U, 3.5U) and m_k ≤ 1.5U²(1 + O(1/U³)). So D_k ≥ 0.2U² and m_k > U² for U ≥ U₀, and these
  k lie in E1⁺.
* Put G_k(θ) := φ(kθ/U)·e(hW_k(θ)). It is smooth and supported in (2.5U/k, 3.5U/k) ⊂ (0, 1). Extend it 1-periodically
  and write G_k(θ) = Σ_ν c_ν(k) e(νθ). Since θ_k = {−p/k}, e(νθ_k) = e(−νp/k), and (exact identity)
  T_φ(h) = Σ_{ν∈ℤ} Σ_{k∈𝒦′} c_ν(k) e(−νp/k).

**Implementation class.** Fix ν₁ := hU. An *implementation* is any argument that
* (i) uses this expansion,
* (ii) applies the triangle inequality over ν, and
* (iii) bounds each k-sum with |ν| ≥ ν₁ by some b_ν ≥ c₀·(Σ_k |c_ν(k)|²)^{1/2}, for a fixed c₀ > 0, i.e. no better than
  square root in the k-sum. Frequencies |ν| < ν₁ may be bounded in any way.

Condition (iii) is an *assumption* defining the class. For direct exponent-pair bounds, applied with a global
partial-summation amplitude factor on the summation interval, it holds when |ν| ≥ ν₁:
* the phase νp/k has F/K² ≍ |ν|/U² ≫ 1/U and F/K ≥ 1;
* the bound is then ≥ max_k|c_ν(k)|·|𝒦′|^{1/2} ≥ ‖c_ν‖₂, since κ + λ ≥ 1/2;
* subdividing the interval keeps this, because Σ_J ‖c_ν‖_{2,J} ≥ ‖c_ν‖₂.
Derivative tests used after subdivision, Bombieri–Iwaniec, and arguments exploiting the phase of c_ν(k) are covered only
insofar as they satisfy (iii).

**Proposition 4.3.** In the fourth-root range, for U ≥ U₀ and 1 ≤ h ≤ U, every implementation gives |T_φ(h)| ≤ Σ_ν b_ν
with Σ_{|ν|≥ν₁} b_ν ≥ c·h^{1/2}U^{3/2}, where c > 0 depends on φ, c₀, c₁, c₂.
* The reverse order — summing ν first, then the triangle inequality over k — gives exactly Σ_k φ(s_k/U), the trivial
  bound.
* So in this class neither order beats the trivial size ≍ U.
* The missing input is a *joint* (ν, k) cancellation, of size h^{1/2}U^{1/2+η} beyond per-line square root. This is the
  additive-twist analogue of SQSIEVE's missing bilinear (ℓ, C) estimate.

*Proof.*
* *Parseval.* Σ_ν |c_ν(k)|² = ∫₀¹ φ(kθ/U)²dθ = (U/k)‖φ‖₂². Summed over k ∈ 𝒦′ this is ≥ ‖φ‖₂²·U·Σ_{k∈𝒦′}1/k ≥ c₃U, since
  the range has ratio 1.485.
* *Low frequencies are negligible.*
  * On the support, k²θ = ks ≥ 2.5U·p/(1.5U²) and W ≤ 3.5U, so hW_k′ = h(k²θ − 2)/W ≫ hU².
  * For |ν| < ν₁ = hU, the phase hW_k − νθ therefore has derivative ≫ hU², and each integration by parts gains
    ≪ 1/(hU). Here the amplitude has scale k/U ≍ U and |hW″|/(hW′)² ≪ 1/(hU).
  * So Σ_{|ν|<ν₁}|c_ν(k)|² ≪_A hU·(U/k)²(hU)^{−2A}, which is ≤ (U/2k)‖φ‖₂² for U ≥ U₀. Hence
    Σ_{|ν|≥ν₁}Σ_k|c_ν(k)|² ≥ c₃U/2.
* *Pointwise bound.*
  * c_ν(k) = ∫ φ(kθ/U)e(hW_k(θ) − νθ)dθ. The phase has second derivative hW_k″ = −4h(kp+1)/W_k³, of constant sign.
  * W_k ≤ 3.5U and k ≥ p/(1.5U²), so |hW_k″| ≥ 4hkp/(3.5U)³ ≥ hp²/(16.1U⁵) ≥ hU³/(16.1c₂⁸) =: λ.
  * Titchmarsh's second-derivative lemma (*Theory of the Riemann zeta-function*, Lemma 4.4: |∫e^{iF}| ≤ 8/√r if
    |F″| ≥ r), combined with one integration by parts against the amplitude, bounds the integral by
    (8/√(2πλ))(sup|amp| + total variation). The total variation of θ ↦ φ(kθ/U) equals that of φ.
  * Hence |c_ν(k)| ≤ C₄(hU³)^{−1/2}.
* *ℓ² size per frequency.* For every ν, Σ_k |c_ν(k)|² ≤ |𝒦′|·C₄²/(hU³) ≤ C₅/(hU), because |𝒦′| ≤ p/U² ≤ U²/c₁⁴.
* *Conclusion.* Σ_{|ν|≥ν₁} b_ν ≥ c₀Σ_{|ν|≥ν₁}‖c_ν‖₂ ≥ c₀(Σ_{|ν|≥ν₁}‖c_ν‖₂²)/max_ν‖c_ν‖₂ ≥ c₀(c₃U/2)(hU/C₅)^{1/2}.
* *Reverse order.* Σ_ν c_ν(k)e(−νp/k) = G_k(θ_k), since the Fourier series converges absolutely, and |G_k(θ_k)| =
  φ(s_k/U). ∎

## 5. Tool classes: scoped statements with deficits

### 5.1 Divisor function in arithmetic progressions (Selberg–Hooley; Fouvry–Iwaniec)

**Proposition 5.1(a) (PROVED; arithmetic of the AP form).** By Lemma 3.1(e), with k := (n−1)/p,
  N₂ = Σ_{n ≡ 1 (mod p), (n−1)/p ∈ 𝒦} #{X | n : X, n/X ∈ (kU, 2kU], X ≡ −1 (mod k), X < n/X}.
Here 𝒦 is the level range; X ≡ −1 (mod k) forces n/X ≡ −1 (mod k), since n ≡ 1 (mod k).
* The progression has modulus q = p and length x/q ≍ U², with x ≍ U²p ≍ p^{3/2}. So q ≍ x^{2/3}: the 2/3 endpoint.
* The classical asymptotic for Σ_{n≤x, n≡a (q)} τ(n) holds uniformly for q < x^{2/3−ε}, with error (q^{1/2} + x^{1/3})x^ε.
  This is as quoted in Fouvry–Iwaniec (Acta Arith. 61 (1992)); VERIFIED-PRIMARY in `LIT_CHECK.md` item 3.
* Here both error terms are ≍ p^{1/2+ε}, against a main term ≍ U² log p ≍ p^{1/2} log p. So direct insertion fails by
  p^{ε}, even for the *untied* divisor sum along this progression.
* Fouvry–Iwaniec's Theorem 1 goes beyond x^{2/3} only *on average*. For squarefree r ≤ x^{3/8} with (a, r) = 1, it
  bounds Σ_{rs² < x^{1−6ε}, (s,ar)=1} |Δ_f(x; rs, a)| by ≪ r^{−1}x^{1−ε}, over the moduli rs. It gives no
  individual-prime-modulus estimate.

**Proposition 5.1(b) (Assessment; model main term, fixed Q).** For a modulus Q *fixed independently of p*, consider the
relaxed count
  N_rel(Q) := Σ_{k∈𝒦} #{X | kp+1 : X ∈ (kU, 2kU], X ≡ −1 (mod gcd(k, Q))} ≥ N₂.
* Its CRT-model main term is ≍ U²·avg_k 1/φ(gcd(k, Q)) ≫ (φ(Q)/Q)U². This exceeds the trivial bound by ≍ U.
* EVIDENCE (§6.3): at p = 100000081 and 100000097 (U = 100), N_rel(1) = 0.53U² and 0.48U², and N_rel(27720) = 0.30U² and
  0.28U², while N₂ = 1 and 0.
* *Scope.* The statement is only about fixed Q. If Q is allowed to depend on p, e.g. Q = lcm of all levels, then
  gcd(k, Q) = k and the full tie is imposed. In that case N_rel(Q) ≤ Σ_u τ(p + u) ≪ U^{1+ε}.

**Deficit (Assessment).** The specified fixed-Q relaxation has main term ≍ U², a factor ≍ p^{1/4} above the trivial bound.
The untied AP asymptotic is at the 2/3 endpoint.

### 5.2 Divisors in short intervals; the Dirichlet-divisor exponent

By Lemma 3.1(c), E1 ⊂ {(s, d) : d | p + s, s ∈ (2U, 4U]}. These are divisors d ∈ (U², 4U²], d ≍ √p, of the integers
p + s in an interval of length 2U ≍ p^{1/4}.
* **Upper bound** (PROVED). |E1| ≤ Σ_s τ(p+s) ≪ U^{1+ε}. No asymptotic is needed for upper bounds.
* **Asymptotic for |E1|** (Assessment).
  * Direct insertion of Huxley's bound Δ(x) ≪ x^{131/416+ε} (Huxley 2003; `LIT_CHECK.md` item 5) gives
    Σ_{x<n≤x+y}τ(n) ~ y log x for y ≥ x^{131/416+ε}. Our y ≍ x^{1/4} falls short of that by 131/416 − 1/4 = 27/416 ≈ 0.065
    in the exponent of x = p.
  * The claimed Bourgain–Watt improvement is withdrawn and is not used.
  * A short-interval asymptotic could also come from cancellation in Δ(x+y) − Δ(x). Restricted divisor sums
    (d ≍ √n) need separate analysis anyway. No impossibility is claimed.
* **Blind to the tie.** The tie is the *square* condition on top of E1. Short-interval divisor bounds control E1 but not
  this condition: s² − 4d = □ is not a divisor condition on p + s. TD (§4) is the additively twisted short-interval
  divisor sum that would be needed. Prop 4.3 shows that its per-variable Fourier implementations (top W-range) fall
  short by h^{1/2}U^{1/2}.
* **Deficit** (Assessment). Untwisted tools reach only |E1| ≪ U^{1+ε}, which is the trivial bound up to U^{ε}.

### 5.3 Anatomy filters (Tenenbaum/Ford H(x,y,z))

**Proposition 5.3 (PROVED).** In the fourth-root range, for U ≥ U₀(c₁, c₂), each one-sided divisibility filter retains a
positive power of U:
(a) |dom f| = #{u ∈ (U,2U] : some B ∈ (U,2U] has u | p + B} ≥ U/6 − O(U^{14/15});
(b) #{u ∈ (U,2U] : p + u has a divisor in (U, 2U]} ≫_ε U^{1−ε}.
So an argument that bounds N₂ by the number of u passing one of the two divisibility conditions, or an anatomy condition
implied by it ("p + u has a divisor in (U, 2U]", Ford's H-type event), saves at most U^{o(1)}. The tie is the
*coincidence* of the two conditions.
*Proof of (a).*
* Let θ_u := {−p/u}. If u ∈ (1.5U, 2U] and θ_u ∈ (2/3, 1), then B := uθ_u = (−p mod u) satisfies B > (2/3)(1.5U) = U and
  B < u ≤ 2U, so u ∈ dom f.
* The number of such u is (1/3)(U/2) + O(U·𝒟), where 𝒟 is the discrepancy of (θ_u)_{u∈(1.5U,2U]}.
* By Erdős–Turán, 𝒟 ≪ 1/H + Σ_{h≤H}h^{−1}U^{−1}|Σ_u e(hp/u)|.
* Take f(u) = hp/u, so f⁗ = 24hp/u⁵, with ratio max/min ≤ (4/3)⁵ on the range and λ₄ ≍ hp/U⁵ ≍ h/U in the fourth-root
  range. The fourth-derivative test (Titchmarsh, Thm 5.13, with k = 4 and K = 8) gives
  Σ_u e(hp/u) ≪ Uλ₄^{1/14} + U^{3/4}λ₄^{−1/14} ≪ h^{1/14}U^{13/14} + U^{11/14}.
* Hence 𝒟 ≪ 1/H + H^{1/14}U^{−1/14} + U^{−3/14}log H, and H = U^{1/15} gives 𝒟 ≪ U^{−1/15}.
*Proof of (b).*
* Let P₁ := #{(u, B) ∈ (U,2U]² : B | p + u}. Each B has at most one u ≡ −p (mod B) in an interval of length U < B.
  So P₁ = #{B : some u ∈ (U,2U] has u ≡ −p (mod B)}, which is |dom f| with the letters exchanged. By (a),
  P₁ ≥ U/6 − O(U^{14/15}).
* By Cauchy–Schwarz, P₁² ≤ #{u : p+u has a divisor in (U,2U]}·Σ_u τ(p+u)².
* Finally Σ_u τ(p+u)² ≤ U·max_{n≤2p}τ(n)² ≪ U^{1+ε}. ∎
**EVIDENCE (§6.2).** P₁/U = |dom f|/U = 0.66–0.73 (log 2 ≈ 0.693), and the count in (b) is 0.33–0.38U at 10¹² and 10¹⁴.
The values at odd squares and near-squares are similar to those at primes.
**Deficit.** The full power U^{1−o(1)}. Ford's (log y)^{−δ}(log log y)^{−3/2} factor (Ann. of Math. 168 (2008),
Cor. 2) is an ambient density over n ≤ x. Prop 5.3(b) shows that nothing better than U^{1−ε} can come from the
one-sided event at a single p.

### 5.4 Determinant method with occupancy pruning (Bombieri–Pila / Heath-Brown)

Z53_HYP2CYCLE Prop D concerns F = kuB − u − B − p. On any translated box |x_i − c_i| ≤ B_i with radii 2 ≤ B₁, B₂, B₃
(for u, B, k), it shows that the auxiliary-surface bound X of Heath-Brown's Theorem 15 satisfies X ≥ min(B_i)^{2/√3}.
That statement is taken from the restatements by Reuss and by Browning–Heath-Brown; the multi-affine F keeps
T = B₁B₂B₃ under translation. The displayed expression is ≥ 1 because log‖F‖ ≥ log p ≥ 1.

**Proposition 5.4 (domination by the elementary per-fibre bound; PROVED relative to HB15 as restated).**
* *Setup.* Let 16U³ ≤ p and let Sol := {(u, B, k) : u < B, {u,B} a 2-cycle at level k}, the unordered pairs.
* *One solution per fibre.* Every value of u, every value of B and every value of k carries at most one point of Sol.
  So a box Q with side lengths a, b, c satisfies |Q ∩ Sol| ≤ min(a, b, c) + 1.
* *Comparison.* X(Q) ≥ max(1, (min(a,b,c)/2)^{2/√3}) ≥ (min(a, b, c) + 1)/5 ≥ |Q ∩ Sol|/5. The first inequality uses
  Prop D with radii (side)/2 when all sides are ≥ 4, and X ≥ 1 otherwise.
* *Consequence.* Take any family 𝒬′ of boxes covering Sol, with any occupancy pruning. Any bound obtained from HB15 as a
  black box (X(Q) times a per-curve bound ≥ 1) is at least a fifth of the elementary per-fibre bound
  Σ_{Q∈𝒬′}(min side(Q) + 1) on the same family. So the black-box determinant method is dominated box by box by
  "≤ 1 solution per u".
* *What a saving would need.* A power saving by this route needs the weighted occupancy condition
  Σ_{Q∈𝒬′}(min side(Q) + 1) ≪ U^{1−η} — a coarse form of the target itself.
*Proof.*
* *Same u.* u(k₁B₁ − k₂B₂) = B₁ − B₂ with |B₁ − B₂| < U < u, so B₁ = B₂ and then k₁ = k₂. Same B: symmetric.
* *Same k.* By Lemma A (16U³ ≤ p) a level carries one unordered pair, which is one point of Sol. The ordered triples
  (u, B, k) and (B, u, k) share k; the example p = 100000037, U = 100, {115, 168}, k = 5176 shows why Sol is unordered.
* *Integer counts.* A side of length a contains ≤ a + 1 integers.
* *The inequality.* For t ≥ 4, (t/2)^{2/√3} ≥ t/2 ≥ (t + 1)/5; for t < 4, (t + 1)/5 < 1 ≤ X. ∎
*Scope.* This covers black-box HB15 with arbitrary pruning. It does not cover arguments that bound the *actual* number
of auxiliary curves below X(Q), Salberger's global method, or p-adic/Coppersmith variants. Any three points of the
surface lie on a plane cubic section of it, so "few curves" must come from arithmetic, not from counting degrees of
freedom.

### 5.5 Lattice points near curves in the thin strip; exponent pairs

**Proposition 5.5 (PROVED, elementary).**
(a) *(Pick collinearity.)* Let L := ⌊c·U^{2/3}⌋, with c = c(c₂) > 0 small and U ≥ U₀. The E1 points (k, m) with k in
    any window [k₀, k₀ + L] are collinear.
(b) *(Per-line bound.)* A line with primitive direction (a, −b), a, b ≥ 1, contains at most 2√(2U/(ab)) + 2 points of E1.
    A line with a = 0 or b = 0 contains at most one. Along such a line s(t) = s₀ + σt − abt² and m(t) = m₀ − bt, so the
    tie becomes integral points on the quartic w² = s(t)² − 4m(t), of geometric genus ≤ 1.
*Proof.*
(a) Write g_j(k) := (p + 2jU)/k (j = 1, 2). E1 points with k ∈ [k₀, k₀+L] lie in {g₁(k) < m ≤ g₂(k)}; clip the window to
    the level range if necessary.
  * Each g_j is convex. So g₁ lies above its tangent t₁ at k₀, and g₂ lies below its chord c₂ over [k₀, k₀+L].
  * Hence the points lie in the convex trapezoid {t₁(k) < m ≤ c₂(k), k₀ ≤ k ≤ k₀+L}. Its vertical width is
    ≤ 2U/k₀ + (1/2 + 1/8)·max g_j″·L² ≤ 2U/k₀ + 1.4pL²/k₀³.
  * Since k₀ ≥ p/(4U²) and p ≥ U⁴/c₂⁴, the area is ≤ 16c₂⁴L/U + 90c₂⁸L³/U². This is < 1/2 for L ≤ cU^{2/3} with c small
    and U ≥ U₀.
  * A lattice triangle has area ≥ 1/2 (Pick), so no three non-collinear lattice points lie in the trapezoid.
(b) Along the line, s(t) is a concave quadratic with leading coefficient −ab.
  * {t ∈ ℝ : s(t) > 2U} is an interval of length 2√(Δ/(ab)), where Δ := max s − 2U. The set {s(t) > 4U} is a
    sub-interval of length 2√((Δ − 2U)₊/(ab)).
  * Since √x − √(x − y) ≤ √y, the set {2U < s(t) ≤ 4U} has total length ≤ 2√(2U/(ab)), so it contains
    ≤ 2√(2U/(ab)) + 2 integers.
  * A fixed k determines m, because the strip has vertical width 2U/k < 1 (k ≥ p/(4U²) > 4U). A fixed m determines k,
    because the horizontal width is 2U/m < 1. ∎
**EVIDENCE (§6.2, §6.4).**
* Lines with ≥ 3 points of E1 exist: "major arcs" at rational slopes b/a of small height, e.g. directions (5, −11),
  (2, −21), (7, −29). The longest have 5–18 points.
* They carry 2.9–6.9 % of E1 at primes with U = 1000 (4.0–9.7 % at odd squares and near-squares), and 2.5–3.4 % at
  U = 3162. The number of such lines rose from a mean of 37 to 70 between the two scales; two scales fix no growth law.
* No enrichment of tie events on these lines was detected (§6.4).
**Assessment (near-curve bounds).** Bounds for R(f, N, δ) = #{n ~ N : ‖f(n)‖ < δ} that depend only on derivative sizes
have a natural second-derivative term Nλ₂^{1/3} ≍ U^{4/3} for f = p/k, N ≍ U², δ ≍ 1/U and λ₂ ≍ U^{−2}. This exceeds
the divisor bound |E1| ≪ U^{1+ε}. The exact Huxley–Sargos statements were not retrieved (`LIT_CHECK.md` item 1,
UNVERIFIED), so this is not stated as a theorem.
**Deficit (Assessment).**
* Strip geometry yields collinearity only at scale U^{2/3} and per-line bounds ≪ (U/ab)^{1/2}.
* No bound on the number of rich lines, or on their total tie contribution, is proved here; a saving on the major arcs is
  not established.
* Points on no rich line carry no structure that a line covering can exploit.
* Exponent pairs and Bombieri–Iwaniec enter through Prop 4.3, where f″ = 2νp/k³ ≍ h ≥ 1; the B-process is self-dual
  for h ≍ 1.

## 6. Computations (scripts `scripts/z54_bilindiv_*`, data `data/z54/bilindiv/`, ≈ 40 kB)

Inputs come from `scripts/z54_bilindiv_inputs.py` (sympy nextprime; lists in §11).

### 6.1 TD falsifier (EVIDENCE; `z54_bilindiv_td.c`)
Columns: n, U, |E1|, |E1⁺|, N₂, N₄, max_h|T(h)|/√|E1⁺|, argmax, rms_h, and |T(1)|/√|E1⁺|. Data in `td_falsifier.txt`
and `td_extended.txt`.

| sample | U | H | \|E1\| / \|E1⁺\| | rms_h \|T\|/√\|E1⁺\| | max |
|---|---|---|---|---|---|
| 20 primes ≡ 1 (24) after 10¹² | 1000 | 20 | 2647–2888 / 1447–1639 | 0.83–1.26 | 2.60 |
| 10 odd squares near 10¹² (control) | 1000 | 20 | 2568–2895 / 1391–1653 | 0.92–1.16 | 2.55 |
| 10 near-squares m²+4 near 10¹² | 1000 | 20 | 2577–2906 / 1398–1652 | 0.80–1.16 | 2.32 |
| 14 FRONTIER §4 item-14 inputs† | 3–54 | 20 | 5–161 / 3–83 | 0.88–1.17 | 2.23 |
| 10 primes ≡ 1 (24) after 10¹⁴ | 3162 | 20 | 8478–8737 / 4747–4860 | 0.79–1.18 | 2.18 |
| 6 primes ≡ 1 (24) after 10¹⁶ | 10⁴ | 20 | 26862–27214 / 14915–15191 | 0.90–1.15 | 2.26 |
| first 3 of those, extended H | 10⁴ | 100 | — | 0.97–1.01 | 2.44 |
| 3 odd squares near 10¹⁶ | 10⁴ | 20 | 27451–27822 / 15334–15584 | 0.93–1.16 | 2.14 |
| 5 primes after 10¹² / 5 odd squares, extended H | 1000 | 32 | — | 0.88–1.21 / 0.94–1.12 | 2.52 / 2.41 |
| 3 primes ≡ 1 (24) after 10¹⁸, extended H | 31 622 | 178 | 89210–89298 / 49743–49763 | 1.02–1.05 | 3.19 |

† The ten listed (★)-failure primes 409, …, 8 813 281, plus the b = 1 / PM-II inputs 193, 2521, 66529, 3361. Lemma A's
condition p ≥ 16U³ holds only for the larger ones; for these inputs only the shape of T is tested.

* |T(h)| is of square-root size at every scale and for every control. Frequencies up to h ≈ U^{1/2} were tested only on
  the "extended" subsets.
* This is consistent with TD(η) for each η < 1/2. That would give N₂ ≪ U^{1/2+ε} (Corollary T).
* |E1|/U has sample means 2.79, 2.72, 2.71 and 2.82 at the prime samples 10¹², 10¹⁴, 10¹⁶ and 10¹⁸. Z53_HYP2CYCLE's
  model value for its unrestricted first filter is 4 log 2 ≈ 2.77.
* |E1⁺|/|E1| ≈ 0.55–0.58.
* Cross-check: N₂ from the strip form agrees with brute force at 300 consecutive primes > 10⁸
  (`z54_bilindiv_brute.py`): 0 mismatches, ΣN₂ = 113.

### 6.2 Geometry and anatomy filters (EVIDENCE; `z54_bilindiv_geom.c`, `geom.txt`)
Columns:
* n, U, |E1|;
* L3 = #lines with ≥ 3 points of E1, and Lmax;
* W = max # of points with k in a half-open window of length ⌊U^{2/3}⌋;
* P₁, A1 = the count in Prop 5.3(b), A2 = |dom f|, and the three divided by U;
* cov3 = # of points on lines with ≥ 3 points, and the direction of a longest line.

Results:
* **10¹², U = 1000, 20 primes.** L3 = 20–46, Lmax = 7–18, W = Lmax in 13/20 cases and W ≤ Lmax in all. The window
  ⌊U^{2/3}⌋ is larger than Prop 5.5(a)'s cU^{2/3}, so this is consistent with (a) but does not test it. cov3/|E1| =
  2.9–6.9 %. A2/U = P₁/U = 0.66–0.73 (equal by Prop 5.3(b)'s symmetry); A1/U = 0.33–0.37.
* **Odd squares and near-squares at 10¹².** Lmax = 5–14, cov3/|E1| = 4.0–9.7 %; the other columns are similar to the
  primes. n and n + 4 have almost the same strip, so the near-square control m² + 4 nearly duplicates the odd square m²
  here.
* **10¹⁴, U = 3162, 10 primes.** L3 = 60–79, Lmax = 6–7, cov3/|E1| = 2.5–3.4 %, A1/U ≈ 0.345.

### 6.3 Fixed-modulus relaxation of the AP form (EVIDENCE; `z54_bilindiv_untied.py`, `untied.txt`)
At p = 100000081 and 100000097 (U = 100, 7 500 levels):

| | p = 100000081 | p = 100000097 |
|---|---|---|
| N_rel(1) | 5253 = 0.53U² | 4792 = 0.48U² |
| N_rel(4) | 0.49U² | 0.45U² |
| N_rel(12) | 0.44U² | 0.40U² |
| N_rel(840) | 0.34U² | 0.31U² |
| N_rel(27720) | 0.30U² | 0.28U² |
| N₂ | 1 | 0 |

### 6.4 Are tie events enriched on the major arcs? (EVIDENCE; `z54_bilindiv_cyclines.c`, `cyclines.txt.gz`)
* *Statistic.* For every 2-cycle level k, r(k) := the largest number of E1 points on a line through (k, m_k).
* *Control.* For each prime *with N₂ > 0*, one control point of E1, chosen deterministically by index n mod |E1|.
  Controls and cycles weight primes differently (one control per such prime, N₂ cycles).

| sample | cycles: r ≥ 3 / r ≥ 4 | controls: r ≥ 3 / r ≥ 4 |
|---|---|---|
| 8 000 consecutive primes after 10¹⁰ (U = 316) | 2 921 cycles: 10.0 % / 5.5 % | 2 469 controls: 10.8 % / 6.4 % |
| 4 000 consecutive primes after 10¹² (U = 1000) | 1 437 cycles: 4.8 % / 2.6 % | 1 185 controls: 5.1 % / 3.0 % |

No enrichment of tie events on rich lines was detected in these samples. This does not establish equality in
distribution.

## 7. FRONTIER §4 hard screens (best idea: Theorem T / TD)
1. **T1 (odd squares).** Theorem T is an upper-bound inequality valid at every n (with N₂ as the product-divisibility
   count). It holds at odd squares, where N₂ can be positive (Z53_HYP2CYCLE Prop S), and it is silent on positivity by
   design. EVIDENCE: T(h) is of square-root size at the tested odd squares (§6.1). TD itself is hypothesised for primes
   only.
2. **8/131.** The argument uses only the strip structure km − n ∈ (2U, 4U] and a square test, so it transfers to other
   numerators. That is harmless for an upper bound.
3. **Tied modulus.** The tie is the square condition D_k = □ on the strip, and the modulus k enters only through the
   first-order remainder s_k = −p mod k. TD does not break the tie; it would bound the number of tie events from above.
4. **Fixed p.** Passed: everything is pointwise in p, with averages only over h, k and the strip.

## 8. Verdict

**Narrowed, with one new sufficient condition.**
* **New sufficient condition.** Theorem T (PROVED): N₂ ≤ 4δ|E1⁺| + 8δΣ_{h≤H}|T(h)| + negligible. Corollary T
  (CONDITIONAL on TD(η)): N₂ ≪ U^{1−η+ε}, so N(U, U) ≪ p^{(1−η)/4+ε}.
  * EVIDENCE: T(h) is of square-root size at 10¹²–10¹⁸, at primes, odd squares, near-squares and the test inputs. This
    is consistent with TD(η) for each η < 1/2, which would give N₂ ≪ U^{1/2+ε}.
  * TD is first order, but at the self-dual scale. Neither TD nor MIX is shown to imply the other.
* **Scoped closures, for the specified implementations:**
  * per-variable Fourier implementations for the smoothed top-W-range strip sum fall short by h^{1/2}U^{1/2} (Prop 4.3,
    PROVED);
  * the untied AP divisor asymptotic sits at the q = x^{2/3} endpoint (Prop 5.1(a), PROVED). The fixed-Q relaxation has
    model main term ≍ U² (Prop 5.1(b), Assessment; EVIDENCE §6.3);
  * short-interval divisor bounds control E1 but not the square condition (§5.2, Assessment);
  * one-sided anatomy filters retain ≫ U^{1−ε} (Prop 5.3, PROVED);
  * black-box HB15 with any occupancy pruning is dominated, box by box, by the elementary per-fibre count (Prop 5.4,
    PROVED relative to HB15 as restated);
  * strip geometry is collinear at scale U^{2/3} with per-line bounds (Prop 5.5, PROVED). Major arcs carry ≈ 3–10 % of
    E1, with no enrichment of tie events detected (EVIDENCE).
* **Survives:**
  * joint (ν, k) cancellation (Assessment: the additive analogue of SQSIEVE's bilinear (ℓ, C) estimate);
  * TD and MIX themselves;
  * the intermediate range U^{1−η} ≤ W = w_k ≪ U of TD (W ≤ U^{1−η} is free by Remark 4.1);
  * bounds on the number of rich lines;
  * counting the actual auxiliary curves;
  * Salberger and p-adic determinant variants;
  * AP methods with p-dependent moduli.

## 9. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1 under the z53 bullets:
> * **Balanced block, divisor/geometry angle (`Z54_BILINDIV.md`, z54; internal).**
>   * *Theorem T (PROVED):* let E1⁺ be the lattice points (k, m) of the strip p + 2U < km ≤ p + 4U with m ∈ (U², 4U²]
>     and D := (km−p)² − 4m ≥ 1 (|E1⁺| ≪ U^{1+ε}), and let w = √D. Then a power saving |Σ_{E1⁺} e(h w)| ≤ U^{1−η} for
>     h ≤ U^η (hypothesis TD) gives N(U,U) ≪ p^{(1−η)/4+ε} (CONDITIONAL on TD).
>   * TD is *first order*: one remainder phase per level, unlike MIX. EVIDENCE: square-root size at 10¹²–10¹⁸,
>     including odd squares.
>   * *Scoped closures for specified implementations:*
>     * per-variable Fourier implementations of the smoothed top-range strip sum fall short by h^{1/2}U^{1/2}
>       (Prop 4.3, the additive analogue of SQSIEVE B2);
>     * the untied AP divisor asymptotic sits at the Selberg–Hooley endpoint q ≍ x^{2/3}, and a fixed-Q relaxation of the
>       tie has model main term ≍ U² (Assessment);
>     * one-sided anatomy (H(x,y,z)) filters keep ≫ U^{1−ε} (Prop 5.3);
>     * black-box HB15 with any occupancy pruning is dominated box by box by "≤ 1 solution per u" (Prop 5.4);
>     * strip points are collinear at scale U^{2/3}; major arcs carry ≈ 3–10 % of the strip points, with no detected
>       enrichment of tie events (EVIDENCE).
>   * Missing: a joint (ν, k) cancellation, or TD/MIX themselves.
In §6 add: "balanced block via fixed-modulus divisor-in-AP / short-interval divisor / one-sided anatomy / black-box
determinant (pruned) → scoped statements, `Z54_BILINDIV` §5".

## 10. Bottom line
In its two most economical parametrisations (dom f and the strip set E1), the balanced block is a count of rare events,
with heuristic probability ≍ 1/U, among ≍ U candidates.
* Divisor and geometry tools control these candidate sets, but the specified implementations do not see the tie.
* AP tools impose it only through a fixed modulus, and even the untied asymptotic sits at the x^{2/3} endpoint.
* One-sided anatomy filters keep U^{1−ε} candidates.
* The black-box determinant method is dominated by "one solution per u".
* Strip geometry is collinear only at scale U^{2/3}; no enrichment of tie events on its major arcs was detected.

What survives is a first-order sufficient condition: square-root-sized sums of e(h√((km−p)² − 4m)) over the strip's
lattice points. TD(η) would give N₂ ≪ U^{1−η+ε}. The condition is numerically of square-root size at 10¹²–10¹⁸, but it
sits at the self-dual point, where the specified per-variable methods fall short by U^{1/2}. A joint (ν, k) cancellation
is the missing ingredient, mirroring the bilinear (ℓ, C) gap of the square sieve. Nothing here bears on positivity, and
ES remains open.

## 11. Reproduction
Every command uses `timeout ≤ 900` and `ulimit -v 4000000`; split the input lists if a run would take longer.
```
cd $REPO; D=data/z54/bilindiv; I=/tmp/z54in; mkdir -p $I
ulimit -v 4000000; timeout 900 uv run --with sympy python scripts/z54_bilindiv_inputs.py $I   # writes p8 p12 p14 p16 p18 sq12 ns12 sq16 test p10big p12big
gcc -O2 -o /tmp/z54td scripts/z54_bilindiv_td.c -lm; gcc -O2 -o /tmp/z54geom scripts/z54_bilindiv_geom.c -lm
gcc -O2 -o /tmp/z54cyc scripts/z54_bilindiv_cyclines.c -lm
for f in p12 sq12 ns12 test p14 p16 sq16; do timeout 900 /tmp/z54td 20 < $I/$f.txt; done     # td_falsifier.txt (~1 min)
head -5 $I/p12.txt | timeout 900 /tmp/z54td 32; head -3 $I/p16.txt | timeout 900 /tmp/z54td 100
timeout 900 /tmp/z54td 178 < $I/p18.txt                                                      # td_extended.txt (~15 s)
for f in p12 sq12 ns12 test p14; do timeout 900 /tmp/z54geom < $I/$f.txt; done               # geom.txt (~2 min)
timeout 900 uv run python scripts/z54_bilindiv_brute.py < $I/p8.txt                          # brute cross-check (~2 min)
timeout 900 uv run --with sympy python scripts/z54_bilindiv_untied.py 100000081 1 4 12 840 27720   # untied.txt
timeout 900 uv run --with sympy python scripts/z54_bilindiv_untied.py 100000097 1 4 12 840 27720
timeout 900 /tmp/z54cyc < $I/p10big.txt; timeout 900 /tmp/z54cyc < $I/p12big.txt             # cyclines (~10 s)
```

## 12. Review log
**Hostile review 1** (deep-mode subagent; `reviews/z54_bilindiv_review1.md`). Verdict **CORRECT WITH FIXES**.
* *Confirmed.* Theorem T, the core of Prop 4.3 (sign, W″, the λ constant 16.08, Parseval, the (hU³)^{−1/2} bound),
  Prop 5.3, and the inequalities of Props 5.4–5.5.
* *Reproduced.* TD rows, a geometry row, the brute cross-check (0 mismatches on 300 primes), both untied runs, and a
  cyclines sample.
* *Fixes applied (numbering as in the review).*
  1. The quadratic-order reading is replaced by the rank-two algebra A_k = ℤ[t]/(t² − st + m), with D = 0 separated.
  2. "Equivalent reading" corrected to the exact identity e(hw) = e(−2hu*), which covers even modes only.
  3. Curvature discussion restricted to the top range W ≍ U.
  4. Prop 4.3 scoped to the smoothed sub-sum T_φ. The reverse-order statement now names the triangle inequality over k.
  5. Condition (iii) stated as an assumption; low frequencies |ν| < hU handled separately; membership claimed only for
     direct exponent-pair bounds.
  6. Fouvry–Iwaniec quoted correctly (moduli rs, average); "q ≍ x^{2/3}".
  7. Prop 5.1(b) restricted to Q fixed independently of p and labelled Assessment. The lcm counterexample (full tie,
     ≪ U^{1+ε}) is recorded and universal claims are deleted.
  8. §5.2: the "necessity" and Ω arguments are deleted; Huxley's bound is used only as a direct-insertion statement.
  9. Prop 5.4 uses unordered Sol (example p = 100000037, k = 5176). HB radii versus side lengths are handled, giving
     constant 1/5; the weighted occupancy condition is stated.
  10. The major-arc saving claim and the U^{1/4} growth claim are deleted; line counts reported as data.
  11. The FRONTIER text uses E1⁺ and the proved bound |E1⁺| ≪ U^{1+ε}.
  12. §6.4 reports the conditioning and denominators: "no enrichment detected".
  13. The "every parametrisation" overclaim, the AP tie probability (≍ U^{−2}) and the model sizes are corrected.
  14. Lemma 3.1 hypotheses and sizes separated; the typo is fixed.
  15. Corollary T: η ≤ 1/2, U ≥ U₀, composite-n convention.
  16. Numbers corrected (|E1| ranges, means 2.79/2.72/2.71/2.82, Lmax 5–18, control 5.1 %, test-input description,
      N₂ = 1/0).
  17. The table's dom f entry is weakened to the proved lower bound.
  18. Labels made standalone and mixed entries split.
  19. "As it must be" deleted; input generator script added; timeouts ≤ 900; window documented; buffer guards added to
      the C scripts (outputs unchanged).
  20. Corollary T strengthened to U^{1−η+ε} (δ = U^{−η+ρ}).
* *Added after review.* Remark 4.1: the small-difference range is free, and TD has a smooth form.
