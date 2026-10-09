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
