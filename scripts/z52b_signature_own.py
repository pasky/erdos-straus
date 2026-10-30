# Lane `signature` (wave z52b): hand-written items (integrator's own matches + feature flips).
# Writes data/z52b/signature_raw/OWN.jsonl.  Rendered/merged by scripts/z52b_signature_merge.py.
import json, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'z52b', 'signature_raw', 'OWN.jsonl')
I = []
def it(title, connection, why, first_step, refs, tags, conf='med', effort='cheap'):
    I.append(dict(title=title, connection=connection, why=why, first_step=first_step,
                  refs=refs, tags=tags + ['src:own'], confidence_not_nonsense=conf, effort=effort))

# ---------------------------------------------------------------- Frobenius / numerical semigroups (new computation)
it("ES words are exactly Frobenius numbers of glued semigroups ⟨tu, tv, u+v⟩",
   "Johnson/Brauer–Shockley gluing gives g(⟨tu, tv, u+v⟩) = t·g(u,v) + (t−1)(u+v) = tuv − u − v when gcd(u,v) = gcd(t,u+v) = 1 "
   "(checked by brute force on 488 triples, scripts/z52b_signature_frob_check.py). So (★)/word-form ES (F16) ⟺ every hard prime p is the "
   "Frobenius number of a 3-generated numerical semigroup ⟨4Cu, 4CB, u+B⟩; for (★) words gcd(4C, u+B) = gcd(4C, p) = 1 automatically.",
   "Rosales–García-Sánchez–García-García–Jiménez Madrid proved every positive integer is the Frobenius number of SOME 3-generated semigroup: "
   "ES becomes a restriction of a solved universality theorem to a structured sub-family (complete intersections glued from a 2-generated piece).",
   "Read Rosales et al. (Math. Scand. 94 (2004) 5–12): which 3-generator family does their construction use for odd g, and can it be forced into the "
   "shape ⟨tu, tv, u+v⟩ with 4 | t?",
   ["https://journals.msp.org/mscand/article/download/792/791/823", "scripts/z52b_signature_frob_check.py"],
   ['F16', 'F01', 'F17', 'numerical-semigroups', 'frobenius', 'solved-sibling', 'new-computation', 'reformulation'], 'high', 'cheap')
it("Symmetric 3-generated semigroups = complete intersections (Herzog): ES as a symmetric-Frobenius representation problem",
   "Herzog: 3-generated symmetric numerical semigroups are complete intersections, i.e. gluings ⟨d·a, d·b, c⟩ with c ∈ ⟨a,b⟩, gcd(d,c) = 1, "
   "whose Frobenius numbers are d(ab − a − b) + (d − 1)c. ES words are the slice c = a + b; other c = αa + βb give other trilinear words "
   "dab − a(d − (d−1)α) − b(d − (d−1)β).",
   "Gives a natural ambient family (all symmetric 3-generated Frobenius numbers = all odd numbers?) containing the ES words; the question 'which (α,β) "
   "slices are universal on primes' is a clean ladder of problems, some maybe solved.",
   "Enumerate, for odd n ≤ 10⁶, which (α,β) ∈ {0,1,2}² slices of d(ab−a−b)+(d−1)(αa+βb) with 4 | d represent n; compare failure sets with U(n)/T1.",
   ["unverified: Herzog 1970, Generators and relations of abelian semigroups and semigroup rings (manuscripta math.)"],
   ['F16', 'F25', 'F08', 'numerical-semigroups', 'complete-intersection', 'ladder'], 'med', 'cheap')
it("Rødseth/Greenberg 3-generator Frobenius algorithm vs. ES₅ continued-fraction length",
   "The Rødseth algorithm computes g(a,b,c) via a negative-continued-fraction (Euclid) expansion of a ratio mod a; for ⟨tu, tv, u+v⟩ that expansion is "
   "short. Compare with λ(p) ≤ 3 (F17).",
   "If the Rødseth expansion of the glued semigroup is exactly the length-3 negative CF of the ES₅ form, the semigroup literature (Kannan, Ramírez Alfonsín) "
   "becomes a dictionary for ES₅.",
   "Run Rødseth's algorithm symbolically on ⟨tu, tv, u+v⟩ and record the CF; check against the BOARD2_SLATE ES₅ slice definitions.",
   ["unverified: Rødseth 1978, On a linear diophantine problem of Frobenius (J. reine angew. Math.)"],
   ['F17', 'F16', 'numerical-semigroups', 'continued-fractions'], 'med', 'cheap')
it("Feature flip: Frobenius numbers of 2-generated semigroups are exactly the t = 1 words (uv − u − v)",
   "g(u,v) = uv − u − v; n is such a number iff n + 1 = (u−1)(v−1)·… i.e. iff n+1 has a suitable factorisation — the t = 1 analogue of ES is a "
   "primality-type condition on n+1 (fails at n+1 prime). ES flips t from 1 to a multiple of 4 and gains the third generator u+v.",
   "Shows precisely which feature (the third, glued generator) converts a primality obstruction into a plausible universality statement.",
   "Tabulate which odd n fail to be g(⟨tu,tv,u+v⟩) for t = 1,2,3,4 separately (each t has its own primality-type failure set) and the union.",
   [], ['F16', 'feature-flip', 'numerical-semigroups', 'F25'], 'high', 'cheap')
it("Genus/Sylvester count of the ES semigroup as a second invariant attached to each witness",
   "Each ES witness (t,u,v) gives a symmetric semigroup S with genus (gaps) (g+1)/2 = (p+1)/2 and an Apéry set of size min generator; these invariants "
   "are fixed by p, so ES asks for a semigroup with prescribed Frobenius number and prescribed shape.",
   "Counting numerical semigroups by genus is a mature field (Kaplan, Zhai's Fibonacci-like growth); ES asks for one member of a structured "
   "subclass among ~φ^g semigroups of genus g — a sparse-subfamily existence question.",
   "Check OEIS/semigroup tables (e.g. GAP package numericalsgps) for counts of complete-intersection semigroups with given Frobenius number.",
   ["unverified: Zhai 2013, Fibonacci-like growth of numerical semigroups of a given genus (Semigroup Forum)"],
   ['numerical-semigroups', 'F04', 'counting'], 'low', 'cheap')

# ---------------------------------------------------------------- idoneal / xy+yz+zx
it("xy + yz + zx: at most 19 non-represented integers (Borwein–Choi) — a solved sibling with the same symmetric form",
   "n ≠ xy+yz+zx (x,y,z ≥ 1) for 18 known n and at most one more (none under GRH). ES's surface is 4xyz = n(xy+yz+zx): the same symmetric quadratic "
   "σ₂ appears. Shares F01, F14, F25 (explicit finite exception list), F23.",
   "The proof route (class numbers of −4n-type discriminants, Weinberger's idoneal bound, ineffectivity via Siegel) is a template for 'all but at most one' "
   "pointwise results — an outcome shape ES has never had.",
   "Read Borwein–Choi (Exp. Math. 9 (2000)) and identify how r_{σ₂}(n) is written as a class-number sum; look for an analogous expression of the ES count "
   "on the slice σ₂ = 4σ₃/n.",
   ["https://projecteuclid.org/journals/experimental-mathematics/volume-9/issue-1/On-the-representations-of-xyyzzx/em/1046889597.full"],
   ['F01', 'F14', 'F25', 'F23', 'idoneal', 'class-numbers', 'solved-sibling', 'seen:BRAINSTORM/bsG_ternary_weinberger.md'], 'high', 'medium')
it("Restrict ES to its σ₂-level sets: (x,y,z) with xy+yz+zx = M and xyz = nM/4",
   "Every ES solution lies on a pair of level sets of elementary symmetric functions σ₂ = M, σ₃ = nM/4; for each M, (x,y,z) are roots of T³ − σ₁T² + MT − nM/4.",
   "Turns ES into: find M and σ₁ such that a cubic with these coefficients splits over ℤ with positive roots — a 'split cubic' problem like those handled "
   "by discriminant/class-group methods.",
   "For hard primes p ≤ 10⁶ list the M = σ₂ values of all solutions; look for structure (e.g. M ≡ 0 mod p, M/p values) suggesting a 1-parameter family.",
   [], ['F14', 'F13', 'symmetric-functions', 'reformulation'], 'med', 'cheap')
it("Weinberger 'at most one exception' via Siegel–Tatuzawa: target theorem shape for ES",
   "Weinberger showed at most one further idoneal number exists (ineffective). Tatuzawa: L(1,χ_D) ≫_ε D^{−ε} for all D but at most one.",
   "A realistic intermediate goal for ES: 'ES holds for all primes except possibly those attached to a single exceptional real character'. ES's BM main "
   "term is a sum of Kronecker characters χ_{−4uB}(p) (F20), exactly where a Siegel-type dichotomy acts.",
   "Check whether the Burgess input in Thm 2.2 (M_BM(p) ≥ 0.019 log²p) can be replaced by Siegel–Tatuzawa to get a larger constant for all p outside "
   "one exceptional modulus.",
   ["unverified: Weinberger 1973, Exponents of the class groups of complex quadratic fields (Acta Arith.)",
    "unverified: Tatuzawa 1951, On a theorem of Siegel (Japan. J. Math.)"],
   ['F20', 'F21', 'siegel-zero', 'ineffective', 'target-shape'], 'med', 'medium')
it("Deuring–Heilbronn / Heath-Brown 'twin primes from Siegel zeros' as a conditional route for ES",
   "Heath-Brown showed that existence of Siegel zeros implies infinitely many twin primes (Siegel zero breaks the parity barrier). ES's obstruction is "
   "parity-like (F22) and its main term is a sum of real characters.",
   "A 'Siegel zero ⇒ ES' or 'Siegel zero ⇒ ES for all large p' theorem would be a genuine new conditional result, and the dichotomy (no Siegel zero ⇒ "
   "better Burgess-type bounds) is the standard way to get unconditional pointwise statements.",
   "Assume χ_D exceptional (χ_D(ℓ) = −1 for most small ℓ); compute whether 4Cp+1 then tends to have many divisors in −1 mod 4C (model with random "
   "primes conditioned on χ_D(ℓ) = −1).",
   ["unverified: Heath-Brown 1983, Prime twins and Siegel zeros (Proc. LMS 47)"],
   ['F22', 'F20', 'siegel-zero', 'conditional', 'parity'], 'med', 'medium')

# ---------------------------------------------------------------- Euler/Goldbach 4xy − x − y
it("Euler–Goldbach: 4xy − x − y is never a square — T1 at level t = 4 is an 18th-century theorem",
   "The classical result (z² = 4xy − x − y has no positive solutions; MathOverflow 364853 traces origin and variations) is exactly the C = 1 case of T1 "
   "(D⁻₄(4m²+1) = 0). Shares F08 (square obstruction by reciprocity), F16.",
   "The MO thread collects variations (other coefficients, more variables); each proved variation is a candidate new T1-type certificate or a candidate "
   "NON-obstruction, which is what ES needs at non-square n.",
   "Read MO 364853 and its references; list every proved variant 'k·xy − x − y ≠ f(z)' and test which correspond to ES slices.",
   ["https://mathoverflow.net/questions/364853/origin-and-variations-of-problem-on-4xy-x-y-being-square"],
   ['F08', 'F16', 'T1', 'reciprocity', 'classical', 'seen:BRAINSTORM/z36_reciprocity_obstruction_home.md'], 'high', 'cheap')
it("IMO 2007/5 Vieta jumping (4ab−1 | (4a²−1)² ⇒ a = b) as an involution proof of T1-type statements",
   "The IMO problem is the same form 4ab − 1 as level-4 ES divisors (d ≡ −1 mod 4). Its standard solution is Vieta jumping (infinite descent on an "
   "involution orbit).",
   "Vieta-jumping proofs give a dynamical (descent) proof of non-existence; reversing them (ascent) is a way to generate witnesses — F38.",
   "Write the Vieta involution on ES words p = 4uBC − u − B in u (fixing B, C) and check whether it maps solutions of p to solutions of related n.",
   ["unverified: IMO 2007 Problem 5 (shortlist N6)"],
   ['F38', 'F08', 'vieta-jumping', 'involution'], 'med', 'cheap')

# ---------------------------------------------------------------- Apollonian / thin groups / Markoff (anchor items; raw lanes have more)
it("Apollonian local-global is FALSE by quadratic/quartic reciprocity (Haag–Kertzer–Rickards–Stange) ↔ T1",
   "HKRS prove entire quadratic and quartic families of curvatures are missed in many integral Apollonian packings despite no congruence obstruction "
   "(Annals 200 (2024)). Same signature as T1: local conditions fine, reciprocity kills square-type families (F06, F08).",
   "Their refined conjecture ('local + reciprocity obstructions are the only ones') is the precise analogue of 'U(n) fails only at squares + finite set'; "
   "the quartic part suggests looking for quartic-reciprocity obstructions in ES sub-families.",
   "Read HKRS §§3–5 (the invariant they attach to the orbit) and attempt to define the same invariant on the ES forest / word set; test on n = 2m², "
   "n = −m² mod ℓ slices.",
   ["https://annals.math.princeton.edu/2024/200-2/p06", "https://arxiv.org/abs/2307.02749"],
   ['F08', 'F06', 'reciprocity', 'thin-orbit', 'apollonian', 'seen:BRAINSTORM/apollonian_reciprocity.md'], 'high', 'medium')
it("Shi (2026): local-global also false for generalized circle packings — more reciprocity-obstruction templates",
   "Extension of HKRS to four further packing types (J. Number Theory 2026). Each new packing type is a new data point for 'which orbit structures "
   "admit reciprocity obstructions'.",
   "A classification of when reciprocity obstructions arise could decide whether ES-type word sets beyond Type I/II can carry them.",
   "Check whether Shi gives a general criterion (e.g. existence of a quadratic form invariant mod squares along the orbit).",
   ["https://www.sciencedirect.com/science/article/abs/pii/S0022314X26000776"],
   ['F08', 'reciprocity', 'thin-orbit'], 'med', 'cheap')

# ---------------------------------------------------------------- Divisors in residue classes (Lenstra etc.)
it("Lenstra: ≤ 11 divisors of N in a class r mod s when s > N^{1/3} — a uniform upper bound per ES level",
   "For N = 4Cp + 1 and s = 4C, Lenstra's bound applies when 4C ≳ p^{1/2}, giving O(1) witnesses per such level; algorithmically "
   "(Coppersmith–Howgrave-Graham–Nagaraj) they are found in poly time. Shares F10.",
   "Gives an unconditional per-level cap; but note that for large C the witnesses are just small (u,B) with uB ≤ √p — a useful sanity link between "
   "the divisor and word pictures.",
   "Verify the dictionary: d = 4Cu − 1, d' = 4CB − 1 ⇒ (4Cu−1)(4CB−1) = 4Cp + 1 ⟺ p = 4uBC − u − B; tabulate R(p) split by C ≤ √p vs C > √p.",
   ["https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1984b/art.pdf", "https://arxiv.org/abs/2410.05030"],
   ['F10', 'F37', 'divisors-in-residue-classes', 'algorithmic'], 'high', 'cheap')
it("Coppersmith lattice method to sample ES witnesses at C ≈ p^{1/4}–p^{1/2}",
   "Coppersmith–Howgrave-Graham–Nagaraj find divisors in a residue class for s > N^{1/4} (with more work). For ES levels C in [p^{1/4}, p^{1/2}] "
   "this is a non-brute-force witness finder.",
   "Turns the search into a lattice-reduction problem; lattice structure could expose WHY witnesses exist (short vectors) — F31.",
   "Implement the Lenstra/Coppersmith divisor search for N = 4Cp+1, r = −1, s = 4C at C ≈ p^{0.3}, p = 10¹⁵ primes; count hits vs. expectation.",
   ["unverified: Coppersmith, Howgrave-Graham, Nagaraj 2008, Divisors in residue classes, constructively (Math. Comp.)"],
   ['F10', 'F31', 'lattice', 'algorithmic'], 'med', 'medium')
it("Ford-style 'anatomy' model: which levels C can host a witness",
   "A random N with k = ω(N) prime factors has ≤ 2^k divisors; their residues mod 4C hit the class −1 with probability ≈ 1 − exp(−2^k/φ(4C)). With "
   "ω ≈ log log p, only levels C ≲ (log p)^{log 2} are 'likely' — an anatomy prediction for where ES witnesses live (cf. Ford's H(x,y,2y)).",
   "Ford solved the divisor-in-interval problem via the anatomy of prime factors; the analogous divisor-in-class statistic would give a sharp "
   "prediction for the distribution of the smallest working level.",
   "Compute, for hard primes p ≤ 10⁹, the smallest C with a (★) witness and compare its distribution with (log p)^{log 2}; regress on ω(4Cp+1).",
   ["unverified: Ford 2008, The distribution of integers with a divisor in a given interval (Annals 168)"],
   ['F10', 'F04', 'anatomy', 'divisors', 'heuristic'], 'med', 'cheap')
it("Maier–Tenenbaum propinquity of divisors as a divisor-structure template",
   "Erdős conjectured almost all n have divisors d < d' ≤ 2d; Maier–Tenenbaum proved it. ES needs 'divisor in a coset of a subgroup' rather than "
   "'two divisors close'. Shares F10w, F05 (almost all).",
   "The Maier–Tenenbaum argument controls the joint distribution of log-divisors; a residue-class version would be the multiplicative-group analogue.",
   "Check whether a residue-class analogue of Maier–Tenenbaum ('almost all N have a divisor ≡ −1 mod q for q ≤ (log N)^c') is in the literature.",
   ["unverified: Maier, Tenenbaum 1984, On the set of divisors of an integer (Invent. Math.)"],
   ['F10', 'F05', 'divisors', 'anatomy'], 'med', 'cheap')

# ---------------------------------------------------------------- Cramér / Maier / short intervals
it("Cramér's conjecture as the closest 'polylog-many expected events must not all fail' analogue",
   "Cramér: every interval [x, x + C log²x] contains a prime — expected count ≍ log x, pointwise, unprovable. ES: ≍ log²p expected witnesses at each "
   "prime. Shares F04, F21, F24, F23 (prime gaps verified to 2⁶⁴).",
   "Whatever makes Cramér hopeless (no structure at polylog scale) is a diagnostic: ES must use structure Cramér lacks (fixed-p algebra, BM-exact main "
   "term) or it is equally hopeless.",
   "Write a one-paragraph 'what ES has that Cramér lacks' list and check each item against the existing proof attempts.",
   ["https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture"],
   ['F04', 'F21', 'F24', 'short-intervals', 'heuristic', 'diagnostic'], 'high', 'cheap')
it("Maier's matrix method for ES: build primes where the Poisson model under-predicts failures",
   "Maier showed the Cramér model fails in short intervals because small-prime biases correlate events. For ES, choose p in progressions modulo "
   "products of small primes (p a square mod many ℓ) and measure R(p) relative to M_BM(p).",
   "If R(p)/M_BM(p) is systematically smaller on such 'Maier primes', the one-sided H⁻_BM is at risk; if not, it is evidence the BM normalisation "
   "already absorbs the Maier effect.",
   "Take primes p ≡ 1 mod 840·∏ℓ with p a QR mod every ℓ ≤ 50, p ≈ 10¹²; compute R(p)/M_BM(p) vs. random primes of same size.",
   ["https://projecteuclid.org/journals/michigan-mathematical-journal/volume-32/issue-2/Primes-in-short-intervals/10.1307/mmj/1029003189.full"],
   ['F24', 'F04', 'maier', 'adversarial', 'seen:DISPROOF_AVENUES.md'], 'high', 'medium')
it("Granville's corrected Cramér model ↔ BM-corrected Poisson model for R(p)",
   "Granville refined Cramér's model by sieving small primes, predicting larger gaps (ξ ≥ 2e^{−γ}). ES's analogue is replacing the naive density 1/(4uC−1) "
   "by 1/φ and then by the BM-corrected main term.",
   "A precise 'Granville-type' ES model would predict the maximal size of log P(R = 0 | M) and hence whether finitely many failures are expected.",
   "Fit P(R*(n) = 0 | M_BM(n)) on odd non-squares ≤ 10⁸ against e^{−cM} with c from a sieved Poisson model.",
   ["unverified: Granville 1995, Harald Cramér and the distribution of prime numbers (Scand. Actuarial J.)"],
   ['F24', 'F04', 'heuristic', 'probabilistic-model'], 'med', 'medium')
it("Legendre / Oppermann (prime between consecutive squares): almost-all known, pointwise open — another polylog-to-polynomial sibling",
   "Prime in (n², (n+1)²): count ≍ n/log n, almost-all via zero-density, pointwise open. Shares F01, F05, F21, F23. Feature flip vs ES: count polynomial "
   "rather than polylog (larger budget, still open).",
   "Calibration: a method that would prove ES pointwise but not Legendre must use something specific to ES's algebra.",
   "List which ES pointwise programs (H⁻_BM etc.) would, if transplanted, also prove Legendre — those are suspect.",
   ["https://en.wikipedia.org/wiki/Legendre%27s_conjecture"],
   ['F05', 'F21', 'feature-flip', 'short-intervals', 'calibration'], 'med', 'cheap')

# ---------------------------------------------------------------- least nonresidue, Artin
it("Least quadratic non-residue: exists iff n is not a square — the exact reciprocity shape of T1",
   "For n > 1, some prime ℓ has (n/ℓ) = −1 iff n is not a square; the least one is ≪ log²n under GRH (Ankeny/Bach) and ≪ n^{1/(4√e)+ε} "
   "unconditionally. ES's BM layer is pointwise free iff n is not a square (SYNTHESIS_SPARKS9 Prop 2.2).",
   "This is the only fully solved problem whose failure set is exactly the squares; ES's remaining difficulty is the 'one more character' step beyond it.",
   "Quantify: for hard primes ≤ 10⁹ correlate ℓ(p) (least non-residue) with R(p) and with the smallest working level; check whether R(p) is small exactly "
   "when ℓ(p) is large.",
   ["https://en.wikipedia.org/wiki/Quadratic_residue"],
   ['F08', 'F20', 'least-nonresidue', 'solved-sibling', 'seen:SYNTHESIS_SPARKS9.md'], 'high', 'cheap')
it("Artin's conjecture: quantifier flip (∃a ∀∞p) vs ES (∀p ∃ witness); Heath-Brown 'one of three' shape",
   "Heath-Brown (Quart. J. Math. 37 (1986)): among any three multiplicatively independent candidates, at most two fail to be primitive roots for "
   "infinitely many p. Squares can never be primitive roots (F08-like obstruction). Shares F08w, F22 (Chen/Fouvry–Iwaniec sieve).",
   "The quantifier order is flipped, which is instructive: fixed-witness/varying-p statements are sieve-accessible; ES's ∀p∃ needs the opposite.",
   "Formulate the ES analogue 'for any three fixed (u,B) pairs, at most two lines fail for a positive proportion of p' — check it is trivial or false.",
   ["https://ora.ox.ac.uk/objects/uuid:2280da4e-9613-46ba-8619-14b2c2fbdbac"],
   ['F08', 'F22', 'artin', 'feature-flip', 'quantifier-order'], 'med', 'cheap')
it("Least primitive root ≪ p^{1/4+ε} (Burgess) as a pointwise-small-witness template",
   "Pointwise existence of a small witness (primitive root) with the bound coming from character-sum estimates (Burgess) — same input as ES's "
   "M_BM ≥ 0.019 log²p bound.",
   "Shows the Burgess route gives pointwise statements only when ONE character sum controls the event; ES needs control of many characters mod "
   "4uB simultaneously.",
   "Write the ES (★) event at fixed level as a sum over characters mod 4uB and identify the minimal set whose Burgess control suffices for one (u,B).",
   [], ['F20', 'F21', 'burgess', 'character-sums'], 'med', 'cheap')

# ---------------------------------------------------------------- Linnik / Hooley / dispersion
it("Linnik's n = p + x² + y² (dispersion method): pointwise count of a divisor-character sum along a long family",
   "r₂(n − p) = 4Σ_{d|n−p} χ₋₄(d): Linnik proved Σ_p r₂(n−p) ∼ main term for every large n. ES's R(p) = Σ_C D_{4C}⁻(4Cp+1) is also a sum over a family "
   "of divisor-in-class counts (F10, F20, F21).",
   "Difference to pin down: Linnik's family has length ≍ n (huge mean), ES's effective length is log p (polylog mean) — the dispersion method needs "
   "the long family; quantify how long an ES family would need to be.",
   "Compute the variance of D_{4C}⁻(4Cp+1) over C ≤ X for fixed p, X = p^θ; see at which θ a dispersion bound would give R > 0.",
   ["unverified: Linnik 1960, An asymptotic formula in an additive problem of Hardy–Littlewood (Izv.)"],
   ['F10', 'F20', 'F21', 'dispersion', 'solved-sibling'], 'high', 'medium')
it("Hooley's GRH proof of p + x² + y² before Linnik: GRH sufficed there — why not for ES?",
   "Hooley (1957) proved the Hardy–Littlewood p + x² + y² asymptotic under GRH; Linnik later removed GRH. For ES, GRH is not known to imply anything "
   "pointwise (F36).",
   "The precise reason (length of averaging) gives a sharp test for any proposed 'GRH ⇒ ES' argument.",
   "Re-derive in one page where Hooley uses the length-n average over p and write the ES analogue with length log p.",
   ["unverified: Hooley 1957, On the representation of a number as the sum of two squares and a prime (Acta Math.)"],
   ['F36', 'F21', 'GRH', 'calibration'], 'med', 'cheap')
it("Hooley's τ(n² + a) asymptotics ↔ Type I divisors of p² + 4c²d",
   "Type I ES ⟺ f | p² + 4c²d with f ≡ −p (mod 4cd): divisors of a quadratic polynomial value in a residue class. Hooley's method (equidistribution "
   "of roots of quadratic congruences; Duke–Friedlander–Iwaniec) controls Σ_n τ(n² + a).",
   "For ES one varies (c,d) at fixed p — the family is the polynomial's coefficients, not its argument; check if a 'coefficient-variable' Hooley theorem exists.",
   "Search: 'divisors of n² + a in arithmetic progressions uniformly in a'; compute the Type I count vs. Hooley-type prediction at fixed p.",
   ["unverified: Hooley 1963, On the number of divisors of a quadratic polynomial (Acta Math.)"],
   ['F10', 'F28', 'quadratic-congruences', 'seen:paper/es-typei-heegner-note'], 'med', 'medium')

# ---------------------------------------------------------------- Goldbach family
it("Goldbach–Linnik: even n = p + q + K powers of 2 (K = 8, Pintz–Ruzsa) — adding a sparse structured set makes pointwise possible",
   "Linnik showed finitely many powers of 2 suffice; Heath-Brown–Puchta K = 13, Pintz–Ruzsa K = 8. Shares F01, F05 (binary Goldbach exceptional set) "
   "and the strategy 'almost-all + a sparse absorbing set'.",
   "ES analogue: show 4/p = 1/x + 1/y + 1/z + (sum of K unit fractions from a sparse set S) with K bounded, then try to shrink K — a ladder of "
   "weakenings with K = ∞ trivial.",
   "Define ES_K(S): 4/p − Σ_{i≤K} 1/s_i ∈ {1/x+1/y+1/z} for some s_i ∈ S = {2^j}; compute the least K needed for p ≤ 10⁷.",
   ["unverified: Heath-Brown, Puchta 2002, Integers represented as a sum of primes and powers of two (Asian J. Math.)"],
   ['F05', 'F01', 'absorption', 'ladder', 'goldbach'], 'med', 'cheap')
it("Romanoff vs Erdős: n = p + 2^k has positive density but infinitely many failures via covering congruences",
   "Bounded expected count ⇒ covering obstruction possible (Erdős 1950). ES's expected count grows (log²p) and ES has no covering/BM obstruction "
   "(F06, F07): the flip shows exactly what protects ES.",
   "If one could prove 'any obstruction to an ES-like problem with growing expected count must be a covering/BM one', ES would follow from BL — "
   "clarifies the shape of a meta-theorem.",
   "Collect polylog-count additive problems with infinitely many failures and check whether every failure mechanism is congruential.",
   ["unverified: Erdős 1950, On integers of the form 2^k + p and some related problems (Summa Brasil. Math.)"],
   ['F06', 'F07', 'F04', 'covering-systems', 'feature-flip'], 'med', 'cheap')
it("Crocker: infinitely many odd n ≠ p + 2^a + 2^b — polylog expected count yet infinitely many failures",
   "Expected count ≍ log n (polylog), like ES, but Crocker exhibits infinitely many exceptions. Shares F04, F24w.",
   "Key calibration: a polylog expected count alone does not imply finitely many failures. Learn what structure Crocker's exceptions exploit and check "
   "that ES cannot be attacked the same way.",
   "Check whether Crocker's exceptions come from a covering-type construction (e.g. n = 2^{2^m} − 1) and whether an ES analogue (n in a sparse "
   "algebraic family) has abnormally small R(n).",
   ["unverified: Crocker 1971, On the sum of a prime and of two powers of two (Pacific J. Math.)"],
   ['F04', 'F24', 'disproof-calibration', 'covering-systems'], 'med', 'cheap')
it("Goldbach's other conjecture (odd n = p + 2a²) fails at 5777, 5993: a finite-failure, low-count sibling",
   "Stern found the two exceptions; expected count ≍ √n/log n yet failures exist at small n. Shares F01, F25, F23.",
   "Shows finite explicit exception lists arise even with growing counts; ES's analogue lists are U(n)'s {105, 2961, …} and the 14 (★) failures.",
   "Compare the 'margin' (expected count at the exceptions) for Stern numbers with M_BM at the 14 (★) failures and at U(n) failures.",
   ["https://oeis.org/A060003"],
   ['F25', 'F24', 'finite-exceptions', 'calibration'], 'high', 'cheap')
it("Ternary Goldbach (Helfgott): analytic theorem for n ≥ N₀ + computation below — the template ES would follow",
   "Helfgott: every odd n > 5 is a sum of three primes (circle method with explicit constants + verification to 8.875·10³⁰). ES has huge verification "
   "(10¹⁷–10¹⁸, F23); only the analytic half is missing.",
   "Every ES proof will have this shape; knowing the verification limit sets the explicit-constant target (p₀ ≤ 10¹⁸).",
   "Estimate what explicit constant ε in H⁻_BM would be needed for p₀ = 10¹⁸ given the proved M_BM ≥ 0.019 log²p.",
   ["https://arxiv.org/abs/1501.05438"],
   ['F23', 'explicit-constants', 'solved-sibling'], 'high', 'cheap')

# ---------------------------------------------------------------- quadratic forms
it("Duke–Schulze-Pillot: ternary forms represent all large locally-represented n outside finitely many spinor square classes",
   "Spinor exceptions live on square classes tm² — the same shape as T1 (F08). Proof: Iwaniec/Duke bounds for half-integral weight cusp form "
   "coefficients; ineffective (Siegel).",
   "If some ternary lattice/quaternion picture of ES (QUATERNION_ES) has T1 as its spinor-exceptional set, DSP gives 'all large non-squares' for that "
   "picture — but only if representation numbers there are ≫ n^{1/2−ε}, which ES's polylog count is not.",
   "Locate in QUATERNION_ES which ternary form's representations map to ES witnesses; compute its theta series coefficient size at primes.",
   ["https://eudml.org/doc/143750"],
   ['F08', 'F31', 'spinor-exceptions', 'ternary-forms', 'seen:QUATERNION_ES.md'], 'high', 'medium')
it("Ono–Soundararajan: x²+y²+10z² represents all odd n except 18 listed, under GRH",
   "A finite explicit odd exception list proved conditionally (Waldspurger + GRH-explicit L-value bounds). Shares F25 (like U(n)'s list), F23, F36w.",
   "Unlike ES, GRH suffices there because the count is a weight-3/2 coefficient of size n^{1/2}; flip shows the role of the count's size.",
   "Record the explicit constant chain in Ono–Soundararajan and compute the analogous 'margin' for ES (log² vs n^{1/2}).",
   ["unverified: Ono, Soundararajan 1997, Ramanujan's ternary quadratic form (Invent. Math. 130)"],
   ['F25', 'F36', 'ternary-forms', 'feature-flip', 'GRH'], 'med', 'cheap')
it("Bhargava–Hanke 290 theorem: universality certified by a finite test set — opposite of B1",
   "A positive-definite integral form is universal iff it represents 1..290 (finite certificate). ES's B1 (F35) says no bounded procedure works for ES.",
   "Feature flip: universality of ONE fixed object (escalation is finite) versus ES's ∀n∃ object; clarifies that ES lacks a finite 'escalator' structure.",
   "Ask whether 'the set of ES word-forms tuv−u−v with t in a finite set' has an escalation theory (which finite t-sets give all large primes?).",
   ["https://math.stanford.edu/~vakil/files/290-Theorem-preprint.pdf"],
   ['F35', 'feature-flip', 'universal-forms', 'escalation'], 'med', 'cheap')
it("Colliot-Thélène–Xu: spinor exceptions are Brauer–Manin obstructions for integral points",
   "CT–Xu (Compositio 2009) explain many integral Hasse failures for quadratic forms (spinor exceptions on square classes) as BM obstructions. ES has "
   "no BM obstruction (BL) yet T1 kills Type I/II at squares.",
   "Suggests T1 is a BM obstruction on a different (sub)scheme — the Type I/II torsor — which is exactly what makes the squares special; a CT–Xu-style "
   "theorem on a non-obstructed torsor could give existence.",
   "Identify the scheme whose integral points are Type I/II solutions and compute its Br/BM pairing at n = m² (should reproduce T1).",
   ["https://arxiv.org/abs/0712.1957"],
   ['F07', 'F08', 'brauer-manin', 'torsors', 'seen:BRAUER_TWISTS.md', 'seen:TWISTED_T1.md'], 'high', 'medium')
it("Tunnell's theorem: congruent numbers via equality of ternary theta coefficients",
   "Tunnell: n congruent ⇒ (under BSD ⇐) #{2x²+y²+8z² = n} = 2#{2x²+y²+32z² = n}. ES has an exact theta-quotient normal form (F19).",
   "Shows how an existence question about rational points can be converted to a comparison of theta coefficients; ES's normal form is a difference "
   "D⁻ − D⁺ of the same kind.",
   "Write R_t(n) = ½(D⁺+D⁻) + ½(D⁻−D⁺) − β and look for a Tunnell-type identity linking the odd part to a ternary theta series at prime n.",
   ["unverified: Tunnell 1983, A classical Diophantine problem and modular forms of weight 3/2 (Invent. Math.)"],
   ['F19', 'F31', 'theta', 'congruent-numbers'], 'med', 'medium')
it("Heegner/Monsky: every prime p ≡ 5, 7 mod 8 is congruent (resp. 2p) — ∀ primes in a class via explicit points",
   "A ∀p-in-a-class existence theorem proved by explicit construction (Heegner points / mock Heegner points). Shares F01p, F29 (residue class of p "
   "matters).",
   "Template for a constructive proof that works on a residue class of primes by building a witness from an auxiliary arithmetic object (here CM points).",
   "Search for CM / Heegner-type constructions that output divisors of 4Cp+1 in class −1 mod 4C (e.g. from ideals in ℚ(√−p) or ℚ(√−4Cp)).",
   ["unverified: Monsky 1990, Mock Heegner points and congruent numbers (Math. Z.)"],
   ['F01', 'F29', 'heegner', 'constructive'], 'low', 'big')

# ---------------------------------------------------------------- primitive divisors
it("Bilu–Hanrot–Voutier primitive divisors ≡ ±1 mod n supply divisors-in-class for Lucas-type ES families",
   "Primitive prime divisors of the n-th Lucas number u_n satisfy q ≡ (D/q) mod n, and exist for all n > 30 (BHV). That is a guaranteed divisor in a "
   "class tied to the index — exactly F10 — for integers in exponential families.",
   "The campaign's proved thin families (3·2^s+1, 4^s+105, …) used algebraic factorizations; BHV could give a systematic source of divisors ≡ −1 mod "
   "4C for p-tied integers in Lucas families.",
   "For the open families 15·2^s+1 and 4^s+297: write 4C·p+1 for small C as a Lucas-sequence value or factor thereof and check whether a primitive "
   "divisor lands in the needed class.",
   ["unverified: Bilu, Hanrot, Voutier 2001, Existence of primitive divisors of Lucas and Lehmer numbers (J. reine angew. Math.)"],
   ['F10', 'F30', 'primitive-divisors', 'thin-families', 'seen:BRAINSTORM/y3_lucas_dickson_trace.md'], 'med', 'medium')
it("Zsigmondy: finite explicit exception list via elementary cyclotomic argument",
   "a^n − b^n has a primitive prime divisor except for an explicit finite list. Shares F01, F25. Primitive divisors of a^n − 1 are ≡ 1 mod n.",
   "Divisors ≡ +1 mod n come for free from cyclotomy; ES needs −1 classes — the sign flip corresponds to a^n + 1 / Lucas 'negative' sequences.",
   "Check whether n-th primitive divisors of a^n + 1 (≡ 1 mod 2n) can be made ≡ −1 mod 4C after multiplying by known factors.",
   ["https://en.wikipedia.org/wiki/Zsigmondy%27s_theorem"],
   ['F10', 'F25', 'primitive-divisors', 'cyclotomy'], 'low', 'cheap')

# ---------------------------------------------------------------- unit fraction relatives
it("Graham: every n > 77 is a sum of distinct integers with reciprocals summing to 1 — inductive (n → 2n+2, 2n+9) proof",
   "Finite exceptions (F25) + all-n statement about unit fractions (F12) proved by an additive recursion. ES has only multiplicative closure (F02).",
   "If an additive 'transport law' n → an + b preserving ES-solvability existed even partially, an inductive proof shape would open.",
   "Search ES solution tables for maps (x,y,z) at n ↦ solutions at 2n+1, 4n+1 etc.; test which affine maps preserve solvability on all n ≤ 10⁵.",
   ["unverified: Graham 1963, A theorem on partitions (J. Austral. Math. Soc.)"],
   ['F12', 'F25', 'F02', 'induction', 'seen:TRANSPORT_LAW.md'], 'med', 'cheap')
it("ES ⇒ m/n is a sum of m − 1 unit fractions for every m ≥ 4 (and 'm−1 terms' is a ladder)",
   "m/n = (m−4)·(1/n) + 4/n, so ES gives m − 1 terms. Flip: m/n in m − 2 terms is Sierpiński-type for m = 5 (3 terms) and is false for large m "
   "(Schinzel exceptions). F11, F12.",
   "Places ES as the first rung of a ladder 'm/n in k(m) terms'; the threshold function k(m) is a natural object whose known values constrain methods.",
   "Tabulate, for m ≤ 12 and n ≤ 10⁴, the least k with m/n a sum of k unit fractions; record the first m where k = m − 2 fails.",
   [], ['F11', 'F12', 'ladder', 'feature-flip'], 'high', 'cheap')
it("No diagonal ES solutions at p ≡ 1 (mod 4): the S₃ action on solutions is free",
   "If x = y then 4/p = 2/x + 1/z forces a = 2x − p ∈ {1, p²} and 4 | p + 1, so p ≡ 3 (mod 4); same for y = z. Checked: no diagonal solution for any "
   "prime p ≡ 1 (4) below 1500; parity of the unordered count is 50/50 (scripts/z52b_signature_parity.py).",
   "Freeness of S₃ means the ordered count is 6× the unordered one and kills simple involution-parity proofs (Zagier-style) — a useful negative "
   "datum for F38.",
   "Look for a non-S₃ involution (e.g. Vieta in the hyperbola fibre) whose fixed points are classifiable; count fixed points for p ≤ 10⁵.",
   ["scripts/z52b_signature_parity.py"],
   ['F14', 'F38', 'involution', 'parity', 'new-computation', 'seen:INVOLUTION_ES.md'], 'high', 'cheap')
it("Zagier's one-sentence proof (windmill involution) as the canonical parity-existence template",
   "p ≡ 1 mod 4 ⇒ sum of two squares via an involution with a unique fixed point. ES's hard primes are exactly p ≡ 1 mod 4 (F29).",
   "A parity proof needs an odd count; the unordered ES count has no fixed parity (see the diagonal item) — so any windmill-type proof must count a "
   "weighted or restricted subset.",
   "Search for a restricted ES subset (e.g. solutions with x minimal in its Vieta orbit) whose count parity is constant on hard primes ≤ 10⁵.",
   ["unverified: Zagier 1990, A one-sentence proof that every prime p ≡ 1 (mod 4) is a sum of two squares (Amer. Math. Monthly)"],
   ['F29', 'F38', 'windmill', 'involution', 'seen:WINDMILL.md'], 'high', 'cheap')
it("Vose: every m/n is a sum of O(√log n) unit fractions — bounded vs. unbounded term counts",
   "Vose's theorem gives a uniform term bound growing with n; ES fixes 3 terms (F12). Erdős conjectured O(log log n) suffices.",
   "Methods that achieve O(√log n) (smooth-number denominators) might give 3 terms for numerator 4 if the smoothness budget is tuned to p.",
   "Re-read Vose's construction and compute the number of terms it produces for 4/p, p hard, p ≤ 10⁹.",
   ["unverified: Vose 1985, Egyptian fractions (Bull. London Math. Soc.)"],
   ['F12', 'feature-flip', 'smooth-numbers'], 'med', 'cheap')
it("Croot's coloring theorem / Bloom's density theorem: unit fractions inside dense sets",
   "Croot (Annals 2003): any finite colouring of ℕ has a monochromatic 1 = Σ1/x_i; Bloom (2021): positive upper density sets contain such sums. "
   "Shares F12, F05 (density statements).",
   "Their engine (Fourier analysis over smooth numbers + combinatorics of divisors) is the strongest existing unit-fraction existence machinery; "
   "ES is the opposite extreme (3 terms, prescribed target).",
   "Identify the step in Bloom where many terms are needed and ask if a 3-term version with target 4/p survives under a smooth-number restriction.",
   ["unverified: Croot 2003, On a coloring conjecture about unit fractions (Annals 157)", "unverified: arXiv:2112.03726 (Bloom)"],
   ['F12', 'F05', 'unit-fractions', 'fourier'], 'med', 'medium')
it("Sierpiński 5/n: numerator flip 4 → 5 — does a T1 analogue exist for 5/n?",
   "5/n = 1/x+1/y+1/z is open, conjectured always solvable. Shares nearly all ES features (F01, F12, F13, F05, F23); flips F11.",
   "If 5/n's Type I/II analogues are NOT obstructed at squares (or are obstructed at a different set), comparing tells which part of T1 is "
   "numerator-4-specific — important for numerator-uniform-argument checks (8/131).",
   "Define 5/n Type I/II (n divides one/two denominators) and compute whether they vanish at odd squares n = m² for m ≤ 10³.",
   ["unverified: Sierpiński 1956, Sur les décompositions de nombres rationnels en fractions primaires (Mathesis)"],
   ['F11', 'F08', 'feature-flip', 'numerator', 'seen:FOUR_SPECIFIC.md'], 'high', 'cheap')
it("Numerator flip 4 → 8: failures at 17, 131, 241 as an anti-overreach test suite",
   "8/n has genuine exceptions (17, 131, 241 among small primes) while satisfying the same local/BM features (needs check). Any ES argument must "
   "visibly use a property false for 8.",
   "Cheapest filter for candidate proofs: run them on 8/131 and 8/241.",
   "For each tool collected in this lane, write one line: 'does the argument distinguish 4 from 8?'.",
   ["AMPLIFY_EXCEPTION.md"],
   ['F11', 'calibration', 'numerator', 'seen:AMPLIFY_EXCEPTION.md'], 'high', 'cheap')
it("Schinzel's conjecture m/n three terms for n > N(m) with N(m) growing — Pomerance–Weingartner exceptions",
   "For each m, ES-type solvability is conjectured for large n, with exceptions up to exp(m^{1/3+o(1)}) (F11). ES is the m = 4 case with N(4) = 1.",
   "Treat ES as the base of a family with a threshold N(m); methods that give N(m) < ∞ for one m > 4 would already be new.",
   "Check the PW lower-bound construction for exceptions and whether its mechanism (covering by many small primes) can be run at m = 4.",
   ["unverified: Pomerance, Weingartner, On primes and practical numbers / exceptions for m/n (check exact title)"],
   ['F11', 'threshold', 'seen:FRONTIER.md'], 'med', 'cheap')
it("Feature flip: allow one negative unit fraction — 4/p = 1/((p−1)/4) − 1/(p(p−1)/4) trivially",
   "Positivity (F27) is the whole difficulty: with signs, two terms suffice for p ≡ 1 mod 4. The positive cone is the 'boundary' making the surface "
   "log K3-like.",
   "Suggests attacking positivity directly: start from the trivial signed solution and move inside the positive cone by symmetries of the cubic "
   "surface (Vieta moves / Cremona maps).",
   "Enumerate signed 3-term solutions with exactly one negative term for hard p and test whether some explicit birational move lands in the positive cone.",
   [], ['F27', 'feature-flip', 'positivity', 'cubic-surface'], 'high', 'cheap')
it("Feature flip: S-integral ES (denominators in ℤ[1/ℓ]) is trivial — integrality at every prime is essential",
   "With ℓ = 2 or 3 allowed in denominators, 4/n = 3·(1/(3n/4)) or 1/n + 1/(n/3) work. Strong approximation away from S is cheap.",
   "Locates the difficulty: it is the archimedean + all-finite-places integrality simultaneously (F06, F07).",
   "For odd ℓ ≥ 5, determine the least S ∋ ℓ making ES trivial; record which S keep the problem nontrivial.",
   [], ['F07', 'F06', 'feature-flip', 'S-integral'], 'med', 'cheap')
it("ES over totally real fields with totally positive denominators (e.g. ℤ[√2])",
   "Over O_K with K totally real, require x,y,z totally positive: a genuine analogue keeping positivity (F27); over imaginary fields positivity "
   "disappears and the problem trivialises.",
   "A field where the analogue can be proved or disproved (units give extra room) gives a new 'proved variant' family like the F_q[T] ones (F26).",
   "Compute, for K = ℚ(√2), totally positive prime elements π of norm ≤ 10⁴ and search for 4/π = Σ 1/x_i with x_i ≫ 0; look for failures.",
   [], ['F26', 'F27', 'number-fields', 'feature-flip'], 'med', 'medium')
it("Equal-denominator / chain sub-problems (x | y | z) as solvable slices",
   "Restricting ES to chains x | y | z or to a fixed ratio y = kx gives two-variable divisor problems with explicit criteria; the diagonal x = y is "
   "empty for p ≡ 1 mod 4 (see diagonal item).",
   "Each restricted slice is a 'line' in the sense of F34; knowing exactly which primes each slice covers sharpens the infinite-covering picture.",
   "For k = 2..20 compute which hard primes ≤ 10⁷ admit solutions with y = kx; tabulate densities.",
   [], ['F34', 'F15', 'slices'], 'med', 'cheap')
it("Polynomial identities in Gaussian coordinates: ES solutions as polynomials in (a,b) with p = a² + b²",
   "Mordell–Schinzel forbid identities polynomial in p covering square classes (F09). Identities polynomial in (a,b) with p = a² + b² are not obviously "
   "excluded: at b = 0 they would give non-Type-I/II solutions or degenerate.",
   "Hard primes are exactly p ≡ 1 mod 4 (F29) — they come with a canonical Gaussian factorisation that no p-polynomial can see.",
   "For hard primes ≤ 10⁷ compute (a,b) and fit low-degree polynomial forms to the smallest solutions' denominators; check B1 Thm M's scope for "
   "procedures that use the two-squares decomposition.",
   ["POINTWISE_SIZE.md"],
   ['F09', 'F29', 'identities', 'gaussian', 'B1-scope'], 'med', 'cheap')

# ---------------------------------------------------------------- triangle / geometry
it("Triangle altitude identity 1/r = 1/h_a + 1/h_b + 1/h_c: ES ⟸ triangle with integer altitudes and inradius n/4",
   "Any triangle has Σ1/h = s/Δ = 1/r. ES solutions whose reciprocals satisfy the triangle inequalities correspond to triangles with integral "
   "altitudes x,y,z and inradius n/4 (rational sides up to scaling).",
   "Imports the classification of triangles with rational altitudes / Heronian-type parametrisations into ES; a parametrised family of such triangles "
   "with r = p/4 would be an ES family.",
   "For hard primes ≤ 10⁵, compute the fraction of ES solutions satisfying the triangle inequality on (1/x,1/y,1/z); look up 'triangles with integer "
   "altitudes' parametrisations.",
   ["https://en.wikipedia.org/wiki/Altitude_(triangle)"],
   ['geometry', 'reformulation', 'F12', 'triangles'], 'med', 'cheap')
it("Descartes/Soddy: three mutually tangent circles of radii x,y,z have inner Soddy curvature 1/x+1/y+1/z + 2√((x+y+z)/xyz)",
   "ES fixes the linear part to 4/n; integrality of the Soddy curvature additionally needs (x+y+z)/(xyz) to be a rational square. Links ES to "
   "Apollonian-type curvature questions (F08 via HKRS).",
   "A sub-family of ES solutions inside integral Apollonian configurations would inherit thin-orbit tools.",
   "Count ES solutions (p ≤ 10⁵) where (x+y+z)·xyz is a square; if non-empty, look for Apollonian structure.",
   [], ['apollonian', 'geometry', 'F13'], 'low', 'cheap')

# ---------------------------------------------------------------- algebraic geometry of the family
it("Manin–Chambert-Loir–Tschinkel prediction for integral points on the ES threefold vs. Elsholtz–Tao's N log³N",
   "The total space {4xyz = n(xy+yz+zx)} ⊂ A⁴ is a log Fano-type threefold; ET count Σ_{n≤N} f(n) ≍ N log³N (F04). CLT predict exponents from the "
   "Clemens complex of the boundary.",
   "If the CLT/Wilsch framework reproduces log³ (all n) and log² (primes), the geometric picture explains which boundary strata carry solutions — "
   "a geometric handle on where witnesses live.",
   "Compute the boundary divisor and its Clemens complex for a compactification of the ES threefold; compare max-face dimension + 1 with 3.",
   ["unverified: Chambert-Loir, Tschinkel 2010, Integral points of bounded height on partial equivariant compactifications of vector groups"],
   ['F13', 'F04', 'manin-conjecture', 'integral-points'], 'med', 'medium')
it("Wilsch: integral points of bounded height on a log Fano threefold — check if the ES threefold is of that type",
   "Wilsch counted integral points on a specific log Fano threefold with torus-like structure. ES's threefold is a cubic with an (S₃ × scaling) symmetry.",
   "A matching asymptotic with explicit leading constant would be a cross-check on ET's log³ constant and on the BM-corrected local densities.",
   "Check the definition of Wilsch's threefold and whether 4xyz = n(xy+yz+zx) is birational to it or to a toric variety.",
   ["unverified: Wilsch, Integral points of bounded height on a log Fano threefold (IMRN 2023?)"],
   ['F13', 'F04', 'manin-conjecture'], 'low', 'cheap')
it("Hilbert property for integral points (Corvaja–Zannier) applied to the fibration n: X → A¹",
   "ES says the image of X(ℤ)_{>0} under n covers ℤ_{≥2}. Corvaja–Zannier relate the Hilbert property/thin images to fundamental groups. "
   "Polynomial-identity families have thin images missing squares (F09).",
   "A thin-set theorem explaining why parametrised families must miss square classes would turn F09 into a geometric statement and show what a "
   "non-thin covering family must look like.",
   "Check whether Mordell–Schinzel's impossibility is a special case of a Corvaja–Zannier-type 'images of integral points are thin' statement.",
   ["unverified: Corvaja, Zannier 2017, On the Hilbert property and the fundamental group of algebraic varieties (Math. Z.)"],
   ['F09', 'F13', 'thin-sets', 'hilbert-property'], 'low', 'medium')
it("Swinnerton-Dyer/Harpaz fibration method on the hyperbola fibration of the ES surface",
   "Fixing x, ES is a split hyperbola (ay − b)(az − b) = b² (F15) — integral points ↔ divisors of b² in a class. Harpaz (JEMS) handles conic log K3 "
   "surfaces by Swinnerton-Dyer's method conditionally / explicitly.",
   "If ES's surface is a conic log K3 in Harpaz's sense, his explicit sufficient conditions might apply at most n.",
   "Check Harpaz's definition (degree of the base, number of degenerate fibres, splitting) against the ES fibration in x.",
   ["https://arxiv.org/abs/1511.04876"],
   ['F13', 'F15', 'fibration-method', 'log-K3'], 'high', 'medium')

# ---------------------------------------------------------------- Markoff / cubic surfaces
it("Sums of three cubes: no BM obstruction (Colliot-Thélène–Wittenberg), log-scale counts, big computations",
   "x³+y³+z³ = n: affine cubic surface, all n ≢ ±4 mod 9 expected, BM-free, heuristic count ≍ log X up to height X, Booker–Sutherland searches. "
   "Shares F06, F07, F13, F23, F24.",
   "Feature flip: there the solution set per n is infinite (search by height), ES's is finite and bounded by n^{O(1)} — which side is easier for "
   "existence proofs is informative.",
   "Compare the singular-series/BM local density formulas: does ES's BM-corrected main term have the same shape as Heath-Brown's density for cubes?",
   ["unverified: Colliot-Thélène, Wittenberg 2012, Groupe de Brauer et points entiers de deux familles de surfaces cubiques affines (Amer. J. Math.)"],
   ['F06', 'F07', 'F13', 'F23', 'sums-of-three-cubes', 'feature-flip'], 'high', 'cheap')
it("Chen's Markoff mod p theorem (nonabelian level structures): ∀p connectivity via topology of moduli of covers",
   "W. Chen proved every component of the Markoff mod-p graph has size divisible by p, completing Bourgain–Gamburd–Sarnak strong approximation for "
   "all large p. ∀p statement on a cubic surface proved via a non-analytic (algebro-topological) invariant.",
   "A non-analytic, 'every p' theorem about a cubic surface family — exactly the kind of tool ES has never had. ES's words/forest structure (F39) "
   "may admit an analogous moduli interpretation.",
   "Check Chen's argument structure (Annals 2024) and whether ES word sets mod q carry an action of a mapping-class-like group.",
   ["unverified: William Y. Chen, Nonabelian level structures, Nielsen equivalence, and Markoff triples (Annals of Math. 2024)"],
   ['F39', 'F13', 'markoff', 'strong-approximation', 'topological'], 'med', 'big')

# ---------------------------------------------------------------- q-series positivity / nonvanishing
it("Borwein conjecture (Chen Wang, Adv. Math. 2022): sign pattern of q-product coefficients by saddle-point + finite check",
   "ES ⟺ positivity/nonvanishing of coefficients of an explicit theta-quotient level series at prime indices (F19). Wang proved a coefficient sign "
   "pattern for all n analytically.",
   "Feature flip: Wang's coefficients have an exponentially dominant main term; ES's are divisor-sized. Clarifies that an ES q-series proof needs a "
   "positivity mechanism, not asymptotics.",
   "Look for a manifestly positive (product/sum-of-squares) expression of Σ_n R(n)q^n restricted to a progression, e.g. via Andrews-style identities.",
   ["https://arxiv.org/abs/1901.10886"],
   ['F19', 'q-series', 'positivity', 'feature-flip'], 'med', 'medium')
it("Lehmer's τ(n) ≠ 0 and Serre lacunarity: coefficient non-vanishing classes",
   "Nonvanishing of q-series coefficients at every index is ES's F19 form; CM forms vanish on a structured set (inert primes), ES's level series vanish "
   "at squares (T1).",
   "Serre's classification (lacunary ⟺ CM) suggests classifying q-series vanishing exactly on squares; ES's all-level series would be one.",
   "Compute the support of Σ_{t,u,v} q^{tuv−u−v} (4|t restriction) up to 10⁸ and test whether its complement is squares ∪ finite set (U(n) data).",
   ["https://en.wikipedia.org/wiki/Ramanujan_tau_function"],
   ['F19', 'F08', 'nonvanishing', 'q-series'], 'med', 'cheap')

# ---------------------------------------------------------------- covering / sieve meta
it("Erdős–Selfridge / Hough distortion method: positive uncovered density for 'small' covering families",
   "Hough (Annals 2015) and Balister–Bollobás–Morris–Sahasrabudhe–Tiba show covering systems with large minimum modulus / Σ1/m small leave a positive "
   "density uncovered. ES's level sets {p : R_C(p) > 0} form an infinite 'covering' of primes (F34).",
   "Running the distortion method on ES level sets tells which hypothesis (independence across levels? Σ density?) must fail for ES to be true.",
   "Compute the density δ_C of primes covered by level C alone and Σ_C δ_C up to C ≤ 10³; compare with the BBMST criterion.",
   ["unverified: Hough 2015, Solution of the minimum modulus problem for covering systems (Annals 181)"],
   ['F34', 'covering-systems', 'sieve'], 'med', 'cheap')
it("Lovász local lemma / Janson for 'avoid all levels': lower tail of R(p) as a dependency-graph problem",
   "R(p) = 0 means p avoids all level events; Janson's inequality bounds P(no event) by exp(−μ + Δ). ES needs this pointwise, but the "
   "probabilistic version gives the correct heuristic decay.",
   "Already exploited in the campaign (EXSET_ARITH_JANSON); signature match with absorbing/LLL-based existence proofs in combinatorics.",
   "Compute Δ (pair correlation of level events) for hard primes ≤ 10⁸ to see whether μ − Δ grows like log²p.",
   ["EXSET_ARITH_JANSON_OPUS.md"],
   ['F04', 'F24', 'janson', 'seen:EXSET_ARITH_JANSON_OPUS.md'], 'high', 'cheap')

# ---------------------------------------------------------------- dynamics / CF
it("Shrinking-target / hitting-time for the Gauss map: λ(p) ≤ 3 as 'some orbit hits a target in ≤ 3 steps'",
   "ES₅: for each p there is q with p/q of continued-fraction length ≤ 3 (with constraints). In dynamics language: some rational point of "
   "denominator p reaches a target set within 3 Gauss-map steps.",
   "Effective equidistribution of rationals with denominator p under the Gauss map (Ustinov, Bykovskii) could give counts of such q with a "
   "main term ≍ log²p.",
   "Check Ustinov's results on the statistics of continued-fraction lengths of a/p for fixed p (number of a with length ≤ k).",
   ["unverified: Ustinov, On the statistical properties of elements of continued fractions (Doklady)"],
   ['F17', 'continued-fractions', 'dynamics', 'gauss-map'], 'med', 'cheap')
it("Zaremba ↔ ES₅ duality: bounded alphabet/unbounded length vs. bounded length/unbounded alphabet",
   "Zaremba (density one: Bourgain–Kontorovich; Huang) bounds partial quotients; ES₅ bounds the length (≤ 3). Both are 'every denominator p has an "
   "a with a CF constraint' (F01, F17).",
   "Bourgain–Kontorovich's thin-semigroup circle method needs Hausdorff dimension close to 1; ES₅'s length-3 set is 3-dimensional in continuant "
   "coordinates — a completely different counting regime (polylog).",
   "Compute #{a mod p : λ(a/p) ≤ 3 with ES₅ constraints} for hard p and fit c·log²p.",
   ["https://annals.math.princeton.edu/2014/180-1/p03"],
   ['F17', 'zaremba', 'thin-orbit', 'seen:ZAREMBA_TRANSFER.md'], 'high', 'cheap')
it("Continuants: p = K(a,b,c) = abc + a + c (positive CF) vs ES's negative continuant tuv − u − v",
   "Length-3 continuants K(a,b,c) = abc + a + c represent every n > ? trivially (a = c = 1: b + 2), while the negative-CF version with a 4ℤ "
   "constraint is ES. The sign flip is the feature (F16, F27).",
   "The positive version is trivially universal; ES lives exactly between positive and negative continuants — a mixed-sign continuant 'abc + a − c' "
   "family may interpolate.",
   "For the 4 sign patterns of abc ± a ± c with a 4ℤ constraint on one coordinate, compute failure sets among primes ≤ 10⁷.",
   [], ['F16', 'F17', 'continuants', 'feature-flip', 'ladder'], 'high', 'cheap')

# ---------------------------------------------------------------- CS / logic
it("ES is a Π₁⁰ sentence (bounded witness) — like Goldbach and RH",
   "All denominators in a 3-term representation of 4/n are ≤ poly(n) (F32), so ES is ∀n ∃(bounded) — Π₁. Independence from PA/ZFC would imply truth.",
   "Places ES in the Busy-Beaver/Π₁ landscape; gives the 'no counterexample is ever verifiable cheaply' meta-structure.",
   "Write a minimal Turing machine (or Lean decidable predicate) that halts iff ES fails; compare its size with the bbchallenge Goldbach machines.",
   ["https://bbchallenge.org"],
   ['F32', 'logic', 'complexity'], 'med', 'cheap')
it("Is finding ES witnesses as hard as factoring p-tied integers?",
   "Witnesses ⟺ divisors of 4Cp+1 in a class (F10). Known fast heuristic (scan small C, factor small numbers). An ES-oracle reveals factors of 4Cp+1 "
   "for some C.",
   "If ES witnesses are always findable in poly(log p) time by a deterministic method, that method may hide a proof; conversely, a reduction from "
   "factoring would explain why no explicit formula exists.",
   "Measure, for p ≈ 10³⁰, the cost of the cheapest witness search (smallest C with a smooth enough 4Cp+1); check if it ever requires factoring a "
   "hard number.",
   [], ['F32', 'F10', 'complexity', 'algorithmic'], 'med', 'cheap')
it("Scholz–Brauer addition chains: ∀n statement proved on infinite thin families, open in general",
   "l(2^n − 1) ≤ n − 1 + l(n) is proved for many infinite families and verified computationally, open in general — the same 'thin families proved, "
   "no density rung' profile as ES (F30, F23).",
   "Compare the family-proof techniques (Brauer chains, Hansen chains) with ES's 3·2^s + 1 family proofs; both rely on algebraic structure of 2^s.",
   "Read Clift's computational verification and check whether the proved families cover a positive density of n.",
   ["https://arxiv.org/html/2302.02143v1"],
   ['F30', 'F23', 'addition-chains', 'thin-families'], 'low', 'cheap')

# ---------------------------------------------------------------- additional matches
it("Erdős–Straus over F_q[T] (proved variants) as the 'function field sibling' with the same features",
   "Polynomial analogues have proved versions (F26); the obstruction mechanisms (T1 analogue, degree/positivity substitute) can be compared exactly.",
   "Where the F_q[T] proof uses a feature ES lacks (e.g. Weil bounds pointwise at a single polynomial), we learn which ingredient is missing.",
   "List the proof ingredients of the F_q[T] theorems in FUNCTIONFIELD_ES*.md and mark each as 'available over ℤ' or not.",
   ["FUNCTIONFIELD_ES.md"],
   ['F26', 'function-field', 'seen:FUNCTIONFIELD_ES.md'], 'high', 'cheap')
it("Primes p ≡ 1 mod 4 as norms: ES-hardness vs. splitting in many imaginary quadratic fields ℚ(√−uB)",
   "M_BM(p) small ⟺ χ_{−4uB}(p) = +1 for many small pairs, i.e. p splits in many ℚ(√−uB) — Chebotarev in a large compositum. Hard primes are "
   "'maximally split' primes (F20, F29).",
   "Gives an explicit adversarial family (primes totally split in the compositum of ℚ(i, √−ℓ) for ℓ ≤ L) and connects ES lower bounds to the least "
   "prime not totally split (Linnik/Lagarias–Odlyzko).",
   "Compute R(p) for the first primes totally split in ℚ(i, √−3, √−5, √−7, √−11, …) (L up to 40) and compare with random p of same size.",
   [], ['F20', 'F29', 'chebotarev', 'adversarial'], 'high', 'medium')
it("Representation of p by x² + ny² for many n simultaneously (Cox) as a model of 'p a square mod everything small'",
   "Hard ES primes are squares modulo many small moduli (Mordell classes mod 840 are squares). Cox's theory characterises p = x² + ny² via ring "
   "class fields; the simultaneous version is a Chebotarev condition.",
   "If ES-hardness is monotone in 'how many small forms represent p', one could try induction on a class-field tower.",
   "For hard primes ≤ 10⁸ count n ≤ 100 with p = x² + ny² and correlate with R(p)/log²p.",
   ["unverified: Cox, Primes of the form x² + ny² (Wiley)"],
   ['F29', 'F20', 'class-field-theory'], 'med', 'cheap')
it("Bourgain–Garaev sums of reciprocals in F_p: modular ES with small denominators",
   "The congruence 4·n⁻¹ ≡ x⁻¹ + y⁻¹ + z⁻¹ (mod q) with small x,y,z is a Kloosterman-type sumset problem with sharp results; the integral ES "
   "requires the exact equation.",
   "Small modular solutions + a lifting step (choose q = some p-tied integer) could be a route to exact solutions; at minimum it shows which "
   "residues are reachable.",
   "Check the Bourgain–Garaev 'sumsets of reciprocals' results and whether the ES equation mod 4Cp+1 reduces to such a sumset.",
   ["unverified: Bourgain, Garaev, Sumsets of reciprocals in prime fields and multilinear Kloosterman sums (Izv. 2014)"],
   ['F33', 'sum-product', 'kloosterman', 'modular'], 'low', 'medium')
it("Agoh–Giuga / Znám problems: unit-fraction equations with divisibility, finite solution families",
   "Znám's problem (each x_i | Π_{j≠i}x_j + 1) and Giuga numbers mix unit fractions with divisibility (F12, F10). Znám's problem solved for k ≥ 5 "
   "(Sun Qi) by construction.",
   "Their constructions produce unit-fraction identities from divisor chains — a source of explicit ES-like families.",
   "Check whether Sun Qi's construction yields 3-term identities for 4/n in any infinite family of primes.",
   ["https://en.wikipedia.org/wiki/Zn%C3%A1m%27s_problem"],
   ['F12', 'F10', 'unit-fractions', 'constructions'], 'low', 'cheap')
it("Breusch/Stewart: every rational with odd denominator is a finite sum of distinct odd unit fractions",
   "Solved universal unit-fraction statement under a parity restriction; ES fixed-length with no parity constraint. Note: 4/n with all three "
   "denominators odd is impossible (parity of numerator), so ES always uses an even denominator.",
   "Parity restrictions change term counts dramatically — a clean feature-flip for the 2-adic side of ES (F29).",
   "Determine the possible 2-adic valuation patterns (v₂(x), v₂(y), v₂(z)) of ES solutions at hard primes ≤ 10⁵.",
   ["https://en.wikipedia.org/wiki/Egyptian_fraction"],
   ['F12', 'F29', '2-adic', 'feature-flip'], 'med', 'cheap')
it("Odd greedy expansion termination (open): an algorithm-existence problem in unit fractions",
   "Does the odd greedy algorithm always terminate on a/b with b odd? Open, verified computationally. ES: does a natural greedy-type search always find "
   "a 3-term solution? (no — greedy gives more terms).",
   "Defines an 'ES greedy' variant (choose x = ⌈p/4⌉ + k for minimal k such that the remainder is a 2-term fraction) whose success rate on hard primes "
   "is computable.",
   "Compute min k such that 4/p − 1/(⌈p/4⌉+k) is a sum of 2 unit fractions, for hard primes ≤ 10⁹; study the distribution of k.",
   ["https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions"],
   ['F12', 'algorithmic', 'greedy'], 'med', 'cheap')
it("Rav / Bernstein criterion for m/n = 1/x + 1/y (divisor sums a + b ≡ 0 mod m) as the 2-term base case",
   "m/n is a sum of 2 unit fractions iff there are coprime divisors a, b of n (or of n²-related numbers) with m | a + b. ES's hyperbola fibres apply this "
   "after choosing x (F15).",
   "ES = ∃x such that the 2-term criterion holds for 4/n − 1/x; a uniform version of the criterion with x as parameter is exactly the F10 divisor form.",
   "State the criterion precisely for (4x − n)/(nx) and check equivalence with Type I/II divisor forms.",
   ["unverified: Rav 1966, On the representation of rational numbers as a sum of a fixed number of unit fractions (J. reine angew. Math.)"],
   ['F15', 'F10', 'two-term', 'base-case'], 'high', 'cheap')
it("Huang–Vaughan mean values for binary Egyptian fractions",
   "Counts of n ≤ N such that m/n is a sum of 2 unit fractions, and mean values of the representation counts (feature F04, F05 for the 2-term problem).",
   "The 2-term problem has a fully understood exceptional set; matching its method to the ES fibration gives the 3-term exceptional set via a "
   "union over x.",
   "Check the exact statements of Huang–Vaughan and whether their mean-value bound is uniform enough to sum over the ES parameter x.",
   ["unverified: Huang, Vaughan, Mean value theorems for binary Egyptian fractions (J. Number Theory)"],
   ['F04', 'F05', 'two-term', 'mean-values'], 'med', 'cheap')
it("Elsholtz–Planitzer: f(n) ≥ (log n)^{log 6 + o(1)} for almost all n — the 'typical count' sibling",
   "Lower bound for the number of solutions for almost all n (F04, F05) via multiplicative structure (many prime factors ⇒ many solutions).",
   "Primes have no multiplicative structure — the gap between n and p is the gap between this theorem and ES.",
   "Check how the log 6 exponent arises and whether a 'prime-shifted' version (using factors of 4Cp+1 instead of n) gives a lower bound for most C.",
   ["unverified: Elsholtz, Planitzer, The number of solutions of the Erdős–Straus equation and sums of k unit fractions (Proc. Roy. Soc. Edinburgh)"],
   ['F04', 'F05', 'counting', 'seen:FRONTIER.md'], 'high', 'cheap')

# ---------------------------------------------------------------- combinatorial absorption / approximate→exact
it("Absorption method (Ringel, Erdős–Faber–Lovász): approximate structure + absorber ⇒ exact",
   "Combinatorial ∀n∃ conjectures were solved by building most of the object randomly and absorbing the leftovers. ES analogue: '4/p − (a cheap "
   "unit fraction) has a 2-term decomposition' succeeds for almost all choices; the absorber is the freedom in x.",
   "Forces the question: is there an 'absorbing' set of x values (depending on p only through simple data) guaranteed to contain a good one?",
   "For hard primes ≤ 10⁸ find the minimal set X(p) of x-values (in terms of p mod small numbers) that always contains a working x; test stability.",
   ["https://arxiv.org/html/2101.04698v3"],
   ['F05', 'absorption', 'combinatorics', 'methodology'], 'low', 'cheap')
it("Collatz (Tao 2019): almost all orbits attain almost bounded values via logarithmic density — the exceptional-set-improvement analogue",
   "∀n conjecture (F01), almost-all known (F05), huge verification (F23), heuristic support (F24). Tao's key was changing the measure (logarithmic "
   "density) to gain an approximate invariance.",
   "ES's exceptional set bound is stuck at exp(−c(log N)^{3/4}) (F40); a change of averaging measure (logarithmic weights in p, or weighting by "
   "the BM main term) might likewise gain invariance.",
   "Recompute the ES exceptional-set argument with logarithmic density in n and see whether the 3/4 barrier changes.",
   ["https://mathoverflow.net/questions/394553"],
   ['F05', 'F40', 'collatz', 'logarithmic-density', 'seen:EXCEPTIONAL_KARY3.md'], 'med', 'medium')

# ---------------------------------------------------------------- Markoff-like ES structures
it("ES as a Hurwitz-type equation with a Vieta group: orbit counts per n",
   "Hurwitz equations Σx_i² = a·Πx_i have finitely many fundamental solutions per (n,a) generating trees under Vieta moves; ES's word set has a "
   "forest structure (F39). Counting fundamental solutions vs. n is a solved problem type.",
   "If ES words admit a finite 'fundamental domain' per p, existence reduces to existence of a fundamental solution with bounded size.",
   "Define Vieta-like moves on (t,u,v) preserving tuv − u − v = p (e.g. u ↦ (something)) and compute orbit structure for p ≤ 10⁴.",
   ["unverified: Hurwitz 1907, Über eine Aufgabe der unbestimmten Analysis"],
   ['F38', 'F39', 'vieta', 'markoff-hurwitz', 'seen:FOREST_CONNECTIVITY.md'], 'med', 'cheap')
it("Mordell's equation for 1/x + 1/y + 1/z = 1/w: complete parametrisation of the rational cubic surface",
   "The ES surface is rational; full rational parametrisations (e.g. of Σ1/x_i = 1/w) exist. Integral points of the ES fibre are thin inside the "
   "rational points (F13).",
   "A parametrisation in which positivity and integrality become linear/congruence conditions could expose the T1 obstruction as a lattice "
   "condition and suggest where non-T1 solutions come from.",
   "Write the standard parametrisation of 1/x+1/y+1/z = 1/w and substitute w = n/4; record the integrality conditions as divisibility conditions.",
   [], ['F13', 'parametrisation', 'rational-surface'], 'med', 'cheap')

# ---------------------------------------------------------------- feature flips systematic
it("Feature flip F04: raise the expected count by allowing 4 terms with all denominators > n — does pointwise become easy?",
   "4 terms trivial with repeats (1/n ×4); with distinct denominators all > n, the count becomes polynomial in n and circle/divisor methods apply.",
   "Measures how much 'count budget' a pointwise proof needs; a descent from 4 to 3 terms (merging two unit fractions) is a classical move.",
   "Characterise when 1/a + 1/b is a unit fraction (a = k(k+l)… form) and count 4-term solutions mergeable to 3 terms for hard p.",
   [], ['F04', 'feature-flip', 'descent'], 'med', 'cheap')
it("Feature flip F28: forbid Type I (p | exactly one denominator) — Type II alone fails at 14+ primes; union never fails ≤ 10⁸",
   "Restricting the type creates explicit failure sets ((★) fails at 14 primes ≤ 10¹⁰; b = 1 line at 3 primes ≤ 10¹¹); their union survives. "
   "Shares the 'two families, each with sparse failures, disjoint failure sets' structure with Heath-Brown's Artin and with Goldbach-type unions.",
   "If failure sets of two families can be shown disjoint by a parity/sign argument (one fails ⇒ the other has many), ES follows for large p.",
   "Compute for p ≤ 10⁹ the joint distribution of (R_(★)(p), R_{b=1}(p)) and test for negative correlation at small values.",
   ["B1_LINE.md"],
   ['F28', 'F25', 'feature-flip', 'two-families', 'seen:B1_LINE.md'], 'high', 'cheap')
it("Feature flip F02: problems without multiplicative closure (Goldbach) can't reduce to primes — ES's prime reduction as an asset",
   "ES(n) ⇐ ES(d) for d | n reduces to primes; for primes the multiplicative structure of n is gone. Conversely, composites have MORE solutions "
   "(Elsholtz–Planitzer).",
   "Suggests 'prime-free' proofs: use auxiliary composites m = p·k with ES(pk) solutions having k | all denominators (equivalent to ES(p)).",
   "For hard p, find the smallest k such that 4/(pk) has a solution with k dividing all three denominators — equals ES(p) — but study the distribution "
   "of 'near-misses' (k dividing two denominators).",
   [], ['F02', 'feature-flip'], 'low', 'cheap')
it("Feature flip F06: Legendre's three squares (local obstruction 4^a(8b+7)) — what local obstruction would look like for ES",
   "Three-squares fails exactly on a locally-defined set; ES has none (F06). Where local obstructions are absent, ternary problems were solved via "
   "class numbers (Gauss).",
   "Provides the contrast: ES's exceptional behaviour (T1 at squares) is not local but reciprocity-based, like spinor exceptions (DSP item).",
   "Write the ES local densities at 2 and at p and confirm they never vanish at hard primes (sanity check for BL).",
   [], ['F06', 'feature-flip', 'three-squares'], 'med', 'cheap')
it("Feature flip F21: problems where a pointwise bound came from averaging over an auxiliary parameter of length ≫ polylog",
   "Pointwise results (Linnik p + x² + y², Vinogradov three primes, Duke ternary) all average over an auxiliary variable of polynomial length. ES's "
   "auxiliary variables (C, u, B) have polynomial range but polylog effective mass.",
   "Suggests looking for an ES formulation with an auxiliary average of polynomial MASS (e.g. counting weighted solutions with weights growing in C).",
   "Search for a weighting w(C,u,B) with Σ w·1[event] provably positive and mass ≫ p^δ — e.g. weights from smooth-number counts.",
   [], ['F21', 'feature-flip', 'weights'], 'med', 'cheap')
it("Feature flip F17: CF length ≤ 2 — which primes are length-2 (two-term) representable — fully explicit",
   "λ(p) ≤ 2 corresponds to 2-term-type representations, characterised by divisor conditions (Rav). ES₅ is the length-3 rung.",
   "Explicit rung below ES; the step 2 → 3 adds one free parameter, which is where the log² count appears.",
   "Compute the density of primes with λ(p) ≤ 2 (under ES₅ constraints) — should decay like a power of 1/log.",
   [], ['F17', 'feature-flip', 'ladder'], 'med', 'cheap')
it("Feature flip F20: if only real characters contributed (pure genus count), ES would follow from genus theory",
   "R*(n) = M_gen(n) + X(n); M_gen is genus (order ≤ 2 characters), X the rest. Problems where only genus characters appear (class number one, "
   "idoneal discriminants) are solved by genus theory.",
   "Idoneal-type phenomena: when the class group is 2-torsion, representation = genus condition. ES-hardness at a prime could be measured by "
   "how far relevant class groups are from being 2-torsion.",
   "For hard primes, compute X(p)/M_gen(p) and correlate with the 2-rank vs. size of class groups of ℚ(√−p·small).",
   ["SINGLE_P_COUNT.md"],
   ['F20', 'feature-flip', 'genus-theory', 'idoneal'], 'med', 'cheap')
it("Feature flip F37: one-sided statements — 'R(p) ≥ ε·M(p)' vs. two-sided — examples of proved one-sided lower bounds",
   "Two-sided asymptotics are false for R(p) (Linnik-type large values). Proved one-sided lower bounds of the right order exist for e.g. "
   "Σ_{n ≤ x} λ-type sieve problems (Chen) but not pointwise for polylog counts.",
   "Collecting proved one-sided pointwise lower bounds (any field) for counts of polylog size would show whether any precedent exists at all.",
   "Literature search: 'pointwise lower bound' 'representation number' 'log' — look for any theorem giving r(n) ≫ (log n)^c for all n in a natural "
   "problem.",
   [], ['F37', 'F21', 'feature-flip', 'precedent-search'], 'med', 'cheap')
it("Precedent search: theorems giving r(n) ≫ (log n)^c for ALL n (polylog pointwise lower bounds)",
   "Examples to check: number of prime factors-related counts, r(n) for sums of a prime and a square-free?, number of divisors in a dense set; "
   "the 'every n has ≫ log n representations as p + 2^a + 2^b' type (false). F04 + F21.",
   "If no natural polylog-scale pointwise lower bound has ever been proved, ES's required statement is unprecedented — a strong strategic datum.",
   "Ask MathOverflow-style search: 'every integer has at least log n representations'; check Erdős–Fuchs-type and additive-basis-order results.",
   [], ['F04', 'F21', 'precedent-search', 'meta'], 'med', 'cheap')
it("Feature flip F35: problems where bounded certificate schemes DO work (Pratt certificates for primality) vs ES's B1",
   "Primality has short certificates (Pratt) found by structured search, but no bounded formula; ES has short certificates (F32) and B1 forbids bounded "
   "procedures under Schinzel H.",
   "Pratt-style recursive certificates (certificate for p uses certificates for factors of p−1) suggest recursive ES certificates using solutions for "
   "factors of 4Cp+1 or p+4d.",
   "Check whether an ES solution for p can be assembled from ES-like data for prime factors of 4Cp+1 (recursive certificate).",
   [], ['F35', 'F32', 'certificates', 'recursion'], 'low', 'cheap')
it("Feature flip F26: ES over F_q[T] (proved variants) vs. ℤ — the missing Weil-type pointwise bound",
   "In F_q[T], pointwise character-sum bounds (Weil/Deligne) are available at a single modulus; over ℤ only Burgess-type. That is the B2 gap.",
   "Quantifies the exact deficit: what pointwise character-sum saving at modulus 4uB would make ES over ℤ follow.",
   "Translate the F_q[T] proof into the needed ℤ-estimate and check whether it is implied by GLH or is stronger.",
   ["FUNCTIONFIELD_ES2.md"],
   ['F26', 'F36', 'feature-flip', 'character-sums'], 'med', 'cheap')

# ---------------------------------------------------------------- more matched problems (classical)
it("Gauss Eureka (n = Δ + Δ + Δ ⟺ 8n + 3 = sum of three odd squares): linear change of variable to a local-global problem",
   "∀n statement solved by transforming n ↦ 8n + 3 and invoking three squares. ES's divisor forms also transform p ↦ 4Cp + 1, p + 4d (F10).",
   "A single fixed affine transformation sufficed there; ES needs a family of transformations (one per C) — the cost of the extra quantifier.",
   "Look for an ES equivalent with a single affine transform (e.g. a statement about 4p + 1 alone with a richer witness) — e.g. via the "
   "Frobenius semigroup item.",
   ["https://en.wikipedia.org/wiki/Fermat_polygonal_number_theorem"],
   ['F10', 'F01', 'reformulation', 'local-global'], 'med', 'cheap')
it("Waring's problem: G(3) and the finite exceptional sets (23, 239 need 9 cubes)",
   "∀n statements with finite explicit exception lists (F25), proved via circle method + explicit computation; 'every large n is a sum of 4 cubes' "
   "open (count polylog-ish? no — n^{1/3}).",
   "Sums of 4 cubes: almost-all known (Davenport), pointwise open, count ≍ n^{1/3} — a sibling for calibrating ES programs.",
   "List which ES-program steps would, mutatis mutandis, prove 'every large n is a sum of 4 cubes' (calibration).",
   ["https://en.wikipedia.org/wiki/Waring%27s_problem"],
   ['F25', 'F05', 'calibration', 'waring'], 'med', 'cheap')
it("Schinzel–Sierpiński: every positive rational is (p+1)/(q+1)? — follows from Hypothesis H; ES's B1 uses H in the opposite direction",
   "Under Schinzel's H many ∀∃ prime statements hold; for ES, H implies every bounded procedure fails (B1 Thm C). Shares F35, F01.",
   "Interesting duality: H supplies primes where we want them (for existence) and where we don't (to defeat finite procedures).",
   "Ask whether H also implies ES (it supplies primes in polynomial families — could it supply divisors in classes?) — likely not, but record why.",
   ["https://en.wikipedia.org/wiki/Schinzel%27s_hypothesis_H"],
   ['F35', 'hypothesis-H', 'conditional'], 'med', 'cheap')
it("Chen's theorem (p + 2 = P₂) and 'almost-ES' with a relaxed term",
   "Chen circumvented parity by allowing almost-primes. ES analogue: 4/p = 1/x + 1/y + a/z with a small, or with one denominator only "
   "'almost integral' (z ∈ ½ℤ). Note numerator 2 makes ES trivial for p ≡ 1 mod 4 (4/p = 1/x + 1/y + 2/z).",
   "Find the weakest relaxation that is not trivial — that marks where the parity-type barrier sits.",
   "Check triviality for relaxations: (i) z ∈ ½ℤ, (ii) one denominator may be divisible by p², (iii) a/z with a = 3; record first nontrivial one.",
   ["https://en.wikipedia.org/wiki/Chen%27s_theorem"],
   ['F22', 'relaxation', 'parity', 'ladder'], 'med', 'cheap')
it("Hardy–Littlewood conjecture F (primes of form n − k²) / Bateman–Horn: singular series with Legendre-symbol factors",
   "Representation counts with singular series involving (n/ℓ) — vanishing for squares-type n (e.g. n = k² + 1 issues). ES's main term M_BM has "
   "the same Legendre-symbol structure (F20).",
   "Lets ES borrow the full Bateman–Horn singular-series machinery for its main term, and the known numerics for its variance.",
   "Compare M_BM(p)/M₀(p) with a Bateman–Horn-type product ∏(1 − (p/ℓ)/(ℓ−1)) — is it asymptotically such a product?",
   ["https://en.wikipedia.org/wiki/Bateman%E2%80%93Horn_conjecture"],
   ['F20', 'singular-series', 'heuristic'], 'med', 'cheap')
it("Elliott–Halberstam-type level of distribution for divisor-in-class counts (Fouvry–Iwaniec, Friedlander–Iwaniec d₃)",
   "Distribution of τ-type functions in APs beyond √x is known for d₂ (Selberg/Hooley/Heath-Brown) and d₃ (Friedlander–Iwaniec, Fouvry–Kowalski–Michel). "
   "ES sums divisor-in-class counts over p-tied integers.",
   "These give averages over moduli (B2); pointwise not. Still the best tools for the averaged ES problems (exceptional set).",
   "Check whether the 3/4 exceptional-set barrier (F40) can be moved by a d₃-in-APs level beyond 1/2 input.",
   ["unverified: Friedlander, Iwaniec 1985, Incomplete Kloosterman sums and a divisor problem (Annals)"],
   ['F40', 'F10', 'level-of-distribution', 'B2'], 'med', 'medium')

# ---------------------------------------------------------------- data / OEIS items
it("OEIS search: numbers not of the form tuv − u − v (t,u,v ≥ 2) and with 4 | t — is the sequence in OEIS?",
   "U(n)'s failure set (odd squares + {105, 2961, 3985, 25305, 111969, 978145}) is an explicit sequence; if it (or its variants) appears in OEIS, "
   "cross-references may reveal an independent characterisation.",
   "OEIS cross-links occasionally reveal a known theorem behind a computed list.",
   "Query OEIS for 105, 2961, 3985, 25305 and for the 14 (★) failure primes (409, …, 8813281).",
   ["https://oeis.org"],
   ['F25', 'oeis', 'data'], 'high', 'cheap')
it("OEIS A005097 (odd primes − 1)/2 ↔ numbers not of form 2xy + x + y: the bilinear primality template",
   "n ≠ 2xy + x + y ⟺ 2n + 1 prime: the simplest 'trilinear-word ⟺ primality' dictionary. ES's (★) word is the level-4C version with a sign flip.",
   "These dictionaries show which word forms detect primality (dead) and which can be universal (ES) — the sign/level flip is the difference.",
   "Generalise: for the form t·xy − x − y with fixed t, characterise non-represented n via divisors of tn + 1 ≡ −1 mod t; tabulate t = 2..12.",
   ["https://oeis.org/A005097"],
   ['F16', 'F10', 'oeis', 'primality'], 'high', 'cheap')

with open(OUT, 'w') as f:
    for k, d in enumerate(I, 1):
        d = dict(id=f'OWN-{k:03d}', **d)
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print(len(I), 'items ->', OUT)
