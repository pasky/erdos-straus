# Items batch 3: Diophantine, automorphic, spectral, dynamics upgrades.

I("FLT", "Inverse Frey: encode the failure of ES at p as an object with impossible properties",
  "Frey/Ribet/Wiles: a hypothetical solution yields an elliptic curve whose mod-ℓ representation would come from a nonexistent level-2 form. ES failure gives no point, but it gives a huge family of constraints (no divisor of 4Cp+1 is ≡ −1 mod 4C, for all C). Package these constraints as a Galois/automorphic object (e.g. a 'character' on level structures) and seek a rigidity contradiction.",
  "The FLT pattern 'counterexample ⇒ object ⇒ contradiction' is the archetypal every-n proof; ES's failure data are rich enough to define objects.",
  "Formalise the failure data as a function F_p(C, a) = 1[class a mod 4C contains a divisor of 4Cp+1]; check whether ES failure makes F_p multiplicative/character-like in C (it would be in the square-mimicking profinite model).",
  ["frey-curve", "counterexample-structure", "rigidity"], "low", "big")
I("FLT", "Almost-all exponents → all: Faltings-type finiteness for ES failure configurations",
  "Heath-Brown/Granville deduced FLT for almost all exponents from Faltings' finiteness. ES: find a family of curves X_p (genus ≥ 2, or of general type) whose extra rational/integral points are forced by ES failure at p; uniform finiteness would bound the failures.",
  "Moves ES to finiteness of the exceptional set — a big intermediate step (finite exceptions + verification would finish).",
  "Look for curves in the ES surface family U_p (e.g. intersections with x = λy) whose integral points correspond to certificates; compute genera.",
  ["finiteness", "faltings", "curves"], "low", "medium")
I("CAT", "Wieferich-type congruences forced on a hypothetical counterexample",
  "Mihăilescu showed a Catalan solution forces p^{q−1} ≡ 1 (mod q²) — strong congruences on the unknowns. ES: a counterexample p must be a square modulo every M for which bounded certificates cover the non-square classes (Mordell: mod 840). Push the list of forced congruences as far as possible and combine with the least-non-residue bound.",
  "If 'no certificate with parameters ≤ L' forces (p/ℓ) = 1 for all ℓ ≤ L^c, Burgess (n(p) ≪ p^{0.152}) gives a contradiction for L^c > p^{0.152}.",
  "For moduli M = 840·m, compute the residues uncovered by certificates with all parameters ≤ L; test whether they are exactly squares mod M and how L must grow with M.",
  ["forced-congruences", "least-nonresidue", "square-classes"], "high", "medium", seen=["AMPLIFY_EXCEPTION.md"])
I("CAT", "Annihilator theory in (ℤ/4C)*: Stickelberger-type relations among divisor classes",
  "Mihăilescu's proof uses annihilators of cyclotomic class groups. The classes of prime factors of 4Cp+1 in (ℤ/4C)* across many C are linked (the same p); look for annihilator-type relations that prevent all of them from avoiding −1.",
  "Odd: ES failure is a statement about a family of subgroups indexed by C; group-ring relations between the families might be forced by the common p.",
  "Compute for fixed p the vectors (class of q mod 4C) for primes q | 4Cp+1, C ≤ 200, and search for linear relations in the group ring that hold for all p.",
  ["group-ring", "cyclotomic", "odd"], "low", "medium")
I("ZSIG", "Primitive divisors of Lucas sequences are ≡ ±1 (mod n): a source of divisors ≡ −1 (mod 4C)",
  "Primitive prime divisors q of a Lucas number u_n satisfy q ≡ (D/q) (mod n); when (D/q) = −1, q ≡ −1 (mod n) — exactly the class ES needs at level n = 4C. Combine with q | 4Cp+1 (i.e. q = 4Cm − 1 with q | p + m).",
  "A structural source of divisors in the class −1 mod 4C; BHV guarantees primitive divisors for n > 30.",
  "For small D and n = 4C, list primitive divisors q ≡ −1 (mod 4C) of u_n and test how often p + m ≡ 0 (mod q) can be arranged (it cannot for fixed p unless q | p + m; compute the induced density).",
  ["primitive-divisors", "lucas-sequences", "residue-class"], "low", "cheap")
I("ZSIG", "Cyclotomic size argument: 'non-certificate part' of Π_C(4Cp+1) must be small",
  "Bang–Zsigmondy: Φ_n(a) is large but its non-primitive part is tiny (only the largest prime of n), so a primitive prime exists. ES analogue: bound the part of Π_{C≤X}(4Cp+1) made of primes that cannot participate in any certificate, and show it is smaller than the whole.",
  "A size argument needs no equidistribution; it uses only the explicit CRT census of prime factors (cf. Erdős–Bertrand item).",
  "Define 'certificate-capable' primes q (those with 4c_q | (q+1)k-type relations) and compute log of the incapable part vs. Σ log(4Cp+1) for test p.",
  ["size-argument", "cyclotomic", "CRT"], "low", "cheap")
I("ROTH", "Subspace-theorem methods for divisibility relations (Corvaja–Zannier)",
  "Roth → Schmidt's subspace theorem → Corvaja–Zannier results on divisibility a^n − 1 | b^n − 1 and on S-integral points. ES is a divisibility relation (4uC − 1) | (p + u); the subspace theorem controls such relations in exponential/algebraic families.",
  "Could prove finiteness of failures in exponential families (e.g. 15·2^s + 1, 4^s + 297 — open in the repo) or structure results for certificate-free p.",
  "Check Corvaja–Zannier's divisibility theorems (e.g. 'On the greatest prime factor of (ab+1)(ac+1)', 'A lower bound for the height of a rational function at S-unit points') for applicability to n = a·b^s + c families with certificate divisibility.",
  ["subspace-theorem", "divisibility", "exponential-families"], "med", "medium", kw=["Corvaja"])
I("BAKER", "'At most one exception' phase: repulsion between ES-failing primes",
  "Heilbronn–Linfoot/Tatuzawa proved there is at most one exceptional discriminant before the full class-number-one solution. ES intermediate: show two (★)-failing or ES-failing primes p, p′ in a range [X, X²] cannot coexist (repulsion), e.g. because their characters would both be exceptional.",
  "Finiteness/at-most-one statements are the classical stepping stone between almost-all and every.",
  "Check the 14 (★)-failures ≤ 10¹⁰ for pairwise relations (p′/p) = 1, shared quadratic-residue profiles, and spacing; compare with random primes having the same individual profiles.",
  ["repulsion", "exceptional-set", "numerics"], "med", "cheap")
I("PELL", "Dirichlet–Pell pigeonhole on near-certificates in M₂(ℤ)",
  "Pell is solvable for every non-square D by: infinitely many (x,y) with bounded norm defect, two with the same defect k and residues mod k, divide them to get norm 1. ES Type I/II fail exactly at odd squares — the Pell exception shape. In the SL₂ form, look for near-certificate matrices with bounded defect; two congruent ones give a quotient that is an exact certificate.",
  "Pigeonhole + group law is the cleanest every-n mechanism whose only failures are squares; T1 must appear as the reason the quotient fails at squares.",
  "Define defect for matrices [[a,p],[c,d]] (e.g. det = 1 + δ, or a ≡ −1 only mod c/δ); generate many for a given p and test whether quotients of pairs with equal defect yield exact certificates.",
  ["pigeonhole", "pell", "SL2", "T1"], "med", "medium")
I("PELL", "Continued-fraction periodicity vs. ES₅ length: Lagrange's proof structure",
  "Pell's solution comes from the periodic CF of √D. ES₅ ⟺ λ(p) ≤ 3 (a continued-fraction length condition for rationals with denominator p). Look for a quadratic irrational (depending on p) whose CF period contains an ES₅ witness, so periodicity forces existence.",
  "Odd but concrete: links ES₅'s CF-length formulation to the one every-n theorem driven by CF structure.",
  "For p ≤ 10⁵, compute the CF periods of √p, √(4p+1), (1+√p)/2 and check whether an ES₅ witness can be read off from convergents.",
  ["continued-fractions", "ES5", "odd"], "low", "cheap", seen=["BRAINSTORM/farey_ford_cf.md"])
I("CONG", "Explicit Heegner-type constructions for Mordell-hard classes",
  "Congruent numbers: explicit Heegner points give results for primes in specific classes (5, 7 mod 8). ES: find an explicit CM/Heegner construction producing certificates for p in one Mordell-hard class (e.g. p ≡ 1 mod 840 with an extra splitting condition), as a 'Monsky/Heegner' theorem for ES.",
  "Partial class-restricted every-p theorems are new territory for ES and would show which arithmetic the hard classes need.",
  "Re-read paper/es-typei-heegner-note for which objects are used; test numerically whether Type I certificates for p correlate with CM points of disc −p·k.",
  ["heegner", "explicit-construction", "hard-classes"], "low", "big", kw=["Heegner"])
I("CONG", "Smith-type distribution of 'certificate-free levels' in twist families",
  "Smith's method computes distributions of Selmer groups in quadratic-twist families. The set of levels C at which p has no certificate is a 'Selmer-like' local-global object varying with p; its distribution over p could be computed by Smith/Koymans–Pagano-style methods.",
  "Exact distributional knowledge of the failing-level profile is stronger than the zero-law heuristics now used.",
  "Define the profile vector (1[level C fails])_{C ≤ K} and tabulate its empirical distribution over p; compare with a product-of-local-factors model.",
  ["distribution", "selmer-like", "numerics"], "low", "medium")
I("GZK", "Non-vanishing criterion (Gross–Zagier style) for the existence of a certificate",
  "Gross–Zagier: a Heegner point is non-torsion iff L′(E,1) ≠ 0 — existence from an analytic non-vanishing. ES: seek a curve/abelian variety A_p with a canonical point whose non-triviality is equivalent to (or implies) an ES certificate, so that a non-vanishing statement proves ES.",
  "Converts existence into non-vanishing of a special value, where analytic tools work for every member of a family.",
  "Look for elliptic fibrations of the ES surface U_p (e.g. fix x/y = λ) and compute whether the integral points relate to multiples of a canonical point.",
  ["special-values", "heegner", "geometry"], "low", "big")
I("RAM", "Geometric cancellation via trace functions for divisor-class sums",
  "Deligne's Ramanujan bound comes from geometry (purity). The ES deviation involves sums over characters of order ≥ 3 mod 4C of σ_χ(4Cp+1); for prime moduli these are sums of trace functions (Kummer sheaves) where Fouvry–Kowalski–Michel give square-root cancellation in long sums.",
  "If the ES non-genus part X(p) can be written as a sum of trace functions with conductor bounded independently of p, Deligne-type bounds apply pointwise.",
  "Restrict to prime levels 4C → prime e (windows) and write the e-slice certificate count as a trace-function sum over divisors; compute the conductors.",
  ["trace-functions", "deligne", "cancellation"], "low", "medium")
I("WEIL", "Lower bound by upper bounds on complements (Stepanov/Weil principle)",
  "In the elementary proofs of Weil's bound, the lower bound for N comes from upper bounds applied to complementary objects. ES: find a family {R_j(p)} with R_0 = R(p) whose total Σ_j R_j(p) has a pointwise asymptotic and whose other members have sharp pointwise upper bounds; then R(p) ≥ total − Σ_{j≠0} upper bounds.",
  "Upper bounds for divisor counts in fixed classes (Shiu/Brun–Titchmarsh type) are much easier than lower bounds; the total over all classes (τ(4Cp+1) summed over C) has a known asymptotic.",
  "Quantify at small levels (C ≤ 8, where φ(4C) ≤ 16): total τ-sum asymptotic vs. best upper bounds for each wrong class; how sharp must the upper bounds be for R(p) > 0 to follow?",
  ["complement-counting", "upper-bounds", "lower-bounds"], "high", "medium")
I("WEIL", "Lenstra/Coppersmith: divisors in residue classes via lattice reduction for large levels",
  "Lenstra (Math. Comp. 42 (1984)): N has ≤ 11 divisors ≡ r (mod s) when s > N^{1/3}, gcd(r,s) = 1, all found in polynomial time; Coppersmith–Howgrave-Graham–Nagaraj (Math. Comp. 77 (2008)) enumerate constructively for s ≥ N^α, any fixed α > 1/4. For C ≳ p^{1/2}, the modulus 4C exceeds (4Cp+1)^{1/3}, so each level has O(1) candidates computable by lattice reduction.",
  "Turns the large-C part of R(p) into a count of short vectors in an explicit family of lattices — a geometry-of-numbers object where Minkowski-type existence arguments live.",
  "Implement Lenstra's algorithm for (N, r, s) = (4Cp+1, −1, 4C) and test the fraction of certificates with C > p^{1/2}; analyse the lattices as C varies.",
  ["lattice-reduction", "divisors-in-classes", "geometry-of-numbers"], "high", "medium", kw=["Coppersmith"])
I("QUE", "Hecke-type relations between ES counts at p, pℓ, pℓ² (Soundararajan's no-escape-of-mass)",
  "Soundararajan prevented escape of mass using λ(ℓ)² = λ(ℓ²) + 1, which forbids both λ(ℓ) and λ(ℓ²) small. ES: find exact or approximate relations between certificate counts f(p), f(pℓ), f(pℓ²) (solutions for composite n come from p, from ℓ, and 'mixed') that make f(p) = 0 incompatible with the controlled values at pℓ, pℓ².",
  "Multiplicative relations at related integers are a way to get pointwise information from quantities that are easier to bound.",
  "Compute f_II(n) (or R(n)) for n = p, pℓ, pℓ² for p ≤ 10⁵, ℓ ≤ 50, and fit f(pℓ) ≈ a·f(p) + b·f(ℓ) + c·f(p)f(ℓ) + mixed; study the mixed term.",
  ["hecke-relations", "multiplicativity", "numerics"], "med", "cheap")
I("QUE", "Classify limit measures of normalised certificate data along hypothetical failing sequences",
  "QE (density one) comes from a variance bound; QUE (every) from classifying all possible limits (measure rigidity + entropy). ES: attach to each p a normalised measure (levels/shapes of certificates or profinite residue data); show that the only possible limit along any sequence p_k → ∞ is the 'Haar' one, incompatible with R(p_k) = 0.",
  "Shifts from 'bound the variance' (almost all) to 'classify limits' (every) — the exact conceptual step of QUE.",
  "Define μ_p on the profinite completion (or on (ℤ/M)* for growing M) from the residues of p; check what the square-mimicking points of B1 look like as limit measures.",
  ["measure-classification", "limits", "profinite"], "med", "medium")
I("QUE", "Positive entropy from arithmetic recurrence on certificate shapes",
  "Bourgain–Lindenstrauss: Hecke recurrence forces positive entropy, ruling out concentration on small sets. ES: Hecke-like correspondences on certificate shapes (if they exist, cf. LINNIK-ERG item) would force any limiting distribution of shapes to be spread, hence to charge every region with positive mass.",
  "Speculative but it is the precise ingredient that made QUE every-form.",
  "First establish a correspondence (see Hecke-operator item); then measure numerically the entropy of the shape distribution of (★) solutions as p grows.",
  ["entropy", "hecke-operators", "speculative"], "low", "big")
I("HQUE", "Complementary failure sets: two ES methods whose exceptions are incompatible",
  "Holowinsky's and Soundararajan's methods each fail only for forms with atypical eigenvalue statistics, in opposite directions; combined they cover every form. ES: the (★) line and the b=1 line never fail simultaneously ≤ 10⁸; find statistics S_A, S_B such that (★) failure forces S_A(p) extreme and b=1 failure forces S_B(p) extreme in an incompatible way.",
  "A two-method union is an every-p proof template that does not need either method to be pointwise by itself.",
  "Compute a battery of statistics (ℓ(p), T(p), L(1,(·/p)), M_BM, level-failure profile) for the 14 (★)-failures, the 3 b=1 failures and controls; look for anticorrelated pairs.",
  ["complementary-methods", "union-of-routes", "numerics"], "high", "cheap", seen=["B1_LINE.md"])
I("HQUE", "Parametrise ES methods by L(1,(·/p)): one should improve as it grows, another as it shrinks",
  "Holowinsky's bound is in terms of Σ_ℓ (|λ(ℓ)| − 1)/ℓ, Soundararajan's in the opposite tendency. M_BM = M₀ − T(p) is hurt when the weighted sum of (−m/p) is large. Find a second certificate family whose expected count increases with T(p).",
  "If the two main terms move in opposite directions with the same character statistic, their sum is bounded below uniformly — Holowinsky–Soundararajan in miniature.",
  "Compute the expected counts of the b=1 line, windows and ES₅ as functions of the Legendre profile (m/p)_{m ≤ 100}; regress against T(p).",
  ["complementary-methods", "character-bias", "main-terms"], "high", "cheap")
I("SUBCONV", "Amplified second moment over a short family around p",
  "Friedlander–Iwaniec amplification: bound an individual member by a family moment weighted with an amplifier peaked at the target. ES: Σ_{|n−p|≤H} |R(n) − M(n)|²·|A_p(n)|² with A_p(n) = Σ_{ℓ≤L} c_ℓ (n/ℓ)(p/ℓ); if this is ≤ (M(p)|A_p(p)|)²/2, then R(p) > 0.",
  "The bookkeeping (family size H vs amplifier length L ~ H) is not immediately hopeless; the hard input is the twisted second moment of R − M over short intervals.",
  "Numerically evaluate the amplified moment for p ~ 10⁶–10⁷, H ~ 10³–10⁴, Legendre-symbol amplifiers, and compare with the diagonal term.",
  ["amplification", "second-moment", "short-intervals"], "med", "medium", kw=["amplifier"])
I("SUBCONV", "Mollified variance to identify which characters explain R's fluctuations",
  "Mollifiers (Selberg/Levinson/Conrey) dampen large values by a short Dirichlet polynomial. Fit R(n)/M(n) − 1 by a short combination of Legendre symbols (n/ℓ), ℓ ≤ L; the residual variance after mollification measures what remains beyond the genus/BM layer.",
  "Tells whether ES fluctuations are dominated by a few small characters (then a Heilbronn-type split is promising) or are spread out (then they are 'X(p)' noise).",
  "Least-squares fit on n ≤ 10⁷ in Mordell-hard classes; report explained variance as a function of L.",
  ["mollifier", "variance", "numerics"], "high", "cheap")
I("SATO", "Potential ES: count solutions over a quadratic field and use Galois parity",
  "Potential automorphy proves things over extensions and descends via Brauer induction. ES over O_K for real quadratic K: Gal(K/ℚ) acts on K-solutions of 4/p = 1/x+1/y+1/z with totally positive x,y,z; fixed points are ℚ-solutions. If the number of K-solutions in a Galois-stable finite window is odd, a rational solution exists.",
  "Parity across a Galois action is a descent mechanism that needs no analysis over ℚ.",
  "For K = ℚ(√2), ℚ(√5) and small p, enumerate totally positive integral solutions with norms bounded (finite after fixing a fundamental domain for units) and compute the parity of the count of non-rational ones.",
  ["descent", "number-fields", "parity"], "low", "medium")
I("SERREMOD", "Minimal-counterexample descent: failure at p ⇒ failure at a smaller related prime",
  "Khare–Wintenberger: induction on conductor reduces to base cases. ES: find a map Φ such that if ES (or (★)) fails at p then it fails at some smaller Φ(p) (e.g. a prime factor of 4p+1 or of (p+e)/4); with verification to 10¹⁸ this proves ES.",
  "Induction on the size of the counterexample is the cleanest every-n mechanism; data on (★)-failures can test candidate maps directly.",
  "For the 14 (★)-failing primes, check whether any simple arithmetic function of p (prime factors of 4p+1, 8p+1, (p+3)/4, p−4k², …) systematically produces another (★)-failing prime.",
  ["descent", "induction", "numerics"], "med", "cheap")
I("SERREMOD", "Killing ramification: remove small-prime structure from a counterexample",
  "KW lower the level by passing through compatible systems. ES: a counterexample p is a square mod 840; transform the problem (via the e-slice or by passing to n = p·m for auxiliary m) to a 'less ramified' instance where certificates are easier, without losing the failure.",
  "Speculative; but ES(pm) → ES(p) fails in general, so the transfer must use primitive certificates of pm (those not coming from m).",
  "Count primitive (non-inherited) Type II solutions of 4/(pm) for small m and test whether they ever yield information about p's certificates.",
  ["level-lowering", "speculative", "transfer"], "low", "medium")
I("BGEXP", "Product of three sets in SL₂(ℤ): ES words as A·T·A with entry p",
  "Bourgain–Gamburd/Helfgott growth makes products of a few sets fill SL₂(F_q). ES words p = tuv − u − v are length-3 'minus continuants': the (1,1) entry of M(u)M(t)M(v) with M(a) = [[a,−1],[1,0]]. ES ⟺ some product in A·T·A (with t ∈ 4ℤ ∪ (8ℤ − p)) has the right entry.",
  "Places ES in the product-set/growth framework where 'every element' theorems exist (at least modulo q).",
  "Check numerically how the (1,1)-entries of M(u)M(t)M(v), u,v,t ≤ X, distribute modulo small q and whether all residues are hit with the expected frequency (local), then compare with the archimedean count.",
  ["growth", "SL2-words", "product-sets"], "med", "cheap", seen=["BRAINSTORM/thin_group_orbits.md"])
I("BGEXP", "Birational automorphisms of U_n preserving integral points (Markoff-style moves)",
  "Markoff surfaces have Vieta involutions generating a group whose orbits structure all integral points; BGS/Chen then work. ES 4xyz = n(xy+yz+zx) is linear in each variable (no Vieta involution); X = 1/x makes it a plane. Search Bir(U_n) for maps preserving integrality (beyond permutations).",
  "If a nontrivial group acts on integral points of U_n, orbit/strong-approximation methods (and Chen's divisibility) become available.",
  "Compute a few Cremona-type maps of the ES surface (e.g. from the Type I/II parametrisations) and test integrality preservation on known solutions.",
  ["birational-maps", "markoff", "integral-points"], "low", "medium", seen=["MARKOFF_ES.md"])
I("SUMPROD", "Sum-product incompatibility: subgroup-avoidance across windows vs linear structure of N_e = (p+e)/4",
  "Bourgain–Katz–Tao: no set is nearly closed under both + and × in F_p. ES failure at many windows e forces the prime factors of N_e = (p+e)/4 into structured multiplicative sets mod e (e.g. squares when e is prime ≡ 3 mod 4), while N_e varies linearly in e.",
  "If the multiplicative constraints at different e were incompatible with the additive progression N_e, ES would follow; sum-product is the canonical incompatibility principle.",
  "For e prime ≡ 3 (mod 4), record whether all prime factors of N_e are QRs mod e for the hard primes; check how often this 'square-avoidance' happens across e ≤ 10⁴ compared to random.",
  ["sum-product", "windows", "incompatibility"], "med", "cheap", seen=["FORCED_WINDOW.md"])
I("MARKOFF", "Congruences for certificate counts (Chen's divisibility mechanism)",
  "Chen proved Markoff components have size ≡ 0 (mod p), which with BGS's 'giant component' gives connectivity. ES: find a congruence R(p) ≡ r(p) (mod m) (or for a refined count) with r(p) ≠ 0 determined by p's residue class; then the count cannot vanish.",
  "A congruence mod a fixed m is a pointwise statement; R(p) is even, so look at R(p)/2 mod 2, mod 3, or counts weighted by characters.",
  "Compute R(p)/2 mod m and several refined counts mod m (m = 2,3,4,8) for p ≤ 10⁷ and test whether any is determined by p mod M for small M.",
  ["congruences", "parity", "numerics"], "high", "cheap", seen=["BRAINSTORM/y1_reciprocal_parity.md"])
I("MARKOFF", "Graph structure on certificates of a fixed p",
  "BGS/Chen study the connectivity of a graph on solutions. Define moves between ES certificates of the same p (change C keeping u, swap roles of u/B, Type I↔II transforms) and study components; 'one certificate ⇒ many' plus a counting congruence on component sizes might exclude zero.",
  "Even if ES is not about connectivity, component structure can produce congruences (as in Chen).",
  "For p ≤ 10⁶ build the move graph on all ES solutions and record component sizes; look for divisibility patterns.",
  ["graphs", "solutions-structure", "numerics"], "low", "medium")
I("APOLLO", "Search for quartic/higher reciprocity obstructions in ES sub-routes",
  "The Apollonian local-global conjecture failed because of quadratic and quartic reciprocity obstructions removing families like squares times constants. T1 is a quadratic one for Type I/II at odd squares. Test sub-routes ((★), b=1, ES₅, windows) for failure sets along families n = k·m², k·m⁴ and quartic-residue conditions.",
  "Finds hidden structured obstructions before they ambush a proof; for ES itself any such family would be a counterexample candidate.",
  "For each sub-route compute failure rates on n = k m² and n = k m⁴ (k ≤ 50) versus random n of the same size and residue class, and (2/p)₄-type quartic symbols on prime failures.",
  ["reciprocity-obstructions", "apollonian", "numerics"], "high", "cheap", seen=["BRAINSTORM/apollonian_reciprocity.md"])
I("APOLLO", "Almost-all does not imply every: a structured-exception audit for ES",
  "Bourgain–Kontorovich proved density one for Apollonian curvatures, yet infinitely many exceptions exist. ES's almost-all theorems (Vaughan) are compatible with an infinite thin exceptional family; list the families where every known ES mechanism is weakest (odd squares for Type I/II; Mordell-hard classes; large ℓ(p)) and check ES (any type) explicitly far along them.",
  "Disproof-side hygiene: the Apollonian story shows the almost-all→every step can fail exactly through reciprocity.",
  "Extend adversarial searches along n = m² · (small k) and primes with large ℓ(p) beyond 10¹⁸ using the cheapest e-slices.",
  ["disproof-hygiene", "exceptional-families", "adversarial-search"], "high", "medium", seen=["DISPROOF_AVENUES.md"])
I("ZAREMBA", "Modular-Zaremba + size control: words with (1,2)-entry ≡ 0 (mod p) and size < 2p",
  "Moshchevitin–Shkredov solve a modular Zaremba problem by growth in SL₂(F_p). ES words: length-3 minus-continuant products; require the relevant entry ≡ 0 (mod p) and bounded by 2p, forcing equality with p. Equidistribution mod p of entries of words of archimedean size ≤ p is the needed input.",
  "Separates ES into a modular part (growth, potentially 'every p') and a size part (counting words in a box).",
  "Numerically test equidistribution mod p of the entries of length-3 words with entries ≤ p (count ≈ p log p) for p ~ 10⁶; measure deviations at 0 mod p.",
  ["zaremba", "growth", "equidistribution"], "med", "cheap", kw=["Zaremba"])
I("ZAREMBA", "Track full Zaremba as ES's closest structural analogue",
  "Zaremba (bounded partial quotients for every q) is at density one (BK, Huang A=5) but not every q, like ES. Any 'every q' progress for some A (or for structured q like Niederreiter's prime powers) would show what kind of argument crosses that wall.",
  "Shared obstruction profile: thin semigroup, polylog-to-power main terms, density-one results.",
  "Search for post-2020 Zaremba results ('Zaremba conjecture every denominator', Kan, Frolenkov, Shkredov, 2023–2026) and record whether any is 'every q' for some A.",
  ["zaremba", "literature", "analogue"], "high", "cheap", kw=["Zaremba"])
I("ZAREMBA", "Niederreiter's recursive constructions for prime powers → ES exponential families",
  "Niederreiter proved Zaremba for every power of 2, 3, 5 by explicit recursive constructions. The repo proved ES for 3·2^s + 1, 7·4^s + 9, 63·2^s + 1; open: 15·2^s + 1, 4^s + 297. Import the recursive (q → 2q, q → 3q) construction idea: produce certificates at n_{s+1} from those at n_s.",
  "Recursive constructions along exponential families are the only way Zaremba got 'every member' for infinite families.",
  "For 15·2^s + 1, list known certificates for s ≤ 60 and look for a recursion (u,B,C)_s → (u,B,C)_{s+k}.",
  ["recursive-construction", "exponential-families"], "med", "cheap")
I("OPP", "Counting integral points on the quadric ad − pc = 1 (Duke–Rudnick–Sarnak / Eskin–McMullen)",
  "Oppenheim/Margulis and DRS/EM count integral points on affine homogeneous varieties via dynamics. The SL₂ form of ES: integer points of the affine quadric ad − pc = 1 (degenerate as a ternary quadratic polynomial: quadratic part ad of rank 2, linear in c — a family of hyperbolas ad = 1 + pc) with a ≡ d ≡ −1 (mod c), c ∈ 4ℕ, a, d ≥ 1. Decompose by c into congruence-subgroup cosets and count each via mixing.",
  "Homogeneous-dynamics counts are pointwise in the variety (here: in p), unlike sieve averages.",
  "For fixed c, the conditions define a coset of a congruence subgroup; compute the expected count Σ_c vol(coset ∩ region) and compare with R(p).",
  ["homogeneous-dynamics", "quadrics", "counting"], "med", "medium")
I("OPP", "Values of rational quadratic forms with congruence: does ES's (degenerate) quadric relate to the exceptional rational case of EMM?",
  "Eskin–Margulis–Mozes: for irrational forms counts are asymptotic, while rational forms of signature (2,1)/(2,2) have exceptional logarithmic behaviour. ES's quadric ad − pc is rational but degenerate (rank-2 quadratic part, linear in c), so EMM does not apply directly; ask whether a nondegenerate model (e.g. after eliminating c via a ≡ d ≡ −1 mod c) falls in the EMM exceptional regime and whether the log-excess there mirrors the log²p main term.",
  "A dictionary between ES's polylog main term and the known exceptional counts of rational quadrics could import their methods.",
  "Read EMM's treatment of rational forms (Annals 1998) and compute the predicted count for ad − pc ∈ {1} with |a|,|d| ≤ T, c ≤ T.",
  ["oppenheim", "rational-forms", "main-term"], "low", "medium")
I("RATNER", "Closed horocycle at height 1/p: equidistribution of (a + i)/p and cusp excursions",
  "Every closed horocycle of length → ∞ equidistributes (Sarnak/Hejhal; sparse versions by Venkatesh, Strömbergsson). Points (a + i)/p, a mod p, lift ES₅-type continued-fraction data of a/p; ES₅ needs a point whose cusp excursion has a specific deep shape.",
  "Puts ES₅ into the horocycle-equidistribution world where every-p statements exist — but probably at too deep a cusp scale (B2), which this item would quantify.",
  "Translate λ(p) ≤ 3 into a statement on the cusp depth/shape of some (a + i)/p and compare with the scales reachable by effective equidistribution.",
  ["horocycles", "equidistribution", "ES5"], "med", "medium", seen=["LENGTH_THREE.md"])
I("RATNER", "Shrinking-target property for every closed horocycle",
  "Logarithm laws (Kleinbock–Margulis) give deep excursions for almost every orbit; ES would need them for the specific closed horocycle of length p and depth ~ p^{θ}. Tseng (Math. Z. 2022) proves shrinking-cusp-target equidistribution for long closed horocycles (effective version included).",
  "If a deep-excursion theorem for every closed horocycle exists at depth p^{θ}, the CF-length formulation might follow for a range of shapes.",
  "Read Tseng, 'Shrinking target equidistribution of horocycles in cusps', Math. Z. 302 (2022), arXiv:2106.00836, and Kelmer, Israel J. Math. 229 (2019), arXiv:1708.08953 (both verified to exist); extract the deepest cusp target reachable for a closed horocycle of length p.",
  ["shrinking-targets", "horocycles", "literature"], "med", "cheap")
I("WEYL", "Weyl/van der Corput differencing on the exponential-sum form of R(p)",
  "Weyl upgraded to every irrational polynomial by differencing. R(p) = Σ_{u,B} (4uB)⁻¹ Σ_{h mod 4uB} e(h(p+u+B)/(4uB)); apply van der Corput differencing in u (or B) to the nonzero frequencies to extract cancellation for fixed p in smoothed ranges.",
  "Standard tool not obviously tried at fixed p; at least gives the true size of the error term in smoothed (★) counts.",
  "Run the differencing on a smoothed model and compare the predicted error with the numerically observed |R_w(p) − M_w(p)|.",
  ["exponential-sums", "differencing"], "low", "medium")
I("FURST", "Profinite Furstenberg: closed ×k-invariant subsets of Ẑ and the ES-hard set",
  "Furstenberg: every infinite closed ×2,×3-invariant subset of the circle is everything. ES certificate existence is closed under n → kn; the closure in Ẑ (or in the solenoid) of the 'certificate-free' set is invariant under division by units? Formulate the right dynamical system on Ẑ and classify its closed invariant sets.",
  "Odd: a topological rigidity statement on Ẑ could say the profinite hard set is exactly the squares, which is the B1 picture.",
  "Write down the action (ℤ_{>0}, ×) on Ẑ and determine which closed invariant subsets contain the profinite square-mimicking points.",
  ["topological-dynamics", "profinite", "odd"], "low", "medium")
I("SNIRBOUND", "Fake-ES models: same local statistics, almost-all holds, infinitely many failures",
  "Kahane–Katznelson show a.e. results can be sharp for any null set. Build synthetic 'ES-like' problems (random divisor data with ES's congruence statistics, or ES with a perturbed rule) where Vaughan's proof goes through verbatim but failures are infinite; the real proof must use a feature the fakes lack.",
  "Identifies which properties of the integers any ES proof must use — the constructive face of the barrier map.",
  "Construct a random model of 'divisors of 4Cp+1' with independent prime-factor classes, run the almost-all argument, and check what pointwise statement fails.",
  ["model-counterexamples", "barriers", "random-models"], "high", "medium", seen=["POINTWISE_SIZE.md"])
