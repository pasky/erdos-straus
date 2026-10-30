# Lane `signature` (wave z52b): second batch of integrator items — gaps in the feature histogram + feature flips per feature.
# Writes data/z52b/signature_raw/OWN2.jsonl.
import json, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'z52b', 'signature_raw', 'OWN2.jsonl')
I = []
def it(title, connection, why, first_step, refs, tags, conf='med', effort='cheap'):
    I.append(dict(title=title, connection=connection, why=why, first_step=first_step,
                  refs=refs, tags=tags + ['src:own'], confidence_not_nonsense=conf, effort=effort))

it("Erdős–Tetali thin bases: random sets A with r_{A,k}(n) ≍ log n for EVERY n — the polylog pointwise regime, solved probabilistically",
   "Erdős–Tetali (1990): for every k there is a basis of order k with Θ(log n) representations of every large n. Same regime as ES (F04: polylog "
   "count, F01: every n, F21: pointwise), proved by independence + concentration (Janson/Chernoff) of the random set.",
   "The cleanest proof that polylog-many expected witnesses CAN give pointwise existence — when witnesses are independent enough. ES's question "
   "becomes: are ES witnesses 'Erdős–Tetali-independent' at each p, and in what quantitative sense?",
   "Estimate the dependency structure of the ES level events at fixed p (pairwise correlations over (u,B,C)) and compare with the Erdős–Tetali "
   "concentration hypotheses (bounded pairwise dependence, expected count ≥ C log n with large C).",
   ["https://tetali.math.gatech.edu/PUBLIS/et.pdf"],
   ['F04', 'F21', 'F24', 'probabilistic-method', 'thin-bases', 'solved-sibling'], 'high', 'cheap')
it("Erdős–Turán conjecture (a basis has unbounded r(n)) vs. ES's Linnik-type large values",
   "Erdős–Turán: if r_{A+A}(n) ≥ 1 for all large n then r is unbounded. ES's R(p) is unbounded (Linnik-type large values; F37) consistent with "
   "this shape; ES's word set is a 'basis' of the primes in a trilinear sense.",
   "A trilinear Erdős–Turán-type theorem would say: a set of words covering all primes must have unbounded multiplicity — the converse direction "
   "(multiplicity forced ⇒ coverage) is what ES needs; clarifies the logical relation.",
   "Check whether Erdős–Fuchs (no representation function is c + small error on average) applies to Σ_{n≤N} R(n) to give a lower bound on its "
   "fluctuations.",
   ["https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Tur%C3%A1n_conjecture_on_additive_bases"],
   ['F37', 'additive-bases', 'erdos-fuchs'], 'med', 'cheap')
it("Sawin–Shusterman: twin primes and Chowla over F_q[T] (q large) by étale cohomology — the geometric pointwise route",
   "Over F_q[T] with q fixed but large relative to degree, they prove twin-prime-type asymptotics via cohomology of moduli spaces. ES has "
   "function-field variants (F26).",
   "Their method gives pointwise (single-degree, single-shift) results where analytic methods give only averages — the exact B2 gap. Testing whether "
   "ES over F_q[T] large-q has a Sawin–Shusterman proof identifies the geometric object (moduli of ES words) to study over ℤ.",
   "Write the ES count over F_q[T] at fixed prime polynomial P as a point count of a variety V_P/F_q and check whether its top cohomology is "
   "controllable (dimension, irreducibility).",
   ["https://annals.math.princeton.edu/2022/196-2/p01"],
   ['F26', 'F21', 'function-field', 'etale-cohomology'], 'med', 'medium')
it("Sun's 1-3-5 conjecture proved via Lipschitz quaternions (Machiavelo–Tsopanidis): ∀n with an extra linear constraint",
   "Every n is x²+y²+z²+w² with x + 3y + 5z a square — a ∀n∃ witness statement with a constraint, proved by quaternion arithmetic (F31). ES has "
   "quaternion-order reformulations.",
   "Shows quaternion factorisation can handle 'constrained witness' existence pointwise; if an ES reformulation lives in a quaternion order with a "
   "linear/square side condition, the same factorisation tricks could apply.",
   "Read the paper's key lemma (factorisation in Lipschitz integers with prescribed residue) and compare with the QUATERNION_ES dictionary.",
   ["https://arxiv.org/abs/2003.02592"],
   ['F31', 'F01', 'quaternions', 'solved-sibling', 'seen:QUATERNION_ES.md'], 'med', 'medium')
it("Zhi-Wei Sun's family of refined-Lagrange conjectures with explicit finite exception lists",
   "Sun posed dozens of 'every n is … with constraint …' conjectures, each with finite explicit exceptions; several were proved (ternary forms, "
   "quaternions, spinor theory). Shares F01, F25, F23.",
   "A large catalogue of solved siblings sharing the 'finite explicit exceptions' feature (like U(n)) with documented proof techniques.",
   "Scan Sun's survey of conjectures on refinements of Lagrange's four-square theorem; list proved ones and their tools.",
   ["unverified: Z.-W. Sun, Refining Lagrange's four-square theorem, J. Number Theory 175 (2017)"],
   ['F25', 'F01', 'catalogue', 'quadratic-forms'], 'med', 'cheap')
it("Andrews–Dyson–Hickerson: σ(q) coefficients almost always 0 yet unbounded, via indefinite theta / Hecke characters of ℚ(√6)",
   "ADH express coefficients of a q-series (σ(q)) as signed counts of ideals in a real quadratic field (indefinite binary form). ES's level series is a "
   "Kronecker theta quotient θ(X²)/θ(X)² — also an indefinite (signature (1,1)) theta object (F19).",
   "ADH-type 'coefficient = signed ideal count' identities make vanishing/nonvanishing questions arithmetic; ES's D⁻ − D⁺ is the split-field "
   "analogue. A non-split twist might carry extra positivity.",
   "Write D_t⁻ − D_t⁺ as a sum over x² − y² type forms (split indefinite theta) and look for an ADH-style real-quadratic twist with the same coefficients.",
   ["https://eudml.org/doc/143546"],
   ['F19', 'indefinite-theta', 'q-series', 'mock-modular'], 'med', 'medium')
it("Zwegers/Appell–Lerch: Kronecker's θ(x²)/θ(x)²-type quotients as Appell–Lerch sums with completions",
   "Quotients of Jacobi theta functions in the elliptic variable are Appell–Lerch sums (Kronecker's identity); Zwegers' completion makes them "
   "harmonic Maass–Jacobi forms. ES's (K1′) normal form is such a quotient (F19).",
   "Bringmann–Ono-style methods give exact formulas/asymptotics for coefficients of mock objects; a sign-definite exact formula at prime indices would "
   "be ES-relevant.",
   "Match (K1′) of METAPLECTIC_ES with Zwegers' μ(u,v;τ) and compute its completion; check whether the nonholomorphic part is supported on squares (T1).",
   ["METAPLECTIC_ES.md"],
   ['F19', 'F08', 'mock-modular', 'appell-lerch', 'seen:METAPLECTIC_ES.md'], 'med', 'medium')
it("ES ⟺ every (4−n)/n is the Euler characteristic of a hyperbolic triangle orbifold S²(x,y,z)",
   "χ(S²(x,y,z)) = 1/x + 1/y + 1/z − 1, so ES(n) ⟺ some triangle orbifold has χ = (4 − n)/n, i.e. hyperbolic area 2π(n−4)/n (n ≥ 5). By "
   "Riemann–Hurwitz any finite quotient G of the triangle group acting on genus g satisfies |G|(n−4) = 2n(g−1).",
   "Imports the theory of triangle groups / quasiplatonic surfaces (genus spectra, Belyi maps) into ES; for n = p prime, p | |G| for every such G.",
   "Check whether 'which rationals are Euler characteristics of triangle orbifolds' appears in the orbifold literature, and test small p via "
   "tables of triangle groups with given area.",
   ["https://en.wikipedia.org/wiki/Triangle_group"],
   ['geometry', 'orbifolds', 'reformulation', 'F12', 'F14'], 'med', 'cheap')
it("Strong symmetric genus spectrum (May–Zimmerman: every value occurs) as a ∀g∃G sibling via triangle groups",
   "May–Zimmerman: there is a group of every strong symmetric genus. Proofs use explicit group families acting with triangle signatures; Riemann–"
   "Hurwitz ties genus to 1/x + 1/y + 1/z (see triangle-orbifold item). Shares F01, F12.",
   "A solved ∀∃ statement whose witness lives in the same unit-fraction equation (via Riemann–Hurwitz) — possibly a source of explicit families "
   "(x,y,z) with constrained 1/x+1/y+1/z.",
   "Read May–Zimmerman's construction and check which signatures (x,y,z) and areas arise; see if area (p−4)/p is ever forced.",
   ["https://www.semanticscholar.org/paper/6f5ab0589e1e1014cf6b2790e9b4407620c7f19d"],
   ['F01', 'F12', 'group-actions', 'riemann-surfaces'], 'low', 'cheap')
it("Hurwitz 84(g−1) / the spectrum of 1 − 1/x − 1/y − 1/z: gaps near 0 vs ES's values (n−4)/n",
   "The set {1 − 1/x − 1/y − 1/z} has the minimum positive value 1/42 and a well-studied accumulation structure (Hurwitz). ES asks whether every "
   "(n−4)/n belongs to {1 − Σ1/x_i} (n ≥ 5).",
   "The order structure of the triangle-group 'area spectrum' (it is well-ordered with known limit points) is classical; ES is a membership "
   "question for an explicit sequence in it.",
   "Compute the area spectrum up to denominator 10⁶ and its intersection with {(n−4)/n}; visualise where the hard n sit in the spectrum.",
   ["https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem"],
   ['F12', 'geometry', 'spectrum'], 'low', 'cheap')
it("Salez's modular filters (verification to 10¹⁷) as an explicit infinite covering family",
   "Salez found new modular equations (identity families) and used them as sieving filters to verify ES to 10¹⁷ (F23, F03, F34).",
   "The filters are a concrete enumerated set of 'lines'; their combined density deficit as a function of the number of filters is an explicit "
   "covering-rate curve to compare with the Poisson model.",
   "Extract Salez's filter list and compute the density of primes left uncovered by the first k filters for k up to 10³; fit the decay rate.",
   ["https://arxiv.org/abs/1406.6307", "https://arxiv.org/abs/2509.00128"],
   ['F23', 'F03', 'F34', 'computation', 'covering'], 'high', 'cheap')
it("Mihnea–Dumitru (2025) to 10¹⁸ with solution-count statistics — data for signature calibration",
   "Their verification reports per-n solution-count distributions (F23, F04).",
   "Independent count data to calibrate the log²p model against an outside source.",
   "Compare their reported count statistics with M_BM(p) predictions at matching heights.",
   ["https://arxiv.org/abs/2509.00128"],
   ['F23', 'F04', 'data'], 'high', 'cheap')
it("Lagrange's four squares: closure (Euler identity) + prime case by pigeonhole and descent — template for F02",
   "Four squares reduces to primes by a composition identity; the prime case is done by finding a multiple mp represented (pigeonhole) and "
   "descending m to 1. ES reduces to primes by trivial closure; the prime case has no descent.",
   "An ES descent ('from a solution of a structured 4/(mp)-type equation produce one with smaller m') would be a Lagrange-type proof.",
   "Search for an operation turning ES-type data at mp (e.g. a solution where m divides two of the denominators) into data at m'p with m' < m.",
   ["https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem", "seen:LONGSHOT_PIGEONHOLE.md"],
   ['F02', 'descent', 'pigeonhole', 'solved-sibling'], 'med', 'cheap')
it("Davenport–Lewis–Schinzel / Cassels–Pfister: polynomial-identity theorems for sums of squares ↔ Mordell–Schinzel for ES",
   "Characterisations of when f(t) is a sum of squares of polynomials (Cassels–Pfister) are the sums-of-squares analogue of 'no polynomial identity "
   "covers the square classes' (F09).",
   "Shows how polynomial-identity impossibility is proved by valuation/specialisation arguments; could give a uniform proof of F09 and its "
   "extensions (identities in two parameters, Gaussian coordinates).",
   "Re-prove Mordell–Schinzel's ES statement by a Cassels–Pfister-style specialisation at a square point and see what extra hypotheses would allow "
   "identities in (a,b) with p = a² + b².",
   ["https://en.wikipedia.org/wiki/Cassels%E2%80%93Pfister_theorem"],
   ['F09', 'identities', 'polynomial'], 'med', 'cheap')
it("Feature flip F13 (cubic → quadric): 4/n = 1/x + 1/y is a hyperbola — fully solved by divisors",
   "The 2-term equation is a split conic; its solvability is a divisor-in-class condition and fails on a positive-density set. ES adds one variable "
   "and becomes a cubic surface with hyperbola fibres (F15).",
   "Exactly measures what the extra dimension buys: from a single divisor condition (fails often) to a union over the fibre parameter (fails maybe never).",
   "Compute the density of primes failing the 2-term condition for 4/p − 1/x as x ranges over the first K admissible values; plot the decay in K.",
   [], ['F13', 'F15', 'feature-flip'], 'high', 'cheap')
it("Feature flip F14: weighted equation 4/p = 1/x + 1/y + 2/z is trivial — symmetry/unit numerators are load-bearing",
   "x = (p+3)/4 leaves 12/(p(p+3)) = 3/N with N = p(p+3)/4, and 3/N = 1/N + 2/N. Breaking the unit-numerator symmetry kills the problem.",
   "Confirms the difficulty sits in the symmetric unit-numerator structure (F12, F14) — any proof must use that all numerators are 1.",
   "List all weightings (a,b,c) with a+b+c small for which a/x + b/y + c/z = 4/p is trivially solvable; the first non-trivial weighting is a "
   "sub-problem ladder.",
   [], ['F14', 'F12', 'feature-flip', 'ladder'], 'high', 'cheap')
it("Feature flip F18: SL₂(ℤ) → SL₂(ℤ[i]) / Bianchi groups — Gaussian words for p ≡ 1 mod 4",
   "ES's SL₂ form asks for [[a,p],[c,d]] with congruence conditions. Over ℤ[i], p = ππ̄ splits; a Gaussian SL₂ version could split the problem into "
   "two conjugate halves.",
   "Hard primes split in ℤ[i] (F29); a formulation where the splitting is visible could separate T1-type obstructions (which concern rational squares) "
   "from the generic case.",
   "Write the SL₂(ℤ[i]) analogue with entry π and conditions mod (1+i)^k c; check whether norm maps produce ES matrices.",
   [], ['F18', 'F29', 'feature-flip', 'bianchi'], 'low', 'medium')
it("Feature flip F22: problems with the parity barrier broken by an extra algebraic structure (Friedlander–Iwaniec x² + y⁴, Heath-Brown x³ + 2y³)",
   "Thin-sequence prime counts became possible when the sequence had bilinear structure (Type II sums). ES's (★) word 4uBC − u − B is bilinear "
   "in (u,B) at fixed C.",
   "If the ES lower-bound problem can be phrased as a sieve problem over a thin bilinear set, Friedlander–Iwaniec-type Type II estimates are the "
   "relevant input — on average over p at least.",
   "Formulate 'p with R(p) = 0' as a sieve problem and check whether Type II information over (u,B) is available in the FI sense.",
   ["unverified: Friedlander, Iwaniec 1998, The polynomial X² + Y⁴ captures its primes (Annals 148)"],
   ['F22', 'bilinear', 'parity', 'feature-flip'], 'med', 'medium')
it("Feature flip F24: sub-problems where the heuristic predicts infinitely many failures (single lines) — calibrate the union",
   "Each single ES line (e.g. (★) at bounded C) fails infinitely often (e.g. when 4Cp+1 is prime); (★) overall fails at 14 primes ≤ 10¹⁰; the "
   "union never fails ≤ 10⁸.",
   "The transition 'infinitely many failures → finitely many → none' along the union is a measurable phase diagram; its rate is the key heuristic input.",
   "Plot, for unions of the first k lines (ordered by density), the count of failures ≤ X for X = 10⁶..10⁹; fit failure counts ~ X·exp(−c k).",
   ["PHASE_DIAGRAM.md"],
   ['F24', 'F34', 'feature-flip', 'phase-diagram', 'seen:PHASE_DIAGRAM.md'], 'high', 'cheap')
it("Feature flip F30: thin families proved via algebraic factorisation (Aurifeuillean, Sophie Germain) — catalogue other Aurifeuillean identities",
   "ES was proved on 3·2^s + 1, 7·4^s + 9, 63·2^s + 1 using factorisations like 4X⁴ + 1 = (2X²+2X+1)(2X²−2X+1). Aurifeuillean factorisations exist "
   "for b^n ± 1 for many b.",
   "Each Aurifeuillean identity is a candidate engine for a new proved thin family (open: 15·2^s + 1, 4^s + 297).",
   "List Aurifeuillean factorisations (b = 2, 3, 5, 6, 7) and test which p-tied integers 4Cp+1 for p = a·b^s + k factor algebraically.",
   ["https://en.wikipedia.org/wiki/Aurifeuillean_factorization"],
   ['F30', 'thin-families', 'factorisation', 'seen:FRONTIER.md'], 'high', 'cheap')
it("Feature flip F33: replace reciprocals by squares/cubes — 4/n = Σ 1/x_i² (Egyptian fractions with square denominators, Graham)",
   "Graham characterised which rationals are sums of distinct reciprocals of squares; 3-term versions with squares are sparse. ES with "
   "squared denominators breaks the hyperbola fibration.",
   "Clarifies which structural feature (linear unit fractions ⇒ divisor problems) ES needs; squares give norm-form problems instead.",
   "Check whether 'a/n = 1/x² + 1/y² + 1/z²' has a known local-global theory; record its obstruction set for small numerators.",
   ["unverified: Graham 1964, On finite sums of reciprocals of distinct nth powers (Pacific J. Math.)"],
   ['F33', 'F12', 'feature-flip'], 'low', 'cheap')
it("Feature flip F38: Markoff (quadratic in each variable ⇒ Vieta group) vs ES (multilinear ⇒ no Vieta) — what symmetry group does the ES cubic have?",
   "The ES surface 4xyz = n(xy+yz+zx) is multilinear; its automorphisms include S₃ and Cremona-type maps (x ↦ 1/x turns it into a plane "
   "1/x+1/y+1/z linear in reciprocals!). In reciprocal coordinates X = 1/x it is the plane X + Y + Z = 4/n.",
   "The integral-points problem is 'points of the plane X+Y+Z = 4/n with all coordinates unit fractions' — the symmetry group of the problem is the "
   "affine group of that plane preserving the unit-fraction lattice condition; a new angle on F38/F39.",
   "Determine the group of birational automorphisms of the ES surface over ℚ that preserve positivity and integrality for infinitely many n.",
   [], ['F38', 'F39', 'F13', 'symmetry', 'feature-flip'], 'med', 'cheap')
it("Feature flip F39: Stern–Brocot / Calkin–Wilf trees enumerate every rational exactly once — is there a tree enumerating ES words with p at a bounded depth?",
   "Universality of a tree enumeration is trivial for rationals; ES's word forest (F39) has connectivity results. A tree in which every prime appears "
   "within bounded depth would prove ES₅-type statements.",
   "Gives a combinatorial reformulation: bounded-depth covering in an explicit tree (like λ(p) ≤ 3 in the Euclid tree).",
   "Compute the depth of each hard prime in the Stern–Brocot-type tree generated by the ES₅ moves; check bounded depth up to 10⁸.",
   ["seen:FOREST_CONNECTIVITY.md"],
   ['F39', 'F17', 'trees', 'feature-flip'], 'med', 'cheap')
it("Feature flip F40: Goldbach's exceptional set has a power saving (Montgomery–Vaughan) — why ES's is stuck at exp(−c(log)^{3/4})",
   "Montgomery–Vaughan: E_Goldbach(N) ≪ N^{1−δ}. ES: E(N) ≪ N exp(−c(log N)^{3/4}) with 3/4 sharp for CRT sieves (F40). The difference: Goldbach "
   "counts are polynomial, ES counts polylog.",
   "A Montgomery–Vaughan-style argument needs a main term exceeding the error on average by a power; with polylog main terms one can expect at best "
   "quasi-polynomial savings — or there is a different route.",
   "Write the heuristic exceptional-set size predicted by the Poisson model (∑_n exp(−M(n))) and compare with N^{1−δ}: is a power saving even "
   "heuristically true for ES?",
   ["unverified: Montgomery, Vaughan 1975, The exceptional set in Goldbach's problem (Acta Arith. 27)"],
   ['F40', 'F05', 'feature-flip', 'exceptional-set'], 'high', 'cheap')
it("Heuristic exceptional-set size for ES and for (★) alone: Σ_n exp(−M(n)) vs. proved bounds",
   "Under the Poisson model with mean M(n) ≍ log²n the expected number of failures ≤ N is Σ exp(−c log²n) < ∞, while for single lines it diverges. "
   "Shares F24, F05, F40.",
   "Quantifies the 'distance' between the proved exceptional bound (N exp(−c(log N)^{3/4})) and the heuristic truth (O(1)).",
   "Compute Σ_{n≤N} exp(−M_BM(n)) numerically for N = 10⁸ with the measured zero-law constant; compare with observed (★) failure counts.",
   ["BM_CORRECTED_COUNT.md"],
   ['F24', 'F05', 'F40', 'heuristic'], 'med', 'cheap')
it("Positive-proportion pointwise lower bound: R(p) ≥ c·log²p for a positive proportion of primes (second-moment / Paley–Zygmund)",
   "From first and second moments of R(p) over p ≤ X, Paley–Zygmund gives R(p) ≥ ½E[R] on a positive proportion (F05w, F04).",
   "A clean, likely provable intermediate theorem with the right order of magnitude — the 'Romanoff' rung of ES.",
   "Check whether the second moment Σ_{p≤X} R(p)² ≪ X log⁴X is available (ET-type divisor-sum bounds) and write the Paley–Zygmund deduction.",
   ["SINGLE_P_COUNT.md"],
   ['F05', 'F04', 'second-moment', 'intermediate-theorem'], 'high', 'cheap')
it("Smallest-solution size statistics: max denominator of the best ES solution vs. p^θ",
   "ES witnesses have size ≤ poly(p) (F32). The distribution of the minimal possible max-denominator (or minimal level C) over hard primes is an "
   "observable comparable to 'least witness' problems (least nonresidue ≪ log², least prime in AP).",
   "If the least witness is always ≤ (log p)^A (in level coordinates) a bounded-search proof shape becomes plausible — B1 says no fixed bound "
   "works, but a log-power bound is untouched by B1.",
   "For hard primes ≤ 10⁹ record the minimal C with R_C(p) > 0 and minimal max(x,y,z)/p; fit against log p.",
   [], ['F32', 'F35', 'least-witness', 'data'], 'high', 'cheap')
it("Least prime in an arithmetic progression (Linnik's constant) as 'least witness' sibling for the minimal ES level",
   "Linnik: least prime ≡ a mod q is ≪ q^L. ES: least level C with a witness. Both are 'least witness' statements; Linnik's proof uses zero-density "
   "+ Deuring–Heilbronn (Siegel zero repulsion) — F21.",
   "Linnik's three principles (zero-free region, log-free zero density, exceptional-zero repulsion) are the canonical pointwise toolkit; their ES "
   "analogues for the family of characters χ_{−4uB} could be written down.",
   "Formulate a 'log-free zero density' statement for the family {χ_{−4uB}} that would imply min level C ≪ p^ε, and check what is known.",
   ["https://en.wikipedia.org/wiki/Linnik%27s_theorem"],
   ['F21', 'F20', 'least-witness', 'zero-density'], 'med', 'medium')
it("Feature flip F03: n ≡ 0, 2, 3 mod 4 and non-square classes mod 840 are covered by identities — what if the hard classes were non-squares?",
   "Mordell's identities cover every class except the six square classes mod 840 (F03, F08, F09). The squares are exactly the classes no polynomial "
   "family can reach — the reciprocity obstruction is the reason.",
   "Problems with a finite congruence covering of ALL classes are solved by identities; ES's residual set is forced to be the squares by reciprocity — "
   "the same reason as in Apollonian packings (HKRS).",
   "For moduli M = 840·ℓ (ℓ ≤ 50), confirm the set of uncovered classes stays 'squares mod M' and record the minimal identity degree needed per class.",
   ["seen:FRONTIER.md"],
   ['F03', 'F08', 'F09', 'feature-flip'], 'high', 'cheap')
it("Feature flip F31: Gauss's three-squares count r₃(n) ~ class number — a lattice count with a class-number main term",
   "r₃(n) = 12h(−4n)-type formulas give pointwise lower bounds via Siegel. If any ES count is (even partially) a class number, Siegel-type lower "
   "bounds apply (ineffectively).",
   "Search for a lattice/genus formulation where an ES sub-count equals a class number or a sum of class numbers of discriminants tied to p.",
   "Compute R(p) and Σ_{small D} h(−Dp) for hard primes ≤ 10⁶ and regress; any exact relation would be striking.",
   [], ['F31', 'class-numbers', 'feature-flip'], 'low', 'cheap')
it("Feature flip F11 downward: 3/n = 1/x + 1/y fails for p ≡ 1 mod 3 — the 'numerator = terms + 1' ladder starts with a genuine obstruction",
   "3/p as two unit fractions requires a divisor condition that fails for primes p ≡ 1 mod 3 (local-type obstruction), while 4/p in three terms has "
   "no local obstruction. m/n in m−1 terms: m = 3 fails, m = 4 is ES.",
   "Shows ES is the first rung where the obstruction disappears; the reason (one extra free parameter) is quantifiable.",
   "Verify the 3/p criterion and check m = 4 with 2 terms (4/p = 1/x + 1/y ⟺ p ≡ 3 mod 4) to complete the small ladder table.",
   [], ['F11', 'F12', 'feature-flip', 'ladder'], 'high', 'cheap')
it("Feature flip F28: Type III-like solutions for composite n (neither type, e.g. 4/9 = 1/4 + 1/6 + 1/36) — the T1-free channel at squares",
   "For n = m², Type I/II vanish (T1) but ES(m²) holds via solutions not of Type I/II (e.g. 4/9 = 1/4 + 1/6 + 1/36). Mixed-type solutions are the "
   "channel T1 does not see.",
   "Understanding how ES survives at squares (via factor m) clarifies why primes cannot use that channel and what a 'prime analogue' would be.",
   "Classify all ES solutions of 4/m² for odd m ≤ 101 by gcd pattern with m; check whether every one is a scaled solution of 4/d for d | m, d < m².",
   ["seen:FRONTIER.md"],
   ['F28', 'F08', 'feature-flip', 'squares'], 'high', 'cheap')
it("Feature flip F36: problems where GRH IS known to give the pointwise result (least nonresidue, Artin, Ramanujan's form) — common structure",
   "In each GRH-success case a single L-function (or bounded family) controls the event at the given n. ES's event needs a family of size ≍ p of "
   "characters χ_{−4uB} at once.",
   "Gives a structural criterion: count how many L-functions must be simultaneously controlled; ES needs too many for GRH-type explicit formulas.",
   "For each GRH-success sibling, record the number of L-functions and the conductor range used; tabulate vs ES.",
   [], ['F36', 'GRH', 'feature-flip', 'calibration'], 'med', 'cheap')
it("Feature flip F37: problems where a two-sided asymptotic for the pointwise count IS true (r₄(n) = 8σ*(n))",
   "Exact formulas (Jacobi) give two-sided control; ES provably has no two-sided polylog asymptotic (Linnik-type large values).",
   "Confirms that ES requires a one-sided method; methods built on exact formulas (Jacobi-type) cannot be complete for ES.",
   "List the exact formulae known for ES-like counts (theta-quotient normal form) and identify which term carries the Linnik large values.",
   [], ['F37', 'feature-flip'], 'med', 'cheap')
it("Feature flip F27 (cone): 4/n = 1/x + 1/y + 1/z with x,y,z ∈ ℤ_{≠0} and at most one negative — count grows polynomially",
   "Allowing one negative denominator turns the problem into an indefinite one with many solutions (count ≫ n^δ). The positive cone cuts it down "
   "to polylog.",
   "Counting solutions in sub-cones (e.g. one denominator 'barely negative') interpolates between trivial and ES; a continuity/sign-change argument "
   "across the cone boundary could be a route.",
   "Count signed solutions with |negative denominator| ≤ p^θ for hard p and see how the count decays as θ → 0.",
   [], ['F27', 'feature-flip', 'cone', 'interpolation'], 'med', 'cheap')
it("Hough/Erdős minimum-modulus theorem vs. ES's identities with growing moduli",
   "Hough: any covering system with distinct moduli has minimum modulus ≤ 10¹⁶. ES's Mordell identities form a congruence covering of non-square "
   "classes; the square classes require infinitely many 'lines' with growing moduli.",
   "The distortion method that proves Hough's theorem quantifies how much of ℤ distinct-moduli APs can cover — giving a lower bound on the uncovered "
   "set for any AP-based ES strategy (consistent with B1).",
   "Apply the BBMST criterion to the list of ES identity classes (moduli ≤ 10⁵) and compute the guaranteed uncovered density.",
   ["unverified: Balister, Bollobás, Morris, Sahasrabudhe, Tiba, The Erdős–Selfridge problem with square-free moduli / On the Erdős covering problem"],
   ['F03', 'F34', 'covering-systems'], 'med', 'cheap')
it("Pratt-certificate analogy: recursive ES certificates via factors of p-tied integers",
   "Pratt certificates for primality recurse on factors of p − 1. ES witnesses are divisors of p-tied integers (F10). A recursive scheme: a "
   "witness for p from 'witness-like data' for prime factors of 4Cp+1.",
   "Recursive certificate structures sometimes reveal inductive proofs (as for Pratt: every prime has a short certificate, by induction).",
   "For hard primes, record which prime factors q of 4Cp+1 'produce' the class −1 (q ≡ −1 mod 4C or products) and whether q's own ES data predict it.",
   [], ['F35', 'F32', 'F10', 'recursion'], 'low', 'cheap')
it("Every n > 1 has a divisor-pair structure: Dirichlet hyperbola method at fixed n as an ES lens",
   "Each ES hyperbola fibre (ay − b)(az − b) = b² counts divisors of b² in a class; summing over x is a hyperbola-method sum at fixed n (F15, F10).",
   "Hyperbola-method symmetries (d ↔ N/d) pair solutions; a 'symmetric half' count may be easier to bound below.",
   "Write the ES count as Σ_x #{d | (nx)² : d ≡ −nx mod (4x − n), d < nx} and check parity/symmetry under d ↔ (nx)²/d.",
   [], ['F15', 'F10', 'hyperbola-method'], 'med', 'cheap')
it("Additive energy of {1/x} and three-fold sums: Bourgain-type sum-product for reciprocals of integers ≤ N",
   "How many rationals of height ≤ H lie in {1/x + 1/y + 1/z}? Counting 3-fold reciprocal sums is a sum-product/energy question (F33).",
   "A lower bound showing the 3-fold reciprocal sumset hits a large fraction of rationals a/n with small numerator would be a density version of "
   "ES-type statements.",
   "Compute |{1/x+1/y+1/z : x,y,z ≤ N}| ∩ {4/n} for N up to 10⁴ and the energy of the reciprocal set.",
   [], ['F33', 'sum-product', 'additive-energy'], 'low', 'cheap')
it("Graph-theoretic reformulation: bipartite 'divisor graph' between levels C and primes p; ES ⟺ no isolated prime vertex",
   "Make a bipartite graph with an edge (C, p) when R_C(p) > 0. ES ⟺ every hard prime has degree ≥ 1. Degree distribution ≍ Poisson(log²p).",
   "Graph tools (expansion, Hall-type conditions, random-graph thresholds for isolated vertices) give a different language for the lower tail "
   "(F04, F24).",
   "Compute the bipartite graph for p ≤ 10⁷, C ≤ 10³; check the isolated-vertex threshold vs. random bipartite graphs with the same degree sequence.",
   [], ['F04', 'F24', 'random-graphs', 'reformulation'], 'med', 'cheap')
it("Sierpiński/Riesel numbers: k·2^n + 1 composite for all n via covering — a 'shifted integer always composite' phenomenon",
   "Covering congruences force k·2^n + 1 to be composite for all n. ES needs p-tied integers 4Cp + 1 to be composite WITH a divisor in a class; "
   "a covering forcing compositeness is a step in the right direction for a fixed p.",
   "If for each hard p a covering-type argument forced some 4Cp + 1 (C ≤ K) to have a SMALL prime factor q ≡ −1 mod 4C·…, a witness might follow "
   "(small prime factor in the right class ⇒ witness when cofactor class matches).",
   "For hard primes, find small primes q with q | 4Cp + 1 and q ≡ −1 (mod 4C) for some C < q (i.e. C ≡ −(4p)⁻¹ mod q with the class condition); "
   "count such (q, C) pairs with q ≤ log²p.",
   ["https://en.wikipedia.org/wiki/Sierpi%C5%84ski_number"],
   ['F10', 'covering-systems', 'small-prime-factor'], 'med', 'cheap')
it("Small-prime-factor witnesses: q | 4Cp + 1 with q ≡ −1 (mod 4C) is itself a witness (d = q)",
   "If a prime q ≡ −1 (mod 4C) divides 4Cp + 1 then the cofactor is ≡ −1 too (product ≡ 1), so d = q is a (★) witness. For each prime q and each "
   "C with 4C | q + 1, q | 4Cp + 1 is a single congruence on p mod q.",
   "So the set of p witnessed by (q, C) is one residue class mod q; ES ⟸ the classes {p ≡ −(4C)⁻¹ mod q : 4C | q+1} cover all hard primes — an "
   "infinite covering by single residue classes, one per (q, C) (F34). Note q ≥ 4C − 1, so q ≈ C scale.",
   "For each hard prime p ≤ 10⁸, find the least prime q such that some C with 4C | q + 1 satisfies q | 4Cp + 1; study the distribution of that q.",
   [], ['F10', 'F34', 'covering', 'new-angle'], 'high', 'cheap')

with open(OUT, 'w') as f:
    for k, d in enumerate(I, 1):
        d = dict(id=f'OWN2-{k:03d}', **d)
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print(len(I), 'items ->', OUT)
