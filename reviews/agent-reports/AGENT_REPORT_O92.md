# Agent report O92 (branch side-agent/lfl-sign-point) — 7-power tower at x̂_9

Deliverable: POINTWISE_TYPEI5.md, scripts/typei5_{relax.c,dmod.c,regimes.py,lehmer_check.py}. Not merged.

## Results
1. **Lemma 1.1 (PROVED, elementary, all L).** If 16PX² − Qu² = 1 with 7 | Q has a solution with u = 7^b (u odd), then it is the
   *minimal* solution: all solutions are α^n (n odd), u_n = u_1·L_n with L_n ≡ n (mod 7), v_7(L_7) = 1, L_7 > 7, so u_n is never a
   7-power for n ≥ 3. **Cor 1.2:** b is a function of (a,c',δ,P_1); the certificate unit is ε_f^k, k ∈ {1,2,4}. This proves TYPEI4
   Obs 1.5 (sharpened) and supersedes Assessment 4.2(c) (BHV n ≤ 30 → n = 1). It also makes the d-graded engine complete for all b.
2. **Comp 2.2 / Cor 2.3 (CERTIFIED once replayed).** New engine typei5_dmod (unit residues mod 2^64 and 7^22 along the CF of √d, plus the
   Legendre-shape filter (A−1)/(2·7^{a+2b}) | M). It reproduces the 8 dgraded hits for c_oδ ≤ 3000, L = 5..24. **No fibre certificate at
   L = 7..10 with c_oδ ≤ 10⁶, any v_7(k).**
3. **Lemma 3.1 (PROVED):** λ = (ρj−m)/u is integral without the hypothesis 7∤j. This fixes the R89-S2 gap in TYPEI4 Lemma 3.6.
   **Lemma 3.2:** exact identities (H) ρΔ = 2λ(Tu+2j) and (Lin), linear in u. **Prop 3.3** splits case B into regimes. (i) λ=0 is
   impossible. (ii) λ<0 and (iii) λ>0, Δ<2Tj are **finite and explicit** at every L. (iv) Δ=2Tj is trivial. (v) λ>0, Δ>2Tj is
   bounded for fixed (σ,a,λ), but σ, λ are unbounded.
4. **Comp 3.4 (CERTIFIED once replayed):** regimes (ii)–(iv) contain no certificate at L = 7..10, for any b. In relax mode it reproduces
   the brute-force relaxed solutions.
5. **Lemma 3.6 (PROVED, by hand; follow-up turn): case A (2y > T7^b) is empty at L = 7..10, for all b.**
   P_1 ≤ z gives J < T/(4·7^a), so J = 1 and ρ = 1 at L = 9, 10. Then G = c'g divides 7 − T/2 ∈ {−9, −25}, which forces u ∈ {1, 7}, and
   both are excluded by hand.
6. **Theorem 3.7:** a certificate at x̂_9 of level 7..10 must have v_7(k) ≥ 8 **and** c_oδ > 10⁶ **and** lie in regime (v) of case B
   (λ ≥ 1, Δ > 2Tj).

## Not achieved / honest assessment
- No level is closed for all b. At L = 7 everything reduces to regime (v): a two-parameter family (σ ≈ 256u/μ², κ = 8·7^aλ). Equivalently
  (Cor 1.2), we need the unit coefficient u_1(d) of the moving family d = c_o(c_oδ²+T) to be a power of 7. LFL/BHV/Baker–Davenport bound
  exponents in a *fixed* field or recurrence. Here the field moves with two free parameters, so they do not apply. This is an Assessment
  of the obstruction, not a theorem. Fixed-(σ,a,λ) slices are finite by Prop 3.3(v), and sweeping them is a cheap extension.
- Regime (v) is the only open part at L = 7..10.

## Review hints
Check the Lemma 1.1(a) unit-group argument (m=2 case, P a square), and the sign claims in Prop 3.3(ii)/(iii)/(v). Also check the
soundness of the dmod filter (Lemma 2.1) and the factorisation R = κs³(4T³−sκ)².
