from z52b_dividing_lib import C, I

def T(title, conn, why, step, refs=(), tags=(), conf="med", effort="medium"):
    I(f"Transfer: {title}", conn, why, step, refs, ["transfer", *tags], conf, effort)

# ---- Mechanism transfers: a proved-side mechanism aimed at ES ----
T("ES as a Linnik-type problem in the progression 1 mod 4p",
  "For fixed p the auxiliary integers N_C = 4Cp + 1 run through the AP 1 (mod 4p) indexed by C; ES (Type I) asks for an element N_C with a divisor ≡ −1 mod 4C. This is a 'least element of an AP with a factorisation property' question, like Linnik's least prime in an AP.",
  "Linnik-type theorems are pointwise in the modulus 4p (power reservoir of AP elements up to (4p)^L) — but the required class mod 4C moves with C, the B2 feature.",
  "Count, for p ≤ 10^6, the least C with a valid divisor and compare with log² p and with the least prime ≡ 1 mod 4p; check whether 'C ≤ p^ε' always holds.",
  [], ["linnik-constant", "fixed-p-AP", "computation"], effort="cheap")
T("trial-count × success-probability profile", "Classify thin problems by (#trials, success probability per trial): Goldbach (power, 1/log²), p + 2^k (log, 1/log), ES (C ≤ X gives X trials but success ≈ 1/C-ish ⇒ Σ ≈ log² X).",
  "ES has power-many trials but harmonically decaying success: a distinct profile from both 'power reservoir' and 'log trials'. Problems with the same profile and their status would be the right comparison class.",
  "Find other problems with harmonic success profiles: e.g. 'n has a divisor d ≡ −1 mod k for some k ≤ X' (Stewart-type), and check what's known pointwise.",
  [], ["profile", "classification"], effort="cheap")
T("Chen-type switching over the C-variable", "Sieve the linear sequence N_C = 4Cp + 1 (C ≤ X, p fixed) to make N_C a P₂ = q·r; then ES needs q ≡ −1 mod 4C, equivalently r ≡ −1 mod 4C. Switching principle: count pairs via the other factor.",
  "Fixed p, varying C: a one-dimensional linear sieve with level of distribution from Bombieri–Vinogradov-type results for the modulus-varying class condition.",
  "Write the bilinear form Σ_{C} Σ_{qr = 4Cp+1} 1[q ≡ −1 (4C)] and check which equidistribution input (in q over moduli 4C) is needed.",
  [], ["mech:sieve", "mech:chen-switching"], effort="medium")
T("Maynard–Tao tuples of C's", "Choose C ∈ {C₀h₁, …, C₀h_k} admissible and force many N_{C_i} = 4C_i p + 1 to be almost-prime simultaneously, then use the multiplicative relations between them to force a class −1 factor.",
  "Multi-dimensional sieves produce simultaneous structure; ES needs one success among many correlated shifted integers.",
  "Check whether the N_{C_i} with C_i = C₀h_i (fixed p) form an admissible linear tuple in the variable C₀.", [], ["mech:maynard-sieve"], conf="med", effort="medium")
T("Type I through binary quadratic forms of discriminant −4d", "f | 4a²d + 1 = (2a)²d + 1 means f is primitively represented by a form of discriminant −4d; Type I at (a,d) ⟺ p ≡ −f (mod 4ad) for such f. ES becomes a union of genus/class conditions on p modulo 4ad.",
  "Brings class groups and genus theory of Q(√−d) into ES; class-group positivity is a proved-side mechanism.",
  "For d ≤ 50, compute the set of residues −f mod 4ad realised by represented f, and check how quickly the union over (a,d) covers all classes mod lcm (local covering) vs primes.",
  [], ["mech:genus", "binary-forms", "computation"], effort="cheap")
T("Duke equidistribution for represented values", "As d grows, values of forms of discriminant −4d (Heegner-type points) equidistribute (Duke 1988); this might equidistribute the residues −f mod 4ad that Type I offers.",
  "Equidistribution in d at fixed p would give many independent chances; pointwise in p requires equidistribution uniform in a small window of d.",
  "Check the error terms in Duke's theorem vs the window of d needed (d ≤ log^A p).", ["Duke 1988 Invent. Math."], ["mech:equidistribution"], conf="med", effort="medium")
T("Kneser/Olson subset-product theory for gate G4", "Stewart's criterion: a fraction fails 2-term representation iff the prime factors of the relevant integer lie in a subgroup H avoiding −1. Kneser/Olson/Davenport-constant bounds describe when subset products must hit −1.",
  "ES failure ⟺ for every C, all prime factors of the relevant auxiliary integers lie in subgroups H_C ∌ −1 — a simultaneous confinement over many C.",
  "Quantify: for random integers N ≡ 1 mod q, the probability of H-confinement ≈ (log N)^{−(1−1/[G:H])}; multiply over independent C to get the heuristic failure rate; compare with data.",
  ["Pomerance slides 2026 (Stewart; Elsholtz 1998)"], ["mech:subset-product", "gate-G4"], conf="high", effort="cheap")
T("reciprocity across C: simultaneous confinement contradiction", "If all prime factors r of N_C lie in H_C ⊂ (ℤ/4C)^× for many C, then quadratic reciprocity links (q/r) for q | C to (N_C/q) = (1/q) = 1. Try to derive a contradiction from many C simultaneously.",
  "Exactly how T1 arises at squares; at primes, the reciprocity constraints may be insufficient — finding where they stop is informative.",
  "Recheck MODP_RECIPROCITY.md and TWISTED_T1.md for the multi-C version.", ["MODP_RECIPROCITY.md", "TWISTED_T1.md"], ["obst:reciprocity", "seen:MODP_RECIPROCITY.md"], conf="med", effort="cheap")
T("half-dimensional sieve for confined integers", "Integers whose prime factors lie in a subgroup H of (ℤ/q)^× have density ≍ (log x)^{−(1−|H|/φ(q))}; Iwaniec's half-dimensional sieve gives lower bounds for such sets in sequences.",
  "ES failure = simultaneous confinement; sieve UPPER bounds for confinement in the C-aspect at fixed p are the pointwise question.",
  "Formulate the upper-bound sieve problem: #{C ≤ X : N_C is H_C-confined} ≤ ? and see whether the expected X·(log)^{−1/2} type bound is attainable pointwise.",
  [], ["mech:sieve", "confinement"], conf="med", effort="medium")
T("Heath-Brown's 'one of three' trick for Artin → ES families", "Heath-Brown showed one of three multiplicatively independent integers is a primitive root for infinitely many primes using that p − 1 can be made to have few prime factors.",
  "An analogous statement 'one of three fixed ES families solves ES(p) for all p in a set S of positive density' could be the first infinite-structured progress.",
  "Find three ES families whose failure sets intersect only in primes with a special multiplicative structure; test numerically intersection of failures for pairs/triples of small-(a,d) families.",
  ["Heath-Brown 1986"], ["mech:exception-rigidity", "computation"], conf="med", effort="medium")
T("AGP-style construction for a disproof (many primes failing simultaneously)", "AGP build L with many primes q, q−1 | L. Dually, a counterexample search could build p with p ≡ prescribed residues mod many 4ad simultaneously (CRT) — avoiding all Type I APs up to a bound.",
  "Covering-type disproofs fail for ES (failures can't fill an AP), but CRT-constructed 'avoiders' up to a bound X show how many families can be dodged simultaneously; prime in the CRT class then by Linnik.",
  "Compute the density of residue classes mod lcm{4ad : ad ≤ X} avoiding all Type I/II APs; how fast does it decay with X? (Gives an 'avoidance exponent'.)",
  [], ["disproof-route", "mech:CRT", "computation"], conf="high", effort="cheap")
T("Integral Manin heuristics for the ES fibre", "For fixed n the ES equation defines an affine cubic surface; integral-point counting conjectures (Chambert-Loir–Tschinkel; Wilsch, Santens for log Fano) predict (log H)^b growth with a product of local densities as constant.",
  "Gives a principled 'singular series' for R(n): ES fails only if the leading constant vanishes (T1?) or by fluctuation.",
  "Compute the log Kodaira dimension / boundary divisor of the ES fibre and check which integral-point conjectures apply; compare predicted exponent b with the observed log² p.",
  ["Wilsch (integral points log Fano, check)", "Chambert-Loir–Tschinkel 2010"], ["integral-points", "singular-series"], conf="med", effort="medium")
T("hyperbolic lattice-point counting in log-size regions", "Type II solutions are integer points on a quadric-type variety in a region whose volume grows only like log² p; equidistribution theorems (Duke–Rudnick–Sarnak, Eskin–McMullen) need power-size regions.",
  "Explains in a geometric language why ES sits below the 'counting with error term' regime; points to effective equidistribution in small regions as the needed input.",
  "Identify an explicit quadric Q and region R_p with #(Q(ℤ) ∩ R_p) = R_II(p); compute vol(R_p).", ["Duke–Rudnick–Sarnak 1993"], ["mech:lattice-counting", "geometry"], conf="med", effort="medium")
T("Serre thin sets and the image of ES integral points", "The set of n with ES solutions is the image of integral points of the ES threefold under the projection to n. Hilbert irreducibility says images of covers are thin; ES asks the image to be everything.",
  "Positive statements 'image = everything' are proved for maps with sections (identities) — ES has sections on non-square classes only (Mordell–Schinzel).",
  "Phrase Mordell–Schinzel as 'no section over the square classes' and ask whether a multisection of growing degree (growing-level identities) exists.",
  [], ["thin-sets", "growing-level"], conf="med", effort="cheap")
T("Halász / Matomäki–Radziwiłł for confinement indicators", "The indicator that N has all prime factors in H ⊂ (ℤ/q)^× is multiplicative in N; Halász-type theorems give mean values over short intervals / sequences.",
  "Pointwise confinement over the sequence N_C (C ≤ X) is a mean of a multiplicative function along an AP 1 mod 4p — Matomäki–Radziwiłł style results along APs may bound it.",
  "Check whether MR-type results apply to multiplicative functions along APs with modulus as large as 4p and length X ≈ p^θ.", ["Matomäki–Radziwiłł Ann. Math. 2016"], ["mech:multiplicative-functions"], conf="med", effort="medium")
T("Smith's method: ES 'spin' distribution", "Koymans–Milovic and Smith control 2-power class group ranks via bilinear 'spin' sums. ES's Type I success for fixed (a,d) is a Jacobi-symbol-type condition on p; the joint distribution over many (a,d) might be a spin system.",
  "Smith's method proves 100% results when pointwise criteria lack governing fields — exactly ES's apparent situation.",
  "Check whether the indicator of 'p solved by (a,d)' can be written via Jacobi symbols (p/q) for q | 4a²d+1 and how they interact for different (a,d).", ["arXiv:1702.02325"], ["mech:smith-method"], conf="low", effort="big")
T("Heegner points on modular curves X₀(N) with N tied to p", "Look for CM points of discriminant −4p or −p (for p ≡ 1 mod 4 one has Q(√−p)) on a curve mapping to the ES surface.",
  "Heegner constructions give O(1)-count pointwise existence at every prime in a class.", "Determine whether the ES surface over Q is rational (it is a cubic surface with rational points, so likely rational) and look for curves of genus ≥ 1 in it parametrised modularly.",
  [], ["mech:heegner"], conf="low", effort="big")
T("Zagier-style involution on I3 words p = tuv − u − v", "The I3 reformulation gives a finite set of (t,u,v); look for an involution composed of 'flip' moves (u ↔ v, and a windmill-type move) with a unique fixed point.",
  "Windmill involutions prove two squares for p ≡ 1 mod 4 using only a finite set and parity; ES has finite certificate sets too.",
  "Compute #{(t,u,v): tuv − u − v = p, t,u,v ≥ 1 with coordinate in 4ℤ ∪ (8ℤ − p)} mod 2 for p ≡ 1 mod 24 ≤ 10^5.",
  ["WINDMILL.md", "WINDMILL_REDUCTION.md"], ["mech:involution-parity", "seen:WINDMILL.md", "computation"], conf="med", effort="cheap")
T("Davenport-constant zero-sum forcing for G4", "Any sequence of length ≥ D(G) in a finite abelian group has a zero-sum subsequence; analogously, many prime factors in (ℤ/4C)^× force subset products to cover cosets.",
  "If N_C has many prime factors (> D((ℤ/4C)^×)), subset products cover a subgroup coset; ES needs −1 in the generated subgroup, not just zero sums.",
  "Compute ω(N_C) vs log|(ℤ/4C)^×| over C ≤ X for fixed p; Erdős–Kac says ω ≈ log log, too small — record the gap.", [], ["mech:davenport-constant", "gate-G4"], conf="high", effort="cheap")
T("Selberg–Delange / Landau for counting H-confined N_C", "Counts of integers composed of primes in a set of Dirichlet density δ follow Landau–Selberg–Delange ~ c x (log x)^{δ−1}.",
  "Gives the precise heuristic per-C failure probability, the input of ES Poisson models.", "Compute δ_C = |H_C|/φ(4C) maximal over subgroups H_C ∌ −1 (which is 1/2 when −1 ∉ index-2 subgroups) and derive the model.",
  [], ["mech:selberg-delange", "heuristic-model"], conf="high", effort="cheap")
T("Poisson / Janson model calibrated on Schinzel's m/n family", "Use Pomerance–Weingartner's m-family as a training set: fit a model P(no solution | p, m) and extrapolate to m = 4.",
  "A model that correctly predicts exceptions for m = 8..15 (where exceptions exist) and predicts none for m = 4 would be a strong calibrated heuristic.",
  "Implement R_m(p) counting for m ≤ 15 and p ≤ 10^7; fit log P(R=0) against (log p)³/m.", ["arXiv:2511.16817"], ["heuristic-model", "family-crossing-line", "computation"], conf="high", effort="medium")
T("Ergodic 'measure rigidity' for exceptional primes", "EKL show Littlewood exceptions have dimension 0 via measure rigidity of diagonal flows; ES exceptions (if any) might correspond to divergent/escaping orbits in some homogeneous space.",
  "If ES certificates correspond to orbit intersections in a homogeneous space, rigidity could restrict exceptional sets.",
  "Look for a homogeneous dynamics model: e.g. the CF/SL₂ words of ES₅ as visits of a geodesic to a cusp region.", ["Einsiedler–Katok–Lindenstrauss 2006"], ["mech:measure-rigidity"], conf="low", effort="big")
T("Bertrand-style exact extraction from a binomial-type integer", "Find an explicit p-tied integer M(p) (product of many N_C, or a binomial/Gauss-period quantity) whose p-adic/multiplicative structure provably contains a factor in the needed class.",
  "Bertrand's postulate is proved by bounding C(2n,n) from both sides: a thick deterministic object with exact extraction.",
  "Consider M = ∏_{C ≤ X} N_C and compare its size with the maximum possible size of an H_C-confined product: can size alone force escape?",
  [], ["mech:T-thick", "mech:binomial-divisibility"], conf="med", effort="medium")
T("Legendre negative-Pell descent ported to ES", "Legendre: from x² − py² = 1 (x odd) factor (x−1)(x+1) = py² and case-split to obtain x² − py² = −1. For ES: start from a forced identity involving p (e.g. a Pell solution, or p = a² + b²) and case-split its factors into ES certificates.",
  "Uses the only known O(1)-count pointwise mechanism at p ≡ 1 mod 4 that is purely elementary.",
  "Take p = a² + b² (Fermat, forced) and test whether (a,b) give ES certificates via simple formulas for a positive fraction of p; record failures.",
  [], ["mech:descent", "mech:forced-object", "computation"], conf="med", effort="cheap")
T("Two-squares decomposition p = a² + b² as a forced object", "p ≡ 1 mod 4 has a unique a² + b²; check whether 4/p has certificates expressible in a, b (e.g. via (a ± b), a² − b², ab).",
  "If a fixed finite set of polynomial-in-(a,b) formulas solved ES, it would bypass Mordell–Schinzel (those are polynomial in p, not in a,b).",
  "For p ≡ 1 mod 24 ≤ 10^6, test whether some x ∈ {a, b, a+b, a−b, ab, a²−b², …}·small multiples gives 4/p − 1/x a 2-term fraction (Stewart test).",
  [], ["mech:forced-object", "polynomial-in-a-b", "computation"], conf="med", effort="cheap")
T("Gaussian-integer lifting of ES", "Over ℤ[i], p = ππ̄ splits. Write 4/p = 4/(ππ̄) and look for Gaussian-integer representations that descend to rational ones (norms/traces).",
  "Splitting of p ≡ 1 mod 4 is the extra structure available exactly at ES's hard primes.",
  "Search for identities 4/(ππ̄) = Σ 1/ξ_i with ξ_i ∈ ℤ[i] such that conjugate pairs combine into rational unit fractions.", [], ["gaussian", "forced-object"], conf="med", effort="medium")
T("Class number h(−p) / h(−4p) parity as a lever", "For p ≡ 1 mod 4, h(−4p) is even (genus theory); 2-power divisibility depends on representations like p = x² + 32y². Correlate ES certificate shapes with 2-power class group data.",
  "Ties ES to Rédei-type structure where governing-field and Smith methods exist.",
  "Tabulate h(−4p) mod 8 and the minimal ES certificate shape for p ≡ 1 mod 24 ≤ 10^6; look for dependence.", ["BRAINSTORM/bsB_redei_oddpart.md"], ["mech:redei", "computation"], conf="med", effort="cheap")
