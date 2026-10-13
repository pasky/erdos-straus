# bsH_lubin_tate_sterile — the sterile point x*_c is a local Artin symbol at T (Lubin–Tate/Carlitz), i.e. a "T1 point with T1 removed" (O181)

**ES is not solved here.** Spark 3 of O177 ("non-archimedean anchors"). No script.

## Idea
Read FUNCTIONFIELD_ES2/3's sterile point x*_c (≡ 1 off T, ≡ 1 + cT at T; A = T²) through class field theory.
## Literature
Hayes 1974 (Gal(F(Λ_M)/F) ≅ (R/M)^*); Lubin–Tate theory for F_q((T)) with uniformiser T (the Carlitz T^∞-tower is
the Lubin–Tate tower); FUNCTIONFIELD_ES2 §0.1 (compactness criterion), §0.2; FUNCTIONFIELD_ES3 (O173).
## Statement (PROVED, class field theory)
R̂^* ≅ Gal(F(Λ_∞)/F) (Carlitz torsion of all levels). Under it x*_c = rec_T((1 + cT)^{−1}) (with Hayes' normalisation, in which rec_T(u) acts on Λ_{T^e} by u^{−1}; with
the opposite normalisation rec_T(1 + cT) — R181 repair D13): an element of the
**wild inertia group at T** (1 + cT ∈ U¹_T; rec_T of a unit acts trivially on every Λ_ℓ, ℓ ≠ T). O140's obstructed
point 1 is the identity. So "is x*_c covered by a linear family" = "is the Artin image of a principal unit at the
place T | A in some validity clopen".
## Dictionary to ℚ (Assessment)
The analogous points over ℚ are rec_2(u), u ∈ ℤ₂^*, at the place 2 | 4. Those with u ≡ 1 (8) are profinite squares,
limits of integer squares m², and are obstructed by T1 (Mordell / ET Prop 1.6). x*_c is likewise a profinite square
(1 + cT is a T-adic square, q odd). Over F_q[T] T1 is absent (degree parity unpinned, bsH_infinity_coordinate), so
Conjecture 0.2 asks whether a T1-point survives as an obstructed point *after* T1 has been removed.
## Barrier screen
No mechanism: the dictionary does not decide Conj 0.2 (FF3: lottery-like). B1 (clopen covering language).
## Assessment
Dictionary; promise 1. Spark: test whether the profinite squares as a whole meet O(3, T²) more often than random
points (closure of {Q²}).
