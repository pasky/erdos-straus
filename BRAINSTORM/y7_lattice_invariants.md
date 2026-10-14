# y7_lattice_invariants — no lattice invariant of the path form sees 7's slices (O215, goal (a))

## Idea
(J)33: S₄(w) ⟺ Q_w is ℚ₂-isotropic, a genus invariant of the path form Q_w (Gram [[v,−1,0],[−1,t,−1],[0,−1,u]],
det n). A "7-adic analogue of (J)33" would be some invariant of the unmarked lattice Q_w (Hasse invariant, genus,
spinor genus, or at worst the ℤ-isometry class) that decides S₇(w). Test the weakest version: is S_M(w) a function
of the ℤ-isometry class of Q_w?

## Why the quadratic versions are dead a priori (PROVED, from CHI_FLIP Thm 1.1 and FOUR_SPECIFIC Thm 2.3)
For prime n ∤ 2M, the ℚ-class of Q_w is fixed by det = n, ε_∞ = −1 and ε₂ = −χ(w) (ε_n = χ(w), ε_ℓ = 1 for
ℓ ∤ 2n, including ℓ = 7: L_w ⊗ ℤ₇ is unimodular and isotropic). The genus adds the n-adic square class of A* (i.e.
(A/n)) and, on χ = −1, nothing at 2 (⟨1, −1, −n⟩). So a genus-level description of S₇ would make S₇ a function of
(χ, (A/n)), which O212's y4_seven feature test already refutes (and (J)32 Thm 3.1(c): S₇ has χ = ±1 members). A 7-adic
Hasse invariant of Q_w does not exist as a variable: it is identically 1.

## Computation (`uv run --with cypari2 python scripts/y7_class_test.py 150 4 7 8 11 5`; PARI qfisom, theta series to 60
as pre-filter; all words incl. boundary words, prime n ≤ 150)
| M | isometry classes | classes containing both S_M members and non-members |
|---|---|---|
| 4 | 238 | 0 (control: S₄ = {χ = −1}) |
| 5 | 236 | 56 |
| 7 | 235 | 59 |
| 8 | 238 | 22 |
| 11 | 235 | 33 |
Smallest example for 7: n = 5, the words (1, 2, 7) ∈ S₇ (7 | v) and (2, 1, 6) ∉ S₇ (2, 1, 6, A = 1, A* = 11) have
isometric path forms.

## Reading
**Prop Y7.2 (PROVED by the explicit examples).** For M ∈ {5, 7, 8, 11}, S_M(w) is not a function of the ℤ-isometry class
of Q_w; for M = 4 it is a function of the genus. So the 7-slices are pure *marking* data (which path basis of the
lattice), in exactly the sense FOUR_SPECIFIC Thm 2.3 found for the one-odd/all-even split of 4. There is no
"7-adic (J)33" on the length-3 slices, not even at class level.
(The ℤ-class does see whether *some* marking of it is a 7-slice; that is the original existence question, rewritten.)

## Barrier screen
B2: marking data = which divisor/basis is chosen = the lottery. Theta-series / Siegel–Weil routes (H-F) only see
class or genus data, so they cannot detect S₇ on single words — they could only count markings, which is B3/B6.

## Assessment
PROVED (negative, exact scope: the five length-3 slices, M ∈ {5, 7, 8, 11}; n ≤ 150 suffices for the examples). Kills
O212 spark 1 in its natural form. 7's structure, if any, is not quadratic-form data on HJ words.
