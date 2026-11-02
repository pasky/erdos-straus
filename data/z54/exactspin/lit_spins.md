# Literature verification: spin sums and nearby tools

Scope: checked the cited arXiv PDFs/text where available. “UNVERIFIED” means I did not establish the claim from a primary source; it is not a claim of nonexistence.

## 1. Friedlander–Iwaniec–Mazur–Rubin

**Reference:** J. B. Friedlander, H. Iwaniec, B. Mazur, K. Rubin, “The spin of prime ideals,” *Invent. Math.* **193** (2013), 697–749; arXiv:1110.6331 (not 1203.*).

- **Setup / definition (Introduction, equation (1.1)):** K/Q is Galois of degree n≥3 with cyclic Galois group; K is assumed totally real, and totally positive units are exactly squares of units. For odd principal a=(α), α totally positive, and σ∈Gal(K/Q), spin(σ,a)=(α/a^σ), the quadratic residue symbol in K. They usually fix σ a generator. Spin is ±1 when (a,a^σ)=1, otherwise 0.
- **Theorem 1.1 (near-verbatim):** For n≥3, assume Conjecture C_n with exponent δ≤2/n. Then, for prime ideals p principal and Np≤x, “we have” Σ spin(p) ≪ x^(1−ν+ε), where ν=δ/[2n(12n+1)] (the paper’s displayed formula); implied constant depends on ε and K. Sum runs over odd prime ideals of K, not rational primes. For n=3, Burgess gives δ(3)=1/48 and ν=1/10656 unconditionally. Degree>1 prime ideals contribute negligibly; degree-one unramified primes have spin ±1.
- **Conjecture C_n (Section 9, (9.4)):** n≥3, Q≥3, N≤Q^(1/n); for any real nonprincipal Dirichlet character χ modulo q≤Q, any interval (M,M+N], Sχ(M,N)≪Q^(1/n−δ+ε), some δ(n)>0. Any interval is required, not just an initial segment. The paper says Burgess proves C_3 with δ=1/48; their application requires progression versions too.
- **Type I and II in their sieve:** Proposition 6.1 is the Type-I congruence estimate: under C_n, A(x)=Σ_{Na≤x,(a,F)=1,m|a}r(a)spin(a)≪x^(1−δ/(2n)+ε), uniformly for (m,m′F)=1; cubic case unconditional. Proposition 7.1 is the bilinear/Type-II estimate: for totally real Galois K/Q, degree n≥3, B(x,y)≪(x+y)^(1/(6n))(xy)^(1−1/(6n)+ε), x,y≥2. Proposition 5.2 combines generic Type-I exponent ϑ and Type-II exponent θ to give prime-sum exponent ϑθ/(2+θ). (Their term “Type I/II” is discussed via these estimates.)
- **Why n≥3:** in degree 2 the spin sign change is “quite regular”; on a fixed residue class mod 8Δ the spin is constant, so the prime-catching bilinear method fails. In cyclic degree n≥3 a generator σ satisfies σ≠σ⁻¹. More basically the inverse pair is the exceptional Chebotarev-correlated pair; see Koymans–Milovic below. The source explicitly notes the degree-2 failure, rather than stating σ≠σ⁻¹ as the sole reason.

## 2. Koymans–Milovic

### 2a. 16-rank, Q(√−2p)

**Reference:** P. Koymans, D. Milovic, “On the 16-rank of class groups of Q(√−2p) for primes p≡1 (mod 4),” *Int. Math. Res. Not. IMRN* (2019), no. 23, 7406–7427; arXiv:1705.05505.

- **Theorem 1 (near-verbatim):** For prime p≡1 mod 4, set e_p=0 if Cl(−8p) has no element of order 8, e_p=1 if it has an element of order 16, and e_p=−1 otherwise. Then Σ_{p≤X, p≡1 mod 4} e_p ≪ X^(1−1/3200), absolute implied constant. In particular density δ(16)=1/8. The sum is over rational primes p and the class group is that of discriminant −8p.
- This is a Vinogradov-method result with an unconditional power saving as stated. The underlying analytic objects/ideal sums occur in a number-field sieve, but this theorem is not the generic FIMR cyclic-field spin theorem. **Exact spin symbol and numbered Type-I/II propositions: UNVERIFIED from the retrieved text** (the PDF abstract/introduction and theorem verified, but not a complete extraction of its proof). Do not identify it without qualification with a single FIMR spin symbol.

### 2b. A non-cyclic spin theorem

**Reference:** P. Koymans, D. Milovic, “Spins of prime ideals and the negative Pell equation x²−2py²=−1,” *Compositio Math.* (2019); arXiv:1611.10337.

- This is not “Joint distribution of spins.” It explicitly treats M=Q(ζ₈,√(1+i)), a totally complex dihedral (non-cyclic) extension of degree 8, with ring of integers a PID. Fix order-four r∈Gal(M/Q), and the quadratic symbol [α]_r=(r(α)/α). Their ideal spin s_a additionally averages over chosen unit/generator representatives with a finite-modulus weight ψ; see (1.1)–(1.3). Thus it is a generalized, averaged spin, not the original totally-real cyclic definition.
- **Theorem 1:** assuming their Conjecture 1 (short character sums), for prime ideals p⊂O_M, Np≤X, Σ s_p≪X^(1−δ′), δ′=δ/400. Implied constant depends on ψ. Conjecture 1 is a short-sum hypothesis; it is not removed. Their Type I is Proposition 3.3 (under Conjecture 1): Σ_{N(a)≤x,m|a}s_a≪x^(1−δ/4+ε), uniformly m. Type II is Proposition 3.4, unconditional: bilinear sum ≪(M+N)^(1/48)(MN)^(47/48+ε) for coefficients bounded by c_ε N(a)^ε. They combine using FIMR Proposition 5.2.
- This directly answers whether non-cyclic fields are covered: yes, this specific dihedral non-cyclic field and generalized spin, still conditional on the short-character-sum conjecture. It does not establish a theorem for arbitrary non-Galois fields.

### 2c. Joint distribution

**Reference:** P. Koymans, D. Milovic, “Joint distribution of spins,” *Duke Math. J.* **170** (2021), 1723–1755; arXiv:1809.09597.

- **Theorem 1:** K/Q Galois of degree n; if totally real, every totally positive unit in O_K is a square. For a nonempty S⊂Gal(K/Q) satisfying σ∈S⇒σ⁻¹∉S, assume Conjecture C_{|S|n} with δ>0. For each prime ideal p, form the product joint spin sp=∏_{σ∈S}spin(σ,p) (with the paper’s finite-modulus/generator-weighted definition s_a); then Σ_{Np≤X} sp≪X^(1−δ/[54|S|²n(12n+1)]+ε). Implied constant depends on ε,K. The sum is over prime ideals of the fixed Galois field, not rational primes.
- No cyclicity assumption: this is a theorem for Galois fields (with the stated real-unit condition); it does **not** cover arbitrary non-Galois fields. It generalizes FIMR’s cyclic case, while retaining a short-character-sum hypothesis. If S contains both σ and σ⁻¹, their product is instead within Chebotarev’s scope.
- **Theorem 2:** in the totally real case with the same square-positive-units and inverse-free S hypotheses, and C_{tn}, each sign vector in {±1}^t occurs with relative density 2^(−t) among principal prime ideals, for S={σ₁,…,σ_t}.
- Its proof expressly invokes FIMR Prop. 5.2; the Type-I and Type-II estimates are adapted from FIMR rather than presented as separately numbered “Proposition Type I/II” in this paper. **UNVERIFIED:** complete exact proposition numbers for the internal adapted estimates.

## 3. Koymans–Pagano (requested scope only)

**Reference:** P. Koymans, C. Pagano, “On the distribution of Cl(K)[l^∞] for degree l cyclic fields,” *J. Eur. Math. Soc.* **24** (2022), 1189–1283; arXiv:1812.06884.

They average the l-primary class groups over a family of degree-l cyclic number fields (with the ordering/family conditions of the paper); the result establishes the Gerth-predicted distribution under GRH, using Smith’s work. This is a family-of-fields class-group distribution, not a prime-ideal spin sum.

## 4. Kummer sums and large sieves

- **D. R. Heath-Brown, S. J. Patterson**, “The distribution of Kummer sums at prime arguments,” *J. Reine Angew. Math.* **310** (1979), 111–130. No arXiv identifier located. Its main result is uniform distribution (around the unit circle) of normalized cubic Kummer sums at prime arguments (the prime arguments are rational primes in the relevant congruence class); this disproves Kummer’s conjectured behavior. **Exact theorem number and exact error term/hypotheses UNVERIFIED** from primary text in this check.
- **D. R. Heath-Brown**, “Kummer’s conjecture for cubic Gauss sums,” *Israel J. Math.* **120** (2000), 97–124. No arXiv identifier located. **UNVERIFIED:** exact Theorem 2 wording not retrieved. The cubic large sieve repeatedly cited as Heath-Brown [HB2, Theorem 2] has the form, for squarefree Eisenstein integers m,n in the prescribed primary congruence classes, Σ_{Nm≤M}* |Σ_{Nn≤N}* a_n (n/m)_3|² ≪ (M+N+(MN)^(2/3))(MN)^ε Σ|a_n|². Source independently reproducing it: Blomer–Goldmakher–Louvel, arXiv:1112.1650, intro (1.2). Exact constant/dependence not checked in HB original.
- **Quartic:** P. Gao, L. Zhao, “Large sieve inequalities for quartic characters,” arXiv:1101.3646, Theorems 1.1–1.2. Theorem 1.1 (Gaussian quartic symbols): for arbitrary a_n indexed by Z[i], Σ*_{Nm≤M}|Σ*_{Nn≤N}a_n(n/m)_4|²≪_ε(M+N+(MN)^(3/4))(MN)^εΣ*_{Nn≤N}|a_n|²; m,n squarefree and ≡1 mod (1+i)^3. Theorem 1.2 gives a Dirichlet quartic-character large sieve: dyadic Q<q≤2Q, primitive χ mod q with χ⁴=χ₀, χ²≠χ₀, and squarefree m in M<m≤2M; bound (QM)^ε times the minimum of Q^(7/4)+M, Q^(11/8)+Q^(1/2)M, Q^(5/4)+Q^(2/3)M, Q+Q^(1/2)M+M^(17/7), times Σ|a_m|².
- **Blomer–Goldmakher–Louvel:** V. Blomer, L. Goldmakher, B. Louvel, “L-functions with n-th-order twists,” arXiv:1112.1650. Theorem 1.3: K contains μ_n, n≥3; a large sieve for n-th order Hecke characters over squarefree ideals coprime to fixed bad places S, with shape (MN)^ε(M+N+(MN)^(2/3))Σ|λ_b|². The authors say this improves the weaker quartic analogue of Gao–Zhao. Not a direct bound for arbitrary composite-modulus characters on a 2D box.

## 5. Burgess/boxes over quadratic integer rings

- **D. A. Burgess**, “Character sums and primitive roots in finite fields,” *Proc. London Math. Soc.* (3) **17** (1967), 11–30. Classical Burgess bound is for incomplete sums of nonprincipal Dirichlet characters modulo q; general-r statements require q cube-free, with familiar variants for primitive characters. FIMR §9 quotes Sχ(M,N)≪N^(1−1/r)q^((r+1)/(4r²)+ε) and discusses the cube-free qualification; this does not itself prove a rectangular-box estimate in O_K.
- **Mei-Chu Chang**, “Burgess inequality in F_{p²},” *Geom. Funct. Anal.* **19** (2009), 1001–; page end UNVERIFIED. Search located Chang’s paper, but its full theorem/hypotheses were not inspected closely enough for a precise box statement. **UNVERIFIED:** claim that it gives cancellation for every box in Z[i] or Z[ω] with side ≥Q^(1/4+ε); do not infer this from the title/finite-field setting.
- Verified relevant comparison results: Heath-Brown’s cubic Eisenstein large sieve and Gao–Zhao’s Gaussian quartic large sieve above average over moduli and coefficients; they are not pointwise Burgess bounds for one fixed composite conductor χ over a box. I found no primary-source theorem in this check proving the requested general bound for χ∈(O/f)^× with arbitrary composite f, norm Q, on a box of side Q^(1/4+ε).

## 6. Shifted-modulus / shifted-divisor spin searches

Searches for sums over w with modulus depending on w via (−p mod w), shifted divisors w|p+ℓ and symbols (π_ℓ/w)_ℓ, “spins of shifted primes,” and roots of norm equations twisted by power-residue symbols did not locate a verified theorem matching that setup. **UNVERIFIED / no matching result located.**

Nearby but not equivalent: Duke–Friedlander–Iwaniec, “Equidistribution of roots of a quadratic congruence to prime moduli,” *Ann. of Math.* **141** (1995), 423–441, concerns roots of quadratic congruences to prime moduli, with equidistribution established by exponential-sum methods; it is not, on the evidence checked, a theorem for those roots twisted by a varying power-residue symbol. Also their work on roots of quadratic congruences supplies methods used in related sieve contexts, but no claimed extension here.
