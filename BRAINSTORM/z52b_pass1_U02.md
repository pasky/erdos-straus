# z52b pass 1 — batch U02 (§2 untried; 207 items) — COMPLETE: every item has a line; some remain open

- Outcomes (207): nothing 87, covered 12, interesting 4, needs-compute 52, skipped 52 (skipped = restatement/meta only, or open items from the first pass that the fix rules did not reach; see the list at the bottom).
- Interesting: Z1054 (exactly one denominator divisible by p ⇒ (y/p)(z/p) = −1 in 10656/10656 cases, p<5000); Z1568 (no proper divisor ≡ −1 mod 4C for any C≤200 among p≤10⁴ gives exactly {409,577,5569,9601}); Z0968 (Tunnell A(p) keeps +0.30 partial correlation with residual log U after (2/p), h(−8p), h(−4p); raw −0.31 is a mod-8 split; item's +0.18 not reproduced); Z2983 (conductor-24 step: the quadratic character (6/p) = (2/p)(3/p) adds +0.06 out-of-sample over the additive mod-8 + mod-3 model; absent from the repo).
- Covered/nothing with substance: Z3075 and Z3030 reproduce the T1 odd-square exclusion (failure rate 1.0 at 975 odd-square N; 0/1600 divisor pairs); Z0339 mean U/log²p = 0.97; Z2562 enrichment is a τ(N) confound; Z3130 parity lemma (d ↦ N/d); Z0541 divisor counts far from equidistributed (93.5% zero-count slices).
- Still open (not run to the fix-rule standard): 52 skipped and 52 needs-compute lines. The needs-compute lines state the computation and an estimate; skipped lines are mostly generic first-pass items (Z0990–Z1313 range) whose step was never made precise. These need a worker decision.
- Proved side facts: Z0259 (no repeated denominators for p≡1 mod 4), Z0868 (≥2 even denominators for odd n), p | xyz for every solution (4xyz = p(xy+yz+zx)), Z3048 (p ∤ xyz for positive Mordell triples).
- Records: data/z52b/pass1/outcome_U02.jsonl; scripts scripts/z52b_p1_U02_*; data data/z52b/pass1/U02/*.json.


## Z1054 — one denominator divisible by p (interesting)

`scripts/z52b_p1_U02_f.py`. Solutions from `esols`, p=1 mod 4, p<5000, 15555 solutions. If exactly one denominator is divisible by p, the other two satisfy (y/p)(z/p) = −1 in all 10656 cases ((−1,+1) 5903, (+1,−1) 4753). Derivation so far: x = pa, 4a−1 = ph, h·yz = a(y+z), yz·h² = a(s+a)²/s with s = hy−a, so (yz/p) = (as/p). Next: prove (as/p) = −1 is forced.

## Z1568 — C-form exceptional set (interesting)

Definition: p=1 mod 4 with no proper divisor d of 4Cp+1 with d ≡ −1 mod 4C, for every C ≤ 200. For p ≤ 10⁴: exactly {409, 577, 5569, 9601} (`scripts/z52b_p1_U02_f.py`, data/z52b/pass1/U02/fix_f.json). With C ≤ 60, p in (10⁴, 6·10⁴] gives 19141, 23041, 23929, 26209, 46237, 49669 (not comparable: smaller C range). Next: extend to p ≤ 10⁶ with C ≤ 200 and test a local obstruction at 2 or at primes dividing C.

## Z0968 — Tunnell counts beyond class numbers (interesting)

A(n)=r_{1,2,8}(n), B(n)=r_{1,2,32}(n), p=1 mod 4, p<2000 (n≈300). Raw corr(resU, A) = −0.31, corr(resU, B) = −0.30, corr(resU, A−2B) = −0.08. A(p)=0 for every p≡5 mod 8 and never for p≡1 mod 8 (`scripts/z52b_p1_U02_h.py`). Controlling (2/p), log h(−8p), log h(−4p): partial corr(resU, A) = +0.30, corr(resU, B) = +0.30. Item's ρ≈+0.18 not reproduced. Next: check definitions against final_checks.json.

## Z2983 — conductor-24 interaction (interesting)

Out-of-sample R² of residual log U (p=1 mod 4, 100<p≤3·10⁴) on residue-class indicators, cumulative over moduli: q=8: 0.57; q=23: 0.63; q=24: 0.73 (`scripts/z52b_p1_U02_o.py`). The step at q=24 is the quadratic character (6/p) = (2/p)(3/p): on the mod-8 + mod-3 base it adds +0.06 out of sample (0.421 → 0.478; `scripts/z52b_p1_U02_p.py`), with corr(residual, (6/p)) = −0.26. The repo has no (6/p) or (2/p)(3/p) term (git grep). Next: test with all Legendre symbols and class numbers on p ≤ 10⁵.

## Reproduce

Helper: scripts/z52b_p1_U02_lib.py (esols, validated against f4_all_30000 for n<3000). Scripts: z52b_p1_U02_{Z0081,a,b,c,d,e,f,fp,g,h,m,n,o,p}.py.
