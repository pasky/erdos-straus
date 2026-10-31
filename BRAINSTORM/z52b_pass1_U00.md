# z52b pass 1 — batch U00 (fix pass applied; 207 items; WAIT, not merged)

- Outcomes (207): covered 103, nothing 68, interesting 2, skipped 13 (all restatement or meta, rule 3), needs-compute 21 (each: >30 min compute or >1 h coding/design, stated). Records: data/z52b/pass1/outcome_U00.jsonl.
- Interesting Z1610: the primes with no C-form witness (C ≤ 200) below 2·10⁴ (409, 577, 5569, 9601) and all 14 R-zero primes ≤ 1.2·10⁷ (no (★) word) are ≡ 1 (mod 24); independence predicts (1/4)^14 ≈ 4·10⁻⁹. No repo memo states this. Next: is p ≡ 1 (mod 24) necessary for (★)-zeros, tested on the other classes to ≥ 10⁸?
- Interesting Z1492: C-form witness counts grow ≈ 1/3 as fast as the uniform-divisor heuristic from C = 100 to 1000 (134 vs 408 over 30 primes near 10⁶; median S/E 0.72 → 0.59; 6 of 30 primes gain nothing). Next: QNR-restricted model vs size effect, on 10³ primes.
- Corrections found in this pass: the apparent C-form closure (P(W_2C|W_C) ≈ 2.4×, Z1475) and the e-slice correlations (Z0351, joint ratios up to 2.3) are artefacts (pooling; p mod 24 class effects). Z0852's product-model deviation is the p ≡ 2 (mod 3) effect (witness a = 3).
- Nothing-level checks that changed a prior verdict: Z0772 (joint zeros = odd squares ∪ {105}), Z0938/Z0945 (A396825 containment holds for the Uv-zeros; R-zeros are not contained, 12 of 31 outside), Z0713 (k1, k2 prefixes verified for n = 2..14; not in OEIS).

## Reproduction
- Minwords census: `gcc -O2 -o minwords scripts/z52b_fingerprint_minwords.c && ./minwords 12000000 > /tmp/u00/minwords_12e6.txt` (≈ 30 s; the file is not committed, ~150 MB). Interior variant: `scripts/z52b_p1_U00_fix_minwords.c`, output `/tmp/u00/minint_12e6.txt`. A396825 b-file: `curl https://oeis.org/A396825/b396825.txt`.
- Scripts (uv run; numpy, sympy, cypari2): `scripts/z52b_p1_U00_{batch1,batch2,Z0354_reg,solver,fix_words,fix_cform,fix_cform2,fix3,fix4,fix5,fix6,fix7,fix8,fix9,fix_solver,fix_solver2}.py`. Results are in `data/z52b/pass1/U00/*.json`.
- Solver: `scripts/z52b_p1_U00_solver.py` (exact enumeration of all solutions of 4/n with x ≤ y ≤ z, via the divisors of b² with b = nx).
- Caveats: a fair share of `covered` verdicts still cite existing memos (not re-derived). Some proxies were chosen by me where the item text was underspecified; each record names its proxy in the summary.
