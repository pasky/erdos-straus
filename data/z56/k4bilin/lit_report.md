# Literature verification report: k4bilin (shifted convolutions in APs, Harman's sieve, r-correlations, BFI-type results)

Legend: **VERIFIED** = I read the statement in the PDF/primary text. **VERIFIED-2nd** = read in a faithful secondary restatement (named). **ABSTRACT-ONLY**. **UNVERIFIED**.
Where I compute ranges from a stated theorem, I mark it **[my derivation]**.

---

## Q1. Level of distribution for the binary additive divisor problem / r(n)r(n+h) in APs

### 1a. Grimmelt–Merikoski, "Twisted correlations of the divisor function via discrete averages of SL2(R) Poincaré series", arXiv:2404.08502. **VERIFIED** (pp. 3–4). This is the current best result.
- **Theorem 1.2** (Divisor correlations with a periodic weight). Let h, q ∈ Z, q square-free, gcd(h,q)=1; X, η>0, −X/2 ≤ h ≤ X^{1+η}; G smooth supported on [1,2] with G^{(j)} ≪ X^{jη}; t: Z/qZ → C any function. Then
  Σ_n G(n/X) d(n) d(n+h) t(n) = Σ_{r mod q} t(r) ω(r,h;q) ∫ G(u/X) P_h(log u, log(u+h)) du + O( X^{1/2+O(η)} q^{1/2} ‖t‖_2 (|h|^θ + (X/q)^θ) ),
  ‖t‖_2² = Σ_r |t(r)|², θ = 7/64; ω(r,h;p) = (p−1)/(p(p+1)) if r(r+h)≢0, (2p−1)/(p(p+1)) if r(r+h)≡0 (mod p).
- **Corollary 1.3** (fixed progression n ≡ r mod q): error O(X^{1/2+O(η)} q^{1/2}(|h|^θ+(X/q)^θ)). Authors: "the first result of this type that goes beyond the range q ≤ X^{1/6−ε} that can be obtained by opening one of the divisor functions and using the fact that d(n) is well distributed in arithmetic progressions to moduli at most X^{2/3−ε}." Unconditionally non-trivial for **q ≤ X^{(1−2θ)/(3−2θ)−ε} (≥ X^{0.281…})** when |h| ≤ X/q; q ≤ X^{1/3−ε}|h|^{−2θ/3} for X/q<|h|≤X^{1+η}. Under Selberg (θ=0): **q ≤ X^{1/3−ε}**.
- **Corollary 1.4** (sum over all residues r mod q of |error|): bound X^{1/2+O(η)} q (|h|^θ+(X/q)^θ); non-trivial for **q ≤ X^{(1−2θ)/(2−2θ)−ε} (≥ X^{0.438…})**; X^{1/2−ε} under Selberg.
- Not found anywhere: an average over moduli q ≤ X^ϑ with a *fixed* residue (Bombieri–Vinogradov-type) for d(n)d(n+h) beyond the above. Corollary 1.4 is an average over residues for a fixed q, not over q.

### 1b. Topacogullari, "On a certain additive divisor problem", arXiv:1512.05770. **VERIFIED** (p. 2).
- **Theorem 1.2**: r0 := min{(r1, r2^∞), (r2, r1^∞)}, h := r1 f2 − r2 f1 ≠ 0. Assume f1 ≪ (r1x)^{1−ε}, f2 ≪ (r2x)^{1−ε}, (r0r1r2,h)h ≪ r0^{1/3}(r1r2)^{5/3}x^{1/3−ε}. Then
  Σ_{x/2<n≤x} d(r1n+f1) d(r2n+f2) = x P(log x) + O( (r0r1r2,h)^θ r0^{2/3+θ} (r1r2)^{1/3} x^{2/3+ε} ).
  (Theorem 1.1 is the smooth version: error O(r0 (r2x1)^{1/2+θ+ε}).)
- **[my derivation]** Taking r1=r2=q (so r0=q) encodes m ≡ f (mod q), m ≤ X with X = qx. The error becomes ≈ q^{5/3+θ} x^{2/3} = q^{1+θ}X^{2/3} against main term ≈ X/q. So non-trivial only for q ≲ X^{1/(6+3θ)} (≈ X^{0.16} with θ=7/64). That is *below* the trivial X^{1/6} range quoted by Grimmelt–Merikoski. Topacogullari therefore doesn't help with large q.

### 1c. Drappeau, "Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method", arXiv:1504.05549 (Proc. LMS 2017). **VERIFIED** (abstract + Thm 5.1).
- It does **not** treat d(n)d(n+h) in APs. Its results are: Thm 1.1 (power saving for Σ_{p≤x} τ(p−1), assuming GRH); Thm 1.2 and Cor. 1.3 (unconditional, isolating the Siegel-zero contribution); Thm 1.5 (power saving for Σ τ_k(n)τ(n+1)); and Thm 2.1, a quintilinear Kloosterman bound with congruence conditions that generalises DI82 Thm 12.
- The relevant equidistribution input is **Theorem 5.1**. Take x = MN, x^{1/4} ≤ Q ≤ x^{1/2+δ}, x^η ≤ N ≤ Q^{2/3−η}, R, |a1|, |a2| ≤ x^δ. Then Σ_{Q<q≤2Q,(q,a1a2)=1} Σ_{m,n} α_m β_n u_R(mn a1 a2; q) ≪ x(log x)^{O(1)} R^{−1}, where u_R subtracts characters of conductor ≤ R. This is a *fixed* residue (a1a2) and *binary convolution* result, with level x^{1/2+δ}.

### 1d. r(n) analogues
- **Friedlander–Iwaniec, "Hyperbolic prime number theorem", Acta Math. 202 (2009) 1–19, DOI 10.1007/s11511-009-0033-z.** **VERIFIED** (PDF).
  - **Lemma 4.1** (Smith): for (a,q)=1, Σ_{m≤x, m≡a(q)} r(m) = (πx/q)Π_{p|q}(1−χ(p)/p) + O(q^{−1/2}x^{2/3+ε}) when q≢0 (mod 4). The main term is multiplied by 1+χ(a) when 4|q. FI: "this gives the asymptotic within the range q < x^{2/3−ε}."
  - **Lemma 4.2**: for d odd, Σ_{n≤x, n≡3(4), n≡0(d)} r(n−2)r(n+2) = 8g(d)x + O(x^{11/12+ε}), with g(d) = d^{−1}Π_{p|d}(p−χ(p))/(p+χ(p)). §5 then says: "this sequence has a level of distribution D = x^{1/12−2ε}."
- **Sedunova, "On the hyperbolic prime number theorem", arXiv:2609.28200 (Sept 2026).** **VERIFIED** (PDF).
  - **Lemma 2** (a refinement of FI Lemma 4.2): error O(d^{−1/2}x^{11/12+ε} + x^{1/2+ε}). This gives level of distribution **x^{1/6−ε}** for r(n−2)r(n+2) with the congruence on the shared variable n.
  - **Remark 1**: "The exponent 1/6 … comes from the individual error term O(d^{−1/2}x^{11/12+ε}) in Lemma 2, which in turn comes from the summation of terms coming from Lemma 1 over the moduli 4dk with k<√x."
  - "Hypothesis R(θ)" (level x^θ for r(n−2)r(n+2)) is stated as a **conjecture**. Expected for all θ<1.
- I found **no** published result giving r(n)r(n+h) in APs to modulus q with a spectral-quality range (like GM's X^{0.28}).
  - MathOverflow 470358 (2024, secondary): P. Humphries and D. Lowry-Duda both comment that they have not seen even fixed-q asymptotics for Σ_{n≡a(q)} r(n)r(n+1) in the literature.
  - Blomer IMRN 2004 and Deshouillers–Iwaniec 1982: **UNVERIFIED** (not read).

---

## Q2. Harman's sieve, "Fundamental Theorem" (Prime-Detecting Sieves, Thm 3.1)

I could not access the book. **VERIFIED-2nd** from J. Teräväinen's notes (jonismathnotes.blogspot.com/2015/01/harmans-sieve.html, "Theorem 3 (Harman's sieve)"); the proof sketch there matches Harman's argument.
- **Statement.** Let A, B ⊂ [1,x] be finite sets of positive integers. Suppose that for all sequences a_n, b_n with |a_n|, |b_n| ≤ τ(n):
  - (i) Type I: Σ_{m≤M, mn∈A} a_m = λ Σ_{m≤M, mn∈B} a_m + O(Y);
  - (ii) Type II: Σ_{x^α<m<x^{α+β}, mn∈A} a_m b_n = λ Σ_{x^α<m<x^{α+β}, mn∈B} a_m b_n + O(Y);
  - for some λ, Y, α, β > 0 with β ≤ 1/2.
- Let |c_r| ≤ 1. Suppose **M > x^α**, 2R < min{M, x^{1−α}}, and further M > x^{1−α} if 2R > x^{α+β}. Then
  Σ_{r∼R} c_r S(A_r, P, x^β) = λ Σ_{r∼R} c_r S(B_r, P, x^β) + O(Y log³x).
  In particular (R=1): S(A, x^β) = λ S(B, x^β) + O(Y log³x).
- **Prime count.** β = 1/2 gives S(A, x^{1/2}) = primes in A∩(x^{1/2},x]. So the requirements are Type I to level M > x^α plus Type II for x^α < m < x^{α+1/2}.
  **[my derivation]** Since Type II is symmetric in m ↔ n = x/m, this is Type II for every factorisation with both factors ≥ x^α.
- **Typical use when Type II is too narrow** (e.g. Merikoski 2112.03617, Type II only for X^{1/4+η} ≪ N ≪ X^{1/3−η}, Prop. 12): Buchstab-decompose further and *discard* the non-asymptotic pieces. The result is a lower bound of the right order, not an asymptotic.

---

## Q3. Linear correlations of r(n) / τ(n)

- **Heath-Brown, "Linear relations amongst sums of two squares"** (LMS Lecture Note 303, 2003; ORA preprint). **VERIFIED** (preprint PDF).
  - **Theorem 1**: four binary linear forms L1..L4 in **2 variables**, satisfying NC1 (no two proportional; R = X·R^{(0)} convex, L_i > 0 on R^{(0)}; all L_i ≡ x1 mod 4). Then S = Σ_{x∈R, x1≡1(4)} Π r(L_i(x)) = 4π⁴ meas(R) Π_{p≥3} σ_p + O(X²(log X)^{−η/2}(log log X)^{15/4}), with η = 1 − (1+log log 2)/log 2 = 0.08607….
  - Theorem 2 gives the local–global version under NC2.
- **Matthiesen, "Linear correlations amongst numbers represented by positive definite binary quadratic forms"**, arXiv:1106.4690 (Acta Arith. 2012). **VERIFIED**.
  - **Theorem 1.1**: f1..ft primitive positive definite binary quadratic forms; Ψ: Z^d → Z^t affine-linear with **no two ψ_i, ψ_j affinely dependent**, linear coefficients bounded; K ⊂ [−N,N]^d convex with Ψ(K) ⊂ [0,N]^t. Then Σ_{n∈Z^d∩K} Π R_{f_i}(ψ_i(n)) = β_∞ Π_p β_p + o(N^d). There is no explicit error term.
  - The authors stress that the "infinite complexity" case E_{n≤N} R_f(n+a1)…R_f(n+a_d) is out of reach.
- **Matthiesen, "Correlations of representation functions of binary quadratic forms"**, arXiv:1205.4145. **VERIFIED**. Theorem 1.1 is the same statement for primitive *irreducible* forms (definite or indefinite), with o(N^d).
- **Matthiesen, "Correlations of the divisor function"**, arXiv:1011.0019 (Proc. LMS 2012). **VERIFIED**. The **Main Theorem** has the same shape for τ̃ (linear parts pairwise linearly independent), with o_{t,d,L}(N^d).
- **Dimension.** In one variable (d=1) any two affine forms are affinely dependent, so all these results need **d ≥ 2** genuinely independent long variables. Equivalently, they need "finite complexity".
- **One-variable triple correlations**:
  - **Blomer, "On triple correlations of divisor functions"**, arXiv:1512.03278 (BLMS 2017). **VERIFIED**.
    - He calls D_h(N) = Σ_{n≤N} τ(n)τ(n−h)τ(n+h) "an extremely interesting and challenging open problem".
    - **Corollary 1**: for 1 ≤ H ≤ N/3 and k ≥ 2, Σ_h W(h/H) Σ_{N≤n≤2N} τ_k(n)τ(n+h)τ(n−h) = Ŵ(1) H N Q_{k+1}(log N) + O(N^ε(H² + N H^{1/2} + N^{3/2}H^{−1/2} + H N^{1−1/(k+2)})). This is non-trivial for **N^{1/3+ε} ≤ H ≤ N^{1−ε}**.
    - Browning's earlier average (Browning, "The divisor problem for binary cubic forms", arXiv:1006.3476, as quoted by Blomer) needed H ≥ N^{3/4+ε}.
  - **No** asymptotic is known for any individual-shift triple correlation Σ τ(n)τ(n+1)τ(n+2) or Σ r(a1m+b1) r(a2m+b2) r(a3m+b3), as far as I found.
  - **Binary r(n)r(n+h):** this is classical (Iwaniec–Kowalski Cor. 15.12, per MO 470358; **UNVERIFIED** in IK).

---

## Q4. Named recent works

**(a) Green–Sawhney, "Primes of the form p² + nq²"**, arXiv:2410.04189. **VERIFIED**.
- **Theorem 1.1**: for n ≡ 0 or 4 (mod 6), W ∈ C_0^∞(R²): Σ_{x,y} Λ(x)Λ(y)Λ(x²+ny²) W(x/N, y/N) = κ_n N² ∫W + O_{W,n}(N²(log log N)²/log N). This covers the n=4 Friedlander–Iwaniec "Gaussian primes conjecture".
- **Inputs:** Type I/II sums in Q(√−n) via a Duke–Friedlander–Iwaniec sieve, plus a dimension-3 upper-bound sieve. Type I is obtained up to X^{1/2−o(1)} (§6 title "Type I up to X^{1/2}/(log X)^A") and Type II for levels between X^{o(1)} and X^{1/2−o(1)}.
- Both are controlled by Gowers norms of f = Λ − Λ_Cramér. The tools are concatenation theorems (Kuca, Kravitz–Kuca–Leng) and Leng's/Leng–Sah–Sawhney quasipolynomial inverse theorem.
- The authors note that "the Type I range is just barely enough".

**(b) Merikoski.**
- **"On the largest prime factor of n²+1"**, arXiv:1908.08816. **VERIFIED**. **Theorem 1**: P⁺(n²+1) > n^{1.279} infinitely often; 1.312 under Selberg. The method is a new Type II estimate via Deshouillers–Iwaniec bounds plus Harman's sieve.
- **Grimmelt–Merikoski, arXiv:2505.00493** (ABSTRACT-ONLY): P⁺(n²+h) ≥ n^{1.312} unconditionally.
- **"The polynomials X²+(Y²+1)² and X²+(Y³+Z³)² also capture their primes"**, arXiv:2112.03617. **VERIFIED**.
  - **Theorem 1**: Σ_{p≤X} Σ_{p=a²+(b²+1)²} 1 ≍ X^{3/4}/log X.
  - **Theorem 2**: the analogous result for a²+(c³+d³)² (c,d>0), ≍ X^{5/6}/log X.
  - **Theorem 3**: incomplete norm forms.
  - **Inputs:** Type I for D ≤ X^{3/4−η}; Type II (Prop. 12) only for X^{1/4+η} ≪ N1 ≪ X^{1/3−η} (Thm 1) and X^{1/6+η} ≪ N2 ≪ X^{2/9−η} (Thm 2), via the Weil bound. This is "too narrow for an asymptotic", so Harman's sieve gives a lower bound only.
- **Merikoski, "On Gaussian primes in sparse sets"**, arXiv:2302.11331 (ABSTRACT-ONLY): primes a²+b² with b ∈ B, |B∩[1,Y]| ≫ Y^{1−δ}.
- **Grimmelt–Merikoski–Pandey–Pascadi, "Primes and the Möbius function over quadratic polynomials"**, arXiv:2610.41356. **VERIFIED**.
  - **Thm 1.1**: Σ_{n²+h≤X} Λ(n²+h) = (1+O(ν)) S_h X^{1/2} for all but ≪ H/(log X)^C of h ≤ H = X^{1/2−ν}.
  - **Thm 1.2**: a lower bound of 0.098 S_h(X−h)^{1/2} for almost all h, for X^{2/5} ≤ H ≤ X/2. This uses Harman's sieve.

**(c) Lichtman.** No paper on primes with sums-of-two-squares conditions found. **ABSTRACT-ONLY** for his relevant level-of-distribution papers:
- arXiv:2211.09641: quadrilinear mean-value theorem for primes to moduli up to x^{17/32} (fixed residue). P⁺(p−1) ≤ p^{0.2844} infinitely often.
- arXiv:2309.08522: level 66/107 ≈ 0.617 with triply well-factorable weights; 5/8 under Selberg.

**(d)**
- **Teräväinen, "Almost primes in almost all short intervals"**, arXiv:1510.06005 (ABSTRACT-ONLY): almost all [x, x+log^{1+ε}x] contain E₃ numbers, and almost all [x, x+log^{3.51}x] contain E₂ numbers.
- **Matomäki–Teräväinen, "Almost primes in almost all short intervals II"**, arXiv:2207.05038 (ABSTRACT-ONLY): (x, x+(log x)^{2.1}] contains E₂ numbers for almost all x. It uses a new Type II estimate built on Heath-Brown's mean value theorem for sparse Dirichlet polynomials.
- **"Almost primes in almost all very short intervals"** is by **Matomäki alone**, arXiv:2012.11565 (ABSTRACT-ONLY): if h → ∞, almost all (x−h log X, x] contain a P₂. It uses Richert's weighted sieve with Deshouillers–Iwaniec Kloosterman input.

**(e) Primes with sums-of-two-squares conditions.**
- **FI 2009 Theorem 5 (unconditional). VERIFIED.** T(x) = Σ_{p≤x} r(p−4) log p = πx Π_p(1+χ(p)/(p(p−1))) + O(x(log x)^{−A}). The proof expands r(p−4) = 8Σ_{k<√p} χ(k) + …, so it needs primes p ≡ 4 (mod k) for k ≤ √x. That is handled by [BFI, Theorem 9] (see Q5).
- **FI 2009 Theorems 2–4.**
  - Σ_n r(n−2)r(n+2)Λ(n) ≍ x (i.e. π_Γ(x) ≍ x/log x) **only under A(θ) "for some θ less than 1 but sufficiently close to 1"**. The upper bound is unconditional.
  - The lower bound uses the **semilinear sieve** with b(n) = 1 iff all prime factors ≡ 1 (mod 4). The remainder R_δ(x) = Σ_{k≤√x} Σ_{d≤D} E_max(x, 4δdk), with D = x^{θ−1/2−ϑ−ε}.
- **Sedunova 2026 (arXiv:2609.28200). VERIFIED.**
  - **Thm 1**: square-free distances s_Γ(x) = 6Cx + O(x^{11/12+ε}).
  - **Thm 2**: s_Γ^{(7)}(x) ≫ x/log x unconditionally (ω(n) ≤ 7).
  - **Thm 3**: under R(θ), ω(n) ≤ ⌊2/θ⌋. She states the prime case remains conditional.
- **Shparlinski–Xiao, arXiv:2609.21460** (ABSTRACT-ONLY): sup-norm ordering, square-free with ≤ 9 prime factors.
- **Nath–Xie, "Almost primes and primes that are sums of two squares plus 1"**, arXiv:2501.16723. **VERIFIED**.
  - **Theorem 1.1**: #{p ≤ x : p = m²+n²+1, Ω(p+2) ≤ 9} ≫ x/(log x)^{5/2}. This is a vector sieve (semilinear × linear).
  - Remark 1.1: Ω(p+2) ≤ 3 under a version of EH.
- **Teräväinen, arXiv:1611.08585** (ABSTRACT-ONLY): binary/ternary Goldbach with primes x²+y²+1.
- **No unconditional hyperbolic PNT (prime case) found.** I also found no unconditional result giving infinitely many primes p with p+a and p+b *both* sums of two squares.

---

## Q5. BFI-type results with residue depending on the factorisation / roots of a polynomial

- **Maynard, "Primes in APs to large moduli III: Uniform residue classes"**, arXiv:2006.08250. **VERIFIED**. These results are exactly "residue may depend on the modulus, beyond x^{1/2}".
  - **Thm 1.1**: Q1 ≤ x^{1/10−3δ}/(log x)^C and Q2 ≤ x^{4/10+4δ}(log x)^C. Then Σ_{q1~Q1} Σ_{q2~Q2} sup_{(a,q1q2)=1} |π(x;q1q2,a) − π(x)/φ(q1q2)| ≪ δπ(x) + x(log log x)²/(log x)². This is a weak, O(δ), saving.
  - **Thm 1.2**: 0<δ<1/1000, Q1Q2Q3 = x^{1/2+δ}, x^{40δ} < Q2 < x^{1/20−7δ}, x^{1/10+12δ}/Q2 < Q3 < x^{1/10−4δ}/Q2^{3/5}. Then Σ_{q1≤Q1} Σ_{q2≤Q2} sup_{(b,q1q2)=1} Σ_{q3≤Q3} sup_{(a,q1q2q3)=1, a≡b (q1q2)} |π(x;q1q2q3,a) − π(x)/φ(q1q2q3)| ≪ x/(log x)^A. Here the residue mod q3 is completely free; only the residue mod q1q2 must not depend on q3.
  - **Thm 1.3**: there is a minorant ρ ≤ 1_P with Σρ ≥ π(x)/8 that is equidistributed with **sup over all residues** for moduli q1q2, Q1 ∈ [x^{2/5+5δ}, x^{3/7}], Q2 = x^{1/2+δ}/Q1, with error x/(log x)^A.
  - So a residue "a1 mod q1, a2 mod q2 with a1 ≠ a2 fixed" *is* covered at level x^{1/2+δ}, δ small, when q has a conveniently sized factor (Thms 1.2/1.3).
- **Zhang / Polymath (MPZ)**, **VERIFIED-2nd** via Tao's reading-seminar post (2013), which restates Zhang's Theorem 2.
  - Statement: Σ_{d<x^{1/2+2ϖ}, d | Π_{p<x^ϖ}p} Σ_{c∈C_i(d)} |Δ(θ;d,c)| ≪ x log^{−A}x, where C_i(d) = {c mod d : (c,d)=1, P(c−h_i) ≡ 0 mod d}. Zhang proves it for 0 < ϖ ≤ 1/1168.
  - This sums over **all roots of a fixed polynomial** P(n) = Π(n+h), i.e. residues depending on the factorisation, but only for smooth squarefree moduli.
  - **[my derivation]** Zhang's P has leading coefficient 1, but the method is via CRT/residue-agnostic Deligne/Weil bounds, so (p+4)(4p+1) should be analogous. Not checked in a source.
- **Bombieri–Vinogradov** handles max over residues up to x^{1/2}/(log x)^B.
- **Spectral (Kloosterman) BFI results need a single fixed residue a ≪ x^ε** (Maynard III, p.2: "this essentially restricts one to only considering the same residue class a ≪ x^ε for all moduli q").
- **BFI 1986 (Acta Math. 156, 203–251), Theorem 9: exact statement UNVERIFIED.** I could not obtain the PDF. Confirmed facts:
  - FI 2009 (VERIFIED) use "[BFI, Theorem 9]" to evaluate Σ_{k≤√x} χ(k) Σ_{k²<p≤x, p≡1(4), p≡4(k)} log p = 8Σχ(k)(x−k²)/φ(4k) + O(x(log x)^{−A}). The moduli 4k go up to 4√x, the residue is fixed (4), and the weights χ(k) are bounded.
  - Friedlander–Granville–Hildebrand–Maier (JAMS 1991, search snippet only) cite "Theorem 9 of [BFI] (for fixed a)".
  - Lichtman 2211.09641 cites "[5, Theorem 9]" as the mean-value theorem giving asymptotics for Σ_l Σ_m π(x; a, lm) in Baker–Harman's shifted-primes argument.
  - Maynard I's Theorem A (BFI 1986 + BFI II) and Theorem B = "[BFI, Theorem 10]" (well-factorable, level x^{4/7−ε}). VERIFIED in Maynard I, arXiv:2006.06572, p.4.

---

## Bottom line for "infinitely many primes p with p+4 and 4p+1 having all prime factors ≡ 1 (mod 4)"

1. **This is structurally the Friedlander–Iwaniec hyperbolic-PNT problem**, which is unsolved unconditionally.
   - Put m = 4p+1. Then 4(p+4) = m+15 and r(4(p+4)) = r(p+4), so the count is ≈ Σ_m Λ-type · r(m) r(m+15).
   - FI (Acta Math 2009, Thm 2/4, VERIFIED) get the lower bound for Σ Λ(n) r(n−2)r(n+2) **only under A(θ), θ<1 close to 1** (an Elliott–Halberstam-type hypothesis). The upper bound is unconditional.
   - Sedunova (2026) still has only almost-primes (ω ≤ 7) unconditionally.
2. **One shifted sum-of-two-squares condition on primes is unconditional; two are not known.**
   - FI Thm 5: Σ_{p≤x} r(p−4) log p ~ c x, via BFI Thm 9 at moduli ≈ √x (Thm 9 exact statement UNVERIFIED).
   - Nath–Xie get p−1 = □+□ with Ω(p+2) ≤ 9 (vector semilinear × linear sieve).
3. **Levels of distribution of the relevant weights are small.**
   - r(n−2)r(n+2) with n ≡ 0 (mod d): level x^{1/6} (Sedunova Lemma 2; FI had x^{1/12}).
   - d(n)d(n+h) in a fixed AP: q ≤ X^{0.281} (X^{1/3} under Selberg), Grimmelt–Merikoski Cor. 1.3. There is no r(n)r(n+h) analogue in the literature.
4. **Residues depending on the factorisation (p ≡ −4 mod d1, 4p ≡ −1 mod d2) are allowed beyond x^{1/2} only in restricted forms**: Maynard III Thms 1.2/1.3 (convenient factor sizes, level x^{1/2+δ}) and Zhang/Polymath MPZ (smooth moduli, all roots of a fixed polynomial). Spectral BFI/Maynard I–II/Lichtman need one fixed residue.
5. **Sieve inputs are too narrow.**
   - Harman's sieve gives an asymptotic from Type I to x^α plus Type II on (x^α, x^{α+1/2}). With narrower Type II it only gives correct-order lower bounds (Merikoski 2112.03617, GMPP 2610.41356).
   - Two-variable linear-correlation theorems (Heath-Brown, Matthiesen) need ≥ 2 independent long variables. One-variable multi-shift r/τ correlations remain open (Blomer: triple τ only on average over h ≥ N^{1/3+ε}).
