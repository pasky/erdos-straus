# z52b pass 1 — batch U00 (complete: 207 items; WAIT, not merged)

- Outcomes (207): covered 96, skipped 81, needs-compute 25, nothing 5, interesting 0. Records: data/z52b/pass1/outcome_U00.jsonl.
- Nothing: Z0845 (Carmichael ratio, 10 numbers), Z1476 (parity of U(p): 791 even / 820 odd), Z1503 (near-squares m²+24k, noise), Z3051 (U(p³) at four primes), Z0144 (pronic/triangular denominators: none found for 147 primes p ≡ 1 (4) ≤ 2000).
- Interesting: none. Checked and found covered: Z0354 (square-residue count D(p): R² +0.126 over prime characters, but +0.004 after 2-adic and class-of-one indicators); Z1513 (every C-form divisor a ≡ −1 mod 4C of 4Cp+1 is a QNR mod p, 1966/1966 cases, Jacobi proof, = y4_t1_numerators Prop 1); Z0682 (U=5 absent to 30000, = fingerprint-0007).
- Needs-compute (25, each with the computation spelled out in its record): Z0687, Z0772, Z0844, Z0850, Z0852, Z0877, Z0930, Z0938, Z0945, Z1392, Z1524, Z1529, Z1619, Z1627, Z1715, Z2375, Z2624, Z2630, Z2642, Z2796, Z3189, Z0012, Z0047, Z0127, Z0133. Several need words_3e6 / minwords_3e6, which is absent from the data tree (regenerate with scripts/z52b_fingerprint_minwords.c).
- Caveat: a large share of `covered` verdicts are citations to existing memos/data (the z52b lanes were already run), not new computations. Skipped items are mostly vague (no defined statistic or no ES target), not refuted.

## Computations run in this pass (all on data/z52b/raw/f4_all_30000.txt; col 0 = n, col 1 = U(n))

- `scripts/z52b_p1_U00_batch1.py` → `data/z52b/pass1/U00/batch1.json`: Z0682 (count of U=5 is 0), Z0845 (10 Carmichael ≤ 3·10⁴, ratio median 3.8), Z0718 (mod-840 class means; six square classes are the six lowest: 1: 0.431, 361: 0.443, 121: 0.461, 169: 0.495, 529: 0.509, 289: 0.527; top: 557: 1.70, 277: 1.48), Z0354 (D(p) vs U: Spearman −0.37).
- `scripts/z52b_p1_U00_Z0354_reg.py` → `data/z52b/pass1/U00/Z0354_reg.json`: regression of log(U+1) on log p, log log p, (q/p) for q < 80: R² 0.685; + D(p): 0.811; + divisors of p−1 ≤ 1000: 0.756 (+D: 0.832, gain 0.076); + 2-adic and 1[p ≡ 1 mod m] (m ≤ 32, and 3..25): 0.841 (+D: 0.845, gain 0.004). The D-gain is therefore the 2-adic / class-of-one effect of H00 Z0199.
- `scripts/z52b_p1_U00_batch2.py` → `data/z52b/pass1/U00/batch2.json`: Z1513 (1966 C-form divisors, p < 3000, C ≤ 300, all (a/p) = −1), Z1476 (parity), Z3051 (U(p), U(p³) for p = 5, 13, 17, 29: 2,4,4,7 and 57,212,258,298), Z1503 (near-squares 0.94–1.76 vs 1.80 overall), Z0190 (pronic / triangular: none for 147 primes ≤ 2000; search bounded by z ≤ ~9·10⁶; the sparse-set count explains it, not a structural claim).

## Reproduce
`uv run --with numpy --with scipy --with sympy python scripts/z52b_p1_U00_batch1.py` (and the other two scripts). Inputs read from the main checkout's untracked data/z52b/raw/ (f4_all_30000.txt, lcm19_U.txt).
