# z35_anti_windows — the exact window law of a representation p = x² + Dy² (O265)

## Idea
A representation is the one place where canonical non-abelian data of p are integers of size ≍ √p — the balanced range of the
b = 1 line (4md = p + g with m, d ≍ √p). Use its coordinates' divisors as windows.

## Literature
(J)84 ("p is a non-square modulo every class modulus 4ab"); ET Prop 1.6; MODP_RECIPROCITY Lemma 3.2, Prop 5.1.

## Barrier screen
Lemma 3.2 (local T1): if p is a unit square modulo the odd part m′ of m (plus a 2-adic condition), window m is sterile.
Prop 5.1: for p = x² + Dy² (or 4p = x² + Dy²), every odd m | y is sterile; odd m | x is sterile when (D/m) = +1 and merely
permitted when (D/m) = −1. So representations FORBID windows and never FORCE one — the χ-shadow as a selection rule. B2 for the
permitted ones. T1: consistent (at squares everything is forbidden).

## Cheap numerics
`scripts/z35_principal_windows.py 1000000`: D = 1, 2, 3, 7: 0 hits on all y-windows (≈ 137 000 trials) and on all x-windows with
(D/x) = +1 (≈ 68 000); 1.75–2.06 % on x-windows with (D/x) = −1 (controls ≈ 1.25 %).

## Assessment
PROVED (exact, elementary) + EVIDENCE. A clean selection rule; not an existence mechanism (≈ τ(x)τ(y) tickets of probability
≍ τ(m + 1)/m ≈ p^{−1/2+o(1)} each).
