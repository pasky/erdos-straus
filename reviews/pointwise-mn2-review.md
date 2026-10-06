# Review of POINTWISE_MN2.md (task R74, hostile reviewer)

Reviewer branch `side-agent/review-mn2` (merged `side-agent/adm-m` at fb981ad). Author has quit;
wording/label repairs are applied directly to `POINTWISE_MN2.md` in this branch, marked
"applied by reviewer". From-scratch scripts: `scripts/review_mn2_*.py`.

## Verdict summary (filled in progressively)

| claim | verdict |
|---|---|
| Lemma 1.1 | (pending) |
| Lemma 1.2 | (pending) |
| Lemma 1.3 | (pending) |
| Input (H) as quoted | (pending) |
| Lemma 2.1 | (pending) |
| Thm 3.1 | (pending) |
| §4 data + Assessment | (pending) |
| Prop 5.1 | (pending) |

## Defects

(pending)

## A. §4 data (recomputed from scratch) — numbers SOUND, headline claim OVERCLAIMED

`scripts/review_mn2_delta.py` (independent CRT-tensor implementation; definition of `H_m(Q)` taken
from MN §0/§3: all `M | Q`, `M ≥ 3`, `M ≡ −1 (m)`, all `D | A²`). Output (exact fractions):

```
m=5 q0=8 Q=168 phi=48 hard=12 delta=1/4 1/delta=4 q0^-1/2/delta=1.414 (#M=4)
m=5 q0=9 Q=504 phi=144 hard=18 delta=1/8 1/delta=8 q0^-1/2/delta=2.667 (#M=6)
m=5 q0=11 Q=5544 phi=1440 hard=132 delta=11/120 1/delta=10.91 q0^-1/2/delta=3.289 (#M=12)
m=5 q0=13 Q=72072 phi=17280 hard=898 delta=449/8640 1/delta=19.24 q0^-1/2/delta=5.337 (#M=24)
m=5 q0=16 Q=144144 phi=34560 hard=1796 delta=449/8640 1/delta=19.24 q0^-1/2/delta=4.811 (#M=30)
m=5 q0=17 Q=2450448 phi=552960 hard=17510 delta=1751/55296 1/delta=31.58 q0^-1/2/delta=7.659 (#M=58)
m=5 q0=19 Q=46558512 phi=9953280 hard=163044 delta=4529/276480 1/delta=61.05 q0^-1/2/delta=14.01 (#M=120)
m=7 q0=8 Q=120 phi=32 hard=10 delta=5/16 1/delta=3.2 q0^-1/2/delta=1.131 (#M=2)
m=7 q0=11 Q=3960 phi=960 hard=234 delta=39/160 1/delta=4.103 q0^-1/2/delta=1.237 (#M=7)
m=7 q0=13 Q=51480 phi=11520 hard=1624 delta=203/1440 1/delta=7.094 q0^-1/2/delta=1.967 (#M=16)
m=7 q0=17 Q=1750320 phi=368640 hard=34930 delta=3493/36864 1/delta=10.55 q0^-1/2/delta=2.56 (#M=40)
m=7 q0=19 Q=33256080 phi=6635520 hard=460160 delta=719/10368 1/delta=14.42 q0^-1/2/delta=3.308 (#M=80)
m=6 q0=11 Q=385 phi=240 hard=84 delta=7/20 1/delta=2.857 q0^-1/2/delta=0.8615 (#M=4)
m=6 q0=13 Q=5005 phi=2880 hard=842 delta=421/1440 1/delta=3.42 q0^-1/2/delta=0.9487 (#M=8)
m=6 q0=17 Q=85085 phi=46080 hard=9110 delta=911/4608 1/delta=5.058 q0^-1/2/delta=1.227 (#M=16)
m=6 q0=19 Q=1616615 phi=829440 hard=128030 delta=12803/82944 1/delta=6.478 q0^-1/2/delta=1.486 (#M=32)
```

Every entry of the §4 table (all three rows m = 5, 7, 6, and the derived `q_0^{−1/2}/δ` row) is
reproduced to the printed precision; `δ_5(Q(8)) = 12/48 = 1/4` agrees with MN's `48/192` mod 840.
Remarks: (i) for m = 6, 7 the quantity `q_0^{−1/2}/δ` grows slowly (m = 6: 0.86 → 1.49 over
q_0 = 11..19) — seven/five data points with `q_0 ≤ 19` say nothing about growth "faster than
`q_0^{1/2}`" asymptotically; (ii) the heuristic `log(1/δ) ≍ (log q_0)³` is not visible at this
range either (m = 5, q_0 = 19: `log(1/δ) = 4.1`, `(log 19)³ = 25.5`). See defect D3.

## B. Input (H) vs. the source — SOUND as quoted (constants not explicit, but effective)

Checked against `sources/henriot-1102.1643.pdf` (pdftotext), §2 (definitions: `‖P‖` = sum of
|coefficients| of P; `M_k(A,B,ε)` via (2.10); `Q* = ∏R_h`, `D* = disc Q*`), Thm 5 (p. 6) and
Cor 1 (p. 7):
* hypotheses: Q primitive (no "no fixed prime divisor" needed — that is exactly Henriot's gain
  over NT Thm 1), `0 < ε < α/(50g(g+1/δ))`, `F ∈ M_k(A,B,ε)`, `x ≥ c_0‖Q‖^δ`, `x^α ≤ y ≤ x`;
  `c_0` and the implied constant depend at most on `g, α, δ, A, B` — quoted correctly;
* Cor 1's RHS carries the extra restrictions `(n_1⋯n_r, D*) = 1`, `(n_i,n_j) = 1`; MN2 drops them,
  which is legitimate for `F ≥ 0` (upper bound). Product is over `g < p ≤ x` — quoted correctly.
* Application in Lemma 2.1(i): `Q_1 = qX + c_1`, `Q_2 = mX + c_2`, `qc_2 − mc_1 = −1`. Re-derived:
  both primitive and coprime; `Q = Q_1Q_2 = qmX² + (qc_2+mc_1)X + c_1c_2` has discriminant
  `(qc_2+mc_1)² − 4qmc_1c_2 = (qc_2−mc_1)² = 1`, so `D* = 1`, `Δ_{D*} = 1` (empty product).
  `‖Q‖ ≤ ‖Q_1‖‖Q_2‖ ≤ (2q+1)·2m ≤ 6qm` ✓. `ρ(p) = 2` for `p ∤ qm` (distinct roots since the
  resultant is ±1), `ρ(p) = 1` for `p | qm` ✓; `ρ_{R_h}(n) ≤ 1` ✓. `ε_0 = 1/1001 < 1/800 =
  α/(50g(g+1/δ))` at `g = 2, α = δ = 1/2` ✓.
* "Ineffective": the source gives no explicit constants, but nothing in the NT/Henriot argument
  is ineffective (no Siegel-type input); the constants are computable in principle. MN2 calls
  `c_1` "ineffective" (§3 Thm 3.1, §4 item 1, §6 table) — wrong word, see defect D2.
