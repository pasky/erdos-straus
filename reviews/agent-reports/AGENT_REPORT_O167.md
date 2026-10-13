# AGENT_REPORT_O167 — strong approximation / rank-4 encodings with a fixed modulus (checkpoint 1)

Main file: `STRONG_APPROX_ES.md`. Script: `scripts/sa_typeII_matrix.py`. ES is not solved; no positive claim.

**Results (labels as in the file).**
1. Literature (§1, research subagent, not re-read by me except Pila): unconditional rank-4 SA = Sardari
   Thm 1.2, `N ≫ q^{6+ε}`, fixed form, odd N; exponent 4 conjectural (Sardari Conj 1.3; BKS covering 4/3
   under Twisted Linnik). No disc-uniform version found.
2. Thm 2.3 (PROVED rel. Pila, Astérisque 228 Thm A — statement checked in the PDF): bounded-degree piecewise
   rational recipes on `{Q_p = N_p} ∩ (λ + q ℤ⁴)` are SA-idle; only constant pieces matter (finite menu).
   Uses Lemma 2.2: the affine quaternary quadric contains no plane. Rank-4/p-dependent analogue of
   POINTWISE_TERNARY Thm 4.1.
3. Prop 3.1 (PROVED): det-n matrices in any class mod q (gcd(n,q)=1) realise every factorisation of n;
   Cor 3.2: factorisation recipes are idle.
4. Thm 4.1 (PROVED rel. ET/Prop 2.3): bounded multiplicity + any SA range exponent > 1 ⇒ all data p^{o(1)};
   the ES-natural quaternary representations (QUATERNION_ES Lemma 3.1 norms 4a²d+p in a form of √D = dp)
   sit at expected count O(1).
5. Matrix dictionary: Type II(p) ⟺ γ = [[f,4cd],[cp,f']] ∈ SL₂(ℤ), f ≡ f' ≡ −1 (mod γ₁₂); the solution set
   is a union of `U⁻`-double cosets, one per M = γ₁₂. EVIDENCE: control to n ≤ 6000 (primes yes, odd squares no).
6. §7: Type II = positivity of weight-2 Eisenstein (rank-4 genus) coefficients σ(n; −1, g); weights are capped
   by the solution, so the polylog scale returns (Cor 7.2).

**Honest verdict.** Every rank-4 SA route found collapses to B1/B2/B6 via the map back to ES solutions. The
fallback (scoped obstruction) is written; the "break-through" part produced no live route. Weakest points
for a hostile reviewer: Thm 2.3's use of σ_p ≥ N^{−o(1)} (anisotropic primes), Prop 5.1's "depends only on
n mod L" (needs bounded `v_ℓ(N_n)`), and the §1 literature statements (subagent-verified only).

**Sparks (not pursued).**
* Uncapped fibre weights (FIBRED (E-a)): is there any rank-4 theta-type identity where an ES solution's
  weight exceeds n? (Cor 7.2 shows the natural one is capped at n.)
* The `U⁻ × U⁻` double-coset structure of Type II: ES = "Γ₀(p) meets the double coset U⁻γ_M U⁻ with the
  extra `c | M/4`". Horocycle/double-coset equidistribution (unipotent flows) at scale M ≍ p^{1/2}? Probably
  meets Thm 4.1 again, but the extra divisibility `c | M/4` is the only non-congruence piece left.
* Exact (cusp-free) quaternary identities (Jacobi r₄ = 8σ) with q = 2, 4 as a source of H-E positive identities.
