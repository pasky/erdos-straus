# z35_gaussian_menus_closed — "identities in a, b" are already closed; the √−1 lift menu is T1-barred on whole classes (O265)

## Idea
Brief goal (3): a, b (p = a² + b²) are canonical but not polynomial in p, so maybe identities in (a, b) — levels d, windows,
side numbers p + 4b² = a² + 5b², p + 4ab, … — escape (J)78/(J)79/(J)84. Also try the non-polynomial lift X ≡ i_p (mod p),
X² + 1 = pN, which moves with X ↦ X + tp.

## Literature
POINTWISE_BINARYFORM Thm 3.2/3.2′, Cor 3.4 ((J)3: polynomial/rational families in the norm-form variables fail on every square
class); (J)78 Thm 1.1 (Type II valid at one point ⟹ in ℚ[Q]); (J)79 Cor 3.2 (any full norm form, any degree, Type I too);
s7_gaussian_square_windows (Gaussian K = S² windows, random rate).

## Barrier screen
The cited theorems are stated in the variables (a, b) themselves, so the premise is wrong for polynomial choices
(MODP_RECIPROCITY §3.1). For the √−1 menu, Prop 3.3: in the class n ≡ 1 (mod M), points (X, N) with n = (X² + 1)/N an odd square
exist (s ≡ 1 (4M) prime, X² ≡ −1 (mod s²)), so no polynomial family in (X, N) is valid on a whole class (T1); restricted domains (sectors,
canonical least lifts) are NOT covered. Sector version
needs equidistribution of roots of X² ≡ −1 (mod s²) (open technical point). Size: forced factorisations of quadratic side
numbers in (a, b) give factors ≍ √p while a witness needs w ≥ 4d − 1 — balanced only at d ≍ √p, where p + 4d = a² + b² + linear
is irreducible.

## Cheap numerics
`scripts/z35_gauss_menu.py 300000` (neighbour-prime controls): no canonical quantity (a, b, a ± b, ab/2, h, k, X₀, N₀) is a
better level than controls (|z| ≤ 3.6, naive variance, correlated controls); windows: a and ab/2 sterile, b and |a − b| mildly enhanced (Jacobi redistribution).
Caution recorded: shifted controls m ± j produce spurious z ≈ 13.

## Assessment
PROVED (premise correction by citation; Prop 3.3) + EVIDENCE. Polynomial Gaussian certificates are closed; only non-polynomial
arithmetic use remains, and its observed effect is the Jacobi selection rule of z35_anti_windows.
