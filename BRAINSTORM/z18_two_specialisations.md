# z18_two_specialisations — a root family through μ = 0 is an interpolation between n = 4^J over ℤ[1/2] and n = k over ℤ_(2) (O245)

## Idea
Y = 2^{s/D} → 1 at odd places and → 0 at 2 as s → 0 in Ẑ. A rational-coefficient polynomial R(Y) is integer-valued near μ = 0
iff R(1) ∈ ℤ[1/2] and R(0) ∈ ℤ_(2) (MENU_LADDER Lemma 2.1, PROVED, two lines). So a root family (a, b, c, d) ∈ ℚ[Y]⁴ of
Type II, cn = 4abcd − a − b, reaches μ = 0 iff (i) positive leading coefficients, (ii) its specialisation at Y = 1 is a
ℤ[1/2]-"solution" for n = c₀ + k = 4^J (the member s = 0!) and (iii) its specialisation at Y = 0 is a ℤ_(2)-solution for n = k.
## Literature
Schinzel's polynomial-identity obstruction (ET 2013 §1); EXPONENT_COVERING Thm 1.4 for the profinite parameter space.
## Barrier screen
(ii)–(iii) are never obstructed locally (ℤ[1/2]-solutions of 4/16 with signs, ℤ_(2)-solutions of 4/1 exist), so the whole
difficulty is GLOBAL-ALGEBRAIC: existence of a polynomial identity interpolating the two specialisations. B1: the
dictionary explains Schinzel at D = 1 (the identity is forced to be affine in Y and the two specialisations become one
congruence class).
## Cheap numerics
All z18 searches use exactly this test (`z18_crt.py`, `z18_tt.py`); Theorem B of O240 passes: specialisations
(a,b,c,d)(1) = (3, 5/2, 1/2, 1/2) for n = 4, (a,b,c,d)(0) = (3, 1, 4/11, 1) for n = 1.
## Assessment
PROVED (dictionary). Useful normal form for any future search; turns "reach μ = 0" into a two-point interpolation problem.
