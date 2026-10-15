# z8_numerator_sign_fields — the ν-sign field ℚ(ζ_{νu}, √−u) and why full T1 ⟺ 4 | ν (O232)

**Idea.** O225 read a 4-word (χ = −1) as "Frob_A = complex conjugation in Σ_u = ℚ(ζ_u, √−u)". For a numerator ν the
five slots ν | t, u, v, A, A* (each gives ν/n = 1/x + 1/y + 1/z) become a Frobenius set C_ν ⊂ Gal(ℚ(ζ_{νu})/ℚ); T1 is the
statement that C_ν avoids the subgroup fixing √−u.

**Literature.** (J)46 SHARP 2 (full T1 ⟺ 4 | ν, via ET §4 / Schinzel Funct. Approx. 28 (2000)); DEDEKIND_ES Thm 4.5;
NEAR_SQUARE_EXIST Thm 2.1; FOUR_SPECIFIC Prop 1.1 ((−M/g) = −1 for g ≡ −1 mod M ⟺ M ≡ 0, 3 mod 4).

**Barrier screen.** It is a description (dictionary), not an existence mechanism: B2 (divisor in a class) is unchanged —
the word still needs a divisor of n + u with prescribed Frobenius. T1: consistent by construction (Thm 2.2).

**Cheap numerics.** `scripts/z8_numerators.py 2000 60 3 4 5 7 8 11 12`: slot identities exact; coprime classification
(Prop 2.1) holds on every word; ν-words at odd squares: 0 for ν ∈ {4, 8, 12}, many for ν odd, all coprime odd-A violators
at levels with √−u ∉ ℚ(ζ_{νu}).

**Assessment.** PROVED (SIGN_FIELDS Prop 2.1, Thm 2.2): t-slot T1 at level u ⟺ √−u ∈ ℚ(ζ_{νu}) (odd A), and this holds for
all u ⟺ ℚ(i) ⊂ ℚ(ζ_ν) ⟺ 4 | ν. ν = 4 is the unique numerator whose coprime slot set is exactly the forbidden half
(φ(ν) = 2 and 4 | ν). A clean Galois explanation of a known fact; SHARP as a dictionary, no new existence.
