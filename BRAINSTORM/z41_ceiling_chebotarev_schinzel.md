# z41_ceiling_chebotarev_schinzel — the forcing t ≡ −n⁻¹ (ℓ) reaches exactly the quadratic layer (O272; TWO_POWER_LADDER §3)

**Idea.** SPARKS9 Prop 2.2 frees the BM character χ_{−t} at a forced prime ℓ | tn + 1 because (−t/ℓ) = (n/ℓ). Climb: do
characters of order 4, 8, … (or 3) mod t at ℓ become functions of n along the forced progression of levels?
**Literature.** Chebotarev in composita; Kummer theory; A. Schinzel, "Abelian binomials, power residues and exponential
congruences", Acta Arith. 32 (1977) 245–274 (abelian criterion for x^m − a); Burde, J. reine angew. Math. 238 (1969)
(rational quartic reciprocity, correction term from sum-of-squares representations); in-repo: CLASS_FORCING Thm 2.1, z33_kummer_shadow.
**Result (Thm 3.1, PROVED; ℓ ∤ m, 4 | lcm(M, m) for m even).** For t = 4q, q ≡ 1 (m) prime in any progression mod M (ℓ | M), the
events "ℓ ∈ F_q^{×e}" have density 1/e (m odd) resp. 2/e given (ℓ/q) = 1 (m even) — equivalently, averaged over pairs (q, 𝔮),
ψ_𝔮(ℓ) is equidistributed on μ_m resp. the fibre. Reason: K(ℓ^{1/d})/ℚ abelian ⟹ d | 2 (direct commutator argument with
complex conjugation; Schinzel's criterion as first cited was misstated, repaired in self-review).
**Barrier screen.** B1/(J)93: this IS (J)93's "abelian = congruence" in level coordinates (roles of fixed and moving prime
swapped) — not new as mathematics. B2 untouched. T1: consistent (squares are exactly the m = 2 forced layer).
**Cheap numerics.** `scripts/z41_ladder_test.py`: e mod 2 constant on 24/24 progressions; 4th powers ≈ 1/2, 8th ≈ 1/4 given
the quadratic part, for n = 7, 13, 73, 101, 131, 241, 9, 25, 49.
**Assessment.** PROVED negative with exact scope (fixed n, ℓ; one varying level prime): the 2-power ladder above BM is NOT
forced by n through the forcing congruence.
