# Writes data/z52b/pass2/outcome_TO2.jsonl (one line per batch item). Outcomes are the verdicts recorded after the
# computations in scripts/z52d_p2_TO2_*.py (+ C helpers) and the repo/literature checks listed in each summary.
import json
B = 'data/z52b/pass2/batch_TO2.jsonl'
O = {}
def o(mid, outcome, summary, evidence, not_done, nxt, prev='none'):
    O[mid] = dict(mid=mid, outcome=outcome, summary=summary, evidence=evidence, not_done=not_done, next=nxt, prev_outcome=prev)
o('Z0472','interesting',
  "Exact R(p) (triples 4uBC-u-B=p) for all 332,180 primes p≡1 (4) ≤1e7. Near-square primes |p-m²|≤10: 3 of the 14 R=0 primes (409, 577, 9601) vs 0.6% of primes (expected ≈0.09): enrichment ≈30x, P≈1e-4. Mean R/log²p: all 0.166, near-square 0.150, p=m²+1 0.122; v2(p-1)≥8: 0 zeros of 5171; Fermat primes 3 (no zeros).",
  ["scripts/z52d_p2_TO2_renum.c","scripts/z52d_p2_TO2_an1.py","data/z52b/pass2/TO2/an1.json","NEAR_SQUARE.md §0 (T1 deformed to near squares)"],
  "Full Type I/II counts for the near-square R=0 primes not computed; no family-level min beyond R=0 found.",
  "Compute f_I, f_II (bs_corr_count) for the 14 R=0 primes and the near-square primes to test whether the enrichment survives in the full families.")
o('Z0473','nothing',
  "arXiv query for prime + three powers of 2 exceptions returned only Goldbach-type papers (e.g. 1308.5492, 2203.02296), none stating a log²-count failure; EXSET_ARITH_JANSON_OPUS.md (at repo root, not BRAINSTORM/) has no Crocker-type discussion by grep. Exact check for p+2^a+2^b+2^c: no odd exception ≤1e7 except n=3 (see Z0512).",
  ["scripts/z52d_p2_TO2_expo.c","data/z52b/pass2/TO2/expo3_1e7_first40.txt"],
  "Crocker 1971 and Sun/Pan full texts not read; the repo pointer BRAINSTORM/EXSET_ARITH_JANSON_OPUS.md is wrong (file is at repo root).",
  "Read the Crocker / Pan papers for the exact exceptional family before any claim about log² counts.")
o('Z0476','covered',
  "ZAREMBA_TRANSFER.md is exactly the thin-orbit pointwise method (SL2 spectral/Zaremba-type) tested on ES in CF coordinates: §1 extracts the method, §2 the ES ladder, §5 the Rickards–Stange reciprocity home, §6 verdict and scope.",
  ["ZAREMBA_TRANSFER.md §§1,2,5,6"], "", "")
o('Z0477','covered',
  "FUNCTIONFIELD_ES.md §5 proves that at fixed q the failure density is 0 as deg P → ∞ (line 189: 'the failure proportion → 0'), and §6.2 proves ES₄(T) is a theorem. The contrast with the q→∞ regime at fixed n (O140 Thm 2.1: failure proportion → 1) is stated in the same file (line 189), so the large-q degeneration is covered.",
  ["FUNCTIONFIELD_ES.md:168-211 (§5), :189, :367"], "", "")
o('Z0478','nothing',
  "Used the repo's exact counts U_m(p) for m=5..48 (primes ≤1e5, data/z52b/raw/m*_pr1e5.txt) and m=4 (primes ≤2e5): m=4 has no prime with U=0 (min U=1 over primes ≤2e5). The failure fraction P(U_m(p)=0) for p∈(1e4,1e5] rises with m (0 for m≤11, 4.5% at m=48), tracking (log p)³/m (Spearman −0.92 over m≥12); R_m·m/(log p)³ itself was not normalised.",
  ["scripts/z52d_p2_TO2_an2.py","data/z52b/pass2/TO2/an2.json"],
  "Normalised R_m·m/(log p)³ not tabulated; m=4 'R_m' is U_4 (the item's R_m is the same unordered count).", "")
o('Z0479','covered',
  "AMPLIFY_EXCEPTION.md enumerates the amplifiers: §1 'this would suffice' theorems, §2 obstruction theorems for classes of laws, §3 constructions and their gates (e.g. §3.2 square law p₀∈E ⇒ p₀²∈E).",
  ["AMPLIFY_EXCEPTION.md §§1–3"], "", "")
o('Z0480','covered',
  "No polynomial identity in p covers the square classes (Mordell–Schinzel), which FRONTIER.md lists among the instances that rule out identity-type routes (FRONTIER.md:194).",
  ["FRONTIER.md:194"], "The (J)10 entry was not located by grep; not checked.", "")
o('Z0481','covered',
  "T1 at odd squares is in FRONTIER.md:48–50 (f_I(m²)=f_II(m²)=0 for odd m; proof lineage ET Prop 1.6, Bright–Loughran). Our check: R(m²)=0 for all 1580 odd squares m² ≤1e7 (the (★) shape), and 780 odd non-square n≤1e7 have R=0 (prime analogue: 14 primes ≡1 (4) with R=0, listed at FRONTIER.md:103).",
  ["FRONTIER.md:48-52, :103", "scripts/z52d_p2_TO2_renum.c", "scripts/z52d_p2_TO2_an1.py"],
  "Full enumeration of all certificate shapes at m² not redone; the (★) check is a subfamily only.", "")
o('Z0482','nothing',
  "CONSTRUCTIVE_ES.md has no digit-recursion analysis (grep 'digit' empty). The cited arXiv:1602.06208 is Cilleruelo–Luca–Baxter 'every positive integer is a sum of three palindromes' — a mis-citation, not a constructive-ES source.",
  ["CONSTRUCTIVE_ES.md (grep)", "arXiv API id 1602.06208"],
  "Whether B1 (no finite ET covering) forbids digit recursion was not analysed.", "Correct the reference and analyse digit recursion in CONSTRUCTIVE_ES terms.")
o('Z0484','nothing',
  "Special-form primes ≤1e7 (p≡1 mod 4): mean R/log²p = 0.166 overall, 0.113 for p≡1 mod 840 (zeros 3/3426 vs 14/332k overall), 0.150 near squares (|p-m²|≤10), 0.161 for v2(p-1)≥8, 0.19 for the 3 Fermat primes. The only structure is the Mordell hard-class deficit already known; no new special family.",
  ["scripts/z52d_p2_TO2_an1.py","data/z52b/pass2/TO2/an1.json"], "Fermat-like families beyond 2^(2^k)+1 not tested.", "")
o('Z0486','covered',
  "STRONG_APPROX_ES.md tests exactly this route: §2 rational recipes make strong approximation idle, §4 even optimal strong approximation is a power too large for the scale window (fibration/fibre-integral version included).",
  ["STRONG_APPROX_ES.md §§2–4"], "", "")
o('Z0487','covered',
  "BRAINSTORM/markoff_hasse_failures_vs_es.md compares the Ghosh–Sarnak (arXiv:1706.06712, verified: HP holds for almost all k and fails for infinitely many k) reduction-theory failures with ES positivity; the memo finds no finite fundamental domain (line 125 says finite-window ratios settle nothing).",
  ["BRAINSTORM/markoff_hasse_failures_vs_es.md:8,125", "arXiv 1706.06712"], "", "")
o('Z0493','nothing',
  "CONDITIONAL_ES.md contains no Dickson-type input (grep 'Dickson' empty), so the proposed input is untried in the repo. No computation can test a conditional input; not run.",
  ["CONDITIONAL_ES.md (grep)"], "The 'Dickson with p fixed' input was not formulated or tested.", "Formulate the auxiliary-variable Dickson input precisely and check which ES reductions it implies.")
o('Z0496','nothing',
  "Vose's O(√log b) construction (ASTRA_BRIEF_DIRECTION2.md cites it) is a 1985 paper not on arXiv; not fetched, so the question 'does it give O(1) terms for 4/p?' was not answered.",
  ["ASTRA_BRIEF_DIRECTION2.md (grep)"], "Vose 1985 not read.", "Obtain Vose 1985 and check the construction for a=4.")
o('Z0499','covered',
  "ES_APPROACH_GENERATORS.md:27 and :65 record Klurman–Shparlinski–Teräväinen (arXiv:2609.25393, verified: almost all q ≤ Q, (log Q)^{1+ε} primes) and the verdict: it is averaging over q, so ES at one tied integer needs Vinogradov's least-QNR input (gate G4).",
  ["ES_APPROACH_GENERATORS.md:27,65", "arXiv 2609.25393"], "", "")
o('Z0500','nothing',
  "Ford's H(x,y,2y) theory describes divisors in dyadic intervals with no residue condition; ES needs divisors ≡ −1 mod 4C of 4Cp+1, so Ford's ladder does not transfer directly. No model of R(p) was fitted (assessment only).",
  [], "Ford's fluctuation model for R(p) not computed.", "")
o('Z0504','nothing',
  "METAPLECTIC_ES.md has no hit for Kummer / Gauss-sum by grep; the cubic Gauss sum route is not in that file. No computation.",
  ["METAPLECTIC_ES.md (grep)"], "Kummer/Heath-Brown–Patterson input not read.", "")
o('Z0510','interesting',
  "Enumerated ALL solutions of 4/n for n≤5000 and tested restrictions. Chains x|y|z: 45 failures, all primes p≡1 mod 24 (45 of 76 such primes ≤5000; first 73, then 193, 313, 337, 409, 577, 2521, 3361). PROVED: for p≡1 (4) a chain solution exists iff (p+1)/2 has a prime factor ≡3 mod 4 (so chain-failure ⇔ p≡1 mod 8 and all prime factors of (p+1)/2 are ≡1 mod 4); verified against the enumeration for all primes ≤5000. Pairwise coprime: impossible for every n (PROVED: S=xy+yz+zx would divide 4 — n≤5000 confirms). Other: squarefree 1199/5000 fail (first 9); exactly-one-even 4374/5000 fail (first 2); all-≡1-mod-4 4688/5000 fail.",
  ["scripts/z52d_p2_TO2_restr.c","data/z52b/pass2/TO2/restr_N5000.txt"],
  "Failure infinitude for the chain variant (heuristically ~x/(log x)^{3/2} primes) not studied; restricted-denominator variants beyond these five not enumerated.",
  "Prove/decide infinitude of primes p with (p+1)/2 composed only of primes ≡1 mod 4 (the chain-variant failure set); then ask whether ES-type statements with divisibility constraints inherit this.")
o('Z0511','interesting',
  "Computed the minimal max-denominator z_min(p) from repo counts for all p≡1 (4) ≤2e5: 74% of primes have z_min > p^{1.5}; 0.35% have z_min > p^{1.75}; none exceed p^{1.9}; the worst exponent is 1.89 (p=1201). So the size-restricted variant z ≤ p^k is satisfied for every p≤2e5 once k ≥ 1.9.",
  ["scripts/z52d_p2_TO2_an6.py","scripts/z52d_p2_TO2_an9.py","data/z52b/pass2/TO2/an6.json","data/z52b/pass2/TO2/an9.json"],
  "Range limited to p≤2e5 (repo count data); the threshold is not proved for large p.",
  "Extend z_min to p≤1e7 with the count program on p≡1 mod 840 and fit the exponent's tail.")
o('Z0512','nothing',
  "Exact check of Crocker-type 'p+2^a+2^b+2^c': every odd n≤1e7 except n=3 is representable (a,b,c≥0; sieve, verified). The cited arXiv:0901.3075 is Z.-W. Sun's 'Mixed sums of primes and other terms' (abstract has no 2^a+2^b+2^c statement); Crocker 1971 is not on arXiv. Crocker's family was not reconstructed, so r₃ on it was not computed.",
  ["scripts/z52d_p2_TO2_expo.c","data/z52b/pass2/TO2/expo3_1e7_first40.txt","arXiv 0901.3075 (abstract)"],
  "Crocker's family and r₃ up to 2^64 not done (sieve-level check only up to 1e7).",
  "Obtain Crocker 1971 and reconstruct his two-power family; then test the three-power extension on it.")
o('Z0513','interesting',
  "Sieve exact count of odd n≤1e8 not of the form p+2^a+2^b (a,b≥0): only n=3 (independently verified ≤2e5 in Python). With a,b≥1 instead: exceptions 3, 5, 6495105 (≤1e8). So odd exceptions are far rarer than the '≫x^{1−ε}' count that BRAINSTORM/s9_lower_tail_literature.md:17 attributes to Pan (Acta Arith. 2011); that statement was not re-verified here, and at this scale there is no exception population to classify.",
  ["scripts/z52d_p2_TO2_expo.c","data/z52b/pass2/TO2/expo2_1e7_first40.txt","data/z52b/pass2/TO2/expo2_1e8_first40.txt","data/z52b/pass2/TO2/expo2e1_1e8.txt"],
  "Pan 2011 not read; the conflict with a claimed ≫x^{1−ε} exception count must be resolved (normalisation of a,b or of p).",
  "Read Pan (Acta Arith. 148, 2011) to fix the normalisation; then recheck the exception count.")
o('Z0514','nothing',
  "Reproduced the Pomerance–Weingartner largest exceptions from repo data (primes ≤1e5): m=8: 241, m=12: 12241, m=15: 20521. Largest-exception scale (log p)³/m is 20.6 (m=8), 69.5 (m=12), 65.3 (m=15), 91 (m=16), 74 (m=20), 63 (m=24): not constant. A fit against exp(c√m) to 3 points is not meaningful, so none was reported.",
  ["scripts/z52d_p2_TO2_an2.py","scripts/z52d_p2_TO2_an3.py","data/z52b/pass2/TO2/an3.json"],
  "Fit of the Schinzel growth exponent with more m and larger p not done.", "")
o('Z0515','nothing',
  "m=12 has 9 failing primes in (1e3,1e5] while m=11,13,14 have 0 and m=15 has 8. Across m≥12 the failure count tracks (log p)³/m (Spearman −0.92), with τ(m) +0.40 and φ(m)/m −0.18. The anomaly is therefore mostly size-driven; no singular-series model E_m(p) was computed.",
  ["scripts/z52d_p2_TO2_an3.py","data/z52b/pass2/TO2/an3.json"],
  "Heuristic expected counts E_m(p) from local densities not computed.", "")
o('Z0516','nothing',
  "arXiv query for 'sums of three cubes integral Hasse' returned no hits; the cited Colliot-Thélène–Wittenberg paper was not read. No computation for k≢±4 mod 9.",
  [], "Literature check on non-BM integral failures for x³+y³+z³=k not completed.", "Fetch Colliot-Thélène–Wittenberg (2012) and check the BM-only statement.")
o('Z0518','nothing',
  "Not run: the search for ES over totally positive integers of Q(√2)/Q(√5) was not implemented in this pass.",
  [], "Totally positive ES over real quadratic K not searched (the item's bounded search).", "Implement a bounded search for ν=p (p≡1 mod 4 split/inert) in Z[√2].")
o('Z0519','nothing',
  "Premise is false as stated: 4/p has reduced denominator p, so p divides lcm(x,y,z) and some denominator is ≥ p. Hence no solution has x,y,z all y-smooth with y < p; the 'smooth ES' question must be posed for the p-free cofactors instead.",
  ["PROVED elementary (denominator argument)"],
  "Cofactor version (largest prime factor of x/p-part) not computed.",
  "Redefine as cofactor smoothness of Type I/II solutions and compute its minimal value for p≤1e6.")
o('Z0521','interesting',
  "Over all primes p≡1 (4), 5<p≤2e5 with repo counts: x_min − p/4 ≤ 0.114 log²p (median 0.006 log²p), x_min/p in [0.250, 0.308], and x_min − p/4 ≤ √p in every case. The smallest admissible denominator is in a very short window above p/4.",
  ["scripts/z52d_p2_TO2_an6.py","data/z52b/pass2/TO2/an6.json"],
  "Only p≤2e5; no proof that the window is O(log²p).",
  "Test the window on p up to 1e6 (window data) and relate x_min to the Type II parameter.")
o('Z0522','nothing',
  "arXiv:2405.08650 (Jain–Pham–Sawhney–Zakharov, 'An explicit economical additive basis') gives an explicit basis with N^{ε}-type representation counts, not r(n)≍log n; so the item's premise (explicit log-count bases) is not what this paper proves.",
  ["arXiv 2405.08650 (abstract)"], "Full text not read.", "Correct the item's reference; search for explicit thin bases with log-type counts.")
o('Z0523','nothing',
  "arXiv query for 'Zaremba critical exponent 1/2' returned no hits; Bourgain–Kontorovich 2014 not re-read. No computation.",
  [], "Critical-dimension Zaremba alphabet not computed.", "")
o('Z0525','nothing',
  "Same literature item as Z0496 (Erdős log log b conjecture, Vose 1985): the paper is not on arXiv and was not fetched.",
  ["ASTRA_BRIEF_DIRECTION2.md (grep)"], "Vose 1985 and Tenenbaum–Yokota not read.", "")
o('Z0527','nothing',
  "arXiv:2511.16817 (Pomerance–Weingartner, 'Exceptions to the ES–Schinzel conjecture', verified abstract) gives n_m ≥ exp(m^{1/3+o(1)}), an explicit m ≥ 6.52e9 theorem and numerics supporting m ≥ 20. Repo counts show P(U_m(p)=0) for p∈(1e4,1e5] rising smoothly from 0 to 4.5% as m goes 11→48: an empirical intermediate regime, not a proof of one.",
  ["arXiv 2511.16817 (abstract)","data/z52b/pass2/TO2/an2.json"],
  "Full text of PW not read; provable intermediate regime not identified.", "")
o('Z0528','nothing',
  "Exact Type I and Type II counts (bs_corr_count.c) for all 9,732 primes p≡1 mod 24 ≤1e6: no prime with f_I=0 or f_II=0; min f_I/log³p = 0.0125, min f_II/log³p = 0.0037 (at p=193). The 14 (★)-failures are not failures of the full Type II family. p=232792561 (prime): f_I=254, f_II=111.",
  ["scripts/z52d_p2_TO2_fIfII.sh","data/z52b/pass2/TO2/fIfII_p24_1e6.txt","data/z52b/pass2/TO2/an7.json"],
  "Range ≤1e6 (not 1e8); the 1e8 claim in FRONTIER:35 is cited, not re-run.", "")
o('Z0531','covered',
  "BRAINSTORM/corr_typeI_typeII_joint.md §4 measured corr(log f_I, log f_II) = +0.75 (Spearman 0.72) and found no negative coupling. Re-check with our 9,732 exact pairs (p≡1 mod 24 ≤1e6): Pearson of logs +0.88, residual after log p quadratic +0.75, bottom-5% joint 384 observed vs 27 independent.",
  ["BRAINSTORM/corr_typeI_typeII_joint.md §4", "data/z52b/pass2/TO2/an7.json"], "", "")
o('Z0532','nothing',
  "The divisor-in-class form R(p)=Σ_C #{d | 4Cp+1 : d ≡ −1 mod 4C} is already FRONTIER.md:92. Applying Halász/Matomäki–Radziwiłł bounds to it was not attempted.",
  ["FRONTIER.md:92"], "Multiplicative-function (Halász-type) estimate not done.", "")
o('Z0533','nothing',
  "The item leaves the operation T undefined. The only operation that is provably closed is scaling (4/(nm) solvable if 4/n is), which gives no descent; no candidate T was tested.",
  ["PROVED elementary"], "A concrete descent map T(p) was not proposed or tested.", "Propose T (e.g. a prime factor of 4p+1 in a fixed class) and test lifting numerically.")
o('Z0534','interesting',
  "Minimal Type-II (★) modulus C_min(p) over all primes p≡1 (4) ≤1e7: 99% have C_min ≤ 0.036 log²p, but the tail is heavy: max C_min/log²p = 157 at p=184837 with C_min = 23105 ≈ p/8 (the only (★) witness is (u,B)=(1,2)). So no Linnik-type polylog bound holds for the (★) subfamily.",
  ["scripts/z52d_p2_TO2_renum.c","scripts/z52d_p2_TO2_an1.py","data/z52b/pass2/TO2/an1.json"],
  "Minimal parameter for the full Type I ∪ II families was not computed.",
  "Compute min over Type I and Type II witnesses (f_I, f_II shapes) of the modulus, same range.")
o('Z0538','covered',
  "SIBLING.md tests sideways reductions directly: §2 finds siblings never share a key, so the reduction stops at 'few keys per parent' (SIBLING.md:18); §4 records the conditional statements.",
  ["SIBLING.md:18, §4"], "", "")
o('Z0540','nothing',
  "The taxonomy (13 classes, 23 catalogue entries) is in BRAINSTORM/z52_deep_thin_pointwise_astra.md. A search for other harmonic-profile problems was not done.",
  ["BRAINSTORM/z52_deep_thin_pointwise_astra.md"], "Literature search for harmonic-profile problems not run.", "")
o('Z0542','nothing',
  "Admissibility of the forms 1+4p·h_i·t: every form equals 1 at t≡0 mod every prime, so the tuple is always admissible (PROVED, elementary). Maynard-type sieving therefore gives almost-primality of the N_{C_i}, which carries no information about a divisor ≡ −1 mod 4C_i.",
  ["PROVED elementary"], "No computation over a specific h-tuple.", "")
o('Z0543','interesting',
  "Residue-level Type I coverage: for p≡1 mod 24 ≤1e6, the classes −f mod 4ad (f | 4a²d+1) over a≤50 cover 50.5% of primes with d≤5, 69.8% with d≤10, 95.8% with d≤20, 99.5% with d≤50. (Upper bound on exact coverage; exact when f ≤ p/2, which holds for most of the range.)",
  ["scripts/z52d_p2_TO2_an8.py","data/z52b/pass2/TO2/an8.json"],
  "The uncovered 0.5% not characterised; b≥a condition only approximated.",
  "Characterise the uncovered primes (d≤50) and check whether they are the (★)-zero primes.")
o('Z0544','nothing',
  "Duke's equidistribution error terms were not extracted from the 1988 paper; no comparison with the d-window was made.",
  [], "Duke 1988 not read; error-window comparison not done.", "")
o('Z0546','nothing',
  "MODP_RECIPROCITY.md and TWISTED_T1.md contain no simultaneous multi-C reciprocity statement (grep). The multi-C contradiction was not attempted.",
  ["MODP_RECIPROCITY.md, TWISTED_T1.md (grep)"], "Multi-C reciprocity argument not attempted.", "")
o('Z0550','nothing','Assessment only: the log Kodaira dimension and boundary of the ES fibre were not computed.', [], "Not computed.", "")
o('Z0551','nothing',
  "The count R(p) is the lattice count of the cubic surface 4uBC−u−B=p, not a quadric; no region R_p with volume matching R(p) was identified.",
  ["PROVED (form of the equation)"], "Region R_p and volume not computed.", "")
o('Z0552','nothing',
  "The Mordell–Schinzel square-class obstruction is known (FRONTIER.md:194); the thin-set image of the ES integral points was not analysed and no multisection was constructed.",
  ["FRONTIER.md:194"], "Growing-degree multisection not analysed.", "")
o('Z0555','nothing',
  "Premise check: the projective closure of the ES fibre 4xyz = n·w·(xy+yz+zx) is a cubic surface, as the item says. Its rationality over Q and any modular parametrisation were not checked.",
  [], "Rationality and Heegner curves not computed.", "")
o('Z0556','nothing',
  "Counted T(n)=#{(t,u,v)≥1: tuv−u−v=n} for n≤1e5: T is odd for 3797 of 4166 primes p≡1 mod 24 (so the unrestricted count gives no parity involution). With my reading of the restriction (some coordinate in 4Z ∪ (8Z−n)), the count is odd for only 149/4166 (ambiguous reading; not a theorem).",
  ["scripts/z52d_p2_TO2_i3.c"], "Coordinate-restriction reading to be confirmed against WINDMILL.md.", "")
o('Z0559','interesting',
  "Using repo counts U_m(p) (m=5..48, primes ∈(1e4,1e5]): log P(U_m(p)=0) ≈ −2.75 − 0.071·(log p)³/m (R²=0.58 over the 33 m with failures). The slope is consistent with a Poisson-type exponent; the intercept shows it is not a pure Poisson law. Extrapolated to m=4 this predicts no ES failures in this range, consistent with data.",
  ["scripts/z52d_p2_TO2_an2.py","data/z52b/pass2/TO2/an2.json"],
  "Fit on m≥12 only (m≤11 has no failures); no independent validation set.", "Fit P(U=0) with the m-family at p≤1e6 (window data) to test the slope.")
o('Z0560','nothing','Not computed: homogeneous-dynamics model of exceptional primes not constructed.', [], "Not done.", "")
o('Z0565','nothing',
  "Class numbers h(−4p) for all 8,976 primes p≡1 (4) ≤2e5 (C reduced-form count). Mean R/log²p by h(−4p) mod 8: 0.171 (0), 0.176 (2), 0.169 (4), 0.177 (6). No dependence; the 2-power class group does not visibly control (★) counts. R=0 primes: 6 with h≡0, 1 with h≡4 mod 8.",
  ["scripts/z52d_p2_TO2_hD.c","data/z52b/pass2/TO2/hD_p1mod4_2e5.txt","data/z52b/pass2/TO2/an7.json"],
  "Tabulation of minimal certificate shapes by h(−4p) mod 8 not done.", "")
o('Z0566','interesting',
  "Smallest m∈[5,48] with a prime p∈(m²,2m²) for which m/p is not a sum of three unit fractions: m=10, p=181 (verified by exact brute force: no solutions). 37 of the 44 m∈[5,48] have failing primes in (m²,2m²) (p≤1e5); none for m∈{5,6,7,8,9,11,19}. This is below the m≥20 numerical threshold PW state, though PW's theorem is for m≥6.52e9.",
  ["scripts/z52d_p2_TO2_an2.py","data/z52b/pass2/TO2/an2.json","arXiv 2511.16817 (abstract)"],
  "Explicit proven threshold 6.52e9 not revisited; j-term not studied.", "")
o('Z0567','nothing',
  "The abstract of arXiv:2511.16817 states a j-unit-fraction generalisation; the transition curve in (m, j) was not extracted (full text not read).",
  ["arXiv 2511.16817 (abstract)"], "j-term section not read.", "Read the j-term section and extract the transition curve.")
o('Z0575','nothing','Item first_step is "None" and the question concerns k·2^n+1 primes, not ES; nothing computed.', [], "Not done (not ES-relevant per repo).", "")
o('Z0579','nothing',
  "Least primitive root g(p) for all 9,462 primes p≡1 (4) ≤2e5: Spearman with U(p) = −0.42 (same sign as least-QNR). No ES step is provided by the item.",
  ["scripts/z52d_p2_TO2_an9.py","data/z52b/pass2/TO2/an9.json"], "Conditional GRH bounds not revisited.", "")
o('Z0580','nothing',
  "Least QNR n(p) ≤29 for all p≡1 (4) ≤2e5; Spearman with U(p) = −0.48 (tie-aware). The Vinogradov conjecture itself is not addressed; ES_APPROACH_GENERATORS.md:65 already notes that beating KST needs it.",
  ["scripts/z52d_p2_TO2_an9.py","data/z52b/pass2/TO2/an9.json","ES_APPROACH_GENERATORS.md:65"], "No new step.", "")
o('Z0587','nothing',
  "Darmon–Granville concerns Fermat-type S-unit equations; the ES equation 4xyz=n(xy+yz+zx) has no comparable signature. No orbifold computation.",
  [], "Orbifold signature not computed.", "")
o('Z0588','nothing',
  "BRAINSTORM/padic_adelic_scaling.md examined Campana points on the boundary but did not establish them. The cited Pieropan–Smeets–Tanimoto–Várilly-Alvarado paper was not checked.",
  ["BRAINSTORM/padic_adelic_scaling.md (grep)"], "Literature check not done.", "")
o('Z0590','nothing',
  "Literal duplicate of the Crocker/Between step (Z0512/Z0513), so it is handled there: a,b≥0 gives only n=3 odd exceptions to 1e8; a,b≥1 gives {3,5,6495105}.",
  ["data/z52b/pass2/TO2/expo2_1e8_first40.txt","data/z52b/pass2/TO2/expo2e1_1e8.txt"],
  "Minimal-pair assessment not written beyond the duplicate.", "")
o('Z0591','nothing',
  "Alphabet {2,4,6,8,10} has all partial quotients even (parity obstruction to Zaremba-type denominators), while {1..5} has no such congruence obstruction. No ES computation; the z31 memo covers the Zaremba side.",
  ["BRAINSTORM/z31_zaremba_thin_orbits.md (not re-read)"], "Not computed.", "")
o('Z0592','nothing',
  "Same calibration as Z0559 (m-family counts, U_m(p) for p≤1e5): the ratio (log p)³/m governs the failure rate; m=4 has no failures to 2e5.",
  ["data/z52b/pass2/TO2/an2.json"], "Large-m extremal primes not computed.", "")
o('Z0595','covered',
  "BRAINSTORM/z31_markoff_chen.md contrasts Markoff mod-p (strong approximation + Chen's divisibility) with the integral Hasse failures (Ghosh–Sarnak, verified arXiv:1706.06712). The ES analogue is not settled there, which the item states.",
  ["BRAINSTORM/z31_markoff_chen.md:1-8", "arXiv 1706.06712"], "", "")
o('Z0596','nothing',
  "Premise checked: negative Pell x²−py²=−1 is solvable for every prime p≡1 mod 4 (Legendre), so the pointwise claim holds; for general d only density results are classical. The 'hardest yet proved' question was not answered.",
  [], "No computation; literature not searched for hardest-prime results.", "")
o('Z0598','covered',
  "BRAINSTORM/apollonian_reciprocity.md uses HKRS (arXiv:2307.02749, verified abstract: local–global for Apollonian packings is false via quadratic/quartic reciprocity, Brauer–Manin-like) as the analogue, and records the ES comparison.",
  ["BRAINSTORM/apollonian_reciprocity.md:1-5", "arXiv 2307.02749"], "", "")
o('Z0602','nothing','Romanoff-type density contrast; no ES step; not computed.', [], "Not done.", "")
o('Z0606','nothing',
  "UNIT_ORBIT_ES.md has no Vieta/Geiser/involution hit by grep; the symmetry question for the ES solution set was not tested on solutions.",
  ["UNIT_ORBIT_ES.md (grep)"], "Vieta moves on repo solutions not tested.", "Apply x ↦ 1/(4/n−1/y−1/z) to the solution lists for p≤1e4 and count integral outputs.")
o('Z0608','nothing',
  "Mordell–Schinzel rules out polynomial identities in p alone (FRONTIER.md:194). The identity search in a,b for n=a²+b² was not run; ident_numerators.md has no such search (grep).",
  ["FRONTIER.md:194", "BRAINSTORM/ident_numerators.md (grep)"], "Symbolic identity search not run.", "")
o('Z0610','nothing',
  "Minimal denominator x_min always lies within p/4 + 0.114 log²p (p≤2e5), so the 'x near p' regime does not host minimal denominators. The correlation between size regimes of all solutions was not computed.",
  ["data/z52b/pass2/TO2/an6.json"], "Regime correlations for all solutions not computed.", "")
o('Z0613','nothing',
  "R(n) is even for every odd n≤1e7 (computed). Elementary reason: the swap (u,B) has fixed points only when n=2u(2uC−1), which is even, so there are none for odd n.",
  ["scripts/z52d_p2_TO2_renum.c","data/z52b/pass2/TO2/an1.json"], "", "")
o('Z0614','nothing','Rickards–Stange fixed-target cancellation not computed; BRAINSTORM/z36_reciprocity_obstruction_home.md not re-read.', [], "Not done.", "")
o('Z0616','interesting',
  "Slice events E_C(p) = [slice C carries a (★) triple], C=1..8, over 39,174 primes p≡1 (4) ≤1e6: P(E_1)=0.76, P(E_2)=0.51. Pairwise correlations are small: mean off-diagonal −0.016; E_1 vs E_2 = −0.14 overall and −0.13 to −0.21 within size windows (the 'negative correlation' lead). P(no slice ≤8 hit) = 1.3%.",
  ["scripts/z52d_p2_TO2_mask.c","scripts/z52d_p2_TO2_an8.py","data/z52b/pass2/TO2/an8.json"],
  "Correlations for the Type I events not included; size-regime effects only partly removed.",
  "Test whether negative E_1–E_2 correlation survives conditioning on p mod 8 and on the Type I count.")
o('Z0617','nothing','erdosproblems.com not scraped; the audit file sources/lit2026/audit-erdosproblems-242-2026-10-04.md exists and was not re-verified.', [], "Scrape and tag review not done.", "")
o('Z0624','nothing',
  "Minimal max-denominator z_min(p) ≤ 0.50 p² for all p≡1 (4) ≤2e5 (max at p=577), median 0.006 p².",
  ["scripts/z52d_p2_TO2_an6.py","data/z52b/pass2/TO2/an6.json"], "Proof of a general z ≤ C n² bound not attempted.", "")
o('Z0627','nothing','Parity-type sieve model not constructed; the item is vague and no sieve axioms were checked.', [], "Not done.", "")
o('Z0628','interesting',
  "Distribution of R(p) (ordered count, always even) for p≡1 mod 24: variance/mean = 3.66 on [1e5,1e6) and 4.13 on [1e6,1e7). Since R = 2·(unordered), the unordered count has variance/mean ≈ 1.83 and 2.06, i.e. over-dispersed relative to Poisson (≈1). Clustering comes from the C-slices.",
  ["scripts/z52d_p2_TO2_an1.py","data/z52b/pass2/TO2/an1.json"],
  "Full distributional fit (negative binomial, Kubilius moments) not done.", "Fit a negative-binomial to the unordered counts per C-slice.")
o('Z0629','nothing','Same data as Z0628 (variance/mean of R over p≡1 mod 24 windows): over-dispersion ≈2 for unordered counts; no separate Erdős–Kac statistic computed.', ["data/z52b/pass2/TO2/an1.json"], "Erdős–Kac-type statistic not computed.", "")
o('Z0630','nothing','Literature survey of covering systems not done; no prime-covering by APs can cover all primes (assessment).', [], "Not done.", "")
o('Z0631','covered',
  "BRAINSTORM/z52_lit_unitfrac_cover.md screened Balister–Bollobás–Morris–Sahasrabudhe–Tiba (arXiv:1811.03547) and the distortion method (covering_distortion_dual.md); the memo records no campaign verdict change.",
  ["BRAINSTORM/z52_lit_unitfrac_cover.md:7,21"], "", "")
o('Z0632','nothing','BALANCED_LATTICE.md and LONGSHOT_PIGEONHOLE.md not checked for the exact congruence/Thue form; no computation.', [], "Not done.", "")
o('Z0633','nothing','Calibration item; no ES step. Covered in the literature memo (BRAINSTORM/s9_lower_tail_literature.md) by reference only.', [], "Not done.", "")
o('Z0638','nothing','S-integral ES (ℤ[1/S]) not tested; BRAINSTORM/bsK_sunit_limit.md not re-read.', [], "Not done.", "")
o('Z0639','covered',
  "BRAINSTORM/s8_signed_genus_wall.md (§0) treats the signed/negative-denominator variant: positivity is the genus wall and there is no |d|-preserving signed→positive move. That is the memo's answer to the item's question.",
  ["BRAINSTORM/s8_signed_genus_wall.md:1-4"], "Explicit identities for 4/p = 1/x+1/y−1/z not written out.", "")
o('Z0640','nothing','bsA_farey_graph_metric.md has no ES₅ word-path check by grep; not re-computed.', [], "Not done.", "")
o('Z0647','nothing',
  "Proved: the solvable set is closed under multiples (4/(nm) = (1/m)·4/n), so an exceptional prime p with p^k exceptional forces p exceptional. This gives no infinitude statement for the exceptional set.",
  ["PROVED elementary"], "Infinitude of the exceptional set not decided.", "")
o('Z0648','nothing',
  "Mean R/log²p on p≡1 mod 24 (p>1e4) split by (p/11), (p/13), (p/17), (p/19): differences ≤5% with inconsistent signs (e.g. (p/17)=+1 higher, (p/11)=+1 lower); R=0 counts too small to split.",
  ["scripts/z52d_p2_TO2_an1.py","data/z52b/pass2/TO2/an1.json"], "Split on p≡1 mod 840 not done.", "")
o('Z0649','nothing','Character-escape list not compiled; the Type I (d/p)=−1 condition is tested under Z0673.', [], "Not done.", "")
o('Z0652','nothing','H4_NOT_POLYLOG.md proves κ-bounds on H4(p), not the exp((ln x/c)^{1/3}) prediction; the Salez / Mihnea–Dumitru family-size data is not in the repo.', ["H4_NOT_POLYLOG.md:10,40"], "Prediction not tested.", "")
o('Z0654','nothing','Least-family size s(p) is not in the repo data; the near-square R=0 enrichment is reported under Z0472.', [], "Least-family records not tabulated.", "")
o('Z0660','nothing','arXiv query for Erdős–Hall divisors in residue classes returned nothing; no computation.', [], "Literature not found.", "")
o('Z0673','interesting',
  "Numerical test of the claim 'Type I at (a,d) needs (d/p) = −1': over 1038 primes p≡1 mod 24 in [1e4,1e5] and all a,d≤50 (witnesses f|4a²d+1, f≡−p mod 4ad, f≤p/2, b≥a), 13,311 witnesses, with (d/p)=+1 in 0 cases. The claim is not recorded in T1_TEMPLATE.md (grep '(d/p)' empty), so the item's premise is only partly right.",
  ["scripts/z52d_p2_TO2_dp.py"],
  "No proof of the necessity; tested only for d≤50, a≤50, p<1e5.",
  "Prove the necessity (likely via reciprocity on f | 4a²d+1) and record it in T1_TEMPLATE.md.")
o('Z0676','nothing','OEIS A192787: repo cache (data/z52b/oeis_cache.json) and the earlier audit record cite only Vaughan; the entry was not re-fetched.', ["data/z52b/oeis_cache.json"], "Not re-fetched.", "")
o('Z0677','nothing','OEIS A073101 not re-fetched; no D(n) bound comparison made.', [], "Not done.", "")
o('Z0681','interesting',
  "Verified: O(n) (ordered solutions of 4/n) is odd exactly when n≡2 mod 4, for all 2≤n≤30000 (0 mismatches in the repo count output). Parity of U(n) itself is ~50/50 on n≡2 mod 4, so only O has the law.",
  ["data/z52b/raw/f4_all_30000.txt (column O)"],
  "The isosceles-count proof (via (4x−2n)(4z−n)=2n²) not written.",
  "Prove O ≡ n/2+... mod 2 from the isosceles and equilateral counts, and check whether it extends to 6-fold orbit counts.")
o('Z0683','nothing',
  "Primes with U(p) ≤ 4 (p≤2e5): {2, 3, 5, 13, 17} exactly. Minimum U over the 1e6 window is 116 and over the 1e7 window 229; min U/log²p is 0.61 (1e6 window) and 0.88 (1e7 window).",
  ["scripts/z52d_p2_TO2_an4.py","data/z52b/pass2/TO2/an4.json"], "Fit of min U over dyadic windows not done.", "")
o('Z0684','nothing',
  "Least prime with U=6 is 193 (verified). Least primes for other small values: U=2:5, 3:3, 4:13, 7:7, 8:97, 9:11, 10:89, 11:19. Enrichment in p≡1 mod 24 and the Type-A classification were not checked.",
  ["data/z52b/pass2/TO2/an4.json"], "Type-A label and m/p failure-set enrichment not checked.", "")
o('Z0685','nothing',
  "Record lows of U(p)/log²p among primes p≥50 are 53, 61, 73, 193, 2521 (verified; with p<50 the records are 3,5,13,17). No new record in the 1e6 or 1e7 windows (min ratios 0.61 and 0.88). Extension to 1e7 by the count program was not run.",
  ["scripts/z52d_p2_TO2_an4.py","data/z52b/pass2/TO2/an4.json"],
  "Full 1e7 extension (p≡1 mod 840 pre-filter) not run within this pass.", "Run the count program on p≡1 mod 840, p≤1e7 (about 3.4k primes) on 3 cores.")
o('Z0686','nothing',
  "232792561 = lcm(1..19)+1 is prime (Miller–Rabin, 12 bases). R(232792561) = 22 (≥1, so not a (★) failure). Exact f_I = 254, f_II = 111. U was not computed; the b=1 (López Type A) test was not run.",
  ["scripts/z52d_p2_TO2_rsingle.c","data/z52b/pass2/TO2/fIfII_232792561.txt"],
  "U(232792561) and the b=1 test not computed.", "Compute U with the count program (≈ hours) or the word sieve.")
o('Z0689','nothing','BRAINSTORM/s7_lvalue_proxy.md defines the Euler-product proxy P(p)=∏(1−(p/ℓ)/ℓ)^{-1}; the heuristic E U(p) ≈ c(log p)²F(χ_p) was not derived.', ["BRAINSTORM/s7_lvalue_proxy.md:5"], "Derivation not done.", "")
o('Z0690','nothing',
  "Per-q regression of log U(p) on −log(1−(p/q)/q) (p≡1 mod 4, 1000<p≤2e5, n=9,383): coefficients q=2: −0.30, 3: −0.30, 5: −0.46, 7: −0.11, 11: −0.35, 13: −0.06, plus 2.9·loglog p; R²=0.73. The weights are not uniform and collinearity is not controlled; not compared with Elsholtz–Tao local densities.",
  ["scripts/z52d_p2_TO2_an5.py","data/z52b/pass2/TO2/an5.json"], "Collinearity check and ET local-density comparison not done.", "")
o('Z0691','covered',
  "Zero-count check: k1 (exactly one denominator divisible by p) and k2 (exactly two) are ≥1 for every prime ≤2e5, so no 'min(k1,k2)=0' case exists. Correlation is positive (Pearson 0.81, Spearman 0.79 for p≡1 mod 4), as recorded in BRAINSTORM/corr_typeI_typeII_joint.md §4.",
  ["scripts/z52d_p2_TO2_an4.py","data/z52b/pass2/TO2/an4.json","BRAINSTORM/corr_typeI_typeII_joint.md §4"], "", "")
o('Z0692','interesting',
  "Over 8,969 primes p≡1 mod 4 ≤2e5: log R(p) regressed on log p and log h(−4p) gives slope 0.396 on log h (R² 0.36, vs 0.21 for log p alone), i.e. the (★) count scales like L(1,χ_{−4p})^{0.4} at fixed size. Adding h(−8p) and h(−3p) raises R² only to 0.38 (coefficients 0.13, 0.08), so {−4} is the essential twist.",
  ["scripts/z52d_p2_TO2_an5.py","data/z52b/pass2/TO2/an5.json","data/z52b/pass2/TO2/hD_p1mod4_2e5.txt"],
  "Only p≤2e5; not tested against the full Type I count.",
  "Test whether the L(1,χ_{−4p}) effect survives for the full f_II count (not only R) on the same primes.")
o('Z0696','nothing',
  "Tie-aware Spearman over p≡1 mod 4 ≤2e5: U(p) vs #QNR ≤ log p = +0.66, k1 vs #QNR ≤ log p = +0.68, log U vs #QNR Pearson +0.66; U vs least QNR = −0.48 (the earlier −0.40 used tie-naive ranks). This partially supports 'main term scales with #QNR' but does not write the Type-I count as a QNR sum.",
  ["scripts/z52d_p2_TO2_an9.py","data/z52b/pass2/TO2/an9.json"],
  "Exact QNR-sum representation of Type I not derived.", "")
rows = [json.loads(l) for l in open(B)]
missing = [r['mid'] for r in rows if r['mid'] not in O]
extra = [m for m in O if m not in {r['mid'] for r in rows}]
print('batch', len(rows), 'outcomes', len(O), 'missing', missing, 'extra', extra)
with open('data/z52b/pass2/outcome_TO2.jsonl', 'w') as f:
    for r in rows:
        f.write(json.dumps(O[r['mid']], ensure_ascii=False) + '\n')
from collections import Counter
print(Counter(O[r['mid']]['outcome'] for r in rows))
