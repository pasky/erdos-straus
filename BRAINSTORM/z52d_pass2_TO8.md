# z52d Pass 2 — batch TO8 (100 'touched' items, never worked in Pass 1)

**Summary (lint-fix round).** Outcomes: nothing 71, covered 14, interesting 15, needs-compute 0, skipped 0. Lint (scripts/z52d_pass2_lint.py): 0 flagged of 100.
Interesting: Z2935 (level-failure sets for t≤64; n≤2·10⁴ with all levels 3..64 failing; rescues at t=98, 364), Z2941 (failures of (★) concentrate at large least non-residue ℓ(p)), Z2952 (23% of failing levels combinatorial, not subgroup-obstructed), Z2966 (congruence certificates cover 13/24 hard classes mod 840 at every 840k), Z2984 (Z[√2]-solutions of the (★)-form exist at 409, 577 where Z has none; parity forced even), Z2997 (ad−pc=1 count ≍ T log T, leading constant ≈2), Z2998 / Z3148 (Tseng's range covers depth p^{1−o(1)} for one closed horocycle of length p; normalisation to be checked), Z3040/Z3065 (periodic covering of 15·2^s+1 misses 1,3,6,13,843,1573), Z3044 (empirical ε≈0.105 for R/M_BM at p≤10⁵), Z3066 (ℓ-share larger when −p is a QR mod ℓ, 10/10 ℓ), Z3069 (odd non-squares ≤3·10⁴ failing (★)∪b=1: 105, 4545), Z3109 (Var(R−M_BM)/E[R] ≈ 0.25 log p), Z3134 (I3-type exception sets: (2,1,1,0), (1,2,2,0) grow, others stable).
**Scope.** Every item now has a recorded step (computation, identity check, literature abstract, or argument) and no needs-compute remains. Several verdicts are argument-level (marked in the per-item summaries) and several computations are at p ≤ 10⁵ or 10⁶ rather than 10⁸. Literature checks used the arXiv API; Strömbergsson (Duke 2004) and Hensley were not found on arXiv.

## Interesting items (numbers and reproduction)

### Z2935
Premise check passes: t=28, N=141=3·47 has divisors {1,3,19,1} mod 28, so D⁻_28(141)=0 (scripts/z52d_p2_TO8_z2935.py). Subset-product criterion (−1 reachable as a sub-multiset product of prime factors mod t) agrees with D⁻_t>0 in 3000/3000 random cases (N<1.28·10⁶, t≤64). For n≤2·10⁴ the failure density of F_t={n:D⁻_t(tn+1)=0} rises from 0.27 (t=3) to 0.95 (t=64); pairwise joint/indep ratios have median 1.0007 but reach 1.45 for (t,t')=(3,5). Seven n≤2·10⁴ (126, 3136, 3250, 5922, 6150, 6336, 9090) fail R_t(n)=0 for every t∈[3,64] (level t=2 rescues five of them; R_98(6150)=2 and R_364(9090)=1 are the first rescues in the t-ordering, scripts/z52d_p2_TO8_z2935b.py).
- Evidence: scripts/z52d_p2_TO8_z2935.py, scripts/z52d_p2_TO8_z2935b.py, data/z52b/pass2/TO8/z2935_out.txt, data/z52b/pass2/TO8/z2935b_out.txt, METAPLECTIC_ES.md:54
- Next: Compute the least rescue level t(n) for all n≤10^5 with t up to a few thousand, and test whether it grows with n (a level-rescue law for the words tuv−u−v).

### Z2941
Among primes p≡1 (mod 24), p≤10⁶, (★)-failures concentrate at large least non-residue ℓ(p): 5 of the 9 failures ≤10⁶ have ℓ≥13 although those bins hold ≈12% of the class (ℓ=13: 3/606, ℓ=23: 2/67, ℓ∈{5,7,11}: 2/≈8800 (the 2 are 23929 and 329617); scripts/z52d_p2_TO8_Z2941_Z2947.py; out z2941_z2947_out.txt). Mean R(p)/log²p falls monotonically from 0.15 (ℓ=5) to 0.075 (ℓ=31), consistent with the Legendre-profile effect on M_BM. With 9 failures this is suggestive only (binomial tail ≈0.03).
- Evidence: scripts/z52d_p2_TO8_Z2941_Z2947.py, data/z52b/pass2/TO8/z2941_z2947_out.txt, BRAINSTORM/z45_siegel_dichotomy.md
- Next: Extend (★) and b=1 failure counts by ℓ(p) to p≤10⁸ restricted to ℓ(p)≥13 (feasible: the tool is O(p log p) per prime) to see whether the excess persists.

### Z2952
Checked, for p∈{9 (★)-failing primes ≤10⁶, 4 controls} and C≤100 (1300 pairs (p,C)): 1276 levels have L_C=0. For 980 of them −1 ∉ ⟨prime factors of 4Cp+1⟩ mod 4C (an algebraic/index obstruction, the same as the subgroup argument); for 296 (23%) −1 lies in the generated subgroup, so the failure is combinatorial (no subset of the prime factors multiplies to −1). Only 24 levels are nonempty (scripts/z52d_p2_TO8_Z2952_Z2957_Z2962.py; out z2952_2957_2962_out.txt). So a sizeable share of level failures is not explained by subgroup index, which is the part a subgroup/Kneser-type argument cannot reach.
- Evidence: scripts/z52d_p2_TO8_Z2952_Z2957_Z2962.py, data/z52b/pass2/TO8/z2952_2957_2962_out.txt, BRAINSTORM/z29_forced_level_characters.md
- Next: Repeat for C up to 10⁴ on p≤10⁶ and report the combinatorial share as a function of C (is it decreasing?).

### Z2966
Pure congruence certificates (class r mod M covered if some q=4uC−1 | M and r≡−u mod q; then every p≡r mod M has a (★)-certificate for p large; scripts/z52d_p2_TO8_Z2966.py; out z2966_out.txt) cover exactly 13 of the 24 hard classes mod 840 (and 26/48, 39/72, 52/96, 78/144 for M=1680…5040): the covered fraction is stuck at 54% as M grows. The 11 uncovered classes mod 840 are the 6 square classes {1,121,169,289,361,529} plus 5 non-square classes {241,337,409,457,577}; the latter contain (★)-failures 329617 (337), 409 and 23929 (409), 577 (577). So forced-congruence pushing to M=840m does not shrink the uncovered set; what remains is genuinely prime-dependent.
- Evidence: scripts/z52d_p2_TO8_Z2966.py, data/z52b/pass2/TO8/z2966_out.txt, data/z52b/pass2/TO8/R_all_1e6.txt
- Next: Check the 14-prime (★) census classes mod 840 against the 11 uncovered classes; if all 14 lie there, the non-square uncovered classes are the next target.

### Z2984
Totally positive solutions of the (★)-form 4uBC−u−B=p over Z[√2] with u,B,C ∈ Z[√2] (coefficients in a box |a|,|b|≤12 or ≤25): for p=409 and 577 (no rational solution, R=0) there are 4 at p=409 and 4 at p=577 (box 12); at box 25: 16 (p=1009), 20 (5569), 20 (9601), 24 (23929), and 16 (p=401, which also has rational solutions), e.g. u=3−2√2, B=4+2√2, C=52+26√2 for p=409 (checked: 4uBC−u−B=409). Non-rational counts are even in every case run: Galois conjugation and the swap u↔B are fixed-point-free on them when no rational solution exists, so the 'Galois parity' is forced to be even and carries no information. The substantive point: the Z[√2]-form has certificates at primes where the rational (★) has none.
- Evidence: scripts/z52d_p2_TO8_Z2984.py, data/z52b/pass2/TO8/z2984_out.txt
- Next: Test whether the K-solutions at 409 and 577 yield rational ES solutions for n=409 via x=Tr/Norm-type combinations.

### Z2997
Counted the rational-form case directly: for the isotropic ternary form Q=ad−pc with value 1, N_p(T)/T increases by a constant amount per factor 4 in T (slope per unit of ln T ≈ 2.00 for p=409, 577, 1009, 5569; ≈1.85 for p=13), i.e. N_p(T) ~ c_p·T log T rather than the T^{n−2}=T rate of the generic (non-degenerate) EMM/DRS ternary count. This is the expected log-divergence for an isotropic split ternary form; the constant ≈2 is the same for four different p, suggesting it is governed by the rational structure rather than by p (scripts/z52d_p2_TO8_Z2996.c, z2996_out.txt).
- Evidence: scripts/z52d_p2_TO8_Z2996.c, data/z52b/pass2/TO8/z2996_out.txt
- Next: Fetch EMM 1998 (arXiv search) to confirm the T log T regime for isotropic ternary forms and the leading constant.

### Z2998
Read the abstract of Tseng (Math. Z. 302 (2022), arXiv:2106.00836, verified via arXiv API): a closed horocycle of length ℓ equidistributes on the cusp neighbourhood shrinking at rate T^{−1} whenever T/ℓ→0 (segment condition max{T^{−1/6},(T/ℓ)^{1/2}}(T/ℓ)^{−δ}, which is trivial for the full closed horocycle). So the deepest reachable target for a closed horocycle of length p has measure ≈1/T with T=p^{1−o(1)}, i.e. measure p^{−1+o(1)}, and the expected number of visits is ℓ/T=p^{o(1)}. Kelmer (arXiv:1708.08953) treats logarithm laws/shrinking targets for discrete flows and does not give the closed-horocycle depth.
- Evidence: arXiv:2106.00836 (abstract via export.arxiv.org API), arXiv:1708.08953 (abstract), BRAINSTORM/bsA_hecke_cusp_excursions.md:35-36
- Next: Check bsA's target normalisation against Tseng's T and length ℓ; if they match, the ES-target depth p^{−1+ε} is inside Tseng's range.

### Z3040
Along n_s=15·2^s+1, the Type II divisor certificates are periodic in s for each fixed divisor d (the set of s with d | 4C n_s+1 is a union of classes mod ord_d(2)). Using C≤60, d≤20000 (d≡−1 mod 4C) the union covers all s in [1,2000] except {1,3,6,13,843,1573}; s=3 and s=6 give odd squares 121 and 961, forced uncovered by T1; enlarging d from 3000 to 20000 removes the misses 661, 783, 1948 (scripts/z52d_p2_TO8_Z3065.py; out z3065_out.txt, z3065_out_D20000.txt). The misses are sporadic, not a progression, so no periodic (Skolem–Mahler–Lech) obstruction is visible at this range.
- Evidence: scripts/z52d_p2_TO8_Z3065.py, data/z52b/pass2/TO8/z3065_out.txt, data/z52b/pass2/TO8/z3065_out_D20000.txt
- Next: Push d to 10⁶ for the surviving misses s=1,13,843,1573 and test whether they are covered only by larger d.

### Z3044
Computed M_BM(p) and X_BM(p)=R(p)−M_BM(p) for all 4783 primes p≡1 (mod 4), p≤10⁵ (scripts/z52d_p2_TO8_mbm.c; out mbm_le1e5.txt; R* from the genus-split form equals R(p) on the test primes). X/M_BM reaches −1 exactly at the (★)-failures (5569, 9601, 23929, 83449); among the non-failing primes the smallest tail ratio R/M_BM is 0.105 (p=98017), then 0.117 (77617). So the empirical ε in H⁻_BM(ε,p₀) at p≤10⁵ is about 0.1, attained by ordinary primes, not by a special family.
- Evidence: scripts/z52d_p2_TO8_mbm.c, data/z52b/pass2/TO8/mbm_le1e5.txt, BM_CORRECTED_COUNT.md:168-172
- Next: Track the minimal R/M_BM over windows up to 10⁶ (about 10× the cost) to see whether the minimum stays near 0.1.

### Z3065
Same computation as Z3040 (scripts/z52d_p2_TO8_Z3065.py): for n_s=15·2^s+1 and C≤60, the divisor certificates d≡−1 (mod 4C), d|4C n_s+1 with d≤3000 leave 9 misses in [1,2000] ({1,3,6,13,661,783,843,1573,1948}); with d≤20000 the misses are {1,3,6,13,843,1573}. The misses 3 and 6 are odd squares (121=11², 961=31²), so T1 forces no Type II certificate there; the rest are not a single progression. Any covering proof would need d beyond 20000 or Type I witnesses.
- Evidence: data/z52b/pass2/TO8/z3065_out.txt, data/z52b/pass2/TO8/z3065_out_D20000.txt
- Next: Test whether the misses 843 and 1573 are covered by Type I witnesses.

### Z3066
Restricted counts R_ℓ(p)=#{(u,C): (4uC−1)|(p+u), ℓ|(4uC−1)} for ℓ∈{11,…,43}, p≡1 (4), p≤10⁵ (scripts/z52d_p2_TO8_lev.c mode ellr). Splitting-condition restriction fails as a positive-density route: R_ℓ=0 for 23–53% of primes with (p/ℓ)=−1 (ℓ=11,13,17). The share R_ℓ/R is larger when −p is a quadratic residue mod ℓ for all 10 tested ℓ (e.g. ℓ=23: 0.075 vs 0.019; ℓ=17: 0.070 vs 0.037), a reciprocity-type asymmetry that is not explained by the (p/ℓ)-sign alone (the sign flips with ℓ mod 4).
- Evidence: data/z52b/pass2/TO8/ellr_*.txt, scripts/z52d_p2_TO8_lev.c, data/z52b/pass2/TO8/primes_le1e5.txt
- Next: Check whether the share ratio equals the expected share under the M_BM pair weights, with the same ℓ.

### Z3069
Over odd non-squares 3≤n≤3·10⁴ (14913 values) the union of the two Type II families (★) and b=1 (R(n)>0 or B1(n)>0) fails at exactly n∈{105, 4545} (scripts/z52d_p2_TO8_lev.c; R_odd_nonsq.txt, B1_odd_nonsq.txt). 105 is in the known U(n) exception list; 4545=3²·5·101 is not, so either a Type I witness exists for 4545 (not checked) or the restricted union is weaker than the Pell-shaped conjecture.
- Evidence: data/z52b/pass2/TO8/R_odd_nonsq.txt, data/z52b/pass2/TO8/B1_odd_nonsq.txt, CONTEXT.md (U(n) exception list)
- Next: Search Type I solutions for 4545 (or the full ES solution) to decide whether the restricted union is the only gap.

### Z3109
Variance-to-mean of R(p)−M_BM(p) over windows: Var/E[R] = 1.79 (10³–10⁴), 2.23 (10⁴–3·10⁴), 2.57 (3·10⁴–10⁵), i.e. over-dispersed relative to a Poisson-type model and growing with p roughly like 0.25·log p (data scripts/z52d_p2_TO8_mbm.c; analysis inline). If the growth persists the fluctuation is not quasi-independent in the level variable. The model-free value is not a proof of the trend.
- Evidence: data/z52b/pass2/TO8/mbm_le1e5.txt, BM_CORRECTED_COUNT.md
- Next: Compute Var/E for windows at 10⁶ and 10⁷ (M_BM code is O(p log p) per prime) to test the log p trend.

### Z3134
Exception sets E(a,b,c,d)={n≤N: n≠a·tuv−bu−cv+d for all t,u,v≥3} for eight small tuples (scripts/z52d_p2_TO8_Z3134.py; out at N=3000 and 20000). Stable-looking (finite-type): (1,1,1,0): 112 exceptions ≤2·10⁴, the count grows only from 105 (N=3000) to 112, last exceptions 5110, 5850, 6336, 7966, 8430, 19600; (1,2,1,0) and (1,1,2,0): 50 exceptions, largest 815; (1,1,3,0): 54, largest 1720. Apparently growing (suggests infinitely many or a positive-density tail): (2,1,1,0): 519→755 (density 0.007 in the top third), (1,2,2,0): 279→568. No residue class mod 3,4,5,6,8,12 carries the tail for (2,1,1,0) or (1,2,2,0).
- Evidence: scripts/z52d_p2_TO8_Z3134.py, data/z52b/pass2/TO8/Z3134_out_3000.txt, data/z52b/pass2/TO8/Z3134_out_20000.txt
- Next: Sieve (1,1,1,0) to 2.5·10⁶ to test the I3 cutoff, and push (2,1,1,0), (1,2,2,0) to 10⁶ to decide growth.

### Z3148
Effective equidistribution scale vs cusp depth, using the verified Tseng result (arXiv:2106.00836, abstract checked; see Z2998): for a closed horocycle of length ℓ=p, equidistribution holds in the cusp region of measure ≈1/T whenever T=o(p), so a target of measure p^{−1+ε} (the ES₅ target scale quoted in BRAINSTORM/bsA_hecke_cusp_excursions.md:35–36) lies inside the range T=p^{1−ε}. The 'B2 depth gap' stated there therefore does not survive for a single closed horocycle of length p, provided the normalisations match. The expected number of visits is ℓ/T=p^{ε}. Strömbergsson's rate (Duke 2004) was not located on arXiv, so the subsegment statement is not checked.
- Evidence: arXiv:2106.00836 (abstract), BRAINSTORM/bsA_hecke_cusp_excursions.md:35-36, BRAINSTORM/bsA_hecke_cusp_excursions.md:36
- Next: Read bsA's ES target definition and verify the length convention before using Tseng's range.

## Tools
`scripts/z52d_p2_TO8_lev.c` (modes all, list, b1, par200, ellr), `scripts/z52d_p2_TO8_mbm.c` (M_BM, M0, R*), `scripts/z52d_p2_TO8_Z2996.c`, `scripts/z52d_p2_TO8_Z3185.c`; Python scripts `scripts/z52d_p2_TO8_*.py`. Outputs in `data/z52b/pass2/TO8/`.
