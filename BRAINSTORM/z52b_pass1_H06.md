# z52b Pass 1 — batch H06

1. Batch H06 is complete: 25 items, outcomes in `data/z52b/pass1/outcome_H06.jsonl`. ES remains open.
2. Counts: nothing 15, covered 10, interesting 0, needs-compute 0, skipped 0.
3. Covered (repo already did the step): Z1931, Z1939, Z1961, Z2026, Z2030, Z2045, Z2099, Z2323, Z2343, Z2360.
4. Banked negatives (PROVED or CERTIFIED): Z1930 (rational exradii triangles: none at any p ≡ 1 (4); for n ≤ 3000, exactly when n has a 3 (mod 4) factor or 4 | n), Z2037 (ℤ[1/S]-ES is trivial for every S ≠ ∅), Z1979 (the certificate family is not Presburger), Z2406 (the 2^{−rank} model is blind to T1), Z2345 (ADH-type formulas are too small).
5. No interesting items: the one surprise (Z1930's χ₋₄ split) has a 10-line descent proof and is a dead variant, like Z1931.

## Z1930 — rational triangles with integer exradii and inradius n/4 (banked negative; outcome `nothing`)

Not `interesting` (the surprise resolved into a short proof), but the lemma is worth keeping.

* Every positive triple (X, Y, Z) is the exradius triple of a unique triangle: s² = XY + YZ + ZX, tangent lengths
  s − a = YZ/s etc., inradius r = XYZ/s² (PROVED, standard). So ES(n) ⇔ integer exradii with r = n/4 (rephrasing).
* The triangle is rational (rational sides and area) ⇔ s² = XY + YZ + ZX is a square ⇔ nXYZ is a square (since 4XYZ = n·s²).
* **CERTIFIED** (`scripts/z52b_p1_H06_exradii.c`, `gcc -O2 … -lm; ./a.out 3000 1`; output
  `data/z52b/pass1/H06/exradii_all_n3000.txt`): for 2 ≤ n ≤ 3000, an ES solution with nXYZ = □ exists **iff 4 | n or n has
  a prime factor ≡ 3 (mod 4)** (525 failing n, exact match). The integer-side (Heronian) version additionally fails at 50
  n ≤ 3000 that have a factor ≡ 3 (4) (3, 7, 9, 11, 21, 23, …).
* **PROVED (primes p ≡ 1 (4)).** No ES solution has pXYZ = □.
  Type II (p ∤ X, p | Y, Z): with Y = pgy, Z = pgz, gcd(y, z) = 1, the equation gives (4X − p)g yz = X(y + z), so X = yzk,
  and pXYZ = p³k(gyz)² is a square only if p | k, i.e. p | X — contradiction.
  Type I (X = pX′, p ∤ Y, Z): Y = gy, Z = gz, gcd(y, z) = 1; (4X′ − 1)g yz = pX′(y + z) gives yz | X′, X′ = yzk, and
  pXYZ = (pgyz)²k is a square ⇒ k = t²; then t² | g, g = t²h and **(4t²yz − 1)h = p(y + z)**. Put D = 4t²yz − 1 ≡ 3 (4).
  Since z ≡ −y (mod y + z), gcd(D, y + z) divides (2ty)² + 1, whose prime factors are all ≡ 1 (4); so D = dD′ with
  d ≡ 1 (4), D′ | p and D′ ≡ 3 (4). Hence D′ = p ≡ 3 (4). ∎
  Same mechanism as the altitude variant Z1931: a positivity/sum-of-two-squares constraint that is χ₋₄-sensitive. Dead
  variant at all hard primes; no depth lane.

## Other short negatives worth keeping (outcome `nothing`)

* **Z2037 (PROVED).** For any prime q, 4/n = 1/(an/q) + 1/(bn/q) + 1/(cn/q) whenever 4/q = 1/a + 1/b + 1/c. So ES over
  ℤ[1/S] is trivial for every S ≠ ∅; the S-integral ladder has no intermediate rung.
* **Z1979 (PROVED, relative to Woods' theorem).** Woods' theorem says parametric Presburger counts are eventually
  quasi-polynomial. So if S_n = {(u,B,C) : 4uBC − u − B = n} were parametric-Presburger, R(n) would be a quasi-polynomial;
  R(n) ≤ n^{o(1)} then forces it to be bounded. But R is unbounded (FRONTIER §2.2 Prop 3.1). Hence Barvinok short
  generating functions cannot carry p as a parameter.
* **Z2406 (EVIDENCE).** The F₂-rank of the squarefree kernels of A = tu − 1 over the words of n is essentially full,
  with similar sizes at primes and at odd squares. At 41², 59², 101² and 257² the rank is 20, 22, 19 and 39, yet N₋ = 0
  is certain by T1. So the random-multiplicative 2^{−rank} model does not see reciprocity.
  Reproduce: `uv run --with sympy python scripts/z52b_p1_H06_f2rank.py 409 1681 …`.
* **Z2345 (EVIDENCE).** Mean |N₊ − N₋|(p) ≈ 0.26–0.30·log²p (samples near 10³, 10⁴ and 10⁵). An ADH-type
  Hecke-character sum over ideals of norm Ap + B in a fixed quadratic field has O(1) mean over primes, so it is too
  small to match.
* **Z2025 (EVIDENCE).** In the dispersion run over C ≤ X (`scripts/z52b_p1_H06_dispersion.py`), Disp saturates at
  small C while M_X grows only like log X. So X·Disp/M_X² ≥ 0.4 at best, and the ratio grows with X.
