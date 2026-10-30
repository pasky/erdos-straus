from z52b_dividing_lib import C, I

# ---- Results of the two cheap computations run in this lane (EVIDENCE, not proofs) ----
I("Result: CRT avoidance density of ES certificate families decays like exp(−c (ln X)³), c ≈ 0.028",
  "Fraction δ(X) of residues in Mordell's hard classes (prime-like) that avoid every Type I family (p ≡ −f mod 4ad, f | 4a²d+1) and Type II family (p ≡ −e mod 4ab, e | a+b) with ad, ab ≤ X: δ(100) = 7.8e-2, δ(1000) = 1.2e-4, δ(1778) = 9e-6; ln δ/(ln X)³ ≈ 0.025–0.030 stable over X = 56..1778 (2·10⁶ samples).",
  "This is exactly the Poisson/independence prediction (expected number of hitting families ~ (log X)³, matching Pomerance–Weingartner's (log p)³/m scaling): ES's certificate families behave like independent events at the level of residues. EVIDENCE only; Chebotarev makes δ(X) the exact density of primes unsolved by families ≤ X.",
  "Extend to X = 10⁴ with 10⁸ samples (vectorised, memory-bounded) to test whether the exponent 3 persists or creeps.",
  ["scripts/z52b_dividing_avoid.py", "data/z52b/dividing_avoid_X3000.txt", "arXiv:2511.16817"],
  ["result", "computation", "heuristic-model", "dual-covering", "EVIDENCE"], "high", "cheap")
I("Result: least certificate-family size s(p) has a p-independent distribution (median 22, 99% ≤ ~200) and the CRT model predicts its maximum",
  "For all 179 468 hard-class primes p < 10⁸ the least s = ad (Type I) or ab (Type II) solving p has median 22, 90% quantile 86, 99% quantile 209 — identical to the < 10⁷ sample (22, 85, 187). The max over p < 10⁷ is 1133 (model n·δ(X) = 1 predicts ≈ 1210); over p < 10⁸ it is 2814 at p = 53049049 (model ≈ 1990, next-largest 1467).",
  "Quantifies 'how far' one must search per prime and shows the independence model is calibrated on the extreme-value statistic, not only on averages. EVIDENCE only.",
  "Push to 10⁹ (≈ 1.6·10⁶ hard primes, model predicts max ≈ 3·10³) and check the record-setters for near-square structure (cf. NEAR_SQUARE.md).",
  ["scripts/z52b_dividing_leastfam.py", "data/z52b/dividing_leastfam.txt"], ["result", "computation", "linnik-constant", "EVIDENCE"], "high", "cheap")
I("Prediction: least ES family size grows like exp((ln x / c)^{1/3}) — super-polylog, sub-power",
  "If δ(X) ≈ exp(−c (ln X)³), the largest least-family size among hard primes ≤ x is ≈ exp((ln π_hard(x)/c)^{1/3}) ≈ exp(((ln x)/c)^{1/3}): about 5·10⁴ at x = 10¹⁸. This matches the shape of H4_NOT_POLYLOG.md's proven lower bounds exp((log p)^κ), κ < 1/12 (κ < 1/6 relative to (G)), and suggests κ = 1/3 is the true exponent (for this coordinate).",
  "Gives a concrete conjectural Linnik-constant law for ES and an explicit target for the proven-lower-bound programme (raise κ towards 1/3) and for any upper bound (which would be ES-strength).",
  "Compare with the Salez / Mihnea–Dumitru verification data to 10¹⁸ if family sizes are recorded there; check whether the H4 coordinate and s(p) are comparable.",
  ["H4_NOT_POLYLOG.md", "data/z52b/dividing_avoid_X3000.txt"], ["prediction", "linnik-constant", "heuristic-model", "seen:H4_NOT_POLYLOG.md"], "med", "cheap")
I("Dividing-line reading of the computation: ES is a 'random covering' with log³ intensity, Crocker's problem a 'random covering' with log intensity",
  "In the residue model, ES's hit intensity grows like (log X)³ (families up to X), so failures become rarer than any power of X; p + 2^a + 2^b has intensity ≈ log n, giving failure probability ≈ n^{−c}, compatible with infinitely many structured failures.",
  "Places ES and Crocker's problem on one axis (intensity growth) where ES is comfortably on the 'all n' side, provided independence holds; the open question is only correlation/structure.",
  "Compute the analogous residue-model intensity for p + 2^a + 2^b + 2^c (expected log²) to complete the axis.", ["Crocker 1971"], ["heuristic-model", "count:log3", "minimal-pair"], "med", "cheap")
I("Records of least family size: are record-setting primes near squares?",
  "Record primes (830041, 7155121, 7183201, 53049049) are not squares; 830041 = 911² + 120, 7183201 = 2680² + 801. T1 makes certificate lines empty at squares — near-square primes might inherit difficulty.",
  "If records concentrate near squares, the T1 shadow governs the tail and the right model is 'random covering conditioned on distance to squares'.",
  "For hard primes < 10⁸, regress least s(p) on log(distance to nearest square)/log p.", ["NEAR_SQUARE.md"], ["computation", "T1-analogue", "seen:NEAR_SQUARE.md"], "med", "cheap")

# ---- More catalog / connections to round out ----
C("Primes p with p = x² + y² and x prime (Fouvry–Iwaniec)", "≍ √p/log p", "none", "proved infinitely many (Fouvry–Iwaniec 1997)", "bilinear forms over Gaussian integers",
  "Thin restriction on a two-squares representation still provable in the family aspect; not pointwise.", "None.", [], ["outcome:proved-family", "mech:bilinear"], conf="high")
C("Gaussian primes in narrow sectors / Hecke Größencharaktere", "power", "none", "proved for sectors of power width", "Hecke L-functions", "Angular equidistribution — ES Gaussian liftings would need sector control.", "None.", [], ["outcome:proved", "gaussian"], conf="med")
C("Least prime p ≡ 1 mod q with additional splitting (Chebotarev least prime, Lagarias–Odlyzko)", "power of discriminant", "none", "proved (bounds ≪ d^{C})", "zero-free regions", "Least-witness in growing fields; ES's growing-level union is a union of such Chebotarev conditions.", "None.", [], ["outcome:proved", "least-witness", "growing-level"], conf="high")
I("Connection: ES ⟺ Frobenius of p lies in a union of Chebotarev sets of growing level — least-prime-in-Chebotarev theory in reverse",
  "Each certificate family is a Chebotarev condition in Q(ζ_{4ad}) (splitting/residue condition). ES says Frob_p always lands in the union over all levels. Least-prime results answer 'is the first prime in a fixed Chebotarev set small?'; ES asks 'is every prime in the union of growing sets?'.",
  "A 'reverse Chebotarev covering' framing makes the dividing feature precise: unions over growing level with total density → 1 at rate exp(−c log³ X).",
  "Search for theorems of the form 'every prime p lies in some Chebotarev set C_L with L ≤ f(p)' for natural families (e.g. every p splits completely in some field of a family).", [], ["mech:chebotarev", "growing-level", "dual-covering"], "med", "medium")
I("Connection: 'every prime splits in some member of a family of fields' problems",
  "Examples: every prime p is ≡ 1 mod some small prime ℓ (trivial), every p is a QNR mod some small ℓ (least non-residue), every p splits in some Q(√d) with d small (least QR prime). ES is a non-abelian-free but class-valued version.",
  "These 'some member of a family' problems are proved pointwise exactly when the family has a forced member (Burgess / pigeonhole); identifying the forced member is the crux.",
  "List such problems with their least-witness bounds and check which have unconditional polylog/power bounds.", [], ["least-witness", "mech:character-sum"], "high", "cheap")
I("Connection: Erdős–Hall 'every n has a divisor ≡ −1 mod m for some small m'-type statements",
  "Stewart's criterion makes 'n has a divisor ≡ −1 mod m' central. Ask the pointwise question 'for every n ≡ 1 mod 4p…'; the analogous unconditional results for integers in APs are about divisors in residue classes (Erdős–Hall, Hall–Tenenbaum).",
  "Divisor-in-class problems for individual integers are typically almost-all; pointwise results need structure (e.g. n has many prime factors).", "Literature check: 'divisors in residue classes Hall Tenenbaum individual integers'.", [], ["divisor-in-class", "literature"], "med", "cheap")
I("Connection: Erdős's multiplication-table / divisor-in-interval as obstruction to ES Type II sizes",
  "Type II needs e | a+b with 4ab | p+e — divisibility plus size constraints; Ford's multiplication-table theory gives the density of integers with divisors in intervals, which bounds Type II counts.",
  "Explains why counts are log-power and not power: integers with structured divisors are rare (Ford's (log)^{−0.086} factor).", "Check Elsholtz–Tao's use of divisor-sum bounds and whether Ford-type exponents appear in ES lower-tail estimates.", ["Ford Ann. Math. 2008"], ["mech:divisor-distribution"], "med", "cheap")
I("Connection: sum-product phenomena mod q for 'p ≡ −e mod 4ab, e | a+b'",
  "Type II couples a product (4ab) with a sum (a+b) through divisibility; sum-product estimates force mixed sets to cover residues, but the problem's residue question is trivial locally — the content is integrality and size.",
  "Records that sum-product tools address local covering (already free for ES) — a dividing-line non-feature.", "None; note only.", [], ["non-feature", "additive-combinatorics"], "med", "cheap")
I("Connection: the 'Ramsey/colouring' version of ES (Erdős–Graham style) is likely easy",
  "Ask: in any finite colouring of primes, is there a monochromatic structure solving 4/p = 1/x+1/y+1/z with x,y,z in prescribed colours? Colouring versions of unit-fraction problems (Croot) are abundance-type and provable.",
  "Shows how quickly relaxations move to the proved side; useful to calibrate which relaxations are informative.", "None.", ["Croot 2003"], ["relaxation", "egyptian"], "med", "cheap")
I("Connection: ES with 'one denominator a prime power of p' only (x = p^k·u)",
  "Restricting which denominators carry p changes the family set (Type I vs II). Pure Type I or pure Type II counts are each ≍ log³-intensity in the residue model?",
  "If one type alone has intensity growing fast enough, ES could in principle be proved within one type; the computation can split intensities by type.", "Modify scripts/z52b_dividing_avoid.py to run Type I only and Type II only; fit exponents separately.",
  ["scripts/z52b_dividing_avoid.py"], ["type-I-II", "computation"], "high", "cheap")
I("Connection: correlation between families measured by survivor statistics",
  "In the residue model, families are independent if δ(X) equals ∏(1 − density of family). Comparing the observed δ(X) with the independent product quantifies correlation exactly (no primes needed).",
  "Correlation is the one unknown dividing-line coordinate for ES; this is a direct, cheap measurement.", "Compute ∏_{families ≤ X}(1 − |res|/φ(m)·…) (careful with non-unit residues) vs observed δ(X).",
  ["scripts/z52b_dividing_avoid.py"], ["correlation", "computation"], "high", "cheap")
I("Connection: the m/p family in the residue model",
  "Run the same CRT-avoidance computation for m = 5..15 (Type I: f | m a² d + 1, m a d | p + f; Type II: e | a+b, m a b | p + e) and compare δ_m(X) with PW's exception tables.",
  "If δ_m(X) predicts the observed largest exceptions for m = 8..15 (e.g. 241 for m = 8), the residue model is validated on cases with actual failures — the strongest available heuristic check for m = 4.",
  "Parametrise scripts/z52b_dividing_avoid.py by m; note PW's exceptions are for all n, not just primes.", ["arXiv:2511.16817", "Pomerance slides 2026"], ["family-crossing-line", "computation", "heuristic-model"], "high", "cheap")
I("Connection: residue model vs actual primes — the only gap is size, not residue",
  "Type I/II parametrisations have no size constraint (Pomerance slides): the residue model is EXACT for each fixed family set. ES ⟺ no prime survives all families; the gap between the model and ES is that X must grow with p (and Chebotarev error terms in level ≈ exp((log p)^{1/3})).",
  "Reformulates ES as a uniform Chebotarev/sieve problem at level exp((log p)^{1/3+ε}): far below power level, where Bombieri–Vinogradov-type averages are strong — but needed pointwise for one p.",
  "Check: is there any pointwise result 'every prime p avoids a sieve of level L = exp((log p)^θ) only if p is in an explicit thin set'? (Least-witness theory for sieves.)", [], ["sieve", "growing-level", "reformulation"], "med", "medium")
I("Connection: Large-sieve dual — primes surviving ES families form a sifted set; Gallagher's larger sieve bounds it",
  "Vaughan's exceptional-set bound is a large-sieve bound on primes avoiding many residue classes; the residue-model intensity log³ suggests the optimal exceptional bound x·exp(−c (log x)^{?}).",
  "Comparing the residue model with Vaughan's exp(−c log^{2/3} x) shows how far known methods are from the model.", "Derive the model's exceptional-set prediction: #{p ≤ x unsolved by families ≤ X(x)} ≈ π(x)·δ(X); optimise X under level-of-distribution constraints.",
  ["Vaughan 1970"], ["mech:large-sieve", "heuristic-model"], "med", "cheap")
