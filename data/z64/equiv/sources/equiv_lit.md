# Literature verification for "equivalent formulations" (z64/equiv)

Access date for every URL below: 2026-11-08 (date reported by arXiv API server).
Status: **V** = read in the source itself; **V2** = read only as restated in a later source (named); **NA** = not accessed / not verified.
pdftotext drops super/subscripts and some glyphs; where that happened it is marked [sic: …].

---

## 1. Lorenzini's critical polynomial, d_{A3} = xyz − x − z

### 1a. D. Lorenzini, "The critical polynomial of a graph" — **V** (arXiv v1)
- Published: J. Number Theory 257 (2024) 215–248 (journal ref confirmed by Lorenzini's homepage listing and by Wang–Lu's citation; journal version itself NOT opened — numbering below is from arXiv:2311.06367v1, 10 Nov 2023, only version on arXiv).
- URL: https://arxiv.org/pdf/2311.06367 (also API https://export.arxiv.org/api/query?id_list=2311.06367).
- Definitions: V_f(r) := {f(a_1,…,a_n) | a_i ∈ Z_{≥r}} ∩ Z_{≥0}; d_G = det(Diag(x_1..x_n) − A_G).
- Intro (p.5–6): "The easiest example of such polynomial is d_{A3}(x, y, z) = xyz − x − z, associated with the path A3 on 3 vertices. Computations suggest that the complement of the set V_{A3}(2) in Z≥0 is contained in the set [0, 1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510] (see Proposition 6.3)."
- **Example 6.2(a)**: "Computations indicate that the complement of V_{A3}(2) in Z≥0 is contained in the following set L_{A3} := [0, 1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510]." (Also (b)–(d) give L_{A4}, L_{A5}, L_{A6}.) Followed by: "It is natural to wonder whether d_{A3}(x, y, z) = xyz − x − z takes every non-negative value when x, y, z ≥ 2, except for the values listed in L_{A3}. We have not been able to answer this question beyond the following remarks."
- **Proposition 6.3**: "The set V_{A3}(2) contains:
  (a) All even positive integers n, except possibly those of the form n = 2^m − 2 with m odd or m = 2, 4. [sic: pdftotext shows "2m − 2"]
  (b) All odd positive integers n such that n + 2 is not prime.
  (c) All odd positive integers congruent to 1 modulo 4 and congruent to 2 or 8 modulo 9."
  Proof begins: "We claim that the complement of V_{A3}(2) in Z≥0 consists only of integers n such that (i) either n + 2 is prime or n + 2 is a power of 2, and (ii) such that n + 4 is prime, or n + 4 is not divisible by a prime p ≥ 7 congruent to 3 modulo 4." (z=2: x(2y−1)=n+2; z=4: x(4y−1)=n+4; for even m>4: x=4, z=6, y=(2^{m−3}+1)/3.)
- **Remark 6.4**: "The first values of 2^{2m+1} − 2 are 0, 6, 30, 126, 510, 2046, 8190, . . . . The values 0, 6, and 510 are not achieved by xyz − x − z with x, y, z ≥ 2. The values 30 and 126 are achieved exactly once, with (x, y, z) = (3, 4, 3) and (12, 2, 6), respectively." Remark continues with f = xyz − ax − bz; Prop 6.5 (V_f(2) ⊇ Z_{>0} if a+1 or b+1 not prime, or 4|a and b=1); Example 6.6 (f = xyz−2x−z: complement possibly {0,1,3,7,15}).
- Related general results (V): Theorem 1.1 (V_G(1)=Z≥0; induced subgraph H with 1∈V_H(2) ⇒ V_G(2) ⊇ Z_{>0}); Theorem 1.3 (proved via Theorem 4.2): V_{d_G}(2) dense in Z≥0 for Dynkin, extended Dynkin, stars, cycles, K_n, K(2,n), K(3,n), cone C(A3), …; Lemma 6.1 (first values of V_{An}(2)). Abstract: "We give numerical evidence that in many cases, the complement of V_{dG}(2) in Z≥0 might in fact be finite." "The only examples of graphs where the complement of V_{dG}(2) in Z≥0 is known to be infinite are the banana graphs".
- Own sanity check (not literature): brute force of xyz−x−z, x,y,z ≥ 2, up to 2·10^5 misses exactly [0,1,2,3,5,6,9,11,14,15,35,105,510] — matches L_{A3}.
- Observation (own): for y = k+1, xyz − x − z = (k+1)xz − x − z is exactly the Beck–Robins k-Frobenius number of (x,z) when gcd(x,z)=1 (item 2); and xyz − x − z = det of the path matrix = numerator p of the HJ continued fraction [x,y,z]^− (item 4).

### 1b. T. Wang, L. Lu, "The Critical Polynomials of Simple Connected Graphs" — **V**
- Electron. J. Combin. 33(3) (2026), #P3.80, doi:10.37236/13899. Submitted Feb 22, 2025; accepted May 18, 2026; published Sep 25, 2026.
- URL: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i3p80/pdf/ (no arXiv preprint found).
- Abstract: "Motivated by Lorenzini's exploration of whether the complement of V_{dG}(2) in Z⩾0 might be finite for typical graphs [J. Number Theory 257 (2024) 215–248], we establish that for any simple connected graph G, the subset V_G(2) is dense in Z⩾0. This provides additional evidence in support of Lorenzini's hypothesis that the larger subset V_{dG}(2) might actually be cofinite in Z⩾0."
- Theorem 3: "If T is a tree on n vertices, then V_T(2) is dense in Z⩾0." Theorem 4: "If G ∈ {C_n, K_{k,l}, K_n, C_n^+, C(P_3)}, then V_G(2) is dense in Z⩾0." **Theorem 5**: "If G is connected simple graph, then V_G(2) is dense in Z⩾0." (density = natural density 1; V_G(2) ⊆ V_{dG}(2) is the positive-definite/cyclic-group subset.)
- Method: Dirichlet's theorem on primes in APs + Lemma 11 (union of APs p_i·u − w_i with Σ1/p_i = ∞ ⇒ density 1), Lorenzini's Theorem 4.2 / Lemma 8 for vertex extensions; inductive tree constructions.
- No cofiniteness proved for any graph: concluding remarks: "Although our results show that V_{dG}(2) is dense in Z⩾0 for every connected simple graph G, it remains an open problem whether the complement of V_{dG}(2) in Z⩾0 is finite." Nothing specific about A3 (=P3) or L_{A3}.

### 1c. Other citing work (2024–2026)
- Semantic Scholar citations API for arXiv:2311.06367 (https://api.semanticscholar.org/graph/v1/paper/arXiv:2311.06367/citations) lists: Wang–Lu (above); arXiv 2604.25671 (Arithmetical structures on ladder graphs); 2505.05392 (Generalized chip firing … trees); 2504.08539 (Harmonic morphisms of arithmetical structures); 2503.01913 (Arithmetical structures on fan graphs); 2301.02114; 2206.14836. I fetched the four arXiv 2025–26 PDFs and grepped: each cites Lorenzini only in the bibliography/background; none treats values of d_{A3} or xyz−x−z. arXiv API search "critical polynomial" AND graph: nothing else relevant. Web searches: nothing.
- **Conclusion: no source found proving Lorenzini's A3 question (complement = L_{A3}), cofiniteness, or the restriction to primes (n odd with n+2 prime). Status: open as of 2026-11-08 per Wang–Lu's explicit statement (for cofiniteness in general).**

---

## 2. Generalized Frobenius numbers for two generators

### 2a. M. Beck, S. Robins — primary source — **V** (arXiv)
- arXiv: math/0204037 "An extension of the Frobenius coin-exchange problem" (v1, 2 Apr 2002); published as "A formula related to the Frobenius problem in two dimensions", in Number Theory (New York Seminar 2003), Springer, New York, 2004, pp. 17–23 (publication data V2 from Beck–Kifer ref. 1 and Aliev–Fukshansky–Henk ref. [7]).
- URL: https://arxiv.org/pdf/math/0204037
- "Definition 1 We say that n is k-representable if n can be represented in the form n = m_1a_1 + · · · + m_da_d in exactly k ways." (m_i nonnegative.)
- "Definition 2 g_k(a_1, . . . , a_d) is the smallest integer beyond which every integer is represented more than k times."
- "**Theorem 3** g_k(a, b) = (k + 1)ab − a − b." (with gcd(a,b)=1; proof shows p_{a,b}((k+1)ab−a−b) = k exactly). Also "Theorem 4 Given k ≥ 2, the smallest k-representable integer is ab(k − 1)." "Theorem 5 There are exactly ab − 1 integers which are uniquely representable."

### 2b. M. Beck, C. Kifer, "An extreme family of generalized Frobenius numbers" — **V**
- Integers 11 (2011), A24; arXiv:1005.2692 (v2 27 Jan 2011). URL https://arxiv.org/pdf/1005.2692
- "g_s = g_s(a_1, …, a_k): the largest integer that has exactly s representations… For example, Beck–Robins [1] showed that (3) g_s(a_1, a_2) = (s + 1)a_1a_2 − a_1 − a_2". Defines g*_s = largest integer with at most s representations.
- Theorem 1 (pairwise coprime a_i, Π = ∏a_i, A_j = Π/a_j, Σ = ΣA_j): for t ≥ 1, g_{C(k+t−2,k−1)} = g*_{C(k+t−2,k−1)} = … = g*_{C(k+t−1,k−1)−1} = (k+t−1)Π − Σ. "This theorem extends (3), which is the case k = 2 (where we have A_1 = a_2 and A_2 = a_1)." So for two coprime generators: largest integer with exactly s reps = largest with at most s reps = (s+1)ab − a − b.

### 2c. Aliev–Fukshansky–Henk, "Generalized Frobenius numbers: bounds and average behavior" — **V**
- arXiv:1105.0841 (Acta Arith., per Fukshansky–Schürmann's reference list "to appear"; not checked). Convention: F_s(a) = largest b with #{z ∈ Z^n_{≥0}: ⟨a,z⟩=b} < s. "Beck and Robins [7] … showed … that for n = 2 (1.1) F_s(a) = s a_1 a_2 − (a_1 + a_2)." (Off-by-one shift from 2a/2b: F_s = g*_{s−1}.)
- Also seen: Fukshansky–Schürmann arXiv:1008.4937 (Eur. J. Combin. 32 (2011) 361–368) attributes the s-Frobenius definition to Beck–Robins; Brown et al. arXiv:1001.0207 ("On a generalization of the Frobenius number", exact-j version, cites [BR04]) — abstracts/intros V, no 2-generator formula quoted there.
- Beck–Robins book "Computing the Continuous Discretely" exercise: **NA** (not accessed).

### 2d. Inverse problem
- J. C. Rosales, P. A. García-Sánchez, J. I. García-García, "Every positive integer is the Frobenius number of a numerical semigroup with three generators", Math. Scand. 94 (2004), 5–12 — **V**. URL https://journals.msp.org/mscand/article/download/792/791/823
  - "**Theorem 1.11.** Let g be a positive integer. Then there exist positive integers n_1, n_2, n_3 such that F(n_1, n_2, n_3) = g."
  - Intro: "every odd positive integer g can be expressed as F(2, g + 2) (see 1.1 (i)). However no even positive integers can be expressed as the Frobenius number associated to a pair of relatively prime numbers. This follows easily from Sylvester's formula … F(n_1, n_2) = (n_1 − 1)(n_2 − 1) − 1 and n_1, n_2 are coprime".
  - Lemma 1.1: "(i) If g is odd, then F(2, g + 2) = g. (ii) If 3 ∤ g, then F(3, a, b) = g, where {a, b} = {x ∈ {g + 1, g + 2, g + 3} | 3 ∤ x}. (iii) If g is even and 4 ∤ g, then F(4, g/2 + 2, g/2 + 4) = g." [sic: "∤" lost in extraction, restored from context]
- Related (V2, title/abstract only via Springer/Project Euclid search snippets): García-Sánchez & Rosales, "Every positive integer is the Frobenius number of an irreducible numerical semigroup with at most four generators", Ark. Mat. 42 (2004) 301–306.
- No source found on the inverse problem for generalized (k-)Frobenius numbers of 2 generators (i.e., which N equal (k+1)ab − a − b with gcd(a,b)=1, k ≥ 1). Note: without the gcd condition that set is exactly V_{A3}(2) (item 1).

---

## 3. Log canonical thresholds in 3 variables

### 3a. J. Kollár, "Which powers of holomorphic functions are integrable?" — **V**
- arXiv:0805.0756 (v1, 6 May 2008). URL https://arxiv.org/pdf/0805.0756. HT_n := set of lcts c_0(f) of holomorphic germs in n variables.
- (3.1) HT_1 = {1, 1/2, 1/3, …, 0}.
- (3.2) "HT_2 = { (c_1 + c_2)/(c_1c_2 + a_1c_2 + a_2c_1) : a_i + c_i ≥ max{2, a_{3−i}} } ∪ {0}." (derived in (15.5) from the Newton-polygon edge between (a_1, a_2+c_2) and (a_1+c_1, a_2); "or it is 0 or 1").
- "Although the sets HT_n are not known for n ≥ 3, and a complete listing as in (3.2) may not even be interesting…"
- "Note by contrast, that by (16.1), any rational number between 0 and 1 is the log canonical threshold of some function for some n." (n not fixed — Egyptian fractions.)
- (16.1): c_0(z_1^{a_1} + · · · + z_n^{a_n}) = min{1, 1/a_1 + · · · + 1/a_n}. Prop. 16: c_0(f(x) ⊕ g(y)) = min{1, c_0(f) + c_0(g)}.
- Theorem 15: "(1) The vector (1/c_0(f), …, 1/c_0(f)) is on or above Newton(f). (2) Fix Newton(f) and assume that the coefficients of the monomials in f are general. Then (1/c_0(f), …) is on Newton(f). (3) If n = 2 then one can choose local analytic coordinates (x, y) such that (1/c_0(f), 1/c_0(f)) is on Newton(f)." (15.4): for m ≤ n linearly independent nonnegative exponent vectors whose convex hull contains (1/c,…,1/c), general Σ b_i ∏ x_j^{a_ij} has c_0 = c. "It is possible that in fact these values give all of HT_n, but I know of no reasons why this should be true."
- §9: "The set HT_3 is still not known, but [Kuw99] determined HT_3 ∩ [5/6, 1] and [Pro02] computed all accumulation points of HT_3 that lie in [1/2, 1]." Gap: ε_3 = 1/42 ([Kol94, 5.5.7]).
- Bibliography [Kuw99]: "Takayasu Kuwata, On log canonical thresholds of surfaces in C^3, Tokyo J. Math. 22 (1999) …" (pages 245–251 per other citations).

### 3b. Kuwata — **NA** (paywalled; only V2 via Kollár above)
- T. Kuwata, "On log canonical thresholds of reducible plane curves", Amer. J. Math. 121 (1999) 701–721; "On log canonical thresholds of surfaces in C^3", Tokyo J. Math. 22 (1999) 245–251. Exact statements not read. Prokhorov (below) cites the Amer. J. Math. paper for the explicit description of T_2 and: "Corollary 3.3 ([8]). Any c ∈ T_2 ∩ (1/2, 1] has the following form" (formula garbled in extraction).

### 3c. Yu. Prokhorov — **V** (abstracts/intro)
- "A note on log canonical thresholds", Comm. Algebra 29(9) (2001) 3961–3970, arXiv:math/0102090: "the largest accumulation point of the set T_3 of all three-dimensional log canonical thresholds c(X,F) is 5/6."
- "On log canonical thresholds, II", Comm. Algebra 30(12) (2002) 5809–5823, arXiv:math/0104251: Theorem 1.2: ∂T_3 ∩ [1/2, 1] = T_2 ∩ [1/2, 1] = {1/2 + 1/n | n ∈ Z, n ≥ 3}. (Note T_d there allows singular lc X, so T_3 ⊋ HT_3 in general.)
- McKernan–Prokhorov, "Threefold thresholds", Manuscripta Math. 114 (2004) (arXiv:math/0304152): Accumulation conjecture in dim 3 (V2 via Kollár).

### 3d. Answer to the question asked
- **No source states that every rational in (0,1] lies in HT_3** (Kollár explicitly: HT_n unknown for n ≥ 3; "any rational … for some n").
- But for 4/n the question is elementary (own derivation from Kollár (3.2)/(15.5), V-sourced formula): take c_1 = 1, c_2 = 3: value 4/(3 + 3a_1 + a_2) with constraints a_2 ≤ a_1 + 1, a_1 ≤ a_2 + 3, a_1 ≥ 1. With a_1 = a ≥ 1, a_2 ∈ [max(0,a−3), a+1] this hits every n ≥ 6. Concretely
  **lct_0( x^a y^b (x + y^3) ) = 4/(3a + b + 3)** when b ≤ a+1 and a ≤ b+3 (checked independently: three blow-ups give divisors with weights (1,1),(2,1),(3,1), ratios 2/(a+b+1), 3/(2a+b+2), 4/(3a+b+3); the last is minimal and ≤ 1/a, 1/b under those inequalities).
  So 4/n ∈ HT_2 ⊂ HT_3 for all n ≥ 6 (a reducible plane curve; Newton-nondegenerate binomial x^a y^{b+3} + x^{a+1} y^b), and 4/5 = 1/2+1/5+1/10 ∈ HT_3 via (16.1), 4/4 = 1. Brute-force search over Kollár's formula: 4/5 ∉ HT_2 (consistent with HT_2 ∩ (1/2,1] = {1/2+1/m}); many other rationals ≤ 5/6 (e.g. 5/7, 7/9, 6/13, 8/13) also not found in HT_2.
  ⇒ "4/n is an lct in 3 variables" carries no Erdős–Straus content unless restricted to diagonal (Brieskorn–Pham) polynomials x^a+y^b+z^c, where (16.1) gives exactly 1/a+1/b+1/c.

---

## 4. Lens spaces bounding negative-definite 4-manifolds with small b_2

Standard fact (V, Aceto–McCoy–Park §1 and Fung–Park §1): L(p,q) (= −p/q surgery on the unknot, p>q>0) bounds the canonical negative-definite linear plumbing X(p,q) with weights −a_1,…,−a_n, a_i ≥ 2, p/q = [a_1,…,a_n]^− (HJ continued fraction); b_2(X(p,q)) = n. Also "−L(p,q) … is orientation-preservingly diffeomorphic to L(p,p−q)"; blowing up gives Q_X ⊕ ⟨−1⟩^m fillings. Hence p = det of the path matrix: n=2: p = a_1a_2 − 1; n=3: p = a_1a_2a_3 − a_1 − a_3 (= Lorenzini's d_{A3}).

### 4a. P. Lisca, "Lens spaces, rational balls and the ribbon conjecture" — **V**
- Geom. Topol. 11 (2007) 429–472; arXiv:math/0701610. URL https://arxiv.org/pdf/math/0701610
- "Theorem 1.2 Let p > q > 0 be coprime integers. Then, the following statements are equivalent: (1) The lens space L(p, q) smoothly bounds a rational homology ball. (2) There exist: (a) A surface with boundary Σ, homeomorphic to a disk if p is odd and to the disjoint union of a disk and a Möbius band if p is even; (b) A ribbon immersion i : Σ → S^3 with i(∂Σ) = K(p, q). (3) p/q belongs to R."
- Definition 1.1: R = smallest subset of Q_{>0} closed under f(p/q) = p/(p−q), g(p/q) = p/q' (qq' ≡ 1 mod p), containing p/q with p = m^2 and q of type "(1) mk ± 1 with m > k > 0 and (m, k) = 1; (2) d(m ± 1), where d > 1 divides 2m ∓ 1; (3) d(m ± 1), where d > 1 is odd and divides m ± 1."
- Corollary 1.3: ribbon conjecture for 2-bridge knots. Sequel (V2 via Fung–Park refs): Lisca, "Sums of lens spaces bounding rational balls", AGT 7 (2007) 2141–2164.

### 4b. Aceto–McCoy–Park, "Definite fillings of lens spaces" — **V**
- J. Differential Geom. 131(1) (2025) 1–41 (ref. V2 via Fung–Park bibliography); arXiv:2208.02586v2. URL https://arxiv.org/pdf/2208.02586
- Theorem 1.1: for L = #L(p_i,q_i), TFAE: "(i) every smooth negative-definite filling X of L satisfies b_2(X) ≥ b_2(♮_i X(p_i, q_i)); (ii) every smooth negative-definite filling X of L satisfies Q_X ≅ Q_{♮X(p_i,q_i)} ⊕ ⟨−1⟩^n for some integer n ≥ 0; (iii) the canonical negative-definite linear plumbing graph associated to L does not contain any of the following configurations as an induced subgraph: (a) (−4) (b) (−5,−2) (c) (−6,−2,−2) (d) (−2)(−2) [non-adjacent pair] (e) (−3,−2,−2) (f) (−3)(−3) … (g) (−3,−2,−3) (h) (−3,−2,−2,−3) (i) (−3,−5,−3,−2) (j) (−2,−2,−3,−5) [weights as printed; induced-subgraph sense, Remark 1.2]; (iv) ♮X(p_i,q_i) does not contain a smooth embedded submanifold diffeomorphic to X(4, 1), X(9, 2), X(16, 3), or X(64, 23)."
- "Those L which admit a filling with b_2(X) = 0 were classified by Lisca [Lis07a, Lis07b]." "Of course, for a general lens space establishing the size of the b_2-minimal negative-definite filling is highly nontrivial."
- Theorem 1.6: "For any positive integer k, there is a lens space L_k such that if X is a negative-definite filling of L_k or −L_k, then b_2(X) ≥ k."

### 4c. A. T. H. Fung, J. Park, "Forbidden configurations and definite fillings of lens spaces" — **V** (arXiv:2601.11083v1, 16 Jan 2026)
- Theorem A: for each k, a finite set S_k of minimal forbidden configurations characterises "Property X_k" (Q_{♮X(p_i,p_i−q_i)} does not embed in (Z^{n_k}, −Id)), which implies b_2(X) ≥ b_2(♮X(p_i,q_i)) − (k−1) for all negative-definite fillings. Theorem B (k=2, |S_2| = 17): TFAE "(i) every smooth negative-definite filling X of L satisfies b_2(X) ≥ b_2(♮_i X(p_i, q_i)) − 1; (ii) … Q_X ≅ Q_{♮X(p_i,q_i)} ⊕ ⟨−1⟩^m or Q_X ≅ Q_{♮X̃(p_i,q_i)} ⊕ ⟨−1⟩^m …". They note the analogue of (c)⇒(b) fails for k = 8.

### 4d. W. Jo, J. Park, K. Park, "On lens spaces bounding smooth 4-manifolds with b_2 = 1" — **V** (arXiv:2410.22719v3, 30 Sep 2026; published Algebr. Geom. Topol. 26 (2026) no. 7 per msp.org URL in search results, not opened)
- Question 1.1 (b_2 = b_2^+ = 1, single 0- and 2-handle) "is equivalent to the lens space realization problem [Gre13]" — resolved by Greene (J. Greene, "The lens space realization problem", Ann. of Math. 177 (2013) — V2 via this paper; Greene: if a lens space is positive integer surgery on a knot in S^3, it is such surgery on a Berge knot).
- Questions 1.2 (π_1 = 1) and 1.3 (b_1 = 0) open in general; topologically: "L(p, q) bounds a simply-connected, topological 4-manifold with b_2 = b_2^+ = 1 if and only if −q is a quadratic residue modulo p [Boy86]."
- Theorems 1.4/1.5: infinite families in L_{π1} \ L_{Dehn} and L_{b1} \ L_{π1} (continued fractions [2,2,2,n+2,m,[2]^m] and [m+2,[2]^{m+2},n+2,[2]^{m+2},m+2]).

### 4e. Owens–Strle
- "A characterisation of the Z^n ⊕ Z(δ) lattice and definite nonunimodular intersection forms", arXiv:0802.1495 (Amer. J. Math., not checked) — **V** abstract/Theorem 1: "Let Q be an integral positive-definite symmetric bilinear form of rank n and determinant δ. Then there exists a characteristic covector ξ for Q with ξ^2 ≤ n − 1 + 1/δ if δ is odd, n − 1 if δ is even; moreover the inequality is strict unless Q = (n − 1)⟨1⟩ ⊕ ⟨δ⟩." Application: small positive surgeries on torus knots do not bound negative-definite manifolds. No lens-space b_2 characterisation found there.
- "Immersed disks, slicing numbers and concordance unknotting numbers", arXiv:1311.6702 — abstract V only; not about lens-space b_2.
- "Rational homology spheres and four-ball genus" (arXiv:math/0308073) — NA beyond title.

### 4f. Conclusion
- b_2 = 0: Lisca (complete). b_2 = 1 via single 2-handle: Greene (complete, lattice/changemaker). b_2 = 1 general, b_2 = 2, 3: **no complete characterisation found**; Aceto–McCoy–Park / Fung–Park characterise when the canonical plumbing is b_2-minimal (or minimal up to 1), which for L(p,q) with HJ length 3 (p = a_1a_2a_3 − a_1 − a_3) gives "minimal negative-definite b_2 = 3" iff no forbidden induced subgraph.
