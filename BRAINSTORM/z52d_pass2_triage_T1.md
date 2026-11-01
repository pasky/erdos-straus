# z52d Pass-2 triage of "interesting" items, shard T1 (52 items; Opus)

ES is OPEN; nothing here bears on it beyond calibration. Input `data/z52b/pass2/triage_input_T1.jsonl`; verdicts in
`data/z52b/pass2/triage_interesting_T1.json`; per-item notes (why + what was re-run) in `triage_notes_T1.jsonl`.
Re-runs were done in `/tmp/t1/*.py` (each ≤ 5 min, `ulimit -v 6e6`); their logic is described in the notes.

## Counts
REDISCOVERY 18 · EXPLAINED-BY 18 · ARTIFACT 6 · ARTIFACT/WEAK 7 · NEW-CALIBRATION 3 · NEW-STRUCTURAL 0 · DEPTH 0.
So 49 of the 52 "interesting" labels dissolve. Pass-1's triage list has none of these mids.

## NEW-CALIBRATION (real, new, no proof role)
- **Z0651** least certificate-family size s(p) for hard-class primes in [1e8,1e9): the median is still 22, the 99% quantile is
  197–230 per block, and the record is 3092 at 393858721. This extends z52b_dividing #311 (< 1e8). Re-run on [3.93e8,3.94e8)
  reproduced it. Caveat: the Type I residues skip the f ≤ p/2 condition, so s is a lower bound.
- **Z0245** numerators m with 4 | m are under-represented among the 3-term-representable m/p. The overall share is 0.228
  (re-run), but about half of the gap is the m = 1, 2, 3 edge effect. Inside m-blocks [16,1024) the share is 0.230–0.237,
  a depletion of about 6% (≈3σ).
- **Z0836** a per-numerator main-term model (log L(1,χ_p) plus Legendre symbols q ≤ 47) ranks the failures of m/p out of
  sample. The median AUC over 25 numerators is 0.788 (re-run); log p alone gives 0.626 and adding L(1,χ_p) gives 0.741. So
  the BM_LVALUE/RESIDUE_HARDNESS predictors carry over to other numerators.

## ARTIFACT (the stated number does not survive)
- **Z0814** Proth primes: the "v2-matched" controls were drawn from [5e6,1e7], a size confound. With a mod-840 + v2
  regression, the residual is −0.25 for p < 1500 and +0.02 (z = 0.3) for p in [1500,1e5].
- **Z1999** Euler n²+n+41: controls were not size-matched. With size and class matching, p = 0.094; the repo's full-R
  comparison (Q05) has the opposite sign.
- **Z2925** "one-class genus" was tested by theta-equality, which counts isometric copies, not the genus. All 2/2/3/5
  classes at N = 11/19/23/47 are locally indistinguishable from G (representation counts mod 64 and mod N²).
- **Z0472** near-square enrichment of the R-zeros: near-square density is ≈ 10/√p. A size-matched baseline expects 1.36
  near-square zeros against 3 observed (P = 0.16).
- **Z1025** the "three-way composition" effect comes from C1 = 1, which makes C1·C2 = C2 automatic. With C1 ≥ 2,
  P(win C1C2 | both) = 0.021 vs 0.023 unconditionally.
- **Z3148** "B2 depth gap does not survive": this applies Tseng's cusp-neighbourhood theorem (abstract re-fetched) to the
  HJ-length-3 cylinder event at the discrete QNR points, which is a different target. The gap stands.

## EXPLAINED-BY: re-verified mechanisms worth remembering
- Z0961 ord_p(10): Spearman 0.128 → 0.006 after adding p mod 840, v2 and 1[q | p−1] controls (RESIDUE_HARDNESS). ord_p(3)
  drops 0.32 → −0.009 the same way.
- Z1035 anticorrelation of the divisor counts of 4p+1 and 8p+1: −0.224 → +0.017 after small-prime divisibility indicators,
  since each ℓ divides at most one of the two.
- Z2658 Σ_i d(L(p,A),i) = p·s(A,p) exactly (checked for all A at p = 37, 101). The QR/QNR split is the letter-sum term in
  DEDEKIND_ES (D2).
- Z3055 Gross–Zagier: all 270 prime factors of N(j(√−p)) are ≡ 2 (3). Primes of 3p−y² that are inert in both fields are
  already 64.5% ≡ 3 (4), against 68.5% for the actual factors.
- Z3066 every (★) modulus M has Jacobi (−p/M) = +1 (0 violations in 24410 certificates), and M = ℓ only when (−p/ℓ) = +1.
  This gives the R_ℓ asymmetry.
- Z2021 line failures are rarer than the product of marginals: 7 vs 14.1 after stratifying by p mod 840. This is the
  within-fibre negative association of EXSET_SHIFT_DIVISORS Thm 3.1.
- Others are explained by known factors: RESIDUE_HARDNESS (Z0727, Z0741, Z0764, Z1802, Z2614), BM_LVALUE Thm A (Z0700,
  Z0843, Z1687), T1 (Z0822), main-term geometry (Z1545), size/units (Z1827, Z2984).

## REDISCOVERY (repo location in notes)
Z0848 (EXSET_SHIFT_DIVISORS §3.2), Z1438 (Type I genus (−d/p) = −1), Z2782 (DEDEKIND_ES Cor 4.1), Z0269, Z0283/Z0521
(A400619, fingerprint #267), Z0511 (Q18; its "worst at 1201" is an argmax bug, the worst is 577), Z0566/Z2215 (PW Table 1),
Z0628/Z3109 (B1_LINE overdispersion), Z0681, Z0827, Z1605, Z1624, Z2367, Z2952, Z3044.
