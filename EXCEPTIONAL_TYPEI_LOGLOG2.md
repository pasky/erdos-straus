# EXCEPTIONAL_TYPEI_LOGLOG2 — closing the exceptional-eigenvalue strip of (D)32 (task O116)

Status labels as in DISCOVERIES.md. TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` (Thm 8.1, CONDITIONAL on (SEL));
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288 (scan `sources/o111/deshouillers-iwaniec-1982.pdf`,
journal pages 219–288 = PDF pages 1–70; p. 232 = PDF p. 14). `L = log N`. Work in progress.

## 0. Summary (running)

* **Re-examination of TTL §3.2/§9.** TTL checked DI Thm 5 (one level) and DI Thm 6 (average over the level,
  general coefficients). It did **not** consider **DI Thm 7** (DI p. 233, (1.41)), the level-averaged
  exceptional large sieve for the **constant sequence** `a_n = 1`:
  `Σ_{q≤Q} Σ^{(q)}_{λ_j exc} X^{4iκ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪_ε (QN)^ε (Q + N + √(NX)) N`
  (DI's "Conjecture" `Q + N + √(NX)` in place of Thm 6's `Q + N + NX`, proved for `a_n = 1`).
  In TTL Prop 5.1 the unfolded coefficients are `b_n = λφ̂(λn)` — a smooth function of n, not a general
  sequence — so partial summation reduces them to `a_n = 1` (Lemma 1.2 below), and the levels `M = 4dq²` of
  TTL vary with `d ≍ D`, which is exactly an average over the level. §1–§2 show that at `q = 1` this
  removes the exceptional obstruction up to the `(QN)^ε` loss of DI Thm 7, with a power of N to spare
  in the `√(NX)` term.
* Remaining issues, treated below: (i) the `(QN)^ε` (Lemma 1.1 bookkeeping tolerates a loss
  `N^{O(1/log L)}`, i.e. a strip `δ ≤ C/log L` costs only `O(N L²)`; §3); (ii) the sieve moduli `q > 1`
  need the exceptional spectrum of `Γ₀(4dq²)` with **even nebentypus mod q** (TTL §5), which DI Thm 7 does not
  cover (§4).

## 1. The input from DI and the reduction to `a_n = 1`

**DI normalisation (DI (1.34), p. 230; as in TTL §5).** For `Γ₀(q)` (trivial character), `u_j` an orthonormal
basis of Maass cusp forms, `u_j(z) = √y Σ_{n≠0} ρ_{j∞}(n) K_{iκ_j}(2π|n|y) e(nx)`, `λ_j = 1/4 + κ_j²`;
exceptional means `λ_j < 1/4`, i.e. `iκ_j ∈ (0, 1/4]` real (DI Thm 4 gives `iκ_j ≤ 1/4`). Write
`σ_j := iκ_j` (= TTL's `σ_j`, `λ_j = 1/4 − σ_j²`).

**DI Theorem 7 (cited; DI p. 233, (1.41); read off the scan).** Let `Q, N, X ≥ 1`, `ε > 0`. Then
`Σ_{q≤Q} Σ_{j exc for Γ₀(q)} X^{4σ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪_ε (QN)^ε (Q + N + √(NX)) N`.

**Lemma 1.2 (partial summation; PROVED, elementary).** Let `c : [1,∞) → ℂ` be `C¹` with
`c(t) → 0` and `∫_1^∞ |c'(t)| dt < ∞`, and `S_j(t) := Σ_{n≤t} ρ_{j∞}(n)`. Then
`|Σ_{n≥1} c(n) ρ_{j∞}(n)|² ≤ (∫_1^∞|c'|)·∫_1^∞ |c'(t)| |S_j(t)|² dt`.
*Proof.* `Σ_{n≥1} c(n)ρ(n) = −∫_1^∞ S_j(t) c'(t) dt` (Abel summation; the boundary term vanishes as
`S_j(t) ≪_j t^{3/2}` and `c(t)`decays as in the application — Schwartz decay), then Cauchy–Schwarz with
the measure `|c'| dt`. ∎

**Drappeau's nebentypus version (cited; Drappeau, Proc. LMS 114 (2017), arXiv:1504.05549, §4.2.3, Lemma 4.10;
statement as extracted by a research subagent, `/tmp/o116_lit.md` — to be eyeballed against the PDF).** For a Dirichlet
character χ mod `q₀`, `Y ≥ 1`, `Q ≥ q₀`, and `a_n = 1_{N<n≤2N}`-type interval coefficients,
`Σ_{q≤Q, q₀|q} Σ_{f ∈ 𝓑(q,χ), t_f ∈ iℝ} Y^{2|t_f|} |Σ_{N<n≤2N} a_n n^{1/2}ρ_{f,∞}(n)|² ≪_ε (QN)^ε (Q/q₀ + N + (NY)^{1/2}) N`
(Drappeau's `n^{1/2}ρ_f(n)` is DI's `ρ_j(n)` up to an absolute constant; `Y^{2|t_f|} = (Y^{1/2})^{4σ_j}`, i.e.
DI's `X = Y^{1/2}`). For `q₀ = 1` this is DI Thm 7. Every summand is `≥ 0`, so the bound holds for any
subset of the levels `q ≤ Q, q₀ | q` — e.g. `{4dq² : d ≍ D}` when `q₀ | q`. A sharp interval `(N, N₁]`,
`N₁ ≤ 2N`, is the difference of two prefix sums, so (with `|x−y|² ≤ 2|x|²+2|y|²`) the same bound holds for
`S_j(t) := Σ_{n≤t} ρ_j(n)` with `N` replaced by `2t` (dyadic decomposition of `[1,t]` and Cauchy–Schwarz over the
`≪ log 2t` blocks: an extra factor `log² 2t`).

Notation for the rest: **(DI7_ε)** denotes the resulting bound, uniformly in `M₀, t, X ≥ 1` and in the
character modulus `q₀ | q`:
`Σ_{M ≤ M₀, q₀|M} Σ_{j exc} X^{4σ_j} |S_j(t)|² ≤ C_ε (M₀ t)^ε (log 2t)² (M₀ + t + √(tX)) t`.

## 2. The exceptional part of TTL Prop 5.1, averaged over d (PROVED rel. (DI7_ε))

Setting of TTL §5–§6: q squarefree, `(q,2d) = 1`, `M = 4dq²`, χ even mod q, `ψ(u) = φ(x/λ)W(y/Y)`,
`Y ≤ λ𝓛^{−3}`, `P_χ = Σ_{Γ_∞\Γ₀(M)} χ̄(γ)ψ∘γ`, `B_j(s) = Σ_{n≠0} ρ̄_j(n) b_n(s)`, `b_n(s) = λφ̂(λn)|n|^{−s}`.

**Lemma 2.1 (exceptional coefficients on a shifted line; PROVED).** Let `u_j` be an exceptional cusp form of
`(Γ₀(M), χ)`, `t_j = iσ_j`, `0 < σ_j ≤ 1/4`. With `s_v := σ_j + 1/𝓛 + iv`,
`|⟨P_χ, u_j⟩|² ≪ 𝓛⁴ Y^{−1−2σ_j} ∫_ℝ |𝒲(s_v)| |B_j(s_v)|² dv`.
*Proof.* TTL Prop 5.1 Step 2 holds on any line `Re s > |Re(it_j)| = σ_j` (the Mellin formula for `K_{it}`
needs `Re s > |Im t|`). Take `Re s = σ_j + 1/𝓛`. There `G_{t_j}(s) = Γ((s−σ_j)/2)Γ((s+σ_j)/2)` has arguments of
real part `1/(2𝓛)` and `σ_j + 1/(2𝓛) ≥ 1/(2𝓛)`, `≤ 1`, so by TTL Step 3 (Stirling / `|Γ(w)| ≪ 1/|w|` near 0)
`|G_{t_j}(s_v)| ≪ 𝓛² e^{−π|v|/2}`; and `|(πY)^{−s_v}| ≤ Y^{−σ_j}·Y^{−1/𝓛} ≤ e·Y^{−σ_j}` (`1/Y ≤ e^𝓛`). Cauchy–Schwarz in v
with the measure `|G𝒲| dv` as in TTL Step 4. ∎
(No contour shift is made, so the `1/σ_j` singularities of `Γ(±σ_j)` never appear; for `σ_j ≤ 1/𝓛` the factor
`Y^{−2σ_j} ≤ e²` and Lemma 2.1 is TTL Step 4 verbatim.)
