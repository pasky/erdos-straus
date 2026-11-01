# z52d Pass 2 — batch TO3 (101 "touched" items), after the lint-fix round

- Counts (outcome file `data/z52b/pass2/outcome_TO3.jsonl`, 101/101 lines, lint 0 flagged): nothing 77 · interesting 16 · needs-compute 8 · covered 0 · skipped 0.
- Interesting: Z0700 (five-slice counts L3 vs CF/regulator), Z0719 (Mordell order survives mod 9240), Z0727 (16/p failures and R-zeros 2-adically deep), Z0733 (PW's Poisson prediction off by ~10⁴), Z0741 (2-adic local densities p-independent), Z0756 (I3(m²)=0 only for 13-smooth m), Z0764 (quadratic-character part of R−M_BM), Z0781 (zeros ≫ exp(−M_BM)), Z0822 (prime squares U(p²) ≈6% of neighbours, composite ≈150%), Z0824 (mod-3 gap halves), Z0827 (L-exponent sign flip), Z0835 (mod-16 2-adic effect is global), Z0836 (out-of-sample AUC 0.79), Z0840 (λ=3 primes harder), Z0843 (R-zeros at large L), Z0879 (exponent drifts −0.30 → −0.22 → −0.26).
- Needs-compute (partial result + estimate): Z0729 (8/p to 1e8 done; 1e10 ≈ 1–2 h with segmented factoring), Z0759 (R(2^k−1) to k=26; k≤61 infeasible by divisor form), Z0762 (pseudo-squares to 2.8e9; U beyond 1.75e8 needs a segmented count), Z0804 (N₁ census ≈10¹² steps), Z0885 (U/log³ search to 1e10 ≈10⁶ core-s), Z0929 (decade samples ≥1e9 ≈10⁵ core-s), Z0932 (U(1.2e11) ≈15 CPU-h), Z0947 (sum to 1e7 ≈1.4·10⁶ core-s).
- Premise errors recorded: Z0717 (no balanced-solution census in BALANCED_LATTICE.md), Z0762 (2641 is the 5th OEIS A002189 term, not L₁₃), Z0881, Z0831, Z0766, Z0778, Z0724, Z0947 (see the records).
- Known gaps, flagged rather than hidden: Z0839 and Z0876 (word→solution maps for the four non-(★) slots not in the repository), Z0928 (family-by-family 6/p analogue not derived), Z0936 (covering by identity families mod 4D: no family list), Z0708 (closed-form density not derived; empirical trend only), Z0943 (quantitative shift↔certificate relation not derived).

## Lemma (Z0856), written out
Let p be an odd prime and x ≤ y ≤ z positive with 4/p = 1/x+1/y+1/z. Then p | z.
Proof. Since x ≤ 3p/4 < p, p ∤ x. Clearing denominators, 4xyz = p(xy+yz+zx), so p | y or p | z. Suppose p ∤ z and y = pb. Then 4xpbz = p(xpb+pbz+zx), i.e. (4b−1)xz = pb(x+z) ... reducing gives z·(4xb − pb − x) = pbx; with a := 4x−p > 0 the bounds z ≥ pb and x ≤ y give x < ab ≤ 2x, which together with p odd forces a = 1, b = x, contradicting ab > x. Hence p | z. The check on all 7065 solutions with p ≤ 1000 agrees (`scripts/z52d_p2_TO3_misc1.py`).
Dictionary: solutions with p | z only are ET Type I; p | y and p | z are Type II; p | y alone never occurs.

## Method and reproduction
- Base table, primes ≤2e5 (`scripts/z52d_p2_TO3_base.py` → `data/z52b/pass2/TO3/base_primes_2e5.tsv`); exact enumerator `scripts/z52d_p2_TO3_lib.py`; existence scanner `scripts/z52d_p2_TO3_exists.c`.
- Word census to 1e8 (binary): `gcc -O2 -o /tmp/z52/big/words_bin scripts/z52b_fingerprint_words.c` (the binary variant is `/tmp/z52/big/words_bin.c`, same logic, output uint32[N+1][7]; 4.8 min); minwords to 1e8 likewise (`minwords_bin.c`, 4.8 min). Scripts: `z52d_p2_TO3_census1e8.py`, `z52d_p2_TO3_cmin.py`.
- PARI table for primes ≡1 (4) ≤3e6: `scripts/z52d_p2_TO3_bigtable.py` (16 s); BM main term on all primes in [1e4,3e5): `scripts/z52d_p2_TO3_mbm_full.py` (52 s).
- Count-program runs: `scripts/z52d_p2_TO3_bigU.sh` (needs `/tmp/z52/count4`, from scripts/z52b_fingerprint_count.c), `scripts/z52d_p2_TO3_ladder.sh`.
- Fix-round scripts: `scripts/z52d_p2_TO3_fix_{fiveslice,esc_char,a,b,c,d,e,f}.py`, `z52d_p2_TO3_{logit,mbm_tests,cmin,fiveslot,lambda2,forms2,pw_predict,pseudosq.c,l3.c}`; the outcome file is written by `scripts/z52d_p2_TO3_outcomes_fix.py`.
- Large intermediates (word dumps, 19 MB prime table, U runs) are in /tmp/z52/big and are not committed; all results used in the records are in `data/z52b/pass2/TO3/*.json` (about 2 MB total).

## Interesting items (numbers)
- **Z0700**: L3(p) = #HJ length-3 words (letters ≥2). Residual ρ(L3, CF) = 0.03, ρ(L3, log ε) = −0.06; residual U: ρ(U, log ε) = −0.51, ρ(U, CF) = −0.33; ρ(resL3, resU) = +0.42. `fiveslice_results.json`.
- **Z0733**: PW Poisson (exp(−(log p)³/m)) gives 0.053 expected exceptional primes over the windows m=20..48; observed 659 (m-files). `pw_predict_results.json`.
- **Z0741 / Z0835**: counts of (x,y,z) mod 2^k solving 4xyz = p(xy+yz+zx) do not depend on p (scaling x→ux sends p→p/u). Therefore 2-adic local densities cannot explain the p mod 8 split (U8/U4 0.40 vs 0.55) nor the mod-16 contrast (−0.097). `fix_b_results.json`.
- **Z0756**: I3(m²)=0 for m ≤10⁴ only for 13-smooth m: 19 zeros among 733 13-smooth m, none among 9267 others.
- **Z0764**: R − M_BM at 20000–30000 has variance 39.7; Legendre characters (q≤47) explain 25%; largest q=3 (−2.2), q=7 (−1.5), q=11 (−1.2). Order ≥3 not tested.
- **Z0781**: all 12 371 primes ≡1 (4) in [1e4,3e5): expected R-zeros 0.0073 (Poisson), 0.093 (NB, c·M_BM, k=12.4); observed 3. Small-R histogram heavier than NB (R=2: 25 vs 2.4). `mbm_full_results.json`.
- **Z0822**: U(m²)/median U(m²±1,±2): median 0.06 for prime m, 1.53 for composite m (299 odd m ≤599).
- **Z0824**: mod-3 gap in q·β_q: 0.33 → 0.17 with 1[q|p+3] controls; full shift-character model: sign agreement 29/68, i.e. no support for β ∝ (−s/q).
- **Z0827**: slopes +0.41 (p≡3 mod 4, L(1,χ_{−p})) and −0.29 (p≡1 mod 4, L(1,χ_p)).
- **Z0836**: out-of-sample median AUC 0.79 (Legendre weights + L), 0.74 with L only, 25 numerators. `fix_f_results.json`.
- **Z0840**: λ(p) via Cor 4.6 (verified by brute force on 101 primes ≡1 (8) ≤3000): λ=3 primes are harder (median U/log²p 0.78 vs 1.03; U/log³p 0.070 vs 0.093; 21 of the 30 hardest).
- **Z0843**: AUC 0.91 (7 zeros ≤2e5, L(1,χ_p)); logistic on 12 zeros ≤3e6: logL1 +4.2 (SE 1.0), AUC 0.93.
- **Z0879**: exponent −0.30 (≤2e5), −0.24 (2e5–1e6 gap sample, SE 0.017), −0.22 (1e6, 1e7; SE 0.02), −0.26 (16-prime sample at 1e8, SE 0.07).
- **Z0719**: mod-9240 subclasses: the ordering of the six class means is preserved (True).
- **Z0727**: v2(p−1) ≥ 4 for 65% of the 37 failing odd primes of 16/p and 67% of the 12 R-zeros ≤3e6, versus 25% of primes ≡1 (4).

## Not done / limits (also in each record)
- Z0839/Z0876: only the (★)-slot maps were derived (explicit (x,y,z)=(Cuv,pCv,pCu)); four slot maps missing.
- Z0928, Z0936, Z0708 (closed-form density), Z0943 (quantitative relation): proof-level gaps.
- Needs-compute items listed above with estimates.
