# z52d Pass 2 — batch TO1 (101 "touched" items; ES is OPEN)

Counts: nothing 95, interesting 4 (Z0269, Z0276, Z0283, Z0284), covered 2 (Z0301, Z0410), needs-compute 0, skipped 0.
Interesting: Z0283/Z0284 (least slice index E(p) = min(4x-p): records 3,7,11,23,31,59,107 up to 10^8; 90% of primes E=3, 98.1% E<=7, ~2% E>=11 per decade, no drift);
Z0269 (per-family failure counts: Type II(1,1) fails at 26% of primes < 5*10^4, the union over Type II with c,d<=12 covers all of them, Type I union leaves 89);
Z0276 (Eisenstein-norm world: every survivor uses 3 | a denominator, forced by a 3-adic congruence).
Caveat: partial pass — 25+ catalogue items were triaged as `nothing` with the step not run (see not_done per item); this is recorded per item, not hidden.

All ES statements are about the existence of solutions for explicit primes; none claims a result about ES in general. Labels: EVIDENCE for every number below; the Z0276 3-adic step is an argument (PROVED for the 3-free case); Z0269 divisor forms are the repo's CONDITIONAL_ES §1 (PROVED there).

## Z0283 / Z0284 — least slice index E(p) = min over solutions of (4x - p), x the least denominator   [EVIDENCE]
- Method: `scripts/z52d_p2_TO1_es.c` mode E (stop at first x with a solution; 128-bit arithmetic); 2,880,504 primes = 1 mod 4 below 10^8 in 20 s. Exact recomputation (sympy, unbounded integers) agrees on 49 sampled primes including all records; every reported solution is verified in exact rationals (`scripts/z52d_p2_TO1_exactE.py`). Full table not kept (30 MB); summary in `data/z52b/pass2/TO1/Eslice_1e8_summary.txt`.
- Records E: p=5 (3), 73 (7), 1129 (11), 1201 (23), 21169 (31), 118801 (59), 8803369 (107); none in (8.8*10^6, 10^8]. E/log^2 p at the records: 1.16, 0.38, 0.22, 0.46, 0.31, 0.43, 0.42.
- Tail: P(E>=11)=1.9e-2, P(E>=19)=3.9e-3, P(E>=27)=6.0e-4, P(E>=35)=1.2e-4 (roughly e^{-0.2 t}).
- Interpretation (not proved): records are consistent with c*log^2 p (c ~0.2-0.46) and with an exponential-tail maximum ~5 log p; 8 records cannot distinguish them. This is the scale of the expected witness count (log^2 p), which is a heuristic match, not evidence for ES.
- Next: segmented sieve to 10^9-10^10 to test the record scale; a fixed-E covering test (Mordell) would need the residue classes of each slice.

## Z0269 — per-family failure counts for Type I / Type II divisor families   [EVIDENCE]
- Families (repo CONDITIONAL_ES §1): Type I(c,d): f | p^2+4c^2d with f = -p (mod 4cd); Type II(c,d): ff' = 1+4c^2dp with f = f' = -1 (mod 4cd). Exact sympy, c,d <= 12.
- p = 1 mod 4 below 5*10^4 (2549 primes): best Type II(1,1) fails at 673 (26%); best Type I(1,2) fails at 1257 (49%); median family fails at ~2460 (96%).
- Unions: Type II over all c,d<=12 leaves 0 primes uncovered; Type I union leaves 89. Below 10^4: Type II union 0 uncovered, Type I union 19.
- Caveat: the family union is over 144 parameter pairs; each family is individually a divisor condition; no asymptotic claim.

## Z0276 — Eisenstein-norm world and the 3-adic reading   [EVIDENCE + argument]
- Norm world (every prime = 2 mod 3 to even power in each denominator) fails at 451 of 499 primes below 8000 (reproduced). The 48 survivors: in every solution at least one denominator is divisible by 3 (`data/z52b/pass2/TO1/worlds_8000.json`, `scripts/z52d_p2_TO1_worlds.py`).
- Argument: a denominator prime to 3 in this world is = 1 (mod 3). If all three were prime to 3, 1/x+1/y+1/z = 0 (mod 3) but 4/p is a 3-adic unit. So 3-free solutions are impossible; the survivors use 3 as the argument predicts.
- The failures themselves (403 with 3 | denominators possible) are not explained by this congruence.

## Other notes from the batch (short)
- Z0260 (12-world: all denominators = 0 mod 3): 18 failures to 10^5, last 12241; no failure in (12241, 10^5]; not shown to stabilise.
- Z0262 (2-adic): realised valuation triples always have the top two valuations equal (forced by ultrametric cancellation); the all-even-with-8 world fails at 14 primes to 10^5.
- Z0318: certified k <= 15 (found factors = 3 mod 4 of 1+l^k) for all odd l < 3*10^5; the 'least k' values have uncertified smaller k (cofactors > 10^6), so no uniform bound claim either way.
- Z0256: Prop 3.3 construction verified for 21 primes; trace descent returns the same remainder l/(px) (no new integer identity).
- Z0461: B2 covering on p = 1 mod 24 (<10^5): C<=2 covers 81%, C<=10 covers 97.3%.
