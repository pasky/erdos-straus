# bsA_hecke_cusp_excursions — QNR Hecke points, cusp geodesics and the large-deviation reading of λ(p) ≤ 3 (O174)

## Idea
Put the ball L_{≤3}(p) into homogeneous dynamics *with* the character, and look for an equidistribution theorem whose
conclusion lands in it.
**H1 (QR/QNR = split-torus orbits; PROVED, elementary).** The p + 1 index-p superlattices of ℤ² (Hecke points
z ↦ (z + A)/p, A ∈ 𝔽_p, and pz) are permuted by the diagonal torus {diag(k, k⁻¹)} ⊂ SL₂(𝔽_p) acting on 𝔽_p via A ↦ k²A.
On A ∈ 𝔽_p^* the orbits are exactly QR_p and QNR_p. So (A/p) = −1 picks out the non-identity orbit of the split torus
on the Hecke points.
**H2 (QNR Hecke points equidistribute; standard).** For smooth compactly supported f on SL₂(ℤ)\ℍ,
Σ_{A} (A/p) f((z+A)/p) is G(χ_p)·Σ_m χ_p(m) c_m(y/p) e(mx/p), with f's Fourier coefficients c_m. This is o(p) uniformly
on compacta (Weil/Deligne-type, or simply rapid decay of c_m), so each half equidistributes with a power saving.
**H3 (the ES event is a large deviation; PROVED dictionary + standard CF fact).** r(p/A) − 1 is the number of right turns
(R-blocks counted by length) of the cusp-to-cusp geodesic ∞ → A/p, i.e. the Series cutting sequence, equivalently the
Stern–Brocot path. The geodesic has length ≈ 2 log p in the thick part. r(p/A) = 3 means it is made of at most three long
cusp excursions of heights ≍ v, t, u with vtu ≍ p. Under the uniform measure on A this event has probability
|L₃(p)|/p ≍ log²p/p.

## Literature
Hecke-point equidistribution: Clozel–Oh–Ullmo (Invent. 2001), Chiu (1995) (from memory). Series, *The modular surface
and continued fractions* (J. LMS 1985; cutting sequences; from memory). Large deviations for CF digit sums
(Hausdorff-dimension spectrum; Iommi–Jordan; from memory).

## Barrier screen
* **B3/B6, in dynamical form.** Equidistribution with power saving p^{−δ} cannot detect an event of measure p^{−1+o(1)}.
  The indicator of "≤ 3 excursions" is not a fixed test function. It is a cylinder in the space of geodesics whose
  measure shrinks like 1/p, so even the best possible rate (p^{−1/2}, square-root cancellation) misses it by p^{1/2}.
  This is exactly the PARITY_FIXED_P "Weil falls short by p^{1/2}" gap.
* The modification that violates "fixed test function": thicken the event to R(p) excursions with R → ∞. This is
  memo bsA_farey_lnr_pigeonhole. One needs R ≍ ln p ln ln p before the event has positive measure, and then the
  conclusion is pigeonhole-trivial and has no ES meaning.
* Shrinking-target theorems (Kleinbock–Margulis logarithm laws) handle targets of measure ≫ (log p)^{−C} along *one*
  orbit. Our targets have measure p^{−1+ε} over a family of p orbits, so this is also out of range.
* T1: at n = m² the "QNR orbit" is empty in the Jacobi sense, consistent.

## Cheap numerics
Covered by `bsA_profile.py`. QNR fractions at small HJ length differ from 1/2 (0.70 at r = 3, 0.41 at r = 5). This is
the expected failure of uniform-distribution heuristics on tiny cylinders: the cylinders are arithmetic, and the mod-8
cell law of Cor 4.1 governs them.

## Assessment
Clean dictionary (QNR = split-torus orbit; λ(p) ≤ 3 = a three-excursion large deviation of a QNR Hecke geodesic). It
places ES precisely at the measure-p^{−1} scale, where dynamics gives nothing. Promise 0/5.
