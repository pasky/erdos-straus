# Hostile review R27 of EXCEPTIONAL_LARGESIEVE2.md (task O27)

Reviewer: side-agent/review-largesieve2. Reviewed: branch
`side-agent/ls-escapes` (checkpoint 1). From-scratch scripts:
`scripts/review_ls2_*.py`. Status: **in progress**.

## Verdict per claim

| claim | verdict |
|---|---|
| Lemma 1.1 (comparison measure) | SOUND (conditional on K2 Thm 5.1, as labelled) |

## Claim-by-claim notes

### Lemma 1.1

Re-derived. Primal: `min E_U ν` over the subspace `V_𝒟` (free
coordinates) subject to `ν(x) ≥ 1_𝒜(x)` for all `x ∈ ℤ/M'` (the `ν ≥ 0`
constraints on 𝒜 are implied, off 𝒜 they are the same family). Finite LP,
feasible (`ν ≡ 1`), bounded below by 0, so strong duality: there is
`μ ≥ 0` on `ℤ/M'` with `Σ_x μ(x)ν(x) = E_U ν` for all `ν ∈ V_𝒟` (equality
because ν is free in a subspace) and `μ(𝒜) = m*`. Signs are right. Since
`1 ∈ V_𝒟`, μ is itself a probability (not stated, harmless). π = μ|_𝒜/m* is
supported on `𝒜 mod M'` by construction; for `f ≥ 0` the dropped mass off 𝒜
only helps. No compactness issue (finite dimension). K2 Thm 5.1's
majorant class (`ν = Σ a_i 1[n≡b_i (d_i)] ≥ 0` on ℤ, `≥ 1` on 𝒜, each
`d_i` of W-rough level `≤ λ`, `λ ≥ λ₀`) contains every primal-feasible ν
(the d ∈ 𝒟 divide M', so "on ℤ/M'" = "on ℤ"), hence `m* ≥ e^{−S(λ)}`.
Remark (iii) / (1.2): checked; the lifted `F(n) = f((n−c)/Q₀)1[n≡c (Q₀)]`
needs `Q₀d | M'`, which holds as `Q₀d ∈ 𝒟`. Converse direction (Remark
(i)) correct.

Numerical check from scratch: see `scripts/review_ls2_lp.py` (pending).

### Theorem 4.3 (unconditional O(log log N) cap for Gallagher) — first pass

Chain re-derived; I find it SOUND (details and constant checks below).
* The law σ: base uniform on K2's `R_W^□` (K2 Lemma 2.3 is stated for
  every `W ≥ 3`; (R1) avoids all W-smooth classes of all four types,
  selectors included — proof is internal, uses K2 Lemmas 2.1–2.2 only),
  then plain sequential singletons with caps `δ_ℓ = ℓ^{−1/2}`. EK Lemma
  2.1(2) gives per-prime inflation `(1−δ_ℓ)^{−1} = γ'(ℓ)`, exactly K2's
  Γ, so K2's chain rule `σ(n≡b (m)) ≤ Γ(m)/m` holds and K2 Lemmas 4.1–4.3
  apply verbatim (their proofs use only the chain rule; checked).
* W-uniformity (the critical point, since W = (log 3Q)^8 grows): K2 Lemma
  4.3 states `C(W) ≤ C(log W)^c`. Checked against K2 Lemma 3.1's proof:
  primes `p ≤ W` contribute `≤ C(H,a)(log W)^{eH2^a}` — a polylog in W
  with an enormous but absolute exponent; Lemma 4.2's short-block
  pointwise bounds use `Γ(q) ≤ 8·3^{ω(q)}` (W-free); Shiu / K2 Lemma 3.5
  constants are W-free. So `𝔏 ≤ C(log W)^{c'}W^{−1/4}` and
  `𝔏·log Q ≤ C(8 log log 3Q)^{c'}(log 3Q)^{−2}log Q = O(1)`. OK.
* Leak: EK Lemma 2.1(1) + `E[p1{p>δ}] ≤ Ep²/δ` gives
  `Σ ℓ^{1/2}Ep_ℓ²`. OK.
* Conditioning: `π(b) ≤ σ(b)/(1−𝔏)` ⇒ `1+χ²(π) ≤ (1+χ²(σ))(1−𝔏)^{−2}`
  and `(1−x)^{−2} ≤ 1+4x` on `[0,1/4]` (checked numerically).
* Marginals: rough ℓ: convexity of χ² in the mixture over histories,
  `χ²(Unif(Ω∖F)) = p/(1−p)`; contraction under `ℤ/ℓ^E → ℤ/ℓ^v`; OK.
  W-smooth p: reduction of unit squares mod `p^e` onto unit squares mod
  `p^v` is a surjective group homomorphism ⇒ uniform; χ² = (p+1)/(p−1)
  (odd p), 1, 3, 7 for `2, 4, 2^v (v≥3)`. Checked from scratch.
* Sum: `Σ_{p≤W} log p/(p−1)·(2+12𝔏) = 2 log W + O(1)` (𝔏 log W = o(1)),
  so `≤ 3 log W + C = 24 log log 3Q + C`. OK (the "2" in front comes from
  χ² ≤ 2 for odd p; p = 2 bounded).
* Consequence via LS Thm 6.2's proof: `N/B ≤ 1 + NX/(ψ(Q)−log N)`; need
  `D* > log N`, `D_u ≤ log Q + c₀` ⇒ `Q ≥ Ne^{−c₀−X}`; for `Q ≤ N²`,
  `(log 3Q)^{24} ≤ 3^{24}(log N)^{24}` so `Q ≥ N(log N)^{−25}` for large N;
  `X ≤ 25 log log N`, saving `≤ 25 log log N + log log log N + C ≤ 26 log
  log N + C`. `Q > N²`: `4NX/Q ≤ 1`. OK.
