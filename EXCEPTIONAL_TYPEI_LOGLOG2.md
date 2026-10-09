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
