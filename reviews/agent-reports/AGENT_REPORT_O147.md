# AGENT_REPORT_O147 — brainstorm: non-abelian / arithmetic-topology / homogeneous-dynamics angles

Branch `side-agent/bs-nonabelian`. Three memos are in `BRAINSTORM/`, with scripts `scripts/bs_nonab_{frob,points}.py`
and log `logs/bs_nonab_frob_4e6.txt`. None of the memos is LIVE, and ES is not solved.

**(a) `BRAINSTORM/nonab_frobenius_redei.md`: COLLAPSES (B2 at D1; B1/B5 at D2/D3).**
* Strongest reason (D1, PROVED, elementary). In the e-slice form, every ES slice event says that (a)(b)⁻¹,
  built from prime factors of N_e, has Artin symbol equal to complex conjugation in ℚ(ζ_e)/ℚ. That is
  abelian Frobenius data of the factors, so non-abelian invariants of p (Rédei symbols, spin, 4-/8-ranks,
  quartic/cubic residuacity) have no slot to enter. At most they can *choose* θ, which is a finite rule
  set and so falls under Thm 2.2(iii).
* D2 (PROVED). Every fixed non-abelian Frobenius condition also holds at suitable odd squares ℓ², via
  composition in the principal genus and (a/m²)_k = (a/m)_k². So it passes T1 and cannot be the step that
  fails there.
* D3 (PROVED relative to Chebotarev + Mordell). Frobenius-gated identity coverings fail. This settles the
  identity-level case of POINTWISE_SIZE E3. Procedure-level E3 is CONDITIONAL on H_K. The Cornacchia/E2
  channel is only sketched.
* EVIDENCE: 35k primes p ≡ 1 (24) below 4·10⁶. The Type II window count shows no dependence on four
  non-abelian Frobenius splits (≤ 2σ), while the abelian control p mod 16 shows ≈ 40σ.

**(b) `BRAINSTORM/nonab_homogeneous_dynamics.md`: COLLAPSES to B3 at "error ≤ main term" (Lemma B).**
* The fixed-p fibre has polylog mass. Every effective equidistribution or counting theorem (EMM, DRS/EM,
  Duke, COU, Benoist–Oh, thin-group expansion) has power-of-complexity errors. The fixed-p target has
  complexity ≥ p^c: a modulus as large as the coordinate on X_d, and shell width (dp)^{−1/2}.
* Averages over discriminants or Hecke operators are T7 leaks.
* By-product, Prop P (PROVED, elementary): K := ℤ̂ ∖ ⋃(Type I/II witness classes) ⊆ Sq̄ would imply ES.
  - It escapes Theorems M/C only because the cover is non-compact.
  - It is falsified if the campaign's candidate x** (a non-square at 11) is sterile (CONJECTURE).
  - Otherwise it is just B1.

**(c) `BRAINSTORM/nonab_motivic_pointcounts.md`: COLLAPSES at "attach a non-trivial Galois representation".**
* Prop 3.1 (PROVED, elementary): #U_n(𝔽_ℓ) = ℓ² + 1 for every ℓ ∤ 2n, independent of n. For ℓ | n it is
  3ℓ² − 3ℓ + 1.
* So the motive of the ES surface is constant mixed Tate, and trace-function, Katz or ℓ-adic routes have
  no input object (consistent with GEOMETRY_ES's toric model).
* Sub-idea, cubic residues (EVIDENCE): odd cubes 27, …, 3375 do have Type I/II solutions. So T1 is purely
  quadratic, and higher residue symbols give neither a hidden obstruction nor a hidden sufficiency.

**Untested next step (if the parent wants one more H-D check).** For Type II solutions, compute the
class of the associated Heegner form of disc −4dp modulo Cl⁴ (a Rédei-symbol quantity). Then test
whether it is forced beyond the known genus lemma (p/f) = −1. Expectation (Assessment): it is
equidistributed within the forced genus, by D1 and O131 Thm 5.2 (dihedral data have coefficient 0).
Not run, to save context.

Novelty of all by-products: modest; Prop 3.1 is probably folklore.
