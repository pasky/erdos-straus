# Markoff Hasse failures (Ghosh–Sarnak) vs Erdős–Straus: why the mechanisms do not transfer (O143, memo 2)

Labels as in DISCOVERIES.md. Scripts: `scripts/bs_cubic_markoff_hp.py` (Markoff h(k), k ≤ 2·10⁵),
`scripts/bs_cubic_fclass.c` + `scripts/bs_cubic_fclass_stats.py` (all ES solutions of 4/p, 10⁵ < p < 1.3·10⁵).

## 1. Idea
In the family of Markoff surfaces V_k: x²+y²+z²−xyz = k, Ghosh–Sarnak (GS) prove that the integral Hasse
principle (HP) holds for almost all k and fails for infinitely many k. The failures are built near the Cayley
member k = 4. The ES surface *is* a Cayley cubic (memo 1), and the redteam lists the GS result as the cautionary
hatch H-F. Question: can the GS failure mechanism be transported to ES, either to produce a counterexample or to
explain why there is none? And can GS's "almost all" technique be sharpened toward all primes?

## 2. Literature anchor (GS read directly: arXiv:1706.06712v3, §§1, 8, 10)
* Thm 1.1: Markoff descent. Every integral point is Γ-equivalent to a unique point of a compact fundamental set
  F_k^±, so h(k) := |F_k^±(ℤ)| is a class number.
* (1.6): Σ_{|k|≤K} h(k) ∼ C K (log K)².
* Prop 8.1 (failures): k = 4 ± 2ν², with ν having prime factors in specific classes mod 8 (and (iii): 4 + 2ℓ²). The
  proof uses the identity (2x₃ − x₁x₂)² − (x₁²−4)(x₂²−4) = 4(k−4). When 4(k−4) = ±8ν², every prime q ∤ ν dividing
  x₁²−4 must have (±2/q) = 1. Choosing ν then rules out all candidate classes.
* Remark 1.3: LM20/CTWX20 explain (i) and (ii) by integral Brauer–Manin; (iii) also uses descent (size bounds
  in F_k) and is not BM.
* §10, Table 3: 12.976% of admissible k ≤ 100800 are failures. Conj 10.2: the number of failures up to K is
  ∼ C₀K^θ with θ ≈ 0.89.

## 3. Findings

**F1 (EVIDENCE; validation).** Our enumeration of F_k⁺(ℤ) reproduces GS Table 3 exactly: **12.98%** failures
among admissible k ≤ 100800 (12.62% for k ≤ 2·10⁵). Admissibility was checked by brute force mod 8, 9 and the
primes ≤ 47; GS's "exceptional" k were removed.

**F2 (EVIDENCE).** Markoff counts behave like Poisson(λ(k)) with λ(k) proportional to the truncated singular
series S(k) = ∏_{ℓ ≤ 47, plus 8, 9} #V_k(ℤ/ℓ)/ℓ². Generic k ∈ [10⁵, 2·10⁵], binned by sextiles of S:

| S bin | mean h | failure rate | Poisson e^{−mean} |
|---|---|---|---|
| < 0.125 | 0.15 | 0.863 | 0.86 |
| 0.125–0.258 | 0.46 | 0.637 | 0.63 |
| 0.258–0.564 | 1.09 | 0.353 | 0.34 |
| 0.564–1.22 | 2.38 | 0.094 | 0.093 |
| 1.22–2.40 | 4.67 | 0.013 | 0.009 |
| > 2.40 | 9.89 | 0.0004 | 0.00005 |

corr(log S, log(1+h)) = 0.81. The numerical failures, ≈ K^{0.89} of them, are therefore explained by a small
mean (≈ 0.019 log²k) **times a widely fluctuating product of local densities**. The algebraic families of
Prop 8.1 are a √K-thin sub-phenomenon.

**F3 (PROVED, elementary). ES local densities are n-flat.** For a prime ℓ ∤ n, including ℓ = 2 when n is
odd, u ↦ u/n is an isomorphism of integral models 𝒰_n ≅ 𝒰_1 over ℤ_ℓ: the equation 4u₁u₂u₃ = n e₂(u)
becomes 4v₁v₂v₃ = e₂(v) after u = nv, and n ∈ ℤ_ℓ^×. Hence #𝒰_p(ℤ/ℓ^k) = #𝒰_1(ℤ/ℓ^k) for every ℓ ≠ p. The
real density is also p-independent after scaling, and BL's class α has inv_ℓ ≡ 1 for ℓ ∤ 2p (BL Lemmas 3.5, 3.8).
So **any adelic main term for f(p)** (Hardy–Littlewood, or Brauer-weighted à la Colliot-Thélène–Xu) is
independent of p mod ℓ for every ℓ ≠ p. Its only p-dependence is through the p-adic factor, a function of p alone.

**F4 (EVIDENCE). The true ES counts depend strongly on p mod 840.** All 2567 primes 10⁵ < p < 1.3·10⁵, total
count f = f_I + f_II (ordered x ≤ y ≤ z):

| #{conditions (p/3)=(p/5)=(p/7)=1, p ≡ 1 (8)} | 0 | 1 | 2 | 3 | 4 (square classes) |
|---|---|---|---|---|---|
| mean f/log³p | 0.181 | 0.169 | 0.144 | 0.110 | 0.053 |
| min f/log³p | 0.085 | 0.068 | 0.061 | 0.040 | 0.028 |

The class means mod 840 run from 0.050 (p ≡ 1) to 0.697 (p ≡ 839), a factor of about 14. The six lowest classes
are exactly the square classes {1, 121, 169, 289, 361, 529}, in agreement with POINTWISE_TYPEII_SPECTRAL for f_II.
Both types are depleted: the ratio "others/square" is 3.1 for f_I and 2.2 for f_II.

**Consequence (F3 + F4; Assessment of interpretation).** ES is the *opposite* of Markoff. Markoff's count is
governed by local densities (F2), and that is where its failures come from. ES's local densities are flat (F3),
yet its counts carry a ×14 main-term dependence on p mod 840 that **no adelic or Brauer–Manin main term can
see**. This is a quantitative form of BL Thm 1.9 (strong approximation fails even with Br): the integral points
of 𝒰_p are not Haar-equidistributed in ∏_ℓ 𝒰_p(ℤ_ℓ), and the bias is of size O(1) × main term. Its source is
the slice structure: small e-slices (Mordell/identity families, B1) succeed or fail according to p mod e,
because e is a coordinate of the solution (B2: "the modulus is part of the solution").

**F5 (PROVED; transport of the GS mechanism).** Under the dictionary of memo 1, the analogue of GS's fibration
identity for ES is ((4u₁−n)u₂ − nu₁)((4u₁−n)u₃ − nu₁) = (nu₁)². Its right-hand side is always a **perfect
square**, i.e. the "k = 4" case of GS's identity, where 4(k−4) = 0. A square is a norm from every quadratic
field, so the step "every prime q | x₁²−4 must have (2ε/q) = 1" has no ES analogue: the per-fibre reciprocity
condition is vacuous. The only reciprocity content of ES is BL's transcendental α, which is never an
obstruction for n = p (BL Thm 1.8). Hence:
* GS-(i)/(ii)-type (BM) failures cannot occur for ES at n ≥ 2 (this is BL Thm 1.8 again);
* a GS-(iii)-type failure (reciprocity + size) would need a reciprocity constraint that kills every slice up to a
  size bound. On Type I, α forces (−d/p) = −1, and this kills small levels exactly at square-mimicking primes.
  But on Type II, α is automatic (GEOMETRY_ES Prop 5.2), and no size bound confines d.

So the GS construction fails at the Type II step. This is the ES "escape" that Markoff lacks, and it agrees with
the campaign's EVIDENCE that the hardest primes still have f ≥ 0.028 log³p.

## 4. Barrier screen
* **B1 / B2.** GS's existence method ("M is full", Thm 1.2(ii)) restricts to a region R with x₁ ≤ (log K)^A, where
  each fibre is a binary-form representation problem. It is a slice method with growing slice set, run on
  average over k. Pointwise, it is the B2 lottery: the fibres have expected count O(1).
* **B6 / T7.** GS's existence result is a variance bound averaged over k. For ES, "almost all n" is already
  known (Vaughan-type), so nothing is gained. F4 shows moreover that a variance argument comparing f(p) with any
  adelic main term would carry an error of the same order as the main term in the square classes (factor ≥ 3):
  the comparison function would itself need the non-adelic mod-e slice main terms. **T2** fails.
* **B5 / T1.** Everything here is about prime n. F3 holds for every n coprime to ℓ (also odd squares); F4 is
  EVIDENCE only.
* **B3.** No main term ≤ p^{o(1)} is produced.

## 5. Viability Assessment
**COLLAPSES (as a route to ES) to B2/B6.** GS's positive result is an average (T7), and its failure mechanism
needs a non-square right-hand side that ES does not have (F5).
**By-products:**
* (PROVED) F3, local flatness;
* (PROVED) F5, the exact reason the Markoff/Cayley reciprocity failures do not transport (the RHS is a square;
  Type II is genus-free);
* (EVIDENCE) F2: Markoff h(k) ≈ Poisson(c·S(k)·log²k), reproducing GS Table 3;
* (EVIDENCE) F4: the ES counts carry a ×14 *non-adelic* main-term bias mod 840.

Together, F3 and F4 sharpen redteam hatch H-F: in Markoff, "geometry delivers almost all" because the count is
adelic. In ES the count is not adelic, so neither the GS failure mechanism nor the GS existence mechanism applies.

Possible next step (not taken): fit f(p) to Σ_e (slice main terms depending on p mod e) and check whether the
residual is Poisson. That would quantify how much of the ES count is "slice-local" vs genuinely random. It is
EVIDENCE-only work and does not lead to a proof.
