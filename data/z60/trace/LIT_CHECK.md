# Literature check (z60 / trace) — results

Checked against primary sources where I could get them (arXiv full texts, Shimura's 1974 Acta paper, the Diamond–Shurman book text). Some items are checked only through secondary sources that quote the result; those are labelled. Downloaded texts are cached in `/tmp/lit/` (not committed).

Confidence: **H** = checked in the primary text; **M** = checked in a secondary source that quotes the result, or partly checked; **L** = from memory, not checked.

---

## 1. Eichler–Selberg trace formula for a general Fuchsian group / double coset ΓαΓ

### Correction: Shimura's 1971 book, Ch. 6, is the wrong reference

- **What I checked:** the table of contents of Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (1971). Source: https://external.dandelon.com/download/attachments/dandelon/ids/DE0043D04F2DDAE605F3CC1257661003E0043.pdf
- **Finding:** Chapter 6 is "Modular functions of higher level". Its sections are §6.1–6.9, covering the reciprocity law, the adelization of GL₂, Aut(𝔉), and canonical models. §6.8 and §6.9 are *not* trace formulas.
- **Finding:** the book has no general trace-formula chapter. Ch. 2 holds the dimension formulas (§2.6). Ch. 3 covers Hecke operators. §7.5 uses the trace of correspondences on V_S.
- **Confidence:** H.

### Correct general-Fuchsian reference: Shimura, Acta Math. 132 (1974)

- **Citation:** G. Shimura, "On the trace formula for Hecke operators", *Acta Math.* 132 (1974) 245–281.
- **URL:** http://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6170-11511_2006_Article_BF02392117.pdf (full text, read).
- **Setting:** Γ ⊂ SL₂(ℝ) is discrete with finite covolume. α lies in the commensurator. The weight m is any rational number.
- **Theorem 4.5 (the group-theoretic, "second formulation"):**
  tr([ΓαΓ]* | A_m) − tr([Γα⁻¹Γ]_* | B_{2−m}) = Σ_{C ∈ Φ(ΓαΓ/Γ)} J(C)
  - A_m is the space of cusp forms. B_{2−m} is the space of "integral forms" of weight 2−m.
  - Theorem 3.7 is the first, algebro-geometric formulation. Theorem 5.2 drops one hypothesis.
- **The set Φ(ΓαΓ) (§4.1)** consists of:
  - scalar elements;
  - elliptic elements;
  - hyperbolic elements whose upper fixed point is a cusp of Γ;
  - parabolic elements whose fixed point is a cusp.
- **J(C) for each type (§4.1):**
  - scalar: ∝ vol(Γ\H)·(m−1)/(4π);
  - elliptic: [Z_Γ(β):1]⁻¹ η⁻¹/(1−λ⁻²);
  - hyperbolic (cusp-fixing): −[Γ∩{±1}:1]⁻¹ η⁻¹/(1−λ⁻²)… (glyphs garbled by OCR);
  - parabolic: two separate cases, according to whether β ∈ {±1}·Γ.
- **The k = 2 correction (introduction):**
  - For integral m > 2, B_{2−m} = 0, which recovers Selberg and Eichler.
  - For m = 2, B₀ consists of the constants, so the correction is tr(Γα⁻¹Γ | constants) = deg(Γα⁻¹Γ), i.e. the number of cosets.
- **Caveats:**
  - The theorem carries technical hypotheses: (3.5.1–2), (3.6.1), and the existence of a normal subgroup Γ₁ with properties (i)–(iv).
  - The exact constants in J(C) are hard to read from the OCR; check them in the PDF before quoting.
- **Confidence:** H.

### Modern statement for any finite-index Γ ⊂ SL₂(ℤ), including Γ(N)

- **Citation:** A. A. Popa, "On the trace formula for Hecke operators on congruence subgroups", *Proc. AMS* 146 (2018); arXiv:1408.4998.
- **Theorem 1 — setting:**
  - Γ is any finite-index subgroup of SL₂(ℤ), k ≥ 2.
  - χ is a character of Γ with finite-index kernel.
  - Σ is a double coset satisfying |Γ\Σ| = |Γ₁\Γ₁Σ|.
- **Theorem 1 — formula:**
  Tr([Σ], M_k(Γ,χ) + S_k^c(Γ,χ)) = Σ_{X⊂Σ} p_{k−2}(tr M_X, det M_X) χ̃(M_X) ε_Γ(X) + δ_{k,2} δ_{χ,1} Σ_{σ∈Γ\Σ} χ̃(σ)
  - The first sum runs over Γ-conjugacy classes. p_w is the Gegenbauer polynomial defined by (1−tx+nx²)⁻¹ = Σ_w p_w(t,n) x^w.
- **Second version:** ε(X) = 1/6 for scalar, −1/|Stab| for elliptic, 1 for hyperbolic fixing two cusps, 0 otherwise.
- **Caveat:** the formula gives the trace on M_k + S̄_k, *not* on S_k alone. Remark 3.2 allows replacing S̄_k by S_k under a symmetry assumption.
- **Directly relevant special cases:**
  - Torsion-free Γ: dim M_k + dim S_k = (k−1)/6·[Γ̄₁:Γ̄] + δ_{k,2}, with the **projective** index [PSL₂(ℤ):Γ̄] (z60 xreview correction: with the SL₂-index, Γ(4) would give 16 for dim M₃ + dim S₃ instead of 7 + 1 = 8).
  - Theorem 3 / (1.3): lim_{n→∞, (n, ℓ(ℓ−1))=1} Tr(T_ℓ, M_k(Γ_n)+S_k(Γ_n))/φ(n) = (ℓ^{k−1}−1)/2.
- **Related papers:**
  - Popa, "A trace formula for Hecke operators on Fuchsian groups", arXiv:2306.10396 (2023). It covers general finite-covolume Γ and a cohomological Lefschetz form Σ(−1)^i tr([Σ], H^i(Γ,V)) = Σ_X ε_Γ(X) tr(M_X, V).
  - Popa, arXiv:1706.02691 (part II), which specialises to Γ₀(N) and Γ₁(N).
- **Confidence:** H.

### Miyake, *Modular Forms*, Ch. 6 "Trace formulae"

- **Finding:** Theorem 6.8.4 is the explicit Eichler–Selberg formula; Hill (arXiv:0902.2603, Thm 3.7) quotes it for Shimura-curve and Γ₀(N)-type groups.
- I could not confirm the number of Miyake's general-Fuchsian-group theorem (somewhere in §6.5–6.6).
- **Confidence:** M for 6.8.4; L for the rest.

### Not checked

- Oesterlé's 1977 thesis.
- Zagier's appendix to Lang. Ribet–Stein confirm it exists and covers SL₂(ℤ) only.
- Knightly–Li, *Traces of Hecke operators* (AMS Surveys 133, 2006).

---

## 2. Cohen–Strömberg, Theorem 12.4.11

- **Citation:** H. Cohen and F. Strömberg, *Modular Forms: A Classical Approach*, AMS GSM 179 (2017), Thm 12.4.11.
- **Number:** confirmed by several independent papers citing "[CS, Theorem 12.4.11]" for the trace on S_k(Γ₀(N), χ):
  - K. Child, arXiv:2101.05663 (Res. Number Theory 2022), eq. (4.1);
  - Cason et al., arXiv:2407.11694, Lemma 2.2;
  - Tu, arXiv:2509.02985, Lemma 9.
- **Shape (as quoted by Child and Cason):**
  - If χ(−1) ≠ (−1)^k the trace is 0. Otherwise:
  - **Tr T_m = A₁ − A₂ − A₃ + A₄.** So the form is A₁ − A₂ − A₃ + A₄, *not* A₁+A₂+A₃+A₄.
  - A₁ = χ(√m)·(k−1)/12·ψ(N)·m^{k/2−1}, where ψ(N) = N∏_{p|N}(1+1/p).
  - A₂ = ½ Σ_{t²<4m} U_{k−1}(t,m) Σ_f h_w((t²−4m)/f²) μ(t,f,m,N).
    - U_{k−1} is the Lucas sequence (ρ^{k−1}−ρ̄^{k−1})/(ρ−ρ̄).
  - A₃ = ½ Σ_{d|m} min(d, m/d)^{k−1} Σ_{τ|N, (τ,N/τ) | (N/f(χ), m/d − d)} φ((τ,N/τ)) χ(y_τ).
    - Child writes it equivalently as Σ'_{d|m, d≤√m} d^{k−1} … .
    - y_τ (Child's x₁) is defined by x ≡ d (mod τ), x ≡ m/d (mod N/τ).
    - The τ-condition (τ, N/τ) | (N/f(χ), m/d − d) is a **congruence condition on m/d − d** (as quoted by Cason).
  - A₄ = Σ_{c|m, (N, m/c)=1} c when k = 2 and χ is trivial; A₄ = 0 otherwise.
- **Caveat:** I did not see the book itself, so the exact typography is unverified. Two independent quotes agree on the signs and the terms.
- **Confidence:** M+.

---

## 3. Eichler–Zagier, *The Theory of Jacobi Forms* (Progress in Math. 55, Birkhäuser 1985)

### Theorem 1.3 (specialisation at torsion points) — confirmed

- **Statement as quoted** by Quinones's thesis (Thm 7.2, "[EZ, Theorem 1.3]"):
  "Let φ be a Jacobi form on Γ of weight k and index m, and let α, β ∈ ℚ. Then f(τ) = e^{2πi m α²τ} φ(τ, ατ+β) is a modular form of weight k on a finite-index subgroup Γ′ depending only on Γ, α, β."
- **Other sources citing "[EZ, Theorem 1.3]"** for the same fact:
  - van Ittersum, arXiv:2102.12964;
  - arXiv:1710.10025, p. 9;
  - arXiv:2606.13173: "specialized to torsion points yields a modular form".
- **Confidence:** M+ (the number agrees across four sources).

### Theorem 2.1 (coefficients of the Jacobi–Eisenstein series), not 2.3

- **Source:** arXiv:1710.10025 (Gritsenko et al.).
- "By [EZ, Theorem 2.1] E_{k,m} (k ≥ 4 even) converges and defines a non-zero element of J_{k,m} … for 4n > r², e_{k,1}(n,r) = H(k−1, 4n−r²)/ζ(3−2k)."
- The relation E_{k,m} = m^{−k+1}∏_{p|m}(1+p^{−k+1})⁻¹ Σ_{d²|m} μ(d) E_{k,1}|U_d∘V_{m/d²} is EZ eq. (13), p. 48.
- **"Theorem 2.3":** I found no source citing EZ Thm 2.3 for this, so the number is unverified. Use "EZ, Theorem 2.1 (and its m = 1 case)" instead.
- **Confidence:** M for 2.1; L/unverified for 2.3.

### Weight 2, index 1: coefficients −12·H(4n − r²)

- **Supporting source:** B. Williams, "Vector-valued Hirzebruch–Zagier series and class number sums", Res. Math. Sci. 2018 (https://btw-47.github.io/hzforms3.pdf).
  - Eq. (1): E*_{2,1/m,β}(τ,z,0) = −12 Σ H(4n − m r²) q^n ζ^r e_γ + (non-holomorphic term).
  - The m = 1 analogue is the classical non-holomorphic E*_{2,1} built on Zagier's weight-3/2 function.
- **Not verified:** where in EZ this weight-2 case is discussed (§2, or the Zagier C.R. reference). It is not a holomorphic Jacobi form; the non-holomorphic correction is needed.
- **Zagier reference** (bibliographic data agree across several sources):
  - D. Zagier, "Nombres de classes et formes modulaires de poids 3/2", *C. R. Acad. Sci. Paris Sér. A-B* 281 (1975), no. 21, A883–A886.
- **Confidence:** M for the −12·H shape; L for the EZ location.

---

## 4. Hurwitz class-number sums in arithmetic progressions

Notation: H_{a,M}(n) := Σ_{t≡a (M)} H(4n − t²).

### (a) Brown, Calkin, Flowers, James, Smith, Stout

- **Citation:** *J. Number Theory* 128(6) (2008) 1847–1863; arXiv:1208.4769.
- **What is evaluated:**
  - Mostly n = p prime, modulus m = 2, 3, 4 (complete), 5 and 7 (partial), with conjectures in tables.
  - Thm 1 (m=2), Thm 2 (m=4), Thm 3 (m=3), Thm 4 (m=5, partial), Thm 6 (m=7).
  - Thm 5 / Prop. 4: m = 3 for general n via weight-3/2 forms; the right-hand side is divisor sums μ₁, μ₂, μ₃ with d ≢ 0 (mod 2 or 3).
- **Methods:** counting elliptic curves over 𝔽_p (Deuring); the m = 3 partial generating function (their Thm 9); and in §4 (Thm 10, Prop. 5) the Eichler–Selberg trace formula for T_p on S₂(7) = 0.
- **min(d, n/d) with congruences?** No. Only the unrestricted Hurwitz identity Σ H(4N − r²) = 2σ(N) − 2λ(N), with λ(N) = ½Σ_{d|N} min(d, N/d).
- **Confidence:** H.

### (b) Bringmann–Kane, "Sums of class numbers and mixed mock modular forms"

- **Citation:** *Math. Proc. Cambridge Philos. Soc.* 167 (2019) 321–333; arXiv:1305.0112.
- **What is evaluated:** H_{a,p}(n) for an odd prime p, any n. This proves the BCFJSS conjectures for p = 5 and 7 (Thm 1.3).
- **Main Theorem 1.4:**
  (H(q)ϑ_{a,p})|U(4) ⊗ χ_{2p} + Σ_{b mod p, b≢±a} G_{p,a+b}(q) | S_{p,a²−b²}
  is a holomorphic weight-2 modular form on Γ₀(p²) ∩ Γ₁(p) (on Γ₀(p²) if a = 0). Here:
  - G_{N,r}(q) := Σ_n Σ_{dd′=n, d′>d, d≡±r (N)} d q^n + Σ_n (Nn−r) q^{(Nn−r)²};
  - S_{N,r} sieves the coefficients with n ≡ r (mod N).
- **min(d, n/d) with congruences? Yes.** These are sums of the smaller divisor d with a congruence on d (d ≡ ±(a+b) mod p), combined with n ≡ a² − b² (mod p).
- **Confidence:** H.

### (c) Mertens, "Mock modular forms and class number relations"

- **Citation:** *Res. Math. Sci.* 1 (2014), Art. 6; arXiv:1305.5122.
- **What it proves:** Cohen's conjecture (Thm 1.2). For odd n, the coefficient of X^ℓ in Σ_{n odd}[Σ_s H(n−s²)/(1−2sX+nX²) + Σ_k λ_{2k+1}(n)X^{2k}]q^n is a modular form of weight ℓ+2 on Γ₀(4), and a cusp form for ℓ > 0.
- Here λ_k(n) = ½Σ_{d|n} min(d, n/d)^k.
- **Congruence conditions?** Only "n odd". There is no t-progression.
- **Confidence:** H.

### (d) Mertens, "Eichler–Selberg type identities for mixed mock modular forms"

- **Citation:** *Adv. Math.* 301 (2016) 359–382; arXiv:1404.5491.
- **General result:** Thm 5.4 gives holomorphic projection of [f, g]_ν for f a weight-3/2 mock modular form and g a weight-1/2 form.
- **Arithmetic progressions (§7.2):** for ϑ_{(p,a)} = Σ_{n≡a (p)} q^{n²},
  Λ^{(p,a)}_ν = Σ_± Σ_{m²−n²>0, m≡±a (p)} 2(m−n)^{2ν+1} q^{m²−n²} + Σ_{m≡±a} m^{2ν+1} q^{m²},
  and ([H, ϑ_{(p,a)}]_ν + Λ^{(p,a)}_ν)|U(4) is a cusp form of weight 2+2ν (quasimodular when ν = 0).
- **Prop. 7.2** rewrites this through λ^{(p,a)}_k(n) = Σ_{d|n, d≤√n, d≡−a (p)} d^k + Σ_{d|n, d<√n, d≡a (p)} d^k. Corollary 7.3 gives explicit p = 5, 7 cases; for p = 7 a cusp form appears (49a1).
- **min(d, n/d) with congruences? Yes.** With t² − s² = n, (t−s)(t+s) = n, so (t−s) = min(d, n/d) and t = (d + n/d)/2. The condition t ≡ ±a (mod p) is therefore exactly a condition on **d + n/d**.
- **Caveat:** the arXiv introduction prints the Kronecker–Hurwitz relation with a "−2λ₁" sign typo. The correct form is Σ H(4n−s²) = 2σ(n) − 2λ(n), and it holds numerically at n = 1.
- **Confidence:** H.

### (e) Kane–Pujahari, "Distribution of moments of Hurwitz class numbers in arithmetic progressions and holomorphic projection"

- **Citation:** *Trans. AMS* 376 (2023), no. 8; arXiv:2010.15325.
- **What is evaluated:** H_{2k,m,M}(n) = Σ_{t≡m (M)} t^{2k} H(4n−t²) for any M (not necessarily prime).
  - Thm 1.1: H_{2k,m,M}(n)/(n^k H_{m,M}(n)) = C_k + O(n^{−1/2+ε}), where C_k are the Catalan numbers.
- **Lemma 3.3** (Mertens' result, corrected and extended to composite M):
  [H, θ_{m,M}]_k + 2^{−1−2k} binom(2k,k) Λ_{2k+1,m,M} | U₄ is a cusp form of weight 2+2k on Γ₀(4M²) ∩ Γ₁(M) (quasimodular for k = 0). Here:
  - λ_{ℓ,m,M}(n) = Σ_± Σ*_{t>s≥0, t²−s²=n, t≡±m (M)} (t−s)^ℓ;
  - the remark notes that Mertens' constant was wrong and that the prime-M assumption is unnecessary.
- **Congruence on (d + n/d)/2? Yes**, as in (d).
- **Confidence:** H.

### (f) Kane–Pujahari–Yang, "The bias conjecture for elliptic curves over finite fields and Hurwitz class numbers in arithmetic progressions" — the most explicit

- **Citation:** *Math. Ann.* (2025), doi:10.1007/s00208-024-03070-w; arXiv:2405.14234.
- **Smaller-divisor sum (1.6):**
  λ_{k,m,M}(n) := Σ*_{t²−s²=4n, t≡m (M), t≥1, s≥0} ((t−s)/2)^{k+1} + (−1)^k Σ*_{t≡−m (M)} … .
  The star means weight ½ when s = 0. (z60 xreview correction of conventions:) with d := (t − s)/2 one has d | n, t = d + n/d and weight d^{k+1}; equivalently with d′ := t − s one has d′ | 4n, t = (d′ + 4n/d′)/2 and weight (d′/2)^{k+1}. So it is a min-divisor sum with the congruence condition d + n/d ≡ ±m (mod M) on divisors d | n.
- **Thm 1.7 (= Thm 2.11):** for any M ≥ 1 and m ≠ 0,
  H_{m,M}(n) = (2ζ(2)/(M L(2, 1_M))) Σ_{η primitive, N_η|M} Σ_{d∈S(η,m,M)} a(η,d) σ_{1,η,η̄}(n/d) + a_{0,m,M}(n) − λ_{0,m,M}(n),
  - a_{0,m,M}(n) is the coefficient of a weight-2 cusp form g_{m,M};
  - a(η,d) and S(η,m,M) are given explicitly in (1.7)–(1.8).
- **Corollary 1.8:** for representatives 1 ≤ m ≤ M, g_{m,M} = 0 iff 1 ≤ M ≤ 5 or (m,M) ∈ {(2,8),(6,8)}. So relations with no cusp form exist only for finitely many progressions.
- **Thm 1.6:** reduces the higher moments to the zeroth moment.
- **Confidence:** H for the statements. The journal volume and pages were not checked.

Related, not read: Bringmann–Kane–Pujahari, "Formulas for moments of class numbers in arithmetic progressions", arXiv:2109.07325; "Odd moments …", arXiv:2112.08205.

---

## 5. Serre (1997) and Conrey–Duke–Farmer (1997)

### Serre, "Répartition asymptotique des valeurs propres de l'opérateur de Hecke T_p"

- **Citation:** *J. AMS* 10 (1997) 75–102.
- **Access:** the AMS PDF is behind a Cloudflare challenge, so I could not read the original.
- **Statement as quoted** by arXiv:2609.17806 (effective Atkin–Lehner equidistribution), §1.1:
  - Fix a prime p and an interval I ⊂ [−2,2]. For levels N coprime to p and even weight k:
  - #(eigenvalues of T′_p = T_p/p^{(k−1)/2} on S_k(N) in I) / dim S_k(N) → ∫_I dμ_p as k + N → ∞;
  - dμ_p = ((p+1)/2π) · √(4−x²) / ((p^{1/2}+p^{−1/2})² − x²) dx (the p-adic Plancherel measure).
- **Extensions mentioned in that paper:** the proof also gives the analogues for S_k^new(N) and S_k(N, χ).
- **Effective version:** Murty–Sinha, with discrepancy ≪ log p / log kN.
- **Caveat:** I believe the result is "Théorème 1" of §1, but I did not see the original, so the number is unverified.
- **Confidence:** M (statement); L (theorem number).

### Conrey–Duke–Farmer, "The distribution of the eigenvalues of Hecke operators"

- **Citation:** *Acta Arith.* 78 (1997), no. 4, 405–409; arXiv:math/9609214 (read).
- **Theorem 1:**
  - Level 1 only (S_k(SL₂(ℤ))), p prime fixed, k → ∞.
  - θ_f(p) (with a_f(p) = 2cos θ_f) becomes equidistributed for (2/π)(1+1/p) sin²θ / ((1 − 1/p)² + (4/p) sin²θ) dθ.
- **How it relates to Serre:** this is μ_p in the θ variable; it tends to Sato–Tate as p → ∞. It is the weight aspect only; Serre's theorem covers N + k → ∞.
- **Confidence:** H.

---

## 6. Dimension formula and Γ(N) data

### Dimension formulas (Diamond–Shurman, read in full text)

- **Thm 3.5.1 (k even, Γ a congruence subgroup):**
  dim S_k(Γ) = (k−1)(g−1) + ⌊k/4⌋ε₂ + ⌊k/3⌋ε₃ + (k/2 − 1)ε∞ for k ≥ 4; and = g for k = 2.
- **Thm 3.6.1 (k odd, −I ∉ Γ):**
  dim S_k(Γ) = (k−1)(g−1) + ⌊k/3⌋ε₃ + ((k−2)/2)ε∞^reg + ((k−1)/2)ε∞^irr for k ≥ 3.
- **Consequence:** with no elliptic points and all cusps regular, dim S_k = (k−1)(g−1) + (k/2 − 1)ε∞ for every k ≥ 3, even or odd. This confirms the formula you gave.
- **Caveat:** Diamond–Shurman state this only for congruence subgroups. For a general torsion-free Fuchsian group cite Shimura Thm 2.23 (even k) and, I believe, Thm 2.25 (odd k).
  - Thm 2.23 as the general dimension formula is confirmed by citations: Alam, GANIT 2023, quotes it for signature (g; n₁, …, n_r); ANTS XVII cites it too.
  - I did not see the odd-weight number 2.25 or the exact cusp term in Shimura's text.
- **Confidence:** H for Diamond–Shurman; M for Shimura 2.23; L for 2.25.

### Γ(N) data (Diamond–Shurman)

- **Index:** [SL₂(ℤ) : Γ(N)] = N³∏_{p|N}(1 − p⁻²) (§1.2, p. 13).
- **d_N:** d_N = [SL₂(ℤ) : {±I}Γ(N)] = (N³/2)∏_{p|N}(1 − p⁻²) for N > 2, and 6 for N = 2 (§3.8, p. 101–102; Fig. 3.3).
  - Since −I ∉ Γ(N) for N > 2, this equals [PSL₂(ℤ) : Γ̄(N)] and is the degree of X(N) → X(1).
- **Cusps:** ε∞(Γ(N)) = d_N/N = (N²/2)∏_{p|N}(1 − p⁻²) for N > 2 (and 3 for N = 2). The cusp width is N.
- **Elliptic points:** ε₂ = ε₃ = 0 for N > 1.
- **Regularity:** all cusps of Γ(N) are regular. The only irregular cusp among Γ₀(N), Γ₁(N), Γ(N) is 1/2 for Γ₁(4) (§3.8).
- **Figure 3.4 (Γ(N), N > 2):**
  - g = 1 + d_N(N−6)/(12N);
  - dim M_k / dim S_k = (k−1)d_N/12 ± d_N/(2N), the same for k even and odd — **for k ≥ 3 only** (z60 xreview correction: at k = 2, dim S₂ = g, e.g. 0 for Γ(4), not −1).
- **Confidence:** H.

---

## Summary of flags

1. **Shimura 1971, Ch. 6 / "Thm 6.8–6.9" is a wrong reference.** Ch. 6 is modular functions of higher level. Use instead:
   - Shimura, Acta Math. 132 (1974), Thm 4.5 (general Fuchsian group, double coset, with the k = 2 / m = 2 correction); or
   - Popa, PAMS 2018, Thm 1 (any finite-index Γ ⊂ SL₂(ℤ), including Γ(N); gives the trace on M_k + S̄_k).
2. **Cohen–Strömberg 12.4.11 is A₁ − A₂ − A₃ + A₄**, not A₁+A₂+A₃+A₄. Checked through secondary quotes only.
3. **Eichler–Zagier:** Theorem 1.3 is confirmed. The Jacobi–Eisenstein coefficient formula is **Theorem 2.1**; "Theorem 2.3" is unverified. Where EZ discusses the weight-2 E_{2,1} with −12·H(4n − r²) is unverified, though the −12·H shape is confirmed via Williams.
4. **Serre 1997:** the statement is confirmed through a secondary quote; the theorem number is not checked (AMS paywall).
5. **Formulas with min(d, n/d) and a congruence on d + n/d:**
   - Explicitly present in Mertens (Adv. Math. 2016, §7.2), Kane–Pujahari (TAMS 2023, Lemma 3.3) and Kane–Pujahari–Yang (Math. Ann. 2025, Thm 1.7).
   - Bringmann–Kane put the congruence on the smaller divisor d, combined with n mod p.
   - BCFJSS have no such terms.
6. **Not checked:** Oesterlé's thesis, Knightly–Li, Zagier's appendix to Lang, the general-Fuchsian theorem number in Miyake, and Shimura Thm 2.25.
