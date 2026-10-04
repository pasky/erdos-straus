# Hostile review: EXCEPTIONAL_KARY.md (task O7), commit 666598b

Reviewer: side-agent/review-kary. Scope: Thm 2.5 (Lemmas 2.1–2.4, Cor 2.6),
§3 constants, Thm 4.1, Lemmas 4.2–4.3, Thm 4.5 (headline). Independent
brute-force code: `scripts/review_kary_bruteforce.py` (written from scratch,
not derived from `kary_check.py`), output `data/kary/review_bruteforce.txt`.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered D1, D2, …

## Items

### 1. Lemma 2.2 (locality) and the symmetrisation of Lemma 2.3 — SOUND

* On a frozen ω, `y^ρ_ℓ ∈ {c_ℓ, y_ℓ}` depends on `ρ_ℓ` alone (and only for
  ℓ ∈ R). Hence each `f_T(y^ρ_T)` is a function of `ρ_{T∩R}`, `|T∩R| ≤ d`,
  i.e. multilinear of degree ≤ d. No sign condition on the `f_T` is needed
  (majorant terms have real coefficients `a_i`; only `f = Σ f_T ≥ 0` is
  used, and `g_ω ≥ 0` pointwise because `y^ρ` is a point of `Ω_V`).
  Locality is in the right coordinates: replacement is coordinatewise, so
  T-dependence stays T-dependence. The worry "is f still d-local after
  replacement" does not arise: R is frozen and `ρ_ℓ` touches only `y^ρ_ℓ`.
* Symmetrisation: averaging `g∘π` over `Sym(R)` fixes `g(1_R)` (the
  all-ones corner is permutation-invariant) and the `Bern(t)^R` mean
  (exchangeable law); it preserves nonnegativity (average of nonnegative
  functions) and degree (`avg ρ^S = C(K,|S|)/C(n,|S|)`). The resulting
  `Q(K)` is ≥ 0 on `{0..n}` and has degree ≤ min(d, n) on that set.
* Lagrange step: `Q(n) = Σ_y ℓ_y(n)Q(y) ≤ Σ|ℓ_y(n)|Q(y) ≤ max(|ℓ_y(n)|/ψ(y))·Σ_{k}ψ(k)Q(k)`
  uses `Q ≥ 0` at all k (nodes and non-nodes). Direction is right: it upper
  bounds the corner value `f(y)` (σ side) by the bulk mean (thinned side).
  `B ≥ 1` always (`Σℓ_y(n) = 1`, `Σψ ≤ 1`), so `Φ ≥ 0` as Thm 4.1 needs.

### 2. Lemma 2.3 constant, (2.1), (3.1), §3 — SOUND

* Used at the right point and in the right direction: Thm 2.5 needs an
  upper bound on the corner `g(1_R) = f(y)` (σ-side value) by the
  `Bern(t)` bulk (thinned side, which Lemma 2.4 then dominates by ν). That
  is exactly what Lemma 2.3 gives. No lower bound on `E_σ f` is ever needed.
* Checked by hand: case (ii) (`C(n,i) ≥ n^i/(i!e^i)`, `(1−t)^n ≥ e^{−1.151nt}`
  for `t ≤ 1/4`), case (iii) (`|ℓ_i(n)| ≤ (2en/(dh))^d`, `h ≥ ½√(m₀/d)`
  ⇒ `≤ (4e√(n/(td)))^d`), and the passage to (3.1) in all three cases.
  The case-(ii) step `n^{d−i}/(d−i)! ≤ (2e)^d t^{−(d−i)}` uses `n ≤ 2d/t`; fine.
* Independent numerics (`scripts/review_kary_B_check.py`): for
  `n ≤ 14`, `t ∈ {.01,.03,.1,.2,.25}`, `d ≤ 4`: LP optimum `B* ≤` Lagrange-min
  B (ratio max 1.0, equality when n ≤ d), `max(log B − (2.1)) = −6.47`,
  `max(log B − (3.1)) = −8.95`. Random nonnegative degree-d multilinear g
  (literal products and squares), 3000 draws, `n ≤ 9`:
  `max g(1)/(B*·E g) = 1.0000000000000004` (tight, never exceeded).
* Cor 2.6's Jensen: `x ↦ log(a + √(bx))` and `x ↦ log(22tx+22)` are concave,
  `E n = E M` is exact (each light ℓ is replaced w.p. `p_ℓ` given the past).
  SOUND.

### 3. Lemma 2.4 (thinned law, supermartingale) — SOUND

* `P_ρ(y^ρ_ℓ = x_ℓ | ω) = (1−t)1{c_ℓ=x_ℓ} + t1{y_ℓ=x_ℓ} ≤ φ_ℓ` holds even
  without the disjointness remark. The filtration is `𝒢_ℓ = σ(c_i, y_i : i ≤ ℓ)`.
  `F_ℓ`, `p_ℓ`, "light", `D_ℓ` are `𝒢_{ℓ−1}`-measurable; `c_ℓ` and the
  fresh draw are independent of `𝒢_{ℓ−1}`. So
  `E[φ_ℓ | 𝒢_{ℓ−1}] = ν_ℓ(x_ℓ) + t·1{light}·p_ℓ·ν_ℓ(x_ℓ)1{x_ℓ∉F_ℓ}/(1−p_ℓ) ≤ ν_ℓ(x_ℓ)D_ℓ`.
* Reviewer's question (3), "is '`F_ℓ` known before ℓ' enough when activated
  sets depend on earlier *replaced* coordinates?": yes. The proof never
  needs the intermediate points `y^ρ` to be paths, nor R to be independent
  of anything; it needs only predictability of `F_ℓ` w.r.t. 𝒢, which holds
  for the plain rule (`F_ℓ = F_ℓ(h, y_{<ℓ})`), the phantom rule, and in fact
  for **any** rule `F_ℓ = F_ℓ(c_{<ℓ}, y_{<ℓ})`. The interpolation coins ρ
  are drawn after the whole path, so there is no feedback from ρ into R.
* t must be deterministic (not path-dependent) for `Π D_ℓ ≤ e^{(4/3)tM}`
  with the same t as in the corner bound. In §4, `t_j(h)` is a function of
  the block history only: fine. (Remark 2.7's path-dependent t is a separate
  argument; it is used only in the checks, not in §4. Not reviewed in detail.)
* Brute force: Lemma 2.4's inequality `max_x E[W P_ρ(y^ρ=x|ω)]/ν(x) ≤ 1`
  is asserted exactly (all paths, all ρ) in every run of item 6 below,
  including arbitrary full-state rules. No violation.
