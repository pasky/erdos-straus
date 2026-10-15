# z18_rung2_positivity — the D = 2 rung is sterile at unit-square points, for an archimedean reason (O245)

## Idea
Root menus Y = 2^{s/2} for c₀·2^s + k (i.e. Y = 2^t for c₀·4^t + k) give n = c₀Y² + k, positive definite. NEAR_SQUARE Thm 2.2
showed families above the squares are non-escaping; transplant the shape analysis.
## Result (MENU_LADDER Theorem 4.1, PROVED for Type II)
Every Type II polynomial family on c₀Y² + k (c₀, k > 0) has witness ≡ rational constant (mod n): the five degree shapes of
(a, b, d) are either "constant-witness" or killed by positivity at a real root of a or m. At a unit-square point the
Kronecker character is +1, so no Type II root family of degree 2 reaches μ = 0. Type I: (0,0,2) verbatim, (1,0,1) open.
Not a T1 effect: Y* is not in the closure of the Pell points (`scripts/z18_pell.py`, mod 17 parity), and not a descent
effect (z18_descent_dies_at_D2).
## Literature
NEAR_SQUARE Thm 2.2; ET 2013 Lemma 2.8 (degree count).
## Barrier screen
B1-type statement for one rung; explains why O239's 4^r + t windows (D = 2 in base 4 without Aurifeuille) could not reach
μ = 0 for c₀ ≡ 7 (8).
## Cheap numerics
`z18_crt.py 15 1 2 …`: 0 hits in 1128 Type I/II shapes, consistent.
## Assessment
PROVED (Type II). The rung-2 obstruction is a fourth kind (positivity), beside Schinzel, descent and magnitude. SHARP-ish.
