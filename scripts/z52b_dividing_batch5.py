from z52b_dividing_lib import I

def B(title, conn, why, step, refs=(), tags=(), conf="med", effort="medium"):
    I(f"Between: {title}", conn, why, step, refs, ["in-between", *tags], conf, effort)

# ---- In-between problems whose resolution would be most informative for ES ----
B("does Crocker's construction extend to p + 2^a + 2^b + 2^c?",
  "Sun's three-powers conjecture (log² count, same as ES) vs Crocker's two-powers failure (log count). Resolution tells whether log² + no local obstruction can still fail i.o.",
  "If a Crocker-type family kills three powers too, the 'log² is safe' heuristic for ES loses its main support; if Crocker provably cannot extend, the reason is a candidate ES lemma.",
  "Reconstruct Crocker's family; for its members n compute r₃(n) = #{n = p + 2^a + 2^b + 2^c} up to n ≈ 2^64 with Miller–Rabin.",
  ["Crocker 1971", "arXiv:0901.3075"], ["count:log2", "twin-of-ES", "computation"], effort="medium")
B("Are all exceptions of p + 2^a + 2^b structured (Crocker-type) or are there 'random' ones?",
  "Pan proves ≫ x^{1−ε} exceptions; classify numerically the exceptions ≤ 10^9 by whether they lie in algebraic families.",
  "If log-count failures are always structured, then ES (log², and failures provably not AP-structured) gains heuristic support.",
  "Enumerate odd n ≤ 10^8 not of the form p + 2^a + 2^b; test membership in known families; look at residues mod small primes.",
  ["Pan 2011 (check)"], ["count:log", "exception-shape", "computation"], effort="medium")
B("Schinzel's N_m growth exponent", "Pomerance–Weingartner predict N'_m = exp(m^{1/2+o(1)}); proving any upper bound N_m < ∞ for one m ≥ 4 would be ES-strength.",
  "Locates ES (m = 4) on a curve; if exceptions at m = 8..15 follow the Poisson model precisely, the model's prediction 'no exceptions for m = 4' is calibrated.",
  "Fit observed largest exceptions (PW table: m=8: 241; m=12: 12241; m=15: 20521) against exp(c·m^{1/2}) and against (log p)³/m ≈ const.",
  ["arXiv:2511.16817", "Pomerance slides 2026"], ["family-crossing-line", "egyptian", "computation"], conf="high", effort="cheap")
B("Why is m = 12 so exceptional in the Pomerance–Weingartner table?",
  "m = 12 has 24 exceptions up to 10^12 vs 9 for m = 10 and 13 for m = 13; the count per m should correlate with an arithmetic singular series (structure of (ℤ/m)^× and −1).",
  "An 'ES singular series' S(m, n) that predicts the m-dependence would be the right object to bound below at m = 4.",
  "Compute heuristic expected counts E_m(p) = Σ_{Type I/II shapes} densities for m = 4..15 and correlate with exception counts.",
  ["Pomerance slides 2026"], ["egyptian", "singular-series", "computation"], conf="high", effort="cheap")
B("Markoff-type surfaces: non-BM Hasse failures explained by reduction theory",
  "Ghosh–Sarnak find infinitely many k with local points but no integral points, beyond Brauer–Manin; mechanism: Vieta-group fundamental domain is small/empty.",
  "ES is integral points on an affine cubic surface with no BM obstruction; a non-BM failure mechanism of reduction type is the most plausible disproof shape.",
  "Ask whether the ES surface has any infinite group of birational automorphisms preserving integral points (analogue of Vieta moves); if not, record the asymmetry.",
  ["arXiv:1706.06712", "MARKOFF_ES.md"], ["integral-points", "disproof-route", "seen:MARKOFF_ES.md"])
B("Sums of three cubes: any non-local, non-BM failure?",
  "If some k ≢ ±4 mod 9 provably had no representation, that would be the first integral Hasse failure on a cubic surface without BM — directly ES-relevant.",
  "Calibrates the plausibility of ES failing despite no BM.",
  "Literature check: 'integral points three cubes Hasse principle failure' (Colliot-Thélène–Wittenberg, Siksek).",
  ["Colliot-Thélène–Wittenberg 2012"], ["integral-points"], conf="high", effort="cheap")
B("U(n) sporadic list finiteness", "U(n) fails at odd squares + {105, 2961, 3985, 25305, 111969, 978145}; is the sporadic list finite and what governs it?",
  "A 'squares + finitely many sporadic' theorem for U(n) would be the ES-adjacent analogue of Rickards–Stange.",
  "Check whether sporadic values share a factor pattern (105 = 3·5·7, 2961 = 3·987=3·3·7·47 …) and compute class numbers / Legendre symbols to see a governing invariant.",
  ["FRONTIER.md"], ["sporadic", "computation"], conf="high", effort="cheap")
B("ES over rings of integers O_K with total positivity", "Define ES_K: 4/ν = 1/ξ + 1/η + 1/ζ with totally positive ξ, η, ζ ∈ O_K. Does it fail for some K (e.g. Q(√2), Q(√5))?",
  "If ES_K fails for a real quadratic K, the failing mechanism (units? positivity at two places?) is a candidate obstruction for ES itself; if it holds via the same covering identities, it's a calibration.",
  "Search ES_K for K = Q(√2), Q(√5) for small totally positive primes ν with a bounded-height search.",
  [], ["number-field", "computation"], conf="med", effort="medium")
B("Smooth-denominator ES", "Require x, y, z to be y-smooth (y = (log p)^A). The count drops with A; find the A where failures start.",
  "Gives a tunable count family inside ES; the critical A tells how much 'slack' ES has.",
  "Compute for p ≤ 10^6 the minimal smoothness bound of the best solution; fit vs log p.",
  [], ["family-crossing-line", "computation"], effort="cheap")
B("ES with a prime denominator", "Require one of x, y, z to be prime. Expected count ≈ log² p / log p ≈ log p — a Crocker-scale count inside ES.",
  "If ES-with-prime-denominator fails infinitely often in a structured family, the structure is informative; if it holds to 10^9 that is evidence log-count can hold here.",
  "Search p ≡ 1 mod 24 ≤ 10^7 for representations 4/p = 1/x + 1/y + 1/z with z (or x) prime; list failures.",
  [], ["count:log", "computation", "restriction"], effort="cheap")
B("ES with the minimal denominator bounded: x ≤ p/4 + p^θ", "Linnik-constant analogue: max over p of minimal admissible window.",
  "If the minimal x always lies in a short window, ES becomes a bounded search (Π₁ → decidable per p with explicit bound).",
  "Compute max_{p ≤ 10^9} (x_min(p) − ⌈p/4⌉)/log² p and fit.", [], ["linnik-constant", "computation"], effort="cheap")
B("Explicit (deterministic) thin additive basis with r(n) ≍ log n",
  "Erdős's construction is probabilistic; check whether an explicit construction with r(n) ≍ log n is known (Kolountzakis gave algorithmic constructions; Jain 2024 discusses open aspects).",
  "ES = 'a deterministic log²-count system covers every prime'. Whether explicit log-count bases can be certified is the purest derandomisation analogue.",
  "Check whether explicit/derandomised constructions with r(n) ≍ log n exist (search Kolountzakis 1995; arXiv:2405.08650).",
  ["arXiv:2405.08650"], ["derandomisation", "mech:probabilistic"], effort="cheap")
B("Hensley alphabet at critical dimension δ_A = 1/2",
  "Thin-orbit CF problems at exactly the critical exponent have count ≍ polylog — the closest SL₂ analogue of ES₅.",
  "Results (or failures) at δ = 1/2 would tell whether polylog-count thin-orbit statements can be pointwise.",
  "Search literature for 'critical dimension 1/2 Zaremba' and compute denominators covered for an alphabet tuned to δ ≈ 1/2.",
  ["Bourgain–Kontorovich 2014"], ["critical-exponent", "continued-fractions"], effort="medium")
B("Goldbach's other conjecture finiteness (p + 2k²)", "Are 5777 and 5993 the only failures?", "Power count; a proof of finiteness would show how sporadic failures are handled when count is power — template for U(n).",
  "None beyond literature check.", [], ["sporadic"], conf="high", effort="cheap")
B("Ternary Egyptian for numerators m with all denominators in an AP", "4/n = 1/x + 1/y + 1/z with x,y,z ≡ r mod q: local obstructions appear; which (q,r) still look universal?",
  "Maps local obstructions vs global failures in a controlled family.", "Compute for q ≤ 12 the residues r for which all n ≤ 10^6 coprime to stuff are solvable.",
  [], ["egyptian", "family-crossing-line", "computation"], effort="cheap")
B("Erdős's log log b terms conjecture", "Every a/b with ≪ log log b terms; Vose gives √log b.", "Uniform bounded-term phenomena for general a; ES is a = 4 with 3 terms.",
  "Read Vose 1985 and Tenenbaum–Yokota; check whether their methods give O(1) terms for 4/p on a density-one set (known anyway) or something new.", ["Vose 1985"], ["egyptian"], effort="cheap")
B("Integral points on log K3 surfaces via fibrations (Harpaz)", "Harpaz proved integral Hasse/BM results for some log K3 surfaces using fibration methods conditionally on Schinzel-type inputs.",
  "The ES affine surface may be log-K3 or log-general-type; Harpaz-type conditional theorems would give conditional ES-type statements.",
  "Determine the log Kodaira dimension of the ES affine surface (complement of the boundary in the cubic surface) and check whether Harpaz's framework applies.",
  ["Harpaz, 'Integral points on conic log K3 surfaces' (check)"], ["integral-points", "mech:fibration-method"], conf="med", effort="medium")
B("Positive-proportion vs almost-all for m/n with fixed large m at moderate n", "PW show 'mostly false' near exp(m^{1/3}); is there a regime where density is strictly between 0 and 1 provably?",
  "A proved intermediate regime would show where the Poisson model is accurate; ES sits in the 'always' regime.", "Read arXiv:2511.16817 for lower bounds on solvable primes.",
  ["arXiv:2511.16817"], ["family-crossing-line", "egyptian"], effort="cheap")
B("ES with x, y, z pairwise coprime-to-p structure (Type I only / Type II only)", "Is every p solvable by Type I alone? by Type II alone?",
  "If one type alone fails for some p, ES's robustness depends on two independent mechanisms — an interesting structural fact.",
  "Compute R_I(p), R_II(p) separately for p ≡ 1 mod 24 ≤ 10^8; list p with R_I = 0 or R_II = 0.", [], ["computation", "type-I-II"], conf="high", effort="cheap")
B("ES restricted to one certificate family per p-class (Mordell-style) with growing modulus", "Mordell's covering of non-square classes uses fixed moduli; with growing moduli (one new modulus per scale) does the proportion of uncovered primes go to 0 at a rate?",
  "Measures how fast the 'identity' approach degrades; (J)10 growing-level loophole.", "Compute uncovered proportion of primes ≤ x by identities of level ≤ L as L grows.",
  ["ES_APPROACH_GENERATORS.md"], ["growing-level", "computation"], effort="cheap")

# ---- Additional dividing-line features ----
def F(feature, has, supply, why, first_step, refs=(), tags=(), conf="med", effort="medium"):
    I(f"Feature: {feature}", f"Dividing-line feature '{feature}'. ES {has}. To supply it one could: {supply}",
      why, first_step, refs, ["feature", *tags], conf, effort)

F("ES as an infinite covering of primes by arithmetic progressions", "IS exactly this: ES(p) ⟺ p lies in some AP −f mod 4ad (f | 4a²d+1) or a Type II AP",
  "study the AP system {−f mod 4ad} as a covering problem: covering theory (Hough's distortion method, Balister et al.) bounds what finite subsystems can do; the infinite system's density Σ 1/φ(4ad)·#f diverges",
  "Covering-system technology decides p + 2^k (failure); ES is the dual 'must cover' statement — the same technology might show that an infinite system with divergent density and specific structure covers all primes.",
  "Search literature for 'infinite covering systems primes divergent sum of reciprocals' and for Hough/Balister lemmas about uncovered sets under divergent density.",
  ["Hough Ann. Math. 2015"], ["mech:covering-system", "dual-covering"], effort="medium")
F("two independent witness mechanisms (Type I and Type II)", "HAS two (p divides one vs two denominators)",
  "prove they are negatively correlated as failure events (if Type I fails because factors of many 4Cp+1 avoid −1, Type II must succeed) — a 'dichotomy' proof",
  "Dichotomy proofs (Siegel-zero dichotomy, Heath-Brown's Artin) convert two weak mechanisms into a pointwise result.",
  "Compute correlation between R_I(p) and R_II(p) over p ≡ 1 mod 24; negative correlation is a lead.",
  [], ["dichotomy", "type-I-II", "computation"], effort="cheap")
F("witness = divisor in a class (multiplicative) rather than prime value (additive)", "HAS multiplicative witnesses; parity barrier is not obviously relevant",
  "use multiplicative-function machinery (Halász, Matomäki–Radziwiłł) on indicator-type functions of 'has a divisor ≡ −1 mod 4C'",
  "Problems with prime-valued witnesses hit the parity barrier; divisor-in-class problems are governed by Stewart-type subgroup criteria instead.",
  "Express 1[N has a divisor ≡ −1 mod q] in terms of characters of (ℤ/q)^× via the subgroup criterion and check if Halász-type bounds apply when N runs over 4Cp+1, C ≤ X.",
  [], ["mech:multiplicative-functions", "parity"], conf="med")
F("exception set closed under a natural operation", "ES exceptions (if any) are closed under nothing obvious; solvable set is closed under multiples",
  "find an operation T on primes (e.g. p ↦ prime factor of some f(p)) with ES(T(p)) ⇒ ES(p); then descent along T",
  "Descent proofs need such operations (Fermat's descent from p | x²+y² to smaller primes).",
  "Search for identities: 4/p solvable if 4/q solvable for some q | (p + k) with structured k — test numerically which small-q solutions lift.",
  [], ["mech:descent", "computation"], conf="med")
F("Linnik-constant bound (smallest witness ≤ n^A)", "UNKNOWN for ES; known witnesses are small in practice",
  "prove a conditional (GRH) bound on the smallest certificate parameter, turning ES into a finite check per p",
  "Least-witness theorems (Linnik, Bach) are among the few pointwise polylog results, though conditional.",
  "Compute max over p ≤ 10^9 of the minimal Type I parameter a·d (or C) and compare with log² p.", [], ["linnik-constant", "computation"], effort="cheap")
F("height growth / Baker-type forcing", "LACKS (no linear forms in logarithms appear)",
  "seek a formulation where nonexistence of an ES certificate forces a very good rational approximation or a small linear form in logs, contradicting Baker",
  "Primitive divisors (BHV), Catalan-type results use Baker-type lower bounds to force existence of divisors.",
  "Ask: if every 4Cp+1 (C ≤ X) has all prime factors in a subgroup H_C avoiding −1, is there an associated multiplicative relation among small primes that Baker could forbid?",
  [], ["mech:baker"], conf="low", effort="big")
F("Galois-theoretic forcing of divisor classes (cyclotomic/Lucas)", "LACKS: ES needs divisors ≡ −1 mod 4C of linear forms, which no cyclotomic structure forces",
  "use Lucas sequences U_n(P,Q) with discriminant D: primitive divisors r of U_n satisfy r ≡ (D/r) mod n, so negative D gives r ≡ −1 mod n for inert r — choose (P,Q) depending on p",
  "Zsigmondy/BHV force divisors in classes ±1 mod n; a −1 mod 4C class appears naturally for inert primes.",
  "Construct for given p a Lucas sequence whose n-th term equals (or divides) 4Cp+1 or a related ES integer; check whether its primitive divisors can be forced inert.",
  ["Bilu–Hanrot–Voutier 2001"], ["mech:zsigmondy", "divisor-in-class", "lucas"], conf="med", effort="medium")
F("algebraic factorisation of the auxiliary integer (Aurifeuillian)", "HAS at squares (T1-type identities) and nowhere else known",
  "classify all polynomial families of n for which the auxiliary integers 4Cn+1 factor algebraically; each family is a candidate thin exceptional set or a solved family",
  "Sierpiński numbers with partial algebraic factorisations and Hardy–Littlewood H at squares show algebraic factorisation is a failure (or success) mechanism.",
  "For n = m², m³, m²+1, … compute whether 4Cn+1 factors as polynomials in m for some C(m) and whether the factors land in the ES class.",
  [], ["mech:algebraic-factorisation", "T1-analogue", "computation"], conf="med", effort="cheap")
F("self-reducibility to smaller instances", "HAS ES(n) ⇐ ES(prime factor) (downward), LACKS upward/sideways reductions among primes",
  "find 'sibling' implications ES(q) ⇒ ES(p) for q related to p (e.g. q | 4p + 1)", "Inductive proofs need sideways reductions; four-squares uses n ↦ prime factors and composition.",
  "Test numerically: is there a rule mapping each p to a smaller prime q with ES(q)'s solution transforming into ES(p)'s? (SIBLING.md)", ["SIBLING.md"], ["mech:descent", "seen:SIBLING.md"], conf="med")
