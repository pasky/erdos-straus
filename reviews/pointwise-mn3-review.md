# Review R82 of POINTWISE_MN3.md (task O82, branch side-agent/sierpinski-si)

Reviewer: hostile side agent `side-agent/review-mn3`. Read: POINTWISE_MN3.md, POINTWISE_MN2.md (§§1–3, 5),
POINTWISE_MN.md Cor 6.1(0), POINTWISE_OMEGA12.md Lemma 2.1, AGENT_REPORT_O82.md.
From-scratch scripts: `scripts/review_mn3_*.py`.

(in progress)

## Verdicts per claim

| claim | verdict |
|---|---|
| Lemma 1.1 (`E_ν[p_0(E^-)] = 1[s|P]φ(s)/φ(M^-) ≤ ℓ/φ(N)`, `E^ν_1 ≤ 2ℓU_1`) | SOUND (re-derived; brute force exact, 0 defects) |
| Lemma 2.1 (N-parametrisation, `R(N) < ∞`) | SOUND (re-derived; brute force on 1.5·10⁶ atoms) |
| Lemma 3.1 (three levels; SI ⟸ (R_a)+(R_b)) | (pending) |
| Lemma 4.1 (prefix part) | (pending) |
| Lemma 5.1 | (pending) |
| Lemma 5.2 (`R(N) ≪ N^{2/3+ε}`) | (pending) |
| §2/§4/§5 EVIDENCE | (pending) |
| §4–§5 Assessments, (M2) | (pending) |

## Re-derivations and from-scratch checks

**Lemma 1.1.** Re-derived: `v_ℓ(Q_0) = a_ℓ ≤ a` (stage-A steps have `ℓ^{a+1} > q_0`) gives `s = gcd(M,Q_0)`;
CRT on units mod `lcm(M^-,Q_0)` with `r ≡ 1 (Q_0)` gives `1[−mD ≡ 1 (s)]φ(s)/φ(M^-)` (this needs `−mD` a unit
mod `M^-`: true since `gcd(D,M) | gcd(A²,mA−1) = 1`, `gcd(m,M) = 1`); `φ(M) = φ(M^-)·(ℓ or ℓ−1)`,
super-multiplicativity of φ. Factor 2 via `mD(mA²/D+1) ≡ mD+1 (mod M)`. Weight `K^{ω(M^-)} ≤ K^{ω(M)}` (K ≥ 1).
`scripts/review_mn3_lemma11.py` enumerates `r mod lcm(Q_0,M^-)` exactly: m = 5, q_0 = 8 (`Q_0 = 168`),
`q ≤ 32`, `M ≤ 2·10⁵`: 4125 atoms, exact probability = formula and ≤ `ℓ/φ(N)` and ≤ `ℓ/(φ(N)φ(g/s))` in every
case; same for m = 7, q_0 = 12 (6566 atoms) and m = 6, q_0 = 9 (2682 atoms).

**Lemma 2.1.** Re-derived all four identities (`fb = cP − af = aN + c`; `cM = ceN = (a+b)N`;
`u(aN+c) ≡ N² + mc²d (mod f)` with `ua = f+N`); `N ≥ (m/2)acd − 1 ≥ acd` from `eN ≥ ef − 2`.
`scripts/review_mn3_atoms.py 5 300000 15`: all 1 513 036 atoms with `D ≤ A`, `M ≤ 3·10⁵` satisfy every
identity, `N ≥ acd`, `f ≤ (m−1)N`, involution invariance of g, and `N ≠ 1`. `R(N)` for `N ≤ 15` from the raw
atom list (complete, since `M = eN ≤ N(mN³+1)`) equals the validated (a,c,d)-count. Note the unvalidated
(a,c,d)-count of the Lemma's displayed bound is ≈ 1.8× R(N) (e.g. Σ_{N≤10³}: 19674 vs 11158) — fine, it is
stated as an upper bound.
