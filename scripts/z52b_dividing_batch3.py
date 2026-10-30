from z52b_dividing_lib import I

def F(feature, has, supply, why, first_step, refs=(), tags=(), conf="med", effort="medium"):
    I(f"Feature: {feature}", f"Dividing-line feature '{feature}'. ES {has}. To supply it one could: {supply}",
      why, first_step, refs, ["feature", *tags], conf, effort)

# ---- Features separating proved from failed (mined from the catalog) ----
F("power-size witness reservoir", "LACKS it (expected witnesses ≍ log² p)",
  "embed ES(p) in a 4-term problem 4/p = Σ_{i≤4} 1/x_i (power count) and prove a 'merging' rule that converts a structured 4-term solution into a 3-term one",
  "Every proved pointwise result with polylog witnesses (Linnik–Gallagher, Chen) rides on a power reservoir.",
  "Count 4-term solutions of 4/p with one denominator in a prescribed divisor class and test how often a merge (1/a + 1/b = 1/c) is available.",
  ["BRAINSTORM/z31_small_count_pointwise.md"], ["mech:T-thick", "reservoir"])
F("free (untied) witness parameter", "has a partially free parameter C (4Cp+1) but the modulus 4C moves with it (B2)",
  "freeze the modulus: restrict to C in a fixed finite set and use many p-tied integers simultaneously (fixed-modulus character events, F3)",
  "Least-witness theorems under GRH need fixed moduli; ES's moving modulus is the precise lack.",
  "List fixed-modulus sub-events of ES (C fixed) and compute the fraction of p ≡ 1 mod 24 solved by C ≤ 10 — how many fixed C are needed empirically?",
  [], ["fixed-modulus", "B2"])
F("periodic witness orbit (enables coverings)", "LACKS it — a protective feature: covering-type failure (p + 2^k, Sierpiński) is unavailable",
  "nothing to supply; instead PROVE formally that ES failure sets cannot be cut out by finitely many congruences beyond T1 (B1-type lemma, already partly known)",
  "Explains why ES differs from p + 2^k; makes failures (if any) unstructured.",
  "State the lemma 'no AP of primes fails ES' (scaling argument exists for q ≡ 3 mod 4) and try to extend to 'no polynomial-value set fails ES'.",
  ["ES_APPROACH_GENERATORS.md §1"], ["obst:covering", "protective"], effort="cheap")
F("involution with odd fixed-point count (Zagier)", "LACKS a known one",
  "search the finite set of ES-adjacent objects (e.g. Type I triples (a,d,f) with f | 4a²d+1, 4ad | p+f, bounded) for involutions with a unique fixed point",
  "Proved O(1)-count results at p ≡ 1 mod 4 (two squares) come exactly from such involutions.",
  "Brute-force: for each p ≡ 1 mod 24 ≤ 10^5, tabulate |S(p)| mod 2 for several natural finite certificate sets S(p); an always-odd set is a lead.",
  ["Zagier 1990", "INVOLUTION_ES.md"], ["mech:involution-parity", "seen:INVOLUTION_ES.md", "computation"], effort="cheap")
F("composition law on targets", "LACKS prime-to-prime composition (only ES(n) ⇒ ES(kn))",
  "look for a bilinear map on ES certificates: from certificates at q₁, q₂ build one at q₁q₂ that 'descends' to a prime factor (as in Euler's four-square descent)",
  "Four squares and two squares are proved by composition + descent.",
  "Check whether the quaternion-order reformulation (QUATERNION_ES.md) carries a multiplicative norm compatible with certificates.",
  ["QUATERNION_ES.md"], ["mech:composition-law", "mech:descent"], effort="big")
F("forced object to descend from (fundamental unit, C(2n,n))", "LACKS a canonical p-tied object guaranteed to contain a certificate",
  "candidate forced objects: fundamental unit of Q(√p), the CF period of √p, the class group of Q(√−p), Gauss periods; test whether any yields a certificate",
  "Legendre's negative-Pell proof and Bertrand's proof both start from a forced object with exact factorisation.",
  "For p ≡ 1 mod 24 ≤ 10^6: take ε_p = (t + u√p)/2 and test whether t, u, t±2, etc. contain a divisor ≡ −1 mod 4C for the relevant C.",
  [], ["mech:forced-object", "mech:descent", "computation"], effort="cheap")
F("class-group parametrisation with positivity", "LACKS (certificates are not known to biject with a class group or genus)",
  "seek a binary/ternary quadratic form Q_p whose representations of a fixed number correspond to ES solutions; then class number > 0 / genus would force existence",
  "Three squares, x²+ny² representations: count = class-number-weighted, positivity from Dirichlet's L(1,χ) > 0.",
  "Write ES Type I solutions as representations by the binary form 4ad·x − f·y patterns; check for a discriminant D(p) attached naturally.",
  [], ["mech:genus", "mech:class-number"], effort="medium")
F("Heegner-type point construction", "LACKS",
  "find a modular curve or Shimura curve whose CM points of discriminant related to p map to the ES surface",
  "Primes p ≡ 5,7 mod 8 congruent and Sylvester's cube problem are pointwise for every prime in a class via Heegner points.",
  "Ask whether the ES cubic surface (projective closure) is dominated by a family of curves with modular parametrisations (e.g. via its conic bundle structure).",
  [], ["mech:heegner"], conf="low", effort="big")
F("root-number / parity forcing", "LACKS a parity-forced object",
  "attach an L-function or Selmer group to p (e.g. from a genus-one fibre of the ES surface) whose root number is −1 for all p ≡ 1 mod 24",
  "Parity of Selmer ranks proves 100% results (Smith) and conditional pointwise results (BSD).",
  "For the elliptic fibrations of the ES surface over Q(p), compute root numbers of a few fibres for p ≡ 1 mod 24 and see whether a sign is forced.",
  [], ["mech:root-number-parity"], conf="low", effort="medium")
F("count divisibility invariant (Chevalley–Warning, Chen's Markoff orbit sizes)", "LACKS",
  "find a finite ES-adjacent set S(p) with |S(p)| ≡ 1 mod ℓ provable via polynomial-method or group-action arguments",
  "Markoff mod p and EGZ are proved via divisibility of counts.",
  "Compute |S(p)| mod 3 and mod 2 for natural sets S(p) (Type I / Type II triples with bounds) across p ≡ 1 mod 24; look for constant residues.",
  [], ["mech:count-divisibility", "computation"], effort="cheap")
F("finite escalation / certificate threshold (290, 451, Graham's 77)", "LACKS (U(n) has sporadic failures to 978145; ES itself has no known threshold theorem)",
  "find a reformulation where an escalation lemma holds: 'if ES-shape S solves all p < B then all p' — unlikely, but record the precise failure",
  "Universality theorems for forms are finite-check because of modular-form bounds; ES has no modular generating function.",
  "Look for a generating series Σ R(n) q^n with modular or mock-modular properties (theta quotients in repo).",
  [], ["mech:escalation", "mech:modular-forms"], conf="med")
F("modular generating function for the count", "LACKS (theta-quotient attempts exist in repo)",
  "build a weighted count R_w(n) of ES solutions that is a Fourier coefficient of a (mock/quasi-)modular form; then Eisenstein vs cusp bounds give pointwise positivity",
  "Duke–Schulze-Pillot and 290/451 rely on Eisenstein main term dominating cusp contributions pointwise.",
  "Compute Σ R(n) q^n for small n with several weightings and test against LMFDB-style modular form spaces of small level.",
  [], ["mech:modular-forms", "computation"], effort="medium")
F("exceptional set has a canonical shape (AP / squares / sparse algebraic)", "HAS one canonical bad shape (odd squares, T1) and sporadic U(n) values",
  "prove that ES failures, if any, avoid every other structured shape (polynomial values, Crocker-type sparse families, APs)",
  "Proved/failed problems both display structured exception sets; classifying admissible exception shapes narrows disproof routes.",
  "Check ES numerically on dense structured families: p = a²+1, p = 2^k·m+1, p = Fermat-like numbers up to large sizes; record min R(p)/log² p per family.",
  [], ["exception-shape", "computation"], effort="cheap")
F("expected count log² vs log (Crocker threshold)", "HAS log², which beats the log-scale counterexamples (Crocker's p+2^a+2^b)",
  "make the 'log² is enough under weak independence' heuristic precise: Janson-type inequality conditional on a correlation bound between certificate families",
  "The only known infinitely-failing log-count problem has log count; ES's log² is one level higher.",
  "Find whether any problem with log² expected count and no local obstruction is known to fail infinitely often (search 'sum of a prime and three powers of 2 exceptions').",
  ["EXSET_ARITH_JANSON_OPUS.md"], ["count:log2", "mech:janson", "seen:EXSET_ARITH_JANSON_OPUS.md"], effort="cheap")
F("independence of witness events", "UNCLEAR: certificate families share the integer p, correlations not controlled",
  "measure empirically the pairwise correlation between Type I families (a,d) and (a',d') as events over p, and bound them by large-sieve arguments",
  "Crocker-type failures exploit strong correlation; Poisson heuristics need weak correlation.",
  "Compute the covariance matrix of the 50 most frequent certificate families over p ≡ 1 mod 24 ≤ 10^7.",
  [], ["correlation", "computation"], effort="cheap")
F("Siegel-ineffective finite exceptions", "COULD HAVE (U(n) sporadic list looks like idoneal / Ramanujan-form lists)",
  "identify an L-function or class number whose smallness would control U(n) failures; prove finiteness ineffectively",
  "Idoneal numbers and Ramanujan's form show 'finite + ineffective' is the natural outcome for class-number-governed problems.",
  "Factor the U(n) sporadic list and compute class numbers of Q(√−n), Q(√−4n), Q(√−3n) etc.; look for uniformly small values.",
  ["Weinberger 1973", "Ono–Soundararajan 1997"], ["mech:siegel-ineffective", "sporadic", "computation"], effort="cheap")
F("thin-orbit expansion (SL₂ spectral gap)", "LACKS: ES₅ is a fixed-length-3 word problem, no growing word length",
  "allow longer words with a constraint that collapses them to length 3 (as Zaremba's alphabet size tunes counts); check if a 'length-collapsing' identity exists",
  "Zaremba / Apollonian density-one results need orbits whose size grows as a power.",
  "None new (ZAREMBA_TRANSFER.md).", ["ZAREMBA_TRANSFER.md"], ["mech:expansion", "seen:ZAREMBA_TRANSFER.md"], effort="cheap")
F("function-field / large-q degeneration", "HAS proved variants over F_q[T]",
  "identify which F_q[T] proof step (RH for curves, large-q equidistribution) has an integer analogue in a 'large auxiliary parameter' regime",
  "Twin primes / Artin are proved over F_q[T] via RH for curves where ℤ needs GRH-plus.",
  "From FUNCTIONFIELD_ES*.md, extract the exact F_q[T] theorem and its 'q → ∞' mechanism.",
  ["FUNCTIONFIELD_ES.md"], ["function-field", "mech:large-q", "seen:FUNCTIONFIELD_ES.md"], effort="cheap")
F("parameter family crossing the dividing line", "IS the endpoint m = 4 of Schinzel's m/n family (Pomerance–Weingartner transition at p ≈ exp(m^{1/2+o(1)}))",
  "prove a monotonicity/interpolation statement: solvability of m/p for m' < m at all large p; or uniform-in-m count lower bounds",
  "Families that cross (5x+1 vs 3x+1, Hensley δ, m/n) localise where proof techniques stop.",
  "Compute R_m(p) for m = 4..20 and the same p; check whether R_m(p)·m/(log p)³ is stable (PW heuristic) and whether m = 4 shows anomalous excess.",
  ["arXiv:2511.16817"], ["family-crossing-line", "computation"], effort="cheap")
F("averaging over targets", "LACKS (pointwise in p)",
  "find a 'self-averaging' trick: express ES(p) as an average over an auxiliary family indexed by p's divisors of p-tied integers (amplification)",
  "Almost-all results (Vaughan) are via averaging; pointwise ones need amplification or rigidity.",
  "See AMPLIFY_EXCEPTION.md for prior attempts; list which amplifiers have not been tried.", ["AMPLIFY_EXCEPTION.md"], ["mech:amplification", "seen:AMPLIFY_EXCEPTION.md"], effort="cheap")
F("algebraic identity covering residue classes", "HAS identities for all non-square classes mod 840·k, blocked at squares (Mordell–Schinzel)",
  "use identities with growing level (parameters depending on p) — the (J)10 loophole: positivity from growing-level identities",
  "Demjanenko/5-cubes are proved by identities; ES identities are blocked exactly at squares.",
  "None new; tag the (J)10 loophole as the one feature-supply route the campaign flagged.", ["ES_APPROACH_GENERATORS.md"], ["mech:polynomial-identity", "growing-level"], effort="cheap")
F("reciprocity obstruction at a thin set (T1 at odd squares)", "HAS it, like Apollonian (HKRS), Rickards–Stange, flea orbits, Conjecture H at squares",
  "exploit it: obstruction theory often comes with a 'reciprocity-corrected' local-global principle that is provable in fat cases (Rickards–Stange)",
  "In the proved fat case, knowing exactly the obstruction gives the full answer; ES's analogue would be 'ES fails only for those certificate lines at squares'.",
  "Compute, for n = m² (m odd), the full set of certificate shapes that survive T1 and check that ES(m²) is always solved by non-line shapes (it is, trivially, since m² composite) — find the prime-level analogue.",
  ["T1_TEMPLATE.md"], ["obst:reciprocity", "T1-analogue", "seen:T1_TEMPLATE.md"])
F("unbounded constructive case analysis", "LACKS a known digit/recursive construction",
  "design recursive constructions driven by p's base-b digits or CF expansion of a/p (as palindrome theorem)",
  "Cilleruelo–Luca–Baxter proves a pointwise result by an explicit algorithm with finitely many local rules applied unboundedly.",
  "Check whether B1 (no finite ET covering) forbids digit-recursive constructions or only fixed-modulus coverings.",
  ["arXiv:1602.06208"], ["mech:constructive-algorithm"], conf="low")
F("effectivity of known partial results", "Vaughan-type bounds are effective; no ineffective input in sight",
  "allow ineffective inputs (Siegel zeros) — maybe a dichotomy: either no Siegel zero ⇒ ES for p ≫ 1, or Siegel zero ⇒ ES via Deuring–Heilbronn",
  "Some pointwise results (ternary forms, Linnik) are proved via Deuring–Heilbronn dichotomies.",
  "Check whether a Siegel zero would help ES (exceptional character makes primes ≡ some class rare — helps or hurts divisor-in-class events?).",
  [], ["mech:siegel-dichotomy"], conf="med")
F("algebraic structure of the target integer (Crocker exploited 2^{2^m}-type targets)", "target p is an arbitrary prime: no exploitable structure",
  "conversely, for disproof attempts, search p with special structure that might kill many certificate families simultaneously",
  "Crocker's failures came from targets with algebraic structure; ES counterexample searches might target analogous structure.",
  "List p ≡ 1 mod 840-class primes of special forms (p = 4^k·a + 1, p near squares) and compare R(p) to typical.",
  [], ["disproof-route", "computation"], effort="cheap")
F("dimension / number of variables", "3 variables with a single equation: below circle-method range",
  "add dummy variables with constraints (e.g. parametrised Type I/II as varieties of higher dimension with 2 equations) to reach circle-method range",
  "Hasse principle for integral points is provable for many-variable forms (Birch).",
  "Write the Type I parametrisation (a,d,f,…) as an affine variety and compute its dimension/degree; check Birch-type criteria.",
  [], ["mech:circle-method", "dimension"], conf="med")
F("strong approximation / integral points on homogeneous spaces", "the ES surface is not a homogeneous space",
  "find a homogeneous space (e.g. SL₂ or a torus) fibration over a parameter of the ES surface; integral points on fibres then follow from strong approximation",
  "Markoff mod p, ternary forms (spin groups) use strong approximation on groups.",
  "See STRONG_APPROX_ES.md for prior work.", ["STRONG_APPROX_ES.md"], ["mech:strong-approximation", "seen:STRONG_APPROX_ES.md"], effort="cheap")
F("positivity as the whole content", "rational/signed ES is trivial; positivity (archimedean condition) carries the problem",
  "treat positivity as an archimedean place condition in an integral Hasse principle and look for 'archimedean obstruction' theory (cf. Markoff positivity/reduction theory)",
  "Markoff Hasse failures arise from reduction-theory (archimedean) constraints, not BM.",
  "Compare the Ghosh–Sarnak reduction-theory failures with ES's positivity constraint: is there an ES 'fundamental domain' argument?",
  ["arXiv:1706.06712"], ["archimedean", "integral-points"])
F("monotone structure in the number of terms k", "ES is k = 3; k = 2 completely classified (Stewart); k ≥ 4 has power counts",
  "use the k = 2 classification as a sieve: ES(p) holds if some explicit p-tied integer N has a coprime-divisor pair (a,b) with 4 | a+b … i.e. reduce to many k = 2 problems",
  "Interpolating between a classified and an open case is a classic route.",
  "Formalise: ES(p) ⟺ ∃x: 4/p − 1/x is a 2-term fraction; apply Stewart's criterion to (4x − p)/(px) for x in [p/4, 3p/4].",
  ["Pomerance slides 2026 (Stewart theorem)"], ["egyptian", "k=2-reduction"], conf="high", effort="cheap")
