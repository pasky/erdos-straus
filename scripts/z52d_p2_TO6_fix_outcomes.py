"""z52d pass2 TO6 lint-fix: replace the 25 flagged outcome lines in data/z52b/pass2/outcome_TO6.jsonl with records whose
summaries report executed steps. Other lines are kept unchanged. One line per mid."""
import json
F='data/z52b/pass2/outcome_TO6.jsonl'
TM='data/z52b/pass2/TO6/'
NEW={}
def rec(mid, outcome, summary, evidence, not_done, nxt):
    NEW[mid]=dict(mid=mid, outcome=outcome, summary=summary, evidence=evidence, not_done=not_done, next=nxt, prev_outcome='none')

rec('Z2021','interesting',
 "Tested the independence (Poisson-type) model of witness absence on the Type-I line data: for all primes p≡1 (mod 4) ≤ 2·10⁵ (8,977), the empirical probability that no line t ≤ 63 (K=16), t ≤ 127 (K=32) has a witness is 0.00078 and 0.00022, i.e. 0.40 and 0.41 times the product ∏(1−π_t) of the single-line densities (0.00196, 0.00054). Witness counts have variance 5.92 against 4.93 under independence (positive correlation between lines). For K=64 the model predicts 1.5 absences and 0 are observed. So the independence heuristic overstates the tail of failures at the level of line unions, and a Granville-type sieved correction must produce a factor ≈ 0.4 at this scale; the R(p)-level fit P(R=0 | M) itself was not made (R(p) ≥ 2 throughout the range, so there are no zeros to fit).",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json', 'data/z52b/pass2/TO6/witmask_p1mod4_2e5.txt'],
 'Did not fit a sieved Granville-type model with explicit constants; the R(p)-level P(R=0|M) fit was not performed (no zero events exist in the computed range).',
 'Fit the 0.4 factor against a sieved model (sieve over small primes ℓ with the Legendre-type densities) and test at p ≤ 10⁶.')

rec('Z2056','nothing',
 "Wrote the rational parametrisation of the ES surface from the fibre over x: with a = 4x−n, b = nx and t = u/v, y = nx(u+v)/(v·a), z = nx(u+v)/(u·a) (sympy: 1/x+1/y+1/z−4/n = 0 and 4xyz−n(xy+yz+zx) = 0 identically). It is birational to the surface, so the ES surface is rational; the fibres over x are conics (a y−b)(a z−b) = b². Integrality census (Z2302) shows only 22 of the 24 positive ordered integer solutions of 4/13 are reached in the box u,v ≤ 200, x ≤ 200, so the integrality conditions are sparse in this parametrisation.",
 ['scripts/z52d_p2_TO6_fix_param.py'],
 'The integrality conditions were not translated into a closed divisibility criterion beyond v·a | nx(u+v) and u·a | nx(u+v); the 2 missing solutions were not located.',
 'Locate the 2 missing solutions of 4/13 (larger u or x) and state the full divisibility criterion in (x,u,v).')

rec('Z2062','nothing',
 "Genus-character test on the class structure: R(p) class means over the 96 classes mod 840 with p≡1 mod 4 (p ≤ 10⁵) are explained by the 32 real (order ≤ 2) characters of (Z/840)^* with R² = 0.84 (rank 16 on these classes), against a shuffle-null of 0.16 (95th percentile 0.27). The genus-type (real) part therefore carries most of the class-level variance. The largest single coefficients are on the character (a=2,3 mod 8 part) and on the mod-5 and mod-3 quadratic characters. No separate 2-rank computation of class groups was needed: for p≡1 (mod 4) the genus characters of Q(√−4p) are these Legendre-type characters.",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json'],
 'Class-group 2-ranks of Q(√−p·small) for D ≠ −4p not computed; the decomposition was done on R(p), not on X(p)/M_gen(p) as defined in SINGLE_P_COUNT.',
 'Repeat the regression for X(p)=R(p)−M_gen with M_gen the genus-character average once the repo definition is pinned.')

rec('Z2071','nothing',
 "Compared R(p) with the Legendre singular-series product S(p) = ∏_{3≤ℓ≤100} (1 − (p/ℓ)/(ℓ−1)) over the 4,783 primes p≡1 (mod 4) ≤ 10⁵. Correlation of log S(p) with log(R(p)/log²p) is 0.42 and with the class mean is 0.50, but after dividing R(p) by its mod-840 class mean the correlation falls to 0.02. The Bateman–Horn-type product therefore carries no information beyond the class mod 840 (it is a function of the same Legendre symbols).",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json'],
 'Exact Bateman–Horn constant for the ES count was not derived; M_BM was not recomputed; only the correlation against a product of the same symbols was tested.',
 'None needed unless a non-Legendre (e.g. Kronecker of −4uB) product is tested.')

rec('Z2095','nothing',
 "Retrieved the statement from Graham's own survey (UCSD ronspubs, 'Paul Erdős and Egyptian fractions'): for all m ≥ 78 there is a set of distinct integers x_k with Σ 1/x_k = 1 and Σ x_k = m, and this fails for m = 77. Exact DFS search (pruned by the reciprocal-mass bound) reproduces this: no set for m = 70, 72, 77; sets exist for 78, 79, 80 (e.g. {2,6,8,10,12,40} for 78). This is a distinct-denominator, sum-of-denominators problem with a variable number of terms; its congruence structure does not transfer to the fixed-three-term, numerator-4 ES problem, and no residue identity was compared.",
 ['scripts/z52d_p2_TO6_fix_graham.py', 'https://mathweb.ucsd.edu/~ronspubs/13_03_Egyptian.pdf'],
 'Congruence decomposition of Graham’s construction not extracted (the survey gives only the statement); no transfer attempted.',
 'None: the problem class differs (variable term count, distinct denominators).')

rec('Z2107','nothing',
 "Character decomposition of the residue indicator on the class group of p≡1 (mod 4) mod 840: the real characters (order ≤ 2; 32 of them, rank 16 on the 96 classes) explain R² = 0.84 of the class-mean variance against a shuffle-null of 0.16 (95th percentile 0.27); the trivial character explains 0 (mean-centred). The nonreal characters cannot be separated at this sample size, since the remaining 80 characters would absorb the residual (the saturated fit has R² = 1 with 96 parameters on 96 classes), so the 'real main term dominates non-real' comparison requires more primes per class.",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json'],
 'Non-real character contribution not estimated (sample too small: ~50 primes per class).',
 'Run the class decomposition on p ≤ 10⁶ (about 500 primes per class) to estimate the non-real part with a noise floor.')

rec('Z2122','nothing',
 "Read Hales (arXiv:2410.05030) Theorem 1.1: the modified Lenstra algorithm works for K = Q(√d), d ∈ {−1,−2,−3,−7,−11} (Euclidean imaginary quadratic fields, including Z[i]) with divisors d = Sx + r, x ∈ O_K, in O(log|N|) operations when |S|³ > |N|. Applied to the ES Type-I integer tp+1 with S = t, the Gaussian version has the same threshold t³ > tp+1 (t ≳ √p) as the integer version, so it gives no new regime for integer witnesses; its possible gain (Gaussian divisors of tp+1 in classes mod t) was not examined.",
 ['arXiv:2410.05030 (full text, Theorem 1.1, Remark 1.2)', 'scripts/z52d_p2_TO6_lenstra_regime.c'],
 'No Gaussian-integer implementation run; the question whether Gaussian divisors add witnesses beyond the integer ones was not tested.',
 'Implement Theorem 1.1 for Z[i] on tp+1 with S = t for p ≤ 10⁴ and compare with the integer witness set.')

rec('Z2125','nothing',
 "Enumerated the F_5[T] analogue of 4/P = 1/X+1/Y+1/Z (equivalently 4XYZ = P(XY+YZ+ZX)) with X,Y,Z nonzero of degree ≤ 2. Nondegenerate solutions (no vanishing subsum) exist for P of degree 1 (e.g. 4/(T+2) = 1/T + 1/(T+3T²) + 1/(2T), checked in sympy over F_5(T)), but only 4 ordered ones for P = T²+2, T²+4T... degree 2 within the search bound. Monic-denominator solutions (degree ≤ 3, monic P of degree 1, 2) do not exist, consistent with BRAINSTORM/ff_erdos_straus.md Prop 1.2. The ordering-based and sign-change steps of the integer argument have no direct analogue here; the degree bound is an assumption of the search, so counts are lower bounds.",
 ['scripts/z52d_p2_TO6_fix_dfi.py', 'scripts/z52d_p2_TO6_fix_fqmonic.py', 'data/z52b/pass2/TO6/fq_monic_TO6.json', 'BRAINSTORM/ff_erdos_straus.md §Prop 1.2'],
 'Degree bound 2 for X,Y,Z only; no proof of the non-existence of monic solutions beyond degree 3; the ES divisor-class analogue over F_5[T] not written out.',
 'Extend the search to deg ≤ 4 for deg P = 2 and check whether nondegenerate solutions persist.')

rec('Z2132','nothing',
 "Verified the continuant/matrix form of the ES word: M(u)M(t)M(v) with M(k) = [[k,−1],[1,0]] has det 1 and (0,0)-entry tuv − u − v (sympy). For primes 5 ≤ p < 2000, p≡1 (mod 4) (147 primes): words (t,u,v ≥ 2) with tuv−u−v = p exist for 146 primes (median 24 words up to reversal, max 50; p = 5 has none), and 146/146 of these have a word with a coordinate in 4ℤ ∪ (8ℤ−p). So the record's prescribed-entry congruence test is nonempty for every computed prime except p=5.",
 ['scripts/z52d_p2_TO6_fix_words.py', 'data/z52b/pass2/TO6/words_TO6.json'],
 'Only primes below 2000 were checked (the word enumeration is O(p log p) per prime); the matrix identity is verified in sympy but not stored in the JSON (the search there returned None because its form was wrong).',
 'Extend the congruence check to primes ≤ 10⁵ with a sieve-based word enumeration.')

rec('Z2267','nothing',
 "Normalised the same SL₂-type words: M(u)M(t)M(v) ∈ SL₂(ℤ) (det 1) and the transpose/reversal symmetry (t,u,v) ↦ (v,u,t) identifies words in pairs; for 147 primes 5 ≤ p < 2000 ≡ 1 (mod 4) the canonical word count (up to reversal) has median 24, min 0 (p=5), max 50. The word problem is thus not a bijection with primes: each prime carries a finite set of canonical words of prescribed (0,0)-entry, and the normalisation removes only the reversal, not the other redundancies.",
 ['scripts/z52d_p2_TO6_fix_words.py', 'data/z52b/pass2/TO6/words_TO6.json'],
 'Other normalisations (cyclic shifts, sign changes of entries) were not tested; SL₂ conjugacy classes of the product were not counted.',
 'Count SL₂(ℤ)-conjugacy classes of the words for hard primes.')

rec('Z2276','nothing',
 "Equidistribution test of the Type-I witness lines over squarefree moduli: for 8,977 primes p ≡ 1 (mod 4) ≤ 2·10⁵, the line densities are far from equidistributed over the classes mod 105 (49 classes, χ² = 972 for t=3, 3023 for t=7, 1563 for t=11 on 48 degrees of freedom) and mod 1155 (481 classes, χ² = 1647, 3341, 1813 on 480 dof). Densities range from 0.61 to 1.0 at t=3 mod 105, i.e. whole classes are fully witnessed. The 'orbit' is therefore not equidistributed mod squarefree moduli at the level of single lines, consistent with the Legendre (reciprocity) structure of the classes.",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json', 'data/z52b/pass2/TO6/class_determinacy_TO6.json'],
 'The Apollonian-type sieve dimension and the Bourgain–Kontorovich expansion step were not analysed (abstract-level reading only).',
 'Replace the class test by a test of equidistribution after removing the mod-840 classes (only 13% of witnesses are unexplained by class mod 840 at t=3).')

rec('Z2302','nothing',
 "Rational versus integral census on the ES cubic: using the rational parametrisation (Z2056) with x integer and t = u/v, the integrality condition is v·a | nx(u+v) and u·a | nx(u+v). For p = 13, 17, 29 the box u,v ≤ 60, x ≤ 400 contains 874,591, 872,388 and 865,779 rational parameter points, of which 18, 16 and 22 give integral positive solutions; for p=13 the box u,v ≤ 200, x ≤ 200 gives 22 of the 24 positive ordered integer solutions. Integral points are therefore a density ≈ 2·10⁻⁵ subset of the rational parameter points in this box, so rational points do not in practice produce integral ones.",
 ['scripts/z52d_p2_TO6_fix_param.py'],
 'The density of integral points as the box grows was not measured beyond these boxes; the 2 missing solutions of 4/13 were not located.',
 'Measure the integral density in shells of (x, max(u,v)).')

rec('Z2310','nothing',
 "Real-character (Kronecker/Legendre) part of the R(p) class structure: the 32 real characters of (Z/840)^* explain R² = 0.84 of the class-mean variance (null 0.16; see Z2062/Z2107). The Kronecker-character term for p≡1 mod 4 is therefore the dominant structure of the class means; the cancellation of nonreal characters on average is not resolved by this sample (see Z2107).",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json'],
 'Non-real cancellation not measured; the explicit Kronecker term for the count was not written as a formula.',
 'Repeat with p ≤ 10⁶ to measure non-real contributions (see Z2107).')

rec('Z2327','nothing',
 "Literature check: a search for quaternion-order treatments of ES found no such reformulation; the closest ES paper (arXiv:2206.10319, classification of solutions of the form (du,dv,duv) and of coinciding coordinates) contains no quaternion content (text checked for the word). No quaternion lattice was written down, so the comparison is not performed.",
 ['web search (quaternion order ES)', 'arXiv:2206.10319 (abstract and full-text grep)'],
 'No quaternion order or norm form computed; the claim of a geometric parametrisation of split-prime classes is untested.',
 'Only pursue if a norm form for Lemma 1.1 (tp+1 = mm″) is identified.')

rec('Z2337','nothing',
 "Genus/one-sided test: the real-character decomposition (see Z2062) accounts for R² = 0.84 of the class structure. For the one-sided pointwise count, R(p) ≥ 2 for every computed prime (min 2 at p=5; min 4 for p ≥ 13 up to 10⁵), so the one-sided positivity is exact in range and the 'forced vs expected' question is answered for the computed range only.",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json', 'data/z52b/pass2/TO6/R_primes_1e5.txt'],
 'Local densities per prime class against a predicted main term were not computed; positivity beyond 10⁵ untested.',
 'Compare the class-mean main term with the genus average for p ≤ 10⁶.')

rec('Z2346','nothing',
 "Verified numerically Kronecker's double-series identity, the building block of the theta-quotient/Appell–Lerch form used in METAPLECTIC_ES.md (K1′): Σ_n x^n/(1−yqⁿ) = (q;q)²(xy;q)(q/(xy);q)/[(x;q)(q/x;q)(y;q)(q/y;q)] agrees to 10⁻³⁰ at three parameter points (q, x, y) = (0.3, 0.5, 0.7), (0.2, 0.45, 0.31), (0.1, −0.4, 0.6). The specific (K1′) normalisation (β_t closed form, the completion, and the support of the nonholomorphic part on squares) was not checked.",
 ['scripts/z52d_p2_TO6_fix_kronecker.py', 'METAPLECTIC_ES.md §(K1′)'],
 'Zwegers completion and the support on squares (T1) not computed; β_t closed form not verified.',
 'Verify the (K1′) coefficient identity for t=3 by expanding the boundary series in q with X specialised as in the memo.')

rec('Z2357','interesting',
 "Phase diagram of the union of the first k witness lines (t = 3, 7, …, 4k−1) on the 8,977 primes p≡1 (mod 4) ≤ 2·10⁵: the number of primes with no witness in those lines is F_1 = 2140, F_4 = 123, F_8 = 33, F_16 = 7, F_32 = 2, and F_43 = 0 (lines up to t = 171). A fit of log F_k over F_k ≥ 20 gives slope −0.49 per line, so the failure count decays geometrically in the number of lines and no prime in the range needs a line beyond t = 171. This is the measured 'transition' the item asks for (finite-range; the decay rate is the heuristic input).",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json', 'data/z52b/pass2/TO6/witmask_p1mod4_2e5.txt'],
 'Only p ≤ 2·10⁵ and lines to t = 255 (64 lines) computed; the X = 10⁶..10⁹ range was not reached; the failure rate for (★) as a whole was not separated from single lines.',
 'Extend the witness bitmask to p ≤ 10⁶ (about 40k primes) and fit the same slope to test stability.')

rec('Z2359','nothing',
 "Depth of p/4 in the Stern–Brocot tree (the sum of the regular continued-fraction quotients) for the 4,783 primes p≡1 (mod 4) ≤ 10⁵: the depth is ~p/4 (median ratio depth/p = 0.25; min 5, max 25,001). So the tree depth is unbounded, not bounded as the item hopes. The regular continued fraction of p/4 is [⌊p/4⌋; 4] and has length 2 trivially, so the record's 'continued-fraction length λ(p) ≤ 3' must refer to a different (negative or restricted) expansion, which the record does not define; the ES₅ tree of FOREST_CONNECTIVITY.md was not reconstructed.",
 ['scripts/z52d_p2_TO6_fix_dfi.py', 'data/z52b/pass2/TO6/dfi_depth_fq_TO6.json'],
 'The ES₅ move set was not reconstructed; a bounded-depth tree for ES was not searched.',
 'Ask for the definition of λ(p) in FOREST_CONNECTIVITY.md before any further test.')

rec('Z2369','nothing',
 "Large values of the witness count: among primes p≡1 (mod 4) ≤ 10⁵ the largest R(p)/log²p are at p = 80077 (R = 397, ratio 3.11), 72797 (352), 76157 (343), 49277 (309), and the top ten all lie in classes mod 840 that are not Mordell square classes (classes 277, 557, 517, 437 mod 840). So the Linnik-type large values sit in the non-hard classes, the opposite of the hard-class deficit; the exact-formula (r₄-type) decomposition was not written.",
 ['scripts/z52d_p2_TO6_fix_chars.py', 'data/z52b/pass2/TO6/chars_TO6.json'],
 'No theta-quotient decomposition of the ES count was computed; the r₄ comparison was only stated.',
 'Check whether the large-value classes are those with all real characters = +1 for small primes.')

rec('Z2374','nothing',
 "Small-prime covering test: for a sample of 2,000 primes p≡1 (mod 4) and t ∈ {3,…,63} (16 lines), every prime has some prime q ≤ (log p)² with q | tp+1 and q ≡ −1 (mod t). The condition is the witness condition restated with a small prime cofactor, so the 100% rate says the small-prime divisor exists for every computed prime, not that it gives a witness (q itself is never divisible by 4, so the cofactor condition must still be checked).",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json'],
 'Joint condition with the cofactor (4 | m and m ≡ −1 mod t) not checked for the small-prime divisors; (q,C) pair counts not tabulated.',
 'Check whether the small-prime divisor q (with cofactor tp+1)/q also satisfies the Type-I congruences.')

rec('Z2376','nothing',
 "Multi-line 'at least m events' statistic for the witness lines (the shape Maynard–Tao weights need): among the first 16 lines, the fraction of primes with at least m witnessed lines is 0.9992, 0.9855, 0.9123, 0.5036, 0.039 for m = 1,2,3,5,8; the independence (Poisson-binomial) prediction is 0.998, 0.979, 0.905, 0.505, 0.042. Among 32 lines the empirical and independent values agree to about 0.01 (m=5: 0.734 vs 0.742). So the at-least-m tail matches independence at this scale, and no obstruction to a Maynard-type first/second moment bound is visible in the data.",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json'],
 'The Maynard–Tao weight ratio itself was not computed (events are divisibility, not primality; admissibility of a reformulated family not checked).',
 'Compute the MT ratio on the 32-line data after writing the events as admissible linear-form primality questions, if a reformulation exists.')

rec('Z2377','nothing',
 "Same witness-line data as Z2376: for 32 lines the at-least-m fractions (m = 1, 2, 3, 5, 8: 0.9998, 0.9942, 0.9641, 0.7334, 0.1954) match the independent prediction (0.9995, 0.9935, 0.9655, 0.7423, 0.1900), so 'dense clusters' of certificate events occur at the rate independence predicts. The Maynard dense-cluster statement needs prime events, which the certificate events are not.",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'data/z52b/pass2/TO6/witness_stats_TO6.json'],
 'Maynard’s dense-cluster theorem not applied; no reformulation of the certificate family as prime events was found or tested.',
 'None unless a prime-event reformulation is found.')

rec('Z2396','nothing',
 "Joint distribution of the root ν/f of ν² ≡ −12 (mod f) against f mod 12 for the 12,970 primes f < 3·10⁵ with a root: the root ν/f falls in the ten bins with densities 0.20 each (bins 0–4 only, as ν ≤ f/2 by symmetry), and the two residue classes f ≡ 1, 7 (mod 12) occur with 6,467 and 6,503 primes. The joint χ² = 2.49 on 9 degrees of freedom: no detectable correlation between the root position and f mod 12 at this size.",
 ['scripts/z52d_p2_TO6_fix_dfi.py', 'data/z52b/pass2/TO6/dfi_depth_fq_TO6.json'],
 'Other D = 4c²d (c, d ≠ 1) not tested; the uniform-in-f statement of Duke–Friedlander–Iwaniec was not verified beyond this single D.',
 'Repeat for D = 4·4·3 and D = 4·25·7.')

rec('Z2398','nothing',
 "Analysis of the first lemma: the ES Type-I count is Σ_t Σ_{m≡−1 (t)} 1[m | tp+1] with 4 | m. Expanding 1[m | tp+1] additively gives phases e(a(tp+1)/m), which are linear in p and t, not the inverse-type fractions e(a m̄/n) of the Bettin–Chandee bilinear form (arXiv:1502.00769 abstract: bounds for Σ α_m β_n ν_a e(a m̄/n) with arbitrary coefficients, improving Duke–Friedlander–Iwaniec). The BC sums are averaged over moduli, so they give statements over ranges of p, not for the fixed prime p of the ES witness; the reduction to an inverse-type phase would need a change of variables that I did not find.",
 ['arXiv:1502.00769 (abstract read via API)', 'derivation in this record'],
 'No Fourier-analytic bound or numerical test of the phase identity; the change of variables was not attempted in detail.',
 'Check whether substituting m'' = (tp+1)/m gives an inverse-type fraction in a modulus that varies with p.')

rec('Z2409','nothing',
 "Pretentiousness test of the witness lines: the largest |correlation| of each line's witness indicator with a real character (d/p), d ∈ {2,3,5,7,11,13,−3,−7,−11,−15,−19,−23}, over the first 3000 primes p≡1 (mod 4) is 0.58 for t=3 (with (2/p)), 0.35 for t=7, 0.39 for t=11, 0.31 for t=19 and ≤ 0.27 for other lines. The t=3 value is explained by p mod 8: every prime p≡5 (mod 8) has a t=3 witness (rate 1.0), while p≡1 (mod 8) has rate 0.52. So the 'pretending' is a mod-8 class effect, and the residual within p≡1 (mod 8) (≈0.52 rate) is the only part left for a pretentious analysis, which was not carried out.",
 ['scripts/z52d_p2_TO6_fix_witness_stats.py', 'scripts/z52d_p2_TO6_fix_classdet.py', 'data/z52b/pass2/TO6/class_determinacy_TO6.json'],
 'Pretentious distance of the residual (within p≡1 mod 8) not computed; no characters of conductor > 40 tested.',
 'Test the residual witness indicator on p ≡ 1 (mod 8) against characters of conductor ≤ 100.')

# ---- replace flagged lines
lines=[json.loads(l) for l in open(F)]
out=[]; n_rep=0
for r in lines:
    if r['mid'] in NEW:
        out.append(NEW[r['mid']]); n_rep+=1
    else:
        out.append(r)
assert n_rep==len(NEW)==25, (n_rep,len(NEW))
open(F,'w').write('\n'.join(json.dumps(r, ensure_ascii=False) for r in out)+'\n')
print('replaced', n_rep)
