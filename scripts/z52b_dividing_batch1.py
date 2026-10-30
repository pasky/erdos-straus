from z52b_dividing_lib import C, I

# ---- Catalog part 1: primes + sparse sequences, coverings ----
C("n = p + 2^k (de Polignac / Romanoff / Erdős)", "≍ Σ_k 1/log n ≍ O(1) (log n terms each 1/log n)",
  "covering congruences {0 mod 2, 0 mod 3, 1 mod 4, 3 mod 8, 7 mod 12, 23 mod 24} force n−2^k divisible by a small prime",
  "false infinitely often (an AP of odd failures, Erdős 1950); Romanoff: positive lower density of representables",
  "failure = periodic orbit k ↦ 2^k mod m covered by finitely many moduli; density = Romanoff's L¹ bound on r(n)",
  "Canonical O(1)-count failure; ES has no periodic witness parameter, so the covering mechanism has no direct ES analogue — the reason why should be stated as a lemma.",
  "Write the ES witness set at p as orbit(s) of a map and test whether any finite modulus set can 'cover' it; check whether this reproduces B1 sterility.",
  ["BRAINSTORM/z31_small_count_pointwise.md", "Erdős 1950 Summa Brasil. Math."],
  ["outcome:false-io", "count:O(1)", "obst:covering", "mech:covering-system", "seen:BRAINSTORM/z31_small_count_pointwise.md"])
C("n = p + 2^a + 2^b (Crocker)", "≍ log n", "no single-modulus covering; failures come from an explicit sparse family",
  "false infinitely often (Crocker 1971; Pan 2011 gives ≫ x^{1−ε} odd exceptions ≤ x)",
  "an explicit sparse family of odd n (check whether it is built from 2^{2^m}−1 and Fermat-number divisibility, as commonly described)",
  "Log-count, no covering, still false i.o. — the sharpest warning that 'log² count + no local obstruction' is not enough; ES's count is log² p.",
  "Read Crocker 1971 (Pacific J. Math.) and isolate the exact structural input; ask whether an ES analogue (p tied to 2^{2^m}) exists among primes.",
  ["Crocker, Pacific J. Math 36 (1971)", "Pan 2011 (per repo s9_lower_tail_literature)", "BRAINSTORM/z52_lit_thin_pointwise.md"],
  ["outcome:false-io", "count:log", "obst:sparse-family", "mech:algebraic-structure-of-target", "seen:BRAINSTORM/z52_lit_thin_pointwise.md"])
C("odd n = p + 2^a + 2^b + 2^c (Sun's conjecture: every odd n > 8)", "≍ log² n — same order as ES",
  "none known", "open (conjectured by Z.-W. Sun, arXiv:0901.3075)", "none; numerics only",
  "Exact twin of ES in expected count (log²) with additive instead of multiplicative witnesses; any proof or disproof calibrates ES directly.",
  "Check whether Crocker's construction extends to three powers (search 'p+2^a+2^b+2^c exceptions'); compute min witness count / log² n up to 10^9.",
  ["arXiv:0901.3075 (Sun, Mixed sums of primes and other terms)"],
  ["outcome:open", "count:log2", "obst:none-known", "twin-of-ES", "in-between"], effort="medium")
C("Sierpiński numbers k·2^n + 1 (78557)", "≍ Σ_n 1/(n log 2) = ∞ (divergent, log N up to N) but along a periodic orbit",
  "covering set {3,5,7,13,19,37,73}", "false for specific k (covering); smallest Sierpiński number still open (78557 conjectured)",
  "covering system on n; also partial algebraic factorisation variants (Filaseta et al.)",
  "Shows a divergent expected count can still vanish identically when the parameter is periodic mod the covering moduli.",
  "Formulate an 'ES-Sierpiński' question: a family p(t) of primes candidates for which every ES certificate line is killed mod fixed primes; relate to T1.",
  ["Sierpiński 1960", "Selfridge 1962 (78557)"], ["outcome:false-io", "count:divergent-log", "obst:covering", "mech:covering-system"])
C("Riesel numbers k·2^n − 1 (509203)", "divergent log, periodic parameter", "covering",
  "false for specific k; minimality open", "covering", "Same mechanism as Sierpiński; included for completeness of the covering family.",
  "Note: ES certificate families are also 'k·m + 1' shapes (4Cp+1): check whether any covering-type identity is impossible for them by B1.",
  ["Riesel 1956"], ["outcome:false-io", "obst:covering", "mech:covering-system"])
C("Brier numbers (both Sierpiński and Riesel)", "divergent log", "simultaneous coverings", "exist (explicit large k)", "two coverings",
  "Simultaneous covering of two linear families is possible — relevant if ES were reduced to two simultaneous divisor conditions.",
  "Check the size of the smallest known Brier number and the covering moduli used.", [], ["outcome:false-io", "obst:covering"], conf="med")
C("n − 2^k composite for all k (Erdős; e.g. via covering)", "O(1)", "covering", "infinitely many such odd n", "covering",
  "Dual phrasing of the p + 2^k problem; witness = prime value of a shifted sparse sequence.",
  "Compare: ES at p asks for a divisor in a class of a p-shifted thin sequence (4Cp+1, C varying) — not a prime value; note the difference in kind.",
  [], ["outcome:false-io", "obst:covering", "count:O(1)"])
C("n = p + F_k (prime + Fibonacci number)", "O(1)", "covering congruences on the Fibonacci orbit (periodic mod m, Pisano period)",
  "check whether: positive proportion represented and an AP of failures known (Wu–Sun style)",
  "Pisano periodicity makes covering possible",
  "Any linear-recurrence witness sequence is periodic mod m, enabling coverings; ES witnesses are divisor-type, not recurrence-type.",
  "Search 'sum of a prime and a Fibonacci number covering' to confirm the AP-of-failures result.",
  [], ["outcome:false-io?", "count:O(1)", "obst:covering", "mech:pisano-periodicity"], conf="med")
C("Romanoff density for p + 2^k (lower density)", "O(1)", "partial covering", "positive lower density proved; upper density < 1/2 (van der Corput / Erdős)",
  "Cauchy–Schwarz + sieve upper bound for r(n) second moment", "Example where second-moment + positive mean gives positive density but not 'almost all'; ES has almost-all, a stronger regime.",
  "Compute the analogue of Romanoff's second moment Σ R(p)² for ES (count ≍ log² p): already known? compare to Elsholtz–Tao.",
  ["Romanoff 1934"], ["outcome:positive-density", "count:O(1)", "mech:second-moment"])
C("p + 2k² for odd composite n (Goldbach's other conjecture)", "≍ √n / log n (power)", "none local",
  "false: 5777 and 5993 (Stern 1856); no others known, finitely many expected", "small-n fluctuation with power count",
  "Calibrates sporadic small failures (like U(n)'s sporadic list) under a power count: failures happen only at very small n.",
  "Fit failure probability vs n for p + 2k² and compare with ES's sporadic structures (U(n) list) on a log-count scale.",
  [], ["outcome:finite-exceptions", "count:power", "obst:none", "sporadic"])
C("Goldbach binary: 2n = p + q", "≍ n / log² n (power)", "none (parity barrier for sieves)",
  "open; almost all (Chudakov, van der Corput, Estermann 1938); verified to 4·10^18",
  "circle method for almost all; parity problem blocks pointwise", "Power count yet open: shows count size alone never suffices; ES is far thinner but has multiplicative (divisor) structure.",
  "Contrast the exceptional-set exponents: Goldbach exceptions ≪ x^{1−δ} vs ES exceptions ≪ x·exp(−c log^{2/3} x); ask why ES's is weaker.",
  [], ["outcome:almost-all", "count:power", "obst:parity", "mech:circle-method"])
C("Ternary Goldbach (Helfgott)", "≍ n² / log³ n", "parity only", "proved for all odd n > 5", "circle method + explicit computation",
  "Prototype of (T): thick reservoir + exact extraction; ES lacks a power reservoir.",
  "None beyond noting it as the (T) anchor.", ["Helfgott 2013 arXiv:1312.7748"], ["outcome:proved-all", "count:power", "mech:circle-method", "mech:T-thick"])
C("Linnik–Gallagher: 2n = p + q + 2^{k_1}+…+2^{k_K}", "power (Goldbach part) × polylog", "none",
  "proved for K ≥ 13 (Heath-Brown–Puchta), K ≥ 6 claimed (Li–Liu 2610.15784)", "Goldbach reservoir absorbs polylog factor",
  "Shows exactly how polylog witnesses ride on power reservoirs; ES has no reservoir.", "None (well covered in repo).",
  ["Heath-Brown–Puchta 2002", "arXiv:2610.15784"], ["outcome:proved-all", "count:power", "mech:T-thick", "seen:BRAINSTORM/z52_lit_thin_pointwise.md"])
C("n = p + m² (Hardy–Littlewood Conjecture H)", "≍ √n/log n × singular series", "algebraic: n = square has m² − k² = (m−k)(m+k) factorisation — fails at squares",
  "open for non-squares; almost-all results known; squares are the forced exceptions",
  "factorisation identity at squares (a 'T1-like' algebraic obstruction)",
  "Exact structural analogue of ES's T1: squares are excluded by an algebraic identity, everything else expected. ES's square obstruction is reciprocity-type, but the shape matches.",
  "Write the ES T1 obstruction in the same language: does 4/m² have a 'difference of squares' factorisation forcing certificate lines empty?",
  [], ["outcome:almost-all", "count:power", "obst:algebraic-at-squares", "T1-analogue"])
C("Lemoine–Levy: odd n = p + 2q", "≍ n / log² n", "none", "open; verified numerically", "circle method for almost all",
  "Goldbach-type control item.", "None.", [], ["outcome:almost-all", "count:power", "obst:parity"], conf="high")
C("Chen: 2n = p + P₂", "power", "none", "proved for large n", "sieve with switching + Bombieri–Vinogradov",
  "Sieve beating parity by accepting a weaker witness — ES analogue would be accepting x,y,z with a weaker property.",
  "Define an 'ES-almost' witness (e.g. 4/p = 1/x + 1/y + 1/z + ε with ε a controlled unit fraction of huge denominator) and see if sieve gives it.",
  [], ["outcome:proved-all", "count:power", "mech:sieve", "weaken-witness"])
C("Linnik: n = p + x² + y²", "≍ n / log n", "none", "proved (Linnik dispersion; Hooley under GRH first)", "dispersion method",
  "Mixed multiplicative/quadratic problem proved pointwise thanks to power reservoir.", "None.", [], ["outcome:proved-all", "count:power", "mech:dispersion"])
C("Every large n = p + squarefree (Estermann)", "power", "none", "proved", "elementary sieve", "Control.", "None.",
  [], ["outcome:proved-all", "count:power"])
C("Prime in (n², (n+1)²) (Legendre)", "≍ n / log n", "none", "open; known for (x, x + x^{0.525})", "zero-density",
  "Short-interval existence with power count still open; calibrates ES's lack of averaging.", "None.", [], ["outcome:open", "count:power", "mech:zero-density"])
C("Bertrand: prime in (n, 2n)", "≍ n/log n", "none", "proved for all n", "elementary binomial-coefficient divisibility (Chebyshev/Erdős)",
  "Pointwise existence from an explicit integer (C(2n,n)) whose factorisation is forced — a 'thick deterministic object' with exact extraction.",
  "Look for an explicit p-tied integer (like C(2n,n)) whose prime factorisation provably contains a divisor in the ES class −1 mod 4C.",
  [], ["outcome:proved-all", "count:power", "mech:T-thick", "mech:binomial-divisibility"])
C("Least prime ≡ a mod q (Linnik)", "≍ q^{...}; window x with count x/(φ(q)log x)", "none",
  "proved P(a,q) ≪ q^5 (Xylouris)", "log-free zero density + Deuring–Heilbronn",
  "Fixed-modulus character event; ES's moduli move with the witness (B2).", "None (seen).", [], ["outcome:proved-all", "count:power", "mech:L-function-zeros", "seen:BRAINSTORM/z31_small_count_pointwise.md"])
C("Least quadratic non-residue n(p)", "polylog window under GRH", "none", "proved ≪ p^{1/(4√e)+ε} (Burgess); ≤ 2 log² p under GRH (Bach)",
  "character sums / L-function zeros", "ES sign layer is a least-QNR event (repo F6); the class layer is not.", "None (seen).",
  [], ["outcome:proved-all", "count:polylog-under-GRH", "mech:character-sum", "seen:BRAINSTORM/z31_small_count_pointwise.md"])
C("Artin's primitive root conjecture", "positive density of primes; for each a an infinite set", "a = square or −1 excluded (local/algebraic)",
  "conditional on GRH (Hooley 1967); unconditionally one of any three suitable a works (Heath-Brown 1986)",
  "Chebotarev in Kummer extensions; Heath-Brown via Fouvry–Iwaniec + sieve",
  "Heath-Brown's 'at most two exceptions' is a rigidity-of-exceptions theorem: ES might admit a 'one of a few certificate families works' statement.",
  "Try: prove that for every p at least one of three named ES certificate families works, using Heath-Brown's style of multiplicative-relations argument.",
  ["Hooley 1967", "Heath-Brown 1986 Quart. J. Math."], ["outcome:conditional", "mech:chebotarev", "mech:exception-rigidity"], effort="medium")
C("Primitive roots: existence of a primitive root mod every prime", "φ(p−1) ≥ 1", "none", "proved", "group structure (cyclicity of F_p^×)",
  "Existence from algebraic structure with count φ(p−1) — (R) with a thick count.", "None.", [], ["outcome:proved-all", "mech:R-rigidity", "count:power"])
C("Fermat: p ≡ 1 mod 4 ⇒ p = x² + y²", "exactly 1 (up to signs/order)", "local (p ≡ 3 mod 4 fails)",
  "proved for all p (many proofs: Euler descent, Thue lemma, Gaussian integers, Zagier involution, continued fractions)",
  "(R): parity of fixed points of an involution; pigeonhole (Thue); UFD",
  "O(1) count, pointwise, same prime class as ES's hard case — the strongest positive anchor. ES lacks a known involution with odd fixed-point count.",
  "Compute R(p) mod 2 (ordered and unordered ES counts) for p ≡ 1 mod 24 up to 10^6 to test for a parity law (see INVOLUTION_ES.md).",
  ["Zagier 1990 Amer. Math. Monthly", "WINDMILL.md"], ["outcome:proved-all", "count:O(1)", "mech:involution-parity", "mech:R-rigidity", "seen:INVOLUTION_ES.md"])
C("p = x² + 2y² (p ≡ 1,3 mod 8), x² + 3y², x² + 7y²…", "O(1)", "local (class mod 8, 3, 7)", "proved", "class number one / genus theory",
  "O(1) count pointwise from h = 1: the class group being trivial forces representation.",
  "Ask whether ES certificates at p are parametrised by a 'class group' whose triviality would force ES; compare QUATERNION_ES.md.",
  [], ["outcome:proved-all", "count:O(1)", "mech:class-number-one"])
C("p = x² + 27y² ⟺ 2 is a cubic residue mod p (p ≡ 1 mod 3)", "O(1)", "reciprocity (cubic)", "proved", "class field theory (ring class field)",
  "Pointwise criteria via class field theory carry reciprocity conditions; ES's T1 is reciprocity-type too.",
  "Look for a ring class field whose splitting of p controls existence of an ES certificate of a fixed shape.",
  ["Cox, Primes of the form x²+ny²"], ["outcome:proved-all", "count:O(1)", "obst:reciprocity", "mech:class-field-theory"])
C("p = x² + 64y² ⟺ 2 is a quartic residue (p ≡ 1 mod 8)", "O(1)", "quartic reciprocity", "proved (Gauss)", "biquadratic reciprocity",
  "Quartic residue symbols separate primes into 'yes/no' classes pointwise; ES survives all such splittings (no BM), but certificate families might each be governed by such symbols.",
  "Tabulate for each fixed ES certificate shape the governing residue symbol (quadratic/quartic) and check whether some finite set of shapes covers all symbol patterns.",
  [], ["outcome:proved-all", "count:O(1)", "obst:reciprocity", "mech:class-field-theory"])
C("Negative Pell x² − py² = −1 for primes p ≡ 1 mod 4 (Legendre)", "1 fundamental solution", "local: fails if a prime ≡ 3 mod 4 divides d",
  "proved for all primes p ≡ 1 mod 4", "parity descent on the fundamental unit of x² − py² = 1",
  "Pointwise O(1) existence at exactly ES's hard primes, proved by elementary descent on a forced object (the fundamental unit). ES lacks a 'forced object'.",
  "Try a Legendre-style descent: start from the fundamental unit ε_p of Q(√p) (or a forced ES-adjacent object) and case-split on gcds to produce a certificate.",
  ["Legendre 1785"], ["outcome:proved-all", "count:O(1)", "mech:descent", "mech:forced-object", "ES-hard-class"], effort="medium")
C("Negative Pell for general d (Stevenhagen conjecture)", "1 or 0", "local + 4-rank (Rédei)", "Koymans–Pagano proved Stevenhagen's density",
  "Rédei matrices, Smith's method", "Pointwise status governed by 2-power class group structure; density proved, pointwise only via governing fields.",
  "Check whether ES solvability for p could be expressed via a Rédei-matrix-type invariant (cf. BRAINSTORM/bsB_redei_oddpart.md).",
  ["Koymans–Pagano arXiv:2201.13424"], ["outcome:density-proved", "mech:redei", "mech:smith-method", "seen:BRAINSTORM/bsB_redei_oddpart.md"])
C("Barrucand–Cohn: 8 | h(−4p) ⟺ p = x² + 32y²", "O(1)", "reciprocity", "proved", "governing field Q(ζ8, ⁴√2)… / class field theory",
  "Pointwise criteria exist iff a governing field exists; 16-rank has none (Milovic/Koymans) yet density proved.",
  "Ask: is there a 'governing field' for existence of ES certificates of bounded shape? If not, ES is in the 16-rank regime (density only).",
  [], ["outcome:proved-all", "mech:governing-field"], conf="high")
C("16-rank of Q(√−2p) (Koymans–Milovic)", "O(1) indicator", "no governing field", "density proved (Vinogradov-type sums)",
  "bilinear sums over Gaussian primes", "Example: no pointwise criterion, only density, due to lack of governing field — strong ES analogue.",
  "Read Koymans–Milovic's bilinear sum and check whether ES's E1 event can be written as a 'spin' with similar oscillation.",
  ["Koymans–Milovic (IMRN/Compositio)"], ["outcome:density-proved", "mech:spin-bilinear", "mech:no-governing-field"], conf="med", effort="medium")
C("Sums of three squares (Legendre–Gauss)", "≍ √n L(1,χ) (class number)", "local: 4^a(8b+7)", "proved", "genus theory + class number > 0",
  "Power count; pointwise thanks to class-number positivity (R). See THREE_SQUARES.md.", "None (seen).",
  [], ["outcome:proved-all", "count:power", "mech:genus", "seen:THREE_SQUARES.md"])
C("Ramanujan's x² + y² + 10z² representing odd n", "≍ √n", "spinor/genus subtleties; 18 known exceptions",
  "finite exception list proved under GRH (Ono–Soundararajan 1997); unconditionally ineffective",
  "Siegel ineffectivity / GRH for L-functions of weight-3/2 forms",
  "Model of 'finite sporadic exceptions + ineffective' — like U(n). ES's sporadic list for U(n) might be finite only via an ineffective argument.",
  "Compare the U(n) sporadic list {105, 2961, 3985, 25305, 111969, 978145} to Ramanujan-form exceptions: any common prime-factor pattern?",
  ["Ono–Soundararajan, Invent. Math. 130 (1997)"], ["outcome:conditional", "count:power", "sporadic", "mech:siegel-ineffective"])
C("Ternary forms, large n in a spinor genus (Duke–Schulze-Pillot)", "≍ n^{1/2−ε}", "spinor exceptions t·m²",
  "proved for n ≫ 1 ineffectively", "Iwaniec's bound for half-integral weight Fourier coefficients",
  "Spinor exceptional square classes are the closest classical analogue of ES's 'odd squares' obstruction.",
  "Check whether T1 can be read as a spinor-exception phenomenon for an attached ternary quadratic form (QUATERNION_ES.md).",
  ["Duke–Schulze-Pillot 1990 Invent. Math."], ["outcome:proved-large", "count:power", "obst:spinor-at-squares", "T1-analogue"], effort="medium")
C("Ternary positive forms with spinor exceptions (Schulze-Pillot, Kneser)", "power", "square classes t·m²",
  "fully classified for which square classes fail", "spinor norm / quadratic reciprocity",
  "Square-class obstructions come from spinor norms: the theory explains exactly which squares fail.",
  "Look up whether a 'spinor norm' type invariant can be attached to the ES variety restricted to n = m².",
  [], ["outcome:classified", "obst:spinor-at-squares", "T1-analogue"], conf="med", effort="medium")
C("Bhargava–Hanke 290 theorem / Conway–Schneeberger 15", "power", "local", "proved: universal iff represents 1..290",
  "escalation + modular forms (Eisenstein vs cusp bounds) for each escalator", "Finite certificate theorem: verifying small n suffices. ES has none (U(n) sporadic).",
  "Ask whether there is an ES 'escalation' statement: if all primes up to B have certificates of some shape then all do? (likely false; record why).",
  [], ["outcome:proved-all", "mech:escalation", "mech:modular-forms"])
C("Rouse 451 theorem (forms representing all odd n)", "power", "local", "proved conditional on three ternary forms representing all odd numbers",
  "escalation + modular forms", "Conditional on a Ramanujan-type ternary statement — itself a finite-exception statement.",
  "None.", ["arXiv:1111.0979"], ["outcome:conditional", "mech:escalation"])
C("Lagrange four squares", "≍ σ(n)", "none", "proved", "identity/composition (Euler four-square) + descent", "Composition law reduces to primes then descent.",
  "Ask what composition law ES admits (ES(n) ⇒ ES(kn) trivially) and whether any 'prime-to-prime' composition exists.",
  [], ["outcome:proved-all", "count:power", "mech:composition-law", "mech:descent"])
C("Sun's 1-3-5 conjecture (n = x²+y²+z²+w² with x+3y+5z a square)", "power (≈ √n)", "none", "proved (Machiavelo–Tsopanidis 2021)",
  "quaternion (Lipschitz) arithmetic, factorization", "Quaternion factorisation proves a thinned four-square statement pointwise — ES has quaternion reformulations.",
  "Read arXiv:2003.02592; check whether its factorisation trick applies to the ES quaternion-order form (QUATERNION_ES.md).",
  ["arXiv:2003.02592"], ["outcome:proved-all", "count:power", "mech:quaternion-factorisation"], effort="medium")
C("Gauss Eureka: n = three triangular numbers", "≍ √n", "none", "proved", "three squares for 8n+3", "Control.", "None.",
  [], ["outcome:proved-all", "count:power", "mech:genus"])
C("Pollock tetrahedral-number conjecture (≤ 5 tetrahedrals)", "≍ n^{2/3}", "none", "open (verified numerically)", "none",
  "Power count still open — non-quadratic forms lack modular-form machinery.", "None.", [], ["outcome:open", "count:power"], conf="med")
C("Waring: g(k), G(k)", "power", "local for small", "g(k) known except finitely many k; G(k) bounds", "circle method + Vinogradov",
  "Control (T).", "None.", [], ["outcome:proved-all", "count:power", "mech:circle-method"])
C("Seven cubes (Linnik) / four cubes conjecture", "power", "local mod 9", "seven cubes for large n proved; 4 cubes open", "circle method", "Control.", "None.",
  [], ["outcome:open", "count:power"])
C("Sums of three cubes x³+y³+z³ = k", "solutions up to height H ≍ log H (grows slowly)", "local: k ≡ ±4 mod 9 impossible; no BM obstruction for other k (Colliot-Thélène–Wittenberg)",
  "open (k = 33, 42 found by Booker / Booker–Sutherland)", "none; search",
  "A Hasse-principle-for-integral-points problem with tiny counts, like ES (integral, no BM). Neither proof nor disproof technique exists.",
  "Compare heuristic density of ES solutions (log² p per p) vs three cubes (log H): ES is 'denser' — articulate which features make ES more tractable.",
  ["Booker 2019 arXiv:1903.04284", "Colliot-Thélène–Wittenberg 2012"], ["outcome:open", "count:log", "obst:local-only", "integral-points"])
C("Sums of four signed cubes (n ≢ ±4 mod 9: Demjanenko)", "infinite families", "none for those classes", "proved for n ≢ ±4 mod 9",
  "polynomial identities covering residue classes + quadratic forms", "Identity coverage by residue classes — exactly what Mordell–Schinzel shows impossible for ES at squares.",
  "Check the precise statement of Demjanenko 1966 and which classes remain (±4 mod 9) and how close it is to Mordell's ES classes.",
  ["Demjanenko 1966"], ["outcome:proved-classes", "mech:polynomial-identity", "mech:R-rigidity"], conf="med")
C("Five signed cubes: 6x = (x+1)³ + (x−1)³ − 2x³", "infinite", "none", "proved for all n", "polynomial identity",
  "Pure identity mechanism; ES with signed denominators is trivial by identity too — positivity is ES's content.",
  "None.", [], ["outcome:proved-all", "mech:polynomial-identity"])
C("Markoff-type integral Hasse x²+y²+z²−xyz = k", "few orbits; count of points of height ≤ H ≍ (log H)^2", "integral Brauer–Manin explains some failures",
  "Hasse fails for infinitely many k (Ghosh–Sarnak); BM explains a positive proportion (Loughran–Mitankin, Colliot-Thélène–Wei–Xu); not all failures BM",
  "reduction theory for the Vieta group action: fundamental domain search shows emptiness",
  "Same 'integral points on affine cubic surface' type as ES, with infinitely many non-BM Hasse failures — direct evidence that no-BM does not imply existence.",
  "Check whether ES's affine cubic surface admits a Vieta-type reduction (fundamental domain) — compare MARKOFF_ES.md.",
  ["Ghosh–Sarnak arXiv:1706.06712", "Loughran–Mitankin IMRN 2021", "Colliot-Thélène–Wei–Xu 2020"], ["outcome:false-io", "obst:BM-partial", "obst:reduction-theory", "integral-points", "seen:MARKOFF_ES.md"])
C("Markoff mod p: transitivity of the Vieta group on X*(p)", "≍ p² points", "none", "proved for all but finitely many p (Bourgain–Gamburd–Sarnak + W. Chen 2024)",
  "Chen: every orbit size ≡ 0 mod p (divisibility invariant)", "Divisibility invariant on orbit sizes forcing a single orbit: ES lacks an infinite group action.",
  "Search for any nontrivial correspondence/group acting on ES solutions mod p (beyond permutations); see UNIT_ORBIT_ES.md.",
  ["W. Chen, Ann. Math. 2024"], ["outcome:proved-almost-all-p", "mech:orbit-divisibility", "seen:ES_APPROACH_GENERATORS.md"])
C("Markoff uniqueness conjecture (Frobenius)", "1 triple per max element", "none", "open", "none",
  "O(1)-count uniqueness (not existence) statement; open for a century.", "None.", [], ["outcome:open", "count:O(1)"], conf="high")
C("Catalan: x^a − y^b = 1", "0 expected beyond 8,9", "—", "proved (Mihăilescu 2002)", "cyclotomic fields, Stickelberger, (R)",
  "Non-existence via rigidity; the flip side of the dividing line (R).", "None.", [], ["outcome:proved-none", "count:zero", "mech:cyclotomic"])
C("Pillai: x^a − y^b = k has finitely many solutions", "finite", "—", "open in general", "Baker's linear forms for fixed exponents",
  "Finiteness side; control.", "None.", [], ["outcome:open", "count:zero"])
C("Brocard n! + 1 = m²", "Σ 1/√(n!) < ∞", "—", "open (finite expected)", "abc implies finiteness",
  "Expected finite counts: open finiteness statements are as hard as ES's existence.", "None.", [], ["outcome:open", "count:zero"])
C("Erdős–Selfridge: product of consecutive integers never a perfect power", "0", "—", "proved (1975)", "elementary combinatorial + Sylvester",
  "Elementary pointwise non-existence via clever divisibility; existence analogue in ES?", "None.", [], ["outcome:proved-none", "mech:elementary-divisibility"])
C("Lehmer's totient problem φ(n) | n − 1 ⇒ n prime", "0 expected", "—", "open", "partial structure (≥ 15 prime factors)",
  "Control on the non-existence side.", "None.", [], ["outcome:open", "count:zero"], conf="high")
C("Skolem problem (zeros of linear recurrences)", "—", "—", "decidability open; Skolem–Mahler–Lech finiteness", "p-adic analysis",
  "p-adic interpolation gives structure of zero sets; ES certificate sets in parametric families might also be p-adically structured.",
  "Check whether the set of C with a divisor of 4Cp+1 in class −1 mod 4C has any p-adic analytic structure.", [], ["outcome:open", "mech:p-adic-analytic"], conf="med")
