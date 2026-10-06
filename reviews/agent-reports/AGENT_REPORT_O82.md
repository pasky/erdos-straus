# AGENT_REPORT_O82 — hypothesis SI for the class-of-one prefix (branch side-agent/sierpinski-si)

Deliverable: `POINTWISE_MN3.md` (closed as an obstruction/localisation write-up, parent decision (c)),
scripts `scripts/mn3_{u1,rn,resid,first}.py`. Summary table with labels: `POINTWISE_MN3.md` §0.

**Outcome: SI is NOT proved; ADM_m and the 1/4 exponent for W_5 remain CONDITIONAL.**

PROVED (under review by R82):
* Lemma 1.1: for `ν = δ_1`, `E^ν_1(q) ≤ 2ℓ·U_1(q)`, `U_1(q) = Σ_{C_q, D≤A} K^{ω(M)}/φ(M/gcd(M,mD+1))`.
* Lemma 2.1: N-parametrisation (`f | aN+c`, `cM = N(a+b)`, `acd ≤ N`), `R(N) < ∞`.
* Lemma 3.1: with three admissible levels, SI(δ_1) ⟸ (R_a) + `U_1(q) ≪ q^{−1/2−δ}` (square-root saving).
* Lemma 4.1: prefix part `s = gcd(g,Q_0)`, extra factor `1/φ(g/s)`.
* Lemma 5.1: `U_1(ℓ) ≥ R_ℓ(ℓ)/(ℓ−1)`; level-0 count on the all-ones path `Y(ℓ) ≤ 2R_ℓ(ℓ)`.
* Lemma 5.2: `R(N) ≪ N^{2/3+ε}`.

Assessment / EVIDENCE: all four linear (H)-routes are short on a residual (Kloosterman-range) region that
carries 72–91% of `U_1(q)` for `q ≤ 199`; its main term is the ES-type multiplicity `R(N)` at
`N = ℓ·(small)`.

CONJECTURE 5.3 (M2): `Σ_{N≤X} R(N)² ≪_ε X^{1+ε}`; data (m = 5) `Σ R²/(Y log⁶Y) = 0.0034 → 0.0026` for
`Y = 10³ … 3·10⁴`.

SKETCH (§5.4, not a proof): (M2) + (H) ⇒ SI via Cauchy–Schwarz over ℓ. Missing: (1) correlation terms of
`E^ν_2`; (2) the large-scale regime, incl. `q_0 < q < Q_0` where the prefix part is huge; (3) the
long-route (H) proofs; (4) the `ℓ | e` part and mixed splits; (5) first-moment totals uniformly in scale.

Waiting for R82's defects.
