# POINTWISE_MORDELL17B — the r = 17 tail: union measure, exact level 6, explicit hypotheses (task O93)

Status: O93 (branch `side-agent/r17-explicit-tail`), work in progress, not reviewed.
Builds on POINTWISE_MORDELL17.md (= "M17"; reviewed R83 rounds 1–2). Notation and labels as there.
`N = 17^K`, K odd; P-data at level K = N-points `(a,b,c,d)` of `Σ^II_N` with `a ≤ b`, `17∤cd`
(equivalently `(a,s,t) = (a,c,d)` with `f = 4ast−1 | s·N + a`, `b = (sN+a)/f ≥ a`); each gives the
two boxes `−f`, `−(4bcd−1)` mod `17^{(K+1)/2}`.

## 1. What has to be bounded (PROVED, elementary)

**Lemma 1.1 (the union is P ∪ Q, by first occurrence).** The union of all boxes of the seven families
meeting `C_5` equals the union of the (P)-boxes and the (Q)-boxes (Q⁻¹ = Q as sets of boxes, √Q = ∅,
U ⊂ P). Hence, writing `μ₅` for the Haar measure normalised to `μ₅(C_5) = 1`,
`μ₅(covered) ≤ μ₅(covered by P-boxes of level ≤5 and Q-boxes of level ≤7) + T_P + T_Q`, with
`T_P = Σ_{K ≥ 11 odd} 17^{(1−K)/2} · NB_P(K)`, `T_Q = Σ_{k ≥ 9 odd} 17^{1−k} · NB_Q(k)`,
where `NB_P(K)` (resp. `NB_Q(k)`) is the number of *new* (not contained in a box of lower level of
the same type) P-boxes of level `(K+1)/2` (Q-boxes of level k) meeting `C_5`. Trivially
`NB_P(K) ≤ 2 D_P(K)`, `NB_Q(k) ≤ 2 D_Q(k)`.
*Proof.* M17 Lemma 1.1 lists the box types; √Q = ∅ (M17 Lemma 1.3); Q⁻¹ = Q as sets (M17 Lemma 5.1,
consequences); every U-box meeting a cell lies in a P-box (M17 Lemma 5.2), which is counted in the
P-union whatever its level. P-boxes have level `(K+1)/2` and K is odd (M17 Lemma 1.3); Q-boxes
exist only at odd levels (M17 Lemma 1.3). A box contained in a box of lower level adds nothing
to the union. Boxes of level `L` have `μ₅ = 17^{1−L}`. ∎

So the base is the exact uncovered fraction `ρ₀` after P-levels ≤ 5 and Q-levels ≤ 7 (M17 Comp. 3.1
gives `1 − 0.322797`; the exact rational is recomputed in §3), and **a sterile point in `C_5` exists
as soon as `T_P + T_Q < ρ₀`** (same proof as M17 Theorem 4.1).
