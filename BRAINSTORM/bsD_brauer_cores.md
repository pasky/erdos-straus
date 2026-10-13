# bsD_brauer_cores — order-m Brauer classes on the ES surface exist over ℚ(μ_m), and corestriction kills them on ℚ-points (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. Script `scripts/bsD_cubic_symbol.py`.

## Idea
Orchestrator's direction (a): T1 is the reciprocity Σ_v inv_v(α(u)) = 0 for Bright–Loughran's quaternion class α
(BL Thm 1.2 = Diff-parity, (J)13). A *degree-m* cyclic class would carry local invariants in (1/m)ℤ/ℤ and could
force an order-m ("ray") condition. On the ES surface such classes really exist: BL Prop 2.5 gives
`Br Ũ_{n,k̄} ≅ ℚ/ℤ(−1)` and Prop 2.6 says that over any field k, `Br Ũ_n / Br k` is represented by the cyclic algebras
`α_ζ = (−u₁/u₃, −u₂/u₃)_ζ, ζ ∈ μ(k)` (checked against `sources/bright-loughran-1908.02526.pdf`, §2). Over
K = ℚ(ζ₃) there is an order-3 (indeed order-6) transcendental class: the cubic norm-residue symbol of the two ratios.
Question: does its reciprocity law constrain the integral points of 𝒰_n?

## Literature
Bright–Loughran, *Brauer–Manin obstruction for Erdős–Straus surfaces*, arXiv:1908.02526 (Prop 2.5, 2.6, Cor 2.7,
Thm 1.6: `Br U_n/Br ℚ ≅ ℤ/2`); Colliot-Thélène–Skorobogatov, *The Brauer–Grothendieck group* (2021), §3.8 (restriction–
corestriction, cores∘res = multiplication by degree) and the compatibility of evaluation with corestriction;
Neukirch–Schmidt–Wingberg, *Cohomology of Number Fields*, (7.1.4) (inv_ℓ ∘ cores_{K_w/ℚ_ℓ} = inv_w).

## Statement
**Theorem 1 (corestriction collapse; PROVED relative to BL Thm 1.6).** Let n ≥ 2, K/ℚ a number field, β ∈ Br U_{n,K}.
For every prime ℓ (or ℓ = ∞) and every u ∈ U_n(ℚ_ℓ),
`Σ_{w | ℓ} inv_w β(u) = inv_ℓ β₀ + ε·inv_ℓ α(u)`, where `cores_{K/ℚ} β = β₀ + εα`, β₀ ∈ Br ℚ, ε ∈ {0, 1}.
If β has odd order, ε = 0 and the ℓ-total is **constant** on U_n(ℚ_ℓ). Hence on ℚ-points (in particular on 𝒰_n(ℤ))
the reciprocity law `Σ_v inv_v β(u) = 0` of *any* Brauer class over *any* number field carries, beyond constants,
only the BL quaternion class α, i.e. only T1 / Diff-parity.
*Proof.* For u ∈ U_n(ℚ_ℓ), base change gives u_K ∈ U_n(K ⊗ ℚ_ℓ) = ∏_{w|ℓ} U_n(K_w), and evaluation commutes with
corestriction along the finite étale map U_{n,K} → U_n: `cores_{K⊗ℚ_ℓ/ℚ_ℓ}(β(u_K)) = (cores β)(u)` (CT–S §3.8).
Apply inv_ℓ and inv_ℓ ∘ cores_{K_w/ℚ_ℓ} = inv_w. By BL Thm 1.6 `cores β ∈ Br U_n = Br ℚ ⊕ ℤ/2·α`; for β of odd order
m, cores β is killed by m, so its α-component (2-torsion) vanishes. ∎
**Explicit form (PROVED, elementary).** For K = ℚ(ζ_m), m odd, ℓ ≡ 1 (m) and u rational, BL's relation
`a·α_ζ = α_{ζ^{a⁻¹}}` and Galois-equivariance give `inv_{σ_a w} α_ζ(u) = a·inv_w α_ζ(u)`, so the ℓ-total is
`x·Σ_{a∈(ℤ/m)^×} a ≡ 0 (mod 1)` (as Σ a = mφ(m)/2 and φ(m) is even for m ≥ 3); other ℓ are covered by Theorem 1. The individual value
x = inv_{w₀} α_ζ(u) is a genuine, non-constant function on solutions (numerics below) — the information exists, but
no global law constrains it.

## Barrier screen
* **T1**: Theorem 1 says T1 (= α) is the *only* reciprocity on 𝒰_n, over every base field. A "cubic T1" from the
  surface is impossible. Consistent with CONJECTURE SQ (Type I/II empty ⟺ square, no "cube" obstruction).
* **Hypotheses of Theorem 1 → escape attempts.** (i) *The class lives on U_n itself.* Classes on auxiliary varieties
  (certificate spaces, families over n) can have arbitrary order — but their evaluation on ES data factors through
  the splitting fields of the certificate's divisor conditions, which are quadratic (bsD_frobenius_closure). (ii)
  *Points are ℚ-rational.* Over ℤ[ζ_m]-points the order-m classes are live (BL Thm 1.8 analogues), but ES needs
  ℚ-points. (iii) *Evaluation on single points.* Using the individual component x at one w | p (not the sum)
  escapes Theorem 1 but has no reciprocity law — it is just a cubic residue symbol, a lottery variable.
* B2/B6: not engaged (no existence claim).

## Cheap numerics (EVIDENCE)
`scripts/bsD_cubic_symbol.py 600` (0.5 s): for all 50 primes p ≡ 1 (3), 7 ≤ p < 600, the cubic tame symbol of
(−x/z, −y/z) at a prime above p is **non-constant** over the ES solutions (all three cube classes occur, e.g. p = 79:
13/12/12), while the sum over w | p is identically 0 (Theorem 1).

## Assessment
PROVED obstruction with exact scope: **no higher-order reciprocity on the ES surface over any number field beyond
T1** (Theorem 1). The order-m BL classes are real but corestrict to constants on ℚ-points. Promise 1 (clean negative
answer to direction (a) on the surface; novelty: the ℚ/ℤ(−1) structure is BL's, the corestriction remark is ours,
elementary).
