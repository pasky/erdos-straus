# z23 — at most one forced slot per Type II point (O251; z21_window_vs_slice spark)

## Idea
A Type II point has a window (m, x) and two slices (g, h), (D, h_D). A slot is forced at ℓ | modulus if the coordinate
is a non-residue mod ℓ (then −1 ∈ ⟨coordinate⟩, CAP_POINTWISE Thm 1.1's group step). Could a point with two forced
slots be forced to exist?
## Literature
CAP_POINTWISE Thm 1.1, CAP_DOWN Thm 1.2; ASTRA_BRIDGE Prop 5.1.
## Barrier screen
LATTICE_MEETING Prop 3.1: 4h ≡ 1 (mod g) makes every slice unforced at *every* prime of g (also composite g); the window
is forced at ℓ | m iff (p/ℓ) = −1 (4x ≡ p). Type I levels: 4H ≡ 1 (mod e), unforced. So ≤ 1 forced slot, structurally.
H-B (parity at fixed p) would need a non-quadratic slice invariant (4-rank, Rédei), about which nothing is proved
here (Cor 1.5 is only norm-dependence of E; WINDMILL 10.3 only limits class functions of N𝔞 mod t; R262 repair M1).
## Cheap numerics
None (identities). Note: Prop 3.1 is near-definitional (slice coordinates are 4⁻¹ mod the modulus).
## Assessment
PROVED (negative). The "two forced slots" mechanism does not exist in Type II/Type I as defined.
