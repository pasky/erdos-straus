# Items batch 2: multiplicative / analytic number theory upgrades.

I("LINNIK", "Linnik's three principles for the least ES certificate",
  "Linnik made Dirichlet effective-for-every-q with: log-free zero density, zero-free region, Deuring–Heilbronn repulsion. ES analogue: bound the least level C(p) (or least e) carrying a certificate by p^L, organising the proof as (a) 'density' of bad character configurations, (b) a 'zero-free' range for small moduli, (c) an exceptional character making other families easier.",
  "Every bound C(p) < ∞ already is ES, so the content is the three-part architecture: separating 'few bad characters' from 'one exceptional character'.",
  "Write the BM-level positivity proof (least ℓ with (p/ℓ) = −1) as principle (b), and formulate precisely what principle (a) would have to say about order-≥3 characters mod 4C.",
  ["least-certificate", "zero-density", "architecture"], "med", "medium")
I("LINNIK", "Exceptional character helps: Deuring–Heilbronn for ES families",
  "In Linnik's theorem a Siegel zero repels other zeros and makes primes more regular in other progressions. For ES, if (·/p) is 'exceptional' (QR at all small primes), the BM main term at small levels vanishes — but maybe other certificate families (b=1 line, windows with q where (q/p) = −1 is forced large) become abundant.",
  "A dichotomy 'either the characters are regular (use H⁻_BM-type counting) or one is exceptional (use the repelled families)' is how Linnik/Heilbronn escaped worst cases.",
  "Among primes with large least non-residue ℓ(p) (p ≡ 1 mod 840·k), compare counts of (★), b=1, ES₅ and window certificates to controls.",
  ["deuring-heilbronn", "dichotomy", "numerics"], "med", "cheap", kw=["Deuring"])
I("DIR", "Dirichlet's product trick: a product of all level series with nonnegative coefficients",
  "Dirichlet: Π_χ L(s,χ) = ζ_K(s) has nonnegative coefficients, so no L(1,χ) vanishes. ES: look for a product/combination of the twisted level series Σ_χ σ_χ(tn+1) whose coefficients are nonnegative and whose value 'at s = 1' (or at the p-th coefficient) is forced positive.",
  "Positivity of a combination is how non-vanishing statements are proved for every modulus; METAPLECTIC Thm K gives exactly these character-twisted series.",
  "From Thm K, form Σ_{χ mod t} σ_χ(N) products over a few levels t and test numerically which combinations have nonnegative coefficients that vanish at p only when R(p) = 0.",
  ["positivity", "L-functions", "generating-functions"], "low", "medium")
I("DIR", "Class-number formula positivity for the BM correction T(p)",
  "Dirichlet's real-character case: L(1,χ) = (const)·h > 0 because h is a positive integer. M_BM = M₀ − T(p) with T(p) = Σ (−uB/p)/φ(4uB); express T(p) through L(1, (·/p)·ψ) for small auxiliary ψ, i.e. through class numbers of Q(√±p m).",
  "If T(p) ≈ c·L(1,(·/p))·(log p) + …, then integrality/positivity of class numbers and known upper bounds of L(1,χ) give an exact grip on the main term, beyond Burgess.",
  "Write T(p) as a Dirichlet series in (·/p) with multiplicative weights; extract the main term as a combination of L(1,(·/p)χ) and check numerically against computed T(p).",
  ["class-number-formula", "BM-main-term", "L(1,chi)"], "high", "medium")
I("BERT", "Erdős–Bertrand size contradiction: ES failure forces 4Cp+1 into thin multiplicative sets for every C",
  "Erdős proved Bertrand by showing C(2n,n) would be too small if no prime lay in (n,2n]. ES failure at p means: for every C, 4Cp+1 has no divisor ≡ −1 (mod 4C) (e.g. C=1: 4p+1 has only prime factors ≡ 1 mod 4; C=2: 8p+1's prime factors lie in {1,3} or {1,5} mod 8). Compare Π_C(4Cp+1) — whose prime-factor multiset is fixed by CRT — with these restrictions.",
  "Converts ES into a sieve problem with explicitly known 'prime factor census' (each prime q divides 4Cp+1 exactly for C in one class mod q).",
  "Formalise the constraint set S_C = {N : no divisor ≡ −1 mod 4C} for C ≤ 32 and compute, for the hard primes, how many C ≤ X have 4Cp+1 ∉ S_C (each such C is a certificate).",
  ["multiplicative-sets", "sieve", "size-argument"], "high", "cheap")
I("BERT", "Prime-factor census by CRT: q | 4Cp+1 iff C ≡ −(4p)⁻¹ (mod q)",
  "In Bertrand/Chebyshev the prime factorisation of a binomial coefficient is explicit. Here every prime q ∤ 2p divides 4Cp+1 exactly on one class C ≡ c_q (mod q); a single-prime certificate exists iff 4c_q | q+1 for some q ≡ 3 (mod 4) (C = c_q < q). Higher certificates combine several q's at a common C.",
  "Makes the certificate problem an explicit combinatorial problem on the residues c_q(p); single-prime certificates have probability ≈ τ((q+1)/4)/q, summing to ≍ log²p — the main term in a transparent form.",
  "Compute the single-prime-certificate count S₁(p) = #{q ≡ 3 (4) prime : 4c_q(p) | q+1} for p ≤ 10⁸ and its share of R(p); check whether S₁(p) alone ever vanishes for p in the hard list.",
  ["CRT", "explicit", "numerics"], "high", "cheap")
I("SHORT", "Harman-style comparison sieve: R(p) versus the average of R(n) over a short interval around p",
  "Harman's sieve gets primes in every short interval by comparing a decomposition with a model where asymptotics are known, discarding only small nonnegative terms. ES: compare R(p) with ⟨R(n)⟩ over n ∈ [p−H, p+H] in the same residue class mod 840, using Type I/II information on the multiplicative structure of 4Cn+1.",
  "Averages of R over short intervals are accessible (E(I) ≪ H exp(−c(log H)^{3/4})); the comparison step is the pointwise-transfer mechanism.",
  "Numerically measure |R(p) − ⟨R⟩_H|/⟨R⟩_H for H = p^θ, θ = 0.1..0.5, and see which H makes the comparison tight.",
  ["harman-sieve", "short-intervals", "comparison"], "med", "big")
I("SHORT", "Large-values / 'zero-density' estimate for levels at fixed p",
  "Hoheisel's every-interval theorem needed that few zeros are far right (zero density). ES analogue: at fixed p, show that only few levels C have a large deviation of the level count D_C(p) from its expected 2/φ(4C)·(…), so the many 'good' levels carry R(p) > 0.",
  "Large-values estimates are statements about one object (here one p) and many 'frequencies' (levels) — the right quantifier order.",
  "Compute the empirical distribution of level deviations for fixed p ~ 10⁹ and test a large-values inequality of the shape #{C ≤ X : |dev_C| > V} ≪ X·(stuff)/V².",
  ["large-values", "zero-density", "levels"], "med", "medium")
I("SHORT", "Intermediate milestone: (★)-primes in every short interval",
  "Every interval [x, x + x^{0.525}] contains primes (BHP) and the ES exceptional set in short intervals satisfies E(I) ≪ H exp(−c(log H)^{3/4}) ((D)30), so every such interval contains primes satisfying the sub-route — check that this holds for (★) itself and for Mordell-hard classes.",
  "A cheap, honest 'every interval' theorem; it calibrates which short-interval statements are already free and which are not (e.g. intervals of length (log x)^A).",
  "Verify that the short-interval exceptional-set bound applies to (★) restricted to p ≡ 1 (mod 840) and combine with BHP for primes in progressions to get the statement; then ask for the shortest H where it holds.",
  ["short-intervals", "milestone", "corollary"], "high", "cheap")
I("BURGESS", "Burgess shift trick on the level variable",
  "Burgess amplifies a short character sum by shifting n → n + ab and using multiplicativity. ES events at level C involve the residue of 4Cp+1 modulo divisors; shifting C → C + kd preserves 'd | 4Cp+1'. Use shifts to relate the certificate count on a short C-range to a complete sum handled by Weil.",
  "A Burgess-type argument for divisor events in a short level range would give certificates with small C (C ≤ p^{1/4+ε}), a pointwise statement.",
  "Write #{C ≤ X : ∃ d | 4Cp+1, d ≡ −1 (4C)} with d in a fixed range as a character sum over C mod d and try the (n + ab) shift with Hölder.",
  ["burgess", "short-sums", "levels"], "low", "medium")
I("BURGESS", "Least non-residue lens: ES failure ⇒ p is a QR modulo every small prime (via the BM layer)",
  "Linnik's large sieve shows n(p) ≪ p^ε for almost all p; Burgess gives n(p) ≪ p^{0.152} for all p. If 'no certificate at levels ≤ L' forced (p/ℓ) = 1 for all ℓ ≤ L^c, then Burgess would contradict failure once L^c > p^{0.152}.",
  "SYNTHESIS_SPARKS9 already shows BM-level positivity via ℓ(n); the question is how far the forcing extends when certificates (not just main terms) are required.",
  "Test empirically: among primes with no (★) certificate at levels C ≤ K, what is the distribution of ℓ(p)? (If ℓ(p) is not forced large, the lens fails for (★).)",
  ["least-nonresidue", "burgess", "forcing"], "high", "cheap", seen=["SYNTHESIS_SPARKS9.md"])
I("HEIL", "Heilbronn case split: ES under GRH-type regularity, and ES under its failure",
  "Heilbronn proved h(−d) → ∞ by: if GRH holds, Hecke; if it fails, the false zero itself forces the result. ES: prove (a) ES for all large p assuming a regularity hypothesis R on the characters (·/p), (·/ℓ) and (b) ES for all large p assuming ¬R (some exceptional character), with (b) using the exceptional bias.",
  "Each half is conditional, the union unconditional — a proven almost→every template that tolerates ignorance about which case holds.",
  "Formulate R as the minimal statement H⁻_BM needs (BM_CORRECTED §3.3 says no standard conjecture implies it — find the weakest one that does), then analyse what ¬R gives for the window/b=1 families.",
  ["case-split", "dichotomy", "conditional-to-unconditional"], "med", "big")
I("SIEGELZ", "ES (or (★)) assuming infinitely many Siegel zeros",
  "Heath-Brown: Siegel zeros ⇒ twin primes; Friedlander–Iwaniec (IMRN 2003): under a strong Siegel-zero hypothesis, asymptotics for primes in APs in ranges beyond GRH-type reach. If exceptional characters exist, primes behave like integers with χ(p) = −1, which might make ES certificates (whose density depends on χ_{−4uB}(p)) more abundant at all large p.",
  "One half of a Heilbronn-type split; also a test of whether ES's difficulty is 'parity-like'.",
  "Friedlander–Iwaniec, 'Exceptional characters and prime numbers in arithmetic progressions', IMRN 2003 no. 37 (verified: conditional on an exceptionally strong Siegel-zero hypothesis); then model ES counts when (·/p) agrees with a fixed χ_D at all small primes.",
  ["siegel-zeros", "conditional", "dichotomy"], "med", "medium", kw=["Siegel zero"])
I("ARTIN", "Heath-Brown's 'one of three' for ES windows",
  "Heath-Brown: among three multiplicatively independent integers satisfying non-square conditions (e.g. three distinct primes), one is a primitive root for infinitely many p. ES windows: failure at window e requires the divisor classes of N_e = (p+e)/4 to avoid −1 in their ratio set (often: lie in an index-2 subgroup without −1). Show three suitably independent windows cannot all fail.",
  "Pigeonhole over several candidate families is an every-type argument that needs no single family to work.",
  "For (★)-failing primes, record for small windows e the subgroup generated by the prime factors of N_e mod e; look for algebraic relations among three windows that make simultaneous avoidance impossible.",
  ["pigeonhole", "windows", "subgroups"], "med", "medium", seen=["FORCED_WINDOW.md"])
I("ARTIN", "Index argument: subgroup generated by prime factors of N in (ℤ/4C)*",
  "Artin-type proofs control the index of ⟨a⟩ in F_p*. ES level C fails iff no subproduct of prime factors of N = 4Cp+1 is ≡ −1 (4C). If the factors generate a subgroup H ∌ −1, failure is automatic; if −1 ∈ H, failure needs few factors. Study the index of H as p varies.",
  "Separates the 'algebraic' failure (−1 ∉ H) from the 'combinatorial' one (too few factors), which need different tools (characters vs. zero-sum theory).",
  "For the hard primes and C ≤ 100, compute H = ⟨prime factors of 4Cp+1⟩ mod 4C and classify each failing level as algebraic or combinatorial.",
  ["subgroups", "classification", "numerics"], "high", "cheap")
I("BV-EH", "Audit EH/BV-conditional ES statements for smooth-moduli (MPZ) versions",
  "Zhang got bounded gaps by replacing EH with an equidistribution statement for smooth moduli only. Check each conditional ES result in CONDITIONAL_ES.md: which moduli does it need, and would Polymath8's MPZ(ϖ,δ) (smooth moduli, fixed residues) suffice?",
  "Turns a list of conditional results into unconditional ones whenever the moduli can be taken smooth — exactly the Zhang move.",
  "Read CONDITIONAL_ES.md and tabulate: hypothesis, moduli used, residues fixed or varying, whether smooth restriction loses only a constant.",
  ["smooth-moduli", "conditional-to-unconditional", "audit"], "high", "cheap", seen=["CONDITIONAL_ES.md"])
I("BV-EH", "Maynard multidimensional weights over an auxiliary parameter",
  "Maynard: with k linear forms, sieve weights force at least m of them prime. For fixed p, take k candidate certificate families indexed by an auxiliary integer t (e.g. windows q(t) in progressions) and use multidimensional weights to force at least one success.",
  "Converts 'one family must succeed' into a sieve-weight positivity problem over t, where averaging is legitimate (t is free, p fixed).",
  "Identify a free auxiliary variable t such that each family's success at t is a 'primality-like' event of a polynomial in t; write the GPY/Maynard ratio for the toy model.",
  ["maynard-sieve", "auxiliary-variable", "multiple-families"], "low", "medium")
I("DS", "GCD-graph overlap analysis of the level events E_C",
  "Koukoulopoulos–Maynard proved Duffin–Schaeffer by controlling overlaps of approximation events via GCD graphs. ES: events E_C(p) = {level C has a certificate}; a Chung–Erdős lower bound needs Σ P(E_C ∩ E_C′) small, and overlaps depend on gcd(4C, 4C′) and on shared prime factors of 4Cp+1, 4C′p+1.",
  "Quasi-independence on average is what upgrades 'expected number → positive probability'; the GCD-graph method is the strongest known tool for that step.",
  "Over primes p ≤ 10⁸ estimate P(E_C ∩ E_C′)/(P(E_C)P(E_C′)) as a function of gcd(C,C′) and C/C′; fit a Duffin–Schaeffer-type overlap model.",
  ["quasi-independence", "second-moment", "overlap"], "med", "medium")
I("DS", "Profinite zero–one law for ES certificate sets",
  "Gallagher's zero–one law makes metric Diophantine sets have measure 0 or 1. In the profinite completion of ℤ, the set of p̂ admitting a certificate at a finite level is open; its complement is closed of Haar measure 0 (almost-all theorem). Characterise the complement (contains square-mimicking points, B1).",
  "The integers are a countable dense subset; ES says no integer lies in the closed null set. Knowing its exact shape (squares only? more?) is the profinite form of the problem.",
  "Compute, for M = 840·k with k ≤ 30, the residues mod M not covered by certificates with all parameters dividing powers of M; compare with the squares mod M.",
  ["profinite", "zero-one-law", "B1"], "high", "medium", seen=["POINTWISE_SIZE.md"])
I("FI", "Use p = a² + b² to create bilinear structure (Friedlander–Iwaniec style)",
  "FI broke parity using Gaussian-integer arithmetic for x² + y⁴. Primes p ≡ 1 (mod 4) are norms ππ̄; rewrite certificate conditions (e.g. 4Cp+1 = dd′) in terms of (a,b) and Gaussian integers to obtain Type II bilinear sums with structure.",
  "Mordell-hard primes are all ≡ 1 (mod 4), so this extra structure is always available and unused in divisor formulations.",
  "Express 4Cp + 1 = 4C(a²+b²) + 1 and look for factorisations over ℤ[i] or ℤ[√−C] (4Ca² + 4Cb² + 1) that align with d ≡ −1 (mod 4C).",
  ["gaussian-integers", "bilinear-forms", "parity"], "low", "medium")
I("FI", "Is ES parity-sensitive? A Selberg-parity test for certificate counts",
  "FI/Heath-Brown matter because sieves cannot distinguish parity of Ω. Test whether the ES certificate indicator correlates with λ(4Cp+1) or λ of the divisor: if certificate detection is 'parity-blind', sieve-theoretic approaches are not blocked by parity.",
  "Clarifies whether parity-breaking technology is needed at all.",
  "Compute Σ_C λ(d)·1[d certificate at level C] over all certificates for many p; compare with the total count.",
  ["parity", "liouville", "numerics"], "med", "cheap")
I("TITCH", "Switching d ↔ (4Cp+1)/d: only d ≤ √(4Cp+1) needed, then the trial form",
  "Titchmarsh/Linnik handle large divisors of p−1 by switching to the complementary divisor. For ES both d and N/d are ≡ −1 (mod 4C), so R(p) = 2·#{small d}, and for small d, C is forced: C = c_d := −(4p)⁻¹ mod d with 4C | d+1 and d² ≤ 4Cp+1 (trial form).",
  "Shows that R(p)/2 = #{d : 4c_d(p) | d+1, d² ≤ 4c_d(p)p + 1} with c_d(p) = −(4p)⁻¹ mod d (reviewer repair: the size condition selects the smaller of the two complementary divisors) — a single explicit arithmetic condition per d, ready for Type I equidistribution in d.",
  "Implement the d-indexed formulation and test whether the events {4c_d(p) | d+1} for d in dyadic ranges behave like independent events with probability τ((d+1)/4)/d.",
  ["switching", "trial-form", "explicit"], "high", "cheap", seen=["PARITY_AUDIT.md"])
I("TITCH", "Bombieri–Friedlander–Iwaniec well-factorable weights for the 'self-referential modulus'",
  "BFI pushed level of distribution beyond 1/2 for well-factorable weights. ES events have modulus 4C that is itself a factor of the divisor equation (d ≡ −1 mod 4C with d | 4Cp+1); exploit factorability of the weights in C.",
  "The self-referential modulus is ES's distinctive structure; BFI-type dispersion is designed for moduli with flexible factorizations.",
  "Rewrite R(p) with C = C₁C₂ factorable weights and check whether the resulting sums fit the BFI dispersion template (sum over moduli of a fixed residue).",
  ["level-of-distribution", "well-factorable", "dispersion"], "low", "big")
I("GTZ", "Linear correlations of restricted divisor functions (Matthiesen-type) with p as a coefficient",
  "Matthiesen proved asymptotics for Σ_t Π_i f(L_i(t)) for divisor-type f via the Green–Tao machinery. R(p) is Σ_C of a restricted divisor function of the linear form 4pC + 1; with more structure (several levels) it becomes a correlation.",
  "Gives asymptotics with uniformity questions in the coefficient p — the precise point to check.",
  "Matthiesen, 'Linear correlations of multiplicative functions', Proc. LMS 121 (2020), arXiv:1606.04482 — verified: fixed linear forms only, coefficients may NOT grow with the range; so the needed input is a uniform-in-coefficients version — state it precisely and look for partial results (e.g. for τ-type functions via Kloosterman methods).",
  ["correlations", "divisor-functions", "uniformity"], "med", "medium")
I("GTZ", "Transference principle: dense subsets of ES certificates relative to a pseudorandom majorant",
  "Green–Tao: a dense subset of a pseudorandom set inherits linear patterns. ES certificate sets for varying p sit inside the majorant {all factorizations of 4Cp+1}; transference could show a positive-density subset of p's certificate data forces patterns that are certificates for other p's.",
  "Odd: it moves information between different p, which is not ES; but a pattern-based closure (certificate for p₁,p₂ ⇒ certificate for p₃) would be an every-type mechanism.",
  "Search the (★) data for linear patterns: triples (p₁,p₂,p₃) in AP whose certificates are linearly related.",
  ["transference", "patterns", "odd"], "low", "medium")
I("SKSO", "ES along almost all polynomial families n = f(m)",
  "Skorobogatov–Sofos prove Schinzel on average over polynomial families. Ask: for 100% of quadratic families f (ordered by height), does Type II hold for all large m (or all m)? The square family m² is the T1 exception; maybe 'square-like' families are the only exceptions.",
  "A different 'almost all' axis (over families, every member) that interacts directly with T1 and with the repo's exponential families.",
  "For random quadratics f(m) = am² + bm + c with small height, compute the Type II failure set among m ≤ 10⁵ and see if failures concentrate on families that are squares up to linear change.",
  ["polynomial-families", "T1", "numerics"], "med", "cheap")
I("SIEGEL", "Siegel's two-character trick for ES: a positive-coefficient product over two primes",
  "Siegel bounds L(1,χ₂) below by using ζ L(χ₁) L(χ₂) L(χ₁χ₂) ≥ 0 together with an exceptional χ₁. ES: combine the certificate counts at p and at an auxiliary prime p′ (or the characters (·/p), (·/p′), (·/pp′)) in a positivity identity, so that failure at p would force excess at a related object which is bounded.",
  "Positivity products across two objects are how individual lower bounds were first obtained from average information.",
  "Look for an identity: Σ over certificates of pp′ (composite!) = (certificates of p)·(…) + (certificates of p′)·(…) + mixed; check numerically whether the mixed term is small/positive.",
  ["siegel", "positivity", "two-objects"], "low", "medium")
I("SIEGEL", "Ineffective lower bound for M_BM via Siegel instead of Burgess",
  "Thm 2.2 gets M_BM ≥ (3/16π²) log²p via Burgess. Siegel's L(1,χ) ≫ q^{−ε} might give the full M_BM ∼ M₀ for the dominant small-modulus part, ineffectively.",
  "Would sharpen the unconditional main term (constant) at the cost of effectivity; useful for any ineffective all-large-p route.",
  "Isolate the contribution of moduli 4uB ≤ (log p)^A in T(p), express it via L(1,·) values of characters of conductor ≤ (log p)^A twisted by (·/p), and apply Siegel–Walfisz-type input.",
  ["siegel", "BM-main-term", "ineffective"], "med", "medium")
