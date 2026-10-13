# bsG_modular_hyperbola — (W) as points of aā ≡ 1 (mod n) with quotient dividing both shifts; Kloosterman screen (O180)

## Idea
(F4) of LORENZINI_W: (W)(n) ⟺ ∃ a with ā = a⁻¹ mod n, b = (aā − 1)/n ≥ 2, b | a + 1, b | ā + 1, a, ā ≥ 2b − 1. Equivalently the matrix
[[a, b],[n, ā]] ∈ SL₂(Z) lies in −Γ¹(b), with top-right entry exactly b. Count the points by completing the conditions with additive characters mod b
and the hyperbola in boxes, i.e. Kloosterman sums S(·,·; n) and the divisor problem for bn + 1.

## Findings
* For fixed b the condition is "bn + 1 = XZ with X ≡ Z ≡ −1 (b)". The count is (1/φ(b)) Σ_χ χ(−1) Σ_{X | bn+1} χ(X) restricted to the box.
  The main term is ≍ τ(bn+1)/φ(b). Summed over b ≤ n this gives ≍ log² n: the mean 0.45 log² n of §2.
* Non-principal χ contributions are (1 ∗ χ)(bn + 1) with box truncation. For real χ these are ≥ 0 counts of ideals, which is the origin of the square shadow
  (χ_{−b} at n = m²). For complex χ there is no sign control.
* Weil/Kloosterman bounds control box-counts of the hyperbola mod n with error ≍ n^{1/2+ε}, against a main term ≍ log² n: the same p^{1/2} gap as
  PARITY_FIXED_P's R(p) (B3).

## Literature
Kloosterman/Weil. Shparlinski's survey on the modular hyperbola. Duke–Friedlander–Iwaniec (bilinear Kloosterman fractions). PARITY_FIXED_P.md.

## Barrier screen
B3 (main term ≤ n^{o(1)}, errors ≥ n^{1/2}). B6 (averaging over n gives density statements only).

## Assessment
Dictionary + standard screen. Dead for pointwise use. Promise 0.
