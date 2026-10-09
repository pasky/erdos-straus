# Review B of EXCEPTIONAL_TYPEI_LOGLOG2.md (R116, second independent reviewer, hostile)

Reviewed: `EXCEPTIONAL_TYPEI_LOGLOG2.md` (branch `side-agent/ttl-unconditional`, merged into this worktree),
claims as listed in `reviews/agent-reports/AGENT_REPORT_O116.md`. Written before reading review A.
From-scratch scripts: `scripts/review_ttl2b_*.py`.

## 0. Sources actually read (quoted)

**DI 1982, p. 233 (scan PDF p. 15, rendered at 300 dpi and read by me).**
> Conjecture. Theorem 6 holds with the factor `Q + N + √N X` in place of `Q + N + NX`. [...] We succeeded to
> prove our conjecture for `a_n = 1`, more precisely we have
> **Theorem 7.** Let `Q, N, X ≥ 1` and ε be any positive constant. We then have
> (1.41) `Σ_{q≤Q} Σ^{(q)}_{λ_j-except} X^{4iκ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪ (QN)^ε (Q + N + √N X) N`,
> the constant implied in ≪ depending on ε alone.

The radical in (1.41) and in the Conjecture covers **N only** (checked at 300 dpi): the bracket is `Q + N + X√N`,
as the document says. `Σ^{(q)}` = exceptional eigenvalues of `Γ₀(q)` (p. 233 top, defined under Thm 6, trivial
character). The q-sum is over **all** levels `q ≤ Q`. Thm 6 (p. 232, (1.39)) has the same q-sum, weight `X^{4iκ_j}`,
general `a_n` on `N < n ≤ 2N` and bracket `Q + N + NX`.

**Drappeau, arXiv:1504.05549, §4.2.3 (pdftotext of `sources/o116/drappeau-1504.05549.pdf`, pp. 15–16).**
Setting (§4.1, p. 10): `Γ = Γ₀(q)`, "χ a character modulo `q₀ | q`", multiplier `χ([[a,b],[c,d]]) = χ(d)`,
weight `κ ∈ {0,1}`, `χ(−1) = (−1)^κ`; `𝓑(q,χ)` an orthonormal basis of Maass cusp forms, expansion with
`ρ_{f𝔞}(n) W_{n/|n|·κ/2, it_f}(4π|n|y)`.
`E_{q,𝔞}(Y,(a_n)) := Σ_{f∈𝓑(q,χ), t_f∈iℝ} Y^{2|t_f|} |Σ_{N<n≤2N} a_n n^{1/2} ρ_{f𝔞}(n)|²`.
> **Lemma 4.9.** [...] Recall that χ has modulus `q₀ ≥ 1`. Then for all `Y ≥ 1` and `Q ≥ q₀`,
> `Σ_{q≤Q, q₀|q} E_{q,∞}(Y,(a_n)) ≪_ε (QN)^ε (Q q₀^{−1} + N + N Y^{1/2}) ‖a_N‖₂²`,
> where the scaling matrices are chosen independently of q.
> **Lemma 4.10.** Assume that the situation is as in Lemma 4.9. Assume moreover that `(a_n)_{N<n≤2N}` is the
> characteristic sequence of an interval of integers. Then
> `Σ_{q≤Q, q₀|q} E_{q,∞}(Y,(a_n)) ≪_ε (QN)^ε (Q q₀^{−1} + N + (NY)^{1/2}) N`.

Also p. 19 (Remark after the proofs): the bounds hold with `Y^{2θ}N^{2θ}Q^{1−4θ}` in place of `(NY)^{1/2}` for
Lemma 4.10 (θ the spectral-gap exponent); with θ = 1/4 this is the stated bound — a consistency check.
Normalisation: for κ = 0, `W_{0,it}(4π|n|y) = 2|n|^{1/2} y^{1/2} K_{it}(2π|n|y)`, so DI's `ρ_j(n) = 2 n^{1/2} ρ_f(n)`
and Drappeau's `Y` is DI's `X²` (weight `Y^{2σ} = X^{4σ}`, `(NY)^{1/2} = X√N`). **The document's transcription of
both statements (§1) is correct.** The "(statement as extracted by a research subagent … to be eyeballed)" caveat
in §1 is stale: the statement matches the PDF (MINOR, see defects).

**DI pp. 276–278 (proof of Thm 7, read by me at 130 dpi).** (8.17): `S(Q,Y,N,0) ≪ (QN)^{5ε}(Q+N+√(NY))N` "for
characteristic sequences `a_n` of intervals `[N,N₁]`, `N ≤ N₁ ≤ 2N`". Then the Thm 14 step gives
`≪ (NY)^ε(Q+N+Y)N`, the rectification (8.18), the induction (8.19) with threshold `Q₀(ε)`, and the conclusion.
No hypothesis beyond `Q,N,X ≥ 1` appears. **The claimed misprint below (8.18) is real:** with `Y₁ = Q+N`,
`√(Y/Y₁)(Q+N+Y₁) ≍ √(QY)+√(NY)` as printed; with `Y₁ = √(Q+N)` one would get `√Y(Q+N)^{3/4}`.
(Immaterial for the theorem.)

## 1. Verdicts per claim

| Claim | Verdict |
|---|---|
| §1 transcription of DI Thm 7 / Drappeau L4.10, normalisation `Y = X²` | SOUND |
| (DI7_ε) prefix-sum form (dyadic blocks + Cauchy–Schwarz) | SOUND (the `log²` is even generous: one `log` suffices) |
| Lemma 1.2 (partial summation) | SOUND |
| Lemma 2.1 (exceptional coefficient on the line `σ_j + 1/𝓛`) | SOUND |
| Prop 2.2 (d-averaged exceptional variance) | SOUND (minor presentational defects D3, D4) |

**From-scratch checks** (`scripts/review_ttl2b_mellin_abel.py`, mpmath, < 1 min): (1) the Mellin formula for
`K_σ` with real `σ ∈ (0,1/4]` on the line `σ + 1/𝓛`: rel. err `5·10⁻³⁰`; (2) `sup_v |G(s_v)|e^{π|v|/2}/𝓛² ≤ 3.9`
over `σ ∈ [10⁻⁴, 1/4]`, `𝓛 ∈ [3, 1000]` (uniform, as Lemma 2.1 needs); (3) `|(πtY_d)^{−s}| ≤ e² w(t)^{σ}`:
0 violations in 20000 random `(Y₀, 𝓛 ≥ log(1/Y₀), Y_d ∈ [Y₀/√2, Y₀], σ, t)`; (4) the Abel identity of Lemma 1.2
(rel. err `2·10⁻¹⁷`) and its Cauchy–Schwarz inequality, random `ρ(n) ~ √n`.

**Re-derivation of Prop 2.2 (the heart of the document).** I re-did the proof independently:
* Uniformity over the exceptional spectrum (brief item 1). After Lemma 2.1 the only j-dependence of the bound for
  `|B̃_j(s_v)|²` is the factor `w(t)^{2σ_j}` inside `∫Φ(t)w(t)^{2σ_j}|S_j(t)|²dt`; `|s_v| ≤ 2+|v|` uses only
  `σ_j ≤ 1/4` (Selberg, valid for nebentypus forms since they live on `Γ₁(M)`), and `𝒲` is replaced by a
  σ-uniform majorant. So for each fixed `t` the j-sum is *exactly* the left side of DI (1.41) / Drappeau L4.10
  with `X = w(t)^{1/2} ≥ 1`. Since (1.41) is uniform in `X`, applying it for each `t` separately and then
  integrating in `t` is legitimate. **The partial-summation reduction to `a_n = 1` is uniform over the spectrum.**
* Levels (brief item 2). q is fixed throughout Prop 2.2/Thm 3.1; the levels `M = 4dq²`, `d ≍ D`, `(q,2d)=1`,
  are distinct, `≤ M₀ = 8Dq²`, and divisible by `q₀ = q` (χ mod q, possibly imprimitive — Drappeau allows any χ
  mod q₀). Every summand of L4.10 is ≥ 0, so restricting to this subset is legitimate. The price is the `Q`-term
  `M₀/q₀ ≤ M₀` instead of `#levels ≍ D`; the document pays the even cruder `M₀` (extra `q²` absorbed later).
  The χ-average `(2/φ(q))Σ_χ` is ≤ max over χ, and each χ is a fixed multiplier — correct order of quantifiers
  (Drappeau's sum is for one fixed χ over many levels; that is what is used).
* Cusp/scaling. Drappeau needs the cusp ∞ with q-independent scaling matrix; TTL's cusp ∞ has width 1 and
  identity scaling for every level `4dq²`. Weight 0 because χ is even. OK.
* Arithmetic: `∫Φ ≪ 𝓛λ₋` (needs `log(1/λ) ≤ 𝓛`, true since `Y ≤ 1`), `∫Φ t^{1+a+ε}log²(2t) ≪ 𝓛²λ₋^{−a−ε}`,
  `√(t w(t)) = max(√t, (πY₀)^{−1/2})`, and the three resulting terms `λ₋M₀`, `1`, `λ₋Y₀^{−1/2}` (times `Y₀^{−1}`)
  all re-derived. `M₀^ελ₋^{−ε} ≤ (M₀/(λ₋Y₀))^{2ε}` holds as `Y₀ ≤ 1 ≤ M₀/λ₋`.

| Claim | Verdict |
|---|---|
| Thm 3.1 (d-averaged per-d count, no SEL) | SOUND |
| Cor 3.2 ((b2),(b3),(b5), relative remainder `q²N^{−δ/4}`, all δ > 0) | SOUND |
| Thm 4.1(i) `≤ Cε₀NL²log L + O_{ε₀}(NL²)`, hence `o(N log²N log log N)` | SOUND (relative to the cited inputs) |
| Thm 4.1(ii) `≪ N log²N` under (EFF) | SOUND as a conditional statement; (EFF) itself is an unproved Assessment |
| Thm 4.1(iii) | SOUND (minor: "inf" may not be attained, take `w` slightly above `w_N`) |
| §6 "TTL missed DI Thm 7" | SOUND (TTL §3.2/§9 mention only Thm 5, Thm 6, Humphries) |

**Thm 3.1 / Cor 3.2 re-derivation.** From TTL Thm 6.2's last line, Cauchy–Schwarz over d and Lemma 6.3:
`Σ_d|E_d| ≪ 𝓛^C q D^{3/4}(Σ_dV_d^{gen} + Σ_d𝓔_d)^{1/2}`. I recomputed `Σ_d V_d^{gen}` from TTL Prop 5.1
(`Σ_{d≍D} q^{1/2}M^{−1}Y_d^{−1} ≍ q^{−1/2}F'√D = q^{−3/2}·(qF'√D)`; matches `N^{ε₁}q^{−3/2}/Y₀`) and the regular
spectrum is indeed SEL-free: Steps 4–7 of TTL Prop 5.1 only need real `t_j` for the Mellin line `σ₀ = 1/𝓛 > |Im t_j|`,
and the large sieve (DI Thm 2 / Drappeau (4.24), weight `1/cosh(πt_f)`, which is `cos(πσ) ≥ cos(π/4)` on the
exceptional part) majorises the sub-sum over real `t_j` by positivity. The three relative-error terms of Thm 3.1
follow with `λ/Y₀ = 2A√D`.
`scripts/review_ttl2b_exponents.py` (from scratch, 390k random exponent points in `R_bad`, `η = η₁ = ε₁ = 0.01`,
`q = N^θ`, `θ ≤ δ/64`): starting from the **unsimplified** five-term bracket, the relative-error exponent minus the
claimed `2θ − δ/4` is `≤ −2·10⁻⁵` in each of (b2), (b3), (b5) (equality approached only at the case boundaries, as
the proof says); the unsimplified and the three-term form of Thm 3.1 agree (max difference 0); and
`log_N(M₀/(λ₋Y₀)) ≤ 3 − 1.25`, so the side condition of Thm 3.1 holds with a wide margin.
(The parenthetical "q ≤ N^{1/100}" is consistent with `Q = N^{δ/64}` because `δ ≤ 1/3 + 4η₁` on R_bad, TTL (b1).)

**Thm 4.1 bookkeeping (brief item 3).** Re-derived: `Σ_{q≤Q}3^{ω(q)}q² ≪ Q³(log Q)²`, `Q = N^{δ/64}`;
`N^{4ε} = N^{w/32} ≤ N^{δ/32}`; total `N^{−δ/4+3δ/64+2δ/64} = N^{−11δ/64}` ✓. Bad layers: a layer `k = ⌊δL⌋` meets
O(1) a-blocks per c-block j (α = (δ+1−γ)/2), (b4) costs `≪ NL/j` per (j, a-block) and `≪ NL` for `c ≍ 1`, so
`≪ NL log L` per layer with an **absolute** constant; `δ < w ≤ 1/4` gives `A, D ≥ N^{1/4}` (`D = N^{1−α−γ} >
N^{3/8−γ/2}`), so (b4)/Lemma 8.4(a2) apply. In (i) the constant `C` is absolute and only the threshold
`N₀(ε₀)` depends on ε₀ (via `C_{ε₀/128}`), so `o(·)` follows by choosing ε₀ after ε'. In (ii),
`exp(A₀/ε) = exp(128A₀/w_N) = L^{1/2}` ✓, and `(11/64)·256A₀L/log L = 44A₀L/log L` ✓. Note `w_N ≤ 1/4` needs
`log L ≥ 1024A₀`, so (ii) is a purely asymptotic statement (from-scratch log-space scan in
`scripts/review_ttl2b_bookkeeping.py`: for `A₀ = 0.01` the good-layer inequality holds for all `δ ≥ w_N` only from
`L ≈ 3·10⁴`; harmless, but worth one sentence). A toy layer-cost model in the same script shows the expected
shapes: cost/L² ≈ const for `w = 2/log L`, grows like `ε₀ log L` for fixed `ε₀`, and like `log L` for `w = 1` (ET).
