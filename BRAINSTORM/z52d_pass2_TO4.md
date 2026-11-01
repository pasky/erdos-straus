# z52d Pass 2 — batch TO4 (101 "touched" items)

Counts (after lint-fix round): 101 inputs, 101 outcomes (`data/z52b/pass2/outcome_TO4.jsonl`): nothing 88, covered 7, interesting 6, needs-compute 0, skipped 0. `scripts/z52d_pass2_lint.py` reports 0 flagged of 101.
Interesting: Z1605 (Type II (c,d) witnesses for the C-form exceptions), Z1620 (winning-C count grows like log X), Z1624 (exact dual form of Type I, c=1), Z1025 (three-way dependence: win(C1)&win(C2) raises win(C1C2) about 2×; pairwise control flat), Z1468 (t≡0 mod 4 restriction loses 8 of 75 primes at t≤100), Z1677 (integral ES triples accumulate at the node P₃).
Lint-fix round (28 flagged items: Z1025 Z1053 Z1057 Z1091 Z1113 Z1149 Z1152 Z1163 Z1172 Z1178 Z1286 Z1297 Z1299 Z1300 Z1301 Z1304 Z1402 Z1468 Z1551 Z1636 Z1666 Z1667 Z1668 Z1673 Z1675 Z1676 Z1677): each now has a measured result; scripts `scripts/z52d_p2_TO4_fix_{A..F}.py`, `scripts/z52d_p2_TO4_lintfix_write.py`. Premise checks: Z1668 (ES surface is log CY, not log Fano; Wilsch is about threefolds), Z1673 (ES fibres are rational conics, not norm tori), Z1149 (no QRT pair: equation linear in x).
Residual, outside the lint list: 21 records not in the lint list still say a step was not done in the middle of the summary (Z0997 Z1002 Z1009 Z1011 Z1014 Z1030 Z1037 Z1275 Z1296 Z1388 Z1437 Z1535 Z1555 Z1577 Z1586 Z1589 Z1600 Z1601 Z1634 Z1645 Z1672). The lint does not catch these; they need a second round.
Not-done fields in other records remain as written in the outcome file.

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

## Z1025 — three-way co-occurrence of C-form wins (interesting)

For p≡1 mod 24, p≤10⁶, C≤400: P(win(C1C2) | win(C1)&win(C2)) = 0.048 (45881 triples) against 0.023 for the same target C unconditionally (ratio 2.1); lcm target 0.046 vs 0.024 (ratio 1.9). Pairwise control: P(win C2 | win C1)/P(win C2) = 0.99 (coprime), 0.96 (non-coprime), so the excess needs the third event. Mechanism not identified.
Reproduce: `scripts/z52d_p2_TO4_fix_F.py` (target-matched), `scripts/z52d_p2_TO4_fix_A.py` (composition table).

## Z1468 — t≡0 (mod 4) restriction in the I3 census (interesting)

For the 75 primes ≡1 mod 24 in [1000,6000]: a word tuv−u−v with t,u,v≥3 and t≤100 exists for all 75; with 4|t for 67; only non-4|t words for 8 (10.7%). This quantifies the gap that the t∈4ℤ restriction creates in this range.
Reproduce: `scripts/z52d_p2_TO4_fix_A.py` (section Z1468).

## Z1677 — integral ES triples near the node P₃ (interesting)

Nodes of the cubic 4xyz=p(xy+yz+zx)w: the four coordinate points (partials vanish). For ES triples x≤y≤z: fraction with y/z<0.01 is 11/15 (p=409), 12/18 (577), 9/19 (1009), 14/22 (1321), 6/9 (2521), 30/42 (3001), 24/27 (5569), 20/23 (9601). No triple approaches the origin node P₀ since x>p/4. Rate of approach versus p not yet measured.
Reproduce: `scripts/z52d_p2_TO4_fix_D.py`.

