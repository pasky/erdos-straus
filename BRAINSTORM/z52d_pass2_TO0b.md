# z52d Pass 2, batch TO0b (99 items): summary (after lint-fix round)

Counts: nothing 89, interesting 8, covered 2 (Z0006, Z0147), needs-compute 0, skipped 0. Interesting: Z0005, Z0086 (proof of positive ES over Z[sqrt3] for n = 1 mod 4), Z0087 (|S| = 1 mechanism for all odd l < 400), Z0094 (Gaussian cone not multiplicatively closed), Z0114, Z0115 (premises false), Z0178 (repo's pure-Ford list contradicted), Z0214 (odd prime squares are harder than 4).
Lint (scripts/z52d_pass2_lint.py): 0 flagged of 99 after the fix round for the 19 stub records. Known gap: 29 records still have summaries beginning 'Not executed' (Z0018-Z0024, Z0033, Z0036, Z0039, Z0040, Z0044, Z0048, Z0054, Z0058, Z0061, Z0062, Z0068, Z0072, Z0079, Z0089, Z0096, Z0176, Z0177, Z0189, Z0194, Z0204, Z0215, Z0250, Z0251). The lint regex does not match 'Not executed', so they pass lint but violate the fix brief; they need a follow-up round.
Full per-item lines: data/z52b/pass2/outcome_TO0b.jsonl (99 lines). Scripts: scripts/z52d_p2_TO0b_*, scripts/z52d_p2_fix_TO0b_*.

## 0. Method and limits
- FF engine: scripts/z52d_p2_TO0b_ff.py. exists_general is lemma-free (ultrametric bound + divisor enumeration) and was cross-checked against the repo's Lemma-1.3 engine and data/ffl/fail_q*.txt (identical fail sets on 13 (q,A,n) cases). A bug found in the Lemma-1.3 counter (kappa is free, so (a,b) pairs over-count triples) is fixed in count_solutions (dedup on triples; brute ordered count = 2*unordered - #(Y=Z) verified on 40 irreducibles).
- Z census: scripts/z52d_p2_TO0b_numer.c (generic numerator, equal to TO1 es.c on m=4), scripts/z52d_p2_TO0b_filters.c.
- Not done: most theory and number-field items (Z0018-Z0021, Z0023, Z0033, Z0036-Z0040, Z0044, Z0048, Z0054, Z0056-Z0058, Z0061-Z0064, Z0068, Z0072, Z0075, Z0078, Z0083-Z0091, Z0094, Z0096, Z0105, Z0166, Z0176-Z0178, Z0186, Z0189, Z0191, Z0194, Z0204, Z0209, Z0215, Z0218, Z0250, Z0251) were not executed; see not_done fields. Z0009, Z0007, Z0015, Z0017, Z0024, Z0028 are partial.

## 1. Z0005 (interesting): leading coefficients restricted to squares
For A = T, q = 5 (H = {1,4}): monic failures 2, 2, 1 of 10, 40, 150 irreducibles (n = 2, 3, 4) drop to 0, 0, 0 with square leading coefficients. For q = 7 (H = {1,2,4}): 6 of 21 and 21 of 112 (n = 2, 3) drop to 0. Free leading coefficients: 0 failures for q = 3 (n <= 5), 5 (n <= 4), 7 (n <= 3). Every square-lc witness verified exactly (A XYZ = P(XY+YZ+XZ)). Reproduce: scripts/z52d_p2_TO0b_Z0005_sqlc.py, scripts/z52d_p2_TO0b_verify_witness.py. Interpretation: the monic normalisation carries the hardness; an index-2 cone already removes all monic failures in this range. Not done: deg P = 8.

## 2. Z0114 (interesting): 'odd-denominator ES is impossible' is false as stated
Parity forces an even number of odd unit fractions (no 3-term odd solutions for odd n <= 301), but two odd terms already exist for 969 of the 1500 odd n in [3, 3001] (4/3 = 1/1 + 1/3, 4/9 = 1/3 + 1/9). Reproduce: scripts/z52d_p2_TO0b_parity_numer.py.

## 3. Z0115 (interesting): 'denominators = 1 mod 3 impossible when 3 does not divide n' is false
4/7 = 1/4 + 1/7 + 1/7 + 1/28 (all denominators = 1 mod 3). For every n = 1 mod 3, n <= 200, a four-term solution with all denominators = 1 mod 3 exists (66/66). Mod-3 bookkeeping only forces k = n (mod 3). Reproduce: scripts/z52d_p2_TO0b_Z0115_check.py.

## 4. Z0214 (interesting): odd prime squares are not like 4
Over primes 5 <= p < 30000, 4/p is 3-term representable for all p; 9/p fails for p = 5, 11, 19 (3 primes); 25/p fails for 80 primes (3, 5, 7, 11, 13, 17, 19, 29, 31, 41, ...). Odd prime squares are strictly harder than 4 and the failure count grows fast. Census: data/z52b/pass2/TO0b/numer/, numer_stats.txt. Not done: residue classes mod 840 of the 80 failures.

## 5. Other checked facts (for the record)
- Divisor closure of numerator sets verified (0 violations, m <= 25, p < 30000).
- Fail(8) = {3, 11, 17, 131, 241} for p < 30000; Fail(4) empty; Fail(16) contains 5, 13, 193 (and 16/5 > 3 is size-trivial).
- Z0200 premise confirmed for p < 2e4 (fails exactly 5, 13, 37, 97). Z0216 chain-world failures: 161 of 267 primes = 1 mod 24, all failures = 1 mod 24. Z0201 premise: 45 is the p = 1 mod 4 count; over all primes the count is 94. Z0202: for every prime p < 2e4 a solution with p not dividing x exists.
- FF: mean solution multisets per irreducible P, A = T, scale as ~0.9 n^3 / q for n >= 4 (q = 3, 5, 7); FUNCTIONFIELD_ES.md §7.1 law confirmed with exact counts.
- Z0060: 2-term 4/p = 1/a + 1/b over Z is solvable iff p = 3 (mod 4) (checked p < 400); the Bradford-Ionascu identity 4 = 1/u + 1/ubar (u = -4+3sqrt2) is verified.
- Literature: Niederreiter's FF Zaremba-type bound (arXiv:1704.02640 Thm 4.2.1) for q != 2.

## 6. Fix round (19 stub records; scripts/z52d_p2_fix_TO0b_*)
- Z0086 (interesting): explicit proof route for D = 3: eps^5 = 362+209 sqrt3 = -1 mod 11 O_K, kappa = 33+19 sqrt3 totally positive, 1/u+1/v = 11 with u = kappa/eta, v = kappa; identity verified exactly for several n = 1 mod 4 (scripts/z52d_p2_fix_TO0b_Z0086_check.py).
- Z0087 (interesting): for every odd prime l < 400 some j <= 12 has a divisor e = 3 mod 4 of 1+l^j (l = 193, 337 need j = 5, e = 11).
- Z0094 (interesting): the Bradford-Ionascu Gaussian cone is not multiplicatively closed ((1+i)(-1-2i) = 1-3i).
- Z0178 (interesting): the pure Ford criterion holds for p = 41 (b = 12, N = 24, e = 7, a = 2) and p = 241 (b = 66, N = 84, e = 23, a = 3); only 5 and 17 fail up to 3000.
- Z0037: no Int(Z)-polynomial identity for 4/(4t+1) with X in a box of degree <= 2; the same code finds 3 identities for 4t+3 (control).
- Z0056, Z0064: integer and semiring replacements of the unit fail (size argument; {1, 2, sqrt2} only).
- Z0075, Z0105: proof-level statements (collapse criterion; local leading-coefficient dictionary).
- Z0078, Z0186: exact reparametrisations (square-discriminant bijection; Dedekind sums reduce to x+y+z).
- Z0083, Z0084: Prop 2.2 encodings, existence checks only.
- Z0088, Z0166: Brandt level 1 vs ES counts (coincidence only at p = 97); lambda(p) <= 3 confirmed to 3*10^4.
- Z0091: Gaussian cone search in a bounded box; element-wise reading is trivial, collective reading gives only real solutions.
- Z0191, Z0209, Z0218: literature (none found), fixed-n local densities, idoneal test (0 of 1559 M-values idoneal).
