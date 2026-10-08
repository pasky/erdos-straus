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

## 2. A complete N^{2/5}-type enumerator for P (PROVED completeness; CERTIFIED output)

**Lemma 2.1 (ET four-regime cover, made exact).** Let `(a,b,c,d,e)` be an N-point of `Σ^II_n` with
`a ≤ b`. If `X_e² X_ad X_ac X_cd ≥ n²` (positive integers), then `e ≤ X_e` or `ad ≤ X_ad` or
`ac ≤ X_ac` or `cd ≤ X_cd`. In each regime the point is recovered from a factorisation:
`e`: `4abd = n+e`; `ad`: `f | n+4a²d`, `f ≡ −1 (4ad)`; `ac`: `f | nc+a`, `f ≡ −1 (4ac)`;
`cd`: `f | 4c²dn+1`, `f ≡ −1 (4cd)` (ET (2.13), (2.19), (2.20), (2.21)).
*Proof.* With `a ≤ b`: `ce = a+b ≤ 2b` and `4abd = n+e` with `e ≤ a+b ≤ 2abd`, so `abd ≤ n/2` and
`acde ≤ 2abd ≤ n` (the proof of ET Lemma 2.8, which uses only the equations). Hence
`e²(ad)(ac)(cd) = (acde)² ≤ n²`. ∎

`scripts/m17b_penum.py K` implements this with `X_cd ≈ n^{0.3}` (so that `4c²dn+1 < 10^{25}`) and
`X_e = X_ad = X_ac = ⌈(n²/X_cd)^{1/4}⌉+1`. Factorisations use GNU coreutils `factor` (GMP; primality
proved by a Lucas test). Every candidate is checked against `4abcd = a+b+nc`. **Validation:** the output
coincides *as a set of (a,b,c,d)* with the naive scan `scripts/m17b_brute.py` (all `a ≤ b`,
`2ab ≤ n`, `e = (−n mod 4ab) | a+b`, M17 §6) for K = 5, 7. Its counts equal M17's `D_P(K)` (both engines)
for K = 1, 3, 5, 7, 9. Run times: K = 9 takes 9 s and K = 11 a few minutes (vs 8 min for K = 9 with `m17_enum`).

**Computation 2.2 (CERTIFIED by one engine, validated above).** `D_P(11) = 836`.
So `D_P(K) = 2, 32, 121, 258, 604, 836` for K = 1, …, 11 (odd).

## 3. Exact union through level 6 (CERTIFIED)

`scripts/m17b_union.py` computes the exact union in `C_5` of the P-boxes from `m17b_penum` and the Q-,
U-boxes (and their inverses) from `m17_enum`. Levels ≤ 5: `covered = 26960/83521`, uncovered
`56561/83521`, which reproduces M17 Comp. 3.1 exactly. Adding Q/U level 7 gives uncovered `16346035/24137569`,
also reproducing M17. Adding the **P-boxes of level 6 (K = 11)** gives 161 boxes in `C_5`, of which 100 are new:

| level | new boxes in C_5 | measure added (fraction of cell) |
|---|---|---|
| 5 | 83 (P 54, Q 29) | 9.94·10⁻⁴ |
| 6 | 100 (P) | 7.04·10⁻⁵ |
| 7 | 94 (Q only; P K=13 pending) | 3.9·10⁻⁶ |

**Computation 3.1.** After all P-boxes of level ≤ 6 and all Q/U boxes of level ≤ 7, the uncovered
fraction of `C_5` is **ρ₁ = 16344335/24137569 = 0.677132606…** (CERTIFIED).
