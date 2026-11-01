# z52d Pass 2 — batch TO5 (101 touched items, never worked in Pass 1)

ES is OPEN; nothing here proves or disproves ES. Labels: EVIDENCE = numerics; Assessment = judgement; PROVED items are cited, not re-proved.

**Summary (5 lines).**
1. Outcomes (101 lines in `data/z52b/pass2/outcome_TO5.jsonl`): nothing 93, interesting 6, covered 2, needs-compute 0, skipped 0.
2. Covered: Z1808 (|T|=o(M0), BM_CORRECTED_COUNT §2), Z1926 (B=1 slice criterion, B1_LINE.md; verified on all 39175 primes ≡1 (4) ≤10^6).
3. Interesting: Z1821/Z1822 (prime-modulus slices: uncovered fraction ~ L^{-1/2}; Σ τ/ℓ ~ ½ log L, not log²), Z1725 (Janson exponent only polynomial in box size), Z1687 (CF-period/regulator association with R/M), Z1802 (hard primes cluster in class 409 mod 840 and the all-QR Legendre cell), Z1827 (small-factor bias of random slice models), Z1927 (shift-slice failures positively correlated, ×3.7).
4. Many items were handled analytically only (see `not_done` per line); 'nothing' with 'Assessment' is used where the step was a reasoning check.
5. Data: `data/z52b/pass2/TO5/` (mbm_1e6, certs2_1e6, hardest_100, nsq_mbm_4e6, controls; 4.6 MB). Scripts: `scripts/z52d_p2_TO5_*`.

## Reproduction
- `scripts/z38_mbm.c` (existing): `./z38_mbm 3 1000000 0 > data/z52b/pass2/TO5/mbm_1e6.txt` (R*, M0, M_BM for primes).
- `scripts/z52d_p2_TO5_certs.c`: `gcc -O2 -o certs2 scripts/z52d_p2_TO5_certs.c -lm; ./certs2 5 1000000 > certs2_1e6.txt 2> certs2_1e6_hist.txt`.
- `scripts/z52d_p2_TO5_pmb.c`: `gcc -O2 -o pmb scripts/z52d_p2_TO5_pmb.c -lm; ./pmb < primes.txt` (same definitions as z38_mbm; validated on 1134241, a known failure).
- Python: `scripts/z52d_p2_TO5_{analyze,hard,hecke,janson,misc,slices,semiprime_bias}.py`; outcomes via `scripts/z52d_p2_TO5_outcomes.py`.

## Interesting items

### Z1821 / Z1822 — prime-modulus certificate slices
Identities (checked in `certs.c`): with C=(p+u+B)/(4uB), d := 4uC−1 = (p+u)/B and e := 4BC−1 = (p+B)/u, d·e = 4Cp+1, d≡e≡−1 (mod 4C).
A certificate with d = ℓ prime exists iff ℓ | 4Cp+1 with 4C | ℓ+1 and p ≡ −(4C)^{-1} (mod ℓ). Numbers over p≡1 (mod 4), p≤10^6 (39175 primes):
- P(∃ prime-d certificate with d ≤ L): 0.50 (L=3), 0.83 (31), 0.90 (101), 0.97 (1001), 0.990 (10^4).
- Uncovered fraction ~ L^{-0.50} (log–log slope −0.50 on [10^3,10^5], −0.52 on [10^5,10^6]).
- Σ_{ℓ≤L, ℓ≡3(4)} τ((ℓ+1)/4)/ℓ = 2.58, 3.89, 5.24 at L = 10^3, 10^4, 10^5 — i.e. ≈ ½ log L. The premise "matches log²" is false; the L^{-1/2} decay is what ½ log L predicts under CRT independence.
- Share of prime-d certificates: 47% (p<10^3) → 25% (10^5–10^6), so prime d does not dominate.
Next: check the L^{-1/2} law at p ≤ 10^7 and whether the uncovered primes are the (★)-failure-like set.

### Z1725 — Janson lower tail in the random-residue model
Events A_(u,B): p ≡ −(u+B) (mod 4uB), box 4uB ≤ X, P(A∧A') = 1/lcm if compatible. μ = Σ 1/φ(4uB); Δ = Σ_{dependent pairs} P(A∧A').
X=200: μ=3.71, Δ/μ=1.8; X=2000: μ=8.13, Δ/μ=3.2; X=16000: μ=13.55, Δ/μ=5.0.
Janson exponent μ²/(2 D̄) = μ/(2(1+Δ/μ)) ≈ 0.145 log X for large X, so the bound is X^{-0.14}, not exp(−μ). Reason: all moduli share the factor 4, so dependence is dense and Δ/μ ∝ log X. Model-level only.

### Z1802 — hard primes and residue classes mod 840
Hard set H = {p≡1 (4), p≤10^6, R/M_BM < 0.25}, |H| = 105 (includes the 9 (★)-failures).
χ² over the 97 classes mod 840 = 660 (96 df). Class 409 mod 840: 13 hard primes (expected 1.1); at R/M<0.5: 71 (expected 11.6).
Legendre cells (3/p),(5/p),(7/p): all-QR (+,+,+) 50/105 (base rate 12.4%); (+,+,−) 22; (+,−,+) 21; (+,−,−) 8; (−,−,+) 4; all other cells 0.
Interpretation (not verified): residual character dependence beyond BM. Next: M_gen residuals and mod-2520 classes.

### Z1827 — calibration of random slice models
For squarefree semiprimes N = 4Cm+1 the success rate (a factor ≡ −1 mod 4C) is below 1/φ(4C) by ratios 0.3–0.6 for φ(4C) ≥ 8. Restricting to balanced factorisations (both factors > N^{1/3}) moves the ratio to 0.8–1.2 (C=6: 0.121 vs 0.125; C=13: 0.035 vs 0.042; C=21: 0.049 vs 0.042; C=24: 0.031 vs 0.031). The deficit is small-factor bias; it appears equally for all odd m, so it is not a prime-p effect. Random-element models for slices must condition on balanced factors.

### Z1927 — iterated Landau–Ramanujan
Shift slices (p+B has a divisor ≡ −1 mod 4B), p≡1 (4), p≤10^6: success B=1 0.872, B=2 0.800, B=3 0.560, B=4 0.465, B=5 0.450, B=6 0.504 (B≥3 without gcd filter, approximate).
Joint failure of B=1..6 is 0.00605 versus 0.00164 from the product of marginals: ratio 3.7. Shift-slice failures are positively correlated.

### Z1687 — CF period (regulator) and R/M
Over 4783 primes ≡1 (4), p≤10^5: corr(log period of √p, R/M) = −0.12; partial correlation given log p = −0.069. Period is always odd (N(ε) = −1). Probably the regulator/L(1,χ_p) effect documented in BM_LVALUE.md; not separated (needs h_p and L(1,χ_p)).

## Covered items (for the record)
- Z1808: |T(p)| = o(L²) is proved in BM_CORRECTED_COUNT.md §2 (Thm 2.2 proof). Data: sup T/M0 = 0.53 (p=73), 0.44, 0.39, 0.35 on successive decades.
- Z1926: B1_LINE.md (b=1 line) gives the criterion (p+1)/2 has a prime factor ≡ 3 (mod 4); verified on all 39175 primes.

## Notes on checks that failed
- Z1916 premise false: for failure slices, −1 lies in the subgroup generated by prime-factor classes in 50/270 slices (18.5%), though never as a subproduct.
- Z1742/Z1703: greedy 4/p has 3-term expansions for ~half of p≤10^5 (trivial structure); Farey adjacency of unit fractions needs consecutive denominators.
- Z1770: the pair form needs no factoring; the premise that certificate search needs factoring is false for it.
- Z1845/Z1846 (near-squares m²+k): offsets have mixed signs across k after own-cell control; no robust family effect. Same-range control (200 primes in (10^6,4·10^6]) mean 1.150.
