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
