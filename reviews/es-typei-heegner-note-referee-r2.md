# Referee report R118 — O118 revision of `paper/es-typei-heegner-note.tex`

Hostile internal referee (R118). Scope: new Theorem 1 (unconditional `o(N log²N log log N)`), new §9
("The exceptional spectrum on average over the level"), Theorem 2 under (SEL) or (EFF), title/abstract,
consistency. Compared against `EXCEPTIONAL_TYPEI_LOGLOG2.md`, `reviews/exceptional-typei-loglog2-review{,-B}.md`.
Internal review only; not external refereeing.

## A. Cited inputs (checked against sources)

* **DI Theorem 7** (`sources/o111/deshouillers-iwaniec-1982.pdf`, scan p. 233 = PDF p. 15): the paper's quote of
  (1.41) and of the Σ^{(q)} sentence is **verbatim correct** (`Q,N,X ≥ 1`, sum `n ≤ N`, `X^{4iκ_j}`,
  `(QN)^ε(Q+N+√N X)N`, "constant implied in ≪ depending on ε alone"). 
* **DI (8.18) misprint** (scan p. 277): confirmed. With `Y₁=√(Q+N)` the printed second line does not follow;
  with `Y₁=Q+N`, `(1+√(Y/Y₁))(Q+N+Y₁) ≍ Q+N+√(NY)+√(QY)`, which is the printed third line. SOUND.
* **Drappeau Lemma 4.10** (`sources/o116/drappeau-1504.05549.pdf`, arXiv p. 16): **verbatim correct**, as are
  the Lemma 4.9 setting (`q₀ ≥ 1`, `Y ≥ 1`, `Q ≥ q₀`, scaling matrices independent of q), the `N ≥ 1/2` of
  Prop. 4.7, and the definition of `E_{q,a}` in §4.2.3. His p. 19 remark ("q₀ appears only with negative powers in
  the error terms") is reproduced fairly. The q₀-uniformity of `≪_ε` is **flagged as our reading** both in §9
  and in the intro status paragraph. Adequate. (Drappeau also requires `χ(−1)=(−1)^κ`; for even χ, κ=0 — fine.)

## B. §9 lemma-by-lemma (re-derived by hand)

* **Cor 9.1 (prefix sums)** — SOUND. Dyadic pieces `(2^{i−1},min(2^i,t)] ⊂ (N_i,2N_i]` are intervals, Lemma 4.10
  allows any interval inside `(N,2N]`, `Q=M₀ ≥ q₀`, positivity handles subsets of levels. Minor: the number of
  pieces is `⌈log₂t⌉+1 ≤ 2+log₂t`, not `≤ 1+log₂t` (e.g. t=3 gives 3 pieces) — harmless (defect m1).
* **Lemma 9.2 (partial summation)** — SOUND. `Σ_{n≤T}c(n)a_n = S(T)c(T) − ∫_1^T S c'`, `S(1⁻)=0`; Cauchy–Schwarz
  with `Ψ dt` is exactly as stated.
* **Lemma 9.3 (shifted line)** — SOUND after a cosmetic fix. Mellin of `K_ν` valid for `Re s > |Re ν| = σ_j`;
  `G_{t_j}(s)=Γ((s−σ_j)/2)Γ((s+σ_j)/2)` (since `it_j = −σ_j`); both real parts in `[1/(2𝓛), 1/2]` for `𝓛 ≥ 2`,
  `|Γ(x+iy)| ≤ Γ(x) ≪ 1/x`. Defect m2: `Re s_v = σ_j+1/𝓛` can be up to `1/4+1/2 = 3/4`, outside the strip
  `0 ≤ σ ≤ 1/2` over which `𝒲*` is defined. Repair: define `𝒲*` as sup over `0 ≤ σ ≤ 1` (𝒲 entire, rapidly
  decreasing on strips, so nothing else changes). Applied (R118 repair).
* **Prop 9.4 (averaged exceptional variance)** — SOUND (modulo m2). Checked: `|(πtY_d)^{−s_v}| ≤ e²w(t)^{σ_j}`
  in both regimes (`πtY_d ≥ 1`: ≤ 1; else `(√2)^{σ_j}·w^{σ_j}·(√2/(πY₀))^{1/𝓛} ≤ 2^{1/8}e < e²`, using
  `𝓛 ≥ log(1/Y₀)`); `|s_v| ≤ 2+|v|`; reflection `z ↦ −z̄` conjugates by `diag(−1,1)`, keeps `γ₂₂`, hence χ, and maps
  an ON basis of each exceptional eigenspace to one (the Σ_j is basis-free) — so the `n<0` part is identical;
  `(DI7_ε)` applied per `t` with `Y=w(t) ≥ 1`, levels `4dq² ≤ M₀`, `q | 4dq²`; `√(t·w) ≤ √t + Y₀^{−1/2}`, `√t ≤ t`.
  Integrals: `∫Φ ≪ 𝓛λ₋` (the `λ|φ̂(λt)|/t` part gives `λ log(2/λ)`, and `𝓛 ≥ log(2+1/λ)` because `Y₀ ≤ 1`);
  `∫Φ t^{1+a+ε}log²(2t) ≪ 𝓛²λ₋^{−a−ε}` after `u=λt`. Assembling: `M₀`-term → `λ₋M₀`, `t`-term (a=1) → `1`,
  `Y₀^{−1/2}`-term → `λ₋Y₀^{−1/2}`, overall `𝓛^7 C_ε (M₀/λ₋)^ε Y₀^{−1}[…]`. Matches the statement.
* **Remark 9.5** — SOUND: constant weight `Y=Y₀^{−1}` gives the `a=1/2` integral, i.e. `λ₋^{1/2}Y₀^{−3/2}`.
* **(9.1) / Thm 9.6 (averaged per-d count)** — SOUND (arithmetic re-derived). `Y_d ∈ [Y₀/√2,Y₀)`, `λ/Y₀ ≍ A√D`;
  `Σ_d V^gen ≪ 𝓛^C[DA√D(1+λ) + N^{ε₁}q^{−3/2}Y₀^{−1}]` using `M ≥ 4Dq²` and `λ^{−ε₁} ≪ N^{ε₁}`
  (`λ ≥ 1/(3q√D)`); Prop 9.4 with `M₀/λ₋ ≤ N³`; the three terms after `·qD^{3/4}/(AD)` are exactly
  `q²(D/A)^{1/2}(1+λ)^{1/2}`, `q^{3/2}F'^{1/2}/A` (the gen-part analogue `q^{3/4}N^{ε₁/2}F'^{1/2}/A` is smaller, so the
  stated combined form is a valid over-estimate), `q^{5/4}F'^{1/4}D^{1/8}/A^{1/2}`. The second box of
  `(1−Δ)ψ` carries the d-dependent scalar `(Y_d/λ)² ≤ 1`, which only decreases `𝓔^{(2)}`; fine but unstated (m4).
  `(1+λ_j)² ≤ 25/16` on the exceptional part, also fine.
