# Items batch 4: combinatorics, Egyptian fractions, CS, misc upgrades.

I("SENDOV", "Compactness/ultraproduct: a nonstandard ES-failing prime",
  "Tao's Sendov proof takes a sequence of counterexamples with degree → ∞ and analyses a limit object. ES: an ultraproduct of hypothetical failing primes p_k → ∞ is a nonstandard prime p* with no internal certificate; internal theorems (Thm 2.2: M_BM(p*) ≥ c log²p*) hold by Łoś. Seek a contradiction in the nonstandard model (e.g. via a Loeb-measure equidistribution statement).",
  "Compactness turns 'all large p' into 'one nonstandard p', making limit-object arguments available.",
  "Write down which standard theorems about p transfer (counts, character sums) and which 'external' statements (limits of normalised counts) could be proved by Loeb-measure arguments.",
  ["compactness", "nonstandard-analysis", "limit-objects"], "med", "medium", kw=["ultraproduct"])
I("SENDOV", "Large-p regime split by arithmetic configuration",
  "Tao handled different limiting zero configurations by different arguments. Split large p by configuration: (i) ℓ(p) small, (ii) ℓ(p) large but some small window works, (iii) (·/p) mimics a fixed character on all primes ≤ (log p)^A, … and design one certificate family per regime.",
  "Each regime has extra structure to exploit; only finitely many regimes are needed if the split is by bounded data plus one 'pretentious' case.",
  "Define the regime map on primes ≤ 10⁹ and check which certificate family is most robust in each regime.",
  ["regime-split", "pretentiousness", "numerics"], "med", "cheap", kw=["pretentious"])
I("EDP", "Fourier reduction of an ES obstruction to a multiplicative (character) obstruction",
  "Tao reduced EDP to completely multiplicative functions by Fourier analysis. ES failure at window e means no divisor ratio ≡ −1 (mod e); reduce this to the existence of a character (or approximate homomorphism) χ mod e with χ(−1) = −1 that is 'large' on the prime factors of N_e.",
  "If every obstruction is character-like, the problem becomes one about Legendre/higher-order characters at p — the BM/genus language where tools exist.",
  "Prove the reduction for prime e: if the ±1-subset products of {g_i} miss −1, is there a character χ with χ(−1) = −1 and Σ_i Re χ(g_i) large? Test on data.",
  ["fourier-reduction", "characters", "obstruction-structure"], "med", "medium")
I("EDP", "Entropy decrement across levels",
  "Tao's entropy decrement shows that for most scales, local statistics at scale H·ℓ are close to those at scale H given residues mod ℓ. ES at fixed p: look for an entropy-decrement statement across levels C (or windows e) that makes certificate events at most levels behave like independent coin flips.",
  "Entropy decrement is a pigeonhole-on-scales device that works with a single sequence, matching ES's fixed-p setting better than probabilistic averaging over p.",
  "Compute the empirical entropy of the joint pattern (D_C(p) > 0)_{C ∈ [K, 2K]} for fixed p across dyadic K and check whether it saturates the independent-model entropy.",
  ["entropy-decrement", "levels", "independence"], "low", "medium")
I("EDP", "SAT search for the smallest profinite obstruction to bounded certificate menus",
  "Konev–Lisitsa used SAT for EDP's C=2. Encode 'no certificate with parameters ≤ K' as residue constraints on p modulo M and use SAT/ILP to find all residue classes mod M consistent with failure; verify that they are exactly squares (B1) and find the minimal K for each M.",
  "Cheap automated confirmation of the B1 picture and a generator of hard test cases.",
  "Encode for M = 840·q (q ≤ 50 prime) and K ≤ 200; compare SAT solutions with the square classes.",
  ["SAT", "computation", "B1"], "high", "cheap", seen=["POINTWISE_SIZE.md"])
I("SENS", "Divisors of squarefree N as a hypercube; certificates as edges of a signed structure",
  "Huang: any induced subgraph of Q_k on > 2^{k−1} vertices has a vertex of degree ≥ √k, via a signed adjacency matrix with A² = kI. Divisors of squarefree N with k prime factors form Q_k; a window/level certificate is a pair of disjoint subsets with product ratio ≡ −1. Look for a signed matrix whose spectral bound forces such a pair once a large subset of divisors lies in one class.",
  "Spectral interlacing is a pigeonhole with algebraic leverage; ES needs exactly a pigeonhole on divisor classes.",
  "Model: vertices = subsets S, label g(S) = Π_{i∈S} q_i mod e; find the maximal size of a set of subsets with no two labels in ratio −1, compare with 2^{k−1}.",
  ["spectral", "hypercube", "pigeonhole"], "low", "medium")
I("KAKEYA3", "Multiscale induction on level sizes",
  "Wang–Zahl proved 3D Kakeya by multiscale induction (sticky structure). ES certificates live at scales (C, u, B) with uBC ≈ p/4; formulate a statement S(X): 'every p has a certificate with C ≤ X or a structural reason to have one at scale X²' and attempt an induction on scales.",
  "Scale induction is how several every-type geometric statements were proved recently; ES has a natural scale hierarchy.",
  "From data, record for each p the smallest C with a certificate and the 'near miss' structure at smaller C; look for a recursive pattern across dyadic scales.",
  ["multiscale", "induction", "levels"], "low", "medium")
I("CAPSET", "Slice-rank bounds for certificate-avoiding exponent sets",
  "Croot–Lev–Pach/Ellenberg–Gijswijt bound sets avoiding x + y + z = 0 via slice rank. ES failure constrains the exponent vectors (mod 2, or in the character group) of prime factors of N_e so that no ±1 combination hits the class of −1: a linear-avoidance condition in a 2-group quotient of (ℤ/e)*. Slice-rank-type bounds limit such sets.",
  "Gives quantitative 'avoidance is rare' statements in elementary abelian quotients of (ℤ/e)*.",
  "For e with (ℤ/e)*/squares ≅ F₂^r, formulate the avoidance condition on the F₂-vectors of prime factors and compute the maximal avoiding sets for small r.",
  ["polynomial-method", "slice-rank", "avoidance"], "low", "medium")
I("DAV", "±1-weighted zero-sum theory in (ℤ/e)*: when do many distinct factor classes force −1?",
  "Olson's group-ring proof computes D(G). ES window certificate: Π q_i^{ε_i} ≡ −1 (mod e) with ε ∈ {−1,0,1} over prime factors q_i of N_e (with multiplicity). Reviewer repair: length alone does not force coverage (mod 7, the sequence 3,1,1,… generates everything but its signed subproducts are only {1,3,5}); zero-sum/covering theorems need many distinct (or well-spread) classes, so the right parameter is the number of distinct classes and their multiplicities.",
  "Zero-sum theory gives exact thresholds; ES then needs only 'enough prime factors' + 'the right subgroup', separating combinatorics from arithmetic.",
  "Compute, for (ℤ/e)* with e ≤ 200, the minimal number of distinct classes (with multiplicity data) guaranteeing that signed subproducts contain −1 when −1 ∈ ⟨classes⟩, and compare with typical ω(N_e) ≈ log log p.",
  ["zero-sum", "davenport-constant", "windows"], "med", "cheap", seen=["BRAINSTORM/s6_divisor_pigeonhole.md"], kw=["zero-sum"])
I("CAUDAV", "Kneser's theorem for the divisor-class product set at level C",
  "Cauchy–Davenport/Kneser lower-bound |A₁⋯A_k| in abelian groups, with equality only via stabiliser subgroups. The divisor classes of N = Π q_i^{a_i} mod 4C form the product set Π_i {1, q_i, …, q_i^{a_i}}; level C fails iff −1 is not in it. Kneser forces either a large product set or a subgroup structure.",
  "Splits failure into 'too few factors' and 'subgroup trap', each attackable separately.",
  "For hard primes and C ≤ 100 compute |product set|/φ(4C) and the Kneser stabiliser; classify failures.",
  ["kneser", "product-sets", "classification"], "high", "cheap", kw=["Kneser"])
I("CAUDAV", "Combinatorial Nullstellensatz on the trial form",
  "Alon's nullstellensatz proves existence of a nonvanishing point in a grid. R(p)/2 = #{d : 4c_d(p) | d + 1, d² ≤ 4c_d(p)p + 1}: encode 'no d in a grid of structured values works' as a polynomial vanishing on a product set, and look for a monomial whose coefficient is nonzero.",
  "A purely algebraic existence argument; most likely to work in a finite-field shadow (mod q) of the problem, giving at least a structural lemma.",
  "Formulate the mod-q shadow: for prime q, find (u, C) ∈ S₁ × S₂ (small sets) with 4uC − 1 ≡ 0 and p + u ≡ 0 (mod q); test the nullstellensatz coefficient condition.",
  ["polynomial-method", "nullstellensatz"], "low", "medium", kw=["Nullstellensatz"])
I("CHEVW", "Chevalley–Warning/Ax–Katz divisibility of auxiliary certificate counts",
  "Chevalley–Warning: few-degree systems have solution counts ≡ 0 mod p; with a trivial solution, a nontrivial one exists. ES local solvability is easy, but counts of certificates of p reduced modulo an auxiliary prime q (in a box) might satisfy Ax–Katz divisibility that, combined with a known trivial/degenerate solution, forces a genuine one.",
  "Divisibility-forces-existence is the exact mechanism of EGZ/Kemnitz and of Chen's Markoff result.",
  "Define for auxiliary prime q the F_q-system 'u·B·C·4 − u − B ≡ p, with box constraints encoded by polynomials'; check degrees vs number of variables for Chevalley–Warning applicability.",
  ["chevalley-warning", "divisibility", "existence"], "low", "medium", kw=["Chevalley"])
I("EGZ", "EGZ-style reduction: from 'composite' certificates to prime-level statements",
  "EGZ for n = ab follows from EGZ for a and b by iterated extraction. ES certificates at a level 4C = 4C₁C₂: is a certificate at level C obtainable from structure at levels C₁ and C₂ (e.g. a divisor ≡ −1 mod 4C₁ and one ≡ −1 mod 4C₂ combined via CRT)?",
  "If levels compose, it suffices to handle prime (power) levels, where character theory is simplest.",
  "For p ≤ 10⁶ test: when 4C₁p+1 and 4C₂p+1 have certificates, does 4C₁C₂p + 1 have one more often than chance?",
  ["composition", "levels", "numerics"], "low", "cheap")
I("KEMNITZ", "Reiher's double counting: subsequences of fixed length with prescribed sum",
  "Reiher combined Chevalley–Warning with counting of subsequences of each length. ES analogue: count divisors of N of each 'length' (number of prime factors) in each class mod 4C; parity/divisibility constraints between lengths might force the class −1 to be hit.",
  "Fine-grained counts by number of prime factors carry more structure than the total divisor-class set.",
  "For N = 4Cp+1 with ω(N) ≥ 4, compute the table (k, class) ↦ #{divisors with k prime factors in class}, and look for identities mod 2 or mod 3.",
  ["zero-sum", "double-counting", "odd"], "low", "cheap")
I("GOWERS", "Quasirandom 'one more factor' trick — size check for ES in SL₂(F_p)",
  "Nikolov–Pyber: if |A||B||C| > |G|³/m then ABC = G. For ES words A·T·A in SL₂(F_p), |A| ≈ |T| ≈ p while |G|³/m ≈ p⁸: the trick fails by a huge margin; quantify the deficit and check whether replacing SL₂(F_p) by a smaller quotient (Borel, affine group) helps.",
  "Records why the canonical almost→every group trick does not apply directly, and where a smaller ambient group might restore it.",
  "Compute |A|, |T|, |G| and m for G = SL₂(F_p), the Borel subgroup and the affine group F_p ⋊ F_p*; find the smallest ambient group in which ES becomes a product-covering statement.",
  ["quasirandom-groups", "product-covering", "size-check"], "high", "cheap")
I("GOWERS", "Almost-all + one more set ⇒ all: ES with a third free 'rescue' parameter",
  "In Gowers's trick, AB covers all but few elements and a third factor rescues the rest. ES: (★) covers all but a thin set of p (the 14 failures ≤ 10¹⁰); b=1 covers all but 3; their union none ≤ 10⁸. Formalise a 'rescue family' whose success set is large in a way that must intersect any thin exceptional set of the first family.",
  "Converts the empirical complementarity of routes into a cardinality argument (needs a lower bound on the rescue family's success set within every thin structured set).",
  "Characterise the (★)-exceptional set structurally (residue conditions, ℓ(p)) and compute the b=1 success rate restricted to primes with that structure.",
  ["rescue-family", "union-of-routes", "pigeonhole"], "med", "cheap", seen=["B1_LINE.md"])
I("ORE", "Move to a nonabelian encoding where character ratios decay",
  "Ore/Waring for finite simple groups works because |χ(g)/χ(1)| is small for large groups (quasirandomness). ES's character expansion lives in abelian groups (ℤ/4uB)* where all ratios are 1 — no decay. Find a nonabelian group encoding (SL₂(ℤ/q), Heisenberg, quaternion units mod q) where the certificate count expands over characters with small ratios.",
  "The abelian encoding may be the reason no pointwise cancellation is visible; nonabelian Fourier analysis has built-in square-root savings from representation dimensions.",
  "Express the SL₂-form certificate condition modulo q as a class-function count in SL₂(ℤ/q) and expand via Frobenius' formula; estimate the non-trivial character contribution.",
  ["nonabelian-fourier", "character-ratios", "encoding"], "low", "medium")
I("DESIGNS", "Nibble + absorber: random greedy first denominator, absorber for the two-term remainder",
  "Designs exist for all large admissible n via an approximate (nibble) decomposition plus a prepared absorber fixing leftovers. ES: choose x so that m = 4x − p is small and smooth (nibble-like), then 'absorb' via the two-term condition (m/(px) = 1/y + 1/z iff px has divisors a, b with a + b ≡ 0 mod m).",
  "Separates ES into a flexible step (many x) and a rigid step (two-term splitting); quantifies how often the absorber succeeds.",
  "For hard primes, enumerate x near p/4 with m ≤ M and measure the success rate of the two-term step as a function of the smoothness and divisor count of x.",
  ["absorption", "two-step", "egyptian-fractions"], "med", "cheap", kw=["absorber"])
I("DESIGNS", "Keevash template: algebraic identity families + random perturbation for square classes",
  "Keevash's randomized algebraic construction starts from an algebraic template and perturbs it. ES: Mordell identities cover all non-square classes mod 840 (algebraic template); perturb identity parameters randomly to handle the square classes, with an absorber for failures.",
  "Mordell–Schinzel forbids polynomial identities covering squares, but random perturbations of identities are not identities.",
  "Take Mordell's identities, introduce free integer parameters (k-fold families), and measure how often random parameter choices give certificates for primes in square classes.",
  ["randomized-algebraic", "identities", "square-classes"], "low", "medium")
I("WILSON", "Closure maps: certificate(p) ∧ certificate(q) ⇒ certificate(r) for some r(p,q)",
  "Wilson's PBD-closure and Graham's 2n+2/2n+9 maps produce 'every large n' from finitely many seeds. ES is closed under n → kn only; search for genuinely bilinear closure operations producing certificates for new primes r from certificates of p and q.",
  "Any nontrivial closure operation on certificate-carrying primes would be a completely new structural fact about ES.",
  "Brute-force search: for pairs of (★) triples (u₁,B₁,C₁), (u₂,B₂,C₂), test small bilinear/polynomial combinations for producing triples of other primes.",
  ["closure-operations", "search", "structure"], "low", "cheap")
I("EFL", "Extremal vs non-extremal split for ES",
  "EFL/Ringel proofs split into 'extremal' configurations (handled by hand) and 'random-like' ones (absorption). ES: random-like p (character values balanced) vs extremal p (QR at many small primes; square-like mod large M); handle extremal p by forced-congruence arguments (least non-residue) and random-like p by second-moment counting.",
  "Gives a concrete division of labour where each part may be tractable; the extremal side is close to the Burgess/least-non-residue world.",
  "Define an extremality score E(p) (e.g. number of primes ℓ ≤ 100 with (p/ℓ) = 1) and examine how certificate counts depend on it.",
  ["extremal-split", "regimes"], "med", "cheap")
I("FOURCOL", "Unavoidable configurations + discharging over levels",
  "Four colour theorem: every planar graph contains one of 633 reducible configurations (found by discharging). ES: define 'configurations' as local data (p mod small M, factorisation pattern of 4Cp+1 for C ≤ K); show by a discharging/averaging argument that every p contains one of a finite list, each of which forces a certificate.",
  "B1's Thm M says bounded procedures follow formal runs at square-mimicking points, so the configuration list must include unbounded data; still the method gives a framework for structured case analysis.",
  "Collect, for p ≤ 10⁸, the minimal 'certificate-forcing' local configurations and see whether a small set covers all p empirically.",
  ["discharging", "case-analysis", "B1"], "med", "medium", seen=["POINTWISE_SIZE.md"])
I("FOURCOL", "Minimal counterexample via the e-slice: ES(p) from data of N = (p+e)/4 < p",
  "Four-colour and many combinatorial proofs consider a minimal counterexample. ES(p) ⟸ a property P(N, e) of the smaller integer N = (p+e)/4. Find a property Q(n), inherited along n ↦ (n + e)/4 for some e, such that Q(n) for all n < p implies Q(p) and Q(p) ⇒ ES(p).",
  "A successful Q would make ES a consequence of verification (10¹⁸) + induction.",
  "Data mining: for each p ≤ 10⁷, list e for which N_e carries a certificate and look for a hereditary property of N_e.",
  ["induction", "minimal-counterexample", "e-slice"], "low", "cheap")
I("PARK", "Spread/expectation threshold of the ES certificate hypergraph",
  "Park–Pham: thresholds are within log of the (fractional) expectation threshold, via 'spread' families. Model ES at p as a random hypergraph where each potential certificate is present with its density; compute its spread and expectation threshold to see whether ES sits 'above threshold' by a log factor or just at it.",
  "The repo finds the expected number of 'hit' levels is ≈ (0.44 → 0.97)·log p (critical); a spread analysis would make 'critical vs supercritical' precise.",
  "Compute the fractional expectation threshold of the (★) certificate family for test p using LP over levels.",
  ["thresholds", "random-models", "criticality"], "low", "medium")
I("UNIONCL", "Entropy inequality for the union of certificate families",
  "Gilmer's entropy argument shows some element is frequent in a union-closed family. ES certificate families are 'union-like' (if a family works for p it works for multiples); an entropy inequality on the joint distribution of certificate indicators across families might force a frequently-successful family.",
  "Odd, but entropy methods recently produced constant-factor every-family results from nothing.",
  "Compute the empirical joint distribution of success indicators of 10 certificate families over primes ≤ 10⁷ and the entropy of their union.",
  ["entropy", "families", "odd"], "low", "cheap")
I("LLL", "Derandomised Janson: P(no certificate) ≤ exp(−μ + Δ/2) in a pseudorandom model",
  "Janson's inequality bounds the probability that no event occurs among weakly dependent monotone events. For fixed p, with μ = expected certificates ≍ log²p and Δ the pair-dependency sum, a derandomised Janson (pseudorandomness of p's residues) would give R(p) > 0 when μ − Δ/2 → ∞.",
  "Connects the campaign's Poisson zero-law heuristics to a precise inequality; the measured zero law (≈ 1.5–2.8 × swap-Poisson) says what Δ must be.",
  "Compute μ and Δ for the (★) events (indexed by (u,B,C)) at test p, and compare exp(−μ + Δ/2) with the observed zero probability at the same M.",
  ["janson", "dependency", "zero-law"], "high", "cheap", kw=["Janson"])
I("PFR", "Entropic Ruzsa distance between divisor-class distributions at different levels",
  "GGMT proved PFR via entropic Ruzsa distance and an entropy-decrement iteration. For fixed p, the distributions of divisor classes of 4Cp+1 across levels C could be compared via entropic distances; structured failure would force small distances to subgroup-uniform distributions.",
  "An odd but well-defined way to quantify 'subgroup trapping' of divisor classes across levels.",
  "Compute entropic distances of the divisor-class distributions to uniform-on-subgroup distributions for hard p.",
  ["entropy", "additive-combinatorics", "odd"], "low", "cheap")
I("CROOT", "Ramsey–ES: a monochromatic solution for every finite colouring (stronger statement)",
  "Croot proved every finite colouring has a monochromatic Egyptian representation of 1. Formulate Ramsey–ES: for every finite colouring of ℕ and every large prime p, is there a monochromatic (x,y,z) with 4/p = 1/x + 1/y + 1/z? If true, it implies ES and may be accessible to Croot-type density arguments (or be false, which is informative).",
  "Strengthenings sometimes have better proofs; falsification would show which colourings are 'ES-hard'.",
  "Test colourings by 2-adic valuation parity, by residue mod 3, and random 2-colourings for p ≤ 10⁴; look for primes with no monochromatic solution.",
  ["ramsey", "strengthening", "numerics"], "med", "cheap")
I("BLOOM", "Bloom/Liu–Sawhney machinery for few-term Egyptian representations with dense denominators",
  "Bloom: positive density sets contain S with Σ1/n = 1, via counting with main term + exponential sums on integers with structured anatomy. Ask what the machinery gives for k-term representations of 4/p (k fixed, small) with denominators restricted to structured sets (multiples of p with smooth cofactors).",
  "Bloom's framework is the modern Fourier-analytic engine for unit-fraction existence; checking where it breaks for k = 3 localises ES's difficulty.",
  "Read Bloom's §§2–4 and identify the minimal number of terms the method needs; check if it can handle 4/p = Σ_{i≤k} 1/n_i with k ~ 10 and n_i in a set of density zero.",
  ["fourier-analysis", "egyptian-fractions", "literature"], "med", "medium", kw=["Bloom"])
I("GRAHAM77", "Graham's 77-theorem mechanism for ES-like partition problems",
  "Graham: if n is representable then so are 2n+2 and 2n+9, plus a finite check (78–333). The mechanism is affine closure maps. ES is closed under n → kn but no affine map n → an + b preserves solvability in general (it would be a Mordell-type identity). Determine all affine maps that preserve Type II solvability on some residue class.",
  "Classifying affine closure maps tells exactly how far identity-based closure can go (Mordell–Schinzel-type limit).",
  "Search a, b ≤ 100 for which ES-solutions of n map to solutions of an + b on a residue class, via the Type II parametrisation.",
  ["closure-operations", "affine-maps", "identities"], "med", "cheap")
I("FIBSYL", "Look-ahead greedy: provably terminating 3-term splitting rules",
  "Fibonacci–Sylvester greedy terminates because the numerator decreases; the odd greedy algorithm is open. For 4/p, analyse non-greedy first-step rules (choose x among ⌈p/4⌉ + k for k ≤ K by a look-ahead criterion) and characterise primes where every rule with K ≤ K₀ fails.",
  "A finite-look-ahead rule is a bounded procedure (B1 says it must fail for some p under H), but the failure set's structure is informative and computable.",
  "For each p ≤ 10⁸ compute the least k such that x = ⌈p/4⌉ + k leaves a two-term-solvable remainder; record the distribution and the extreme p.",
  ["algorithms", "greedy", "numerics"], "high", "cheap")
I("BREUSCH", "Restricted-denominator ES: which congruence restrictions on x, y, z keep ES true?",
  "Breusch/Stewart: every rational with odd denominator is a sum of distinct odd unit fractions (many terms). For three terms, all-odd is impossible (parity: 4xyz = p(xy+yz+zx) forces an even denominator). Classify restrictions (x,y,z in prescribed classes mod m) that are consistent with ES for all small p, and test which ones look 'every p'.",
  "Restricted versions that hold numerically are stronger statements that may carry more structure for a proof (or reveal new obstructions).",
  "For m = 3, 4, 5, 8 and all class-restriction patterns, compute the failure set among p ≤ 10⁶.",
  ["restricted-denominators", "strengthening", "numerics"], "high", "cheap")
I("HOUGH", "ES as an infinite congruence 'covering' of the non-squares; distortion-method analysis",
  "Hough and Balister–Bollobás–Morris–Sahasrabudhe–Tiba bound the uncovered density of covering systems via a distorted-measure sieve. ES Type II (★): the classes p ≡ −(u+B) (mod 4uB) over all (u,B) must cover every prime; they never cover odd squares (T1). Study the uncovered set of the subsystem with moduli ≤ M within [1, X] as M grows.",
  "The distortion method controls the uncovered set precisely for systems with many moduli; ES's system is explicit and its uncovered set is known to contain squares.",
  "Compute the uncovered set of {−(u+B) mod 4uB : 4uB ≤ M} in [1, X] for M up to 10⁵, X up to 10⁸; compare its size with #squares + #(small sporadic) and track how fast non-squares disappear.",
  ["covering-systems", "distortion-method", "T1"], "high", "cheap", kw=["covering system"])
I("HOUGH", "Minimum-modulus-type statement: every certificate system covering a class must use a small modulus",
  "Hough: every distinct covering has a modulus ≤ 10¹⁶. ES analogue: for each Mordell-hard class r mod 840, any finite set of (★) congruences covering all primes in r ∩ [X, 2X] must include moduli of a certain size or divisibility (e.g. divisible by many small primes). Gives structural information on what certificates must look like.",
  "Constraints on the moduli of any covering are a form of 'forced structure' usable in a proof by contradiction.",
  "Empirically compute, for each hard class and dyadic X, the greedy minimum set of moduli covering all primes; record its smallest modulus and prime-divisibility profile.",
  ["covering-systems", "structure", "numerics"], "med", "cheap")
I("GOLDOTHER", "Left-tail extrapolation: does Σ_p P(R(p) = 0) converge?",
  "Goldbach's other conjecture failed at 5777/5993 where the expected representation count was small. For ES, extrapolate the measured zero law (P(R* = 0 | M)) to estimate Σ_p P(no certificate) over p > 10¹⁸; if it is ≪ 10⁻⁶, the 'heuristic' evidence for ES is overwhelming, and the computation identifies which sub-route is safest to target.",
  "Sanity-checks which formulations are heuristically true for all p (needed before trying to prove them).",
  "Fit log P(R* = 0 | M) on the repo's data and integrate against the distribution of M(p) for p > 10¹⁸; do the same for (★), b=1, union.",
  ["heuristics", "left-tail", "borel-cantelli"], "high", "cheap", seen=["BM_CORRECTED_COUNT.md"])
I("ONO", "Modular forms mod ℓ for the ES word series",
  "Ono used half-integral weight forms mod m and Serre's Hecke-nilpotence/Chebotarev results to get congruences for every prime modulus. Reduce the ES word series W(q) = Σ_{t,u,v≥2} q^{tuv−u−v} (or the level series of Thm K) mod 2 or 3 and look for congruences with eta/theta quotients that determine R(p) mod m from p's class.",
  "A modular congruence 'R(p) ≡ nonzero (mod m) on a class' is an every-p statement on that class.",
  "Compute W(q) mod 2, mod 3 to 10⁶ terms and test linear relations with products of θ(q^k), η(q^k) modulo 2/3.",
  ["modular-forms-mod-l", "congruences", "generating-functions"], "med", "medium", seen=["METAPLECTIC_ES.md"])
I("KNESER", "Topological existence: Tucker/Ky Fan on a complex built from divisor lattices",
  "Lovász proved Kneser via Borsuk–Ulam; Tucker's lemma is its combinatorial form. Build a simplicial complex from divisor configurations of 4Cp+1 across levels with a free ℤ/2-action (d ↔ N/d swap or u ↔ B swap) such that an equivariant labelling without a 'complementary edge' is impossible, and complementary edges are certificates.",
  "Topological methods give existence with no counting at all, immune to the polylog-main-term problem.",
  "Toy version: for one level C, model divisors as vertices of a cross-polytope (±q_i) and check whether certificate-freeness defines an antipodal-free labelling; compute its index.",
  ["topological-method", "borsuk-ulam", "existence"], "low", "big", seen=["BRAINSTORM/invol_topological.md"])
I("THOM", "Strengthen to induct: a stronger ES statement with an inductive parameter",
  "Thomassen proved 5-choosability by proving a much stronger precoloured statement that inducts. ES candidates: 'for every p and every prescribed residue r of x mod 8 (or of C mod 3), a certificate with that property exists' — check numerically which strengthenings hold, then look for an induction parameter (number of prime factors of 4Cp+1, size of e).",
  "Often the right strengthening is what makes induction possible; numerics cheaply filter candidates.",
  "Compute, for p ≤ 10⁶, which prescribed-property versions of (★)/ES hold for all p; keep the strongest surviving ones.",
  ["strengthening", "induction", "numerics"], "med", "cheap")
I("SUN135", "Representations with linear side conditions: ES certificates as constrained quaternion norms",
  "Machiavelo–Tsopanidis proved Sun's 1-3-5 conjecture (four squares with a linear condition) for every n. If ES certificates can be phrased as 'p (or 4Cp+1) is a norm from an order with a linear side condition on coordinates', their arithmetic arguments may transfer.",
  "Linear side conditions on norm representations are exactly the shape of ES congruence constraints.",
  "Read Machiavelo–Tsopanidis' method; try to phrase (★) as N(α) = 4Cp+1 with α in an order and a linear congruence on α's coordinates.",
  ["quaternions", "side-conditions", "norm-forms"], "low", "medium")
I("CFT", "Type I via binary forms: divisors of p² + 4c²d in classes mod 4cd",
  "Class field theory decides which primes are represented by which forms. Type I: f | p² + 4c²d with f ≡ −p (mod 4cd). Divisors of values of X² + 4dY² are constrained by genus/class-group characters of disc −16d; the condition f ≡ −p couples them to p. Compute exactly which classes mod 4cd are possible for divisors, and show −p is excluded exactly when p is a square (T1).",
  "Puts Type I in CFT language where every-p statements (Chebotarev, ring class fields) are standard.",
  "For small d, c enumerate possible classes of divisors of p² + 4c²d mod 4cd via genus characters, and compare with −p's class; verify the T1 exclusion at squares.",
  ["class-field-theory", "type-I", "genus-theory"], "med", "medium", kw=["genus character"])
I("CFT", "Bhargava-style composition on (★) triples (2×2×2 cubes)",
  "Bhargava's cubes give composition laws on binary forms. A (★) triple (u, B, C) with 4uBC − u − B = p might be the data of a 2×2×2 integer cube or a pair of binary forms whose composition carries ES structure.",
  "A composition law on certificates would be a new structural tool (descent, closure).",
  "Search for a cube A(u,B,C,p) with small entries whose Cayley hyperdeterminant or derived forms equal expressions like (4uC−1)(4BC−1) = 4Cp+1.",
  ["composition-laws", "bhargava-cubes", "odd"], "low", "medium")
I("FFGOLD", "Map the proved F_q[T] ES variants to their 'last ingredient'",
  "Function-field analogues (Goldbach over F_q[T], twin primes for large q) became every-degree theorems through RH for curves or étale cohomology. The repo notes ES over F_q[T] has proved variants; identify exactly which ingredient proved them (degree counting? Lang–Weil? an identity?) and its ℤ-analogue.",
  "If the F_q[T] proof uses only 'degree' arguments, its ℤ-analogue is a size argument; if it uses Weil, the analogue is a missing RH-type input.",
  "git grep -il 'F_q\\[T\\]' and read the relevant memos; extract the decisive step in each proof.",
  ["function-fields", "dictionary", "audit"], "high", "cheap", kw=["F_q[T]"])
I("FFGOLD", "Large-q limit for ES over F_q[T]: a Lang–Weil statement",
  "For fixed degree n and q → ∞, solutions of 4/P = 1/X + 1/Y + 1/Z with deg bounded are F_q-points of a variety; Lang–Weil/Deligne give counts ~ q^{dim}. Identify the variety and its geometric irreducibility; the ℤ-analogue of 'q large' is a heuristic for which structures make ES easy.",
  "Large-q results (Bary-Soroker, Sawin–Shusterman) are how hard ℤ-conjectures got function-field proofs; ES may already be easy there.",
  "Write the variety of degree-bounded solutions for deg P = n small and compute its irreducible components (Magma/Sage over F_q).",
  ["function-fields", "lang-weil", "large-q"], "med", "medium")
I("MR", "Matomäki–Radziwiłł-type short-interval averages of R(n): what is free and what is not",
  "MR show multiplicative functions behave in almost all short intervals of length h → ∞; every-interval statements need h ≥ x^θ. For ES: the average of R(n) over almost all intervals of length (log n)^A is ≈ M; the step to every interval mirrors the step to every n.",
  "Clarifies the ladder: every n ⇐ every short interval of length 1; quantify the shortest interval length for which an every-interval result can be proved.",
  "Combine the short-interval exceptional-set bound (D)30 with the primes-in-short-intervals literature to find the smallest H(x) such that every [x, x+H] contains a prime with a (★) certificate.",
  ["short-intervals", "ladder", "milestone"], "high", "cheap")
I("NEGPELL", "Rédei/Smith-style exact densities of level-failure profiles",
  "Koymans–Pagano proved Stevenhagen's density via Smith's method + reflection principles. The joint law of 'level C fails' events over p (governed by multiplicative structure of 4Cp+1 in (ℤ/4C)*) might be computable exactly by similar reflection/Rédei-symbol techniques, giving the true density of p failing (★) at all levels ≤ K.",
  "Exact densities would sharpen the zero-law heuristics and could expose genuine structure among failures.",
  "Compute empirical densities of failing-at-all-C ≤ K for K = 1..20 and compare with the independence model and with a Rédei-type model.",
  ["densities", "redei-symbols", "numerics"], "low", "medium")
I("SHAF", "Tower of moduli with auxiliary primes (Shafarevich-style embedding problems)",
  "Shafarevich realised solvable groups by solving embedding problems step by step, choosing auxiliary primes to control local behaviour. ES: build a certificate as a sequence of lifts through moduli 4 → 8 → 24 → 840 → … with auxiliary prime factors of 4Cp+1 chosen at each step, keeping a global integer solution possible at each stage.",
  "Gives a stepwise view of where integrality is lost; the final step (a genuine integer) is the crux.",
  "Trace actual (★) certificates for hard primes: at which modulus in the tower does the certificate's structure become determined?",
  ["embedding-problems", "towers", "odd"], "low", "medium")
I("HARDYZ", "Gradient ladder: infinitely many → positive proportion → 100% → every, for ES sub-statements",
  "Hardy→Selberg→Levinson→Conrey climbed the ladder for zeros on the line. For ES sub-routes (e.g. 'certificate with C ≤ (log p)^A', 'Type II with u = 1'), place each on the ladder (infinitely many / positive proportion / 100% / every) to find the highest rung reachable for a restricted family.",
  "Restricted families at '100%' rung are cheap wins; the transition points show which restriction kills 'every'.",
  "Tabulate known/expected rungs for 10 restricted sub-routes using repo results and quick numerics.",
  ["ladder", "restricted-families", "meta-strategy"], "high", "cheap")
I("AKS", "AKS-style 'too large and too small' group argument for a counterexample",
  "AKS: if n is not a prime power, a group of polynomials would be both ≥ a binomial lower bound and ≤ n^{√t}. ES: if p has no certificate, the set of divisor classes of 4Cp+1 across levels generates a structure (e.g. a subgroup of Π_C (ℤ/4C)* avoiding all −1's) that might be shown both large (many independent prime factors across C) and small (avoidance).",
  "The most striking conditional→unconditional derandomisation used exactly this double counting.",
  "Define G_K(p) = subgroup of Π_{C≤K} (ℤ/4C)* generated by the vectors (q mod 4C)_C over primes q > 4K dividing some 4Cp+1 (so q is a unit at every level); compute its index and whether it avoids the −1 pattern for hard p.",
  ["double-counting", "derandomization", "group-size"], "low", "medium")
I("AKS", "Miller → AKS: deterministic certificate search for every p, with a provable bound",
  "Miller's test needed ERH to bound the search; AKS removed the hypothesis by a different certificate. ES certificate searches are fast in practice; a provable polynomial-time (in log p) algorithm that always returns a certificate would prove ES. Even a conditional one (under GRH) would be a new result.",
  "Algorithmic formulations sometimes admit unconditional proofs via a cleverer certificate.",
  "State precisely what a GRH-conditional 'ES certificate in time (log p)^A' would need (BM_CORRECTED says GRH gives only M_gen ≥ log log p) and what kind of different certificate could avoid that.",
  ["algorithms", "certificates", "complexity"], "med", "cheap")
I("SPENCER", "Partial-colouring pigeonhole: collisions of near-certificates yield certificates",
  "Spencer/Beck: exponentially many colourings fall into few buckets, two collide, their difference is a good partial colouring. ES: generate many near-certificates for p (objects mapping to a small 'defect' space), pigeonhole two into the same bucket, and combine them (difference/quotient) into an exact certificate — the Pell/Dirichlet mechanism with an entropy count.",
  "The entropy count tells exactly how many near-certificates are needed versus the bucket count; if near-certificates are power-many while buckets are polylog-many, collisions are guaranteed.",
  "Identify a combination law (SL₂ quotients, divisor ratios) and a defect space; count near-certificates vs buckets for test p.",
  ["pigeonhole", "entropy", "combination-law"], "med", "medium")
I("MOLS", "Euler's false conjecture: an 'obstruction class' that turned out solvable",
  "Euler believed n ≡ 2 (mod 4) had no orthogonal Latin squares; only 2 and 6 fail. Mordell-hard square classes look like an obstruction class for identities, yet ES holds there numerically. BSP's recursive constructions crossed the class barrier — look for recursive (product) constructions for ES certificates that move from easy classes into square classes.",
  "Product/recursive constructions are exactly what identities (polynomial in p) cannot do; ES(n) ⇒ ES(kn) is a product construction but goes the wrong way.",
  "Search for constructions producing certificates for p from certificates for auxiliary integers in easy classes (e.g. via the e-slice N = (p+e)/4 structure).",
  ["recursive-construction", "square-classes", "history"], "low", "medium")
I("RINGEL", "Residue-class case split with per-class constructions (Ringel–Youngs) — and its limit",
  "Ringel–Youngs proved the Heawood bound by 12 residue cases, each with its own construction family. ES: Mordell's identities do this for non-square classes mod 840; the square classes need infinitely many sub-cases. Measure how the number of needed per-class families grows with the modulus (cf. B1).",
  "Quantifies the 'case explosion' and hence how far case-analysis approaches can go.",
  "For M = 840·k, count the minimal number of polynomial certificate families needed to cover all non-square classes mod M; plot vs M.",
  ["case-analysis", "identities", "growth-rate"], "high", "cheap", seen=["POINTWISE_SIZE.md"])
I("ERDCOV", "Covering-system obstructions: could a finite set of primes block all certificate families at once?",
  "Erdős showed infinitely many odd n are not p + 2^k because a covering system makes every candidate divisible by a small prime — invisible to density heuristics and not Brauer–Manin. ES has no BM obstruction (BL), but check whether ES certificate families admit a covering-type obstruction on some infinite set (all certificates forced to be non-integral by a finite set of primes).",
  "Disproof-side hygiene: covering obstructions are the classical way heuristically-true statements fail infinitely often.",
  "Argue structurally: ES certificate existence is not a 'primality of many shifts' condition, so covering obstructions should not apply; make this precise by checking that certificate conditions are open in the profinite topology for non-squares.",
  ["covering-obstruction", "disproof-hygiene", "brauer-manin"], "high", "cheap", seen=["BRAINSTORM/bsE_sierpinski_moving_integer.md"])
I("SML", "p-adic interpolation along exponential families (Skolem–Mahler–Lech)",
  "SML proves zero sets of linear recurrences are periodic + finite via p-adic analytic interpolation. ES along n_s = a·b^s + c: certificate conditions involve divisors of 4C·n_s + 1 = 4Ca·b^s + (4Cc + 1), an exponential sequence; p-adic interpolation of 'divisibility by a fixed d' gives periodic structure in s, possibly proving ES for open families like 15·2^s + 1 by periodic covering + finitely many checks.",
  "The repo already proved several exponential families via windows; SML-type periodicity could organise the remaining ones.",
  "For 15·2^s + 1 compute, for each small (C, d) with d ≡ −1 (mod 4C), the set of s with d | 4C·n_s + 1 (periodic in s); check whether a finite union of these covers all s.",
  ["p-adic", "exponential-families", "periodicity"], "high", "cheap", seen=["BRAINSTORM/bsE_padic_interpolation.md"])
I("VIAZ", "Dual certificates: an exact 'magic function' proving positivity of a weighted ES count",
  "Viazovska's proof found an exact auxiliary function (from modular forms) satisfying sign conditions — a dual certificate. ES: seek weights w on certificate shapes and an exact identity Σ w·(certificates of p) = (explicit positive function of p) + (manifestly nonnegative terms), with the identity coming from modular forms (Thm K level series).",
  "Positivity via an exact identity with sign conditions is a way to bypass error terms entirely.",
  "Using the Thm K series, search linear combinations of level series (with q-expansion coefficients) whose p-th coefficient is a nonnegative combination of R_t(p) plus a known positive term.",
  ["dual-certificates", "modular-forms", "positivity"], "low", "big")
I("VIAZ", "LP/Positivstellensatz duality: proof-complexity view of ES failure",
  "Cohn–Elkies LP bounds have dual certificates; for integer feasibility, Positivstellensatz/Nullstellensatz/cutting-plane proofs certify infeasibility. If ES failed at p, a refutation exists in a strong enough system; show that refutations of 'no certificate with parameters ≤ X' in some algebraic proof system have degree growing with X, while the certificate-search space is fixed.",
  "A proof-complexity lower bound for ES-refutations would be a new kind of evidence (and occasionally of proof).",
  "Encode 'no (★) certificate with u, B, C ≤ X' for a fixed true p as an infeasible polynomial system and compute Nullstellensatz degree for small X.",
  ["proof-complexity", "duality", "odd"], "low", "medium")
I("LITTLE", "Dimension-zero exceptional set as an intermediate target",
  "Einsiedler–Katok–Lindenstrauss showed Littlewood's exceptional set has Hausdorff dimension 0 via measure rigidity. ES analogue: E(N) ≪ N^ε (zero 'dimension') — strictly between the current N exp(−c(log N)^{3/4}) and finiteness.",
  "A measure-rigidity or entropy approach might reach 'dimension 0' even if CRT sieves stop at exponent 3/4 (EXCEPTIONAL_KARY3).",
  "Formulate the profinite/adelic dynamical system whose invariant measures would control ES exceptions and check whether an entropy argument bounds the counting dimension of the exceptional set.",
  ["exceptional-set", "measure-rigidity", "intermediate-target"], "low", "big", seen=["EXCEPTIONAL_KARY3.md"])
I("RADEM", "Rademacher-type exact series for the ES level/word series",
  "Rademacher turned the Hardy–Ramanujan asymptotic into an exact convergent series for every n, with an explicitly bounded tail; Bringmann–Manschot extended exact expansions to some meromorphic Jacobi forms. METAPLECTIC Thm K writes the level series as Kronecker theta quotients θ(X²)/θ(X)² (meromorphic Jacobi-form-like); an exact Rademacher-type expansion of their coefficients would give R_t(p) as main term + explicit tail.",
  "An exact formula with first term ≍ main term and an explicit tail is a pointwise-in-n statement by construction.",
  "Check the modular/Jacobi properties of θ(X²)/θ(X)² as a function of (τ, z) and whether Bringmann–Manschot's framework (or Appell–Lerch sum expansions) applies; compute the first few terms numerically.",
  ["exact-formula", "jacobi-forms", "rademacher"], "med", "big", kw=["Rademacher"])
I("RADEM", "Positivity from an exact divisor-sum formula: where the tail can be bounded",
  "For the partition function, positivity is trivial but Lehmer bounded the Rademacher tail explicitly. ES level counts are exact divisor-class sums (R_t(n) = D_t^−(tn+1) − β_t(n)); summing over t with weights, the 'tail' is the order-≥3 character part X(n). Ask for the explicit size of X(n) relative to M_BM in the exact formula at small levels.",
  "Even without analysis, the exact formula tells which levels dominate and how much the tail can at most remove.",
  "Compute M_BM(p) and X(p) separately for p ≤ 10⁷ and plot X(p)/M_BM(p); identify primes where it approaches −1.",
  ["exact-formula", "tail-bounds", "numerics"], "high", "cheap", seen=["BM_CORRECTED_COUNT.md"])
I("POINC", "Monotone-quantity flow on certificate space",
  "Perelman finished Poincaré with a flow and monotone entropy that forces termination at a canonical object. ES: define a deterministic 'flow' on candidate triples (x, y, z) for 4/p (e.g. a descent on the defect 4xyz − p(xy+yz+zx) using local moves) with a monovariant that can only stop at a certificate, and prove no other stopping states exist (or classify them).",
  "Odd but concrete: a local-move dynamical system on integer triples is easy to experiment with; classification of its sinks is a finite-ish problem per p.",
  "Design local moves (change one coordinate by ±1, or by divisor-jumps) decreasing |defect| and compute sinks for p ≤ 10⁴.",
  ["flows", "monovariant", "odd"], "low", "cheap")
