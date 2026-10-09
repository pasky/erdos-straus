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

