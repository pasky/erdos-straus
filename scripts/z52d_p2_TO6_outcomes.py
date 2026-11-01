"""z52d pass2 TO6: writes data/z52b/pass2/outcome_TO6.jsonl (one line per input record)."""
import json
D = 'data/z52b/pass2/'
SC = 'scripts/'
E_EG3 = ['scripts/z52d_p2_TO6_egypt3.c', 'data/z52b/pass2/TO6/egypt3_fail_k3-40_n60000.txt']
E_EG4 = ['scripts/z52d_p2_TO6_egypt4.py']
E_TM = ['scripts/z52d_p2_TO6_tmin.c', 'data/z52b/pass2/TO6/tmin_p1mod4_1e6.txt', 'scripts/z52d_p2_TO6_lenstra_regime.c', 'data/z52b/pass2/TO6/lenstra_regime_2e5.txt']
E_R = ['scripts/z52d_p2_TO6_egypt3.c', 'data/z52b/pass2/TO6/R_primes_1e5.txt', 'scripts/z52d_p2_TO6_analysis.py', 'scripts/z52d_p2_TO6_control.py', 'data/z52b/pass2/TO6/analysis_TO6.json', 'data/z52b/pass2/TO6/control_TO6.json']
E_Q = ['scripts/z52d_p2_TO6_quick.py', 'data/z52b/pass2/TO6/quick_checks.json']
E_SG = ['scripts/z52d_p2_TO6_signed.py']
E_SQ = ['scripts/z52d_p2_TO6_sqclass.py']
E_T12 = ['scripts/z52d_p2_TO6_typeI_II.py']
rows = []
def add(mid, outcome, summary, evidence, not_done, nxt=''):
    rows.append(dict(mid=mid, outcome=outcome, summary=summary, evidence=evidence, not_done=not_done, next=nxt, prev_outcome='none'))

add('Z1997','covered',
 "Function-field large-q existence is refuted by the repo's depth proof: BRAINSTORM/ff_erdos_straus.md Theorem 2.1 (PROVED): for fixed n,k the proportion of irreducible P of degree n with ES_q(A,P) tends to 0 as q→∞ (quoted: 'for fixed n and k the proportion ... tends to 0 as q → ∞'). So 'ES for every P once q ≫ deg P' is false in the repo's own setting; the monodromy computation was not needed.",
 ['BRAINSTORM/ff_erdos_straus.md §Theorem 2.1 (lines ~54-62)'],
 'Did not re-verify the Theorem 2.1 proof line by line; did not compute monodromy.', '')

add('Z2012','nothing',
 "Checked the proposed shape ('ES for all primes except those attached to one exceptional real character'): Tatuzawa/Siegel-type exceptional-character statements are ineffective, so they give no explicit list of possible exceptions, and an ineffective 'all but one' statement cannot be verified for a pointwise ES claim. No computation performed; Weinberger's idoneal-number claim was not checked against the primary source.",
 [], 'Did not verify Weinberger 1973 statement or trace Tatuzawa step; no character-sum test of M_BM.', 'Check Weinberger 1973 and whether an effective exceptional-discriminant bound exists.')

add('Z2013','nothing',
 "The C=1 case of T1 (square obstruction for 4xy−x−y) is already in the repo (T1_TEMPLATE.md); I did not read MathOverflow 364853 or enumerate the proved variants 'k·xy−x−y ≠ f(z)', so the variant list is not produced.",
 ['T1_TEMPLATE.md'], 'MO 364853 not read; variant list not built; no test of which variants correspond to ES slices.', 'Fetch MO 364853 and tabulate variants against the ES slice equations.')

add('Z2015','nothing',
 "Read the arXiv abstract of Shi–Shi–Whitehead (arXiv:2510.21702): quadratic invariants give reciprocity obstructions to the local-global conjecture in four further packings, with partial obstructions on curvature sets. The abstract states no general criterion for when reciprocity obstructions arise; the full text was not read, so no classification criterion was extracted and no ES word set was tested.",
 ['arXiv:2510.21702 (abstract read via export.arxiv.org API)'], 'Full paper not read; no general criterion extracted; ES transfer not attempted.', 'Read the full paper for the invariant construction and test whether ES words admit a comparable quadratic invariant.')

add('Z2016','nothing',
 "Measured, rather than implemented a lattice method: for all 39,175 primes p≡1 (mod 4) below 10⁶ the minimal Type-I slice parameter t_min (CONDITIONAL_ES §1, Lemma 1.1) satisfies t_min ≥ p^{1/4} for only 0.9% of primes and t_min ≥ √p for 5 primes, with median 3. So a Coppersmith-type search at C≈p^{1/4}–p^{1/2} would be needed for a small tail, but the typical witness is far smaller. The Coppersmith–Howgrave-Graham–Nagaraj method itself was not implemented.",
 E_TM, 'Coppersmith lattice (divisor-size hypotheses, LLL run) not implemented; no timing for p ~ 10^15.', 'Implement the lattice search on the 347 primes ≤10⁶ with t_min ≥ p^{1/4}.')

add('Z2019','nothing',
 "Analogy item; I did not write the 'what ES has that Cramér lacks' audit. The only quantitative fact produced in this batch is the witness-size distribution (median minimal Type-I parameter 3; Z2016/Z2123 data), which is the kind of structure the audit should cite.",
 E_TM, 'Audit paragraph not written; no Cramér-scale comparison computed.', 'Write the audit against CONDITIONAL_ES.md §7.3.')

add('Z2021','nothing',
 "Did not perform the sieved Poisson fit P(R=0 | M_BM) that the item asks for. Recorded that R(p) (sorted 3-term ES count) is ≥2 for every prime ≤10⁵ with small minimum (R(5)=2), so no R=0 event occurs in the computed range.",
 E_R, 'Granville-sieved model not fitted; M_BM not recomputed; only the R-distribution is available.', 'Fit log P(R(p)=k) against the BM main term with a sieved model.')

add('Z2023','nothing',
 "Least quadratic non-residue ℓ(p) against R(p) for 4,783 primes p≡1 (mod 4) up to 10⁵: Pearson corr(log ℓ, log R) = −0.48 overall and −0.41/−0.69/−0.66 in size bins, but after dividing R(p) by its mod-840 class mean the correlation is −0.015. The ℓ(p) effect is therefore fully carried by the Mordell square-class structure mod 840 (see Z2050). Note: ℓ(p) is undefined for squares n, so the 'square-class flip' of Z2103 has no direct analogue.",
 E_R, 'Did not test the explicit-Burgess version (see Z2417); correlation measured only up to 10⁵.', 'None: the residual test already shows no extra information beyond mod 840.')

add('Z2028','nothing',
 "Brute-force check of odd n ≤ 2·10⁵ not of the form p+2^a+2^b (a,b≥0): only n = 1 and n = 3 (independently confirmed up to 2·10⁴ by sympy). The literature (arXiv:2607.05357 abstract) gives N(x) ≫ log log x for Crocker's exceptions and N(x) ≫ x·exp(−(4+η)·loglog log x/loglog x·log x) (Pan-type). So exceptions are extremely sparse and start beyond 2·10⁵; finite checks cannot test the mechanism. Crocker's construction via Fermat numbers is mentioned in an MO snippet but not verified by me.",
 E_Q + ['arXiv:2607.05357 (abstract)'], 'Crocker construction not read; covering/Fermat structure not checked.', 'Locate Crocker 1971 construction and compare its exceptional family with the ES mod-840 covering.')

add('Z2029','covered',
 "The Brauer computation the item asks for is done in BRAUER_TWISTS.md §(0): for the universal-cover twist Y_d: ABC = k(A+B+C), k = n/(md), the algebraic Brauer quotient is Z/2 and the full Brauer quotient is Z/2 unless k is a rational square, in which case it is (Z/2)². The memo's own verdict is 'COLLAPSES' as a finite étale–Brauer T1 mechanism, so this covers the question but not an ES theorem.",
 ['BRAUER_TWISTS.md §(0) Summary'], 'Colliot-Thélène–Xu spinor framing not cited; not re-derived; integral-points transfer is the memo’s open issue.', '')

add('Z2031','nothing',
 "Premise check: Bilu–Hanrot–Voutier primitive-divisor results apply to Lucas-type values U_n(P,Q) with index n, so they supply divisors ≡ ±1 mod n only for integers of that Lucas form. The tied integers tp+1 are not Lucas values in general, and the item's families 15·2^s+1, 4^s+297 were not checked for the required form. No primitive divisors were computed.",
 [], 'No factorisations of Lucas-type values computed; family form not verified.', 'Test whether tp+1 = U_t(P,Q) for any small P,Q, or drop the item.')

add('Z2032','nothing',
 "The m−2 ladder for m/n (exact, existence-only): 5/n in 3 terms has no failures for n ≤ 60000 (C tool); 5/n in 4 terms none for n ≤ 200; 6/n in 4 terms none for n ≤ 1500; 7/n in 5 terms none for n ≤ 400; 8/n in 6 terms none for n ≤ 150 (recursion). Numerators with first 3-term failures: k=7 (n=2), k=8 (3,11,17,131,241). Consistent with Pomerance–Weingartner (arXiv:2511.16817): n_m ≥ exp(m^{1/3+o(1)}) for 3-term representability; their prediction (a prime in (m²,2m²) failing for m ≥ 20) is confirmed by exact enumeration for every m=20..40 (e.g. 401 for m=20).",
 E_EG3 + E_EG4 + ['arXiv:2511.16817 (abstract)'], 'Ladder only to m=8 and n ≤ 60000 (3 terms) / 1500 (4 terms); no statement about the first m where k = m−2 fails beyond that.', 'Extend the 4-term table to n ≤ 10⁵ with the C-style divisor method.')

add('Z2033','nothing',
 "Proved (elementary) and checked: for p≡1 (mod 4) there is NO diagonal solution (x=y forces a=4x−2p ∈ {2,2p,2p²} with a(4z−p)=2p², and each case needs p≡3 mod 4); verified for all 8,977 primes p≡1 (mod 4) ≤ 2·10⁵ (zero found). For p≡3 (mod 4) diagonal solutions always exist, e.g. x=y=(p+1)/2, z=p(p+1)/4 (9006 primes checked). So S₃ acts freely exactly in the class the title names; the record's 'p≡1 mod 4 checked below 1500' is now a proof. No non-S₃ involution was sought.",
 E_Q, 'No non-S₃ involution searched; fixed-point count for the involution not done.', 'Search for an involution on the fibre with classifiable fixed points for p ≡ 1 (mod 4).')

add('Z2035','interesting',
 "Exact 3-term check of the numerator-8 control: 8/n = 1/x+1/y+1/z has no solution for n ∈ {2,3,11,17,131,241} and for no other n ≤ 60000 (C enumeration, cross-checked with the Python recursion for n ≤ 300). Among primes > 3 the failures are exactly 11, 17, 131, 241, matching the record. This gives a small exact anti-overreach set: a candidate argument that does not separate 4/p from 8/p at these primes is not valid.",
 E_EG3 + E_EG4, 'Per-tool audit (does each argument distinguish 4 from 8?) not done; only the set of failures was computed.', 'Run each collected ES argument on 8/11, 8/17, 8/131, 8/241 and record which steps fail.')

add('Z2036','nothing',
 "Identity checked: 4/p = 1/((p−1)/4) − 1/(p(p−1)/4) holds, so signed relaxation is trivial. Exact enumeration of all nonzero-integer solutions of 4/13 = 1/x+1/y+1/z with max|·| ≤ B: 36, 78, 108, 120, 120 for B = 100, 300, 1000, 3000, 10⁴ (63 with exactly one negative entry at B=10⁴). The count saturates, so there is no growth to measure; the proposed 'move into the positive cone' step was not attempted.",
 E_SG, 'Birational move into the positive cone not attempted.', 'Check whether each one-negative solution of 4/13 is connected to a positive one by a coordinate permutation or Vieta-type move.')

add('Z2040','nothing',
 "Premise check against the cited source (Elsholtz–Tao arXiv:1107.1010 abstract): their theorem is Σ_{p≤N} f(p) ≍ N log²N up to a log log factor, i.e. average f(p) ≈ log³p over primes, not Σ_{n≤N} f(n) ≍ N log³N as the record states. The Clemens-complex / Manin–CLT exponent computation was not done.",
 ['arXiv:1107.1010 (abstract)'], 'Compactification, boundary divisor and Clemens complex not computed.', 'Correct the record’s exponent and decide whether a CLT prediction is worth computing.')

add('Z2048','interesting',
 "The Type-I slice (CONDITIONAL_ES Lemma 1.1, parameter t) gives a concrete witness: first witness t_min for primes p≡1 (mod 4) has median 3 over 39,175 primes ≤ 10⁶, so the typical first witness is found by factoring tp+1 ≈ 3p, an integer of size p. The divisor search 'divisor of tp+1 in class −1 mod t' is therefore a factorisation-type problem at small t, and only the Lenstra/Hales regime (t³ > tp+1, i.e. t ≳ √p) is known to be polynomial. The cost of factoring p-size numbers is what a witness search at small t pays.",
 E_TM, 'No timing at p ~ 10^30; the claim \"as hard as factoring\" is not established, only that the first witness is typically a factorisation of a ~p-size number.', 'Time factoring of 3p+1 for 30-digit p and check whether the first witness is always found from a smooth cofactor.')

add('Z2050','nothing',
 "Totally split primes (Legendre (−d/p)=1 for d=3,5,7 with p≡1 mod 4) have mean R(p) 95 versus 123 for others (p≡1 mod 4, p≤10⁵). But (−d/p)=(p/d) for these d, so this is a condition mod 105, and the effect is entirely the Mordell square classes mod 840: the 273 primes that are squares mod 840 have mean R=63, while split primes that are not squares mod 840 have mean 124 (= nonsplit mean 123). The residue-matched control is vacuous because split status is constant on classes mod 840.",
 E_R, 'Did not test total splitting in fields outside Q(i,√−d) for d ≤ 11 or the least-prime-splitting statement.', 'None: the split effect is fully explained by the mod-840 class.')

add('Z2056','nothing',
 "Not done: the standard parametrisation of 1/x+1/y+1/z = 1/w and the substitution w = n/4 were not written out, and no integrality conditions were tabulated.",
 [], 'Parametrisation, integrality conditions and counts not computed.', 'Write the parametrisation and test one congruence family.')

add('Z2058','nothing',
 "Exhaustive classification of the sorted 3-term solutions of 4/p for all 429 primes p≤3000: every prime has a Type I solution (exactly one denominator divisible by p) and a Type II solution (exactly two). Neither type alone fails at any prime ≤ 3000, so the record's claim of Type-II failures (14+ primes ≤ 10¹⁰) is not contradicted but not tested beyond 3000. The Type-I slice a=1 (t-parametrisation) also solves all p ≡ 1 mod 4 up to 10⁶, which is the disjointness question the item raises.",
 E_T12 + E_TM, 'Joint distribution of failure sets, the 10¹⁰ range, and the disjointness/parity argument were not done.', 'Extend the Type I/II classification to p ≤ 10⁶ using the t-slice and direct Type II search.')

add('Z2062','nothing',
 "Not done: genus-character decomposition X(p)/M_gen(p) and the 2-rank of class groups of Q(√−p·small) were not computed.",
 [], 'Genus decomposition not computed.', 'Compute 2-ranks of class groups for the hard primes and compare with R(p).')

add('Z2063','nothing',
 "Literature search for pointwise one-sided lower bounds of polylog size not carried out beyond the abstracts used elsewhere in this batch; no precedent was catalogued.",
 [], 'No literature survey performed.', 'Search for pointwise lower bounds on representation counts of size (log n)^c.')

add('Z2069','nothing',
 "Reasoning only: Hypothesis H supplies primes in polynomial families, which do not directly give divisors of a fixed-p integer in a residue class, so H does not obviously imply ES; the item's claim about every positive rational as (p+1)/(q+1) was not checked. No computation.",
 [], 'Claim about (p+1)/(q+1) not verified; no argument for or against H ⇒ ES written out.', 'Check the Schinzel–Sierpiński statement and whether H ⇒ ES via Dickson-type divisor counting.')

add('Z2071','nothing',
 "Not done: the Bateman–Horn comparison M_BM(p)/M₀(p) against a product ∏(1 − (p/ℓ)/(ℓ−1)) was not computed.",
 [], 'Singular-series comparison not computed.', 'Compute M_BM/M₀ for p ≤ 10⁵ and compare with the Bateman–Horn product.')

add('Z2072','nothing',
 "Literature-only item (Friedlander–Iwaniec d₃ level of distribution); no computation or source read in this pass.",
 [], 'Source not read; exceptional-set barrier F40 not analysed.', 'Read Friedlander–Iwaniec 1985 for the d₃ level and compare with the 3/4 barrier.')

add('Z2079','nothing',
 "Numerical check of the Borwein–Choi square-factor claim for xy+yz+zx (positive x,y,z): up to 10⁴ the non-representable N with a square factor are exactly {4, 18}, consistent with the cited theorem. The three-variable divisor parametrisation the item attributes to Borwein–Choi was not verified and has no computed link to the ES equation.",
 E_Q, 'Borwein–Choi paper not read; no ES link computed.', 'Read Borwein–Choi 2000 for the class-group argument.')

add('Z2083','nothing',
 "Romanoff's positive-density theorem for p+2^k is a density result; no pointwise ES connection was identified and no computation was performed.",
 [], 'Romanoff proof not read; no comparison with ES almost-all arguments.', 'None unless a concrete ES comparison is identified.')

add('Z2085','nothing',
 "Crocker's p+2^a+2^b exceptions: the explicit exceptions are extremely sparse (only n=1,3 below 2·10⁵, computed), so 'structured failure families' cannot be detected by finite search here. Literature: exceptions are infinite but with N(x) ≫ log log x (see Z2028). The obstruction-structure comparison with the ES mod-840 cover was not done.",
 E_Q + ['arXiv:2607.05357 (abstract)'], 'Comparison with ES cover and failed (★) primes not made.', 'See Z2028.')

add('Z2087','nothing',
 "Premise check: 4Cp+1 (or p+4d) is not a cyclotomic difference in general, so Zsigmondy's primitive divisors do not directly give divisors ≡ −1 mod 4C for ES parameters. No primitive-divisor computation was done.",
 [], 'No computation; cyclotomic reformulation not attempted for ES parameters.', 'Drop unless an ES family is shown to be cyclotomic.')

add('Z2095','nothing',
 "Not done: Graham's proof of his unit-fraction threshold was not retrieved and the claimed threshold 77 was not verified; no residue-class identity was compared with the mod-840 cover.",
 [], 'Source not retrieved; no comparison.', 'Retrieve Graham 1963 and verify the threshold statement before transferring anything.')

add('Z2100','nothing',
 "Read the abstract of Haag–Kertzer–Rickards–Stange (arXiv:2307.02749): the local-global conjecture for Apollonian packings is false. The ES-side transfer (spinor/reciprocity invariant for prescribed-entry matrices) was not attempted.",
 ['arXiv:2307.02749 (title via API)'], 'Full paper not read; no ES invariant tested.', 'Read the reciprocity criterion and test prescribed-entry matrices.')

add('Z2103','nothing',
 "Premise check: ℓ(n) (least non-residue) is undefined for square n, so 'the least-non-residue failure at squares' is not a feature flip of the least non-residue itself. The square-class effect the item looks for is present in R(p) but is the Mordell mod-840 class effect (Z2023/Z2050 controls), not a character degeneration in a separate sense.",
 E_R, 'Real-character contribution on square classes not separately computed.', 'None.')

add('Z2107','nothing',
 "Not done: character expansion of the residue indicator for R(p) modulo 4C and separation into principal/real/nonreal characters was not computed.",
 [], 'Character-expansion computation not done.', 'Compute the principal/real/nonreal split for p ≤ 10⁴.')

add('Z2109','nothing',
 "Read the abstract of Harpaz (arXiv:1511.04876): explicit sufficient conditions for integral points on schemes fibred into affine conics, including log K3 cases. Observed that the ES equation is a conic bundle over the x-line: for fixed x the fibre is (a y − b)(a z − b) = b² with a = 4x−p, b = px. Harpaz's conditions were not checked on this fibration.",
 ['arXiv:1511.04876 (abstract)'], 'Explicit criteria not verified on the ES fibration; base-change not analysed.', 'Check the Swinnerton-Dyer-type condition on the ES conic bundle for one fibre.')

add('Z2110','nothing',
 "Read the abstract of Mitankin–Uhlemann (arXiv:2411.02629): semi-integral Hasse principle holds for Markoff orbifold pairs, and strict semi-integral points without integral points are measured. The ES comparison was not made.",
 ['arXiv:2411.02629 (abstract)'], 'Theorem statements not read; no ES comparison.', 'Read the semi-integrality conditions and compare with ES denominators.')

add('Z2111','nothing',
 "Same source as Z2110 (arXiv:2411.02629 abstract): it separates approximation properties from Hasse existence for Markoff orbifold pairs. No ES example was translated.",
 ['arXiv:2411.02629 (abstract)'], 'Examples not read; no translation to the fixed-n ES surface.', 'Translate one approximation example to the ES surface.')

add('Z2112','nothing',
 "Same source as Z2110 (arXiv:2411.02629 abstract): relaxation of positivity/integrality is discussed for Markoff pairs. No ES relaxation was computed (the signed-solution test in Z2036/Z2370 is the closest computed analogue).",
 ['arXiv:2411.02629 (abstract)', 'scripts/z52d_p2_TO6_signed.py'], 'No semi-integral ES formulation tested.', 'Formulate the ES semi-integral question and check applicability.')

add('Z2113','nothing',
 "Same source as Z2110 (arXiv:2411.02629 abstract). The local-place conditions were not extracted and no congruence-subfamily test was run.",
 ['arXiv:2411.02629 (abstract)'], 'Local conditions not extracted.', 'Extract local conditions and test against the mod-840 classes.')

add('Z2121','nothing',
 "Read the abstract of Hales (arXiv:2410.05030, 'Divisors in residue classes revisited'): Lenstra's residue-class divisor algorithm runs in polynomial time when S³ > N, and a new sign-change-free method extends to Euclidean rings and Z[x]. I did not implement the algorithm on 4Cp+1; the threshold translation and witness-location data are in Z2123.",
 ['arXiv:2410.05030 (abstract)'] + E_TM, 'Algorithm not implemented or timed on tp+1.', 'Implement Lenstra/Hales on tp+1 for t ≥ √p and compare with the t_min data.')

add('Z2122','nothing',
 "Not done: the Euclidean-ring (e.g. Z[i]) generalisation was not applied to any ES certificate; only the integer-case threshold was considered (Z2123).",
 ['arXiv:2410.05030 (abstract)'], 'No Euclidean-ring computation.', 'Apply the Z[i] version to 4Cp+1 factorisations in Z[i] for one prime.')

add('Z2123','interesting',
 "Threshold translated to ES parameters: Lenstra's condition S³ > N with S = t, N = tp+1 is t ≳ √p. Among 39,175 primes p≡1 (mod 4) below 10⁶ only 5 have minimal Type-I parameter t_min ≥ √p. Within the window t∈[√p,4√p] (t≡3 mod 4), 86.3% of the 8,977 primes ≡1 (mod 4) below 2·10⁵ have at least one witness (median count 2), so the polynomial regime contains witnesses for most primes, but the typical minimal witness (median t=3) lies far below it, where the algorithm’s guarantee does not apply.",
 E_TM, 'Algorithm itself not run; the window statistic is existence of witnesses, not an algorithmic success rate.', 'Run Hales/Lenstra at each t ∈ [√p, 4√p] for p ≤ 10⁵ and record success against witness existence.')

add('Z2125','nothing',
 "Not done: function-field Z[T] analogue of the divisor search was not specialised to ES parameters.",
 [], 'Not done.', 'Specialise the Hales algorithm to F_q[T] for the ES divisor condition.')

add('Z2132','nothing',
 "Not done: the continuant/SL₂ matrix encoding of the length-three word and the congruence test on its entries were not written out or computed.",
 [], 'Matrix computation not done.', 'Write the length-3 ES word as a product of CF matrices and test the entry congruences on small primes.')

add('Z2133','nothing',
 "Checked the title of arXiv:1608.08322 (Paulin, 'Largest values of the Stern sequence, alternating binary expansions and continuants'); the ordering argument was not read and no ES counting analogue was tested.",
 ['arXiv:1608.08322 (title via API)'], 'Ordering argument not read; no test.', 'Read the continuant normalisation and test on the ES certificate ordering by denominator.')

add('Z2136','nothing',
 "The source is Greg Martin, 'Denser Egyptian fractions' (arXiv:math/9811112; the record's ID lacks the 'math/' prefix). The abstract/construction was not read, so the step at which a fixed term count fails was not identified.",
 ['arXiv:math/9811112 (title via API)'], 'Construction not read.', 'Read Martin’s construction and identify the term-count step.')

add('Z2140','nothing',
 "Checked the proposed involution directly: for fixed x the fibre is (a y − b)(a z − b) = b² with a = 4x−p, b = px, and the divisor swap d ↦ b²/d sends (y,z) ↦ (z,y). So the 'nontrivial' involution is just the transposition y↔z; no height-decreasing move exists. Also the ES surface is linear in x, x(4yz − n(y+z)) = n yz, so no Vieta root swap exists (matching the record's own caveat).",
 ['derivation in this record (algebra); see Z2258 / Z2297'], 'No descent tested numerically (none exists beyond the transposition).', 'None: drop the Vieta-descent idea unless a different parametrisation is used.')

add('Z2146','nothing',
 "Title of arXiv:1309.3595 (Lamzouri–Li–Soundararajan, 'Conditional bounds for the least quadratic non-residue and related problems') checked; the conditional bound was not compared with an ES fibre witness statement.",
 ['arXiv:1309.3595 (title via API)'], 'Explicit GRH dependence not read; no comparison.', 'Read the explicit GRH bound and state the ES-fibre analogue.')

add('Z2147','nothing',
 "Same source as Z2146 (arXiv:1309.3595). No ES tied-integer reformulation as a least-prime-in-progression question was attempted.",
 ['arXiv:1309.3595 (title via API)'], 'Not done.', 'Attempt the reformulation for one residue class.')

add('Z2154','nothing',
 "Literature item (Croot; Liu–Sawhney unit-fraction density bounds) not fetched; no counting inequality extracted.",
 [], 'Sources not read.', 'Read Liu–Sawhney 2024 and check whether the counting inequality restricts to three denominators.')

add('Z2209','nothing',
 "Checked the claimed square-factor theorem for xy+yz+zx with positive x,y,z up to 10⁴: the non-representable N with a square factor are exactly {4, 18}, consistent with Borwein–Choi. This equation is not the ES cubic 4xyz = n(xy+yz+zx), so no ES certificate was produced by the parametrisation.",
 E_Q, 'Square-factor parametrisation not transferred to ES (n = m r² test not run).', 'None.')

add('Z2210','nothing',
 "Squarefree non-representables by xy+yz+zx (positive x,y,z) up to 10⁴: 16 numbers, {1,2,6,10,22,30,42,58,70,78,102,130,190,210,330,462}, the last being 462 (consistent with a finite list). ES failure counts split by squarefreeness were not computed.",
 E_Q, 'ES side not computed; finiteness not proved.', 'Compare the squarefree/non-squarefree split of the 3-term failing n for k=8 and k=10 (Z2215) with the xy+yz+zx squarefree list.')

add('Z2212','nothing',
 "Only the xy+yz+zx side was checked (see Z2209). The discriminant/class-group reading of ES witnesses in Q(i) was not tested.",
 E_Q, 'Q(i) class data not computed.', 'Compare witness counts with class data of Q(i) for hard primes.')

add('Z2214','nothing',
 "Read the Elsholtz–Tao abstract (arXiv:1107.1010): Σ_{p≤N} f(p) ≍ N log²N (log log factor), and f(p) = O(log³p·loglog p) for primes of density 1; they also give f(p) ≪ p^{3/5}. This is an averaged result: it gives 'almost all primes have witnesses' with the density-zero exceptional set uncontrolled, so it does not yield the pointwise statement. The MathOverflow power-saving question (≤ n^{0.99}) was not settled.",
 ['arXiv:1107.1010 (abstract)'], 'MO thread not read; power-saving bound for the exceptional set not derived.', 'Quantify the exceptional-set size from the averaged bound and compare with the n^{0.99} question.')

add('Z2215','interesting',
 "Exact 3-term failure sets of k/n for n ≤ 60000 (k = 3..40, C enumeration): k=3–6 none; k=7: {2}; k=8: largest 241; k=9: 19; k=10: 181; k=11: 37; k=12: 12241; k=13: 281; k=14: 841; k=15: 20521; k=16: 36529. No clean law in k, and for k ≥ 27 the largest failure sits near the 60000 cutoff, so n(k) is undetermined there. The failure density rises steeply (k=40: 461 failures ≤ 60000, about 0.8%); Pomerance–Weingartner (arXiv:2511.16817) predict primes in (m²,2m²) fail for m ≥ 20, confirmed for every m = 20..40 (e.g., 401 for m=20).",
 E_EG3 + ['arXiv:2511.16817 (abstract)'], 'Cutoff 60000 is too small to determine n(k) for k ≳ 27; no fit to the MO growth k^{8/7}; did not extend to 10⁶.', 'Extend the k ≥ 27 scans to 10⁶ in the C tool (needs b² ≤ 2⁶⁴, so switch to 128-bit throughout) and test the largest-failure growth.')

add('Z2216','nothing',
 "Exact 4-term check of the 'k < a terms' regime: 5/n has no 4-term failures for n ≤ 200, and 6/n none for n ≤ 1500 (recursion, cross-checked on 3/n, 4/n two-term failures and 8/n three-term failures). Equivalent statements in MO 212865 were not read.",
 E_EG4, "MathOverflow thread and Elsholtz (2001) not read; the k ≥ a regime is not compared.", 'Read Elsholtz 2001 for the k<a-term obstruction.')

add('Z2217','nothing',
 "Compared numerators 3..6: no 3-term failures for k ∈ {3,4,5,6} at any n ≤ 60000; the first 3-term failures are k=7 (n=2 only), k=8 (3,11,17,131,241), k=9 (2,5,11,19), k=10 (2,3,7,11,43,61,67,181). The residue tagging of missing k against p mod 840 was not carried out.",
 E_EG3, 'Tagging by residues mod 840 not done.', 'Tabulate the k=8 and k=10 failing primes by residue mod 840.')

add('Z2219','nothing',
 "Identity: 2xy+x+y = n ⇔ (2x+1)(2y+1) = 2n+1, so the prime criterion holds. For ES the fibre (a y − b)(a z − b) = b² also factors, but its right-hand side depends on x, so the criterion becomes a divisor-in-class question, not a primality test. No analogue of 2n+1 was found.",
 [], 'No computation.', 'None.')

add('Z2227','nothing',
 "Checked the Borwein–Choi square-factor covering for xy+yz+zx up to 10⁴ (only 4 and 18 fail among non-squarefree N) and the squarefree residue (16 non-representables, last 462; see Z2210). The ES-side square/squarefree decomposition of 4Cp+1 was not tested.",
 E_Q, 'ES-side decomposition not tested.', 'Partition the Type-I tied integers 4Cp+1 by square factor for hard primes.')

add('Z2229','nothing',
 "Boundary exceptions for xy+yz+zx verified up to 10⁴: only 4 and 18 (non-squarefree). The ES denominator boundary cases (zero, negative, repeated denominators) were not catalogued computationally; the diagonal case is handled in Z2033.",
 E_Q, 'ES boundary list not produced.', 'Catalogue ES denominator boundary cases for small p.')

add('Z2230','nothing',
 "Literature item (A025052 reference to indecomposable binary forms, Zhu–Shao/Peters) not read; no discriminant invariant computed for ES witnesses.",
 [], 'Source not read.', 'Read the cited reference and test a discriminant invariant on ES witnesses in Q(i).')

add('Z2231','nothing',
 "Squarefree non-representables by xy+yz+zx up to 10⁴ are the 16 numbers listed in Z2210 (last 462); finiteness is observed, not proved. Le's (1998) note was not read, so no tail bound was derived and nothing was tested on ES's residual squarefree parameters.",
 E_Q, 'Le 1998 not read; no tail bound; no ES residual test.', 'Read Le 1998 for a divisor-estimate tail bound.')

add('Z2253','nothing',
 "Literature item: Bourgain–Kontorovich (arXiv:1205.4416) title checked; the density-one sieve was not read and no comparison with ES was made.",
 ['arXiv:1205.4416 (title via API)'], 'Sieve step not read.', 'Read the expansion step of Bourgain–Kontorovich.')

add('Z2258','nothing',
 "Checked: the ES equation 4xyz = n(xy+yz+zx) is linear in each variable (x(4yz − n(y+z)) = n yz), so there is no Markov-type Vieta root swap; the only fibre involutions are the S₃ coordinate permutations (Z2140). No descent with decreasing height exists beyond these.",
 ['derivation in this record (algebra)'], 'No Markov-type uniqueness test (none to test).', 'None.')

add('Z2267','nothing',
 "Not done: the negative-continuant matrix product for ES and the continued-fraction normalisation test were not computed.",
 [], 'Matrix product and normalisation test not done.', 'Compute the normalisation on the ES words for primes ≤ 10⁴.')

add('Z2268','nothing',
 "Greedy Egyptian expansion of 4/p for primes p≡1 (mod 4) up to 10⁵ (4,783 primes): greedy terminates with 3 terms for 2,399 of them (already an ES certificate, x₁ = ⌈p/4⌉) and with 4 terms for 2,384. The 4-term cases were not analysed for a 3-term compression identity.",
 E_Q, 'Compression identity search for the 4-term cases not done.', 'Look at the 4-term greedy remainder and test whether a pair of terms can be merged.')

add('Z2276','nothing',
 "Literature-only item (Apollonian density-one sifting): not analysed.",
 ['arXiv:1205.4416 (title via API)', 'arXiv:2307.02749 (title via API)'], 'Sieve dimension and expansion not analysed.', 'Read the sieve dimension of Bourgain–Kontorovich.')

add('Z2281','nothing',
 "Checked the EFL reference (Kang–Kelly–Kühn, arXiv:2101.04698, 'A proof of the Erdős–Faber–Lovász conjecture'); the large-n threshold and its finite verification range were not extracted, so the proof-organisation comparison was not done.",
 ['arXiv:2101.04698 (title via API)'], 'Threshold not extracted.', 'Extract the large-n threshold from the paper.')

add('Z2286','nothing',
 "Bit-length check: for a fixed prime p, every sorted solution has denominators bounded by a polynomial in p (x ≤ 3p/4, y and z ≤ (b²+b)/a with b = px ≤ p²), so witnesses have O(log p) bits. Certificate size is therefore not the obstruction; the search cost is (Z2048). The cited arXiv:2302.02143 is Tall's paper on the Scholz conjecture for addition chains, which is topically relevant but not checked against this item.",
 ['arXiv:2302.02143 (title via API)', 'derivation in this record'], 'No addition-chain bound compared.', 'None.')

add('Z2288','nothing',
 "Numerator-contrast data: k=3,4,5,6 have no 3-term failures up to 60000; k=7 (n=2), k=8 and above have failures (Z2215). The known constructions for m=4 versus m>4 and the point where constants fail to be uniform were not analysed.",
 E_EG3 + E_EG4, 'Constants for general m not analysed.', 'Compare the known constructions for m=4 and m=5 in the Schinzel literature.')

add('Z2292','covered',
 "The function-field Egyptian-fraction analogue is answered in the repo: BRAINSTORM/ff_erdos_straus.md Theorem 2.1 (PROVED): for fixed n and k the proportion of irreducible P of degree n with ES_q(A,P) tends to 0 as q → ∞, so the function-field analogue fails in the large-q regime. The integer translation of the key divisor-counting lemma and the marked failing estimate were not written out.",
 ['BRAINSTORM/ff_erdos_straus.md §Theorem 2.1'], 'Integer translation of the counting lemma not done.', '')

add('Z2295','nothing',
 "Literature/analysis item (Châtelet surfaces, descent by torsors) not carried out; the ES fibres are conics over the x-line, which is the only structure checked (Z2296).",
 [], 'Torsor descent not computed.', 'Check whether the ES conic bundle is a Châtelet-type fibration over Q.')

add('Z2296','nothing',
 "Observed that the ES surface is a conic bundle over the x-line: for fixed x the fibre (a y − b)(a z − b) = b² with a = 4x − p, b = px is a conic in (y,z), and integer points of each fibre are the divisor pairs of b² in a class. Uniform fibrewise estimates were not computed.",
 E_T12, 'No uniform fibre bound computed.', 'Compute the number of fibre points as a function of x for one prime.')

add('Z2297','nothing',
 "Checked for height-reducing involutions on the ES solution set: the only fibre involutions are the S₃ coordinate permutations (Z2140, Z2258), which do not reduce max(x,y,z). So the canonical reduced representative is the sorted triple, and no orbit-reduction beyond sorting exists.",
 ['derivation in this record (algebra)'], 'No orbit computation beyond sorting.', 'None.')

add('Z2302','nothing',
 "Not done: no rational parametrisation of the ES cubic was written, so no denominator-divisibility comparison was made.",
 [], 'Not done.', 'Write one rational parametrisation and check the denominator structure.')

add('Z2310','nothing',
 "Not done: the character expansion of the ES count and the Kronecker-character term for p≡1 mod 4 were not computed.",
 E_R, 'Character expansion not computed.', 'Compute the real-character term for p ≤ 10⁴ against R(p).')

add('Z2327','nothing',
 "Not done: the quaternion-order reformulation and its lattice were not compared with the ES quadratic form.",
 [], 'Not done.', 'Write the ES quadratic form and its lattice.')

add('Z2330','nothing',
 "Orbit counting checked: for p ≡ 1 (mod 4) no solution has two equal denominators (Z2033), so the ordered count is exactly 6 × the sorted count. Verified for p=13 (24 ordered positive solutions = 6 × 4 sorted) and p=17 (24 = 6 × 4).",
 E_SG + E_R, 'Orbit counts for p ≡ 3 (mod 4) (where stabilisers of order 2 occur) not tabulated.', 'Tabulate the p ≡ 3 mod 4 two-equal solutions.')

add('Z2334','nothing',
 "Positive versus signed counts for 4/p with nonzero integer denominators: for p=13 the total is 120 (24 positive, 96 with a negative denominator; 63 with exactly one negative) at B = 10⁴; for p=17 it is 114 at B = 1000 (24 positive). Convexity of the feasible region for one denominator was not analysed.",
 E_SG, 'Convex-region analysis not done; p=17 not saturated beyond B=1000.', 'Test saturation for p=17 to B=10⁴.')

add('Z2337','nothing',
 "Not done: genus decomposition of the ES count and comparison of local densities per prime class were not computed.",
 [], 'Not done.', 'Compute genus-character contributions for p ≤ 10⁴.')

add('Z2346','nothing',
 "Not done: the Appell–Lerch completion of (K1′) from METAPLECTIC_ES.md and the nonholomorphic support check were not carried out.",
 [], 'Not done.', 'Check the completion of the theta quotient for one level.')

add('Z2354','nothing',
 "Identities checked: 4/p = 1/p + 1/p + 2/p, and with x = (p+3)/4 the remainder 12/(p(p+3)) = 3/N with N = p(p+3)/4 = 1/N + 2/N. Other weightings (a,b,c) were not enumerated for non-triviality.",
 [], 'Weightings beyond (1,1,2) not enumerated.', 'Enumerate small weights (a,b,c) for which a/x+b/y+c/z = 4/p is nontrivially solvable.')

add('Z2357','nothing',
 "Not done: the union-of-lines phase diagram (failure counts as lines are added) was not computed; the single-line and (★) data were not re-derived.",
 [], 'Not done.', 'Define the lines and compute failure counts for X = 10⁶..10⁹.')

add('Z2358','nothing',
 "Checked the reciprocal-coordinate form: with X = 1/x etc., the ES equation is X+Y+Z = 4/n, linear. The birational automorphism group preserving positivity was not computed.",
 ['derivation in this record (algebra)'], 'Automorphism group not computed.', 'Compute the automorphisms of the reciprocal plane preserving unit-fraction lattice points.')

add('Z2359','nothing',
 "Not done: no Stern–Brocot-type tree generated by ES₅ moves was constructed and no depth data were computed.",
 [], 'Not done.', 'Construct the ES₅ tree for primes ≤ 10⁴ and record depths.')

add('Z2361','nothing',
 "Premise check: the Elsholtz–Tao sum is Σ_{p≤N} f(p) ≍ N log²N (see Z2214/Z2040), so an average over all n with exp(−M(n)) weights is not what is measured in the cited bound. The sum Σ_n exp(−M_BM(n)) was not computed.",
 ['arXiv:1107.1010 (abstract)'], 'Sum not computed; M_BM not recomputed.', 'Compute Σ_n exp(−M(n)) for a model M from R(p) data.')

add('Z2364','nothing',
 "Mordell-hard classes check: among primes ≡1 (mod 4) below 10⁵, the 273 primes that are squares mod 840 have mean R=63 versus 123 for the rest (R data), consistent with the square classes being the hard residual set. The covering identities for the non-square classes mod M = 840ℓ (ℓ ≤ 50) were not checked.",
 E_R, 'Covering for M = 840ℓ not computed.', 'Check the non-square classes mod 840·3 against an explicit identity list.')

add('Z2366','nothing',
 "Verified exhaustively for primes ≤ 3000: 3/p has a two-term representation iff p ≡ 2 (mod 3) or p = 3 (fails for every p ≡ 1 mod 3), and 4/p has a two-term representation iff p ≡ 3 (mod 4) (fails for every p ≡ 1 mod 4). Both are elementary (divisor argument). The m/n ladder with m−1 terms was tabulated only for m = 3, 4.",
 E_Q + E_EG4, 'Full ladder table for m ≥ 5 with m−1 terms not produced.', 'Tabulate 5/n in 4 terms (done in Z2216: no failures ≤ 200) and check the obstruction at m = 3 for other primes.')

add('Z2367','interesting',
 "Classified all sorted 3-term solutions of 4/m² for odd m ≤ 61 by the number of denominators divisible by m. For every prime m in this range no solution has exactly one denominator divisible by m (Type-I-type absent, consistent with T1); for composite m such solutions exist (m=9: 6+11 solutions; m=15: 91+37; m=21: 193+56). The item's claim that every solution of 4/m² is a scaled solution of 4/d with d | m is false: for m=9 only 5 of 46 solutions have gcd(x,y,z) ∈ {9,27} (scaled from 4/9 or 4/3); 9 are primitive (gcd 1).",
 E_SQ + E_Q, 'Mixed-type solutions for composite m not characterised beyond counts; claim about all odd m ≤ 101 only for m ≤ 61 (classes) and ≤ 81 (gcd).', 'Check whether the exactly-one-denominator solutions for composite m=9·k come from a prime factor square and whether T1 forbids them.')

add('Z2369','nothing',
 "Not done: exact formula for r₄(n) = 8σ*(n) was noted, but the analogous theta-quotient decomposition of ES counts and the Linnik large-value term were not identified.",
 [], 'Not done.', 'Compare the theta-quotient normal form with r₄ for one level.')

add('Z2370','nothing',
 "Premise check failed: signed solutions of 4/13 with nonzero integer denominators are finite in this range. Exact counts: 36, 78, 108, 120, 120 for max|·| ≤ 100, 300, 1000, 3000, 10⁴ (one negative entry: 63 at B=10⁴), so the count does not grow polynomially as the record states; it saturates. For p=61 there are none for B ≤ 300 and 87 at B=1000.",
 E_SG, 'Dependence on p^θ cutoffs not studied; only three primes tested.', 'Check saturation for two more primes to B=10⁴ and whether the saturated count equals the number of divisor-class solutions.')

add('Z2374','nothing',
 "Not done: the small-prime-factor count (q | 4Cp+1 with q ≡ −1 mod 4C and q ≤ log²p) was not computed. The condition is equivalent to a divisor of 4Cp+1 in a class, i.e. the witness condition itself, so it adds no new information beyond the Type-I data.",
 E_TM, 'Small-prime-factor count not computed.', 'Count (q, C) pairs with q ≤ log²p for primes ≤ 10⁵ using the t_min data.')

add('Z2376','nothing',
 "Not done. The ES events are divisibility events ('4Cp+1 has a divisor ≡ −1 mod 4C'), not primality events, so Maynard–Tao weights do not apply directly; no MT ratio was computed.",
 [], 'Not done; admissibility not checked.', 'Only attempt if the divisor events are reformulated as prime events.')

add('Z2377','nothing',
 "Not done. Same reason as Z2376: certificate events are divisibility events, not primality, so Maynard's dense-cluster theorem does not apply without reformulation.",
 [], 'Not done.', 'None unless reformulated.')

add('Z2378','nothing',
 "Smoothness of the minimal Type-I parameter: with y = (log p)², t_min is y-smooth for 99.99% of the 39,175 primes ≡1 (mod 4) below 10⁶ and for 99.4% of the 158 'hard' primes with t_min ≥ 30. So restricting to smooth C is nearly free for the minimal witness. The item’s actual question, whether R(p) restricted to smooth C keeps the log²p main term, was not measured; the memo verdict ('COLLAPSES', B6 leak) was not revisited.",
 E_TM, 'R(p) restricted to smooth C not computed; main term not fitted.', 'Compute R restricted to smooth C for p ≤ 10⁵ and compare the log² p fit.')

add('Z2379','nothing',
 "Literature-only item (Maynard, Primes in APs to large moduli I–III, arXiv:2006.06572 title checked). The uniform-residue-class variant (part III) was not read; the ES Type II sum was not written in that form.",
 ['arXiv:2006.06572 (title via API)'], 'Parts II–III not read.', 'Read part III and write the ES Type II sum with a(p) residue.')

add('Z2383','nothing',
 "Literature-only item (Matomäki–Radziwiłł, arXiv:1501.04585 title checked). The fixed-p progression version (Klurman–Mangerel–Teräväinen) was not checked for the modulus 4p and interval length.",
 ['arXiv:1501.04585 (title via API)'], 'Not checked.', 'Check Klurman–Mangerel–Teräväinen for modulus 4p.')

add('Z2396','nothing',
 "Not done: joint distribution of (ν/f, f mod 4cd) for the roots of ν² ≡ −D was not computed.",
 [], 'Not done.', 'Compute the joint distribution for D = 4c²d small and f ≤ 10⁶.')

add('Z2398','nothing',
 "Not done beyond the repo's own note (PARITY_AUDIT B7 records the Kloosterman-fraction form as degenerate in the (u,C) variables). The trilinear application was not attempted.",
 [], 'Not done.', 'None unless the degeneracy is shown to be avoidable.')

add('Z2409','nothing',
 "Not done: pretentious distances for the divisor-class character sums were not computed.",
 [], 'Not done.', 'Compute the character sums for the failing set of k/n (Z2215) and test for a real-character pretentious shift.')

add('Z2415','nothing',
 "Literature-only item (Thorner–Zaman, arXiv:1604.01750 title checked). The ES forcing-line exponents were not tabulated.",
 ['arXiv:1604.01750 (title via API)'], 'Not done.', 'Tabulate required Chebotarev classes for EXSET_CHAR_FORCING lines.')

add('Z2417','nothing',
 "Least quadratic non-residue ℓ(p) for all primes up to 10⁶ (exact Legendre symbols): maximum ℓ = 43 at p = 366791; 2,365 primes have ℓ ≥ 13 and 1,145 have ℓ ≥ 17; the first prime with ℓ ≥ 17 is p = 1559, so the 'ℓ ≤ 13' forcing line already fails there. The explicit Burgess/Treviño bound was not evaluated, and the claim that ES is classically settled when the least QNR is 3, 5, or 7 was not verified.",
 E_Q, 'Explicit Burgess (Treviño) constants not computed; the 3/5/7 claim not verified.', 'Evaluate Treviño’s explicit Burgess bound for p ≤ 10⁶ and compare with the observed ℓ(p).')

out = '\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n'
open(D + 'outcome_TO6.jsonl', 'w').write(out)
print('rows', len(rows))
