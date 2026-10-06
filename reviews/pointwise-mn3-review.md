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

**Lemma 3.1.** Re-derived. With L levels, "no bad step ⇒ Λ(ℓ) ≤ (1−θ)^{−L}" is immediate (Lemma 1.3).
(b): a ≥ 1, ℓ (or 2) fibre lifts, Markov + MN2's supermartingale first moment (Ψ_0 = 1 for δ_1, Ψ ≤ K^{ω(M^-)}
while alive) + Lemma 1.1 give `P(bad) ≤ E^ν_1(q)/(θℓ) ≤ 2U_1(q)/θ` (the stated `4U_1/θ` is a safe overestimate);
all (b) q are distinct proper prime powers `> q_0`, and `#{proper pp ∈ (x,2x]} ≪ x^{1/2}/log x` gives
`Σ ≪ q_0^{−δ}`. (c), ℓ > q_0: `k ≥ 4`, `Σ_ℓ ℓ·ℓ^{−k(1/2+δ)}` summable. (c), ℓ ≤ q_0: `q ≥ ℓ^{a_ℓ+4} > q_0ℓ³`
(as `ℓ^{a_ℓ} > q_0/ℓ`), so the term is `≤ q_0^{−1/2}ℓ^{−1/2}` up to a geometric factor, total `≪ 1/log q_0`.
I checked that L = 3 is really needed: with L = 2, (c) at `q = ℓ³`, ℓ > q_0, would need `Σ_ℓ ℓ^{−1/2−3δ}` — divergent.
So the lemma is correct, but it proves the **three-level analogue** of SI (call it SI_3), not MN2's SI
(two levels, K = (1−θ)^{−2}) — see defect 4.

**Lemma 4.1.** The inequality is right (`M/s = N·(g/s)`, super-multiplicativity). Two statements are not:
see defects 5, 6. Brute force (`review_mn3_lemma11.py`): on every positive-weight atom `s = gcd(g,Q_0)` and
weight `≤ ℓ/(φ(N)φ(g/s))`; but on 2568 of 4125 atoms (m = 5, q_0 = 8) the weight is 0 and `s ≠ gcd(g,Q_0)`.

**Lemma 5.1.** Re-derived; trivial first clause, second clause correct (M_1 | L(ℓ) fully revealed and ℓ ∤ M_1,
so `M_1 | g`, `N ∈ {1, ℓ}`; `N = 1` never occurs — also confirmed on 1.5·10⁶ atoms). From-scratch
`review_mn3_first.py 5 11 … 31`: `Y(ℓ) = 4, 6, 7, 13, 12, 25, 6`, all with `N = ℓ`, `Y ≤ 2R_ℓ(ℓ)`
(strict only when the fixed point D = A occurs), forbidden fractions 0.200–0.455 — matches the author's 0.20–0.46.

**Lemma 5.2.** Re-derived; correct (pairwise products of a, c, d multiply to `(acd)² ≤ N²`; each case a divisor
count of a quantity `≤ N^{O(1)}`). But it is not the best this device gives — see defect 1 (MAJOR): the
author's coordinates are *exactly* Elsholtz–Tao's Type I sextuples and ET's 3/5 argument goes through verbatim.
