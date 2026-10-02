# Hostile review: EXCEPTIONAL_THETA.md (branch side-agent/theta-beyond-34)

Reviewer: side-agent review-theta-2 (restart of the interrupted first review).
Subject files imported verbatim from `side-agent/theta-beyond-34`:
EXCEPTIONAL_THETA.md, AGENT_REPORT_A2.md, scripts/theta_*.py, data/theta/.
Literature assessment reused from the first reviewer: `reviews/theta-lit-notes.md`
(verdict: apparently new; no prior source found).

Status: IN PROGRESS (items are committed one at a time).

## Item 1 — Theorem 2.5 (with Lemmas 2.1–2.3, Proposition 2.4)

**Verdict: SOUND** (presentation repairs T1–T4 only; none load-bearing).

### 1.1 Direction of the inequality

The goal is a *lower* bound on `min{Eν : ν ≥ 0 on ℤ, ν ≥ 1 on 𝒜, level ≤ λ}`.
The proof is primal: for an arbitrary feasible ν it exhibits
`1 ≤ ν_c(0) ≤ (bounded constant)·E ν_c`. The interpolation functional
`Q ↦ Σ_j c_j (⊗_g I_{j_g} Q)(0)` with Lagrange weights is exactly a
dual-feasible certificate: it reproduces Q(0) on the whole span and is
dominated by `B·(probability measure)` on the support. So the direction is
right. No minimax or strong-duality step is used, so no duality-gap issue
can arise.

### 1.2 Line-by-line check

* **Lemma 2.1.** MacWilliams–Sloane Ch. 10 Lemma 7 gives
  `C(z,y) ≥ (8y(1−y/z))^{−1/2} e^{zH(y/z)}`. Combined with `D ≤ χ²` and
  `1/(1−q) ≤ 4/3`, this gives the stated bound. Checked.
* **Lemma 2.2.**
  * (2.1) uses `P ≥ 0` on Y only. Correct.
  * (a): `⌈μ'⌉ ≤ z−1` needs z ≥ 3, which holds because μ' ≥ 1 and q ≤ 1/4
    force z ≥ 4 (unstated, T4).
  * (b): exact.
  * (c): I re-derived the node bounds.
    * `W+k+1 ≤ √(kμ')` uses `k ≤ √(kμ')/4` (from k ≤ μ'/16) and
      `2 ≤ √(kμ')/4` (from kμ' ≥ 64).
    * Nodes lie in `[μ'/2, 2μ'] ⊆ [1, z−1]`, using `2qz ≤ z/2`.
    * `|ℓ_i(0)| ≤ (2μ')^k 2^k (e/k)^k (k/μ')^{k/2} = (4e√(μ'/k))^k`.
    * `16e^{2+8/3} ≈ 1703 ≤ C₁ = 16e⁶`.
  * (2.2): the Legendre step `max_k[(k/2)log(C₁μ'/k) − αks] = (C₁μ'/2e)e^{−2αs}`
    is exact, and `C₁/(2e) = 8e⁵ = C₄`. The three fallback cases are correct.
    In particular `1.151·16 = 18.4 ≤ 19`, and `C₄e^{−2} ≫ 1.151`.
* **Lemma 2.3.**
  * The telescoping `Σ_{j∈Λ}⊗Δ_{j_g}` reproduces every `x^a` with `a ∈ Λ`.
    Nestedness of nodes is not needed, because `Δ_k` kills degree < k
    exactly.
  * `|c_j| ≤ 2^G`.
  * Checked numerically with random non-nested nodes (Part C below).
* **Proposition 2.4.**
  * *Step 0.* Correct: a term containing a coordinate with `s_i > λ` would
    violate the level.
  * *Step 2 (thinning).* `x = u∘w` has the right law. `f_w(u) = f(u∘w)` is
    nonnegative, λ-level, and has `f_w(0) = f(0) ≥ 1`, because the map
    `u ↦ u∘w` sends 0 to 0.
  * *Step 3 (symmetrisation).*
    * Averaging over `Π Sym(Z_g)` preserves nonnegativity, the value at 0,
      and the mean, since the law of u is exchangeable inside each band
      (common `q_g`; this is why thinning is done first).
    * It produces a polynomial in the counts. The multidegree of `u^S`,
      `S ⊆ T`, satisfies `Σ_g j_g s_g ≤ Σ_{i∈S} s_i ≤ λ`, because
      `s_i ≥ s_g` on `B_g`.
    * Reduction modulo `Π_{i=0}^{z_g}(K_g−i)` lowers only the g-th degree,
      so the support stays in the lower set and lands in Λ'.
    * Q ≥ 0 at *every* grid point, since every count vector is realised by
      some u.

    So the level, nonnegativity and the normalisation at 0 are all
    preserved, as the task asked to verify.
  * *Step 4.* `|(⊗I)Q(0)| ≤ Π_g B_g(j_g) · Σ_{y∈grid_j} Π_g ψ_g(y_g) Q(y)
    ≤ Π_g B_g(j_g) · E Q(K)`. The second inequality uses Q ≥ 0 on the
    whole support. The product structure of the Lagrange weights makes the
    one-dimensional constants multiply. Correct.
  * *Step 5.* `Σ_g 19α j_g s_g ≤ 19αλ`.
    * `|Λ| ≤ Π_g(1+λ/s_g) ≤ (1+λ/s_*)^G`.
    * Jensen: `E f = E_w E_u f_w ≥ E_w e^{−Φ(w)} ≥ e^{−E_wΦ(w)}`.
    * `E_w q_g z_g = μ_g`, and concavity handles the log term.
    * `e^{−2αs_g} ≤ e^{−αs_i}` on `B_g`, since `s_i < 2s_g`.

    All correct.
* **Theorem 2.5 (CRT form).**
  * Given c, the coordinates `n mod ℓ^{E_ℓ}` (ℓ∈𝒫), the finer digits of
    the Q₀-primary part, and the free primes are independent (CRT). Since
    `x_ℓ` is a function of `n mod ℓ` only, conditioning on `(c,x)` keeps
    the product structure.
  * Each class indicator therefore conditions to a product of functions of
    `x_ℓ`, ℓ ∈ T_i. That is λ-level with weights `log ℓ`. Prime powers and
    free primes are harmless.
  * `ν_c(0) ≥ 1` needs `P(x=0|c) > 0`, i.e. `|F_ℓ(c)| < ℓ` for *all* ℓ,
    including invisible ℓ > e^λ. This is correctly listed as a hypothesis.
    Without it the statement is false: a fibre with no avoiders lets ν
    vanish there.
  * Jensen over c is fine: Φ_c is affine in `(p_ℓ(c))_ℓ` apart from the
    concave log term.
* **Uniformity in |𝒫|.** (2.4) depends on 𝒫 only through the truncated
  profile `Σ_{ℓ≤e^λ} p̄_ℓ ℓ^{−α}`, through `log μ̄`, and through
  `s_* = log min 𝒫`. Primes above e^λ enter only via `p_ℓ < 1`. The bound is
  uniform in |𝒫|, as claimed.

### 1.3 Independent exact-LP tests (`scripts/review_theta_lp.py`, own code)

* **Part A (CRT level).**
  * *Setup.* An exact LP over `ℤ/Q_tot` for ν in the span of all class
    indicators of slice-level ≤ λ. The small part is free.
    Configurations: Q₀ ∈ {2,3,4,6}, slice primes {5,7,11,13(,17)}, a
    prime-power coordinate 5², and a free non-slice prime 3. F_ℓ(c) is
    random with `|F_ℓ(c)| ≤ ℓ/4`, and λ ranges over log 5 … log 1001.
  * *Prediction.* The proof of Thm 2.5 shows `W_CRT ≥ (1/Q₀)Σ_{c∈R} W_bool(c)`.
    Lifting the Boolean fibre optima shows `≤`. So **equality** is the
    sharp prediction.
  * *Result.* Equality holds in every instance to 10⁻⁷
    (`data/theta/review_lp_partA.txt`). The conditioning step is therefore
    lossless, including the prime-power digits and the free primes.
  * *Theorem's bound.* (2.4), optimised over α, is always satisfied. It is
    extremely slack at these sizes: −log bound ≈ 130–430 against true
    savings ≈ 0.8–1.5, because of the additive `75G` and `C₄ = 8e⁵`. The
    theorem is asymptotic, so this is expected.
* **Part B (Proposition 2.4 chain).** 51 random multi-band weighted
  instances (n ≤ 7, p ≤ 1/4, up to 3 bands). Every inequality of the chain
  holds (`data/theta/review_lp_partB.txt`):

      W_bool ≥ E_w W_multi ≥ E_w[1/Σ_j|c_j|Π_g B_g(j_g)] ≥ e^{−E_w log Σ…} ≥ e^{−RHS(2.3)}

  * `W_multi` is the exact LP over P_{Λ'} on the count grid.
  * `B_g` is the exact `B(Y)` of the Lemma 2.2 node recipes.
  * Minimum gaps: `−2·10⁻¹⁶` and `−3·10⁻¹⁶` (rounding), then `0`, then
    `0.05`.
  * Thinning/symmetrisation loses at most 0.24 nats here. Lagrange
    interpolation loses up to ≈2 nats at these toy sizes.
* **Part C.**
  * The Lemma 2.3 identity holds to 10⁻¹¹ on 200 random lower sets with
    random non-nested nodes.
  * Lemma 2.2 (c) and (2.2) show 0 violations on 12 570 grid cases, with
    z up to 2000, q up to 1/4, k up to min(z,60), and boundary values
    `k = ⌊μ'/16⌋, ⌊μ'/16⌋+1`. The worst margin in (2.2) is 74.4 nats, i.e.
    the additive 74 is never needed in these cases.

### 1.4 Defects (item 1)

* **T1 (minor; summary table, §0, row "Thm 2.5", and the phrase
  "−O(log²λ)").**
  * *Problem.* The explicit error in (2.4) is
    `G(75+log(2+λ/s_*)) + (G/2)log(16μ̄+16)`. This is O(log²λ) only when
    `s_* ≫ 1` and `log μ̄ ≪ log λ`. In general μ̄ can be as large as
    `π(e^λ)/4`, which makes the term ≍ λ log λ. The 1.15 nats of
    `(16μ')^{1/2}` per band are genuine slack of the Lagrange method. Even
    a degree-0 band loses `½ log μ'`.
  * *Impact.* Harmless in every application, where `μ̄_λ ≪ λ³`.
  * *Fix.* Say "O(log²λ) provided μ̄ ≤ λ^{O(1)}", or keep the explicit
    form.
* **T2 (minor; Thm 2.5 statement, "Here μ̄ may be read as the truncated
  mass").** The truncated reading is the one that is proved: Step 0
  discards s_i > λ before μ is formed. Make it the definition rather than
  an aside. As stated, μ̄ is the untruncated mass, which can be infinite
  for infinite families, while the proof only needs the truncated one.
* **T3 (cosmetic; Prop 2.4 Step 5).** Write out the Jensen chain
  `E f = E_w E_u f_w ≥ E_w e^{−Φ(w)} ≥ e^{−E_wΦ(w)}`. The phrase "Jensen
  for exp and for log" is cryptic.
* **T4 (cosmetic; Lemma 2.2(a)).** Record that μ' ≥ 1 and q ≤ 1/4 give
  z ≥ 4. Otherwise `⌈μ'⌉ ≤ z−1` looks unjustified.

The literature status is unchanged from `reviews/theta-lit-notes.md`:
apparently new. My spot checks found nothing contrary. The mechanism
(Christoffel/Lagrange extremal mass, combination technique) is classical.
The weighted lower-set CRT statement is not in the sources consulted.
