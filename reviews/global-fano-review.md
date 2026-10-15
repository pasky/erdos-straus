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

### C2. Thm 2.1 / z9_depth_walks Lemma 1, Cor 2, Prop 3 (depth = conic-marked walk)
Re-derivation (reviewer):
* Vertex step. F = F_j has Q integral, B half-integral, det_B F = p/4, so b = 2B mod 2 on F/2F is alternating of rank 2 with
  radical r, and q(r) = 1 (else F + ℤr/2 would be integral of det p/16). A hyperplane H ⊂ F/2F is classical (B|H integral) ⟺
  b|H = 0 ⟺ r ∈ H (if r ∉ H, b|H is the nondegenerate quotient form). The 3 hyperplanes through r are {0, r, c, c + r} with
  q(c + r) = q(c) + 1, so each contains exactly one of the 3 conic points: hyperplanes ⟷ conic points. Hence "unique classical
  index-2 sublattice through z′" holds iff z̄′ ≠ r; the conic marking (q(z̄′) = 0) is one sufficient way to exclude r.
* Reviewer addition: for a *primitive* x with 4 | Q(x), x/2 is **never** ≡ r in F₁/2F₁ (r ≡ x/2 would force B(x, L) ⊂ 2ℤ, i.e.
  x ∈ 2L at 2, contradicting primitivity). So **without the marking every pointer has a unique continuation** — confirmed
  numerically: all 720 depth-2 pointers (p ≤ 200) have exactly one unmarked classical continuation through x/2. This strengthens
  the author's repair (the unmarked walk never stops at the first vertex, so the marking is not merely "needed in one example",
  it is the whole content of the step count).
* Step count: edge→vertex from L_j needs k − 2j + 2 ≥ 2, vertex→edge from F_j needs k − 2j ≥ 1; ⌊k/2⌋ + ⌊(k−1)/2⌋ = k − 1. Correct.
  Non-backtracking and primitivity arguments are correct (odd-prime primitivity is unaffected by 2-power index changes).
* Cor 2: k ≥ 3 ⟺ 8 | Q(x) ⟺ marked walk ≥ 2 half-steps — a restatement (near-tautological once Lemma 1 is in place); its content
  is the reading "two distinct edges at F₁ = non-backtracking 2-path = cyclic 4-isogeny", which is correct. Wording "a point of
  X₀(4)" is fine as a datum of G_p (Deuring), not a CM statement.
* Prop 3 (i)–(iii): correct as stated (v₂A + v₂A* = v₂(AA*) = v₂(tp + 1); f, f* are the two distinct even classes of FOUR_ADIC
  Lemma 1.1, so if both are isotropic they are the two isotropic classes and point at different overlattices; total s − 2).
  Examples re-checked by hand: 293 = 3·37·3 − 40 (A = 110, A* = 8, split (1,3) ∈ S₈); 293 = 3·7·15 − 22 (A = 20, A* = 44, split
  (2,2) ∉ S₈); 97: (2, 7, 8) ∈ S₈ (8 | v), (2, 20, 3) ∉ S₈; 131: s(t) = 2, 1, 4, 1, 2, 1, 3 for t = 1, 3, …, 13; (5, 1, 33): A = 4,
  A* = 164 = 4·41. All correct. Labels PROVED are justified (elementary).

From-scratch certification (`scripts/review_r234_depth.py`; own HNF/sublattice code; asserts: z primitive in L_j, det(F_j) = p/4,
det(L_{j+1}) = p, exactly 3 classical index-2 sublattices of F_j, exactly one through z′, no backtracking): **all 1190 pentagon
pointers of all χ = −1 words, odd primes 5 ≤ p ≤ 200, 0 violations, walk length = k − 1** (1196 including p = 3; 368 for p ≡ 1 (4)).
The author's "1190" is over all odd primes 5..200, not only p ≡ 1 (4) — say so (MINOR, D-list).

**Verdict C2: SOUND** (with the MINOR wording items below).
