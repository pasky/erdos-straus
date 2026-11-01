# z52d pass 2 — batch SK3 (85 items; SK = skipped or weakly-covered in Pass 1)

Summary (5 lines)
1. Outcomes over 85 input lines (one output line each, `data/z52b/pass2/outcome_SK3.jsonl`): nothing 82, interesting 1 (Z2003), skipped 2 (Z2005 board-round process item; Z2872 meta transfer table), covered 0, needs-compute 0.
2. Computed: Z2363 least (★) level sweep to 8.6·10⁷ (reproduces the 14 census failing primes exactly); Z2003 T/M₀ windows at 10⁵–10⁷; Z2148 smoothness control; Z2139 SL₂ unipotent orbit (0 of 100,197 moves); Z2240 boundary strata (13.1%); Z2317 independence check; Z2912 square-sum check; Z2135 parity rules (arXiv:2003.13229 full text).
3. Interesting: Z2003 — a finite-size caveat on BM_LVALUE's constant 0.1402 (p≡1 mod 8), see §Z2003 below.
4. Honest scope: about 60 items are analysis or assessment only (no compute; a short identity or argument is written in the record, labelled as such). Items whose step needs an undefined object (families, maps, r(·) in S₃(p), Thm K series) are `nothing` with the missing definition named in `not_done`.
5. All 16 Pass-1 `covered` verdicts were downgraded: their citations were idea lists (BRAINSTORM/z52b_*.md, ES_CONNECTIONS_TODO) or abstracts without the item's step. No Pass-2 `covered` was issued (none met rule 4).

## Z2003 — interesting: finite-size status of the p≡1 (mod 8) constant

Definitions (FRONTIER §2.2): 𝒫(p) = {(u,B): gcd(u,B)=1, u+B odd, 4uB−u−B ≤ p}, M₀(p)=Σ1/φ(4uB), T(p)=Σ(−uB/p)/φ(4uB), M_BM = M₀ − T.

Results (primes p ≡ 1 mod 4, all primes in each window):

| window | primes | worst T/M₀ | mean T/M₀ | min M_BM/log²p (≡1 mod 8) | frac of ≡1(8) primes with M_BM/log²p < 0.1402 | min (≡5 mod 8) |
|---|---|---|---|---|---|---|
| [10⁵, 1.1·10⁵] | 422 | +0.338 (p=102001) | 0.026 | 0.0985 | 0.435 | 0.149 |
| [10⁶, 1.01·10⁶] | 390 | +0.308 (p=1007161) | 0.018 | 0.1034 | 0.318 | 0.150 |
| [10⁷, 1.001·10⁷] | 282 | +0.242 (p=10008769) | 0.015 | 0.1137 | 0.230 | 0.150 |

- The worst case of T/M₀ shrinks with p, and T concentrates on uB ≤ √p (Tm/M₀ ≤ 0.015 in the printed samples).
- BM_LVALUE Thm A states M_BM(p) ≥ 0.1402 log²p at p≡1 (mod 8) (via T ≈ (σ/4)E·L(1,χ_p)² + O(p^{−1/16} log p)). The asymptotic is consistent with the data, but at p ≤ 10⁷ a large fraction of p≡1(8) primes sits below 0.1402. The error term p^{−1/16}log p is still of the order of T itself at these sizes.
- Not done: a re-derivation of Thm 2.2's constant by summation by parts (analysis), a fit of the deficit against p^{−1/16}log p.

Reproduce: `gcc -O2 -o z52d_tm0 scripts/z52d_p2_SK3_TM0.c -lm && ./z52d_tm0 1000000 1010000 1` (output: `data/z52b/pass2/SK3/Z2003_TM0_windows.txt`).

## Other numerical records used in the outcomes

- Z2363 (`scripts/z52d_p2_SK3_cmin.c`, `data/z52b/pass2/SK3/Z2363_cmin_8.6e7_C1e6.txt`): Cmin histogram by decade; P(Cmin=1) 0.757→0.790 and P(Cmin≥10) 0.016→0.005 over 10⁴–10⁷; max Cmin 41027 at p=85664329; the 14 primes with no level ≤10⁶ are exactly the census list (409 … 8813281).
- Z2148 (`scripts/z52d_p2_SK3_smooth.py`): apparent smoothness effect (0.82 vs 0.46 for C≤3) vanishes after conditioning on τ(4Cp+1).
- Z2139 (`scripts/z52d_p2_SK3_sl2orbit.py`): 0 of 100,197 lower-unipotent moves land in ES-form SL₂ solutions.
- Z2240 (`scripts/z52d_p2_SK3_boundary.py`): at least level, 1174 of 8954 primes have only boundary witnesses.
- Z2317 (`scripts/z52d_p2_SK3_cover.py`): P(E_C) C≤12 measured; P(no level ≤12)=0.00745 vs 0.01077 under independence.
- Z2912/Z3020 (`scripts/z52d_p2_SK3_squares.py`): square-sum fractions are size/2-adic effects; union-indicator entropy 0.063 bits.
