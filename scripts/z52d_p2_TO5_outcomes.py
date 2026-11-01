"""z52d_p2_TO5_outcomes.py — writes data/z52b/pass2/outcome_TO5.jsonl (one line per batch_TO5 input, checked).
Outcome texts were written after running the scripts listed in 'evidence'. Run: python3 scripts/z52d_p2_TO5_outcomes.py"""
import json
B='data/z52b/pass2/batch_TO5.jsonl'; OUT='data/z52b/pass2/outcome_TO5.jsonl'
S='scripts/z52d_p2_TO5_'; DAT='data/z52b/pass2/TO5/'
A=lambda: None
O={}
def add(mid,outcome,summary,evidence,not_done,nxt):
    assert outcome in ('nothing','covered','interesting','needs-compute','skipped')
    O[mid]=dict(mid=mid,outcome=outcome,summary=summary,evidence=evidence,not_done=not_done,next=nxt,prev_outcome='none')

add('Z1679','nothing',
 "Computed a_p for the conductor-11 (11a) and conductor-37 (37a) elliptic newforms (a_p = -sum_x (f(x)/p), checked against known a_2,a_3,a_5,a_7,a_13) and correlated a_p/sqrt(p) with the BM residual (R-M_BM)/sqrt(M_BM) over the 8977 primes p≡1 (mod 4), p≤2·10^5: r = +0.0007 (11a) and -0.0127 (37a), |r| ≈ 1.2 standard errors. No Hecke-type correlation.",
 [S+'hecke.py',DAT+'mbm_1e6.txt'],
 "Only two newforms, no weight-12 Delta (a_p not computed), no twisted/residue-class-restricted correlation, no trace-formula identity attempted.",
 "Repeat with Delta and conductors 15–100 up to 10^6 if a Hecke link is pursued.")

add('Z1680','nothing',
 "Analytic step: the defining relation 4uBC-u-B=p is cubic in (u,B,C), so R(p) is not a quadratic-lattice theta coefficient; per C the divisor form gives sum_{d|4Cp+1, d≡-1 (4C)} = (1/phi(4C)) sum_chi chibar(-1) sum_{d|N} chi(d) with N=4Cp+1, i.e. Eisenstein-type coefficients evaluated at 4Cp+1 rather than at p. Also d ≡ -1 (mod 4) for every certificate, so the chi_{-4}-signed count is trivially -R. Identity (4uC-1)(4BC-1)=4Cp+1 checked symbolically and in code (scripts assert d*e=4Cp+1).",
 [S+'certs.c'],
 "No Siegel–Weil/weight computation; no test of a mock-theta or theta decomposition numerically.",
 "Only if a quadratic space is written down for a fixed C (none found).")

add('Z1682','nothing',
 "Analytic: with a=4C the series sum_{u,B} q^{4CuB-u-B} = sum_u q^{(4C-1)u-1}/(1-q^{4Cu-1}) has coefficient of q^n equal to #{(u,B): 4CuB-u-B=n}; the substitution 4Cn+1=(4Cu-1)(4CB-1) turns it into the shifted divisor count #{d | 4Cn+1 : d≡-1 mod 4C}. The nonprincipal-character parts are Eisenstein-type, but the principal part sum_{N≡1(4C)} d(N) q^{(N-1)/4C} (a Lambert series in d(n)) is, by Assessment, not modular, so no exact Appell–Lerch closed formula is expected.",
 [S+'certs.c'],
 "Did not check mock modularity numerically; claim about the principal part is Assessment.",
 "None unless a modular completion is sought.")

add('Z1687','interesting',
 "Over the 4783 primes p≡1 (mod 4), p≤10^5, the continued-fraction period of sqrt(p) (= regulator-type quantity; always odd since N(eps)=-1) correlates with the BM ratio R/M_BM: corr(log period, R/M) = -0.12, and -0.069 after regressing out log p (≈4.7 naive standard errors). The sign and size are those expected if the effect is the L(1,chi_p) / regulator effect that BM_LVALUE.md documents (hard ⇔ large L(1,chi)); not separated here.",
 [S+'misc.py',DAT+'mbm_1e6.txt','BM_LVALUE.md'],
 "Class numbers h_p and L(1,chi_p) not computed, so the regulator-vs-L-value separation is untested; no smallest-certificate word analysis (ES₅ CF-length test) done.",
 "Compute h_p·R_p = sqrt(p) L(1,chi_p)/2 and regress R/M on log L(1,chi_p) and log period jointly.")

add('Z1688','nothing',
 "Analytic step only: for 4xyz=n(xy+yz+zx) with v_p(n)=1 and valuations (a,b,c) of (x,y,z), the tropical condition is that min{0,1-a,1-b,1-c} is attained at least twice, which reproduces the Type I/II valuation patterns (as already in Elsholtz–Tao). No new tropical cone was found by hand.",
 [],
 "Did not enumerate tropical cones by computer nor compare with actual solutions' valuation vectors.",
 "Enumerate cones in [-3,3]^3 and match with solution valuations for p ≤ 10^3.")

add('Z1690','nothing',
 "Substitute measurement (disclosed): the e-slice ratio set {ab^{-1} mod e : ab|N} was not computed; instead D_C(p)={d mod 4C : d | 4Cp+1}. For the 105 hard primes (R/M<0.25, p≤10^6) and C≤30 (3150 slices): mean |D|/phi(4C)=0.28, the whole unit group is hit in only 42 slices, and -1 ∈ D in 91 slices (2.9%, i.e. the ES slice-success rate). For the 9 (★)-failures D never contains -1. The divisor residue sets are far from the whole group, so sum-product covering is not the operative regime.",
 [S+'misc.py'],
 "e-slice ratio set not computed; no sum-product or Bourgain–Glibichuk–Konyagin bound applied; C≤30 only.",
 "Recompute with the ratio set {ab^{-1}} and e up to 200 for hard primes.")

add('Z1691','nothing',
 "Restatement check: the subproduct set of the prime factors of N=4Cp+1 in (Z/4C)^× equals the divisor-residue set D_C(p) measured in Z1690. Whole-group events are rare (42 of 3150 hard slices, C≤30) and -1 is hit in 2.9%; with ω(N)≈log log N elements, Olson/EGZ-type zero-sum theorems (which need many elements) do not apply. Assessment.",
 [S+'misc.py'],
 "No literature check of Olson-type bounds for multiplicative subsets of size ω(N).",
 "None.")

add('Z1694','nothing',
 "Analytic: at q=p the defining equation of U_p reduces to 4xyz ≡ 0 (mod p), so the F_p-shadow is degenerate and local solvability is trivial; no natural finite-field statement implying ES(p) with a size gap was identified.",
 [],
 "No explicit F_p-curve or set construction tested.",
 "None unless a concrete F_p statement is proposed.")

add('Z1695','nothing',
 "Analytic: the condition (4uC-1) | p+u is not a polynomial nonvanishing condition over F_ℓ in (u,C) (it is a divisibility of integers), so the Combinatorial Nullstellensatz has no polynomial to apply; no construction of a grid polynomial was found.",
 [],
 "No symbolic coefficient computation (the object does not exist as stated).",
 "None.")

add('Z1697','nothing',
 "Exact count: for u·B≠0 the variety V_p: 4uBC-u-B=p over F_q has C uniquely determined, and the lines u=0 (B=-p) and B=0 (u=-p) contribute q points each; hence #V_p(F_q) = (q-1)^2+2q = q^2+1 for every p≢0 (mod q). The point count is independent of p, so the F_q-counts carry no p-dependence; all information is arithmetic (integrality), not geometric.",
 [],
 "No brute-force F_q check was run (count is by hand).",
 "None.")

add('Z1698','nothing',
 "Same decomposition in K_0(Var): [V_n] = [G_m^2] + 2[A^1] = L^2 + 1 for every n≠0, independent of n; the variety is rational (C solved as (n+u+B)/(4uB)). Motivic classes do not see the integrality condition that carries ES.",
 [],
 "None beyond the computation.",
 "None.")

add('Z1701','nothing',
 "Analytic: Descartes' relation for curvatures is quadratic (k4 = k1+k2+k3 ± 2 sqrt(k1k2+k2k3+k3k1)), whereas 1/x+1/y+1/z=4/p is linear in reciprocals; no literal embedding of ES into a circle configuration was found (Assessment).",
 [],
 "No circle-configuration search done.",
 "None.")

add('Z1702','nothing',
 "Analytic only: Stern–Brocot/CF of 4/p has length of order log p and no ES criterion was identified in the tree positions; the run-length pattern was not computed.",
 [],
 "SB paths and run-length statistics not computed.",
 "Compute run-lengths of SB paths of 4/p for hard primes against R/M.")

add('Z1703','nothing',
 "Analytic: 1/x and 1/y are Farey neighbours iff |x-y|=1, so Farey edges among the terms of an Egyptian triple occur only for consecutive denominators; the Farey-path reading of ES is therefore degenerate.",
 [],
 "No path-length statistics computed.",
 "None.")

add('Z1704','nothing',
 "Analytic: no discriminant D(p) or target set in the unit tangent bundle was proposed, so the first step (identify D(p) and test a target of size ≫ D^{-δ}) could not be executed as stated.",
 [],
 "Geodesic/discriminant construction not performed.",
 "Propose D(p) explicitly, then test.")

add('Z1706','nothing',
 "Thue-type box test: for p≡1 (mod 4) the fraction of primes with NO certificate (4uB | p+u+B) having uB ≤ sqrt(p) is 10.0% (p<10^3), 6.2% (10^3–10^4), 3.2% (10^4–10^5), 1.2% (10^5–10^6). The Thue-size box alone is not a covering, and the failure fraction decays but is not zero at the scales checked.",
 [S+'certs.c',S+'analyze.py',DAT+'certs2_1e6.txt'],
 "No fixed modulus M(p) or residue a(p) searched; box test only.",
 "Test a modulus-based Thue variant only if the box test's failures are structured.")

add('Z1708','nothing',
 "Not executed beyond analysis: the ray-class/splitting statement 'ES(p) ⇐ p splits completely in K_p' was not tested; for the hard primes the splitting question in ℚ(ζ_840) is trivially 'split' (p ≡ 1 mod 840), so the test must target non-abelian fields, which were not constructed.",
 [],
 "No splitting-field construction or Chebotarev test performed.",
 "Compute splitting of hard primes in a non-abelian field (e.g. cubic) and compare with R/M.")

add('Z1712','nothing',
 "Not executed: data/ec and the curve E_n attached to 4/n were not inspected in this pass; no rank/root-number comparison performed.",
 [],
 "Whole item (curve E_n, rank vs certificates).",
 "Inspect data/ec and test root number against R(p)>0.")

add('Z1713','nothing',
 "Analytic: no family E_p with w(E_p)=-1 for all relevant p and a map from points to certificates was proposed; parity forcing has no concrete input here (Assessment).",
 [],
 "No elliptic-curve family constructed.",
 "None unless a family is proposed.")

add('Z1714','nothing',
 "Analytic: no map from CM/Heegner points on X_0(N) to integer certificates was identified; the 'norm of a coordinate' question was not checked.",
 [],
 "No Heegner computation.",
 "None.")

add('Z1717','nothing',
 "Analytic: abc gives Diophantine non-existence and radical-size bounds, not existence; the requested implication (abc ⇒ failure forces radical patterns) was not established and no data test was run.",
 [],
 "No radical-pattern data test.",
 "None.")

add('Z1718','nothing',
 "Sanity item: B1 (Dickson/Schinzel H) gives infinitely many evaders of any fixed menu, so any proposed proof must use an unbounded menu. The observed (★)-failure list (9 primes ≡1 mod 4 up to 10^6, reproduced by scripts/z38 and matching BM_CORRECTED_COUNT) is consistent with this calibration; no new information.",
 [DAT+'mbm_1e6.txt'],
 "No new calibration beyond B1.",
 "None.")

add('Z1719','nothing',
 "Analytic: R(p) is an integral-point count, not a Frobenius trace; T(p)=sum (−uB/p)/phi(4uB) is a character sum but has no Deligne-type bound from a known motive. No Tate-module identification was made.",
 [],
 "No Galois-representation construction.",
 "None.")

add('Z1725','interesting',
 "Janson-type lower-tail bound in a random-residue model for the box {4uB ≤ X} (events p ≡ -(u+B) mod 4uB): mu grows as ≈0.145 (log X)^2 (mu=13.55 at X=16000) while Delta/mu grows ≈0.5 log X (Delta/mu=5.0 at X=16000) because all moduli share the factor 4 and dependence is dense. Janson's bound exp(-mu^2/(2 Dbar)) = exp(-mu/(2(1+Delta/mu))) therefore decays only like X^{-c} (c≈0.14) rather than exp(-mu): the standard inequality is polynomial, not poly-logarithmic-exponential, in the box size. Model-level result; not a bound on the actual R(p).",
 [S+'janson.py'],
 "Only the random-residue model was studied; no proof that the actual R(p) satisfies the model's dependency structure; no Suen or higher-order inequality tested.",
 "Test whether a Janson-type bound improves after conditioning on the factor-4 structure (u,B parity classes).")

add('Z1730','nothing',
 "Not executed: Baladi–Vallée counts of CF-length for a/p were not computed; analytic note only (the ES₅ CF-length condition is a fixed-length condition, not a count of length-3 expansions).",
 [],
 "Whole item.",
 "Compute CF-length distribution of a/p with a up to small bounds vs ES₅ counts.")

add('Z1732','nothing',
 "Analytic: the ES equation 4xyz = n(xy+yz+zx) is linear in each variable separately (not only bilinear); after y=x+s it becomes quadratic in x, so a Vieta move may exist, but no descent relation preserving positivity was identified.",
 [],
 "No symbolic descent search.",
 "Search for a Vieta involution with positive partner.")

add('Z1734','nothing',
 "Not executed: the random-multiplicative simulation (Rademacher f replacing (·/p) in T(p)) was not run; analytic note only.",
 [],
 "Whole simulation.",
 "Simulate T_f and compare its distribution with T/M0 from DAT mbm data.")

add('Z1737','nothing',
 "Analytic: an incompressibility argument would need a counterexample to be of low description complexity; no such implication is available from the data (hardest-100 list is not low-complexity in an obvious sense). Assessment.",
 [DAT+'hardest_100.tsv'],
 "No complexity ranking computed.",
 "None.")

add('Z1738','nothing',
 "Analytic: Furstenberg-type ×2×3 rigidity gives orbit density in (Z/q)^× for the semigroup generated by 2,3, but the certificate needs -1 in the set of divisor classes of 4Cp+1, which is not an orbit of a fixed semigroup; no test done.",
 [],
 "No orbit computation.",
 "None.")

add('Z1742','nothing',
 "Greedy (Fibonacci–Sylvester) expansion of 4/p over p≡1 (mod 4), p≤10^5: length exactly 3 for 2399 primes and 4 for 2384 primes, i.e. a 3-term greedy ES certificate exists for about half of these primes (this is the trivial part of the picture; it is consistent with R(p)≥1). Partial correlation of greedy length with R/M given log p: +0.10 (not analysed further). Engel expansions (O150) are a different object and the greedy length is not a density heuristic for R.",
 [S+'misc.py'],
 "Engel/Sylvester metric-theory densities not computed.",
 "Check whether the greedy success set is contained in the (★)-positive set (should be by construction).")

add('Z1755','nothing',
 "Analytic: a second-moment (Paley–Zygmund) positive-proportion statement over short intervals needs E[R^2]/E[R]^2 bounded on the interval, which requires variance information not computed here; EXCEPTIONAL_SHORT.md covers the exceptional-set side only.",
 [],
 "No second-moment computation.",
 "Compute E[R^2]/E[R]^2 over intervals of length H = (log X)^A.")

add('Z1756','nothing',
 "Analytic: no lattice Λ_p in ℝ^3 with a small-cone-to-certificate correspondence was constructed; the SL_2 reading is in bsA_hecke_cusp_excursions.md and is not extended.",
 [],
 "No SL_3 construction.",
 "None.")

add('Z1760','nothing',
 "Least-squares fit of M0(p)=sum 1/phi(4uB) over all primes p∈[10^3,10^6] with M0 = a L^2 + b L + c, L=log p: a = 0.15203 (vs 3/(2π²)=0.15198, agreement 3·10^-4); fitted b ≈ -0.022 and c ≈ -0.19 are numerical, not derived by Mellin transform.",
 [S+'misc.py',DAT+'mbm_1e6.txt'],
 "No Mellin/zeta-regularisation derivation of b and c.",
 "Derive b and c via the Dirichlet series of sum 1/phi(4uB) and compare.")

add('Z1761','nothing',
 "Not executed: functional-graph statistics of the greedy-remainder map on a/p were not computed; analytic note that the map is the Fibonacci–Sylvester step (see Z1742).",
 [],
 "Whole item.",
 "Build the functional graph on fractions with denominator p·k, k≤10.")

add('Z1768','nothing',
 "Not executed: the minimal prime p≡1 (mod 840) avoiding all (u,C) with 4uC-1 ≤ B by CRT was not computed.",
 [],
 "Whole item.",
 "Compute minimal evader vs B for B ≤ 200.")

add('Z1769','nothing',
 "Analytic: the pair enumeration (u,B) for R(p) decides ES(p) with O(p log p) divisibility tests (no factoring), so the complexity of certificate search is polynomial in p, not polylogarithmic in p; the witnessing-theorem route therefore needs a polylog search that is not available.",
 [S+'certs.c'],
 "No proof-complexity lower bound or Buss witnessing analysis.",
 "None.")

add('Z1770','nothing',
 "Premise check: divisor-form certificates need factoring only if one insists on the divisor form; the pair form (u,B) is searched by divisibility tests alone (as in scripts/z52d_p2_TO5_certs.c), so the 'factoring hardness' premise is false for the pair form. No conclusion about provability.",
 [S+'certs.c'],
 "No witnessing-theorem argument.",
 "None.")

add('Z1772','nothing',
 "Analytic: no map from a set of size >N to size N whose collisions are certificates was identified; PPP framing gives no test.",
 [],
 "None.",
 "None.")

add('Z1773','nothing',
 "Not executed beyond the repo's earlier enumerative search (924 programs, BRAINSTORM/z45_program_synthesis.md); LLM-guided synthesis not run.",
 [],
 "New synthesis run.",
 "None.")

add('Z1780','nothing',
 "Not executed: the LLL-on-exponent-lattice test with the size constraint d<√N was not run; the repo's gon_lll memo was not re-read in this pass.",
 [],
 "Whole item.",
 "Re-read gon_lll memo and add the size constraint.")

add('Z1787','nothing',
 "Premise and step: for p=409 (a (★)-failure) the trial set P(409) has 272 pairs (68 distinct moduli 4uB) with sum 1/phi(4uB)=5.1506 (matches z38_mbm), and no pair is a certificate. Each pair's failure is a separate congruence fact, so the shortest 'proof of failure' is the full list; no covering by fewer moduli is possible.",
 [S+'misc.py'],
 "No comparison across the 9 failures; no check of whether failure proofs share a shape.",
 "Compare the failure trial sets of the 9 known (★)-failures.")

add('Z1802','interesting',
 "Among the 105 hard primes (R/M_BM<0.25, p≤10^6) the residue distribution mod 840 is strongly non-uniform (chi^2=660 on 96 df). Class 409 (mod 840) holds 13 hard primes (expected 1.1); at R/M<0.5 it holds 71 (expected 11.6). By Legendre cells (3/p),(5/p),(7/p): all-QR cell (+,+,+) holds 50 of 105 hard primes against a 12.4% base rate; hard primes are never in (−,−,−),(−,−,+),(−,+,−),(−,+,+) cells except 4 in (−,−,+). The signal is a residual dependence on quadratic characters mod 105 that M_BM does not absorb (interpretation, not checked against M_gen).",
 [S+'hard.py',S+'misc.py',DAT+'mbm_1e6.txt'],
 "Not tested against M_gen or higher-modulus classes (mod 2520); quartic-symbol part (Z1803) confounded with this.",
 "Recompute residual vs M_gen and mod 2520 classes; check class 409 at p>10^6.")

add('Z1803','nothing',
 "Quartic symbols (2/p)_4,(3/p)_4,(5/p)_4,(7/p)_4 among p≡1 (mod 8): on the hard set (n≈105) the distribution of (5/p)_4 and (7/p)_4 differs from controls (e.g. (7/p)_4 ∈ {±i} 28% vs 50%), but the hard set is concentrated in the quadratic cell and class 409 (Z1802), so the quartic effect is not separated from the quadratic-cell effect. Result: no independent quartic invariant established.",
 [S+'hard.py'],
 "No separation of quartic from quadratic-cell effects (would need controls matched on (3,5,7)-cells).",
 "Match controls on the (3/p),(5/p),(7/p) cell before reading quartic symbols.")

add('Z1808','covered',
 "The question (|T(p)| ≤ (1-δ)M0(p) asymptotically) is answered in BM_CORRECTED_COUNT.md §2 (Thm 2.2 proof, line ~133): T(p) = o(L^2) hence M_BM(p) = M0(p)(1+o(1)), proved via the hyperbola decomposition and Dirichlet-series bounds. Data check: sup over p≡1 (mod 4) of T/M0 is 0.528 (p=73), 0.443 (10^3–10^4), 0.387 (10^4–10^5), 0.349 (10^5–10^6): decreasing, consistent with T=o(M0).",
 ['BM_CORRECTED_COUNT.md',DAT+'mbm_1e6.txt'],
 "Explicit δ(p) not extracted; the bound is asymptotic.",
 "None (depth document exists).")

add('Z1809','nothing',
 "Analytic: sum_{u,B} chi(u)chi(B)/phi(4uB) is a hyperbola-truncated sum (uB ≤ p/4), not an Euler product, so identification with L(1,chi)^2 holds only up to a truncation error that is not controlled here; no Mellin inversion carried out.",
 [],
 "No numerical test of T(p) against L(1,chi_p)^2.",
 "Compare T(p) with L(1,chi_p)^2 (requires L-values).")

add('Z1810','nothing',
 "The pairing d↔e is the swap (u,B)→(B,u): d=(p+u)/B maps to e=(p+B)/u (identity asserted in scripts/z52d_p2_TO5_certs.c). It is fixed-point-free on P(p) because u=B forces u=B=1, excluded by u+B odd; hence R(p) is even. Checked: all 39175 primes p≡1 (mod 4), p≤10^6 have even R. Exact hyperbola error tracking was not done.",
 [S+'certs.c',DAT+'mbm_1e6.txt'],
 "No hyperbola-error analysis.",
 "None.")

add('Z1812','nothing',
 "Analytic: a solution of 4/(kp) whose denominators are all divisible by k scales to 4/p; non-tautological descent needs denominators sharing only part of k, which was not enumerated. The transport statement is therefore tautological in its trivial case.",
 [],
 "No enumeration of solutions for 4/(kp), k≤50.",
 "Enumerate for hard p and k≤50.")

add('Z1813','nothing',
 "Analytic: the m/(kp) family reduces to scaling; non-trivial transports need gcd(k, x,y,z) partial, characterised algebraically but not enumerated for k≤12.",
 [],
 "No enumeration.",
 "Enumerate for k≤12.")

add('Z1817','nothing',
 "Analytic: the forbidden-class density sum_{4uC-1 ≤ B} 1/(4uC-1) grows like log^2 B, far above 1, so a lower-bound avoidance sieve at level B is outside the regime where Rosser–Iwaniec-type minorants are positive; B1 already yields evaders, so no unconditional lower bound follows from this route (Assessment).",
 [],
 "No sieve computation.",
 "None.")

add('Z1818','nothing',
 "Analytic: 4Cp+1 with C fixed is a linear form in p; a Maynard–Tao argument could make several of them prime simultaneously, and prime 4Cp+1 kills slice C (verified: 25682 prime-N slices, 0 successes). This gives a menu-evasion family but no new certificate statement.",
 [S+'slices.py'],
 "No Maynard-type admissibility computation.",
 "None.")

add('Z1819','nothing',
 "Premise verified: for prime N=4Cp+1 the C-slice never succeeds (25682 slices, C≤40, p≡1 (mod 4), p≤10^5: 0 successes). Semiprime and higher slices succeed with rates Ω=2: 0.044, Ω=3: 0.112, Ω=4: 0.19, Ω=5: 0.28, Ω=6: 0.35, Ω=7: 0.41 (scripts/z52d_p2_TO5_slices.py).",
 [S+'slices.py',S+'semiprime_bias.py'],
 "No closed formula for the success rate by factorisation type.",
 "Use the Ω-table as the calibration for slice-success models.")

add('Z1821','interesting',
 "Prime-modulus slices: a certificate with d=(p+u)/B prime exists iff some prime ℓ | 4Cp+1 with 4C | ℓ+1 and p ≡ -(4C)^{-1} mod ℓ. Over p≡1 (mod 4): P(exists such ℓ ≤ L) = 0.50 (L=3), 0.83 (L=31), 0.90 (L=101), 0.97 (L=1001), 0.990 (L=10^4). The uncovered fraction decays as L^{-0.50} (log-log slope -0.50 on [10^3,10^5], -0.52 on [10^5,10^6]). The premise 'sum tau((ℓ+1)/4)/ℓ matches log^2' is false: the sum over ℓ≤L, ℓ≡3 (4) is 2.58, 3.89, 5.24 at L=10^3,10^4,10^5, i.e. ≈ ½ log L, which explains the L^{-1/2} decay. Prime-d certificates are 47% of all certificates for p<10^3 but 25% for p∈[10^5,10^6].",
 [S+'certs.c',S+'analyze.py',DAT+'certs2_1e6.txt'],
 "No rigorous covering theorem; the L^{-1/2} law is empirical up to 10^6 and the heuristic is Π(1-τ/ℓ) under CRT independence.",
 "Test the L^{-1/2} law for p up to 10^7 and check whether the uncovered set is the (★)-failure-like set.")

add('Z1822','nothing',
 "Same data as Z1821: the union over primes ℓ of the classes -(4C)^{-1} mod ℓ (C | (ℓ+1)/4) covers all but ≈ L^{-1/2} of the primes up to L. Since the total class density Σ τ/ℓ diverges (≈½ log L), density arguments do not exclude a covering of all primes, but CRT evaders (B1) exist; no new statement.",
 [S+'analyze.py',DAT+'certs2_1e6.txt'],
 "No covering-system literature check.",
 "None.")

add('Z1823','nothing',
 "Route test: -1 ∈ ⟨classes of prime factors of 4Cp+1⟩ mod 4C holds for 25% of hard-prime slices (C≤30) but -1 is a subproduct (divisor residue) in only 2.9%: the subgroup/Artin gate overcounts ≈9× and is not the operative condition. For the 9 (★)-failures the subgroup test still holds in 18.5% of slices (50/270), while the subproduct test never does.",
 [S+'misc.py'],
 "No Chebotarev/Kummer density computation.",
 "Use the subproduct gate, not the subgroup gate, in any Artin-type model.")

add('Z1824','nothing',
 "corr(R/M_BM, log tau(p+1)) = +0.53 and corr(R/M_BM, log tau_3(p+1)) = +0.533 over 4783 primes p≡1 (mod 4), p≤10^5. The association is mechanical: the B=1 slice counts divisors of p+1 that are ≡3 (mod 4); tau_3 adds nothing beyond tau.",
 [S+'misc.py'],
 "No τ_3 comparison with R beyond the B=1 slice.",
 "Remove the B=1 slice and re-test.")

add('Z1825','nothing',
 "Analytic: the Dirichlet series D(s)=sum R(n) n^{-s} has no visible product formula; the triple-pole heuristic is consistent with the log^2 mean but was not verified.",
 [],
 "No Mellin/Tauberian computation.",
 "None.")

add('Z1827','interesting',
 "Calibration of the random subset-product model: for squarefree semiprimes N=4Cm+1 the success rate (q≡-1 mod 4C for a factor q) is below the naive 1/phi(4C) for φ(4C)≥8 (ratio success·φ ≈ 0.3–0.6), but for balanced semiprimes (both factors > N^{1/3}) the ratio returns to ≈0.8–1.2 (C=6: 0.12 vs 0.125; C=13: 0.035 vs 0.042; C=21: 0.049 vs 0.042; C=24: 0.030 vs 0.031). The deficit comes from small factors (q < N^{1/3}) that cannot be ≡-1 mod 4C in range. Same behaviour for N from primes p and from all odd m, so it is not a prime-p effect.",
 [S+'semiprime_bias.py',S+'slices.py'],
 "Only semiprimes; no full subset-product distribution for k≥3 factors.",
 "Use balanced-factor conditioning in any random-element model of slice success.")

add('Z1828','nothing',
 "Exact: N=4Cp+1 ≡ 1 (mod 4C), so d ≡ -1 iff N/d ≡ -1: the total-product constraint is automatic. The semiprime success criterion (smaller factor ≡ -1) is consistent with this symmetry. The random-model probabilities were not recomputed under the constraint.",
 [S+'semiprime_bias.py'],
 "No recomputed random-model probabilities.",
 "Recompute the subset-product model with total-product conditioning and balanced factors.")

add('Z1829','nothing',
 "Analytic: hard primes split completely in ℤ[ω] and ℤ[i]-type fields; a certificate formula in (a,b) with p=a²+3b² was not searched.",
 [],
 "No search for linear/quadratic expressions in (a,b).",
 "None.")

add('Z1830','nothing',
 "Analytic: any polynomial identity in (a,b) with p=a²+b² specialises at b=0 to n=a², an odd square where Type I/II solutions do not exist (T1), so polynomial identities in (a,b) are obstructed; rational identities with poles on b=0 were not tested.",
 [],
 "No symbolic search.",
 "None.")

add('Z1831','nothing',
 "Analytic: for prime p the representation p=a²+b² is unique up to signs and order, so integrality of rational parametrisations with b in denominators is a condition on one representation per prime; no low-degree search was run.",
 [],
 "No search.",
 "None.")

add('Z1834','nothing',
 "Analytic: no bijection between certificates and reduced forms of discriminant -4pk was constructed; the windmill memo covers the related objects.",
 [],
 "No enumeration.",
 "None.")

add('Z1836','nothing',
 "Analytic: a Rédei/4-rank reformulation of the -1 subproduct question would need the F_2-matrix of quadratic characters of prime factors; not computed (see Z1837 for the elementary-2 case).",
 [],
 "No F_2 matrix computed.",
 "None.")

add('Z1837','nothing',
 "Analytic: for 4C=24 the group (Z/24)^× ≅ (Z/2)^3, and the subproduct question becomes a subset-sum over F_2^3 (not a linear system); a linear-span test is only necessary. Not computed.",
 [],
 "No F_2 computation.",
 "Compare subset-sum and span tests for 4C=24 on hard primes.")

add('Z1838','nothing',
 "Measured the forcing-line coverage: the cell (3/p)=(5/p)=(7/p)=+1 has 12.4% of primes p≡1 (mod 4), p≤10^6 (≈1/8). Outside it, the repo's proven forcing lines F_3, F_5, F_7 (EXSET_CHAR_FORCING.md; classical for least-QNR ∈{3,5,7}) apply; 50 of the 105 hard primes lie in the all-QR cell (base rate 12.4%). No new multi-symbol forcing pattern was identified beyond the all-QR complement.",
 [S+'misc.py',DAT+'mbm_1e6.txt','EXSET_CHAR_FORCING.md'],
 "No attempt to prove a forcing line for q=11 or a joint pattern.",
 "Quantify the all-QR cell at larger p and test q=11 forcing.")

add('Z1839','nothing',
 "Least quadratic non-residue n2(p) over p≡1 (mod 4), p≤2·10^5: max 29, mean 3.57, max n2/log²p = 0.77. The implication chain ES ⇐ (F_q for q ≤ n2(p)) is a restatement; proven forcing lines cover 87.6% of primes, and F_11 would add ≈6.2% (the all-QR-up-to-7 cell halved), so the least-QNR bound is not the bottleneck.",
 [S+'misc.py'],
 "No Burgess/Treviño explicit bound computed.",
 "None.")

add('Z1841','nothing',
 "Analytic: sterile profinite points were not constructed; the 'locally a square' classification was not tested (the odd-square T1 obstruction is local at 2 and 3 only in the known families).",
 [],
 "No profinite computation.",
 "None.")

add('Z1843','nothing',
 "Analytic: nonstandard counterexample reasoning is logic hygiene; no finite test is available.",
 [],
 "None.",
 "None.")

add('Z1844','nothing',
 "Analytic: overspill/underspill gives only uniform-bound equivalences with explicit bounds; no new statement.",
 [],
 "None.",
 "None.")

add('Z1845','nothing',
 "Near-square primes p=m²+k (k=4,16,36,100,144, m<1000, p≤10^6): R/M_BM means 1.11, 1.12, 0.83, 1.31, 1.25 with no R=0. Against own-cell controls (same (3/p) and p mod 8, ≤10^6) the offsets are −0.08, −0.11, −0.17, +0.14, +0.19: mixed signs, consistent with residue-class effects beyond the (3/p), p mod 8 cells; no uniform 'near-square' effect (see Z1846 for the extended test).",
 [S+'analyze.py',DAT+'mbm_1e6.txt',DAT+'nsq_mbm_4e6.txt'],
 "No modulus-5/7 controls.",
 "None unless a robust family effect appears at larger p.")

add('Z1846','nothing',
 "Extended test of m²+k to p≤4·10^6 (982 primes, data/z52b/pass2/TO5/nsq_mbm_4e6.txt via scripts/z52d_p2_TO5_pmb.c; validated on the known failure 1134241): for k=4 the family mean is 0.97 (p∈(10^6,4·10^6]) vs same-range random control 1.15 (n=200), a −0.18 offset (SE 0.03) against −0.075 for the own-cell control at ≤10^6; for k=100 the offset is +0.04. No consistent Gaussian-factorisation effect: signs differ across k, and the k=4 offset is explained largely by its cell. No forced certificate found.",
 [S+'pmb.c',DAT+'nsq_mbm_4e6.txt',DAT+'same_range_ctl_1e6_4e6.txt'],
 "No residue-matched control in (10^6,4·10^6] (only 200 random primes); no algebraic certificate for m²+4.",
 "Build a residue-matched control on 840 classes in (10^6,4·10^6] if the family is revisited.")

add('Z1847','nothing',
 "Analytic: for n=4m²+1 or m²+1 a Gaussian factorisation identity would produce certificates only if an identity of the form 4/n = Σ 1/x_i with polynomial x_i exists, which is excluded on residue classes containing squares by Mordell–Schinzel; the family's data (Z1846) show no forced structure.",
 [DAT+'nsq_mbm_4e6.txt'],
 "No finite covering test by ET classes.",
 "None.")

add('Z1849','nothing',
 "Analytic: no word-level invariant (Jacobi-symbol combination constant on ES₅ words) was computed; the T1 statement is already built into the pair form (R(m²)=0).",
 [],
 "No word enumeration.",
 "None.")

add('Z1850','nothing',
 "Not executed as stated: the I3 'least interior endpoint u(p)' is not computed in this batch's data (the minuB column of scripts/z52d_p2_TO5_certs.c is min uB, a different statistic); Jacobsthal-type model not run.",
 [S+'certs.c'],
 "Whole item (I3 endpoint and Jacobsthal model).",
 "Compute the I3 endpoint from BRAINSTORM/I3_DEEP_FABLE.md's definition.")

add('Z1856','nothing',
 "Shift form verified and quantified: for p+B=u(4BC-1) the B-slice succeeds iff p+B has a divisor ≡ -1 (mod 4B). Slice success rates over p≡1 (mod 4), p≤10^6: B=1 0.872 (verified exactly against certificate counts for all 39175 primes), B=2 0.800, B=3 0.560, B=4 0.465, B=5 0.450, B=6 0.504 (B≥3 without the gcd(u,B)=1 filter, so approximate). Most certificates have small B: 58% of certificates have B<0.1√p.",
 [S+'misc.py',S+'certs.c',DAT+'certs2_1e6_hist.txt'],
 "Exact per-B certificate counts for B≥2 (gcd filter) not computed; block-sum identity not proved.",
 "Add per-B certificate counts to the certs tool to make B≥3 exact.")

add('Z1857','nothing',
 "Histogram of all 2.13M certificates over p≤10^6 (both coordinates): B/√p < 0.1 for 58%, B ≥ √p for 23%, and intermediate deciles 0.1–1 for the rest. The √p-scale 'near-square factorisation' regime carries a minority of certificates, so the Sylvester–Schur-type mechanism is not the bulk. Hard-prime-restricted histogram not computed.",
 [DAT+'certs2_1e6_hist.txt'],
 "No hard-prime-restricted histogram; no literature search for divisors of consecutive integers near square roots.",
 "Repeat histogram restricted to R/M<0.5.")

add('Z1869','nothing',
 "Produced the hardest-100 list (smallest R/M_BM among p≡1 (mod 4), p≤10^6): data/z52b/pass2/TO5/hardest_100.tsv. The top entries are the 9 (★)-failures ≡1 (mod 8) up to 10^6 (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321) followed by 9649, 25609, 116329; the list is a reusable test set, not a new result.",
 [S+'hard.py',DAT+'hardest_100.tsv'],
 "No features beyond R/M and p mod 840.",
 "Use as default test set.")

add('Z1871','nothing',
 "Not completed: a dossier of PROVED necessary conditions for a counterexample was not assembled; the only quantitative input computed here is the all-QR cell density (12.4%, Z1838) and the (★)-failure list (Z1869).",
 [S+'misc.py'],
 "Full dossier.",
 "Assemble from DISPROOF_AVENUES.md.")

add('Z1872','nothing',
 "Analytic: no family statement S(m) distinguishing m≤7 from m=8 was formulated; the repo's 8/n failures at n=131, 241 (FRONTIER §1) are the boundary data.",
 [],
 "No formulation.",
 "None.")

add('Z1873','nothing',
 "Analytic: no Hasse diagram of ES-implying statements was built.",
 [],
 "Whole item.",
 "None.")

add('Z1891','nothing',
 "Analytic: supersaturation gives lower tails for counts in extremal settings; ES's R(p) is a count in a sparse set of pairs, and no supersaturation theorem with polylog mean was identified. Literature search not performed.",
 [],
 "No literature search.",
 "Run web-search for supersaturation with polylog means.")

add('Z1896','nothing',
 "Analytic: a Sperner-type labelling was not constructed.",
 [],
 "None.",
 "None.")

add('Z1900','nothing',
 "Analytic: the Type II condition for fixed C is 4uB | p+u+B, not a quadratic form in a fixed Schwartz space; no Weil-representation identity for slice counts was found.",
 [],
 "None.",
 "None.")

add('Z1903','nothing',
 "Analytic: the T1 obstruction is a reciprocity-type statement; a linking-number dictionary was not tested against data.",
 [],
 "None.",
 "None.")

add('Z1905','nothing',
 "Duplicate of Z1691 (subset products / zero-sum in (Z/4C)^×); same measurements (Z1690/Z1691) apply: the whole group is rarely hit and -1 in 2.9% of hard slices.",
 [S+'misc.py'],
 "Waring-type group theory not checked beyond the abelian case.",
 "None.")

add('Z1910','nothing',
 "Not executed: the ℤ[T]-identity search for quadratic n(T) with small coefficients was not run; the Mordell–Schinzel classification is in BRAINSTORM/z18_two_specialisations.md.",
 [],
 "Whole search.",
 "Run bounded-degree search for x,y,z ∈ ℤ[T].")

add('Z1911','nothing',
 "Analytic: ES is not a system of linear divisibilities with fixed unknowns (the C-variable enters multiplicatively with u), so a local-global theorem for linear divisibility does not apply directly.",
 [],
 "None.",
 "None.")

add('Z1912','nothing',
 "Analytic: D(N,m)=∃d|N, d≡-1 (mod m) is an NP-type predicate; complexity statement only.",
 [],
 "None.",
 "None.")

add('Z1916','nothing',
 "Premise refuted: the claim 'avoiding -1 among subproducts forces the subgroup generated by the prime-factor classes to avoid -1' is false: for the 9 (★)-failures and C≤30, -1 lies in that subgroup in 50 of 270 slices (18.5%) while never as a subproduct (scripts/z52d_p2_TO5_misc.py).",
 [S+'misc.py'],
 "No structure theorem.",
 "None.")

add('Z1925','nothing',
 "Slice table for small B (see Z1856): B=1 0.872, B=2 0.800, B=3 0.560, B=4 0.465, B=5 0.450, B=6 0.504 over p≡1 (mod 4), p≤10^6. Divisors of p+B give the small-B slices directly; the union over B≤6 succeeds for 99.4% of these primes (joint failure 0.00605, Z1927), so the first few slices already cover almost everything.",
 [S+'misc.py'],
 "No coverage curve beyond K=6.",
 "Extend to K=100 to fit the coverage curve.")

add('Z1926','covered',
 "Criterion check: the B=1 slice succeeds iff (p+1)/2 has a prime factor ≡3 (mod 4). Verified for all 39175 primes p≡1 (mod 4), p≤10^6 (100% agreement). Failure fractions 0.100 on [5,10^3), 0.146 on [10^3,10^4), 0.140 on [10^4,10^5), 0.126 on [10^5,10^6), and c/√log p fits with c≈0.45 on [10^3,10^6]: the Landau–Ramanujan shape. The criterion and the framing are already in B1_LINE.md (b=1 line, López's line).",
 ['B1_LINE.md',S+'misc.py',S+'analyze.py'],
 "Density constant not derived.",
 "None.")

add('Z1927','interesting',
 "Iterated Landau–Ramanujan for consecutive shifts: over p≡1 (mod 4), p≤10^6, the probability that all of the slices B=1..6 fail is 0.00605, versus 0.00164 for the product of marginal failure rates: a factor 3.7. Failures of the shift slices are strongly positively correlated, so the independence heuristic (product of (log p)^{-δ_B}) underestimates joint failure by about 4× here. Exact for B=1,2; approximate for B≥3 (no gcd filter).",
 [S+'misc.py',DAT+'mbm_1e6.txt'],
 "Exponents δ_B not computed; B≥3 approximate.",
 "Add the gcd filter and compute joint failure for B≤K with K up to 20.")

add('Z1929','nothing',
 "Analytic: a Selberg upper-bound sieve for (★)-failures is available in principle; no computation performed.",
 [],
 "None.",
 "None.")

add('Z1934','nothing',
 "Analytic check: every certificate divisor d satisfies d ≡ -1 (mod 4), so χ_{-4}(d) = -1 identically and the χ_{-4}-signed count equals -R (trivial). Nontrivial sign characters (mod 8, 3, 5) not searched.",
 [S+'certs.c'],
 "No search over characters mod 8, 3, 5.",
 "Search χ_8 and χ_{-8} signed sums.")

add('Z1937','nothing',
 "R(p) mod m over p≡1 (mod 24), p≤10^6 (9732 primes): every residue is taken for m=3, 5, 7, 9 (roughly uniform); for m=8 and 16 only even residues occur (R is even, Z1810). No forbidden nonzero residue; no count-congruence obstruction at these moduli. Partial counts R_C not computed.",
 [S+'analyze.py',DAT+'mbm_1e6.txt'],
 "Partial counts R_C(p) and residues mod 3 of B=1 counts not computed.",
 "Repeat for partial counts restricted to C in a residue class.")

add('Z1940','nothing',
 "Not executed: the signed (one negative denominator) search was not run; analytic note that ES signed relaxations are trivially solvable by many identities, so the positivity content must be localised as in Z1910.",
 [],
 "Whole item.",
 "None.")

add('Z1946','nothing',
 "Not executed: Type I counts f_I(p) are not in this batch's data (the pair form corresponds to the Type II construction 4/n = 1/(uBC)+1/(nBC)+1/(nuC)); a Type I count requires the trial-form enumeration.",
 [],
 "Whole item.",
 "Compute f_I(p) by the Elsholtz–Tao trial form and correlate with f_II = R.")

add('Z1956','nothing',
 "Identity: X=(d+e)/2 and Y=(e-d)/2 satisfy X²-Y²=4Cp+1 with X ≡ -1 (mod 2C) (since d≡e≡-1 mod 4C) and Y=2C(B-u); this is a reformulation of the divisor form, not new counting. Fermat-type search counts not performed.",
 [S+'certs.c'],
 "No Fermat search counts.",
 "None.")

add('Z1959','nothing',
 "Analytic: simultaneous primality of 4Cp+1 for C ≤ K kills all slices C ≤ K (verified: prime-N slices never succeed, Z1819); no record search of runs was performed.",
 [S+'slices.py'],
 "No search for long runs.",
 "None.")

add('Z1987','nothing',
 "Analytic: for prime d, d ≡ -1 (mod 4C) iff the Artin symbol of (d) in ℚ(ζ_{4C}) is complex conjugation (standard). For composite divisors the statement needs multiplicativity; no Kummer-field computation was done.",
 [],
 "No Galois computation.",
 "None.")

add('Z1988','nothing',
 "Analytic: the CM extension ℚ(ζ_{4C})/ℚ(ζ_{4C})^+ and its odd characters are the natural decomposition of the class gate; relative class number or Stickelberger analysis not performed.",
 [],
 "None.",
 "None.")

# ---- verify coverage and write
ids=[json.loads(l)['mid'] for l in open(B) if l.strip()]
missing=[m for m in ids if m not in O]; extra=[m for m in O if m not in ids]
assert not missing and not extra, (missing, extra)
with open(OUT,'w') as f:
    for m in ids: f.write(json.dumps(O[m],ensure_ascii=False)+'\n')
from collections import Counter
print("wrote",OUT,len(ids),"lines; counts:",dict(Counter(O[m]['outcome'] for m in ids)))
