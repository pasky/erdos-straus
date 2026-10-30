from z52b_dividing_lib import C, I

# ---- Catalog part 7: count-scale extremes ----
C("n = p + k! (prime plus factorial)", "≍ (log n/log log n)·(1/log n) → 0", "none", "density zero of representable n (expected count → 0); not a theorem I verified",
  "count tends to zero", "Extreme of the count axis: below O(1) existence fails generically — anchors the bottom of the dividing scale.",
  "Check whether a density-zero theorem for p + k! is in the literature (search 'sum of a prime and a factorial').", [], ["count:to-zero", "outcome:density-zero?"], conf="med")
C("n = p + x³ (prime plus cube)", "≍ n^{1/3}/log n", "local mod small primes; algebraic at cubes (n = m³: m³ − x³ factors)", "open; almost-all expected",
  "—", "Same as Conjecture H with cubes: algebraic factorisation at perfect cubes — another 'T1-like' algebraic exceptional family.",
  "None.", [], ["outcome:open", "count:power", "obst:algebraic-at-powers", "T1-analogue"], conf="high")
C("n = 2^a·3^b + p (prime plus 3-smooth)", "≍ log n (#3-smooth ≤ n ≈ log²n/2 log2 log3) × 1/log n ≈ log n", "covering possible (periodic orbits of 2^a3^b)",
  "unknown to me (check)", "—", "Log-count with periodic two-parameter witnesses; covering may or may not be available in two parameters — informative for the covering mechanism's reach.",
  "Search for coverings that kill all n − 2^a3^b; compute exceptions ≤ 10^8.", [], ["count:log", "obst:covering?", "computation"], conf="med", effort="cheap")
C("Every odd n > 1 = p + 2q² (q prime?) / Sun-type mixed sums", "power/log mixes", "various", "mostly conjectural (Sun's lists)", "—",
  "Z.-W. Sun's mixed-sum conjectures supply dozens of small-count problems with numerics; a systematic table of them by count order is a dividing-line dataset.",
  "Mine arXiv:0901.3075 for conjectures with log or log² expected counts and record their numerical exception lists.", ["arXiv:0901.3075"], ["dataset", "count:log"], conf="high", effort="cheap")
C("Erdős: 4/n with x, y, z ≤ C·n²? (size of ES solutions)", "log² (all solutions have max ≤ n²·const)", "—", "known size bounds (all positive solutions are ≪ n²)", "elementary",
  "Size bounds make ES a bounded search per n, so 'least witness' questions are well-posed.", "None.", [], ["egyptian", "size-restriction"], conf="med")

# ---- More connections ----
def X(title, conn, why, step, refs=(), tags=(), conf="med", effort="medium"):
    I(title, conn, why, step, refs, tags, conf, effort)

X("Greedy set-cover growth of primes by ES certificate families",
  "Order Type I/II families (by modulus) and compute the minimum number of families needed to cover all primes ≡ 1 mod 24 up to x. Finite coverings are impossible (B1); the growth rate (log x? log² x?) measures 'how infinite' ES's covering is.",
  "Compare with covering systems (finite) and with p + 2^k (no covering of the complement). A slow (≈ log x) growth would suggest a structured infinite covering.",
  "Implement greedy set cover over families with modulus ≤ M for primes ≤ 10^7; plot cover size vs x.",
  [], ["dual-covering", "computation"], "high", "cheap")
X("AP-avoidance density: CRT classes dodging all Type I families with ad ≤ X",
  "Compute the density δ(X) of residue classes (coprime, ≡ 1 mod 24) that avoid every Type I AP −f mod 4ad with ad ≤ X. ES ⇔ no prime survives all X; the decay rate of δ(X) is the 'covering strength'.",
  "If δ(X) decays like exp(−c log² X) it matches Vaughan's exceptional set; slower decay would leave room for many CRT-constructed near-counterexamples.",
  "Monte Carlo over random large residues, X = 10..2000; fit log δ vs log X.", [], ["disproof-route", "computation", "dual-covering"], "high", "cheap")
X("Sieve-limit (parity-type) model for ES",
  "Selberg's parity example shows sieves cannot distinguish primes from integers with λ(n) = −1. Ask for an analogue: a set S with the sieve statistics of primes (level of distribution, local densities) on which every ES certificate family fails — odd squares are such a set for certificate lines (T1).",
  "If such a model exists, sieve-only proofs of ES are impossible; if the statistics of primes already exclude it, a sieve route exists.",
  "Try S = {n : n ≡ 1 mod 24, n = m² or m²·(unit-like)} and generalisations; check which sieve axioms each candidate violates.",
  ["T1_TEMPLATE.md"], ["parity", "T1-analogue", "barrier-model"], "med", "medium")
X("Proof-complexity status of ES as a Π₁ sentence",
  "ES is Π₁; known natural Π₁ statements unprovable in PA are consistency-type. No 'small-count number theory' Π₁ statement is known to be independent of PA.",
  "Situates ES on the logic side of the dividing line: proved/disproved small-count statements are all provable in weak systems (e.g. EFA) — does any known proof of a small-count pointwise theorem need strong axioms?",
  "Literature check: 'Π1 sentences number theory independence natural' (Friedman's work) — is any Diophantine-existence-for-all-n statement known independent?",
  [], ["logic", "meta"], "med", "cheap")
X("Kubilius-type probabilistic model of R(p) as a sum of weakly dependent indicators",
  "R(p) = Σ_{families} 1[p ∈ AP(family)]; Kubilius models replace dependence by independence across moduli. The model's prediction for P(R(p) = 0) is exp(−(1+o(1))·E R(p)) if dependence is weak.",
  "Formal backbone for the 'log² ⇒ true' heuristic; the dividing line is the dependence structure.",
  "Fit the empirical distribution of R(p)/E[R(p)] for p ≡ 1 mod 24 and compare to Poisson; repo LOWER_TAIL memos have related data.",
  ["LOWER_TAIL_ASTRA.md"], ["heuristic-model", "seen:LOWER_TAIL_ASTRA.md"], "high", "cheap")
X("Turán–Kubilius / Erdős–Kac for the number of certificate families hitting p",
  "If the number of hitting families behaves like ω(n) (Erdős–Kac normal with mean and variance log²-scale), the lower tail would be Gaussian-small, not Poisson-small.",
  "Distinguishes two heuristic regimes with very different exceptional-set predictions.",
  "Compute mean and variance of R(p) in windows; compare variance/mean ratio to 1 (Poisson) vs ≫ 1 (overdispersion).", [], ["heuristic-model", "computation"], "med", "cheap")
X("ES as a 'prime covering' dual to Sierpiński: an explicit infinite system that must cover all primes",
  "Sierpiński numbers are k such that a finite covering hits every k·2^n + 1; ES is the claim that an infinite AP system {−f mod 4ad} hits every prime. Both are covering statements, one about a sequence, one about primes.",
  "Unifies the failure mechanism of p + 2^k with the success claim of ES: covering theory is the common language.",
  "Survey: are there theorems that an infinite family of APs with divergent Σ1/modulus and a 'genericity' condition covers all primes (or all integers) except an explicit set?", [], ["dual-covering", "literature"], "med", "cheap")
X("Erdős–Selfridge 'covering with distinct moduli and divergent density' analogue for primes",
  "Known covering results bound minimum modulus (Hough) and handle densities; the ES system has distinct moduli 4ad with multiplicities. Ask for a 'prime covering lemma' with explicit hypotheses.",
  "Would give a structural theorem in which ES is an instance — even a conditional one.", "Read Balister–Bollobás–Morris–Sahasrabudhe–Tiba 'distortion method' and see if it bounds uncovered primes for infinite systems.",
  ["Hough 2015"], ["dual-covering", "mech:distortion-method"], "med", "medium")
X("ES certificate as small solution of a congruence: lattice/Thue reformulation with p fixed",
  "For fixed (a, k), Type I asks f | 4a²d+1 with 4ad | p+f: equivalently a pair of congruences in (d, f) — a 2-dim lattice problem modulo p-dependent moduli, solvable by Thue's lemma when moduli and bounds balance.",
  "Thue-type pigeonhole proves O(1)-count statements; the obstruction is the divisibility (not congruence) condition f | 4a²d+1.",
  "Check LONGSHOT_PIGEONHOLE.md and BALANCED_LATTICE.md for this exact form.", ["LONGSHOT_PIGEONHOLE.md", "BALANCED_LATTICE.md"], ["mech:pigeonhole", "seen:BALANCED_LATTICE.md"], "med", "cheap")
X("ES and Romanoff-type 'positive lower density for restricted families' as a stepping stone",
  "Prove: for a fixed finite set of certificate families, the set of primes they solve has positive relative density in the hard classes (trivially true by Dirichlet). The interesting stepping stone is 'density → 1 as family set grows, with an explicit rate' (Vaughan-type).",
  "Clarifies which partial results are new vs trivial.", "None; tag as a calibration.", [], ["calibration"], "high", "cheap")
X("Arithmetic statistics of 'ES-failing residue systems' (Cohen–Lenstra style)",
  "Model the subgroups H_C ∌ −1 confining N_C's factors as random subgroups; Cohen–Lenstra-type weights might give the right probabilities for simultaneous confinement.",
  "Arithmetic statistics heuristics with correct weights often predict exceptional sets accurately (e.g. Stevenhagen's negative Pell).",
  "Compute the empirical distribution of the subgroup generated by N_C's prime factors in (ℤ/4C)^× for fixed small C over many p.", [], ["heuristic-model", "cohen-lenstra", "computation"], "med", "cheap")
X("Stevenhagen-type conjecture for ES: exact density of p solved by families with modulus ≤ M",
  "Stevenhagen predicted the negative-Pell density via a Markov chain on 2-ranks, later proved (Koymans–Pagano). For ES, a Markov-chain model over growing family sets could predict exact densities at finite M.",
  "Exact finite-M densities are provable (Chebotarev); comparing them with a model checks the model's dependence structure.",
  "Compute exact densities of primes solved by families with 4ad ≤ M for M ≤ 200 (finite CRT computation) and fit decay of the unsolved density.",
  ["arXiv:2201.13424"], ["heuristic-model", "computation"], "med", "cheap")
X("Analogy with Lehmer's question for unit fractions: smallest positive value of 4/p − 1/x − 1/y − 1/z",
  "If ES fails at p, the closest approach |4/p − Σ 1/x_i| > 0 is bounded below by 1/(pxyz). Study the 'Egyptian approximation gap' distribution; ES ⇔ gap = 0 is attained.",
  "Converts existence into a Diophantine-approximation statement where Baker/geometry-of-numbers tools might bite.",
  "Compute, for p ≤ 10^5, the minimal positive gap and the number of near-solutions with gap ≤ 1/(p·xyz)·K.", [], ["diophantine-approximation", "computation"], "med", "cheap")
X("Unit fractions in function fields of characteristic 2/3 as 'bad characteristic' analogues",
  "ES over F_q[T] with q even or q ≡ 0 mod 3 changes the role of 4 and 3; failures there would localise the arithmetic role of 4 = 2².",
  "Bad-characteristic behaviour often reveals which primes in the statement carry structure.", "Check FUNCTIONFIELD_ES*.md for char 2/3 results; if absent, small brute force over F_2[T], F_3[T].",
  ["FUNCTIONFIELD_ES.md"], ["function-field", "computation"], "med", "cheap")
X("ES over ℤ[1/S] (S-integral ES)",
  "Allow denominators in ℤ[1/S] — i.e. x, y, z rationals with S-unit denominators. For S ∋ 2 or 3 does ES become provable for all p via identities?",
  "Moving between integral and rational points one prime at a time locates the integrality obstruction.",
  "Find the smallest S for which a polynomial identity covers all p ≡ 1 mod 24 with x, y, z ∈ ℤ[1/S] positive.", [], ["integral-points", "S-integral"], "med", "cheap")
X("Archimedean variant: 4/p = 1/x + 1/y + 1/z with x, y, z ∈ ℤ allowing one negative denominator",
  "With one negative denominator the problem changes count regime (infinitely many solutions?) and becomes identity-solvable; the dividing line between 'all positive' and 'one negative' measures the positivity cost.",
  "Isolates positivity as the obstacle (feature item 'positivity as the whole content').",
  "Find explicit identities for 4/p = 1/x + 1/y − 1/z valid for all p; check known literature (it is classical that signed versions are easy).", [], ["archimedean", "positivity"], "high", "cheap")
X("Expander-free 'thin' structure: ES₅ words as length-3 paths in the Farey graph",
  "ES₅ ⟺ λ(p) ≤ 3: a short path in the Farey/Stern–Brocot graph between specific vertices. Graph distance ≤ 3 problems in growing graphs with no expansion argument.",
  "Diameter/short-path existence results in arithmetic graphs (e.g. Cayley graphs of SL₂(ℤ/p)) are proved by expansion only at log diameter, not fixed length.",
  "See BRAINSTORM/bsA_farey_graph_metric.md.", ["BRAINSTORM/bsA_farey_graph_metric.md"], ["continued-fractions", "seen:BRAINSTORM/bsA_farey_graph_metric.md"], "med", "cheap")
X("Fixed-length words in SL₂(ℤ): Waring problem for SL₂ / word maps",
  "Every element of SL₂(ℤ/p) is a product of ≤ 3 (or bounded) elements of a given type (Waring for word maps; Larsen–Shalev). ES₅ is a fixed-length word condition in SL₂(ℤ) with integrality.",
  "Bounded-width results in finite groups are proved by character theory (Frobenius formula) — a 'thick' count over the group — but ES needs integral lifts.",
  "Check whether the ES₅ word count over SL₂(ℤ/N) is given by a Frobenius character formula and whether lifting to ℤ is the only gap.",
  ["Larsen–Shalev (word maps, check)"], ["word-maps", "mech:character-theory"], "med", "medium")
X("Bounded generation of SL₂(ℤ[1/p]) / elementary matrices (Carter–Keller, Vsemirnov)",
  "Bounded generation results (every matrix a product of ≤ N elementary matrices) are pointwise for every element, proved by arithmetic (Dirichlet's theorem) — closest to 'fixed-length word exists for every target'.",
  "ES₅ is an existence of a fixed-length word; bounded generation proofs use primes in APs to steer entries.",
  "Read Vsemirnov / Morgan–Rapinchuk–Sury on bounded generation of SL₂(ℤ[1/p]) and compare the word shape with ES₅'s.",
  ["Morgan–Rapinchuk–Sury 2018 (check)"], ["word-maps", "mech:dirichlet-steering"], "med", "medium")
X("Dirichlet-steering constructions: use primes in APs to steer a certificate",
  "Bounded-generation proofs choose an auxiliary prime q in an AP to make entries coprime/divisible as needed. For ES, choose a prime q ≡ 3 mod 4 dividing a p-tied integer (Obláth: q | p + 1) — steering requires q to divide something specific, not just lie in an AP.",
  "Clarifies the gap: steering works when the auxiliary object is free (any prime in an AP), not when it must divide a fixed integer.",
  "List ES certificate constructions where the auxiliary prime can be chosen freely in an AP (if any exist, they would prove ES).", [], ["mech:dirichlet-steering", "free-choice"], "med", "cheap")
X("Erdős–Graham problem on 4/n with distinct denominators all ≤ n^{1+ε}?",
  "Bounding the largest denominator changes count; there might be literature on 'Egyptian fractions with small denominators' (Erdős–Graham book) for 4/n specifically.",
  "A family where the count is tunable by the size bound.", "Check Erdős–Graham 'Old and new problems' section on unit fractions for size-bounded ES variants.",
  [], ["egyptian", "size-restriction", "literature"], "med", "cheap")
X("Thick object: the multiplicative group (ℤ/pℤ)^× and its subgroup lattice",
  "ES certificates for p correspond to residues of p modulo many 4ad, but one could also look mod p: x ≡ ? mod p. The set {x : 4x ≡ … mod p} is 'thick' (size p); extraction rule: lift to ℤ with size constraints.",
  "Generator-matrix item (thick object × extraction rule): (ℤ/p)^× as thick object with an archimedean extraction rule.",
  "Write ES Type II as a condition on a residue mod p plus a size bound and check whether the residue set has structure (subgroup/coset).", ["ES_APPROACH_GENERATORS.md"], ["mech:T-thick"], "med", "cheap")
X("Bourgain–Gamburd–Sarnak style 'strong approximation + giant component' for a hypothetical ES group",
  "If any infinite group acted on signed integral ES solutions (as Vieta on Markoff), BGS-type results mod p plus a 'giant component' argument could transfer.",
  "Markoff integral points are controlled by this exact mechanism; ES lacks the group — finding one would be a structural breakthrough.",
  "Check whether the signed ES surface 4xyz = n(xy+yz+zx) has an infinite group of polynomial automorphisms (likely not; record the proof).", [], ["symmetry", "mech:strong-approximation"], "med", "cheap")
X("Lower bounds for exceptional sets: can one prove ES's exceptional set (if nonempty) is infinite?",
  "For p + 2^k, failures come in APs (infinite). For ES, scaling preserves solvability only downward; an ES counterexample p need not imply others. Ask: does one failing prime force infinitely many failing integers (yes: none — ES(kp) can hold via other factors)?",
  "Structure of potential exceptional sets clarifies disproof shapes (single sporadic vs infinite families).",
  "Prove/disprove: if ES fails at prime p then it fails at p^k (probably false/irrelevant since 4/p^k = (1/p^{k-1})·4/p … check directions).", [], ["exception-shape"], "med", "cheap")
X("Correlation with Mordell's quadratic-residue classes: strength of 'residual' structure among hard primes",
  "Mordell's classes are exactly p that are squares mod 840 — the T1 shadow. Within these, does R(p) correlate with further quadratic-residue conditions (mod 11, 13, …)?",
  "If the hard primes get progressively harder with more QR conditions, T1's shadow is the governing structure; ES failure would need p to be a QR mod 'everything' (impossible for a non-square), suggesting a proof route via 'p non-square ⇒ some character escapes'.",
  "Compute mean R(p)/log² p for p in hard classes split by (p/11), (p/13), (p/17), (p/19).", [], ["T1-analogue", "computation", "QR-shadow"], "high", "cheap")
X("'p is not a square' as the only input: character-escape lemma",
  "Since T1 kills certificate lines exactly at squares, and a non-square p is a non-residue modulo some prime ℓ ≤ ℓ(p) (least non-residue-type bound), look for a certificate family that is activated precisely by (p/ℓ) = −1.",
  "Turns ES into a least-non-residue problem (pointwise under GRH with polylog ℓ, Burgess unconditionally) if each ℓ has a family activated by (p/ℓ) = −1 that always works.",
  "For each small prime ℓ, list certificate families whose solvability condition is implied by (p/ℓ) = −1 alone — known to fail? (repo F6 'sign layer is easy'; class layer is the problem). Record where it breaks.",
  ["BRAINSTORM/z31_small_count_pointwise.md"], ["mech:character-escape", "T1-analogue", "least-witness"], "med", "cheap")
