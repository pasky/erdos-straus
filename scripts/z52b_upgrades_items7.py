# Items batch 7: fourth pass — new catalogue entries and further variations.

I("HLSQ", "Power-size main terms are not enough: p + m² is open with a √n main term",
  "Hardy–Littlewood's conjecture that every large non-square n is p + m² has main term ≍ √n/log n, yet is open pointwise (binary). So 'lift ES to a count with a power-size main term' (TART items) is necessary but not sufficient: the lifted problem must also have enough free variables (ternary-or-more) for minor-arc control.",
  "Self-correction for the power-main-term items: specifies the extra requirement (dimension) any lift must meet.",
  "For each proposed lift V_p of ES, count the number of free variables after fixing p and compare with the Kloosterman/circle-method thresholds (≥ 4 for quadratic-type, more for cubic).",
  ["main-term-size", "binary-problem", "self-critique"], "high", "cheap")
I("HLSQ", "Two square degeneracies: algebraic factorisation (p + m²) vs reciprocity (ES Type I/II)",
  "p + m² degenerates at squares because n − m² = (a − m)(a + m) allows at most one representation (m = a − 1); T1 makes Type I/II fail at odd squares through a reciprocity cancellation. Compare: exceptional-set technology for p + m² is power-saving (H. Li 2003: E(X) ≪ X^0.982; verified), more advanced than ES's; can ES's T1 be rewritten as an algebraic factorisation in some model (e.g. 4Cm² + 1 or (p + e)/4 at squares)?",
  "If T1 becomes algebraic in some coordinates, Hardy–Littlewood-type machinery for 'non-square n' transfers more directly.",
  "At n = m², examine 4Cm² + 1 and (m² + e)/4 for algebraic factorisations that explain the absence of certificates (e.g. Sophie Germain-type identities).",
  ["T1", "square-obstruction", "factorisation"], "med", "cheap")
I("YOCCOZ", "Exact characterisation of sub-route success sets (Brjuno-type)",
  "Yoccoz showed the Brjuno condition is exactly the linearisable set, turning 'almost every' into 'iff'. For ES sub-routes, seek the exact arithmetic characterisation of the success set (e.g. Type I ∪ II succeeds iff n is not an odd square and n ∉ finite list; (★) succeeds iff …), including a mechanism producing the failures.",
  "An exact 'iff' is the strongest form of an every-type theorem and forces understanding of the failure mechanism.",
  "For (★) and b=1, fit the failure sets ≤ 10¹⁰/10¹¹ to candidate closed-form conditions and look for a constructive mechanism that produces the failures (as Yoccoz constructed non-linearisable examples).",
  ["exact-characterisation", "sub-routes", "failure-mechanism"], "med", "medium")
I("YOCCOZ", "Brjuno-type sum as a certificate-difficulty index",
  "The Brjuno sum Σ log q_{n+1}/q_n measures cumulative small-divisor difficulty. Define an analogous additive difficulty index for p (e.g. Σ over small levels C of −log of the probability that level C fails given p's residues) and test whether ES certificate counts are governed by it.",
  "A single scalar controlling difficulty would focus both proofs and adversarial searches.",
  "Compute the index for primes ≤ 10⁹ and correlate with R(p), least certificate C and sub-route failures.",
  ["difficulty-index", "numerics", "small-divisors"], "med", "cheap")
I("LEHMER", "Lehmer's τ(p) ≠ 0 as a structural twin of ES",
  "τ(p) ≠ 0 is open for every p although density-one non-vanishing is known and congruences (mod 691, 2^k, 3^k, 5, 7, 23) exclude vanishing on all but a thin set of residue classes. ES: Mordell identities exclude all but six classes mod 840; the remaining classes need size/structure input. Compare the two endgames.",
  "Two famous 'non-vanishing at every prime' problems with identical architecture (congruence exclusion + thin residual set) — methods for one may inspire the other.",
  "Write the comparison: what is known about the residual set for τ (e.g. τ(p) = 0 forces p in specific classes mod large M) vs ES's square classes; check whether ES has analogues of the mod-ℓ Galois-image arguments.",
  ["non-vanishing", "congruences", "stuck-mirror"], "high", "cheap")
I("LEHMER", "Congruence mod ℓ from a mod-ℓ Galois image: ES counts with large-image structure",
  "Swinnerton-Dyer's classification of exceptional primes for τ gives congruences τ(p) ≡ explicit function of p (mod ℓ). If ES counts (or a weighted combination of level series, Thm K) were coefficients of a form with a mod-ℓ Galois representation, congruences R(p) ≡ g(p) (mod ℓ) would follow, and ES would hold wherever g(p) ≢ 0.",
  "Turns ES non-vanishing into a congruence problem with explicit exceptions — the τ approach.",
  "Check whether the theta-quotient/Eisenstein parts of Thm K have coefficients satisfying Eisenstein-type congruences mod small ℓ (they are divisor sums twisted by characters, so congruences like σ_χ(N) ≡ … mod ℓ may exist).",
  ["galois-representations", "congruences", "modular-forms"], "med", "medium", seen=["METAPLECTIC_ES.md"])
I("ELKIES", "Jacobi-symbol parity forces a prime factor in a nonresidue class — how far toward the exact class?",
  "Elkies: (−D/H_D(j)) parity forces a prime factor inert in ℚ(√−D). ES windows: (N_e/e) = (p/e) for N_e = (p+e)/4, so if (p/e) = −1 then N_e has a prime factor q with (q/e) = −1 (FORCED_WINDOW's condition). ES needs more: a divisor ratio exactly ≡ −1. Identify what extra 'forcing' (higher-order characters, sign/size of N_e) could pin the class.",
  "Clarifies the gap between the proven quadratic forcing and the needed exact-class statement; Elkies needed only a quadratic class.",
  "For window primes e ≡ 3 (mod 4) with (p/e) = −1, measure the distribution of the forced nonresidue factors' classes and how often a complementary divisor completes −1.",
  ["jacobi-symbol", "parity-forcing", "windows"], "high", "cheap", seen=["FORCED_WINDOW.md"])
I("ELKIES", "Sign/size arguments on special values: choose auxiliary objects whose values have forced factors",
  "Elkies chose D so that H_D(j(E)) has a controlled sign and size. ES: choose auxiliary integers built from p (values of polynomials P(p) or norms from auxiliary fields) whose sign/size/Jacobi symbol forces a prime factor in a class tied to a level C, with the factor also dividing 4Cp + 1.",
  "A systematic search space for 'forcing' constructions that guarantee prime factors in classes.",
  "Search quadratic polynomials P with P(p) | (4Cp+1)·(something) for families of C and compute Jacobi-symbol constraints on their prime factors.",
  ["forcing", "special-values", "search"], "low", "medium")
I("CAUCHY", "Conjecture I3 as ES's cleanest 'universality' cousin of Cauchy/Waring",
  "Cauchy's polygonal theorem and Waring are universality statements. Conjecture I3 (FRONTIER §7: every n > 2 433 600 is tuv − u − v with t, u, v ≥ 3) is a sign-free, prime-free universality statement for a cubic polynomial; universality proofs for polynomials (Cauchy's lemma, Linnik's 7 cubes via ternary forms) are natural models.",
  "I3 drops ES's 4ℤ constraint on t; a proof technique for I3 is the right first test of any universality mechanism.",
  "Read EXSET_I3.md / I3_DEEP_ASTRA.md; then try a Cauchy-lemma-style reduction: for fixed t, tuv − u − v = n ⟺ (tu − 1)(tv − 1) = tn + 1 — ask which t make 'tn + 1 has a factorisation into two factors ≡ −1 (mod t), both ≥ 3t − 1' provable for all large n.",
  ["universality", "I3", "polygonal"], "high", "medium", seen=["I3_DEEP_ASTRA.md"])
I("FIFTEEN", "Universality classification for the family a·tuv − b·u − c·v + d",
  "Bhargava classified universal quadratic forms by finite criteria. For the cubic family F(t,u,v) = a·tuv − b·u − c·v + d with lower bounds on t, u, v, classify which members represent every large integer (I3 is the member a = b = c = 1, d = 0, bounds ≥ 3) and find the nearest universal member to ES's constrained form.",
  "Mapping the universality frontier in a family containing ES shows which constraint (4 | t, sign of d, bounds) is decisive.",
  "Compute exception sets up to 10⁸ for small (a, b, c, d) and bounds; record which appear finite.",
  ["universality", "classification", "numerics"], "med", "cheap", seen=["EXSET_I3.md"])
I("GTZ", "Uniformity obstruction for linear-forms-in-primes certificate schemes at fixed p",
  "For fixed p, every ES certificate has bounded size (denominators ≤ O(p²)), so any 'auxiliary primes' scheme needs prime tuples of linear forms in a box of size ≍ p whose coefficients depend on p. Green–Tao–Ziegler asymptotics are not uniform in coefficients comparable to the box, so they do not apply directly (correcting the BHS item).",
  "Records precisely why the conditional→unconditional (Harpaz–Skorobogatov–Wittenberg) move does not transfer to ES as stated, and what uniformity would be needed.",
  "State the needed uniform version: count of t ≤ T with L_i(t) all prime for forms with coefficients ≤ T^{1+ε}; compare with known uniform results (e.g. for a single form: Brun–Titchmarsh / Siegel–Walfisz ranges).",
  ["uniformity", "linear-forms-in-primes", "self-critique"], "high", "cheap")
I("SKSO", "Polynomial-in-m identities for n = m² + k (Schinzel's obstruction is in n, not in m)",
  "Mordell–Schinzel forbid identities polynomial in n covering square classes. For families n = m² + k (k ≠ 0) parametrised by m, identities X(m), Y(m), Z(m) with 4/(m² + k) = 1/X + 1/Y + 1/Z on congruence classes of m are not excluded by that theorem. Determine for which k such identities exist.",
  "Would give every-m theorems for quadratic families — a new kind of infinite family for ES beyond exponential ones.",
  "Search polynomial X, Y, Z of degree ≤ 4 in m for k = 1, 2, 3, 5, 7 (with congruence conditions on m), via undetermined coefficients.",
  ["identities", "quadratic-families", "mordell-schinzel"], "med", "cheap")
I("RAM", "Trivial vs needed pointwise bound for the non-genus part X(p)",
  "Ramanujan/Deligne improved the trivial (Hecke) bound to the sharp one. For ES, compute the trivial pointwise bound for |X(p)| (from the character expansion) and the bound needed (|X| < M_gen); quantify the gap in powers of log p.",
  "Measures how much 'Ramanujan-type' saving ES needs in the non-genus part.",
  "Bound |X(p)| ≤ Σ_q Σ_{χ mod q, ord ≥ 3} |stuff|/φ(q) trivially and evaluate numerically against M_gen for test p.",
  ["trivial-bounds", "gap-analysis", "non-genus"], "high", "cheap")
I("LLL", "Exact CRT independence in the level variable at fixed p",
  "LLL/Janson need limited dependence. At fixed p, the events {q | 4Cp + 1} for distinct primes q are exactly independent and uniform over complete periods of C (CRT); the only C-dependence that breaks independence is the class condition modulo 4C itself. Separate the two: write certificate events as (CRT-random divisibility pattern) × (C-dependent class test).",
  "Identifies a genuine source of exact independence at fixed p, which probabilistic arguments could exploit without averaging over p.",
  "Formalise for C in a range [K, 2K] with periods Q = Π_{q ≤ y} q: the divisibility pattern is equidistributed over C mod Q; compute the conditional certificate probability given the pattern and the size of C.",
  ["CRT", "independence", "fixed-p"], "high", "cheap")
I("GOLDOTHER", "The b=1 line as a 'Goldbach's other conjecture' model with sporadic failures",
  "The b=1 line fails at 193, 2521, 66529 and nowhere else ≤ 10¹¹ — like 5777 and 5993 for Goldbach's other conjecture. Fit the expected b=1 count at these primes and test whether failures are 'explained' by small expected counts; calibrate the same model on (★) (14 failures ≤ 10¹⁰).",
  "Validates the heuristic models on sub-routes with real failures before trusting them for ES.",
  "Compute the b=1 model main term at all p ≤ 10⁷ and the empirical P(fail | main term); check that the three failures sit at the extreme low end.",
  ["heuristics", "sporadic-failures", "calibration"], "high", "cheap", seen=["B1_LINE.md"])
I("HASSE", "Descent to universal torsors: more variables for the circle method",
  "Heath-Brown and others proved Manin-type results via universal torsors, which have more variables and simpler equations. ES's Type I/II parametrisations (Elsholtz–Tao) look like torsor coordinates; identify the universal torsor of the ES surface (BL computed its Brauer/Picard data) and count integral points on its twists with fixed p.",
  "More variables after descent is the standard route to circle-method feasibility; the torsor equations may be quadratic in many variables.",
  "From BL's description of Pic of the compactification of U_n, write torsor equations and compare with the ET parametrisation n = 4abcd − … ; count variables per equation.",
  ["universal-torsors", "descent", "circle-method"], "med", "medium", kw=["universal torsor"])
I("TWOSQ", "Elsholtz's windmill framework for sums of two squares and related problems",
  "Zagier's proof was generalised combinatorially (Elsholtz, 'A combinatorial approach to sums of two squares and related problems', Additive Number Theory: Festschrift for M. B. Nathanson, Springer 2010, 115–140; verified). Elsholtz is also an ES author (ET 2013); check whether the windmill framework was ever applied to ES-like equations.",
  "A direct bridge from the canonical parity proof to ES by an author who knows both problems.",
  "Read the paper; list the equations handled (x² + ky², etc.) and try its windmill construction on the (★) set or on {(u,B,C) : 4uBC − u − B = p}.",
  ["parity", "windmills", "literature"], "med", "cheap", seen=["WINDMILL.md"])
I("DIR", "Non-vanishing on the line Re s = 1 analogue: a level Dirichlet series that cannot vanish",
  "PNT/Dirichlet need L(1 + it, χ) ≠ 0 via the 3-4-1 positivity trick (Mertens). For fixed p consider F_p(s) = Σ_C D_C(p) C^{−s} (finite sum): ES ⟺ F_p ≢ 0. A '3-4-1'-type positivity combination of F_p, its twists, and F at related p might force non-vanishing.",
  "Odd, but 3-4-1 is the archetype of extracting non-vanishing from positivity of a trigonometric polynomial.",
  "Look for nonnegative trigonometric polynomials in a 'twist' variable (characters mod 4C) such that the combination of twisted level counts is ≥ c·(untwisted total) − (controlled).",
  ["positivity", "3-4-1", "odd"], "low", "medium")
I("BERT", "Chebyshev-type explicit bounds for the certificate-capable prime mass",
  "Chebyshev proved x/log x-type bounds for π(x) by explicit factorial inequalities. Define the 'certificate-capable prime mass' Θ_p(K) = Σ_{q certificate-capable at some C ≤ K} log q and try to prove Chebyshev-type explicit lower bounds for it at fixed p using only CRT structure of Π_C(4Cp + 1).",
  "Explicit elementary lower bounds are exactly what turns into 'every p ≥ p₀'.",
  "Compute Θ_p(K) numerically for hard p and K up to 10⁵; compare with the elementary upper/lower bounds derivable from Π_C (4Cp+1).",
  ["chebyshev", "explicit", "elementary"], "low", "cheap")
I("ARTIN", "Two-candidate version: (★) and b=1 as Heath-Brown's 'one of three' with two",
  "Heath-Brown's argument needs three candidates because two can both fail. ES data show (★) and b=1 never fail together ≤ 10⁸; test whether a third family (e.g. ES₅, small windows) is needed to make a proof-style argument robust, by finding primes where any two of three fail.",
  "Determines the minimal number of families an 'at least one works' argument must juggle.",
  "Compute joint failure sets of (★), b=1, ES₅ and the first-k windows up to 10⁹; report pairs/triples that fail together.",
  ["multiple-families", "joint-failures", "numerics"], "high", "cheap", seen=["B1_LINE.md"])
I("QUE", "Hecke operators on ES counts as functions of n: R(nℓ) vs R(n) for split/inert ℓ",
  "QUE uses Hecke operators T_ℓ acting on eigenfunctions. Define T_ℓ on functions of n by (T_ℓ f)(n) = f(nℓ) + (character)·f(n/ℓ) and test whether R (or f_II) is approximately an eigenfunction of some T_ℓ on Mordell-hard n, with eigenvalue depending on (n/ℓ).",
  "An approximate Hecke structure would give the multiplicative relations needed for Soundararajan-type arguments.",
  "Regress f_II(nℓ) on f_II(n) for n prime and ℓ ≤ 50, separately for (n/ℓ) = ±1.",
  ["hecke-operators", "multiplicativity", "numerics"], "med", "cheap")
I("SUBCONV", "Moments in the level aspect at fixed p: Σ_C |D_C(p) − E_C|² via spectral methods",
  "Subconvexity proofs bound moments of families by spectral decomposition. At fixed p, the family of levels C gives the moment Σ_{C ≤ X} |D_C(p) − E_C|²; express it via sums of Kloosterman sums (Kuznetsov) and bound it pointwise in p.",
  "A good level-aspect second moment at fixed p would show the deviations are small for most levels — then a positive proportion of levels with expected positive counts carry certificates.",
  "Compute the moment numerically for p ~ 10⁸ and compare with Σ E_C (if Var ≈ mean, the moment is Poisson-like).",
  ["level-aspect", "moments", "kuznetsov"], "med", "medium")
I("BGEXP", "Uniform spectral gap for the 'ES move graph' on residues mod q",
  "Bourgain–Gamburd give uniform expansion of Cayley graphs mod q. Define a graph on (ℤ/q)³ (or on SL₂(ℤ/q)) by ES-preserving moves (change of one word parameter) and test for a uniform spectral gap in q; uniform mixing would give quantitative equidistribution of words mod q with archimedean size control.",
  "Uniform-in-q expansion is the input for affine-sieve/Bourgain–Kontorovich-type counting, which is how thin-orbit local-global results are proved.",
  "Compute the spectral gap of the move graph for primes q ≤ 200 and look for uniformity.",
  ["expanders", "spectral-gap", "numerics"], "low", "cheap")
I("SUMPROD", "Multiplicative energy of divisor classes vs additive shifts N_e = (p + e)/4",
  "Sum-product: sets with small multiplicative energy have large sumsets. The divisor-class multisets of N_e across consecutive windows e (an additive progression in N) — compute their multiplicative energies; ES failure across many windows would force large multiplicative structure (subgroup trapping) along an additive progression.",
  "Quantitative version of the sum-product incompatibility item, measurable on data.",
  "For hard primes, compute E^×(classes of divisors of N_e mod e) for e ≤ 10³ and compare with random integers.",
  ["multiplicative-energy", "sum-product", "numerics"], "low", "cheap")
I("OPP", "Unipotent flows and ES words: the horocycle parametrisation of minus-continuants",
  "Margulis used unipotent orbits. The matrices M(t) = [[t, −1],[1, 0]] are products of a unipotent [[1, t],[0, 1]] and a fixed rotation, so ES words M(u)M(t)M(v) are points on products of horocycle segments. Read ES as a statement about a three-step 'unipotent walk' hitting a target integer matrix.",
  "Puts ES words into the language of unipotent dynamics, where every-orbit statements exist.",
  "Write M(u)M(t)M(v) = n(u) w n(t) w n(v) w and characterise which targets [[p, ·],[·,·]] are reachable with t ∈ 4ℤ; compare with horospherical equidistribution scales.",
  ["unipotent-dynamics", "SL2-words", "horocycles"], "med", "cheap", seen=["BRAINSTORM/thin_group_orbits.md"])
I("RATNER", "Effective equidistribution scale vs the required cusp depth (quantify the B2 gap)",
  "Every-orbit equidistribution theorems come with effective rates (Strömbergsson, Venkatesh). ES₅/word formulations require hitting regions of measure ≈ (log p)²/p-ish; compute the smallest measure of target region that current effective rates for closed horocycles of length p can resolve.",
  "Turns 'B2' into a number in the dynamics language: the exponent gap between the required and available resolution.",
  "From Strömbergsson's effective rate (Duke Math. J. 123 (2004): subsegments longer than ℓ^{1/2+ε} of a closed horocycle of length ℓ equidistribute; verified), compute the minimal region measure resolvable at length p and compare with the ES₅ target measure.",
  ["effective-rates", "B2", "gap-analysis"], "med", "cheap")
I("WEYL", "Equidistribution of (−(4p)⁻¹ mod d)/d as d varies: the trial-form sequence",
  "Weyl-type equidistribution of sequences {f(d)} mod 1. In the trial form, R(p)/2 = #{d : 4c_d | d + 1} with c_d = −(4p)⁻¹ mod d; the normalised residues c_d/d equidistribute in [0,1] as d varies (Kloosterman-type, Hooley/Duke–Friedlander–Iwaniec for modular inverses). ES needs the finer event 4c_d | d + 1, i.e. c_d/d near 0 with a divisibility condition.",
  "Equidistribution of modular inverses is a proven every-p theorem (for each fixed p as d varies); the certificate event is a thin, arithmetic refinement of it.",
  "Measure the discrepancy of {c_d/d : d ≤ D} for fixed p, and the hit rate of 4c_d | d + 1 among d with c_d/d < 1/(4·k).",
  ["equidistribution", "modular-inverses", "trial-form"], "high", "cheap", seen=["PARITY_AUDIT.md"])
I("FURST", "Non-lacunary semigroups of levels: multiplicative closure of 'working levels'",
  "Furstenberg's ×2×3 rigidity uses non-lacunarity of {2^a 3^b}. If level C works for p, does level C·k work for p for many k? (If d | 4Cp + 1 with d ≡ −1 mod 4C, then nothing obvious at level Ck.) Study whether the set of working levels for p is close to a multiplicative semigroup.",
  "If working levels had semigroup structure, rigidity theorems for multiplicative semigroups could constrain failure.",
  "For p ≤ 10⁷ compute the set of working levels and test closure under multiplication by small k.",
  ["semigroups", "levels", "odd"], "low", "cheap")
I("SENS", "Huang-type degree bound on the 'divisor-class hypercube' for windows with ω(N_e) = k",
  "Huang: any 2^{k−1}+1 vertices of Q_k induce max degree ≥ √k. For N_e squarefree with k prime factors, label each subset S by its class g(S) mod e; ES at window e ⟺ two disjoint subsets with g(S)/g(T) ≡ −1. Bound the largest family of subsets with no such pair; if it is ≤ 2^{k−1}, a signed-hypercube argument forces a certificate whenever 'many' subsets share a structure.",
  "A precise extremal question about labelled hypercubes that directly encodes window certificates.",
  "Compute by brute force, for e ≤ 50 and k ≤ 12 with random labels, the maximum certificate-free subset family size.",
  ["hypercube", "extremal-combinatorics", "windows"], "low", "cheap")
I("KEMNITZ", "Fixed-length subproducts: ES with a prescribed number of prime factors in the divisor",
  "Kemnitz/Reiher control zero-sums of prescribed length. Refine ES: is there always a certificate whose divisor d has exactly k prime factors for some small k (e.g. k ≤ 2)? If 'k ≤ 2' holds empirically, ES reduces to a statement about prime pairs (q₁ q₂ ≡ −1 mod 4C) — a zero-sum of length 2.",
  "A bounded-length version is much more structured (pairs of primes in classes) and amenable to sieve/character methods.",
  "For p ≤ 10⁸, record for each p the minimal Ω(d) over certificates; find primes requiring Ω(d) ≥ 3.",
  ["bounded-length", "zero-sum", "numerics"], "high", "cheap")
I("CHEVW", "Chevalley–Warning for the window system modulo e with a forced trivial solution",
  "Chevalley–Warning gives a nontrivial zero when the number of zeros is ≡ 0 (mod char) and a trivial zero exists. For window e (prime), consider the system over F_e in variables (exponent choices) encoding Π q_i^{ε_i} ≡ −1 · (trivial adjustment); design it so ε = 0 is a solution and the degree condition holds, forcing a nonzero ε.",
  "The classical algebraic route from 'many variables relative to degree' to existence; here variables = prime factors of N_e.",
  "Write the system for e = 3, 7, 11 with k prime factors and compute degree vs variables; find k at which Chevalley–Warning applies.",
  ["chevalley-warning", "windows", "algebraic-existence"], "low", "cheap")
I("EFL", "Absorbers from Mordell identities: reserve identity-covered structure to fix square classes",
  "Absorption reserves a structure that can repair any leftover. Mordell identities cover non-square classes; for a hard p, consider auxiliary integers N related to p (e.g. N_e = (p + e)/4, which may lie in easy classes) whose identity-certificates can be 'absorbed' into a certificate for p via the e-slice.",
  "Transfers the power of identities (which fail only on square classes) to hard p through an auxiliary object.",
  "For hard p, compute which N_e lie in identity-covered classes and whether their identity certificates translate into window certificates for p.",
  ["absorption", "identities", "e-slice"], "low", "cheap")
I("PFR", "Approximate-group structure of failing divisor-class sets",
  "PFR says sets with small doubling are close to subgroups (cosets). If at many levels the divisor-class sets of 4Cp + 1 have small doubling (as they would if trapped in subgroups avoiding −1), PFR-type structure theorems identify the subgroups; ES failure ⇒ many approximate subgroups ⇒ contradiction with CRT independence.",
  "Structure theorems turn 'avoidance' into explicit algebraic objects that can be compared across levels.",
  "Compute doubling constants |A·A|/|A| of divisor-class sets for hard p at levels C ≤ 200.",
  ["approximate-groups", "structure", "numerics"], "low", "cheap")
I("BREUSCH", "Distinct-denominator and ordering refinements as stronger every-n statements",
  "Breusch/Stewart required distinct denominators of a given parity. ES refinements: x < y < z distinct (automatic except special cases), x ≤ p/2, z ≤ p²/2, gcd conditions. Determine the strongest refinement that still holds for all p ≤ 10⁹; it defines the 'tightest' every-p target.",
  "The tightest true statement carries the most structure for a proof and the most information for disproof searches.",
  "Tabulate, for p ≤ 10⁹, the minimal max-denominator over solutions normalised by p², and other extremal statistics.",
  ["refinements", "extremal-statistics", "numerics"], "high", "cheap")
I("FIBSYL", "Odd greedy algorithm as a cautionary every-n problem",
  "The odd greedy expansion (always choose the smallest odd denominator) is conjectured to terminate for every rational with odd denominator, but this is open even though Breusch/Stewart show odd representations exist. ES has the same split: existence vs a specific algorithm. Keep proofs about existence, not about a fixed procedure (consistent with B1's bounded-procedure barrier).",
  "Prevents investing in 'prove algorithm X always succeeds' routes that are harder than existence.",
  "List ES approaches in the repo that are algorithmic (fixed search order) and mark which could be restated as pure existence.",
  ["algorithms-vs-existence", "cautionary", "meta-strategy"], "high", "cheap")
I("SUN135", "Sun-style refinements as data: four-square-like refinements of ES",
  "Sun formulated many 'refined Lagrange' conjectures by computer search; several were proved. Generate ES refinements automatically (x + y or z constrained to be a square, a prime, ≡ r mod m, etc.), test them to 10⁷, and keep those that never fail — new conjectures whose extra structure may make them provable or reveal hidden symmetries.",
  "Automated conjecture generation found provable statements for sums of squares; ES has never been mined this way systematically (check repo).",
  "Write a search over ~200 refinement predicates P(x, y, z, p) and test on all p ≤ 10⁶; report survivors.",
  ["conjecture-generation", "refinements", "data-mining"], "med", "cheap")
I("ONO", "Distribution of R(p) modulo small primes ℓ (Ono-style equidistribution vs bias)",
  "Ono/Ahlgren studied p(n) modulo m: every residue class occurs. For ES, study R(p)/2 mod ℓ: equidistribution would be 'no structure', while a bias toward nonzero residues on some class would be a usable congruence. In particular check whether R(p)/2 ≡ 0 (mod ℓ) occurs with frequency ≈ 1/ℓ.",
  "Cheap probe for hidden modular structure in the counts.",
  "Compute the distribution of R(p)/2 mod 2, 3, 5, 7 over primes in each Mordell-hard class up to 10⁷.",
  ["congruences", "distribution", "numerics"], "high", "cheap")
I("KNESER", "Sperner/Tucker on the level × divisor grid",
  "Sperner's lemma forces a fully-labelled cell in any boundary-respecting labelling. Lay out levels C (one axis) and divisor sizes log d / log N (other axis); label grid cells by the class of the divisor relative to −1 (mod 4C); boundary conditions come from trivial divisors (1 and N always in class 1). A fully-labelled cell would be a certificate.",
  "Odd, but Sperner-type lemmas give existence from boundary data alone.",
  "Construct the labelled grid for small p and check whether natural boundary conditions hold and what a fully-labelled cell means.",
  ["sperner", "topological-combinatorics", "odd"], "low", "cheap")
I("MOLS", "Recursive product constructions: certificates for p from certificates for pieces of 4Cp + 1",
  "Bose–Shrikhande–Parker built orthogonal Latin squares of composite orders from smaller ones. For ES, 4Cp + 1 = N₁N₂ (coprime): if N₁ has a divisor ≡ a (mod 4C) and N₂ one ≡ b with ab ≡ −1, the product is a certificate. Study 'recursive' constructions splitting N and combining class information from each piece.",
  "Product constructions are the combinatorial counterpart of the Kneser/product-set items, with an explicit recursive structure.",
  "For hard p, enumerate coprime splittings of 4Cp + 1 and compute the class sets of divisors of each piece; count combinations giving −1.",
  ["recursive-construction", "product-sets", "levels"], "med", "cheap")
I("SML", "Periodicity of certificate patterns along n = a·b^s + c (p-adic interpolation), automated",
  "SML's p-adic interpolation implies periodic structure of divisibility along exponential sequences. Automate: for each open exponential family in the repo and each small certificate shape (C, d-class), compute the set of s where it applies (periodic mod ord_d(b)); solve the resulting covering problem over s with an ILP.",
  "Mechanises the repo's family proofs and either proves open families or identifies a residual progression of s as a disproof candidate.",
  "Implement for 15·2^s + 1 and 4^s + 297 with d ≤ 10⁵, C ≤ 10³.",
  ["exponential-families", "covering", "automation"], "high", "cheap", seen=["BRAINSTORM/bsE_padic_interpolation.md"])
I("POINC", "Surgery on near-certificates: local modifications that remove a single obstruction",
  "Perelman's surgery removes singularities and continues the flow. For a near-certificate at level C (a divisor d of 4Cp + 1 in a class ≠ −1), define 'surgeries' changing one prime factor (moving to another level C′ sharing that factor via CRT) and study whether repeated surgery reaches a certificate.",
  "Gives a local-move graph on near-certificates across levels, linked by shared prime factors.",
  "Build the graph (nodes: (C, d); edges: share a prime factor q, C ≡ C′ (mod q)) for small p and search paths to certificates.",
  ["surgery", "move-graphs", "odd"], "low", "cheap")
I("RINGEL", "Current-graph-style explicit constructions for one residue class mod a large modulus",
  "Ringel–Youngs used 'current graphs' — compact algebraic data generating a whole family. For one Mordell-hard class r mod M (M large, e.g. 840·1001), search for compact algebraic data (a finite list of certificate templates with parameters depending on p's residues mod M′) covering all primes in that class up to 10⁹.",
  "Even if B1 forbids bounded templates for all p, the minimal template count per class reveals growth rates and hidden structure.",
  "Run a greedy set-cover of primes in the class by parametric templates (Type II with C | M′) and plot template count vs X.",
  ["templates", "set-cover", "numerics"], "med", "cheap", seen=["POINTWISE_SIZE.md"])
I("SIEGEL", "Landau–Siegel 'at most one exceptional modulus' analogue for ES levels",
  "Landau: at most one real character mod q ≤ Q has L(1,χ) tiny. ES analogue: among the characters χ_{−4uB} driving M_BM, show at most one (or boundedly many) can be 'exceptional' at p (strongly biased), so M_BM stays large except via one identifiable character whose effect can be handled separately.",
  "The 'at most one exception' structure is what makes Siegel-type arguments work; ES's main term is a sum over many real characters.",
  "Model T(p) as a sum over real characters and quantify how much a single character can reduce M_BM; compare with the observed minima of M_BM/L².",
  ["exceptional-characters", "landau-siegel", "BM-main-term"], "med", "cheap")
I("AKS", "Polynomial congruence certificate: an identity in ℤ[X]/(X^r − 1, p) detecting ES",
  "AKS used a polynomial congruence that holds iff n is prime. Ask whether ES(p) has a characterisation by a polynomial identity modulo (X^r − 1, p) or modulo auxiliary moduli (e.g. a product over levels of polynomials whose evaluation detects certificates), testable deterministically.",
  "Odd: algebraic characterisations sometimes admit clean counting proofs (as in AKS's group-size argument).",
  "Construct the generating polynomial P_p(X) = Π_{C ≤ K} (1 − X^{[level C fails]}) style objects and look for algebraic relations they satisfy for all p.",
  ["polynomial-identities", "algebraic-characterisation", "odd"], "low", "medium")
I("ZAREMBA", "Thin-semigroup local-global with the ES constraint t ∈ 4ℤ ∪ (8ℤ − p): local obstructions?",
  "Bourgain–Kontorovich require knowing the local (congruence) obstructions of the semigroup before counting. Compute the reductions mod q of the ES-word set with the constraint on t (4ℤ for one branch, 8ℤ − p for the other, which depends on p!) and determine exactly which residues of p are locally admissible; check that only squares-related obstructions appear (T1-type).",
  "The p-dependent constraint (8ℤ − p) is unusual for thin-orbit theory; its local analysis is a concrete, finite task.",
  "For q ≤ 200 compute the set of p mod q (and mod 8q) hit by words with each constraint branch.",
  ["local-obstructions", "thin-orbits", "SL2-words"], "high", "cheap")
I("MARKOFF", "Strong approximation mod p for the ES surface fibre U_p (BGS-style) — sanity check",
  "BGS proved Markoff surfaces satisfy strong approximation mod p for most p. For ES, check the analogous local statement: does U_n(ℤ) → U_n(ℤ/q) have dense image for various q (it is BM-obstructed for strong approximation by BL)? Quantify the BL obstruction concretely on data.",
  "Makes BL's 'BM obstruction to strong approximation always exists' concrete and shows which residue patterns ES solutions avoid.",
  "For small n with many solutions, compute the reductions of solutions mod q and compare with U_n(ℤ/q).",
  ["strong-approximation", "brauer-manin", "numerics"], "high", "cheap")
I("DS", "Erdős–Vaaler-type restricted versions: ES with levels restricted to squarefree or prime C",
  "Before Duffin–Schaeffer was proved in general, restricted cases (ψ supported on special sets) were proved first. Restrict ES (★) to prime levels C (or squarefree C): the overlap structure simplifies (gcd(C, C′) = 1). Study the prime-level-only (★) failure set and its overlap model.",
  "Restricted versions with clean overlap structure are the natural first targets of a Duffin–Schaeffer-type method.",
  "Compute (★) restricted to prime C for p ≤ 10⁹ and list failures; fit an independence model.",
  ["restricted-versions", "overlap", "numerics"], "high", "cheap")
I("TITCH", "Divisor sum over shifted primes reversed: Σ_{q prime} 1[q | p + m] for structured m",
  "The Titchmarsh divisor problem counts divisors of shifted primes. The trial form needs prime (or general) divisors of p + u in the class −1 mod (stuff tied to u); reverse the roles: for fixed p, count primes q ≡ 3 (4) with q | p + u and q = 4uC − 1 for some C — a 'Titchmarsh problem with a tied modulus' at a single p.",
  "Relates single-prime certificates to the distribution of prime divisors of p + u, a classical object.",
  "Count, for fixed p, pairs (u, q) with q | p + u, q ≡ −1 (mod 4u), q prime; compare with heuristic Σ_u τ*/φ(4u).",
  ["titchmarsh", "single-prime-certificates", "numerics"], "med", "cheap")
I("TART", "Siegel–Weil for indefinite ternary forms with congruence: ES's SL₂ quadric",
  "For indefinite forms in ≥ 3 variables representing a number, Siegel–Weil and strong approximation (spin groups) give local-global with spinor exceptions. The SL₂ form ad − pc = 1 is an indefinite ternary quadric; the ES congruence a ≡ d ≡ −1 (mod c) is not a lattice coset condition (modulus = coordinate), so classical theory does not apply directly. Find a reformulation where the congruence becomes a fixed-modulus coset condition.",
  "If achieved, strong approximation for spin groups (no spinor obstruction ⇒ every locally represented integer is represented) would be the closing theorem.",
  "Try substitutions a = ck − 1, d = cl − 1 and fix c's residue class; examine whether the resulting variety in (k, l, c) is homogeneous for a group with strong approximation.",
  ["strong-approximation", "indefinite-forms", "reformulation"], "med", "medium")
