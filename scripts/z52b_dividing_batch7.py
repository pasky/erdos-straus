from z52b_dividing_lib import C, I

# ---- Catalog part 6 ----
C("Pomerance–Weingartner explicit: for m ≥ 6.52·10^9 some prime p ∈ (m², 2m²) has m/p not a sum of 3 unit fractions", "≈ (log p)³/m ≪ 1 at p ≈ m²",
  "none local; count too small", "proved (explicit), numerically supported already for m ≥ 20", "Brun–Titchmarsh upper bound on solvable primes",
  "A proved failure statement for the ES family purely from count deficit, showing the 'count too small ⇒ failure' side is provable; the 'count large ⇒ success' side is the open one.",
  "Find the smallest m for which numerics show failures in (m², 2m²) and compare predicted vs observed failure fraction.",
  ["arXiv:2511.16817"], ["outcome:false-io", "count:small", "egyptian", "family-crossing-line"])
C("Pomerance–Weingartner j-unit-fraction generalisation", "≈ (log p)^{2j−3}/m-type (check)", "none", "proved generalisation of the exception bound to j terms (per abstract)",
  "Elsholtz–Tao-style counting", "Two-parameter (m, j) family; ES at (4, 3).", "Read the j-term section of arXiv:2511.16817 and extract the predicted transition curve in (m, j).",
  ["arXiv:2511.16817"], ["egyptian", "family-crossing-line"], conf="med")
C("Every large odd n = prime + practical number (Pomerance–Weingartner, Margenstern's conjecture)", "large (practical numbers ≍ x/log x)", "none",
  "proved for large odd n (arXiv:2007.11062)", "distribution of practical shifted primes + sieve",
  "Practical numbers are Egyptian-fraction-friendly; a Goldbach-type pointwise theorem with a log-thin witness set is provable because the set has density x/log x.",
  "Look for an ES reformulation with 'practical' or 'smooth-divisor-rich' auxiliary integers (if p + k is practical with suitable divisors, a certificate exists?).",
  ["arXiv:2007.11062"], ["outcome:proved-large", "egyptian", "mech:sieve"])
C("Breusch–Stewart: rationals with odd denominator have Egyptian expansions with odd denominators", "—", "parity restriction necessary", "proved",
  "explicit construction", "Parity-restricted Egyptian expansions exist without bounded length; with bounded length (3 terms) odd denominators are impossible for 4/n.",
  "None.", [], ["outcome:proved", "egyptian"], conf="high")
C("Graham: rationals as sums of distinct reciprocals of squares (e.g. in [0, π²/6 − 1) ∪ …)", "—", "interval obstructions", "proved (Graham 1964)",
  "Graham's general theorem on Egyptian expansions with denominators in a set", "Unbounded-term Egyptian problems are decided by Graham's general theorem; bounded-term ones are not.",
  "None.", ["Graham 1964 (check exact statement)"], ["outcome:proved", "egyptian"], conf="med")
C("Hardy–Littlewood second conjecture π(x+y) ≤ π(x) + π(y)", "—", "—", "incompatible with prime k-tuples (Hensley–Richards 1973)", "admissible dense tuples",
  "Plausible numerically, but structurally false under a stronger conjecture — calibrates that ES numerics to 10^18 constrain only 'random' failure mechanisms.",
  "None.", [], ["outcome:likely-false", "calibration-numerics"], conf="high")
C("π(x) < li(x)", "—", "—", "false (Littlewood 1914); first crossing beyond 10^19-ish (Skewes bounds)", "zeta zeros", "Calibration of numerics.", "None.", [], ["outcome:false", "calibration-numerics"])
C("Dirichlet's theorem on primes in APs", "x/(φ(q) log x)", "local (gcd)", "proved", "L(1, χ) ≠ 0", "Existence from nonvanishing of an L-value: does ES have an L-value whose nonvanishing would force a certificate?",
  "Look for a Dirichlet series D_p(s) = Σ_C w(C, p) C^{−s} encoding certificates whose analytic behaviour at s = 1 detects existence.", [], ["outcome:proved", "mech:L-nonvanishing"], conf="high")
C("Chebotarev density theorem", "positive density", "—", "proved", "Artin L-functions", "Splitting conditions are governed by Chebotarev; ES Type I conditions at fixed (a,d) are splitting conditions in a fixed abelian field.",
  "Make explicit: Type I at (a,d) ⟺ Frob_p in a specified subset of Gal(Q(ζ_{4ad}, …)/Q); ES ⟺ Frob_p hits the union over (a,d) — a 'growing Chebotarev' covering.",
  [], ["outcome:proved", "mech:chebotarev", "growing-level"])
C("Hilbert irreducibility", "—", "—", "proved", "thin sets", "See Serre-thin-set transfer item.", "None.", [], ["outcome:proved", "thin-sets"], conf="high")
C("Primes k·2^n + 1 for fixed non-Sierpiński k (infinitely many n?)", "Σ 1/n diverges", "none for non-Sierpiński k", "open", "none",
  "Divergent log-count without obstruction, still open — 'divergent count + no obstruction' is the generic open state.", "None.", [], ["outcome:open", "count:divergent-log"], conf="high")
C("Fermat primes 2^{2^n} + 1 finite?", "Σ 2^{−n} < ∞", "—", "open (heuristically finite)", "—", "Convergent-count side; control.", "None.", [], ["outcome:open", "count:zero"], conf="high")
C("Waring–Goldbach: n = p₁² + … + p₅² (Hua)", "power", "local mod 24", "proved for large n in the right class", "circle method", "Control.", "None.", [], ["outcome:proved", "count:power"], conf="high")
C("Goldbach–Linnik numbers in short intervals", "power", "—", "almost all", "zero density", "Control.", "None.", [], ["outcome:almost-all", "count:power"], conf="med")
C("Least primitive root g(p)", "polylog under GRH (Shoup)", "—", "unconditional ≪ p^{1/4+ε}; GRH ≪ log⁶ p", "character sums", "Same as least-QNR class.", "None.", [],
  ["outcome:proved", "count:polylog-under-GRH", "seen:BRAINSTORM/z31_small_count_pointwise.md"])
C("Vinogradov's least-QNR conjecture n(p) ≪ p^ε", "—", "—", "open", "Burgess barrier", "KST say beating their result needs this; ES gate G4 has similar flavour.", "None.", [],
  ["outcome:open", "gate-G4"], conf="high")
C("AKS: deterministic primality in polynomial time", "—", "—", "proved", "polynomial identity (x + a)^n ≡ x^n + a mod (n, x^r − 1)",
  "Derandomisation of a witness search by an algebraic identity — ES's certificate search is 'easy in practice' but not derandomised.",
  "Ask whether a deterministic certificate-finding procedure with a provable step bound would follow from any known identity-based test.", [], ["outcome:proved", "derandomisation", "mech:polynomial-identity"], conf="med")
C("Burgess-range representation: every p has x ≤ p^{1/4+ε} with x² + 1 ≡ 0 mod… (small solutions of congruences)", "—", "—", "various proved", "character sums",
  "Small solutions to congruences mod p are typical least-witness problems.", "None.", [], ["outcome:proved", "mech:character-sum"], conf="med")
C("Erdős–Woods numbers", "—", "—", "infinitely many known (constructive)", "CRT constructions", "Control (CRT constructive).", "None.", [], ["outcome:proved"], conf="med")
C("Giuga / Agoh conjecture", "0", "—", "open", "—", "Control.", "None.", [], ["outcome:open", "count:zero"], conf="med")
C("Every even n = difference of two primes (in infinitely many ways)", "power", "—", "open; bounded gaps give some even numbers", "Maynard sieve", "Control.", "None.", [], ["outcome:open"], conf="high")
C("Wiles/Taylor: Fermat's Last Theorem", "0", "—", "proved", "modularity", "Rigidity side.", "None.", [], ["outcome:proved-none", "mech:modularity"], conf="high")
C("Darmon–Granville generalised Fermat finiteness", "finite", "—", "proved finite for 1/p+1/q+1/r < 1", "Faltings",
  "Hyperbolic signature 1/p + 1/q + 1/r < 1 — a unit-fraction condition governing Diophantine finiteness; the ES surface boundary geometry may have an orbifold-signature reading.",
  "Compute the orbifold/log-geometry signature of the ES boundary (as in Campana orbifolds) to see if ES lies in a 'Campana-special' class.",
  [], ["outcome:proved", "mech:faltings", "orbifold"], conf="med")
C("Campana's conjecture for orbifold points / Darmon points on P¹", "varies by signature", "—", "partially proved", "orbifold geometry",
  "ES fibre's 'positivity + integrality' could be framed as Campana points on an orbifold; Campana-special orbifolds conjecturally have potentially dense points.",
  "Literature check: 'Campana points cubic surface integral' (Pieropan–Smeets–Tanimoto–Várilly-Alvarado) and whether ES is a Campana problem.",
  [], ["outcome:partial", "orbifold", "integral-points"], conf="low", effort="medium")
