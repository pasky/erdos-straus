# AGENT_REPORT_O82 — hypothesis SI for the class-of-one prefix (branch side-agent/sierpinski-si)

Deliverable: `POINTWISE_MN3.md`, scripts `scripts/mn3_{u1,rn,resid,first}.py`. Checkpoint 1.

**Outcome: SI is NOT proved.** A precise localisation of the difficulty instead.

PROVED:
* Lemma 1.1: for `ν = δ_1`, the ν-weights of completed restrictions are bounded by class-of-one
  weights, `E^ν_1(q) ≤ 2ℓ·U_1(q)`, `U_1(q) = Σ_{C_q, D≤A} K^{ω(M)}/φ(M/gcd(M,mD+1))`.
* Lemma 3.1: with three admissible levels (`K = (1−θ)^{−3}`) SI needs only `U_1(q) ≪ q^{−1/2−δ}`
  (proper prime powers) plus the level-0 pair sums — a square-root, not full, saving.
* Lemmas 2.1, 4.1, 5.1, 5.2: N-parametrisation (`f | aN+c`, `cM = N(a+b)`), prefix part
  `s = gcd(g,Q_0)` with extra factor `1/φ(g/s)`, `U_1(ℓ) ≥ R_ℓ(ℓ)/(ℓ−1)`, `R(N) ≪ N^{2/3+ε}`.

Assessment (§4, §5): every linear route (sum over c, d, a, or N with (H)) is short on a "residual"
region (Kloosterman range of the hyperbola `ef ≡ 1 mod ma²`), and EVIDENCE shows the residual carries
72–91% of `U_1(q)` for `q ≤ 199`. Its main term is the Erdős–Straus-type multiplicity
`R(N) = #{atoms with M/gcd(M,mD+1) = N}` at `N = ℓ·(small)`. SI at level 0 needs one of: a pointwise
bound `R(N) ≪ N^{θ}` with `θ ≈ 1/10` (best known analogue for ES counts: ET's `3/5`; here 2/3),
equidistribution of R along `N ≡ 0 (mod ℓ)` at level `X^{1−δ}`, or (via Cauchy–Schwarz over ℓ) the
congruence-free second moment `(M2) Σ_{N≤X} R(N)² ≪ X^{1+o(1)}` — CONJECTURE, data to `3·10⁴`
fit `≈ 0.003 X(log X)⁶`.

Not done / caveats: the "long-route" regimes are only tabulated (Assessment), not written as proofs;
the implication (M2) ⇒ SI is sketched, not proved (correlation terms of `E^ν_2` and the large-scale
regime missing). No overclaim intended: ADM_m and the 1/4 exponent for `W_5` remain CONDITIONAL.

Decision requested from parent: (a) continue towards "SI ⟸ (M2) + (H)" as a written conditional
theorem (several more days: long-route proofs, correlations, large scale), or (b) attack (M2) itself
(a 6-variable ES-type pair count), or (c) stop here with the obstruction write-up.
