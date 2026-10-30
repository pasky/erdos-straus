# Items batch 1: additive / circle method / quadratic forms (TG .. CAUCHY). I() is injected by the builder.

I("TG", "Helfgott meet-in-the-middle: an explicit 'all p > X' theorem for any ES sub-route with X ≤ 10¹⁸",
  "Ternary Goldbach became 'every n' only when the analytic threshold dropped below the numerical verification horizon (8.875·10³⁰). ES is verified to 10¹⁸; any effective all-large-p statement for (★), b=1, ES₅ or Type II with p₀ ≤ 10¹⁸ closes ES.",
  "Turns the goal from 'prove for all p' into 'make some asymptotic statement effective with a concrete constant', which is how Vinogradov→Helfgott actually moved.",
  "Make a table: every asymptotic/conditional ES statement in FRONTIER §2.4/§5 (H⁻_BM, Thm 2.2, ES₅ Thm 3.5) with the explicit p₀ it would need and the explicit constants it currently lacks.",
  ["effective-threshold", "verification", "meta-strategy"], "high", "medium")
I("TG", "Explicit Burgess constants (Treviño-type) for the Legendre-sum T(p) in M_BM",
  "Helfgott needed fully explicit major arcs; the ES analogue is an explicit version of Thm 2.2 (M_BM(p) ≥ (3/16π² − o(1)) log²p), whose o(1) comes from Burgess on Σ(−m/p)w(m).",
  "An explicit M_BM ≥ c·log²p for all p ≥ p₁ is a prerequisite of every H⁻_BM-type route and is purely a bookkeeping task with existing explicit Burgess inequalities.",
  "Treviño, 'The Burgess inequality and the least kth power non-residue', IJNT 11 (2015) 1653–1678, arXiv:1412.3062 gives explicit Burgess estimates (verified, data/z52b/upgrades_leads_check.md); check that its ranges cover the weighted hyperbolic sum T(p) and compute the resulting explicit p₁.",
  ["explicit-constants", "burgess", "BM-main-term"], "high", "medium", kw=["Treviño"])
I("TG", "Smoothing as a decisive ingredient: smooth weights on (u,B,C) for a weighted R_w(p)",
  "Helfgott's minor arcs only closed after choosing smoothing functions optimally. ES: replace R(p) by R_w(p) = Σ w(u,B,C)1[4uBC−u−B=p] with smooth nonnegative w; R_w(p) > 0 ⇒ ES(p).",
  "Error terms in Poisson/Voronoi-based treatments of R(p) depend heavily on sharp cut-offs of the hyperbolic region; smoothing is free for a positivity statement.",
  "Numerically compare Var_p(R_w(p)/M_w(p)) over primes near 10⁷ for sharp vs. Gaussian/Beurling–Selberg weights; pick the weight minimising the left tail.",
  ["smoothing", "numerics", "weights"], "high", "cheap")
I("TG", "Vinogradov bilinear decomposition of the (★) count",
  "Vinogradov's Type I/II bilinear sums made ternary Goldbach unconditional. R(p) = Σ_C #{d | 4Cp+1 : d ≡ −1 (4C)} is a sum over factorizations ab = 4Cp+1; split by the sizes of a, b, C into 'Type I' (one factor short: congruence sums in C) and 'Type II' (both medium: bilinear forms in (a,b)).",
  "Gives a structured place where cancellation must be found; the Type I part may be treatable pointwise in p by elementary counting.",
  "Write R(p) = Σ_{a,b} α_a β_b 1[ab ≡ 1 mod 4C, ab = 4Cp+1] with dyadic ranges; compute numerically which range carries the solutions for p ~ 10⁸–10¹⁰.",
  ["bilinear-forms", "type-I-II", "decomposition"], "med", "medium")
I("BG", "Sparsity index: why binary Goldbach is stuck and ES is worse",
  "Binary Goldbach has a main term n/log²n among ~n terms and never got pointwise; ES has main term ≍ log²p among ≍ p log p 'trial events' (PARITY_AUDIT trial form).",
  "Quantifies how far ES is from any problem ever upgraded; directs search to reformulations with denser events (fewer trials, larger main term).",
  "Define sparsity = log(main term)/log(#trials) for each ES reformulation (★, b=1, ES₅, e-slice, I3 words) and tabulate; look for the least sparse one.",
  ["meta-strategy", "binary-problem", "reformulation"], "high", "cheap")
I("BG", "Montgomery–Vaughan power-saving exceptional set for ES or (★)",
  "MV proved E_Goldbach(N) ≪ N^{1−δ} by large sieve + zero density + Siegel-zero analysis; ES has only E(N) ≪ N exp(−c(log N)^{3/4}) and 3/4 is sharp for CRT sieves (EXCEPTIONAL_KARY3).",
  "A power-saving exceptional set would need exactly the non-CRT input the campaign identified (residue-dense large sieve); MV is a model of how that input looked for Goldbach.",
  "Read MV §§3–6 and identify the step that becomes 'large sieve over moduli 4uB with p in the variable'; check whether the ES analogue of their Siegel-zero case analysis is available.",
  ["exceptional-set", "large-sieve", "power-saving"], "med", "big")
I("BG", "Goldbach exceptions are tied to one exceptional character — are ES/(★) failures tied to a character?",
  "In MV the only way to have many Goldbach exceptions is a Siegel zero. Analogue: (★)-failures (14 primes ≤ 10¹⁰) and b=1 failures (193, 2521, 66529) might share an extreme value of a single character statistic (e.g. least non-residue ℓ(p), or L(1, (·/p))).",
  "If failures of sub-routes are 'explained' by one character, a Deuring–Heilbronn-type dichotomy becomes plausible.",
  "For the 17 known sub-route failures and random controls compute ℓ(p), Σ_{m≤100}(m/p)/m, L(1,(·/p)) and the class number of Q(√p); compare ranks.",
  ["exceptional-character", "numerics", "least-nonresidue"], "high", "cheap", kw=["least non-residue"])
I("CHEN", "Chen switching for ES: Type I ↔ Type II role switch to upper-bound 'near misses'",
  "Chen bounded the bad P₃ contribution by sieving the switched set. ES: a 'near miss' at level C is a divisor of 4Cp+1 in a wrong class; switching d ↔ (4Cp+1)/d and C ↔ another parametrisation (Type I ↔ Type II) may convert hard lower bounds into upper bounds of a switched count.",
  "Lower bound = (computable total) − (upper-bounded bad part) is the only robust way sieves get existence.",
  "List all involutions/bijections between ES certificate sets (Type I/II, (★)↔b=1, level switching) and check whether any maps near-misses of one family to near-misses with a computable total in another.",
  ["switching", "sieve", "type-I-II"], "med", "medium")
I("CHEN", "Almost-prime levels: choose C with 4Cp+1 = q₁q₂ (two primes) and study the class of q₁ mod 4C",
  "Chen-type results produce almost-primes in linear sequences. If 4Cp+1 = q₁q₂, the certificate condition at level C is q₁ ≡ −1 (mod 4C), a single-prime class condition.",
  "Reduces a divisor-class problem to an equidistribution question for prime factors of almost-primes in a progression, a better-studied object.",
  "For p ~ 10⁸ and C ≤ 10⁵ measure: fraction of C with 4Cp+1 = P₂, and the rate at which a factor hits −1 mod 4C versus the model 2/φ(4C).",
  ["almost-primes", "numerics", "chen-sieve"], "med", "cheap")
I("SCHN", "Schnirelmann/Mann in the space of fractions: ES as U + (U+U) ∋ 4/n",
  "Schnirelmann turned a positive density for P+P into 'every n'. ES asks 4/n ∈ U+U+U (U = unit fractions). Translate to: 4/n − U meets U+U, and look for Mann-type sumset theorems for sets of rationals with structured denominators.",
  "4-term ES is trivial (4/p = 1/(k+1) + 3/(p(k+1)) and 3/m always splits into ≤ 3 terms), so the problem is exactly the 'order 3 vs order 4' gap of a basis — a classical additive-combinatorics shape.",
  "Formalize U+U as {a/b : b has a divisor pair (d,e) with d+e ≡ 0 mod a}; study the measure/density of 4/n − U ∩ (U+U) for n in a dyadic range.",
  ["additive-basis", "sumset", "egyptian-fractions"], "low", "medium")
I("SCHN", "Diophantine approximation spectrum of 4/p by three unit fractions",
  "Schnirelmann-type arguments start from approximate representations. Define δ(p) = min_{x,y,z} |4/p − 1/x − 1/y − 1/z| over x,y,z ≤ p^A (A large enough that all solutions are included); ES(p) ⟺ δ(p) = 0. Study the gap structure of the set of values near 4/p.",
  "If near-solutions are abundant at scale p^{−k} and the set of 3-term sums has a 'no isolated gap' property near 4/p, existence might follow by a continuity/pigeonhole step.",
  "Compute the k smallest nonzero |4/p − Σ| for p ≤ 10⁵ and look for universal patterns in the residual numerators.",
  ["approximation", "numerics", "egyptian-fractions"], "low", "cheap")
I("GL", "Powers-of-two slice: ES solutions with x = 2^k",
  "Goldbach–Linnik used the lacunary set of powers of 2. ES slice: 4/p = 1/2^k + 1/y + 1/z needs (2^{k+2} − p)/(p·2^k) to split into two unit fractions; e.g. via the divisor p it needs (2^{k+2} − p) | (2^i + 1) for some i ≤ k+2.",
  "A lacunary, explicit family of candidate first denominators with rich multiplicative structure (2^i+1 factors via cyclotomy) — the ES analogue of Linnik's 2^v.",
  "Compute, for p ≡ 1 (mod 24) up to 10⁷, the fraction of p having an ES solution with a power-of-2 denominator and the distribution of the least k.",
  ["lacunary", "numerics", "explicit-family"], "high", "cheap")
I("GL", "Measure of joint failure along a lacunary level sequence C ∈ {2^j}",
  "Linnik's key estimate is the small measure of α where Σ e(2^v α) is large. Analogue: the set of p failing (★) at every level C = 2^j, j ≤ J, should have density ≈ Π_j(1 − P_j); measure its correlation structure.",
  "Lacunary levels give nearly independent constraints (moduli 2^{j+2} are nested though!) — quantifies how much independence nested moduli really give.",
  "Compute failure indicators at C = 2^j for p ≤ 10⁸ and estimate joint failure probabilities versus the independent model.",
  ["lacunary", "independence", "numerics"], "med", "cheap")
I("WAR", "Universal-form reduction: a map from representations by a universal quadratic form to ES certificates",
  "Linnik/Watson reduced 7 cubes to ternary forms; Hilbert used identities + Lagrange. Seek a quadratic form Q_p (or a fixed universal Q) and an explicit rational map Φ such that every representation Q(v) = g(p) yields an ES solution for p; universality/three-squares then proves ES.",
  "Not a polynomial identity in p (so Mordell–Schinzel does not apply directly); the map may depend on the representation. Must be compatible with T1 (Type I/II fail at odd squares).",
  "Search small Φ: take ES (★) triples (u,B,C) for many p and test whether u, B, C, or 4uC−1 are systematically sums of two/three squares with coordinates linked to p.",
  ["quadratic-forms", "reduction", "identities"], "med", "big", kw=["universal form"])
I("WAR", "Smooth-number restriction (Vaughan–Wooley) with smooth moduli in APs (Drappeau/Harper)",
  "Smooth numbers drove progress on G(k). ES: restrict certificates to smooth (u,B) or smooth 4C, where distribution in progressions to large moduli is better (friable Bombieri–Vinogradov beyond 1/2).",
  "Smooth moduli are where the strongest level-of-distribution results live; ES certificates are numerically often smooth.",
  "Drappeau, 'Théorèmes de type Fouvry–Iwaniec pour les entiers friables', Compositio 151 (2015), arXiv:1307.7554 (verified) gives beyond-√ distribution for friable integers; check whether it applies to sums Σ_{C smooth} #{d | 4Cp+1, d ≡ −1 (4C)}; measure numerically the fraction of (★) solutions with y-smooth C for y = p^{0.1}.",
  ["smooth-numbers", "level-of-distribution"], "med", "medium", kw=["friable", "smooth moduli"])
I("WAR", "g(4)=19 descent: analytic threshold + greedy reduction to the verified range",
  "BDD reduced every n below 10³⁶⁷ to the verified range by subtracting biquadrates. ES has no subtraction structure, but the e-slice form reduces ES(p) to a property of N = (p+e)/4 < p; formalize a 'descent' that moves a hard instance to a smaller one.",
  "If certificate existence at p could be read off from data at N ≈ p/4 that is itself verifiable recursively, verification scales.",
  "Measure: for the hardest primes (DISPROOF_AVENUES list) how many e ≤ 1000 give N = (p+e)/4 with ≥ k divisors; is there always an e with N highly composite?",
  ["descent", "verification", "e-slice"], "med", "cheap")
I("LIN7", "Ternary-form reduction with Duke–Schulze-Pillot as the closing theorem",
  "Linnik's 7 cubes: identity reduces the problem to n − (cubes) being represented by a ternary quadratic form in an AP, closed by ternary-form theory. ES: find an ES-certificate family equivalent to 'some N(p) is primitively represented by a positive ternary form in a fixed genus'.",
  "DSP gives every sufficiently large n in the spinor genus (ineffectively) — an 'all large p' ES theorem even if ineffective would be new.",
  "Search the (★)/b=1/ES₅ certificate shapes for a sum-of-three-squares interpretation (e.g. 4Cp+1 = d d' with d = x²+y²+z²-type constraint); test on data.",
  ["ternary-forms", "reduction", "ineffective"], "med", "big")
I("LIN7", "Divisor counts in a class as coset theta series of the split form xy",
  "Watson's trick works with sums of squares in arithmetic progressions (coset theta series). D_t^−(N) = #{xy = N, x ≡ −1 (t)} is a representation number of the indefinite binary form xy on a lattice coset.",
  "Puts ES level counts into the language of (indefinite) lattice cosets where theta-lifts and Siegel–Weil apply; METAPLECTIC_ES already gives the generating function.",
  "Write Σ_N D_t^−(N)q^N as a coset theta series of xy and compare with METAPLECTIC_ES Thm K; then try a theta lift to a ternary/quaternary positive form.",
  ["theta-series", "lattice-cosets", "split-form"], "high", "medium", kw=["theta quotient"])
I("VMVT", "Decoupling/energy for the hyperbolic ES surface {4uBC − u − B}",
  "BDG decoupling bounds moments of exponential sums over curves. Additive energy of the ES-word set (#{w₁ = w₂} with w = 4uBC−u−B ≤ N) controls the second moment Σ_n R(n)².",
  "Second-moment control is the ingredient of every almost-all → pointwise attempt via variance; decoupling-type bounds for this specific surface could be sharp.",
  "Compute the energy E(N) = Σ_{n≤N} R(n)² for N up to 10⁷ and fit N·(log N)^a; compare with what a decoupling inequality for (u, B, uB) would predict.",
  ["decoupling", "energy", "second-moment"], "med", "medium", seen=["data/energy_note"])
I("VMVT", "Efficient congruencing in the level variable",
  "Wooley's method lifts solutions p-adically and compares congruence classes at several scales. ES solutions as solutions of p ≡ −(u+B) (mod 4uB) for growing 4uB: congruencing across scales of the modulus.",
  "Odd but not empty: ES is literally a family of congruences whose modulus is a variable; congruencing-type iteration handles such 'modulus as variable' counts in VMVT.",
  "Write the count of (u,B) with 4uB ≤ Q and p ≡ −(u+B) mod 4uB as a mean value of a Weyl-like sum and see if the efficient-congruencing recursion has an analogue.",
  ["congruencing", "odd"], "low", "medium")
I("HLP", "Linnik dispersion for the fixed-p level sum Σ_C D(4Cp+1; −1 mod 4C)",
  "Linnik proved an asymptotic for every n of #{n = p + x² + y²} = Σ_p r₂(n − p): a pointwise result for a sum of divisor-type functions. R(p) is a sum over C of restricted divisor counts of 4Cp+1.",
  "The dispersion method is one of the few techniques giving pointwise-in-n asymptotics for sums of arithmetic functions over a sparse family — exactly ES's shape, though the main term is only polylog.",
  "Compute Disp(p) = Σ_C (D_C(p) − 2/φ(4C)·τ*(4Cp+1))² for test p and compare with M(p)²; if Disp ≪ M², a dispersion-type proof is not excluded numerically.",
  ["dispersion", "pointwise", "divisor-sums"], "med", "medium", kw=["dispersion method"])
I("HLP", "Divisor function in APs to a single modulus 4p as the base asymptotic",
  "Σ_{C≤X} τ(4Cp+1) is a divisor sum in the progression 1 mod 4p; asymptotics are known for X ≥ (4p)^{2/3+ε} (Selberg/Hooley/Heath-Brown/Fouvry–Iwaniec-type). The ES count refines τ to the class d ≡ −1 (mod 4C).",
  "Starts from a pointwise-in-p theorem that is already true, and asks for a twist by the 'self-referential' modulus 4C — a precise, new-looking question.",
  "Write D(4Cp+1; −1 mod 4C) via additive characters mod 4C and apply Voronoi summation in C to the twisted divisor sum; identify which terms are new.",
  ["divisor-in-AP", "voronoi", "pointwise"], "high", "medium", kw=["Voronoi"])
I("LAG", "Lagrange descent on near-certificates via a composition law",
  "Lagrange got every p by producing m·p = sum of 4 squares with m < p and descending m using Euler's identity. ES needs a composition law on 'defective' certificates (defect m) that lowers |m|.",
  "Descent is the oldest almost→every mechanism; ES lacks an obvious composition, but the SL₂ form (matrices [[a,p],[c,d]]) has matrix multiplication.",
  "Define defect for SL₂-form near-certificates (e.g. congruence a ≡ −1 only mod c/m); test whether products/quotients of two near-certificates with the same defect yield smaller defect.",
  ["descent", "composition-law", "SL2"], "med", "medium")
I("LAG", "Chord–tangent operations on the ES cubic surface family",
  "Euler's identity is a composition law on norm forms. The ES surface 4xyz = n(xy+yz+zx) is a cubic surface; secant/tangent constructions (Manin) generate rational points from rational points.",
  "Rational points are plentiful; the question is whether some composition preserves integrality or near-integrality across fibres n.",
  "Implement the secant operation on U_n(ℚ) and measure denominators of the third point when the two inputs are integral points of nearby fibres (n, n') with n' | n·k.",
  ["cubic-surface", "composition-law", "geometry"], "low", "medium")
I("LAG", "Pigeonhole over complementary divisor sets: |Div(N₁)| + |Div(N₂)| > φ(e) forces a certificate",
  "Lagrange's lemma: the sets {x²} and {−1−y²} each have (p+1)/2 elements so they meet. ES e-slice: for a coprime split N = N₁N₂ (N = (p+e)/4), if |Div(N₁) mod e| + |Div(N₂) mod e| > φ(e), some a | N₁ and b | N₂ satisfy a ≡ −b, so −1 ∈ Rat_e(N).",
  "A clean sufficient condition reducing ES to finding e with N highly composite relative to φ(e).",
  "For p in the hard list, search e ≤ 10⁴ maximising (|Div(N₁)|+|Div(N₂)|)/φ(e) over coprime splits; report how close to 1 the best ratio gets.",
  ["pigeonhole", "e-slice", "divisor-classes"], "high", "cheap", seen=["BRAINSTORM/s6_divisor_pigeonhole.md"])
I("TWOSQ", "Zagier-type involution with a unique fixed point on an ES-related finite set",
  "Zagier: a finite set with two involutions; one has exactly one fixed point ⇒ odd cardinality ⇒ the other has a fixed point = representation. ES: find a finite set S_p (defined by ES-like equations) with an involution whose fixed points are ES certificates and another with a unique fixed point.",
  "Parity replaces analysis entirely; it is the only known 'proof from the Book' mechanism for an every-p existence theorem of this flavour.",
  "Enumerate small finite sets S_p = {(a,b,c,d) ∈ ℕ⁴ : quadratic/cubic ES-like relation = p} with natural windmill-type involutions; compute |S_p| mod 2 for p ≤ 10⁴ and look for sets with provably odd size.",
  ["parity", "involution", "proof-from-the-book"], "high", "medium", seen=["BRAINSTORM/invol_windmill_signature.md", "BRAINSTORM/y2_parity_involution.md"])
I("TWOSQ", "Naive parity of a level count is trivial — record the lemma and the needed asymmetry",
  "D_t^−(tp+1) is even unless tp+1 = s² with s ≡ −1 (mod t), i.e. unless p = t − 2; so parity of single-level counts carries no information (pairing d ↔ N/d). Zagier needed an asymmetric second involution.",
  "Clears a trap: any parity proof needs a set where the obvious involution is broken (e.g. by a non-symmetric constraint like d < N/d with an extra condition).",
  "Write the lemma; then search for natural subsets (e.g. d in a half-interval, or d with an extra character condition) where the count is not forced even and test its parity distribution.",
  ["parity", "lemma", "negative-result"], "high", "cheap")
I("TWOSQ", "Dedekind's Gaussian-integer proof analogue: an order where ES(p) ⟺ p is a norm",
  "Fermat two squares follows from ℤ[i] being Euclidean. Find a (possibly noncommutative) ring/order R and norm-like map such that ES certificates ↔ elements of 'norm' p with congruence side conditions; then a class-number-one/Euclidean property gives existence.",
  "Quaternion orders and theta quotients already appear in the repo; the missing piece is a ring whose class number is 1 and whose norm condition matches the ES congruences.",
  "Read the quaternion-order memos (git grep -il quaternion); compute class/type numbers of the orders arising there.",
  ["quaternion-orders", "class-number-one", "norm-form"], "med", "medium", kw=["quaternion order"])
I("THUE", "Thue's lemma / short vectors in lattices L_{p,λ} producing (★) triples",
  "Thue's pigeonhole gives |x|,|y| ≤ √p with x ≡ λy (mod p). Choose λ from ES structure (e.g. λ ≡ −4⁻¹ or ratios from Rat_e) and test whether short vectors produce positive (★) data.",
  "Pigeonhole-in-a-box is the cheapest every-p mechanism; ES's linear congruence p ≡ −(u+B) (mod 4uB) has a modulus depending on the unknowns, so a 2-D lattice must be found for each candidate level.",
  "For fixed C (or u), (★) says 4uC − 1 | p + u: build the lattice {(x,y) : x ≡ y·λ_C mod (something)} and check numerically whether LLL-short vectors give solutions.",
  ["pigeonhole", "geometry-of-numbers", "lattices"], "med", "cheap", seen=["BRAINSTORM/gon_lll_relation_lattice.md"])
I("THUE", "Small vector + congruence ⇒ equality, for the cubic ES polynomial (Ankeny-style)",
  "Thue/Ankeny: if F(v) ≡ 0 mod M and |F(v)| < M then F(v) = 0. For F = 4xyz − p(xy+yz+zx) with |v| ≈ X: |F| ≈ pX² and Minkowski gives |v| ≈ M^{1/3}; the scales match when M ≳ p³, X ≈ p.",
  "The scale bookkeeping does not immediately fail; the open question is whether an affine sublattice of index ~M on which F ≡ 0 (mod M) exists.",
  "Classify affine sublattices of ℤ³ on which F vanishes mod q for primes q (e.g. the Type II slices y,z ≡ 0 mod p); see if CRT combinations of such slices reach M ≳ p³.",
  ["geometry-of-numbers", "minkowski", "cubic"], "low", "medium")
I("THREESQ", "Class number one in the genus: search for an ES-encoding lattice with a one-class genus",
  "Gauss's three squares: local solvability + one class in the genus of x²+y²+z² ⇒ global. ES is locally solvable everywhere (Bright–Loughran); if ES(p) ⟺ a lattice L represents an invariant of p, and gen(L) has one class (or one spinor genus), ES follows.",
  "The most classical local→global mechanism; repo has quaternion/lattice reformulations whose class numbers may never have been computed.",
  "For each lattice reformulation in the repo, compute the class number of its genus (Sage/Magma genus enumeration) for small parameters.",
  ["class-number-one", "local-global", "lattices"], "med", "medium")
I("THREESQ", "Auxiliary-prime skeleton of the three-squares proof applied to ES windows",
  "Gauss/Dirichlet: choose an auxiliary prime q with (−n/q) = 1, build a form of determinant 1 representing n, then use one class. ES windows: auxiliary prime q ≡ 3 (4), (q/p) = −1, K = (p+q)/4 (FORCED_WINDOW). Mirror each step: is there an object 'of determinant 1' built from (p,q) whose uniqueness forces −1 ∈ Rat_q(K)?",
  "The auxiliary-prime step is already in the campaign; the missing 'uniqueness of the class' step is the one Gauss had and ES lacks.",
  "Write the window certificate as a statement about a binary/ternary form built from (p, q, K) and compute its genus/class structure for small cases.",
  ["auxiliary-prime", "windows", "local-global"], "med", "medium", seen=["FORCED_WINDOW.md"])
I("CAUCHY", "Cauchy-lemma analogue: simultaneous control of (u+B, uB)",
  "Cauchy's lemma represents a number and its 'trace' simultaneously. (★) in pair form: s = u+B, q = uB with s ≡ −p (mod 4q) and s² − 4q a square. Seek an inequality region in (s,q) where existence is forced, as Cauchy's b² < 4a, 3a < b²+2b+4 does.",
  "Simultaneous norm/trace representation is the mechanism behind every-n polygonal theorems; ES's (s,q) formulation is of the same shape (sum and product of two unknowns).",
  "Plot, for many p, the set of (s,q) satisfying the congruence and check where the 'square discriminant' condition is hit; look for a region of guaranteed hits.",
  ["simultaneous-representation", "norm-trace"], "low", "cheap")
I("TART", "Power-size main term requirement: lift ES to a variety with power-many points fibred over certificates",
  "Tartakowsky/Kloosterman work because the Eisenstein term ≍ n^{k/2−1} beats cusp-form bounds; ES's main term is log²p. Seek V_p → {ES certificates of p} with fibres of size p^δ (nontrivial geometry), so V_p's point count has a power-size main term that vanishes iff ES(p) fails.",
  "Changes the competition 'polylog main term vs. error' into 'power main term vs. error' — the only regime where every-n theorems for forms were ever proved.",
  "Construct candidates V_p (e.g. adjoin variables parametrising the Type II h-family or the factorizations of 4Cp+1 into 3 factors) and compute their point counts and singular series.",
  ["main-term-size", "fibration", "circle-method"], "med", "big")
I("TART", "Kloosterman refinement in the level variable t for Σ_t D_t^−(tp+1)",
  "Kloosterman's refinement made 4-variable forms work by averaging Kloosterman sums over the Farey denominators. The all-level ES count Σ_t D_t^−(tp+1) is a divisor problem whose Fourier expansion in t produces Kloosterman sums (cf. the Type I Heegner/Kuznetsov note).",
  "Kuznetsov is already used for the Type I sum; applying it to the level sum at fixed p is the pointwise version.",
  "Write Σ_{t≤T} D_t^−(tp+1) via additive characters, identify the Kloosterman sums S(m,n;c), and estimate their contribution using Weil + Kuznetsov for fixed p.",
  ["kloosterman", "kuznetsov", "level-sum"], "med", "big", kw=["Kuznetsov"])
I("DUKE", "Spinor-exceptional square classes as the exact model of T1",
  "For ternary forms the integers t·m² in spinor-exceptional classes are represented by only half the spinor genera (Schulze-Pillot); everything else large is represented. T1 says Type I/II solutions vanish exactly at odd squares — a 'square-class' exception of the same shape.",
  "If an ES certificate family is a ternary representation problem whose spinor exceptions are exactly the odd squares, DSP would give all large non-square p (ineffectively).",
  "Compute spinor-exceptional classes for ternary forms of small discriminant; look for one whose exceptions are {m²} and whose representations of p biject with Type II data.",
  ["spinor-genus", "T1", "ternary-forms"], "med", "medium", kw=["spinor exceptional", "spinor"])
I("DUKE", "Correlate f_I(p), R(p) with class numbers h(−4p), h(−kp)",
  "Duke/Iwaniec: representation numbers of ternary forms ≈ class numbers. If some ES count correlates with h(−kp) for small k, a class-number-sized main term may be hidden in a weighted ES count.",
  "Cheap test of whether ES counts carry class-number information beyond the BM/genus layer.",
  "For primes p ≤ 10⁷, regress R(p)/log²p and f_I(p)/log²p on h(−4p)/√p, h(p)·reg/√p and L(1,(·/p)); report partial correlations.",
  ["class-numbers", "numerics", "correlation"], "high", "cheap")
I("DUKE", "An ineffective 'all large p' theorem is acceptable progress",
  "DSP (via Siegel) is ineffective yet counted as a full upgrade. For ES, an ineffective theorem 'ES(p) for p > p₀ (ineffective)' would already be a first-ever all-large result.",
  "Opens Siegel-type inputs (L(1,χ) ≫ q^{−ε}) that the campaign may have discarded because they are ineffective.",
  "Re-read BM_CORRECTED_COUNT §3 and check where a Siegel lower bound for L(1,(·/p)) or L(1,χ_{−4uB}) could replace Burgess and what it yields.",
  ["ineffective", "siegel", "BM-main-term"], "high", "cheap")
I("LINNIK-ERG", "Linnik with a varying auxiliary split prime: ℓ = least prime with prescribed (p/ℓ)",
  "Linnik's ergodic method needed (−n/ℓ) = 1 for a fixed ℓ; varying ℓ with n is how one covers every n if the method is uniform in ℓ. ES: SYNTHESIS_SPARKS9 shows the BM layer is pointwise free using the least ℓ with (n/ℓ) = −1; find an ℓ-adic dynamical argument for certificates using that ℓ.",
  "Bounded ℓ ≤ 4ℓ(n) is already known to suffice for BM positivity; a dynamical/Hecke argument at that ℓ could control the next layer.",
  "Look for an ℓ-Hecke correspondence on ES certificates (e.g. on the quaternion/SL₂ form: matrices of determinant ℓ acting on [[a,p],[c,d]]) and test whether it maps certificates of p to certificates of p.",
  ["hecke-operators", "ergodic-method", "auxiliary-prime"], "med", "big", seen=["SYNTHESIS_SPARKS9.md"])
I("LINNIK-ERG", "Always-existing objects (CM points / closed geodesics of discriminant tied to p) landing in a target region",
  "Duke's theorem works because Heegner points of discriminant −d always exist (h(−d) ≥ 1) and equidistribute. ES needs existence; find objects attached to every p (e.g. CM points of disc −4p, geodesics of disc p) such that landing in an explicit cusp/congruence region ⟺ an ES certificate.",
  "Equidistribution then forces existence for all large p (possibly ineffectively) — the general almost→every template of Duke/Linnik.",
  "Try: reduced forms [a,b,c] of disc −16p or −4(4Cp+1); check whether 'a ≡ −1 (mod 4C), a small' type conditions encode (★); measure how deep in the cusp the region lies (it may be too deep — the B2 issue).",
  ["equidistribution", "CM-points", "homogeneous-dynamics"], "med", "medium")
I("FIFTEEN", "Escalation of certificate menus: the ES 'truant' tree",
  "Bhargava's escalation: adjoin the smallest truant each time; finitely many escalators. ES: start with a certificate menu (Mordell identities, (★), b=1, ES₅, windows), find the least prime not covered, adjoin the cheapest family covering it, iterate; study the growth of the escalation tree.",
  "Gives an empirical picture of how many families are needed up to X (B1 says bounded menus fail under Hypothesis H — the escalation rate measures how fast menus must grow).",
  "Implement escalation over the repo's family menu up to 10⁸ and plot menu size vs. X.",
  ["escalation", "certificate-menu", "numerics"], "high", "medium", seen=["POINTWISE_SIZE.md"], kw=["escalat"])
I("FIFTEEN", "Per-level explicit thresholds: R_t(n) is exactly a divisor count — make each level's failure set explicit",
  "290 theorem: explicit per-form cusp bounds + finite checks. ES levels have no cusp part (METAPLECTIC Thm K: R_t = D_t^− − β_t), so each level's failure set is an explicit multiplicative condition on tn+1. Compose them escalator-style.",
  "Explicit per-level failure sets turn the menu escalation into a computation on multiplicative sets (thin sets S_t).",
  "For t ≤ 64 describe {n : D_t^−(tn+1) = 0} as 'no sub-multiset product of the prime factors of tn+1 is ≡ −1 mod t' (prime factors in a subgroup avoiding −1 is sufficient but not necessary — e.g. t = 28, N = 141 = 3·47) and compute the densities of intersections.",
  ["explicit", "multiplicative-sets", "levels"], "high", "cheap", seen=["METAPLECTIC_ES.md"])
I("RAMTERN", "Waldspurger-type formula: is some ES deviation a central L-value?",
  "Ono–Soundararajan proved Ramanujan's form under GRH because coefficient² ∝ L(1/2, f⊗χ_n) (Waldspurger), which GRH bounds. ES: look for an ES generating function with a cuspidal component whose p-th coefficient² is a twisted central value.",
  "If such a formula existed, GRH (or subconvexity) would bound the deviation pointwise; METAPLECTIC says level series are Eisenstein + theta quotients, so a cusp form would have to come from a different construction (e.g. products/derivatives).",
  "Decompose products of two level series (or the all-level series) into Eisenstein + cuspidal parts at small level numerically (Sage modular symbols) and look for nonzero cuspidal components.",
  ["waldspurger", "L-values", "GRH"], "low", "medium", kw=["Waldspurger"])
I("RAMTERN", "Sporadic exceptions U(n) = {105, 2961, 3985, 25305, 111969, 978145} vs. Ramanujan's 2719",
  "Ramanujan's form had sporadic exceptions explained by a finite computation + GRH. The finite U(n) exception list might be sporadic in the same sense, or the start of a structured family (a reciprocity family as in Apollonian packings).",
  "Deciding 'sporadic vs structured' tells whether U(n) is a good proxy target for ES.",
  "Factor the U(n) exceptions, compute their residues mod 840 and character values (n/ℓ) for ℓ ≤ 50, and extend the U(n) search to 10⁸ if not already done.",
  ["sporadic-exceptions", "numerics", "reciprocity"], "high", "cheap")
I("HASSE", "Many-variable relaxations: ES with an extra term tied to the others",
  "Hasse principle holds for forms in many variables (Davenport, Heath-Brown, Hooley). 4-term ES is trivial; find intermediate 'k-term ES with constraints' (e.g. 1/x+1/y+1/z+1/w with w forced to equal xyz·k, or two terms merging 1/a+1/b = 1/c) that are circle-method accessible and imply 3-term ES.",
  "Interpolates between trivial (4 free terms) and hard (3 terms); the implication step is the interesting part.",
  "List 4-term constrained families and for each check (i) does a solution give a 3-term solution, (ii) number of variables after eliminating constraints.",
  ["many-variables", "relaxation", "circle-method"], "low", "medium")
I("BHS", "A certificate scheme whose only hard condition is primality of linear forms (Green–Tao–Ziegler unconditional)",
  "Harpaz–Skorobogatov–Wittenberg made Hypothesis-H-conditional fibration arguments unconditional when only linear polynomials must be prime, via Green–Tao–Ziegler. ES: search for a certificate parametrisation where, for fixed p, it suffices that a finite system of linear forms in free auxiliary variables be simultaneously prime.",
  "GTZ would then give infinitely many such auxiliary tuples for each p — an unconditional every-p mechanism. Thm C (bounded witnesses fail under H) does not obviously forbid unbounded prime-based witnesses.",
  "Enumerate ES certificate shapes where a denominator or factor is a free prime (e.g. Type I f prime, window prime q) and check whether remaining conditions can be made linear in auxiliary variables.",
  ["linear-forms-in-primes", "green-tao", "conditional-to-unconditional"], "med", "big", kw=["Hypothesis H"])
I("BHS", "Integral-point fibration on U_n by the curves x = const (two-term problems)",
  "Fibration method for rational points; integral versions exist for some schemes fibred into affine conics (Harpaz, JEMS 2019, conditional on stated hypotheses). Fixing x makes ES a two-term problem 1/y + 1/z = 4/n − 1/x, a divisor problem.",
  "U_n is a log K3-type affine cubic surface (check); an integral fibration method with a BM-type local condition would be a structural every-n mechanism.",
  "Harpaz, 'Integral points on conic log K3 surfaces', JEMS 21 (2019), arXiv:1511.04876 (verified: sufficient conditions under stated arithmetic/geometric hypotheses, not unconditional); check whether U_n fits the framework and which hypotheses fail.",
  ["fibration-method", "integral-points", "log-K3"], "med", "medium", kw=["log K3"])
