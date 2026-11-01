# z52d Pass 2 — batch TO4 (101 "touched" items)

Counts: 101 inputs, 101 outcomes (`data/z52b/pass2/outcome_TO4.jsonl`): nothing 91, covered 7, interesting 3, needs-compute 0, skipped 0.
Interesting: Z1605 (Type II (c,d) witnesses for the C-form exceptions), Z1620 (winning-C count grows like log X, not linearly), Z1624 (exact dual form of Type I with c=1).
Premise corrections: Z1355 (U_n is rational: X=1/x gives the plane X+Y+Z=4/n, so the Fricke/PVI identification is moot), Z1668 (ES surface is log Calabi–Yau, not log Fano), Z1674 (y/z-pencil slices are line + conic, not elliptic), Z1598 (rich failures are not index-2 type).
Not done (explicit per item in the outcome file): 47 items record a step not run (Q-series/theta, Brandt, QRT, Yang–Baxter, cusp lattices, Painlevé-side, SOS, Frobenius/Chebotarev, MW-rank computations); their `not_done` fields say so.
Scripts: `scripts/z52d_p2_TO4_*` (C-form sweep, Type I sweep, analyses, subgroup criterion, e-slice, outcomes writer). Data: `data/z52b/pass2/TO4/`.
Note on tools: the C-form and Type I sweeps and full-C checks are in the scripts; sample sizes and caps are stated per item.

## Z1605 — Type II (c,d) certificates for the C-form exceptions (interesting)

Type II(c,d) ⟺ 4c²dp+1 has a divisor f ≡ −1 (mod 4cd) with cofactor also ≡ −1 (mod 4cd) (CONDITIONAL_ES §1). The C-form is c=1.
Minimal (c,d) with a Type II solution, over the nine full-C C-form exceptions ≤ 10⁶ (checked for all C ≤ (p+2)/4):
- (2,1): 409, 577, 5569, 9601, 23929, 712321 (e.g. 409: 16·409+1 = 6545 = 7·935, 7 ≡ 935 ≡ −1 mod 8)
- (2,2): 83449, 329617
- (3,22): 102001
Every one of the nine has a Type II certificate with c ≤ 3; c = 1 never works for them.
Reproduce: `scripts/z52d_p2_TO4_forms.py` (`typeII`), `scripts/z52d_p2_TO4_fix.py`, C-form full-C check `/tmp/cform_TO4 p (p+2)/4 p` from `scripts/z52d_p2_TO4_cform.c`.
Next: check whether the (c,d) witnesses share a structure (c²d versus the class of p).

## Z1620 — growth of the winning-C count (interesting)

For p ≡ 1 (mod 24), p ≤ 10⁷, C ≤ 400: N(X) = #{C ≤ X : C-form win}. Mean N(X)/log X = 1.266 (X=30), 1.254 (X=100), 1.220 (X=300), 1.208 (X=400). Mean N(X) = 7.24 at X=400. So lim inf N(X)/X = 0; the count is logarithmic (C=1 slice). Σ_C win/C converges (≈1.4 over p ≥ 1000, K=300 data). The item's "positive density" premise is false on data.
Caveat: this is the c=1 slice only. ET's log² p count for all solutions needs the c>1 slices too; this is where the Z1605 witnesses live.
Reproduce: `scripts/z52d_p2_TO4_stats.py`, `scripts/z52d_p2_TO4_analyze.py`.

## Z1624 — exact dual form of Type I with c = 1 (interesting)

Claim (proved in the outcome, checked on 51 primes ≡ 1 mod 4 below 600): Type I with c=1 (f | p²+4d, f ≡ −p mod 4d) holds iff ∃ k ≥ 1 such that kp+1 has a divisor f ≡ −p (mod 4k).
Proof sketch: put 4dk = f+p. Then k(p²+4d) ≡ p(kp+1) (mod f), and gcd(f,k)=1 when f | kp+1. Swap d↔k to go both ways.
Result: the same data reappears as a shifted-form statement with modulus 4k, target −p and number kp+1 (C-form has modulus 4C, target −1, number 4Cp+1). Reparametrisation only; no new existence result.
Reproduce: `scripts/z52d_p2_TO4_batch2.py` (section Z1624).
