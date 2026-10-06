# Hostile review of POINTWISE_OMEGA17.md (task R68b, round 1)

Reviewer branch `side-agent/review-omega17` (merged `side-agent/support-aware` at d33aff5).
From-scratch scripts: `scripts/review_o17_*.py` (none reuse the author's code).

## Verdicts per claim

| item | verdict | notes |
|---|---|---|
| Lemma 5.2 (capped planting) | SOUND | re-derived; exact-rational brute force, 192 random instances (n≤8, k≤3) + equal-odds boundary cases, `scripts/review_o17_capped.py`. Bound is attained for k=0 (dev = 1/R = s−1). |
| Prop 3.1 (i)–(iii) | SOUND | Charlier normalisation matches `₂F₀(−n,−j;;−1/R)`; (ii) checked exactly (`E[ψ_n(N)_m]=R^m`, m<n≤7, three R); (iii) uses `Σ_{|Y|=r}1[Y on]=(N)_r/r!`. |
| Prop 3.1 (iv) table | SOUND (EVIDENCE label correct; can be strengthened) | all 15 R_min values reproduced, positivity on **all** integers j≥0 with a rigorous (Fujiwara) root cutoff, `scripts/review_o17_charlier.py`, `data/review_o17/charlier.txt`. |

## Lemma 5.2 — details

Re-derivation: `(ν−P)(1_y)/P(1_y)=(−1)^{|y|+1}e_{k+1−j}(r_{∖y})/e_{k+1}(r)` follows directly from
O14 Lemma 1.1's definition (`Σ_{J⊇y}w_J=∏_y r·e_{k+1−j}(r_{∖y})/e_{k+1}(r)`). The chain uses the
*full* vector r (not `r_{∖y}`), so only `R−(n−1)r*>0` for `n≤k+1` is needed, which follows from
`R−kr*≥(k+1)/(s−1)≥k+1`; also `e_{k+1}(r)>0` since `R>kr*`. Each factor
`(k+1−i)/(R−(k−i)r*)≤(k+1)/(R−kr*)≤s−1` and `(s−1)^j≤s−1` as `s≤2`. Correct.
Script: builds ν by explicit summation over all `J`, checks `ν(0)=0`, `ν≥0`, equality of all
`≤k`-marginals, and `max_{y≠0}|dν/dP−1|≤s−1` with the tightest admissible
`s=1+(k+1)/(R−kr*)`; all pass, ratio max 1.0 (k=0 equality case).

## Prop 3.1 — details

(i) `C_n(0;R)=1`. (ii) Standard Charlier orthogonality under Poisson(R); reproduced in exact
rationals via `(N)_r(N)_m=Σ_i C(r,i)C(m,i)i!(N)_{r+m−i}` and `E(N)_a=R^a`. (iii) correct
(`C(N,r)` counts the r-sets of events that hold; in the ES reading, two events at the same ℓ with
distinct residues have empty intersection, which does not change the identity).
(iv) From scratch, integer arithmetic on `R^nψ_n(j)`: for each odd n in the table and each
integer R in `[1,R_min+40]` (n≤41) resp. `[R_min−3,R_min+40]` (n=61,81) I computed the
power-basis coefficients, a Fujiwara root bound B (beyond which `R^nψ_n>0`, leading coefficient
positive for n odd; float evaluation with 0.1% safety margin), and evaluated ψ_n at **every**
integer `0≤j≤B` (B up to 51245). Result: the table's R_min is exactly the least good integer R
in every case, the good set is up-closed on each window, and the first failure at `R_min−1`
lies at j between 3 and 567, far below the author's cutoff `4R+6n+20`. So the caveat "the
cutoff is not proved to be beyond the last sign change; a root bound is owed" is now discharged
for the listed (n,R) pairs (reviewer computation; not inserted into the author's text as
new mathematics). Still unverified: non-integer R, and monotonicity in R beyond the windows.

## Defects

(none yet)
