# Hostile review of POINTWISE_OMEGA17.md (task R68b, round 1)

Reviewer branch `side-agent/review-omega17` (merged `side-agent/support-aware` at d33aff5).
From-scratch scripts: `scripts/review_o17_*.py` (none reuse the author's code).

## Verdicts per claim

| item | verdict | notes |
|---|---|---|
| Lemma 5.2 (capped planting) | SOUND | re-derived; exact-rational brute force, 192 random instances (n≤8, k≤3) + equal-odds boundary cases, `scripts/review_o17_capped.py`. Bound is attained for k=0 (dev = 1/R = s−1). |

## Lemma 5.2 — details

Re-derivation: `(ν−P)(1_y)/P(1_y)=(−1)^{|y|+1}e_{k+1−j}(r_{∖y})/e_{k+1}(r)` follows directly from
O14 Lemma 1.1's definition (`Σ_{J⊇y}w_J=∏_y r·e_{k+1−j}(r_{∖y})/e_{k+1}(r)`). The chain uses the
*full* vector r (not `r_{∖y}`), so only `R−(n−1)r*>0` for `n≤k+1` is needed, which follows from
`R−kr*≥(k+1)/(s−1)≥k+1`; also `e_{k+1}(r)>0` since `R>kr*`. Each factor
`(k+1−i)/(R−(k−i)r*)≤(k+1)/(R−kr*)≤s−1` and `(s−1)^j≤s−1` as `s≤2`. Correct.
Script: builds ν by explicit summation over all `J`, checks `ν(0)=0`, `ν≥0`, equality of all
`≤k`-marginals, and `max_{y≠0}|dν/dP−1|≤s−1` with the tightest admissible
`s=1+(k+1)/(R−kr*)`; all pass, ratio max 1.0 (k=0 equality case).

## Defects

(none yet)
