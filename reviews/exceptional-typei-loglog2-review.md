# Hostile review R116 of EXCEPTIONAL_TYPEI_LOGLOG2.md (O116, branch side-agent/ttl-unconditional)

Reviewer: side-agent/review-ttl2. Scope: all claims of `reviews/agent-reports/AGENT_REPORT_O116.md`.
From-scratch scripts: `scripts/review_ttl2_*.py`. Status: round 1 IN PROGRESS.

## A. The cited inputs, read against the sources

**DI Thm 7 (scan p. 233 = PDF p. 15, read at 300 dpi by me).** Verbatim:
> Theorem 7. Let Q, N, X ≥ 1 and ε be any positive constant. We then have
> (1.41) Σ_{q≤Q} Σ^{(q)}_{λ_j-except} X^{4iκ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪ (QN)^ε (Q + N + √N X) N,
> the constant implied in ≪ depending on ε alone.

(The radical covers only N. It is preceded by the Conjecture "Theorem 6 holds with the factor Q+N+√N X
in place of Q+N+NX" and by "We succeeded to prove our conjecture for a_n = 1".) Trivial character,
group Γ₀(q), cusp ∞, **all** levels q ≤ Q, prefix interval n ≤ N. O116 §1 quotes this correctly; with
`Y = X²` the bracket is `Q + N + √(NY)` and the weight `Y^{2σ_j}`, consistent with DI (8.17)–(8.19) on
pp. 276–278 (I read pp. 277–278: (8.18) `S ≪ (1+√(Y/Y₁))(Q+N+Y₁)N(NY₁)^ε`, then
`≪ (QN)^ε(Q+N+√(NY)+√(QY))N`; this needs `Y₁ ≍ Q+N`, so O116's "misprint" remark is right in
substance: with `Y₁ = √(Q+N)` the displayed line does not follow). DI's proof of (8.19) itself uses
partial summation against `n^{it}` to reduce varying coefficients to interval sums — the same device as
O116 Lemma 1.2, which supports its legitimacy.

**Drappeau Lemma 4.10 (arXiv:1504.05549, p. 16; pdftotext, checked by me).** Setting §4.1: Γ₀(q), χ a
character modulo `q₀ | q`, `κ ∈ {0,1}` with `χ(−1) = (−1)^κ`; `B(q,χ)` an orthonormal (Petersson,
unnormalised) basis of Maass cusp forms; Fourier expansion at a cusp with Whittaker `W_{0,it_f}(4π|n|y)`
(for κ = 0); `E_{q,a}(Y,(a_n)) := Σ_{f∈B(q,χ), t_f∈iℝ} Y^{2|t_f|} |Σ_{N<n≤2N} a_n n^{1/2} ρ_{fa}(n)|²`.
> Lemma 4.9. ... Recall that χ has modulus q₀ ≥ 1. Then for all Y ≥ 1 and Q ≥ q₀,
> Σ_{q≤Q, q₀|q} E_{q,∞}(Y,(a_n)) ≪_ε (QN)^ε (Q q₀^{−1} + N + N Y^{1/2}) ‖a_N‖², where the scaling matrices are
> chosen independently of q.
> Lemma 4.10. Assume that the situation is as in Lemma 4.9. Assume moreover that (a_n)_{N<n≤2N} is the
> characteristic sequence of an interval of integers. Then
> Σ_{q≤Q, q₀|q} E_{q,∞}(Y,(a_n)) ≪_ε (QN)^ε (Q q₀^{−1} + N + (NY)^{1/2}) N.

O116 §1's quote is correct (its text still says "as extracted by a research subagent … to be eyeballed";
it now has been — see MINOR m2). Normalisation: `W_{0,it}(4π|n|y) = 2|n|^{1/2} y^{1/2} K_{it}(2π|n|y)`, so
DI's `ρ_j(n) = 2 n^{1/2} ρ_f(n)`; `Y^{2|t_f|} = Y^{2σ_j}`. For χ even κ = 0. Drappeau's proof is a sketch
("the induction arguments in [DI82b, pages 274, 277] are easily reproduced"; (4.30) is proved in a page).
His own §4.3 applies Lemma 4.10 with q₀ varying, and remarks that the bounds "decrease with q₀"; so the
implied constant is meant to depend on ε only (uniform in q₀ and χ). Accepted, but it is a cited sketch.

**Hypotheses used by O116 and whether they hold.**
* `Y ≥ 1`: O116 uses `Y = w(t) = max(1, 1/(πtY₀)) ≥ 1`. ✓
* `Q ≥ q₀`: `Q = M₀ = 8Dq² ≥ q`. ✓
* levels divisible by q₀ = q, same χ for all levels: levels `4dq²`, χ mod q fixed while d varies. ✓
* cusp ∞ with scaling matrix independent of the level: identity (TTL uses cusp ∞, width 1). ✓
* subset of levels: every summand is ≥ 0, so restricting to `{4dq² : d ≍ D, (d,q)=1}` is legitimate. ✓
* interval coefficients: `S_j(t) = Σ_{n≤t}` is split into ≤ log₂(2t)+1 dyadic pieces, each an interval inside
  some `(N,2N]`; Cauchy–Schwarz over pieces. Costs one log (O116 books log², harmless). ✓

**Verdict A — SOUND.** The citations are applied within their hypotheses. Drappeau's Lemma 4.10 is a
published (Proc. LMS) lemma whose proof is sketched by transposition from DI; the result is in the same
evidential class as Drappeau Prop 4.7, which TTL already relies on.

## B. Verdicts on §1–§3

**V1. Lemma 1.2 (partial summation) — SOUND.** Abel: `Σ_{n<T} c(n)ρ(n) = c(T)S(T) − ∫_1^T S c'`; the boundary
term vanishes (`S_j ≪_j t^{3/2}`, c Schwartz); then Cauchy–Schwarz with `|c'|dt`. From scratch
(`scripts/review_ttl2_analytic.py` (a)): with the actual `c(t) = λφ̂(λt)(πtY)^{−s}`, complex `s = σ+1/𝓛+iv`
and random `ρ(n)` of size `n^{1/2}`, the ratio LHS/RHS is ≤ 0.91 in 40 trials.

**V2. Lemma 2.1 (shifted line) — SOUND.** Re-derived TTL's Mellin formula
`K_ν(x) = (8πi)^{−1}∫ Γ((s+ν)/2)Γ((s−ν)/2)(x/2)^{−s}ds`, `Re s > |Re ν|`, and
`I_t(n) = Y^{−1/2}(8πi)^{−1}∫G_t(s)𝒲(s)(π|n|Y)^{−s}ds`; for `ν = σ_j` the line `σ_j + 1/𝓛` is admissible and no
contour shift is made. Gamma bound checked numerically ((c): `|G|/(𝓛²e^{−π|v|/2}) ≤ 4.0` over
`𝓛 ∈ {5,…,1000}`, `σ_j ∈ [10⁻⁶, 1/4]`, `|v| ≤ 60`).

**V3. Prop 2.2 (averaged exceptional variance) — SOUND.** Checked line by line:
* The coefficient depends on j only through `s_v = σ_j + 1/𝓛 + iv`, and the j-dependence is fully absorbed into
  (i) the j-free majorant `Φ(t)` and `𝒲*(v)` and (ii) the factor `w(t)^{2σ_j}`, which is exactly DI/Drappeau's
  weight `Y^{2|t_f|}` with `Y = w(t)` depending on t only. So for each fixed t one may sum over all levels, χ and
  exceptional j and apply Lemma 4.10 (Tonelli: all terms ≥ 0). **This is the crux and it is legitimate: the
  reduction to `a_n = 1` is uniform over the exceptional spectrum.**
* `|(πtY_d)^{−s}| ≤ e² w(t)^{σ_j}` incl. the case `πtY_d ≤ 1 < πtY₀`; `|s| ≤ 2+|v|`. Numerically (b): max ratio
  `|c'|/(e²(2+|v|)Φw^σ) = 0.33` over 2000 random parameter sets.
* `√(t w(t)) ≤ √t + (πY₀)^{−1/2}`; `∫Φ ≪ 𝓛λ₋`, `λ₋^a∫Φt^{1+a} ≪ 1` (numerically (d): bounded by 3 for
  `λ ∈ [10⁻⁴, 10]`, a ∈ {0, ½, 1}); the `√t` piece gives `a = ½`, absorbed since `λ₋ ≤ 1`.
* χ-average: `(2/φ(q))·#{even χ} = 1`. The reflected `n<0` part is again a basis for an even character mod q.
* Levels `4dq² ≤ M₀`, all divisible by q (= q₀). ✓
The final bound `𝓛^C C_ε (M₀/(λ₋Y₀))^{2ε} Y₀^{−1}[λ₋M₀ + 1 + λ₋Y₀^{−1/2}]` is correct.

**V4. Thm 3.1 — SOUND (one inaccurate side remark, m3).** Re-derived: `Σ_d|E_d| ≤ q(Σ#Λ_d)^{1/2}(ΣV_d)^{1/2}`
with `ΣV_d^{gen} ≪ D(λ/Y₀)(1+λ) + N^{ε₁}q^{−3/2}/Y₀` (TTL Prop 5.1 without (SEL): exceptional forms removed by
positivity — note `cosh(πt_f) = cos(π|t_f|) ≥ cos(π/4) > 0` for them, so they are positive terms of DI Thm 2
/ Drappeau Prop 4.7 and dropping them is legitimate), and Prop 2.2. Dividing by AD reproduces the three
relative terms exactly (`λ/Y₀ = 2A√D`). `M₀/(λ₋Y₀) ≤ N³` holds in all cases (grid: 0 failures).

**V5. Cor 3.2 — SOUND.** `scripts/review_ttl2_exponents.py` recomputes the relative error from the *raw* Prop 2.2 +
TTL bounds (not from the author's three terms) on 3.9·10⁵ random points of the (b2)/(b3)/(b5) regions with
`q ≤ N^{δ/64}`, `ε ≤ δ/128`: 0 violations of `rel ≤ q²N^{−δ/4+3ε}` (the only "violations", ≤ 2.5·10⁻⁴ in
exponent, come from my deliberately including the `a/2 ≤ b < a` cells at exponent scale, i.e. a factor
≤ 2 in `A/e`, an O(1) constant). The author's 3-term form dominates the raw expression everywhere.
`F' ≤ 3A√D` in (b3) holds since `min(e,f) ≤ (ef)^{1/2}` and `ef = 4a²d+1`. No upper bound on δ is needed.
