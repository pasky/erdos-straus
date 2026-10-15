# R234 — hostile review of O233 (GLOBAL_FANO.md, BRAINSTORM/z9_*.md)

Reviewer: R234 side agent. Scope: brief items 1–10. Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim-by-claim

### C1. Thm 1.1 / z9_frobenius_layers Lemma 1 (loops = representations of 2; r_L(m) for m < p/4)
Re-derivation (reviewer, independent):
* Trace-zero step. O = End E maximal in B_{p,∞}; P = {x ∈ O : p | nrd x} is the unique two-sided prime over p, and x̄ = trd x − x ∈ P
  for x ∈ P, so trd x ∈ P ∩ ℤ = pℤ. With nrd x = mp, |trd x| ≤ 2√(mp) < p ⟺ m < p/4. So all such x lie in E⁰ and CONSTRUCTIVE_ES
  Prop 3.1 gives r_L(m) = #{x ∈ End(E, C) : nrd x = mp}. Correct.
* (r_L(2) > 0 ⟹ loop.) ε ∈ End(E, C), ε² = −2p (needs 2 < p/4, i.e. p ≥ 11 among p ≡ 1 (4): p ≥ 13). ε(C) ∈ {0, C}; ε(C) = C is
  impossible because ε² = −2p kills E[2]. deg ε = 2p and E[p] = 0, so the inseparable degree is exactly p; writing ε = σ∘π_p
  (σ separable of degree 2), ker ε(𝔽̄_p) has order 2 and contains C, so equals C; hence ε = θ∘φ_C with θ: E/C → E of degree p and
  trivial point kernel, so θ = (iso)∘Frobenius and E ≅ (E/C)^{(p)}, i.e. E/C ≅ E^{(p)} (j ∈ 𝔽_{p²}). Correct.
* (loop ⟹ r_L(2) > 0.) E/C ≅ E^{(p)}: ε = ι∘π∘φ_C kills C, degree 2p, trace 0 by the step above. E/C ≅ E with j ∉ 𝔽_p: φ_C gives
  a degree-2 endomorphism, disc ∈ {−4, −7, −8}, all class number 1 and maximal, so by Deuring lifting j ∈ {1728, −3375, 8000} ⊂ 𝔽_p;
  contradiction. Correct. (Loop-ness is w₂-invariant, so it is a property of the class in 𝔊⁻_p, as needed.)
* Side claim "edges representing both 1 and 2 are ⟨1⟩ ⊥ [[2, 1], [1, (p+1)/2]] = word (1, (p+3)/2, 3)": re-derived — a norm-1
  vector splits, L = ⟨1⟩ ⊥ M; a norm-2 vector is either (±1, m) with Q(m) = 1, giving ⟨1, 1, p⟩ (isotropic at p for p ≡ 1 (4),
  so not in 𝔊⁻_p), or lies in M, giving M ≅ [[2, 1], [1, (p+1)/2]]; this class is in 𝔊⁻_p iff (−2/p) = −1 iff p ≡ 5 (8).
  So the "79" is just the number of primes p ≡ 5 (8) in [5, 2000] (see recount below). Correct.

From-scratch recertification (`scripts/review_r234_lib.py`, `review_r234_loops.py`, `review_r234_quat.py`; no z9/ce code):
classes of det p enumerated from Minkowski-type reduced Grams and canonicalised by successive-minima bases; 𝔊⁻_p selected by the
p-adic test (−d/p) = −1 on the binary quotient of L/pL; class counts reproduce 4, 7, 9, 15, 69 at p = 37, 73, 97, 193, 1009.
Loop test on the lattice side = isometry of the two vertex overlattices L + ℤx/2 (maximal-order types = j up to Frob).
