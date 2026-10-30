# Items batch 5: second pass — more items for the strongest templates, fill gaps.

I("TG", "Σ over the first denominator of a two-term representation function (ternary-Goldbach shape)",
  "Ternary Goldbach averages a binary problem over one prime: Σ_p r₂(n − p). ES: R_ES(p) = Σ_x r₂^{EF}((4x − p)/(px)), where r₂^{EF}(m/N) = #{1/y + 1/z = m/N} is a divisor-pair count (a + b ≡ 0 mod m over divisor pairs of N). The average over x is the extra variable that made Goldbach-type problems pointwise.",
  "Makes the 'three-variable' structure explicit with a sum over a long free variable x ∈ (p/4, 3p/4), whose length is power-size even if the main term is not.",
  "Compute for hard p the distribution of r₂^{EF} over x and the correlation between consecutive x; check whether the x-sum behaves like a sum of independent rare events.",
  ["two-step", "egyptian-fractions", "averaging"], "high", "cheap")
I("TG", "Real-variable circle method for 1/x + 1/y + 1/z = 4/p",
  "Count near-solutions via ∫ S(α)³ e(−4α/p) K(α) dα with S(α) = Σ_{x≤X} e(α/x) (van der Corput sums of smooth phases); exact solutions need tolerance ~ 1/(pxyz), far below what such integrals resolve.",
  "Not nonsense: it gives the density of near-solutions and the scale at which arithmetic must take over; it locates the 'resolution gap' quantitatively.",
  "Estimate the number of triples with |1/x + 1/y + 1/z − 4/p| < δ as a function of δ via the integral and compare with exact counts for p ≤ 10⁵.",
  ["circle-method", "near-solutions", "scales"], "low", "medium")
I("TART", "Is M_BM a Siegel–Weil mass? A genus/class decomposition of certificates",
  "Tartakowsky/Siegel: the main term is a mass formula Σ_{classes in genus} r_L(n)/|Aut L| / Σ 1/|Aut L|. Check whether the BM-corrected main term M_BM(p) is a mass formula over some 'genus of certificate types'; if so the deviation splits into class/spinor contributions with their own theory.",
  "A mass-formula interpretation would identify the analogue of the cusp part and of spinor exceptions (T1) in a conceptual way.",
  "Express M_BM as Π of local densities (singular series) for the (★) variety and compare with the BL Brauer-corrected Siegel–Weil heuristics; look for the 'classes' whose average it is.",
  ["siegel-weil", "mass-formula", "BM-main-term"], "med", "medium", seen=["BM_CORRECTED_COUNT.md"])
I("TWOSQ", "Liouville/Mordell class-number formulas for xy + yz + zx = n meet ES",
  "Liouville-type elementary identities relate the number of positive solutions of xy + yz + zx = n to class numbers (check the exact classical formula). ES reads σ₂(x,y,z)/σ₃(x,y,z) = 4/p, i.e. xy + yz + zx = 4xyz/p: solutions with prescribed σ₂ = m and σ₃ = pm/4 are a sub-count of a class-number-sized count.",
  "Connects ES directly to a classical every-n identity with class-number size (power-size) counts; the extra σ₃ condition is the cost.",
  "Check the classical formula for #{x,y,z ≥ 1 : xy+yz+zx = n}; then for ES solutions of small p tabulate m = xy+yz+zx and the class-number formula's prediction at n = m.",
  ["class-numbers", "symmetric-functions", "liouville"], "med", "cheap")
I("BV-EH", "τ₃ in progressions beyond 1/2 (Type III / Kloosterman–Deligne) for the shifted-d₃ reading",
  "Zhang/Polymath used Type III estimates: the ternary divisor function in APs to moduli beyond √x via Deligne's bounds (Friedlander–Iwaniec, Heath-Brown, Fouvry–Kowalski–Michel). ES words count (u,B,C) with 4uBC = p + u + B — a shifted d₃-type count; METAPLECTIC notes a shifted-d₃/GL(3)-Eisenstein reading.",
  "If ES can be put as 'τ₃-like function of a shifted argument in a progression', Type III technology offers power savings in exactly the needed shape.",
  "Write the (u, B, C) count as Σ_{n} τ₃-like(n) over n in a progression determined by p; identify the modulus size relative to the length.",
  ["type-III", "divisor-functions", "deligne"], "med", "medium", seen=["METAPLECTIC_ES.md"])
I("HQUE", "Weak subconvexity: ES needs only an ε-saving over the trivial bound R ≥ 0",
  "Soundararajan's weak subconvexity extracts a (log)^{−δ} saving from multiplicativity and mean values alone. ES: R = M_gen + X with X ≥ −M_gen trivially (R ≥ 0); ES is exactly 'X > −M_gen', any saving over the trivial bound. Seek a multiplicativity-driven argument producing X ≥ −(1 − δ)M_gen.",
  "Frames ES as the weakest possible improvement over a trivial bound, the regime where 'soft' multiplicative arguments sometimes succeed.",
  "Identify the multiplicative structure of the coefficients in X(p) (characters of order ≥ 3 mod 4uB evaluated at p) and test whether a Halász-type mean-value argument applies.",
  ["weak-subconvexity", "multiplicativity", "trivial-bound"], "low", "medium")
I("WEIL", "Zeta-type packaging of Type I/II counts at p^k (T1 kills even k)",
  "Hasse–Davenport/Weil: point counts over all extensions assemble into a rational zeta function, so a few counts determine all. T1 gives f_{I,II}(p^{2k}) = 0 for odd p. Study f_{I,II}(p^{2k+1}) and the series Σ_k f(p^k) t^k: any rationality or recursion linking f(p³), f(p⁵), … to f(p) would make f(p) > 0 follow from large odd powers.",
  "Odd powers of p may have solutions that do not come from p; a recursion would be a Hecke-type relation in the 'p-power direction'.",
  "Compute f_I, f_II at p, p³, p⁵ for small primes p ≤ 200 and look for linear recurrences in k.",
  ["zeta-functions", "T1", "p-powers"], "med", "cheap")
I("ZAREMBA", "Critical exponent of the ES word set on the Bourgain–Kontorovich dimension scale",
  "BK's density-one Zaremba needs the Hausdorff dimension of the bounded-quotient Cantor set above 5/6 (positive proportion above 1/2, etc.). The ES word set (minus-continuants of length 3 with t ∈ 4ℤ ∪ (8ℤ − p)) has #words ≤ X ≈ X log X; compute its effective 'critical exponent' and where it sits relative to BK thresholds.",
  "Places ES in the thin-orbit hierarchy: it is 'fat' (exponent 1 with log), explaining density one, and shows the every-p question is about the log factor.",
  "Count ES words ≤ X for X up to 10⁹ and fit X^δ (log X)^a; compare with the semigroup Hausdorff-dimension heuristics.",
  ["thin-orbits", "critical-exponent", "numerics"], "high", "cheap", seen=["BRAINSTORM/thin_group_orbits.md"])
I("MARKOFF", "Rotation structure: fixing two word parameters makes ES a progression",
  "BGS's middle game uses 'rotations' (fix one Markoff coordinate → conic with a cyclic action). ES words p = tuv − u − v: fixing (t, u) gives v(tu − 1) = p + u, an arithmetic condition mod tu − 1; fixing (u, v) gives t·uv = p + u + v. Use these one-parameter 'rotations' to move between certificate-bearing and non-bearing configurations.",
  "The local-to-global passage in BGS relies on such fibrations; ES has them in elementary form.",
  "For hard p, compute for each (t,u) with tu ≤ T the residue of p + u mod tu − 1 and visualise the hit structure; look for orbit-like propagation.",
  ["rotations", "fibrations", "markoff"], "low", "cheap")
I("HEIL", "Goldfeld–Gross–Zagier-type effectivity: an auxiliary L-function with a high-order zero",
  "Goldfeld showed that an L-function with a zero of order ≥ 3 at s = 1/2 makes Siegel effective (Gross–Zagier supplied it). For an ineffective ES theorem (via Siegel), an analogous auxiliary object with a forced high-order vanishing would make p₀ explicit.",
  "Only relevant once an ineffective all-large-p ES theorem exists, but it shows the route from ineffective to effective is not blocked in principle.",
  "List places where Siegel's theorem could enter an ES argument (main-term lower bounds via L(1,χ)) and check whether Goldfeld's effective bound (h(−d) ≫ log d) is enough there.",
  ["effectivity", "goldfeld", "L-functions"], "low", "cheap")
I("BAKER", "Modular units / Weber functions as certificate generators",
  "Heegner and Stark solved class number one through values of modular functions at CM points giving explicit Diophantine equations. Look for modular functions whose values at CM points related to p (disc −4p, −16p) are algebraic integers that factor into ES certificate data.",
  "CM values give 'always-existing' algebraic objects attached to p; if their norms produce divisors in the right classes, existence follows.",
  "Compute norms of Weber-function values f(√−p) or of singular moduli j((1+√−p)/2) differences for small p and check their prime factors against −1 (mod 4C) classes for the relevant C.",
  ["CM-values", "modular-functions", "odd"], "low", "medium")
I("SNIRBOUND", "8/n exceptions as a built-in falsification test",
  "Kolmogorov/Kahane–Katznelson show almost-everywhere statements can fail on prescribed null sets. ES has a real-world analogue: 8/n fails at 131 and 241 while being 'almost all'. Any ES argument that is uniform in the numerator m without a threshold would prove 8/131 — use this as a mandatory test for every candidate mechanism.",
  "Cheap and decisive filter for proof attempts (already in FRONTIER (J)41); worth applying to each upgrade template in this list.",
  "For each template here (complementary methods, pigeonhole + group law, Hecke relations, …) check whether its ES version would also apply verbatim to 8/131.",
  ["falsification-test", "numerator-uniformity", "8/n"], "high", "cheap", seen=["AMPLIFY_EXCEPTION.md"])
I("DAV", "Group-ring/Fourier formula for the window certificate count",
  "Olson's method works in group rings. For window e and N = Π q_i^{a_i} (coprime to e), the number of coprime divisor pairs (a, b) with ab | N and a ≡ −b (mod e) equals (1/φ(e)) Σ_{χ mod e} χ(−1) Π_i (1 + Σ_{1≤j≤a_i} (χ(q_i)^j + χ̄(q_i)^j)). ES at window e ⟺ this is > 0.",
  "An exact character-sum formula for each window; non-vanishing is a statement about one finite character sum, open to zero-sum/Fourier techniques.",
  "Implement the formula, verify against brute force, then study which characters dominate when the count is 0 for hard (p, e) pairs.",
  ["group-ring", "character-sums", "exact-formula"], "high", "cheap")
I("THREECUBES", "Certificate-search complexity as a heuristic proxy",
  "Three cubes is 'computation only' because representations are astronomically large. ES certificates are tiny and fast to find; measure the asymptotic cost of the cheapest search (e.g. via Lenstra divisors-in-classes or e-slice scans) as p grows to quantify how 'easy' every p is.",
  "If the search cost provably stays polylog for all p in a model, a proof by 'algorithm + analysis' (AKS-style) becomes a natural target.",
  "Benchmark the cheapest certificate finder on the adversarial primes at 10¹⁸–10²⁵ and fit cost vs log p.",
  ["algorithms", "complexity", "numerics"], "high", "cheap")
I("KAKEYA-FF", "Dvir-type bound for certificate-free residue sets modulo q",
  "Dvir's polynomial argument shows Kakeya sets are large. Dual question for ES: how large can a set A of residues r mod q (q prime) be such that no r ∈ A admits a (★)-type certificate with parameters in a box (u, B, C ≤ Q)? A low-degree polynomial vanishing on A and its 'directions' could bound |A|.",
  "Upper bounds on certificate-free residue sets mod q translate into 'most residues are covered' statements with explicit polynomial-method constants.",
  "Compute certificate-free residue sets mod q for q ≤ 10⁴ and box sizes Q; compare their sizes with q·(1 − c) and check for algebraic structure (squares?).",
  ["polynomial-method", "residue-sets"], "low", "medium")
I("BIEB", "Special-function positivity (Askey–Gasper) for weighted ES counts",
  "de Branges reduced every n to the Askey–Gasper positivity of Jacobi-polynomial sums. Seek weights w_C on levels such that Σ_C w_C · D_C(p) is expressible as a positive combination of 'basis' quantities via a classical positivity identity (e.g. Fejér kernels, Jacobi sums), valid for all p.",
  "Every-n positivity theorems often reduce to one special-function inequality; ES weighted counts have explicit Fourier expansions over characters.",
  "Write the character expansion of Σ_C w_C D_C(p) and search for weights making the coefficient vector positive-definite (Bochner/Fejér-type), at least in a model where p's character values are free.",
  ["positivity", "special-functions", "weights"], "low", "medium")
I("BIEB", "Case-by-case → uniform: the small-n Bieberbach proofs were all different",
  "Before de Branges, each n (2–6) needed a different method; the uniform proof came from changing the statement (Milin's stronger conjecture). ES analogue: the repo's exponential families each needed bespoke windows; look for a stronger uniform statement (Milin-like) that implies all of them.",
  "Suggests searching for the right stronger statement rather than more cases.",
  "List the proved families (3·2^s+1, 7·4^s+9, 63·2^s+1, 4^s+k) and extract the common certificate mechanism; formulate a single conjecture implying all and test it on the open families.",
  ["strengthening", "uniformity", "exponential-families"], "med", "cheap")
I("COLLATZ", "Collatz wall vs ES wall: what Tao's 'almost all' could not do",
  "Tao proved almost all Collatz orbits attain almost bounded values via 3-adic mixing of the Syracuse random variable; every orbit is out of reach for the same quantifier reason as ES. Compare the precise failure point of both arguments (single-orbit vs averaged mixing).",
  "A side-by-side 'what fails' analysis of two famous almost-all walls can suggest which extra structure ES has that Collatz lacks (ES has algebraic structure: divisors, characters, modular forms).",
  "Write a one-page comparison: Tao's Syracuse estimate vs Vaughan/ES exceptional-set estimates; note where ES has exact algebraic identities (Thm K) that Collatz lacks.",
  ["stuck-mirror", "comparison", "meta-strategy"], "high", "cheap")
I("COLLATZ", "Logarithmic density as an intermediate notion for ES-type sub-routes",
  "Tao's Collatz and Chowla results hold in logarithmic density, which is easier than natural density. For ES sub-routes whose failure sets might be infinite (e.g. (★) alone), compute logarithmic-density statements and the corresponding 'log-averaged' tools (Tao's entropy decrement).",
  "Log-averaging made several almost-all results possible where natural density was stuck; useful for sub-route exceptional sets.",
  "Estimate Σ_{p ≤ X, (★) fails} 1/p numerically and check whether log-averaged tools give a finite bound.",
  ["log-density", "sub-routes", "exceptional-set"], "med", "cheap")
I("AXKOCHEN", "Ultraproduct transfer between F_q[T]-ES and ℤ-ES statements",
  "Ax–Kochen: first-order statements true for F_p((t)) for almost all p transfer to Q_p for almost all p. ES over F_q[T] has proved variants; ES itself is not first-order in the needed way (it quantifies over integers of unbounded size), but bounded-complexity sub-statements (certificates of bounded 'shape') are. Identify which transfer.",
  "Clarifies precisely which ES-type statements a model-theoretic transfer could ever reach (and that the full statement likely cannot).",
  "Formulate ES sub-statements with bounded quantifier complexity (e.g. 'a certificate with C dividing a fixed polynomial in p') and check whether they are decidable/transferable.",
  ["model-theory", "transfer", "function-fields"], "low", "medium")
I("AXKOCHEN", "All-but-finitely-many with genuine small exceptions (Terjanian) — ES-type numerator analogues",
  "Ax–Kochen's statement is true for p > p₀(d) and false for some small p (Terjanian). The ES numerator family behaves similarly: 4/n has no known exception, but 8/n fails at 131, 241. A structural explanation of where p₀(m) lies for m/n would show what makes m = 4 special.",
  "Understanding why 4 behaves like 'p₀ = 1' while 8 has small exceptions is a sharp test of any mechanism.",
  "Tabulate the exceptions of m/n for m ≤ 30 (PW data) and search for a statistic predicting their largest exception (cf. Schinzel's exp(m^{1/3+o(1)})).",
  ["numerator-family", "exceptions", "threshold"], "med", "cheap", seen=["AMPLIFY_EXCEPTION.md"])
I("ERDCOV", "Covering-system disproof search on exponential families (Sierpiński-type)",
  "Sierpiński/Erdős obstructions arise when every member of an exponential family is forced to have a small prime factor. For ES families n_s = k·2^s + 1, check whether a covering system could force every certificate condition to fail for all s (it would give infinitely many ES counterexamples).",
  "Disproof-side: open families (15·2^s + 1, 4^s + 297) are exactly where such an obstruction would show up first.",
  "For n_s = 15·2^s + 1, compute for small (C, d) the periodic sets of s with a certificate; check whether their union is all s (proof) or misses a progression (potential covering obstruction).",
  ["covering-obstruction", "exponential-families", "disproof-hygiene"], "high", "cheap", seen=["BRAINSTORM/bsE_sierpinski_moving_integer.md"])
I("LINNIK-ERG", "Splitting-condition families: ES for all p with (p/ℓ) = −1 for a fixed small ℓ",
  "Linnik's ergodic method proved Duke-type equidistribution under a fixed splitting condition. Intermediate ES goal: prove ES (or (★)) for all p in the set {p : (p/ℓ) = −1} for one fixed ℓ (e.g. ℓ = 3 excluded by Mordell classes; ℓ = 11, 13, …), where the BM main term at levels involving ℓ is guaranteed.",
  "A fixed non-residue gives a guaranteed positive BM contribution (SYNTHESIS_SPARKS9); a theorem for one fixed ℓ would be the first infinite every-p family of Mordell-hard primes.",
  "For ℓ = 11, 13, 17 compute the (★) and ES₅ counts restricted to levels using ℓ, over primes with (p/ℓ) = −1; check whether these restricted counts ever vanish.",
  ["splitting-condition", "intermediate-target", "BM-layer"], "high", "cheap", seen=["SYNTHESIS_SPARKS9.md"])
I("DUKE", "Ineffective all-large p for the subfamily of p with a bounded non-residue profile",
  "Duke–Schulze-Pillot's theorem is ineffective but for every large n. Target: 'for every fixed L, all sufficiently large p with ℓ(p) ≤ L satisfy ES' (ineffectively). Since ℓ(p) ≤ L for 100% of primes as L → ∞, this would be a strong almost-all-with-structure result.",
  "Combines the guaranteed BM positivity at small ℓ with a Siegel-type ineffective control of the error at those levels.",
  "Formulate the restricted count using only levels built from primes ≤ L and estimate its main term vs error for fixed L as p → ∞.",
  ["ineffective", "non-residue-profile", "intermediate-target"], "med", "medium")
I("QUE", "Escape of mass for ES: certificates drifting to extreme shapes",
  "Soundararajan's step was 'no escape of mass': limiting measures are probability measures. ES analogue: as p → ∞, could the certificates' normalized shape distribution (log C / log p, log u / log p) concentrate at the boundary (C ≈ 1 or C ≈ p), so that 'typical' regions are empty? Show mass stays in the bulk.",
  "If certificates escape to extreme shapes for hard p, proofs focusing on bulk shapes miss them; if not, bulk counting suffices.",
  "For hard primes vs controls, compute the empirical distribution of (log C/log p, log u/log p) of all certificates.",
  ["escape-of-mass", "shape-distribution", "numerics"], "med", "cheap")
I("PELL", "Pell-shaped conjecture: Type I ∪ II for all odd non-squares beyond a finite list",
  "Pell is solvable exactly for non-squares. ES Type I/II fail at all odd squares (T1) and, per the repo, U(n) fails at odd squares plus {105, 2961, 3985, 25305, 111969, 978145}. Formulate the precise 'Pell-shaped' conjecture (Type I ∪ II solvable for every odd non-square n outside an explicit finite list) and treat it as the natural target with the right exception set.",
  "A conjecture whose exception set is exactly squares + finite list has the shape of classical every-n theorems (Pell, three squares).",
  "Extend the Type I ∪ II census over odd non-squares (not just primes) to 10⁹ and confirm the exception list.",
  ["exception-set", "conjecture", "T1"], "high", "cheap")
I("SPENCER", "Entropy count of near-certificates vs defect buckets",
  "Spencer's partial colouring needs (#objects) > (#buckets)·(something). For ES, near-certificates of p with defect δ in a set of size Q number ~ p^{a}; buckets (defect, residues) number ~ Q^{b}. If a > b·log Q / log p, collisions are forced; compute a and b for concrete combination laws.",
  "A pure counting check that tells whether any pigeonhole + combination mechanism can possibly work for ES.",
  "For the SL₂-form near-certificates (det = 1 + δ with |δ| ≤ Δ), count objects with entries ≤ p and the number of congruence buckets needed for the quotient to be integral.",
  ["entropy", "pigeonhole", "counting"], "med", "cheap")
I("GOWERS", "Affine-group encoding: (★) as a product-covering statement in Aff(ℤ/q)",
  "In small groups (affine group of F_q, order q(q−1)) the Gowers/Nikolov–Pyber thresholds are less demanding. The (★) condition (4uC − 1) | (p + u) can be read as an affine relation x ↦ 4uC·x − u evaluated mod divisors; look for a formulation as 'target ∈ A·B·C' in an affine group with sets of size ≈ q^{2/3}.",
  "If an encoding into a small quasirandom-enough group exists, the 'one more factor' trick could cover every target mod q; integrality still needs a size argument.",
  "Search encodings: map (u, C) ↦ affine maps mod q and check whether the product set of three natural sets covers Aff(F_q) for q ≤ 101.",
  ["affine-group", "product-covering", "encoding"], "low", "medium")
I("CHEN", "Parity of Ω(4Cp+1) and certificate existence",
  "Chen's theorem lives at the parity barrier (P₂ but not primes). Certificates at level C need a divisor in a class; if 4Cp+1 is prime, the only divisors are 1 and itself (class 1), so prime values of 4Cp+1 are useless. Measure the dependence of certificate probability on Ω(4Cp+1).",
  "Tells whether ES needs 'many prime factors' (sieve-friendly almost-primes in reverse) and quantifies the loss from prime values.",
  "For p ~ 10⁹ and C ≤ 10⁵ tabulate P(certificate at C | Ω(4Cp+1) = k) for k = 1..8.",
  ["almost-primes", "parity", "numerics"], "high", "cheap")
I("SCHN", "Basis of order 3 vs order 4: Egyptian 'order' of 4/p is ≤ 4 trivially",
  "Schnirelmann bounds the order of a basis. For unit fractions, 4/p is always a sum of 4 unit fractions (4/p = 1/(k+1) + 3/(p(k+1)), and 3/m splits into ≤ 3 terms); ES asks for order 3. Study the 'order-3 deficiency': which 4-term representations of 4/p are 'one merge away' from a 3-term one (two terms with 1/a + 1/b a unit fraction)?",
  "Turns ES into a merging problem on abundant 4-term representations, a different combinatorial entry point.",
  "For p ≤ 10⁵ enumerate 4-term representations with bounded denominators and count mergeable pairs; compare with the number of 3-term solutions.",
  ["merging", "egyptian-fractions", "order-of-basis"], "med", "cheap")
I("HLP", "Hooley's GRH-conditional pointwise proofs: what GRH buys ES pointwise",
  "Hooley proved n = p + x² + y² for all large n under GRH before Linnik's unconditional proof. The repo says GRH gives only M_gen(p) ≥ (1 − o(1)) log log p for ES. Pin down exactly which GRH-type statement (GRH for which family, with which uniformity) would give a pointwise ES theorem, as Hooley's did.",
  "Knowing the exact conditional input needed is the first step of any conditional → unconditional upgrade (Hooley → Linnik pattern).",
  "Re-derive SINGLE_P_COUNT (J)98 and identify where GRH's log-log loss arises (number of characters vs. length); test whether 'GRH + pair correlation' or 'GRH for higher-order characters' changes it.",
  ["GRH", "conditional", "pointwise"], "med", "medium", seen=["SINGLE_P_COUNT.md"])
I("LAG", "Quaternion (Hurwitz) proof of four squares: Euclidean order as the 'every p' engine",
  "Lagrange's theorem has a proof via the Hurwitz order being (left) Euclidean: p = ππ̄ factors, giving p as a norm. ES quaternion reformulations (repo) would need an order with a Euclidean-like property relative to a congruence structure tied to 4C.",
  "If the relevant order (or its Eichler sub-order of level 4C) has class number one for small C, ES at those levels follows from factorisation.",
  "Compute class numbers of Eichler orders of level 4C in the Hurwitz quaternion algebra (Sage) for C ≤ 20 and compare with which levels never fail.",
  ["quaternion-orders", "euclidean", "class-number-one"], "med", "cheap", kw=["Eichler order"])
I("THREESQ", "Genus-theory exclusion at squares mirrors the 4^a(8b+7) exclusion",
  "Three squares fail exactly on 4^a(8b+7) — a local obstruction at 2. T1 is a global (reciprocity) exclusion at odd squares for Type I/II. Look for a ternary/quaternary encoding where the T1 exclusion becomes a local obstruction (at 2 or at an auxiliary prime) after a change of variables, which would make it 'genus visible'.",
  "If T1 could be made local in some encoding, the remaining problem would be a pure genus-to-class question.",
  "Test encodings: n ↦ 4Cn + 1 for small C; at odd squares n = m², check whether 4Cm² + 1's divisor-class failure is explained by local conditions at 2 or at primes dividing C.",
  ["genus-theory", "T1", "local-obstruction"], "med", "cheap")
I("RAMTERN", "GRH + computation template for ES sub-routes with explicit exceptions",
  "Ono–Soundararajan: GRH-conditional explicit threshold + computation to 2·10¹⁰ gives an exact exception list. For a sub-route whose failures are explicitly known (b=1 line: 193, 2521, 66529 ≤ 10¹¹), attempt a GRH-conditional proof that there are no further failures.",
  "A conditional complete classification for a sub-route would be a first 'every p' theorem (conditional) in the ES landscape.",
  "Identify the sub-route with the simplest certificate condition (b=1: p + 4d has a divisor ≡ −1 mod 4d) and attempt a GRH-conditional lower bound for its count with explicit constants.",
  ["GRH", "sub-routes", "explicit-exceptions"], "med", "medium", seen=["B1_LINE.md"])
I("APOLLO", "Corrected local-global: formulate ES sub-routes with their reciprocity exceptions removed",
  "After the Apollonian disproof, the corrected conjecture excludes the reciprocity families. For ES sub-routes, formulate 'corrected' versions (e.g. Type I/II for all non-squares; (★) for all p outside an explicit reciprocity-defined set) and test which corrected statements have finite exception sets.",
  "Ensures the targets are the right ones before attempting proofs.",
  "Use the repo's census data to fit, for each sub-route, its failure set to explicit reciprocity conditions; report residual sporadic failures.",
  ["reciprocity-obstructions", "corrected-conjecture"], "high", "cheap")
I("SENDOV", "Large-degree analogue: ES for m/p as m grows with p",
  "Tao's Sendov proof works for sufficiently high degree, using the degree as a large parameter. ES has a natural large parameter family: m/p for growing m (ES_m). Uniform-in-m results exist for the exceptional set ((D)31: E_m(I) ≪ H exp(−c(log H)^{3/4} m^{−1/4})); study the regime m ≈ log p where Schinzel-type exceptions appear, as a 'large-parameter' analogue.",
  "The large-m regime has genuine exceptions; the transition region may show which mechanism protects m = 4.",
  "Compute the least m(p) for which m/p fails (3-term) for primes p ≤ 10⁵, and the distribution of m(p)/log p.",
  ["numerator-family", "large-parameter", "numerics"], "med", "cheap")
I("EGZ", "Zero-sum over levels: among many levels, some combination of near-certificates is exact",
  "EGZ guarantees a zero-sum subsequence of prescribed length. ES near-certificates at different levels C carry 'defect classes' in groups (ℤ/4C)*; if defects lived in a common group, a zero-sum subsequence of defects could combine into an exact certificate (requires a combination law across levels).",
  "Odd: needs a multiplicative combination law; but zero-sum theory exactly converts 'many near-misses' into 'one hit'.",
  "Find a common quotient group for defects at levels C ≡ 0 (mod M) (e.g. (ℤ/M)*) and test whether products of near-certificates at different levels produce certificates at the lcm level.",
  ["zero-sum", "combination-law", "odd"], "low", "medium")
I("CROOT", "Croot's 'one target, all colourings' as a pointwise model for ES",
  "Croot's theorem is pointwise in the target (exactly 1) and uniform over colourings — the quantifier structure ES needs (one target 4/p, every p). Study Croot's proof for which step converts averaged Fourier information into a single-target statement.",
  "Croot's argument is one of the few in Egyptian fractions where a specific target is hit for every configuration; its key lemma may transfer to 'every p' with a family of targets.",
  "Read Croot (Ann. Math. 2003) and isolate the single-target step; test whether its numerics (number of terms, smoothness) can be squeezed to 3 terms for targets 4/p.",
  ["egyptian-fractions", "single-target", "literature"], "med", "medium")
I("BERT", "Explicit inequalities + finite check as the complete proof shape",
  "Bertrand's postulate is fully proved by an explicit inequality for n ≥ n₀ plus a hand check. For ES, collect every inequality-type sufficient condition (e.g. M_BM(p) > |X(p)| bound, Lagrange-pigeonhole ratio > 1 for some e, single-prime certificate count ≥ 1) and see if any admits an explicit lower-bound/upper-bound argument for all p ≥ p₀ with p₀ ≤ 10¹⁸.",
  "Forces each mechanism to be phrased as an inequality between explicit quantities — useful even if none closes.",
  "Write the 5 most promising sufficient conditions as explicit inequalities and evaluate both sides numerically at p ~ 10¹⁸ for the adversarial primes.",
  ["explicit-inequalities", "verification", "meta-strategy"], "high", "cheap")
I("FLT", "Modularity of an ES generating object and a 'level-lowering' contradiction",
  "Ribet's level lowering forced a hypothetical form to level 2 where none exists. ES generating functions (Thm K level series) are modular of level t; a failure of ES at p might force some auxiliary modular form (e.g. a twisted combination vanishing at p) to have a special property that lowers its level or weight to a space that is empty.",
  "Speculative, but 'empty space of modular forms' contradictions are the archetypal every-n mechanism.",
  "Search for linear combinations of level-t series whose p-th coefficient is R(p) times a nonzero constant, and determine the space they live in; ask whether vanishing at all ES-failing p would force membership in a smaller space.",
  ["modularity", "level-lowering", "speculative"], "low", "big")
I("SUBCONV", "Family of twists by characters mod p: R as a coefficient of a p-twisted object",
  "Subconvexity in the q-aspect uses the family of all characters mod q. ES at p involves characters mod p evaluated at small integers ((−m/p) in T(p)); consider the family {R_χ(p) : χ mod p} of character-twisted certificate counts and its moments, where orthogonality mod p is available.",
  "The q-aspect family is the natural family for a fixed p (it does not need varying p), so moment methods apply without leaving p.",
  "Define R_χ(p) = Σ_{certificates} χ(u)… for χ mod p; compute Σ_χ |R_χ(p)|² exactly by orthogonality and see whether it controls the trivial-character term.",
  ["q-aspect", "character-twists", "moments"], "med", "medium")
I("ORE", "Frobenius count in SL₂(ℤ/q) for the SL₂ form of ES",
  "Ore-type proofs count solutions of word equations via Σ_χ χ(g)/χ(1). The SL₂ form asks for γ = [[a, p],[c, d]] with a ≡ d ≡ −1 (mod c); reduced mod q this is a count of elements in a double-coset-type subset of SL₂(ℤ/q); its character expansion has nontrivial terms bounded by 1/χ(1) ~ 1/q.",
  "Shows how much cancellation is available 'for free' in a nonabelian encoding (local information only, but with strong decay).",
  "Compute for primes q the number of solutions mod q via characters of SL₂(F_q) and compare with the abelian (genus) expansion's error.",
  ["nonabelian-fourier", "SL2", "local-counts"], "low", "medium")
