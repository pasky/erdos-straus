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
* **Cor 9.7 (cases (ii)–(iv))** — SOUND after repairs m5/m6. `D/A = N^{−δ}`; first term: (ii) `(A/E)^{1/2} ≪ N^{γ/2}
  ≤ N^{δ/4}` for `k ≥ 2j`, (iv) `(A/F)^{1/2} = N^{(β−1)/2} ≤ N^{δ/4}` for `k' ≤ k/2`, (iii) `λ ≪ 1/q`.
  `F' ≪ A√D` in all three cases (`E ≪ A`; `min(e,f) ≤ (ef)^{1/2} = (4a²d+1)^{1/2}`; `F < A`). Third term
  `≤ q^{5/4}(D/A)^{1/4}`, second `≤ q^{3/2}N^{ε₁/2}A^{−1/4}(D/A)^{1/4} ≤ q²(D/A)^{1/4}` since `A ≥ N^{1/3−2η₁}`.
  From-scratch exponent scan (`scripts/review_r118_checks.py` (e), 2·10⁵ random cells of 𝓡_bad(0.01) on `D<A`):
  `max(T1,T2,T3)+δ/4 ≤ 0` in every case, no `F' > A√D` violation; the (iii) third term is tight (equality at
  `F' = A√D`), so there is no spare margin there, but none is needed.
* **Thm 9.9 (i)–(iii) bookkeeping** — SOUND. `−16/64+3/64+2/64 = −11/64`; `11/64 > 1/6`; good layers;
  strip = non-good layers ⊂ {δ<w}, each costs `O(N𝓛 log 𝓛)` by (C:eq:BT-layer) (valid: `k ≤ 𝓛/3`), at most `w𝓛+1`
  layers; (i) `C_{ε₀/64}` fixed, threshold `N₀(ε₀)` only enters `O_{ε₀}`, and `C` is absolute (BT); (ii)
  `ε = 2A₀/log𝓛`, `log C_ε ≤ 𝓛^{1/2}`, `(11/64)δ𝓛 ≥ 22A₀𝓛/log𝓛`; strip `≪ A₀N𝓛²`; (iii) `9/64·δ𝓛 ≥ (C+2)log𝓛`
  for `δ ≥ 𝓛^{−1/2}`, threshold independent of G. The uses of (SEL) in Thm 8.1 are exactly those listed (step 3
  (ii) k≥2j, (iii), (iv) k'≤k/2, and the `|r_σ(1)|` comparison in step 4, which is the q=1 case of Cor 9.7). The
  residual-spectrum point (b) is a genuine standard fact, correctly flagged as cited-with-unverified-locator.
* **Assessment 9.11 / open problem "effective constants"** — honest labels. The claim that a loss
  `exp(o(log X/log log X))` suffices is correct: it yields `log C_ε ≤ exp(o(1/ε))`, hence `log G(64/w) = 𝓛^{o(1)}`
  at `w ≍ 1/log𝓛`. (Checked by hand.)

## C. Title, abstract, intro, consistency

* Title "an unconditional improvement" + abstract "without any hypothesis … All results are relative to cited
  inputs" — acceptable; the improvement is honestly described as unquantified. Theorem 2 is conditional and labelled
  so (abstract, intro, Thm 8.1, Thm 9.9(ii)). (EFF) is an Assessment, never a PROVED input. ES is nowhere claimed.
* The q₀-uniformity reading is flagged in §9 and in the status paragraph but not in the abstract, although the word
  "unconditional" rests on it (m8; repaired by one parenthesis in the abstract).
* §10, Prop 5.1 and the open problems are consistent with §9 (old "no unconditional improvement" removed;
  residual spectrum no longer attributed to (SEL)). No stale statement found by grep.
