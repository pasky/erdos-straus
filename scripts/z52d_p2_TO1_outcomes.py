# z52d pass2 TO1: writes data/z52b/pass2/outcome_TO1.jsonl (one line per input mid). Decisions + summaries recorded here.
import json
S = 'scripts/z52d_p2_TO1_'
ES = 'data/z52b/pass2/TO1/es_100000.tsv'
SL = 'data/z52b/pass2/TO1/Eslice_1e8.tsv'
rec = {}
def R(mid, outcome, summary, evidence, not_done, nxt):
    rec[mid] = dict(mid=mid, outcome=outcome, summary=summary, evidence=evidence, not_done=not_done, next=nxt, prev_outcome='none')

R('Z0252','nothing',"B2 divisor covering as Chebotarev sets: p is covered by (C,d) when d | 4Cp+1 with d = -1 (mod 4C), i.e. p = -(4C)^{-1} (mod d), a Frobenius condition in Q(zeta_d) for prime d. Over the 4783 primes = 1 mod 4 below 10^5, C<=10, d<=2000 cover 98.5% (C=1 alone 74%, C<=2 90%); 70 stay uncovered (157, 409, 577, 1621, 2521, ...).",
  [ES, S+'chebotarev.py'], "Chebotarev effective bounds and the field list beyond d<=2000 not done; no covering theorem claimed (Mordell obstruction unaffected).", "Test whether the uncovered set is exactly the large-C-certificate primes (409, 577, 5569 are the Lean-noted ones).")
R('Z0255','nothing',"Checked the premise: for S={5}, e=3 divides 1+5^j exactly for odd j (period 2), so the instances are infinite. General argument: whether e | 1+eta holds depends only on eta mod e, and the S-unit group maps to (Z/e)^* with finite image, so the instances for fixed S form finitely many exponent cosets, i.e. congruence type (B1). Argument only; no search for non-congruence families.",
  [], "No computer search for non-congruence families (argument-level only).", "None needed unless a non-congruence instance is searched for.")
R('Z0256','nothing',"Ran the Prop 3.3 construction for all 21 primes p = 1 mod 4 <= 200: eps = a+b sqrt p (N = -1), inert l = 3 mod 4, eta = eps^{2j} = -1 (mod l), kappa=(1+eta)/l; verified Tr(kappa)/N(kappa)=l and 4/p-1/x = l/(px) with x=(p+l)/4 for all 21. Trace descent returns exactly the Lemma 3.1 remainder: kappa and its conjugate give 1/kappa+1/kappabar = l, so the Z-identity is the same l/(px) remainder, no new integer identity. Coefficients grow to 10^60+ (eta is huge).",
  [S+'quadunit.py', 'BRAINSTORM/other_rings.md §3'], "8/p trace-descent variant not run; only p <= 200.", "Ask whether l/(px) = 1/y+1/z has a p-polynomial solution family for the l that occur.")
R('Z0258','nothing',"The p-tied surrogate eta(p) = 4Cp makes 1+eta = 4Cp+1, so the 'integer unit' condition is exactly the B2 divisor condition (d | 4Cp+1, d = -1 mod 4C). Its covering by C<=10, d<=2000 is 98.5% of p=1 mod 4 below 10^5 (Z0252). Nothing beyond B2 was tested for other eta families.",
  [ES, S+'chebotarev.py'], "Other eta(p) forms (a p^k +- b) not searched; T1 check at squares not redone.", "Test eta(p)=a p^2 forms on the uncovered primes.")
R('Z0260','nothing',"Full enumeration of all ES solutions for primes = 1 mod 4 below 10^5: the 'all denominators = 0 mod 3' world fails at 18 primes: 5,13,29,37,73,97,193,433,577,1129,1657,1873,2521,2593,3433 (below 8000, matching the 15 in the brief) and 10369, 12049, 12241 above. No failure in (12241, 10^5] (about 4300 primes), but this does not show stabilisation. For comparison the all-even (m=8) world fails only at {17, 241} up to 10^5, reproducing the brief.",
  [ES, S+'es.c', S+'analyse.py'], "Stabilisation is not proved; a tail argument would need a density estimate for solutions with 3 | all denominators.", "Extend the m=12 run to 10^6 with the E-mode style early exit if a mod-3 filter is added.")
R('Z0262','nothing',"2-adic table over all 4783 primes: every realised sorted valuation triple has its top two valuations equal (forced: the maximal valuation of the reciprocal sum must cancel), e.g. (0,1,1) realised by all primes; (0,1,2) never. The all-even world with some denominator = 0 mod 8 fails at 13 primes below 8000 (5,13,17,73,97,113,193,241,577,769,2521,3169,3361) and at 8161 above; these primes still realise admissible patterns like (1,3,3) for most p, so the failures are not explained by 2-adic pattern exclusion alone.",
  [ES, S+'es.c', S+'patterns.py'], "Per-pattern failure table is recorded only as realised/missing counts; no conditional lottery model fitted.", "Fit failures of the 8-world against the 2-adic pattern counts at 10^6 (requires the 2-adic column in the solver).")
R('Z0263','nothing',"Minimal max-denominator M(p) over all solutions, primes = 1 mod 4 below 10^5: M(p) > p^{3/2} for 3539 of 4783 primes (74%; 359/499 below 8000, same as the brief). Median log M/log p = 1.55 in every decade; over p >= 10^4 the exponent ranges in [1.43, 1.80].",
  [ES, S+'analyse.py'], "No liminf/limsup claim; exponent range is data-level only.", "Compare the exponent distribution with the lottery model prediction of minimal denominators.")
R('Z0269','interesting',"Per-family failure counts (exact sympy, primes = 1 mod 4 below 5*10^4, families c,d <= 12) from the divisor forms in FRONTIER/CONDITIONAL_ES: Type II(1,1) is the single closest family (fails at 673 of 2549 primes, 26%); the best Type I(1,2) fails at 1257 (49%). The union over Type II families (c,d<=12) leaves 0 uncovered primes, while the union over Type I families leaves 89 uncovered. The next step is to find the least (c,d) per prime and its growth.",
  [S+'families.py', 'data/z52b/pass2/TO1/families_50000_12.json', 'data/z52b/pass2/TO1/families_10000_12.json'], "Only c,d<=12 and p<5*10^4; the family ranking is for these parameters only; no asymptotics. The union result is a data-level observation, not a proof (each family is conditional on the divisor form).", "Compute the least (c,d) cost per prime up to 10^6 with Type II and look at its growth in log p.")
R('Z0273','nothing',"Read the Z[1/3] mechanism (other_rings Prop 3.2: 7 = 1/(4/27)+1/4 with 7 | 1+27 used for n = 1 mod 4); the comparison with the 'numerator 3 over Z[1/3]' world and the tie to the m = 9, 25 computations were not run (no data file for m = 9,25 was located under this item).",
  ['BRAINSTORM/other_rings.md §3 (Prop 3.2)'], "The comparison and the m = 9, 25 tie-in were not computed.", "Locate or rerun the m = 9, 25 searches and compare with the Z[1/3] numerator-4 mechanism.")
R('Z0274','nothing',"Checked the repo places named (QUATERNION_ES.md, y1_heegner_level_t.md, z31_duke_equidistribution.md, z9_heegner_layers.md): they discuss the quaternionic reformulation but no discriminant attached to p. Did not identify a discriminant or run a Hecke orbit test.",
  ['QUATERNION_ES.md', 'BRAINSTORM/z9_heegner_layers.md'], "Discriminant attached to p and any Hecke/Heegner test not done.", "Identify the discriminant of the quaternion order attached to 4/p first.")
R('Z0275','nothing',"Strict thinning (every denominator has no prime factor = 3 mod 4), exact enumeration for primes = 1 mod 4 below 8000: the world fails at 57 of 499 primes (11%), first at 41, 137, 233, 241, 557, last 7529. This world is a subset of the sums-of-two-squares norm world (which fails at about 2%, 40 primes below 2*10^4), so its failures must be at least as many (monotone check); Eisenstein 451/499 and x^2+2y^2 276/499 fail far more. The lottery-fit comparison was not run.",
  [S+'worlds.py', 'data/z52b/pass2/TO1/worlds_8000.json'], "Per-thinning lottery fit (predicted vs observed failure fraction) not done; only p < 8000.", "Fit the failure fraction of the strict world against the density of allowed denominators and extend to 10^5 with a C factoriser.")
R('Z0276','interesting',"Eisenstein-norm world (all primes = 2 mod 3 in denominators to even power) fails at 451 of 499 primes (p < 8000). Its 48 survivors all have, in every solution, a denominator divisible by 3 (no 3-free solution exists). This is forced: a 3-free denominator in this world is = 1 mod 3, so a 3-free solution would give 4/p = sum of three units = 0 (mod 3), but 4/p is a 3-adic unit.",
  [S+'worlds.py', 'data/z52b/pass2/TO1/worlds_8000.json'], "The 3-adic argument covers the 3-free case only; the 403 failures with 3 | denominators are not explained by it.", "Count, for the 48 survivors, how many denominators are divisible by 3 and by which power.")
R('Z0277','nothing',"Not in batch.", [], "", "")
R('Z0280','nothing',"The only composition law in the repo is ES(n) => ES(kn) (scaling); a prime-to-prime law ES(q) => ES(p) with q < p would need a p-tied integer whose q-divisors supply certificates. Not searched.",
  ['COMPOSITION_ES.md'], "Search for f(p) with q | f(p), q < p, not done.", "Check COMPOSITION_ES.md for laws with a q < p always available.")
R('Z0281','nothing',"Pencil y = t x is a conic family in (x,z); checked the repo entries (LONGSHOT_FIBRED.md, elliptic_fibration_es.md) by name only; no conic-pencil integral point computation run.",
  ['LONGSHOT_FIBRED.md', 'BRAINSTORM/elliptic_fibration_es.md'], "Pencil and integral-point analysis not done.", "Write the pencil explicitly for a fixed p and count integral points per member.")
R('Z0282','nothing',"Brute-force local counts N_k = #{(x,y,z) mod p^k: 4xyz = p(xy+yz+zx) mod p^k} with N_k/p^{2k}: p=3: 2.11, 3.67, 3.67 (k=1,2,3; stable from k=2); p=5: 2.44, 4.52, 4.84 (k=1..3, still moving); p=13: 2.78, 5.40 (k=1,2); p=17: 2.83, 5.54. The density is not yet stable at k=3 for p=5, so no closed form.",
  [S+'padic.py'], "k >= 4 for p = 5 (needs vectorised code); no closed form for sigma_p.", "Vectorise the count for p=5, k=4,5 to test stabilisation.")
R('Z0283','interesting',"Slice index E(p) = min over solutions of (4x - p), with x the least denominator: computed exactly for all 2880504 primes = 1 mod 4 below 10^8 (C enumerator; spot-checked by exact sympy at 49 primes incl. all records). Typical E is 3 (90%); E <= 7 for 98.1%; E >= 11 for 1.9-2.8% in every decade (no drift). Records: E = 3,7,11,23,31,59,107 at p = 5,73,1129,1201,21169,118801,8803369; no further record up to 10^8 (max E = 63 on [10^7,10^8)).",
  ['data/z52b/pass2/TO1/Eslice_1e8_summary.txt', S+'es.c', S+'exactE.py'], "Growth law not established: records fit c log^2 p (c in [0.22,0.46]) and an exponential tail P(E>=t) ~ e^{-0.2 t} also fits; 8 records cannot separate them. Only p < 10^8.", "Extend the E-mode to 10^9 with a segmented sieve and test the record scale.")
R('Z0284','interesting',"Same quantity as Z0283 (least slice index E(p) = min(4x-p)): the bounded-slice world with E <= 7 holds for 98.1% of primes = 1 mod 4 below 10^8, and the share with E > E0 falls off roughly exponentially in E0; no limit statement is made. Records grow slowly (E=107 at p = 8803369, 0.42 log^2 p); the 'least E is ~log^2 p' scale of the expected witness count is consistent with the data but not proven.",
  ['data/z52b/pass2/TO1/Eslice_1e8_summary.txt', S+'exactE.py'], "Mordell-type claim (fixed E fails infinitely often) not tested; the growth fit is not decided. Same computation as Z0283.", "As Z0283.")
R('Z0289','nothing',"Built no Dirichlet series; the local factors of the ES count were not computed in this pass (counts are on file: es_100000.tsv).",
  ['BRAINSTORM/anal_dirichlet_series.md'], "Series and its continuation not done.", "Compute partial sums of #ES(n) for n up to 10^5 and the local factors.")
R('Z0294','nothing',"log #ES(p) for primes = 1 mod 4 below 10^5: mean log# = 3.97 / 4.66 / 4.92 in three ranges vs 2 log log p = 4.15 / 4.64 / 4.83, so the mean matches 2 log log p (typical #ES ~ log^2 p). The variance is 0.31 / 0.11 / 0.10, decreasing, not growing like c log log p as an Erdos-Kac heuristic would need.",
  [ES, S+'analyse.py'], "No formal normality test; range too short for a log log p variance trend.", "Repeat on 10^6 with the E-style sampling (counts need full enumeration).")
R('Z0295','nothing',"Degree (= #ES solutions) of each prime p = 1 mod 4 below 10^5: the minimum degree is 2 (p=5), 9 (p=2521 below 10^4), 23 (p=20521 below 10^5); there are no isolated primes (the smallest counts are 2, 4, 4 at p = 5, 13, 17). The Poisson prediction of isolated primes (e^{-lambda}) is irrelevant: the solution counts are far from Poisson.",
  [ES], "Random-graph threshold comparison not quantified beyond this.", "Compare the minimum-degree growth with log^2 p.")
R('Z0297','nothing',"Z[1/l] mechanism rechecked: least k with a found factor = 3 mod 4 of 1+l^k (the Prop 3.2 certificate) is k <= 7 for l < 3000 and k <= 15 for l < 3*10^5 (found certificates). Translation of FF_MUTE Thm 3.5 into the e | 1+eta language was not written.",
  ['scripts/z52b_analogues_zl.py', S+'zlk.py', 'data/z52b/pass2/TO1/zlk_300000.txt'], "Written FF_MUTE translation and elementary FF proof not done.", "Write the FF_MUTE mechanism as an e | 1+eta statement and compare.")
R('Z0298','nothing',"Read EXSET_FUNCTION_FIELD §1.3 (Prop 1.7): the exact-squares result uses q-1 unit shifts for a Weil sum. The integer shift family and its Burgess-range cancellation were not analysed.",
  ['EXSET_FUNCTION_FIELD.md §1.3'], "Integer shift family and cancellation estimate not done.", "Pick multipliers C <= C0 and estimate the sum numerically.")
R('Z0299','nothing',"Read EXSET_FUNCTION_FIELD §7': the monodromy of word covers is a function-field statement. The integer Galois group over Q(n) was not computed.",
  ['EXSET_FUNCTION_FIELD.md §7'], "Galois-group computation not done.", "Compute the Galois group of a small word system with sympy.")
R('Z0300','nothing',"Read EXSET_FUNCTION_FIELD and EXSET_I3 (large-q Poisson-shape model). The integer fit p_f(n) e^{-M_g(n)} with integer shape masses was not run.",
  ['EXSET_FUNCTION_FIELD.md', 'EXSET_I3.md'], "Integer fit not run.", "Fit the shape-mass model to the U(n) exceptional table.")
R('Z0301','covered',"Corrects the item's guess 'char 2 <=> covering': the repo gives the table: finite linear coverings exist for F_4 (FUNCTIONFIELD_ES.md §6.2, 'ES_4(T) is a theorem') and for q=3 (FUNCTIONFIELD_ES (J)4; FF_ODD_ABSENCE Cor 2.3 says q=3^r, r>=2 have none); for char >= 5 none exist for any A (FUNCTIONFIELD_ES.md:331); q=9, 27 and 9-with-T^k none (FF_ODD_ABSENCE Thm 2.2; FF_STERILE_SMALL Thms 3.1, 5.2). Criterion: odd characteristic 3 is special (q=3 yes, q=9,27 no), so 'char 2' is not the criterion.",
  ['FUNCTIONFIELD_ES.md:331', 'FF_ODD_ABSENCE.md Cor 2.3 (line 4)', 'FF_STERILE_SMALL.md Thm 5.2 (line 196)'], "q = 5, 7, 8 not separately tabulated from the cited passages.", "Tabulate q = 5, 7, 8 from FF_STERILE_PUSH.")
R('Z0302','nothing',"Checked FUNCTIONFIELD_ES2.md (q=3 tree data, A = T^2+1 slice tests 28/72 uncovered at (T^2+1)^2). The proposed rule (every ES mechanism gets an F_3[T] translation and a degree <= 15 test) was not applied to any new mechanism.",
  ['FUNCTIONFIELD_ES2.md §10 (lines 29-49)'], "Rule not tested on a new mechanism.", "Apply the rule to the Z[1/l] mechanism at q=3 (not done).")
R('Z0305','nothing',"Premise problem: the item's congruence 4/n = 1/x+1/y+1/z (mod p) has n undefined; with n = p it has a zero denominator mod p. No well-defined H(p) without choosing n. Not computed.",
  [], "Whole item not computed; premise needs fixing (choice of n coprime to the modulus).", "Restate with n = a fixed integer coprime to the modulus p, then compute H(p).")
R('Z0306','nothing',"Signed ES (one negative term) was not computed for n <= 10^4; the repo's SIGNED_REFACTOR.md and BRAINSTORM/s8_signed_genus_wall.md were checked by name only.",
  ['SIGNED_REFACTOR.md'], "Minimal max-denominator of signed representations not computed.", "Write a two-term solver for 4/n + 1/z = 1/x+1/y with z <= C n.")
R('Z0314','nothing',"Read QUATERNION_ES.md by name; norm-slice counting via r4 coefficients not carried out.",
  ['QUATERNION_ES.md'], "r4 slice count not done.", "Compute the r4-weighted slice count for n up to 10^3.")
R('Z0318','nothing',"Certified: for every odd prime l < 3*10^5 a found factor = 3 mod 4 of 1+l^k exists with k <= 15 (histogram 1:22370, 3:3153, 5:391, 7:57, 9:22, 11,13,15: one each). But for l = 12721, 34897, 140473, 185641 etc. the smaller k had unfactored cofactors, so the 'least k' values are only upper bounds and the question of a uniform bound (k <= 7 for all l) is not settled by this data.",
  [S+'zlk.py', 'data/z52b/pass2/TO1/zlk_300000.txt'], "Uniform bound not proved or refuted; cofactors above 10^6 not factored.", "Factor the uncertified cofactors (ECM) for the 25 primes with k >= 9.")
R('Z0319','nothing',"Matched the 2-adic cells: the only realised sorted valuation triples have the top two valuations equal (computed for all 4783 primes, same table as Z0262), which is the tropical cell condition for 4/p at 2. Did not compare with a p-adic tropicalisation at p itself.",
  [ES, S+'analyse.py'], "p-adic cells at p not analysed.", "Repeat the cell match at the target prime p.")
R('Z0320','nothing',"Local obstruction verified in argument: if all denominators are = 1 mod p^k then their reciprocal sum is = 3 mod p^k, a p-adic unit, while 4/p has valuation -1 at p; so the cone 1+p^k Z_p is locally obstructed (not collapsed), as the item says.",
  [], "Not checked numerically (argument only).", "None.")
R('Z0321','nothing',"Adelic density product at 2, p, infinity not computed; the local counts at p (Z0282) are the first input and do not stabilise at k=3 for p=5.",
  [S+'padic.py'], "Product of local densities and comparison with Elsholtz-Tao not done.", "Finish Z0282 to k = 4 and then form the product.")
R('Z0322','nothing',"Not run: the FUNCTIONFIELD_ES2 slice tests cover A = T^2+1 for q = 3 (28/72 units uncovered mod (T^2+1)^2), but the requested FF search over deg P <= 10 with A in {T^2, T^2+1, T^2+T+2} is not in the repo's output files.",
  ['FUNCTIONFIELD_ES2.md:48'], "Requested FF search not run.", "Run the FF search script for q = 3 on the three A values.")
R('Z0325','nothing',"Verified: in characteristic 3, 4 = 1, so 4/P = 1/P and 1/P = 1/(P+1) + 1/(P(P+1)) (check: 1/P - 1/(P+1) = 1/(P(P+1))). Constant numerator 4 is trivial in char 3; only polynomial numerators are faithful.",
  ['BRAINSTORM/ff_erdos_straus.md'], "None.", "None.")
R('Z0328','nothing',"Inheritance direction checked: ES(d) => ES(dk) for all k >= 1 (4/d = sum 1/x_i gives 4/(dk) = sum 1/(k x_i)); the converse direction is not implied. The T1 emptiness at squares is recorded in LEAN_Z1546.md (no_cform_square).",
  ['LEAN_Z1546.md'], "Generation of p-solutions from multiples of p not analysed.", "None.")
R('Z0334','nothing',"FUNCTIONFIELD_ES.md §5 has the FF density-zero rate; a GRH-conditional integer analogue was not searched in the literature in this pass.",
  ['FUNCTIONFIELD_ES.md §5', 'CONDITIONAL_ES.md'], "Literature check and the Bombieri-Vinogradov argument not done.", "arXiv search for conditional ES exceptional-set bounds.")
R('Z0335','nothing',"The eta(p) surrogate families are the same as Z0258: eta = 4Cp is B2 (98.5% covered by C <= 10, d <= 2000); the Pell-unit family is verified in Z0256 (21 primes). No new family tested.",
  [ES, S+'chebotarev.py', S+'quadunit.py'], "Families beyond 4Cp and the Pell unit not tested.", "None beyond Z0258.")
R('Z0337','nothing',"Filter recorded as a checklist note; the brief says it is not applied in this wave.",
  ['POINTWISE_TERNARY.md §3'], "Checklist not applied.", "None.")
R('Z0338','nothing',"Gaussian projection not tested; norm-constrained data (Z0275-Z0276 world) show 40+ failures but no equivariant map was constructed.",
  ['BRAINSTORM/other_rings.md §4'], "Equivariant map not constructed.", "Test real-part projections on Gaussian solutions of 4/p.")
R('Z0346','nothing',"Lemma checked: if all denominators are = 1 mod 4 then their reciprocal sum is = 3 mod 4, a 2-adic unit, while 4/p (p odd) has 2-adic valuation 2. So the sign-restricted world is empty for every odd p: a 2-adic congruence obstruction (B1 type), not a lottery.",
  [], "No numerical check (argument only; the lemma is elementary).", "None.")
R('Z0352','nothing',"Premise: the cone for the Gaussian twin is not fixed in the item and in other_rings §4 only 'open' is recorded. Not enumerated.",
  ['BRAINSTORM/other_rings.md §4'], "Cone undefined; no enumeration.", "Fix the cone (positive real part or Bradford-Ionascu's) and enumerate e with small norm.")
R('Z0360','nothing',"Catalogue entry (sibling problem n = p + 2^a + 2^b; Crocker 1971). The first step asks for the structural input of Crocker's proof; not done here. The repo row is in BRAINSTORM/s9_lower_tail_literature.md.",
  ['BRAINSTORM/s9_lower_tail_literature.md'], "Literature reading not done.", "Read Crocker 1971 for the covering structure.")
R('Z0361','nothing',"Sun's odd three-power conjecture (n = p + 2^a + 2^b + 2^c, n > 8) checked for odd n <= 2*10^5 (sibling calibration, not ES): 0 failures; min count/log^2 n = 0.54 at n = 62447, median 0.93. No ES-side content.",
  [S+'sun.py'], "Extension to 10^9 not done; no ES-side step.", "None for ES.")
R('Z0362','nothing',"Catalogue entry (Sierpinski/covering). No ES-side covering test was run; the repo memo BRAINSTORM/bsE_sierpinski_moving_integer.md has the framing only.",
  ['BRAINSTORM/bsE_sierpinski_moving_integer.md'], "Covering test for ES not run.", "None.")
R('Z0363','nothing',"Catalogue entry (Riesel). The step (direct covering check for 4Cp+1) was not run; the B2 covering numbers (Z0252) are the nearest data.",
  [ES], "Covering check for 4Cp+1 not run as a Riesel-type test.", "Run a Riesel-type covering test on the B2 forms.")
R('Z0364','nothing',"Catalogue entry (Brier numbers). Covering moduli and the ES-side analogue not recorded.",
  ['BRAINSTORM/bsG_even_half.md'], "Not done.", "None.")
R('Z0365','nothing',"Catalogue entry (n - 2^k composite). The comparison note in the item is a difference-in-kind remark; no computation.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0366','nothing',"Catalogue entry (prime + Fibonacci). No Pisano covering test for ES was run.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "Pisano covering test not run.", "None.")
R('Z0367','nothing',"Catalogue entry (Romanoff). Second moment for ES not computed; the counts are on file (es_100000.tsv) so this is feasible.",
  ['BRAINSTORM/z52_lit_thin_pointwise.md'], "Second moment not computed.", "Compute sum over p of #ES(p)^2 / (sum #ES(p))^2 on the 10^5 table.")
R('Z0369','nothing',"Catalogue entry (binary Goldbach). The exception exponent comparison was not applied; no ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "Comparison not applied.", "None.")
R('Z0370','nothing',"Catalogue anchor (ternary Goldbach). No ES-side step by the item's own statement.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0371','nothing',"Catalogue entry (Linnik-Gallagher). No ES-side step.",
  ['B2_ACROSS_FIELDS.md'], "None needed.", "None.")
R('Z0372','nothing',"Difference-of-squares remark at square classes: 4/m^2 = 1/x+1/y+1/z has no certificate line by T1 (Z1546 Lean), so the Hardy-Littlewood reading is the same obstruction. No separate Hardy-Littlewood computation.",
  ['LEAN_Z1546.md'], "Hardy-Littlewood reading not written.", "None.")
R('Z0373','nothing',"Catalogue entry (Lemoine-Levy). No ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0374','nothing',"Catalogue entry (Chen). The 'ES-almost witness' was not formulated; no step run.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "Not done.", "None.")
R('Z0375','nothing',"Catalogue entry (Linnik n = p + x^2 + y^2). No ES-side step.",
  ['BRAINSTORM/s9_lower_tail_literature.md'], "None needed.", "None.")
R('Z0376','nothing',"Catalogue entry (Estermann). No ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0377','nothing',"Catalogue entry (Legendre). No ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0378','nothing',"Bertrand / binomial-coefficient idea: the p-tied integer C(2n,n) with an ES divisor class was not tested.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "Binomial test not run.", "Test whether C(2n,n) for n = (p-1)/2 has a divisor = -1 mod 4C.")
R('Z0380','nothing',"Catalogue entry (Artin). The 'three named families' covering argument was not attempted.",
  ['BRAINSTORM/z44_one_mute_odd.md'], "Not done.", "None.")
R('Z0381','nothing',"Catalogue entry (primitive roots). No ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0382','nothing',"Catalogue entry (p = x^2 + 2y^2 etc). Class-group reformulation of ES not carried out.",
  ['BRAINSTORM/z31_quadratic_forms.md'], "Not done.", "None.")
R('Z0383','nothing',"Catalogue entry (p = x^2 + 27y^2). Ring-class-field criterion for ES not written.",
  ['BRAINSTORM/z35_cubic_jacobi.md'], "Not done.", "None.")
R('Z0384','nothing',"Catalogue entry (p = x^2 + 64y^2, quartic residue). Per-shape residue table not recorded; not done.",
  ['BRAINSTORM/z39_quartic_slices.md'], "Not done.", "None.")
R('Z0386','nothing',"Catalogue entry (Stevenhagen negative Pell). Redei-type invariant for ES not defined.",
  ['BRAINSTORM/bsB_redei_oddpart.md'], "Not done.", "None.")
R('Z0387','nothing',"Catalogue entry (Barrucand-Cohn). Governing-field question for ES shapes not identified.",
  ['BRAINSTORM/nonab_frobenius_redei.md'], "Not done.", "None.")
R('Z0388','nothing',"Catalogue entry (16-rank of Q(sqrt(-2p))). Bilinear-sum transfer not written.",
  ['BRAINSTORM/bsB_redei_oddpart.md'], "Not done.", "None.")
R('Z0392','nothing',"Catalogue entry (Rouse 451). No ES-side step.",
  ['LITERATURE_AUTOMORPHIC.md'], "None needed.", "None.")
R('Z0393','nothing',"Catalogue entry (Lagrange four squares). Prime-to-prime composition not analysed.",
  ['COMPOSITION_ES.md'], "Not done.", "None.")
R('Z0396','nothing',"Catalogue entry (Pollock tetrahedral). No ES-side step.",
  ['BRAINSTORM/z31_small_count_pointwise.md'], "None needed.", "None.")
R('Z0398','nothing',"Catalogue entry (cubes). No ES-side step.",
  ['BRAINSTORM/z31_integral_points_cubics.md'], "None needed.", "None.")
R('Z0399','nothing',"Demjanenko residue classes: the mod-9 remainder comparison was not recorded; not done.",
  ['BRAINSTORM/bsI_tes_cubic_t1.md'], "Not done.", "None.")
R('Z0406','nothing',"Erdos-Selfridge (product of consecutive integers is not a perfect power): proved, wrong direction for a construction; no test.",
  ['BRAINSTORM/z52_deep_thin_pointwise_astra.md'], "None needed.", "None.")
R('Z0407','nothing',"Skolem problem: the p-adic analytic structure of the family C with a divisor of 4Cp+1 in class -1 mod 4C was not examined.",
  ['BRAINSTORM/bsK_skolem_dictionary.md'], "Not done.", "None.")
R('Z0410','covered',"Depth document does the step: EXCEPTIONAL_MN.md §0 Theorem A proves the uniform PW-type bound for every m >= 4 relative to the note (absolute c, C), with the m = 4 case explicit (line 41 and §0), and Cor C/§5 (EXCEPTIONAL_SHORT) gives the short-interval version.",
  ['EXCEPTIONAL_MN.md §0 (Thm A, line 14)', 'EXCEPTIONAL_MN.md §5 (Cor C)'], "Pushing to short intervals around a prime is covered by Cor C, not re-derived here.", "None.")
R('Z0411','nothing',"Catalogue entry (Erdos-Graham colouring, Croot 2003). Repo judged not applicable pointwise; no test.",
  ['BRAINSTORM/z52_lit_thin_pointwise.md'], "None needed.", "None.")
R('Z0412','nothing',"Catalogue entry (Bloom density unit fractions). Parent note downgraded; no ES step.",
  ['BRAINSTORM/addcomb_unit_fraction_density.md'], "None needed.", "None.")
R('Z0414','nothing',"Catalogue entry (Zaremba). The transfer is conditional on unrefereed preprints (ZAREMBA_TRANSFER.md); nothing new computed.",
  ['ZAREMBA_TRANSFER.md'], "Not checked against the preprint.", "None.")
R('Z0415','nothing',"Catalogue entry (Hensley). Alphabet search for the critical exponent not recorded.",
  ['BRAINSTORM/z31_zaremba_thin_orbits.md'], "Not done.", "None.")
R('Z0422','nothing',"Catalogue entry (flea orbits). Completeness open; no ES step.",
  ['ES_APPROACH_GENERATORS.md'], "None needed.", "None.")
R('Z0424','nothing',"Congruent-number root-number parity (Smith): no elliptic curve attached to p was constructed.",
  ['BRAINSTORM/bsB_root_number_parity.md'], "Not done.", "None.")
R('Z0427','nothing',"Idoneal numbers vs Weinberger ternary set; U(n) class-number link not examined.",
  ['BRAINSTORM/bsG_ternary_weinberger.md'], "Not done.", "None.")
R('Z0441','nothing',"Chevalley-Warning / EGZ count-divisibility for an ES-adjacent set: judged to need primality input (B2_ACROSS_FIELDS). Not run.",
  ['B2_ACROSS_FIELDS.md'], "Not done.", "None.")
R('Z0442','nothing',"Combinatorial Nullstellensatz: displayed forms collapse (polynomial_method.md). No test.",
  ['BRAINSTORM/polynomial_method.md'], "Not done.", "None.")
R('Z0443','nothing',"Thue's lemma: covers transparent coset certificates only (LONGSHOT_PIGEONHOLE.md). Not run.",
  ['LONGSHOT_PIGEONHOLE.md'], "Not done.", "None.")
R('Z0444','nothing',"Minkowski / balanced lattice route: left open in the repo; no computation.",
  ['BALANCED_LATTICE.md'], "Not done.", "None.")
R('Z0447','nothing',"Twin primes / bounded gaps: no ES-side step in the item.",
  ['BRAINSTORM/tech_maynard_theta.md'], "None needed.", "None.")
R('Z0451','nothing',"Euler sum-of-powers: elliptic fibration of the ES surface examined in the repo; the link to counterexample regions not recorded and not run.",
  ['BRAINSTORM/elliptic_fibration_es.md'], "Not done.", "None.")
R('Z0458','nothing',"Twin primes in F_q[T] (Sawin-Shusterman): repo note does not carry out a large-q ES statement; not done.",
  ['BRAINSTORM/ff_erdos_straus.md'], "Not done.", "None.")
R('Z0459','nothing',"Bilharz-type argument for Artin over function fields: the Artin analogue was not tested.",
  ['BRAINSTORM/z44_one_mute_odd.md'], "Not done.", "None.")
R('Z0460','nothing',"Feature 'power-size witness reservoir': a merge rule for 4-term solutions was not tested; judged not transferable in BREADTH_Z45.md.",
  ['BREADTH_Z45.md'], "Four-term merge test not run.", "None.")
R('Z0461','nothing',"Fixed-modulus sub-events (B2 with C fixed) on the 1181 primes = 1 mod 24 below 10^5: C=1 alone covers 49%; C=2 alone 59%; cumulative C<=2 81%, C<=3 88%, C<=5 94%, C<=10 97.3%; 32 primes uncovered (409, 577, 2521, 5569, ...). Empirically a handful of fixed C suffices in range.",
  [S+'cover24.py', ES], "Only B2 divisor forms with d <= 2000; no claim about the limit.", "Find the least C for each uncovered prime and its growth.")
R('Z0462','nothing',"Feature 'periodic witness orbit': the reduction to congruence covering (ES_APPROACH_GENERATORS §1) was not tested for ES.",
  ['DEPTH_ASPECT.md'], "Not done.", "None.")
R('Z0464','nothing',"Composition law on targets: quaternion norm compatibility not analysed; not done.",
  ['BM_CORRECTED_COUNT.md'], "Not done.", "None.")
R('Z0465','nothing',"Forced-object test: the fundamental unit of Q(sqrt p) was computed for the 21 primes <= 200 (Z0256); the divisor test on t, u, t±2 for p = 1 mod 24 was not run.",
  [S+'quadunit.py'], "Divisor test on the unit coordinates not run beyond Z0256.", "Run the divisor test on (t, u) for p = 1 mod 24 up to 10^4.")
R('Z0466','nothing',"Binary-form / class-group parametrisation: positivity-constrained version not analysed; not done.",
  ['BRAINSTORM/ident_invariants.md'], "Not done.", "None.")
R('Z0467','nothing',"Heegner-type point construction: cubic-surface domination not settled in the repo; not done here.",
  ['B2_ACROSS_FIELDS.md'], "Not done.", "None.")
R('Z0468','nothing',"Root-number forcing on the ES fibrations: not computed (needs fibre equations).",
  ['BRAINSTORM/bsB_root_number_parity.md'], "Not done.", "None.")
R('Z0469','nothing',"Count residues: #ES(p) mod 2 and mod 3 for primes = 1 mod 4 below 10^5 are equidistributed (mod 2: 2409 vs 2363; mod 3: 1621/1550/1601). No constant residue, so the count-divisibility invariant does not hold for the full solution set.",
  [ES], "Type I/II subsets not split out (only total counts).", "Repeat mod-3 counts for Type I and Type II separately.")
R('Z0471','nothing',"Modular generating function for the ES count: the weighted series and LMFDB-style test were not run; the repo memo has no holomorphic form.",
  ['BRAINSTORM/s9_no_fixed_integer.md'], "Not done.", "None.")

ids = ["Z0252","Z0255","Z0256","Z0258","Z0260","Z0262","Z0263","Z0269","Z0273","Z0274","Z0275","Z0276","Z0280","Z0281","Z0282","Z0283","Z0284","Z0289","Z0294","Z0295","Z0297","Z0298","Z0299","Z0300","Z0301","Z0302","Z0305","Z0306","Z0314","Z0318","Z0319","Z0320","Z0321","Z0322","Z0325","Z0328","Z0334","Z0335","Z0337","Z0338","Z0346","Z0352","Z0360","Z0361","Z0362","Z0363","Z0364","Z0365","Z0366","Z0367","Z0369","Z0370","Z0371","Z0372","Z0373","Z0374","Z0375","Z0376","Z0377","Z0378","Z0380","Z0381","Z0382","Z0383","Z0384","Z0386","Z0387","Z0388","Z0392","Z0393","Z0396","Z0398","Z0399","Z0406","Z0407","Z0410","Z0411","Z0412","Z0414","Z0415","Z0422","Z0424","Z0427","Z0441","Z0442","Z0443","Z0444","Z0447","Z0451","Z0458","Z0459","Z0460","Z0461","Z0462","Z0464","Z0465","Z0466","Z0467","Z0468","Z0469","Z0471"]
if __name__ == '__main__':
    import sys
    batch = [json.loads(l)['mid'] for l in open('data/z52b/pass2/batch_TO1.jsonl')]
    missing = [m for m in batch if m not in rec]
    extra = [m for m in rec if m not in batch]
    print('batch', len(batch), 'recorded', len(rec), 'missing', missing, 'extra', extra)
    # drop the non-batch placeholder
    rec.pop('Z0277', None)
    with open('data/z52b/pass2/outcome_TO1.jsonl','w') as f:
        for m in batch:
            f.write(json.dumps(rec[m], ensure_ascii=False)+'\n')
    from collections import Counter
    print(Counter(rec[m]['outcome'] for m in batch))
