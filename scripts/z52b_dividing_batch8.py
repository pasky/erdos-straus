from z52b_dividing_lib import I

def P(a, b, diff, side, step, refs=(), tags=(), conf="med", effort="cheap"):
    I(f"Minimal pair: {a} vs {b}", f"{a} vs {b}: they differ essentially in one feature — {diff}. ES's position: {side}",
      "Minimal pairs isolate the feature responsible for crossing the dividing line; each is a precise question about ES.", step, refs,
      ["minimal-pair", *tags], conf, effort)

P("3x+1 (open, almost-all)", "5x+1 (false)", "sign of the random-walk drift", "ES's analogue of drift is the expected count log² p → ∞ (positive 'drift'), on the true side.",
  "Define an ES 'drift': d(p) = log E[R(p)] and check monotone growth in data.", [], ["dynamics"])
P("p + 2^a + 2^b (false i.o., log count)", "p + 2^a + 2^b + 2^c (open, log² count)", "one more logarithm of witnesses",
  "ES has log² — equal to the open member; the pair's resolution is the most informative single calibration.", "See 'Between: Crocker extension' item.", ["Crocker 1971"], ["count:log2", "twin-of-ES"])
P("Hensley alphabet {2,4,6,8,10} (false)", "Zaremba alphabet {1..5} (claimed true)", "a congruence obstruction from the alphabet; both have δ > 1/2",
  "ES has no local obstruction at primes (only T1 at squares), so sides with Zaremba on this axis.", "None.", ["Bourgain–Kontorovich 2014"], ["obst:congruence"])
P("m/n, m large, p ≈ exp(m^{1/3}) (mostly false)", "m = 4 (ES, open, verified 10^18)", "expected count (log p)³/m crossing 1",
  "ES sits far on the large-count side for every p ≥ 2; the transition is a pure count transition with no arithmetic obstruction.", "See PW calibration items.", ["arXiv:2511.16817"], ["family-crossing-line", "egyptian"], conf="high")
P("Fermat two squares at p ≡ 1 mod 4 (proved, count 1)", "ES at p ≡ 1 mod 4 (open, count log²)", "rigid algebraic structure (Gaussian integers, involution) vs none",
  "Larger count but no structure: the dividing line is structure, not count.", "Look for any ring R with p splitting such that ES certificates are norms/traces from R.", [], ["mech:R-rigidity"], conf="high")
P("Conjecture H at non-squares (open)", "Conjecture H at squares (false, algebraic)", "algebraic factorisation at squares",
  "ES matches: T1 at odd squares (reciprocity) vs open elsewhere; the non-square side is open in both.", "None.", [], ["T1-analogue"], conf="high")
P("ternary forms outside spinor exceptions (proved for large n)", "spinor-exceptional square classes (fail)", "spinor norm obstruction",
  "ES's T1 at squares parallels the spinor exceptions; the 'proved for large n' side uses modular forms (half-integral weight) that ES lacks.", "Search for a half-integral weight form attached to ES counts (theta-type).", [], ["T1-analogue", "mech:modular-forms"])
P("Markoff mod p (proved)", "Markoff integral Hasse for k (false i.o.)", "finite field (strong approximation + orbit divisibility) vs integers with reduction theory",
  "ES is trivially solvable mod every prime power (no local obstruction) — the integral side is everything, as for Markoff k.", "None.", [], ["integral-points"], conf="high")
P("negative Pell at primes p ≡ 1 mod 4 (proved pointwise)", "negative Pell at general d (density only)", "number of prime factors of d (rigidity when d prime)",
  "ES is a prime-target problem; does primality of the target simplify anything as in Legendre? (For ES composite n are easy instead.)", "Note the reversed difficulty: for ES composites are easy. Ask for any problem where primes are hardest yet proved.", [], ["mech:descent"])
P("k = 2 Egyptian (classified by Stewart)", "k = 3 Egyptian (ES, open)", "one more unit fraction: from a single divisor-class condition to a union over a 2-parameter family",
  "The k = 2 criterion is the gate; ES is a union of k = 2 gates.", "See 'k=2 reduction' feature item.", ["Pomerance slides 2026"], ["egyptian", "k=2-reduction"], conf="high")
P("Apollonian (false: reciprocity)", "Zaremba (claimed true)", "reciprocity obstructions present vs absent (for the standard alphabet)",
  "ES: reciprocity obstruction present at squares only.", "None.", ["arXiv:2307.02749"], ["obst:reciprocity"])
P("Goldbach (open, power count)", "ternary Goldbach (proved, power count)", "number of variables (2 vs 3) in circle method",
  "ES has 3 variables but one equation of degree 3 with tiny count — circle method irrelevant.", "None.", [], ["mech:circle-method"], conf="high")
P("p + 2^k (false, periodic witnesses)", "ES (open, non-periodic witnesses)", "periodicity of witness parameter mod fixed moduli",
  "ES is protected from covering-type failure.", "State/prove the 'no covering failure' lemma in general form.", [], ["obst:covering", "protective"], conf="high")
P("Artin conjecture (conditional)", "existence of a primitive root (proved)", "fixed base a vs free choice of base",
  "ES has free choice of certificate parameters (like free base), which suggests existence should be easier than an Artin-type fixed-witness statement.", "Quantify how much freedom ES has: number of 'independent' parameters vs constraint count.", [], ["free-choice"])
P("Ramanujan's form x²+y²+10z² (finite exceptions, GRH)", "x²+y²+z² (proved by genus)", "class number of the genus > 1 (spinor genus not a single class)",
  "ES has no class-number parametrisation at all; closer to the harder member.", "None.", [], ["mech:genus"])
P("Romanoff (positive density, O(1) count)", "Vaughan ES (almost all, log² count)", "count size O(1) vs log²",
  "Growing count upgrades positive density to almost all; does it upgrade almost all to all? (Answer for log count: no — Crocker.)", "None.", [], ["count:log2"], conf="high")

def F(feature, has, supply, why, first_step, refs=(), tags=(), conf="med", effort="medium"):
    I(f"Feature: {feature}", f"Dividing-line feature '{feature}'. ES {has}. To supply it one could: {supply}",
      why, first_step, refs, ["feature", *tags], conf, effort)

F("universal-torsor parametrisation of the ES surface", "HAS parametrisations (Type I/II, I3 words) that look like torsor parametrisations, not yet identified as such",
  "identify the Type I/II parametrisation with the universal torsor of the cubic surface 4xyz = n(xy+yz+zx) (Colliot-Thélène–Sansuc descent); torsor methods (Derenthal, Heath-Brown) count points via lattice counting on torsors",
  "Manin-conjecture proofs for del Pezzo surfaces pass through universal torsors; identifying ES's parametrisation with a torsor imports that toolbox (and its limits).",
  "Compute the Picard group/lines of the ES cubic surface over Q̄ and Q, and compare the torsor equations with the Type I variables (a, d, f, …).",
  [], ["mech:universal-torsor", "integral-points"], conf="med")
F("singular series bounded below on the target set", "UNKNOWN: an ES local-density product S(p) is not standardly defined; T1 suggests S vanishes on certificate lines at squares",
  "define S(n) as the Euler product of local solution densities of the ES fibre with positivity region; show S(p) ≫ 1 for primes",
  "Every proved pointwise asymptotic (Goldbach-ternary, Waring) needs the singular series bounded below; failures (Conj H at squares) are where it vanishes.",
  "Compute local densities of 4xyz = n(xy+yz+zx) mod q^k for small q and n = p vs n = m²; check whether the product distinguishes squares.",
  [], ["singular-series", "computation"], conf="med", effort="cheap")
F("variance / second moment control", "KNOWN on average (Elsholtz–Tao moments)",
  "use the second moment Σ_p R(p)² with Cauchy–Schwarz pointwise in short families (primes in a residue class mod a large modulus)",
  "Romanoff-type and almost-all results come from second moments; pointwise needs higher moments or rigidity.", "Read Elsholtz–Tao's moment computations; check whether higher moments (k-th) are computed.",
  ["Elsholtz–Tao J. Aust. Math. Soc. 2013"], ["mech:second-moment"], conf="high", effort="cheap")
F("symmetry group of the solution set", "HAS only S₃ (permutations) and scaling n ↦ kn",
  "look for hidden symmetries: Cremona/Geiser involutions of the cubic surface that preserve positivity on some subsets",
  "Markoff (Vieta group), Pell (unit group), two squares (involutions) all exploit large symmetry groups.",
  "Compute birational automorphisms of the ES cubic surface defined over Q (Geiser involutions through rational points) and test whether they map positive integral solutions to integral ones for some pairs.",
  ["UNIT_ORBIT_ES.md"], ["symmetry", "seen:UNIT_ORBIT_ES.md", "computation"], conf="med", effort="medium")
F("uniformity in an auxiliary large parameter", "PARTIAL (PW uniform-in-m Vaughan bound)",
  "introduce an artificial large parameter (m, or modulus Q of restricted classes) where uniform results give pointwise results at a special point",
  "Function-field large-q results and PW's uniformity show how an extra parameter can be leveraged.", "Ask: is ES(p) implied by a uniform-in-m statement for m/(kp) with k varying (scaling ES(n) ⇒ ES(kn))?", ["arXiv:2511.16817"], ["uniformity"], conf="med")
F("deterministic witness of fixed algebraic form (identity in p)", "LACKS at square classes (Mordell–Schinzel)",
  "allow identities in auxiliary forced quantities (two-squares decomposition a, b of p; continued fraction of √p) rather than in p itself",
  "Mordell–Schinzel only forbids polynomial identities in n; identities in other p-determined quantities are not covered.",
  "Run a small symbolic search: rational-function identities 4/(a²+b²) = Σ 1/X_i(a,b) with X_i polynomials (with sign/positivity conditions on regions).",
  [], ["polynomial-in-a-b", "mech:polynomial-identity", "computation"], conf="med", effort="cheap")
F("structure of the exceptional set at composite n", "ES at composites reduces to prime factors (trivial)",
  "use the fact that U(n)-type variants have sporadic composite failures (105 = 3·5·7, …) to locate which sub-certificate families matter",
  "Composite sporadic failures of variants show which certificate families are 'load-bearing'.", "Factor U(n) sporadic list and check whether each prime factor's variant certificates are 'incompatible' under scaling.", [], ["sporadic"], conf="med", effort="cheap")
F("multiple disjoint certificate 'regimes' by size (x near p/4 vs x near p)", "HAS distinct size regimes (Type I: one denominator divisible by p; Type II: two)",
  "treat regimes as independent experiments and prove an anti-correlation (if small-x regime fails then large-x regime succeeds)",
  "Dichotomy arguments need two regimes with complementary failure conditions.", "Compute regime-wise counts for p ≤ 10^7 and their correlation.", [], ["dichotomy", "type-I-II", "computation"], conf="med", effort="cheap")
F("p-adic / archimedean transition (local densities at ∞)", "positivity region is bounded (finitely many positive solutions)",
  "view the positive solutions as integral points in a compact region of a non-compact surface; volume of region ~ log² p (matches count)",
  "Counting in bounded regions with volume → ∞ slowly is the generic 'small count' regime; proofs require effective equidistribution at log scale.", "Compute the volume of the positivity region in Haar/log measure and compare with R(p) on average.", [], ["archimedean", "computation"], conf="med", effort="cheap")
F("hereditary consistency across scales (ES(p) solutions at p shape solutions at p·k)", "HAS trivial scaling",
  "seek non-trivial 'lifting' from n = pq to p, i.e. a solution for 4/(pq) which is not a scaled 4/p solution, giving info about p",
  "Non-trivial composite information might feed back to primes via descent.", "Count non-scaled solutions of 4/(pq) and test whether their existence correlates with R(p).", [], ["mech:descent"], conf="low", effort="cheap")
F("fixed-point-free action ⇒ even count", "UNKNOWN", "if a natural involution on solutions of 4/p has fixed points exactly at special solutions, R(p) parity encodes existence of special solutions",
  "Parity-of-count arguments are the cheapest pointwise mechanism (Zagier).", "Compute R(p) mod 2 for ordered/unordered triples and correlate with existence of solutions with x = y or y = z.", ["INVOLUTION_ES.md"], ["mech:involution-parity", "computation"], conf="med", effort="cheap")
F("strong cancellation in a fixed-target character sum (Rickards–Stange)", "LACKS (fibre size log²)",
  "replace the fibre over p by a larger fibre over a p-dependent family (e.g. all n = p·k, k ≤ K) of size power, then extract p",
  "The only proved 'squares + sporadic' theorem uses a long character sum over one target's fibre.", "Count solutions of 4/(pk) over k ≤ K that do NOT come from scaling — is that fibre power-size and does it carry p-information?", [], ["mech:character-sum", "reservoir"], conf="med")

# ---- Meta / process items ----
I("Meta: build the dividing-line table as a feature matrix and fit a decision tree",
  "Encode each catalog problem by features (count order, obstruction type, witness type, rigidity, reservoir, periodic parameter, symmetry group) and outcome; fit a tiny decision tree and see where ES lands and which feature flips it.",
  "A crude but systematic way to read off the dividing line from data; the splits are candidate 'missing features'.",
  "Export catalog tags from data/z52b/dividing.jsonl to a CSV, hand-correct features, fit sklearn DecisionTreeClassifier with depth ≤ 3.",
  ["data/z52b/dividing.jsonl"], ["meta", "computation"], "med", "cheap")
I("Meta: 'witness profile' taxonomy (trials × success × correlation × structure)",
  "Classify all small-count existence problems by four numbers: log #trials, typical success probability, correlation strength between trials, and presence of algebraic structure. Plot proved/false/open.",
  "Moves the dividing-line discussion from anecdotes to a 4-dimensional chart; ES's coordinates can be measured empirically.",
  "Measure ES's correlation strength between certificate families empirically (pairwise covariance) — the unknown coordinate.", [], ["meta", "profile"], "med", "medium")
I("Meta: search Guy's UPINT D11 and Erdős problems site for unit-fraction problems with known 'dividing' resolutions",
  "Erdős problems database (erdosproblems.com) lists many unit-fraction problems, some recently resolved; each resolution mechanism is a data point for the dividing line.",
  "Recent AI-assisted resolutions are concentrated in abundance regimes; listing which unit-fraction problems remain open sharpens the line.",
  "Scrape erdosproblems.com tag 'unit fractions' and record status + mechanism for each.", ["https://www.erdosproblems.com"], ["meta", "egyptian", "literature"], "high", "cheap")
I("Meta: catalogue of 'verified to 10^N, then false' small-count conjectures",
  "Collect conjectures with small expected counts that failed only at large N (Pólya 9·10^8, Mertens, Skewes, Euler sum of powers) and compare their count regimes with ES.",
  "All large-first-counterexample examples are oscillation/structure-driven, not count-driven; ES verification to 10^18 is strong evidence against random-type failures but not structural ones.",
  "Tabulate (expected count at first failure, mechanism) for each; check whether any count-driven conjecture failed beyond 10^9.", [], ["meta", "calibration-numerics"], "high", "cheap")
I("Meta: Poisson model predicts largest exception for each m — test at m = 4 by 'virtual exceptions'",
  "Under the PW Poisson model P(fail) ≈ exp(−(log p)³/m · κ), compute the expected number of exceptions beyond 10^18 for m = 4: if astronomically small, ES's verification is 'model-complete'.",
  "Clarifies what verification to 10^18 means under the best available model.",
  "Fit κ from m = 8..15 exception data, compute Σ_{p > 10^18} P(fail) for m = 4.", ["arXiv:2511.16817"], ["meta", "heuristic-model", "computation"], "high", "cheap")
