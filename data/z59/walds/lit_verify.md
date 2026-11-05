# z59 WALDS — literature verification log

| # | Statement used | Source, number | How verified | Confidence |
|---|---|---|---|---|
| 1 | Prop. 1 (Shimura): S_{k/2}(N,χ) = ⊕_{φ₀} S_{k/2}(N,χ,φ₀), φ₀ newforms of weight k−1, character χ², S(N,χ,φ₀) = {f : T(p²)f = λ_p(φ₀)f for almost all p ∤ N}; for k = 3 the space is the complement of unary thetas (I.1) | Waldspurger, J. Math. Pures Appl. 60 (1981) 375–484, p. 376–377 | primary PDF https://mate.dm.uba.ar/~nsirolli/files/waldspurger.pdf, pp. 376–379 rendered as images and read by the lane | high |
| 2 | Prop. 2 (Flicker): S(N,χ,φ₀) ≠ 0 for some N iff (H1) | ibid. p. 377 | same | high |
| 3 | χ₀(n) = χ(n)(−1/n)^{(k−1)/2}; χ_t = quadratic character of ℚ(√t); φν = newform with λ_p(φν) = ν(p)λ_p(φ) a.e.; L(φ, s) completed with 2(2π)^{−(s−1+k/2)}Γ(s−1+k/2) | ibid. pp. 376–378 | same | high |
| 4 | Théorème 1 (needs (H1), (H2)): A(t)² = L(φ₀χ₀^{−1}χ_t, ½)ε(χ₀^{−1}χ_t, ½); a_n(c_E, A) = A(n^{sc})n^{(k−2)/4}∏_p c_p(n); c_p ∈ U_p(e_p, φ₀), ℤ_p^{×2}-invariant (I.3, 4°), c_p = c_p⁰ with c_p⁰(u) = 1 for v_p(u) ∈ {0,1} in the general case (5°) | ibid. pp. 377–379 | same | high |
| 5 | Corollaire 2 (needs only (H1)): a_{n₁}(f)²L(φ₀χ₀^{−1}χ_{n₂}, ½)χ(n₂/n₁)n₂^{k/2−1} = a_{n₂}(f)²L(φ₀χ₀^{−1}χ_{n₁}, ½)n₁^{k/2−1} for f ∈ S(N,χ,φ₀), n₁, n₂ squarefree, n₁/n₂ ∈ ℚ_p^{×2} ∀p | N | ibid. p. 379 | same | high |
| 6 | Twist of a primitive form by a primitive character of coprime conductor: level qr², root number × χ(r)ψ(q)τ(ψ)²/r | Iwaniec–Kowalski, Analytic Number Theory (2004), Prop. 14.20, p. 377 | research subagent, book PDF | high |
| 7 | Ono–Skinner: Cor. 3, #{|D| ≤ X : L(F⊗χ_D, k) ≠ 0, (D,M)=1} ≫ X/log X (fundamental D; prime twists left open) | Invent. Math. 134 (1998) 651–660 | research subagent, author-hosted PDF | high |
| 8 | Ono: Thm 1, non-vanishing for twists by D_F·p₁⋯p_{2j} (even number of primes from a Frobenius set) | J. reine angew. Math. 533 (2001) 81–97 | research subagent, author-hosted PDF | high |
| 9 | CKRS Conjecture 1, eq. (25): #{p ≤ T prime : L_E(½,χ_p) = 0, sign +} ∼ c_E T^{3/4}(log T)^{−5/8} | Conrey–Keating–Rubinstein–Snaith, Number Theory for the Millennium I (2002); arXiv math/0012043 | research subagent, PDF | high (that it is stated for prime twists); no residue-class version found |
| 10 | Heath-Brown Thm 3 (under RH for twists: average analytic rank ≤ 3/2 + o(1) in each sign family), Thm 4 (≥ 1/4 of + family rank 0, weighted) | Duke Math. J. 122 (2004) 591–623; arXiv math/0305114 | research subagent, arXiv PDF | high |
| 11 | Lester–Radziwiłł Thm 1 (GRH: ≫ X sign changes), Thm 2 (unconditional ≫ X^{1−ε}) for plus-space forms, indices 8n, n odd squarefree; appendix level 4N, N odd squarefree | Math. Ann. 379 (2021) 1553–1604; arXiv 1903.05811 | research subagent, arXiv PDF | high |
| 12 | Gross–Zagier + Kolyvagin: analytic rank ≤ 1 ⟹ Mordell–Weil rank = analytic rank (so MW rank ≥ 2 ⟹ L(E,1) = 0) | stated in W. Zhang, "Selmer groups and the indivisibility of Heegner points", Camb. J. Math. 2 (2014), §1 (PDF https://math.mit.edu/~wz2113/math/online/Kconj.pdf, line "The theorem of Gross–Zagier and Kolyvagin asserts that if the analytic rank of E/Q is at most one, then the Mordell–Weil rank is equal to the analytic rank and Ш(E/Q) is finite") | lane, secondary statement read; originals (Gross–Zagier Invent. Math. 84 (1986); Kolyvagin 1988/1990) not re-read | medium-high |
| 13 | Shimura's T(p²) formula (S4); TERNARY inputs (S1)–(S5) | as in `data/z58/ternary/lit_verify.md` §§1–4, 8 | inherited (TERNARY + its cross-model review) | as there |

Not verified and **not used**: Rankin–Selberg prime orthogonality (Liu–Wang–Ye 2005) and linear independence of
characters of Galois representations — Theorem W1 avoids both by using (T1\*) at all squares built from large primes
(Dedekind-type argument, §3.1 Step 3). Waldspurger 1991 (Forum Math.) and Baruch–Mao (Thm 10.1 is restricted to odd
squarefree level) were checked only to the extent that neither removes (H2) in our setting; Remark W3's sign −1 case
without (H2) stays CONDITIONAL.
