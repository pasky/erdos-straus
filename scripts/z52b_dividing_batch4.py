from z52b_dividing_lib import C, I

# ---- Catalog part 5: local–global failures, rational/integral points, Egyptian extras ----
C("Grunwald–Wang special case (16 is an 8th power locally almost everywhere, not globally)", "—",
  "a 2-adic special case of the local–global principle for powers", "proved: the principle holds except the explicit special case",
  "cyclotomic Z/2^k structure at 2", "Exceptional local–global failures confined to one explicit special family — like T1 at squares; a theorem with 'everything but the special case' is the model shape.",
  "Ask whether ES's T1 can be phrased as a Grunwald–Wang-type special case of a general principle for 'class-avoiding divisor' problems.",
  [], ["outcome:proved-with-special-case", "obst:special-case", "T1-analogue"], conf="med")
C("Selmer's cubic 3x³ + 4y³ + 5z³ = 0", "0 rational points", "Sha / Brauer–Manin on the curve", "proved Hasse failure", "descent",
  "Classical local–global failure with nothing local wrong; ES has no BM obstruction (Bright–Loughran), so failures would have to be non-BM (integral/positivity).",
  "None.", [], ["outcome:false", "obst:sha", "local-global"])
C("Lind–Reichardt x⁴ − 17 = 2y²", "0", "Sha", "proved Hasse failure", "descent", "Same as above.", "None.", [], ["outcome:false", "obst:sha", "local-global"])
C("Cassels–Guy cubic surface 5x³ + 9y³ + 10z³ + 12w³ = 0", "0", "Brauer–Manin", "proved Hasse failure", "BM obstruction",
  "Cubic surfaces can fail Hasse; ES's cubic surface has no BM obstruction — conjecturally rational points satisfy Hasse (Colliot-Thélène), but ES is integral/positive.",
  "None.", [], ["outcome:false", "obst:BM", "cubic-surface"])
C("Hasse principle for diagonal cubic surfaces (Swinnerton-Dyer; Heath-Brown–Skorobogatov)", "—", "BM", "conditional (finiteness of Sha / Schinzel's H)",
  "fibration method + descent", "Pointwise rational existence on cubic surfaces is conditional on Schinzel H — is ES (integral) conditional on some Dickson/H-type input with p fixed?",
  "Check CONDITIONAL_ES.md for which conditional inputs have been tried; test 'Dickson's conjecture for linear forms in auxiliary variables with p fixed' as an input.",
  ["CONDITIONAL_ES.md"], ["outcome:conditional", "mech:fibration-method", "seen:CONDITIONAL_ES.md"], conf="med")
C("Cassels: solutions of x³ + y³ + z³ = 3 satisfy x ≡ y ≡ z mod 9", "unknown count", "none — but cubic reciprocity constrains solutions",
  "proved (Cassels 1985 via cubic reciprocity)", "cubic reciprocity on Z[ω]",
  "Reciprocity can constrain the shape of integral solutions without forbidding them — ES's T1 may have 'soft' analogues at primes restricting which certificate shapes can occur.",
  "For p ≡ 1 mod 24, tabulate which Type I/II shapes appear and test for reciprocity-type correlations with (p/q) symbols for small q.",
  ["Cassels 1985 Math. Comp.", "Siksek 'Sums of integer cubes'"], ["outcome:proved-constraint", "obst:reciprocity-soft", "integral-points"], effort="cheap")
C("Melfi: every even number is a sum of two practical numbers", "large", "none", "proved (Melfi 1996)",
  "practical numbers are dense-ish (≍ x/log x, Weingartner) with multiplicative closure", "Practical numbers are the Egyptian-fraction-friendly integers; a 'Goldbach' for them is provable via their multiplicative structure.",
  "Look at whether ES for p holds trivially when p+something is practical with suitable divisor sums; formalise 'practical-number' certificates.",
  ["Melfi 1996", "arXiv:2007.11062"], ["outcome:proved-all", "egyptian", "mech:multiplicative-closure"])
C("Erdős: every a/b has an Egyptian expansion with ≪ log log b terms", "—", "none", "open; Vose 1985 proves O(√log b)",
  "explicit multi-scale constructions", "General-numerator analogue of ES (term count bounded in terms of b); ES is the strongest bounded-term case at a = 4.",
  "Read Vose's construction; check whether it gives 4/p with O(1) terms in some families of p.",
  ["Vose 1985", "Graham 'Paul Erdős and Egyptian fractions'"], ["outcome:open", "egyptian", "mech:constructive-algorithm"])
C("Greedy algorithm length for 4/n", "—", "—", "known: at most 4 terms (numerator decreases each step)", "numerator decrease",
  "Monotone-numerator argument gives 4 terms for free; ES needs 3. One-step lookahead improvements of greedy are a cheap source of families.",
  "Characterise the p for which some 'greedy with one free choice' algorithm gives 3 terms; compare with Mordell's classes.", [], ["outcome:proved", "egyptian", "algorithmic"], conf="high")
C("Euclid–Mullin sequence contains every prime", "heuristic yes", "none", "open", "none", "Pointwise-every-prime statement with no structure; control.", "None.", [], ["outcome:open"], conf="med")
C("Carmichael numbers: infinitely many (AGP 1994)", "x^{c}", "none", "proved", "construct L with many primes p with p−1 | L (thick object) + subset-product zero-sum",
  "Thick-object + combinatorial extraction (subset products hitting 1 in a group) — ES's gate G4 asks subset products of prime factors to hit −1.",
  "Compare: AGP subset-product argument (Davenport constant of (ℤ/L)^×) vs ES gate: can Davenport-constant bounds force a subset product ≡ −1 mod 4C among prime factors of p-tied integers?",
  ["Alford–Granville–Pomerance Ann. Math. 1994"], ["outcome:proved", "mech:subset-product", "mech:davenport-constant", "gate-G4"], effort="medium")
C("Klurman–Shparlinski–Teräväinen: small primes generate (ℤ/q)^× for almost all q", "(log Q)^{1+ε} primes", "—", "proved almost all q",
  "averaging over q", "Shows subset-product generation by small primes is provable on average; ES needs it at one tied integer.", "None new.", ["arXiv:2609.25393"],
  ["outcome:almost-all", "mech:subset-product", "seen:ES_APPROACH_GENERATORS.md"])
C("Ford: integers with a divisor in (y, 2y] (H(x,y,2y))", "—", "—", "order of magnitude proved", "distribution of divisors, Erdős–Tenenbaum",
  "ES is a 'divisor in a class' problem; Ford's machinery describes the probability that an integer has divisors in prescribed ranges.",
  "Model R(p) as 'number of divisors of N in a class within a range' and use Ford's local laws to predict fluctuations (does Ford's ladder-of-divisors give log² for ES?).",
  ["Ford Ann. Math. 2008"], ["outcome:proved", "mech:divisor-distribution"], effort="medium")
C("Hooley's Δ-function / divisors in short ranges", "—", "—", "proved bounds (Hall–Tenenbaum, Ford–Green–Koukoulopoulos)", "concentration of divisors",
  "Same toolbox as above.", "Check whether Δ(4Cp+1) lower bounds help produce divisors in a window compatible with ES certificate size constraints.", [],
  ["outcome:proved", "mech:divisor-distribution"], conf="med")
C("Every prime p > 3: p = a + b with a, b ≥ 1 and ab a square? (trivial cases) vs p = x² + y² + 1? (Linnik: p − 1 = x² + y²)", "power", "none", "proved (Linnik)",
  "dispersion", "Linnik's p − 1 = x² + y² is a pointwise-prime theorem via dispersion over primes (averaging over primes!).",
  "Control: the averaging is over p, not pointwise in a fixed n.", [], ["outcome:proved", "mech:dispersion"], conf="med")
C("Piatetski-Shapiro primes / primes in thin sets for ternary Goldbach", "power", "none", "proved for exponent ranges", "exponential sums",
  "Thin witness sets still pointwise when count is a power.", "None.", [], ["outcome:proved", "count:power"])
C("Gauss's Last Entry / Kummer's conjecture on cubic Gauss sums", "—", "—", "Kummer's conjecture false-as-stated; distribution proved (Heath-Brown–Patterson)", "metaplectic forms",
  "Distribution vs pointwise: Gauss sums equidistribute but individual sign/argument unknown — metaplectic links (METAPLECTIC_ES.md).",
  "None new.", ["METAPLECTIC_ES.md"], ["outcome:distribution", "mech:metaplectic", "seen:METAPLECTIC_ES.md"], conf="med")
C("Gaussian moat problem", "—", "—", "open (moats exist for small steps)", "computation", "Control.", "None.", [], ["outcome:open"], conf="med")
C("Lonely runner conjecture", "—", "—", "open beyond ~10 runners", "Diophantine approximation + case analysis", "Pointwise existence (a good time t) via finite case analysis, proved for small numbers of runners.",
  "None.", [], ["outcome:open", "mech:case-analysis"], conf="med")
C("Erdős–Szekeres / Ramsey-type existence", "—", "—", "proved existence", "pigeonhole", "Pigeonhole control.", "None.", [], ["outcome:proved", "mech:pigeonhole"], conf="med")
C("Goldbach for Gaussian integers / number fields (Mitsui)", "power", "—", "almost all", "Hecke L-functions", "Control.", "None.", [], ["outcome:almost-all", "count:power"], conf="med")
C("Erdős–Straus over F_q[T] (proved variants per repo)", "—", "—", "proved variants", "see FUNCTIONFIELD_ES.md", "Direct analogue.", "None new.", ["FUNCTIONFIELD_ES.md"],
  ["outcome:proved-ff", "function-field", "seen:FUNCTIONFIELD_ES.md"])
C("4/n with restricted denominators (squarefree; x | y | z; x,y,z ≡ 1 mod 4; …)", "≤ log² n", "parity kills some restrictions outright: three odd denominators are impossible for 4/n, n odd (odd·n = 4·odd)", "mostly unknown",
  "—", "Restricting denominators thins the count — find the restriction at which an ES-type statement provably fails (dividing line inside ES variants).",
  "Compute, for restrictions (squarefree; x | y | z; exactly one even denominator; pairwise coprime up to n), the first n with no solution up to 10^7.",
  [], ["outcome:open", "egyptian", "family-crossing-line", "computation"], conf="med", effort="cheap")
C("Erdős–Straus for 4/n with x ≤ y ≤ z and z ≤ n^k bounded exponent", "count depends on k", "—", "unknown; ES solutions can have z ≍ n² (Type I)",
  "—", "Size-restricted variant gives a tunable count; dividing line in k.", "Compute min over p of the minimal max-denominator exponent log z / log p for p ≤ 10^7.",
  [], ["outcome:open", "egyptian", "size-restriction", "computation"], conf="med", effort="cheap")
