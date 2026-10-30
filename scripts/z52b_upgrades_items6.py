# Items batch 6: third pass — odd items, new catalogue entries, cross-template items.

I("SHORT", "Distribution of certificates across dyadic level ranges",
  "Primes in every short interval vs almost all: the analogue at fixed p is whether certificates appear in every dyadic level range [K, 2K] (K ≤ p^{1/2}) or cluster. With R(p) ≍ log²p spread over ≍ log p dyadic ranges, ≍ log p certificates per range are expected.",
  "If every dyadic range typically carries certificates, a proof could target one range of convenient size (e.g. C ≈ p^{1/3}) where tools are best; if they cluster, that range is fixed by the data.",
  "For p ≤ 10¹⁰ in the hard list, histogram certificates by ⌊log₂ C⌋ and record the empty ranges.",
  ["levels", "dyadic-ranges", "numerics"], "high", "cheap")
I("SHORT", "Saving in x versus saving in H: the exact form an every-n exceptional bound must take",
  "Every-interval results for primes need savings depending on the location x, not only on the interval length H. For ES, (D)30 gives E(I) ≪ H exp(−c(log H)^{3/4}); a bound E(I) ≪ H·exp(−c(log x)^θ) uniform down to H = 1 would be < 1 for H ≤ exp(c(log x)^θ), hence ES. So the target is an x-dependent saving in short intervals.",
  "Makes precise how 'almost all in short intervals' must improve to reach 'every': any argument giving savings in log x at fixed small H is already pointwise.",
  "Re-examine the (D)30 proof and identify where the saving is tied to H (the number of n averaged) rather than to x; ask whether any piece gives x-dependent savings.",
  ["exceptional-set", "short-intervals", "quantifiers"], "high", "cheap", seen=["EXCEPTIONAL_KARY3.md"])
I("LINNIK", "Extreme-value statistics of the least certificate parameter",
  "Linnik-type theorems bound the least prime in a class. Measure the least certificate parameter (least C for (★), least e for windows) as p grows and fit an extreme-value law; a provable bound of the observed shape would be the 'Linnik constant' of ES.",
  "Calibrates which quantitative statements are plausible (e.g. C(p) ≤ (log p)^A for all p?) before trying to prove any.",
  "From the repo's census (and adversarial primes at 10¹⁸–10²⁵) tabulate max over p ≤ X of least C and least e versus log X.",
  ["least-certificate", "extreme-values", "numerics"], "high", "cheap", seen=["DISPROOF_AVENUES.md"])
I("HASSE", "Integral Brauer–Manin for the (u,B,C) threefold as a family of affine conics over the C-line",
  "For fixed C, (★) is the hyperbola (4uC − 1)(4BC − 1) = 4Cp + 1, an affine conic. Integral Hasse/BM results for families of affine quadrics (Colliot-Thélène–Xu, strong approximation with BM) treat such fibrations; analyse the total space over the C-line.",
  "BL computed Br for the ES surface; the (u,B,C) threefold is a different model where fibrewise integral BM is classical.",
  "Compute the Brauer group of the generic fibre (a split conic? then trivial) and the integral obstruction for the total space; compare with BL's ℤ/2.",
  ["integral-points", "brauer-manin", "conic-bundles"], "med", "medium")
I("BURGESS", "Vinogradov's smooth-number trick for divisor classes",
  "Vinogradov bounded n(p): if every ℓ ≤ y is a QR, all y-smooth numbers are QRs, contradicting character-sum bounds since smooth numbers are plentiful. ES: if level C fails, no divisor of 4Cp+1 is ≡ −1 (mod 4C); if additionally we know the classes of small primes, smooth parts of 4Cp+1 are constrained. Count C for which 4Cp+1 has a y-smooth divisor in a forced class.",
  "Transfers a proven every-p argument shape (n(p) bounds) to divisor classes, using smooth numbers in APs (Granville, Harper).",
  "Model: fix the classes mod 4C of primes ≤ y; count C ≤ X such that 4Cp+1 has a y-smooth divisor d ≡ −1 (mod 4C) using smooth-number distribution; compare with data.",
  ["smooth-numbers", "vinogradov-trick", "least-nonresidue"], "med", "medium")
I("FLT", "Kummer-style 'regular' primes for ES: an invariant κ(p) that makes ES provable",
  "Kummer proved FLT for regular primes (p ∤ class number) long before Wiles. Look for an arithmetic invariant κ(p) (class number of ℚ(√−p), 2-rank/4-rank, parity of the fundamental unit norm of ℚ(√p), ℓ(p)) such that ES (or a sub-route) is provable for all p with κ(p) in some set, giving an infinite every-p family.",
  "Partial every-p theorems on natural infinite sets of Mordell-hard primes do not yet exist; Kummer's theorem is the historical model.",
  "Correlate (★)/ES₅ counts with κ(p) candidates for p ≤ 10⁸ and look for an invariant whose small/large values guarantee many certificates.",
  ["regular-primes", "invariants", "intermediate-target"], "med", "cheap")
I("SATO", "Limiting distribution of R(p)/M_BM(p) (a Sato–Tate/Cohen–Lenstra-type law)",
  "Sato–Tate identified the exact limiting law of normalised a_p. For ES, determine the limiting distribution of R(p)/M_BM(p) (and of f(p)/log³p) as p → ∞ through Mordell-hard primes; its behaviour near 0 is what decides ES heuristically.",
  "A precise conjectural law with a computable left tail sharpens the heuristic case for ES and indicates which normalisation is 'right'.",
  "Histogram R(p)/M_BM(p) for primes in windows at 10⁶, 10⁸, 10¹⁰; test convergence and fit the left tail.",
  ["limiting-distribution", "left-tail", "numerics"], "high", "cheap")
I("ONO", "Ramanujan-type congruences for ES counts on progressions",
  "Ramanujan/Ono congruences say p(An + B) ≡ 0 (mod m). Search for progressions An + B on which f_II(n) or R(n) is always ≡ 0 (mod m) (m = 2, 3, 4, 8) beyond the trivial evenness; such congruences would reveal modular structure that might also produce nonzero congruences at primes.",
  "Systematic congruence mining is cheap and has historically uncovered hidden modular structure.",
  "Compute f_II(n), R(n) for n ≤ 10⁷ and test all A ≤ 840, B mod A for congruences mod 2, 3, 4, 8.",
  ["congruences", "data-mining", "modular-structure"], "high", "cheap")
I("MARKOFF", "ES as an orbifold Euler-characteristic realisation problem (triangle groups, Hurwitz spaces)",
  "Chen's Markoff theorem is a statement about Hurwitz spaces. Note: 1/x + 1/y + 1/z − 1 is the orbifold Euler characteristic of the sphere with cone points of orders x, y, z. So ES(p) ⟺ some triangle orbifold S²(x,y,z) has χ^orb = (4 − p)/p, i.e. hyperbolic area 2π(p − 4)/p.",
  "Gives ES a geometric/topological reading where covering-space and Hurwitz-space divisibility arguments (as in Chen) might apply.",
  "Work out what Riemann–Hurwitz says for covers of S²(x,y,z) with χ = (4 − p)/p (index must be divisible by p); look for a moduli space whose nonemptiness is equivalent to ES(p).",
  ["triangle-groups", "orbifolds", "hurwitz-spaces"], "med", "medium", kw=["triangle group"])
I("CFT", "Prime-capture problems: every prime is caught by an infinite family of Chebotarev conditions",
  "Chebotarev forbids any finite family of splitting conditions from catching every prime; ES Type II (abelian conditions p ≡ −(u+B) mod 4uB) and Type I (dihedral conditions via ring class fields) are infinite families with conductors up to ≍ p. List known 'every prime is captured by a family with conductor ≤ f(p)' theorems (e.g. least non-residue: some ℓ ≤ p^{0.152} has (p/ℓ) = −1) and place ES among them.",
  "Identifies the closest proven 'prime-capture' statements and how their conductor bounds compare with what ES needs.",
  "Write the conductor/size of the capturing family for ES sub-routes and for known capture theorems (Burgess, Linnik, Vinogradov) in one table.",
  ["prime-capture", "chebotarev", "conductors"], "med", "cheap")
I("TWOSQ", "Class-number parity (genus theory, Rédei) as the source of oddness for a Zagier-type argument",
  "Heath-Brown's/Zagier's proofs use a set whose size parity is forced. Natural sets attached to p have sizes tied to class numbers h(−4p), h(−8p), whose parities/2-parts are governed by genus theory and Rédei symbols. Find an ES-related finite set whose cardinality equals (up to known even terms) such a class number with known parity.",
  "Supplies the 'odd cardinality' input a parity proof needs from established theory.",
  "Compute |S_p| for candidate sets (e.g. reduced forms of disc −16p with an extra congruence) and compare parity with h(−4p), h(−8p) and Rédei-symbol predictions.",
  ["parity", "class-numbers", "genus-theory"], "low", "medium")
I("FI", "Polynomial certificate families in the Gaussian variables (a,b), p = a² + b²",
  "Mordell–Schinzel forbids polynomial identities in n covering the square classes; identities in the variables (a, b) with p = a² + b² are a different class. T1 requires that at odd-square points (Pythagorean (a,b)) such an identity yield only non-Type-I/II (imprimitive) solutions, which is not obviously impossible.",
  "A genuinely new parametrisation space for identity searches, exactly where the classical obstruction may not bite.",
  "Search low-degree X, Y, Z ∈ ℚ[a,b] with 4XYZ = (a²+b²)(XY+YZ+ZX) identically and X,Y,Z positive integral on a congruence region; check behaviour at Pythagorean points.",
  ["identities", "gaussian-integers", "mordell-schinzel"], "med", "medium")
I("THREESQ", "Genus-theoretic parametrisations: Mordell-hard primes as values of principal-genus forms",
  "Gauss's genus theory: p is a square mod 840-type moduli iff p lies in principal genera of the relevant discriminants, so p = Q(x, y) for a form Q in a principal genus (disc −4·210 etc.). Seek certificate families polynomial in (x, y) for p = Q(x, y), exploiting that Mordell-hard classes are exactly where these representations exist.",
  "Turns 'square classes' from an obstacle into a parametrisation: hard primes come with extra representations.",
  "For Mordell-hard primes ≤ 10⁷, compute representations by forms of discriminants dividing −4·840 and correlate (x, y) with known certificates (u, B, C).",
  ["genus-theory", "parametrisation", "square-classes"], "med", "cheap")
I("SYLV", "Large prime factors in the AP {4Cp + 1 : C ≤ K} (Sylvester–Schur/Shorey–Tijdeman)",
  "Sylvester–Schur: products of consecutive integers have a large prime factor; Shorey–Tijdeman extend to AP terms. For ES, a single prime q | 4Cp+1 with q ≡ −1 (mod 4C) is a certificate. Large prime factors are guaranteed in the product over C ≤ K; the class condition q ≡ −1 (mod 4C) is the extra requirement.",
  "Gives a guaranteed supply of large prime divisors; the problem reduces to a class-distribution question for these forced large primes.",
  "For p ~ 10⁹, list the largest prime factor of 4Cp+1 for C ≤ 10⁴ and test the rate at which it is ≡ −1 (mod 4C) against 2/φ(4C)-type models.",
  ["large-prime-factors", "residue-classes", "numerics"], "med", "cheap")
I("SYLV", "Legendre-formula bookkeeping for Π_C(4Cp+1): which primes can make up the product?",
  "Sylvester–Schur works by bounding the contribution of small primes via Legendre's formula. For Π_{C≤K}(4Cp+1) the contribution of each prime q is explicit by CRT (q divides the terms with C ≡ c_q mod q). Compute the share of the product coming from primes q that could serve as single-prime certificates, versus the rest.",
  "Makes the 'size argument' quantitative: if certificate-capable primes must contribute a definite share of log Π, one of them must divide some term in the right class.",
  "Compute Σ_{q} (number of C ≤ K with q | 4Cp+1)·log q split by whether 4c_q | q+1-type conditions can hold.",
  ["size-argument", "legendre-formula", "CRT"], "low", "cheap")
I("ERDSELF", "Erdős–Selfridge distinct-small-parts mechanism for consecutive levels",
  "Erdős–Selfridge: writing consecutive factors as a_i·(power) forces the a_i to be distinct and small, contradiction by counting. ES failure forces each 4Cp+1 (C = 1, …, K) into a thin multiplicative set S_C; write 4Cp+1 = a_C·b_C with b_C the S_C-compatible part and look for a forced-distinctness/smallness contradiction among the a_C.",
  "An elementary combinatorial mechanism for consecutive terms that might bite on the explicit sets S_C at small C.",
  "For C ≤ 8 characterise S_C explicitly (e.g. S_1: all prime factors ≡ 1 mod 4) and test numerically how small K can be such that no prime has 4Cp+1 ∈ S_C for all C ≤ K... (there are such primes for each K; record their density decay).",
  ["elementary", "multiplicative-sets", "consecutive-levels"], "low", "cheap")
I("REINGOLD", "Instance transformation that preserves certificate existence but amplifies counts",
  "Reingold transformed every graph into an expander while preserving connectivity. ES: find a transformation p ↦ (structured object with power-many 'attempts') such that ES(p) ⟺ the object has a 'connected/nonzero' property that is robustly detectable (e.g. a spectral quantity), amplifying the polylog main term.",
  "If the count can be amplified while preserving the zero/nonzero status, the polylog-main-term barrier (B2) changes character.",
  "Look at natural equivalences ES(p) ⟺ ∃e (window) and ES(p) ⟺ ∃C (level); build a graph on (e, divisors of N_e) whose connectivity property is equivalent to ES(p), and compute its spectral gap for small p.",
  ["amplification", "derandomization", "graphs"], "low", "medium")
I("REINGOLD", "Randomized certificate search with provable success → derandomize",
  "Before Reingold, connectivity was in randomized logspace. ES certificates are found by trying random e or C; a proof that a random attempt succeeds with probability ≥ 1/poly(log p) for every p would already be ES; the derandomization view asks for an explicit small 'hitting set' of attempts for every p.",
  "Hitting-set language matches B1's analysis of bounded procedures and suggests pseudorandom-generator constructions (attempt sets that fool the certificate test).",
  "Define the certificate test as a function of the attempt (e, or C); compute the minimal hitting set for all primes ≤ 10⁸ and its growth.",
  ["hitting-sets", "derandomization", "B1"], "med", "cheap", seen=["POINTWISE_SIZE.md"])
I("WEDD", "Wielandt-style orbit counting: a group action whose non-certificate orbits have size ≡ 0 (mod m)",
  "Wielandt proves Sylow existence because |X| = C(p^a m, p^a) ≢ 0 (mod p), so some orbit has size prime to p. ES: find a finite set X_p (e.g. 4-term or 'imprimitive' representations, or divisor configurations) with a group G (ℤ/3 permuting coordinates, S₃, or a dihedral group of moves) acting so that every orbit not containing a certificate has size divisible by m while |X_p| ≢ 0 (mod m).",
  "Generalises the Zagier involution (m = 2) to larger groups where the needed congruence of |X_p| may be easier to establish.",
  "Enumerate candidate (X_p, G) pairs for small p and check orbit-size divisibility; look for one where |X_p| mod m is given by a formula in p.",
  ["orbit-counting", "group-actions", "congruences"], "med", "medium")
I("WEDD", "Class-equation divisibility: Φ_n(q)-type obstruction to 'no certificate'",
  "Witt's proof of Wedderburn: the class equation has all terms but one divisible by Φ_n(q), forcing a contradiction. For ES, write an exact counting identity for a quantity attached to p (e.g. Σ_C τ(4Cp+1) over a full period, or a divisor-class census over (ℤ/4C)*) as a sum over 'orbits' where all non-certificate terms are divisible by some cyclotomic-type number.",
  "A divisibility contradiction needs no asymptotic analysis.",
  "Look for counting identities over complete residue systems (C mod q) where certificate-free contributions have a forced common factor.",
  ["divisibility", "counting-identities", "odd"], "low", "medium")
I("MSS", "Arithmetic constructions cover some classes, interlacing covers all: the LPS → MSS lesson",
  "LPS/Morgenstern built Ramanujan graphs arithmetically only for degrees d − 1 = prime power; MSS proved existence for every d by a non-arithmetic existence method (interlacing families). ES: Mordell identities (arithmetic) cover all non-square classes mod 840; the square classes may need a non-identity existence method of a comparable kind.",
  "Historical precedent that 'arithmetic constructions stop at a class barrier, existence methods cross it'.",
  "Identify the analogue of 'expected characteristic polynomial' for ES: a polynomial built from the family of attempts (levels C or windows e) whose real-rootedness/root location certifies existence for some member.",
  ["interlacing", "existence-method", "square-classes"], "med", "medium", seen=["BRAINSTORM/z45_interlacing_stable.md"])
I("MSS", "Interlacing families over windows: real-rooted averages certify a good window",
  "MSS: if a family of real-rooted polynomials has a common interlacer, some member's largest root is ≤ that of the average. Define for each window e a polynomial f_e(t) (e.g. Π over prime factors q of N_e of (t − Re χ(q)) for a character χ mod e with χ(−1) = −1) whose root location detects certificates; average over e.",
  "Converts 'some e works' into a statement about an averaged polynomial, which can be computed or estimated.",
  "Construct toy f_e for small e, test interlacing numerically for hard p, and check whether the average polynomial's root implies a certificate for some e.",
  ["interlacing", "real-stable-polynomials", "windows"], "low", "medium")
I("GL", "Exceptional set of the two-term step is tiny: 'almost all two-term + rescue' structure",
  "Goldbach–Linnik used that the binary Goldbach exceptional set is small enough for a sparse rescue set. In ES, the two-term step m/N = 1/y + 1/z (after choosing x) fails on a thin set of (m, N); show that for every p, among the ≍ p choices of x the pairs (m_x, N_x) cannot all lie in that thin set, using its explicit structure.",
  "The thin exceptional set of the two-term problem is explicit (divisor-class avoidance), so 'cannot all avoid' is a concrete combinatorial statement.",
  "Characterise {(m, N) : m/N not a sum of two unit fractions} for small m and compute the fraction of x ∈ (p/4, p/2) for which (4x − p, px) lands in it, for hard p.",
  ["two-step", "exceptional-set", "rescue-family"], "high", "cheap")
I("WILSON", "Eventual periodicity of 'ES-easy' residue structures (Wilson-style)",
  "Wilson showed the set of orders admitting designs is eventually periodic, so finitely many residue classes need checking. For ES sub-routes, test whether 'the set of levels C at which the BM main term is positive for all p in a class r mod M' is eventually periodic in C, giving a finite description of guaranteed-positive levels.",
  "Eventually periodic structures can be checked by finite computation and then fed into an every-p argument.",
  "For M = 840, compute for each hard class r the set of C ≤ 10⁴ with M_C^lev > 0 for all p ≡ r (mod M·4C) and test periodicity in C.",
  ["periodicity", "BM-layer", "finite-description"], "med", "cheap")
I("THOM", "Precoloured version: ES with a prescribed denominator divisible by a given small prime",
  "Thomassen's induction works for a stronger precoloured statement. Candidate strengthening: for every prime p and every small prime r, there is an ES solution with r | x (or r ∤ any denominator). If such a refined statement holds numerically, its extra structure might allow an induction over r or over the e-slice.",
  "Strengthenings with an inductive parameter are how many every-n combinatorial theorems were proved.",
  "For p ≤ 10⁶, check which (r, condition) refinements hold for all p; record the first failure for each.",
  ["strengthening", "induction", "refinements"], "med", "cheap")
I("HOUGH", "Uncovered density of the (★) system restricted to moduli with bounded prime factors",
  "Hough's argument tracks how the uncovered set shrinks as primes are added to the moduli. Restrict ES congruences p ≡ −(u+B) (mod 4uB) to moduli 4uB built from primes ≤ y; compute the uncovered density δ(y) among integers in the hard classes and its decay in y.",
  "A precise decay law for δ(y) (power of log y? exp?) quantifies how many prime 'layers' certificates need — a structural fingerprint of ES.",
  "Compute δ(y) for y ≤ 50 by inclusion over moduli dividing a bounded smooth number, restricted to n ≤ 10⁸ in hard classes.",
  ["covering-systems", "smooth-moduli", "density-decay"], "high", "cheap")
I("DS", "Variance-to-mean ratio of R(p) as a quasi-independence diagnostic",
  "Koukoulopoulos–Maynard's key was showing overlaps are small on average (quasi-independence). For ES, the variance of R(p) over primes near X relative to its mean measures overlap; Poisson-like behaviour (ratio ≈ 1 after removing the genus fluctuation) indicates quasi-independent events.",
  "If the residual variance after the BM/genus layer is ≈ mean, the second-moment method is near-optimal and the remaining obstacle is purely the 'single realisation' issue.",
  "Compute Var(R(p) − M_BM(p))/E[R(p)] in windows at 10⁶, 10⁸, 10¹⁰.",
  ["variance", "quasi-independence", "numerics"], "high", "cheap", seen=["BM_CORRECTED_COUNT.md"])
I("ZSIG", "Primitive part of 4Cp+1 relative to smaller levels as a 'new divisor' source",
  "Zsigmondy isolates primes dividing a^n − 1 but no earlier term. For fixed p, call a prime factor q of 4Cp+1 'new' if q ∤ 4C′p+1 for C′ < C (equivalently c_q = C). New primes have c_q = C < q, and a new prime q is a single-prime certificate iff 4C | q + 1. Study the number of new primes at each level.",
  "New-prime counts give an explicit, level-ordered supply of candidates with a clean certificate test.",
  "For p ~ 10⁸ and C ≤ 10⁵ compute the new primes at each level and the frequency of 4C | q + 1.",
  ["primitive-divisors", "levels", "numerics"], "med", "cheap")
I("CAT", "From Tijdeman (effective finiteness) to Mihăilescu (exact): bound first, then algebra",
  "Catalan moved from 'finitely many, bounded effectively' to 'exactly one' via algebra that did not need the bound. For ES-type finiteness targets (e.g. finitely many (★)-failures), an algebraic characterisation of failures (all 14 known (★)-failures share a property P) might give the exact list without analysis.",
  "The 14 known (★)-failures ≤ 10¹⁰ are a finite data set where an exact algebraic description is testable.",
  "List the 14 primes with their factorisations of 4Cp+1 for small C, residues mod 840·k, and ℓ(p); look for a shared algebraic property and test it as a predictor above 10¹⁰.",
  ["exact-classification", "sub-routes", "numerics"], "med", "cheap", seen=["B1_LINE.md"])
I("GZK", "Euler-system-style bounds on the 'obstruction group' of certificate-free levels",
  "Kolyvagin bounded Selmer groups with an Euler system of Heegner points. Define for p the 'obstruction group' O_p = set of levels/windows that fail with their local data; a norm-compatible system of near-certificates across levels (if it existed) would bound O_p and force it to be smaller than the set of all levels.",
  "Highly speculative, but Euler systems are the one tool that converts a supply of compatible objects into a bound on an obstruction.",
  "First check whether near-certificates at levels C | C′ satisfy any norm/trace compatibility (e.g. divisor classes mod 4C′ reducing to classes mod 4C).",
  ["euler-systems", "speculative", "obstruction-group"], "low", "big")
I("KAKEYA3", "Furstenberg-set analogue: certificate 'lines' in the (C, d) plane",
  "Kakeya/Furstenberg estimates bound unions of lines/tubes from below. For fixed p, each prime q gives the 'line' {C ≡ c_q (mod q)} of levels where q | 4Cp+1; certificates are incidences of these lines with the conditions 4C | (product of chosen q's) + 1. An incidence-geometry lower bound might force a certificate.",
  "Incidence bounds are robust every-configuration statements; ES at fixed p is an incidence problem between residue lines and divisibility conditions.",
  "Plot, for small p, the incidence structure (q, c_q) and the certificate incidences; ask for the right incidence theorem (Szemerédi–Trotter over ℤ/q? Bourgain–Katz–Tao in F_q?).",
  ["incidences", "furstenberg-sets", "odd"], "low", "medium")
I("CAPSET", "Slice-rank of the ES 'certificate tensor' modulo q",
  "The cap-set proof bounds sets avoiding a pattern via the slice rank of the pattern's indicator tensor. Consider the tensor T(u, B, C) = 1[4uBC − u − B ≡ p (mod q)] over F_q³; its slice rank bounds how large a product set of parameter values can avoid certificates mod q.",
  "Gives polynomial-method bounds on 'certificate-avoiding parameter sets' mod q, a local statement with sharp constants.",
  "Compute the slice rank (or a polynomial-method upper bound) of T for small q and compare with the largest avoiding product sets found by search.",
  ["slice-rank", "polynomial-method", "local"], "low", "medium")
I("UNIONCL", "Union-closed structure of the family of ES-solvable sets of numerators",
  "Gilmer's method applies to union-closed families. For each n, the set A_n = {m : m/n is a 3-term Egyptian fraction} — is the family {A_n} (or its complements) closed under unions/intersections in a way that forces a frequent element (a numerator m that works for most n)? For m = 4 the conjecture is 'all n'.",
  "Odd, but the numerator–denominator incidence structure (with 8/n failing at 131, 241) is a natural set system to analyse with these tools.",
  "Compute A_n ∩ [1, 30] for n ≤ 10⁵ and test closure properties and element frequencies.",
  ["set-systems", "numerator-family", "odd"], "low", "cheap")
I("PARK", "Is ES critical or supercritical? Fractional expectation threshold of the level hypergraph",
  "Park–Pham relate thresholds to expectation thresholds. The repo measures ≈ (0.44 → 0.97)·log p expected hit levels (critical regime). Compute, in a random model matching ES's level statistics, the threshold for 'some level hits' and see whether ES sits above it by a growing margin.",
  "If ES is only 'critically' above threshold in natural models, any proof must exploit non-random structure; if supercritical, second-moment-type methods are favoured.",
  "Simulate the matched random model and compute P(no hit) as a function of the scaling parameter; compare with data for hard primes.",
  ["thresholds", "criticality", "random-models"], "med", "cheap", seen=["SYNTHESIS_SPARKS9.md"])
I("GRAHAM77", "Classify all 'transfer maps' between ES instances via the e-slice",
  "Graham's closure maps transfer representability from n to 2n+2, 2n+9. For ES, the e-slice transfers between p and N = (p+e)/4. Classify maps T: (N, e) ↦ (N′, e′) such that a certificate for (N, e) yields one for (N′, e′); a rich enough transfer system could connect every instance to verified ones.",
  "Transfer systems are the engine of closure-type every-n proofs.",
  "Search small linear maps (N, e) ↦ (aN + b, ce + d) preserving −1 ∈ Rat_e(N) on all data with N ≤ 10⁶.",
  ["closure-operations", "e-slice", "transfer"], "low", "cheap")
I("BLOOM", "Harmonic-sum thresholds for the denominator set of ES solutions",
  "Liu–Sawhney: a set A ⊂ [1, N] with Σ_{n∈A} 1/n ≥ (log N)^{4/5+o(1)} contains S with Σ_{S} 1/n = 1. ES solutions for p use denominators in {multiples of p} ∪ {numbers ≈ p/4 … p²}; compute the 'harmonic mass' of the possible denominator sets and compare with such thresholds (for 3 terms, thresholds are presumably different, but the bookkeeping shows the gap).",
  "Quantifies how far ES is from the regime where density-based unit-fraction theorems apply.",
  "Compute Σ 1/n over the set of denominators appearing in any ES solution for p (data) and over natural supersets.",
  ["harmonic-sums", "egyptian-fractions", "gap-analysis"], "low", "cheap")
I("KNESER", "Antipodal structure: the swap involution u ↔ B as a free ℤ/2-action on near-certificates",
  "Borsuk–Ulam/Tucker need a free ℤ/2-action. The (★) data (u, B) ↦ (B, u) is a ℤ/2-action, free off the diagonal u = B; certificates come in swap pairs (R(p) even). Study the ℤ/2-index of the space of near-certificates (a cell complex over levels) — a non-trivial index would force a fixed configuration, i.e. a certificate.",
  "Uses a symmetry ES already has (R(p) even) in a topological rather than parity way.",
  "Build a small complex for p ≤ 10³ (cells = near-certificates, faces = relaxations) and compute its ℤ/2-index.",
  ["topological-method", "Z2-index", "symmetry"], "low", "medium", seen=["BRAINSTORM/invol_topological.md"])
I("MR", "Multiplicative-function structure of the level indicator at fixed p",
  "MR's method uses multiplicativity in n. At fixed p, the function C ↦ D_C(p) is not multiplicative in C, but N ↦ 1[N has a divisor ≡ −1 mod t] is 'multiplicative-ish' in N for fixed t. Study the Dirichlet-series/Halász structure of n ↦ D_t^−(tn + 1) for fixed t (its mean value over n is controlled by Halász-type theorems).",
  "Halász/MR techniques give 'every interval of length h' results for multiplicative functions; level-t certificate indicators along n might be accessible.",
  "Express 1[D_t^−(tn+1) > 0] via the multiplicative set S_t and compute its mean in short intervals of n numerically; compare with Landau–Ramanujan-type predictions.",
  ["multiplicative-functions", "halasz", "levels"], "med", "medium")
I("NEGPELL", "Rédei-type reciprocity explains T1 — look for its 'higher' analogues in ES sub-routes",
  "Negative Pell's obstructions beyond local ones come from Rédei symbols (higher reciprocity). T1 is a quadratic-reciprocity cancellation. Search for Rédei-symbol-type (quartic/biquadratic) conditions that predict extra failures of sub-routes ((★), b=1, ES₅) among primes, beyond what the BM/genus layer explains.",
  "If found, such conditions refine the main term (like Stevenhagen's refinement) and sharpen targets; if absent, the genus layer is complete.",
  "Compute Rédei symbols [a, b, p] for small a, b and correlate with (★) failures / low counts.",
  ["redei-symbols", "reciprocity", "numerics"], "med", "cheap")
I("SHAF", "Auxiliary-prime choice with prescribed local behaviour for windows",
  "Shafarevich's embedding-problem induction succeeds by choosing auxiliary primes with prescribed local behaviour at each step. For ES windows, choose the window prime q with prescribed splitting behaviour in fields built from p (e.g. q splits in ℚ(√p, i) or has given Frobenius in a Kummer extension) so that Rat_q(K) is forced to contain −1.",
  "Chebotarev guarantees auxiliary primes with any prescribed Frobenius; if the window certificate were a Frobenius condition, existence would follow.",
  "Test whether success of window q for p is predicted by the Frobenius of q in ℚ(ζ_8, √p) or in Kummer fields ℚ(ζ_4, p^{1/4}).",
  ["auxiliary-primes", "chebotarev", "windows"], "med", "cheap", seen=["FORCED_WINDOW.md"])
I("HARDYZ", "Positive proportion of levels with a certificate is false — find the right normalisation",
  "Selberg's positive-proportion step needed the right normalisation (zeros up to height T). For ES at fixed p, only ≍ log²p of ≍ p levels carry certificates; identify the natural finite set of 'attempts' of which a positive proportion succeed (e.g. levels C ≤ (log p)^A, windows e ≤ (log p)^B with weights), so that a positive-proportion statement would be meaningful and imply ES.",
  "A positive-proportion statement over a small set of attempts is a pointwise statement; finding the set where proportions are stable is the first step.",
  "For hard primes, compute success proportions over attempt sets of various shapes and sizes; find shapes where the proportion stays bounded below as p grows.",
  ["normalisation", "attempt-sets", "positive-proportion"], "high", "cheap")
I("LITTLE", "Measure-rigidity on the adelic space of 'residue profiles' of p",
  "EKL used higher-rank diagonal actions and entropy. The residue profile of p (its classes modulo all 4C) lives in Ẑ; the joint action of multiplication by many integers on Ẑ is 'higher rank'. Ask whether invariant measures for such actions with positive entropy are classified, and whether ES-failing profiles would support an invariant measure.",
  "A structural (measure-rigidity) description of the profinite failure set could bound its 'dimension' (Littlewood-style intermediate result).",
  "Formulate the action of (ℕ, ×) on Ẑ restricted to the closure of ES-failing profiles, and check against Furstenberg/Rudolph-type rigidity statements for ×a, ×b actions on solenoids.",
  ["measure-rigidity", "profinite", "higher-rank"], "low", "big")
I("VIAZ", "Fourier interpolation/uniqueness: ES data at primes determine a function vanishing somewhere?",
  "Radchenko–Viazovska Fourier interpolation shows a function is determined by values at √n. Odd idea: the function n ↦ R(n) (or its smoothed version) is determined by data on a sparse set via modular identities (Thm K); if R vanished at p, interpolation formulas would force a contradiction with positivity elsewhere.",
  "Interpolation/uniqueness theorems from modular forms are a way to transfer information between sparse and dense sets of n.",
  "Check whether Thm K level series admit Rademacher/Fourier-interpolation-type formulas expressing R(p) via values at other n with explicit kernels.",
  ["fourier-interpolation", "modular-forms", "odd"], "low", "big")
I("RINGEL", "Hardest residue cases needed new constructions: identify ES's 'case 3 mod 12'",
  "In Ringel–Youngs some residue classes (e.g. cases 1, 9 mod 12) took years and ad hoc ideas. Among the six Mordell-hard classes mod 840 (1, 121, 169, 289, 361, 529), measure which is hardest (lowest counts, most sub-route failures) and focus constructions there.",
  "Concentrating effort on the hardest class mirrors the historical endgame.",
  "From census data, compute per-class mean/minimum of R(p)/log²p and sub-route failure counts.",
  ["case-analysis", "hard-classes", "numerics"], "high", "cheap")
