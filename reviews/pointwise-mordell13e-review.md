# Review R107 of POINTWISE_MORDELL13E.md (O107, branch side-agent/xss-sterility) — light, hostile

Reviewer: side agent R107 (branch `side-agent/review-m13e`). Scripts: `scripts/review_m13e_*.py` (from scratch).

## Verdicts

| claim | verdict |
|---|---|
| Lemma 2.1 (parity of ES level in the (2,2) cell) | SOUND |
| §2 scope (x** ≡ x* mod 143 ⇒ no mod-143 argument) | (pending) |
| Comp 3.1 (x** in no class of ES level < 2.59·10¹⁰) | (pending) |
| Prop 4.1 (measure criterion; reduction) | (pending) |
| Labels | (pending) |

## Lemma 2.1 — SOUND

Re-derived. 13B Lemma 1.2 needs only: for q | (relevant T-part), the class condition reduced mod q,
i.e. `f≡−x_q`, `2a²d≡−1` (II3/II2, from `e_T | x_q+4a²d` and `x_q≡2 (q)`), `c²d≡−1` (I3, from
`f_T | x_q²+4c²d`), `c≡−2a` (I2), `2e≡−1` (I4) mod q. All of these depend on `x_q mod q` only, so the lemma
holds on the whole cell `x_11≡2 (11), x_13≡2 (13)` (15≡2 mod 13: yes). The ES-level formulas (13B Lemmas
2.1–2.4, Cor 2.5) give the parities stated: II1/I4 `v_T(ab)`, II2 `v_T(f)`, I2 `v_T(ac)+v_T(f)`, II3
`v_T(e)+v_T(d)` (since `N=e_T a_T² d_T`), I1 `v_T(d)`, I3 `v_T(f)+v_T(d)` (`N=f_T c_T² d_T`); with Lemma 1.2
(`v_T(d)` odd for I3) this is the statement.

*From-scratch check* (`scripts/review_m13e_parity.py 3000 {1,2}`): random T-generic data of all 7 families
(T-parts up to `11³`, `13³`, `11²13`, …), literal classes from the ET Prop 1.9 residues (own code), ES level
**verified by the explicit ES identity** of 13B Lemmas 2.1–2.4 (exact fractions) for every T-generic datum
(≈38 000), `M_T ≤ N ≤ M_T²` for all; 906 data whose box meets the (2,2) cell: **0 parity failures**. The I3
exception is non-vacuous (both parities of `v_T(f)` occur). Negative control: in the cell (2,1) the same test
fails for 25 of 208 data, so the check has teeth.
