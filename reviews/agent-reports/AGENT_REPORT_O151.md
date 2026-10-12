# AGENT_REPORT_O151 — brainstorm: analytic exotica (branch side-agent/bs-analytic-exotica)

Three memos in BRAINSTORM/, scripts `scripts/bs_anal_*.py`. All the counts come from `scripts/spec_typecount.c`
run to 4·10⁶ (about 35 s, outputs in /tmp, not committed). No memo is LIVE. ES is not solved.

**anal_dirichlet_series.md — (a) Dirichlet series of f_I, f_II and of the sterile indicator. COLLAPSES to B6/T7.**
The strongest reason is Prop A.2 (PROVED, elementary). Change f to 0 on a set of primes of convergence exponent 0.
This changes D_f only by a function holomorphic on Re s > 0. So nothing known or knowable about D_f on Re s > 0 can see
a sparse sterile set. Prop A.1 (PROVED) is an exact reformulation: ES for all large p ⟺ the sterile-prime series
P_E continues along the real axis to s = 0.
* No known result gives even abscissa σ_E < 1. That would be a power-saving exceptional set, which the
  LARGESIEVE 3/4 cap excludes for CRT methods.
* The non-linear inclusion–exclusion version collapses to the Bonferroni 3/4 ceiling.
* Fixed-p zeta-regularisation of the level sum collapses to H-E.

**anal_moments_structured.md — (b) moments, anti-concentration, structured exceptional sets. COLLAPSES (B3/B6, B1/B4, B2).**
* Prop B.1 (PROVED, elementary, essentially known). On the nine exponent-2 slices (4ad | 24), sterility is a
  subgroup condition on the prime factors of p + 4a²d.
* Remark B.2 records a tempting false lemma. If the subgroup condition held for all d it would give
  E(N) ≪ N exp(−(log N)^{1−ε}). It fails once (ℤ/4ad)^× has elements of order > 2; there is an explicit counterexample.
  The correct condition is a forced-class mixture, so the 3/4 cap applies.
* EVIDENCE on the shape of the fluctuations:
  * At accessible p, f(p) is not CLT-concentrated. var log(f/log³p) ≈ 0.95/log p, and the overdispersion against
    Poisson is 6–23×.
  * The non-local part dominates. About a quarter of it is explained by τ₃((p+e)/4) of the first Type II e-slices,
    with weights ≈ c/e. That is the shift-factorisation lottery (B2).
* Chebyshev on that variance gives only E(N) ≪ π(N)/log N.

**anal_euler_product_law.md — (c, own idea) f(p) as an L(1,χ_p)-type statistic. COLLAPSES to B1.**
The strongest reason: the local data are a CRT conditional mean (POINTWISE_SIZE Prop A).
* The law is real, which is new as far as the campaign files show (EVIDENCE). For p ≡ 1 (8),
  log(f/log³p) ≈ const − (A/log p)·log L_Y(1,χ_p).
  * The single-regressor R² is 0.54 for f_I and 0.31 for f_II.
  * A ≈ 6.2 (f_I) and 4.5 (f_II), stable over p ∈ [2·10⁴, 4·10⁶].
  * The per-q coefficients are ≈ −0.35/q for every q ≤ 61.
* Because β ∝ 1/log p, square-mimicking lowers the conditional mean by only a relative O(log log p/log p). Sterility
  risk is entirely non-local.
* The T1 analogy (ζ's pole for L(s,χ_{m²})) is spurious. The square zero is the global Jacobi identity
  (EXF Prop 2.1).
* Process note: a first pooled run suggested "saturation beyond q = 13". That was an artefact of mixing the classes
  mod 8, and I corrected it in the moments memo.

Items for the parent to check: the three regression tables (rerun takes < 3 min each), Prop A.2, Prop B.1 and the
B.2 counterexample.
