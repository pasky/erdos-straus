# z52d Pass 2 — batch SK2 (86 items; skipped/covered/nothing re-verification of Pass-1 verdicts)

ES is OPEN. Nothing here proves or disproves ES; all numbers are EVIDENCE/CERTIFIED computations as labelled.

**Summary (5 lines).**
1. Outcomes (86 input lines, 86 output lines in `data/z52b/pass2/outcome_SK2.jsonl`): nothing 48, skipped 28, covered 8, interesting 2, needs-compute 0.
2. Interesting: **Z1415** (exact C_min to 10⁸: record 41027 at p = 85664329, interior minimiser (u,B) = (18,29); 14 primes with no certificate) and **Z1545** (the (★) count is not concentrated on small C: 42 % from C ≤ 20, but 72 % from min(u,B) ≤ 20, spread over scales).
3. Pass-1 verdicts corrected: Z1932 (Descartes is quadratic in curvatures; the premise was false), Z1767 and Z1955 and Z1480 (cited sibling entries, not depth documents), Z1663 and Z1967 now exact.
4. Skipped (28) are outreach/organisational only (e-mails, MO/forum posts, prizes, GPU/crowd plans, tagging/process docs). Covered (8): Z1318, Z1319, Z1430, Z1509, Z1514, Z1684, Z1862, Z1992.
5. Not done (explicit): Webb/Li table, Browning–Elsholtz parametrisation, Nagell per-case table, Sylvester-wave formula, Coppersmith small-root test, percolation graph on C, adaptive query rule, all-solution enumeration for p ≡ 3 (mod 4).

Reproduce: `scripts/z52d_p2_SK2_cmin.c` (census to 10⁸, cap 3000) + `scripts/z52d_p2_SK2_starcmin.c` (exact C_min for the capped stragglers) + `scripts/z52d_p2_SK2_profile.c` (exact R_C(p) for all C; `profile 10000000 4 k 0`); statistics in `scripts/z52d_p2_SK2_stats.py`; checks in `scripts/z52d_p2_SK2_slices.py`, `..._valuation.py`, `..._checks2.py`. Summary numbers in `data/z52b/pass2/SK2/*.json`.

## Method notes (used across items)

* **Exact (★)/C-form counts.** R_C(p) = #{(u,B) ≥ 1 : 4CuB − u − B = p} = #{d | 4Cp+1 : d ≡ −1 (mod 4C)} (the map is d = 4Cu − 1, cofactor 4CB − 1). Every solution has min(u,B) ≤ √p + 2 (if u ≤ B: 4uB ≤ p + 2B; if B ≥ √p then u ≤ √p/4 + 1, else u ≤ B < √p). So enumerating u ≤ √p and divisors D of p + u with D ≡ −1 (mod 4u) gives all solutions with C = (D+1)/(4u), B = (p+u)/D, with no cap.
* **Checks.** The cap-3000 census agrees with the Pass-1 U05 program on all primes ≤ 10⁵ with C ≤ 300 (4776 winners each). The exact profile agrees with brute-force divisor counting on all 51 primes p ≡ 1 (mod 4) ≤ 600. Its C-form zeros are exactly the known exceptions 409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281 (14 primes, all ≤ 10⁸, consistent with the 14 failures quoted in B1_LINE.md).
* **Compute caps.** Census to 10⁸ ≈ 5 s on one core; profile to 10⁷ ≈ 110 s on 4 cores. Well inside the 30 min / 4-core cap.

## Interesting items

### Z1415 — is C_min bounded? (exact to 10⁸)

* Census of all 2,880,504 primes p ≡ 1 (mod 4) ≤ 10⁸ (C-form, exact; the 7 primes with C_min > 3000 resolved by the uncapped enumerator). C_min distribution: P(=1) = 0.789, P(≤2) = 0.932, P(≤5) = 0.986, P(≤10) = 0.9957, P(≤100) = 0.99992; quantiles 50/90/99/99.9 % = 1/2/6/21.
* Record sequence (p, C_min) up to 10⁸: (4357, 39), (4789, 40), (19141, 141), (26209, 149), (60217, 251), (98017, 557), (184837, 23105), (85664329, **41027**). Pass-1 fingerprint #180 stated "records to 23105"; that was the range ≤ 3·10⁶ only.
* 184837 has minimiser (u,B) = (1,2): a boundary case (4·23105·2 − 3 = 184837). 85664329 has minimiser (18,29), interior: 4·41027·18·29 − 47 = 85664329. So the record tail is not only boundary families.
* Primes with C_min > 3000 (≤ 10⁸), exact values: 184837 → 23105, 434437 → 3879, 706801 → 4016, 11814001 → 8636, 20445289 → 13106, 28175101 → 4163, 85664329 → 41027 (`data/z52b/pass2/SK2/stats.json`, key `stragglers_exact_gt3000`). Primes with no C-form certificate at all: 14 (≤ 8813281), the same set at 10⁷ and 10⁸.
* Interpretation: C_min is unbounded in range, with heavy but rare tail; the Pass-1 fingerprint's record ceiling was an artefact of the range.
* **Next:** run the exact enumerator (`z52d_p2_SK2_starcmin.c`, O(√p) per prime) on 10⁸–10⁹ windows to see whether later records are interior or boundary.

### Z1545 — is the (★) count explained by small parameters?

* Exact R(p) = Σ_C R_C(p) for p ≡ 1 (mod 4), 10⁵ < p < 10⁷ (327,397 primes).
* Mean share of R from C ≤ 2: 20 %; C ≤ 20: 42 %; C ≤ 500: 69 %.
* Mean share from min(u,B) ≤ 1: 24 %; ≤ 2: 35 %; ≤ 5: 51 %; ≤ 20: 72 %.
* Regression of log R on log R_{C≤20}: R² = 0.49 (slope 0.54); on log R_{C≤2}: R² = 0.18 (slope 0.22).
* So the count is not concentrated on small C. The small-parameter notion that fits better is min(u,B), but even there each dyadic scale carries a roughly constant share, which looks like the Σ 1/φ(4m) weighting of M_BM (log-uniform in scale).
* **Next:** check whether the dyadic distribution of min(u,B) matches the Mertens-type weights of M_BM (BM_LVALUE.md). If it does, "small-parameter theory" cannot explain more than a fixed fraction of R.

## Notes on the nothing/covered verdicts that changed

* **Z1932 (sangaku):** Pass 1 said covered by Descartes. Descartes' theorem is quadratic in curvatures; the linear relation 1/r = Σ1/r_i that the item asks about does not hold for tangent circles in general, so the premise is false.
* **Z1767 (Coppersmith):** Pass 1 cited a sibling entry. The threshold 64C³ ≥ p is right; for p ≡ 1 (4) ≤ 10⁵, 4660 of 4783 primes have a certificate with C in [p^{1/3}/4, 500]. The small-root computation itself was not run.
* **Z1480 / Z1955:** Pass 1 cited sibling items, not depth documents. Recorded as nothing (identities only).
* **Z1663 and Z1967:** exact computations (isosceles set; two-term slice criterion). Z1967's x = p branch is dead on p ≡ 1 (mod 3) exactly (3/p solvable iff p ≡ 2 mod 3).
* **Z1310 / Z1311:** the (★) surface is smooth mod every odd q; N_1(a) = q² + 1 − q·[q | a]; P(v_q(u) ≥ j) = q^{2−j}/(q²+1) for j ≥ 1.
* **Z1308:** C = 1 count is R_1(p) = (τ(4p+1) − r₂(4p+1)/4)/2 (checked for 1125 primes). No p-adic family in p.
* **Z1757:** Einsiedler–Katok–Lindenstrauss (Annals 164 (2006)) proved the Littlewood exceptional set has Hausdorff dimension zero (arXiv math/0612721). The analogy with ES's exact divisibility condition gives no test.

## Not done (silent omissions made explicit)

* Z1641 Webb/Li historical table: web search returned no primary sources.
* Z1664 Browning–Elsholtz parametrisation: not fetched.
* Z1423 Nagell/Mordell per-case table: Banderier et al. read (formula for A₂(p) and length-3 parametrisation), per-case list not extracted.
* Z1993 Sylvester-wave double sum: not derived.
* Z1842 profinite closure test: not run (δ(X) data in z52b_dividing.md are related, not the same test).
* Z1335 percolation graph on C: not built (C_min histogram only).
* Z1404 adaptive query rule: not designed.
* Z1663 all-solution enumeration for p ≡ 3 (mod 4): not done (existence of repeats only).
* Z1405 ATP, Z1408 MCTS, Z1722 stat-mech Z(β), Z1800 meet-in-the-middle collisions, Z1811 Turán sieve, Z1801 picture: not run (reasons in the outcome file).
