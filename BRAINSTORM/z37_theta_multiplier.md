# z37 — Rickards–Stange's Kronecker character is the theta multiplier on the positive semigroup (O267) — SHARP candidate

## Idea
Explain *why* RS's Ψ = {γ ∈ Γ₁(4)_{≥0} : (a/b) = 1} is a semigroup and why the method fails for groups (RS §10,
Question 10.1), by recognising σ(γ) = (c/d) as the multiplier of θ(z) = Σ e(m²z) on Γ₁(4).

## Literature
RS arXiv:2401.01860v3 Lemma 3.1, (3.0.1), §10; Shimura (Ann. Math. 1973) / Koblitz GTM 97 IV §4 (θ(γz) =
ε_d^{−1}(c/d)(cz+d)^{1/2}θ(z), γ ∈ Γ₀(4)); Kubota 1969 (metaplectic cocycle); arXiv:2510.21702 §1 (suggests
metaplectic covers as the general explanation of reciprocity obstructions). Not found stated in RS or its citers.

## Content (QUESTION_R Thm 1.5, PROVED from the classical theta law)
σ(γ₁γ₂) = σ(γ₁)σ(γ₂)·w(γ₁, γ₂), w = archimedean square-root cocycle, and w = 1 on non-negative matrices (z = iy,
y → 0⁺). So σ is a homomorphism of Γ₁(4)_{≥0}, Ψ = ker σ; σ is not the restriction of a homomorphism of
Γ₁(4) = ⟨T, L⁴⟩ (σ(T) = σ(L⁴) = 1, σ([[5,2],[12,5]]) = −1). The obstruction to extension is exactly the real place.

## Barrier screen
T1/B5: this is the conceptual source of the square obstruction (θ is supported on squares; positivity kills w).
Matches the campaign's "positivity / archimedean sign" theme ((J)52, (J)55). B1–B4, B6: not a route, a dictionary.

## Cheap numerics
`scripts/z37_dictionary.py`: 20 000 random positive Γ₁(4) products, 0 failures of multiplicativity or (c/d) = (a/b).

## Assessment
PROVED (classical input), presumably folklore-level, but it answers RS §10's informal remark precisely and gives the
natural home for reciprocity obstructions: kernels of metaplectic multipliers restricted to positive cones. Spark: for
HKRS's quartic obstructions, the analogue would be a quartic (Kubota) multiplier on a positive cone in SL₂(ℤ[i]).
