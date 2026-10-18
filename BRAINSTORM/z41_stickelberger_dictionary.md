# z41_stickelberger_dictionary — forcing sees the Stickelberger component, ES needs the norm component (O272; §3, Thm 3.2)

**Idea.** Write the Frobenius of a split prime ℓ at the level prime 𝔮 | q as a vector x_a = (σ_aλ/𝔮)_m, a ∈ (ℤ/m)^×. Which
linear form of x does the forcing (q mod ℓ) see, and which one does the ES event (ℓ mod q) need?
**Literature.** Cubic/biquadratic reciprocity (Ireland–Rosen Ch. 9); Eisenstein reciprocity and Stickelberger
(Ireland–Rosen Ch. 14; Lemmermeyer, *Reciprocity Laws*, Ch. 11); Burde's rational quartic law (as the m = 4 shadow).
**Result (PROVED, m = 3, 4).** Forcing: S = (q/λ)_m = ±∏ x_a^{a⁻¹} (Stickelberger-weighted). ES: D = ψ_𝔮(ℓ) = ∏ x_a (norm).
D/S = ±∏ x_a^{1−a⁻¹}; the exponents generate gcd(2, m)ℤ/m, so S determines D exactly modulo μ_m^{gcd(2,m)}: the
quadratic layer for m even, nothing for m odd. For m = 2 (K = ℚ) S = D — the BM layer and T1 in one line.
**Barrier screen.** No new barrier is bypassed; this explains why (J)93/(J)96 see only quadratic data. T1: squares make S
trivial; for m = 2 that is D, for m ≥ 3 it is an anti-cyclotomic Hecke datum, ES-invisible.
**Cheap numerics.** `scripts/z41_stickelberger.py`: (q/λ)₃ = x₁x₂² on 882/882 pairs; S constant on forced progressions,
D uniform (≈ 1/3 cubes) for n = cubes, squares, generic.
**Assessment.** PROVED (classical reciprocity; the dictionary is new as packaging for ES). A clean reason T1 is quadratic only.
