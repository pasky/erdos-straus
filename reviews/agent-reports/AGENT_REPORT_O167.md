# AGENT_REPORT_O167 — strong approximation / rank-4 encodings with a fixed modulus (checkpoint 1)

Main file: `STRONG_APPROX_ES.md`. Script: `scripts/sa_typeII_matrix.py`. ES is not solved; no positive claim.

**Results (labels as in the file).**
1. Literature (§1, research subagent, not re-read by me except Pila): unconditional rank-4 SA = Sardari
   Thm 1.2, `N ≫ q^{6+ε}`, fixed form, odd N; exponent 4 conjectural (Sardari Conj 1.3; BKS covering 4/3
   under Twisted Linnik; BKS is IMRN, not Duke; Sardari Thm 1.6 needs λ primitive — R167 repair). No disc-uniform
   version found.
2. Thm 2.3 (PROVED rel. Pila, Astérisque 228 Thm A — statement checked in the PDF): bounded-degree piecewise
   rational recipes on `{Q_p = N_p} ∩ (λ + q ℤ⁴)` are SA-idle; only constant pieces matter (finite menu).
   Uses Lemma 2.2: the affine quaternary quadric contains no plane. Rank-4/p-dependent analogue of
   POINTWISE_TERNARY Thm 4.1.
3. Prop 3.1 (PROVED): det-n matrices in any class mod q (gcd(n,q)=1) realise every factorisation of n;
   Cor 3.2: factorisation recipes valid on the whole unboxed class are idle (R167 repair: for recipes valid only
   on the boxed R_p this is UNPROVED; indefinite Eichler orders only; recipe must factor through g).
4. Thm 4.1 (PROVED rel. ET/Prop 2.3, under (A) σ_p ≥ N_p^{−o(1)} — R167 repair: false without (A), e.g.
   x²+y²+3z²+3w² at N = 9^k): bounded multiplicity + any SA range exponent > 1 ⇒ all data p^{o(1)};
   the ES-natural quaternary representations (QUATERNION_ES Lemma 3.1 norms 4a²d+p in a form of √D = dp)
   sit at expected count O(1).
5. Matrix dictionary: Type II(p) ⟺ γ = [[f,4cd],[cp,f']] ∈ SL₂(ℤ), f ≡ f' ≡ −1 (mod γ₁₂); the solution set
   is a union of `U⁻`-double cosets, one per M = γ₁₂. EVIDENCE: control to n ≤ 6000 (primes yes, odd squares no).
6. §7: Type II = positivity of the divisor sums σ(n; −1, g) (R167 repair: these are NOT rank-4 genus coefficients —
   the Type II content is in the odd-character part, which has no weight-2 form; Cor 7.2 relabelled Assessment); weights are capped
   by the solution, so the polylog scale returns (Cor 7.2).

**Honest verdict.** Every rank-4 SA route found collapses to B1/B2/B6 via the map back to ES solutions. The
fallback (scoped obstruction) is written; the "break-through" part produced no live route. Self-check repair: Cor 2.4's margin is only Sardari's fixed ε₀
(N ≥ q^{6+ε₀}); with a better (conjectural, exponent-4) range near its boundary, Thm 2.3 is too weak (gap
recorded in §2). Weakest points
for a hostile reviewer: Thm 2.3's use of σ_p ≥ N^{−o(1)} (anisotropic primes), Prop 5.1's "depends only on
n mod L" (needs bounded `v_ℓ(N_n)`), and the §1 literature statements (subagent-verified only).
*(R167 repair: all three confirmed by R167 and repaired in the file — (A) made an explicit hypothesis of Cor 2.4/
Thm 4.1; Prop 5.1 restricted to m in suitable classes and to Type I/II-valued recipes; §1 citations fixed. Cor 4.2
relabelled Assessment.)*

**Sparks (not pursued).**
* Uncapped fibre weights (FIBRED (E-a)): is there any rank-4 theta-type identity where an ES solution's
  weight exceeds n? (Cor 7.2 shows the natural one is capped at n.)
* The `U⁻ × U⁻` double-coset structure of Type II: ES = "Γ₀(p) meets the double coset U⁻γ_M U⁻ with the
  extra `c | M/4`". Horocycle/double-coset equidistribution (unipotent flows) at scale M ≍ p^{1/2}? Probably
  meets Thm 4.1 again, but the extra divisibility `c | M/4` is the only non-congruence piece left.
* Exact (cusp-free) quaternary identities (Jacobi r₄ = 8σ) with q = 2, 4 as a source of H-E positive identities.

## Checkpoint 2 (sparks: exact identities, double cosets, uncapped weights) — STRONG_APPROX_ES.md §§9–11

1. **Thm 9.1 / Cor 9.3 (PROVED, elementary).** Every finite combination E of `σ_k(n; χ, ψ)` (conductors | L)
   covers all rank-4 one-class genera via Siegel–Weil, Jacobi's r₄, and old-form shifts. Such an E is a
   quasi-polynomial at primes. If E vanishes at infinitely many prime squares ℓ² ≡ 1 (L), then E(p) = 0 for
   *all* primes p ≡ 1 (L). The minorant version holds too (E ≤ 0 at squares ⇒ E(p) ≤ 0), and so does the
   counting version (an n-uniform error B·n^θ ⇒ no certification on p ≡ 1 (L)). So no H-E identity of this
   kind exists for Type I/II certificate counts (which vanish at odd squares), whatever the weights. Proof:
   compare top monomials of `P(ℓ) = Σ C_k(1+ℓ^k+ℓ^{2k})` and `E(p) = Σ C_k(1+p^k)`.
   Scope: only the class p ≡ 1 (L) is claimed; for other square classes the induction is not clean (not needed).
   *(R167 repair: Cor 9.2's extension to "every n-local quasi-polynomial object" was false (h(n) = n·μ(n)²) and is
   restricted to divisor-sum combinations; Cor 9.3's Reading holds only for maps valid at all odd n, not for maps
   valid only at primes.)*
2. **EVIDENCE (`scripts/sa_exact_fit.py 10000`).** I tested 150 basis functions: σ_k at n, n+1, n+2 with
   characters mod 3, 4, 8, plus quasi-polynomials mod 24. None fits the cubic certificate counts
   `guv − u − v = n` (all / Type II / weighted by m; test residual ≈ mean). The Type II counts vanish on all odd
   squares ≤ 10⁴.
3. **Double cosets (Lemma 10.1, Prop 10.2; PROVED — R167 repair: p ∤ M now proved; Prop 10.2's "what a level can
   impose" reading and the §10 expected counts are Assessment/heuristic).** Type II = `⊔_M U⁻γ_M U⁻ ∩ {γ₂₁ = cp}`. After
   conjugating by diag(1,c), the only non-congruence condition is `c = γ₁₂/M | M/4`. One level can absorb it only
   for a fixed finite menu of c, and each M still needs its own level. The needed statement is the distribution
   of the modular hyperbola mod Mp in hyperbolic shells, each with expected count `log p/M`, against the
   divisor-indexed family `c' | M/4`. Summed over a dyadic range the main term is ≍ log²p, against Kloosterman
   errors of size (Mp)^{1/2}. That is the polylog regime, beyond any known or standard-conjectural input.
4. **Uncapped weights (§11).** FIBRED Lemma 1.3 is a tautology. Uncapped weights would allow a power main term,
   but Cor 9.3 kills fixed-level Eisenstein main terms independently of the weights. Every rank-4 weight found
   here is capped.

**Verdict.** Spark (1) turned into a clean negative theorem (Thm 9.1), which is new as a formal statement in the
campaign as far as I know. Spark (2) became a precise statement of the required equidistribution, which sits in
the polylog regime. Spark (3) also turned out negative. No live route. ES is not proved.

**Remaining sparks.** (a) A main term with genus data at the place p (not n-local) plus a valid encoding. This is
FIBRED (E-b), and Cor 9.3 points there as the only exit. (b) Infinite shifted families `Σ_g σ(gn+1; −1, g)`
with weights in g chosen so that the g-sum telescopes; the numerics only covered fixed shifts. (c) Thm 9.1 for
general square classes r² mod L, which needs the B/A-coefficient induction.
