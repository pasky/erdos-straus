# z52b pass 1 — batch H01 (25 items, Z0217–Z0391)

**Summary.** covered 15 · nothing 10 · interesting 0 · needs-compute 0 · skipped 0. Outcomes: `data/z52b/pass1/outcome_H01.jsonl`.
Covered: Z0217 Z0219 Z0220 Z0230 Z0234 Z0235 Z0236 Z0237 Z0239 Z0247 Z0248 Z0331 Z0359 Z0390 Z0391. Each was already handled by a cited memo.
Nothing: Z0221 Z0223 Z0226 Z0231 Z0240 Z0246 Z0253 Z0368 Z0379 Z0389. The steps were done; the notable observations are below.
The closest call: Ramanujan x²+y²+10z² exceptions vs (★) zeros at p ≡ 7 (8) overlap in {7, 31, 79, 2719}. The overlap is fully explained by small-prime Legendre symbols (§3).
ES remains OPEN; nothing here bears on a proof. Labels: EVIDENCE unless stated.

No item reached `interesting`. The observations below are kept so the computations can be reproduced and are not repeated.

## 1. Least certificate vs least non-residue (Z0230, Z0379) — EVIDENCE
`scripts/z52b_p1_H01_hmin_lnr.py 10000000` (8 s; data `data/z52b/pass1/H01/hmin_lnr_10000000.npz`). Here h_min is the
least Type II modulus, as in `s3_min_scale.py`, and l is the least prime non-residue. Primes p ≡ 1 (4) < 10⁷:
* p ≡ 1 (8): h_min ≥ l in 100 % of cases. Mordell: h_min = l for l ∈ {3, 7}. corr(log h_min, log l) = 0.88, and max h_min/l² = 8.6.
* Within a fixed l the max grows with p: l = 17 gives 335 (10⁶) → 2495 (10⁷); l = 2 (p ≡ 5 (8)) gives 419 → 791. So there is no h_min ≤ C·l^κ.

## 2. Fixed-modulus divisor-in-class density (Z0231) — EVIDENCE
`scripts/z52b_p1_H01_ford_resdiv.py 1e9` → `data/z52b/pass1/H01/ford_resdiv_1e9.txt`. F_m(x) is the fraction of n ≤ x,
n ≡ 1 (m), with no divisor d ≡ −1 (m), d ≤ √n. The local slope d log F/d log log x is −0.50 for m = 4 (Landau) and drifts
toward −1/2 for larger m: −0.43 (m = 8), −0.28 (24), −0.09 (100) at 10⁹. The law is Landau-type, (log x)^{−1/2}, set by the
kernel of an odd real character mod m; it is not Ford's interval law.

## 3. Ramanujan's form vs (★) zeros (Z0389) — EVIDENCE
`scripts/z52b_p1_H01_rstar_all.c` (R*(n) for all odd n), `scripts/z52b_p1_H01_ramanujan.py`, `…_ramanujan_partial.py`.
* A003585 (odd n ≠ x²+y²+10z²) primes ≡ 7 (8): {7, 31, 79, 223, 2719}. (★) zeros at p ≡ 7 (8) ≤ 10⁶: {7, 31, 79, 127, 199,
  2719, 8191, 861199}. Overlap {7, 31, 79, 2719}; the naive hypergeometric p-value on the 109 primes < 3000 is 1.3·10⁻⁵.
  At p ≡ 3 (8) the only overlap is {3}.
* For p ∈ (10⁴, 10⁶), r_Q(p)/√p and R(p)/log²p have Spearman 0.14 (7 mod 8) and 0.17 (3 mod 8). Regressing both on the
  symbols (q/p), q ≤ 50, kills the correlation (residual ρ ≈ −0.01; the symbols explain R² = 0.92 of r_Q and 0.17 of R). The
  common driver is "many small primes split": at 2719 the primes 5, 7, 11, 17, 19, 23, 29, 31 are all quadratic residues.

## 4. Thin-set test for hard primes (Z0253) — EVIDENCE
`scripts/z52b_p1_H01_rzeros.c 30000000` (6 s) reproduces exactly the 14 (★) zeros. `scripts/z52b_p1_H01_thin.py` then
compares hard primes (R ≤ r) with size-matched controls for p = m² + k, |k| ≤ K. The only excess is at |k| ≤ 16–64 (ratio
1.3–3.5 on 3–37 primes), which is THREE_SQUARES Lemma 1.4. There is no other polynomial clustering. Hard list:
`data/z52b/pass1/H01/R_le6_p1mod4_3e7.txt`.
