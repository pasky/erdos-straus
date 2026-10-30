# z52b lane `signature` — signature matching for Erdős–Straus (ES is OPEN)

*Wave z52b, breadth-first. Status: IN PROGRESS.*

**Item count: 465** (dropped 25 raw items; drop log in `data/z52b/signature_raw/drops.json` + literal-duplicate filter).

Confidence-not-nonsense: {'high': 143, 'med': 254, 'low': 68}; effort: {'cheap': 220, 'medium': 216, 'big': 29}.

Generators: gen:integrator 147, gen:sub-arxiv 48, gen:sub-classical 53, gen:sub-erdosproblems 63, gen:sub-generic 64, gen:sub-oeis-mo-guy 35, gen:sub-other-fields 55

Feature-tag histogram (features in `data/z52b/signature_features.md`): F01 101, F01p 2, F01w 6, F02 7, F02w 1, F03 43, F04 61, F04w 3, F05 45, F05w 6, F06 29, F07 27, F08 22, F08w 16, F09 9, F10 60, F10w 3, F11 13, F12 111, F13 57, F14 32, F15 23, F16 20, F16w 19, F17 26, F17w 1, F18 16, F18w 1, F19 13, F20 35, F21 92, F22 28, F23 36, F24 33, F25 40, F26 8, F27 41, F28 3, F29 39, F30 19, F31 32, F32 79, F33 36, F34 26, F35 8, F36 17, F37 9, F38 22, F39 9, F40 11

Top free tags: partial 150, src:own 147, solved 135, feature-flip 95, src:erdosproblems 63, src:arXiv 48, src:arxiv 48, open 26, src:OEIS 23, quadratic-forms 12, src:MathOverflow 12, divisors 11, src:tao-blog 11, conditional 10, GRH 10, sieve 10, computation 10, solved-sibling 8, ladder 8, heuristic 8, continued-fractions 7, parity 7, thin-families 7, positivity 7, density 7, Egyptian-fractions 7, reformulation 6, calibration 6, unit-fractions 6, geometry 6, exceptional-set 6, symmetry 6, covering 6, solved-large-n 6, numerical-semigroups 5, counting 5, reciprocity 5, absorption 5, covering-systems 5, algorithm 5, primes 5, src:Zaremba 5, src:lonely-runner 5, src:EFL 5, src:addition-chains 5


## Method
1. Wrote ES's structural signature as 40 features F01–F40 (+ weakened variants) — `data/z52b/signature_features.md`.
2. Searched for problems sharing ≥ 3 features, solved ones first, with five research sub-agents (erdosproblems.com tags; arXiv API
   keyword queries; MathOverflow / Guy UPINT / OEIS; problem lists outside analytic NT; classical solved pointwise theorems) plus the
   integrator's own matches and systematic feature-flip items.
3. Only filter: obvious nonsense / literal duplicates (logged in `data/z52b/signature_raw/drops.json`). No barrier screening.


## Items

1. **ES words are exactly Frobenius numbers of glued semigroups ⟨tu, tv, u+v⟩** [high/cheap] — Johnson/Brauer–Shockley gluing gives g(⟨tu, tv, u+v⟩) = t·g(u,v) + (t−1)(u+v) = tuv − u − v when gcd(u,v) = gcd(t,u+v) = 1 (checked by brute force on 488 triples, scripts/z52b_signature_frob_check.py). So (★)/word-form ES (F16) ⟺ every hard prime p is the Frobenius number of a 3-generated numerical semigroup ⟨4Cu, 4CB, u+B⟩; for (★) words gcd(4C, u+B) = gcd(4C, p) = 1 automatically. — *First step:* Read Rosales et al. (Math. Scand. 94 (2004) 5–12): which 3-generator family does their construction use for odd g, and can it be forced into the shape ⟨tu, tv, u+v⟩ with 4 | t?  
   `signature-0001` tags: F16, F01, F17, numerical-semigroups, frobenius, solved-sibling, new-computation, reformulation, src:own, gen:integrator

2. **Symmetric 3-generated semigroups = complete intersections (Herzog): ES as a symmetric-Frobenius representation problem** [med/cheap] — Herzog: 3-generated symmetric numerical semigroups are complete intersections, i.e. gluings ⟨d·a, d·b, c⟩ with c ∈ ⟨a,b⟩, gcd(d,c) = 1, whose Frobenius numbers are d(ab − a − b) + (d − 1)c. ES words are the slice c = a + b; other c = αa + βb give other trilinear words dab − a(d − (d−1)α) − b(d − (d−1)β). — *First step:* Enumerate, for odd n ≤ 10⁶, which (α,β) ∈ {0,1,2}² slices of d(ab−a−b)+(d−1)(αa+βb) with 4 | d represent n; compare failure sets with U(n)/T1.  
   `signature-0002` tags: F16, F25, F08, numerical-semigroups, complete-intersection, ladder, src:own, gen:integrator

3. **Rødseth/Greenberg 3-generator Frobenius algorithm vs. ES₅ continued-fraction length** [med/cheap] — The Rødseth algorithm computes g(a,b,c) via a negative-continued-fraction (Euclid) expansion of a ratio mod a; for ⟨tu, tv, u+v⟩ that expansion is short. Compare with λ(p) ≤ 3 (F17). — *First step:* Run Rødseth's algorithm symbolically on ⟨tu, tv, u+v⟩ and record the CF; check against the BOARD2_SLATE ES₅ slice definitions.  
   `signature-0003` tags: F17, F16, numerical-semigroups, continued-fractions, src:own, gen:integrator

4. **Feature flip: fixed small t — t ≤ 3 is trivially universal on odd n, fixed t = 4 has a primality-type failure set** [high/cheap] — The word tuv − u − v with u = 1 gives (t−1)v − 1, so t = 2 or 3 (and t = 1, = Frobenius numbers g(u,v) = uv−u−v, e.g. g(2,n+2) = n) represents every odd n trivially. Fixed t = 4 gives n = 4uv − u − v ⟺ 4n+1 = (4u−1)(4v−1), which fails e.g. whenever 4n+1 is prime. ES needs the union over t ∈ 4ℤ (plus the glued third generator u+v in the semigroup picture). — *First step:* Tabulate which odd n (and primes) fail to be 4Cuv − u − v for each fixed C = 1,2,3,… separately (each level has its own divisor-type failure set) and for unions over C ≤ K.  
   `signature-0004` tags: F16, feature-flip, numerical-semigroups, F25, src:own, gen:integrator

5. **Genus/Sylvester count of the ES semigroup as a second invariant attached to each witness** [low/cheap] — Each ES witness (t,u,v) gives a symmetric semigroup S with genus (gaps) (g+1)/2 = (p+1)/2 and an Apéry set of size min generator; these invariants are fixed by p, so ES asks for a semigroup with prescribed Frobenius number and prescribed shape. — *First step:* Check OEIS/semigroup tables (e.g. GAP package numericalsgps) for counts of complete-intersection semigroups with given Frobenius number.  
   `signature-0005` tags: numerical-semigroups, F04, counting, src:own, gen:integrator

6. **xy + yz + zx: at most 19 non-represented integers (Borwein–Choi) — a solved sibling with the same symmetric form** [high/medium] — n ≠ xy+yz+zx (x,y,z ≥ 1) for 18 known n and at most one more (none under GRH). ES's surface is 4xyz = n(xy+yz+zx): the same symmetric quadratic σ₂ appears. Shares F01, F14, F25 (explicit finite exception list), F23. — *First step:* Read Borwein–Choi (Exp. Math. 9 (2000)) and identify how r_{σ₂}(n) is written as a class-number sum; look for an analogous expression of the ES count on the slice σ₂ = 4σ₃/n.  
   `signature-0006` tags: F01, F14, F25, F23, idoneal, class-numbers, solved-sibling, seen:BRAINSTORM/bsG_ternary_weinberger.md, src:own, gen:integrator

7. **Restrict ES to its σ₂-level sets: (x,y,z) with xy+yz+zx = M and xyz = nM/4** [med/cheap] — Every ES solution lies on a pair of level sets of elementary symmetric functions σ₂ = M, σ₃ = nM/4; for each M, (x,y,z) are roots of T³ − σ₁T² + MT − nM/4. — *First step:* For hard primes p ≤ 10⁶ list the M = σ₂ values of all solutions; look for structure (e.g. M ≡ 0 mod p, M/p values) suggesting a 1-parameter family.  
   `signature-0007` tags: F14, F13, symmetric-functions, reformulation, src:own, gen:integrator

8. **Weinberger 'at most two more idoneal numbers' / Siegel–Tatuzawa: an 'all but O(1) exceptions' target shape for ES** [med/medium] — Weinberger's work implies at most two idoneal numbers beyond Euler's list (none under GRH), ineffectively. Tatuzawa: L(1,χ_D) ≫_ε D^{−ε} for all D but at most one. — *First step:* Check whether the Burgess input in Thm 2.2 (M_BM(p) ≥ 0.019 log²p) can be replaced by Siegel–Tatuzawa to get a larger constant for all p outside one exceptional modulus.  
   `signature-0008` tags: F20, F21, siegel-zero, ineffective, target-shape, src:own, gen:integrator

9. **Deuring–Heilbronn / Heath-Brown 'twin primes from Siegel zeros' as a conditional route for ES** [med/medium] — Heath-Brown showed that existence of Siegel zeros implies infinitely many twin primes (Siegel zero breaks the parity barrier). ES's obstruction is parity-like (F22) and its main term is a sum of real characters. — *First step:* Assume χ_D exceptional (χ_D(ℓ) = −1 for most small ℓ); compute whether 4Cp+1 then tends to have many divisors in −1 mod 4C (model with random primes conditioned on χ_D(ℓ) = −1).  
   `signature-0009` tags: F22, F20, siegel-zero, conditional, parity, src:own, gen:integrator

10. **Euler–Goldbach: 4xy − x − y is never a square — T1 at level t = 4 is an 18th-century theorem** [high/cheap] — The classical result (z² = 4xy − x − y has no positive solutions; MathOverflow 364853 traces origin and variations) is exactly the C = 1 case of T1 (D⁻₄(4m²+1) = 0). Shares F08 (square obstruction by reciprocity), F16. — *First step:* Read MO 364853 and its references; list every proved variant 'k·xy − x − y ≠ f(z)' and test which correspond to ES slices.  
   `signature-0010` tags: F08, F16, T1, reciprocity, classical, seen:BRAINSTORM/z36_reciprocity_obstruction_home.md, src:own, gen:integrator

11. **IMO 2007/5 Vieta jumping (4ab−1 | (4a²−1)² ⇒ a = b) as an involution proof of T1-type statements** [med/cheap] — The IMO problem is the same form 4ab − 1 as level-4 ES divisors (d ≡ −1 mod 4). Its standard solution is Vieta jumping (infinite descent on an involution orbit). — *First step:* Identify the auxiliary quadratic in the IMO solution ((4a²−1)² = k(4ab−1), quadratic in a) whose Vieta involution proves the level-4 statement, and write its analogue for level 4C divisors d ≡ −1 (mod 4C) of 4Cm²+1.  
   `signature-0011` tags: F38, F08, vieta-jumping, involution, src:own, gen:integrator

12. **Apollonian local-global is FALSE by quadratic/quartic reciprocity (Haag–Kertzer–Rickards–Stange) ↔ T1** [high/medium] — HKRS prove entire quadratic and quartic families of curvatures are missed in many integral Apollonian packings despite no congruence obstruction (Annals 200 (2024)). Same signature as T1: local conditions fine, reciprocity kills square-type families (F06, F08). — *First step:* Read HKRS §§3–5 (the invariant they attach to the orbit) and attempt to define the same invariant on the ES forest / word set; test on n = 2m², n = −m² mod ℓ slices.  
   `signature-0012` tags: F08, F06, reciprocity, thin-orbit, apollonian, seen:BRAINSTORM/apollonian_reciprocity.md, src:own, gen:integrator

13. **Shi (2026): local-global also false for generalized circle packings — more reciprocity-obstruction templates** [med/cheap] — Extension of HKRS to four further packing types (J. Number Theory 2026). Each new packing type is a new data point for 'which orbit structures admit reciprocity obstructions'. — *First step:* Check whether Shi gives a general criterion (e.g. existence of a quadratic form invariant mod squares along the orbit).  
   `signature-0013` tags: F08, reciprocity, thin-orbit, src:own, gen:integrator

14. **Lenstra: ≤ 11 divisors of N in a class r mod s when s > N^{1/3} — a uniform upper bound per ES level** [high/cheap] — For N = 4Cp + 1 and s = 4C, Lenstra's bound applies when 4C ≳ p^{1/2}, giving O(1) witnesses per such level; algorithmically (Coppersmith–Howgrave-Graham–Nagaraj) they are found in poly time. Shares F10. — *First step:* Verify the dictionary: d = 4Cu − 1, d' = 4CB − 1 ⇒ (4Cu−1)(4CB−1) = 4Cp + 1 ⟺ p = 4uBC − u − B; tabulate R(p) split by C ≤ √p vs C > √p.  
   `signature-0014` tags: F10, F37, divisors-in-residue-classes, algorithmic, src:own, gen:integrator

15. **Coppersmith lattice method to sample ES witnesses at C ≈ p^{1/4}–p^{1/2}** [med/medium] — Coppersmith–Howgrave-Graham–Nagaraj find divisors in a residue class for s > N^{1/4} (with more work). For ES levels C in [p^{1/4}, p^{1/2}] this is a non-brute-force witness finder. — *First step:* Implement the Lenstra/Coppersmith divisor search for N = 4Cp+1, r = −1, s = 4C at C ≈ p^{0.3}, p = 10¹⁵ primes; count hits vs. expectation.  
   `signature-0015` tags: F10, F31, lattice, algorithmic, src:own, gen:integrator

16. **Ford-style 'anatomy' model: which levels C can host a witness** [med/cheap] — A random N with k = ω(N) prime factors has ≤ 2^k divisors; their residues mod 4C hit the class −1 with probability ≈ 1 − exp(−2^k/φ(4C)). With ω ≈ log log p, only levels C ≲ (log p)^{log 2} are 'likely' — an anatomy prediction for where ES witnesses live (cf. Ford's H(x,y,2y)). — *First step:* Compute, for hard primes p ≤ 10⁹, the smallest C with a (★) witness and compare its distribution with (log p)^{log 2}; regress on ω(4Cp+1).  
   `signature-0016` tags: F10, F04, anatomy, divisors, heuristic, src:own, gen:integrator

17. **Maier–Tenenbaum propinquity of divisors as a divisor-structure template** [med/cheap] — Erdős conjectured almost all n have divisors d < d' ≤ 2d; Maier–Tenenbaum proved it. ES needs 'divisor in a coset of a subgroup' rather than 'two divisors close'. Shares F10w, F05 (almost all). — *First step:* Check whether a residue-class analogue of Maier–Tenenbaum ('almost all N have a divisor ≡ −1 mod q for q ≤ (log N)^c') is in the literature.  
   `signature-0017` tags: F10, F05, divisors, anatomy, src:own, gen:integrator

18. **Cramér's conjecture as the closest 'polylog-many expected events must not all fail' analogue** [high/cheap] — Cramér: every interval [x, x + C log²x] contains a prime — expected count ≍ log x, pointwise, unprovable. ES: ≍ log²p expected witnesses at each prime. Shares F04, F21, F24, F23 (prime gaps verified to 2⁶⁴). — *First step:* Write a one-paragraph 'what ES has that Cramér lacks' list and check each item against the existing proof attempts.  
   `signature-0018` tags: F04, F21, F24, short-intervals, heuristic, diagnostic, src:own, gen:integrator

19. **Maier's matrix method for ES: build primes where the Poisson model under-predicts failures** [high/medium] — Maier showed the Cramér model fails in short intervals because small-prime biases correlate events. For ES, choose p in progressions modulo products of small primes (p a square mod many ℓ) and measure R(p) relative to M_BM(p). — *First step:* Take primes p ≡ 1 mod 840·∏ℓ with p a QR mod every ℓ ≤ 50, p ≈ 10¹²; compute R(p)/M_BM(p) vs. random primes of same size.  
   `signature-0019` tags: F24, F04, maier, adversarial, seen:DISPROOF_AVENUES.md, src:own, gen:integrator

20. **Granville's corrected Cramér model ↔ BM-corrected Poisson model for R(p)** [med/medium] — Granville refined Cramér's model by sieving small primes, predicting larger gaps (ξ ≥ 2e^{−γ}). ES's analogue is replacing the naive density 1/(4uC−1) by 1/φ and then by the BM-corrected main term. — *First step:* Fit P(R*(n) = 0 | M_BM(n)) on odd non-squares ≤ 10⁸ against e^{−cM} with c from a sieved Poisson model.  
   `signature-0020` tags: F24, F04, heuristic, probabilistic-model, src:own, gen:integrator

21. **Legendre / Oppermann (prime between consecutive squares): almost-all known, pointwise open — another polylog-to-polynomial sibling** [med/cheap] — Prime in (n², (n+1)²): count ≍ n/log n, almost-all via zero-density, pointwise open. Shares F01, F05, F21, F23. Feature flip vs ES: count polynomial rather than polylog (larger budget, still open). — *First step:* List which ES pointwise programs (H⁻_BM etc.) would, if transplanted, also prove Legendre — those are suspect.  
   `signature-0021` tags: F05, F21, feature-flip, short-intervals, calibration, src:own, gen:integrator

22. **Least quadratic non-residue: exists iff n is not a square — the exact reciprocity shape of T1** [high/cheap] — For n > 1, some prime ℓ has (n/ℓ) = −1 iff n is not a square; the least one is ≪ log²n under GRH (Ankeny/Bach) and ≪ n^{1/(4√e)+ε} unconditionally. ES's BM layer is pointwise free iff n is not a square (SYNTHESIS_SPARKS9 Prop 2.2). — *First step:* Quantify: for hard primes ≤ 10⁹ correlate ℓ(p) (least non-residue) with R(p) and with the smallest working level; check whether R(p) is small exactly when ℓ(p) is large.  
   `signature-0022` tags: F08, F20, least-nonresidue, solved-sibling, seen:SYNTHESIS_SPARKS9.md, src:own, gen:integrator

23. **Artin's conjecture: quantifier flip (∃a ∀∞p) vs ES (∀p ∃ witness); Heath-Brown 'one of three' shape** [med/cheap] — Heath-Brown (Quart. J. Math. 37 (1986)): among any three multiplicatively independent candidates, at least one is a primitive root for infinitely many p (so at most two are exceptional). Squares can never be primitive roots (F08-like obstruction). Shares F08w, F22 (Chen/Fouvry–Iwaniec sieve). — *First step:* Formulate the ES analogue 'for any three fixed (u,B) pairs, at most two lines fail for a positive proportion of p' — check it is trivial or false.  
   `signature-0023` tags: F08, F22, artin, feature-flip, quantifier-order, src:own, gen:integrator

24. **Least primitive root ≪ p^{1/4+ε} (Burgess) as a pointwise-small-witness template** [med/cheap] — Pointwise existence of a small witness (primitive root) with the bound coming from character-sum estimates (Burgess) — same input as ES's M_BM ≥ 0.019 log²p bound. — *First step:* Write the ES (★) event at fixed level as a sum over characters mod 4uB and identify the minimal set whose Burgess control suffices for one (u,B).  
   `signature-0024` tags: F20, F21, burgess, character-sums, src:own, gen:integrator

25. **Linnik's n = p + x² + y² (dispersion method): pointwise count of a divisor-character sum along a long family** [high/medium] — r₂(n − p) = 4Σ_{d|n−p} χ₋₄(d): Linnik proved Σ_p r₂(n−p) ∼ main term for every large n. ES's R(p) = Σ_C D_{4C}⁻(4Cp+1) is also a sum over a family of divisor-in-class counts (F10, F20, F21). — *First step:* Compute the variance of D_{4C}⁻(4Cp+1) over C ≤ X for fixed p, X = p^θ; see at which θ a dispersion bound would give R > 0.  
   `signature-0025` tags: F10, F20, F21, dispersion, solved-sibling, src:own, gen:integrator

26. **Hooley's GRH proof of p + x² + y² before Linnik: GRH sufficed there — why not for ES?** [med/cheap] — Hooley (1957) proved the Hardy–Littlewood p + x² + y² asymptotic under GRH; Linnik later removed GRH. For ES, GRH is not known to imply anything pointwise (F36). — *First step:* Re-derive in one page where Hooley uses the length-n average over p and write the ES analogue with length log p.  
   `signature-0026` tags: F36, F21, GRH, calibration, src:own, gen:integrator

27. **Hooley's τ(n² + a) asymptotics ↔ Type I divisors of p² + 4c²d** [med/medium] — Type I ES ⟺ f | p² + 4c²d with f ≡ −p (mod 4cd): divisors of a quadratic polynomial value in a residue class. Hooley's method (equidistribution of roots of quadratic congruences; Duke–Friedlander–Iwaniec) controls Σ_n τ(n² + a). — *First step:* Search: 'divisors of n² + a in arithmetic progressions uniformly in a'; compute the Type I count vs. Hooley-type prediction at fixed p.  
   `signature-0027` tags: F10, F28, quadratic-congruences, seen:paper/es-typei-heegner-note, src:own, gen:integrator

28. **Goldbach–Linnik: even n = p + q + K powers of 2 (K = 8, Pintz–Ruzsa) — adding a sparse structured set makes pointwise possible** [med/cheap] — Linnik showed finitely many powers of 2 suffice; Heath-Brown–Puchta K = 13, Pintz–Ruzsa K = 8. Shares F01, F05 (binary Goldbach exceptional set) and the strategy 'almost-all + a sparse absorbing set'. — *First step:* Define ES_K(S): 4/p − Σ_{i≤K} 1/s_i ∈ {1/x+1/y+1/z} for some s_i ∈ S = {2^j}; compute the least K needed for p ≤ 10⁷.  
   `signature-0028` tags: F05, F01, absorption, ladder, goldbach, src:own, gen:integrator

29. **Romanoff vs Erdős: n = p + 2^k has positive density but infinitely many failures via covering congruences** [med/cheap] — Bounded expected count ⇒ covering obstruction possible (Erdős 1950). ES's expected count grows (log²p) and ES has no covering/BM obstruction (F06, F07): the flip shows exactly what protects ES. — *First step:* Collect polylog-count additive problems with infinitely many failures and check whether every failure mechanism is congruential.  
   `signature-0029` tags: F06, F07, F04, covering-systems, feature-flip, src:own, gen:integrator

30. **Crocker: infinitely many odd n ≠ p + 2^a + 2^b — polylog expected count yet infinitely many failures** [med/cheap] — Expected count ≍ log n (polylog), like ES, but Crocker exhibits infinitely many exceptions. Shares F04, F24w. — *First step:* Check whether Crocker's exceptions come from a covering-type construction (e.g. n = 2^{2^m} − 1) and whether an ES analogue (n in a sparse algebraic family) has abnormally small R(n).  
   `signature-0030` tags: F04, F24, disproof-calibration, covering-systems, src:own, gen:integrator

31. **Goldbach's other conjecture (odd n = p + 2a²) fails at 5777, 5993: a finite-failure, low-count sibling** [high/cheap] — Stern found the two exceptions; expected count ≍ √n/log n yet failures exist at small n. Shares F01, F25, F23. — *First step:* Compare the 'margin' (expected count at the exceptions) for Stern numbers with M_BM at the 14 (★) failures and at U(n) failures.  
   `signature-0031` tags: F25, F24, finite-exceptions, calibration, src:own, gen:integrator

32. **Ternary Goldbach (Helfgott): analytic theorem for n ≥ N₀ + computation below — the template ES would follow** [high/cheap] — Helfgott: every odd n > 5 is a sum of three primes (circle method with explicit constants + verification to 8.875·10³⁰). ES has huge verification (10¹⁷–10¹⁸, F23); only the analytic half is missing. — *First step:* Estimate what explicit constant ε in H⁻_BM would be needed for p₀ = 10¹⁸ given the proved M_BM ≥ 0.019 log²p.  
   `signature-0032` tags: F23, explicit-constants, solved-sibling, src:own, gen:integrator

33. **Duke–Schulze-Pillot: ternary forms represent all large locally-represented n outside finitely many spinor square classes** [high/medium] — Spinor exceptions live on square classes tm² — the same shape as T1 (F08). Proof: Iwaniec/Duke bounds for half-integral weight cusp form coefficients; ineffective (Siegel). — *First step:* Locate in QUATERNION_ES which ternary form's representations map to ES witnesses; compute its theta series coefficient size at primes.  
   `signature-0033` tags: F08, F31, spinor-exceptions, ternary-forms, seen:QUATERNION_ES.md, src:own, gen:integrator

34. **Ono–Soundararajan: x²+y²+10z² represents all odd n except 18 listed, under GRH** [med/cheap] — A finite explicit odd exception list proved conditionally (Waldspurger + GRH-explicit L-value bounds). Shares F25 (like U(n)'s list), F23, F36w. — *First step:* Record the explicit constant chain in Ono–Soundararajan and compute the analogous 'margin' for ES (log² vs n^{1/2}).  
   `signature-0034` tags: F25, F36, ternary-forms, feature-flip, GRH, src:own, gen:integrator

35. **Bhargava–Hanke 290 theorem: universality certified by a finite test set — opposite of B1** [med/cheap] — A positive-definite integral form is universal iff it represents 1..290 (finite certificate). ES's B1 (F35) says no bounded procedure works for ES. — *First step:* Ask whether 'the set of ES word-forms tuv−u−v with t in a finite set' has an escalation theory (which finite t-sets give all large primes?).  
   `signature-0035` tags: F35, feature-flip, universal-forms, escalation, src:own, gen:integrator

36. **Colliot-Thélène–Xu: spinor exceptions are Brauer–Manin obstructions for integral points** [high/medium] — CT–Xu (Compositio 2009) explain many integral Hasse failures for quadratic forms (spinor exceptions on square classes) as BM obstructions. ES has no BM obstruction (BL) yet T1 kills Type I/II at squares. — *First step:* Identify the scheme whose integral points are Type I/II solutions and compute its Br/BM pairing at n = m² (should reproduce T1).  
   `signature-0036` tags: F07, F08, brauer-manin, torsors, seen:BRAUER_TWISTS.md, seen:TWISTED_T1.md, src:own, gen:integrator

37. **Tunnell's theorem: congruent numbers via equality of ternary theta coefficients** [med/medium] — Tunnell: n congruent ⇒ (under BSD ⇐) #{2x²+y²+8z² = n} = 2#{2x²+y²+32z² = n}. ES has an exact theta-quotient normal form (F19). — *First step:* Write R_t(n) = ½(D⁺+D⁻) + ½(D⁻−D⁺) − β and look for a Tunnell-type identity linking the odd part to a ternary theta series at prime n.  
   `signature-0037` tags: F19, F31, theta, congruent-numbers, src:own, gen:integrator

38. **Heegner/Monsky: every prime p ≡ 5, 7 mod 8 is congruent (resp. 2p) — ∀ primes in a class via explicit points** [low/big] — A ∀p-in-a-class existence theorem proved by explicit construction: primes p ≡ 5, 7 mod 8 are congruent numbers, and 2p is congruent for p ≡ 3, 7 mod 8 (Heegner points / Monsky's mock Heegner points). Shares F01p, F29 (residue class of p matters). — *First step:* Search for CM / Heegner-type constructions that output divisors of 4Cp+1 in class −1 mod 4C (e.g. from ideals in ℚ(√−p) or ℚ(√−4Cp)).  
   `signature-0038` tags: F01, F29, heegner, constructive, src:own, gen:integrator

39. **Bilu–Hanrot–Voutier primitive divisors ≡ ±1 mod n supply divisors-in-class for Lucas-type ES families** [med/medium] — Primitive prime divisors of the n-th Lucas number u_n satisfy q ≡ (D/q) mod n, and exist for all n > 30 (BHV). That is a guaranteed divisor in a class tied to the index — exactly F10 — for integers in exponential families. — *First step:* For the open families 15·2^s+1 and 4^s+297: write 4C·p+1 for small C as a Lucas-sequence value or factor thereof and check whether a primitive divisor lands in the needed class.  
   `signature-0039` tags: F10, F30, primitive-divisors, thin-families, seen:BRAINSTORM/y3_lucas_dickson_trace.md, src:own, gen:integrator

40. **Zsigmondy: finite explicit exception list via elementary cyclotomic argument** [low/cheap] — a^n − b^n has a primitive prime divisor except for an explicit finite list. Shares F01, F25. Primitive divisors of a^n − 1 are ≡ 1 mod n. — *First step:* Check whether n-th primitive divisors of a^n + 1 (≡ 1 mod 2n) can be made ≡ −1 mod 4C after multiplying by known factors.  
   `signature-0040` tags: F10, F25, primitive-divisors, cyclotomy, src:own, gen:integrator

41. **Graham: every n > 77 is a sum of distinct integers with reciprocals summing to 1 — inductive (n → 2n+2, 2n+9) proof** [med/cheap] — Finite exceptions (F25) + all-n statement about unit fractions (F12) proved by an additive recursion. ES has only multiplicative closure (F02). — *First step:* Search ES solution tables for maps (x,y,z) at n ↦ solutions at 2n+1, 4n+1 etc.; test which affine maps preserve solvability on all n ≤ 10⁵.  
   `signature-0041` tags: F12, F25, F02, induction, seen:TRANSPORT_LAW.md, src:own, gen:integrator

42. **ES ⇒ m/n is a sum of m − 1 unit fractions for every m ≥ 4 (and 'm−1 terms' is a ladder)** [high/cheap] — m/n = (m−4)·(1/n) + 4/n, so ES gives m − 1 terms (with repeats). Flip: m/n in m − 2 terms is Sierpiński's 5/n problem for m = 5 (3 terms); for general m it trivially fails at small n (e.g. n = 1), and whether it holds for all large n is to be checked (for fixed 3 terms, Schinzel exceptions grow like exp(m^{1/3+o(1)}), Pomerance–Weingartner). F11, F12. — *First step:* Tabulate, for m ≤ 12 and n ≤ 10⁴, the least k with m/n a sum of k unit fractions; record the first m where k = m − 2 fails.  
   `signature-0042` tags: F11, F12, ladder, feature-flip, src:own, gen:integrator

43. **No diagonal ES solutions at p ≡ 1 (mod 4): the S₃ action on solutions is free** [high/cheap] — If x = y then 4/p = 2/x + 1/z forces a = 2x − p ∈ {1, p²} and 4 | p + 1, so p ≡ 3 (mod 4); same for y = z. Checked: no diagonal solution for any prime p ≡ 1 (4) below 1500; parity of the unordered count is 50/50 (scripts/z52b_signature_parity.py). — *First step:* Look for a non-S₃ involution (e.g. Vieta in the hyperbola fibre) whose fixed points are classifiable; count fixed points for p ≤ 10⁵.  
   `signature-0043` tags: F14, F38, involution, parity, new-computation, seen:INVOLUTION_ES.md, src:own, gen:integrator

44. **Zagier's one-sentence proof (windmill involution) as the canonical parity-existence template** [high/cheap] — p ≡ 1 mod 4 ⇒ sum of two squares via an involution with a unique fixed point. ES's hard primes are exactly p ≡ 1 mod 4 (F29). — *First step:* Search for a restricted ES subset (e.g. solutions with x minimal in its Vieta orbit) whose count parity is constant on hard primes ≤ 10⁵.  
   `signature-0044` tags: F29, F38, windmill, involution, seen:WINDMILL.md, src:own, gen:integrator

45. **Vose: every m/n is a sum of O(√log n) unit fractions — bounded vs. unbounded term counts** [med/cheap] — Vose's theorem gives a uniform term bound growing with n; ES fixes 3 terms (F12). Erdős conjectured O(log log n) suffices. — *First step:* Re-read Vose's construction and compute the number of terms it produces for 4/p, p hard, p ≤ 10⁹.  
   `signature-0045` tags: F12, feature-flip, smooth-numbers, src:own, gen:integrator

46. **Croot's coloring theorem / Bloom's density theorem: unit fractions inside dense sets** [med/medium] — Croot (Annals 2003): any finite colouring of ℕ has a monochromatic 1 = Σ1/x_i; Bloom (2021): positive upper density sets contain such sums. Shares F12, F05 (density statements). — *First step:* Identify the step in Bloom where many terms are needed and ask if a 3-term version with target 4/p survives under a smooth-number restriction.  
   `signature-0046` tags: F12, F05, unit-fractions, fourier, src:own, gen:integrator

47. **Sierpiński 5/n: numerator flip 4 → 5 — does a T1 analogue exist for 5/n?** [high/cheap] — 5/n = 1/x+1/y+1/z is open, conjectured always solvable. Shares nearly all ES features (F01, F12, F13, F05, F23); flips F11. — *First step:* Define 5/n Type I/II (n divides one/two denominators) and compute whether they vanish at odd squares n = m² for m ≤ 10³.  
   `signature-0047` tags: F11, F08, feature-flip, numerator, seen:FOUR_SPECIFIC.md, src:own, gen:integrator

48. **Numerator flip 4 → 8: failures at 17, 131, 241 as an anti-overreach test suite** [high/cheap] — 8/n has genuine exceptions (11, 17, 131, 241 among primes > 3; recomputed by brute force for p < 400) while satisfying the same local/BM features (needs check). Any ES argument must visibly use a property false for 8. — *First step:* For each tool collected in this lane, write one line: 'does the argument distinguish 4 from 8?'.  
   `signature-0048` tags: F11, calibration, numerator, seen:AMPLIFY_EXCEPTION.md, src:own, gen:integrator

49. **Schinzel's conjecture m/n three terms for n > N(m) with N(m) growing — Pomerance–Weingartner exceptions** [med/cheap] — For each m, ES-type solvability is conjectured for large n, with exceptions up to exp(m^{1/3+o(1)}) (F11). ES is the m = 4 case with N(4) = 1. — *First step:* Check the PW lower-bound construction for exceptions and whether its mechanism (covering by many small primes) can be run at m = 4.  
   `signature-0049` tags: F11, threshold, seen:FRONTIER.md, src:own, gen:integrator

50. **Feature flip: allow one negative unit fraction — 4/p = 1/((p−1)/4) − 1/(p(p−1)/4) trivially** [high/cheap] — Positivity (F27) is the whole difficulty: with signs, two terms suffice for p ≡ 1 mod 4. The positive cone is the 'boundary' making the surface log K3-like. — *First step:* Enumerate signed 3-term solutions with exactly one negative term for hard p and test whether some explicit birational move lands in the positive cone.  
   `signature-0050` tags: F27, feature-flip, positivity, cubic-surface, src:own, gen:integrator

51. **Feature flip: S-integral ES (denominators in ℤ[1/ℓ]) is trivial — integrality at every prime is essential** [med/cheap] — With ℓ = 2 or 3 allowed in denominators, 4/n = 3·(1/(3n/4)) or 1/n + 1/(n/3) work. Strong approximation away from S is cheap. — *First step:* For odd ℓ ≥ 5, determine the least S ∋ ℓ making ES trivial; record which S keep the problem nontrivial.  
   `signature-0051` tags: F07, F06, feature-flip, S-integral, src:own, gen:integrator

52. **ES over totally real fields with totally positive denominators (e.g. ℤ[√2])** [med/medium] — Over O_K with K totally real, require x,y,z totally positive: a genuine analogue keeping positivity (F27); over imaginary fields positivity disappears and the problem trivialises. — *First step:* Compute, for K = ℚ(√2), totally positive prime elements π of norm ≤ 10⁴ and search for 4/π = Σ 1/x_i with x_i ≫ 0; look for failures.  
   `signature-0052` tags: F26, F27, number-fields, feature-flip, src:own, gen:integrator

53. **Equal-denominator / chain sub-problems (x | y | z) as solvable slices** [med/cheap] — Restricting ES to chains x | y | z or to a fixed ratio y = kx gives two-variable divisor problems with explicit criteria; the diagonal x = y is empty for p ≡ 1 mod 4 (see diagonal item). — *First step:* For k = 2..20 compute which hard primes ≤ 10⁷ admit solutions with y = kx; tabulate densities.  
   `signature-0053` tags: F34, F15, slices, src:own, gen:integrator

54. **Polynomial identities in Gaussian coordinates: ES solutions as polynomials in (a,b) with p = a² + b²** [med/cheap] — Mordell–Schinzel forbid identities polynomial in p covering square classes (F09). Identities polynomial in (a,b) with p = a² + b² are not obviously excluded: at b = 0 they would give non-Type-I/II solutions or degenerate. — *First step:* For hard primes ≤ 10⁷ compute (a,b) and fit low-degree polynomial forms to the smallest solutions' denominators; check B1 Thm M's scope for procedures that use the two-squares decomposition.  
   `signature-0054` tags: F09, F29, identities, gaussian, B1-scope, src:own, gen:integrator

55. **Triangle altitude identity 1/r = 1/h_a + 1/h_b + 1/h_c: ES ⟸ triangle with integer altitudes and inradius n/4** [med/cheap] — Any triangle has Σ1/h = s/Δ = 1/r. ES solutions whose reciprocals satisfy the triangle inequalities correspond to triangles with integral altitudes x,y,z and inradius n/4 (rational sides up to scaling). — *First step:* For hard primes ≤ 10⁵, compute the fraction of ES solutions satisfying the triangle inequality on (1/x,1/y,1/z); look up 'triangles with integer altitudes' parametrisations.  
   `signature-0055` tags: geometry, reformulation, F12, triangles, src:own, gen:integrator

56. **Descartes/Soddy: three mutually tangent circles of radii x,y,z have inner Soddy curvature 1/x+1/y+1/z + 2√((x+y+z)/xyz)** [low/cheap] — ES fixes the linear part to 4/n; rationality of the Soddy curvature additionally needs (x+y+z)/(xyz) to be a rational square. Links ES to Apollonian-type curvature questions (F08 via HKRS). — *First step:* Count ES solutions (p ≤ 10⁵) where (x+y+z)·xyz is a square; if non-empty, look for Apollonian structure.  
   `signature-0056` tags: apollonian, geometry, F13, src:own, gen:integrator

57. **Manin–Chambert-Loir–Tschinkel prediction for integral points on the ES threefold vs. Elsholtz–Tao's N log³N** [med/medium] — The total space {4xyz = n(xy+yz+zx)} ⊂ A⁴ is a log Fano-type threefold; ET count Σ_{n≤N} f(n) ≍ N log³N (F04). CLT predict exponents from the Clemens complex of the boundary. — *First step:* Compute the boundary divisor and its Clemens complex for a compactification of the ES threefold; compare max-face dimension + 1 with 3.  
   `signature-0057` tags: F13, F04, manin-conjecture, integral-points, src:own, gen:integrator

58. **Wilsch: integral points of bounded height on a log Fano threefold — check if the ES threefold is of that type** [low/cheap] — Wilsch counted integral points on a specific log Fano threefold with torus-like structure. ES's threefold is a cubic with an (S₃ × scaling) symmetry. — *First step:* Check the definition of Wilsch's threefold and whether 4xyz = n(xy+yz+zx) is birational to it or to a toric variety.  
   `signature-0058` tags: F13, F04, manin-conjecture, src:own, gen:integrator

59. **Hilbert property for integral points (Corvaja–Zannier) applied to the fibration n: X → A¹** [low/medium] — ES says the image of X(ℤ)_{>0} under n covers ℤ_{≥2}. Corvaja–Zannier relate the Hilbert property/thin images to fundamental groups. Polynomial-identity families have thin images missing squares (F09). — *First step:* Check whether Mordell–Schinzel's impossibility is a special case of a Corvaja–Zannier-type 'images of integral points are thin' statement.  
   `signature-0059` tags: F09, F13, thin-sets, hilbert-property, src:own, gen:integrator

60. **Swinnerton-Dyer/Harpaz fibration method on the hyperbola fibration of the ES surface** [high/medium] — Fixing x, ES is a split hyperbola (ay − b)(az − b) = b² (F15) — integral points ↔ divisors of b² in a class. Harpaz (JEMS) handles conic log K3 surfaces by Swinnerton-Dyer's method conditionally / explicitly. — *First step:* Check Harpaz's definition (degree of the base, number of degenerate fibres, splitting) against the ES fibration in x.  
   `signature-0060` tags: F13, F15, fibration-method, log-K3, src:own, gen:integrator

61. **Sums of three cubes: no BM obstruction (Colliot-Thélène–Wittenberg), log-scale counts, big computations** [high/cheap] — x³+y³+z³ = n: affine cubic surface, all n ≢ ±4 mod 9 expected, BM-free, heuristic count ≍ log X up to height X, Booker–Sutherland searches. Shares F06, F07, F13, F23, F24. — *First step:* Compare the singular-series/BM local density formulas: does ES's BM-corrected main term have the same shape as Heath-Brown's density for cubes?  
   `signature-0061` tags: F06, F07, F13, F23, sums-of-three-cubes, feature-flip, src:own, gen:integrator

62. **Chen's Markoff mod p theorem (nonabelian level structures): ∀p connectivity via topology of moduli of covers** [med/big] — W. Chen proved every component of the Markoff mod-p graph has size divisible by p, completing Bourgain–Gamburd–Sarnak strong approximation for all large p. ∀p statement on a cubic surface proved via a non-analytic (algebro-topological) invariant. — *First step:* Check Chen's argument structure (Annals 2024) and whether ES word sets mod q carry an action of a mapping-class-like group.  
   `signature-0062` tags: F39, F13, markoff, strong-approximation, topological, src:own, gen:integrator

63. **Borwein conjecture (Chen Wang, Adv. Math. 2022): sign pattern of q-product coefficients by saddle-point + finite check** [med/medium] — ES ⟺ positivity/nonvanishing of coefficients of an explicit theta-quotient level series at prime indices (F19). Wang proved a coefficient sign pattern for all n analytically. — *First step:* Look for a manifestly positive (product/sum-of-squares) expression of Σ_n R(n)q^n restricted to a progression, e.g. via Andrews-style identities.  
   `signature-0063` tags: F19, q-series, positivity, feature-flip, src:own, gen:integrator

64. **Lehmer's τ(n) ≠ 0 and Serre lacunarity: coefficient non-vanishing classes** [med/cheap] — Nonvanishing of q-series coefficients at every index is ES's F19 form; CM forms vanish on a structured set (inert primes), ES's level series vanish at squares (T1). — *First step:* Compute the support of Σ_{t,u,v} q^{tuv−u−v} (4|t restriction) up to 10⁸ and test whether its complement is squares ∪ finite set (U(n) data).  
   `signature-0064` tags: F19, F08, nonvanishing, q-series, src:own, gen:integrator

65. **Erdős–Selfridge / Hough distortion method: positive uncovered density for 'small' covering families** [med/cheap] — Hough (Annals 2015) and Balister–Bollobás–Morris–Sahasrabudhe–Tiba show covering systems with large minimum modulus / Σ1/m small leave a positive density uncovered. ES's level sets {p : R_C(p) > 0} form an infinite 'covering' of primes (F34). — *First step:* Compute the density δ_C of primes covered by level C alone and Σ_C δ_C up to C ≤ 10³; compare with the BBMST criterion.  
   `signature-0065` tags: F34, covering-systems, sieve, src:own, gen:integrator

66. **Lovász local lemma / Janson for 'avoid all levels': lower tail of R(p) as a dependency-graph problem** [high/cheap] — R(p) = 0 means p avoids all level events; Janson's inequality bounds P(no event) by exp(−μ + Δ). ES needs this pointwise, but the probabilistic version gives the correct heuristic decay. — *First step:* Compute Δ (pair correlation of level events) for hard primes ≤ 10⁸ to see whether μ − Δ grows like log²p.  
   `signature-0066` tags: F04, F24, janson, seen:EXSET_ARITH_JANSON_OPUS.md, src:own, gen:integrator

67. **Shrinking-target / hitting-time for the Gauss map: λ(p) ≤ 3 as 'some orbit hits a target in ≤ 3 steps'** [med/cheap] — ES₅: for each p there is q with p/q of continued-fraction length ≤ 3 (with constraints). In dynamics language: some rational point of denominator p reaches a target set within 3 Gauss-map steps. — *First step:* Check Ustinov's results on the statistics of continued-fraction lengths of a/p for fixed p (number of a with length ≤ k).  
   `signature-0067` tags: F17, continued-fractions, dynamics, gauss-map, src:own, gen:integrator

68. **Zaremba ↔ ES₅ duality: bounded alphabet/unbounded length vs. bounded length/unbounded alphabet** [high/cheap] — Zaremba (density one: Bourgain–Kontorovich; Huang) bounds partial quotients; ES₅ bounds the length (≤ 3). Both are 'every denominator p has an a with a CF constraint' (F01, F17). — *First step:* Compute #{a mod p : λ(a/p) ≤ 3 with ES₅ constraints} for hard p and fit c·log²p.  
   `signature-0068` tags: F17, zaremba, thin-orbit, seen:ZAREMBA_TRANSFER.md, src:own, gen:integrator

69. **Continuants: p = K(a,b,c) = abc + a + c (positive CF) vs ES's negative continuant tuv − u − v** [high/cheap] — Length-3 continuants K(a,b,c) = abc + a + c represent every n > ? trivially (a = c = 1: b + 2), while the negative-CF version with a 4ℤ constraint is ES. The sign flip is the feature (F16, F27). — *First step:* For the 4 sign patterns of abc ± a ± c with a 4ℤ constraint on one coordinate, compute failure sets among primes ≤ 10⁷.  
   `signature-0069` tags: F16, F17, continuants, feature-flip, ladder, src:own, gen:integrator

70. **ES is a Π₁⁰ sentence (bounded witness) — like Goldbach and RH** [med/cheap] — All denominators in a 3-term representation of 4/n are ≤ poly(n) (F32), so ES is ∀n ∃(bounded) — Π₁. Independence from PA/ZFC would imply truth. — *First step:* Write a minimal Turing machine (or Lean decidable predicate) that halts iff ES fails; compare its size with the bbchallenge Goldbach machines.  
   `signature-0070` tags: F32, logic, complexity, src:own, gen:integrator

71. **Is finding ES witnesses as hard as factoring p-tied integers?** [med/cheap] — Witnesses ⟺ divisors of 4Cp+1 in a class (F10). Known fast heuristic (scan small C, factor small numbers). An ES-oracle reveals factors of 4Cp+1 for some C. — *First step:* Measure, for p ≈ 10³⁰, the cost of the cheapest witness search (smallest C with a smooth enough 4Cp+1); check if it ever requires factoring a hard number.  
   `signature-0071` tags: F32, F10, complexity, algorithmic, src:own, gen:integrator

72. **Scholz–Brauer addition chains: ∀n statement proved on infinite thin families, open in general** [low/cheap] — l(2^n − 1) ≤ n − 1 + l(n) is proved for many infinite families and verified computationally, open in general — the same 'thin families proved, no density rung' profile as ES (F30, F23). — *First step:* Read Clift's computational verification and check whether the proved families cover a positive density of n.  
   `signature-0072` tags: F30, F23, addition-chains, thin-families, src:own, gen:integrator

73. **Erdős–Straus over F_q[T] (proved variants) as the 'function field sibling' with the same features** [high/cheap] — Polynomial analogues have proved versions (F26); the obstruction mechanisms (T1 analogue, degree/positivity substitute) can be compared exactly. — *First step:* List the proof ingredients of the F_q[T] theorems in FUNCTIONFIELD_ES*.md and mark each as 'available over ℤ' or not.  
   `signature-0073` tags: F26, function-field, seen:FUNCTIONFIELD_ES.md, src:own, gen:integrator

74. **Primes p ≡ 1 mod 4 as norms: ES-hardness vs. splitting in many imaginary quadratic fields ℚ(√−uB)** [high/medium] — M_BM(p) small ⟺ χ_{−4uB}(p) = +1 for many small pairs, i.e. p splits in many ℚ(√−uB) — Chebotarev in a large compositum. Hard primes are 'maximally split' primes (F20, F29). — *First step:* Compute R(p) for the first primes totally split in ℚ(i, √−3, √−5, √−7, √−11, …) (L up to 40) and compare with random p of same size.  
   `signature-0074` tags: F20, F29, chebotarev, adversarial, src:own, gen:integrator

75. **Representation of p by x² + ny² for many n simultaneously (Cox) as a model of 'p a square mod everything small'** [med/cheap] — Hard ES primes are squares modulo many small moduli (Mordell classes mod 840 are squares). Cox's theory characterises p = x² + ny² via ring class fields; the simultaneous version is a Chebotarev condition. — *First step:* For hard primes ≤ 10⁸ count n ≤ 100 with p = x² + ny² and correlate with R(p)/log²p.  
   `signature-0075` tags: F29, F20, class-field-theory, src:own, gen:integrator

76. **Bourgain–Garaev sums of reciprocals in F_p: modular ES with small denominators** [low/medium] — The congruence 4·n⁻¹ ≡ x⁻¹ + y⁻¹ + z⁻¹ (mod q) with small x,y,z is a Kloosterman-type sumset problem with sharp results; the integral ES requires the exact equation. — *First step:* Check the Bourgain–Garaev 'sumsets of reciprocals' results and whether the ES equation mod 4Cp+1 reduces to such a sumset.  
   `signature-0076` tags: F33, sum-product, kloosterman, modular, src:own, gen:integrator

77. **Agoh–Giuga / Znám problems: unit-fraction equations with divisibility, finite solution families** [low/cheap] — Znám's problem (each x_i | Π_{j≠i}x_j + 1) and Giuga numbers mix unit fractions with divisibility (F12, F10). Znám's problem solved for k ≥ 5 (Sun Qi) by construction. — *First step:* Check whether Sun Qi's construction yields 3-term identities for 4/n in any infinite family of primes.  
   `signature-0077` tags: F12, F10, unit-fractions, constructions, src:own, gen:integrator

78. **Breusch/Stewart: every rational with odd denominator is a finite sum of distinct odd unit fractions** [med/cheap] — Solved universal unit-fraction statement under a parity restriction; ES fixed-length with no parity constraint. Note: for odd n, 4/n with all three denominators odd is impossible (4xyz is even but n(xy+yz+zx) is odd), so ES at odd n always uses an even denominator. — *First step:* Determine the possible 2-adic valuation patterns (v₂(x), v₂(y), v₂(z)) of ES solutions at hard primes ≤ 10⁵.  
   `signature-0078` tags: F12, F29, 2-adic, feature-flip, src:own, gen:integrator

79. **Odd greedy expansion termination (open): an algorithm-existence problem in unit fractions** [med/cheap] — Does the odd greedy algorithm always terminate on a/b with b odd? Open, verified computationally. ES: does a natural greedy-type search always find a 3-term solution? (no — greedy gives more terms). — *First step:* Compute min k such that 4/p − 1/(⌈p/4⌉+k) is a sum of 2 unit fractions, for hard primes ≤ 10⁹; study the distribution of k.  
   `signature-0079` tags: F12, algorithmic, greedy, src:own, gen:integrator

80. **Rav / Bernstein criterion for m/n = 1/x + 1/y (divisor sums a + b ≡ 0 mod m) as the 2-term base case** [high/cheap] — m/n is a sum of 2 unit fractions iff there are coprime divisors a, b of n (or of n²-related numbers) with m | a + b. ES's hyperbola fibres apply this after choosing x (F15). — *First step:* State the criterion precisely for (4x − n)/(nx) and check equivalence with Type I/II divisor forms.  
   `signature-0080` tags: F15, F10, two-term, base-case, src:own, gen:integrator

81. **Huang–Vaughan mean values for binary Egyptian fractions** [med/cheap] — Counts of n ≤ N such that m/n is a sum of 2 unit fractions, and mean values of the representation counts (feature F04, F05 for the 2-term problem). — *First step:* Check the exact statements of Huang–Vaughan and whether their mean-value bound is uniform enough to sum over the ES parameter x.  
   `signature-0081` tags: F04, F05, two-term, mean-values, src:own, gen:integrator

82. **Elsholtz–Planitzer lower bounds for f(n) — the 'typical count' sibling** [high/cheap] — Lower bounds for the number of solutions for almost all n / for primes in residue classes (F04, F05) via multiplicative structure; check whether the bound f(n) ≥ (log n)^{log 6 + o(1)} for almost all n is the one stated there (the abstract states a lower bound exp((5 log 2/(12 lcm(m,f)) + o(1)) log p/log log p) for infinitely many primes p in each class). — *First step:* Check how the almost-all lower-bound exponent arises and whether a 'prime-shifted' version (using factors of 4Cp+1 instead of n) gives a lower bound for most C.  
   `signature-0082` tags: F04, F05, counting, seen:FRONTIER.md, src:own, gen:integrator

83. **Absorption method (Ringel, Erdős–Faber–Lovász): approximate structure + absorber ⇒ exact** [low/cheap] — Combinatorial ∀n∃ conjectures were solved by building most of the object randomly and absorbing the leftovers. ES analogue: '4/p − (a cheap unit fraction) has a 2-term decomposition' succeeds for almost all choices; the absorber is the freedom in x. — *First step:* For hard primes ≤ 10⁸ find the minimal set X(p) of x-values (in terms of p mod small numbers) that always contains a working x; test stability.  
   `signature-0083` tags: F05, absorption, combinatorics, methodology, src:own, gen:integrator

84. **Collatz (Tao 2019): almost all orbits attain almost bounded values via logarithmic density — the exceptional-set-improvement analogue** [med/medium] — ∀n conjecture (F01), almost-all known (F05), huge verification (F23), heuristic support (F24). Tao's key was changing the measure (logarithmic density) to gain an approximate invariance. — *First step:* Recompute the ES exceptional-set argument with logarithmic density in n and see whether the 3/4 barrier changes.  
   `signature-0084` tags: F05, F40, collatz, logarithmic-density, seen:EXCEPTIONAL_KARY3.md, src:own, gen:integrator

85. **ES as a Hurwitz-type equation with a Vieta group: orbit counts per n** [med/cheap] — Hurwitz equations Σx_i² = a·Πx_i have finitely many fundamental solutions per (n,a) generating trees under Vieta moves; ES's word set has a forest structure (F39). Counting fundamental solutions vs. n is a solved problem type. Caveat: tuv − u − v and the ES cubic are multilinear, so classical Vieta root swaps do not exist on them; the analogue must use other involutions/birational moves. — *First step:* Search for involutions or birational moves on (t,u,v) preserving tuv − u − v = p (e.g. moves through the divisor pairing d ↔ (4Cp+1)/d, swaps across levels) and compute orbit structure for p ≤ 10⁴.  
   `signature-0085` tags: F38, F39, vieta, markoff-hurwitz, seen:FOREST_CONNECTIVITY.md, src:own, gen:integrator

86. **Mordell's equation for 1/x + 1/y + 1/z = 1/w: complete parametrisation of the rational cubic surface** [med/cheap] — The ES surface is rational; full rational parametrisations (e.g. of Σ1/x_i = 1/w) exist. Integral points of the ES fibre are thin inside the rational points (F13). — *First step:* Write the standard parametrisation of 1/x+1/y+1/z = 1/w and substitute w = n/4; record the integrality conditions as divisibility conditions.  
   `signature-0086` tags: F13, parametrisation, rational-surface, src:own, gen:integrator

87. **Feature flip F04: raise the expected count by allowing 4 terms with all denominators > n — does pointwise become easy?** [med/cheap] — 4 terms trivial with repeats (1/n ×4); with distinct denominators all > n, the count becomes polynomial in n and circle/divisor methods apply. — *First step:* Characterise when 1/a + 1/b is a unit fraction (a = k(k+l)… form) and count 4-term solutions mergeable to 3 terms for hard p.  
   `signature-0087` tags: F04, feature-flip, descent, src:own, gen:integrator

88. **Feature flip F28: forbid Type I (p | exactly one denominator) — Type II alone fails at 14+ primes; union never fails ≤ 10⁸** [high/cheap] — Restricting the type creates explicit failure sets ((★) fails at 14 primes ≤ 10¹⁰; b = 1 line at 3 primes ≤ 10¹¹); their union survives. Shares the 'two families, each with sparse failures, disjoint failure sets' structure with Heath-Brown's Artin and with Goldbach-type unions. — *First step:* Compute for p ≤ 10⁹ the joint distribution of (R_(★)(p), R_{b=1}(p)) and test for negative correlation at small values.  
   `signature-0088` tags: F28, F25, feature-flip, two-families, seen:B1_LINE.md, src:own, gen:integrator

89. **Feature flip F02: problems without multiplicative closure (Goldbach) can't reduce to primes — ES's prime reduction as an asset** [low/cheap] — ES(n) ⇐ ES(d) for d | n reduces to primes; for primes the multiplicative structure of n is gone. Conversely, composites have MORE solutions (Elsholtz–Planitzer). — *First step:* For hard p, find the smallest k such that 4/(pk) has a solution with k dividing all three denominators — equals ES(p) — but study the distribution of 'near-misses' (k dividing two denominators).  
   `signature-0089` tags: F02, feature-flip, src:own, gen:integrator

90. **Feature flip F06: Legendre's three squares (local obstruction 4^a(8b+7)) — what local obstruction would look like for ES** [med/cheap] — Three-squares fails exactly on a locally-defined set; ES has none (F06). Where local obstructions are absent, ternary problems were solved via class numbers (Gauss). — *First step:* Write the ES local densities at 2 and at p and confirm they never vanish at hard primes (sanity check for BL).  
   `signature-0090` tags: F06, feature-flip, three-squares, src:own, gen:integrator

91. **Feature flip F21: problems where a pointwise bound came from averaging over an auxiliary parameter of length ≫ polylog** [med/cheap] — Pointwise results (Linnik p + x² + y², Vinogradov three primes, Duke ternary) all average over an auxiliary variable of polynomial length. ES's auxiliary variables (C, u, B) have polynomial range but polylog effective mass. — *First step:* Search for a weighting w(C,u,B) with Σ w·1[event] provably positive and mass ≫ p^δ — e.g. weights from smooth-number counts.  
   `signature-0091` tags: F21, feature-flip, weights, src:own, gen:integrator

92. **Feature flip F17: CF length ≤ 2 — which primes are length-2 (two-term) representable — fully explicit** [med/cheap] — λ(p) ≤ 2 corresponds to 2-term-type representations, characterised by divisor conditions (Rav). ES₅ is the length-3 rung. — *First step:* Compute the density of primes with λ(p) ≤ 2 (under ES₅ constraints) — should decay like a power of 1/log.  
   `signature-0092` tags: F17, feature-flip, ladder, src:own, gen:integrator

93. **Feature flip F20: if only real characters contributed (pure genus count), ES would follow from genus theory** [med/cheap] — R*(n) = M_gen(n) + X(n); M_gen is genus (order ≤ 2 characters), X the rest. Problems where only genus characters appear (class number one, idoneal discriminants) are solved by genus theory. — *First step:* For hard primes, compute X(p)/M_gen(p) and correlate with the 2-rank vs. size of class groups of ℚ(√−p·small).  
   `signature-0093` tags: F20, feature-flip, genus-theory, idoneal, src:own, gen:integrator

94. **Feature flip F37: one-sided statements — 'R(p) ≥ ε·M(p)' vs. two-sided — examples of proved one-sided lower bounds** [med/cheap] — Two-sided asymptotics are false for R(p) (Linnik-type large values). Proved one-sided lower bounds of the right order exist for e.g. Σ_{n ≤ x} λ-type sieve problems (Chen) but not pointwise for polylog counts. — *First step:* Literature search: 'pointwise lower bound' 'representation number' 'log' — look for any theorem giving r(n) ≫ (log n)^c for all n in a natural problem.  
   `signature-0094` tags: F37, F21, feature-flip, precedent-search, src:own, gen:integrator

95. **Precedent search: theorems giving r(n) ≫ (log n)^c for ALL n (polylog pointwise lower bounds)** [med/cheap] — Examples to check: number of prime factors-related counts, r(n) for sums of a prime and a square-free?, number of divisors in a dense set; the 'every n has ≫ log n representations as p + 2^a + 2^b' type (false). F04 + F21. — *First step:* Ask MathOverflow-style search: 'every integer has at least log n representations'; check Erdős–Fuchs-type and additive-basis-order results.  
   `signature-0095` tags: F04, F21, precedent-search, meta, src:own, gen:integrator

96. **Feature flip F35: problems where bounded certificate schemes DO work (Pratt certificates for primality) vs ES's B1** [low/cheap] — Primality has short certificates (Pratt) found by structured search, but no bounded formula; ES has short certificates (F32) and B1 forbids bounded procedures under Schinzel H. — *First step:* Check whether an ES solution for p can be assembled from ES-like data for prime factors of 4Cp+1 (recursive certificate).  
   `signature-0096` tags: F35, F32, certificates, recursion, src:own, gen:integrator

97. **Feature flip F26: ES over F_q[T] (proved variants) vs. ℤ — the missing Weil-type pointwise bound** [med/cheap] — In F_q[T], pointwise character-sum bounds (Weil/Deligne) are available at a single modulus; over ℤ only Burgess-type. That is the B2 gap. — *First step:* Translate the F_q[T] proof into the needed ℤ-estimate and check whether it is implied by GLH or is stronger.  
   `signature-0097` tags: F26, F36, feature-flip, character-sums, src:own, gen:integrator

98. **Gauss Eureka (n = Δ + Δ + Δ ⟺ 8n + 3 = sum of three odd squares): linear change of variable to a local-global problem** [med/cheap] — ∀n statement solved by transforming n ↦ 8n + 3 and invoking three squares. ES's divisor forms also transform p ↦ 4Cp + 1, p + 4d (F10). — *First step:* Look for an ES equivalent with a single affine transform (e.g. a statement about 4p + 1 alone with a richer witness) — e.g. via the Frobenius semigroup item.  
   `signature-0098` tags: F10, F01, reformulation, local-global, src:own, gen:integrator

99. **Waring's problem: G(3) and the finite exceptional sets (23, 239 need 9 cubes)** [med/cheap] — ∀n statements with finite explicit exception lists (F25), proved via circle method + explicit computation; 'every large n is a sum of 4 cubes' open (count polylog-ish? no — n^{1/3}). — *First step:* List which ES-program steps would, mutatis mutandis, prove 'every large n is a sum of 4 cubes' (calibration).  
   `signature-0099` tags: F25, F05, calibration, waring, src:own, gen:integrator

100. **Schinzel–Sierpiński: every positive rational is (p+1)/(q+1)? — follows from Hypothesis H; ES's B1 uses H in the opposite direction** [med/cheap] — Under Schinzel's H many ∀∃ prime statements hold; for ES, H implies every bounded procedure fails (B1 Thm C). Shares F35, F01. — *First step:* Ask whether H also implies ES (it supplies primes in polynomial families — could it supply divisors in classes?) — likely not, but record why.  
   `signature-0100` tags: F35, hypothesis-H, conditional, src:own, gen:integrator

101. **Chen's theorem (p + 2 = P₂) and 'almost-ES' with a relaxed term** [med/cheap] — Chen circumvented parity by allowing almost-primes. ES analogue: 4/p = 1/x + 1/y + a/z with a small, or with one denominator only 'almost integral' (z ∈ ½ℤ). Note numerator 2 makes ES trivial for p ≡ 1 mod 4 (4/p = 1/x + 1/y + 2/z). — *First step:* Check triviality for relaxations: (i) z ∈ ½ℤ, (ii) one denominator may be divisible by p², (iii) a/z with a = 3; record first nontrivial one.  
   `signature-0101` tags: F22, relaxation, parity, ladder, src:own, gen:integrator

102. **Hardy–Littlewood Conjecture H (large non-square n = p + k²) / Bateman–Horn: singular series with Legendre-symbol factors** [med/cheap] — Representation counts whose singular series involve (n/ℓ) — e.g. HL Conjecture H, where squares n are excluded (n − k² factors). ES's main term M_BM has the same Legendre-symbol structure and also degenerates at squares (F20, F08). — *First step:* Compare M_BM(p)/M₀(p) with a Bateman–Horn-type product ∏(1 − (p/ℓ)/(ℓ−1)) — is it asymptotically such a product?  
   `signature-0102` tags: F20, singular-series, heuristic, src:own, gen:integrator

103. **Elliott–Halberstam-type level of distribution for divisor-in-class counts (Fouvry–Iwaniec, Friedlander–Iwaniec d₃)** [med/medium] — Distribution of τ-type functions in APs beyond √x is known for d₂ (Selberg/Hooley/Heath-Brown) and d₃ (Friedlander–Iwaniec, Fouvry–Kowalski–Michel). ES sums divisor-in-class counts over p-tied integers. — *First step:* Check whether the 3/4 exceptional-set barrier (F40) can be moved by a d₃-in-APs level beyond 1/2 input.  
   `signature-0103` tags: F40, F10, level-of-distribution, B2, src:own, gen:integrator

104. **OEIS search: numbers not of the form tuv − u − v (t,u,v ≥ 2) and with 4 | t — is the sequence in OEIS?** [high/cheap] — U(n)'s failure set (odd squares + {105, 2961, 3985, 25305, 111969, 978145}) is an explicit sequence; if it (or its variants) appears in OEIS, cross-references may reveal an independent characterisation. — *First step:* Query OEIS for 105, 2961, 3985, 25305 and for the 14 (★) failure primes (409, …, 8813281).  
   `signature-0104` tags: F25, oeis, data, src:own, gen:integrator

105. **OEIS A005097 (odd primes − 1)/2 ↔ numbers not of form 2xy + x + y: the bilinear primality template** [high/cheap] — n ≠ 2xy + x + y ⟺ 2n + 1 prime: the simplest 'trilinear-word ⟺ primality' dictionary. ES's (★) word is the level-4C version with a sign flip. — *First step:* Generalise: for the form t·xy − x − y with fixed t, characterise non-represented n via divisors of tn + 1 ≡ −1 mod t; tabulate t = 2..12.  
   `signature-0105` tags: F16, F10, oeis, primality, src:own, gen:integrator

106. **Burgess bound for least quadratic nonresidue** [high/medium] — Like ES, this asks for a witness prime uniformly for each input; the least nonresidue bound is a pointwise rather than average result (F01,F21). Unlike ES it has a square-class failure built into the input (F08w). — *First step:* For prime p, compare Burgess's character-sum proof with the incomplete character sums implicit in R(p); check whether a Burgess-style bound can force a nonzero count.  
   `signature-0106` tags: F01, F08w, F21, solved, src:journal-search, character-sums, gen:sub-classical

107. **Ankeny conditional least-nonresidue bound as a pointwise template** [med/big] — Ankeny's GRH result is a uniform individual-input bound, matching F01/F21; its quadratic-residue obstruction on squares echoes F08w. It is a precise conditional pointwise existence template, not a direct analogue of ES's witness equation. — *First step:* Write R(p) in character-sum form and test whether its principal and real-character terms admit an explicit-formula lower bound under GRH.  
   `signature-0107` tags: F01, F08w, F20, F21, solved, conditional, GRH, gen:sub-classical

108. **Bach–Sorenson explicit GRH least-prime bounds** [med/big] — The least-prime-in-a-class problem has a single-input/single-witness formulation (F01,F21), and a finite exceptional regime controlled by explicit estimates. Its class-group characters resemble the character sums in ES (F20). — *First step:* Read Bach–Sorenson's explicit GRH bounds and identify the exact zero-sum inequality; test its analogue on the finite character expansion defining R(p).  
   `signature-0108` tags: F01, F20, F21, solved, conditional, GRH, explicit-formula, gen:sub-classical

109. **Hooley's conditional proof of Artin primitive roots** [high/big] — Under GRH, Hooley obtains pointwise-in-the-fixed-base infinitude of prime witnesses through a sieve over divisors (F01,F21,F22); this is structurally close to ES's character/divisor counting (F10,F20). — *First step:* Inspect Hooley's tail estimate over prime divisors of p−1 and ask whether an analogous truncation handles the moduli C in R(p).  
   `signature-0109` tags: F01, F10, F20, F21, F22, solved, conditional, GRH, sieve, gen:sub-classical

110. **Heath-Brown's one-of-three primitive-root theorem** [high/medium] — A pointwise family of three candidate bases guarantees that at least one succeeds infinitely often; this is an infinite-family covering result (F34) rather than a single-input universal theorem. It offers a contrasting way to combine several incomplete witness families (F08,F34). — *First step:* Identify the exact three-base linear sieve lemma in Heath-Brown and see if ES certificate-line sets have a comparable pairwise independence property.  
   `signature-0110` tags: F08, F22, F34, solved, partial, sieve, primitive-root, gen:sub-classical

111. **Gupta–Murty simultaneous primitive-root sieve** [med/medium] — A sieve combines several candidate primitive-root conditions on primes; this resembles combining ES's thin certificate families (F22,F34), with pointwise restrictions (F21). — *First step:* Check Gupta–Murty's sieve inequality for a usable lower bound on a union; formulate the analogous count for ES line certificates modulo p.  
   `signature-0111` tags: F21, F22, F34, solved, sieve, primitive-root, gen:sub-classical

112. **Borwein–Choi on idoneal numbers and three-variable factorization** [med/big] — The equation n=xy+yz+zx is a three-variable bilinear representation with divisor parametrizations (F10,F16w), and the idoneal-number result is pointwise with at most a possible exceptional value under hypotheses (F01,F21). — *First step:* Read the exact Borwein–Choi theorem and isolate how class-group characters bound the exceptional discriminant; compare the genus term with R(p)'s real-character term.  
   `signature-0112` tags: F01, F10, F16, F20, F21, solved, quadratic-forms, gen:sub-classical

113. **Weinberger's at-most-one idoneal exception** [med/big] — Weinberger's class-group results imply at most two idoneal numbers beyond Euler's list exist, and none under GRH: a universal representation theorem with a possible tiny ineffective exceptional set matches ES's ∀n-with-exceptions shape (F01,F21) and the possibility that ineffective class-number bounds leave unresolved cases (F36). — *First step:* Trace the class-number lower bound and Tatuzawa-style exceptional-discriminant step, then ask what a similarly effective bound on ES's character sum would give.  
   `signature-0113` tags: F01, F20, F21, F36, solved, conditional, GRH, Siegel-ineffectivity, gen:sub-classical

114. **Duke–Schulze-Pillot representation by ternary forms** [high/medium] — A fixed ternary quadratic form represents almost all locally represented integers, with exceptional square classes; this matches local-to-global arithmetic and square-class failure (F06,F08w), but ES needs every integer (F01). — *First step:* Read the theorem's spinor-exception square-class condition and test whether ES's failed certificate subfamilies can be organized into analogous square classes.  
   `signature-0114` tags: F01, F06, F08w, F20, solved, partial, quadratic-forms, spinor-exceptions, gen:sub-classical

115. **Ono–Soundararajan GRH test for Ramanujan's ternary form** [med/big] — Representability by x²+y²+10z² is reduced to local eligibility plus an analytic pointwise argument; under GRH Ono–Soundararajan show the only odd non-represented integers are 18 explicit ones (largest 2719) (F06,F21,F25). — *First step:* Fetch the Ono–Soundararajan paper and extract the precise GRH hypothesis and eligible-number inequality; substitute ES's divisor count for its representation coefficient.  
   `signature-0115` tags: F01, F06, F08w, F21, F31, solved, conditional, GRH, gen:sub-classical

116. **Bhargava–Hanke 290 theorem: finite test set** [high/big] — Universality of a quadratic form is decided by finitely many small represented integers, matching F01 and a finite certificate/candidate reduction (F32); ES's finite congruence cover (F03) is a related finite reduction, though not a fixed test set. — *First step:* Read the 290 theorem proof's escalation and local-global steps; test whether ES's finite Mordell covering can be turned into an escalation criterion for certificate classes.  
   `signature-0116` tags: F01, F03, F32, solved, quadratic-forms, finite-criterion, gen:sub-classical

117. **Linnik's theorem for p plus two squares** [med/big] — A pointwise representation n=p+x²+y² combines a prime with a quadratic-form witness (F01,F31,F33); its dispersion method controls a thin arithmetic set (F21,F22). — *First step:* Locate the dispersion inequality in the proof and test an analogous second-moment estimate for the ES divisor-count R(p), stratified by C.  
   `signature-0117` tags: F01, F21, F22, F31, F33, solved, dispersion, gen:sub-classical

118. **Heath-Brown–Puchta: Goldbach–Linnik with powers of two** [med/big] — Every large even integer is a sum of two primes and a bounded number K of powers of 2 (Heath-Brown–Puchta: K = 13), matching F01w,F21,F33; the powers-of-two summands form a thin structured family (F30). — *First step:* Check the theorem's exact exceptional range and identify the major/minor arc estimate that supplies pointwise coverage; compare with ES certificate lines.  
   `signature-0118` tags: F01w, F21, F22, F30, F33, solved, circle-method, sieve, gen:sub-classical

119. **Pintz–Ruzsa: two primes plus K = 8 powers of two** [low/medium] — Pointwise additive representation of every large even integer by two primes plus a few elements of a highly sparse set (powers of 2; Pintz–Ruzsa K = 8) (F01w,F30,F33), with circle-method estimates bridging density to all sufficiently large inputs (F21). — *First step:* Read the Pintz–Ruzsa bound for the exponential sum over powers of two and test whether ES certificate parameters have usable Fourier decay.  
   `signature-0119` tags: F01w, F21, F30, F33, solved, circle-method, Fourier, gen:sub-classical

120. **Helfgott's ternary Goldbach proof** [high/big] — Every odd integer > 5 is a sum of three primes (Helfgott), an additive three-witness pointwise theorem (F01,F12,F21,F33); the proof combines circle method for n ≥ N₀ with explicit finite verification below (F23). — *First step:* Read Helfgott's major-arc lower bound and explicit minor-arc constants; ask whether a similarly explicit lower bound for R(p) could bridge the remaining finite interval.  
   `signature-0120` tags: F01w, F12, F21, F23, F33, solved, circle-method, computation, gen:sub-classical

121. **Romanoff's theorem on prime plus powers of two** [high/medium] — A positive proportion of integers have form p+2^k, giving a positive-density witness subset (F05w,F30,F33), unlike ES's universal target (F01). — *First step:* Compare Romanoff's lower-density proof with the ES almost-all exceptional-set proof and identify whether a pointwise lower bound can survive for residue classes of p.  
   `signature-0121` tags: F05w, F30, F33, partial, additive-primes, density, gen:sub-classical

122. **Erdős's covering argument for prime plus powers of two** [med/medium] — The complement of n=p+2^k is controlled by congruence covering phenomena, resembling ES's finite congruence cover (F03) and thin-family unions (F34). — *First step:* Write the covering congruence system in the Erdős argument and test whether ES failed primes have a finite modular covering explanation.  
   `signature-0122` tags: F03, F08, F34, partial, covering-congruences, gen:sub-classical

123. **Crocker's prime plus two powers of two obstruction** [low/medium] — The equation p+2^a+2^b=n has an explicit exceptional/obstruction structure (F01,F08w,F30,F33), contrasting positive-density coverage with universal coverage. — *First step:* Read Crocker's construction (check whether his non-represented integers form a sparse family like 2^{2^m}−1 rather than residue classes) and compare its mechanism with the ES residue cover modulo 840 and the failed (★) primes.  
   `signature-0123` tags: F01, F03, F08w, F30, F33, partial, obstructions, gen:sub-classical

124. **Cramér–Maier matrix method for pointwise short intervals** [med/medium] — The matrix method extracts pointwise irregularities at polylogarithmic scales (F04w,F21,F37), sharing ES's delicate pointwise-versus-average issue (F05,F21). — *First step:* Build the analogous residue-class-by-C matrix for R(p) over a modest prime range and test whether Maier-style row/column discrepancies appear.  
   `signature-0124` tags: F04w, F21, F37, solved, matrix-method, irregularity, gen:sub-classical

125. **Zsigmondy's theorem and its finite exceptional list** [med/medium] — Every n>1 has a new prime divisor in a cyclotomic difference except explicit small cases (F01,F23); cyclotomic factorization gives a short witness (F32) and finite exceptions (F25). — *First step:* Check whether any ES parametrization yields a cyclotomic factor whose primitive divisor forces d≡−1 mod 4C; begin with 4Cp+1.  
   `signature-0125` tags: F01, F25, F32, solved, factorization, finite-exceptions, gen:sub-classical

126. **Bilu–Hanrot–Voutier primitive divisors in Lucas sequences** [med/medium] — A uniform primitive-divisor theorem gives a short prime witness for each sufficiently large sequence index, with a finite explicit exception regime (F01,F25,F32). — *First step:* Read the BHV primitive divisor definition and test whether primitive factors of 4Cp+1 can lie in the required residue class −1 mod 4C.  
   `signature-0126` tags: F01, F10, F25, F32, solved, Lucas-sequences, gen:sub-classical

127. **Congruent primes via Heegner and Monsky arguments** [low/big] — The congruent-number property for primes in particular residue classes has pointwise arithmetic criteria (F01,F29,F31), and elliptic-curve descent converts the question into a local/global witness problem (F06,F07). — *First step:* Check the exact prime congruence classes and descent construction in Monsky's result; compare the resulting 2-adic local conditions with ES's F29 split case.  
   `signature-0127` tags: F01, F06, F07, F29, F31, solved, elliptic-curves, gen:sub-classical

128. **Tunnell's theta-series criterion for congruent numbers** [high/medium] — Tunnell gives a computable ternary quadratic-form criterion for a rational-point question (necessary; sufficient assuming BSD), matching ES's quadratic-form reformulations and theta-series coefficient lens (F19,F31). — *First step:* Read Tunnell's theorem statement and compare the two weighted representation counts with the ES theta-quotient coefficient; seek an analogous exact criterion.  
   `signature-0128` tags: F19, F31, solved, partial, theta-series, elliptic-curves, gen:sub-classical

129. **Tian's rank results for congruent-number curves** [low/big] — A family-wide rank argument yields pointwise conclusions for primes in selected classes (F01p,F29,F31), through Selmer and analytic rank structures rather than direct counting. — *First step:* Verify Tian's exact residue-class rank theorem and identify the Selmer parity input; test for an analogous parity constraint on ES certificate counts.  
   `signature-0129` tags: F01p, F29, F31, solved, elliptic-curves, descent, gen:sub-classical

130. **Smith's positive proportion of congruent numbers via Selmer groups** [low/big] — A positive-proportion theorem for a thin arithmetic property shares ES's local solubility and global integral-witness divide (F06,F07,F31), but is density-level rather than pointwise (F05w). — *First step:* Check Smith's Selmer distribution theorem hypotheses and ask whether a 2-Selmer-like object exists for the ES cubic surface family.  
   `signature-0130` tags: F05w, F06, F07, F31, partial, Selmer-groups, gen:sub-classical

131. **Zagier's involution for sums of two squares** [low/medium] — A constructive involution pairs representations and establishes a universal arithmetic assertion through symmetry (F14,F38), with an explicit short witness (F32). — *First step:* Write the Zagier involution on the relevant finite representation set and test whether ES divisors d and complementary divisors can be paired without fixed points.  
   `signature-0131` tags: F14, F32, F38, solved, involution, sums-of-squares, gen:sub-classical

132. **Heath-Brown's density of integers with two-square prime factors** [low/medium] — A density theorem uses quadratic-form factorization to force prime factors of a special type (F05w,F29,F31), matching ES's Gaussian-integer hard case and character-sum averages (F20). — *First step:* Check Heath-Brown's exact two-square-prime-factor result and test its Gaussian-integer decomposition on 4Cp+1.  
   `signature-0132` tags: F05w, F20, F29, F31, partial, Gaussian-integers, gen:sub-classical

133. **Waring's theorem and finite exceptional sums of cubes** [med/medium] — Waring gives a bounded number of additive witnesses for every sufficiently large integer and a finite explicit exception set (F01w,F12,F25,F32). — *First step:* Inspect the proof of the nine-cubes exceptions 23 and 239; test whether the descent step has any reciprocal analogue for 4/p.  
   `signature-0133` tags: F01w, F12, F25, F32, solved, additive-number-theory, gen:sub-classical

134. **Gauss Eureka theorem on triangular numbers** [high/medium] — Every positive integer is a sum of three triangular numbers, a three-witness universal representation theorem (F01,F12,F31), with a quadratic-form/theta-series mechanism (F19). — *First step:* Compare the triangular-number theta identity with ES's proposed theta quotient and identify whether a modular-form coefficient identity can enforce nonvanishing.  
   `signature-0134` tags: F01, F12, F19, F31, solved, theta-series, gen:sub-classical

135. **Chen Wang's proof of Borwein's coefficient-positivity conjecture** [low/medium] — A coefficient-nonvanishing/positivity problem in q-series is close to ES's theta-quotient coefficient criterion (F19), while requiring control at each index (F01,F21). — *First step:* Fetch Wang's paper; extract the coefficient recurrence/positivity mechanism and test the first recurrence terms of ES's generating function.  
   `signature-0135` tags: F01, F19, F21, solved, q-series, positivity, gen:sub-classical

136. **Schinzel–Sierpiński on primes among shifted linear forms** [low/medium] — The existence of primes in structured shifted forms is a pointwise prime-witness problem (F01,F21), and it interacts with the conjectural prime-plus-one/prime-divisor structure of ES (F10,F33). — *First step:* Verify the exact Schinzel–Sierpiński statement intended by (p+1)/(q+1), then test its local admissibility conditions on ES's linear forms 4Cp+1.  
   `signature-0136` tags: F01, F10, F21, F33, conditional, sieve, gen:sub-classical

137. **Hooley's GRH result for x²+y²+z³** [low/big] — A conditional pointwise representation by mixed-degree forms resembles ES's affine surface family and pointwise integral-witness problem (F01,F13,F21), with analytic prime-distribution input. — *First step:* Verify the exact Hooley theorem and hypotheses, then inspect its treatment of local factors and compare them with the ES surface's local densities.  
   `signature-0137` tags: F01, F13, F21, conditional, GRH, circle-method, gen:sub-classical

138. **Graham's unit-fraction theorem beyond 77** [high/medium] — A universal Egyptian-fraction statement for all sufficiently large inputs (F01w,F12) directly shares ES's unit-fraction format and bounded-term rigidity (F27). — *First step:* Retrieve Graham's proof of the 77 threshold; tabulate the residue-class identities and compare with ES's Mordell covering modulo 840.  
   `signature-0138` tags: F01w, F03, F12, F27, solved, Egyptian-fractions, gen:sub-classical

139. **Lenstra's small divisors in residue classes** [high/medium] — A divisor in a prescribed residue class and size interval (F10w) is exactly the sort of certificate sought in ES's divisor formulation; Lenstra's result offers a pointwise bounded-divisor tool (F21). — *First step:* Check Lenstra's theorem's modulus-versus-N exponent and enumerate its hypotheses for N=4Cp+1, modulus 4C, and target class −1.  
   `signature-0139` tags: F10, F10w, F21, solved, divisors, residue-classes, gen:sub-classical

140. **Coppersmith's algorithm for small roots** [med/medium] — The ES divisor certificate can be phrased as a constrained modular/arithmetic root search (F10,F32); lattice-based small-root methods are a computational analogue of the quadratic-form reformulations (F31). — *First step:* Express the ES fixed-C divisor condition as a polynomial congruence and test Coppersmith bounds on p up to a small bit size, comparing against direct divisor enumeration.  
   `signature-0140` tags: F10, F31, F32, solved, algorithm, lattice, gen:sub-classical

141. **Ford's divisors in short intervals** [high/medium] — Ford's distribution results for divisors in short intervals match the interval-restricted version of ES's divisor witness (F10w,F21), while ES additionally imposes a residue class (F10). — *First step:* Compute the ES-allowed divisor interval for fixed C and compare Ford's divisor interval estimates; then add the residue-class constraint by characters.  
   `signature-0141` tags: F10, F10w, F21, solved, divisors, short-intervals, gen:sub-classical

142. **Erdős–Hall and Hooley estimates for the divisor function** [high/medium] — The distribution of divisor counts has average and exceptional-set estimates (F04,F05,F21), closely parallel to ES's need to turn an average count into a pointwise positive count. — *First step:* Derive the first and second moments of R(p) over p≤X and compare their structure with the classical Δ(n) moment method.  
   `signature-0142` tags: F04, F05, F21, solved, partial, moments, divisor-function, gen:sub-classical

143. **Tatuzawa's effective Siegel lower bound** [med/big] — Tatuzawa's theorem makes a class-number lower bound effective apart from at most one exceptional discriminant (F01,F21,F36), paralleling conditional/ineffective pointwise existence arguments. — *First step:* Check Tatuzawa's explicit bound and identify the exceptional-discriminant dependency; test whether the ES real-character main term has a comparable lower bound.  
   `signature-0143` tags: F20, F21, F36, solved, effective-bounds, Siegel-ineffectivity, gen:sub-classical

144. **Harpaz's integral points on log K3 surfaces** [low/big] — The ES family is an affine surface with integral points, and the cited log-K3 work studies integral-point existence on related surface families (F01,F07,F13). — *First step:* Verify the precise Harpaz theorem and surface hypotheses; compute whether the ES affine cubic surface fits the same log-K3 class and boundary configuration.  
   `signature-0144` tags: F01, F07, F13, partial, arithmetic-geometry, integral-points, gen:sub-classical

145. **Colliot-Thélène–Wittenberg and Brauer–Manin for sums of three cubes** [med/big] — The sum-of-three-cubes problem is a cubic integral-point problem with Brauer–Manin phenomena (F07,F13,F33); ES is likewise an affine cubic surface whose BM obstruction is absent (F07,F13). — *First step:* Read the exact CT–Wittenberg result and calculate the Brauer group of the ES surface using the same fibration setup.  
   `signature-0145` tags: F07, F13, F33, partial, Brauer-Manin, cubic-surfaces, gen:sub-classical

146. **Ghosh–Sarnak Markoff Hasse failures** [med/big] — Markoff-type surfaces exhibit local solubility without integral/global representation, sharing ES's affine surface and Hasse-principle tension (F06,F07,F13). — *First step:* Verify the relevant Markoff theorem and compute the ES surface's integral Brauer group or orbit structure in the same framework.  
   `signature-0146` tags: F06, F07, F13, partial, Hasse-principle, cubic-surfaces, gen:sub-classical

147. **Loughran–Mitankin Markoff failures and thin exceptional sets** [low/big] — The arithmetic of Markoff surfaces includes systematic failures of integral Hasse principles and thin exceptional sets, akin to ES's integral surface family and sparse square-class failures (F07,F08w,F13). — *First step:* Check the exact Loughran–Mitankin theorem, then test whether failed ES primes cluster on finitely many thin polynomial orbits.  
   `signature-0147` tags: F07, F08w, F13, partial, thin-sets, arithmetic-geometry, gen:sub-classical

148. **Apollonian reciprocity obstructions** [low/big] — Apollonian packings have local congruence conditions and global reciprocity obstructions (F06,F07,F18,F31); ES has a prescribed-entry SL₂ matrix formulation plus congruence constraints (F18). — *First step:* Read Haag–Kertzer–Rickards–Stange's reciprocity criterion and test whether ES's prescribed-entry matrices admit a comparable spinor/reciprocity invariant.  
   `signature-0148` tags: F06, F07, F18, F31, partial, reciprocity, group-orbits, gen:sub-classical

149. **Finite congruence obstruction tests for universal forms** [high/medium] — Local representability is checked prime-by-prime, then a finite criterion can settle universality (F01,F03,F06); ES also has a finite congruence cover but no global witness criterion. — *First step:* For each ES residue class modulo 840, compute the local densities of the associated ternary form and test whether a finite criterion set can control all classes.  
   `signature-0149` tags: F01, F03, F06, F31, solved, local-global, gen:sub-classical

150. **Spinor-genus exceptions as feature-flip model** [high/medium] — Ternary forms often represent locally eligible integers except an exceptional square class: changing only the square-class condition changes universal coverage (F06,F08w). This isolates what the square obstruction buys, as a feature-flip analogue for ES. — *First step:* Partition ES's failed subfamily by square-free part and check whether the missing primes align with a fixed spinor-exception square class.  
   `signature-0150` tags: F06, F08w, feature-flip, solved, quadratic-forms, spinor-exceptions, gen:sub-classical

151. **Conditional Artin proof versus ES's missing pointwise lower bound** [high/big] — Hooley's conditional result combines a pointwise target with GRH-controlled character sums and a sieve (F20,F21,F22); ES shares the character-sum/sieve signature but lacks its proven lower bound (F36). — *First step:* Map every Hooley error term to an ES analogue in R(p)=Σ_C #{d|4Cp+1:d≡−1 mod 4C}; identify the single term preventing positivity.  
   `signature-0151` tags: F20, F21, F22, F36, solved, conditional, GRH, feature-flip, gen:sub-classical

152. **Least-nonresidue square failure as ES feature flip** [high/medium] — Least quadratic nonresidue existence is pointwise away from squares, while squares are exactly where the quadratic character degenerates (F01,F08w). This feature flip isolates a natural thin exceptional set rather than an analytic failure. — *First step:* Compute the real-character contribution to R(p) separately on p's square classes and test for an analogue of the principal-character degeneration.  
   `signature-0152` tags: F01, F08w, F20, feature-flip, solved, quadratic-characters, gen:sub-classical

153. **Almost-all to all via exceptional-set methods** [high/medium] — Classical almost-all representation results control an exceptional set rather than individual failures (F05,F21); ES has a strong almost-all theorem but still needs positivity for each prime. — *First step:* Compare the ES exceptional-set proof's final sieve step with the exceptional-set arguments for ternary quadratic-form representation; test a per-prime refinement.  
   `signature-0153` tags: F05, F21, partial, exceptional-set, quadratic-forms, gen:sub-classical

154. **Three-term versus four-term Egyptian fraction feature flip** [high/medium] — For unit fractions, changing the fixed term count from three to four makes existence much easier, while ES's three-term constraint is central (F12,F27); this is a feature-flip comparison rather than a proposed direct solution. — *First step:* Take the standard greedy four-term decomposition and classify the final denominator patterns that would permit merging two terms into one for numerator 4/p.  
   `signature-0154` tags: F12, F27, feature-flip, solved, Egyptian-fractions, gen:sub-classical

155. **Divisor residue-class computation as a cheap transfer test** [high/cheap] — Lenstra-style divisor-in-a-coset theorems match ES's exact witness equivalence (F10) and tied integer 4Cp+1; the relevant count is already explicit in the ★ formula. — *First step:* For small primes p, enumerate C and divisors d|4Cp+1 with d≡−1 mod 4C; tabulate d's size and compare against Lenstra's modulus>N^(1/3) regime.  
   `signature-0155` tags: F10, F10w, F21, solved, divisor-test, computation, gen:sub-classical

156. **Linnik dispersion applied to ES divisor counts** [high/big] — Dispersion is designed to derive pointwise existence from averaged arithmetic progressions (F05,F21,F22), and ES's ★ count is itself a sum of progression-restricted divisor counts (F10,F20). — *First step:* Form the bilinear sum over p and C from R(p), apply Cauchy-Schwarz/dispersion, and check whether off-diagonal terms are bounded by available divisor correlations.  
   `signature-0156` tags: F05, F10, F20, F21, F22, solved, dispersion, gen:sub-classical

157. **Character orthogonality and real-character main terms** [high/medium] — Quadratic-form representation counts split into genus characters and an analytic remainder (F20,F31); ES likewise has a real-character main term in its sum over moduli (F20). — *First step:* For each C in R(p), expand the residue indicator using characters modulo 4C and explicitly separate principal, real, and nonreal characters for p≡1 mod 4.  
   `signature-0157` tags: F20, F21, F29, F31, solved, characters, genus, gen:sub-classical

158. **Universal quadratic form escalation as an ES covering strategy** [med/medium] — The 290 proof escalates from local representation data to a universal form, while ES combines a finite congruence cover with parametrized certificate families (F03,F09,F34). — *First step:* Translate each ES certificate line into a representation vector and simulate escalation on residue classes modulo 840, tracking which new line covers each uncovered class.  
   `signature-0158` tags: F03, F09, F34, solved, quadratic-forms, escalation, gen:sub-classical

159. **Harpaz (adapting Swinnerton-Dyer) conic-fibration integral-point criterion** [high/medium] — The explicit sufficient conditions for integral points on conic-fibered log K3 surfaces in arXiv:1511.04876 match ES F01, F13, F15, F21: a universal integral-point question on a surface family with conic fibres and a pointwise existence issue. — *First step:* Read the theorem hypotheses and proof in arXiv:1511.04876; specialize the fibre calculation to the ES cubic's fixed-coordinate conic and check whether the hypotheses can be stated in terms of its coefficients.  
   `signature-0159` tags: F01, F13, F15, F21, src:arXiv, partial, conic-fibration, gen:sub-arxiv

160. **Integral conic-fibre descent as a certificate search** [high/medium] — The conic-fibration method of arXiv:1511.04876 connects ES F13/F15 (affine cubic and split-hyperbola slices) with F32 (small explicit witnesses) and F01. — *First step:* Check whether a fixed ES slice admits a conic parametrization with integral parameter conditions as explicit as those in the paper, then bound the resulting denominator sizes.  
   `signature-0160` tags: F01, F13, F15, F32, src:arXiv, partial, integral-points, gen:sub-arxiv

161. **Effective conic fibre points for bounded ES searches** [med/cheap] — The explicit conic-fibration conditions in arXiv:1511.04876 link ES F15's divisor-like hyperbola slices to F32's bounded certificates and F21's pointwise lower-bound need. — *First step:* Extract the paper's explicit integral-point construction and test it symbolically on the ES slice with one denominator fixed to its smallest admissible value.  
   `signature-0161` tags: F15, F21, F32, src:arXiv, partial, explicit, gen:sub-arxiv

162. **Markoff orbifold semi-integral Hasse principle** [high/medium] — The arXiv:2411.02629 study of local-global principles for semi-integral Markoff-type orbifold pairs matches ES F01/F06/F13 and F07: an integral-point existence problem on a surface with local-global and approximation questions. — *First step:* Read the theorem statements in arXiv:2411.02629 and compare their semi-integrality conditions with the denominators and positivity constraints in ES.  
   `signature-0162` tags: F01, F06, F07, F13, src:arXiv, solved, Markoff, gen:sub-arxiv

163. **Weak approximation versus actual ES witnesses** [high/medium] — arXiv:2411.02629 analyzes weak and strong approximation alongside semi-integral Hasse principles for Markoff orbifold pairs; this matches ES F06/F07 and F13, while highlighting the gap between local points and positive integral witnesses (F27). — *First step:* Identify the paper's examples where approximation holds or fails and translate the obstruction mechanism to the fixed-n ES surface, keeping positivity explicit.  
   `signature-0163` tags: F06, F07, F13, F27, src:arXiv, solved, approximation, gen:sub-arxiv

164. **Semi-integral variants as a diagnostic for ES** [med/medium] — The semi-integral Markoff-type framework in arXiv:2411.02629 shares ES F13/F06/F01 and offers a feature-flip comparison with F27: relax positivity/integrality and see which part of the local-global theorem survives. — *First step:* Formulate the ES surface's corresponding semi-integral-point question and check whether any theorem in arXiv:2411.02629 applies after a birational change.  
   `signature-0164` tags: F01, F06, F13, F27, src:arXiv, solved, feature-flip, gen:sub-arxiv

165. **Approximation off a finite set and ES residue families** [med/medium] — The strong-approximation results for Markoff orbifold pairs in arXiv:2411.02629 connect ES F06/F07/F13 with F03's congruence coverage: local approximation data may suggest congruence-class subfamilies, though not itself guarantee integral points. — *First step:* Extract its local-place conditions and test whether analogous conditions on ES denominator triples reproduce known Mordell classes modulo 840.  
   `signature-0165` tags: F03, F06, F07, F13, src:arXiv, solved, congruences, gen:sub-arxiv

166. **Markoff-type K3 integral Hasse counterexamples** [high/medium] — arXiv:2504.10992 constructs Markoff-type K3 surfaces with Zariski-dense rational points that fail the integral Hasse principle; this matches ES F07/F13/F27 and flips F06-style local solubility into failure of integral points. — *First step:* Read the counterexample construction and isolate the integral obstruction; test whether its mechanism has an analogue on an ES fixed-n fibre.  
   `signature-0166` tags: F07, F13, F27, src:arXiv, solved, feature-flip, Hasse-failure, gen:sub-arxiv

167. **Integral Hasse failure despite dense rational points** [high/cheap] — The Markoff-type K3 examples of arXiv:2504.10992 share ES F13/F07 and F21: global integral existence can fail despite abundance at the rational level, unlike the pointwise positive-integer target. — *First step:* Compare the authors' obstruction with the denominators in a rational parametrization of the ES cubic; determine where integrality is lost.  
   `signature-0167` tags: F07, F13, F21, src:arXiv, solved, integral-points, gen:sub-arxiv

168. **Zariski density is not an ES existence theorem** [high/medium] — arXiv:2504.10992 gives Markoff-type K3 surfaces with dense rational points but integral Hasse failure, matching ES F13 and contrasting F01/F07; it is a feature-flip from rational abundance to integral scarcity. — *First step:* Take one explicit surface from the paper and trace a dense rational orbit's denominators; compare with ES's reciprocal-variable divisibility requirement.  
   `signature-0168` tags: F01, F07, F13, src:arXiv, solved, feature-flip, gen:sub-arxiv

169. **Use Markoff K3 obstructions to audit local tests** [high/medium] — The Hasse-failing Markoff-type K3 family in arXiv:2504.10992 shares ES F06/F07/F13 and demonstrates why checking all local conditions need not supply a global integral point. — *First step:* Read the local-solubility verification in the paper and list which parts depend on the Markoff form, then test their analogues on ES modulo small prime powers.  
   `signature-0169` tags: F06, F07, F13, src:arXiv, solved, local-global, gen:sub-arxiv

170. **Spinor-genus representation obstruction with congruence conditions** [high/medium] — The ternary quadratic-form and lattice-coset spinor-genus classification in arXiv:2104.08798 matches ES F31/F29/F03 and F21: a representation problem with congruence-restricted integral vectors can have exceptional classes. — *First step:* Read the paper's classified spinor exceptions and test whether any ES quadratic-form reduction lands in a corresponding lattice coset.  
   `signature-0170` tags: F03, F21, F29, F31, src:arXiv, solved, quadratic-forms, gen:sub-arxiv

171. **Near-miss identities as an ES obstruction detector** [med/medium] — ArXiv:2104.08798 studies near-miss identities for ternary integral quadratic forms under congruence conditions, matching ES F03/F21/F31 and the exceptional-set theme F25. — *First step:* Extract one near-miss identity and see whether an ES quadratic-form reformulation admits an analogous identity with an explicit residual term.  
   `signature-0171` tags: F03, F21, F25, F31, src:arXiv, solved, near-miss, gen:sub-arxiv

172. **Congruence-sensitive quadratic forms and prime ES cases** [med/medium] — ArXiv:2104.08798 treats congruence conditions in ternary-form representation, matching ES F03/F29/F31 and the prime-specific target F01p. — *First step:* Attempt the encoding for p≡1 mod 4 and verify whether the congruence conditions define a fixed lattice coset amenable to spinor-genus tests.  
   `signature-0172` tags: F01p, F03, F29, F31, src:arXiv, partial, primes, gen:sub-arxiv

173. **Quadratic-form exception sets and ES square classes** [med/cheap] — Spinor-genus classification of ternary forms with congruence conditions in arXiv:2104.08798 shares ES F09/F25/F31: exceptional representation classes can be structured rather than random. — *First step:* Compare the exceptional square classes from the ES Mordell-Schinzel discussion against spinor-exception shapes in this paper's classification.  
   `signature-0173` tags: F09, F25, F31, src:arXiv, solved, exceptions, gen:sub-arxiv

174. **Divisors in residue classes via sign changes** [high/cheap] — Lenstra's divisor-in-residue-class algorithm, revisited in arXiv:2410.05030, matches ES F10/F15/F21: a tied integer's divisor in a prescribed residue class is the witness-shaped target. — *First step:* Read the algorithm and try its sign-change sequence on the ES tied integer 4Cp+1 with target divisor residue −1 mod 4C for the smallest C-family.  
   `signature-0174` tags: F10, F15, F21, src:arXiv, solved, divisors, gen:sub-arxiv

175. **Generalized Euclidean divisor search for ES certificates** [med/cheap] — Arxiv:2410.05030 generalizes Lenstra's divisor search to additional Euclidean rings, matching ES F10/F32 and F16's algebraic word encodings. — *First step:* Check the paper's sequence construction in the ordinary integer case and determine whether the ES tied integer can be fed in without requiring the algorithm's S³>N range.  
   `signature-0175` tags: F10, F16, F32, src:arXiv, solved, algorithm, gen:sub-arxiv

176. **Threshold limitations in divisor-class algorithms** [med/cheap] — The Lenstra algorithm and its generalization in arXiv:2410.05030 match ES F10/F21/F32, while the stated S³>N condition is a useful feature-flip: algorithmic tractability holds in a restricted size regime, not automatically for every ES parameter. — *First step:* Translate S and N in the paper's bound into ES parameters and test whether any known certificate family satisfies S³>N.  
   `signature-0176` tags: F10, F21, F32, src:arXiv, solved, feature-flip, algorithm, gen:sub-arxiv

177. **Divisor-class sign changes for fixed ES slices** [high/medium] — Arxiv:2410.05030 uses a sign change in a constructed sequence to locate a divisor in a residue class; ES F10 and F15 reduce to divisors on split-hyperbola fibres, with F21 requiring this for each individual p. — *First step:* Derive the paper's integer sequence for a fixed ES fibre and check whether its sign at the two ends is forced to differ by the ES congruences.  
   `signature-0177` tags: F10, F15, F21, src:arXiv, solved, sign-change, gen:sub-arxiv

178. **Euclidean-ring extensions and function-field ES** [med/medium] — The extension in arXiv:2410.05030 to polynomial rings and other Euclidean rings matches ES F26/F10/F16: it offers a neighboring setting where divisor-class searches may be more tractable. — *First step:* Specialize the algorithm to Z[T] and formulate the polynomial analogue of the ES divisor condition; check which steps use ordering/sign changes unavailable over finite fields.  
   `signature-0178` tags: F10, F16, F26, src:arXiv, partial, function-field, gen:sub-arxiv

179. **Quadratic-form representations through continuants** [high/medium] — Arxiv:1203.0347 extends H. J. S. Smith's continuant approach to proper binary quadratic-form representations and gives deterministic algorithms; this matches ES F16/F17/F31 and F32. — *First step:* Read the algorithmic theorem and test whether the ES length-three negative-continuant form can be converted into the paper's proper quadratic-form representation input.  
   `signature-0179` tags: F16, F17, F31, F32, src:arXiv, solved, continuants, gen:sub-arxiv

180. **Polynomial continuants and two-square representations** [med/medium] — Arxiv:1112.4535 extends continuant constructions for two-square representations to polynomial rings, matching ES F16/F26/F31 and the Gaussian feature F29. — *First step:* Inspect the polynomial two-square algorithm and attempt the analogous identity for ES over Fq[T], preserving the denominator congruence conditions.  
   `signature-0180` tags: F16, F26, F29, F31, src:arXiv, partial, function-field, gen:sub-arxiv

181. **Ordering continuants by local transformations** [med/medium] — The operation increasing continuants in arXiv:1608.08322 matches ES F16/F17/F32: bounded continued-fraction words encode integers, and local word changes control their size. — *First step:* Read the operation in the paper and test whether an analogous adjacent-letter move preserves n=tuv−u−v while changing the coordinate residue.  
   `signature-0181` tags: F16, F17, F32, src:arXiv, solved, continued-fractions, gen:sub-arxiv

182. **Continuant recurrences as bounded ES word identities** [med/cheap] — Arxiv:2501.06512 derives a continuant formulation for second-order recurrences and associated identities, matching ES F16/F17/F19 and F32's short certificate theme. — *First step:* Extract the recurrence identity and check whether the ES trilinear polynomial is a specialization of a continuant recurrence or determinant expansion.  
   `signature-0182` tags: F16, F17, F19, F32, src:arXiv, solved, recurrence, gen:sub-arxiv

183. **Periodic continuant formulas and ES residue periodicity** [med/cheap] — The explicit periodic-continuant formulas in arXiv:2001.06213 match ES F16/F17/F03, since periodic continued-fraction words can encode structured congruence families. — *First step:* Use the paper's periodic formula on a short periodic word and compare its resulting n-values modulo the ES covering modulus 840.  
   `signature-0183` tags: F03, F16, F17, src:arXiv, solved, continued-fractions, gen:sub-arxiv

184. **Continued-fraction convergence bounds for word certificates** [med/cheap] — The continuant estimates in arXiv:2106.03789 concern extremal sizes of structured continued fractions, matching ES F17/F32 and the small-witness feature F04's sparse-count setting. — *First step:* Read the extremal bound and apply it to length-three ES words with the required coordinate congruences; record the resulting denominator exponent.  
   `signature-0184` tags: F04, F17, F32, src:arXiv, partial, bounds, gen:sub-arxiv

185. **Continued-fraction matrices for ES congruence constraints** [med/cheap] — Continuants are matrix-entry polynomials, and the verified continuant treatment in arXiv:1203.0347 matches ES F17/F18/F16: a short word can be tested as an SL₂(Z) matrix with a prescribed entry. — *First step:* Write the length-three ES word as a product of 2×2 continued-fraction matrices and impose the ES coordinate congruences on its entries.  
   `signature-0185` tags: F16, F17, F18, src:arXiv, partial, matrices, gen:sub-arxiv

186. **Stern-sequence extremals and witness-count analogies** [med/medium] — Arxiv:1608.08322 proves results on largest values in Stern rows using alternating binary expansions and continuants; it matches ES F16/F17/F32 and offers a structured-word counting analogue for F04. — *First step:* Read its reduction of ordering to continuants and test whether the same normalization orders ES certificates for a fixed prime by denominator size.  
   `signature-0186` tags: F04, F16, F17, F32, src:arXiv, solved, word-counting, gen:sub-arxiv

187. **Shift two unit fractions while preserving exactness** [med/cheap] — The Egyptian-fraction rewriting operator in arXiv:2003.13229 and ES F12/F14/F27: exact reciprocal decompositions admit local transformations while positivity/parity constrain the result. — *First step:* Read the operator identity and apply it to a two-term portion of a known three-term ES identity; check whether it preserves three terms and positivity.  
   `signature-0187` tags: F12, F14, F27, src:arXiv, solved, Egyptian-fractions, gen:sub-arxiv

188. **Parity control in Egyptian-fraction rewrites** [high/cheap] — Arxiv:2003.13229 explicitly discusses parity in Egyptian fractions, matching ES F12/F27/F29 and the denominator parity constraints underlying ES. — *First step:* Extract its parity rules and check whether one rewrite preserves the 2-adic valuation pattern of the denominators in known ES triples (e.g. 4/7 = 1/2+1/21+1/42 has no denominator divisible by 4).  
   `signature-0188` tags: F12, F27, F29, src:arXiv, solved, parity, gen:sub-arxiv

189. **Denser Egyptian fractions as a bounded-term contrast** [high/cheap] — The all-rational Egyptian-fraction construction in arXiv:9811112 matches ES F12/F27/F32 in the broad unit-fraction setting, but flips fixed term count (F12): its term count grows with the denominator scale. — *First step:* Read the denominator-versus-term-count bound and identify the exact step that fails if the number of terms is fixed at three.  
   `signature-0189` tags: F12, F27, F32, src:arXiv, solved, feature-flip, Egyptian-fractions, gen:sub-arxiv

190. **Egyptian-fraction rewriting and S₃ normalization** [med/cheap] — The rewrite identity of arXiv:2003.13229 matches ES F12/F14/F27: local transformations can interact with the S₃ symmetry of the three denominator variables and the positivity boundary. — *First step:* Generate the rewrite orbit of a single small ES triple under its stated operator and denominator permutations; check for a canonical congruence representative.  
   `signature-0190` tags: F12, F14, F27, src:arXiv, partial, symmetry, gen:sub-arxiv

191. **Two-term failure versus three-term ES threshold** [med/medium] — The two-for-two rewriting operator of arXiv:2003.13229 acts on unit-fraction decompositions, matching ES F12/F14/F27; it can be used to probe the term-count transition (two terms fail, three conjecturally suffice). — *First step:* Use the paper's rewrite relation to characterize when two reciprocal terms can replace a pair in ES, then identify the invariant that prevents a universal two-term reduction.  
   `signature-0191` tags: F12, F14, F27, src:arXiv, partial, feature-flip, gen:sub-arxiv

192. **Matrix encoding of Markoff solution orbits** [med/medium] — Arxiv:0709.1499 encodes Markoff triples in integral upper-triangular matrices and connects them to the Markoff tree, matching ES F18/F38/F39 and surface-family feature F13. — *First step:* Read the matrix correspondence and see whether ES's fixed-entry SL₂(Z) formulation admits analogous generators preserving the ES equation.  
   `signature-0192` tags: F13, F18, F38, F39, src:arXiv, solved, matrices, gen:sub-arxiv

193. **Vieta jumping as a search-space reduction for ES** [med/cheap] — The Markoff equation and its tree in arXiv:1208.4032 share ES F13/F38/F32: involutions navigate integral solutions, and a decreasing-coordinate argument can yield small certificates. — *First step:* Write the fixed-x fibre as (ay−b)(az−b)=b² with a=4x−p, b=px. Compose the divisor swap with the coordinate permutations and check integrality and positivity. Then check whether some height decreases outside a finite base set, as in the Markoff tree.  
   `signature-0193` tags: F13, F32, F38, src:arXiv, partial, Vieta, gen:sub-arxiv

194. **Markoff-type equations and logarithmic solution growth** [med/medium] — The generalized Markov–Hurwitz equations studied in arXiv:2605.05075 share ES F01/F13/F38 and F04w: positive integral surface solutions are organized by nonlinear equation structure and have a reported logarithmic asymptotic phenomenon. — *First step:* Check the theorem's exact solution-counting variable and determine whether any ES parametrized subfamily has comparable tree growth.  
   `signature-0194` tags: F01, F04w, F13, F38, src:arXiv, solved, Markov-Hurwitz, gen:sub-arxiv

195. **Positive solution orbits versus positivity in ES** [med/medium] — The positive-integer Markov–Hurwitz solution study in arXiv:2605.05075 matches ES F01/F13/F27 and F38, where positivity is part of the arithmetic orbit structure. — *First step:* Inspect the orbit-generation recurrence and check whether an ES analogue preserves all denominator positivity constraints.  
   `signature-0195` tags: F01, F13, F27, F38, src:arXiv, solved, positivity, gen:sub-arxiv

196. **Integral orbit tree versus finite ES residue covers** [med/cheap] — The Markoff–Hurwitz positive-solution asymptotics in arXiv:2605.05075 match ES F13/F38/F34: an infinite orbit tree is a contrast to ES's need to cover every prime by families. — *First step:* Compute the mod-840 action of candidate ES coordinate involutions and compare the orbit's residue coverage with the known Mordell covering.  
   `signature-0196` tags: F13, F34, F38, src:arXiv, partial, orbits, gen:sub-arxiv

197. **Stern continuants and orbit-growth bounds** [med/medium] — The explicit transformation/order methods for continuants in arXiv:1608.08322 match ES F16/F17/F38 and the tree-like certificate organization F39. — *First step:* Build the graph of length-three ES word moves induced by continued-fraction identities and test whether the extremal operation from the paper bounds depth at fixed n.  
   `signature-0197` tags: F16, F17, F38, F39, src:arXiv, partial, orbits, gen:sub-arxiv

198. **Least nonresidue bounds as a reciprocity-search analogue** [med/medium] — The Fourier-optimization bounds for least quadratic nonresidues in arXiv:2404.08380 match ES F08/F29/F36 and F21: a pointwise quadratic-character condition is central, but conditional distribution bounds do not automatically solve a single-integer witness problem. — *First step:* Read the Fourier optimization setup and test whether its majorant/minorant can bound the number of ES parameters excluded by the relevant quadratic character.  
   `signature-0198` tags: F08, F21, F29, F36, src:arXiv, partial, characters, gen:sub-arxiv

199. **GRH conditional bounds as an ES benchmark, not a proof** [high/cheap] — The conditional least-nonresidue results in arXiv:1309.3595 match ES F08/F29/F36 and feature-flip F21: even strong character-distribution input gives bounds on a least witness, not necessarily a witness in every ES fibre. — *First step:* Read the explicit GRH dependence and identify the analogous character sum whose bound would force one ES denominator choice for each p.  
   `signature-0199` tags: F08, F21, F29, F36, src:arXiv, solved, feature-flip, gen:sub-arxiv

200. **Least prime in a progression and ES tied-divisor residues** [med/medium] — Arxiv:1309.3595 treats least primes in arithmetic progressions alongside least nonresidues, matching ES F10/F20/F29 and the residue-class existence question. — *First step:* Check whether any ES tied integer condition can be reformulated as a least-prime-in-progression condition without losing the same-parameter divisibility constraint.  
   `signature-0200` tags: F10, F20, F29, src:arXiv, partial, progressions, gen:sub-arxiv

201. **Smooth-number equidistribution and ES divisor classes** [med/medium] — Soundararajan's theorem (arXiv:0707.0299) shows that y-smooth integers below x are equidistributed in reduced residue classes mod q for q < y^{4√e−ε}. This matches ES F10/F20/F21, while ES needs a pointwise tied divisor. — *First step:* Read the modulus range in the theorem and test whether an ES family's tied integer can be forced smooth at a compatible modulus.  
   `signature-0201` tags: F10, F20, F21, src:arXiv, solved, feature-flip, smooth-numbers, gen:sub-arxiv

202. **Character-sum distribution versus ES pointwise count** [high/medium] — The least-nonresidue Fourier methods of arXiv:2404.08380 share ES F20/F21/F29: both involve character sums, but ES requires a lower bound for one integer rather than an average over characters or moduli. — *First step:* Write the ES representation count in its character-sum form and compare each sum's length and conductor with the optimization bounds in the paper.  
   `signature-0202` tags: F20, F21, F29, src:arXiv, partial, character-sums, gen:sub-arxiv

203. **A matrix-orbit test for ES certificate connectivity** [med/cheap] — Markoff matrix/tree encodings in arXiv:0709.1499 match ES F18/F38/F39 and F32: the central question can be reframed as whether short transformations connect all required certificate states. — *First step:* Define vertices as ES word certificates modulo a small modulus and test whether candidate matrix generators connect every admissible residue state.  
   `signature-0203` tags: F18, F32, F38, F39, src:arXiv, partial, connectivity, gen:sub-arxiv

204. **Classical continuant algorithms for Gaussian ES structure** [high/cheap] — Arxiv:1203.0347 gives deterministic algorithms for proper binary quadratic-form representations, matching ES F29/F31/F32 and the continuant encoding F17. — *First step:* Take p≡1 mod 4, compute its two-square representation using the paper's algorithm, and inspect whether the output naturally supplies ES denominator congruences.  
   `signature-0204` tags: F17, F29, F31, F32, src:arXiv, solved, Gaussian, gen:sub-arxiv

205. **Ternary lattice-coset representation versus ES three denominators** [med/medium] — Arxiv:2104.08798 treats ternary integral quadratic forms with congruence conditions, matching ES F12/F27/F31 and F03: three variables, positivity/integrality constraints, and congruence-restricted representations. — *First step:* Attempt to eliminate one ES denominator using a fixed slice and identify whether the remaining condition is a ternary quadratic form on a fixed coset.  
   `signature-0205` tags: F03, F12, F27, F31, src:arXiv, partial, quadratic-forms, gen:sub-arxiv

206. **Bounded continued-fraction words and thin ES families** [med/medium] — The extremal continuant results in arXiv:2106.03789 match ES F17/F30/F32: restricted words generate thin infinite families with controlled growth, analogous to known ES families that do not yet cover all primes. — *First step:* Apply the paper's extremal bounds to an ES word family such as periodic partial quotients and estimate the number of primes it could cover up to X.  
   `signature-0206` tags: F17, F30, F32, src:arXiv, partial, thin-families, gen:sub-arxiv

207. **Bloom positive-density unit-fraction theorem (298): density extraction** [high/medium] — Erdős problem 298 ↔ ES features F01, F12, F21, F33: universal-in-input representation existence, bounded unit-fraction sums, pointwise versus density, additive reciprocal structure. — *First step:* Read the proof linked on https://www.erdosproblems.com/298 and isolate the density-to-finite-relation lemma; test it on primes/candidate denominator sets in a finite interval.  
   `signature-0207` tags: F01, F12, F21, F33, src:erdosproblems, solved, density, unit-fractions, gen:sub-erdosproblems

208. **Problem 298: positive upper density variant** [med/medium] — Problem 298 ↔ ES F01, F05, F12, F33: existence for every input versus positive-density existence and bounded reciprocal sums. — *First step:* Check whether the proof’s density hypothesis can be instantiated with the set of ES parameters admitting a specified denominator pattern; identify the exact density-loss step.  
   `signature-0208` tags: F01, F05, F12, F33, src:erdosproblems, solved, density, gen:sub-erdosproblems

209. **Problem 299: finite-sum obstruction and contrapositive** [med/cheap] — Problem 299 ↔ ES F01, F12, F27, F33: finite sums of reciprocals, positivity, and universal representation behavior. — *First step:* Write out the exact 299 statement and Bloom’s 298 implication; test whether ES failures could define a sequence meeting the forbidden finite-sum condition.  
   `signature-0209` tags: F01, F12, F27, F33, src:erdosproblems, solved, contrapositive, gen:sub-erdosproblems

210. **Problem 300: Croot and Liu–Sawhney density bounds** [high/medium] — Problem 300 ↔ ES F04, F05, F12, F21, F33: count of reciprocal-sum representations, density bounds, and pointwise-versus-average tension. — *First step:* Read Croot [Cr03] and Liu–Sawhney [LiSa24] as linked from the page; extract the counting inequality and ask whether its variables can be restricted to three denominators summing to 4/p.  
   `signature-0210` tags: F04, F05, F12, F21, F33, src:erdosproblems, solved, density, counting, gen:sub-erdosproblems

211. **Problem 300: sparse-set reciprocal-sum count** [med/medium] — Problem 300 ↔ ES F04, F12, F21, F24: representation counts, fixed reciprocal-sum length, pointwise estimates, and heuristic abundance. — *First step:* Compare the paper’s count with the number R(p) of ES triples for primes p; identify whether the proof counts by denominator scale or by residue class.  
   `signature-0211` tags: F04, F12, F21, F24, src:erdosproblems, solved, representation-count, gen:sub-erdosproblems

212. **Problem 301: extremal distinct unit fractions** [med/cheap] — Problem 301 ↔ ES F04, F12, F14, F27: reciprocal equations with distinct variables, symmetric witnesses, and positivity. — *First step:* Inspect the elementary argument summarized at https://www.erdosproblems.com/301 and test its disjoint blocks against denominator triples satisfying 4/p.  
   `signature-0212` tags: F04, F12, F14, F27, src:erdosproblems, partial, extremal, unit-fractions, gen:sub-erdosproblems

213. **Problem 302: density forces a reciprocal relation** [med/medium] — Problem 302 ↔ ES F01, F05, F12, F33: density-to-existence, finite reciprocal sums and additive structure. — *First step:* Read the cited elementary argument and determine whether its density threshold can be applied to residues of candidate ES denominators modulo p.  
   `signature-0213` tags: F01, F05, F12, F33, src:erdosproblems, partial, density, gen:sub-erdosproblems

214. **Problem 303: Brown–Rödl coloring theorem** [med/medium] — Problem 303 ↔ ES F01, F12, F14, F33: monochromatic reciprocal equations, universal finite coloring, and symmetric additive structure. — *First step:* Read Brown–Rödl [BrRo91] from the page and check whether the proof produces quantitative bounds on the smallest monochromatic solution that could include ES-shaped equations.  
   `signature-0214` tags: F01, F12, F14, F33, src:erdosproblems, solved, Ramsey, coloring, gen:sub-erdosproblems

215. **Problem 304: minimal length Egyptian fractions** [med/medium] — Problem 304 ↔ ES F04, F12, F21, F32: bounded-length reciprocal representations, representation complexity and explicit certificates. — *First step:* Read Bloom–van Doorn’s linked exposition and compare its denominator-growth lemmas with the special target 4/p and length three.  
   `signature-0215` tags: F04, F12, F21, F32, src:erdosproblems, solved, Egyptian-fractions, gen:sub-erdosproblems

216. **Problem 305: prime-target Egyptian fraction bounds** [high/medium] — Problem 305 ↔ ES F04, F12, F21, F29: prime-specific reciprocal representations and a pointwise existence/count problem. — *First step:* Read Yokota [Yo88] and Liu–Sawhney [LiSa24] from the page; check whether their constructions treat prime b specially, and test the construction at targets 4/p.  
   `signature-0216` tags: F04, F12, F21, F29, src:erdosproblems, solved, primes, gen:sub-erdosproblems

217. **Problem 306: multiplicative prime-factor Egyptian decompositions** [low/big] — Problem 306 ↔ ES F01, F12, F14, F33: universal decomposition format, fixed reciprocal sums and symmetric terms. — *First step:* Read Butler–Erdős–Graham [BEG15] linked from the page and isolate the construction; test whether its prime-factor allocation can impose 4/p as the sum.  
   `signature-0217` tags: F01, F12, F14, F33, src:erdosproblems, solved, factorization, gen:sub-erdosproblems

218. **Problem 307: coprime reciprocal sums** [low/cheap] — Problem 307 ↔ ES F12, F14, F27, F33: reciprocal-sum identities, permutation symmetry, positivity and coprimality. — *First step:* Read the statement and examples on the problem page; try imposing pairwise coprime denominators on a few ES solutions and compare the resulting algebra.  
   `signature-0218` tags: F12, F14, F27, F33, src:erdosproblems, open, coprimality, gen:sub-erdosproblems

219. **Problem 308: Croot’s threshold for unit-fraction subset sums** [med/medium] — Problem 308 ↔ ES F01, F04, F12, F21: existence threshold, reciprocal subset sums and pointwise representation. — *First step:* Read Croot [Cr99] on the page and test whether its threshold argument can start from one ES denominator and complete with two terms.  
   `signature-0219` tags: F01, F04, F12, F21, src:erdosproblems, solved, subset-sums, gen:sub-erdosproblems

220. **Problem 309: many integers represented by reciprocal subsets** [med/medium] — Problem 309 ↔ ES F04, F05, F12, F21: counts of represented values, abundance and pointwise gaps. — *First step:* Read the lower-bound argument and test its distribution statement on the target values 4/p rather than all integers in a range.  
   `signature-0220` tags: F04, F05, F12, F21, src:erdosproblems, partial, coverage, gen:sub-erdosproblems

221. **Problem 310: Liu–Sawhney bounded reciprocal-sum refinement** [high/medium] — Problem 310 ↔ ES F01, F04, F12, F21: existence of a reciprocal subsum with controlled parameters and pointwise bounds. — *First step:* Read [LiSa24] via the page and write its parameter dependence explicitly; check whether the ES denominator triple can be embedded in the allowed sequence.  
   `signature-0221` tags: F01, F04, F12, F21, src:erdosproblems, solved, quantitative, gen:sub-erdosproblems

222. **Problem 311: Tang’s least nonzero reciprocal subset sum** [med/medium] — Problem 311 ↔ ES F04, F12, F21, F32: a least positive reciprocal sum, controlled denominators and explicit certificates. — *First step:* Read Tang’s linked note; identify the exact least-sum construction and test whether it can force a remainder of the form 4/p−1/x.  
   `signature-0222` tags: F04, F12, F21, F32, src:erdosproblems, partial, small-denominator, gen:sub-erdosproblems

223. **Problem 312: reciprocal sums from large multisets** [low/medium] — Problem 312 ↔ ES F01, F04, F12, F33: large input forces a reciprocal subsum, bounded-complexity additive structure. — *First step:* Determine the exact theorem statement from the page and inspect its proof/reference; check whether a large set of candidate denominators supplies the required reciprocal subsum.  
   `signature-0223` tags: F01, F04, F12, F33, src:erdosproblems, partial, multiset, gen:sub-erdosproblems

224. **Problem 313: primary pseudoperfect reciprocal identity** [low/cheap] — Problem 313 ↔ ES F12, F14, F27, F33: exact reciprocal identity over prime denominators, symmetric sum and positivity. — *First step:* Use the defining equation on the page to derive the associated product congruences; compare them with the denominator divisibility conditions in ES parametrizations.  
   `signature-0224` tags: F12, F14, F27, F33, src:erdosproblems, open, prime-reciprocals, gen:sub-erdosproblems

225. **Problem 314: Lim–Steinerberger reciprocal-sum exponent** [med/medium] — Problem 314 ↔ ES F04, F12, F21, F24: extremal reciprocal sum, representation scale and heuristic exponent. — *First step:* Read Lim–Steinerberger [LiSt24] linked on the page and compare the exponent derivation with denominator size requirements for 4/p.  
   `signature-0225` tags: F04, F12, F21, F24, src:erdosproblems, solved, exponents, gen:sub-erdosproblems

226. **Problem 315: Sylvester-sequence stability and Vardi constant** [low/medium] — Problem 315 ↔ ES F01, F12, F27, F32: reciprocal expansions, positivity and constructive denominator growth. — *First step:* Read Kamio [Ka25] or Li–Tang [LiTa25] from the page; test their stability lemma on the rational target 4/p after one or two greedy terms.  
   `signature-0226` tags: F01, F12, F27, F32, src:erdosproblems, solved, greedy, gen:sub-erdosproblems

227. **Problem 316: divisor-set partition counterexample** [low/cheap] — Problem 316 ↔ ES F03, F10, F12, F33: divisor structure, partition obstructions and reciprocal sums. — *First step:* Study Sándor’s proper-divisor counterexample and check whether analogous divisor partitions constrain divisors of 4Cp+1 in ES.  
   `signature-0227` tags: F03, F10, F12, F33, src:erdosproblems, solved, divisors, gen:sub-erdosproblems

228. **Problem 317: reciprocal-sum noncancellation** [low/cheap] — Problem 317 ↔ ES F04, F12, F21, F27 (flip): small nonzero signed sums Σδ_k/k with δ_k∈{−1,0,1}, contrasted with ES's positive three-term sums. — *First step:* Read the problem’s current comments/proof sketch and test the claimed bound on the residual 4/p−1/x−1/y for small candidate x,y.  
   `signature-0228` tags: F04, F12, F21, F27, src:erdosproblems, open, lower-bounds, gen:sub-erdosproblems

229. **Problem 318: arithmetic progression reciprocal sums** [med/medium] — Problem 318 ↔ ES F01, F05, F12, F33: finite reciprocal subsums in structured sets and density-sensitive existence. — *First step:* Read Larsen’s linked proof for squares and identify the step handling sparse sets; test analogous sets of candidate ES denominators in fixed residue classes.  
   `signature-0229` tags: F01, F05, F12, F33, src:erdosproblems, solved, arithmetic-progression, squares, gen:sub-erdosproblems

230. **Problem 319: Croot reciprocal discrepancy construction** [low/medium] — Problem 319 ↔ ES F04, F05, F12, F21: controlled reciprocal sums, density and discrepancy. — *First step:* Read Croot [Cr01] from the page and compute the discrepancy of its constructed set in residue classes relevant to p modulo 8.  
   `signature-0230` tags: F04, F05, F12, F21, src:erdosproblems, solved, discrepancy, gen:sub-erdosproblems

231. **Problem 320: iterative unit-fraction sum counting** [med/medium] — Problem 320 ↔ ES F04, F05, F12, F21: representation counts, almost-all distribution and pointwise exception problem. — *First step:* Read the linked proof exposition and translate its smooth/rough split to the ES count R(p), checking whether a recurrence survives the fixed target 4/p.  
   `signature-0231` tags: F04, F05, F12, F21, src:erdosproblems, partial, smooth-numbers, recurrence, gen:sub-erdosproblems

232. **Problem 321: distinctness range for reciprocal sums** [med/medium] — Problem 321 ↔ ES F04, F12, F14, F21: multiplicity of reciprocal sums, symmetry and distinct-term constraints. — *First step:* Compare its bounds with the count of ordered versus unordered ES triples; identify whether a collision argument improves a lower bound for R(p).  
   `signature-0232` tags: F04, F12, F14, F21, src:erdosproblems, partial, collisions, gen:sub-erdosproblems

233. **Problem 327: unit-fraction characterization of odd sets** [med/cheap] — Problem 327 ↔ ES F03, F12, F27, F33: reciprocal-equation equivalence, parity and additive structure. — *First step:* Read the van Doorn argument linked through problem 301 and determine whether its forced pair construction can generate an ES triple for each prime residue class.  
   `signature-0233` tags: F03, F12, F27, F33, src:erdosproblems, partial, parity, gen:sub-erdosproblems

234. **Problem 825: divisor-sum representation of weird numbers** [med/medium] — Problem 825 ↔ ES F01, F10, F12, F33: representation by divisors, universal threshold behavior and additive arithmetic structure. — *First step:* Read Larsen’s linked proof and isolate the divisor-selection lemma; test whether the same selection principle works for a divisor of 4Cp+1 in the required class.  
   `signature-0234` tags: F01, F10, F12, F33, src:erdosproblems, solved, divisors, gen:sub-erdosproblems

235. **Problem 825: prime-factor threshold as feature flip** [med/medium] — Problem 825 ↔ ES features F01, F10, F12, with the flip being an imposed prime-factor restriction absent in ES. — *First step:* Read the theorem’s exact restriction in Larsen’s paper; enumerate which factorization conditions are compatible with 4Cp+1 and an ES divisor certificate.  
   `signature-0235` tags: F01, F10, F12, feature-flip, src:erdosproblems, solved, divisor-sum, gen:sub-erdosproblems

236. **Problem 298: positivity-sensitive cancellation test** [med/medium] — Problem 298 ↔ ES F12, F27, F33; feature flip: arbitrary signed sums can cancel, while positive reciprocal terms cannot. — *First step:* Mark every use of positivity in Bloom’s proof and test whether an analogous monotonicity can be retained after fixing the ES sum at 4/p.  
   `signature-0236` tags: F12, F27, F33, feature-flip, src:erdosproblems, solved, positivity, gen:sub-erdosproblems

237. **Problem 300: Croot density method versus pointwise ES** [high/medium] — Problem 300 ↔ ES F04, F05, F12, with feature flip F21: density/average control versus a bound at each prime. — *First step:* Compare the density theorem’s exceptional set with primes p individually; inspect whether the proof has a uniform lower bound after conditioning on p mod 8.  
   `signature-0237` tags: F04, F05, F12, F21, feature-flip, src:erdosproblems, solved, pointwise-gap, gen:sub-erdosproblems

238. **Problem 304: shortest expansion versus ES fixed length** [med/medium] — Problem 304 ↔ ES F04, F12, F32; feature flip F12: variable minimum length versus exactly three terms. — *First step:* Read the proof exposition and compare its greedy length estimate against the exact algebraic constraints after fixing two ES denominators.  
   `signature-0238` tags: F04, F12, F32, feature-flip, src:erdosproblems, solved, Egyptian-fractions, gen:sub-erdosproblems

239. **Problem 305: prime target versus all-integer target** [med/medium] — Problem 305 ↔ ES F01, F12, F29; feature flip F29: prime targets, with p≡1 mod 4 the difficult ES split. — *First step:* Check whether the Bleicher–Erdős lower-bound argument for primes or the Yokota/Liu–Sawhney upper bounds distinguish p mod 4; if so, try adapting the hardest residue case to 4/p.  
   `signature-0239` tags: F01, F12, F29, feature-flip, src:erdosproblems, solved, primes, gen:sub-erdosproblems

240. **Problem 308: threshold versus individual target** [med/medium] — Problem 308 ↔ ES F01, F04, F12; feature flip F01: eventual threshold statement rather than all n. — *First step:* Read [Cr99] and identify how the least missed integer is bounded; test whether the argument yields a threshold for residual targets after one ES term.  
   `signature-0240` tags: F01, F04, F12, feature-flip, src:erdosproblems, solved, threshold, gen:sub-erdosproblems

241. **Problem 310: sharp dependence versus ES denominator bound** [med/medium] — Problem 310 ↔ ES F04, F12, F21, F32: sharp quantitative dependence, fixed-length expansion and certificate size. — *First step:* Extract the sharp dependence stated on the page; compare it to known computational ES denominator sizes as p grows.  
   `signature-0241` tags: F04, F12, F21, F32, src:erdosproblems, solved, quantitative, gen:sub-erdosproblems

242. **Problem 311: least positive value and ES near-miss** [low/medium] — Problem 311 ↔ ES F10, F12, F21, F32: least nonzero reciprocal combination, divisor algebra and certificate bounds. — *First step:* After choosing x in ES, compare the size of the nonzero residual 4/p−1/x−1/y (trivially ≥ 1/(pxy)) with Tang's near-miss scale; derive the induced interval for the divisor parameter in the two-term completion.  
   `signature-0242` tags: F10, F12, F21, F32, src:erdosproblems, partial, near-miss, gen:sub-erdosproblems

243. **Problem 318: squares as sparse exceptional family** [med/medium] — Problem 318 ↔ ES F01, F08, F12, F30: structured sparse inputs, algebraic exceptional families, reciprocal sums. — *First step:* Read Larsen’s proof and identify the square-specific decomposition; test if the ES failure locus for a fixed certificate family has a similarly tractable parameterization.  
   `signature-0243` tags: F01, F08, F12, F30, src:erdosproblems, solved, sparse-family, gen:sub-erdosproblems

244. **Problem 318: arithmetic progressions and congruence covering** [med/medium] — Problem 318 ↔ ES F03, F06, F12, F34: progression structure, local congruences and union of families. — *First step:* Read the progression proof linked through the page; test if its finite-sum selection can be arranged separately on the square classes modulo 840.  
   `signature-0244` tags: F03, F06, F12, F34, src:erdosproblems, solved, congruences, gen:sub-erdosproblems

245. **Problem 321: collision count versus ES witness multiplicity** [med/cheap] — Problem 321 ↔ ES F04, F14, F21, F38: representation collisions, symmetry and pointwise multiplicity. — *First step:* Derive the number of ordered triples from the unordered R(p) count and test whether distinctness bounds from 321 control repeated partial sums.  
   `signature-0245` tags: F04, F14, F21, F38, src:erdosproblems, partial, collisions, gen:sub-erdosproblems

246. **Problem 303: finite coloring as certificate-family selection** [low/medium] — Problem 303 ↔ ES F01, F12, F14, F34: universal coloring theorem, symmetric reciprocal solutions and covering by families. — *First step:* Check the Brown–Rödl proof for explicit color dependence and test coloring candidate denominator triples by their residue class mod 8.  
   `signature-0246` tags: F01, F12, F14, F34, src:erdosproblems, solved, coloring, covering, gen:sub-erdosproblems

247. **Problem 302: density-zero exceptional set analogue** [low/medium] — Problem 302 ↔ ES F03, F05, F21, F22: density control, exceptional inputs and thin-set existence. — *First step:* Extract the explicit density estimate from the page’s proof and compare it with the known ES exceptional-set form; check whether the same counting variable exists.  
   `signature-0247` tags: F03, F05, F21, F22, src:erdosproblems, partial, exceptional-set, gen:sub-erdosproblems

248. **Problem 298: positive density versus all-prime coverage** [high/medium] — Problem 298 ↔ ES F01, F05, F12, with feature flip F01: density existence does not imply universal existence. — *First step:* Locate the density hypothesis in Bloom’s proof and ask what additional uniform lower bound on the ES candidate set would upgrade it to each prime p.  
   `signature-0248` tags: F01, F05, F12, feature-flip, src:erdosproblems, solved, density, gen:sub-erdosproblems

249. **Problem 300: Croot construction as a thin-set stress test** [med/medium] — Problem 300 ↔ ES F04, F05, F12, F24: sparse representation counts, density bounds and heuristic abundance. — *First step:* Use the construction cited on the page to build a restricted denominator set and calculate whether its induced ES candidate count is atypically small.  
   `signature-0249` tags: F04, F05, F12, F24, src:erdosproblems, solved, thin-set, gen:sub-erdosproblems

250. **Problem 304: Vose bound and denominator-size stress test** [med/medium] — Problem 304 ↔ ES F04, F12, F32: bounded-length representation, denominator growth and certificate size. — *First step:* Read Vose [Vo85] and identify how denominators grow in his construction; compare with the polynomial-in-p size of any three-term ES certificate.  
   `signature-0250` tags: F04, F12, F32, src:erdosproblems, solved, denominator-bounds, gen:sub-erdosproblems

251. **Problem 309: coverage of many target values** [med/medium] — Problem 309 ↔ ES F04, F05, F12, F34: many represented values, almost-all coverage and families of representations. — *First step:* Read Croot’s all-small-integers coverage argument and check whether the construction works uniformly on the sparse target sequence 4/p.  
   `signature-0251` tags: F04, F05, F12, F34, src:erdosproblems, partial, coverage, gen:sub-erdosproblems

252. **Problem 310: sharp dependence as finite-search bound** [med/medium] — Problem 310 ↔ ES F04, F12, F21, F23: bounded representation count, pointwise search and computational verification. — *First step:* Translate the Liu–Sawhney parameter bound into an explicit maximum denominator and compare with existing verified ES computation ranges.  
   `signature-0252` tags: F04, F12, F21, F23, src:erdosproblems, solved, computation, gen:sub-erdosproblems

253. **Problem 313: prime reciprocal equation and local congruences** [low/cheap] — Problem 313 ↔ ES F03, F06, F12, F29: prime denominators, local conditions and fixed reciprocal identity. — *First step:* Reduce the 313 identity modulo each prime and modulo 8, then compare the resulting local constraints with the ES p-adic checks.  
   `signature-0253` tags: F03, F06, F12, F29, src:erdosproblems, open, local, gen:sub-erdosproblems

254. **Problem 314: extremal reciprocal bounds and Poisson scale** [low/medium] — Problem 314 ↔ ES F04, F12, F24, F37: representation-scale heuristic, reciprocal extremals and count fluctuations. — *First step:* Inspect the examples attaining the lower bound and compare their reciprocal-sum multiplicities with the predicted log-scale distribution of R(p).  
   `signature-0254` tags: F04, F12, F24, F37, src:erdosproblems, solved, heuristics, gen:sub-erdosproblems

255. **Problem 315: greedy expansion as a certificate algorithm** [low/cheap] — Problem 315 ↔ ES F12, F17, F32: reciprocal expansion, bounded construction steps and certificate length. — *First step:* Implement only a hand-sized greedy expansion for 4/p and compare the first terms and residual with the argument in Kamio or Li–Tang.  
   `signature-0255` tags: F12, F17, F32, src:erdosproblems, solved, algorithm, gen:sub-erdosproblems

256. **Problem 316: explicit minimal obstruction and feature flip** [low/cheap] — Problem 316 ↔ ES F03, F10, F12; feature flip: a finite divisor-set obstruction versus ES’s universal prime family. — *First step:* Check the cited minimal set and compute which congruence classes its divisors occupy; compare with the ES divisor-class criterion.  
   `signature-0256` tags: F03, F10, F12, feature-flip, src:erdosproblems, solved, counterexample, gen:sub-erdosproblems

257. **Problem 320: recurrence method versus pointwise lower bound** [high/medium] — Problem 320 ↔ ES F04, F05, F21, F40; feature flip F21: averaged recursive count versus each individual prime. — *First step:* Trace the induction in the proof exposition and mark the line where summing over targets is essential; test a conditioned version at a single prime p.  
   `signature-0257` tags: F04, F05, F21, F40, feature-flip, src:erdosproblems, partial, recurrence, gen:sub-erdosproblems

258. **Problem 300: almost-all reciprocal representation and ES exceptions** [med/medium] — Problem 300 ↔ ES F05, F12, F21, F25: abundance theorem versus explicit exceptional cases and pointwise demand. — *First step:* Read the explicit examples listed on the unit-fraction tag page and compare their mechanism with the known ES near-miss primes for restricted certificates.  
   `signature-0258` tags: F05, F12, F21, F25, src:erdosproblems, solved, exceptions, gen:sub-erdosproblems

259. **Problem 301: disjoint blocks and divisor-fiber decomposition** [med/cheap] — Problem 301 ↔ ES F10, F12, F15, F33: disjoint reciprocal blocks, fixed-variable divisor fibers and additive-multiplicative structure. — *First step:* Fix x in 4/p=1/x+1/y+1/z and rewrite the y,z equation as a divisor product; compare its fibers to the disjoint sets in the 301 argument.  
   `signature-0259` tags: F10, F12, F15, F33, src:erdosproblems, partial, divisor-fibers, gen:sub-erdosproblems

260. **Problem 307: prime reciprocal partition and finite covering** [low/cheap] — Problem 307 ↔ ES F03, F12, F14, F29: prime reciprocal sums, symmetric partition and congruence classes. — *First step:* Check Cambie's coprime examples on the page modulo 4 and 8; formulate a finite congruence-covering search for an ES denominator triple.  
   `signature-0260` tags: F03, F12, F14, F29, src:erdosproblems, open, covering, gen:sub-erdosproblems

261. **Problem 312: multiset extraction and candidate denominator supply** [low/medium] — Problem 312 ↔ ES F01, F04, F12, F34: large supply forces a reciprocal sum, multiple candidate families cover targets. — *First step:* Read the exact threshold and test a candidate multiset formed from denominators in a chosen arithmetic progression; determine whether the resulting sum can equal a residual 4/p.  
   `signature-0261` tags: F01, F04, F12, F34, src:erdosproblems, partial, extraction, gen:sub-erdosproblems

262. **Problem 314: infinite extremizers and thin ES families** [low/medium] — Problem 314 ↔ ES F12, F24, F30, F32: reciprocal constructions, heuristic extremality, thin infinite families and certificates. — *First step:* Take the explicit infinite family in the proof and substitute its parameter into the ES certificate identity, checking whether a prime subfamily emerges.  
   `signature-0262` tags: F12, F24, F30, F32, src:erdosproblems, solved, thin-families, gen:sub-erdosproblems

263. **Problem 319: reciprocal-set construction and residue-class balance** [low/medium] — Problem 319 ↔ ES F03, F05, F12, F20: reciprocal sets, density, congruence balance and character-like averaging. — *First step:* Compute residue-class reciprocal sums for the constructed set modulo 4 and 8 and compare with the real-character main terms in ES counts.  
   `signature-0263` tags: F03, F05, F12, F20, src:erdosproblems, solved, residue-classes, gen:sub-erdosproblems

264. **Problem 355: lacunary reciprocal sequence covers an interval** [low/medium] — Problem 355 ↔ ES F01, F12, F27, F32: reciprocal expansions, positivity and constructive coverage. — *First step:* Read [DoKo25] linked on the page and inspect the interval-covering construction; ask whether 4/p lies in the covered interval with a three-term restriction.  
   `signature-0264` tags: F01, F12, F27, F32, src:erdosproblems, solved, interval-coverage, gen:sub-erdosproblems

265. **Problem 355: lacunarity versus bounded ES length** [med/medium] — Problem 355 ↔ ES F12, F17, F32, with feature flip F17: unrestricted sequence length versus fixed bounded length three. — *First step:* Determine the number of terms used for each rational in the proof and check whether the first three already cover any infinite prime subfamily 4/p.  
   `signature-0265` tags: F12, F17, F32, feature-flip, src:erdosproblems, solved, lacunary, gen:sub-erdosproblems

266. **Problem 300: reciprocal sum-set method and bounded length** [med/medium] — Problem 300 ↔ ES F04, F12, F33: rich reciprocal sumsets and fixed-length additive-multiplicative structure. — *First step:* Inspect the proof for sumset iteration; stop at the first stage producing three distinct reciprocals and test the resulting target set against primes 4/p.  
   `signature-0266` tags: F04, F12, F33, src:erdosproblems, solved, sumsets, gen:sub-erdosproblems

267. **Problem 304: greedy residual and split-hyperbola completion** [med/cheap] — Problem 304 ↔ ES F12, F15, F32: reciprocal expansion and fixed-denominator divisor fiber. — *First step:* Choose x=floor(p/4)+1 in 4/p, derive the residual two-term equation, and compare its divisor parameter with bounds used in 304.  
   `signature-0267` tags: F12, F15, F32, src:erdosproblems, solved, greedy, divisors, gen:sub-erdosproblems

268. **Problem 308: subset-sum threshold as a two-term completion probe** [low/medium] — Problem 308 ↔ ES F01, F12, F15, F32: universal tail coverage, reciprocal sums and fixed-variable hyperbola completion. — *First step:* Fix a candidate x and test whether the reciprocal subset-sum interval guaranteed by the theorem contains the residual 4/p−1/x using only two terms.  
   `signature-0268` tags: F01, F12, F15, F32, src:erdosproblems, solved, completion, gen:sub-erdosproblems

269. **Problem 302: density threshold as a quantitative toy model** [med/cheap] — Problem 302 ↔ ES F01, F05, F12, F24: forced reciprocal solution above density threshold versus ES heuristic existence. — *First step:* Work through the simplest density estimate on the page and compare its combinatorial lower bound with a numerical estimate of ES candidate triples at primes.  
   `signature-0269` tags: F01, F05, F12, F24, src:erdosproblems, partial, density-threshold, gen:sub-erdosproblems

270. **Square-factor saturation for the trilinear form xy+yz+zx** [high/medium] — OEIS A025052 studies positive integers omitted by xy+yz+zx; the page records Borwein–Choi's theorem that every N with a square factor is represented except 4 and 18. This shares F01/F08w/F13/F16w: a universal representation problem, algebraic exceptional strata, and a cubic/trilinear polynomial encoding. — *First step:* Translate the A025052 square-factor parametrization to ES: fix n=m r² and test whether the induced denominators can be made positive integers; enumerate small m,r and record exactly where integrality fails.  
   `signature-0270` tags: F01, F08w, F13, F16w, src:OEIS, solved, trilinear, square-factors, gen:sub-oeis-mo-guy

271. **Squarefree obstruction list for xy+yz+zx** [high/cheap] — OEIS A055745 is the squarefree subset of integers not represented by xy+yz+zx, sharing F25/F08w/F13 and F04: a concrete finite-looking exceptional set arises within an algebraic family and representation counts are computable. — *First step:* Compute ES failure counts separately for squarefree n and n with square factors over a modest prime range, and compare the apparent exceptional pattern with A055745's finite-list phenomenon.  
   `signature-0271` tags: F08w, F13, F24, F25, src:OEIS, partial, squarefree, gen:sub-oeis-mo-guy

272. **Uniquely represented trilinear integers as a model for witness multiplicity** [med/medium] — OEIS A093669/A093670, cross-referenced by A025052, classify numbers with a unique representation by ab+ac+bc. They share F04/F13/F14: count integral points on a symmetric cubic-form fibre, including unusually sparse one-witness fibres. — *First step:* For primes p, compare the number of ordered ES solutions up to permutation with the analogous factorization count on a small trilinear surface; look for a divisor-sum identity or a stable multiplicity statistic.  
   `signature-0272` tags: F04, F13, F14, src:OEIS, partial, multiplicity, gen:sub-oeis-mo-guy

273. **Idoneal numbers and sparse failures of a cubic representation** [med/medium] — A025052 cross-references A000926 (Euler idoneal numbers) as integers not of the strict form ab+ac+bc with 0<a<b<c. This shares F08w/F13/F25/F31: a thin algebraically structured exceptional set tied to quadratic forms. — *First step:* Read the A000926 cross-reference and test whether the ES divisor-witness count on primes is better organized by discriminant/class data in Q(i) than by raw residue classes.  
   `signature-0273` tags: F08w, F13, F25, F31, src:OEIS, partial, quadratic-forms, gen:sub-oeis-mo-guy

274. **Goldbach's other conjecture and explicit finite exceptions** [high/cheap] — OEIS A060003 records odd composites not expressible as a prime plus twice a square, with 5777 and 5993 identified as the known exceptions. It shares F01/F03/F25/F32: a universal arithmetic representation, finite explicit failures, and compact certificates checked by divisor/prime search. — *First step:* Build an ES analogue of A060003: for each prime p in increasing order, record the least denominator triple and the minimal search certificate; inspect whether witness-free candidates have a recognizable arithmetic signature.  
   `signature-0274` tags: F01, F03, F25, F32, src:OEIS, solved, finite-exceptions, computation, gen:sub-oeis-mo-guy

275. **Goldbach failure certificates versus ES certificate search** [med/cheap] — The Goldbach-other problem turns a missing representation into a finite list of excluded prime-plus-square candidates. This matches F10/F21/F32/F25: divisor- or candidate-indexed witnesses, pointwise detection, short certificates, and explicit exceptions. — *First step:* For each ES prime p, enumerate a single parameterized family of denominators and store a compact proof that all candidates in that family fail when none succeeds; compare against the full divisor criterion.  
   `signature-0275` tags: F10, F21, F25, F32, src:OEIS, solved, certificate, gen:sub-oeis-mo-guy

276. **Schinzel's fixed-numerator three-unit-fraction generalization** [high/cheap] — The MathOverflow question explicitly compares ES with Schinzel's conjecture that k/n is a sum of three unit fractions for fixed k and sufficiently large n. This shares F01w/F11/F12/F25: a numerator threshold, fixed-length Egyptian fractions, and a largest-exception function. — *First step:* Use the MO question's suggested n(k) viewpoint: compute largest failures for k=4,5,… over small ranges and test whether the same divisor-in-one-class parametrization extends uniformly in k.  
   `signature-0276` tags: F01, F11, F12, F25, src:MathOverflow, open, numerator-threshold, gen:sub-oeis-mo-guy

277. **Exceptional-set density question for Egyptian-fraction equations** [high/medium] — The MathOverflow question asks whether the set of n failing ES (4/n) is known, under standard conjectures, to have a power-saving bound such as ≤ n^{0.99}. This matches F05/F21/F22/F36: almost-all versus pointwise existence, thin exceptional sets, and limits of equidistribution heuristics. — *First step:* Read the cited Elsholtz–Tao counting paper from the MO comment and identify which averaging step prevents its bound from implying a pointwise ES witness; test that precise step on prime moduli.  
   `signature-0277` tags: F05, F21, F22, F36, src:MathOverflow, partial, exceptional-set, gen:sub-oeis-mo-guy

278. **The largest exceptional denominator as a function of numerator** [med/cheap] — For Schinzel's k/n variant, the MO question asks for the largest failure n(k), and notes a lower-growth bound. This shares F11/F12/F24/F25: numerator threshold, fixed number of unit fractions, heuristic finite exceptions, and explicit small failures. — *First step:* For several small k, exhaustively find all n up to a modest cutoff with no three-term decomposition and plot the maximum against k; compare with the k^(8/7) growth suggested in the MO question and with Pomerance–Weingartner's proven lower bound n_k ≥ exp(k^{1/3+o(1)}) (arXiv:2511.16817).  
   `signature-0278` tags: F11, F12, F24, F25, src:MathOverflow, open, computation, gen:sub-oeis-mo-guy

279. **Egyptian fraction term-count threshold as a feature flip** [med/cheap] — MO 212865 asks whether a/n (a > 4) is a sum of k < a unit fractions, e.g. 5/n with four terms; comments note this is open in general (citing Elsholtz, Trans. AMS 353 (2001)) while k ≥ a terms is easy by greedy. Matches F11/F12 and flips the term-count threshold relative to the numerator. — *First step:* Read MO 212865 and the Elsholtz (2001) paper it cites; compare the easy k ≥ a regime with the k < a regime for a/n and isolate the algebraic step that fails when one term is removed.  
   `signature-0279` tags: F11, F12, feature-flip, src:MathOverflow, partial, Egyptian-fractions, gen:sub-oeis-mo-guy

280. **More-than-three unit fractions and numerator-dependent exceptions** [med/cheap] — The MO question asks about k/n as a sum of a fixed number of unit fractions when k>4. This shares F01w/F11/F12/F25 and flips the exact numerator 4: fixed-term existence may become easier or harder with k. — *First step:* On primes p in a small interval, compare the number of three-term representations of k/p for k=3,4,5 and tag each missing k against p's residue classes.  
   `signature-0280` tags: F01, F11, F12, F25, feature-flip, src:MathOverflow, open, gen:sub-oeis-mo-guy

281. **Four-term ES decompositions as a triviality control** [high/cheap] — The MathOverflow question on ES with four terms supplies a direct neighboring problem where term count changes, matching F12/F11/F32 and flipping the conjectural three-term bound to four terms. — *First step:* Implement a canonical greedy four-term decomposition for 4/p, then compare its denominator scale and residues with the shortest three-term witnesses for the same primes.  
   `signature-0281` tags: F11, F12, F32, feature-flip, src:MathOverflow, solved, unit-fractions, gen:sub-oeis-mo-guy

282. **Prime-minus-one characterization of a bilinear-form complement** [med/medium] — OEIS A005097 identifies the complement of values represented by 2xy+x+y as n with 2n+1 prime. This shares F01/F02/F10/F16w: an exact prime-indexed criterion, a simple polynomial representation, and a complementary exceptional set. — *First step:* Rewrite the ES divisor certificate conditions as an equivalent primality or factorization test if possible; first search for an affine transform analogous to 2n+1 in the simple bilinear identity.  
   `signature-0282` tags: F01, F02, F10, F16w, src:OEIS, solved, bilinear, gen:sub-oeis-mo-guy

283. **Bilinear polynomial representation via completing the product** [high/cheap] — For A005097 the missing values are exactly those for which 2n+1 is prime, while represented values satisfy 2n+1=(2x+1)(2y+1) under the natural factorization. This shares F10/F15/F16w: a polynomial identity becomes a divisor-pair search on each fibre. — *First step:* Derive the analogous factorization on an ES fixed-variable slice and compare its residue constraints to the odd-factor pair factorization behind 2xy+x+y.  
   `signature-0283` tags: F10, F15, F16w, src:OEIS, solved, factorization, gen:sub-oeis-mo-guy

284. **Combinatorial Nullstellensatz proof on prime-sized cyclic seats** [med/medium] — A005097's comments cite Kohen–Sadofschi: a prescribed-distance seating problem on 2n+1 seats is solvable for every distance list iff 2n+1 is prime, proved using the Combinatorial Nullstellensatz. It shares F01/F03/F29/F31: universal finite-field conditions, prime residue structure, and an algebraic certificate. — *First step:* Read Kohen's Nullstellensatz argument and test whether the polynomial coefficient-extraction method yields a nonzero count for ES witnesses modulo p, especially in the difficult p≡1 mod 4 class.  
   `signature-0284` tags: F01, F03, F29, F31, feature-flip, src:OEIS, solved, finite-fields, gen:sub-oeis-mo-guy

285. **A prime criterion hidden in a missing-value sequence** [med/cheap] — A005097 is simultaneously a prime transform and a complement of a polynomial value set. It shares F10/F16w/F24/F25: one can enumerate witnesses by factor pairs and the nonrepresented values have an exact, computable criterion. — *First step:* Select a natural ES subfamily (e.g. one denominator divisible by p), calculate its omitted primes, and check whether omission is equivalent to primality of a low-degree transform.  
   `signature-0285` tags: F10, F16w, F24, F25, src:OEIS, solved, complement, gen:sub-oeis-mo-guy

286. **Goldbach-other exceptions beyond the two famous composites** [high/cheap] — A060003 records the full candidate list beginning 1,3,17,137,… and identifies 5777 and 5993 as its only known exceptions above the Stern-prime terms. It matches F01/F21/F25/F32: pointwise representation search, a rare exceptional set, and explicit negative certificates. — *First step:* For each claimed ES witness-free candidate, publish a terminating exact check over the full parameter range and separate proven failure from conjectural no-further-failures in the report.  
   `signature-0286` tags: F01, F21, F25, F32, src:OEIS, partial, exceptional-set, gen:sub-oeis-mo-guy

287. **Residue restriction on exceptional additive representations** [high/cheap] — A060003 notes that its terms greater than 3 all lie in 6n−1. This shares F03/F25/F29: congruence restrictions sharply constrain the exceptional set, while leaving a sparse residue class to investigate. — *First step:* Compute ES witness counts by residue class modulo 840 and by prime splitting in Q(i), then check whether any analogous single congruence class carries almost all low-count primes.  
   `signature-0287` tags: F03, F25, F29, src:OEIS, solved, congruences, gen:sub-oeis-mo-guy

288. **Stern primes and a second notion of additive nonrepresentation** [med/cheap] — The A060003 comments identify several small exceptions as odd Stern primes, i.e. primes not of the form p+2b². This combines prime inputs with a restricted additive representation and finite exceptional values, matching F01p/F10/F25/F29. — *First step:* Run the same candidate-generation code on ES primes and composites separately, comparing first-witness distributions and residue classes with the Stern-prime subset in A060003.  
   `signature-0288` tags: F01, F10, F25, F29, src:OEIS, partial, primes, gen:sub-oeis-mo-guy

289. **Large gaps between detected representations and exceptional candidates** [high/cheap] — A060003 reports progressively improved lower bounds for the next possible omitted value, with no claim that the sequence is complete. This matches F23/F24/F25/F32: computation, heuristic finiteness, explicit exceptions, and verifiable search bounds. — *First step:* For ES, record the largest tested prime and the exact complete divisor-search bound alongside every ‘no counterexample’ statement; do not report a cutoff without the bound proof.  
   `signature-0289` tags: F23, F24, F25, F32, src:OEIS, partial, computation, gen:sub-oeis-mo-guy

290. **Square-factor theorem as a route from a thin stratum to near-universality** [high/medium] — A025052's Borwein–Choi result covers all N with a square factor except 4,18, leaving squarefree inputs as the difficult stratum. It shares F01/F05/F08w/F25 and is a feature-flip: broad coverage is proved off the squarefree locus. — *First step:* Partition ES primes and general n by square factors in the tied divisor quantities (4Cp+1 or p+4d), and test whether the certificate family handles all but a squarefree residual condition.  
   `signature-0290` tags: F01, F05, F08w, F25, feature-flip, src:OEIS, solved, squarefree, gen:sub-oeis-mo-guy

291. **Explicit parametrization rather than mere existence for a cubic form** [med/medium] — A025052 gives explicit formulas for x,y,z after writing N=mn² and splitting according to n relative to m+1 and a residue k mod m+1. It matches F13/F15/F16w/F32: an integral surface is solved by casework and short parameters. — *First step:* Adapt the three A025052 case splits as a design pattern for ES: choose an integer parameter, reduce to its residue modulo a linear function, and check whether the remainder becomes an integral positive third denominator.  
   `signature-0291` tags: F13, F15, F16w, F32, src:OEIS, solved, parametrization, gen:sub-oeis-mo-guy

292. **Exceptional small values in a square-factor covering theorem** [high/cheap] — The square-factor theorem for xy+yz+zx has the explicit exceptions 4 and 18. This shares F08w/F25/F27: a universal positivity-constrained representation has algebraic-family exceptions, and positivity matters to the theorem. — *First step:* In ES parameter identities, list every boundary case where a denominator is zero, negative, or repeated; compare whether the remaining failures are similarly confined to low parameter values.  
   `signature-0292` tags: F08w, F25, F27, src:OEIS, solved, positivity, gen:sub-oeis-mo-guy

293. **Quadratic-form reinterpretation of a trilinear omission set** [med/medium] — A025052 links its omission set to integers lacking an indecomposable positive definite binary quadratic form of the corresponding discriminant (as reported in the entry). This shares F13/F25/F31: a representation problem on a cubic form is reframed through quadratic forms and a sparse obstruction list. — *First step:* Trace the Zhu–Shao/Peters reference from A025052 and check whether any discriminant/class-number invariant can be attached to ES's divisor witnesses in Q(i).  
   `signature-0293` tags: F13, F25, F31, src:OEIS, partial, quadratic-forms, gen:sub-oeis-mo-guy

294. **Squarefree tail bounds as a model for proving an omission list finite** [med/medium] — A055745 lists the squarefree integers not represented by xy+yz+zx (a finite-looking list; an OEIS comment says at most 17 terms); Le's note on positive solutions is cited in the companion entry A025052. It matches F05/F08w/F25/F40: isolate a sparse algebraic locus, study its exceptional tail, and distinguish an observed finite list from a theorem. — *First step:* Read Le's cited paper and extract any mechanism bounding squarefree nonrepresentables; test its divisor estimates on the squarefree parameters left after ES's 840-class identities.  
   `signature-0294` tags: F05, F08w, F25, F40, src:OEIS, partial, squarefree, gen:sub-oeis-mo-guy

295. **Counting distinct unit-fraction solutions, not just proving existence** [high/cheap] — MathOverflow 229514 asks for the number of strictly increasing tuples with reciprocal sum 1 and reports the unique 3-term solution 1/2+1/3+1/6. This shares F04/F12/F14/F21: an exact representation-count problem with symmetry removed and pointwise counts rather than existence alone. — *First step:* Adopt the increasing-denominator convention from the MO question and recompute small-prime ES representation counts, comparing them to ordered counts after dividing by S3 orbit sizes.  
   `signature-0295` tags: F04, F12, F14, F21, src:MathOverflow, partial, counting, gen:sub-oeis-mo-guy

296. **Odd-denominator restriction creates exact term-count obstructions** [med/cheap] — The accepted answer on MO 229514 reports the distinct odd-denominator equation sum 1/x_i=1 has no solutions for even term count, and five solutions at the first odd case n=9. This shares F11/F12/F25/F27: a term-count threshold and positivity/integrality constraints create sharp exceptions. — *First step:* For ES, classify triples by denominator parity pattern and test whether excluding one pattern leaves an exceptional family analogous to the even-term impossibility.  
   `signature-0296` tags: F11, F12, F25, F27, src:MathOverflow, solved, parity, gen:sub-oeis-mo-guy

297. **Landau-style bounds on the number of reciprocal representations** [med/medium] — The MO answer to 229514 cites Landau's bound for solutions to sum 1/x_i=1 with unrestricted positive integer denominators. This shares F04/F12/F21/F32: bounded-length unit fractions, representation multiplicity, and an explicit counting bound. — *First step:* Follow the Landau reference identified in the MO answer and see whether its argument, applied to 4/p after scaling, yields any nontrivial upper bound on R(p).  
   `signature-0297` tags: F04, F12, F21, F32, src:MathOverflow, solved, counting-bound, gen:sub-oeis-mo-guy

298. **Odd unit-fraction solution counts and polynomial lower bounds** [med/medium] — The same MO answer cites a result giving a lower bound on the number of odd-denominator solutions for larger odd term counts, while exact counts remain unknown. This matches F04w/F12/F21/F22: a lower-bound count for constrained reciprocal representations but a gap to exact pointwise behavior. — *First step:* Read Chen–Elsholtz–Jiang, cited in the answer (arXiv:1108.6118), and extract its solution-generating operation; test whether it produces multiplicative families of ES triples.  
   `signature-0298` tags: F04w, F12, F21, F22, src:MathOverflow, partial, lower-bound, gen:sub-oeis-mo-guy

299. **Group class equations naturally generate reciprocal sums** [low/medium] — MO 229514 notes that a finite group with n conjugacy classes gives a reciprocal sum equal to 1 using centralizer orders. This shares F01/F12/F14/F33: a structured family of unit-fraction representations arises from a symmetry object and its orbit stabilizers. — *First step:* Check whether any finite-group class equation can be normalized to 4/p with three distinct centralizer orders; start with small groups and inspect the resulting divisibility constraints.  
   `signature-0299` tags: F01, F12, F14, F33, src:MathOverflow, partial, group-theory, gen:sub-oeis-mo-guy

300. **Denominator-sum generating sequence for reciprocal representations** [med/medium] — The MO answer points to OEIS A051907, counting representations of 1 as unit fractions with a fixed denominator sum. This shares F04/F12/F19/F21: a coefficient/counting viewpoint turns reciprocal solutions into sequence coefficients indexed by a complexity statistic. — *First step:* Inspect A051907's definition and recurrence, then formulate the corresponding generating series for ordered ES triples by denominator sum or maximum denominator and compare low coefficients.  
   `signature-0300` tags: F04, F12, F19, F21, src:MathOverflow, partial, generating-functions, gen:sub-oeis-mo-guy

301. **Strictly ordered cubic-form representations and symmetry reduction** [high/cheap] — OEIS A093669 counts unique representations by ab+ac+bc under 0<a<b<c, removing permutation symmetry. It shares F04/F13/F14: a symmetric three-variable surface whose raw point count is converted to canonical unordered witnesses. — *First step:* For primes p, count only x≤y≤z ES triples and compare with the fully ordered count, separately tracking repeated-coordinate strata.  
   `signature-0301` tags: F04, F13, F14, src:OEIS, partial, symmetry, gen:sub-oeis-mo-guy

302. **Unique-representation locus as a low-multiplicity test** [med/cheap] — A093669 lists integers with exactly one strictly ordered representation as ab+ac+bc, sharing F04/F13/F25 and contrasting ES's expected polylogarithmic abundance with a rigid one-point fibre. — *First step:* Enumerate ES primes with exactly one unordered solution orbit up to a modest cutoff and compare their factorization and residue signatures to the one-representation trilinear terms.  
   `signature-0302` tags: F04, F13, F25, src:OEIS, partial, unique-representation, gen:sub-oeis-mo-guy

303. **Boundary-inclusive representation count changes the exceptional set** [high/cheap] — A093670 counts unique ab+ac+bc representations with 1≤a≤b≤c, unlike A093669's strict inequalities. It shares F13/F14/F25 and flips the boundary convention, showing that allowing coincident coordinates changes which values have a unique witness. — *First step:* Split ES solutions into all-distinct, exactly-two-equal, and all-equal denominator triples and verify whether any attempted reduction discards a necessary boundary stratum.  
   `signature-0303` tags: F13, F14, F25, feature-flip, src:OEIS, partial, boundary-cases, gen:sub-oeis-mo-guy

304. **Factor-pair enumeration for a unique cubic-form witness** [high/cheap] — A093669 provides a computation for unique ab+ac+bc representations by looping over a,b and testing whether n−ab is divisible by a+b, yielding c. This matches F10/F15/F32: each fibre is reduced to a divisor/congruence test and can be exhaustively certified. — *First step:* Implement the A093669 loop pattern for ES after fixing one denominator, using the exact split-hyperbola divisor condition; compare outputs against independent brute force for small p.  
   `signature-0304` tags: F10, F15, F32, src:OEIS, solved, algorithm, gen:sub-oeis-mo-guy

305. **Zaremba: bounded partial quotients as a coverage engine** [high/medium] — Zaremba’s denominator problem shares F01, F17, F18, F23: every denominator is sought via a bounded-length continued-fraction/SL₂ word, with extensive computational exploration. ES has bounded CF length in ES₅ and prescribed matrix entries (F17,F18). — *First step:* Read Bourgain–Kontorovich’s 2014 paper and test whether its semigroup/matrix-counting setup adapts to the ES₅ five-slice parametrization for p≡1 mod 4.  
   `signature-0305` tags: F01, F17, F18, F23, src:Zaremba, open, continued-fractions, SL2, gen:sub-other-fields

306. **Zaremba: thin semigroup growth versus universal coverage** [med/medium] — Zaremba shares F01, F17, F22, F30: universal denominator coverage is conjectured, while restricted-CF semigroups first yield large/thin sets. ES similarly has thin proved prime families but no all-prime rung (F30). — *First step:* Extract the precise denominator-count lower bound in the cited paper and ask whether a corresponding count of ES primes covered by bounded parameter boxes is accessible.  
   `signature-0306` tags: F01, F17, F22, F30, src:Zaremba, open, feature-flip, gen:sub-other-fields

307. **Zaremba feature flip: bounded partial quotients** [med/cheap] — Zaremba matches ES’s universal-existence goal, matrix/continued-fraction structure, and computational checks (F01,F18,F23), but demands bounded partial quotients (F17w) rather than ES’s bounded CF length. This feature-flip isolates a stronger regularity condition. — *First step:* Compare the matrix products in Zaremba’s proof with ES₅ matrices and record exactly where a uniform digit bound enters.  
   `signature-0307` tags: F01, F17w, F18, F23, src:Zaremba, open, feature-flip, gen:sub-other-fields

308. **Collatz: Tao’s almost-all theorem and exceptional sets** [high/medium] — Collatz shares F01w, F05, F23, F24: a universal orbit claim has a strong almost-all theorem and enormous computational checking, while heuristic expectations remain. ES also has an almost-all theorem but needs pointwise coverage (F05,F21). — *First step:* Read Tao’s 2019 paper’s main theorem and exceptional-set definition; compare its quantifiers with ES’s exceptional-set estimate and identify any usable smoothing lemma.  
   `signature-0308` tags: F01w, F05, F23, F24, src:Collatz, partial, almost-all, gen:sub-other-fields

309. **Collatz parity vectors as finite-word certificates** [med/cheap] — The Collatz problem shares F16w, F22, F32, F23: finite parity words encode trajectories and permit certificate-style computation for a universal integer claim. ES has fixed polynomial/word forms and short certificates (F16,F32). — *First step:* Write a tiny enumerator for ES n=tuv−u−v certificates by bounded word/parameter height and compare its pruning by congruences with Collatz parity-vector pruning.  
   `signature-0309` tags: F16w, F22, F32, F23, src:Collatz, partial, word-encoding, gen:sub-other-fields

310. **Collatz feature flip: almost-all control is not pointwise control** [high/cheap] — Tao’s Collatz result shares ES’s universal target, computational verification, and a structured arithmetic map (F01,F23,F16w), but proves an almost-all weakened conclusion rather than all inputs (F05). — *First step:* Check Tao’s theorem’s exact exceptional notion and test whether ES exceptional primes can be grouped by a corresponding large-deviation statistic.  
   `signature-0310` tags: F01, F05, F16w, F23, src:Collatz, partial, feature-flip, gen:sub-other-fields

311. **Lonely runner: finite-dimensional torus avoidance** [med/medium] — Lonely runner shares F01, F06, F23, F24: a universal integer-speed assertion has no simple local obstruction, strong finite verification, and geometric/torus heuristics. ES similarly combines local solubility with a global integral point question (F06,F07). — *First step:* Read Perarnau’s survey and identify a solved small-runner argument using a finite covering of the torus; translate the covering step into ES residue classes.  
   `signature-0311` tags: F01, F06, F23, F24, src:lonely-runner, open, torus, gen:sub-other-fields

312. **Lonely runner: cyclic gap and symmetry reduction** [med/cheap] — The lonely-runner problem shares F14,F23,F24,F01 through interchangeable runner labels, finite verified cases, and a universal conjecture. ES witness permutation symmetry is S₃ (F14), likewise reducing redundant cases. — *First step:* Inspect the survey’s symmetry reductions and implement canonical representatives for ES triples (x,y,z) and the corresponding residue constraints.  
   `signature-0312` tags: F01, F14, F23, F24, src:lonely-runner, open, symmetry, gen:sub-other-fields

313. **Lonely runner feature flip: geometric witness intervals** [med/cheap] — Lonely runner matches ES’s universal quantifier, symmetry, and computational study (F01,F14,F23), but its witness is a real time in a compact torus, unlike ES’s positive-integer point (F27). — *First step:* Compare a torus-compactness proof for a low-dimensional runner case with an ES congruence-cover proof and list the precise integrality-dependent steps.  
   `signature-0313` tags: F01, F14, F23, F27, src:lonely-runner, open, feature-flip, gen:sub-other-fields

314. **Erdős–Faber–Lovász: absorption for a universal finite coloring bound** [med/medium] — EFL shares F01, F05w, F23: a universal finite-structure assertion proved (Kang–Kelly–Kühn–Methuku–Osthus, arXiv:2101.04698) for all sufficiently large n; small n are not covered by that proof. Its absorption proof is a candidate pattern for ES's infinite family of thin certificate lines (F34). — *First step:* Read the proof’s absorption section and formulate an explicit ES analogue: a reservoir of certificate lines that absorbs a bounded set of uncovered prime residue patterns.  
   `signature-0314` tags: F01, F05w, F23, F34, src:EFL, solved-large-n, absorption, gen:sub-other-fields

315. **EFL: approximate coloring plus absorbing reservoir** [med/medium] — EFL’s proof shares F01,F03,F05w: universal coverage is achieved by a global bound, finite local compatibility, and an absorption step. ES’s finite congruence covering and exceptional square classes have the same cover-then-patch outline (F03,F08). — *First step:* Extract the EFL approximate-decomposition/absorption interface and test a toy version on ES residue classes modulo 840 with square classes left uncovered.  
   `signature-0315` tags: F01, F03, F05w, F08, src:EFL, solved-large-n, absorption, gen:sub-other-fields

316. **EFL feature flip: hypergraph structure versus arithmetic family** [med/medium] — EFL shares ES’s universal quantifier, finite local constraints, and proof-by-cover-plus-repair (F01,F03,F34), but its objects have a finite hypergraph decomposition while ES ranges over primes with multiplicative arithmetic (F33). — *First step:* Check whether ES certificate lines admit a bounded-overlap notion analogous to edge-disjoint color classes, then assess if an absorber can be defined.  
   `signature-0316` tags: F01, F03, F34, F33, src:EFL, solved-large-n, feature-flip, gen:sub-other-fields

317. **Apollonian curvatures: local-global density one versus every integer** [high/medium] — The Apollonian curvature problem shares F03,F05,F10,F23: congruence-allowed values, density-one local-global results, and arithmetic orbit structure. Its known density-one scope contrasts with ES’s pointwise target (F21). — *First step:* Read Bourgain–Kontorovich's density-one theorem (arXiv:1205.4416) and isolate its sieve/expansion step; then read the 2024 Annals counterexample paper and ask whether ES's p-tied divisor parametrization can supply an analogous orbit.  
   `signature-0317` tags: F03, F05, F10, F23, src:Apollonian, partial, local-global, gen:sub-other-fields

318. **Apollonian local-global feature flip: exceptional algebraic families** [high/cheap] — Apollonian curvature results share ES’s local congruence restrictions, thin witnesses, and almost-all progress (F03,F05,F22), but explicit algebraic families can be missed, unlike a universal existential target. This is a feature-flip warning about exceptional subfamilies. — *First step:* Read the counterexample-family discussion in the 2024 paper and compare its quadratic/quartic obstructions with ES’s square-class obstruction.  
   `signature-0318` tags: F03, F05, F08w, F22, src:Apollonian, partial, feature-flip, gen:sub-other-fields

319. **Scholz–Brauer: inductive addition-chain constructions** [med/medium] — The Scholz conjecture shares F01,F16w,F23,F30: a universal bound is sought, short arithmetic words are certificates, and constructive families establish infinite subcases. ES also has short polynomial certificates and thin proven families. — *First step:* Read the construction for the proved infinite family in the 2023 paper and search for ES maps n↦an+b preserving a unit-fraction certificate.  
   `signature-0319` tags: F01, F16w, F23, F30, src:addition-chains, partial, induction, gen:sub-other-fields

320. **Addition chains: certificate search with rigorous lower bounds** [med/cheap] — Addition chains match ES through F01,F32,F23,F24: finite verifiable certificates, computer searches, and a global existence/bound problem. The Scholz–Brauer problem also illustrates the gap between finding certificates and proving optimality. — *First step:* Build a bounded-depth ES certificate enumerator that canonicalizes symmetric triples and records the first uncovered prime at each depth.  
   `signature-0320` tags: F01, F32, F23, F24, src:addition-chains, partial, computation, gen:sub-other-fields

321. **Addition chains feature flip: minimization versus mere existence** [high/cheap] — Scholz–Brauer shares ES’s universal integers, short word certificates, and constructive recurrences (F01,F16w,F32), but asks for a near-optimal shortest chain rather than any witness. The flipped optimality constraint is what creates its sharp lower-bound difficulty. — *First step:* Compare the proof’s chain-length inequalities with ES parameter-size bounds and discard any step that depends on optimality.  
   `signature-0321` tags: F01, F16w, F32, src:addition-chains, partial, feature-flip, gen:sub-other-fields

322. **Markov uniqueness: Vieta jumping on a cubic surface** [high/medium] — Markov uniqueness shares F13,F14,F38,F23: integral points on a cubic surface have coordinate permutations and Vieta involutions, with finite computation testing uniqueness. ES is also a cubic surface with S₃ symmetry and involution structure. — *First step:* Read the Markov mutation/Vieta descent and explicitly derive any analogous involution of 4/n=1/x+1/y+1/z preserving positive integral points.  
   `signature-0322` tags: F13, F14, F38, F23, src:Markov, open, Vieta, gen:sub-other-fields

323. **Markov triples: mutation trees and orbit enumeration** [med/cheap] — Markov triples share ES’s integral cubic equation, involutive transformations, thin witness families, and finite checks (F13,F30,F38,F23). Mutation organizes infinitely many solutions from a small seed. — *First step:* Enumerate low-height ES triples modulo permutation and test for simple rational transformations preserving the defining cubic after fixing n.  
   `signature-0323` tags: F13, F30, F38, F23, src:Markov, open, orbits, gen:sub-other-fields

324. **Markov uniqueness feature flip: uniqueness of maximal coordinate** [high/cheap] — The Markov uniqueness conjecture shares ES’s cubic integral points, coordinate symmetry, and Vieta-type involutions (F13,F14,F38), but asks uniqueness of a maximal coordinate rather than existence. This feature flip spotlights orbit collisions, not missing witnesses. — *First step:* Read the uniqueness conjecture statement and compare its mutation-tree fundamental domain with ES’s S₃-reduced solution count.  
   `signature-0324` tags: F13, F14, F38, src:Markov, open, feature-flip, gen:sub-other-fields

325. **Three-generator Frobenius numbers as sparse witnesses** [med/medium] — The 3-generator Frobenius problem shares F01,F10,F23,F32: arithmetic objects are characterized by integer parameters and modular/divisibility constraints, with finite certificates and computational catalogs. ES similarly searches thin divisor witnesses for each prime. — *First step:* Read a three-generator Frobenius formula and test an Apéry-style residue table for ES’s tied divisor integer 4Cp+1.  
   `signature-0325` tags: F01, F10, F23, F32, src:Frobenius, partial, semigroups, gen:sub-other-fields

326. **Frobenius problem feature flip: fixed embedding dimension** [high/cheap] — Three-generator semigroups share ES’s universal integer parameter, divisibility certificates, and finite exception analysis (F01,F10,F25), but the Frobenius number is an output of chosen generators, not a witness for each input. This flip highlights the direction of quantifiers. — *First step:* Write the exact ∀generators ∃largest-gap quantifiers beside ES’s ∀n∃triple, then identify which Apéry formulas preserve the latter direction.  
   `signature-0326` tags: F01, F10, F25, src:Frobenius, partial, feature-flip, gen:sub-other-fields

327. **Numerical semigroup Apéry sets and finite residue certificates** [med/cheap] — The Frobenius problem shares F03,F10,F32: congruence classes modulo a generator reduce an infinite additive semigroup question to finite residue representatives. ES witness divisibility similarly reduces to residue classes and a finite certificate. — *First step:* For small primes, tabulate ES’s admissible divisors by residue class modulo 4C and compare the completeness proof format with Apéry-set closure.  
   `signature-0327` tags: F03, F10, F32, src:Frobenius, partial, residues, gen:sub-other-fields

328. **Frobenius finite exceptions and parameter stratification** [med/cheap] — Three-generated numerical semigroups share F11,F25,F32: parameter regimes can have exceptional cases and finite certificates. ES has numerator-dependent failures of related Egyptian-fraction statements and explicit finite counterexample lists. — *First step:* The ref (Moreno-Frías–Rosales 2025) concerns numerical semigroups with a given Frobenius number and fixed gaps; check whether its parameter stratification (or that in Robles-Pérez–Rosales, dimension three) offers an exceptional-parameter template for ES square classes.  
   `signature-0328` tags: F11, F25, F32, src:Frobenius, partial, exceptions, gen:sub-other-fields

329. **SL₂(Z) semigroup membership as bounded-word reachability** [med/cheap] — Matrix-semigroup membership shares F16w,F18,F32,F23: existence asks for a finite word producing a target matrix, with short certificates and decidable bounded searches. ES has a prescribed-entry SL₂ formulation and bounded certificate length. — *First step:* Encode the ES matrix identity as generators and run breadth-first search modulo small moduli, retaining only states compatible with the target entry.  
   `signature-0329` tags: F16w, F18, F32, F23, src:matrix-semigroups, partial, word-problem, gen:sub-other-fields

330. **Matrix mortality: existence of a zero-product word** [low/medium] — Matrix mortality shares F16w,F18,F32,F23: a finite word in matrices witnesses a target property; bounded word search is computationally checkable. ES is likewise a word-reachability problem with a target entry. — *First step:* Review a matrix mortality reduction and check whether its modular invariant argument yields a useful obstruction or pruning rule for ES matrices.  
   `signature-0330` tags: F16w, F18, F32, F23, src:matrix-semigroups, partial, feature-flip, gen:sub-other-fields

331. **SL₂ word problem: continued fractions as matrix products** [high/cheap] — Restricted continued fractions and SL₂ words share F16w,F17,F18,F32: a finite digit string is a short certificate for a matrix entry. ES’s length-three negative-continuant representation is unusually short, suggesting direct word enumeration. — *First step:* Derive ES’s negative-continuant matrix product explicitly and test the standard continued-fraction normalization on small prime cases.  
   `signature-0331` tags: F16w, F17, F18, F32, src:SL2, partial, continued-fractions, gen:sub-other-fields

332. **Cluster algebra friezes: Laurent positivity and integral parametrization** [low/medium] — Frieze/cluster patterns share F16w,F18,F19,F32: recurrence words generate integer entries and positivity/periodicity constraints, much like ES’s polynomial word certificates and generating-function positivity reformulation. — *First step:* Check whether ES’s cubic surface can be embedded as a rank-two cluster recurrence with a positivity invariant; begin with its trilinear identity.  
   `signature-0332` tags: F16w, F18, F19, F32, src:cluster-algebras, partial, positivity, gen:sub-other-fields

333. **Egyptian fraction greedy expansions: termination and bounded remainder** [high/cheap] — Odd greedy Egyptian expansions share F01,F12,F27,F32: positive unit-fraction representations are sought constructively, with a greedy algorithm producing short certificates when it terminates. ES fixes exactly three terms and positivity. — *First step:* Run the odd greedy algorithm symbolically on 4/n and determine the exact condition under which it terminates within three terms.  
   `signature-0333` tags: F01, F12, F27, F32, src:Egyptian-fractions, open, greedy, gen:sub-other-fields

334. **Odd greedy algorithm feature flip: unbounded term count** [high/cheap] — Greedy Egyptian expansion shares ES’s positive unit fractions, universal input, and integer certificates (F01,F12,F27), but typically permits a variable number of terms rather than fixed three. This flip pinpoints bounded-term termination as ES’s core difficulty. — *First step:* Compare the first three greedy terms for 4/p against a complete ES certificate and identify a local compression identity.  
   `signature-0334` tags: F01, F12, F27, src:Egyptian-fractions, partial, feature-flip, gen:sub-other-fields

335. **Lüroth expansions and finite digit alphabets** [low/medium] — Lüroth and continued-fraction expansions share F17,F18,F32: digits encode rational values by short arithmetic words, with bounded-digit variants producing thin sets. ES also has bounded-length CF/SL₂ descriptions. — *First step:* Search for a Lüroth representation of 4/p with constrained first digits and test whether three digit choices imply an ES decomposition.  
   `signature-0335` tags: F17, F18, F32, src:expansions, open, feature-flip, gen:sub-other-fields

336. **Pierce expansions: alternating unit-fraction dynamics** [med/cheap] — Pierce expansions share F12,F16w,F27,F32: rational numbers are encoded by a finite sequence of integer choices and positive unit-fraction arithmetic. ES asks for a fixed-term positive representation rather than a variable-length expansion. — *First step:* Write the Pierce recurrence for 4/p and check whether a two-step truncation yields a three-term ES certificate for any residue classes.  
   `signature-0336` tags: F12, F16w, F27, F32, src:expansions, partial, unit-fractions, gen:sub-other-fields

337. **Graceful tree conjecture: infinite families and absorption** [med/medium] — Graceful labeling shares F01,F05w,F23,F34: a universal finite-graph existence problem, many verified cases/families, and proof strategies that cover large classes. ES likewise needs an infinite union of thin certificate families. — *First step:* Read an absorption proof for a tree labeling result and abstract its ‘leave’ and absorber; formulate analogous objects as uncovered ES prime classes and certificate families.  
   `signature-0337` tags: F01, F05w, F23, F34, src:graceful-trees, open, absorption, gen:sub-other-fields

338. **Ringel’s tree packing: complementarity and finite obstruction checks** [med/cheap] — Ringel's conjecture (proved for large n by Montgomery–Pokrovskiy–Sudakov and Keevash–Staden) and the open graceful-tree problem share F01,F23,F34: universal finite-structure coverage, computation, and families whose union must cover all edges/labels. ES similarly unions thin prime-covering families. — *First step:* Identify the smallest uncovered residue class after a standard ES covering and see if a complementary parametrized line covers it.  
   `signature-0338` tags: F01, F23, F34, src:Ringel, solved-large-n, covering, gen:sub-other-fields

339. **Sandpile recurrence: finite states and critical group invariants** [med/cheap] — Chip-firing/sandpile questions share F18w,F23,F32: reachability under local moves has finite-state invariants and short move-sequence certificates. ES matrix-word reachability offers a similar state-transition viewpoint. — *First step:* Model ES matrix generators modulo m as a finite directed state graph and compare its conserved quantities with sandpile group invariants.  
   `signature-0339` tags: F18w, F23, F32, src:sandpiles, partial, reachability, gen:sub-other-fields

340. **Triangle altitudes and inradius: a reciprocal-sum identity** [med/cheap] — Triangle geometry gives 1/r=1/h_a+1/h_b+1/h_c, sharing F12,F13,F27,F32: a fixed three-term reciprocal identity with positive geometric/integer data in special rational triangles. This is structurally close to ES’s three-unit-fraction equation. — *First step:* Derive the altitude/inradius identity under rational side-area normalization and check which integral triangle families yield denominators matching 4/n.  
   `signature-0340` tags: F12, F13, F27, F32, src:triangle-geometry, partial, feature-flip, gen:sub-other-fields

341. **Resistor networks and reciprocal conductance decompositions** [med/cheap] — Series/parallel resistor networks share F12,F16w,F27,F32: rational effective conductance is built from reciprocal operations and positive integer network certificates. ES is a fixed three-term reciprocal decomposition. — *First step:* Translate 4/n into a three-branch parallel network and enumerate series-parallel reductions to see whether known ES identities emerge.  
   `signature-0341` tags: F12, F16w, F27, F32, src:resistor-networks, partial, feature-flip, gen:sub-other-fields

342. **Erdős–Faber–Lovász: finite colorings as congruence coverings** [med/medium] — EFL shares F01,F03,F34: every finite input must be covered by one of finitely many compatible color classes, paralleling ES’s finite residue covers and infinite certificate-line union. — *First step:* Map ES certificate families to vertices in a conflict graph (edges for incompatible residue coverage) and test whether a coloring gives a finite cover.  
   `signature-0342` tags: F01, F03, F34, src:EFL, solved-large-n, covering, gen:sub-other-fields

343. **Zaremba: transfer-operator counting for restricted digits** [med/medium] — Restricted-CF denominator problems share F17,F18,F22,F24: thin matrix semigroups are counted via digit words and growth heuristics. ES’s bounded CF length and matrix-entry target invite analogous transfer operators. — *First step:* Define a transfer operator for ES’s allowed three-step matrix digits and calculate its predicted count against small-prime data.  
   `signature-0343` tags: F17, F18, F22, F24, src:Zaremba, open, counting, gen:sub-other-fields

344. **Apollonian thin-orbit sieve and congruence expansion** [med/medium] — Apollonian packings share F03,F05,F10,F22: a thin orbit is sifted among locally allowed integers, yielding density-one coverage. ES’s witness divisors are thin and congruence constrained. — *First step:* Read the density-one theorem’s sieve dimension and test whether an ES parameter orbit has comparable equidistribution modulo squarefree moduli.  
   `signature-0344` tags: F03, F05, F10, F22, src:Apollonian, partial, sieve, gen:sub-other-fields

345. **Lonely runner: simultaneous Diophantine approximation** [med/medium] — Lonely runner shares F01,F06,F24,F32: integer parameters must admit a witness time, there are no evident local obstructions, and approximation supplies constructive witnesses. ES likewise needs a pointwise witness despite local solubility. — *First step:* Inspect the survey’s reduction to a finite set of simultaneous inequalities; ask whether ES’s divisor-in-residue condition admits a comparable finite approximation statement.  
   `signature-0345` tags: F01, F06, F24, F32, src:lonely-runner, open, approximation, gen:sub-other-fields

346. **Collatz: density notions and logarithmic sampling** [med/cheap] — Collatz and ES share F05,F21,F23,F24: strong almost-all/computational evidence leaves pointwise exceptional inputs unresolved. Tao’s logarithmic-density approach makes the quantifier gap explicit. — *First step:* Compute the logarithmic count of ES primes lacking each fixed certificate family over existing bounded data and compare with natural-density counts.  
   `signature-0346` tags: F05, F21, F23, F24, src:Collatz, partial, density, gen:sub-other-fields

347. **Egyptian fraction identities as local witness transformations** [high/cheap] — Egyptian fraction problems share F12,F14,F16w,F27: positive reciprocal equations have permutation symmetry and algebraic transformations between representations. ES has the same three-term symmetric witness geometry. — *First step:* Enumerate unit-fraction splitting identities preserving denominator divisibility by p and check if they close a missing ES square class.  
   `signature-0347` tags: F12, F14, F16w, F27, src:Egyptian-fractions, solved, identities, gen:sub-other-fields

348. **Kourovka group problems: SL₂(Z) word reachability** [med/cheap] — Group word problems share F16w,F18,F32: whether a target element is represented by a word has a short explicit certificate and congruence quotients provide cheap tests. ES has a prescribed-entry SL₂ reachability form. — *First step:* Take the ES generator matrices, compute their images in SL₂(Z/mZ) for small m, and compare reachable target-entry states by prime residue.  
   `signature-0348` tags: F16w, F18, F32, src:Kourovka, partial, groups, gen:sub-other-fields

349. **Group word-problem feature flip: equality versus existence** [high/cheap] — Group word problems share ES’s finite words, matrix structure, and short certificates (F16w,F18,F32), but often ask whether two given words are equal, rather than whether some witness word exists. This feature flip marks a decision-versus-search distinction. — *First step:* Check whether the ES generator set admits a normal form in SL₂(Z); if not, test the simpler congruence quotient search first.  
   `signature-0349` tags: F16w, F18, F32, src:Kourovka, partial, feature-flip, gen:sub-other-fields

350. **Erdős–Faber–Lovász feature flip: exact bound versus asymptotic bound** [high/cheap] — EFL shares ES’s universal finite objects, covering structure, and computational finite verification (F01,F03,F23), but an asymptotic ‘large n’ theorem alone does not cover small instances. ES likewise needs all n, not almost all. — *First step:* Extract the large-n threshold from the EFL proof and compare the role of finite verification with ES’s computational range.  
   `signature-0350` tags: F01, F03, F23, src:EFL, solved-large-n, feature-flip, gen:sub-other-fields

351. **Apollonian curvature counterfamilies as a test for ES square obstructions** [med/medium] — Apollonian local-global phenomena share ES’s congruence covers, thin witness sets, and algebraic exceptional families (F03,F08w,F22). The comparison is specifically between an orbit missing a structured family and ES’s square-class failure modes. — *First step:* Read the 2024 paper’s missed-family construction and try to formulate an invariant on ES’s quadratic witness equation that vanishes on squares.  
   `signature-0351` tags: F03, F08w, F22, src:Apollonian, partial, feature-flip, gen:sub-other-fields

352. **Frobenius semigroups and conductor-style ES bounds** [med/medium] — Numerical semigroups share ES’s integer parameterization, finite residue representatives, and explicit size bounds (F10,F15,F32). Frobenius conductor arguments turn residue coverage into a maximum-gap bound. — *First step:* For each ES modulus 4C, derive the largest missing admissible divisor residue from small data and seek a semigroup-style conductor bound.  
   `signature-0352` tags: F10, F15, F32, src:Frobenius, partial, bounds, gen:sub-other-fields

353. **Addition-chain recurrences as ES multiplicative closure analogues** [med/medium] — Addition chains share F02w,F16w,F30,F32: recursive operations extend certificates from known inputs, and special infinite families follow. ES also has multiple-closure and thin recursive prime families. — *First step:* Search the addition-chain constructions for an explicit certificate-extension recurrence and test whether an ES identity can realize n↦2n+c.  
   `signature-0353` tags: F02w, F16w, F30, F32, src:addition-chains, partial, recurrence, gen:sub-other-fields

354. **Zaremba and ES: finite alphabet versus finite word length** [high/cheap] — Both Zaremba and ES use continued fractions and SL₂ words (F17,F18,F32), but Zaremba constrains the digit alphabet while ES constrains word length and matrix entries. This feature flip isolates alphabet complexity from length complexity. — *First step:* Compute partial quotients of the ES₅ representations for small primes and test for a finite digit alphabet covering a positive fraction.  
   `signature-0354` tags: F17, F18, F32, src:Zaremba, open, feature-flip, gen:sub-other-fields

355. **Tiling problems: local rules and global periodic witnesses** [low/medium] — Tiling existence shares F01,F03,F23,F32: local compatibility constraints must yield a global object, finite patches provide certificates, and computational searches test instances. ES similarly combines local congruences with a global positive integral witness. — *First step:* Choose a concrete Wang-tile undecidability example and compare its local-to-global obstruction with ES’s local solubility; do not assume the techniques transfer absent a finite-state reduction.  
   `signature-0355` tags: F01, F03, F23, F32, src:tilings, partial, feature-flip, gen:sub-other-fields

356. **ES reciprocal equation through the triangle geometry lens** [med/medium] — Triangle altitude/inradius identities share F12,F13,F27,F33: a positive reciprocal sum is encoded by a geometric surface with integral/rational parameter families. This is structurally close to the ES affine cubic surface. — *First step:* Homogenize the triangle identity and ES surface side by side and identify whether either has a birational map preserving positive rational points.  
   `signature-0356` tags: F12, F13, F27, F33, src:triangle-geometry, partial, surfaces, gen:sub-other-fields

357. **Markov Vieta involutions and ES divisor involution test** [high/cheap] — Markov and ES share F13,F14,F38: cubic surfaces with coordinate symmetry and involutive transformations. Markov’s mutation gives a concrete comparison to ES’s fixed-fibre hyperbola involution. — *First step:* Write the ES fixed-x factorization and its divisor-pair swap, then compare its orbit structure with Markov mutation descent.  
   `signature-0357` tags: F13, F14, F38, src:Markov, partial, involutions, gen:sub-other-fields

358. **Lonely runner feature flip: interval witness versus divisor witness** [high/cheap] — Lonely runner shares F01,F06,F24,F32 with ES’s universal witness search, but its witness is a real-time interval event rather than an integer divisor (F10). This feature flip marks discreteness as the central obstacle to importing compactness. — *First step:* Take a proof of a small lonely-runner case and mark every use of continuity; compare against an ES proof attempt to locate where a divisor theorem must replace it.  
   `signature-0358` tags: F01, F06, F24, F32, src:lonely-runner, open, feature-flip, gen:sub-other-fields

359. **Addition-chain certificate-size analogy for ES witnesses** [med/cheap] — Addition chains and ES share F01,F23,F24,F32: universal arithmetic targets, finite certificates, computational checking, and heuristic expectations of manageable witness size. ES denominators can be checked exactly in polynomial-time arithmetic. — *First step:* Bound the bit-length of ES witness coordinates in terms of p for each known parametrized family and compare with generic addition-chain length bounds.  
   `signature-0359` tags: F01, F23, F24, F32, src:addition-chains, partial, certificates, gen:sub-other-fields

360. **Egyptian fraction counts and sieve moments** [high/medium] — ES shares F04, F12, F21, F22 with counting representations by unit fractions. The transferable object is a count of divisor parametrisations rather than mere existence. — *First step:* Read Elsholtz–Tao, identify their count parametrisation, and test whether the second-moment argument localizes to prime n.  
   `signature-0360` tags: F04, F12, F21, F22, src:tao-blog, partial, egyptian-fractions, gen:sub-generic

361. **General fixed-numerator Egyptian fraction conjectures** [high/medium] — Schinzel-type equations m/n as bounded sums share F01, F02w, F11, F12, F25. The contrast between numerator 4 and neighboring numerators is structurally relevant. — *First step:* Compare the known m=4 and m>4 constructions and isolate the first point where constants cease to be uniform.  
   `signature-0361` tags: F01, F02, F11, F12, F25, src:mathoverflow, open, feature-flip, gen:sub-generic

362. **Four-unit-fraction representations** [med/cheap] — The four-term Egyptian fraction problem shares F01, F12, F27, F33, while adding a spare summand changes the geometry of the equation. — *First step:* Classify standard four-term constructions by whether two terms combine to a unit fraction and test the resulting divisibility condition for p.  
   `signature-0362` tags: F01, F12, F27, F33, src:mathoverflow, solved, feature-flip, gen:sub-generic

363. **Egyptian fractions with distinct denominators** [med/cheap] — Distinct-denominator variants share F01, F12, F27 and the positivity constraint, but impose an extra exclusion on the ES witness. — *First step:* Read the distinct-denominator constructions in Graham's survey and check which families permit coincident denominators.  
   `signature-0363` tags: F01, F12, F27, src:ucsd, solved, feature-flip, gen:sub-generic

364. **Unit fractions with restricted prime factors** [low/medium] — Restricted-denominator Egyptian fraction problems share F10, F12, F22, F29: existence becomes a question about allowed divisors in arithmetic classes. — *First step:* Search the literature for restricted-prime-factor unit fraction equations and extract the exact divisor-sum identity.  
   `signature-0364` tags: F10, F12, F22, F29, src:arxiv, partial, gen:sub-generic

365. **Divisor equations in the Erdős–Straus parametrisation** [high/medium] — The divisor-sum formulation shares F10, F15, F21, F29: an ES witness exists iff a p-tied integer has a divisor in a prescribed residue class (this sub-problem is open, not solved). — *First step:* For prime p≡1 mod 4, derive the precise divisor interval and compare with known bounds for divisors in arithmetic progressions.  
   `signature-0365` tags: F10, F15, F21, F29, src:tao-blog, partial, divisors, gen:sub-generic

366. **Sums of two unit fractions and multiplication tables** [med/cheap] — Two-term reciprocal equations share F10, F15, F33 and reduce to factor pairs, much like each fixed-x ES fibre. — *First step:* Write the two-term equation as (a y−b)(a z−b)=c and catalogue the bounds retained when one term is fixed.  
   `signature-0366` tags: F10, F15, F33, src:aimspress, solved, divisors, gen:sub-generic

367. **Function-field Egyptian fractions** [med/medium] — Function-field analogues share F01, F12, F26, F27 and replace integer primes by irreducible polynomials. — *First step:* Locate the function-field ES proof and translate its key divisor-counting lemma to integer primes, marking the exact failed estimate.  
   `signature-0367` tags: F01, F12, F26, F27, src:arxiv, solved, gen:sub-generic

368. **Unit-fraction equations over polynomial rings** [low/medium] — Polynomial-ring reciprocal equations share F12, F13, F26 and often admit algebraic factorisation unavailable over integers. — *First step:* Compare the polynomial proof's factorisation with the integer identity (4x−p)(4y−p)(4z−p) variants.  
   `signature-0368` tags: F12, F13, F26, src:arxiv, solved, gen:sub-generic

369. **Local-global principles for integral points on surfaces** [med/medium] — Integral surface families share F06, F07, F13, F21: local solubility and Brauer–Manin tests may leave integral-point existence unresolved. — *First step:* Compare ES's surface with published counterexamples to integral Hasse principles; test whether a descent or torsor formulation exists.  
   `signature-0369` tags: F06, F07, F13, F21, src:literature, partial, arithmetic-geometry, gen:sub-generic

370. **Brauer–Manin obstruction in integral-point problems** [med/medium] — Integral-point problems share F07, F13, F20 and distinguish rational points from integral points via adelic conditions. — *First step:* Read Bright–Loughran's ES analysis and compare its adelic pairing computation with one integral-surface example.  
   `signature-0370` tags: F07, F13, F20, src:arxiv, partial, BM, gen:sub-generic

371. **Hasse norm principle and norm-form equations** [med/medium] — Norm-form local-global problems share F06, F07, F20, F29; quadratic characters encode splitting and local constraints. — *First step:* Rewrite the hard p≡1 mod 4 case using norms from Q(i), then compare local-global criteria for the resulting norm equation.  
   `signature-0371` tags: F06, F07, F20, F29, src:arxiv, partial, gen:sub-generic

372. **Châtelet surfaces and descent by torsors** [low/medium] — Châtelet-type surfaces share F07, F13, F15 and may turn a surface-point question into norm equations and divisor conditions. — *First step:* Check whether an ES fibre is birational to a conic bundle with a usable torsor descent; derive the smallest fibre example.  
   `signature-0372` tags: F07, F13, F15, src:arxiv, solved, geometry, gen:sub-generic

373. **Integral points on log K3 surfaces** [low/medium] — The ES family shares F07, F13, F32 with integral-point problems on affine log K3 surfaces. — *First step:* Check the ES surface's classification and compare available integral-point algorithms for the same surface type.  
   `signature-0373` tags: F07, F13, F32, src:arxiv, partial, geometry, gen:sub-generic

374. **Conic bundles and integral fibres** [med/medium] — Conic-bundle families share F13, F15, F29 and make each base value a separate factorisation problem. — *First step:* Express the ES surface as a conic bundle and inspect uniform integral-point bounds for its fibre discriminants.  
   `signature-0374` tags: F13, F15, F29, src:arxiv, partial, gen:sub-generic

375. **Vieta jumping on cubic Diophantine surfaces** [med/cheap] — Cubic surface Diophantine problems share F13, F14, F38, with solution-preserving swaps or involutions. — *First step:* Check whether the ES involution graph has a canonical reduced representative for each orbit by minimizing max(x,y,z).  
   `signature-0375` tags: F13, F14, F38, src:arxiv, partial, symmetry, gen:sub-generic

376. **Pell equations and thin prime families** [med/cheap] — Pell-type problems share F02w, F30, F34, often proving infinite but thin parameterized families. — *First step:* Search Pell parameterisations yielding ES identities and compute the induced prime residue classes symbolically.  
   `signature-0376` tags: F02, F30, F34, src:arxiv, partial, thin-families, gen:sub-generic

377. **Polynomial identity methods for Diophantine coverings** [med/medium] — Polynomial identity problems share F03, F09, F34, F35: finite algebraic families cover some classes but may provably miss others. — *First step:* Formalize ES identity families as polynomial maps and compute the algebraic locus they cover modulo several small primes.  
   `signature-0377` tags: F03, F09, F34, F35, src:arxiv, partial, gen:sub-generic

378. **Hasse principle failures for affine cubic surfaces** [med/medium] — Affine cubic surfaces share F07, F13, F27, where positivity and integrality make rational-point results insufficient. — *First step:* Collect cubic-surface counterexamples with local points but no integral points and compare the missing integrality condition to ES positivity.  
   `signature-0378` tags: F07, F13, F27, src:arxiv, partial, gen:sub-generic

379. **Integral points and effective height bounds** [med/medium] — Effective integral-point problems share F13, F32 and the tension between small certificates and uniform existence. — *First step:* Check known effective bounds for integral points on the ES surface and identify whether they are uniform in the parameter p.  
   `signature-0379` tags: F13, F32, src:arxiv, partial, height, gen:sub-generic

380. **Rational points versus integral points on cubic surfaces** [med/cheap] — The distinction shares F07, F13, F27: rational parametrisation need not preserve positive integral coordinates. — *First step:* Take a rational parametrisation of the ES surface, track denominator divisibility, and compare with integral-point parametrisations in the literature.  
   `signature-0380` tags: F07, F13, F27, src:arxiv, partial, gen:sub-generic

381. **Circle method exceptional sets for Diophantine equations** [high/medium] — Almost-all Diophantine results share F05, F21, F40: average abundance can coexist with a difficult thin exceptional set. — *First step:* Compare ES's 3/4 exponent proof with circle-method exceptional-set arguments and identify the precise sieve loss.  
   `signature-0381` tags: F05, F21, F40, src:tao-blog, partial, exceptional-set, gen:sub-generic

382. **Large sieve for thin exceptional sets** [med/medium] — Thin-set problems share F05, F22, F40 and need upper bounds for integers evading every local or combinatorial route. — *First step:* Identify the moduli and sieve dimension in the ES exceptional-set argument, then test a larger-sieve bound on the same sequence.  
   `signature-0382` tags: F05, F22, F40, src:arxiv, partial, sieve, gen:sub-generic

383. **Sieve methods for almost-prime values of polynomials** [low/big] — Polynomial sieve problems share F05, F22, F40 and seek pointwise hits in sparse arithmetic sets. — *First step:* Translate the ES witness parameter into a polynomial sequence and check whether a bilinear or dispersion estimate applies.  
   `signature-0383` tags: F05, F22, F40, src:arxiv, partial, sieve, gen:sub-generic

384. **Parity problem in sieve theory** [med/medium] — Sieve parity problems share F21, F22, F40 and explain why robust average estimates may fail to detect a single required arithmetic type. — *First step:* Check whether ES's restricted-divisor sequence has a parity-insensitive distribution indistinguishable from a counterexample sequence.  
   `signature-0384` tags: F21, F22, F40, src:arxiv, partial, feature-flip, gen:sub-generic

385. **Linear sieve and switching principles** [med/medium] — Thin sequence sieve problems share F05, F22, F40 and often gain from switching between primal and dual variables. — *First step:* Recast the ES divisor condition in both numerator and divisor variables and check whether a switching identity improves level of distribution.  
   `signature-0385` tags: F05, F22, F40, src:arxiv, partial, sieve, gen:sub-generic

386. **Sum-product estimates for reciprocal sets** [med/medium] — Reciprocal additive equations share F12, F22, F33 and couple additive structure to multiplication of denominators. — *First step:* Apply an incidence bound to the sets {1/a} and {1/b+1/c} for bounded denominator ranges and compare with required p-scale.  
   `signature-0386` tags: F12, F22, F33, src:arxiv, partial, additive-combinatorics, gen:sub-generic

387. **Multiplication-table divisor distribution** [med/cheap] — Multiplication tables share F10, F15, F21: ES needs a divisor in a specific congruence class of a tied integer. — *First step:* For the forms 4Cp+1, tabulate divisors by residue class and interval for a bounded sample of primes, then compare with known multiplication-table bounds.  
   `signature-0387` tags: F10, F15, F21, src:arxiv, partial, divisors, gen:sub-generic

388. **Divisors in arithmetic progressions** [high/medium] — Residue-restricted divisor problems share F10, F20, F21, F29 and are a direct analytic analogue of the ES witness criterion. — *First step:* Extract bounds for sum_{d|N, d≡−1 mod q}1 and specialize N to ES's p-tied forms.  
   `signature-0388` tags: F10, F20, F21, F29, src:arxiv, partial, gen:sub-generic

389. **Character-sum cancellation and genus terms** [high/medium] — Character-sum counting shares F04, F20, F21; real characters can dominate while non-real characters cancel on average. — *First step:* Re-derive the count's character expansion and isolate the Kronecker-character term for p≡1 mod 4.  
   `signature-0389` tags: F04, F20, F21, src:tao-blog, partial, characters, gen:sub-generic

390. **Chebotarev and splitting-sensitive Diophantine families** [med/medium] — Splitting problems share F06, F29, F36; Chebotarev controls average prime classes but not necessarily a witness for every prime. — *First step:* List which ES identity families require p split in Q(i), and check whether a compositum's Frobenius classes encode them.  
   `signature-0390` tags: F06, F29, F36, src:arxiv, partial, primes, gen:sub-generic

391. **Quadratic reciprocity obstructions in parametrised identities** [high/cheap] — Reciprocity-limited parametrisations share F08, F09, F29: a natural family fails on a quadratic-residue locus. — *First step:* For each known ES family, record its Legendre-symbol condition and test whether two families have complementary failure sets.  
   `signature-0391` tags: F08, F09, F29, src:arxiv, partial, reciprocity, gen:sub-generic

392. **Covering congruences in prime representation problems** [med/cheap] — Finite congruence coverings share F03, F29, F34 and build a union of identity families over residue classes. — *First step:* Encode existing ES identity conditions as residue-class sets modulo a common modulus and search for minimal complementary covers.  
   `signature-0392` tags: F03, F29, F34, src:arxiv, partial, coverings, gen:sub-generic

393. **Infinite covering systems by parametrised families** [med/big] — Infinite covering problems share F03w, F30, F34 and replace one finite certificate with infinitely many thin families. — *First step:* Sort known ES families by prime density and overlap; formulate a criterion under which their union covers all primes.  
   `signature-0393` tags: F03, F30, F34, src:arxiv, open, coverings, gen:sub-generic

394. **Finite certificate impossibility and polynomial values** [med/medium] — Bounded-certificate failures share F09, F35, F36 and show that fixed algebraic templates can miss infinitely many inputs. — *First step:* Read the proof of the conditional no-finite-scheme result and list precisely which assumptions fail for infinite or adaptive schemes.  
   `signature-0394` tags: F09, F35, F36, src:arxiv, partial, gen:sub-generic

395. **Prime gaps and thin algebraic sequences** [low/medium] — Thin-family problems share F30, F34, F36 and balance infinitely many explicit cases against no density guarantee. — *First step:* For a known ES-valid sequence, count primes in its values or identify a guaranteed prime subsequence using established results.  
   `signature-0395` tags: F30, F34, F36, src:arxiv, partial, thin-families, gen:sub-generic

396. **Random covering and coupon-collector heuristics** [med/cheap] — Random covering models share F03, F24, F34; many thin identity families may collectively cover each prime class. — *First step:* Estimate coverage probabilities from the actual residue conditions of known ES identities, not independent random assumptions.  
   `signature-0396` tags: F03, F24, F34, src:arxiv, heuristic, gen:sub-generic

397. **Poisson heuristics for rare representation counts** [med/cheap] — Rare-count problems share F04, F24, F37 and model the number of representations as a random variable with fluctuations. — *First step:* Estimate the mean and variance of the prime witness count from data and compare against a Poisson model stratified by p mod 8.  
   `signature-0397` tags: F04, F24, F37, src:tao-blog, heuristic, gen:sub-generic

398. **Large deviations for arithmetic representation counts** [med/medium] — Representation-count problems share F04, F21, F24 and require a lower-tail bound rather than just a mean estimate. — *First step:* Check independence or dependency hypotheses for the ES representation indicators and compute a second-moment lower-tail bound.  
   `signature-0398` tags: F04, F21, F24, src:arxiv, partial, gen:sub-generic

399. **Linnik-type maximal fluctuations of representation functions** [med/medium] — Arithmetic representation functions share F04, F21, F37: average sizes can coexist with exceptional large spikes. — *First step:* Read the maximal-order bound for the relevant divisor sum and derive what it says about ES witness-count fluctuations.  
   `signature-0399` tags: F04, F21, F37, src:arxiv, partial, gen:sub-generic

400. **Computational proof certificates for Diophantine existence** [high/cheap] — Certificate problems share F23, F32, F35: a compact witness is easy to verify even when finding one universally is hard. — *First step:* Design a checker for a residue-class identity certificate and verify its proof obligations independently of the generator.  
   `signature-0400` tags: F23, F32, F35, src:arxiv, partial, certificates, gen:sub-generic

401. **Formal verification of exhaustive congruence arguments** [high/medium] — Finite congruence proofs share F03, F23, F32 and can be checked by small proof certificates. — *First step:* Encode the standard ES Mordell identities and their residue coverage in a proof assistant or a short independently audited checker.  
   `signature-0401` tags: F03, F23, F32, src:arxiv, solved, computation, gen:sub-generic

402. **SAT/SMT search for Diophantine identity families** [med/medium] — Identity-search problems share F03, F16, F32 and turn bounded algebraic templates into a finite search space. — *First step:* Generate bounded-coefficient bilinear/trilinear identities for ES and SAT-search for residue coverage beyond known families.  
   `signature-0402` tags: F03, F16, F32, src:arxiv, partial, computation, gen:sub-generic

403. **Continued fractions and bounded-length Diophantine representations** [high/medium] — Bounded continued-fraction problems share F16, F17, F32 and encode integers through short recurrences. — *First step:* Translate the ES₅ formulation into continuants and search for a theorem bounding the omitted length-three cases.  
   `signature-0403` tags: F16, F17, F32, src:arxiv, partial, continued-fractions, gen:sub-generic

404. **Theta series and coefficient nonvanishing** [med/medium] — Theta-series problems share F19, F31, F32: arithmetic representations become coefficients of modular generating functions. — *First step:* Inspect the ES theta-quotient identity and compare it with modular-form coefficient nonvanishing criteria at prime indices.  
   `signature-0404` tags: F19, F31, F32, src:arxiv, partial, modular-forms, gen:sub-generic

405. **Modular forms and nonvanishing of Fourier coefficients** [med/medium] — Coefficient-nonvanishing problems share F19, F20, F36; analytic average nonvanishing may fall short of every prime coefficient. — *First step:* Identify the modular object, its Eisenstein/cusp decomposition, and available nonvanishing theorems for the relevant prime subsequence.  
   `signature-0405` tags: F19, F20, F36, src:arxiv, partial, gen:sub-generic

406. **Quaternion orders and representation of primes** [low/medium] — Quaternionic representation problems share F29, F31, F36 and encode prime splitting through lattice or order structure. — *First step:* Write the ES quadratic-form reformulation explicitly and compare its lattice with norm representations in a quaternion order.  
   `signature-0406` tags: F29, F31, F36, src:arxiv, partial, gen:sub-generic

407. **Lattice-point counts on hyperbolas in residue classes** [high/medium] — Fixed-x ES slices share F15, F21, F29 with lattice-point problems on split hyperbolas under congruence restrictions. — *First step:* Count factor pairs of the fixed-x product equation in the required residue classes using divisor bounds and compare across x.  
   `signature-0407` tags: F15, F21, F29, src:tao-blog, partial, lattice-points, gen:sub-generic

408. **Bilinear forms in Kloosterman sums** [low/big] — Kloosterman-sum problems share F10, F20, F21 and can control divisor variables tied by a modular inverse condition. — *First step:* Derive the modular inverse relation from an ES divisor parametrisation and check if the resulting sum matches a known bilinear Kloosterman estimate.  
   `signature-0408` tags: F10, F20, F21, src:arxiv, partial, analytic-number-theory, gen:sub-generic

409. **Additive combinatorics of reciprocal residues** [med/medium] — Reciprocal residue sets share F10, F22, F33, where modular inverses combine additively to hit a target residue. — *First step:* For a prime modulus, compute restricted reciprocal sumsets from the ES denominator conditions and test known sum-product expansion bounds.  
   `signature-0409` tags: F10, F22, F33, src:arxiv, partial, additive-combinatorics, gen:sub-generic

410. **Graph connectivity of Diophantine representations** [med/cheap] — Representation graphs share F14, F38, F39: vertices are solutions and local transformations connect them. — *First step:* Construct the ES witness graph under coordinate swaps and Vieta moves for small primes, then determine whether graph invariants suggest a general connectivity lemma.  
   `signature-0410` tags: F14, F38, F39, src:arxiv, partial, graphs, gen:sub-generic

411. **Orbit counting under S3 symmetry** [high/cheap] — Symmetric representation problems share F14, F38, F04; orbit-stabilizer corrections affect the count of witnesses. — *First step:* Compute stabilizers of ES triples and derive an orbit-count identity for R(p), including repeated-coordinate cases.  
   `signature-0411` tags: F04, F14, F38, src:tao-blog, partial, symmetry, gen:sub-generic

412. **Branching processes for solution-tree growth** [low/cheap] — Solution-tree problems share F24, F38, F39 and model repeated involutive moves as branching orbits. — *First step:* Determine whether the ES transformation graph is locally tree-like at bounded height and calculate its first-return probabilities.  
   `signature-0412` tags: F24, F38, F39, src:arxiv, heuristic, gen:sub-generic

413. **Universal Diophantine statements with multiplicative closure** [med/cheap] — Universal representation problems share F01, F02, F06; multiplicative closure reduces the domain to primes plus local cases. — *First step:* Formalize the ES multiple-closure map and compare it with closure reductions in other universal Diophantine representation problems.  
   `signature-0413` tags: F01, F02, F06, src:arxiv, solved, reductions, gen:sub-generic

414. **Local solubility without integral global points** [high/medium] — Local-global counterexamples share F06, F07, F27 and test whether local conditions suffice under positivity and integrality. — *First step:* Compare ES with integral conic and norm-form examples having solutions at every completion but no integral point.  
   `signature-0414` tags: F06, F07, F27, src:arxiv, partial, feature-flip, gen:sub-generic

415. **Positivity in additive Diophantine equations** [med/cheap] — Positive-variable problems share F27, F33, F01, while signed solutions can be plentiful and structurally misleading. — *First step:* List all sign-sensitive inequalities in the ES parametrisations and test whether they define a convex feasible region for one denominator.  
   `signature-0415` tags: F01, F27, F33, src:arxiv, partial, gen:sub-generic

416. **Almost-all versus every-input representation theorems** [high/medium] — Universal-versus-almost-all problems share F01, F05, F21 and make exceptional inputs the central issue. — *First step:* Compare the proof architecture of an almost-all theorem with a pointwise theorem for a nearby fixed-term representation problem.  
   `signature-0416` tags: F01, F05, F21, src:tao-blog, partial, gen:sub-generic

417. **Branching of prime representations by quadratic forms** [med/medium] — Quadratic-form representation problems share F29, F31, F36 and encode prime classes through splitting and lattice points. — *First step:* List the quadratic forms in ES reformulations and compare their represented prime classes via genus characters.  
   `signature-0417` tags: F29, F31, F36, src:arxiv, partial, quadratic-forms, gen:sub-generic

418. **Genus theory and one-sided representation counts** [high/medium] — Genus-theory problems share F20, F29, F31 and can explain main terms while leaving a pointwise positive count unsettled. — *First step:* Decompose the ES count into genus characters and compare the local densities with the predicted main term for each prime class.  
   `signature-0418` tags: F20, F29, F31, src:tao-blog, partial, gen:sub-generic

419. **Residue-class divisor sums and real-character bias** [high/medium] — Divisor sums share F10, F20, F37; exceptional real characters can create one-sided fluctuations. — *First step:* Compute the real-character contribution to the ES divisor count separately and see when it can dominate the error terms.  
   `signature-0419` tags: F10, F20, F37, src:tao-blog, partial, characters, gen:sub-generic

420. **Exceptional primes for parametrised reciprocal identities** [med/cheap] — Sparse algebraic failure sets share F08w, F25, F30, where a construction works except at explicit exceptional inputs. — *First step:* For each ES identity family, factor the obstruction polynomial and compare its prime roots with the failures of sister statements.  
   `signature-0420` tags: F08, F25, F30, src:arxiv, partial, feature-flip, gen:sub-generic

421. **Prime gaps inside thin congruence-defined families** [low/big] — Thin-family and congruence problems share F03w, F30, F36; families may contain infinitely many primes without positive density. — *First step:* Check whether any known ES parameter sequences are polynomial or recurrence sequences with established prime-counting theorems.  
   `signature-0421` tags: F03, F30, F36, src:arxiv, partial, gen:sub-generic

422. **Adelic methods for integral points in families** [med/medium] — Arithmetic families share F06, F07, F13, F20; local densities may vary with the parameter and influence global integral points. — *First step:* Compute local densities of ES surface points at primes dividing 2p and compare with the global expected count across p residue classes.  
   `signature-0422` tags: F06, F07, F13, F20, src:arxiv, partial, gen:sub-generic

423. **Certificate-length bounds and NP-style arithmetic witnesses** [high/medium] — Small-witness problems share F32, F01, F23: every positive instance has a short certificate even if universal existence is open. — *First step:* Derive an explicit bound on the minimal ES denominator from known constructions and test whether it is polynomial in p with effective constants.  
   `signature-0423` tags: F01, F23, F32, src:tao-blog, partial, gen:sub-generic

424. **Erdős–Tetali thin bases: random sets A with r_{A,k}(n) ≍ log n for EVERY n — the polylog pointwise regime, solved probabilistically** [high/cheap] — Erdős–Tetali (1990): for every k there is a basis of order k with Θ(log n) representations of every large n. Same regime as ES (F04: polylog count, F01: every n, F21: pointwise), proved by independence + concentration (Janson/Chernoff) of the random set. — *First step:* Estimate the dependency structure of the ES level events at fixed p (pairwise correlations over (u,B,C)) and compare with the Erdős–Tetali concentration hypotheses (bounded pairwise dependence, expected count ≥ C log n with large C).  
   `signature-0424` tags: F04, F21, F24, probabilistic-method, thin-bases, solved-sibling, src:own, gen:integrator

425. **Erdős–Turán conjecture (a basis has unbounded r(n)) vs. ES's Linnik-type large values** [med/cheap] — Erdős–Turán: if r_{A+A}(n) ≥ 1 for all large n then r is unbounded. ES's R(p) is unbounded (Linnik-type large values; F37) consistent with this shape; ES's word set is a 'basis' of the primes in a trilinear sense. — *First step:* Check whether Erdős–Fuchs (no representation function is c + small error on average) applies to Σ_{n≤N} R(n) to give a lower bound on its fluctuations.  
   `signature-0425` tags: F37, additive-bases, erdos-fuchs, src:own, gen:integrator

426. **Sawin–Shusterman: twin primes and Chowla over F_q[T] (q large) by étale cohomology — the geometric pointwise route** [med/medium] — Over F_q[T] with q fixed but large relative to degree, they prove twin-prime-type asymptotics via cohomology of moduli spaces. ES has function-field variants (F26). — *First step:* Write the ES count over F_q[T] at fixed prime polynomial P as a point count of a variety V_P/F_q and check whether its top cohomology is controllable (dimension, irreducibility).  
   `signature-0426` tags: F26, F21, function-field, etale-cohomology, src:own, gen:integrator

427. **Sun's 1-3-5 conjecture proved via Lipschitz quaternions (Machiavelo–Tsopanidis): ∀n with an extra linear constraint** [med/medium] — Every n is x²+y²+z²+w² with x + 3y + 5z a square — a ∀n∃ witness statement with a constraint, proved by quaternion arithmetic (F31). ES has quaternion-order reformulations. — *First step:* Read the paper's key lemma (factorisation in Lipschitz integers with prescribed residue) and compare with the QUATERNION_ES dictionary.  
   `signature-0427` tags: F31, F01, quaternions, solved-sibling, seen:QUATERNION_ES.md, src:own, gen:integrator

428. **Zhi-Wei Sun's family of refined-Lagrange conjectures with explicit finite exception lists** [med/cheap] — Sun posed dozens of 'every n is … with constraint …' conjectures, each with finite explicit exceptions; several were proved (ternary forms, quaternions, spinor theory). Shares F01, F25, F23. — *First step:* Scan Sun's survey of conjectures on refinements of Lagrange's four-square theorem; list proved ones and their tools.  
   `signature-0428` tags: F25, F01, catalogue, quadratic-forms, src:own, gen:integrator

429. **Andrews–Dyson–Hickerson: σ(q) coefficients almost always 0 yet unbounded, via indefinite theta / Hecke characters of ℚ(√6)** [med/medium] — ADH express coefficients of a q-series (σ(q)) as signed counts of ideals in a real quadratic field (indefinite binary form). ES's level series is a Kronecker theta quotient θ(X²)/θ(X)² — also an indefinite (signature (1,1)) theta object (F19). — *First step:* Write D_t⁻ − D_t⁺ as a sum over x² − y² type forms (split indefinite theta) and look for an ADH-style real-quadratic twist with the same coefficients.  
   `signature-0429` tags: F19, indefinite-theta, q-series, mock-modular, src:own, gen:integrator

430. **Zwegers/Appell–Lerch: Kronecker's θ(x²)/θ(x)²-type quotients as Appell–Lerch sums with completions** [med/medium] — Quotients of Jacobi theta functions in the elliptic variable are Appell–Lerch sums (Kronecker's identity); Zwegers' completion makes them harmonic Maass–Jacobi forms. ES's (K1′) normal form is such a quotient (F19). — *First step:* Match (K1′) of METAPLECTIC_ES with Zwegers' μ(u,v;τ) and compute its completion; check whether the nonholomorphic part is supported on squares (T1).  
   `signature-0430` tags: F19, F08, mock-modular, appell-lerch, seen:METAPLECTIC_ES.md, src:own, gen:integrator

431. **ES ⟺ every (4−n)/n is the Euler characteristic of a hyperbolic triangle orbifold S²(x,y,z)** [med/cheap] — χ(S²(x,y,z)) = 1/x + 1/y + 1/z − 1, so ES(n) ⟺ some triangle orbifold has χ = (4 − n)/n, i.e. hyperbolic area 2π(n−4)/n (n ≥ 5). By Riemann–Hurwitz any finite quotient G of the triangle group acting on genus g satisfies |G|(n−4) = 2n(g−1). — *First step:* Check whether 'which rationals are Euler characteristics of triangle orbifolds' appears in the orbifold literature, and test small p via tables of triangle groups with given area.  
   `signature-0431` tags: geometry, orbifolds, reformulation, F12, F14, src:own, gen:integrator

432. **Strong symmetric genus spectrum (May–Zimmerman: every value occurs) as a ∀g∃G sibling via triangle groups** [low/cheap] — May–Zimmerman: there is a group of every strong symmetric genus. Proofs use explicit group families acting with triangle signatures; Riemann–Hurwitz ties genus to 1/x + 1/y + 1/z (see triangle-orbifold item). Shares F01, F12. — *First step:* Read May–Zimmerman's construction and check which signatures (x,y,z) and areas arise; see if area (p−4)/p is ever forced.  
   `signature-0432` tags: F01, F12, group-actions, riemann-surfaces, src:own, gen:integrator

433. **Hurwitz 84(g−1) / the spectrum of 1 − 1/x − 1/y − 1/z: gaps near 0 vs ES's values (n−4)/n** [low/cheap] — The set {1 − 1/x − 1/y − 1/z} has the minimum positive value 1/42 and a well-studied accumulation structure (Hurwitz). ES asks whether every (n−4)/n belongs to {1 − Σ1/x_i} (n ≥ 5). — *First step:* Compute the area spectrum up to denominator 10⁶ and its intersection with {(n−4)/n}; visualise where the hard n sit in the spectrum.  
   `signature-0433` tags: F12, geometry, spectrum, src:own, gen:integrator

434. **Salez's modular filters (verification to 10¹⁷) as an explicit infinite covering family** [high/cheap] — Salez found new modular equations (identity families) and used them as sieving filters to verify ES to 10¹⁷ (F23, F03, F34). — *First step:* Extract Salez's filter list and compute the density of primes left uncovered by the first k filters for k up to 10³; fit the decay rate.  
   `signature-0434` tags: F23, F03, F34, computation, covering, src:own, gen:integrator

435. **Mihnea–Dumitru (2025) to 10¹⁸ with solution-count statistics — data for signature calibration** [high/cheap] — Their verification reports per-n solution-count distributions (F23, F04). — *First step:* Compare their reported count statistics with M_BM(p) predictions at matching heights.  
   `signature-0435` tags: F23, F04, data, src:own, gen:integrator

436. **Lagrange's four squares: closure (Euler identity) + prime case by pigeonhole and descent — template for F02** [med/cheap] — Four squares reduces to primes by a composition identity; the prime case is done by finding a multiple mp represented (pigeonhole) and descending m to 1. ES reduces to primes by trivial closure; the prime case has no descent. — *First step:* Search for an operation turning ES-type data at mp (e.g. a solution where m divides two of the denominators) into data at m'p with m' < m.  
   `signature-0436` tags: F02, descent, pigeonhole, solved-sibling, src:own, gen:integrator

437. **Davenport–Lewis–Schinzel / Cassels–Pfister: polynomial-identity theorems for sums of squares ↔ Mordell–Schinzel for ES** [med/cheap] — Characterisations of when f(t) is a sum of squares of polynomials (Cassels–Pfister) are the sums-of-squares analogue of 'no polynomial identity covers the square classes' (F09). — *First step:* Re-prove Mordell–Schinzel's ES statement by a Cassels–Pfister-style specialisation at a square point and see what extra hypotheses would allow identities in (a,b) with p = a² + b².  
   `signature-0437` tags: F09, identities, polynomial, src:own, gen:integrator

438. **Feature flip F13 (cubic → quadric): 4/n = 1/x + 1/y is a hyperbola — fully solved by divisors** [high/cheap] — The 2-term equation is a split conic; its solvability is a divisor-in-class condition and fails on a positive-density set. ES adds one variable and becomes a cubic surface with hyperbola fibres (F15). — *First step:* Compute the density of primes failing the 2-term condition for 4/p − 1/x as x ranges over the first K admissible values; plot the decay in K.  
   `signature-0438` tags: F13, F15, feature-flip, src:own, gen:integrator

439. **Feature flip F14: weighted equation 4/p = 1/x + 1/y + 2/z is trivial — symmetry/unit numerators are load-bearing** [high/cheap] — x = (p+3)/4 leaves 12/(p(p+3)) = 3/N with N = p(p+3)/4, and 3/N = 1/N + 2/N. Breaking the unit-numerator symmetry kills the problem. — *First step:* List all weightings (a,b,c) with a+b+c small for which a/x + b/y + c/z = 4/p is trivially solvable; the first non-trivial weighting is a sub-problem ladder.  
   `signature-0439` tags: F14, F12, feature-flip, ladder, src:own, gen:integrator

440. **Feature flip F18: SL₂(ℤ) → SL₂(ℤ[i]) / Bianchi groups — Gaussian words for p ≡ 1 mod 4** [low/medium] — ES's SL₂ form asks for [[a,p],[c,d]] with congruence conditions. Over ℤ[i], p = ππ̄ splits; a Gaussian SL₂ version could split the problem into two conjugate halves. — *First step:* Write the SL₂(ℤ[i]) analogue with entry π and conditions mod (1+i)^k c; check whether norm maps produce ES matrices.  
   `signature-0440` tags: F18, F29, feature-flip, bianchi, src:own, gen:integrator

441. **Feature flip F22: problems with the parity barrier broken by an extra algebraic structure (Friedlander–Iwaniec x² + y⁴, Heath-Brown x³ + 2y³)** [med/medium] — Thin-sequence prime counts became possible when the sequence had bilinear structure (Type II sums). ES's (★) word 4uBC − u − B is bilinear in (u,B) at fixed C. — *First step:* Formulate 'p with R(p) = 0' as a sieve problem and check whether Type II information over (u,B) is available in the FI sense.  
   `signature-0441` tags: F22, bilinear, parity, feature-flip, src:own, gen:integrator

442. **Feature flip F24: sub-problems where the heuristic predicts infinitely many failures (single lines) — calibrate the union** [high/cheap] — Each single ES line (e.g. (★) at bounded C) fails infinitely often (e.g. when 4Cp+1 is prime); (★) overall fails at 14 primes ≤ 10¹⁰; the union never fails ≤ 10⁸. — *First step:* Plot, for unions of the first k lines (ordered by density), the count of failures ≤ X for X = 10⁶..10⁹; fit failure counts ~ X·exp(−c k).  
   `signature-0442` tags: F24, F34, feature-flip, phase-diagram, seen:PHASE_DIAGRAM.md, src:own, gen:integrator

443. **Feature flip F30: thin families proved via algebraic factorisation (Aurifeuillean, Sophie Germain) — catalogue other Aurifeuillean identities** [high/cheap] — ES was proved on 3·2^s + 1, 7·4^s + 9, 63·2^s + 1 using factorisations like 4X⁴ + 1 = (2X²+2X+1)(2X²−2X+1). Aurifeuillean factorisations exist for b^n ± 1 for many b. — *First step:* List Aurifeuillean factorisations (b = 2, 3, 5, 6, 7) and test which p-tied integers 4Cp+1 for p = a·b^s + k factor algebraically.  
   `signature-0443` tags: F30, thin-families, factorisation, seen:FRONTIER.md, src:own, gen:integrator

444. **Feature flip F33: replace reciprocals by squares/cubes — 4/n = Σ 1/x_i² (Egyptian fractions with square denominators, Graham)** [low/cheap] — Graham characterised which rationals are sums of distinct reciprocals of squares; 3-term versions with squares are sparse. ES with squared denominators breaks the hyperbola fibration. — *First step:* Check whether 'a/n = 1/x² + 1/y² + 1/z²' has a known local-global theory; record its obstruction set for small numerators.  
   `signature-0444` tags: F33, F12, feature-flip, src:own, gen:integrator

445. **Feature flip F38: Markoff (quadratic in each variable ⇒ Vieta group) vs ES (multilinear ⇒ no Vieta) — what symmetry group does the ES cubic have?** [med/cheap] — The ES surface 4xyz = n(xy+yz+zx) is multilinear; its automorphisms include S₃ and Cremona-type maps (x ↦ 1/x turns it into a plane 1/x+1/y+1/z linear in reciprocals!). In reciprocal coordinates X = 1/x it is the plane X + Y + Z = 4/n. — *First step:* Determine the group of birational automorphisms of the ES surface over ℚ that preserve positivity and integrality for infinitely many n.  
   `signature-0445` tags: F38, F39, F13, symmetry, feature-flip, src:own, gen:integrator

446. **Feature flip F39: Stern–Brocot / Calkin–Wilf trees enumerate every rational exactly once — is there a tree enumerating ES words with p at a bounded depth?** [med/cheap] — Universality of a tree enumeration is trivial for rationals; ES's word forest (F39) has connectivity results. A tree in which every prime appears within bounded depth would prove ES₅-type statements. — *First step:* Compute the depth of each hard prime in the Stern–Brocot-type tree generated by the ES₅ moves; check bounded depth up to 10⁸.  
   `signature-0446` tags: F39, F17, trees, feature-flip, src:own, gen:integrator

447. **Feature flip F40: Goldbach's exceptional set has a power saving (Montgomery–Vaughan) — why ES's is stuck at exp(−c(log)^{3/4})** [high/cheap] — Montgomery–Vaughan: E_Goldbach(N) ≪ N^{1−δ}. ES: E(N) ≪ N exp(−c(log N)^{3/4}) with 3/4 sharp for CRT sieves (F40). The difference: Goldbach counts are polynomial, ES counts polylog. — *First step:* Write the heuristic exceptional-set size predicted by the Poisson model (∑_n exp(−M(n))) and compare with N^{1−δ}: is a power saving even heuristically true for ES?  
   `signature-0447` tags: F40, F05, feature-flip, exceptional-set, src:own, gen:integrator

448. **Heuristic exceptional-set size for ES and for (★) alone: Σ_n exp(−M(n)) vs. proved bounds** [med/cheap] — Under the Poisson model with mean M(n) ≍ log²n the expected number of failures ≤ N is Σ exp(−c log²n) < ∞, while for single lines it diverges. Shares F24, F05, F40. — *First step:* Compute Σ_{n≤N} exp(−M_BM(n)) numerically for N = 10⁸ with the measured zero-law constant; compare with observed (★) failure counts.  
   `signature-0448` tags: F24, F05, F40, heuristic, src:own, gen:integrator

449. **Positive-proportion pointwise lower bound: R(p) ≥ c·log²p for a positive proportion of primes (second-moment / Paley–Zygmund)** [high/cheap] — From first and second moments of R(p) over p ≤ X, Paley–Zygmund gives R(p) ≥ ½E[R] on a positive proportion (F05w, F04). — *First step:* Check whether the second moment Σ_{p≤X} R(p)² ≪ X log⁴X is available (ET-type divisor-sum bounds) and write the Paley–Zygmund deduction.  
   `signature-0449` tags: F05, F04, second-moment, intermediate-theorem, src:own, gen:integrator

450. **Smallest-solution size statistics: max denominator of the best ES solution vs. p^θ** [high/cheap] — ES witnesses have size ≤ poly(p) (F32). The distribution of the minimal possible max-denominator (or minimal level C) over hard primes is an observable comparable to 'least witness' problems (least nonresidue ≪ log², least prime in AP). — *First step:* For hard primes ≤ 10⁹ record the minimal C with R_C(p) > 0 and minimal max(x,y,z)/p; fit against log p.  
   `signature-0450` tags: F32, F35, least-witness, data, src:own, gen:integrator

451. **Least prime in an arithmetic progression (Linnik's constant) as 'least witness' sibling for the minimal ES level** [med/medium] — Linnik: least prime ≡ a mod q is ≪ q^L. ES: least level C with a witness. Both are 'least witness' statements; Linnik's proof uses zero-density + Deuring–Heilbronn (Siegel zero repulsion) — F21. — *First step:* Formulate a 'log-free zero density' statement for the family {χ_{−4uB}} that would imply min level C ≪ p^ε, and check what is known.  
   `signature-0451` tags: F21, F20, least-witness, zero-density, src:own, gen:integrator

452. **Feature flip F03: n ≡ 0, 2, 3 mod 4 and non-square classes mod 840 are covered by identities — what if the hard classes were non-squares?** [high/cheap] — Mordell's identities cover every class except the six square classes mod 840 (F03, F08, F09). The squares are exactly the classes no polynomial family can reach — the reciprocity obstruction is the reason. — *First step:* For moduli M = 840·ℓ (ℓ ≤ 50), confirm the set of uncovered classes stays 'squares mod M' and record the minimal identity degree needed per class.  
   `signature-0452` tags: F03, F08, F09, feature-flip, src:own, gen:integrator

453. **Feature flip F31: Gauss's three-squares count r₃(n) ~ class number — a lattice count with a class-number main term** [low/cheap] — r₃(n) = 12h(−4n)-type formulas give pointwise lower bounds via Siegel. If any ES count is (even partially) a class number, Siegel-type lower bounds apply (ineffectively). — *First step:* Compute R(p) and Σ_{small D} h(−Dp) for hard primes ≤ 10⁶ and regress; any exact relation would be striking.  
   `signature-0453` tags: F31, class-numbers, feature-flip, src:own, gen:integrator

454. **Feature flip F11 downward: 3/n = 1/x + 1/y fails for p ≡ 1 mod 3 — the 'numerator = terms + 1' ladder starts with a genuine obstruction** [high/cheap] — 3/p as two unit fractions requires a divisor condition that fails for primes p ≡ 1 mod 3 (local-type obstruction), while 4/p in three terms has no local obstruction. m/n in m−1 terms: m = 3 fails, m = 4 is ES. — *First step:* Verify the 3/p criterion and check m = 4 with 2 terms (4/p = 1/x + 1/y ⟺ p ≡ 3 mod 4) to complete the small ladder table.  
   `signature-0454` tags: F11, F12, feature-flip, ladder, src:own, gen:integrator

455. **Feature flip F28: Type III-like solutions for composite n (neither type, e.g. 4/9 = 1/4 + 1/6 + 1/36) — the T1-free channel at squares** [high/cheap] — For n = m², Type I/II vanish (T1) but ES(m²) holds via solutions not of Type I/II (e.g. 4/9 = 1/4 + 1/6 + 1/36). Mixed-type solutions are the channel T1 does not see. — *First step:* Classify all ES solutions of 4/m² for odd m ≤ 101 by gcd pattern with m; check whether every one is a scaled solution of 4/d for d | m, d < m².  
   `signature-0455` tags: F28, F08, feature-flip, squares, src:own, gen:integrator

456. **Feature flip F36: problems where GRH IS known to give the pointwise result (least nonresidue, Artin, Ramanujan's form) — common structure** [med/cheap] — In each GRH-success case a single L-function (or bounded family) controls the event at the given n. ES's event needs a family of size ≍ p of characters χ_{−4uB} at once. — *First step:* For each GRH-success sibling, record the number of L-functions and the conductor range used; tabulate vs ES.  
   `signature-0456` tags: F36, GRH, feature-flip, calibration, src:own, gen:integrator

457. **Feature flip F37: problems where a two-sided asymptotic for the pointwise count IS true (r₄(n) = 8σ*(n))** [med/cheap] — Exact formulas (Jacobi) give two-sided control; ES provably has no two-sided polylog asymptotic (Linnik-type large values). — *First step:* List the exact formulae known for ES-like counts (theta-quotient normal form) and identify which term carries the Linnik large values.  
   `signature-0457` tags: F37, feature-flip, src:own, gen:integrator

458. **Feature flip F27 (cone): 4/n = 1/x + 1/y + 1/z with x,y,z ∈ ℤ_{≠0} and at most one negative — count grows polynomially** [med/cheap] — Allowing one negative denominator turns the problem into an indefinite one with many solutions (count ≫ n^δ). The positive cone cuts it down to polylog. — *First step:* Count signed solutions with |negative denominator| ≤ p^θ for hard p and see how the count decays as θ → 0.  
   `signature-0458` tags: F27, feature-flip, cone, interpolation, src:own, gen:integrator

459. **Hough/Erdős minimum-modulus theorem vs. ES's identities with growing moduli** [med/cheap] — Hough: any covering system with distinct moduli has minimum modulus ≤ 10¹⁶. ES's Mordell identities form a congruence covering of non-square classes; the square classes require infinitely many 'lines' with growing moduli. — *First step:* Apply the BBMST criterion to the list of ES identity classes (moduli ≤ 10⁵) and compute the guaranteed uncovered density.  
   `signature-0459` tags: F03, F34, covering-systems, src:own, gen:integrator

460. **Pratt-certificate analogy: recursive ES certificates via factors of p-tied integers** [low/cheap] — Pratt certificates for primality recurse on factors of p − 1. ES witnesses are divisors of p-tied integers (F10). A recursive scheme: a witness for p from 'witness-like data' for prime factors of 4Cp+1. — *First step:* For hard primes, record which prime factors q of 4Cp+1 'produce' the class −1 (q ≡ −1 mod 4C or products) and whether q's own ES data predict it.  
   `signature-0460` tags: F35, F32, F10, recursion, src:own, gen:integrator

461. **Every n > 1 has a divisor-pair structure: Dirichlet hyperbola method at fixed n as an ES lens** [med/cheap] — Each ES hyperbola fibre (ay − b)(az − b) = b² counts divisors of b² in a class; summing over x is a hyperbola-method sum at fixed n (F15, F10). — *First step:* Write the ES count as Σ_x #{d | (nx)² : d ≡ −nx mod (4x − n), d < nx} and check parity/symmetry under d ↔ (nx)²/d.  
   `signature-0461` tags: F15, F10, hyperbola-method, src:own, gen:integrator

462. **Additive energy of {1/x} and three-fold sums: Bourgain-type sum-product for reciprocals of integers ≤ N** [low/cheap] — How many rationals of height ≤ H lie in {1/x + 1/y + 1/z}? Counting 3-fold reciprocal sums is a sum-product/energy question (F33). — *First step:* Compute |{1/x+1/y+1/z : x,y,z ≤ N}| ∩ {4/n} for N up to 10⁴ and the energy of the reciprocal set.  
   `signature-0462` tags: F33, sum-product, additive-energy, src:own, gen:integrator

463. **Graph-theoretic reformulation: bipartite 'divisor graph' between levels C and primes p; ES ⟺ no isolated prime vertex** [med/cheap] — Make a bipartite graph with an edge (C, p) when R_C(p) > 0. ES ⟺ every hard prime has degree ≥ 1. Degree distribution ≍ Poisson(log²p). — *First step:* Compute the bipartite graph for p ≤ 10⁷, C ≤ 10³; check the isolated-vertex threshold vs. random bipartite graphs with the same degree sequence.  
   `signature-0463` tags: F04, F24, random-graphs, reformulation, src:own, gen:integrator

464. **Sierpiński/Riesel numbers: k·2^n + 1 composite for all n via covering — a 'shifted integer always composite' phenomenon** [med/cheap] — Covering congruences force k·2^n + 1 to be composite for all n. ES needs p-tied integers 4Cp + 1 to be composite WITH a divisor in a class; a covering forcing compositeness is a step in the right direction for a fixed p. — *First step:* For hard primes, find small primes q with q | 4Cp + 1 and q ≡ −1 (mod 4C) for some C < q (i.e. C ≡ −(4p)⁻¹ mod q with the class condition); count such (q, C) pairs with q ≤ log²p.  
   `signature-0464` tags: F10, covering-systems, small-prime-factor, src:own, gen:integrator

465. **Small-prime-factor witnesses: q | 4Cp + 1 with q ≡ −1 (mod 4C) is itself a witness (d = q)** [high/cheap] — If a prime q ≡ −1 (mod 4C) divides 4Cp + 1 then the cofactor is ≡ −1 too (product ≡ 1), so d = q is a (★) witness. For each prime q and each C with 4C | q + 1, q | 4Cp + 1 is a single congruence on p mod q. — *First step:* For each hard prime p ≤ 10⁸, find the least prime q such that some C with 4C | q + 1 satisfies q | 4Cp + 1; study the distribution of that q.  
   `signature-0465` tags: F10, F34, covering, new-angle, src:own, gen:integrator
