# z8_exp_near_square_cover — ES on exponential near-squares n = c₀·4^s + k by exponent coverings (O232)

**Idea.** n = m² + k with m = 2^s: the polynomial family m² + k cannot be covered by polynomial families in m when
k ≡ 0, 1, 5 (mod 8) (NEAR_SQUARE Thm 2.2, Z_k^□ ≠ ∅), but the exponential subfamily has a *coupled* parameter space
(EXPONENT_COVERING Prop 2.2), so finite exponent coverings may exist.

**Literature.** EXPONENT_COVERING §5.4 (no prior "ES for all k·2^m + 1"); Sierpiński/Erdős covering systems; Bertók–Hajdu
(Math. Comp. 2016, arXiv:1407.6499) for the exponential local–global principle. Nothing found on ES for 4^s + k.

**Barrier screen.** B1: not violated — its product-structure hypothesis is absent (coupled exponents). T1/B5: integer
unit-square points do not exist for c₀ = 1, k ≥ 3 odd (SIGN_FIELDS Lemma 1.2), so the (J)22 Cor 1.5 obstruction never
fires; non-unit square points (4^ℓ + k = s², 1 + k4^a = s²) only raise the cost. B2/B3/B6: irrelevant (finite covering
of a sparse family; says nothing about generic primes).

**Cheap numerics.** `scripts/z8_expnear_survey.py`, `z8_expnear_cert.py`: k ≤ 300, c₀ = 1: 13 non-trivial offsets
(k ≡ 9 mod 24), 9 certified (k = 9, 57, 81, 129, 153, 177, 201, 225, 249; data/z8/), 4 OPEN (33, 105, 273, 297), every
OPEN k has an integer non-unit square point.

**Assessment.** PROVED (computer-assisted, certificates checked): ES for all 4^s + k, k in the list. Modest: these are
sparse families, and the novelty is that they are near-square families provably out of reach of polynomial families in m.
They do not touch the hard core (B1/B5).
