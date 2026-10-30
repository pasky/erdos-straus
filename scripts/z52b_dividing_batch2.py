from z52b_dividing_lib import C, I

# ---- Catalog part 2: Egyptian fractions, continued fractions, thin orbits ----
C("m/n = 1/x + 1/y (two unit fractions; Stewart 1964 criterion)", "O(d(n)) — tiny", "local+multiplicative: needs coprime divisors a,b of n with m | a+b",
  "fully characterised; for fixed m almost all n work, asymptotic for exceptions (Elsholtz 1998, Huang–Vaughan 2011); 4/p never works for p ≡ 1 mod 4",
  "divisor criterion: exceptions = n whose prime factors lie in a subgroup of (ℤ/m)^× avoiding −1",
  "The k = 2 analogue of ES is completely understood: failure ⟺ prime factors in a subgroup avoiding −1. ES's E1/E2 events are this criterion applied to p-tied auxiliary integers.",
  "Recast ES as: ∃ auxiliary integer N(p, params) whose prime factors are NOT confined to a subgroup avoiding −1 mod 4C; list which subgroups are forced at squares (T1).",
  ["Pomerance slides 2026 (math.dartmouth.edu/~carlp/esconjfl.pdf)", "Stewart 1964", "Huang–Vaughan 2011"],
  ["outcome:classified", "count:O(1)", "obst:subgroup-avoiding--1", "mech:divisor-criterion", "egyptian"])
C("Schinzel: m/n = 1/x+1/y+1/z for n > N_m (fixed m ≥ 4)", "≍ (log p)³/m at primes (Pomerance–Weingartner heuristic)",
  "none local for large n", "open for every m ≥ 4; Pomerance–Weingartner: N_m ≥ exp(m^{1/3−ε}) (most primes near exp(m^{1/3−ε}) fail)",
  "Brun–Titchmarsh upper bound on Type I/II solvable primes when count (log p)³/m ≪ 1; Poisson heuristic predicts transition to 'always' at p ≈ exp(m^{1/2+o(1)})",
  "Gives a one-parameter family crossing the dividing line: m/p moves from 'mostly false' to 'always true' as p grows; ES is m = 4 at the 'always' end. Very direct calibration.",
  "Compute for m = 8..40 the largest exceptional prime up to 10^9 and fit log N_m vs log m (prediction exponent 1/2); does m = 4's empirical margin match?",
  ["arXiv:2511.16817 (Pomerance–Weingartner)", "Pomerance slides 2026"],
  ["outcome:open", "count:log3/m", "egyptian", "family-crossing-line", "mech:Brun-Titchmarsh", "seen:BRAINSTORM/ident_numerators.md"], effort="medium")
C("Sierpiński 5/n = 1/x+1/y+1/z", "≍ log² n (same as ES)", "none", "open; verified to 10^18 (Pomerance–Weingartner)", "covering congruences except quadratic-residue classes",
  "Sibling of ES; same dividing-line position.", "None new (repo has sibling studies).", ["Pomerance slides 2026"],
  ["outcome:open", "count:log2", "egyptian", "seen:SIBLING.md"])
C("Vaughan almost-all for m/n (exceptions ≪ N exp(−c(m) log^{2/3} N))", "log²", "none", "proved almost all; Pomerance–Weingartner: c(m) = c/φ(m)^{1/3} uniformly for m ≤ log² N",
  "large sieve over many independent Type I/II congruence families", "The almost-all mechanism; uniformity in m is new and quantifies how the almost-all exponent degrades with m.",
  "Read PW's uniform version; check whether its proof gives an explicit c for m = 4 and whether it can be pushed to short intervals around a prime.",
  ["arXiv:2511.16817", "Vaughan 1970 Mathematika"], ["outcome:almost-all", "count:log2", "mech:large-sieve", "egyptian"])
C("Graham 1963: every n > 77 is a sum of distinct integers with Σ1/a_i = 1", "power (huge)", "none", "proved; 77 is the last exception",
  "constructive induction (doubling/splitting identities)", "Egyptian-fraction 'every n beyond a threshold' proved by an inductive constructive scheme because the count is enormous.",
  "Check whether a Graham-style induction (n ↦ 2n+c) has an ES analogue on p via families p ↦ f(p) preserving solvability.",
  ["Graham, Pacific J. Math 1963 (check)"], ["outcome:finite-exceptions", "count:power", "mech:induction", "egyptian"], conf="med")
C("Erdős–Graham colouring conjecture (monochromatic Σ1/x = 1)", "power", "none", "proved (Croot 2003)", "Fourier/smooth numbers",
  "Density/colouring versions of unit-fraction problems are provable (abundance); control.", "None.", ["Croot, Ann. Math. 2003"],
  ["outcome:proved-all", "count:power", "egyptian", "mech:fourier"])
C("Bloom: positive-density sets contain S with Σ_{n∈S} 1/n = 1", "power", "none", "proved (Bloom 2021)", "Fourier analysis on unit fractions",
  "Control: abundance regime.", "None.", ["Bloom arXiv:2112.03726"], ["outcome:proved-all", "egyptian", "mech:fourier"])
C("Odd greedy algorithm termination for x/y with y odd", "unclear", "none", "open", "none", "Algorithmic Egyptian question near ES.",
  "None.", [], ["outcome:open", "egyptian", "algorithmic"], conf="med")
C("Zaremba: every q has a/q with partial quotients ≤ 5", "≍ q^{2δ_5 − 1} (power)", "none", "claimed proved (Zhang 2605.02518v2, unrefereed); Bourgain–Kontorovich almost all (A = 50)",
  "thin-orbit expansion in SL₂(ℤ/q); alphabet size tunes the count", "ES₅ is a CF-length-3 question; Zaremba's count is a tunable power, ES's is fixed log².",
  "None new.", ["arXiv:2605.02518", "Bourgain–Kontorovich Ann. Math. 2014"], ["outcome:claimed-all", "count:power", "mech:expansion", "seen:ZAREMBA_TRANSFER.md"])
C("Hensley's conjecture (δ_A > 1/2 ⇒ almost all q)", "q^{2δ_A − 1}", "congruence obstruction for A = {2,4,6,8,10}", "false as stated (Bourgain–Kontorovich); corrected forms open",
  "local obstruction mod small moduli", "Count crossing 1 at δ_A = 1/2 is the exact dividing line for power-count orbits; ES sits at count log², i.e. 'δ = 1/2 + logarithmic'.",
  "Find an alphabet A with δ_A = 1/2 (critical) and look at what is known: is ES₅ a 'critical-exponent' thin orbit problem?",
  ["Bourgain–Kontorovich, Ann. Math. 180 (2014)"], ["outcome:false-as-stated", "obst:congruence", "critical-exponent", "seen:BRAINSTORM/z31_zaremba_thin_orbits.md"], effort="medium")
C("Rickards–Stange: CF reciprocity obstructions (squares missing)", "power", "reciprocity (quadratic/quartic) excludes squares", "proved: squares + finitely many sporadic for a fat orbit (Thm 2.8)",
  "long character sum over a fibre", "The only proved 'squares + sporadic' theorem; template for ES's (T1 + U(n) sporadic) shape.",
  "None new (repo).", ["Rickards–Stange"], ["outcome:proved-squares+sporadic", "obst:reciprocity", "T1-analogue", "seen:ES_APPROACH_GENERATORS.md"])
C("Apollonian local–global conjecture", "≍ n^{δ−1}·… (power, δ ≈ 1.3057)", "quadratic and quartic reciprocity obstructions",
  "false (Haag–Kertzer–Rickards–Stange 2023); density one (Bourgain–Kontorovich)",
  "reciprocity obstructions on curvatures in certain residue classes", "Power-count problem killed by reciprocity: ES's T1 at squares is reciprocity-type; HKRS shows reciprocity can kill entire infinite families.",
  "Check: do HKRS-type reciprocity obstructions for ES produce anything beyond odd squares (e.g. n = k·m² families)? Test numerically for n = 3m², 5m², 7m².",
  ["arXiv:2307.02749"], ["outcome:false-io", "count:power", "obst:reciprocity", "T1-analogue", "seen:BRAINSTORM/apollonian_reciprocity.md"])
C("Niederreiter: a/2^k, a/3^k, a/5^k with partial quotients ≤ 3 (5)", "power", "none", "proved for these prime-power moduli", "explicit construction / folding lemma",
  "Thin-count pointwise along special moduli via explicit folding — (R)-type construction; ES at special primes (e.g. p tied to powers) might be constructible.",
  "Check whether a folding-lemma-style construction produces ES₅ words for p in special families (e.g. p = 2^k·a + 1).",
  ["Niederreiter 1986 Monatsh. Math."], ["outcome:proved-special", "mech:folding", "mech:R-rigidity"], conf="med")
C("Korobov/Niederreiter: every q has a with partial quotients ≪ log q", "power", "none", "proved", "counting (averaging over a)", "Control.", "None.", [], ["outcome:proved-all", "count:power", "mech:counting"])
C("McMullen: real quadratic fields with infinitely many bounded-type periodic CF", "—", "none", "open in general (known for some fields)", "dynamics/arithmetic",
  "Bounded-type CF existence in prescribed fields — pointwise-in-field question.", "None.", [], ["outcome:open", "continued-fractions"], conf="med")
C("Littlewood conjecture", "—", "none", "open; exceptions have Hausdorff dim 0 (Einsiedler–Katok–Lindenstrauss)", "measure rigidity",
  "'Exceptions of dimension 0' is a strong thin-exception result via rigidity; ES's exceptional set analogue would be 'zero density with structure'.",
  "None.", ["Einsiedler–Katok–Lindenstrauss Ann. Math. 2006"], ["outcome:almost-all-strong", "mech:measure-rigidity"])
C("Duffin–Schaeffer", "—", "none", "proved (Koukoulopoulos–Maynard 2020)", "GCD graphs, compression", "Almost-everywhere statements via combinatorial structure.",
  "None.", ["arXiv:1907.04593"], ["outcome:proved", "mech:gcd-graphs"])
C("Flea orbits (Alkauskas) missing squares", "power (≈ X^0.31 multiplicity)", "provably misses squares", "five further sporadic values ≤ 10^12; completeness open",
  "algebraic invariant forbidding squares", "Same 'squares + sporadic' shape as U(n).", "None new.", ["arXiv:2508.05347"],
  ["outcome:open-sporadic", "T1-analogue", "seen:ES_APPROACH_GENERATORS.md"])

# ---- Catalog part 3: rational points, Heegner, class groups ----
C("Congruent numbers: primes p ≡ 5,7 mod 8 are congruent", "rank-1 Heegner point: 1 generator", "root number",
  "proved for every such prime (Heegner, Monsky; Tian extends to many n)", "Heegner points / modular parametrisation",
  "Pointwise existence of a rational point at every prime in a residue class via an explicit construction (R). ES is also 'every prime in class' but integral/positive.",
  "Ask: is there an auxiliary curve E_p whose Heegner point would produce an ES certificate (e.g. via a map from E_p to the ES surface)?",
  ["Monsky 1990", "Tian 2014 Camb. J. Math."], ["outcome:proved-classes", "count:O(1)", "mech:heegner", "mech:R-rigidity", "rational-points"], effort="big")
C("Congruent numbers n ≡ 5,6,7 mod 8 (all) — Smith distribution", "rank parity", "root number forces odd rank",
  "100% of n ≡ 5,6,7 mod 8 (Smith); all such n conditional on BSD", "Selmer group distribution (Smith's method) + parity",
  "'Parity forces existence' is a powerful pointwise mechanism (rank odd ⇒ point exists, given finiteness of Sha). ES has no parity-forced object known.",
  "Look for an elliptic curve or Selmer-type group attached to p whose rank parity is forced by p ≡ 1 mod 4 and which maps to ES solutions.",
  ["Smith arXiv:1702.02325", "Tunnell 1983"], ["outcome:density-100", "mech:root-number-parity", "mech:selmer"], effort="big")
C("Sylvester: primes p ≡ 4,7,8 mod 9 are sums of two rational cubes", "rank 1 expected", "root number", "partial (Satgé; check Dasgupta–Voight for p ≡ 4,7 mod 9 under a cubic-residue condition)",
  "Heegner/mock-Heegner points", "Another 'every prime in class' via Heegner-type points.",
  "Check the exact hypotheses of Dasgupta–Voight 'Sylvester's problem and mock Heegner points'.", ["Dasgupta–Voight (check)"],
  ["outcome:partial", "mech:heegner", "rational-points"], conf="med", effort="medium")
C("Gauss class number one (Heegner–Baker–Stark)", "finite list", "—", "proved", "modular functions / transcendence",
  "Finite exceptional lists proved via deep rigidity.", "None.", [], ["outcome:proved-finite", "mech:transcendence"])
C("Euler's idoneal (convenient) numbers", "65 known", "—", "list complete except possibly one more (Weinberger; complete under GRH)", "Siegel ineffectivity",
  "'Finite sporadic list + at most one ineffective extra' — exact template for what a U(n)-sporadic theorem could look like.",
  "Check whether ES-type sporadic lists (U(n)) could be governed by a class-number-type quantity of small discriminants.",
  ["Weinberger 1973"], ["outcome:finite-up-to-one", "mech:siegel-ineffective", "sporadic"])
C("Ramanujan–Nagell 2^n − 7 = x²", "finite", "—", "proved (5 solutions)", "arithmetic of Q(√−7)", "Control (R).", "None.", [], ["outcome:proved-finite", "mech:R-rigidity"])
C("Thue equations F(x,y) = m", "finite", "—", "proved finite (Thue), effective (Baker)", "Diophantine approximation", "Control.", "None.", [], ["outcome:proved-finite", "mech:baker"])
C("Bilu–Hanrot–Voutier: primitive divisors of Lucas/Lehmer terms n > 30", "≥ 1 per term", "—", "proved for all n > 30",
  "Baker linear forms + computation + cyclotomic factorisation", "Pointwise existence of a prime with prescribed property in a thin integer: closest (R) analogue to 'divisor of 4Cp+1 in a class'.",
  "Try: a primitive divisor of a cyclotomic-type value Φ_k(p) or of a Lucas term tied to p satisfies a congruence (≡ 1 mod k): can it be steered to −1 mod 4C?",
  ["Bilu–Hanrot–Voutier, Crelle 2001"], ["outcome:proved-all", "count:O(1)", "mech:cyclotomic", "mech:zsigmondy", "divisor-in-class"], effort="medium")
C("Zsigmondy/Bang: a^n − b^n has a primitive prime divisor (n ≠ 6 etc.)", "≥ 1", "—", "proved", "cyclotomic polynomial Φ_n and its factor structure",
  "Forced divisors lie in class 1 mod n — cyclotomic structure forces divisor classes. ES needs class −1 mod 4C.",
  "Look for a polynomial Ψ(p) whose prime divisors are forced ≡ −1 mod something (e.g. Lucas sequences with negative discriminant give ±1 mod n).",
  [], ["outcome:proved-all", "mech:zsigmondy", "divisor-in-class"])
C("Primitive divisors of elliptic divisibility sequences", "≥ 1 per term beyond a bound", "—", "proved for many cases (Silverman; Ingram et al.)", "heights",
  "Divisor existence via height growth: another forced-divisor mechanism.", "None.", [], ["outcome:partial", "mech:heights", "divisor-in-class"], conf="med")
C("Every prime has a Wieferich-type property?", "—", "—", "open both ways", "none", "Control (expected counts log log).", "None.", [], ["outcome:open", "count:loglog"], conf="med")
C("Hilbert's 10th problem / Matiyasevich", "—", "—", "no algorithm in general", "Diophantine sets", "ES is Π₁; any proof must be non-search.", "None.", [], ["logic", "outcome:undecidable-general"])

# ---- Catalog part 4: dynamics / probabilistic / combinatorial ----
C("Collatz (3x+1)", "random-walk drift −log(4/3) per step", "none", "open; Tao 2019: almost all orbits attain almost bounded values (log density)", "Syracuse random variable, entropy/characteristic function",
  "Prime example of pointwise statement with no obstruction and only 'almost all' proved.", "None.", ["arXiv:1909.03562"], ["outcome:almost-all", "mech:random-walk", "dynamics"])
C("5x+1 problem", "positive drift", "—", "false (divergent orbits expected; cycles exist)", "drift sign",
  "Same problem shape with a parameter flipped crosses the dividing line — like m/n for large m.", "None.", [], ["outcome:false-io", "dynamics", "family-crossing-line"], conf="med")
C("Erdős thin basis: ∃ B with r_B(n) ≍ log n for all n", "≍ log n (constructed)", "—", "proved (Erdős 1956) by probabilistic method; order k by Erdős–Tetali 1990",
  "random construction + Chernoff + Borel–Cantelli: log n is exactly the threshold where all-n succeeds",
  "Expected count log n is the probabilistic threshold for 'all n'; ES has log² p, safely above it — random models say ES true; the gap is derandomisation.",
  "Write the 'ES random model': Poisson(c log² p) per p ⇒ P(fail) = p^{−c log p}; compute c from data and compare to Elsholtz–Tao.",
  ["Erdős 1956", "Erdős–Tetali 1990"], ["outcome:proved-exists", "count:log", "mech:probabilistic", "derandomisation"])
C("Erdős–Turán conjecture (r_B(n) ≥ 1 ∀ n ⇒ unbounded)", "—", "—", "open", "none", "Says log-scale thin bases cannot be too thin; ES witness counts are unbounded — consistent.", "None.", [], ["outcome:open"], conf="med")
C("Erdős's ternary conjecture: 2^n has a digit 2 in base 3 for n > 8", "Σ (2/3)^{c n} finite expected failures", "—", "open (Lagarias partial)", "none",
  "Finitely-many-expected-witness non-existence open; analogue of 'finite sporadic list'.", "None.", ["Lagarias 2009"], ["outcome:open", "count:zero"])
C("Every n is a sum of three palindromes (base ≥ 5)", "power-ish", "none", "proved (Cilleruelo–Luca–Baxter)", "explicit digit-by-digit carry algorithm with case analysis",
  "Constructive case analysis proves a pointwise statement; ES case analysis on residues is finite-covering-impossible (B1), but digit-level (unbounded) case analysis is not covered by B1.",
  "Try a 'digit-recursive' ES construction: base-b expansion of p drives the choice of C, digit by digit — check whether B1 excludes it.",
  ["arXiv:1602.06208"], ["outcome:proved-all", "mech:constructive-algorithm", "unbounded-case-analysis"], effort="medium")
C("Chevalley–Warning / Erdős–Ginzburg–Ziv", "count ≡ 0 mod p", "—", "proved", "polynomial method: number of zeros divisible by p",
  "Existence from a divisibility of counts (≥ 1 since trivial zero exists). ES over F_p is trivial, but a 'count mod something' over ℤ could force solutions.",
  "Look for a natural finite set of ES-adjacent objects whose cardinality is provably odd / ≢ 0 mod ℓ and whose non-trivial elements are certificates.",
  [], ["outcome:proved-all", "mech:count-divisibility", "mech:polynomial-method"])
C("Combinatorial Nullstellensatz (Alon) / Cauchy–Davenport", "—", "—", "proved", "polynomial method", "Same family as above.", "None.", [], ["outcome:proved-all", "mech:polynomial-method"])
C("Thue's lemma: x ≡ ay mod p with |x|,|y| ≤ √p", "≥ 1", "—", "proved", "pigeonhole", "Pigeonhole proves O(1)-count statements (two squares). ES has pigeonhole reformulations (LONGSHOT_PIGEONHOLE.md).", "None new.",
  [], ["outcome:proved-all", "mech:pigeonhole", "seen:LONGSHOT_PIGEONHOLE.md"])
C("Minkowski convex body theorem", "≥ 1 lattice point", "—", "proved", "volume", "Geometry-of-numbers existence; ES lattice reformulations exist (BALANCED_LATTICE.md).", "None.", [], ["outcome:proved-all", "mech:geometry-of-numbers", "seen:BALANCED_LATTICE.md"])
C("Odd covering problem (Erdős–Selfridge)", "—", "—", "open; Hough 2015 bounded minimum modulus; squarefree-odd case settled (check Balister et al.)", "distortion method",
  "Limits of covering systems — relevant to which failure mechanisms are available.", "None.", ["Hough Ann. Math. 2015"], ["outcome:open", "mech:covering-system", "meta"])
C("Carmichael's totient conjecture (φ(x) = m never has exactly one solution)", "multiplicity", "—", "open; Ford: every k ≥ 2 occurs as a multiplicity", "sieve + structure",
  "Multiplicity-1 non-existence; counts of preimages — ES counts R(p) might have forbidden values too.", "Check the distribution of R(p) values (unordered solutions) for forbidden small values (e.g. is R(p) = 1 ever attained?).",
  ["Ford Ann. Math. 1999"], ["outcome:open", "mech:sieve"], conf="med")
C("Twin primes / bounded gaps (Zhang, Maynard)", "x/log² x", "parity", "open; bounded gaps proved", "GPY/Maynard sieve", "Control.", "None.", [], ["outcome:open", "count:power", "obst:parity"])
C("Landau: n² + 1 prime infinitely often", "√x/log x", "parity", "open; Iwaniec P₂", "half-dimensional sieve", "Control.", "None.", [], ["outcome:open", "obst:parity"])
C("Friedlander–Iwaniec x² + y⁴ primes", "x^{3/4}/log x", "parity overcome", "proved", "bilinear forms + asymptotic sieve", "Control (family-level).", "None.", ["arXiv:math/9811185"], ["outcome:proved", "mech:asymptotic-sieve", "seen:BRAINSTORM/z52_lit_thin_pointwise.md"])
C("Maynard: primes with a missing digit", "x^{…}", "none", "proved", "Fourier + sieve on digit sets", "Control.", "None.", [], ["outcome:proved", "mech:fourier"])
C("Mauduit–Rivat: Thue–Morse/digit sum on primes", "—", "none", "proved", "Fourier carries", "Control.", "None.", [], ["outcome:proved"], conf="high")
C("Euler's sum of powers conjecture", "—", "—", "false (Lander–Parkin 1966 fifth powers; Elkies 1988 fourth powers)", "computer search / elliptic curve construction",
  "False conjecture with small counts — failure found by geometry (Elkies used an elliptic fibration). Disproof route for ES: a rational/elliptic family hitting a gap.",
  "Check whether ES's surface has elliptic fibrations whose integral-point structure could predict a counterexample region (cf. DISPROOF_AVENUES.md).",
  ["Elkies Math. Comp. 1988"], ["outcome:false", "mech:elliptic-fibration", "disproof-route", "seen:DISPROOF_AVENUES.md"])
C("Pólya conjecture (L(n) ≤ 0)", "—", "—", "false, first counterexample 906150257 (Tanaka 1980)", "zeta zeros (Haselgrove)",
  "Large first counterexample: numerics to 10^18 cannot decide statements driven by oscillation; ES numerics have a different (count) nature.",
  "Quantify: for ES, what model predicts first counterexample size if any? Poisson model gives none beyond tiny p.", [], ["outcome:false", "calibration-numerics"])
C("Mertens conjecture", "—", "—", "false (Odlyzko–te Riele 1985), no explicit counterexample", "zeta zeros", "Same calibration.", "None.", [], ["outcome:false", "calibration-numerics"])
C("Perfect cuboid", "0 expected?", "—", "open", "none", "Control.", "None.", [], ["outcome:open", "count:zero"], conf="high")
C("Lehmer τ(n) ≠ 0", "—", "—", "open", "none", "Control.", "None.", [], ["outcome:open"], conf="high")
C("abc conjecture", "—", "—", "open (Mochizuki claim disputed)", "—", "Many finiteness statements reduce to it; not ES-direct.", "None.", [], ["outcome:open"], conf="high")
C("Erdős–Moser 1^k + … + (m−1)^k = m^k", "0", "—", "open; partial (Moree)", "congruences", "Control.", "None.", [], ["outcome:open", "count:zero"], conf="med")
C("Twin primes in F_q[T] (Sawin–Shusterman)", "q^n/n²", "—", "proved for q large vs constants", "large-q limit + étale cohomology / Möbius cancellation",
  "Function-field large-q proofs exist for statements open over ℤ; ES over F_q[T] has proved variants.",
  "Compare with repo FUNCTIONFIELD_ES*.md: does a large-q limit prove a ES-strength statement there?", ["arXiv:1808.04001"],
  ["outcome:proved-ff", "mech:large-q", "function-field", "seen:FUNCTIONFIELD_ES.md"])
C("Artin's conjecture over function fields (Bilharz)", "—", "—", "proved", "RH for curves (Weil)", "Function-field version proved via RH; number field needs GRH.", "None.", [], ["outcome:proved-ff", "mech:RH-curves", "function-field"])
