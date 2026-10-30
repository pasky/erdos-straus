# Items batch 8: fifth pass — baselines, failed-upgrade lessons, more cross-field items.

I("TG", "No minor arcs: positivity lets ES discard all but the smallest levels",
  "Goldbach-type proofs must bound minor arcs because terms cancel. ES counts are sums of nonnegative level counts, R(p) = Σ_C D_C(p) ≥ Σ_{C ≤ K} D_C(p); so ES ⟸ a certificate among levels C ≤ K = (log p)^A, where the expected count is still ≍ (log p)·(log K) → ∞. The whole problem is a lower bound for a short, explicit 'major-level' sum.",
  "Reframes which part of the analytic machinery is needed: only lower bounds on a few explicit structured counts, no cancellation estimates for the bulk.",
  "For p in the hard lists, find the least K(p) such that some level ≤ K(p) carries a certificate, and fit K(p) against (log p)^A.",
  ["positivity", "major-levels", "reframing"], "high", "cheap")
I("BERT", "Baseline: a single level already gives density one",
  "Level C = 1 works for p iff 4p + 1 has a prime factor ≡ 3 (mod 4) (it then automatically has two, so both cofactors are ≥ 3); the primes p for which 4p + 1 has only prime factors ≡ 1 (mod 4) have density zero (≍ X/(log X)^{3/2}). So 'almost all p' is cheap; all information sits in how fast the exceptional set of K levels decays.",
  "A sanity baseline for every almost-all statement in this list: improvements must be measured in exceptional-set decay, not in 'density one'.",
  "Compute the counting function of primes failing all levels C ≤ K for K = 1..10 up to 10⁹ and fit X/(log X)^{α_K}; compare α_K with Σ_{C≤K} δ_C from Landau–Ramanujan-type densities.",
  ["baseline", "exceptional-set", "multiplicative-sets"], "high", "cheap")
I("BERT", "Sieve of growing dimension: when do the thin sets S_C (C ≤ K) exhaust all primes?",
  "Failing levels 1..K means 4Cp + 1 ∈ S_C for all C ≤ K, an intersection of thin multiplicative sets of total 'dimension' Σ_{C≤K} δ_C. Upper-bound sieves for such intersections are standard for fixed K; ES needs K growing with p until the expected number of survivors near X is < 1 — a sieve problem of growing dimension.",
  "Puts the ES exceptional-set question in the language of high-dimensional sieves (Diamond–Halberstam–Richert), where the dependence on dimension is explicit.",
  "Compute Σ_{C≤K} δ_C as a function of K and the K(X) at which X·(log X)^{−Σδ} < 1; compare with the observed least K(p).",
  ["sieve-dimension", "exceptional-set", "thin-sets"], "high", "cheap")
I("EDP", "Pretentious distance D((·/p), 1; y) as the controlling statistic for ES difficulty",
  "Tao's EDP and Granville–Soundararajan's pretentious theory organise multiplicative functions by their distance to characters. The BM main term (via T(p)) and the least non-residue are governed by how much the Legendre symbol (·/p) 'pretends' to be 1 on small primes. Test whether all ES sub-route difficulty is a function of D((·/p), 1; y) for suitable y.",
  "If one pretentious distance controls difficulty, the problem reduces to the 'pretentious case' (p a QR mod many small primes), where structure is strongest.",
  "Compute D² = Σ_{ℓ ≤ y} (1 − (ℓ/p))/ℓ for primes ≤ 10⁹ and correlate with R(p)/M₀(p), least certificate C, and sub-route failures.",
  ["pretentiousness", "character-bias", "numerics"], "high", "cheap", seen=["BRAINSTORM/bsB_sterile_pretentious.md"])
I("BGEXP", "Affine-sieve strengthening: certificates with prime or almost-prime parameters",
  "Bourgain–Gamburd–Sarnak's affine sieve produces almost-primes in orbits once expansion is known. Ask whether every p has a (★) certificate with u, B (or 4uC − 1, 4BC − 1) prime or with ≤ r prime factors; if true numerically, sieve methods on the word set apply and the strengthened statement has more structure.",
  "Strengthenings with prime parameters connect ES to the affine-sieve toolkit and to Chen-type almost-prime results.",
  "For p ≤ 10⁸ compute the least r such that a certificate with Ω(4uC − 1) ≤ r and Ω(4BC − 1) ≤ r exists; find primes needing large r.",
  ["affine-sieve", "almost-primes", "strengthening"], "med", "cheap", seen=["BRAINSTORM/thin_group_orbits.md"])
I("ELKIES", "Supersingular points and maximal orders: ≈ p/12 objects attached to every p",
  "Every prime p has ≈ p/12 supersingular j-invariants, in bijection (Deuring) with maximal-order types of the quaternion algebra ramified at p and ∞. These always exist, like Elkies's CM values; map them (or their small-norm elements, Eichler orientations) to ES certificate data.",
  "Supplies power-many canonical objects for every p; if any natural map lands in certificates with positive probability, existence follows from their number.",
  "Read the repo's supersingular/Eichler memos; for small p compute the maximal orders' reduced norms forms and test whether ES certificates appear as small vectors.",
  ["supersingular", "quaternion-orders", "canonical-objects"], "med", "medium", kw=["supersingular"])
I("SATO", "ES over imaginary quadratic rings (ℤ[i], ℤ[ω]): does unit freedom make it easy?",
  "Potential-automorphy-style arguments work over extensions first. For ES over O_K (K imaginary quadratic), 4/π = 1/ξ + 1/η + 1/ζ with ξ, η, ζ ∈ O_K and no positivity (no real place): the extra units and the lack of positivity might allow identity-based proofs for every prime π. Determine what makes ℤ-ES hard (positivity at the real place? the square classes?) by seeing which ring versions are easy.",
  "Isolating the role of the archimedean positivity constraint tells whether the difficulty is archimedean or arithmetic.",
  "Search the literature ('Erdős–Straus number field', 'Gaussian integers Egyptian fractions'); experimentally find identities for 4/π over ℤ[i] covering all Gaussian primes up to norm 10⁶.",
  ["number-fields", "positivity", "archimedean"], "med", "cheap")
I("ZAREMBA", "Large deviations of Euclid's algorithm at a fixed denominator (Hensley, Baladi–Vallée)",
  "The CF length of a/p, a mod p, is asymptotically Gaussian with mean ≍ log p (Heilbronn, Hensley, Baladi–Vallée via transfer operators, with power-saving errors for fixed denominators). ES₅ (λ(p) ≤ 3) asks for an extreme left-tail event (length 3, prescribed shape). Large-deviation estimates for fixed p from the dynamical analysis of Euclid's algorithm would give lower bounds in exactly this quantifier order.",
  "The dynamical analysis of Euclid's algorithm is 'every p' by construction (it averages over a, not p); the question is how far into the tail its estimates reach.",
  "Read Baladi–Vallée ('Euclidean algorithms are Gaussian', J. Number Theory 2005; check) for fixed-denominator large-deviation statements and the error terms; compare the reachable tail with length-3 events (count ≍ log²p out of p).",
  ["transfer-operators", "large-deviations", "ES5"], "med", "medium", seen=["BRAINSTORM/farey_ford_cf.md"], kw=["Hensley"])
I("GSMARKOFF", "Why do Markoff-type surfaces have infinitely many integral Hasse failures, and does ES escape the mechanism?",
  "Ghosh–Sarnak: the integral Hasse principle for x² + y² + z² − xyz = k holds for almost all k but fails for infinitely many, via reduction theory of the Vieta-group action (all orbit representatives in a fundamental set excluded by congruences). ES shares the (log)²-scale counts and BM picture (FRONTIER §2.4 caution) but has no group action. Pin down whether 'no group action' removes the failure mechanism or merely hides it.",
  "The closest precedent for an almost-all statement that is false for infinitely many cases; understanding why ES differs is mandatory hygiene.",
  "Read Ghosh–Sarnak §§4–6 and extract the failure construction; try to replicate it for ES with a 'reduction theory' given by the smallest denominator x ∈ (p/4, 3p/4) or by minimal certificate parameters.",
  ["failed-upgrade", "integral-hasse", "disproof-hygiene"], "high", "medium", kw=["Ghosh"])
I("GSMARKOFF", "Reduction theory for ES solutions and congruence exclusion of all reduced representatives",
  "In Ghosh–Sarnak failures every orbit has a reduced representative in a bounded region, and congruence conditions can exclude all of them. ES: every solution has x ∈ (p/4, 3p/4] (x minimal); the 'reduced representatives' are the pairs (x, m = 4x − p). Ask whether congruence conditions modulo a fixed M can exclude all reduced representatives for infinitely many p (that would be a non-BM obstruction).",
  "A concrete search space for genuinely new obstructions; if impossible for structural reasons, that fact is itself a (small) theorem.",
  "For M = 840·k, compute which residues of p mod M admit a reduced representative whose two-term remainder is locally solvable mod M; check that no non-square class is fully excluded.",
  ["reduction-theory", "congruence-obstructions", "disproof-hygiene"], "high", "cheap")
I("FFGOLD", "Search for F_q[T] counterexamples to the direct ES analogue at small q",
  "Function-field analogues sometimes fail at small q (as Artin's C₂ fails for small p). If the direct analogue of ES over F_q[T] (with a suitable positivity replacement, e.g. degree constraints) fails for some small q, the failure mechanism is an explicit structure that ℤ-ES must avoid; if it holds for all tested q, the F_q[T] proof (repo) is the template.",
  "Cheap exhaustive computation with high information value (8/131-type test in the function-field world).",
  "For q = 2, 3, 4, 5 and irreducible P of degree ≤ 12, search solutions of 4/P = 1/X + 1/Y + 1/Z (with the repo's degree conventions) and list failures.",
  ["function-fields", "counterexample-search", "small-q"], "high", "cheap", kw=["F_q[T]"])
I("APOLLO", "Positive proportion before density one (Bourgain–Fuchs) for bounded-shape certificates",
  "Bourgain–Fuchs proved a positive proportion of integers are Apollonian curvatures before density one. For ES, bounded-shape certificate families (u, B ≤ U fixed) cover a positive proportion of primes by Dirichlet; quantify the proportion covered by shapes with u, B ≤ U as U grows, versus the full ES density one.",
  "Measures how much of ES is 'explained' by bounded shapes (Mordell-type) vs growing ones — the shape-growth rate needed for density one.",
  "Compute coverage of primes ≤ 10⁹ by (★) with u, B ≤ U for U = 1..100.",
  ["bounded-shapes", "coverage", "numerics"], "high", "cheap", seen=["POINTWISE_SIZE.md"])
I("MSS", "Lee–Yang / stability-preserver view of the window generating polynomial",
  "Lee–Yang (zeros on the unit circle for every ferromagnetic Ising model) and Borcea–Brändén stability preservers prove non-vanishing for every instance via polynomial stability. The window certificate count is a coefficient of Π_i (Σ_{|j|≤a_i} x^{j·g_i}) in the group ring; ask whether a multivariate stable polynomial encodes certificate existence so that stability forces a nonzero coefficient.",
  "Stability/interlacing proved 'every instance' theorems where probabilistic arguments only gave typical instances.",
  "Write the multivariate polynomial Π_i (1 + z_i + z_i^{-1}) with z_i ↦ characters; examine real-stability of natural specialisations for small examples.",
  ["stable-polynomials", "lee-yang", "odd"], "low", "medium", seen=["BRAINSTORM/z45_interlacing_stable.md"])
I("HQUE", "Third-method insurance: find a family whose success is uncorrelated with both (★) and b=1",
  "Holowinsky–Soundararajan needed exactly two complementary methods. ES data show (★) ∪ b=1 never fail together ≤ 10⁸, but a proof-grade argument may need a third family whose success correlates with neither (e.g. ES₅, Type I lines, small windows). Measure correlations of success indicators among 6–8 families.",
  "Identifies the minimal robust family set for a complementary-methods proof.",
  "Compute the correlation matrix of family success indicators (and of their counts) over primes ≤ 10⁸ in Mordell-hard classes.",
  ["complementary-methods", "correlation", "numerics"], "high", "cheap")
I("DUKE", "Mordell's class-number formula for yz + zx + xy = p as an exact power-size count",
  "Duke/Iwaniec exploit class-number-sized representation counts. Mordell (1923) gives, for prime n, the number of positive solutions of yz + zx + xy = n as 3G(n) − 3 (G class-number type). ES solutions satisfy σ₂(x,y,z) = 4σ₃/p; scaling Type II solutions (y = pY, z = pZ) gives p·YZ = x(4YZ − Y − Z), a σ₂-type relation. Look for a bijection or injection from a subset of Mordell's solutions (power-many) to ES certificates.",
  "Would tie ES to an exact class-number count (power-size, every p), the Duke template.",
  "For small primes, list Mordell's solutions of yz + zx + xy = p (or = 4p, kp) and test which ones transform into ES solutions via simple rational maps.",
  ["class-numbers", "exact-counts", "symmetric-functions"], "med", "cheap")
I("SNIRBOUND", "Which almost-all ES results are sharp in the Kolmogorov sense?",
  "Kolmogorov's divergent Fourier series shows some a.e. theorems are optimal. For each ES-type almost-all theorem (single levels, (★), b=1, ES₅), decide whether infinitely many failures are known/expected (then the almost-all result is 'sharp') or not; only the latter are candidates for every-p upgrades.",
  "Avoids attempting upgrades of statements that are actually false infinitely often (like single-level or (★)-only versions may be).",
  "For each sub-route, estimate Σ_p P(fail) under the calibrated model; classify as 'expected finitely many' vs 'expected infinitely many' failures.",
  ["sharpness", "sub-routes", "heuristics"], "high", "cheap")
I("SKSO", "Average over p of Schinzel-type events for the polynomials 4Cp + 1 in C",
  "Skorobogatov–Sofos average over polynomial families. At fixed p, the family {4Cp + 1 : C} is a linear polynomial in C; averaging over p (with C free) gives Schinzel-on-average-type statements on factorisations of 4Cp + 1 that underlie the almost-all ES theorem. Make explicit which 'Schinzel on average' input the almost-all proof uses and whether a pointwise-in-p version is a known open problem.",
  "Locates ES exactly within the Schinzel-on-average landscape (what is averaged, over what).",
  "Rewrite Vaughan's almost-all proof as a statement about factorisations of 4Cp + 1 averaged over p; identify the pointwise analogue.",
  ["schinzel", "averaging", "locating-the-gap"], "med", "cheap")
I("WEIL", "Twists by characters mod 4C as 'twisted point counts' with an exactly known total",
  "Weil-type lower bounds use that twisted counts sum to an exact total. At level C, Σ_{χ mod 4C} χ(−1)·#{d | N : χ(d)…} expansions give D_C^−(N) = (1/φ(4C)) Σ_χ χ̄(−1) σ_χ(N) exactly; the trivial character gives τ(N)/φ(4C), others are twisted divisor sums. A lower bound needs |Σ_{χ ≠ 1} …| < τ(N): bound the twisted divisor sums σ_χ(N) pointwise (multiplicative, |σ_χ(q^a)| ≤ a + 1).",
  "Pointwise bounds on σ_χ(N) are trivial-to-moderate; the issue is how many characters and how cancellation among them behaves for structured N = 4Cp + 1.",
  "For hard p and small C, compute |Σ_{χ ≠ 1} χ̄(−1)σ_χ(N)| vs τ(N) and record how close it gets.",
  ["twists", "character-expansion", "level-counts"], "high", "cheap")
I("RAMTERN", "Kaplansky-type ternary forms with conditional (GRH) complete lists as structural analogues",
  "Beyond Ramanujan's form, several ternary forms have GRH-conditional complete lists of exceptions (Ono–Soundararajan type). Their exception lists are finite but sporadic; ES-adjacent statements with sporadic exceptions (U(n) list, b=1 failures) might be 'ternary-form-like'. Test whether the U(n)/b=1 exceptions are represented/non-represented by specific ternary forms.",
  "A direct dictionary between sporadic ES-adjacent exceptions and ternary-form exceptions would import Waldspurger/GRH technology.",
  "For the known sporadic exception lists, test representability by all reduced positive ternary forms of discriminant ≤ 500.",
  ["ternary-forms", "sporadic-exceptions", "dictionary"], "low", "cheap")
I("CHEN", "Switching between the two cofactors of 4Cp + 1 and the two ES types",
  "Chen's switching replaces a hard count by a dual count where the roles of variables swap. In (★), 4Cp + 1 = (4uC − 1)(4BC − 1) is symmetric; the b=1 line uses p + 4d with a divisor ≡ −1 (mod 4d). Find an explicit bijection/switch between near-certificates of one line and of the other, so that an upper bound for near-misses of one yields a lower bound for hits of the other.",
  "Switching is the concrete mechanism behind complementary-route arguments.",
  "Search for maps (u, B, C) ↦ (d, w) between (★) data and b=1 data for the same p, and test on hard primes.",
  ["switching", "sub-routes", "bijections"], "med", "cheap", seen=["B1_LINE.md"])
I("LINNIK", "Zero-free region analogue: a range of levels where no 'conspiracy' is possible",
  "Linnik's theorem uses a zero-free region near s = 1 for all characters of modulus ≤ Q. For ES, find a range of small levels (C ≤ C₀(p)) where the relevant characters (mod 4C) are so few that a full conspiracy against certificates would force p into explicit square-like residue classes (contradiction for non-squares).",
  "Small levels have few characters; a 'no conspiracy at small levels' lemma would be the ES zero-free region.",
  "For C ≤ 30, characterise the residues of p (mod lcm(4C)) for which all these levels fail; compute the density of such residues and whether they are squares.",
  ["small-levels", "conspiracy", "residue-classes"], "high", "cheap")
I("THUE", "Box principle for windows: two windows with the same residue data combine",
  "Thue's lemma is a box principle. Pigeonhole windows e by the residue vector of p modulo small primes and the factorisation shape of N_e; two windows with equal data might combine (via CRT) into a certificate at the window e·e′ or at lcm, if a combination law exists.",
  "Pigeonhole needs a combination law; windows have CRT structure that may supply one.",
  "Test on data: for pairs of failing windows e, e′ with compatible data, check whether e·e′ (or another derived window) succeeds more often than random.",
  ["pigeonhole", "windows", "CRT"], "low", "cheap")
I("RADEM", "Exact formulas for divisor-class counts: Ramanujan sums expansion of D_C^−(N)",
  "Rademacher-type exact expansions use Kloosterman/Ramanujan sums. The class-restricted divisor count D^−_{4C}(N) has an exact finite Fourier expansion over additive characters mod 4C (Ramanujan sums c_q(·)); for the all-level sum this becomes a series Σ_q c_q-type terms, an ES 'singular series' with exact tail.",
  "An exact Ramanujan-sum expansion of R(p) separates the main (BM) part from the rest explicitly and may be summable in closed form at small q.",
  "Write R(p) = Σ_q A_q(p) with A_q built from Ramanujan sums; compute A_q(p) numerically for q ≤ 100 and the remainder.",
  ["exact-formula", "ramanujan-sums", "singular-series"], "med", "cheap")
I("SHAF", "Grunwald–Wang-type exceptions: when local prescriptions at 2 cannot be realised globally",
  "Shafarevich's 2-group case had a gap related to the Grunwald–Wang special case (local conditions at 2 not realisable globally). ES certificate conditions involve 4C and 8ℤ − p (2-adic structure). Check whether ES sub-routes have Grunwald–Wang-type 2-adic exceptions: residue patterns at 2 that are locally fine but globally unrealisable for certain p.",
  "2-adic subtleties are exactly where 'local implies global' historically failed in a structured way.",
  "Analyse the 2-adic constraints in (★) and b=1 (C, d powers of 2, p mod 2^k) and test failures' residues mod 2^k.",
  ["2-adic", "grunwald-wang", "local-global"], "low", "cheap")
I("ORE", "Commutator-style 'every element' from character ratios: target −1 in (ℤ/e)* via products of few divisor classes",
  "Ore-type results show every element is a product of few commutators using character bounds. Analogue for windows: when the prime-factor classes of N_e generate a large subgroup H ∋ −1, show −1 is a product of a bounded number of them (with ±1 exponents) using additive-combinatorics in abelian groups (Cauchy–Davenport/Kneser iterated), i.e. a bound on the 'diameter' of H w.r.t. the generating multiset.",
  "Reduces window certificates to a diameter bound in a Cayley graph of an abelian group — fully finite and checkable.",
  "Compute the ±1-diameter of (ℤ/e)* w.r.t. the multiset of prime-factor classes of N_e for hard (p, e), versus ω(N_e).",
  ["cayley-graphs", "diameter", "windows"], "med", "cheap")
I("GRAHAM77", "Finite base + closure: what finite verification would an ES closure theorem need?",
  "Graham's 77-theorem needed a finite check (78–333) plus closure maps. If any closure/transfer system for ES certificates were found (see closure items), compute the minimal 'base' of verified instances it needs; ES is verified to 10¹⁸, so any closure system with base ≤ 10¹⁸ would finish.",
  "Turns closure-map searches into a concrete success criterion.",
  "For each candidate closure map found by search, compute the set of primes it reaches from primes ≤ 10⁶ and check whether its complement thins out.",
  ["closure-operations", "verification", "criteria"], "low", "cheap")
I("COLLATZ", "Syracuse-type random variable for ES: the 2-adic/3-adic structure of minimal certificates",
  "Tao's Collatz proof analysed the distribution of a 3-adic 'Syracuse random variable'. ES certificates carry 2-adic data (4 | t; 8ℤ − p branch) and 3-adic data (Mordell classes mod 3). Define the analogous random variable (residues of minimal certificate parameters mod 2^k, 3^k) and study its distribution and mixing as p varies.",
  "Fine-scale mixing of certificate residues is the kind of statement that powers almost-all → 'almost every scale' improvements.",
  "Compute the distribution of minimal certificate parameters mod 2^k·3^j over primes ≤ 10⁸ and test for Fourier decay.",
  ["p-adic-distribution", "mixing", "numerics"], "low", "cheap")
I("SML", "Linear recurrences for minimal certificates along exponential families",
  "SML-type structure suggests that along n_s = a·b^s + c the minimal certificate parameters may follow linear recurrences in s on residue classes of s. Detect such recurrences for the proved families (3·2^s + 1, 63·2^s + 1) and use them to predict certificates for open families.",
  "Recurrences would give explicit every-s constructions (as Niederreiter for Zaremba).",
  "Run Berlekamp–Massey on sequences of minimal (u, B, C) along proved families restricted to s in fixed classes.",
  ["recurrences", "exponential-families", "data-mining"], "med", "cheap")
I("FOURCOL", "Reducibility check automation: verify 'configuration ⇒ certificate' lemmas by computer",
  "The four-colour proof verified each configuration's reducibility by computer. For ES, configuration lemmas of the form 'if p ≡ r (mod M) and 4Cp + 1 has factorisation pattern π then a certificate exists' can be verified symbolically for each (r, π); automate generation and checking of such lemmas.",
  "Builds a library of machine-checked partial results that any case-analysis proof would need.",
  "Implement a checker that, given (M, r, C, pattern), decides via CRT whether a certificate is forced; run over small M and patterns.",
  ["automation", "case-analysis", "verification"], "med", "medium", seen=["POINTWISE_SIZE.md"])
I("KAKEYA3", "Stickiness analogue: certificates at nearby levels share prime factors",
  "Wang–Zahl handled 'sticky' Kakeya sets where tubes cluster coherently across scales. For fixed p, near-certificates at levels C and C + kq share the prime q (CRT); study whether certificate data are 'sticky' across levels (coherent families sharing primes) and whether non-sticky configurations are easier to force.",
  "A structural dichotomy (sticky vs non-sticky) that may split the problem into two tractable halves.",
  "Measure, for fixed p, the clustering of certificate-bearing levels modulo primes dividing their divisors.",
  ["multiscale", "stickiness", "odd"], "low", "cheap")
I("SENDOV", "Limit objects of normalised divisor-class data as p → ∞ (Sendov's limiting measures)",
  "Tao's Sendov proof studies limiting zero distributions. For ES, attach to p the empirical measure of (log d / log N, class of d mod 4C) over levels C ≤ K and divisors d of 4Cp + 1; study its limit as p → ∞ (should be a product of uniform measures) and the rate; a counterexample sequence would converge to a measure avoiding a fixed 'certificate region'.",
  "Gives a concrete limit object for compactness arguments.",
  "Compute these empirical measures for p ~ 10⁶, 10⁸, 10¹⁰ and measure distance to the product-uniform model.",
  ["limit-measures", "compactness", "numerics"], "med", "cheap")
